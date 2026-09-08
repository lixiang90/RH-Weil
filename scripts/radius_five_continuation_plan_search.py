"""E only: enrich a finite minimum of analytic continuation plans."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import differential_evolution

from radius_five_analytic_bellman_extension import Extension
from radius_five_subaction_grid import exact_profile_as_float

ROOT = Path(__file__).resolve().parents[1]


class Plans:
    def __init__(self, kernel, alpha, eta, margin):
        self.kernel, self.alpha, self.eta, self.margin = kernel, alpha, eta, margin
        self.items = [dict(gaps=[], offset=0.)]
        self.by_key = {((), 0.): 0}
        x = np.linspace(0., 640., 320001)
        self.fast = CubicSpline(x, kernel(x), extrapolate=False)
        self.groups = None

    def add(self, gaps, offset):
        key = (tuple(map(float, gaps)), float(offset))
        if key not in self.by_key:
            self.by_key[key] = len(self.items)
            self.items.append(dict(gaps=list(key[0]), offset=key[1]))
            self.groups = None
        return self.by_key[key]

    def build(self):
        self.groups = {}
        for m in range(1, 5):
            ids = np.array([i for i, p in enumerate(self.items) if len(p["gaps"]) == m])
            if len(ids):
                paths = np.array([self.items[i]["gaps"] for i in ids])
                offsets = np.array([self.items[i]["offset"] for i in ids])
                prefix = np.cumsum(paths, axis=1)
                unique = [np.unique(prefix[:, j], return_inverse=True) for j in range(m)]
                self.groups[m] = (ids, offsets, unique)

    def value(self, states, exact=False):
        if self.groups is None:
            self.build()
        kernel = self.kernel if exact else self.fast
        states = np.atleast_2d(states)
        all_best, all_ids = [], []
        for low in range(0, len(states), 64):
            s = states[low:low+64]
            suffix = np.flip(np.cumsum(np.flip(s, axis=1), axis=1), axis=1)
            best, choice = np.zeros(len(s)), np.zeros(len(s), dtype=int)
            internal = np.zeros(len(s))
            for m in range(1, 5):
                internal += (self.eta*s[:, m-1]/(2*np.pi)-self.alpha-self.margin
                             +2*np.sum(kernel(np.cumsum(s[:, m-1:], axis=1))**2, axis=1))
                if m not in self.groups:
                    continue
                ids, offsets, unique = self.groups[m]
                values = internal[:, None]+offsets[None, :]
                for j in range(m):
                    prefixes, inverse = unique[j]
                    for i in range(j, m):
                        values += 2*kernel(suffix[:, i, None]+prefixes[None, :])[:, inverse]**2
                which = np.argmin(values, axis=1)
                candidate = values[np.arange(len(s)), which]
                improved = candidate < best
                best[improved] = candidate[improved]
                choice[improved] = ids[which[improved]]
            all_best.extend(best.tolist())
            all_ids.extend(choice.tolist())
        return np.array(all_best), np.array(all_ids)

    def cost(self, words, exact=False):
        kernel = self.kernel if exact else self.fast
        return (2*np.sum(kernel(np.cumsum(words, axis=1))**2, axis=1)
                +self.eta*words[:, 0]/(2*np.pi)-self.alpha)

    def residual(self, words, exact=False):
        return self.cost(words, exact)+self.value(words[:, 1:], exact)[0]-self.value(words[:, :4], exact)[0]

    def extend(self, transition, tail_id):
        previous = self.items[int(tail_id)]
        gaps, offset = [float(transition[-1])]+previous["gaps"], previous["offset"]
        if len(gaps) == 5:
            offset += float(self.cost(np.array(gaps)[None, :], exact=True)[0])-self.margin
            gaps = gaps[:4]
        return self.add(gaps, offset)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--iterations", type=int, default=8)
    args = parser.parse_args()
    assert args.iterations > 0
    source = json.loads((ROOT / "reviews/2026-09-08/radius-five-subaction-grid.json").read_text())
    kernel, alpha, eta = exact_profile_as_float()
    profile_hash = hashlib.sha256((ROOT / "reviews/2026-09-08/radius-five-rational-profile-candidate.json").read_bytes()).hexdigest()
    grid = np.array(source["grid"])
    output_path = ROOT / "reviews/2026-09-08/radius-five-continuation-plan-search.json"
    if args.resume:
        prior = json.loads(output_path.read_text())
        assert prior["alpha"] == alpha and prior["eta"] == eta
        # The legacy 8+24 batch was independently bound to this exact profile.
        legacy_hash = "3a89799a5705cc8c30c629643f32d72ee000c34bf67798510d6bfdd8575bdca0"
        assert profile_hash == prior.get("profile_sha256", legacy_hash), "Profile changed"
        margin = prior["margin"]
        plans = Plans(kernel, alpha, eta, margin)
        for item in prior["plans"][1:]:
            plans.add(item["gaps"], item["offset"])
        assert plans.items == prior["plans"]
        history, initial_count = prior["history"], prior["initial_count"]
        batches = prior.get("search_batches", [dict(start=0, iterations=len(history),
                                                   seed=570128, initial_sampling=True)])
        seed = 570128+1000*len(history)
        rng = np.random.default_rng(seed)
    else:
        ext = Extension(kernel, grid, alpha, eta)
        margin = ext.margin
        seed = 570128
        rng = np.random.default_rng(seed)
        states = np.r_[rng.choice(grid, (1000, 4)),
                       np.clip(rng.choice(grid[:-1], (1000, 4))
                               +rng.normal(0, .35, (1000, 4)), 5.7, 80),
                       rng.uniform(5.7, 80, (1000, 4))]
        _, winners = ext.value(states, return_paths=True)
        plans = Plans(kernel, alpha, eta, margin)
        for path in winners:
            if not path:
                continue
            offset = 0.
            if len(path) == 4:
                digits = [int(np.where(grid == v)[0][0]) for v in path]
                offset = float(ext.h[np.array(digits) @ len(grid)**np.arange(3, -1, -1)])
            plans.add(path, offset)
        initial_count, history, batches = len(plans.items), [], []
    start = len(history)
    batches.append(dict(start=start, iterations_requested=args.iterations,
                        iterations_completed=0, seed=seed,
                        initial_sampling=not args.resume))
    print("Initial selected plans", initial_count, flush=True)
    for iteration in range(start, start+args.iterations):
        core = np.clip(rng.choice(grid[:-1], (3000, 5))
                       +rng.normal(0, .5, (3000, 5)), 5.7, 128)
        broad = rng.uniform(5.7, 128, (1000, 5))
        words = np.r_[core, broad]
        values = plans.residual(words)
        selected = np.argsort(values)[:60]
        bad_words = list(words[selected[values[selected] < 0]])
        cuts = []

        def objective(v):
            ar = np.asarray(v)
            g = ar[None, :] if ar.ndim == 1 else ar.T
            value = plans.residual(g)
            return float(value[0]) if ar.ndim == 1 else value

        for upper in (13.5, 21., 128.):
            found = differential_evolution(
                objective, [(5.7, upper)]*5, seed=1900+31*iteration+int(upper),
                popsize=6, maxiter=110, vectorized=True, updating="deferred", polish=False)
            # Re-evaluate the minimum over every selected plan with the original
            # kernel. This is still floating arithmetic, not interval proof.
            exact_value = float(plans.residual(found.x[None, :], exact=True)[0])
            cuts.append(dict(upper=upper, gaps=list(map(float, found.x)),
                             spline_residual=float(found.fun), original_kernel_residual=exact_value,
                             search_success=bool(found.success)))
            if found.fun < 0:
                bad_words.append(found.x.copy())
        D = alpha+margin-eta*5.7/(2*np.pi)
        lower = min(p["offset"]-len(p["gaps"])*D for p in plans.items)
        entry = dict(iteration=iteration, plans_before_update=len(plans.items),
                     sample_min=float(values.min()), cuts=cuts,
                     analytic_height_formula_float=-lower)
        history.append(entry)
        print(f"iteration={iteration}, plans={len(plans.items)}, sample={values.min():+.5e}, "
              f"DE={min(c['original_kernel_residual'] for c in cuts):+.5e}, "
              f"height bound~{-lower:.6g}", flush=True)
        additions = []
        if bad_words:
            bad = np.array(bad_words)
            _, tail_ids = plans.value(bad[:, 1:])
            for g, tail_id in zip(bad, tail_ids):
                additions.append(plans.extend(g, tail_id))
        entry["added_or_existing_plan_ids"] = additions
        batches[-1]["iterations_completed"] = iteration-start+1
        output = dict(status="E only: finite analytic plan candidates; no global subaction",
                      alpha=alpha, eta=eta, margin=margin, initial_count=initial_count,
                      profile_sha256=profile_hash,
                      search_batches=batches,
                      domain=[5.7, 128], spline_step=.002, spline_domain=[0, 640],
                      history=history, plans=plans.items,
                      indexing="history candidate uses plans[:plans_before_update]",
                      scope="Updates use true-kernel floating costs; global verification and rigorous rounding remain open")
        output_path.write_text(
            json.dumps(output, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()

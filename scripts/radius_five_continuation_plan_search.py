"""E only: enrich a finite minimum of analytic continuation plans."""

from __future__ import annotations

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
    source = json.loads((ROOT / "reviews/2026-09-08/radius-five-subaction-grid.json").read_text())
    kernel, alpha, eta = exact_profile_as_float()
    grid = np.array(source["grid"])
    ext = Extension(kernel, grid, alpha, eta)
    rng = np.random.default_rng(570128)
    states = np.r_[rng.choice(grid, (1000, 4)),
                   np.clip(rng.choice(grid[:-1], (1000, 4))
                           +rng.normal(0, .35, (1000, 4)), 5.7, 80),
                   rng.uniform(5.7, 80, (1000, 4))]
    _, winners = ext.value(states, return_paths=True)
    plans = Plans(kernel, alpha, eta, ext.margin)
    for path in winners:
        if not path:
            continue
        offset = 0.
        if len(path) == 4:
            digits = [int(np.where(grid == v)[0][0]) for v in path]
            offset = float(ext.h[np.array(digits) @ len(grid)**np.arange(3, -1, -1)])
        plans.add(path, offset)
    initial_count = len(plans.items)
    print("Initial selected plans", initial_count, flush=True)
    history = []
    for iteration in range(8):
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
        D = alpha+ext.margin-eta*5.7/(2*np.pi)
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
        output = dict(status="E only: finite analytic plan candidates; no global subaction",
                      alpha=alpha, eta=eta, margin=ext.margin, initial_count=initial_count,
                      domain=[5.7, 128], spline_step=.002, spline_domain=[0, 640],
                      history=history, plans=plans.items,
                      indexing="history candidate uses plans[:plans_before_update]",
                      scope="Updates use true-kernel floating costs; global verification and rigorous rounding remain open")
        (ROOT / "reviews/2026-09-08/radius-five-continuation-plan-search.json").write_text(
            json.dumps(output, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()

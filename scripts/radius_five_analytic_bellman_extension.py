"""E: analytic finite-continuation extension of a discrete subaction.

Spline evaluations accelerate candidate search only. Selected paths can be
recomputed with the original 90-term kernel. No continuous certificate.
"""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import differential_evolution

from radius_five_subaction_grid import exact_profile_as_float

ROOT = Path(__file__).resolve().parents[1]


class Extension:
    def __init__(self, kernel, grid, alpha, eta, margin=1e-5):
        self.kernel = kernel
        self.grid, self.alpha, self.eta, self.margin = grid, alpha, eta, margin
        self.q = len(grid)
        self.future = {m: np.array(list(product(grid, repeat=m)))
                       for m in range(1, 5)}
        self.prefix = {m: self.future[m].sum(axis=1) for m in range(1, 5)}
        edges = np.array(list(product(grid, repeat=5)))
        sums = np.cumsum(edges, axis=1)
        u, inv = np.unique(sums, return_inverse=True)
        costs = (2*np.sum(kernel(u)[inv].reshape(sums.shape)**2, axis=1)
                 +eta*edges[:, 0]/(2*np.pi)-alpha-margin)
        tail = np.arange(self.q**5) % self.q**4
        h = np.zeros(self.q**4)
        for step in range(1000):
            new = np.minimum(0, (costs+h[tail]).reshape(-1, self.q).min(axis=1))
            change = np.max(abs(new-h))
            h = new
            if change < 1e-13:
                break
        else:
            raise RuntimeError("Discrete iteration did not stabilize")
        self.h = h
        self.discrete_record = dict(iterations=step+1, final_change=float(change),
                                    oscillation=float(np.ptp(h)),
                                    grid_residual=float(np.min(
                                        costs+margin+h[tail]-h[np.arange(self.q**5)//self.q])))
        x = np.linspace(0., 400., 200001)
        self.fast_kernel = CubicSpline(x, kernel(x), extrapolate=False)
        print("Discrete Bellman", self.discrete_record, flush=True)

    def value(self, states, exact=False, return_paths=False):
        states = np.atleast_2d(states)
        assert np.all(states >= self.grid[0]) and np.all(states <= self.grid[-1])
        kernel = self.kernel if exact else self.fast_kernel
        result, path_result = [], []
        for low in range(0, len(states), 24):
            s = states[low:low+24]
            suffix = np.flip(np.cumsum(np.flip(s, axis=1), axis=1), axis=1)
            internal = np.zeros(len(s))
            best = np.zeros(len(s))
            paths = [[] for _ in s]
            for m in range(1, 5):
                # The first m anchors pay only their own original gap and all
                # forward edges contained in the initial four-gap state.
                internal += (self.eta*s[:, m-1]/(2*np.pi)-self.alpha-self.margin
                             +2*np.sum(kernel(np.cumsum(s[:, m-1:], axis=1))**2, axis=1))
                values = np.repeat(internal[:, None], self.q**m, axis=1)
                if m == 4:
                    values += self.h[None, :]
                # Cross-boundary edges: anchor i uses j future gaps iff j<=i+1.
                for j in range(1, m+1):
                    partial = np.zeros((len(s), self.q**j))
                    for i in range(j-1, m):
                        partial += 2*kernel(suffix[:, i, None]+self.prefix[j][None, :])**2
                    values += np.repeat(partial, self.q**(m-j), axis=1)
                argmin = np.argmin(values, axis=1)
                current = values[np.arange(len(s)), argmin]
                for idx in np.flatnonzero(current < best):
                    paths[idx] = list(map(float, self.future[m][argmin[idx]]))
                best = np.minimum(best, current)
            result.extend(best.tolist())
            path_result.extend(paths)
        answer = np.array(result)
        return (answer, path_result) if return_paths else answer

    def path_value(self, state, path):
        if not path:
            return 0.
        g = np.r_[state, path]
        m = len(path)
        value = 0.
        for i in range(m):
            value += (2*np.sum(self.kernel(np.cumsum(g[i:i+5]))**2)
                      +self.eta*g[i]/(2*np.pi)-self.alpha-self.margin)
        if m == 4:
            indices = [int(np.where(self.grid == p)[0][0]) for p in path]
            value += self.h[np.array(indices) @ self.q**np.arange(3, -1, -1)]
        return float(value)


def main():
    source = json.loads((ROOT / "reviews/2026-09-08/radius-five-subaction-grid.json").read_text())
    kernel, alpha, eta = exact_profile_as_float()
    ext = Extension(kernel, np.array(source["grid"]), alpha, eta)
    # Agreement with the exact finite graph at selected states.
    rng = np.random.default_rng(906)
    states = np.array(list(product(ext.grid, repeat=4)))
    sample = rng.choice(len(states), 300, replace=False)
    agreement = float(np.max(abs(ext.value(states[sample])-ext.h[sample])))
    print("grid extension discrepancy", agreement, flush=True)

    def objective(v):
        ar = np.asarray(v)
        words = ar[None, :] if ar.ndim == 1 else ar.T
        result = (2*np.sum(ext.fast_kernel(np.cumsum(words, axis=1))**2, axis=1)
                  +eta*words[:, 0]/(2*np.pi)-alpha
                  +ext.value(words[:, 1:])-ext.value(words[:, :4]))
        return float(result[0]) if ar.ndim == 1 else result

    cuts = []
    for upper in (13.5, 21., 80.):
        found = differential_evolution(
            objective, [(5.7, min(29.2, upper))]+[(5.7, upper)]*4,
            seed=190+int(upper), popsize=6, maxiter=90,
            vectorized=True, updating="deferred", polish=False)
        head, hp = ext.value(found.x[:4], return_paths=True)
        tail, tp = ext.value(found.x[1:], return_paths=True)
        path_residual = (2*np.sum(kernel(np.cumsum(found.x))**2)
                         +eta*found.x[0]/(2*np.pi)-alpha
                         +ext.path_value(found.x[1:], tp[0])
                         -ext.path_value(found.x[:4], hp[0]))
        item = dict(upper=upper, gaps=list(map(float, found.x)),
                    spline_residual=float(found.fun), selected_path_residual=float(path_residual),
                    head_path=hp[0], tail_path=tp[0], optimizer_success=bool(found.success))
        cuts.append(item)
        print(item, flush=True)
        output = dict(status="E only: finite-continuation candidate, no all-real certificate",
                      discrete_record=ext.discrete_record, grid=list(map(float, ext.grid)),
                      margin=ext.margin, terminal_values=list(map(float, ext.h)),
                      grid_agreement_sample=agreement, sample_count=len(sample),
                      spline_step=.002, spline_domain=[0, 400], cuts=cuts,
                      caution="The original kernel checks selected paths, not their global minimum; spline errors are not certified")
        (ROOT / "reviews/2026-09-08/radius-five-analytic-bellman-extension.json").write_text(
            json.dumps(output, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()

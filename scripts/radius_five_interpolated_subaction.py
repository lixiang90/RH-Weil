"""E only: adversarial fitting of a multilinear four-gap subaction."""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, linprog
from scipy.sparse import coo_matrix

from radius_five_subaction_grid import exact_profile_as_float

ROOT = Path(__file__).resolve().parents[1]


def interpolation(state, grid):
    state = np.atleast_2d(state)
    q = len(grid)
    left = np.clip(np.searchsorted(grid, state, side="right")-1, 0, q-2)
    fraction = (state-grid[left])/(grid[left+1]-grid[left])
    assert np.all(fraction >= -1e-12) and np.all(fraction <= 1+1e-12)
    indices, weights = [], []
    for bits in product((0, 1), repeat=4):
        bit = np.array(bits)
        index = (left+bit) @ (q**np.arange(3, -1, -1))
        weight = np.prod(np.where(bit, fraction, 1-fraction), axis=1)
        indices.append(index)
        weights.append(weight)
    return np.array(indices).T, np.array(weights).T


def coboundary(words, grid, h):
    ih, wh = interpolation(words[:, :4], grid)
    it, wt = interpolation(words[:, 1:], grid)
    return np.sum(h[it]*wt-h[ih]*wh, axis=1)


def fit_words(words, costs, grid):
    n, q = len(words), len(grid)
    ih, wh = interpolation(words[:, :4], grid)
    it, wt = interpolation(words[:, 1:], grid)
    matrix = coo_matrix(
        (np.r_[wh.ravel(), -wt.ravel(), np.ones(n)],
         (np.r_[np.repeat(np.arange(n), 16), np.repeat(np.arange(n), 16), np.arange(n)],
          np.r_[ih.ravel(), it.ravel(), np.full(n, q**4)])),
        shape=(n, q**4+1)).tocsr()
    matrix.eliminate_zeros()
    fit = linprog(np.r_[np.zeros(q**4), -1.], A_ub=matrix, b_ub=costs,
                  bounds=[(0, .01)]*q**4+[(None, None)], method="highs",
                  options={"primal_feasibility_tolerance": 1e-9,
                           "dual_feasibility_tolerance": 1e-9,
                           "time_limit": 180.})
    if not fit.success:
        raise RuntimeError(fit.message)
    return fit.x[:-1], float(fit.x[-1])


def main():
    source = json.loads((ROOT / "reviews/2026-09-08/radius-five-subaction-grid.json").read_text())
    grid = np.array(source["grid"])
    h = np.array(source["h"])
    kernel, alpha, eta = exact_profile_as_float()
    q = len(grid)
    indices = np.arange(q**5)
    words = grid[np.column_stack([(indices//q**j) % q for j in range(4, -1, -1)])]

    def cost(g):
        sums = np.cumsum(g, axis=1)
        return 2*np.sum(kernel(sums)**2, axis=1)+eta*g[:, 0]/(2*np.pi)-alpha

    costs = cost(words)
    rng = np.random.default_rng(20260908)
    history = []
    cuts = []
    for iteration in range(4):
        # Both core gaps and the entire compact domain are sampled.
        jitter = np.clip(rng.choice(grid[:-1], size=(2500, 5))
                         +rng.uniform(-.3, .3, size=(2500, 5)), grid[0], grid[-1])
        broad = rng.uniform(grid[0], grid[-1], size=(1000, 5))
        extra = np.r_[jitter, broad]
        words, costs = np.r_[words, extra], np.r_[costs, cost(extra)]
        try:
            h, margin = fit_words(words, costs, grid)
        except RuntimeError as exc:
            output = dict(status="E only: run stopped before the next fit completed",
                          grid=list(map(float, grid)), alpha=alpha, eta=eta,
                          interpolation="continuous multilinear tensor interpolation",
                          height_bound=.01, history=history,
                          termination=dict(attempted_iteration=iteration, reason=str(exc),
                                           completed_iterations=len(history)),
                          scope="Solver failure is not a mathematical infeasibility certificate")
            (ROOT / "reviews/2026-09-08/radius-five-interpolated-subaction.json").write_text(
                json.dumps(output, indent=2)+"\n", encoding="utf-8")
            print(output["termination"], flush=True)
            return
        sample_residual = costs+coboundary(words, grid, h)
        print(f"round {iteration}: rows={len(words)}, margin={margin:+.8e}", flush=True)

        def objective(v):
            ar = np.asarray(v)
            g = ar[None, :] if ar.ndim == 1 else ar.T
            value = cost(g)+coboundary(g, grid, h)
            return float(value[0]) if ar.ndim == 1 else value

        round_cuts = []
        for upper in (13.5, 21., 80.):
            for seed in (31, 71):
                bounds = [(5.7, min(29.2, upper))]+[(5.7, upper)]*4
                found = differential_evolution(
                    objective, bounds, seed=seed+100*iteration,
                    popsize=10, maxiter=220, vectorized=True,
                    updating="deferred", polish=True, tol=1e-8)
                item = dict(iteration=iteration, upper=upper, seed=seed,
                            gaps=list(map(float, found.x)),
                            residual=float(found.fun), success=bool(found.success))
                cuts.append(item)
                round_cuts.append(item)
                print(f"  upper={upper:g}, seed={seed}, residual={found.fun:+.8e}", flush=True)
        record = dict(iteration=iteration, rows=len(words), fit_margin=margin,
                      margin_meaning="floating solver output, not a rigorous optimum",
                      recomputed_sample_min=float(sample_residual.min()),
                      oscillation=float(np.ptp(h)), h=list(map(float, h)),
                      cuts=round_cuts)
        history.append(record)
        output = dict(status="E only; floating LP and adversarial searches",
                      grid=list(map(float, grid)), alpha=alpha, eta=eta,
                      interpolation="continuous multilinear tensor interpolation",
                      height_bound=.01, history=history,
                      scope="No whole-domain lower bound, no certified continuous subaction")
        (ROOT / "reviews/2026-09-08/radius-five-interpolated-subaction.json").write_text(
            json.dumps(output, indent=2)+"\n", encoding="utf-8")
        extra = np.array([c["gaps"] for c in round_cuts])
        # Local perturbations supply additional cuts; no exhaustiveness claim.
        extra = np.r_[extra, np.clip(np.repeat(extra, 150, axis=0)
                                    +rng.normal(0, .03, (900, 5)), grid[0], grid[-1])]
        words, costs = np.r_[words, extra], np.r_[costs, cost(extra)]


if __name__ == "__main__":
    main()

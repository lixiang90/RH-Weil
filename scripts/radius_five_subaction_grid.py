"""E only: finite-alphabet subaction LP for the exact profile of note 354.

Every word over the selected alphabet is included, even symbol repetitions.
Feasibility on this finite graph is not a continuous-domain certificate.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

from spectral_four_point_prefilter import mt_kernel

ROOT = Path(__file__).resolve().parents[1]


def exact_profile_as_float():
    source = ROOT / "reviews/2026-09-08/radius-five-rational-profile-candidate.json"
    record = json.loads(source.read_text())
    t = np.array([float(v["t"]) for v in record["terms"]])
    y = np.array([float(v["y"]) for v in record["terms"]])
    z = y*t*t/(t*t-2)
    sinc = lambda x: np.sinc(x/(2*np.pi))
    A = 1 - z @ sinc(t)

    def kernel(x):
        x = np.asarray(x)
        shape = x.shape
        flat = x.ravel()
        out = np.empty(len(flat))
        for lo in range(0, len(flat), 2000):
            v = flat[lo:lo+2000]
            J = (sinc(v[:, None]-t)+sinc(v[:, None]+t))/2
            out[lo:lo+len(v)] = A*mt_kernel(v)+J@z
        return out.reshape(shape)

    return kernel, float(record["alpha"]), float(record["eta"])


def main():
    kernel, alpha, eta = exact_profile_as_float()
    # Deliberately coarse: state values are candidate data, never interpolated
    # into a certificate without a separate error/whole-domain proof.
    grid = np.array([5.7, 6.43, 6.52, 6.56, 6.60, 12.34, 12.43, 12.52, 18.41, 80.])
    q = len(grid)
    edges = np.arange(q**5)
    digits = np.column_stack([(edges//q**j) % q for j in range(4, -1, -1)])
    words = grid[digits]
    sums = np.cumsum(words, axis=1)
    values, inverse = np.unique(sums, return_inverse=True)
    kernels = kernel(values)[inverse].reshape(sums.shape)
    cost = 2*np.sum(kernels**2, axis=1)+eta*words[:, 0]/(2*np.pi)-alpha
    head, tail = edges//q, edges % q**4
    # h(head)-h(tail)+margin <= cost.
    rows = np.tile(edges, 3)
    cols = np.r_[head, tail, np.full(len(edges), q**4)]
    vals = np.r_[np.ones(len(edges)), -np.ones(len(edges)), np.ones(len(edges))]
    constraints = coo_matrix((vals, (rows, cols)), shape=(q**5, q**4+1)).tocsr()
    objective = np.r_[np.zeros(q**4), -1.]
    print(f"LP: {q**4} states, {q**5} edges, {len(values)} distinct distances", flush=True)
    fit = linprog(objective, A_ub=constraints, b_ub=cost,
                  bounds=[(0, .01)]*q**4+[(None, None)], method="highs",
                  options={"primal_feasibility_tolerance": 1e-9,
                           "dual_feasibility_tolerance": 1e-9,
                           "time_limit": 180.})
    print(fit.message, flush=True)
    assert fit.success, fit.message
    h, margin = fit.x[:-1], fit.x[-1]
    residual = cost+h[tail]-h[head]
    worst = int(np.argmin(residual))
    output = dict(status="E only: finite alphabet, floating LP; no all-real subaction",
                  grid=list(map(float, grid)), states=q**4, edges=q**5,
                  alpha=alpha, eta=eta, height_bound=.01,
                  optimum_margin=float(margin),
                  min_recomputed_residual=float(residual[worst]),
                  worst_word=list(map(float, words[worst])),
                  oscillation=float(np.ptp(h)),
                  state_index="base-q digits in chronological order, four gaps",
                  h=list(map(float, h)),
                  open_input="bounded h on all real gaps in the compact domain")
    path = ROOT / "reviews/2026-09-08/radius-five-subaction-grid.json"
    path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print({k: v for k, v in output.items() if k != "h"}, flush=True)


if __name__ == "__main__":
    main()

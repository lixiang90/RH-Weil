"""Exploratory constant-gap constraints for note 347, not a certificate.

Profiles are f_MT +/- epsilon*cos(2*pi*u) with equal weights.  Their mixed
baseline is known exactly in terms of C0 and epsilon; all LP decisions here are
floating point and only prescreen this particular adjacent-edge construction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog


def sinc0(x):
    return np.sinc(np.asarray(x) / np.pi)


def mt_kernel(x):
    beta = math.sqrt(2)
    x = np.asarray(x)
    return (sinc0((x - beta) / 2) + sinc0((x + beta) / 2)) / (2 * sinc0(beta / 2))


def perturbation_kernel(x):
    x = np.asarray(x)
    return (sinc0((x - 2*np.pi) / 2) + sinc0((x + 2*np.pi) / 2)) / 2


def main():
    c0 = 1.5 - 1 / math.sqrt(2) / math.tan(1 / math.sqrt(2))
    cost = .5 - 1 / (4 * math.pi**2)
    roots = [brentq(lambda x: float(mt_kernel(x)), 2*math.pi*n, 2*math.pi*n + 1)
             for n in range(1, 13)]
    grid = np.unique(np.r_[np.linspace(0, 80, 8001), roots])
    a_ub = np.column_stack([np.ones_like(grid), -grid / (2*np.pi)])
    records = []
    for eps in (0, .01, .03, .1, .2, .4, .6, .8):
        # f_MT >= cos(1/sqrt(2))/(sqrt(2)*sin(1/sqrt(2))) > .827,
        # so all these two-profile densities stay positive and have integral 1.
        minimum_density_bound = math.cos(1/math.sqrt(2)) / (
            math.sqrt(2) * math.sin(1/math.sqrt(2))) - eps
        assert minimum_density_bound > 0
        kp, km = mt_kernel(grid) + eps*perturbation_kernel(grid), mt_kernel(grid) - eps*perturbation_kernel(grid)
        dp, dm = np.maximum(1, 2*np.abs(kp)), np.maximum(1, 2*np.abs(km))
        values = kp**2 * (2/dp - 1/dp**2) + km**2 * (2/dm - 1/dm**2)
        baseline = c0 - eps**2 * cost
        for target in (c0, .673399):
            # For any bounded subaction, constant-gap substitution forces
            # alpha <= V(g,g,g) + eta*g/(2*pi). These are necessary only.
            fit = linprog([-target, 1], A_ub=a_ub, b_ub=values,
                          bounds=[(0, 1), (0, baseline)], method="highs")
            assert fit.success, fit.message
            alpha, eta = map(float, fit.x)
            slack = target*alpha - eta - (target - baseline)
            residual = values - a_ub @ fit.x
            tight = np.argsort(residual)[:4]
            row = dict(epsilon=eps, mixed_baseline=baseline, target=target,
                       density_lower_bound=minimum_density_bound,
                       alpha=alpha, eta=eta, best_sampled_target_slack=slack,
                       minimum_constraint_residual=float(residual.min()),
                       near_tight_gaps=[float(grid[i]) for i in tight],
                       interpretation="floating necessary-condition LP only; not feasibility of a subaction")
            records.append(row)
            print(f"eps={eps:.2f}, target={target:.9f}: sampled best slack={slack:+.6e}, "
                  f"alpha={alpha:.3e}, eta={eta:.3e}")
    output = dict(scope="E: selected finite profile family and constant-gap grid; no rigorous exclusion or zero bound",
                  C0=c0, perturbation_cost=cost, mt_roots=roots,
                  constraint_count=len(grid), records=records)
    path = Path(__file__).resolve().parents[1] / "reviews/2026-09-08/spectral-four-point-prefilter.json"
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

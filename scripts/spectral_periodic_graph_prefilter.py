"""Floating necessary conditions for degree-normalized finite-range graphs.

Each period describes an infinite chain; period aliases are distinct vertices.
This is adversarial candidate generation, never a whole-domain certificate.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, linprog

from spectral_four_point_prefilter import mt_kernel

C0 = 1.5 - 1 / math.sqrt(2) / math.tan(1 / math.sqrt(2))
TARGET = .673399


def cosine_kernel(x, mode):
    return (np.sinc((x - 2*np.pi*mode)/(2*np.pi))
            + np.sinc((x + 2*np.pi*mode)/(2*np.pi))) / 2


def periodic_value(gaps, radius, profiles=((1., 0., 0.),)):
    """Return mean potential per vertex; gaps shape (batch, period).

    Profile tuples are (mixture weight, cos(2 pi u) coefficient,
    cos(4 pi u) coefficient), added to MT density.
    """
    gaps = np.atleast_2d(np.asarray(gaps, dtype=float))
    length = gaps.shape[1]
    distances = np.zeros((len(gaps), length))
    forward = []
    for offset in range(radius):
        distances = distances + np.roll(gaps, -offset, axis=1)
        forward.append(distances.copy())
    result = np.zeros(len(gaps))
    for weight, a, b in profiles:
        kernels = [mt_kernel(x) + a*cosine_kernel(x, 1) + b*cosine_kernel(x, 2)
                   for x in forward]
        degrees = np.zeros_like(gaps)
        for r, k in enumerate(kernels, start=1):
            degrees += np.abs(k) + np.roll(np.abs(k), r, axis=1)
        degrees = np.maximum(degrees, 1)
        per_vertex = np.zeros_like(gaps)
        for r, k in enumerate(kernels, start=1):
            product = degrees * np.roll(degrees, -r, axis=1)
            per_vertex += 2*k*k*(2/np.sqrt(product) - 1/product)
        result += weight*np.mean(per_vertex, axis=1)
    return result


def fit_constraints(z, values, baseline, target):
    z, values = np.asarray(z), np.asarray(values)
    fit = linprog([-target, 1],
                  A_ub=np.column_stack([np.ones_like(z), -z]),
                  b_ub=values, bounds=[(0, .99), (0, baseline)], method="highs")
    assert fit.success, fit.message
    alpha, eta = map(float, fit.x)
    return dict(alpha=alpha, eta=eta,
                target_slack=target*alpha-eta-(target-baseline),
                relaxed_output=(baseline-eta)/(1-alpha),
                min_sample_residual=float(np.min(values-alpha+eta*z)))


def main():
    # A finite grid gives only an optimistic necessary-condition relaxation.
    grid = np.linspace(0, 100, 12001)
    rows = []
    for radius in (2, 3, 4, 5):
        z = list(grid/(2*np.pi))
        values = list(periodic_value(grid[:, None], radius))
        fits, cuts = [], []
        for iteration in range(3):
            fit = fit_constraints(z, values, C0, TARGET)
            fits.append(fit)
            eta = fit["eta"]
            print(f"R={radius}, round={iteration}, relaxed output="
                  f"{fit['relaxed_output']:.12f}, slack={fit['target_slack']:+.6e}",
                  flush=True)
            for period in (2, 3, 4, 6, 8):
                def objective(x):
                    # scipy vectorized DE passes shape (period, population).
                    a = np.asarray(x)
                    words = a[None, :] if a.ndim == 1 else a.T
                    out = periodic_value(words, radius) + eta*np.mean(words, axis=1)/(2*np.pi)
                    return float(out[0]) if a.ndim == 1 else out
                found = differential_evolution(
                    objective, [(0, 24)]*period,
                    seed=9000+100*radius+10*iteration+period,
                    popsize=12, maxiter=350, tol=1e-10,
                    vectorized=True, updating="deferred", polish=True)
                word = list(map(float, found.x))
                average_gap = float(np.mean(found.x)/(2*np.pi))
                value = float(periodic_value(found.x, radius)[0])
                residual = value + eta*average_gap - fit["alpha"]
                z.append(average_gap)
                values.append(value)
                cuts.append(dict(iteration=iteration, period=period, gaps=word,
                                 z=average_gap, value=value, residual=residual,
                                 search_success=bool(found.success),
                                 meaning="finite floating point witness; DE success is not global minimality"))
                print(f"  period={period}: residual={residual:+.4e}, "
                      f"mean gap={2*np.pi*average_gap:.5f}", flush=True)
        rows.append(dict(radius=radius, profiles=[[1,0,0]], baseline=C0,
                         target=TARGET, fits=fits, periodic_candidates=cuts,
                         final_fit=fit_constraints(z, values, C0, TARGET)))
    output = dict(
        status="E only; necessary constraints on selected periodic chains",
        scope="No proof of stationary subaction, no certification outside sampled gaps, no actual zero proportion",
        constant_grid=dict(min=0,max=100,count=len(grid)),
        search_box=[0,24], rows=rows)
    path = Path(__file__).resolve().parents[1] / "reviews/2026-09-08/spectral-periodic-graph-prefilter.json"
    path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()

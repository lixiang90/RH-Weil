"""Audit the omitted high-product part of the alternating paired diagonal.

This script checks exact flat-window constants and numerical window integrals.
It does not estimate off-diagonal prime correlations.
"""

from __future__ import annotations

import math
from collections.abc import Callable

import numpy as np
from numpy.polynomial.legendre import leggauss


TOL = 2.0e-11


def flat_window(value: np.ndarray) -> np.ndarray:
    return (np.abs(value) <= 0.5).astype(float)


def mt_window(value: np.ndarray) -> np.ndarray:
    return np.where(
        np.abs(value) <= 0.5,
        np.cos(math.sqrt(2.0) * value),
        0.0,
    )


def gauss_integral(
    function: Callable[[np.ndarray], np.ndarray],
    lower: float,
    upper: float,
    nodes: np.ndarray,
    weights: np.ndarray,
) -> float:
    if upper <= lower:
        return 0.0
    midpoint = 0.5 * (lower + upper)
    half_length = 0.5 * (upper - lower)
    return float(
        half_length * np.dot(weights, function(midpoint + half_length * nodes))
    )


def alternating_overlap_region(
    window: Callable[[np.ndarray], np.ndarray],
    order: int,
    sum_threshold: float | None,
) -> tuple[float, float]:
    """Return raw and mass-normalized A_+ integrals.

    If sum_threshold is None, integrate the full square. Otherwise integrate
    r+s>sum_threshold. Symmetry reduces both domains to r>=s.
    """
    nodes, weights = leggauss(order)
    r_lower = 0.0 if sum_threshold is None else 0.5 * sum_threshold
    r_upper = 1.0
    raw = 0.0

    for base_r, base_r_weight in zip(nodes, weights):
        r = 0.5 * (r_upper - r_lower) * base_r + 0.5 * (
            r_upper + r_lower
        )
        r_weight = 0.5 * (r_upper - r_lower) * base_r_weight
        s_lower = 0.0 if sum_threshold is None else sum_threshold - r
        s_lower = max(0.0, s_lower)
        s_upper = r
        if s_lower >= s_upper:
            continue
        for base_s, base_s_weight in zip(nodes, weights):
            s = 0.5 * (s_upper - s_lower) * base_s + 0.5 * (
                s_upper + s_lower
            )
            s_weight = 0.5 * (s_upper - s_lower) * base_s_weight
            overlap = gauss_integral(
                lambda u: window(u) ** 2 * window(u + r) * window(u + s),
                -0.5,
                0.5 - r,
                nodes,
                weights,
            )
            raw += 2.0 * r_weight * s_weight * r * s * overlap

    mass = gauss_integral(window, -0.5, 0.5, nodes, weights)
    return raw, 4.0 * raw / mass**4


def audit_flat_exact() -> None:
    total_raw, total_normalized = alternating_overlap_region(
        flat_window, 18, None
    )
    tail_raw, tail_normalized = alternating_overlap_region(
        flat_window, 18, 1.0
    )
    assert abs(total_raw - 1.0 / 20.0) <= TOL
    assert abs(total_normalized - 1.0 / 5.0) <= TOL
    assert abs(tail_raw - 1.0 / 32.0) <= TOL
    assert abs(tail_normalized - 1.0 / 8.0) <= TOL
    assert abs(tail_normalized / total_normalized - 5.0 / 8.0) <= TOL
    print(
        "flat high-product tail: raw=1/32, normalized=1/8, "
        "share=5/8"
    )


def audit_mt_tail() -> None:
    coarse_total = alternating_overlap_region(mt_window, 36, None)
    fine_total = alternating_overlap_region(mt_window, 52, None)
    coarse_tail = alternating_overlap_region(mt_window, 36, 1.0)
    fine_tail = alternating_overlap_region(mt_window, 52, 1.0)
    for coarse, fine in zip(coarse_total + coarse_tail, fine_total + fine_tail):
        assert abs(coarse - fine) <= 3.0e-11
    assert fine_tail[1] > 0.0
    assert fine_tail[1] < fine_total[1]
    print(
        "MT alternating diagonal: "
        f"total={fine_total[1]:.12f}, high-tail={fine_tail[1]:.12f}, "
        f"share={fine_tail[1] / fine_total[1]:.12f}"
    )


def audit_moving_cutoff() -> None:
    previous = -1.0
    values: list[float] = []
    for logarithm in (20.0, 50.0, 100.0, 250.0):
        threshold = 1.0 + 2.0 * math.log(logarithm) / logarithm
        _, normalized = alternating_overlap_region(
            mt_window, 40, threshold
        )
        values.append(normalized)
        assert normalized > previous
        previous = normalized
    limiting = alternating_overlap_region(mt_window, 40, 1.0)[1]
    assert values[-1] < limiting
    print(
        "moving XL^2 cutoff MT tails: "
        + ", ".join(f"{value:.9f}" for value in values)
        + f" -> {limiting:.9f}"
    )


def main() -> None:
    audit_flat_exact()
    audit_mt_tail()
    audit_moving_cutoff()
    print("alternating high-product support audits passed")
    print("[scope] window geometry only; no off-diagonal prime estimate")


if __name__ == "__main__":
    main()

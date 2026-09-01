"""Finite audit for the first lower Gabor-boundary prime response.

The script compares its exact height mean square with the diagonal
Montgomery--Vaughan prediction and the limiting constant 1/(4*pi^2).  It uses
actual von Mangoldt prime-power weights and the fixed-width smooth window from
the quarter-turn audit.  Finite values are diagnostics, not asymptotic proofs.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

from adjacent_bulk_edge_audit import prime_power_weights
from boundary_quarter_turn_audit import (
    centered_response_modes,
    window_mass,
)


@dataclass(frozen=True)
class MeanSquareMetrics:
    limit: int
    atom_count: int
    normalized_diagonal: float
    normalized_exact_mean: float
    normalized_off_diagonal: float
    sampled_minimum: float
    sampled_median: float
    sampled_maximum: float


def response_coefficients(limit: int) -> tuple[np.ndarray, np.ndarray, float]:
    length = math.log(limit)
    spacing = 2.0 * math.pi / length
    atoms = prime_power_weights(limit)
    logarithms = np.array([item.log_n for item in atoms], dtype=float)
    centered_mode = np.array(
        [centered_response_modes(item.log_n, length, 1)[1] for item in atoms],
        dtype=float,
    )
    coefficients = np.array(
        [
            -math.sqrt(item.weight) / (2.0 * math.pi)
            for item in atoms
        ],
        dtype=complex,
    )
    coefficients *= centered_mode * np.exp(-0.5j * spacing * logarithms)
    beta = 2.0 * math.pi / (window_mass(length) * length)
    return logarithms, coefficients, beta


def exact_interval_mean_square(
    logarithms: np.ndarray,
    coefficients: np.ndarray,
    left: float,
    right: float,
) -> float:
    length = right - left
    frequency = logarithms[:, None] - logarithms[None, :]
    kernel = np.ones_like(frequency, dtype=complex)
    off_diagonal = frequency != 0.0
    omega = frequency[off_diagonal]
    kernel[off_diagonal] = (
        np.exp(1j * right * omega) - np.exp(1j * left * omega)
    ) / (1j * length * omega)
    coefficient_gram = coefficients[:, None] * coefficients.conj()[None, :]
    result = np.sum(coefficient_gram * kernel)
    assert abs(result.imag) <= 2.0e-10 * max(1.0, abs(result.real))
    return float(result.real)


def metrics(limit: int, sample_count: int) -> MeanSquareMetrics:
    logarithms, coefficients, beta = response_coefficients(limit)
    diagonal = float(np.sum(np.abs(coefficients) ** 2))
    exact_mean = exact_interval_mean_square(
        logarithms, coefficients, float(limit), float(2 * limit)
    )

    heights = np.linspace(float(limit), float(2 * limit), sample_count)
    samples = np.exp(1j * np.outer(heights, logarithms)) @ coefficients
    normalized_samples = beta * np.abs(samples)
    return MeanSquareMetrics(
        limit=limit,
        atom_count=logarithms.size,
        normalized_diagonal=beta**2 * diagonal,
        normalized_exact_mean=beta**2 * exact_mean,
        normalized_off_diagonal=beta**2 * (exact_mean - diagonal),
        sampled_minimum=float(np.min(normalized_samples)),
        sampled_median=float(np.median(normalized_samples)),
        sampled_maximum=float(np.max(normalized_samples)),
    )


def audit(limits: tuple[int, ...], sample_count: int) -> None:
    target = 1.0 / (4.0 * math.pi**2)
    results = [metrics(limit, sample_count) for limit in limits]
    print(f"limiting normalized mean-square constant: {target:.10f}")
    print(
        "X      atoms   beta^2 diagonal   beta^2 exact mean   "
        "beta^2 offdiag   sampled min   sampled median   sampled max"
    )
    for result in results:
        print(
            f"{result.limit:<6d} {result.atom_count:<7d} "
            f"{result.normalized_diagonal:>16.10f} "
            f"{result.normalized_exact_mean:>19.10f} "
            f"{result.normalized_off_diagonal:>16.10f} "
            f"{result.sampled_minimum:>13.8f} "
            f"{result.sampled_median:>16.8f} "
            f"{result.sampled_maximum:>13.8f}"
        )

    assert all(result.normalized_diagonal > 0.0 for result in results)
    assert all(result.normalized_exact_mean > 0.0 for result in results)
    assert all(np.isfinite(value) for result in results for value in result.__dict__.values())
    assert all(
        right.normalized_diagonal > left.normalized_diagonal
        for left, right in zip(results, results[1:])
    )
    assert abs(results[-1].normalized_diagonal - target) < 0.003
    assert abs(results[-1].normalized_off_diagonal) < 1.0e-4
    print("first boundary-entry mean-square audits passed")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limits", nargs="+", type=int, default=(128, 256, 512, 1024))
    parser.add_argument("--sample-count", type=int, default=2001)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    audit(tuple(args.limits), args.sample_count)


if __name__ == "__main__":
    main()

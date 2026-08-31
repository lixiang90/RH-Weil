"""Regression checks for reciprocal-barrier harmonic Schur identities."""

from __future__ import annotations

import numpy as np

from reciprocal_barrier import (
    amplitude_scaled_schur_bound,
    barrier_energy,
    negative_mass,
    reciprocal_kernel_gram,
    schur_projection,
)


def main() -> None:
    rng = np.random.default_rng(171)
    weights = rng.uniform(0.1, 1.0, 80)
    weights /= weights.sum()
    symbol = rng.normal(size=80)

    exact = negative_mass(symbol, weights)
    for epsilon in (1e-1, 1e-3, 1e-6):
        background = np.sqrt(symbol**2 + epsilon**2)
        assert barrier_energy(symbol, background, weights) >= exact - 1e-13
    assert abs(barrier_energy(symbol, np.sqrt(symbol**2 + 1e-12), weights) - exact) < 1e-6

    q = rng.uniform(size=symbol.size)
    background = rng.uniform(0.2, 2.0, symbol.size)
    lhs = (symbol - background) ** 2 / (4.0 * background) + symbol * q
    rhs = (
        (symbol + background * (2.0 * q - 1.0)) ** 2
        / (4.0 * background)
        + background * q * (1.0 - q)
    )
    assert np.max(np.abs(lhs - rhs)) < 1e-12
    assert lhs.min() > -1e-13

    heights = np.linspace(-4.0, 5.0, symbol.size)
    lengths = np.array([0.0, 0.2, 0.8, 1.6, 2.5])
    gram = reciprocal_kernel_gram(lengths, heights, weights, background)
    assert np.linalg.eigvalsh(gram).min() > -1e-12

    base = 2.0 + 0.2 * np.cos(heights)
    predictors = np.column_stack(
        [np.cos(0.7 * heights), np.sin(1.1 * heights), np.cos(1.9 * heights)]
    )
    coefficients = np.array([0.25, -0.18, 0.12])
    residual = predictors @ coefficients + 0.08 * np.sin(2.7 * heights)
    projection = schur_projection(residual, predictors, weights / base)
    projected = np.asarray(projection["projected"])
    direct_shorted = float(np.dot(weights / base, (residual - projected) ** 2))
    assert abs(direct_shorted - float(projection["shorted"])) < 1e-13

    result = amplitude_scaled_schur_bound(
        base, residual, predictors, weights, theta=0.4
    )
    adaptive_background = np.asarray(result["background"])
    assert adaptive_background.min() >= 0.6 * base.min() - 1e-13
    full_symbol = base + residual
    actual = negative_mass(full_symbol, weights)
    exact_background_bound = barrier_energy(
        full_symbol, adaptive_background, weights
    )
    assert actual <= exact_background_bound + 1e-13
    assert exact_background_bound <= float(result["bound"]) + 1e-13

    # Schur residual alone is unsafe when the projected background is negative.
    bad_base = np.ones(5)
    bad_residual = -11.0 * np.ones(5)
    bad_predictor = bad_residual[:, None]
    unsafe = schur_projection(
        bad_residual, bad_predictor, np.full(5, 0.2)
    )
    assert abs(float(unsafe["shorted"])) < 1e-12
    assert negative_mass(bad_base + bad_residual, np.full(5, 0.2)) == 10.0

    print("reciprocal barrier and harmonic Schur checks passed")


if __name__ == "__main__":
    main()

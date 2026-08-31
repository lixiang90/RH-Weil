"""Regression checks for square-completed Schur--L4 certificates."""

from __future__ import annotations

import numpy as np

from reciprocal_barrier import barrier_energy, negative_mass, reciprocal_kernel_gram
from square_completed_background import (
    schur_l4_bound,
    square_completed_background,
    squared_orbit_measure,
)


def main() -> None:
    rng = np.random.default_rng(172)
    points = np.linspace(-5.0, 6.0, 121)
    weights = rng.uniform(0.2, 1.0, points.size)
    weights /= weights.sum()
    base = 1.7 + 0.25 * np.cos(0.4 * points)
    predictor = 5.0 * np.sin(1.3 * points)

    for epsilon in (0.1, 1.0 / 3.0, 0.8):
        background = square_completed_background(base, predictor, epsilon)
        assert np.min(background - epsilon * base) > -1e-12
        sharp = 1.0 / (4.0 * (1.0 - epsilon))
        x_min = -1.0 / (2.0 * (0.99 * sharp))
        assert 1.0 + x_min + 0.99 * sharp * x_min**2 < epsilon

    predictors = np.column_stack(
        [np.cos(0.6 * points), np.sin(1.1 * points), np.cos(1.8 * points)]
    )
    residual = predictors @ np.array([0.8, -0.55, 0.35]) + 0.12 * np.sin(2.9 * points)
    result = schur_l4_bound(base, residual, predictors, weights)
    full_symbol = base + residual
    background = np.asarray(result["background"])
    actual = negative_mass(full_symbol, weights)
    exact_background_bound = barrier_energy(full_symbol, background, weights)
    assert actual <= exact_background_bound + 1e-12
    assert exact_background_bound <= float(result["bound"]) + 1e-12
    expected = 1.5 * float(result["shorted"]) + 27.0 / 128.0 * float(result["fourth"])
    assert abs(float(result["bound"]) - expected) < 1e-13

    # The fourth-order reciprocal kernel is positive definite.
    gram = reciprocal_kernel_gram(
        np.array([0.0, 0.2, 0.7, 1.4]), points, weights, base**3
    )
    assert np.linalg.eigvalsh(gram).min() > -1e-12

    # Check Re Q_zeta = (Re Q_xi)^2 for the pair sum/difference measure.
    lags = np.array([0.0, 0.35, 0.9])
    coefficients = np.array([0.4 + 0.1j, -0.2 + 0.3j, 0.15 - 0.08j])
    q = np.exp(-1j * np.outer(points, lags)) @ coefficients
    zeta_lags, zeta_coefficients = squared_orbit_measure(lags, coefficients)
    q_zeta = np.exp(-1j * np.outer(points, zeta_lags)) @ zeta_coefficients
    assert np.max(np.abs(q.real**2 - q_zeta.real)) < 1e-12

    print("square-completed background and Schur--L4 checks passed")


if __name__ == "__main__":
    main()

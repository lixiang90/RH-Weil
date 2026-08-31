"""Finite square-completed Hodge background and Schur--L4 bounds."""

from __future__ import annotations

import numpy as np

from reciprocal_barrier import schur_projection


def square_completed_background(
    base: np.ndarray, predictor: np.ndarray, epsilon: float
) -> np.ndarray:
    base = np.asarray(base, dtype=float)
    predictor = np.asarray(predictor, dtype=float)
    if np.any(base <= 0.0) or not 0.0 < epsilon < 1.0:
        raise ValueError("need positive base and 0 < epsilon < 1")
    return base + predictor + predictor**2 / (4.0 * (1.0 - epsilon) * base)


def schur_l4_bound(
    base: np.ndarray,
    residual: np.ndarray,
    predictors: np.ndarray,
    weights: np.ndarray,
    epsilon: float = 1.0 / 3.0,
) -> dict[str, np.ndarray | float]:
    """Project the residual, then apply the square-completed L4 bound."""

    base = np.asarray(base, dtype=float)
    residual = np.asarray(residual, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if np.any(base <= 0.0) or not 0.0 < epsilon < 1.0:
        raise ValueError("need positive base and 0 < epsilon < 1")
    projection = schur_projection(residual, predictors, weights / base)
    projected = np.asarray(projection["projected"])
    fourth = float(np.dot(weights, projected**4 / base**3))
    shorted = float(projection["shorted"])
    bound = shorted / (2.0 * epsilon) + fourth / (
        32.0 * epsilon * (1.0 - epsilon) ** 2
    )
    background = square_completed_background(base, projected, epsilon)
    return {
        **projection,
        "fourth": fourth,
        "epsilon": float(epsilon),
        "bound": float(bound),
        "background": background,
    }


def squared_orbit_measure(
    lags: np.ndarray, coefficients: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Return the finite measure zeta with Re Q_zeta = (Re Q_xi)^2."""

    lags = np.asarray(lags, dtype=float)
    coefficients = np.asarray(coefficients, dtype=complex)
    out_lags: list[float] = []
    out_coefficients: list[complex] = []
    for j, lag_j in enumerate(lags):
        for k, lag_k in enumerate(lags):
            out_lags.append(float(lag_j - lag_k))
            out_coefficients.append(0.5 * coefficients[j] * coefficients[k].conjugate())
            out_lags.append(float(lag_j + lag_k))
            out_coefficients.append(0.5 * coefficients[j] * coefficients[k])
    return np.asarray(out_lags), np.asarray(out_coefficients)

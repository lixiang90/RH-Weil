"""Finite algebra for reciprocal-barrier and harmonic Schur certificates.

The routines check exact finite identities only; they do not certify RH.
"""

from __future__ import annotations

import numpy as np


def negative_mass(symbol: np.ndarray, weights: np.ndarray) -> float:
    symbol = np.asarray(symbol, dtype=float)
    weights = np.asarray(weights, dtype=float)
    return float(np.dot(weights, np.maximum(-symbol, 0.0)))


def barrier_energy(
    symbol: np.ndarray, background: np.ndarray, weights: np.ndarray
) -> float:
    symbol = np.asarray(symbol, dtype=float)
    background = np.asarray(background, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if np.any(background <= 0.0):
        raise ValueError("background must be strictly positive")
    return float(np.dot(weights, (symbol - background) ** 2 / background) / 4.0)


def reciprocal_kernel_gram(
    length_nodes: np.ndarray,
    heights: np.ndarray,
    weights: np.ndarray,
    background: np.ndarray,
) -> np.ndarray:
    """Gram of the positive measure dmu / background."""

    length_nodes = np.asarray(length_nodes, dtype=float)
    heights = np.asarray(heights, dtype=float)
    weights = np.asarray(weights, dtype=float)
    background = np.asarray(background, dtype=float)
    if np.any(background <= 0.0):
        raise ValueError("background must be strictly positive")
    phases = np.exp(-1j * np.outer(length_nodes, heights))
    return (phases * (weights / background)) @ phases.conj().T


def schur_projection(
    residual: np.ndarray,
    predictors: np.ndarray,
    weights_over_background: np.ndarray,
) -> dict[str, np.ndarray | float]:
    """Weighted real projection and its Schur complement.

    predictors has shape (number of points, number of predictors).
    """

    residual = np.asarray(residual, dtype=float)
    predictors = np.asarray(predictors, dtype=float)
    metric = np.asarray(weights_over_background, dtype=float)
    gram = predictors.T @ (metric[:, None] * predictors)
    cross = predictors.T @ (metric * residual)
    alpha = np.linalg.pinv(gram, hermitian=True) @ cross
    projected = predictors @ alpha
    energy = float(np.dot(metric, residual**2))
    gain = float(cross @ np.linalg.pinv(gram, hermitian=True) @ cross)
    shorted = energy - gain
    return {
        "gram": gram,
        "cross": cross,
        "alpha": alpha,
        "projected": projected,
        "energy": energy,
        "gain": gain,
        "shorted": shorted,
    }


def amplitude_scaled_schur_bound(
    base_background: np.ndarray,
    residual: np.ndarray,
    predictors: np.ndarray,
    weights: np.ndarray,
    theta: float,
) -> dict[str, np.ndarray | float]:
    """The finite version of the amplitude-certified Schur bound."""

    base_background = np.asarray(base_background, dtype=float)
    residual = np.asarray(residual, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if np.any(base_background <= 0.0) or not 0.0 < theta < 1.0:
        raise ValueError("need positive base background and 0 < theta < 1")
    projection = schur_projection(
        residual, predictors, weights / base_background
    )
    projected = np.asarray(projection["projected"])
    ratio = np.max(np.abs(projected) / base_background)
    scale = 1.0 if ratio == 0.0 else min(1.0, theta / ratio)
    numerator = float(projection["energy"]) - (
        2.0 * scale - scale**2
    ) * float(projection["gain"])
    bound = numerator / (4.0 * (1.0 - theta))
    background = base_background + scale * projected
    return {
        **projection,
        "amplitude_ratio": float(ratio),
        "scale": float(scale),
        "numerator": float(numerator),
        "bound": float(bound),
        "background": background,
    }

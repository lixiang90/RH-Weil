"""Finite models for capped positive-definite correspondence kernels.

These routines verify algebraic identities only; they do not certify RH.
"""

from __future__ import annotations

import numpy as np


def kernel_values(
    lags: np.ndarray, heights: np.ndarray, weights: np.ndarray
) -> np.ndarray:
    """Fourier transform of a finite positive spectral measure."""

    lags = np.asarray(lags, dtype=float)
    heights = np.asarray(heights, dtype=float)
    weights = np.asarray(weights, dtype=float)
    return np.exp(-1j * np.outer(lags, heights)) @ weights


def capped_kernel_values(
    lags: np.ndarray,
    heights: np.ndarray,
    weights: np.ndarray,
    effect: np.ndarray,
) -> np.ndarray:
    """Fourier transform of q mu for a discrete effect 0 <= q <= 1."""

    effect = np.asarray(effect, dtype=float)
    if np.any(effect < 0.0) or np.any(effect > 1.0):
        raise ValueError("effect must lie in [0, 1]")
    return kernel_values(lags, heights, np.asarray(weights) * effect)


def gram_from_measure(
    length_nodes: np.ndarray,
    heights: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    """Positive Gram [kappa(lambda_j-lambda_k)] from a discrete measure."""

    length_nodes = np.asarray(length_nodes, dtype=float)
    phases = np.exp(-1j * np.outer(length_nodes, np.asarray(heights, dtype=float)))
    return (phases * np.asarray(weights, dtype=float)) @ phases.conj().T


def capped_index(symbol: np.ndarray, weights: np.ndarray) -> float:
    """Exact discrete negative spectral mass sum mu_j max(-H_j, 0)."""

    symbol = np.asarray(symbol, dtype=float)
    weights = np.asarray(weights, dtype=float)
    return float(np.dot(weights, np.maximum(-symbol, 0.0)))


def effect_objective(
    symbol: np.ndarray, weights: np.ndarray, effect: np.ndarray
) -> float:
    """Discrete orbit objective integral H q dmu."""

    return float(
        np.dot(
            np.asarray(weights, dtype=float),
            np.asarray(symbol, dtype=float) * np.asarray(effect, dtype=float),
        )
    )

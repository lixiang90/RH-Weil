"""Finite-matrix utilities for the tracial lattice-clipping theorem."""

from __future__ import annotations

import numpy as np


def hermitian_part(matrix: np.ndarray) -> np.ndarray:
    """Return the Hermitian part of a square matrix."""

    matrix = np.asarray(matrix, dtype=np.complex128)
    return (matrix + matrix.conj().T) / 2.0


def positive_powers(
    matrix: np.ndarray, powers: tuple[float, ...]
) -> tuple[np.ndarray, ...]:
    """Apply scalar powers to a positive-definite Hermitian matrix."""

    eigenvalues, eigenvectors = np.linalg.eigh(hermitian_part(matrix))
    if float(np.min(eigenvalues)) <= 0.0:
        raise ValueError("matrix must be positive definite")
    return tuple(
        (eigenvectors * (eigenvalues**power)) @ eigenvectors.conj().T
        for power in powers
    )


def trace_negative(matrix: np.ndarray) -> float:
    """Return the unnormalized trace of the negative part."""

    eigenvalues = np.linalg.eigvalsh(hermitian_part(matrix))
    return float(np.maximum(-eigenvalues, 0.0).sum())


def operator_barrier_energy(h_current: np.ndarray, background: np.ndarray) -> float:
    """Return (1/4) Tr((H-B) B^{-1} (H-B))."""

    h_current = hermitian_part(h_current)
    background = hermitian_part(background)
    difference = h_current - background
    solved = np.linalg.solve(background, difference)
    value = np.trace(difference @ solved).real / 4.0
    return float(value)


def relative_clip(
    background: np.ndarray, predictor: np.ndarray, epsilon: float
) -> tuple[np.ndarray, np.ndarray]:
    """Return the relative clipped predictor and its positive background."""

    if not 0.0 < epsilon < 1.0:
        raise ValueError("epsilon must lie in (0, 1)")
    background = hermitian_part(background)
    predictor = hermitian_part(predictor)
    sqrt_background, invsqrt_background = positive_powers(
        background, (0.5, -0.5)
    )
    relative = hermitian_part(invsqrt_background @ predictor @ invsqrt_background)
    eigenvalues, eigenvectors = np.linalg.eigh(relative)
    clipped_values = np.maximum(eigenvalues, -(1.0 - epsilon))
    clipped_relative = (
        eigenvectors * clipped_values
    ) @ eigenvectors.conj().T
    clipped_predictor = hermitian_part(
        sqrt_background @ clipped_relative @ sqrt_background
    )
    clipped_background = hermitian_part(background + clipped_predictor)
    return clipped_predictor, clipped_background


def clipped_residual_bound(
    background: np.ndarray,
    residual: np.ndarray,
    predictor: np.ndarray,
    epsilon: float,
) -> float:
    """Return the right side of the lattice-clipped residual inequality."""

    background = hermitian_part(background)
    residual = hermitian_part(residual)
    clipped_predictor, _ = relative_clip(background, predictor, epsilon)
    difference = residual - clipped_predictor
    solved = np.linalg.solve(background, difference)
    value = np.trace(difference @ solved).real / (4.0 * epsilon)
    return float(value)


def scalar_quartic_capacity(
    background: np.ndarray,
    predictor: np.ndarray,
    weights: np.ndarray,
) -> tuple[float, float, float]:
    """Return D, P4, M0 for the scalar quartic-capacity inequality."""

    background = np.asarray(background, dtype=float)
    predictor = np.asarray(predictor, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if np.any(background <= 0.0) or np.any(weights < 0.0):
        raise ValueError("background must be positive and weights nonnegative")
    d_energy = float(np.sum(weights * predictor**2 / background))
    fourth = float(np.sum(weights * predictor**4 / background**3))
    mass = float(np.sum(weights * background))
    return d_energy, fourth, mass

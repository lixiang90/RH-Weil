"""Regression checks for tracial lattice clipping.

These are finite floating-point identity checks, not RH evidence.
"""

from __future__ import annotations

import numpy as np

from lattice_clipped_background import (
    clipped_residual_bound,
    hermitian_part,
    operator_barrier_energy,
    relative_clip,
    scalar_quartic_capacity,
    trace_negative,
)


def random_hermitian(rng: np.random.Generator, size: int) -> np.ndarray:
    raw = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    return hermitian_part(raw)


def random_positive(rng: np.random.Generator, size: int) -> np.ndarray:
    raw = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    return hermitian_part(raw @ raw.conj().T + 0.75 * np.eye(size))


def test_noncommuting_operator_barrier_and_clip() -> None:
    rng = np.random.default_rng(173)
    epsilon = 0.31
    for _ in range(24):
        size = 5
        background = random_positive(rng, size)
        residual = random_hermitian(rng, size)
        predictor = random_hermitian(rng, size)
        h_current = background + residual
        clipped_predictor, clipped_background = relative_clip(
            background, predictor, epsilon
        )

        loewner_gap = clipped_background - epsilon * background
        assert np.linalg.eigvalsh(loewner_gap).min() >= -2.0e-10

        actual = trace_negative(h_current)
        barrier = operator_barrier_energy(h_current, clipped_background)
        clipped = clipped_residual_bound(
            background, residual, predictor, epsilon
        )
        assert actual <= barrier + 2.0e-9
        assert barrier <= clipped + 2.0e-9

        commutator = background @ clipped_predictor - clipped_predictor @ background
        assert np.linalg.norm(commutator) > 1.0e-8


def test_scalar_quartic_capacity_and_sharpness() -> None:
    rng = np.random.default_rng(4173)
    background = np.exp(rng.normal(size=80))
    predictor = rng.normal(size=80)
    weights = rng.random(size=80)
    d_energy, fourth, mass = scalar_quartic_capacity(
        background, predictor, weights
    )
    assert d_energy**2 <= fourth * mass + 1.0e-10

    constant = -2.75
    sharp_predictor = constant * background
    d_energy, fourth, mass = scalar_quartic_capacity(
        background, sharp_predictor, weights
    )
    assert abs(d_energy**2 - fourth * mass) <= 1.0e-10 * fourth * mass


def test_safe_predictor_has_zero_clipped_residual() -> None:
    background = np.diag([1.0, 2.0, 3.0])
    residual = np.diag([12.0, 0.25, -0.4])
    predictor = residual.copy()
    epsilon = 0.5
    clipped_predictor, clipped_background = relative_clip(
        background, predictor, epsilon
    )
    assert np.allclose(clipped_predictor, predictor)
    assert clipped_residual_bound(
        background, residual, predictor, epsilon
    ) <= 1.0e-14
    assert trace_negative(background + residual) == 0.0
    assert np.linalg.eigvalsh(clipped_background).min() > 0.0


def test_amplitude_counterexample_is_not_erased() -> None:
    level = 20.0
    epsilon = 0.4
    background = np.array([[1.0]])
    residual = np.array([[-level - 1.0]])
    predictor = residual.copy()
    clipped_predictor, _ = relative_clip(background, predictor, epsilon)
    assert np.allclose(clipped_predictor, [[-(1.0 - epsilon)]])
    actual = trace_negative(background + residual)
    bound = clipped_residual_bound(background, residual, predictor, epsilon)
    assert abs(actual - level) <= 1.0e-12
    assert bound >= actual


def main() -> None:
    test_noncommuting_operator_barrier_and_clip()
    test_scalar_quartic_capacity_and_sharpness()
    test_safe_predictor_has_zero_clipped_residual()
    test_amplitude_counterexample_is_not_erased()
    print("tracial lattice-clipped background checks passed")


if __name__ == "__main__":
    main()

"""Finite audits for note 225's fourfold signed boundary closure.

The checks cover finite-section algebra, modulation signs, nuclear crossing
bounds, and asymptotic exponent bookkeeping.  They do not implement the
Henriot sieve theorem, prove a prime asymptotic, or provide RH evidence.
"""

from __future__ import annotations

import math
from collections.abc import Mapping

import numpy as np


TOL = 5.0e-11


def toeplitz(coefficients: Mapping[int, complex], dimension: int) -> np.ndarray:
    return np.array(
        [
            [coefficients.get(row - column, 0.0) for column in range(dimension)]
            for row in range(dimension)
        ],
        dtype=complex,
    )


def convolve(
    left: Mapping[int, complex], right: Mapping[int, complex]
) -> dict[int, complex]:
    result: dict[int, complex] = {}
    for left_mode, left_value in left.items():
        for right_mode, right_value in right.items():
            mode = left_mode + right_mode
            result[mode] = result.get(mode, 0.0) + left_value * right_value
    return result


def crossing(
    left: Mapping[int, complex],
    right: Mapping[int, complex],
    dimension: int,
) -> tuple[np.ndarray, np.ndarray]:
    bandwidth = sum(
        max((abs(mode) for mode in coefficients), default=0)
        for coefficients in (left, right)
    )
    outside = list(range(-bandwidth, 0)) + list(
        range(dimension, dimension + bandwidth)
    )
    left_cross = np.array(
        [
            [left.get(row - index, 0.0) for index in outside]
            for row in range(dimension)
        ],
        dtype=complex,
    )
    right_cross = np.array(
        [
            [right.get(index - column, 0.0) for column in range(dimension)]
            for index in outside
        ],
        dtype=complex,
    )
    return left_cross, right_cross


def hankel(
    left: Mapping[int, complex],
    right: Mapping[int, complex],
    dimension: int,
) -> np.ndarray:
    left_cross, right_cross = crossing(left, right, dimension)
    return left_cross @ right_cross


def boundary_energy(coefficients: Mapping[int, complex], dimension: int) -> float:
    return float(
        sum(
            min(dimension, abs(mode)) * abs(value) ** 2
            for mode, value in coefficients.items()
        )
    )


def conjugate_symbol(coefficients: Mapping[int, complex]) -> dict[int, complex]:
    return {mode: value.conjugate() for mode, value in coefficients.items()}


def nuclear_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def audit_fourfold_telescoping() -> None:
    rng = np.random.default_rng(225)
    dimension = 13
    symbols = [
        {
            mode: 0.15 * (rng.normal() + 1j * rng.normal())
            for mode in range(-bandwidth, bandwidth + 1)
        }
        for bandwidth in (2, 3, 2, 4)
    ]
    cumulative = [symbols[0]]
    for symbol in symbols[1:]:
        cumulative.append(convolve(cumulative[-1], symbol))

    finite = np.eye(dimension, dtype=complex)
    for symbol in symbols:
        finite = finite @ toeplitz(symbol, dimension)
    bulk = toeplitz(cumulative[-1], dimension)
    telescoped = bulk.copy()
    for index in range(3):
        term = hankel(cumulative[index], symbols[index + 1], dimension)
        for tail in symbols[index + 2 :]:
            term = term @ toeplitz(tail, dimension)
        telescoped -= term

    residual = np.linalg.norm(finite - telescoped, ord="fro")
    assert residual <= TOL * max(1.0, np.linalg.norm(finite, ord="fro"))
    print("fourfold Toeplitz telescoping identity passed")


def translate(
    coefficients: Mapping[int, complex], spacing: float, shift: float
) -> dict[int, complex]:
    return {
        mode: np.exp(1j * mode * spacing * shift) * value
        for mode, value in coefficients.items()
    }


def audit_adjoint_modulation_sign() -> None:
    rng = np.random.default_rng(226)
    dimension = 10
    length = 17.0
    spacing = 2.0 * math.pi / length
    shift = 2.3
    positive = {0: complex(rng.normal())}
    for mode in range(1, 4):
        value = rng.normal() + 1j * rng.normal()
        positive[mode] = value
        positive[-mode] = value.conjugate()

    diagonal = np.diag(
        np.exp(1j * spacing * shift * np.arange(dimension, dtype=float))
    )
    response = toeplitz(positive, dimension) @ diagonal
    adjoint = response.conj().T
    negative_symbol = translate(positive, spacing, -shift)
    reconstructed = toeplitz(negative_symbol, dimension) @ diagonal.conj().T
    assert np.linalg.norm(adjoint - reconstructed, ord="fro") <= TOL * max(
        1.0, np.linalg.norm(adjoint, ord="fro")
    )
    print("adjoint modulation/translation sign passed")


def audit_nuclear_crossing_bound() -> None:
    rng = np.random.default_rng(227)
    dimension = 12
    symbols = [
        {
            mode: 0.08 * (rng.normal() + 1j * rng.normal())
            for mode in range(-3, 4)
        }
        for _ in range(4)
    ]
    cumulative = [symbols[0]]
    for symbol in symbols[1:]:
        cumulative.append(convolve(cumulative[-1], symbol))

    phase = 0.37
    unitary = np.diag(np.exp(1j * phase * np.arange(dimension)))
    finite = np.eye(dimension, dtype=complex)
    for symbol in symbols:
        finite = finite @ toeplitz(symbol, dimension)
    delta_trace = abs(
        np.trace((finite - toeplitz(cumulative[-1], dimension)) @ unitary)
    )

    predicted = 0.0
    for index in range(3):
        left = cumulative[index]
        right = symbols[index + 1]
        tail_norm = 1.0
        for tail in symbols[index + 2 :]:
            tail_norm *= np.linalg.norm(toeplitz(tail, dimension), ord=2)
        predicted += math.sqrt(
            boundary_energy(left, dimension)
            * boundary_energy(conjugate_symbol(right), dimension)
        ) * tail_norm

    exact_nuclear = 0.0
    for index in range(3):
        term = hankel(cumulative[index], symbols[index + 1], dimension)
        for tail in symbols[index + 2 :]:
            term = term @ toeplitz(tail, dimension)
        exact_nuclear += nuclear_norm(term)

    assert delta_trace <= exact_nuclear + TOL
    assert exact_nuclear <= predicted + TOL
    print("fourfold scalar boundary nuclear crossing bound passed")


def audit_exponent_ledger() -> None:
    # Write u=log L.  The normalized near term is
    # (1+u)u^4 exp(-u/2); the normalized far term is
    # (1+u) exp(-9u/2).
    log_lengths = (20.0, 40.0, 80.0, 160.0)
    near = [(1.0 + u) * u**4 * math.exp(-u / 2.0) for u in log_lengths]
    far = [(1.0 + u) * math.exp(-4.5 * u) for u in log_lengths]
    assert all(right < left for left, right in zip(near, near[1:]))
    assert all(right < left for left, right in zip(far, far[1:]))
    assert near[-1] < 1e-23
    assert far[-1] < 1e-300
    print("3+1/4+0 finite-boundary exponent ledger passed")


def audit_signed_vs_absolute_mean() -> None:
    amplitude = 7.0
    frequency = 1.3
    height = 100.0
    signed = amplitude * abs(
        (np.exp(1j * height * frequency) - 1.0)
        / (1j * height * frequency)
    )
    absolute = amplitude
    assert signed <= 2.0 * amplitude / (height * frequency) + TOL
    assert absolute == amplitude
    assert signed < 0.02 * absolute
    print("signed mean / mean-absolute separation passed")


def main() -> None:
    audit_fourfold_telescoping()
    audit_adjoint_modulation_sign()
    audit_nuclear_crossing_bound()
    audit_exponent_ledger()
    audit_signed_vs_absolute_mean()
    print("fourfold signed Toeplitz boundary audits passed")
    print("[scope] finite algebra/exponents only; no sieve theorem or RH claim")


if __name__ == "__main__":
    main()

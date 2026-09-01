"""Finite audits for the Toeplitz--Hankel adjacent transfer.

These checks cover exact finite-section algebra, crossing-pair counting,
the modulation/translation sign, and the logarithmic boundary-energy scale
for a smooth compact window.  They do not prove a prime asymptotic or a
zeta fourth-moment estimate.
"""

from __future__ import annotations

import math
from collections.abc import Mapping

import numpy as np

from adjacent_bulk_edge_audit import prime_power_weights


TOL = 2.0e-11


def toeplitz_from_coefficients(
    coefficients: Mapping[int, complex], dimension: int
) -> np.ndarray:
    return np.array(
        [
            [coefficients.get(row - column, 0.0) for column in range(dimension)]
            for row in range(dimension)
        ],
        dtype=complex,
    )


def convolve_coefficients(
    left: Mapping[int, complex], right: Mapping[int, complex]
) -> dict[int, complex]:
    result: dict[int, complex] = {}
    for left_mode, left_value in left.items():
        for right_mode, right_value in right.items():
            mode = left_mode + right_mode
            result[mode] = result.get(mode, 0.0) + left_value * right_value
    return result


def cross_boundary_factors(
    left: Mapping[int, complex],
    right: Mapping[int, complex],
    dimension: int,
) -> tuple[np.ndarray, np.ndarray, list[int]]:
    bandwidth = max(
        max((abs(mode) for mode in left), default=0),
        max((abs(mode) for mode in right), default=0),
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
    return left_cross, right_cross, outside


def boundary_energy(coefficients: Mapping[int, complex], dimension: int) -> float:
    return float(
        sum(
            min(dimension, abs(mode)) * abs(value) ** 2
            for mode, value in coefficients.items()
        )
    )


def audit_toeplitz_hankel_identity() -> None:
    rng = np.random.default_rng(204)
    dimension = 11
    bandwidth = 4
    left = {
        mode: rng.normal() + 1j * rng.normal()
        for mode in range(-bandwidth, bandwidth + 1)
    }
    right = {
        mode: rng.normal() + 1j * rng.normal()
        for mode in range(-bandwidth, bandwidth + 1)
    }

    left_toeplitz = toeplitz_from_coefficients(left, dimension)
    right_toeplitz = toeplitz_from_coefficients(right, dimension)
    product_symbol = convolve_coefficients(left, right)
    bulk = toeplitz_from_coefficients(product_symbol, dimension)
    left_cross, right_cross, _ = cross_boundary_factors(left, right, dimension)
    defect = left_cross @ right_cross

    residual = left_toeplitz @ right_toeplitz - (bulk - defect)
    assert np.linalg.norm(residual, ord="fro") <= TOL * max(
        1.0, np.linalg.norm(bulk, ord="fro")
    )

    crossing_norm = float(np.linalg.norm(left_cross, ord="fro") ** 2)
    predicted = boundary_energy(left, dimension)
    assert abs(crossing_norm - predicted) <= TOL * max(1.0, predicted)
    print("Toeplitz product and crossing-pair boundary identity passed")


def audit_modulation_translation_sign() -> None:
    rng = np.random.default_rng(205)
    dimension = 9
    length = 13.0
    spacing = 2.0 * math.pi / length
    shift = 1.7
    coefficients = {
        mode: rng.normal() + 1j * rng.normal() for mode in range(-3, 4)
    }

    diagonal = np.diag(
        np.exp(1j * spacing * shift * np.arange(dimension, dtype=float))
    )
    translated = {
        mode: np.exp(1j * mode * spacing * shift) * value
        for mode, value in coefficients.items()
    }
    conjugated = (
        diagonal
        @ toeplitz_from_coefficients(coefficients, dimension)
        @ diagonal.conj().T
    )
    target = toeplitz_from_coefficients(translated, dimension)
    assert np.linalg.norm(conjugated - target, ord="fro") <= TOL * max(
        1.0, np.linalg.norm(target, ord="fro")
    )
    print("diagonal modulation equals q(u-x) symbol translation")


def smootherstep(value: np.ndarray) -> np.ndarray:
    clipped = np.clip(value, 0.0, 1.0)
    return clipped**3 * (10.0 - 15.0 * clipped + 6.0 * clipped**2)


def smooth_compact_window(grid: np.ndarray, length: float) -> np.ndarray:
    distance_to_endpoint = length / 2.0 - np.abs(grid)
    return smootherstep(distance_to_endpoint)


def fourier_coefficients_from_samples(values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    sample_count = values.size
    # Samples are ordered on [-L/2,L/2); the phase shift affects coefficients
    # but not the boundary energy, which only uses their moduli.
    coefficients = np.fft.fft(values) / sample_count
    modes = np.fft.fftfreq(sample_count, d=1.0 / sample_count).astype(int)
    return modes, coefficients


def sampled_boundary_energy(length: float, sample_count: int = 1 << 16) -> float:
    grid = np.linspace(-length / 2.0, length / 2.0, sample_count, endpoint=False)
    phi = smooth_compact_window(grid, length)
    shift = 0.42 * length
    shifted_argument = shift - grid
    shifted_phi = np.where(
        np.abs(shifted_argument) <= length / 2.0,
        smooth_compact_window(shifted_argument, length),
        0.0,
    )
    symbol = phi * shifted_phi
    modes, coefficients = fourier_coefficients_from_samples(symbol)
    return float(
        np.sum(np.abs(modes).astype(float) * np.abs(coefficients) ** 2)
    )


def audit_logarithmic_boundary_scale() -> None:
    lengths = (16.0, 32.0, 64.0, 128.0)
    energies = [sampled_boundary_energy(length) for length in lengths]
    normalized = [energy / math.log(length) for energy, length in zip(energies, lengths)]
    assert all(math.isfinite(value) and value > 0.0 for value in energies)
    assert max(normalized) < 1.0
    assert energies[-1] < 4.0 * energies[0]
    print(
        "smooth-window boundary energies: "
        + ", ".join(
            f"L={length:g}: {energy:.8f}" for length, energy in zip(lengths, energies)
        )
    )


def audit_arithmetic_defect_scale() -> None:
    limits = (20_000, 100_000, 500_000)
    ratios = []
    for limit in limits:
        log_x = math.log(limit)
        quadratic_weight = sum(item.weight for item in prime_power_weights(limit))
        # beta^4 and b_a^2 b_b^2 cancel the (2*pi)^4 factors.
        defect_majorant = (
            quadratic_weight**2 * math.log(2.0 + log_x) / log_x**4
        )
        zero_scale = limit * log_x
        ratios.append(defect_majorant / zero_scale)
        print(
            f"X={limit:>7d}: defect_majorant={defect_majorant:.8f}, "
            f"defect/N={ratios[-1]:.3e}"
        )
    assert ratios[-1] < ratios[0]
    assert ratios[-1] < 1.0e-6


def main() -> None:
    audit_toeplitz_hankel_identity()
    audit_modulation_translation_sign()
    audit_logarithmic_boundary_scale()
    audit_arithmetic_defect_scale()
    print("Toeplitz--Hankel adjacent audits passed.")


if __name__ == "__main__":
    main()

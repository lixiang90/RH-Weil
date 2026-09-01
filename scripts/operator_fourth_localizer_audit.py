"""Audits for fourth-word operator structure and localizer completion.

The checks are finite algebraic identities.  They do not prove the weighted
Gabor boundary estimate or positivity of an arithmetic localizer hierarchy.
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction

import numpy as np
from numpy.polynomial.legendre import leggauss


TOL = 2.0e-10


def schatten_norm(matrix: np.ndarray, exponent: float) -> float:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    return float(np.sum(singular_values**exponent) ** (1.0 / exponent))


def audit_degree_four_indistinguishability() -> None:
    positive = (
        (Fraction(1, 5), 15),
        (Fraction(3, 5), 45),
        (Fraction(1, 1), 5),
    )
    indefinite = (
        (Fraction(-1, 5), 1),
        (Fraction(2, 5), 40),
        (Fraction(4, 5), 24),
    )

    def moments(measure: tuple[tuple[Fraction, int], ...], degree: int):
        return tuple(
            sum(weight * point**power for point, weight in measure)
            / 65
            for power in range(degree + 1)
        )

    expected = (
        Fraction(1, 1),
        Fraction(7, 13),
        Fraction(109, 325),
        Fraction(371, 1625),
        Fraction(1357, 8125),
    )
    assert moments(positive, 4) == expected
    assert moments(indefinite, 4) == expected
    first_localizer_determinant = expected[1] * expected[3] - expected[2] ** 2
    assert first_localizer_determinant == Fraction(1104, 105625)

    def polynomial(point: Fraction) -> Fraction:
        return (point - Fraction(2, 5)) * (point - Fraction(4, 5))

    witness = sum(
        weight * point * polynomial(point) ** 2
        for point, weight in indefinite
    ) / 65
    assert witness == Fraction(-9, 8125)
    print(
        "degree-four localizer no-go passed: "
        f"moments={expected}, degree-two witness={witness}"
    )


def audit_intrinsic_signed_kernel_spectrum() -> None:
    rng = np.random.default_rng(2609200)
    for sample_count, feature_count in ((7, 4), (11, 6)):
        raw = rng.normal(size=(sample_count, feature_count)) + 1j * rng.normal(
            size=(sample_count, feature_count)
        )
        signs = np.diag(rng.choice((-1.0, 1.0), size=sample_count))
        finite = np.conjugate(raw.T) @ signs @ raw
        envelope = raw @ np.conjugate(raw.T)
        eigenvalues, eigenvectors = np.linalg.eigh(envelope)
        square_root = (
            eigenvectors
            @ np.diag(np.sqrt(np.maximum(eigenvalues, 0.0)))
            @ np.conjugate(eigenvectors.T)
        )
        intrinsic = square_root @ signs @ square_root
        finite_spectrum = np.linalg.eigvalsh(finite)
        intrinsic_spectrum = np.linalg.eigvalsh(intrinsic)
        finite_nonzero = finite_spectrum[np.abs(finite_spectrum) > 1.0e-8]
        intrinsic_nonzero = intrinsic_spectrum[
            np.abs(intrinsic_spectrum) > 1.0e-8
        ]
        assert np.allclose(
            finite_nonzero, intrinsic_nonzero, atol=2.0e-8, rtol=2.0e-8
        )
        assert abs(
            np.trace(np.linalg.matrix_power(finite, 4))
            - np.trace(np.linalg.matrix_power(intrinsic, 4))
        ) <= TOL * max(
            1.0, abs(np.trace(np.linalg.matrix_power(finite, 4)))
        )
    print("intrinsic signed-kernel spectrum audit passed")


def audit_noncommutative_two_two_ledger() -> None:
    rng = np.random.default_rng(2609201)
    for dimension in (3, 7):
        z = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
            size=(dimension, dimension)
        )
        z_star = np.conjugate(z.T)
        adjacent = schatten_norm(z @ z, 2.0) ** 2
        alternating = schatten_norm(z @ z_star, 2.0) ** 2
        commutator = z @ z_star - z_star @ z
        commutator_energy = schatten_norm(commutator, 2.0) ** 2
        assert abs(
            alternating - adjacent - 0.5 * commutator_energy
        ) <= TOL * max(1.0, alternating)
        two_two = 4.0 * adjacent + 2.0 * alternating
        assert abs(two_two - (6.0 * adjacent + commutator_energy)) <= (
            TOL * max(1.0, two_two)
        )
        assert abs(
            two_two - (6.0 * alternating - 2.0 * commutator_energy)
        ) <= TOL * max(1.0, two_two)

        direct = np.trace(np.linalg.matrix_power(z + z_star, 4))
        ledger = (
            2.0 * np.real(np.trace(np.linalg.matrix_power(z, 4)))
            + 8.0 * np.real(np.trace(np.linalg.matrix_power(z, 3) @ z_star))
            + two_two
        )
        assert abs(direct - ledger) <= TOL * max(1.0, abs(direct))
    print("noncommutative 2+2 commutator ledger passed")


def audit_product_and_ratio_blocks() -> None:
    rng = np.random.default_rng(2609202)
    atoms = (2, 3, 4, 6)
    dimension = 4
    coefficients = {
        atom: rng.normal() + 1j * rng.normal() for atom in atoms
    }
    responses = {
        atom: rng.normal(size=(dimension, dimension))
        + 1j * rng.normal(size=(dimension, dimension))
        for atom in atoms
    }
    z = sum(coefficients[atom] * responses[atom] for atom in atoms)

    product_blocks: defaultdict[int, np.ndarray] = defaultdict(
        lambda: np.zeros((dimension, dimension), dtype=complex)
    )
    ratio_blocks: defaultdict[tuple[int, int], np.ndarray] = defaultdict(
        lambda: np.zeros((dimension, dimension), dtype=complex)
    )
    for left in atoms:
        for right in atoms:
            product_blocks[left * right] += (
                coefficients[left]
                * coefficients[right]
                * responses[left]
                @ responses[right]
            )
            divisor = math.gcd(left, right)
            ratio = (left // divisor, right // divisor)
            ratio_blocks[ratio] += (
                coefficients[left]
                * np.conjugate(coefficients[right])
                * responses[left]
                @ np.conjugate(responses[right].T)
            )

    reconstructed_square = sum(product_blocks.values())
    reconstructed_mixed = sum(ratio_blocks.values())
    assert np.allclose(reconstructed_square, z @ z)
    assert np.allclose(reconstructed_mixed, z @ np.conjugate(z.T))
    adjacent_gram = sum(
        np.vdot(left, right)
        for left in product_blocks.values()
        for right in product_blocks.values()
    )
    alternating_gram = sum(
        np.vdot(left, right)
        for left in ratio_blocks.values()
        for right in ratio_blocks.values()
    )
    assert abs(adjacent_gram - np.vdot(z @ z, z @ z)) <= TOL * max(
        1.0, abs(adjacent_gram)
    )
    assert abs(
        alternating_gram
        - np.vdot(z @ np.conjugate(z.T), z @ np.conjugate(z.T))
    ) <= TOL * max(1.0, abs(alternating_gram))
    print(
        "product/ratio Gram blocks passed: "
        f"products={len(product_blocks)}, ratios={len(ratio_blocks)}"
    )


def audit_schatten_boundary_scale() -> None:
    previous_rank_one_ratio = 0.0
    for logarithm in (20.0, 30.0, 40.0):
        height = math.exp(logarithm)
        iterated_log = 1.0 + math.log(logarithm)
        q_squared = height * iterated_log**2 / logarithm**2
        zero_count_scale = height * logarithm
        conservative_second_error = height * iterated_log
        assert q_squared / conservative_second_error < 0.1
        rank_one_fourth_ratio = q_squared**2 / zero_count_scale
        assert rank_one_fourth_ratio > previous_rank_one_ratio
        previous_rank_one_ratio = rank_one_fourth_ratio

        hs_target = logarithm**3 / iterated_log**2
        assert abs(q_squared * hs_target / zero_count_scale - 1.0) <= TOL
    print(
        "Schatten boundary scale passed: rank-one fourth/N grows, "
        "q^2 times HS target equals N"
    )


def cosine_path_overlap(shifts: tuple[float, ...], parameter: float) -> float:
    nodes, weights = leggauss(96)
    lower = max(-0.5 - shift for shift in shifts)
    upper = min(0.5 - shift for shift in shifts)
    if upper <= lower:
        return 0.0
    midpoint = 0.5 * (lower + upper)
    half_length = 0.5 * (upper - lower)
    locations = midpoint + half_length * nodes
    values = np.ones_like(locations)
    for shift in shifts:
        values *= np.cos(parameter * (locations + shift))
    return float(half_length * np.dot(weights, values))


def audit_cosine_edge_overlap() -> None:
    for parameter in (math.sqrt(2.0), 3.1, math.pi):
        endpoint_value = math.cos(parameter / 2.0)
        for edge_length in (0.2, 0.08, 0.02):
            shifts = (0.0, 0.23, 0.61, 1.0 - edge_length)
            overlap = cosine_path_overlap(shifts, parameter)
            bound = (
                endpoint_value**2 * edge_length
                + endpoint_value * parameter * edge_length**2
                + parameter**2 * edge_length**3 / 6.0
            )
            assert -TOL <= overlap <= bound + TOL

    interior_shifts = (0.23, 0.61)
    predicted = (
        math.pi**2
        / 6.0
        * math.sin(math.pi * interior_shifts[0])
        * math.sin(math.pi * interior_shifts[1])
    )
    ratios = []
    for edge_length in (0.04, 0.02, 0.01, 0.005):
        shifts = (
            0.0,
            interior_shifts[0],
            interior_shifts[1],
            1.0 - edge_length,
        )
        overlap = cosine_path_overlap(shifts, math.pi)
        ratios.append(overlap / edge_length**3)
        assert overlap <= math.pi**2 * edge_length**3 / 6.0 + TOL
    assert abs(ratios[-1] - predicted) <= 0.015
    normalized_center = (3.0 / 8.0) / (2.0 / math.pi) ** 4
    assert abs(normalized_center - 3.0 * math.pi**4 / 128.0) <= TOL
    assert normalized_center > 1.0
    print(
        "cosine path-edge audit passed: "
        f"cubic coefficient={ratios[-1]:.9f}, predicted={predicted:.9f}"
    )


def main() -> None:
    audit_degree_four_indistinguishability()
    audit_intrinsic_signed_kernel_spectrum()
    audit_noncommutative_two_two_ledger()
    audit_product_and_ratio_blocks()
    audit_schatten_boundary_scale()
    audit_cosine_edge_overlap()
    print("Operator fourth/localizer audits passed.")


if __name__ == "__main__":
    main()

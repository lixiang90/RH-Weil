"""Finite audits for the alternating prime-power ratio decomposition.

The checks cover the exact alternating Toeplitz--Hankel product, ratio-cluster
multiplicity under von Mangoldt support, convergence of noncentral same-prime
chains, and the even determinant gap for odd primitive prime ratios.  They do
not prove the open square-root Farey response estimate.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction

import numpy as np

from adjacent_bulk_edge_audit import primes_up_to
from toeplitz_hankel_adjacent_audit import (
    convolve_coefficients,
    cross_boundary_factors,
    toeplitz_from_coefficients,
)


TOL = 3.0e-11


@dataclass(frozen=True)
class PrimePowerAtom:
    n: int
    prime: int
    exponent: int
    log_prime: float


def prime_power_atoms(limit: int) -> list[PrimePowerAtom]:
    atoms: list[PrimePowerAtom] = []
    for prime in primes_up_to(limit):
        power = prime
        exponent = 1
        while power <= limit:
            atoms.append(
                PrimePowerAtom(power, prime, exponent, math.log(prime))
            )
            if power > limit // prime:
                break
            power *= prime
            exponent += 1
    atoms.sort(key=lambda atom: atom.n)
    return atoms


def audit_alternating_toeplitz_hankel_identity() -> None:
    rng = np.random.default_rng(210)
    dimension = 10
    bandwidth = 4
    length = 13.0
    spacing = 2.0 * math.pi / length
    shift = -2.3
    left = {
        mode: rng.normal() + 1j * rng.normal()
        for mode in range(-bandwidth, bandwidth + 1)
    }
    right = {
        mode: rng.normal() + 1j * rng.normal()
        for mode in range(-bandwidth, bandwidth + 1)
    }
    translated_right = {
        mode: np.exp(1j * mode * spacing * shift) * value
        for mode, value in right.items()
    }
    diagonal = np.diag(
        np.exp(1j * spacing * shift * np.arange(dimension, dtype=float))
    )
    left_toeplitz = toeplitz_from_coefficients(left, dimension)
    right_toeplitz = toeplitz_from_coefficients(right, dimension)
    bulk = toeplitz_from_coefficients(
        convolve_coefficients(left, translated_right), dimension
    )
    left_cross, right_cross, _ = cross_boundary_factors(
        left, translated_right, dimension
    )
    defect = left_cross @ right_cross
    finite_product = left_toeplitz @ diagonal @ right_toeplitz
    target = (bulk - defect) @ diagonal
    assert np.linalg.norm(finite_product - target, ord="fro") <= TOL * max(
        1.0, np.linalg.norm(target, ord="fro")
    )
    print("alternating Toeplitz--Hankel product identity passed")


def ratio_clusters(limit: int) -> dict[Fraction, list[tuple[PrimePowerAtom, PrimePowerAtom]]]:
    atoms = prime_power_atoms(limit)
    clusters: dict[
        Fraction, list[tuple[PrimePowerAtom, PrimePowerAtom]]
    ] = defaultdict(list)
    for left in atoms:
        for right in atoms:
            clusters[Fraction(left.n, right.n)].append((left, right))
    return clusters


def audit_ratio_multiplicity() -> None:
    limit = 300
    clusters = ratio_clusters(limit)
    primitive_count = 0
    chain_count = 0
    central_size = len(clusters[Fraction(1, 1)])
    for ratio, pairs in clusters.items():
        if ratio == 1:
            assert all(left.n == right.n for left, right in pairs)
            continue
        if ratio.numerator > 1 and ratio.denominator > 1:
            primitive_count += 1
            assert len(pairs) == 1
            left, right = pairs[0]
            assert left.prime != right.prime
        else:
            chain_count += 1
            bases = {left.prime for left, _ in pairs} | {
                right.prime for _, right in pairs
            }
            assert len(bases) == 1
    print(
        "ratio multiplicity classification passed: "
        f"primitive={primitive_count}, chains={chain_count}, "
        f"central-size={central_size}"
    )


def noncentral_chain_coefficient(limit: int) -> float:
    total = 0.0
    for prime in primes_up_to(limit):
        values = []
        power = prime
        while power <= limit:
            values.append(math.log(prime) / math.sqrt(power))
            if power > limit // prime:
                break
            power *= prime
        total += sum(values) ** 2 - sum(value * value for value in values)
    return total


def audit_chain_convergence() -> None:
    limits = (1_000, 10_000, 100_000)
    values = [noncentral_chain_coefficient(limit) for limit in limits]
    increments = [right - left for left, right in zip(values, values[1:])]
    assert all(value > 0.0 for value in values)
    assert all(increment > 0.0 for increment in increments)
    assert increments[-1] < increments[0]
    print(
        "noncentral same-prime l1 coefficients: "
        + ", ".join(
            f"X={limit}: {value:.8f}"
            for limit, value in zip(limits, values)
        )
    )


def primitive_odd_ratios(lower: int, upper: int) -> list[Fraction]:
    primes = [prime for prime in primes_up_to(upper) if lower <= prime <= upper and prime > 2]
    return sorted(
        {
            Fraction(numerator, denominator)
            for numerator in primes
            for denominator in primes
            if numerator != denominator
        }
    )


def audit_even_determinant_gap() -> None:
    boxes = ((50, 100), (100, 200), (200, 400))
    for lower, upper in boxes:
        ratios = primitive_odd_ratios(lower, upper)
        determinants = []
        scaled_log_gaps = []
        for left, right in zip(ratios, ratios[1:]):
            determinant = abs(
                left.numerator * right.denominator
                - left.denominator * right.numerator
            )
            determinants.append(determinant)
            scaled_log_gaps.append(
                upper**2 * abs(math.log(float(right / left)))
            )
        assert determinants
        assert all(determinant >= 2 and determinant % 2 == 0 for determinant in determinants)
        print(
            f"odd prime ratio box [{lower},{upper}]: ratios={len(ratios)}, "
            f"min-det={min(determinants)}, "
            f"min upper^2*log-gap={min(scaled_log_gaps):.6f}"
        )
    print("odd primitive determinant parity gap passed")


def main() -> None:
    audit_alternating_toeplitz_hankel_identity()
    audit_ratio_multiplicity()
    audit_chain_convergence()
    audit_even_determinant_gap()
    print("Alternating ratio-cluster audits passed.")


if __name__ == "__main__":
    main()

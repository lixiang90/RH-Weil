"""Finite audits for the radial ``+/- L`` alias seam.

The script checks three algebraic/arithmetic facts used in note 213:

1. the exact finite Toeplitz trace decomposition with a translated symbol;
2. the support gap for actual prime-power ratio atoms near a ``+L`` alias;
3. the trace-class bound for the finite-section Hankel remainder.

These are finite identity and geometry checks.  They do not supply a prime
asymptotic or any statement about zeta zeros.
"""

from __future__ import annotations

import bisect
import math
from dataclasses import dataclass

import numpy as np

from adjacent_bulk_edge_audit import prime_power_weights
from toeplitz_hankel_adjacent_audit import (
    convolve_coefficients,
    cross_boundary_factors,
    toeplitz_from_coefficients,
)


TOL = 5.0e-11


def hermitian_coefficients(
    rng: np.random.Generator, bandwidth: int
) -> dict[int, complex]:
    coefficients: dict[int, complex] = {0: complex(rng.normal())}
    for mode in range(1, bandwidth + 1):
        value = rng.normal() + 1j * rng.normal()
        coefficients[mode] = value
        coefficients[-mode] = value.conjugate()
    return coefficients


def audit_translated_trace_identity() -> None:
    rng = np.random.default_rng(213)
    dimension = 13
    length = 17.0
    spacing = 2.0 * math.pi / length
    delta = 6.3
    left = hermitian_coefficients(rng, 4)
    right = hermitian_coefficients(rng, 4)

    modulation = np.diag(
        np.exp(1j * spacing * delta * np.arange(dimension, dtype=float))
    )
    translated_right = {
        mode: np.exp(1j * mode * spacing * delta) * value
        for mode, value in right.items()
    }
    left_matrix = toeplitz_from_coefficients(left, dimension)
    right_matrix = toeplitz_from_coefficients(right, dimension)

    direct = np.trace(left_matrix @ modulation @ right_matrix)
    product_symbol = convolve_coefficients(left, translated_right)
    bulk_zero_mode = product_symbol.get(0, 0.0)
    dirichlet = np.trace(modulation)
    left_cross, right_cross, _ = cross_boundary_factors(
        left, translated_right, dimension
    )
    hankel_remainder = left_cross @ right_cross
    decomposed = bulk_zero_mode * dirichlet - np.trace(
        hankel_remainder @ modulation
    )

    assert abs(direct - decomposed) <= TOL * max(1.0, abs(direct))
    print("translated Toeplitz trace identity passed")


@dataclass(frozen=True)
class RatioAtom:
    ratio: float
    left_log: float
    right_log: float


def ratio_atoms(limit: int) -> list[RatioAtom]:
    prime_powers = prime_power_weights(limit)
    atoms: list[RatioAtom] = []
    for left in prime_powers:
        if left.n > limit // 2:
            continue
        left_log = math.log(left.n)
        for right in prime_powers:
            if right.n == left.n:
                continue
            if left.n * right.n > limit:
                continue
            atoms.append(
                RatioAtom(
                    ratio=left_log - math.log(right.n),
                    left_log=left_log,
                    right_log=math.log(right.n),
                )
            )
    atoms.sort(key=lambda atom: atom.ratio)
    return atoms


def nearest_atom(
    ordered_ratios: list[float], atoms: list[RatioAtom], target: float
) -> RatioAtom:
    location = bisect.bisect_left(ordered_ratios, target)
    candidates = atoms[max(0, location - 1) : min(len(atoms), location + 2)]
    return min(candidates, key=lambda atom: abs(atom.ratio - target))


def audit_alias_support_gap() -> None:
    alias_radius = 0.50
    assert alias_radius < math.log(2.0)
    for limit in (1_000, 5_000, 20_000):
        length = math.log(limit)
        atoms = ratio_atoms(limit)
        ordered_ratios = [atom.ratio for atom in atoms]
        checked = 0
        smallest_gap = math.inf
        largest_residual = 0.0
        for high in atoms:
            low = nearest_atom(ordered_ratios, atoms, high.ratio - length)
            delta = high.ratio - low.ratio
            epsilon = length - delta
            if abs(epsilon) >= alias_radius:
                continue

            # The +L alias forces the high ratio to be nonnegative and the
            # low ratio to be nonpositive.  Translation by delta modulo L is
            # translation by -epsilon in the physical u variable.
            assert high.ratio >= 0.0
            assert low.ratio <= 0.0
            high_lower = high.left_log - length / 2.0
            translated_low_lower = low.left_log - length / 2.0 - epsilon
            translated_low_upper = -length / 2.0 + high.ratio
            high_upper = length / 2.0

            # No translated interval wraps around the chosen period.
            assert translated_low_lower >= -length / 2.0 - TOL
            assert translated_low_upper <= length / 2.0 + TOL
            assert high_upper <= length / 2.0 + TOL

            gap = high_lower - translated_low_upper
            assert abs(gap - high.right_log) <= TOL
            assert gap >= math.log(2.0) - TOL
            checked += 1
            smallest_gap = min(smallest_gap, gap)
            largest_residual = max(largest_residual, abs(epsilon))

        assert checked > 0
        maximum_ratio_span = atoms[-1].ratio - atoms[0].ratio
        assert maximum_ratio_span <= 2.0 * length - 4.0 * math.log(2.0) + TOL
        assert 2.0 * length - maximum_ratio_span >= 4.0 * math.log(2.0) - TOL
        print(
            f"X={limit:>5d}: alias_pairs={checked:>5d}, "
            f"min_gap={smallest_gap:.6f}, "
            f"max_|epsilon|={largest_residual:.6f}, "
            f"2L-span={2.0 * length - maximum_ratio_span:.6f}"
        )


def audit_trace_class_remainder_bound() -> None:
    rng = np.random.default_rng(214)
    dimension = 19
    left = hermitian_coefficients(rng, 5)
    right = hermitian_coefficients(rng, 5)
    left_cross, right_cross, _ = cross_boundary_factors(
        left, right, dimension
    )
    remainder = left_cross @ right_cross
    trace_norm = float(np.linalg.svd(remainder, compute_uv=False).sum())
    factor_bound = float(
        np.linalg.norm(left_cross, ord="fro")
        * np.linalg.norm(right_cross, ord="fro")
    )
    assert trace_norm <= factor_bound + TOL * max(1.0, factor_bound)

    phases = np.exp(1j * rng.normal() * np.arange(dimension, dtype=float))
    diagonal_unitary = np.diag(phases)
    trace_pairing = abs(np.trace(remainder @ diagonal_unitary))
    assert trace_pairing <= trace_norm + TOL * max(1.0, trace_norm)
    print(
        "Hankel trace-class audit passed: "
        f"trace_norm={trace_norm:.8f}, factor_bound={factor_bound:.8f}"
    )


def main() -> None:
    audit_translated_trace_identity()
    audit_alias_support_gap()
    audit_trace_class_remainder_bound()
    print("radial alias-seam audits passed")


if __name__ == "__main__":
    main()

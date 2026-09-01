"""Finite audits for local alternating prime-power ratio boxes.

The script checks the local von Mangoldt L2/L1 budgets, the exact degree-two
structure of fixed determinant layers, and the associated sparse Schur norm.
It is an audit of the arithmetic indexing used in note 210; it does not prove
the asymptotic Chebyshev estimates or a global cross-box bound.
"""

from __future__ import annotations

import math
from collections import defaultdict

import numpy as np

from alternating_ratio_cluster_audit import PrimePowerAtom, prime_power_atoms


def dyadic_atoms(lower: int) -> list[PrimePowerAtom]:
    return [
        atom
        for atom in prime_power_atoms(2 * lower)
        if lower <= atom.n <= 2 * lower
    ]


def local_budgets(lower: int) -> tuple[int, float, float]:
    atoms = dyadic_atoms(lower)
    l2 = sum(atom.log_prime**2 / atom.n for atom in atoms)
    l1 = sum(atom.log_prime / math.sqrt(atom.n) for atom in atoms)
    return len(atoms), l2, l1


def audit_local_budgets() -> None:
    for lower in (1_000, 10_000, 100_000):
        count, l2, l1 = local_budgets(lower)
        assert count > 0 and l2 > 0.0 and l1 > 0.0
        print(
            f"local box [{lower},{2 * lower}]: atoms={count}, "
            f"W2/log(2Y)={l2 / math.log(2 * lower):.6f}, "
            f"W1/sqrt(Y)={l1 / math.sqrt(lower):.6f}, "
            f"count*log(Y)/Y={count * math.log(lower) / lower:.6f}"
        )


def primitive_pairs(
    numerator_lower: int, denominator_lower: int
) -> list[tuple[PrimePowerAtom, PrimePowerAtom]]:
    numerator_atoms = dyadic_atoms(numerator_lower)
    denominator_atoms = dyadic_atoms(denominator_lower)
    return [
        (numerator, denominator)
        for numerator in numerator_atoms
        for denominator in denominator_atoms
        if numerator.prime != denominator.prime
    ]


def determinant_edges(
    numerator_lower: int, denominator_lower: int, determinant: int
) -> tuple[int, list[tuple[int, int]], int, int]:
    pairs = primitive_pairs(numerator_lower, denominator_lower)
    pair_index = {
        (numerator.n, denominator.n): index
        for index, (numerator, denominator) in enumerate(pairs)
    }
    numerator_by_n = {
        atom.n: atom for atom in dyadic_atoms(numerator_lower)
    }
    denominator_by_n = {
        atom.n: atom for atom in dyadic_atoms(denominator_lower)
    }
    edges: list[tuple[int, int]] = []
    row_degrees: defaultdict[int, int] = defaultdict(int)
    column_degrees: defaultdict[int, int] = defaultdict(int)

    for source_index, (numerator, denominator) in enumerate(pairs):
        residue = (
            determinant * pow(numerator.n, -1, denominator.n)
        ) % denominator.n
        first = denominator_lower + (
            (residue - denominator_lower) % denominator.n
        )
        target_denominators = range(
            first, 2 * denominator_lower + 1, denominator.n
        )
        for target_denominator_n in target_denominators:
            target_denominator = denominator_by_n.get(target_denominator_n)
            if target_denominator is None:
                continue
            numerator_product = (
                numerator.n * target_denominator_n - determinant
            )
            if numerator_product % denominator.n:
                continue
            target_numerator_n = numerator_product // denominator.n
            target_numerator = numerator_by_n.get(target_numerator_n)
            if target_numerator is None:
                continue
            if target_numerator.prime == target_denominator.prime:
                continue
            target_index = pair_index[(target_numerator_n, target_denominator_n)]
            assert (
                numerator.n * target_denominator_n
                - denominator.n * target_numerator_n
                == determinant
            )
            edges.append((source_index, target_index))
            row_degrees[source_index] += 1
            column_degrees[target_index] += 1

    max_row = max(row_degrees.values(), default=0)
    max_column = max(column_degrees.values(), default=0)
    return len(pairs), edges, max_row, max_column


def audit_fixed_determinant_layers() -> None:
    boxes = ((50, 50), (50, 100), (100, 50), (100, 200))
    for numerator_lower, denominator_lower in boxes:
        for determinant in (-2, 2):
            size, edges, max_row, max_column = determinant_edges(
                numerator_lower, denominator_lower, determinant
            )
            assert max_row <= 2
            assert max_column <= 2
            matrix = np.zeros((size, size), dtype=float)
            for row, column in edges:
                matrix[row, column] = 1.0
            operator_norm = (
                float(np.linalg.svd(matrix, compute_uv=False)[0])
                if edges
                else 0.0
            )
            assert operator_norm <= 2.0 + 1.0e-12
            print(
                f"box A={numerator_lower}, B={denominator_lower}, "
                f"h={determinant:+d}: "
                f"vertices={size}, edges={len(edges)}, "
                f"degrees=({max_row},{max_column}), "
                f"adjacency-op={operator_norm:.6f}"
            )


def audit_log_gap_identity() -> None:
    numerator_lower = 100
    denominator_lower = 200
    for determinant in (-2, 2):
        pairs = primitive_pairs(numerator_lower, denominator_lower)
        _, edges, _, _ = determinant_edges(
            numerator_lower, denominator_lower, determinant
        )
        for source_index, target_index in edges:
            numerator, denominator = pairs[source_index]
            target_numerator, target_denominator = pairs[target_index]
            left = math.log(numerator.n / denominator.n)
            right = math.log(target_numerator.n / target_denominator.n)
            gap = abs(left - right)
            assert gap + 1.0e-15 >= abs(determinant) / (
                4.0 * numerator_lower * denominator_lower
            )
    print("fixed-layer logarithmic determinant gap passed")


def main() -> None:
    audit_local_budgets()
    audit_fixed_determinant_layers()
    audit_log_gap_identity()
    print("Alternating local-box audits passed.")


if __name__ == "__main__":
    main()

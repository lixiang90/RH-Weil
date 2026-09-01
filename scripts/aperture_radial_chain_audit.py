"""Finite audits for radial-chain closure and aperture seam compression.

The checks cover hyperbolic ratio spacing, local aperture L2/L1 budgets, the
Montgomery--Vaughan scaling proxy, far-aperture harmonic summability, and a
positive semidefinite path-Gram obstruction at the remaining seam scale.
They do not prove cancellation on the actual aperture seam Gram.
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction

import numpy as np

from alternating_ratio_cluster_audit import prime_power_atoms


def hyperbolic_ratio_data(
    limit: int, aperture_width: float = 1.0
) -> tuple[list[Fraction], dict[int, float], dict[int, float]]:
    atoms = prime_power_atoms(limit)
    ratios: list[Fraction] = []
    energy: defaultdict[int, float] = defaultdict(float)
    mass: defaultdict[int, float] = defaultdict(float)
    for numerator in atoms:
        for denominator in atoms:
            if numerator.n * denominator.n > limit:
                break
            if numerator.prime == denominator.prime:
                continue
            ratio = Fraction(numerator.n, denominator.n)
            log_ratio = math.log(float(ratio))
            aperture = math.floor(log_ratio / aperture_width)
            numerator_weight = numerator.log_prime / math.sqrt(numerator.n)
            denominator_weight = denominator.log_prime / math.sqrt(denominator.n)
            pair_mass = numerator_weight * denominator_weight
            ratios.append(ratio)
            energy[aperture] += pair_mass**2
            mass[aperture] += pair_mass
    assert len(ratios) == len(set(ratios))
    return sorted(ratios), dict(energy), dict(mass)


def audit_hyperbolic_spacing_and_budgets() -> None:
    for limit in (1_000, 5_000, 20_000):
        ratios, energy, mass = hyperbolic_ratio_data(limit)
        log_gaps = [
            math.log(float(right / left))
            for left, right in zip(ratios, ratios[1:])
        ]
        assert log_gaps
        scaled_gap = limit * min(log_gaps)
        logarithm = math.log(limit)
        max_energy_ratio = max(energy.values()) / logarithm**3
        max_mass_ratio = max(mass.values()) / math.sqrt(limit)
        block_ratio = len(energy) / logarithm
        assert scaled_gap >= 0.45
        assert max_energy_ratio < 1.0
        assert max_mass_ratio < 3.0
        assert block_ratio < 3.0
        print(
            f"hyperbola X={limit}: ratios={len(ratios)}, "
            f"X*min-log-gap={scaled_gap:.6f}, "
            f"maxS/L^3={max_energy_ratio:.6f}, "
            f"maxM/sqrtX={max_mass_ratio:.6f}, "
            f"blocks/L={block_ratio:.6f}"
        )


def circular_distance(value: float, period: float) -> float:
    residue = value % period
    return min(residue, period - residue)


def audit_far_aperture_harmonic_sum() -> None:
    for logarithm in (32.0, 64.0, 128.0, 256.0):
        indices = np.arange(-math.floor(logarithm), math.floor(logarithm) + 1)
        total = 0.0
        seam_edges = 0
        for left_index, left in enumerate(indices):
            for right in indices[left_index + 1 :]:
                distance = circular_distance(float(right - left), logarithm)
                if distance <= 2.0:
                    seam_edges += 1
                    continue
                total += 1.0 / (distance - 1.0)
        normalized = total / (logarithm * math.log(logarithm))
        assert normalized < 20.0
        assert seam_edges <= 12 * len(indices)
        print(
            f"aperture L={logarithm:g}: far/(L logL)={normalized:.6f}, "
            f"seam-edges={seam_edges}, blocks={len(indices)}"
        )


def audit_seam_path_no_go() -> None:
    for logarithm in (32, 64, 128, 256):
        block_count = logarithm
        main_scale = float(logarithm)
        diagonal = main_scale / logarithm
        neighbor = diagonal / 4.0
        gram = np.eye(block_count) * diagonal
        for index in range(block_count - 1):
            gram[index, index + 1] = neighbor
            gram[index + 1, index] = neighbor
        eigenvalues = np.linalg.eigvalsh(gram)
        aggregate = float(np.sum(gram))
        diagonal_sum = float(np.trace(gram))
        excess_ratio = (aggregate - diagonal_sum) / main_scale
        assert eigenvalues[0] > 0.0
        assert 0.45 <= excess_ratio < 0.5
        print(
            f"seam PSD L={logarithm}: min-eig={eigenvalues[0]:.6f}, "
            f"offdiag/N={excess_ratio:.6f}"
        )


def main() -> None:
    audit_hyperbolic_spacing_and_budgets()
    audit_far_aperture_harmonic_sum()
    audit_seam_path_no_go()
    print("Aperture radial-chain audits passed.")


if __name__ == "__main__":
    main()

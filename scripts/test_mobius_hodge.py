"""Finite exact checks for the Mobius--Hodge hard-channel identities."""

from __future__ import annotations

from fractions import Fraction

import mpmath as mp
import numpy as np

from mobius_hodge import (
    canonical_vaughan_hard_coefficients,
    divisibility_cylinder_gram,
    factorization_fiber_bessel_lower_bound,
    hard_channel_diagonal_energy_ledger,
    mobius_defect_second_moment,
    mobius_threshold_complex_data,
    truncated_mobius_divisor_sum,
    two_channel_hadamard_gram,
    weighted_partial_summation_ledger,
)


def main() -> None:
    # The truncated Mobius sum is simultaneously a face Euler characteristic,
    # a reduced-Hodge supertrace, and a one-vertex boundary-shell sum.
    for q in range(2, 91):
        for cutoff in (1, 2, 3, 5, 8, 13, 21):
            data = mobius_threshold_complex_data(q, cutoff)
            assert data["a"] == -data["reduced_euler_faces"]
            assert data["b"] == data["reduced_euler_faces"]
            assert data["b"] == data["hodge_supertrace"]
            assert data["a"] == data["boundary_shell"]["sum"]
            assert all(value >= 0 for value in data["betti"].values())

    # The limiting gcd form has an exact positive decomposition, while the
    # finite floor error and the absolute lcm majorant obey the proved bounds.
    for cutoff, length in ((3, 17), (5, 43), (8, 101)):
        moment = mobius_defect_second_moment(cutoff, length)
        assert moment["gcd_gram"] == moment["positive_decomposition"]
        assert moment["gcd_gram"] >= Fraction(0, 1)
        assert abs(moment["floor_remainder"]) <= cutoff**2
        assert moment["exact_moment"] <= moment["absolute_majorant"]

    # The lcm kernel is the exact Haar Gram of divisibility cylinders and is
    # positive for arbitrary complex (including twisted) coefficients.
    cylinder = divisibility_cylinder_gram(12)
    cylinder_float = np.array(
        [[float(value) for value in row] for row in cylinder]
    )
    assert np.linalg.eigvalsh(cylinder_float)[0] > -1e-12
    twisted = np.array(
        [complex(np.cos(index), np.sin(index)) for index in range(12)]
    )
    assert np.vdot(twisted, cylinder_float @ twisted).real >= -1e-12

    # Discrete Abel summation transfers the prefix second moment to every
    # decreasing weight without a hidden remainder.
    values = [truncated_mobius_divisor_sum(q, 7) ** 2 for q in range(1, 81)]
    weights = [Fraction(1, q + 2) for q in range(1, 81)]
    weighted = weighted_partial_summation_ledger(values, weights)
    assert weighted["left"] == weighted["right"]

    # For V>=U, the hard Type-I and Type-II coefficients sum to Lambda_{>U}
    # for every coefficient, independently of V.
    mp.mp.dps = 60
    for cutoff_v in (5, 9, 17):
        hard = canonical_vaughan_hard_coefficients(120, 4, cutoff_v)
        for n in range(1, 121):
            assert mp.almosteq(
                hard["hard_i"][n] + hard["hard_ii"][n],
                hard["target"][n],
                rel_eps=mp.mpf("1e-55"),
                abs_eps=mp.mpf("1e-55"),
            )

    # Weighted coefficient diagonals obey the exact divisor Cauchy majorant;
    # Type I is controlled by the target tail plus Type II coefficient energy.
    for parameters in ((100, 4, 7, 40.0, 0.5), (140, 6, 11, 70.0, 0.63)):
        diagonal = hard_channel_diagonal_energy_ledger(*parameters)
        assert all(
            row["type_ii_square"] <= row["cauchy_bound"] + mp.mpf("1e-55")
            for row in diagonal["pointwise"]
        )
        assert diagonal["type_ii_energy"] <= (
            diagonal["type_ii_cauchy_majorant"] + mp.mpf("1e-55")
        )
        assert diagonal["type_i_energy"] <= 2 * (
            diagonal["target_energy"] + diagonal["type_ii_energy"]
        ) + mp.mpf("1e-55")

    # Hadamard rotation isolates the physical sum and primitive difference;
    # the real cross entry is exactly one quarter of their energy difference.
    first = np.array([1 + 2j, -3 + 0.5j, 4 - 1j])
    second = np.array([-2 + 1j, 0.25 - 2j, 3 + 0.5j])
    gram = two_channel_hadamard_gram(first, second)
    expected = np.array(
        [
            [
                np.vdot(gram["physical"], gram["physical"]) / 2,
                np.vdot(gram["physical"], gram["primitive"]) / 2,
            ],
            [
                np.vdot(gram["primitive"], gram["physical"]) / 2,
                np.vdot(gram["primitive"], gram["primitive"]) / 2,
            ],
        ]
    )
    assert np.max(np.abs(gram["hadamard_gram"] - expected)) < 1e-12
    assert abs(gram["cross_identity_residual"]) < 1e-12

    # Exact-product collisions alone force the raw factorization synthesis
    # constant to be at least the largest fiber multiplicity.
    products = [30, 30, 30, 42, 42, 70]
    assert factorization_fiber_bessel_lower_bound(products) == 3

    print("Mobius threshold-Hodge and hard-channel checks passed.")


if __name__ == "__main__":
    main()

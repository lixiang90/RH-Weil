"""Compare algebraic Laurent channels with finite Vaughan component Grams.

This is a diagnostic, not an interval certificate and not evidence for RH.
It deliberately uses one common finite Feshbach normalization
``epsilon=tail_edge+lambda_1`` so that bases containing the physical vector
cannot win merely by sending the unused tail penalty to infinity.
"""

from __future__ import annotations

import argparse

import mpmath as mp

from qw_matrix import (
    channel_projector_stability_certificate,
    component_channel_feshbach_majorant,
    forced_physical_transverse_channel_basis,
    vaughan_paired_incidence_channel_certificate,
    vaughan_incidence_separated_channel_certificate,
    vaughan_incidence_separated_basis_from_ratios,
    incidence_separated_plane_angle_certificate,
    frozen_vaughan_tilted_incidence_basis,
    multiscale_vaughan_continuum_gauge_audit,
    orthonormal_channel_basis_from_seeds,
    vaughan_laurent_channel_data,
)


BASE_BLOCKS = [
    (80, 30, 2, [(2, 3), (4, 5), (6, 7), (8, 9)]),
    (80, 30, 8, [(2, 3), (4, 5), (6, 7), (8, 9)]),
    (160, 60, 2, [(3, 4), (6, 7), (9, 10), (12, 13)]),
    (160, 60, 8, [(3, 4), (6, 7), (9, 10), (12, 13)]),
]

EXTENDED_BLOCKS = [
    (80, 30, 4, [(2, 3), (4, 5), (6, 7), (8, 9)]),
    (80, 30, 16, [(2, 3), (4, 5), (6, 7), (8, 9)]),
    (160, 60, 4, [(3, 4), (6, 7), (9, 10), (12, 13)]),
    (160, 60, 16, [(3, 4), (6, 7), (9, 10), (12, 13)]),
    (240, 90, 8, [(4, 5), (8, 9), (12, 13), (16, 17)]),
]

FROZEN_TILTED_TEST_BLOCKS = [
    (320, 120, 4, [(5, 6), (10, 11), (15, 16), (20, 21)]),
    (320, 120, 16, [(5, 6), (10, 11), (15, 16), (20, 21)]),
]


def format_decimal(value: mp.mpf, digits: int = 6) -> str:
    return mp.nstr(value, digits, min_fixed=0, max_fixed=0)


def audit_block(block: tuple[int, int, int, list[tuple[int, int]]]):
    cutoff, abel_scale, center_height, cutoff_pairs = block
    gauge = multiscale_vaughan_continuum_gauge_audit(
        cutoff=cutoff,
        cutoff_pairs=cutoff_pairs,
        center_height=mp.mpf(center_height),
        log_window_width=mp.mpf("0.25") / center_height,
        horizontal_offset=mp.mpf("0.1"),
        abel_scale=mp.mpf(abel_scale),
        continuum_lag_start=mp.mpf("0.001"),
        continuum_lag_end=mp.log(cutoff + 1),
        continuum_lag_cells=20,
    )
    simplex = gauge["simplex_optimizer"]
    laurent = vaughan_laurent_channel_data(
        cutoff_pairs,
        simplex["optimal_scale_weights"],
        simplex["optimal_background_weights"],
    )
    integer = orthonormal_channel_basis_from_seeds(
        [[17, -1, 4, 10], [3, -17, -10, -2]], ambient_size=4
    )
    physicalized_integer = orthonormal_channel_basis_from_seeds(
        [[1, 1, 1, 1], [133, -134, -49, 50]], ambient_size=4
    )
    paired_small_integer = orthonormal_channel_basis_from_seeds(
        [[1, 1, 1, 1], [8, -8, -3, 3]], ambient_size=4
    )
    gram = gauge["simplex_component_gram"]
    incidence_certificate = vaughan_paired_incidence_channel_certificate(
        gram
    )
    separated_incidence = vaughan_incidence_separated_channel_certificate(
        gram
    )
    fixed_separated = frozen_vaughan_tilted_incidence_basis()
    separated_angle = incidence_separated_plane_angle_certificate(
        separated_incidence["physical_coarse_tilt"],
        separated_incidence["paired_ratio"],
        mp.mpf(1) / 20,
        mp.mpf(3),
    )
    unrestricted_optimal = incidence_certificate["unrestricted_optimal"]
    paired_optimal = incidence_certificate["paired_optimal"]
    candidates = [
        ("singular", laurent["singular_basis"]),
        ("singular-annihilator", laurent["singular_annihilator_basis"]),
        ("physical+double", laurent["physical_double_basis"]),
        ("physical+simple", laurent["physical_simple_basis"]),
        ("physical+regular", laurent["physical_regular_basis"]),
        ("integer", integer),
        ("physicalized-integer", physicalized_integer),
        ("paired-8:3", paired_small_integer),
        ("forced-physical-optimal", unrestricted_optimal["basis"]),
        ("paired-optimal", paired_optimal["basis"]),
        ("incidence-separated-optimal", separated_incidence["basis"]),
        ("tilted-(1/20,3)", fixed_separated),
    ]
    physical = mp.matrix([1, 1, 1, 1])
    rows = []
    for name, basis in candidates:
        stability = channel_projector_stability_certificate(
            gram, basis["full_channel_basis"], basis["core_rank"]
        )
        threshold = (
            stability["actual_tail_edge"]
            + stability["leading_eigenvalue"]
        )
        feshbach = component_channel_feshbach_majorant(
            gram,
            basis["full_channel_basis"],
            basis["core_rank"],
            tail_threshold=threshold,
        )
        projector = basis["core_projector"]
        overlap = mp.re(
            (physical.transpose_conj() * projector * physical)[0, 0]
        ) / 4
        physical_energy = feshbach["physical_energy"]
        excess = (
            (feshbach["physical_upper_bound"] / physical_energy - 1) * 100
        )
        rows.append({
            "basis": name,
            "rank": basis["core_rank"],
            "physical_overlap": overlap,
            "principal_sine": stability["maximum_principal_sine"],
            "relative_tail_edge": (
                stability["actual_tail_edge"]
                / stability["leading_eigenvalue"]
            ),
            "relative_coupling": (
                stability["actual_coupling_norm"]
                / stability["leading_eigenvalue"]
            ),
            "standardized_feshbach_excess_percent": excess,
            "loewner_minimum": feshbach[
                "minimum_majorant_difference_eigenvalue"
            ],
        })
    return gauge, laurent, rows, {
        "paired_optimal_ratio": incidence_certificate["optimal_ratio"],
        "paired_fixed_sine": incidence_certificate[
            "fixed_line_sine_direct"
        ],
        "unrestricted_paired_leakage": incidence_certificate[
            "coarse_leakage"
        ],
        "unrestricted_incidence_coordinates": incidence_certificate[
            "unrestricted_incidence_coordinates"
        ],
        "unrestricted_projected_ratio": incidence_certificate[
            "unrestricted_projected_ratio"
        ],
        "fixed_to_unrestricted_sine": incidence_certificate[
            "fixed_to_unrestricted_sine_direct"
        ],
        "incidence_certificate": incidence_certificate,
        "separated_incidence": separated_incidence,
        "separated_angle": separated_angle,
        "paired_optimal": paired_optimal,
        "unrestricted_optimal": unrestricted_optimal,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--extended", action="store_true", help="include five out-of-sample blocks"
    )
    parser.add_argument(
        "--only-extended",
        action="store_true",
        help="run only the five out-of-sample blocks",
    )
    parser.add_argument(
        "--frozen-test",
        action="store_true",
        help="run only two N=320 blocks held out from tilted-basis selection",
    )
    arguments = parser.parse_args()
    mp.mp.dps = 40
    if arguments.frozen_test:
        blocks = FROZEN_TILTED_TEST_BLOCKS
    elif arguments.only_extended:
        blocks = EXTENDED_BLOCKS
    else:
        blocks = BASE_BLOCKS + (EXTENDED_BLOCKS if arguments.extended else [])
    print(
        "| N,Y,T | basis | rank | physical overlap | sin theta | "
        "tail/lambda1 | coupling/lambda1 | standardized excess |"
    )
    print("|---:|:---|---:|---:|---:|---:|---:|---:|")
    for block in blocks:
        gauge, laurent, rows, incidence = audit_block(block)
        label = f"{block[0]},{block[1]},{block[2]}"
        for row in rows:
            if row["loewner_minimum"] < -mp.mpf("1e-30"):
                raise ArithmeticError("Feshbach Loewner certificate failed")
            print(
                f"| {label} | {row['basis']} | {row['rank']} | "
                f"{format_decimal(row['physical_overlap'])} | "
                f"{format_decimal(row['principal_sine'])} | "
                f"{format_decimal(row['relative_tail_edge'])} | "
                f"{format_decimal(row['relative_coupling'])} | "
                f"{format_decimal(row['standardized_feshbach_excess_percent'])}% |"
            )
        if max(
            abs(laurent[key])
            for key in (
                "mixed_double_sum_residual",
                "mixed_simple_sum_residual",
                "balanced_simple_sum_residual",
            )
        ) > mp.mpf("1e-30"):
            raise ArithmeticError("Laurent residue identities failed")
        if abs(gauge["direct_energy_residual"]) > mp.mpf("1e-30"):
            raise ArithmeticError("multiscale energy identity failed")
        print(
            f"paired-optimal ratio for {label}: "
            f"{format_decimal(mp.re(incidence['paired_optimal_ratio']), 10)}"
            f" {format_decimal(mp.im(incidence['paired_optimal_ratio']), 6)}i; "
            f"fixed sine={format_decimal(incidence['paired_fixed_sine'], 7)}; "
            f"coarse leakage="
            f"{format_decimal(incidence['unrestricted_paired_leakage'], 7)}; "
            f"unrestricted ratio="
            f"{format_decimal(mp.re(incidence['unrestricted_projected_ratio']), 8)}"
            f" {format_decimal(mp.im(incidence['unrestricted_projected_ratio']), 5)}i; "
            f"fixed-to-unrestricted sine="
            f"{format_decimal(incidence['fixed_to_unrestricted_sine'], 7)}"
        )
        print(
            f"separated ratios for {label}: tau="
            f"{format_decimal(mp.re(incidence['separated_incidence']['physical_coarse_tilt']), 9)}"
            f" {format_decimal(mp.im(incidence['separated_incidence']['physical_coarse_tilt']), 5)}i; "
            f"q={format_decimal(mp.re(incidence['separated_incidence']['paired_ratio']), 9)}"
            f" {format_decimal(mp.im(incidence['separated_incidence']['paired_ratio']), 5)}i; "
            f"fixed-plane sine="
            f"{format_decimal(incidence['separated_angle']['formula_projector_sine'], 7)}"
        )


if __name__ == "__main__":
    main()

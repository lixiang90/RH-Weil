"""Run the registered finite checks and named interval certificates.

These checks prove only their stated finite identities or interval bounds.
They are not asymptotic estimates and are not evidence for RH.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parent
CHECKS = (
    ("finite-check group coverage", [sys.executable, "test_check_groups.py"]),
    ("paper layout", [sys.executable, "check_repo_layout.py"]),
    ("paper layout regression", [sys.executable, "test_repo_layout.py"]),
    (
        "double Perron finite costs and existing cubic-boundary enclosures",
        [sys.executable, "hybrid_double_perron_checkpoint.py", "--check"],
    ),
    ("post-67.25 literature constants", [sys.executable, "post_6725_constant_audit.py"]),
    ("quartic boundary and normalization certificate", [sys.executable, "quartic_boundary_certificate.py"]),
    ("elliptic degree and odd-polarization benchmark", [sys.executable, "elliptic_degree_benchmark.py"]),
    (
        "portable Brownian component reduction",
        [sys.executable, "test_brownian_portable_reduction.py"],
    ),
    (
        "Mellin dual separator",
        [sys.executable, "test_mellin_dual_separator.py"],
    ),
    ("prolate boundary correction", [sys.executable, "test_prolate_candidate.py"]),
    ("QW formulas and tails", [sys.executable, "test_qw_bounds.py"]),
    (
        "frozen Vaughan/Laurent channels",
        [sys.executable, "audit_vaughan_laurent_channels.py", "--frozen-test"],
    ),
    (
        "Mobius threshold Hodge structure",
        [sys.executable, "test_mobius_hodge.py"],
    ),
    (
        "Selberg--Volterra cross-fiber transport",
        [sys.executable, "test_selberg_volterra.py"],
    ),
    (
        "Selberg profile equivalence bookkeeping",
        [sys.executable, "test_selberg_profile.py"],
    ),
    (
        "capped correspondence kernel",
        [sys.executable, "test_capped_correspondence.py"],
    ),
    (
        "reciprocal barrier and harmonic Schur",
        [sys.executable, "test_reciprocal_barrier.py"],
    ),
    (
        "square-completed background and Schur--L4",
        [sys.executable, "test_square_completed_background.py"],
    ),
    (
        "tracial lattice-clipped background",
        [sys.executable, "test_lattice_clipped_background.py"],
    ),
    (
        "finite arithmetic cone and Hodge transgression",
        [sys.executable, "test_nonconstructive_routes.py"],
    ),
    (
        "soft negative effect and Cauchy moments",
        [sys.executable, "test_soft_negative_moment.py"],
    ),
    (
        "formal soft zeta orbit response",
        [sys.executable, "audit_soft_zeta_orbit.py"],
    ),
    (
        "nonvacuous Vaughan--Brownian physical Schur completion",
        [sys.executable, "vaughan_brownian_schur_audit.py"],
    ),
    (
        "Brownian common-convolution sign obstruction",
        [sys.executable, "brownian_convolution_sign_obstruction_audit.py"],
    ),
    (
        "symmetric spectral sign and overlap degeneration",
        [sys.executable, "symmetric_spectral_overlap_no_go_audit.py"],
    ),
    (
        "Brownian interval denominator and TV perturbation",
        [sys.executable, "test_brownian_interval_certificate.py"],
    ),
    (
        "B1f floating forward-error ledger",
        [sys.executable, "test_b1f_forward_error.py"],
    ),
    (
        "B1e exact surrogate support and denominator",
        [sys.executable, "inspect_b1e_response_support.py"],
    ),
    (
        "B1f intended finite denominator certificate",
        [sys.executable, "b1f_base_coefficient_interval_audit.py"],
    ),
    (
        "B1g fixed-point trigonometric ledger",
        [sys.executable, "test_b1g_fixed_intervals.py"],
    ),
    (
        "B1g directed finite numerator certificate",
        [sys.executable, "b1g_directed_numerator_interval_audit.py"],
    ),
    (
        "B1h second-scale interval helpers",
        [sys.executable, "test_b1h_second_scale_intervals.py"],
    ),
    (
        "B1h second-scale directed finite certificate",
        [sys.executable, "b1h_second_scale_interval_audit.py"],
    ),
    (
        "B1i normalized common-core exact helpers",
        [sys.executable, "test_b1i_normalized_common_core.py"],
    ),
    (
        "B1i normalized two-scale common-core certificate",
        [sys.executable, "b1i_normalized_common_core_certificate.py"],
    ),
    (
        "B1j Stieltjes transfer and fixed-lag diagnostics",
        [sys.executable, "b1j_stieltjes_fixed_lag_audit.py"],
    ),
    (
        "B1l balanced-core multiplier degeneracy",
        [sys.executable, "b1l_multiplier_degeneracy_audit.py"],
    ),
    (
        "B1m universal raw Brownian limit",
        [sys.executable, "b1m_raw_brownian_limit_audit.py"],
    ),
    (
        "Vaughan scalarized spectral ratio capture",
        [sys.executable, "vaughan_spectral_ratio_capture_audit.py"],
    ),
    (
        "partial Weil proportions and depth visibility",
        [sys.executable, "partial_weil_audit.py"],
    ),
    (
        "positive-background quotient rank and trace",
        [sys.executable, "positive_background_quotient_audit.py"],
    ),
    (
        "critical-window clustered and periodic visibility",
        [sys.executable, "critical_window_visibility_audit.py"],
    ),
    (
        "MT triple exact rational certificate and spectral slack",
        [sys.executable, "mt_triple_slack_audit.py"],
    ),
    (
        "quadratic fourth-moment channels",
        [sys.executable, "fourth_moment_channel_audit.py"],
    ),
    (
        "smooth fourth-window cycle",
        [sys.executable, "smooth_fourth_window_audit.py"],
    ),
    (
        "operator fourth words and localizer completion",
        [sys.executable, "operator_fourth_localizer_audit.py"],
    ),
    (
        "adjacent-product bulk edge tightness",
        [sys.executable, "adjacent_bulk_edge_audit.py", "--limits", "20000", "100000"],
    ),
    (
        "Toeplitz--Hankel adjacent transfer",
        [sys.executable, "toeplitz_hankel_adjacent_audit.py"],
    ),
    (
        "alternating ratio multiplicity and square-root core",
        [sys.executable, "alternating_ratio_cluster_audit.py"],
    ),
    (
        "alternating local weights and determinant layers",
        [sys.executable, "alternating_local_box_audit.py"],
    ),
    (
        "radial cross-box coherence obstruction",
        [sys.executable, "radial_cross_box_obstruction_audit.py"],
    ),
    (
        "aperture radial-chain and seam compression",
        [sys.executable, "aperture_radial_chain_audit.py"],
    ),
    (
        "radial alias-seam translated support gap",
        [sys.executable, "alias_seam_overlap_audit.py"],
    ),
    (
        "ordinary seam and semiprime harmonic correlation",
        [sys.executable, "ordinary_seam_kernel_audit.py"],
    ),
    (
        "supercritical logarithmic collar coordinates",
        [sys.executable, "supercritical_collar_coordinate_audit.py"],
    ),
    (
        "transition-scale signed ratio kernel",
        [sys.executable, "transition_ratio_kernel_audit.py"],
    ),
    (
        "balanced transition-core frame and affine fibers",
        [sys.executable, "transition_core_frame_audit.py"],
    ),
    (
        "clustered Fejer transition closure",
        [sys.executable, "clustered_fejer_transition_audit.py"],
    ),
    (
        "critical logarithmic-square local boxes",
        [sys.executable, "critical_local_box_audit.py"],
    ),
    (
        "balanced Selberg--Kloosterman local density",
        [sys.executable, "balanced_sieve_density_audit.py"],
    ),
    (
        "unbalanced critical two-regime sieve",
        [sys.executable, "unbalanced_critical_sieve_audit.py"],
    ),
    (
        "adjacent Montgomery--Vaughan and boundary no-go",
        [sys.executable, "adjacent_mv_boundary_no_go_audit.py"],
    ),
    (
        "supercritical boundary pseudocovariance",
        [sys.executable, "supercritical_pseudocovariance_audit.py"],
    ),
    (
        "boundary quarter-turn and locality obstruction",
        [sys.executable, "boundary_quarter_turn_audit.py"],
    ),
    (
        "first boundary-entry positive mean square",
        [sys.executable, "boundary_entry_mean_square_audit.py"],
    ),
    (
        "short-height Hilbert adjacent closure",
        [sys.executable, "adjacent_short_height_audit.py"],
    ),
    (
        "short-height signed 3+1 and 4+0 bulk closure",
        [sys.executable, "short_height_31_40_audit.py"],
    ),
    (
        "fourfold signed Toeplitz boundary closure",
        [sys.executable, "fourfold_toeplitz_boundary_audit.py"],
    ),
    (
        "Archimedean zero-frequency background reduction",
        [sys.executable, "archimedean_background_audit.py"],
    ),
    (
        "deterministic-background mixed-frequency closure",
        [sys.executable, "mixed_background_evacuation_audit.py"],
    ),
    (
        "relative-dense moving zero-block transfer",
        [sys.executable, "relative_dense_zero_block_audit.py"],
    ),
    (
        "external-input reverse-audit identities",
        [sys.executable, "external_input_reverse_audit.py"],
    ),
    (
        "cyclic fourth-constant reconstruction",
        [sys.executable, "cyclic_fourth_constant_reconstruction.py"],
    ),
    (
        "alternating central/noncentral cross repair",
        [sys.executable, "alternating_central_cross_audit.py"],
    ),
    (
        "alternating high-product support obstruction",
        [sys.executable, "alternating_high_product_tail_audit.py"],
    ),
    (
        "alternating aperture-depth and power-high ceiling",
        [sys.executable, "alternating_aperture_depth_audit.py"],
    ),
    (
        "power-high Gabor band-pass and core-tail cancellation",
        [sys.executable, "power_high_bandpass_audit.py"],
    ),
    (
        "exact finite dyadic band-discrepancy scales",
        [sys.executable, "exact_dyadic_band_audit.py"],
    ),
    (
        "power-high prime response-measure diagnostics",
        [sys.executable, "power_high_prime_measure_audit.py"],
    ),
    (
        "power-high elementary mass-ledger exponents",
        [sys.executable, "power_high_mass_scale_audit.py"],
    ),
    (
        "cumulative discrepancy versus exact band response no-go",
        [sys.executable, "cumulative_discrepancy_band_no_go_audit.py"],
    ),
    (
        "band energy versus physical response direction no-go",
        [sys.executable, "band_energy_physical_direction_no_go_audit.py"],
    ),
    (
        "power-high physical one-factor Vaughan channels",
        [sys.executable, "power_high_physical_vaughan_channel_audit.py"],
    ),
    (
        "centered Mobius divisor pullback and dyadic Abel blocks",
        [sys.executable, "mobius_divisor_pullback_audit.py"],
    ),
)

GROUPS = ("all", "core", "b1h", "b1i")
HEAVY_CHECK_SCRIPTS = {
    "b1h": "b1h_second_scale_interval_audit.py",
    "b1i": "b1i_normalized_common_core_certificate.py",
}


def checks_for_group(group: str = "all", checks=None):
    """Partition the registry without changing any check or its arguments.

    New ordinary checks belong to core automatically.  The two heavy checks
    must each exist exactly once, so renaming or duplicating one cannot
    silently produce an empty job or remove work from the parallel suite.
    """
    if group not in GROUPS:
        raise ValueError(f"unknown check group: {group!r}")
    registered = tuple(CHECKS if checks is None else checks)
    heavy = {
        name: tuple(
            check for check in registered
            if Path(check[1][1]).name == script
        )
        for name, script in HEAVY_CHECK_SCRIPTS.items()
    }
    for name, selected in heavy.items():
        if len(selected) != 1:
            raise ValueError(
                f"group {name!r} requires exactly one registered "
                f"{HEAVY_CHECK_SCRIPTS[name]}; found {len(selected)}"
            )
    if group == "all":
        selected = registered
    elif group == "core":
        selected = tuple(
            check for check in registered
            if Path(check[1][1]).name not in HEAVY_CHECK_SCRIPTS.values()
        )
    else:
        selected = heavy[group]
    if not selected:
        raise ValueError(f"check group {group!r} is empty")
    return selected


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--group", choices=GROUPS, default="all",
        help="all checks (default), ordinary core checks, or one heavy certificate",
    )
    args = parser.parse_args(argv)
    selected = checks_for_group(args.group)
    for label, command in selected:
        print(f"==> {label}", flush=True)
        subprocess.run(command, cwd=SCRIPTS, check=True)
    if args.group == "all":
        print("All finite sanity checks passed.")
    else:
        print(f"Finite sanity checks passed (group={args.group}, checks={len(selected)}).")


if __name__ == "__main__":
    main()

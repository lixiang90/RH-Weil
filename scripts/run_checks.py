"""Run all reproducible finite sanity checks.

These checks validate implementation identities only. They are not interval
certificates and are not evidence for RH.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parent
CHECKS = (
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
        "partial Weil proportions and depth visibility",
        [sys.executable, "partial_weil_audit.py"],
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

)

def main() -> None:
    for label, command in CHECKS:
        print(f"==> {label}", flush=True)
        subprocess.run(command, cwd=SCRIPTS, check=True)
    print("All finite sanity checks passed.")


if __name__ == "__main__":
    main()

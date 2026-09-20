"""Check finite-shift invariance and boundary-rank algebra with pinned Lean."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["finiteShiftInvariant_zero","boundaryRank_kernel","boundaryRank_surjective","boundaryRank_positive_zero","boundaryRank_signed_iff","unequalLength_residual","cyclicDegrees_determinant"],
        source_files=["F1/Analysis/BoundaryGluing.lean", "checks/BoundaryGluingAudit.lean"],
        report_prefix="boundary-gluing",
        scope="Seven finite-support shift, rank-boundary and scalar-residual results. No quotient topology, C*-extension, Morita, PV, Bott, K-theory or full F1 build.",
    )

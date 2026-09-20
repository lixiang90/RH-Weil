"""Check boundary-clutch algebra using the pinned Lean runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=['stepWeighted_transport', 'geometricPhase_transport', 'weightedPermutation_det', 'iterate_unitDrift', 'no_bounded_unitDrift'],
        source_files=["F1/Analysis/BoundaryClutch.lean", "checks/BoundaryClutchAudit.lean"],
        report_prefix="boundary-clutch",
        scope='Five algebraic checks of shift transport, phase, weighted permutation determinant and bounded integer drift. No continuity, winding number, Fredholm, Morita, K-theory or full F1 build is formalized.',
    )

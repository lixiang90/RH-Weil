"""Check finite-chain and backward-shift algebra using the pinned Lean runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["nilpotentGeometric_right","nilpotentGeometric_left","backwardResolvent_factor","backwardResolvent_rightInverse"],
        source_files=["F1/Analysis/BoundaryResolvent.lean", "checks/BoundaryResolventAudit.lean"],
        report_prefix="boundary-resolvent",
        scope="Four algebraic geometric-inverse and backward-resolvent results. No operator convergence, Fredholm index, heat trace, adele geometry or full F1 build is formalized.",
    )

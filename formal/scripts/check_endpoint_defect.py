"""Check endpoint isometry defect algebra with the pinned Lean runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=['leftInverseDefect_mul', 'leftInverseDefect_left', 'leftInverseDefect_idempotent', 'leftInverse_powers', 'leftInverseDefect_distinctPowers', 'leftInverseDefect_ne_zero'],
        source_files=["F1/Analysis/EndpointDefect.lean", "checks/EndpointDefectAudit.lean"],
        report_prefix="endpoint-defect",
        scope='Six algebraic left-inverse defect identities, including power cancellation and distinct wandering sectors. No Hilbert convergence, C*-quotient, trace, K-theory or full F1 build is formalized.',
    )

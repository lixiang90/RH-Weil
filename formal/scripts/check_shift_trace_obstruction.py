"""Algebraic trace obstruction; analytic operator realization is separate."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["shift_commutator_defect","cyclic_map_kills_shift_defect","nonzero_shift_defect_not_cyclic"],
        source_files=["F1/Analysis/ShiftTraceObstruction.lean", "checks/ShiftTraceObstructionAudit.lean"],
        report_prefix="shift-trace-obstruction",
        scope="Three algebraic shift-commutator and additive cyclic-trace obstruction identities. No time crossed-product isomorphism, operator realization, trace weights, norm-density theorem, source noncompactness or full F1 build.",
    )

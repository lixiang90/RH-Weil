"""Exact multiplication-defect algebra; analytic traces are separate."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["multiplication_defect_associativity","antisymmetrized_defect_boundary","weighted_commutator_transfer"],
        source_files=["F1/Analysis/WeightedTraceDefect.lean","checks/WeightedTraceDefectAudit.lean"],
        report_prefix="weighted-trace-defect",
        scope="Three ring identities for multiplication defect associativity, its antisymmetrized boundary and weighted commutator transfer. No Schatten ideals, analytic trace, Fourier density, cyclic cohomology or full F1 build.",
    )

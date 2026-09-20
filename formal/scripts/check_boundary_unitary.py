"""Check the explicit boundary shift and finite flux identities with pinned Lean."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["positiveTail_leftInverse","positiveTail_rankOneDefect","positiveTail_injective","finiteFlux","finiteFlux_one_to_zero","weightedFiniteFlux"],
        source_files=["F1/Analysis/BoundaryUnitary.lean", "checks/BoundaryUnitaryAudit.lean"],
        report_prefix="boundary-unitary",
        scope="Six sequence shift and finite flux identities. No Hilbert boundedness, C*-algebra, corner, Fredholm index, geometry or full F1 build.",
    )

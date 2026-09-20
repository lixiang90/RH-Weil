"""Check four unit-descent algebra lemmas with the pinned shared runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["regularUnitInvariant_iff","unitQuotient_factor_iff","unitQuotient_obstruction","moment_preservation_obstruction"],
        source_files=["F1/Analysis/UnitDescent.lean", "checks/UnitDescentAudit.lean"],
        report_prefix="unit-descent",
        scope="Four algebraic unit-descent tests. Regular-unit identification, analytic determinants and geometry remain unformalized. No full F1 build.",
    )

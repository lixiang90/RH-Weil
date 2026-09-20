"""Check the eight algebraic TraceRadical results using the pinned shared runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=['momentCorrectedPairing_radical', 'quarterMoments_self_pairing', 'quarterMoments_not_radical', 'degree_basis_moments', 'codegree_basis_moments', 'remove_two_moments', 'two_moment_coordinates_unique', 'trace_kernel_radical_iff_moments'],
        source_files=["F1/Analysis/TraceRadical.lean", "checks/TraceRadicalAudit.lean"],
        report_prefix="trace-radical",
        scope="Eight moment/trace algebra lemmas. Analytic identities remain explicit hypotheses; no full F1 build or principal-divisor construction.",
    )

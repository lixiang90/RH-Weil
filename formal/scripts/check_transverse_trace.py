"""Check geometric tails and affine-index obstructions with the pinned Lean runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["coherentTail_hasSum","coherentTail_normalized","coherentTail_overlap","affine_secondDifference","geometric_secondDifference","coherentTail_not_affine","commonMixedTerm_weight"],
        source_files=["F1/Analysis/TransverseTrace.lean", "checks/TransverseTraceAudit.lean"],
        report_prefix="transverse-trace",
        scope="Seven geometric-tail sum and affine-index obstruction results. No p-adic Hilbert construction, suspension, operator trace, K-theory or full F1 build.",
    )

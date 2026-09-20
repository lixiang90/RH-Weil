"""Check crossed-product coordinate algebra with the pinned Lean runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["weightedPull_mul","weightedPull_pow_form","weightedPull_diagonal_zero","weightedPull_pow_diagonal_zero","weightedWord_form","weightedWord_diagonal_zero","weightedPull_inverse_pair","loopResiduePolynomial_pos", "lowerBoundedRecurrence_zero"],
        source_files=["F1/Analysis/WeightedArrows.lean", "checks/WeightedArrowsAudit.lean"],
        report_prefix="weighted-arrows",
        scope="Nine coordinate-algebra, bounded-recurrence and residue-polynomial results. No Hilbert trace, determinant, adele construction or full F1 build is formalized.",
    )

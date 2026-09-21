"""Check the noncommutative matrix identities of note 415 with pinned Lean."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=['block2_mul', 'block2_one', 'dilation_left', 'dilation_right', 'defect_diagonal', 'commutator_transfer', 'firstBlock_idempotent', 'dilation_projection', 'dilation_projection_idempotent', 'defect_projection_difference', 'defect_projection_diagonal', 'block2_conjTranspose', 'sqrt_intertwining_adjoint', 'dilation_conjTranspose', 'dilation_unitary', 'defect_projection_selfAdjoint', 'defect_projection', 'shell_overlap_cancel'],
        source_files=["F1/Analysis/DefectProjection.lean", "checks/DefectProjectionAudit.lean"],
        report_prefix="defect-projection",
        scope="Actual two-by-two matrix identities, self-adjoint idempotent, defect diagonal, shell scalar cancellation and commutator transfer. No C* positivity, functional calculus, ideal membership, Hilbert estimates, trace convergence or full F1 build.",
    )

"""Algebraic checks for the next projection-connection candidate."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=['projection_derivative_corner', 'projection_connection_commutator', 'projection_connection_corner', 'corner_derivative_parallel', 'compressed_connection_defect', 'projection_connection_skew'],
        source_files=["F1/Analysis/ProjectionConnection.lean", "checks/ProjectionConnectionAudit.lean"],
        report_prefix="projection-connection",
        scope="Six algebraic projection-derivative, corner-parallelism, skew-adjoint and compression identities. No actual Green corner derivative, unbounded connection, evolution, equivariance, trace comparison or full F1 build.",
    )

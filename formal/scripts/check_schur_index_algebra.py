"""Noncommutative Schur identities; analytic family-index theory is separate."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["schur_upper_inverse","schur_lower_inverse","schur_lower_elimination","schur_upper_elimination"],
        source_files=["F1/Analysis/SchurIndexAlgebra.lean","checks/SchurIndexAlgebraAudit.lean"],
        report_prefix="schur-index-algebra",
        scope="Four generic-ring Schur elimination and triangular inverse identities. No rectangular Hilbert-space analysis, Hardy estimates, family index, Chern sign, arithmetic trace or full F1 build.",
    )

"""Reusable cocycle and connection identities; no analytic evolution claim."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["right_twisted_cocycle_group_law","left_cocycle_group_law","compressed_parallel_defect","parallel_factor_derivative"],
        source_files=["F1/Analysis/ConnectionEvolutionAlgebra.lean", "checks/ConnectionEvolutionAlgebraAudit.lean"],
        report_prefix="connection-evolution-algebra",
        scope="Four algebraic right/left cocycle group-law, compressed-parallel defect and phase-factor derivative identities. No analytic Dyson existence, domain, equivariance, GNS or trace-class formalization; no full F1 build.",
    )

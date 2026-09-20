"""Check finite-visit product estimates with the pinned Lean runner."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["visitMajorant_product","visitMajorant_pointwise","finiteVisitProductBound","orbit_interval_span"],
        source_files=["F1/Analysis/OrbitDecay.lean", "checks/OrbitDecayAudit.lean"],
        report_prefix="orbit-decay",
        scope="Four finite-product and interval-span results. No Banach completion, spectral radius, adele geometry or full F1 build is formalized.",
    )

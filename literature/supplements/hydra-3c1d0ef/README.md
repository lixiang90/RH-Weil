# Independent verification of *zeta-23*, and a public witness for its bandwidth-one ceiling

This repository contains an independent third-party verification of the results of

> L. Alpöge and R. Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637v1 (submitted 13 August 2026; a v2 dated 19 August 2026 adds provenance and extension material without altering the main theorems — this report audits v1), with Lean 4 formalization at [`anthropics/zeta-23-lean`](https://github.com/anthropics/zeta-23-lean),

together with an independently constructed, fully public **witness law** for the paper's bandwidth-one ceiling.

Everything here is reproducible from public materials. We introduce no new claims about the Riemann zeta function.

**Prior work.** We are not the first to check parts of this. An independent kernel rebuild and axiom audit
was published by [`stevemoraco/qs` PR #363](https://github.com/stevemoraco/qs/pull/363) on 13 August 2026,
and an independent reproduction of the ceiling data from the published enclosures by
[`teal-sea/zeta-lab` PR #12](https://github.com/teal-sea/zeta-lab/pull/12) on 11 August 2026 — the latter
obtaining the same digits we did. The `EnclOK` availability gap was raised in repository issues
[#8](https://github.com/anthropics/zeta-23-lean/issues/8) and
[#14](https://github.com/anthropics/zeta-23-lean/issues/14), both still open. Findings 1, 3 and 4 below
therefore corroborate work others published first. What is new here is finding 2 — a statement-fidelity
audit, which no other effort has attempted — and finding 5, an independently constructed witness.

**Author:** Bryan Carson, Hydra Dynamix — <bcarson@hydradynamix.com>
**Date:** 21 August 2026

## Summary of findings

| # | Finding | Status |
|---|---|---|
| 1 | The Lean formalization builds from source on independent hardware and all **34** headline theorems depend on exactly the three standard axioms, sorry-free | **Confirmed** |
| 2 | All **15** trusted definitions and **17** challenge statements faithfully encode the paper's informal claims | **Confirmed, 0 discrepancies** |
| 3 | The numerical certificate behind the ~0.682 ceiling (`cert_N256_blk_b128m.json`) is **not public**, so `EnclOK` cannot be verified by anyone outside the authors | **Data-availability gap** |
| 4 | The integer certificate layer downstream of `EnclOK` (255 row inequalities, edge bound, p₀ arithmetic) reproduces exactly under an independent implementation | **Confirmed** |
| 5 | An independently constructed witness law certifies a bandwidth-one ceiling of **p = 0.681810782**, **below** the paper's p₀ = 0.681828687 by **1.79 × 10⁻⁵** — at the paper's own edge bound, with every link publicly reproducible | **New artifact** |
| 6 | That witness is **verified in the Lean kernel** by instantiating the paper's own generic ceiling theorem, on the same three standard axioms and with no `sorry` — the first machine-checked bandwidth-one ceiling derived from a *public* certificate | **New artifact** |

Findings 1, 2 and 4 support the paper (1 and 4 independently corroborating earlier third-party checks; see *Prior work* above). Finding 3 concerns reproducibility of one auxiliary section, not the correctness of the main theorems — **Theorems A–E are provably independent of the certificate in question**, as our axiom audit confirms. The repository's README and the paper both document the certificate's status accurately; the gap is availability, not disclosure.


## Why findings 5 and 6 matter

The paper's §7.2 shows that no *bandwidth-one certificate* — the entire method class its main theorem
belongs to — can prove more than ≈ 0.6819 of zeros simple and on the critical line. That upper bound is
established by exhibiting a witness law: a configuration law matching the pair-correlation data zeta is
known to have, but containing only p₀ = 68.18% simple zeros.

That witness rests on a certificate file which is not distributed (finding 3). Ours is different in two
ways.

**It is lower.** Our certified value is p = 0.681810782, below the paper's p₀ = 0.681828687 by
1.79 × 10⁻⁵. A *lower* witness is a *stronger* result: it shows the method class is more limited than
the published witness alone establishes. It satisfies the paper's own edge bound |D(1)| ≤ 0.82395317
(we measure 0.823950881), so the two ceiling statements differ only in the band tolerance τ — ours
1/10⁷, theirs 3/10⁴⁰ — which moves the downstream error constant by 1.95 × 10⁻¹⁰, four orders below
the improvement.

**It is checkable.** Every position, weight and enclosure is in this repository. The certification is
exact-rational and interval-arithmetic; `witness/verify_law.py` re-checks it from the artifact alone in
seconds with no dependencies. And `witness/lean/` instantiates the paper's *own* generic ceiling theorem
(`ceiling_nearCUE`) on our law, so the ceiling is verified by Lean's kernel rather than by our Python:

```
LawHD256_check     depends on axioms: [propext]
lawHD256_rows      depends on axioms: [propext, Classical.choice, Quot.sound]
ceiling_lawHD256   depends on axioms: [propext, Classical.choice, Quot.sound]
```

— the same axiom profile as the paper's `ceiling_law256`, no `sorry`, no added hypotheses.
`LawHD256_check` passes by `decide +kernel` on `propext` alone, meaning Lean re-verified all 256 row
enclosures and both edge-bound inequalities as integer arithmetic. Because the paper's certificate file
is not distributed, its `EnclOK` cannot be discharged by anyone outside the authors; this is, to our
knowledge, the first kernel-verified bandwidth-one ceiling obtained from a public certificate.

**What this is not.** This is a *ceiling* on a method class, not a lower bound on the proportion of
zeros. It does **not** improve the paper's 67.25% result, which would require a better certificate
rather than a better witness. What it does is tighten the published obstruction and make it
independently verifiable.

## Layout

```
audit/
  build-summary.txt              build + axiom-audit transcript (finding 1)
  statement-fidelity-audit.md    per-definition and per-statement verdicts (finding 2)
  paper-reference-extraction.md  the paper-side reference the audit was diffed against
  independent_rowcheck.py        independent re-implementation of the RowCert checker (finding 4)
  rowcheck-output.txt            its output
witness/
  law_certified.txt              the certified witness: exact rational p, integer enclosures, support
  verify_law.py                  standalone exact-arithmetic verifier for the above (no dependencies)
  colgen.py colgen2.py           column generation (stage 1: positions; stage 2: mark moves)
  colgen3.py colgen4.py          faster pricers (FFT kernel; global-field coordinate descent)
  certify_cg.py                  dyadic snap + rigorous interval-enclosure certification
  extract_dual.py                extracts the optimal certificate (LP dual) from a snapshot
NOTE.md                          the technical note: methods, results, limitations
```

## Reproducing the audit (findings 1, 2, 4)

```sh
# 1. build the formalization and audit its axioms (~30 min with the Mathlib cache)
git clone https://github.com/anthropics/zeta-23-lean && cd zeta-23-lean
lake exe cache get && lake build && lake build Solution Solution.XiPrime
lake env lean comparator/PrintAxioms.lean            # expect: the three standard axioms only
lake env lean comparator/PrintAxioms/XiPrime.lean
lake env lean comparator/PrintAxioms/PairCeiling.lean

# 2. re-run the independent integer-certificate check (seconds, no dependencies)
python audit/independent_rowcheck.py path/to/zeta-23-lean/Zeta23/PairCeiling/LawN256.lean
```

Statement fidelity (finding 2) is a reading task: `audit/statement-fidelity-audit.md` gives per-item verdicts for
`comparator/ChallengeDeps.lean` (15 definitions) and `comparator/Challenge.lean` (17 statements) against the paper.

## Reproducing the witness (finding 5)

**Verifying the witness takes seconds and needs nothing but Python** — the certified law is
self-contained, so a skeptical reader never has to re-run the search:

```sh
cd witness && python verify_law.py        # exact rational arithmetic, no dependencies
# -> 255 rows checked, 0 band failures, certified p = 0.681810782,
#    gap to p0 = -0.000017906 (BELOW p0), edge bound OK
```

Regenerating the law from scratch (many hours, stochastic):

```sh
pip install numpy scipy mpmath
cd witness
# column generation with dual stabilisation; the D(1) edge bound is carried in the master,
# because E[F(256)] is a free direction for lowering p and an unconstrained solve drifts
# above the paper's cap and produces an inadmissible law.
python wholelaw_stab.py <state-tag> 60 12 3 5 0.15
# rigorous certification: dyadic snap + exact rational weights + interval enclosures
CERT_SNAP_BITS=44 CERT_PREC=260 python certify2.py <pool.pkl> law_certified.txt 1e-7 0.00000009
```

Re-checking the Lean ceiling (needs the paper's repository and its Mathlib cache):

```sh
git clone https://github.com/anthropics/zeta-23-lean && cd zeta-23-lean
lake exe cache get
cp ../witness/lean/LawHD256.lean ../witness/lean/CeilingLawHD256.lean Zeta23/PairCeiling/
lake build Zeta23.PairCeiling.CeilingLawHD256
lake env lean ../witness/lean/CeilingHD256.lean    # prints the axiom audit
```

Column generation is stochastic; re-runs converge to nearby values rather than the identical law.
`witness/law_certified.txt` is the exact artifact our run produced, and its certification is deterministic:
the enclosures and the exact rational p can be re-verified from that file alone.

## Provenance

The verification was conducted as a pre-registered research programme in
[LDGR](https://ldgr.run) (`ldgr-research`), an evidence ledger for bounded, falsifiable experiments.
Every experiment in this report was registered with its pass/fail criteria *before* it ran, and every
artifact was checksummed at creation. (Later experiments in the programme additionally freeze a
cryptographic hash of the registered definition so that post-hoc edits are detectable; the experiments
behind this report predate that feature and are pre-registered without it.) The
findings above correspond to experiments `zeta23-exp1` (build and axioms), `zeta23-exp2` (statement
fidelity), `zeta23-exp3` (the `EnclOK` gap and the independent integer check), and `zeta23-exp7` (the
witness). Ledger records are available on request.

## Disclosure

This verification was carried out with substantial AI assistance (Claude, Anthropic), including the
column-generation search, the certification pipeline, and the drafting of this report. All quantitative
claims are machine-checkable from the artifacts here, and all reproduction commands in this README were
executed. Adversarial review of our own intermediate conclusions is described in `NOTE.md` §6.

Per the [Leiden Declaration on AI and Mathematics](https://leidendeclaration.ai/) (June 2026), we state
this involvement explicitly rather than in a footnote.

## License

Verification artifacts and code: Apache-2.0, matching the licence of the audited repository.

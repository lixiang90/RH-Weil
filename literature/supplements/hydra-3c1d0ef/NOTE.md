# Independent verification of *zeta-23*, and a public witness for its bandwidth-one ceiling

**Technical note.** Bryan Carson, Hydra Dynamix (<bcarson@hydradynamix.com>).
Verification performed 19–21 August 2026 on commodity hardware (Windows x86-64).
Subject: Alpöge–Furman, *More than two thirds of the zeta zeros are simple and on the critical line*,
**arXiv:2608.13637v1**, with formalization at `anthropics/zeta-23-lean`. A v2 (19 August 2026) adds a
provenance appendix, a ξ′ remark, and a family-averaging extension (Remark 7.2, giving 0.811 simple-on-line,
explicitly *not* covered by the Lean formalisation); the main theorems and constants are byte-identical
between versions. This report audits v1.

---

## 1. Scope

The paper proves, unconditionally, that at least ⅔ — and with the Montgomery–Taylor window at least
0.67250… — of the nontrivial zeros of ζ are simple and lie on the critical line, together with a 5/6
distinctness bound and analogues for primitive Dirichlet *L*-functions and for ξ′. The proof was
discovered by an AI system and is verified in Lean 4; the authors verified and communicated it.

At the time of writing the result has no journal referee report and no completed independent verification.
Parts of it have been checked publicly by others: an independent kernel rebuild and axiom audit
(`stevemoraco/qs` PR #363, 13 Aug), an independent reproduction of the ceiling data from the published
enclosures (`teal-sea/zeta-lab` PR #12, 11 Aug, agreeing with our digits), and two open issues raising the
`EnclOK` availability gap (#8, #14). None of those is a statement-level audit, and none constructs an
independent witness. This note supplies both, alongside corroboration of the earlier checks, in three parts:

1. **mechanical verification**: does the formalization build, and do its theorems rest only on standard axioms?
2. **statement fidelity**: do the formal statements mean what the paper claims? (A Lean proof is worthless
   if its statements encode the wrong theorem; this is the part no kernel can check.)
3. **the ceiling certificate**: §7.2's ~0.682 upper bound on the whole method class rests on numerical data.
   Is that data verifiable?

Part 3 produced a data-availability finding, which in turn motivated the construction of an independent
public witness (§5).

## 2. Mechanical verification

Toolchain installed from scratch (elan 4.2.3); the repository pins Lean `4.33.0-rc2` and Mathlib
`51e6992efd06126df61a496bebf8f49482a4e129`, both of which resolved and built without modification.
Total wall-clock ≈ 26 minutes: Mathlib cache (8 681 files), `lake build`, `lake build Solution
Solution.XiPrime`, and the three axiom audits.

Result: **all 34 headline declarations audit clean.** Thirty-two report exactly
`[propext, Classical.choice, Quot.sound]`; `Zeta23.PairCeiling.LawN256_check` reports `[propext]` alone and
`LawN256_edge` reports no axioms at all (both are `decide`-evaluated integer computations, so this is
expected and stronger, not weaker). No `sorryAx` appears anywhere, which is machine confirmation that the
development is sorry-free. The only anomaly in the entire build transcript is one cosmetic
`unused simp argument` warning at `Zeta23/XiPrime/Transfer.lean:718`.

This confirms the repository's own audit claims on independent hardware. Transcript: `audit/build-summary.txt`.

## 3. Statement fidelity

The repository concentrates its human-judgment surface deliberately: `comparator/ChallengeDeps.lean`
holds **15 definitions** built from Mathlib alone, and `comparator/Challenge.lean` holds **17 theorem
statements**; everything else is machine-verified against those. We audited all 32 items against the paper.

**Verdict: faithful, 0 discrepancies.** Full per-item table in `audit/statement-fidelity-audit.md`. Salient points:

- Counting conventions match the paper exactly: half-open windows `T₁ < Im ρ ≤ T₂`, positive ordinates
  (not `|Im ρ|`), open critical strip, multiplicity via Mathlib's `analyticOrderAt`, exact `Re ρ = 1/2`
  for on-line, `zeroMult ρ = 1` for simple, and multiplicity-weighted denominators throughout.
- Mechanical checks: the definitions inlined into `Challenge.lean` are character-identical to
  `ChallengeDeps.lean`; the 17 statements in `Solution.lean` are byte-identical (modulo whitespace) to
  their trusted counterparts, so the axiom audit of §2 transfers to the trusted statements.
- We specifically probed the two places a subtle encoding error could hide. First, the `∑ᶠ`/`ncard`
  conventions return 0 on infinite sets — but finiteness of zeros in a window is provable and proved
  solution-side, and the dangerous direction (an infinite reading trivializing the claim) can only occur
  on the *denominator*, where it is blocked. Second, the Montgomery–Taylor constant: `cMT` evaluates to
  0.7532960679, its reciprocal to 1.3274992963, agreeing with the closed form ½ + 2^(−1/2)cot(2^(−1/2)) to
  better than 10⁻¹⁴, and yielding proportions 0.6725007 and 0.8362504 — the paper's stated 0.67250… and
  0.83625….
- The headline claim of the paper is precisely `montgomery_taylor_simple_on_critical_line_mult`, and its
  ε–T₀ encoding of "liminf ≥ c" is the standard and correct one.

Coverage direction is one-way in the safe sense: every formal statement is a claim the paper makes; a few
claims the paper makes (e.g. some cumulative Montgomery–Taylor variants) are not formalized. Omissions
cannot inflate the result.

## 4. The ceiling certificate: a data-availability gap

Section 7.2 bounds the *entire* bandwidth-one certificate class at ≈ 0.6819 by exhibiting an extremal
256-periodic law with simple-point fraction

    p₀ = 10909258999421303588095230195816054408197 / (16 · 10³⁹) = 0.68182868746…

The Lean theorem `ceiling_law256` takes a hypothesis `EnclOK`: that the true form factor of that law lies
inside the published integer enclosures. **`EnclOK` is not proved in Lean.** The paper says so plainly
(§7.2: the enclosures "are certified by interval arithmetic and are *not* checked by the Lean kernel"), and
so does the source file header of `Zeta23/PairCeiling/LawN256.lean`.

The repository README documents this accurately: it states the enclosures were "obtained outside Lean by
interval arithmetic from an exact-rational certificate … available from the authors", and that "everything
downstream of the enclosures … is checked in the kernel by `decide`". The issue is availability of the certificate,
not disclosure of its status.

The substantive issue is that the law itself — the weights, positions and marks whose form factor `EnclOK`
asserts — lives in `cert_N256_blk_b128m.json`
(sha256 `cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8`), which is **not in the
repository and not in the arXiv source** (25 KB, LaTeX only); the paper states it is available from the
authors. Consequently **no one outside the authors can currently verify `EnclOK`**, and the ~0.682 ceiling
— unlike Theorems A–E — is not publicly reproducible end to end.

**What we could check, we did.** We re-implemented the row-certificate semantics of `RowCert.lean`
independently in Python with exact integer arithmetic (`audit/independent_rowcheck.py`, no dependencies),
parsing the enclosure integers directly from the Lean source. All checks agree with Lean's kernel evaluation:

- all **255** row inequalities pass at *both* endpoints, with margin factor 1.63 against τ = 3 × 10⁻⁴⁰
  (largest implied |256·S(j) − j| = 1.837 × 10⁻⁴⁰);
- both edge-bound checks pass; the implied D(1) lies in [0.823953161, 0.823953161], inside the claimed
  0.82395317;
- the exact rational p₀ matches its published decimal and the paper's rounded bound p₀ ≤ 0.6818287.

One incidental observation supports the enclosures' provenance: 131 of the 255 rows deviate from the
idealised grid value j·2¹³² by exactly one unit in the last place (2⁻¹⁴⁰), with irregular per-row rounding
— the fingerprint of a genuine high-precision interval computation rather than synthetic data.

**We emphasise: Theorems A–E do not depend on any of this.** Our axiom audit (§2) confirms the main
theorems carry no such hypothesis. The gap concerns only the meta-theorem bounding the method class.

## 5. An independent public witness for the ceiling, below p₀ and kernel-verified

The paper's §7.2 bounds the whole bandwidth-one method class by exhibiting a witness law: a
configuration law consistent with the pair-correlation data zeta is known to have, whose simple-point
fraction is only p₀ = 0.681828687463832. No certificate in that class can prove more.

We constructed such a law independently, by column generation over marked configurations on Z/256
with an exact-rational master LP, and certified it with dyadic snapping and interval arithmetic.

**Result.** p = 412129329181963620513241/604462909807282866662336 = 0.681810781927646, which is
**below p₀ by 1.790554 × 10⁻⁵**. A lower witness is a *stronger* obstruction: it shows the method
class is more limited than the published witness alone establishes.

| | published | this work |
|---|---|---|
| witness value p | 0.681828687463832 | **0.681810781927646** |
| band tolerance τ | 3/10⁴⁰ | 1/10⁷ |
| edge bound \|D(1)\| ≤ | 82395317/10⁸ | same constant (measured 0.823950881) |
| downstream error constant | 2.5431315 × 10⁻⁶ | 2.5433268 × 10⁻⁶ |
| certificate public? | no | **yes** |

The τ difference costs 1.95 × 10⁻¹⁰ in the error constant of the paper's Theorem 1′ — four orders of
magnitude below the 1.79 × 10⁻⁵ by which the witness improves, so the improvement is not an artefact
of the looser band. A second certificate at τ = 1/10⁴ gives a slightly deeper 0.681810419964139.

### 5.1 Kernel verification

The paper's `ceiling_law256` is stated for its own law, but is proved through a *generic*
`ceiling_nearCUE`. We therefore emitted our law as a `RowCertData` record and instantiated that generic
theorem on it. The normalisation transfers exactly: the paper's S(j) is our Σ_c w_c F_c(j) divided by
256, so at K = 2⁶⁸ our interval-arithmetic enclosure integers are used *unchanged* — the integers Lean
checks are the ones our certification produced, with no intervening rescaling.

```
LawHD256_check     depends on axioms: [propext]
lawHD256_rows      depends on axioms: [propext, Classical.choice, Quot.sound]
ceiling_lawHD256   depends on axioms: [propext, Classical.choice, Quot.sound]
```

`LawHD256_check` passes by `decide +kernel`, so Lean's kernel independently re-verified all 256 row
enclosures and both edge-bound inequalities as integer arithmetic. The ceiling theorem carries the same
three standard axioms as the paper's, with no `sorry` and no added hypotheses. Files in `witness/lean/`.

Because the paper's certificate file is not distributed (finding 3, §4), its `EnclOK` hypothesis cannot
be discharged by anyone outside the authors. This is, to our knowledge, the first kernel-verified
bandwidth-one ceiling obtained from a certificate that is public.

### 5.2 What this does and does not claim

It is a **ceiling on a method class**, not a lower bound on the proportion of zeros on the critical
line. It does **not** improve the paper's 67.25% result; that would require a better *certificate*,
not a better *witness*. Its content is that the room remaining inside bandwidth-one methods is smaller
than published, and that the bound is now independently checkable.

### 5.3 One constraint that is easy to lose

E[F(256)] is a free direction for lowering p, so a master LP that does not carry the edge bound will
drift above it and produce a law that looks excellent and is inadmissible. This happened to us: a law
at 0.681853248 had to be discarded and re-solved under the constraint, at a cost of 4.6 × 10⁻⁷. The
edge bound is now carried in both the optimisation and the certification masters, and
`witness/verify_law.py` checks it independently of either.

## 6. Adversarial review of our own work

Each numerical component was validated against a brute-force reference before use. This caught two sign
errors during development (an FFT-constructed kernel derivative, and a conjugate-bin placement in a field
computation) that would otherwise have degraded search quality while producing plausible-looking output.

More significantly: this verification is part of a larger programme, and one of that programme's own
intermediate conclusions — a claimed unconditional third-moment separation — was **refuted by an
adversarial review we commissioned against ourselves**, on two independent grounds (the Rudnick–Sarnak
correlation theorem assumes RH; and the test kernel violated its ℓ¹ admissibility condition, so most of the
apparent effect was inadmissible content). We mention this because it calibrates the rest: the findings in
this note are the ones that survived that process, and each is mechanically checkable rather than
argumentative.

## 6a. Provenance

The work was run as a pre-registered programme in [LDGR](https://ldgr.run) (`ldgr-research`): each experiment
was registered with explicit pass/fail criteria before execution, verdicts were recorded against a frozen hash
of the registered definition (so post-hoc reinterpretation is detectable), and artifacts were checksummed on
creation. §2 is experiment `zeta23-exp1`, §3 is `zeta23-exp2`, §4 is `zeta23-exp3`, §5 is `zeta23-exp7`. The
refutation described in §6 was itself a registered adversarial experiment whose `pass` verdict automatically
marked the attacked claim contested.

## 7. Limitations

- We did not run the external `leanprover/comparator` tool itself. Statement equality between the trusted
  and solution modules was established by textual byte-identity plus the kernel-unfolding argument of §3.
  Running the tool would close this small residual.
- We audited the 15 definitions and 17 statements. The ξ′ (6) and PairCeiling (11) comparator statements
  passed the axiom audit but their *fidelity* was outside our registered scope.
- Mathlib's semantics for `riemannZeta`, `DirichletCharacter.LFunction` and `analyticOrderAt` are trusted
  as the declared base.
- Our witness (§5) is *lower* than the paper's by 1.79 × 10⁻⁵, but column generation is a heuristic
  search, so the law is not claimed optimal — only certified. A rigorous lower bound we derived
  separately puts the true optimum of this formulation at or above 0.679278205285913 (exact rational,
  certified by a squared-polynomial positivity argument that requires no solver to be trusted), so
  between 0.6793 and our witness there may still be room we have not reached.
- Our witness is certified at τ = 1/10⁷ rather than the paper's 3/10⁴⁰. This costs 1.95 × 10⁻¹⁰ in the
  error constant of Theorem 1′ — four orders below the improvement — but the two statements are not
  literally identical and the difference should be stated whenever they are compared.
- The paper-side reference used during the fidelity audit was extracted from the PDF, which mangles some
  mathematics; every reconstructed item was resolved against the Lean source or the arXiv LaTeX source
  before use (`audit/paper-reference-extraction.md` carries the ambiguity ledger).

## 8. What we do not claim

We make no new claim about ζ. We do not claim the paper is correct beyond what a kernel and a careful
reading establish: our audit shows the proofs check and the statements say what the paper says, not that
the informal mathematics is free of conceptual error. We do not claim our witness is optimal, nor that the
published ceiling is wrong — our construction is consistent with it and strengthens it, and everything we
found about the published enclosures (§4) indicates a genuine computation. In particular, a *lower*
witness does not contradict the paper: p₀ is an upper bound on what the method class can prove, and any
valid law below it simply tightens that bound.

We also do not claim any improvement to the paper's 67.25% lower bound on the proportion of zeros simple
and on the critical line. That is the opposite-facing result and is untouched by this work: a better
witness constrains the method, a better *certificate* would be needed to prove more zeros.

## References

- L. Alpöge, R. Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637.
- `anthropics/zeta-23-lean` (Apache-2.0), tag v1.0.
- E. Carneiro, V. Chandee, F. Littmann, M. Milinovich, *Hilbert spaces and the pair correlation of zeros*, arXiv:1406.5462.
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24 (1973).
- Leiden Declaration on AI and Mathematics, June 2026.

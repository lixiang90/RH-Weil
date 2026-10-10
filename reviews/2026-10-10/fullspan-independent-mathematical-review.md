# Independent mathematical review of the total-span nine-point certificate

Date: 2026-10-10. Reviewer: independent frontier/proof audit agent, not the certificate author.

**Conclusion: mathematical PASS under the explicitly inherited continuous PC8 admission and all-zero analytic framework.** The new finite implication is an exact rational certificate. This review does not assert a new Lean theorem or official website acceptance.

## Frozen inputs and actual replays

The research certificate is `branch-fullspan-805403-47.json`, raw SHA-256 `9442b3c399e05a4267a5dde3b236959ef941498d12b588947e515192b97fe279`. Its original checker is `check_branch_fullspan_certificate.py`, raw SHA-256 `0d55687f9e4db2f47abee2641f0df2082304b9e9dafcce004b2cabf17f2d5cbd`.

I actually reran that checker, independently checked its complete replacement set and every positive tangent support, and independently reran the public portable checker both offline and with the original source. The corresponding records are `branch-fullspan-exact-check.json`, `fullspan-independent-structure-review.json`, `portable-offline-independent.json`, and `portable-source-independent.json` in this audit directory. The public files reviewed are:

| File | Raw SHA-256 |
| --- | --- |
| `am_ninth_span_certificate.py` | `b03b3259a385702300520bd02f33c79d228b76a0e07c6b42cec23b6a02a5e673` |
| `am-ninth-span-certificate.json` | `9fc7f9d8a00ebbc3e2f8ff236b247af5ac3173c3942ec72b9180c4473a65cf96` |
| `am-ninth-span-point-catalog.json` | `cda8ce5fce3d0a639975f54e57b1991c7d5a2a2cb112df4e3dd13237a954fb27` |

The public certificate changes dependency metadata to canonical LF hashes. Its entire `replacements` payload is exactly equal to that of the frozen research certificate. It must be paired with the public catalog; mixing the newer checker with the older research metadata correctly fails. This is a version mismatch, not a mathematical failure.

## Continuous geometry and guards

The unchanged 241 low cells and their full reflections yield 482 labels. Labels are outer covers: a cell need not consist entirely of low configurations. For any real low frame, choose any covering label. Closed overlaps, threshold boundaries, and reflected direction boundaries are admissible. When two actual adjacent low frames select labels, their six shared gaps force a nonempty compatible domain.

The checker enumerates all 232,324 ordered label pairs, obtaining 4,796 after shared-gap intersection, 2,405 after shared-span intersection, and 2,399 after exact difference closure. Its resulting complete ordered list agrees with the inherited report. No real gap is restricted to a lattice by integer-scaled difference constraints.

The replacement keys are exactly the 47 inherited domains with lower bound below `805403/100000000`. Their total-span intervals are covered by 84 consecutive closed branches. Each branch covers the common endpoint with its neighbors. The endpoints equal the original closure's entire span interval; no small tail is dropped. Each branch recomputes full closure after adding both span constraints. All 84 are nonempty in the frozen certificate.

For direct-region cuts, the point, packed value/derivatives and original PTL list index match the catalog. The original REG convexity interval contains the entire expanded interval `[min(l,p),max(u,p)]`; checking just the query interval or the point alone would not suffice. Old-enabled cuts must match an enabled inherited atom and remain within its previously admitted interval. Packed derivative bounds are correctly decoded. Direct-region reanchoring is valid by convexity even when the original point is outside the query interval. Old-enabled reanchoring instead uses its admitted exact tangent, as detailed below. These conclusions use the real semantics of the source's PTF/PTL, REG and TVal admission, not rounded sample values.

The original raw source was separately downloaded from [the fixed public PC8 source](https://raw.githubusercontent.com/josusanmartin/riemann/d272437e7ebeb17b87c8c3d7cece592aa23785ab/submissions/dani-bound-2026/proof/Solution.lean). Its 1,675,641 bytes have SHA-256 `012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f`, equal to the source pin. The optional-source replay reextracts all 2,196 point entries and the REG table, checks all 541 new direct-region catalog entries and all 237 inherited extra-point entries against this source. I did not recompile the source's analytic admission.

In particular, I independently read the source's `ext_tangent`, `TVal` and `tangent_valZ` (the soundness proof for `tcheckPZ`). Old-enabled validity does not require claiming the entire old interval is convex: its inherited `TVal` provides the exact tangent lower bound `v+w1(p)*(s-p)<=wfun(s)` throughout that admitted interval, together with the true derivative bounds. Both reanchored lines lie below that exact tangent by the same interval comparison. Derivative/zero-order extension beyond REG is therefore used only through that existing `TVal`, never as a newly asserted convexity interval.

## Exact lower bounds and the unbounded domain

The objective is exactly `2*10^8*F9`. It includes the total-span square with coefficient `4*10^8`; common distances share one square variable. Every dual multiplier is nonnegative. For residual `r=q+A^T lambda`, the lower bound uses the lower box endpoint for `r>=0` and the upper endpoint for `r<0`. This is the correct sign for `Ax<=b` and pays every residual without assuming exact stationarity.

All 2,399 domains are actually rechecked, including the 2,352 domains retaining inherited multipliers. The finite minimum is

`263917374155379049835090394947 / 32768000000000000000000000000000`,

which strictly exceeds `805403/100000000`. All 2,955 added tangent rows have positive dual support; 68 uses constrain the total span, at 15 distinct total-span points. The total tangent support uses 573 distinct points. The direct-region subcatalog has 541 points and accounts for 2,553 row uses; the 402 old-enabled uses reuse 97 admitted atom points, of which 32 are outside that subcatalog. These are compatible data counts, not missing entries.

The finite minimum is not the global reward. If either frame has `F8>=805803/10^8`, the other has the inherited unconditional `F8>=805003/10^8`. Nonnegativity of the new square gives the exact outside lower bound `(805803+805003)/(2*10^8)=805403/10^8`. Otherwise both frames are in the complete low cover. Thus the uniform reward on the full unbounded separated domain is exactly the certified value `c=805403/10^8`.

## Transport and counting semantics

The new pair weight has index-span capacity at most two; the gap fees still sum to `B=404350/10^8`. Summing windows therefore gives ordered-pair energy at least `c(m-8)-B*span`. The short-chain case is paid because its right side is nonpositive. The inherited close-pair reward `1/40` exceeds `c`. The local pair total remains below 16, so the old `32*d_epsilon*n` smoothing fee still suffices. The actual all-zero Hermitian operator, off-line conjugate-reflection pairs, repeated zeros and positive-inertia deficit remain the inherited objects.

Consequently the same energy bound `2-C(f)>67216841/10^8` gives

`(2-C(f)-B)/(1-c) >= 66812491/99194597 = 941021/1397107`.

This ratio counts **simple critical-line zeros** in the numerator and **all nontrivial zeros with multiplicity** in the denominator. The improvement over `66812491/99194740` is exactly `134566003/138585665617180`, approximately `0.0000970995105451` percentage points. It may be weakened to a distinct-critical-line count, but those two targets must not be identified in the other direction.

## Public reproduction and remaining scope

The portable checker has no default `tmp` dependency, network request, solver, Lean invocation or output write. Explicit `--source` adds a byte-pinned source extraction check. Default/offline checks bind the old report and its script/dependencies by canonical hashes; match the exact new catalog to every direct-region descriptor; check the 164 catalog points overlapping the old 237-point catalog; and retain all old admitted atom data. Checking all 237 points against the full original source occurs in the optional-source mode, which I actually ran.

A catalog's source-hash string does not independently prove analytic value/derivative/convexity assertions. The theorem therefore correctly discloses the inherited continuous PC8 admission. The public data are a small reproducible mathematical certificate, rather than a claim that its strengthened theorem is already Lean checked. The separate formalization and record website must still process the new implication before those statuses can be asserted.

The accompanying isolated 14-file replay is recorded by `run_portable_clean_independently.py` and its manifest. It deliberately includes no ignored original source and no `tmp` directory. No WSL or Lean work was performed.

Finally, in the currently relaxed high/low storage graph, both directions `H <-> a` have weight `805403/10^8`. Their two-cycle makes every valid potential reward at most this number. A potential certificate alone cannot exceed the new pointwise reward in this graph. Such graph cycles are not certificates of realizable periodic configurations and provide no upper bound on the actual attainable zero proportion.

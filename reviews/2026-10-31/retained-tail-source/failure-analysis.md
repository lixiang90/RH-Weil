# Retained-tail source gate: terminal containment failure, cause not certified

2026-10-31. Limited read-only diagnosis after the one admitted independent replay stopped. No producer, checker, factorial seed, original448 array, individual source coordinate or numerical sign calculation was rerun; no original file was amended. Only this analysis is written. The producer packet, both freezes, checker and terminal stop remain preserved. Same Goal1793085111/C066 spent/latest603; zero mathematics and no source consumption.

## Recorded execution and exact failing predicate

The existing replay-result.json and replay-progress.json both report `STOPPED_NO_RETRY`, elapsed383.65088509999623 seconds, ValueError `INDEPENDENT_CONTAINMENT: h:0:1660`. Bound versions are:

* Producer SHA256 `05f395038a4e2a75027b69996f990e1978d6e09c799dfbd43fd41fa1add8d45b`.
* Checker SHA256 `1d36d353cdeaccb9cfa63529bebb08d6a5f09cdf7e2b280b53f287d64ba54753`.
* Source result SHA256 `a9fb5f5150bc17f56ebc3bd9e981ce0ec421c8efdf5612554ccc3a751eff6de5`.
* Producer/replay-freeze SHAs `833f360a8f1edde9c69a7287fc1f921c1585aa590cc1904ee481b6c4c9013975` / `910c09a29f0b6142f22ae8aa8b1b7e2678b050d731dca0a68ebd0e32f3aa73e6`.

The stage string `sinc-factorial-seeds` is the last progress label, with m2046/summands1049600. The actual exception arose later inside replay_h: the seed construction had returned and the checker was reading h entries. It failed before column0 completed, before the full-h norm/width certificate, before q/band rectangle replay, before all finite V/G entries and before the complement/tail-norm replay. Thus it is not an independent packet PASS with one cosmetic exception. Later arrays are unconsumed.

Existing stored rows, read without recomputation, are:

    [0,1656,"0","1"]
    [0,1658,"0","1"]
    [0,1660,"0","1"]
    [0,1662,"0","1"]
    [0,1664,"-1","1"]

The h denominator is2^640. At the failed index the stored interval is therefore [0,2^-640], with center2^-641. Since i1660 differs from s0, there is no identity/delta diagonal contribution: the checked value is -L^2 times the independently reconstructed sinc row seed, L^2=81/64. There is no native Gram conversion inside this particular scalar containment predicate; that later conversion cannot explain away its failure.

The check requires, in working integer units,

    stored_lo * 2^(3072-640) <= replay_lo <= replay_hi
       <= stored_hi * 2^(3072-640).

Its exception records only the label, not replay_lo/replay_hi. No saved exact checker interval or source working interval is available in the terminal record. Existing bytes therefore do not directly identify the signed excess or prove whether the exact mathematical coefficient lies in the stored interval.

## What near-zero nesting can explain, and what is not proved

The zero lower endpoint and neighboring transition to a two-sided interval are actual evidence that this coordinate lies at a sensitive enclosure boundary. Interval nesting is a stronger demand than both intervals containing the same exact number. For example, J=[0,2^-640] and I=[-2^-3072,2^-3071] can both contain x=2^-3075, while I is not a subset of J. This example is generic; it does not recover the actual stopped checker interval or establish the actual coefficient's sign.

There is also a symbolic smallness check available from the reviewed formulas, without evaluating any coordinate or summing seeds. For i1660, the absolute finite sinc-column coefficient obeys

    |h_i| <= (2048 L^2/p_pi)
       sum_(m even,i<=m<=2046)
         576^m m! / [(m-i+1)!(m+i+2)!]
       < 864 * 576^i/(i+1)^(i+2) * exp(576) <2^-1626.

The first bound uses p_pi>3. For the last inequality, 576/1661<7/20, (7/20)^2<1/8, exp(1)<68/25 and (68/25)^2<8 give powers2^-2490 and2^864, while864/1661^2<1. The checker's closed first-row sum at this index has194 nonzero rational summands. Under its stated exact-ratio arithmetic, each endpoint differs from the exact seed by at most194*2^-3072; final -81/64 scaling adds at most one working unit. Consequently those algorithmic bounds put both final endpoints within2^-1625 of zero, far below2^-640. Conditional on the reviewed factorial identity and the literal arithmetic implementation, the failed inequality is therefore the zero-lower-bound side, rather than the distant upper endpoint.

This deduction is a range bound and predicate analysis, not a regenerated coordinate, an actual interval dump, or a proof that the producer's exact coefficient is nonnegative. In particular, it does **not** distinguish a correct shared-point/non-nested enclosure from an actual sign/source error. Neither stored positivity nor checker failure proves the exact coefficient's sign. No rounding padding, clipping, parity/source amendment, relaxed acceptance or repaired PASS has been made.

## Settlement and possible future certificate responsibility

The frozen success condition was independent containment of every entry, followed by actual global norm checks. That condition failed. The source gate ends as **producer completed; independent certification stopped; full V/G packet not root-consumed**. The time cap did not cause the stop. There is no permitted retry, higher precision, different seed route, cropped row, new rank or automatic signed-head continuation under this budget.

A different future certificate could in principle bound each exact source value's distance to the final stored center and aggregate the native HS error without requiring one independently rounded verification interval to nest inside another. It would need a new explicit admission, complete global source/rounding analysis, actual full-shape checks and independent consumption. Mere interval overlap would still be insufficient. That is an unpaid certificate possibility, not an implementation request or a paid repair of this packet.

The old analytic facilities, operator domains, positivity of R/tiny floor and source representation remain in their previously reviewed scope. The new actual full-H column certificate and outside-head coupling are not established by this failed replay. No conclusion about RH, whole S_ret sign, growing-window/Xi, or impossibility of retained-tail methods follows. Principal/sections/mixed/core responsibilities and the long Goal's completion gates are unchanged.

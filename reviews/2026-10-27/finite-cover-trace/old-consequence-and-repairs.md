# Finite-cover residue gate: strongest-old consequences and repair scope

2026-10-27. Independent scope/old-result audit for the unique action in STATE, not a new mathematical contract. This file edits neither STATE nor cadence. Its geometric input is conditional on the separately audited [orbit-trace transport](orbit-trace-transport.md); existence of this draft is not root consumption.

## 1. Inputs, original domain and the actual relation

The fixed source space is the complex Fréchet space

\[
 F=S_{\exp,\mathbb C},\qquad
 p_{N,k}(r)=\sup_u e^{N|u|}|D^kr(u)|<\infty\quad\text{for every }N,k.
\]

The physical source is \(r=e^{u/2}f\), not the uncentered \(f\). From [405 §§4–5](../../../notes/405-f1-adelic-restriction-moments-and-radical.md), let

\[
 \eta(x)=\pi x^2(\pi x^2-3/2)e^{-\pi x^2},\quad
 h(u)=2\sum_{n\ge1}\eta(ne^u),\quad H(u)=e^{u/2}h(u).
\]

Then \(H>0\), \(H\in F\), and

\[
 p=(D^2-1/4)H\ne0,\qquad
 M_H(t)=\int H(u)e^{tu}du=\xi_{\rm Riemann}(t+1/2)/2>0
 \quad(t\in\mathbb R).                                      \tag{1}
\]

These are paid inputs, also used explicitly in [584 §§3,5](../../../notes/584-marked-cusp-borel-kernel-and-pan-residue-collapse.md). Positivity in (1) comes from the actual positive function \(H\), without RH. Let \(P=C(P_{\rm an,\mathbb C})\subset F\) be the complexified physical analytic relation space of 405, where \(C f=e^{u/2}f\). It contains every \(p_b=\tau_b p=p(\cdot-b)\), and all their finite complex linear combinations. Indeed

\[
 C(\tau_b((D^2+D)h))=e^{b/2}\tau_b p.
\]

Scalar rescaling preserves this relation space. Every fixed translate is an actual noncompact relation, with full Weil pairing zero against every source in \(F\); the complete two pole moments vanish. This does not identify \(P\) with a geometric principal-divisor image.

For every fixed \(b\), all strong seminorms remain finite and
\(p_{N,k}(p_b)\le e^{N|b|}p_{N,k}(p)\). Original full-line \(du\), zero-extension \(D_{\log}\), and \(H_{\log}\) norms are translation invariant. The strong seminorm price is not a uniform original-norm price. No compact cropping is used in this audit. The compact-window relation test alone would be inadequate: [553 §4](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md) already records that the relevant exact compact principal intersection is zero.

## 2. Compact-real reader lemma: already paid, with exact quantifiers

Let \(\mu\) be one fixed finite complex Borel measure of compact support \(K\subset\mathbb R\), independent of \(r\) and \(b\), and define

\[
 R_\mu(r)=\int_K L_r(t)d\mu(t),\qquad
 L_r(t)=\int_{\mathbb R}r(u)e^{tu}du.
\]

All integrals and the following exchanges converge absolutely: compactness of \(K\) supplies one finite exponential weight, and \(H,p\) have all exponential moments. Integration by parts in \(u\), with no boundary terms, gives

\[
 L_{p_b}(t)=e^{bt}(t^2-1/4)M_H(t),\qquad
 R_\mu(p_b)=\int_K e^{bt}q(t)d\mu(t),\quad
 q(t)=(t^2-1/4)M_H(t).                                      \tag{2}
\]

If \(R_\mu(p_b)=0\) for every real \(b\), differentiate under the compactly supported integral at \(b=0\). All polynomial moments of the finite complex measure \(q\mu\) vanish. Polynomials are dense in \(C([A,B])\) for any interval containing \(K\), so \(q\mu=0\). Since \(M_H>0\) on the real line,

\[
 \operatorname{supp}\mu\subset\{-1/2,1/2\}.                 \tag{3}
\]

Conversely, (3) gives (2) equal to zero for every \(b\). Thus this is an equivalence for the actual full translate orbit, not merely a necessary condition inferred from one probe.

Consequences that must be deducted before any novelty claim:

* On the double-pole-zero source subspace \(F_{00}=\{r:L_r(-1/2)=L_r(1/2)=0\}\), every such annihilating reader vanishes.
* If \(\mu\) has an \(L^1\) density, it has no atoms, so (3) forces \(\mu=0\) and the reader is zero on **all** of \(F\), not only \(F_{00}\).
* For support \([0,1728]\), the finite-measure exception is only an atom at \(+1/2\); the \(L^1\) conclusion remains total zero.
* A nonzero \(L^1\) reader therefore fails the actual relation test for at least one real \(b\). This does not supply a universal sign, a numeric counterexample, a common threshold, or the positive \(e^{1728b}/\sqrt b\) asymptotic. The latter required the specific nonzero endpoint coefficient of 584 and must not be transported to arbitrary complex \(\omega\) or masks.

This is exactly the strongest-old lemma already consumed in 584 §5: actual 405 input plus standard compact Laplace uniqueness. It is not a new theorem of the current gate. The global bounded-Hilbert-reader argument of 553 is neither needed nor silently applied to exponential kernels here.

## 3. Fixed finite collections: full Pan image is an old linear-algebra consequence

Suppose a fixed finite collection of readers has been transported to complex \(L^1\) densities \(\nu_1,\ldots,\nu_m\) on one compact real interval. Different compact real supports may first be placed in their finite union. Set

\[
 \mathcal B(r)=(R_{\nu_1}(r),\ldots,R_{\nu_m}(r)),\quad
 V=\mathcal B(F),\quad
 W=\operatorname{span}_{\mathbb C}\{\mathcal B(p_b):b\in\mathbb R\}.
\]

Both \(W\subset V\subset\mathbb C^m\) are algebraic vector subspaces. If \(\ell\in(\mathbb C^m)^*\) annihilates \(W\), the reader \(\ell\mathcal B\) has the \(L^1\) density \(\sum_j\ell_j\nu_j\) and kills every \(p_b\). Section 2 forces this density and reader to be zero, so \(\ell\) annihilates \(V\). The reverse inclusion of annihilators is automatic. Finite-dimensional duality gives

\[
 W=V,\qquad
 \boxed{\mathcal B(P)=\mathcal B(F).}                       \tag{4}
\]

The second equality uses \(\operatorname{span}_{\mathbb C}\{p_b\}\subset P\subset F\). It does not require any closure, boundedness assumption, equality \(P=\operatorname{rad}Q_\zeta\), or source-surjectivity onto \(\mathbb C^m\). In particular, geometric identities such as the total residue sum zero merely make \(V\) a proper subspace; the equality in (4) is relative to the actual image \(V\).

This applies to a fixed finite set of whole-cusp residues and any finite collection of holomorphic differentials/masks, once the actual complex \(L^1\) transport is paid. It is the finite-dimensional annihilator version of the already consumed same-image argument in 584 §4, using the already consumed lemma in 584 §5. It supplies no additional whole-Weil or arithmetic-capacity consequence.

If the coordinates are only finite measures rather than \(L^1\), the conclusion must be weakened: an annihilating linear combination can retain the two pole atoms. One can conclude equality after recording/removing those paid pole directions, or make the corresponding statement on \(F_{00}\); one cannot silently claim all-source equality (4) in that larger class.

## 4. Nonlinear and infinite-output qualifications

For (4), let \(T:V\to Y\) be one source-independent postmap into any set. If

\[
 T(\mathcal B(p'))=y_0\quad\text{for every }p'\in P,
\]

then (4) makes \(T\) constant, equal to \(y_0\), on all of \(V\). Continuity, linearity, and a norm on \(Y\) are unnecessary. The stronger descent requirement
\(T(\mathcal B(r+p'))=T(\mathcal B(r))\) for all \(r,p'\) also implies this conclusion. A fixed bilinear or quadratic construction based only on this finite \(\mathcal B\) cannot obtain a nonzero descended source object by relabeling the same data.

There is a necessary distinction for multiple coordinates: the bare assertion \(T(\mathcal B(p_b))=y_0\) for individual translates does **not** imply that a nonlinear \(T\) vanishes on their linear span. One must test every relation (in particular all finite complex linear combinations), or impose the actual coset-descent property. In 584's rank-one image, complex multiples of one nonzero Pan value already cover the image; the present finite-dimensional proof uses the full relation subspace instead.

For an infinite fixed coordinate family of \(L^1\) readers, every finite projection of \(\mathcal B(P)\) equals the corresponding projection of \(\mathcal B(F)\). Hence \(\mathcal B(P)\) is dense in \(\mathcal B(F)\) in the **product/subspace topology**. A postmap continuous for that particular topology and constant equal to \(y_0\) on all relation images is constant if its target is Hausdorff, or more generally if the singleton \(\{y_0\}\) is closed. Exact image equality in the infinite output, continuity for a stronger target topology, or continuity merely in the source Fréchet topology does not follow. This optional product-topology observation is again standard duality, not a paid strong-topology repair or a new core result.

## 5. Family, limit, source and meromorphic repairs: what is and is not tested

The current conclusion has the following precise scope.

* Varying the level, finite index, cusp count, holomorphic \(\omega\), or fixed complex masks does not help an individual member if its full output is only the finite \(L^1\) residue data and it must descend all \(P\). Every such exact-descending member is zero/constant on its own actual source image. No uniform fee or common level bound was used in this memberwise conclusion.
* A sequence of these already zero scalar readers on a common source domain has only a zero pointwise or distributional limit there. Likewise, a finite-data postmap that exactly descends every relation is already constant before taking a limit. Growing constants alone cannot turn zero values into nonzero ones.
* This does not rule out intermediate approximants that **do not** annihilate \(P\) level by level. Positive \(D'\) approximations to the complete Weil distribution require positivity and the correct full signed limit, not stagewise Pan descent. The preceding exact-member argument cannot be applied to them.
* Nor does this audit pass a limit through \(\mu_n\), through all \(b\), or through the relation test under an unpaid uniformity assumption. In particular, divergent variation/order budgets can lose the finite-measure compact-real representation in the topology actually used on source functions. Fixed-cut labels alone do not justify applying the fixed-reader lemma to the limit.
* Source-adaptive masks \(\lambda_c(r)\) are outside the same-output conclusion only if they actually retain source information beyond this finite \(\mathcal B(r)\). A mask depending only on \(\mathcal B(r)\) is just a nonlinear postmap of that same data and remains covered by §4. A genuinely different source map, an output retaining additional actual data, and stronger/infinite target topologies are not covered by (4); they are not proved successful either. They require an actual formula, domain/range, relation test, same-source visibility, original-norm/strong fees and full signed comparison.
* Arbitrary masks on individual sheets instead of whole cusp-monodromy orbits do not inherit the single-valued trace premise. A non-single-valued expression is not automatically a legal repaired reader.
* Meromorphic \(\omega\) with additional poles is outside the stated holomorphic transport. The added pole locations/orders and residue/contact terms must be retained, with no claim that they automatically escape the old lemma. Real compact finite-order distribution readers have a standard extension of the same obstruction: if \(R(r)=\langle\mu,L_r\rangle\) and (2) holds distributionally, compact Fourier-Laplace uniqueness gives \(q\mu=0\); the real zeros of \(q\) are simple, so only \(\delta_{\pm1/2}\) survive, not their derivatives. This is an old-uniqueness variant, not a construction of a meromorphic repair. Nonreal poles or noncompact spectral support are not addressed by the real-support argument.
* Some noncompact real-measure classes with paid absolute exponential moments can admit analogous uniqueness arguments. This file makes no universal unbounded-support assertion. In the complex plane \(M_H\) can vanish; its positivity on \(\mathbb R\) cannot be transported to complex spectral support or used to assert RH.

Full \(\Gamma\)/contact, all proper powers, both pole degrees, all complex sources and the actual source-to-Weil coupling are not replaced by the finite residue output. No positive-classic-Weil identity or independent primitive/mixed-RR capacity has been obtained.

## 6. Fees retained; stronger-old comparison and counting recommendation

For the transported class \(\nu\in L^1([0,a])\), \(a=1728\), the elementary bound is

\[
 |R_\nu(r)|\le\|\nu\|_1\!\int |r(u)|e^{a u_+}du
 \le \|\nu\|_1\left(\frac1N+\frac1{N-a}\right)p_{N,0}(r)
 \quad(N>a).
\]

For \(\operatorname{supp}r\subset[-L,L]\), a valid original-\(du\) upper fee is
\(\|\nu\|_1\sqrt{2L}e^{aL}\); the same upper fee divided by \(\sqrt{\log2}\) works for the stated zero-extension \(D_{\log}\), since its squared norm is at least \(\log2\|r\|_{du}^2\). These are sufficient fixed-window fees, not exact norms or a necessary universal growth lower bound. For fixed derivative order of the kernel an extra factor \(a^k\) suffices. Different curves/forms/masks have their own actual \(\|\nu\|_1\); no family-uniform bound is inferred.

Strongest-old chain:

\[
 \text{405 actual }H,p_b
 \Longrightarrow \text{584 §5 compact-real uniqueness}
 \Longrightarrow \text{finite-dimensional annihilator identity (4)}.
\]

Once the separately checked whole-orbit trace supplies the actual \(L^1\) class membership, all relation and same-output conclusions above are immediate standard compositions of this chain. The width/trace/single-valuedness checks are important for valid consumption; they do not by themselves supply independent arithmetic input, a new quantitative full-Weil bound, or a nonstandard new comparison principle. Recommended classification is **zero additional mathematical rounds, standard/old transport review**, provided the geometric audit finds no different actual output or genuinely new needed ingredient. Do not introduce C048 or 585 merely for the family quantifier. Root must settle the actual final proof and this recommendation; this draft does not settle cadence.

The strongest classical net consequence remains the previously consumed 542+555→557 whole leading \(4/5\) negative-inertia **upper** budget. Independent nonzero primitive source, integral filtration/section multiplication/mixed RR, all-source growth signed comparison, actual core/coupling and \(\Xi\) remain unpaid. A method-class statement restricted to these fixed finite residue readers is not the long Goal's full substantive completion gate.

## 7. One concrete next admission: the joint oldform tower, not another finite mask

This review can stop automatic level/cusp/mask tuning and prevent a redundant Maass/height construction whose final class depends only on the same finite residue data. It does not furnish a new primitive source-map. In particular, “add relative data,” “make it source-adaptive,” “use a complex pole,” and “take a limit” are scopes left untested, not admitted mathematical inputs.

The root has supplied a different actual joint candidate, so the next comparison need not be an abstract wait for a map. Keep the base form \(g_{11}(q)=\sum_{k\ge1}c_g(k)q^k\), \(c_g(1)=1\), and consider every integer \(d\ge1\) simultaneously:

\[
 \mathcal B_\infty(r)_d
 =\operatorname{CT}_q\big(L_r(j(q))g_{11}(q^d)\big)
 =\sum_{k\ge1}c_g(k)a_{-dk}(r).                            \tag{5}
\]

This is not a search for a level at which a single finite coordinate descends. It is an actual infinite joint map with a topology question that (4) does not settle. Its modular oldform interpretation at level \(11d\) needs the usual degeneracy-map check; in particular the pullback of the differential \(g_{11}(q)dq/q\) has the extra factor \(d\), whereas (5) deliberately reads \(g_{11}(q^d)dq/q\). That factor must not disappear in consumption.

The inexpensive test is specific. For a rapid-geometric sequence \(a_d=a_{-d}(r)\), set
\(Ta_d=\sum_{k\ge1}c_g(k)a_{dk}\). Since \(c_g(1)=1\), the formal Dirichlet inverse \(b*c_g=\delta_1\) exists and suggests

\[
 a_d=\sum_{k\ge1}b(k)(Ta)_{dk}.                            \tag{6}
\]

The next admission should check absolute interchange and continuity in an explicitly fixed sequence topology, not just formal inversion. The existing fixed-radius Cauchy bound on \(c_g(k)\) is exponential. Its Dirichlet inverse can likewise be bounded exponentially by expanding over ordered factorizations: the factor length is at most \(\log_2 k\), the sum of the factors is at most their product \(k\), and the number of terms is at most \(e^{O((\log k)^2)}\). The all-radius supergeometric decay of the actual \(a_{-m}\) from 583 is then the expected sufficient input for (6). This paragraph identifies the test and its paid inputs; it does not claim that the full joint topology/closure has already been root-audited here.

If (6) and the mutual continuity close in the rapid-geometric topology, the joint raw map is simply the already injective 583 raw source data in different coordinates. That is a standard/old-coordinate comparison, recommended zero additional mathematics, not an independent primitive or mixed-RR input. Its Pan quotient may still be nontrivial in a strong topology; finite-prefix surjectivity and product-density alone do not settle that closure. Any claimed different completion must specify its topology and compare with the existing 519/520/553 spectral-quotient assets before admission.

Thus this one actual tower comparison is compatible with stopping C047's finite-reader recipe, and it can prevent a false infinite-output impossibility claim. No C048 or 585 is recommended in advance. Stop if it is only the old coordinate change, with no automatic extra level, mask, norm or paper chain. The final next action remains the root's decision in STATE; this file does not create a second execution authority. Merely adding period labels to finite data is also not an admitted escape: a dessin-spine representation may place those periods in the same compact-real class, but that extra topological transport has not been proved or consumed in this file.

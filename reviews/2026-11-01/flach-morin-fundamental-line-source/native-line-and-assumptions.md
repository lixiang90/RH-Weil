# Native fundamental line: definitions, hypotheses and the two determinant maps

2026-11-01. One frozen source gate, not a mathematical contract or a new theorem. Source: Flach-Morin, Documenta Math. 23 (2018), 1425-1560, [publisher PDF](https://ems.press/content/serial-article-files/26429). Original PDF: 970098 bytes, 136 pages, SHA256 `6bec18d3f87c7c1270df4ddfb11f3009e665b193b8cff169ecb1d0a1f5d07f5a`.

## Scope and locator correction

Read the frozen texts at PDF indices 14,24,25,44,45,50,51,52,55,56 and the first paragraph of 5.8.3 at78. Key definitions, signs and qualifications were checked on page images. The initial B-assumption locator14 is wrong: that page has Remark2.2/Lemma2.3. With ROOT's minimal-locator correction, only the sum-trace endpoint on15 and Conjecture2.5 statement on16 were added. A heading search on12-19 exposed locator lines, not a review of their proofs. Shared-page material from3.3,5.3,5.8.1/.2 and the following5.8.3 proof is exposure, not an additional input. No references, later special-value proofs or other source were opened.

## The actual hypotheses

Let X be a proper, regular, connected arithmetic scheme of dimension d, and n an integer. In 5.2 the standing assumptions are L(barX_et,n), L(barX_et,d-n), AV(barX_et,n). The additional assumption for Proposition5.2 is B(X,n).

- L is finite generation of H^i(barX_et,Z(n)) for i<=2n+1 and vanishing for sufficiently negative i (3.2, printed1449). Both weights n and d-n occur. The source lists dimension<=1 as a known case.
- AV is a compatible torsion product inducing perfect finite-group dualities in degrees i and 2d+1-i, with complementary Tate weights and target Q/Z (3.1). This is arithmetic torsion duality, not positive Hermitian duality. Its stated known cases include smooth number-ring schemes and regular schemes when n<=0 or n>=d.
- B(X,n), Conjecture2.5, is that for every i the pairing
  H_c^i(X,R(n)) x H^(2d-i)(X,R(d-n)) -> H_c^(2d)(X,R(d)) -> R
  is a perfect pairing of finite-dimensional real vector spaces. It does not assert a sign for a same-source Hermitian form.

The trace endpoint here is genuine arithmetic data: the end of Lemma2.3(a), printed1440, describes H_c^(2d) through the regulator cokernel in R^(S_infinity). The unit/product-formula constraint puts the regulator image in the sum-zero subspace, so coordinate summation descends to R. This native compatibility must not be erased; it is also not a constructed map from the project's physical405 relation space.

For X=Spec(O_F), the first paragraph of5.8.3, printed1503, explicitly states that L, B and AV are known for every integer n. Accordingly, their use for Spec Z is **CITED known**, not an unpaid RH hypothesis. This review does not reprove the cited regulator/K-theoretic results or the later special-value calculation. The general conditional theorem cannot be relabelled as conditional on unknown L/B/AV for Spec Z.

## Definition5.1 and direct proof of Proposition5.2

Write W_Z=RΓ_W,c(X,Z(n)), D_Z=RΓ_dR(X/Z)/F^n. Definition5.1 is the invertible integral determinant line

    Delta(X/Z,n) = det_Z W_Z tensor_Z det_Z D_Z.

Section5.1 uses derived de Rham cohomology modulo the Hodge filtration, not an unfiltered complex. D_Z=0 for n<=0. Its cohomology is bounded and finitely generated; the displayed flat base change identifies D_Z tensor R with D_R=RΓ_dR(X_R/R)/Fil^n. The upstream perfection/construction of W_Z is cited from the native Weil-etale construction; its full proof is outside this gate.

For C_R=RΓ_c(X,R(n)), Definition4.1 gives A_R=RΓ_ar,c(X,R-tilde(n))=C_R direct-sum C_R[-1]. Thus H^i(A_R)=H^i(C_R) direct-sum H^(i-1)(C_R). In typed coordinates the theta map is

    (a,b) in H^i(C_R) + H^(i-1)(C_R)  |->  (0,a)
      in H^(i+1)(C_R) + H^i(C_R).

The printed2x2 matrix is compatible with row-vector convention; it must not be transposed into an ill-typed map. Kernel=image at every degree, giving(53). This is exactness of the **theta cochain on cohomology**, not acyclicity of the underlying complex A_R. Its finite determinant supplies the first isomorphism R -> det_R A_R in5.2.

Proposition4.14 supplies the second ingredient:

    D_R[-2] -> A_R -> W_Z tensor R -> D_R[-1].             (64)

Its displayed proof identifies the real archimedean complex with real Betti cohomology, uses the Deligne/de Rham triangle(66), and combines the native splitting(54) with the duality isomorphism B(X,n) in the middle column. The resulting top row is(64). The upstream splitting and motivic/Deligne comparison formalism remain **CITED**, while this direct diagram and determinant implication have been checked.

Because the shift is even, det(D_R[-2])=det D_R, not its inverse. The determinant functor on(64), with its graded tensor reordering, gives

    det_R A_R = det_R W_R tensor_R det_R D_R
              = Delta(X/Z,n) tensor R.

Composing yields the stated canonical real trivialization lambda_infinity:R -> Delta(X/Z,n) tensor R. No numerical equality to a zeta function is a premise or conclusion of Proposition5.2 itself.

## Canonical determinant versus canonical geometric object

Printed1469 distinguishes two levels. A compact-support Weil-etale cone may be compared by a nonunique quasi-isomorphism, yet its determinant comparison is independent of that choice. In contrast, the integral Weil-Arakelov objects defined by mapping fibres/cones in4.2/4.4 are only specified up to noncanonical isomorphism there. The direct-sum real complex and canonical determinant trivialization do not upgrade those integral objects to a canonical positive geometry.

Native facility: an integral global arithmetic determinant line and its real trivialization, conditional in the stated generality and applicable to number rings with cited known premises. No positive Hilbert norm or positive physical-source pairing is supplied by these determinant assertions. They neither identify a continuous source r with a class nor recover the complete mixed Weil distribution. A later bridge would need its own source map, domain/norm, principal compatibility, nonzero coverage and full Gamma/proper-power/pole comparison. The lack of that bridge here is not a proof of impossibility.

Disposition for ROOT: native scoped definitions/direct determinant proof PASS with the stated cited dependencies; no new classical positivity input established by this reading. No new mathematical round,607,C071 or successor is assigned by this file.

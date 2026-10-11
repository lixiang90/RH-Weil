# 521–523 final mathematical review

Date: 2026-10-11. Reviewer: mixed_kernel_analysis. Baseline: b9651f2375a89b905191225e7dd710075a05be96.

Authorship and independence: I constructed the moving-source argument and wrote public note 521 under the parent agent's explicit authorization. Its review below is an author self-check, not an independent review of my own authorship. I read the complete final texts of 522 and 523 and independently checked their derivations. The parent has separately reported that root and prime_transfer_chain fully checked 521 without blocking errors. No public notes 522–523 or Git state were edited by me.

All final hashes below refer to the frozen public texts, including the final paragraph of 521 linking the completed 522 and specifying the growth exponent infimum.

## 1. Result, scope, and source of the arithmetic assumption

521 author self-check: PASS.
522 independent review: PASS.
523 independent review: PASS.

No blocking mathematical error was found in the final three manuscripts. The exact theorem is a functional-analytic comparison in the specified actual source quotient:
\[
 \inf\{\gamma\ge0:\ \forall n\ \exists m,C\
 \bar P_n(V_a x)\le Ce^{\gamma|a|}\bar P_m(x)\ \forall a,x\}
 =\sup_\rho|\Re\rho-\tfrac12|.
\]
Only an infimum is asserted. A bound at the endpoint itself is not proved and may fail in a genuine boundary Jordan block.

The equivalence of the full-jet subexponential growth contract with RH is now proved inside this model. The upper-bound direction uses a right zero-free region determined by the actual unknown zero width. It does not establish a new arithmetic zero-free region, compute that width, or independently prove the RH-sized growth bound. The naturally unitary single-line Hilbert completion has a zero source quotient, so it cannot provide a faithful implementation of the nonzero Fréchet quotient.

## 2. 521: author self-check by section

### Section 1: original quotient and simultaneous representative

The closed actual source identity \(I_\mathbb C=\mathcal R_{\rm jet,\mathbb C}\) is precisely the one proved in 518–519, with no added target degree constraints.

The finite maximum of original seminorms is formed before the quotient infimum. This is necessary: separately choosing minimizers for its components would not supply a common representative. The directed quotient seminorms generate the actual quotient Fréchet topology.

The function \(Z(s)=(s-1)\zeta(s)\) is entire. Its value at 1 is 1, and it is zero-free in the right region \(\Re s>b=\sup_\rho\Re\rho\). Trivial zeros are on the negative real axis, and do not enter the right region. The requirement \(d_0>b\) is explicit arithmetic input; it is not claimed that b=1/2 is known.

### Section 2: actual source and normalization

For a normalized compact smooth \(\psi\) supported in (1,2),
\[
 \theta_\lambda=(r\partial_r+1)(r^{-\lambda}\psi)
\]
has a smooth even extension, vanishes at zero, and has zero real-line integral because its positive-half-line integral is the boundary term
\(\int\partial_r(r^{1-\lambda}\psi)\,dr=0\).
These are both of the original source conditions. Complex parameters require the complexified source, which the note explicitly uses.

Mellin integration by parts gives
\[
 M_+\theta_\lambda(s)=(1-s)J_\psi(s-\lambda),\quad
 M_{E\theta_\lambda}(s)=-2Z(s)J_\psi(s-\lambda),
 \quad J_\psi(0)=1.
\]
The target identity initially holds by absolute summation on Re s>1; both sides are entire and then agree everywhere. The precise calibration is
\[
 M_{h_\lambda}(\lambda)=-2Z(\lambda).
\]
The removable value at λ=1 is −2. There is no reciprocal Gamma factor. Because the source is actual and admissible, hλ is in I; equivalently, its Mellin transform preserves the full orders at all nontrivial zeros.

### Section 3: all-height Harnack bound

A chain of disks with radius 2r and step at most r stays entirely in Re s>b. The chain length is bounded independently of the height T. On that fixed positive-real-part strip, the N=1 Euler–Maclaurin identity gives
\[
 Z(s)=s-s(s-1)\int_1^\infty
              (x-\lfloor x\rfloor)x^{-s-1}\,dx,
\]
so its absolute upper bound is \(C(1+|T|)^2\), including at s=1 by continuation.

At the fixed Euler anchor σ*>1,
\[
 |Z(\sigma_*+iT)|\ge(\sigma_*-1)/\zeta(\sigma_*)>0.
\]
For \(u=\log M_T-\log|Z|\), the Poisson kernel on each disk gives a Harnack ratio at most
\((2r+r)/(2r-r)=3\). After J steps,
\[
 |Z(\sigma+iT)|\ge M_T^{1-3^J}c_0^{3^J}.
\]
Therefore 1/Z has a fixed polynomial bound uniformly for every T. The estimate is crude but sufficient. It does not depend on zero spacing, zero multiplicity bounds, or a selected sequence of good heights. Constants may deteriorate as the real-part line approaches b, so no boundary estimate is asserted.

Primary formulas were checked against
[NIST DLMF 25.2.8](https://dlmf.nist.gov/25.2#E8) and
[NIST DLMF 25.4.3](https://dlmf.nist.gov/25.4#E3).
The Harnack step itself is derived from the disk Poisson kernel.

### Section 4: finite target cost of the moving source

Every source derivative costs a finite polynomial in λ on its fixed support. For positive target t the actual E series has finitely many terms and vanishes for t>log2.

For negative target t, both source constraints give
\[
 h_\lambda(t)=2r^{-1}\sum_{m\ge1}\widehat\theta_\lambda(m/r),
 \qquad r=e^t\le1.
\]
Applying j target derivatives gives
\(r^{-1}(-1-y\partial_y)^j\widehat\theta_\lambda(y)\).
With K=n+2, Fourier integration by parts on the terms
\(y^\ell\widehat\theta_\lambda^{(\ell)}(y)\) requires ordinary source derivatives only through K+j. Their parameter cost is at most \((1+|T|)^{K+j+1}\). Summing y^(-K) yields r^(K−1), which pays the largest target weight r^(-n). Thus
\[
 P_n(h_\lambda)\le C_n(1+|T|)^{2n+3}.
\]
No height-dependent seminorm index is hidden.

### Section 5: actual inverse, sign, and uniform decay

The moment-corrected function
\[
 v_\lambda(f)=f-\frac{M_f(\lambda)}{-2Z(\lambda)}h_\lambda
\]
has zero λ moment. The original actual integral operator satisfies
\((D+\lambda)R_\lambda v=v\). Since B=−D−1/2 and z=λ−1/2,
\[
 (z-B)^{-1}[f]=[R_\lambda v_\lambda(f)].
\]
The sign is positive Rλ; the negative Tλ in 520 is the inverse of A−λ, a different signed operator. Preservation of I and two-sidedness follow from the full-jet unit argument. No simple-zero assumption enters.

D commutes with Rλ on the zero-moment subspace. The same moment vanishes for Dv. Hence
\[
 R_\lambda v=v/\lambda-R_\lambda Dv/\lambda.
\]
Choose fixed k>n+S. Tail estimates control each Rλ term by Pk without any imaginary-height factor, after commuting D. Mellin integration by parts with any fixed sufficiently large order q gives decay of Mf(λ), which absorbs the polynomial 1/Z cost and the P(k+1) moving-source cost. For instance \(q\ge L+2k+5\) suffices.

This proves one fixed m,C with
\[
 \bar P_n((z-B)^{-1}x)
 \le C(1+|\Im z|)^{-1}\bar P_m(x)
\]
on the whole fixed right strip. The original-space inequality is proved first, and the quotient infimum is then taken with one representative. Reλ>d0>1/2 ensures the stated uniform bound for 1/|λ| even at small heights.

The X-valued resolvent family is holomorphic: the source and scalar denominator are holomorphic, and the tail integrals and their parameter derivatives are uniformly controlled on parameter compact sets by finite larger exponential weights.

### Section 6: final scope

The last paragraph accurately links the completed 522 bridge and specifies the growth exponent infimum. It makes no new zero-free-region claim and does not treat b=1/2 as unconditional.

## 3. 522: independent review by section

### Section 1: actual Banach completions

The seminorm presentation in 522 is exactly the one in 521: taking the maximum over N≤n merely returns N=n, because the exponential weights are monotone.

The coarse translation bound descends to the quotient before completion and preserves each seminorm kernel. It extends the actual group to a Banach C0 group on En. Strong continuity follows from continuity on the dense actual quotient image and a uniform bound on compact time intervals.

The maps from X into En need not be injective. The proof explicitly permits this. The Banach generator agrees with B on the smooth actual quotient image, including all its powers. No abstract Fréchet spectrum is used to manufacture a group.

### Section 2: correct resolvent comparison scope

The unknown width β is defined from the true zeros. Functional-equation symmetry gives the right edge 1/2+β. The 521 estimate gives one fixed input seminorm for the complete strip, not one per zero or height.

The actual resolvent equals the Banach generator resolvent on the legitimate initial half-plane Re z>n+1/2: the actual inverse lands in the generator domain and solves its equation, and uniqueness of the Banach resolvent proves equality. The proof explicitly does not claim that the shifted contour is in the Banach resolvent set of all of En. This distinction is crucial and is handled correctly.

### Section 3: genuine inversion and exact second-order regularization

The exact identity is
\[
 (z-B)^{-1}x=x/z+Bx/z^2+z^{-2}(z-B)^{-1}B^2x.
\]
There is no sign error or missing scalar factor.

Two actual time integrations give
\[
 V_ax-x-aBx=\int_0^a(a-u)V_uB^2x\,du.
\]
For a large enough initial real part c, exponential damping gives an L1 Banach-valued function, extended continuously by zero to the negative time half-line. Its Fourier transform is exactly the regularized resolvent divided by (c+iT)^2.

On this initial line, the genuine Banach group resolvent has its usual uniform bound \(1/(c-n-1/2)\). The transform is thus L1 in T. The manuscript gives a sufficient Gaussian approximate-identity derivation of Banach Fourier inversion. It does not assume an unproved general Fréchet Bromwich theorem or one initial line valid for every seminorm simultaneously.

### Section 4: legitimate contour move and both time directions

The contour integrand is Banach-valued holomorphic in the fixed strip, by the actual X resolvent followed by the continuous map into En. The 521 bound makes horizontal sides O(|T|^(-3)) and both vertical sides absolutely integrable. The regularization pole at 0 remains strictly to the left because the target real part is greater than β≥0. No actual zero or pole is crossed.

The output estimate pays B² by two additional derivatives, and x+aBx by a further finite seminorm and the same positive exponential. A single larger index controls everything. The index and constant never depend on a or zero height.

The actual sharp involution satisfies
\(\sharp V_a=V_{-a}\sharp\) and loses only one exponent index plus finite derivative constants. Applying the positive-time result twice with this involution supplies the same exponent for negative time. No left-side contour near trivial zeros is required, and no Jordan block is removed.

### Section 5: exact infimum and conditional RH equivalence

Every exponent strictly greater than β is admissible. For the reverse inequality, each true zero has a nonzero actual eigenclass from 520. Hausdorffness guarantees a seminorm detecting it. Considering positive and negative times forces any admissible exponent to dominate its real displacement; the supremum gives β.

The endpoint is expressly not asserted to be admissible. A true Jordan chain at an extremal zero can cause polynomial growth at the endpoint, consistent with every strictly larger exponent.

The subexponential contract is equivalent to β=0, hence to RH. The upper direction is conditional on the zero-free half-plane corresponding to RH; this is not an independent RH proof. Simple zeros are not assumed or implied.

### Section 6: source-correction quantifiers and limits

The actual-source version has the correct order of quantifiers:
n,ε fixed first, then m,C fixed, then all a,f, and finally a permissible source θ depending on a,f.

A quotient infimum need only be approximated, not attained. For a nonzero raw representative f, Pm(f)>0, so one can absorb a sufficiently close source approximation by enlarging the constant. For f=0 choose θ=0. In the reverse direction apply the source statement to f−Eψ, use invariance of I under the group, then take the infimum over ψ. This does not assume a continuous linear section or an optimizing source, and correctly handles nonzero seminorm kernels.

## 4. 523: independent review by section

### Section 1: unchanged actual source

The model is the same full-jet quotient, and the chosen actual h0 belongs to I. Its entire Mellin transform is nonzero as a function, although it vanishes at the actual zeros. Translation invariance of I is already paid.

### Section 2: single-line weighted Hilbert density

The weight-removal map Uσ is unitary and the original F embeds densely because it contains compact smooth functions. The identity
\(U_\sigma\tau_a h_0=e^{\sigma a}\tau_a(U_\sigma h_0)\)
shows that all ordinary translates are in the weighted image of I up to a nonzero scalar.

For a vector orthogonal to all those translates, Plancherel gives the L1 product
\[
 \widehat v(T)\overline{H_0(\sigma-iT)}.
\]
The sign σ−iT is correct. Fourier uniqueness makes that product zero almost everywhere. H0 is a nonzero entire function, so its fixed-line zeros are discrete and have zero measure. Therefore v=0 and I is dense in every single-line weighted Hilbert completion.

This argument is unconditional and does not assume all zeros are simple.

### Section 3: precise single-line Sobolev extension

The fixed-order derivative norm after Uσ has Fourier weight
\(w_k(T)=\sum_{j=0}^kT^{2j}\).
Weighted Cauchy–Schwarz makes
\(w_k\widehat v\,\overline{H_0(\sigma-iT)}\)
integrable, so the same proof works. The actual weighted source is Schwartz and belongs to every such finite-order Sobolev space.

The conclusion is appropriately limited to the same single real-part line and these translation-invariant derivative weights. It is not expanded to physical-coordinate polynomial weights or multiple exponential weights.

### Section 4: correct natural-unitarity obstruction

The exact norm factor is
\(\|V_af\|_{H_\sigma}=e^{(\sigma-1/2)a}\|f\|_{H_\sigma}\).
Hence the center line is naturally unitary, but its completed source quotient is zero by density. It cannot faithfully realize the nonzero original quotient. Source-space unitarity also does not imply cokernel unitarity.

The separate full-jet Jordan obstruction from 520 is correctly distinguished from this completion collapse.

### Section 5: Mellin evaluation and the scope boundary

The Mellin functional is nonzero and continuous in the original F, vanishes on I, and cannot continuously extend to Hσ because I is dense there.

The Riesz-kernel check gives
\(e^{(\overline\rho-\sigma)t}\), whose squared norm diverges for every σ. Polynomial factors for higher jets do not repair this. This independently verifies the failure of single-line L2 continuity.

The double-ended counterexample is essential and correct. If N>|Reρ|, then
\[
 \int_\mathbb R
 \frac{e^{2\Re\rho\,t}}{e^{2Nt}+e^{-2Nt}}\,dt<\infty.
\]
It gives a nonzero continuous Mellin functional killing I, so I is not dense in that two-ended Hilbert space. Thus no conclusion of collapse is claimed for arbitrary intersections or combinations of exponential weights.

### Section 6: remaining arithmetic cost

Single-line approximation supplies no uniform estimate in all the output exponential weights and derivatives. The remaining contract requires fixed finite m,C controlling all times and all inputs. The completed 521–522 comparison does not independently shrink the zero width. This limitation is accurately stated.

## 5. Finite diagnostics and their limits

Under separate authorization I wrote and ran:

- scripts/centered_growth_source_diagnostics.py
- reviews/2026-10-11/f1-centered-growth-diagnostics.json

At 50 decimal digits, the run completed in approximately 8.6 seconds with 123/123 PASS: 68 exact finite rational-algebra checks and 55 ordinary non-interval floating checks. Failure saves the result and exits nonzero.

Finite coverage includes actual compact smooth sources and their source integral/Mellin calibration including λ=1, a finite E log integral and explicit Dirichlet tail, actual Gaussian forcing for the one-sided Rλ integrals with endpoint corrections, D commutation and the 1/λ identity, hypothetical finite Jordan group/resolvent algebra, two finite Bromwich cutoffs with explicit finite-model tail formulas, and the exact Poisson ratio 3.

The finite Jordan blocks do not assert multiple zeta zeros. Source grid samples do not bound a continuous supremum or prove all-height estimates. Floating quadrature and tail comparisons are not interval certificates or Lean proofs. The infinite quotient, density, resolvent and growth assertions require the manuscript proofs. The parent subsequently reported prime_transfer_chain's independent rerun: 123/123 PASS and the independently saved JSON exactly matches the public JSON. The parent also reported that a fresh separate reviewer passed the complete three-note text. These are additional execution/review records, not interval or Lean certification.

## 6. Final LF-normalized hashes

UTF-8 content, CRLF/CR normalized to LF before SHA256:

| File | LF SHA256 |
|---|---|
| notes/521-f1-moving-source-correction-and-uniform-resolvent.md | 2950f12602d08086fb642396e2f287b33671b7a098da63233bc7c7dffcd71f95 |
| notes/522-f1-optimal-centered-growth-and-rh-equivalence.md | a36b872c7bb68fa6f5f46aa1768cdbade09579393ba3ec6195134e0a1a2d0dd3 |
| notes/523-f1-natural-hilbert-collapse-and-growth-gap.md | 33a42f3f8f06f1478a862aeb1766b2b5ff333e6fd1d36241d19d038168405145 |
| scripts/centered_growth_source_diagnostics.py | 26b1023cd7165029f77602f2932435f03e61b0a331d0037608b99785bad14b95 |
| reviews/2026-10-11/f1-centered-growth-diagnostics.json | a3389710ea4ead70adac93341dcd9f448a42eccbe9666573a5748083dbc85572 |

No new RH proof, zero-free region, zero proportion, simplicity theorem, faithful Hilbert realization, Weil sign, global HH bridge, or world-priority claim is certified by this review.

提交前仅删除521及诊断脚本末尾的多余空白行；数学正文与计算逻辑未改。
上表为此换行整理后的LF哈希，有限诊断已按最终文件重新执行。

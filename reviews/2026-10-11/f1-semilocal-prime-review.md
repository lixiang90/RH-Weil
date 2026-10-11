# Final independent source/sign/domain review of 511–512

2026-10-11. Reviewer: semilocal_gamma_prime. This report changes no public file.

## Coverage and source identity

Reread the complete FINAL public notes 511 and 512, all six / six numbered sections,
with note510's proof already fully read in the earlier task. Also independently
read 404–405 and Connes math/9811068v1 PDF29–31 and PDF72–73 in the original
extraction. This review specifically checks dense-source Mellin calculations,
the finite-place signs and Haar constants, trace-class reuse, exact output
scope, quarter-Gamma constants, degree-zero moments, Parseval, and the broad
test limit. The final reread additionally covers all of the new 512 §5:
the source-defined isometric embedding, full-space inversion/projection
intertwining, the radial common-Fourier mismatch, its noncompactness, exact
operator norm, and the trace-class-correction obstruction. It does not reprove
every analytic statement of Connes Theorem4.

FINAL public-source SHA256:

    511: d0a9607e27402967f488c2536093ff6ea6d7a0efb7df57064df6131b41420f6f
    512: fd07fadfbe4ab84d5c2097ed890fefe1a91924e5d370a7f1ad198a374560a747

These hashes identify the complete final reread after all requested patches.
No numerical result is used as proof.

## Final verdict and closed corrections

All mathematical conclusions in the final 511–512, including new 512 §5,
PASS independent review. There are no outstanding mathematical corrections.
The source strip clarification was made exactly where needed: although
(511)(10) holds for Re s>0, the ordinary Schwartz cosine-Mellin functional
equation immediately after it now explicitly uses 0<Re s<1. The later use
s=1/2-i tau is inside that strip. The originally requested correction was:

    Replace "510的实际偶Mellin计算给"
    by "在 0<Re s<1 上，510的实际偶Mellin计算给".

This displayed-domain clarification is now present, with no change to the
theorem. The historical-intent wording "原文将相容常数吸入内积" was also replaced
by the neutral statement that, with the present explicit measure convention,
the inner-product expansion retains rho^(-1). The normalization calculation
itself remains correct. The generating algebra in final 511 §4 now explicitly
lists 1, F_S, I_S, P_0 and Pi, so the closure does not rest on an implicit
generator description.

No false all-tests assertion for S={infinity,2,5}, no partial-Fourier descent,
no unjustified infinite Euler product, and no RH implication were found.

## 1. Actual dense source and normalization

The fundamental-domain representative is unique: finite valuations force the
two S-unit exponents; the real sign forces the remaining +/-1. Lifting a
compactly supported smooth C_S function to the positive-real, unit-finite
domain and extending by zero is an actual Schwartz source. Its periodization
on the domain has only q=1. Hence the completion maps onto the weighted
L^2(C_S), not merely into it.

On the fundamental domain the standard self-dual additive measure has density
rho_S=(1-1/2)(1-1/5)=2/5 relative to |c|d*c. Expanding the norm and unfolding
therefore gives rho_S^(-1) times the additive sum of inner products. Fourier
permutes q and q^(-1) and has |q|_S=1; it preserves the same norm, regardless
of this fixed constant. Nothing is inferred from a hypothetical zero moment
condition absent from the original finite-S definition.

Source inversion on compact tests away from every zero coordinate extends by
zero to a Schwartz test and interchanges periodization exactly. On the
completion it is unitary by changing c to c^(-1) in the multiplicative Haar
integral. It is enough to prove this on the stated dense source; the public
note correctly declines to claim that every Schwartz source is preserved.

The radial source tensor

    F_phi=phi(real) 1_Z2 1_Z5

has actual periodization 2 sum_(m,n>=0)phi(2^m5^n r). Its weighted logarithmic
form is the bounded invertible geometric-shift operator (511)(9) applied to
v_phi. Every compact smooth logarithmic test corresponds to an even Schwartz
phi supported away from zero. This proves density in the radial block.

Absolute Mellin Fubini for Re s=sigma>0 is paid by

    integral |phi(t)|t^(sigma-1)dt
       /[(1-2^(-sigma))(1-5^(-sigma))].

The same bound applies to F_infinity phi. On the critical axis both Mellin
integrals in the real functional equation lie in the valid strip. The ratio
of the actual two geometric denominators is exactly

    product_p (1-p^(-(1-s)))/(1-p^(-s)).

For s=1/2-i tau this yields the numerator exp(-i tau log p) and denominator
exp(+i tau log p) in (511)(11). The source factor 2 and unitary Fourier
normalization cancel, so neither an extra real-sign factor nor an extra
log p phase constant occurs.

## 2. Finite-place derivative, trace-class reuse and the compact block

With a=p^(-1/2), L=log p,

    m_p'/m_p=i 2L sum_(n>=1)a^n cos(n tau L).

This independently confirms b_p negative in (511)(15), because m'/m=-ib.
Differentiating any finite number of times is legitimate uniformly since
sum n^j a^n<infinity. The complete phase consequently obeys the first three
polylog bounds used by 510. Its near-diagonal difference quotient and its
right-variable first two derivatives satisfy the same estimates; its
off-diagonal 1/(xi-zeta) tail is square-integrable in xi. Multiplying on the
right by the oscillator therefore makes a Hilbert–Schmidt kernel, and the
inverse right oscillator is Hilbert–Schmidt. This proves S1, not just S2.
The strong-compression proof of the diagonal trace also carries over.

The compact-unit average in U(h_S) projects to exactly one K_S character,
the trivial character. The Fourier–inversion product commutes with all unit
actions; Pi also does. Thus the boundary is the proved radial S1 operator
and zero on the infinite orthogonal block, without infinite multiplicity.

Pairing with the Schwartz transform gives

    -(1/2pi) integral b_p(tau) varphi(tau)dt
      =2 log p sum_(n>=1)p^(-n/2)eta(n log p)
      =2 log p sum_(n>=1)h(n log p).

The finite prime-power time sum is actually finite. The only identity
constant comes from the already fixed real phase; the conductor-zero
finite-unit constant is zero. Consequently Omega_S/2=N_S, including h(0).
The full N comparison requires missing prime-power values to vanish. The
support coverage condition given in 511 is sufficient and properly quantified.

## 3. Gamma and Parseval constants in 512

The exact quarter-psi value follows by combining

    psi(3/4)-psi(1/4)=pi,
    psi(1/4)+psi(3/4)=2psi(1/2)-2log2,
    psi(1/2)=-gamma-2log2.

It is psi(1/4)=-gamma-pi/2-3log2. Each finite phase contributes
2log p a/(1-a) at tau=0. Thus a_S(0)>0, with the signs and constants shown
in (512)(2).

For f_R=exp(-t/2)(d^2-1/4)chi(t/R), compact support removes all boundary
terms in weighted integration by parts. The exact Mellin prefactor is
((s-1/2)^2-1/4)=s(s-1), so both degree moments vanish for EVERY R. This
does not rest on cancellation in a numerical integral.

The Fourier convention in 512 is nonunitary, so

    integral |hat chi(v)|^2dv = 2pi ||chi||_2^2.

The transform of F_R has the coefficient
-(tau^2+1/4)R hat chi(R tau). Squaring, changing v=R tau in the charge,
and taking its limit produce

    Omega_S/R -> a_S(0)/(32pi) integral |hat chi|^2
              = a_S(0)||chi||_2^2/16,
    N_S/R     -> a_S(0)||chi||_2^2/32.

Both constants in (512)(7) are correct. The dominating polynomial/log weight
is integrable against the Schwartz square and is uniform in R>=1 for FIXED
S. It is not uniform in growing S. The public note correctly emphasizes that
f_R's support expands and the omitted prime sum has no paid sign. It therefore
does not incorrectly turn the positive fixed-S limit into a counterexample
to full Weil negativity or RH.

## 4. A strict next-cycle obstruction from the natural unramified embedding

Let ell be a prime outside S_f and S'=S union {ell}. Consider the actual
source map

    j_src(F)=F tensor 1_(Z_ell^*).

For a representative (r,kappa_S,kappa_ell) in the S' fundamental domain,
the new S-unit ell^k satisfies 1_(Z_ell^*)(ell^k kappa_ell)=0 unless k=0.
The remaining sum is exactly the original periodization E_SF. Consequently
j_src passes to an isometric completion map:

    j: H_S -> H_S',    (j psi)(r,kappa_S,kappa_ell)=psi(r,kappa_S).

This uses compact new-unit Haar mass 1, so no additive rho ratio multiplies
the Hilbert map. On the radial weighted logarithmic representation j is
literally the identity. This is true at the source level; it is not imposed
by identifying abstract L^2 spaces.

The independently proved common Fourier formulas then give

    F_S' j - j F_S
      = M_((m_ell-1)m_S) J_tau

on this radial source block. Partial local Fourier descent is not assumed.
For ell fixed this operator is NONCOMPACT: |m_ell-1| is bounded below by a
positive number on some real interval, and the non-atomic interval contains
infinitely many disjoint positive-measure subsets. Normalized indicators on
those sets form an orthonormal sequence whose images under the multiplier
remain orthogonal and have uniformly positive norms. Composing with the
unitary J_tau and m_S does not change compactness.

In particular the mismatch is not in S1, so this particular natural j does
not identify the old and new Fourier operators even modulo the relative
trace-class ideal. It still preserves the actual dilation, inversion, radial
projection and compact-unit-trivial inclusion. The unpaid piece is Fourier.

For clarity the norm is also exactly computable:

    |m_ell(tau)-1|
      =2a |sin theta|/sqrt(1+a^2-2a cos theta),
    a=ell^(-1/2), theta=tau log ell.

The square ratio attains its maximum 1 when cos theta=a, hence

    ||F_S'j-jF_S||_(radial)=2/sqrt(ell).

This tends to zero as the newly added prime tends to infinity, but for each
fixed ell it is still noncompact. Thus the obstruction is a precise failure
of the most natural source map's Fourier compatibility, not a proof that no
corrected maps, larger ideals, or other globalization mechanisms can work.

## 5. Final public §5 comparison and rectangular trace-class correction

Final 512 §5's displayed m_ell-1 numerator is +2ia sin(theta), consistent with
the exact source gamma direction. Its norm proof is exact because

    (1+a^2-2az) - (1-z^2) = (z-a)^2,

and z=a is achieved on a positive-measure neighborhood up to arbitrary
precision; the essential supremum is the displayed value 2a.

The new-variable constancy also proves full-space, not only radial,
I_S'j=jI_S and Pi_S'j=jPi_S. New tight Haar probability is what makes j
an isometry; no standard additive Haar coefficient is silently added.
The noncompactness claim uses an actual non-atomic spectral interval and
therefore is stronger than merely "a nonzero operator" or infinite rank.

If K:H_S -> H_S' is trace class, its Fourier compatibility correction is

    F_S' K - K F_S,

which is trace class because the two Fourier operators are bounded. It
cannot cancel the already proved noncompact mismatch of j. This verifies
the exact public claim that adding a trace-class correction to THIS j
does not make the common Fourier operators intertwine. The argument does
not preclude a different source intertwiner, a larger proven relative
ideal, or a weighted boundary transfer. The public note preserves those
limits and correctly records the additional ordinary charge
2log ell sum h(nlog ell) as the next transfer cost.

Final mathematical audit status: PASS, including all of new 512 §5.

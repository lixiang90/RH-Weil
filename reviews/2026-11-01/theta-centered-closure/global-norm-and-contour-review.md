# Independent direct norm check: centered incomplete Eisenstein map

2026-11-01; /root/theta_centered_norm, exclusive output. **PASS for the actual global norm and contour claim, with the domain/role restrictions below.** This is a bounded strongest-old recovery, not ROOT settlement, a new mathematical contract, C072/607 or a classical RH consequence. I recovered README/STATE/check/show, the active Goal, stopped C071, latest AA decision and frontier before reading the exact current formation and old evidence. The parent's actual runtime1793085111 observation is not replaced by a child-local Goal claim. No web, PDF body, reference proof, scientific code, numerical run or authority edit was used.

I read formation-and-single-test.md, the complete prior ROOT direct calculation8716/a41d15e1abf7df6eb446d7246ac7c6f84d3659bef3691a984cb7e587e414401a and independent native/formula10549/3e68c485c329f94620b5574ac7c7b1267028715b1c60a206f33519d52760f5ae, plus actual545 and553 in full. The directly used paid inputs are545's normalized constant term, completed meromorphic continuation and full Maass-Selberg formula, ordinary Mellin/Fourier inversion and the prior actual Theta/S_exp convergence/unfolding. I do NOT import a full automorphic spectral-Plancherel theorem or identify the range with every continuous-spectrum vector.

## 1. Frozen actual map, mean and measure

Use M=PSL2(Z)\H, dmu=dxdy/y^2, cusp width1 and volume pi/3. The physical source is complex r=e^(u/2)f, Fourier convention rhat(t)=integral r(u)exp(-itu)du. For compact smooth r define

    h_r(y)=sqrt(y)r(log y),
    Theta_r(z)=sum_(Gamma_infinity\Gamma)h_r(Im gamma z),
    mu_-(r)=integral exp(-u/2)r(u)du,
    c(r)=3mu_-(r)/pi,
    T0 r=Theta0_r=Theta_r-c(r)1.

The prior actual calculation proves that Theta_r is continuous/bounded and supported in a bounded-height part of the fundamental domain. Absolute ordinary unfolding gives integral_M Theta_r dmu=mu_-(r). Thus T0r has ordinary mean0 and lies in ordinary L2(M). The mean factor3/pi uses precisely the width1 hyperbolic measure; it is not6/pi in this source variable. The seed's L2(dy/y^2) norm equals the original physical ||r||_du norm, not ||f||_du.

## 2. A uniform scattering bound from the paid diagonal MS formula

Write Lambda(w)=pi^(-w/2)Gamma(w/2)zeta(w), phi(s)=Lambda(2s-1)/Lambda(2s), and E(z,s): y^s+phi(s)y^(1-s). Lambda is meromorphic, not entire xi. For s=sigma+it, 1/2<sigma<=2, |t|>=1, the denominator has no zeros because Re(2s)>1 and the ordinary Euler product applies. This uses no critical-strip zero-location assumption. The normalized truncated E_Y(s) is a genuine L2 vector, as follows also by dividing the paid completed truncation by its nonzero completion factor in this region.

Put delta=2sigma-1>0. The full old545 formula at equal parameters is

    ||E_Y(s)||^2
      =[Y^delta-|phi(s)|^2Y^(-delta)]/delta
       +[conjugate(phi(s))Y^(2it)-phi(s)Y^(-2it)]/(2it).

The mixed term is REAL and its absolute value is at most |phi(s)|/|t|, not twice that value. Positivity of the left side gives

    |phi|^2Y^(-delta)<=Y^delta+delta|phi|/|t|.

With x=|phi|Y^(-delta), this is x^2<=1+(delta/|t|)x. The positive quadratic root is at most1+delta/|t|. Choosing Y=2, delta<=3 yields

    |phi(s)|<=2^delta(1+delta/|t|)<=32.                 (A)

The upper bound is uniform all the way toward the unitary line, at these large heights. It requires neither a derivative bound on phi nor an unreviewed spectral decomposition.

## 3. Unitary-line regularity and exact residue

Set g(s)=Lambda(2s). The functional equation and real-type conjugation give

    phi(s)=g(1-s)/g(s),
    g(conjugate(s))=conjugate(g(s)).

At any s0 with Re s0=1/2, 1-s0=conjugate(s0). The numerator and denominator have the SAME meromorphic order there, including possible common zeros or poles. Their quotient is consequently holomorphic and nonzero at s0 after removable continuation. Where neither vanishes, the quotient is conjugate(g(s0))/g(s0), of modulus1; continuity gives the same conclusion at the removable points. In particular the two Lambda poles at s=1/2 cancel and phi(1/2)=-1. Thus

    Phi(t):=phi(1/2+it),
    |Phi(t)|=1, Phi(-t)=conjugate(Phi(t)), Phi(t)Phi(-t)=1.

No assertion about unknown zeta zeros, PNT improvement or unitary-line zeros of the uncompleted Eisenstein family is required for this scalar statement. In the open strip Re s>1/2, phi has only the pole at s=1: the denominator is zero-free by absolute Euler convergence, and the only relevant numerator pole is there. Its residue is

    Res_(s=1)phi(s)=(1/2)/Lambda(2)=3/pi,
    Lambda(2)=pi/6.                                  (B)

The scalar phi, rather than the entire uncompleted E family, is all that must be moved to the boundary below.

## 4. Scalar constant-term contour, with the mean residue retained

Let M_r(z)=integral r(u)exp(zu)du and m_r(s)=M_r(1/2-s). For compact smooth r, m_r decays faster than any power on vertical lines, uniformly on the fixed real-part strip[1/2,2]. On Re s=2, Mellin inversion gives

    h_r(y)=(2pi i)^(-1)integral_(Re s=2)m_r(s)y^s ds.

The initial Poincare/Mellin exchange is absolute: |E(z,2+it)|<=E(z,2), and m_r is integrable in t. Taking the x-average therefore gives the actual scalar constant coefficient

    a0(Theta_r)(y)=h_r(y)
       +(2pi i)^(-1)integral_(Re s=2)
                       phi(s)m_r(s)y^(1-s)ds.         (C)

For each fixed y>0, shift the second integral to Re s=1/2. On horizontal sides at height |t|>=1, (A) and the uniform rapid decay of m_r make the integrals tend to0. On compact heights, phi is meromorphic with only the s=1 pole and the already removable unitary-line points. Hence no boundary indentation, extra pole or independent finite-part convention is needed. Both limiting vertical integrals are absolutely convergent. Formula(B) contributes the POSITIVE residue

    (3/pi)m_r(1)y^0=(3/pi)M_r(-1/2)=c(r).

Subtracting c(r)1 from Theta_r leaves

    a0(T0r)(y)=sqrt(y)[r(log y)+(Sr)(log y)],           (D)
    (Sr)(u)=(2pi)^(-1)integral_R
                       Phi(t)rhat(t)exp(-itu)dt.

There is no unjustified L2 claim for a single untruncated E on the unitary line and no exchange over a growing source family. Only the scalar constant term in(C) was shifted. The unitary integral in(D) is absolutely convergent on the initial compact smooth source because rhat is Schwartz and |Phi|=1.

## 5. Reflection, conjugation and the exact ordinary norm

On the Fourier side, the complex-LINEAR operator S in(D) is

    (Sr)hat(t)=Phi(-t)rhat(-t).

Reflection is not conjugation of the source. The relations for Phi show S is a unitary involution on physical L2(R,du), hence self-adjoint. Put P_+=(I+S)/2, its ordinary orthogonal projection.

For compact smooth r, T0r is bounded on M and has mean0. Thus the following unfolding is absolute: the majorant is sup_M|T0r| times the finite strip integral of |h_r|. In the first-linear inner-product convention,

    ||T0r||^2=<Theta_r,T0r>
       =integral_0^infinity h_r(y)conjugate(a0(T0r)(y))dy/y^2
       =integral_R r(u)conjugate(r(u)+Sr(u))du
       =||r||^2+<r,Sr>
       =2||P_+r||^2<=2||r||^2.                        (E)

Centering is essential in the first equality; <c1,T0r>=0 uses its actual ordinary mean. In particular the norm identity and upper2 are ACTUAL, not a conditional statement with an unpaid Plancherel premise. Elementary source Fourier Plancherel is used for the unitary multiplier/reflection; a spectral-Plancherel theorem on M is not used.

## 6. Extension order and exact role limits

The bound(E) first defines a unique bounded extension T0:L2(R,du)->L2(M) by compact smooth density. For a general L2 input, mu_- may not exist and the Poincare series need not have its pointwise meaning. T0 is then defined by this extension, not by separately evaluating an undefined constant or series.

For r in S_exp, choose smooth compact cutoffs r_n converging in S_exp and L2. The prior actual source construction is continuous S_exp->L2(M), while mu_- is continuous in S_exp. Therefore Theta_(r_n)-c(r_n)1 converges to the actual Theta_r-c(r)1 in L2(M). It also converges to the newly extended T0r by(E). Uniqueness identifies the two limits. This matches the exact physical noncompact405 relations, not merely an unspecified completed source.

General Theta_r for S_exp is rapid, but T0r is rapid MINUS a constant. Its native cusp polynomial is -c(r), not0 unless mu_-(r)=0. The product has its corresponding constant cusp model. These functions remain ordinarily integrable/square integrable, and RN agrees with their ordinary integrals, but the native alpha0 residue exception would still matter if one attempted to compute a raw Rankin residue. This proof uses no such residue. For principal P and its translates, mu_-=0, so T0P=Theta_P is rapid as before.

The exact norm identity(E) continues to all L2 sources. It also implies the extended range H0=RanT0 is closed: on the complete source subspace RanP_+, T0 is a sqrt(2)-isometry, while it kills KerP_+. It is enough for the parent argument to use closure RanT0. Do not identify H0 with the entire continuous automorphic spectrum, or with the full mean-zero L2(M), without a further theorem. Every image here is orthogonal to the constant function; the full ambient cusp spectrum is not being classified.

## 7. Strongest-old consumption and scope

Old553 already proves that the complex span of the physical405 principal translates is dense in physical L2 (and Hlog). Since T0 is now paid globally bounded in precisely that norm and agrees with Theta on those relations, it follows that closure Theta(P_c)=closure RanT0=H0. This is an output-closure consequence on the FROZEN carrier; the separate output-scope review and ROOT must retain all quotient/nonlinear continuity hypotheses before consuming it.

This strengthens the recoverable consequence beyond the prior finite-rank obstruction by supplying the previously unasserted centered norm premise. It does not change the uncentered map into a globally du-bounded operator: its mean functional is unbounded. It does not invalidate strong-topology escapes for genuinely different carriers, nor force general Dprime layers to annihilate noncompact principal relations. No new full Gamma/contact/proper-power/dual-pole/mixed core identity, integral sections/mixedRR capacity, growing Xi consequence or independent arithmetic input follows.

Recommendation: ACTUAL PASS for the global centered norm/contour/extension recovery. Its proof is the already paid full MS/constant-term framework plus elementary scalar contour, absolute unfolding and Fourier/Hilbert calculus, so standard-old recovery0 rather than a new mathematical contract or new whole-classical gain. Strongest old consequences, the actual core bottleneck and all three long-Goal gates remain unchanged/open. No C072/607, cadence reset, source/rank/parameter successor or Goal completion follows. ROOT must full-read and raw-pin this terminal exclusive record before consumption.

## 8. Complete final ROOT-version scope check

Before issuing this terminal pin I additionally read the COMPLETE root-direct-global-bound.md, RAW10447 bytes/SHA25624c142682e1181ae9d9dcaf65e7b25d38f0715b2678bf20d8ca470e9e689c057. Formula/domain/scope PASS for that exact version; no correction is required. It retains the correct mean factor3/pi, mixed-MS factor, positive contour residue, source reflection rather than source conjugation, ordinary integrals, S_exp cutoff agreement, centered constant cusp model and general-L2 extension limits. Its exact operator norm sqrt(2) follows legitimately from(E), closed plus-space isometry and the previously proved nonzero Theta_P. It does not require P_+ to preserve S_exp.

I also checked the final ROOT version's downstream closure logic. The augmented Phi=(mu_-,mu_+,T0) retains both degree coordinates even though it is not globallydu bounded. Principal images have closure {0}^2 directsum H0, using their exact zero moments and the paid cyclic family. On a closed Hilbert quotient the centered source image is therefore zero; this says nothing about unused ambient cusp vectors. For nonlinear readouts on the actual Phi(S_exp) subspace, the proof correctly requires individual continuity into a Hausdorff target and invariance under EVERY principal coset. Principal approximants keep both degrees fixed, so their images converge to the desired same-degree source image in the inherited output topology. Uniqueness of the constant sequence's limit then gives degree-only dependence. No uniform bound or modulus across indices is needed for that limited exact-descent class. The ROOT version explicitly keeps general Dprime layers, stronger/nonclosed output structures, outside source information and genuinely different signed/indefinite mechanisms outside the obstruction. This final scope PASS is not a new independent RH proof or a certification of every upstream cited theorem.

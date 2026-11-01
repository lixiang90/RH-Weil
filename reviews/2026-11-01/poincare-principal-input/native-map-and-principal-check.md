# Independent formula and scope check: the actual incomplete-Eisenstein map

2026-11-01; /root/poincare_principal_formula, exclusive output. This is a terminal admission/formula review, not ROOT settlement or C072. I recovered README/STATE/check/show, the active Goal, stopped C071, latest Z decision and macro frontier, then read formation-and-test.md, actual405 sections2-5, actual545 sections1/4 and the existing reviewed RN definitions. No web/PDF/body extension, scientific code, numerical run or authority-file edit was used. The parent's current runtime1793085111 observation is not replaced by a child-local Goal claim.

I also read the complete final ROOT direct calculation: root-direct-calculation.md, RAW8716 bytes/SHA256 a41d15e1abf7df6eb446d7246ac7c6f84d3659bef3691a984cb7e587e414401a. **Formula/scope PASS: no correction is required in that version.** The independent checks and exact limits follow.

Old versions actually read: notes/405-f1-adelic-restriction-moments-and-radical.md,14633 bytes/SHA256 fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d; notes/545-modular-packet-norm-cusp-blindness-and-weil-transport-gate.md,13140 bytes/SHA256 25b778a2c1d1b9360ff2dd553f853a33c0dda7575740ab3aeac6ec46f555acfa. No old PDF was reread. The separate strong-old task governs additional historical dedup.

## 1. Legal map, measure and fixed-window norm

Use Gamma=PSL2(Z), M=Gamma\H, dmu=dxdy/y^2 and cusp width1. For physical complex r put

    h_r(y)=sqrt(y)r(log y),
    Theta_r(z)=sum_(Gamma_infinity\Gamma) h_r(Im gamma z).

For smooth r supported in[-L,L], the seed support is[a,b]=[exp(-L),exp(L)] and

    integral_0^infinity |h_r(y)|^2dy/y^2=||r||^2_du.

This is r-du. If r=exp(u/2)f, it is integral exp(u)|f(u)|^2du, not the unweighted f-du norm.

On the standard fundamental domain y>=sqrt(3)/2, nonidentity cosets have primitive bottom row(c,d), c>=1, and height v=y/[(cx+d)^2+c^2y^2]. A nonzero seed term forces v>=a, hence c<=2exp(L/2) and y<=exp(L). For each c the allowed d lie in an interval of length at most2exp(L), giving at most2exp(L)+1 integers. With the identity, N_L=1+6exp(3L/2) is a sufficient overlap upper for L>=0. It is not a degree or a necessary growth fee. Pointwise Cauchy-Schwarz and nonnegative unfolding give

    ||Theta_r||^2_L2(M)<=N_L integral_0^infinity |h_r|^2dy/y^2
                       =N_L||r||^2_du.

The seed vanishes above b and nonidentity heights are<=1/y, so Theta_r is zero for y>exp(L). The bound extends the linear map to all physical L2([-L,L]); zero-extension Dlog controls this du norm. Native pointwise continuity/RN membership is asserted on smooth sources, not automatically on every L2 representative. The extended form is the ordinary Hilbert Gram. No global whole-line du bound or uniform-in-L growing-Weil estimate has been proved.

## 2. Strong-source extension and RN role

For the complexification of405's S_exp, both multiplication by exp(u/2) and its inverse are continuous. The seed and its logarithmic derivatives decay faster than all powers at0 and infinity. On compact z-sets, the Poincare series converges locally uniformly: for an integer A>1 the small-height tail is bounded by a finite source seminorm times the convergent c,d sum below. Its differentiated series have the same property using finitely more derivative seminorms.

In the cusp y>=2, every nonidentity height v<=1/y. Since |h_r(v)|<=C_A(r)v^A for v<=1,

    sum_(c>=1,d in Z)|h_r(v)|
      <=C_A(r)y^A sum_(c,d)[(cx+d)^2+c^2y^2]^(-A)
      <=C'_A(r)y^(1-A) sum_(c>=1)c^(1-2A).

The shifted d-sum estimate is uniform in x: one maximum term plus a constant times the integral of (t^2+(cy)^2)^(-A) bounds it by C_A(cy)^(1-2A) when cy>=1. The identity seed decays faster than all powers at infinity. Choosing A arbitrarily large proves all-N cusp decay of Theta_r. The constants depend on finitely many S_exp seminorms, yielding a continuous S_exp->L2(M) map and the stated strong-source extension. This is not boundedness in one global du or Hlog norm.

Consequently Theta_r conjugate(Theta_s) has native cusp model0 and all-N remainder. Its prescribed RN integral is exactly its ordinary integral. Thus

    B_Theta(r,s)=integral_M Theta_r conjugate(Theta_s)dmu

is a genuine first-linear positive Gram on this source image. The previous native non-L2 negative-square control does not refute positivity of this particular image. Positivity and a legal native intermediate object do not establish principal descent or a complete Weil identity.

## 3. Exact absolute unfolding and the actual405 witness

For real t>1, write the ordinary normalized Eisenstein constant term as

    E(z,t): y^t+phi(t)y^(1-t),
    phi(t)=Lambda(2t-1)/Lambda(2t)>0.

The parameter t here is real, not the Fourier-frequency variable in545. E(z,t) is positive. Tonelli applied first to the absolute seed gives

    integral_M sum_gamma |h_r(Im gamma z)| E(z,t)dmu
      =integral_0^infinity |h_r(y)|[y^t+phi(t)y^(1-t)]dy/y^2<infinity.

Finiteness holds for each r in S_exp because its seed has all power decay at both ends. Therefore the signed/complex unfolding is justified without a spectral-line superposition or an untruncated-E L2 claim:

    L_r(t):=integral_M Theta_r E(z,t)dmu
           =M_r(t-1/2)+phi(t)M_r(1/2-t).

This is a bilinear integrable witness, not an ordinary source trace or a Hilbert norm lower estimate.

Use actual405 h=E_eta and p=(D^2+D)h, with

    M_h(t)=xi(t)/2,
    M_p(t)=t(t-1)xi(t)/2,
    M_p(0)=M_p(1)=0, M_p(2)=pi/6.

These are old paid identities, including the complete contact/pole normalization. Sharp invariance of h implies sharp invariance of p: conjugating D by sharp sends D to -D-1, which preserves D^2+D. Hence M_p(1-t)=M_p(t). For physical P(u)=exp(u/2)p(u), P is even and in S_exp, with Q_zeta(P)=0 and full mixed radical vanishing by405. Since M_P(z)=M_p(z+1/2),

    L_P(2)=[1+phi(2)]M_p(2)=[1+phi(2)]pi/6>0.

Therefore Theta_P is nonzero, so B_Theta(P,P)>0 while Q_zeta(P)=0. The witness uses no unknown zero position or simplicity. Absolute ordinary unfolding also yields integral_M Theta_P dmu=M_P(-1/2)=M_p(0)=0. Removing the ordinary constant mode leaves Theta_P unchanged; degree-only corrections whose coefficients are mu_+P and mu_-P likewise vanish on P.

## 4. Translations and precisely fixed finite-rank corrections

For P_a=tau_a P, the uncentered source is exp(-a/2)tau_a p and remains in the actual principal ideal. Absolute unfolding gives

    L_(P_a)(t)=M_p(t)[exp(a(t-1/2))+phi(t)exp(-a(t-1/2))].

For real t>=2,

    0<phi(t)=B(t-1/2,1/2) zeta(2t-1)/zeta(2t)<=3pi/4.

The beta integral is<=B(3/2,1/2)=pi/2; zeta(2t-1)<=zeta(3)<3/2 and zeta(2t)>=1. Thus no new gamma asymptotic is needed. Suppose finitely many distinct nonnegative a_i give sum_i c_i Theta_(P_ai)=0 in L2. Continuous rapidly decreasing representatives yield the same pointwise zero and all L-witnesses vanish. Since M_p(t)>0 for t>1, divide by M_p(t)exp(a_max(t-1/2)), where a_max is the largest a with nonzero coefficient. If a_max>0, all other direct and all reflected terms tend to0 as t->infinity, contradicting c_max!=0. If only a=0 remains, 1+phi(t)>0 gives the same contradiction. Hence these principal images span an infinite-dimensional space.

For any fixed finite-rank linear R:S_exp,C->L2(M), exact annihilation by A=Theta+R of ALL physical principal relations would imply Theta(P_c) is contained in range(R), an impossibility. This exact principal-kernel statement needs no global-du boundedness and does not even need Frechet continuity of R. It is an additive fixed-output-rank statement, not a claim about arbitrary infinite-rank quotient maps.

To infer failure of a complete positive-Gram identity asserted only for ALL compact sources, an extra continuity premise is necessary: A:S_exp->L2 must be Frechet-continuous. Then cutoff approximations to any P_a converge in S_exp, complete Q_zeta is continuous by405, and the compact identity extends to the noncompact principal witness. Theta itself has this continuity; fixed finite-rank R with continuous S_exp coefficient functionals also does, even if du-unbounded. For discontinuous R, do not infer compact-only failure just from a noncompact principal test. For an identity directly asserted on ALL S_exp, positivity already forces A to annihilate each principal relation without this extension argument. A common scalar0 cannot match the nonzero537 probe; a fixed positive scalar does not remove the obstruction.

No conclusion is made about growing rank, per-layer Dprime approximation, source-adaptive/nonlinear recipes, paid signed comparisons, indefinite RN/Hodge pairings or relative/higher quotients. Dprime approximation does not require each layer to annihilate the noncompact principal class. No uniform lower in the translation parameter or growing-layer error has been established.

## 5. Root-version verdict and old consequence

The reviewed ROOT8716 version retains the correct measure, source norm, all-N domain, both moment directions, original source change and finite-rank/compact-continuity limits. Its N_L count is a sufficient real upper, its E2 witness is absolutely integrable rather than L2, and its principal-span proof only needs bounded positive phi on real t>=2. Formula/scope PASS is justified by the calculations above.

The seed is already an EXACT instance of545's construction: set f_r(v)=exp(v/2)r(-2v); then y^(3/4)f_r(-log(y)/2)=sqrt(y)r(log y). In545's nonnegative-unfolding norm expression, 2 integral exp(-v)|f_r(v)|^2dv=||r||^2_du. This is not a new packet, a new whole norm bound or a new positivity input. The principal witness is the old405 nonzero Mellin moment, and its translation/rank qualification is elementary finite-exponential independence of that paid family. Old553's bounded-global-readout hypotheses must not be silently imposed on this Frechet map.

Recommendation: consume a concrete standard-old rejection of THIS recipe/principal claim, with no new independent classical input and zero incremental mathematical responsibility. ROOT's separate strongest-old audit and final consumption govern the sole cadence. No C072/607 or source/parameter/math successor follows. Strongest whole17/16, finite9/8E448,605 one-head/all-complement positive completion,560/602 whole identities and whole4/5 negative-inertia UPPER are unchanged. Actual principal/sections/mixed/growing core-coupling/Xi obligations and all three Goal gates remain open; same long Goal remains active. This is not a Goal completion or a general modular/regularized no-go.

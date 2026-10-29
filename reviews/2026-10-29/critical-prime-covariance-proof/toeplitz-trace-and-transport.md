# Th6.5: actual Toeplitz kernel, strict trace update, and physical K transport

2026-10-29. Independent domain/proof audit for the unique critical-prime covariance gate. This is a draft for root consumption, not an iteration settlement. No source, STATE, cadence, Goal, or Git mutation is part of this audit. The original paper is preserved unchanged.

The result of this audit is that the actual unweighted Sonin projection satisfies the uniform Toeplitz commutator estimate, and the exact localized trace update can be proved using positive compressions and Hilbert--Schmidt operators. The growing-prime covariance rate additionally requires the shrinking-window localization proved in the separate localization audit. The K update below is derived directly from the already-paid identity in 560; it does not certify the paper's insufficiently expanded notation q_{infinity,F}.

## 1. Fixed objects, source, and precise consumption scope

The fixed paper is `literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md`, 61862 bytes, SHA256 `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`. The proof clauses audited here are lines1024--1081, (6.21)--(6.26), and lines1093--1100, exact projection/trace update. The necessary conventions in lines21--57 and reflected archimedean conjugation in lines698--717 were read. Lines1083--1091 state how these pieces consume (6.20); the independent localization file supplies that additional proof obligation. No claim uses the sharp result in section6.4 or section7. Reference[11] is not imported as a black-box uniform estimate: the necessary Toeplitz argument is proved below.

Recovery read goals/README and STATE, ran research_state.py check and then show, and read the same active Goal, D20261029X, macro summary, and `reviews/2026-10-29/core-input-portfolio/next-critical-prime-covariance-proof-gate.md`. The stopped C058 budget is not reopened by this document. No round number or Goal completion is claimed.

Use exactly the objects in 560, 585 and 589. In physical logarithmic coordinates

    H = L2(R,dy),  (U_a v)(y)=v(y-a),
    B_F = product_{q in F}(I-q^(-1/2) U_logq),
    M = Ran P,  G_F = (P B_F* B_F P)|M,
    Pi_F = B_F P G_F^(-1) P B_F*.

P is the gap-one archimedean cosine Sonin orthogonal projection. Pi_F is the actual physical orthogonal projection onto B_F M; B_F is bounded invertible for each finite F and is not unitary. The source operator and Fourier convention are

    A_f = integral f(a) U_a da,
    fhat(t) = integral f(u) exp(-itu) du,
    ||fhat||^2_{L2(dt/(2pi))}=||f||^2_{L2(du)}.

The source f is physical; a bare multiplicative source is exp(-u/2)f(u). The source variable u, receiver variable y, raw Mellin boundary variable t, and an evaluation vector are different roles. The paper's convolution T_f is this A_f. In particular the actual localized trace already paid for every finite F and every compact smooth complex f is

    t_F[f] = Tr(A_f Pi_F A_f*) = ||A_f Pi_F||_HS^2 < infinity.       (T)

The spectral norm remains dt/(2pi) after reflection. The paper's section6.1 positive compression includes a generic component; it must not be identified with (T). The Sonin projection S used in section6.3 and below is the reflected Mellin conjugate of Pi_F, so it does give (T). The range formula, Gram inverse, and actual trace are those of 560/585/589, rather than a quotient-only description.

Fix a prime p, L=log p, r=p^(-1/2), predecessor F={q prime:q<p}, and F'=F union {p}. All the following operator statements hold for an arbitrary finite predecessor F not containing p. On the reflected receiver boundary let V be multiplication by exp(itL), and put

    D=I-rV,  B=(I+V)*(I+V)=2I+V+V*,  0 <= B <= 4I.

The reflected multiplier of A_h is hhat(-t); hence W0=A_h* A_h is multiplication by w(t)=|hhat(-t)|^2. The reflection changes no norm, trace, or real-variable cutoff estimates. In the paper's unreflected convention w=|hhat(t)|^2; simultaneous reflection of all the multipliers gives the same statements. For f_p=h+U_L h, W=A_fp* A_fp=W0 B. These are bounded commuting multipliers. No assertion that S commutes with them is used.

## 2. Both Sonin support conditions give an actual unweighted Toeplitz kernel

We first check the phase and both directions of the space identification. Define the raw Mellin transform by

    (Mg)(t)=integral_0^infinity g(x) x^(-1/2-it) dx,
    f(t)=(Mg)(-t).

The logarithmic map g -> exp(y/2)g(exp y) is unitary. Under reflection the condition g=0 on (0,1) is exactly f in H2(C_+), by the L2 Fourier support characterization of the upper Hardy space. The full boundary Hilbert space is L2(R,dt/(2pi)). Let H2_- be the orthogonal complement of H2_+ on this boundary.

The cosine transform C has kernel 2 cos(2pi xy). With gamma(s)=pi^(-s/2) Gamma(s/2), its Mellin multiplier is

    M(Cg)(t) = [gamma(1/2-it)/gamma(1/2+it)] (Mg)(-t).       (C)

For example, initially on a Mellin strip this follows by integrating the cosine kernel:

    2 (2pi)^(-s) Gamma(s) cos(pi s/2)=gamma(s)/gamma(1-s),

and the L2 statement follows by the unitary Mellin transform and density. This fixes the sign; it agrees with the paper's reflected ratio. Physical complex conjugation J commutes with C because its kernel is real. If

    u_infinity(t)=gamma(1/2+it)/gamma(1/2-it),

then (C) applied to C J g gives on the reflected boundary

    M(C J g)(-t)=u_infinity(t) overline{f(t)}=:C0 f(t).       (C0)

The second physical support condition Cg=0 on (0,1) is equivalent to C J g=0 there. Thus the actual complex Sonin space, after reflection, is exactly

    { f in H2_+ : C0 f in H2_+ }.

Here both implications use the two physical support conditions; invariance under an anti-linear conjugation alone would not prove the claim. On the real boundary |u_infinity|=1, and complex conjugation maps H2_+ onto H2_-. Conjugating the second condition gives

    overline{u_infinity} f in H2_-.

Consequently the reflected archimedean range is

    K0=ker T_phi0,  phi0=overline{u_infinity},
    T_phi=P_+ M_phi|H2_+ .                                      (K0)

This is an unweighted Hardy Toeplitz kernel with bounded unimodular symbol; no receiver measure or weighted norm has been changed.

After reflection, the finite Euler product is

    D_F^+(z)=product_{q in F}(1-q^(-1/2) exp(iz logq)).

Both D_F^+ and its inverse belong to H-infinity(C_+) for each finite F: for Im z>=0 every factor is bounded away from zero by 1-q^(-1/2). These individual norms need not be uniform in F. The paid actual range formula is Ran S=D_F^+ K0. Since multiplication by D_F^+ is a bijection of H2_+,

    f in D_F^+ K0
      iff f in H2_+ and P_+(phi0 f / D_F^+)=0.

Thus, with equality in the original boundary norm,

    Ran S=ker T_phiF,  phiF=phi0/D_F^+ in L-infinity(R).       (KF)

This is a two-way membership argument. It is not an assertion that D_F^+ is unitary or a use of a possibly growing inverse-angle bound. No bound on ||phiF|| or ||(D_F^+)^(-1)|| appears in the commutator constant below. The symbol can also be replaced by the unimodular symbol phi0 overline{D_F^+}/D_F^+: multiplying its Toeplitz operator on the left by the invertible coanalytic Toeplitz operator T_overline{D_F^+} preserves the kernel. This optional replacement is not needed.

## 3. Universal full-boundary rank-two commutator and every Cayley scale

Let K=ker T_phi be a disk Hardy Toeplitz kernel, and let S be its orthogonal projection in the full boundary L2(T). Write Z=M_z, a unitary on that full space. The operator

    T_phi Z - Z T_phi

has rank at most one: P_+ z P_- applied to phi f depends only on its Fourier coefficient of degree -1. For f in K, (I-S)Zf belongs to H2 intersect K-perp. T_phi is injective on this intersection, and its image on these vectors lies in the same one-dimensional space. Therefore

    rank((I-S)ZS)<=1.

For the other direction, if f in K and f(0)=0, then bar z f belongs to H2 and

    phi bar z f=bar z phi f in H2_-.

It follows that bar z f is in K. The map (I-S)Z* S therefore vanishes on the codimension-at-most-one kernel of evaluation at zero in K, and has rank at most one. This uses full multiplication by bar z: the possible negative Hardy component for f(0) nonzero is included, not discarded. Both off-diagonal blocks have operator norm at most one. Since

    [S,Z]=SZ(I-S)-(I-S)ZS,

their rank and trace-norm bounds give

    rank[S,Z]<=2,  ||[S,Z]||_S1<=2.                            (R2)

For every integer n, telescoping Z^n (and Z* for negative n) gives ||[S,Z^n]||_S1<=2|n|. Hence, first for Fourier polynomials and then by trace-norm convergence,

    ||[S,M_v]||_S1 <= 2 sum_n |n| |vhat(n)|.                   (F)

This applies after the exact unitary Cayley transformation at each d>0,

    b_d(t)=(t-id)/(t+id).

For clarity, the boundary weighted-composition map from disk to half-plane is multiplication by sqrt(2d)/(t+id) followed by composition with b_d. With normalized measures dtheta/(2pi) and dt/(2pi), its modulus squared and the Cayley Jacobian agree. It is a full-boundary unitary, maps H2 onto H2, and intertwines multiplication by v with multiplication by v(b_d). It therefore intertwines the Hardy projections and the Toeplitz kernels as well. Formula (F) becomes

    ||[S,M_{v(b_d)}]||_S1 <=2 sum_n |n||vhat(n)|,             (6.21)

with the same numerical constant at every scale d and for every finite F. This is where (KF) is used; a general range relation without the Hardy kernel identification would not suffice.

For completeness split the Fourier sum at an integer N>=1. Parseval and Cauchy--Schwarz give

    sum_|n|<=N |n||vhat(n)| <= C N^(3/2)||v||_2,
    sum_|n|>N  |n||vhat(n)| <= C N^(-1/2)||v''||_2.

Choosing N comparable to max(1,sqrt(||v''||_2/||v||_2)), with the zero function treated separately, proves

    sum_n |n||vhat(n)|
       <= C (||v||_2+||v||_2^(1/4)||v''||_2^(3/4)).          (6.22)

There is no missing constant when the proposed optimum is below one: choose N=1 and absorb ||v''||_2 into ||v||_2 in that case.

## 4. Actual cutoff commutators, coercivity, and strict trace ideals

Choose a fixed even smooth nonnegative cutoff chi, equal to one on [-1,1], zero outside [-2,2], nonincreasing on [0,infinity). Fix h in C_c-infinity(R), so w is Schwartz. For L>=1, d=delta=L^(-2/5)<=1, put a=w chi(t/d)B. In the Cayley coordinate t=-d cot(theta/2), this multiplier has fixed support away from infinity. Its circle L2 norm is O_h(1). Two derivatives of w(-d cot(theta/2)) and chi(-cot(theta/2)) are uniformly bounded for d<=1 on that support; two derivatives of B cost at most C(1+Ld)^2. Thus

    ||v''||_2<=C_h(1+Ld)^2,
    ||[S,M_{w chi(t/d) B}]||_S1<=C_h(1+Ld)^(3/2).             (6.23)

At the fixed Cayley scale d=1, two circle derivatives of w(t)(1-chi(t/T))B(t), T>=1, introduce polynomial powers of t, at most two powers of L, and cutoff derivatives. Since |t|>=T on the support and w is Schwartz, all these polynomial powers are absorbed by arbitrarily high Schwartz seminorms. The circle H2 norm, and hence the Fourier sum in (F), is at most C_{h,N}(1+L)^2 T^(-N), for each fixed N. Therefore

    ||[S,M_{w(1-chi(t/T))B}]||_S1
       <=C_{h,N}(1+L)^2 T^(-N).                              (6.24)

All constants here depend on fixed h, cutoff and (for the tail) N; they do not depend on F, the multiplier norm of its inverse Euler product, or an angle between ranges.

On SH, let

    G=(S D*D S)|SH=(1+r)^2 I_SH-r S B S.

Since ||Dx||>=(1-r)||x||,

    G>=(1-r)^2 I_SH,  ||G^(-1)||<=(1-r)^(-2).                (G)

This is the exact full inverse. In particular it is uniformly bounded for p>=2. If [S,a] is trace class, then Sa(I-S)=[S,a](I-S) is trace class, so the ordinary trace is legitimate and

    |Tr_SH(Sa(I-S)B S G^(-1))|
       <=4(1-r)^(-2)||[S,a]||_S1.                            (6.25)

The notation G^(-1) means its action on SH; adding terminal S makes the corresponding full-space extension explicit.

For (6.26) take a bounded nonnegative multiplier u, commuting with B, and assume the positive compression has finite trace

    tau_u=Tr_SH(SuS)=||sqrt(u)S||_HS^2<infinity.

This includes every actual weight used below, since 0<=u<=w and (T) gives tau_w<infinity. It is not necessary to prove (6.26) for arbitrary unbounded formal weights. Factor the actual operator as

    SuB(I-S)BS
      =(S sqrt(u))[sqrt(u)B^2S-sqrt(u)BSBS].

The first factor is HS with norm sqrt(tau_u). Commutation of sqrt(u) and B gives

    sqrt(u)B^2 S = B^2 sqrt(u)S,
    sqrt(u)B S B S = B sqrt(u)S B S.

Each term in brackets is HS with norm at most 16 sqrt(tau_u), using ||B||<=4. The product of two HS operators is trace class, and

    ||SuB(I-S)BS||_S1<=32 tau_u.                              (6.26)

Thus every subsequent cyclicity is ordinary trace-class cyclicity. In this proof Tr(uS) in the paper means the finite positive compression Tr_SH(SuS), or equivalently this HS square. It is not an unproved assertion that the bare product uS is trace class.

The localized diagonal convention is consistent with this definition. If k_F(t,s) is the reproducing kernel of the actual reflected range, in the norm dt/(2pi), then for nonnegative u the positive-compression trace is

    tau_u=integral u(t) k_F(t,t) dt/(2pi).

One can verify the formula with an orthonormal basis of SH, then apply Tonelli; no signed trace or infinite Hardy diagonal is used. The density rho_F=k_F(t,t)/(2pi) appearing in 560/589 therefore has exactly the same normalization.

## 5. Exact projection update and HS interpretation of both localized traces

Multiplication by D maps SH onto the actual new Sonin range: B_F and the added Euler factor commute, so the physical range formula gives DS H=B_{F'}M after reflection. Since D is bounded invertible, this range is closed and its exact orthogonal projection is

    S'=D S G^(-1) S D* .                                     (P')

Define A=SWS|SH. It is a positive trace-class operator because 0<=W=W0B<=4W0 and tau_w=t_F[h]<infinity. The old localized trace is

    t_S[f_p]=Tr_SH(A)=||A_fp S||_HS^2.

The bare products WS and WS' are not required to be trace class. This qualification is a necessary repair of the paper's shorthand at lines1096--1097; its source file is not changed.

The map J_D=DS G^(-1/2):SH->H is an isometry onto S'H. Since W commutes with D and D*, J_D* W J_D is a positive trace-class operator (bounded D and G^(-1/2), with W^(1/2)S HS). The actual new trace equals

    t_S'[f_p]
      =Tr_SH(G^(-1/2) S D* W D S G^(-1/2)).                  (T')

Let X=S W(I-S)B S|SH. Formula (6.26) with u=w makes X trace class. Using D*D=(1+r)^2I-rB and the commutation of W with D,

    S D* W D S = A G - r X.                                 (E)

Indeed the only difference between S W B S and S W S B S is S W(I-S)B S. Substitute (E) into (T'). Both A and X are S1 and all powers of G used here are bounded. Cyclicity gives

    Tr(G^(-1/2) A G^(1/2))=Tr(A),
    Tr(G^(-1/2) X G^(-1/2))=Tr(X G^(-1)).

Consequently the exact, actual identity is

    Delta t_p[f_p]:=t_F'[f_p]-t_F[f_p]
      =-r Tr_SH(S W(I-S)B S G^(-1))=-r C_p.                  (DT)

Reality of C_p follows directly from the real difference of the two finite positive traces and r>0. There is no need to move a non-trace-class bare WS through a trace, or to assert that a formal skew-adjoint commutator has trace zero. The full Gram inverse is present throughout.

## 6. Exact dependence on the independent localization proof

The companion `localization-and-rate-proof.md` is a separate output. This domain audit proves its listed obligations D1--D4: the full-boundary Toeplitz projection, the normalized positive diagonal trace, G coercivity/legitimate ideals, and (6.25)--(6.26). It does not replace that file's shrinking-window proof by the fact that a localized density was written in the original paper. Conversely the localized density alone does not prove D1--D4.

For root consumption, the needed additional statement is the actual predecessor density estimate

    sup_{delta<=|t|<=L^b} k_<p(t,t)
       <=C exp(-c A delta^2),
    delta=L^(-2/5), A=sqrt(p)/L, and each fixed b>0,          (LOC)

including omission of the prime p, in the same dt/(2pi) norm, with constants uniform along p. This is the (6.20) obligation. There is no inverse-angle cost to add on top of it. A generic Paley--Wiener projection without (LOC) is not a counterexample to its present use.

For clarity, if (LOC) is admitted, the rate follows as an actual operator trace calculation. Set T=L and split w into nonnegative weights

    u0=w chi(t/delta),
    u1=w[chi(t/T)-chi(t/delta)],
    u2=w[1-chi(t/T)].

The monotonic cutoff and T>=delta ensure positivity; each weight is bounded by w. Apply (6.25) to a=u0B and a=u2B. The center is O_h((1+Ldelta)^(3/2))=O_h(L^(9/10)); the tail is O_{h,N}(L^(2-N)). The middle support is delta<=|t|<=2L, so choose fixed b=2 in (LOC) (2L<=L^2 for large L). Positive compression and its normalized diagonal give

    tau_u1<=C_h L exp(-c A delta^2).

Use (6.26), followed by (G), for its contribution. Since A delta^2=sqrt(p)/L^(9/5) tends to infinity and one may fix N=4, these estimates yield

    C_p=O_h(L^(9/10)),
    Delta t_p[f_p]=O_h(p^(-1/2) L^(9/10)).                  (RATE | LOC)

The constants depend on the single fixed h and the fixed cutoff; this is not a uniform assertion over all moving h_p or all expanding Dlog balls. The local rate consumes (LOC), rather than following from old fixed-source qualitative localization or from (DT) alone.

## 7. Transport to the actual compact error without importing paper q

The entire q_{infinity,F} form in the paper's (6.19) is only referred to earlier normalizations; this audit does not independently identify that whole symbol with a form in this repository. It is unnecessary for the desired actual K consequence. Use instead the exact paid finite-F identity in 560, on any common physical interval I containing the source supports:

    t_F[f]=q_Gamma[f]-P_F[f]+<f,K_(F,I)f>,                 (560)
    P_F[f]=sum_{q in F,k>=1} (log q) q^(-k/2)
                         [R_f(k log q)+R_f(-k log q)],
    R_f(v)=integral f(u+v) overline{f(u)} du.

Here Gamma(t)=Re psi(1/4+it/2)-log pi=2 theta'(t), with the old contact/finite-part convention already paid. Its coefficient is not inferred from the new paper's q notation. For the same source and same I, q_Gamma cancels in subtracting (560) for F' and F. Thus exactly

    <f,Delta K_p f>=Delta t_p[f]+P_{p}[f],
    Delta K_p=K_(F',I)-K_(F,I).                               (DK)

For the single fixed nonzero h, let f_p=h+U_L h and choose a common I=I_p containing both translates. When L exceeds the diameter of supp h, the copies are disjoint, ||f_p||_du^2=2||h||_du^2, and

    R_fp(v)=2R_h(v)+R_h(v-L)+R_h(v+L).

In particular R_fp(L)=R_fp(-L)=||h||_du^2 and R_fp(+-kL)=0 for every k>=2. All added prime powers are present in (560); those with k>=2 vanish by support, rather than being dropped from the formula. Therefore

    P_p[f_p]=2L p^(-1/2)||h||_du^2.                          (PP)

Combine (DK), (PP), and (RATE | LOC) to get, conditional only on the separate (LOC) closure beyond the domains proved here,

    <f_p,Delta K_p f_p>
       =2L p^(-1/2)||h||_du^2+O_h(p^(-1/2)L^(9/10)).        (K-rate)

The leading coefficient two comes from the two opposite autocorrelations in 560. No 2pi factor is lost: the source norm and autocorrelation are physical du, while dt/(2pi) is used only for the unitary receiver representation. For fixed nonzero h the scalar Rayleigh quotient is consequently

    <f_p,Delta K_p f_p>/||f_p||_du^2
       =L p^(-1/2)[1+O_h(L^(-1/10))].                       (RQ)

This gives eventual positivity of this one scalar increment and a relative scalar limit after division by L/sqrt(p). Since L/sqrt(p) tends to zero, it is not operator-norm convergence, a uniform lower bound on Delta K_p, or a positive-operator assertion. In the full identity Q=t-K+pole the positive K coefficient is an adverse error contribution; (K-rate) alone neither makes Q negative nor improves the whole core/coupling budget.

Poles are not needed to form the finite-prime difference (DK). If the full Weil form is used instead, both poles and every unselected prime contribution must remain in the original identity; the unchanged pole term cancels when comparing the same source in the two finite-F decompositions. For a pole-free moving test one may fix nonzero psi in C_c-infinity and take h=(d^2/du^2-1/4)psi: integration by parts annihilates both exponential moments, and the same moments stay zero after translation. Such an h is nonzero: otherwise psi would solve the constant-coefficient homogeneous ODE psi''-psi/4=0, and compact support plus uniqueness would force psi=0. This optional source choice changes none of the domains above.

Finally ||f_p||_Dlog<=2||h||_Dlog for the translation-invariant logarithmic Fourier norm, from fphat=(1+exp(-itL))hhat. This does not bound stronger exponentially weighted source seminorms uniformly: translating a fixed source can cost p^N in such norms. A legal source and a correct scalar coefficient are not coverage of the whole required source family.

## 8. Root-consumption record and stop boundary

Paid here: exact actual reflected Sonin=unweighted Toeplitz kernel, all finite-F/uniform-scale rank-two commutators, the cutoff multiplier estimates, G coercivity, positive-compression/HS trace ideals, the actual exact projector update (DT), and the physical 560-to-K transport including all prime powers, two-sided correlations, pole handling, and source norms.

Separate required input: (LOC) and its growing-prime quantifiers, including omit-p stability. The localization companion proves it from the paid weighted entire-evaluation and actual range-kernel inputs; root must reconcile and consume those premises and this domain audit together. This file alone does not count an unconsumed companion draft as a theorem.

Changed premise compared with the paper's shorthand: bare Tr(WS), Tr(WS'), and Tr(uS) are interpreted and re-proved as finite positive-compression/HS traces; no claim about bare-product S1 membership is retained. Changed downstream path: (6.19)'s unspecified q form is not consumed; actual (K-rate) follows from (DT) plus old (560). These changes preserve every operator, source, full Gram inverse, normalization, and coefficient used in the actual consequence.

Old 585/589 fixed-source lower/upper or scalar normalization cannot supply a quantitative signed single-prime projection difference for f_p. Conversely this signed increment does not supersede their already-paid fixed-source growth conclusions, does not establish a whole-budget improvement, and does not remove the macro core/coupling bottleneck by itself. Root retains responsibility for comparison with the strongest old consequence and the macro admission gate. No iteration number, C059/596, new parameter search, section6.4/section7, external-reference expansion, or Goal completion is preauthorized by this proof note.

## 9. Exact input fingerprints

All entries below were checked as raw UTF-8/LF bytes. These fingerprints freeze input identity; they do not promote a companion draft into a root-consumed result.

| Input | Bytes | SHA256 |
|---|---:|---|
| Fixed raw source | 61862 | `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058` |
| 560 physical finite-F bridge | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| 585 actual fixed-source trace | 7857 | `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af` |
| 589 actual weighted/kernel transport | 7185 | `c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5` |
| Current next-critical-prime-covariance proof gate | 4739 | `ede94f14a3430afbd100d907ca3649929aaef1138cd065dc896513311b616f33` |
| Separate localization-and-rate proof | 14467 | `3a5c61a0aacdd6aa7815387e666939d086d0f4da01d939d9df7b52b5d1a2bf36` |

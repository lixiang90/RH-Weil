# ROOT direct strongest-old recovery: centered bound and output closure

2026-11-01; same Goal1793085111/baseline0c4f. This is a direct calculation for ONE strongest-old comparison, not ROOT settlement, new independent arithmetic input or a new contract. It uses old545's normalized full Maass-Selberg/constant-term data and basic Mellin inversion/unfolding, old405/553's actual principal source and cyclic closure, and the previous actualTheta domain proof. No external PDF/body/readscope or new spectral-Plancherel theorem is imported.

## 1. Frozen physical carrier and the mean

Let M=PSL2(Z)\H, dmu=dxdy/y², vol(M)=pi/3, h_r(y)=sqrt(y)r(log y), Theta_r=Poincare(h_r). For compact smooth physical r, Theta_r is bounded and compactly supported in cusp height, with the previous exact original-du seed norm. Its ordinary mean is mu_-(r)=integral exp(-u/2)r(u)du. Define

    c(r)=3mu_-(r)/pi,
    T0 r=Theta0_r=Theta_r-c(r)1.

Then integral_M T0 r dmu=0. The uncentered coefficient c is NOT bounded on global r-du. The present test concerns T0, not a false global bound for Theta or the augmented degree map. The strong S_exp map and its native rapid-image/ordinary-RN roles were paid in the prior exact input test.

For general S_exp r it is the UNcentered Theta_r which is rapid. T0r has constant cusp model -c(r), and a product has constant model c(r)conjugate(c(s)); it is still ordinary integrable and RN agrees with that ordinary integral. Do not transfer the phi=0 label to every centered source or use a raw residue without its alpha0 exception. This proof uses ordinary integrals, not an RN residue. On the actual principal and pole-free tests c=0, so their centered images remain rapid.

## 2. The old full MS gives a uniform scattering bound

Write phi(s)=Lambda(2s-1)/Lambda(2s), Lambda(w)=pi^(-w/2)Gamma(w/2)zeta(w), with its actual poles. For s=sigma+it, sigma>1/2, t!=0, delta=2sigma-1, old545's complete uncompleted MS diagonal is

    ||E_Y(s)||²
      =[Y^delta-|phi(s)|²Y^(-delta)]/delta
       +[conjugate(phi(s))Y^(2it)-phi(s)Y^(-2it)]/(2it).

Here E_Y is the actual cusp-constant-term-truncated Eisenstein vector, not an untruncated L2 vector. The mixed term has absolute value at most |phi(s)|/|t|. Nonnegativity of this genuine norm implies, with x=|phi(s)|/Y^delta,

    x²<=1+(delta/|t|)x,
    x<=(delta/|t|+sqrt((delta/t)²+4))/2<=1+delta/|t|.

Set Y=2. Thus |phi(s)|<=32 for1/2<sigma<=2 and |t|>=1. This is a bounded closed strip on its right side; no limiting source uniformity or favorable signed-Weil budget has been inferred. It is an elementary consequence of the already paid full MS Gram, not a new scattering or zero-free estimate.

For boundary values put g(s)=Lambda(2s). The functional equation gives phi(s)=g(1-s)/g(s). At Re s=1/2, conjugation gives 1-s=conjugate(s), and g is real-type. Numerator and denominator have equal zero/pole orders there, so their ratio is removable and nonzero. In particular at s=1/2 the two Lambda poles give phi=-1. Boundary phi is analytic and has modulus1. This argument does not assume a new zero-free statement on Re w=1 or unknown zeta zeros. In the OPEN right half-plane the denominator has no zeros by the absolutely convergent Euler product; the only phi pole between Re s=1/2 and2 is s=1, with residue (1/2)/Lambda(2)=3/pi. On bounded portions of the boundary strip away from this known pole, ordinary meromorphic compactness supplies the remaining uniform bound.

## 3. Scalar constant-term contour, with its residue retained

For compact smooth r let m_r(s)=M_r(1/2-s). On every closed vertical strip it decays faster than every power in |Im s|. Mellin inversion gives h_r(y)=(2pi i)^(-1)integral_Re2 m_r(s)y^s ds. Absolute initial Poincare summation is justified by |E(z,2+it)|<=E(z,2), and yields the complete constant term

    a0(Theta_r)(y)=h_r(y)
       +(2pi i)^(-1)integral_Re2 phi(s)m_r(s)y^(1-s)ds.

Move this SCALAR contour to Re s=1/2. The uniform32 bound from MS makes the horizontal sides vanish. Removable unitary boundary values and the same bound permit dominated passage to that line. The s=1 residue is POSITIVE and equals (3/pi)m_r(1)=(3/pi)mu_-(r)=c(r). No other pole is crossed. Therefore

    a0(T0 r)(y)=sqrt(y)[r(log y)+(Sr)(log y)],
    (Sr)(u)=(2pi)^(-1)integral_R phi(1/2+it)rhat(t)exp(-itu)dt.

With rhat(t)=integral r(u)exp(-itu)du and Plancherel measure dt/(2pi),

    (Sr)^hat(t)=phi(1/2-it)rhat(-t).

Real-type symmetry and |phi|=1 show S²=I and S is unitary/self-adjoint. No untruncated Eisenstein L2 expansion, completeness of its spectrum, or prime-cofactor positivity has been assumed. This is the scalar constant term plus the old full MS estimate.

## 4. Exact original-du norm, then legal extensions

For compact smooth r, T0 r is bounded on M and square integrable; Theta_r is compact in cusp height. The compact seed makes absolute unfolding against conjugate(T0 r) legal. Its zero ordinary mean gives

    ||T0 r||²=<Theta_r,T0 r>
      =integral_0^infinity h_r(y)conjugate(a0(T0 r)(y))dy/y²
      =||r||²_du+<r,Sr>_du
      =2||P_+r||²_du <=2||r||²_du,
    P_+=(I+S)/2.

The inner product is first-linear. The exact identity and its polarization define the unique bounded extension T0:L2(R,du)->L2(M). Its values have zero ordinary mean, a closed condition in L2(M). For r in S_exp, compact smooth cutoffs converge in BOTH S_exp and du. The previous Fréchet-continuous Theta/c maps and this bounded extension give the same L2 limit, so T0 r equals the previously defined Theta_r-c(r)1 on every actual principal test. No global du bound is assigned to c or Theta. The sharper global bound concerns the centered map only; the previous local overlap estimate was never the strongest centered consequence of old facilities.

There is also an exact closed-range qualification: T0 kills the S-minus subspace, and on the complete S-plus subspace it is sqrt(2) times an isometry. Hence Ran(T0) is closed. The previously checked Theta_P!=0 guarantees this plus subspace is nonzero, so the extended operator norm is EXACTLY sqrt(2), not only an upper. This does not assert that P_+ preserves S_exp, or that mu_-,c or the raw Poincare series are defined for every general L2 source. The general L2 map is the bounded extension only.

## 5. Actual output closure, including both degree directions

Let P_c be all physical405 principal relations, including every translate of the fixed P=e^(u/2)p. Old553 proves span{tau_a P:a in R} dense in physical L2, with NO RH or zero-simplicity premise. Their mu_+ and mu_- both vanish. Bounded T0 and density give the ACTUAL closure

    closure_L2(M) Theta(P_c) = closure Ran(T0) =: Hc.

The inclusion to the right uses Theta_p=T0p on P_c; the reverse uses the dense translated family and continuity. This is a closure statement on the supplied source image. It does not identify Hc with ALL mean-zero automorphic functions or import an unpaid continuous-spectrum completeness theorem. Unused cuspidal directions are not source coverage.

By the exact norm identity Hc is also Ran(T0) itself. Keeping the closure notation makes the cyclic-density step explicit; it does not leave a closed-range premise unpaid.

To retain the full two-degree information use the actual augmented source

    Phi(r)=(mu_-(r),mu_+(r),T0r) in C² directsum L2(M), r in S_exp.

This augmented map is Fréchet-continuous and need not be globallydu bounded. Its principal-image closure is {0}² directsum Hc. Any CLOSED linear Hilbert quotient containing all Phi(P_c) therefore kills the whole centered source information; only the two degree coordinates can remain in its source image. A bounded linear output A annihilating all principal images has the same consequence. There is no restriction to finite-rank, local or source-independent-in-index projections, and no uniform bound across a family A_j is needed; each individual continuous map already collapses the pole-free image.

The same scope extends to an individually continuous nonlinear readout F of Phi(S_exp), in its inherited Hilbert topology, with a Hausdorff target and exact coset invariance F(Phi(r+p))=F(Phi(r)) for EVERY r and p in P_c. For r,s having equal two degrees, choose principal p_n with T0p_n->T0(r-s). Then Phi(s+p_n)->Phi(r), so invariance and continuity imply F(Phi(s))=F(Phi(r)). No extension outside the actual source image is needed. For each index j this applies separately, even with no uniform modulus. If these readouts are claimed to approximate the full Weil form, their values at0 and537's nonzero pole-free probe coincide at each j, contradicting the two different target values. A Hilbert quotient Gram has normalization at0 automatically.

## 6. Strongest-old classification and exact escape scope

The closed-output result is an actual consequence AFTER the centered bound, not a conditional theorem substituted for it. Its short dependence is old545 full MS/constant term/residue plus elementary Mellin/unfolding -> bounded T0 -> old553 actual principal cyclic closure -> continuity/closedness. Old405 supplies both degrees and old537 the pole-free nonroot. The full classical target, including Gamma/contact, all proper powers and both poles, is the unchanged405/537 object. The new display of a stronger old implication is not a new independent arithmetic input, favorable signed core estimate or whole-Weil improvement. It does not pass any long-Goal completion gate.

The obstruction belongs to readouts of THIS frozen Theta carrier which are continuous in THIS Hilbert output topology and exactly invariant under ALL noncompact principal cosets. It does NOT impose that exact invariance on general Dprime approximants. Stronger output topologies, nonclosed/unbounded quotient maps, different primitive carriers, source information outside Phi, and genuine signed/indefinite mechanisms without this Hilbert continuity/descent premise remain legal. A signed scalar readout is included only when it satisfies the stated continuity and coset invariance on this same Phi; there is no general signed-method no-go. Old526's faithful stronger/nonuniform cofinal quotient is not reclassified as impossible.

C071 and the previous fixed-rank recipe remain spent/stopped. No C072/607, new primary body, numerical/scientific code or automatic rank/weight/source/audit/math sequel. ROOT final consumption awaits both current terminal independent records and their exact normalization/old-scope reconciliation.

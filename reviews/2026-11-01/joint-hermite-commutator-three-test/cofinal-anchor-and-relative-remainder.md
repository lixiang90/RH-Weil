# C070 anchor cut: exact physical-boundary channel; ratios OPEN

2026-11-01; `/root/bc72_fresh_review`, current mathematical proof cut, not an independent reviewer of the other cuts. Author terminal; independent review and ROOT consumption pending. SAME Goal1793085111 and shared ONE C070 responsibility. Only X_j=e^j,N_j=j^2 and the original591 real g, tau_(1/2)g,g' are considered. No source/web/PDF, numerical experiment, code, alternate scale or parameter is introduced. No STATE/cadence/Goal/Git change is made here.

**Result.** There is an exact actual lower channel for the commutator, in terms of a fixed physical-boundary Hankel operator applied to the full finite-Mobius/Hermite/Gram-inverse columns. It also gives a precise necessary condition for the proposed relative even-Taylor remainder to be small. Neither establishes a cofinal lower for the full g anchor or a three-test ratio limit. The arbitrary-common-gain question remains OPEN. No absolute upper is used to assert a ratio conclusion.

## 1. Coordinates and actual finite columns

Use the unitary log receiver coordinate y: H=L2(R,dy), U_a v(y)=v(y-a), A_r v=r*v. Here u/a are source/dilation variables, y is receiver position, and t is the Mellin/Fourier frequency. Multiplication by rhat is the same A_r after receiver Fourier transform; y and t must not be interchanged in the support argument.

Write P for the actual archimedean Sonin projection, M=Ran P. Its physical support condition is M subset H_+=L2([0,infinity),dy). Let H_- be multiplication by1_(y<0). The full actual finite-prime operators are

    B_j=product_(p<=e^j)(I-p^(-1/2)U_logp),
    G_j=(P B_j* B_j P)|M,
    Pi_j=B_j P G_j^(-1) P B_j*.

Every finite j uses its entire Gram inverse. No Neumann truncation or bare Euler multiplier is substituted. B_j is a finite sum of nonnegative receiver shifts, so B_j M subset H_+ and H_- Pi_j=0.

Let I_N:C^N->H have the actual ON log-Hermite columns h_n,0<=n<N. Thus E_N=I_N I_N*. Define actual finite-column maps into M,

    Xi_j=P B_j* I_(j^2),       T_j=G_j^(-1)Xi_j.

Then Pi_j I_(j^2)=B_j T_j. The explicit finite Mobius sum is

    Xi_(j,n)=P sum_(d|product_(p<=e^j)p) mu(d)/sqrt(d)
                         h_n(y+log d),       n<j^2.          (1)

This is a finite identity, not an infinite Mobius series or a limiting multiplier1/zeta. In particular it supplies no already-paid nonzero limit or uniform conditioning for Xi/T. The positive projection and each finite inverse make these columns legal, not quantitatively coercive.

## 2. Exact short-support physical-boundary factorization

**Lemma1.** Let r have source support in[-c,c], c<log2. Then the following actual finite-column identity holds:

    H_- [Pi_j,A_r] I_(j^2) = - L_r T_j,
    L_r:=H_- A_r P : M->H_-.                              (2)

**Proof.** In the finite squarefree expansion of B_j, its identity term is I. Every other term shifts to the right by log d>=log2. Every column v of T_j lies in M subset H_+. Thus A_r v has receiver support in[-c,infinity), and every nonidentity term U_logd A_r v has support in[log2-c,infinity). Consequently

    H_- B_j A_r v=H_- A_r v.

The source convolution commutes with every dilation shift, so A_r B_j=B_j A_r. Also H_- Pi_j A_r I_N=0. Substituting Pi_j I_N=B_j T_j gives(2). All operations are bounded for r in L1 and have finite-column HS meaning. No assertion that Pi_j I_N has low Mellin-frequency OUTPUT has been made. QED.

591 uses psi supported in(-1/16,1/16), so g and g' have support in[-b,b] with b=1/8. Put a=1/2. Both translates tau_(+/-a)g have support in[-a-b,a+b], where a+b=5/8<log2. Thus(2) applies to all reflected sources in the actual three tests.

For g even and g' odd, the reflection average leaves their diagonal HS norms unchanged. Therefore the genuine lower channels are

    B_j(g):=||L_g T_j||HS^2 <= C_j(g),
    B_j(g'):=||L_g' T_j||HS^2 <= C_j(g').                   (3)

These are lower bounds by ACTUAL quantities, not positive numerical/cofinal lower bounds. We have not proved B_j(g)>0 or that it controls a fixed fraction of C_j(g).

The fixed operator in(2) is especially explicit. For v supported in y>=0,

    (L_g v)(y)=int_0^b g(y-z)v(z) dz,    -b<y<0,

and it is zero outside[-b,0]. In other words only the physical interval[0,b] of the full G_j^(-1)Xi_j columns enters this channel. This is a compact fixed Hankel-type operator, not the full variable Sonin projection.

## 3. Actual derivative and translation channel comparisons

For any column v of T_j put F=A_g v. It is smooth, has support in[-b,infinity) and F(-b)=0. On(-b,0), F'=A_g' v. The fundamental theorem and Cauchy--Schwarz give

    int_(-b)^0 |F|^2 <= (b^2/2) int_(-b)^0 |F'|^2.

Summing the actual finite columns proves the unconditional comparison

    B_j(g') >= (2/b^2) B_j(g).                            (4)

It does NOT imply the same comparison between C_j(g') and C_j(g), since only B_j(g)<=C_j(g) is known.

For translated sources, source convolution gives A_(tau_a g)=U_a A_g. Because a>b,

    L_(tau_a g)T_j=0,
    ||L_(tau_-a g)T_j||HS^2
       =sum_(n<j^2) int_(-b)^a |(A_g T_(j,n))(z)|^2 dz.

This is the negative-receiver component of ONE of the two reflection terms only. Thus

    C_j(tau_a g) >= (1/2)||L_(tau_-a g)T_j||HS^2
                  >= (1/2) B_j(g).                       (5)

There is no claim that the positive-receiver component or the coherent full-column cross terms disappear. Equations4--5 are actual physical-support consequences, but they do not compare either target ratio to q1/q0 or1.

## 4. Full anchor written without hidden cancellation removal

To identify the missing lower precisely, define for any actual L1 source r

    Xi_j(r)=P B_j* A_r I_(j^2),
    K_j(r)=(P B_j* A_r B_j P)|M.

The identity Xi_j above has no delta source inserted into the physical Weil form; it was defined directly. The adjoint source is r^dagger(u)=conj(r(-u)), so A_r* A_r=A_(r^dagger*r). Direct finite-column expansion of Pi_j A_r I_N-A_r Pi_j I_N gives

    ||[Pi_j,A_r]I_N||HS^2
      = Tr_N(Xi_j(r)* G_j^(-1) Xi_j(r))
        -2 Re Tr_N(Xi_j(r)* G_j^(-1) K_j(r) G_j^(-1) Xi_j)
        +Tr_N(Xi_j* G_j^(-1) K_j(r^dagger*r) G_j^(-1) Xi_j).
                                                               (6)

All traces here are finite-column traces. The middle sign and its actual phase are retained. For r=g this is exactly C_j(g), since g is real even. Merely bounding the first/last captures below or bounding ||Xi_j|| does not provide a lower for their difference(6). A lower for Pi_j E_N also would not be a lower for the commutator.

The support channel(3) is a legitimate way around the cancellation in(6), but requires a real cofinal bound for

    H_- A_g P G_j^(-1) P sum_d mu(d)/sqrt(d)
                              U_(-logd) I_(j^2).          (7)

This is the explicit missing finite-Mobius/actual-Gram column quantity. Norm bounds on G_j^(-1), nonzero individual finite objects, or positivity of the full projection do not prevent its columns from approaching the kernel of the fixed boundary operator. We have not established the needed angle or its comparison with the full anchor.

## 5. Even Taylor remainder: a rigorous necessary boundary condition

This section does not assume a Taylor hierarchy. Let G(t)=rhat_g(t), G(0)=1, and m2=int u^2 g(u)du>0. Set lambda=a^2/m2 and

    R_e(t)=(cos(at)-1)G(t)-lambda(G(t)-1).

It is O(t^4) at0, but its commutator is generated by the ACTUAL compact source

    r_e=(tau_a g+tau_-a g)/2-(1+lambda)g,                  (8)

because the remaining constant lambda has zero commutator with Pi_j. That constant is only a bounded auxiliary identity operator, never a physical delta source evaluated by the Weil form.

On the physical output interval I=(-a-b,-b), the g and tau_a g convolution outputs of any v in M are zero. Only the tau_-a g term of(8) survives. Applying Lemma1 and shifting z=y+a gives

    ||[Pi_j,M_(R_e)] I_N||HS^2
       >= (1/4) sum_n int_(-b)^(a-b) |(A_g T_(j,n))(z)|^2 dz
       >= (1/4) B_j(g).                                  (9)

Here M_(R_e) is in Mellin coordinates, unitarily the operator A_(r_e)+lambda I in the physical coordinate; the norms agree. The interval comparison uses a>b and contains all(-b,0). No moving-core localization or limiting interchange is involved.

If C_j(g)>0, define beta_j=B_j(g)/C_j(g) in[0,1]. An actual even relative-Taylor assertion

    ||[Pi_j,M_(R_e)]I_N||HS=o(sqrt(C_j(g)))

would therefore REQUIRE beta_j->0. Taylor vanishing order and an absolute o(j) estimate do not prove this. If instead the physical boundary channel is a nonvanishing fraction of the anchor, that proposed relative-Taylor hierarchy cannot be valid. This is a necessary condition for that APPROACH, not a decision of the three-test problem: beta_j is presently unknown. No conditional model is being consumed as actual asymptotics.

## 6. What was attempted and what is NOT proved

The attempted anchor route uses the full Pi_j=B_j P G_j^(-1)P B_j*, its actual Mobius/Hermite columns(1), and the hard physical Sonin gap. It extracts the exact low-output channel(2), the source-specific lower form(3), comparisons4--5 and the concrete obstruction9 to assuming a small even remainder. It does not replace the source by an occupation covariance or an alternate receiver.

What remains unpaid is either a cofinal positive lower for the full anchor(6) together with relative coherent-error control, or a direct ratio comparison for the actual columns in(7). Even a lower for their total capture would not establish the local boundary angle or the middle cancellation in(6). The available fixed-eta Mellin-diagonal localization controls absolute mass, not these quantities. A moving-eta bound, if separately paid in a stronger old record, may improve the absolute upper; it still needs comparison to this actual anchor before any arbitrary-gain conclusion follows.

Accordingly none of the following is proved here: eventual C_j(g)>0; infinitely many zero denominators; a limit/limsup for C_j(tau_a g)/C_j(g) or C_j(g')/C_j(g); delta_j->0 or a positive lower for limsup delta_j. In particular this cut does NOT reject all finite common c_j>=0, impose a bounded-gain assumption, or pass the three-source necessary gate.

The full physical source/first-linear/reflection conventions are unchanged. q0,q1 remain the complete591 Weil values with Gamma/contact, every proper power and BOTH signed poles. These support lemmas alter no target coefficient and prove no full-complex mixed/D-prime convergence, principal/sections/mixed capacity or growing core/coupling/Xi result. Strongest classical old consequences and all Goal gates are unchanged. The shared C070 budget is not counted per file; ROOT must classify/consume exact proved partial statements and the OPEN main result once. No successor, scale, receiver, gain, source, numerical or engineering queue is supplied.

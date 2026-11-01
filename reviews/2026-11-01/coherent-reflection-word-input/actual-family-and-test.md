# Actual ordered reflection-word source: formation and test specification

2026-11-01; /root/reflection_word_formation. Terminal formation output for ROOT consumption, not a mathematics contract or final admission. Same G20261027/runtime1793085111 and original0c4f baseline. I read the current Goal/stopped C070/latest W/frontier and the actual560/591/594/602 and C070 root scopes. No new PDF, web/source search, numerical run, science code, STATE/board/library/cadence edit or successor is used here.

## 1. Frozen object and source roles

Use H=L2(R,dy), or its unitary Fourier model L2(R,dmu), dmu(t)=dt/(2pi). U_a v(y)=v(y-a). P is the original real-place Sonin orthogonal projection. For each actual prime p put

    q_p=p^(-1/2),  B_p=I-q_p U_logp,
    G_p=(P B_p*B_p P)|RanP,
    Pi_p=B_p P G_p^(-1)P B_p*,
    R_0=2P-I,  R_p=2Pi_p-I,  V_p=R_p R_0.

These are the exact one-prime objects of560, including their full Gram inverses. Since (1-q_p)^2 I<=G_p<=(1+q_p)^2 I on RanP, every inverse exists. R_0/R_p are selfadjoint unitaries; V_p is unitary, generally not selfadjoint. They do not require unknown zeta zeros or target positivity.

For integers j>=1 take F_j={p prime:p<=exp(j)}, list it as p_1<...<p_m, and freeze

    W_j=V_(p_1)V_(p_2)...V_(p_m).

The largest prime's factor acts first on a vector. This order is part of the proposal. W_j* reverses the factor order and adjoints each V_p; no factors are commuted or reordered. W_j denotes this unitary, NOT a Weil distribution.

For physical complex r=e^(u/2)f, initially r in C_c^infty(R), define

    A_r=integral r(a)U_a da,   D_j(r)=[W_j,A_r],
    check r(u)=r(-u),          r_dagger(u)=conjugate(r(-u)),
    C_j(r,s)=1/2 sum_(eps=id,check) Tr(D_j(eps s)*D_j(eps r)).       (1)

A_r is M_(rhat) in Fourier coordinates, not M_r. Reflection is complex-linear; dagger is antilinear and A_r*=A_(r_dagger). The first slot of C_j is linear. The word is not selfadjoint, so D_j(r)*=-[W_j*,A_(r_dagger)], not generally -[W_j,A_(r_dagger)]. The reflection average is retained exactly as specified; no parity argument deletes the odd diagonal.

## 2. Legal HS domain and explicit finite-level fees

560 pays the ordinary positive trace

    a(r)^2=||A_r P||HS^2=t_0(r)=integral |rhat(t)|^2 rho_0(t)dt

for every fixed-window original zero-extension Dlog source. Since r_dagger has Fourier transform conjugate(rhat), a(r_dagger)=a(r). Consequently ||[P,A_r]||HS<=2a(r). This uses two source-sandwiched HS operators, not a bare trace of P or P A_r.

Here is an explicit relative-factor estimate that does not replace the full inverse. Write Delta_p=Pi_p-P and, on the full space, extend G_p^(-1) by P on either side. The exact expansion is

    Delta_p=(B_p-I)P G_p^(-1)P B_p*
             +P(G_p^(-1)-I_RanP)P B_p*+P(B_p*-I).

The source A_r commutes with B_p and B_p*. Using ||G_p^(-1)||<=(1-q_p)^(-2) and ||G_p-I||<=2q_p+q_p^2 gives

    ||A_r Delta_p||HS <= h(q_p)a(r),
    h(q)=q+(3q+q^2)(1+q)/(1-q)^2=4q+O(q^2).                     (2)

The adjoint argument gives ||Delta_p A_r||HS<=h(q_p)a(r). The same operator-norm expansion and the difference-of-projections bound give

    ||Delta_p||op<=d_p:=min(1,h(q_p)).

Because V_p=I+2Delta_p R_0,

    [V_p,A_r]=2Delta_p[R_0,A_r]+2[Delta_p,A_r]R_0,
    ||[V_p,A_r]||HS <=[8d_p+4h(q_p)]a(r)<=12h(q_p)a(r).          (3)

All constants in (2)-(3) are actual finite-level upper fees, not estimates of the unknown cofinal ratio. A sharper bound would not by itself be a new whole-Weil result.

For prefixes L_k=V_(p_1)...V_(p_(k-1)) and suffixes S_k=V_(p_(k+1))...V_(p_m), the exact Leibniz formula is

    D_j(r)=sum_(k=1)^m E_(k,j)(r),
    E_(k,j)(r)=L_k[V_(p_k),A_r]S_k.                              (4)

All L_k/S_k are unitary, so (3) implies

    ||D_j(r)||HS<=12 H_j a(r),   H_j=sum_(p<=exp(j)) h(q_p),
    0<=C_j(r,r)<=144 H_j^2 [t_0(r)+t_0(check r)]/2.               (5)

This closes the actual HS domain; each trace in (1) is a product of two HS operators and is S1. It does NOT assert that A_r W_j A_r* has an ordinary trace: the full-space unitary has an identity part and no such trace is needed.

For support in a fixed I=(-L,L), use the original physical norm

    ||r||Dlog^2=(2pi)^(-1)integral [1+log(2+|t|)]|rhat(t)|^2dt.

The paid empty-base identity t_0=q_Gamma+<r,K_(0,I)r>, epsilon_0=2pi rho_0-Gamma in C0, gives a finite bound t_0(r)<=M_(0,I)||r||Dlog^2; for example M_(0,I)=C_Gamma+||epsilon_0||infty is legal when C_Gamma bounds |Gamma(t)|/[1+log(2+|t|)]. These are the actual560 quantities, not newly evaluated constants. Reflection preserves this norm. Thus (5) gives the fully stated finite-j Dlog fee 144H_j^2 M_(0,I). No derivative-free du bound or uniform-in-j/sources/growing-L bound is claimed. The estimate is for physical r; it must not be silently called the unweighted f-du norm. H_j is finite but grows; no whole signed-core consequence follows from its upper size.

The original compact core therefore extends (1) to each fixed I's zero-extension Dlog domain. Exponential strong sources outside a fixed compact window require their own summability fees; no new full S_exp or noncompact405 operator-domain claim is made here.

## 3. Exact mixed terms, actual kernel, and what coherence means

Expanding (1) using (4) gives

    C_j(r,s)=1/2 sum_eps sum_(k,l=1)^m
                 Tr(E_(l,j)(eps s)* E_(k,j)(eps r)).             (6)

The k!=l terms are not removed, bounded away by orthogonality, or replaced by a sum of one-prime energies. Their individual real parts can have either sign. Positivity belongs to the whole squared feature, not to each interference term.

There is also a legal positive-jump representation, which limits the interpretation of those cross terms. In the Fourier RKHS model of560, P/Pi_p have continuous evaluation kernels with L2 rows. Expand the finite word W_j-I into a finite linear sum of nonempty products of these projections. A product of length>=2 has the form Pi_a T Pi_b, with a,b possibly the empty base and T bounded, and continuous kernel <T k_(b,v),k_(a,t)>. A product of length1 uses its original projection kernel. Hence W_j-I has a continuous kernel K_j(t,v) with locally finite L2 rows. This is a finite-level statement; no infinite word or limiting kernel is asserted.

Since the identity part commutes with M_(rhat), the distribution kernel of D_j(r) is

    [rhat(v)-rhat(t)] K_j(t,v).

The already proved HS property identifies this with its L2 kernel. Thus the unaveraged mixed energy is exactly

    integral integral (rhat(v)-rhat(t))
       conjugate(shat(v)-shat(t)) |K_j(t,v)|^2 dmu(t)dmu(v).       (7)

Reflection averaging can be retained as a sum of two such integrals, or by using the reflected averaged nonnegative jump density. Only the symmetric part under t<->v contributes. This is NOT an independently signed Weil kernel: all prime interference survives inside the actual K_j and then |K_j|^2. No ordinary covariance representation with 0<=R_j<=Pi_(F_j) follows merely from (7).

In particular, because the old591 G=g_hat=|psi_hat|^2 is nonnegative,

    C_j(tau_a g,tau_a g)-C_j(g,g)>=0                            (8)

for every real a: in each jump integral the difference is 2G(t)G(v)[1-cos(a(t-v))]|K_j(t,v)|^2. This is a standard pointwise identity, not a cofinal gap. No strict calibration-independent lower ratio follows from nonnegativity alone.

There is an additional exact source-role reduction. Put B=B_p,

    C_p=P B*B P+(I-P),  Q_p=C_p^(-1),  D_0(r)=[P,A_r].

Then

    [C_p,A_r]=D_0 B*B P+P B*B D_0-D_0,
    [Pi_p,A_r]=B(D_0 Q_p P-P Q_p[C_p,A_r]Q_p P+P Q_p D_0)B*.      (9)

Thus the full D_j(r) is a source-independent bounded two-sided HS superoperator applied to the old D_0(r). It is a specific coherent receiver/postprocessing of an old source feature, not a newly supplied arithmetic primitive or principal cocycle. This factorization does not automatically put it in old591's occupation class or old C070's finite right-Hermite receiver class; establishing such a reduction would be a concrete old-premise admission result.

## 4. Actual nonempty initial control, not a cofinal anchor

At j=1 only p=2 occurs, so W_1=V_2. The paid560 one-prime density identity, compared with the empty base at R_n=2pi n/log2, gives

    rho_2(R_n)-rho_0(R_n)
       -> -(log2/pi) q_2/(1-q_2) !=0.

Therefore Pi_2!=P and W_1-I=2(Pi_2-P)R_0!=0. Its continuous kernel K_1 is nonzero. The actual591 G is real-analytic and nonconstant (G(0)=1 and G tends0 at infinity); each level set has measure0. If [W_1,M_G]=0, then (G(v)-G(t))K_1(t,v)=0 almost everywhere. The difference factor vanishes on a null subset of R2; continuity would force K_1=0, contradiction. Hence C_1(g,g)>0.

This is a genuine initial source/nonzero check using old paid ingredients and standard kernel facts. It does not show C_j(g,g)>0 eventually, provide a lower denominator, or establish any cofinal ratio. A nonempty first level cannot pay those responsibilities.

## 5. Frozen necessary test and admission boundary

Use EXACTLY old591's psi, g=psi*psi#, a=1/2, g', with its paid complete classical values

    q_0=Q_zeta(g)=Q_zeta(tau_a g)>0,   q_1=Q_zeta(g')>0.

These include full Gamma/contact, every proper power and both poles. For b_j=C_j(g,g)>0 define

    Delta_j=max(|C_j(tau_a g,tau_a g)/b_j-1|,
                |C_j(g',g')/b_j-q_1/q_0|).                     (10)

If one source-independent finite c_j>=0 makes c_j C_j match those three targets, then b_j must be positive eventually and Delta_j->0. No boundedness of the sequence c_j is assumed. Infinitely many zero denominators or a nonzero limsup in (10) rejects THIS frozen ordered word and every common positive calibration. Finite exceptional zeros do not suffice. Passing (10) would only pass three necessary tests, not the complete mixed/full-source limit.

Formation/HS/positive-jump identities and initial nonemptiness are standard consequences of paid560. New independent core input has not been shown. The only potentially new mathematical responsibility would be an actual cofinal comparison of THIS word's kernel/energy on the frozen tests, including its denominator and full prime cross terms. It is still open in this document. Neither (5), (8), (9), nor a missing application of an old theorem proves that responsibility is admissible; ROOT must reconcile the separate strongest-old/admission review first.

Old591 requires 0<=R<=Pi_(F_j) and its actual row/localization tail; this has not been established for the present positive jump kernel. Old594 is a prime-linear ordinary-trace selfadjoint pencil with integer word times; the present source commutator of a generally nonselfadjoint unitary product is a different typed object. Old602 controls the whole onebody compact error, not the coherent multi-prime row tail of (7). C070's finite Hermite right receiver remains stopped and its unknown comparison is not a budget for this word. Conversely, any genuine old exact decomposition dominating the present consequence must be consumed as old, not hidden by these category differences.

No favorable signed core, K_J/growing-L coupling, principal405 descent, full537 coverage, integral sections/multiplication/mixed RR or full Weil source identity is supplied. A PSD form on source pairs is not automatically a positive-type distribution on their convolution differences: (8) already shows that stationarity is a separate issue. A full all-compact-source limit to the Weil form would suffice to pass positivity to the limit, but it is not proved by a three-test pass or by this construction. The strongest old fixed17/16, finite9/8E448, same605 one-head/all-complement completion and whole4/5 negative-inertia UPPER remain unchanged.

Recommendation: **actual family formed, native domain/HS/finite fees closed; cofinal comparison and independent core consequence OPEN, no automatic mathematical admission**. Do not label this document a new theorem, completed method boundary, new round, C071/607 or Goal completion. No prime-order, gain, receiver, basis, source, numerical, chapter or paper queue follows from it. If strongest-old comparison leaves no genuinely new actual responsibility, settle NONE; otherwise any subsequent single proof responsibility requires a separate ROOT admission and stop rule.

# C018: all-prime carry and the projected signed dual pole

2026-10-14, independent prime/pole audit by /root/c017_prime_pole. Only this
file is owned by this agent. No STATE, cadence, contract, root note or Git
mutation is made. Source-interface and rank-two algebra are not counted as
new mathematical iterations or macro forcing consequences.

## Recovery, actual source and scope

Recovered AGENTS, README, STATE, then ran research_state.py check and show;
the check passed structurally, not mathematically. Read the current Goal,
macro frontier, C018, D20261014S, and the original cycle-11 source-entry
derivation. At entry STATE named latest 546, cadence 0/8 and C018 ready;
Git was clean at HEAD 3cebe129e1785eeaaff8f76b82152e1cbe334264. The child
get_goal returned null, which is not evidence of the root Goal's runtime.
The Goal's fixed baseline remains 0c4f3a3 / all results <=538. The prior
016/017/023/028/069/080/167/539/543/546 scopes are retained; a finite-source
constraint is not a free prime norm bound, and a component counterexample
does not make whole Q negative.

Freeze every integer N>=4, M=N-1 and L=(log N)/2. The unitary coordinate
transport is

    x=exp(u+L), F(x)=f(log x-L), du=dx/x,
    H_N=L2((1,N),dx/x).

It preserves the original complex Lebesgue-u norm. Every source is
zero-extended from I_L=(-L,L), and its form domain remains the actual Dlog
domain in u, with Gamma(t)=Re psi(1/4+it/2)-log pi=2 theta'(t). No weighted
arithmetic replacement norm, parity condition or pole moment condition is
introduced.

Set J_n=(n,n+1), ell_n=log((n+1)/n), e_n=1_Jn/sqrt(ell_n). The original-norm
orthogonal projections are

    (PF)|_Jn=ell_n^(-1) integral_Jn F(x)dx/x, R=I-P.

Thus RF has zero dx/x-weighted mean on each whole cell, not zero Lebesgue-dx
mean. For fixed N, each e_n becomes a compactly supported BV step source in
u and lies in Dlog (its Fourier transform is O(1/|t|)). P has finite rank,
so P and R preserve Dlog for that fixed N. No uniform-N Dlog multiplier norm
is inferred. The prime operators below are bounded L2 operators, so their
mixed terms need no extra Gamma-domain assumption on T_qF.

## 1. Exact full carry, the adjoint, and the one-sided triangle

For every integer 2<=q<N, define the actual partial translations

    (T_qF)(x)=1_(qx<N)F(qx),
    (T_q*F)(x)=1_(x>q)F(x/q).

Both are L2 contractions, not unitaries on this finite interval. Their
adjoint relation is exact because dx/x=dy/y under y=qx. All prime powers
with coefficient w_q=Lambda(q)/sqrt(q), including proper powers, are kept.

Write F_n(v)=F(n+v), 0<v<1. If r=floor(qv), w=qv-r, then
qx=qn+r+w, 0<=r<q. The complete correlation is

    <F,T_qF>
      =sum_n sum_(0<=r<q, qn+r<=M)
         integral_(r/q)^((r+1)/q)
           conjugate(F_n(v)) F_(qn+r)(qv-r) dv/(n+v).

After w=qv-r, dv/(n+v)=dw/(qn+r+w). Every carry r, not just r=0,
is required. The integer boundary N truncates the final output at an
integer endpoint, so all retained target cells are whole cells; there is
no missing fractional target-cell ledger. Profiles in distinct cells may
be unrelated complex functions.

For RF, change variables in a whole output cell:

    integral_Jn T_q(RF)(x)dx/x
      =integral_((qn,q(n+1)) intersect (1,N)) RF(y)dy/y=0.

The right side is a union of complete integer cells, even when the output
cell is cut at N/q. Consequently, on all of H_N,

    P T_q R=0, T_q R=R T_q R, R T_q* P=0.                 (1)

The reverse blocks are not zero. For example, N>=4 and q=2 give

    T_2 e_2=1_(1,3/2)/sqrt(ell_2),
    ||R T_2 e_2||^2=1-ell_2/ell_1>0.

Thus R T_2 P and its adjoint P T_2* R are genuinely nonzero in the original
domain. This is an explicit legitimate step-source counterexample to a
two-sided block-diagonal claim. The mean matrix also keeps every carry:

    <e_n,P T_q P e_m>=sqrt(ell_m/ell_n)
    if qn<=m<=min(q(n+1)-1,M), and is zero otherwise.

It is not the sparse exact-divisor matrix from the thin C017 comb.

## 2. The actual mixed Weil form

Let

    B_N=sum_(q<N) w_q(T_q+T_q*),
    a_+(x)=N^(-1/4)sqrt(x), a_-(x)=N^(1/4)x^(-1/2),
    A_+(F)=integral F a_+ dx/x, A_-(F)=integral F a_- dx/x,
    D_pole=|a_+><a_-|+|a_-><a_+|.

The complete actual form is q_Gamma(F)-<F,B_NF>+<F,D_pole F>, and the pole
is exactly 2 Re(A_+ conjugate(A_-)). Use the inner product antilinear in
its first argument. For G=PG and H=RH, both in Dlog, the exact mixed form is

    q_Q(H,G)
      =q_Gamma(H,G)-sum_(q<N) w_q <H,T_qG>
       +conjugate(A_+(H))A_-(G)+conjugate(A_-(H))A_+(G).   (2)

Here (1) removed only R T_q* P; it did not remove R T_q P. Gamma's Fourier
pairing remains the full actual multiplier on the original source, and
its constant Gamma_0 pairing vanishes only because <H,G>=0. In particular

    Q(G+H)=Q(G)+Q(H)+2 Re q_Q(H,G).

No Gamma, reverse-prime or dual-pole mixed term is declared zero or paid by
the forward triangular identity. Whether the three actual components
cancel is an additional whole-source question.

## 3. Exact detail projections of the two actual pole vectors

Define d_n=sqrt(n+1)-sqrt(n). The weighted means on J_n are

    P(sqrt x)|_Jn=2d_n/ell_n,
    P(x^(-1/2))|_Jn=2d_n/[sqrt(n(n+1))ell_n].

Put

    v_n=1-4d_n^2/ell_n,
    k_n=ell_n-4d_n^2/[sqrt(n(n+1))ell_n],
    U_M=sum_(n<=M) v_n,
    V_M=sum_(n<=M) v_n/[n(n+1)],
    kappa_M=sum_(n<=M) k_n.

Direct weighted integrations, with the original dx/x norm, give

    ||R a_+||^2=N^(-1/2) U_M,
    ||R a_-||^2=N^(1/2) V_M,
    <R a_+,R a_->=kappa_M.                              (3)

In particular the second per-cell squared residual is exactly the first
one divided by n(n+1); it is not an estimate. v_n>0 by strict weighted
Cauchy-Schwarz. k_n<0 because sqrt(x) increases and x^(-1/2) decreases:
their residual covariance is

    (2ell_n)^(-1) integral_(Jn x Jn)
       (sqrt x-sqrt y)(x^(-1/2)-y^(-1/2)) dx dy/(xy)<0.

This sign also follows from

    k_n=ell_n-16 sinh^2(ell_n/4)/ell_n.

Weighted variance is at most one quarter of the squared range times the
cell mass. Thus

    0<v_n<=ell_n d_n^2/4<=1/(16n^2),
    0<v_n/[n(n+1)]<=1/(16n^4).

Using elementary sum/integral bounds, uniformly for every N>=4,

    U_M<=1/8, V_M<=1/12.                                (4)

No raw norm has been used as a lower cost for its projected vector.
Indeed ||a_+||^2=||a_-||^2=sqrt N-N^(-1/2), while (3) has very different
scales and must be combined before charging the signed operator.

## 4. Exact asymptotics and the uniformly bounded signed detail operator

Elementary Taylor expansions at ell_n=log(1+1/n) give

    v_n=1/(48n^2)+O(n^(-3)),
    v_n/[n(n+1)]=1/(48n^4)+O(n^(-5)),
    k_n=-1/(48n^3)+O(n^(-4)).

Therefore the positive constants U_infty=sum_n v_n and
V_infty=sum_n v_n/[n(n+1)] and negative kappa_infty=sum_n k_n converge.
For M=N-1, tail integral comparisons give

    U_M=U_infty-1/(48N)+O(N^(-2)),
    V_M=V_infty-1/(144N^3)+O(N^(-4)),
    kappa_M=kappa_infty+1/(96N^2)+O(N^(-3)).

Consequently ||R a_+||^2~U_infty N^(-1/2) and
||R a_-||^2~V_infty N^(1/2); individually the two norms have powers
N^(-1/4) and N^(1/4). Their product, not their sum or the two unprojected
norms, controls the complete signed detail pairing.

On R H_N the exact compressed pole is

    R D_pole R=|R a_+><R a_-|+|R a_-><R a_+|.

Its two nonzero eigenvalues are

    lambda_+=kappa_M+sqrt(U_M V_M)>0,
    lambda_-=kappa_M-sqrt(U_M V_M)<0.                    (5)

The strict inequalities hold because the two residual functions cannot
be proportional even on one positive-width cell: a reciprocal square-root
cannot be an affine function of a square-root on an interval. Their
eigenvectors R a_+/||R a_+|| +/- R a_-/||R a_-|| are piecewise smooth BV
sources in the actual Dlog domain. In particular the negative pole is
still present; no parity or moment condition removed it.

The exact norm and lower cost are

    ||R D_pole R||=sqrt(U_M V_M)-kappa_M,
    R D_pole R >= -[sqrt(U_M V_M)-kappa_M] I.             (6)

By Cauchy-Schwarz and (4),

    sqrt(U_M V_M)-kappa_M<=2sqrt(U_M V_M)<=1/sqrt(24).   (7)

This uniform O(1) actual signed detail fee is proved for all integers N>=4
and every complex detail source. It has the finite nonzero limit
sqrt(U_infty V_infty)-kappa_infty. Inferring a growth cost from the growing
norm of R a_- alone, or from two raw C/S norms, would be incorrect.

## 5. The pole mixed block has genuine growth, despite (7)

Write alpha=R a_+, beta=R a_-, c=P a_+, d=P a_-. Exact orthogonal splitting
gives

    ||c||^2=N^(-1/2)(N-1-U_M),
    ||d||^2=N^(1/2)(1-1/N-V_M),
    <c,d>=log N-kappa_M,
    K_N:=R D_pole P=|alpha><d|+|beta><c|.               (8)

This uses the same signed pole, not a sum of unrelated raw estimates.
For the actual normalized head source c/||c||,

    K_N c/||c||=beta ||c||
                 +alpha (log N-kappa_M)/||c||.

The first summand has norm sqrt[V_M(N-1-U_M)]~sqrt(N V_infty); the second
has norm O(log N/sqrt N). An upper bound from (8) is the first norm plus
sqrt[U_M(1-1/N-V_M)], whose added term is O(1). Thus

    ||R D_pole P||/sqrt N -> sqrt(V_infty)>0.            (9)

The lower test source is a step head source in the original Dlog, so (9)
is not an inverse-domain or finite-matrix artifact. For an optional exact
check, let A=||alpha||^2, B=||beta||^2, a=||c||^2, b=||d||^2,
k=kappa_M and D=log N-k. The two nonzero squared singular values of K_N
are the roots of

    z^2-tau z+Delta=0,
    tau=A b+B a+2kD,
    Delta=(AB-k^2)(ab-D^2).

These are Gram identities on the actual source; no numerical diagonalization
is used. tau/N->V_infty and Delta/N^2->0 reproduce (9).

Equation (9) concerns the pole component of R Q P only. It neither proves
that the whole mixed Weil form has this norm nor excludes cancellation
with actual Gamma/prime mixed terms in (2). Nor does it turn the remaining
whole-source problem into a pole-norm problem: the complete pole has one
negative direction, and the old count argument may pay it by rank one.

## 6. Consumption and the remaining core responsibility

The source/carry identities, one-sided triangle and actual projected pole
fee are now explicit for all N, all strict prime powers and all original
complex profiles. The detail pole can be charged by the fixed constant
(7), while a claim of uniform mixed-pole norm is disproved by (9). These
are source-interface clarifications and rank-two computations. They do
not independently pay a new arithmetic/Gamma relative theorem or whole
count consequence, and are not registered here as a new research round.

Old 539 already handles finite L2-continuous constraints at each fixed N;
the M weighted cell means are such constraints. Its high-frequency carrier
argument therefore rules out the proposed free unweighted detail-prime
O(log N) norm shortcut. That old result is consumed, not reproved or
recounted. Gamma on those carriers grows, so neither it nor (9) disproves
the distinct signed relative candidate

    <F,B_NF> <= eta J_Gamma(F)+C log N ||F||^2,
    F in R H_N intersect Dlog, fixed eta<1 and absolute C.

The count route previously needs only one negative-pole rank, so improving
its operator-norm fee to (7) does not by itself improve that count route.
The new candidate, reverse-prime/Gamma joint terms, actual core capture
after their fees, and ordinary zeta/Xi identification remain open. The
unique next useful action is the root's signed Gamma-relative fee gate,
with all source and error terms from (2), rather than another positive
Gram label, pole omission, or finite matrix expansion.

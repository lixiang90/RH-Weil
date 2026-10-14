# C017 independent strict-prime compression and signed dual-pole audit

2026-10-14. Scope: the frozen arithmetic comb, every independent complex cell
profile, the original Lebesgue norm, all strict prime powers, and the complete
dual-pole pairing. This audit does not prove the whole Gamma gate, whole-Weil
positivity, coverage of the growth core, or the macro Goal.

## Recovery and source authority

Read AGENTS.md, goals/README.md and goals/STATE.json; ran research_state.py check
and then show. The check passed structurally and expressly does not certify
mathematics. Recovered Goal G20261014, its fixed baseline
0c4f3a3eb609bb1d9564138fa4a35701f05605f2 / all results <=538, the macro frontier,
C017 and decision D20261014R. At this audit's start Git was clean, HEAD
25d856b7b15f1b7dec6fb971c53f15d7f5ec174b. The child get_goal result was null;
the root runtime must be observed by the root, not inferred from this child.
The recovered cadence was 3/8, latest mathematical note 545. This child does
not change STATE, cadence, contracts or Git and does not count an iteration.

Needed originals read: 016/017 exact prime-graph and Euler identities, 023
Gamma-bottom/core scope, 028 negative-trace/core scope, 069/080 reciprocal
incidence and its unpaid RH-strength norm, 167 divisor-diagonal versus mixed
geometry scope, and 543 actual normalization and the strongest old scalar
budget comparison. The self-contained Chebyshev proof was recovered from
reviews/2026-10-14/c013-moments/growing-measure-derivation.md, section 4.
No unknown zeta-zero information or PNT is used below. All arithmetic lemmas
below are proved here; no external theorem is invoked without its proof.

The actual normalization is

    Gamma(t)=Re psi(1/4+it/2)-log pi=2 theta'(t),
    Q_L(f)=q_Gamma(f)-2 sum_(q<N) Lambda(q)/sqrt(q) Re C_logq(f)
           +2 Re(A_+(f) conjugate(A_-(f))),
    C_a(f)=integral conjugate(f(u)) f(u+a) du,
    A_+(f)=integral f(u)e^(u/2)du,
    A_-(f)=integral f(u)e^(-u/2)du.

The sum is over every integer q with Lambda(q)>0, including proper prime
powers. The source is zero-extended from I_L=(-L,L), its physical norm is
Lebesgue L2, and Q's form domain is the original complex Dlog domain. The
prime and pole calculations below hold on all L2 sources supported on the
comb; they restrict to Dlog without changing their norms or quantifiers.

## 1. Spacing proves the exact compression, with no near overlaps

Freeze an arbitrary integer N>=4, M=N-1, L=(log N)/2 and

    h=1/[8N(log(2N))^2],
    x_n=-L+log n,
    I_n=(x_n,x_n+h), 1<=n<=M,
    Omega_N=union_(n=1)^M I_n.

Set d_N=log(N/(N-1)). Since log(1+x)>=x/(1+x),

    d_N>=1/N>h.

The gap between consecutive logarithmic integer centers with indices <=M
is at least log(M/(M-1))>d_N. The first cell starts at -L and is open; the
last cell ends below L because L-x_M=d_N>h. Thus all cells are disjoint and
contained in the original open I_L. Endpoints are null sets, not new sources.

For any strict q<N with Lambda(q)>0, and any n,m<=M, an overlap between
I_n+log q and I_m requires |log(qn/m)|<h. If qn!=m and qn<=M, two distinct
integers <=M have logarithmic separation at least log(M/(M-1))>d_N. If qn>M,
then qn>=M+1=N and m<=M, giving log(qn/m)>=d_N. Hence no such overlap occurs.
When m=qn<=M the two cells agree exactly, including the same profile
coordinate v in (0,h). This also audits the potentially dangerous n,q with
qn as large as M^2: those shifted centers lie above the top cell and cannot
produce a small gap. There is no omitted near-integer or partial overlap.

Define the unitary identification with the unchanged physical norm:

    U: directsum_(n=1)^M L2(0,h) -> L2(Omega_N),
    (UF)(x_n+v)=F_n(v),
    ||UF||^2=sum_n ||F_n||^2.

Translation in the logarithmic coordinate has Jacobian one. In particular
there is no n, q, or exp(u) weight in this source norm. Exact compression gives

    C_logq(UF)=sum_(n<=M/q) integral_0^h conjugate(F_n(v)) F_qn(v)dv,

and, with the real symmetric matrix

    B_(n,m)=Lambda(n/m)/sqrt(n/m) if m|n and n>m,
    B_(m,n)=B_(n,m), B_(n,n)=0,

the actual prime term is exactly -<F,(B tensor I)F>. This is an infinite
dimensional source-class identity, not a finite coefficient ansatz or a
finite matrix test. Every F_n may have an unrelated complex profile.

## 2. A self-contained quantitative logarithmic Mertens ledger

Prime factorization gives, for every integer n>=1,

    sum_(d|n) Lambda(d)=log n.

For example n=4 needs both q=2 and q=4; omitting proper powers breaks this
identity. Summing it over n<=K yields the exact factorial identity

    log(K!)=sum_(q<=K) Lambda(q) floor(K/q), K>=1.

The already paid elementary Chebyshev bound can be verified as follows.
Each prime-power valuation of binomial(2j,j) is a sum of 0/1 carries. In
particular all prime powers q in (j,2j] occur in those carries, and so

    psi(2j)-psi(j)<=log binomial(2j,j)<=2j log 2.

Sum this inequality at dyadic j, then enlarge any real x>=1 to its next
dyadic integer. It gives

    psi(x)=sum_(q<=x) Lambda(q)<=C_psi x, C_psi=4 log 2.

This is a restored elementary old tool; no new arithmetic theorem is claimed.
Let R(y)=sum_(q<=y) Lambda(q)/q for real y>=1 and K=floor(y). By the factorial
identity,

    R(K)=log(K!)/K + K^(-1) sum_(q<=K) Lambda(q){K/q}.

The second term is between 0 and C_psi. Increasing-integral comparison gives
log(K!)>=K log K-K+1, while log(K!)<=K log K. Since K>=y/2, including the
entire range 1<=y<2, we obtain the uniform bound

    log y-C_0 <= R(y) <= log y+C_psi,
    C_0=1+log 2.                                           (1)

No eventual threshold, hidden o(log y), or unknown-zero estimate occurs.

## 3. Weighted Schur is in the original norm; log M is leading sharp

Use the positive auxiliary Schur vector v_n=n^(-1/2). This is a proof device,
not a replacement Hilbert norm. Its exact weighted row is

    r_n=v_n^(-1) sum_m B_(n,m)v_m
       =sum_(q|n,q>=2) Lambda(q)
        +sum_(q<=M/n) Lambda(q)/q
       =log n+R(M/n).

Thus, by (1), uniformly for every n<=M,

    log M-C_0 <= r_n <= log M+C_psi.                       (2)

For a=(||F_1||,...,||F_M||), positivity of B and
2a_i a_j <= (v_j/v_i)a_i^2+(v_i/v_j)a_j^2 prove

    |<F,(B tensor I)F>| <= sum_n r_n ||F_n||^2
                        <=(log M+C_psi)||F||^2.             (3)

This is the ordinary L2 / ordinary ell2 operator bound, for all independent
complex profiles. The prime contribution is consequently bounded below by
-(log M+C_psi)||f||^2 on the frozen comb.

The leading log M fee cannot be lowered to O(1) on the full comb source class.
Let H_M=sum_(n=1)^M 1/n, choose any g in Cc-infinity(0,h) with ||g||=1, and set

    F_n(v)=g(v)/sqrt(n H_M).

This is an actual normalized smooth compact source in the original Weil
domain. Formula (2), averaged with weights 1/(n H_M), gives

    log M-C_0 <= <F,(B tensor I)F> <= log M+C_psi.            (4)

Equivalently ||B||=log M+O(1), with the displayed absolute constants. One
could also invoke a Perron vector, but (4) proves the necessary lower fee
without that tool. Its actual whole-line Fourier transform is

    hat f(t)=hat g(t) exp(itL)
             [sum_(n<=M) n^(-1/2-it)]/sqrt(H_M).             (5)

Gamma must be charged against (5), including every cross term and all
frequencies. A list of isolated-cell lower bounds is not yet a whole-Gamma
proof. The large prime Rayleigh value in (4) does not make whole Q negative.
This is precisely the legal source on which to test an alleged joint gate.

## 4. Complete signed dual pole and exact eigenvalues

Let a(u)=1_Omega(u)e^(u/2), b(u)=1_Omega(u)e^(-u/2), considered in the original
Lebesgue L2(Omega). The dual-pole form is the self-adjoint rank-two operator

    T_pole=|a><b|+|b><a|,
    <f,T_pole f>=2 Re(A_+(f) conjugate(A_-(f))).

This is exactly 2|C|^2-2|S_pole|^2 with C=(A_++A_-)/2 and
S_pole=(A_+-A_-)/2. The cancellation is retained before taking a norm.
Exact integrations over every cell give

    ||a||^2=N^(-1/2)(e^h-1) M(M+1)/2,
    ||b||^2=N^(1/2)(1-e^(-h)) H_M,
    <a,b>=Mh.

Set

    P_N=sqrt[(e^h-1)(1-e^(-h)) M(M+1) H_M/2],
    p_N=Mh.

The two nonzero eigenvalues are exactly

    p_N+P_N, p_N-P_N.                                     (6)

Indeed a/||a|| +/- b/||b|| are the two eigenvectors. Cauchy-Schwarz gives
P_N>=p_N, strictly for this positive-width comb because exp(u) is nonconstant
on Omega. Thus the signed pole is not positive; it has one genuine negative
direction. These explicit eigenvectors lie in Dlog: each is compactly
supported and piecewise smooth with finitely many jumps, hence its Fourier
transform is O(1/|t|) and log(2+|t|)|hat f|^2 is integrable. This validates the
negative direction in the actual form domain without making a claim about Q.

In particular the requested full-norm and the sharper lower-fee statements
are both valid:

    ||T_pole||=p_N+P_N <= 2P_N,
    <f,T_pole f> >= -(P_N-p_N)||f||^2.                      (7)

Since sqrt[(e^h-1)(1-e^(-h))]=2 sinh(h/2)<=h exp(h/2), h<=1, and
H_M<=1+log M,

    P_N<=e^(1/2) hM sqrt(1+log M),
    ||T_pole||<=2 e^(1/2) hM sqrt(1+log M).                 (8)

The frozen h implies hM<=1/[8(log(2N))^2], so this full signed fee is
O((log N)^(-3/2)), uniformly as N grows. Its exact formula, not an exponential
bound inherited from the enclosing interval, is the appropriate ledger.
Independently bounding |C| and |S_pole| discards cancellation and may charge
the much larger positive/negative squares; rank two alone does not justify
discarding a pole. No pole condition or parity restriction was imposed here.

## 5. What this audit pays and does not pay

Paid for all integers N>=4 and all independent complex profiles: exact strict
all-prime-power compression with no near-overlap error, unchanged physical
norm, quantitative Schur prime fee log M+C_psi, the actual smooth near-sharp
family, complete signed dual-pole norm/lower fee and legitimate pole domain.
All these proofs are independent of unknown zeta positions. Gamma's actual
factor is recorded correctly but its self/cross estimates are not certified
by this prime/pole audit.

The restoration of Lambda*1=log, factorial/Chebyshev/Mertens and Schur is an
old-tool input, not by itself a new macro forcing consequence. Old 080's
incidence construction gives a positive finite observable but its special
arithmetic uniform norm remains RH-strength. Old 167 explicitly retains
mixed and continuum/Gamma cross geometry. Neither theorem can be consumed
as an automatic payment of this whole-Gamma gate. Conversely old 016/017
exact decompositions are available and must be included in the strongest-old
comparison; this audit does not certify global novelty by comparing only
against their crude independent operator norms. Old 028/543 whole-source
count/trace budgets remain distinct from strict positivity of a comb subclass.

The immediate decisive input is a proof or counterexample for the original
Gamma self/crosscell form on all these independent profiles, followed by
the joint lower bound using (3) and the sharper fee (7). If that is paid, it
still proves only an Omega_N source-class consequence. Here |Omega_N|=Mh
tends to zero. For each fixed [-R,R], its cells have n=O_R(sqrt(N)); hence the
intersection measure is O_R(sqrt(N)h) tending to zero. Absolute continuity of
the integral then makes the projection of every fixed compact L2 source onto
Omega_N tend to zero. There is no whole-source or growth-core exhaustion,
and no free passage to RH or the macro Goal. Coverage, complement coupling,
signed core and ordinary zeta/Xi identification remain unpaid.

Stopping/re-entry: if the Gamma joint gate is only old uncertainty restored,
or remains unknown, the root's contract rules determine zero-round entry
stop; no smaller h or larger N is proposed to manufacture progress. New
whole-Gamma/arithmetic joint information or an actual core-coverage mechanism
would change that choice. The unique next action remains the root's all-profile
Gamma gate and strongest-old comparison, not a finite matrix experiment.

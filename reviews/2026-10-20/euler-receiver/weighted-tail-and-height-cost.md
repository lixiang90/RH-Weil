# Actual Euler weighted receiver: original domain, complete tail and finite-height cost

2026-10-20, producer proof for the once-only cycle14 admission. This file does not
settle a contract/cadence and does not modify STATE or Git. Recovered same G20261014,
frozen 0c4f/≤538 baseline, C034/571, cycle14, latest D20261020N and macro frontier.
Strongest actual-zeta whole consequence remains 542+555→557, leading 4/5; no result
below is a statement about the actual Sonin error or all Weil sources.

## 1. Concrete input, test, and net consequence

Input: the actual finite Euler polynomial and the already paid complete causal inverse,
acting on the real restricted receiver (571 (9)), with T fixed to complete Γ(R).
The test is exact coherent coefficient grouping followed by an original-domain
finite-height estimate which includes every coefficient beyond the cutoff.

There are two different outcomes. Finite Euler differences do **not** make the
ordinary-gap infinite MV cost Σ n||a_n||² finite, already for one prime. This does
not exclude the actual-gap MV theorem: BMS/Matveev makes its cost finite for every
first-fixed F. Moreover, there is a genuinely synchronous cofinal estimate with
the full |b|² weight and no m² normalization: for the sufficient range θ>2e,

    average |b_F(R)|² ||L_-D_F*H_(Γ(R))w_R||² = O_θ(L^4),
    F={p<e^(2L)}, R∈[exp(θe^L), exp(θe^L)+exp(βθe^L)],          (A)

for a suitable fixed β∈(0,1). Its normalized average divided by ||w_R||² tends
to zero. The θ>2e restriction belongs to the certificate proved here, not to
the actual cost. It lies outside the dangerous θ≤1 core and outside the minimum
old θ>1 favorable-frequency threshold. It does not pay the Sonin k_R/full-inverse
transport, the negative part of the model residual, or the all-source Weil budget.

## 2. Exact grouped coefficients and the original domain

Use H=L²(R,dy), U_a f(y)=f(y−a), P_T=1_(0,T), L_-=1_(-∞,0),

    B_F=∏_(p∈F)(I−p^(-1/2)U_(log p)), D_F=B_F^(-1),
    b_F(R)=∏_(p∈F)(1−p^(-1/2)e^(-iRlog p)),
    w_(R,T)=e^(iRy)1_(0,T)/√(2π), v_(R,T)=L_-D_F*P_Tw_(R,T).

Here F is initially any finite nonempty set of ordinary primes, T>0. Let
N_F denote the F-smooth positive integers, rad(n) their squarefree radical,
x_n=log n, ω(n) the number of its distinct prime divisors. In the genuine
L²((0,∞),dt) receiver coordinate y=−t, 571 gives

    √(2π)e^(iRt)v_(R,T)(−t)
       =Σ_(n∈N_F) n^(-1/2)e^(iRx_n)1_(t<x_n<t+T).

Multiplication by the finite scalar polynomial overline(b_F(R)), followed by
grouping the exact collisions n·d=N, gives the identity

    √(2π)e^(iRt) overline(b_F(R))v_(R,T)(−t)
          =Σ_(N∈N_F) a_(N,T)(t)e^(iRx_N),                    (1)
    a_(N,T)(t)=N^(-1/2) Σ_(d|rad(N)) μ(d)
                                1_(t<log(N/d)<t+T), t>0.    (2)

The d coefficients are μ(d), not μ(d)/√d: the latter weight has already combined
with (N/d)^(-1/2) into N^(-1/2). The n=1 coefficient is identically zero. Multiplying
by b instead of overline(b) would produce a different reindexing; modulus equality
alone would not validate (2).

Every interval in (2) has length at most T, and lies inside (0,x_N). Consequently,

    ||a_(N,T)||₂ ≤ N^(-1/2) 2^ω(N) √min(T,x_N),
    ||a_(N,T)||₂² ≤ N^(-1)4^ω(N) min(T,x_N).                  (3)

For each fixed finite F,

    Σ_(N∈N_F) N^(-1/2)2^ω(N)
      =Z_(2,F)(1/2)=∏_(p∈F)(1+p^(-1/2))/(1−p^(-1/2))<∞.    (4)

Thus (1) converges absolutely in the **original** L²(t>0) norm, uniformly in R for
fixed T. It is not a Mellin/Fourier transformed or freely chosen low input. The
tail after exact grouping is the tail of this same physical receiver; it need
not equal the tail of the unweighted D series times overline(b).
In particular the cutoff log N≤A is imposed **after** the finite Euler
convolution and exact collision grouping. Truncating D first at log n≤A and
then multiplying by overline(b) instead creates frequencies up to
A+log(rad(F)); that is a different truncation and cannot use (14) or (17).
All reorderings are first made for a fixed finite F; only the resulting
exact identities and proved uniform estimates are then used cofinally.

## 3. A cheap negative test, and its legal actual-gap repair

For F={p}, a=log p and N=p^k, k≥1,

    a_(p^k,T)(t)=p^(-k/2)
      [1_(t<ka<t+T)−1_(t<(k−1)a<t+T)].                       (5)

When k is sufficiently large that neither interval is clipped by t=0, their
symmetric difference has length 2min(T,a)>0. Hence

    Σ_(N∈N_F) N||a_(N,T)||₂²=∞                              (6)

already for the one-prime system. Formula (6) only rules out the convenient
ordinary spacing δ_(log N)≥1/(2N) in an infinite Corollary 3 application. The
actual single-prime gaps are all log p; indeed Σ||a_(p^k,T)||² is finite. A claimed
obstruction to **every** infinite MV application would be false.

More generally fix F with d primes. The already paid BMS/Matveev theorem gives,
for distinct F-smooth m,n with |log(m/n)|≤1, a polynomial lower bound in log n.
One explicit valid choice is

    M_D(F)=1.4·30^(d+3)d^(9/2) ∏_(p∈F)log p,
    c_0=max(1,1/log(min F)),
    δ_(log n)^(-1) ≤ exp(M_D+1)c_0^(M_D)(1+log n)^(M_D).     (7)

Here δ is distance to the nearest distinct F-smooth log frequency. Indeed both
exponent vectors are bounded by c_0(1+log n) if that distance is ≤1; unique
factorization makes their rational product different from 1. BMS bounds that
product minus 1, and |e^x−1|≤e|x| for |x|≤1 gives (7). Distances >1 only improve
the bound. Source: Bugeaud–Mignotte–Siksek, Annals 163(2006), pp988–989,
[Theorem 9.4](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf),
real-field D=1 case. This is an old external theorem/new instance, not a new
Diophantine theorem or a property of unrestricted g-integers.

By (3), the actual-gap cost

    K_F(T)=Σ_(n∈N_F) δ_(log n)^(-1)||a_(n,T)||₂²             (8)

is finite, uniformly in T. For example set Z_(j,F)(σ)=Σ j^ω(n)n^(-σ), so

    Z_(j,F)(σ)=∏_(p∈F)(1+(j−1)p^(-σ))/(1−p^(-σ)).            (9)

The elementary inequality

    x(1+x)^M ≤ e^(1/2)[2(M+1)/e]^(M+1)e^(x/2), x≥0,

together with (7) proves

    K_F(T) ≤ e^(1/2)c_0^(M_D)[2(M_D+1)]^(M_D+1)Z_(4,F)(1/2).
                                                                    (10)

For fixed F, finite Hilbert-valued MV with actual gaps, followed by absolute
L² convergence from (4), therefore yields a legitimate **infinite** formula

    (1/H)∫_(R0)^(R0+H)||Σ_n a_(n,T)e^(iRx_n)||₂² dR
       ≤ Σ_n||a_(n,T)||₂² +(C/H)K_F(T).                     (11)

One can use finite truncations of the full frequency set: their local gaps are
at least the full-set gaps, so the same summable majorant (8) applies. No
unjustified theorem for a non-summable weighted sequence is needed.

The bound (10) is not uniform enough for the desired cofinal height. If
F=F_L={p<e^(2L)}, d~e^(2L)/(2L), then

    log M_D(F)=d[log(2L)+log30+o(1)].                         (12)

The logarithm of the **available upper certificate** (10) is of order
M_D log M_D, far above log H=βθe^L for fixed θ. This does not prove a lower
bound for the true K_F, nor a lower bound for actual source cost. It only means
this perfectly legal fixed-F repair does not certify the simultaneous limit.

## 4. Diagonal and finite-height error, retaining all coefficient weights

From now on F=F_L, L→∞. All constants below are independent of L after fixed
θ,β and cutoff constants are chosen. Ordinary PNT/Mertens input is already
paid in 560/571 and does not use RH.

Formula (3) and differentiation of the positive Euler product give

    D_L(T):=Σ_n||a_(n,T)||₂²
       ≤Σ_n4^ω(n)n^(-1)log n
       =Z_(4,F)(1) Σ_(p∈F)4p log p/[(p−1)(p+3)]
       =O(L^5).                                             (13)

Indeed Z_(4,F)(1)=O(L^4), while the last prime sum is O(L). This is a deliberately
rough independent check. The stronger support/least-prime grouping proved in
the companion [coefficient/domain proof](coefficients-domain-and-diagonal.md),
(10)/(12), gives

    sup_(T>0) D_L(T)=O(L^4).                                 (13a)

We consume that stronger already available diagonal in the theorem below;
improving the weaker check (13) is not a second result. A diagonal by itself
does not pay finite height or the complete tail.

Freeze T=T0 temporarily and keep only log n≤A. Finite Hilbert-valued MV with
ordinary integer spacing δ_(log n)≥1/(2n) gives, for arbitrary R0,H>0,

    (1/H)∫_(R0)^(R0+H)||Σ_(log n≤A)a_(n,T0)e^(iRx_n)||₂²dR
      ≤C L^4+(C/H)Σ_(log n≤A)n||a_(n,T0)||₂²
      ≤C L^4+(CA/H)e^(A/2)Z_(4,F)(1/2).                    (14)

The last step uses Σ_(log n≤A)4^ω(n)≤e^(A/2)Z_(4,F)(1/2), a finite positive
Rankin bound. It is important that the error is not called O(diagonal/H).
The cofinal Euler product obeys

    log Z_(4,F_L)(1/2)=(4+o(1))e^L/L.                        (15)

Thus when A=c e^L, R0=exp(θe^L), H=R0^β, the finite-height error is at most

    C A exp{−(βθ−c/2)e^L+(4+o(1))e^L/L}.                    (16)

This tends to zero whenever c<2βθ. There is no m^-2 normalization in (13)–(16).

## 5. Paying the complete coherent tail in the same original norm

Let P_A be the truncated sum in (14), and P_full the sum (1). By (3), without
discarding any signs or coefficients in the underlying object,

    sup_R||P_full(R)−P_A(R)||₂
       ≤√T0 S_L(A),
    S_L(A):=Σ_(log n>A)2^ω(n)n^(-1/2).                       (17)

The upper uses absolute coefficients only as a sufficient estimate, not as
an actual tail lower bound. For every 0<α<1/2,

    S_L(A)≤e^(−αA)Z_(2,F_L)(1/2−α)
      =e^(−αA)∏_(p<e^(2L))
         (1+p^(-1/2+α))/(1−p^(-1/2+α)).                     (18)

Choose fixed k>0 and α=k/(2L), valid for large L. Uniform PNT on this fixed
k scale and the log product expansion give

    log Z_(2,F_L)(1/2−k/(2L))
          =(2e^k+o(1))e^L/L.                               (19)

To see the constant, Σ_(p<e^(2L))p^(-1/2+k/(2L))
=(e^k+o(1))e^L/L; the cubic and higher terms in
log[(1+q)/(1−q)] contribute O(1) for large L.

The moving exponent in this statement is paid as follows. Abel summation
from the ordinary PNT π(t)=t/log t·(1+o(1)), with its all-t error envelope
beyond a fixed head, gives uniformly for s∈[1/4,3/4]

    Σ_(p<X)p^(-s)=(1+o(1))X^(1−s)/[(1−s)log X].             (19a)

The fixed head is negligible uniformly because 1−s≥1/4. The integrated
PNT error has the same uniform envelope; a final elementary integration
by parts for ∫_2^X t^(-s)/log t dt has a uniform O(1/log X) relative error.
For X=e^(2L), s=1/2−k/(2L), the main expression is exactly
e^(L+k)/(L+k), giving the coefficient in (19). For this fixed k and all
sufficiently large L one has s≥5/12; hence Σ_p p^(-3s)≤Σ_p p^(-5/4)<∞,
uniformly, which pays the cubic O(1). At s=1/2, the quadratic/higher
error in log Z_4 is O(Σ_(p<X)1/p)=O(log L), harmless in (15).
No fixed-α asymptotic has been silently substituted at a moving α.

With A=c e^L, (18)–(19a) give

    log S_L(c e^L)≤[2e^k−kc/2+o(1)]e^L/L.                 (20)

For c>4e choose k=log(c/4)>1. Then

    d(c):=(c/2)[log(c/4)−1]>0,
    S_L(c e^L)≤exp{−[d(c)+o(1)]e^L/L}.                     (21)

Since T0~θe^L, the **unnormalized** squared full-tail cost in (17) is

    T0 exp{−[2d(c)+o(1)]e^L/L}=o(1).                        (22)

Every coefficient beyond A has been paid, not merely those up to a second
cutoff. No step uses the divergent ordinary-gap infinite MV sum (6), and no
factor m^-2 has been hidden in a probability normalization. This is a legal
non-sharp complete-tail certificate. The conditions c>4e and θ>2e below are
not proved necessary for the signed tail or for any capacity mechanism.

## 6. Locking complete Γ and the sufficient synchronous range θ>2e

Fix θ>2e. Choose β∈(0,1) and c so that

    4e<c<2βθ,  R0=exp(θe^L), H=R0^β,
    I_L=[R0,R0+H], T_R=Γ(R), T0=Γ(R0), A=c e^L.              (23)

Equations (14), (16), (17) and (22) imply

    (1/H)∫_(I_L)|b_F(R)|²||v_(R,T0)||²dR=O_θ(L^4),          (24)

including the harmless factor 1/(2π) from (1). Squared triangle inequalities
cost absolute numerical constants; no claimed exact leading diagonal is needed.

The final receiver has T_R, not T0. Complete Γ satisfies Γ′(R)=R^-1+O(R^-3),
so Δ_T=sup_(I_L)|T_R−T0|≤C H/R0. Original hard-endpoint cost gives

    ||w_(R,T_R)−w_(R,T0)||²=|T_R−T0|/(2π),
    |b_F(R)|²||v_(R,T_R)−v_(R,T0)||²
       ≤(M_op/m_op)² Δ_T/(2π).                             (25)

Here m_op=∏(1−p^-1/2), M_op=∏(1+p^-1/2) are the original operator bounds;
they are unrelated to the Diophantine exponent M_D(F) in (7). The exact
asymptotic is

    log(M_op²/m_op²)=(4+o(1))e^L/L.

Consequently (25) is exp{−(1−β)θe^L+(4+o(1))e^L/L}=o(1). Combining gives (A),
and, because ||w_(R,T_R)||²=T_R/(2π)~θe^L/(2π),

    (1/H)∫_(I_L)
       |b_F(R)|²||v_(R,T_R)||²/||w_(R,T_R)||²dR
          =O_θ(L^4e^(−L))→0.                               (26)

This is an actual b-weighted **original receiver norm** estimate, not the old
m²-normalized estimate. Its all-tail payment is new relative to 571. It is a
height average, not pointwise/ALL-height control, not a bound on the unweighted
norm (division by |b|² could reintroduce m_op^-2), and not a norm-ratio bound for
the receiver direction under a second operator.

For first-fixed F the actual-gap infinite formula (11), followed by the same
endpoint argument, instead gives an O_F(1) raw weighted average whenever
H→∞ and H/R0→0. One must not interchange that statement with (24): (10) does
not certify the cofinal rate, whereas (17)–(22) really do for (23).

## 7. Complete two-boundary inverse, model direction, and remaining payment

Keep exactly 571's true receivers u=H_+D_F P_Tw, v=L_-D_F*P_Tw,
K=L_-B_F D_F*H_+, J=[[I,K],[K*,I]]. Full returns and both boundaries obey

    δ_win=||v||²+||u||²−<(v,u),J^-1(v,u)>,
    δ_win≤min(||v||²,||u||²), ||u||=||v||.                   (27)

We do not replace J^-1 by finitely many returns. Equations (24)/(26) and (27)
therefore pay, in the same θ>2e range, the averaged positive part

    average |b_F(R)|²(δ_win(R))_+ =O_θ(L^4),
    average |b_F(R)|²(δ_win(R))_+/||w_R||²→0.                 (28)

The negative part, absolute δ, or its favorable signed cancellation would
require additional information. A bad gap factor is absent from the positive
upper (27), not magically absent from every inverse estimate.

If both boundary receivers are cleaned simultaneously, set V=overline(b)v,
U=b u. Then U=e^(iRT)R_T V for the original antiunitary reflection R_T, and

    |b|²δ_win=||V||²+||U||²−<(V,U),J_b^-1(V,U)>,
    J_b=C_b*JC_b, C_b=diag(I,overline(b)/b),
    (J_b)_(12)=(overline(b)/b)K.                              (28a)

All these phases have modulus one because b≠0. Keeping the old K after
independently cleaning both receivers would be wrong. The estimates (28)
only use the original pair and (27), so do not require replacing J by J_b
or estimating its cross term.

The actual Sonin error ε_F and the full source identity remain exactly 560/571:

    2πρ_F(R)=Γ(R)−2Σ_(p∈F,k≥1)log p p^(-k/2)cos(kRlog p)+ε_F(R),
    Q_W(r)=t_F(r)−<r,K_(F,I)r>
       +2|<r,cosh(u/2)>|²−2|<r,sinh(u/2)>|².                 (29)

The finite polynomial in (1) did not replace the complete prime-power sums in
(29). No pole or Γ/contact term is set to zero. The original Weil-source norm
is du L²/zero-extension Dlog, different from physical receiver dt and from
||w_R||²; neither transport is free. Cofinal k_R→w_R/full Sonin inverse
clipping remains unpaid, including the old word-budget gap, and (28) cannot
be renamed an ε_F or Q_W estimate.
The other Z and single-boundary terms in S_T, and their cofinal trace tails,
are not paid merely by estimating G_T^-1−S_T on a carrier. Their fixed-F
identities remain valid; a cofinal full-density consumption must also keep
their actual finite/infinite-height remainders.

The threshold θ>2e is well beyond θ≤1 dangerous core; θ>1 was already the old
555 favorable high-frequency size range. Thus (24) is a real local fee input
for the model receiver at an original weighted norm, but no whole-zeta leading
4/5 improvement, independent global RR capacity, or RH proof follows.
Requiring all complete mixed Weil Grams PSD would still be an equivalent
reformulation, while a separately proved same-source capacity would be a
genuine new input. This file supplies only the explicitly proved receiver
estimate, not that capacity.

## 8. General g-integer scope and stop condition

The algebraic coefficient identity needs genuine finite Euler generators and
their complete causal inverse; exact colliding values must first be grouped.
The physical norm argument also needs absolute convergence. Ordinary prime
independence, integer log spacing, the Z_j Euler products and the cofinal PNT
asymptotics enter different steps and cannot be inferred from generalized
functional duality. Continuous distributions require their own actual
Plancherel/renewal estimate; they do not inherit the ordinary MV spacing.

This gate has a concrete new finite-height whole-tail payment (24), so it is
more than a fixed-F Bohr average or a renamed unknown tail. It still stops
before Sonin transport/core; varying the cutoff just to reduce 2e is not a
new capacity input. A next contract should require a new exact transport or
source-level Γ-relative comparison, or an independently sourced global
sections/RR budget, rather than reuse the available model norm estimate to
claim complete positivity. The root alone decides admission/settlement.

No numerical fitting, finite inverse truncation, or pending process is used.

## 9. Source-reading scope in this producer turn

The BMS original Annals PDF was reopened through web on 2026-10-20, text
pages 19–20 / printed pp988–989: the modified-height definitions, the real
and complex versions of Theorem 9.4, and its short reduction to Matveev
Corollary 2.3 were read. This does not claim a reading of all 50 pages,
the whole proof of the paper's main theorem, or a fresh reading/reproof
of Matveev's original theorem. Its exact real D=1 constants are the source
of (7); unique factorization, the bounded-log ratio conversion, and the
summability argument are given here.

MV is consumed in the already paid 571/local source-audit scope: finite
Hilbert-valued real-log-gap inequality, by coordinate summation. This turn
did not re-download or re-read the entire MV proof. PNT/Mertens are the
old ordinary-prime inputs of 560/571; the uniform moving-exponent Abel
deduction needed for this new tail bound is explicitly supplied in (19a).
None of these source facts assumes unknown ζ zero locations.

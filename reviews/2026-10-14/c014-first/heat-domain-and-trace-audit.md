# C014 independent audit: actual Gamma, killed domain and profile trace

2026-10-14. Owned by `/root/c014_heat_core`; requested by root for the first
C014 admission. This file changes no STATE, cadence or Git and consumes no
separate research iteration. It does not declare the macro Goal complete.

## 1. Recovery, object and audit decision

Recovered AGENTS, README/STATE, `research_state.py check` then `show`, current
Goal/frontier, C014 and D20261014O. At this audit's start the actual working
tree was clean and HEAD was
`d8894ce35b45b793f510fb62891e533f7fed668d`. Subagent `get_goal` returned null;
that isolated result does not supersede the root's active runtime Goal.
The fixed macro baseline is `0c4f3a3eb609bb1d9564138fa4a35701f05605f2` and all
results at most 538. Current completion gate remains open.

Consumed draft:
[gamma-profile-heat-entry](../c013-moments/gamma-profile-heat-entry.md), raw
SHA256 `315d7c71d3c52d853c7b579ddc2d335a4b11d167d96401a48cdcdcb8f7766e89`.
Also checked actual normalization and full-tail argument in
[541](../../../notes/541-native-chebyshev-variation-and-full-gamma-boundary.md),
the exact graph/profile identity and its normalization correction in
[016](../../../notes/016-prime-graph-hodge-inequality.md), and the scalar
negative-trace theorem in
[028](../../../notes/028-core-renormalized-negative-trace.md).

**Decision:** the Gamma-only heat/profile transport is valid on the original
zero-extension complex Dlog domain. No fatal domain, factor, positivity or
limit-order flaw was found. Two compressed steps in the draft should be made
explicit when consumed: prove that the half-product is Hilbert--Schmidt
before invoking the cyclic trace, and spell out the graph-norm orbit in the
bounded-potential Trotter proof. Both repairs are proved below without an
unchecked Golden--Thompson claim or a whole-Weil positive semigroup.

This audit establishes only the heat/source transport and the heat endpoint
fee. It does not independently settle the arithmetic record selection,
cofinal net comparison, baseline novelty or the macro completion gate.

## 2. Actual multiplier and full zero-extension form

On I=(-L,L), with Lebesgue L2 and zero extension E, keep

    Gamma(t)=Re psi(1/4+it/2)-log pi=actual 2 theta'(t),
    Gamma0=-gamma-pi/2-3 log 2-log pi,
    Phi(t)=Gamma(t)-Gamma0.

The primary [NIST digamma integral](https://dlmf.nist.gov/5.9#E16) was browsed
and checked. Subtract its value at z=1/4, take real parts and set its
integration variable equal to 2a. This gives exactly

    Phi(t)=integral_0^infinity w(a)(1-cos(ta)) da,
    w(a)=2 exp(-a/2)/(1-exp(-2a)),
    nu(a)=w(|a|)/2=exp(-|a|/2)/(1-exp(-2|a|)).        (A)

Thus Phi is nonnegative, even and continuous, not a half-Gamma substitute.
The symmetric Levy measure has finite integral of min(1,a^2); in fact its
full second moment is finite. Parseval gives

    J(f)=1/2 integral_0^infinity w(a)||T_a f-f||_2^2 da
        =(2pi)^-1 integral_R Phi(t)|fhat(t)|^2 dt.    (B)

The factor 1/2 in (B) is correct: the translation norm square supplies
2(1-cos(ta)). Equivalently the full symmetric Levy form is
`1/2 integral_R nu(a)||T_a f-f||^2 da`.

The full form is closed with domain the weighted Fourier L2 space. The Binet
estimate in section 8 gives Phi(t)=log(2+|t|)+O(1), with fixed upper/lower
comparability after adding the L2 norm. Hence this is the actual Dlog form
domain. Restriction to zero-extended functions supported in the closure of I
is closed: the support condition is an L2-closed subspace, and the form norm
dominates L2. Smooth sources supported inside I give density in L2(I).

This restriction has Cc-infinity(I) as a form core. One explicit proof uses
unitary dilation U_r f(x)=r^(-1/2) f(x/r), r increasing to 1 from below. Its
Fourier transform is sqrt(r) fhat(rt), and the logarithmic weights obey
`w_log(t/r) <= C w_log(t)` uniformly for 1/2 <= r <= 1. Approximation in
weighted Fourier L2 by compact continuous functions proves strong
continuity of U_r in the form norm. The support is now inside rI. Mollify
with a nonnegative compact smooth kernel of radius smaller than its boundary
margin; its Fourier multiplier is bounded by 1 and tends to 1. Dominated
convergence proves form convergence. This establishes the intended domain,
not an extra Sobolev boundary condition chosen to help the estimate.

Let A_I be the nonnegative selfadjoint operator of this restricted form.
Then Gamma_I=Gamma0 I+A_I. This is the killed/Dirichlet realization needed
below, not a regional jump form and not one-time free-semigroup compression.
All form and operator statements use the complexification of the real form.

## 3. Free probability density, including small time

Truncate nu on |a|>epsilon. The resulting symmetric compound-Poisson laws
at time s have characteristic functions exp(-s Phi_epsilon(t)) and second
moments at most s integral a^2 nu(a) da. The uniform second moment makes
them tight. Every weak subsequential limit has characteristic function
exp(-s Phi(t)), which is continuous at zero. Fourier uniqueness yields one
probability law, and characteristic functions prove its convolution
composition for arbitrary positive times. The same construction applies to
every nonnegative submeasure with finite Levy second moment.

The asserted submeasure is correctly normalized:

    nu0(a)=exp(-|a|/2)/(2|a|) <= nu(a),
    Phi0(t)=1/2 log(1+4t^2).                         (C)

The inequality follows from 1-exp(-2a)<=2a. The exponent follows by
integrating exp(-a/2)(1-cos(ta))/a on the positive half-line. At time s its
law is the difference of independent Gamma(s/2, scale 2) variables: direct
Laplace integration of the gamma density gives characteristic function
(1+4t^2)^(-s/2). This law has an L1 density for every s>0. Convolution with
the residual probability law therefore gives an L1 density p_s of the full
free law for every s>0. Symmetric nonnegative representatives may be used.

For s>1, exp(-s Phi) is integrable by (C), and inversion gives the canonical
continuous bounded density with

    p_s(0)=(2pi)^-1 integral exp(-s Phi(t)) dt,
    0 <= p_s(x) <= p_s(0).                         (D)

For s<=1 this boundedness and canonical diagonal value are not asserted.
For the later half-time calculation, if s>1 then exp(-(s/2)Phi) is in L2,
so Plancherel and the already constructed L1 density give

    ||p_(s/2)||_2^2=p_s(0).                         (E)

This identity does not depend on a diagonal representative at time s/2.

## 4. Killed/free domination and existence of a measurable kernel

For real nonnegative g, test a resolvent equation against the solution's
negative part. The jump inequality
`(a-b)(a_- - b_-) <= -(a_- - b_-)^2` gives positivity of the full and the
restricted resolvents. These are real statements; their linear operators
then act on the full complex Hilbert space.

For lambda>0 and g>=0 supported in I, put

    u=(lambda+A_I)^-1 g, extended by zero,
    r=(lambda+A_R)^-1 Eg, A_R=Phi(D) on the line.

Both are nonnegative. Their difference is in the full form domain; normal
real contraction gives h=(u-r)_+ in that domain. Since u=0 and r>=0 off I,
h is also an admissible restricted test function. Subtraction of the two
variational equations gives

    lambda ||h||^2+J(u-r,h)=0,
    J(u-r,h)>=J(h,h)>=0.                           (F)

The second inequality is the pointwise positive-part inequality inside the
full jump integral. Thus h=0 and Eu<=r. Positivity permits iteration of the
resolvent comparison. The spectral-calculus approximation
`exp(-sA)=strong-limit (I+sA/m)^(-m)` then gives

    E exp(-sA_I)g <= exp(-sA_R)Eg, all s>0, g>=0.   (G)

Kernel existence can be proved directly rather than assumed. On rectangular
sets E1 x E2 in I^2, the positive bimeasure
`<1_E1, exp(-sA_I)1_E2>` is dominated by the finite positive measure with
density p_s(u-v). Finite grid refinements make it an additive positive
functional on the rectangle algebra. Dominance gives continuity from above
on that algebra and hence a measure extension; Radon--Nikodym supplies
its density r_s. Agreement first on indicators and simple functions, then
Young's bound and L2 density, proves the operator representation. Selfadjointness
gives symmetry. In particular

    0 <= r_s(u,v) <= p_s(u-v) a.e. on I^2.           (H)

For s>1, (E) and (H) show that exp(-sA_I/2) is Hilbert--Schmidt, with
its squared HS norm at most 2L p_s(0). Consequently exp(-sA_I) is trace
class. Compact resolvent is a consequence of this trace statement, not its
unproved premise.

## 5. Bounded step potential: a direct strong product limit

For every fixed L the actual D_L is a bounded real finite step function.
No uniform-in-L boundedness and no preservation of Dom(A_I) by multiplication
are required. Write A=A_I, D=D_L, H=A-D with Dom(H)=Dom(A), and

    F(h)=exp(hD/2) exp(-hA) exp(hD/2).

H is selfadjoint by bounded perturbation. Its graph norm and A's graph norm
are equivalent. F(h) is positive selfadjoint, positivity preserving, and
`||F(h)^n|| <= exp(nh ||D||_infinity)`.

Let E_h=exp(hD/2), T_h=exp(-hA). For f in Dom(A), expand exactly

    F(h)f-f = E_h(T_h-I)f
            +E_h(T_h-I)(E_h-I)f +(E_h^2-I)f.        (I)

After division by h the first and third terms tend to -Af and Df.
The middle term tends to zero because `(E_h-I)f/h -> Df/2` in L2 and
T_h-I tends strongly to zero with uniformly bounded norms. This is the
precise reason a discontinuous D need not map Dom(A) into itself.

The resulting difference quotients are uniformly bounded from the graph
norm to L2: `||(T_h-I)f/h||<=||Af||`, and the bounded D terms are controlled
by C_D ||f||. The same graph bound holds for the exact semigroup quotient
of H. Thus the local error
`[F(h)-exp(-hH)]f/h -> 0` is uniform on every compact graph-norm set.
For f in Dom(H), its orbit `{exp(-rH)f:0<=r<=s}` is graph-norm continuous
and compact, since H commutes with its semigroup. The telescoping identity
for `F(s/n)^n-exp(-sH)`, stability and uniform local consistency show
its norm on f tends to zero. Density and stability extend this convergence
to every complex L2 source. No small-time trace convergence is needed here.

## 6. Even products: HS first, cycle second, positive trace last

Fix s>1 and n=2m, h=s/n. Let M=||D||_infinity. The kernel of F(h) is
`exp(hD(u)/2) r_h(u,v) exp(hD(v)/2)`. Its m-fold nonnegative Tonelli
composition K_m represents F(h)^m and is dominated by

    K_m(u,v) <= exp(mh M) p_(mh)(u-v)
             =exp(sM/2) p_(s/2)(u-v) a.e.           (J)

Here all intermediate restricted variables were extended to the line;
convolution of L1 densities is legitimate even at the small time h<=1.
By (E), K_m is in L2(I^2). Therefore F(h)^m is Hilbert--Schmidt **before**
the cyclic trace formula is used. Its symmetry and Tonelli give

    Tr F(h)^(2m)=||F(h)^m||_HS^2
      =integral_(I^n) product_j r_h(u_j,u_(j+1))
         exp[(s/n) sum_j D(u_j)] du_1...du_n,
      u_(n+1)=u_1.                                 (K)

Scalar Jensen bounds the exponential by `(1/n)sum_j exp(sD(u_j))`.
Rotation of the cycle reduces all n contributions to one. Replace the
restricted kernels by (H), and extend u2,...,un to the line. The resulting
anchored free cycle is evaluated by splitting into two m-step paths:

    integral_R p_(s/2)(u1-v) p_(s/2)(v-u1) dv
      =||p_(s/2)||_2^2=p_s(0).                     (L)

This proves, uniformly in even n,

    Tr F(s/n)^n <= p_s(0) integral_I exp(sD(u)) du.  (M)

It does not read a possibly noncanonical small-time diagonal. Positivity
and the strong limit from section 5 imply positive-trace lower semicontinuity:
for each finite orthonormal family, take the limit of its sum of quadratic
matrix elements and bound by (M); then take the supremum over such families.
Consequently

    Tr exp[-s(Gamma_I-D)]
      <= C_Gamma(s) integral_I exp(sD(u)) du,
    C_Gamma(s)=(2pi)^-1 integral_R exp[-s Gamma(t)]dt,
    s>1.                                          (N)

Both the product limit and the trace argument are for fixed L,s. Arithmetic
growth and s approaching 1 are applied only after this exact inequality,
with their separate fees; no simultaneous uniform Trotter assertion is used.

## 7. Original complex-source inertia and complete poles

The actual completed-square identity is

    Q_L = Gamma_I +sum_(n<exp(2L)) w_n E_(log n)
          -D_L +2|C><C|-2|S_pole><S_pole|,
    w_n=Lambda(n)/sqrt(n),
    E_a(f)=integral_overlap |f(u+a)-f(u)|^2 du,
    C(f)=integral_I f(u)cosh(u/2)du,
    S_pole(f)=integral_I f(u)sinh(u/2)du.            (O)

Every actual prime power remains; each graph form and the even pole is
nonnegative. The odd pole is a bounded rank-one negative form on the same
complex Dlog domain. Equation (N) implies compact resolvent of Gamma_I-D;
all graph and pole perturbations are bounded for a fixed L. Form min--max
and rank-one interlacing therefore give

    n_-(Q_L) <= n_-(Gamma_I-D_L)+1
              <= 1+C_Gamma(s) integral_I exp(sD_L). (P)

The last step uses exp(-s lambda)>1 for each negative eigenvalue. It applies
to the whole complex domain, with multiplicities, rather than a matrix or
a condition S_pole(f)=0. The +1 accounts for the original odd pole. No
positive-semigroup claim is made for Q_L, and the 529 standard-cone
obstruction is not revived.

## 8. Full Gamma heat endpoint: the two tails really cost 2/eta

The primary [NIST Binet identity](https://dlmf.nist.gov/5.9#E15) was checked.
Use z=5/4+it/2 and recurrence from z0=1/4+it/2. For |t|>=1, the Binet
remainder has modulus at most 1/(15|t|), as in 541. Also

    log|z|-log(|t|/2)=1/2 log(1+25/(4t^2)) <=25/(8t^2),
    |1/(2z)|<=1/|t|, |1/z0|<=2/|t|.

Thus the explicit safe bound is

    Gamma(t)=log(|t|/(2pi))+epsilon(t),
    |epsilon(t)| <= 7/|t|, |t|>=1.                 (Q)

For 1<s<=2, `|exp(-s epsilon)-1|<=14 exp(14)/|t|`. The difference between
the complete two-tail contribution to C_Gamma and its log model is therefore
O(1) uniformly in s, since the residual integral is bounded by a constant
times integral_1^infinity t^(-s-1) dt. On |t|<=1 use Gamma>=Gamma0 to pay
a uniform finite fee. The two-tail log model is

    (2pi)^s/[pi(s-1)].

Hence for 0<eta<=1,

    C_Gamma(1+eta)=2/eta+O(1),                      (R)

with an absolute O(1). Both signs of frequency, the actual multiplier,
and low-frequency mass are included. There is no uncharged remainder of
size o(S) inside an exponent. A half-Gamma or one-tail normalization cannot
be substituted into (R).

## 9. Scope retained for root reconciliation

The source/domain and heat-fee gates (N), (P), (R) are independently proved.
They hold for every finite L>0 and every s>1 on the full original complex
domain. Their constants do not hide an arithmetic approximation to D.
The original finite step integral is exact and can now be bounded using an
independently audited actual arithmetic input.

This does not make Q positive, supply a lower bound for its negative count,
identify a Xi spectral branch, or complete the long Goal. The arithmetic
record and strict-cutoff fee must still be reconciled by root. Any net
consequence must also beat the strongest baseline assets, including the
old exact profile/scalar negative trace. All-L claims cannot be inferred
from a cofinal record family. This review is one separately owned input to
root's single C014 settlement, not a new round or an authorization change.

## 10. Final note 543 consumption and version confirmation

Root requested this read-only reconciliation after the first review. At the
follow-up start I again recovered AGENTS/README/STATE, ran check then show,
and read the unchanged Goal/frontier, C014 and D20261014O. STATE still names
C014 running with no settled iteration; the original cadence remains 1/8.
Actual HEAD remains `d8894ce35b45b793f510fb62891e533f7fed668d`; the worktree
contains root's in-progress STATE/checkpoint/note543 and the separately
owned reviews. Subagent runtime lookup again returned null, which makes no
claim about root's active Goal. Recovery and this reconciliation are zero
additional research rounds.

Read the full
[543](../../../notes/543-full-gamma-heat-arithmetic-records-and-thermal-boundary.md),
raw SHA256 `965a20f403ddd78a88c007dc81bd4e5a1272d26095a471037211cfda83e6ae08`.
Its sections 2--4 correctly consume the actual Gamma/domain and trace
argument audited here. The original 2 theta-prime multiplier, Levy factors,
all s>0 free densities, killed zero-extension form, resolvent comparison,
and s>1 half-time HS calculation are retained. Section 3 now explicitly
pays the half-product HS norm before the cyclic trace and uses the common
operator domain/equivalent graph norms/compact semigroup orbit for the
bounded-D Trotter limit. No requirement that the actual step multiplication
preserve Dom(A_I) was introduced.

The resulting monotone comparison remains on all complex sources with
original pole multiplicity: the graph and positive even pole are dropped
only for a lower comparison, and the full negative odd pole costs exactly
one dimension. Both frequency tails and the low-frequency mass in the
heat fee are included; `C_Gamma(1+eta)=2/eta+O(1)` has the correct actual
normalization. Product limits are fixed-L, fixed-s before the separate
arithmetic and temperature bounds are applied.

No over-consumption was found in the scope statements: the note labels the
record bound cofinal, compares certified upper budgets rather than actual
negative counts, distinguishes Gamma-only positivity from whole-Q
positivity, and leaves PSD/Xi and the macro Goal unpaid. The thermal ledger
limitation is explicitly limited to that ledger, allowing core removal and
joint signed graph/pole escapes. Arithmetic/net-baseline assertions in
sections 5--7 are outside this heat auditor's independent certification;
their assigned reviews and root reconciliation remain the authority.

**Final heat/domain/source scope verdict: PASS for the inspected note543
version above.** This appends a consumption/version check, not a new theorem,
new iteration, STATE edit or completion decision. Any later mathematical
edit to those consumed sections requires scope revalidation rather than
silently inheriting this hash-bound confirmation.

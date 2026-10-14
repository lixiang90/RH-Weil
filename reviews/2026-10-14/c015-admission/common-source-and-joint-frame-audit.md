# C015 independent common-source and joint-frame audit

2026-10-14. Owned review by `/root/c015_joint_frame`; no STATE, cadence,
Goal, producer or Git mutation. This is evidence for the parent admission
iteration, not an independently counted research round.

Recovery read AGENTS, README, STATE, check/show, current Goal/frontier,
C015 and D20261014P. The actual starting HEAD was
`8cba2c811ca301a17816a8330b40a2a1ef87c5d3`, with a clean worktree at that
observation. `get_goal` in this child returned null: it cannot certify or
replace the parent's active runtime Goal. STATE's saved runtime observation
is not a live parent observation. Fixed macro baseline remains
`0c4f3a3eb609bb1d9564138fa4a35701f05605f2` and all results through 538.

The previous completed turn 543 made progress: it supplied a cofinal actual
whole-source count budget that saves a factor L over the strongest old
scalar trace family, and stopped thermal refinement. It did not pay PSD,
the exponentially sized dangerous core, or Xi identification. This audit
addresses the next causal gap: whether local positive time delay, once
transported to a common physical source, supplies additional joint data.

## 1. Exact object and verdict

Let I=(-L,L), H_L=L2(I,du), with complex sources and zero extension J_L to
L2(R). Use the unnormalized Fourier transform

    Ff(t)=integral_R f(u)exp(-itu)du,
    ||f||^2=(2pi)^(-1)integral_R |Ff(t)|^2dt.

The original form domain is

    Dlog={f in H_L: integral log(2+|t|)|F(J_L f)(t)|^2dt<infinity}.

Write R_f(h)=integral_R f(u+h)conjugate(f(u))du, X=exp(2L),
S_L=sum_(p^m<X) log(p)p^(-m/2). The actual whole form is

    Q_L(f)= (2pi)^(-1) integral Gamma(t)|Ff(t)|^2dt
            -2 sum_(p^m<X) log(p)p^(-m/2) Re R_f(m log p)
            +2|C(f)|^2-2|S_pole(f)|^2,
    Gamma(t)=Re psi(1/4+it/2)-log pi=actual 2theta'(t),
    C(f)=integral_I f(u)cosh(u/2)du,
    S_pole(f)=integral_I f(u)sinh(u/2)du.

The conclusions of this independent audit are:

1. Zak periodization and frequency fiberization are genuine *linear*,
   isometric common-source maps. Their sign conventions require a theta
   reflection when the stated Fourier convention is used.
2. Positive local time delay transports exactly to the reflected actual
   prime-power contribution after the unit term is subtracted within each
   prime. This identity extends to original L2, hence Dlog, without an
   approximation error, a new norm or a missing prime power.
3. Cross-prime source compatibility and the full cross-prime filter Gram
   can be written explicitly. They are not orthogonality relations or a
   new Bessel estimate. In particular there is no unweighted all-prime
   positive analysis frame: every prime with log p>=2L contributes exactly
   log(p) times the original mass.
4. The finite joint positive Gram, after the exact unit subtraction,
   contains precisely the old 017 prime translation operator. Its local
   square completion is the same old Euler graph square. No new whole
   growth consequence, domination or core-density estimate has been
   proved by this transport.

Thus the common norm and signs are paid entry checks, but the C015 new-net
gate remains unpaid. This is not a claim that all graded or joint-prime
methods fail, and it is not a counterexample to Q_L positivity.

## 2. Scope of the local source used here

The primary source inspected was
[Burnol, math/9901051v2, Theorems II and VII/VIII/X](https://arxiv.org/html/math/9901051).
For the unramified, unit-invariant Q_p component, its formulas specialize
to the bounded circle multipliers below. The time-delay sign is positive;
the actual conductor uses its negative sign after a unit correction.
The original trace theorem is a graded local statement and supplies no
global joint domination of the common physical source.

Set a=log p, r=p^(-1/2), and

    P_r(theta)=(1-r^2)/|1-r exp(i theta)|^2,
    T_p(theta)=a P_r(theta),
    H_p(theta)=a-T_p(theta).

The positive rank-one interacting kernel in this component has diagonal
P_r. Integrating its shifted projection squares reproduces multiplication
by aP_r; the latter is bounded for every fixed p. Its inverse and positive
square root are bounded as well because

    (1-r)/(1+r) <= P_r(theta) <= (1+r)/(1-r).

No ramified component is added to the zeta source. No source-dependent
choice of grading changes H_p into +T_p. The identities below are elementary
linear transports of these exact unramified multipliers; they do not
identify the real f with a single Schwartz--Bruhat local test function.
The ancillary continuous variable v, or frequency alias index j, carries
the multiplicity required by the original real physical source.

## 3. Zak map, its inverse, support range and norm

For a>0 define

    (Z_a f)(v,theta)=sum_(k in Z) f(v+ka) exp(ik theta),
    0<=v<a, 0<=theta<2pi.

For full L2(R), this is an L2 Fourier series in k for almost every v.
It defines a unitary map to

    K_a=L2([0,a) x circle, dv dtheta/(2pi)).

Indeed discrete Parseval and the disjoint partition u=v+ka give

    ||Z_a f||^2=integral_0^a sum_k |f(v+ka)|^2dv=||f||^2.

Conversely, for h in K_a and u=v+ka,

    (Z_a^(-1)h)(u)=integral_circle h(v,theta)exp(-ik theta)dtheta/(2pi).

The disjoint partition and Fourier completeness prove surjectivity, not
just an injection. For the original H_L, its range is the *closed* space

    R_(a,L)={h: h_k(v)=0 whenever v+ka is outside I, almost everywhere}.

For smooth compactly supported f each v has only finitely many nonzero
coefficients. The zero-extension convention, rather than a periodic
physical source, determines this support constraint. The endpoints of I
have measure zero and do not alter any norm or operator statement.

In particular if a>=2L, for almost every v there is at most one allowed k.
The modulus of h(v,theta) is then independent of theta. This elementary
support fact will be important for the large-prime cancellation.

## 4. Frequency fibers and the theta reflection

Define the linear fiber map requested in the admission contract by

    (U_a f)(theta)_j=a^(-1/2) Ff((theta+2pi j)/a), j in Z.

It is unitary from L2(R) to
L2(circle,dtheta/(2pi);ell2(Z)); partitioning the frequency line proves

    integral_circle sum_j |U_a f(theta)_j|^2 dtheta/(2pi)=||f||^2.

With the stated sign of F and Z, U_a corresponds to Z_a(v,-theta), not
Z_a(v,theta). Specifically, let t_j=(theta+2pi j)/a. The functions
a^(-1/2)exp(it_j v), j in Z, are an orthonormal basis of L2([0,a)), and

    integral_0^a Z_a f(v,-theta)exp(-it_j v)dv=Ff(t_j).

Proof: put u=v+ka; the remaining factor is
exp(ik(at_j-theta))=exp(2pi i j k)=1. The basis coefficient therefore is
a^(-1/2)Ff(t_j). If Z_a(v,theta) is kept instead, use t_j=(2pi j-theta)/a.
These are equivalent unitary conventions. Since P_r(theta)=P_r(-theta),
the time-delay quadratic energy is unchanged by the required reflection.

This explicitly repairs a possible bookkeeping ambiguity without changing
the object, source norm or prime signs. The fiberized local energy is

    E_p(f)=integral_circle a P_r(theta) sum_j |U_a f(theta)_j|^2 dtheta/(2pi)
          =(2pi)^(-1) integral_R a P_r(at)|Ff(t)|^2dt
          =integral_0^a integral_circle a P_r(theta)|Z_a f(v,theta)|^2
                                             dtheta/(2pi)dv.

Every equality holds for all full L2 sources and thus for original H_L.
No nonlinear square root of a periodized |Ff|^2 has been called a linear map.

## 5. Exact prime powers, unit cancellation and form-domain extension

The uniformly and absolutely convergent Poisson expansion is

    P_r(theta)=1+2 sum_(m>=1) r^m cos(m theta).

Plancherel gives

    E_p(f)=a||f||^2+2a sum_(m>=1)r^m Re R_f(ma),
    a||f||^2-E_p(f)=-2a sum_(m>=1)r^m Re R_f(ma).          (A)

With zero extension of f supported in I, R_f(h)=0 for |h|>=2L.
At |h|=2L the overlap has measure zero; this includes any exact cutoff
prime power p^m=X. Thus (A) reduces exactly to all and only p^m<X.
The prime weight is log p for every proper power, never m log p.

For each fixed p, the time-delay multiplier is bounded. The right side
of (A) is norm continuous on L2 and, on H_L, is a finite sum of bounded
translation-compression forms. Hence it extends from smooth sources to
all original complex H_L without a remainder. Restricting to Dlog is
legitimate. The finite pole functionals are bounded on H_L; Gamma keeps
its actual multiplier and original Dlog domain. Nothing in this local
identity supplies a new Gamma lower bound or a pole domination.

If p>=X, all nonconstant correlations vanish, so exactly

    E_p(f)=log(p)||f||^2,
    <H_p U_a f,U_a f>=0.                                  (B)

This is true for *every* original source, not just finite tests or a low
frequency subspace. Consequently sum_p E_p(f) and sum_p log(p)||f||^2
both diverge for every nonzero f. The actual signed contribution is zero
prime by prime in that tail. Separating the two divergent totals and
renormalizing after summation is not licensed by the local theorem.

For a finite place set P,

    sum_(p in P) <H_p U_p f,U_p f>
      =sum_(p in P)log(p)||f||^2-sum_(p in P)E_p(f)

is safe. Once the unit term has been canceled within each p, all tail
p>=X terms can be removed. This order is indispensable even at fixed L.

## 6. Cross-prime range compatibility is exact but not an inequality

For two positive steps a,b, define

    W_(b,a)=Z_b Z_a^(-1): K_a -> K_b.

It is a unitary and maps R_(a,L) onto R_(b,L). A pair of physical images
(h_a,h_b) comes from the same f exactly when

    h_a in R_(a,L), h_b=W_(b,a)h_a.                       (C)

Here is a computable L2 expression for W. For each x=v+lb, put

    v_a(x)=x-a floor(x/a), k_a(x)=floor(x/a).

Then

    (W_(b,a)h)(v,theta)
      =sum_l exp(il theta) integral_circle
           h(v_a(v+lb),phi)exp(-ik_a(v+lb)phi)dphi/(2pi).

The expression uses Fourier series in L2. On the restricted support range,
only finitely many l have v+lb in I, and the support conditions pay the
other terms exactly. For any finite family of primes, one member h_p
determines all the others by (C). Conversely, these compatibility
conditions reconstruct one and the same original f.

Thus the joint range is a correlated diagonal graph of unitary maps; it
is not a product of independently chosen local positive vectors. For
n places the bare joint map f -> (Z_p f)_p has norm sqrt(n)||f||.
There is no factor independent of n from common-source compatibility.
This is an exact description of the range, not new arithmetic coercivity.

The frequency version is equivalent: each local alias family is obtained
by regrouping the *same* Ff(t). On H_L that function also has the original
Paley--Wiener support constraints. The local theorem does not add an
independent relation between Ff and the actual Gamma or pole responses.
Proving a stronger estimate on this common range would be new work; merely
writing the common range is not that estimate.

## 7. A fully computable cross-prime filter Gram

There is also a useful common-output realization of the positive energy.
On full L2(R), set tau_h f(u)=f(u+h) and

    B_p=sqrt(a(1-r^2)) sum_(m>=0) r^m tau_(ma).

The series converges in operator norm. Its Fourier multiplier is
sqrt(a(1-r^2))/(1-r exp(iat)), so

    ||B_p f||^2=E_p(f),
    B_p^* B_p=a[I+sum_(m>=1)r^m(tau_(ma)+tau_(-ma))].       (D)

The Zak and fiber analysis maps are unitary presentations of this
positive quadratic form; B_p is an explicit positive-square factor with
a harmless phase choice. B_p is invertible on full L2 for each fixed p.

For a second prime q, write b=log q, s=q^(-1/2). The cross Gram is

    B_p^* B_q=sqrt(ab(1-r^2)(1-s^2))
                  sum_(m,n>=0) r^m s^n tau_(nb-ma).        (E)

The double series is absolutely convergent in operator norm. Compression
to H_L is J_L^* (E) J_L; each translation contributes only if
|nb-ma|<2L, with any endpoint contribution zero. These are mixed ratios
log(q^n/p^m), not additional prime powers of a single prime. Formula (E)
is a calculable kernel/Gram, not a positive cancellation theorem for
the actual signed form.

The outputs are not automatically orthogonal. For any nonzero, real,
nonnegative f in Cc-infinity(I), every translation autocorrelation is
nonnegative. The m=n=0 term in (E) gives the rigorous lower bound

    <B_p f,B_q f> >=sqrt(ab(1-1/p)(1-1/q))||f||^2.          (F)

Thus distinct-prime outputs can have a large coherent unit component on
an actual legal source. This does not make Q_L negative; it only prevents
inferring an orthogonality gain from different prime labels. Mixed
near-ratios in (E) require their own signed arithmetic control if used.

Squaring a *combined* output sum_p c_p B_p f yields all mixed kernels
conjugate(c_p)c_q(E). The original Q_L contains no such cross-prime terms.
No canonical coefficients or paid comparison are supplied by local
positivity to replace those extra terms. Deleting them, or announcing
their favorable sign, would add an unproved premise.

## 8. Direct-sum Bessel budgets and the exact finite operator

For a finite P define A_P f=(B_p J_L f)_(p in P). Its exact analysis Gram is

    A_P^*A_P=sum_(p in P) J_L^* B_p^*B_p J_L
       =theta_P I+sum_(p in P,m>=1) a r^m
                  J_L^*(tau_(ma)+tau_(-ma))J_L,
    theta_P=sum_(p in P)log p.                            (G)

Only strict active prime powers survive the compressed nonconstant terms.
Subtracting theta_P I in (G), with the conductor sign, returns exactly
the old actual prime adjacency in 017. In particular if all p in P
are at least X, then A_P^* A_P=theta_P I, with best Bessel constant
theta_P. Allowing additional such primes makes that constant arbitrarily
large for every fixed L and every nonzero source.

More generally, for nonnegative scalar weights c_p, the tail p>=X of a
direct-sum analysis has the exact Bessel mass sum_(p>=X)c_p log p.
It is finite precisely when that weighted scalar series is finite.
Choosing summable weights changes the actual unit/prime coefficient
unless a separately proved inverse or signed comparison restores it.
The physical unweighted local formula corresponds to c_p=1 and cannot
be turned into an infinite positive Bessel frame.

There is no need for a repeated high-frequency carrier construction to
establish this entry limitation: it holds identically for every source
in the large-prime tail. It excludes only this unrenormalized positive
direct-sum rule. It does not exclude a genuinely coupled graded rule
that cancels units within each p and then controls its signed remainder.

## 9. Strongest old comparison and the unpaid new gate

[017 sections 1--2](../../../notes/017-unitary-euler-graph-structure.md)
already gives the actual translation square identity

    -2 Re R_f(h)=||f-tau_h f||^2-2||f||^2,

and, for the strict active powers,

    prime_Q(f)=sum_(p^m<X) log(p)p^(-m/2)||f-tau_(m log p)f||^2
                       -2S_L||f||^2.                    (H)

For a single p, full-line completion before compression reads

    a P_r(0)||f||^2-E_p(f)
      =a sum_(m>=1)r^m||f-tau_(ma)f||^2.

The infinitely many nonoverlapping translations on the right are not
free extra positive supply: their mass exactly cancels the scalar
P_r(0) shift to produce (A). On H_L the finite partial graph completion
of [016](../../../notes/016-prime-graph-hodge-inequality.md) further keeps
the spatial degree D_L. That stronger old representation, not the loose
sum of local scalar bottoms, must be the comparison baseline.

The actual Gamma convention is the corrected one in 016/017. The old
half-Gamma displays and numerical default shifts are not consumed.
Old 028 with the degree profile already implies the eventual
C L exp(S_L) whole negative-count upper budget. Newly settled
[543](../../../notes/543-full-gamma-heat-arithmetic-records-and-thermal-boundary.md)
gives C exp(S_L) on cofinal actual record windows; neither result pays PSD.
Equations (A)--(H) do not improve either budget, give a new common core
evaluation density, or provide a growing near-PSD error tending to zero.

Since A_P^* A_P-theta_P I is the same prime operator, a claimed estimate

    sum_(p<X)E_p(f)-theta_(p<X)||f||^2+2|S_pole(f)|^2
       <=q_Gamma(f)+2|C(f)|^2+epsilon_L||f||^2

for every complex Dlog source, with cofinal epsilon_L ->0, is exactly
the unpaid old whole Weil domination written through time delay. It is
not an independently supplied consequence of local positive T_p.
Likewise a compression or finite-core version needs its actual residual,
cross Gram, tail and source-uniform errors paid; local identities do not
do so. No finite matrix, frequency sample or unknown zeta position has
been used in this audit.

## 10. Admission recommendation and retained escape routes

The transport and exact local coefficient checks pass. The proposed new
joint forcing does not follow from the source now inspected. Close C015
after the parent's complete admission round unless another independent
review supplies a genuinely new joint source theorem. Do not spend its
budget on repeated Poisson identities, already known carriers, growing N,
or a new name for the global domination premise.

The bottleneck is unchanged: a new source must couple the actual signed
prime remainder, full Gamma and both pole responses on the same original
complex domain, with growing-support and core/complement fees quantified.
An independently proved bound for the mixed signed Gram (E), a common
graded polarization with a paid remainder, or a new core-density theorem
could change the decision. None is ruled out by this admission audit.
Canonical ordinary Sonin free comparison remains stopped under 535;
the bounded unramified time-delay transport here is not a revival of it.

Only the exact common-source formulas and the specific positive-direct-sum
failure above are established. No claim about all multi-prime scattering,
all graded geometry, actual negative spectrum, RH failure, worldwide
novelty or macro Goal completion is made.

## 11. Supplementary scope gate: removing the filter's constant does not save the actual weight

Parent-requested supplementary source check, zero additional research
rounds. Recovery again read AGENTS/README/STATE/check/show/current
Goal/frontier/C015/D20261014P and actual Git. HEAD remained `8cba2c8...`;
the observed worktree contained the parent's running-state checkpoint and
source material as well as independent review files. Child `get_goal`
again returned null and did not certify the parent runtime.

To avoid reusing the weights c_p from section 8, call the constant
coefficient of B_p

    beta_p=sqrt(a(1-r^2)), a=log p, r=p^(-1/2).

Subtracting it at the *filter* level gives the bounded full-line operator

    C_p=B_p-beta_p I=beta_p sum_(m>=1)r^m tau_(ma)
       =r tau_a B_p.                                      (J)

All series converge in operator norm; the last equality uses only the
translation group law and a change of index. Since tau_a is unitary,

    C_p^*C_p=r^2 B_p^*B_p=p^(-1) B_p^*B_p,
    H_p^(physical)=aI-B_p^*B_p=aI-p C_p^*C_p.              (K)

The identities are on full L2(R); compression by J_L pays the same
original complex source norm. In Zak/fiber language B_p^*B_p is exactly
the transported T_p from sections 4--5, so (K) is not a changed local
conductor or grading. Both local forms extend to all H_L and Dlog.

This distinguishes filter subtraction from subtracting a unit *energy*.
Indeed B_p=beta_p I+C_p, and its energy is

    ||B_p f||^2=beta_p^2||f||^2
                  +2 beta_p Re <f,C_p f>+||C_p f||^2.

The interference term is generally present. One cannot obtain the
original centered time-delay energy by just discarding beta_p I and
retaining an unweighted positive ||C_p f||^2.

For p>=X, the exact local energies are

    ||B_p J_L f||^2=a||f||^2,
    ||C_p J_L f||^2=(a/p)||f||^2.                          (L)

Thus a finite tail of the unweighted C_p analysis seems to have the
cheap scalar budget sum log(p)/p. Old PNT assets give its logarithmic
growth with the finite prime cutoff; this is an old consequence, not a
new input. But the actual signed Weil coefficients in (K) require the
*weighted* analysis energy sum_p p||C_p J_L f||^2. On the same tail its
exact budget is sum_p log p, canceling the unit mass within each p as
before. The gain of a factor p is paid back identically. Unweighted
C_p^*C_p also scales every nonconstant prime-power coefficient by 1/p;
using it without this restoration changes the actual zeta object.

For every finite P, one can check the exact statement directly:

    sum_(p in P) [a||f||^2-p||C_p J_L f||^2]
      =-2 sum_(p in P,m>=1) a r^m Re R_f(ma),

with all m a>=2L terms zero. The original proper-power weights, strict
cutoff, original norm and local negative conductor sign are unchanged.
The full Gamma and both poles must still be supplied on the same source;
the cheaper unweighted tail frame pays none of those joint fees.

The output norm in (L) is the full-line norm. If instead one clips the
filter output back to I, then J_L^* C_p J_L=0 for a>=2L, so the altered
formula a||f||^2-p||J_L^*C_p J_L f||^2 gives a||f||^2 rather than the
actual zero local contribution. Such clipping is another object change,
not a free support improvement.

This supplement verifies a concrete normalization gate; it does not
constitute a new whole-spectrum bound or a broad method boundary. It
does not change the earlier verdict, C015 budget, cadence or macro
completion gate. A genuinely new signed mixed-Gram or common graded
polarization theorem would still require independent arithmetic input.

## 12. Final 544 scope audit and zero-round classification

Read the complete parent note
`notes/544-graded-local-source-admission-without-new-joint-input.md`, raw
SHA256 `e54479df63ccb7d12301a45e2b0f65eda5f5938d3b1cfb61d9a26f494260fa18`.
This final scope review changes no root text, STATE, cadence or Git.
Mandatory recovery again found C015 running, latest mathematical iteration
543 and cadence 2; a saved handle entry did not itself establish live
runtime. Child `get_goal` was null as before; the parent must own its
runtime audit and terminal inventory reconciliation.

The assigned common-source content in 544 sections 2--4 passes:

- original complex Lebesgue L2, zero extension, Dlog and actual Gamma
  with both pole terms are retained;
- Zak norm has the correct dv dtheta/(2pi) measure; the plus-sign alias
  fiber is correctly identified with Z(v,-theta), and the even Poisson
  symbol pays the theta reflection without changing energy;
- local weights are log p for all powers; correlations with m log p>=2L
  vanish exactly, including any strict-cutoff endpoint;
- B_p uses the full-line norm; its absolute operator series gives the
  displayed mixed cross Gram with shift nb-ma;
- the cross Gram is not inserted into Q as a supplied new term, and
  different prime labels are not treated as orthogonal;
- p>=X has exact E_p=log(p)||f||^2 and zero conductor response; units
  cancel within each p before any place sum;
- C_p=r tau_a B_p has C_p* C_p=p^(-1)T_p; restoring actual Weil weights
  requires multiplying by p, and output clipping is correctly rejected;
- common source transport and joint positive Gram are identified as
  old 017 operator content. Stronger 016/028 and newly paid 543 are kept
  as spectrum comparisons; no count, near-PSD or Xi improvement is
  inferred from these formulas.

The final note also preserves the exact distinction between local positive
time delay and negatively graded unramified conductor. Original local
theorem/Haar/trace proof attribution is the separate source review's
responsibility; this scope review adds no independent global assertion.
The next modular-source preparation in section 5 is not consumed here as
a proven physical-norm transport or net result.

Classification is **source admission and old-tool recovery, zero new
mathematical rounds**. The phrase "parent complete admission round" in
section 10 describes completion of the review pass only, not mathematical
cadence settlement; the explicit 544 classification controls. A detailed
proof check, exact norm transport, supplementary normalization gate or
negative verdict on the missing new input does not manufacture a failed
mathematical iteration. Cadence remains 2 and latest settled mathematical
evidence remains 543. C015 may be stopped at this entry without claiming
a new method-class theorem or macro Goal completion.

The paid bookkeeping changes the next action, while the actual growth
joint signed/core/near-PSD and Xi bottlenecks are unchanged. This confirms
544's stated scope rather than silently promoting the local formulas.

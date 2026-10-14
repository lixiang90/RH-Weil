# C019: the projected Chebyshev critical rate retains RH strength

2026-10-14, independent audit by /root/c017_prime_pole. Only this file is
owned by this agent. No STATE/cadence/contract/root-note/Git mutation or
mathematical iteration settlement is made here.

## Recovery and precise conclusion

Recovered AGENTS, README, STATE, ran research_state.py check and then show,
and read the active Goal, macro frontier, C019 and D20261014T. The structural
check passed and does not certify mathematics. Needed original evidence was
547 section 4 and its canonical-joint short audit, 068/069/070 critical
Chebyshev energy scopes, and 521/522 source-growth scopes. At entry Git was
clean at HEAD 812d76d7af702ea815c2376aa228f6ba8990543b. STATE named latest
mathematical 546, C019 ready and cadence 0; 547 was a zero-round source-entry
note. The child get_goal result was null and does not replace the root's
runtime observation. Fixed baseline remains 0c4f3a3 / all results <=538.

For the exact projected arithmetic response W_N defined below, the following
conditions are equivalent:

    RH;
    for every epsilon>0, ||W_N||<=C_epsilon N^epsilon for all integers N>=4;
    ||W_N||<=C (1+log N)^K for all integers N>=4,
       for some finite fixed K and C.

In fact RH implies ||W_N||=O(sqrt(log N)) by the already paid 068 prefix
energy. A proposed specified smaller log exponent, in particular a uniform
O(1) bound, implies RH by the reverse proof; this audit does not assert its
converse. No stronger conditional regularity or log-exponent optimization
is pursued. The equivalence is a critical-strength identification, not a
new independent arithmetic bound. By C019's rule it supports zero-round
entry stop and strategy review, not macro Goal completion.

## 1. Exact arithmetic object and normalization

For every integer N>=4 put M=N-1, L=(log N)/2, x=exp(u+L). The original source
space is H_N=L2((1,N),dx/x), unitarily the original complex Lebesgue-u space
on I_L=(-L,L), with zero extension and the same Dlog form domain. P_N is
the dx/x-weighted mean projection on every complete cell (n,n+1), n<N,
and R_N=I-P_N. Write

    a_N(x)=N^(-1/4)sqrt x, p_N=P_N a_N,
    U_M=sum_(n<N)[1-4(sqrt(n+1)-sqrt n)^2/log(1+1/n)],
    ||p_N||^2=N^(-1/2)(M-U_M), 0<U_M<=1/8,
    psi_<(y)=sum_(q<y) Lambda(q), E_<(y)=psi_<(y)-y,
    W_N=R_N[a_N E_<(N/x)]/||p_N||
       =R_N[sqrt x E_<(N/x)]/sqrt(M-U_M).                (1)

The sum includes all proper prime powers. Since x>1, q<N/x automatically
implies the original strict q<N cutoff. At x=N/q an atom changes only a
null set; no atom, carry or positive-measure error is discarded.

547's exact canonical source identity is

    R_N Q_L p_N=R_N Gamma p_N-R_N[a_N E_<(N/x)]
       +R_N[D_N^+ R_N a_N]+D R_N a_N
       -N^(-1/2)(1+U_M)R_N b_N,
    b_N=N^(1/4)x^(-1/2), D=log N-<R_N a_N,R_N b_N>.

Its normalized carry is O(1), and its two displayed pole corrections are
o(1), with all carry and both actual poles retained. This audit does not
independently pay a uniform norm for R_N Gamma p_N/||p_N||; that is owned
by the Gamma review. If that normalized Gamma term is also uniformly
bounded, the complete normalized mixed response equals -W_N plus an O(1)
vector. Then its subpower rate and existence of a finite polylog bound are
equivalent to those in (1) by the triangle inequality. This conditional
statement is about the actual vector, not separately estimated component
norms or a fitted source.

## 2. Fixed first-cell legitimate probes

Choose any fixed complex h in Cc-infinity((1,2)) satisfying

    integral_1^2 h(x)dx/x=0.

It is a detail source for every N>=4: R_N h=h. Transported to u it is a
smooth compact source inside the original I_L; its dependence on u through
the fixed unitary transport is legitimate. We keep h fixed as N grows.
Define for real Y>=2

    S_h(Y)=integral_1^2 sqrt x E_<(Y/x) conjugate(h(x))dx/x,
    H_h(s)=integral_1^2 conjugate(h(x)) x^(1/2-s)dx/x.     (2)

H_h is entire. Self-adjointness of R_N gives the exact integer probe

    S_h(N)=sqrt(M-U_M) <h,W_N>.

Hence a subpower norm bound in (1) implies, for every such fixed h,

    |S_h(N)|<=C_(h,epsilon) N^(1/2+epsilon), N>=4.       (3)

The norm bound is a statement about the full detail vector, and therefore
controls all these probes. This is not the assumption that one specially
chosen probe detects every zero simultaneously.

## 3. Integer N is sufficient; the step function causes no missing limit

Let Y in [N,N+1], N>=4. For 1<x<2, the interval between N/x and Y/x has
length <1. It contains at most one possible integer prime-power jump.
Since Lambda(q)<=log q,

    |E_<(Y/x)-E_<(N/x)|<=log(Y+1)+1

a.e. in x. Strict/open endpoints can alter isolated x only. Consequently

    |S_h(Y)-S_h(N)|<=C_h[log(Y+1)+1].                    (4)

The compact Y range [2,4] is bounded directly. Equations (3)-(4) prove
|S_h(Y)|=O_(h,epsilon)(Y^(1/2+epsilon)) for every real Y>=2. We extend only
this scalar probe, not the whole integer-cell projection to a noninteger
last cell. Thus no unproved fractional-cell convention or continuity of
W_N in N is required.

## 4. Full Mellin continuation and absence of zero-mode cancellation

For Re s>1, absolute convergence of the Euler product and its logarithmic
derivative gives the exact all-prime-power Mellin identity

    D_E(s):=integral_1^infinity E_<(y)y^(-s-1)dy
          =-(1/s) zeta'(s)/zeta(s)-1/(s-1).              (5)

Indeed integrating each step 1_(q<y) gives q^(-s)/s. Proper powers in
Lambda are exactly the logarithmic-derivative coefficients; excluding
them would invalidate (5). The standard Euler product/meromorphic zeta
normalization was checked against [NIST DLMF 25.2](https://dlmf.nist.gov/25.2),
and (5) itself is derived here. At s=1 the main pole cancels: zeta has a
simple pole of residue one, so the right side is analytic there.

Set

    M_h(s)=integral_2^infinity S_h(Y)Y^(-s-1)dY.

Under (3)-(4), M_h is holomorphic on Re s>1/2. On any compact subregion use
epsilon smaller than its distance to the line 1/2; the same tail domination
allows s derivatives with additional log factors. For Re s>1, Fubini and
Y=xy give

    M_h(s)=H_h(s)D_E(s)-J_h(s),
    J_h(s)=integral_1^2 conjugate(h(x))x^(1/2-s)
              integral_1^(2/x) E_<(y)y^(-s-1)dy dx/x.    (6)

J_h is entire: its y range is a fixed compact subset of [1,2], where E is
bounded; no infinite tail or missing atom is in this head correction.
Meromorphic continuation and the identity theorem extend (6) throughout
Re s>1/2. This uses no explicit zero-series interchange or isolated-mode
asymptotic assumption.

Suppose a nontrivial zero rho has Re rho>1/2 and multiplicity m_rho>=1.
The right side of (5) has residue -m_rho/rho at rho. We can choose one
fixed smooth zero-mean h with H_h(rho)!=0: otherwise the smooth zero-mean
tests would all annihilate x^(1/2-rho), making that function constant on
(1,2) as a distribution. It is not constant because rho!=1/2. Equivalently
take two sufficiently narrow weighted-mean-normalized bumps at points
where x^(1/2-rho) differs, and subtract them. Such h may be chosen after
the purported zero, but remains fixed in N; the all-source norm bound
applies to it.

For this h, (6) has the nonzero residue

    Res_(s=rho) M_h(s)=-m_rho H_h(rho)/rho,              (7)

contradicting holomorphy. Other zeros occur at different s and cannot
cancel this local pole; multiplicity increases its residue rather than
removing it. The entire head term cannot cancel it. Conjugate zeros are
not identified or thrown away. Thus there are no zeros to the right of
1/2. The ordinary completed-zeta functional equation and reality then
exclude zeros to the left, proving RH. Its nontrivial-zero symmetry and
unchanged multiplicities are the standard ordinary-zeta facts in
[NIST DLMF 25.4](https://dlmf.nist.gov/25.4) and
[25.10(i)](https://dlmf.nist.gov/25.10#i).

This argument handles every possible nontrivial zero at every height. It
does not require a zero attaining the rightmost supremum, simple zeros,
a zero gap, absence of conjugates, or a common probe nonvanishing at all
zeros. It proves an implication of the bound without claiming that an
off-critical zero actually exists.

## 5. RH forward direction: consume the strongest paid old energy

Projection is contractive, and substitution y=N/x in the original norm
gives the exact unprojected comparison

    ||W_N||^2
      <= [N/(M-U_M)] integral_1^N |E_<(y)|^2 y^(-2)dy.  (8)

The prefactor is at most 2 for every N>=4. Old 068's actual prefix-flow
theorem under RH gives

    integral_1^N |psi(y)-floor y|^2 y^(-2)dy=O(log N).

The difference from E_<(y) is y-floor y a.e., whose full weighted squared
norm is at most integral_1^infinity y^(-2)dy=1. Minkowski therefore gives
the same O(log N) bound for the integral in (8), proving

    RH => ||W_N||=O(sqrt(log N)), all integers N>=4.     (9)

This uses 068 sections 3 and 5, with 070's uniform local-energy proof as
the stronger original RH input; it is an inherited conditional theorem,
not a new arithmetic source. The strong old (9) is the relevant baseline
and is not weakened merely to make a new polylog target seem novel.

Together (3)-(7) and (9) prove the equivalences at the start. In particular
a finite polylog bound implies the every-epsilon subpower bound, and RH
already supplies a finite polylog exponent. A specified uniform bound or
smaller exponent has only the reverse implication established here.

## 6. Exact scope, old-equivalence subtraction and stop recommendation

The all-integer projected critical/subpower norm is not weaker than RH.
The zero-mean filter removes a cell constant but does not erase the
ordinary zeta poles from all smooth detail probes. Sections 3-4 give the
full-spectrum reason; a single off-critical mode example alone would not
have proved this statement.

Old 068/069 already identify critical subpower arithmetic energy with RH;
old 070 supplies RH local-energy control; old 521/522 identify the original
source-quotient subexponential growth with RH without providing it
independently. The current canonical same-source representation is useful
for locating the native arithmetic responsibility, but its critical norm
cannot be assumed as a new independent input. Paying the separate Gamma
norm or the already bounded carry corrections does not pay (1).

This audit supplies no new arithmetic inequality, zero-free optimization,
whole-count improvement, PSD/nearPSD conclusion or ordinary Xi spectral
identification. It does not exclude changing the head/source, a genuinely
new signed joint mechanism, noncanonical geometry, or a quantitatively
weaker independent arithmetic theorem. No such new source is provided
here, and no stronger conditional polylog regularity is pursued to extend
an old-equivalence contract.

Recommendation: C019's critical-input route should stop at entry with zero
new mathematical rounds, retain the exact source and this independent
full-spectrum scope audit as evidence, and perform the required strategy
review before selecting another actual input. The global Goal remains
open; recovery, representation, equivalence, stop and push do not complete it.

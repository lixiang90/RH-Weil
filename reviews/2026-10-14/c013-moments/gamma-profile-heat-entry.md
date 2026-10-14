# Actual Gamma / exact arithmetic degree profile: heat-trace entry for the next contract

2026-10-14. Owned by \`/root/c013_growth_measure\`; root requested preparation only.
Recovered AGENTS, README/STATE, check/show, Goal/frontier/C013/D20261014N;
current STATE still C013 ready while root settles 542. This file changes no
STATE/cadence/Git, and does not register a new iteration or complete a Goal.
Subagent get_goal again returned null; it does not override root's active Goal.

## 1. Admission conclusion and strongest old comparison

The exact profile can be transported through the **Gamma-only** positive jump
semigroup, without asserting positivity of the complete Weil semigroup:

\[
n_-(Q_L)\le1+C_\Gamma(s)\int_{-L}^L e^{sD_L(u)}\,du,\qquad s>1,
\quad
C_\Gamma(s)=\frac1{2\pi}\int_{\mathbb R}e^{-s\Gamma(t)}dt. \tag{1}
\]

Below the zero-extension domain, killed-kernel domination, bounded-potential
Trotter limit, trace finiteness and original odd-pole +1 are supplied directly.
In particular, no unchecked general Golden--Thompson label substitutes for
those premises. The generic trace mechanism and record selection are tools;
neither is claimed new by itself.

The strongest consumed old scalar baseline is 028 §1, with exact degree
maximum \(M_L=\operatorname{ess\,sup}D_L\):

\[
n_-(Q_L)\le
1+\frac L\pi\int_{\mathbb R}[M_L+1-\Gamma(t)]_+dt
=O(Le^{M_L}+LM_L). \tag{2}
\]

This is stronger than the phase-volume bound \(O(LS_Le^{S_L})\). Using standard
PNT only in this old comparison, \(M_L=S_L\) for all sufficiently large L:
near the endpoint the short side is empty; beyond distance log 2 from it the
long side is at most \(A(X/2)\), and the short side at most \(A(\sqrt X)\),
whose sum is eventually smaller than \(A(X)\). Thus the old budget is
\(O(Le^{S_L})\). Compare a new result with (2), never only with the weaker
\(2S_L\) or \(LS_Le^{S_L}\) ledgers.

An independently checked **record-window escape** below uses only elementary
Chebyshev growth, retains the strict cutoff at the record's own primepower n,
and gives the candidate cofinal bound

\[
n_-(Q_{L_n})\le1+C e^{S_{L_n}},\qquad L_n=\tfrac12\log n\to\infty. \tag{3}
\]

The constant is absolute. This saves the factor L of the old scalar budget
on this cofinal actual family. It does not establish positivity, restrict the
final negative core, identify Xi or independently pass the macro Goal gate.
This is entry preparation pending root reconciliation and a separate reverse
audit; (3) must not silently become an all-L assertion.

## 2. Actual form, all arithmetic atoms and exact profile

Write \(I=(-L,L)\), \(X=e^{2L}\), \(w_n=\Lambda(n)/\sqrt n\),
and \(A(Z)=\sum_{2\le n<Z}w_n\). Only actual primepowers have nonzero w.
The old 016 completed-square identity, in actual Gamma normalization, is

\[
Q_L(f)=q_{\Gamma,I}(f)+
\sum_{n<X}w_n E_{\log n}(f)
-\int_I D_L(u)|f(u)|^2du
+2|C(f)|^2-2|S(f)|^2, \tag{4}
\]

where \(E_a(f)=\int_{-L}^{L-a}|f(u+a)-f(u)|^2du\ge0\),
\(C(f)=\int_I f(u)\cosh(u/2)du\), \(S(f)=\int_I f(u)\sinh(u/2)du\), and

\[
D_L(u)=A(e^{L-u})+A(e^{L+u})\quad\text{a.e. on }I. \tag{5}
\]

Finite endpoint conventions have no effect on the form/essential supremum.
The form \(q_{\Gamma,I}\) uses zero extension and the full multiplier
\(\Gamma(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi=2\theta'(t)\).
Both actual poles remain in (4); only the nonnegative graph and even pole
will be dropped for the spectral upper comparison.

For a finite-window certificate no asymptotic replacement of D is needed.
Sort the distinct breakpoints

\[
0,\ L,\ |\log n-L|\quad(n<X,\ \Lambda(n)>0)
\]

within [0,L]. If these are \(0=x_0<\cdots<x_m=L\), choose any
\(v_j\in(x_j,x_{j+1})\), and put

\[
D_j=\sum_{n<X}w_n
\bigl({\bf1}_{\log n<L-v_j}+{\bf1}_{\log n<L+v_j}\bigr).
\]

Then the exact finite profile integral is

\[
\mathcal H_L(s)=\int_I e^{sD_L(u)}du
=2\sum_{j=0}^{m-1}(x_{j+1}-x_j)e^{sD_j}. \tag{6}
\]

It contains every proper power. If D is nonconstant a.e., this is strictly
smaller than \(2Le^{sM_L}\) for each fixed s>0. That internal improvement over
the scalar **heat** budget alone is insufficient: actual admission compares
the full right side of (1) against the stronger old bound (2).
Errors in D are multiplied by s in the exponent. In particular, PNT profile
\(D=D_{\rm main}+o(S)\) cannot be consumed as a \(1+o(1)\) exponential error.

## 3. Full Gamma positive jump, closed domain and density

Let \(\Gamma_0=\Gamma(0)=-\gamma-\pi/2-3\log2-\log\pi<0\) and
\(\Phi(t)=\Gamma(t)-\Gamma_0\). The exact 541/NIST digamma integral gives

\[
\Phi(t)=\int_0^\infty w(a)(1-\cos ta)\,da,\qquad
w(a)=\frac{2e^{-a/2}}{1-e^{-2a}}>0. \tag{7}
\]

This follows from the
[NIST digamma integral](https://dlmf.nist.gov/5.9#E16), with no Gamma tail
cutoff. The symmetric Levy measure is
\(\nu(da)=w(|a|)\,da/2\); its small-jump second moment and its total large-jump
mass are finite. Its full quadratic form is

\[
\mathcal J(f)=\frac12\int_0^\infty
w(a)\|T_a f-f\|_{L^2(\mathbb R)}^2 da
=\frac1{2\pi}\int_{\mathbb R}\Phi(t)|\widehat f(t)|^2dt. \tag{8}
\]

It is closed and nonnegative, with domain the weighted Fourier L² space.
Binet/recurrence give \(\Phi(t)=\log(2+|t|)+O(1)\) up to fixed constants
and a bounded low-frequency contribution, so its graph norm is the actual
Dlog norm. Normal real contractions reduce (8), since they reduce each
pointwise squared difference. In particular the form is Markovian.

Restrict the full form to functions vanishing a.e. outside I. This is a closed,
densely defined form on \(L^2(I)\); call its operator \(A_I\ge0\). The Gamma
operator is \(\Gamma_I=\Gamma_0 I+A_I\).
Cc∞(I) is a form core: shrink a zero-extended source by a dilation r<1 to
leave a positive boundary margin, then mollify inside the margin. Dilation
is strongly continuous in the weighted Fourier norm as r→1 (first compact
Fourier truncation, then use the logarithmic weight's uniform dilation bound);
mollification converges by dominated convergence of its bounded Fourier
multiplier. Both steps preserve eventual interior support. Thus this
restriction is the actual zero-extension Dlog form, not a stronger boundary
Sobolev domain selected to gain positivity.

For clarity, the full free semigroup has a nonnegative density \(p_s\) for
every s>0, including s≤1 where that density need not be bounded. One direct
construction is to truncate ν at small jumps, form compound-Poisson laws,
and let the truncation vanish. The uniformly bounded second moments give
tightness; characteristic functions converge to \(e^{-s\Phi(t)}\), a
continuous function at zero. The resulting probability measures are unique
and satisfy convolution composition.

Density follows by extracting the positive Levy submeasure

\[
\nu_0(da)=\frac{e^{-|a|/2}}{2|a|}da\le\nu(da),
\quad
\Phi_0(t)=\tfrac12\log(1+4t^2).
\]

Its law at time s is the difference of two independent Gamma(s/2, scale 2)
variables, so it has an L¹ density; convolution with the residual law gives
an L¹ density for the full law. For s>1,
\(e^{-s\Phi(t)}\le(1+4t^2)^{-s/2}\in L^1(dt)\), so \(p_s\) is bounded and
continuous, and

\[
p_s(0)=\frac1{2\pi}\int e^{-s\Phi(t)}dt,\qquad
0\le p_s(x)\le p_s(0). \tag{9}
\]

The integral is finite exactly for s>1, by the actual log asymptotic.
No unjustified pointwise kernel bound at s/n≤1 is used below.

## 4. Killed-kernel domination by a direct resolvent comparison

For λ>0 and g≥0, the full and restricted resolvents are positive.
This follows by testing their variational equations on a negative part:
the jump form of a function against its negative part is at most minus
the negative part's own energy, so that part must vanish.

Take g supported in I. Put
\(u=(\lambda+A_I)^{-1}g\), extended by zero, and
\(r=(\lambda+A_{\mathbb R})^{-1}g\), where
\(A_{\mathbb R}=\Phi(D)\). Since r≥0, \(h=(u-r)_+\) vanishes outside I.
Normal contraction puts h in the common form domain, and it is an admissible
test for both equations. Subtracting them gives

\[
\lambda\langle u-r,h\rangle+\mathcal J(u-r,h)=0.
\]

But \(\langle u-r,h\rangle=\|h\|^2\) and
\(\mathcal J(u-r,h)\ge\mathcal J(h,h)\), by
\((a-b)(a_+-b_+)\ge(a_+-b_+)^2\). Thus h=0 and u≤r.
Iteration followed by
\(e^{-sA}=\mathrm{s}\!-\!\lim_m(I+sA/m)^{-m}\) gives domination of the
restricted positive semigroup by the full free semigroup.

Consequently \(e^{-sA_I}\) has a symmetric nonnegative measurable kernel
\(r_s(u,v)\) on \(I^2\) satisfying

\[
0\le r_s(u,v)\le p_s(u-v)\quad\text{a.e.} \tag{10}
\]

Existence of such a kernel is not a continuity assumption: the bilinear
positive measure on rectangles is dominated by the known finite measure
\(p_s(u-v)\,du\,dv\), so Radon--Nikodym supplies the kernel. This is the
Dirichlet/killed realization of the Gamma jump process in the only sense
needed here. It is distinct from a periodic multiplier or a compression
of the free semigroup at one time.

Already for s>1, \(e^{-sA_I/2}\) is Hilbert--Schmidt:

\[
\iint_{I^2}r_{s/2}(u,v)^2du\,dv
\le2L\|p_{s/2}\|_2^2=2Lp_s(0)<\infty.
\]

Thus \(e^{-sA_I}\) is trace class. This proves trace finiteness rather than
inferring it merely from compact resolvent.

## 5. Bounded-potential Trotter trace proof, including the strong limit

For fixed L, D is a bounded real step function. Set \(H_I=A_I-D\) on
operator domain Dom(AI), and for h=s/n set

\[
F(h)=e^{hD/2}e^{-hA_I}e^{hD/2}.
\]

Then \(\|F(h)^n\|\le e^{s\|D\|_\infty}\), and on Dom(AI),
\((F(h)-I)f/h\to-(A_I-D)f\). No claim that D preserves Dom(AI) is required:
expand the extra term as
\[
e^{hD/2}(e^{-hA_I}-I)(e^{hD/2}-I)f/h,
\]
which tends to zero by strong continuity, since
\((e^{hD/2}-I)f/h\to Df/2\).
The difference quotients are uniformly bounded from the graph norm of AI
to L². Therefore consistency is uniform on each compact graph-norm orbit
\(\{e^{-rH_I}f:0\le r\le s\}\), f in Dom(AI). A telescoping sum of
\(F(s/n)^n-e^{-sH_I}\), with this consistency and the preceding stability,
gives strong convergence on that dense domain and then on all L².
This supplies the bounded-potential Trotter limit directly.

Use only even n=2m. F(h) is a positive selfadjoint operator, so F(h)^n is
the square of F(h)^m. Its trace is the Hilbert--Schmidt norm square of that
half product, given by the positive cyclic kernel integral

\[
\operatorname{Tr}F(s/n)^n
=\int_{I^n}
\prod_{j=1}^n r_{s/n}(u_j,u_{j+1})\,
\exp\!\left(\frac sn\sum_{j=1}^nD(u_j)\right)
\,du_1\cdots du_n,\quad u_{n+1}=u_1. \tag{11}
\]

Tonelli and truncation justify the expression even if a small-time kernel
is unbounded. Finiteness follows from the ensuing estimate, so this is not
assuming the trace property that it must prove.

Scalar Jensen gives
\[
\exp\!\left(\frac sn\sum_jD(u_j)\right)
\le\frac1n\sum_j e^{sD(u_j)}.
\]
Use (10), rotation symmetry of the cyclic product, and extend all integration
variables except u1 to the full line. The full convolution cycle integrates
to \(p_s(0)\), yielding

\[
\operatorname{Tr}F(s/n)^n
\le p_s(0)\int_I e^{sD(u)}du. \tag{12}
\]

For even n the full cycle can be split into two identical half-convolutions;
its value is \(\|p_{s/2}\|_2^2=p_s(0)\). Thus this step does not infer a
possibly noncanonical diagonal from an L¹ kernel at s/n.

All approximating operators are positive selfadjoint. Strong convergence
and the finite-orthonormal-family definition of positive trace give
\[
\operatorname{Tr}e^{-s(A_I-D)}
\le\liminf_{n\to\infty,\ n\ {\rm even}}\operatorname{Tr}F(s/n)^n.
\]
Multiply by \(e^{-s\Gamma_0}\). This proves the exact actual-normalization
profile trace inequality

\[
\operatorname{Tr}e^{-s(\Gamma_I-D)}
\le C_\Gamma(s)\mathcal H_L(s),\qquad s>1. \tag{13}
\]

An AMS fetch of Trotter's original 1959 paper returned 403 during preparation;
it was not treated as a checked proof. The finite-product/strong-limit proof
above is independent of that inaccessible source and of a general GT claim.

## 6. Full complex-source inertia and complete pole

Equation (4) and min--max give
\[
n_-(Q_L)\le n_-(\Gamma_I-D-2|S\rangle\langle S|)
\le n_-(\Gamma_I-D)+1.
\]
The +1 is the full original odd-pole rank, not an assumption that the source
has vanishing odd moment. The actual graph and positive even pole are dropped
only in this monotone comparison. For each negative eigenvalue λ,
\(e^{-s\lambda}>1\); hence \(n_-(\Gamma_I-D)\le
\operatorname{Tr}e^{-s(\Gamma_I-D)}\). Equation (13) proves (1).
The Gamma heat trace is compact for s>1, and bounded D/graph/poles retain
the common actual Dlog domain and compact resolvent. These conclusions apply
to all complex sources in that domain, not a finite matrix/core.

The Gamma-only semigroup is positive; the complete Q semigroup has not been
asserted positive. The old [529](../../../notes/529-full-weil-positive-cone-semigroup-boundary.md)
standard-cone obstruction is therefore neither contradicted nor reopened.

## 7. Exact heat endpoint and why an all-L shortcut would be unpaid

The actual Binet/recurrence bound gives
\(\Gamma(t)=\log(|t|/(2\pi))+\epsilon(t)\),
\(|\epsilon(t)|\le A/|t|\) for |t|≥1 with an absolute A (A=7 suffices).
For 1<s≤2, the complete |t|≥1 integral differs by O(1), uniformly in s,
from \((2\pi)^s/[\pi(s-1)]\); the |t|≤1 part is uniformly bounded.
Thus, retaining both low and high frequency parts,

\[
C_\Gamma(1+\eta)=2/\eta+O(1)\quad(0<\eta\le1). \tag{14}
\]

This includes the residue 2 from the actual Gamma and both signs of t.
Neither a half-Gamma multiplier nor a one-sided integral gives the same gate.

There is a useful negative control for a proposed all-L claim. Let \(n_*\)
be the largest actual primepower below X and
\[
h_L=\min\{\log2,\ \log(X/n_*)\}>0.
\]
On the two endpoint intervals of length h, the short side has no atom and
the long side includes all n<X, so D=S exactly. Therefore
\[
\mathcal H_L(s)\ge2h_Le^{sS_L}. \tag{15}
\]
For 1<s≤2, the tail Gamma upper bound gives
\(C_\Gamma(s)\ge c_1/(s-1)\); for s≥2, a fixed neighborhood where Γ≤0
gives \(C_\Gamma(s)\ge c_2>0\). Consequently, for S≥1,
\[
\inf_{s>1}C_\Gamma(s)\mathcal H_L(s)
\ge c\,h_LS_Le^{S_L}. \tag{16}
\]
Indeed \(e^{\eta S}/\eta\ge eS\) for η>0, and for η≥1 use \(e^{\eta S}\ge S\).
Thus global PNT alone cannot erase endpoint plateaus in an exponential
profile estimate. The naive all-L transport would still need a relevant
near-X arithmetic gap control. This is only an admission warning, not a
proof that the actual gaps violate it.

The record construction below deliberately pays a different cofinal
arithmetic quantifier; it does not manufacture a global short-interval theorem.

## 8. Independently checked actual-record escape, with ≤ / < endpoints

Let
\[
A_\le(x)=\sum_{n\le x}\Lambda(n)/\sqrt n.
\]
The binomial-coefficient Chebyshev proof in the independent C013 derivation
gives \(\Psi(x)\ge(\log2)x/2\) for x≥16. Consequently
\(A_\le(x)\ge c_0\sqrt x\), with \(c_0=\log2/2\).
Fix \(\kappa=c_0/2=\log2/4>0\), and set
\[
F(x)=A_\le(x)-\kappa\sqrt x.
\]
F is unbounded above, and strictly decreases between the actual primepower
jumps. Therefore there are arbitrarily large **strict historical record**
primepowers n, satisfying \(F(n)\ge F(x)\) for every x≤n.
This gives the cofinality needed for \(L_n=(\log n)/2\to\infty\).

For every real y≤n, take the left limit at y in the record inequality:
\[
A_\le(n)-A_<(y)\ge\kappa(\sqrt n-\sqrt y). \tag{17}
\]
The strict-cutoff actual window is X=n. It includes n'<n and excludes n
itself:
\[
S=A_<(n)=A_\le(n)-w_n,\quad
w_n=\Lambda(n)/\sqrt n\le\log n/\sqrt n\to0. \tag{18}
\]
No atom has been added to the original form to align the record convention.

Parameterize the positive half-window by u=L−r, 0<r<L. For 0<r<log2,
the exact short side is empty, so (5), (17) and (18) give
\[
D_L(L-r)=A_<(ne^{-r})
\le S+w_n-\kappa\sqrt n(1-e^{-r/2}). \tag{19}
\]
On this range \(1-e^{-r/2}\ge r/(2\sqrt2)\). For log2≤r≤L,
the short side is at most \(A_\le(\sqrt n)\le C_0n^{1/4}\) by elementary
Chebyshev partial summation, while the record lower drop is at least
\(\kappa(1-2^{-1/2})\sqrt n\). Thus for all sufficiently large record n
\[
D_L(L-r)\le S-c\sqrt n,\qquad
c=\tfrac12\kappa(1-2^{-1/2})>0. \tag{20}
\]
This uses a long-side *record* lower bound, not a uniform PNT approximation
within a square-root-length interval.

Integrating the two exact regions and doubling by symmetry yields, for every
s>1 and every sufficiently large actual record n,
\[
\mathcal H_{L_n}(s)\le
\frac{4\sqrt2}{s\kappa\sqrt n}e^{s(S+w_n)}
+2L_n e^{s(S-c\sqrt n)}. \tag{21}
\]

All constants are independent of the record, s and L. Only the cutoff atom
w is charged; its fee tends to zero rather than an unquantified o(S) exponent.
Elementary Chebyshev also gives \(S\asymp\sqrt n\). Choose analytically
\[
s_n=1+1/S.
\]
Then (14), (18) and (21) give
\[
C_\Gamma(s_n)\mathcal H_{L_n}(s_n)
\le C e^S+
O\!\left(L_nS\,e^{S+1-c\sqrt n}\right)
\le C'e^S. \tag{22}
\]
For the boundary term the factor \(C_\Gamma(s_n)/(s_n\sqrt n)\) is bounded,
and \(s_n(S+w_n)=S+1+o(1)\). The interior remainder vanishes relative to e^S.
Equations (1) and (22) prove the candidate (3) on a cofinal actual family.
No PNT, zero-location input, growing precision scan or fitted spectral data
is used for this record family.

This method does not assert every growing window is a record; intermediate
nonrecord windows cannot inherit (17). Cofinal form domains are enough for
the stated family, but the exponential index allowance remains enormous.

## 9. Baseline deduction, source adaptation and entry status

The record tool is not new. I read [275](../../../notes/275-record-envelope-and-growing-low-frequency-closure.md)
§§1–2: its source is \(\psi(x)-x\), its record is
\(|R(n)|/n^\beta\), its large mass is supplied by Littlewood oscillation, and
its consequence is a Vaughan--Brownian weighted discrepancy response.
Here the source is the positive exact \(A_\le(x)\), the record is
\(A_\le(x)-\kappa\sqrt x\), and the consequence is the actual D-profile
whole-Weil inertia via the original Gamma kernel. The finite record-selection
idea is inherited; the domains, weights, signs, full Gamma/pole transport
and claimed output differ. This is a targeted object audit, not an assertion
of global/world novelty or of having reread every ≤538 page.

The new candidate is a source-independent cofinal arithmetic choice of L,
followed by an all-complex-source spectral bound for each chosen L. It does
not adapt L to the unknown spectrum or to a source f. Variations in s and
step-profile error must be charged in (6)/(13)/(21), not optimized by a
finite grid and promoted to all-parameter claims.

Before consumption as a complete C014 iteration, root should independently
audit (10)–(13), the strict record cutoff atom in (18), and the strongest
scalar baseline (2), and settle the actual net consequence in a note.
Current file is **zero-round preparation**. The stable macro Goal keeps
its original full gate; a polynomial factor improvement in a huge permitted
negative index does not by itself erase the growth positivity/Xi bottleneck.
No scientific process or numerical certificate is pending.

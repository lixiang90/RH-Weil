# C014 independent audit: arithmetic records, strict cutoffs and spatial profile

2026-10-14. Owned output of `/root/c014_records_core`.
Recovered AGENTS, README/STATE, `research_state.py check/show`, the current Goal,
frontier, C014 and D20261014O, and checked the actual working tree. Observed
HEAD was `d8894ce35b45b793f510fb62891e533f7fed668d`; the tree initially had no
changes. The subagent's `get_goal` returned null, which is not a root Goal
observation. No scientific producer or numerical certificate is used here.
This audit changes neither STATE nor cadence nor Git and consumes no separate
research round.

## 1. Verdict and dependencies

The arithmetic/profile part of
[the entry draft](../c013-moments/gamma-profile-heat-entry.md), §§6–9, passes.
Its actual-source record family and endpoint fee give, for all sufficiently
large members of a cofinal family of actual primepowers n,

\[
\mathcal H_{L_n}(s)\le
\frac{4\sqrt2}{s\kappa\sqrt n}e^{s(S+w_n)}
+2L_n e^{s(S-c\sqrt n)},\qquad s>1,                         \tag{1}
\]

where the quantities are those of the original strict-cutoff Weil object:

\[
L_n=\tfrac12\log n,\quad X=n,\quad
S=A_<(n),\quad w_n=\Lambda(n)/\sqrt n,
\quad \kappa=\log2/4,\quad
c=\tfrac12\kappa(1-2^{-1/2})>0.
\]

The independently paid Gamma endpoint calculation below gives
\(C_\Gamma(1+1/S)=2S+O(1)\). Thus

\[
C_\Gamma(1+1/S)\mathcal H_{L_n}(1+1/S)\le C e^S.          \tag{2}
\]

If the separate killed-Gamma domain/kernel/Trotter trace audit pays the
actual full-source bridge
\(n_-(Q_L)\le1+C_\Gamma(s)\mathcal H_L(s)\), then (2) yields
\(n_-(Q_{L_n})\le1+C e^{S_{L_n}}\). This audit does not treat that bridge
as proved merely because it appears in the entry draft. The +1 must remain
the actual odd-pole rank and all sources must remain complex in the original
zero-extension Dlog domain.

The improved quantity is an upper spectral budget. It gives no negative
eigenvalue, no lower bound on the actual count, no full positivity, and no Xi
identification. The cofinal quantifier does not become an all-L quantifier.
The macro Goal's growth positivity/identification gate remains separate.

## 2. Elementary arithmetic estimates, independently reconstructed

Let \(\Psi(x)=\sum_{m\le x}\Lambda(m)\). For an integer q≥1, the valuation of
the central binomial coefficient is

\[
v_p\binom{2q}{q}=\sum_{j\ge1}
\bigl(\lfloor2q/p^j\rfloor-2\lfloor q/p^j\rfloor\bigr).
\]

Every summand is 0 or 1. Hence
\(\log\binom{2q}{q}\le\Psi(2q)\). Every primepower in (q,2q] contributes
one of these carries, so also

\[
\Psi(2q)-\Psi(q)\le\log\binom{2q}{q}\le2q\log2.
\]

The central term is the largest of the 2q+1 binomial coefficients and their
sum is \(4^q\). Consequently
\(\log\binom{2q}{q}\ge2q\log2-\log(2q+1)\).
For real x≥16 choose q=⌊x/2⌋. Monotonicity gives

\[
\Psi(x)\ge(x-2)\log2-\log(x+1)\ge(\log2)x/2.             \tag{3}
\]

For the last inequality, its difference is positive at x=16 and its
derivative \((\log2)/2-1/(x+1)\) is positive thereafter. Summing the upper
binomial estimate on dyadic arguments gives
\(\Psi(2^j)\le2(\log2)2^j\); enlarging x to the next dyadic point gives

\[
\Psi(x)\le C_\psi x\quad(x\ge1),\qquad C_\psi=4\log2.    \tag{4}
\]

For \(A_\le(x)=\sum_{m\le x}\Lambda(m)/\sqrt m\), the lower bound is immediate:
\(A_\le(x)\ge\Psi(x)/\sqrt x\). Stieltjes partial summation and (4) give

\[
A_\le(x)=\frac{\Psi(x)}{\sqrt x}
+\frac12\int_1^x\Psi(t)t^{-3/2}dt
\le2C_\psi\sqrt x.
\]

Therefore, with \(c_0=(\log2)/2\) and \(C_0=2C_\psi=8\log2\),

\[
c_0\sqrt x\le A_\le(x)\le C_0\sqrt x\quad(x\ge16),       \tag{5}
\]

with the upper estimate valid already for x≥1. All proper powers are
included; no prime-only approximation or PNT enters (3)–(5).

## 3. Cofinal strict records and the all-real-y quantifier

Define \(F(x)=A_\le(x)-\kappa\sqrt x\) for x≥0, with
\(\kappa=c_0/2\) and F(0)=0. By (5),
\(F(x)\ge(c_0-\kappa)\sqrt x\to\infty\). Between actual primepower jumps,
F strictly decreases. On every bounded prefix its maximum is attained at
0 or at one of finitely many primepowers. Thus there are infinitely many,
and arbitrarily large, primepowers n that make a strict historical record:

\[
F(n)>\max\bigl(0,\{F(m):m<n,\ \Lambda(m)>0\}\bigr).
\]

Such a record satisfies F(n)≥F(y) for every real 0≤y≤n. Taking a left limit
at an arbitrary y∈(0,n] gives

\[
A_\le(n)-A_<(y)\ge\kappa(\sqrt n-\sqrt y).               \tag{6}
\]

The left limit is required when y is itself an actual jump. At y=n this
retains the excluded boundary atom rather than claiming it absent. At y=0
the same inequality follows directly from the record condition at 0.

The family depends only on the actual positive arithmetic sequence and
the frozen constant κ. It does not depend on any source f or unknown
spectral data. To certify a proposed strict record in a finite prefix one
checks every earlier primepower value and 0; monotonicity between jumps
then pays the continuum quantifier. Strict finite comparisons have positive
margins and can be interval-certified. No uniform fixed precision,
polynomial runtime, or numerical sample is asserted. Cofinality is analytic.

This record mechanism is a generic selection tool, not a novelty claim by
itself. The old [275](../../../notes/275-record-envelope-and-growing-low-frequency-closure.md)
uses a different discrepancy source and normalized absolute record. Its
record-selection idea is inherited; it is not automatically the actual
positive A-profile input in (6).

## 4. Original strict cutoff and the exact step ledger

Use the original window X=n, not a modified window containing the record
atom. Then

\[
S=A_<(n)=A_\le(n)-w_n,\qquad
0<w_n=\Lambda(n)/\sqrt n\le\log n/\sqrt n\longrightarrow0. \tag{7}
\]

Here Λ(n)=log p when n=p^j; replacing it by log n merely enlarges the
error fee and does not delete proper powers. The complete-square identity
in old [016](../../../notes/016-prime-graph-hodge-inequality.md) gives, a.e.,

\[
D_L(u)=A_<(e^{L-u})+A_<(e^{L+u}).                         \tag{8}
\]

The original degree indicators can use closed endpoints; their difference
from (8) occurs at only finitely many u and has zero Lebesgue measure.
This does not change the form, essential maximum, or profile integral.

For completeness, all jumps of (8) on [0,L] occur among
\(0,L,|\log m-L|\) with actual m<X. Sort the distinct points as
\(0=x_0<\cdots<x_q=L\). The value D_j on each open cell is exactly

\[
D_j=\sum_{m<X}\frac{\Lambda(m)}{\sqrt m}
\left({\bf1}_{\log m<L-v_j}+{\bf1}_{\log m<L+v_j}\right),
\quad v_j\in(x_j,x_{j+1}).
\]

Symmetry and cell constancy give the exact finite ledger

\[
\mathcal H_L(s)=2\sum_{j=0}^{q-1}(x_{j+1}-x_j)e^{sD_j}.   \tag{9}
\]

Neither missed repeated atoms nor any interpolation error occurs in (9).
Near-integer rounding of floating cutoffs is not a substitute for this
actual-cell expression. A profile error δD would cost \(e^{s\delta D}\);
an unspecified PNT o(S) cannot be converted to a vanishing exponent fee.

## 5. Boundary layer, interior and all-s integration

Put u=L−r on the positive half-window. Then 0<r<L,
\(e^{L-u}=e^r\), and \(e^{L+u}=ne^{-r}\).
For 0<r<log2 the short-side sum is empty. Apply (6) to the long side:

\[
D_L(L-r)\le S+w_n-\kappa\sqrt n(1-e^{-r/2}).             \tag{10}
\]

On this interval the derivative of \(1-e^{-r/2}\) is at least
\(1/(2\sqrt2)\), hence \(1-e^{-r/2}\ge r/(2\sqrt2)\).
For log2≤r≤L, the short side is at most
\(A_\le(\sqrt n)\le C_0n^{1/4}\), and the long-side drop in (10) is at least
\(a_0\sqrt n\), where \(a_0=\kappa(1-2^{-1/2})\).
Since \(w_n+C_0n^{1/4}\le(a_0/2)\sqrt n\) for all sufficiently large n,

\[
D_L(L-r)\le S-c\sqrt n\quad(\log2\le r\le L),
\qquad c=a_0/2.                                        \tag{11}
\]

The eventual threshold is independent of the record and s and can be
paid by the explicit inequality just stated. In particular it is not a
nonuniform short-interval PNT assumption.

Double the positive half and integrate (10) with its linear bound,
enlarging that boundary integral to [0,∞). The result is
\(4\sqrt2 e^{s(S+w_n)}/(s\kappa\sqrt n)\).
The interior contribution from (11) is at most
\(2L e^{s(S-c\sqrt n)}\). This proves (1), uniformly for every s>1.
The equality-point conventions r=log2 and r=L have no integral cost.

Chebyshev and the subsum up to n/2 give, for n≥32,

\[
(c_0/\sqrt2)\sqrt n\le S\le C_0\sqrt n.                 \tag{12}
\]

These bounds hold for all sufficiently large n, not only records, and
do not confuse A_< with A_≤ at the selected window endpoint.

## 6. Independently paid Gamma endpoint, including both frequency signs

Only the scalar Gamma endpoint is audited here, not the heat-domain bridge.
The [NIST Binet digamma formula](https://dlmf.nist.gov/5.9#E15), inspected
at its formula and Re z>0 condition, is

\[
\psi(z)=\log z-\frac1{2z}
-2\int_0^\infty\frac{v\,dv}{(v^2+z^2)(e^{2\pi v}-1)}.
\]

For t≥1 choose z=5/4+it/2 and use recurrence to reach 1/4+it/2.
The denominator modulus is at least \(|\Im z^2|=5t/4\), and
\(\int_0^\infty v/(e^{2\pi v}-1)dv=1/24\), so the integral remainder
is at most 1/(15t). The two reciprocal terms cost at most 1/t and 2/t.
Finally

\[
0\le\log|z|-\log(t/2)
=\tfrac12\log(1+25/(4t^2))\le25/(8t^2).
\]

Therefore the actual multiplier, without halving, satisfies

\[
\Gamma(t)=\log(|t|/(2\pi))+\varepsilon(t),\qquad
|\varepsilon(t)|\le7/|t|\quad(|t|\ge1).                 \tag{13}
\]

For 1<s≤2, the difference between \(e^{-s\varepsilon(t)}\) and 1 is at
most \(14e^{14}/|t|\). Both tails then give

\[
C_\Gamma(s)=\frac{(2\pi)^s}{\pi(s-1)}+O(1),
\qquad 1<s\le2,                                        \tag{14}
\]

uniformly in s. Indeed the error integrates against \(t^{-s-1}\),
and the compact-frequency contribution is uniformly finite by continuity
of Γ on [−1,1]. Expanding only the explicit factor \((2\pi)^s\), with
η=s−1, gives

\[
C_\Gamma(1+\eta)=2/\eta+O(1)\quad(0<\eta\le1).           \tag{15}
\]

The residue 2 comes from the actual Γ normalization and both tails; it is
not optional. For the frozen choice s=1+1/S, (12), (15), and (7) give
\(C_\Gamma(s)=2S+O(1)\),
\(s(S+w_n)=S+1+o(1)\), and a uniformly bounded
\(C_\Gamma(s)/(s\sqrt n)\).
The second term of (1), after multiplication by CΓ, divided by e^S is
\(O(LS e^{1-c\sqrt n})\to0\). This proves (2) without scanning or optimizing s.

## 7. All-L plateau warning and the record's paid escape

For an arbitrary actual window with S≥1 let n_* be the last primepower
strictly below X, and put
\(h=\min(\log2,\log(X/n_*))>0\).
For 0<r<h, the small cutoff e^r is below 2, while the long cutoff
Xe^{-r} is above n_*. Thus D=S on both endpoint intervals, and

\[
\mathcal H_L(s)\ge2h e^{sS}.                            \tag{16}
\]

From (13), \(C_\Gamma(1+\eta)\ge c_1/\eta\) for 0<η≤1.
For s≥2, continuity and Γ(0)<0 supply a fixed interval on which Γ≤0,
and hence \(C_\Gamma(s)\ge c_2>0\). Since
\(e^{\eta S}/\eta\ge eS\) and, for η≥1, \(e^{\eta S}\ge S\),

\[
\inf_{s>1}C_\Gamma(s)\mathcal H_L(s)\ge c h S e^S.        \tag{17}
\]

This controls the same heat upper-budget mechanism for every temperature,
including arbitrary varying s(L)>1. A proposed uniform Ce^S budget from
this mechanism would need a uniform bound on hS. Global PNT alone does not
state that near-X gap condition. Equation (17) does not prove that actual
primepower gaps violate it, that the actual count is large, or that another
estimate retaining positive graph/poles cannot improve the budget.

At the selected record X=n, (10) instead pays this plateau. If h denotes
the actual preceding-atom plateau, then taking r↑h in (10) yields

\[
\kappa\sqrt n(1-e^{-h/2})\le w_n.
\]

For large records h<log2 and hence

\[
h\le\frac{2\sqrt2\,w_n}{\kappa\sqrt n}
\le\frac{2\sqrt2\log n}{\kappa n}.                      \tag{18}
\]

Thus the record family genuinely pays its endpoint width; it does not
silently erase the plateau. This is a cofinal consequence of the record
guard, not a new all-window short-interval theorem.

## 8. Same-object old budget comparison and consumption limits

At every finite window the endpoint plateau implies \(M=\operatorname{ess\,sup}D\ge S\).
For large records, (10)–(11) give M≤S+w_n. Therefore
\(M=S+o(1)\) on this family without PNT.
The old [028 §1](../../../notes/028-core-renormalized-negative-trace.md)
negative-trace bridge already yields the scalar budget

\[
B_{\rm old}(L,M)=1+\frac L\pi
\int_{\mathbb R}[M+1-\Gamma(t)]_+dt.
\]

For a→∞, (13) gives
\(\int[a-\Gamma(t)]_+dt=4\pi e^a+O(a)\).
To check the error, compare positive parts with
\([a-\log(|t|/(2\pi))]_+\). On |t|≥1 the union of their supports is
contained in |t|≤2πe^{a+7}; the Lipschitz error integrates to O(a) using
7/|t|. The compact-frequency contribution and the omitted log integral
on |t|<1 cost O(a). The exact log integral over both signs is 4πe^a.
Consequently

\[
B_{\rm old}(L,M)=1+4e L e^M+O(L(M+1))
\sim4e L e^S                                             \tag{19}
\]

along the records. Hence the new conditional upper budget in (2),
divided by this exact old scalar upper budget, is O(1/L)→0. This is stronger
than comparing only a weak 2S Fourier ledger or a scalar heat estimate.
It is still a comparison of upper budgets, never a count lower bound.

This audit checks the named 016/027/028/275 assets and the specified
arithmetic/Gamma consumption. It is not a claim of having exhausted every
≤538 asset or established world novelty. Root must reconcile any stronger
old direct consequence before claiming a new net result, and must pay the
separate heat/source-domain proof. Even if the Ce^S bound is consumed, the
allowed negative index remains enormous, so growth PSD and Xi remain unpaid.

## 9. Integer-record boundary: global and formal local temperatures

Root asked for an additional independent stop-boundary check. At record
X=n, the predecessor n_* is an integer with n_*≤n−1. Therefore, for n≥2,

\[
h=\min(\log2,\log(n/n_*))\ge1/n,
\]

because \(\log(n/(n-1))=-\log(1-1/n)>1/n\) and log2≥1/n.
Combine this with (12) and the all-temperature plateau lower bound (17):

\[
\mathcal B_n:=\inf_{s>1}C_\Gamma(s)\mathcal H_{L_n}(s)
\ge c\frac{e^S}{\sqrt n}=c e^{S-L_n}.                    \tag{20}
\]

The record upper bound (2) supplies \(\mathcal B_n\le C e^S\). Since
L_n/S→0, these two estimates prove

\[
\frac{\log(1+\mathcal B_n)}{S}\longrightarrow1.           \tag{21}
\]

Thus arbitrary temperature optimization in this exact positive heat
ledger cannot remove its leading exponential allowance. This statement
is about the upper ledger, not a lower bound on the actual negative index.
It does not say every method paying the positive graph/poles has that
allowance.

The elementary plateau boundary extends even to the following **formal
local positive ledger** for any measurable function s(u)>1:

\[
\mathcal L_n[s(\cdot)]
=\int_{I_n}C_\Gamma(s(u))e^{s(u)D_{L_n}(u)}du.             \tag{22}
\]

The integral may be infinite. On the two endpoint strips D=S, and the
pointwise all-s estimates used in (17) give
\(C_\Gamma(s(u))e^{s(u)S}\ge cS e^S\).
Consequently every such ledger satisfies
\(\mathcal L_n\ge c h S e^S\ge c'e^{S-L_n}\).
The lower bound allows every measurable local temperature, so freezing s
does not cause this obstruction. Conversely a constant s=1+1/S gives
(2), hence the infimum of (22) has the same leading logarithm as (21).

Equation (22) has not been proved to upper-bound any full-source spectral
quantity. It is an algebraic fee ledger with an independently proved
boundary, not a spatial bracketing theorem. A new localization theorem
would have to pay its actual kernel/domain/interface costs before
consumption. Signed graph/pole cancellations, changing the positive
comparison operator, source-aware core evaluation densities, and a
different joint trace mechanism all remain outside this boundary.
This is not a complete method-class exclusion and does not complete
the macro Goal.

No pending process, finite matrix, ζ-zero fit or source-dependent cutoff
enters the audit. The saved next dependency is the independent killed-Gamma
trace audit and strongest-baseline reconciliation; no C014 settlement is
performed by this subagent.

## 10. Final root-note consumption audit, zero additional round

Read root
[note 543](../../../notes/543-full-gamma-heat-arithmetic-records-and-thermal-boundary.md)
in full, concentrating on §§5–7. The reviewed raw-byte SHA256 was
`965a20f403ddd78a88c007dc81bd4e5a1272d26095a471037211cfda83e6ae08`.
AGENTS/README/STATE, check/show, Goal/frontier/C014/D20261014O and actual Git
were recovered again; root was still settling its first C014 iteration,
with HEAD unchanged at `d8894ce35b45b793f510fb62891e533f7fed668d`.
The subagent Goal observation was again null and does not supersede root.

Final arithmetic consumption passes. Root retains every actual primepower,
the original strict cutoff X=n, all-real-y record guard and its left limit,
and the excluded atom fee w_n. Its boundary/interior estimates and exact
profile integration agree with §§2–6 of this audit. The frozen temperature
and full actual-Gamma residue 2 pay the Ce^S bound without a PNT exponent
substitution or a source/spectrum-dependent record choice.

Root strengthened the maximum from the sufficient M≤S+w_n to **M=S**,
without PNT. This is valid: for r<log2 the short side is empty and the
original strict long sum is a subsum of S, so D≤S; for r≥log2 the paid
record drop gives D<S for large records; a positive-width endpoint stripe
has D=S. Thus the essential supremum equals S exactly. This consumes
old 016 together with the record guard and is not a separate new round.

The final old comparison also allows arbitrary δ>0, rather than fixing
δ=1. Since I(a)=4πe^a+O(a+1), its relative error is uniformly o(1) on all
a=M+δ≥M as M→∞. Multiplication by δ^−1 preserves that uniform relative
comparison. Taking the infimum then uses inf e^δ/δ=e and gives
the stated optimized old scalar budget (4e+o(1))L e^S. The new certified
upper budget has ratio O(1/L) to that whole scalar family. This remains a
comparison of upper budgets, not an actual-count lower bound or a claim
that no stronger non-scalar old core asset exists.

Root's §7 consumes the integer-record plateau h≥1/n and the already paid
all-temperature lower bound with the correct direction. It proves the
leading logarithm 1 for the optimized **heat ledger** only. The local
temperature expression is expressly a formal positive ledger, with no
unproved bracketing theorem asserted. The remaining signed graph/pole,
core/evaluation-density, different comparison and geometry escapes are
preserved, and the macro Goal is expressly incomplete.

One scope clarification was sent to root: the predecessor n_* in §7 is
defined only for windows containing an actual atom. The subsequent lower
bound already assumes S≥1, which guarantees this; prefixing the opening
sentence by that same condition makes its definition explicit. This is
a notation/domain clarification and does not affect any record-family
theorem or any proof above. This supplement changes neither root note nor
STATE/cadence/Git and adds zero research rounds.

# Same-presentation mixed sixth-power restoration and remaining cross sum

2026-10-11. Research scratch only. Baseline: authoritative main note 503.
No external repository modified; no Lean run; no result pushed.

**Outcome:** a concrete relative lemma extends the source's exact sixth-power
amplification identity to the actual long inverse / two short plain / once
selected prime product. Its raw Gram has an explicitly computable convolution
coefficient. The complete **same sixth-free ideal class** block costs only
O(H U^epsilon), including unequal ideal columns, all natural zeros and fixed-ray
phases. The different-class signed cross sum remains unbounded. No new count
decrement or zero-free region is claimed.

## 1. Frozen source and interfaces

Source:
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
canonical LF SHA-256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

The actual Hecke characters, ideal counting, natural zero extensions, fixed
masks, finite-ray coefficient classes, smooth calculus and existing moments
remain relative to the paper's explicit imported package R.

Source locations (one-based frozen-file lines):

- 9220--9268: common-sign natural inverse/prime product; marked moment requires
  r+2z < row width and 2r+8z < 3 row width, both with fixed positive margins.
- 12343--12408: raw all-element inverse moment and its scale supremum.
- 12409--12475: exact sixth-power column identity, injectivity and rowwise
  profile/height Sobolev allowance.
- 12500--12586: common natural masks, fixed Theta coefficients and plain
  capacity n1+n2+6 kappa z <= effective width. Note 450 replays the underlying
  proof down to kappa>=37/50 rather than invoking the statement out of range.
- 15113--15169: actual selected slots, whole-slot rounding, common orientation
  and the fact that witness and physical heights need not coincide.
- 7081--7138: full finite Gauss correlation with all collision zeros.
- 8335--8364: quantitative additive Gram for specified ray coefficients,
  including all three terms; no arbitrary convolution-coefficient moment.

The latest separate formalization `docs/proof-status.md` and
`upstream/plain-kappa/README.md` were read. They keep complete four-field
Moments, improved count consumers and actual low/raw-high physical probes
open. The terminal energy and universal plain_marked field do not supply the
new mixed estimate below.

## 2. Actual object and normalization

Fix a real row bin U, physical parameter tuple and common presentation
\[
 \psi_u(n)=\nu(n)\chi_n(u)^{\epsilon_\chi},\quad
 \epsilon_\chi\in\{-1,1\}.
\]
All original zero extensions and the same permitted row-independent puncture
mask are retained. Multiplicativity includes these zero values.

Use the actual normalized annular columns
\[
 M_u(D)=D^{-1/2}\sum_n\mu(n)\psi_u(n)W_L(q_n/D),\qquad
 S_{j,u}(X_j)=X_j^{-1/2}\sum_b\psi_u(b)W_j(q_b/X_j),
\]
and the once-only selected whole-slot product
\[
 Q_u=\prod_{i\in I}Y_i^{-1/2}
 \sum_{p\in\mathcal P_i}a_i(p)\psi_u(p)W_i(q_p/Y_i).
\]
The underlying supports are disjoint before masks, and a_i are the original
row-independent finite-ray combinations after orientation adjustment. No
arbitrary row-dependent prime coefficient is allowed. The detector's two
plain factors may be copies of the same short witness. Their height is not
identified with the long inverse or physical height.

Set Pi_u=M_u S_{1,u} S_{2,u} Q_u. Its normalization is exactly N^(-1/2), where
\[
 N=D X_1 X_2\prod_iY_i.
\]
Equal short scales give N=D X^2 Y. A single physical selected Qi is |I|=1;
the same proof covers the original selected whole-slot product occurring once.

## 3. Lemma: actual mixed restoration through ua^6

Let a be a primary amplifier ideal outside the fixed exclusions and avoiding
all selected underlying prime supports. Put v=ua^6. The row identity is
\[
 \psi_{ua^6}(n)=\psi_u(n)1_{(n,a)=1}. \tag{1}
\]
Here nu(n) stays fixed while the row changes, and chi_n(a^6) is one on units
and zero on nonunits. If u and a share primes both sides vanish on the same
nonunits. All common natural masks and fixed punctures are retained.

Decompose a squarefree inverse index as n=d m with d|rad(a), (m,a)=1.
The exact source identity is
\[
 M_u(D)=\sum_{d\mid\operatorname{rad}a}
 \mu(d)\psi_u(d)q_d^{-1/2}M_{ua^6}(D/q_d). \tag{2}
\]
For a plain index decompose b=h m, where h is supported on rad(a), with
arbitrary valuations, and (m,a)=1. This unique decomposition gives
\[
 S_{j,u}(X_j)=\sum_{h\mid(\operatorname{rad}a)^\infty}
 \psi_u(h)q_h^{-1/2}S_{j,ua^6}(X_j/q_h). \tag{3}
\]
The sum is finite at each fixed X_j because of annular support. W_j stays
the same, with its own height; small-scale empty ranges are retained.

The support exclusion gives Q_{ua^6}=Q_u exactly. Multiplying (2)--(3),
\[
 \Pi_u=\sum_{d,h_1,h_2}\mu(d)\psi_u(dh_1h_2)
 (q_dq_{h_1}q_{h_2})^{-1/2}
 M_{ua^6}(D/q_d)S_{1,ua^6}(X_1/q_{h_1})
 S_{2,ua^6}(X_2/q_{h_2})Q_{ua^6}. \tag{4}
\]
Thus all three original columns remain in one actual presentation.

The absolute coefficient mass is at most
\[
 A(a)=\prod_{p\mid a}(1+q_p^{-1/2})(1-q_p^{-1/2})^{-2}
 \ll_\epsilon q_a^\epsilon. \tag{5}
\]
Separate finitely many small primes into the constant; each remaining prime's
local logarithm is <=epsilon log(q_p). This proves (5). Triangle inequality
and squaring, with preliminary epsilon halved, give
\[
 |\Pi_u|^2\ll_\epsilon q_a^\epsilon
 \sup_{D'\le D,\ X'_j\le X_j}
 |M_{ua^6}(D')S_{1,ua^6}(X'_1)S_{2,ua^6}(X'_2)Q_{ua^6}|^2. \tag{6}
\]

For H=U^B, B>1 fixed, put P=(H/U)^(1/6). Fixed-field counting gives >>P
primary a outside the fixed set. Those sharing a selected support prime number
at most O(P sum_p q_p^(-1))=o(P), because each fixed positive annulus gives
sum_p q_p^(-1)=O(1/log Y_i). Primes of norm>P divide no nonunit amplifier.
Bounded/zero-length slots are absorbed by the original constant convention.
Thus >>P eligible amplifiers remain.

The original valuation-mod-six argument makes (u,a)->ua^6 injective for
sixth-power-free original rows, including units and without (u,a)=1.
Average (6), sum u and apply injectivity:
\[
 \sum_{u\in C}|\Pi_u|^2\ll_\epsilon P^{-1}U^\epsilon
 \sum_{\substack{0<q_v\ll H\\v\ {\rm retained}}}
 \sup_{D'\le D,\ X'_j\le X_j}
 |M_v(D')S_{1,v}(X'_1)S_{2,v}(X'_2)Q_v|^2. \tag{7}
\]
The same inducing-nonexceptional class and fixed masks remain. Passing to all
such rows is a nonnegative majorization; it does not authorize an exceptional
plain positive-slot invocation.

The scale supremum is controlled only if the new raw bound is uniform over
the same finite derivative closure. For instance d/dlogD' replaces W_L by
-W_L/2-y W_L'; derivatives act separately on both short profiles. Rowwise
witness parameters are carried to the uniquely recovered v. Apply the source
finite-parameter Sobolev calculus to the *entire product*, before forming its
fixed-profile Gram. Its cost (1+T1)^A is fixed before the external height
exponent and tail order. No common phase is assumed. (7) itself gives no chi.

## 4. Actual Gram and paid same sixth-free class block

Fix one parameter tuple after this Sobolev reduction and one scale dyad.
Define the row-independent actual coefficient
\[
 c(k)=\sum_{n b_1 b_2\prod_i p_i=k}
 \mu(n)\prod_i a_i(p_i)\,
 W_L(q_n/D')W_1(q_{b_1}/X'_1)W_2(q_{b_2}/X'_2)
 \prod_iW_i(q_{p_i}/Y_i). \tag{8}
\]
Every p_i is in its actual selected support. With N'=D'X'_1X'_2 prod_iY_i,
multiplicativity of the zero-extended character gives
\[
 \Pi_v=N'^{-1/2}\sum_k c(k)\psi_v(k). \tag{9}
\]
This uses no division by a character value.

Let w_H be a fixed nonnegative radial majorant of the actual row ball and set
\[
 K_H(k,l)=\sum_v w_H(v)\psi_v(k)\overline{\psi_v(l)}.
\]
The retained row condition may be kept; dropping it only majorizes the
nonnegative raw energy. For the chosen kernel the exact fixed-profile energy is
\[
 E_{\rm raw}=N'^{-1}\sum_{k,l}c(k)\overline{c(l)}K_H(k,l). \tag{10}
\]
All masks are inside psi. Since |psi|<=1, actual ideal/element counting gives
|K_H(k,l)|<<H. For fixed slot count/profiles, the coefficient (8) is bounded
by a fixed ideal divisor function, hence |c(k)|<<N'^epsilon on q_k asymp N'.
This divisor bound claims no cancellation or fixed prime-density saving.

**Paid lemma.** The whole block with k and l having the same sixth-power-free
ideal part, including k!=l, has absolute contribution
\[
 |E_{\rm same6}|\ll_\epsilon H N'^\epsilon. \tag{11}
\]

**Proof.** Write uniquely k=s a^6 and l=s b^6, where s is sixth-power-free.
For q_s<=C N', fixed-field ideal counting bounds the number of possible a by
O((N'/q_s)^(1/6)), and the number of pairs by O((N'/q_s)^(1/3)).
Summing over all s (enlarging the sixth-free subset),
\[
 \sum_{q_s\le CN'}(N'/q_s)^{1/3}
 \ll N'^{1/3}N'^{2/3}=O(N').
\]
The last weighted sum follows by dyadic ideal counting/partial summation.
Finite units and primary/ray representatives contribute fixed multiplicity.
Use |c|<<N'^epsilon and |K_H|<<H, then divide by exactly N' in (10), and
rename preliminary epsilon. This pays every same-class unequal pair and all
natural zeros. QED.

This is a same sixth-free **ideal class grouping**, not an assertion about the
complete phase-resonant locus. In column direction psi_v(a^6)=nu(a)^6 times
its natural mask need not be one. This is different from row identity (1).
The grouping proof only uses |K_H|<=O(H), so it pays any fixed-ray phase
rather than dropping it. The height/profile tuple is fixed before (8).

## 5. The exact cross term that remains

Put
\[
 {\cal X}_H=N'^{-1}
 \sum_{\operatorname{sixthfree}(k)\ne\operatorname{sixthfree}(l)}
 c(k)\overline{c(l)}K_H(k,l). \tag{12}
\]
It is real by Hermitian symmetry. No shared-prime terms, natural masks,
unequal witness heights, local collision zeros or finite-ray phases are
discarded. By (10)--(11), a new estimate
\[
 {\cal X}_H\ll_\epsilon H U^{1-R-\lambda+\epsilon}(1+T1)^A,
 \qquad 0<\lambda<1-R, \tag{13}
\]
uniform in all restored scales and finite derivative profile tuples, would
supply the desired raw mixed bound; the same6 block is then smaller.

Source 7081 gives exact *Gauss* correlations for a later masked Poisson
treatment, not (13). The raw character kernel in (10) is not silently
identified with that Gauss correlation. Source 8335 concerns a specified ray
coefficient and cannot simply be applied to (8). The marked inverse theorem
allows M*Q, the plain theorem S*S*Q, while (8) contains M*S*S*Q and a long
squarefree Möbius convolution. Replacing it by arbitrary admissible coefficients
is not licensed by either statement. The compiled low-kappa plain energy also
does not supply (13). New transform/cross estimates for this actual coefficient
class remain required.

## 6. Exact target budget, including strict width cost

At note 503's necessary test label take
\[
 B_0=17499/20000,\quad\kappa_0=7499/10000=2B_0-1,\quad
 \delta=19429/50000,\quad x=1/2,\quad\alpha=5/6.
\]
Define c=1/(3kappa0), Dk=5/2-c, Pk=1-c/2, J=(alpha-delta)Dk+delta Pk,
\[
 t=1+\delta Pk/(2J),\quad
 r_S=((2-c)t-(1-c)/2)/Dk,\quad
 m=t-r_S,\quad z=(1-2m)/(6\kappa_0).
\]

| Quantity | Exact | Orientation |
|---|---|---|
| long length t | 9229494722/8209647083 | 1.1242255152614 |
| short inverse r_S | 5875092361/8209647083 | .7156327551724 |
| short plain m | 3354402361/8209647083 | .4085927600891 |
| selected U-length z | 333565000/8209647083 | .0406308574081 |
| reference count R | 136828076410631/205241177075000 | .6666697119976 |
| convolution length t+2m+z | 1479260404/746331553 | 1.9820418928476 |
| required raw exponent t+1-R | 299150468714369/205241177075000 | 1.4575558032638 |

Physical e≈.1668386 is a **Z-length**, not t or z. The table gives limiting
budgets, not equality invocation of a strict moment theorem. Real selected
capacity is z-nu0 with fixed positive nu0, and whole-slot mesh losses must be
reserved before selecting slots.

Exact identities:
\[
 R+\delta t=(1+5t)/6,\qquad 2\delta m+\delta z=1-R.
\]
Therefore mixed upper energy U^(1+delta t-chi+epsilon) divided by the real
lower spike U^(delta t+2delta m+delta z) gives #C<<U^(R-chi+epsilon).

For (7) take B=t+eta with fixed eta>0. If the **unproved** raw estimate (13)
were available, then
\[
 E_{\rm mixed}\ll U^{1+\delta t-\chi+\epsilon}(1+T1)^A,\qquad
 \chi=\lambda-\frac56\eta. \tag{14}
\]
The cost 5eta/6 is retained. For example lambda=1/20000, eta=1/10^6 would
conditionally leave chi=59/1200000≈.0000491666667, larger than the necessary
test decrement .0000379526642292785... . Neither lambda nor chi is attained.
Mesh, bin, height and tail losses must still be deducted.

A single rational tuple is insufficient for a region theorem: (13) must be
uniform on the real admitted bins and actual kappa=2beta*-1 under contradiction,
with a suitable neighborhood, the remaining physical row ranges, low estimate
and continuation. No target-kappa premise is inserted into an actual call.

The arithmetic demand is substantially larger than the small final chi:
even a hypothetical generic large-sieve budget H+N' has largest-dyad exponent
about 1.982041893, versus the required raw 1.457555803-chi. This is a scalar
orientation comparison, not an invocation of an available sextic large sieve.

The existing marked M*Q estimate needs B>=t+2z, rather than t+eta. Its
amplified count cost (5/3-2q)z is positive at q=delta/2. Attaching slots to
that old inverse upper alone cannot create the new negative cost. The actual
mixed cross term (12) is where that separate-payment penalty must be avoided.

## 7. Reproduction and scope

Run:
`C:/Python312/python.exe -B -X utf8 tmp/research-resume-20261011/zero-free/mixed-sixth-restoration-budget.py`

73 exact scalar/local-coefficient checks passed. The output JSON binds the
frozen source checksum and current status documents, exact target parameters,
local Euler restoration signs/normalization and conditional slack cost.
It does not simulate a Hecke row family or prove (13).

Paid, relative to explicit written inputs: exact mixed restoration; actual
injective amplification reduction; actual convolution/character Gram; complete
same sixth-free class absolute block. Still open: different-class signed
cross saving with original masks, profiles, real height order and actual kappa
feedback, followed by complete physical/source assembly.

No new zero-free boundary, actual count saving, Lean theorem or external
release is asserted.

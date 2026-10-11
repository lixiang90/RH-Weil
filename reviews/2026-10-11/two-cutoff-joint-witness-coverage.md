# Two-cutoff actual detector coverage with one presentation and a paid joint-core tax

2026-10-11, research round 505. This work reads note 504, its revised
mixed-restoration report and independent review, then returns to the actual
joint-witness/coverage gate. This source-relative analytic argument is separate from the proportion formalization. It does not establish a mixed upper bound or a new zero-free region.

**Conclusion:** one cannot require the fixed long inverse at t0 and the fixed
short witness at m0 on every row from the stated single detector contract.
However, replaying the *actual source proof* at two nearby cutoffs, with the
same zero and presentation fixed first, gives a legal exhaustive partition.
Every discarded branch has an existing strictly better count; the remaining
core genuinely has a long inverse and a short plain witness together in one
presentation. An additional plain branch makes the real short-length range
narrow and excludes the m>=1/2 capacity failure.

This pays a concrete coverage repair, relative to the source's written
analytic inputs R, rather than adding joint spikes as a new assumption.
The mixed raw upper bound still has not been proved. Coverage consumes a
quantified saving, approximately a factor 5.4700 at the test label. The prior
hypothetical raw lambda=1/20000 does not survive that cost. No count improvement
or new zero-free region is asserted.

## 1. Actual source: fix the zero and presentation before both cutoffs

Frozen source:
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
canonical LF SHA-256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

Source 4229--4257 defines
X_u={nu(n)chi_n(u)^sign: nu in Theta, sign=+/-1},
including every natural zero extension. Buffered bins 4291--4309 choose a
presentation psi in X_u and a genuine primitive zero rho=sigma+i gamma with
a<=sigma<a+e, |gamma|<=3iT1. The corresponding original L has the same zero,
since its deleted Euler factors are finite analytic multipliers there.

The source proof of Proposition detector-witness starts by **choosing that
zero rho**, then introduces D*=U^t (4554--4565); no later step changes
psi or rho. The Gamma-integral bound is uniform for 1<=t<=3/2
(4583--4590), and the dyadic separation/product lower bound is constructed
from the same L_orig and C_psi (4609--4666), followed by saturation
(4668--4683). Therefore the proof itself,
not merely an interchange of quantifiers in the displayed proposition, gives:

**Same-zero finite-cutoff lemma, relative to R.** For each retained row in a
nonfloor bin, first fix psi_u and rho_u from the buffered bin. For any prescribed
finite list of cutoffs in [1,3/2], run the same construction for each cutoff.
Each produces an actual pair (M_{r_j},S_{m_j}) for this same psi_u, with
\[
 r_j\le t_j+O(1/\log U),\quad r_j+m_j\ge t_j-O(1/\log U),
\]
\[
 |M_{r_j}|^2\gg U^{\delta r_j-\epsilon},\qquad
 |S_{m_j}|^2\gg U^{\delta m_j-\epsilon},\quad
 0\le m_j\le1/2+O(\epsilon). \tag{1}
\]
Their full profiles and selected dyads can differ between calls. For each call
the inverse/short pair has height gamma_u-nu_j. The two calls below keep nu_+
and nu_- independent; they do not turn their product into one common frequency.

One may choose the small assigned Fourier fraction c before both calls so that
their finitely many added frequencies fit the single cumulative T1/2 allowance
in each relevant L-argument. This is the same choice allowed by source
4434--4477 and 4650--4673; finite extra Sobolev parameters change a fixed height
order, not a U-exponent before closure. The profile windows and height order
are fixed before the external height exponent and tail derivative order.
Take maxima of the finite losses/thresholds. Each row's labels are then
subdivided by the common nu/sign and two dyadic pairs: at most O(log^4 U)
subclasses, with a fixed finite ray-label factor. Logarithmic multiplicity is
absorbed in an arbitrarily small prescribed power.

The inverse profile at the upper call is the *actual*
W_1(y)V_le(D y/D*_+) y^(-sigma-i(gamma-nu_+)).
Its original cutoff parameter D*_+ is retained even under later restoration;
the plain profile from the lower call retains its own gamma-nu_- height.
There is no same-height assumption, mask division or replacement of one
dyad by U^t0.

## 2. Parameter envelope used solely for the legal partition

Use the same real dynamic/amplitude bin, mean q=delta*x, 0<=x<=1/2,
actual kappa=2 beta*-1, alpha=5/6. Retain the original whole-slot supply
ell/d>1/5 with a fixed positive margin, complete natural masks, finite-ray
coefficients and fixed physical parameters.

The underlying plain proof replay of
`notes/450-plain-kappa-extension-and-actual-capacity.md` supplies the
actual-kappa capacity, with its explicit R inputs: lines 25--38 state the
positive-slot and zero-slot interfaces, 80--102 give the actual crossing
and strict widths, and 109--111 require the common actual feedback kappa.
Define
\[
 c=(3\kappa)^{-1},\quad D=3-(1+2c)x,\quad
 P=(2-2cx)(1-x),\quad A=\alpha-\delta,
\]
\[
 J=A D+\delta P,\quad
 t_0=1+\frac{\delta P}{2J},\quad
 r_0=\frac{(2-2cx)t_0-(1-c)x}{D},\quad m_0=t_0-r_0.
\]
Set
\[
 L(t)=1-\delta+A(t-1),\qquad
 S(t)=1-\delta+\frac{\delta P}{D}(3/2-t),\quad
 R_0=L(t_0)=S(t_0),
\]
\[
 I(r)=1-\delta[x+(1-x)r],\quad
 \Phi(m)=2\delta m+2q\frac{1-2m}{6\kappa}
         =\delta[cx+(2-2cx)m]\quad(m\le1/2).
\]
Thus I(r0)=1-Phi(m0)=R0. Let
\[
 B=\delta P/D,\quad I_1=\delta(1-x),\quad
 C_m=\delta(2-2cx).
\]
B,I1,Cm,A are positive in a sufficiently small compact neighborhood of the
critical label (delta≈.38858,kappa≈.7499,x≈.5). The following construction
requires A>0, t0 strictly inside (1,3/2), r0 strictly between 1/2 and 1,
and m0 strictly between 1/3 and 1/2; it does not claim the same partition
works at delta=alpha or every other bin without separate treatment.

For a small fixed desired branch decrement g>0 choose
\[
 s_+=g/B,\quad s_-=g/A,\quad a_L=g/A,\quad
 \rho_I=g/I_1,\quad t_+=t_0+s_+,\quad t_-=t_0-s_-,
\]
\[
 r_L^{\min}=t_0-a_L,\quad r_{\rm cut}=r_0+\rho_I,\quad
 m_{\min}=m_0-s_--\rho_I,\quad
 m_{\rm cut}=m_0+g/C_m. \tag{2}
\]
Take g small enough that both cutoffs are legal, rL_min>1,
r_cut<1 and 1/3<m_min<m_cut<1/2. These strict conditions hold at the exact
test below and persist on a compact neighborhood by continuity.
All these real parameters are fixed on the bin before its varying-row sum.

## 3. Exhaustive actual partition and existing budgets

Fix both actual witness pairs of (1), with lengths (r_+,m_+) and (r_-,m_-).
Take fixed positive capacity buffers nu_I,nu_P so that
\[
 r_{\rm cut}<1-\nu_I,\quad m_{\rm cut}<1/2-\nu_P,
\]
\[
 1-\delta+\delta\nu_I<R_0-g,\quad
 1-\delta+2\delta\nu_P<R_0-g. \tag{3}
\]
Work in each common finite/dyadic subdivision. The following are **ordered**
parts: after removing a part, apply the next condition to the remaining rows.

1. **Upper call short branch: r_+<1.** The actual short count construction gives
   exponent <=S(t_+)=R0-g, with arbitrarily small losses. If m_+>=1/2 or
   a capacity is in its fixed nearzero neighborhood, use its original
   unweighted endpoint as in source 15312--15321 and 15422--15434; no shrinking marked margin
   is invoked. The construction is the same two-moment min bound with the
   note-450 actual capacity, not source's optional 3/4 baseline replacement.

2. **Upper call shorter long branch: r_+<=rL_min.** All remaining rows have
   r_+>=1. Source 15249--15311 inverse amplification gives
   exponent L(r_+)<=L(rL_min)=R0-g. This is uniform at r=1 and does not
   use marked moment at a shrinking width.

3. **Lower call near-one and long inverse: r_->=1-nu_I.** For r_-<1 the
   unmarked count is <=1-delta+delta nu_I<R0-g. For r_->=1 it is
   <=L(t_-)+o(1)=R0-g+o(1). This part includes the exact long-only possibility
   r_-=t_-,m_-=0 and pays it by an already proved count.

4. **Lower call marked inverse: r_->=r_cut.** Its remaining range is
   r_cut<=r_-<1-nu_I. Request the original capacity
   zM=(1-r_-)/2 minus a small fixed nu0. Both strict widths are explicit:
   \[
    1-r_--2z=2\nu_0>0,\quad
    3-2r_--8z=8\nu_0+2r_--1\ge8\nu_0+2r_{\rm cut}-1>0.
   \]
   Source 15223--15246 and 15370--15390 give the selected inverse count;
   whole slots and their average q give I(r_-)<=I(r_cut)=R0-g,
   plus reserved moment/bin/rounding/height losses. Supply is sufficient
   since zM<1/5. The same actual Q coefficient class and orientation
   adjustment of source 15136--15169 is used.

5. **Lower call large plain length: m_->=m_cut.** For
   m_-<1/2-nu_P request zP=(1-2m_-)/(6 kappa) minus nu0. Its capacity has
   a fixed positive margin and count 1-Phi(m_-)<=1-Phi(m_cut)=R0-g.
   For m_->=1/2-nu_P the original **zero-slot** plain moment
   (source 15312--15314 and 15428--15434) gives
   1-2delta m_-<=1-delta+2delta nu_P<R0-g. This covers m_->=1/2,
   rather than assigning it a negative selected capacity.

The common height factor is (1+T1)^A for a finite A fixed before tau.
The complete original masks, fixed ray coefficients and physical-slot
supports remain in every application. Different parts may select different
whole-slot subcollections; fixing their finite labels before summing rows
is the source's original mechanism.

The remaining **actual joint core** satisfies
\[
 r_L=r_+>r_L^{\min},\quad r_L\le t_++o(1),\qquad
 m=m_-\in[m_{\min}-o(1),m_{\rm cut}). \tag{4}
\]
It has the saturated M_{r_L} from the upper call and saturated S_m from the
lower call *simultaneously in the same psi_u*. The short and long heights
remain independent. It also has a valid positive selected capacity:
\[
 z(m)=(1-2m)/(6\kappa)-\nu_0.
\]
Since m_cut<1/2-nu_P, this capacity has a fixed positive lower margin on the
core. Greedy original whole-slot selection gains at least q times requested
length, losing only the original 2q nu0+delta max_i w_i reserve.
Thus the genuine joint product lower spike is
\[
 |M_{r_L}|^2|S_m|^4|Q_{\rm sel}|^2
 \gg U^{\delta r_L+\Phi(m)-{\cal L}}, \tag{5}
\]
where L includes M-loss+2S-loss+Q-loss and all chosen capacity/rounding losses.
Every omitted original row lies in one of the five paid parts. The core is
not created by assuming a particular prescribed dyad or by deleting rows
without paying their count.

Equations (4) record the actual support errors o(1)=O(1/log U), not exact
finite-U limiting endpoints. For a future raw theorem take a fixed small
buffer around these intervals before U, charge its slope cost to L, and
then increase the threshold. No U-dependent shrinking moment margin is used.

## 4. The narrower moving-crossing threshold does not erase the tax

The exact crossing derivatives are
\[
 r_{\rm crit}'(t)=(2-2cx)/D,\quad
 m_{\rm crit}'(t)=(1-x)/D,\quad
 r_{\rm crit}'+m_{\rm crit}'=1.
\]
At x=1/2, mcrit'=1/(5-2c). However, using the moving crossing at t_- changes
the inverse budget: I(rcrit(t_-))=S(t_-)=R0+B s_-.
To keep the discarded inverse part at <=R0-g one needs
\[
 \rho_- \ge(g+B s_-)/I_1.
\]
Since B/I1=rcrit', the smallest legal cut is still
\[
 rcrit(t_-)+\rho_-=r_0+g/I_1=r_{\rm cut},
\]
and its actual short-length loss is
\[
 mcrit' s_-+\rho_-=s_-+g/I_1. \tag{6}
\]
Thus the apparent smaller mcrit' loss is paid back exactly by the inverse
threshold offset. One cannot use only mcrit' s_- while keeping the old
discarded-row exponent R0-g.

These are exact affine identities from the actual count formulas, not a
sampled optimization. They identify the narrowest cut within this specified
old-inverse-budget partition; they do not prove every possible multi-detector
correlation method optimal.

## 5. Uniform mixed contract still needed and quantitative coverage cost

A new mixed upper theorem would have to cover **all actual pairs** in (4),
their common natural presentation, original upper inverse cutoff, independent
two witness heights, physical height, and requested z(m), with whole slots.
After the mixed restoration of 504, the raw contract must also cover the
two independent restored plain scales, all restored inverse scales and the
finite Sobolev derivative closure. Narrow original m does not mean the
restored X'_1 and X'_2 remain in this same narrow interval.

If a uniform mixed estimate
\[
 \sum_{\rm core}|M_{r_L}S_m^2Q|^2
 \ll U^{1+\delta r_L-\chi+\epsilon}(1+T1)^A \tag{7}
\]
were proved per actual length subdivision, division by (5) would yield
\[
 \#\mathrm{core}\ll U^{R_0-\chi+T_{\rm cov}+\epsilon+{\cal L}},
 \qquad T_{\rm cov}=C_m(s_-+\rho_I).
\]
Because Phi is increasing, its worst actual m is m_min (up to paid buffer).
To match every complement's decrement g it is sufficient, before other losses,
\[
 \chi\ge g+T_{\rm cov}
 =g\left[1+C_m/A+C_m/I_1\right]. \tag{8}
\]
This is conditional: no estimate (7) has been established here.

### Two different raw references must not be confused

Write R_L(r)=1/6+(5/6-delta)r=L(r). For H=U^(r_L+eta), eta>0 fixed:

- A genuinely **stronger varying-long reference contract**
  Eraw<<H U^(1-R_L(r_L)-lambda+epsilon) would give
  chi=lambda-5eta/6 in (7). Thus it must have
  lambda>=g+Tcov+5eta/6, plus all other losses, uniformly across (4).

- Keeping 504's **fixed central R0 contract**
  Eraw<<H U^(1-R0-lambda+epsilon) instead gives
  chi(r_L)=lambda-5eta/6-[R_L(r_L)-R0].
  Worst r_L=t0+s_+ charges A*s_+, plus its actual support buffer.
  Its sufficient requirement is
  lambda>=g+Tcov+A*s_++5eta/6, plus all other losses.

The raw upper hypotheses are different; the first is not already supplied by
a single-label fixed-R bound. Natural kernels/same-sixth-free-part payment
from 504 remain algebraic reductions only.

## 6. Exact target-label verification

At Btarget=17499/20000=.87495, kappa=7499/10000, delta=19429/50000,
x=1/2 and alpha=5/6, take g=1/20000=.00005.

| Quantity | Exact | Orientation |
|---|---|---|
| t0 | 9229494722/8209647083 | 1.1242255152614 |
| r0 | 5875092361/8209647083 | .7156327551724 |
| m0 | 3354402361/8209647083 | .4085927600891 |
| R0 | 136828076410631/205241177075000 | .6666697119976 |
| s+ | 462425/1359796852 | .0003400691797 |
| s-=aL | 15/133426 | .0001124218668 |
| rhoI | 5/19429 | .0002573472644 |
| t+ | see JSON | 1.1245655844411 |
| t- | see JSON | 1.1241130933946 |
| m_min | see JSON | .4082229909579 |
| m_cut | 4562229232981298827/11163452259494382716 | .4086754820043 |
| Tcov | 3354402361/15008423610000 | .0002235013115 |
| required chi before other losses | 8209647083/30016847220000 | .0002735013115 |
| coverage factor 1+C_m/A+C_m/I1 | 8209647083/1500842361 | 5.4700262308228 |
| fixed-R extra A*s+ | 1233990361/8158781112000 | .0001512469012 |

With eta=1/10^6, the necessary designed raw levels are approximately
.0002743346449 for the varying-long reference, or .0004255815461 for the
fixed R0 reference, before other reserved losses. The old single-core
proposal lambda=1/20000 gives chi=59/1200000 but only
chi/5.47002623≈.0000089884 as an all-branch decrement within this repair.
This is below the target necessary .0000379526642, even with zero remaining
height/bin/rounding cost.

In the limiting lossless version of this partition, making the target
necessary decrement available already requires raw lambda strictly above
chi_target*5.47002623 for the varying reference, and above
chi_target*(5.47002623+A/B) for the fixed reference. JSON records both exact
fractions. They are budget requirements, not achieved savings or a global
impossibility theorem.

A future uniform mixed chi=.0003 would leave the five complement exponents
at R0-.00005 and the core strictly better. Reserving <.00001 for all finite
profile/witness/bin/whole-slot/height losses would then conditionally leave an
overall decrement >.00004. That exceeds the *necessary* target test budget,
but would still not certify a region: the mixed upper, actual-kappa
neighborhood, physical row ranges, low/raw-high estimates and continuation
would all remain necessary. Neither chi=.0003 nor any positive cross saving
was obtained this round.

## 7. Scope of the single-row countermodel and reproducibility

For the bare numerical single-detector contract, one scalar row can have
|M_r|^2=U^(delta r), S_0=1 and S_m=0 for every fixed m>0. At each cutoff take
r=t,m=0 (or the next dyadic r, within O(1/log U)). It satisfies the stated
detector individual/product lower and pointwise upper exponents, while
containing no prescribed positive short spike. One row also satisfies the
numerical inverse/plain marginal energy exponents on the bounded range.
This is **not a Hecke family, original coefficients or actual zero model**;
it only shows that the displayed scalar existential contract cannot force
per-row fixed long+short spikes. The real two-cutoff partition legally discards
such a row in its lower-call long branch rather than treating this scalar
example as an actual arithmetic obstruction.

Run
`C:/Python312/python.exe -B -X utf8 tmp/research-round505-20261011/zero-free/two-cutoff-coverage-check.py`.
All 51 exact checks passed, including source identity, every branch threshold,
the moving-crossing refund (6), positive strict capacities, same-presentation
parameter bookkeeping and both different raw-reference budgets.
The program certifies finite algebra; the actual source-relative coverage
proof is the argument above.

Paid this round: a source-proof-based same-zero finite-cutoff detector
strengthening, exhaustive old-budget partition, real simultaneous-long/short
core with a positive capacity and narrow actual m interval, and its exact
coverage tax. Still open: uniform actual mixed upper for this core and all
of its restored scales/heights/profile derivatives, complete physical/source
assembly and the full arithmetic zero-free conclusion.

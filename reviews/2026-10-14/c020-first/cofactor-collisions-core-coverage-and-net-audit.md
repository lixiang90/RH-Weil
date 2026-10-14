# C020 actual cofactor collisions, core coverage and strongest-old net audit

2026-10-14; independent audit by `/root/c017_macro_net`. Only this file is
edited. No STATE, cadence, Goal, contract or Git mutation and no independent
round settlement is made here.

## 1. Recovered responsibility and upstream premise

AGENTS/README/STATE/check/show, current Goal/frontier, C020 and D20261014U
were restored. Baseline remains `0c4f3a3eb609bb1d9564138fa4a35701f05605f2`
(all through 538), Goal G20261014, LF SHA256
`9ec2e58f9a4e2d8ad4302be5ce0369a89e6ce671ce1b3be77c0d26a93e032228`.
At initial recovery HEAD was `bc2a891e885f5cb4412c44c5f10df049cfc9127f`,
latest settled mathematics 546, cadence zero, C020 ready/budget one/settled
empty. Concurrent root dispatch and audit edits are live work, not a remote
or clean-tree completion certificate. This child does not own the root's
runtime Goal or counting decisions.

The raw mu norm proof and original MR nonpretentiousness/source proof are
separate upstream audits. Root consumption must first pay their exact common
premise; the present transport does not assume RH or substitute the external
paper's name for those checks. The cached MR PDF is 2007.15644v3, SHA256
`fef1a239e616f40c57aa45e7df3397aebe880cde8ce5763acb815a24a171f6aa`;
the metadata and original were read, not downloaded again.

The transport premise needed below, for each arbitrary fixed B >= 1, is

    (MR_B) sup_(sqrt D<=T<=B sqrt D, |tau|<=T, Y0>=D)
                ||V_(D,T,tau,Y0)||^2 -> 0 as D -> infinity,
    V(u)=sum_(D<d<=2D) mu(d)d^(-1/2-i tau)e^(-d/Y0)
                                      1_[log d-1/T,log d](u).

The frozen first norm gate has B=6. That alone covers kappa<=8, but is not
enough for the full trace limit below. Arbitrary fixed B requires an explicit
fixed-aspect extension of the same source/variable-window proof; it is not a
claim for B growing with D. The MR k=1 character range
epsilon D^2/H^2 contains B sqrt D for large D in every such fixed aspect.
The required centre-average, variable H, two dyadic endpoint strips, Abel
weight and original du norm remain upstream hypotheses until reconciled.

Final cross-audit reconciliation read during this audit: the source reviewer
explicitly pays the distance-vs-squared-distance convention, the growing-time
fixed-Q mu prerequisite from the original MRT 2015 equation (1.12), and every
separately fixed B (source file SHA256
`172933ca4ae437be5d146fd97ca1e1abcd9cd98d09d646b9fbd3ed679064df19`).
The physical/Gamma reviewer explicitly extends the full original-norm proof
to every such fixed B (file SHA256
`d4879f2180591a49867f061ffa22e5dbab28432e68c5f44359163a0acfe842b5`).
Their finite-frequency and large-D/then-grid-limit quantifiers match MR_B
above. Thus its premises have actual independent audit inputs available for
root consumption; this is not an assumption of the sought critical bound.
There remains no B(D) or effective-rate implication.

Local old originals read include 151 (SHA256
`5117e3e69abc630fe2912089771b0ea28ed9929e1213b01f92bf12434f445619`),
164 (`a0e9d412e55ebf298a209915c6b2870eab6c6a62d340b13c6a2e53a4ae6367d5`),
165 and 167 (`383eef4e43c21e789e4a1f88e24b34174451538d49d7515920383e666dbab3fd`).
These identify versions and paid scopes, not certification of a missing input.

## 2. Exact mask, all prime powers and finite complex Gram

Fix Y -> infinity, sqrt Y <= T <= 2sqrt Y, h=1/T, |tau|<=T,
U=floor(T/log^2(e+T)), V=1. Use the original synthesis

    E_n(u)=1_[log n-h,log n](u),
    s_n=n^(-1/2-i tau)e^(-n/Y),
    n in (Y,2Y].

Old 164 gives raw Type II coefficients as the full convolution
`mu_(d>U)*Lambda_(m>1)*1_r`. Group the exact product kappa=mr before any
inequality. Since Lambda(1)=0 and `Lambda*1=log`,

    sum_(m|kappa,m>1) Lambda(m)=log kappa.            (1)

The sum includes every proper prime power; replacing it with primes alone
would make (1) false. Define the actual cofactor columns

    F_kappa(u)=log kappa sum_(Y<kappa d<=2Y, d>U)
                        mu(d)s_(kappa d) E_(kappa d)(u).  (2)

Then the complete Type II vector on this dyadic n block is exactly

    II_Y = sum_(2<=kappa<=M) F_kappa,
    M=floor(2Y/(U+1)).                             (3)

Empty columns are harmless. There is no fractional endpoint approximation:
d is an integer, d>=U+1, n<=2Y implies kappa<=M. Different labels with the
same n have been added with their signs inside the same physical feature.

For the frozen kappa<=8 and large enough Y, Y/8>U, so d>U is automatic.
Writing D_kappa=Y/kappa, all weights and shifts are exact:

    F_kappa(u)=log kappa kappa^(-1/2-i tau)
                  V_(D_kappa,T,tau,D_kappa)(u-log kappa). (4)

Indeed exp[-d/D_kappa]=exp[-kappa d/Y]; the shift turns E_d into E_(kappa d).
Moreover T/sqrt D_kappa lies in [sqrt kappa,2sqrt kappa], contained in [1,6]
for kappa<=8. This pays the prescribed aspect without silently using the
earlier [1,2] preparation. Original du/L2 measure and complex phases are
preserved, and each fixed finite source is compact BV, hence legal Dlog and
actual Gamma operator-domain input.

Let A_8 alpha=sum_(2<=kappa<=8) alpha_kappa F_kappa and G_8=A_8* A_8, with
the complex inner-product convention fixed consistently. Its entries contain
the complete kernel

    (h-|log(kappa d/(lambda e))|)_+,

including exact and near product collisions, the full factor
`mu(d)mu(e) log(kappa)log(lambda) s_(kappa d)conj(s_(lambda e))`, and all
cross entries. Under (MR_6), every column has norm o(1), so positivity gives

    0 <= G_8 <= Tr(G_8) I = o(1) I.                (5)

Thus the result is uniform over every complex alpha in this finite label
space, not merely the actual alpha=1. The use of a trace bound does not set
cross terms to zero: it bounds the entire positive Gram including them.
The label ell2 norm is explicit; it is not a replacement for the physical
source norm or a bound on every original Weil source.

## 3. A genuine full-cofactor joint trace gate

There is a stronger joint consequence than successively increasing a finite
head. It combines every arbitrary fixed-aspect MR column with a source-free
summable column tail, keeping the full original cutoff (2).

All columns are supported in

    log Y-h <= u <= log(2Y),

whose length is at most log 2+1 for large Y. At x=e^u, the window of admissible
d has at most `1+C Y/(kappa T)` integers, even when d>U clips it, or when it
meets either dyadic endpoint. On this mask |s_(kappa d)|<=Y^(-1/2). Therefore,
uniformly in all tau and all kappa<=M,

    ||F_kappa||^2 <= C (log kappa)^2
                      [Y/(kappa^2 T^2)+1/Y].       (6)

This retains the discrete one-integer error; dropping 1/Y would be invalid
near the maximal cofactor. There is no assumed cancellation in the clipped
tail. U is comparable to T/log^2(e+T), so

    M <= C sqrt Y log^2 Y,
    M(log M)^2/Y = O(log^4 Y/sqrt Y) -> 0.          (7)

For every fixed J, (6),(7) give

    sum_(J<kappa<=M) ||F_kappa||^2
      <= C sum_(kappa>J) (log kappa)^2/kappa^2
           + C M(log M)^2/Y.                       (8)

For kappa<=J, d>U is automatic for large Y, (4) applies, and (MR_B) with
B=2sqrt J gives a finite sum tending to zero. First take the large-Y limit
with J fixed, then J->infinity. The summable series in (8) tends to zero.
Consequently, conditional only on the fully audited fixed-aspect MR premise,

    eta(Y):=sup_(sqrt Y<=T<=2sqrt Y, |tau|<=T)
             sum_(2<=kappa<=M) ||F_kappa||^2 -> 0,
    0 <= G_full <= eta(Y) I on C^(M-1).             (9)

The proof covers all actual cofactors, clipped d cutoffs, endpoint strips,
proper prime powers and all complex label vectors in the flat ell2 norm.
It does not need an MR rate for kappa growing with Y, nor MR cancellation
below one integer. Formula (9) is a joint full-mask source fee, not just a
fixed-kappa positive class. It requires arbitrary *fixed* aspect, so one
cannot infer (9) from the frozen kappa<=8 conclusion alone.

The same gate also supplies normalized full Gamma label fees. For the Fourier
convention hat f(t)=integral f(u)e^(-itu)du, write

    hat F_kappa(t)=hat chi_h(t) P_kappa(t),
    chi_h=1_[-h,0], |hat chi_h(t)|<=min(h,2/|t|).

The original n-polynomial P_kappa has coefficient square mass at most
`C(log kappa)^2/kappa`: sum 1/d over a clipped dyadic interval is bounded.
Old elementary mean value from 133/150, valid for every initial frequency,
gives on a shell of length X

    integral_shell |P_kappa|^2
      <= C[X+Y log(2Y)](log kappa)^2/kappa.          (10)

At |t|>=Y^2, sinc decay and dyadic summation imply, for p=0,1,2,

    (2pi)^(-1) integral_(|t|>=Y^2)
           [1+log(2+|t|)]^p |hat F_kappa(t)|^2 dt
      <= C_p (log Y)^p/Y^2 * (log kappa)^2/kappa.    (11)

Summing every kappa<=M costs only O(log^3 M), so the total tail is
O(log^(p+3)Y/Y^2). Below Y^2 the log weight costs at most C log Y per power.
For beta>=c log(e+T), with fixed c>0, the trace of the positive Dlog/Gamma
budget divided by beta tends to zero, and the trace of the Gamma operator
square budget divided by beta^2 tends to zero, by (9)-(11). Positivity again
gives the corresponding entire label Gram bounds, including all cross terms.
Here Gamma is the original `Re psi(1/4+it/2)-log pi=2theta'`, with its
original 2pi Plancherel factor. This does not assert the stronger division of
the operator square by beta. Nor does it use MR at tau+t outside its finite
character range; (10) is the old generic all-frequency tail input.

These are conditional source-fee consequences until the upstream MR_B proof
and nonpretentiousness are consumed by root. No extra iteration or automatic
promotion is introduced by this stronger full-mask reconciliation.

## 4. Exact shortest-window obstruction and remaining physical responsibility

The smallest additive length at a maximal cofactor is

    D_kappa of order Y/kappa, H_kappa of order D_kappa/T,
    kappa of order Y/U gives H_kappa of order 1/log^2 Y. (12)

The failure of a normalized MR short-window cancellation input at this scale
can be checked on the actual mu source, not just on arbitrary model sequences.
For 0<H<=1 a.e. interval (x,x+H] contains at most one integer. Consequently,
for every tau,

    integral_D^(2D) |sum_(x<d<=x+H) mu(d)d^(-i tau)| dx
      = H sum_(D<d<=2D) mu(d)^2 + O(H)
      = [6/pi^2+O(D^(-1/2))] D H.                  (13)

The supremum over characters inside this integral changes nothing. The error
is uniform for 0<H<=1. The elementary squarefree estimate follows from
`mu(n)^2=sum_(r^2|n)mu(r)`, summing the floor errors up to sqrt(2D), and the
absolutely convergent series sum mu(r)/r^2=1/zeta(2). No zero-position
assumption enters. Thus an o(DH) input for this shortest window is false.

In the original log interval, if kappa>=4Y/T then D_kappa<=T/4 and h is
strictly shorter than successive log d spacings in the dyadic d range for
large Y. Features for that single kappa are disjoint, giving exactly

    ||V||^2=h sum_(D_kappa<d<=2D_kappa, d>U)
                         mu(d)^2/d * exp(-2d/D_kappa). (14)

For an unclipped dyadic range with D_kappa/T tending to zero, this is of
order 1/T, whereas the putative continuous cancellation normalization
D_kappa/T^2 is smaller by T/D_kappa. In particular that ratio is of order
log^2 Y at the shortest scales. Equation (14) is not a lower bound for the
sum across different kappas: cross-cofactor cancellation and the Type I
channel can still occur. This obstruction stops the individual-window
cancellation supplier, not every signed joint method or the complete Weil Q.

The actual physical Type II vector corresponds to alpha_kappa=1 in (3).
Its flat label norm squared is M-1, so (9) yields only

    ||II_Y||^2 <= eta(Y)(M-1).                     (15)

Qualitative eta->0 supplies no required rate to offset sqrt Y log^2 Y.
Gamma versions likewise retain this label mass. This is precisely why a
complete all-label Gram fee may still fail to pay the actual physical
direction. A source-domain success is not whole-core coverage.

The physical remainder also includes the Type I counterpart and continuum;
old 164 gives their exact sum independently of the gauge V. V=1 does not
delete the companion channel. Full prime/pole and Gamma-continuum mixed
fees, the whole height schedule and actual zeta/Xi consequences remain unpaid.

## 5. Strongest-old subtraction: what is actually new

The old 151 triangular Gram and 164 common synthesis already give the
identities (1)-(4). Merely regrouping them is zero new mathematics. Old 165
already excludes free raw-label Bessel bounds through exact-product fiber
multiplicity; old 167 already bounds actual hard coefficient diagonals and
their polylog-height removal. It does not set near-product entries to zero.
The proof of the old 167 diagonal bound also works at V=1: m>=2 wherever
Lambda(m) is nonzero, and `R_I=Lambda_(>U)-II` follows from the old full
identity and support gap. Recharging that diagonal after changing V would
be repetition.

Under the paid MR premise, (5) and (9) improve the original unweighted
physical/cofactor label Gram from a source-free bounded trace to a vanishing
trace, and the normalized Gamma label fees similarly vanish. This is a
new actual signed-source fee relative to the reviewed old assets. It is not
the first invention of MR uniformity, which is attributed to its authors.

Two stronger old macro comparisons prevent overclaiming:

1. For kappa<=8, (6) alone gives G_8<=C_8 I. On this single square-root
   height band, dividing the actual head energy by beta of order log T
   already gives O(1/log Y)->0. Hence MR's head norm o(1) cannot be counted
   again as a new removal of that barrier-weighted core condition. Its
   stronger raw norm and normalized Gamma source fee are the correct scope.

2. The complete old decomposition and the elementary absolute window count
   also bound the actual vector more strongly than (15). Summing the
   pointwise bound behind (6) before squaring gives

       |II_Y(u)| <= Y^(-1/2) sum_(kappa<=M) log kappa
                    + C sqrt Y/T sum_(kappa<=M) log kappa/kappa
                 <= C log^3 Y,
       ||II_Y||^2 <= C log^6 Y.                    (16)

   This follows directly from old exact identities and |mu|<=1; it is a
   strongest-old consequence for comparison, not a fresh arithmetic theorem.
   Without a rate, eta(Y) M cannot be shown to beat (16). The whole physical
   core criterion still cannot consume O(log^6 Y) across its heights.

The old 016/028 complete-object negative-trace assets and the newer 543
cofinal C exp(S) count budget are not improved by this label norm alone.
No whole Q sign, nearPSD, improved actual negative count, Xi identification
or Macro Goal completion follows. A label-space bound after scaling source
coefficients cannot silently be renamed a physical-source relative bound.

## 6. Stop decision, next information gate and organization recommendations

If root pays MR_B and reconciles the above transport, one complete C020
admission may record the new original raw/cofactor/Gamma source fees once.
The main physical growing-label/Type I/continuum responsibility remains;
stop this contract after that one iteration. Do not enlarge fixed kappa,
increase a numerical Y, or cite another averaged theorem with unchanged
label mass as a new route. If MR_B is not paid, all its downstream o(1)
statements above remain conditional and entry restoration is zero rounds.

The next gate with actual information value is a joint comparison on the
remaining physical direction in this complete quotient: either a primary
arithmetic theorem controlling the cofactor-row near-product correlations
in the original density/cost norm with a rate that beats (16), or a legal
necessary fee for that density norm after exact fiber summation. The flat
ell2 trace gate has now been tested. The claim that the remaining full
physical energy is bounded cannot itself be named an independent lemma or
source: old 164/165 make that circularity explicit. This audit supplies no
such new row theorem and creates no further contract. A source search must
produce its actual premise and nonempty relevant scope before a next
research round is authorized by root's current state.

Four small organization changes are recommended, without another Goal epoch
or a copied counter:

- Every asset should carry a short output passport: exact object/norm,
  growth and source quantifiers, paid error, *actual physical coefficient
  direction*, and strongest-old net result. For C020 this must say that full
  kappa label Gram vanishing retains actual alpha=1 mass M and gives no
  proved improvement of (16). The passport travels with the asset through
  compression; a source label never travels as a whole-object theorem.
- Recovery should restore the causal obstruction together with the current
  action: which successful local norm does not meet the completion gate,
  which missing arrow remains, and why the proposed next input addresses it.
  STATE can link this passport/frontier rather than duplicating long proofs.
- A concrete core/net counterfactual must run in the same admission as a new
  source proof. Here it is the full cofactor physical direction, (12)-(16),
  not only seven columns. Otherwise source success makes the missed coverage
  disappear from a compacted summary and creates a thin-head loop.
- Consecutive zero entries should be visible through existing decisions,
  without a new round counter. After them the strategy review must exhibit
  a changed payable premise or falsifiable necessary-cost gate before the
  next contract. A different paper, representation or unknown domination
  name is insufficient. Organization/source recovery and pushes stay zero
  rounds; genuinely new cost and its scope are settled by root only once.

The completion audit remains bound to the current fixed Goal version and
baseline. All paused routes and the root's active macro status are inherited.

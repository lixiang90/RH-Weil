# NEW Cret gate: static mathematical code review

2026-11-01; `/root/retained_tail_representation`, same Goal1793085111. Recovered STATE/check/show and current admissions. Reviewed COMPLETE FINAL signed-head-gate.py, **23940 bytes/442 lines**, SHA256 **`ed32fa2749c11c1dd1adae3bb078a331c5206a9d79f975a23c45e7df5f2fb7c3`**. Actual bytes and ast.parse syntax PASS were checked. No driver import/function evaluation, actual source/seed/coordinate/matrix/eigen/inverse/gate calculation or shared-state/Git change occurred. Only this review is written.

**Limited static mathematical/code PASS; no blocker found.** Root must reconcile the protocol audit and exact freeze before ONE run. Existing math-admission/algorithm/congruence records carry the analytic proofs; this review checks their implementation, not an actual sign or runtime result.

## 1. Raw centers and exact assembly

load_centers checks root-consumed center-source authority, L9/8/N448/Omega256/beta7/2, J0=L²H and225 prime pairs. Old A/J0 sums have denominator2^257; old896 tail midpoint sums denominator2^641, with midTwice/order/parity checks. They construct OLD C0 only. NEW G comes from the COMPLETE accepted458528-row V stream, with bytes/hash/order and100352 head positions checked. Counterpart midpoint equality enforces symmetric G. No old float/P0/trial/witness is read; failed new interval box-truth is not used.

assemble uses ORIGINAL degrees idx=parity,parity+2,...,447 and w_i=2idx_i+1, preserving D_ii=9/(4w_i). Its exact integers are

    c=(Aint+J0int)2^1025+36 sum h_s h_s*,
    C0raw=c/2^1282, Graw=g/2^257,
    Bint=9*2^255 I+diag(w)g, Jint=g diag(w)g,
    Kint=Bint*(c+2^1025g)Bint
              -81*2^1535g-9*2^1280Jint,
    K=Kint/(81*2^1792).

gw weights COLUMN j by w_j. The three products, adjoint orientation, exponents and raw36 are correct. Integers remain exact; size guards stop without clipping. Exact g/c/Jint/Kint symmetry is checked. No inverse or native square root is computed.

The pre-arithmetic fee eps_C+3*2^-203<2^-201 is checked exactly. Old9*2^-512 is used for C0 HEAD error, not an896-coordinate whole-H claim. Old/new h centers are not assumed to cancel. Initialization encloses EXACT K±EPS*T, EPS=2^-201,

    T=B*DB=D+2g/2^257+Jint/(9*2^512), B=D^-1(Graw+D).

This is the native Loewner source fee transported by congruence, not an entrywise EPS box or raw Euclidean error. D's rational diagonal is retained; no second Gram/half-density conversion occurs.

## 2. Directed arithmetic and Schur invariant

Intervals are integer endpoints/UNIT, UNIT=2^1024. rat floors/ceilings exact rationals including negative values; up(a,b)=-floor(-a/b) is signed ceiling for b>0. sub uses a_lo-b_hi,a_hi-b_lo; mul takes all four product corners. square uses lower0 when crossing0, otherwise the lesser endpoint square, and the greater square as upper.

div_positive requires b_lo>0 and uses the correct cases:

* a>=0: [a_lo/b_hi,a_hi/b_lo];
* a<=0: [a_lo/b_lo,a_hi/b_hi];
* a crosses0: [a_lo/b_lo,a_hi/b_lo].

Bounds are rescaled and rounded outward. Division occurs only after d_lo>0; no zero-crossing pivot is guessed positive.

At pivot k, ell[i][k]=a[i][k]/d is saved before trailing updates. Updates touch ONLY i,j>k, so a[i][k],a[j][k] remain unchanged throughout that pivot. The implemented a_ij-a_ik*a_jk/d is therefore valid interval Schur elimination, using a dependent diagonal square and exact symmetry copying. Dependency may widen, not falsely narrow, its enclosure.

d_hi<0 only proposes a direction; d_lo<=0 otherwise gives unresolved. Upper-positive alone is not a true-head lower proof. Only positive LOWER pivots in BOTH224 sectors give POSITIVE_HEAD_ONLY. A negative lower pivot never triggers negative_proposal. The two real parity sectors cover the original complex448 head.

## 3. Point proposal and EXACT physical sign

At negative upper pivot k, ell[j][i], i<k,j<=k, exists from the positive prefix. Z_k=UNIT and higher entries0; backward steps compute

    Z_i=nearest[-sum_(j>i)^k (ell_lo+ell_hi)_ji Z_j/(2*UNIT)].

This is midpoint-L point backsolve, rounding ONCE after the COMPLETE integer dot product. Floor divmod plus2r>=d implements nearest ties toward positive infinity for either sign. Proposal accuracy is NOT a sign premise.

The terminal authority is exact integer/Fraction arithmetic:

    anum=Bint*Z, a=anum/(b*UNIT)=Bz,
    qK=(Z*Kint*Z)/(dK*UNIT²),
    norm=sum_i 9*anum_i²/[4w_i*(b*UNIT)²]=a*Da=z*Tz,
    upper=qK+EPS*norm.

Only norm>0 AND upper<0 emits negativeCertified. The exact upper/norm is the original-du Rayleigh upper. All denominator powers/original-index weights are correct. This direct check pays proposal rounding without an inverse/factor-residual assumption. Raw polynomial sources lie in original zero-extension Dlog.

gate() RETURNS after the first proposal whether it succeeds or fails: GLOBAL ONE is control flow, not merely metadata. Failed exact verification terminates UNRESOLVED with no other sector/vector. Ordinary uncertainty WITHOUT a proposal may inspect the other prescheduled parity. No direction/precision/pivot queue exists.

## 4. Validation and limits

Exact assembly has zero rounding. Finite interval conversion/LDL certifies the shifted rational target directly; no guessed finite operator fee is silently included in source<2^-201.

Root's633-byte arithmetic-leaves-result.json binds this FINAL SHA and reports18150 Fraction/scalar/3D-SYNTHETIC controls, including signed endpoints, zero-crossing squares/division, ties, positive/negative LDL, exact witness, source-band ambiguity and zero-pivot refusal. It records no research sources/driver import/actual Cret. I read that corroborating receipt, not reran its helper; the static reasoning above is independent of its PASS label.

Exact-code/review/pin/one-attempt guards, fixed1024/1800s/8MiB separate output, atomic logs and final source/self/freeze/log rechecks are present. Reviews must name the COMPLETE SHA above. Protocol coverage remains separately reviewed; root must reconcile both audits.

No actual head sign is established here. Negative stops PSD of this bounded Lret only; Q retains tau/unused positive tail. Positive is HEAD ONLY, not whole Sret/Q. Arithmetic unresolved is experiment pending root, not a mathematical obstruction. Program settles no cadence. Whole MV/Gram/inverse/M10 correlation and long Goal gates remain open; this static review counts zero mathematics.

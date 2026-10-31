# ONE fixed retained-tail head sign gate, without an inverse

2026-11-01; `/root/retained_tail_source_design`. Recovered README/STATE/check/show, Goal, C066spent/latest603, D20261101A/frontier and the saved next-signed-head admission. Same Goal1793085111/baseline0c4f. This design uses the root-consumed new G source; it does not rerun old C0/P0/witness/pilot/source or perform any matrix, inverse, eigenvalue or sign calculation. No state/cadence/library/Git mutation. Standard finite arithmetic design earns0 mathematics.

## 1. Fixed object and source authority

Use the two native parity sectors j=0,2,...,446 and j=1,3,...,447, each224 dimensions, in that order. Put D=diag(g_j), g_j=9/[4(2j+1)]. Original source is raw p_j(u)=P_j(u/L), L=9/8, in H=L2(I,du;C); native normalization is D^-1/2 exactly once. E448/eta1/Omega256 remain fixed.

The exact center-model matrix is

    Chat=C0hat+Graw-D+D(Graw+D)^-1D,
    C0hat=Araw+J0raw+36 sum_s old_t_s old_t_s^T.

Old A/J0 centers are (lo+hi)/2^257; old tail t_s are midTwice/2^641. These are the OLD accepted448 h coordinates for C0, not the newly expanded h polynomial centers. J0 already includes the full band and both pole signs, in convention L_squared_H. NEW Graw consists of the first448 rows of the SAME accepted finite V center stream, also (lo+hi)/2^257. G_R is neither V*V nor the inverse-M Gram. Exact symmetry/parity, full source shape and all input versions must be checked. No old direction is read.

Accepted source errors are native, not entrywise:

    eps_C=2^-204+2*2^-220+9*2^-512,
    eps_G=2^-203,  true G>=0,
    eps_source=eps_C+3eps_G <eps:=2^-201.

The resolvent identity proves this source bound without commutation; I+Ghat>=1-eps_G. Consequently S=Graw+D>(1-eps_G)D, so the rational matrix B=D^-1S is invertible before any finite sign test. Source errors are kept separate from all subsequent finite arithmetic.

## 2. Exact inverse-free congruence

Let H=C0hat+Graw-D and define

    K=B^T H B+S,
    T=B^T D B=S D^-1 S.

Then K=B^T Chat B and T>0. Equivalently

    K=B^T(C0hat+Graw)B-Graw-Graw D^-1 Graw,
    T=D+2Graw+Graw D^-1 Graw.

This removes inverse computation and its conditioning/error budget. It preserves the source inequality exactly:

    K-eps*T <= B^T Cret_raw B <= K+eps*T.

The inequalities are form order after the SAME raw/native transport. No finite norm error is inserted into eps: K,T will be assembled as exact rational/integer matrices, and sign arithmetic will enclose those exact matrices directly.

For a fully specified integer assembly set q=2^257, g=q*Graw, w_i=2j_i+1, and old h integers h_si=midTwice. Define

    c=(Aint+J0int)*2^1025+36 sum_s h_s h_s^T,
    b=9*2^255,
    Bint=bI+diag(w)g,
    Jint=g diag(w) g,
    dK=81*2^1792,
    Kint=Bint^T (c+2^1025*g) Bint
         -81*2^1535*g-9*2^1280*Jint.

Exactly C0hat=c/2^1282, B=Bint/b, K=Kint/dK, and

    T=D+2g/q+Jint/(9*2^512).

Three exact integer matrix multiplications per parity suffice: Jint; (c+2^1025g)Bint; Bint^T times that product. Integer additions/shifts/products are exact. Check exact symmetry of g,c,Jint,Kint. D has rational diagonal entries; keep these exact in T and in witness norms. Do not replace D by a nearby dyadic matrix or clear its varying denominators incorrectly.

## 3. Fixed interval LDL predicate

Freeze P=1024 dyadic directed arithmetic, eps=2^-201, even then odd, upper then conditional lower. Do not use floats, numerical eigenvectors, pivot searches, permutations, adaptive precision or a second route. The source model and all center values stay exact/immutable.

For each parity, first enclose each EXACT entry of K+eps*T outward on the1024-bit grid. Apply unpivoted symmetric Schur LDL in increasing degree order. At step k, for a strictly positive pivot interval d_k, form interval L_ik=A_ik/d_k with outward division, then update the trailing upper triangle by A_ij<-A_ij-A_ik*A_jk/d_k (or the algebraically equivalent reviewed LDL recurrence). Keep a complete interval for the exact factor; copying the triangle uses exact symmetry. Every add/product/division rounds outward, and division occurs only if the pivot lower endpoint is positive.

If the pivot upper endpoint is negative after a positive prefix, it proposes ONE negative direction as in section4. If its interval contains zero, stop that sector as unresolved; do not divide through it. If all upper pivots are positive, repeat the SAME1024-bit predicate from the exact entries of K-eps*T. All lower pivots positive certify this sector's true Cret head positive. A lower negative/zero-straddling pivot only makes the sector unresolved; it is not a true negative certificate.

Process both fixed sectors unless the globally ONE negative proposal terminates the gate. An ordinary unresolved even interval still permits the already scheduled odd test, because a negative odd witness would decide the bounded-lower question. The first strictly negative upper pivot across even then odd triggers that sole proposal; an exact witness failure is terminal UNRESOLVED, without a second proposal or remaining-sector computation. No additional direction/precision/parameter variant is admitted. Aggregate output is NEGATIVE_HEAD if the sole witness is certified negative, POSITIVE_HEAD_ONLY only if both lower-shift tests finish positive, otherwise UNRESOLVED.

Interval Schur arithmetic is a direct enclosure proof for exact K±eps*T. It need not be summarized by a guessed global1024-bit rounding fee. Finite enclosure width or a pivot touching zero produces an honest unresolved outcome. In particular source<2^-201 and finite rounding must not be silently added and still called<2^-201: here exact assembly and direct interval sign enclosure avoid that problem entirely.

## 4. ONE dyadic witness and exact final verification

At the first strictly negative upper pivot in a sector, use only its already computed unit-L prefix. Take deterministic fixed-grid midpoint entries of L and backsolve L^T z=e_k, with z_i=0 for i>k. Use P1024 dyadic point operations, one prescribed rounding rule after each complete dot product, and z_k=1. This is a proposal, not a certificate based on approximate factor accuracy. No alternate witness follows if it fails.

Represent z=Z/2^1024 exactly. Form the original raw source a=Bz exactly, i.e. its integer numerators are Bint*Z with denominator b*2^1024. Evaluate, with exact integers/Fraction,

    qK=Z^T Kint Z/(dK*2^2048),
    n=sum_i g_i*a_i^2=z^T T z,
    upper=qK+eps*n.

Require n>0 and upper<0 strictly. This exact final quadratic check pays ALL midpoint/backsolve/finite-proposal errors; no inverse or approximate-L residual assumption is used to claim the sign. If it fails, terminate the entire gate UNRESOLVED; do not improve/re-round/replace the vector or finish the other parity. On success the true physical Rayleigh quotient is at most upper/n<0, and the original E448 source lies in the zero-extension Dlog domain. Save exact Z, a, qK, n, upper, native/source scope and hashes sufficient for an independent stdlib rational checker.

A negative witness proves that the particular bounded Lret=Llow+V(G+I)^-1V* is not PSD. The actual full Q still has nonnegative R-Uret omitted from this lower bound; this does NOT prove Q negative or disprove RH. A positive head remains only a necessary finite-head gate; whole Sret/M10/mixed MV/Gram/inverse/complement correlations are unpaid.

## 5. One concrete resource budget and stops

Admit code preparation first; root full code, independent reviews and exact-code freeze are required before ONE numerical run. Freeze1800 wall-clock seconds, P1024, eps201, two224 sectors, globally ONE witness at most, and an8MiB separate ignored output cap. No existing output directory may be reused. Proposed destination: literature/local/2026-11-01-retained-tail-signed-head/run-01/.

Assembly requires at most6*224^3=67,436,544 integer multiply-add terms across both sectors, with operands mostly260 to1800 bits. Four complete symmetric LDL passes require fewer than4*224^3/6<7.5 million trailing entry updates; early negative/uncertain pivots reduce that cost. Each uses fixed1024-bit interval arithmetic with bounded integer exponents. Source parsing/hashing is about100MiB. Expected stdlib runtime is hundreds of seconds, unmeasured;1800s is a plausible hard cap, not a promised completion. The exact inverse-free route is cheaper and easier to audit than forming two dense interval inverses and multiplying them. No benchmark or matrix computation was performed in this design.

Deadline checks occur before/after each exact matmul row, each LDL pivot, each source-hash chunk, and inside sufficiently long row/update loops. Save current stage/sector/row/pivot and exact intervals before guards. Cap failure is terminal even if some pivots were proved; no precision/retry/row-order/eta/window/source queue follows. Reserve space for atomic terminal failure/progress. A defensive integer-size guard may stop on unexpectedly large factor/witness numerators; if included it must be frozen before execution and must never change a value to satisfy the cap.

Save atomic progress and terminal result plus exact pivot/witness records within8MiB. Do not serialize full dense Kint or all interval factors if it breaks the cap; inputs+assembly recipe and relevant pivots/witness suffice for reproduction. Exact initial/final input hashes, full source count/order/parity/symmetry, final self/freeze hashes and all scopes are mandatory. Exception logs preserve the current mathematical object, phase, pivot interval, proposal/source location and any exact prefix relevant to the failure. All required validation must be inside terminal-stop handling after a valid one-attempt authorization guard.

## 6. Concrete schema/pins before code freeze

The three main mathematical data pins are:

| File | Bytes | SHA256 |
|---|---:|---|
| old source-matrices.json | 23377672 | a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2 |
| old tail-columns.json | 296046 | d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e |
| accepted finite-columns.jsonl | 73598411 | d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080 |

The first two prefix is literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/; the third is literature/local/2026-10-31-retained-tail-source/run-01/. These values are inherited from the accepted manifests, not new matrix reads in this design. A/J0 each has50400 upper-parity entries (i ascending then j>=i of same parity), centers from lo+hi, output256. The old tail wrapper packet has896 column-major entries including448 parity zeros; use midTwice=lo+hi and output640. The new V JSONL has458528 entries [column,degree,lo,hi] ordered by column then ascending same-parity degree0..2046. Read/hash its COMPLETE stream, selecting the100352 entries with degree<448, and require50400 unique exactly copied head entries. No unconsumed interval-box truth is needed to extract these accepted centers.

Additional small authority pins actually hashed during this design:

| File | Bytes | SHA256 |
|---|---:|---|
| old source-stage-verification.json | 14179 | dbb31208d0568feac7c9adff27722d5b55d08381002d23e0a4e35f150b1472c1 |
| center-certificate run-01/result.json | 70183 | 3eb9e77d71f92ead44775bfbafb7499a7ff0fd2e5bc81ac00095332a4f912739 |
| center-admission/root-consumption-scope.json | 20127 | 6e0df0fed60465622f8b95551e4e361203a8de9b199bf167c38709caf4caaac3 |
| center-admission/source-centers-consumed.md | 4973 | a823cabb902b1fd0270fd210db0d2efa4a0085d7918b49ec3afb79739178a4a6 |
| center-admission/next-signed-head-admission.md | 4160 | 3449a74e67fc71a9c5d0cb20430ddf420071ad803af50deb9af7bf644b5e2a56 |

The old stage prefix is reviews/2026-10-29/weil-9-8-admission/; center-admission is reviews/2026-10-31/retained-tail-center-admission/; center-certificate prefix is literature/local/2026-10-31-retained-tail-center-certificate/. The center machine PENDING_ROOT flag is preserved; root's external consumption record supplies authority. Also pin the original full-Weil transfer version0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466, this algorithm, the exact future code and its separate freeze/reviews.

Terminal schema must distinguish arithmetic completion from NEGATIVE_HEAD / POSITIVE_HEAD_ONLY / UNRESOLVED / STOPPED_NO_RETRY, record sector-specific status and pivots, exact eps/source bound, no inverse, exact assembly recipe/pins, and any independently checkable witness. Keep Goal/cadence/library-manifest literal guards before/after; do not recheck an old broad root binding set against unrelated newly edited .gitattributes. Pin only the actual immutable source/proof authorities plus current guards. Set wholeQ/RH/Goal completion unproved and mathematical settlement pending root. Root may settle a strict physical negative or both-sector strict positive theorem as ONE iteration; source/arithmetic/budget-only unresolved is EXPERIMENT0, not a theorem that the bounded candidate failed. Code never updates cadence itself. Passing this gate would change the next fixed-lower decision only; the long Goal remains active and its key whole/core/growing responsibilities remain open.

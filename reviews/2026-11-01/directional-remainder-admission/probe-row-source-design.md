# Fixed448 complement probe: exact model-row supply and bounded admission

2026-11-01; SAME Goal1793085111/0c4f, spent C068/605. Recovered current macro/state. Only this additional proof is written; prior supplier unchanged. No science/scalar/row computation, import/run, C069, execution or budget reuse.

Fix the SINGLE existing605 even source, not a new proposal. Let U=2^1024, b0=9*2^255, z=Z/U and a=rawSourceNumerators/(b0 U), exactly as serialized in the root-consumed605 witness; set bCoeff=a-z. Original degrees are0,2,...,446. Their normalized input is D_N^(1/2)a, with n=a*D_N a>0 already replayed. E448 stays unchanged. The one complement test is p_448, d_448=9/(4*897), not an enlarged source basis or a search over degrees.

## Immutable input API

Under A=literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/ and T=literature/local/2026-10-31-retained-tail-source/run-01/:

* A/source-matrices.json, SHA a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2: wrapper.packet.primeCenters has15 {key,a,w} records, denominator2^2048. Use EXACT centers; check opposite paired offsets/equal weights, zero weight7/2 and all seven powers. Old true-center eta2048 is paid; no scalar oracle.
* A/moments.json, SHA2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9: true1024 rows, thetaMid=(lo+hi)/2^1153, Binet included once.
* T/h-columns.jsonl, SHA37f2c0410beb1b1c43b9f8d2df24d72fce3170b5f359d089c198742f1eee4e74:2047 parity records [s,i,lo,hi], t_is=(lo+hi)/2^641 define FULL UHat; old896 head coordinates do not.
* T/finite-columns.jsonl, SHAd841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080:458528 rows [j,i,lo,hi], raw Vcenter=(lo+hi)/2^257. Select ONLY i=448 and even j<448; hash/shape/order/parity bind the entire stream.
* reviews/2026-11-01/retained-tail-whole-execution/prefix-result.json, SHA3dd3a82946a07c38fa80f18422af215de7e9d1a0c2b5b2e0dc817bfc0acb7e6c; its witness supplies a,z,n. The independent terminal-replay-result.json SHA32299c4c720caf2d1b4380a7cd01bf4a20611ad3ed81dcbb65536fe7b59ef30d and root consumption bind the exact source/norm/head upper, not merely a result status.

Pilot/source/08-produce.py SHAae0f487544c203905faecbb78b30f94fb16fe4f2f63c6b9846ca13ea673ba2b7 and07-check.py SHA85fcaaefd2d752a8401b9f7686c1c8779282c2cc21504129aabda7d1e37a83de were read as text. Future standalone code copies reviewed formulas, never imports drivers. Bind the supplier/old-fee/source-center proofs and verify every pin pre/end.

## Exact224-entry rows

For stored alpha_l=a_l/2^2048, weight w_l/2^2048, define M_c=sum_l weight_l T_alpha_l, T_alpha f(u)=1_I(u+alpha)f(u+alpha). This paired real operator is selfadjoint. The exact model row is

    m_j=<p448,M_c p_j>
       =sum_l weight_l integral_(I intersect(I-alpha_l)) p448(u)p_j(u+alpha_l)du.

Use symmetry m_j=<p_j,M_c p448>. The15 A seeds are polynomial overlaps on [max(-L,-L-alpha),min(L,L-alpha)], primitive(P_(k+1)-P_(k-1))/(2k+1). No M^2/225-pair/B trace term. Input r=j<=446, column448 has r+448<=894: seed0<=894, seed1<=893, boundary<=895 suffice. Old08/07's dependency wedge contains them, but retained/checked packet indices were<448: actual row448 numbers remain unpaid.

For Kstar use the full supplier's exact kernel coefficients

    a_(2q)=[2L^(2q)+(-1)^q thetaMid_q*576^(2q)]/(2q)!, q<1024.
    k_j=L^2 K_(j,448)+36 sum_(s=0,1) t_(448,s)t_(j,s).

K_(j,448) is the dimensionless double integral for sum a_m((z-w)/2)^m; multiply L^2 ONCE. Producer uses08 boundary seeds, checker07 factorial-quotient seeds and separate recurrence. M checker uses07 exact-center overlap/Legendre seeds and separate expansion. Compare independent true endpoints to final centers, not interval overlap/old half-width. Avoid huge-denominator affine monomial expansion.

At fixed producer3072/checker3328 bits and raw output256, require for EACH new M/K row

    sum_(j even<448) r_j^2/(d448*d_j) <=2^-460,

where r_j is maximum independent-endpoint distance to the final raw center. This is native row l2 error<=2^-230. These width/rounding predicates have NOT been evaluated. Opposite parity is exact0; keep all224 even entries including numerical zeros. Existing Vrow is SAME stored center data, with old full-H op226 error, not a newly generated V row or a native/raw factor change.

## One exact contraction and its sign meaning

From the three final rows compute the exact rational MODEL number

    t0=sum_j mCenter_j a_j +Vcenter_(448,j) bCoeff_j+kCenter_j a_j.

No d_j division belongs in this RAW contraction. It equals <p448,Nhat D_N^(1/2)a>; N=F+XB+Y and Bhat a_native corresponds to bCoeff=a-z. Keep bCoeff distinct from scalar bounds/operator B.

Old full-column ME-to-McE error1008 is used by L2 duality; the head-only primitive2021/derivative estimate is NOT extended to p448. Together Kstar264, V/G226, B transport and both actual row230 checks fit projected epsN<2^-223. The source-model coupling norms are<7. For s=<p448,Lret f_a>, therefore

    |s-t0|<=2^-223 sqrt(d448*n),  |t0|<7 sqrt(d448*n),
    2t0*s-t0^2 >=t0^2-2^-219*d448*n.                         (1)

This pays the POINT witness directly. Old true head is<2^-122 n; complement diagonal<11I since M<433/64, ||QKQ||<h and ||XAX*||<(9/5)^2. The sole strict predicate

    t0^2/(d448*n)-2^-219 >11*2^-122                          (2)

implies an ACTUAL negative bounded-Lret quadratic on

    f_a - [t0/(11*d448)] p448.

Orthogonality/n>0 make it nonzero. Norm is f-du, equivalently integral exp(-u)|r|^2du, r=exp(u/2)f. This is NOT negative full Q, which retains unspent positive tail. If(2) is not strict or any check fails, STOP: no degree/direction/Gram/parameter fallback, no positivity conclusion.

## Prospective cost gate, not execution

ONE NEW complete probe may be frozen at900s/8MiB including source guards, row production, independent checks, contraction, point verification, launch/terminal receipts and temporary/failure bytes. C068 contributes neither time nor permission. Source file reads do not require re-generating any scalar/packet. Working storage is the895 seed/wedge vectors,224 final rows and fixed witness; outputs can be far below8MiB without full matrices. Kernel seeds cost about1024*448 directed updates; recurrence about10^5 per implementation, versus the already reported115.474s old COMPLETE matrices stage including A/B/J0/225 pairs. This supports plausibility, not a proof of900s completion: independent checker widths, arithmetic and actual runtime remain unpaid code gates.

Future code requires NEW exact root/self/review/source pins, exclusive once-only namespace, atomic progress/result, external lifetime/byte accounting and terminal deadline/width/overflow/schema/pin stop. Independent replay covers ONLY these rows/SAME point; no LDL/inverse/new proposal/automatic next probe. Until reviewed code/root freeze, this is design only:0 mathematics/no C069/data.

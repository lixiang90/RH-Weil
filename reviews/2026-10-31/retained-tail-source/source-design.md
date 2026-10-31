# Fixed retained-tail source algorithm: design, not production

2026-10-31; owner `/root/retained_tail_source_design`. Recovered README/STATE, check/show, Goal, BD/frontier and the 6166-byte admission. Same Goal1793085111/C066spent/latest603. No production, science run, installation, web, state/cadence/library/Git mutation or iteration. Proposed ONE budget, conditional on root consumption/freeze.

## 1. Object and available primitives

Fix I=(-L,L), L=9/8, H=L2(I,du), N=448, Omega=256, eta=1. Let p_j(u)=P_j(u/L), g_j=2L/(2j+1), e_j=p_j/sqrt(g_j). The requested columns are V=RE, R=T_tail-tau I-U_old; G_R=E*V, not V*V or the old inverse-M Gram. Keep delta=2^-49158 and tau=delta/16 as exact symbolic rationals.

Bundled Python has NumPy, but no flint/mpmath/sympy/scipy. Rigor uses stdlib integers/Fraction and dyadic intervals. Old02 has Mesh.rat/add/sub/scale/mul/div, Machin pi, atanh log and exact Bernoulli factors; old08 has convolution seed/Legendre recurrences; old11/12 have an independent factorial-quotient route for sinc columns. Copy reviewed primitives; do not run old scientific modules or alter old files.

The old moments wrapper has rows q=0..1023, each q/lo/hi on the 1152-bit grid, midpoint radius <=2^-1098. They are actual theta_q=(256/pi) integral_0^1 x^(2q)(Gamma(256x)-7/2) dx. No gamma/pi constant enclosure is exported. New scalar intervals must be produced explicitly. For gamma use H_255-psi(256), a positive-real Binet expansion with K=256; certify its remainder (e.g. the old uniform bound 4*513!/(6^514*256^514), checked against 2^-1400). Use independently bracketed Machin pi/logs and require the combined contact scalar gamma+log(2*pi*L) radius <2^-600. Failure of the stated remainder/enclosure check is a stop, not permission to assume a decimal constant.

## 2. Full H representation; no discarded endpoint tail

Consume the sibling proof of

    A_Gamma p_j = [H_j-gamma-log(2*pi*L)-.5 log(1-z^2)]p_j-Q_q p_j,
    z=u/L, Q_q kernel q(|u-v|),
    q(v)=exp(-v/2)/(1-exp(-2v))-1/(2v).

Fix q's Taylor degree576 INCLUDING c_0..c_576: c_m=2^m B_(m+1)(3/4)/(m+1)!. Its full-H operator remainder is eps_q<2^-227. Its convolution columns have degree <=1023. The old band approximation has 1024 EVEN terms through degree2046: **576 is the argument 2L*Omega, not its degree**. The sinc approximation and resulting old rank-two polynomial functions also have degree <=2046. Freeze D=2046.

Write Lambda_ij=integral_-1^1 P_i P_j log(1-z^2) dz. Opposite parity gives zero. For equal parity,

    i!=j: Lambda_ij=-4/(abs(i-j)*(i+j+1)),
    i=j:  Lambda_jj=4/(2j+1)*[log2-1/(2j+1)-2(H_(2j)-H_j)].

These follow by differentiating Jacobi orthogonality: for n>m, the log(1-z) integral is -2/[(n-m)(n+m+1)]; the diagonal follows from the Jacobi norm and leading coefficient. Reflection supplies log(1+z). This O(ND) formula avoids cubic product expansions or oscillatory quadrature.

Produce raw interval entries S_ij=<p_i,Vhat p_j>, 0<=i<=D, 0<=j<N. Here Vhat p_j denotes the unnormalized column approximation before division by sqrt(g_j), not an operator acting on arbitrary H. Native finite coefficients are S_ij/sqrt(g_i*g_j). In the exact polynomial/log model,

    S_ij=g_j[H_j-c-7/2-tau]1_(i=j)-L*Lambda_ij/2
         -Qpoly_ij-Bandpoly_ij-36 sum_(s=0,1) t_is*t_js,

where c=gamma+log(2*pi*L), t_is=<p_i,(I-Bsinc_poly-delta I)p_s>. Thus raw U coefficient is 36; do not multiply serialized columns by 81/27 again. The latter constants apply to h_s=S e_s, and 81/g_0=27/g_1=36.

For i>D, all model polynomial terms vanish. Keep the remaining coefficients EXACTLY, for same parity,

    <e_i,Vhat_j>=b_ij=sqrt((2i+1)(2j+1))/[(i-j)(i+j+1)],

and zero for opposite parity. Equivalently the raw p_i expansion coefficient of the unnormalized column is (2i+1)/[(i-j)(i+j+1)]. This symbolic infinite tail is part of the H-valued output; D is not a projection of the endpoint logarithm. It gives square-summable columns and includes the full outside-head coupling.

## 3. Reconstruct the SAME global polynomial sources

Reconstruct Bandpoly from the pinned moment MIDPOINTS, not the old448x448 J0 entries. On t=|u-v|/(2L), its coefficient of t^(2q) is (-1)^q theta_mid,q*576^(2q)/(2q)!. The accepted old global kernel-to-operator bound <2^-204 applies to this SAME polynomial on all |u-v|<=9/4. The proof's larger constant914 includes a harmless pole allowance; it also dominates the band-only remainder. The moment Binet remainder is already included; do not charge it twice. No pole is subtracted from V when constructing the band directly. Both original pole signs remain in Llow/Q.

Reconstruct Bsinc_poly kernel (Omega/p_pi) sum_(q=0)^1023 (-1)^q[Omega(u-v)]^(2q)/(2q+1)!, where p_pi is the exact Machin160 rational used by old12. The global band error is <2^-513+2^-646. Form ALL coefficients of w_s=(I-Bsinc_poly-delta I)p_s, not only their old448 coordinates. Choose their dyadic centers at output640; require their normalized full-polynomial rounding errors <2^-520, using all i<=D. Then ||h_s-hhat_s||<2^-512. The accepted norms ||h_0||<1/29, ||h_1||<3/50 give ||U_old-Uhat||<9*2^-512 on all H. The old896 coordinate widths or old finite2^-220 row budget alone cannot pay this claim.

Compute Qpoly from the exact rational c_m and L. For each kernel sum alpha_m*t^m, use boundary moments

    b_j=2(-1)^j sum_(m>=j) alpha_m*(m!)^2/[(m-j)!(m+j+1)!].

Generate each m's weights by starting 1/(m+1), then multiplying (m-j)/(m+j+2); all are nonexpansive. For dimensionless double integrals K_rj on [-1,1]^2,

    K_00=2(b_0+b_1),
    K_0j=2(b_(j+1)-b_(j-1))/(2j+1)              (j even>=2),
    K_1j=[K_0,j-1-K_0,j+1+2(b_(j+1)-b_(j-1))]/(2j+1),
    K_rj=K_(r-2),j-(2r-1)(K_(r-1),j+1-K_(r-1),j-1)/(2j+1).

Use symmetry with r=min(input,output), j=max(input,output). Only r<=447 is needed; for the rectangle the seed range reaches r+j<=2493, with boundary indices through2494, not the old895. Multiply every double integral by L^2 exactly ONCE to obtain physical raw entries. The recurrence follows first-order integration by parts and translation invariance; it remains valid for continuous |z-w|^m kernels, with piecewise first derivatives. Store exact parity zeros; analytic polynomial degrees give exact zeros beyond their support.

Use exact source centers in this recurrence. Feeding the original moment INTERVALS through all recurrences loses dependency and can explode widths; the moment midpoint error is instead paid by the global kernel bound. Directed arithmetic encloses the exact midpoint polynomial. A checker should replay seed sums by the independent factorial quotient, then the rectangular recurrence and final assembly; do not use interval overlap as containment.

## 4. G consistency and actual complement data

The native Ghat is the first448 rows of the SAME coefficient stream, using exact du Gram congruence. Fill its symmetric head from a single upper-triangle computation. This makes Ghat=E*Vhat exactly in the represented model. G_R differs by the global V error; an independent head approximation is unnecessary. A finite inverse or signed Schur margin is outside this source budget.

The explicit outside-head object consists of rows448..2046 plus b_ij for i>2046. Its Hilbert-Schmidt norm is finite coefficient squares plus exact tail traces. For fixed j let i0 be the least integer>D with parity j and K=(i0-j)/2. Then

    sum_(i>D,sameparity) b_ij^2
      =sum_(k>=K)[1/(2k)^2-1/(2k+2j+1)^2]
      =-pi^2/12-H_(K-1)^(2)/4+sum_(r=0)^(K+j-1)1/(2r+1)^2.

Bracket pi^2 and use directed/exact rational arithmetic, retaining nonnegative lower bounds only when certified. No integration of log^2 products is needed. If later required, cross-tail Gram entries also reduce to finite harmonic differences: for j!=k of equal parity, divide the sum of

    1/(i-j)+1/(i+j+1)-1/(i-k)-1/(i+k+1)

over the same i>D parity progression by j(j+1)-k(k+1), then multiply sqrt((2j+1)(2k+1)). Opposite parity is zero. This does not replace actual rows448..2046 or their errors. V*V remains a different matrix from G_R.

## 5. ONE quantitative budget and stop

Propose fixed work3072 bits, V raw output256 bits, h output640 bits, q577 coefficients, band/sinc1024 terms, D2046, E448/eta1 unchanged. Streaming parity entries number458528. Do not build a dense Fraction monomial conversion. Seed work is about two million terms; rectangular recurrence/assembly is O(ND), not a cubic dense log moment calculation. Expected stdlib runtime is minutes, unmeasured; freeze one elapsed cap1800s and total derived packet cap160MiB. Stream JSONL with hashes to avoid huge Python object trees. No timing experiment or source production has been run.

For raw coefficient radii r_ij require the ACTUAL final check

    sum_(i<=D,j<N) r_ij^2/(g_i*g_j) <=2^-440.

This certifies global arithmetic Hilbert-Schmidt error <=2^-220, not an inherited old row allowance. The few-million3072-bit operations leave ample expected guard room, but observed directed widths decide. With the separately paid scalar, kernel and rank-two errors,

    ||V-Vhat||op <=2^-204+2^-227+9*2^-512+2^-600+2^-220 <2^-203,
    ||V-Vhat||HS <2^-198;  ||G_R-Ghat||op <2^-203.

Record the sharper actual component bounds, same pins, full shape/order/parity, symmetric head, h full norm checks, symbolic infinite tail, complement HS interval and source/roundoff ledger. Error in later inversion/shorting/whole Schur is not prepaid. Stop once on a failed source identity, scalar remainder, containment/width, actual shape/normalization, cap, or missing global approximation binding. Do not try another precision/rank/window/crop/source sequence. A too-large complement bound is valid data, not permission to drop it.

## 6. Actual input pins and scope

Prefix A=`literature/local/2026-10-29-weil-9-8/pilot/`; B=`reviews/2026-10-29/weil-9-8-admission/`. Bytes/SHA256 were read from actual files this task.

| Path | Bytes | SHA256 |
|---|---:|---|
| A/run-01/certificates/moments.json | 734638 | 2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9 |
| A/run-01/certificates/tail-columns.json | 296046 | d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e |
| A/source/02-produce.py | 6946 | 792ee1c93291459ca903b6f4f5e3c4f051f2463a1a020eac756b13fa6b913337 |
| A/source/08-produce.py | 9863 | ae0f487544c203905faecbb78b30f94fb16fe4f2f63c6b9846ca13ea673ba2b7 |
| A/source/11-checker_quotient.py | 7899 | ea6f8ed0e2780aa2835bb75f1a7e08fd807220ac4eb1b14f8c6aa0834e331af3 |
| A/source/12-raw_column_producer.py | 5460 | a8a67b4e08d540f51e152fe05bd19d77ae69fc618e4d6c08cb24c730b3afbb9c |
| B/full-weil-analytic-transfer-fresh.md | 13990 | 0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466 |

Feasible without new libraries, subject to root freeze and actual checks. No V/G values yet. This design earns zero mathematics; no whole S_ret/core/growing-window/Xi consequence is claimed. The bottleneck remains the signed whole comparison with its full complement.

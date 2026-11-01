# C071 actual row-tail attempt: common receiver control does not close the ratios

2026-11-01; /root/c071_rowtail_proof. This executes the row-tail part of the ONE C071 proof attempt, together with ROOT and the separate word-algebra proof. It is not a second contract or a new source gate. Read the active Goal/STATE/check/show, C071, actual input formation and consumption limits, and the needed old531/532/560/591/602 scopes. No source/web/PDF, scientific code/numerics, parameter change, authority-file/cadence edit or successor was used.

**Outcome.** There is a legal actual whole-word row envelope with logarithmic largest-prime size, and the old pointwise near/far inequality gives an explicit necessary normalized-tail condition. Neither provides an upper bound tending to zero for the ACTUAL ratio B_j(delta)/b_j. I do not prove either cofinal ratio verdict. The receiver-envelope consequence is standard strongest-old common-range control, not a new classical whole bound and not a new result merely because the formation memo issued a weaker sum-of-factors fee. The separate highest-prime proof supplies nonzero denominators, not their required source-energy size.

## 1. Exact row object, normalization and trace role

Keep C071's fixed word W_j, with all p<=exp(j) in ascending written order and the largest factor acting first. K_j denotes the operator W_j-I and its continuous Fourier kernel relative to dmu=dt/(2pi). Set

    J_j(t,v)=1/4 (|K_j(t,v)|^2+|K_j(v,t)|^2
                  +|K_j(-t,-v)|^2+|K_j(-v,-t)|^2),
    m_j(t)=integral J_j(t,v)dmu(v).

Then the actual reflection-averaged energy is

    C_j(r,r)=integral integral |rhat(t)-rhat(v)|^2 J_j(t,v)dmu(t)dmu(v).

All prime cross terms remain inside the actual K_j before squaring. This is not a sum of one-prime energies or an occupation kernel with an unproved rho_X dominance.

Unitarity gives the exact bounded-operator identity

    K_j K_j*=K_j* K_j=-(K_j+K_j*).

The finite projection-word expansion supplies continuous L2 row vectors; products therefore have their continuous integral kernels. Equality of the operators gives equality of these kernels and on the diagonal

    integral |K_j(t,v)|^2dmu(v)=-2 Re K_j(t,t),
    m_j(t)=-(Re K_j(t,t)+Re K_j(-t,-t)).                 (1)

This is a local kernel identity, not an assertion that K_j, A_r W_j or A_r I has an ordinary trace. It permits the actual B_j to be read from the actual word diagonal, but does not evaluate its cofinal size.

The real g of591 has G=g_hat=|psi_hat|^2 nonnegative, real-analytic, nonconstant and positive except at a discrete set. Thus, for each fixed j, the already paid continuous kernel shows

    b_j=C_j(g,g)=0 iff W_j=I.

If W_j is not I, the translation anomaly alpha_j=C_j(tau_(1/2)g)-b_j is also strictly positive: its integrand is 2G(t)G(v)(1-cos((t-v)/2))J_j, whose extra zero sets are null lines. This is only fixed-layer strictness; there is no uniform lower alpha_j/b_j. The separate sibling argument `whole-word-cofinal-comparison.md` proves actual nonidentity using the high-boundary symbol. I do not replace that proof with the fixed-layer kernel observation.

## 2. Actual common receiver, retaining every factor

Use the original positive-x model L2((0,infinity),dx), its unitary log coordinate, and the original unitary cosine transform F. Let X be the largest prime occurring in the finite word and let Q_X be the orthogonal projection onto

    N_X={f : f(x)=0 for x<1, (Ff)(x)=0 for x<1/X}.

For every p<=X, Ran Pi_p=B_p Ran P lies in N_X. Indeed B_p is a positive causal dilation combination, so it preserves the physical cutoff x>=1. The exact relation F U_logp=U_(-logp) F means its Fourier cutoff is at least 1/p, hence at least 1/X. No approximation to the full Gram inverse was made.

Therefore P, every Pi_p, and all reflection factors reduce N_X. Every V_p is I on N_X-perp, so the actual word obeys

    K_j=Q_X K_j Q_X,   ||K_j||op<=2.                    (2)

This is a genuine containment statement for this actual word. It does not put the graph projection or another contraction below the actual joint finite-Euler Pi_(F_j). N_X is a larger unequal-cutoff real-place Sonin receiver, not that arithmetic projection.

If d_X(t) is the evaluation-kernel diagonal of N_X in L2(dmu), (2) gives

    integral |K_j(t,v)|^2dmu(v)<=4 d_X(t).              (3)

This bound includes the entire word and every interference term. It does not add old602 onebody source errors to estimate the word.

## 3. A fully stated enlarged-Sonin evaluation bound

Here is the standard common-range consequence needed to make (3) useful. Put E=1_(0,1), C=E F E on EH, and kappa=||C||<1, the original real-place low-cutoff gap of531/532/602. Write d_0(t)=2pi rho_0(t) for the original P evaluation diagonal.

Dilation balances the unequal cutoffs of N_X to the common cutoff lambda=X^(-1/2); it multiplies Mellin evaluations by a unimodular phase and preserves their diagonal norm. Let f belong to this balanced Sonin space, and set D_lambda=1_(lambda,1), L=log(1/lambda). Since M_1=Ran P is contained in it, write

    f=P f+u+Fv,   u,v in EH.

This decomposition is unique: the map (u,v)->u+Fv has Gram matrix [[I,C],[C,I]], bounded below by 1-kappa, and its range is M_1-perp. Its normal equations are

    u+C v=D_lambda f,
    C u+v=D_lambda Ff.

Consequently

    ||u||+||v||<=2/(1-kappa) ||f||.

Use the plain unitary Mellin coordinate M_t f=integral f(x)x^(-1/2-it)dx. The cosine-transform Mellin multiplier from532 has modulus1 on this line. For w in EH the kernel of C is 2cos(2pi xy), so

    |Cw(x)|<=2||w||,   |M_t(Cw)|<=4||w||.

The two normal equations therefore show

    |M_t u|<=sqrt(L)||f||+4||v||,
    |M_(-t) v|<=sqrt(L)||f||+4||u||.

The weighted Mellin integrals in these formulas exist: D_lambda terms are separated from0, while C terms are bounded smooth functions there. The Mellin Fourier relation first holds in the unitary L2 transform and then uses these continuous representatives. Combining it with the native evaluation of Pf gives

    |M_t f|<=[sqrt(d_0(t))+2sqrt(L)+8/(1-kappa)]||f||.

This constructs the bounded evaluation on the enlarged space and yields the explicit envelope

    d_X(t)<=M_X(t):=3d_0(t)+6log X+192/(1-kappa)^2.      (4)

It is enough to establish the formula first on the projected compact smooth core and then extend by the bounded evaluations. The original projection formula and kappa<1 provide that core; no global unbounded Mellin evaluation on arbitrary L2 functions is used. In particular this proof does not separately assign an arbitrary low-supported L2 u a convergent critical Mellin integral: the two normal equations supply precisely the additional regularity used above.

The native d_0 is even and bounded by C[1+log(2+|t|)] from532/560. Combining (3), its reflected counterpart and the symmetrization gives

    0<=m_j(t)<=4M_X(t)<=C_kappa[1+log X+log(2+|t|)].    (5)

All constants are independent of the number/order of factors and t. Here the order remains the frozen C071 order; the estimate makes no claim that those factors commute.

## 4. What the actual absolute envelope does and does not pay

Let delta be EXACTLY591/C071's fixed min(1/2,sqrt(q1/[16(q0+1)])). Define the finite fixed-source constants

    T_1(delta)=integral_(|t|>delta) t^2G(t)^2dmu(t),
    T_0(delta)=integral_(|t|>delta) t^2G(t)^2d_0(t)dmu(t).

The actual row-tail therefore satisfies

    B_j(delta)<=12T_0(delta)
                 +[24log X+768/(1-kappa)^2]T_1(delta).  (6)

For the current word X<=exp(j), this is O_g,kappa(j+1). The same row envelope gives, for the original physical complex source on its paid Dlog domain,

    C_j(r,r)<=4 integral |rhat(t)|^2m_j(t)dmu(t)
             <=48t_0(r)
                 +[96log X+3072/(1-kappa)^2]||r||_(physicaldu)^2
             <=C_kappa(j+1)||r||Dlog^2.                (7)

The displayed numeric constants follow by inserting (4) into16 integral M_X |rhat|^2: 16*192=3072. The physical r-du norm is not unweighted f-du. The complete Gamma multiplier is present in t_0 and its original Dlog bound; this is a receiver/source upper estimate, not a new full Weil comparison.

This improves the weak issued sum-of-factors envelope only as a calculation. The stronger exact common-range control was already implied by the old cutoff/Gram/Fourier assets and unitarity, before that weaker formation bound was issued. Accordingly (6)-(7) must be deducted as standard strongest-old support. They are not a new whole-Q budget, favorable mixed/core result or new mathematics merely by comparison with the weaker printed bound.

Crucially, (6) is an upper bound which grows with j. It is not a lower bound on actual B_j, not a proof of its divergence, and not a quiet-tail estimate tending to zero. An upper bound on b_j from(7) cannot be used as a lower denominator in B_j/b_j. Even knowing b_j>0 for every j supplies no needed size comparison. Nothing in (2)-(7) gives B_j/b_j->0 or a nonzero limsup of either frozen energy ratio.

## 5. The exact normalized condition remains unpaid

For completeness, the near/far normalization can be closed without the occupation shortcut. Write

    b_j=C_j(g), alpha_j=C_j(tau_(1/2)g)-b_j>=0,
    d_j=C_j(gprime), R=q1/q0.

On the near square |t|,|v|<=delta, use G>=1/2 and 1-cos((t-v)/2)>=(t-v)^2/16. On a near/far rectangle use |t-v|<=2|v_far|. On the far square use the two diagonal square bound and merge the rows. This is the old591 pointwise argument, with the current C_j carrying the full jump integral rather than its half. It gives

    d_j<=2delta^2 b_j+32alpha_j+16B_j(delta).           (8)

Thus, on b_j>0, C071's discrepancy obeys the standard support inequality

    Delta_j >= [R-2delta^2-16B_j(delta)/b_j]_+ /33.     (9)

Matching the three targets by one common positive calibration would force

    liminf B_j(delta)/b_j
       >=(R-2delta^2)/16 >=7R/128>0.                  (10)

This is a necessary condition, not an upper estimate and not a cofinal rejection. Equations(8)-(10) use the actual word row, not rho_X; replacing that row by the quiet occupation rho_X is still unproved and would change the object. A direct proof of the ratios is not logically required to use this tail sufficient route, and the tail sufficient route is not a necessary characterization of all possible ratio failures.

The actual remaining comparison is precise: with the word itself fixed, establish a bound on B_j/b_j or a direct estimate of alpha_j/b_j and d_j/b_j that has a strict cofinal consequence. No such comparison is closed by this attempt. The denominator nonzero result in the sibling proof does not pay it. I have not changed the word/order/cutoff/gain/source/receiver to obtain a more convenient test.

## 6. Consumption boundary

Classification of this row attempt: exact local identities and standard strongest-old absolute receiver control; actual normalized cofinal comparison OPEN. No new classical consequence, no full mixed/all-source/Dprime limit, no principal405 descent, no537 full-coverage or sections/mixedRR input, no change to the growing signed-core/coupling/ordinaryXi gap. The strongest old whole17/16, finite9/8, same605 one-head/all-complement completion and whole4/5 negative-inertia UPPER remain unchanged.

This is a terminal output for ROOT and a different-organization reverse review. It neither settles C071 on its own nor authorizes renewal. If the other actual-word proof and ROOT cannot close the normalized comparison, the one attempt should stop with that exact unknown, not announce rejection, pass, a general unitary boundary or a new source queue.

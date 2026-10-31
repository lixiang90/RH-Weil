# Retained-tail source design: independent limited inverse check

2026-10-31. Audit target `source-design.md`: 10986 bytes, SHA256 `55373dda47da0f18e01fd6c0d75e71bb91cac0091cf199ed843d951911a16e2c`. Same active Goal1793085111; C066 spent/latest603. Recovered README/STATE/check/show, Goal, C066/BD/frontier and actual tree. This audit writes only this file, does not amend the target, run actual448 science, produce V/G arrays, change STATE/cadence/library/Git or claim a mathematical iteration. The already closed realspace Gamma representation is an input, not re-audited here.

**Verdict: conditional analytic/design PASS, with an explicit recurrence-domain correction required in the producer.** The K_1j formula must be used only for odd j; even j must take the exact parity-zero branch before recurrence. The design's instruction to store parity zeros can implement this correction. All actual width, scalar, full-function binding and budget checks remain execution conditions, not already observed source certificates.

## 1. Log Gram and its complete infinite tail

On (-1,1), define Lambda_ij=integral P_i P_j log(1-z²). Opposite parity vanishes. For n>m of equal parity, put lambda_n=n(n+1). Legendre's differential equation and integration by parts give

    (lambda_n-lambda_m)Lambda_nm
       = -2 integral z(P_n'P_m-P_nP_m') dz = -4.

For the last equality, orthogonality kills the lower-degree terms, while integration by parts gives integral zP_n'P_m=[zP_nP_m]_-1^1=2. Boundary terms with (1-z²)log(1-z²) vanish. Thus the design's offdiagonal formula -4/[(n-m)(n+m+1)] has the correct sign and factor.

For the diagonal, differentiate the Jacobi norm along alpha=beta=s at s=0. The logarithmic derivatives of its norm and leading coefficient are respectively

    2log2-2/(2j+1),       2(H_(2j)-H_j).

The derivative of the polynomial contributes twice the second expression times the Legendre norm 2/(2j+1). This gives exactly

    Lambda_jj=4/(2j+1)[log2-1/(2j+1)-2(H_(2j)-H_j)].

Physical raw entries of the endpoint term are -L Lambda_ij/2. Dividing by sqrt(g_i g_j), g_i=2L/(2i+1), gives for i>D>=j

    b_ij=sqrt((2i+1)(2j+1))/[(i-j)(i+j+1)]

on equal parity, zero otherwise. This is a coefficient of the ACTUAL endpoint-log H function, not an estimate of a discarded residual. In particular,

    b_ij²=1/(i-j)²-1/(i+j+1)².

Let i0>D be the first row of parity j and K=(i0-j)/2. Summing over i=i0+2l gives

    sum_(i>D) b_ij²
      =-pi²/12-H_(K-1)^(2)/4+sum_(r=0)^(K+j-1)1/(2r+1)².

The negative pi²/12 is correct: the full even reciprocal-square sum contributes pi²/24 and the odd sum contributes pi²/8. The finite expressions may cancel strongly, so an interval intersected with [0,infinity) must still contain the exact value; an uncertified positive point value is not allowed.

For j!=k of equal parity, set A_j=(i-j)(i+j+1)=i(i+1)-j(j+1). Then

    (2i+1)/(A_j A_k)
      ={1/(i-j)+1/(i+j+1)-1/(i-k)-1/(i+k+1)}
        /[j(j+1)-k(k+1)].

Multiplication by sqrt((2j+1)(2k+1)) proves the cross-tail formula, including its denominator sign. Along the fixed parity progression its divergent-looking individual harmonic series must be grouped into the displayed convergent differences before evaluation; the remaining differences telescope to finite rational sums. Diagonal tail traces suffice for an HS norm; a later Gram computation must not confuse this V*V information with G_R=E*V.

## 2. Right-boundary seed, parity and rectangle

Write kappa(z,w)=sum alpha_m (|z-w|/2)^m and K_rj=double_integral P_r(z)kappa(z,w)P_j(w) dz dw. The seed in the design is specifically the RIGHT-boundary moment

    b_j=integral kappa(1,w)P_j(w)dw
       =2(-1)^j sum_(m>=j) alpha_m (m!)²/[(m-j)!(m+j+1)!].

The sign comes from (1-w)^m, not (1+w)^m. For each m the factorial quotient starts at 1/(m+1), and its j-to-j+1 ratio (m-j)/(m+j+2) is correct and in [0,1]. The left-boundary moment is (-1)^j b_j.

Use F_j=(P_(j+1)-P_(j-1))/(2j+1), j>=1, and partial_z kappa=-partial_w kappa a.e. Boundary integration gives

    K_00=2(b_0+b_1),
    K_0j=2(b_(j+1)-b_(j-1))/(2j+1),   j even>=2,
    K_1j=[K_0,j-1-K_0,j+1+2(b_(j+1)-b_(j-1))]/(2j+1), j ODD.

The last parity domain is essential. For the single kernel |z-w|/2, true K_12=0 but its unrestricted displayed formula would give 2/15. This is not a reason to change the correct odd-j recurrence; it is a reason to enforce K_rj=0 whenever r+j is odd before evaluating recurrences. No formula using j-1 is legal at j=0; use symmetry for that position.

For r>=2, j>=1, integrating the derivative of P_r-P_(r-2) gives

    K_rj=K_(r-2),j
       -(2r-1)[K_(r-1),j+1-K_(r-1),j-1]/(2j+1).

It is valid for these continuous absolute-power kernels: first derivatives exist piecewise, no jump in kappa creates an internal boundary mass. The sign is minus. Evaluate with r=min(input,output), j=max(input,output), enforce parity first, and retain enough upper seed columns to close j+1 dependencies. Maximum input+output is 447+2046=2493; boundary moments through2494 suffice. Physical raw entries multiply these dimensionless double integrals by L² exactly once. Alpha_m must already encode the physical kernel's change of argument; there is no further 2^m or L^m conversion after this step.

A small exact-rational check, independent of the recurrence, integrated monomial powers over the two triangles z>=w and z<=w. It verified 128 seed/odd-row/rectangle identities for kernels (|z-w|/2)^m, 0<=m<=7, with indices at most8. It also exhibited the even-j counterexample above. These are limited symbolic controls, not the actual448 computation. A separate read-only agent confirmed the log/tail/seed algebra and physical scaling.

## 3. Degree2046 is consistent with q degree576

The q approximation contains c_0,...,c_576, exactly577 coefficients. Its convolution against native P_j, j<=447, is polynomial degree at most1023 (the largest odd m is575). Separately, the band and sinc approximations contain1024 EVEN terms, powers0,2,...,2046. The number576 in their coefficients is 2L*Omega, not their degree. Thus D=2046 covers all polynomial output; exact endpoint-log coefficients continue beyond D. A producer that projects or zeros those log coefficients at D changes the H object and loses the stated error ledger.

The full finite rectangle has2047*224=458528 parity-compatible entries, while its analytic endpoint tail is infinite. Raw rational centers with exact Gram congruence may represent native coefficients symbolically; any decimal approximation to sqrt(g_i g_j) requires its own included arithmetic error. Exact rational squared-norm tests can avoid that approximation.

## 4. Gamma constant by a positive-real Binet bound

For z>0 the Binet integral is

    psi(z)=log z-1/(2z)-2 integral_0^infinity
               t/[(t²+z²)(exp(2pi t)-1)] dt.

Expand 1/(t²+z²) through K terms. The omitted psi remainder has absolute value at most

    2(2K+1)! z^(-2K-2) zeta(2K+2)/(2pi)^(2K+2).

At K=256, z=256, use zeta(514)<2 and 2pi>6 to obtain the design's symmetric bound

    R <=4*513!/(6^514*256^514).

Exact stdlib integer/Fraction comparison performed here proves this is <2^-1500, hence also <2^-1400. Its reduced numerator and denominator have2970 and4524 bits. Since psi(256)=H_255-gamma, the design's gamma=H_255-psi(256) has correct index/sign. The Bernoulli contribution in psi is minus sum B_(2k)/(2k z^(2k)); hence in gamma it is plus. A symmetric remainder avoids needing a one-sided sign implementation. This does not yet certify any generated gamma/contact interval: the actual Machin/log interval and final radius tests must still pass.

## 5. Old global sources are usable only under the exact binding

I read the pinned old02 and old12 code and the accepted full analytic transfer record, especially its section5. They support the proposed global reconstruction, rather than a promotion of the old finite448 coordinates:

* With theta_q=(Omega/pi)integral_0^1 x^(2q)(Gamma(Omega*x)-7/2)dx, the SAME midpoint band kernel has coefficient (-1)^q theta_mid,q*576^(2q)/(2q)! in (|u-v|/(2L))^(2q). The old1024 true intervals include Binet error already. Their midpoint radius<=2^-1098 and the old uniform Taylor estimate yield the full original-H operator fee <2^-204. The larger914 constant also permits a pole allowance and is conservative for the band alone. Do not add/subtract a pole in V when reconstructing band-only theta.
* The SAME sinc polynomial uses the old exact Machin160 rational p_pi, not a newly rounded substitute. Its operator error from the true sinc band is <2^-513+2^-646 on full H. It has degree2046 and acts on p_0,p_1 to give whole polynomial functions. A new full-degree normalized rounding check <2^-520, plus that global error, proves ||h_s-hhat_s||<2^-512. The old896-coordinate widths alone do not prove it.
* With original normalized h_0,h_1 bounds1/29 and3/50, rank-one difference gives, for eps=2^-512,

      ||U_old-Uhat|| <=(162/29+162/50)eps+108eps² <9eps.

  Exact rational comparison checked 162/29+162/50=6399/725 and 6399/725+108*2^-512<9. Raw columns w_s=S p_s satisfy h_s=w_s/sqrt(g_s), so81/g_0=27/g_1=36. The proposed raw update36 sum t_is*t_js is correct, and the full polynomial w_s centers used here must be exactly those used in assembly.

These old global bounds require replayed identity/pin/argument checks, including original H measure and L² transfer, not merely matching labels. Old head row allowance2^-220 cannot substitute for a new whole-column rounding certificate. The old moment remainder must not be charged again; a different kernel/precision/degree cannot inherit this binding automatically. Original prime-powers and both pole signs stay in Llow/Q, and are not erased by a band-only reconstruction.

## 6. Model/rounding semantics and consumption conditions

Define the unrounded analytic approximant W first: same centered band/sinc polynomials, exact q polynomial and endpoint-log H functions, with its scalar convention fixed and separately paid if approximate. Define Vhat by the FINAL finite raw output centers, exact symbolic native normalization, and the unchanged infinite endpoint tail. Let r_ij genuinely enclose <p_i,W p_j> minus each output center, including scalar intervals, recursive arithmetic, copied symmetric entries and any normalization approximation. The ACTUAL final check

    sum r_ij²/(g_i*g_j)<=2^-440

then pays finite arithmetic HS<=2^-220 and therefore op<=2^-220. This is a rectangular global-H check, not a row-sum inheritance or a max-column estimate. If contact scalar/log2 errors are already carried in those radii, separately charging a scalar bound is conservative; otherwise they require an explicit scalar-I fee. A contact interval alone does not silently cover a separately used unbracketed log2.

For global kernel/rank-two errors acting on E, operator fees retain their dimension-free values, while HS fees multiply by sqrt448. Keeping the finite arithmetic HS fee separately gives

    ||V-Vhat||op <2^-204+2^-227+9*2^-512+2^-600+2^-220 <2^-203,
    ||V-Vhat||HS <sqrt448*(2^-204+2^-227+9*2^-512+2^-600)+2^-220
                    <2^-198.

These claims are conditional on the actual checks above; work3072 alone proves neither. The source model's first448 rows, copied from one symmetric triangle, must define Ghat=E*Vhat exactly. Then ||G_R-Ghat||op<2^-203 follows by compression. An independent head estimate or Vhat*Vhat is not that consistency certificate.

Likewise the represented complement norm from rows448..2046 and the exact endpoint tail must be labeled as the MODEL norm. For the actual source, triangle inequality adds eps_HS to its upper norm bound (and subtracts it for a lower bound, clipped at0). Squared-norm or Gram bounds require the corresponding norm-dependent propagation; they do not inherit the same additive scalar unchanged. Later inversion, U_ret formation, signed head or whole Schur fees remain unpaid.

## 7. Stop and net scope

The ONE3072-bit/256-output/640-h/1800s/160MiB proposal is coherent as a bounded source attempt, subject to root freeze and the recurrence parity annotation. This review does not establish runtime feasibility or actual source widths. On a failed check/cap/missing global binding the design stops once; no implicit precision/rank/window successor is granted. The strongest-old R positivity and tiny floor already imply nonzero shorting, so a correct source representation alone has zero new whole-object consequence. Actual V/G data and a signed whole comparison with complement coupling remain unproduced here; the core/cross/growing-window/Xi bottleneck is unchanged.

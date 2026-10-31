# Retained-tail source representation: analytic PASS, source values unpaid

2026-10-31. Read-only mathematical check for the one source gate, not C067/604 or a research iteration. Fixed original complex physical space H=L²(I,dx), I=(-L,L), L=9/8, original native E=E448, eta=1 and Omega=256. Recovery used current STATE/check/show, active Goal, C066/BD/frontier and `direct-weil-core-admission/retained-tail-next-admission.md`. No new paper, numerical source arrays, library/state/cadence/Git changes. This file supplies a derivation, not an actual V/G packet.

## 1. Objects and accepted dependencies

Use Ff(t)=integral f(x) exp(-itx) dx and receiver measure dt/(2pi). J is zero extension from H; B=FJ. Write

    Gamma(t)=Re psi(1/4+it/2)-log(pi),
    e_j(x)=sqrt((2j+1)/(2L)) P_j(x/L), 0<=j<=447,
    A_Gamma = compressed full Gamma multiplier (defined by its closed form).

The following old inputs are accepted in their recorded scope, not reproved here: full original archimedean multiplier/contact and Fourier convention; tail form/operator T from symbol 1_(|t|>256)(Gamma(t)-7/2); old T>=tau I+U_old with tau=2^-49158/16 and the same certified 81/27 rank-two U_old; and the old Llow decomposition including every prime-power and both pole signs. U_old is a bounded operator on original H, not a map in an unnormalized serialized coordinate space. The preceding admission proves native e_j belong to D(T), rather than merely the form domain Dlog. We also check that fact below for this representation.

Here E:C^448->H is the native isometry, V=RE with R=T-tau I-U_old. E*V=G_R is the retained-tail form compression; it is NOT V*V or the old inverse-M Gram. Positivity, shorting and the tiny old floor are accepted standard/old facilities, not a new signed whole-object consequence. Every formula below is fixed-window, all complex sources in the stated spaces; no growing-L, growing-degree or Xi quantifier is claimed.

## 2. Digamma kernel and operator meaning

Set b(v)=exp(-v/2)/(1-exp(-2v))=exp(v/2)/(2sinh(v)) for v>0. The ordinary convergent digamma difference series, followed termwise by the Laplace integral, gives

    Gamma(t)-Gamma(0) = 2 integral_0^infinity b(v)(1-cos(tv)) dv.       (1)

Indeed substitute s=2v in the psi kernel exp(-s/4)/(1-exp(-s)); this is where the factor 2 is fixed. For p polynomial on I and zero outside, (1) gives in H

    A_Gamma p(x) = Gamma(0)p(x)
      + integral_0^infinity b(v)[2p(x)-Jp(x+v)-Jp(x-v)] dv.          (2)

There is no extra 2pi in (2): it is the inverse of the multiplier 2(1-cos(tv)) with the stated receiver measure. At infinity the realspace integral is exponentially integrable. At zero, zero-extended p is compact BV, so its translation difference in L² is O(sqrt(v)); multiplying by b(v)=O(1/v) is integrable. Thus (2) is an H-valued integral, even though pointwise inverse Fourier absolute convergence is not asserted.

For an independent domain check, integration by parts gives

    |B e_j(t)| <= [|e_j(-L)|+|e_j(L)|+||e_j'||_1]/|t|.

Since Gamma(t)=O(log(2+|t|)), Gamma B e_j is in L²(dt/(2pi)). Testing against the closed-form domain identifies e_j in the operator domain of A_Gamma and T, with (2) its actual operator value. Bounded subtraction of tau I+U_old gives e_j in D(R). Equivalently, truncated versions of (1) converge in L² by domination with Gamma-Gamma(0). Endpoint logarithms below are in L²(I); endpoint point values are unnecessary.

## 3. Regional Legendre identity and endpoint/contact constant

On (-1,1), let Dp(x)=integral_-1^1 (p(x)-p(y))/|x-y| dy. Splitting at y=x gives, for n>=1,

    D x^n = 2 H_n x^n
      - sum_(k=0)^(n-1) [1+(-1)^(k+1)] x^(n-1-k)/(k+1).

Thus D preserves each polynomial degree and has leading coefficient 2H_n. On polynomials it is symmetric, because

    <Dp,q> = (1/2) double_integral
       (p(x)-p(y)) overline(q(x)-q(y))/|x-y| dx dy.

Consequently DP_n is orthogonal to every lower degree and DP_n=2H_n P_n (also D1=0). Scaling to I introduces no L factor. The regional kernel 1/(2|x-y|) therefore contributes H_j e_j.

Write q(v)=b(v)-1/(2v) and d_plus=L-x, d_minus=L+x. An exact antiderivative is

    K0(d)=integral_d^infinity b(v)dv
         =atanh(exp(-d/2))+atan(exp(-d/2)),
    c0=lim_(d->0+) [K0(d)+(1/2)log(d)]=log(2)+pi/4,
    integral_0^d q(v)dv = c0-K0(d)-(1/2)log(d).

Split (2) into its regional b part and the two exterior endpoint tails K0(d_plus)+K0(d_minus). Splitting b=1/(2v)+q inside I, the diagonal q terms plus those exterior tails equal 2c0-(1/2)log(d_plus d_minus). Finally

    Gamma(0)=-gamma-pi/2-3log(2)-log(pi),
    Gamma(0)+2c0=-gamma-log(2pi).

This proves, as an equality of operator values in H (and a.e. inside I),

    A_Gamma e_j(x)
      =[H_j-gamma-log(2pi)-(1/2)log(L²-x²)]e_j(x)
       - integral_I q(|x-y|)e_j(y)dy.                              (3)

Both the sign of the convolution and the full contact in (3) are fixed. As a simple symbolic check, j=0 and x=0 in (2) gives Gamma(0)+2K0(L), agreeing with (3). No endpoint Dirac mass or adjustable contact is added.

For a producer using z=x/L, the unnormalized P_j version of (3) has constant H_j-gamma-log(2pi L), endpoint term -(1/2)log(1-z²), and convolution -L integral_-1^1 q(L|z-w|)P_j(w)dw. The native normalization factor still multiplies the complete result.

## 4. Degree-576 q approximation with a full H operator error

The function

    q(z)=exp(z/2)/(2sinh(z))-1/(2z)

has a removable singularity at zero, q(0)=1/4, and its next poles at +/-i*pi. Its Taylor coefficients are exactly rational:

    q(z)=sum_(m>=0) c_m z^m,
    c_m=2^m B_(m+1)(3/4)/(m+1)!.

This follows by the Bernoulli-polynomial generating function with t=2z. Initial coefficients are 1/4, -1/48, -1/32; these are symbolic checks, not measured source data.

Here is a conservative elementary Cauchy certificate. On |z|=3, write z=x+iy. Since |sinh z|²=sinh²x+sin²y, if |x|>=1/10 then |sinh z|>=1/10. Otherwise sqrt(8.99)<|y|<=3, so |sin y|>=sin(3)>69423/492800>1/10; the displayed rational lower bound is the sine Taylor partial sum through degree 11, whose next alternating remainder is positive. Hence

    sup_(|z|=3)|q(z)| <= 5exp(3/2)+1/6 <32<512.

The weaker frozen 512 is therefore valid. Cauchy gives |c_m|<=512/3^m. Freeze **degree M=576, including c_0,...,c_576 (577 coefficients)**. Because 0<=|x-y|<=2L=9/4,

    sup_[0,9/4] |q-q_576|
       <=2048(3/4)^577 =: eps_kernel,
    ||Q_q-Q_q576||_(H->H)
       <=(2L)eps_kernel=4608(3/4)^577=:eps_q <2^-227.              (4)

The operator step is Schur's test on the full interval, not a finite-coordinate estimate. The last strict inequality is exact: it is equivalent to 3^579<2^918; use 579=14*41+5, 3^41=36472996377170786403<2^65 and 3^5=243<2^8. Degree 575 / 576 coefficients does NOT earn (4).

Thus (4) controls (Q_q-Q_q576)E as a C^448->H operator and its native head compression; the aggregate Hilbert-Schmidt column bound is at most sqrt(448)eps_q. The bound does not grow with the native column index. Integrating |x-y|^m times a polynomial exactly gives a polynomial: even m gives degree at most m; odd m, after splitting at y=x, gives degree at most j+m+1. For these j,M the maximum is 1023. Rational L, c_m and P_j coefficients make this polynomial algebra exact up to the explicitly retained native square-root normalization. The endpoint-log times e_j in (3) remains an actual H function; replacing it by a finite polynomial head incurs a separate unpaid tail.

## 5. Actual V representation and the unpaid source-error ledger

Let

    Kband = B* [1_(|t|<=256)(Gamma(t)-7/2)] B.

Since B*B=I, the exact tail operator on the native columns is

    T e_j=A_Gamma e_j-(7/2)e_j-Kband e_j,
    V_j=[A_Gamma-(7/2+tau)I-Kband-U_old]e_j.                      (5)

Equations (3)-(5) give endpoint-log times polynomial + explicit polynomial + the old bounded band/rank-two functions. If the old source instead names Kcompact=Kband+Pole, use Kband=Kcompact-Pole with BOTH pole signs, including the negative odd Lorentz contribution. No prime operator is silently introduced into V; every prime-power and both poles remain in the original whole Q/Llow decomposition.

This derivation has NOT supplied a certified whole-function representation of Kband E or U_old E. The old finite 448x448 J0 compression and old 896 tail coordinates do not by themselves supply those H-valued columns. The producer must recover the SAME global band-kernel / old rank-two function approximants and their full L² errors, including outside-head components. In particular, a finite native row allowance (e.g. 2^-220), a serialized coordinate center, or finite tail coordinates cannot be promoted to a global H column/operator error. Any old global kernel truncation bound is usable only after its actual kernel, coefficient, domain and norm transport are matched. This is a remaining source-design payment, not a failure of (3).

Conditionally, if the producer proves full operator errors eps_band for Kband, eps_old for U_old, and scalar eps_contact, eps_tau on original H, then using exact endpoint logs and the native isometry gives

    ||Vhat-V||_(C^448->H)
       <=eps_q+eps_band+eps_old+eps_contact+eps_tau = eps_V,
    ||E*Vhat-G_R|| <= eps_V.

For columnwise-only certificates one must instead pay the corresponding joint/HS norm; no free replacement by max-column error. G_R consistency must use the same V columns and normalization, and G_R is E*V, never V*V. Rounding/error in subsequent formation or inversion of G_R+I is an additional payment, not covered here.

## 6. Admission and strongest-old comparison

Limited conclusion: **the proposed full realspace representation and degree-576 global q remainder PASS analytically**. A separate read-only check by `legendre_kernel_check` confirmed the regional eigenvalue, circle bound and exact tail inequality. The source gate may freeze this representation before any production, subject to the remaining global band/old-function errors above. There are still no new actual V/G values, signed C_ret margin, outside-head coupling bound or whole S_ret margin.

This is standard kernel/digamma and polynomial machinery, not a new theorem attribution; a broad text search was not exhaustive enough to claim the formula absent from the repository. The strongest accepted old consequence already makes R positive, G_R positive and U_ret nonzero. Neither this representation nor eps_q alone improves that whole-object consequence. New actual columns could supply information unavailable from old A/B/J0 or S v_0/v_1, but that is an unexecuted source-data possibility, not a root-consumed result. Source feasibility/design earns zero mathematical iterations and does not remove core/cross/growing-window/Xi bottlenecks.

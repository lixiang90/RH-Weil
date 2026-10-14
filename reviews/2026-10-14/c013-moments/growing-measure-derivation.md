# C013 independent derivation: actual all-band high moments and growing bad-set budget

2026-10-14. Owned output of `/root/c013_growth_measure`; no STATE, cadence or Git
mutation. Recovered AGENTS, README, STATE, check/show, current Goal/frontier/C013
and D20261014N. Working HEAD observed `6657ca447bba75a03c8a7e947f244806de64d7ec`.
This is an independent analytic derivation, not a numerical scan or a completion audit.

## 1. Result, exact object and scope

For (L\ge1), put (X=e^{2L}) and retain every actual prime power strictly below X:

\[
P_L(t)=\sum_{p^j<X}\frac{\log p}{p^{j/2}}e^{it\log(p^j)},\qquad
S_L=\sum_{p^j<X}\frac{\log p}{p^{j/2}}.
\]

The multiplier is

\[
b_L(t)=\Gamma(t)-2\operatorname{Re}P_L(t),\quad
\Gamma(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi=2\theta'(t),\quad
E_L=\{t\in\mathbb R:b_L(t)<1\}.
\]

No half-Gamma convention, removal of proper powers, pole simplification or unknown
zero location enters the estimate. The proof below gives a finite, exact all-band
upper ledger (U_L) and, without PNT,

\[
\log(1+|E_L|)\le\log(1+U_L)
\le S_L+O\!\left(\frac{S_L\log L}{L}+L^3\right)
=(1+o(1))S_L. \tag{1}
\]

The constants are absolute. This improves the leading exponent of the old
absolute cutoff/second-moment ledger, (2S_L+o(S_L)). It is only an upper bound:
it neither determines the actual size of E nor establishes PSD/RH. Most
importantly, it does **not** improve the strongest already-paid whole-inertia
baseline: the original exact degree profile yields the smaller remainder
(S_L+A(e^L)+O(L)), as checked in §7 below. Thus this measure result does not
meet C013's required strict net whole-spectrum improvement. Transport to the
complete Weil inertia must retain the odd negative pole and the original
complex source domain; that separate bridge is the root's responsibility.

## 2. Independent input and finite high moment, with complete length cost

The independent external input is Montgomery--Vaughan, *Hilbert's Inequality*
(1974), Theorem 2 and Corollary 2, in the
[author-hosted original](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).
For a finite Dirichlet polynomial (A(t)=\sum_{n\le N}a_n n^{it}), the minimum
spacing of its distinct log-frequencies is at least (1/N). The two endpoint
Hilbert terms therefore give

\[
\int_T^{2T}|A(t)|^2dt\le(T+2\pi N)\sum_n|a_n|^2. \tag{2}
\]

An interval shift changes only coefficient phases. The constant is independent
of N, T and the number of nonzero coefficients. No condition (T\ge N) is
needed to apply (2); that condition will be enforced when bounding its cost.

Separate

\[
P_1(t)=\sum_{p<X}a_p p^{it},\quad a_p=\log p/\sqrt p,\qquad
V_L=\sum_{p<X}a_p^2,\qquad
R_L=\sum_{p^j<X,\ j\ge2}\log p/p^{j/2}.
\]

For every integer (k\ge1), unique factorization identifies the coefficient
of the exponent vector \(\alpha\), \(\sum_p\alpha_p=k\), in (P_1^k) as

\[
c_\alpha=\frac{k!}{\prod_p\alpha_p!}\prod_pa_p^{\alpha_p}.
\]

Repeated primes are included. Since (k!/\prod\alpha_p!\le k!),

\[
\sum_\alpha|c_\alpha|^2
\le k!\sum_\alpha\frac{k!}{\prod\alpha_p!}\prod_pa_p^{2\alpha_p}
=k!V_L^k.
\]

Each product integer is (<X^k). Taking (N=\lceil X^k\rceil) in (2) yields

\[
\int_T^{2T}|P_1(t)|^{2k}dt
\le(T+2\pi\lceil X^k\rceil)k!V_L^k. \tag{3}
\]

This is valid for arbitrary k, including k growing with L/T, and has no omitted
collision cost. Factorial/MV tools themselves are baseline assets; the new
candidate consumption is their actual all-band growing budget in (1).

## 3. All proper powers, actual Gamma lower bound and terminal cutoff

The exact uniform bound is (|P_L-P_1|\le R_L); it is never replaced by zero.
For t≥1, Binet's formula for (z=5/4+it/2), followed by
\(\psi(1/4+it/2)=\psi(z)-(1/4+it/2)^{-1}\), gives

\[
\Gamma(t)\ge\log(t/(2\pi))-\frac{46}{15t}
\ge\log t-G,\quad G=\log(2\pi)+46/15. \tag{4}
\]

For clarity, the Binet integral remainder has absolute value at most (1/(15t)),
because (|v^2+z^2|\ge5t/4) and
\(\int_0^\infty v/(e^{2\pi v}-1)\,dv=1/24\). The reciprocal terms have
absolute real-part costs at most (1/t) and (2/t); (
\operatorname{Re}\log z\ge\log(t/2)). These conservative costs total 46/(15t).
This uses the [NIST Binet digamma formula](https://dlmf.nist.gov/5.9#E15),
with the same normalization paid in 541.

Set

\[
Y_L=2S_L+G+1,\qquad\Omega_L=e^{Y_L}.
\]

For (|t|\ge\Omega_L), evenness of Gamma and (4) imply

\[
b_L(t)\ge\log|t|-G-2S_L\ge1.
\]

Thus E is bounded, measurable (indeed open), and lies in

\[
E_L\subset(-\Omega_L,\Omega_L). \tag{5}
\]

For a positive-frequency band ([T,2T]), (T\ge1), define the explicitly
certified threshold

\[
D_L=G+1+2R_L,\qquad u_L(T)=(\log T-D_L)/2.
\]

If (u_L(T)>0), (b_L(t)<1) forces \(\operatorname{Re}P_1(t)>u_L(T)\),
so (3) gives the complete band ledger

\[
|E_L\cap[T,2T]|\le
\min\left\{T,\frac{(T+2\pi\lceil X^k\rceil)k!V_L^k}{u_L(T)^{2k}}\right\}.
\tag{6}
\]

If (u_L(T)\le0), its payment is the whole T. There is no division by a
nonpositive threshold. All negative-frequency costs are exactly doubled,
because coefficients are real and b is even.

## 4. Self-contained elementary arithmetic growth, no PNT

Let \(\Psi(x)=\sum_{n\le x}\Lambda(n)\) and \(\Theta(x)=\sum_{p\le x}\log p\).
Central binomial coefficients give both elementary Chebyshev estimates needed
here. Every prime-power valuation of \(\binom{2n}{n}\) is a sum of 0/1 carries,
so

\[
\log\binom{2n}{n}\le\Psi(2n),\qquad
\Psi(2n)-\Psi(n)\le\log\binom{2n}{n}\le2n\log2.
\]

The lower bound \(\binom{2n}{n}\ge4^n/(2n+1)\) yields
\(\Psi(x)\ge(x-2)\log2-\log(x+1)\ge(\log2)x/2\) for x≥16.
Summing the upper dyadic bound at powers of 2 and enlarging x to its next power
of 2 gives

\[
\Psi(x)\le Cx\quad(x\ge1),\quad C=4\log2,
\qquad\Theta(x)\le\Psi(x). \tag{7}
\]

Partial summation then gives, for L≥1,

\[
V_L\le2LC(1+2L),\qquad
R_L\le C(1+L)+K_{\rm pp}, \tag{8}
\]

where

\[
K_{\rm pp}=\frac1{1-2^{-1/2}}
\sum_{n\ge2}\frac{\log n}{n^{3/2}}<\infty.
\]

For R the j=2 terms use \(\sum_{p<e^L}\log p/p\le C(1+L)\); all j≥3
terms are bounded by Kpp. Thus the proper-power l¹ fee is O(L), not O(1).
For V use \((\log p)^2/p\le(2L)\log p/p\).

For S, Stieltjes partial summation and (7) give \(S_L\le2Ce^L\).
The subsum n≤X/2, all strictly below X, gives for X/2≥16

\[
S_L\ge\frac{\Psi(X/2)}{\sqrt{X/2}}
\ge c e^L,\qquad c=\frac{\log2}{2\sqrt2}. \tag{9}
\]

Consequently

\[
\log S_L=L+O(1),\quad V_L=O(L^2),\quad R_L=O(L),
\quad L^3=o(S_L). \tag{10}
\]

No PNT asymptotic such as S~2e^L is used. Strict n<X versus n≤X cannot
invalidate either direction: the upper estimate enlarges the sum and the lower
estimate uses n≤X/2.

## 5. Analytically frozen head, all bands, k and rounding

For every L≥1 the prime 2 is present, so V>0. Define

\[
M_L=4V_L/L,\qquad
H_L=\max\{L^3,4D_L,4L,4M_L\},\qquad T_0=e^{H_L}.
\]

Charge the whole head (|t|\le T_0) at cost (2T_0), including every low-T
band with nonpositive u. This head has logarithmic cost O(L³) by (8).
If Y≤H, there are no other bands. Otherwise set

\[
J_L=\left\lceil\frac{Y_L-H_L}{\log2}\right\rceil,
\quad T_j=T_0 2^j,\quad y_j=\log T_j,
\quad k_j=\left\lfloor\frac{y_j}{2L}\right\rfloor,
\quad0\le j<J_L. \tag{11}
\]

The final band may overshoot Ω; (6) is still applied to its full interval, so
this only overpays. Every used band has H≤yj<Y, uj>0 and kj≥1.
In particular (X^{k_j}=e^{2Lk_j}\le e^{y_j}=T_j), hence

\[
T_j+2\pi\lceil X^{k_j}\rceil
\le(1+4\pi)T_j. \tag{12}
\]

The exact finite all-band ledger promised above is

\[
U_L=2e^{H_L}+2\sum_{j=0}^{J_L-1}
\min\left\{T_j,
\frac{(T_j+2\pi\lceil X^{k_j}\rceil)k_j!V_L^{k_j}}
{((y_j-D_L)/2)^{2k_j}}\right\}, \tag{13}
\]

with J=0 when Y≤H. This fixes parameters analytically; it is not a fitted
frequency or moment-order optimization.

Since y≥4D,

\[
\frac{kV_L}{u^2}
\le\frac{2V_Ly}{L(y-D_L)^2}
\le\frac{4V_L}{Ly}=\frac{M_L}{y}\le\frac14.
\]

Using (k!\le k^k), (k\ge y/(2L)-1), and the negativity of
\(\log(M_L/y)\), (6)–(12) imply

\[
|E_L\cap[T_j,2T_j]|\le(1+4\pi)e^{F_L(y_j)},\qquad
F_L(y)=y-\left(\frac y{2L}-1\right)\log(y/M_L). \tag{14}
\]

Flooring k is explicitly responsible for the additive \(+\log(y/M_L)\) in F;
it is not dropped as negligible before all bands are summed.

## 6. Growth bound and strict comparison with the k=1 ledger

The presence of prime 2 gives \(V_L\ge(\log2)^2/2\), whereas (8) gives V=O(L²).
With (9) and (10),

\[
\log(Y_L/M_L)=L+O(\log L). \tag{15}
\]

For all sufficiently large L, Y>H and

\[
F_L'(y)=1-\frac{\log(y/M_L)+1}{2L}+\frac1y>0
\qquad(H_L\le y\le Y_L). \tag{16}
\]

Indeed the worst logarithm is at Y, and (15) makes the right-hand lower bound
(1/2+O(\log L/L)>0). This is uniform over every intermediate band, not only
a terminal asymptotic. More explicitly, (7)–(9) and prime 2 give absolute
constants A2,A3 with

\[
L-\log L-A_3\le\log(Y/M)\le L+\log L+A_2.
\]

The lower inequality in (15) yields

\[
F_L(Y_L)\le\frac{Y_L}{2}
+\frac{Y_L}{2L}(\log L+A_3)+L
=S_L+O(S_L\log L/L+L). \tag{17}
\]

The number of bands satisfies \(J_L\le Y_L/\log2+1=O(S_L)\), so
\(\log(1+J_L)=O(L)=o(S_L)\). Sum (14), pay the head and the negative frequencies:

\[
|E_L|\le2e^{H_L}+2(1+4\pi)J_Le^{F_L(Y_L)}.
\]

Taking a logarithm, with H=O(L³)=o(S), proves (1). This controls absolute
measure; the factor T in the moment estimate has not been replaced by density.

For a precise same-object comparison, retain the same head, bands, threshold
and terminal cutoff but use k=1 in every band of (13). Call this certified
upper ledger (U_L^{(2)}). Its last band has

\[
y_{J-1}=Y_L+O(1),\quad u_{J-1}=S_L+O(L),\quad
T_{J-1}=e^{2S_L+O(1)},\quad X=e^{2L}\ll T_{J-1}.
\]

Here V is bounded below by a positive constant and above by O(L²), so the
moment term is eventually less than T and its logarithm is

\[
\log\left[\frac{(T_{J-1}+2\pi\lceil X\rceil)V_L}{u_{J-1}^2}\right]
=2S_L-2\log S_L+\log V_L+O(1)
=2S_L+o(S_L).
\]

This single summand gives the lower bound on the *old upper ledger*; the trivial
T cap summed over all bands gives the matching upper bound. Therefore

\[
\log(1+U_L^{(2)})=2S_L+o(S_L),\qquad
\log(1+U_L)\le S_L+o(S_L). \tag{18}
\]

Equation (18) proves strict improvement of these two certified budgets, not a
lower bound on the true bad-set measure and not optimality among all possible
second-moment strategies.

## 7. Stronger old degree-profile baseline and failed net-index admission

After the all-band derivation, the independent inertia reverse audit identified
the original [016 degree-profile asset](../../../notes/016-prime-graph-hodge-inequality.md).
I checked its §5 exact formula directly. With

\[
A(Z)=\sum_{n<Z}\Lambda(n)/\sqrt n,\qquad
D_L(u)=A(e^{L-u})+A(e^{L+u}),\quad |u|<L\text{ a.e.},
\]

The finite primepower endpoint conventions can differ at finitely many u,
which do not change the form or essential supremum. One argument is ≤e^L and
the other ≤e^{2L}. Thus monotonicity gives exactly

\[
\|D_L\|_\infty\le S_L+A(e^L)=:d_L,
\qquad A(e^L)\le2C e^{L/2}=o(S_L). \tag{19}
\]

No asymptotic profile/PNT approximation was used in this bound. The exact
prime-graph decomposition gives

\[
Q_L\ge \Gamma\text{-form}-d_L\|f\|^2
+2|C(f)|^2-2|S(f)|^2,
\]

because the graph energy is nonnegative. The full odd pole still costs +1 in
inertia. The Gamma-only multiplier's bad set at threshold 1 is contained by
(4) in \(|t|<e^{d_L+G+1}\). The original concentration-trace bridge, with lower
multiplier bound \(\Gamma(0)-d_L\), therefore already yields a certified bound

\[
n_-(Q_L)\le1+
\frac{2L}{\pi}(1+d_L-\Gamma(0))e^{d_L+G+1},
\]

and hence

\[
\log(1+n_-(Q_L))\le S_L+A(e^L)+O(L). \tag{20}
\]

The remainder (A(e^L)+O(L)=O(e^{L/2}+L)) is smaller than the remainder
delivered by this high-k measure ledger,
(O(S_L\log L/L+L^3)). Accordingly (18) is a strict improvement only relative
to the weaker k=1 or naive absolute cutoff budgets. It is not a strict net
whole-index improvement over the complete frozen baseline and cannot be
registered as C013 success or as a macro Goal consequence. This negative
admission fact should accompany any consumption of the measure proof.

## 8. Consumption limits and remaining responsibility

The input avoids ζ zeros, PNT and numerical expansion. It retains the complete
actual prime-power polynomial, conservative full-Gamma error, low-frequency
head, length (X^k), rounding, all signs and the final exact empty tail.
It remains a very large permitted bad-set measure. On its own it cannot pay
any uniform small-concentration claim for all source Fourier transforms.

The root may separately combine (1) with the already-paid concentration trace
and the complete dual pole to obtain a valid whole-source inertia upper bound,
but §7 shows it has no required strict net benefit over the stronger old asset.
The generic MV/factorial/trace statements must be deducted from novelty.
Nothing here claims Goal completion, C013 success, a negative direction of Q,
or the absence of such directions. No moment-order micro-optimization is
proposed as a remedy for the failed net-index admission.

No pending scientific process, finite matrix or fitted data was used. The
subagent's runtime get_goal returned null, which is an isolated subagent
observation and does not override the root's active Goal observation.

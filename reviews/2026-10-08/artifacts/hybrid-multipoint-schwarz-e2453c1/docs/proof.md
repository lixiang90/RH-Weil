# Proof sketch with exact constants

This note records the deduction from the exact finite inequality to the
candidate asymptotic bound. It takes Anthropic's Theorem D and its analytic
setup as cited input. The separate file [`VERIFICATION_STATUS.md`](../VERIFICATION_STATUS.md)
states exactly which parts have completed a dependency-closed Lean replay.

## 1. Imported Montgomery--Taylor input

Let

$$
N=N(T,2T),\qquad S=N_0^s(T,2T),
$$

where $N$ counts zeros with multiplicity and $S$ counts zeros that are both
simple and on the critical line. Put

$$
H_{\mathrm{MT}}
=\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
=0.6725007036794116457\ldots .
$$

Anthropic's analytic argument supplies the original lower bound and the
Montgomery--Taylor overlap kernel

$$
k(x)=\frac{K(x)}{K(0)},\qquad
K(x)=\int_{-1/2}^{1/2}\cos(\sqrt2t)\cos(2\pi xt)\,dt.
$$

For bounded normalized separations, the inner products of the retained
simple-zero atoms are $k(x_\gamma-x_{\gamma'})+o(1)$ uniformly.

## 2. Stability-enhanced rank--trace inequality

Define

$$
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
$$

If $V$ has $r$ columns of norm at most one, $P=VV^*$, $M=V^*V$, and $Q$
is Hermitian with at most $b$ positive eigenvalues, then

$$
\|P+Q\|_F^2
\ge4\operatorname{tr}(P+Q)-3r-4b+\operatorname{tr}\Psi(M). \tag{2.1}
$$

This follows by writing $Q=Q_+-Q_-$, applying von Neumann's trace inequality,
and using

$$
\min_{n\ge0}\big((p-n)^2+4n\big)=2p-1+\Psi(p).
$$

Applied to the simple-zero part of Anthropic's decomposition, with the same
tail and prime-side estimates, it gives

$$
S\ge H_{\mathrm{MT}}N+\mathcal D(M^\circ)-o(N),\qquad
\mathcal D(M)=\operatorname{tr}\Psi(M). \tag{2.2}
$$

## 3. Certified seven-point inequality

Write $w(x)=k(x)^2$. For six nonnegative consecutive gaps define

$$
\mathcal F_6(g_1,\ldots,g_6)
=\frac1{3000}\sum_{i=1}^6g_i
+\sum_{s=1}^6\frac{2}{7-s}
  \sum_{i=1}^{7-s}w(g_i+\cdots+g_{i+s-1}). \tag{3.1}
$$

The interval verifier proves

$$
\mathcal F_6(g_1,\ldots,g_6)
\ge q,\qquad q=\frac{382623}{100000000}, \tag{3.2}
$$

for every $g_i\ge0$. The committed report records `verified=true`, 980,069
visited nodes, 490,399 pruned nodes, 489,670 splits, and maximum depth 65.

For $m$ ordered points $y_1<\cdots<y_m$, let

$$
E_m=2\sum_{1\le i<j\le m}w(y_j-y_i),\qquad
x=\frac{y_m-y_1}{500}.
$$

Summing (3.2) over all consecutive seven-point windows gives

$$
E_m+x\ge q(m-6). \tag{3.3}
$$

The coefficient of $x$ is $6/3000=1/500$; every pair term is counted with
total coefficient at most two.

## 4. Exact finite-dimensional spectral conversion

Let $G$ be an $m\times m$ correlation matrix and put

$$
E=\operatorname{tr}(G-I)^2,
\qquad D=\operatorname{tr}\Psi(G).
$$

The exact lower envelope of $D$ at fixed $E$ is

$$
g_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,
  &m/(m-1)\le E\le m(m-1).
\end{cases} \tag{4.1}
$$

It is increasing and 1-Lipschitz. Consequently, if $E+x\ge A$, then

$$
D+x\ge g_m(A). \tag{4.2}
$$

Indeed, for $E\ge A$ use monotonicity. For $E<A$, use
$x\ge A-E\ge g_m(A)-g_m(E)$.

For $m=279$ and the certified value of $q$,

$$
A=q(m-6)=\frac{104456079}{100000000},
$$

and

$$
C=g_{279}(A)
=\frac{11606231}{3100000000}
 +2\sqrt{\frac{1613266109}{1550000000}}-1. \tag{4.3}
$$

Thus every full block of 279 consecutive retained simple zeros satisfies

$$
\mathcal D(G_B)+\frac{\operatorname{span}(B)}{500}
\ge C-o(1). \tag{4.4}
$$

The $o(1)$ term accounts for the uniform overlap-kernel limit and the
normalization of the asymptotic Gram diagonal to one.

## 5. Shifted pinching and the final constant

Average (4.4) over all 279 offsets of the consecutive block partition.
Pinching is valid because $X\mapsto\operatorname{tr}\Psi(X)$ is convex and
unitarily invariant. Each adjacent gap occurs in at most 278 block spans, so

$$
\mathcal D(M^\circ)
\ge \frac{C}{279}S
 -\frac{278}{500\cdot279}N-o(N). \tag{5.1}
$$

Substituting (5.1) into (2.2) and rearranging gives

$$
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
B_{279}:=
\frac{H_{\mathrm{MT}}-139/69750}{1-C/279}. \tag{5.2}
$$

Equivalently,

$$
B_{279}=
\frac{864900000000H_{\mathrm{MT}}-1723600000}
 {867988393769-20000\sqrt{100022498758}}.
$$

Directed 256-bit Arb arithmetic proves

$$
0.6730266625438475496579090211642630978
<B_{279}
<0.6730266625438475496579090211642630979.
$$

An exact finite scan through $7\le m\le1000$, followed by a monotonicity
argument for the real tail, makes $m=279$ the unique optimal block size.

For the tail, put $q=382623/10^8$ and, for real $x\ge1000$, define

$$
s(x)=\sqrt{q\left(x-7+\frac6x\right)}.
$$

On the second spectral branch,

$$
\frac{C_x}{x}=\frac{q(x-6)}{x^2}+\frac{2s(x)-1}{x}.
$$

The first term decreases for $x>12$. The derivative of the second has the
sign of

$$
s(x)-q\left(x-14+\frac{18}{x}\right).
$$

The exact checkpoints

$$
q(986)^2-1000=\frac{67996137527}{25000000}>0,
\qquad
2q(986)-1=\frac{163633139}{25000000}>0
$$

show that $q(x-14)^2-x$ is positive and increasing for $x\ge1000$. Hence

$$
s(x)<\sqrt{qx}<q(x-14)
<q\left(x-14+\frac{18}{x}\right),
$$

so $C_x/x$ decreases. The numerator
$H_{\mathrm{MT}}-1/500+1/(500x)$ decreases and the positive denominator
$1-C_x/x$ increases. Therefore $B_x$ decreases on the entire real tail.
Together with the directed finite scan, this proves global uniqueness of
$m=279$.

## 6. Proof boundary

The standalone interval verifier establishes (3.2), and Sections 2--5 give
the mathematical deduction to (5.2). The zero-counting, tail, trace, and
test-family inputs are imported from Anthropic's paper and Lean artifact.

The present release candidate does not claim that every generated terminal
catalog and the final public theorem have completed a clean, transitive Lean
build. That stronger status requires the gates listed in
[`VERIFICATION_STATUS.md`](../VERIFICATION_STATUS.md).

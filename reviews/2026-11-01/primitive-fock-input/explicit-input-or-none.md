# ONE actual prime–Fock candidate: explicit construction, input NONE

2026-11-01. Unadmitted input formation only; no new mathematical contract or iteration. This is a different proposed carrier, not a continuation of the stopped C070 Hermite path. The answer is **NONE after deduction of 566/576/577/578**: the actual positive Fock construction is legal, but its primitive extraction gives exactly the previously paid positive-jump-minus-degree identity, not a new signed-core estimate. This record does not reject all Fock, relative, nonlocal or source-adapted constructions.

## 1. Frozen source, target and candidate

Keep the physical source (r(u)=e^{u/2}f(u)), ALL complex (r\in C_c^\infty(\mathbb R)), 
\(\widehat r(t)=\int r(u)e^{-itu}du\), (r^*(u)=\overline{r(-u)}), and (h_r=r*r^*\). The primary norm is the original physical (L^2(du)); fixed support and zero-extension Dlog/Hlog are not identified with a different Fock norm. First-slot linear mixed forms are retained. The full target is exactly 577:

\[
 W_\zeta=W_\Gamma+H-P,\quad H=2\cosh(u/2)du,
 \quad P=\sum_{p,k\ge1}(\log p)p^{-k/2}
       (\delta_{k\log p}+\delta_{-k\log p}).                 \tag{1}
\]

Here (W_\Gamma) has its already fixed finite part/contact and Fourier multiplier (\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi\). All proper powers and both poles remain. In particular,

\[
 Q_H(r)=2\Re\bigl(\mu_+(r)\overline{\mu_-(r)}\bigr),
 \qquad \mu_\pm(r)=\int e^{\pm u/2}r(u)du,                \tag{2}
\]

which is not an automatically positive degree term; the odd contribution cannot be discarded.

Take the actual one-particle Hilbert space (\mathfrak h=\ell^2(\{p:p\text{ prime}\})\), with (he_p=(\log p)e_p\), and bosonic Fock space (\mathcal F=\Gamma_s\mathfrak h\). Its occupation basis is indexed by finite sequences (m_p\ge0\). Unique prime factorization identifies this basis with (n=\prod p^{m_p}\in\mathbb N\), and

\[
 \mathcal F\simeq\ell^2(\mathbb N),\qquad
 \mathsf H=d\Gamma(h),\qquad \mathsf H e_n=(\log n)e_n.   \tag{3}
\]

This is a nonzero, self-adjoint, nonnegative operator obtained from the actual primes, with no zero-position input.

## 2. What the positive thermal trace actually gives

Direct summation of (3), rather than an assumed spectral identity, gives

\[
 \operatorname{Tr}e^{-\beta\mathsf H}
 =\sum_{n\ge1}n^{-\beta}=\prod_p(1-p^{-\beta})^{-1}
 =\zeta(\beta)<\infty\quad(\beta>1).                     \tag{4}
\]

For (\beta\le1\), the ordinary trace in (4) is infinite. Hence the normalized thermal state (\rho_\beta=e^{-\beta\mathsf H}/\zeta(\beta)\) exists by this rule only for (\beta>1\), not at (\beta=1/2\). Analytically continuing a scalar zeta value does not analytically continue a positive trace-class density.

Set (V(t)=e^{it\mathsf H}\), and (A_r=\int r(u)V(-u)du\). Then (\|A_r\|\le\|r\|_1\), and for (\beta>1\),

\[
 \operatorname{Tr}(A_r\rho_\beta A_r^*)
 =\zeta(\beta)^{-1}\sum_{n\ge1}n^{-\beta}
                         |\widehat r(\log n)|^2\ge0.     \tag{5}
\]

For fixed support ([-L,L]), this is at most (2L\|r\|_2^2\). This is a legitimate positive source form. Its spectral labels are the integer energies (\log n\); after reflection averaging they are (\pm\log n\). These are **Fourier spectral atoms**. They are not the physical-space prime atoms (\delta_{\pm k\log p}\) in (1), nor the zeta-zero trace measure. There is no identification of (5) with (Q_\zeta\).

## 3. The actual connected/primitive extraction

For (\beta>1\), the characteristic function and its absolutely convergent logarithm are

\[
 \chi_\beta(t)=\operatorname{Tr}(\rho_\beta V(t))
             =\frac{\zeta(\beta-it)}{\zeta(\beta)},\quad
 \log\chi_\beta(t)=\sum_{p,k\ge1}\frac{p^{-k\beta}}k
                         (e^{itk\log p}-1).              \tag{6}
\]

The logarithm here is the continuous branch fixed by the displayed series and value zero at (t=0\). Differentiating the convergent series gives

\[
 -\partial_\beta\log\chi_\beta(t)
 =\sum_{p,k\ge1}(\log p)p^{-k\beta}
                         (e^{itk\log p}-1).              \tag{7}
\]

The (1/k\) cancels against (k\log p\), giving exactly (\Lambda(p^k)=\log p\), not (\log(p^k)\). No proper powers have been deleted. The **negative twice-real part** of (7), rather than (7) itself as a positive trace, is the positive jump multiplier.

For a finite prime set (S\), equations (4), (6), (7) are also valid with the finite Euler product and all (k\ge1\), for every (\beta>0\). Put

\[
 a_{\beta,p,k}=(\log p)p^{-k\beta},\quad
 c_{\beta,S}=2\sum_{p\in S,k\ge1}a_{\beta,p,k}
            =2\sum_{p\in S}\frac{\log p}{p^\beta-1},
\]
\[
 P_{\beta,S}=\sum_{p\in S,k\ge1}a_{\beta,p,k}
                   (\delta_{k\log p}+\delta_{-k\log p}).  \tag{8}
\]

Let (T_vr(u)=r(u-v)\). The actual linear source feature

\[
 F_{\beta,S}(r)=
 \bigl(\sqrt{a_{\beta,p,k}}(T_{k\log p}-I)r\bigr)_{p,k}
 \in\bigoplus_{p\in S,k\ge1}L^2(du)                      \tag{9}
\]

is bounded on the original full (L^2(du)\), with squared norm at most (2c_{\beta,S}\|r\|_2^2\). Its positive form is exactly

\[
 \boxed{\ E_{\beta,S}(r)=\|F_{\beta,S}(r)\|^2
       =c_{\beta,S}\|r\|_2^2-P_{\beta,S}(h_r).\ }         \tag{10}
\]

Polarization gives the corresponding first-linear mixed identity on the same domain. This step uses no unknown projection, no subtraction in a positive trace, and no source-dependent weights.

## 4. The first decisive comparison at the critical weights

At (\beta=1/2\), each finite-(S\) feature (9) is legal. But as (S\) exhausts the primes,

\[
 c_{1/2,S}=2\sum_{p\in S}\frac{\log p}{\sqrt p-1}
                       \longrightarrow\infty.           \tag{11}
\]

No sharp PNT estimate is needed for this divergence. For nonzero (r\in L^2(du)\), its autocorrelation tends to zero at infinity: (h_r\in C_0(\mathbb R)\), by Fourier inversion of (\lvert\widehat r\rvert^2\in L^1\). Thus (\|T_vr-r\|_2^2\to2\|r\|_2^2\). The infinite positive sum in (9) consequently diverges for every nonzero (r\in L^2\). Its finite-energy domain is ({0}\), not a dense positive closed-form domain. For compact (r\) the statement is even exact beyond the support diameter: the relevant translations are disjoint.

Now fix any source half-window (L\), and choose finite (S\) containing every prime (p\le e^{2L}\). Every nonzero term of (P(h_r)\) then occurs in (P_{1/2,S}(h_r)\), because (\operatorname{supp}h_r\subset[-2L,2L]\). All returns (k\ge1\) remain in (8); the later ones vanish on this test by support, not by a changed Euler factor. Equations (1) and (10) give the exact full-target comparison

\[
 \boxed{\ Q_\zeta(r)=E_{1/2,S}(r)+Q_\Gamma(r)+Q_H(r)
                             -c_{1/2,S}\|r\|_2^2.\ }     \tag{12}
\]

Increasing (S\) beyond this point adds exactly the same positive scalar mass to (E\) and its subtracted degree. The cancellation is legal, but the subtracted expression is not thereby positive. A renormalized/super trace does not inherit ordinary positive-trace positivity. The missing signed comparison is precisely the sign of the right side of (12), with the fixed Gamma/contact and both pole moments; it has not been supplied by the Fock construction.

There is likewise no supplied primitive orthogonal projection. The known Fock particle-number-one projection produces prime-energy spectral atoms in (5) and omits the returns of (7). Removing the vacuum only removes the (n=1\) energy state. Taking a logarithm of a partition function is a connected/cumulant operation, not an automatically positive orthogonal compression realizing (12). Naming an unspecified projection that pays the final signed difference would assume the missing input.

## 5. Strongest-old deduction and consumption limits

- **566 §§2,7 already pay this failure formula.** Its safe positive jump is bounded and has no finite ordinary heat trace on the full translation carrier; its critical unrenormalized jump has domain ({0}\). Equation (10) at critical weights is exactly 566(14), regrouped by finite prime sets with full returns. This is an old consequence, not a newly proved general Fock boundary.
- **578 §3 already separates the operators.** Positive Euler/Toeplitz data and Hermitian squares do not give the same linear prime distribution plus the fixed Gamma/poles. The primitive extraction (7) transports the original coefficients accurately, but supplies none of the additional signed estimate. Its thermal/cumulant notation is not new arithmetic cancellation.
- **576 §§5,8–10 already pay richness versus membership.** Producing a positive source family, or putting it into a large positive distribution cone, does not identify its limit with the complete classical target. Fixed-window costs and Dprime/strong-source convergence also cannot be silently exchanged.
- **577 §§6,9 already give a stronger target-specific positive-family facility.** Its explicit positive layers retain the actual Gamma/contact and all prime/pole data with paid fixed-window and strong-source errors. The actual negative-part repair still lacks an independent vanishing budget. The present thermal family does not improve that facility; equation (12) only returns to the same signed responsibility.

The old complete fixed-window/head and whole negative-inertia assets are unchanged. This formation supplies neither principal descent for the 405 noncompact relations, independent primitive sections/capacity, a new whole-object inequality, nor growing signed-core/coupling control. The automatic positive family must not be labeled complete zeta matching, an actual RH counterexample, or a method-class no-go. In particular, failure of this ordinary thermal state at critical weights does not exclude other paid relative/infinite-dimensional constructions.

**Disposition: NONE; stop this ONE candidate.** No new independent actual input/test with a net consequence survives subtraction of the stated old assets. No new mathematical iteration, no607, no C071, no continued temperature/cutoff/fermionic/projection/source queue. ROOT decides settlement and publication. This file does not alter STATE, cadence, board, library or the active long Goal.

# Independent review of the semilocal floating diagnostics

2026-10-11. Reviewer: semilocal_gamma_prime. No public file changed.

## Verdict, coverage and identities

PASS for the stated bounded diagnostic scope. Read the entire script
scripts/semilocal_relative_cycle_diagnostics.py and its complete published
JSON reviews/2026-10-11/f1-semilocal-relative-cycle-diagnostics.json.
Independently reran the script with output only in
tmp/f1-semilocal-20261011/independent-diagnostics-rerun.json; exit code 0.
Parsed comparison proves the rerun JSON equals the published JSON exactly.

Reviewed file SHA256:

    script: 5f2faac12b33db18a536291e5c0fd1ecf9226d2c68b8f23627a5b086829f4071
    public JSON: 7e83c1f18e89f0e365a6900e4739bd943ad903b9a0578798b2f503cfd1ebdd79

The JSON's LF-normalized mathematical note hashes match the final independent
511–512 review:

    511: d0a9607e27402967f488c2536093ff6ea6d7a0efb7df57064df6131b41420f6f
    512: fd07fadfbe4ab84d5c2097ed890fefe1a91924e5d370a7f1ad198a374560a747

Actual rerun result:

    status PASS
    39 numerical identity checks
    516 norm bound samples
    maximum observed identity error 9.72590359671137625e-24
    working precision 45 decimal digits

The 39 count is correctly 18 common phase/unitarity checks, 4 common
self-dual-source checks, 12 finite spectral/time comparisons, 4 norm attainment
checks, and 1 zero-frequency Gamma/prime constant check. The 516 count is
4 primes times 129 sample points; each grid includes both periodic endpoints.
They are samples, not 516 independently certified global norm bounds.

## 1. Gaussian common-source Mellin direction

The source phi(r)=exp(-pi r^2) is self-dual for the stated actual real additive
Fourier. Finite unit balls are also self-dual for conductor-Z_p characters.
The script directly integrates the positive-real source Mellin integral and
multiplies by the source periodization denominator:

    H_S(s)=2 integral_0^infinity exp(-pi r^2)r^(s-1)dr
                   /product_(p=2,5)(1-p^(-s)).

For s=1/2-i tau the ratio H_S(s)/H_S(1-s) is consequently the actual
common Fourier factor m_S(tau), rather than its inverse. The numerator in
each finite factor is exp(-i tau log p), exactly as in 511. The real Gamma
factor is Gamma(1/4-i tau/2)/Gamma(1/4+i tau/2) times pi^(i tau).
The unnormalized factor 2 cancels in this ratio.

The derivative check uses i*m_S'/m_S=b_S, consistent with m_S'/m_S=-i b_S.
Its density helper has the negative finite-prime sign. Thus the unitary and
derivative diagnostics independently match both the phase direction and the
conductor convention of the public derivation.

The direct quadrature has an integrable singular endpoint at r=0. Its observed
accuracy is about 23 decimal places for the largest sampled tau, consistent
with the explicit 1e-20 tolerance. The JSON reports 45 WORKING digits and
the observed error separately; it does not falsely claim 45 accurate digits
or an interval quadrature bound.

## 2. Finite spectral/time pairing

For Gaussian eta(t)=exp(-t^2/(2sigma^2)), the script uses its exact unnormalized
Fourier transform sqrt(2pi)sigma exp(-sigma^2 tau^2/2). For eta(t)=t^2 times
that Gaussian, its transform is minus the second frequency derivative:

    sqrt(2pi)sigma exp(-sigma^2 tau^2/2)
       *sigma^2(1-sigma^2 tau^2).

This is the exact polynomial factor implemented; it is not required to be
pointwise positive for this local linear identity.

The finite density is

    b_p(tau)=-2log p Re[a exp(i tau log p)/(1-a exp(i tau log p))],
    a=p^(-1/2).

Because both factors of the spectral pairing are even, integrating
-b_p*phi/pi on [0,infinity) correctly equals the full
-(1/2pi) integral over R. The time side is 2log p sum a^n eta(nlog p), with
the factor 2 and the unitarizing factor a^n exactly correct.

Two widths, two identity-value behaviors, and three separate primes give
12 local comparisons. Including prime11 is a local-factor diagnostic; the
common-source test still uses S_f={2,5}. The finite time sum is truncated
at n=300, while the spectral quadrature retains a final interval to infinity.
The Gaussian tails are far below the chosen tolerance for these fixed
parameters. No rigorous numerical tail certificate is claimed.

## 3. Norm constant and zero-frequency density

The four attainment checks use tau=acos(a)/log p. At these points cos(theta)=a,
so the exact multiplier norm is |m_p-1|=2a. The 129-point full-period grids
test the inequality against that same constant. All new primes 3,7,11,97
are outside the common base S_f={2,5}.

The mathematical norm proof in 512 uses the exact algebraic identity
(1+a^2-2az)-(1-z^2)=(z-a)^2. The floating attainment/grid checks are
consistent with that proof; they do not establish the supremum themselves,
and do not certify noncompactness.

The zero-density comparison implements

    -b_S(0)=gamma+pi/2+3log2+log pi
               +2sum_(p=2,5) log p *a_p/(1-a_p).

This agrees with psi(1/4)=-gamma-pi/2-3log2 and the geometric prime series.
The assert that this number is positive is appropriate as a diagnostic.
The actual strict positivity in 512 follows from its displayed exact
constants, not from this floating assert.

## 4. Limits and nonclaims

The script header and JSON limits accurately say these are floating
Schwartz-Gaussian checks, not compact tests, interval arithmetic or a Lean
certificate. No compact double-moment countertest is instantiated here.
No quotient descent, S1 admission, noncompactness proof, actual HH1 cycle,
global negativity, growing-S limit, or RH is certified by these calculations.
Those claims are independently reviewed mathematical arguments in the notes.

No mathematical correction or diagnostic-scope correction is needed.

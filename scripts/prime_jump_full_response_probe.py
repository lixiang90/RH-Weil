#!/usr/bin/env python3
"""[E] Finite-band full J4/mu^4 at prime-jump-selected Abel cutoffs.

Run: python -B scripts/prime_jump_full_response_probe.py
Optional bounded extension: --max-m 12 or --max-frequency 512.

For sigma=.25, q is the first prime above Y=2**m; floating-point masses
choose N in {q-1,q} with larger absolute mass. The two actual centered
channels are p_hat<=0 and c_hat>=0, with r_hat=p_hat+c_hat retained before
raising to the fourth power. D is computed independently from positive
Brownian min-kernel and continuum tail-square identities, not from the
finite frequency band. Outputs are floating-point [E], not certified
full-frequency bounds. No files are written.
"""

import argparse
import math
import sys

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np

from abel_mass_discrepancy_probe import continuum_mass, prime_power_ledger
from prime_jump_cutoff_probe import first_prime_above, mass_float, von_mangoldt_mp
from quartic_signed_frequency_probe import (
    centered_transform,
    composite_gauss,
    continuum_rule,
    exact_continuum_transform,
)


def prime_brownian_energy(lags, coefficients):
    """E(p)=1/2 sum a_i a_j min(lambda_i,lambda_j), linear sorted suffix."""
    assert np.all(lags >= 0) and np.all(np.diff(lags) >= 0)
    assert np.all(coefficients > 0)
    suffix = np.cumsum(coefficients[::-1], dtype=np.longdouble)[::-1]
    after = np.concatenate((suffix[1:], [np.longdouble(0)]))
    return np.sum(lags*coefficients*(coefficients+2*after),
                  dtype=np.longdouble)/2


def continuum_brownian_energy_mp(Y, N):
    """E(c)=1/2 integral_0^logN beta((u,logN])^2 du."""
    a, upper = mp.mpf(".75"), mp.log(N)
    def tail(u):
        return mp.power(Y, a)*mp.gammainc(a, mp.exp(u)/Y, mp.mpf(N)/Y)
    return mp.quad(lambda u: tail(u)**2, [0, upper/2, upper])/2


def full_frequency_integrals(Y, N, lags, coefficients, thresholds, inner, outer):
    continuum = continuum_rule(Y, 0, math.log(N), max(thresholds), inner)
    total_p, total_c = np.longdouble(0), np.longdouble(0)
    outputs = {}
    left = 0.
    for right in thresholds:
        xi_all, quadrature = composite_gauss(left, right, .125, outer)
        for begin in range(0, len(xi_all), 128):
            end = min(begin+128, len(xi_all))
            xi, qw = xi_all[begin:end], quadrature[begin:end]
            p = centered_transform(xi, lags, coefficients)
            c = -centered_transform(xi, *continuum)
            assert np.all(p <= 0) and np.all(c >= 0)
            r = p+c
            common = qw*r**4/(np.pi*xi**2)
            total_p += np.sum(common*p*p, dtype=np.longdouble)
            total_c += np.sum(common*c*c, dtype=np.longdouble)
        outputs[right] = (total_p, total_c)
        left = right
    return outputs


def continuum_sample_check(Y, N, maximum):
    xi = np.array([0., .3, 1., 8., 32., 128.])
    if maximum > 128:
        xi = np.append(xi, maximum)
    rule = continuum_rule(Y, 0, math.log(N), maximum, 18)
    computed_c = -centered_transform(xi, *rule)
    differences = []
    for frequency, value in zip(xi, computed_c):
        exact_c = -exact_continuum_transform(Y, mp.mpf(1), mp.mpf(N), frequency)
        differences.append(abs(mp.mpf(str(value))-exact_c)/(1+abs(exact_c)))
    return max(differences), len(differences)


def independent_small_case(Y, N, Dprime_float, Dcontinuum_mp, ratio_float):
    """Trial-factorized 50-digit coefficients, direct min matrix, adaptive band."""
    ledger = []
    for n in range(2, N+1):
        lam = von_mangoldt_mp(n)
        if lam:
            ledger.append((mp.log(n), lam*mp.power(n, mp.mpf("-.25"))
                           *mp.exp(-mp.mpf(n)/Y)))
    A = mp.fsum(weight for _, weight in ledger)
    M = A-continuum_mass(.25, Y, N)
    Dprime_mp = mp.fsum(a*b*min(x, y) for x, a in ledger
                       for y, b in ledger)/2
    def integrand(xi):
        if xi == 0:
            return mp.mpf(0)
        p = -2*mp.fsum(weight*mp.sin(xi*lag/2)**2 for lag, weight in ledger)
        c = -exact_continuum_transform(Y, mp.mpf(1), mp.mpf(N), xi)
        return (p+c)**4*(p*p+c*c)/(mp.pi*xi*xi)
    numerator = mp.quad(integrand, [0, mp.mpf(".5"), 1])
    ratio = numerator/(M**4*(Dprime_mp+Dcontinuum_mp))
    relative = abs(mp.mpf(str(ratio_float))-ratio)/ratio
    Dprime_error = abs(mp.mpf(str(Dprime_float))-Dprime_mp)
    assert relative < mp.mpf("1e-9")
    assert Dprime_error/(1+Dprime_mp) < mp.mpf("1e-12")
    return numerator, ratio, relative, Dprime_error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, choices=(8, 10, 12), default=10)
    parser.add_argument("--max-frequency", type=int, choices=(128, 512), default=128)
    args = parser.parse_args()
    mp.mp.dps = 50
    m_values = [m for m in (4, 6, 8, 10, 12) if m <= args.max_m]
    primes = {m: first_prime_above(2**m) for m in m_values}
    all_n, all_lambda = prime_power_ledger(max(primes.values()))
    thresholds = [1., 8., 32., 128.]
    if args.max_frequency > 128:
        thresholds.append(float(args.max_frequency))
    print("[E] bounded finite-band full-response estimates only; "
          "not certified totals or certified lower bounds.")
    print("sigma=.25; N is the floating-point |M|-maximizer in {q-1,q}; "
          "q is the first prime in (Y,2Y).")
    print("J4_leT/mu^4 = integral_0^T (p_hat+c_hat)^4 "
          "(p_hat^2+c_hat^2)/(pi xi^2) divided by (M^4 D).")
    print("Dprime uses a sorted min-kernel formula; Dcontinuum uses an "
          "independent 50-digit positive tail-square integral.")
    print(f"numpy={np.__version__}; mpmath={mp.__version__}; "
          f"longdouble_explicit_mantissa_bits={np.finfo(np.longdouble).nmant}")
    print("Coarse/fine: continuum Gaussian10/18 and frequency Gaussian8/12; "
          "frequency-panel width<=1/8. No omitted-tail certification.")
    print("m,Y,q,N,prime_powers,M,Dprime,Dcontinuum,D_over_LS2")
    outputs = []
    smallest = None
    for m in m_values:
        Y, q = 2**m, primes[m]
        before, _ = mass_float(all_n, all_lambda, Y, q-1)
        after, _ = mass_float(all_n, all_lambda, Y, q)
        N, M = (q-1, before) if abs(before) >= abs(after) else (q, after)
        count = np.searchsorted(all_n, N, side="right")
        n, lam = all_n[:count], all_lambda[:count]
        lags = np.log(n)
        coefficients = lam*np.exp(-.25*lags-n/Y)
        A = np.sum(coefficients, dtype=np.longdouble)
        B = np.longdouble(str(continuum_mass(.25, Y, N)))
        S, L = A+B, math.log(Y)
        Dp = prime_brownian_energy(lags, coefficients)
        Dc_mp = continuum_brownian_energy_mp(Y, N)
        Dc = np.longdouble(str(Dc_mp))
        D = Dp+Dc
        print(f"{m},{Y},{q},{N},{count},{M:.14g},{Dp:.14g},"
              f"{Dc:.14g},{D/(L*S*S):.14g}")
        coarse = full_frequency_integrals(Y, N, lags, coefficients, thresholds, 10, 8)
        fine = full_frequency_integrals(Y, N, lags, coefficients, thresholds, 18, 12)
        denominator = M**4*D
        assert denominator > 0
        for T in thresholds:
            ip, ic = fine[T]
            cp, cc = coarse[T]
            total, previous = ip+ic, cp+cc
            ratio_p, ratio_c = ip/denominator, ic/denominator
            difference = abs(total-previous)/max(abs(total), np.longdouble(1e-30))
            outputs.append((m, T, ip, ic, ratio_p, ratio_c, ratio_p+ratio_c, difference))
            if smallest is None and T == 1:
                smallest = (Y, N, Dp, Dc_mp, ratio_p+ratio_c)
        sample_error, samples = continuum_sample_check(Y, N, args.max_frequency)
        assert sample_error < mp.mpf("1e-9")
        print(f"continuum_gamma_sample_check,m={m},samples={samples},"
              f"largest_scaled_error={mp.nstr(sample_error, 8)}")
    print("m,T,prime_channel_partial,continuum_channel_partial,"
          "prime_ratio,continuum_ratio,total_J4leT_over_mu4,"
          "coarse_fine_relative_difference")
    for m, T, ip, ic, rp, rc, ratio, difference in outputs:
        print(f"{m},{T:g},{ip:.14g},{ic:.14g},{rp:.14g},{rc:.14g},"
              f"{ratio:.14g},{difference:.6g}")
    numerator, ratio, relative, dp_error = independent_small_case(*smallest)
    print("Independent m=4,T=1 adaptive high-precision check:")
    print(f"numerator={mp.nstr(numerator, 24)}; "
          f"J4le1_over_mu4={mp.nstr(ratio, 24)}; "
          f"relative_difference={mp.nstr(relative, 8)}; "
          f"prime_min_kernel_error={mp.nstr(dp_error, 8)}")
    print("All numerical trends remain [E]. Finite bands and floating-point "
          "cutoff selection establish no uniform arithmetic budget or RH claim.")


if __name__ == "__main__":
    main()

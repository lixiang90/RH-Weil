#!/usr/bin/env python3
"""[E] Bounded finite-frequency signed quartic Abel-response probe.

Run: python -B scripts/quartic_signed_frequency_probe.py

Default sigma=.25, m=4,6,8, Y=2**m, N=floor(Y log(Y)**2), and
H=min(log L,L/8), L=log Y. All transforms use cos(x)-1=-2*sin(x/2)**2.
Two composite Gaussian rules are compared, and continuum transforms at
selected frequencies are independently checked by complex incomplete gamma.
Outputs are finite-band floating-point estimates, NOT total energies or
certified lower bounds. No files are written and no E2 fourfold sum is used.
"""

import argparse
import math
import sys

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

from abel_mass_discrepancy_probe import continuum_mass, prime_power_ledger


def cutoff(m):
    return int(mp.floor(mp.mpf(2)**m * (m*mp.log(2))**2))


def composite_gauss(left, right, max_width, order):
    count = max(1, math.ceil((right-left)/max_width))
    edges = np.linspace(left, right, count+1)
    nodes, weights = leggauss(order)
    widths = np.diff(edges)
    centers = (edges[:-1]+edges[1:])/2
    points = centers[:, None]+widths[:, None]*nodes[None, :]/2
    quadrature = widths[:, None]*weights[None, :]/2
    return points.ravel(), quadrature.ravel()


def continuum_rule(Y, left_lag, right_lag, max_frequency, order):
    # Each lag panel has at most 8 radians of phase at the largest frequency.
    nodes, quadrature = composite_gauss(
        left_lag, right_lag, min(.125, 8/max_frequency), order)
    coefficients = quadrature*np.exp(.75*nodes-np.exp(nodes)/Y)
    return nodes, coefficients


def centered_transform(frequencies, lags, coefficients):
    if len(lags) == 0:
        return np.zeros_like(frequencies)
    return -2*(np.sin(frequencies[:, None]*lags[None, :]/2)**2 @ coefficients)


def frequency_integrals(Y, prime_lags, prime_weights, local_lags, local_weights,
                        lower_lag, upper_lag, logN, thresholds, inner, outer):
    continuum = continuum_rule(Y, 0, logN, max(thresholds), inner)
    local_continuum = continuum_rule(
        Y, lower_lag, upper_lag, max(thresholds), inner)
    result = {}
    total_a, total_b = np.longdouble(0), np.longdouble(0)
    left = 0.0
    for right in thresholds:
        frequencies, quadrature = composite_gauss(left, right, .125, outer)
        for begin in range(0, len(frequencies), 128):
            end = min(begin+128, len(frequencies))
            xi, qw = frequencies[begin:end], quadrature[begin:end]
            r = (centered_transform(xi, prime_lags, prime_weights)
                 -centered_transform(xi, *continuum))
            rH = (centered_transform(xi, local_lags, local_weights)
                  -centered_transform(xi, *local_continuum))
            difference = (r-rH)*(r+rH)
            total_a += np.sum(qw*difference**2/xi**2/np.pi, dtype=np.longdouble)
            total_b += np.sum(qw*rH**4/xi**2/np.pi, dtype=np.longdouble)
        result[right] = (total_a, total_b)
        left = right
    return result


def exact_continuum_transform(Y, left_x, right_x, xi):
    a = mp.mpf(".75")
    if xi == 0:
        return mp.mpf(0)
    s = a+1j*mp.mpf(str(xi))
    oscillating = mp.power(Y, s)*mp.gammainc(s, left_x/Y, right_x/Y)
    mass = mp.power(Y, a)*mp.gammainc(a, left_x/Y, right_x/Y)
    return mp.re(oscillating)-mass


def verify_continuum(Y, lower_lag_mp, upper_lag_mp, N, max_frequency):
    frequencies = np.array([0, .3, 1, 8, 32, 128], dtype=float)
    if max_frequency > 128:
        frequencies = np.append(frequencies, max_frequency)
    full_rule = continuum_rule(Y, 0, math.log(N), max_frequency, 18)
    local_rule = continuum_rule(
        Y, float(lower_lag_mp), float(upper_lag_mp), max_frequency, 18)
    comparisons = []
    for label, rule, left_x, right_x in (
            ("full", full_rule, mp.mpf(1), mp.mpf(N)),
            ("local", local_rule, mp.exp(lower_lag_mp), mp.exp(upper_lag_mp))):
        computed = centered_transform(frequencies, *rule)
        for xi, value in zip(frequencies, computed):
            exact = exact_continuum_transform(Y, left_x, right_x, xi)
            absolute = abs(mp.mpf(str(value))-exact)
            scaled = absolute/(1+abs(exact))
            comparisons.append((label, xi, absolute, scaled))
    return comparisons


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, choices=(8, 10), default=8)
    parser.add_argument("--max-frequency", type=int, choices=(128, 512), default=128)
    args = parser.parse_args()
    mp.mp.dps = 50
    m_values = [m for m in (4, 6, 8, 10) if m <= args.max_m]
    thresholds = [1., 8., 32., 128.]
    if args.max_frequency > 128:
        thresholds.append(float(args.max_frequency))
    all_n, all_lambda = prime_power_ledger(cutoff(max(m_values)))
    print("[E] finite-band floating-point estimates only: not total energies,"
          " not certified lower bounds.")
    print("sigma=.25; H=min(log L,L/8); Y=2^m; N=floor(Y log^2Y)")
    print("Transforms: rhat=(prime centered cosine)-(continuum centered cosine); "
          "cos-1=-2sin^2.")
    print("A4partial^2=(1/pi) integral_0^T (rhat^2-rHhat^2)^2/xi^2; "
          "B4partial^2=(1/pi) integral_0^T rHhat^4/xi^2.")
    print(f"numpy={np.__version__}; mpmath={mp.__version__}; "
          f"longdouble_explicit_mantissa_bits={np.finfo(np.longdouble).nmant}")
    print("Coarse/fine rules: lag Gaussian 10/18; frequency Gaussian 8/12; "
          "frequency-panel width<=1/8.")
    print("m,N,prime_powers,local_prime_powers,H,M,MH")
    outputs = []
    for m in m_values:
        Y, N = 2**m, cutoff(m)
        Lmp = m*mp.log(2)
        Hmp = min(mp.log(Lmp), Lmp/8)
        assert 0 < Hmp < Lmp/6
        L, H = float(Lmp), float(Hmp)
        lower_lag_mp = max(mp.mpf(0), Lmp-Hmp)
        upper_lag_mp = min(mp.log(N), Lmp+Hmp)
        count = np.searchsorted(all_n, N, side="right")
        n, lam = all_n[:count], all_lambda[:count]
        lags = np.log(n)
        weights = lam*np.exp(-.25*lags-n/Y)
        A = np.sum(weights, dtype=np.longdouble)
        B = np.longdouble(str(continuum_mass(.25, Y, N)))
        M = A-B
        local = ((n >= int(mp.ceil(mp.exp(lower_lag_mp))))
                 & (n <= int(mp.floor(mp.exp(upper_lag_mp)))))
        local_lags, local_weights = lags[local], weights[local]
        AH = np.sum(local_weights, dtype=np.longdouble)
        BH = mp.power(Y, mp.mpf(".75"))*mp.gammainc(
            mp.mpf(".75"), mp.exp(lower_lag_mp)/Y, mp.exp(upper_lag_mp)/Y)
        MH = AH-np.longdouble(str(BH))
        print(f"{m},{N},{len(n)},{len(local_lags)},{H:.12g},{M:.14g},{MH:.14g}")
        coarse = frequency_integrals(
            Y, lags, weights, local_lags, local_weights,
            float(lower_lag_mp), float(upper_lag_mp), math.log(N), thresholds, 10, 8)
        fine = frequency_integrals(
            Y, lags, weights, local_lags, local_weights,
            float(lower_lag_mp), float(upper_lag_mp), math.log(N), thresholds, 18, 12)
        denominator = M*M*np.sqrt(L)
        for T in thresholds:
            a_sq, b_sq = fine[T]
            a_coarse, b_coarse = coarse[T]
            a_ratio = np.sqrt(a_sq)/denominator
            b_ratio = np.exp(-.75*H)*np.sqrt(b_sq)/denominator
            rel_a = abs(a_sq-a_coarse)/max(abs(a_sq), np.longdouble(1e-30))
            rel_b = abs(b_sq-b_coarse)/max(abs(b_sq), np.longdouble(1e-30))
            outputs.append((m, T, a_sq, b_sq, a_ratio, b_ratio, rel_a, rel_b))
        comparisons = verify_continuum(Y, lower_lag_mp, upper_lag_mp, N,
                                       args.max_frequency)
        largest_absolute = max(row[2] for row in comparisons)
        largest_scaled = max(row[3] for row in comparisons)
        assert largest_scaled < mp.mpf("1e-9")
        print(f"continuum_special_function_sample_check,m={m},"
              f"max_abs={mp.nstr(largest_absolute, 8)},"
              f"max_scaled={mp.nstr(largest_scaled, 8)},samples={len(comparisons)}")
    print("m,T,A4partial_squared,B4partial_squared,"
          "A4partial_over_M2sqrtL,exp_minus_aH_B4partial_over_M2sqrtL,"
          "A4squared_rule_relative_difference,B4squared_rule_relative_difference")
    for m, T, a_sq, b_sq, a_ratio, b_ratio, rel_a, rel_b in outputs:
        print(f"{m},{T:g},{a_sq:.14g},{b_sq:.14g},{a_ratio:.14g},"
              f"{b_ratio:.14g},{rel_a:.6g},{rel_b:.6g}")
    print("Finite-band positivity does not certify the omitted tail, arithmetic"
          " asymptotics, total-energy comparisons, or a signed-transfer bound.")


if __name__ == "__main__":
    main()

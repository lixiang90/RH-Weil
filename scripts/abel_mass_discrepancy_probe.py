#!/usr/bin/env python3
"""[E] Bounded actual Abel mass and centered primitive-energy probe.

Dependencies: installed numpy and mpmath only. No files are written.
Run: python scripts/abel_mass_discrepancy_probe.py

The sieve reaches 25*2**18 by default, but only nonzero prime-power terms
(fewer than 500,000) are evaluated. Printed tail bounds are elementary
analytic majorants evaluated numerically, not interval certificates.
E1 is Gaussian quadrature, checked at two orders; it is not an exact audit.
No asymptotic limit, RH assertion, or first-zero location is inferred.
"""

import argparse
import math

import mpmath as mp
import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial.legendre import leggauss


def prime_power_ledger(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    primes = np.flatnonzero(sieve)
    numbers = [primes]
    values = [np.log(primes.astype(float))]
    extra_n, extra_v = [], []
    for p in primes[primes <= math.isqrt(limit)]:
        p = int(p)
        q, logp = p * p, math.log(p)
        while q <= limit:
            extra_n.append(q)
            extra_v.append(logp)
            q *= p
    numbers.append(np.array(extra_n, dtype=np.int64))
    values.append(np.array(extra_v, dtype=float))
    n, lam = np.concatenate(numbers), np.concatenate(values)
    order = np.argsort(n)
    return n[order], lam[order]


def continuum_mass(sigma, Y, N):
    a = 1 - mp.mpf(str(sigma))
    return mp.power(Y, a) * mp.gammainc(a, mp.mpf(1) / Y, mp.mpf(N) / Y)


def infinite_tail_bound(sigma, Y, N):
    """sum_{n>N} log(n)w(n) + integral_N^infty w(x) dx majorant.

For N/Y>=25, log(x)x^-sigma exp(-x/Y) decreases. The discrete
tail is bounded by its integral from N. Then use
log(x)<=log(N)+(x-N)/N. This yields the expression below.
"""
    a = 1 - mp.mpf(str(sigma))
    tail0 = mp.power(Y, a) * mp.gammainc(a, mp.mpf(N) / Y, mp.inf)
    tail1 = mp.power(Y, a + 1) * mp.gammainc(a + 1, mp.mpf(N) / Y, mp.inf)
    return mp.log(N) * tail0 + tail1 / N


def integrated_lagrange_matrix(nodes):
    out = np.empty((len(nodes), len(nodes)))
    for k in range(len(nodes)):
        polynomial = Polynomial.fromroots(np.delete(nodes, k))
        polynomial /= polynomial(nodes[k])
        primitive = polynomial.integ()
        out[:, k] = primitive(nodes) - primitive(-1)
    return out


def centered_E1(n, weights, sigma, Y, N, A, B, order):
    """Approximate integral |F_{alpha-(A/B)beta}|^2 d(log x).

The prime primitive is exact on intervals between prime powers. Beta is
integrated by Gaussian rules and a polynomial antiderivative on each
interval. Repeating with orders 6 and 10 supplies a numerical check.
"""
    endpoints = np.concatenate(([1], n, [N]))
    if endpoints[-1] == endpoints[-2]:
        endpoints = endpoints[:-1]
    logs = np.log(endpoints.astype(float))
    prime_cdf = np.concatenate(([0.0], np.cumsum(weights, dtype=np.longdouble)))
    prime_cdf = prime_cdf[:len(logs) - 1]
    nodes, gauss_weights = leggauss(order)
    integration = integrated_lagrange_matrix(nodes)
    total_energy, beta_before = np.longdouble(0), np.longdouble(0)
    ratio = np.longdouble(A) / np.longdouble(B)
    for begin in range(0, len(logs) - 1, 65536):
        end = min(begin + 65536, len(logs) - 1)
        widths = np.diff(logs[begin:end + 1])
        midpoints = (logs[begin:end] + logs[begin + 1:end + 1]) / 2
        evaluation = midpoints[:, None] + widths[:, None] * nodes[None, :] / 2
        density = np.exp((1 - sigma) * evaluation - np.exp(evaluation) / Y)
        beta_intervals = widths / 2 * (density @ gauss_weights)
        beta_left = np.concatenate(([0.0], np.cumsum(
            beta_intervals[:-1], dtype=np.longdouble))) + beta_before
        beta_partial = widths[:, None] / 2 * (density @ integration.T)
        primitive = prime_cdf[begin:end, None] - ratio * (
            beta_left[:, None] + beta_partial)
        total_energy += np.sum(widths / 2 * (
            primitive * primitive @ gauss_weights), dtype=np.longdouble)
        beta_before += np.sum(beta_intervals, dtype=np.longdouble)
    return total_energy, beta_before


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=18)
    parser.add_argument("--tail-factor", type=int, default=25)
    parser.add_argument("--skip-e1", action="store_true")
    args = parser.parse_args()
    if not 3 <= args.max_m <= 18 or args.tail_factor < 25:
        parser.error("This bounded probe requires 3<=max-m<=18 and tail-factor>=25.")
    limit = args.tail_factor * 2**args.max_m
    if limit > 12_000_000:
        parser.error("Boolean sieve limit exceeds the bounded 12-million cap.")
    mp.mp.dps = 50
    n_all, lambda_all = prime_power_ledger(limit)
    print("[E] finite numerical probe; no asymptotic or RH claim")
    print(f"sieve_limit={limit}; nonzero_prime_power_terms={len(n_all)}")
    print(f"numpy={np.__version__}; mpmath={mp.__version__}")
    print(f"explicit_mantissa_bits: float64={np.finfo(np.float64).nmant}; "
          f"longdouble={np.finfo(np.longdouble).nmant}")
    print("Tail majorants exclude floating-point coefficient/summation errors; "
          "sample signs are not interval-certified.")
    gamma1 = mp.im(mp.zetazero(1))
    print("sigma,C_sigma,first_zero_Gamma_abs,isolated_pair_balance_log10Y")
    constants = {}
    for sigma in (0.25, 0.5, 0.75):
        s = mp.mpf(str(sigma))
        constant = -mp.diff(mp.zeta, s) / mp.zeta(s) + 1 / (1 - s)
        amplitude = abs(mp.gamma(mp.mpf(".5") - s + 1j * gamma1))
        constants[sigma] = constant
        balance = ("n/a" if sigma >= .5 else mp.nstr(
            mp.log10(abs(constant) / (2 * amplitude)) / (mp.mpf(".5") - s), 16))
        print(f"{sigma},{mp.nstr(constant, 24)},{mp.nstr(amplitude, 16)},{balance}")
    print("Pair balance compares amplitudes only; it does not locate a mass zero.")
    print("sigma,m,Y,N,M_N,M_N_minus_C,numerically_evaluated_tail_majorant")
    e1_cases = []
    for sigma in (0.25, 0.5, 0.75):
        for m in range(3, args.max_m + 1):
            Y, N = 2**m, args.tail_factor * 2**m
            count = np.searchsorted(n_all, N, side="right")
            n, lam = n_all[:count], lambda_all[:count]
            weights = lam * np.exp(-sigma * np.log(n) - n / Y)
            A = np.sum(weights, dtype=np.longdouble)
            Bmp = continuum_mass(sigma, Y, N)
            B = np.longdouble(str(Bmp))
            M = A - B
            delta = mp.mpf(str(M)) - constants[sigma]
            tail = infinite_tail_bound(sigma, Y, N)
            print(f"{sigma},{m},{Y},{N},{M:.16g},{mp.nstr(delta, 12)},{mp.nstr(tail, 8)}")
            if m in {3, min(10, args.max_m), args.max_m}:
                e1_cases.append((sigma, m, Y, N, count, A, B, M))
    if not args.skip_e1:
        print("sigma,m,E1_order6,E1_order10,relative_order_difference,"
              "beta_mass_quadrature_error,E1_over_M_squared")
        for sigma, m, Y, N, count, A, B, M in e1_cases:
            n, lam = n_all[:count], lambda_all[:count]
            weights = lam * np.exp(-sigma * np.log(n) - n / Y)
            e6, _ = centered_E1(n, weights, sigma, Y, N, A, B, 6)
            e10, b10 = centered_E1(n, weights, sigma, Y, N, A, B, 10)
            rel = abs(e6 - e10) / max(abs(e10), np.longdouble(1e-30))
            print(f"{sigma},{m},{e6:.14g},{e10:.14g},{rel:.6g},"
                  f"{abs(b10-B):.6g},{e10/(M*M):.14g}")
        print("E1 is quadrature evidence, not a certified or exact enclosure.")


if __name__ == "__main__":
    main()

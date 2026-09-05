#!/usr/bin/env python3
"""[E] Frozen sigma=1/4, Y=2**m, N=floor(Y log(Y)**2), 3<=m<=18.

Reuses existing Abel routines read-only and writes no data files. The only
evidence is a bounded floating-point calculation; no asymptotic or RH claim.
Run: python -B scripts/dyadic_balanced_moment_probe.py
"""

import argparse
import sys

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np

from abel_mass_discrepancy_probe import (
    centered_E1,
    continuum_mass,
    prime_power_ledger,
)


def cutoff(m):
    return int(mp.floor(mp.mpf(2)**m * (m * mp.log(2))**2))


def continuum_first_moment(Y, N):
    """Derivative in a of integral_1^N x**(a-1) exp(-x/Y) dx."""
    return mp.diff(lambda a: mp.power(Y, a) * mp.gammainc(
        a, mp.mpf(1) / Y, mp.mpf(N) / Y), mp.mpf("0.75"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=18)
    args = parser.parse_args()
    if not 3 <= args.max_m <= 18:
        parser.error("The bounded calculation requires 3<=max-m<=18.")
    mp.mp.dps = 50
    sigma = 0.25
    limit = cutoff(args.max_m)
    n_all, lambda_all = prime_power_ledger(limit)
    print("[E] fixed actual Abel schedule: sigma=1/4, Y=2^m, N=floor(Y log^2Y)")
    print(f"sieve_limit={limit}; nonzero_prime_power_terms={len(n_all)}")
    print(f"numpy={np.__version__}; mpmath={mp.__version__}; "
          f"longdouble_explicit_mantissa_bits={np.finfo(np.longdouble).nmant}")
    print("Float coefficient/summation errors are not interval-enclosed. "
          "Quadrature agreement is not a proof or asymptotic bound.")
    print("m,Y,N,M,first_moment_zeta,first_moment_squared_over_LM2")
    e1_cases = []
    for m in range(3, args.max_m + 1):
        Y, N = 2**m, cutoff(m)
        L = np.longdouble(str(m * mp.log(2)))
        count = np.searchsorted(n_all, N, side="right")
        n, lam = n_all[:count], lambda_all[:count]
        logs = np.log(n)
        weights = lam * np.exp(-sigma * logs - n / Y)
        A = np.sum(weights, dtype=np.longdouble)
        A1 = np.sum(weights * logs, dtype=np.longdouble)
        B = np.longdouble(str(continuum_mass(sigma, Y, N)))
        B1 = np.longdouble(str(continuum_first_moment(Y, N)))
        M = A - B
        first = A1 - (A / B) * B1
        moment_ratio = first * first / (L * M * M)
        print(f"{m},{Y},{N},{M:.16g},{first:.16g},{moment_ratio:.14g}")
        if m in {3, 8, 12, 16, 18}:
            e1_cases.append((m, Y, N, L, count, A, B, M, first))
    print("m,E1_order6,E1_order10,relative_order_difference,"
          "E1_over_LM2,first_moment_squared_over_logN_E1,"
          "beta_mass_quadrature_error")
    for m, Y, N, L, count, A, B, M, first in e1_cases:
        n, lam = n_all[:count], lambda_all[:count]
        weights = lam * np.exp(-sigma * np.log(n) - n / Y)
        E6, _ = centered_E1(n, weights, sigma, Y, N, A, B, 6)
        E10, beta10 = centered_E1(n, weights, sigma, Y, N, A, B, 10)
        difference = abs(E6 - E10) / max(abs(E10), np.longdouble(1e-30))
        energy_ratio = E10 / (L * M * M)
        # Integration by parts and Cauchy give first^2 <= log(N) E1
        # for exact zero-mass zeta. This ratio measures that test's capture.
        capture = first * first / (np.log(N) * E10)
        print(f"{m},{E6:.14g},{E10:.14g},{difference:.6g},"
              f"{energy_ratio:.14g},{capture:.14g},{abs(beta10-B):.6g}")
    print("All displayed trends remain finite numerical evidence [E].")


if __name__ == "__main__":
    main()

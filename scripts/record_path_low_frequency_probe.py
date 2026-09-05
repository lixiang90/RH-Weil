#!/usr/bin/env python3
"""[E] Bounded record-envelope and actual Abel-path probe; no files written.

Run: python -B scripts/record_path_low_frequency_probe.py --max-m 12
Fixed sigma=1/4, beta=3/8. Each dyadic window uses the floating maximum
over the finite endpoint/prime-power candidates of note 271. This is NOT
an interval-certified maximum, a historical-record selection, or a point
on the theoretical cofinal sequence. All path quadrature is numerical.

H(log x)=sum_{n<=x} Lambda(n)n^-sigma exp(-n/Y) - integral_1^x w_Y.
H is the UNBALANCED discrepancy path, not the mass-zero zeta path of
note 264. Integrals use du=dx/x and preserve every integer jump. Splitting
each sign-changing cell removes the absolute-value kink. Orders 12/24
are compared; their difference is not a certified integration error.
The smallest window uses independent trial division and 50-digit
Stieltjes/Fourier checks. No asymptotic or full-J4 conclusion follows.
"""

from __future__ import annotations

import argparse
import math
import sys
import time
from fractions import Fraction

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np
import scipy
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import gamma, gammainc

from abel_mass_discrepancy_probe import prime_power_ledger


SIGMA = 0.25
BETA = 0.375
DELTA = BETA - SIGMA
A = 1.0 - SIGMA


def ell(Y: int) -> float:
    return max(1.0, math.log(math.log(math.log(Y))))


def continuum(Y: int, x):
    return Y**A * gamma(A) * (gammainc(A, np.asarray(x) / Y) - gammainc(A, 1.0 / Y))


def unweighted_records(limit: int, numbers, lambdas):
    """Maintain psi, R, and its normalized prefix maximum independently of w."""
    ledger = np.zeros(limit + 1)
    ledger[numbers] = lambdas
    psi = np.cumsum(ledger, dtype=np.longdouble)
    integers = np.arange(limit + 1, dtype=np.longdouble)
    discrepancy = psi - integers
    scores = np.zeros(limit + 1, dtype=np.longdouble)
    scores[1:] = np.abs(discrepancy[1:]) / integers[1:]**BETA
    return discrepancy, scores, np.maximum.accumulate(scores)


def weighted_prefix(limit: int, numbers, lambdas, Y: int):
    ledger = np.zeros(limit + 1, dtype=np.longdouble)
    ledger[numbers] = lambdas * np.exp(-SIGMA * np.log(numbers) - numbers / Y)
    return np.cumsum(ledger, dtype=np.longdouble)


def candidate_maximum(Y: int, numbers, prefix):
    jumps = numbers[(numbers > Y) & (numbers <= 2 * Y)]
    candidates = np.unique(np.concatenate(([Y, 2 * Y], jumps - 1, jumps)))
    masses = prefix[candidates] - continuum(Y, candidates)
    selected = int(np.argmax(np.abs(masses)))
    return int(candidates[selected]), float(masses[selected]), len(candidates)


def split_integer_cells(Y: int, N: int, prefix):
    left = np.arange(1, N, dtype=float)
    right = left + 1.0
    prime = np.asarray(prefix[1:N], dtype=float)
    hl = prime - continuum(Y, left)
    hr = prime - continuum(Y, right)  # right limit BEFORE that endpoint's jump
    crossing = np.flatnonzero((hl > 0) & (hr < 0))
    extra_left, extra_right, extra_prime = [], [], []
    for index in crossing:
        old_right = right[index]
        root = brentq(lambda x: prime[index] - float(continuum(Y, x)),
                      left[index], old_right, xtol=1e-13, rtol=1e-14)
        right[index] = root
        extra_left.append(root)
        extra_right.append(old_right)
        extra_prime.append(prime[index])
    return (np.concatenate((left, extra_left)),
            np.concatenate((right, extra_right)),
            np.concatenate((prime, extra_prime)), len(crossing))


def path_norms(Y: int, cells, order: int):
    left, right, prime, _ = cells
    nodes, weights = leggauss(order)
    total1, total2 = np.longdouble(0), np.longdouble(0)
    for begin in range(0, len(left), 4096):
        end = min(begin + 4096, len(left))
        ulo, uhi = np.log(left[begin:end]), np.log(right[begin:end])
        half = (uhi - ulo) / 2
        u = (ulo + uhi)[:, None] / 2 + half[:, None] * nodes
        h = prime[begin:end, None] - continuum(Y, np.exp(u))
        measure = half[:, None] * weights
        total1 += np.sum(measure * np.abs(h), dtype=np.longdouble)
        total2 += np.sum(measure * h**2, dtype=np.longdouble)
    return float(total1), float(total2)


def exact_endpoint_normalization() -> None:
    # (1-cos t)^4 = sum_{k=0}^4 c_k cos(k t).
    coefficients = [Fraction(35, 8), Fraction(-7), Fraction(7, 2),
                    Fraction(-1), Fraction(1, 8)]
    assert sum(coefficients) == 0
    # (2pi)^-1 integral_R (1-cos(k t))/t^2 dt = |k|/2.
    constant = -sum(k * coefficients[k] for k in range(1, 5)) / 2
    assert constant == Fraction(5, 4)
    print("Exact rational normalization: endpoint fourth-energy constant = 5/4.")


def trial_lambda(n: int):
    """Independent integer trial division; never reuse the sieve logarithms."""
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            rest = n
            while rest % p == 0:
                rest //= p
            return mp.log(p) if rest == 1 else mp.mpf(0)
    return mp.log(n) if n >= 2 else mp.mpf(0)


def independent_small_check(Y: int, N: int, mass: float, norms, record_value: float):
    mp.mp.dps = 50
    sigma, beta = mp.mpf(1) / 4, mp.mpf(3) / 8
    exponent = 1 - sigma
    lam = [trial_lambda(n) for n in range(2 * Y + 1)]
    prime, psi = [mp.mpf(0)], [mp.mpf(0)]
    for n in range(1, 2 * Y + 1):
        prime.append(prime[-1] + lam[n] * mp.power(n, -sigma) * mp.exp(-mp.mpf(n) / Y))
        psi.append(psi[-1] + lam[n])

    def continuous(x):
        return mp.power(Y, exponent) * mp.gammainc(exponent, mp.mpf(1) / Y, x / Y)

    def hcell(x, j):
        return prime[j] - continuous(x)

    masses = {j: prime[j] - continuous(mp.mpf(j)) for j in range(Y, 2 * Y + 1)}
    winner = max(masses, key=lambda j: abs(masses[j]))
    assert winner == N, "Small independent full scan disagrees with float candidate"
    high_mass = masses[N]
    high_record = max(abs(psi[j] - j) / mp.power(j, beta) for j in range(1, N + 1))
    assert abs(high_mass - mass) < mp.mpf("1e-11")
    assert abs(high_record - record_value) < mp.mpf("1e-11")
    energy1, energy2 = mp.mpf(0), mp.mpf(0)
    for j in range(1, N):
        lo, hi = mp.mpf(j), mp.mpf(j + 1)
        points = [lo, hi]
        if hcell(lo, j) > 0 > hcell(hi, j):
            a, b = lo, hi
            for _ in range(100):
                middle = (a + b) / 2
                if hcell(middle, j) > 0:
                    a = middle
                else:
                    b = middle
            points = [lo, (a + b) / 2, hi]
        energy1 += mp.quad(lambda x: abs(hcell(x, j)) / x, points)
        energy2 += mp.quad(lambda x: hcell(x, j)**2 / x, points)
    errors = [abs(energy1 - norms[0]), abs(energy2 - norms[1])]
    assert max(errors) < mp.mpf("1e-10")
    print("  MP50 independent m=4: trial-Lambda full integer winner agrees; "
          f"mass_error={mp.nstr(abs(high_mass-mass), 6)}, "
          f"P_error={mp.nstr(abs(high_record-record_value), 6)}, "
          f"path_errors={[mp.nstr(e, 6) for e in errors]}")
    tau = mp.log(N)
    largest = mp.mpf(0)
    for xi in (mp.mpf(0), mp.mpf(1) / 8, mp.mpf(1) / 2, mp.sqrt(mp.log(Y))):
        discrete = mp.fsum(lam[n] * mp.power(n, -sigma) * mp.exp(-mp.mpf(n) / Y)
                          * (mp.cos(xi * mp.log(n)) - 1) for n in range(2, N + 1))
        continuous_response = mp.quad(
            lambda x: mp.power(x, -sigma) * mp.exp(-x / Y) * (mp.cos(xi * mp.log(x)) - 1),
            [1, N],
        )
        direct = discrete - continuous_response
        sine = mp.fsum(mp.quad(lambda x: hcell(x, j) * mp.sin(xi * mp.log(x)) / x,
                              [j, j + 1]) for j in range(1, N))
        stieltjes = high_mass * (mp.cos(xi * tau) - 1) + xi * sine
        error = abs(direct - stieltjes)
        largest = max(largest, error)
        assert error < mp.mpf("1e-38")
        print(f"  MP50 rhat xi={mp.nstr(xi, 10)}: value={mp.nstr(direct, 18)}, "
              f"Stieltjes_error={mp.nstr(error, 6)}")
    return largest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=12, choices=(4, 6, 8, 10, 12, 14, 16))
    args = parser.parse_args()
    started = time.perf_counter()
    m_values = [m for m in (4, 6, 8, 10, 12, 14, 16) if m <= args.max_m]
    limit = 2**(args.max_m + 1)
    numbers, lambdas = prime_power_ledger(limit)
    _, scores, records = unweighted_records(limit, numbers, lambdas)
    print("[E] sigma=1/4 beta=3/8; floating window maxima, NOT certified/cofinal points.")
    print(f"numpy={np.__version__}; scipy={scipy.__version__}; mpmath={mp.__version__}")
    exact_endpoint_normalization()
    print("m,Y,N,M,Pbeta,record_index,Pbeta_Ndelta_over_absM,H_L1_over_absM,"
          "H_L2_squared_over_M2,absM_over_large_threshold,large_threshold_reached,"
          "sign_split_cells,quad12_24_L1_difference,quad12_24_L2_squared_difference")
    small = None
    for m in m_values:
        Y = 2**m
        prefix = weighted_prefix(2 * Y, numbers[numbers <= 2 * Y], lambdas[numbers <= 2 * Y], Y)
        N, mass, _ = candidate_maximum(Y, numbers, prefix)
        assert mass != 0, "Numerically zero selected mass cannot be normalized"
        cells = split_integer_cells(Y, N, prefix)
        low = path_norms(Y, cells, 12)
        high = path_norms(Y, cells, 24)
        threshold = Y**(0.5 - SIGMA) * math.sqrt(ell(Y))
        pvalue = float(records[N])
        record_index = int(np.argmax(scores[:N + 1]))
        print(f"{m},{Y},{N},{mass:.15g},{pvalue:.12g},{record_index},"
              f"{pvalue*N**DELTA/abs(mass):.12g},{high[0]/abs(mass):.12g},"
              f"{high[1]/mass**2:.12g},{abs(mass)/threshold:.12g},"
              f"{abs(mass)>threshold},{cells[3]},"
              f"{abs(low[0]-high[0]):.5g},{abs(low[1]-high[1]):.5g}", flush=True)
        if m == 4:
            small = (Y, N, mass, high, pvalue)
    identity_error = independent_small_check(*small)
    print(f"PASS finite normalization/smoke checks; windows={len(m_values)}; "
          f"max_MP50_identity_error={mp.nstr(identity_error, 6)}; "
          f"elapsed_seconds={time.perf_counter()-started:.3f}")
    print("[E] Quadrature/order comparisons and MP samples are not interval certificates. "
          "No theoretical cofinal selection, asymptotic estimate, or full J4 was computed.")


if __name__ == "__main__":
    main()

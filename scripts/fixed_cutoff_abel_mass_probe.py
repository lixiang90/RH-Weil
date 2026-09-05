#!/usr/bin/env python3
"""[E] Integer samples of M(Y,Y), incomplete-gamma checks, finite Mellin identity.

Run: python -B scripts/fixed_cutoff_abel_mass_probe.py
Default scans every INTEGER N=Y<=2^18; --max-m 16 shortens the scan.
No O(N^2) summation: on n/N in [0,1], degree-18/24 Taylor polynomials
for exp(-n/N) reduce each scan to normalized positive prefix sums.
The analytic degree-k remainder is <= sum_{n<=N}Lambda(n)n^-sigma/(k+1)!.
This controls polynomial truncation ONLY, not floating-point roundoff.
Selected sample endpoints/extrema are separately checked by direct fsum
and an MP50 continuum mass. Opposite integer signs are NOT certified
continuous roots: M(Y,Y) has prime-power jumps, and unsampled real Y
are not exhausted.

For X=16,32, an independent piecewise-in-Y Gaussian MP50 integral checks
the exact FINITE identity
 int_1^X M(Y,Y)Y^(-s-1)dY
 = sum_{n<=X}Lambda(n)n^(-sigma-s) int_{n/X}^1 t^(s-1)e^-t dt
   - int_1^X x^(-sigma-s) int_{x/X}^1 t^(s-1)e^-t dt dx.
The finite kernel equals gamma(s,1)-gamma(s,x/X), with no infinite
sum exchange or limiting-height assumption. Each Y-cell keeps all
n<=floor(Y), with its right-continuous lower-end atom included.

gamma1=Im(mpmath.zetazero(1)) is only a numerical template parameter.
Lower-gamma recurrence and nonzero magnitudes are compared at MP50.
Separately, Re s>=0 and |Im s|>2 imply the analytic lower bound
 |gamma(s,1)| >= exp(-1)*(1-2/|Im s|)/|s|:
 integration by parts bounds gamma(s+1,1) by 2 exp(-1)/|Im s|
 because its positive log-coordinate density is decreasing. Combine
 with s*gamma(s,1)=gamma(s+1,1)+exp(-1).
Printed evaluations of this bound remain floating-point [E].

No files, PDF, CI changes, full-frequency responses, certified zeros,
infinite oscillation, or note-275 cofinal certification are produced.
SciPy is an optional local probe dependency.
"""

from __future__ import annotations

import argparse
import math
import sys
import time

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np
import scipy
from scipy.special import gamma, gammainc

from abel_mass_discrepancy_probe import prime_power_ledger
from record_path_low_frequency_probe import trial_lambda

SIGMA = .25


def integer_scan(limit, numbers, lambdas):
    """O(24*limit) normalized prefix sums; Kahan summation over Taylor degrees."""
    integers = np.arange(1, limit + 1, dtype=np.longdouble)
    grid = integers / limit
    weighted = np.zeros(limit, dtype=np.longdouble)
    weighted[numbers - 1] = lambdas * np.exp(-SIGMA * np.log(numbers))
    prefix0 = np.cumsum(weighted, dtype=np.longdouble)
    approximation = prefix0.copy()
    compensation = np.zeros(limit, dtype=np.longdouble)
    factor = np.ones(limit, dtype=np.longdouble)
    coarse = None
    for degree in range(1, 25):
        weighted *= grid
        factor *= -1 / (degree * grid)
        term = factor * np.cumsum(weighted, dtype=np.longdouble)
        increment = term - compensation
        updated = approximation + increment
        compensation = (updated - approximation) - increment
        approximation = updated
        if degree == 18:
            coarse = approximation.copy()
    n_float = np.asarray(integers, dtype=float)
    continuum = n_float**.75 * gamma(.75) * (
        gammainc(.75, 1.) - gammainc(.75, 1 / n_float)
    )
    masses = approximation - continuum
    masses[0] = 0  # exact M(1,1); never infer its sign from rounding
    return masses, float(np.max(np.abs(approximation - coarse))), \
        float(prefix0[-1] / math.factorial(25))


def direct_scan_checks(masses, numbers, lambdas, selected):
    largest = 0.0
    for N in sorted(selected):
        keep = numbers <= N
        n, lam = numbers[keep], lambdas[keep]
        discrete = math.fsum(lam * np.exp(-SIGMA * np.log(n) - n / N))
        continuous = mp.power(N, mp.mpf(".75")) * mp.gammainc(
            mp.mpf(".75"), mp.mpf(1) / N, 1
        )
        direct = mp.mpf(discrete) - continuous
        error = abs(mp.mpf(float(masses[N - 1])) - direct)
        largest = max(largest, float(error))
        print(f"direct sample N={N},M={mp.nstr(direct, 17)},"
              f"prefix_abs_difference={mp.nstr(error, 6)}")
    assert largest < 1e-6
    return largest


def gamma_checks():
    gamma1 = mp.im(mp.zetazero(1))
    print("MP50 gamma1 NUMERICAL TEMPLATE=" + mp.nstr(gamma1, 40))
    print("s,abs_lower_gamma,abs_complete_gamma,recurrence_error,"
          "abs_gamma_splus1_over_exp_minus1,analytic_lower_bound_evaluated")
    for s in (mp.mpf(".25"), mp.mpf(".25") + 1j*gamma1,
              mp.mpf(".25") + 2j*gamma1):
        lower = mp.gammainc(s, 0, 1)
        next_lower = mp.gammainc(s + 1, 0, 1)
        error = abs(s * lower - next_lower - mp.exp(-1))
        assert error < mp.mpf("1e-45")
        lower_bound = (mp.exp(-1) * (1 - 2/abs(mp.im(s))) / abs(s)
                       if abs(mp.im(s)) > 2 else mp.mpf(0))
        assert abs(lower) >= lower_bound
        print(",".join(mp.nstr(value, 13) for value in (
            s, abs(lower), abs(mp.gamma(s)), error,
            abs(next_lower) / mp.exp(-1), lower_bound
        )))
    return gamma1


def left_mellin_values(cases, order, ledger):
    """Direct Y-cell integral, independent of the exchanged finite kernel."""
    nodes, weights = mp.gauss_quadrature(order, "legendre")
    results = [mp.mpc(0) for _ in cases]
    upper = max(X for X, _ in cases)
    quarter = mp.mpf(1) / 4
    for integer in range(1, upper):
        active = [(n, lam * mp.power(n, -quarter))
                  for n, lam in ledger if n <= integer]
        for node, weight in zip(nodes, weights):
            y = mp.mpf(integer) + (node + 1) / 2
            discrete = mp.fsum(coefficient * mp.exp(-mp.mpf(n) / y)
                               for n, coefficient in active)
            continuous = mp.power(y, mp.mpf(3)/4) * mp.gammainc(
                mp.mpf(3)/4, 1/y, 1
            )
            mass = discrete - continuous
            for index, (X, s) in enumerate(cases):
                if integer < X:
                    results[index] += weight/2 * mass * mp.power(y, -s-1)
    return results


def right_mellin_value(X, s, order, ledger):
    """Swapped finite expression; continuum integrated in log x, not Y cells."""
    quarter = mp.mpf(1) / 4

    def kernel(x):
        return mp.gammainc(s, mp.mpf(x) / X, 1)

    discrete = mp.fsum(lam * mp.power(n, -quarter-s) * kernel(n)
                       for n, lam in ledger if n <= X)
    nodes, weights = mp.gauss_quadrature(order, "legendre")
    log_x = mp.log(X)
    panels = int(mp.ceil(log_x / mp.mpf(".5")))
    continuous = mp.mpc(0)
    for panel in range(panels):
        lo, hi = log_x * panel / panels, log_x * (panel + 1) / panels
        for node, weight in zip(nodes, weights):
            u = (lo + hi)/2 + (hi - lo)*node/2
            continuous += (hi-lo)*weight/2 * mp.exp((1-quarter-s)*u) * kernel(mp.exp(u))
    return discrete - continuous


def finite_mellin_checks(gamma1):
    real_s, complex_s = mp.mpf(".25"), mp.mpf(".25") + 1j*gamma1
    cases = [(16, real_s), (16, complex_s), (32, complex_s)]
    ledger = [(n, trial_lambda(n)) for n in range(2, 33)]
    ledger = [(n, lam) for n, lam in ledger if lam]
    lhs20, lhs32 = left_mellin_values(cases, 20, ledger), left_mellin_values(cases, 32, ledger)
    largest_identity, largest_rule = mp.mpf(0), mp.mpf(0)
    print("MP50 finite Mellin: X,s,LHS32,RHS32,absolute_identity_error,"
          "largest_20_32_difference")
    for index, (X, s) in enumerate(cases):
        rhs20 = right_mellin_value(X, s, 20, ledger)
        rhs32 = right_mellin_value(X, s, 32, ledger)
        identity = abs(lhs32[index] - rhs32)
        difference = max(abs(lhs32[index] - lhs20[index]), abs(rhs32 - rhs20))
        largest_identity, largest_rule = max(largest_identity, identity), max(largest_rule, difference)
        assert identity < mp.mpf("1e-28")
        assert difference < mp.mpf("1e-18")
        print(f"{X}," + ",".join(mp.nstr(value, 18) for value in (
            s, lhs32[index], rhs32, identity, difference
        )))
    return largest_identity, largest_rule


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, choices=(12, 14, 16, 18), default=18)
    args = parser.parse_args()
    started = time.perf_counter()
    mp.mp.dps = 50
    limit = 2**args.max_m
    numbers, lambdas = prime_power_ledger(limit)
    masses, order_difference, remainder_bound = integer_scan(limit, numbers, lambdas)
    scan_seconds = time.perf_counter() - started
    minimum_N, maximum_N = int(np.argmin(masses[1:])) + 2, int(np.argmax(masses[1:])) + 2
    tolerance = 1e-7  # diagnostic exclusion band, NOT a certified error bound
    signs = np.where(masses > tolerance, 1, np.where(masses < -tolerance, -1, 0))
    changes = np.flatnonzero(signs[1:-1] * signs[2:] == -1) + 2
    print("[E] all INTEGER Y=N samples; sign changes are not continuous-root certificates.")
    print(f"numpy={np.__version__}; scipy={scipy.__version__}; mpmath={mp.__version__}; "
          f"longdouble_mantissa={np.finfo(np.longdouble).nmant}")
    print(f"scan_limit={limit}; seconds={scan_seconds:.3f}; degree18_24_difference={order_difference:.6g}; "
          f"degree24_analytic_truncation_majorant={remainder_bound:.6g} (roundoff excluded)")
    print(f"positive_samples={np.count_nonzero(signs[1:] == 1)};"
          f" negative_samples={np.count_nonzero(signs[1:] == -1)};"
          f" near_zero_samples={np.count_nonzero(signs[1:] == 0)};"
          f" opposite_adjacent_integer_pairs={len(changes)}")
    print("N,M(N,N),prefix_min_N,prefix_min_M,prefix_max_N,prefix_max_M")
    for m in range(4, args.max_m + 1, 2):
        N = 2**m
        imin, imax = int(np.argmin(masses[1:N])) + 2, int(np.argmax(masses[1:N])) + 2
        print(f"{N},{masses[N-1]:.12g},{imin},{masses[imin-1]:.12g},"
              f"{imax},{masses[imax-1]:.12g}")
    shown = sorted(set(changes[:4].tolist() + changes[-4:].tolist()))
    print("Opposite integer-sign samples (left,right): "
          + ",".join(f"({N},{N+1})" for N in shown))
    selected = {16, 32, limit, minimum_N, maximum_N}
    for N in changes[:1].tolist() + changes[-1:].tolist():
        selected.update((N, N + 1))
    direct_error = direct_scan_checks(masses, numbers, lambdas, selected)
    gamma1 = gamma_checks()
    identity_error, mellin_rule = finite_mellin_checks(gamma1)
    print(f"SUMMARY sampled extrema: min M({minimum_N})={masses[minimum_N-1]:.12g}; "
          f"max M({maximum_N})={masses[maximum_N-1]:.12g}.")
    print(f"SUMMARY largest selected direct-prefix difference={direct_error:.7g}; "
          f"finite Mellin identity error={mp.nstr(identity_error, 7)}, "
          f"20/32-order difference={mp.nstr(mellin_rule, 7)}.")
    print(f"SUMMARY PASS finite checks; elapsed_seconds={time.perf_counter()-started:.3f}.")
    print("SUMMARY [E] No certified signs, unbounded oscillation, kernel zero location, "
          "infinite Mellin formula, or note-275 record selection established.")


if __name__ == "__main__":
    main()

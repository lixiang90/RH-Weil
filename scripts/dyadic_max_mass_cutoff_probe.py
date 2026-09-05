#!/usr/bin/env python3
"""[E] Bounded integer-cutoff search for the actual matched Abel mass.

Run: python -B scripts/dyadic_max_mass_cutoff_probe.py
Optional: --max-m 20 (default 18; fixed list 4,6,8,10,12,16,18,20).

For sigma=1/4 and each Y=2**m, search integer N in [Y,2Y]. Between
prime powers the prime mass is constant and the continuum mass increases
strictly. Thus an integer maximizer of |M| is among the window endpoints
and n-1,n for prime powers Y<n<=2Y. The selection itself uses float64:
it is NOT a certified maximizer. SciPy incomplete gamma evaluates every
candidate continuum mass; 50-digit mpmath recomputes complete prime sums
for the five floating leaders, the winner's nearby integers, and the
first-prime pair used in note 268. The smallest window is additionally
checked by a full integer scan with independent trial-factor coefficients.

All output is finite floating-point evidence, not interval arithmetic,
an asymptotic lower bound, or a theorem about the full response J4.
No files are written and no dependencies are installed.
"""

import argparse
import math
import sys
import time

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np
import scipy
from scipy.special import gamma, gammainc

from abel_mass_discrepancy_probe import continuum_mass, prime_power_ledger
from prime_jump_cutoff_probe import first_prime_above, von_mangoldt_mp


SIGMA = 0.25
A_EXPONENT = 0.75


def candidate_cutoffs(n, Y):
    """All possible integer extrema; endpoints and before/at each jump."""
    jumps = n[(n > Y) & (n <= 2*Y)]
    return np.unique(np.concatenate(([Y, 2*Y], jumps-1, jumps)))


def continuum_vector(Y, cutoffs):
    lower = gammainc(A_EXPONENT, 1.0/Y)
    return (Y**A_EXPONENT * gamma(A_EXPONENT)
            * (gammainc(A_EXPONENT, cutoffs.astype(float)/Y)-lower))


def float_masses(n, lam, Y, cutoffs):
    weights = lam*np.exp(-SIGMA*np.log(n)-n/Y)
    prefix = np.concatenate(([0.0], np.cumsum(weights, dtype=np.float64)))
    counts = np.searchsorted(n, cutoffs, side="right")
    return prefix[counts]-continuum_vector(Y, cutoffs)


def recover_integer_bases(n, lam):
    """Recover exact bases from the sieve ledger and verify integer powers.

    The ledger's sieve determines primality. The integer power check means
    mpmath never treats the stored floating logarithm as an exact coefficient.
    Independent trial factorization is used for the smallest-window scan.
    """
    bases = np.rint(np.exp(lam)).astype(np.int64)
    for number, base in zip(n, bases):
        rest, base = int(number), int(base)
        assert base >= 2
        while rest % base == 0:
            rest //= base
        assert rest == 1, (number, base)
    return bases


def mp_masses(n, bases, Y, cutoffs):
    """Complete 50-digit sums, with one ordered pass for selected cutoffs."""
    wanted = sorted(set(int(N) for N in cutoffs))
    result, cursor = {}, 0
    prime_mass = mp.mpf(0)
    sigma = mp.mpf(".25")
    for N in wanted:
        endpoint = int(np.searchsorted(n, N, side="right"))
        terms = []
        for index in range(cursor, endpoint):
            number, base = int(n[index]), int(bases[index])
            terms.append(mp.log(base)*mp.power(number, -sigma)
                         *mp.exp(-mp.mpf(number)/Y))
        prime_mass += mp.fsum(terms)
        result[N] = prime_mass-continuum_mass(SIGMA, Y, N)
        cursor = endpoint
    return result


def independent_small_scan(Y, candidates, selected_N, selected_mass):
    """All integer cutoffs; coefficients independently trial-factored."""
    prime_mass, values = mp.mpf(0), {}
    sigma = mp.mpf(".25")
    for N in range(2, 2*Y+1):
        prime_mass += (von_mangoldt_mp(N)*mp.power(N, -sigma)
                       *mp.exp(-mp.mpf(N)/Y))
        if N >= Y:
            values[N] = prime_mass-continuum_mass(SIGMA, Y, N)
    winner = max(values, key=lambda N: abs(values[N]))
    candidate_winner = max((int(N) for N in candidates),
                           key=lambda N: abs(values[N]))
    assert winner == candidate_winner == selected_N
    error = abs(values[winner]-mp.mpf(str(selected_mass)))
    assert error < mp.mpf("1e-10")
    print("Independent m=4 full-integer 50-digit scan: "
          f"integers={Y+1}; winner_N={winner}; "
          f"winner_M={mp.nstr(values[winner], 25)}; "
          f"float_error={mp.nstr(error, 7)}; "
          "candidate reduction and float winner agree numerically.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=18,
                        choices=(4, 6, 8, 10, 12, 16, 18, 20))
    args = parser.parse_args()
    started = time.perf_counter()
    mp.mp.dps = 50
    m_values = [m for m in (4, 6, 8, 10, 12, 16, 18, 20)
                if m <= args.max_m]
    limit = 2**(args.max_m+1)
    n_all, lam_all = prime_power_ledger(limit)
    bases_all = recover_integer_bases(n_all, lam_all)
    print("[E] actual sigma=.25; bounded integer-cutoff maximum probe")
    print(f"numpy={np.__version__}; scipy={scipy.__version__}; "
          f"mpmath={mp.__version__}; mp_dps={mp.mp.dps}; "
          f"longdouble_explicit_mantissa_bits={np.finfo(np.longdouble).nmant}")
    print(f"sieve_limit={limit}; total_prime_power_terms={len(n_all)}")
    print("Every maximum is a floating candidate, not an interval-certified "
          "global maximum. No asymptotic or full-response conclusion follows.")
    print("m,Y,window_prime_powers,candidates,float_best_N,float_best_M,"
          "max_absM_over_logY_quarter,max_absM_over_Y_quarter,best_N_over_Y,"
          "first_prime_q,first_pair_best_N,first_pair_M,"
          "first_absM_over_logY_quarter,max_over_first_absM,"
          "float_top_two_abs_gap,mp_best_M,mp_checked_cutoffs,"
          "max_float_mass_error_in_checks,max_continuum_error_in_checks")
    small_check = None
    max_mass_error = mp.mpf(0)
    max_beta_error = mp.mpf(0)
    for m in m_values:
        Y, L = 2**m, math.log(2**m)
        end = int(np.searchsorted(n_all, 2*Y, side="right"))
        n, lam, bases = n_all[:end], lam_all[:end], bases_all[:end]
        candidates = candidate_cutoffs(n, Y)
        masses = float_masses(n, lam, Y, candidates)
        order = np.argsort(-np.abs(masses), kind="stable")
        winner_index = int(order[0])
        winner_N, winner_mass = int(candidates[winner_index]), masses[winner_index]
        q = first_prime_above(Y)
        first_cutoffs = np.array([q-1, q], dtype=np.int64)
        first_masses = float_masses(n, lam, Y, first_cutoffs)
        first_index = int(np.argmax(np.abs(first_masses)))
        first_N, first_mass = int(first_cutoffs[first_index]), first_masses[first_index]
        nearby = [N for N in range(winner_N-2, winner_N+3) if Y <= N <= 2*Y]
        checks = sorted(set(nearby + [int(candidates[i]) for i in order[:5]]
                            + [q-1, q]))
        high = mp_masses(n, bases, Y, checks)
        high_winner = max(checks, key=lambda N: abs(high[N]))
        high_first = max((q-1, q), key=lambda N: abs(high[N]))
        assert high_winner == winner_N, "MP checks disagree with float winner"
        assert high_first == first_N, "MP checks disagree with first-pair choice"
        checked_floats = float_masses(n, lam, Y, np.array(checks))
        checked_betas = continuum_vector(Y, np.array(checks))
        mass_error = max(abs(mp.mpf(str(value))-high[N])
                         for N, value in zip(checks, checked_floats))
        beta_error = max(abs(mp.mpf(str(value))-continuum_mass(SIGMA, Y, N))
                         for N, value in zip(checks, checked_betas))
        max_mass_error = max(max_mass_error, mass_error)
        max_beta_error = max(max_beta_error, beta_error)
        # Generous smoke-test tolerances, not certified error enclosures.
        assert mass_error < mp.mpf("1e-6")
        assert beta_error < mp.mpf("1e-7")
        window_terms = int(np.count_nonzero((n > Y) & (n <= 2*Y)))
        gap = abs(masses[order[0]])-abs(masses[order[1]])
        print(f"{m},{Y},{window_terms},{len(candidates)},{winner_N},"
              f"{winner_mass:.16g},{abs(winner_mass)/L**.25:.14g},"
              f"{abs(winner_mass)/Y**.25:.14g},{winner_N/Y:.14g},"
              f"{q},{first_N},{first_mass:.16g},"
              f"{abs(first_mass)/L**.25:.14g},"
              f"{abs(winner_mass)/abs(first_mass):.14g},{gap:.9g},"
              f"{mp.nstr(high[winner_N], 23)},{len(checks)},"
              f"{mp.nstr(mass_error, 7)},{mp.nstr(beta_error, 7)}", flush=True)
        print("  MP50 checked N and mass: " + "; ".join(
            f"{N}:{mp.nstr(high[N], 18)}" for N in checks), flush=True)
        if m == 4:
            small_check = (Y, candidates, winner_N, winner_mass)
    independent_small_scan(*small_check)
    print(f"PASS {len(m_values)} bounded windows; all floating winners "
          "agree with their checked MP50 competitors. "
          f"largest_checked_mass_error={mp.nstr(max_mass_error, 7)}; "
          f"largest_checked_continuum_error={mp.nstr(max_beta_error, 7)}; "
          f"elapsed_seconds={time.perf_counter()-started:.3f}")
    print("MP50 samples do not certify unexamined floating ordering or "
          "global error bounds. A rigorous maximum requires interval arithmetic.")


if __name__ == "__main__":
    main()

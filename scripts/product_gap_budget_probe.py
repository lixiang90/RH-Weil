#!/usr/bin/env python3
"""[E] Eight bounded actual product-support nearest-gap computations.

Run: python -B scripts/product_gap_budget_probe.py

Fixed sigma=1/4 and Y=16,64,256,1024. For each Y use N=2Y and the
floating maximum-mass candidate recomputed among all possible integer
extrema in [Y,2Y]. No cutoff choice is claimed to be interval-certified.

Integer products are aggregated exactly as integer keys; their actual
logarithmic/Abel coefficients and gap energies use floating arithmetic.
Nearest logarithmic gaps are evaluated by log1p on adjacent sorted keys.
The two Y=16 cases are independently recomputed with trial-factorized
coefficients, mpmath at 50 digits, and dictionary product aggregation.

No assertion certifies the asymptotic conjecture
G(Y,N) = O_sigma(Y**(4-4*sigma)*log(Y)). An unknown-constant asymptotic
bound cannot be disproved by a single bounded sample. No files are written.
"""

import math
import sys
import time

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np

from abel_mass_discrepancy_probe import prime_power_ledger
from dyadic_max_mass_cutoff_probe import candidate_cutoffs, float_masses
from prime_jump_cutoff_probe import von_mangoldt_mp


def gap_energy_float(n, lam, Y):
    """Aggregate ordered pairs by exact int64 product; coefficients are floats."""
    weights = lam*np.exp(-0.25*np.log(n)-n/Y)
    products = (n[:, None]*n[None, :]).ravel()
    pair_weights = (weights[:, None]*weights[None, :]).ravel()
    support, inverse = np.unique(products, return_inverse=True)
    coefficients = np.bincount(inverse, weights=pair_weights)
    assert len(support) >= 2 and np.all(coefficients > 0)
    assert np.all(support[1:] > support[:-1])
    integer_gaps = np.diff(support)
    adjacent_gaps = np.log1p(integer_gaps/support[:-1])
    nearest_gaps = np.minimum(np.r_[np.inf, adjacent_gaps],
                              np.r_[adjacent_gaps, np.inf])
    assert np.all(nearest_gaps > 0)
    squares = coefficients*coefficients
    G = float(np.sum(squares/nearest_gaps))
    B0 = float(np.sum(squares))
    B1 = float(np.sum(support*squares))
    # Finite numerical sanity checks, not interval-certified enclosures.
    assert np.isclose(np.sum(coefficients), np.sum(weights)**2, rtol=2e-14)
    assert 0 < G <= 2*B1*(1+1e-14)
    return {"support": support, "coefficients": coefficients, "G": G,
            "B0": B0, "B1": B1,
            "min_integer_gap": int(np.min(integer_gaps)),
            "max_integer_gap": int(np.max(integer_gaps))}


def independent_mp_check(Y, N, floating):
    """Independent small-case coefficients and product-aggregation algorithm."""
    assert Y == 16 and N <= 32
    terms = []
    for number in range(2, N+1):
        lam = von_mangoldt_mp(number)
        if lam:
            weight = (lam*mp.power(number, -mp.mpf(".25"))
                      *mp.exp(-mp.mpf(number)/Y))
            terms.append((number, weight))
    by_product = {}
    for left, left_weight in terms:
        for right, right_weight in terms:
            product = left*right
            by_product[product] = (by_product.get(product, mp.mpf(0))
                                   + left_weight*right_weight)
    keys = sorted(by_product)
    assert keys == [int(k) for k in floating["support"]]
    summands = []
    for index, key in enumerate(keys):
        gaps = []
        if index:
            gaps.append(mp.log(mp.mpf(key)/keys[index-1]))
        if index+1 < len(keys):
            gaps.append(mp.log(mp.mpf(keys[index+1])/key))
        summands.append(by_product[key]**2/min(gaps))
    Gmp = mp.fsum(summands)
    ratio_mp = Gmp/(Y**3*mp.log(Y))
    relative_error = abs(mp.mpf(str(floating["G"]))-Gmp)/Gmp
    coefficient_error = max(
        abs(mp.mpf(str(value))-by_product[int(key)])/by_product[int(key)]
        for key, value in zip(floating["support"], floating["coefficients"]))
    mass_identity_error = abs(mp.fsum(by_product.values())
                              - mp.fsum(weight for _, weight in terms)**2)
    assert relative_error < mp.mpf("1e-12")
    assert coefficient_error < mp.mpf("1e-12")
    assert mass_identity_error < mp.mpf("1e-45")
    return ratio_mp, relative_error, coefficient_error, mass_identity_error


def main():
    started = time.perf_counter()
    mp.mp.dps = 50
    n_all, lam_all = prime_power_ledger(2048)
    print("[E] bounded actual product-gap probe; sigma=.25")
    print(f"numpy={np.__version__}; mpmath={mp.__version__}; mp_dps=50; "
          "sieve_limit=2048; integer_product_cap=4194304")
    print("Product keys and pair membership use exact integers. Coefficients, "
          "logarithmic gaps, and maximum-mass selections are not certified.")
    print("m,Y,N,cutoff_kind,prime_powers,distinct_products,"
          "G_over_Y3_logY,B1_over_Y3_logY2,G_over_B1,"
          "min_integer_gap,max_integer_gap")
    high_checks = []
    cases = 0
    for m in (4, 6, 8, 10):
        Y = 2**m
        L = math.log(Y)
        end = int(np.searchsorted(n_all, 2*Y, side="right"))
        n_window, lam_window = n_all[:end], lam_all[:end]
        candidates = candidate_cutoffs(n_window, Y)
        masses = float_masses(n_window, lam_window, Y, candidates)
        selected_N = int(candidates[int(np.argmax(np.abs(masses)))])
        for N in sorted(set((selected_N, 2*Y))):
            count = int(np.searchsorted(n_window, N, side="right"))
            result = gap_energy_float(n_window[:count], lam_window[:count], Y)
            kind = "float_max_mass" if N == selected_N else "2Y"
            if selected_N == 2*Y:
                kind = "float_max_mass_and_2Y"
            print(f"{m},{Y},{N},{kind},{count},{len(result['support'])},"
                  f"{result['G']/(Y**3*L):.14g},"
                  f"{result['B1']/(Y**3*L**2):.14g},"
                  f"{result['G']/result['B1']:.14g},"
                  f"{result['min_integer_gap']},{result['max_integer_gap']}")
            if m == 4:
                high_checks.append((Y, N, independent_mp_check(Y, N, result)))
            cases += 1
    print("Independent MP50 checks: Y,N,G_over_Y3_logY,"
          "relative_G_error,max_relative_coefficient_error,"
          "product_coefficient_mass_identity_residual")
    for Y, N, check in high_checks:
        ratio, relative, coefficient, identity = check
        print(f"{Y},{N},{mp.nstr(ratio, 28)},{mp.nstr(relative, 7)},"
              f"{mp.nstr(coefficient, 7)},{mp.nstr(identity, 7)}")
    assert cases == 8 and len(high_checks) == 2
    print(f"PASS {cases} bounded gap computations and {len(high_checks)} "
          f"independent MP50 checks; elapsed_seconds={time.perf_counter()-started:.3f}")
    print("The uniform logarithmic saving (G) remains OPEN. These finite "
          "samples neither prove an asymptotic bound nor certify a full response.")


if __name__ == "__main__":
    main()

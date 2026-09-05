#!/usr/bin/env python3
"""[E] Bounded weighted localization of the actual product-gap budget.

Run: python -B scripts/product_gap_localization_probe.py
Optional: --max-m 12 adds Y=4096; the default ends at Y=1024.
Default H=ceil(log(Y)**2) matches note 273; --h-power 1 reproduces
the first exploratory H=ceil(log(Y)) ledger.

Use sigma=1/4, Y=16,64,256,1024, and N=2Y or a newly computed floating
maximum-mass candidate. Products and representation flags use exact integer
keys. A product is exceptional if ANY representation uses a composite
prime power. G itself always uses the full support's nearest LOG gap.
Partitions use nearest INTEGER gap d<=log(Y), not the log-nearest neighbor's
integer distance. The near-pair ledger uses H=ceil(log(Y)**h_power):

 E_H = sum_k k*b_k**2 * sum_(0<|l-k|<=H, l in support) 1/|l-k|.

The general bound G<=B0+B1/H+E_H follows from
1/delta_k <= 1+k/d_k. The additional bound G<=2*B1/H+2*E_H is checked
for these actual supports, which have d_k<=k. Bounds and partitions are
evaluated numerically, not interval-certified. The two Y=16 cases also use
MP50 coefficients, independent trial factorization/dictionary aggregation,
and an independent all-pairs Fraction near-neighbor ledger.

No asymptotic gap estimate, certified maximum, or full response is proved
by these experiments. No files are written or dependencies installed.
"""

import argparse
from fractions import Fraction
import math
import sys
import time

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np

from abel_mass_discrepancy_probe import prime_power_ledger
from dyadic_max_mass_cutoff_probe import candidate_cutoffs, float_masses
from dyadic_max_mass_cutoff_probe import recover_integer_bases
from prime_jump_cutoff_probe import is_prime, von_mangoldt_mp


def aggregate(n, lam, bases, Y):
    weights = lam*np.exp(-.25*np.log(n)-n/Y)
    products = (n[:, None]*n[None, :]).ravel()
    pair_weights = (weights[:, None]*weights[None, :]).ravel()
    pure = n == bases
    pure_pairs = (pure[:, None] & pure[None, :]).ravel()
    support, inverse = np.unique(products, return_inverse=True)
    coefficients = np.bincount(inverse, weights=pair_weights)
    has_pure = np.zeros(len(support), dtype=bool)
    has_exception = np.zeros(len(support), dtype=bool)
    has_pure[inverse[pure_pairs]] = True
    has_exception[inverse[~pure_pairs]] = True
    # A product of two primes cannot also have a representation of total
    # prime-factor multiplicity >=3. This is checked on the exact pair flags.
    assert np.all(has_pure | has_exception)
    assert not np.any(has_pure & has_exception)
    assert np.isclose(np.sum(coefficients), np.sum(weights)**2, rtol=2e-14)
    return support, coefficients, has_exception


def near_pair_reciprocals(support, H):
    """Sparse bounded-offset search; no quadratic support-pair matrix."""
    reciprocal_sum = np.zeros(len(support), dtype=float)
    unordered_pairs = 0
    for offset in range(1, H+1):
        target = support+offset
        positions = np.searchsorted(support, target)
        left = np.flatnonzero(positions < len(support))
        left = left[support[positions[left]] == target[left]]
        right = positions[left]
        reciprocal_sum[left] += 1.0/offset
        reciprocal_sum[right] += 1.0/offset
        unordered_pairs += len(left)
    return reciprocal_sum, unordered_pairs


def localize(support, coefficients, exceptional, Y, h_power):
    L, H = math.log(Y), math.ceil(math.log(Y)**h_power)
    gaps = np.diff(support)
    sentinel = np.iinfo(np.int64).max
    left_integer = np.r_[sentinel, gaps]
    right_integer = np.r_[gaps, sentinel]
    d = np.minimum(left_integer, right_integer)
    adjacent_log = np.log1p(gaps/support[:-1])
    left_log, right_log = np.r_[np.inf, adjacent_log], np.r_[adjacent_log, np.inf]
    delta = np.minimum(left_log, right_log)
    integer_chooses_left = left_integer <= right_integer
    log_chooses_left = left_log <= right_log
    log_neighbor_integer_distance = np.where(log_chooses_left,
                                              left_integer, right_integer)
    integer_neighbor_log_gap = np.where(integer_chooses_left, left_log, right_log)
    squares = coefficients**2
    weighted_squares = support*squares
    g_terms = squares/delta
    reciprocal_sum, pair_count = near_pair_reciprocals(support, H)
    e_terms = weighted_squares*reciprocal_sum
    G, E = float(np.sum(g_terms)), float(np.sum(e_terms))
    B0, B1 = float(np.sum(squares)), float(np.sum(weighted_squares))
    pure_keys = support[~exceptional]
    pure_adjacent = np.log1p(np.diff(pure_keys)/pure_keys[:-1])
    pure_delta = np.minimum(np.r_[np.inf, pure_adjacent],
                            np.r_[pure_adjacent, np.inf])
    pure_terms = squares[~exceptional]/pure_delta
    G_pure = float(np.sum(pure_terms))
    own_exception = float(np.sum(g_terms[exceptional]))
    pollution = float(np.sum(g_terms[~exceptional]-pure_terms))
    polluted_count = int(np.count_nonzero(delta[~exceptional] < pure_delta))
    assert polluted_count <= 2*int(np.count_nonzero(exceptional))
    assert pollution >= -1e-12*G
    assert np.isclose(G, G_pure+own_exception+pollution, rtol=2e-14)
    generic = B0+B1/H+E
    actual_two = 2*B1/H+2*E
    assert np.all(d <= support), "The additional actual-support premise failed"
    # Verify the mathematical pointwise comparisons numerically, separately
    # from the global finite totals. These tolerances are not certificates.
    tolerance = 1+1e-12
    assert np.all(1/delta <= (1+support/d)*tolerance)
    assert np.all(1/delta <= (1+support/H+support*reciprocal_sum)*tolerance)
    assert np.all(1/delta <= (2*support/H+2*support*reciprocal_sum)*tolerance)
    assert G <= generic*tolerance and G <= actual_two*tolerance
    masks = {"near_integer_d_le_L": d <= L,
             "small_product": support <= Y**2/L**4,
             "exceptional_product": exceptional,
             "log_neighbor_integer_distance_le_L": log_neighbor_integer_distance <= L}
    pieces = {}
    for name, mask in masks.items():
        pieces[name] = (float(np.sum(g_terms[mask])), float(np.sum(g_terms[~mask])),
                        float(np.sum(e_terms[mask])), float(np.sum(e_terms[~mask])),
                        int(np.count_nonzero(mask)))
        assert np.isclose(pieces[name][0]+pieces[name][1], G, rtol=2e-14)
        assert np.isclose(pieces[name][2]+pieces[name][3], E, rtol=2e-14)
    return {"G": G, "E": E, "B0": B0, "B1": B1, "H": H,
            "G_pure": G_pure, "own_exception": own_exception,
            "pollution": pollution, "polluted_count": polluted_count,
            "generic": generic, "actual_two": actual_two, "pieces": pieces,
            "pair_count": pair_count, "support": support,
            "coefficients": coefficients, "exceptional": exceptional,
            "reciprocal_sum": reciprocal_sum,
            "weighted_reciprocal_mean": E/B1,
            "unweighted_reciprocal_mean": float(np.mean(reciprocal_sum)),
            "integer_proxy": float(np.sum(weighted_squares/d)),
            "integer_neighbor_G": float(np.sum(squares/integer_neighbor_log_gap)),
            "choice_difference": int(np.count_nonzero(integer_chooses_left != log_chooses_left)),
            "integer_ties": int(np.count_nonzero(left_integer == right_integer)),
            "strict_distance_difference": int(np.count_nonzero(log_neighbor_integer_distance > d))}


def independent_mp_small(Y, N, result):
    """All-pairs rational reciprocal ledger, independent of the offset search."""
    assert Y == 16 and N <= 32
    terms = []
    for number in range(2, N+1):
        lam = von_mangoldt_mp(number)
        if lam:
            w = lam*mp.power(number, -mp.mpf(".25"))*mp.exp(-mp.mpf(number)/Y)
            terms.append((number, w, is_prime(number)))
    by_product, exceptional = {}, {}
    for u, wu, prime_u in terms:
        for v, wv, prime_v in terms:
            key = u*v
            by_product[key] = by_product.get(key, mp.mpf(0))+wu*wv
            exceptional[key] = exceptional.get(key, False) or not (prime_u and prime_v)
    keys = sorted(by_product)
    assert keys == [int(k) for k in result["support"]]
    assert [exceptional[k] for k in keys] == list(result["exceptional"])
    Gmp, Emp, B0mp, B1mp = (mp.mpf(0) for _ in range(4))
    maximum_reciprocal_error = 0.0
    for index, key in enumerate(keys):
        near_fraction = sum((Fraction(1, abs(other-key)) for other in keys
                             if 0 < abs(other-key) <= result["H"]), Fraction(0))
        reciprocal_mp = mp.mpf(near_fraction.numerator)/near_fraction.denominator
        maximum_reciprocal_error = max(maximum_reciprocal_error,
            abs(float(near_fraction)-result["reciprocal_sum"][index]))
        log_gaps = []
        if index:
            log_gaps.append(mp.log(mp.mpf(key)/keys[index-1]))
        if index+1 < len(keys):
            log_gaps.append(mp.log(mp.mpf(keys[index+1])/key))
        square = by_product[key]**2
        Gmp += square/min(log_gaps)
        Emp += key*square*reciprocal_mp
        B0mp += square
        B1mp += key*square
    assert Gmp <= B0mp+B1mp/result["H"]+Emp
    assert Gmp <= 2*B1mp/result["H"]+2*Emp
    error_g = abs(mp.mpf(str(result["G"]))-Gmp)/Gmp
    error_e = abs(mp.mpf(str(result["E"]))-Emp)/Emp
    assert error_g < mp.mpf("1e-12") and error_e < mp.mpf("1e-12")
    assert maximum_reciprocal_error < 1e-14
    scale = Y**3*mp.log(Y)
    return Gmp/scale, Emp/scale, error_g, error_e, maximum_reciprocal_error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=10, choices=(10, 12))
    parser.add_argument("--h-power", type=int, default=2, choices=(1, 2))
    args = parser.parse_args()
    started = time.perf_counter()
    mp.mp.dps = 50
    limit = 2**(args.max_m+1)
    n_all, lam_all = prime_power_ledger(limit)
    bases_all = recover_integer_bases(n_all, lam_all)
    print("[E] actual weighted product-gap localization; sigma=.25")
    print(f"sieve_limit={limit}; max_ordered_product_pairs={len(n_all)**2}; "
          f"integer_product_cap={limit**2}; numpy={np.__version__}; mpmath={mp.__version__}")
    print(f"Near G partitions use d<=L; E_H uses integer H=ceil(L**{args.h_power}). "
          "G always uses the full support's nearest log gap, including exceptional neighbors.")
    print("m,Y,N,kind,H,products,G_over_Y3L,E_H_over_Y3L,B1_over_H_Y3L,"
          "B0_over_Y3L,G_over_generic_bound,G_over_actual_2_bound,"
          "weighted_reciprocal_mean,unweighted_reciprocal_mean,near_unordered_pairs,"
          "integer_proxy_over_G,integer_neighbor_G_over_G,neighbor_choice_differences,"
          "integer_neighbor_ties,strict_neighbor_distance_differences,"
          "G_over_Y3_log2L,pure_support_G_over_Y3L,"
          "exception_own_G_over_Y3L,exception_pollution_G_over_Y3L,polluted_pure_count")
    rows, checks = [], []
    for m in (4, 6, 8, 10, 12):
        if m > args.max_m:
            continue
        Y = 2**m
        end = int(np.searchsorted(n_all, 2*Y, side="right"))
        n, lam, bases = n_all[:end], lam_all[:end], bases_all[:end]
        candidates = candidate_cutoffs(n, Y)
        masses = float_masses(n, lam, Y, candidates)
        selected = int(candidates[int(np.argmax(np.abs(masses)))])
        for N in sorted(set((selected, 2*Y))):
            count = int(np.searchsorted(n, N, side="right"))
            support, coefficients, exceptional = aggregate(n[:count], lam[:count], bases[:count], Y)
            result = localize(support, coefficients, exceptional, Y, args.h_power)
            scale = Y**3*math.log(Y)
            kind = "float_max_mass" if N == selected else "2Y"
            print(f"{m},{Y},{N},{kind},{result['H']},{len(support)},"
                  f"{result['G']/scale:.13g},{result['E']/scale:.13g},"
                  f"{result['B1']/(result['H']*scale):.13g},{result['B0']/scale:.9g},"
                  f"{result['G']/result['generic']:.9g},{result['G']/result['actual_two']:.9g},"
                  f"{result['weighted_reciprocal_mean']:.9g},{result['unweighted_reciprocal_mean']:.9g},"
                  f"{result['pair_count']},{result['integer_proxy']/result['G']:.9g},"
                  f"{result['integer_neighbor_G']/result['G']:.9g},"
                  f"{result['choice_difference']},{result['integer_ties']},"
                  f"{result['strict_distance_difference']},"
                  f"{result['G']/(Y**3*math.log(2*math.log(Y))):.12g},"
                  f"{result['G_pure']/scale:.12g},{result['own_exception']/scale:.12g},"
                  f"{result['pollution']/scale:.12g},{result['polluted_count']}", flush=True)
            rows.append((m, Y, N, result['pieces'], scale))
            if m == 4:
                checks.append((Y, N, independent_mp_small(Y, N, result)))
    print("Partitions, all normalized by Y^3*L: m,Y,N,mask,mask_count,"
          "G_inside,G_outside,E_H_inside,E_H_outside")
    for m, Y, N, pieces, scale in rows:
        for name, (gin, gout, ein, eout, count) in pieces.items():
            print(f"{m},{Y},{N},{name},{count},{gin/scale:.12g},{gout/scale:.12g},"
                  f"{ein/scale:.12g},{eout/scale:.12g}")
    print("Independent MP50/Fraction checks: Y,N,G_over_Y3L,E_H_over_Y3L,"
          "relative_G_error,relative_E_H_error,max_near_reciprocal_error")
    for Y, N, (g, e, rg, re, near_error) in checks:
        print(f"{Y},{N},{mp.nstr(g, 25)},{mp.nstr(e, 25)},"
              f"{mp.nstr(rg, 6)},{mp.nstr(re, 6)},{near_error:.6g}")
    print(f"PASS {len(rows)} bounded localizations and {len(checks)} independent checks; "
          f"elapsed_seconds={time.perf_counter()-started:.3f}")
    print("Unweighted support density does not replace the actual k*b_k^2 near-pair weights. "
          "No cutoff is certified optimal; no asymptotic saving or full response is certified.")


if __name__ == "__main__":
    main()

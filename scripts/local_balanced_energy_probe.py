#!/usr/bin/env python3
"""[E] Bounded actual local Abel windows, sigma=1/4, m=6,10,14,18.

Run: python -B scripts/local_balanced_energy_probe.py

The two requested widths L/8 and min(log L,L/8) are deduplicated. Source
primitives start at the window's left endpoint; the continuum mass uses
50-digit incomplete gamma. NumPy coefficient arithmetic is not certified.
The smallest case is checked independently by trial factorization and
high-precision adaptive integration of the analytic continuum primitive.
No E2 computation, asymptotic theorem, or file output is performed.
"""

import math
import sys

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

from abel_mass_discrepancy_probe import (
    continuum_mass,
    integrated_lagrange_matrix,
    prime_power_ledger,
)


def cutoff(m):
    return int(mp.floor(mp.mpf(2)**m * (m * mp.log(2))**2))


def beta_mass(Y, left, right, a=mp.mpf("0.75")):
    return mp.power(Y, a) * mp.gammainc(a, left / Y, right / Y)


def local_energy(n, weights, Y, left, right, A, B, order):
    """Piecewise Gaussian energy; both local cumulative sources start at zero."""
    edges = np.unique(np.concatenate(([float(left)], n, [float(right)])))
    log_edges = np.log(edges)
    prefix = np.concatenate(([np.longdouble(0)],
                             np.cumsum(weights, dtype=np.longdouble)))
    # Include a possible atom at a left endpoint before the following interval.
    prime_cdf = prefix[np.searchsorted(n, edges[:-1], side="right")]
    nodes, gauss_weights = leggauss(order)
    integration = integrated_lagrange_matrix(nodes)
    ratio = np.longdouble(A) / np.longdouble(B)
    beta_before, energy = np.longdouble(0), np.longdouble(0)
    for begin in range(0, len(edges) - 1, 65536):
        end = min(begin + 65536, len(edges) - 1)
        widths = np.diff(log_edges[begin:end + 1])
        midpoints = (log_edges[begin:end] + log_edges[begin + 1:end + 1]) / 2
        nodes_local = midpoints[:, None] + widths[:, None] * nodes[None, :] / 2
        density = np.exp(.75 * nodes_local - np.exp(nodes_local) / Y)
        beta_intervals = widths / 2 * (density @ gauss_weights)
        beta_left = beta_before + np.concatenate((
            [np.longdouble(0)], np.cumsum(beta_intervals[:-1], dtype=np.longdouble)))
        partial = widths[:, None] / 2 * (density @ integration.T)
        primitive = prime_cdf[begin:end, None] - ratio * (
            beta_left[:, None] + partial)
        energy += np.sum(widths / 2 * (primitive**2 @ gauss_weights),
                         dtype=np.longdouble)
        beta_before += np.sum(beta_intervals, dtype=np.longdouble)
    balance_residual = np.longdouble(A) - ratio * beta_before
    return energy, beta_before, balance_residual


def trial_von_mangoldt(n):
    """Independent small-case ledger from trial division, evaluated by mpmath."""
    for prime in range(2, math.isqrt(n) + 1):
        if n % prime == 0:
            remainder = n
            while remainder % prime == 0:
                remainder //= prime
            return mp.log(prime) if remainder == 1 else mp.mpf(0)
    return mp.log(n) if n >= 2 else mp.mpf(0)


def independent_small_case(Y, left, right, n_reference):
    ledger = []
    for n in range(int(mp.ceil(left)), int(mp.floor(right)) + 1):
        lam = trial_von_mangoldt(n)
        if lam:
            ledger.append((n, lam * mp.power(n, mp.mpf("-.25"))
                            * mp.exp(-mp.mpf(n) / Y)))
    assert [n for n, _ in ledger] == [int(n) for n in n_reference]
    A = mp.fsum(weight for _, weight in ledger)
    B = beta_mass(Y, left, right)
    ratio = A / B
    first = mp.fsum(weight * mp.log(n) for n, weight in ledger) - ratio * mp.diff(
        lambda a: beta_mass(Y, left, right, a), mp.mpf(".75"))
    boundaries = sorted({left, right} | {mp.mpf(n) for n, _ in ledger})
    energy = mp.mpf(0)
    for xleft, xright in zip(boundaries, boundaries[1:]):
        cumulative = mp.fsum(weight for n, weight in ledger if n <= xleft)
        def integrand(u):
            continuum_primitive = beta_mass(Y, left, mp.exp(u))
            return (cumulative - ratio * continuum_primitive)**2
        energy += mp.quad(integrand, [mp.log(xleft), mp.log(xright)])
    return A, B, first, energy, A - ratio * B


def main():
    mp.mp.dps = 50
    m_values = (6, 10, 14, 18)
    limit = cutoff(max(m_values))
    assert limit <= 41_000_000
    all_n, all_lambda = prime_power_ledger(limit)
    print("[E] actual local Abel probe: sigma=.25; N=floor(Y log^2Y)")
    print(f"sieve_limit={limit}; total_prime_power_terms={len(all_n)}; "
          f"longdouble_explicit_mantissa_bits={np.finfo(np.longdouble).nmant}")
    print("All widths satisfy 0<H<L/6. Ratios use local MH, not full-source M.")
    print("Floating-point and quadrature results are not interval-certified.")
    print("m,width_labels,H,local_prime_powers,M_full,MH,MH_over_M,"
          "E1H_order6,E1H_order10,E1H_over_MH2_sqrtLH,"
          "first_moment_balanced,relative_order_difference,"
          "beta_mass_quadrature_error,balance_residual")
    smallest = None
    window_count = 0
    for m in m_values:
        Y, N = 2**m, cutoff(m)
        L = m * mp.log(2)
        cutoff_count = np.searchsorted(all_n, N, side="right")
        full_n, full_lambda = all_n[:cutoff_count], all_lambda[:cutoff_count]
        full_weights = full_lambda * np.exp(-.25 * np.log(full_n) - full_n / Y)
        full_A = np.sum(full_weights, dtype=np.longdouble)
        full_B = np.longdouble(str(continuum_mass(.25, Y, N)))
        full_M = full_A - full_B
        widths = {}
        for name, H in (("L/8", L / 8), ("min(logL,L/8)", min(mp.log(L), L / 8))):
            widths.setdefault(H, []).append(name)
        for H, labels in widths.items():
            window_count += 1
            assert 0 < H < L / 6
            left, right = max(mp.mpf(1), mp.exp(L-H)), min(mp.mpf(N), mp.exp(L+H))
            lower = np.searchsorted(all_n, int(mp.ceil(left)), side="left")
            upper = np.searchsorted(all_n, int(mp.floor(right)), side="right")
            n, lam = all_n[lower:upper], all_lambda[lower:upper]
            weights = lam * np.exp(-.25 * np.log(n) - n / Y)
            A = np.sum(weights, dtype=np.longdouble)
            Bmp = beta_mass(Y, left, right)
            B = np.longdouble(str(Bmp))
            assert A > 0 and B > 0
            MH = A - B
            A1 = np.sum(weights * np.log(n), dtype=np.longdouble)
            B1 = np.longdouble(str(mp.diff(
                lambda a: beta_mass(Y, left, right, a), mp.mpf(".75"))))
            first = A1 - (A/B) * B1
            e6, _, _ = local_energy(n, weights, Y, left, right, A, B, 6)
            e10, beta10, residual10 = local_energy(n, weights, Y, left, right, A, B, 10)
            relative = abs(e6-e10) / max(abs(e10), np.longdouble(1e-30))
            ratio = (e10 / (MH**2 * np.longdouble(str(mp.sqrt(L*H)))))
            print(f"{m},{'='.join(labels)},{float(H):.12g},{len(n)},"
                  f"{full_M:.14g},{MH:.14g},{MH/full_M:.14g},"
                  f"{e6:.14g},{e10:.14g},{ratio:.14g},{first:.14g},"
                  f"{relative:.6g},{abs(beta10-B):.6g},{residual10:.6g}")
            if smallest is None:
                smallest = (Y, left, right, n.copy(), A, B, first, e10)
    Y, left, right, n, A, B, first, e10 = smallest
    a_mp, b_mp, first_mp, energy_mp, balance_mp = independent_small_case(
        Y, left, right, n)
    discrepancies = {
        "A_absolute_difference": abs(mp.mpf(str(A)) - a_mp),
        "B_absolute_difference": abs(mp.mpf(str(B)) - b_mp),
        "first_absolute_difference": abs(mp.mpf(str(first)) - first_mp),
        "E1_relative_difference": abs(mp.mpf(str(e10)) - energy_mp) / energy_mp,
    }
    assert discrepancies["E1_relative_difference"] < mp.mpf("1e-10")
    assert discrepancies["first_absolute_difference"] < mp.mpf("1e-10")
    print(f"Independent smallest-case PASS: trial ledger and analytic "
          f"primitive/adaptive integration; unique_windows={window_count}")
    print(f"Independent E1H={mp.nstr(energy_mp, 24)}; "
          f"first_moment={mp.nstr(first_mp, 24)}; balanced_mass_residual={mp.nstr(balance_mp, 5)}")
    for name, value in discrepancies.items():
        print(f"{name}={mp.nstr(value, 8)}")
    print("These bounded samples prove no asymptotic local budget or signed-transfer statement.")


if __name__ == "__main__":
    main()

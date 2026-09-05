#!/usr/bin/env python3
"""[E] Bounded true-response and double-discrepancy shell comparison.

Run: python -B scripts/midband_double_discrepancy_probe.py
Optional: --max-m 12 (adds Y=4096 and can be substantially slower).
Fixed sigma=1/4, beta=3/8; Y=16,64,256,1024 by default. Each N is
the floating finite-window maximum of note 271, NOT a certified maximum
or a member of the new record-guarded cofinal sequence of note 275.

For U=sqrt(log Y), log Y, T*/2 integrate the positive-frequency shell
[U,2U], with factor 1/pi accounting for its negative reflection.
T*=Y sqrt(log(2 log Y)/log Y). The top shell [T*/2,T*] is a CONTROL:
note 274 already closes fixed multiples of this tail on large-mass
sequences. It is not a new open shell. Samples at U~log Y illustrate
an interior scale, but cannot establish the theoretical sequence budget.

The actual channels p<=0, c>=0 use cos-1=-2sin^2. Thus r=p+c equals
Re F-Re C-M, retaining the mass term and both cutoffs x=1 and x=N.
For S_H(xi)=integral_0^logN H(u) sin(xi u)du,
r=M(cos(xi logN)-1)+xi S_H. The double-error spectrum
xi^2 |S_H|^4 is evaluated via this exact identity, not by an arbitrary
Bessel bound. Small MP50 samples additionally integrate H directly.

All outputs are [E]. Gaussian-order differences are NOT certified errors.
The reported min(c/B) is only a minimum over nodes plus shell endpoints.
No files, full J4, omitted-tail certification, asymptotic conclusion,
or RH claim are produced. SciPy is an optional local probe dependency.
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

from abel_mass_discrepancy_probe import prime_power_ledger
from prime_jump_full_response_probe import (
    continuum_brownian_energy_mp,
    prime_brownian_energy,
)
from quartic_signed_frequency_probe import (
    centered_transform,
    composite_gauss,
    continuum_rule,
    exact_continuum_transform,
)
from record_path_low_frequency_probe import (
    SIGMA,
    candidate_maximum,
    ell,
    trial_lambda,
    weighted_prefix,
)


def shell_integrals(Y, N, lags, coefficients, mass, B, shells, inner, outer):
    """Four unnormalized energies and sampled continuum-channel minima."""
    maximum = max(2 * U for _, U in shells)
    rule = continuum_rule(Y, 0.0, math.log(N), maximum, inner)
    results = {}
    for label, U in shells:
        frequencies, quadrature = composite_gauss(U, 2 * U, 0.25, outer)
        totals = np.zeros(4, dtype=np.longdouble)
        sampled_min = float(np.min(
            -centered_transform(np.array([U, 2 * U]), *rule) / B
        ))
        for begin in range(0, len(frequencies), 128):
            xi = frequencies[begin:begin + 128]
            qw = quadrature[begin:begin + 128]
            p = centered_transform(xi, lags, coefficients)
            c = -centered_transform(xi, *rule)
            assert np.all(p <= 0) and np.all(c >= 0)
            r = p + c
            endpoint = -2 * mass * np.sin(xi * math.log(N) / 2)**2
            double_error = r - endpoint  # exactly xi * S_H(xi)
            common = qw / (np.pi * xi**2)
            fourth, double_fourth = r**4, double_error**4
            channels = p**2 + c**2
            pieces = (fourth, double_fourth,
                      fourth * channels, double_fourth * channels)
            for index, piece in enumerate(pieces):
                totals[index] += np.sum(common * piece, dtype=np.longdouble)
            sampled_min = min(sampled_min, float(np.min(c / B)))
        results[label] = (totals, sampled_min, len(frequencies))
    return results


def continuum_sample_check(Y, N, shells, order=18):
    maximum = max(2 * U for _, U in shells)
    rule = continuum_rule(Y, 0.0, math.log(N), maximum, order)
    frequencies = np.array(sorted({x for _, U in shells for x in (U, 1.5 * U, 2 * U)}))
    floating = -centered_transform(frequencies, *rule)
    error = mp.mpf(0)
    for xi, value in zip(frequencies, floating):
        exact = -exact_continuum_transform(Y, mp.mpf(1), mp.mpf(N), xi)
        error = max(error, abs(mp.mpf(str(value)) - exact) / (1 + abs(exact)))
    assert error < mp.mpf("1e-9")
    return error, len(frequencies)


def independent_small_shell(Y, N, mass, Dp, Dc, U, fine):
    """Independent trial division, MP50 adaptive full FIRST shell, path check."""
    mp.mp.dps = 50
    quarter, a = mp.mpf(1) / 4, mp.mpf(3) / 4
    lam = [trial_lambda(n) for n in range(2 * Y + 1)]
    prefix = [mp.mpf(0)]
    ledger = []
    for n in range(1, 2 * Y + 1):
        weight = lam[n] * mp.power(n, -quarter) * mp.exp(-mp.mpf(n) / Y)
        prefix.append(prefix[-1] + weight)
        if weight and n <= N:
            ledger.append((mp.log(n), weight))

    def continuous(x):
        return mp.power(Y, a) * mp.gammainc(a, mp.mpf(1) / Y, x / Y)

    masses = {n: prefix[n] - continuous(mp.mpf(n)) for n in range(Y, 2 * Y + 1)}
    assert max(masses, key=lambda n: abs(masses[n])) == N
    M = masses[N]
    dp_exact = mp.fsum(w * v * min(u, t) for u, w in ledger for t, v in ledger) / 2
    assert abs(dp_exact - Dp) / (1 + dp_exact) < mp.mpf("1e-12")
    assert abs(M - mass) < mp.mpf("1e-11")
    tau = mp.log(N)
    # Match the floating shell endpoints exactly; endpoint rounding is not
    # silently confused with integration error.
    lo, hi = mp.mpf(U), mp.mpf(2 * U)
    cache = {}

    def integrands(xi):
        if xi not in cache:
            p = -2 * mp.fsum(w * mp.sin(xi * u / 2)**2 for u, w in ledger)
            c = -exact_continuum_transform(Y, mp.mpf(1), mp.mpf(N), xi)
            r = p + c
            d = r + 2 * M * mp.sin(xi * tau / 2)**2
            denominator = mp.pi * xi**2
            cache[xi] = (r**4 / denominator, d**4 / denominator,
                         r**4 * (p*p + c*c) / denominator,
                         d**4 * (p*p + c*c) / denominator)
        return cache[xi]

    partition = [lo + (hi - lo) * j / 4 for j in range(5)]
    exact = [mp.quad(lambda xi: integrands(xi)[j], partition) for j in range(4)]
    errors = [abs(mp.mpf(str(fine[j])) - exact[j]) / abs(exact[j]) for j in range(4)]
    assert max(errors) < mp.mpf("1e-9")
    print("MP50 independent first shell: relative errors "
          "(quartic,double,actual_response,double_response)="
          + ",".join(mp.nstr(error, 8) for error in errors))
    print("MP50 first-shell normalized: Q/(M^4 L)="
          + mp.nstr(exact[0] / (M**4 * mp.log(Y)), 18)
          + "; actual_response/(M^4 D)="
          + mp.nstr(exact[2] / (M**4 * (dp_exact + Dc)), 18))
    identity_error = mp.mpf(0)
    for xi in (lo, (lo + hi) / 2, hi):
        sine = mp.fsum(mp.quad(
            lambda x: (prefix[n] - continuous(x)) * mp.sin(xi * mp.log(x)) / x,
            [n, n + 1],
        ) for n in range(1, N))
        p = -2 * mp.fsum(w * mp.sin(xi * u / 2)**2 for u, w in ledger)
        c = -exact_continuum_transform(Y, mp.mpf(1), mp.mpf(N), xi)
        reconstructed = -2 * M * mp.sin(xi * tau / 2)**2 + xi * sine
        identity_error = max(identity_error, abs(p + c - reconstructed))
    assert identity_error < mp.mpf("1e-38")
    print("MP50 direct piecewise H sine integral: largest identity error="
          + mp.nstr(identity_error, 8))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, choices=(4, 6, 8, 10, 12), default=10)
    args = parser.parse_args()
    started = time.perf_counter()
    mp.mp.dps = 50
    numbers, lambdas = prime_power_ledger(2**(args.max_m + 1))
    print("[E] sigma=1/4, beta=3/8; floating 271 window maxima, NOT record/cofinal points.")
    print(f"numpy={np.__version__}; scipy={scipy.__version__}; mpmath={mp.__version__}")
    print("Shells [U,2U] + reflection: sqrtL, L (interior), Tstar/2 (already-closed tail control).")
    print("Coarse/fine continuum Gauss10/18; frequency Gauss8/12, panel width<=0.25.")
    print("Q=(1/pi)int r^4/xi^2; E=(1/pi)int xi^2|S_H|^4; "
          "response inserts the ACTUAL p^2+c^2.")
    print("m,Y,N,M,absM_over_large_threshold,D_over_S2L")
    smallest = None
    for m in (value for value in (4, 6, 8, 10, 12) if value <= args.max_m):
        Y = 2**m
        mask = numbers <= 2 * Y
        prefix = weighted_prefix(2 * Y, numbers[mask], lambdas[mask], Y)
        N, selected_mass, _ = candidate_maximum(Y, numbers, prefix)
        mask = numbers <= N
        n, lam = numbers[mask], lambdas[mask]
        lags = np.log(n)
        coefficients = lam * np.exp(-SIGMA * lags - n / Y)
        A = np.sum(coefficients, dtype=np.longdouble)
        B = float(mp.power(Y, mp.mpf(".75")) *
                  mp.gammainc(mp.mpf(".75"), mp.mpf(1) / Y, mp.mpf(N) / Y))
        M = float(A - B)
        assert M != 0 and abs(M - selected_mass) < 1e-10
        Dp = prime_brownian_energy(lags, coefficients)
        Dc_mp = continuum_brownian_energy_mp(Y, N)
        D = float(Dp + np.longdouble(str(Dc_mp)))
        L, S = math.log(Y), float(A + B)
        Tstar = Y * math.sqrt(math.log(2 * L) / L)
        shells = [("sqrtL", math.sqrt(L)), ("L", L), ("Tstar/2", Tstar / 2)]
        print(f"{m},{Y},{N},{M:.15g},"
              f"{abs(M)/(Y**(.5-SIGMA)*math.sqrt(ell(Y))):.12g},"
              f"{D/(S*S*L):.12g}", flush=True)
        coarse = shell_integrals(Y, N, lags, coefficients, M, B, shells, 10, 8)
        fine = shell_integrals(Y, N, lags, coefficients, M, B, shells, 18, 12)
        print("m,shell,U,2U,Q_over_M4L,E_over_M4L,actual_over_M4D,"
              "double_actual_over_M4D,sampled_min_c_over_B,max_rule_relative_difference")
        for label, U in shells:
            values, minimum, _ = fine[label]
            low = coarse[label][0]
            differences = np.abs(values - low) / np.maximum(np.abs(values), 1e-30)
            assert np.max(differences) < 1e-7
            normalized = values / np.array([M**4 * L, M**4 * L, M**4 * D, M**4 * D])
            print(f"{m},{label},{U:.12g},{2*U:.12g},"
                  + ",".join(f"{value:.12g}" for value in normalized)
                  + f",{minimum:.12g},{float(np.max(differences)):.6g}", flush=True)
        error, samples = continuum_sample_check(Y, N, shells)
        print(f"continuum MP50 gamma samples,m={m},count={samples},"
              f"largest_scaled_error={mp.nstr(error, 8)}", flush=True)
        if smallest is None:
            smallest = (Y, N, M, Dp, Dc_mp, shells[0][1], fine["sqrtL"][0])
    independent_small_shell(*smallest)
    print(f"PASS finite checks; elapsed_seconds={time.perf_counter()-started:.3f}")
    print("[E] No certified quadrature error, continuum-channel global minimum, "
          "record/cofinal point, asymptotic bound, or full J4 is established.")


if __name__ == "__main__":
    main()

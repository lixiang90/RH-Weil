#!/usr/bin/env python3
"""[E] Fixed first-zero-shaped template versus actual finite Abel responses.

Run: python -B scripts/first_zero_midband_template_probe.py
Default Y=2^8,2^10,2^12,2^14; --max-m 12 shortens the experiment.
For each Y use N=Y, N=2Y, and the floating mass maximizer of note 271.
These are NOT interval-certified maxima or note-275 record/cofinal points.

gamma1=Im(mpmath.zetazero(1)) is a 50-digit NUMERICAL TEMPLATE PARAMETER.
This script does not certify a zero, assume all zeros are on the line,
or claim a complete truncated explicit formula. The predetermined, unfitted
real template is
 z1(xi)=-2 integral_1^N x^(-sigma-1/2) exp(-x/Y) cos(gamma1 log x)
                         [cos(xi log x)-1] dx.
Its coefficient is not fitted to the actual response.

E=[log Y,2 log Y], Z=[gamma1-1.5,gamma1+1.5]. We integrate their disjoint
pieces, then report E, Z, E intersection Z, and E minus Z without double
counting. Positive-frequency integrals use 1/pi for the reflected band.
Raw Q, Q/Y, and mass-relative energies distinguish a changing numerator
from small-M denominator effects. The range stops at Y=2^14 so the E
upper endpoint is below the next usual low-zero comparison region.

The actual r=p+c=Re F-Re C-M keeps both cutoffs and the central mass.
With v=r-z1, its quartic actual-channel energy is expanded into the FIVE
SIGNED terms z1^4,4z1^3v,6z1^2v^2,4z1v^3,v^4. Their numerical sum is
checked against the independently accumulated r^4 energy. The Holder
bound is a diagnostic for this fixed decomposition, NOT a Type I/II
or arbitrary-coefficient Bessel estimate.

All results are [E]. Gaussian-order comparisons, sampled peak locations,
and MP50 comparisons are not interval certificates or asymptotic results.
No full J4, files, PDF, CI modification, or omitted-tail claim is produced.
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


def template_rule(Y, N, maximum, inner, gamma1):
    lags, coefficients = continuum_rule(Y, 0.0, math.log(N), maximum, inner)
    template_coefficients = coefficients * (
        -2 * np.exp(-0.5 * lags) * np.cos(gamma1 * lags)
    )
    return (lags, coefficients), (lags, template_coefficients)


def integrals(Y, N, lags, coefficients, gamma1, inner, outer):
    """Seven energies: bare Q, true weighted fourth, then five signed pieces."""
    L = math.log(Y)
    E, Z = (L, 2 * L), (gamma1 - 1.5, gamma1 + 1.5)
    boundaries = sorted(set(E + Z))
    continuous, template = template_rule(Y, N, boundaries[-1], inner, gamma1)
    bands = {
        name: {"values": np.zeros(7, dtype=np.longdouble), "peak": (0.0, math.nan)}
        for name in ("E", "Z", "intersection", "outside")
    }
    for left, right in zip(boundaries[:-1], boundaries[1:]):
        middle = (left + right) / 2
        inside_e, inside_z = E[0] < middle < E[1], Z[0] < middle < Z[1]
        destinations = []
        if inside_e:
            destinations += ["E", "intersection" if inside_z else "outside"]
        if inside_z:
            destinations.append("Z")
        if not destinations:
            continue
        frequencies, quadrature = composite_gauss(left, right, 0.125, outer)
        totals = np.zeros(7, dtype=np.longdouble)
        peak = (0.0, math.nan)
        for begin in range(0, len(frequencies), 128):
            xi, qw = frequencies[begin:begin + 128], quadrature[begin:begin + 128]
            p = centered_transform(xi, lags, coefficients).astype(np.longdouble)
            c = -centered_transform(xi, *continuous).astype(np.longdouble)
            assert np.all(p <= 0) and np.all(c >= 0)
            r = p + c
            z = centered_transform(xi, *template).astype(np.longdouble)
            v = r - z
            base = qw.astype(np.longdouble) / (np.pi * xi.astype(np.longdouble)**2)
            physical = base * (p*p + c*c)
            pieces = (z**4, 4*z**3*v, 6*z*z*v*v, 4*z*v**3, v**4)
            totals[0] += np.sum(base * r**4, dtype=np.longdouble)
            totals[1] += np.sum(physical * r**4, dtype=np.longdouble)
            for index, piece in enumerate(pieces):
                totals[index + 2] += np.sum(physical * piece, dtype=np.longdouble)
            winner = int(np.argmax(np.abs(r)))
            if abs(r[winner]) > peak[0]:
                peak = (float(abs(r[winner])), float(xi[winner]))
        for name in destinations:
            bands[name]["values"] += totals
            if peak[0] > bands[name]["peak"][0]:
                bands[name]["peak"] = peak
    return bands


def exact_template(Y, N, xi, gamma1):
    """Independent MP50 product-to-sum and complex incomplete-gamma formula."""
    exponent = mp.mpf(1) / 2 - mp.mpf(1) / 4

    def kernel(frequency):
        s = exponent + 1j * frequency
        return mp.re(mp.power(Y, s) * mp.gammainc(
            s, mp.mpf(1) / Y, mp.mpf(N) / Y
        ))

    return 2 * kernel(gamma1) - kernel(gamma1 + xi) - kernel(gamma1 - xi)


def sample_checks(Y, N, gamma1_mp, lags, coefficients, independent_prime=False):
    gamma1 = float(gamma1_mp)
    frequencies = np.array([math.log(Y), gamma1, 2 * math.log(Y)])
    continuous, template = template_rule(Y, N, max(frequencies), 18, gamma1)
    values = centered_transform(frequencies, *template)
    max_template = mp.mpf(0)
    max_continuum = mp.mpf(0)
    actual = centered_transform(frequencies, lags, coefficients) - centered_transform(
        frequencies, *continuous
    )
    ledger = []
    if independent_prime:
        for n in range(2, N + 1):
            lam = trial_lambda(n)
            if lam:
                ledger.append((mp.log(n), lam * mp.power(n, -mp.mpf(1)/4)
                               * mp.exp(-mp.mpf(n) / Y)))
    max_actual = mp.mpf(0)
    for index, xi_float in enumerate(frequencies):
        xi = mp.mpf(float(xi_float))
        exact = exact_template(Y, N, xi, gamma1_mp)
        max_template = max(max_template, abs(mp.mpf(float(values[index])) - exact)
                           / (1 + abs(exact)))
        cont_exact = exact_continuum_transform(Y, mp.mpf(1), mp.mpf(N), xi)
        cont_value = centered_transform(np.array([xi_float]), *continuous)[0]
        max_continuum = max(max_continuum, abs(mp.mpf(float(cont_value)) - cont_exact)
                            / (1 + abs(cont_exact)))
        if independent_prime:
            p_exact = -2 * mp.fsum(w * mp.sin(xi * u / 2)**2 for u, w in ledger)
            direct = p_exact - cont_exact
            max_actual = max(max_actual, abs(mp.mpf(float(actual[index])) - direct)
                             / (1 + abs(direct)))
    assert max_template < mp.mpf("1e-9")
    assert max_continuum < mp.mpf("1e-9")
    assert max_actual < mp.mpf("1e-9")
    return max_template, max_continuum, max_actual


def rule_comparison(coarse, fine):
    """Cross terms use their absolute-sum scale, avoiding division by near zero."""
    worst, sum_error = 0.0, 0.0
    for name in fine:
        low, high = coarse[name]["values"], fine[name]["values"]
        if high[1] == 0:  # empty geometric intersection, not a spectral inference
            assert np.all(high == 0)
            continue
        energy_error = max(
            abs(high[index] - low[index]) / max(abs(high[index]), 1e-30)
            for index in (0, 1)
        )
        term_scale = max(np.sum(np.abs(high[2:])), abs(high[1]), 1e-30)
        cross_error = np.max(np.abs(high[2:] - low[2:])) / term_scale
        identity_error = abs(np.sum(high[2:], dtype=np.longdouble) - high[1]) / high[1]
        worst = max(worst, float(energy_error), float(cross_error))
        sum_error = max(sum_error, float(identity_error))
    assert worst < 1e-7
    assert sum_error < 1e-8
    return worst, sum_error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, choices=(8, 10, 12, 14), default=14)
    args = parser.parse_args()
    started = time.perf_counter()
    mp.mp.dps = 50
    gamma1_mp = mp.im(mp.zetazero(1))
    gamma1 = float(gamma1_mp)
    numbers, lambdas = prime_power_ledger(2**(args.max_m + 1))
    print("[E] fixed numerical first-zero-shaped template, not a certified zero "
          "or complete explicit formula; no coefficient fitting.")
    print(f"gamma_parameter_MP50={mp.nstr(gamma1_mp, 45)}")
    print(f"numpy={np.__version__}; scipy={scipy.__version__}; mpmath={mp.__version__}")
    print("sigma=1/4; E=[L,2L], Z=[gamma-1.5,gamma+1.5], reflected bands included.")
    print("Continuum Gauss10/18, frequency Gauss8/12, frequency panels<=1/8.")
    print("m,cutoff,N,M,absM_over_threshold,Q_E,Q_E_minus_Z,Q_Z,Q_Z_over_Y,"
          "J_E_over_mu4,J_EminusZ_over_mu4,J_Z_over_mu4,"
          "fraction_E_response_in_Z,sampled_peak_E,sampled_peak_Z,rule_error")
    cross_rows = []
    max_rule = max_identity = 0.0
    mp_errors = [mp.mpf(0)] * 3
    reached, configurations = 0, 0
    summaries = []
    for m in (value for value in (8, 10, 12, 14) if value <= args.max_m):
        Y = 2**m
        mask = numbers <= 2 * Y
        prefix = weighted_prefix(2 * Y, numbers[mask], lambdas[mask], Y)
        maximum_N, _, _ = candidate_maximum(Y, numbers, prefix)
        for label, N in (("Y", Y), ("2Y", 2 * Y), ("maxM", maximum_N)):
            mask = numbers <= N
            n, lam = numbers[mask], lambdas[mask]
            lags = np.log(n)
            coefficients = lam * np.exp(-SIGMA * lags - n / Y)
            A = np.sum(coefficients, dtype=np.longdouble)
            B_mp = mp.power(Y, mp.mpf(".75")) * mp.gammainc(
                mp.mpf(".75"), mp.mpf(1) / Y, mp.mpf(N) / Y
            )
            M = float(A - np.longdouble(str(B_mp)))
            assert M != 0, "Raw energies remain meaningful, but this case cannot divide by M."
            D = prime_brownian_energy(lags, coefficients) + np.longdouble(
                str(continuum_brownian_energy_mp(Y, N))
            )
            denominator = M**4 * D
            threshold_ratio = abs(M) / (Y**.25 * math.sqrt(ell(Y)))
            reached += threshold_ratio > 1
            configurations += 1
            coarse = integrals(Y, N, lags, coefficients, gamma1, 10, 8)
            fine = integrals(Y, N, lags, coefficients, gamma1, 18, 12)
            error, identity = rule_comparison(coarse, fine)
            max_rule, max_identity = max(max_rule, error), max(max_identity, identity)
            sample = sample_checks(Y, N, gamma1_mp, lags, coefficients,
                                   independent_prime=(m == 8 and label == "maxM"))
            mp_errors = [max(old, new) for old, new in zip(mp_errors, sample)]
            e, z = fine["E"]["values"], fine["Z"]["values"]
            overlap, outside = fine["intersection"]["values"], fine["outside"]["values"]
            assert abs(e[1] - overlap[1] - outside[1]) < 1e-10 * e[1]
            fraction = overlap[1] / e[1]
            print(f"{m},{label},{N},{M:.12g},{threshold_ratio:.8g},"
                  f"{e[0]:.10g},{outside[0]:.10g},{z[0]:.10g},{z[0]/Y:.10g},"
                  f"{e[1]/denominator:.10g},{outside[1]/denominator:.10g},"
                  f"{z[1]/denominator:.10g},{fraction:.8g},"
                  f"{fine['E']['peak'][1]:.8g},{fine['Z']['peak'][1]:.8g},{error:.4g}",
                  flush=True)
            for band in ("E", "Z"):
                values = fine[band]["values"]
                terms = values[2:]
                holder = (terms[0]**.25 + terms[4]**.25)**4
                cross_rows.append((m, label, band, terms / values[1],
                                   holder / values[1],
                                   abs(np.sum(terms) - values[1]) / values[1]))
            if label == "maxM":
                summaries.append((Y, fraction, e[1]/denominator,
                                  outside[1]/denominator, z[1]/denominator))
    print("m,cutoff,band,z4_over_full,4z3v_over_full,6z2v2_over_full,"
          "4zv3_over_full,v4_over_full,Holder_over_full,signed_sum_relative_error")
    for m, label, band, ratios, holder, identity in cross_rows:
        print(f"{m},{label},{band}," + ",".join(f"{value:.9g}" for value in ratios)
              + f",{holder:.9g},{identity:.4g}")
    print(f"SUMMARY finite configurations={configurations}; "
          f"large-mass threshold reached={reached}; none are certified record points.")
    print(f"SUMMARY max Gaussian comparison={max_rule:.6g}; "
          f"max signed-five-term/full relative mismatch={max_identity:.6g}.")
    print("SUMMARY MP50 max scaled errors (template,continuum,independent actual)="
          + ",".join(mp.nstr(value, 7) for value in mp_errors) + ".")
    for Y, fraction, full, outside, zband in summaries:
        print(f"SUMMARY maxM Y={Y}: overlap fraction={fraction:.6g}, "
              f"J_E/mu4={full:.6g}, J_EminusZ/mu4={outside:.6g}, J_Z/mu4={zband:.6g}.")
    print(f"SUMMARY PASS finite checks; elapsed_seconds={time.perf_counter()-started:.3f}.")
    print("SUMMARY [E] Template residual is not certified other-zero error; "
          "no uniform saving, Type I/II estimate, full J4, or asymptotic conclusion.")


if __name__ == "__main__":
    main()

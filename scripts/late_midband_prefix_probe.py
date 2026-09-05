#!/usr/bin/env python3
"""[E] Actual signed early/late Abel responses on a bounded middle band.

Run: python -B scripts/late_midband_prefix_probe.py
Default Y=2^8,2^10,2^12,2^14; --max-m 12 shortens the run.
Fixed sigma=1/4, beta=3/8, h=3, K=floor(N/log(Y)^3).
Use N=Y,2Y,and the floating note-271 mass maximizer. All cutoffs share the
same Y and lag origin. The exceptional Y=N=256 has K=1: its early source
is identically zero, as separately permitted in note 279. It is labelled
degenerate, NOT silently changed to K=2.

The exact split is [1,K] plus (K,N]: an atom at the integer K belongs
ONLY to the early prime source. Both continuum cutoffs and all central
masses are retained. r_full, r_early, r_late are computed from the
actual signed prime-minus-continuum sources, not separate TV majorants.
The reflected band is sqrt(log Y)<=|xi|<=log Y. We report bare Q energies,
the SAME original-M normalized fourth roots, and the actual full/late
channel responses using their respective positive Brownian denominators.
Late lags are not translated to zero.

All selections and Gaussian integrals are finite numerical [E]. None is
claimed to be a note-275 certified record/cofinal point. The epsilon
column is the scale in note 279, not a fitted or certified inequality
constant. The L4 Minkowski check itself requires no arithmetic assumption.
No files, full-frequency J4, PDF, CI changes, or asymptotic claim.
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
    DELTA,
    candidate_maximum,
    ell,
    trial_lambda,
    weighted_prefix,
)


def continuum_mass_mp(Y, left, right):
    a = mp.mpf(3) / 4
    return mp.power(Y, a) * mp.gammainc(a, mp.mpf(left) / Y, mp.mpf(right) / Y)


def continuum_late_energy_mp(Y, K, N):
    """Original-log-lag Brownian energy, including its [0,log K] plateau."""
    if K == 1:
        return continuum_brownian_energy_mp(Y, N)
    lo, hi = mp.log(K), mp.log(N)
    total = continuum_mass_mp(Y, K, N)

    def tail(u):
        return continuum_mass_mp(Y, mp.exp(u), N)

    return (lo * total**2 + mp.quad(lambda u: tail(u)**2,
                                   [lo, (lo + hi) / 2, hi])) / 2


def band_integrals(Y, K, N, lags, coefficients, early_mask, inner, outer):
    L = math.log(Y)
    xi_all, quadrature = composite_gauss(math.sqrt(L), L, .125, outer)
    full_c = continuum_rule(Y, 0., math.log(N), L, inner)
    early_c = continuum_rule(Y, 0., math.log(K), L, inner)
    late_c = continuum_rule(Y, math.log(K), math.log(N), L, inner)
    totals = np.zeros(5, dtype=np.longdouble)  # Qf,Qe,Ql,actual_f,actual_l
    split_error = 0.0
    for begin in range(0, len(xi_all), 128):
        xi, qw = xi_all[begin:begin + 128], quadrature[begin:begin + 128]
        pf = centered_transform(xi, lags, coefficients)
        pe = centered_transform(xi, lags[early_mask], coefficients[early_mask])
        pl = centered_transform(xi, lags[~early_mask], coefficients[~early_mask])
        cf = -centered_transform(xi, *full_c)
        ce = -centered_transform(xi, *early_c)
        cl = -centered_transform(xi, *late_c)
        assert np.all(pf <= 0) and np.all(pe <= 0) and np.all(pl <= 0)
        assert np.all(cf >= 0) and np.all(ce >= 0) and np.all(cl >= 0)
        rf, re, rl = pf + cf, pe + ce, pl + cl
        split_error = max(split_error, float(np.max(
            np.abs(rf - re - rl) / (1 + np.abs(rf) + np.abs(re) + np.abs(rl))
        )))
        base = qw / (np.pi * xi**2)  # both reflected sides
        pieces = (rf**4, re**4, rl**4,
                  rf**4 * (pf*pf + cf*cf), rl**4 * (pl*pl + cl*cl))
        for index, piece in enumerate(pieces):
            totals[index] += np.sum(base * piece, dtype=np.longdouble)
    return totals, split_error


def small_mp50_check(Y, K, N, numbers, lags, coefficients, masses):
    """Independent trial-Lambda and exact MP50 sharp endpoint accounting."""
    quarter = mp.mpf(1) / 4
    ledger = []
    for n in range(2, N + 1):
        lam = trial_lambda(n)
        if lam:
            ledger.append((n, mp.log(n),
                           lam * mp.power(n, -quarter) * mp.exp(-mp.mpf(n) / Y)))
    atom = trial_lambda(K) * mp.power(K, -quarter) * mp.exp(-mp.mpf(K) / Y)
    assert atom > 0, "Chosen small audit must genuinely test a prime-power endpoint."
    ae = mp.fsum(weight for n, _, weight in ledger if n <= K)
    al = mp.fsum(weight for n, _, weight in ledger if n > K)
    af = mp.fsum(weight for _, _, weight in ledger)
    be, bl = continuum_mass_mp(Y, 1, K), continuum_mass_mp(Y, K, N)
    bf = continuum_mass_mp(Y, 1, N)
    assert abs(af - ae - al) < mp.mpf("1e-45")
    assert abs(bf - be - bl) < mp.mpf("1e-45")
    assert abs(mp.fsum(weight for n, _, weight in ledger if n >= K) - al - atom) \
        < mp.mpf("1e-45")
    exact_masses = (af - bf, ae - be, al - bl)
    mass_error = max(abs(mp.mpf(float(value)) - exact)
                     for value, exact in zip(masses, exact_masses))
    assert mass_error < mp.mpf("1e-10")
    frequencies = np.array([math.sqrt(math.log(Y)),
                            (math.sqrt(math.log(Y)) + math.log(Y)) / 2, math.log(Y)])
    rules = (continuum_rule(Y, 0., math.log(N), math.log(Y), 18),
             continuum_rule(Y, 0., math.log(K), math.log(Y), 18),
             continuum_rule(Y, math.log(K), math.log(N), math.log(Y), 18))
    masks = (np.ones(len(lags), dtype=bool), numbers <= K, numbers > K)
    floating = [centered_transform(frequencies, lags[mask], coefficients[mask])
                - centered_transform(frequencies, *rule)
                for mask, rule in zip(masks, rules)]
    max_actual_error, max_split_error = mp.mpf(0), mp.mpf(0)
    for index, xi_float in enumerate(frequencies):
        xi = mp.mpf(float(xi_float))
        exact_values = []
        for part, left, right in (("full", 1, N), ("early", 1, K), ("late", K, N)):
            p = -2 * mp.fsum(weight * mp.sin(xi * lag / 2)**2
                            for n, lag, weight in ledger if left < n <= right)
            c = -exact_continuum_transform(Y, mp.mpf(left), mp.mpf(right), xi)
            exact_values.append(p + c)
        max_split_error = max(max_split_error,
                              abs(exact_values[0] - exact_values[1] - exact_values[2]))
        for row, exact in zip(floating, exact_values):
            max_actual_error = max(max_actual_error,
                                   abs(mp.mpf(float(row[index])) - exact) / (1 + abs(exact)))
    assert max_actual_error < mp.mpf("1e-9")
    assert max_split_error < mp.mpf("1e-40")
    print(f"MP50 sharp-endpoint audit Y={Y},N={N},K={K}: "
          f"atom_at_K={mp.nstr(atom, 16)} belongs only to early; "
          f"mass_abs_error={mp.nstr(mass_error, 7)}, "
          f"actual_scaled_error={mp.nstr(max_actual_error, 7)}, "
          f"exact_split_error={mp.nstr(max_split_error, 7)}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, choices=(8, 10, 12, 14), default=14)
    args = parser.parse_args()
    started = time.perf_counter()
    mp.mp.dps = 50
    numbers, lambdas = prime_power_ledger(2**(args.max_m + 1))
    print("[E] actual signed early/late responses; sigma=1/4,beta=3/8,h=3; "
          "floating selections, NOT certified record points.")
    print(f"numpy={np.__version__}; scipy={scipy.__version__}; mpmath={mp.__version__}")
    print("E={sqrt(L)<=|xi|<=L}; Gauss10/18 continuum,8/12 frequency; "
          "K atoms ONLY early; all lags keep original origin.")
    print("m,cutoff,N,K,degenerate,M,M_late,Mlate_over_M,Sl_over_S,Dl_over_D,"
          "mass_threshold_ratio,Qfull,Qearly,Qlate,Qfull_over_M4L,"
          "Qearly_over_M4L,Qlate_over_M4L,L4difference_over_MLquarter,"
          "L4early_over_MLquarter,epsilon279,Minkowski_ratio,"
          "Jfull_over_mu4,Jlate_over_mulate4,rule_error")
    cases, reached = 0, 0
    worst_rule = worst_split = worst_minkowski = 0.0
    smallest = None
    summaries = []
    for m in (value for value in (8, 10, 12, 14) if value <= args.max_m):
        Y, L = 2**m, m * math.log(2)
        mask = numbers <= 2 * Y
        prefix = weighted_prefix(2 * Y, numbers[mask], lambdas[mask], Y)
        chosen, _, _ = candidate_maximum(Y, numbers, prefix)
        for label, N in (("Y", Y), ("2Y", 2 * Y), ("maxM", chosen)):
            K = math.floor(N / L**3)
            assert K == int(mp.floor(mp.mpf(N) / mp.log(Y)**3)), \
                "Floating cutoff floor disagrees with its independent MP50 value."
            assert K >= 1 and K <= Y / 2
            mask = numbers <= N
            n, lam = numbers[mask], lambdas[mask]
            lags = np.log(n)
            coefficients = lam * np.exp(-SIGMA * lags - n / Y)
            early = n <= K
            af = np.sum(coefficients, dtype=np.longdouble)
            ae = np.sum(coefficients[early], dtype=np.longdouble)
            al = np.sum(coefficients[~early], dtype=np.longdouble)
            bf = np.longdouble(str(continuum_mass_mp(Y, 1, N)))
            be = np.longdouble(str(continuum_mass_mp(Y, 1, K)))
            bl = np.longdouble(str(continuum_mass_mp(Y, K, N)))
            M, me, ml = float(af - bf), float(ae - be), float(al - bl)
            assert M != 0 and ml != 0
            assert abs(M - me - ml) < 1e-10
            S, Sl = af + bf, al + bl
            D = prime_brownian_energy(lags, coefficients) + np.longdouble(
                str(continuum_brownian_energy_mp(Y, N)))
            Dl = prime_brownian_energy(lags[~early], coefficients[~early]) + np.longdouble(
                str(continuum_late_energy_mp(Y, K, N)))
            coarse, _ = band_integrals(Y, K, N, lags, coefficients, early, 10, 8)
            fine, split_error = band_integrals(Y, K, N, lags, coefficients, early, 18, 12)
            nonzero = np.abs(fine) > 1e-30
            error = float(np.max(np.abs(fine[nonzero] - coarse[nonzero]) / np.abs(fine[nonzero])))
            assert error < 1e-7 and split_error < 1e-9
            qf, qe, ql, jf, jl = fine
            difference = abs(qf**.25 - ql**.25)
            if K == 1:
                assert qe == 0 and abs(qf - ql) < 1e-12 * qf
                minkowski = 0.0  # degenerate equality; not a division by zero
            else:
                minkowski = float(difference / qe**.25)
                assert minkowski <= 1 + 1e-8
            denominator = abs(M) * L**.25
            epsilon = (K / N)**DELTA * (1 + L)**.25
            threshold = abs(M) / (Y**.25 * math.sqrt(ell(Y)))
            cases += 1
            reached += threshold > 1
            worst_rule, worst_split = max(worst_rule, error), max(worst_split, split_error)
            worst_minkowski = max(worst_minkowski, minkowski)
            print(f"{m},{label},{N},{K},{K==1},{M:.11g},{ml:.11g},{ml/M:.9g},"
                  f"{Sl/S:.9g},{Dl/D:.9g},{threshold:.8g},"
                  + ",".join(f"{value:.10g}" for value in (qf, qe, ql))
                  + "," + ",".join(f"{value/(M**4*L):.9g}" for value in (qf, qe, ql))
                  + f",{difference/denominator:.8g},{qe**.25/denominator:.8g},"
                  f"{epsilon:.8g},{minkowski:.8g},{jf/(M**4*D):.9g},"
                  f"{jl/(ml**4*Dl):.9g},{error:.4g}", flush=True)
            if smallest is None and K >= 2:
                smallest = (Y, K, N, n, lags, coefficients, (M, me, ml))
            if label == "maxM":
                summaries.append((Y, K, qf/(M**4*L), qe/(M**4*L),
                                  ql/(M**4*L), ml/M))
    small_mp50_check(*smallest)
    print(f"SUMMARY cases={cases}; large-mass threshold reached={reached}; "
          "Y=N=256,K=1 is explicitly degenerate, early source zero.")
    print(f"SUMMARY max Gaussian relative difference={worst_rule:.7g}; "
          f"max scaled source-split discrepancy={worst_split:.7g}; "
          f"max L4 Minkowski ratio={worst_minkowski:.7g} <= 1.")
    for Y, K, qf, qe, ql, massratio in summaries:
        print(f"SUMMARY maxM Y={Y},K={K}: Qfull/early/late over original M4L="
              f"{qf:.7g},{qe:.7g},{ql:.7g}; Mlate/M={massratio:.7g}.")
    print(f"SUMMARY PASS finite checks; elapsed_seconds={time.perf_counter()-started:.3f}.")
    print("SUMMARY [E] No certified maxima, record point, uniform arithmetic constant, "
          "late-band saving, or full J4 established.")


if __name__ == "__main__":
    main()

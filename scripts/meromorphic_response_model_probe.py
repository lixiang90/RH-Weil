#!/usr/bin/env python3
"""[E] A fixed positive integer source with unit-residue off-line poles.

Run: python -B scripts/meromorphic_response_model_probe.py [--max-m 18]
Defaults Y=N=2^14,2^16; --max-m 18 adds 2^18. No output files are written.

sigma=1/4, rho=17/20+2i, B=ceil(4^(20/3))=10322 are fixed ONCE.
F(x)=0 for x<=B, and F(x)=-2 Re((x^rho-B^rho)/rho) for x>B.
lambda(n)=1+F(n)-F(n-1) lies in [1/2,3/2], since |F'|<=1/2.
The baseline includes EVERY integer n>=2, not primes or prime powers.

The associated D=sum lambda(n)n^-s satisfies
 D=zeta(s)-1-zeta(s+1-rho)-zeta(s+1-conj(rho))+H(s),
with H holomorphic for Re(s)>Re(rho)-1. Its residues are 1,-1,-1.
Thus Z=exp(sum lambda(n)n^-s/log(n)), initially Re(s)>1, has a
single-valued meromorphic continuation with pole 1 and zeros rho,conj(rho).
This is NOT a Riemann/Dirichlet zeta counterexample: no functional equation,
Euler product over primes, or Gamma/Weil bridge is supplied by this model.
The finite script does not prove the continuation or the full response bound.

Actual p/c, central mass, both cutoffs, and original Brownian denominator are
retained. The continuous model uses F'(x)dx ONLY on (B,N]; its exact finite
incomplete-gamma mass is distinguished from the asymptotic Gamma coefficient.
We integrate the reflected bands [0,sqrt L], [sqrt L,L], [L,2L], not full J4.
No Y is claimed to be a certified amplitude record or a 275/284 selection.
Gaussian-order and MP50 checks are numerical [E], not error certificates.
"""

from __future__ import annotations

import argparse
import math
import sys
import time

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np

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

SIGMA = .25
THETA = .85
GAMMA = 2.0
RHO = complex(THETA, GAMMA)
B = 10322


def source_coefficients(N):
    n = np.arange(2, N + 1, dtype=np.float64)
    lam = np.ones_like(n)
    active = n > B
    previous = n[active] - 1
    # Stable adjacent difference, including the first cell (B,B+1].
    difference = np.exp(RHO * np.log(previous)) * np.expm1(
        RHO * np.log1p(1 / previous)
    ) / RHO
    lam[active] -= 2 * np.real(difference)
    assert np.min(lam) >= .5 and np.max(lam) <= 1.5
    return n, lam


def mode_rule(Y, N, maximum, order):
    if N <= B:
        return np.array([], dtype=float), np.array([], dtype=float)
    u, weights = continuum_rule(Y, math.log(B), math.log(N), maximum + GAMMA, order)
    return u, weights * (-2 * np.exp((THETA - 1) * u) * np.cos(GAMMA * u))


def exact_mode_transform(Y, N, xi):
    if N <= B:
        return mp.mpf(0)
    rho = mp.mpc(mp.mpf(17) / 20, 2)
    exponent = rho - mp.mpf(1) / 4

    def integral(frequency):
        s = exponent + 1j * frequency
        return mp.power(Y, s) * mp.gammainc(s, mp.mpf(B) / Y, mp.mpf(N) / Y)

    return -mp.re(integral(xi) + integral(-xi) - 2 * integral(0))


def exact_mode_mass(Y, N):
    if N <= B:
        return mp.mpf(0)
    s = mp.mpc(mp.mpf(17) / 20 - mp.mpf(1) / 4, 2)
    return -2 * mp.re(mp.power(Y, s) * mp.gammainc(s, mp.mpf(B) / Y, mp.mpf(N) / Y))


def integrate(Y, N, lags, coefficients, inner, outer):
    L = math.log(Y)
    thresholds = (0., math.sqrt(L), L, 2 * L)
    continuous = continuum_rule(Y, 0., math.log(N), thresholds[-1], inner)
    mode = mode_rule(Y, N, thresholds[-1], inner)
    result = []
    for left, right in zip(thresholds[:-1], thresholds[1:]):
        frequencies, weights = composite_gauss(left, right, .125, outer)
        # Q_actual, Q_mode, Q_residual, actual response, FIVE signed terms.
        total = np.zeros(9, dtype=np.longdouble)
        for start in range(0, len(frequencies), 32):
            xi = frequencies[start:start + 32]
            qw = weights[start:start + 32]
            p = centered_transform(xi, lags, coefficients).astype(np.longdouble)
            c = -centered_transform(xi, *continuous).astype(np.longdouble)
            assert np.all(p <= 0) and np.all(c >= 0)
            actual = p + c
            model = centered_transform(xi, *mode).astype(np.longdouble)
            residual = actual - model
            base = qw.astype(np.longdouble) / (np.pi * xi.astype(np.longdouble)**2)
            physical = base * (p*p + c*c)
            for index, value in enumerate((actual, model, residual)):
                total[index] += np.sum(base * value**4, dtype=np.longdouble)
            total[3] += np.sum(physical * actual**4, dtype=np.longdouble)
            pieces = (model**4, 4*model**3*residual,
                      6*model*model*residual*residual,
                      4*model*residual**3, residual**4)
            for index, piece in enumerate(pieces):
                total[4 + index] += np.sum(physical * piece, dtype=np.longdouble)
        result.append(total)
    return np.array(result)


def mp_checks(Y, N, lags, coefficients, independent_atomic):
    rho = mp.mpc(mp.mpf(17) / 20, 2)
    cutoff_exact = int(mp.ceil(mp.power(4, mp.mpf(20) / 3)))
    assert cutoff_exact == B
    max_coefficient = mp.mpf(0)
    max_remainder = mp.mpf(0)
    for n in (2, B, B + 1, B + 2, B + 17, N):
        if n > N:
            continue
        exact = mp.mpf(1)
        if n > B:
            exact -= 2 * mp.re((mp.power(n, rho) - mp.power(n - 1, rho)) / rho)
            remainder = exact - 1 + 2 * mp.re(mp.power(n, rho - 1))
            bound = abs(rho - 1) * mp.power(n - 1, mp.re(rho) - 2)
            assert abs(remainder) <= bound
            max_remainder = max(max_remainder, abs(remainder) / bound)
        computed = source_coefficients(n)[1][-1]
        max_coefficient = max(max_coefficient, abs(mp.mpf(float(computed)) - exact))
    samples = np.array([.125, GAMMA, math.log(Y), 2 * math.log(Y)])
    continuous = continuum_rule(Y, 0., math.log(N), samples[-1], 18)
    mode = mode_rule(Y, N, samples[-1], 18)
    mode_values = centered_transform(samples, *mode)
    continuum_values = centered_transform(samples, *continuous)
    mode_error = continuum_error = mp.mpf(0)
    for xi_float, v_mode, v_continuum in zip(samples, mode_values, continuum_values):
        xi = mp.mpf(float(xi_float))
        mode_exact = exact_mode_transform(Y, N, xi)
        continuum_exact = exact_continuum_transform(Y, mp.mpf(1), mp.mpf(N), xi)
        mode_error = max(mode_error, abs(mp.mpf(float(v_mode)) - mode_exact) / (1 + abs(mode_exact)))
        continuum_error = max(continuum_error, abs(mp.mpf(float(v_continuum)) - continuum_exact) / (1 + abs(continuum_exact)))
    atomic_error = mp.mpf(0)
    if independent_atomic:
        # One complete atom sum at gamma, independently using MP50 adjacent powers.
        xi = mp.mpf(2)
        exact_terms = []
        for n in range(2, N + 1):
            lam = mp.mpf(1)
            if n > B:
                lam -= 2 * mp.re((mp.power(n, rho) - mp.power(n - 1, rho)) / rho)
            weight = lam * mp.power(n, -mp.mpf(1)/4) * mp.exp(-mp.mpf(n)/Y)
            exact_terms.append(-2 * weight * mp.sin(xi * mp.log(n)/2)**2)
        exact_p = mp.fsum(exact_terms)
        floating_p = centered_transform(np.array([2.]), lags, coefficients)[0]
        atomic_error = abs(mp.mpf(float(floating_p)) - exact_p) / (1 + abs(exact_p))
    assert max_coefficient < mp.mpf('1e-12')
    assert max(mode_error, continuum_error, atomic_error) < mp.mpf('1e-9')
    return max_coefficient, max_remainder, mode_error, continuum_error, atomic_error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-m', type=int, choices=(14, 16, 18), default=16)
    args = parser.parse_args()
    started = time.perf_counter()
    mp.mp.dps = 50
    s = mp.mpc(mp.mpf(3)/5, 2)
    asymptotic_coefficient = -2 * mp.gammainc(s, 0, 1)
    recurrence_error = abs(s * mp.gammainc(s, 0, 1) - mp.exp(-1) - mp.gammainc(s + 1, 0, 1))
    assert recurrence_error < mp.mpf('1e-45')
    print('[E] Fixed positive all-integer model; no Euler product, FE, RH counterexample, or record certification.')
    print(f'sigma=1/4; theta=17/20; gamma=2; B={B}; lambda in [1/2,3/2].')
    print('Finite reflected bands [0,sqrt L], [sqrt L,L], [L,2L]; no omitted-tail numerical claim.')
    print('MP50 asymptotic coefficient -2*gamma(3/5+2i,1)=' + mp.nstr(asymptotic_coefficient, 32))
    print('m,N,lambda_min,lambda_max,M,M_mode_finite,M_gamma_main,M_minus_mode,'
          'absM_over_Ytheta_minus_sigma,Q_partial,Q_partial_over_M4L,Q_mode_over_M4L,'
          'Q_residual_over_M4L,J_partial_over_mu4,J_sqrtL_to_L_over_mu4,'
          'J_L_to_2L_over_mu4,gauss_error,signed_sum_error')
    max_rule = max_sum = 0.
    max_checks = [mp.mpf(0)] * 5
    cross_rows = []
    for m in (value for value in (14, 16, 18) if value <= args.max_m):
        Y = N = 2**m
        n, lam = source_coefficients(N)
        lags = np.log(n)
        coefficients = lam * np.exp(-SIGMA * lags - n/Y)
        A = np.sum(coefficients, dtype=np.longdouble)
        B_mass = mp.power(Y, mp.mpf(3)/4) * mp.gammainc(mp.mpf(3)/4, mp.mpf(1)/Y, 1)
        M = float(A - np.longdouble(str(B_mass)))
        model_mass = exact_mode_mass(Y, N)
        main_mass = mp.re(asymptotic_coefficient * mp.power(Y, s))
        mass_residual = mp.mpf(M) - model_mass
        # Exact theorem has <=1.5*exp(-1/Y); tolerance here covers floating summation.
        assert abs(mass_residual) < mp.mpf('1.500001')
        D = prime_brownian_energy(lags, coefficients) + np.longdouble(str(continuum_brownian_energy_mp(Y, N)))
        assert M != 0
        mass_scale = M**4 * math.log(Y)
        response_scale = M**4 * D
        coarse = integrate(Y, N, lags, coefficients, 10, 8)
        fine = integrate(Y, N, lags, coefficients, 18, 12)
        scale = np.maximum(np.abs(fine[:, :4]), np.longdouble(1e-20))
        error = float(np.max(np.abs(coarse[:, :4] - fine[:, :4]) / scale))
        term_scale = np.maximum(np.sum(np.abs(fine[:, 4:]), axis=1), np.longdouble(1e-20))
        error = max(error, float(np.max(np.abs(coarse[:, 4:] - fine[:, 4:]) / term_scale[:, None])))
        identity = float(np.max(np.abs(np.sum(fine[:, 4:], axis=1) - fine[:, 3]) / fine[:, 3]))
        assert error < 1e-7 and identity < 1e-8
        max_rule, max_sum = max(max_rule, error), max(max_sum, identity)
        checks = mp_checks(Y, N, lags, coefficients, independent_atomic=(m == 14))
        max_checks = [max(old, new) for old, new in zip(max_checks, checks)]
        total = np.sum(fine, axis=0)
        cross_rows.append((m, total[4:] / total[3]))
        print(f'{m},{N},{np.min(lam):.9g},{np.max(lam):.9g},{M:.12g},'
              f'{float(model_mass):.12g},{float(main_mass):.12g},{float(mass_residual):.9g},'
              f'{abs(M)/Y**(THETA-SIGMA):.9g},{total[0]:.10g},{total[0]/mass_scale:.10g},'
              f'{total[1]/mass_scale:.10g},{total[2]/mass_scale:.10g},'
              f'{total[3]/response_scale:.10g},{fine[1,3]/response_scale:.10g},'
              f'{fine[2,3]/response_scale:.10g},{error:.4g},{identity:.4g}', flush=True)
    print('m,mode4_over_full,4mode3res_over_full,6mode2res2_over_full,4moderes3_over_full,res4_over_full')
    for m, terms in cross_rows:
        print(str(m) + ',' + ','.join(f'{value:.10g}' for value in terms))
    print(f'SUMMARY max Gaussian comparison={max_rule:.6g}; signed-five-term identity={max_sum:.6g}.')
    print('SUMMARY MP50 (coefficient error,remainder/bound,mode transform error,continuum error,atom sum error)='
          + ','.join(mp.nstr(value, 7) for value in max_checks) + '.')
    print('SUMMARY Gamma recurrence error=' + mp.nstr(recurrence_error, 7) + '; its nonvanishing theorem is not inferred from sampling.')
    print('SUMMARY Fixed-prefix correction is retained; these finite windows need not be in the asymptotic regime or at amplitude records.')
    print('SUMMARY Only the separate analytic argument can establish full J4=O(mu^4) on good-amplitude sequences; no infinite conclusion is fitted here.')
    print(f'SUMMARY PASS finite checks; elapsed_seconds={time.perf_counter()-started:.3f}; no files written.')


if __name__ == '__main__':
    main()

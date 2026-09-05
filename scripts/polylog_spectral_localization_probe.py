#!/usr/bin/env python3
"""[E] Finite MP70 checks for growing-order shifted integration by parts.

Run: python -B scripts/polylog_spectral_localization_probe.py

Only six synthetic rho values and Y=N in {16,64,256} are used. They are NOT
claimed to be zeta zeros. sigma=1/4, L=log(Y), T=L, m=ceil(L), h=mT, V=4h.
Each physical frequency obeys 1<=q<=T. Cases include small, near-resonant,
and greater-than-V imaginary parts; one real part is below sigma.

The unchanged kernel is I_rho=(1/rho) integral_log2^logN e^(s_rho u) A_q(u)du,
 s_rho=rho-sigma,
 A_q=-exp(-x)*[(sigma+x)(cos(qu)-1)+q*sin(qu)], x=exp(u)/Y.
It retains the central '-1' and BOTH endpoints log2 and logN.

Write A_q=exp(-x) sum_nu P_nu(x) exp(i nu u), nu=0,+q,-q, with
 P_0=sigma+x, P_+=-(sigma+x)/2+iq/2, P_-=conjugate(P_+).
Normalized jets h^-j(D-h)^j A_q use the polynomial recursion
 P_next=(x/h)P' + (i nu/h-1-x/h)P.
Each monomial integral is evaluated using a finite incomplete-gamma interval,
not differentiation of the full kernel. A separate direct MP70 quadrature
checks the first small-frequency case, and low jet orders are independently
checked by differentiation of exp(-hu)A_q.

All numbers are [E], not interval certificates. These finite identities do
NOT prove uniform-in-m constants, all-height spectral sums, a history bound,
the zeta explicit formula, a full J4 budget, or RH. No output files are written.
Only the already installed optional research dependency mpmath is used.
"""

from __future__ import annotations

import sys
import time

sys.dont_write_bytecode = True

import mpmath as mp


def next_polynomial(polynomial, frequency, h):
    """Exact algebraic recurrence, evaluated at the current MP precision."""
    result = [mp.mpc(0) for _ in range(len(polynomial)+1)]
    for k, coefficient in enumerate(polynomial):
        result[k] += (mp.mpf(k)/h + 1j*frequency/h - 1)*coefficient
        result[k+1] -= coefficient/h
    return result


def jet_polynomials(sigma, q, h, m):
    frequencies = (mp.mpf(0), q, -q)
    initial = (
        [mp.mpc(sigma), mp.mpc(1)],
        [mp.mpc(-sigma/2, q/2), mp.mpc(-mp.mpf(1)/2)],
        [mp.mpc(-sigma/2, -q/2), mp.mpc(-mp.mpf(1)/2)],
    )
    jets = [list(initial)]
    for _ in range(m):
        jets.append([next_polynomial(poly, nu, h)
                     for poly, nu in zip(jets[-1], frequencies)])
    return frequencies, jets


def polynomial_value(polynomial, x):
    result = mp.mpc(0)
    for coefficient in reversed(polynomial):
        result = result*x + coefficient
    return result


def normalized_jet(u, Y, frequencies, polynomials):
    x = mp.exp(u)/Y
    value = mp.fsum(polynomial_value(poly, x)*mp.exp(1j*nu*u)
                    for nu, poly in zip(frequencies, polynomials))
    return mp.exp(-x)*value


def monomial_integral(Y, N, s, frequencies, polynomials):
    values = []
    for nu, polynomial in zip(frequencies, polynomials):
        exponent = s+1j*nu
        factor = mp.power(Y, exponent)
        values.append(factor*mp.fsum(
            coefficient*mp.gammainc(exponent+k, mp.mpf(2)/Y, mp.mpf(N)/Y)
            for k, coefficient in enumerate(polynomial)
        ))
    return mp.fsum(values)


def original_amplitude(u, Y, sigma, q):
    x = mp.exp(u)/Y
    # Stable centering, independent of the polynomial coefficient encoding.
    centered_cosine = -2*mp.sin(q*u/2)**2
    return -mp.exp(-x)*((sigma+x)*centered_cosine+q*mp.sin(q*u))


def finite_case(Y, q_kind, real_part, gamma_kind, direct_quadrature=False):
    N, sigma = Y, mp.mpf(1)/4
    L = mp.log(Y)
    m, T = int(mp.ceil(L)), L
    h = m*T
    q = {'one': mp.mpf(1), 'half': T/2, 'top': T}[q_kind]
    gamma = {'low': mp.mpf('.7'), 'near': q+mp.mpf('.3'),
             'equal': q, 'high': 4*h+1}[gamma_kind]
    rho, s = mp.mpc(real_part, gamma), mp.mpc(real_part-sigma, gamma)
    assert 1 <= q <= T
    frequencies, jets = jet_polynomials(sigma, q, h, m)
    u0, u1 = mp.log(2), mp.log(N)
    original = monomial_integral(Y, N, s, frequencies, jets[0])/rho
    ratio = -h/(s+h)
    upper = mp.fsum(ratio**j*mp.exp(s*u1)*normalized_jet(u1, Y, frequencies, jets[j])
                    for j in range(m))/(rho*(s+h))
    lower = mp.fsum(ratio**j*mp.exp(s*u0)*normalized_jet(u0, Y, frequencies, jets[j])
                    for j in range(m))/(rho*(s+h))
    jet_integral = monomial_integral(Y, N, s, frequencies, jets[m])
    remainder = ratio**m*jet_integral/rho
    reconstructed = upper-lower+remainder
    identity_error = abs(original-reconstructed)/(1+abs(original))
    cancellation_scale = (abs(upper)+abs(lower)+abs(remainder))/(1+abs(original))

    derivative_error = mp.mpf(0)
    midpoint = (u0+u1)/2
    for j in (0, 1, 2):
        independent = mp.exp(h*midpoint)*mp.diff(
            lambda u: mp.exp(-h*u)*original_amplitude(u, Y, sigma, q), midpoint, j
        )/h**j
        polynomial = normalized_jet(midpoint, Y, frequencies, jets[j])
        derivative_error = max(derivative_error,
                               abs(polynomial-independent)/(1+abs(independent)))

    quadrature_error = mp.mpf(0)
    if direct_quadrature:
        nodes = [u0+(u1-u0)*k/8 for k in range(9)]
        integral = mp.quad(lambda u: mp.exp(s*u)*original_amplitude(u, Y, sigma, q), nodes)/rho
        quadrature_error = abs(integral-original)/(1+abs(integral))

    sampled_jet_ratio = max(
        abs(normalized_jet(u, Y, frequencies, jets[j]))/q
        for u in (u0, midpoint, u1) for j in range(m+1)
    )
    normalized_remainder_integral = abs(jet_integral)/(q*mp.power(Y, 1-sigma))
    assert max(identity_error, derivative_error, quadrature_error) < mp.mpf('1e-55')
    return (Y, m, q, gamma, h, abs(original), abs(upper), abs(lower), abs(remainder),
            identity_error, derivative_error, quadrature_error, sampled_jet_ratio,
            normalized_remainder_integral, cancellation_scale)


def main():
    started = time.perf_counter()
    mp.mp.dps = 70
    cases = (
        (16, 'one', mp.mpf('.1'), 'low', True),
        (16, 'top', mp.mpf('.85'), 'near', False),
        (64, 'half', mp.mpf('.85'), 'low', False),
        (64, 'top', mp.mpf('.85'), 'high', False),
        (256, 'top', mp.mpf('.85'), 'equal', False),
        (256, 'top', mp.mpf('.85'), 'high', False),
    )
    print('[E] MP70 finite synthetic-rho checks, not actual zeros or an infinite spectral certificate.')
    print('N=Y; sigma=1/4; T=logY; m=ceil(logY); h=mT; high cases have gamma>4h.')
    print('I=upper_boundary-lower_boundary+remainder; central -1 and both endpoints retained.')
    print('Y,m,q,gamma,h,abs_I,abs_upper,abs_lower,abs_remainder,'
          'IBP_scaled_error,jet_derivative_scaled_error,direct_quadrature_scaled_error,'
          'sampled_max_abs_normalized_jet_over_q,abs_jet_integral_over_qY075,cancellation_scale')
    rows = [finite_case(*case) for case in cases]
    for row in rows:
        print(','.join(str(value) if index < 2 else mp.nstr(value, 12)
                       for index, value in enumerate(row)))
    print('SUMMARY max shifted-IBP identity error=' + mp.nstr(max(row[9] for row in rows), 8)
          + '; independent low-order jet error=' + mp.nstr(max(row[10] for row in rows), 8)
          + '; independent direct-integral error=' + mp.nstr(max(row[11] for row in rows), 8) + '.')
    print('SUMMARY Normalized jet and remainder ratios are finite diagnostics only; '
          'no uniform bound is inferred from these samples.')
    print(f'SUMMARY PASS {len(rows)} cases; elapsed_seconds={time.perf_counter()-started:.3f}; no files written.')


if __name__ == '__main__':
    main()

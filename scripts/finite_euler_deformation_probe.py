#!/usr/bin/env python3
"""Finite checks for one-prime Euler deformations; no required dependencies.

Run: python -B scripts/finite_euler_deformation_probe.py
     python -B scripts/finite_euler_deformation_probe.py --no-mpmath

The main fixed model is Z(s)=zeta(s) P(2^-s), P(t)=1+(29/10)t+2t^2.
Its Dirichlet coefficients are 1,39/10,59/10 according as v_2(n)=0,1,>=2.
Exact Fraction arithmetic checks polynomial reciprocity, these coefficients,
and the first 64 local logarithmic-derivative coefficients in TWO ways.
T_0=2,T_1=29,T_k=29T_(k-1)-200T_(k-2), with S_k=T_k/10^k.
The coefficient of 2^-ks in -Z'/Z, divided by log(2), is
 1+(-1)^(k-1) S_k.
Thus ordinary Dirichlet positivity is NOT logarithmic-source positivity.

A SEPARATE prefix countermodel uses P_K(t)=1-R^d t^d, R=3/2,d=K+1.
Its first K local logarithmic-derivative coefficients agree with zeta's,
but its d-th is 1-d R^d<0, and its polynomial zeros have |t|=1/R<1/sqrt(2).
This second model does NOT assert the first model's completed functional
equation or positive Dirichlet coefficients. Do not combine their axioms.

All floating/MP60 values are [E], not interval certificates. Exact FINITE
identities do not substitute for the proofs of infinite sign statements,
analytic continuation, a functional equation on the whole plane, or RH.
No response positivity, full J4, Weil configuration, or Selberg-class claim.
No files, PDFs, dependency changes, or network requests are produced.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import math
import sys
import time

sys.dont_write_bytecode = True

P = 2
A = Fraction(29, 10)


def logarithmic_derivative(local_coefficients):
    """Exact formal t L'(t)/L(t), from L*g=t L'; independent of roots."""
    assert local_coefficients[0] == 1
    output = [Fraction(0)]
    for k in range(1, len(local_coefficients)):
        value = k * local_coefficients[k]
        value -= sum((output[j] * local_coefficients[k-j]
                      for j in range(1, k)), Fraction(0))
        output.append(value)
    return output


def exact_main_checks(maximum):
    polynomial = {0: Fraction(1), 1: A, 2: Fraction(P)}
    # P(t)=2 t^2 P(1/(2t)); negative integer powers stay rational.
    reciprocal = {2-k: coefficient * Fraction(P)**(1-k)
                  for k, coefficient in polynomial.items()}
    assert reciprocal == polynomial
    discriminant = A*A - 4*P
    assert discriminant == Fraction(41, 100)
    assert A*A > 4*P and A < P+1

    for n in range(1, 257):
        direct = sum((coefficient for degree, coefficient in polynomial.items()
                      if n % P**degree == 0), Fraction(0))
        expected = (Fraction(1) if n % 2 else
                    Fraction(39, 10) if n % 4 else Fraction(59, 10))
        assert direct == expected and direct > 0

    integers = [2, 29]
    for k in range(2, maximum+1):
        integers.append(29*integers[-1] - 200*integers[-2])
    expected_log = [Fraction(0)] + [
        1 + (-1)**(k-1) * Fraction(integers[k], 10**k)
        for k in range(1, maximum+1)
    ]
    local = [Fraction(1)] + [Fraction(39, 10)] + [
        Fraction(59, 10) for _ in range(2, maximum+1)
    ]
    formal_log = logarithmic_derivative(local)
    assert formal_log == expected_log
    assert all(formal_log[k] > 0 if k % 2 else formal_log[k] < 0
               for k in range(1, maximum+1))
    assert formal_log[1] == Fraction(39, 10)
    if maximum >= 2:
        assert formal_log[2] == -Fraction(341, 100)
    return formal_log


def exact_prefix_checks(K):
    R, d = Fraction(3, 2), K+1
    # Local Euler factor (1-R^d t^d)/(1-t), through degree 2d.
    local = [Fraction(1) if k < d else 1-R**d for k in range(2*d+1)]
    formal_log = logarithmic_derivative(local)
    expected = [Fraction(0)] + [
        1-d*R**k if k % d == 0 else Fraction(1)
        for k in range(1, 2*d+1)
    ]
    assert formal_log == expected
    assert all(formal_log[k] == 1 for k in range(1, K+1))
    assert formal_log[d] == 1-d*R**d < 0
    assert R*R > P and R < P
    # The lost ordinary Dirichlet positivity is explicit, not concealed.
    assert local[d] < 0
    return d, formal_log[d]


def numerical_checks(disable):
    if disable:
        mp = None
    else:
        try:
            import mpmath as mp
        except ImportError:
            mp = None
    if mp is None:
        alpha = (29 + math.sqrt(41))/20
        theta = math.log(alpha)/math.log(2)
        print(f'[E] float only: theta={theta:.15g}, 1-theta={1-theta:.15g}; '
              'mpmath disabled/unavailable, no numerical FE check attempted.')
        return

    mp.mp.dps = 60
    a = mp.mpf(29)/10
    alpha, beta = (29+mp.sqrt(41))/20, (29-mp.sqrt(41))/20
    theta = mp.log(alpha)/mp.log(2)
    gamma0 = mp.pi/mp.log(2)

    def factor(s):
        t = mp.power(2, -s)
        return 1+a*t+2*t*t

    def xi(s):
        return s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)/2

    def completed(s):
        return mp.power(2, s-mp.mpf(1)/2)*factor(s)*xi(s)

    def symmetric_factor(s):
        return (mp.power(2, s-mp.mpf(1)/2)
                + mp.power(2, mp.mpf(1)/2-s) + a/mp.sqrt(2))

    fe_error = identity_error = mp.mpf(0)
    for re, im in (('.2', '.7'), ('.7', '4.2'), ('1.4', '-3'), ('.5', '12')):
        s = mp.mpc(re, im)
        left, right = completed(s), completed(1-s)
        fe_error = max(fe_error, abs(left-right)/(1+abs(left)+abs(right)))
        alternative = symmetric_factor(s)*xi(s)
        identity_error = max(identity_error,
                             abs(left-alternative)/(1+abs(left)+abs(alternative)))
    zero_error = mp.mpf(0)
    for re in (theta, 1-theta):
        for height in (gamma0, 3*gamma0):
            zero_error = max(zero_error, abs(factor(re+1j*height)))
    assert max(fe_error, identity_error, zero_error) < mp.mpf('1e-45')
    print('[E] MP60: alpha=' + mp.nstr(alpha, 25) + ', beta=' + mp.nstr(beta, 25)
          + '; theta=' + mp.nstr(theta, 25) + ', 1-theta=' + mp.nstr(1-theta, 25)
          + '; first |Im|=' + mp.nstr(gamma0, 25) + '.')
    print('[E] MP60 scaled completed-FE error=' + mp.nstr(fe_error, 7)
          + ', symmetric-factor identity error=' + mp.nstr(identity_error, 7)
          + ', added-factor zero residual=' + mp.nstr(zero_error, 7) + '.')
    print('[E] Central-line factor lower value a/sqrt(2)-2='
          + mp.nstr(a/mp.sqrt(2)-2, 20)
          + '; positive central values do not remove off-line factor zeros.')


def bounded_positive(value):
    number = int(value)
    if not 1 <= number <= 256:
        raise argparse.ArgumentTypeError('must be an integer from 1 to 256')
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-power', type=bounded_positive, default=64)
    parser.add_argument('--prefix-k', type=bounded_positive, default=64)
    parser.add_argument('--no-mpmath', action='store_true')
    args = parser.parse_args()
    started = time.perf_counter()
    coefficients = exact_main_checks(args.max_power)
    d, first_negative = exact_prefix_checks(args.prefix_k)
    print('Finite exact checks are not substitutes for infinite theorems; all numerical values are [E].')
    print('[finite exact PASS] P(t)=2t^2P(1/(2t)); positive Dirichlet classes '
          '1,39/10,59/10 checked for n<=256.')
    print(f'[finite exact PASS] Integer T recurrence equals independent formal log-derivative '
          f'convolution for 1<=k<={args.max_power}; alternating signs checked.')
    if args.max_power >= 2:
        print(f'[finite exact] lambda(2)/log(2)={coefficients[1]}; '
              f'lambda(4)/log(2)={coefficients[2]}.')
    print(f'[finite exact PASS] SEPARATE prefix model R=3/2,d={d}: first K={args.prefix_k} '
          f'log coefficients equal 1; coefficient d is {first_negative} < 0; R^2>2.')
    print('[scope] Prefix model does not retain positive Dirichlet coefficients or the completed FE; '
          'the main model does not retain positive logarithmic-source coefficients.')
    numerical_checks(args.no_mpmath)
    print(f'PASS; elapsed_seconds={time.perf_counter()-started:.3f}; '
          'no files, dependency installation, or infinite-frequency claims.')


if __name__ == '__main__':
    main()

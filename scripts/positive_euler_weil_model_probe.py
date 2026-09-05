#!/usr/bin/env python3
"""Finite checks for note 290; standard library only.

The formal curve-shaped model has
Z(t)=(1-q*t+q*t*t)/((1-t)*(1-q*t)), q>=5.
Exact integer checks: power traces, positive closed-point counts, an
independent truncated Euler product, graded pairing, and rational FE.
Exact Fraction checks: full (not sampled-frequency) Brownian moments for
positive GEOMETRIC weights w_n=2**(-n), including orders 2,4,6,8.
These weights are not the Abel weight. Separate floating [E] checks use
the original Abel choice q**(-sigma*n)*exp(-q**n/Y), Y=q**K, sigma=1/4.

The common factor log(q) and lattice spacing log(q) cancel in the ratios.
Finite checks do not replace the all-n positivity or all-moment proofs.
This is not the zeta function of an actual smooth projective curve.
No files, PDFs, dependencies, or network operations are produced.
"""

from fractions import Fraction as F
from math import comb, exp
import time


def mobius(n):
    value, prime = 1, 2
    while prime * prime <= n:
        if n % prime == 0:
            n //= prime
            value = -value
            if n % prime == 0:
                return 0
        prime += 1
    return -value if n > 1 else value


def counts(q, length):
    traces = [2, q]
    for n in range(2, length + 1):
        traces.append(q * traces[-1] - q * traces[-2])
    points = [0] + [q**n + 1 - traces[n] for n in range(1, length + 1)]
    closed = [0]
    for n in range(1, length + 1):
        numerator = sum(mobius(n // d) * points[d]
                        for d in range(1, n + 1) if n % d == 0)
        assert numerator % n == 0
        closed.append(numerator // n)
        assert closed[-1] > 0
        assert sum(d * closed[d] for d in range(1, n + 1)
                   if n % d == 0) == points[n]
    assert closed[1] == 1 and closed[2] == q
    return traces, points, closed


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i+j] += x*y
    return out


def matrix_multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def exact_algebra(q):
    traces, points, closed = counts(q, 80)
    length = 20
    product = [1] + [0] * length
    for n in range(1, length + 1):
        factor = [0] * (length + 1)
        for k in range(length // n + 1):
            factor[n*k] = comb(closed[n]+k-1, k)
        product = multiply(product, factor)[:length+1]
    denominator = [1, -(q+1), q]
    assert multiply(product, denominator)[:length+1] == [1, -q, q] + [0]*(length-2)

    numerator = [F(1), F(-q), F(q)]
    # q*t^2 P(1/(q*t))=P(t), and the denominator has the same symmetry.
    for polynomial in (numerator, list(map(F, denominator))):
        reciprocal = [polynomial[2-k] * F(q)**(k-1) for k in range(3)]
        assert reciprocal == polynomial

    matrix = [[0, -q], [1, q]]
    transpose = list(map(list, zip(*matrix)))
    pairing = [[0, 1], [-1, 0]]
    assert matrix_multiply(matrix_multiply(transpose, pairing), matrix) == [
        [0, q], [-q, 0]]
    power = [[1, 0], [0, 1]]
    for n in range(1, 21):
        power = matrix_multiply(power, matrix)
        assert power[0][0] + power[1][1] == traces[n]
    return traces, points, closed


def measure(weights, sign=1):
    k = len(weights)
    out = [F(0)] * (2*k + 1) if weights and isinstance(weights[0], F) else [0.0]*(2*k+1)
    out[k] = -sign * sum(weights)
    for n, weight in enumerate(weights, 1):
        out[k-n] = out[k+n] = sign * weight / 2
    return out


def primitive_inner(left, right):
    assert len(left) == len(right)
    first = second = 0
    result = 0
    for a, b in zip(left[:-1], right[:-1]):
        first += a
        second += b
        result += first * second
    return result


def primitive_norm(coefficients):
    return primitive_inner(coefficients, coefficients)


def physical_moment(p, c, r, S, D, half_order):
    # Fourier Plancherel: integral rhat^(2k)*(phat^2+chat^2)/xi^2.
    r_power = [1]
    for _ in range(half_order):
        r_power = multiply(r_power, r)
    numerator = primitive_norm(multiply(r_power, p))
    numerator += primitive_norm(multiply(r_power, c))
    return numerator / (S**(2*half_order) * D)


def exact_moments(q, cutoff):
    traces, points, _ = counts(q, max(2, cutoff))
    a = [F(points[n], 2**n) for n in range(1, cutoff+1)]
    b = [F(q**n+1, 2**n) for n in range(1, cutoff+1)]
    p, c = measure(a), measure(b, -1)
    r = [x+y for x, y in zip(p, c)]
    S, M = sum(a)+sum(b), sum(a)-sum(b)
    D = primitive_norm(p) + primitive_norm(c)
    assert S > 0 and D > 0 and M < 0
    c_q = F(1, q+1)
    assert all(c_q*y <= x <= y for x, y in zip(a, b))
    schur = -primitive_inner(p, c) / D
    assert schur >= c_q / (1+c_q*c_q)
    ratios = []
    for k in range(1, 5):
        ratio = physical_moment(p, c, r, S, D, k) / (M/S)**(2*k)
        assert 0 <= ratio <= 2**(2*k)
        ratios.append(float(ratio))
    return ratios, float(schur)


def abel_moments(q, cutoff):
    sigma = .25
    traces, points, _ = counts(q, cutoff)
    weights = [q**(-sigma*n) * exp(-q**(n-cutoff)) for n in range(1, cutoff+1)]
    a = [points[n]*weights[n-1] for n in range(1, cutoff+1)]
    b = [(q**n+1)*weights[n-1] for n in range(1, cutoff+1)]
    scale = sum(a)+sum(b)
    a = [x/scale for x in a]
    b = [x/scale for x in b]
    # Form the tiny signed discrepancy directly, not by subtracting a and b.
    discrepancy = [-traces[n]*weights[n-1]/scale for n in range(1, cutoff+1)]
    p, c, r = measure(a), measure(b, -1), measure(discrepancy)
    S, M = sum(a)+sum(b), sum(discrepancy)
    D = primitive_norm(p) + primitive_norm(c)
    ratio = physical_moment(p, c, r, S, D, 2) / (M/S)**4
    schur = -primitive_inner(p, c)/D
    assert 0 <= ratio <= 16*(1+1e-10)
    assert schur + 1e-12 >= (q+1)/((q+1)**2+1)
    return ratio, schur


def main():
    start = time.perf_counter()
    for q in (5, 7, 8, 9, 16):
        _, _, closed = exact_algebra(q)
        print(f'[finite exact PASS] q={q}: B_n positive integral for n<=80; '
              f'Euler coefficients through 20, reciprocity, pairing; B_1..6={closed[1:7]}')
    for cutoff in (2, 4, 6, 8):
        ratios, schur = exact_moments(5, cutoff)
        print(f'[finite exact PASS; decimal display] geometric weights, q=5,K={cutoff}: '
              f'J_2k/mu^(2k), k=1..4={ratios}; -z/D={schur:.12g}')
    for cutoff in (4, 8, 12, 16, 24):
        ratio, schur = abel_moments(5, cutoff)
        print(f'[E] Abel weights, q=5,sigma=.25,K={cutoff}: '
              f'full J4/mu4={ratio:.12g}; -z/D={schur:.12g}')
    print(f'PASS; seconds={time.perf_counter()-start:.3f}. '
          'Exact finite checks and floating experiments are not infinite theorems or RH evidence.')


if __name__ == '__main__':
    main()

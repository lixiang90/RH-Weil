"""Finite audits for note 224's short-height 3+1 and 4+0 closure.

These checks validate combinatorial identities, interval kernels, and exponent
bookkeeping.  They do not implement Henriot's sieve theorem, prove an
asymptotic prime correlation, or provide evidence for RH.
"""

from __future__ import annotations

import cmath
import math


def prime_factors_with_multiplicity(n: int) -> list[int]:
    factors: list[int] = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def von_mangoldt(n: int) -> float:
    factors = prime_factors_with_multiplicity(n)
    if factors and all(p == factors[0] for p in factors):
        return math.log(factors[0])
    return 0.0


def triple_convolution(n: int) -> float:
    total = 0.0
    for a in range(2, n + 1):
        if n % a:
            continue
        for b in range(2, n // a + 1):
            if (n // a) % b:
                continue
            c = n // (a * b)
            if c >= 2:
                total += von_mangoldt(a) * von_mangoldt(b) * von_mangoldt(c)
    return total


def check_prime_power_diagonal() -> None:
    for p in (2, 3, 5, 7):
        for k in range(3, 8):
            actual = triple_convolution(p**k)
            expected = math.comb(k - 1, 2) * math.log(p) ** 3
            assert abs(actual - expected) < 1e-10 * max(1.0, expected)


def path_span(signs: tuple[int, int, int, int], logs: tuple[float, ...]) -> float:
    partial = [0.0]
    running = 0.0
    for sign, value in zip(signs[:3], logs[:3]):
        running += sign * value
        partial.append(running)
    return max(partial) - min(partial)


def check_path_support() -> None:
    samples = (
        (0.12, 0.19, 0.27, 0.91),
        (0.31, 0.34, 0.36, 0.07),
        (0.20, 0.25, 0.54, 0.99),
    )
    for logs in samples:
        expected = sum(logs[:3])
        for signs in ((1, 1, 1, -1), (1, 1, 1, 1)):
            assert abs(path_span(signs, logs) - expected) < 1e-14
            assert (path_span(signs, logs) <= 1.0) == (expected <= 1.0)


def interval_kernel(frequency: float, left: float, height: float) -> complex:
    if frequency == 0.0:
        return 1.0 + 0.0j
    return (
        cmath.exp(1j * (left + height) * frequency)
        - cmath.exp(1j * left * frequency)
    ) / (1j * height * frequency)


def check_interval_kernel() -> None:
    left, height = 17.0, 13.0
    for frequency in (0.01, 0.2, 1.0, 3.0):
        value = abs(interval_kernel(frequency, left, height))
        assert value <= min(1.0, 2.0 / (height * frequency)) + 1e-13


def distinct_primes(n: int) -> set[int]:
    return set(prime_factors_with_multiplicity(n))


def delta_majorant(h: int, constant: float = 4.0) -> float:
    value = 1.0
    for p in distinct_primes(h):
        value *= 1.0 + constant / p
    return value


def check_discriminant_harmonic_scale() -> None:
    # Finite diagnostics for the Euler-product majorant; the analytic bounded
    # mean is part of the cited theorem/elementary divisor expansion.
    for bound in (1000, 5000, 20000):
        mean = sum(delta_majorant(h) for h in range(1, bound + 1)) / bound
        harmonic = sum(
            delta_majorant(h) / h for h in range(1, bound + 1)
        ) / math.log(bound)
        assert mean < 20.0
        assert harmonic < 20.0


def check_exponent_ledger() -> None:
    # Write u = log L.  Then (log L)^4/sqrt(L) = u^4 exp(-u/2).
    # Sampling u directly makes the genuinely asymptotic decay visible
    # without ever constructing X = exp(exp(u)).
    ratios = [u**4 * math.exp(-u / 2.0) for u in (20.0, 40.0, 80.0, 160.0)]
    assert all(right < left for left, right in zip(ratios, ratios[1:]))
    assert ratios[-1] < 1e-25


def main() -> None:
    check_prime_power_diagonal()
    check_path_support()
    check_interval_kernel()
    check_discriminant_harmonic_scale()
    check_exponent_ledger()
    print("short-height 3+1/4+0 combinatorial and exponent audits passed")
    print("[scope] finite identities only; no sieve theorem or RH claim")


if __name__ == "__main__":
    main()

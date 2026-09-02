"""Finite identities for note 229's external-input reverse audit.

This checks elementary inclusion--exclusion, rational exponent bookkeeping,
and a finite discriminant-majorant expansion.  It does not implement the
Bettin--Chandee or Henriot theorems and is not evidence for RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import prod


def local_survivors(p: int, h: int) -> int:
    return sum(
        1
        for a in range(p)
        for c in range(p)
        if (a - c - h) % p == 0 and a != 0 and c != 0
    )


def check_local_density() -> None:
    for p in (3, 5, 7, 11, 13, 17, 19):
        for h in range(p):
            expected = p - 1 if h == 0 else p - 2
            assert local_survivors(p, h) == expected


def check_single_sequence_expansion() -> None:
    for divides_a in (0, 1):
        for divides_c in (0, 1):
            union = int(bool(divides_a or divides_c))
            expanded = divides_a + divides_c - divides_a * divides_c
            assert union == expanded


def check_exponents() -> None:
    assert Fraction(1) + Fraction(7, 10) + Fraction(1, 4) == Fraction(39, 20)
    q_cost = 2 * Fraction(7, 20) * 2 + Fraction(1, 4) * 2
    assert q_cost == Fraction(19, 10)
    assert Fraction(2) + q_cost == Fraction(39, 10)
    assert -Fraction(1, 20) + Fraction(39, 10) * Fraction(1, 100) < 0
    assert -Fraction(1, 20) + Fraction(39, 10) * Fraction(1, 78) == 0


def prime_divisors(n: int) -> list[int]:
    factors: list[int] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def check_discriminant_majorant() -> None:
    c = Fraction(3)
    values: list[Fraction] = []
    for h in range(1, 501):
        primes = prime_divisors(h)
        euler = prod((1 + c / p for p in primes), start=Fraction(1))
        divisor_expansion = Fraction(0)
        for mask in range(1 << len(primes)):
            term = Fraction(1)
            for index, p in enumerate(primes):
                if mask & (1 << index):
                    term *= c / p
            divisor_expansion += term
        assert euler == divisor_expansion
        values.append(euler)

    # Finite diagnostic only; the proof is the convergent Euler product
    # sum_{d squarefree} C^omega(d)/d^2.
    assert sum(values) / len(values) < 20


def main() -> None:
    check_local_density()
    check_single_sequence_expansion()
    check_exponents()
    check_discriminant_majorant()
    print("external-input reverse-audit identities: PASS")


if __name__ == "__main__":
    main()

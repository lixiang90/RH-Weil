#!/usr/bin/env python3
"""Exact finite audits of prime-valuation isolation for note 261.

Run: python scripts/abel_prime_atom_audit.py

Locations are positive rationals representing exponentiated logarithmic lags.
Weights and convolution arithmetic use fractions.Fraction. The checks cover
finite prime-power supports, two positive rational weight patterns, and
negative, zero, and positive discrepancy-center coefficients. No floating
point logarithms, numerical von Mangoldt weights, or asymptotic inference
are used. Continuous-density bounds and Abel-mass oscillation are proved
separately in the note, not tested by this finite calculation.
"""

from fractions import Fraction as F
from math import isqrt


def primes_up_to(limit):
    """Trial division is sufficient for the deliberately small audit inputs."""
    return [n for n in range(2, limit + 1)
            if all(n % d for d in range(2, isqrt(n) + 1))]


def prime_powers_up_to(limit):
    powers = set()
    for prime in primes_up_to(limit):
        power = prime
        while power <= limit:
            powers.add(power)
            power *= prime
    return sorted(powers)


def symmetric_atomic(weights, center):
    """sum_n a_n/2 (delta_n + delta_(1/n)) - center delta_1."""
    result = {F(1): -F(center)}
    for n, weight in weights.items():
        result[F(n)] = result.get(F(n), F(0)) + weight / 2
        inverse = F(1, n)
        result[inverse] = result.get(inverse, F(0)) + weight / 2
    return {x: coefficient for x, coefficient in result.items() if coefficient}


def multiplicative_convolution(left, right):
    result = {}
    for x, a in left.items():
        for y, b in right.items():
            location = x * y
            result[location] = result.get(location, F(0)) + a * b
    return {x: coefficient for x, coefficient in result.items() if coefficient}


def check_spacing(location, target, limit):
    """Check |log(location)-log(target)| >= log(1 + limit**(-3)).

    For location=u/v and integer target=q**3, the two distinct integers
    u and v*target have minimum at most u <= limit**3. Their ratio therefore
    satisfies the stated inequality. The cross-multiplication below checks
    that implication with exact integers, independently of taking logs.
    """
    assert target.denominator == 1
    u, v = location.numerator, location.denominator
    assert 1 <= u <= limit ** 3
    assert 1 <= v <= limit ** 3
    left, right = u, v * target.numerator
    assert left != right
    small, large = min(left, right), max(left, right)
    assert small <= limit ** 3
    assert large * limit ** 3 >= small * (limit ** 3 + 1)


def audit_case(limit, weights, discrepancy_center, source_center):
    atomic_r = symmetric_atomic(weights, discrepancy_center)
    atomic_p = symmetric_atomic(weights, source_center)
    response = multiplicative_convolution(
        multiplicative_convolution(atomic_r, atomic_r), atomic_p)

    # This checks every surviving atom, not only atoms adjacent to q**3.
    for location in response:
        assert location.numerator <= limit ** 3
        assert location.denominator <= limit ** 3

    targets = [q for q in primes_up_to(limit) if q * q > limit]
    assert targets
    spacing_checks = 0
    for q in targets:
        target = F(q ** 3)
        expected = weights[q] ** 3 / 8
        assert response.get(target, F(0)) == expected, (
            limit, q, discrepancy_center, source_center,
            response.get(target), expected)
        assert expected > 0
        for location in response:
            if location != target:
                check_spacing(location, target, limit)
                spacing_checks += 1
    return len(targets), spacing_checks


def main():
    case_count = atom_checks = spacing_checks = 0
    for limit in (8, 12, 25, 40):
        powers = prime_powers_up_to(limit)
        weight_patterns = (
            {n: F(n % 7 + 1, n + 1) for n in powers},
            {n: F((3 * n) % 11 + 2, n + 2) for n in powers},
        )
        limit_cases = 0
        for weights in weight_patterns:
            total = sum(weights.values(), F(0))
            # The first p-center equals the actual source mass. The other
            # two deliberately test the stronger, arbitrary-center identity.
            centers = ((F(-3, 5), total), (F(0), F(5, 7)),
                       (F(7, 4), F(-2, 9)))
            for discrepancy_center, source_center in centers:
                atoms, spacings = audit_case(
                    limit, weights, discrepancy_center, source_center)
                case_count += 1
                limit_cases += 1
                atom_checks += atoms
                spacing_checks += spacings
        print(f"PASS N={limit}: {len(powers)} prime powers, "
              f"{limit_cases} rational-weight/center cases")
    print(f"PASS exact isolated-atom coefficients: {atom_checks}")
    print(f"PASS exact rational spacing inequalities: {spacing_checks}")
    print(f"PASS all {case_count} finite cases; no asymptotic inference")


if __name__ == "__main__":
    main()

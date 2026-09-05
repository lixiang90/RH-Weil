"""Exact finite audits for prime-power product and ratio energy identities.

Run with ``python -B scripts/prime_power_product_fiber_audit.py``.
All arithmetic is Fraction arithmetic; no floating-point tolerance is used.
These finite tests are evidence [E], not proofs of an asymptotic assertion.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction


ZERO = Fraction(0)
Source = dict[int, Fraction]


def prime_power_coordinates(n: int) -> tuple[int, int] | None:
    """Return (p, k) for n = p**k, or None, by trial division."""
    if n < 2:
        return None
    p = 2
    while p * p <= n and n % p:
        p += 1
    if p * p > n:
        return n, 1
    quotient, exponent = n, 0
    while quotient % p == 0:
        quotient //= p
        exponent += 1
    return (p, exponent) if quotient == 1 else None


def weighted_source(limit: int, variant: int = 0) -> Source:
    """Bounded rational weights g_p p**(-k)/(1+p**k), sigma = 1."""
    result: Source = {}
    for n in range(2, limit + 1):
        coordinates = prime_power_coordinates(n)
        if coordinates is not None:
            p, _ = coordinates
            g_p = Fraction(1 + (p + 2 * variant) % 5, 6 + variant)
            result[n] = g_p / (n * (1 + n))
    return result


def restrict(source: Source, members: set[int]) -> Source:
    return {n: weight for n, weight in source.items() if n in members}


def square_mass(source: Source) -> Fraction:
    return sum((weight * weight for weight in source.values()), ZERO)


def fourth_diagonal(source: Source) -> Fraction:
    return sum((weight**4 for weight in source.values()), ZERO)


def direct_products(left: Source, right: Source) -> dict[int, Fraction]:
    """Aggregate ordered pairs at their integer product, without fibers."""
    result: dict[int, Fraction] = defaultdict(Fraction)
    for u, a_u in left.items():
        for v, b_v in right.items():
            result[u * v] += a_u * b_v
    return dict(result)


def direct_ratios(source: Source) -> dict[Fraction, Fraction]:
    """Aggregate ordered pairs at exact reduced Fraction ratios."""
    result: dict[Fraction, Fraction] = defaultdict(Fraction)
    for u, a_u in source.items():
        for v, a_v in source.items():
            result[Fraction(u, v)] += a_u * a_v
    return dict(result)


def coefficient_energy(coefficients: dict) -> Fraction:
    return sum((coefficient**2 for coefficient in coefficients.values()), ZERO)


def chain_excess(source: Source) -> Fraction:
    """Compute E by its separate one-prime chain formula, including holes.

    The indices j+h and k are allowed to coincide.  In particular, j=h=1,
    k=2 contributes 4*a_p*a_(p**2)**2*a_(p**3).
    """
    chains: dict[int, dict[int, Fraction]] = defaultdict(dict)
    for n, weight in source.items():
        coordinates = prime_power_coordinates(n)
        if coordinates is None:
            raise ValueError(f"Not a prime power: {n}")
        p, exponent = coordinates
        chains[p][exponent] = weight
    excess = ZERO
    for chain in chains.values():
        last = max(chain)
        for h in range(1, last):
            for j in range(1, last - h + 1):
                for k in range(j + 1, last - h + 1):
                    excess += (
                        4
                        * chain.get(j, ZERO)
                        * chain.get(j + h, ZERO)
                        * chain.get(k, ZERO)
                        * chain.get(k + h, ZERO)
                    )
    return excess


def require_equal(label: str, actual: Fraction, expected: Fraction) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: actual={actual}, expected={expected}")


def check_energy_identities(name: str, source: Source) -> None:
    q = square_mass(source)
    d4 = fourth_diagonal(source)
    excess = chain_excess(source)
    products = direct_products(source, source)
    ratios = direct_ratios(source)
    product_energy = coefficient_energy(products)
    nonunit_ratio_energy = sum(
        (coefficient**2 for ratio, coefficient in ratios.items() if ratio != 1),
        ZERO,
    )
    require_equal(f"{name}: product energy", product_energy, 2 * q**2 - d4 + excess)
    require_equal(
        f"{name}: nonunit ratio energy", nonunit_ratio_energy, q**2 - d4 + excess
    )
    require_equal(f"{name}: unit ratio coefficient", ratios.get(Fraction(1), ZERO), q)
    require_equal(f"{name}: product/ratio energy", product_energy, coefficient_energy(ratios))


def subset_cases(variant: int = 0) -> list[tuple[str, Source]]:
    base = weighted_source(128, variant)
    keys = set(base)
    cases: list[tuple[str, Source]] = [("empty", {})]
    for limit in (2, 4, 7, 8, 16, 32, 64, 128):
        cases.append((f"prefix_{limit}", {n: w for n, w in base.items() if n <= limit}))
    fixed = {
        "first_collision_p2": {2, 4, 8},
        "first_collision_p3": {3, 9, 27},
        "deleted_middle": {2, 8},
        "one_prime_with_holes": {2, 4, 16, 32},
        "late_three_term_chain": {32, 64, 128},
        "single_high_power": {64},
        "several_prime_chains": {2, 4, 8, 3, 9, 27, 5, 25, 125},
    }
    for name, members in fixed.items():
        cases.append((name, restrict(base, members)))
    primes = {n for n in keys if prime_power_coordinates(n)[1] == 1}
    cases.extend((
        ("primes_only", restrict(base, primes)),
        ("higher_powers_only", restrict(base, keys - primes)),
    ))
    for offset in range(4):
        members = {n for n in keys if (3 * n + offset) % 7 in {0, 1, 3}}
        cases.append((f"arbitrary_mask_{offset}", restrict(base, members)))
    return cases


def check_mixed_bound(name: str, left: Source, right: Source) -> None:
    # sigma=1 gives max(2, (1+1/4)/(1-1/4)) = 2 exactly.
    constant = max(Fraction(2), (1 + Fraction(1, 4)) / (1 - Fraction(1, 4)))
    actual = coefficient_energy(direct_products(left, right))
    budget = constant * square_mass(left) * square_mass(right)
    if actual > budget:
        raise AssertionError(f"{name}: mixed product energy {actual} exceeds {budget}")


def main() -> None:
    cases_a = subset_cases()
    cases_b = subset_cases(variant=1)
    for name, source in cases_a + [(f"variant_1/{n}", s) for n, s in cases_b]:
        check_energy_identities(name, source)

    by_name = dict(cases_a)
    require_equal("no p**3 below 8", chain_excess(by_name["prefix_7"]), ZERO)
    require_equal("deleted middle destroys collision", chain_excess(by_name["deleted_middle"]), ZERO)
    first = by_name["first_collision_p2"]
    first_excess = 4 * first[2] * first[4] ** 2 * first[8]
    require_equal("first collision, repeated middle index", chain_excess(first), first_excess)
    if first_excess <= 0 or chain_excess(by_name["one_prime_with_holes"]) <= 0:
        raise AssertionError("Required collision coverage is missing")

    mixed_indices = [(0, 8), (8, 0), (8, 8), (17, 18), (18, 17), (9, 10), (13, 8)]
    mixed_indices += [(i, (5 * i + 3) % len(cases_b)) for i in range(9)]
    for i, j in mixed_indices:
        name_a, source_a = cases_a[i]
        name_b, source_b = cases_b[j]
        check_mixed_bound(f"{name_a} x variant_1/{name_b}", source_a, source_b)

    print(f"PASS: {len(cases_a) + len(cases_b)} exact product/ratio/chain identity cases")
    print(f"PASS: {len(mixed_indices)} exact mixed-source C_sigma=2 bounds")
    print("PASS: no-cube, first-collision, repeated-middle, holes, and late-chain coverage")
    print("Arithmetic: fractions.Fraction only; N <= 128; finite evidence [E]")


if __name__ == "__main__":
    main()

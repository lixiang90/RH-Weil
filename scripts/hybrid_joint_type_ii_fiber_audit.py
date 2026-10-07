"""Exact small-domain audit for the joint Type-II determinant-fiber report.

Prints JSON only. Formal log(p) bases keep the convolution checks integral.
This certifies finite identities, not asymptotic estimates or a zero proportion.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


REPORT = "reviews/2026-10-07/hybrid-joint-type-ii-fiber-research.md"
EXPECTED_REPORT_SHA256 = "238fd374cad6da451fd186c6f3766d79d869ff8ae92ed6441e0ca516e1398473"
DOMAIN_FIRST = 12
DOMAIN_LAST = 22
V = 3


def factorization(n: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    prime = 2
    while prime * prime <= n:
        exponent = 0
        while n % prime == 0:
            n //= prime
            exponent += 1
        if exponent:
            factors.append((prime, exponent))
        prime += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def mobius(n: int) -> int:
    factors = factorization(n)
    if any(exponent > 1 for _, exponent in factors):
        return 0
    return (-1) ** len(factors)


def formal_lambda(n: int) -> dict[int, int]:
    factors = factorization(n)
    return {factors[0][0]: 1} if len(factors) == 1 else {}


def divisors(n: int) -> list[int]:
    return [divisor for divisor in range(1, n + 1) if n % divisor == 0]


def add_scaled(target: dict, source: dict, scale: int) -> None:
    for basis, coefficient in source.items():
        target[basis] = target.get(basis, 0) + scale * coefficient
        if not target[basis]:
            del target[basis]


def tensor(left: dict[int, int], right: dict[int, int]) -> dict[tuple[int, int], int]:
    return {
        (left_prime, right_prime): left_coefficient * right_coefficient
        for left_prime, left_coefficient in left.items()
        for right_prime, right_coefficient in right.items()
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    report_bytes = (root / REPORT).read_bytes()
    canonical_bytes = report_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    report_hash = hashlib.sha256(canonical_bytes).hexdigest()
    assert report_hash == EXPECTED_REPORT_SHA256, "Final report hash mismatch"

    mu = {n: mobius(n) for n in range(1, DOMAIN_LAST + 1)}
    lam = {n: formal_lambda(n) for n in range(1, DOMAIN_LAST + 1)}
    div = {n: divisors(n) for n in range(1, DOMAIN_LAST + 1)}
    completion: dict[int, dict[int, int]] = {}
    for n in range(1, DOMAIN_LAST + 1):
        completion[n] = {}
        for prime_power in div[n]:
            if prime_power > V:
                add_scaled(completion[n], lam[prime_power], 1)

    domain = range(DOMAIN_FIRST, DOMAIN_LAST + 1)
    for a in domain:
        reconstructed: dict[int, int] = {}
        for r in div[a]:
            add_scaled(reconstructed, completion[a // r], mu[r])
        assert reconstructed == lam[a], (a, reconstructed, lam[a])

    physical_quadruples = 0
    signed_divisor_terms = 0
    denominator_core_rows = 0
    full_physical_core_rows = 0
    shared_divisor_terms = 0
    for a in domain:
        for b in domain:
            if math.gcd(a, b) > 1:
                continue
            for c in domain:
                for d in domain:
                    if math.gcd(c, d) > 1:
                        continue
                    h = a * d - b * c
                    if not h:
                        assert (a, b) == (c, d), "Primitive diagonal equivalence"
                        continue
                    physical_quadruples += 1
                    in_core = abs(h) < DOMAIN_FIRST
                    if in_core and lam[b] and lam[d]:
                        denominator_core_rows += 1
                        assert math.gcd(b, d) == 1, "Denominator core coprimality"
                        if lam[a] and lam[c]:
                            full_physical_core_rows += 1
                            assert math.gcd(a, c) == 1, "Physical numerator core"

                    reconstructed_tensor: dict[tuple[int, int], int] = {}
                    for r in div[a]:
                        if not mu[r]:
                            continue
                        for s in div[c]:
                            if not mu[s]:
                                continue
                            signed_divisor_terms += 1
                            add_scaled(
                                reconstructed_tensor,
                                tensor(completion[a // r], completion[c // s]),
                                mu[r] * mu[s],
                            )
                            g = math.gcd(r, s)
                            u, v = r // g, s // g
                            if g > 1:
                                shared_divisor_terms += 1
                            assert h % g == 0
                            assert math.gcd(u, v) == 1
                            assert math.gcd(g, u) == math.gcd(g, v) == 1
                            assert mu[r] * mu[s] == mu[u] * mu[v]
                            q = math.gcd(b, d)
                            assert math.gcd(g, q) == 1
                            assert h % (g * q) == 0
                            b0, d0 = b // q, d // q
                            a_completion, c_completion = a // r, c // s
                            assert math.gcd(u * d0, v * b0) == 1
                            m = h // (g * q)
                            modulus = v * b0
                            a0 = (
                                (m * pow(u * d0, -1, modulus)) % modulus
                                if modulus > 1
                                else 0
                            )
                            c0 = (u * d0 * a0 - m) // modulus
                            assert (a_completion - a0) % modulus == 0
                            ell = (a_completion - a0) // modulus
                            assert c_completion == c0 + u * d0 * ell
                            assert u * a_completion * d0 - v * b0 * c_completion == m
                            # Exact scaled ratio equality; no floating-point logs.
                            assert (
                                a * d * v * b0 * c_completion
                                == b * c * u * a_completion * d0
                            )
                    assert reconstructed_tensor == tensor(lam[a], lam[c])

    print(
        json.dumps(
            {
                "status": "PASS",
                "scope": "finite integer and formal-log identities only",
                "report": REPORT,
                "report_canonical_lf_sha256": report_hash,
                "domain": [DOMAIN_FIRST, DOMAIN_LAST],
                "V": V,
                "formal_basis": "ordered log(p) tensor log(q) with integer coefficients",
                "physical_nonzero_determinant_quadruples": physical_quadruples,
                "nonzero_mobius_divisor_terms": signed_divisor_terms,
                "shared_divisor_terms": shared_divisor_terms,
                "denominator_prime_power_core_rows": denominator_core_rows,
                "full_physical_prime_power_core_rows": full_physical_core_rows,
                "checks": {
                    "canonical_completion": True,
                    "physical_tensor_reconstruction": True,
                    "primitive_diagonal_equivalence": True,
                    "gq_divides_h": True,
                    "mobius_common_sign_square": True,
                    "affine_solution_reconstruction": True,
                    "scaled_actual_ratio": True,
                    "core_coprimality": True,
                },
                "not_certified": [
                    "asymptotic signed cancellation",
                    "Type-II tail saving",
                    "finite fourth-moment constant",
                    "new zero proportion",
                    "external zero-free input",
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

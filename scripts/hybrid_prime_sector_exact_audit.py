"""Finite exact algebra for high/low prime sectors and a specified reference.

No analytic estimate, infinite prime sum, or actual prime correlation is tested.
"""

from collections import Counter
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/hybrid-prime-sector-exact-audit.json"
INPUTS = [
    "notes/452-subquarter-padding-and-fourth-trace-stability.md",
    "notes/453-explicit-low-prime-fourth-moment-budget.md",
    "reviews/2026-10-07/hybrid-high-prime-four-word-response-research.md",
    "reviews/2026-10-07/hybrid-physical-determinant-average-research.md",
    "reviews/2026-10-07/hybrid-critical-neighborhood-mixed-witness-research.md",
]


def binding(path):
    data = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
        "canonical_utf8_bytes": len(data),
    }


def cyclic(word):
    return min(word[j:] + word[:j] for j in range(len(word)))


def partition_identity(labels):
    expected, rhs = Counter(), Counter()
    for word in product(labels, repeat=4):
        if len(set(word)) < 4:
            expected[cyclic(word)] += 1
    for p, a, b in product(labels, repeat=3):
        rhs[cyclic((p, p, a, b))] += 4
        rhs[cyclic((p, a, p, b))] += 2
    for p, q in product(labels, repeat=2):
        rhs[cyclic((p, p, q, q))] -= 2
        rhs[cyclic((p, q, p, q))] -= 1
        rhs[cyclic((p, p, p, q))] -= 8
    for p in labels:
        rhs[cyclic((p, p, p, p))] += 6
    assert {w: c for w, c in rhs.items() if c} == dict(expected)
    return {"labels": len(labels), "ordered_words": len(labels) ** 4, "cyclic_classes": len(expected)}


def low_coefficient_identity(primes, weighted):
    # Coefficients in commuting formal variables b_p, with integer product n
    # retaining all prime-factor collisions. This is a finite symbolic model.
    coefficients = {}
    for i, p in enumerate(primes):
        for j, q in enumerate(primes):
            exponent = tuple(int(k == i) + int(k == j) for k in range(len(primes)))
            coefficients.setdefault(p * q, Counter())[exponent] += 1
    actual, expected = Counter(), Counter()
    for n, poly in coefficients.items():
        for e1, c1 in poly.items():
            for e2, c2 in poly.items():
                actual[tuple(a + b for a, b in zip(e1, e2))] += c1 * c2 * (n if weighted else 1)
    for i, p in enumerate(primes):
        for j, q in enumerate(primes):
            e = tuple(2 * int(k == i) + 2 * int(k == j) for k in range(len(primes)))
            expected[e] += 2 * (p * q if weighted else 1)
        diag = tuple(4 * int(k == i) for k in range(len(primes)))
        expected[diag] -= p * p if weighted else 1
    assert dict(actual) == dict(expected)
    return {"weighted": weighted, "primes": primes, "product_columns": len(coefficients)}


def local_factor(p, h):
    return Q(p, p - 1) if h % p == 0 else Q(p * (p - 2), (p - 1) ** 2)


def certify():
    partitions = [partition_identity(tuple(range(n))) for n in range(1, 5)]
    collisions = [low_coefficient_identity([2, 3, 5, 7], w) for w in [False, True]]
    # d(v)=(v+v^2)/2 on [0,1/2]; integrate its squared polynomial exactly.
    symbol_square = 2 * (Q(1, 2)**3 / 3 + 2 * Q(1, 2)**4 / 4 + Q(1, 2)**5 / 5) / 4
    assert symbol_square == Q(19, 480)
    low_flat_upper = 16 * Q(3, 16) * Q(1, 2)**4
    assert low_flat_upper == Q(3, 16)
    primes = [2, 3, 5, 7, 11, 13]
    residue_checks = 0
    for p in primes:
        counts = Counter((a*d-b*c) % p for a, b, c, d in product(range(1, p), repeat=4))
        for h in range(p):
            expected = (p - 1)**3 if h == 0 else (p - 1)**2 * (p - 2)
            assert counts[h] == expected
            assert Q(p * counts[h], (p - 1)**4) == local_factor(p, h)
            residue_checks += 1
    period = prod(primes)
    finite_mean_sum = sum((prod(local_factor(p, h) for p in primes) for h in range(period)), Q(0))
    assert finite_mean_sum == period
    return {
        "status": "PASS: finite exact algebra only",
        "cyclic_partition_models": partitions,
        "finite_symbolic_prime_product_models": collisions,
        "indicator_symbol_square_integral": str(symbol_square),
        "indicator_repeated_high_upper": str(4 * symbol_square),
        "flat_low_scalar_jensen_upper": str(low_flat_upper),
        "local_residue_checks": residue_checks,
        "finite_euler_period": period,
        "finite_euler_factor_sum": str(finite_mean_sum),
        "not_certified": [
            "Hilbert mean-value estimates, projection leakage and infinite tails",
            "actual high-prime distinct or low/high mixed correlations",
            "infinite singular series asymptotic and physical four-point condition",
            "critical mixed-witness power saving, zero-free boundary, proportions or RH",
            "imported source or external kernels",
        ],
        "inputs_read_and_hashed_from_disk": [binding(ROOT / p) for p in INPUTS],
        "script_read_and_hashed_from_disk": binding(Path(__file__).resolve()),
    }


if __name__ == "__main__":
    result = certify()
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "repeated_high_upper": result["indicator_repeated_high_upper"],
        "low_upper": result["flat_low_scalar_jensen_upper"],
        "local_residue_checks": result["local_residue_checks"],
        "output": str(OUT),
    }, ensure_ascii=False))

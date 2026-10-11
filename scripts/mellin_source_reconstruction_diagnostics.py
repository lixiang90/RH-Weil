"""Bounded exact and floating diagnostics for the new interfaces in 518--520.

The analytic infinite statements are proved in the notes.  These checks are
neither interval certificates nor Lean proofs.  The finite Jordan models are
hypothetical; they do not assert a multiple zero of the Riemann zeta function.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
NOTES = (
    "notes/518-f1-quantitative-mellin-division-and-mobius-source.md",
    "notes/519-f1-closed-source-image-and-degree-moments.md",
    "notes/520-f1-source-quotient-spectrum-and-centered-growth.md",
)
GAUSSIAN_TERMS = 12
MOBIUS_CUTOFFS = (16, 32, 48)


def lf_sha256(path: Path) -> str:
    source = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def mobius_values(bound: int) -> list[int]:
    """Integer sieve, including the convention mu(1)=1."""
    values = [1] * (bound + 1)
    values[0] = 0
    prime_flags = [True] * (bound + 1)
    for prime in range(2, bound + 1):
        if not prime_flags[prime]:
            continue
        for multiple in range(prime, bound + 1, prime):
            values[multiple] *= -1
            if multiple != prime:
                prime_flags[multiple] = False
        for multiple in range(prime * prime, bound + 1, prime * prime):
            values[multiple] = 0
    return values


def identity(size: int):
    return [[Fraction(row == column) for column in range(size)] for row in range(size)]


def matrix_add(left, right):
    return [[a + b for a, b in zip(x, y)] for x, y in zip(left, right)]


def matrix_scale(scalar, matrix):
    return [[scalar * entry for entry in row] for row in matrix]


def matrix_mul(left, right):
    size = len(left)
    return [
        [sum(left[row][k] * right[k][column] for k in range(size)) for column in range(size)]
        for row in range(size)
    ]


def matrix_power(matrix, exponent: int):
    result = identity(len(matrix))
    for _ in range(exponent):
        result = matrix_mul(result, matrix)
    return result


def matrix_rank(matrix) -> int:
    work = [row[:] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scalar = work[rank][column]
        work[rank] = [entry / scalar for entry in work[rank]]
        for row in range(len(work)):
            if row != rank:
                scalar = work[row][column]
                work[row] = [x - scalar * y for x, y in zip(work[row], work[rank])]
        rank += 1
    return rank


def nilpotent_exponential(matrix, parameter: Fraction):
    result = matrix_scale(Fraction(0), identity(len(matrix)))
    for exponent in range(len(matrix)):
        result = matrix_add(
            result,
            matrix_scale(parameter**exponent / factorial(exponent), matrix_power(matrix, exponent)),
        )
    return result


def polynomial_add(left, right):
    size = max(len(left), len(right))
    return [
        (left[k] if k < len(left) else 0) + (right[k] if k < len(right) else 0)
        for k in range(size)
    ]


def polynomial_mul(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def polynomial_eval(coefficients, point: Fraction):
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * point + coefficient
    return result


def divide_linear(coefficients, point: Fraction):
    """Independent exact synthetic division by s-point."""
    work = coefficients[:]
    quotient = [Fraction(0)] * (len(work) - 1)
    for degree in range(len(work) - 1, 0, -1):
        quotient[degree - 1] = work[degree]
        work[degree - 1] += point * work[degree]
    return quotient, work[0]


def theta_zero(radius):
    if not radius:
        return mp.mpf(0)
    z = mp.pi * radius**2
    return z * (z - mp.mpf("1.5")) * mp.exp(-z)


def positive_periodization(radius):
    """Used only at radius>=1; the Gaussian sum is deliberately finite."""
    return 2 * mp.fsum(theta_zero(n * radius) for n in range(1, GAUSSIAN_TERMS + 1))


def target_at_radius(radius):
    """Poisson/sharp relation pays the negative-log argument stably."""
    if radius >= 1:
        return positive_periodization(radius)
    return positive_periodization(1 / radius) / radius


def source_mellin_closed(s):
    if s == 0:
        return mp.mpf("-0.25")
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) / 8


def target_mellin_closed(s):
    if s in (0, 1):
        return mp.mpf("0.25")
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s) / 4


def source_integral(function):
    return mp.quad(function, [0, mp.mpf("0.25"), 1, 2, 4, mp.inf])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=60)
    parser.add_argument("--output", default="reviews/2026-10-11/f1-mellin-source-diagnostics.json")
    args = parser.parse_args()
    if args.precision < 40:
        parser.error("Use at least 40 decimal digits.")
    mp.mp.dps = args.precision
    tolerance = mp.power(10, -(args.precision - 15))
    checks = []

    def exact(check_id, observed, expected):
        checks.append({
            "id": check_id, "kind": "exact_finite_rational_or_integer",
            "passed": observed == expected,
            "observed": str(observed), "expected": str(expected),
        })

    def floating(check_id, observed, expected, limit=None, detail=None):
        limit = tolerance if limit is None else limit
        error = abs(observed - expected)
        record = {
            "id": check_id, "kind": "non_interval_mpmath_floating",
            "passed": bool(error <= limit),
            "observed": mp.nstr(observed, 35), "expected": mp.nstr(expected, 35),
            "absolute_error": mp.nstr(error, 8), "tolerance": mp.nstr(limit, 8),
        }
        if detail is not None:
            record["detail"] = detail
        checks.append(record)

    # Source Mellin integrals and genuine two-degree source integrals.
    for s in (mp.mpf("0.7"), mp.mpf(1), mp.mpf(2), mp.mpc(2, "0.9"), mp.mpc(-1, "0.4")):
        value = source_integral(lambda r: theta_zero(r) * mp.power(r, s - 1) if r else 0)
        floating(f"gaussian_source_mellin_{s}", value, source_mellin_closed(s))

    floating("source_zero_integral", source_integral(theta_zero), mp.mpf(0))
    c_value = -source_integral(lambda r: theta_zero(r) / r if r else 0)
    d_value = 2 * source_integral(lambda r: theta_zero(r) * mp.log(r) if r else 0)
    floating("source_degree_c_negative_dr_over_r", c_value, mp.mpf("0.25"))
    floating("source_degree_d_twice_log_r_dr", d_value, mp.mpf("0.25"))

    # The split formula is the actual target Mellin integral, with Poisson on r<1.
    for s in (mp.mpf(0), mp.mpf(1), mp.mpf("0.7"), mp.mpf(2), mp.mpc(2, "0.9")):
        value = mp.quad(
            lambda r: positive_periodization(r) * (mp.power(r, s - 1) + mp.power(r, -s)),
            [1, 2, 4, mp.inf],
        )
        floating(
            f"actual_target_H0_mellin_{s}", value, target_mellin_closed(s),
            detail={"positive_gaussian_terms": GAUSSIAN_TERMS, "negative_log_via_poisson": True},
        )

    mu = mobius_values(96)
    for integer in range(1, 97):
        divisor_sum = sum(mu[d] for d in range(1, integer + 1) if integer % d == 0)
        exact(f"mobius_divisor_identity_{integer}", divisor_sum, int(integer == 1))

    for radius in (mp.mpf("0.3"), mp.mpf("0.8"), mp.mpf("1.4")):
        direct_periodization = 2 * mp.fsum(theta_zero(n * radius) for n in range(1, 65))
        floating(
            f"poisson_periodization_at_{radius}", target_at_radius(radius), direct_periodization,
            detail={"direct_gaussian_terms": 64, "stable_target_terms": GAUSSIAN_TERMS},
        )
        for cutoff in MOBIUS_CUTOFFS:
            rebuilt = mp.fsum(mu[n] * target_at_radius(n * radius) for n in range(1, cutoff + 1)) / 2
            limit = max(tolerance, mp.mpf("1e-28")) if cutoff == 16 else tolerance
            floating(
                f"actual_mobius_source_at_{radius}_N{cutoff}", rebuilt, theta_zero(radius), limit,
                {"mobius_cutoff": cutoff, "target_terms": GAUSSIAN_TERMS,
                 "negative_log_target_uses_poisson": True},
            )

    # Negative-even residues: actual target value via xi symmetry, numerical zeta derivative.
    for k in range(1, 5):
        residue = target_mellin_closed(1 + 2 * k) / (2 * mp.diff(mp.zeta, -2 * k))
        taylor_coefficient = mp.pi**k * (-1)**k * (mp.mpf(k) + mp.mpf("0.5")) / factorial(k - 1)
        gamma_residue = mp.pi**k * (-1)**k * (2 * k) * (2 * k + 1) / (4 * factorial(k))
        floating(f"trivial_zero_residue_vs_source_taylor_k{k}", residue, taylor_coefficient)
        floating(f"gamma_residue_vs_source_taylor_k{k}", gamma_residue, taylor_coefficient)

    # Hypothetical finite Jordan blocks: no claim about actual multiple zeta zeros.
    for size in range(1, 5):
        nilpotent = [[Fraction(column == row + 1) for column in range(size)] for row in range(size)]
        for exponent in range(1, size + 2):
            dimension = size - matrix_rank(matrix_power(nilpotent, exponent))
            exact(f"hypothetical_jordan_kernel_m{size}_k{exponent}", dimension, min(size, exponent))
        first, second = Fraction(2, 3), Fraction(-5, 7)
        exact(
            f"hypothetical_jordan_group_law_m{size}",
            matrix_mul(nilpotent_exponential(nilpotent, first), nilpotent_exponential(nilpotent, second)),
            nilpotent_exponential(nilpotent, first + second),
        )
        parameter = Fraction(2, 3)
        inverse = matrix_scale(Fraction(0), identity(size))
        for exponent in range(size):
            inverse = matrix_add(
                inverse, matrix_scale(-parameter ** (-exponent - 1), matrix_power(nilpotent, exponent)),
            )
        operator = matrix_add(nilpotent, matrix_scale(-parameter, identity(size)))
        exact(f"hypothetical_jordan_left_resolvent_m{size}", matrix_mul(operator, inverse), identity(size))
        exact(f"hypothetical_jordan_right_resolvent_m{size}", matrix_mul(inverse, operator), identity(size))

        # A polynomial analogue of the h0 correction and its paid one-factor division.
        rho, lam = Fraction(1, 2), Fraction(3, 2)
        h_polynomial = [Fraction(1)]
        for _ in range(size):
            h_polynomial = polynomial_mul(h_polynomial, [-rho, Fraction(1)])
        original = [Fraction(1), Fraction(2), Fraction(3)]
        correction = polynomial_eval(original, lam) / polynomial_eval(h_polynomial, lam)
        numerator = polynomial_add(original, [-correction * entry for entry in h_polynomial])
        quotient, remainder = divide_linear(numerator, lam)
        exact(f"hypothetical_corrected_mellin_numerator_m{size}", polynomial_eval(numerator, lam), Fraction(0))
        exact(f"hypothetical_mellin_division_remainder_m{size}", remainder, Fraction(0))
        recovered = polynomial_add(
            polynomial_mul([-lam, Fraction(1)], quotient),
            [correction * entry for entry in h_polynomial],
        )
        padded_original = original + [Fraction(0)] * (len(recovered) - len(original))
        exact(f"hypothetical_mellin_resolvent_identity_m{size}", recovered, padded_original)

    passed = sum(item["passed"] for item in checks)
    report = {
        "schema_version": 1,
        "research_date": "2026-10-11",
        "notes_lf_sha256": {name: lf_sha256(ROOT / name) for name in NOTES},
        "script_lf_sha256": lf_sha256(Path(__file__)),
        "precision_decimal_digits": args.precision,
        "gaussian_terms_for_radius_ge_one": GAUSSIAN_TERMS,
        "mobius_cutoffs": list(MOBIUS_CUTOFFS),
        "direct_poisson_comparison_terms": 64,
        "exact_mobius_maximum": 96,
        "hypothetical_jordan_block_sizes": [1, 2, 3, 4],
        "check_count": len(checks),
        "passed_count": passed,
        "failed_count": len(checks) - passed,
        "limitations": [
            "Floating checks are not interval certificates or Lean proofs.",
            "Finite Gaussian and Mobius sums do not certify infinite analytic statements.",
            "The infinite source, division and spectrum theorems, and only the conditional implication from the proposed growth bound, are proved in the notes.",
            "Jordan blocks are finite hypothetical models, not observations of multiple zeta zeros.",
            "No RH, independent subexponential bound, positive Hilbert realization, or global HH1 is certified.",
        ],
        "checks": checks,
    }
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "checks": len(checks), "passed": passed,
                      "failed": len(checks) - passed}, ensure_ascii=False))
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

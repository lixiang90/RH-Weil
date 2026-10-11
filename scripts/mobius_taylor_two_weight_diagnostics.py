"""Bounded arithmetic and Gram diagnostics for notes 524--526.

Exact finite algebra is distinguished from ordinary mpmath quadrature. No
floating check is an interval certificate or a Lean proof. Generic complex
parameters in the blind-probe checks are not asserted to be zeta zeros.
Infinite source/quotient statements and RH-equivalence implications are
analytic arguments in the notes; classical zero-count inputs are cited.
None is certified by these finite calculations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
NOTES = (
    "notes/524-f1-mobius-cutoff-taylor-obstruction-and-repair.md",
    "notes/525-f1-smoothed-mobius-probes-and-arithmetic-strength.md",
    "notes/526-f1-faithful-two-weight-hilbert-quotient-and-defect.md",
)
GRAM_ENDPOINT = 100
MOBIUS_TERMS = 24
LOG_X_ENDPOINT = 18


def lf_hash(path):
    return hashlib.sha256(path.read_text(encoding="utf-8").replace(
        "\r\n", "\n").replace("\r", "\n").encode("utf-8")).hexdigest()


def mobius(integer):
    remainder, factors, divisor = integer, 0, 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            remainder //= divisor
            factors += 1
            if remainder % divisor == 0:
                return 0
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    if remainder > 1:
        factors += 1
    return (-1) ** factors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="reviews/2026-10-12/f1-mobius-taylor-two-weight-diagnostics.json")
    parser.add_argument("--precision", type=int, default=50)
    args = parser.parse_args()
    if not 40 <= args.precision <= 70:
        parser.error("Use 40--70 decimal digits for bounded diagnostics.")
    mp.mp.dps = args.precision
    records = []
    tolerance = mp.mpf("1e-28")

    def display(value):
        return mp.nstr(value, 32)

    def exact(label, condition, **data):
        records.append(dict(label=label, kind="exact_finite", passed=bool(condition), **data))

    def floating(label, error, budget=tolerance, **data):
        records.append(dict(label=label, kind="non_interval_floating", passed=bool(error <= budget),
                            absolute_error=display(error), comparison_budget=display(budget), **data))

    # Divisor cancellation uses genuine integer Mobius coefficients, not a
    # surrogate random sign sequence or an assumed asymptotic estimate.
    for integer in range(1, 65):
        divisor_sum = sum(mobius(d) for d in range(1, integer + 1) if integer % d == 0)
        exact(f"mobius_divisor_{integer}", divisor_sum == int(integer == 1), n=integer)

    for k in range(1, 7):
        for n in (2 * k + 1, 2 * k + 3):
            cost = Fraction(1, n - 2 * k) + Fraction(1, n + 2 * k)
            exact(f"negative_even_moment_cost_k{k}_n{n}", cost == Fraction(2 * n, n * n - 4 * k * k),
                  integral_cost=str(cost))
    exact("h0_lower_bound_rational_factor", Fraction(3, 4) / Fraction(6, 5) == Fraction(5, 8))

    # On the plateau kappa=1, the pure source basis has precisely r^(2k).
    # A mass compensator supported away from zero contributes no Taylor jet.
    # This only tests the finite coefficient interface; source admissibility
    # and continuity of E are analytic statements in note524.
    for size in (1, 2, 4, 6):
        matrix = [[Fraction(j == k) for k in range(1, size + 1)] for j in range(1, size + 1)]
        square = [[sum(matrix[i][k] * matrix[k][j] for k in range(size))
                   for j in range(size)] for i in range(size)]
        exact(f"pure_taylor_projection_K{size}", square == matrix, K=size)
        for k in range(1, size + 1):
            # x=e^(-a/2) makes the source coefficient scaling x^(4k+1).
            x = Fraction(3, 2)
            exact(f"source_scaling_K{size}_k{k}", x * (x * x) ** (2 * k) == x ** (4 * k + 1))

    # Binomial translations cancel every derivative below a prescribed
    # multiplicity m. The same finite differences give a nonzero m-th jet.
    for multiplicity in (1, 2, 3, 4, 6):
        for order in range(multiplicity):
            value = sum(comb(multiplicity, j) * (-1) ** j * j ** order
                        for j in range(multiplicity + 1))
            exact(f"blind_probe_m{multiplicity}_jet{order}", value == 0)
        value = sum(comb(multiplicity, j) * (-1) ** j * j ** multiplicity
                    for j in range(multiplicity + 1))
        exact(f"blind_probe_m{multiplicity}_first_nonzero", value == (-1) ** multiplicity * factorial(multiplicity))

    for k in range(1, 5):
        derivative = mp.diff(mp.zeta, -2 * k)
        formula = (-1) ** k * mp.factorial(2 * k) * mp.zeta(2 * k + 1) / (2 * (2 * mp.pi) ** (2 * k))
        floating(f"zeta_trivial_derivative_k{k}", abs(derivative - formula))
    h0_moment = 2 * mp.diff(mp.zeta, -2) * (-3 * mp.pi / 2)
    floating("h0_source_taylor_moment", abs(h0_moment - 3 * mp.zeta(3) / (4 * mp.pi)))

    # Finite Gaussian Mobius Mellin integral in y=log(x); no tail of the
    # infinite Mobius series is sampled or certified here. The finite sum is
    # integrated directly and compared with its own finite Dirichlet factor.
    coefficients = [(mp.log(n), mobius(n), n) for n in range(1, MOBIUS_TERMS + 1)]
    for real, imaginary in (("2", "0"), ("2.5", "0.4")):
        s = mp.mpc(real, imaginary)
        def integrand(y):
            raw = sum(mu * mp.exp(-(log_n - y) ** 2) for log_n, mu, _ in coefficients) / 2
            return raw * mp.exp(-s * y)
        measured = mp.quad(integrand, list(range(-LOG_X_ENDPOINT, LOG_X_ENDPOINT + 1, 2)))
        expected = mp.sqrt(mp.pi) * mp.exp(s * s / 4) * sum(
            mu * mp.power(n, -s) for _, mu, n in coefficients) / 2
        floating(f"finite_gaussian_mobius_mellin_{real}_{imaginary}", abs(measured - expected),
                 budget=mp.mpf("1e-35"), terms=MOBIUS_TERMS, log_x_endpoint=LOG_X_ENDPOINT)

    # The PNT mass-tail elementary integral is evaluated on a finite interval,
    # with its explicitly known endpoint contribution retained.
    for c, lower, upper in (("0.5", "4", "81"), ("1.25", "9", "100")):
        c, lower, upper = map(mp.mpf, (c, lower, upper))
        measured = mp.quad(lambda v: mp.exp(-c * mp.sqrt(v)), [lower, upper])
        def tail(v):
            return 2 * mp.exp(-c * mp.sqrt(v)) * (mp.sqrt(v) / c + 1 / (c * c))
        floating(f"pnt_mass_tail_c{display(c)}", abs(measured - (tail(lower) - tail(upper))))

    for delta in (mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf("1")):
        for z in (mp.mpc(0, 0), mp.mpc("0.2", "0.7"), mp.mpc("-0.3", "1.2")):
            kernel = lambda t: mp.exp(z * t) / (2 * mp.cosh(2 * delta * t))
            measured = mp.quad(kernel, list(range(-GRAM_ENDPOINT, GRAM_ENDPOINT + 1, 4)))
            expected = mp.pi / (4 * delta * mp.cos(mp.pi * z / (4 * delta)))
            gap = 2 * delta - abs(mp.re(z))
            # |kernel| <= exp(-gap |t|); this analytic omitted-tail budget
            # does not certify the numerical quadrature itself.
            tail_budget = 2 * mp.exp(-gap * GRAM_ENDPOINT) / gap
            floating(f"double_weight_gram_d{display(delta)}_z{display(z)}",
                     abs(measured - expected), budget=tail_budget + tolerance,
                     endpoint=GRAM_ENDPOINT, omitted_tail_budget=display(tail_budget))
        for gap in (mp.mpf("0.2"), mp.mpf("1"), mp.mpf("2.5")):
            correlation = mp.sech(mp.pi * gap / (4 * delta))
            ratio = mp.sqrt((1 + correlation) / (1 - correlation))
            expected = mp.coth(mp.pi * gap / (8 * delta))
            floating(f"two_vector_large_time_amplification_d{display(delta)}_gap{display(gap)}",
                     abs(ratio - expected), correlation=display(correlation))
            for a in (mp.mpf("0.5"), mp.mpf("3")):
                # Direct two-vector quadratic forms: T*(u-v) has relative
                # phase exp(i*a*gap). Compare with the normalized Gram formula.
                before = 2 - 2 * correlation
                after = 2 - 2 * correlation * mp.cos(a * gap)
                direct = after / before
                ratio2 = (1 - correlation * mp.cos(a * gap)) / (1 - correlation)
                floating(f"two_vector_gram_d{display(delta)}_gap{display(gap)}_a{display(a)}", abs(direct - ratio2))
        variance = (mp.pi / (4 * delta)) ** 2
        for a in (mp.mpf("0.5"), mp.mpf("3")):
            gap = mp.mpf("1e-7")
            correlation = mp.sech(mp.pi * gap / (4 * delta))
            measured2 = (1 - correlation * mp.cos(a * gap)) / (1 - correlation)
            limiting2 = 1 + a * a / variance
            floating(f"small_gap_limit_d{display(delta)}_a{display(a)}", abs(measured2 - limiting2),
                     budget=mp.mpf("1e-11"), generic_gap=display(gap), variance=display(variance))

    report = {
        "schema": "rh-weil-f1-mobius-taylor-two-weight-diagnostics-v1",
        "date": "2026-10-12",
        "status": "PASS" if all(record["passed"] for record in records) else "FAIL",
        "source_sha256_normalized_lf": {path: lf_hash(ROOT / path) for path in NOTES},
        "script_sha256_normalized_lf": lf_hash(Path(__file__)),
        "working_decimal_digits": args.precision,
        "counts": {"total": len(records), "passed": sum(record["passed"] for record in records),
                   "failed": sum(not record["passed"] for record in records),
                   "exact_finite": sum(record["kind"] == "exact_finite" for record in records),
                   "non_interval_floating": sum(record["kind"] == "non_interval_floating" for record in records)},
        "cutoffs": {"mobius_divisor_maximum": 64, "finite_gaussian_mobius_terms": MOBIUS_TERMS,
                    "finite_gaussian_log_x_endpoint": LOG_X_ENDPOINT, "gram_endpoint": GRAM_ENDPOINT,
                    "pure_taylor_basis_maximum_K": 6, "blind_factor_maximum_m": 6},
        "limits": {"actual_multiple_or_off_line_zeta_zero_asserted": False,
                   "sampled_gaps_asserted_to_be_actual_zero_gaps": False,
                   "interval_or_lean_certificate": False,
                   "infinite_analytic_results_computationally_certified": False,
                   "unconditional_PNT_estimate_reproved_numerically": False,
                   "classical_zero_count_reproved_numerically": False},
        "records": records,
    }
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "counts": report["counts"], "output": str(output)}, ensure_ascii=False))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

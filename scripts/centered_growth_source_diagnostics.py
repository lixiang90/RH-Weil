"""Bounded diagnostics for the new interfaces in notes 521--523.

Only finite exact algebra and ordinary mpmath quadrature are checked.  Floating
calculations are neither interval certificates nor Lean proofs.  Hypothetical
Jordan blocks do not assert any multiple Riemann-zeta zero.  Infinite source,
resolvent, density and growth theorems are proved in the notes, not certified by
this script; no new RH proof or zero-free region is claimed.
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
    "notes/521-f1-moving-source-correction-and-uniform-resolvent.md",
    "notes/522-f1-optimal-centered-growth-and-rh-equivalence.md",
    "notes/523-f1-natural-hilbert-collapse-and-growth-gap.md",
)
E_CUTOFF = 4
GAUSSIAN_CUTOFF = 12
BROMWICH_CUTOFFS = (24, 48)


def lf_sha256(path):
    source = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def identity(size):
    return [[Fraction(i == j) for j in range(size)] for i in range(size)]


def scale(scalar, matrix):
    return [[scalar * entry for entry in row] for row in matrix]


def add(left, right):
    return [[a + b for a, b in zip(x, y)] for x, y in zip(left, right)]


def multiply(left, right):
    size = len(left)
    return [
        [sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size)]
        for i in range(size)
    ]


def power(matrix, exponent):
    result = identity(len(matrix))
    for _ in range(exponent):
        result = multiply(result, matrix)
    return result


def nilpotent(size):
    return [[Fraction(j == i + 1) for j in range(size)] for i in range(size)]


def nilpotent_exp(matrix, parameter):
    result = scale(Fraction(0), identity(len(matrix)))
    for k in range(len(matrix)):
        result = add(result, scale(parameter**k / factorial(k), power(matrix, k)))
    return result


def exact_resolvent(offset, nil, parameter):
    result = scale(Fraction(0), identity(len(nil)))
    for k in range(len(nil)):
        result = add(result, scale((parameter - offset) ** (-k - 1), power(nil, k)))
    return result


def mpmatrix(exact):
    return mp.matrix(
        [[mp.mpf(x.numerator) / x.denominator for x in row] for row in exact]
    )


def vector_norm(vector):
    return max(abs(entry) for entry in vector)


def split_quad(function, lower, upper):
    internal = [mp.mpf(x) for x in ("-6", "-3", "-1.5", "0", "1.5", "3", "6")]
    points = [lower] + [x for x in internal if lower < x < upper] + [upper]
    return mp.quad(function, points)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=50)
    parser.add_argument("--output", default="reviews/2026-10-11/f1-centered-growth-diagnostics.json")
    args = parser.parse_args()
    if not 40 <= args.precision <= 70:
        parser.error("Use 40--70 decimal digits for this bounded diagnostic.")
    mp.mp.dps = args.precision
    tolerance = mp.power(10, -(args.precision - 15))
    checks = []

    def number(value):
        return mp.nstr(value, 35)

    def exact_check(label, condition, **metadata):
        checks.append(
            {
                "label": label,
                "kind": "exact finite rational algebra",
                "passed": bool(condition),
                "metadata": metadata,
            }
        )

    def close_check(label, actual, expected, **metadata):
        error = abs(actual - expected)
        checks.append(
            {
                "label": label,
                "kind": "ordinary non-interval floating calculation",
                "passed": bool(error <= tolerance),
                "absolute_error": number(error),
                "tolerance": number(tolerance),
                "metadata": metadata,
            }
        )

    def bound_check(label, error, bound, **metadata):
        checks.append(
            {
                "label": label,
                "kind": "ordinary non-interval floating comparison with an analytic finite-model bound",
                "passed": bool(error <= bound + tolerance),
                "absolute_error": number(error),
                "computed_bound": number(bound),
                "rounding_tolerance": number(tolerance),
                "metadata": metadata,
            }
        )

    # A genuinely smooth compact source profile on (1,2), normalized by dr/r.
    def raw_profile(radius):
        if radius <= 1 or radius >= 2:
            return mp.mpf(0)
        q = (radius - 1) * (2 - radius)
        return mp.exp(-1 / q)

    profile_normalizer = mp.quad(
        lambda r: raw_profile(r) / r, [1, mp.mpf("1.25"), mp.mpf("1.5"), mp.mpf("1.75"), 2]
    )

    def profile(radius):
        return raw_profile(radius) / profile_normalizer

    def profile_derivative(radius):
        if radius <= 1 or radius >= 2:
            return mp.mpf(0)
        q = (radius - 1) * (2 - radius)
        return profile(radius) * (3 - 2 * radius) / q**2

    def theta(parameter, radius):
        if radius <= 1 or radius >= 2:
            return mp.mpc(0)
        return mp.power(radius, -parameter) * (
            (1 - parameter) * profile(radius) + radius * profile_derivative(radius)
        )

    source_points = [mp.mpf(x) for x in ("1", "1.25", "1.5", "1.75", "2")]

    def source_quad(function):
        return mp.quad(function, source_points)

    def z_entire(parameter):
        return mp.mpf(1) if parameter == 1 else (parameter - 1) * mp.zeta(parameter)

    close_check(
        "compact profile dr/r normalization",
        source_quad(lambda r: profile(r) / r),
        1,
        profile="C exp(-1/((r-1)(2-r))) on 1<r<2; zero elsewhere",
    )
    parameters = (
        mp.mpc("0.8", "0"),
        mp.mpc("0.8", "3"),
        mp.mpc("0.8", "8"),
        mp.mpc("1", "0"),
        mp.mpc("1.25", "3"),
    )
    for parameter in parameters:
        label = str(parameter)
        close_check(
            f"legal moving source zero integral, lambda={label}",
            2 * source_quad(lambda r: theta(parameter, r)),
            0,
            source_is_even=True,
            source_at_zero=0,
        )
        moment = source_quad(lambda r: mp.power(r, parameter - 1) * theta(parameter, r))
        close_check(
            f"moving source Mellin at lambda={label}",
            moment,
            1 - parameter,
            source_support=[1, 2],
        )
        if parameter == 1:
            derivative = source_quad(lambda r: mp.log(r) * theta(parameter, r))
            close_check(
                "lambda=1 pole removal gives target normalization -2",
                2 * derivative,
                -2,
                formula="2 residue(zeta,1) M_+theta_1'(1)",
            )
        else:
            close_check(
                f"target calibration -2 Z(lambda), lambda={label}",
                2 * mp.zeta(parameter) * moment,
                -2 * z_entire(parameter),
                normalization="Mh_lambda(lambda) = -2 (lambda-1) zeta(lambda)",
            )

    # A few source norm samples pay the explicit pointwise triangle bound only.
    # No grid is asserted to bound a continuous supremum, much less all heights.
    for height in (0, 3, 8):
        parameter = mp.mpc("0.8", height)
        sampled_ratio = mp.mpf(0)
        violation = mp.mpf(0)
        for k in range(1, 160):
            radius = 1 + mp.mpf(k) / 160
            value = abs(theta(parameter, radius))
            triangle = mp.power(radius, -mp.re(parameter)) * (
                abs(1 - parameter) * abs(profile(radius))
                + radius * abs(profile_derivative(radius))
            )
            sampled_ratio = max(sampled_ratio, value / (1 + height))
            violation = max(violation, value - triangle)
        bound_check(
            f"sampled source triangle inequality at height {height}",
            violation,
            0,
            grid_points=159,
            maximum_sampled_abs_theta_divided_by_1_plus_height=number(sampled_ratio),
            limitation="Samples do not certify a supremum or the all-height theorem.",
        )

    # Actual finite E periodization moment in logarithmic coordinates.
    parameter = mp.mpc("3.25", "0.6")
    e_moment = mp.mpc(0)
    for n in range(1, E_CUTOFF + 1):
        lower, upper = -mp.log(n), mp.log(2) - mp.log(n)
        midpoint = (lower + upper) / 2
        e_moment += mp.quad(
            lambda t, n=n: 2 * mp.exp(parameter * t) * theta(parameter, n * mp.exp(t)),
            [lower, midpoint, upper],
        )
    source_moment = source_quad(
        lambda r: mp.power(r, parameter - 1) * theta(parameter, r)
    )
    finite_dirichlet = mp.fsum(mp.power(n, -parameter) for n in range(1, E_CUTOFF + 1))
    close_check(
        "actual finite E log-integral has the Mellin factor 2",
        e_moment,
        2 * source_moment * finite_dirichlet,
        cutoff=E_CUTOFF,
        real_part=number(mp.re(parameter)),
    )
    e_tail = (
        2
        * abs(source_moment)
        * mp.power(E_CUTOFF, 1 - mp.re(parameter))
        / (mp.re(parameter) - 1)
    )
    bound_check(
        "finite E moment compared with target -2 Z(lambda)",
        abs(e_moment + 2 * z_entire(parameter)),
        e_tail,
        cutoff=E_CUTOFF,
        tail_formula="2 |M_+theta(lambda)| N^(1-Re lambda)/(Re lambda-1)",
        limitation="The absolute Dirichlet tail is evaluated in ordinary floating arithmetic.",
    )

    # Gaussian forcing is an actual S_exp example whose lambda moment is zero.
    # f=(D+lambda)g is chosen before applying R_lambda, independently of source calibration.
    def gaussian(t):
        return mp.exp(-t**2)

    def forcing(parameter, t):
        return (parameter - 2 * t) * gaussian(t)

    def forcing_derivative(parameter, t):
        return (4 * t**2 - 2 - 2 * parameter * t) * gaussian(t)

    gaussian_parameters = (mp.mpc("0.75", "0"), mp.mpc("1.2", "3"), mp.mpc("0.6", "8"))
    cutoff = mp.mpf(GAUSSIAN_CUTOFF)
    for parameter in gaussian_parameters:
        finite_moment = split_quad(
            lambda u: mp.exp(parameter * u) * forcing(parameter, u), -cutoff, cutoff
        )
        boundary_moment = gaussian(cutoff) * (
            mp.exp(parameter * cutoff) - mp.exp(-parameter * cutoff)
        )
        close_check(
            f"Gaussian forcing finite lambda moment is a boundary term, lambda={parameter}",
            finite_moment,
            boundary_moment,
            cutoff=GAUSSIAN_CUTOFF,
            full_line_moment=0,
        )
        for t in (mp.mpf("-1.3"), mp.mpf("0"), mp.mpf("1.1")):
            if t <= 0:
                endpoint = -cutoff
                r_forcing = mp.exp(-parameter * t) * split_quad(
                    lambda u: mp.exp(parameter * u) * forcing(parameter, u), endpoint, t
                )
                r_derivative = mp.exp(-parameter * t) * split_quad(
                    lambda u: mp.exp(parameter * u) * forcing_derivative(parameter, u), endpoint, t
                )
                side = "left"
            else:
                endpoint = cutoff
                r_forcing = -mp.exp(-parameter * t) * split_quad(
                    lambda u: mp.exp(parameter * u) * forcing(parameter, u), t, endpoint
                )
                r_derivative = -mp.exp(-parameter * t) * split_quad(
                    lambda u: mp.exp(parameter * u) * forcing_derivative(parameter, u), t, endpoint
                )
                side = "right"
            boundary_g = mp.exp(parameter * (endpoint - t)) * gaussian(endpoint)
            boundary_dg = -2 * endpoint * boundary_g
            metadata = {
                "cutoff": GAUSSIAN_CUTOFF,
                "side": side,
                "t": number(t),
                "lambda": str(parameter),
                "absolute_omitted_boundary_g": number(abs(boundary_g)),
                "absolute_omitted_boundary_dg": number(abs(boundary_dg)),
            }
            close_check(
                f"actual truncated R_lambda f recovers Gaussian: {parameter}, t={t}",
                r_forcing,
                gaussian(t) - boundary_g,
                **metadata,
            )
            close_check(
                f"actual R_lambda D commutation with boundary: {parameter}, t={t}",
                r_derivative,
                -2 * t * gaussian(t) - boundary_dg,
                **metadata,
            )
            boundary_f = mp.exp(parameter * (endpoint - t)) * forcing(parameter, endpoint)
            close_check(
                f"actual 1/lambda identity with boundary: {parameter}, t={t}",
                r_forcing - (forcing(parameter, t) - r_derivative) / parameter,
                -boundary_f / parameter,
                **metadata,
            )

    # Exact finite models only: no claim that zeta has one of these Jordan blocks.
    for size in range(1, 5):
        nil = nilpotent(size)
        eye = identity(size)
        for offset in (Fraction(0), Fraction(1, 8), Fraction(-1, 8)):
            b_matrix = add(scale(offset, eye), nil)
            parameter = Fraction(3, 4)
            resolvent = exact_resolvent(offset, nil, parameter)
            z_minus_b = add(scale(parameter, eye), scale(-1, b_matrix))
            exact_check(
                f"hypothetical Jordan resolvent left inverse, m={size}, beta={offset}",
                multiply(resolvent, z_minus_b) == eye,
            )
            exact_check(
                f"hypothetical Jordan resolvent right inverse, m={size}, beta={offset}",
                multiply(z_minus_b, resolvent) == eye,
            )
            regularized = add(
                add(scale(1 / parameter, eye), scale(1 / parameter**2, b_matrix)),
                scale(1 / parameter**2, multiply(resolvent, power(b_matrix, 2))),
            )
            exact_check(
                f"hypothetical Jordan exact B^2/z^2 decomposition, m={size}, beta={offset}",
                regularized == resolvent,
            )
        for t in (Fraction(-2), Fraction(-1, 2), Fraction(1, 2), Fraction(2)):
            exact_check(
                f"hypothetical Jordan nilpotent group inverse for both signs, m={size}, t={t}",
                multiply(nilpotent_exp(nil, t), nilpotent_exp(nil, -t)) == eye,
            )
        exact_check(
            f"hypothetical Jordan nilpotent group law across signs, m={size}",
            multiply(nilpotent_exp(nil, Fraction(-2)), nilpotent_exp(nil, Fraction(1, 2)))
            == nilpotent_exp(nil, Fraction(-3, 2)),
        )

    # The disk Harnack constant 3 is exact arithmetic, not a sampled harmonic-function proof.
    for radius in (Fraction(1, 8), Fraction(1, 4), Fraction(1, 100)):
        for fraction in (Fraction(0), Fraction(1, 2), Fraction(1)):
            distance = radius * fraction
            ratio = (2 * radius + distance) / (2 * radius - distance)
            exact_check(
                f"radius-2r Poisson ratio at relative distance {fraction}, r={radius}",
                ratio <= 3,
                exact_ratio=str(ratio),
            )
        exact_check(
            f"radius-2r boundary distance r has exact Harnack constant 3, r={radius}",
            (2 * radius + radius) / (2 * radius - radius) == 3,
        )

    # Finite Bromwich integral for one explicit hypothetical 3x3 block.
    size, offset = 3, Fraction(1, 8)
    nil_exact = nilpotent(size)
    b_exact = add(scale(offset, identity(size)), nil_exact)
    b_matrix = mpmatrix(b_exact)
    nil_matrix = mpmatrix(nil_exact)
    beta = mp.mpf(offset.numerator) / offset.denominator
    x = mp.matrix([1, -2, 3])
    b_squared_x = b_matrix**2 * x
    delta, time = mp.mpf("0.75"), mp.mpf("0.75")
    group = mp.exp(beta * time) * mpmatrix(nilpotent_exp(nil_exact, Fraction(3, 4)))
    expected_regularized = group * x - x - time * b_matrix * x

    def resolvent_vector(z):
        value = mp.matrix([0] * size)
        power_vector = b_squared_x.copy()
        for k in range(size):
            value += power_vector / (z - beta) ** (k + 1)
            power_vector = nil_matrix * power_vector
        return value

    for height in BROMWICH_CUTOFFS:
        points = [-height, -16, -8, -4, -2, -1, 0, 1, 2, 4, 8, 16, height]
        integral = mp.matrix([0] * size)
        for component in range(size):
            integral[component] = mp.quad(
                lambda frequency, component=component: (
                    mp.exp((delta + 1j * frequency) * time)
                    * resolvent_vector(delta + 1j * frequency)[component]
                    / (delta + 1j * frequency) ** 2
                ),
                points,
            ) / (2 * mp.pi)
        # Infinity norm of N^k is <=1.  For |T|>=H,
        # |z|>=|T| and |z-beta|>=|T|, so both tails have the stated bound.
        tail = (
            mp.exp(delta * time)
            * vector_norm(b_squared_x)
            / mp.pi
            * mp.fsum(
                mp.power(height, -k - 2) / (k + 2) for k in range(size)
            )
        )
        bound_check(
            f"finite hypothetical Jordan Bromwich cutoff H={height}",
            vector_norm(integral - expected_regularized),
            tail,
            size=size,
            beta=str(offset),
            real_contour=number(delta),
            positive_time=number(time),
            cutoff=height,
            tail_formula="exp(delta a) ||B^2 x||_infty / pi * sum_{k<m} H^(-k-2)/(k+2)",
            limitation="Finite model and non-interval quadrature; no actual zeta spectrum or infinite growth certification.",
        )

    for offset in (Fraction(1, 8), Fraction(-1, 8)):
        scalar = mp.mpf(offset.numerator) / offset.denominator
        positive = mp.exp(2 * scalar) * mpmatrix(nilpotent_exp(nil_exact, Fraction(2)))
        negative = mp.exp(-2 * scalar) * mpmatrix(nilpotent_exp(nil_exact, Fraction(-2)))
        close_check(
            f"full hypothetical Jordan group inverse with scalar for beta={offset}",
            max(abs(entry) for entry in positive * negative - mp.eye(size)),
            0,
            positive_and_negative_time=2,
        )

    passed = sum(check["passed"] for check in checks)
    exact_count = sum(check["kind"].startswith("exact") for check in checks)
    document = {
        "scope": "Finite diagnostics for notes 521--523",
        "precision_decimal_digits": args.precision,
        "floating_tolerance": number(tolerance),
        "source_profile": {
            "formula": "C exp(-1/((r-1)(2-r))) on (1,2), zero elsewhere; C chosen by dr/r normalization",
            "normalizer_before_C": number(profile_normalizer),
            "target_source": "(r d/dr + 1)(r^(-lambda) psi(r)), evenly extended",
            "sampled_heights": [0, 3, 8],
        },
        "cutoffs": {
            "finite_E_terms": E_CUTOFF,
            "Gaussian_integral_endpoint": GAUSSIAN_CUTOFF,
            "finite_Bromwich_heights": list(BROMWICH_CUTOFFS),
            "hypothetical_Jordan_sizes": [1, 2, 3, 4],
        },
        "notes_lf_sha256": {relative: lf_sha256(ROOT / relative) for relative in NOTES},
        "script_lf_sha256": lf_sha256(Path(__file__).resolve()),
        "summary": {
            "total": len(checks),
            "passed": passed,
            "failed": len(checks) - passed,
            "exact_finite_checks": exact_count,
            "non_interval_floating_checks": len(checks) - exact_count,
        },
        "limitations": [
            "Ordinary mpmath quadrature and rounding comparisons are not interval certificates or Lean proofs.",
            "Hypothetical finite Jordan blocks do not assert any actual multiple Riemann-zeta zero.",
            "Finite source samples do not prove an all-height bound or a continuous supremum.",
            "Finite Bromwich tests only check the displayed finite model and its tail estimate.",
            "Infinite source image, full-jet quotient, uniform resolvent, density and optimal-growth theorems require the analytic proofs in the notes.",
            "No new RH proof, zero-free region, zero proportion, simplicity theorem, independent arithmetic growth estimate or faithful Hilbert realization is claimed.",
        ],
        "checks": checks,
    }
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(document["summary"], sort_keys=True))
    print(f"Saved {output}")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

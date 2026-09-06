#!/usr/bin/env python3
"""[E] Bounded critical-window visibility checks, MP120 versus MP180.

No actual zeros or large-height divisor are computed.  This is an ordinary
multiple-precision consistency check, NOT interval/asymptotic certification.
All frequencies use f_z(u)=eta_A(u)*exp(-i*z*u).

The Montgomery--Taylor-shaped weight is
  eta_A(u)^2 = cos(u/(sqrt(2)*A))/(2*A*sinc(1/sqrt(2))) on [-A,A].
Its entire analytic Gram kernel is implemented locally below.  We check:
  (1) a finite clustered real background, including its positive g direction;
  (2) the exact two-point-fiber residual for the COMPLETE periodic background.
The latter is an integral identity, not a finite lattice truncation.  Parity
also makes the positive even g direction orthogonal to the odd residual.
Neither calculation identifies a compressed trace with the original operator.
The program writes no files.
"""

from __future__ import annotations

import json
import time

import mpmath as mp

from positive_background_quotient_audit import (
    principal,
    require,
    schur_residual,
    sinc,
    vector_specs,
)


def mt_kernel(omega, width):
    """Fourier transform of the normalized MT-shaped squared window."""
    b = 1 / mp.sqrt(2)
    return (sinc(width * omega - b) + sinc(width * omega + b)) / (2 * sinc(b))


def mt_density(u, width):
    """Density inside the observation interval; callers supply |u| <= width."""
    b = 1 / mp.sqrt(2)
    return mp.cos(b * u / width) / (2 * width * sinc(b))


def mt_gram(specifications, width, tolerance):
    dimension = len(specifications)
    gram = mp.matrix(dimension)
    imaginary_error = mp.mpf(0)
    for i in range(dimension):
        for j in range(i, dimension):
            value = mp.fsum(
                coefficient * mp.conj(other_coefficient)
                * mt_kernel(z - mp.conj(w), width)
                for z, coefficient in specifications[i]
                for w, other_coefficient in specifications[j]
            )
            imaginary_error = max(imaginary_error, abs(mp.im(value)))
            require(abs(mp.im(value)) <= tolerance, "real-type MT Gram")
            gram[i, j] = gram[j, i] = mp.re(value)
    return gram, imaginary_error


def relative_error(first, second):
    require(second != 0, "nonzero reference for relative comparison")
    return abs(first - second) / abs(second)


def quadrature(function, left, right):
    """Four fixed subintervals, avoiding a large unpartitioned hyperbolic arc."""
    points = [left + (right - left) * j / 4 for j in range(5)]
    return mp.quad(function, points)


def cluster_at_precision(width_input, precision):
    with mp.workdps(precision):
        width = mp.mpf(width_input)
        n = int(mp.ceil(2 * width))
        depth = radius = mp.mpf(1) / 4
        z = mp.j * depth
        height = mp.exp(2 * width)
        tolerance = mp.mpf(10) ** (-(precision - 25))
        nodes = [-radius + 2 * radius * j / (n + 1) for j in range(1, n + 1)]
        require(len(set(nodes)) == n, "distinct interior cluster nodes")
        require(all(abs(node) < radius for node in nodes), "cluster radius")
        specifications = vector_specs(nodes, [z])
        gram, imaginary_error = mt_gram(specifications, width, tolerance)
        cholesky = mp.cholesky(gram)
        require(all(cholesky[j, j] > 0 for j in range(n + 2)), "positive full Gram")
        target = n + 1
        real_indices = list(range(n))
        positive_indices = list(range(n + 1))  # ALL real features, then g_z.
        residual = schur_residual(gram, positive_indices, [target])[0, 0]
        real_residual = schur_residual(gram, real_indices, [target])[0, 0]
        require(residual > 0, "strictly positive quotient residual at this precision")
        require(real_residual > 0, "strictly positive real-span residual")
        require(residual <= real_residual + tolerance, "adding g cannot increase distance")

        coefficients = [
            mp.fprod((z - other) / (node - other)
                     for k, other in enumerate(nodes) if k != j)
            for j, node in enumerate(nodes)
        ]
        real_coefficients = mp.matrix([mp.im(value) for value in coefficients])
        cross = mp.matrix([gram[j, target] for j in real_indices])
        error_squared = gram[target, target] - 2 * (real_coefficients.T * cross)[0]
        error_squared += (real_coefficients.T * principal(gram, real_indices)
                          * real_coefficients)[0]
        bound = mp.exp(width * depth) * width**n / mp.factorial(n)
        bound *= mp.fprod(abs(z - node) for node in nodes)
        require(error_squared > 0, "positive interpolation error")
        require(real_residual <= error_squared + tolerance, "projection versus interpolation")
        require(error_squared <= bound**2 + tolerance, "divided-difference bound")
        coefficient_l1 = mp.fsum(abs(value) for value in coefficients)
        coefficient_bound = mp.exp(2) * height ** (1 + mp.log(2) / 2)
        require(coefficient_l1 <= coefficient_bound, "polynomial Lagrange coefficient budget")

        norm_squared = gram[target, target]
        analytic_norm = mp.re((mt_kernel(2 * mp.j * depth, width) - 1) / 2)
        require(relative_error(norm_squared, analytic_norm) < tolerance, "MT target norm identity")
        require(abs(mt_kernel(0, width) - 1) <= tolerance, "MT window normalization")
        for u in (-width, -width / 2, mp.mpf(0), width / 2, width):
            target_value = -mp.j * mp.sinh(depth * u)
            approximant = mp.fsum(mp.im(value) * mp.exp(-mp.j * node * u)
                                   for value, node in zip(coefficients, nodes))
            point_bound = mp.exp(abs(depth * u)) * abs(u)**n / mp.factorial(n)
            point_bound *= mp.fprod(abs(z - node) for node in nodes)
            require(abs(target_value - approximant) <= point_bound + tolerance,
                    "real-coefficient pointwise interpolation")

        values = {
            "quotient_residual_squared": residual,
            "real_span_residual_squared": real_residual,
            "target_norm_squared": norm_squared,
            "normalized_residual_squared": residual / norm_squared,
            "normalized_residual_norm": mp.sqrt(residual / norm_squared),
            "interpolation_error_squared": error_squared,
            "interpolation_bound_squared": bound**2,
            "complex_coefficient_l1": coefficient_l1,
            "coefficient_l1_upper": coefficient_bound,
        }
        return {
            "width": width_input, "n": n, "precision": precision,
            "values": {name: mp.nstr(value, precision) for name, value in values.items()},
            "maximum_imaginary_Gram_error": mp.nstr(imaginary_error, precision),
        }


def visible_at_precision(width_input, precision):
    with mp.workdps(precision):
        width = mp.mpf(width_input)
        depth, p = mp.mpf(1) / 4, mp.mpf(7) / 8
        period = 2 * p * width
        b = 1 / mp.sqrt(2)
        tolerance = mp.mpf(10) ** (-(precision - 30))
        require(width < period < 2 * width, "at most two points per periodic fiber")
        left, right = -width, width - period
        difference = lambda u: mp.sinh(depth * u) - mp.sinh(depth * (u + period))
        uniform_residual = mp.sinh(depth * p * width)**2 * (
            (1 - p) + mp.sinh(2 * depth * width * (1 - p)) / (2 * depth * width)
        )
        uniform_integral = quadrature(lambda u: difference(u)**2 / (4 * width), left, right)
        uniform_norm = mp.sinh(2 * depth * width) / (4 * depth * width) - mp.mpf("0.5")
        norm_integral = quadrature(lambda u: mp.sinh(depth * u)**2 / (2 * width), -width, width)
        require(relative_error(uniform_integral, uniform_residual) < tolerance,
                "complete periodic uniform fiber formula D")
        require(relative_error(norm_integral, uniform_norm) < tolerance, "uniform target norm H")

        def weighted_fiber(u):
            first, second = mt_density(u, width), mt_density(u + period, width)
            return first * second / (first + second) * difference(u)**2

        weighted_residual = quadrature(weighted_fiber, left, right)
        weighted_norm = quadrature(lambda u: mt_density(u, width) * mp.sinh(depth * u)**2,
                                   -width, width)
        kernel_norm = mp.re((mt_kernel(2 * mp.j * depth, width) - 1) / 2)
        require(relative_error(weighted_norm, kernel_norm) < tolerance, "MT norm integral/kernel")
        density_lower, density_upper = mp.cos(b) / sinc(b), 1 / sinc(b)
        require(weighted_residual >= density_lower * uniform_residual * (1 - tolerance),
                "weighted residual lower comparison")
        require(weighted_norm <= density_upper * uniform_norm * (1 + tolerance),
                "weighted norm upper comparison")
        weighted_ratio = weighted_residual / weighted_norm
        lower_ratio = mp.cos(b) * uniform_residual / uniform_norm
        require(weighted_ratio >= lower_ratio * (1 - tolerance), "MT normalized visibility lower bound")
        require(0 < weighted_ratio < 1, "finite positive proper residual fraction")
        values = {
            "uniform_residual_D": uniform_residual,
            "uniform_norm_H": uniform_norm,
            "uniform_normalized_residual_squared": uniform_residual / uniform_norm,
            "MT_residual_squared": weighted_residual,
            "MT_norm_squared": weighted_norm,
            "MT_normalized_residual_squared": weighted_ratio,
            "cos_b_times_D_over_H": lower_ratio,
        }
        return {
            "width": width_input, "precision": precision,
            "values": {name: mp.nstr(value, precision) for name, value in values.items()},
            "uniform_formula_relative_error": mp.nstr(relative_error(uniform_integral, uniform_residual), precision),
            "MT_norm_relative_error": mp.nstr(relative_error(weighted_norm, kernel_norm), precision),
        }


def compare_precisions(coarse, fine):
    errors = [relative_error(mp.mpf(coarse["values"][name]), mp.mpf(value))
              for name, value in fine["values"].items()]
    maximum = max(errors)
    require(maximum < mp.mpf("1e-55"), "MP120/180 agreement on positive residuals and budgets")
    return maximum


def main():
    started = time.perf_counter()
    mp.mp.dps = 180
    maximum_difference = mp.mpf(0)
    for kind, function, widths in (
        ("finite clustered MT Gram", cluster_at_precision, (2, 4, 6, 8)),
        ("complete periodic fiber integral", visible_at_precision, (2, 8, 32, 128)),
    ):
        for width in widths:
            coarse = function(width, 120)
            fine = function(width, 180)
            difference = compare_precisions(coarse, fine)
            maximum_difference = max(maximum_difference, difference)
            record = {
                "status": "[E] PASS", "kind": kind, "A": width,
                "precisions": [120, 180],
                "max_relative_precision_difference": mp.nstr(difference, 10),
                **{name: mp.nstr(mp.mpf(value), 15) for name, value in fine["values"].items()},
            }
            if "n" in fine:
                record["n_real_nodes"] = fine["n"]
            else:
                record["uniform_formula_relative_error"] = mp.nstr(mp.mpf(fine["uniform_formula_relative_error"]), 8)
                record["MT_norm_relative_error"] = mp.nstr(mp.mpf(fine["MT_norm_relative_error"]), 8)
            print(json.dumps(record), flush=True)
    print(json.dumps({
        "status": "PASS", "label": "[E] finite critical-window visibility audit only",
        "cluster_cases": 4, "complete_periodic_formula_cases": 4,
        "precisions": [120, 180],
        "max_relative_precision_difference": mp.nstr(maximum_difference, 12),
        "seconds": round(time.perf_counter() - started, 3),
        "actual_zeros_used": False,
        "asymptotic_or_interval_certification": False,
        "whole_operator_equals_compression": False,
    }), flush=True)


if __name__ == "__main__":
    main()

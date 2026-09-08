"""Finite evidence for notes 342--343; no asymptotic or RH certification.

The physical-cell test retains all four Mangoldt weights and the shared shell.
Poisson tests integrate the symmetric Dirichlet kernel, check two quadrature
orders, and compare against the original integer sum with its point corrections.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import roots_legendre, sici

from mobius_divisor_pullback_audit import exact_central_average
from power_high_bandpass_audit import finite_kernel
from power_high_prime_measure_audit import balanced_records, flat_overlap_weight


def continuous_kernel(t):
    value = np.asarray(t)
    return np.sinc(value) * np.cos(3 * np.pi * value)


def continuous_average(radius: float) -> float:
    return float((sici(4 * np.pi * radius)[0] - sici(2 * np.pi * radius)[0])
                 / (2 * np.pi * radius))


def cell_audit(limit: int) -> dict:
    length, radius = math.log(limit), math.sqrt(limit)
    bar_f = exact_central_average(limit, radius)
    bar_c = continuous_average(radius)
    atoms, records = balanced_records(limit)
    actual_f = actual_c = shell_mass = point_error = 0.0
    count = 0
    for index, left in enumerate(records):
        for right in records[index + 1:]:
            delta = right.ratio_log - left.ratio_log
            if delta > radius / limit:
                break
            if left.numerator * right.denominator == left.denominator * right.numerator:
                continue
            t = limit * delta
            weight = 2 * left.weight * right.weight * flat_overlap_weight(left, right, length)
            fk, ck = finite_kernel(limit, t), float(continuous_kernel(t))
            actual_f += weight * (fk - bar_f)
            actual_c += weight * (ck - bar_c)
            shell_mass += weight
            point_error = max(point_error, abs(fk - ck))
            count += 2
    bound = shell_mass * (point_error + abs(bar_f - bar_c))
    assert abs(actual_f - actual_c) <= bound + 1e-12
    grid = np.linspace(-radius, radius, 5001)
    sampled_error = max(abs(finite_kernel(limit, float(t)) - float(continuous_kernel(t)))
                        for t in grid)
    return dict(X=limit, M=radius, atom_count=atoms, ratio_records=len(records),
                ordered_shell_terms=count, shell_mass=shell_mass,
                finite_response=actual_f, continuous_response=actual_c,
                response_difference=actual_f - actual_c, exact_triangle_bound=bound,
                finite_center=bar_f, continuous_center=bar_c,
                sampled_kernel_sup_error=sampled_error,
                sampled_Q_times_error=limit * length * sampled_error,
                scope="fixed finite cells and 5001 samples; no uniform or asymptotic proof")


def overlap(a, b: int, c: int, d: int, length: float):
    a = np.asarray(a)
    log_a = np.log(a)
    lower_l = log_a - length / 2
    upper_l = length / 2 + np.minimum(0, log_a - math.log(b))
    delta = log_a + math.log(d) - math.log(b) - math.log(c)
    lower_r = math.log(c) - length / 2
    upper_r = length / 2 + min(0, math.log(c / d))
    total = np.zeros_like(a, dtype=float)
    for winding in (-1, 0, 1):
        total += np.maximum(0, np.minimum(upper_l, upper_r + delta + winding * length)
                            - np.maximum(lower_l, lower_r + delta + winding * length))
    return total / length


def poisson_case(label: str, m: int, b: int, c: int, d: int, taper: bool = False) -> dict:
    limit = 400
    length, radius, y = math.log(limit), math.sqrt(limit), limit ** 0.75
    lower, upper = math.ceil(.7 * y), math.floor(1.3 * y)
    a0, w0 = b * c / d, b * c / (d * m)
    lo = max(lower / m, w0 * math.exp(-radius / limit))
    hi = min(upper / m, w0 * math.exp(radius / limit))
    assert lo < hi
    center = continuous_average(radius)

    def smooth(w):
        a = m * np.asarray(w)
        t = limit * np.log(a / a0)
        result = overlap(a, b, c, d, length) * (continuous_kernel(t) - center) / np.sqrt(a)
        if taper:
            s = np.clip((radius - np.abs(t)) / limit ** -.25, 0, 1)
            result = result * (3 * s ** 2 - 2 * s ** 3)
        return result

    integers = list(range(math.ceil(lo), math.floor(hi) + 1))
    # All discrete masks are checked with integer arithmetic, not log tolerances.
    allowed = [n for n in integers if m * n != b and m * n * d != b * c]
    direct = sum(float(smooth(n)) for n in allowed)
    correction, events = 0.0, []
    for n in integers:
        inside_left = lo < n <= hi
        inside_right = lo <= n < hi
        value = float(smooth(n))
        actual = value if n in allowed else 0.0
        diff = actual - .5 * (inside_left + inside_right) * value
        correction += diff
        if diff:
            events.append(dict(n=n, a=m*n, correction=diff,
                               endpoint=n == lo or n == hi,
                               deleted=m*n == b or m*n*d == b*c))

    # These examples have no winding +/-1 overlap. Their only possible overlap
    # slope breaks lie at a=b or a=a0; include both for piecewise quadrature.
    cuts = sorted(set([lo, hi] + [x for x in (b / m, w0) if lo < x < hi]))
    if taper:
        transitions = [w0 * math.exp(sign * (radius - limit ** -.25) / limit)
                       for sign in (-1, 1)]
        cuts = sorted(set(cuts + [x for x in transitions if lo < x < hi]))
    truncations = (32, 64, 128, 256, 512, 1024, 2048)
    quadratures = []
    for order in (4096, 8192):
        nodes, weights = roots_legendre(order)
        values = {}
        zero = 0.0
        for left, right in zip(cuts[:-1], cuts[1:]):
            points = (left + right) / 2 + (right - left) / 2 * nodes
            amplitudes = (right - left) / 2 * weights * smooth(points)
            zero += float(np.sum(amplitudes))
            remainder = points - np.rint(points)
            for r in truncations:
                # Stable periodic Dirichlet kernel also at exact integer nodes.
                kernel = (2*r + 1) * np.sinc((2*r + 1) * remainder) / np.sinc(remainder)
                values[r] = values.get(r, 0.0) + float(np.sum(amplitudes * kernel))
        quadratures.append((zero, values))
    discrepancy = max(abs(quadratures[0][1][r] - quadratures[1][1][r]) for r in truncations)
    assert discrepancy < 2e-9, (label, discrepancy)
    convergence = [dict(R=r, symmetric_sum=quadratures[1][1][r],
                        corrected=quadratures[1][1][r] + correction,
                        difference=quadratures[1][1][r] + correction - direct)
                   for r in truncations]
    assert abs(convergence[-1]["difference"]) < 2e-5, (label, convergence)
    return dict(label=label, taper=taper, X=limit, r=1, v=m, m=m, b=b, c=c, d=d,
                interval=[lo, hi], integers=integers, allowed=allowed,
                direct_sum=direct, point_correction=correction, events=events,
                poisson_zero=quadratures[1][0], quadrature_orders=[4096, 8192],
                quadrature_discrepancy=discrepancy, convergence=convergence,
                scope="fixed actual outer variables; finite R convergence evidence only")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = {
        "scope": "E only; original normalization excludes external beta^4 D",
        "physical_cells": [cell_audit(x) for x in (100, 400, 1600)],
        "poisson_cases": [
            poisson_case("no_integer_endpoint_or_deletion", 5, 67, 71, 73),
            poisson_case("included_integer_cell_endpoint", 7, 67, 71, 73),
            poisson_case("deleted_ratio_diagonal", 9, 73, 81, 73),
            poisson_case("deleted_equal_numerator_denominator", 9, 81, 71, 73),
        ],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    for row in results["physical_cells"]:
        print(f"cell X={row['X']}: difference={row['response_difference']:.3e}, "
              f"triangle={row['exact_triangle_bound']:.3e}, "
              f"sampled Q*error={row['sampled_Q_times_error']:.6f}")
    for row in results["poisson_cases"]:
        print(f"{row['label']}: Ept={row['point_correction']:.6e}, "
              f"R2048 error={row['convergence'][-1]['difference']:.3e}, "
              f"quadrature difference={row['quadrature_discrepancy']:.3e}")
    print("PASS finite evidence only; no RH or asymptotic certification")


if __name__ == "__main__":
    main()

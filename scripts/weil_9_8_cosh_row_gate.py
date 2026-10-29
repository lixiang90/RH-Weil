"""Exact first operator gate for the single candidate L=9/8.

This evaluates the already paid 555 cosh-weighted Schur bound.  It does
not certify the full Weil form, a finite head, or any old C009 artifact.
All transcendental inputs are bounded by explicit positive rational series.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

L = Q(9, 8)
TERMS = 96
POWERS = (2, 3, 4, 5, 7, 8, 9)
BASE = {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2, 9: 3}


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    assert a[0] >= 0 and b[0] >= 0
    return a[0] * b[0], a[1] * b[1]


def div(a, b):
    assert a[0] >= 0 and b[0] > 0
    return a[0] / b[1], a[1] / b[0]


def atanh_log(r):
    assert 0 <= r <= Q(1, 3)
    total = sum((2 * r ** (2 * j + 1) / (2 * j + 1)
                 for j in range(TERMS)), Q(0))
    tail = 2 * r ** (2 * TERMS + 1) / ((2 * TERMS + 1) * (1 - r * r))
    return total, total + tail


def logarithm(n, log2):
    k = n.bit_length() - 1
    b = 1 << k
    residual = atanh_log(Q(n - b, n + b))
    return add((k * log2[0], k * log2[1]), residual)


def exponential():
    term = Q(1)
    total = term
    for k in range(1, TERMS + 1):
        term *= L / k
        total += term
    next_term = term * L / (TERMS + 1)
    tail = next_term / (1 - L / (TERMS + 2))
    return total, total + tail


def serial(a):
    return [str(a[0]), str(a[1])]


def calculate():
    log2 = atanh_log(Q(1, 3))
    logs = {p: logarithm(p, log2) for p in (2, 3, 5, 7)}
    exponential_l = exponential()
    one = (Q(1), Q(1))

    # x=exp(u), 0<=u<=L. Each row is (A*x+B)/(x+1).
    points = [("1", one), ("E/3", div(exponential_l, (Q(3), Q(3)))),
              ("4/E", div((Q(4), Q(4)), exponential_l)),
              ("E/2", div(exponential_l, (Q(2), Q(2))))]
    points += [(f"{n}/E", div((Q(n), Q(n)), exponential_l))
               for n in (5, 7, 8, 9)]
    points += [("E", exponential_l)]
    assert all(a[1][1] < b[1][0] for a, b in zip(points, points[1:]))

    cells = []
    certified_upper = Q(0)
    for left, right in zip(points, points[1:]):
        middle = (left[1][1] + right[1][0]) / 2
        negative = []
        positive = []
        for n in POWERS:
            threshold_neg = div((Q(n), Q(n)), exponential_l)
            threshold_pos = div(exponential_l, (Q(n), Q(n)))
            assert middle < threshold_neg[0] or middle > threshold_neg[1]
            assert middle < threshold_pos[0] or middle > threshold_pos[1]
            if middle > threshold_neg[1]:
                negative.append(n)
            if middle < threshold_pos[0]:
                positive.append(n)

        coefficient_a = (Q(0), Q(0))
        coefficient_b = (Q(0), Q(0))
        for n in negative:
            coefficient_a = add(coefficient_a, div(logs[BASE[n]], (Q(n), Q(n))))
            coefficient_b = add(coefficient_b, logs[BASE[n]])
        for n in positive:
            coefficient_a = add(coefficient_a, logs[BASE[n]])
            coefficient_b = add(coefficient_b, div(logs[BASE[n]], (Q(n), Q(n))))

        endpoint_values = []
        # A fractional-linear function has no interior strict extremum.
        # Both one-sided endpoints of every active-set cell are checked.
        for name, x in (left, right):
            numerator = add(mul(coefficient_a, x), coefficient_b)
            value = div(numerator, add(x, one))
            certified_upper = max(certified_upper, value[1])
            endpoint_values.append({"point": name, "row": serial(value)})
        cells.append({"left": left[0], "right": right[0],
                      "negative_shifts": negative, "positive_shifts": positive,
                      "endpoint_rows": endpoint_values})

    # Preserve the failed proposed threshold rather than suppressing a receipt.
    proposed = Q(13, 4)
    # A dyadic rounding of the computed enclosure, not a window/weight search.
    beta = Q((64 * certified_upper.numerator + certified_upper.denominator - 1)
             // certified_upper.denominator, 64)
    assert certified_upper < beta < Q(7, 2)
    coercivity = Q(7, 2) - beta
    upper_m = Q(7, 2) + beta
    # New analytic r=2^-85 gate supplied by the full-window ellipse formula.
    r_left = 81 * 68 ** 240 * 2 ** 1066
    r_right = 25 ** 240 * 3 ** 896
    r_gate = r_left < r_right
    return {
        "schema": "weil-single-window-9-8-operator-first-gate-v1",
        "classification": "exact evaluation of old555 operator bound; not full Q positivity",
        "half_width": "9/8", "terms": TERMS, "prime_powers": list(POWERS),
        "weight": "cosh(u/2)", "x": "exp(u), 0<=u<=L; negative side by evenness",
        "log_intervals": {str(p): serial(v) for p, v in logs.items()},
        "exp_L_interval": serial(exponential_l), "cells": cells,
        "proposed_row_bound": str(proposed),
        "proposed_bound_passed": certified_upper < proposed,
        "row_upper_less_than": str(beta), "max_enclosure_upper": str(certified_upper),
        "coercive_m": str(coercivity), "upper_b": str(upper_m),
        "consequence": f"||A_L||<{beta}; ({coercivity})I < (7/2)I-A_L < ({upper_m})I",
        "old_inverse_threshold_29_over_32_paid": coercivity > Q(29, 32),
        "r_2_minus_85_integer_gate": {"passed": r_gate,
            "left": str(r_left), "right": str(r_right),
            "scope": "Only the supplied ellipse bound scalar check, not a projection-error theorem"},
        "full_weil_positivity": "NOT_ESTABLISHED",
        "unpaid": ["new source moments/matrices/columns and all allowances",
                   "new full complement/cross and inverse/congruence/Gram certificate"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    destination = Path(args.output)
    assert not destination.exists(), "Preserve previous results; choose a fresh output"
    result = calculate()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(destination),
                      "proposed_13_over_4_passed": result["proposed_bound_passed"],
                      "row_bound": result["row_upper_less_than"],
                      "coercive_m": result["coercive_m"], "upper_b": result["upper_b"],
                      "r_2_minus_85_scalar": result["r_2_minus_85_integer_gate"]["passed"],
                      "full_weil_positivity": "NOT_ESTABLISHED"}))


if __name__ == "__main__":
    main()

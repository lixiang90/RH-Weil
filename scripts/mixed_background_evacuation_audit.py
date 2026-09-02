"""Finite audits for note 227's deterministic-background mixed closure.

These checks do not implement Henriot's theorem or a zero-counting argument.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def von_mangoldt(n: int) -> float:
    for p in range(2, n + 1):
        value = n
        exponent = 0
        while value % p == 0:
            value //= p
            exponent += 1
        if value == 1 and exponent:
            return math.log(p)
    return 0.0


def audit_twofold_prime_power_identity() -> None:
    for p in (2, 3, 5, 7):
        for exponent in range(2, 8):
            n = p**exponent
            convolution = sum(
                von_mangoldt(divisor) * von_mangoldt(n // divisor)
                for divisor in range(1, n + 1)
                if n % divisor == 0
            )
            expected = (exponent - 1) * math.log(p) ** 2
            assert abs(convolution - expected) < 1e-11
    print("twofold von Mangoldt prime-power identity passed")


def span(values: list[float]) -> float:
    return max(values) - min(values)


def audit_sign_walk_support() -> None:
    for steps in itertools.product((0.07, 0.19, 0.41), repeat=3):
        walk = [0.0]
        for step in steps:
            walk.append(walk[-1] + step)
        assert (span(walk) <= 1.0) == (sum(steps) <= 1.0)

    for x1, x2, x3 in itertools.product((0.11, 0.37, 0.63), repeat=3):
        walk = [0.0, x1, x1 + x2, x1 + x2 - x3]
        if span(walk) <= 1.0:
            assert x1 + x2 <= 1.0 + 1e-15
    print("mixed sign-walk support classification passed")


def audit_asymptotic_ledgers() -> None:
    log_x_values = [math.exp(value) for value in (8.0, 16.0, 32.0, 64.0)]
    ratio_two = [
        math.log(log_x) ** 2 / math.sqrt(log_x) for log_x in log_x_values
    ]
    ratio_three = [
        math.log(log_x) ** 3 / math.sqrt(log_x) for log_x in log_x_values
    ]
    assert all(right < left for left, right in zip(ratio_two, ratio_two[1:]))
    assert all(right < left for left, right in zip(ratio_three, ratio_three[1:]))
    assert ratio_two[-1] < 1e-9
    assert ratio_three[-1] < 1e-8
    print("mixed short-height exponent ledgers passed")


def schatten_four(matrix: np.ndarray) -> float:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    return float(np.sum(singular_values**4) ** 0.25)


def audit_whole_trace_selection_triangle() -> None:
    rng = np.random.default_rng(20260902)
    for dimension in (3, 7, 11):
        raw_s = rng.normal(size=(dimension, dimension))
        raw_p = rng.normal(size=(dimension, dimension))
        s = 0.5 * (raw_s + raw_s.T)
        p = 0.5 * (raw_p + raw_p.T)
        lhs = schatten_four(p)
        rhs = schatten_four(s + p) + schatten_four(s)
        assert lhs <= rhs + 1e-12
        fourth_trace = float(np.trace(np.linalg.matrix_power(s + p, 4)))
        assert abs(fourth_trace - schatten_four(s + p) ** 4) < 2e-9
    print("whole-trace selection Schatten triangle passed")


def audit_mt_constant() -> None:
    d_zero = 0.0000787875112465
    d_mixed = 0.00784079916792143
    d_22 = 0.244589382034426
    total = d_zero + d_mixed + d_22
    assert abs(total - 0.252508968713594) < 2e-13
    print(f"MT deterministic-background fourth constant: {total:.12f}")


def main() -> None:
    audit_twofold_prime_power_identity()
    audit_sign_walk_support()
    audit_asymptotic_ledgers()
    audit_whole_trace_selection_triangle()
    audit_mt_constant()
    print("Mixed deterministic-background audits passed")
    print("[scope] no Henriot implementation and no zero-counting claim")


if __name__ == "__main__":
    main()
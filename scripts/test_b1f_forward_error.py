"""Exact spot checks for the B1f floating forward-error ledger."""

from __future__ import annotations

from fractions import Fraction

from b1f_base_coefficient_interval_audit import (
    audited_centered_component,
    audited_float_convolution,
    audited_float_scale,
    audited_float_sum,
)
from formal_lag_response import FormalLag


def rational_map(source: dict[FormalLag, complex]) -> dict[FormalLag, Fraction]:
    return {
        lag: Fraction.from_float(float(coefficient.real))
        for lag, coefficient in source.items()
    }


def exact_convolution(
    left: dict[FormalLag, Fraction], right: dict[FormalLag, Fraction]
) -> dict[FormalLag, Fraction]:
    result: dict[FormalLag, Fraction] = {}
    for left_lag, left_value in left.items():
        for right_lag, right_value in right.items():
            lag = left_lag + right_lag
            result[lag] = result.get(lag, Fraction(0)) + left_value * right_value
    return result


def tv_distance(
    exact: dict[FormalLag, Fraction], approximate: dict[FormalLag, complex]
) -> Fraction:
    approximate_rational = rational_map(approximate)
    return sum(
        (
            abs(
                exact.get(lag, Fraction(0))
                - approximate_rational.get(lag, Fraction(0))
            )
            for lag in set(exact) | set(approximate_rational)
        ),
        Fraction(0),
    )


def main() -> None:
    left = {
        FormalLag.prime(2, 0): complex(0.1),
        FormalLag.prime(3, 0): complex(-0.2),
    }
    right = {
        FormalLag.prime(5, 0): complex(0.3),
        FormalLag.prime(7, 0): complex(0.4),
    }
    product, product_error = audited_float_convolution(
        left, Fraction(0), right, Fraction(0)
    )
    exact_product = exact_convolution(rational_map(left), rational_map(right))
    assert tv_distance(exact_product, product) <= product_error

    scaled, scaled_error = audited_float_scale(
        product, product_error, complex(-0.7)
    )
    scalar = Fraction.from_float(-0.7)
    exact_scaled = {
        lag: scalar * coefficient for lag, coefficient in exact_product.items()
    }
    assert tv_distance(exact_scaled, scaled) <= scaled_error

    summed, summed_error = audited_float_sum(
        ((left, Fraction(0)), (right, Fraction(0)))
    )
    exact_sum = rational_map(left)
    for lag, coefficient in rational_map(right).items():
        exact_sum[lag] = exact_sum.get(lag, Fraction(0)) + coefficient
    assert tv_distance(exact_sum, summed) <= summed_error

    zero = FormalLag.zero(0)
    centered, centered_error = audited_centered_component(left, zero)
    exact_left = rational_map(left)
    exact_left[zero] = -sum(exact_left.values(), Fraction(0))
    assert tv_distance(exact_left, centered) <= centered_error
    print("B1f forward-error exact spot checks passed")
    print("[scope] finite IEEE replay bounds; no zeta or RH claim")


if __name__ == "__main__":
    main()

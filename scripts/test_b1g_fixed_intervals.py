"""Exact unit checks for the B1g fixed-point trigonometric ledger."""

from __future__ import annotations

from fractions import Fraction

from b1g_directed_numerator_interval_audit import (
    FIXED_SCALE,
    FixedInterval,
    PI_RATIONAL,
    ceiling_fraction,
    floor_fraction,
    rational_cosine_fixed,
)
from brownian_interval_certificate import RationalInterval


def contains(interval: FixedInterval, value: Fraction) -> bool:
    return (
        interval.lower * value.denominator
        <= value.numerator * FIXED_SCALE
        <= interval.upper * value.denominator
    )


def main() -> None:
    assert floor_fraction(Fraction(-1, 3), 10) == -4
    assert ceiling_fraction(Fraction(-1, 3), 10) == -3
    assert floor_fraction(Fraction(1, 3), 10) == 3
    assert ceiling_fraction(Fraction(1, 3), 10) == 4

    left = RationalInterval(Fraction(-1, 5), Fraction(3, 10))
    right = RationalInterval(Fraction(-2, 7), Fraction(4, 9))
    fixed_left = FixedInterval.from_rational_interval(left)
    fixed_right = FixedInterval.from_rational_interval(right)
    product = fixed_left.multiply(fixed_right)
    for endpoint_left in (left.lower, left.upper):
        for endpoint_right in (right.lower, right.upper):
            assert contains(product, endpoint_left * endpoint_right)

    assert Fraction(333, 106) < PI_RATIONAL.lower
    assert PI_RATIONAL.upper < Fraction(355, 113)
    assert PI_RATIONAL.upper - PI_RATIONAL.lower < Fraction(1, 10**100)

    cosine_zero = rational_cosine_fixed(
        RationalInterval(Fraction(0), Fraction(0))
    )
    assert contains(cosine_zero, Fraction(1))
    cosine_pi = rational_cosine_fixed(PI_RATIONAL)
    assert contains(cosine_pi, Fraction(-1))
    cosine_two_pi = rational_cosine_fixed(PI_RATIONAL.scale_integer(2))
    assert contains(cosine_two_pi, Fraction(1))

    print("B1g fixed-point interval exact tests passed")
    print("[scope] rational arithmetic and trig enclosure; no zeta or RH claim")


if __name__ == "__main__":
    main()

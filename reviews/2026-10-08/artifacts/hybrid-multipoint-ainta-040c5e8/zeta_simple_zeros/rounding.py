"""Small IEEE-754 helpers for outward-rounded nonnegative arithmetic."""

from __future__ import annotations

import math


def down_ratio(numerator: int, denominator: int) -> float:
    """A binary64 lower bound for a nonnegative rational number."""

    if numerator < 0 or denominator <= 0:
        raise ValueError("down_ratio expects numerator >= 0 and denominator > 0")
    if numerator == 0:
        return 0.0
    return math.nextafter(numerator / denominator, -math.inf)


def up_ratio(numerator: int, denominator: int) -> float:
    """A binary64 upper bound for a nonnegative rational number."""

    if numerator < 0 or denominator <= 0:
        raise ValueError("up_ratio expects numerator >= 0 and denominator > 0")
    if numerator == 0:
        return 0.0
    return math.nextafter(numerator / denominator, math.inf)


def down_mul(left: float, right: float) -> float:
    """A lower bound for the product of two nonnegative lower bounds."""

    if left < 0.0 or right < 0.0:
        raise ValueError("down_mul expects nonnegative inputs")
    if left == 0.0 or right == 0.0:
        return 0.0
    return max(0.0, math.nextafter(left * right, -math.inf))


def down_add(left: float, right: float) -> float:
    """A lower bound for the sum of two nonnegative lower bounds."""

    if left < 0.0 or right < 0.0:
        raise ValueError("down_add expects nonnegative inputs")
    if left == 0.0 and right == 0.0:
        return 0.0
    return max(0.0, math.nextafter(left + right, -math.inf))

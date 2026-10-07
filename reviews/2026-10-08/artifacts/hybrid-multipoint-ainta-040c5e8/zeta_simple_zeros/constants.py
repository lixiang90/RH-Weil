"""Closed-form constants occurring in the two certificates."""

from __future__ import annotations

import math


H0 = 1.5 - (1.0 / math.sqrt(2.0)) / math.tan(1.0 / math.sqrt(2.0))
"""Anthropic's Montgomery-Taylor constant (Theorem D)."""


def three_point_bound(epsilon: float) -> float:
    """Return (H0 - epsilon/4) / (1 - epsilon/2)."""

    if not 0.0 < epsilon <= 1.0:
        raise ValueError("epsilon must lie in (0, 1]")
    return (H0 - epsilon / 4.0) / (1.0 - epsilon / 2.0)


def seven_point_bound() -> float:
    """Return the bound produced by the certified F6 >= 19/5000 inequality."""

    return (1_345_000.0 * H0 - 2_680.0) / 1_340_003.0

"""Finite sanity helpers for the Selberg-profile localization.

The routines encode only algebraic/telescoping identities and the scale of
proved majorants.  They are not asymptotic certificates and do not test RH.
"""

from __future__ import annotations

import math
from collections.abc import Callable


def microscopic_profile_majorant(n_scale: float, s: float) -> float:
    """Return N*s*(N*s+1)*log(3N), the bound in theorem ADM."""
    if n_scale < 2 or not 0 <= s <= math.log(1.5):
        raise ValueError("require N >= 2 and 0 <= s <= log(3/2)")
    return n_scale * s * (n_scale * s + 1.0) * math.log(3.0 * n_scale)


def telescope_dilation(
    error: Callable[[float], complex], x: float, steps: int
) -> tuple[complex, complex]:
    """Return direct and telescoped values of E(2x)-E(x)."""
    if x <= 0 or steps <= 0:
        raise ValueError("require x > 0 and steps > 0")
    r = math.log(2.0) / steps
    pieces = sum(
        error(math.exp((j + 1) * r) * x) - error(math.exp(j * r) * x)
        for j in range(steps)
    )
    return error(2.0 * x) - error(x), pieces


def wedge_scale_majorant(n_scale: float, height: float) -> float:
    """Return log(3N)*(N/T^2+1/T), suppressing absolute constants."""
    if n_scale < 2 or height <= 0:
        raise ValueError("require N >= 2 and T > 0")
    return math.log(3.0 * n_scale) * (
        n_scale / height**2 + 1.0 / height
    )


def dyadic_wedge_budget(height: float, eta: float) -> float:
    """Sum the model wedge majorant over dyadic N <= T^(2-eta)."""
    if height < 2 or not 0 < eta < 1:
        raise ValueError("require T >= 2 and 0 < eta < 1")
    cutoff = height ** (2.0 - eta)
    n_scale = 2.0
    total = 0.0
    while n_scale <= cutoff:
        total += wedge_scale_majorant(n_scale, height)
        n_scale *= 2.0
    return total / math.log(height)


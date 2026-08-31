"""Regression checks for the profile-equivalence bookkeeping."""

from __future__ import annotations

import cmath
import math

from selberg_profile import (
    dyadic_wedge_budget,
    microscopic_profile_majorant,
    telescope_dilation,
)


def test_telescope() -> None:
    def error(x: float) -> complex:
        return cmath.exp(0.37j * math.log(x)) + 0.2 * math.sin(x / 7.0)

    for steps in (1, 2, 7, 31, 128):
        direct, pieces = telescope_dilation(error, 3.25, steps)
        assert abs(direct - pieces) < 2e-13


def test_microscopic_scaling() -> None:
    n_scale = 10_000.0
    very_short = microscopic_profile_majorant(n_scale, 0.25 / n_scale)
    twice_short = microscopic_profile_majorant(n_scale, 0.5 / n_scale)
    assert 1.0 < twice_short / very_short < 3.0


def test_wedge_decay() -> None:
    eta = 0.3
    heights = (2.0**12, 2.0**16, 2.0**20)
    normalized = [
        dyadic_wedge_budget(height, eta) * height**eta
        for height in heights
    ]
    # The theorem allows logarithmic variation after extracting T^{-eta}.
    assert max(normalized) / min(normalized) < 4.0
    raw = [dyadic_wedge_budget(height, eta) for height in heights]
    assert raw[0] > raw[1] > raw[2]


def main() -> None:
    test_telescope()
    test_microscopic_scaling()
    test_wedge_decay()
    print("Selberg profile equivalence checks passed.")


if __name__ == "__main__":
    main()


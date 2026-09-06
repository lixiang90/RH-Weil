"""Regression evidence for the finite kernel, not a prime correlation bound."""
from __future__ import annotations

import json
import math

import mpmath as mp

from power_high_bandpass_audit import finite_kernel


def main() -> None:
    mp.mp.dps = 80
    cases = []
    for limit in (10, 400):
        scale = limit * math.log(limit)
        dimension = round(scale)
        for t in (0.0, 1e-15, .5, -2.75, math.sqrt(limit), scale,
                  scale + 1e-7, 2 * scale - .125):
            direct = math.fsum(
                math.cos(2 * math.pi * (1 + k / scale) * t)
                for k in range(dimension)
            ) / dimension
            error = abs(finite_kernel(limit, t) - direct)
            assert error < 2e-11, (limit, t, error)
            cases.append({"X": limit, "t": t, "reference": "direct sum",
                          "absolute_error": error})
    limit = 10**14
    scale = limit * math.log(limit)
    dimension = round(scale)
    for t in (0.0, .5, -1.25, 100.125, math.sqrt(limit)):
        # Exact high-precision finite sum formula with the same floating scale
        # and integer dimension as the audited implementation.
        x = mp.pi * mp.mpf(t) / mp.mpf(scale)
        sinc = lambda z: mp.sin(z) / z if z else mp.mpf(1)
        reference = sinc(dimension * x) / sinc(x) * mp.cos(
            2 * mp.pi * mp.mpf(t) + (dimension - 1) * x)
        actual = finite_kernel(limit, t)
        error = abs(actual - float(reference))
        assert error < 1e-12, (limit, t, error)
        cases.append({"X": limit, "t": t, "value": actual,
                      "reference": str(reference), "absolute_error": error})
    print(json.dumps({"status": "PASS", "scope": "finite numeric regression only",
                      "cases": cases}, indent=2))


if __name__ == "__main__":
    main()

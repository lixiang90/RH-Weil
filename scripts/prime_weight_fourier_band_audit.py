"""Finite evidence for note 340; no asymptotic inference from these scales."""
from __future__ import annotations

import json
import math

import numpy as np
from sympy import nextprime, primerange


def audit(limit: int) -> dict:
    y = limit**.75
    lower, upper = math.ceil(.7 * y), math.floor(1.3 * y)
    p = int(nextprime(4 * upper**2))
    assert 4 * upper**2 < p < 8 * upper**2
    lam = np.zeros(upper + 1)
    for prime in primerange(2, upper + 1):
        power = prime
        while power <= upper:
            lam[power] = math.log(prime)
            power *= prime
    n = np.arange(lower, upper + 1)
    w, v = np.zeros(p), np.zeros(p)
    w[n] = lam[n] / np.sqrt(n)
    v[n] = 1 / np.sqrt(n)
    fw, fv = np.fft.fft(w), np.fft.fft(v)
    total = float(np.vdot(fw, fw).real)
    expected = float(p * np.vdot(w, w).real)
    assert abs(total / expected - 1) < 1e-12
    bands = []
    for exponent in (0, 1, 2):
        multiplier = math.log(y)**exponent
        q = math.floor(p / y * multiplier)
        assert q < p // 2
        # Include 0 and both signed tails of the residue array.
        indices = np.concatenate((np.arange(q + 1), np.arange(p - q, p)))
        mass = float(np.vdot(fw[indices], fw[indices]).real)
        difference = fw[indices] - fv[indices]
        bands.append({"B_log_exponent": exponent, "Q": q,
                      "prime_energy_fraction": mass / total,
                      "scaled_prime_band_energy": mass / p,
                      "smooth_band_energy": float(
                          np.vdot(fv[indices], fv[indices]).real / p),
                      "scaled_band_difference_energy": float(
                          np.vdot(difference, difference).real / p)})
    return {"X": limit, "Y": y, "interval": [lower, upper], "prime_modulus": p,
            "sum_Lambda_squared_over_n": expected / p,
            "comparison_one_over_logY": 1 / math.log(y), "bands": bands}


if __name__ == "__main__":
    print(json.dumps({"status": "PASS", "scope": "three finite actual-weight cells",
                      "cases": [audit(x) for x in (100, 400, 1600)]}, indent=2))

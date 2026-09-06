"""Finite checks of note 336; all residues, including h=0 and singular duals."""
from __future__ import annotations

import json

import numpy as np


def audit(prime: int) -> dict:
    shape = (prime,) * 4
    coords = np.indices(shape).reshape(4, -1).T
    determinant = (coords[:, 0] * coords[:, 3]
                   - coords[:, 1] * coords[:, 2]) % prime
    phases = np.exp(2j * np.pi * np.arange(prime) / prime)
    units = np.arange(1, prime)
    inverses = np.array([pow(int(v), -1, prime) for v in units])
    max_error = 0.0
    # For p=3,5 compare coefficient vectors exactly in Z[z]/Phi_p(z).
    all_dot = coords @ coords.T % prime if prime <= 5 else None
    exact_checks = 0
    for h in range(prime):
        fiber = (determinant == h).reshape(shape)
        transform = np.fft.ifftn(fiber) * prime**4
        kloosterman = np.array([
            phases[(h * units + n * inverses) % prime].sum()
            for n in range(prime)
        ])
        expected = prime * kloosterman[determinant]
        expected[0] += prime**3
        error = float(np.max(np.abs(transform.ravel() - expected)))
        assert error < 1e-9, (prime, h, error)
        max_error = max(max_error, error)
        if all_dot is not None:
            mask = determinant == h
            for i, n in enumerate(determinant):
                difference = np.bincount(all_dot[i, mask], minlength=prime)
                difference -= prime * np.bincount(
                    (h * units + n * inverses) % prime, minlength=prime)
                if i == 0:
                    difference[0] -= prime**3
                assert np.all(difference == difference[0]), (prime, h, i)
                exact_checks += 1
    return {"prime": prime, "all_h_all_frequencies": prime**5,
            "maximum_float_error": max_error,
            "exact_cyclotomic_checks": exact_checks}


if __name__ == "__main__":
    print(json.dumps({"status": "PASS",
                      "scope": "finite algebra only; no asymptotic prime bound",
                      "cases": [audit(p) for p in (3, 5, 7, 11)]}, indent=2))

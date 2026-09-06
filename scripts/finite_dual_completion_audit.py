"""Finite algebra evidence for note 339; arbitrary complex test coefficients."""
from __future__ import annotations

import json

import numpy as np


def audit(p: int) -> dict:
    rng = np.random.default_rng(20260907 + p)
    grid = np.indices((p,) * 4).reshape(4, -1).T
    det = (grid[:, 0] * grid[:, 3] - grid[:, 1] * grid[:, 2]) % p
    units = np.arange(1, p)
    inverses = np.array([pow(int(v), -1, p) for v in units])
    roots = np.exp(2j * np.pi * np.arange(p) / p)
    s = np.array([[roots[(m * units + n * inverses) % p].sum()
                   for n in range(p)] for m in range(p)])
    errors = {"square": float(np.max(np.abs(s @ s - (
        p**2 * np.eye(p) - p * np.ones((p, p))))))}
    errors["row_sum"] = float(np.max(np.abs(s.sum(axis=1))))
    errors["coefficient_transform"] = 0.0
    errors["zero_layer"] = 0.0
    errors["inverse_response"] = 0.0
    for h in range(1, p):
        f = rng.standard_normal(p**4) + 1j * rng.standard_normal(p**4)
        f[0] = 0  # The formula in 339 assumes F_h(0)=0.
        fhat = np.fft.fftn(f.reshape((p,) * 4)).ravel()
        b = np.array([f[det == r].sum() for r in range(p)])
        a = np.array([fhat[(det == n) & (np.arange(p**4) != 0)].sum()
                      for n in range(p)])
        c = f.sum()
        expected = p * s @ b
        expected[0] -= c
        errors["coefficient_transform"] = max(
            errors["coefficient_transform"], float(np.max(np.abs(a - expected))))
        errors["zero_layer"] = max(
            errors["zero_layer"], float(abs(a[0] - (p**2 * b[0] - (p + 1) * c))))
        errors["inverse_response"] = max(
            errors["inverse_response"],
            float(abs(a @ s[h] / p**3 - (b[h] - (p**-1 - p**-3) * c))))
    assert max(errors.values()) < 1e-8, (p, errors)
    return {"prime": p, "errors": errors}


if __name__ == "__main__":
    print(json.dumps({"status": "PASS", "scope": "finite algebra; no prime estimate",
                      "cases": [audit(p) for p in (3, 5, 7, 11)]}, indent=2))

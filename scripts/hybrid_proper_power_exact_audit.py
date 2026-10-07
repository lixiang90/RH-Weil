"""Finite coefficient algebra for note 455; not an analytic norm certificate."""

from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/hybrid-proper-power-exact-audit.json"
INPUT = ROOT / "notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md"


def binding(path):
    data = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return {"path": path.relative_to(ROOT).as_posix(),
            "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data)}


def product_model(primes, weights):
    coefficients = defaultdict(Q)
    for p, wp in zip(primes, weights):
        for q, wq in zip(primes, weights):
            coefficients[p*q] += wp*wq
    s = sum((w*w for w in weights), Q(0))
    weighted_s = sum((p*w*w for p, w in zip(primes, weights)), Q(0))
    plain = sum((c*c for c in coefficients.values()), Q(0))
    weighted = sum((m*c*c for m, c in coefficients.items()), Q(0))
    assert plain == 2*s*s-sum((w**4 for w in weights), Q(0))
    assert weighted == 2*weighted_s**2-sum((p*p*w**4 for p, w in zip(primes, weights)), Q(0))
    assert len(coefficients) == len(primes)*(len(primes)+1)//2
    # The actual powers have indices m^2 but frequency 2 log m: no new collision.
    squared_indices = {m*m for m in coefficients}
    assert len(squared_indices) == len(coefficients)
    return {"primes": primes, "weights": [str(w) for w in weights],
            "product_coefficients": {str(m): str(c) for m, c in sorted(coefficients.items())},
            "plain_energy": str(plain), "base_weighted_energy": str(weighted),
            "square_index_collisions": False}


def certify():
    all_primes = [2, 3, 5, 7, 11]
    models = []
    for n in range(1, 6):
        primes = all_primes[:n]
        for weights in ([Q(1, p) for p in primes], [Q(i+2, 7) for i in range(n)]):
            models.append(product_model(primes, weights))
    # 4 e (b+e)^3 - ((b+e)^4-b^4), in powers b^i e^j.
    factor_coefficients = {(2, 2): 6, (1, 3): 8, (0, 4): 3}
    assert all(n >= 0 for n in factor_coefficients.values())
    scalar_checks = 0
    for b in [Q(0), Q(1, 7), Q(1), Q(13, 4)]:
        for e in [Q(0), Q(1, 100), Q(1, 2), Q(2)]:
            residual = sum((n*b**i*e**j for (i, j), n in factor_coefficients.items()), Q(0))
            assert residual == 4*e*(b+e)**3-((b+e)**4-b**4)
            for a in [max(Q(0), b-e), b, b+e]:
                assert abs(a-b) <= e
                assert abs(a**4-b**4) <= 4*e*(b+e)**3
                scalar_checks += 1
    return {
        "status": "PASS: finite coefficient identities and scalar polynomial algebra only",
        "product_models": models,
        "root_to_fourth_scalar_checks": scalar_checks,
        "nonnegative_bound_residual_coefficients": {"b^2 e^2": 6, "b e^3": 8, "e^4": 3},
        "input_read_and_hashed_from_disk": binding(INPUT),
        "script_read_and_hashed_from_disk": binding(Path(__file__).resolve()),
        "not_certified": [
            "Montgomery-Vaughan mean-value estimate or infinite coefficient bounds",
            "scalar spectral Jensen, full-height Fourier tails or Schatten Minkowski",
            "whole prime fourth bound, physical distinct or mixed sectors",
            "new zero-free boundary, zero proportion, RH, or external kernels",
        ],
    }


if __name__ == "__main__":
    result = certify()
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "product_models": len(result["product_models"]),
                      "scalar_checks": result["root_to_fourth_scalar_checks"],
                      "output": str(OUT)}, ensure_ascii=False))

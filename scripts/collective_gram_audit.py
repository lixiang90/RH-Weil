"""Exact algebra for phase 3. Does not certify zeta geometry or asymptotics."""

from pathlib import Path
import json
import sympy as sp

n = sp.symbols("n", positive=True)
M = n**4
assert sp.simplify(n / sp.sqrt(M) - 1/n) == 0
assert sp.expand((1+n)**2 - 1) == n**2 + 2*n
# A small exact instance of the rank-one projection counterexample.
size, t = 16, sp.Integer(2)
q = sp.ones(size, 1) / 4
projection = q * q.T
assert projection * projection == projection
v = sp.eye(size) + t * projection
assert v.T * v == sp.eye(size) + (2*t+t*t) * projection
assert (v.T * v).eigenvals() == {sp.Integer(1): 15, sp.Integer(9): 1}

s, d0, theta = map(sp.Rational, ("7/20", "2/5", "1/5"))
depth = sp.symbols("depth")
nu = 3*(sp.Rational(1, 2)-depth)/(sp.Rational(3, 2)-depth)
crossing = 3*(1-theta)/(2*(3-theta))
assert sp.simplify(nu.subs(depth, crossing) - theta) == 0
phi = crossing-theta
psi = crossing
assert psi-theta == phi
k = max(s, sp.Rational(1, 4)+phi/2)
mu = sp.Rational(1, 10)
result = {
    "scope": "Exact algebra only; no proof of operator estimates or actual clusters.",
    "rank_one_example": {
        "dimension": 16, "per_column_error_squared": "1/4",
        "common_gram_eigenvalues": {"1": 15, "9": 1},
        "general_per_column_error": "1/n",
        "general_common_gram_norm": "(1+n)^2",
    },
    "example_parameters": {
        "s": str(s), "d0": str(d0), "theta": str(theta),
        "crossing": str(crossing), "phi": str(phi), "psi": str(psi),
        "common_base_power": str(k), "cheap_base_margin": str(d0-k),
        "illustrative_cluster_count_power": str(mu),
        "HS_base_power": str(k+mu/2),
        "HS_base_excess_over_d0": str(k+mu/2-d0),
        "external_density_count_power": str(nu.subs(depth, d0)),
    },
}
assert d0-k == sp.Rational(1, 28)
assert k+mu/2-d0 == sp.Rational(1, 70)
assert 0 < mu < nu.subs(depth, d0) < 1-theta
target = Path(__file__).resolve().parents[1] / "reviews/2026-09-06/phase3-exact-algebra.json"
target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))

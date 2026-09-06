"""Exact exponent bookkeeping for 323; no certification of actual smallness."""
from fractions import Fraction as F
import json
from pathlib import Path

s, d0, theta = F(7, 20), F(2, 5), F(1, 5)
nu = lambda v: 3*(F(1, 2)-v)/(F(3, 2)-v)
r = 3*(1-theta)/(2*(3-theta))
phi = r-theta if s <= r else s+nu(s)-2*theta
xi = phi+2*theta
first, second = F(1, 4)+xi/2, xi-theta
assert (xi, first, first-d0, second) == (
    F(22, 35), F(79, 140), F(23, 140), F(3, 7))
assert F(1, 2)-d0 > 0
# Exact weighted Markov bound, including the empty bad-set boundary.
for weights, leaks, eps in [
    ([F(1), F(3)], [F(0), F(0)], F(1, 10)),
    ([F(1), F(9)], [F(1, 5), F(0)], F(1, 10)),
    ([F(1), F(9)], [F(1, 5), F(2)], F(1, 10)),
]:
    bad = [j for j in range(len(weights)) if leaks[j] > eps*weights[j]]
    assert sum((weights[j] for j in bad), F(0)) <= (
        sum((leaks[j] for j in bad), F(0))/eps)

result = {
    "scope": "Exact exponents and finite weighted inequality only. "
             "A growing upper bound does not prove actual growth or impossibility.",
    "s": str(s), "d0": str(d0), "theta": str(theta),
    "Phi": str(phi), "Xi": str(xi),
    "K_first_power": str(first), "K_first_excess": str(first-d0),
    "K_second_power": str(second),
    "leakage_bound_power": str(F(1, 2)-d0),
    "weighted_markov_cases": 3,
}
path = Path(__file__).resolve().parents[1]/"reviews/2026-09-06/near-deep-exponents.json"
path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))

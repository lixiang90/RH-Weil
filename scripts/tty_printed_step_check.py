"""Exact check of the failing printed step in TTY v1, Theorem 51.

This tests one implication in its printed proof, not the theorem's conclusion.
"""
from fractions import Fraction as F
from pathlib import Path
import json

sigma, tau = F(17, 22), F(11, 10)
tau0 = min(9 * (3 * sigma - 2) / 2, 8 * (2 * sigma - 1) / 3)
q = (3 - 3 * sigma) / tau0
threshold = -max((10 - 16 * sigma) / 3, 18 - 24 * sigma) / (1 - q)
alpha2 = max(11 - 16 * sigma + tau, F(0))
alpha1 = tau / 3 - F(2, 3) * (7 * sigma - 5) - alpha2 / 6
left = tau / 3 + (16 - 20 * sigma) / 3 + alpha2 / 3
right = q * tau
assert 2 * tau0 / 3 <= tau <= tau0
assert tau >= threshold and alpha1 >= 0 and alpha2 >= 0
assert left - right == F(19, 770) > 0
# The proposed k=4 preliminary bound covers this point; this single check
# does not certify the proposed repair on the full parameter domain.
k4_bound = max(2 - 2 * sigma, tau + (7 - 11 * sigma) / 2,
               tau + 24 - 32 * sigma)
assert k4_bound <= right
result = {key: str(value) for key, value in {
    "sigma": sigma, "tau": tau, "tau0": tau0, "q": q,
    "printed_40_threshold": threshold, "alpha1": alpha1, "alpha2": alpha2,
    "printed_42_left": left, "required_right": right,
    "positive_violation": left - right, "k4_at_this_point": k4_bound,
}.items()}
result["scope"] = "One exact printed-step counterexample; not a counterexample to the theorem."
target = Path(__file__).resolve().parents[1] / "reviews/2026-09-06/tty-printed-step.json"
target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(result, indent=2))

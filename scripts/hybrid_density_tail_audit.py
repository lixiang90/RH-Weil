"""Exact algebra for note 314; no certification of analytic density inputs."""

import json
from pathlib import Path
import sympy as sp


def main():
    q = sp.Rational
    v, theta = sp.symbols("v theta", real=True)
    nu = 3 * (q(1, 2) - v) / (q(3, 2) - v)
    cross = 3 * (1 - theta) / (2 * (3 - theta))
    assert sp.cancel(nu.subs(v, cross) - theta) == 0
    assert sp.cancel(sp.diff(v + nu, v) - (1 - 3 / (q(3, 2) - v) ** 2)) == 0
    # On 0 <= v <= 1/2 the derivative is at most -1/3.
    assert 1 - 3 / q(3, 2) ** 2 == -q(1, 3)
    d, s, gap = q(2, 5), q(7, 20), q(1, 5)
    r = cross.subs(theta, gap)
    phi = r - gap if s <= r else s + nu.subs(v, s) - 2 * gap
    k = max(s, q(1, 4) + phi / 2)
    alpha_old, beta_old = q(1, 2) - gap, (1 - gap) / 2
    assert s < d and phi < d and k < d
    result = {
        "gap_power": str(gap), "crossover_depth": str(r),
        "tail_alpha_power": str(phi), "lambda_power": str(k),
        "alpha_power_saving": str(alpha_old - phi),
        "beta_power_saving": str(beta_old - (q(1, 4) + phi / 2)),
        "global_inverse_cost_power_lower_bound": str(2 * (d - k)),
        "symbolic_crossing_and_derivative": "PASS",
        "scope": "Exact algebra only; density theorem, uniform operator bounds, and actual isolation require separate proofs",
    }
    text = json.dumps(result, indent=2) + "\n"
    print(text, end="")
    path = Path(__file__).resolve().parents[1] / "reviews/2026-09-06/314-exponent-check.json"
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

"""Exact parameter arithmetic for note 313; not an operator proof."""

from fractions import Fraction as Q
import json


def main():
    d, delta, eps = Q(2, 5), Q(1, 20), Q(1, 5)
    s = d - delta
    a = Q(1, 2) - d + eps
    k = max(s, (1 - a) / 2)
    assert 0 < delta < d < Q(1, 2) and 0 < eps < d
    assert s < d and Q(1, 2) - a - d < 0 and k < d
    assert s - k <= 0 and (1 - a) / 2 - k <= 0
    result = {
        "target_min_depth": str(d),
        "shallow_max_depth": str(s),
        "height_gap_power": str(a),
        "lambda_power": str(k),
        "alpha_shallow_relative_power": str(s - d),
        "alpha_far_relative_power": str(Q(1, 2) - a - d),
        "beta_shallow_over_lambda_power": str(s - k),
        "beta_far_over_lambda_power": str((1 - a) / 2 - k),
        "global_inverse_cost_power_lower_bound": str(2 * (d - k)),
        "scope": "Exact rational exponent audit only; does not certify operator inequalities, uniformity or actual zeta separation",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

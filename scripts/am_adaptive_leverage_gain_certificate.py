"""Exact algebra for the conditional all-zero adaptive leverage gain.

No positive normalized leverage input is proved here. The finite spectral
lemma and its fixed-smoothing zeta transport require the separate analytic
research note. This check only verifies the rational consequence and targets.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/am-adaptive-leverage-gain-certificate.json"


def sha(path):
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def certificate():
    assert __debug__
    c = Q(805003, 10**8)
    b = Q(404350, 10**8)
    a = Q(67216841, 10**8)
    gamma, d = 1-c, a-b
    p0 = Q(66812491, 99194997)
    assert d == gamma*p0
    assert 0 < p0 < 1 and gamma > 0
    # gamma*(r-p0)*(1-r) = -gamma*r^2+(gamma+d)*r-d.
    expanded = (-gamma, gamma+d, -d)
    assert expanded == (-gamma, gamma*(1+p0), -gamma*p0)
    vertex = (1+p0)/2
    maximum = gamma*(vertex-p0)*(1-vertex)
    h_square_upper = maximum/2
    assert h_square_upper == gamma*(1-p0)**2/8
    assert h_square_upper == Q(262156673710009, 19838999400000000)
    h_upper = Q(114954, 10**6)
    assert h_square_upper < h_upper*h_upper

    h_required = Q(3, 2000)
    p_target = Q(67356, 10**5)
    method_ceiling = Q(67355961, 10**8)
    assert p0 < method_ceiling < p_target < vertex < 1
    # This concave polynomial increases throughout [p0,p_target]. Its
    # negative value at the right endpoint excludes that entire interval.
    derivative_min = gamma*(1+p0-2*p_target)
    assert derivative_min > 0
    residual = gamma*(p_target-p0)*(1-p_target)-2*h_required*h_required
    assert residual == -Q(17817139237, 62500000000000000) < 0
    required_at_ceiling_square = gamma*(method_ceiling-p0)*(1-method_ceiling)/2
    near_threshold = Q(1431, 10**6)
    assert near_threshold*near_threshold > required_at_ceiling_square
    assert h_required*h_required > required_at_ceiling_square

    return {
        "schema": "rh-weil-am-adaptive-leverage-gain-v1",
        "scope": "exact rational consequences of the separately proved conditional spectral inequality only",
        "not_a_new_actual_zero_proportion": True,
        "normalized_positive_input_proved_here": False,
        "finite_spectral_lemma_proved_here": False,
        "analytic_zeta_transport_proved_here": False,
        "script_canonical_lf_sha256": sha(Path(__file__)),
        "admitted_base_proportion": str(p0), "gamma": str(gamma), "plain_gain_minus_fee": str(d),
        "normalized_quantity": "h=(tr Q_- + tr(P 1_(Q>0)))/N, P counts simple critical zeros only",
        "necessary_asymptotic_inequality": "gamma*(r-p0)*(1-r) >= 2*h^2",
        "normalized_quantity_square_upper": str(h_square_upper),
        "normalized_quantity_strict_upper": str(h_upper),
        "conditional_input_required": str(h_required),
        "input_limit_order": "liminf_(epsilon down to 0) liminf_(T to infinity) h >= required",
        "conditional_proportion_strict_lower": str(p_target),
        "target_polynomial_strict_negative_residual": str(residual),
        "target_interval_derivative_strict_lower": str(derivative_min),
        "fixed_AM_range_seven_method_strict_ceiling": str(method_ceiling),
        "input_square_threshold_at_method_ceiling": str(required_at_ceiling_square),
        "conservative_input_exceeding_method_ceiling_threshold": str(near_threshold),
        "status": "PASS_CONDITIONAL_ALGEBRA_ONLY",
    }


def main():
    if not __debug__:
        raise SystemExit("Run without -O: all certificate assertions are required")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = certificate()
    if args.check:
        assert json.loads(OUTPUT.read_text(encoding="utf-8")) == result
        print("PASS conditional adaptive leverage algebra and committed report")
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        print("PASS; wrote output/am-adaptive-leverage-gain-certificate.json")


if __name__ == "__main__":
    main()

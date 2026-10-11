"""Exact necessary ceilings for the current AM kernel and range eight.

These are limits on specified local certificate methods, not upper bounds on
the actual zeta-zero proportion. Floating searches are not consumed here.
The accompanying research note proves the periodic averaging implication.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import am_lossless_majorant_certificate as am

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/am-range-eight-periodic-ceiling-certificate.json"
INPUT_SHA = "11da56ae04a60fd436d273f39463e6aa85b0f023ebf62a0389c5f9af0b2aabf4"
WORDS = [[1042249, 1972639], [1034650, 1034650, 1964373, 1042133, 1964373]]
ENERGY_UPPERS = [Q(2002693589, 10**12), Q(2450440012, 10**12)]


def sha(path):
    raw = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(raw).hexdigest()


def square(interval):
    lo, hi = interval
    assert lo <= hi
    return (Q(0) if lo <= 0 <= hi else min(lo*lo, hi*hi), max(lo*lo, hi*hi))


def certificate():
    assert __debug__
    assert sha(Path(am.__file__)) == INPUT_SHA
    machin = am.add(am.scale(am.atan_interval(5), 16),
                    am.scale(am.atan_interval(239), -4))
    pi = Q(314159265358979323846, 10**20), Q(314159265358979323847, 10**20)
    assert pi[0] < machin[0] <= machin[1] < pi[1]
    pi2 = am.mul(pi, pi)
    norm = am.trig_interval((Q(1, 2), Q(1, 2)), True)
    cot = am.divide(am.trig_interval((Q(1, 2), Q(1, 2))), norm)
    cs = [Q(x, 10**9) for x in am.CS]
    correction_lower = sum((c*c*(Q(1, 2)-1/(4*pi[0]**2*j*j))
                            for j, c in enumerate(cs, 1)), Q(0))/norm[1]**2
    gain_upper = Q(672168411, 10**9)
    assert Q(3, 2)-cot[0]-correction_lower < gain_upper
    cache = {}

    def sinc(x):
        if x == 0:
            return Q(1), Q(1)
        phase = (x+1) % 2-1
        return am.scale(am.trig_interval(am.scale(pi2, phase*phase), True), phase/x)

    def kernel(x):
        assert x >= Q(4, 5)
        if x in cache:
            return cache[x]
        phase = (x+1) % 2-1
        sq = am.scale(pi2, phase*phase)
        sin_times_angle = am.scale(am.mul(pi2, am.trig_interval(sq, True)), x*phase)
        num = am.add(am.mul(cot, sin_times_angle), am.scale(am.trig_interval(sq), -Q(1, 2)))
        den = am.add(am.scale(pi2, x*x), (-Q(1, 2), -Q(1, 2)))
        perturbation = Q(0), Q(0)
        for j, cj in enumerate(cs, 1):
            perturbation = am.add(perturbation, am.scale(am.add(sinc(x-j), sinc(x+j)), cj))
        cache[x] = am.add(am.divide(num, den), am.divide(perturbation, am.scale(norm, 2)))
        return cache[x]

    capacities = [sum((Q(am.ROWS[i][s-1], 10**8) for i in range(8-s)), Q(0))
                  for s in range(1, 8)] + [Q(2)]
    assert all(0 <= cap <= 2 for cap in capacities)
    pressure = Q(sum(am.BS), 10**8)
    assert pressure == Q(404350, 10**8)
    reports, means, fixed_values = [], [], []
    for word, upper in zip(WORDS, ENERGY_UPPERS):
        gaps = [Q(x, 10**6) for x in word]
        assert all(x >= Q(4, 5) for x in gaps)
        m = len(gaps)
        rows = []
        for span in range(1, 9):
            energy = Q(0), Q(0)
            for i in range(m):
                distance = sum((gaps[(i+t) % m] for t in range(span)), Q(0))
                energy = am.add(energy, square(kernel(distance)))
            rows.append(am.scale(energy, Q(1, m)))
        total, fixed = (Q(0), Q(0)), (Q(0), Q(0))
        for cap, row in zip(capacities, rows):
            total = am.add(total, am.scale(row, 2))
            fixed = am.add(fixed, am.scale(row, cap))
        assert total[1] < upper < 1
        mean = sum(gaps, Q(0))/m
        fixed = am.add(fixed, (pressure*mean, pressure*mean))
        means.append(mean)
        fixed_values.append(fixed)
        reports.append({"gap_numerators": word, "gap_denominator": 10**6,
                        "mean_gap": str(mean),
                        "range_eight_ordered_energy_strict_upper": str(upper)})

    u1, u2 = [1-x for x in ENERGY_UPPERS]
    g1, g2 = means
    determinant = u1*g2-u2*g1
    assert determinant != 0
    lam1 = (gain_upper*g2-u2)/determinant
    lam2 = (u1-gain_upper*g1)/determinant
    assert lam1 > 0 and lam2 > 0
    assert lam1*u1+lam2*u2 == gain_upper
    assert lam1*g1+lam2*g2 == 1
    output_upper = lam1+lam2
    assert output_upper == Q(331856527056851000, 492670815881465791)
    rounded_upper = Q(673586737, 10**9)
    assert output_upper < rounded_upper < 1

    # The first word additionally bounds the exact fixed F9 coefficients.
    fixed_reward_upper = Q(8098043377, 10**12)
    assert fixed_values[0][1] < fixed_reward_upper < 1
    fixed_output_upper = (gain_upper-pressure)/(1-fixed_reward_upper)
    assert fixed_output_upper == Q(668124911000, 991901956623)
    current = Q(941021, 1397107)
    assert current < fixed_output_upper < output_upper
    fourth_moment_threshold = 4/(9*current)-Q(1, 3)
    assert fourth_moment_threshold == Q(2765365, 8469189)
    return {
        "schema": "rh-weil-am-range-eight-periodic-ceiling-v1",
        "status": "PASS_METHOD_NECESSARY_CUTS_ONLY",
        "not_an_actual_zeta_proportion_upper_bound": True,
        "not_a_new_proportion_lower_bound": True,
        "scope": "fixed AM13 kernel, index range <=8, nonnegative pair weights with total span capacities <=2, bounded telescoping storage, c<1",
        "periodic_cuts": reports,
        "input_interval_helper_canonical_lf_sha256": INPUT_SHA,
        "script_canonical_lf_sha256": sha(Path(__file__)),
        "pi_interval": [str(x) for x in pi],
        "am_plain_gain_strict_upper": str(gain_upper),
        "dual_weights": [str(lam1), str(lam2)],
        "dual_objective_upper": str(output_upper),
        "method_output_strict_upper": str(rounded_upper),
        "fixed_F9_span_capacities": [str(x) for x in capacities],
        "fixed_F9_pressure": str(pressure),
        "fixed_F9_period_two_reward_strict_upper": str(fixed_reward_upper),
        "fixed_F9_output_strict_upper": str(fixed_output_upper),
        "current_verified_proportion": str(current),
        "fixed_F9_output_upper_minus_current": str(fixed_output_upper-current),
        "range_eight_output_upper_minus_current": str(output_upper-current),
        "flat_v_one_third_fourth_moment_threshold_to_exceed_current": str(fourth_moment_threshold),
        "unique_kernel_distances_enclosed": len(cache),
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
        print("PASS exact range-eight periodic necessary cuts and saved report")
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        print("PASS; wrote output/am-range-eight-periodic-ceiling-certificate.json")


if __name__ == "__main__":
    main()

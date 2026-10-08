"""Two exact periodic necessary cuts for the fixed AM13, range-seven scheme.

This proves a ceiling for a specified certificate method, not an upper bound
on the actual proportion of critical zeros. Uses only stdlib Fractions and the
already audited small Taylor-interval primitives in the lossless certificate.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import am_lossless_majorant_certificate as am

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/am-storage-periodic-ceiling-certificate.json"
INPUT_SHA = "11da56ae04a60fd436d273f39463e6aa85b0f023ebf62a0389c5f9af0b2aabf4"
WORDS = [[1042697, 1974488], [1035512, 1035512, 1966573, 1042733, 1966573]]


def sha(path):
    b = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(b).hexdigest()


def certificate():
    assert __debug__
    assert sha(Path(am.__file__)) == INPUT_SHA
    machin = am.add(am.scale(am.atan_interval(5), 16), am.scale(am.atan_interval(239), -4))
    pi = Q(314159265358979323846, 10**20), Q(314159265358979323847, 10**20)
    assert pi[0] < machin[0] <= machin[1] < pi[1]
    pi2 = am.mul(pi, pi)
    norm = am.trig_interval((Q(1, 2), Q(1, 2)), True)
    cot = am.divide(am.trig_interval((Q(1, 2), Q(1, 2))), norm)
    cs = [Q(x, 10**9) for x in am.CS]
    energy_correction_lower = sum((c*c*(Q(1, 2)-1/(4*pi[0]**2*j*j))
                                   for j, c in enumerate(cs, 1)), Q(0)) / norm[1]**2
    a_upper = Q(672168411, 10**9)
    assert Q(3, 2)-cot[0]-energy_correction_lower < a_upper

    def sinc_interval(x):
        if x == 0:
            return Q(1), Q(1)
        phase = (x+1) % 2-1
        return am.scale(am.trig_interval(am.scale(pi2, phase*phase), True), phase/x)

    cache = {}

    def kernel_interval(x):
        assert x >= Q(4, 5)
        if x in cache:
            return cache[x]
        phase = (x+1) % 2-1
        sq = am.scale(pi2, phase*phase)
        sine_times_full_angle = am.scale(am.mul(pi2, am.trig_interval(sq, True)), x*phase)
        numerator = am.add(am.mul(cot, sine_times_full_angle),
                           am.scale(am.trig_interval(sq), -Q(1, 2)))
        denominator = am.add(am.scale(pi2, x*x), (-Q(1, 2), -Q(1, 2)))
        value = am.divide(numerator, denominator)
        perturbation = Q(0), Q(0)
        for j, cj in enumerate(cs, 1):
            legs = am.add(sinc_interval(x-j), sinc_interval(x+j))
            perturbation = am.add(perturbation, am.scale(legs, cj))
        value = am.add(value, am.divide(perturbation, am.scale(norm, 2)))
        cache[x] = value
        return value

    energies, means = [], []
    e_upper = [Q(1964888763, 10**12), Q(2381521000, 10**12)]
    reports = []
    for word, upper in zip(WORDS, e_upper):
        gaps = [Q(x, 10**6) for x in word]
        assert all(x >= Q(4, 5) for x in gaps)
        m = len(gaps)
        energy = Q(0), Q(0)
        for i in range(m):
            distance = Q(0)
            for s in range(1, 8):
                distance += gaps[(i+s-1) % m]
                k = kernel_interval(distance)
                energy = am.add(energy, am.mul(k, k))
        energy = am.scale(energy, Q(2, m))
        assert energy[1] < upper
        mean = sum(gaps, Q(0))/m
        energies.append(energy)
        means.append(mean)
        lower = Q(energy[0].numerator*10**12//energy[0].denominator, 10**12)
        reports.append({"gap_numerators": word, "gap_denominator": 10**6,
                        "mean_gap": str(mean), "range_seven_ordered_energy_lower": str(lower),
                        "range_seven_ordered_energy_strict_upper": str(upper)})

    u1, u2 = 1-e_upper[0], 1-e_upper[1]
    g1, g2 = means
    determinant = u1*g2-u2*g1
    assert determinant != 0
    lam1 = (a_upper*g2-u2)/determinant
    lam2 = (u1-a_upper*g1)/determinant
    assert lam1 > 0 and lam2 > 0
    assert lam1*u1+lam2*u2 == a_upper
    assert lam1*g1+lam2*g2 == 1
    upper_output = lam1+lam2
    ceiling = Q(67355961, 10**8)
    assert upper_output < ceiling
    current = Q(66812491, 99194997)
    assert current < upper_output
    return {
        "schema": "rh-weil-am-storage-periodic-ceiling-v1",
        "scope": "necessary ceiling for fixed AM13 kernel, index range <=7, span budgets <=2 and bounded telescoping storage",
        "not_an_actual_zeta_proportion_upper_bound": True,
        "not_a_new_local_lower_certificate": True,
        "input_interval_helper_canonical_lf_sha256": INPUT_SHA,
        "script_canonical_lf_sha256": sha(Path(__file__)),
        "pi_interval": [str(x) for x in pi], "am_plain_gain_strict_upper": str(a_upper),
        "periodic_cuts": reports, "dual_weights": [str(lam1), str(lam2)],
        "dual_objective_upper": str(upper_output), "method_output_strict_upper": str(ceiling),
        "admitted_current_proportion_lower": str(current),
        "strict_ceiling_minus_current": str(ceiling-current),
        "unique_kernel_distances_enclosed": len(cache), "status": "PASS",
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
        print("PASS exact periodic method ceiling and committed report")
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        print("PASS; wrote output/am-storage-periodic-ceiling-certificate.json")


if __name__ == "__main__":
    main()

"""Exact rational certificate for the lossless AM13 assembly.

This verifies the small continuous majorant, the AM energy bound and finite
algebra. It does not replay the separately admitted seven-gap PC8CL certificate
or formally verify the analytic zeta-zero counting argument.
Run without -O; use --check to compare the committed JSON report.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/am-lossless-majorant-certificate.json"
CS = [12310798, -15041681, 3867664, 6489926, -992327, 5580097,
      -6846472, 3781297, -5670353, 3355089, -450523, -218483]
ROWS = [[13630830, 0, 19565904, 20317441, 45030671, 100000000, 200000000],
        [29997996, 30621878, 47766489, 79682558, 109938656, 100000000],
        [37356140, 69378121, 65335210, 79682558, 45030671],
        [38030065, 69378121, 47766489, 20317441],
        [37356140, 30621878, 19565904], [29997996, 0], [13630830]]
BS = [28898, 57272, 75526, 80958, 75526, 57272, 28898]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    products = [x * y for x in a for y in b]
    return min(products), max(products)


def scale(a, k):
    return mul(a, (k, k))


def divide(a, b):
    assert b[0] > 0
    return mul(a, (1 / b[1], 1 / b[0]))


def atan_interval(n):
    value = sum(((-1)**k * Q(1, n**(2*k+1) * (2*k+1))
                 for k in range(24)), Q(0))
    return value, value + Q(1, n**49 * 49)


def trig_interval(q, sinc=False):
    """cos(sqrt(q)) or sin(sqrt(q))/sqrt(q), including the removable zero.

    All consumed q intervals lie in [0, 10). Terms from index 13 onward
    decrease in absolute value; the alternating tail is bounded by its first
    term. Interval arithmetic encloses the preceding polynomial.
    """
    assert 0 <= q[0] <= q[1] < 10
    value, power = (Q(0), Q(0)), (Q(1), Q(1))
    for k in range(13):
        value = add(value, scale(power, Q((-1)**k, factorial(2*k + int(sinc)))))
        power = mul(power, q)
    remainder = q[1]**13 / factorial(26 + int(sinc))
    return value[0] - remainder, value[1] + remainder


def certificate():
    assert __debug__, "Optimized Python disables required assertions"
    machin = add(scale(atan_interval(5), 16), scale(atan_interval(239), -4))
    pi = Q(3141592653, 10**9), Q(3141592654, 10**9)
    assert pi[0] < machin[0] <= machin[1] < pi[1]
    pi2 = mul(pi, pi)
    norm = trig_interval((Q(1, 2), Q(1, 2)), True)
    assert norm[0] > Q(9, 10)
    cs = [Q(x, 10**9) for x in CS]
    assert sum(map(abs, cs)) == Q(6460471, 10**8) < Q(13, 200)
    theta, gamma = Q(4, 5), Q(61, 100)
    for k in range(129):
        u = Q(k, 256)
        numerator = trig_interval((2*u*u, 2*u*u))
        for j, cj in enumerate(cs, 1):
            phase = (2*j*u + 1) % 2 - 1
            numerator = add(numerator, scale(trig_interval(scale(pi2, phase*phase)), cj))
        density = divide(numerator, norm)
        h = add(trig_interval(scale(pi2, theta*theta*(u-Q(1, 2))**2), True),
                trig_interval(scale(pi2, theta*theta*(u+Q(1, 2))**2), True))
        majorant = scale(mul(h, h), gamma)
        assert majorant[0] - density[1] > Q(9, 100)
    derivative = 4*gamma*Q(22, 7)*theta + (
        Q(3, 2) + Q(44, 7)*sum((j*abs(c) for j, c in enumerate(cs, 1)), Q(0))) / Q(9, 10)
    assert derivative < 16
    continuous_margin = Q(9, 100) - Q(16, 512)
    assert continuous_margin == Q(47, 800) > 0
    # beta*cot(beta) = cos(beta)/sinc(beta), beta^2=1/2.
    cot_ratio = divide(trig_interval((Q(1, 2), Q(1, 2))), norm)
    base_gain_lower = Q(3, 2) - cot_ratio[1]
    twice_sin2_lower = norm[0]**2
    correction_upper = sum((c*c*(Q(1, 2)-1/(4*pi[1]**2*j*j))
                            for j, c in enumerate(cs, 1)), Q(0)) / twice_sin2_lower
    gain_lower = Q(67216841, 10**8)
    assert base_gain_lower - correction_upper > gain_lower
    capacities = [sum((Q(ROWS[i][s-1], 10**8) for i in range(8-s)), Q(0))
                  for s in range(1, 8)]
    assert all(cap <= 2 for cap in capacities)
    c, b = Q(805003, 10**8), sum((Q(x, 10**8) for x in BS), Q(0))
    assert b == Q(404350, 10**8)
    close_lower = Q(7, 30) - Q(39, 550)
    assert close_lower == Q(134, 825) and close_lower**2 > Q(1, 40) > c
    mass_upper = 2*gamma/theta * Q(5, 4)
    assert mass_upper == Q(61, 32) < 2
    bound = (gain_lower-b)/(1-c)
    benchmark = Q(1669159, 2478195)
    assert bound == Q(66812491, 99194997)
    difference = bound-benchmark
    assert difference == Q(719712074, 81941515196805) > 0
    return {
        "schema": "rh-weil-am-lossless-certificate-v1",
        "scope": "exact small continuous majorant, energy bound and finite algebra only",
        "not_verified_here": ["PC8CL global seven-gap certificate", "analytic zero-counting proof",
                              "full Lean kernel certification", "world-record priority"],
        "script_canonical_lf_sha256": hashlib.sha256(
            Path(__file__).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest(),
        "pi_interval": [str(x) for x in pi], "half_window_nodes_checked": 129,
        "grid_margin_strict_lower": "9/100", "derivative_strict_upper": "16",
        "nearest_node_distance_upper": "1/512",
        "continuous_majorant_margin_strict_lower": str(continuous_margin),
        "theta": str(theta), "gamma": str(gamma), "majorant_mass_upper": str(mass_upper),
        "normalized_smoothing_mass_required_strict_lower": "61/64",
        "close_kernel_strict_lower": str(close_lower), "close_kernel_squared_strict_lower": "1/40",
        "am_energy_gain_strict_lower": str(gain_lower), "local_reward": str(c),
        "gap_fee": str(b), "span_capacities": [str(x) for x in capacities],
        "simple_critical_proportion_lower": str(bound),
        "checked_paper_benchmark": str(benchmark), "positive_difference": str(difference),
        "status": "PASS",
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
        print("PASS exact continuous majorant, AM energy and committed report")
    else:
        OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
        print("PASS; wrote output/am-lossless-majorant-certificate.json")


if __name__ == "__main__":
    main()

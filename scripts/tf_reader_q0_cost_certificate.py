"""Executed, outward-rounded cost/residual input for the fixed h0 q0 reader.

This does not compute a nonzero-trial q0 value. It verifies the finite B h0
step input exactly and produces genuine sufficient polynomial-degree bounds.
The zero trial is a valid but usually uninformative full-Hilbert certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path

from tf_reader_arch_gap_certificate import Intervals, floor_fraction, ceil_fraction


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)


def reciprocal_sqrt_interval(p: int, scale: int):
    lower = isqrt(scale*scale//p)
    assert p*lower*lower <= scale*scale < p*(lower+1)*(lower+1)
    return F(lower, scale), F(lower+1, scale)


def outward_power(base, n: int, arithmetic: Intervals):
    result = arithmetic.enclose(F(1))
    while n:
        if n & 1:
            result = arithmetic.mul(result, base)
        base = arithmetic.mul(base, base)
        n >>= 1
    return result


def first_sufficient_exponent(base, factor: F, target: F, arithmetic: Intervals):
    def test(n):
        power = outward_power(base, 2*n, arithmetic)
        upper = factor*F(power[1], arithmetic.unit)
        return upper <= target, upper, power
    low, high = 0, 1
    while not test(high)[0]:
        high *= 2
        if high > 2**30:
            raise ArithmeticError("The fixed sufficient certificate exceeds 2**30 iterations")
    while high-low > 1:
        middle = (high+low)//2
        if test(middle)[0]:
            high = middle
        else:
            low = middle
    passed, upper, power = test(high)
    assert passed
    previous = test(high-1)
    return {"exponent": high, "residual_squared_upper": str(upper),
            "target_squared": str(target),
            "power_interval_scaled": [str(power[0]), str(power[1])],
            "previous_sufficient_test_passed": previous[0],
            "interpretation": "First passing index for this outward sufficient envelope; not a necessary iteration lower bound."}


def finite_b_h0_steps():
    divisors = [(1, 1)]
    for p in PRIMES:
        divisors += [(d*p, -mu) for d, mu in divisors]
    divisors.sort()
    assert len(divisors) == 256 and divisors[-1][0] == 9699690
    events = {}
    for d, mu in divisors:
        coefficient = F(mu, d)
        events[d] = events.get(d, F(0))+coefficient
        events[2*d] = events.get(2*d, F(0))-coefficient
    amplitude = F(0)
    previous = min(events)
    norm2 = F(0)
    cells = []
    for endpoint, change in sorted(events.items()):
        if endpoint > previous and amplitude:
            norm2 += (endpoint-previous)*amplitude*amplitude
            cells.append({"left": previous, "right": endpoint,
                          "coefficient": str(amplitude)})
        amplitude += change
        previous = endpoint
    assert amplitude == 0
    # Independently verify the sweep norm through all exact pair overlaps.
    double_sum = sum((F(mu*nu, d*e)*max(0, min(2*d, 2*e)-max(d, e))
                      for d, mu in divisors for e, nu in divisors), F(0))
    assert norm2 == double_sum and norm2 > 0
    return divisors, cells, norm2


def short_fraction_bounds(value: F, scale: int):
    return [str(F(floor_fraction(value*scale), scale)),
            str(F(ceil_fraction(value*scale), scale))]


def build_record(precision: int):
    arithmetic = Intervals(precision)
    unit = arithmetic.unit
    mlow = mhigh = Mlow = Mhigh = F(1)
    sqrt_records = []
    for p in PRIMES:
        low, high = reciprocal_sqrt_interval(p, unit)
        sqrt_records.append({"p": p, "inverse_sqrt_interval": [str(low), str(high)]})
        mlow *= 1-high
        mhigh *= 1-low
        Mlow *= 1+low
        Mhigh *= 1+high
    # Publish fixed precision rational scalars before further operations.
    mlow = F(floor_fraction(mlow*unit), unit)
    mhigh = F(ceil_fraction(mhigh*unit), unit)
    Mlow = F(floor_fraction(Mlow*unit), unit)
    Mhigh = F(ceil_fraction(Mhigh*unit), unit)
    dlow = F(floor_fraction(mlow*mlow*unit), unit)
    dhigh = F(ceil_fraction(mhigh*mhigh*unit), unit)
    ulow = F(floor_fraction(Mlow*Mlow*unit), unit)
    uhigh = F(ceil_fraction(Mhigh*Mhigh*unit), unit)
    rho_low = (ulow-dhigh)/(ulow+dhigh)
    rho_high = (uhigh-dlow)/(uhigh+dlow)
    cheb_low = (Mlow-mhigh)/(Mlow+mhigh)
    cheb_high = (Mhigh-mlow)/(Mhigh+mlow)
    rho = arithmetic.enclose(rho_low, rho_high)
    cheb = arithmetic.enclose(cheb_low, cheb_high)
    divisors, cells, v2 = finite_b_h0_steps()
    # Keep a factor4 of the final residual-squared budget for action errors.
    target = dlow/F(128)
    neumann = first_sufficient_exponent(rho, v2, target, arithmetic)
    chebyshev = first_sufficient_exponent(cheb, 4*v2, target, arithmetic)
    residual_target_low = F(isqrt((dlow.numerator*unit*unit)//(32*dlow.denominator)), unit)
    assert residual_target_low**2 <= dlow/32
    zero_trial_width = min(F(1), v2/dlow)
    return {
      "schema": "tf-reader-q0-executed-cost-v1", "precision": precision,
      "scope": "Fixed physical h0=1_[1,2], original F8 and q0; exact input and sufficient-cost certificate only.",
      "primes": list(PRIMES), "N_F": 9699690,
      "h0_norm_squared": "1", "B_h0_step_sum_terms": len(divisors),
      "B_h0_nonzero_partition_cells": len(cells),
      "B_h0_norm_squared_exact": str(v2),
      "B_h0_norm_squared_sweep_equals_pair_overlap": True,
      "B_h0_norm_squared_decimal_enclosure": short_fraction_bounds(v2, 10**24),
      "B_h0_canonical_steps": cells,
      "inverse_sqrt_witnesses": sqrt_records,
      "m_interval": [str(mlow), str(mhigh)], "M_interval": [str(Mlow), str(Mhigh)],
      "d_interval": [str(dlow), str(dhigh)], "u_interval": [str(ulow), str(uhigh)],
      "rho_interval": [str(F(floor_fraction(rho_low*unit), unit)),
                       str(F(ceil_fraction(rho_high*unit), unit))],
      "chebyshev_contraction_upper": short_fraction_bounds(cheb_high, unit)[1],
      "residual_norm_safe_target": str(residual_target_low),
      "neumann_residual_certificate": neumann,
      "chebyshev_residual_certificate": chebyshev,
      "primitive_counts_for_exact_reference_on_M": {
          "neumann_P_actions": neumann["exponent"]+1,
          "chebyshev_P_actions": chebyshev["exponent"]+1,
          "chebyshev_cosine_actions_at_two_per_P": 2*(chebyshev["exponent"]+1),
          "chebyshev_dilation_actions_at_16_per_W": 16*chebyshev["exponent"],
          "note": "Factorized W uses8 three-term factors; numerical compression/reprojection and true-H errors still required. Counts are not runtime lower bounds."},
      "zero_trial_full_H_certificate": {
          "trial": "z=0", "J_interval": ["0", "0"],
          "true_residual_squared_upper": str(v2),
          "q0_interval": ["0", str(zero_trial_width)],
          "width_le_1_over_16": zero_trial_width <= F(1,16),
          "status": "Executed valid but non-accepting certificate; no q0 value inferred."},
      "unpaid": ["Actual nonzero trial construction", "Actual P/full inverse action residual enclosures", "J quadrature and arithmetic enclosure", "Final q0 interval width<=1/16", "Original five-source T/E and crossblocks"],
      "claim_limits": "Polynomial counts are conservative sufficient bounds, not required work or a method-class obstruction. No new mathematical round, signed sign, RH, whole-budget result, or completed Goal."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--precision", type=int, default=64)
    args = parser.parse_args()
    record = build_record(args.precision)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes((json.dumps(record, indent=2)+"\n").encode())
    print(json.dumps({"status": "executed-cost-and-zero-trial-only",
        "B_h0_norm_squared_enclosure": record["B_h0_norm_squared_decimal_enclosure"],
        "neumann_degree": record["neumann_residual_certificate"]["exponent"],
        "chebyshev_degree": record["chebyshev_residual_certificate"]["exponent"],
        "q0_acceptance": record["zero_trial_full_H_certificate"]["width_le_1_over_16"],
        "output": str(target)}))


if __name__ == "__main__":
    main()

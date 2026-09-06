#!/usr/bin/env python3
"""[E] Finite synthetic pole/carrier test; no actual zeta coefficients.

MP50; gamma=2, H=1/4, L=32,64,128, q=0,1/2,1.  S consists of
complete negative half-periods mirrored about the positive center gamma.
The output is -p_min * integral_S f(t) dt, the linear lower-functional
of the nonnegative test p_min/p(t) * 1_S(t).  This functional can be
negative.  It is NOT the full negative trace or its numerical evaluation.

Method 1 uses analytic entire-Ein endpoint primitives; the Abel version
uses an explicit finite exponential expansion with a factorial tail bound.
Method 2 independently integrates the original finite log-lag expression
after Fubini.  Ordinary MP arithmetic is not interval certification;
these finite checks do not prove an asymptotic, RH, or actual-record claim.
"""

from __future__ import annotations

import json
import time

import mpmath as mp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def entire_ein(value):
    # log + E1 has cancelling branch jumps; the combination is entire.
    # All nonzero arguments used below have nonzero imaginary part.
    if value == 0:
        return mp.mpf(0)
    return mp.euler + mp.log(value) + mp.e1(value)


def cosine_primitive(delta, length, frequency):
    """An h-primitive of integral_0^L exp(-delta*u) cos(h*u) du."""
    if frequency == 0:
        return mp.mpf(0)
    return mp.re(1j * entire_ein((delta - 1j * frequency) * length))


def make_test_set(length, gamma, half_width):
    halves, intervals = [], []
    k = 0
    while (2 * k + 2) * mp.pi <= length * half_width:
        left, right = (2 * k + 1) * mp.pi, (2 * k + 2) * mp.pi
        halves.append((left, right))
        intervals.extend([
            (gamma - right / length, gamma - left / length),
            (gamma + left / length, gamma + right / length),
        ])
        k += 1
    return halves, sorted(intervals)


def rectangular_endpoint_integral(delta, length, gamma, intervals):
    total = mp.mpf(0)
    cache = {}

    def primitive(frequency):
        # The primitive can be chosen odd: its derivative is even in h.
        sign = 1 if frequency >= 0 else -1
        key = abs(frequency)
        if key not in cache:
            cache[key] = cosine_primitive(delta, length, key)
        return sign * cache[key]

    for left, right in intervals:
        for shift in (-gamma, gamma):
            total += primitive(right + shift) - primitive(left + shift)
    return total


def original_fubini_integral(delta, length, gamma, halves, abel):
    """Both conjugate modes and both mirrored test intervals are retained."""
    def integrand(u):
        if u == 0:
            factor = sum((right - left) / length for left, right in halves)
        else:
            factor = sum(
                mp.sin(right * u / length) - mp.sin(left * u / length)
                for left, right in halves
            ) / u
        weight = mp.exp(-delta * u)
        if abel:
            weight *= mp.exp(-mp.exp(u - length))
        # One cos(gamma*u) is from the pole pair; the other is from
        # the mirrored interval endpoints.  This is not a single mode.
        return 4 * weight * mp.cos(gamma * u) ** 2 * factor

    panels = [length * k / 8 for k in range(9)]
    return mp.quad(integrand, panels)


def main():
    mp.mp.dps = 50
    started = time.perf_counter()
    gamma, half_width = mp.mpf(2), mp.mpf(1) / 4
    order = 18
    tolerance = mp.mpf("1e-36")
    p_min = 1 / (mp.pi * (1 + (gamma + half_width) ** 2))
    amplitudes = tuple(mp.mpf(value) for value in (0, 1, -1, 1000, -1000))
    rows = []
    max_carrier_error = max_rect_error = max_amplitude_error = mp.mpf(0)
    max_abel_tail_ratio = mp.mpf(0)

    for integer_length in (32, 64, 128):
        length = mp.mpf(integer_length)
        halves, intervals = make_test_set(length, gamma, half_width)
        require(halves, "test set unexpectedly empty")
        measure = sum(right - left for left, right in intervals)
        require(0 < measure <= 2 * half_width, "test support escaped the chosen window")
        carrier_endpoints = sum(
            (mp.sin(length * right) - mp.sin(length * left)) / length
            for left, right in intervals
        )
        # An independent finite integral tests the actual phase cos(L*t).
        carrier_quad = sum(mp.quad(lambda t: mp.cos(length * t), [left, right])
                           for left, right in intervals)
        max_carrier_error = max(max_carrier_error, abs(carrier_endpoints), abs(carrier_quad))
        require(abs(carrier_endpoints) <= tolerance, "endpoint carrier annihilation failed")
        require(abs(carrier_quad) <= tolerance, "quadrature carrier annihilation failed")

        for q in (mp.mpf(0), mp.mpf("0.5"), mp.mpf(1)):
            delta = q / length
            require(0 <= delta < 1, "factorial Abel tail requires delta<1")
            rect_endpoint = rectangular_endpoint_integral(delta, length, gamma, intervals)
            rect_fubini = original_fubini_integral(delta, length, gamma, halves, abel=False)
            rect_error = abs(rect_endpoint - rect_fubini) / (1 + abs(rect_fubini))
            require(rect_error <= tolerance, "rectangular endpoint/Fubini identity failed")
            max_rect_error = max(max_rect_error, rect_error)

            # exp(-exp(u-L)) = sum_k (-1)^k exp(k*(u-L))/k!.
            # The k-th term uses the same finite primitive with delta-k;
            # it is never replaced by an infinite Mellin integral.
            abel_endpoint = mp.mpf(0)
            for k in range(order + 1):
                abel_endpoint += (
                    (-1) ** k * mp.exp(-k * length) / mp.factorial(k)
                    * rectangular_endpoint_integral(delta - k, length, gamma, intervals)
                )
            abel_fubini = original_fubini_integral(delta, length, gamma, halves, abel=True)
            # For k>=order+1, integral exp(-delta*u+k*(u-L))du
            # <= exp(-q)/(k-delta); sum the factorial tail geometrically.
            # The factor 2 retains the full real conjugate pair.
            abel_tail_bound = (
                4 * measure * mp.exp(-q)
                / ((order + 1 - delta) * mp.factorial(order + 1))
            )
            abel_error = abs(abel_endpoint - abel_fubini)
            require(abel_error <= abel_tail_bound + tolerance, "finite Abel series exceeded its explicit tail bound")
            max_abel_tail_ratio = max(max_abel_tail_ratio, abel_error / abel_tail_bound)

            # The test functional is unchanged for every displayed
            # physical carrier amplitude, including both large signs.
            amplitude_errors = []
            for amplitude in amplitudes:
                rect_with_carrier = rect_fubini - amplitude * carrier_quad
                abel_with_carrier = abel_fubini - amplitude * carrier_quad
                error = max(abs(rect_with_carrier - rect_fubini),
                            abs(abel_with_carrier - abel_fubini))
                require(error <= tolerance * (1 + abs(amplitude)), "carrier amplitude changed the linear test functional")
                amplitude_errors.append(error)
                max_amplitude_error = max(max_amplitude_error, error)

            # The uniform POINTWISE Abel-vs-rectangular bound, multiplied
            # by the Lebesgue measure of S, bounds these ordinary integrals.
            finite_difference_bound = 2 * measure * mp.exp(-q) / (1 - delta)
            require(abs(abel_fubini - rect_fubini) <= finite_difference_bound + tolerance,
                    "finite-test Abel/rectangle difference bound failed")

            rows.append({
                "L": integer_length,
                "q": mp.nstr(q, 12),
                "delta": mp.nstr(delta, 12),
                "test_intervals": len(intervals),
                "test_measure": mp.nstr(measure, 12),
                "integral_S_R_rect": mp.nstr(rect_fubini, 14),
                "integral_S_R_Abel": mp.nstr(abel_fubini, 14),
                "rect_lower_functional_NOT_kappa": mp.nstr(-p_min * rect_fubini, 14),
                "Abel_lower_functional_NOT_kappa": mp.nstr(-p_min * abel_fubini, 14),
                "rect_endpoint_scaled_error": mp.nstr(rect_error, 8),
                "Abel_endpoint_error": mp.nstr(abel_error, 8),
                "Abel_factorial_tail_bound": mp.nstr(abel_tail_bound, 8),
                "max_amplitude_invariance_error": mp.nstr(max(amplitude_errors), 8),
            })

    require(len(rows) == 9, "the preregistered grid changed")
    print(json.dumps({
        "status": "PASS",
        "evidence": "[E] MP50 synthetic gamma=2; no actual zeros, arithmetic source, records, or full-axis negative-trace computation.",
        "test_definition": "Complete negative half-periods of sin(L*(t-gamma)), mirrored about gamma, inside |t-gamma|<=1/4; fixed unweighted test integrals.",
        "warning": "Only a nonnegative test's linear lower-functional is output. It may be negative and is not full kappa. No finite asymptotic closeness is asserted.",
        "carrier_amplitudes": [0, 1, -1, 1000, -1000],
        "Abel_expansion_last_order": order,
        "max_carrier_annihilation_error": mp.nstr(max_carrier_error, 10),
        "max_rect_endpoint_Fubini_scaled_error": mp.nstr(max_rect_error, 10),
        "max_Abel_endpoint_error_to_tail_bound": mp.nstr(max_abel_tail_ratio, 10),
        "max_amplitude_invariance_error": mp.nstr(max_amplitude_error, 10),
        "cases": rows,
        "elapsed_seconds": round(time.perf_counter() - started, 3),
    }, indent=2))


if __name__ == "__main__":
    main()

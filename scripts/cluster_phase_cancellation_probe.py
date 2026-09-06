#!/usr/bin/env python3
"""[E] MP50 synthetic two-pair phase-cancellation checks, not actual zeta.

The two positive centers are gamma=2 and gamma+d, d=pi/L; their negative
reflections are included.  L=32,64,128 and q=1,log(log(L)), delta=q/L.
We check four-branch rectangular identities, independent original lag
integrals, the Abel correction bound, complete nonoscillatory tail norms,
and the Cauchy--Schwarz majorant.  No full negative trace is computed.

For a=delta+i(t-gamma), b=delta+i(t+gamma), E=exp(-q), the merged tails are
  T+ = -i*d*E*exp(i*(gamma-t)*L)/(a*(a-i*d)),
  T- = +i*d*E*exp(-i*(gamma+t)*L)/(b*(b+i*d)).
The rectangular real symbol is a nonnegative four-Poisson background minus
Re(T++T-).  The analytic bound is
  kappa_Abel <= E*(2*pi/q + 4/(1-delta)).
The finite checks do not themselves prove this uniform bound or asymptotic.

Tail Cauchy norms use t=tan(theta), -pi/2<=theta<=pi/2, with the stable
sine/cosine integrand below; its endpoint limit is zero.  The unweighted
CS kernel uses t=gamma+d/2+delta*tan(theta); after multiplying by delta
its endpoint limit is one.  Thus these transformed quadratures include
the entire real axis, with no omitted numerical tail.  They are ordinary
MP quadrature, not interval certificates; their error estimates are only
numerical diagnostics.  No files, dependencies, or actual-zero data are
created or modified by running this script.
"""

from __future__ import annotations

import json
import time

import mpmath as mp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def scalar(value):
    return mp.nstr(value, 14)


def rectangular_data(length, delta, gamma, physical_t):
    spacing = mp.pi / length
    amplitude = mp.exp(-delta * length)
    centers = (gamma, gamma + spacing, -gamma, -gamma - spacing)
    denominators = [delta + 1j * (physical_t - center) for center in centers]
    branch_tails = [mp.exp(-denom * length) / denom for denom in denominators]
    rectangular = mp.re(sum(-mp.expm1(-denom * length) / denom for denom in denominators))
    poisson = sum(delta / (delta**2 + (physical_t - center)**2) for center in centers)
    a = delta + 1j * (physical_t - gamma)
    b = delta + 1j * (physical_t + gamma)
    positive = -1j * spacing * amplitude * mp.exp(1j * (gamma - physical_t) * length)
    positive /= a * (a - 1j * spacing)
    negative = 1j * spacing * amplitude * mp.exp(-1j * (gamma + physical_t) * length)
    negative /= b * (b + 1j * spacing)
    errors = [
        abs(sum(branch_tails[:2]) - positive),
        abs(sum(branch_tails[2:]) - negative),
        abs(rectangular - (poisson - mp.re(positive + negative))),
    ]
    return rectangular, poisson, positive, negative, max(errors)


def independent_lag(length, delta, gamma, physical_t, abel):
    spacing = mp.pi / length
    largest_frequency = abs(gamma) + spacing + abs(physical_t)
    pieces = max(1, int(mp.ceil(largest_frequency * length / (16 * mp.pi))))
    points = [length * j / pieces for j in range(pieces + 1)]

    def integrand(u):
        weight = mp.exp(-delta * u)
        if abel:
            weight *= mp.exp(-mp.exp(u - length))
        return 2 * weight * (mp.cos(gamma * u) + mp.cos((gamma + spacing) * u)) * mp.cos(physical_t * u)

    return mp.quad(integrand, points)


def complete_tail_norm(delta, first_center, second_center, amplitude, spacing):
    half_pi = mp.pi / 2

    def integrand(theta):
        if abs(theta) == half_pi:
            return mp.mpf(0)
        sine, cosine = mp.sin(theta), mp.cos(theta)
        first = mp.sqrt((delta * cosine)**2 + (sine - first_center * cosine)**2)
        second = mp.sqrt((delta * cosine)**2 + (sine - second_center * cosine)**2)
        return cosine**2 / (first * second)

    # Resolve both resonance widths without truncating either infinite tail.
    cuts = {-half_pi, mp.mpf(0), half_pi}
    for center in (first_center, second_center):
        for multiple in (-4, -1, 0, 1, 4):
            cuts.add(mp.atan(center + multiple * delta))
    integral, estimate = mp.quad(integrand, sorted(cuts), error=True)
    prefactor = amplitude * spacing / mp.pi
    return prefactor * integral, prefactor * estimate


def complete_cs_integral(delta, spacing):
    """Return delta*integral_R 1/(two square-root factors) dt.

    After the centered tangent substitution this is the expression below.
    At both angular endpoints it tends to 1, not 0 or infinity.
    """
    half_pi = mp.pi / 2
    half_shift = spacing / (2 * delta)

    def integrand(theta):
        if abs(theta) == half_pi:
            return mp.mpf(1)
        sine, cosine = mp.sin(theta), mp.cos(theta)
        first = mp.sqrt(cosine**2 + (sine + half_shift * cosine)**2)
        second = mp.sqrt(cosine**2 + (sine - half_shift * cosine)**2)
        return 1 / (first * second)

    return mp.quad(integrand, [-half_pi, 0, half_pi], error=True)


def main():
    started = time.perf_counter()
    mp.mp.dps = 50
    tolerance = mp.mpf("1e-42")
    gamma = mp.mpf(2)
    maxima = {name: mp.mpf(0) for name in (
        "scaled_identity_error", "scaled_rectangular_lag_error",
        "abel_difference_over_positive_lag_cap", "positive_lag_cap_over_analytic_cap",
        "single_tail_norm_over_pi_E_over_q", "CS_integral_over_pi",
        "tail_reflection_error", "reported_quadrature_error",
    )}
    cases = 0
    for length_input in (32, 64, 128):
        length = mp.mpf(length_input)
        for q_label, q in (("1", mp.mpf(1)), ("loglogL", mp.log(mp.log(length)))):
            cases += 1
            delta, spacing, amplitude = q / length, mp.pi / length, mp.exp(-q)
            require(1 <= q and 0 < delta <= mp.mpf("0.25"), "registered parameter range")
            case_identity, case_lag = mp.mpf(0), mp.mpf(0)
            locations = [mp.mpf(0)]
            for center in (gamma, gamma + spacing / 2, gamma + spacing):
                locations.extend([center, -center])
            for physical_t in locations:
                rectangular, poisson, positive, negative, error = rectangular_data(length, delta, gamma, physical_t)
                scale = max(1, abs(rectangular), poisson, abs(positive), abs(negative))
                require(error <= tolerance * scale, "merged tails / four-Poisson identity")
                require(poisson > 0, "positive infinite-kernel background")
                require(max(-rectangular, 0) <= abs(positive) + abs(negative) + tolerance * scale,
                        "pointwise rectangular negative-part upper bound")
                case_identity = max(case_identity, error / scale)

            # Positive lag upper bound for the entire two-pair Abel difference.
            # The v=L-u form avoids numerical underflow/cancellation for u<<L.
            lag_cap = 4 * amplitude * mp.quad(
                lambda v: mp.exp(delta * v) * (-mp.expm1(-mp.exp(-v))),
                [0, 1, 4, 16, length],
            )
            analytic_abel_cap = 4 * amplitude / (1 - delta)
            require(lag_cap <= analytic_abel_cap + tolerance, "complete positive Abel lag cap")
            case_abel_ratio = mp.mpf(0)
            for physical_t in (mp.mpf(0), gamma, gamma + spacing / 2):
                rectangular = rectangular_data(length, delta, gamma, physical_t)[0]
                original_rectangle = independent_lag(length, delta, gamma, physical_t, False)
                original_abel = independent_lag(length, delta, gamma, physical_t, True)
                scale = max(1, abs(rectangular), abs(original_rectangle))
                error = abs(rectangular - original_rectangle)
                require(error <= tolerance * scale, "independent original rectangular lag integral")
                require(abs(original_abel - original_rectangle) <= lag_cap + tolerance * scale,
                        "independent Abel difference / full positive lag bound")
                case_lag = max(case_lag, error / scale)
                case_abel_ratio = max(case_abel_ratio, abs(original_abel - original_rectangle) / lag_cap)

            norm_positive, estimate_positive = complete_tail_norm(delta, gamma, gamma + spacing, amplitude, spacing)
            norm_negative, estimate_negative = complete_tail_norm(delta, -gamma, -gamma - spacing, amplitude, spacing)
            cs_value, estimate_cs = complete_cs_integral(delta, spacing)
            single_tail_cap = mp.pi * amplitude / q
            require(max(norm_positive, norm_negative) <= single_tail_cap + tolerance, "complete Cauchy tail norm cap")
            require(cs_value <= mp.pi + tolerance, "complete CS majorant")
            require(abs(norm_positive - norm_negative) <= tolerance, "reflection of Cauchy tail norms")
            reported_error = max(estimate_positive, estimate_negative, estimate_cs)
            require(reported_error <= mp.mpf("1e-35"), "transformed quadrature numerical stability diagnostic")
            maxima["scaled_identity_error"] = max(maxima["scaled_identity_error"], case_identity)
            maxima["scaled_rectangular_lag_error"] = max(maxima["scaled_rectangular_lag_error"], case_lag)
            maxima["abel_difference_over_positive_lag_cap"] = max(maxima["abel_difference_over_positive_lag_cap"], case_abel_ratio)
            maxima["positive_lag_cap_over_analytic_cap"] = max(maxima["positive_lag_cap_over_analytic_cap"], lag_cap / analytic_abel_cap)
            maxima["single_tail_norm_over_pi_E_over_q"] = max(maxima["single_tail_norm_over_pi_E_over_q"], norm_positive / single_tail_cap, norm_negative / single_tail_cap)
            maxima["CS_integral_over_pi"] = max(maxima["CS_integral_over_pi"], cs_value / mp.pi)
            maxima["tail_reflection_error"] = max(maxima["tail_reflection_error"], abs(norm_positive - norm_negative))
            maxima["reported_quadrature_error"] = max(maxima["reported_quadrature_error"], reported_error)
            print(json.dumps({
                "status": "[E] PASS", "L": length_input, "q_rule": q_label, "q": scalar(q),
                "scaled_identity_error": scalar(case_identity),
                "scaled_rectangular_lag_error": scalar(case_lag),
                "complete_positive_tail_Cauchy_norm": scalar(norm_positive),
                "single_tail_analytic_cap": scalar(single_tail_cap),
                "CS_integral_over_pi": scalar(cs_value / mp.pi),
                "Abel_lag_cap_over_analytic_cap": scalar(lag_cap / analytic_abel_cap),
            }))

    phase_rows = []
    for label, shift, expected in (("(0,0)", 0, 2), ("(0,pi)", mp.pi, 0), ("(0,2pi)", 2 * mp.pi, 2)):
        phase_sum = 1 + mp.exp(1j * shift)
        require(abs(phase_sum - expected) <= tolerance, "finite phase-sum identity")
        phase_rows.append({"shifts": label, "real": scalar(mp.re(phase_sum)), "imag": scalar(mp.im(phase_sum))})
    print(json.dumps({"status": "[E] PASS", "finite_phase_sums": phase_rows}))
    print(json.dumps({
        "status": "PASS", "label": "[E] synthetic identities and nonoscillatory norms only",
        "dps": mp.mp.dps, "cases": cases,
        "maxima": {name: scalar(value) for name, value in maxima.items()},
        "seconds": round(time.perf_counter() - started, 3),
        "full_negative_trace_computed": False,
        "whole_axis_tail_norms": "complete tangent substitutions; ordinary MP quadrature, not certification",
    }))


if __name__ == "__main__":
    main()

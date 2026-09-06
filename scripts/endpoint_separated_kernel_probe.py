#!/usr/bin/env python3
"""[E] MP50 checks of six synthetic endpoint-separated Fourier kernels.

For u0=log(2), L>u0, 0<delta<=1/4, q=delta*L, set, on u>=u0,
  k(u)=exp(-delta*u)*(1-exp(-exp(u-L))*1_{u<=L}),
  v(u)=exp(-delta*u+u-L-exp(u-L))*1_{u<=L}.
Both functions are extended by zero below u0.  Their lower jump and both
cutoff jumps are included in total variation.  Fourier convention is +iru.

A finite exponential series is compared with independent finite log-lag
quadrature; the infinite tail of k is integrated analytically.  Explicit
factorial truncation bounds are printed separately from numerical roundoff.
The BV/L1/Fourier cap checks use only these finite synthetic configurations.
Ordinary MP quadrature is not certified interval arithmetic.  This script
does not evaluate a full-axis Cauchy norm, use actual zeros or von Mangoldt
coefficients, certify records, or prove any uniform/asymptotic theorem.
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


def lag_breaks(lower, length, frequency):
    # At most eight oscillations per subinterval.  The quadrature evaluates
    # the original lag functions, not the series or an incomplete gamma.
    pieces = max(1, int(mp.ceil(abs(frequency) * (length - lower) / (16 * mp.pi))))
    return [lower + (length - lower) * j / pieces for j in range(pieces + 1)]


def lag_kernels(length, delta, frequency):
    lower = mp.log(2)
    exponent = -delta + 1j * frequency
    points = lag_breaks(lower, length, frequency)
    lower_k = mp.quad(
        lambda u: mp.exp(exponent * u) * (-mp.expm1(-mp.exp(u - length))),
        points,
    )
    kernel_v = mp.quad(
        lambda u: mp.exp(exponent * u + u - length - mp.exp(u - length)),
        points,
    )
    # delta>0: this is the entire [L,infinity) tail, not a finite truncation.
    kernel_k = lower_k - mp.exp(exponent * length) / exponent
    return kernel_k, kernel_v


def series_kernels(length, delta, frequency, order):
    """K includes n=1..order; V includes n=0..order.

    Alternating exponential remainders on 0<=x<=1 give
      err_K <= E*(1-x0**(order+1-delta)) /
                    ((order+1)!*(order+1-delta)),
      err_V <= E*(1-x0**(order+2-delta)) /
                    ((order+1)!*(order+2-delta)).
    These are absolute, frequency-uniform truncation bounds.
    """
    exponent = -delta + 1j * frequency
    log_x0 = mp.log(2) - length
    prefactor = mp.exp(exponent * length)
    value_k = -1 / exponent
    value_v = mp.mpc(0)
    coefficient = mp.mpf(1)
    for n in range(order + 1):
        if n:
            coefficient *= -mp.mpf(1) / n
            value_k -= coefficient * (-mp.expm1((exponent + n) * log_x0)) / (exponent + n)
        value_v += coefficient * (-mp.expm1((exponent + n + 1) * log_x0)) / (exponent + n + 1)
    amplitude = mp.exp(-delta * length)
    factorial = mp.factorial(order + 1)
    powers = (order + 1 - delta, order + 2 - delta)
    errors = [
        amplitude * (-mp.expm1(power * log_x0)) / (factorial * power)
        for power in powers
    ]
    return prefactor * value_k, prefactor * value_v, errors[0], errors[1]


def path_checks(length, delta, tolerance):
    lower = mp.log(2)
    amplitude = mp.exp(-delta * length)

    def lower_k(u):
        return mp.exp(-delta * u) * (-mp.expm1(-mp.exp(u - length)))

    def lower_v(u):
        return mp.exp(-delta * u + u - length - mp.exp(u - length))

    def derivative_k(u):
        x = mp.exp(u - length)
        return mp.exp(-delta * u) * ((x + delta) * mp.exp(-x) - delta)

    def derivative_v(u):
        return (1 - delta - mp.exp(u - length)) * lower_v(u)

    norm_k = mp.quad(lower_k, [lower, length]) + amplitude / delta
    norm_v = mp.quad(lower_v, [lower, length])
    # k: lower jump + variation below L + positive jump E/e + tail variation E.
    tv_k = lower_k(lower) + mp.quad(lambda u: abs(derivative_k(u)), [lower, length])
    tv_k += amplitude / mp.e + amplitude
    peak = length + mp.log(1 - delta)
    points = [lower] + ([peak] if lower < peak < length else []) + [length]
    # v: lower jump + its full interior variation + the downward cutoff jump.
    tv_v = lower_v(lower) + mp.quad(lambda u: abs(derivative_v(u)), points) + amplitude / mp.e
    cap_k = 4 * amplitude / (3 * delta)
    cap_v = 4 * amplitude / 3
    require(norm_k <= cap_k + tolerance, "L1 k cap")
    require(norm_v <= cap_v + tolerance, "L1 v cap")
    require(abs(tv_k - 2 * amplitude) <= tolerance, "k total variation includes all jumps")
    require(tv_v <= 2 * amplitude + tolerance, "v total variation cap")
    return norm_k, norm_v, tv_k, tv_v, amplitude


def main():
    started = time.perf_counter()
    mp.mp.dps = 50
    order = 32
    tolerance = mp.mpf("1e-44")
    configurations = [
        (4, "0.25", 0), (4, "0.05", 2), (8, "0.25", 2),
        (8, "0.05", 16), (16, "0.25", 16), (16, "0.05", 40),
    ]
    maxima = {name: mp.mpf(0) for name in [
        "series_error", "error_over_factorial_bound", "scaled_lag_error",
        "l1_k_cap_ratio", "l1_v_cap_ratio", "tv_v_cap_ratio",
        "tv_k_identity_error", "fourier_cap_ratio", "factorial_bound",
    ]}
    total_checks = 0
    for length_input, delta_input, gamma_input in configurations:
        length, delta, gamma = map(mp.mpf, (length_input, delta_input, gamma_input))
        norm_k, norm_v, tv_k, tv_v, amplitude = path_checks(length, delta, tolerance)
        maxima["l1_k_cap_ratio"] = max(maxima["l1_k_cap_ratio"], norm_k * 3 * delta / (4 * amplitude))
        maxima["l1_v_cap_ratio"] = max(maxima["l1_v_cap_ratio"], norm_v * 3 / (4 * amplitude))
        maxima["tv_v_cap_ratio"] = max(maxima["tv_v_cap_ratio"], tv_v / (2 * amplitude))
        maxima["tv_k_identity_error"] = max(maxima["tv_k_identity_error"], abs(tv_k - 2 * amplitude))
        case_error, case_factorial, case_cap = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        # Keep all four requested physical frequencies, including the repeated
        # t=0 for gamma=0; each check is explicitly tied to its physical t.
        for physical_t in (gamma, gamma - delta, gamma + delta, mp.mpf(0)):
            frequency = gamma - physical_t
            lag_k, lag_v = lag_kernels(length, delta, frequency)
            series_k, series_v, bound_k, bound_v = series_kernels(length, delta, frequency, order)
            for label, exact, series, bound, norm, variation in [
                ("k", lag_k, series_k, bound_k, norm_k, tv_k),
                ("v", lag_v, series_v, bound_v, norm_v, tv_v),
            ]:
                error = abs(exact - series)
                rounding_allowance = tolerance * max(1, norm)
                require(error <= bound + rounding_allowance, f"{label}: finite-series factorial remainder")
                cap = norm if frequency == 0 else min(norm, variation / abs(frequency))
                require(abs(exact) <= cap + rounding_allowance, f"{label}: L1/BV Fourier cap")
                # For these fixed values the factorial bound is much larger
                # than the roundoff allowance; print both, never conflate them.
                require(rounding_allowance < bound / 100, "precision resolves factorial truncation")
                maxima["series_error"] = max(maxima["series_error"], error)
                maxima["error_over_factorial_bound"] = max(maxima["error_over_factorial_bound"], error / bound)
                maxima["scaled_lag_error"] = max(maxima["scaled_lag_error"], error / max(1, norm))
                maxima["fourier_cap_ratio"] = max(maxima["fourier_cap_ratio"], abs(exact) / cap)
                maxima["factorial_bound"] = max(maxima["factorial_bound"], bound)
                case_error, case_factorial = max(case_error, error), max(case_factorial, bound)
                case_cap = max(case_cap, abs(exact) / cap)
                total_checks += 1
        print(json.dumps({
            "status": "[E] PASS", "L": length_input, "delta": delta_input,
            "synthetic_gamma": gamma_input, "q": scalar(delta * length),
            "max_series_vs_lag_error": scalar(case_error),
            "max_explicit_factorial_bound": scalar(case_factorial),
            "max_fourier_cap_ratio": scalar(case_cap),
        }, ensure_ascii=False))
    print(json.dumps({
        "status": "PASS", "label": "[E] synthetic finite checks only",
        "dps": mp.mp.dps, "series_order": order, "configurations": len(configurations),
        "individual_transform_checks": total_checks,
        "base_roundoff_allowance": scalar(tolerance),
        "maxima": {name: scalar(value) for name, value in maxima.items()},
        "seconds": round(time.perf_counter() - started, 3),
        "full_axis_Cauchy_integral_computed": False,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

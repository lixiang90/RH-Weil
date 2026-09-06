#!/usr/bin/env python3
"""[E] Finite synthetic critical-pole boundary checks; no actual zeta data.

The nine cases use gamma=2, L=64,256,1024 and z=0,log(log L),
2*log(log L), with delta=z/L and Y=exp(L).  ``kappa_loc_primary``
is the sum of the negative parts of ONE primary rectangular pole in
each of the two windows |t-gamma|<=epsilon and |t+gamma|<=epsilon.
It is NOT the negative trace of the full conjugate pair, nor the full
Abel trace.  The off-resonant pole, outside-window, and Abel corrections
are bounded separately.  No full-axis oscillatory quadrature is used.

All checks are ordinary MP50 numerical checks, not interval certificates.
Finite agreement does not prove the uniform asymptotic, locate actual
zeros, certify a record, or establish an RH/GRH consequence.
"""

from __future__ import annotations

import argparse
import json
import time

import mpmath as mp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def cauchy(t):
    return 1 / (mp.pi * (1 + t * t))


def rectangular_cos(delta, length, omega):
    """Integral_0^L exp(-delta*u) cos(omega*u) du, including (0,0)."""
    if delta == 0 and omega == 0:
        return length
    z = delta * length
    return (
        delta
        + mp.exp(-z)
        * (-delta * mp.cos(omega * length) + omega * mp.sin(omega * length))
    ) / (delta * delta + omega * omega)


def rectangular_pair(delta, length, gamma, t):
    return rectangular_cos(delta, length, gamma + t) + rectangular_cos(
        delta, length, gamma - t
    )


def abel_complex(s, length):
    """Finite positive-endpoint gamma integral: entire in s, even at s=0."""
    return mp.exp(s * length) * mp.gammainc(s, mp.exp(-length), 1)


def abel_pair(delta, length, gamma, t):
    return mp.re(
        abel_complex(-delta + 1j * (gamma + t), length)
        + abel_complex(-delta + 1j * (gamma - t), length)
    )


def prefix_quad(function, length):
    """Dyadic panels resolve the decaying non-oscillatory/low-mode tails."""
    nodes = [mp.mpf(0)]
    node = mp.mpf(1)
    while node < length:
        nodes.append(node)
        node *= 2
    nodes.append(length)
    return mp.quad(function, nodes)


def bracket_root(function, left, right, tol):
    """Deterministic safeguarded bisection, not an unbracketed root guess."""
    f_left, f_right = function(left), function(right)
    if f_left == 0:
        return left
    if f_right == 0:
        return right
    require(f_left * f_right < 0, "root interval does not bracket a sign change")
    for _ in range(max(240, 4 * mp.mp.dps + 32)):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_middle == 0 or right - left <= tol * (1 + abs(middle)):
            return middle
        if f_left * f_middle < 0:
            right, f_right = middle, f_middle
        else:
            left, f_left = middle, f_middle
    raise AssertionError("bracketed bisection did not converge")


def primary_window_trace(length, z, gamma, epsilon, root_tol):
    """Exact rectangular primary kernel, with all negative roots split."""
    end = epsilon * length
    drift_max = z * (mp.exp(z) + 1)
    total = mp.mpf(0)
    periods = negative_pieces = no_negative_periods = clipped_periods = 0
    max_root_residual = mp.mpf(0)

    def numerator(y):
        return y * mp.sin(y) + z * (mp.exp(z) - mp.cos(y))

    def derivative(y):
        return (1 + z) * mp.sin(y) + y * mp.cos(y)

    k = 0
    while (2 * k + 1) * mp.pi < end:
        left = (2 * k + 1) * mp.pi
        right = (2 * k + 2) * mp.pi
        periods += 1
        if z == 0:
            first, last = left, right
        else:
            # On (3*pi/2+2*k*pi, 2*pi+2*k*pi), the derivative
            # is strictly increasing from -(1+z) to right.
            valley = bracket_root(
                derivative, (2 * k + mp.mpf("1.5")) * mp.pi, right, root_tol
            )
            require(left < valley < right, "valley left its negative half-period")
            if numerator(valley) >= 0:
                no_negative_periods += 1
                k += 1
                continue
            first = bracket_root(numerator, left, valley, root_tol)
            last = bracket_root(numerator, valley, right, root_tol)
            for root in (first, last):
                residual = abs(numerator(root)) / (1 + abs(root) + drift_max)
                max_root_residual = max(max_root_residual, residual)
            require(first < valley < last, "negative interval lost its valley")
            require(numerator((first + last) / 2) < 0, "negative root interval has wrong sign")

        if first >= end:
            clipped_periods += 1
            k += 1
            continue
        last = min(last, end)
        require(first < last, "empty negative interval was integrated")

        def integrand(y):
            # R=2 Re K: two conjugate resonances and both sides of each
            # resonance give the two weights and the factor 2 below.
            density = cauchy(gamma + y / length) + cauchy(gamma - y / length)
            return -numerator(y) * density / (y * y + z * z)

        piece = mp.quad(integrand, [first, (first + last) / 2, last])
        require(piece >= 0, "negative-part integral became negative")
        total += piece
        negative_pieces += 1
        k += 1

    if z * mp.expm1(z) >= end:
        # N(y)>=-y+z(exp(z)-1)>=0 throughout this finite window.
        require(negative_pieces == 0 and total == 0, "failed analytic no-negative-root branch")

    return 2 * mp.exp(-z) * total, {
        "negative_half_periods_examined": periods,
        "negative_pieces": negative_pieces,
        "no_negative_periods": no_negative_periods,
        "pieces_beyond_window": clipped_periods,
        "max_scaled_root_residual": max_root_residual,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=50, help="working precision (at least 50)")
    args = parser.parse_args()
    require(args.dps >= 50, "this preregistered probe requires at least MP50")
    mp.mp.dps = args.dps
    started = time.perf_counter()
    gamma, epsilon = mp.mpf(2), mp.mpf(1) / 4
    tolerance = mp.mpf(10) ** (-args.dps + 12)
    root_tol = mp.mpf(10) ** (-args.dps + 5)

    def fmt(value):
        return mp.nstr(value, 14)

    # Independent original-integral checks deliberately use a short L=4.
    # They include the removable (delta,omega)=(0,0) resonance and nearby t.
    short_length = mp.mpf(4)
    point_specs = [
        (mp.mpf(0), mp.mpf(0)),
        (mp.mpf(0), gamma),
        (mp.mpf(0), gamma + mp.mpf("1e-12")),
        (mp.mpf("0.1"), mp.mpf("0.37")),
        (mp.mpf("0.1"), gamma),
        (mp.mpf("0.1"), gamma - mp.mpf("1e-12")),
    ]
    max_rect_error = max_abel_error = max_point_difference_ratio = mp.mpf(0)
    for delta, t in point_specs:
        raw_rect = 2 * mp.quad(
            lambda u: mp.exp(-delta * u) * mp.cos(gamma * u) * mp.cos(t * u),
            [0, 1, 2, short_length],
        )
        raw_abel = 2 * mp.quad(
            lambda u: mp.exp(-delta * u - mp.exp(u - short_length))
            * mp.cos(gamma * u)
            * mp.cos(t * u),
            [0, 1, 2, short_length],
        )
        closed_rect = rectangular_pair(delta, short_length, gamma, t)
        closed_abel = abel_pair(delta, short_length, gamma, t)
        rect_error = abs(closed_rect - raw_rect) / (1 + abs(raw_rect))
        abel_error = abs(closed_abel - raw_abel) / (1 + abs(raw_abel))
        require(rect_error <= tolerance, "rectangular closed form failed original-integral check")
        require(abel_error <= tolerance, "finite gamma formula failed original-integral check")
        max_rect_error = max(max_rect_error, rect_error)
        max_abel_error = max(max_abel_error, abel_error)
        point_budget = 2 * mp.exp(-delta * short_length) / (1 - delta)
        max_point_difference_ratio = max(
            max_point_difference_ratio, abs(closed_abel - closed_rect) / point_budget
        )
        require(abs(closed_abel - closed_rect) <= point_budget + tolerance, "Abel pointwise budget failed")

    require(rectangular_cos(0, short_length, 0) == short_length, "zero resonance lost its continuous value")
    mean_limit = 2 / (1 + gamma * gamma)
    coefficient = 4 / (mp.pi**2 * (1 + gamma * gamma))
    window_mass = 2 * (
        mp.atan(gamma + epsilon) - mp.atan(gamma - epsilon)
    ) / mp.pi
    rows = []
    max_mean_error = max_abel_budget_ratio = max_root_error = mp.mpf(0)
    all_empty = 0

    for integer_length in (64, 256, 1024):
        length = mp.mpf(integer_length)
        threshold = mp.log(mp.log(length))
        sinc_primary = None
        for multiplier in (0, 1, 2):
            z = multiplier * threshold
            delta = z / length
            require(0 <= delta <= mp.mpf("0.5"), "uniform Abel budget needs delta<=1/2")
            kappa_loc, counts = primary_window_trace(length, z, gamma, epsilon, root_tol)
            max_root_error = max(max_root_error, counts["max_scaled_root_residual"])
            require(counts["max_scaled_root_residual"] <= tolerance, "root residual exceeded tolerance")
            all_empty += int(counts["negative_pieces"] == 0)
            if multiplier == 0:
                sinc_primary = kappa_loc
            sinc_upper = mp.exp(-z) * sinc_primary
            require(kappa_loc <= sinc_upper + tolerance, "positive Poisson drift increased negative primary trace")

            # Uniform analytic deficit estimate obtained by splitting at
            # Q=max(1,z(exp(z)+1)); no small-L asymptotic is assumed.
            cutoff = max(mp.mpf(1), z * (mp.exp(z) + 1))
            deficit_budget = (
                4 * mp.exp(-z) / (mp.pi * (1 + (gamma - epsilon) ** 2))
                * (mp.log(cutoff) + mp.mpf("1.5"))
            )
            require(sinc_upper - kappa_loc <= deficit_budget + tolerance, "harmonic-drift deficit budget failed")

            # This lag integral dominates the ENTIRE Cauchy L1 difference
            # between the Abel pair and the rectangular pair.  It is not
            # an oscillatory full-axis quadrature.
            abel_lag_l1 = 2 * mp.exp(-z) * prefix_quad(
                lambda v: mp.exp(delta * v) * (-mp.expm1(-mp.exp(-v))), length
            )
            abel_budget = 2 * mp.exp(-z) * (-mp.expm1(-(1 - delta) * length)) / (1 - delta)
            require(0 <= abel_lag_l1 <= abel_budget + tolerance, "whole-axis Abel L1 budget failed")
            require(abel_budget <= 4 * mp.exp(-z) + tolerance, "uniform Abel budget failed")
            max_abel_budget_ratio = max(max_abel_budget_ratio, abel_lag_l1 / abel_budget)

            mean_raw = 2 * prefix_quad(
                lambda u: mp.exp(-(1 + delta) * u - mp.exp(u - length)) * mp.cos(gamma * u),
                length,
            )
            mean_gamma = 2 * mp.re(abel_complex(-(1 + delta) + 1j * gamma, length))
            mean_error = abs(mean_raw - mean_gamma) / (1 + abs(mean_raw))
            require(mean_error <= tolerance, "Cauchy mean finite-gamma check failed")
            max_mean_error = max(max_mean_error, mean_error)
            mean_rect = 2 * rectangular_cos(1 + delta, length, gamma)
            prefix_mass = length if delta == 0 else -mp.expm1(-z) / delta
            mean_abel_budget = 2 * mp.exp(-length) * prefix_mass
            require(abs(mean_raw - mean_rect) <= mean_abel_budget + tolerance, "weighted Abel mean budget failed")

            # Safe analytic comparison to full rectangular/Abel kappa_-.
            # Near either resonance the other pole is bounded pointwise;
            # off both windows the Poisson background is nonnegative.
            separation = 2 * gamma - epsilon
            other_pole_bound = (
                delta / separation**2
                + mp.exp(-z) * (delta / separation**2 + 1 / separation)
            )
            other_window_budget = window_mass * other_pole_bound
            outside_window_budget = 2 * mp.exp(-z) * (delta / epsilon**2 + 1 / epsilon)
            full_abel_comparison_budget = other_window_budget + outside_window_budget + abel_budget
            benchmark = coefficient * mp.exp(-z) * mp.log(length)

            rows.append({
                "L": integer_length,
                "z_rule": ("0", "log(log L)", "2*log(log L)")[multiplier],
                "z": fmt(z),
                "delta": fmt(delta),
                "kappa_loc_primary_NOT_full_kappa": fmt(kappa_loc),
                "asymptotic_benchmark_NOT_asserted": fmt(benchmark),
                "local_to_benchmark_ratio_NOT_asserted": fmt(kappa_loc / benchmark),
                "scaled_sinc_primary_upper": fmt(sinc_upper),
                "harmonic_drift_deficit_budget": fmt(deficit_budget),
                "abel_lag_L1_majorant": fmt(abel_lag_l1),
                "abel_global_L1_budget": fmt(abel_budget),
                "full_Abel_vs_local_comparison_budget": fmt(full_abel_comparison_budget),
                "mean_R_Abel": fmt(mean_raw),
                "mean_limit": fmt(mean_limit),
                "mean_rect_vs_Abel_error": fmt(abs(mean_raw - mean_rect)),
                **{key: fmt(value) if isinstance(value, mp.mpf) else value for key, value in counts.items()},
            })

    require(len(rows) == 9, "preregistered nine-case grid changed")
    require(all_empty >= 2, "expected no-negative-root test cases were not exercised")
    print(json.dumps({
        "status": "PASS",
        "evidence": "[E] Synthetic gamma=2; not an actual zeta zero, source, or record.",
        "precision_dps": args.dps,
        "gamma": fmt(gamma),
        "epsilon": fmt(epsilon),
        "coefficient_4_over_pi2_1plusgamma2": fmt(coefficient),
        "quantity_warning": "kappa_loc_primary is the primary rectangular pole in two local windows; NOT full kappa. Positive trace is not computed by adding the mean to this local quantity.",
        "integration_warning": "Only finite root-split local oscillatory integrals and decaying lag integrals are evaluated; no full-axis oscillatory quadrature or numerical asymptotic assertion.",
        "independent_point_checks": len(point_specs),
        "max_rectangular_original_integral_scaled_error": fmt(max_rect_error),
        "max_Abel_gamma_original_integral_scaled_error": fmt(max_abel_error),
        "max_Abel_point_difference_to_budget_ratio": fmt(max_point_difference_ratio),
        "max_mean_gamma_original_integral_scaled_error": fmt(max_mean_error),
        "max_Abel_lag_integral_to_budget_ratio": fmt(max_abel_budget_ratio),
        "max_scaled_root_residual": fmt(max_root_error),
        "zero_negative_piece_cases": all_empty,
        "cases": rows,
        "elapsed_seconds": round(time.perf_counter() - started, 3),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

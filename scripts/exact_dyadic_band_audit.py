"""Numerical sanity checks for the exact dyadic band-discrepancy bridge.

The theorem itself is analytic.  This script checks the finite kernel indexing,
pre-alias envelope, dyadic variation, and shell-integral scales used in note
235.  It contains no prime asymptotic and no RH claim.
"""

from __future__ import annotations

import math

from power_high_bandpass_audit import finite_kernel, simpson_integral


def sampled_variation(limit: int, left: float, right: float) -> float:
    samples = 8_000
    previous = finite_kernel(limit, left)
    variation = abs(previous)
    for index in range(1, samples + 1):
        location = left + (right - left) * index / samples
        current = finite_kernel(limit, location)
        variation += abs(current - previous)
        previous = current
    variation += abs(previous)
    return variation


def audit_exact_shells(limit: int) -> None:
    length = math.log(limit)
    dimension = round(limit * length)
    lam = dimension / (limit * length)
    shell_ratios: list[float] = []
    variation_values: list[float] = []
    envelope_values: list[float] = []

    for radius in (2.0, 4.0, 8.0, 16.0, 32.0):
        integral = simpson_integral(
            lambda t: finite_kernel(limit, t),
            radius,
            2.0 * radius,
            20_000,
        )
        predicted_scale = 1.0 / radius
        shell_ratios.append(abs(integral) / predicted_scale)
        variation_values.append(sampled_variation(limit, radius, 2.0 * radius))

        for index in range(1, 2_001):
            location = radius + radius * index / 2_000
            envelope_values.append(location * abs(finite_kernel(limit, location)))

    central_radius = limit**0.25
    central_integral = simpson_integral(
        lambda t: finite_kernel(limit, t),
        0.0,
        central_radius,
        20_000,
    )
    central_scale = 1.0 / central_radius
    central_variation = sampled_variation(limit, 0.0, central_radius)

    print(
        f"X={limit:>5d}: max R|K_D|={max(envelope_values):.6f}, "
        f"max dyadic variation={max(variation_values):.6f}, "
        f"max shell integral/scale={max(shell_ratios):.6f}, "
        f"central integral/scale={abs(central_integral)/central_scale:.6f}, "
        f"central variation/log(2+M)="
        f"{central_variation/math.log(2.0+central_radius):.6f}"
    )

    assert max(envelope_values) < 1.0
    assert max(variation_values) < 20.0
    assert max(shell_ratios) < 2.0
    assert abs(central_integral) / central_scale < 2.0
    assert central_variation / math.log(2.0 + central_radius) < 10.0


def main() -> None:
    for limit in (400, 1_600, 6_400):
        audit_exact_shells(limit)
    print("exact dyadic finite-band audits passed")
    print("[scope] finite kernel sanity checks only; theorems 235-G/H are analytic")


if __name__ == "__main__":
    main()

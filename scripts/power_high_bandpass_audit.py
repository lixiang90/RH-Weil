"""Finite audit of the fixed-power alternating Gabor band-pass kernel.

The checks are deterministic and concern only the response geometry.  They do
not estimate the prime-weighted determinant measure and make no RH claim.
"""

from __future__ import annotations

import math


def finite_kernel(limit: int, t: float) -> float:
    """Exact normalized real Gabor response at t = X * Delta."""

    length = math.log(limit)
    dimension = round(limit * length)
    # Reduce the frequency increment modulo one before the geometric sum.
    # A small denominator alone does not make the full response equal to one.
    scale = limit * length
    half_angle = math.pi * (math.remainder(t, scale) / scale)

    def sinc0(value: float) -> float:
        return 1.0 if value == 0.0 else math.sin(value) / value

    amplitude = sinc0(dimension * half_angle) / sinc0(half_angle)
    phase = (
        2.0 * math.pi * math.remainder(t, 1.0)
        + (dimension - 1) * half_angle
    )
    return amplitude * math.cos(phase)


def limiting_kernel(t: float) -> float:
    """Integral from frequency 1 to 2 of cos(2*pi*frequency*t)."""

    if abs(t) < 1.0e-14:
        return 1.0
    return (
        math.sin(4.0 * math.pi * t) - math.sin(2.0 * math.pi * t)
    ) / (2.0 * math.pi * t)


def simpson_integral(function, left: float, right: float, panels: int) -> float:
    if panels % 2:
        raise ValueError("Simpson panel count must be even")
    step = (right - left) / panels
    total = function(left) + function(right)
    for index in range(1, panels):
        total += (4.0 if index % 2 else 2.0) * function(left + index * step)
    return total * step / 3.0


def audit_exact_kernel() -> None:
    radius = 16.0
    samples = 3_201
    for limit in (300, 1_200, 4_800):
        length = math.log(limit)
        dimension = round(limit * length)
        frequencies = [1.0, 1.0 + (dimension - 1) / (limit * length)]
        assert frequencies[0] == 1.0
        assert 1.99 < frequencies[1] < 2.01
        maximum_error = 0.0
        for index in range(samples):
            t = -radius + 2.0 * radius * index / (samples - 1)
            maximum_error = max(
                maximum_error, abs(finite_kernel(limit, t) - limiting_kernel(t))
            )
        print(
            f"X={limit:>5d}: d/(XL)={dimension/(limit*length):.10f}, "
            f"max_|t|<=16 kernel error={maximum_error:.6e}"
        )
        assert maximum_error < 0.08 / length
    print("exact finite response and local band-pass limit: PASS")


def audit_core_tail_cancellation() -> None:
    panels = 200_000
    core = simpson_integral(limiting_kernel, -1.0, 1.0, panels)
    # Positivity also has an analytic proof by pairing the positive and negative
    # sine lobes on [2*pi,4*pi].
    assert core > 0.0
    print(f"coherent-core mass c0={core:.12f}")
    for radius in (4.0, 8.0, 16.0, 32.0):
        whole = simpson_integral(
            limiting_kernel, -radius, radius, panels
        )
        tail = whole - core
        print(
            f"radius={radius:>4.0f}: whole={whole:+.9e}, "
            f"tail={tail:+.9e}, core+tail={whole:+.9e}"
        )
    whole_32 = simpson_integral(limiting_kernel, -32.0, 32.0, panels)
    assert abs(whole_32) < 1.0e-3
    assert abs((whole_32 - core) + core) < 1.0e-3
    print("positive core and compensating oscillatory tail: PASS")


def audit_balanced_mesh() -> None:
    for limit in (400, 1_600, 6_400):
        scale = limit**1.5
        resolution = scale / limit
        denominator_product = round(scale)
        maximum_error = 0.0
        for determinant in range(-round(resolution), round(resolution) + 1):
            exact = limit * math.log(
                (denominator_product + determinant) / denominator_product
            )
            linear = determinant / resolution
            maximum_error = max(maximum_error, abs(exact - linear))

        mesh = 1.0 / resolution
        core_index = math.floor(1.0 / mesh)
        full_index = math.floor(32.0 / mesh)
        core_sum = mesh * sum(
            limiting_kernel(index * mesh)
            for index in range(-core_index, core_index + 1)
        )
        full_sum = mesh * sum(
            limiting_kernel(index * mesh)
            for index in range(-full_index, full_index + 1)
        )
        print(
            f"X={limit:>5d}: mesh={mesh:.6e}, "
            f"max core linearization error={maximum_error:.6e}, "
            f"mesh-core={core_sum:.9f}, mesh-full32={full_sum:+.9e}"
        )
        assert maximum_error < 1.1 / limit
        assert core_sum > 0.0
        assert abs(full_sum) < 1.0e-3
    print("theta=3/4 determinant mesh and core-tail model: PASS")


def main() -> None:
    audit_exact_kernel()
    audit_core_tail_cancellation()
    audit_balanced_mesh()
    print("power-high band-pass audits passed")
    print("[scope] response geometry/model discrepancy only; no prime asymptotic")


if __name__ == "__main__":
    main()

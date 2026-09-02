"""Exact-grid audit of band-energy overstrength.

For the positive density 1+epsilon*cos(3*pi*t) on [-M,M], the centered
Fourier mass is concentrated around the interior band frequency 3/2.
Its exact discrete [1,2] energy grows like sqrt(M), while the all-ones
physical response stays bounded.  This is a response-geometry no-go, not
an arithmetic model and not an RH claim.
"""

from __future__ import annotations

import math


def interval_transform(radius: int, frequency: float) -> float:
    """Integral of exp(2*pi*i*frequency*t) over [-radius,radius]."""

    if abs(frequency) < 1.0e-14:
        return 2.0 * radius
    return math.sin(2.0 * math.pi * frequency * radius) / (
        math.pi * frequency
    )


def audit_in_band_modulation(root: int, epsilon: float) -> None:
    if root % 2:
        raise ValueError("root must be even")
    radius = root * root
    limit = root**4
    length = math.log(limit)
    grid_scale = limit * length
    dimension = round(grid_scale)
    carrier = 1.5

    response_sum = 0.0
    energy_square_sum = 0.0
    for index in range(dimension):
        frequency = 1.0 + index / grid_scale
        centered_transform = 0.5 * epsilon * (
            interval_transform(radius, frequency - carrier)
            + interval_transform(radius, frequency + carrier)
        )
        full_transform = (
            interval_transform(radius, frequency) + centered_transform
        )
        response_sum += full_transform
        energy_square_sum += centered_transform * centered_transform

    response = response_sum / dimension
    band_energy = math.sqrt(energy_square_sum / dimension)
    error_scale = 1.0 / radius + radius * radius / grid_scale

    print(
        f"n={root:>2d}, X={limit:>5d}, M={radius:>3d}, D={dimension:>6d}: "
        f"response={response:+.9f}, response-eps/2={response-epsilon/2:+.3e}, "
        f"error-scale={error_scale:.3e}, "
        f"Bband/sqrt(M)={band_energy/math.sqrt(radius):.9f}, "
        f"Bband/|response|={band_energy/abs(response):.6f}"
    )

    assert abs(response - epsilon / 2.0) < 2.5 * error_scale
    assert band_energy / math.sqrt(radius) > 0.25
    assert band_energy > abs(response)


def main() -> None:
    epsilon = 0.5
    for root in (4, 6, 8, 10):
        audit_in_band_modulation(root, epsilon)
    print("band-energy / physical-direction separation audits passed")
    print("[scope] positive continuous response model only; no prime asymptotic")


if __name__ == "__main__":
    main()

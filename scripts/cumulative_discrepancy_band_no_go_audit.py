"""Finite audit of the cumulative-discrepancy / band-response separation.

The positive density 1+epsilon*cos(2*pi*t/sqrt(M)) has cumulative discrepancy
of order sqrt(M), while its modulation lies below the Gabor band [1,2].  The
exact finite band response therefore decays.  This is a geometry no-go, not an
arithmetic model and not an RH claim.
"""

from __future__ import annotations

import math

from power_high_bandpass_audit import finite_kernel, simpson_integral


def audit_slow_modulation(radius: int, limit: int, epsilon: float) -> None:
    root = round(math.sqrt(radius))
    if root * root != radius:
        raise ValueError("radius must be a perfect square")
    frequency = 1.0 / root
    # frequency * radius = root is integral, so the cosine has zero total mass
    # on the symmetric interval and the constant comparison density is exactly 1.
    total_mass = 2.0 * radius
    discrepancy = epsilon / (2.0 * math.pi * frequency)

    panels = max(20_000, 200 * radius)
    if panels % 2:
        panels += 1
    response = simpson_integral(
        lambda t: finite_kernel(limit, t)
        * (1.0 + epsilon * math.cos(2.0 * math.pi * frequency * t)),
        -float(radius),
        float(radius),
        panels,
    )

    print(
        f"M={radius:>4d}: omega={frequency:.6f}, B={total_mass:.1f}, "
        f"E={discrepancy:.6f}, E/sqrt(M)={discrepancy/math.sqrt(radius):.6f}, "
        f"response={response:+.6e}, M*|response|={radius*abs(response):.6e}"
    )
    assert abs(total_mass - 2.0 * radius) < 1.0e-12
    assert abs(discrepancy / math.sqrt(radius) - epsilon / (2.0 * math.pi)) < 1e-12
    assert radius * abs(response) < 0.2


def main() -> None:
    limit = 200_000
    epsilon = 0.5
    for radius in (16, 64, 256, 1_024):
        audit_slow_modulation(radius, limit, epsilon)
    print("cumulative-discrepancy / exact-band separation audits passed")
    print("[scope] positive continuous response model only; no prime asymptotic")


if __name__ == "__main__":
    main()

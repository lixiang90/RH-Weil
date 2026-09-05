#!/usr/bin/env python3
"""Exact finite audit of the signed two-channel truncation bridge.

Run: python -B scripts/signed_truncation_bridge_audit.py

Positive source measures have rational weights and nonnegative physical lags.
Window restriction is closed and is performed before even centering. No
carrier-separation assumption is made. Fraction arithmetic checks measures,
primitive and distance energies, and square-root bounds without floating
point. These finite cases certify no arithmetic/PNT or asymptotic input.
"""

import sys

sys.dont_write_bytecode = True

from fractions import Fraction as F
from random import Random

from carrier_sector_coercivity_audit import (
    add,
    centered,
    convolve,
    distance,
    mass,
    measure,
    primitive_energy,
    scale,
)


def keep_window(mu, L, H):
    assert H >= 0
    return {x: a for x, a in mu.items() if L-H <= x <= L+H}


def energy(mu):
    assert mass(mu) == 0
    value = primitive_energy(mu)
    assert value == distance(mu)
    assert value >= 0
    return value


def sqrt_sum_upper(squared_left, squared_first, squared_second):
    """Exact check sqrt(left)<=sqrt(first)+sqrt(second)."""
    assert min(squared_left, squared_first, squared_second) >= 0
    excess = squared_left - squared_first - squared_second
    return excess <= 0 or excess**2 <= 4*squared_first*squared_second


def audit(alpha, beta, L, H):
    assert all(x >= 0 and a > 0 for mu in (alpha, beta)
               for x, a in mu.items())
    alphaH, betaH = keep_window(alpha, L, H), keep_window(beta, L, H)
    alpha_out = add(alpha, scale(alphaH, -1))
    beta_out = add(beta, scale(betaH, -1))
    A, B = mass(alpha), mass(beta)
    Aout, Bout = mass(alpha_out), mass(beta_out)
    assert min(Aout, Bout) >= 0
    S, K, Kout = A+B, A*A+B*B, Aout*Aout+Bout*Bout
    # The helper's L=0 interprets the input locations as physical lags.
    p, c = centered(alpha, F(0)), scale(centered(beta, F(0)), -1)
    pH, cH = centered(alphaH, F(0)), scale(centered(betaH, F(0)), -1)
    r, rH = add(p, c), add(pH, cH)
    e = add(r, scale(rH, -1))
    blue = convolve(e, add(r, rH))
    local_square = convolve(rH, rH)
    full_square = convolve(r, r)
    assert add(full_square, scale(local_square, -1)) == blue
    A4sq, B4sq = energy(blue), energy(local_square)
    response_squared = difference_squared = F(0)
    first_squared = second_squared = F(0)
    for channel, local_channel in ((p, pH), (c, cH)):
        full_response = convolve(full_square, channel)
        local_response = convolve(local_square, local_channel)
        difference = add(full_response, scale(local_response, -1))
        first = convolve(blue, channel)
        second = convolve(local_square, add(channel, scale(local_channel, -1)))
        assert difference == add(first, second)
        response_squared += energy(full_response)
        difference_squared += energy(difference)
        first_squared += energy(first)
        second_squared += energy(second)
        energy(local_response)
    assert first_squared <= 4*K*A4sq
    assert second_squared <= 4*Kout*B4sq
    assert sqrt_sum_upper(difference_squared, first_squared, second_squared)
    assert sqrt_sum_upper(difference_squared, 4*K*A4sq, 4*Kout*B4sq)
    assert response_squared <= 16*S*S*K*energy(r)
    return {
        "zero_width": H == 0,
        "all_kept": not alpha_out and not beta_out,
        "all_deleted": not alphaH and not betaH,
        "balanced": A == B,
        "boundary_atom": any(x in (L-H, L+H) for mu in (alpha, beta) for x in mu),
        "positive_difference": difference_squared > 0,
    }


def main():
    rng = Random(265)
    identical = measure([(0, F(1, 2)), (1, F(1, 2))])
    pairs = [
        (measure([(F(1, 2), 1), (F(3, 2), 2)]),
         measure([(F(1, 2), 2), (1, 1), (F(3, 2), 1)])),
        (measure([(0, F(1, 2)), (1, F(1, 2))]),
         measure([(F(1, 3), F(1, 3)), (F(8, 3), F(2, 3))])),
        (identical, identical),
    ]
    grid = [F(i, 3) for i in range(10)]
    for _ in range(2):
        alpha_sites, beta_sites = rng.sample(grid, 5), rng.sample(grid, 4)
        alpha = measure((x, F(rng.randint(1, 9), rng.randint(1, 7)))
                        for x in alpha_sites)
        beta = measure((x, F(rng.randint(1, 9), rng.randint(1, 7)))
                       for x in beta_sites)
        pairs.append((alpha, beta))
    windows = ((F(0), F(0)), (F(1), F(0)),
               (F(1), F(1, 2)), (F(3, 2), F(3, 2)),
               (F(5), F(0)), (F(1, 2), F(1, 2)))
    totals = {}
    cases = 0
    for alpha, beta in pairs:
        for L, H in windows:
            result = audit(alpha, beta, L, H)
            cases += 1
            for key, value in result.items():
                totals[key] = totals.get(key, 0) + value
    assert cases == 30
    assert all(totals[key] > 0 for key in totals)
    print("PASS exact signed-truncation bridge audit (stdlib Fraction)")
    print(f"Cases: {cases}; source pairs: {len(pairs)}; closed windows: {len(windows)}")
    print("Checked both channel measure identities before taking energies.")
    print("Checked every used energy by primitive and distance calculations.")
    print("Checked Z <= 2 sqrt(K) A4 + 2 sqrt(Kout) B4 by exact rational squaring.")
    print("Checked full response P^2 <= 16 S^2 K E(r).")
    for key, value in totals.items():
        print(f"{key}: {value}")
    print("No carrier separation was imposed; no PNT or asymptotic assertion is tested.")


if __name__ == "__main__":
    main()

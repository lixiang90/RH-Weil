#!/usr/bin/env python3
"""Exact bounded audits of sharp Brownian energy-square inequalities.

Run: python -B scripts/brownian_energy_square_audit.py

All coordinates, weights, integrals, and comparisons use Fraction. Independent
step-primitive, distance-kernel, and overlap-autocorrelation calculations
check finite real zero-mass atomic measures on [-H,H]. Finite checks do not
replace the accompanying proof for arbitrary finite measures.
"""

from fractions import Fraction as F
from random import Random


def measure(items):
    result = {}
    for x, coefficient in items:
        x, coefficient = F(x), F(coefficient)
        result[x] = result.get(x, F(0)) + coefficient
    return {x: a for x, a in result.items() if a}


def mass(mu):
    return sum(mu.values(), F(0))


def convolve(mu, nu):
    return measure((x + y, a * b) for x, a in mu.items()
                   for y, b in nu.items())


def reflect(mu):
    return measure((-x, a) for x, a in mu.items())


def primitive_intervals(mu):
    assert mass(mu) == 0
    locations = sorted(mu)
    height, intervals = F(0), []
    for i in range(len(locations) - 1):
        height += mu[locations[i]]
        if height:
            intervals.append((locations[i], locations[i + 1], height))
    return intervals


def primitive_energy(mu):
    return sum(((right - left) * height * height
                for left, right, height in primitive_intervals(mu)), F(0))


def distance_energy(mu):
    assert mass(mu) == 0
    return -sum((a * b * abs(x - y) for x, a in mu.items()
                 for y, b in mu.items()), F(0)) / 2


def overlap_autocorrelation(intervals, t):
    """Integrate f(x)f(x+t) directly from overlaps of constant intervals."""
    return sum((a * b * max(F(0), min(right, other_right - t)
                          - max(left, other_left - t))
                for left, right, a in intervals
                for other_left, other_right, b in intervals), F(0))


def autocorrelation_derivative_energy(mu, H):
    """Compute the exact piecewise-linear profile and integrate its slope."""
    intervals = primitive_intervals(mu)
    endpoints = {x for left, right, _ in intervals for x in (left, right)}
    breaks = sorted({F(0), -2 * H, 2 * H}
                    | {x - y for x in endpoints for y in endpoints})
    profile = {t: overlap_autocorrelation(intervals, t) for t in breaks}
    assert profile[F(0)] == primitive_energy(mu)
    assert profile[-2 * H] == profile[2 * H] == 0
    assert all(profile[t] == profile[-t] for t in breaks)
    correlation_measure = convolve(mu, reflect(mu))
    energy = F(0)
    for left, right in zip(breaks, breaks[1:]):
        midpoint = (left + right) / 2
        slope = (profile[right] - profile[left]) / (right - left)
        # A''=-mu*check(mu), hence A'=-F_(mu*check(mu)).
        primitive_at_midpoint = sum(
            (a for x, a in correlation_measure.items() if x <= midpoint), F(0))
        assert slope == -primitive_at_midpoint
        energy += slope * slope * (right - left)
    return energy, len(breaks) - 1


def audit(mu, H):
    assert H > 0 and mass(mu) == 0
    assert all(-H <= x <= H for x in mu)
    E1 = primitive_energy(mu)
    assert E1 == distance_energy(mu)
    square = convolve(mu, mu)
    correlation = convolve(mu, reflect(mu))
    E2 = primitive_energy(square)
    assert E2 == distance_energy(square)
    assert E2 == primitive_energy(correlation) == distance_energy(correlation)
    autocorrelation_energy, intervals = autocorrelation_derivative_energy(mu, H)
    assert E2 == autocorrelation_energy
    assert E2 >= E1 * E1 / H
    first = sum((x * a for x, a in mu.items()), F(0))
    assert E1 >= first * first / (2 * H)
    assert E2 >= F(3, 16) * first**4 / H**3
    # Combining the two sharp energy inequalities gives the stronger constant.
    assert E2 >= first**4 / (4 * H**3)
    return E1, E2, first, intervals


def main():
    rng = Random(262)
    H_values = (F(1, 3), F(1), F(5, 2), F(7))
    total = nonzero = endpoint_cases = zero_first_nonzero = intervals = 0
    square_ratios = []
    for H in H_values:
        cases = []
        for c in (F(0), F(1, 7), F(-3, 2), F(2)):
            cases.append((measure([(-H, c), (H, -c)]), c))
        patterns = (
            [(-1, 1), (0, -2), (1, 1)],
            [(F(-1, 2), F(3, 4)), (F(1, 2), F(-3, 4))],
            [(-1, F(1, 3)), (F(-1, 3), F(-5, 7)),
             (F(1, 2), F(2, 5)), (1, F(-2, 105))],
            [(-1, 1), (F(-1, 2), -3), (0, 3), (F(1, 2), -1)],
        )
        for pattern in patterns:
            mu = measure((H * x, a) for x, a in pattern)
            assert mass(mu) == 0
            cases.append((mu, None))
        grid = [F(i, 7) for i in range(-7, 8)]
        for _ in range(18):
            sites = rng.sample(grid, rng.randint(2, 7))
            coefficients = [F(rng.randint(-9, 9), rng.randint(1, 7))
                            for _ in sites[:-1]]
            coefficients.append(-sum(coefficients, F(0)))
            cases.append((measure((H * x, a)
                                  for x, a in zip(sites, coefficients)), None))
        for mu, endpoint_c in cases:
            E1, E2, first, count = audit(mu, H)
            total += 1
            intervals += count
            if E1:
                nonzero += 1
                square_ratios.append(H * E2 / (E1 * E1))
                zero_first_nonzero += first == 0
            if endpoint_c is not None:
                endpoint_cases += 1
                assert E1 == 2 * H * endpoint_c**2
                assert E2 == 4 * H * endpoint_c**4
                assert E2 == E1**2 / H == first**4 / (4 * H**3)
    print("PASS exact Brownian energy-square audit (stdlib Fraction)")
    print(f"Cases: {total}; nonzero measures: {nonzero}; H values: {len(H_values)}")
    print(f"Autocorrelation slope intervals checked independently: {intervals}")
    print("Checked: primitive = distance energy for mu, mu*mu, mu*check(mu)")
    print("Checked: E(mu*mu) = integral |A'|^2, with A from interval overlaps")
    print("Checked sharp bound: E2 >= E1^2/H")
    print("Checked moment bounds: E2 >= 3*m1^4/(16*H^3) and >= m1^4/(4*H^3)")
    print(f"Endpoint equality cases: {endpoint_cases}; minimum H*E2/E1^2: {min(square_ratios)}")
    print(f"Nonzero-energy cases with zero first moment: {zero_first_nonzero}")
    print("Finite exact checks only; arbitrary-measure conclusions require proof.")


if __name__ == "__main__":
    main()

"""Exact tests for Brownian interval-denominator helpers."""

from __future__ import annotations

from fractions import Fraction

from brownian_interval_certificate import (
    brownian_cluster_energy_upper_bound,
    brownian_tv_perturbation_upper_bound,
    canonical_position_interval,
    canonical_rational_grid_key,
    centered_component_tv_error_upper_bound,
    polynomial_convolution_tv_error_upper_bound,
    rational_decimal_lower,
    rational_decimal_upper,
    rational_log_interval,
    smooth_rational_log_interval,
)
from formal_lag_response import FormalLag


def main() -> None:
    assert rational_decimal_lower(Fraction(1, 3), 3) == "0.333"
    assert rational_decimal_upper(Fraction(1, 3), 3) == "0.334"
    assert rational_decimal_lower(Fraction(-1, 3), 3) == "-0.334"
    assert rational_decimal_upper(Fraction(-1, 3), 3) == "-0.333"
    for value in (
        Fraction(1, 17),
        Fraction(2),
        Fraction(3),
        Fraction(81, 40),
        Fraction(729),
    ):
        interval = rational_log_interval(value)
        inverse = rational_log_interval(1 / value)
        assert interval.lower + inverse.lower <= 0
        assert interval.upper + inverse.upper >= 0
        coarse = rational_log_interval(value, terms=48)
        assert coarse.lower <= interval.lower <= interval.upper <= coarse.upper
    smooth = smooth_rational_log_interval(
        Fraction(3**4 * 5, 2**3 * 7), (2, 3, 5, 7)
    )
    generic = rational_log_interval(Fraction(3**4 * 5, 2**3 * 7))
    assert max(smooth.lower, generic.lower) <= min(
        smooth.upper, generic.upper
    )

    nodes = (Fraction(1, 4), Fraction(3, 4))
    left = FormalLag(Fraction(3, 2), (1, 1))
    right = FormalLag(Fraction(3, 2), (4, 0))
    assert canonical_rational_grid_key(left, nodes) == (
        Fraction(3, 2),
        Fraction(1),
    )
    assert canonical_rational_grid_key(left, nodes) == (
        canonical_rational_grid_key(right, nodes)
    )
    position = canonical_position_interval(
        canonical_rational_grid_key(left, nodes)
    )
    direct = rational_log_interval(Fraction(3, 2))
    assert position == type(position)(direct.lower + 1, direct.upper + 1)

    exact = brownian_cluster_energy_upper_bound(
        (
            (Fraction(0), Fraction(0), Fraction(1)),
            (Fraction(1), Fraction(1), Fraction(-1)),
        )
    )
    assert exact["energy_upper"] == 1
    assert exact["cluster_count"] == 2
    assert exact["maximum_cluster_size"] == 1

    overlapping = brownian_cluster_energy_upper_bound(
        (
            (Fraction(0), Fraction(1, 5), Fraction(1)),
            (Fraction(1, 10), Fraction(1), Fraction(-1)),
        )
    )
    assert overlapping["energy_upper"] == 4
    assert overlapping["cluster_count"] == 1
    assert overlapping["maximum_cluster_size"] == 2

    perturbed = brownian_tv_perturbation_upper_bound(
        Fraction(1), Fraction(2), Fraction(1, 100), Fraction(1, 10)
    )
    assert perturbed == Fraction(5511, 5000)

    polynomial_error = polynomial_convolution_tv_error_upper_bound(
        Fraction(2),
        Fraction(1, 100),
        (Fraction(3), Fraction(5), Fraction(7)),
        (Fraction(1, 1000), Fraction(2, 1000), Fraction(3, 1000)),
    )
    assert polynomial_error == Fraction(347, 1000)
    assert centered_component_tv_error_upper_bound(Fraction(1, 100)) == (
        Fraction(1, 50)
    )
    print("Brownian interval-certificate exact tests passed")
    print("[scope] rational finite inequalities; no zeta enclosure or RH claim")


if __name__ == "__main__":
    main()

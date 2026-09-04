"""Small independent checks for the B1h second-scale interval machinery."""

from __future__ import annotations

from fractions import Fraction

from b1f_base_coefficient_interval_audit import prime_weight_interval as b1f_weight
from b1h_second_scale_interval_audit import (
    PRIME_POWERS,
    build_interval_data,
    prime_weight_interval,
    rational_surrogate_energy_upper,
)
from brownian_interval_certificate import rational_log_interval
from formal_lag_response import FormalLag


def main() -> None:
    data = build_interval_data()
    assert len(data["prime_weights"]) == len(PRIME_POWERS) == 9
    assert len(data["continuum_masses"]) == 5
    for interval in data["prime_weights"] + data["continuum_masses"]:
        assert 0 < interval.lower <= interval.upper

    # The larger Abel scale weakens exp(-n/Y), hence every common prime atom
    # has strictly larger weight than in B1f.
    for integer, prime in PRIME_POWERS[:7]:
        old = b1f_weight(integer, prime)
        new = prime_weight_interval(integer, prime)
        assert old.upper < new.lower

    # A two-atom centered measure -delta_0+delta_log(2) has Brownian energy
    # exactly log(2). The generic surrogate routine must enclose it.
    zero = FormalLag.zero(1)
    lag = FormalLag.prime(2, 1)
    energy, clusters, maximum_cluster = rational_surrogate_energy_upper(
        {zero: -1.0 + 0.0j, lag: 1.0 + 0.0j},
        (Fraction(0),),
    )
    log_two = rational_log_interval(Fraction(2))
    assert energy >= log_two.upper
    assert clusters == 2
    assert maximum_cluster == 1

    print("B1h second-scale interval helper tests passed")


if __name__ == "__main__":
    main()

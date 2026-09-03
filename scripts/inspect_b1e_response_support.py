"""Inspect the numerical support geometry of the frozen B1e response."""

from __future__ import annotations

from fractions import Fraction

from audit_soft_zeta_orbit import soft_zeta_orbit_audit
from brownian_interval_certificate import (
    brownian_cluster_energy_upper_bound,
    canonical_position_interval,
    canonical_rational_grid_key,
    rational_decimal_lower,
    rational_decimal_upper,
)
from formal_lag_response import degree_two_centered_response_channel_maps


def main() -> None:
    audit = soft_zeta_orbit_audit(
        scale=8.0, integer_cutoff=10, lag_cells=4, degree=2
    )
    spectral = audit["vaughan_brownian_audit"]["spectral_overlap_data"]
    factorization = degree_two_centered_response_channel_maps(
        {
            "prime": spectral["prime_component"],
            "continuum": spectral["continuum_component"],
        },
        audit["spectral_bound"],
        audit["rho"],
    )
    nodes = spectral["continuum_nodes"]
    lag_start = Fraction(3, 100)
    lag_end = Fraction(2)
    lag_width = (lag_end - lag_start) / 4
    rational_nodes = tuple(
        lag_start + (Fraction(index) + Fraction(1, 2)) * lag_width
        for index in range(4)
    )
    if len(nodes) != len(rational_nodes):
        raise AssertionError("unexpected continuum-node count")
    for label, component in factorization["response_components"].items():
        grouped: dict[tuple[Fraction, Fraction], Fraction] = {}
        for lag, coefficient in component.items():
            if coefficient.imag != 0.0:
                raise AssertionError("expected a real symmetric response")
            key = canonical_rational_grid_key(lag, rational_nodes)
            exact_float = Fraction.from_float(float(coefficient.real))
            grouped[key] = grouped.get(key, Fraction(0)) + exact_float
        total = sum(grouped.values(), Fraction(0))
        zero = (Fraction(1), Fraction(0))
        grouped[zero] = grouped.get(zero, Fraction(0)) - total

        atoms = sorted(
            (
                (
                    canonical_position_interval(
                        key, terms=96, smooth_primes=(2, 3, 5, 7)
                    ),
                    coefficient,
                    key,
                )
                for key, coefficient in grouped.items()
                if coefficient
            ),
            key=lambda atom: atom[0].lower,
        )
        certified_gaps = [
            atoms[index + 1][0].lower - atoms[index][0].upper
            for index in range(len(atoms) - 1)
        ]
        minimum_gap = min(certified_gaps)
        if minimum_gap <= 0:
            raise AssertionError("position intervals do not certify atom order")
        certificate = brownian_cluster_energy_upper_bound(
            (
                interval.lower,
                interval.upper,
                coefficient,
            )
            for interval, coefficient, _ in atoms
        )
        print(
            f"{label}: formal={len(component)}, canonical={len(grouped)}, "
            f"atoms={len(atoms)}, certified_min_gap_lower="
            f"{rational_decimal_lower(minimum_gap, 20)}, "
            f"rational_energy_upper="
            f"{rational_decimal_upper(certificate['energy_upper'], 20)}, "
            f"clusters={certificate['cluster_count']}, "
            f"max_cluster={certificate['maximum_cluster_size']}"
        )


if __name__ == "__main__":
    main()

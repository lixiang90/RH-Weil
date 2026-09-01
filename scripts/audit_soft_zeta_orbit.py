"""Frozen finite audit of the canonical soft zeta orbit direction.

This is a diagnostic of a small Abel prime--continuum quadrature.  It is not
an interval certificate, a cofinal estimate, or evidence for RH.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np

from formal_lag_response import (
    cauchy_gaussian_mixture_band_ledger,
    cauchy_signed_layer_cake_ledger,
    chebyshev_formal_orbit_coefficients,
    degree_two_gaussian_response_upper_bound,
    degree_two_parity_exact_ledger,
    degree_two_response_frequency_map,
    formal_arbitrary_direction_audit,
    formal_cauchy_response_ledger,
    gaussian_heat_shell_ledger,
    gaussian_signed_layer_cake_ledger,
    stationary_response_from_frequency_map,
    two_sided_prime_continuum_symbol,
)
from qw_matrix import zeta_abel_shared_lag_loewner_quadrature
from soft_negative_moment import chebyshev_soft_series


def soft_zeta_orbit_audit(
    *,
    scale: float,
    integer_cutoff: int,
    lag_cells: int,
    degree: int,
    horizontal_offset: float = 0.1,
    lag_start: float = 0.03,
    lag_end: float = 2.0,
    near_cutoff: float = 0.5,
) -> dict[str, object]:
    data = zeta_abel_shared_lag_loewner_quadrature(
        horizontal_offset=mp.mpf(horizontal_offset),
        scale=mp.mpf(scale),
        integer_cutoff=integer_cutoff,
        lag_start=mp.mpf(lag_start),
        lag_end=mp.mpf(lag_end),
        lag_cells=lag_cells,
        geometric_mesh=False,
        compute_loewner_relaxation=False,
    )
    prime_atoms = []
    for node, coefficient in zip(
        data["prime_atom_lag_nodes"], data["prime_atom_coefficients"]
    ):
        integer = int(mp.nint(mp.exp(node)))
        if abs(node - mp.log(integer)) > mp.mpf("1e-30"):
            raise ArithmeticError("prime atom did not retain an exact integer lag")
        prime_atoms.append((integer, complex(coefficient)))
    continuum_atoms = [
        (float(node), complex(coefficient))
        for node, coefficient in zip(
            data["continuum_background_lag_nodes"],
            data["continuum_background_coefficients"],
        )
    ]
    formal = two_sided_prime_continuum_symbol(
        prime_atoms, continuum_atoms
    )
    symbol = formal["combined_map"]
    spectral_bound = sum(abs(coefficient) for coefficient in symbol.values())
    rho = spectral_bound / 3.0
    series = chebyshev_soft_series(spectral_bound, rho, degree=degree)
    effect = chebyshev_formal_orbit_coefficients(
        symbol, spectral_bound, series
    )
    ledger = formal_cauchy_response_ledger(
        {
            "prime": formal["prime_map"],
            "continuum": formal["continuum_map"],
        },
        effect,
        formal["continuum_nodes"],
        near_cutoff=near_cutoff,
    )
    direction = formal_arbitrary_direction_audit(
        symbol, effect, formal["continuum_nodes"]
    )
    parity = (
        degree_two_parity_exact_ledger(symbol, spectral_bound, rho)
        if degree == 2
        else None
    )
    response_map = (
        degree_two_response_frequency_map(symbol, spectral_bound, rho)
        if degree == 2
        else None
    )
    gaussian_mixture = (
        cauchy_gaussian_mixture_band_ledger(
            response_map,
            formal["continuum_nodes"],
            (0.0, 0.01, 0.04, 0.16, 0.64, 2.56, math.inf),
        )
        if response_map is not None
        else None
    )
    gaussian_scale_audit = []
    if response_map is not None:
        for gaussian_scale in (0.16, 0.64, 2.56, 10.24):
            actual_response = stationary_response_from_frequency_map(
                response_map,
                formal["continuum_nodes"],
                lambda value, scale=gaussian_scale: math.exp(
                    -(value**2) / (4.0 * scale)
                ),
            )
            upper = degree_two_gaussian_response_upper_bound(
                symbol,
                formal["continuum_nodes"],
                spectral_bound,
                rho,
                gaussian_scale,
            )
            gaussian_scale_audit.append(
                {
                    "scale": gaussian_scale,
                    "actual_response": actual_response,
                    "upper_bound": upper["response_upper_bound"],
                    "upper_to_actual_ratio": (
                        upper["response_upper_bound"] / abs(actual_response)
                        if abs(actual_response) > 0.0
                        else math.inf
                    ),
                    "total_mass": upper["total_mass"],
                    "primitive_l1": upper["primitive_l1"],
                }
            )
    heat_shell_audit = (
        gaussian_heat_shell_ledger(
            response_map, formal["continuum_nodes"], 0.01
        )
        if response_map is not None
        else None
    )
    signed_profile_audit = (
        [
            gaussian_signed_layer_cake_ledger(
                response_map, formal["continuum_nodes"], gaussian_scale
            )
            for gaussian_scale in (0.01, 0.16, 2.56)
        ]
        if response_map is not None
        else []
    )
    cauchy_profile_audit = (
        cauchy_signed_layer_cake_ledger(
            response_map, formal["continuum_nodes"]
        )
        if response_map is not None
        else None
    )
    prime_continuum_mass = sum(
        complex(coefficient)
        for coefficient in data["prime_continuum_discrepancy_coefficients"]
    )
    separated_mass = sum(
        complex(coefficient) for coefficient in data["prime_atom_coefficients"]
    ) + sum(
        complex(coefficient)
        for coefficient in data["continuum_background_coefficients"]
    )
    return {
        "quadrature": data,
        "formal_symbol": formal,
        "spectral_bound": spectral_bound,
        "rho": rho,
        "degree": degree,
        "series_coefficients": series,
        "effect_support_size": len(effect),
        "response_ledger": ledger,
        "direction_audit": direction,
        "parity_exact_ledger": parity,
        "degree_two_response_map": response_map,
        "gaussian_mixture_ledger": gaussian_mixture,
        "gaussian_scale_audit": gaussian_scale_audit,
        "heat_shell_audit": heat_shell_audit,
        "signed_profile_audit": signed_profile_audit,
        "cauchy_profile_audit": cauchy_profile_audit,
        "provenance_mass_residual": separated_mass - prime_continuum_mass,
    }


def frozen_soft_zeta_audit() -> dict[str, object]:
    return soft_zeta_orbit_audit(
        scale=8.0,
        integer_cutoff=10,
        lag_cells=2,
        degree=2,
    )


def main() -> None:
    audit = frozen_soft_zeta_audit()
    ledger = audit["response_ledger"]
    direction = audit["direction_audit"]
    signed_total = sum(ledger["signed"].values())
    component_total = sum(
        sum(component.values())
        for component in ledger["by_component"].values()
    )
    assert abs(audit["provenance_mass_residual"]) <= 1.0e-12
    assert abs(signed_total - component_total) <= 1.0e-10
    assert abs(signed_total.real - ledger["total_response"]) <= 1.0e-10
    assert abs(
        ledger["total_response"]
        - direction["canonical_negative_response"]
    ) <= 1.0e-10
    assert ledger["imaginary_residual"] <= 1.0e-10
    assert ledger["counts"]["exact"] > 0
    assert direction["canonical_negative_depth"] <= (
        direction["arbitrary_negative_depth"] + 1.0e-9
    )
    assert 0.0 <= direction["canonical_to_arbitrary_depth_ratio"] <= 1.0 + 1.0e-8
    assert audit["parity_exact_ledger"] is not None
    assert audit["gaussian_mixture_ledger"] is not None
    assert abs(
        audit["gaussian_mixture_ledger"]["total_response"]
        - ledger["total_response"]
    ) <= 2.0e-10
    assert all(
        abs(item["actual_response"]) <= item["upper_bound"] + 1.0e-10
        for item in audit["gaussian_scale_audit"]
    )
    assert audit["heat_shell_audit"] is not None
    assert abs(
        audit["heat_shell_audit"]["total_response"]
        - stationary_response_from_frequency_map(
            audit["degree_two_response_map"],
            audit["formal_symbol"]["continuum_nodes"],
            lambda value: math.exp(-(value**2) / 0.04),
        )
    ) <= 1.0e-10
    assert all(
        item["profile_capacity"] <= item["coefficient_variation"] + 1.0e-10
        for item in audit["signed_profile_audit"]
    )
    assert audit["cauchy_profile_audit"] is not None
    assert abs(
        audit["cauchy_profile_audit"]["total_response"]
        - ledger["total_response"]
    ) <= 1.0e-10
    assert ledger["signed"]["exact"].real <= (
        audit["parity_exact_ledger"]["exact_response_upper_bound"] + 1.0e-10
    )
    assert ledger["signed"]["exact"].real <= (
        audit["parity_exact_ledger"]["exact_response_l2_upper_bound"]
        + 1.0e-10
    )
    assert ledger["signed"]["exact"].real <= (
        audit["parity_exact_ledger"]["exact_response_norm_upper_bound"]
        + 1.0e-10
    )
    print(
        "soft zeta orbit audit passed: "
        f"support={direction['support_size']}, "
        f"exact={ledger['signed']['exact'].real:.6g}, "
        f"near={ledger['signed']['near'].real:.6g}, "
        f"far={ledger['signed']['far'].real:.6g}, "
        "canonical/arbitrary="
        f"{direction['canonical_to_arbitrary_depth_ratio']:.6g}, "
        "breaker="
        f"{audit['parity_exact_ledger']['breaker_fraction']:.6g}, "
        "small-mixture="
        f"{audit['gaussian_mixture_ledger']['signed'][0].real:.6g}, "
        "inner-heat="
        f"{audit['heat_shell_audit']['signed_weighted'][0].real:.6g}, "
        "profile/variation="
        f"{audit['signed_profile_audit'][0]['capacity_to_variation_ratio']:.6g}, "
        "Cauchy-profile/variation="
        f"{audit['cauchy_profile_audit']['capacity_to_variation_ratio']:.6g}"
    )


if __name__ == "__main__":
    main()

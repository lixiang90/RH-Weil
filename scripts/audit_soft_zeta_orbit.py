"""Frozen finite audit of the canonical soft zeta orbit direction.

This is a diagnostic of a small Abel prime--continuum quadrature.  It is not
an interval certificate, a cofinal estimate, or evidence for RH.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np

from formal_lag_response import (
    brownian_component_cross_sign_ledger,
    brownian_primitive_component_gram,
    cauchy_gaussian_mixture_band_ledger,
    cauchy_profile_brownian_energy_ledger,
    cauchy_signed_layer_cake_ledger,
    cauchy_translate_compactness_ledger,
    chebyshev_formal_orbit_coefficients,
    degree_two_gaussian_response_upper_bound,
    degree_two_centered_response_decomposition,
    degree_two_centered_response_channel_maps,
    degree_two_parity_exact_ledger,
    degree_two_response_frequency_map,
    formal_arbitrary_direction_audit,
    formal_cauchy_response_ledger,
    gaussian_heat_shell_ledger,
    gaussian_signed_layer_cake_ledger,
    stationary_response_from_frequency_map,
    two_sided_prime_continuum_symbol,
)
from qw_matrix import (
    canonical_vaughan_two_channel_coefficients,
    zeta_abel_shared_lag_loewner_quadrature,
)
from soft_negative_moment import chebyshev_soft_series


def soft_zeta_orbit_audit(
    *,
    scale: float,
    integer_cutoff: int,
    lag_cells: int,
    degree: int,
    vaughan_cutoff: int | None = None,
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
    brownian_energy_audit = (
        cauchy_profile_brownian_energy_ledger(
            response_map, formal["continuum_nodes"]
        )
        if response_map is not None
        else None
    )
    compactness_audit = (
        cauchy_translate_compactness_ledger(
            response_map,
            formal["continuum_nodes"],
            (-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0),
        )
        if response_map is not None
        else None
    )
    vaughan_brownian_audit = None
    if response_map is not None:
        if vaughan_cutoff is None:
            # A simultaneous square-root cutoff makes Type II vacuous:
            # (U+1)(V+1)>N.  The balanced cube-root choice leaves a genuine
            # Type-II range and is the relevant finite channel audit.
            vaughan_cutoff = max(1, int(integer_cutoff ** (1.0 / 3.0)))
            while (vaughan_cutoff + 1) ** 3 <= integer_cutoff:
                vaughan_cutoff += 1
            while vaughan_cutoff**3 > integer_cutoff:
                vaughan_cutoff -= 1
        if not 1 <= vaughan_cutoff <= integer_cutoff:
            raise ValueError("Vaughan cutoff must lie in [1, integer_cutoff]")
        vaughan = canonical_vaughan_two_channel_coefficients(
            integer_cutoff, vaughan_cutoff, vaughan_cutoff
        )
        type_i_atoms = []
        type_ii_atoms = []
        for integer, coefficient in prime_atoms:
            target = complex(vaughan["target"][integer])
            if abs(target) <= 1.0e-15:
                if abs(coefficient) > 1.0e-12:
                    raise ArithmeticError(
                        "prime quadrature atom has zero Mangoldt target"
                    )
                continue
            common_weight = coefficient / target
            type_i_atoms.append(
                (
                    integer,
                    common_weight
                    * complex(vaughan["components"]["type_i"][integer]),
                )
            )
            type_ii_atoms.append(
                (
                    integer,
                    common_weight
                    * complex(vaughan["components"]["type_ii"][integer]),
                )
            )
        type_i_formal = two_sided_prime_continuum_symbol(
            type_i_atoms, continuum_atoms
        )
        type_ii_formal = two_sided_prime_continuum_symbol(
            type_ii_atoms, continuum_atoms
        )
        channel_factorization = degree_two_centered_response_channel_maps(
            {
                "type_i": type_i_formal["prime_map"],
                "type_ii": type_ii_formal["prime_map"],
                "continuum": formal["continuum_map"],
            },
            spectral_bound,
            rho,
        )
        channel_gram = brownian_primitive_component_gram(
            channel_factorization["response_components"],
            formal["continuum_nodes"],
        )
        base_cross_sign = brownian_component_cross_sign_ledger(
            {
                "prime": formal["prime_map"],
                "continuum": formal["continuum_map"],
            },
            formal["continuum_nodes"],
            ("prime",),
            "continuum",
        )
        physical_cross_sign = brownian_component_cross_sign_ledger(
            channel_factorization["response_components"],
            formal["continuum_nodes"],
            ("type_i", "type_ii"),
            "continuum",
        )
        vaughan_brownian_audit = {
            "mobius_cutoff": vaughan_cutoff,
            "mangoldt_cutoff": vaughan_cutoff,
            "type_ii_support_lower_bound": vaughan[
                "type_ii_support_lower_bound"
            ],
            "symbol_reconstruction_residual": max(
                [
                    abs(value)
                    for value in (
                        channel_factorization["symbol"].get(lag, 0.0 + 0.0j)
                        - coefficient
                        for lag, coefficient in symbol.items()
                    )
                ]
                + [
                    abs(value)
                    for lag, value in channel_factorization["symbol"].items()
                    if lag not in symbol
                ]
                + [0.0]
            ),
            "response_reconstruction_residual": channel_factorization[
                "maximum_reconstruction_residual"
            ],
            "channel_gram": channel_gram,
            "base_cross_sign": base_cross_sign,
            "physical_cross_sign": physical_cross_sign,
            "spectral_overlap_data": {
                "prime_component": formal["prime_map"],
                "continuum_component": formal["continuum_map"],
                "common_symbol": channel_factorization["symbol"],
                "continuum_nodes": formal["continuum_nodes"],
                "total_mass": channel_factorization["total_mass"],
                "level": channel_factorization["level"],
                "response_scalar": -(
                    channel_factorization["polynomial_factor"] ** 2
                ),
            },
            "diagonal_to_full_ratio": (
                channel_gram["diagonal_sum"] / channel_gram["total_energy"]
                if channel_gram["total_energy"] > 0.0
                else 0.0
            ),
        }
    centered_response_audit = None
    if response_map is not None:
        decomposition = degree_two_centered_response_decomposition(
            symbol, spectral_bound, rho
        )
        centered_response_audit = {
            "total_mass": decomposition["total_mass"],
            "relative_total_mass": (
                decomposition["total_mass"] / spectral_bound
            ),
            "balanced_profile": cauchy_signed_layer_cake_ledger(
                decomposition["balanced_square_response"],
                formal["continuum_nodes"],
            ),
            "mass_correction_profile": cauchy_signed_layer_cake_ledger(
                decomposition["mass_correction_response"],
                formal["continuum_nodes"],
            ),
        }
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
        "brownian_energy_audit": brownian_energy_audit,
        "compactness_audit": compactness_audit,
        "vaughan_brownian_audit": vaughan_brownian_audit,
        "centered_response_audit": centered_response_audit,
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
    assert audit["brownian_energy_audit"] is not None
    assert abs(audit["brownian_energy_audit"]["signed_cauchy_response"]) <= (
        audit["brownian_energy_audit"]["signed_response_upper_bound"]
        + 1.0e-10
    )
    assert audit["compactness_audit"] is not None
    assert audit["compactness_audit"]["minimum_test_gram_eigenvalue"] >= (
        -1.0e-10
    )
    assert audit["compactness_audit"]["range_residual"] <= 1.0e-10
    assert audit["compactness_audit"]["least_norm_squared"] <= (
        audit["compactness_audit"]["actual_package_norm_squared"] + 1.0e-10
    )
    assert audit["compactness_audit"]["minimum_budget_block_eigenvalue"] >= (
        -1.0e-10
    )
    assert audit["vaughan_brownian_audit"] is not None
    assert (
        audit["vaughan_brownian_audit"]["symbol_reconstruction_residual"]
        <= 1.0e-10
    )
    assert (
        audit["vaughan_brownian_audit"]["response_reconstruction_residual"]
        <= 1.0e-10
    )
    channel_gram = audit["vaughan_brownian_audit"]["channel_gram"]
    assert channel_gram["minimum_eigenvalue"] >= -1.0e-10
    assert max(
        abs(value) for value in channel_gram["centered_mass_residuals"]
    ) <= 1.0e-10
    assert abs(
        channel_gram["total_energy"]
        - audit["brownian_energy_audit"]["primitive_l2_energy"]
    ) <= 1.0e-10
    assert audit["centered_response_audit"] is not None
    assert abs(
        audit["centered_response_audit"]["balanced_profile"]["total_response"]
        + audit["centered_response_audit"]["mass_correction_profile"]["total_response"]
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
        f"{audit['cauchy_profile_audit']['capacity_to_variation_ratio']:.6g}, "
        "M/B="
        f"{audit['centered_response_audit']['relative_total_mass'].real:.6g}, "
        "Brownian-bound/actual="
        f"{audit['brownian_energy_audit']['signed_upper_to_actual_ratio']:.6g}, "
        "Vaughan-diagonal/full="
        f"{audit['vaughan_brownian_audit']['diagonal_to_full_ratio']:.6g}, "
        "compactness-capture="
        f"{audit['compactness_audit']['captured_norm_ratio']:.6g}"
    )


if __name__ == "__main__":
    main()

"""Rigorous second-scale B1h finite overlap certificate.

The pre-registered instance is (Y,N,J,h)=(16,15,4,1/200), with positive
frequencies below 256.  This script independently encloses the intended base
coefficients, certifies the binary64 surrogate Brownian energies by rational
atom ordering, transfers those energies to the intended response, and then
performs the same directed whole-cell numerator audit as B1g.

Only one additional finite instance is proved.  No scale-uniform estimate and
no assertion about RH or GRH is made.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import sys

from audit_soft_zeta_orbit import soft_zeta_orbit_audit
from b1f_base_coefficient_interval_audit import (
    add_scaled,
    audited_centered_component,
    audited_float_convolution,
    audited_float_scale,
    audited_float_sum,
    center,
    float_map_tv_norm,
    interval_sum,
    point,
    rationalize_map,
)
from b1g_directed_numerator_interval_audit import (
    FIXED_SCALE,
    FixedInterval,
    ceiling_fraction,
    decimal_lower_from_fixed,
    floor_fraction,
    fixed_polynomial,
    multiply_lower,
    rational_cosine_fixed,
)
from brownian_interval_certificate import (
    RationalInterval,
    brownian_cluster_energy_upper_bound,
    brownian_tv_perturbation_upper_bound,
    canonical_position_interval,
    canonical_rational_grid_key,
    centered_component_tv_error_upper_bound,
    polynomial_convolution_tv_error_upper_bound,
    rational_decimal_lower,
    rational_decimal_upper,
    rational_exp_interval,
    rational_exp_point_interval,
    rational_log_interval,
    rational_square_root_interval,
)
from formal_lag_response import (
    FormalLag,
    degree_two_centered_response_channel_maps,
)


SCALE = 16
INTEGER_CUTOFF = 15
LAG_CELLS = 4
FREQUENCY_STEP = Fraction(1, 200)
FREQUENCY_CUTOFF = Fraction(256)
CELL_RADIUS = FREQUENCY_STEP / 2
SAMPLE_COUNT = int(FREQUENCY_CUTOFF / FREQUENCY_STEP)
RATIO_LOWER = Fraction(1, 4)
RATIO_UPPER = Fraction(4)
PRIME_POWERS = (
    (2, 2),
    (3, 3),
    (4, 2),
    (5, 5),
    (7, 7),
    (8, 2),
    (9, 3),
    (11, 11),
    (13, 13),
)
SMOOTH_PRIMES = (2, 3, 5, 7, 11, 13)
FROZEN_B1H_INTENDED_DENOMINATOR_UPPER = Fraction(
    "0.001025620093083457466797381202"
)
FROZEN_B1H_NUMERATOR_LOWER = Fraction(
    "0.000163944504546660552689839988"
)
FROZEN_B1H_VERIFIED_CELL_COUNT = 10065
FROZEN_B1H_INDEX_SHA256 = (
    "6ee45ac6e3d3908bb2b0fa464f98672065d9a6718f46e44d79d06a19bf6efdc9"
)
FROZEN_B1H_BOUND_SHA256 = (
    "52c87473889013e920172f3a1eb80831540bbba61d388561b9e5256d77c1ce40"
)


def abel_density_interval(value: Fraction) -> RationalInterval:
    """Enclose exp(2*x/5-exp(x)/16) at a rational x."""
    outer = rational_exp_point_interval(value)
    exponent = point(Fraction(2, 5) * value).subtract(
        outer.multiply(point(Fraction(1, SCALE)))
    )
    return rational_exp_interval(exponent)


def continuum_mass_interval(
    left: Fraction, right: Fraction, panels: int = 8
) -> RationalInterval:
    """Composite-Simpson enclosure; the B1f global fourth-derivative bound applies."""
    if not Fraction(0) <= left < right <= Fraction(2):
        raise ValueError("continuum interval must lie in [0,2]")
    if panels < 2 or panels % 2:
        raise ValueError("Simpson panels must be positive and even")
    step = (right - left) / panels
    weighted = point(0)
    for index in range(panels + 1):
        weight = 1 if index in (0, panels) else (4 if index % 2 else 2)
        weighted = weighted.add(
            abel_density_interval(left + index * step).scale_integer(weight)
        )
    approximation = weighted.multiply(point(step / 3))
    # For Y=16 and x in [0,2], f<3, |g'|<1, and exp(x)/Y<1.
    # Hence the same conservative |f''''|<45 used in B1f remains valid.
    if rational_exp_point_interval(Fraction(4, 5)).upper >= 3:
        raise AssertionError("failed to certify f < 3")
    if rational_exp_point_interval(Fraction(2)).upper >= SCALE:
        raise AssertionError("failed to certify exp(2)/Y < 1")
    error = (right - left) * step**4 * Fraction(1, 4)
    return RationalInterval(
        max(Fraction(0), approximation.lower - error),
        approximation.upper + error,
    )


def prime_weight_interval(integer: int, prime: int) -> RationalInterval:
    """Enclose Lambda(n)n^(-3/5)exp(-n/16)."""
    log_prime = rational_log_interval(Fraction(prime))
    log_integer = rational_log_interval(Fraction(integer))
    exponent = log_integer.multiply(point(Fraction(-3, 5))).subtract(
        point(Fraction(integer, SCALE))
    )
    return log_prime.multiply(rational_exp_interval(exponent))


def rational_surrogate_energy_upper(
    component: dict[FormalLag, complex],
    rational_nodes: tuple[Fraction, ...],
) -> tuple[Fraction, int, int]:
    """Certify the exactly recentered binary64 response Brownian energy."""
    grouped: dict[tuple[Fraction, Fraction], Fraction] = {}
    for lag, coefficient in component.items():
        if coefficient.imag != 0.0:
            raise AssertionError("B1h response must remain real")
        key = canonical_rational_grid_key(lag, rational_nodes)
        grouped[key] = grouped.get(key, Fraction(0)) + Fraction.from_float(
            float(coefficient.real)
        )
    zero = (Fraction(1), Fraction(0))
    grouped[zero] = grouped.get(zero, Fraction(0)) - sum(
        grouped.values(), Fraction(0)
    )
    atoms = []
    for key, coefficient in grouped.items():
        if coefficient:
            interval = canonical_position_interval(
                key,
                terms=96,
                smooth_primes=SMOOTH_PRIMES,
            )
            atoms.append((interval.lower, interval.upper, coefficient))
    certificate = brownian_cluster_energy_upper_bound(atoms)
    return (
        Fraction(certificate["energy_upper"]),
        int(certificate["cluster_count"]),
        int(certificate["maximum_cluster_size"]),
    )


def build_interval_data() -> dict[str, object]:
    lag_start = Fraction(3, 100)
    lag_end = Fraction(2)
    lag_width = (lag_end - lag_start) / LAG_CELLS
    edges = tuple(
        lag_start + index * lag_width for index in range(LAG_CELLS + 1)
    )
    continuum_nodes = tuple(
        (edges[index] + edges[index + 1]) / 2
        for index in range(LAG_CELLS)
    )
    prime_weights = tuple(
        prime_weight_interval(integer, prime)
        for integer, prime in PRIME_POWERS
    )
    prime_lags = tuple(
        rational_log_interval(Fraction(integer))
        for integer, _ in PRIME_POWERS
    )
    continuum_masses = (
        continuum_mass_interval(Fraction(0), lag_start),
    ) + tuple(
        continuum_mass_interval(edges[index], edges[index + 1])
        for index in range(LAG_CELLS)
    )
    prime_mass = interval_sum(prime_weights)
    continuum_mass = interval_sum(continuum_masses)
    symbol_norm = prime_mass.add(continuum_mass)
    total_mass = prime_mass.subtract(continuum_mass)
    kappa = rational_square_root_interval(Fraction(3)).multiply(
        point(Fraction(1, 2))
    )
    level = kappa.multiply(symbol_norm)
    difference = total_mass.subtract(level)
    coefficients = (
        total_mass.square().multiply(difference.square()),
        total_mass.multiply(difference.square()),
        difference.square(),
        total_mass.subtract(level.scale_integer(2)),
        point(1),
    )
    amplitude = kappa.divide(kappa.add(point(Fraction(1, 3))))
    scalar = amplitude.square().multiply(point(Fraction(-4, 9))).divide(
        symbol_norm.square().square()
    )
    return {
        "continuum_nodes": continuum_nodes,
        "prime_weights": prime_weights,
        "prime_lags": prime_lags,
        "continuum_masses": continuum_masses,
        "prime_mass": prime_mass,
        "continuum_mass": continuum_mass,
        "symbol_norm": symbol_norm,
        "total_mass": total_mass,
        "level": level,
        "difference": difference,
        "coefficients": coefficients,
        "scalar": scalar,
    }


def intended_denominator_upper(data: dict[str, object]) -> tuple[Fraction, dict[str, object]]:
    if not (
        sys.float_info.radix == 2
        and sys.float_info.mant_dig == 53
        and sys.float_info.max_exp == 1024
        and sys.float_info.min_exp == -1021
        and sys.float_info.rounds == 1
    ):
        raise RuntimeError("B1h audit requires round-to-nearest IEEE binary64")
    audit = soft_zeta_orbit_audit(
        scale=float(SCALE),
        integer_cutoff=INTEGER_CUTOFF,
        lag_cells=LAG_CELLS,
        degree=2,
    )
    formal = audit["formal_symbol"]
    spectral = audit["vaughan_brownian_audit"]["spectral_overlap_data"]
    factorization = degree_two_centered_response_channel_maps(
        {
            "prime": spectral["prime_component"],
            "continuum": spectral["continuum_component"],
        },
        audit["spectral_bound"],
        audit["rho"],
    )
    dimension = len(formal["continuum_nodes"])
    zero = FormalLag.zero(dimension)

    prime_weights = data["prime_weights"]
    continuum_masses = data["continuum_masses"]
    prime_mass = data["prime_mass"]
    continuum_mass = data["continuum_mass"]
    symbol_norm = data["symbol_norm"]
    coefficients = data["coefficients"]
    scalar = data["scalar"]

    surrogate_prime_weights = tuple(
        2
        * Fraction.from_float(
            float(formal["prime_map"][FormalLag.prime(integer, dimension)].real)
        )
        for integer, _ in PRIME_POWERS
    )
    prime_error = sum(
        (
            interval.distance_upper(surrogate)
            for interval, surrogate in zip(
                prime_weights, surrogate_prime_weights
            )
        ),
        Fraction(0),
    )
    surrogate_continuum_masses = [
        -Fraction.from_float(float(formal["continuum_map"][zero].real))
    ]
    for index in range(LAG_CELLS):
        lag = FormalLag.continuum_basis(index, dimension)
        surrogate_continuum_masses.append(
            -2
            * Fraction.from_float(
                float(formal["continuum_map"][lag].real)
            )
        )
    continuum_error = sum(
        (
            interval.distance_upper(surrogate)
            for interval, surrogate in zip(
                continuum_masses, surrogate_continuum_masses
            )
        ),
        Fraction(0),
    )
    symbol_error = prime_error + continuum_error
    prime_map = rationalize_map(formal["prime_map"])
    continuum_map = rationalize_map(formal["continuum_map"])
    symbol_map = dict(prime_map)
    add_scaled(symbol_map, continuum_map, Fraction(1))
    surrogate_symbol_norm = sum(
        (abs(value) for value in symbol_map.values()), Fraction(0)
    )
    symbol_norm_upper = max(symbol_norm.upper, surrogate_symbol_norm)

    # Use the exact floating operands consumed by the production factorization.
    # The surrounding ledger may accumulate the same values in another order.
    surrogate_total_mass = complex(factorization["total_mass"])
    surrogate_level = float(factorization["level"])
    surrogate_difference = surrogate_total_mass - surrogate_level
    surrogate_coefficient_values = (
        surrogate_total_mass**2 * surrogate_difference**2,
        surrogate_total_mass * surrogate_difference**2,
        surrogate_difference**2,
        surrogate_total_mass - 2.0 * surrogate_level,
        1.0 + 0.0j,
    )
    surrogate_coefficients = tuple(
        Fraction.from_float(float(value.real))
        for value in surrogate_coefficient_values
    )
    coefficient_abs_uppers = tuple(
        interval.abs_upper() for interval in coefficients
    )
    coefficient_error_uppers = tuple(
        interval.distance_upper(surrogate)
        for interval, surrogate in zip(
            coefficients, surrogate_coefficients
        )
    )
    polynomial_error = polynomial_convolution_tv_error_upper_bound(
        symbol_norm_upper,
        symbol_error,
        coefficient_abs_uppers,
        coefficient_error_uppers,
    )
    polynomial_norm_upper = sum(
        (
            coefficient_abs_uppers[degree] * symbol_norm_upper**degree
            for degree in range(5)
        ),
        Fraction(0),
    )
    production_response_scalar = -float(factorization["polynomial_factor"]) ** 2
    surrogate_scalar = Fraction.from_float(production_response_scalar)
    scalar_error = scalar.distance_upper(surrogate_scalar)

    identity = {zero: 1.0 + 0.0j}
    audited_powers: dict[int, tuple[dict[FormalLag, complex], Fraction]] = {
        0: (identity, Fraction(0))
    }
    for degree in range(1, 5):
        audited_powers[degree] = audited_float_convolution(
            audited_powers[degree - 1][0],
            audited_powers[degree - 1][1],
            factorization["symbol"],
            Fraction(0),
        )
    scaled_terms = (
        audited_powers[4],
        audited_float_scale(
            audited_powers[3][0],
            audited_powers[3][1],
            surrogate_coefficient_values[3],
        ),
        audited_float_scale(
            audited_powers[2][0],
            audited_powers[2][1],
            surrogate_coefficient_values[2],
        ),
        audited_float_scale(
            audited_powers[1][0],
            audited_powers[1][1],
            surrogate_coefficient_values[1],
        ),
        audited_float_scale(
            audited_powers[0][0],
            audited_powers[0][1],
            surrogate_coefficient_values[0],
        ),
    )
    audited_polynomial, polynomial_roundoff = audited_float_sum(scaled_terms)
    if audited_polynomial != factorization["divided_difference"]:
        raise AssertionError("audited polynomial did not replay production code")

    response_data: dict[str, dict[str, Fraction | int]] = {}
    rational_nodes = data["continuum_nodes"]
    denominator_upper = Fraction(0)
    for label, formal_component, base_map, base_error, base_norm_upper in (
        ("prime", formal["prime_map"], prime_map, prime_error, prime_mass.upper),
        (
            "continuum",
            formal["continuum_map"],
            continuum_map,
            continuum_error,
            continuum_mass.upper,
        ),
    ):
        surrogate_centered = center(base_map, zero)
        float_centered, centering_roundoff = audited_centered_component(
            formal_component, zero
        )
        float_convolution, convolution_roundoff = audited_float_convolution(
            float_centered,
            centering_roundoff,
            audited_polynomial,
            polynomial_roundoff,
        )
        replayed_response, expansion_error = audited_float_scale(
            float_convolution,
            convolution_roundoff,
            complex(production_response_scalar),
        )
        if replayed_response != factorization["response_components"][label]:
            raise AssertionError("audited response did not replay production code")
        response_mass_residual = abs(
            sum(
                (
                    Fraction.from_float(float(value.real))
                    for value in replayed_response.values()
                ),
                Fraction(0),
            )
        )
        expansion_error += response_mass_residual
        intended_to_ideal = (
            scalar_error * 2 * base_norm_upper * polynomial_norm_upper
            + abs(surrogate_scalar)
            * centered_component_tv_error_upper_bound(base_error)
            * polynomial_norm_upper
            + abs(surrogate_scalar)
            * sum(
                (abs(value) for value in surrogate_centered.values()),
                Fraction(0),
            )
            * polynomial_error
        )
        response_error = intended_to_ideal + expansion_error
        surrogate_energy_upper, cluster_count, max_cluster = (
            rational_surrogate_energy_upper(
                factorization["response_components"][label],
                rational_nodes,
            )
        )
        channel_upper = brownian_tv_perturbation_upper_bound(
            surrogate_energy_upper,
            Fraction(30),
            response_error,
            Fraction(1, 100),
        )
        denominator_upper += channel_upper
        response_data[label] = {
            "surrogate_energy_upper": surrogate_energy_upper,
            "response_error": response_error,
            "cluster_count": cluster_count,
            "maximum_cluster_size": max_cluster,
            "channel_upper": channel_upper,
        }
    response_data["base"] = {
        "prime_error": prime_error,
        "continuum_error": continuum_error,
        "polynomial_error": polynomial_error,
        "scalar_error": scalar_error,
    }
    return denominator_upper, response_data


def directed_numerator_lower(data: dict[str, object]) -> dict[str, object]:
    prime_weights = data["prime_weights"]
    prime_lags = data["prime_lags"]
    continuum_masses = data["continuum_masses"]
    continuum_nodes = data["continuum_nodes"]
    symbol_norm = data["symbol_norm"]
    total_mass = data["total_mass"]
    level = data["level"]
    difference = data["difference"]
    coefficients = data["coefficients"]
    scalar = data["scalar"]

    prime_lipschitz_upper = sum(
        (
            weight.multiply(lag).upper
            for weight, lag in zip(prime_weights, prime_lags)
        ),
        Fraction(0),
    )
    continuum_lipschitz_upper = sum(
        (
            continuum_masses[index + 1].multiply(point(node)).upper
            for index, node in enumerate(continuum_nodes)
        ),
        Fraction(0),
    )
    symbol_lipschitz_upper = (
        prime_lipschitz_upper + continuum_lipschitz_upper
    )
    derivative_supremum = (
        4 * symbol_norm.upper**3
        + 3
        * total_mass.subtract(level.scale_integer(2)).abs_upper()
        * symbol_norm.upper**2
        + 2 * difference.abs_upper() ** 2 * symbol_norm.upper
        + total_mass.abs_upper() * difference.abs_upper() ** 2
    )
    q_lipschitz_upper = derivative_supremum * symbol_lipschitz_upper
    prime_radius_error = ceiling_fraction(prime_lipschitz_upper * CELL_RADIUS)
    continuum_radius_error = ceiling_fraction(
        continuum_lipschitz_upper * CELL_RADIUS
    )
    q_radius_error = ceiling_fraction(q_lipschitz_upper * CELL_RADIUS)

    prime_weight_fixed = tuple(
        FixedInterval.from_rational_interval(weight) for weight in prime_weights
    )
    continuum_mass_fixed = tuple(
        FixedInterval.from_rational_interval(mass) for mass in continuum_masses
    )
    fixed_coefficients = tuple(
        FixedInterval.from_rational_interval(value) for value in coefficients
    )
    prefactor_lower = floor_fraction(
        scalar.square().lower * FREQUENCY_STEP
        / rational_pi_upper()
    )

    verified_indices: list[int] = []
    verified_bounds: list[tuple[int, int]] = []
    numerator_lower = 0
    for index in range(1, SAMPLE_COUNT):
        midpoint = Fraction(2 * index + 1, 400)
        wp = FixedInterval(0, 0)
        dhat = FixedInterval(0, 0)
        for weight, lag in zip(prime_weight_fixed, prime_lags):
            cosine = rational_cosine_fixed(lag.multiply(point(midpoint)))
            one_minus_cosine = FixedInterval(
                FIXED_SCALE - cosine.upper,
                FIXED_SCALE - cosine.lower,
            ).intersect(0, 2 * FIXED_SCALE)
            wp = wp.add(weight.multiply(one_minus_cosine))
            dhat = dhat.add(weight.multiply(cosine))
        wc = FixedInterval(0, 0)
        dhat = dhat.subtract(continuum_mass_fixed[0])
        for mass, node in zip(continuum_mass_fixed[1:], continuum_nodes):
            cosine = rational_cosine_fixed(point(midpoint * node))
            one_minus_cosine = FixedInterval(
                FIXED_SCALE - cosine.upper,
                FIXED_SCALE - cosine.lower,
            ).intersect(0, 2 * FIXED_SCALE)
            wc = wc.add(mass.multiply(one_minus_cosine))
            dhat = dhat.subtract(mass.multiply(cosine))

        wp_lower = max(0, wp.lower - prime_radius_error)
        wp_upper = wp.upper + prime_radius_error
        wc_lower = max(0, wc.lower - continuum_radius_error)
        wc_upper = wc.upper + continuum_radius_error
        q_midpoint = fixed_polynomial(dhat, fixed_coefficients)
        q_lower = max(0, q_midpoint.abs_lower() - q_radius_error)
        if not (
            wp_lower > 0
            and wc_lower > 0
            and q_lower > 0
            and 4 * wp_lower >= wc_upper
            and wp_upper <= 4 * wc_lower
        ):
            continue
        wp_square_lower = wp_lower * wp_lower // FIXED_SCALE
        wc_square_lower = wc_lower * wc_lower // FIXED_SCALE
        q_square_lower = q_lower * q_lower // FIXED_SCALE
        contribution = multiply_lower(prefactor_lower, q_square_lower)
        contribution = multiply_lower(
            contribution, wp_square_lower + wc_square_lower
        )
        right_endpoint = (index + 1) * FREQUENCY_STEP
        contribution = multiply_lower(
            contribution, floor_fraction(1 / right_endpoint**2)
        )
        numerator_lower += contribution
        verified_indices.append(index)
        verified_bounds.append((index, contribution))

    index_payload = (
        "B1h-v1|Y=16|N=15|J=4|h=1/200|cutoff=256|ratio=1/4,4|"
        + ",".join(str(index) for index in verified_indices)
    ).encode("ascii")
    bound_payload = (
        "B1h-v1|scale=10^60|"
        + ",".join(f"{index}:{bound}" for index, bound in verified_bounds)
    ).encode("ascii")
    return {
        "numerator_lower": Fraction(numerator_lower, FIXED_SCALE),
        "verified_indices": tuple(verified_indices),
        "verified_bounds": tuple(verified_bounds),
        "verified_cell_count": len(verified_indices),
        "index_hash": sha256(index_payload).hexdigest(),
        "bound_hash": sha256(bound_payload).hexdigest(),
    }


def rational_pi_upper() -> Fraction:
    # PI_RATIONAL is held in B1g; importing lazily keeps this dependency explicit.
    from b1g_directed_numerator_interval_audit import PI_RATIONAL

    return PI_RATIONAL.upper


def main() -> None:
    data = build_interval_data()
    denominator_upper, response_data = intended_denominator_upper(data)
    numerator = directed_numerator_lower(data)
    numerator_lower = Fraction(numerator["numerator_lower"])
    ratio_lower = numerator_lower / denominator_upper
    if denominator_upper > FROZEN_B1H_INTENDED_DENOMINATOR_UPPER:
        raise AssertionError("frozen B1h denominator upper is too small")
    if numerator_lower < FROZEN_B1H_NUMERATOR_LOWER:
        raise AssertionError("frozen B1h numerator lower is too large")
    if numerator["verified_cell_count"] != FROZEN_B1H_VERIFIED_CELL_COUNT:
        raise AssertionError("frozen B1h verified-cell count changed")
    if numerator["index_hash"] != FROZEN_B1H_INDEX_SHA256:
        raise AssertionError("frozen B1h verified-cell index hash changed")
    if numerator["bound_hash"] != FROZEN_B1H_BOUND_SHA256:
        raise AssertionError("frozen B1h verified-cell bound hash changed")
    if ratio_lower <= Fraction(3, 20):
        raise AssertionError("B1h directed finite ratio did not clear 0.15")

    base = response_data["base"]
    print(
        "prime_base_tv_error_upper=",
        rational_decimal_upper(base["prime_error"], 30),
        sep="",
    )
    print(
        "continuum_base_tv_error_upper=",
        rational_decimal_upper(base["continuum_error"], 30),
        sep="",
    )
    print(
        "polynomial_tv_error_upper=",
        rational_decimal_upper(base["polynomial_error"], 30),
        sep="",
    )
    print(
        "scalar_error_upper=",
        rational_decimal_upper(base["scalar_error"], 30),
        sep="",
    )
    for label in ("prime", "continuum"):
        channel = response_data[label]
        print(
            f"{label}_surrogate_energy_upper=",
            rational_decimal_upper(channel["surrogate_energy_upper"], 30),
            sep="",
        )
        print(
            f"{label}_response_tv_error_upper=",
            rational_decimal_upper(channel["response_error"], 30),
            sep="",
        )
        print(
            f"{label}_clusters={channel['cluster_count']},"
            f" max_cluster={channel['maximum_cluster_size']}"
        )
    print(
        "intended_denominator_upper=",
        rational_decimal_upper(denominator_upper, 30),
        sep="",
    )
    print(f"verified_cell_count={numerator['verified_cell_count']}")
    print(
        "verified_width_lower=",
        rational_decimal_lower(
            numerator["verified_cell_count"] * FREQUENCY_STEP, 12
        ),
        sep="",
    )
    print(f"verified_index_sha256={numerator['index_hash']}")
    print(f"verified_bound_sha256={numerator['bound_hash']}")
    print(
        "numerator_lower=",
        rational_decimal_lower(numerator_lower, 30),
        sep="",
    )
    print(
        "ratio_lower=",
        rational_decimal_lower(ratio_lower, 18),
        sep="",
    )
    print(
        "overlap_delta_lower=",
        rational_decimal_lower(Fraction(3, 85), 18),
        sep="",
    )
    print(
        "diagonal_to_full_lower=",
        rational_decimal_lower(Fraction(85, 79), 18),
        sep="",
    )
    print("B1h second-scale interval audit passed")
    print("[scope] two finite ratios only; scale-uniform overlap and RH remain open")


if __name__ == "__main__":
    main()

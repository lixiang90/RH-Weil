"""Rational base-coefficient and Brownian denominator audit for B1f.

The target is the single finite model (Y,N,J)=(8,10,4).  This script
certifies coefficient intervals and transfers them through the degree-two
response in total variation.  It does not yet certify the good-cell
trigonometric numerator and makes no asymptotic or RH claim.
"""

from __future__ import annotations

from fractions import Fraction
import sys

from audit_soft_zeta_orbit import soft_zeta_orbit_audit
from brownian_interval_certificate import (
    FROZEN_B1E_SURROGATE_ENERGY_UPPERS,
    RationalInterval,
    brownian_tv_perturbation_upper_bound,
    centered_component_tv_error_upper_bound,
    polynomial_convolution_tv_error_upper_bound,
    rational_decimal_upper,
    rational_exp_interval,
    rational_exp_point_interval,
    rational_log_interval,
    rational_square_root_interval,
)
from formal_lag_response import (
    FormalLag,
    add_frequency_maps,
    convolve_frequency_maps,
    degree_two_centered_response_channel_maps,
    scale_frequency_map,
)


RationalMap = dict[FormalLag, Fraction]
FLOAT_TOLERANCE = Fraction.from_float(1.0e-14)
UNIT_ROUNDOFF = Fraction(1, 2**53)
MINIMUM_SUBNORMAL = Fraction(1, 2**1074)
PRUNING_ERROR = FLOAT_TOLERANCE / (1 - UNIT_ROUNDOFF) + 4 * MINIMUM_SUBNORMAL
FROZEN_B1F_INTENDED_DENOMINATOR_UPPER = Fraction(
    "0.000735925241553713216150037691"
)


def point(value: Fraction | int) -> RationalInterval:
    value = Fraction(value)
    return RationalInterval(value, value)


def interval_sum(values: tuple[RationalInterval, ...]) -> RationalInterval:
    result = point(0)
    for value in values:
        result = result.add(value)
    return result


def abel_density_interval(value: Fraction) -> RationalInterval:
    """Enclose exp(2*x/5-exp(x)/8) at one rational x."""
    outer = rational_exp_point_interval(value)
    exponent = point(Fraction(2, 5) * value).subtract(
        outer.multiply(point(Fraction(1, 8)))
    )
    return rational_exp_interval(exponent)


def continuum_mass_interval(
    left: Fraction, right: Fraction, panels: int = 8
) -> RationalInterval:
    """Composite-Simpson enclosure with the global |f''''| <= 45 bound."""
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
    # f=exp(g), g'=2/5-u, g^(k)=-u (k>=2), u=exp(x)/8.
    # On [0,2], f<3, |g'|<1 and u<1, hence |f''''|<3*(1+4+3+6+1)=45.
    if rational_exp_point_interval(Fraction(4, 5)).upper >= 3:
        raise AssertionError("failed to certify f < 3")
    if rational_exp_point_interval(Fraction(2)).upper >= 8:
        raise AssertionError("failed to certify exp(2)/8 < 1")
    error = (right - left) * step**4 * Fraction(1, 4)
    return RationalInterval(
        max(Fraction(0), approximation.lower - error),
        approximation.upper + error,
    )


def prime_weight_interval(integer: int, prime: int) -> RationalInterval:
    """Enclose Lambda(n)n^(-3/5)exp(-n/8) for n=p^k."""
    log_prime = rational_log_interval(Fraction(prime))
    log_integer = rational_log_interval(Fraction(integer))
    exponent = log_integer.multiply(point(Fraction(-3, 5))).subtract(
        point(Fraction(integer, 8))
    )
    return log_prime.multiply(rational_exp_interval(exponent))


def add_scaled(target: RationalMap, source: RationalMap, scalar: Fraction) -> None:
    for lag, coefficient in source.items():
        value = target.get(lag, Fraction(0)) + scalar * coefficient
        if value:
            target[lag] = value
        else:
            target.pop(lag, None)


def rationalize_map(source: dict[FormalLag, complex]) -> RationalMap:
    result: RationalMap = {}
    for lag, coefficient in source.items():
        if coefficient.imag != 0.0:
            raise AssertionError("fixed symmetric model must have real coefficients")
        result[lag] = Fraction.from_float(float(coefficient.real))
    return result


def center(source: RationalMap, zero: FormalLag) -> RationalMap:
    result = dict(source)
    result[zero] = result.get(zero, Fraction(0)) - sum(
        result.values(), Fraction(0)
    )
    return {lag: coefficient for lag, coefficient in result.items() if coefficient}


def float_map_tv_norm(source: dict[FormalLag, complex]) -> Fraction:
    total = Fraction(0)
    for coefficient in source.values():
        if coefficient.imag != 0.0:
            raise AssertionError("fixed symmetric model must remain real")
        total += abs(Fraction.from_float(float(coefficient.real)))
    return total


def gamma_bound(operation_count: int) -> Fraction:
    """Standard gamma_n bound, with a factor already chosen by the caller."""
    if operation_count < 0 or operation_count * UNIT_ROUNDOFF >= 1:
        raise ValueError("invalid floating-operation count")
    return operation_count * UNIT_ROUNDOFF / (
        1 - operation_count * UNIT_ROUNDOFF
    )


def audited_float_convolution(
    left: dict[FormalLag, complex],
    left_error: Fraction,
    right: dict[FormalLag, complex],
    right_error: Fraction,
) -> tuple[dict[FormalLag, complex], Fraction]:
    """Float convolution plus an L1 forward-error bound.

    A target group element has at most min(|left|,|right|) representations.
    Four real operations per complex multiply/add are budgeted even though
    this frozen model is real.  Every pair is also allowed one full pruning
    tolerance and one minimum-subnormal absolute error.
    """
    output = convolve_frequency_maps(left, right)
    left_norm = float_map_tv_norm(left)
    right_norm = float_map_tv_norm(right)
    pairs = len(left) * len(right)
    maximum_bucket = min(len(left), len(right))
    local_error = (
        gamma_bound(4 * maximum_bucket) * left_norm * right_norm
        + pairs * PRUNING_ERROR
    )
    propagated = (
        right_norm * left_error
        + left_norm * right_error
        + left_error * right_error
    )
    return output, propagated + local_error


def audited_float_scale(
    source: dict[FormalLag, complex],
    source_error: Fraction,
    scalar: complex,
) -> tuple[dict[FormalLag, complex], Fraction]:
    if scalar.imag != 0.0:
        raise AssertionError("fixed response scalar must be real")
    scalar_absolute = abs(Fraction.from_float(float(scalar.real)))
    source_norm = float_map_tv_norm(source)
    output = scale_frequency_map(source, scalar)
    local_error = (
        gamma_bound(4) * scalar_absolute * source_norm
        + len(source) * PRUNING_ERROR
    )
    return output, scalar_absolute * source_error + local_error


def audited_float_sum(
    terms: tuple[tuple[dict[FormalLag, complex], Fraction], ...]
) -> tuple[dict[FormalLag, complex], Fraction]:
    if not terms:
        return {}, Fraction(0)
    output = add_frequency_maps(*(term[0] for term in terms))
    norm_sum = sum(
        (float_map_tv_norm(term[0]) for term in terms), Fraction(0)
    )
    term_count = sum(len(term[0]) for term in terms)
    local_error = (
        gamma_bound(4 * len(terms)) * norm_sum
        + term_count * PRUNING_ERROR
    )
    return output, sum((term[1] for term in terms), Fraction(0)) + local_error


def audited_centered_component(
    component: dict[FormalLag, complex], zero: FormalLag
) -> tuple[dict[FormalLag, complex], Fraction]:
    float_mass = sum(component.values())
    if float_mass.imag != 0.0:
        raise AssertionError("fixed component mass must be real")
    exact_mass = sum(
        (Fraction.from_float(float(value.real)) for value in component.values()),
        Fraction(0),
    )
    mass_error = abs(
        Fraction.from_float(float(float_mass.real)) - exact_mass
    )
    return audited_float_sum(
        (
            (component, Fraction(0)),
            ({zero: -float_mass}, mass_error),
        )
    )


def main() -> None:
    if not (
        sys.float_info.radix == 2
        and sys.float_info.mant_dig == 53
        and sys.float_info.max_exp == 1024
        and sys.float_info.min_exp == -1021
        and sys.float_info.rounds == 1
    ):
        raise RuntimeError("B1f audit requires round-to-nearest IEEE binary64")
    audit = soft_zeta_orbit_audit(
        scale=8.0, integer_cutoff=10, lag_cells=4, degree=2
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

    prime_powers = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3))
    prime_intervals = tuple(
        prime_weight_interval(integer, prime)
        for integer, prime in prime_powers
    )
    surrogate_prime_weights: list[Fraction] = []
    for integer, _ in prime_powers:
        lag = FormalLag.prime(integer, dimension)
        surrogate_prime_weights.append(
            2 * Fraction.from_float(float(formal["prime_map"][lag].real))
        )
    prime_error = sum(
        (
            interval.distance_upper(surrogate)
            for interval, surrogate in zip(
                prime_intervals, surrogate_prime_weights
            )
        ),
        Fraction(0),
    )
    prime_mass = interval_sum(prime_intervals)

    lag_start = Fraction(3, 100)
    lag_end = Fraction(2)
    lag_width = (lag_end - lag_start) / 4
    edges = tuple(lag_start + index * lag_width for index in range(5))
    continuum_intervals = (continuum_mass_interval(Fraction(0), lag_start),) + tuple(
        continuum_mass_interval(edges[index], edges[index + 1])
        for index in range(4)
    )
    surrogate_continuum_masses = [
        -Fraction.from_float(float(formal["continuum_map"][zero].real))
    ]
    for index in range(4):
        lag = FormalLag.continuum_basis(index, dimension)
        surrogate_continuum_masses.append(
            -2 * Fraction.from_float(
                float(formal["continuum_map"][lag].real)
            )
        )
    continuum_error = sum(
        (
            interval.distance_upper(surrogate)
            for interval, surrogate in zip(
                continuum_intervals, surrogate_continuum_masses
            )
        ),
        Fraction(0),
    )
    continuum_mass = interval_sum(continuum_intervals)

    exact_symbol_norm = prime_mass.add(continuum_mass)
    exact_total_mass = prime_mass.subtract(continuum_mass)
    symbol_error = prime_error + continuum_error
    prime_map = rationalize_map(formal["prime_map"])
    continuum_map = rationalize_map(formal["continuum_map"])
    symbol_map = dict(prime_map)
    add_scaled(symbol_map, continuum_map, Fraction(1))
    surrogate_symbol_norm = sum(
        (abs(value) for value in symbol_map.values()), Fraction(0)
    )
    symbol_norm_upper = max(exact_symbol_norm.upper, surrogate_symbol_norm)

    kappa = rational_square_root_interval(Fraction(3)).multiply(
        point(Fraction(1, 2))
    )
    level = kappa.multiply(exact_symbol_norm)
    amplitude = kappa.divide(kappa.add(point(Fraction(1, 3))))
    scalar = amplitude.square().multiply(point(Fraction(-4, 9))).divide(
        exact_symbol_norm.square().square()
    )
    difference = exact_total_mass.subtract(level)
    coefficient_intervals = (
        exact_total_mass.square().multiply(difference.square()),
        exact_total_mass.multiply(difference.square()),
        difference.square(),
        exact_total_mass.subtract(level.scale_integer(2)),
        point(1),
    )

    surrogate_total_mass = complex(spectral["total_mass"])
    surrogate_level = float(spectral["level"])
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
        interval.abs_upper() for interval in coefficient_intervals
    )
    coefficient_error_uppers = tuple(
        interval.distance_upper(surrogate)
        for interval, surrogate in zip(
            coefficient_intervals, surrogate_coefficients
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
    surrogate_scalar = Fraction.from_float(
        float(complex(spectral["response_scalar"]).real)
    )
    scalar_error = scalar.distance_upper(surrogate_scalar)

    print(
        "prime_base_tv_error_upper=",
        rational_decimal_upper(prime_error, 30),
        sep="",
        flush=True,
    )
    print(
        "continuum_base_tv_error_upper=",
        rational_decimal_upper(continuum_error, 30),
        sep="",
        flush=True,
    )
    print(
        "symbol_tv_error_upper=",
        rational_decimal_upper(symbol_error, 30),
        sep="",
        flush=True,
    )
    print(
        "polynomial_tv_error_upper=",
        rational_decimal_upper(polynomial_error, 30),
        sep="",
        flush=True,
    )
    print(
        "scalar_error_upper=",
        rational_decimal_upper(scalar_error, 30),
        sep="",
        flush=True,
    )
    identity = {zero: 1.0 + 0.0j}
    audited_powers: dict[
        int, tuple[dict[FormalLag, complex], Fraction]
    ] = {0: (identity, Fraction(0))}
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

    channel_data = {}
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
            complex(spectral["response_scalar"]),
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
        centered_error = centered_component_tv_error_upper_bound(base_error)
        exact_centered_norm_upper = 2 * base_norm_upper
        surrogate_centered_norm = sum(
            (abs(value) for value in surrogate_centered.values()), Fraction(0)
        )
        intended_to_ideal = (
            scalar_error * exact_centered_norm_upper * polynomial_norm_upper
            + abs(surrogate_scalar)
            * centered_error
            * polynomial_norm_upper
            + abs(surrogate_scalar)
            * surrogate_centered_norm
            * polynomial_error
        )
        response_error = intended_to_ideal + expansion_error
        channel_data[label] = {
            "base_error": base_error,
            "polynomial_error": polynomial_error,
            "scalar_error": scalar_error,
            "expansion_error": expansion_error,
            "response_mass_residual": response_mass_residual,
            "response_error": response_error,
        }

    if rational_exp_point_interval(Fraction(3)).lower <= 10:
        raise AssertionError("failed to certify log(10) < 3")
    support_length_upper = Fraction(30)
    tau = Fraction(1, 100)
    denominator_upper = Fraction(0)
    for label in ("prime", "continuum"):
        denominator_upper += brownian_tv_perturbation_upper_bound(
            FROZEN_B1E_SURROGATE_ENERGY_UPPERS[label],
            support_length_upper,
            channel_data[label]["response_error"],
            tau,
        )
    if denominator_upper > FROZEN_B1F_INTENDED_DENOMINATOR_UPPER:
        raise AssertionError("frozen intended denominator upper is too small")

    for label in ("prime", "continuum"):
        print(
            f"{label}_expansion_tv_error_upper=",
            rational_decimal_upper(channel_data[label]["expansion_error"], 30),
            sep="",
        )
        print(
            f"{label}_response_tv_error_upper=",
            rational_decimal_upper(channel_data[label]["response_error"], 30),
            sep="",
        )
    print(
        "intended_denominator_upper=",
        rational_decimal_upper(denominator_upper, 30),
        sep="",
    )
    print("B1f base-coefficient/denominator interval audit passed")
    print("[scope] one finite denominator only; numerator and asymptotics open")


if __name__ == "__main__":
    main()

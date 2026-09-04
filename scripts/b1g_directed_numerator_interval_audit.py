"""Directed rational numerator certificate for the frozen B1g model.

This audits every positive-frequency cell for (Y,N,J,h)=(8,10,4,1/200)
up to frequency 256.  All transcendental enclosures have rational endpoints:
Machin's identity encloses pi, Taylor remainders enclose cosine, and a common
decimal fixed-point grid performs outward interval arithmetic.  The result is
one finite numerator certificate only; it is not a scale-uniform estimate and
makes no RH claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import factorial

from b1f_base_coefficient_interval_audit import (
    FROZEN_B1F_INTENDED_DENOMINATOR_UPPER,
    continuum_mass_interval,
    interval_sum,
    point,
    prime_weight_interval,
)
from brownian_interval_certificate import (
    RationalInterval,
    rational_decimal_lower,
    rational_log_interval,
    rational_square_root_interval,
)


DECIMAL_PLACES = 60
FIXED_SCALE = 10**DECIMAL_PLACES
FREQUENCY_STEP = Fraction(1, 200)
FREQUENCY_CUTOFF = Fraction(256)
SAMPLE_COUNT = int(FREQUENCY_CUTOFF / FREQUENCY_STEP)
CELL_RADIUS = FREQUENCY_STEP / 2
RATIO_LOWER = Fraction(1, 4)
RATIO_UPPER = Fraction(4)
COSINE_ORDER = 22
TARGET_NUMERATOR_LOWER = FROZEN_B1F_INTENDED_DENOMINATOR_UPPER / 10
FROZEN_VERIFIED_CELL_COUNT = 12785
FROZEN_VERIFIED_INDEX_SHA256 = (
    "d781244d33bbec81edb8ba786eb28f035465883981b5abde178c3da5d3cabb9b"
)
FROZEN_VERIFIED_BOUND_SHA256 = (
    "4237a9a77ce37542db43f680374d3fdba8f778e68f91070b519adc3e2e134a10"
)
FROZEN_B1G_NUMERATOR_LOWER = Fraction(
    "0.000140734590642330727559468708"
)


def floor_fraction(value: Fraction, scale: int = FIXED_SCALE) -> int:
    value = Fraction(value)
    return value.numerator * scale // value.denominator


def ceiling_fraction(value: Fraction, scale: int = FIXED_SCALE) -> int:
    value = Fraction(value)
    return -((-value.numerator * scale) // value.denominator)


@dataclass(frozen=True)
class FixedInterval:
    """Closed interval with endpoints on the grid FIXED_SCALE^(-1)."""

    lower: int
    upper: int

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("fixed interval endpoints are reversed")

    @classmethod
    def from_rational_interval(cls, value: RationalInterval) -> "FixedInterval":
        return cls(
            floor_fraction(value.lower),
            ceiling_fraction(value.upper),
        )

    @classmethod
    def from_fraction(cls, value: Fraction | int) -> "FixedInterval":
        value = Fraction(value)
        return cls(floor_fraction(value), ceiling_fraction(value))

    def add(self, other: "FixedInterval") -> "FixedInterval":
        return FixedInterval(self.lower + other.lower, self.upper + other.upper)

    def negate(self) -> "FixedInterval":
        return FixedInterval(-self.upper, -self.lower)

    def subtract(self, other: "FixedInterval") -> "FixedInterval":
        return self.add(other.negate())

    def multiply(self, other: "FixedInterval") -> "FixedInterval":
        products = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return FixedInterval(
            min(products) // FIXED_SCALE,
            -((-max(products)) // FIXED_SCALE),
        )

    def scale_fraction(self, scalar: Fraction | int) -> "FixedInterval":
        scalar = Fraction(scalar)
        if scalar < 0:
            return self.negate().scale_fraction(-scalar)
        lower_numerator = self.lower * scalar.numerator
        upper_numerator = self.upper * scalar.numerator
        return FixedInterval(
            lower_numerator // scalar.denominator,
            -((-upper_numerator) // scalar.denominator),
        )

    def square(self) -> "FixedInterval":
        if self.lower <= 0 <= self.upper:
            lower_product = 0
        else:
            lower_product = min(self.lower**2, self.upper**2)
        upper_product = max(self.lower**2, self.upper**2)
        return FixedInterval(
            lower_product // FIXED_SCALE,
            -((-upper_product) // FIXED_SCALE),
        )

    def abs_lower(self) -> int:
        if self.lower <= 0 <= self.upper:
            return 0
        return min(abs(self.lower), abs(self.upper))

    def abs_upper(self) -> int:
        return max(abs(self.lower), abs(self.upper))

    def intersect(self, lower: int, upper: int) -> "FixedInterval":
        result = FixedInterval(max(self.lower, lower), min(self.upper, upper))
        return result


def atan_reciprocal_interval(denominator: int, terms: int = 90) -> RationalInterval:
    """Enclose atan(1/denominator) by its alternating rational series."""
    if denominator < 2 or terms < 1:
        raise ValueError("atan denominator and term count are too small")
    x = Fraction(1, denominator)
    partial = Fraction(0)
    for index in range(terms):
        term = x ** (2 * index + 1) / (2 * index + 1)
        partial += term if index % 2 == 0 else -term
    remainder = x ** (2 * terms + 1) / (2 * terms + 1)
    if terms % 2 == 0:
        return RationalInterval(partial, partial + remainder)
    return RationalInterval(partial - remainder, partial)


def rational_pi_interval() -> RationalInterval:
    """Machin enclosure pi=16 atan(1/5)-4 atan(1/239)."""
    return atan_reciprocal_interval(5).scale_integer(16).subtract(
        atan_reciprocal_interval(239).scale_integer(4)
    )


PI_RATIONAL = rational_pi_interval()
PI_FIXED = FixedInterval.from_rational_interval(PI_RATIONAL)
TWO_PI_FIXED = PI_FIXED.scale_fraction(2)


def nearest_integer(value: Fraction) -> int:
    """Round a nonnegative rational to the nearest integer, ties upward."""
    if value < 0:
        raise ValueError("nearest_integer expects a nonnegative value")
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)


COSINE_COEFFICIENTS = tuple(
    FixedInterval.from_fraction(Fraction((-1) ** degree, factorial(2 * degree)))
    for degree in range(COSINE_ORDER + 1)
)
COSINE_REMAINDER_UPPER = FixedInterval.from_fraction(
    Fraction(22, 7) ** (2 * COSINE_ORDER + 2)
    / factorial(2 * COSINE_ORDER + 2)
).upper


def rational_cosine_fixed(interval: RationalInterval) -> FixedInterval:
    """Enclose cos on a narrow rational interval by range reduction/Taylor."""
    source = FixedInterval.from_rational_interval(interval)
    midpoint = (interval.lower + interval.upper) / 2
    two_pi_midpoint = PI_RATIONAL.lower + PI_RATIONAL.upper
    turns = nearest_integer(midpoint / two_pi_midpoint)
    reduced = source.subtract(TWO_PI_FIXED.scale_fraction(turns))
    if 7 * reduced.abs_upper() > 22 * FIXED_SCALE:
        raise AssertionError("cosine range reduction escaped [-22/7,22/7]")
    squared = reduced.square()
    value = COSINE_COEFFICIENTS[-1]
    for coefficient in reversed(COSINE_COEFFICIENTS[:-1]):
        value = value.multiply(squared).add(coefficient)
    value = FixedInterval(
        value.lower - COSINE_REMAINDER_UPPER,
        value.upper + COSINE_REMAINDER_UPPER,
    )
    return value.intersect(-FIXED_SCALE, FIXED_SCALE)


def fixed_polynomial(
    argument: FixedInterval,
    coefficients: tuple[FixedInterval, ...],
) -> FixedInterval:
    value = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        value = value.multiply(argument).add(coefficient)
    return value


def multiply_lower(left: int, right: int) -> int:
    if left < 0 or right < 0:
        raise ValueError("lower product factors must be nonnegative")
    return left * right // FIXED_SCALE


def decimal_lower_from_fixed(value: int, places: int = 30) -> str:
    return rational_decimal_lower(Fraction(value, FIXED_SCALE), places)


def directed_numerator_certificate() -> dict[str, object]:
    if not (
        Fraction(333, 106)
        < PI_RATIONAL.lower
        < PI_RATIONAL.upper
        < Fraction(355, 113)
    ):
        raise AssertionError("Machin interval failed a rational pi cross-check")

    prime_powers = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3))
    prime_weights = tuple(
        prime_weight_interval(integer, prime)
        for integer, prime in prime_powers
    )
    prime_lags = tuple(
        rational_log_interval(Fraction(integer))
        for integer, _ in prime_powers
    )

    lag_start = Fraction(3, 100)
    lag_width = (Fraction(2) - lag_start) / 4
    edges = tuple(lag_start + index * lag_width for index in range(5))
    continuum_nodes = tuple(
        (edges[index] + edges[index + 1]) / 2 for index in range(4)
    )
    continuum_masses = (
        continuum_mass_interval(Fraction(0), lag_start),
    ) + tuple(
        continuum_mass_interval(edges[index], edges[index + 1])
        for index in range(4)
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
    coefficient_intervals = (
        total_mass.square().multiply(difference.square()),
        total_mass.multiply(difference.square()),
        difference.square(),
        total_mass.subtract(level.scale_integer(2)),
        point(1),
    )
    fixed_coefficients = tuple(
        FixedInterval.from_rational_interval(value)
        for value in coefficient_intervals
    )
    amplitude = kappa.divide(kappa.add(point(Fraction(1, 3))))
    scalar = amplitude.square().multiply(point(Fraction(-4, 9))).divide(
        symbol_norm.square().square()
    )
    scalar_square_lower = scalar.square().lower

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
    symbol_norm_upper = symbol_norm.upper
    difference_abs = difference.abs_upper()
    total_mass_abs = total_mass.abs_upper()
    cubic_abs = total_mass.subtract(level.scale_integer(2)).abs_upper()
    derivative_supremum = (
        4 * symbol_norm_upper**3
        + 3 * cubic_abs * symbol_norm_upper**2
        + 2 * difference_abs**2 * symbol_norm_upper
        + total_mass_abs * difference_abs**2
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
    prefactor_lower = floor_fraction(
        scalar_square_lower * FREQUENCY_STEP / PI_RATIONAL.upper
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
        contribution = multiply_lower(
            prefactor_lower,
            q_square_lower,
        )
        contribution = multiply_lower(
            contribution,
            wp_square_lower + wc_square_lower,
        )
        right_endpoint = (index + 1) * FREQUENCY_STEP
        reciprocal_square_lower = floor_fraction(1 / right_endpoint**2)
        contribution = multiply_lower(contribution, reciprocal_square_lower)
        numerator_lower += contribution
        verified_indices.append(index)
        verified_bounds.append((index, contribution))

    index_payload = (
        "B1g-v1|Y=8|N=10|J=4|h=1/200|cutoff=256|ratio=1/4,4|"
        + ",".join(str(index) for index in verified_indices)
    ).encode("ascii")
    bound_payload = (
        "B1g-v1|scale=10^60|"
        + ",".join(f"{index}:{bound}" for index, bound in verified_bounds)
    ).encode("ascii")
    index_hash = sha256(index_payload).hexdigest()
    bound_hash = sha256(bound_payload).hexdigest()
    numerator_fraction = Fraction(numerator_lower, FIXED_SCALE)
    ratio_lower = numerator_fraction / FROZEN_B1F_INTENDED_DENOMINATOR_UPPER
    if len(verified_indices) != FROZEN_VERIFIED_CELL_COUNT:
        raise AssertionError(
            f"frozen verified-cell count changed: {len(verified_indices)}"
        )
    if index_hash != FROZEN_VERIFIED_INDEX_SHA256:
        raise AssertionError(
            f"frozen verified-cell index hash changed: {index_hash}"
        )
    if bound_hash != FROZEN_VERIFIED_BOUND_SHA256:
        raise AssertionError(
            f"frozen verified-cell bound hash changed: {bound_hash}"
        )
    if numerator_fraction < FROZEN_B1G_NUMERATOR_LOWER:
        raise AssertionError("frozen B1g numerator lower is too large")
    if numerator_fraction <= TARGET_NUMERATOR_LOWER:
        raise AssertionError("directed numerator did not clear the 0.10 target")
    if ratio_lower <= Fraction(19, 100):
        raise AssertionError("directed finite ratio did not clear 0.19")

    print(f"fixed_decimal_places={DECIMAL_PLACES}")
    print(f"cosine_order={COSINE_ORDER}")
    print(f"sample_count={SAMPLE_COUNT - 1}")
    print(f"verified_cell_count={len(verified_indices)}")
    print(
        "verified_width_lower=",
        rational_decimal_lower(
            len(verified_indices) * FREQUENCY_STEP,
            12,
        ),
        sep="",
    )
    print(f"verified_index_sha256={index_hash}")
    print(f"verified_bound_sha256={bound_hash}")
    print(
        "numerator_lower=",
        decimal_lower_from_fixed(numerator_lower, 30),
        sep="",
    )
    print(
        "ratio_lower=",
        rational_decimal_lower(ratio_lower, 18),
        sep="",
    )
    print(
        "overlap_delta_lower=",
        rational_decimal_lower(Fraction(19, 425), 18),
        sep="",
    )
    print(
        "diagonal_to_full_lower=",
        rational_decimal_lower(Fraction(425, 387), 18),
        sep="",
    )
    print("B1g directed numerator interval audit passed")
    print("[scope] one finite ratio only; scale-uniform overlap and RH remain open")
    return {
        "verified_indices": tuple(verified_indices),
        "verified_bounds": tuple(verified_bounds),
        "index_hash": index_hash,
        "bound_hash": bound_hash,
        "numerator_lower": numerator_fraction,
        "ratio_lower": ratio_lower,
    }


def main() -> None:
    directed_numerator_certificate()


if __name__ == "__main__":
    main()

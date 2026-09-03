"""Exact rational helpers for finite Brownian denominator certificates.

This module deliberately separates support geometry from coefficient error.
It proves finite rational inequalities only; it does not certify any zeta
coefficient enclosure by itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Iterable

from formal_lag_response import FormalLag


FROZEN_B1E_SURROGATE_ENERGY_UPPERS = {
    "prime": Fraction("0.00055130411625587258"),
    "continuum": Fraction("0.00015289136767059444"),
}


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("interval endpoints are reversed")

    def add(self, other: "RationalInterval") -> "RationalInterval":
        return RationalInterval(
            self.lower + other.lower, self.upper + other.upper
        )

    def scale_integer(self, integer: int) -> "RationalInterval":
        if integer >= 0:
            return RationalInterval(
                integer * self.lower, integer * self.upper
            )
        return RationalInterval(
            integer * self.upper, integer * self.lower
        )

    def negate(self) -> "RationalInterval":
        return RationalInterval(-self.upper, -self.lower)

    def subtract(self, other: "RationalInterval") -> "RationalInterval":
        return self.add(other.negate())

    def multiply(self, other: "RationalInterval") -> "RationalInterval":
        products = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return RationalInterval(min(products), max(products))

    def reciprocal(self) -> "RationalInterval":
        if self.lower <= 0 <= self.upper:
            raise ZeroDivisionError("interval contains zero")
        endpoints = (1 / self.lower, 1 / self.upper)
        return RationalInterval(min(endpoints), max(endpoints))

    def divide(self, other: "RationalInterval") -> "RationalInterval":
        return self.multiply(other.reciprocal())

    def square(self) -> "RationalInterval":
        upper = max(self.lower * self.lower, self.upper * self.upper)
        lower = (
            Fraction(0)
            if self.lower <= 0 <= self.upper
            else min(self.lower * self.lower, self.upper * self.upper)
        )
        return RationalInterval(lower, upper)

    def abs_upper(self) -> Fraction:
        return max(abs(self.lower), abs(self.upper))

    def distance_upper(self, point: Fraction) -> Fraction:
        point = Fraction(point)
        return max(abs(self.lower - point), abs(self.upper - point))


def _format_scaled_integer(integer: int, decimal_places: int) -> str:
    sign = "-" if integer < 0 else ""
    digits = str(abs(integer)).rjust(decimal_places + 1, "0")
    if decimal_places == 0:
        return sign + digits
    return sign + digits[:-decimal_places] + "." + digits[-decimal_places:]


def rational_decimal_lower(value: Fraction, decimal_places: int) -> str:
    """Format a rational with certified downward decimal rounding."""
    if decimal_places < 0:
        raise ValueError("decimal_places must be nonnegative")
    value = Fraction(value)
    scale = 10**decimal_places
    scaled_floor = value.numerator * scale // value.denominator
    return _format_scaled_integer(scaled_floor, decimal_places)


def rational_decimal_upper(value: Fraction, decimal_places: int) -> str:
    """Format a rational with certified upward decimal rounding."""
    if decimal_places < 0:
        raise ValueError("decimal_places must be nonnegative")
    value = Fraction(value)
    scale = 10**decimal_places
    scaled_ceiling = -((-value.numerator * scale) // value.denominator)
    return _format_scaled_integer(scaled_ceiling, decimal_places)


def rational_square_root_interval(
    value: Fraction, decimal_places: int = 80
) -> RationalInterval:
    """Enclose a nonnegative rational square root by integer arithmetic."""
    value = Fraction(value)
    if value < 0 or decimal_places < 0:
        raise ValueError("value and decimal_places must be nonnegative")
    scale = 10**decimal_places
    scaled_square_floor = value.numerator * scale**2 // value.denominator
    lower_integer = isqrt(scaled_square_floor)
    lower = Fraction(lower_integer, scale)
    if lower * lower == value:
        return RationalInterval(lower, lower)
    return RationalInterval(lower, Fraction(lower_integer + 1, scale))


def rational_exp_point_interval(
    value: Fraction, terms: int = 24
) -> RationalInterval:
    """Enclose exp(value) by a rational Taylor sum and geometric tail."""
    value = Fraction(value)
    if terms < 1:
        raise ValueError("terms must be positive")
    if value < 0:
        positive = rational_exp_point_interval(-value, terms)
        return positive.reciprocal()
    if value >= terms + 2:
        raise ValueError("increase terms so the geometric tail converges")
    term = Fraction(1)
    partial = Fraction(1)
    for degree in range(1, terms + 1):
        term = term * value / degree
        partial += term
    next_term = term * value / (terms + 1)
    remainder = next_term / (1 - value / (terms + 2))
    return RationalInterval(partial, partial + remainder)


def rational_exp_interval(
    interval: RationalInterval, terms: int = 24
) -> RationalInterval:
    """Enclose exp on a rational interval using monotonicity."""
    lower = rational_exp_point_interval(interval.lower, terms).lower
    upper = rational_exp_point_interval(interval.upper, terms).upper
    return RationalInterval(lower, upper)


def _atanh_log_unit_interval(
    value: Fraction, terms: int
) -> RationalInterval:
    """Enclose log(value) for 1 <= value <= 2 by a rational series."""
    if not Fraction(1) <= value <= Fraction(2):
        raise ValueError("unit log reduction requires 1 <= value <= 2")
    if terms < 1:
        raise ValueError("terms must be positive")
    z = (value - 1) / (value + 1)
    z_squared = z * z
    power = z
    partial = Fraction(0)
    for index in range(terms):
        partial += 2 * power / (2 * index + 1)
        power *= z_squared
    remainder = (
        2 * power / ((2 * terms + 1) * (1 - z_squared))
        if z
        else Fraction(0)
    )
    return RationalInterval(partial, partial + remainder)


def rational_log_interval(
    value: Fraction, terms: int = 96
) -> RationalInterval:
    """Return a rigorous rational enclosure of log(value), value > 0.

    Powers of two reduce the argument to [1,2].  On that interval the
    atanh series has nonnegative terms and an elementary geometric tail.
    """
    value = Fraction(value)
    if value <= 0:
        raise ValueError("logarithm argument must be positive")
    reduced = value
    exponent = 0
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    reduced_log = _atanh_log_unit_interval(reduced, terms)
    log_two = _atanh_log_unit_interval(Fraction(2), terms)
    return reduced_log.add(log_two.scale_integer(exponent))


def smooth_rational_log_interval(
    value: Fraction,
    primes: tuple[int, ...],
    terms: int = 96,
) -> RationalInterval:
    """Enclose log(value) from a supplied smooth-prime factorization."""
    value = Fraction(value)
    if value <= 0:
        raise ValueError("logarithm argument must be positive")
    numerator = value.numerator
    denominator = value.denominator
    result = RationalInterval(Fraction(0), Fraction(0))
    for prime in primes:
        if prime < 2:
            raise ValueError("smooth factors must be primes at least two")
        exponent = 0
        while numerator % prime == 0:
            numerator //= prime
            exponent += 1
        while denominator % prime == 0:
            denominator //= prime
            exponent -= 1
        if exponent:
            result = result.add(
                rational_log_interval(Fraction(prime), terms).scale_integer(
                    exponent
                )
            )
    if numerator != 1 or denominator != 1:
        raise ValueError("rational is not smooth over the supplied primes")
    return result


def canonical_rational_grid_key(
    lag: FormalLag, rational_nodes: tuple[Fraction, ...]
) -> tuple[Fraction, Fraction]:
    """Quotient a formal lag by all exact rational grid relations."""
    if len(lag.continuum) != len(rational_nodes):
        raise ValueError("lag and rational grid have incompatible dimensions")
    shift = sum(
        (
            multiplicity * node
            for multiplicity, node in zip(lag.continuum, rational_nodes)
        ),
        Fraction(0),
    )
    return lag.ratio, shift


def canonical_position_interval(
    key: tuple[Fraction, Fraction],
    terms: int = 96,
    smooth_primes: tuple[int, ...] | None = None,
) -> RationalInterval:
    """Enclose log(ratio)+shift for a canonical rational-grid key."""
    ratio, shift = key
    logarithm = (
        smooth_rational_log_interval(ratio, smooth_primes, terms)
        if smooth_primes is not None
        else rational_log_interval(ratio, terms)
    )
    return RationalInterval(
        logarithm.lower + shift, logarithm.upper + shift
    )


def brownian_cluster_energy_upper_bound(
    atoms: Iterable[tuple[Fraction, Fraction, Fraction]],
) -> dict[str, Fraction | int]:
    """Bound primitive L2 energy without ordering overlapping intervals.

    Each atom is ``(position_lower, position_upper, coefficient)``.  The
    coefficients must have exact total zero.  Overlapping position intervals
    are merged transitively.  Inside a cluster, every possible primitive is
    bounded by incoming absolute mass plus cluster total variation; between
    clusters the primitive is the exact cumulative cluster mass.
    """
    ordered = sorted(
        (
            (Fraction(lower), Fraction(upper), Fraction(coefficient))
            for lower, upper, coefficient in atoms
        ),
        key=lambda atom: (atom[0], atom[1]),
    )
    if not ordered:
        return {
            "energy_upper": Fraction(0),
            "support_length_upper": Fraction(0),
            "cluster_count": 0,
            "maximum_cluster_size": 0,
        }
    for lower, upper, _ in ordered:
        if lower > upper:
            raise ValueError("atom position interval is reversed")
    if sum((coefficient for _, _, coefficient in ordered), Fraction(0)):
        raise ValueError("Brownian primitive measure must have exact mass zero")

    clusters: list[list[tuple[Fraction, Fraction, Fraction]]] = []
    current = [ordered[0]]
    current_upper = ordered[0][1]
    for atom in ordered[1:]:
        if atom[0] <= current_upper:
            current.append(atom)
            current_upper = max(current_upper, atom[1])
        else:
            clusters.append(current)
            current = [atom]
            current_upper = atom[1]
    clusters.append(current)

    energy_upper = Fraction(0)
    cumulative = Fraction(0)
    for index, cluster in enumerate(clusters):
        cluster_lower = min(atom[0] for atom in cluster)
        cluster_upper = max(atom[1] for atom in cluster)
        variation = sum(
            (abs(atom[2]) for atom in cluster), Fraction(0)
        )
        energy_upper += (cluster_upper - cluster_lower) * (
            abs(cumulative) + variation
        ) ** 2
        cumulative += sum(
            (atom[2] for atom in cluster), Fraction(0)
        )
        if index + 1 < len(clusters):
            next_lower = min(atom[0] for atom in clusters[index + 1])
            energy_upper += (next_lower - cluster_upper) * abs(cumulative) ** 2
    if cumulative:
        raise AssertionError("internal mass accounting failed")
    return {
        "energy_upper": energy_upper,
        "support_length_upper": (
            max(atom[1] for atom in ordered)
            - min(atom[0] for atom in ordered)
        ),
        "cluster_count": len(clusters),
        "maximum_cluster_size": max(len(cluster) for cluster in clusters),
    }


def brownian_tv_perturbation_upper_bound(
    approximate_energy_upper: Fraction,
    support_length_upper: Fraction,
    total_variation_error_upper: Fraction,
    tau: Fraction = Fraction(1, 100),
) -> Fraction:
    """Rational Young bound for a centered-measure TV perturbation."""
    approximate_energy_upper = Fraction(approximate_energy_upper)
    support_length_upper = Fraction(support_length_upper)
    total_variation_error_upper = Fraction(total_variation_error_upper)
    tau = Fraction(tau)
    if (
        approximate_energy_upper < 0
        or support_length_upper < 0
        or total_variation_error_upper < 0
        or tau <= 0
    ):
        raise ValueError("energy, length, error and tau must be nonnegative")
    return (
        (1 + tau) * approximate_energy_upper
        + (1 + 1 / tau)
        * support_length_upper
        * total_variation_error_upper**2
    )


def polynomial_convolution_tv_error_upper_bound(
    measure_norm_upper: Fraction,
    measure_tv_error_upper: Fraction,
    coefficient_abs_uppers: tuple[Fraction, ...],
    coefficient_error_uppers: tuple[Fraction, ...],
) -> Fraction:
    """Banach-algebra error for Q(mu) versus Q_tilde(mu_tilde).

    Both measure norms are assumed at most ``measure_norm_upper``.  Entry k
    bounds the exact coefficient |a_k| and |a_k-a_tilde_k| respectively.
    """
    measure_norm_upper = Fraction(measure_norm_upper)
    measure_tv_error_upper = Fraction(measure_tv_error_upper)
    absolute = tuple(Fraction(value) for value in coefficient_abs_uppers)
    errors = tuple(Fraction(value) for value in coefficient_error_uppers)
    if len(absolute) != len(errors) or not absolute:
        raise ValueError("coefficient ledgers must have equal positive length")
    if (
        measure_norm_upper < 0
        or measure_tv_error_upper < 0
        or any(value < 0 for value in absolute + errors)
    ):
        raise ValueError("all norm and error bounds must be nonnegative")
    input_error = sum(
        (
            degree
            * absolute[degree]
            * measure_norm_upper ** (degree - 1)
            * measure_tv_error_upper
            for degree in range(1, len(absolute))
        ),
        Fraction(0),
    )
    coefficient_error = sum(
        (
            errors[degree] * measure_norm_upper**degree
            for degree in range(len(errors))
        ),
        Fraction(0),
    )
    return input_error + coefficient_error


def centered_component_tv_error_upper_bound(
    component_tv_error_upper: Fraction,
) -> Fraction:
    """Centering at zero costs at most twice the component TV error."""
    component_tv_error_upper = Fraction(component_tv_error_upper)
    if component_tv_error_upper < 0:
        raise ValueError("component error must be nonnegative")
    return 2 * component_tv_error_upper

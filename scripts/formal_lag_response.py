"""Formal product/continuum lags for finite Chebyshev orbit audits.

Integer logarithms are represented by exact rational products.  Continuum
quadrature nodes are represented by independent formal basis coordinates.
Numerical lag values are used only after exact formal cancellation has been
decided.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math

import numpy as np


@dataclass(frozen=True)
class FormalLag:
    ratio: Fraction
    continuum: tuple[int, ...]

    @classmethod
    def zero(cls, continuum_dimension: int) -> "FormalLag":
        return cls(Fraction(1, 1), (0,) * continuum_dimension)

    @classmethod
    def prime(cls, integer: int, continuum_dimension: int) -> "FormalLag":
        if integer < 1:
            raise ValueError("integer product must be positive")
        return cls(Fraction(integer, 1), (0,) * continuum_dimension)

    @classmethod
    def continuum_basis(
        cls, index: int, continuum_dimension: int
    ) -> "FormalLag":
        coordinates = [0] * continuum_dimension
        coordinates[index] = 1
        return cls(Fraction(1, 1), tuple(coordinates))

    def __add__(self, other: "FormalLag") -> "FormalLag":
        if len(self.continuum) != len(other.continuum):
            raise ValueError("formal lags have incompatible continuum dimensions")
        return FormalLag(
            self.ratio * other.ratio,
            tuple(left + right for left, right in zip(self.continuum, other.continuum)),
        )

    def __neg__(self) -> "FormalLag":
        return FormalLag(
            1 / self.ratio,
            tuple(-coordinate for coordinate in self.continuum),
        )

    def __sub__(self, other: "FormalLag") -> "FormalLag":
        return self + (-other)

    def is_zero(self) -> bool:
        return self.ratio == 1 and not any(self.continuum)

    def numerical_value(self, continuum_nodes: tuple[float, ...]) -> float:
        if len(self.continuum) != len(continuum_nodes):
            raise ValueError("continuum node list has incompatible dimension")
        return (
            math.log(self.ratio.numerator)
            - math.log(self.ratio.denominator)
            + sum(
                coefficient * node
                for coefficient, node in zip(self.continuum, continuum_nodes)
            )
        )


FrequencyMap = dict[FormalLag, complex]


def _big_omega(integer: int) -> int:
    """Return the number of prime factors with multiplicity."""
    if integer < 1:
        raise ValueError("integer must be positive")
    remaining = integer
    factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            remaining //= divisor
            factors += 1
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors += 1
    return factors


def formal_lag_parity(lag: FormalLag) -> int:
    """The product/continuum character chi:G->{-1,+1}."""
    exponent = (
        _big_omega(lag.ratio.numerator)
        + _big_omega(lag.ratio.denominator)
        + sum(lag.continuum)
    )
    return -1 if exponent % 2 else 1


def split_frequency_map_by_parity(
    source: FrequencyMap,
) -> tuple[FrequencyMap, FrequencyMap]:
    """Return chi=-1 odd support and chi=+1 parity breakers."""
    odd: FrequencyMap = {}
    breakers: FrequencyMap = {}
    for lag, coefficient in source.items():
        target = odd if formal_lag_parity(lag) == -1 else breakers
        target[lag] = coefficient
    return odd, breakers


def add_frequency_term(
    target: FrequencyMap, lag: FormalLag, coefficient: complex, tolerance: float = 1.0e-14
) -> None:
    value = target.get(lag, 0.0 + 0.0j) + complex(coefficient)
    if abs(value) <= tolerance:
        target.pop(lag, None)
    else:
        target[lag] = value


def add_frequency_maps(*maps: FrequencyMap) -> FrequencyMap:
    result: FrequencyMap = {}
    for source in maps:
        for lag, coefficient in source.items():
            add_frequency_term(result, lag, coefficient)
    return result


def scale_frequency_map(source: FrequencyMap, scalar: complex) -> FrequencyMap:
    return {
        lag: scalar * coefficient
        for lag, coefficient in source.items()
        if abs(scalar * coefficient) > 1.0e-14
    }


def convolve_frequency_maps(left: FrequencyMap, right: FrequencyMap) -> FrequencyMap:
    result: FrequencyMap = {}
    for left_lag, left_coefficient in left.items():
        for right_lag, right_coefficient in right.items():
            add_frequency_term(
                result,
                left_lag + right_lag,
                left_coefficient * right_coefficient,
            )
    return result


def convolution_power(source: FrequencyMap, power: int) -> FrequencyMap:
    """Return a finite formal convolution power."""
    if power < 0:
        raise ValueError("power must be nonnegative")
    if not source:
        return {} if power else {FormalLag.zero(0): 1.0 + 0.0j}
    dimension = len(next(iter(source)).continuum)
    result: FrequencyMap = {FormalLag.zero(dimension): 1.0 + 0.0j}
    for _ in range(power):
        result = convolve_frequency_maps(result, source)
    return result


def exact_formal_moment(source: FrequencyMap, power: int) -> complex:
    """Return the identity coefficient of a formal convolution power."""
    if not source:
        return 1.0 + 0.0j if power == 0 else 0.0 + 0.0j
    dimension = len(next(iter(source)).continuum)
    return convolution_power(source, power).get(
        FormalLag.zero(dimension), 0.0 + 0.0j
    )


def frequency_l2_norm(source: FrequencyMap) -> float:
    return math.sqrt(sum(abs(value) ** 2 for value in source.values()))


def parity_breaker_odd_moment_l2_bound(
    source: FrequencyMap, power: int
) -> float:
    """Telescoping convolution-L2 bound for an odd exact moment."""
    if power < 1 or power % 2 == 0:
        raise ValueError("power must be a positive odd integer")
    odd, breakers = split_frequency_map_by_parity(source)
    if not source:
        return 0.0
    dimension = len(next(iter(source)).continuum)
    identity = {FormalLag.zero(dimension): 1.0 + 0.0j}
    source_powers = [identity]
    odd_powers = [identity]
    for _ in range(power - 1):
        source_powers.append(
            convolve_frequency_maps(source_powers[-1], source)
        )
        odd_powers.append(
            convolve_frequency_maps(odd_powers[-1], odd)
        )
    bound = 0.0
    for left_power in range(power):
        right = convolve_frequency_maps(
            breakers, odd_powers[power - 1 - left_power]
        )
        bound += (
            frequency_l2_norm(source_powers[left_power])
            * frequency_l2_norm(right)
        )
    return bound


def degree_two_parity_exact_ledger(
    symbol: FrequencyMap, spectral_bound: float, rho: float
) -> dict[str, float]:
    """Bound the degree-two exact response by parity-breaker mass."""
    if spectral_bound <= 0.0 or rho <= 0.0:
        raise ValueError("spectral bound and rho must be positive")
    odd, breakers = split_frequency_map_by_parity(symbol)
    odd_mass = sum(abs(value) for value in odd.values())
    breaker_mass = sum(abs(value) for value in breakers.values())
    symbol_l2_mass = frequency_l2_norm(symbol)
    breaker_l2_mass = frequency_l2_norm(breakers)
    total_mass = odd_mass + breaker_mass
    second_convolution = convolve_frequency_maps(symbol, symbol)
    exact_fourth_moment = sum(
        abs(value) ** 2 for value in second_convolution.values()
    )
    odd_third_bound = total_mass**3 - odd_mass**3
    odd_fifth_bound = total_mass**5 - odd_mass**5
    odd_third_l2_bound = parity_breaker_odd_moment_l2_bound(symbol, 3)
    odd_fifth_l2_bound = parity_breaker_odd_moment_l2_bound(symbol, 5)
    node = math.sqrt(3.0) / 2.0
    amplitude = node * spectral_bound / (node * spectral_bound + rho)
    polynomial_factor = 2.0 * amplitude / (3.0 * spectral_bound**2)
    exact_response_upper_bound = polynomial_factor**2 * (
        2.0 * node * spectral_bound * exact_fourth_moment
        + odd_fifth_bound
        + node**2 * spectral_bound**2 * odd_third_bound
    )
    exact_response_l2_upper_bound = polynomial_factor**2 * (
        2.0 * node * spectral_bound * exact_fourth_moment
        + odd_fifth_l2_bound
        + node**2 * spectral_bound**2 * odd_third_l2_bound
    )
    odd_third_norm_bound = (
        3.0 * breaker_l2_mass * symbol_l2_mass * total_mass
    )
    odd_fifth_norm_bound = (
        5.0 * breaker_l2_mass * symbol_l2_mass * total_mass**3
    )
    exact_response_norm_upper_bound = polynomial_factor**2 * (
        2.0
        * node
        * spectral_bound
        * total_mass**2
        * symbol_l2_mass**2
        + odd_fifth_norm_bound
        + node**2 * spectral_bound**2 * odd_third_norm_bound
    )
    return {
        "odd_l1_mass": odd_mass,
        "breaker_l1_mass": breaker_mass,
        "breaker_fraction": breaker_mass / total_mass if total_mass else 0.0,
        "symbol_l2_mass": symbol_l2_mass,
        "breaker_l2_mass": breaker_l2_mass,
        "exact_fourth_moment": exact_fourth_moment,
        "odd_third_moment_bound": odd_third_bound,
        "odd_fifth_moment_bound": odd_fifth_bound,
        "odd_third_moment_l2_bound": odd_third_l2_bound,
        "odd_fifth_moment_l2_bound": odd_fifth_l2_bound,
        "odd_third_moment_norm_bound": odd_third_norm_bound,
        "odd_fifth_moment_norm_bound": odd_fifth_norm_bound,
        "degree_two_polynomial_factor": polynomial_factor,
        "exact_response_upper_bound": exact_response_upper_bound,
        "exact_response_l2_upper_bound": exact_response_l2_upper_bound,
        "exact_response_norm_upper_bound": exact_response_norm_upper_bound,
    }


def degree_two_response_frequency_map(
    symbol: FrequencyMap, spectral_bound: float, rho: float
) -> FrequencyMap:
    """Return the signed frequency map of -P*p_2(P)^2.

    The degree-two interpolant is p_2(x)=c*x*(x-a*B), with
    a=sqrt(3)/2. Combining the response before applying a stationary kernel
    exposes its single shifted-moment factorization and avoids the much
    larger outer/effect/effect triple ledger.
    """
    if spectral_bound <= 0.0 or rho <= 0.0:
        raise ValueError("spectral bound and rho must be positive")
    if not symbol:
        raise ValueError("symbol must be nonempty")
    node = math.sqrt(3.0) / 2.0
    amplitude = node * spectral_bound / (node * spectral_bound + rho)
    polynomial_factor = 2.0 * amplitude / (3.0 * spectral_bound**2)
    dimension = len(next(iter(symbol)).continuum)
    third = convolution_power(symbol, 3)
    shifted = add_frequency_maps(
        symbol,
        {FormalLag.zero(dimension): -node * spectral_bound},
    )
    return scale_frequency_map(
        convolve_frequency_maps(
            third, convolve_frequency_maps(shifted, shifted)
        ),
        -(polynomial_factor**2),
    )


def centered_degree_two_volterra_coefficients(
    total_mass: complex, spectral_bound: float
) -> tuple[complex, ...]:
    """Coefficients of (M+z)^3*(M-a*B+z)^2 in ascending order."""
    if spectral_bound <= 0.0:
        raise ValueError("spectral bound must be positive")
    total_mass = complex(total_mass)
    shifted_mass = total_mass - math.sqrt(3.0) * spectral_bound / 2.0
    return (
        total_mass**3 * shifted_mass**2,
        2.0 * total_mass**3 * shifted_mass
        + 3.0 * total_mass**2 * shifted_mass**2,
        total_mass**3
        + 6.0 * total_mass**2 * shifted_mass
        + 3.0 * total_mass * shifted_mass**2,
        3.0 * total_mass**2
        + 6.0 * total_mass * shifted_mass
        + shifted_mass**2,
        3.0 * total_mass + 2.0 * shifted_mass,
        1.0 + 0.0j,
    )


def stationary_response_from_frequency_map(
    response: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    kernel,
) -> complex:
    """Evaluate a signed response map against a numerical lag kernel."""
    return sum(
        coefficient * kernel(lag.numerical_value(continuum_nodes))
        for lag, coefficient in response.items()
    )


def cauchy_gaussian_mixture_cdf(lag: float, upper_scale: float) -> float:
    """Cauchy Gaussian-mixture mass below upper_scale at one lag.

    For u>0 let mu_u be the normalized Gaussian with density
    sqrt(u/pi)*exp(-u*t^2). The normalized Cauchy state is the exact
    Gamma(1/2,1) mixture of these states. This function returns

        int_0^U exp(-u-lag^2/(4u)) du/sqrt(pi*u).

    Its limit as U tends to infinity is exp(-abs(lag)).
    """
    if upper_scale < 0.0:
        raise ValueError("upper scale must be nonnegative")
    absolute_lag = abs(float(lag))
    if upper_scale == 0.0:
        return 0.0
    if math.isinf(upper_scale):
        return math.exp(-absolute_lag)
    root = math.sqrt(upper_scale)
    first_argument = absolute_lag / (2.0 * root) - root
    second_argument = absolute_lag / (2.0 * root) + root
    return 0.5 * (
        math.exp(-absolute_lag) * math.erfc(first_argument)
        - math.exp(absolute_lag) * math.erfc(second_argument)
    )


def cauchy_gaussian_mixture_band_ledger(
    response: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    scale_edges: tuple[float, ...],
) -> dict[str, object]:
    """Split a Cauchy response into exact Gaussian-mixture scale bands."""
    if len(scale_edges) < 2:
        raise ValueError("at least two scale edges are required")
    if scale_edges[0] != 0.0 or not math.isinf(scale_edges[-1]):
        raise ValueError("scale edges must start at zero and end at infinity")
    if any(
        right <= left
        for left, right in zip(scale_edges, scale_edges[1:])
    ):
        raise ValueError("scale edges must be strictly increasing")
    signed: list[complex] = []
    variation: list[float] = []
    exact: list[complex] = []
    for left, right in zip(scale_edges, scale_edges[1:]):
        band_signed = 0.0 + 0.0j
        band_variation = 0.0
        band_exact = 0.0 + 0.0j
        for lag, coefficient in response.items():
            numerical_lag = lag.numerical_value(continuum_nodes)
            weight = (
                cauchy_gaussian_mixture_cdf(numerical_lag, right)
                - cauchy_gaussian_mixture_cdf(numerical_lag, left)
            )
            term = coefficient * weight
            band_signed += term
            band_variation += abs(coefficient) * weight
            if lag.is_zero():
                band_exact += term
        signed.append(band_signed)
        variation.append(band_variation)
        exact.append(band_exact)
    return {
        "scale_edges": scale_edges,
        "signed": signed,
        "variation": variation,
        "exact": exact,
        "nonexact": [
            value - diagonal for value, diagonal in zip(signed, exact)
        ],
        "total_response": sum(signed),
        "total_variation": sum(variation),
    }


def gaussian_heat_shell_ledger(
    response: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    gaussian_scale: float,
    heat_edges: tuple[float, ...] = (
        0.0,
        0.25,
        1.0,
        4.0,
        16.0,
        math.inf,
    ),
) -> dict[str, object]:
    """Split a Gaussian response by dimensionless heat distance.

    A nonzero lag ell is assigned the coordinate z=ell^2/(4u).  Both the
    signed unweighted shell mass and its exp(-z)-weighted response are kept,
    so cancellation is visible rather than replaced by a variation bound.
    """
    if gaussian_scale <= 0.0:
        raise ValueError("Gaussian scale must be positive")
    if len(heat_edges) < 2:
        raise ValueError("at least two heat edges are required")
    if heat_edges[0] != 0.0 or not math.isinf(heat_edges[-1]):
        raise ValueError("heat edges must start at zero and end at infinity")
    if any(
        right <= left for left, right in zip(heat_edges, heat_edges[1:])
    ):
        raise ValueError("heat edges must be strictly increasing")
    shell_count = len(heat_edges) - 1
    signed_unweighted = [0.0 + 0.0j] * shell_count
    signed_weighted = [0.0 + 0.0j] * shell_count
    weighted_variation = [0.0] * shell_count
    counts = [0] * shell_count
    exact_response = 0.0 + 0.0j
    for lag, coefficient in response.items():
        if lag.is_zero():
            exact_response += coefficient
            continue
        numerical_lag = lag.numerical_value(continuum_nodes)
        heat_distance = numerical_lag**2 / (4.0 * gaussian_scale)
        shell = next(
            index
            for index, (left, right) in enumerate(
                zip(heat_edges, heat_edges[1:])
            )
            if left <= heat_distance < right
        )
        weight = math.exp(-heat_distance)
        signed_unweighted[shell] += coefficient
        signed_weighted[shell] += coefficient * weight
        weighted_variation[shell] += abs(coefficient) * weight
        counts[shell] += 1
    total_response = exact_response + sum(signed_weighted)
    return {
        "gaussian_scale": gaussian_scale,
        "heat_edges": heat_edges,
        "exact_response": exact_response,
        "signed_unweighted": signed_unweighted,
        "signed_weighted": signed_weighted,
        "weighted_variation": weighted_variation,
        "counts": counts,
        "nonexact_response": sum(signed_weighted),
        "total_response": total_response,
    }


def gaussian_signed_layer_cake_ledger(
    response: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    gaussian_scale: float,
) -> dict[str, object]:
    """Exact signed cumulative-profile formula for a Gaussian response.

    If Q(h) is the sum of all nonexact response coefficients with numerical
    lag in (-h,h), then the nonexact Gaussian response equals

        integral_0^infinity exp(-z) Q(2*sqrt(u*z)) dz.

    The profile capacity integrates abs(Q) instead and is an upper bound that
    preserves all cancellation accumulated before each heat radius.
    """
    if gaussian_scale <= 0.0:
        raise ValueError("Gaussian scale must be positive")
    exact_response = 0.0 + 0.0j
    grouped: dict[float, complex] = {}
    coefficient_variation = 0.0
    for lag, coefficient in response.items():
        if lag.is_zero():
            exact_response += coefficient
            continue
        numerical_lag = lag.numerical_value(continuum_nodes)
        heat_distance = numerical_lag**2 / (4.0 * gaussian_scale)
        grouped[heat_distance] = (
            grouped.get(heat_distance, 0.0 + 0.0j) + coefficient
        )
        coefficient_variation += abs(coefficient) * math.exp(-heat_distance)
    distances = sorted(grouped)
    cumulative = 0.0 + 0.0j
    signed_integral = 0.0 + 0.0j
    profile_capacity = 0.0
    maximum_cumulative = 0.0
    segment_count = 0
    for index, distance in enumerate(distances):
        cumulative += grouped[distance]
        next_distance = (
            distances[index + 1]
            if index + 1 < len(distances)
            else math.inf
        )
        exponential_mass = math.exp(-distance) - (
            math.exp(-next_distance)
            if not math.isinf(next_distance)
            else 0.0
        )
        signed_integral += cumulative * exponential_mass
        profile_capacity += abs(cumulative) * exponential_mass
        maximum_cumulative = max(maximum_cumulative, abs(cumulative))
        segment_count += 1
    return {
        "gaussian_scale": gaussian_scale,
        "exact_response": exact_response,
        "nonexact_response": signed_integral,
        "total_response": exact_response + signed_integral,
        "profile_capacity": profile_capacity,
        "coefficient_variation": coefficient_variation,
        "capacity_to_variation_ratio": (
            profile_capacity / coefficient_variation
            if coefficient_variation > 0.0
            else 0.0
        ),
        "maximum_cumulative_profile": maximum_cumulative,
        "segment_count": segment_count,
    }


def cauchy_signed_layer_cake_ledger(
    response: FrequencyMap,
    continuum_nodes: tuple[float, ...],
) -> dict[str, object]:
    """Exact signed cumulative-profile formula for the Cauchy response.

    With Q(h) the cumulative nonexact coefficient mass inside lag radius h,

        <exp(-abs(x)),q> = q({0}) + integral exp(-h) Q(h) dh.

    Integrating abs(Q) gives a cancellation-preserving capacity bounded by
    the ordinary coefficient variation.
    """
    exact_response = 0.0 + 0.0j
    grouped: dict[float, complex] = {}
    coefficient_variation = 0.0
    for lag, coefficient in response.items():
        if lag.is_zero():
            exact_response += coefficient
            continue
        numerical_lag = abs(lag.numerical_value(continuum_nodes))
        grouped[numerical_lag] = (
            grouped.get(numerical_lag, 0.0 + 0.0j) + coefficient
        )
        coefficient_variation += abs(coefficient) * math.exp(-numerical_lag)
    radii = sorted(grouped)
    cumulative = 0.0 + 0.0j
    signed_integral = 0.0 + 0.0j
    profile_capacity = 0.0
    maximum_cumulative = 0.0
    for index, radius in enumerate(radii):
        cumulative += grouped[radius]
        next_radius = radii[index + 1] if index + 1 < len(radii) else math.inf
        exponential_mass = math.exp(-radius) - (
            math.exp(-next_radius) if not math.isinf(next_radius) else 0.0
        )
        signed_integral += cumulative * exponential_mass
        profile_capacity += abs(cumulative) * exponential_mass
        maximum_cumulative = max(maximum_cumulative, abs(cumulative))
    return {
        "exact_response": exact_response,
        "nonexact_response": signed_integral,
        "total_response": exact_response + signed_integral,
        "profile_capacity": profile_capacity,
        "coefficient_variation": coefficient_variation,
        "capacity_to_variation_ratio": (
            profile_capacity / coefficient_variation
            if coefficient_variation > 0.0
            else 0.0
        ),
        "maximum_cumulative_profile": maximum_cumulative,
        "segment_count": len(radii),
    }


def centered_cumulative_l1(
    source: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    reality_tolerance: float = 1.0e-10,
) -> dict[str, object]:
    """Center a real lag measure at zero and compute its primitive L1 norm."""
    if not source:
        return {
            "total_mass": 0.0,
            "centered_atoms": (),
            "primitive_l1": 0.0,
            "centered_mass_residual": 0.0,
        }
    numerical_atoms: dict[float, complex] = {}
    for lag, coefficient in source.items():
        numerical_lag = lag.numerical_value(continuum_nodes)
        numerical_atoms[numerical_lag] = (
            numerical_atoms.get(numerical_lag, 0.0 + 0.0j) + coefficient
        )
    total = sum(numerical_atoms.values())
    numerical_atoms[0.0] = numerical_atoms.get(0.0, 0.0 + 0.0j) - total
    atoms = sorted(
        (lag, coefficient)
        for lag, coefficient in numerical_atoms.items()
        if abs(coefficient) > 1.0e-14
    )
    if any(abs(coefficient.imag) > reality_tolerance for _, coefficient in atoms):
        raise ValueError("cumulative discrepancy requires a real signed measure")
    cumulative = 0.0
    primitive_l1 = 0.0
    for index, (lag, coefficient) in enumerate(atoms):
        cumulative += coefficient.real
        if index + 1 < len(atoms):
            primitive_l1 += abs(cumulative) * (atoms[index + 1][0] - lag)
    return {
        "total_mass": float(np.real_if_close(total)),
        "centered_atoms": tuple(
            (lag, coefficient.real) for lag, coefficient in atoms
        ),
        "primitive_l1": primitive_l1,
        "centered_mass_residual": cumulative,
    }


def gaussian_centered_moment_upper_bound(
    source: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    power: int,
    gaussian_scale: float,
) -> dict[str, float]:
    """Repeated-primitive bound for one Gaussian stationary moment.

    If d=M*delta_0+d_0 and A is the cumulative primitive of the zero-mass
    measure d_0, then

        |<exp(-x^2/(4u)), d_0^{*j}>|
          <= Gamma((j+1)/2)/(sqrt(pi)*u^(j/2)) * ||A||_1^j.

    Expanding d^{*power} gives the returned upper bound.
    """
    if power < 0:
        raise ValueError("power must be nonnegative")
    if gaussian_scale <= 0.0:
        raise ValueError("Gaussian scale must be positive")
    cumulative = centered_cumulative_l1(source, continuum_nodes)
    total_mass = abs(float(cumulative["total_mass"]))
    primitive_l1 = float(cumulative["primitive_l1"])
    terms = []
    for centered_power in range(power + 1):
        derivative_bound = (
            math.gamma((centered_power + 1.0) / 2.0)
            / math.sqrt(math.pi)
            / gaussian_scale ** (centered_power / 2.0)
        )
        terms.append(
            math.comb(power, centered_power)
            * total_mass ** (power - centered_power)
            * derivative_bound
            * primitive_l1**centered_power
        )
    return {
        "total_mass": total_mass,
        "primitive_l1": primitive_l1,
        "upper_bound": sum(terms),
        "largest_binomial_term": max(terms, default=0.0),
    }


def degree_two_gaussian_response_upper_bound(
    symbol: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    spectral_bound: float,
    rho: float,
    gaussian_scale: float,
) -> dict[str, float]:
    """Bound the degree-two response in one normalized Gaussian state."""
    if spectral_bound <= 0.0 or rho <= 0.0:
        raise ValueError("spectral bound and rho must be positive")
    node = math.sqrt(3.0) / 2.0
    amplitude = node * spectral_bound / (node * spectral_bound + rho)
    polynomial_factor = 2.0 * amplitude / (3.0 * spectral_bound**2)
    moment_bounds = {
        power: gaussian_centered_moment_upper_bound(
            symbol, continuum_nodes, power, gaussian_scale
        )
        for power in (3, 4, 5)
    }
    upper_bound = polynomial_factor**2 * (
        moment_bounds[5]["upper_bound"]
        + 2.0
        * node
        * spectral_bound
        * moment_bounds[4]["upper_bound"]
        + node**2
        * spectral_bound**2
        * moment_bounds[3]["upper_bound"]
    )
    return {
        "gaussian_scale": gaussian_scale,
        "total_mass": moment_bounds[3]["total_mass"],
        "primitive_l1": moment_bounds[3]["primitive_l1"],
        "third_moment_upper_bound": moment_bounds[3]["upper_bound"],
        "fourth_moment_upper_bound": moment_bounds[4]["upper_bound"],
        "fifth_moment_upper_bound": moment_bounds[5]["upper_bound"],
        "response_upper_bound": upper_bound,
    }


def two_sided_prime_continuum_symbol(
    prime_atoms: list[tuple[int, complex]],
    continuum_atoms: list[tuple[float, complex]],
    zero_tolerance: float = 1.0e-15,
) -> dict[str, object]:
    """Build formal two-sided maps for Re sum c_lambda exp(-i lambda t)."""
    nonzero_continuum = [
        (float(node), complex(coefficient))
        for node, coefficient in continuum_atoms
        if abs(float(node)) > zero_tolerance
    ]
    continuum_nodes = tuple(node for node, _ in nonzero_continuum)
    dimension = len(continuum_nodes)
    zero = FormalLag.zero(dimension)
    prime_map: FrequencyMap = {}
    continuum_map: FrequencyMap = {}

    for integer, coefficient in prime_atoms:
        lag = FormalLag.prime(int(integer), dimension)
        add_frequency_term(prime_map, lag, coefficient / 2.0)
        add_frequency_term(prime_map, -lag, np.conjugate(coefficient) / 2.0)

    for node, coefficient in continuum_atoms:
        coefficient = complex(coefficient)
        if abs(float(node)) <= zero_tolerance:
            add_frequency_term(continuum_map, zero, coefficient.real)
            continue
        index = continuum_nodes.index(float(node))
        lag = FormalLag.continuum_basis(index, dimension)
        add_frequency_term(continuum_map, lag, coefficient / 2.0)
        add_frequency_term(
            continuum_map, -lag, np.conjugate(coefficient) / 2.0
        )

    combined = add_frequency_maps(prime_map, continuum_map)
    return {
        "continuum_nodes": continuum_nodes,
        "prime_map": prime_map,
        "continuum_map": continuum_map,
        "combined_map": combined,
    }


def chebyshev_formal_orbit_coefficients(
    symbol: FrequencyMap,
    spectral_bound: float,
    series_coefficients: np.ndarray,
) -> FrequencyMap:
    """Expand sum alpha_k T_k(P/B) in the formal lag algebra."""
    if spectral_bound <= 0.0:
        raise ValueError("spectral bound must be positive")
    if not symbol:
        raise ValueError("symbol must be nonempty")
    dimension = len(next(iter(symbol)).continuum)
    q_previous = {FormalLag.zero(dimension): 1.0 + 0.0j}
    combined = scale_frequency_map(q_previous, complex(series_coefficients[0]))
    if len(series_coefficients) == 1:
        return combined
    q_current = scale_frequency_map(symbol, 1.0 / spectral_bound)
    combined = add_frequency_maps(
        combined,
        scale_frequency_map(q_current, complex(series_coefficients[1])),
    )
    for degree in range(1, len(series_coefficients) - 1):
        q_next = add_frequency_maps(
            scale_frequency_map(
                convolve_frequency_maps(symbol, q_current),
                2.0 / spectral_bound,
            ),
            scale_frequency_map(q_previous, -1.0),
        )
        combined = add_frequency_maps(
            combined,
            scale_frequency_map(
                q_next, complex(series_coefficients[degree + 1])
            ),
        )
        q_previous, q_current = q_current, q_next
    return combined


def formal_cauchy_response_ledger(
    symbol_components: dict[str, FrequencyMap],
    effect: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    near_cutoff: float,
) -> dict[str, object]:
    """Split -int P|b|^2 dmu into formal exact, near, and far terms."""
    if near_cutoff <= 0.0:
        raise ValueError("near cutoff must be positive")
    signed = {"exact": 0.0 + 0.0j, "near": 0.0 + 0.0j, "far": 0.0 + 0.0j}
    variation = {"exact": 0.0, "near": 0.0, "far": 0.0}
    counts = {"exact": 0, "near": 0, "far": 0}
    by_component: dict[str, dict[str, complex]] = {}
    for component, symbol in symbol_components.items():
        component_signed = {
            "exact": 0.0 + 0.0j,
            "near": 0.0 + 0.0j,
            "far": 0.0 + 0.0j,
        }
        for outer_lag, outer_coefficient in symbol.items():
            for left_lag, left_coefficient in effect.items():
                for right_lag, right_coefficient in effect.items():
                    residual = outer_lag + left_lag - right_lag
                    numerical_residual = abs(
                        residual.numerical_value(continuum_nodes)
                    )
                    if residual.is_zero():
                        bucket = "exact"
                    elif numerical_residual <= near_cutoff:
                        bucket = "near"
                    else:
                        bucket = "far"
                    term = -(
                        outer_coefficient
                        * left_coefficient
                        * np.conjugate(right_coefficient)
                        * math.exp(-numerical_residual)
                    )
                    signed[bucket] += term
                    component_signed[bucket] += term
                    variation[bucket] += abs(term)
                    counts[bucket] += 1
        by_component[component] = component_signed
    total = sum(signed.values())
    return {
        "signed": signed,
        "variation": variation,
        "counts": counts,
        "by_component": by_component,
        "total_response": float(np.real_if_close(total)),
        "imaginary_residual": float(abs(total.imag)),
    }


def formal_arbitrary_direction_audit(
    symbol: FrequencyMap,
    effect: FrequencyMap,
    continuum_nodes: tuple[float, ...],
    eigenvalue_tolerance: float = 1.0e-11,
) -> dict[str, float | int]:
    """Compare the canonical ray with the optimal direction on its support."""
    if not effect:
        return {
            "support_size": 0,
            "effective_gram_rank": 0,
            "canonical_energy": 0.0,
            "canonical_negative_response": 0.0,
            "canonical_negative_depth": 0.0,
            "arbitrary_negative_depth": 0.0,
            "canonical_to_arbitrary_depth_ratio": 0.0,
        }
    effect_lags = list(effect)
    frequencies = np.array(
        [lag.numerical_value(continuum_nodes) for lag in effect_lags]
    )
    coefficients = np.array([effect[lag] for lag in effect_lags])
    difference = frequencies[:, None] - frequencies[None, :]
    gram = np.exp(-np.abs(difference))
    objective = np.zeros_like(gram, dtype=complex)
    for lag, coefficient in symbol.items():
        frequency = lag.numerical_value(continuum_nodes)
        objective += coefficient * np.exp(-np.abs(frequency + difference))
    gram = 0.5 * (gram + np.conjugate(gram.T))
    objective = 0.5 * (objective + np.conjugate(objective.T))
    gram_values, gram_vectors = np.linalg.eigh(gram)
    keep = gram_values > eigenvalue_tolerance * max(1.0, gram_values.max())
    whitening = gram_vectors[:, keep] / np.sqrt(gram_values[keep])
    compressed = np.conjugate(whitening.T) @ objective @ whitening
    compressed = 0.5 * (compressed + np.conjugate(compressed.T))
    arbitrary_negative_depth = max(
        0.0, -float(np.linalg.eigvalsh(compressed).min())
    )
    canonical_energy = float(
        np.real(np.conjugate(coefficients) @ gram @ coefficients)
    )
    canonical_response = float(
        -np.real(np.conjugate(coefficients) @ objective @ coefficients)
    )
    canonical_depth = max(0.0, canonical_response / canonical_energy)
    fraction = (
        canonical_depth / arbitrary_negative_depth
        if arbitrary_negative_depth > 0.0
        else 0.0
    )
    return {
        "support_size": len(effect_lags),
        "effective_gram_rank": int(np.count_nonzero(keep)),
        "canonical_energy": canonical_energy,
        "canonical_negative_response": canonical_response,
        "canonical_negative_depth": canonical_depth,
        "arbitrary_negative_depth": arbitrary_negative_depth,
        "canonical_to_arbitrary_depth_ratio": fraction,
    }

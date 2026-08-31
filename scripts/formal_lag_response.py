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

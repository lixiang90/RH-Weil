"""Audits for the smooth-window cyclic fourth-moment ledger.

The finite feature identity and noncommutative word expansion are exact.
The window quadrature evaluates the paired arithmetic diagonal only; it does
not estimate the unpaired zeta correlations or the finite-Gabor boundary.
"""

from __future__ import annotations

import math
from collections.abc import Callable

import numpy as np
from numpy.polynomial.legendre import leggauss


TOL = 2.0e-10


def hermitian_random(
    rng: np.random.Generator, dimension: int
) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    return 0.5 * (raw + np.conjugate(raw.T))


def audit_noncommutative_word_ledger() -> None:
    rng = np.random.default_rng(260902)
    for dimension in (3, 7):
        background = hermitian_random(rng, dimension)
        prime = hermitian_random(rng, dimension)
        direct = np.trace(np.linalg.matrix_power(background + prime, 4))
        ledger = (
            np.trace(np.linalg.matrix_power(background, 4))
            + 4.0
            * np.trace(
                np.linalg.matrix_power(background, 3) @ prime
            )
            + 4.0
            * np.trace(
                np.linalg.matrix_power(background, 2)
                @ np.linalg.matrix_power(prime, 2)
            )
            + 2.0
            * np.trace(background @ prime @ background @ prime)
            + 4.0
            * np.trace(
                background @ np.linalg.matrix_power(prime, 3)
            )
            + np.trace(np.linalg.matrix_power(prime, 4))
        )
        assert abs(direct - ledger) <= TOL * max(1.0, abs(direct))
    print("noncommutative cyclic word ledger passed")


def audit_finite_feature_cycle() -> None:
    rng = np.random.default_rng(120926)
    for feature_count, sample_count in ((4, 7), (7, 11)):
        features = rng.normal(size=(feature_count, sample_count))
        signed_measure = rng.normal(size=sample_count)
        scale = 1.73
        matrix = (
            features
            @ np.diag(signed_measure)
            @ features.T
            / scale
        )
        kernel = features.T @ features
        cyclic = np.einsum(
            "ij,jk,kl,li,i,j,k,l->",
            kernel,
            kernel,
            kernel,
            kernel,
            signed_measure,
            signed_measure,
            signed_measure,
            signed_measure,
            optimize=True,
        ) / scale**4
        direct = np.trace(np.linalg.matrix_power(matrix, 4))
        assert abs(direct - cyclic) <= TOL * max(1.0, abs(direct))
    print("finite feature-kernel fourth-cycle identity passed")


def schatten_norm(matrix: np.ndarray, exponent: float) -> float:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    return float(np.sum(singular_values**exponent) ** (1.0 / exponent))


def audit_schatten_four_stability() -> None:
    rng = np.random.default_rng(1992609)
    for dimension in (3, 6, 10):
        left = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
            size=(dimension, dimension)
        )
        right = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
            size=(dimension, dimension)
        )
        difference = left - right
        left_norm = schatten_norm(left, 4.0)
        right_norm = schatten_norm(right, 4.0)
        difference_norm = schatten_norm(difference, 4.0)
        bound = difference_norm * (
            left_norm**3
            + right_norm * left_norm**2
            + right_norm**2 * left_norm
            + right_norm**3
        )
        trace_difference = abs(
            np.trace(np.linalg.matrix_power(left, 4))
            - np.trace(np.linalg.matrix_power(right, 4))
        )
        assert trace_difference <= bound + TOL * max(1.0, bound)
    print("Schatten-four fourth-trace stability passed")


def indicator_window(value: np.ndarray) -> np.ndarray:
    return (np.abs(value) <= 0.5).astype(float)


def montgomery_taylor_window(value: np.ndarray) -> np.ndarray:
    return np.where(
        np.abs(value) <= 0.5,
        np.cos(math.sqrt(2.0) * value),
        0.0,
    )


def cosine_window(parameter: float) -> Callable[[np.ndarray], np.ndarray]:
    return lambda value: np.where(
        np.abs(value) <= 0.5,
        np.cos(parameter * value),
        0.0,
    )


def cosine_second_constant(parameter: float) -> float:
    """Closed R(psi) for psi(u)=cos(parameter*u) on [-1/2,1/2]."""
    if parameter == 0.0:
        return 4.0 / 3.0
    sine_half = math.sin(parameter / 2.0)
    mass = 2.0 * sine_half / parameter
    square_mass = 0.5 + math.sin(parameter) / (2.0 * parameter)
    distance_energy = (
        2.0 * sine_half**2 / parameter**2
        + 2.0 * math.sin(parameter) / parameter**3
        - 2.0 * square_mass / parameter**2
    )
    return (square_mass + distance_energy) / mass**2


def gauss_integral(
    function: Callable[[np.ndarray], np.ndarray],
    lower: float,
    upper: float,
    nodes: np.ndarray,
    weights: np.ndarray,
) -> float:
    if upper <= lower:
        return 0.0
    midpoint = 0.5 * (lower + upper)
    half_length = 0.5 * (upper - lower)
    values = function(midpoint + half_length * nodes)
    return float(half_length * np.dot(weights, values))


def paired_diagonal_components(
    window: Callable[[np.ndarray], np.ndarray],
    order: int,
) -> dict[str, float]:
    """Return the three overlap integrals in the paired 2+2 diagonal."""
    nodes, weights = leggauss(order)
    unit_nodes = 0.5 * (nodes + 1.0)
    unit_weights = 0.5 * weights
    same = 0.0
    opposite = 0.0
    rectangle = 0.0

    for r, r_weight in zip(unit_nodes, unit_weights):
        # A_same is symmetric in r,s, so integrate on 0 <= s <= r.
        for base_s, base_weight in zip(unit_nodes, unit_weights):
            s = r * base_s
            outer_weight = 2.0 * r_weight * r * base_weight * r * s
            inner = gauss_integral(
                lambda u: (
                    window(u) ** 2
                    * window(u + r)
                    * window(u + s)
                ),
                -0.5,
                0.5 - r,
                nodes,
                weights,
            )
            same += outer_weight * inner

        # A_opposite and B live on r+s <= 1.
        for base_s, base_weight in zip(unit_nodes, unit_weights):
            s = (1.0 - r) * base_s
            outer_weight = (
                r_weight * (1.0 - r) * base_weight * r * s
            )
            opposite_inner = gauss_integral(
                lambda u: (
                    window(u) ** 2
                    * window(u + r)
                    * window(u - s)
                ),
                -0.5 + s,
                0.5 - r,
                nodes,
                weights,
            )
            rectangle_inner = gauss_integral(
                lambda u: (
                    window(u)
                    * window(u + r)
                    * window(u + s)
                    * window(u + r + s)
                ),
                -0.5,
                0.5 - r - s,
                nodes,
                weights,
            )
            opposite += outer_weight * opposite_inner
            rectangle += outer_weight * rectangle_inner

    mass = gauss_integral(window, -0.5, 0.5, nodes, weights)
    alternating_family = 4.0 * same / mass**4
    adjacent_family = 4.0 * (opposite + rectangle) / mass**4
    return {
        "mass": mass,
        "same_overlap": same,
        "opposite_overlap": opposite,
        "rectangle_overlap": rectangle,
        "alternating_family": alternating_family,
        "adjacent_family": adjacent_family,
        "paired_diagonal": alternating_family + adjacent_family,
    }


def audit_flat_window_exact_values() -> None:
    result = paired_diagonal_components(indicator_window, 12)
    expected = {
        "mass": 1.0,
        "same_overlap": 1.0 / 20.0,
        "opposite_overlap": 1.0 / 120.0,
        "rectangle_overlap": 1.0 / 120.0,
        "alternating_family": 1.0 / 5.0,
        "adjacent_family": 1.0 / 15.0,
        "paired_diagonal": 4.0 / 15.0,
    }
    for key, value in expected.items():
        assert abs(result[key] - value) <= TOL
    print(
        "flat paired diagonal: "
        "alternating=1/5, adjacent=1/15, total=4/15"
    )


def audit_montgomery_taylor_window() -> None:
    coarse = paired_diagonal_components(montgomery_taylor_window, 36)
    fine = paired_diagonal_components(montgomery_taylor_window, 52)
    for key in (
        "mass",
        "same_overlap",
        "opposite_overlap",
        "rectangle_overlap",
        "paired_diagonal",
    ):
        assert abs(coarse[key] - fine[key]) <= 2.0e-11

    expected_mass = math.sqrt(2.0) * math.sin(1.0 / math.sqrt(2.0))
    assert abs(fine["mass"] - expected_mass) <= TOL
    second_constant = cosine_second_constant(math.sqrt(2.0))
    expected_second_constant = (
        0.5
        + 1.0
        / math.sqrt(2.0)
        / math.tan(1.0 / math.sqrt(2.0))
    )
    assert abs(second_constant - expected_second_constant) <= TOL
    second_centered = second_constant - 1.0
    remainder_budget = second_centered - fine["paired_diagonal"]
    assert fine["paired_diagonal"] < 0.25
    assert remainder_budget > 0.077
    print(
        "Montgomery--Taylor paired diagonal: "
        f"D22={fine['paired_diagonal']:.12f}, "
        f"alternating={fine['alternating_family']:.12f}, "
        f"adjacent={fine['adjacent_family']:.12f}, "
        f"self-improvement remainder budget={remainder_budget:.12f}"
    )


def audit_cosine_endpoint_candidate() -> None:
    kappa = 2.0 - cosine_second_constant(math.sqrt(2.0))
    result = paired_diagonal_components(cosine_window(math.pi), 24)
    second_constant = cosine_second_constant(math.pi)
    centered_second = second_constant - 1.0
    threshold = (
        (1.0 - centered_second) ** 2 / kappa
        - 1.0
        + 2.0 * centered_second
    )
    margin = threshold - result["paired_diagonal"]
    assert abs(second_constant - 1.48370055013617) <= 2.0e-13
    assert abs(result["paired_diagonal"] - 0.165513041999767) <= 2.0e-13
    assert abs(margin - 0.198267006980362) <= 2.0e-13
    sigma_at_threshold = (
        centered_second - threshold
    ) / (1.0 - centered_second)
    assert 0.0 < sigma_at_threshold < 0.75
    print(
        "cos(pi*u) endpoint candidate: "
        f"R={second_constant:.12f}, "
        f"D22={result['paired_diagonal']:.12f}, "
        f"record-beating remainder margin={margin:.12f}"
    )


def main() -> None:
    audit_noncommutative_word_ledger()
    audit_finite_feature_cycle()
    audit_schatten_four_stability()
    audit_flat_window_exact_values()
    audit_montgomery_taylor_window()
    audit_cosine_endpoint_candidate()
    print("Smooth fourth-window audits passed.")


if __name__ == "__main__":
    main()

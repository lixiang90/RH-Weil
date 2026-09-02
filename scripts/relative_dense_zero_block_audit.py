"""Finite audits for note 228's moving zero-block transfer.

This script checks normalization and moment algebra.  It does not prove the
prime-side fourth-trace estimate or a new zeta-zero proportion.
"""

from __future__ import annotations

import math

import numpy as np


def audit_gabor_block_length() -> None:
    for height in (1.0e4, 1.0e6, 1.0e8):
        log_scale = math.log(height / (2.0 * math.pi))
        step = 2.0 * math.pi / log_scale
        dimension = math.floor(log_scale * height / (2.0 * math.pi))
        block_length = dimension * step
        assert 0.0 <= height - block_length < step
    print("AF moving-grid block length passed")


def audit_relative_dense_endpoint_scale() -> None:
    ratios = [1.0 / math.sqrt(log_scale) for log_scale in (16.0, 64.0, 256.0)]
    assert all(right < left for left, right in zip(ratios, ratios[1:]))
    assert ratios[-1] < 0.07
    print("relative-dense endpoint displacement scale passed")


def audit_centered_trace_identities() -> None:
    rng = np.random.default_rng(20260902)
    for dimension in (3, 7, 12):
        raw = rng.normal(size=(dimension, dimension))
        matrix = 0.5 * (raw + raw.T)
        identity = np.eye(dimension)
        centered_second = np.trace((matrix - identity) @ (matrix - identity))
        raw_second = (
            np.trace(matrix @ matrix) - 2.0 * np.trace(matrix) + dimension
        )
        assert abs(centered_second - raw_second) < 1.0e-10

        centered_fourth = np.trace(np.linalg.matrix_power(matrix - identity, 4))
        raw_fourth = (
            np.trace(np.linalg.matrix_power(matrix, 4))
            - 4.0 * np.trace(np.linalg.matrix_power(matrix, 3))
            + 6.0 * np.trace(matrix @ matrix)
            - 4.0 * np.trace(matrix)
            + dimension
        )
        assert abs(centered_fourth - raw_fourth) < 1.0e-9
    print("raw-to-centered trace identities passed")


def mt_constants() -> tuple[float, float, float, float, float]:
    centered_second = (
        -0.5 + math.cos(1.0 / math.sqrt(2.0))
        / (math.sqrt(2.0) * math.sin(1.0 / math.sqrt(2.0)))
    )
    centered_fourth = 0.252508968713594
    sigma = (centered_second - centered_fourth) / (1.0 - centered_second)
    simple = (1.0 - centered_second) ** 2 / (
        1.0 - 2.0 * centered_second + centered_fourth
    )
    distinct = 0.5 * (1.0 + simple)
    return centered_second, centered_fourth, sigma, simple, distinct


def audit_quartic_certificate() -> None:
    centered_second, centered_fourth, sigma, simple, distinct = mt_constants()
    assert centered_fourth < centered_second < 1.0
    assert sigma < 0.75
    assert abs(simple - 0.756902665727919) < 2.0e-15
    assert abs(distinct - 0.878451332863959) < 2.0e-15
    second_moment_simple = 1.0 - centered_second
    assert simple > second_moment_simple
    print(
        "MT moving-block quartic implication: "
        f"sigma={sigma:.12f}, simple={simple:.12f}, distinct={distinct:.12f}"
    )


def moments(points: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return np.array([np.dot(weights, points**degree) for degree in range(5)])


def christoffel_at_zero(raw_moments: np.ndarray) -> float:
    moment_matrix = np.array(
        [[raw_moments[row + column] for column in range(3)] for row in range(3)]
    )
    return 1.0 / np.linalg.inv(moment_matrix)[0, 0]


def audit_christoffel_data_gap() -> None:
    variance, fourth, _, _, _ = mt_constants()
    q = variance**2 / fourth
    radius = math.sqrt(fourth / variance)
    symmetric_points = np.array([1.0, 1.0 - radius, 1.0 + radius])
    symmetric_weights = np.array([1.0 - q, 0.5 * q, 0.5 * q])

    kurtosis = fourth / variance**2
    ratio_sum = kurtosis + 1.0
    odds = 0.5 * (ratio_sum + math.sqrt(ratio_sum**2 - 4.0))
    p = 1.0 / (1.0 + odds)
    positive = math.sqrt(variance * (1.0 - p) / p)
    negative = math.sqrt(variance * p / (1.0 - p))
    skew_points = np.array([1.0 + positive, 1.0 - negative])
    skew_weights = np.array([p, 1.0 - p])

    symmetric = moments(symmetric_points, symmetric_weights)
    skew = moments(skew_points, skew_weights)
    for degree in (0, 1, 2, 4):
        centered_symmetric = np.dot(
            symmetric_weights, (symmetric_points - 1.0) ** degree
        )
        centered_skew = np.dot(skew_weights, (skew_points - 1.0) ** degree)
        assert abs(centered_symmetric - centered_skew) < 2.0e-14
    symmetric_third = np.dot(symmetric_weights, (symmetric_points - 1.0) ** 3)
    skew_third = np.dot(skew_weights, (skew_points - 1.0) ** 3)
    assert abs(symmetric_third) < 1.0e-14
    assert abs(skew_third - 0.218106199166593) < 2.0e-15

    symmetric_christoffel = christoffel_at_zero(symmetric)
    # A degree-two polynomial can vanish at both skew support points while
    # taking value one at zero, so its Christoffel minimum is exactly zero.
    assert 0.13 < symmetric_christoffel < 0.15
    assert np.all(skew_points > 0.0)
    print(
        "Christoffel data gap passed: "
        f"symmetric={symmetric_christoffel:.12f}, skew=0"
    )


def main() -> None:
    audit_gabor_block_length()
    audit_relative_dense_endpoint_scale()
    audit_centered_trace_identities()
    audit_quartic_certificate()
    audit_christoffel_data_gap()
    print("Relative-dense zero-block audits passed")
    print("[scope] implication only; no prime-side fourth theorem or record claim")


if __name__ == "__main__":
    main()

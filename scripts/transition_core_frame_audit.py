"""Finite spectral audit of the balanced transition determinant core.

The vertices are the actual primitive prime-power ratio atoms in a band around
``X log X``.  After division by the exact flat-window atomic diagonal, the
von Mangoldt weights cancel.  We therefore measure both the absolute Schur
row sums and the largest eigenvalue of the response-specific Hermitian core.

This is exploratory evidence only.  In particular, bounded values at the
tested heights do not prove a uniform frame inequality.
"""

from __future__ import annotations

import math

import numpy as np

from ordinary_seam_kernel_audit import (
    RatioRecord,
    flat_support,
    geometric_sum,
    periodic_shifted_overlap,
)
from transition_ratio_kernel_audit import transition_records


def balanced_records(limit: int) -> list[RatioRecord]:
    length = math.log(limit)
    central_product = limit * length
    factor_lower = central_product**0.25
    factor_upper = central_product**0.75
    return [
        record
        for record in transition_records(limit, 0.75, 1.25)
        if factor_lower <= record.numerator <= factor_upper
        and factor_lower <= record.denominator <= factor_upper
    ]


def normalized_cross(
    left: RatioRecord,
    right: RatioRecord,
    length: float,
    height: float,
    dimension: int,
) -> complex:
    delta = left.ratio_log - right.ratio_log
    left_support = flat_support(left, length)
    right_support = flat_support(right, length)
    left_mass = (left_support[1] - left_support[0]) / length
    right_mass = (right_support[1] - right_support[0]) / length
    overlap = periodic_shifted_overlap(
        left_support, right_support, delta, length
    ) / length
    phase = complex(math.cos(height * delta), math.sin(height * delta))
    response = phase * geometric_sum(
        dimension, 2.0 * math.pi / length, delta
    )
    return overlap * response / (
        dimension * math.sqrt(left_mass * right_mass)
    )


def core_edges(
    records: list[RatioRecord], limit: int, cutoff_multiple: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    length = math.log(limit)
    height = 2.0 * math.pi * limit
    dimension = round(limit * length)
    determinant_cutoff = cutoff_multiple * length
    product_lower = limit * length**0.75
    # If mn >= product_lower^2 and |m-n| <= H, then min(m,n) is at
    # least this value.  Hence the ratio window below cannot miss a core edge.
    cross_lower = (
        math.sqrt(determinant_cutoff**2 + 4.0 * product_lower**2)
        - determinant_cutoff
    ) / 2.0
    ratio_window = math.log1p(determinant_cutoff / cross_lower)

    left_indices: list[int] = []
    right_indices: list[int] = []
    values: list[complex] = []
    for left_index, left in enumerate(records):
        for right_index in range(left_index + 1, len(records)):
            right = records[right_index]
            if right.ratio_log - left.ratio_log > ratio_window:
                break
            determinant = (
                left.numerator * right.denominator
                - left.denominator * right.numerator
            )
            if determinant == 0 or abs(determinant) > determinant_cutoff:
                continue
            value = normalized_cross(left, right, length, height, dimension)
            left_indices.append(left_index)
            right_indices.append(right_index)
            values.append(value)

    return (
        np.asarray(left_indices, dtype=np.int64),
        np.asarray(right_indices, dtype=np.int64),
        np.asarray(values, dtype=np.complex128),
    )


def hermitian_matvec(
    vector: np.ndarray,
    left: np.ndarray,
    right: np.ndarray,
    values: np.ndarray,
) -> np.ndarray:
    result = vector.copy()
    np.add.at(result, left, values * vector[right])
    np.add.at(result, right, values.conjugate() * vector[left])
    return result


def largest_eigenvalue_lanczos(
    vertex_count: int,
    left: np.ndarray,
    right: np.ndarray,
    values: np.ndarray,
    steps: int = 64,
) -> float:
    if vertex_count == 0:
        return 0.0
    rng = np.random.default_rng(20260902)
    vector = rng.normal(size=vertex_count) + 1j * rng.normal(size=vertex_count)
    vector /= np.linalg.norm(vector)
    basis: list[np.ndarray] = []
    diagonal: list[float] = []
    off_diagonal: list[float] = []
    previous = np.zeros(vertex_count, dtype=np.complex128)
    beta = 0.0

    for _ in range(min(steps, vertex_count)):
        basis.append(vector.copy())
        image = hermitian_matvec(vector, left, right, values) - beta * previous
        alpha = float(np.vdot(vector, image).real)
        image -= alpha * vector
        # Full reorthogonalization keeps the small tridiagonal audit stable.
        for old_vector in basis:
            image -= np.vdot(old_vector, image) * old_vector
        next_beta = float(np.linalg.norm(image))
        diagonal.append(alpha)
        if next_beta <= 1.0e-13:
            break
        off_diagonal.append(next_beta)
        previous, vector, beta = vector, image / next_beta, next_beta

    tridiagonal = np.diag(diagonal)
    if len(diagonal) > 1:
        bands = np.asarray(off_diagonal[: len(diagonal) - 1])
        tridiagonal += np.diag(bands, 1) + np.diag(bands, -1)
    return float(np.linalg.eigvalsh(tridiagonal)[-1])


def largest_affine_clique(
    records: list[RatioRecord],
    determinant_cutoff: float,
    edge_left: np.ndarray,
    edge_right: np.ndarray,
) -> tuple[int, int, int, int, list[RatioRecord]]:
    lines: dict[tuple[int, int, int], set[int]] = {}
    for left_index, right_index in zip(edge_left, edge_right):
        left = records[int(left_index)]
        right = records[int(right_index)]
        delta_a = right.numerator - left.numerator
        delta_b = right.denominator - left.denominator
        divisor = math.gcd(abs(delta_a), abs(delta_b))
        direction_a = delta_a // divisor
        direction_b = delta_b // divisor
        if direction_a < 0 or (direction_a == 0 and direction_b < 0):
            direction_a = -direction_a
            direction_b = -direction_b
        intercept = (
            left.numerator * direction_b
            - left.denominator * direction_a
        )
        key = (direction_a, direction_b, intercept)
        lines.setdefault(key, set()).update((int(left_index), int(right_index)))

    best: tuple[int, int, int, int, list[RatioRecord]] = (0, 0, 0, 0, [])
    for (direction_a, direction_b, intercept), indices in lines.items():
        base_index = next(iter(indices))
        base = records[base_index]
        parameterized: list[tuple[int, int]] = []
        for index in indices:
            record = records[index]
            delta_a = record.numerator - base.numerator
            delta_b = record.denominator - base.denominator
            if direction_a != 0:
                assert delta_a % direction_a == 0
                parameter = delta_a // direction_a
                assert delta_b == parameter * direction_b
            else:
                assert delta_b % direction_b == 0
                parameter = delta_b // direction_b
                assert delta_a == 0
            parameterized.append((parameter, index))
        parameterized.sort()
        left_position = 0
        for right_position, (right_parameter, _) in enumerate(parameterized):
            while (
                abs(intercept)
                * (right_parameter - parameterized[left_position][0])
                > determinant_cutoff
            ):
                left_position += 1
            cluster = [
                records[index]
                for _, index in parameterized[left_position : right_position + 1]
            ]
            if len(cluster) > best[0]:
                best = (
                    len(cluster),
                    direction_a,
                    direction_b,
                    intercept,
                    cluster,
                )
    return best

def audit_core(limit: int, cutoff_multiple: float) -> None:
    records = balanced_records(limit)
    left, right, values = core_edges(records, limit, cutoff_multiple)
    degrees = np.zeros(len(records), dtype=np.int64)
    absolute_rows = np.zeros(len(records), dtype=float)
    np.add.at(degrees, left, 1)
    np.add.at(degrees, right, 1)
    np.add.at(absolute_rows, left, np.abs(values))
    np.add.at(absolute_rows, right, np.abs(values))
    largest = largest_eigenvalue_lanczos(len(records), left, right, values)
    max_index = int(np.argmax(absolute_rows)) if records else 0
    max_record = records[max_index] if records else None
    percentile_degree = float(np.quantile(degrees, 0.99)) if records else 0.0
    percentile_row = float(np.quantile(absolute_rows, 0.99)) if records else 0.0
    mean_degree = 2.0 * len(values) / max(len(records), 1)
    label = (
        f"{max_record.numerator}/{max_record.denominator}"
        if max_record is not None
        else "none"
    )
    print(
        f"X={limit:>5d}, C={cutoff_multiple:g}: vertices={len(records):>6d}, "
        f"edges={len(values):>6d}, mean-degree={mean_degree:.4f}, "
        f"p99-degree={percentile_degree:.1f}, max-degree={degrees.max(initial=0)}, "
        f"p99-Schur={percentile_row:.4f}, max-Schur={absolute_rows.max(initial=0.0):.4f}, "
        f"lambda_max={largest:.6f}, max-row-vertex={label}"
    )
    if limit >= 10_000 and cutoff_multiple == 1.0 and max_record is not None:
        incidents: list[tuple[int, complex]] = []
        for edge_index in np.flatnonzero(left == max_index):
            incidents.append((int(right[edge_index]), values[edge_index]))
        for edge_index in np.flatnonzero(right == max_index):
            incidents.append((int(left[edge_index]), values[edge_index].conjugate()))
        details = []
        for neighbor_index, value in sorted(incidents):
            neighbor = records[neighbor_index]
            determinant = (
                max_record.numerator * neighbor.denominator
                - max_record.denominator * neighbor.numerator
            )
            radial_ratio = math.sqrt(
                (neighbor.numerator * neighbor.denominator)
                / (max_record.numerator * max_record.denominator)
            )
            details.append(
                f"{neighbor.numerator}/{neighbor.denominator}:"
                f"h={determinant:+d},scale={radial_ratio:.3f},"
                f"|g|={abs(value):.3f},arg={np.angle(value):+.3f}"
            )
        print("  max-row neighbors: " + "; ".join(details))
    if cutoff_multiple == 1.0:
        clique_size, direction_a, direction_b, intercept, clique = largest_affine_clique(
            records,
            cutoff_multiple * math.log(limit),
            left,
            right,
        )
        points = ",".join(
            f"{record.numerator}/{record.denominator}" for record in clique
        )
        print(
            f"  largest affine clique: size={clique_size}, "
            f"direction=({direction_a},{direction_b}), "
            f"r={intercept:+d}, points={points}"
        )
    if limit == 10_000 and cutoff_multiple == 1.0:
        expected = {(23, 3449), (27, 4049), (29, 4349), (31, 4649), (32, 4799)}
        observed = {(record.numerator, record.denominator) for record in clique}
        assert observed == expected
        assert (direction_a, direction_b, intercept) == (1, 150, 1)
        assert max(
            abs(a * d - b * c)
            for a, b in expected
            for c, d in expected
        ) <= math.log(limit)
    assert np.all(np.isfinite(values))
    assert largest <= 1.0 + absolute_rows.max(initial=0.0) + 1.0e-9


def main() -> None:
    for limit in (300, 600, 1_200, 2_500, 5_000, 10_000):
        for cutoff_multiple in (1.0, 4.0):
            audit_core(limit, cutoff_multiple)
    print("balanced transition-core frame audit passed")


if __name__ == "__main__":
    main()

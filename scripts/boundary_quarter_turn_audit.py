"""Audit the optimal and natural quarter-turns for Gabor boundary blocks.

The finite experiments use actual von Mangoldt prime-power weights and a
fixed-width smooth compact window.  They test a candidate polarization of the
exterior Gabor modes; they do not prove an asymptotic estimate or a zeta-zero
statement.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

from adjacent_bulk_edge_audit import prime_power_weights


TOL = 2.0e-10


def smootherstep(value: np.ndarray) -> np.ndarray:
    clipped = np.clip(value, 0.0, 1.0)
    return clipped**3 * (10.0 - 15.0 * clipped + 6.0 * clipped**2)


def window_value(value: np.ndarray, length: float) -> np.ndarray:
    return smootherstep(length / 2.0 - np.abs(value))


def window_mass(length: float, sample_count: int = 8193) -> float:
    grid = np.linspace(-length / 2.0, length / 2.0, sample_count)
    values = window_value(grid, length) ** 2
    return float(np.trapezoid(values, grid) / length)


def centered_response_modes(
    shift: float,
    length: float,
    max_mode: int,
    sample_count: int = 2049,
) -> np.ndarray:
    """Numerically integrate the real-even centered coefficients c_x(r)."""

    half_support = (length - shift) / 2.0
    centered_grid = np.linspace(-half_support, half_support, sample_count)
    left = window_value(shift / 2.0 + centered_grid, length)
    right = window_value(shift / 2.0 - centered_grid, length)
    symbol = left * right
    modes = np.arange(max_mode + 1, dtype=float)
    cosine = np.cos(
        np.outer(modes * (2.0 * math.pi / length), centered_grid)
    )
    return np.trapezoid(cosine * symbol[None, :], centered_grid, axis=1) / length


def quarter_turn(half_dimension: int) -> np.ndarray:
    identity = np.eye(half_dimension)
    zero = np.zeros_like(identity)
    return np.block([[zero, -identity], [identity, zero]])


@dataclass(frozen=True)
class BoundaryMetrics:
    limit: int
    dimension: int
    exterior_width: int
    normalized_energy: float
    normalized_pseudocovariance: float
    row_circularity_ratio: float
    natural_hs_fraction: float
    optimal_hs_fraction: float
    normalized_natural_op_defect: float
    normalized_operator_norm: float
    natural_op_defect_ratio: float


def actual_boundary_block(limit: int, exterior_width: int | None) -> tuple[np.ndarray, float, float]:
    length = math.log(limit)
    height = float(limit)
    spacing = 2.0 * math.pi / length
    dimension = max(2, round(height * length / (2.0 * math.pi)))
    width = dimension if exterior_width is None else min(dimension, exterior_width)

    rows = np.arange(dimension, dtype=int)[:, None]
    lower = -np.arange(1, width + 1, dtype=int)
    upper = dimension + np.arange(width, dtype=int)
    columns = np.concatenate((lower, upper))[None, :]
    differences = np.abs(rows - columns)
    phase_heights = height + 0.5 * spacing * (rows + columns)
    max_mode = int(np.max(differences))

    boundary = np.zeros((dimension, 2 * width), dtype=complex)
    for item in prime_power_weights(limit):
        centered = centered_response_modes(item.log_n, length, max_mode)
        coefficient = -math.sqrt(item.weight) / (2.0 * math.pi)
        boundary += (
            coefficient
            * centered[differences]
            * np.exp(1j * phase_heights * item.log_n)
        )

    beta = 2.0 * math.pi / (window_mass(length) * length)
    return boundary, beta, height * length


def boundary_metrics(limit: int, exterior_width: int | None) -> BoundaryMetrics:
    boundary, beta, zero_scale = actual_boundary_block(limit, exterior_width)
    dimension, doubled_width = boundary.shape
    width = doubled_width // 2
    energy = float(np.linalg.norm(boundary, ord="fro") ** 2)
    pseudocovariance = boundary @ boundary.T
    row_covariance = boundary @ boundary.conj().T
    pseudocovariance_norm = float(np.linalg.norm(pseudocovariance, ord="fro"))
    row_covariance_norm = float(np.linalg.norm(row_covariance, ord="fro"))

    natural = quarter_turn(width)
    natural_defect = boundary @ natural - 1j * boundary
    natural_hs_fraction = float(
        np.linalg.norm(natural_defect, ord="fro") ** 2 / (2.0 * energy)
    )

    column_covariance = boundary.conj().T @ boundary
    skew_imaginary = np.imag(column_covariance)
    assert np.linalg.norm(skew_imaginary.T + skew_imaginary, ord="fro") <= (
        TOL * max(1.0, np.linalg.norm(skew_imaginary, ord="fro"))
    )
    nuclear_skew = float(np.linalg.svd(skew_imaginary, compute_uv=False).sum())
    optimal_hs_fraction = max(0.0, 1.0 - nuclear_skew / energy)

    natural_op_defect = float(np.linalg.norm(natural_defect, ord=2))
    operator_norm = float(np.linalg.norm(boundary, ord=2))
    return BoundaryMetrics(
        limit=limit,
        dimension=dimension,
        exterior_width=width,
        normalized_energy=beta**2 * energy / zero_scale,
        normalized_pseudocovariance=(
            beta**4 * pseudocovariance_norm**2 / zero_scale
        ),
        row_circularity_ratio=pseudocovariance_norm / row_covariance_norm,
        natural_hs_fraction=natural_hs_fraction,
        optimal_hs_fraction=optimal_hs_fraction,
        normalized_natural_op_defect=beta * natural_op_defect,
        normalized_operator_norm=beta * operator_norm,
        natural_op_defect_ratio=natural_op_defect / operator_norm,
    )


def audit_optimal_formula() -> None:
    rank = 5
    identity = np.eye(rank, dtype=complex)
    coherent = np.hstack((identity, np.zeros_like(identity)))
    circular = np.hstack((identity, 1j * identity)) / math.sqrt(2.0)
    natural = quarter_turn(rank)

    for boundary, expected_fraction in ((coherent, 1.0), (circular, 0.0)):
        energy = float(np.linalg.norm(boundary, ord="fro") ** 2)
        covariance = boundary.conj().T @ boundary
        nuclear_skew = float(np.linalg.svd(np.imag(covariance), compute_uv=False).sum())
        fraction = 1.0 - nuclear_skew / energy
        assert abs(fraction - expected_fraction) <= TOL

    exact_defect = circular @ natural - 1j * circular

    rng = np.random.default_rng(209)
    random_boundary = rng.normal(size=(2 * rank, 2 * rank)) + 1j * rng.normal(
        size=(2 * rank, 2 * rank)
    )
    random_covariance = random_boundary.conj().T @ random_boundary
    random_skew = np.imag(random_covariance)
    left_vectors, singular_values, right_vectors = np.linalg.svd(random_skew)
    optimal = right_vectors.T @ left_vectors.T
    assert np.linalg.norm(optimal.T + optimal, ord="fro") <= TOL
    assert np.linalg.norm(optimal @ optimal + np.eye(2 * rank), ord="fro") <= TOL
    attained = float(np.trace(optimal @ random_skew))
    assert abs(attained - singular_values.sum()) <= TOL * singular_values.sum()
    defect = np.linalg.norm(random_boundary @ optimal - 1j * random_boundary, ord="fro") ** 2
    predicted = (
        2.0 * np.linalg.norm(random_boundary, ord="fro") ** 2
        - 2.0 * singular_values.sum()
    )
    assert abs(defect - predicted) <= TOL * max(1.0, predicted)
    assert np.linalg.norm(exact_defect, ord="fro") <= TOL
    print("optimal quarter-turn trace/nuclear-norm formula anchors passed")



def audit_finite_band_locality_no_go() -> None:
    rng = np.random.default_rng(208)
    dimension = 13
    bandwidth = 4
    indices = list(range(-bandwidth, dimension + bandwidth))
    matrix = np.zeros((len(indices), len(indices)), dtype=complex)
    for row_position, row in enumerate(indices):
        for column_position, column in enumerate(indices):
            if abs(row - column) <= bandwidth:
                matrix[row_position, column_position] = (
                    rng.normal() + 1j * rng.normal()
                )

    interior = [indices.index(index) for index in range(dimension)]
    lower = [indices.index(-offset) for offset in range(1, bandwidth + 1)]
    upper = [
        indices.index(dimension - 1 + offset)
        for offset in range(1, bandwidth + 1)
    ]
    lower_block = matrix[np.ix_(interior, lower)]
    upper_block = matrix[np.ix_(interior, upper)]
    assert abs(np.vdot(lower_block, upper_block)) <= TOL

    boundary = np.hstack((lower_block, upper_block))
    defect = boundary @ quarter_turn(bandwidth) - 1j * boundary
    baseline = 2.0 * np.linalg.norm(boundary, ord="fro") ** 2
    assert abs(np.linalg.norm(defect, ord="fro") ** 2 - baseline) <= (
        TOL * max(1.0, baseline)
    )
    print("finite-band lower/upper locality no-go passed")

def audit_actual_blocks(limits: tuple[int, ...], exterior_width: int | None) -> None:
    results = [boundary_metrics(limit, exterior_width) for limit in limits]
    print(
        "X      d    w    beta^2||B||^2/N   beta^4||BB^T||^2/N   "
        "||BB^T||/||BB*||   natural-HS   optimal-HS   beta||B||op   "
        "beta||E_J||op   ||E_J||op/||B||op"
    )
    for result in results:
        print(
            f"{result.limit:<6d} {result.dimension:<4d} "
            f"{result.exterior_width:<4d} "
            f"{result.normalized_energy:>18.8e} "
            f"{result.normalized_pseudocovariance:>23.8e} "
            f"{result.row_circularity_ratio:>19.8e} "
            f"{result.natural_hs_fraction:>12.8f} "
            f"{result.optimal_hs_fraction:>12.8f} "
            f"{result.normalized_operator_norm:>13.8e} "
            f"{result.normalized_natural_op_defect:>15.8e} "
            f"{result.natural_op_defect_ratio:>19.8f}"
        )

    assert all(np.isfinite(value) for result in results for value in result.__dict__.values())
    assert all(0.0 <= result.optimal_hs_fraction <= 1.0 + TOL for result in results)
    assert all(result.natural_hs_fraction >= result.optimal_hs_fraction - TOL for result in results)
    print("actual von Mangoldt / smooth-window boundary blocks audited")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limits", nargs="+", type=int, default=(64, 128, 256))
    parser.add_argument(
        "--exterior-width",
        type=int,
        default=1000,
        help="number of modes retained at each Gabor boundary",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    audit_optimal_formula()
    audit_finite_band_locality_no_go()
    audit_actual_blocks(tuple(args.limits), args.exterior_width)
    print("Boundary quarter-turn audits passed.")


if __name__ == "__main__":
    main()

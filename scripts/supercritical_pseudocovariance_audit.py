"""Finite audits for the supercritical boundary pseudocovariance reduction.

The checks cover transpose symmetry, the exact boundary block factorization,
the centered physical-response fibres, covariance blindness, and the
quarter-turn identity.  They do not prove the open Vaughan estimate or any
zeta asymptotic.
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence

import numpy as np


TOL = 5.0e-11


def centered_coefficients(
    shift: float,
    spacing: float,
    bandwidth: int,
    rng: np.random.Generator,
) -> tuple[dict[int, float], dict[int, complex]]:
    """Return real-even c(r) and qhat(r)=exp(i r h x/2)c(r)."""

    centered: dict[int, float] = {0: float(rng.normal())}
    for mode in range(1, bandwidth + 1):
        value = float(rng.normal() / (1.0 + mode) ** 2)
        centered[mode] = value
        centered[-mode] = value
    coefficients = {
        mode: np.exp(0.5j * mode * spacing * shift) * value
        for mode, value in centered.items()
    }
    return centered, coefficients


def response_matrix(
    indices: Sequence[int],
    shift: float,
    spacing: float,
    coefficients: Mapping[int, complex],
) -> np.ndarray:
    return np.array(
        [
            [
                coefficients.get(row - column, 0.0)
                * np.exp(1j * column * spacing * shift)
                for column in indices
            ]
            for row in indices
        ],
        dtype=complex,
    )


def audit_transpose_symmetry_and_physical_fibres() -> None:
    rng = np.random.default_rng(206)
    length = 17.0
    spacing = 2.0 * math.pi / length
    height = 23.0
    dimension = 7
    exterior_width = 5
    indices = list(range(-exterior_width, dimension + exterior_width))
    shifts = (1.3, 4.2, 7.1)
    weights = (-0.7, 0.4, 1.1)
    bandwidth = 2 * (dimension + exterior_width)

    centered_data: list[dict[int, float]] = []
    coefficient_data: list[dict[int, complex]] = []
    response = np.zeros((len(indices), len(indices)), dtype=complex)

    for shift, weight in zip(shifts, weights):
        centered, coefficients = centered_coefficients(
            shift, spacing, bandwidth, rng
        )
        centered_data.append(centered)
        coefficient_data.append(coefficients)

        for mode, value in coefficients.items():
            reflected = coefficients.get(-mode, 0.0)
            target = np.exp(-1j * mode * spacing * shift) * value
            assert abs(reflected - target) <= TOL * max(1.0, abs(value))

        response += (
            weight
            * np.exp(1j * height * shift)
            * response_matrix(indices, shift, spacing, coefficients)
        )

    assert np.linalg.norm(response.T - response, ord="fro") <= TOL * max(
        1.0, np.linalg.norm(response, ord="fro")
    )

    predicted = np.zeros_like(response)
    for row_position, row in enumerate(indices):
        for column_position, column in enumerate(indices):
            mode = row - column
            predicted[row_position, column_position] = sum(
                weight
                * centered.get(mode, 0.0)
                * np.exp(
                    1j
                    * (height + 0.5 * spacing * (row + column))
                    * shift
                )
                for shift, weight, centered in zip(
                    shifts, weights, centered_data
                )
            )
    assert np.linalg.norm(response - predicted, ord="fro") <= TOL * max(
        1.0, np.linalg.norm(response, ord="fro")
    )

    interior_positions = [indices.index(index) for index in range(dimension)]
    exterior_positions = [
        position
        for position, index in enumerate(indices)
        if index < 0 or index >= dimension
    ]
    boundary = response[np.ix_(interior_positions, exterior_positions)]
    reverse_boundary = response[np.ix_(exterior_positions, interior_positions)]
    product_block = boundary @ reverse_boundary
    pseudocovariance = boundary @ boundary.T
    assert np.linalg.norm(
        product_block - pseudocovariance, ord="fro"
    ) <= TOL * max(1.0, np.linalg.norm(product_block, ord="fro"))
    print("centered fibres, transpose symmetry, and boundary factorization passed")


def audit_covariance_blindness() -> None:
    rank = 6
    identity = np.eye(rank, dtype=complex)
    zero = np.zeros_like(identity)
    coherent = np.hstack((identity, zero))
    circular = np.hstack((identity, 1j * identity)) / math.sqrt(2.0)

    coherent_covariance = coherent @ coherent.conj().T
    circular_covariance = circular @ circular.conj().T
    assert np.linalg.norm(coherent_covariance - identity, ord="fro") <= TOL
    assert np.linalg.norm(circular_covariance - identity, ord="fro") <= TOL
    assert np.linalg.norm(
        coherent_covariance - circular_covariance, ord="fro"
    ) <= TOL
    assert np.linalg.norm(coherent @ coherent.T - identity, ord="fro") <= TOL
    assert np.linalg.norm(circular @ circular.T, ord="fro") <= TOL

    coherent_singular = np.linalg.svd(coherent, compute_uv=False)
    circular_singular = np.linalg.svd(circular, compute_uv=False)
    assert np.linalg.norm(coherent_singular - circular_singular) <= TOL
    print("same-covariance / opposite-pseudocovariance obstruction passed")


def quarter_turn(rank: int) -> np.ndarray:
    identity = np.eye(rank)
    zero = np.zeros_like(identity)
    return np.block([[zero, -identity], [identity, zero]])


def audit_quarter_turn_identity() -> None:
    rng = np.random.default_rng(207)
    row_count = 5
    half_columns = 7
    boundary = rng.normal(size=(row_count, 2 * half_columns)) + 1j * rng.normal(
        size=(row_count, 2 * half_columns)
    )
    complex_structure = quarter_turn(half_columns)
    assert np.linalg.norm(
        complex_structure.T + complex_structure, ord="fro"
    ) <= TOL
    assert np.linalg.norm(
        complex_structure @ complex_structure + np.eye(2 * half_columns),
        ord="fro",
    ) <= TOL

    defect = boundary @ complex_structure - 1j * boundary
    pseudocovariance = boundary @ boundary.T
    reconstructed = (
        1j * boundary @ defect.T
        + 1j * defect @ boundary.T
        + defect @ defect.T
    ) / 2.0
    assert np.linalg.norm(
        pseudocovariance - reconstructed, ord="fro"
    ) <= TOL * max(1.0, np.linalg.norm(pseudocovariance, ord="fro"))

    left = np.linalg.norm(pseudocovariance, ord="fro")
    right = (
        2.0
        * np.linalg.norm(boundary, ord="fro")
        * np.linalg.norm(defect, ord=2)
    )
    assert left <= right + TOL * max(1.0, right)

    identity = np.eye(half_columns, dtype=complex)
    circular = np.hstack((identity, 1j * identity)) / math.sqrt(2.0)
    exact_defect = circular @ complex_structure - 1j * circular
    assert np.linalg.norm(exact_defect, ord="fro") <= TOL
    assert np.linalg.norm(circular @ circular.T, ord="fro") <= TOL
    print("quarter-turn identity and quantitative certificate passed")


def main() -> None:
    audit_transpose_symmetry_and_physical_fibres()
    audit_covariance_blindness()
    audit_quarter_turn_identity()
    print("Supercritical pseudocovariance audits passed.")


if __name__ == "__main__":
    main()

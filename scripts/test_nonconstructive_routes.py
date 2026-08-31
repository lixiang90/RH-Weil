"""Finite audits for notes 175--176.

These checks validate finite cone/KKT and Hodge-transgression identities only.
They are not interval certificates and are not evidence for RH.
"""

from __future__ import annotations

import numpy as np


def matrix_function(matrix: np.ndarray, function) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return (eigenvectors * function(eigenvalues)) @ eigenvectors.T


def supertrace(matrix: np.ndarray, grading: np.ndarray) -> float:
    return float(np.trace(grading @ matrix))


def test_atomic_kkt_certificate() -> None:
    # A = {(a,b,a+b)} and K = A intersect the positive orthant.
    phi = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    point = np.array([-1.0, 2.0, 1.0])
    coefficient = np.array([0.0, 1.5])
    projection = phi @ coefficient
    residual = point - projection

    annihilator = np.array([0.5, 0.5, -0.5])
    multipliers = np.array([1.5, 0.0, 0.0])

    assert np.allclose(residual, annihilator - multipliers)
    assert np.allclose(phi.T @ annihilator, 0.0)
    assert np.all(projection >= 0.0)
    assert np.all(multipliers >= 0.0)
    assert np.allclose(multipliers * projection, 0.0)

    # Variational inequality against random feasible points.
    rng = np.random.default_rng(175)
    for _ in range(100):
        candidate = phi @ rng.random(2)
        assert residual @ (candidate - projection) <= 1.0e-12


def test_rank_one_gram_separator() -> None:
    # L(a,b) = [[a,b],[b,a]], whose PSD cone is a >= |b|.
    point = np.array([0.0, 2.0])
    projection = np.array([1.0, 1.0])
    residual = point - projection

    u = np.array([1.0, -1.0]) / np.sqrt(2.0)
    witness = np.outer(u, u)
    l_star_witness = np.array(
        [np.trace(witness), witness[0, 1] + witness[1, 0]]
    )
    gram_at_projection = np.array([[1.0, 1.0], [1.0, 1.0]])

    assert np.allclose(residual, -l_star_witness)
    assert np.linalg.eigvalsh(witness).min() >= -1.0e-14
    assert np.linalg.eigvalsh(gram_at_projection).min() >= -1.0e-14
    assert abs(np.trace(witness @ gram_at_projection)) <= 1.0e-14


def test_inserted_hodge_transgression() -> None:
    boundary = np.array([[1.0, 0.3], [0.0, 2.0]])
    zero = np.zeros((2, 2))
    dirac = np.block([[zero, boundary.T], [boundary, zero]])
    grading = np.diag([1.0, 1.0, -1.0, -1.0])
    laplacian = dirac @ dirac

    a_plus = np.array([[1.2, 0.4], [0.4, -0.2]])
    a_minus = np.array([[0.3, -0.1], [-0.1, 0.8]])
    insertion = np.block([[a_plus, zero], [zero, a_minus]])
    commutator = dirac @ insertion - insertion @ dirac

    time = 0.37
    heat = matrix_function(laplacian, lambda x: np.exp(-time * x))
    inverse = matrix_function(laplacian, lambda x: 1.0 / x)

    left = supertrace(insertion @ heat, grading)
    right = -0.5 * supertrace(
        commutator @ dirac @ inverse @ heat, grading
    )
    assert abs(left - right) <= 2.0e-12

    # Check the derivative identity independently by a centered difference.
    step = 1.0e-6
    heat_plus = matrix_function(
        laplacian, lambda x: np.exp(-(time + step) * x)
    )
    heat_minus = matrix_function(
        laplacian, lambda x: np.exp(-(time - step) * x)
    )
    finite_difference = (
        supertrace(insertion @ heat_plus, grading)
        - supertrace(insertion @ heat_minus, grading)
    ) / (2.0 * step)
    derivative = 0.5 * supertrace(
        commutator @ dirac @ heat, grading
    )
    assert abs(finite_difference - derivative) <= 2.0e-9


def test_face_weight_commutator_ledger() -> None:
    incidence = np.array([[1.0, -1.0], [0.0, 1.0]])
    zero = np.zeros((2, 2))
    dirac = np.block([[zero, incidence.T], [incidence, zero]])
    weights_even = np.array([0.2, 1.1])
    weights_odd = np.array([-0.4, 0.7])
    insertion = np.diag(np.concatenate([weights_even, weights_odd]))
    commutator = dirac @ insertion - insertion @ dirac

    edge_energy = 0.0
    for odd in range(2):
        for even in range(2):
            edge_energy += (
                abs(incidence[odd, even]) ** 2
                * abs(weights_even[even] - weights_odd[odd]) ** 2
            )
    assert abs(np.linalg.norm(commutator, "fro") ** 2 - 2.0 * edge_energy) <= (
        1.0e-12
    )


def test_spectral_density_only_no_go() -> None:
    laplacian = np.eye(2)
    threshold = 0.5
    low_spectral_mass = int(np.count_nonzero(np.linalg.eigvalsh(laplacian) <= threshold))
    point = np.array([-1.0, -1.0])
    positive_projection = np.maximum(point, 0.0)
    distance_squared = np.linalg.norm(point - positive_projection) ** 2
    assert low_spectral_mass == 0
    assert abs(distance_squared - 2.0) <= 1.0e-14


def test_random_grid_fejer_identity() -> None:
    positions = np.array([-0.7, 0.1, 0.8, 1.55])
    coefficients = np.array([0.4 + 0.2j, -0.3j, 0.7, -0.2 + 0.1j])
    cell_width = 1.0
    difference = positions[:, None] - positions[None, :]
    triangular = np.maximum(1.0 - np.abs(difference) / cell_width, 0.0)
    fejer_energy = float(
        np.real(np.conjugate(coefficients) @ triangular @ coefficients)
    )

    # Midpoint quadrature is exact up to boundary cells and converges rapidly.
    sample_count = 20000
    shifts = (np.arange(sample_count) + 0.5) * cell_width / sample_count
    cell_energies = []
    for shift in shifts:
        cells = np.floor((positions - shift) / cell_width).astype(int)
        energy = 0.0
        for cell in np.unique(cells):
            total = coefficients[cells == cell].sum()
            energy += abs(total) ** 2
        cell_energies.append(energy)
    averaged_energy = float(np.mean(cell_energies))

    assert abs(averaged_energy - fejer_energy) <= 2.0e-4
    assert min(cell_energies) <= fejer_energy + 1.0e-12
    assert np.linalg.eigvalsh(triangular).min() >= -1.0e-12


def test_convex_randomization_no_gain() -> None:
    point = np.array([-0.4, 0.6, 1.2])
    predictors = np.array(
        [
            [0.0, 0.2, 1.0],
            [0.3, 0.9, 1.5],
            [0.1, 0.5, 0.8],
        ]
    )
    barycenter = predictors.mean(axis=0)
    expected_loss = np.mean(
        np.sum((predictors - point[None, :]) ** 2, axis=1)
    )
    bias = np.sum((barycenter - point) ** 2)
    variance = np.mean(
        np.sum((predictors - barycenter[None, :]) ** 2, axis=1)
    )
    assert np.all(predictors >= 0.0)
    assert np.all(barycenter >= 0.0)
    assert abs(expected_loss - bias - variance) <= 1.0e-14
    assert expected_loss >= bias


def local_occupancy(points: np.ndarray, width: float) -> int:
    ordered = np.sort(points)
    best = 0
    right = 0
    for left in range(len(ordered)):
        right = max(right, left)
        while right < len(ordered) and ordered[right] - ordered[left] < width:
            right += 1
        best = max(best, right - left)
    return best


def test_fejer_occupancy_capacity() -> None:
    positions = np.array([-0.2, 0.0, 0.08, 0.22, 0.9, 1.02, 1.08])
    width = 0.5
    difference = positions[:, None] - positions[None, :]
    gram = np.maximum(1.0 - np.abs(difference) / width, 0.0)
    largest = np.linalg.eigvalsh(gram).max()
    occupancy = local_occupancy(positions, width)
    half_occupancy = local_occupancy(positions, width / 2.0)

    assert largest <= occupancy + 1.0e-12
    assert largest + 1.0e-12 >= half_occupancy / 2.0

    # The normalized constant packet on a densest half-width interval
    # realizes the lower-bound mechanism.
    ordered = np.sort(positions)
    for left in range(len(ordered)):
        selected = np.flatnonzero(
            (positions >= ordered[left])
            & (positions < ordered[left] + width / 2.0)
        )
        if len(selected) == half_occupancy:
            packet = np.zeros(len(positions))
            packet[selected] = 1.0 / np.sqrt(half_occupancy)
            assert packet @ gram @ packet >= half_occupancy / 2.0 - 1.0e-12
            break
    else:
        raise AssertionError("failed to locate a densest half-width interval")


def test_dyadic_logarithmic_occupancy() -> None:
    size = 200
    width = 0.12
    positions = np.log(np.arange(size, 2 * size, dtype=float))
    occupancy = local_occupancy(positions, width)
    half_occupancy = local_occupancy(positions, width / 2.0)
    difference = positions[:, None] - positions[None, :]
    gram = np.maximum(1.0 - np.abs(difference) / width, 0.0)
    largest = np.linalg.eigvalsh(gram).max()

    assert occupancy <= 1.0 + 4.0 * size * width
    assert half_occupancy >= max(1.0, size * width / 2.0 - 1.0)
    assert largest <= 1.0 + 4.0 * size * width + 1.0e-10
    assert largest >= max(0.5, size * width / 4.0 - 0.5) - 1.0e-10


def main() -> None:
    test_atomic_kkt_certificate()
    test_rank_one_gram_separator()
    test_inserted_hodge_transgression()
    test_face_weight_commutator_ledger()
    test_spectral_density_only_no_go()
    test_random_grid_fejer_identity()
    test_convex_randomization_no_gain()
    test_fejer_occupancy_capacity()
    test_dyadic_logarithmic_occupancy()
    print("finite cone and Hodge-transgression checks passed")


if __name__ == "__main__":
    main()

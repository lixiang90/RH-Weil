"""Explore the prolate candidate k_lambda and its canonical correction.

The angular prolate operator is represented in the orthonormal Legendre
basis. This avoids a SciPy dependency and makes the endpoint and inversion
defects in notes/007 directly reproducible. It is an exploratory
floating-point calculation, not an interval certificate.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import legval
from numpy.polynomial.legendre import leggauss


@dataclass
class ProlateCandidate:
    lam: float
    degrees: np.ndarray
    coefficients: np.ndarray
    eigenvalues: tuple[float, float]
    chis: tuple[float, float]

    def psi(self, z: np.ndarray | float) -> np.ndarray:
        standard = np.zeros(int(self.degrees[-1]) + 1)
        standard[self.degrees] = self.coefficients * np.sqrt(
            (2 * self.degrees + 1) / 2
        )
        return legval(z, standard)

    def k_value(self, u: float) -> float:
        """E(h_lambda)(u), with h_lambda extended by zero."""
        maximum = int(math.floor(self.lam / u + 1e-12))
        if maximum < 1:
            return 0.0
        n = np.arange(1, maximum + 1, dtype=float)
        z = n * u / self.lam
        return float(math.sqrt(u / self.lam) * np.sum(self.psi(z)))

    @property
    def upper_endpoint(self) -> float:
        return float(self.psi(1.0))

    @property
    def lower_endpoint(self) -> float:
        return self.k_value(1 / self.lam)

    @property
    def boundary_average(self) -> float:
        return (self.lower_endpoint + self.upper_endpoint) / 2


def _multiplication_by_z(size: int) -> np.ndarray:
    """Matrix of z in the orthonormal Legendre basis phi_l."""
    matrix = np.zeros((size, size))
    for degree in range(size - 1):
        value = (degree + 1) / math.sqrt(
            (2 * degree + 1) * (2 * degree + 3)
        )
        matrix[degree, degree + 1] = value
        matrix[degree + 1, degree] = value
    return matrix


def build_candidate(lam: float, basis_size: int = 80) -> ProlateCandidate:
    """Build the zero-integral combination of prolate modes n=0 and n=4."""
    if lam <= 1:
        raise ValueError("lambda must exceed 1")
    if basis_size < 8:
        raise ValueError("basis_size must be at least 8")

    degrees = np.arange(0, 2 * basis_size, 2)
    # Include degree 2*basis_size so multiplication by z twice is exact on
    # the retained block before the final Galerkin projection.
    full_size = 2 * basis_size + 2
    z_matrix = _multiplication_by_z(full_size)
    z_squared = z_matrix @ z_matrix
    even_z_squared = z_squared[np.ix_(degrees, degrees)]
    gamma = 2 * math.pi * lam**2
    operator = np.diag(degrees * (degrees + 1)) + gamma**2 * even_z_squared
    eigenvalues, eigenvectors = np.linalg.eigh(operator)

    mode_zero = eigenvectors[:, 0].copy()
    mode_four = eigenvectors[:, 2].copy()

    def at_origin(vector: np.ndarray) -> float:
        standard = np.zeros(int(degrees[-1]) + 1)
        standard[degrees] = vector * np.sqrt((2 * degrees + 1) / 2)
        return float(legval(0.0, standard))

    if at_origin(mode_zero) < 0:
        mode_zero *= -1
    if at_origin(mode_four) < 0:
        mode_four *= -1

    # Integral of phi_0 over [-1,1] is sqrt(2); all higher Legendre modes
    # integrate to zero.
    integral_zero = math.sqrt(2) * mode_zero[0]
    integral_four = math.sqrt(2) * mode_four[0]
    combination = integral_four * mode_zero - integral_zero * mode_four
    combination /= np.linalg.norm(combination)

    chi_zero = lam * integral_zero / at_origin(mode_zero)
    chi_four = lam * integral_four / at_origin(mode_four)
    return ProlateCandidate(
        lam=lam,
        degrees=degrees,
        coefficients=combination,
        eigenvalues=(float(eigenvalues[0]), float(eigenvalues[2])),
        chis=(float(chi_zero), float(chi_four)),
    )


def build_near_radical_trial_family(
    lam: float, dimension: int = 3, basis_size: int = 80
) -> list[ProlateCandidate]:
    """Build a stable positive-Fourier prolate near-radical subspace.

    The first ``dimension + 1`` angular prolate modes in the positive
    Fourier-sign branch (indices 0, 4, 8, ...) are intersected with the
    stable condition integral(h)=0.  On an exact positive Fourier eigenspace
    this is the same as h(0)=0; for compressed prolate modes their difference
    is the exponentially small defect isolated in Lemma AL.  Enforcing both
    nearly dependent rows numerically is exponentially ill-conditioned, so
    the separate fixed-bump h(0) correction is intentionally not hidden
    here.  This is a float64 diagnostic, not an interval certificate.
    """
    if lam <= 1:
        raise ValueError("lambda must exceed 1")
    if dimension < 1:
        raise ValueError("dimension must be positive")
    number_modes = dimension + 1
    mode_indices = np.arange(0, 2 * number_modes, 2)
    if basis_size <= int(mode_indices[-1]):
        raise ValueError("basis_size is too small for the requested family")

    degrees = np.arange(0, 2 * basis_size, 2)
    full_size = 2 * basis_size + 2
    z_matrix = _multiplication_by_z(full_size)
    even_z_squared = (z_matrix @ z_matrix)[np.ix_(degrees, degrees)]
    gamma = 2 * math.pi * lam**2
    operator = np.diag(degrees * (degrees + 1)) + gamma**2 * even_z_squared
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    modes = eigenvectors[:, mode_indices].copy()

    origin_values = np.empty(number_modes)
    for j in range(number_modes):
        standard = np.zeros(int(degrees[-1]) + 1)
        standard[degrees] = modes[:, j] * np.sqrt((2 * degrees + 1) / 2)
        origin_values[j] = float(legval(0.0, standard))
        if origin_values[j] < 0:
            modes[:, j] *= -1
            origin_values[j] *= -1

    integral_values = math.sqrt(2) * modes[0, :]
    constraint = integral_values[None, :]
    constraint /= np.linalg.norm(constraint)
    _, _, right_vectors = np.linalg.svd(constraint, full_matrices=True)
    null_coordinates = right_vectors[1:, :].T

    family: list[ProlateCandidate] = []
    for j in range(dimension):
        coefficients = modes @ null_coordinates[:, j]
        coefficients /= np.linalg.norm(coefficients)
        family.append(
            ProlateCandidate(
                lam=lam,
                degrees=degrees,
                coefficients=coefficients,
                eigenvalues=(
                    float(eigenvalues[0]),
                    float(eigenvalues[int(mode_indices[-1])]),
                ),
                chis=(math.nan, math.nan),
            )
        )
    return family


def _mp_legendre_values(z: mp.mpf, maximum: int) -> list[mp.mpf]:
    values = [mp.mpf(1)]
    if maximum == 0:
        return values
    values.append(z)
    for degree in range(2, maximum + 1):
        values.append(
            ((2 * degree - 1) * z * values[-1] - (degree - 1) * values[-2])
            / degree
        )
    return values


def high_precision_diagnostics(
    lam: mp.mpf, basis_size: int = 40, dps: int = 80
) -> dict[str, mp.mpf]:
    """Resolve endpoint defects below float64 using a tridiagonal mp matrix."""
    mp.mp.dps = dps

    def a_value(degree: int) -> mp.mpf:
        if degree < 0:
            return mp.mpf(0)
        return (degree + 1) / mp.sqrt(
            (2 * degree + 1) * (2 * degree + 3)
        )

    gamma = 2 * mp.pi * lam**2
    operator = mp.matrix(basis_size, basis_size)
    for index in range(basis_size):
        degree = 2 * index
        z2_diagonal = a_value(degree) ** 2 + a_value(degree - 1) ** 2
        operator[index, index] = degree * (degree + 1) + gamma**2 * z2_diagonal
        if index + 1 < basis_size:
            off_diagonal = gamma**2 * a_value(degree) * a_value(degree + 1)
            operator[index, index + 1] = off_diagonal
            operator[index + 1, index] = off_diagonal

    eigenvalues, eigenvectors = mp.eigsy(operator)
    mode_zero = [eigenvectors[index, 0] for index in range(basis_size)]
    mode_four = [eigenvectors[index, 2] for index in range(basis_size)]

    def evaluate(vector: list[mp.mpf], z: mp.mpf) -> mp.mpf:
        polynomials = _mp_legendre_values(z, 2 * (basis_size - 1))
        return mp.fsum(
            vector[index]
            * mp.sqrt((2 * degree + 1) / 2)
            * polynomials[degree]
            for index, degree in enumerate(range(0, 2 * basis_size, 2))
        )

    if evaluate(mode_zero, mp.mpf(0)) < 0:
        mode_zero = [-value for value in mode_zero]
    if evaluate(mode_four, mp.mpf(0)) < 0:
        mode_four = [-value for value in mode_four]

    integral_zero = mp.sqrt(2) * mode_zero[0]
    integral_four = mp.sqrt(2) * mode_four[0]
    combination = [
        integral_four * mode_zero[index] - integral_zero * mode_four[index]
        for index in range(basis_size)
    ]
    norm = mp.sqrt(mp.fsum(value**2 for value in combination))
    combination = [value / norm for value in combination]

    upper = evaluate(combination, mp.mpf(1))
    maximum = int(mp.floor(lam**2 + mp.mpf("1e-40")))
    lower = mp.fsum(
        evaluate(combination, mp.mpf(n) / lam**2)
        for n in range(1, maximum + 1)
    ) / lam
    boundary = (lower + upper) / 2
    chi_zero = lam * integral_zero / evaluate(mode_zero, mp.mpf(0))
    chi_four = lam * integral_four / evaluate(mode_four, mp.mpf(0))
    return {
        "eigenvalue_0": eigenvalues[0],
        "eigenvalue_4": eigenvalues[2],
        "chi_0": chi_zero,
        "chi_4": chi_four,
        "chi_difference": chi_four - chi_zero,
        "integral_residual": mp.sqrt(2) * combination[0],
        "lower_endpoint": lower,
        "upper_endpoint": upper,
        "boundary_average": boundary,
    }


def candidate_diagnostics(
    candidate: ProlateCandidate, grid_size: int = 1001
) -> dict[str, float]:
    if grid_size < 3 or grid_size % 2 == 0:
        raise ValueError("grid_size must be an odd integer at least 3")
    ell = math.log(candidate.lam)
    y = np.linspace(-ell, ell, grid_size)
    raw = np.array([candidate.k_value(math.exp(value)) for value in y])
    reflected = raw[::-1]
    even = (raw + reflected) / 2
    boundary = candidate.boundary_average
    corrected = even - boundary

    raw_norm = math.sqrt(float(np.trapezoid(raw**2, y)))
    odd_norm = math.sqrt(float(np.trapezoid(((raw - reflected) / 2) ** 2, y)))
    correction_norm = math.sqrt(float(np.trapezoid((corrected - raw) ** 2, y)))
    return {
        "raw_norm": raw_norm,
        "odd_norm": odd_norm,
        "relative_odd_norm": odd_norm / raw_norm,
        "correction_norm": correction_norm,
        "relative_correction_norm": correction_norm / raw_norm,
        "corrected_endpoint_max": max(abs(corrected[0]), abs(corrected[-1])),
        "corrected_inversion_max": float(np.max(np.abs(corrected - corrected[::-1]))),
    }


def corrected_fourier_coefficients(
    candidate: ProlateCandidate,
    cutoff: int,
    quadrature_order: int = 48,
    enforce_boundary: bool = True,
) -> tuple[dict[int, mp.mpf], dict[str, mp.mpf]]:
    """Fourier-project the even, endpoint-zero correction from notes/007."""
    if cutoff < 0:
        raise ValueError("cutoff must be nonnegative")
    if quadrature_order < 8:
        raise ValueError("quadrature_order must be at least 8")
    length = 2 * math.log(candidate.lam)
    mu = candidate.lam**2
    maximum = int(math.floor(mu + 1e-12))
    breakpoints = {0.0, length}
    for n in range(1, maximum + 1):
        point = math.log(mu / n)
        if 0 < point < length:
            breakpoints.add(point)
    points = sorted(breakpoints)
    nodes, weights = leggauss(quadrature_order)
    boundary = candidate.boundary_average
    coefficients = {n: 0.0j for n in range(-cutoff, cutoff + 1)}

    for left, right in zip(points[:-1], points[1:]):
        midpoint = (left + right) / 2
        half_width = (right - left) / 2
        x_values = midpoint + half_width * nodes
        raw = np.array(
            [candidate.k_value(math.exp(x) / candidate.lam) for x in x_values]
        )
        reflected = np.array(
            [candidate.k_value(candidate.lam / math.exp(x)) for x in x_values]
        )
        corrected = (raw + reflected) / 2 - boundary
        for n in coefficients:
            phase = np.exp(-2j * math.pi * n * x_values / length)
            coefficients[n] += (
                half_width * np.dot(weights, corrected * phase) / math.sqrt(length)
            )

    # Enforce the exact algebraic conditions used by Theorem V. Numerical
    # quadrature already makes the coefficients real and even to high
    # accuracy; averaging removes the irrelevant roundoff asymmetry.
    mp_coefficients: dict[int, mp.mpf] = {}
    for n in range(1, cutoff + 1):
        averaged = (
            coefficients[n].real + coefficients[-n].real
        ) / 2
        mp_coefficients[n] = mp.mpf(str(averaged))
        mp_coefficients[-n] = mp_coefficients[n]
    mp_coefficients[0] = mp.mpf(str(coefficients[0].real))
    raw_norm = mp.sqrt(
        mp.fsum(abs(value) ** 2 for value in mp_coefficients.values())
    )
    raw_normalized = {
        n: value / raw_norm for n, value in mp_coefficients.items()
    }
    boundary_before = mp.fsum(raw_normalized.values())

    if enforce_boundary:
        boundary_unnormalized = mp.fsum(mp_coefficients.values())
        mp_coefficients[0] -= boundary_unnormalized
    norm = mp.sqrt(mp.fsum(abs(value) ** 2 for value in mp_coefficients.values()))
    output = {n: value / norm for n, value in mp_coefficients.items()}
    correction_distance = mp.sqrt(
        mp.fsum(
            abs(output[n] - raw_normalized[n]) ** 2 for n in output
        )
    )
    metadata = {
        "projection_boundary_before": boundary_before,
        "boundary_correction_distance": correction_distance,
    }
    return output, metadata


def finite_even_cluster_diagnostics(
    family: list[ProlateCandidate],
    fourier_cutoff: int,
    quadrature_order: int = 48,
    dps: int = 50,
    reference: ProlateCandidate | None = None,
    target_dimension: int | None = None,
) -> dict[str, mp.mpf]:
    """Compare an energy-adapted prolate Ritz space with the low spectrum.

    All spectral and principal-angle quantities here are exploratory
    float64 diagnostics.  The Weil entries themselves are first evaluated
    with mpmath so this routine uses the same formulas as the rigorous-tail
    experiments.
    """
    if not family:
        raise ValueError("family must be nonempty")
    if fourier_cutoff < len(family):
        raise ValueError("fourier_cutoff must be at least the family dimension")
    library_dimension = len(family)
    dimension = library_dimension if target_dimension is None else target_dimension
    if not 1 <= dimension <= library_dimension:
        raise ValueError("target_dimension must lie between one and family size")
    lam = family[0].lam
    if any(abs(item.lam - lam) > 10 * np.finfo(float).eps * lam for item in family):
        raise ValueError("all trial functions must have the same lambda")

    from qw_matrix import build_parity_blocks_mp

    columns: list[np.ndarray] = []
    for item in family:
        coefficients, _ = corrected_fourier_coefficients(
            item,
            fourier_cutoff,
            quadrature_order,
            enforce_boundary=True,
        )
        column = np.empty(fourier_cutoff + 1)
        column[0] = float(coefficients[0])
        for n in range(1, fourier_cutoff + 1):
            column[n] = math.sqrt(2) * float(coefficients[n])
        columns.append(column)
    trial_matrix = np.column_stack(columns)
    trial_basis, triangular = np.linalg.qr(trial_matrix, mode="reduced")
    if np.min(np.abs(np.diag(triangular))) <= 1e-12:
        raise ArithmeticError("projected trial family is numerically rank deficient")

    mp.mp.dps = dps
    even_block_mp, _ = build_parity_blocks_mp(mp.mpf(str(lam)), fourier_cutoff)
    eigenvalues_mp, eigenvectors_mp = mp.eigsy(even_block_mp)
    eigenvectors = np.array(
        [
            [float(eigenvectors_mp[i, j]) for j in range(fourier_cutoff + 1)]
            for i in range(fourier_cutoff + 1)
        ]
    )
    low_basis = eigenvectors[:, :dimension]
    trial_basis_mp = mp.matrix(
        [
            [mp.mpf(str(trial_basis[i, j])) for j in range(library_dimension)]
            for i in range(fourier_cutoff + 1)
        ]
    )
    compression_mp = trial_basis_mp.T * even_block_mp * trial_basis_mp
    ritz_values_mp, ritz_vectors_mp = mp.eigsy(compression_mp)
    selected_ritz_vectors_mp = mp.matrix(library_dimension, dimension)
    for i in range(library_dimension):
        for j in range(dimension):
            selected_ritz_vectors_mp[i, j] = ritz_vectors_mp[i, j]
    ritz_basis_mp = trial_basis_mp * selected_ritz_vectors_mp
    ritz_basis = np.array(
        [
            [float(ritz_basis_mp[i, j]) for j in range(dimension)]
            for i in range(fourier_cutoff + 1)
        ]
    )
    singular_values = np.linalg.svd(
        low_basis.T @ ritz_basis, compute_uv=False
    )
    squared_cosines = singular_values**2
    selected_ritz_values_mp = mp.diag(
        [ritz_values_mp[j] for j in range(dimension)]
    )
    residual_mp = (
        even_block_mp * ritz_basis_mp
        - ritz_basis_mp * selected_ritz_values_mp
    )
    residual_frobenius = mp.sqrt(
        mp.fsum(
            abs(residual_mp[i, j]) ** 2
            for i in range(residual_mp.rows)
            for j in range(residual_mp.cols)
        )
    )
    residual_gram = residual_mp.T * residual_mp
    residual_squares, _ = mp.eigsy(residual_gram)

    result = {
        "cluster_dimension": mp.mpf(dimension),
        "cluster_library_dimension": mp.mpf(library_dimension),
        "cluster_max_input_integral_defect": mp.mpf(
            str(
                max(
                    abs(math.sqrt(2) * item.coefficients[0])
                    for item in family
                )
            )
        ),
        "cluster_max_input_origin_defect": mp.mpf(
            str(max(abs(float(item.psi(0.0))) for item in family))
        ),
        "cluster_chordal_leakage_squared": mp.mpf(
            str(float(dimension - np.sum(squared_cosines)))
        ),
        "cluster_max_sine_squared": mp.mpf(
            str(float(1 - np.min(squared_cosines)))
        ),
        "cluster_min_principal_cosine_squared": mp.mpf(
            str(float(np.min(squared_cosines)))
        ),
        "cluster_ritz_residual_frobenius": residual_frobenius,
        "cluster_ritz_residual_operator": mp.sqrt(
            residual_squares[residual_squares.rows - 1]
        ),
        "cluster_exact_external_gap": (
            eigenvalues_mp[dimension] - eigenvalues_mp[dimension - 1]
        ),
    }
    for j in range(dimension + 1):
        result[f"cluster_exact_eigenvalue_{j}"] = eigenvalues_mp[j]
    for j in range(dimension):
        result[f"cluster_ritz_eigenvalue_{j}"] = ritz_values_mp[j]
        result[f"cluster_ritz_residual_vector_{j}"] = mp.sqrt(
            mp.fsum(
                abs(residual_mp[i, j]) ** 2
                for i in range(residual_mp.rows)
            )
        )
        result[f"cluster_ritz_ground_overlap_{j}"] = mp.mpf(
            str(float(abs(eigenvectors[:, 0] @ ritz_basis[:, j]) ** 2))
        )
    for j, value in enumerate(np.sort(squared_cosines)):
        result[f"cluster_principal_cosine_squared_{j}"] = mp.mpf(str(value))

    if reference is not None:
        coefficients, _ = corrected_fourier_coefficients(
            reference,
            fourier_cutoff,
            quadrature_order,
            enforce_boundary=True,
        )
        vector = np.empty(fourier_cutoff + 1)
        vector[0] = float(coefficients[0])
        for n in range(1, fourier_cutoff + 1):
            vector[n] = math.sqrt(2) * float(coefficients[n])
        vector /= np.linalg.norm(vector)
        result["reference_trial_space_overlap"] = mp.mpf(
            str(float(np.linalg.norm(trial_basis.T @ vector) ** 2))
        )
        result["reference_ritz_space_overlap"] = mp.mpf(
            str(float(np.linalg.norm(ritz_basis.T @ vector) ** 2))
        )
        for j in range(dimension):
            result[f"reference_ritz_vector_overlap_{j}"] = mp.mpf(
                str(float(abs(ritz_basis[:, j] @ vector) ** 2))
            )
        result["reference_exact_low_cluster_overlap"] = mp.mpf(
            str(float(np.linalg.norm(low_basis.T @ vector) ** 2))
        )
        result["reference_exact_ground_overlap"] = mp.mpf(
            str(float(abs(eigenvectors[:, 0] @ vector) ** 2))
        )
    return result


def qw_residual_diagnostics(
    candidate: ProlateCandidate,
    fourier_cutoff: int,
    buffer_cutoff: int,
    phase_cutoff: int | None = None,
    resolvent_order: int = 6,
    quadrature_order: int = 48,
    dps: int = 50,
    enforce_boundary: bool = True,
) -> dict[str, mp.mpf]:
    """Insert the corrected prolate projection into the Weil matrix."""
    if buffer_cutoff < max(1, 2 * fourier_cutoff):
        raise ValueError("buffer_cutoff must be at least 2*fourier_cutoff")
    from qw_matrix import (
        all_orders_candidate_tail_certificate,
        boundary_vanishing_candidate_tail_bound,
        candidate_fourth_order_coefficient,
        candidate_leading_coefficient,
        finite_phase_third_order_candidate_tail_bound,
        fourth_order_candidate_tail_bound,
        qw_entry,
        second_order_candidate_tail_bound,
        third_order_candidate_tail_bound,
        third_order_oscillatory_coefficient,
        weighted_candidate_tail_bound,
    )

    mp.mp.dps = dps
    coefficients, projection_metadata = corrected_fourier_coefficients(
        candidate,
        fourier_cutoff,
        quadrature_order,
        enforce_boundary=enforce_boundary,
    )
    length = 2 * mp.log(mp.mpf(str(candidate.lam)))
    cache: dict[tuple[int, int], mp.mpf] = {}

    def entry(m: int, n: int) -> mp.mpf:
        key = (min(m, n), max(m, n))
        if key not in cache:
            cache[key] = qw_entry(key[0], key[1], length)
        return cache[key]

    mu = mp.fsum(
        coefficients[m] * entry(m, n) * coefficients[n]
        for m in coefficients
        for n in coefficients
    )
    core_squared = mp.mpf(0)
    buffer_squared = mp.mpf(0)
    for m in range(-buffer_cutoff, buffer_cutoff + 1):
        component = mp.fsum(
            entry(m, n) * value for n, value in coefficients.items()
        ) - mu * coefficients.get(m, mp.mpf(0))
        if abs(m) <= fourier_cutoff:
            core_squared += abs(component) ** 2
        else:
            buffer_squared += abs(component) ** 2
    generic_tail = weighted_candidate_tail_bound(
        coefficients, buffer_cutoff, length
    )
    accelerated_tail = (
        boundary_vanishing_candidate_tail_bound(
            coefficients, buffer_cutoff, length
        )
        if enforce_boundary
        else mp.inf
    )
    chosen_tail = min(generic_tail, accelerated_tail)

    leading = candidate_leading_coefficient(coefficients, length)
    second_order_tail = (
        second_order_candidate_tail_bound(
            coefficients, buffer_cutoff, length
        )
        if enforce_boundary
        else mp.inf
    )
    third_order_tail = (
        third_order_candidate_tail_bound(
            coefficients, buffer_cutoff, length
        )
        if enforce_boundary
        else mp.inf
    )
    finite_phase_tail = (
        finite_phase_third_order_candidate_tail_bound(
            coefficients,
            buffer_cutoff,
            phase_cutoff,
            length,
        )
        if enforce_boundary and phase_cutoff is not None
        else mp.inf
    )
    fourth_order_tail = (
        fourth_order_candidate_tail_bound(
            coefficients,
            buffer_cutoff,
            phase_cutoff,
            length,
        )
        if enforce_boundary and phase_cutoff is not None
        else mp.inf
    )
    resolvent_certificate = (
        all_orders_candidate_tail_certificate(
            coefficients,
            buffer_cutoff,
            phase_cutoff,
            resolvent_order,
            length,
        )
        if enforce_boundary and phase_cutoff is not None
        else {"tail_bound": mp.inf}
    )
    resolvent_tail = resolvent_certificate["tail_bound"]
    chosen_tail = min(
        chosen_tail,
        second_order_tail,
        third_order_tail,
        finite_phase_tail,
        fourth_order_tail,
        resolvent_tail,
    )
    fourth = candidate_fourth_order_coefficient(coefficients, length)
    edge_third = third_order_oscillatory_coefficient(
        coefficients, buffer_cutoff, length
    )
    edge_component = mp.fsum(
        entry(buffer_cutoff, n) * value
        for n, value in coefficients.items()
    )
    even_block = mp.matrix(fourier_cutoff + 1)
    even_block[0, 0] = entry(0, 0)
    for n in range(1, fourier_cutoff + 1):
        even_block[0, n] = mp.sqrt(2) * entry(0, n)
        even_block[n, 0] = even_block[0, n]
        for m in range(1, n + 1):
            value = entry(n, m) + entry(n, -m)
            even_block[n, m] = value
            even_block[m, n] = value
    even_values, even_vectors = mp.eigsy(even_block)
    even_coordinates = mp.matrix(fourier_cutoff + 1, 1)
    even_coordinates[0] = coefficients[0]
    for n in range(1, fourier_cutoff + 1):
        even_coordinates[n] = mp.sqrt(2) * coefficients[n]
    even_overlaps = [
        abs(
            mp.fsum(
                even_vectors[n, j] * even_coordinates[n]
                for n in range(fourier_cutoff + 1)
            )
        )
        ** 2
        for j in range(fourier_cutoff + 1)
    ]
    best_even_index = max(
        range(fourier_cutoff + 1), key=lambda j: even_overlaps[j]
    )
    return {
        **projection_metadata,
        "boundary_sum": mp.fsum(coefficients.values()),
        "coefficient_norm": mp.sqrt(
            mp.fsum(abs(value) ** 2 for value in coefficients.values())
        ),
        "rayleigh": mu,
        "core_residual_squared": core_squared,
        "buffer_residual_squared": buffer_squared,
        "generic_tail": generic_tail,
        "accelerated_tail": accelerated_tail,
        "second_order_tail": second_order_tail,
        "third_order_tail": third_order_tail,
        "finite_phase_third_order_tail": finite_phase_tail,
        "fourth_order_tail": fourth_order_tail,
        **{
            f"resolvent_{key}": value
            for key, value in resolvent_certificate.items()
        },
        "pole_leading_coefficient": leading["pole"],
        "arch_leading_coefficient": leading["arch"],
        "prime_leading_coefficient": leading["prime"],
        "combined_leading_coefficient": leading["combined"],
        "pole_fourth_order_coefficient": fourth["pole"],
        "arch_fourth_order_coefficient": fourth["arch"],
        "prime_fourth_order_coefficient": fourth["prime"],
        "combined_fourth_order_coefficient": fourth["combined"],
        "buffer_edge_B_m": edge_third,
        "buffer_edge_m2_asymptotic": (
            leading["combined"] + edge_third / buffer_cutoff
        ),
        "buffer_edge_m2_fourth_asymptotic": (
            leading["combined"]
            + edge_third / buffer_cutoff
            + fourth["combined"] / buffer_cutoff**2
        ),
        "buffer_edge_m2_residual": buffer_cutoff**2 * edge_component,
        "finite_even_lowest": even_values[0],
        "finite_even_second": (
            even_values[1] if fourier_cutoff >= 1 else mp.inf
        ),
        "finite_even_eigenvalues_below_rayleigh": sum(
            1 for value in even_values if value < mu
        ),
        "finite_even_ground_overlap": even_overlaps[0],
        "finite_even_best_overlap_index": mp.mpf(best_even_index),
        "finite_even_best_overlap": even_overlaps[best_even_index],
        "finite_even_best_eigenvalue": even_values[best_even_index],
        "residual_lower": mp.sqrt(core_squared + buffer_squared),
        "residual_upper": mp.sqrt(
            core_squared + buffer_squared + chosen_tail
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=float, default=math.sqrt(13))
    parser.add_argument(
        "--mu",
        type=str,
        help="set lambda=sqrt(mu), preserving an exact decimal mu in mp mode",
    )
    parser.add_argument("--basis", type=int, default=80)
    parser.add_argument("--grid", type=int, default=1001)
    parser.add_argument("--high-precision", action="store_true")
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--fourier-cutoff", type=int)
    parser.add_argument("--buffer-cutoff", type=int)
    parser.add_argument(
        "--cluster-dimension",
        type=int,
        help=(
            "compare a positive-Fourier prolate near-radical trial space of "
            "this dimension with the lowest even Weil eigenspace"
        ),
    )
    parser.add_argument(
        "--cluster-library-dimension",
        type=int,
        help=(
            "number of near-radical directions before Weil-Ritz rotation; "
            "defaults to --cluster-dimension"
        ),
    )
    parser.add_argument(
        "--phase-cutoff",
        type=int,
        help="retain exact third-order oscillations through this index",
    )
    parser.add_argument(
        "--resolvent-order",
        type=int,
        default=6,
        help="Taylor order used to certify the exact rational far tail",
    )
    parser.add_argument("--quadrature-order", type=int, default=48)
    parser.add_argument(
        "--keep-projection-boundary",
        action="store_true",
        help="do not correct the finite Fourier coefficient sum",
    )
    parser.add_argument(
        "--tail-bound-only",
        action="store_true",
        help="skip the finite Weil residual matrix and print analytic tails",
    )
    args = parser.parse_args()
    lam_float = math.sqrt(float(args.mu)) if args.mu is not None else args.lam

    if args.high_precision:
        lam_mp = (
            mp.sqrt(mp.mpf(args.mu))
            if args.mu is not None
            else mp.mpf(str(args.lam))
        )
        result = high_precision_diagnostics(
            lam_mp, basis_size=args.basis, dps=args.dps
        )
        print(
            f"lambda={lam_float:.12g}, high-precision Legendre even "
            f"basis={args.basis}, dps={args.dps}"
        )
        for key, value in result.items():
            print(f"{key}:", mp.nstr(value, 30))
        print("exploratory only: no directed rounding")
        return

    if args.cluster_dimension is not None and args.fourier_cutoff is None:
        parser.error("--cluster-dimension requires --fourier-cutoff")
    if (
        args.cluster_library_dimension is not None
        and args.cluster_dimension is None
    ):
        parser.error("--cluster-library-dimension requires --cluster-dimension")
    if (
        args.cluster_library_dimension is not None
        and args.cluster_library_dimension < args.cluster_dimension
    ):
        parser.error("cluster library dimension must be at least target dimension")
    if (
        args.cluster_dimension is None
        and (args.fourier_cutoff is None) != (args.buffer_cutoff is None)
    ):
        parser.error(
            "--fourier-cutoff and --buffer-cutoff must be supplied together"
        )
    if args.phase_cutoff is not None and args.buffer_cutoff is None:
        parser.error("--phase-cutoff requires --buffer-cutoff")
    if (
        args.phase_cutoff is not None
        and args.phase_cutoff < args.buffer_cutoff
    ):
        parser.error("--phase-cutoff must be at least --buffer-cutoff")

    candidate = build_candidate(lam_float, args.basis)
    if args.cluster_dimension is not None:
        library_dimension = (
            args.cluster_dimension
            if args.cluster_library_dimension is None
            else args.cluster_library_dimension
        )
        family = build_near_radical_trial_family(
            lam_float,
            dimension=library_dimension,
            basis_size=args.basis,
        )
        result = finite_even_cluster_diagnostics(
            family,
            args.fourier_cutoff,
            quadrature_order=args.quadrature_order,
            dps=args.dps,
            reference=candidate,
            target_dimension=args.cluster_dimension,
        )
        print(
            f"lambda={lam_float:.12g}, prolate near-radical cluster dimension="
            f"{args.cluster_dimension}, library dimension={library_dimension}, "
            f"Fourier cutoff={args.fourier_cutoff}"
        )
        for key, value in result.items():
            print(f"{key}:", mp.nstr(value, 24))
        print("exploratory only: nullspace, projection, and eigensolve use float64")
        return
    if args.fourier_cutoff is not None:
        if args.tail_bound_only:
            from qw_matrix import (
                all_orders_candidate_tail_certificate,
                boundary_vanishing_candidate_tail_bound,
                candidate_fourth_order_coefficient,
                candidate_leading_coefficient,
                finite_phase_third_order_candidate_tail_bound,
                fourth_order_candidate_tail_bound,
                second_order_candidate_tail_bound,
                third_order_candidate_tail_bound,
                third_order_oscillatory_coefficient,
                weighted_candidate_tail_bound,
            )

            mp.mp.dps = args.dps
            coefficients, metadata = corrected_fourier_coefficients(
                candidate,
                args.fourier_cutoff,
                args.quadrature_order,
                enforce_boundary=not args.keep_projection_boundary,
            )
            length = 2 * mp.log(mp.mpf(str(lam_float)))
            result = {
                **metadata,
                **{
                    f"leading_{key}": value
                    for key, value in candidate_leading_coefficient(
                        coefficients, length
                    ).items()
                },
                "generic_tail": weighted_candidate_tail_bound(
                    coefficients, args.buffer_cutoff, length
                ),
            }
            if not args.keep_projection_boundary:
                result["accelerated_tail"] = (
                    boundary_vanishing_candidate_tail_bound(
                        coefficients, args.buffer_cutoff, length
                    )
                )
                result["second_order_tail"] = second_order_candidate_tail_bound(
                    coefficients, args.buffer_cutoff, length
                )
                result["third_order_tail"] = third_order_candidate_tail_bound(
                    coefficients, args.buffer_cutoff, length
                )
                if args.phase_cutoff is not None:
                    result["finite_phase_third_order_tail"] = (
                        finite_phase_third_order_candidate_tail_bound(
                            coefficients,
                            args.buffer_cutoff,
                            args.phase_cutoff,
                            length,
                        )
                    )
                    result["fourth_order_tail"] = (
                        fourth_order_candidate_tail_bound(
                            coefficients,
                            args.buffer_cutoff,
                            args.phase_cutoff,
                            length,
                        )
                    )
                    result.update(
                        {
                            f"fourth_{key}": value
                            for key, value in candidate_fourth_order_coefficient(
                                coefficients, length
                            ).items()
                        }
                    )
                    result.update(
                        {
                            f"resolvent_{key}": value
                            for key, value in all_orders_candidate_tail_certificate(
                                coefficients,
                                args.buffer_cutoff,
                                args.phase_cutoff,
                                args.resolvent_order,
                                length,
                            ).items()
                        }
                    )
                edge_b = third_order_oscillatory_coefficient(
                    coefficients, args.buffer_cutoff, length
                )
                result["edge_B_m"] = edge_b
                result["edge_m2_asymptotic"] = (
                    result["leading_combined"]
                    + edge_b / args.buffer_cutoff
                )
                if args.phase_cutoff is not None:
                    result["edge_m2_fourth_asymptotic"] = (
                        result["edge_m2_asymptotic"]
                        + result["fourth_combined"]
                        / args.buffer_cutoff**2
                    )
            print(
                f"lambda={lam_float:.12g}, analytic prolate tail, Fourier "
                f"cutoff={args.fourier_cutoff}, tail cutoff={args.buffer_cutoff}"
            )
            for key, value in result.items():
                print(f"{key}:", mp.nstr(value, 24))
            print("exploratory only: prolate projection uses float64")
            return
        result = qw_residual_diagnostics(
            candidate,
            args.fourier_cutoff,
            args.buffer_cutoff,
            phase_cutoff=args.phase_cutoff,
            resolvent_order=args.resolvent_order,
            quadrature_order=args.quadrature_order,
            dps=args.dps,
            enforce_boundary=not args.keep_projection_boundary,
        )
        print(
            f"lambda={lam_float:.12g}, prolate Fourier cutoff="
            f"{args.fourier_cutoff}, Weil buffer={args.buffer_cutoff}"
        )
        for key, value in result.items():
            print(f"{key}:", mp.nstr(value, 24))
        print("exploratory only: prolate eigensolve/quadrature are float64")
        return
    diagnostics = candidate_diagnostics(candidate, args.grid)
    integral = math.sqrt(2) * candidate.coefficients[0]

    print(f"lambda={lam_float:.12g}, Legendre even basis={args.basis}")
    print("prolate eigenvalues n=0,4:", candidate.eigenvalues)
    print("finite-Fourier eigenvalues chi_0,chi_4:", candidate.chis)
    print("zero-integral combination residual:", f"{integral:.6e}")
    print("K_lambda(lambda^-1):", f"{candidate.lower_endpoint:.16e}")
    print("K_lambda(lambda):", f"{candidate.upper_endpoint:.16e}")
    print("boundary average b_lambda:", f"{candidate.boundary_average:.16e}")
    for key, value in diagnostics.items():
        print(f"{key}:", f"{value:.16e}")
    print("exploratory only: eigensolve and quadrature use float64")


if __name__ == "__main__":
    main()

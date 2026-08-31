"""Numerical finite-section matrices for the semilocal Weil form QW_lambda.

The formulas are (3.13), (4.1)--(4.4) of Connes--Consani--Moscovici,
"Zeta Spectral Triples" (arXiv:2511.22755v1).  This is an exploratory
calculator, not an interval-arithmetic certificate.
"""

from __future__ import annotations

import argparse
import bisect
import itertools
import math

import mpmath as mp
import numpy as np


def von_mangoldt(k: int) -> mp.mpf:
    """Return log(p) if k is a positive prime power, and 0 otherwise."""
    n = k
    prime = None
    p = 2
    while p * p <= n:
        if n % p == 0:
            prime = p
            while n % p == 0:
                n //= p
            if n != 1:
                return mp.mpf("0")
            return mp.log(p)
        p += 1 if p == 2 else 2
    if prime is None:  # k itself is prime
        return mp.log(k)
    return mp.log(prime)


def q_nm(x: mp.mpf, n: int, m: int, length: mp.mpf) -> mp.mpf:
    if n == m:
        return 2 * (1 - x / length) * mp.cos(2 * mp.pi * n * x / length)
    return (
        mp.sin(2 * mp.pi * m * x / length)
        - mp.sin(2 * mp.pi * n * x / length)
    ) / (mp.pi * (n - m))


def w02(n: int, m: int, length: mp.mpf) -> mp.mpf:
    numerator = (
        32
        * length
        * mp.sinh(length / 4) ** 2
        * (length**2 - 16 * mp.pi**2 * m * n)
    )
    denominator = (length**2 + 16 * mp.pi**2 * m**2) * (
        length**2 + 16 * mp.pi**2 * n**2
    )
    return numerator / denominator


def w_real(n: int, m: int, length: mp.mpf) -> mp.mpf:
    omega0 = mp.mpf(2 if n == m else 0)
    constant = omega0 / 2 * (
        mp.euler
        + mp.log(4 * mp.pi * (mp.e**length - 1) / (mp.e**length + 1))
    )

    def integrand(x: mp.mpf) -> mp.mpf:
        if abs(x) < mp.mpf("1e-30"):
            # q_nm'(0)=-2/L for every n,m.
            return omega0 / 4 - 1 / length
        omega = q_nm(x, n, m, length)
        return (mp.e ** (x / 2) * omega - omega0) / (
            mp.e**x - mp.e ** (-x)
        )

    return constant + mp.quad(integrand, [0, length])


def w_primes(n: int, m: int, length: mp.mpf) -> mp.mpf:
    total = mp.mpf("0")
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            total += (
                mangoldt
                * mp.power(k, mp.mpf("-0.5"))
                * q_nm(mp.log(k), n, m, length)
            )
    return total


def prime_mass(length: mp.mpf) -> mp.mpf:
    """P_lambda = sum_{2 <= k <= exp(L)} Lambda(k) / sqrt(k)."""
    total = mp.mpf("0")
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            total += mangoldt * mp.power(k, mp.mpf("-0.5"))
    return total


def weighted_prime_gap_average(length: mp.mpf, gap_test) -> mp.mpf:
    """Average a test function against the endpoint prime-gap measure.

    The gap coordinate is ``v = L - log(k)`` and the probability weights
    are proportional to ``Lambda(k) / sqrt(k)`` for ``k <= exp(L)``.
    Theorem DR of notes/030 proves weak convergence to the density
    ``exp(-v/2) / 2`` as ``L`` tends to infinity.
    """
    mass = prime_mass(length)
    if not mass:
        raise ValueError("the prime-gap measure is empty")
    total = mp.mpf("0")
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            gap = length - mp.log(k)
            total += mangoldt / mp.sqrt(k) * gap_test(gap)
    return total / mass


def smoothed_prime_gap_sum(endpoint: int, gap_test) -> mp.mpf:
    """Return the smoothed endpoint sum A_h(x) from Theorem DV."""
    if endpoint < 2:
        raise ValueError("endpoint must be at least 2")
    x = mp.mpf(endpoint)
    total = mp.mpf("0")
    for k in range(2, endpoint + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            total += (
                mangoldt / mp.sqrt(k) * gap_test(mp.log(x / k))
            )
    return total


def zeta_smoothed_gap_explicit_approximation(
    endpoint: int,
    laplace_transform,
    zero_count: int,
    trivial_count: int = 8,
) -> dict[str, mp.mpf | mp.mpc]:
    """Truncate the smoothed endpoint explicit formula of Theorem DV.

    ``mp.zetazero`` supplies positive critical-line zeros, so this routine is
    only a numerical transcription audit.  It must not be used as a proof of
    RH or as a rigorous remainder enclosure.
    """
    if endpoint < 2:
        raise ValueError("endpoint must be at least 2")
    if zero_count < 0 or trivial_count < 0:
        raise ValueError("truncation counts must be nonnegative")
    x = mp.mpf(endpoint)
    main = mp.sqrt(x) * laplace_transform(mp.mpf("0.5"))
    zero_terms = mp.fsum(
        2
        * mp.re(
            laplace_transform(mp.j * mp.im(mp.zetazero(index)))
            * x ** (mp.j * mp.im(mp.zetazero(index)))
        )
        for index in range(1, zero_count + 1)
    )
    trivial_terms = mp.fsum(
        laplace_transform(-2 * index - mp.mpf("0.5"))
        * x ** (-2 * index - mp.mpf("0.5"))
        for index in range(1, trivial_count + 1)
    )
    return {
        "main": main,
        "zero_terms": zero_terms,
        "trivial_terms": trivial_terms,
        "approximation": main - zero_terms - trivial_terms,
    }


def zeta_boundary_zero_gram(laplace_transforms, zero_count: int) -> mp.matrix:
    """Truncated RH spectral Gram matrix from Proposition EB.

    Positive and negative numerical critical-line zeros are included.  The
    routine assumes the tabulated zeros are simple and is an exploratory
    conjugation/sign check, not evidence for RH.
    """
    transforms = list(laplace_transforms)
    if zero_count < 0:
        raise ValueError("zero_count must be nonnegative")
    gram = mp.matrix(len(transforms), len(transforms))
    for index in range(1, zero_count + 1):
        ordinate = mp.im(mp.zetazero(index))
        for signed_ordinate in (ordinate, -ordinate):
            values = [
                transform(mp.j * signed_ordinate)
                for transform in transforms
            ]
            for row, row_value in enumerate(values):
                for column, column_value in enumerate(values):
                    gram[row, column] += (
                        row_value * mp.conj(column_value)
                    )
    return gram


def zeta_boundary_zero_abel_gram(
    laplace_transforms,
    zero_count: int,
    sigma: mp.mpf,
) -> mp.matrix:
    """Truncated Abel Gram of critical-line zero modes, equation (16).

    This numerical RH model omits the finite initial segment and trivial-zero
    corrections.  It checks the Abel Cauchy kernel, not the location of any
    uncomputed zero.
    """
    transforms = list(laplace_transforms)
    sigma = mp.mpf(sigma)
    if zero_count < 0:
        raise ValueError("zero_count must be nonnegative")
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    frequencies = []
    vectors = []
    for index in range(1, zero_count + 1):
        ordinate = mp.im(mp.zetazero(index))
        for frequency in (ordinate, -ordinate):
            frequencies.append(frequency)
            vectors.append(
                [transform(mp.j * frequency) for transform in transforms]
            )
    gram = mp.matrix(len(transforms), len(transforms))
    for frequency, values in zip(frequencies, vectors, strict=True):
        for other_frequency, other_values in zip(
            frequencies, vectors, strict=True
        ):
            kernel = 2 * sigma / (
                2 * sigma - mp.j * (frequency - other_frequency)
            )
            for row, row_value in enumerate(values):
                for column, column_value in enumerate(other_values):
                    gram[row, column] += (
                        kernel * row_value * mp.conj(column_value)
                    )
    return gram


def two_channel_hodge_lower_eigenvalue(
    left_diagonal: mp.mpf,
    right_diagonal: mp.mpf,
    off_diagonal: mp.mpf | mp.mpc,
) -> mp.mpf:
    """Exact lower eigenvalue of a Hermitian two-channel Hodge block."""
    left = mp.mpf(left_diagonal)
    right = mp.mpf(right_diagonal)
    off = mp.mpc(off_diagonal)
    return (
        left
        + right
        - mp.sqrt((left - right) ** 2 + 4 * abs(off) ** 2)
    ) / 2


def two_channel_schur_margin(
    left_diagonal: mp.mpf,
    right_diagonal: mp.mpf,
    off_diagonal: mp.mpf | mp.mpc,
    shift: mp.mpf,
) -> mp.mpf:
    """Determinant margin in Corollary EH after a scalar shift."""
    left_shifted = mp.mpf(left_diagonal) + mp.mpf(shift)
    right_shifted = mp.mpf(right_diagonal) + mp.mpf(shift)
    if left_shifted <= 0 or right_shifted <= 0:
        raise ValueError("shifted diagonal entries must be positive")
    return left_shifted * right_shifted - abs(off_diagonal) ** 2


def _power_interval_integral(
    left: mp.mpf, right: mp.mpf, exponent: mp.mpf
) -> mp.mpf:
    """Integrate x**exponent over one positive interval."""
    if abs(exponent + 1) < mp.mpf("1e-40"):
        return mp.log(right / left)
    return (
        right ** (exponent + 1) - left ** (exponent + 1)
    ) / (exponent + 1)


def chebyshev_abel_energy(endpoint: int, sigma: mp.mpf) -> mp.mpf:
    """Finite Chebyshev Abel energy I_sigma(X), equation (26).

    The integral is evaluated exactly on intervals where psi(x) is constant,
    up to the current mpmath arithmetic precision.
    """
    if endpoint < 2:
        raise ValueError("endpoint must be at least 2")
    sigma = mp.mpf(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    psi_value = mp.mpf("0")
    total = mp.mpf("0")
    power = 2 * sigma + 2
    for integer in range(1, endpoint):
        if integer >= 2:
            psi_value += von_mangoldt(integer)
        left = mp.mpf(integer)
        right = mp.mpf(integer + 1)
        total += (
            psi_value**2
            * _power_interval_integral(left, right, -power)
            - 2
            * psi_value
            * _power_interval_integral(left, right, 1 - power)
            + _power_interval_integral(left, right, 2 - power)
        )
    return 2 * sigma * total


def power_prefix_hodge_energy(
    charges: list[mp.mpf | mp.mpc],
    center_exponent: mp.mpf,
) -> mp.mpf:
    """Line-graph Hodge energy of a prefix flow with power weights."""
    if not charges:
        raise ValueError("at least one charge is required")
    center_exponent = mp.mpf(center_exponent)
    if center_exponent <= 0:
        raise ValueError("center_exponent must be positive")
    prefix = mp.mpc("0")
    total = mp.mpf("0")
    for index, charge in enumerate(charges, start=1):
        prefix += charge
        edge_weight = (
            mp.mpf(index) ** (-center_exponent)
            - mp.mpf(index + 1) ** (-center_exponent)
        ) / center_exponent
        total += edge_weight * abs(prefix) ** 2
    return total


def chebyshev_prefix_hodge_energy(endpoint: int) -> mp.mpf:
    """Exact critical prefix-flow energy through the interval [1, endpoint]."""
    if endpoint < 2:
        raise ValueError("endpoint must be at least two")
    charges = [
        von_mangoldt(integer) - 1
        for integer in range(1, endpoint)
    ]
    return power_prefix_hodge_energy(charges, mp.mpf("1"))


def chebyshev_prefix_log_block_energy(start: int, endpoint: int) -> mp.mpf:
    """Exact step-current Hodge energy on one finite logarithmic block."""
    if start < 1 or endpoint <= start:
        raise ValueError("require 1 <= start < endpoint")
    prefix = mp.mpf("0")
    total = mp.mpf("0")
    for integer in range(1, endpoint):
        prefix += von_mangoldt(integer) - 1
        if integer >= start:
            total += prefix**2 / (mp.mpf(integer) * (integer + 1))
    return total


def chebyshev_step_block_variance(start: int, endpoint: int) -> mp.mpf:
    """Exact integral of |psi(x)-floor(x)|^2 on an integer block."""
    if start < 1 or endpoint <= start:
        raise ValueError("require 1 <= start < endpoint")
    prefix = mp.mpf("0")
    total = mp.mpf("0")
    for integer in range(1, endpoint):
        prefix += von_mangoldt(integer) - 1
        if integer >= start:
            total += prefix**2
    return total


def chebyshev_step_block_charges(start: int, endpoint: int) -> list[mp.mpf]:
    """Boundary-compressed charges whose prefixes are the block discrepancies."""
    if start < 1 or endpoint <= start:
        raise ValueError("require 1 <= start < endpoint")
    boundary_prefix = mp.fsum(
        von_mangoldt(integer) - 1
        for integer in range(1, start + 1)
    )
    return [boundary_prefix] + [
        von_mangoldt(integer) - 1
        for integer in range(start + 1, endpoint)
    ]


def reverse_brownian_green_kernel(size: int) -> mp.matrix:
    """Green matrix K(i,j)=size-max(i,j) for a finite local prefix block."""
    if size < 1:
        raise ValueError("size must be positive")
    return mp.matrix(
        [
            [mp.mpf(size - max(left, right)) for right in range(size)]
            for left in range(size)
        ]
    )


def reverse_dirichlet_laplacian(size: int) -> mp.matrix:
    """Inverse of reverse_brownian_green_kernel."""
    if size < 1:
        raise ValueError("size must be positive")
    difference = mp.zeros(size, size)
    for index in range(size):
        difference[index, index] = 1
        if index > 0:
            difference[index, index - 1] = -1
    return difference * difference.transpose_conj()


def prefix_scalar_bridge_decomposition(
    charges: list[mp.mpf | mp.mpc],
) -> tuple[mp.mpf | mp.mpc, mp.mpf, mp.mpf]:
    """Split prefix-square energy into its constant mode and bridge variance."""
    if not charges:
        raise ValueError("at least one charge is required")
    prefix = mp.mpc("0")
    prefixes: list[mp.mpc] = []
    for charge in charges:
        prefix += charge
        prefixes.append(prefix)
    mean = mp.fsum(prefixes) / len(prefixes)
    scalar_energy = mp.mpf(len(prefixes)) * abs(mean) ** 2
    bridge_energy = mp.fsum(abs(value - mean) ** 2 for value in prefixes)
    return mean, scalar_energy, bridge_energy


def discrete_brownian_bridge_green_kernel(block_length: int) -> mp.matrix:
    """Schur complement on the fresh charges of a prefix block."""
    if block_length < 2:
        raise ValueError("block_length must be at least two")
    return mp.matrix(
        [
            [
                mp.mpf(min(left, right))
                * (block_length - max(left, right))
                / block_length
                for right in range(1, block_length)
            ]
            for left in range(1, block_length)
        ]
    )


def dirichlet_bridge_laplacian(block_length: int) -> mp.matrix:
    """Inverse of the discrete Brownian-bridge Green kernel."""
    if block_length < 2:
        raise ValueError("block_length must be at least two")
    size = block_length - 1
    laplacian = mp.zeros(size, size)
    for index in range(size):
        laplacian[index, index] = 2
        if index > 0:
            laplacian[index, index - 1] = -1
            laplacian[index - 1, index] = -1
    return laplacian


def cesaro_orbit_metric(operator: mp.matrix, radius: int) -> mp.matrix:
    """Finite Cesaro metric averaging the two-sided orbit of an invertible map."""
    rows, columns = operator.rows, operator.cols
    if rows != columns or rows < 1:
        raise ValueError("operator must be a nonempty square matrix")
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    inverse = operator**-1
    forward = mp.eye(rows)
    backward = mp.eye(rows)
    metric = mp.eye(rows)
    for _ in range(radius):
        forward = forward * operator
        backward = backward * inverse
        metric += forward.transpose_conj() * forward
        metric += backward.transpose_conj() * backward
    return metric / (2 * radius + 1)


def cesaro_orbit_gram(
    operator: mp.matrix,
    vectors: mp.matrix,
    radius: int,
) -> mp.matrix:
    """Positive Gram of finitely many vectors under a two-sided Cesaro orbit."""
    if vectors.rows != operator.rows or vectors.cols < 1:
        raise ValueError("vectors must be a nonempty matrix of column vectors")
    metric = cesaro_orbit_metric(operator, radius)
    return vectors.transpose_conj() * metric * vectors


def cesaro_orbit_energy(
    operator: mp.matrix,
    vector: mp.matrix,
    radius: int,
) -> mp.mpf:
    """Two-sided averaged squared orbit norm of one column vector."""
    if vector.cols != 1:
        raise ValueError("vector must have one column")
    value = cesaro_orbit_gram(operator, vector, radius)[0, 0]
    return mp.re(value)


def polarization_similitude_residual(
    operator: mp.matrix,
    metric: mp.matrix,
    scale: mp.mpf = mp.mpf("1"),
) -> mp.matrix:
    """Residual F^* H F - scale H of a candidate positive polarization."""
    if operator.rows != operator.cols or operator.rows < 1:
        raise ValueError("operator must be a nonempty square matrix")
    if metric.rows != operator.rows or metric.cols != operator.cols:
        raise ValueError("metric and operator dimensions must agree")
    scale = mp.mpf(scale)
    if scale <= 0:
        raise ValueError("scale must be positive")
    return operator.transpose_conj() * metric * operator - scale * metric


def ihara_frobenius_operator(
    adjacency: mp.matrix,
    q: mp.mpf,
) -> mp.matrix:
    """Bass--Ihara companion Frobenius [[A,-qI],[I,0]]."""
    if adjacency.rows != adjacency.cols or adjacency.rows < 1:
        raise ValueError("adjacency must be a nonempty square matrix")
    q = mp.mpf(q)
    if q <= 0:
        raise ValueError("q must be positive")
    dimension = adjacency.rows
    operator = mp.zeros(2 * dimension, 2 * dimension)
    for row in range(dimension):
        for column in range(dimension):
            operator[row, column] = adjacency[row, column]
        operator[row, dimension + row] = -q
        operator[dimension + row, row] = 1
    return operator


def ihara_hodge_metric(
    adjacency: mp.matrix,
    q: mp.mpf,
) -> mp.matrix:
    """Explicit Ihara form [[I,-A/2],[-A/2,qI]] for self-adjoint A."""
    if adjacency.rows != adjacency.cols or adjacency.rows < 1:
        raise ValueError("adjacency must be a nonempty square matrix")
    q = mp.mpf(q)
    if q <= 0:
        raise ValueError("q must be positive")
    dimension = adjacency.rows
    metric = mp.zeros(2 * dimension, 2 * dimension)
    for row in range(dimension):
        metric[row, row] = 1
        metric[dimension + row, dimension + row] = q
        for column in range(dimension):
            metric[row, dimension + column] = -adjacency[row, column] / 2
            metric[dimension + row, column] = -adjacency[row, column] / 2
    return metric


def ihara_bass_matrix(
    adjacency: mp.matrix,
    q: mp.mpf,
    variable: mp.mpc,
) -> mp.matrix:
    """Vertex Bass factor I-uA+q u^2 I for a regular graph."""
    if adjacency.rows != adjacency.cols or adjacency.rows < 1:
        raise ValueError("adjacency must be a nonempty square matrix")
    q = mp.mpf(q)
    if q <= 0:
        raise ValueError("q must be positive")
    variable = mp.mpc(variable)
    dimension = adjacency.rows
    return (
        mp.eye(dimension)
        - variable * adjacency
        + q * variable**2 * mp.eye(dimension)
    )


def primes_up_to(limit: int) -> list[int]:
    """Return all primes at most ``limit`` by a finite Eratosthenes sieve."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [integer for integer in range(2, limit + 1) if sieve[integer]]


def prime_orbit_schatten_sum(
    sigma: mp.mpf,
    order: int,
    prime_cutoff: int,
) -> mp.mpf:
    """Finite S_order^order sum for diag(p^{-s}) over p <= cutoff."""
    sigma = mp.mpf(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    if order < 1:
        raise ValueError("order must be positive")
    if prime_cutoff < 2:
        raise ValueError("prime_cutoff must be at least 2")
    return mp.fsum(
        mp.power(prime, -order * sigma)
        for prime in primes_up_to(prime_cutoff)
    )


def finite_prime_euler_inverse(
    point: mp.mpc,
    prime_cutoff: int,
) -> mp.mpc:
    """Finite inverse Euler product product_{p<=P}(1-p^{-s})."""
    if prime_cutoff < 2:
        raise ValueError("prime_cutoff must be at least 2")
    point = mp.mpc(point)
    return mp.fprod(
        1 - mp.power(prime, -point)
        for prime in primes_up_to(prime_cutoff)
    )


def finite_prime_regularized_determinant(
    point: mp.mpc,
    order: int,
    prime_cutoff: int,
) -> mp.mpc:
    """Finite det_order(I-diag(p^{-s})) canonical product."""
    if order < 1:
        raise ValueError("order must be positive")
    if prime_cutoff < 2:
        raise ValueError("prime_cutoff must be at least 2")
    point = mp.mpc(point)
    value = mp.mpc(1)
    for prime in primes_up_to(prime_cutoff):
        local = mp.power(prime, -point)
        counterterm = mp.fsum(local**power / power for power in range(1, order))
        value *= (1 - local) * mp.exp(counterterm)
    return value


def finite_prime_regularization_counterterm(
    point: mp.mpc,
    order: int,
    prime_cutoff: int,
) -> mp.mpc:
    """Counterterm converting det_order back to the finite Euler product."""
    if order < 1:
        raise ValueError("order must be positive")
    if prime_cutoff < 2:
        raise ValueError("prime_cutoff must be at least 2")
    point = mp.mpc(point)
    exponent = mp.fsum(
        -mp.power(prime, -power * point) / power
        for prime in primes_up_to(prime_cutoff)
        for power in range(1, order)
    )
    return mp.exp(exponent)


def regularized_positive_residual_certificate(
    positive_kernel: mp.matrix,
    order: int,
) -> dict[str, object]:
    """Canonical det_order rigidity for a positive primitive residual.

    For K>=0, det_order(I+K) removes the first order-1 Taylor traces.
    The remaining scalar logarithm has the fixed sign (-1)^(order-1),
    so the regularized determinant is one only for K=0.
    """
    if order < 1:
        raise ValueError("order must be positive")
    if positive_kernel.rows != positive_kernel.cols:
        raise ValueError("positive_kernel must be square")
    positive_kernel = mp.matrix(positive_kernel)
    dimension = positive_kernel.rows
    eigenvalues = mp.eigsy(positive_kernel, eigvals_only=True)
    tolerance = mp.eps * max(
        mp.mpf("1"),
        max(
            (abs(eigenvalues[index]) for index in range(dimension)),
            default=mp.mpf("0"),
        ),
    )
    if any(eigenvalues[index] < -tolerance for index in range(dimension)):
        raise ValueError("positive_kernel must be positive semidefinite")
    clipped_eigenvalues = [
        max(mp.mpf("0"), mp.re(eigenvalues[index]))
        for index in range(dimension)
    ]
    trace_powers = [
        mp.fsum(value**power for value in clipped_eigenvalues)
        for power in range(1, order)
    ]
    counterterm_exponent = mp.fsum(
        (-1) ** power * trace_powers[power - 1] / power
        for power in range(1, order)
    )
    ordinary_determinant = mp.fprod(
        1 + value for value in clipped_eigenvalues
    )
    regularized_determinant = (
        ordinary_determinant * mp.exp(counterterm_exponent)
    )
    logarithmic_remainder = mp.fsum(
        mp.log(1 + value)
        + mp.fsum(
            (-1) ** power * value**power / power
            for power in range(1, order)
        )
        for value in clipped_eigenvalues
    )
    integral_remainder = (
        (-1) ** (order - 1)
        * mp.fsum(
            mp.quad(
                lambda variable: variable ** (order - 1)
                / (1 + variable),
                [0, value],
            )
            for value in clipped_eigenvalues
        )
    )
    signed_logarithmic_remainder = (
        (-1) ** (order - 1) * logarithmic_remainder
    )
    return {
        "positive_kernel": positive_kernel,
        "order": order,
        "eigenvalues": eigenvalues,
        "clipped_eigenvalues": clipped_eigenvalues,
        "trace_powers": trace_powers,
        "ordinary_determinant": ordinary_determinant,
        "counterterm_exponent": counterterm_exponent,
        "regularized_determinant": regularized_determinant,
        "logarithmic_remainder": logarithmic_remainder,
        "integral_remainder": integral_remainder,
        "signed_logarithmic_remainder": (
            signed_logarithmic_remainder
        ),
        "identical_pair_regularized_ratio": mp.mpf("1"),
        "is_zero_kernel": all(
            value <= tolerance for value in clipped_eigenvalues
        ),
    }


def prime_critical_regularization_certificate(
    prime_cutoff: int,
    height: mp.mpf = mp.mpf("0"),
) -> dict[str, object]:
    """Finite det_3 bookkeeping for the zeta prime operator on Re(s)=1/2."""
    if prime_cutoff < 2:
        raise ValueError("prime_cutoff must be at least two")
    point = mp.mpc(mp.mpf("0.5"), mp.mpf(height))
    order = 3
    primes = primes_up_to(prime_cutoff)
    missing_linear_trace = mp.fsum(
        mp.power(prime, -point) for prime in primes
    )
    missing_quadratic_trace = mp.fsum(
        mp.power(prime, -2 * point) / 2 for prime in primes
    )
    hilbert_schmidt_partial_sum = mp.fsum(
        mp.mpf(1) / prime for prime in primes
    )
    cubic_schatten_sum = mp.fsum(
        mp.power(prime, mp.mpf("-1.5")) for prime in primes
    )
    regularized_determinant = finite_prime_regularized_determinant(
        point, order, prime_cutoff
    )
    counterterm = finite_prime_regularization_counterterm(
        point, order, prime_cutoff
    )
    finite_euler_inverse = finite_prime_euler_inverse(
        point, prime_cutoff
    )
    return {
        "prime_cutoff": prime_cutoff,
        "height": mp.mpf(height),
        "point": point,
        "order": order,
        "prime_count": len(primes),
        "missing_linear_trace": missing_linear_trace,
        "missing_quadratic_trace": missing_quadratic_trace,
        "hilbert_schmidt_partial_sum": hilbert_schmidt_partial_sum,
        "cubic_schatten_sum": cubic_schatten_sum,
        "regularized_determinant": regularized_determinant,
        "counterterm": counterterm,
        "finite_euler_inverse": finite_euler_inverse,
        "reconstructed_euler_inverse": (
            regularized_determinant * counterterm
        ),
    }


def prime_regularization_anomaly_current_certificate(
    point: mp.mpc,
    prime_cutoff: int,
) -> dict[str, object]:
    """Split the finite Euler logarithmic derivative at det_3 order.

    If t_p=p^{-s}, the current -zeta_X'/zeta_X is

        sum_p log(p) t_p/(1-t_p)

    and splits exactly into the missing k=1,2 anomaly current and the
    convergent k>=3 det_3 current.  This is a derivative-level version of
    ``prime_critical_regularization_certificate`` valid at any finite point.
    """
    if prime_cutoff < 2:
        raise ValueError("prime_cutoff must be at least two")
    point = mp.mpc(point)
    primes = primes_up_to(prime_cutoff)
    local_parameters = [mp.power(prime, -point) for prime in primes]
    anomaly_potential = mp.fsum(
        local + local**2 / 2 for local in local_parameters
    )
    low_current = mp.fsum(
        mp.log(prime) * (local + local**2)
        for prime, local in zip(primes, local_parameters)
    )
    regularized_tail_current = mp.fsum(
        mp.log(prime) * local**3 / (1 - local)
        for prime, local in zip(primes, local_parameters)
    )
    euler_log_derivative = mp.fsum(
        mp.log(prime) * local / (1 - local)
        for prime, local in zip(primes, local_parameters)
    )
    return {
        "point": point,
        "prime_cutoff": prime_cutoff,
        "prime_count": len(primes),
        "anomaly_potential": anomaly_potential,
        "low_current": low_current,
        "regularized_tail_current": regularized_tail_current,
        "euler_log_derivative": euler_log_derivative,
        "reconstructed_euler_log_derivative": (
            low_current + regularized_tail_current
        ),
    }


def positive_real_pick_gram(
    points: list[mp.mpc],
    impedance_values: list[mp.mpc],
) -> mp.matrix:
    """Pick/positive-real kernel (F(z)+F(w)^*)/(z+w^*).

    The points must lie in the open right half-plane.  Positivity of all
    such finite matrices is the passive-boundary form of Hodge positivity.
    """
    if not points:
        raise ValueError("points must be nonempty")
    if len(points) != len(impedance_values):
        raise ValueError("points and impedance_values must have equal length")
    points = [mp.mpc(point) for point in points]
    values = [mp.mpc(value) for value in impedance_values]
    if any(mp.re(point) <= 0 for point in points):
        raise ValueError("points must lie in the open right half-plane")
    gram = mp.zeros(len(points), len(points))
    for row, point in enumerate(points):
        for column, other in enumerate(points):
            gram[row, column] = (
                values[row] + mp.conj(values[column])
            ) / (point + mp.conj(other))
    return gram


def positive_real_completion_certificate(
    points: list[mp.mpc],
    impedance_values: list[mp.mpc],
) -> dict[str, object]:
    """Least constant passive channel needed on a finite Pick set.

    Adding a real constant c to an impedance adds the positive Szego kernel
    2c/(z+w^*) to its Pick kernel.  The least c for the supplied point set is
    the negative part of the smallest generalized eigenvalue of this pencil.
    This normalization makes defects comparable across different point sets.
    """
    pick_gram = positive_real_pick_gram(points, impedance_values)
    normalized_points = [mp.mpc(point) for point in points]
    szego_gram = mp.zeros(len(points), len(points))
    for row, point in enumerate(normalized_points):
        for column, other in enumerate(normalized_points):
            szego_gram[row, column] = 2 / (
                point + mp.conj(other)
            )
    hermitian_pick = (pick_gram + pick_gram.transpose_conj()) / 2
    hermitian_szego = (szego_gram + szego_gram.transpose_conj()) / 2
    cholesky = mp.cholesky(hermitian_szego)
    inverse_cholesky = cholesky**-1
    normalized_pick = (
        inverse_cholesky
        * hermitian_pick
        * inverse_cholesky.transpose_conj()
    )
    normalized_pick = (
        normalized_pick + normalized_pick.transpose_conj()
    ) / 2
    generalized_eigenvalues = mp.eighe(
        normalized_pick, eigvals_only=True
    )
    smallest_generalized_eigenvalue = min(
        generalized_eigenvalues[index]
        for index in range(generalized_eigenvalues.rows)
    )
    completion_charge = max(
        mp.mpf("0"), -smallest_generalized_eigenvalue
    )
    completed_pick_gram = (
        hermitian_pick + completion_charge * hermitian_szego
    )
    completed_eigenvalues = mp.eighe(
        completed_pick_gram, eigvals_only=True
    )
    return {
        "points": normalized_points,
        "pick_gram": pick_gram,
        "szego_gram": szego_gram,
        "normalized_pick_gram": normalized_pick,
        "generalized_pick_eigenvalues": generalized_eigenvalues,
        "smallest_generalized_pick_eigenvalue": (
            smallest_generalized_eigenvalue
        ),
        "completion_charge": completion_charge,
        "completed_pick_gram": completed_pick_gram,
        "completed_pick_eigenvalues": completed_eigenvalues,
    }


def stable_pole_passive_impedance_certificate(
    points: list[mp.mpc],
    stable_poles: list[mp.mpc],
    multiplicities: list[int] | None = None,
) -> dict[str, object]:
    """Passive Pick realization for poles in the closed left half-plane.

    This is the finite rational model behind the passivity-abscissa theorem.
    Each term 1/(z-r), Re(r)<=0, contributes a rank-one resolvent Gram plus
    (-2 Re(r)) times a Szego-kernel Schur product.
    """
    if not points or not stable_poles:
        raise ValueError("points and stable_poles must be nonempty")
    points = [mp.mpc(point) for point in points]
    poles = [mp.mpc(pole) for pole in stable_poles]
    if any(mp.re(point) <= 0 for point in points):
        raise ValueError("points must lie in the open right half-plane")
    if any(mp.re(pole) > 0 for pole in poles):
        raise ValueError("stable_poles must lie in the closed left half-plane")
    if multiplicities is None:
        multiplicities = [1] * len(poles)
    if len(multiplicities) != len(poles) or any(
        multiplicity <= 0 or int(multiplicity) != multiplicity
        for multiplicity in multiplicities
    ):
        raise ValueError("multiplicities must be positive integers")
    multiplicities = [int(value) for value in multiplicities]
    values = [
        mp.fsum(
            multiplicity / (point - pole)
            for pole, multiplicity in zip(poles, multiplicities)
        )
        for point in points
    ]
    pick_gram = positive_real_pick_gram(points, values)
    decomposed_gram = mp.zeros(len(points), len(points))
    for row, point in enumerate(points):
        for column, other in enumerate(points):
            decomposed_gram[row, column] = mp.fsum(
                multiplicity
                * (
                    1
                    / (
                        (point - pole)
                        * (mp.conj(other) - mp.conj(pole))
                    )
                    + (-2 * mp.re(pole))
                    / (
                        (point - pole)
                        * (mp.conj(other) - mp.conj(pole))
                        * (point + mp.conj(other))
                    )
                )
                for pole, multiplicity in zip(poles, multiplicities)
            )
    hermitian_gram = (pick_gram + pick_gram.transpose_conj()) / 2
    eigenvalues = mp.eighe(hermitian_gram, eigvals_only=True)
    return {
        "points": points,
        "stable_poles": poles,
        "multiplicities": multiplicities,
        "impedance_values": values,
        "pick_gram": pick_gram,
        "decomposed_gram": decomposed_gram,
        "pick_eigenvalues": eigenvalues,
        "minimum_pick_eigenvalue": min(
            eigenvalues[index] for index in range(eigenvalues.rows)
        ),
    }


def centerline_passive_impedance_certificate(
    points: list[mp.mpc],
    positive_ordinates: list[mp.mpf],
    multiplicities: list[int] | None = None,
    central_multiplicity: int = 0,
) -> dict[str, object]:
    """Finite passive realization for a center-line spectral divisor.

    A central zero contributes m/z.  A pair 1/2 +/- i*gamma contributes
    m[(z-i*gamma)^(-1)+(z+i*gamma)^(-1)].  The associated Pick matrix is
    returned both from the impedance formula and as an explicit Gram sum.
    """
    if not points:
        raise ValueError("points must be nonempty")
    points = [mp.mpc(point) for point in points]
    if any(mp.re(point) <= 0 for point in points):
        raise ValueError("points must lie in the open right half-plane")
    ordinates = [mp.mpf(ordinate) for ordinate in positive_ordinates]
    if any(ordinate <= 0 for ordinate in ordinates):
        raise ValueError("positive_ordinates must be positive")
    if multiplicities is None:
        multiplicities = [1] * len(ordinates)
    if len(multiplicities) != len(ordinates):
        raise ValueError("multiplicities must match positive_ordinates")
    if central_multiplicity < 0 or any(
        multiplicity <= 0 or int(multiplicity) != multiplicity
        for multiplicity in multiplicities
    ):
        raise ValueError("spectral multiplicities must be nonnegative integers")
    multiplicities = [int(multiplicity) for multiplicity in multiplicities]
    impedance_values = []
    for point in points:
        value = mp.mpf(central_multiplicity) / point
        value += mp.fsum(
            multiplicity
            * (
                1 / (point - 1j * ordinate)
                + 1 / (point + 1j * ordinate)
            )
            for ordinate, multiplicity in zip(ordinates, multiplicities)
        )
        impedance_values.append(value)
    pick_gram = positive_real_pick_gram(points, impedance_values)
    feature_gram = mp.zeros(len(points), len(points))
    for row, point in enumerate(points):
        for column, other in enumerate(points):
            value = (
                mp.mpf(central_multiplicity)
                / (point * mp.conj(other))
            )
            value += mp.fsum(
                multiplicity
                * (
                    1
                    / (
                        (point - 1j * ordinate)
                        * (mp.conj(other) + 1j * ordinate)
                    )
                    + 1
                    / (
                        (point + 1j * ordinate)
                        * (mp.conj(other) - 1j * ordinate)
                    )
                )
                for ordinate, multiplicity in zip(
                    ordinates, multiplicities
                )
            )
            feature_gram[row, column] = value
    hermitian_pick_gram = (pick_gram + pick_gram.transpose_conj()) / 2
    eigenvalues = mp.eighe(hermitian_pick_gram, eigvals_only=True)
    return {
        "points": points,
        "positive_ordinates": ordinates,
        "multiplicities": multiplicities,
        "central_multiplicity": central_multiplicity,
        "impedance_values": impedance_values,
        "pick_gram": pick_gram,
        "feature_gram": feature_gram,
        "pick_eigenvalues": eigenvalues,
        "minimum_pick_eigenvalue": min(
            eigenvalues[index] for index in range(eigenvalues.rows)
        ),
    }


def zeta_renormalized_prime_impedance(
    point: mp.mpc,
    integer_cutoff: int,
) -> mp.mpc:
    """Prime--Gamma approximation to xi'/xi with the pole tail removed.

    Here ``point`` is z=s-1/2 in the open right half-plane.  The expression
    uses only Lambda(n) for n<=X, the archimedean factor, and the continuum
    tail X^(1-s)/(s-1).  The latter cancels the apparent pole at s=1; the
    quotient is evaluated by its analytic value log(X) there.
    """
    if integer_cutoff < 2:
        raise ValueError("integer_cutoff must be at least two")
    point = mp.mpc(point)
    if mp.re(point) <= 0:
        raise ValueError("point must lie in the open right half-plane")
    s = point + mp.mpf("0.5")
    logarithm = mp.log(integer_cutoff)
    displacement = s - 1
    if abs(displacement) <= mp.sqrt(mp.eps):
        pole_pair = logarithm
    else:
        pole_pair = (1 - mp.exp(-displacement * logarithm)) / displacement
    prime_current = mp.fsum(
        von_mangoldt(integer) * mp.power(integer, -s)
        for integer in range(2, integer_cutoff + 1)
    )
    return (
        1 / s
        + pole_pair
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        - prime_current
    )


def zeta_renormalized_impedance_pick_certificate(
    points: list[mp.mpc],
    integer_cutoff: int,
) -> dict[str, object]:
    """Finite Pick audit for the prime--continuum impedance approximation."""
    values = [
        zeta_renormalized_prime_impedance(point, integer_cutoff)
        for point in points
    ]
    completion = positive_real_completion_certificate(points, values)
    pick_gram = completion["pick_gram"]
    hermitian_pick_gram = (pick_gram + pick_gram.transpose_conj()) / 2
    eigenvalues = mp.eighe(hermitian_pick_gram, eigvals_only=True)
    return {
        "points": [mp.mpc(point) for point in points],
        "integer_cutoff": integer_cutoff,
        "impedance_values": values,
        "pick_gram": pick_gram,
        "pick_eigenvalues": eigenvalues,
        "minimum_pick_eigenvalue": min(
            eigenvalues[index] for index in range(eigenvalues.rows)
        ),
        "completion_charge": completion["completion_charge"],
        "generalized_pick_eigenvalues": (
            completion["generalized_pick_eigenvalues"]
        ),
        "completed_pick_eigenvalues": (
            completion["completed_pick_eigenvalues"]
        ),
    }


def zeta_abel_prime_impedance(
    point: mp.mpc,
    scale: mp.mpf,
    integer_cutoff: int,
) -> dict[str, object]:
    """Exponentially Abel-smoothed prime approximation to xi'/xi.

    With s=1/2+z and Y=scale, this computes

        B_infinity(s) + integral_1^infinity x^{-s}e^{-x/Y} dx
        - sum_{n<=N} Lambda(n)n^{-s}e^{-n/Y}.

    The omitted prime-current tail is bounded using Lambda(n)<=log(n).
    The continuum integral is Y^(1-s) Gamma(1-s,1/Y), so every fixed-Y
    candidate is holomorphic rather than carrying an artificial pole at s=1.
    """
    if integer_cutoff < 3:
        raise ValueError("integer_cutoff must be at least three")
    point = mp.mpc(point)
    scale = mp.mpf(scale)
    if mp.re(point) <= 0:
        raise ValueError("point must lie in the open right half-plane")
    if scale <= 0:
        raise ValueError("scale must be positive")
    s = point + mp.mpf("0.5")
    continuum_current = mp.power(scale, 1 - s) * mp.gammainc(
        1 - s, 1 / scale, mp.inf
    )
    prime_current = mp.fsum(
        von_mangoldt(integer)
        * mp.power(integer, -s)
        * mp.exp(-mp.mpf(integer) / scale)
        for integer in range(2, integer_cutoff + 1)
    )
    value = (
        1 / s
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + continuum_current
        - prime_current
    )
    sigma = mp.re(s)
    cutoff = mp.mpf(integer_cutoff)
    monotonicity_margin = (
        sigma + cutoff / scale - 1 / mp.log(cutoff)
    )
    if monotonicity_margin <= 0:
        raise ValueError(
            "integer_cutoff is too small for the monotone tail bound"
        )
    prime_tail_bound = mp.quad(
        lambda variable: (
            mp.log(variable)
            * mp.power(variable, -sigma)
            * mp.exp(-variable / scale)
        ),
        [cutoff, mp.inf],
    )
    return {
        "point": point,
        "s": s,
        "scale": scale,
        "integer_cutoff": integer_cutoff,
        "continuum_current": continuum_current,
        "truncated_prime_current": prime_current,
        "impedance": value,
        "prime_tail_bound": prime_tail_bound,
        "monotonicity_margin": monotonicity_margin,
    }


def zeta_abel_impedance_pick_certificate(
    points: list[mp.mpc],
    scale: mp.mpf,
    integer_cutoff: int,
) -> dict[str, object]:
    """Pick spectrum and a rigorous analytic truncation-error majorant.

    The numerical eigenvalues are not interval arithmetic.  The returned
    ``pick_operator_error_bound`` is nevertheless a proved scalar majorant:
    by Weyl's inequality, the exact infinite Abel Pick eigenvalues differ
    from the truncated ones by no more than this amount.
    """
    if not points:
        raise ValueError("points must be nonempty")
    data = [
        zeta_abel_prime_impedance(point, scale, integer_cutoff)
        for point in points
    ]
    normalized_points = [item["point"] for item in data]
    values = [item["impedance"] for item in data]
    tail_bounds = [item["prime_tail_bound"] for item in data]
    completion = positive_real_completion_certificate(
        normalized_points, values
    )
    pick_gram = completion["pick_gram"]
    hermitian_pick_gram = (pick_gram + pick_gram.transpose_conj()) / 2
    eigenvalues = mp.eighe(hermitian_pick_gram, eigvals_only=True)
    entry_error_bounds = mp.zeros(len(points), len(points))
    for row, point in enumerate(normalized_points):
        for column, other in enumerate(normalized_points):
            entry_error_bounds[row, column] = (
                tail_bounds[row] + tail_bounds[column]
            ) / abs(point + mp.conj(other))
    pick_operator_error_bound = max(
        mp.fsum(
            entry_error_bounds[row, column]
            for column in range(len(points))
        )
        for row in range(len(points))
    )
    minimum_eigenvalue = min(
        eigenvalues[index] for index in range(eigenvalues.rows)
    )
    return {
        "points": normalized_points,
        "scale": mp.mpf(scale),
        "integer_cutoff": integer_cutoff,
        "point_data": data,
        "impedance_values": values,
        "prime_tail_bounds": tail_bounds,
        "pick_gram": pick_gram,
        "pick_eigenvalues": eigenvalues,
        "minimum_pick_eigenvalue": minimum_eigenvalue,
        "completion_charge": completion["completion_charge"],
        "generalized_pick_eigenvalues": (
            completion["generalized_pick_eigenvalues"]
        ),
        "completed_pick_eigenvalues": (
            completion["completed_pick_eigenvalues"]
        ),
        "entry_error_bounds": entry_error_bounds,
        "pick_operator_error_bound": pick_operator_error_bound,
        "certified_minimum_lower_bound": (
            minimum_eigenvalue - pick_operator_error_bound
        ),
        "certified_minimum_upper_bound": (
            minimum_eigenvalue + pick_operator_error_bound
        ),
    }


def zeta_abel_resonance_well_audit(
    horizontal_offset: mp.mpf,
    scale: mp.mpf,
    integer_cutoff: int,
    height_start: mp.mpf,
    height_end: mp.mpf,
    height_step: mp.mpf,
    scalar_completion: mp.mpf = mp.mpf("0"),
) -> dict[str, object]:
    """Sample negative wells of an Abel-smoothed arithmetic impedance.

    The prime coefficients are assembled once, making a vertical resonance
    scan much cheaper than repeated single-point certificates.  Well lengths
    are grid diagnostics; the returned prime tail and mean-square bounds are
    analytic majorants rather than sampling claims.
    """
    horizontal_offset = mp.mpf(horizontal_offset)
    scale = mp.mpf(scale)
    height_start = mp.mpf(height_start)
    height_end = mp.mpf(height_end)
    height_step = mp.mpf(height_step)
    scalar_completion = mp.mpf(scalar_completion)
    if horizontal_offset <= 0:
        raise ValueError("horizontal_offset must be positive")
    if scale <= 0 or integer_cutoff < 3:
        raise ValueError("scale must be positive and cutoff at least three")
    if height_end < height_start or height_step <= 0:
        raise ValueError("height interval and step must be positive")
    sigma = mp.mpf("0.5") + horizontal_offset
    coefficients = []
    logarithmic_frequencies = []
    for integer in range(2, integer_cutoff + 1):
        mangoldt = von_mangoldt(integer)
        if mangoldt:
            coefficients.append(
                mangoldt
                * mp.power(integer, -sigma)
                * mp.exp(-mp.mpf(integer) / scale)
            )
            logarithmic_frequencies.append(mp.log(integer))
    coefficient_square_mass = mp.fsum(
        coefficient**2 for coefficient in coefficients
    )
    coefficient_absolute_mass = mp.fsum(coefficients)
    height_count = int(
        mp.floor((height_end - height_start) / height_step)
    ) + 1
    heights = [
        height_start + index * height_step
        for index in range(height_count)
    ]
    real_impedances = []
    for height in heights:
        s = mp.mpc(sigma, height)
        continuum_current = mp.power(scale, 1 - s) * mp.gammainc(
            1 - s, 1 / scale, mp.inf
        )
        prime_current = mp.fsum(
            coefficient * mp.exp(-1j * height * frequency)
            for coefficient, frequency in zip(
                coefficients, logarithmic_frequencies
            )
        )
        impedance = (
            1 / s
            - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2
            + continuum_current
            - prime_current
            + scalar_completion
        )
        real_impedances.append(mp.re(impedance))
    negative_indices = [
        index for index, value in enumerate(real_impedances) if value < 0
    ]
    wells = []
    if negative_indices:
        first = negative_indices[0]
        previous = first
        for index in negative_indices[1:]:
            if index != previous + 1:
                wells.append((heights[first], heights[previous]))
                first = index
            previous = index
        wells.append((heights[first], heights[previous]))
    cutoff = mp.mpf(integer_cutoff)
    monotonicity_margin = (
        sigma + cutoff / scale - 1 / mp.log(cutoff)
    )
    if monotonicity_margin <= 0:
        raise ValueError(
            "integer_cutoff is too small for the monotone tail bound"
        )
    prime_tail_bound = mp.quad(
        lambda variable: (
            mp.log(variable)
            * mp.power(variable, -sigma)
            * mp.exp(-variable / scale)
        ),
        [cutoff, mp.inf],
    )
    window_length = max(mp.mpf("0"), height_end - height_start)
    elementary_mean_square_bound = (
        window_length + 4 * cutoff * mp.harmonic(integer_cutoff)
    ) * coefficient_square_mass
    sampled_negative_mass = height_step * mp.fsum(
        max(mp.mpf("0"), -value) for value in real_impedances
    )
    return {
        "horizontal_offset": horizontal_offset,
        "scale": scale,
        "integer_cutoff": integer_cutoff,
        "height_start": height_start,
        "height_end": height_end,
        "height_step": height_step,
        "scalar_completion": scalar_completion,
        "heights": heights,
        "real_impedances": real_impedances,
        "negative_indices": negative_indices,
        "sampled_wells": wells,
        "sampled_negative_measure": (
            height_step * len(negative_indices)
        ),
        "sampled_negative_mass": sampled_negative_mass,
        "minimum_real_impedance": min(real_impedances),
        "minimum_height": heights[
            min(
                range(len(real_impedances)),
                key=lambda index: real_impedances[index],
            )
        ],
        "coefficient_square_mass": coefficient_square_mass,
        "coefficient_absolute_mass": coefficient_absolute_mass,
        "elementary_mean_square_bound": elementary_mean_square_bound,
        "prime_tail_bound": prime_tail_bound,
    }


def zeta_abel_cauchy_negative_mass_audit(
    horizontal_offset: mp.mpf,
    scale: mp.mpf,
    integer_cutoff: int,
    height_end: mp.mpf,
    height_step: mp.mpf,
    resolvent_points: list[mp.mpc] | None = None,
) -> dict[str, object]:
    """Sample the full-line Cauchy-weighted Abel passivity defect.

    Real type makes ``Re F_Y(x+it)`` even in ``t``.  A scan on ``[0,H]``
    therefore gives trapezoidal diagnostics for

        J_Y(H) = integral_[-H,H] [-Re F_Y(x+it)]_+/(1+t^2) dt

    and, optionally, for the diagonal resolvent energies

        (2*pi)^-1 integral W_Y(t)/|z-it|^2 dt.

    These are sampled diagnostics, not interval quadrature enclosures.
    """
    height_end = mp.mpf(height_end)
    height_step = mp.mpf(height_step)
    if height_end <= 0 or height_step <= 0:
        raise ValueError("height end and step must be positive")
    scan = zeta_abel_resonance_well_audit(
        horizontal_offset=horizontal_offset,
        scale=scale,
        integer_cutoff=integer_cutoff,
        height_start=mp.mpf("0"),
        height_end=height_end,
        height_step=height_step,
    )
    heights = scan["heights"]
    negative_values = [
        max(mp.mpf("0"), -value) for value in scan["real_impedances"]
    ]

    def trapezoid(values: list[mp.mpf]) -> mp.mpf:
        if len(values) < 2:
            return mp.mpf("0")
        return height_step * (
            mp.fsum(values) - (values[0] + values[-1]) / 2
        )

    weighted_values = [
        value / (1 + height**2)
        for value, height in zip(negative_values, heights)
    ]
    full_line_negative_mass = 2 * trapezoid(negative_values)
    full_line_cauchy_negative_mass = 2 * trapezoid(weighted_values)
    capped_defect_per_pi = full_line_cauchy_negative_mass / mp.pi
    unrestricted_character_negative_depth = max(
        mp.mpf("0"), -scan["minimum_real_impedance"]
    )
    character_to_capped_defect_ratio = mp.inf
    if capped_defect_per_pi > 0:
        character_to_capped_defect_ratio = (
            unrestricted_character_negative_depth / capped_defect_per_pi
        )
    signed_cauchy_integral = 2 * trapezoid([
        value / (1 + height**2)
        for value, height in zip(scan["real_impedances"], heights)
    ])
    center_point = mp.mpc(mp.mpf(horizontal_offset) + 1, 0)
    center_data = zeta_abel_prime_impedance(
        center_point, scale, integer_cutoff
    )
    center_real_impedance = mp.re(center_data["impedance"])
    centered_quadratic_integral = 2 * trapezoid([
        (value - center_real_impedance) ** 2 / (1 + height**2)
        for value, height in zip(scan["real_impedances"], heights)
    ])
    quadratic_negative_mass_upper = mp.inf
    if center_real_impedance > 0:
        quadratic_negative_mass_upper = (
            centered_quadratic_integral / (4 * center_real_impedance)
        )
    normalized_points = [
        mp.mpc(point) for point in (resolvent_points or [])
    ]
    resolvent_energies = []
    for point in normalized_points:
        if mp.re(point) <= 0:
            raise ValueError(
                "resolvent points must lie in the right half-plane"
            )
        integrand = [
            value
            * (
                1 / abs(point - 1j * height) ** 2
                + 1 / abs(point + 1j * height) ** 2
            )
            for value, height in zip(negative_values, heights)
        ]
        resolvent_energies.append(trapezoid(integrand) / (2 * mp.pi))
    return {
        **scan,
        "sampled_full_line_negative_mass": full_line_negative_mass,
        "sampled_full_line_cauchy_negative_mass": (
            full_line_cauchy_negative_mass
        ),
        "sampled_capped_defect_per_pi": capped_defect_per_pi,
        "sampled_unrestricted_character_negative_depth": (
            unrestricted_character_negative_depth
        ),
        "sampled_character_to_capped_defect_ratio": (
            character_to_capped_defect_ratio
        ),
        "poisson_center_point": center_point,
        "poisson_center_impedance": center_data["impedance"],
        "poisson_center_real_impedance": center_real_impedance,
        "exact_full_line_signed_cauchy_integral": (
            mp.pi * center_real_impedance
        ),
        "sampled_full_line_signed_cauchy_integral": (
            signed_cauchy_integral
        ),
        "sampled_signed_cauchy_tail_residual": (
            mp.pi * center_real_impedance - signed_cauchy_integral
        ),
        "sampled_centered_quadratic_cauchy_integral": (
            centered_quadratic_integral
        ),
        "sampled_quadratic_negative_mass_upper": (
            quadratic_negative_mass_upper
        ),
        "resolvent_points": normalized_points,
        "sampled_resolvent_negative_energies": resolvent_energies,
        "quadrature_rule": "symmetric composite trapezoid",
    }


def cayley_dirichlet_inner_value(
    logarithmic_frequency: mp.mpf,
    disk_point: mp.mpc,
) -> mp.mpc:
    """Singular-inner Cayley image of a Dirichlet boundary phase.

    Under ``z=delta+(1+q)/(1-q)``, the boundary character
    ``exp(-it*lambda)`` is the a.e. boundary value of

        Theta_lambda(q) = exp(-lambda*(1+q)/(1-q)).

    The family is an inner semigroup:
    ``Theta_a*Theta_b=Theta_(a+b)``.  This is the Hardy-space image of
    multiplication of Dirichlet frequencies.
    """
    logarithmic_frequency = mp.mpf(logarithmic_frequency)
    disk_point = mp.mpc(disk_point)
    if logarithmic_frequency < 0:
        raise ValueError("logarithmic_frequency must be nonnegative")
    if abs(disk_point) >= 1:
        raise ValueError("disk_point must lie in the open unit disk")
    return mp.exp(
        -logarithmic_frequency
        * (1 + disk_point)
        / (1 - disk_point)
    )


def finite_shift_autocorrelation(
    samples: list[mp.mpc],
    normalize: bool = False,
) -> list[mp.mpc]:
    """One-sided zero-extended shift autocorrelations of a finite vector.

    The returned value at lag k is

        r(k) = sum_j samples[j] * conjugate(samples[j+k]).

    It is the discrete Paley--Wiener model of
    ``<Theta_k h,h>``.  Its Hermitian two-sided extension is positive
    definite.  When requested, divide by r(0).
    """
    if not samples:
        raise ValueError("samples must be nonempty")
    values = [mp.mpc(value) for value in samples]
    correlations = [
        mp.fsum(
            values[index] * mp.conj(values[index + lag])
            for index in range(len(values) - lag)
        )
        for lag in range(len(values))
    ]
    if normalize:
        if abs(correlations[0]) == 0:
            raise ValueError("a zero vector cannot be normalized")
        correlations = [
            value / correlations[0] for value in correlations
        ]
    return correlations


def autocorrelation_toeplitz_gram(
    correlations: list[mp.mpc],
) -> mp.matrix:
    """Hermitian Toeplitz Gram associated with one-sided correlations."""
    if not correlations:
        raise ValueError("correlations must be nonempty")
    values = [mp.mpc(value) for value in correlations]
    size = len(values)
    gram = mp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            lag = column - row
            gram[row, column] = (
                values[lag] if lag >= 0 else mp.conj(values[-lag])
            )
    return gram


def cauchy_correlation_dominating_gram(
    lag_nodes: list[mp.mpf],
) -> mp.matrix:
    """Gram of the full Cauchy spectral cap on arbitrary lag nodes.

    The probability measure ``dt/(pi*(1+t^2))`` has Fourier transform
    ``exp(-|lambda|)``.  Hence the returned matrix is
    ``K[j,k]=exp(-|lambda_j-lambda_k|)``.
    """
    if not lag_nodes:
        raise ValueError("lag_nodes must be nonempty")
    nodes = [mp.mpf(node) for node in lag_nodes]
    return mp.matrix([
        [mp.exp(-abs(first - second)) for second in nodes]
        for first in nodes
    ])


def cauchy_capped_correlation_modulus_bound(
    lag_distance: mp.mpf,
) -> dict[str, mp.mpf]:
    """Uniform modulus for correlations with spectral density ``0<=theta<=1``.

    Direct L1 integration of ``min(2,|t|d)`` against the Cauchy measure gives

        d/pi*log(1+4/d^2) + 4/pi*(pi/2-atan(2/d)).

    The returned bound is the smaller of this cap-sensitive estimate and
    the generic L2 estimate ``sqrt(2*(1-exp(-d)))``.
    """
    lag_distance = abs(mp.mpf(lag_distance))
    if lag_distance == 0:
        return {
            "lag_distance": lag_distance,
            "cauchy_l1_modulus_bound": mp.mpf("0"),
            "cauchy_l2_modulus_bound": mp.mpf("0"),
            "combined_modulus_bound": mp.mpf("0"),
        }
    l1_bound = (
        lag_distance
        * mp.log(1 + 4 / lag_distance**2)
        / mp.pi
        + 4
        * (mp.pi / 2 - mp.atan(2 / lag_distance))
        / mp.pi
    )
    l2_bound = mp.sqrt(2 * (1 - mp.exp(-lag_distance)))
    return {
        "lag_distance": lag_distance,
        "cauchy_l1_modulus_bound": l1_bound,
        "cauchy_l2_modulus_bound": l2_bound,
        "combined_modulus_bound": min(l1_bound, l2_bound),
    }


def capped_correlation_gram_certificate(
    lag_nodes: list[mp.mpf],
    correlation_gram: mp.matrix,
) -> dict[str, object]:
    """Finite Loewner audit for a Cauchy-dominated correlation.

    A contractive-outer correlation must satisfy ``0<=R<=K_Cauchy`` on
    every finite lag set.  This function returns the spectra of both
    positive Gram blocks.  Numerical eigenvalues are diagnostics rather
    than interval certificates.
    """
    cap_gram = cauchy_correlation_dominating_gram(lag_nodes)
    if correlation_gram.rows != cap_gram.rows or (
        correlation_gram.cols != cap_gram.cols
    ):
        raise ValueError("correlation_gram dimensions must match lag_nodes")
    hermitian_correlation = (
        correlation_gram + correlation_gram.transpose_conj()
    ) / 2
    complement_gram = cap_gram - hermitian_correlation
    correlation_eigenvalues = mp.eighe(
        hermitian_correlation, eigvals_only=True
    )
    complement_eigenvalues = mp.eighe(
        complement_gram, eigvals_only=True
    )
    return {
        "lag_nodes": [mp.mpf(node) for node in lag_nodes],
        "correlation_gram": hermitian_correlation,
        "cauchy_cap_gram": cap_gram,
        "cap_complement_gram": complement_gram,
        "correlation_eigenvalues": correlation_eigenvalues,
        "cap_complement_eigenvalues": complement_eigenvalues,
        "minimum_correlation_eigenvalue": min(
            correlation_eigenvalues[index]
            for index in range(correlation_eigenvalues.rows)
        ),
        "minimum_cap_complement_eigenvalue": min(
            complement_eigenvalues[index]
            for index in range(complement_eigenvalues.rows)
        ),
    }


def correlation_first_column_objective_gram(
    coefficients: list[mp.mpc],
) -> mp.matrix:
    """Hermitian objective for real linear functionals of correlations.

    For a Hermitian correlation matrix R, the returned C satisfies

        trace(C*R) = Re(c[0]*R[0,0] + sum_(j>0)c[j]*R[j,0]).

    This packages quadrature and orbit coefficients into a standard
    Loewner-interval SDP objective.
    """
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    values = [mp.mpc(value) for value in coefficients]
    size = len(values)
    objective = mp.zeros(size, size)
    objective[0, 0] = mp.re(values[0])
    for index in range(1, size):
        objective[0, index] = values[index] / 2
        objective[index, 0] = mp.conj(values[index]) / 2
    return objective


def loewner_interval_linear_minimum(
    cap_gram: mp.matrix,
    objective_gram: mp.matrix,
) -> dict[str, object]:
    """Closed-form minimum of trace(CR) over ``0<=R<=K``.

    Congruence writes ``R=K^(1/2) X K^(1/2)``, ``0<=X<=I``.  Therefore
    the minimum is the sum of the negative eigenvalues of
    ``K^(1/2) C K^(1/2)``; the optimizer is obtained from its negative
    spectral projection.  Singular positive K is supported on its range.
    """
    if cap_gram.rows != cap_gram.cols or (
        objective_gram.rows != objective_gram.cols
    ):
        raise ValueError("cap and objective matrices must be square")
    if cap_gram.rows != objective_gram.rows:
        raise ValueError("cap and objective dimensions must match")
    hermitian_cap = (cap_gram + cap_gram.transpose_conj()) / 2
    hermitian_objective = (
        objective_gram + objective_gram.transpose_conj()
    ) / 2
    cap_eigenvalues, cap_eigenvectors = mp.eigh(hermitian_cap)
    cap_scale = max(
        mp.mpf("1"),
        max(abs(cap_eigenvalues[index]) for index in range(cap_eigenvalues.rows)),
    )
    tolerance = 100 * mp.eps * cap_scale
    if min(
        cap_eigenvalues[index] for index in range(cap_eigenvalues.rows)
    ) < -tolerance:
        raise ValueError("cap_gram must be positive semidefinite")
    square_root_diagonal = mp.diag([
        mp.sqrt(max(mp.mpf("0"), cap_eigenvalues[index]))
        for index in range(cap_eigenvalues.rows)
    ])
    cap_square_root = (
        cap_eigenvectors
        * square_root_diagonal
        * cap_eigenvectors.transpose_conj()
    )
    normalized_objective = (
        cap_square_root * hermitian_objective * cap_square_root
    )
    objective_eigenvalues, objective_eigenvectors = mp.eigh(
        normalized_objective
    )
    negative_diagonal = mp.diag([
        mp.mpf("1") if objective_eigenvalues[index] < 0 else mp.mpf("0")
        for index in range(objective_eigenvalues.rows)
    ])
    negative_projection = (
        objective_eigenvectors
        * negative_diagonal
        * objective_eigenvectors.transpose_conj()
    )
    optimizer = (
        cap_square_root * negative_projection * cap_square_root
    )
    minimum = mp.fsum(
        min(mp.mpf("0"), objective_eigenvalues[index])
        for index in range(objective_eigenvalues.rows)
    )
    return {
        "cap_gram": hermitian_cap,
        "objective_gram": hermitian_objective,
        "cap_square_root": cap_square_root,
        "normalized_objective": normalized_objective,
        "normalized_objective_eigenvalues": objective_eigenvalues,
        "negative_spectral_projection": negative_projection,
        "optimizer_gram": optimizer,
        "minimum_objective": minimum,
        "optimizer_objective": mp.re(mp.fsum(
            (hermitian_objective * optimizer)[index, index]
            for index in range(optimizer.rows)
        )),
        "cap_tolerance": tolerance,
    }


def loewner_interval_linear_minimum_numpy(
    cap_gram: mp.matrix,
    objective_gram: mp.matrix,
) -> dict[str, object]:
    """Double-precision spectral audit for a larger Loewner interval.

    This evaluates the same closed formula as
    :func:`loewner_interval_linear_minimum`, but uses NumPy's Hermitian
    eigensolver.  It is intended for exploratory quadrature matrices; it is
    not an interval certificate.
    """
    if cap_gram.rows != cap_gram.cols or (
        objective_gram.rows != objective_gram.cols
    ):
        raise ValueError("cap and objective matrices must be square")
    if cap_gram.rows != objective_gram.rows:
        raise ValueError("cap and objective dimensions must match")
    size = cap_gram.rows
    cap_array = np.array([
        [complex(cap_gram[row, column]) for column in range(size)]
        for row in range(size)
    ], dtype=np.complex128)
    objective_array = np.array([
        [complex(objective_gram[row, column]) for column in range(size)]
        for row in range(size)
    ], dtype=np.complex128)
    cap_array = (cap_array + cap_array.conj().T) / 2
    objective_array = (objective_array + objective_array.conj().T) / 2
    cap_eigenvalues, cap_eigenvectors = np.linalg.eigh(cap_array)
    cap_scale = max(1.0, float(np.max(np.abs(cap_eigenvalues))))
    tolerance = 1e-10 * cap_scale
    if float(np.min(cap_eigenvalues)) < -tolerance:
        raise ValueError("cap_gram must be positive semidefinite")
    clipped_cap_eigenvalues = np.maximum(cap_eigenvalues, 0.0)
    cap_square_root = (
        cap_eigenvectors
        @ np.diag(np.sqrt(clipped_cap_eigenvalues))
        @ cap_eigenvectors.conj().T
    )
    normalized_objective = (
        cap_square_root @ objective_array @ cap_square_root
    )
    objective_eigenvalues, objective_eigenvectors = np.linalg.eigh(
        normalized_objective
    )
    negative_mask = objective_eigenvalues < 0
    negative_projection = (
        objective_eigenvectors
        @ np.diag(negative_mask.astype(float))
        @ objective_eigenvectors.conj().T
    )
    optimizer = cap_square_root @ negative_projection @ cap_square_root
    minimum = float(np.minimum(objective_eigenvalues, 0.0).sum())
    optimizer_objective = float(np.trace(objective_array @ optimizer).real)
    return {
        "backend": "numpy.complex128",
        "cap_eigenvalues": cap_eigenvalues,
        "cap_square_root": cap_square_root,
        "normalized_objective": normalized_objective,
        "normalized_objective_eigenvalues": objective_eigenvalues,
        "negative_spectral_projection": negative_projection,
        "optimizer_gram": optimizer,
        "minimum_objective": minimum,
        "optimizer_objective": optimizer_objective,
        "cap_tolerance": tolerance,
    }


def correlation_stationarity_defect(
    lag_nodes: list[mp.mpf],
    correlation_gram: object,
    difference_tolerance: float = 1e-10,
) -> dict[str, object]:
    """Audit whether a finite Gram depends only on lag differences.

    Entries with equal node differences must agree for a stationary
    correlation kernel.  The audit groups differences to the requested
    tolerance and reports the largest within-group diameter.  It accepts an
    mpmath matrix or a NumPy-compatible square array.
    """
    if not lag_nodes:
        raise ValueError("lag_nodes must be nonempty")
    if difference_tolerance <= 0:
        raise ValueError("difference_tolerance must be positive")
    nodes = np.asarray([float(node) for node in lag_nodes], dtype=float)
    if isinstance(correlation_gram, mp.matrix):
        size = correlation_gram.rows
        gram = np.array([
            [complex(correlation_gram[row, column]) for column in range(size)]
            for row in range(size)
        ], dtype=np.complex128)
    else:
        gram = np.asarray(correlation_gram, dtype=np.complex128)
        size = gram.shape[0]
    if gram.ndim != 2 or gram.shape != (len(nodes), len(nodes)):
        raise ValueError("correlation_gram dimensions must match lag_nodes")
    groups: dict[int, list[complex]] = {}
    for row in range(size):
        for column in range(size):
            difference = nodes[row] - nodes[column]
            key = int(round(difference / difference_tolerance))
            groups.setdefault(key, []).append(complex(gram[row, column]))
    maximum_diameter = 0.0
    largest_group_size = 0
    repeated_group_count = 0
    for values in groups.values():
        largest_group_size = max(largest_group_size, len(values))
        if len(values) > 1:
            repeated_group_count += 1
            anchor = values[0]
            maximum_diameter = max(
                maximum_diameter,
                2 * max(abs(value - anchor) for value in values),
            )
    diagonal = np.real(np.diag(gram))
    diagonal_spread = float(np.max(diagonal) - np.min(diagonal))
    return {
        "difference_tolerance": difference_tolerance,
        "difference_group_count": len(groups),
        "repeated_difference_group_count": repeated_group_count,
        "largest_difference_group_size": largest_group_size,
        "diagonal_spread": diagonal_spread,
        "maximum_equal_lag_entry_diameter_upper": maximum_diameter,
        "is_stationary_within_tolerance": (
            maximum_diameter <= 2 * difference_tolerance
        ),
    }


def stationary_capped_functional_minimum(
    lag_nodes: list[mp.mpf],
    coefficients: list[mp.mpc],
    height_cutoff: mp.mpf,
    height_cells: int,
    chunk_size: int = 4096,
) -> dict[str, object]:
    """One-dimensional minimum over the exact stationary Cauchy cap.

    For ``P(t)=Re sum c_j exp(-it lambda_j)``, minimization over spectral
    densities ``0<=theta<=1`` equals ``integral min(P,0)dmu``.  This uses
    exact Cauchy masses on uniform midpoint cells.  The symbol Lipschitz
    constant bounds the grid error, and its absolute coefficient mass
    bounds the omitted Cauchy tail.
    """
    if not lag_nodes or len(lag_nodes) != len(coefficients):
        raise ValueError("nodes and coefficients must be nonempty and aligned")
    height_cutoff = mp.mpf(height_cutoff)
    if height_cutoff <= 0 or height_cells < 1 or chunk_size < 1:
        raise ValueError("height cutoff and cell count must be positive")
    nodes = np.asarray([float(node) for node in lag_nodes], dtype=float)
    values = np.asarray(
        [complex(coefficient) for coefficient in coefficients],
        dtype=np.complex128,
    )
    cutoff = float(height_cutoff)
    edges = np.linspace(-cutoff, cutoff, height_cells + 1)
    cell_masses = (
        np.arctan(edges[1:]) - np.arctan(edges[:-1])
    ) / math.pi
    sampled_minimum = 0.0
    symbol_minimum = math.inf
    negative_cell_count = 0
    for start in range(0, height_cells, chunk_size):
        stop = min(height_cells, start + chunk_size)
        midpoints = (edges[start:stop] + edges[start + 1:stop + 1]) / 2
        symbols = np.real(
            np.exp(-1j * np.outer(midpoints, nodes)) @ values
        )
        sampled_minimum += float(
            np.dot(
                cell_masses[start:stop],
                np.minimum(symbols, 0.0),
            )
        )
        symbol_minimum = min(symbol_minimum, float(np.min(symbols)))
        negative_cell_count += int(np.count_nonzero(symbols < 0))
    cell_width = 2 * cutoff / height_cells
    symbol_lipschitz_bound = float(np.dot(np.abs(values), np.abs(nodes)))
    grid_error_bound = symbol_lipschitz_bound * cell_width / 2
    coefficient_absolute_mass = float(np.abs(values).sum())
    cauchy_tail_mass = 1 - 2 * math.atan(cutoff) / math.pi
    tail_error_bound = coefficient_absolute_mass * cauchy_tail_mass
    total_error_bound = grid_error_bound + tail_error_bound
    return {
        "height_cutoff": height_cutoff,
        "height_cells": height_cells,
        "chunk_size": chunk_size,
        "sampled_stationary_minimum": sampled_minimum,
        "symbol_minimum_on_midpoints": symbol_minimum,
        "symbol_lipschitz_bound": symbol_lipschitz_bound,
        "coefficient_absolute_mass": coefficient_absolute_mass,
        "cauchy_tail_mass": cauchy_tail_mass,
        "grid_error_bound": grid_error_bound,
        "tail_error_bound": tail_error_bound,
        "total_error_bound": total_error_bound,
        "certified_stationary_lower_bound": (
            sampled_minimum - total_error_bound
        ),
        "sampled_negative_cell_fraction": float(
            negative_cell_count / height_cells
        ),
    }


def stationary_cauchy_block_negative_trace_audit(
    lag_nodes: list[mp.mpf],
    coefficients: list[mp.mpc],
    positive_block_edges: list[mp.mpf],
    cells_per_block: int = 1024,
    chunk_size: int = 4096,
) -> dict[str, object]:
    """Dyadic-style ledger for the Cauchy negative spectral trace.

    The nonnegative edges ``0=T_0<...<T_m`` define symmetric blocks
    ``[-T_{j+1},-T_j]`` and ``[T_j,T_{j+1}]``.  Midpoint symbol values are
    integrated against the *exact* Cauchy mass of every cell.  The global
    symbol Lipschitz constant certifies the midpoint error block by block;
    coefficient absolute mass controls the two-sided omitted tail.

    This is a floating formula audit, not interval arithmetic.  Nevertheless
    all reported error formulas are deterministic consequences of the input
    coefficients and mesh.
    """
    if not lag_nodes or len(lag_nodes) != len(coefficients):
        raise ValueError("nodes and coefficients must be nonempty and aligned")
    if len(positive_block_edges) < 2:
        raise ValueError("at least two block edges are required")
    if cells_per_block < 1 or chunk_size < 1:
        raise ValueError("cell and chunk counts must be positive")
    nodes = np.asarray([float(node) for node in lag_nodes], dtype=float)
    values = np.asarray(
        [complex(coefficient) for coefficient in coefficients],
        dtype=np.complex128,
    )
    edges = np.asarray(
        [float(edge) for edge in positive_block_edges], dtype=float
    )
    if edges[0] != 0 or np.any(~np.isfinite(edges)):
        raise ValueError("block edges must be finite and start at zero")
    if np.any(np.diff(edges) <= 0):
        raise ValueError("block edges must be strictly increasing")
    symbol_lipschitz_bound = float(
        np.dot(np.abs(values), np.abs(nodes))
    )
    coefficient_absolute_mass = float(np.abs(values).sum())
    records = []
    sampled_negative_trace = 0.0
    covered_grid_error_bound = 0.0
    for block_index, (left, right) in enumerate(
        zip(edges[:-1], edges[1:])
    ):
        cell_edges = np.linspace(left, right, cells_per_block + 1)
        cell_midpoints = (cell_edges[:-1] + cell_edges[1:]) / 2
        positive_cell_masses = (
            np.arctan(cell_edges[1:]) - np.arctan(cell_edges[:-1])
        ) / math.pi
        block_sample = 0.0
        block_symbol_minimum = math.inf
        negative_cell_count = 0
        for start in range(0, cells_per_block, chunk_size):
            stop = min(cells_per_block, start + chunk_size)
            midpoint_chunk = cell_midpoints[start:stop]
            phase = np.exp(-1j * np.outer(midpoint_chunk, nodes))
            positive_symbols = np.real(phase @ values)
            negative_symbols = np.real(np.conjugate(phase) @ values)
            mass_chunk = positive_cell_masses[start:stop]
            block_sample += float(np.dot(
                mass_chunk,
                np.maximum(-positive_symbols, 0.0)
                + np.maximum(-negative_symbols, 0.0),
            ))
            block_symbol_minimum = min(
                block_symbol_minimum,
                float(np.min(positive_symbols)),
                float(np.min(negative_symbols)),
            )
            negative_cell_count += int(
                np.count_nonzero(positive_symbols < 0)
                + np.count_nonzero(negative_symbols < 0)
            )
        block_cauchy_mass = float(
            2 * (math.atan(right) - math.atan(left)) / math.pi
        )
        half_cell_width = (right - left) / (2 * cells_per_block)
        block_grid_error = (
            symbol_lipschitz_bound
            * half_cell_width
            * block_cauchy_mass
        )
        sampled_negative_trace += block_sample
        covered_grid_error_bound += block_grid_error
        records.append({
            "block_index": block_index,
            "absolute_height_left": left,
            "absolute_height_right": right,
            "two_sided_cauchy_mass": block_cauchy_mass,
            "sampled_negative_trace": block_sample,
            "symbol_minimum_on_midpoints": block_symbol_minimum,
            "negative_cell_fraction": (
                negative_cell_count / (2 * cells_per_block)
            ),
            "grid_error_bound": block_grid_error,
            "covered_negative_trace_lower_bound": max(
                0.0, block_sample - block_grid_error
            ),
            "covered_negative_trace_upper_bound": (
                block_sample + block_grid_error
            ),
        })
    height_cutoff = float(edges[-1])
    covered_cauchy_mass = float(2 * math.atan(height_cutoff) / math.pi)
    cauchy_tail_mass = 1 - covered_cauchy_mass
    tail_negative_trace_bound = coefficient_absolute_mass * cauchy_tail_mass
    return {
        "positive_block_edges": edges,
        "cells_per_block": cells_per_block,
        "chunk_size": chunk_size,
        "records": records,
        "height_cutoff": height_cutoff,
        "symbol_lipschitz_bound": symbol_lipschitz_bound,
        "coefficient_absolute_mass": coefficient_absolute_mass,
        "covered_cauchy_mass": covered_cauchy_mass,
        "cauchy_tail_mass": cauchy_tail_mass,
        "sampled_covered_negative_trace": sampled_negative_trace,
        "covered_grid_error_bound": covered_grid_error_bound,
        "covered_negative_trace_lower_bound": max(
            0.0, sampled_negative_trace - covered_grid_error_bound
        ),
        "covered_negative_trace_upper_bound": (
            sampled_negative_trace + covered_grid_error_bound
        ),
        "tail_negative_trace_bound": tail_negative_trace_bound,
        "full_negative_trace_upper_bound": (
            sampled_negative_trace
            + covered_grid_error_bound
            + tail_negative_trace_bound
        ),
    }


def stationary_modulated_interval_energy(
    lag_nodes: list[mp.mpf],
    coefficients: list[mp.mpc],
    center_height: mp.mpf,
    log_window_width: mp.mpf,
) -> dict[str, object]:
    """Exact triangular-Gram energy of modulated sliding lag windows.

    For the atomic lag measure ``nu=sum c_j delta_{lambda_j}``, put

        nu_tau=sum c_j exp(-i*tau*lambda_j) delta_{lambda_j}.

    The integral over all window origins of

        |nu_tau([x,x+h])|^2

    is the positive quadratic form with kernel

        exp(-i*tau*(lambda_j-lambda_k))
        * max(0, h-|lambda_j-lambda_k|).

    This is the finite arithmetic energy appearing on the right side of the
    frequency-shifted Gallagher lemma.
    """
    if not lag_nodes or len(lag_nodes) != len(coefficients):
        raise ValueError("nodes and coefficients must be nonempty and aligned")
    center_height = mp.mpf(center_height)
    log_window_width = mp.mpf(log_window_width)
    if log_window_width <= 0:
        raise ValueError("log window width must be positive")
    nodes = [mp.mpf(node) for node in lag_nodes]
    if any(not mp.isfinite(node) for node in nodes):
        raise ValueError("lag nodes must be finite")
    values = [mp.mpc(coefficient) for coefficient in coefficients]
    phased_values = [
        coefficient * mp.exp(-1j * center_height * node)
        for node, coefficient in zip(nodes, values)
    ]
    diagonal_energy = log_window_width * mp.fsum(
        abs(value) ** 2 for value in phased_values
    )
    ordered = sorted(zip(nodes, phased_values), key=lambda item: item[0])
    active_conjugate_sum = mp.mpc(0)
    active_lag_conjugate_sum = mp.mpc(0)
    left = 0
    strict_upper_triangle = mp.mpc(0)
    for index, (node, value) in enumerate(ordered):
        while (
            left < index
            and node - ordered[left][0] >= log_window_width
        ):
            old_node, old_value = ordered[left]
            active_conjugate_sum -= mp.conj(old_value)
            active_lag_conjugate_sum -= old_node * mp.conj(old_value)
            left += 1
        strict_upper_triangle += value * (
            (log_window_width - node) * active_conjugate_sum
            + active_lag_conjugate_sum
        )
        active_conjugate_sum += mp.conj(value)
        active_lag_conjugate_sum += node * mp.conj(value)
    energy_complex = (
        diagonal_energy
        + strict_upper_triangle
        + mp.conj(strict_upper_triangle)
    )
    tolerance = 100 * mp.eps * max(
        mp.mpf("1"), abs(energy_complex), abs(diagonal_energy)
    )
    if abs(mp.im(energy_complex)) > tolerance:
        raise ArithmeticError("modulated interval energy is not real")
    energy = mp.re(energy_complex)
    if -tolerance <= energy < 0:
        energy = mp.mpf("0")
    if energy < 0:
        raise ArithmeticError("modulated interval energy became negative")
    return {
        "lag_nodes": nodes,
        "coefficients": values,
        "center_height": center_height,
        "log_window_width": log_window_width,
        "phased_coefficients": phased_values,
        "modulated_interval_energy": energy,
        "diagonal_energy": diagonal_energy,
        "off_diagonal_energy": energy - diagonal_energy,
        "strict_upper_triangle_energy": strict_upper_triangle,
        "algorithm": "sorted sliding prefix O(m log m)",
        "imaginary_residual": abs(mp.im(energy_complex)),
        "positivity_tolerance": tolerance,
    }


def gallagher_fejer_band_constant(
    half_bandwidth: mp.mpf,
    relative_window_parameter: mp.mpf = mp.mpf("0.25"),
) -> dict[str, mp.mpf]:
    """Explicit Fejer lower bound behind the shifted Gallagher estimate.

    Put ``h=theta/B``.  The exact sliding-window Plancherel kernel is

        W_h(s)=|int_0^h exp(-isx) dx|^2.

    On ``|s|<=B`` it is at least
    ``h^2*sinc(theta/2)^2`` (with ``sinc(x)=sin(x)/x``).  Consequently

        int_{tau-B}^{tau+B}|D(t)|^2 dt
          <= C_theta*B^2*G,

    where ``C_theta=2*pi/(theta^2*sinc(theta/2)^2)`` and ``G`` is the
    modulated sliding-window energy.
    """
    half_bandwidth = mp.mpf(half_bandwidth)
    relative_window_parameter = mp.mpf(relative_window_parameter)
    if half_bandwidth <= 0:
        raise ValueError("half bandwidth must be positive")
    if not 0 < relative_window_parameter < mp.pi:
        raise ValueError("relative window parameter must lie in (0, pi)")
    log_window_width = relative_window_parameter / half_bandwidth
    half_parameter = relative_window_parameter / 2
    sinc_value = mp.sin(half_parameter) / half_parameter
    minimum_fejer_weight = log_window_width**2 * sinc_value**2
    dimensionless_constant = 2 * mp.pi / (
        relative_window_parameter**2 * sinc_value**2
    )
    return {
        "half_bandwidth": half_bandwidth,
        "relative_window_parameter": relative_window_parameter,
        "log_window_width": log_window_width,
        "sinc_half_parameter": sinc_value,
        "minimum_fejer_weight_on_band": minimum_fejer_weight,
        "dimensionless_gallagher_constant": dimensionless_constant,
        "band_energy_multiplier": (
            dimensionless_constant * half_bandwidth**2
        ),
    }


def stationary_cauchy_symbol_moments(
    lag_nodes: list[mp.mpf],
    coefficients: list[mp.mpc],
) -> dict[str, object]:
    """Exact Cauchy first and second moments of a stationary symbol.

    If ``Q(t)=sum c_j exp(-it lambda_j)`` and ``P=Re Q``, then for
    ``dmu=dt/(pi*(1+t^2))`` the Fourier identity

        int exp(-it*x)dmu(t) = exp(-abs(x))

    gives exact finite formulas for ``int P dmu`` and ``int P^2 dmu``.
    The latter is a positive quadratic energy and bounds the capped
    negative mass by Cauchy--Schwarz.
    """
    if not lag_nodes or len(lag_nodes) != len(coefficients):
        raise ValueError("nodes and coefficients must be nonempty and aligned")
    nodes = [mp.mpf(node) for node in lag_nodes]
    values = [mp.mpc(coefficient) for coefficient in coefficients]
    if any(node < 0 for node in nodes):
        raise ValueError("stationary orbit lags must be nonnegative")
    ordered = sorted(zip(nodes, values), key=lambda item: item[0])
    cauchy_mean_complex = mp.fsum(
        coefficient * mp.exp(-abs(node))
        for node, coefficient in ordered
    )
    diagonal_modulus_mass = mp.fsum(
        abs(coefficient) ** 2 for _, coefficient in ordered
    )
    conjugated_exponential_prefix = mp.mpc(0)
    ordered_cross_sum = mp.mpc(0)
    for node, coefficient in ordered:
        ordered_cross_sum += (
            coefficient
            * mp.exp(-node)
            * conjugated_exponential_prefix
        )
        conjugated_exponential_prefix += (
            mp.conj(coefficient) * mp.exp(node)
        )
    modulus_square_moment = (
        diagonal_modulus_mass + 2 * mp.re(ordered_cross_sum)
    )
    analytic_square_moment = cauchy_mean_complex**2
    mean = mp.re(cauchy_mean_complex)
    direct_second_moment = (
        mp.re(modulus_square_moment)
        + mp.re(analytic_square_moment)
    ) / 2
    tolerance = mp.mpf("1e-40") * max(
        mp.mpf("1"), abs(modulus_square_moment), abs(analytic_square_moment)
    )
    green_tail_energy = (
        mp.re(modulus_square_moment) - abs(cauchy_mean_complex) ** 2
    ) / 2
    if -tolerance <= green_tail_energy < 0:
        green_tail_energy = mp.mpf("0")
    if green_tail_energy < 0:
        raise ArithmeticError("the Cauchy Green tail energy became negative")
    second_moment = mean**2 + green_tail_energy
    if abs(second_moment - direct_second_moment) > tolerance:
        raise ArithmeticError("the two Cauchy second-moment formulas disagree")
    if -tolerance <= second_moment < 0:
        second_moment = mp.mpf("0")
    if second_moment < 0:
        raise ArithmeticError("the Cauchy second moment became negative")
    centered_variance = second_moment - mean**2
    if -tolerance <= centered_variance < 0:
        centered_variance = mp.mpf("0")
    if centered_variance < 0:
        raise ArithmeticError("the Cauchy centered variance became negative")
    negative_mass_upper_bound = mp.sqrt(second_moment)
    return {
        "cauchy_mean_complex": cauchy_mean_complex,
        "cauchy_mean": mean,
        "modulus_square_moment": modulus_square_moment,
        "analytic_square_moment": analytic_square_moment,
        "cauchy_boundary_real_square": mean**2,
        "cauchy_green_tail_energy": green_tail_energy,
        "cauchy_second_moment": second_moment,
        "cauchy_centered_variance": centered_variance,
        "stationary_negative_mass_upper_bound": negative_mass_upper_bound,
        "cauchy_defect_upper_bound": mp.pi * negative_mass_upper_bound,
    }


def stationary_signed_orbit_laplacian_audit(
    lag_nodes: list[mp.mpf],
    coefficients: list[mp.mpc],
    heights: list[mp.mpf],
    imaginary_tolerance: mp.mpf = mp.mpf("1e-30"),
) -> dict[str, object]:
    """Exact signed-edge Laplacian decomposition on sampled characters.

    For real coefficients and nonnegative lags,

        P(t) = degree + D_negative(t) - D_positive(t),

    where ``D_positive`` uses positive cosine coefficients and
    ``D_negative`` uses their negative counterparts; both are sums of
    nonnegative orbit-edge energies ``weight*(1-cos(t*lag))``.
    """
    if not lag_nodes or len(lag_nodes) != len(coefficients):
        raise ValueError("nodes and coefficients must be nonempty and aligned")
    if not heights:
        raise ValueError("heights must be nonempty")
    imaginary_tolerance = mp.mpf(imaginary_tolerance)
    if imaginary_tolerance < 0:
        raise ValueError("imaginary tolerance must be nonnegative")
    nodes = [mp.mpf(node) for node in lag_nodes]
    if any(node < 0 for node in nodes):
        raise ValueError("orbit lags must be nonnegative")
    real_coefficients = []
    for coefficient in coefficients:
        coefficient = mp.mpc(coefficient)
        if abs(mp.im(coefficient)) > imaginary_tolerance:
            raise ValueError("the scalar Laplacian audit requires real coefficients")
        real_coefficients.append(mp.re(coefficient))
    degree_anomaly = mp.fsum(real_coefficients)
    positive_edge_mass = mp.fsum(
        coefficient for coefficient in real_coefficients if coefficient > 0
    )
    negative_edge_mass = mp.fsum(
        -coefficient for coefficient in real_coefficients if coefficient < 0
    )
    records = []
    maximum_identity_error = mp.mpf("0")
    minimum_laplacian_margin = mp.inf
    minimum_symbol = mp.inf
    for height in heights:
        height = mp.mpf(height)
        positive_laplacian = mp.fsum(
            coefficient * (1 - mp.cos(height * node))
            for node, coefficient in zip(nodes, real_coefficients)
            if coefficient > 0
        )
        negative_laplacian = mp.fsum(
            -coefficient * (1 - mp.cos(height * node))
            for node, coefficient in zip(nodes, real_coefficients)
            if coefficient < 0
        )
        symbol = mp.fsum(
            coefficient * mp.cos(height * node)
            for node, coefficient in zip(nodes, real_coefficients)
        )
        laplacian_margin = negative_laplacian - positive_laplacian
        reconstructed_symbol = degree_anomaly + laplacian_margin
        identity_error = abs(symbol - reconstructed_symbol)
        maximum_identity_error = max(maximum_identity_error, identity_error)
        minimum_laplacian_margin = min(
            minimum_laplacian_margin, laplacian_margin
        )
        minimum_symbol = min(minimum_symbol, symbol)
        records.append(
            {
                "height": height,
                "symbol": symbol,
                "positive_coefficient_laplacian": positive_laplacian,
                "negative_coefficient_laplacian": negative_laplacian,
                "laplacian_domination_margin": laplacian_margin,
                "reconstructed_symbol": reconstructed_symbol,
                "identity_error": identity_error,
            }
        )
    return {
        "degree_anomaly": degree_anomaly,
        "positive_edge_mass": positive_edge_mass,
        "negative_edge_mass": negative_edge_mass,
        "records": records,
        "minimum_laplacian_domination_margin": minimum_laplacian_margin,
        "minimum_symbol": minimum_symbol,
        "maximum_identity_error": maximum_identity_error,
        "sampled_laplacian_domination_holds": (
            minimum_laplacian_margin >= -imaginary_tolerance
        ),
    }


def single_abel_zero_wave_half_period_certificate(
    horizontal_displacement: mp.mpf,
    horizontal_offset: mp.mpf,
    ordinate: mp.mpf,
    scale: mp.mpf,
    multiplicity: int = 1,
    relative_remainder_bound: mp.mpf = mp.mpf("0"),
) -> dict[str, object]:
    """Explicit negative-well bound for one Abel zero-residue wave.

    Put ``b=horizontal_displacement-horizontal_offset`` and consider

        m Gamma(b+i(gamma-t)) Y^(b+i(gamma-t)) + R_Y(t).

    On the carrier half-period

        t=gamma+u/log(Y),  2*pi/3 <= u <= 4*pi/3,

    the cosine is at most ``-1/2``.  Euler's differentiated Gamma integral
    gives the uniform derivative majorant

        |Gamma'(b+iv)| <= int exp(-x) x^(b-1) |log x| dx.

    If ``|Re R_Y(t)| <= relative_remainder_bound * Y^b`` there, the returned
    positive margin produces a rigorous formula-level lower bound for the
    Cauchy defect ``int [-Re F(t)]_+/(1+t^2) dt``.  Numerical evaluation is
    not interval arithmetic; the theorem using these formulas is proved in
    notes/144-abel-zero-wave-obstruction.md.
    """
    horizontal_displacement = mp.mpf(horizontal_displacement)
    horizontal_offset = mp.mpf(horizontal_offset)
    ordinate = mp.mpf(ordinate)
    scale = mp.mpf(scale)
    relative_remainder_bound = mp.mpf(relative_remainder_bound)
    if horizontal_displacement <= horizontal_offset:
        raise ValueError(
            "the zero must lie strictly to the right of the sampling line"
        )
    if scale <= 1:
        raise ValueError("scale must exceed one")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    if relative_remainder_bound < 0:
        raise ValueError("relative remainder bound must be nonnegative")
    exponent = horizontal_displacement - horizontal_offset
    logarithm = mp.log(scale)
    phase_left = 2 * mp.pi / 3
    phase_right = 4 * mp.pi / 3
    phase_length = phase_right - phase_left
    gamma_value = mp.gamma(exponent)
    gamma_log_moment_bound = (
        mp.quad(
            lambda variable: (
                mp.exp(-variable)
                * variable ** (exponent - 1)
                * abs(mp.log(variable))
            ),
            [0, 1],
        )
        + mp.quad(
            lambda variable: (
                mp.exp(-variable)
                * variable ** (exponent - 1)
                * mp.log(variable)
            ),
            [1, mp.inf],
        )
    )
    gamma_variation_bound = (
        multiplicity
        * gamma_log_moment_bound
        * phase_right
        / logarithm
    )
    cosine_negative_depth = multiplicity * gamma_value / 2
    normalized_pointwise_negative_margin = max(
        mp.mpf("0"),
        cosine_negative_depth
        - gamma_variation_bound
        - relative_remainder_bound,
    )
    height_radius = phase_right / logarithm
    cauchy_denominator_upper = 1 + (abs(ordinate) + height_radius) ** 2
    normalized_cauchy_defect_lower_bound = (
        normalized_pointwise_negative_margin
        * phase_length
        / (logarithm * cauchy_denominator_upper)
    )
    amplitude = scale**exponent
    return {
        "horizontal_displacement": horizontal_displacement,
        "horizontal_offset": horizontal_offset,
        "residue_exponent": exponent,
        "ordinate": ordinate,
        "scale": scale,
        "log_scale": logarithm,
        "multiplicity": multiplicity,
        "relative_remainder_bound": relative_remainder_bound,
        "phase_left": phase_left,
        "phase_right": phase_right,
        "height_interval_left": ordinate + phase_left / logarithm,
        "height_interval_right": ordinate + phase_right / logarithm,
        "gamma_value": gamma_value,
        "gamma_log_moment_bound": gamma_log_moment_bound,
        "gamma_variation_bound": gamma_variation_bound,
        "cosine_negative_depth": cosine_negative_depth,
        "normalized_pointwise_negative_margin": (
            normalized_pointwise_negative_margin
        ),
        "cauchy_denominator_upper": cauchy_denominator_upper,
        "normalized_cauchy_defect_lower_bound": (
            normalized_cauchy_defect_lower_bound
        ),
        "cauchy_defect_lower_bound": (
            amplitude * normalized_cauchy_defect_lower_bound
        ),
        "capped_stationary_negative_minimum_upper": (
            -amplitude * normalized_cauchy_defect_lower_bound / mp.pi
        ),
        "has_positive_certificate": (
            normalized_pointwise_negative_margin > 0
        ),
    }


def gamma_translate_l2_gram(
    exponent: mp.mpf,
    ordinates: list[mp.mpf],
) -> mp.matrix:
    """Exact full-line L2 Gram of translated Abel residue envelopes.

    For ``g_gamma(t)=Gamma(b+i*(gamma-t))``, Plancherel and Euler's Gamma
    integral give

        <g_gamma,g_eta>
          = 2*pi*2^(-2*b-i*(gamma-eta))
            * Gamma(2*b+i*(gamma-eta)).

    This positive Gram is a finite shadow of the noncancellation argument
    for countable rightmost residue packets in notes/144.
    """
    exponent = mp.mpf(exponent)
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    if not ordinates:
        raise ValueError("ordinates must be nonempty")
    ordinates = [mp.mpf(ordinate) for ordinate in ordinates]
    gram = mp.matrix(len(ordinates), len(ordinates))
    for row, gamma in enumerate(ordinates):
        for column, eta in enumerate(ordinates):
            difference = gamma - eta
            gram[row, column] = (
                2
                * mp.pi
                * mp.power(2, -2 * exponent - 1j * difference)
                * mp.gamma(2 * exponent + 1j * difference)
            )
    return gram


def zeta_abel_capped_loewner_quadrature(
    horizontal_offset: mp.mpf,
    scale: mp.mpf,
    integer_cutoff: int,
    pole_end: mp.mpf,
    pole_cells: int,
    gamma_start: mp.mpf,
    gamma_end: mp.mpf,
    gamma_cells: int,
    continuum_end: mp.mpf,
    continuum_cells: int,
) -> dict[str, object]:
    """Finite capped-Loewner audit of the full Abel Hodge functional.

    Pole, regularized Gamma, and continuum orbit integrals are replaced by
    cell-mass midpoint correlations.  The Cauchy spectral cap gives the
    uniform modulus

        |r(a)-r(b)| <= sqrt(2*(1-exp(-|a-b|))).

    The interval ``[0,gamma_start]`` is bounded jointly, preserving the
    removable cancellation in the digamma numerator.  Returned error
    formulas are analytic majorants assuming exact scalar cell integrals;
    the mpmath evaluation itself is not interval arithmetic.
    """
    horizontal_offset = mp.mpf(horizontal_offset)
    scale = mp.mpf(scale)
    pole_end = mp.mpf(pole_end)
    gamma_start = mp.mpf(gamma_start)
    gamma_end = mp.mpf(gamma_end)
    continuum_end = mp.mpf(continuum_end)
    if horizontal_offset <= 0 or scale <= 0:
        raise ValueError("horizontal_offset and scale must be positive")
    if integer_cutoff < 3:
        raise ValueError("integer_cutoff must be at least three")
    if pole_end <= 0 or continuum_end <= 0:
        raise ValueError("pole and continuum ends must be positive")
    if gamma_start <= 0 or gamma_end <= gamma_start:
        raise ValueError("gamma interval must satisfy 0<start<end")
    if pole_cells < 1 or gamma_cells < 1 or continuum_cells < 1:
        raise ValueError("all quadrature cell counts must be positive")
    sigma = mp.mpf("0.5") + horizontal_offset
    coefficients_by_node: dict[mp.mpf, mp.mpc] = {
        mp.mpf("0"): -(
            mp.log(mp.pi) + mp.euler
        ) / 2
    }
    def add_coefficient(node: mp.mpf, coefficient: mp.mpc) -> None:
        node = mp.mpf(node)
        coefficients_by_node[node] = (
            coefficients_by_node.get(node, mp.mpc(0)) + coefficient
        )

    def cap_modulus(maximum_distance: mp.mpf) -> mp.mpf:
        return cauchy_capped_correlation_modulus_bound(
            maximum_distance
        )["combined_modulus_bound"]

    pole_width = pole_end / pole_cells
    pole_quadrature_error = mp.mpf("0")
    for cell in range(pole_cells):
        left = cell * pole_width
        right = (cell + 1) * pole_width
        midpoint = (left + right) / 2
        mass = (
            mp.exp(-sigma * left) - mp.exp(-sigma * right)
        ) / sigma
        add_coefficient(midpoint, mass)
        pole_quadrature_error += mass * cap_modulus(pole_width / 2)
    pole_tail_bound = mp.exp(-sigma * pole_end) / sigma

    gamma_width = (gamma_end - gamma_start) / gamma_cells
    gamma_quadrature_error = mp.mpf("0")
    for cell in range(gamma_cells):
        left = gamma_start + cell * gamma_width
        right = left + gamma_width
        midpoint = (left + right) / 2
        positive_mass = (
            mp.log(1 - mp.exp(-right))
            - mp.log(1 - mp.exp(-left))
        ) / 2
        negative_mass = mp.quad(
            lambda variable: (
                mp.exp(-sigma * variable / 2)
                / (2 * (1 - mp.exp(-variable)))
            ),
            [left, right],
        )
        add_coefficient(mp.mpf("0"), positive_mass)
        add_coefficient(midpoint / 2, -negative_mass)
        gamma_quadrature_error += (
            negative_mass * cap_modulus(gamma_width / 4)
        )
    gamma_small_bound = (
        mp.sqrt(gamma_start)
        + abs(1 - sigma / 2)
        * mp.exp(max(mp.mpf("0"), 1 - sigma / 2) * gamma_start)
        * gamma_start
        / 2
    )
    gamma_tail_bound = mp.quad(
        lambda variable: (
            mp.exp(-variable)
            + mp.exp(-sigma * variable / 2)
        ) / (2 * (1 - mp.exp(-variable))),
        [gamma_end, mp.inf],
    )

    continuum_width = continuum_end / continuum_cells
    continuum_quadrature_error = mp.mpf("0")
    continuum_shape = 1 - sigma
    continuum_scale_factor = mp.power(scale, continuum_shape)
    for cell in range(continuum_cells):
        left = cell * continuum_width
        right = (cell + 1) * continuum_width
        midpoint = (left + right) / 2
        mass = continuum_scale_factor * mp.gammainc(
            continuum_shape,
            mp.exp(left) / scale,
            mp.exp(right) / scale,
        )
        add_coefficient(midpoint, mass)
        continuum_quadrature_error += (
            mass * cap_modulus(continuum_width / 2)
        )
    continuum_tail_bound = continuum_scale_factor * mp.gammainc(
        continuum_shape,
        mp.exp(continuum_end) / scale,
        mp.inf,
    )

    for integer in range(2, integer_cutoff + 1):
        mangoldt = von_mangoldt(integer)
        if mangoldt:
            add_coefficient(
                mp.log(integer),
                -mangoldt
                * mp.power(integer, -sigma)
                * mp.exp(-mp.mpf(integer) / scale),
            )
    cutoff = mp.mpf(integer_cutoff)
    monotonicity_margin = sigma + cutoff / scale - 1 / mp.log(cutoff)
    if monotonicity_margin <= 0:
        raise ValueError(
            "integer_cutoff is too small for the monotone prime-tail bound"
        )
    prime_tail_bound = mp.quad(
        lambda variable: (
            mp.log(variable)
            * mp.power(variable, -sigma)
            * mp.exp(-variable / scale)
        ),
        [cutoff, mp.inf],
    )

    nodes = sorted(coefficients_by_node)
    if nodes[0] != 0:
        raise AssertionError("the zero lag must be present")
    coefficients = [coefficients_by_node[node] for node in nodes]
    cap_gram = cauchy_correlation_dominating_gram(nodes)
    objective_gram = correlation_first_column_objective_gram(coefficients)
    loewner_data = loewner_interval_linear_minimum_numpy(
        cap_gram, objective_gram
    )
    optimizer_stationarity = correlation_stationarity_defect(
        nodes, loewner_data["optimizer_gram"]
    )
    constant_probe_value = mp.re(mp.fsum(
        coefficient * mp.exp(-node)
        for node, coefficient in zip(nodes, coefficients)
    ))
    center_data = zeta_abel_prime_impedance(
        mp.mpc(horizontal_offset + 1, 0), scale, integer_cutoff
    )
    center_real_value = mp.re(center_data["impedance"])
    quadrature_error_bound = (
        pole_quadrature_error
        + gamma_small_bound
        + gamma_quadrature_error
        + continuum_quadrature_error
    )
    tail_error_bound = (
        pole_tail_bound
        + gamma_tail_bound
        + continuum_tail_bound
        + prime_tail_bound
    )
    uniform_error_bound = quadrature_error_bound + tail_error_bound
    return {
        "horizontal_offset": horizontal_offset,
        "scale": scale,
        "integer_cutoff": integer_cutoff,
        "sigma": sigma,
        "lag_nodes": nodes,
        "correlation_coefficients": coefficients,
        "cap_gram": cap_gram,
        "objective_gram": objective_gram,
        "loewner_data": loewner_data,
        "optimizer_stationarity": optimizer_stationarity,
        "relaxed_minimum_objective": loewner_data["minimum_objective"],
        "pole_quadrature_error_bound": pole_quadrature_error,
        "pole_tail_bound": pole_tail_bound,
        "gamma_small_interval_bound": gamma_small_bound,
        "gamma_quadrature_error_bound": gamma_quadrature_error,
        "gamma_tail_bound": gamma_tail_bound,
        "continuum_quadrature_error_bound": continuum_quadrature_error,
        "continuum_tail_bound": continuum_tail_bound,
        "prime_tail_bound": prime_tail_bound,
        "quadrature_error_bound": quadrature_error_bound,
        "tail_error_bound": tail_error_bound,
        "uniform_functional_error_bound": uniform_error_bound,
        "constant_probe_quadrature_value": constant_probe_value,
        "constant_probe_exact_truncated_value": center_real_value,
        "constant_probe_absolute_error": abs(
            constant_probe_value - center_real_value
        ),
    }


def zeta_abel_shared_lag_loewner_quadrature(
    horizontal_offset: mp.mpf,
    scale: mp.mpf,
    integer_cutoff: int,
    lag_start: mp.mpf,
    lag_end: mp.mpf,
    lag_cells: int,
    geometric_mesh: bool = True,
    compute_loewner_relaxation: bool = True,
) -> dict[str, object]:
    """Shared-lag capped quadrature preserving pole--Gamma cancellation.

    After setting ``t=2*lambda`` in the digamma current, the pole orbit and
    the negative Gamma orbit combine exactly.  The nonzero-lag continuous
    weight is

        exp((1-sigma)lambda-exp(lambda)/Y)
          - exp(-(sigma+2)lambda)/(1-exp(-2lambda)).

    Pole, Gamma, and continuum therefore share one lag mesh.  A geometric
    mesh grades cells toward the removable origin singularity.
    """
    horizontal_offset = mp.mpf(horizontal_offset)
    scale = mp.mpf(scale)
    lag_start = mp.mpf(lag_start)
    lag_end = mp.mpf(lag_end)
    if horizontal_offset <= 0 or scale <= 0:
        raise ValueError("horizontal_offset and scale must be positive")
    if integer_cutoff < 3:
        raise ValueError("integer_cutoff must be at least three")
    if lag_start <= 0 or lag_end <= lag_start:
        raise ValueError("lag interval must satisfy 0<start<end")
    if lag_cells < 1:
        raise ValueError("lag_cells must be positive")
    sigma = mp.mpf("0.5") + horizontal_offset
    continuum_shape = 1 - sigma
    continuum_scale_factor = mp.power(scale, continuum_shape)
    if geometric_mesh:
        lag_ratio = mp.power(lag_end / lag_start, 1 / lag_cells)
        edges = [
            lag_start * mp.power(lag_ratio, index)
            for index in range(lag_cells + 1)
        ]
        edges[-1] = lag_end
    else:
        lag_width = (lag_end - lag_start) / lag_cells
        edges = [
            lag_start + index * lag_width
            for index in range(lag_cells + 1)
        ]
    coefficients_by_node: dict[mp.mpf, mp.mpc] = {
        mp.mpf("0"): -(
            mp.log(mp.pi) + mp.euler
        ) / 2
    }
    prime_continuum_by_node: dict[mp.mpf, mp.mpc] = {}

    def add_coefficient(node: mp.mpf, coefficient: mp.mpc) -> None:
        node = mp.mpf(node)
        coefficients_by_node[node] = (
            coefficients_by_node.get(node, mp.mpc(0)) + coefficient
        )

    def add_prime_continuum_coefficient(
        node: mp.mpf, coefficient: mp.mpc
    ) -> None:
        node = mp.mpf(node)
        prime_continuum_by_node[node] = (
            prime_continuum_by_node.get(node, mp.mpc(0)) + coefficient
        )

    def continuum_mass(left: mp.mpf, right: mp.mpf) -> mp.mpf:
        return continuum_scale_factor * mp.gammainc(
            continuum_shape,
            mp.exp(left) / scale,
            mp.exp(right) / scale,
        )

    def residual_gamma_weight(variable: mp.mpf) -> mp.mpf:
        return (
            mp.exp(-(sigma + 2) * variable)
            / (1 - mp.exp(-2 * variable))
        )

    def combined_orbit_weight(variable: mp.mpf) -> mp.mpf:
        return (
            mp.exp((1 - sigma) * variable)
            * mp.exp(-mp.exp(variable) / scale)
            - residual_gamma_weight(variable)
        )

    zero_lag_coefficient = coefficients_by_node[mp.mpf("0")]
    pole_small_mass = (
        1 - mp.exp(-sigma * lag_start)
    ) / sigma
    continuum_small_mass = continuum_mass(mp.mpf("0"), lag_start)
    add_prime_continuum_coefficient(
        mp.mpf("0"), -continuum_small_mass
    )
    zero_lag_coefficient += pole_small_mass + continuum_small_mass
    gamma_positive_mass = (
        mp.log(1 - mp.exp(-2 * lag_end))
        - mp.log(1 - mp.exp(-2 * lag_start))
    ) / 2
    zero_lag_coefficient += gamma_positive_mass
    coefficients_by_node[mp.mpf("0")] = zero_lag_coefficient

    small_modulus = cauchy_capped_correlation_modulus_bound(
        lag_start
    )["combined_modulus_bound"]
    small_pole_continuum_error = (
        pole_small_mass + continuum_small_mass
    ) * small_modulus
    gamma_origin_end = 2 * lag_start
    gamma_small_bound = (
        mp.sqrt(gamma_origin_end)
        + abs(1 - sigma / 2)
        * mp.exp(
            max(mp.mpf("0"), 1 - sigma / 2) * gamma_origin_end
        )
        * gamma_origin_end
        / 2
    )

    lag_quadrature_error = mp.mpf("0")
    cell_variation_masses = []
    for cell in range(lag_cells):
        left = edges[cell]
        right = edges[cell + 1]
        midpoint = (left + right) / 2
        continuum_cell_mass = continuum_mass(left, right)
        residual_cell_mass = mp.quad(
            residual_gamma_weight, [left, right]
        )
        signed_cell_mass = continuum_cell_mass - residual_cell_mass
        variation_mass = mp.quad(
            lambda variable: abs(combined_orbit_weight(variable)),
            [left, right],
        )
        add_coefficient(midpoint, signed_cell_mass)
        add_prime_continuum_coefficient(midpoint, -continuum_cell_mass)
        cell_modulus = cauchy_capped_correlation_modulus_bound(
            (right - left) / 2
        )["combined_modulus_bound"]
        lag_quadrature_error += variation_mass * cell_modulus
        cell_variation_masses.append(variation_mass)

    gamma_positive_tail_bound = -mp.log(
        1 - mp.exp(-2 * lag_end)
    ) / 2
    residual_gamma_tail_bound = mp.quad(
        residual_gamma_weight, [lag_end, mp.inf]
    )
    continuum_tail_bound = continuum_scale_factor * mp.gammainc(
        continuum_shape,
        mp.exp(lag_end) / scale,
        mp.inf,
    )

    for integer in range(2, integer_cutoff + 1):
        mangoldt = von_mangoldt(integer)
        if mangoldt:
            prime_atom = (
                mangoldt
                * mp.power(integer, -sigma)
                * mp.exp(-mp.mpf(integer) / scale)
            )
            add_coefficient(
                mp.log(integer),
                -prime_atom,
            )
            add_prime_continuum_coefficient(mp.log(integer), prime_atom)
    cutoff = mp.mpf(integer_cutoff)
    monotonicity_margin = sigma + cutoff / scale - 1 / mp.log(cutoff)
    if monotonicity_margin <= 0:
        raise ValueError(
            "integer_cutoff is too small for the monotone prime-tail bound"
        )
    prime_tail_bound = mp.quad(
        lambda variable: (
            mp.log(variable)
            * mp.power(variable, -sigma)
            * mp.exp(-variable / scale)
        ),
        [cutoff, mp.inf],
    )

    nodes = sorted(coefficients_by_node)
    coefficients = [coefficients_by_node[node] for node in nodes]
    prime_continuum_nodes = sorted(prime_continuum_by_node)
    prime_continuum_coefficients = [
        prime_continuum_by_node[node] for node in prime_continuum_nodes
    ]
    cap_gram = None
    objective_gram = None
    loewner_data = None
    optimizer_stationarity = None
    relaxed_minimum_objective = None
    if compute_loewner_relaxation:
        cap_gram = cauchy_correlation_dominating_gram(nodes)
        objective_gram = correlation_first_column_objective_gram(coefficients)
        loewner_data = loewner_interval_linear_minimum_numpy(
            cap_gram, objective_gram
        )
        optimizer_stationarity = correlation_stationarity_defect(
            nodes, loewner_data["optimizer_gram"]
        )
        relaxed_minimum_objective = loewner_data["minimum_objective"]
    constant_probe_value = mp.re(mp.fsum(
        coefficient * mp.exp(-node)
        for node, coefficient in zip(nodes, coefficients)
    ))
    center_data = zeta_abel_prime_impedance(
        mp.mpc(horizontal_offset + 1, 0), scale, integer_cutoff
    )
    center_real_value = mp.re(center_data["impedance"])
    quadrature_error_bound = (
        small_pole_continuum_error
        + gamma_small_bound
        + lag_quadrature_error
    )
    tail_error_bound = (
        gamma_positive_tail_bound
        + residual_gamma_tail_bound
        + continuum_tail_bound
        + prime_tail_bound
    )
    uniform_error_bound = quadrature_error_bound + tail_error_bound
    return {
        "horizontal_offset": horizontal_offset,
        "scale": scale,
        "integer_cutoff": integer_cutoff,
        "sigma": sigma,
        "geometric_mesh": geometric_mesh,
        "compute_loewner_relaxation": compute_loewner_relaxation,
        "lag_edges": edges,
        "lag_nodes": nodes,
        "shared_continuous_lag_count": lag_cells,
        "correlation_coefficients": coefficients,
        "prime_continuum_discrepancy_lag_nodes": prime_continuum_nodes,
        "prime_continuum_discrepancy_coefficients": (
            prime_continuum_coefficients
        ),
        "cell_variation_masses": cell_variation_masses,
        "cap_gram": cap_gram,
        "objective_gram": objective_gram,
        "loewner_data": loewner_data,
        "optimizer_stationarity": optimizer_stationarity,
        "relaxed_minimum_objective": relaxed_minimum_objective,
        "small_pole_continuum_error_bound": small_pole_continuum_error,
        "gamma_small_interval_bound": gamma_small_bound,
        "shared_lag_quadrature_error_bound": lag_quadrature_error,
        "gamma_positive_tail_bound": gamma_positive_tail_bound,
        "residual_gamma_tail_bound": residual_gamma_tail_bound,
        "continuum_tail_bound": continuum_tail_bound,
        "prime_tail_bound": prime_tail_bound,
        "quadrature_error_bound": quadrature_error_bound,
        "tail_error_bound": tail_error_bound,
        "uniform_functional_error_bound": uniform_error_bound,
        "constant_probe_quadrature_value": constant_probe_value,
        "constant_probe_exact_truncated_value": center_real_value,
        "constant_probe_absolute_error": abs(
            constant_probe_value - center_real_value
        ),
    }


def zeta_abel_shared_stationary_certificate(
    horizontal_offset: mp.mpf,
    scale: mp.mpf,
    integer_cutoff: int,
    lag_start: mp.mpf,
    lag_end: mp.mpf,
    lag_cells: int,
    height_cutoff: mp.mpf,
    height_cells: int,
    geometric_mesh: bool = True,
    height_chunk_size: int = 4096,
) -> dict[str, object]:
    """Combine shared arithmetic quadrature with the stationary cap minimum."""
    quadrature = zeta_abel_shared_lag_loewner_quadrature(
        horizontal_offset=horizontal_offset,
        scale=scale,
        integer_cutoff=integer_cutoff,
        lag_start=lag_start,
        lag_end=lag_end,
        lag_cells=lag_cells,
        geometric_mesh=geometric_mesh,
        compute_loewner_relaxation=False,
    )
    stationary = stationary_capped_functional_minimum(
        quadrature["lag_nodes"],
        quadrature["correlation_coefficients"],
        height_cutoff=height_cutoff,
        height_cells=height_cells,
        chunk_size=height_chunk_size,
    )
    moments = stationary_cauchy_symbol_moments(
        quadrature["lag_nodes"],
        quadrature["correlation_coefficients"],
    )
    full_hodge_lower_bound = (
        stationary["certified_stationary_lower_bound"]
        - quadrature["uniform_functional_error_bound"]
    )
    total_functional_error = (
        stationary["total_error_bound"]
        + quadrature["uniform_functional_error_bound"]
    )
    sampled_minimum = stationary["sampled_stationary_minimum"]
    defect_over_pi_lower_bound = max(
        mp.mpf("0"),
        -sampled_minimum - total_functional_error,
    )
    defect_over_pi_upper_bound = max(
        mp.mpf("0"),
        -sampled_minimum + total_functional_error,
    )
    return {
        "quadrature": quadrature,
        "stationary": stationary,
        "moments": moments,
        "sampled_stationary_minimum": stationary[
            "sampled_stationary_minimum"
        ],
        "stationary_discretization_error_bound": stationary[
            "total_error_bound"
        ],
        "arithmetic_quadrature_error_bound": quadrature[
            "uniform_functional_error_bound"
        ],
        "total_functional_error_bound": total_functional_error,
        "certified_full_hodge_lower_bound": full_hodge_lower_bound,
        "cauchy_defect_over_pi_lower_bound": (
            defect_over_pi_lower_bound
        ),
        "cauchy_defect_over_pi_upper_bound": (
            defect_over_pi_upper_bound
        ),
        "cauchy_defect_lower_bound": (
            mp.pi * defect_over_pi_lower_bound
        ),
        "cauchy_defect_upper_bound": (
            mp.pi * defect_over_pi_upper_bound
        ),
        "cauchy_defect_over_pi_quadratic_upper_bound": (
            moments["stationary_negative_mass_upper_bound"]
            + quadrature["uniform_functional_error_bound"]
        ),
        "cauchy_defect_quadratic_upper_bound": mp.pi * (
            moments["stationary_negative_mass_upper_bound"]
            + quadrature["uniform_functional_error_bound"]
        ),
    }


def zeta_abel_shared_cauchy_energy_certificate(
    horizontal_offset: mp.mpf,
    scale: mp.mpf,
    integer_cutoff: int,
    lag_start: mp.mpf,
    lag_end: mp.mpf,
    lag_cells: int,
    geometric_mesh: bool = True,
) -> dict[str, object]:
    """Height-free bounded-defect certificate from exact Cauchy moments."""
    quadrature = zeta_abel_shared_lag_loewner_quadrature(
        horizontal_offset=horizontal_offset,
        scale=scale,
        integer_cutoff=integer_cutoff,
        lag_start=lag_start,
        lag_end=lag_end,
        lag_cells=lag_cells,
        geometric_mesh=geometric_mesh,
        compute_loewner_relaxation=False,
    )
    moments = stationary_cauchy_symbol_moments(
        quadrature["lag_nodes"],
        quadrature["correlation_coefficients"],
    )
    defect_over_pi_upper_bound = (
        moments["stationary_negative_mass_upper_bound"]
        + quadrature["uniform_functional_error_bound"]
    )
    return {
        "quadrature": quadrature,
        "moments": moments,
        "arithmetic_quadrature_error_bound": quadrature[
            "uniform_functional_error_bound"
        ],
        "cauchy_defect_over_pi_quadratic_upper_bound": (
            defect_over_pi_upper_bound
        ),
        "cauchy_defect_quadratic_upper_bound": (
            mp.pi * defect_over_pi_upper_bound
        ),
    }


def abel_shared_cofinal_discretization_schedule(
    scale: mp.mpf,
) -> dict[str, object]:
    """Explicit polynomial-size asymptotic schedule for all finite meshes.

    The schedule is deliberately conservative.  It proves that lag and
    height discretization are not logical obstructions: existing Cauchy-cap
    modulus and elementary coefficient-mass bounds make their errors vanish.
    The resulting dimensions are far larger than practical audit sizes.
    """
    scale = mp.mpf(scale)
    if scale <= mp.e:
        raise ValueError("scale must exceed e for the asymptotic schedule")
    logarithm = mp.log(scale)
    horizontal_offset = 1 / (4 + mp.sqrt(logarithm))
    prime_cutoff = int(mp.ceil(scale * logarithm**2))
    lag_start = scale**-4
    lag_end = 3 * logarithm
    lag_cells = int(mp.ceil(scale**4 * logarithm**2))
    height_cutoff = scale**4
    height_step = scale**-4
    height_cells = int(mp.ceil(2 * height_cutoff / height_step))
    lag_log_ratio = mp.log(lag_end / lag_start)
    maximum_lag_width_upper = (
        lag_end * lag_log_ratio / lag_cells
    )
    lag_modulus_upper = cauchy_capped_correlation_modulus_bound(
        maximum_lag_width_upper / 2
    )["combined_modulus_bound"]
    cauchy_height_tail_mass = (
        1 - 2 * mp.atan(height_cutoff) / mp.pi
    )
    return {
        "scale": scale,
        "horizontal_offset": horizontal_offset,
        "horizontal_offset_times_log_scale": (
            horizontal_offset * logarithm
        ),
        "prime_cutoff": prime_cutoff,
        "lag_start": lag_start,
        "lag_end": lag_end,
        "lag_cells": lag_cells,
        "lag_log_ratio": lag_log_ratio,
        "maximum_lag_width_upper": maximum_lag_width_upper,
        "lag_modulus_upper": lag_modulus_upper,
        "height_cutoff": height_cutoff,
        "height_step": height_step,
        "height_cells": height_cells,
        "cauchy_height_tail_mass": cauchy_height_tail_mass,
        "gamma_origin_square_root_scale": mp.sqrt(2 * lag_start),
    }


def weighted_prolate_core_rank_bound(
    bandwidth: mp.mpf,
    negative_mass_bound: mp.mpf,
    complement_tolerance: mp.mpf,
) -> dict[str, object]:
    """Trace/rank bound for a weighted negative-frequency Hodge core.

    For Fourier transforms of L2 functions supported in [-B,B], the operator
    P_B W P_B has trace B*pi^{-1} integral W.  Removing all eigenvectors with
    eigenvalue greater than epsilon leaves negative quadratic-form error at
    most epsilon and needs at most trace/epsilon directions.
    """
    bandwidth = mp.mpf(bandwidth)
    negative_mass_bound = mp.mpf(negative_mass_bound)
    complement_tolerance = mp.mpf(complement_tolerance)
    if bandwidth <= 0:
        raise ValueError("bandwidth must be positive")
    if negative_mass_bound < 0:
        raise ValueError("negative_mass_bound must be nonnegative")
    if complement_tolerance <= 0:
        raise ValueError("complement_tolerance must be positive")
    trace_bound = bandwidth * negative_mass_bound / mp.pi
    rank_bound_real = trace_bound / complement_tolerance
    return {
        "bandwidth": bandwidth,
        "negative_mass_bound": negative_mass_bound,
        "complement_tolerance": complement_tolerance,
        "weighted_concentration_trace_bound": trace_bound,
        "core_rank_bound_real": rank_bound_real,
        "core_rank_bound": int(mp.ceil(rank_bound_real)),
        "complement_negative_error_bound": complement_tolerance,
        "negative_inertia_above_tolerance_bound": int(
            mp.ceil(rank_bound_real)
        ),
    }


def abel_coefficient_square_mass_majorant(
    horizontal_margin: mp.mpf,
) -> dict[str, mp.mpf]:
    """Explicit delta^{-3} majorant for Abel prime coefficient mass.

    Lambda(n)^2 <= log(n)^2 and comparison with
    integral_1^infinity log(x+1)^2 x^{-1-2 delta} dx gives

        sum log(n)^2 n^{-1-2 delta}
        <= log(2)^2/delta + 1/(2 delta^3).
    """
    horizontal_margin = mp.mpf(horizontal_margin)
    if horizontal_margin <= 0:
        raise ValueError("horizontal_margin must be positive")
    explicit_majorant = (
        mp.log(2) ** 2 / horizontal_margin
        + 1 / (2 * horizontal_margin**3)
    )
    return {
        "horizontal_margin": horizontal_margin,
        "explicit_square_mass_majorant": explicit_majorant,
        "delta_cubic_normalization": (
            horizontal_margin**3 * explicit_majorant
        ),
        "simple_delta_inverse_cubic_majorant": (
            horizontal_margin**-3
            if horizontal_margin <= 1
            else explicit_majorant
        ),
    }


def abel_cofinal_scaling_ledger(
    horizontal_margin: mp.mpf,
    log_height: mp.mpf,
    window_mass_prefactor: mp.mpf = mp.mpf("1"),
) -> dict[str, mp.mpf]:
    """Balanced delta->0 ledger for Abel error and relative core rank.

    If integral W <= C_delta T/log(T), choosing
    epsilon=sqrt(C_delta/log(T)) makes both the complement error and the
    core/Shannon relative-dimension bound equal to this balanced scale.
    ``window_mass_prefactor`` records constants from the analytic window
    estimate rather than silently treating them as one.
    """
    horizontal_margin = mp.mpf(horizontal_margin)
    log_height = mp.mpf(log_height)
    window_mass_prefactor = mp.mpf(window_mass_prefactor)
    if log_height <= 0:
        raise ValueError("log_height must be positive")
    if window_mass_prefactor <= 0:
        raise ValueError("window_mass_prefactor must be positive")
    mass_data = abel_coefficient_square_mass_majorant(horizontal_margin)
    effective_constant = (
        window_mass_prefactor
        * mass_data["explicit_square_mass_majorant"]
    )
    balanced_scale = mp.sqrt(effective_constant / log_height)
    return {
        "horizontal_margin": horizontal_margin,
        "log_height": log_height,
        "window_mass_prefactor": window_mass_prefactor,
        "coefficient_square_mass_majorant": mass_data[
            "explicit_square_mass_majorant"
        ],
        "effective_window_constant": effective_constant,
        "balanced_complement_tolerance": balanced_scale,
        "relative_shannon_core_bound": balanced_scale,
        "delta_cubed_log_height": horizontal_margin**3 * log_height,
    }


def abel_cauchy_high_tail_bound(
    horizontal_margin: mp.mpf,
    height_start: mp.mpf,
    window_mass_prefactor: mp.mpf = mp.mpf("1"),
) -> dict[str, mp.mpf]:
    """Full two-sided Cauchy-defect bound above a dyadic start height.

    If each positive or negative window ``[T,2T]`` has negative mass at
    most ``A*C_delta*T/log(T)``, then summing the Cauchy-weighted dyadic
    windows on both signs gives

        integral_(|t|>=T) W(t)/(1+t^2) dt
            <= 4*A*C_delta/(T*log(T)).
    """
    horizontal_margin = mp.mpf(horizontal_margin)
    height_start = mp.mpf(height_start)
    window_mass_prefactor = mp.mpf(window_mass_prefactor)
    if height_start <= 1:
        raise ValueError("height_start must exceed one")
    if window_mass_prefactor <= 0:
        raise ValueError("window_mass_prefactor must be positive")
    mass_data = abel_coefficient_square_mass_majorant(horizontal_margin)
    effective_constant = (
        window_mass_prefactor
        * mass_data["explicit_square_mass_majorant"]
    )
    tail_bound = 4 * effective_constant / (
        height_start * mp.log(height_start)
    )
    return {
        "horizontal_margin": horizontal_margin,
        "height_start": height_start,
        "window_mass_prefactor": window_mass_prefactor,
        "coefficient_square_mass_majorant": mass_data[
            "explicit_square_mass_majorant"
        ],
        "effective_window_constant": effective_constant,
        "two_sided_cauchy_high_tail_bound": tail_bound,
    }


def abel_square_root_core_schedule(
    scale: mp.mpf,
    logarithmic_margin_exponent: mp.mpf,
    cutoff_multiplier: mp.mpf = mp.mpf("3"),
    high_tail_log_power: mp.mpf = mp.mpf("6"),
) -> dict[str, mp.mpf | int]:
    """Ledger for the square-root Abel Cauchy-core localization.

    With ``delta=(log Y)^(-alpha)`` the Montgomery--Vaughan mean-value
    bound localizes the unresolved trace to

        T0=sqrt(Y)*delta^(-3/2)*log(Y).

    ``N=A*Y*log(Y)`` gives a power-small exponential Abel truncation tail,
    while ``T1=Y*log(Y)^6`` enters the established dyadic high-tail regime.
    Returned proxy terms suppress analytic constants and are diagnostics,
    not interval enclosures.
    """
    scale = mp.mpf(scale)
    logarithmic_margin_exponent = mp.mpf(
        logarithmic_margin_exponent
    )
    cutoff_multiplier = mp.mpf(cutoff_multiplier)
    high_tail_log_power = mp.mpf(high_tail_log_power)
    if scale <= mp.e:
        raise ValueError("scale must exceed e")
    if not 0 < logarithmic_margin_exponent < mp.mpf("1") / 3:
        raise ValueError("margin exponent must lie strictly between 0 and 1/3")
    if cutoff_multiplier <= 2:
        raise ValueError("cutoff multiplier must exceed two")
    if high_tail_log_power <= 3:
        raise ValueError("high-tail log power must exceed three")
    log_scale = mp.log(scale)
    horizontal_margin = mp.power(
        log_scale, -logarithmic_margin_exponent
    )
    core_height = (
        mp.sqrt(scale)
        * mp.power(horizontal_margin, -mp.mpf("1.5"))
        * log_scale
    )
    high_tail_start = scale * mp.power(
        log_scale, high_tail_log_power
    )
    prime_cutoff = int(mp.ceil(cutoff_multiplier * scale * log_scale))
    square_mass_data = abel_coefficient_square_mass_majorant(
        horizontal_margin
    )
    square_mass_bound = square_mass_data["explicit_square_mass_majorant"]
    core_log = mp.log(core_height)
    diagonal_shell_proxy = square_mass_bound / (
        core_height * core_log
    )
    off_diagonal_shell_proxy = (
        square_mass_bound
        * prime_cutoff
        / (core_height**2 * core_log)
    )
    continuum_barrier_ratio = (
        1 + mp.power(scale, mp.mpf("0.5") - horizontal_margin)
    ) / (core_height * core_log)
    high_tail_proxy = 4 * square_mass_bound / (
        high_tail_start * mp.log(high_tail_start)
    )
    return {
        "scale": scale,
        "log_scale": log_scale,
        "logarithmic_margin_exponent": logarithmic_margin_exponent,
        "horizontal_margin": horizontal_margin,
        "core_height": core_height,
        "high_tail_start": high_tail_start,
        "cutoff_multiplier": cutoff_multiplier,
        "prime_cutoff": prime_cutoff,
        "high_tail_log_power": high_tail_log_power,
        "coefficient_square_mass_bound": square_mass_bound,
        "abel_cutoff_exponential_factor": mp.exp(-prime_cutoff / scale),
        "intermediate_diagonal_trace_proxy": diagonal_shell_proxy,
        "intermediate_off_diagonal_trace_proxy": off_diagonal_shell_proxy,
        "continuum_barrier_ratio_proxy": continuum_barrier_ratio,
        "dyadic_high_tail_trace_proxy": high_tail_proxy,
        "unresolved_core_to_scale_ratio": core_height / scale,
    }


def weighted_hodge_inertia_density_bound(
    bandwidth: mp.mpf,
    frequency_window_length: mp.mpf,
    negative_mass_bound: mp.mpf,
    spectral_threshold: mp.mpf,
) -> dict[str, object]:
    """Negative-index and relative-Shannon bound for A-C_W, A>=0.

    Min--max gives N_{(-infinity,-epsilon)}(A-C_W) no larger than the
    number of eigenvalues of C_W above epsilon.  The latter is controlled by
    the weighted concentration trace.  The Shannon dimension used for the
    relative bound is B*L/pi.
    """
    bandwidth = mp.mpf(bandwidth)
    frequency_window_length = mp.mpf(frequency_window_length)
    negative_mass_bound = mp.mpf(negative_mass_bound)
    spectral_threshold = mp.mpf(spectral_threshold)
    if frequency_window_length <= 0:
        raise ValueError("frequency_window_length must be positive")
    rank_data = weighted_prolate_core_rank_bound(
        bandwidth, negative_mass_bound, spectral_threshold
    )
    shannon_dimension = (
        bandwidth * frequency_window_length / mp.pi
    )
    relative_bound = (
        rank_data["core_rank_bound_real"] / shannon_dimension
    )
    return {
        **rank_data,
        "frequency_window_length": frequency_window_length,
        "shannon_dimension": shannon_dimension,
        "negative_inertia_bound": rank_data[
            "negative_inertia_above_tolerance_bound"
        ],
        "negative_inertia_relative_shannon_bound": relative_bound,
    }


def abel_cyclic_core_leakage_bound(
    horizontal_margin: mp.mpf,
    height_start: mp.mpf,
    decay_exponent: mp.mpf,
    profile_constant: mp.mpf = mp.mpf("1"),
    window_mass_prefactor: mp.mpf = mp.mpf("1"),
    include_dyadic_tail: bool = True,
) -> dict[str, mp.mpf]:
    """Absolute leakage of a decaying cyclic vector into Abel negative cores.

    Assume |fhat(t)| <= C t^{-r}, r>1/2, and the negative-mass estimate
    integral_[T,2T] W <= A C_delta T/log(T).  At the balanced spectral
    threshold sqrt(A C_delta/log(T)), the core-projection norm squared is
    bounded by the weighted energy divided by that threshold.  When requested,
    all dyadic windows above T are summed by a geometric series.
    """
    horizontal_margin = mp.mpf(horizontal_margin)
    height_start = mp.mpf(height_start)
    decay_exponent = mp.mpf(decay_exponent)
    profile_constant = mp.mpf(profile_constant)
    window_mass_prefactor = mp.mpf(window_mass_prefactor)
    if height_start <= 1:
        raise ValueError("height_start must exceed one")
    if decay_exponent <= mp.mpf("0.5"):
        raise ValueError("decay_exponent must exceed one half")
    if profile_constant < 0 or window_mass_prefactor <= 0:
        raise ValueError("profile and mass constants must be nonnegative")
    mass_data = abel_coefficient_square_mass_majorant(horizontal_margin)
    effective_constant = (
        window_mass_prefactor
        * mass_data["explicit_square_mass_majorant"]
    )
    logarithm = mp.log(height_start)
    balanced_threshold = mp.sqrt(effective_constant / logarithm)
    geometric_factor = mp.mpf("1")
    if include_dyadic_tail:
        geometric_factor = 1 / (
            1 - mp.power(2, 1 - 2 * decay_exponent)
        )
    weighted_energy_bound = (
        effective_constant
        * profile_constant**2
        * mp.power(height_start, 1 - 2 * decay_exponent)
        * geometric_factor
        / (2 * mp.pi * logarithm)
    )
    core_projection_norm_squared_bound = (
        weighted_energy_bound / balanced_threshold
    )
    return {
        "horizontal_margin": horizontal_margin,
        "height_start": height_start,
        "decay_exponent": decay_exponent,
        "profile_constant": profile_constant,
        "window_mass_prefactor": window_mass_prefactor,
        "coefficient_square_mass_majorant": mass_data[
            "explicit_square_mass_majorant"
        ],
        "effective_window_constant": effective_constant,
        "balanced_spectral_threshold": balanced_threshold,
        "dyadic_geometric_factor": geometric_factor,
        "weighted_cyclic_energy_bound": weighted_energy_bound,
        "core_projection_norm_squared_bound": (
            core_projection_norm_squared_bound
        ),
        "core_projection_norm_bound": mp.sqrt(
            core_projection_norm_squared_bound
        ),
    }


def abel_resolvent_core_leakage_bound(
    horizontal_margin: mp.mpf,
    height_start: mp.mpf,
    resolvent_point: mp.mpc,
    window_mass_prefactor: mp.mpf = mp.mpf("1"),
    truncation_length: mp.mpf | None = None,
) -> dict[str, object]:
    """Specialize cyclic leakage to a finite-filter resolvent vector.

    On ``L2([-B,0])`` the correct vector is ``f_z(y)=exp(zy)`` and its
    Fourier profile is

        q_(z,B)(t) = (1-exp(-(z-it)B))/(z-it).

    Thus, for T>=2|z|, its profile is at most
    ``2*(1+exp(-Re(z)B))/t``.  The untruncated Hardy profile ``1/(z-it)``
    is not itself the Fourier transform of a vector in a finite interval,
    so ``truncation_length`` is required here.
    """
    resolvent_point = mp.mpc(resolvent_point)
    height_start = mp.mpf(height_start)
    if truncation_length is None:
        raise ValueError("truncation_length is required for a finite core")
    truncation_length = mp.mpf(truncation_length)
    if mp.re(resolvent_point) <= 0:
        raise ValueError("resolvent_point must lie in the right half-plane")
    if truncation_length <= 0:
        raise ValueError("truncation_length must be positive")
    if height_start < 2 * abs(resolvent_point):
        raise ValueError("height_start must be at least twice |resolvent_point|")
    profile_constant = 2 * (
        1 + mp.exp(-mp.re(resolvent_point) * truncation_length)
    )
    leakage = abel_cyclic_core_leakage_bound(
        horizontal_margin=horizontal_margin,
        height_start=height_start,
        decay_exponent=mp.mpf("1"),
        profile_constant=profile_constant,
        window_mass_prefactor=window_mass_prefactor,
        include_dyadic_tail=True,
    )
    return {
        **leakage,
        "resolvent_point": resolvent_point,
        "truncation_length": truncation_length,
    }


def cauchy_resolvent_weight_constant(
    resolvent_point: mp.mpc,
    truncation_length: mp.mpf | None = None,
) -> dict[str, object]:
    """Sharp Cauchy-weight constant for a (possibly truncated) resolvent.

    If z=x+iy with x>0, generalized eigenvalues give the exact identity

        sup_t (1+t^2)/|z-it|^2
          = (tau+sqrt(tau^2-4x^2))/(2x^2),
        tau=1+|z|^2.

    A finite-interval profile gains the rigorous numerator factor
    ``(1+exp(-xB))^2``.
    """
    resolvent_point = mp.mpc(resolvent_point)
    horizontal_part = mp.re(resolvent_point)
    if horizontal_part <= 0:
        raise ValueError("resolvent_point must lie in the right half-plane")
    trace = 1 + abs(resolvent_point) ** 2
    hardy_constant = (
        trace + mp.sqrt(trace**2 - 4 * horizontal_part**2)
    ) / (2 * horizontal_part**2)
    truncation_factor = mp.mpf("1")
    normalized_length = None
    if truncation_length is not None:
        normalized_length = mp.mpf(truncation_length)
        if normalized_length <= 0:
            raise ValueError("truncation_length must be positive")
        truncation_factor = (
            1 + mp.exp(-horizontal_part * normalized_length)
        ) ** 2
    return {
        "resolvent_point": resolvent_point,
        "truncation_length": normalized_length,
        "hardy_weight_constant": hardy_constant,
        "truncation_factor": truncation_factor,
        "cauchy_weight_constant": hardy_constant * truncation_factor,
    }


def cauchy_weighted_core_gram_bound(
    cauchy_negative_mass: mp.mpf,
    spectral_threshold: mp.mpf,
    resolvent_points: list[mp.mpc],
    truncation_length: mp.mpf | None = None,
) -> dict[str, object]:
    """Dominate a negative-core resolvent Gram by one scalar defect.

    For ``C_W>=0`` and ``Q=1_(epsilon,infinity)(C_W)``, spectral calculus
    gives ``Q<=C_W/epsilon``.  Hence

        |<Q f_z,Q f_w>|
          <= J sqrt(C_z C_w)/(2*pi*epsilon),

    where ``J=integral W(t)/(1+t^2)dt`` and ``C_z`` is returned by
    :func:`cauchy_resolvent_weight_constant`.  Taking
    ``epsilon=sqrt(J)`` makes both the complement defect and every fixed
    Gram entry tend to zero whenever ``J`` does.
    """
    cauchy_negative_mass = mp.mpf(cauchy_negative_mass)
    spectral_threshold = mp.mpf(spectral_threshold)
    if cauchy_negative_mass < 0:
        raise ValueError("cauchy_negative_mass must be nonnegative")
    if spectral_threshold <= 0:
        raise ValueError("spectral_threshold must be positive")
    if not resolvent_points:
        raise ValueError("resolvent_points must be nonempty")
    weight_data = [
        cauchy_resolvent_weight_constant(point, truncation_length)
        for point in resolvent_points
    ]
    constants = [item["cauchy_weight_constant"] for item in weight_data]
    size = len(constants)
    entry_bounds = mp.zeros(size, size)
    prefactor = cauchy_negative_mass / (
        2 * mp.pi * spectral_threshold
    )
    for row in range(size):
        for column in range(size):
            entry_bounds[row, column] = prefactor * mp.sqrt(
                constants[row] * constants[column]
            )
    return {
        "cauchy_negative_mass": cauchy_negative_mass,
        "spectral_threshold": spectral_threshold,
        "complement_negative_error_bound": spectral_threshold,
        "resolvent_weight_data": weight_data,
        "gram_entry_bounds": entry_bounds,
        "maximum_gram_entry_bound": max(
            entry_bounds[row, column]
            for row in range(size)
            for column in range(size)
        ),
        "balanced_spectral_threshold": (
            mp.sqrt(cauchy_negative_mass)
            if cauchy_negative_mass > 0
            else mp.mpf("0")
        ),
    }


def dirichlet_convolution_matrix(
    coefficients: list[mp.mpc],
) -> mp.matrix:
    """Finite divisibility-incidence matrix for Dirichlet convolution.

    ``coefficients[n]`` is a(n); index zero is ignored.  Rows and columns
    correspond to 1,...,N, and the (n,d) entry is a(n/d) when d divides n.
    """
    if len(coefficients) < 2:
        raise ValueError("coefficients must contain indices zero and one")
    if abs(coefficients[1]) == 0:
        raise ValueError("the coefficient at one must be nonzero")
    size = len(coefficients) - 1
    matrix = mp.zeros(size, size)
    for integer in range(1, size + 1):
        for divisor in range(1, integer + 1):
            if integer % divisor == 0:
                matrix[integer - 1, divisor - 1] = coefficients[
                    integer // divisor
                ]
    return matrix


def dirichlet_inverse_coefficients(
    coefficients: list[mp.mpc],
) -> list[mp.mpc]:
    """Finite coefficients of the Dirichlet-convolution inverse."""
    if len(coefficients) < 2:
        raise ValueError("coefficients must contain indices zero and one")
    leading = mp.mpc(coefficients[1])
    if abs(leading) == 0:
        raise ValueError("the coefficient at one must be nonzero")
    size = len(coefficients) - 1
    inverse = [mp.mpc(0) for _ in range(size + 1)]
    inverse[1] = 1 / leading
    for integer in range(2, size + 1):
        subtotal = mp.fsum(
            mp.mpc(coefficients[integer // divisor]) * inverse[divisor]
            for divisor in range(1, integer)
            if integer % divisor == 0
        )
        inverse[integer] = -subtotal / leading
    return inverse


def dirichlet_incidence_hodge_kernel(
    coefficients: list[mp.mpc],
    center_parameter: mp.mpf = mp.mpf("1"),
) -> mp.matrix:
    """Rank-one positive Green--Hodge kernel C^{-*} vv^* C^{-1}."""
    center_parameter = mp.mpf(center_parameter)
    if center_parameter <= 0:
        raise ValueError("center_parameter must be positive")
    incidence = dirichlet_convolution_matrix(coefficients)
    size = incidence.rows
    constant_mode = mp.ones(size, 1) / mp.power(size, center_parameter / 2)
    inverse = incidence**-1
    propagated = inverse.transpose_conj() * constant_mode
    return propagated * propagated.transpose_conj()


def dirichlet_incidence_hodge_energy(
    coefficients: list[mp.mpc],
    center_parameter: mp.mpf = mp.mpf("1"),
) -> mp.mpf:
    """N^{-c}|sum_{n<=N} b(n)|^2 for the Dirichlet inverse b."""
    center_parameter = mp.mpf(center_parameter)
    if center_parameter <= 0:
        raise ValueError("center_parameter must be positive")
    inverse = dirichlet_inverse_coefficients(coefficients)
    size = len(coefficients) - 1
    summatory = mp.fsum(inverse[1:])
    return abs(summatory) ** 2 / mp.power(size, center_parameter)


def beurling_fractional_feature(index: int, value: mp.mpf) -> mp.mpf:
    """Báez--Duarte feature rho_index(x)={1/(index*x)} on (0,infinity)."""
    if index < 1:
        raise ValueError("index must be positive")
    value = mp.mpf(value)
    if value <= 0:
        raise ValueError("value must be positive")
    argument = 1 / (index * value)
    return argument - mp.floor(argument)


def positive_gram_schur_distance(
    gram: mp.matrix,
    coupling: mp.matrix,
    target_norm_squared: mp.mpf,
) -> mp.mpf:
    """Squared distance to a finite feature span from its Gram data."""
    if gram.rows != gram.cols or gram.rows < 1:
        raise ValueError("gram must be a nonempty square matrix")
    if coupling.rows != gram.rows or coupling.cols != 1:
        raise ValueError("coupling must be a compatible column vector")
    target_norm_squared = mp.mpf(target_norm_squared)
    if target_norm_squared < 0:
        raise ValueError("target norm must be nonnegative")
    projection_squared = (
        coupling.transpose_conj() * (gram**-1) * coupling
    )[0, 0]
    distance = mp.re(target_norm_squared - projection_squared)
    tolerance = mp.mpf("1e-40") * max(1, abs(target_norm_squared))
    if distance < -tolerance:
        raise ValueError("Gram data give a negative Schur complement")
    return max(distance, mp.mpf(0))


def sampled_beurling_hodge_data(
    indices: list[int],
    sample_points: list[mp.mpf],
    sample_weights: list[mp.mpf],
) -> dict[str, mp.matrix | mp.mpf]:
    """Positive quadrature Gram/Schur data for finite Beurling features."""
    if not indices or any(index < 1 for index in indices):
        raise ValueError("indices must be a nonempty list of positive integers")
    if len(sample_points) != len(sample_weights) or not sample_points:
        raise ValueError("sample points and weights must have equal positive length")
    points = [mp.mpf(point) for point in sample_points]
    weights = [mp.mpf(weight) for weight in sample_weights]
    if any(point <= 0 for point in points):
        raise ValueError("sample points must be positive")
    if any(weight <= 0 for weight in weights):
        raise ValueError("sample weights must be positive")
    features = mp.matrix(
        [
            [beurling_fractional_feature(index, point) for index in indices]
            for point in points
        ]
    )
    target = mp.matrix([1 if point <= 1 else 0 for point in points])
    weight_matrix = mp.diag(weights)
    gram = features.transpose_conj() * weight_matrix * features
    coupling = features.transpose_conj() * weight_matrix * target
    target_norm_squared = mp.re(
        (target.transpose_conj() * weight_matrix * target)[0, 0]
    )
    distance_squared = positive_gram_schur_distance(
        gram, coupling, target_norm_squared
    )
    return {
        "features": features,
        "target": target,
        "weights": weight_matrix,
        "gram": gram,
        "coupling": coupling,
        "target_norm_squared": target_norm_squared,
        "distance_squared": distance_squared,
    }


def beurling_target_coupling(index: int) -> mp.mpf:
    """Exact <rho_index, 1_(0,1)> = (log(index)+1-gamma)/index."""
    if index < 1:
        raise ValueError("index must be positive")
    return (mp.log(index) + 1 - mp.euler) / index


def beurling_feature_norm_squared(index: int) -> mp.mpf:
    """Exact ||rho_index||_2^2 = (log(2*pi)-gamma)/index."""
    if index < 1:
        raise ValueError("index must be positive")
    return (mp.log(2 * mp.pi) - mp.euler) / index


def normalize_beurling_gram_data(
    gram: mp.matrix,
    coupling: mp.matrix,
    indices: list[int],
) -> tuple[mp.matrix, mp.matrix]:
    """Pass from rho_n to equal-norm phi_n=sqrt(n) rho_n."""
    if gram.rows != gram.cols or gram.rows != len(indices):
        raise ValueError("gram dimension and indices must agree")
    if coupling.rows != gram.rows or coupling.cols != 1:
        raise ValueError("coupling must be a compatible column vector")
    if any(index < 1 for index in indices):
        raise ValueError("indices must be positive")
    scaling = mp.diag([mp.sqrt(index) for index in indices])
    return scaling * gram * scaling, scaling * coupling


def positive_gram_feshbach_distance(
    gram: mp.matrix,
    coupling: mp.matrix,
    target_norm_squared: mp.mpf,
    core_size: int,
) -> dict[str, mp.matrix | mp.mpf]:
    """Exact Schur/Feshbach elimination of a Gram complement block."""
    if gram.rows != gram.cols or gram.rows < 2:
        raise ValueError("gram must be a square matrix of size at least two")
    if coupling.rows != gram.rows or coupling.cols != 1:
        raise ValueError("coupling must be a compatible column vector")
    if core_size < 1 or core_size >= gram.rows:
        raise ValueError("core_size must lie strictly between zero and the size")
    target_norm_squared = mp.mpf(target_norm_squared)
    core = list(range(core_size))
    complement = list(range(core_size, gram.rows))

    def submatrix(rows: list[int], columns: list[int]) -> mp.matrix:
        return mp.matrix(
            [[gram[row, column] for column in columns] for row in rows]
        )

    core_gram = submatrix(core, core)
    coupling_block = submatrix(core, complement)
    complement_gram = submatrix(complement, complement)
    core_target = mp.matrix([coupling[row, 0] for row in core])
    complement_target = mp.matrix([coupling[row, 0] for row in complement])
    complement_inverse = complement_gram**-1
    effective_gram = (
        core_gram
        - coupling_block * complement_inverse * coupling_block.transpose_conj()
    )
    effective_target = (
        core_target
        - coupling_block * complement_inverse * complement_target
    )
    effective_norm = mp.re(
        target_norm_squared
        - (
            complement_target.transpose_conj()
            * complement_inverse
            * complement_target
        )[0, 0]
    )
    distance = positive_gram_schur_distance(
        effective_gram, effective_target, effective_norm
    )
    return {
        "effective_gram": effective_gram,
        "effective_target": effective_target,
        "effective_norm_squared": effective_norm,
        "distance_squared": distance,
    }


def mobius(integer: int) -> int:
    """Return the Möbius function mu(integer)."""
    if integer < 1:
        raise ValueError("integer must be positive")
    remaining = integer
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            if remaining % prime == 0:
                return 0
            parity += 1
            while remaining % prime == 0:
                remaining //= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def _finite_dirichlet_convolution(
    left: list[mp.mpc], right: list[mp.mpc]
) -> list[mp.mpc]:
    """Dirichlet convolution through the common finite cutoff."""
    if len(left) != len(right) or len(left) < 2:
        raise ValueError("finite coefficient lists must have equal size")
    cutoff = len(left) - 1
    result = [mp.mpc(0) for _ in range(cutoff + 1)]
    for integer in range(1, cutoff + 1):
        result[integer] = mp.fsum(
            mp.mpc(left[divisor]) * mp.mpc(right[integer // divisor])
            for divisor in range(1, integer + 1)
            if integer % divisor == 0
        )
    return result


def balanced_vaughan_coefficients(
    cutoff: int, mobius_cutoff: int, mangoldt_cutoff: int
) -> dict[str, object]:
    """Exact centered Vaughan decomposition through ``cutoff``.

    With ``mu_1=mu*1_{n<=U}``, ``Lambda_1=Lambda*1_{n<=V}``, the
    four returned components are

        mu_1*log - 1,
        -mu_1*Lambda_1*1,
        mu_2*Lambda_2*1,
        Lambda_1.

    Their sum is exactly ``Lambda-1`` (up to transcendental arithmetic
    roundoff).  This follows from ``log=Lambda*1`` and ``mu*1=epsilon``.
    The coefficient ``-1`` is deliberately kept inside the first Type-I
    component; the remaining counting-measure minus Lebesgue-measure cell
    error must be retained separately when a continuum term is present.
    """
    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    if not 1 <= mobius_cutoff <= cutoff:
        raise ValueError("mobius cutoff must lie between one and cutoff")
    if not 1 <= mangoldt_cutoff <= cutoff:
        raise ValueError("Mangoldt cutoff must lie between one and cutoff")
    zeros = [mp.mpc(0) for _ in range(cutoff + 1)]
    ones = zeros.copy()
    logarithm = zeros.copy()
    mu_low = zeros.copy()
    mu_high = zeros.copy()
    mangoldt_low = zeros.copy()
    mangoldt_high = zeros.copy()
    centered_target = zeros.copy()
    for integer in range(1, cutoff + 1):
        ones[integer] = 1
        logarithm[integer] = mp.log(integer)
        mu_value = mobius(integer)
        if integer <= mobius_cutoff:
            mu_low[integer] = mu_value
        else:
            mu_high[integer] = mu_value
        mangoldt_value = von_mangoldt(integer)
        if integer <= mangoldt_cutoff:
            mangoldt_low[integer] = mangoldt_value
        else:
            mangoldt_high[integer] = mangoldt_value
        centered_target[integer] = mangoldt_value - 1
    type_i_log = _finite_dirichlet_convolution(mu_low, logarithm)
    type_i_balanced = type_i_log.copy()
    for integer in range(1, cutoff + 1):
        type_i_balanced[integer] -= 1
    type_i_correction = _finite_dirichlet_convolution(
        _finite_dirichlet_convolution(mu_low, mangoldt_low), ones
    )
    type_i_correction = [-value for value in type_i_correction]
    type_ii = _finite_dirichlet_convolution(
        _finite_dirichlet_convolution(mu_high, mangoldt_high), ones
    )
    low_prime_power = mangoldt_low
    components = {
        "balanced_type_i_log": type_i_balanced,
        "type_i_correction": type_i_correction,
        "type_ii": type_ii,
        "low_prime_power": low_prime_power,
    }
    uncentered_components = {
        "type_i_log": type_i_log,
        "type_i_correction": type_i_correction,
        "type_ii": type_ii,
        "low_prime_power": low_prime_power,
    }
    reconstruction = [mp.mpc(0) for _ in range(cutoff + 1)]
    for integer in range(1, cutoff + 1):
        reconstruction[integer] = mp.fsum(
            component[integer] for component in components.values()
        )
    residuals = [
        reconstruction[integer] - centered_target[integer]
        for integer in range(cutoff + 1)
    ]
    return {
        "cutoff": cutoff,
        "mobius_cutoff": mobius_cutoff,
        "mangoldt_cutoff": mangoldt_cutoff,
        "components": components,
        "uncentered_components": uncentered_components,
        "centered_target": centered_target,
        "reconstruction": reconstruction,
        "reconstruction_residuals": residuals,
        "maximum_reconstruction_residual": max(
            abs(value) for value in residuals
        ),
        "type_ii_support_lower_bound": (
            mobius_cutoff + 1
        ) * (mangoldt_cutoff + 1),
        "identity": (
            "Lambda-1=(mu_<=U*log-1)"
            "-(mu_<=U*Lambda_<=V*1)"
            "+(mu_>U*Lambda_>V*1)+Lambda_<=V"
        ),
    }


def canonical_vaughan_two_channel_coefficients(
    cutoff: int, mobius_cutoff: int, mangoldt_cutoff: int
) -> dict[str, object]:
    """Collapse the four uncentered Vaughan terms to physical Type I/II.

    If ``P_1,...,P_4`` are the uncentered components returned by
    :func:`balanced_vaughan_coefficients`, the physical quotient is

        I  = P_1 + P_2 + P_4,
        II = P_3.

    Thus ``Lambda=I+II`` exactly.  Moreover ``II`` is supported on
    ``n >= (U+1)(V+1)``, so ``I(n)=Lambda(n)`` below that threshold.
    """
    decomposition = balanced_vaughan_coefficients(
        cutoff, mobius_cutoff, mangoldt_cutoff
    )
    four = decomposition["uncentered_components"]
    first = four["type_i_log"]
    correction = four["type_i_correction"]
    type_ii = four["type_ii"]
    low = four["low_prime_power"]
    type_i = [mp.mpc(0) for _ in range(cutoff + 1)]
    target = [mp.mpc(0) for _ in range(cutoff + 1)]
    reconstruction = [mp.mpc(0) for _ in range(cutoff + 1)]
    for integer in range(1, cutoff + 1):
        type_i[integer] = first[integer] + correction[integer] + low[integer]
        target[integer] = von_mangoldt(integer)
        reconstruction[integer] = type_i[integer] + type_ii[integer]
    residuals = [
        reconstruction[integer] - target[integer]
        for integer in range(cutoff + 1)
    ]
    support_lower_bound = decomposition["type_ii_support_lower_bound"]
    agreement_residuals = [
        type_i[integer] - target[integer]
        for integer in range(1, min(cutoff + 1, support_lower_bound))
    ]
    return {
        "cutoff": cutoff,
        "mobius_cutoff": mobius_cutoff,
        "mangoldt_cutoff": mangoldt_cutoff,
        "components": {"type_i": type_i, "type_ii": type_ii},
        "target": target,
        "reconstruction": reconstruction,
        "reconstruction_residuals": residuals,
        "maximum_reconstruction_residual": max(
            abs(value) for value in residuals
        ),
        "type_ii_support_lower_bound": support_lower_bound,
        "type_i_target_agreement_residual": max(
            [abs(value) for value in agreement_residuals] + [mp.mpf(0)]
        ),
        "physical_quotient_matrix": mp.matrix([
            [1, 1, 0, 1],
            [0, 0, 1, 0],
        ]),
        "identity": (
            "Lambda=[(mu_<=U*1)*Lambda_>V+Lambda_<=V]"
            "+[mu_>U*Lambda_>V*1]"
        ),
    }


def canonical_vaughan_two_channel_gram(
    four_component_gram: mp.matrix,
) -> dict[str, object]:
    """Push a four-component Vaughan Gram to its physical two-channel quotient."""
    if four_component_gram.rows != 4 or four_component_gram.cols != 4:
        raise ValueError("Vaughan component Gram must be four by four")
    hermitian = (
        four_component_gram + four_component_gram.transpose_conj()
    ) / 2
    quotient = mp.matrix([
        [1, 1, 0, 1],
        [0, 0, 1, 0],
    ])
    two_channel = quotient * hermitian * quotient.transpose_conj()
    physical_four = mp.matrix([1, 1, 1, 1])
    physical_two = mp.matrix([1, 1])
    energy_four = mp.re(
        (physical_four.transpose_conj() * hermitian * physical_four)[0, 0]
    )
    energy_two = mp.re(
        (physical_two.transpose_conj() * two_channel * physical_two)[0, 0]
    )
    return {
        "quotient_matrix": quotient,
        "two_channel_gram": two_channel,
        "four_channel_physical_energy": energy_four,
        "two_channel_physical_energy": energy_two,
        "physical_energy_residual": energy_two - energy_four,
        "physical_pullback_residual": mp.norm(
            quotient.transpose_conj() * physical_two - physical_four
        ),
        "hermitian_residual": mp.norm(
            two_channel - two_channel.transpose_conj()
        ),
    }


def vaughan_laurent_channel_data(
    cutoff_pairs: list[tuple[int, int]],
    scale_weights: list[mp.mpf],
    continuum_weights: list[mp.mpf],
) -> dict[str, object]:
    """Laurent principal-part channels of mixed Vaughan decompositions.

    Put ``z=s-1`` and write

        M_U(s)=sum_{d<=U} mu(d)d^{-s}=m0+m1*z+O(z^2),
        L_V(s)=sum_{m<=V} Lambda(m)m^{-s}=l0+O(z).

    For the four *uncentered* components in the order

        M_U(-zeta'), -M_U L_V zeta,
        (1-M_U zeta)(-zeta'/zeta-L_V), L_V,

    their double- and simple-pole coefficient vectors are respectively

        m0*(1,0,-1,0),
        (m1,-m0*l0,1+m0*l0-m1,0).

    The first vector has coordinate sum zero and the second sum one.  Mixing
    cutoffs with real weights of sum one preserves these identities.  After
    distributing the continuum residue by real shares ``alpha`` of sum one,
    the balanced simple-pole vector is ``simple-alpha`` and also lies in the
    coefficient-sum-zero hyperplane.

    Besides the singular span (rank at most two), return two canonical
    physical rank-at-most-two candidates obtained by adjoining the all-ones
    vector to the double or balanced-simple channel.  Degenerate seeds are
    removed rather than promoted to an artificial extra channel.
    """
    if not cutoff_pairs:
        raise ValueError("at least one Vaughan cutoff pair is required")
    if len(set(cutoff_pairs)) != len(cutoff_pairs):
        raise ValueError("Vaughan cutoff pairs must be distinct")
    if len(scale_weights) != len(cutoff_pairs):
        raise ValueError("scale weights have incompatible length")
    if len(continuum_weights) != 4:
        raise ValueError("exactly four continuum weights are required")
    if any(first < 1 or second < 1 for first, second in cutoff_pairs):
        raise ValueError("Vaughan cutoffs must be positive")

    def real_scalar(value: mp.mpf, name: str) -> mp.mpf:
        candidate = mp.mpc(value)
        if mp.im(candidate) != 0:
            raise ValueError(f"{name} must be real")
        return mp.re(candidate)

    local_scale_weights = [
        real_scalar(weight, "scale weights") for weight in scale_weights
    ]
    local_continuum_weights = [
        real_scalar(weight, "continuum weights")
        for weight in continuum_weights
    ]
    tolerance = 1000 * mp.eps * max(
        mp.mpf(1),
        mp.fsum(abs(weight) for weight in local_scale_weights),
        mp.fsum(abs(weight) for weight in local_continuum_weights),
    )
    scale_sum_residual = mp.fsum(local_scale_weights) - 1
    continuum_sum_residual = mp.fsum(local_continuum_weights) - 1
    if abs(scale_sum_residual) > tolerance:
        raise ValueError("scale weights must sum to one")
    if abs(continuum_sum_residual) > tolerance:
        raise ValueError("continuum weights must sum to one")

    cutoff_records = []
    euler_gamma = mp.euler
    first_stieltjes_constant = mp.stieltjes(1)
    for mobius_cutoff, mangoldt_cutoff in cutoff_pairs:
        mobius_value = mp.fsum(
            mp.mpf(mobius(integer)) / integer
            for integer in range(1, mobius_cutoff + 1)
        )
        mobius_derivative = -mp.fsum(
            mp.mpf(mobius(integer)) * mp.log(integer) / integer
            for integer in range(1, mobius_cutoff + 1)
        )
        mobius_second_coefficient = mp.fsum(
            mp.mpf(mobius(integer)) * mp.log(integer) ** 2 / (2 * integer)
            for integer in range(1, mobius_cutoff + 1)
        )
        mangoldt_value = mp.fsum(
            von_mangoldt(integer) / integer
            for integer in range(1, mangoldt_cutoff + 1)
        )
        mangoldt_derivative = -mp.fsum(
            von_mangoldt(integer) * mp.log(integer) / integer
            for integer in range(1, mangoldt_cutoff + 1)
        )
        double_pole = [
            mobius_value,
            mp.mpf(0),
            -mobius_value,
            mp.mpf(0),
        ]
        simple_pole = [
            mobius_derivative,
            -mobius_value * mangoldt_value,
            1 + mobius_value * mangoldt_value - mobius_derivative,
            mp.mpf(0),
        ]
        regular_constant = [
            mobius_second_coefficient
            + mobius_value * first_stieltjes_constant,
            -(
                mobius_value * mangoldt_value * euler_gamma
                + mobius_derivative * mangoldt_value
                + mobius_value * mangoldt_derivative
            ),
            (
                -euler_gamma
                - mangoldt_value
                - mobius_value * first_stieltjes_constant
                + mobius_value * mangoldt_derivative
                + mobius_value * euler_gamma * mangoldt_value
                + mobius_derivative * mangoldt_value
                - mobius_second_coefficient
            ),
            mangoldt_value,
        ]
        cutoff_records.append({
            "cutoff_pair": (mobius_cutoff, mangoldt_cutoff),
            "mobius_value_at_one": mobius_value,
            "mobius_derivative_at_one": mobius_derivative,
            "mobius_second_laurent_coefficient": (
                mobius_second_coefficient
            ),
            "truncated_mangoldt_value_at_one": mangoldt_value,
            "truncated_mangoldt_derivative_at_one": mangoldt_derivative,
            "double_pole_vector": double_pole,
            "simple_pole_vector": simple_pole,
            "regular_constant_vector": regular_constant,
            "double_sum_residual": mp.fsum(double_pole),
            "simple_sum_residual": mp.fsum(simple_pole) - 1,
            "regular_sum_residual": (
                mp.fsum(regular_constant) + euler_gamma
            ),
        })

    mixed_double = [
        mp.fsum(
            local_scale_weights[index]
            * cutoff_records[index]["double_pole_vector"][component]
            for index in range(len(cutoff_pairs))
        )
        for component in range(4)
    ]
    mixed_simple = [
        mp.fsum(
            local_scale_weights[index]
            * cutoff_records[index]["simple_pole_vector"][component]
            for index in range(len(cutoff_pairs))
        )
        for component in range(4)
    ]
    balanced_simple = [
        mixed_simple[index] - local_continuum_weights[index]
        for index in range(4)
    ]
    mixed_regular = [
        mp.fsum(
            local_scale_weights[index]
            * cutoff_records[index]["regular_constant_vector"][component]
            for index in range(len(cutoff_pairs))
        )
        for component in range(4)
    ]
    regular_transverse = [
        mixed_regular[index] + euler_gamma / 4 for index in range(4)
    ]
    physical = [mp.mpf(1)] * 4

    def spanning_basis(seeds: list[list[mp.mpf]]) -> dict[str, object]:
        independent: list[list[mp.mpf]] = []
        orthonormal: list[mp.matrix] = []
        seed_scale = max(
            mp.mpf(1),
            *(mp.norm(mp.matrix(seed)) for seed in seeds),
        )
        dependence_tolerance = 1000 * mp.eps * seed_scale
        residual_norms = []
        for seed in seeds:
            residual = mp.matrix([mp.mpc(value) for value in seed])
            for vector in orthonormal:
                residual -= vector * (
                    vector.transpose_conj() * residual
                )[0, 0]
            residual_norm = mp.norm(residual)
            residual_norms.append(residual_norm)
            if residual_norm > dependence_tolerance:
                independent.append(seed)
                orthonormal.append(residual / residual_norm)
        if independent:
            basis = orthonormal_channel_basis_from_seeds(independent, 4)
        else:
            basis = {
                "channel_seeds": [],
                "ambient_size": 4,
                "core_rank": 0,
                "full_channel_basis": mp.eye(4),
                "core_channel_basis": mp.zeros(4, 0),
                "core_projector": mp.zeros(4, 4),
                "unitarity_residual": mp.mpf(0),
            }
        basis["spanning_seeds"] = seeds
        basis["seed_residual_norms"] = residual_norms
        return basis

    singular_basis = spanning_basis([mixed_double, balanced_simple])
    physical_double_basis = spanning_basis([physical, mixed_double])
    physical_simple_basis = spanning_basis([physical, balanced_simple])
    physical_regular_basis = spanning_basis([physical, regular_transverse])

    singular_rank = singular_basis["core_rank"]
    singular_full_basis = singular_basis["full_channel_basis"]
    annihilator_order = list(range(singular_rank, 4)) + list(
        range(singular_rank)
    )
    annihilator_full_basis = mp.matrix([
        [singular_full_basis[row, column] for column in annihilator_order]
        for row in range(4)
    ])
    annihilator_rank = 4 - singular_rank
    annihilator_core_basis = mp.matrix([
        [annihilator_full_basis[row, column] for column in range(annihilator_rank)]
        for row in range(4)
    ])
    singular_annihilator_basis = {
        "ambient_size": 4,
        "core_rank": annihilator_rank,
        "full_channel_basis": annihilator_full_basis,
        "core_channel_basis": annihilator_core_basis,
        "core_projector": (
            annihilator_core_basis * annihilator_core_basis.transpose_conj()
        ),
        "unitarity_residual": mp.norm(
            annihilator_full_basis.transpose_conj()
            * annihilator_full_basis
            - mp.eye(4)
        ),
        "annihilated_singular_projector": singular_basis["core_projector"],
    }
    return {
        "component_names": [
            "type_i_log",
            "type_i_correction",
            "type_ii",
            "low_prime_power",
        ],
        "cutoff_pairs": cutoff_pairs,
        "scale_weights": local_scale_weights,
        "continuum_weights": local_continuum_weights,
        "cutoff_records": cutoff_records,
        "mixed_double_pole_vector": mixed_double,
        "mixed_simple_pole_vector": mixed_simple,
        "balanced_simple_pole_vector": balanced_simple,
        "mixed_regular_constant_vector": mixed_regular,
        "regular_transverse_vector": regular_transverse,
        "euler_gamma": euler_gamma,
        "first_stieltjes_constant": first_stieltjes_constant,
        "physical_vector": physical,
        "singular_principal_part_matrix": mp.matrix([
            [mixed_double[row], balanced_simple[row]] for row in range(4)
        ]),
        "singular_basis": singular_basis,
        "singular_annihilator_basis": singular_annihilator_basis,
        "physical_double_basis": physical_double_basis,
        "physical_simple_basis": physical_simple_basis,
        "physical_regular_basis": physical_regular_basis,
        "scale_weight_sum_residual": scale_sum_residual,
        "continuum_weight_sum_residual": continuum_sum_residual,
        "mixed_double_sum_residual": mp.fsum(mixed_double),
        "mixed_simple_sum_residual": mp.fsum(mixed_simple) - 1,
        "balanced_simple_sum_residual": mp.fsum(balanced_simple),
        "mixed_regular_sum_residual": (
            mp.fsum(mixed_regular) + euler_gamma
        ),
        "regular_transverse_sum_residual": mp.fsum(regular_transverse),
        "singular_physical_orthogonality_residuals": [
            mp.fsum(mixed_double), mp.fsum(balanced_simple)
        ],
    }


def balanced_vaughan_modulated_gram_audit(
    cutoff: int,
    mobius_cutoff: int,
    mangoldt_cutoff: int,
    center_height: mp.mpf,
    log_window_width: mp.mpf,
    horizontal_offset: mp.mpf = mp.mpf("0"),
    abel_scale: mp.mpf | None = None,
) -> dict[str, object]:
    """Full component Gram for the centered finite Vaughan vector.

    The optional arithmetic weight is

        n^(-1/2-horizontal_offset) exp(-n/abel_scale).

    If ``abel_scale`` is omitted, only the critical power weight is used.
    The audit is atomic: in a prime-minus-continuum measure its companion
    counting-minus-Lebesgue unit-cell vector remains a separate component.
    """
    center_height = mp.mpf(center_height)
    log_window_width = mp.mpf(log_window_width)
    horizontal_offset = mp.mpf(horizontal_offset)
    if log_window_width <= 0:
        raise ValueError("log window width must be positive")
    if horizontal_offset < 0:
        raise ValueError("horizontal offset must be nonnegative")
    if abel_scale is not None:
        abel_scale = mp.mpf(abel_scale)
        if abel_scale <= 0:
            raise ValueError("Abel scale must be positive")
    decomposition = balanced_vaughan_coefficients(
        cutoff, mobius_cutoff, mangoldt_cutoff
    )
    component_names = list(decomposition["components"])
    nodes = [mp.log(integer) for integer in range(1, cutoff + 1)]
    weights = [
        mp.power(integer, -mp.mpf("0.5") - horizontal_offset)
        * (mp.exp(-mp.mpf(integer) / abel_scale)
           if abel_scale is not None else 1)
        for integer in range(1, cutoff + 1)
    ]
    weighted_components = {
        name: [
            mp.mpc(coefficients[integer]) * weights[integer - 1]
            for integer in range(1, cutoff + 1)
        ]
        for name, coefficients in decomposition["components"].items()
    }
    phased_components = {
        name: [
            coefficient * mp.exp(-1j * center_height * node)
            for node, coefficient in zip(nodes, coefficients)
        ]
        for name, coefficients in weighted_components.items()
    }
    size = len(component_names)
    gram = mp.zeros(size, size)
    for row, row_name in enumerate(component_names):
        for column, column_name in enumerate(component_names):
            gram[row, column] = mp.fsum(
                row_value
                * mp.conj(column_value)
                * max(
                    mp.mpf("0"),
                    log_window_width - abs(row_node - column_node),
                )
                for row_node, row_value in zip(
                    nodes, phased_components[row_name]
                )
                for column_node, column_value in zip(
                    nodes, phased_components[column_name]
                )
            )
    weighted_reconstruction = [
        decomposition["reconstruction"][integer] * weights[integer - 1]
        for integer in range(1, cutoff + 1)
    ]
    full_energy_audit = stationary_modulated_interval_energy(
        nodes,
        weighted_reconstruction,
        center_height,
        log_window_width,
    )
    gram_total = mp.fsum(
        gram[row, column]
        for row in range(size)
        for column in range(size)
    )
    diagonal_total = mp.re(mp.fsum(gram[index, index] for index in range(size)))
    hermitian_residual = max(
        abs(gram[row, column] - mp.conj(gram[column, row]))
        for row in range(size)
        for column in range(size)
    )
    return {
        "decomposition": decomposition,
        "component_names": component_names,
        "lag_nodes": nodes,
        "weights": weights,
        "weighted_components": weighted_components,
        "component_gram": gram,
        "gram_total_energy": mp.re(gram_total),
        "component_diagonal_energy": diagonal_total,
        "component_cross_energy": mp.re(gram_total) - diagonal_total,
        "full_energy_audit": full_energy_audit,
        "energy_reconstruction_residual": (
            mp.re(gram_total)
            - full_energy_audit["modulated_interval_energy"]
        ),
        "hermitian_residual": hermitian_residual,
        "center_height": center_height,
        "log_window_width": log_window_width,
        "horizontal_offset": horizontal_offset,
        "abel_scale": abel_scale,
        "continuum_cell_component_included": False,
    }


def modulated_atomic_component_gram(
    components: dict[
        str, tuple[list[mp.mpf], list[mp.mpc]]
    ],
    center_height: mp.mpf,
    log_window_width: mp.mpf,
) -> dict[str, object]:
    """Hermitian triangular Gram of separately supported atomic vectors."""
    if not components:
        raise ValueError("at least one component is required")
    center_height = mp.mpf(center_height)
    log_window_width = mp.mpf(log_window_width)
    if log_window_width <= 0:
        raise ValueError("log window width must be positive")
    normalized: dict[str, tuple[list[mp.mpf], list[mp.mpc]]] = {}
    for name, (nodes, coefficients) in components.items():
        if not nodes or len(nodes) != len(coefficients):
            raise ValueError("every component must be nonempty and aligned")
        normalized_nodes = [mp.mpf(node) for node in nodes]
        if any(not mp.isfinite(node) for node in normalized_nodes):
            raise ValueError("component lag nodes must be finite")
        normalized[name] = (
            normalized_nodes,
            [
                mp.mpc(coefficient)
                * mp.exp(-1j * center_height * node)
                for node, coefficient in zip(
                    normalized_nodes, coefficients
                )
            ],
        )
    names = list(normalized)
    size = len(names)
    gram = mp.zeros(size, size)
    for row, row_name in enumerate(names):
        row_nodes, row_values = normalized[row_name]
        for column in range(row, size):
            column_nodes, column_values = normalized[names[column]]
            value = mp.fsum(
                row_value
                * mp.conj(column_value)
                * max(
                    mp.mpf("0"),
                    log_window_width - abs(row_node - column_node),
                )
                for row_node, row_value in zip(row_nodes, row_values)
                for column_node, column_value in zip(
                    column_nodes, column_values
                )
            )
            gram[row, column] = value
            gram[column, row] = mp.conj(value)
    return {
        "component_names": names,
        "component_gram": gram,
        "center_height": center_height,
        "log_window_width": log_window_width,
        "hermitian_residual": max(
            abs(gram[row, column] - mp.conj(gram[column, row]))
            for row in range(size)
            for column in range(size)
        ),
    }


def component_gram_channel_spectrum(
    component_gram: mp.matrix,
    physical_vector: list[mp.mpc] | None = None,
) -> dict[str, object]:
    """Spectral channels of a PSD component Gram along one physical mode."""
    if component_gram.rows != component_gram.cols or component_gram.rows < 1:
        raise ValueError("component Gram must be nonempty and square")
    size = component_gram.rows
    if physical_vector is None:
        physical = mp.matrix([mp.mpc(1) for _ in range(size)])
    else:
        if len(physical_vector) != size:
            raise ValueError("physical vector has incompatible length")
        physical = mp.matrix([mp.mpc(value) for value in physical_vector])
    hermitian = (component_gram + component_gram.transpose_conj()) / 2
    eigenvalues, eigenvectors = mp.eighe(hermitian)
    scale = max(
        mp.mpf("1"),
        max(abs(hermitian[row, column]) for row in range(size) for column in range(size)),
    )
    tolerance = 1000 * mp.eps * scale
    minimum_eigenvalue = min(eigenvalues[index] for index in range(size))
    if minimum_eigenvalue < -tolerance:
        raise ValueError("component Gram must be positive semidefinite")
    records = []
    for index in range(size):
        eigenvalue = max(mp.mpf("0"), mp.re(eigenvalues[index]))
        projection = mp.fsum(
            mp.conj(eigenvectors[row, index]) * physical[row]
            for row in range(size)
        )
        contribution = eigenvalue * abs(projection) ** 2
        records.append({
            "eigenvalue": eigenvalue,
            "physical_projection_squared": abs(projection) ** 2,
            "physical_energy_contribution": contribution,
            "eigenvector": mp.matrix([
                eigenvectors[row, index] for row in range(size)
            ]),
        })
    records_by_energy = sorted(
        records,
        key=lambda item: item["physical_energy_contribution"],
        reverse=True,
    )
    physical_energy = mp.re(
        (physical.transpose_conj() * hermitian * physical)[0, 0]
    )
    trace = mp.re(mp.fsum(hermitian[index, index] for index in range(size)))
    frobenius_squared = mp.fsum(
        abs(hermitian[row, column]) ** 2
        for row in range(size)
        for column in range(size)
    )
    contribution_square_sum = mp.fsum(
        record["physical_energy_contribution"] ** 2 for record in records
    )
    cumulative = mp.mpf("0")
    for rank, record in enumerate(records_by_energy, start=1):
        cumulative += record["physical_energy_contribution"]
        record["energy_rank"] = rank
        record["cumulative_physical_energy"] = cumulative
        record["cumulative_physical_fraction"] = (
            cumulative / physical_energy
            if physical_energy > 0 else mp.mpf("0")
        )
    physical_norm_squared = mp.re(
        (physical.transpose_conj() * physical)[0, 0]
    )
    diagonal_majorant = physical_norm_squared * trace
    return {
        "hermitian_component_gram": hermitian,
        "physical_vector": physical,
        "eigenvalues": eigenvalues,
        "eigenvectors": eigenvectors,
        "channel_records": records,
        "channels_by_physical_energy": records_by_energy,
        "physical_energy": physical_energy,
        "trace": trace,
        "frobenius_norm_squared": frobenius_squared,
        "stable_rank": (
            trace**2 / frobenius_squared
            if frobenius_squared > 0 else mp.mpf("0")
        ),
        "physical_participation_ratio": (
            physical_energy**2 / contribution_square_sum
            if contribution_square_sum > 0 else mp.mpf("0")
        ),
        "physical_norm_squared": physical_norm_squared,
        "diagonal_cauchy_majorant": diagonal_majorant,
        "diagonal_majorant_loss_factor": (
            diagonal_majorant / physical_energy
            if physical_energy > 0 else mp.inf
        ),
        "minimum_eigenvalue": minimum_eigenvalue,
        "spectral_reconstruction_residual": abs(
            mp.fsum(
                record["physical_energy_contribution"] for record in records
            ) - physical_energy
        ),
    }


def matrix_bessel_loewner_certificate(
    component_gram: mp.matrix,
    loewner_majorant: mp.matrix,
    physical_vector: list[mp.mpc] | None = None,
) -> dict[str, object]:
    """Certify G<=M and compare matrix versus diagonal physical bounds."""
    if component_gram.rows != component_gram.cols or (
        loewner_majorant.rows != loewner_majorant.cols
    ) or component_gram.rows != loewner_majorant.rows:
        raise ValueError("Gram and majorant must be compatible square matrices")
    size = component_gram.rows
    physical = (
        mp.matrix([mp.mpc(1) for _ in range(size)])
        if physical_vector is None
        else mp.matrix([mp.mpc(value) for value in physical_vector])
    )
    if physical.rows != size:
        raise ValueError("physical vector has incompatible length")
    gram = (component_gram + component_gram.transpose_conj()) / 2
    majorant = (loewner_majorant + loewner_majorant.transpose_conj()) / 2
    difference = majorant - gram
    gram_eigenvalues = mp.eighe(gram, eigvals_only=True)
    difference_eigenvalues = mp.eighe(difference, eigvals_only=True)
    gram_energy = mp.re((physical.transpose_conj() * gram * physical)[0, 0])
    matrix_bound = mp.re(
        (physical.transpose_conj() * majorant * physical)[0, 0]
    )
    physical_norm_squared = mp.re(
        (physical.transpose_conj() * physical)[0, 0]
    )
    diagonal_bound = physical_norm_squared * mp.re(mp.fsum(
        majorant[index, index] for index in range(size)
    ))
    return {
        "component_gram": gram,
        "loewner_majorant": majorant,
        "majorant_difference": difference,
        "gram_eigenvalues": gram_eigenvalues,
        "majorant_difference_eigenvalues": difference_eigenvalues,
        "minimum_gram_eigenvalue": min(
            gram_eigenvalues[index] for index in range(size)
        ),
        "minimum_majorant_difference_eigenvalue": min(
            difference_eigenvalues[index] for index in range(size)
        ),
        "physical_energy": gram_energy,
        "matrix_physical_upper_bound": matrix_bound,
        "diagonal_cauchy_upper_bound": diagonal_bound,
        "matrix_bound_gain_over_diagonal": (
            diagonal_bound / matrix_bound if matrix_bound > 0 else mp.inf
        ),
    }


def component_gram_vector_error_majorant(
    approximate_gram: mp.matrix,
    approximate_component_norms: list[mp.mpf],
    component_error_norms: list[mp.mpf],
) -> dict[str, object]:
    """Loewner-majorize an exact Gram from component-vector norm errors."""
    if approximate_gram.rows != approximate_gram.cols:
        raise ValueError("approximate Gram must be square")
    size = approximate_gram.rows
    if len(approximate_component_norms) != size or (
        len(component_error_norms) != size
    ):
        raise ValueError("component norm lists must match the Gram size")
    norms = [mp.mpf(value) for value in approximate_component_norms]
    errors = [mp.mpf(value) for value in component_error_norms]
    if any(value < 0 for value in norms + errors):
        raise ValueError("component norms and errors must be nonnegative")
    entry_error_bounds = mp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            entry_error_bounds[row, column] = (
                errors[row] * norms[column]
                + errors[column] * norms[row]
                + errors[row] * errors[column]
            )
    loewner_radius = max(
        mp.fsum(entry_error_bounds[row, column] for column in range(size))
        for row in range(size)
    )
    hermitian_approximation = (
        approximate_gram + approximate_gram.transpose_conj()
    ) / 2
    majorant = hermitian_approximation + loewner_radius * mp.eye(size)
    return {
        "approximate_gram": hermitian_approximation,
        "approximate_component_norms": norms,
        "component_error_norms": errors,
        "entry_error_bounds": entry_error_bounds,
        "loewner_radius": loewner_radius,
        "loewner_majorant": majorant,
    }


def common_component_channel_basis(
    component_grams: list[mp.matrix],
    channel_rank: int,
    gram_weights: list[mp.mpf] | None = None,
    trace_normalize: bool = True,
) -> dict[str, object]:
    """PCA basis of several PSD component Grams on one channel space."""
    if not component_grams:
        raise ValueError("at least one component Gram is required")
    size = component_grams[0].rows
    if size < 1 or any(
        gram.rows != size or gram.cols != size for gram in component_grams
    ):
        raise ValueError("component Grams must be compatible square matrices")
    if not 1 <= channel_rank <= size:
        raise ValueError("channel rank must lie between one and Gram size")
    if gram_weights is None:
        weights = [mp.mpf(1) for _ in component_grams]
    else:
        if len(gram_weights) != len(component_grams):
            raise ValueError("Gram weights have incompatible length")
        weights = [mp.mpf(weight) for weight in gram_weights]
        if any(weight <= 0 for weight in weights):
            raise ValueError("Gram weights must be positive")
    normalized_grams = []
    aggregate = mp.zeros(size, size)
    for gram, weight in zip(component_grams, weights):
        hermitian = (gram + gram.transpose_conj()) / 2
        trace = mp.re(mp.fsum(hermitian[index, index] for index in range(size)))
        if trace_normalize:
            if trace <= 0:
                raise ValueError("trace-normalized Grams must have positive trace")
            normalized = hermitian / trace
        else:
            normalized = hermitian
        normalized_grams.append(normalized)
        aggregate += weight * normalized
    aggregate /= mp.fsum(weights)
    eigenvalues, eigenvectors = mp.eighe(aggregate)
    descending_indices = list(reversed(range(size)))
    full_basis = mp.matrix([
        [eigenvectors[row, index] for index in descending_indices]
        for row in range(size)
    ])
    ordered_eigenvalues = [
        mp.re(eigenvalues[index]) for index in descending_indices
    ]
    core_basis = mp.matrix([
        [full_basis[row, column] for column in range(channel_rank)]
        for row in range(size)
    ])
    core_projector = core_basis * core_basis.transpose_conj()
    return {
        "component_grams": component_grams,
        "normalized_component_grams": normalized_grams,
        "gram_weights": weights,
        "trace_normalize": trace_normalize,
        "aggregate_gram": aggregate,
        "aggregate_eigenvalues_descending": ordered_eigenvalues,
        "full_channel_basis": full_basis,
        "core_channel_basis": core_basis,
        "core_projector": core_projector,
        "channel_rank": channel_rank,
        "unitarity_residual": mp.norm(
            full_basis.transpose_conj() * full_basis - mp.eye(size)
        ),
    }


def orthonormal_channel_basis_from_seeds(
    channel_seeds: list[list[mp.mpc]],
    ambient_size: int,
) -> dict[str, object]:
    """Complete explicit channel seeds to a unitary basis by Gram--Schmidt."""
    if ambient_size < 1 or not channel_seeds:
        raise ValueError("ambient size and channel seeds must be nonempty")
    if len(channel_seeds) > ambient_size or any(
        len(seed) != ambient_size for seed in channel_seeds
    ):
        raise ValueError("channel seeds have incompatible dimensions")
    tolerance = 1000 * mp.eps
    orthonormal_vectors: list[mp.matrix] = []

    def append_if_independent(vector: mp.matrix) -> bool:
        residual = mp.matrix([mp.mpc(vector[index]) for index in range(ambient_size)])
        for basis_vector in orthonormal_vectors:
            residual -= basis_vector * (
                basis_vector.transpose_conj() * residual
            )[0, 0]
        residual_norm = mp.norm(residual)
        if residual_norm <= tolerance:
            return False
        orthonormal_vectors.append(residual / residual_norm)
        return True

    for seed in channel_seeds:
        if not append_if_independent(mp.matrix([mp.mpc(value) for value in seed])):
            raise ValueError("channel seeds must be linearly independent")
    core_rank = len(orthonormal_vectors)
    for coordinate in range(ambient_size):
        standard_basis = mp.zeros(ambient_size, 1)
        standard_basis[coordinate] = 1
        append_if_independent(standard_basis)
        if len(orthonormal_vectors) == ambient_size:
            break
    full_basis = mp.matrix([
        [orthonormal_vectors[column][row] for column in range(ambient_size)]
        for row in range(ambient_size)
    ])
    core_basis = mp.matrix([
        [full_basis[row, column] for column in range(core_rank)]
        for row in range(ambient_size)
    ])
    return {
        "channel_seeds": [
            [mp.mpc(value) for value in seed] for seed in channel_seeds
        ],
        "ambient_size": ambient_size,
        "core_rank": core_rank,
        "full_channel_basis": full_basis,
        "core_channel_basis": core_basis,
        "core_projector": core_basis * core_basis.transpose_conj(),
        "unitarity_residual": mp.norm(
            full_basis.transpose_conj() * full_basis - mp.eye(ambient_size)
        ),
    }


def forced_physical_transverse_channel_basis(
    component_gram: mp.matrix,
    transverse_seeds: list[list[mp.mpc]] | None = None,
    physical_vector: list[mp.mpc] | None = None,
) -> dict[str, object]:
    """Best rank-two plane containing a prescribed physical direction.

    The second channel maximizes ``v*Gv`` among unit vectors in the span of
    the supplied seeds after orthogonal projection away from the physical
    vector.  With no seeds, the admissible transverse space is the whole
    physical orthogonal complement.  Thus the construction is the forced-
    physical Ky Fan solution, optionally restricted to an algebraic
    incidence subspace.
    """
    if component_gram.rows != component_gram.cols:
        raise ValueError("component Gram must be square")
    size = component_gram.rows
    if size < 2:
        raise ValueError("component Gram must have size at least two")
    physical = mp.matrix(
        [mp.mpc(1) for _ in range(size)]
        if physical_vector is None
        else [mp.mpc(value) for value in physical_vector]
    )
    if physical.rows != size or mp.norm(physical) == 0:
        raise ValueError("physical vector must be nonzero and compatible")
    physical_unit = physical / mp.norm(physical)
    seeds = (
        [
            [mp.mpc(1 if row == column else 0) for row in range(size)]
            for column in range(size)
        ]
        if transverse_seeds is None
        else transverse_seeds
    )
    if not seeds or any(len(seed) != size for seed in seeds):
        raise ValueError("transverse seeds must be nonempty and compatible")
    scale = max(
        mp.mpf(1),
        max(
            abs(component_gram[row, column])
            for row in range(size)
            for column in range(size)
        ),
    )
    tolerance = 1000 * mp.eps * scale
    transverse_frame: list[mp.matrix] = []
    seed_projection_residuals = []
    for seed in seeds:
        vector = mp.matrix([mp.mpc(value) for value in seed])
        vector -= physical_unit * (
            physical_unit.transpose_conj() * vector
        )[0, 0]
        for frame_vector in transverse_frame:
            vector -= frame_vector * (
                frame_vector.transpose_conj() * vector
            )[0, 0]
        residual_norm = mp.norm(vector)
        seed_projection_residuals.append(residual_norm)
        if residual_norm > tolerance:
            transverse_frame.append(vector / residual_norm)
    if not transverse_frame:
        raise ValueError("transverse seeds contain no physical-orthogonal direction")
    frame = mp.matrix([
        [transverse_frame[column][row] for column in range(len(transverse_frame))]
        for row in range(size)
    ])
    gram = (component_gram + component_gram.transpose_conj()) / 2
    compressed = frame.transpose_conj() * gram * frame
    eigenvalues, eigenvectors = mp.eighe(compressed)
    leading_index = eigenvalues.rows - 1
    transverse = frame * mp.matrix([
        eigenvectors[index, leading_index]
        for index in range(eigenvectors.rows)
    ])
    basis = orthonormal_channel_basis_from_seeds(
        [
            [physical[row] for row in range(size)],
            [transverse[row] for row in range(size)],
        ],
        size,
    )
    return {
        "component_gram": gram,
        "physical_vector": physical,
        "physical_unit_vector": physical_unit,
        "transverse_seed_frame": frame,
        "transverse_seed_rank": frame.cols,
        "seed_projection_residuals": seed_projection_residuals,
        "compressed_transverse_gram": compressed,
        "compressed_eigenvalues": eigenvalues,
        "optimal_transverse_vector": transverse,
        "optimal_transverse_energy": mp.re(eigenvalues[leading_index]),
        "basis": basis,
        "physical_orthogonality_residual": abs(
            (physical_unit.transpose_conj() * transverse)[0, 0]
        ),
        "transverse_normalization_residual": abs(mp.norm(transverse) - 1),
    }


def vaughan_paired_incidence_channel_certificate(
    component_gram: mp.matrix,
    fixed_ratio: mp.mpf = mp.mpf(8) / 3,
) -> dict[str, object]:
    """Four-channel incidence reduction and a fixed paired-line certificate.

    The orthonormal label directions are the physical sum, the two internal
    pair differences, and the coarse pair imbalance::

        e=(1,1,1,1)/2,
        u=(1,-1,0,0)/sqrt(2),
        v=(0,0,-1,1)/sqrt(2),
        c=(1,1,-1,-1)/2.

    The paired optimum is the leading eigenline of the ``u,v`` compression.
    If its coordinates are ``(q,1)``, then

        conj(B) q^2 + (C-A) q - B = 0

    for the Hermitian paired block ``[[A,B],[conj(B),C]]``.  The function
    also compares this line with the fixed real ratio and measures how far
    the unrestricted forced-physical optimum leaks into the coarse channel.
    """
    if component_gram.rows != 4 or component_gram.cols != 4:
        raise ValueError("paired Vaughan incidence requires a four-channel Gram")
    fixed_ratio = mp.mpf(fixed_ratio)
    incidence_basis = mp.matrix([
        [mp.mpf("0.5"), 1 / mp.sqrt(2), 0, mp.mpf("0.5")],
        [mp.mpf("0.5"), -1 / mp.sqrt(2), 0, mp.mpf("0.5")],
        [mp.mpf("0.5"), 0, -1 / mp.sqrt(2), -mp.mpf("0.5")],
        [mp.mpf("0.5"), 0, 1 / mp.sqrt(2), -mp.mpf("0.5")],
    ])
    gram = (component_gram + component_gram.transpose_conj()) / 2
    incidence_gram = (
        incidence_basis.transpose_conj() * gram * incidence_basis
    )
    paired_block = mp.matrix([
        [incidence_gram[1, 1], incidence_gram[1, 2]],
        [incidence_gram[2, 1], incidence_gram[2, 2]],
    ])
    paired = forced_physical_transverse_channel_basis(
        gram,
        transverse_seeds=[[1, -1, 0, 0], [0, 0, -1, 1]],
    )
    unrestricted = forced_physical_transverse_channel_basis(gram)
    paired_vector = paired["optimal_transverse_vector"]
    paired_coordinates = incidence_basis.transpose_conj() * paired_vector
    denominator = paired_coordinates[2]
    tolerance = 1000 * mp.eps * max(
        mp.mpf(1), mp.norm(paired_block)
    )
    if abs(denominator) <= tolerance:
        raise ArithmeticError("paired optimal ratio is infinite")
    optimal_ratio = paired_coordinates[1] / denominator
    first_diagonal = paired_block[0, 0]
    coupling = paired_block[0, 1]
    second_diagonal = paired_block[1, 1]
    ratio_quadratic_residual = (
        mp.conj(coupling) * optimal_ratio**2
        + (second_diagonal - first_diagonal) * optimal_ratio
        - coupling
    )
    fixed_line_sine_formula = abs(optimal_ratio - fixed_ratio) / mp.sqrt(
        (1 + abs(optimal_ratio) ** 2) * (1 + fixed_ratio**2)
    )
    fixed_transverse = mp.matrix([
        fixed_ratio / mp.sqrt(2),
        -fixed_ratio / mp.sqrt(2),
        -1 / mp.sqrt(2),
        1 / mp.sqrt(2),
    ]) / mp.sqrt(1 + fixed_ratio**2)
    paired_line_inner = (
        fixed_transverse.transpose_conj() * paired_vector
    )[0, 0]
    fixed_line_sine_direct = mp.sqrt(max(
        mp.mpf(0), 1 - abs(paired_line_inner) ** 2
    ))
    unrestricted_vector = unrestricted["optimal_transverse_vector"]
    unrestricted_coordinates = (
        incidence_basis.transpose_conj() * unrestricted_vector
    )
    coarse_leakage = abs(unrestricted_coordinates[3])
    unrestricted_paired_denominator = unrestricted_coordinates[2]
    if abs(unrestricted_paired_denominator) <= tolerance:
        raise ArithmeticError("unrestricted paired projection ratio is infinite")
    unrestricted_projected_ratio = (
        unrestricted_coordinates[1] / unrestricted_paired_denominator
    )
    unrestricted_projected_line_sine = abs(
        unrestricted_projected_ratio - fixed_ratio
    ) / mp.sqrt(
        (1 + abs(unrestricted_projected_ratio) ** 2)
        * (1 + fixed_ratio**2)
    )
    fixed_to_unrestricted_sine_formula = mp.sqrt(
        coarse_leakage**2
        + (1 - coarse_leakage**2) * unrestricted_projected_line_sine**2
    )
    fixed_to_unrestricted_inner = (
        fixed_transverse.transpose_conj() * unrestricted_vector
    )[0, 0]
    fixed_to_unrestricted_sine_direct = mp.sqrt(max(
        mp.mpf(0), 1 - abs(fixed_to_unrestricted_inner) ** 2
    ))
    paired_eigenvalues = mp.eighe(paired_block, eigvals_only=True)
    return {
        "component_gram": gram,
        "incidence_basis": incidence_basis,
        "incidence_gram": incidence_gram,
        "paired_block": paired_block,
        "paired_eigenvalues": paired_eigenvalues,
        "paired_spectral_gap": mp.re(
            paired_eigenvalues[1] - paired_eigenvalues[0]
        ),
        "paired_optimal": paired,
        "unrestricted_optimal": unrestricted,
        "optimal_ratio": optimal_ratio,
        "fixed_ratio": fixed_ratio,
        "ratio_quadratic_residual": ratio_quadratic_residual,
        "fixed_line_sine_formula": fixed_line_sine_formula,
        "fixed_line_sine_direct": fixed_line_sine_direct,
        "fixed_line_sine_residual": (
            fixed_line_sine_formula - fixed_line_sine_direct
        ),
        "unrestricted_incidence_coordinates": unrestricted_coordinates,
        "unrestricted_projected_ratio": unrestricted_projected_ratio,
        "unrestricted_projected_line_sine": (
            unrestricted_projected_line_sine
        ),
        "coarse_leakage": coarse_leakage,
        "fixed_to_unrestricted_sine_formula": (
            fixed_to_unrestricted_sine_formula
        ),
        "fixed_to_unrestricted_sine_direct": (
            fixed_to_unrestricted_sine_direct
        ),
        "fixed_to_unrestricted_sine_residual": (
            fixed_to_unrestricted_sine_formula
            - fixed_to_unrestricted_sine_direct
        ),
        "incidence_unitarity_residual": mp.norm(
            incidence_basis.transpose_conj() * incidence_basis - mp.eye(4)
        ),
    }


def vaughan_incidence_separated_channel_certificate(
    component_gram: mp.matrix,
) -> dict[str, object]:
    """Best one-line-per-incidence-sector rank-two channel plane.

    In the fixed incidence basis ``(e,u,v,c)``, split label space as

        span(e,c) direct-sum span(u,v).

    Among rank-two planes that are the direct sum of one line in each
    sector, the trace-maximizer consists of the leading eigenline of the two
    compressed 2-by-2 blocks.  Its physical/coarse line is written
    ``(1,tau)`` and its paired line ``(q,1)`` whenever those affine charts
    are finite.  Unlike the forced-physical construction, a nonzero ``tau``
    does not contain the exact physical direction.
    """
    paired_data = vaughan_paired_incidence_channel_certificate(component_gram)
    gram = paired_data["component_gram"]
    incidence_basis = paired_data["incidence_basis"]
    incidence_gram = paired_data["incidence_gram"]
    physical_coarse_block = mp.matrix([
        [incidence_gram[0, 0], incidence_gram[0, 3]],
        [incidence_gram[3, 0], incidence_gram[3, 3]],
    ])
    paired_block = paired_data["paired_block"]
    physical_eigenvalues, physical_eigenvectors = mp.eighe(
        physical_coarse_block
    )
    paired_eigenvalues, paired_eigenvectors = mp.eighe(paired_block)
    physical_coordinates = mp.matrix([
        physical_eigenvectors[0, 1], physical_eigenvectors[1, 1]
    ])
    paired_coordinates = mp.matrix([
        paired_eigenvectors[0, 1], paired_eigenvectors[1, 1]
    ])
    tolerance = 1000 * mp.eps * max(
        mp.mpf(1), mp.norm(incidence_gram)
    )
    if abs(physical_coordinates[0]) <= tolerance:
        raise ArithmeticError("physical/coarse tilt is infinite")
    if abs(paired_coordinates[1]) <= tolerance:
        raise ArithmeticError("paired ratio is infinite")
    physical_coarse_tilt = (
        physical_coordinates[1] / physical_coordinates[0]
    )
    paired_ratio = paired_coordinates[0] / paired_coordinates[1]
    physical_sector_frame = mp.matrix([
        [incidence_basis[row, 0], incidence_basis[row, 3]]
        for row in range(4)
    ])
    paired_sector_frame = mp.matrix([
        [incidence_basis[row, 1], incidence_basis[row, 2]]
        for row in range(4)
    ])
    physical_coarse_vector = physical_sector_frame * physical_coordinates
    paired_vector = paired_sector_frame * paired_coordinates
    basis = orthonormal_channel_basis_from_seeds(
        [
            [physical_coarse_vector[row] for row in range(4)],
            [paired_vector[row] for row in range(4)],
        ],
        4,
    )
    core_trace = mp.re(mp.fsum(
        (
            basis["core_channel_basis"][:, column].transpose_conj()
            * gram
            * basis["core_channel_basis"][:, column]
        )[0, 0]
        for column in range(2)
    ))
    optimal_sector_trace = mp.re(
        physical_eigenvalues[1] + paired_eigenvalues[1]
    )
    return {
        "component_gram": gram,
        "incidence_basis": incidence_basis,
        "incidence_gram": incidence_gram,
        "physical_coarse_block": physical_coarse_block,
        "paired_block": paired_block,
        "physical_coarse_eigenvalues": physical_eigenvalues,
        "paired_eigenvalues": paired_eigenvalues,
        "physical_coarse_vector": physical_coarse_vector,
        "paired_vector": paired_vector,
        "physical_coarse_tilt": physical_coarse_tilt,
        "paired_ratio": paired_ratio,
        "basis": basis,
        "core_trace": core_trace,
        "optimal_sector_trace": optimal_sector_trace,
        "trace_optimality_residual": core_trace - optimal_sector_trace,
        "sector_orthogonality_residual": abs(
            (physical_coarse_vector.transpose_conj() * paired_vector)[0, 0]
        ),
    }


def vaughan_incidence_separated_basis_from_ratios(
    physical_coarse_tilt: mp.mpc,
    paired_ratio: mp.mpc,
) -> dict[str, object]:
    """Fixed tilted Vaughan incidence plane from two affine ratios."""
    tau = mp.mpc(physical_coarse_tilt)
    ratio = mp.mpc(paired_ratio)
    incidence_basis = mp.matrix([
        [mp.mpf("0.5"), 1 / mp.sqrt(2), 0, mp.mpf("0.5")],
        [mp.mpf("0.5"), -1 / mp.sqrt(2), 0, mp.mpf("0.5")],
        [mp.mpf("0.5"), 0, -1 / mp.sqrt(2), -mp.mpf("0.5")],
        [mp.mpf("0.5"), 0, 1 / mp.sqrt(2), -mp.mpf("0.5")],
    ])
    physical_coarse_vector = incidence_basis * mp.matrix([1, 0, 0, tau])
    paired_vector = incidence_basis * mp.matrix([0, ratio, 1, 0])
    basis = orthonormal_channel_basis_from_seeds(
        [
            [physical_coarse_vector[row] for row in range(4)],
            [paired_vector[row] for row in range(4)],
        ],
        4,
    )
    return {
        "physical_coarse_tilt": tau,
        "paired_ratio": ratio,
        "incidence_basis": incidence_basis,
        "physical_coarse_vector": physical_coarse_vector,
        "paired_vector": paired_vector,
        "basis": basis,
        "sector_orthogonality_residual": abs(
            (physical_coarse_vector.transpose_conj() * paired_vector)[0, 0]
        ),
        "physical_inclusion_residual": mp.norm(
            (mp.eye(4) - basis["core_projector"])
            * mp.matrix([1, 1, 1, 1])
        ),
    }


def incidence_separated_plane_angle_certificate(
    first_physical_coarse_tilt: mp.mpc,
    first_paired_ratio: mp.mpc,
    second_physical_coarse_tilt: mp.mpc,
    second_paired_ratio: mp.mpc,
) -> dict[str, object]:
    """Exact projector angle between two incidence-separated planes."""
    first_tilt = mp.mpc(first_physical_coarse_tilt)
    first_ratio = mp.mpc(first_paired_ratio)
    second_tilt = mp.mpc(second_physical_coarse_tilt)
    second_ratio = mp.mpc(second_paired_ratio)

    def line_sine(first: mp.mpc, second: mp.mpc) -> mp.mpf:
        return abs(first - second) / mp.sqrt(
            (1 + abs(first) ** 2) * (1 + abs(second) ** 2)
        )

    physical_coarse_sine = line_sine(first_tilt, second_tilt)
    paired_sine = line_sine(first_ratio, second_ratio)
    formula_projector_sine = max(physical_coarse_sine, paired_sine)
    first_basis = vaughan_incidence_separated_basis_from_ratios(
        first_tilt, first_ratio
    )["basis"]
    second_basis = vaughan_incidence_separated_basis_from_ratios(
        second_tilt, second_ratio
    )["basis"]
    projector_difference = (
        first_basis["core_projector"] - second_basis["core_projector"]
    )
    difference_eigenvalues = mp.eighe(
        (projector_difference + projector_difference.transpose_conj()) / 2,
        eigvals_only=True,
    )
    direct_projector_sine = max(
        abs(difference_eigenvalues[index])
        for index in range(difference_eigenvalues.rows)
    )
    return {
        "first_physical_coarse_tilt": first_tilt,
        "first_paired_ratio": first_ratio,
        "second_physical_coarse_tilt": second_tilt,
        "second_paired_ratio": second_ratio,
        "physical_coarse_line_sine": physical_coarse_sine,
        "paired_line_sine": paired_sine,
        "formula_projector_sine": formula_projector_sine,
        "direct_projector_sine": direct_projector_sine,
        "projector_sine_residual": (
            formula_projector_sine - direct_projector_sine
        ),
        "projector_difference": projector_difference,
    }


def frozen_vaughan_tilted_incidence_basis() -> dict[str, object]:
    """Explicit integer incidence basis with tilt 1/20 and paired ratio 3.

    Core seeds are ``(21,21,19,19)`` and ``(3,-3,-1,1)``.  Sector-orthogonal
    tail seeds are ``(19,19,-21,-21)`` and ``(-1,1,-3,3)``.  After the
    displayed normalizations they form a unitary basis.  The all-ones
    physical vector has relative squared tail mass exactly ``1/401``.
    """
    integer_columns = [
        [21, 21, 19, 19],
        [3, -3, -1, 1],
        [19, 19, -21, -21],
        [-1, 1, -3, 3],
    ]
    column_norms = [2 * mp.sqrt(401), 2 * mp.sqrt(5)] * 2
    full_basis = mp.matrix([
        [
            mp.mpf(integer_columns[column][row]) / column_norms[column]
            for column in range(4)
        ]
        for row in range(4)
    ])
    core_basis = mp.matrix([
        [full_basis[row, column] for column in range(2)]
        for row in range(4)
    ])
    physical = mp.matrix([1, 1, 1, 1])
    physical_coordinates = full_basis.transpose_conj() * physical
    core_mass = mp.fsum(
        abs(physical_coordinates[index]) ** 2 for index in range(2)
    )
    tail_mass = mp.fsum(
        abs(physical_coordinates[index]) ** 2 for index in range(2, 4)
    )
    return {
        "integer_columns": integer_columns,
        "column_norms": column_norms,
        "full_channel_basis": full_basis,
        "core_channel_basis": core_basis,
        "core_projector": core_basis * core_basis.transpose_conj(),
        "core_rank": 2,
        "ambient_size": 4,
        "physical_vector": physical,
        "physical_coordinates": physical_coordinates,
        "physical_core_mass": core_mass,
        "physical_tail_mass": tail_mass,
        "relative_physical_core_mass": core_mass / 4,
        "relative_physical_tail_mass": tail_mass / 4,
        "unitarity_residual": mp.norm(
            full_basis.transpose_conj() * full_basis - mp.eye(4)
        ),
        "physical_mass_residual": core_mass + tail_mass - 4,
        "physical_coarse_tilt": mp.mpf(1) / 20,
        "paired_ratio": mp.mpf(3),
    }


def frozen_vaughan_tilted_channel_coefficients(
    cutoff: int,
    mobius_cutoff: int,
    mangoldt_cutoff: int,
) -> dict[str, object]:
    """Exact arithmetic coefficients in the frozen tilted channel basis.

    Put ``a_U=mu_{<=U}*1``, ``X=a_U*Lambda_{>V}``,
    ``Y=a_U*Lambda_{<=V}``, ``L=Lambda`` and ``V0=Lambda_{<=V}``.
    The normalized channels are

        (2X+19L)/(2sqrt(401)),
        (4X+6Y-L+2V0)/(2sqrt(5)),
        (40X-21L)/(2sqrt(401)),
        (2X-2Y-3L+6V0)/(2sqrt(5)).

    The first two are core channels and the last two tail channels.  Their
    physical synthesis is exactly ``L`` through the first and third channel
    with coefficients ``40/sqrt(401)`` and ``-2/sqrt(401)``.
    """
    decomposition = balanced_vaughan_coefficients(
        cutoff, mobius_cutoff, mangoldt_cutoff
    )
    component_names = list(decomposition["uncentered_components"])
    components = [
        decomposition["uncentered_components"][name]
        for name in component_names
    ]
    basis = frozen_vaughan_tilted_incidence_basis()
    full_basis = basis["full_channel_basis"]
    channels = [
        [
            mp.fsum(
                mp.conj(full_basis[component, channel])
                * components[component][integer]
                for component in range(4)
            )
            for integer in range(cutoff + 1)
        ]
        for channel in range(4)
    ]
    type_i_high = [
        components[0][integer] + components[1][integer]
        for integer in range(cutoff + 1)
    ]
    type_i_low = [
        -components[1][integer] for integer in range(cutoff + 1)
    ]
    mangoldt = [
        mp.mpc(0) if integer == 0 else mp.mpc(von_mangoldt(integer))
        for integer in range(cutoff + 1)
    ]
    mangoldt_low = components[3]
    expected_channels = [
        [
            (2 * type_i_high[integer] + 19 * mangoldt[integer])
            / (2 * mp.sqrt(401))
            for integer in range(cutoff + 1)
        ],
        [
            (
                4 * type_i_high[integer]
                + 6 * type_i_low[integer]
                - mangoldt[integer]
                + 2 * mangoldt_low[integer]
            ) / (2 * mp.sqrt(5))
            for integer in range(cutoff + 1)
        ],
        [
            (40 * type_i_high[integer] - 21 * mangoldt[integer])
            / (2 * mp.sqrt(401))
            for integer in range(cutoff + 1)
        ],
        [
            (
                2 * type_i_high[integer]
                - 2 * type_i_low[integer]
                - 3 * mangoldt[integer]
                + 6 * mangoldt_low[integer]
            ) / (2 * mp.sqrt(5))
            for integer in range(cutoff + 1)
        ],
    ]
    formula_residuals = [
        [
            channels[channel][integer]
            - expected_channels[channel][integer]
            for integer in range(cutoff + 1)
        ]
        for channel in range(4)
    ]
    reconstructed_mangoldt = [
        40 / mp.sqrt(401) * channels[0][integer]
        - 2 / mp.sqrt(401) * channels[2][integer]
        for integer in range(cutoff + 1)
    ]
    reconstruction_residuals = [
        reconstructed_mangoldt[integer] - mangoldt[integer]
        for integer in range(cutoff + 1)
    ]
    return {
        "cutoff": cutoff,
        "mobius_cutoff": mobius_cutoff,
        "mangoldt_cutoff": mangoldt_cutoff,
        "component_names": component_names,
        "decomposition": decomposition,
        "basis": basis,
        "type_i_high_coefficients": type_i_high,
        "type_i_low_coefficients": type_i_low,
        "mangoldt_coefficients": mangoldt,
        "mangoldt_low_coefficients": mangoldt_low,
        "channel_names": [
            "core_sum_tilt",
            "core_paired",
            "tail_sum_residual",
            "tail_paired",
        ],
        "channel_coefficients": channels,
        "expected_channel_coefficients": expected_channels,
        "formula_residuals": formula_residuals,
        "maximum_formula_residual": max(
            abs(value) for channel in formula_residuals for value in channel
        ),
        "reconstructed_mangoldt": reconstructed_mangoldt,
        "reconstruction_residuals": reconstruction_residuals,
        "maximum_reconstruction_residual": max(
            abs(value) for value in reconstruction_residuals
        ),
    }


def component_projector_no_free_lunch_certificate(
    core_projector: mp.matrix,
    physical_vector: list[mp.mpc],
    amplitude: mp.mpf,
) -> dict[str, object]:
    """Rank-one Gram showing tail/coupling control cannot bound core energy.

    If the physical vector has a nonzero core projection, concentrate an
    arbitrary positive rank-one Gram on that direction.  Its tail and
    core-tail coupling vanish while its physical energy grows linearly with
    ``amplitude``.  If the core projection vanishes, the analogous Gram is
    concentrated in the tail.  This is a finite-dimensional obstruction to
    any compression argument that omits the sector carrying the physical
    vector.
    """
    if core_projector.rows != core_projector.cols:
        raise ValueError("core projector must be square")
    size = core_projector.rows
    physical = mp.matrix([mp.mpc(value) for value in physical_vector])
    if physical.rows != size or mp.norm(physical) == 0:
        raise ValueError("physical vector must be nonzero and compatible")
    amplitude = mp.mpf(amplitude)
    if amplitude <= 0:
        raise ValueError("amplitude must be positive")
    projector = (core_projector + core_projector.transpose_conj()) / 2
    complement = mp.eye(size) - projector
    tolerance = 1000 * mp.eps
    if mp.norm(projector * projector - projector) > tolerance:
        raise ValueError("core projector must be orthogonal")
    core_physical = projector * physical
    tail_physical = complement * physical
    if mp.norm(core_physical) > tolerance:
        concentration_sector = "core"
        direction = core_physical / mp.norm(core_physical)
    else:
        concentration_sector = "tail"
        direction = tail_physical / mp.norm(tail_physical)
    gram = amplitude * direction * direction.transpose_conj()
    core_block = projector * gram * projector
    coupling_block = projector * gram * complement
    tail_block = complement * gram * complement
    physical_energy = mp.re(
        (physical.transpose_conj() * gram * physical)[0, 0]
    )
    return {
        "core_projector": projector,
        "physical_vector": physical,
        "amplitude": amplitude,
        "concentration_sector": concentration_sector,
        "concentration_direction": direction,
        "rank_one_gram": gram,
        "core_block": core_block,
        "coupling_block": coupling_block,
        "tail_block": tail_block,
        "physical_energy": physical_energy,
        "core_block_norm": mp.norm(core_block),
        "coupling_block_norm": mp.norm(coupling_block),
        "tail_block_norm": mp.norm(tail_block),
        "gram_positivity_minimum": min(
            mp.re(value)
            for value in mp.eighe(gram, eigvals_only=True)
        ),
    }


def channel_projector_stability_certificate(
    component_gram: mp.matrix,
    full_channel_basis: mp.matrix,
    channel_rank: int,
) -> dict[str, object]:
    """Compare a fixed channel projector with the leading spectral projector."""
    if component_gram.rows != component_gram.cols:
        raise ValueError("component Gram must be square")
    size = component_gram.rows
    if full_channel_basis.rows != size or full_channel_basis.cols != size:
        raise ValueError("full channel basis has incompatible dimensions")
    if not 1 <= channel_rank < size:
        raise ValueError("channel rank must be positive and smaller than size")
    gram = (component_gram + component_gram.transpose_conj()) / 2
    eigenvalues, eigenvectors = mp.eighe(gram)
    descending_indices = list(reversed(range(size)))
    leading_basis = mp.matrix([
        [
            eigenvectors[row, descending_indices[column]]
            for column in range(channel_rank)
        ]
        for row in range(size)
    ])
    fixed_core_basis = mp.matrix([
        [full_channel_basis[row, column] for column in range(channel_rank)]
        for row in range(size)
    ])
    fixed_projector = fixed_core_basis * fixed_core_basis.transpose_conj()
    leading_projector = leading_basis * leading_basis.transpose_conj()
    projector_difference = fixed_projector - leading_projector
    projector_difference_eigenvalues = mp.eighe(
        (projector_difference + projector_difference.transpose_conj()) / 2,
        eigvals_only=True,
    )
    principal_sine = max(
        abs(projector_difference_eigenvalues[index])
        for index in range(projector_difference_eigenvalues.rows)
    )
    transformed = (
        full_channel_basis.transpose_conj() * gram * full_channel_basis
    )
    tail_count = size - channel_rank
    coupling = mp.matrix([
        [
            transformed[row, channel_rank + column]
            for column in range(tail_count)
        ]
        for row in range(channel_rank)
    ])
    tail = mp.matrix([
        [
            transformed[channel_rank + row, channel_rank + column]
            for column in range(tail_count)
        ]
        for row in range(tail_count)
    ])
    tail_eigenvalues = mp.eighe(tail, eigvals_only=True)
    actual_tail_edge = max(
        mp.mpf("0"),
        max(mp.re(tail_eigenvalues[index]) for index in range(tail_count)),
    )
    coupling_square = coupling.transpose_conj() * coupling
    coupling_square_eigenvalues = mp.eighe(
        coupling_square, eigvals_only=True
    )
    actual_coupling_norm = mp.sqrt(max(
        mp.mpf("0"),
        max(
            mp.re(coupling_square_eigenvalues[index])
            for index in range(coupling_square_eigenvalues.rows)
        ),
    ))
    leading_eigenvalue = mp.re(eigenvalues[descending_indices[0]])
    omitted_eigenvalue = mp.re(eigenvalues[descending_indices[channel_rank]])
    tail_angle_upper = (
        omitted_eigenvalue
        + (leading_eigenvalue - omitted_eigenvalue) * principal_sine**2
    )
    coupling_angle_upper = 2 * leading_eigenvalue * principal_sine
    return {
        "component_gram": gram,
        "full_channel_basis": full_channel_basis,
        "channel_rank": channel_rank,
        "leading_spectral_basis": leading_basis,
        "fixed_projector": fixed_projector,
        "leading_projector": leading_projector,
        "projector_difference": projector_difference,
        "projector_difference_eigenvalues": projector_difference_eigenvalues,
        "maximum_principal_sine": principal_sine,
        "leading_eigenvalue": leading_eigenvalue,
        "first_omitted_eigenvalue": omitted_eigenvalue,
        "actual_tail_edge": actual_tail_edge,
        "principal_angle_tail_upper_bound": tail_angle_upper,
        "actual_coupling_norm": actual_coupling_norm,
        "principal_angle_coupling_upper_bound": coupling_angle_upper,
        "tail_bound_slack": tail_angle_upper - actual_tail_edge,
        "coupling_bound_slack": coupling_angle_upper - actual_coupling_norm,
    }


def component_channel_feshbach_majorant(
    component_gram: mp.matrix,
    full_channel_basis: mp.matrix,
    channel_rank: int,
    physical_vector: list[mp.mpc] | None = None,
    tail_threshold: mp.mpf | None = None,
) -> dict[str, object]:
    """Loewner majorant from a fixed core basis and Feshbach completion.

    In core/tail coordinates write ``G=[[A,B],[B*,C]]``.  For
    ``epsilon>||C||`` the returned majorant is

        diag(A+B(epsilon I-C)^-1 B*, epsilon I).

    Its difference from G is positive by Schur completion.  If no threshold
    is supplied and the physical vector has a nonzero tail component, the
    physical-direction upper bound is minimized over epsilon by a
    one-dimensional convex solve.  If the physical vector lies wholly in
    the core while still coupling to the tail, the scalar infimum occurs
    only as epsilon tends to infinity; an explicit finite threshold is then
    required.
    """
    if component_gram.rows != component_gram.cols:
        raise ValueError("component Gram must be square")
    size = component_gram.rows
    if full_channel_basis.rows != size or full_channel_basis.cols != size:
        raise ValueError("full channel basis has incompatible dimensions")
    if not 1 <= channel_rank < size:
        raise ValueError("channel rank must be positive and smaller than size")
    physical = (
        mp.matrix([mp.mpc(1) for _ in range(size)])
        if physical_vector is None
        else mp.matrix([mp.mpc(value) for value in physical_vector])
    )
    if physical.rows != size:
        raise ValueError("physical vector has incompatible length")
    unitary_residual = mp.norm(
        full_channel_basis.transpose_conj() * full_channel_basis
        - mp.eye(size)
    )
    scale = max(
        mp.mpf("1"),
        max(
            abs(component_gram[row, column])
            for row in range(size)
            for column in range(size)
        ),
    )
    tolerance = 1000 * mp.eps * scale
    if unitary_residual > tolerance:
        raise ValueError("full channel basis must be unitary")
    gram = (component_gram + component_gram.transpose_conj()) / 2
    transformed = (
        full_channel_basis.transpose_conj() * gram * full_channel_basis
    )
    tail_count = size - channel_rank
    core = mp.matrix([
        [transformed[row, column] for column in range(channel_rank)]
        for row in range(channel_rank)
    ])
    coupling = mp.matrix([
        [
            transformed[row, channel_rank + column]
            for column in range(tail_count)
        ]
        for row in range(channel_rank)
    ])
    tail = mp.matrix([
        [
            transformed[channel_rank + row, channel_rank + column]
            for column in range(tail_count)
        ]
        for row in range(tail_count)
    ])
    tail_eigenvalues, tail_eigenvectors = mp.eighe(tail)
    tail_spectral_edge = max(
        mp.mpf("0"),
        max(mp.re(tail_eigenvalues[index]) for index in range(tail_count)),
    )
    physical_coordinates = full_channel_basis.transpose_conj() * physical
    physical_core = mp.matrix([
        physical_coordinates[index] for index in range(channel_rank)
    ])
    physical_tail = mp.matrix([
        physical_coordinates[channel_rank + index]
        for index in range(tail_count)
    ])
    coupling_source = coupling.transpose_conj() * physical_core
    diagonal_coupling_source = (
        tail_eigenvectors.transpose_conj() * coupling_source
    )
    physical_tail_norm_squared = mp.re(
        (physical_tail.transpose_conj() * physical_tail)[0, 0]
    )
    physical_norm_squared = mp.re(
        (physical.transpose_conj() * physical)[0, 0]
    )
    zero_tail_tolerance = tolerance**2 * max(
        mp.mpf(1), physical_norm_squared
    )
    separation = 1000 * mp.eps * max(mp.mpf("1"), tail_spectral_edge)
    lower_threshold = tail_spectral_edge + separation

    def derivative(threshold: mp.mpf) -> mp.mpf:
        return physical_tail_norm_squared - mp.fsum(
            abs(diagonal_coupling_source[index]) ** 2
            / (threshold - mp.re(tail_eigenvalues[index])) ** 2
            for index in range(tail_count)
        )

    threshold_optimized = tail_threshold is None
    if tail_threshold is None:
        if physical_tail_norm_squared <= zero_tail_tolerance:
            if mp.norm(coupling_source) > tolerance:
                raise ValueError(
                    "physical Feshbach infimum has no finite optimizer; "
                    "supply a tail threshold"
                )
            chosen_threshold = lower_threshold
        elif derivative(lower_threshold) >= 0:
            chosen_threshold = lower_threshold
        else:
            upper_threshold = max(
                lower_threshold + 1,
                2 * lower_threshold,
            )
            while derivative(upper_threshold) < 0:
                upper_threshold *= 2
            left = lower_threshold
            right = upper_threshold
            for _ in range(160):
                midpoint = (left + right) / 2
                if derivative(midpoint) < 0:
                    left = midpoint
                else:
                    right = midpoint
            chosen_threshold = (left + right) / 2
    else:
        chosen_threshold = mp.mpf(tail_threshold)
        if chosen_threshold <= tail_spectral_edge:
            raise ValueError("tail threshold must exceed the tail spectral edge")
    tail_gap = chosen_threshold * mp.eye(tail_count) - tail
    core_correction = (
        coupling * (tail_gap**-1) * coupling.transpose_conj()
    )
    core_majorant = core + core_correction
    coordinate_majorant = mp.zeros(size, size)
    for row in range(channel_rank):
        for column in range(channel_rank):
            coordinate_majorant[row, column] = core_majorant[row, column]
    for index in range(tail_count):
        coordinate_majorant[
            channel_rank + index, channel_rank + index
        ] = chosen_threshold
    majorant = (
        full_channel_basis
        * coordinate_majorant
        * full_channel_basis.transpose_conj()
    )
    difference = majorant - gram
    difference_eigenvalues = mp.eighe(
        (difference + difference.transpose_conj()) / 2,
        eigvals_only=True,
    )
    physical_energy = mp.re(
        (physical.transpose_conj() * gram * physical)[0, 0]
    )
    physical_upper = mp.re(
        (physical.transpose_conj() * majorant * physical)[0, 0]
    )
    core_physical_term = mp.re(
        (physical_core.transpose_conj() * core * physical_core)[0, 0]
    )
    coupling_completion_term = mp.re(
        (
            physical_core.transpose_conj()
            * core_correction
            * physical_core
        )[0, 0]
    )
    tail_physical_term = (
        chosen_threshold * physical_tail_norm_squared
    )
    return {
        "component_gram": gram,
        "full_channel_basis": full_channel_basis,
        "channel_rank": channel_rank,
        "transformed_component_gram": transformed,
        "core_block": core,
        "coupling_block": coupling,
        "tail_block": tail,
        "tail_eigenvalues": tail_eigenvalues,
        "tail_spectral_edge": tail_spectral_edge,
        "tail_threshold": chosen_threshold,
        "tail_threshold_optimized": threshold_optimized,
        "tail_gap": tail_gap,
        "core_correction": core_correction,
        "core_majorant": core_majorant,
        "coordinate_majorant": coordinate_majorant,
        "loewner_majorant": majorant,
        "majorant_difference_eigenvalues": difference_eigenvalues,
        "minimum_majorant_difference_eigenvalue": min(
            difference_eigenvalues[index]
            for index in range(difference_eigenvalues.rows)
        ),
        "physical_energy": physical_energy,
        "physical_upper_bound": physical_upper,
        "physical_upper_loss_factor": (
            physical_upper / physical_energy
            if physical_energy > 0 else mp.inf
        ),
        "core_physical_term": core_physical_term,
        "coupling_completion_term": coupling_completion_term,
        "tail_physical_term": tail_physical_term,
        "physical_tail_norm_squared": physical_tail_norm_squared,
        "unitary_residual": unitary_residual,
        "decomposition_residual": abs(
            physical_upper
            - core_physical_term
            - coupling_completion_term
            - tail_physical_term
        ),
    }


def optimal_real_rank_one_background_split(
    component_gram: mp.matrix,
    background_couplings: list[mp.mpc],
    background_norm_squared: mp.mpf,
    anchor_index: int = 0,
) -> dict[str, object]:
    """Optimally distribute one background vector among components.

    If ``P`` is the Gram of vectors p_r, ``b_r=<p_r,c>`` and
    ``C=||c||^2``, this minimizes

        sum_r ||p_r-alpha_r*c||^2

    over real ``alpha_r`` with ``sum alpha_r=1``.  Real splitting preserves
    the conjugation symmetry between positive and negative height blocks.
    """
    if component_gram.rows != component_gram.cols:
        raise ValueError("component Gram must be square")
    size = component_gram.rows
    if size < 1 or len(background_couplings) != size:
        raise ValueError("background couplings must match the Gram size")
    if not 0 <= anchor_index < size:
        raise ValueError("anchor index is outside the component range")
    background_norm_squared = mp.mpf(background_norm_squared)
    if background_norm_squared <= 0:
        raise ValueError("background norm squared must be positive")
    couplings = [mp.mpc(value) for value in background_couplings]
    real_couplings = [mp.re(value) for value in couplings]
    mean_real_coupling = mp.fsum(real_couplings) / size
    optimal_weights = [
        mp.mpf(1) / size
        + (value - mean_real_coupling) / background_norm_squared
        for value in real_couplings
    ]
    equal_weights = [mp.mpf(1) / size for _ in range(size)]
    anchor_weights = [
        mp.mpf(1 if index == anchor_index else 0)
        for index in range(size)
    ]

    def balanced_gram(weights: list[mp.mpf]) -> mp.matrix:
        gram = mp.zeros(size, size)
        for row in range(size):
            for column in range(size):
                gram[row, column] = (
                    component_gram[row, column]
                    - weights[column] * couplings[row]
                    - weights[row] * mp.conj(couplings[column])
                    + weights[row]
                    * weights[column]
                    * background_norm_squared
                )
        return gram

    def diagonal_budget(gram: mp.matrix) -> mp.mpf:
        return mp.re(mp.fsum(gram[index, index] for index in range(size)))

    optimized_gram = balanced_gram(optimal_weights)
    equal_gram = balanced_gram(equal_weights)
    anchor_gram = balanced_gram(anchor_weights)
    full_discrepancy_energy = mp.re(
        mp.fsum(
            component_gram[row, column]
            for row in range(size)
            for column in range(size)
        )
        - 2 * mp.fsum(couplings)
        + background_norm_squared
    )
    optimized_total = mp.re(mp.fsum(optimized_gram))
    optimized_diagonal = diagonal_budget(optimized_gram)
    minimum_formula = (
        mp.re(mp.fsum(component_gram[index, index] for index in range(size)))
        - mp.fsum(value**2 for value in real_couplings)
        / background_norm_squared
        + (
            background_norm_squared - mp.fsum(real_couplings)
        ) ** 2
        / (size * background_norm_squared)
    )
    return {
        "optimal_weights": optimal_weights,
        "equal_weights": equal_weights,
        "anchor_weights": anchor_weights,
        "optimized_gram": optimized_gram,
        "equal_split_gram": equal_gram,
        "anchor_split_gram": anchor_gram,
        "optimized_diagonal_budget": optimized_diagonal,
        "equal_split_diagonal_budget": diagonal_budget(equal_gram),
        "anchor_split_diagonal_budget": diagonal_budget(anchor_gram),
        "optimized_cross_energy": optimized_total - optimized_diagonal,
        "full_discrepancy_energy": full_discrepancy_energy,
        "optimized_total_energy": optimized_total,
        "energy_invariance_residual": (
            optimized_total - full_discrepancy_energy
        ),
        "minimum_formula": minimum_formula,
        "minimum_formula_residual": optimized_diagonal - minimum_formula,
        "weight_sum_residual": mp.fsum(optimal_weights) - 1,
        "real_background_couplings": real_couplings,
        "background_norm_squared": background_norm_squared,
    }


def abel_continuum_lag_quadrature(
    sigma: mp.mpf,
    scale: mp.mpf,
    lag_start: mp.mpf,
    lag_end: mp.mpf,
    lag_cells: int,
    log_window_width: mp.mpf,
    geometric_mesh: bool = True,
) -> dict[str, object]:
    """Positive midpoint quadrature of the Abel continuum Hodge vector."""
    sigma = mp.mpf(sigma)
    scale = mp.mpf(scale)
    lag_start = mp.mpf(lag_start)
    lag_end = mp.mpf(lag_end)
    log_window_width = mp.mpf(log_window_width)
    if not mp.mpf("0.5") <= sigma < 1:
        raise ValueError("sigma must lie in [1/2,1)")
    if scale <= 0 or log_window_width <= 0:
        raise ValueError("scale and log window width must be positive")
    if lag_start <= 0 or lag_end <= lag_start or lag_cells < 1:
        raise ValueError("invalid lag interval or cell count")
    if geometric_mesh:
        ratio = mp.power(lag_end / lag_start, mp.mpf(1) / lag_cells)
        edges = [
            lag_start * ratio**index for index in range(lag_cells + 1)
        ]
    else:
        width = (lag_end - lag_start) / lag_cells
        edges = [lag_start + index * width for index in range(lag_cells + 1)]
    edges[-1] = lag_end
    shape = 1 - sigma
    factor = mp.power(scale, shape)

    def mass(left: mp.mpf, right: mp.mpf) -> mp.mpf:
        return factor * mp.gammainc(
            shape, mp.exp(left) / scale, mp.exp(right) / scale
        )

    small_mass = mass(mp.mpf("0"), lag_start)
    nodes = [mp.mpf("0")]
    coefficients = [small_mass]
    localization_norm_bound = small_mass * mp.sqrt(
        2 * min(log_window_width, lag_start)
    )
    for left, right in zip(edges[:-1], edges[1:]):
        midpoint = (left + right) / 2
        cell_mass = mass(left, right)
        nodes.append(midpoint)
        coefficients.append(cell_mass)
        localization_norm_bound += cell_mass * mp.sqrt(
            2 * min(log_window_width, (right - left) / 2)
        )
    tail_mass = factor * mp.gammainc(
        shape, mp.exp(lag_end) / scale, mp.inf
    )
    exact_total_mass = factor * mp.gammainc(shape, 1 / scale, mp.inf)
    return {
        "sigma": sigma,
        "scale": scale,
        "lag_nodes": nodes,
        "coefficients": coefficients,
        "lag_edges": edges,
        "small_interval_mass": small_mass,
        "represented_mass": mp.fsum(coefficients),
        "tail_mass": tail_mass,
        "exact_total_mass": exact_total_mass,
        "mass_reconstruction_residual": (
            mp.fsum(coefficients) + tail_mass - exact_total_mass
        ),
        "localization_vector_norm_bound": localization_norm_bound,
        "tail_vector_norm_bound": mp.sqrt(log_window_width) * tail_mass,
        "geometric_mesh": geometric_mesh,
    }


def balanced_vaughan_continuum_gauge_audit(
    cutoff: int,
    mobius_cutoff: int,
    mangoldt_cutoff: int,
    center_height: mp.mpf,
    log_window_width: mp.mpf,
    horizontal_offset: mp.mpf,
    abel_scale: mp.mpf,
    continuum_lag_start: mp.mpf,
    continuum_lag_end: mp.mpf,
    continuum_lag_cells: int,
) -> dict[str, object]:
    """Optimize the continuum gauge of a truncated Vaughan Hodge Gram."""
    center_height = mp.mpf(center_height)
    log_window_width = mp.mpf(log_window_width)
    horizontal_offset = mp.mpf(horizontal_offset)
    abel_scale = mp.mpf(abel_scale)
    sigma = mp.mpf("0.5") + horizontal_offset
    decomposition = balanced_vaughan_coefficients(
        cutoff, mobius_cutoff, mangoldt_cutoff
    )
    integer_nodes = [mp.log(integer) for integer in range(1, cutoff + 1)]
    integer_weights = [
        mp.power(integer, -sigma) * mp.exp(-mp.mpf(integer) / abel_scale)
        for integer in range(1, cutoff + 1)
    ]
    component_data = {
        name: (
            integer_nodes,
            [
                coefficients[integer] * integer_weights[integer - 1]
                for integer in range(1, cutoff + 1)
            ],
        )
        for name, coefficients in decomposition[
            "uncentered_components"
        ].items()
    }
    continuum = abel_continuum_lag_quadrature(
        sigma,
        abel_scale,
        continuum_lag_start,
        continuum_lag_end,
        continuum_lag_cells,
        log_window_width,
    )
    extended_data = dict(component_data)
    extended_data["abel_continuum"] = (
        continuum["lag_nodes"], continuum["coefficients"]
    )
    extended_gram_data = modulated_atomic_component_gram(
        extended_data, center_height, log_window_width
    )
    extended_gram = extended_gram_data["component_gram"]
    component_count = len(component_data)
    component_gram = mp.matrix([
        [extended_gram[row, column] for column in range(component_count)]
        for row in range(component_count)
    ])
    background_couplings = [
        extended_gram[row, component_count]
        for row in range(component_count)
    ]
    background_norm_squared = mp.re(
        extended_gram[component_count, component_count]
    )
    split = optimal_real_rank_one_background_split(
        component_gram,
        background_couplings,
        background_norm_squared,
    )
    direct_nodes: list[mp.mpf] = []
    direct_coefficients: list[mp.mpc] = []
    for nodes, coefficients in component_data.values():
        direct_nodes.extend(nodes)
        direct_coefficients.extend(coefficients)
    direct_nodes.extend(continuum["lag_nodes"])
    direct_coefficients.extend(
        [-coefficient for coefficient in continuum["coefficients"]]
    )
    direct_energy = stationary_modulated_interval_energy(
        direct_nodes,
        direct_coefficients,
        center_height,
        log_window_width,
    )
    return {
        "decomposition": decomposition,
        "component_data": component_data,
        "continuum_quadrature": continuum,
        "extended_component_gram": extended_gram,
        "background_couplings": background_couplings,
        "background_norm_squared": background_norm_squared,
        "optimal_split": split,
        "direct_discrepancy_energy": direct_energy,
        "direct_energy_residual": (
            split["full_discrepancy_energy"]
            - direct_energy["modulated_interval_energy"]
        ),
        "center_height": center_height,
        "log_window_width": log_window_width,
        "horizontal_offset": horizontal_offset,
        "abel_scale": abel_scale,
        "continuum_is_midpoint_quadrature": True,
    }


def constrained_real_quadratic_minimizer(
    quadratic_gram: mp.matrix,
    constraint_matrix: mp.matrix,
    constraint_target: list[mp.mpf],
) -> dict[str, object]:
    """Minimize z^T Q z subject to A z=b through the exact KKT system."""
    if quadratic_gram.rows != quadratic_gram.cols:
        raise ValueError("quadratic Gram must be square")
    variable_count = quadratic_gram.rows
    constraint_count = constraint_matrix.rows
    if constraint_matrix.cols != variable_count:
        raise ValueError("constraint matrix has incompatible width")
    if len(constraint_target) != constraint_count:
        raise ValueError("constraint target has incompatible length")
    symmetry_residual = max(
        abs(quadratic_gram[row, column] - quadratic_gram[column, row])
        for row in range(variable_count)
        for column in range(variable_count)
    )
    tolerance = 100 * mp.eps * max(
        mp.mpf("1"),
        max(
            abs(quadratic_gram[row, column])
            for row in range(variable_count)
            for column in range(variable_count)
        ),
    )
    if symmetry_residual > tolerance:
        raise ValueError("quadratic Gram must be real symmetric")
    eigenvalues = mp.eigsy(
        mp.matrix([
            [
                mp.re(quadratic_gram[row, column])
                for column in range(variable_count)
            ]
            for row in range(variable_count)
        ]),
        eigvals_only=True,
    )
    minimum_eigenvalue = min(
        eigenvalues[index] for index in range(eigenvalues.rows)
    )
    if minimum_eigenvalue < -tolerance:
        raise ValueError("quadratic Gram must be positive semidefinite")
    system_size = variable_count + constraint_count
    kkt = mp.zeros(system_size, system_size)
    rhs = mp.zeros(system_size, 1)
    for row in range(variable_count):
        for column in range(variable_count):
            kkt[row, column] = mp.re(quadratic_gram[row, column])
        for constraint in range(constraint_count):
            kkt[row, variable_count + constraint] = constraint_matrix[
                constraint, row
            ]
            kkt[variable_count + constraint, row] = constraint_matrix[
                constraint, row
            ]
    for constraint, target in enumerate(constraint_target):
        rhs[variable_count + constraint] = mp.mpf(target)
    try:
        solution = mp.lu_solve(kkt, rhs)
    except ZeroDivisionError as error:
        raise ValueError(
            "KKT system is singular; remove redundant gauge variables"
        ) from error
    variables = mp.matrix([
        solution[index] for index in range(variable_count)
    ])
    multipliers = mp.matrix([
        solution[variable_count + index]
        for index in range(constraint_count)
    ])
    constraint_residual = constraint_matrix * variables - mp.matrix(
        [mp.mpf(value) for value in constraint_target]
    )
    stationarity_residual = (
        quadratic_gram * variables
        + constraint_matrix.transpose() * multipliers
    )
    objective = mp.re(
        (variables.transpose() * quadratic_gram * variables)[0, 0]
    )
    return {
        "variables": variables,
        "multipliers": multipliers,
        "minimum_objective": objective,
        "constraint_residual_norm": mp.norm(constraint_residual),
        "stationarity_residual_norm": mp.norm(stationarity_residual),
        "quadratic_symmetry_residual": symmetry_residual,
        "minimum_quadratic_eigenvalue": minimum_eigenvalue,
        "kkt_matrix": kkt,
    }


def simplex_scale_affine_quadratic_minimizer(
    quadratic_gram: mp.matrix,
    scale_count: int,
    component_count: int,
) -> dict[str, object]:
    """Globally minimize a cutoff-simplex/background-affine quadratic.

    The first ``scale_count`` variables are constrained to be nonnegative
    and sum to one.  The remaining background shares only have to sum to
    one.  Enumerating all nonempty scale faces gives the exact finite
    convex-program solution for modest scale count.
    """
    if scale_count < 1 or component_count < 1:
        raise ValueError("scale and component counts must be positive")
    if scale_count > 12:
        raise ValueError("simplex face enumeration is limited to 12 scales")
    variable_count = scale_count + component_count
    if quadratic_gram.rows != variable_count or (
        quadratic_gram.cols != variable_count
    ):
        raise ValueError("quadratic Gram has incompatible dimensions")
    feasibility_tolerance = 1000 * mp.eps * max(
        mp.mpf("1"),
        max(
            abs(quadratic_gram[row, column])
            for row in range(variable_count)
            for column in range(variable_count)
        ),
    )
    candidates = []
    examined_face_count = 0
    for mask in range(1, 1 << scale_count):
        active_scales = [
            index for index in range(scale_count) if mask & (1 << index)
        ]
        selected_indices = active_scales + list(
            range(scale_count, variable_count)
        )
        selected_count = len(selected_indices)
        subgram = mp.matrix([
            [
                quadratic_gram[row_index, column_index]
                for column_index in selected_indices
            ]
            for row_index in selected_indices
        ])
        constraints = mp.zeros(2, selected_count)
        for index in range(len(active_scales)):
            constraints[0, index] = 1
        for index in range(len(active_scales), selected_count):
            constraints[1, index] = 1
        examined_face_count += 1
        try:
            optimizer = constrained_real_quadratic_minimizer(
                subgram, constraints, [mp.mpf(1), mp.mpf(1)]
            )
        except ValueError:
            continue
        active_weights = [
            optimizer["variables"][index]
            for index in range(len(active_scales))
        ]
        if any(weight < -feasibility_tolerance for weight in active_weights):
            continue
        full_variables = mp.zeros(variable_count, 1)
        for selected_index, original_index in enumerate(selected_indices):
            full_variables[original_index] = optimizer["variables"][
                selected_index
            ]
        candidates.append({
            "active_scale_indices": active_scales,
            "variables": full_variables,
            "minimum_objective": optimizer["minimum_objective"],
            "face_optimizer": optimizer,
        })
    if not candidates:
        raise ArithmeticError("no feasible simplex face was found")
    best = min(candidates, key=lambda item: item["minimum_objective"])
    variables = best["variables"]
    return {
        "variables": variables,
        "optimal_scale_weights": [
            variables[index] for index in range(scale_count)
        ],
        "optimal_background_weights": [
            variables[scale_count + index]
            for index in range(component_count)
        ],
        "active_scale_indices": best["active_scale_indices"],
        "minimum_objective": best["minimum_objective"],
        "examined_face_count": examined_face_count,
        "feasible_face_count": len(candidates),
        "scale_weight_sum_residual": (
            mp.fsum(variables[index] for index in range(scale_count)) - 1
        ),
        "background_weight_sum_residual": (
            mp.fsum(
                variables[scale_count + index]
                for index in range(component_count)
            ) - 1
        ),
        "minimum_scale_weight": min(
            variables[index] for index in range(scale_count)
        ),
    }


def multiscale_vaughan_continuum_gauge_audit(
    cutoff: int,
    cutoff_pairs: list[tuple[int, int]],
    center_height: mp.mpf,
    log_window_width: mp.mpf,
    horizontal_offset: mp.mpf,
    abel_scale: mp.mpf,
    continuum_lag_start: mp.mpf,
    continuum_lag_end: mp.mpf,
    continuum_lag_cells: int,
) -> dict[str, object]:
    """Jointly optimize Vaughan cutoff mixing and continuum allocation.

    Every cutoff pair supplies the same exact sum ``Lambda`` with four
    different Type-I/II components.  Real weights summing to one mix those
    decompositions without changing the arithmetic vector.  A second affine
    constraint distributes the continuum vector among the four categories.
    """
    if not cutoff_pairs:
        raise ValueError("at least one Vaughan cutoff pair is required")
    if len(set(cutoff_pairs)) != len(cutoff_pairs):
        raise ValueError("Vaughan cutoff pairs must be distinct")
    center_height = mp.mpf(center_height)
    log_window_width = mp.mpf(log_window_width)
    horizontal_offset = mp.mpf(horizontal_offset)
    abel_scale = mp.mpf(abel_scale)
    sigma = mp.mpf("0.5") + horizontal_offset
    decompositions = [
        balanced_vaughan_coefficients(cutoff, first, second)
        for first, second in cutoff_pairs
    ]
    component_names = list(decompositions[0]["uncentered_components"])
    component_count = len(component_names)
    scale_count = len(cutoff_pairs)
    integer_nodes = [mp.log(integer) for integer in range(1, cutoff + 1)]
    integer_weights = [
        mp.power(integer, -sigma) * mp.exp(-mp.mpf(integer) / abel_scale)
        for integer in range(1, cutoff + 1)
    ]
    extended_data: dict[
        str, tuple[list[mp.mpf], list[mp.mpc]]
    ] = {}
    for scale_index, decomposition in enumerate(decompositions):
        for component_name, coefficients in decomposition[
            "uncentered_components"
        ].items():
            extended_data[f"{scale_index}:{component_name}"] = (
                integer_nodes,
                [
                    coefficients[integer] * integer_weights[integer - 1]
                    for integer in range(1, cutoff + 1)
                ],
            )
    continuum = abel_continuum_lag_quadrature(
        sigma,
        abel_scale,
        continuum_lag_start,
        continuum_lag_end,
        continuum_lag_cells,
        log_window_width,
    )
    continuum_index = scale_count * component_count
    extended_data["abel_continuum"] = (
        continuum["lag_nodes"], continuum["coefficients"]
    )
    gram_data = modulated_atomic_component_gram(
        extended_data, center_height, log_window_width
    )
    extended_gram = gram_data["component_gram"]
    background_norm_squared = mp.re(
        extended_gram[continuum_index, continuum_index]
    )

    def component_index(scale_index: int, component_index_value: int) -> int:
        return scale_index * component_count + component_index_value

    variable_count = scale_count + component_count
    quadratic = mp.zeros(variable_count, variable_count)
    for first_scale in range(scale_count):
        for second_scale in range(scale_count):
            quadratic[first_scale, second_scale] = mp.re(mp.fsum(
                extended_gram[
                    component_index(first_scale, component),
                    component_index(second_scale, component),
                ]
                for component in range(component_count)
            ))
    for scale_index in range(scale_count):
        for component in range(component_count):
            coupling = mp.re(extended_gram[
                component_index(scale_index, component), continuum_index
            ])
            quadratic[scale_index, scale_count + component] = -coupling
            quadratic[scale_count + component, scale_index] = -coupling
    for component in range(component_count):
        quadratic[
            scale_count + component, scale_count + component
        ] = background_norm_squared
    constraints = mp.zeros(2, variable_count)
    for scale_index in range(scale_count):
        constraints[0, scale_index] = 1
    for component in range(component_count):
        constraints[1, scale_count + component] = 1
    optimizer = constrained_real_quadratic_minimizer(
        quadratic, constraints, [mp.mpf(1), mp.mpf(1)]
    )
    simplex_optimizer = simplex_scale_affine_quadratic_minimizer(
        quadratic, scale_count, component_count
    )
    variables = optimizer["variables"]
    scale_weights = [variables[index] for index in range(scale_count)]
    continuum_weights = [
        variables[scale_count + index]
        for index in range(component_count)
    ]

    def assemble_balanced_component_gram(
        local_scale_weights: list[mp.mpf],
        local_continuum_weights: list[mp.mpf],
    ) -> mp.matrix:
        balanced_gram = mp.zeros(component_count, component_count)
        mixed_couplings = [
            mp.fsum(
                local_scale_weights[scale_index]
                * extended_gram[
                    component_index(scale_index, component),
                    continuum_index,
                ]
                for scale_index in range(scale_count)
            )
            for component in range(component_count)
        ]
        for row_component in range(component_count):
            for column_component in range(component_count):
                prime_entry = mp.fsum(
                    local_scale_weights[first_scale]
                    * local_scale_weights[second_scale]
                    * extended_gram[
                        component_index(first_scale, row_component),
                        component_index(second_scale, column_component),
                    ]
                    for first_scale in range(scale_count)
                    for second_scale in range(scale_count)
                )
                balanced_gram[row_component, column_component] = (
                    prime_entry
                    - local_continuum_weights[column_component]
                    * mixed_couplings[row_component]
                    - local_continuum_weights[row_component]
                    * mp.conj(mixed_couplings[column_component])
                    + local_continuum_weights[row_component]
                    * local_continuum_weights[column_component]
                    * background_norm_squared
                )
        return balanced_gram

    optimized_component_gram = assemble_balanced_component_gram(
        scale_weights, continuum_weights
    )
    simplex_variables = simplex_optimizer["variables"]
    simplex_scale_weights = [
        simplex_variables[index] for index in range(scale_count)
    ]
    simplex_continuum_weights = [
        simplex_variables[scale_count + index]
        for index in range(component_count)
    ]
    simplex_component_gram = assemble_balanced_component_gram(
        simplex_scale_weights, simplex_continuum_weights
    )
    optimized_diagonal = mp.re(mp.fsum(
        optimized_component_gram[index, index]
        for index in range(component_count)
    ))
    optimized_total = mp.re(mp.fsum(optimized_component_gram))

    single_scale_records = []
    for scale_index, cutoff_pair in enumerate(cutoff_pairs):
        prime_gram = mp.matrix([
            [
                extended_gram[
                    component_index(scale_index, row),
                    component_index(scale_index, column),
                ]
                for column in range(component_count)
            ]
            for row in range(component_count)
        ])
        couplings = [
            extended_gram[
                component_index(scale_index, component), continuum_index
            ]
            for component in range(component_count)
        ]
        split = optimal_real_rank_one_background_split(
            prime_gram, couplings, background_norm_squared
        )
        single_scale_records.append({
            "cutoff_pair": cutoff_pair,
            "optimal_split": split,
        })
    equal_scale_weights = [mp.mpf(1) / scale_count] * scale_count
    equal_prime_gram = mp.zeros(component_count, component_count)
    equal_couplings = []
    for row in range(component_count):
        equal_couplings.append(mp.fsum(
            equal_scale_weights[scale_index]
            * extended_gram[
                component_index(scale_index, row), continuum_index
            ]
            for scale_index in range(scale_count)
        ))
        for column in range(component_count):
            equal_prime_gram[row, column] = mp.fsum(
                equal_scale_weights[first_scale]
                * equal_scale_weights[second_scale]
                * extended_gram[
                    component_index(first_scale, row),
                    component_index(second_scale, column),
                ]
                for first_scale in range(scale_count)
                for second_scale in range(scale_count)
            )
    equal_scale_split = optimal_real_rank_one_background_split(
        equal_prime_gram, equal_couplings, background_norm_squared
    )

    first_decomposition = decompositions[0]["uncentered_components"]
    direct_nodes: list[mp.mpf] = []
    direct_coefficients: list[mp.mpc] = []
    for coefficients in first_decomposition.values():
        direct_nodes.extend(integer_nodes)
        direct_coefficients.extend([
            coefficients[integer] * integer_weights[integer - 1]
            for integer in range(1, cutoff + 1)
        ])
    direct_nodes.extend(continuum["lag_nodes"])
    direct_coefficients.extend(
        [-coefficient for coefficient in continuum["coefficients"]]
    )
    direct_energy = stationary_modulated_interval_energy(
        direct_nodes,
        direct_coefficients,
        center_height,
        log_window_width,
    )["modulated_interval_energy"]
    return {
        "cutoff": cutoff,
        "cutoff_pairs": cutoff_pairs,
        "component_names": component_names,
        "decompositions": decompositions,
        "continuum_quadrature": continuum,
        "extended_component_gram": extended_gram,
        "quadratic_gram": quadratic,
        "optimizer": optimizer,
        "simplex_optimizer": simplex_optimizer,
        "optimal_scale_weights": scale_weights,
        "optimal_continuum_weights": continuum_weights,
        "optimal_scale_weight_l1": mp.fsum(
            abs(weight) for weight in scale_weights
        ),
        "optimal_continuum_weight_l1": mp.fsum(
            abs(weight) for weight in continuum_weights
        ),
        "optimized_component_gram": optimized_component_gram,
        "simplex_component_gram": simplex_component_gram,
        "optimized_channel_spectrum": component_gram_channel_spectrum(
            optimized_component_gram
        ),
        "simplex_channel_spectrum": component_gram_channel_spectrum(
            simplex_component_gram
        ),
        "optimized_diagonal_budget": optimized_diagonal,
        "optimized_total_energy": optimized_total,
        "direct_discrepancy_energy": direct_energy,
        "direct_energy_residual": optimized_total - direct_energy,
        "single_scale_records": single_scale_records,
        "best_single_scale_diagonal_budget": min(
            record["optimal_split"]["optimized_diagonal_budget"]
            for record in single_scale_records
        ),
        "equal_scale_split": equal_scale_split,
        "equal_scale_diagonal_budget": equal_scale_split[
            "optimized_diagonal_budget"
        ],
        "simplex_scale_diagonal_budget": simplex_optimizer[
            "minimum_objective"
        ],
        "center_height": center_height,
        "log_window_width": log_window_width,
        "horizontal_offset": horizontal_offset,
        "abel_scale": abel_scale,
    }


def mobius_log_divisor_moment(integer: int, power: int) -> mp.mpf:
    """Sum_{d|n} mu(d) log(d)^power, the polynomial mollifier charge."""
    if integer < 1:
        raise ValueError("integer must be positive")
    if power < 0:
        raise ValueError("power must be nonnegative")
    return mp.fsum(
        mobius(divisor) * mp.log(divisor) ** power
        for divisor in range(1, integer + 1)
        if integer % divisor == 0
    )


def polynomial_mobius_mollifier_coefficients(
    size: int,
    polynomial_coefficients: list[mp.mpf],
) -> list[mp.mpf]:
    """mu(n) P(log(n)/log(size)), with coefficients in increasing degree."""
    if size < 2:
        raise ValueError("size must be at least two")
    if not polynomial_coefficients:
        raise ValueError("polynomial coefficients must be nonempty")
    coefficients = [mp.mpf(value) for value in polynomial_coefficients]
    logarithmic_scale = mp.log(size)
    mollifier = [mp.mpf(0)] * (size + 1)
    for integer in range(1, size + 1):
        argument = mp.log(integer) / logarithmic_scale
        polynomial_value = mp.fsum(
            coefficient * argument**degree
            for degree, coefficient in enumerate(coefficients)
        )
        mollifier[integer] = mobius(integer) * polynomial_value
    return mollifier


def zeta_mollifier_low_convolution(
    mollifier_coefficients: list[mp.mpf],
) -> list[mp.mpf]:
    """Low coefficients of zeta(s) times a finite mollifier Dirichlet series."""
    if len(mollifier_coefficients) < 2:
        raise ValueError("mollifier must contain indices zero and one")
    size = len(mollifier_coefficients) - 1
    return [mp.mpf(0)] + [
        mp.fsum(
            mollifier_coefficients[divisor]
            for divisor in range(1, integer + 1)
            if integer % divisor == 0
        )
        for integer in range(1, size + 1)
    ]


def beurling_mollifier_residual(
    value: mp.mpf,
    mollifier_coefficients: list[mp.mpf],
) -> mp.mpf:
    """Real-space Nyman residual chi(x)+sum b_n {1/(nx)}."""
    value = mp.mpf(value)
    if value <= 0:
        raise ValueError("value must be positive")
    if len(mollifier_coefficients) < 2:
        raise ValueError("mollifier must contain indices zero and one")
    return (1 if value <= 1 else 0) + mp.fsum(
        mollifier_coefficients[index]
        * beurling_fractional_feature(index, value)
        for index in range(1, len(mollifier_coefficients))
    )


def beurling_mollifier_local_energy(
    mollifier_coefficients: list[mp.mpf],
) -> dict[str, object]:
    """Exact energy of a finite Nyman residual on y<=N (equiv. x>=1/N)."""
    if len(mollifier_coefficients) < 3:
        raise ValueError("mollifier size must be at least two")
    size = len(mollifier_coefficients) - 1
    slope = mp.fsum(
        mollifier_coefficients[index] / index
        for index in range(1, size + 1)
    )
    convolution = zeta_mollifier_low_convolution(mollifier_coefficients)
    cumulative_charge = mp.mpf("0")
    interval_energies = [abs(slope) ** 2]
    local_energy = interval_energies[0]
    for integer in range(1, size):
        cumulative_charge += convolution[integer]
        intercept = 1 - cumulative_charge
        interval_energy = (
            abs(slope) ** 2
            + 2
            * mp.re(slope * mp.conj(intercept))
            * mp.log(mp.mpf(integer + 1) / integer)
            + abs(intercept) ** 2
            * (mp.mpf(1) / integer - mp.mpf(1) / (integer + 1))
        )
        interval_energies.append(interval_energy)
        local_energy += interval_energy
    return {
        "slope": slope,
        "low_convolution": convolution,
        "interval_energies": interval_energies,
        "local_energy": local_energy,
    }


def linear_mobius_mollifier_slope(size: int) -> mp.mpf:
    """Return A_N(1) for b_n=mu(n)(1-log(n)/log(N))."""
    mollifier = polynomial_mobius_mollifier_coefficients(size, [1, -1])
    return mp.fsum(mollifier[integer] / integer for integer in range(1, size + 1))


def weighted_mertens_normalized_slope(size: int) -> mp.mpf:
    """Return log(N) A_N(1) through its exact weighted Mertens integral."""
    if size < 2:
        raise ValueError("size must be at least two")
    logarithmic_scale = mp.log(size)
    mertens_value = 0
    total = mp.mpf("0")
    for integer in range(1, size):
        mertens_value += mobius(integer)
        left_weight = mp.log(size / mp.mpf(integer)) / integer
        right_weight = (
            mp.log(size / mp.mpf(integer + 1)) / (integer + 1)
        )
        total += mertens_value * (left_weight - right_weight)
    return total


def chebyshev_ratio_mean(size: int) -> mp.mpf:
    """Mean of psi(y)/y on 1<=y<=N, written as a prime-power sum."""
    if size < 2:
        raise ValueError("size must be at least two")
    return mp.fsum(
        von_mangoldt(integer) * mp.log(size / mp.mpf(integer))
        for integer in range(2, size + 1)
    ) / (size - 1)


def linear_mollifier_local_hodge_decomposition(size: int) -> dict[str, mp.mpf]:
    """Exact scalar/variance split of the linear Nyman residual for y<=N.

    With y=1/x, this is the energy on x>=1/N.  The omitted x<1/N
    boundary layer is deliberately not estimated here.
    """
    if size < 2:
        raise ValueError("size must be at least two")
    logarithmic_scale = mp.log(size)
    slope = linear_mobius_mollifier_slope(size)
    normalized_slope = logarithmic_scale * slope
    ratio_mean = chebyshev_ratio_mean(size)

    chebyshev_value = mp.mpf("0")
    ratio_second_moment = mp.mpf("0")
    piecewise_energy = slope**2  # The interval 0<y<1.
    for integer in range(1, size):
        chebyshev_value += von_mangoldt(integer)
        reciprocal_drop = mp.mpf(1) / integer - mp.mpf(1) / (integer + 1)
        ratio_second_moment += chebyshev_value**2 * reciprocal_drop
        piecewise_energy += (
            slope**2
            - 2
            * slope
            * chebyshev_value
            / logarithmic_scale
            * mp.log(mp.mpf(integer + 1) / integer)
            + (chebyshev_value / logarithmic_scale) ** 2
            * reciprocal_drop
        )

    centered_variance = ratio_second_moment - (size - 1) * ratio_mean**2
    # Suppress only roundoff-level negativity in the mathematically PSD term.
    tolerance = mp.eps * max(1, abs(ratio_second_moment)) * 20
    if -tolerance <= centered_variance < 0:
        centered_variance = mp.mpf("0")
    scalar_mismatch = (size - 1) * (normalized_slope - ratio_mean) ** 2
    decomposed_energy = (
        normalized_slope**2 + centered_variance + scalar_mismatch
    ) / logarithmic_scale**2
    return {
        "slope": slope,
        "normalized_slope": normalized_slope,
        "ratio_mean": ratio_mean,
        "ratio_second_moment": ratio_second_moment,
        "centered_variance": centered_variance,
        "scalar_mismatch": scalar_mismatch,
        "local_energy": decomposed_energy,
        "piecewise_energy": piecewise_energy,
    }


def reduced_denominator_density(denominator: int) -> mp.mpf:
    """Return product_{p|r}(1-p^-2) for a positive denominator r."""
    if denominator < 1:
        raise ValueError("denominator must be positive")
    remaining = denominator
    prime = 2
    density = mp.mpf("1")
    while prime * prime <= remaining:
        if remaining % prime == 0:
            density *= 1 - mp.mpf(1) / prime**2
            while remaining % prime == 0:
                remaining //= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        density *= 1 - mp.mpf(1) / remaining**2
    return density


def beurling_periodic_fourier_energy(
    mollifier_coefficients: list[mp.mpf],
) -> dict[str, object]:
    """Parseval mass of 1+sum b_n {y/n}, grouped by reduced denominator."""
    if len(mollifier_coefficients) < 2:
        raise ValueError("mollifier must contain indices zero and one")
    size = len(mollifier_coefficients) - 1
    mean = 1 + mp.fsum(mollifier_coefficients[1:]) / 2
    divisor_sums = [mp.mpf("0")] * (size + 1)
    conductor_masses = [mp.mpf("0")] * (size + 1)
    for denominator in range(1, size + 1):
        divisor_sum = mp.fsum(
            mollifier_coefficients[multiple] / multiple
            for multiple in range(denominator, size + 1, denominator)
        )
        divisor_sums[denominator] = divisor_sum
        conductor_masses[denominator] = (
            denominator**2
            * abs(divisor_sum) ** 2
            * reduced_denominator_density(denominator)
            / 12
        )
    oscillatory_energy = mp.fsum(conductor_masses[1:])
    return {
        "mean": mean,
        "divisor_sums": divisor_sums,
        "conductor_masses": conductor_masses,
        "oscillatory_energy": oscillatory_energy,
        "periodic_mean_square": abs(mean) ** 2 + oscillatory_energy,
    }


def mollifier_conductor_amplitude(
    mollifier_coefficients: list[mp.mpf], denominator: int
) -> mp.mpf:
    """Return r*S_N(r)=sum_{r|n} b_n*r/n for a Farey conductor r."""
    if len(mollifier_coefficients) < 2:
        raise ValueError("mollifier must contain indices zero and one")
    size = len(mollifier_coefficients) - 1
    if denominator < 1 or denominator > size:
        raise ValueError("denominator must lie between one and the mollifier size")
    return mp.fsum(
        mollifier_coefficients[multiple] * denominator / multiple
        for multiple in range(denominator, size + 1, denominator)
    )


def linear_mollifier_conductor_amplitude_majorant(
    size: int, denominator: int
) -> mp.mpf:
    """Endpoint-smoothing majorant for |r*S_N(r)| of the linear filter."""
    if size < 2:
        raise ValueError("size must be at least two")
    if denominator < 1 or denominator > size:
        raise ValueError("denominator must lie between one and size")
    logarithmic_ratio = mp.log(mp.mpf(size) / denominator)
    return (
        logarithmic_ratio + logarithmic_ratio**2 / 2
    ) / mp.log(size)


def parabolic_shell_diagonal_energy(
    mollifier_coefficients: list[mp.mpf], scale: mp.mpf
) -> dict[str, mp.mpf]:
    """Fourier diagonal energy on [Y,2Y] from conductors r>sqrt(Y)."""
    if len(mollifier_coefficients) < 2:
        raise ValueError("mollifier must contain indices zero and one")
    size = len(mollifier_coefficients) - 1
    scale = mp.mpf(scale)
    if scale <= 0:
        raise ValueError("scale must be positive")
    threshold = int(mp.floor(mp.sqrt(scale)))
    fourier = beurling_periodic_fourier_energy(mollifier_coefficients)
    conductor_mass = mp.fsum(
        fourier["conductor_masses"][denominator]
        for denominator in range(max(1, threshold + 1), size + 1)
    )
    return {
        "threshold": mp.mpf(threshold),
        "conductor_mass": conductor_mass,
        "diagonal_energy": conductor_mass / (2 * scale),
    }


def farey_determinant_reduction(
    denominator: int, other_denominator: int, determinant: int
) -> dict[str, int | bool]:
    """Reduce h*r'-h'*r=Delta by gcd(r,r') and record primitive conditions."""
    if denominator < 1 or other_denominator < 1:
        raise ValueError("denominators must be positive")
    common_divisor = math.gcd(denominator, other_denominator)
    reduced_left = denominator // common_divisor
    reduced_right = other_denominator // common_divisor
    divisible = determinant % common_divisor == 0
    reduced_determinant = determinant // common_divisor if divisible else 0
    primitive_necessary = divisible and math.gcd(
        abs(reduced_determinant), reduced_left * reduced_right
    ) == 1
    return {
        "gcd": common_divisor,
        "left_quotient": reduced_left,
        "right_quotient": reduced_right,
        "lcm": denominator // common_divisor * other_denominator,
        "gcd_divides_determinant": divisible,
        "reduced_determinant": reduced_determinant,
        "primitive_necessary": primitive_necessary,
    }


def generic_unrestricted_farey_harmonic_correlation(
    left_coefficient: int,
    right_coefficient: int,
    determinant: int,
) -> dict[str, mp.mpf | int]:
    """Cotangent sum of 1/(uv) over A*u-B*v=Delta in the generic case."""
    if left_coefficient < 1 or right_coefficient < 1:
        raise ValueError("coefficients must be positive")
    common_divisor = math.gcd(left_coefficient, right_coefficient)
    if determinant == 0 or determinant % common_divisor != 0:
        raise ValueError("determinant must be nonzero and divisible by the gcd")
    reduced_left = left_coefficient // common_divisor
    reduced_right = right_coefficient // common_divisor
    reduced_determinant = determinant // common_divisor
    if (
        reduced_left <= 1
        or reduced_right <= 1
        or math.gcd(
            abs(reduced_determinant), reduced_left * reduced_right
        )
        != 1
    ):
        raise ValueError(
            "generic cotangent formula requires coprime nontrivial quotients"
        )
    initial_left = (
        reduced_determinant
        * pow(reduced_left, -1, reduced_right)
    ) % reduced_right
    initial_right = (
        reduced_left * initial_left - reduced_determinant
    ) // reduced_right
    correlation = mp.pi / reduced_determinant * (
        mp.cot(mp.pi * mp.mpf(initial_right) / reduced_left)
        - mp.cot(mp.pi * mp.mpf(initial_left) / reduced_right)
    )
    return {
        "reduced_left": reduced_left,
        "reduced_right": reduced_right,
        "reduced_determinant": reduced_determinant,
        "initial_left": initial_left,
        "initial_right": initial_right,
        "correlation": correlation,
    }


def coprime_farey_harmonic_reciprocity(
    left_denominator: int,
    right_denominator: int,
    reduced_determinant: int,
) -> dict[str, mp.mpf | int]:
    """Reciprocity formula for b*h-a*h'=delta with coprime a,b."""
    a = left_denominator
    b = right_denominator
    delta = reduced_determinant
    if a <= 1 or b <= 1 or math.gcd(a, b) != 1:
        raise ValueError("denominators must be nontrivial and coprime")
    if delta == 0 or math.gcd(abs(delta), a * b) != 1:
        raise ValueError("determinant must be nonzero and coprime to both")
    inverse_a = pow(a, -1, b)
    inverse_b = pow(b, -1, a)
    sign = 1 if (delta + 1) % 2 == 0 else -1
    correlation = (
        sign
        * mp.pi
        / delta
        * mp.sin(mp.pi * delta / (a * b))
        / (
            mp.sin(mp.pi * delta * inverse_a / b)
            * mp.sin(mp.pi * delta * inverse_b / a)
        )
    )
    return {
        "inverse_left_mod_right": inverse_a,
        "inverse_right_mod_left": inverse_b,
        "correlation": correlation,
        "uniform_bound": mp.pi**2 / 4,
    }


def finite_cotangent_dft(modulus: int, residue: int) -> dict[str, object]:
    """Exact finite Fourier expansion of cot(pi*k/q), with k nonzero mod q."""
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    reduced_residue = residue % modulus
    if reduced_residue == 0:
        raise ValueError("residue must be nonzero modulo the modulus")
    coefficients = [
        mp.mpf(modulus - 2 * frequency) / modulus
        for frequency in range(1, modulus)
    ]
    fourier_value = mp.j * mp.fsum(
        coefficients[frequency - 1]
        * mp.exp(
            -2
            * mp.pi
            * mp.j
            * frequency
            * reduced_residue
            / modulus
        )
        for frequency in range(1, modulus)
    )
    coefficient_l2_squared = mp.fsum(
        coefficient**2 for coefficient in coefficients
    )
    return {
        "residue": reduced_residue,
        "coefficients": coefficients,
        "fourier_value": fourier_value,
        "cotangent_value": mp.cot(
            mp.pi * reduced_residue / modulus
        ),
        "coefficient_l2_squared": coefficient_l2_squared,
        "coefficient_l2_squared_closed": mp.mpf(
            (modulus - 1) * (modulus - 2)
        )
        / (3 * modulus),
        "cotangent_grid_l2_squared": mp.mpf(
            (modulus - 1) * (modulus - 2)
        )
        / 3,
    }


def coprime_farey_cotangent_dft(
    left_denominator: int,
    right_denominator: int,
    reduced_determinant: int,
) -> dict[str, object]:
    """Paired Kloosterman-fraction DFT of the coprime Farey kernel."""
    a = left_denominator
    b = right_denominator
    delta = reduced_determinant
    if a <= 1 or b <= 1 or math.gcd(a, b) != 1:
        raise ValueError("denominators must be nontrivial and coprime")
    if delta == 0 or math.gcd(abs(delta), a * b) != 1:
        raise ValueError("determinant must be nonzero and coprime to both")
    inverse_a = pow(a, -1, b)
    inverse_b = pow(b, -1, a)
    right_modulus_term = finite_cotangent_dft(
        b, delta * inverse_a
    )
    left_modulus_term = finite_cotangent_dft(
        a, delta * inverse_b
    )
    correlation = -mp.pi / delta * (
        right_modulus_term["fourier_value"]
        + left_modulus_term["fourier_value"]
    )
    return {
        "inverse_left_mod_right": inverse_a,
        "inverse_right_mod_left": inverse_b,
        "right_modulus_term": right_modulus_term,
        "left_modulus_term": left_modulus_term,
        "correlation": correlation,
    }


def coprime_farey_product_modulus_dft(
    left_denominator: int,
    right_denominator: int,
    reduced_determinant: int,
) -> dict[str, object]:
    """Single product-modulus DFT retaining the cotangent reciprocity difference."""
    a = left_denominator
    b = right_denominator
    delta = reduced_determinant
    if a <= 1 or b <= 1 or math.gcd(a, b) != 1:
        raise ValueError("denominators must be nontrivial and coprime")
    if delta == 0 or math.gcd(abs(delta), a * b) != 1:
        raise ValueError("determinant must be nonzero and coprime to both")
    product_modulus = a * b
    inverse_a = pow(a, -1, b)
    lifted_residue = (delta * a * inverse_a) % product_modulus
    paired_coefficients = [
        mp.mpf(product_modulus - 2 * frequency)
        / product_modulus
        * (
            1
            - mp.exp(
                2
                * mp.pi
                * mp.j
                * frequency
                * delta
                / product_modulus
            )
        )
        for frequency in range(1, product_modulus)
    ]
    cotangent_difference = mp.j * mp.fsum(
        paired_coefficients[frequency - 1]
        * mp.exp(
            -2
            * mp.pi
            * mp.j
            * frequency
            * lifted_residue
            / product_modulus
        )
        for frequency in range(1, product_modulus)
    )
    return {
        "product_modulus": product_modulus,
        "lifted_residue": lifted_residue,
        "paired_coefficients": paired_coefficients,
        "paired_coefficient_l2_squared": mp.fsum(
            abs(coefficient) ** 2 for coefficient in paired_coefficients
        ),
        "cotangent_difference": cotangent_difference,
        "correlation": -mp.pi * cotangent_difference / delta,
    }


def euler_totient(integer: int) -> int:
    """Euler's totient, used in the conductor Mellin-residue audit."""
    if integer < 1:
        raise ValueError("integer must be positive")
    result = integer
    remaining = integer
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            result -= result // prime
            while remaining % prime == 0:
                remaining //= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        result -= result // remaining
    return result


def linear_conductor_mellin_data(size: int, denominator: int) -> dict[str, object]:
    """Exact finite sum and z=0 residue for a squarefree linear conductor."""
    if size < 2:
        raise ValueError("size must be at least two")
    if denominator < 1 or denominator > size:
        raise ValueError("denominator must lie between one and size")
    mobius_denominator = mobius(denominator)
    if mobius_denominator == 0:
        raise ValueError("denominator must be squarefree")
    ratio = mp.mpf(size) / denominator
    cutoff = size // denominator
    reciprocal_log_sum = mp.fsum(
        mp.mpf(mobius(integer))
        / integer
        * mp.log(ratio / integer)
        for integer in range(1, cutoff + 1)
        if math.gcd(integer, denominator) == 1
    )
    logarithmic_scale = mp.log(size)
    amplitude = (
        mobius_denominator * reciprocal_log_sum / logarithmic_scale
    )
    residue_main_term = (
        mp.mpf(mobius_denominator)
        * denominator
        / euler_totient(denominator)
        / logarithmic_scale
    )
    return {
        "ratio": ratio,
        "cutoff": cutoff,
        "reciprocal_log_sum": reciprocal_log_sum,
        "amplitude": amplitude,
        "zero_residue_main_term": residue_main_term,
        "contour_remainder": amplitude - residue_main_term,
        "endpoint_one_term": cutoff == 1,
    }


def mobius_logarithmic_riesz_sum(argument: mp.mpf) -> mp.mpf:
    """Return sum_{n<=x} mu(n) log(x/n)/n for real x>=1."""
    argument = mp.mpf(argument)
    if argument < 1:
        raise ValueError("argument must be at least one")
    return mp.fsum(
        mp.mpf(mobius(integer))
        / integer
        * mp.log(argument / integer)
        for integer in range(1, int(mp.floor(argument)) + 1)
    )


def coprime_mobius_logarithmic_riesz_sum(
    argument: mp.mpf, modulus: int
) -> mp.mpf:
    """Coprime-restricted logarithmic Mobius Riesz sum T_r(x)."""
    argument = mp.mpf(argument)
    if argument < 1 or modulus < 1:
        raise ValueError("argument and modulus must be positive")
    return mp.fsum(
        mp.mpf(mobius(integer))
        / integer
        * mp.log(argument / integer)
        for integer in range(1, int(mp.floor(argument)) + 1)
        if math.gcd(integer, modulus) == 1
    )


def local_smooth_convolution_riesz_sum(
    argument: mp.mpf, modulus: int
) -> mp.mpf:
    """Expand T_r(x) over integers supported on primes dividing r."""
    argument = mp.mpf(argument)
    if argument < 1 or modulus < 1:
        raise ValueError("argument and modulus must be positive")

    def supported_on_modulus_primes(integer: int) -> bool:
        remaining = integer
        while remaining > 1:
            common = math.gcd(remaining, modulus)
            if common == 1:
                return False
            remaining //= common
        return True

    return mp.fsum(
        mobius_logarithmic_riesz_sum(argument / divisor) / divisor
        for divisor in range(1, int(mp.floor(argument)) + 1)
        if supported_on_modulus_primes(divisor)
    )


def mobius_logarithmic_riesz_moment(
    argument: mp.mpf, power: int
) -> mp.mpf:
    """Return sum_{n<=x} mu(n) log(x/n)^j/n for an integer j>=1."""
    argument = mp.mpf(argument)
    if argument < 1:
        raise ValueError("argument must be at least one")
    if power < 1:
        raise ValueError("power must be positive")
    return mp.fsum(
        mp.mpf(mobius(integer))
        / integer
        * mp.log(argument / integer) ** power
        for integer in range(1, int(mp.floor(argument)) + 1)
    )


def coprime_mobius_logarithmic_riesz_moment(
    argument: mp.mpf, modulus: int, power: int
) -> mp.mpf:
    """Coprime-restricted logarithmic Mobius Riesz moment T_{r,j}(x)."""
    argument = mp.mpf(argument)
    if argument < 1 or modulus < 1:
        raise ValueError("argument and modulus must be positive")
    if power < 1:
        raise ValueError("power must be positive")
    return mp.fsum(
        mp.mpf(mobius(integer))
        / integer
        * mp.log(argument / integer) ** power
        for integer in range(1, int(mp.floor(argument)) + 1)
        if math.gcd(integer, modulus) == 1
    )


def local_smooth_convolution_riesz_moment(
    argument: mp.mpf, modulus: int, power: int
) -> mp.mpf:
    """Expand T_{r,j}(x) over integers supported on primes dividing r."""
    argument = mp.mpf(argument)
    if argument < 1 or modulus < 1:
        raise ValueError("argument and modulus must be positive")
    if power < 1:
        raise ValueError("power must be positive")

    def supported_on_modulus_primes(integer: int) -> bool:
        remaining = integer
        while remaining > 1:
            common = math.gcd(remaining, modulus)
            if common == 1:
                return False
            remaining //= common
        return True

    return mp.fsum(
        mobius_logarithmic_riesz_moment(
            argument / divisor, power
        )
        / divisor
        for divisor in range(1, int(mp.floor(argument)) + 1)
        if supported_on_modulus_primes(divisor)
    )


def endpoint_polynomial_riesz_data(
    polynomial_coefficients: list[mp.mpf],
) -> dict[str, object]:
    """Expand P(1-v) and return its elementary endpoint Riesz norm."""
    if not polynomial_coefficients:
        raise ValueError("polynomial must have at least one coefficient")
    coefficients = [mp.mpf(value) for value in polynomial_coefficients]
    degree = len(coefficients) - 1
    endpoint_coefficients = [mp.mpf("0")] * (degree + 1)
    for exponent, coefficient in enumerate(coefficients):
        for power in range(exponent + 1):
            endpoint_coefficients[power] += (
                coefficient
                * math.comb(exponent, power)
                * (-1) ** power
            )
    tolerance = mp.eps * max(
        1, mp.fsum(abs(value) for value in coefficients)
    )
    if abs(endpoint_coefficients[0]) > tolerance:
        raise ValueError("endpoint polynomial must satisfy P(1)=0")
    endpoint_coefficients[0] = mp.mpf("0")
    riesz_norm = mp.fsum(
        power * abs(endpoint_coefficients[power])
        for power in range(1, degree + 1)
    )
    return {
        "endpoint_coefficients": endpoint_coefficients,
        "riesz_norm": riesz_norm,
    }


def endpoint_direction_riesz_transform(direction_count: int) -> mp.matrix:
    """Map coefficients of u^j(1-u) directions to P(1-v) coefficients."""
    if direction_count < 1:
        raise ValueError("direction_count must be positive")
    transform = mp.matrix(direction_count + 1, direction_count)
    for direction in range(1, direction_count + 1):
        for endpoint_power in range(1, direction + 2):
            transform[endpoint_power - 1, direction - 1] = (
                (-1) ** (endpoint_power - 1)
                * math.comb(direction, endpoint_power - 1)
            )
    return transform


def endpoint_riesz_projection_certificate(
    metric: mp.matrix,
    response: mp.matrix,
    target_response: mp.mpf,
    base_coupling: mp.matrix | None = None,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Coefficient-leverage certificate for a constrained endpoint projection.

    The base polynomial is 1-u.  If base_coupling is omitted, this is the
    minimum-metric correction.  Otherwise it is the full affine constrained
    projection with quadratic coupling h.
    """
    if metric.rows != metric.cols or metric.rows < 1:
        raise ValueError("metric must be a nonempty square matrix")
    dimension = metric.rows
    if response.rows != dimension or response.cols != 1:
        raise ValueError("response must be a compatible column")
    if base_coupling is not None and (
        base_coupling.rows != dimension or base_coupling.cols != 1
    ):
        raise ValueError("base_coupling must be a compatible column")
    if endpoint_weights is None:
        weights = [mp.mpf(power) for power in range(1, dimension + 2)]
    else:
        if len(endpoint_weights) != dimension + 1:
            raise ValueError("endpoint_weights must have direction_count+1 entries")
        weights = [mp.mpf(value) for value in endpoint_weights]
        if any(value <= 0 for value in weights):
            raise ValueError("endpoint weights must be positive")

    metric = mp.matrix(metric)
    response = mp.matrix(response)
    metric_inverse = metric**-1
    capacity = mp.re(
        (response.transpose_conj() * metric_inverse * response)[0, 0]
    )
    if capacity <= 0:
        raise ValueError("response capacity must be positive")
    transform = endpoint_direction_riesz_transform(dimension)
    response_representer = metric_inverse * response
    transformed_response = transform * response_representer
    response_leverage = mp.fsum(
        weights[row] * abs(transformed_response[row])
        for row in range(dimension + 1)
    ) / capacity

    if base_coupling is None:
        coupling_representer = mp.matrix(dimension, 1)
        response_residual = target_response
    else:
        base_coupling = mp.matrix(base_coupling)
        coupling_representer = metric_inverse * base_coupling
        response_residual = target_response + (
            response.transpose_conj() * coupling_representer
        )[0, 0]
    transformed_coupling = transform * coupling_representer
    coupling_leverage = mp.fsum(
        weights[row] * abs(transformed_coupling[row])
        for row in range(dimension + 1)
    )
    alphas = (
        -coupling_representer
        + response_residual / capacity * response_representer
    )
    endpoint_coefficients = transform * alphas
    endpoint_coefficients[0] += 1
    exact_riesz_norm = mp.fsum(
        weights[row] * abs(endpoint_coefficients[row])
        for row in range(dimension + 1)
    )
    triangle_upper_bound = (
        weights[0]
        + coupling_leverage
        + abs(response_residual) * response_leverage
    )

    inverse_endpoint_kernel = (
        transform * metric_inverse * transform.transpose_conj()
    )
    phase_box_majorant = mp.fsum(
        weights[row]
        * weights[column]
        * abs(inverse_endpoint_kernel[row, column])
        for row in range(dimension + 1)
        for column in range(dimension + 1)
    )
    response_leverage_energy_upper = mp.sqrt(
        phase_box_majorant / capacity
    )
    return {
        "transform": transform,
        "endpoint_coefficients": endpoint_coefficients,
        "alphas": alphas,
        "capacity": capacity,
        "response_residual": response_residual,
        "response_leverage": response_leverage,
        "coupling_leverage": coupling_leverage,
        "exact_riesz_norm": exact_riesz_norm,
        "triangle_upper_bound": triangle_upper_bound,
        "inverse_endpoint_kernel": inverse_endpoint_kernel,
        "phase_box_majorant": phase_box_majorant,
        "response_leverage_energy_upper": response_leverage_energy_upper,
        "correction_energy": mp.re(
            (alphas.transpose_conj() * metric * alphas)[0, 0]
        ),
    }


def mobius_endpoint_direction_spatial_gram(
    size: int,
    direction_count: int,
    left_endpoint: int,
    right_endpoint: int,
) -> dict[str, object]:
    """Exact integer-window spatial Gram of Mobius endpoint jets in y."""
    if size < 2:
        raise ValueError("size must be at least two")
    if direction_count < 1:
        raise ValueError("direction_count must be positive")
    if left_endpoint < 0 or right_endpoint <= left_endpoint:
        raise ValueError("endpoints must satisfy 0 <= left < right")
    logarithmic_scale = mp.log(size)
    directions: list[list[mp.mpf]] = []
    slopes: list[mp.mpf] = []
    cumulative_charges: list[list[mp.mpf]] = []
    response = mp.matrix(direction_count, 1)
    for offset in range(direction_count):
        power = offset + 1
        direction = [mp.mpf("0")] * (size + 1)
        for integer in range(1, size + 1):
            coordinate = mp.log(integer) / logarithmic_scale
            direction[integer] = (
                mobius(integer)
                * coordinate**power
                * (1 - coordinate)
            )
        directions.append(direction)
        slopes.append(
            mp.fsum(
                direction[integer] / integer
                for integer in range(1, size + 1)
            )
        )
        response[offset] = mp.fsum(direction[1:])
        convolution = [mp.mpf("0")] * right_endpoint
        for divisor in range(1, size + 1):
            coefficient = direction[divisor]
            if coefficient == 0:
                continue
            for multiple in range(divisor, right_endpoint, divisor):
                convolution[multiple] += coefficient
        cumulative = mp.mpf("0")
        charges = [mp.mpf("0")] * right_endpoint
        for integer in range(1, right_endpoint):
            cumulative += convolution[integer]
            charges[integer] = cumulative
        cumulative_charges.append(charges)

    metric = mp.matrix(direction_count, direction_count)
    for row in range(direction_count):
        for column in range(direction_count):
            value = (
                slopes[row] * mp.conj(slopes[column])
                if left_endpoint == 0
                else mp.mpf("0")
            )
            for integer in range(max(1, left_endpoint), right_endpoint):
                left_intercept = -cumulative_charges[row][integer]
                right_intercept = -cumulative_charges[column][integer]
                logarithmic_width = mp.log(
                    mp.mpf(integer + 1) / integer
                )
                reciprocal_drop = (
                    mp.mpf(1) / integer
                    - mp.mpf(1) / (integer + 1)
                )
                value += (
                    slopes[row] * mp.conj(slopes[column])
                    + (
                        slopes[row] * mp.conj(right_intercept)
                        + left_intercept * mp.conj(slopes[column])
                    )
                    * logarithmic_width
                    + left_intercept
                    * mp.conj(right_intercept)
                    * reciprocal_drop
                )
            metric[row, column] = value
    return {
        "metric": metric,
        "response": response,
        "directions": directions,
        "slopes": slopes,
        "cumulative_charges": cumulative_charges,
        "left_endpoint": left_endpoint,
        "right_endpoint": right_endpoint,
    }


def mobius_endpoint_direction_local_gram(
    size: int, direction_count: int
) -> dict[str, object]:
    """Exact y<=N Gram and boundary responses of Mobius endpoint jets."""
    return mobius_endpoint_direction_spatial_gram(
        size, direction_count, 0, size
    )


def mobius_endpoint_direction_periodic_gram(
    size: int, direction_count: int
) -> dict[str, object]:
    """Exact one-period Parseval Gram of Mobius endpoint jet fields."""
    spatial_data = mobius_endpoint_direction_spatial_gram(
        size, direction_count, 0, 1
    )
    directions = spatial_data["directions"]
    response = spatial_data["response"]
    conductor_amplitudes = mp.matrix(size, direction_count)
    for denominator in range(1, size + 1):
        for column in range(direction_count):
            conductor_amplitudes[denominator - 1, column] = mp.fsum(
                directions[column][multiple] * denominator / multiple
                for multiple in range(denominator, size + 1, denominator)
            )
    metric = response * response.transpose_conj() / 4
    for denominator in range(1, size + 1):
        density = reduced_denominator_density(denominator)
        for row in range(direction_count):
            for column in range(direction_count):
                metric[row, column] += (
                    density
                    * conductor_amplitudes[denominator - 1, row]
                    * mp.conj(
                        conductor_amplitudes[denominator - 1, column]
                    )
                    / 12
                )
    return {
        "metric": metric,
        "response": response,
        "directions": directions,
        "conductor_amplitudes": conductor_amplitudes,
    }


def nyman_endpoint_spatial_far_certificate(
    size: int,
    direction_count: int,
    far_majorant_constant: mp.mpf = mp.mpf("1"),
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Finite leverage certificate using y<N^2 plus a periodic far majorant."""
    far_majorant_constant = mp.mpf(far_majorant_constant)
    if far_majorant_constant <= 0:
        raise ValueError("far_majorant_constant must be positive")
    spatial = mobius_endpoint_direction_spatial_gram(
        size, direction_count, 0, size**2
    )
    periodic = mobius_endpoint_direction_periodic_gram(
        size, direction_count
    )
    far_majorant = (
        far_majorant_constant / size**2 * periodic["metric"]
    )
    localized = localized_endpoint_riesz_leverage_certificate(
        spatial["metric"],
        far_majorant,
        spatial["response"],
        endpoint_weights,
    )
    return {
        "spatial_metric": spatial["metric"],
        "periodic_metric": periodic["metric"],
        "far_majorant": far_majorant,
        "response": spatial["response"],
        "localized": localized,
        "far_majorant_constant": far_majorant_constant,
    }


def endpoint_quadratic_mass(
    direction_count: int,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Quadratic endpoint mass E^* diag(c_l^2) E for jet directions."""
    if direction_count < 1:
        raise ValueError("direction_count must be positive")
    if endpoint_weights is None:
        weights = [mp.mpf(power) for power in range(1, direction_count + 2)]
    else:
        if len(endpoint_weights) != direction_count + 1:
            raise ValueError("endpoint_weights must have direction_count+1 entries")
        weights = [mp.mpf(value) for value in endpoint_weights]
        if any(value <= 0 for value in weights):
            raise ValueError("endpoint weights must be positive")
    transform = endpoint_direction_riesz_transform(direction_count)
    weight_square = mp.diag([value**2 for value in weights])
    mass = transform.transpose_conj() * weight_square * transform
    return {
        "mass": mass,
        "transform": transform,
        "weights": weights,
    }


def endpoint_polarization_alignment_certificate(
    metric: mp.matrix,
    response: mp.matrix,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Feshbach misalignment of global and endpoint canonical representatives."""
    if metric.rows != metric.cols or metric.rows < 1:
        raise ValueError("metric must be a nonempty square matrix")
    dimension = metric.rows
    if response.rows != dimension or response.cols != 1:
        raise ValueError("response must be a compatible column")
    if max(abs(response[index]) for index in range(dimension)) == 0:
        raise ValueError("response must be nonzero")
    metric = mp.matrix(metric)
    response = mp.matrix(response)
    endpoint_data = endpoint_quadratic_mass(
        dimension, endpoint_weights
    )
    endpoint_mass = endpoint_data["mass"]
    transform = endpoint_data["transform"]
    weights = endpoint_data["weights"]
    metric_inverse = metric**-1
    endpoint_inverse = endpoint_mass**-1
    metric_capacity = mp.re(
        (response.transpose_conj() * metric_inverse * response)[0, 0]
    )
    endpoint_capacity = mp.re(
        (response.transpose_conj() * endpoint_inverse * response)[0, 0]
    )
    if metric_capacity <= 0 or endpoint_capacity <= 0:
        raise ValueError("both response capacities must be positive")
    metric_representative = metric_inverse * response / metric_capacity
    endpoint_representative = (
        endpoint_inverse * response / endpoint_capacity
    )
    difference = metric_representative - endpoint_representative
    endpoint_minimum = 1 / endpoint_capacity
    endpoint_norm = mp.re(
        (
            metric_representative.transpose_conj()
            * endpoint_mass
            * metric_representative
        )[0, 0]
    )
    endpoint_excess = mp.re(
        (difference.transpose_conj() * endpoint_mass * difference)[0, 0]
    )
    dimensionless_excess = endpoint_capacity * endpoint_excess
    alignment_cosine_squared = 1 / (
        endpoint_capacity * endpoint_norm
    )
    response_line_energy = mp.re(
        (
            endpoint_representative.transpose_conj()
            * metric
            * endpoint_representative
        )[0, 0]
    )

    if dimension == 1:
        null_basis = mp.matrix(1, 0)
        null_metric = mp.matrix(0, 0)
        null_coupling = mp.matrix(0, 1)
        null_endpoint_mass = mp.matrix(0, 0)
        null_generalized_eigenvalues = mp.matrix(0, 1)
        null_spectral_forcing = mp.matrix(0, 1)
        null_forcing_dual_mass = mp.mpf("0")
        null_coercivity = mp.inf
        feshbach_excess_upper = mp.mpf("0")
        null_green_first_moment = mp.mpf("0")
        feshbach_first_moment_upper = mp.mpf("0")
        effective_null_slope = mp.inf
        shorted_null_metric = mp.matrix(0, 0)
        shorted_generalized_eigenvalues = mp.matrix(0, 1)
        shorted_spectral_forcing = mp.matrix(0, 1)
        shorted_forcing_green_mass = mp.mpf("0")
        shorted_second_green_mass = mp.mpf("0")
        shorted_coercivity = mp.inf
        shorted_excess_prediction = mp.mpf("0")
        shorted_excess_upper = mp.mpf("0")
        null_endpoint_contributions: list[mp.mpf] = []
        feshbach_shift = mp.matrix([mp.mpf("0")])
        feshbach_endpoint_excess = mp.mpf("0")
    else:
        pivot = max(
            range(dimension), key=lambda index: abs(response[index])
        )
        free_indices = [
            index for index in range(dimension) if index != pivot
        ]
        null_basis = mp.matrix(dimension, dimension - 1)
        for column, free_index in enumerate(free_indices):
            null_basis[free_index, column] = 1
            null_basis[pivot, column] = (
                -mp.conj(response[free_index])
                / mp.conj(response[pivot])
            )
        null_metric = (
            null_basis.transpose_conj() * metric * null_basis
        )
        null_coupling = (
            null_basis.transpose_conj()
            * metric
            * endpoint_representative
        )
        feshbach_shift = (
            -null_basis * (null_metric**-1) * null_coupling
        )
        feshbach_endpoint_excess = mp.re(
            (
                feshbach_shift.transpose_conj()
                * endpoint_mass
                * feshbach_shift
            )[0, 0]
        )
        null_endpoint_mass = (
            null_basis.transpose_conj()
            * endpoint_mass
            * null_basis
        )
        null_endpoint_cholesky = mp.cholesky(null_endpoint_mass)
        inverse_null_endpoint_cholesky = (
            null_endpoint_cholesky**-1
        )
        null_compact = (
            inverse_null_endpoint_cholesky
            * null_metric
            * inverse_null_endpoint_cholesky.transpose_conj()
        )
        (
            null_generalized_eigenvalues,
            null_generalized_eigenvectors,
        ) = mp.eigsy(null_compact)
        transformed_null_coupling = (
            inverse_null_endpoint_cholesky * null_coupling
        )
        null_spectral_forcing = (
            null_generalized_eigenvectors.transpose_conj()
            * transformed_null_coupling
        )
        null_forcing_dual_mass = mp.fsum(
            abs(null_spectral_forcing[index]) ** 2
            for index in range(dimension - 1)
        )
        null_coercivity = mp.re(null_generalized_eigenvalues[0])
        if null_coercivity <= 0:
            raise ValueError("null metric must be endpoint-coercive")
        feshbach_excess_upper = (
            endpoint_capacity
            * null_forcing_dual_mass
            / null_coercivity**2
        )
        null_green_first_moment = mp.fsum(
            abs(null_spectral_forcing[index]) ** 2
            / null_generalized_eigenvalues[index]
            for index in range(dimension - 1)
        )
        feshbach_first_moment_upper = (
            endpoint_capacity
            * null_green_first_moment
            / null_coercivity
        )
        spectral_endpoint_excess = mp.fsum(
            abs(null_spectral_forcing[index]) ** 2
            / null_generalized_eigenvalues[index] ** 2
            for index in range(dimension - 1)
        )
        null_endpoint_contributions = [
            (
                abs(null_spectral_forcing[index]) ** 2
                / null_generalized_eigenvalues[index] ** 2
            )
            / spectral_endpoint_excess
            if spectral_endpoint_excess > 0
            else mp.mpf("0")
            for index in range(dimension - 1)
        ]
        effective_null_slope = (
            null_green_first_moment / spectral_endpoint_excess
            if spectral_endpoint_excess > 0
            else mp.inf
        )
        shorted_null_metric = (
            null_metric
            - null_coupling
            * null_coupling.transpose_conj()
            / response_line_energy
        )
        shorted_compact = (
            inverse_null_endpoint_cholesky
            * shorted_null_metric
            * inverse_null_endpoint_cholesky.transpose_conj()
        )
        (
            shorted_generalized_eigenvalues,
            shorted_generalized_eigenvectors,
        ) = mp.eigsy(shorted_compact)
        shorted_spectral_forcing = (
            shorted_generalized_eigenvectors.transpose_conj()
            * transformed_null_coupling
        )
        shorted_forcing_green_mass = mp.fsum(
            abs(shorted_spectral_forcing[index]) ** 2
            / shorted_generalized_eigenvalues[index]
            for index in range(dimension - 1)
        )
        shorted_second_green_mass = mp.fsum(
            abs(shorted_spectral_forcing[index]) ** 2
            / shorted_generalized_eigenvalues[index] ** 2
            for index in range(dimension - 1)
        )
        shorted_coercivity = mp.re(
            shorted_generalized_eigenvalues[0]
        )
        if shorted_coercivity <= 0:
            raise ValueError("shorted null metric must be endpoint-coercive")
        shorted_normalization = response_line_energy * metric_capacity
        shorted_excess_prediction = (
            endpoint_capacity
            * shorted_second_green_mass
            / shorted_normalization**2
        )
        shorted_excess_upper = (
            endpoint_capacity
            * shorted_forcing_green_mass
            / (
                shorted_coercivity
                * shorted_normalization**2
            )
        )
    transformed_metric_representative = transform * metric_representative
    exact_response_leverage_l1 = mp.fsum(
        weights[row] * abs(transformed_metric_representative[row])
        for row in range(dimension + 1)
    )
    response_leverage_l1_upper = mp.sqrt(
        (dimension + 1) * endpoint_norm
    )
    return {
        "endpoint_mass": endpoint_mass,
        "transform": transform,
        "weights": weights,
        "metric_capacity": metric_capacity,
        "endpoint_capacity": endpoint_capacity,
        "metric_representative": metric_representative,
        "endpoint_representative": endpoint_representative,
        "difference": difference,
        "endpoint_minimum": endpoint_minimum,
        "endpoint_norm": endpoint_norm,
        "endpoint_excess": endpoint_excess,
        "dimensionless_excess": dimensionless_excess,
        "alignment_cosine_squared": alignment_cosine_squared,
        "response_line_energy": response_line_energy,
        "null_basis": null_basis,
        "null_metric": null_metric,
        "null_coupling": null_coupling,
        "null_endpoint_mass": null_endpoint_mass,
        "null_generalized_eigenvalues": null_generalized_eigenvalues,
        "null_spectral_forcing": null_spectral_forcing,
        "null_forcing_dual_mass": null_forcing_dual_mass,
        "null_coercivity": null_coercivity,
        "feshbach_excess_upper": feshbach_excess_upper,
        "null_green_first_moment": null_green_first_moment,
        "feshbach_first_moment_upper": feshbach_first_moment_upper,
        "effective_null_slope": effective_null_slope,
        "shorted_null_metric": shorted_null_metric,
        "shorted_generalized_eigenvalues": (
            shorted_generalized_eigenvalues
        ),
        "shorted_spectral_forcing": shorted_spectral_forcing,
        "shorted_forcing_green_mass": shorted_forcing_green_mass,
        "shorted_second_green_mass": shorted_second_green_mass,
        "shorted_coercivity": shorted_coercivity,
        "shorted_excess_prediction": shorted_excess_prediction,
        "shorted_excess_upper": shorted_excess_upper,
        "null_endpoint_contributions": null_endpoint_contributions,
        "feshbach_shift": feshbach_shift,
        "feshbach_endpoint_excess": feshbach_endpoint_excess,
        "exact_response_leverage_l1": exact_response_leverage_l1,
        "response_leverage_l1_upper": response_leverage_l1_upper,
    }


def endpoint_transversal_hodge_shorting(
    metric: mp.matrix,
    response: mp.matrix,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Extract the maximal pure endpoint-transversal block contained in W."""
    base = endpoint_polarization_alignment_certificate(
        metric, response, endpoint_weights
    )
    dimension = metric.rows
    identity = mp.eye(dimension)
    homogeneous_projection = (
        identity
        - base["endpoint_representative"] * response.transpose_conj()
    )
    completion_metric = (
        homogeneous_projection.transpose_conj()
        * base["endpoint_mass"]
        * homogeneous_projection
    )
    if dimension == 1:
        maximal_strength = mp.inf
        residual_metric = mp.matrix(metric)
    else:
        maximal_strength = base["shorted_coercivity"]
        residual_metric = (
            mp.matrix(metric) - maximal_strength * completion_metric
        )
    return {
        "base": base,
        "homogeneous_projection": homogeneous_projection,
        "completion_metric": completion_metric,
        "maximal_strength": maximal_strength,
        "residual_metric": residual_metric,
    }


def endpoint_spatial_block_wedge_certificate(
    size: int,
    direction_count: int,
    left_endpoint: int,
    right_endpoint: int,
    block_endpoints: list[int],
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Finite block-integral wedge frame below the spatial Schur short."""
    if len(block_endpoints) < 3:
        raise ValueError("at least two spatial blocks are required")
    if (
        block_endpoints[0] != left_endpoint
        or block_endpoints[-1] != right_endpoint
    ):
        raise ValueError("block endpoints must span the spatial window")
    if any(
        left >= right
        for left, right in zip(block_endpoints, block_endpoints[1:])
    ):
        raise ValueError("block endpoints must be strictly increasing")
    spatial_data = mobius_endpoint_direction_spatial_gram(
        size, direction_count, left_endpoint, right_endpoint
    )
    alignment = endpoint_polarization_alignment_certificate(
        spatial_data["metric"],
        spatial_data["response"],
        endpoint_weights,
    )
    slopes = spatial_data["slopes"]
    cumulative_charges = spatial_data["cumulative_charges"]
    null_basis = alignment["null_basis"]
    endpoint_representative = alignment["endpoint_representative"]

    block_measures: list[mp.mpf] = []
    block_direction_integrals: list[mp.matrix] = []
    block_response_integrals: list[mp.mpf] = []
    block_null_integrals: list[mp.matrix] = []
    projected_metric = mp.matrix(direction_count, direction_count)
    for block_left, block_right in zip(
        block_endpoints, block_endpoints[1:]
    ):
        direction_integral = mp.matrix(direction_count, 1)
        if block_left == 0:
            for row in range(direction_count):
                direction_integral[row] += slopes[row]
        for integer in range(max(1, block_left), block_right):
            logarithmic_width = mp.log(
                mp.mpf(integer + 1) / integer
            )
            for row in range(direction_count):
                direction_integral[row] += (
                    slopes[row]
                    - cumulative_charges[row][integer]
                    * logarithmic_width
                )
        block_measure = mp.mpf(block_right - block_left)
        block_measures.append(block_measure)
        block_direction_integrals.append(direction_integral)
        projected_metric += (
            direction_integral
            * direction_integral.transpose_conj()
            / block_measure
        )
        block_response_integrals.append(
            (
                endpoint_representative.transpose_conj()
                * direction_integral
            )[0, 0]
        )
        block_null_integrals.append(
            null_basis.transpose_conj() * direction_integral
        )

    null_dimension = max(0, direction_count - 1)
    wedge_lower_metric = mp.matrix(null_dimension, null_dimension)
    wedge_vectors: list[mp.matrix] = []
    wedge_pairs: list[tuple[int, int]] = []
    wedge_pair_count = (
        len(block_measures) * (len(block_measures) - 1) // 2
    )
    wedge_vectors_materialized = wedge_pair_count <= 4096
    projected_remainder_metric = (
        spatial_data["metric"] - projected_metric
    )
    unit_cell_partition = all(
        right - left == 1
        for left, right in zip(block_endpoints, block_endpoints[1:])
    )
    if unit_cell_partition:
        unit_cell_variance_metric = mp.matrix(
            direction_count, direction_count
        )
        unit_cell_poincare_majorant = mp.matrix(
            direction_count, direction_count
        )
        for integer in range(max(1, left_endpoint), right_endpoint):
            charge_vector = mp.matrix(
                [
                    cumulative_charges[row][integer]
                    for row in range(direction_count)
                ]
            )
            logarithmic_width = mp.log(
                mp.mpf(integer + 1) / integer
            )
            variance_coefficient = (
                mp.mpf(1) / integer
                - mp.mpf(1) / (integer + 1)
                - logarithmic_width**2
            )
            poincare_coefficient = (
                mp.mpf(1) / integer**3
                - mp.mpf(1) / (integer + 1) ** 3
            ) / (3 * mp.pi**2)
            charge_outer = (
                charge_vector * charge_vector.transpose_conj()
            )
            unit_cell_variance_metric += (
                variance_coefficient * charge_outer
            )
            unit_cell_poincare_majorant += (
                poincare_coefficient * charge_outer
            )
    else:
        unit_cell_variance_metric = None
        unit_cell_poincare_majorant = None
    if null_dimension > 0:
        discrete_response_energy = mp.fsum(
            abs(block_response_integrals[index]) ** 2
            / block_measures[index]
            for index in range(len(block_measures))
        )
        discrete_null_metric = mp.matrix(
            null_dimension, null_dimension
        )
        discrete_null_coupling = mp.matrix(null_dimension, 1)
        for index in range(len(block_measures)):
            discrete_null_metric += (
                block_null_integrals[index]
                * block_null_integrals[index].transpose_conj()
                / block_measures[index]
            )
            discrete_null_coupling += (
                block_null_integrals[index]
                * mp.conj(block_response_integrals[index])
                / block_measures[index]
            )
        if discrete_response_energy <= 0:
            raise ValueError(
                "block projection has zero response-line energy"
            )
        wedge_lower_metric = (
            discrete_response_energy * discrete_null_metric
            - discrete_null_coupling
            * discrete_null_coupling.transpose_conj()
        ) / discrete_response_energy
        if wedge_vectors_materialized:
            for left_index in range(len(block_measures)):
                for right_index in range(
                    left_index + 1, len(block_measures)
                ):
                    wedge_vectors.append(
                        block_response_integrals[left_index]
                        * block_null_integrals[right_index]
                        / mp.sqrt(
                            block_measures[left_index]
                            * block_measures[right_index]
                        )
                        - block_response_integrals[right_index]
                        * block_null_integrals[left_index]
                        / mp.sqrt(
                            block_measures[left_index]
                            * block_measures[right_index]
                        )
                    )
                    wedge_pairs.append((left_index, right_index))
        null_endpoint_cholesky = mp.cholesky(
            alignment["null_endpoint_mass"]
        )
        inverse_null_endpoint_cholesky = (
            null_endpoint_cholesky**-1
        )

        def generalized_compact(metric: mp.matrix) -> mp.matrix:
            return (
                inverse_null_endpoint_cholesky
                * metric
                * inverse_null_endpoint_cholesky.transpose_conj()
            )

        wedge_compact = generalized_compact(wedge_lower_metric)
        wedge_eigenvalues = mp.eigsy(
            wedge_compact, eigvals_only=True
        )
        wedge_lower_coercivity = max(
            mp.mpf("0"), mp.re(wedge_eigenvalues[0])
        )
        wedge_remainder_metric = (
            alignment["shorted_null_metric"] - wedge_lower_metric
        )
        wedge_remainder_eigenvalues = mp.eigsy(
            generalized_compact(wedge_remainder_metric),
            eigvals_only=True,
        )
        wedge_remainder_coercivity = max(
            mp.mpf("0"), mp.re(wedge_remainder_eigenvalues[0])
        )
        captured_coercivity_ratio = (
            wedge_lower_coercivity / alignment["shorted_coercivity"]
        )
        response_energy_capture_ratio = (
            discrete_response_energy
            / alignment["response_line_energy"]
        )
        wedge_normalized_determinant = max(
            mp.mpf("0"), mp.re(mp.det(wedge_compact))
        )
        wedge_normalized_trace = mp.fsum(
            mp.re(wedge_compact[index, index])
            for index in range(null_dimension)
        )
        if null_dimension == 1:
            determinant_trace_coercivity_lower = (
                wedge_normalized_determinant
            )
        elif wedge_normalized_trace > 0:
            determinant_trace_coercivity_lower = (
                wedge_normalized_determinant
                / (
                    wedge_normalized_trace / (null_dimension - 1)
                ) ** (null_dimension - 1)
            )
        else:
            determinant_trace_coercivity_lower = mp.mpf("0")
        determinant_trace_capture_ratio = (
            determinant_trace_coercivity_lower
            / alignment["shorted_coercivity"]
        )
    else:
        discrete_response_energy = mp.mpf("0")
        discrete_null_metric = mp.matrix(0, 0)
        discrete_null_coupling = mp.matrix(0, 1)
        wedge_eigenvalues = mp.matrix(0, 1)
        wedge_lower_coercivity = mp.inf
        wedge_remainder_metric = mp.matrix(0, 0)
        wedge_remainder_eigenvalues = mp.matrix(0, 1)
        wedge_remainder_coercivity = mp.inf
        captured_coercivity_ratio = mp.mpf("1")
        response_energy_capture_ratio = mp.mpf("1")
        wedge_compact = mp.matrix(0, 0)
        wedge_normalized_determinant = mp.mpf("1")
        wedge_normalized_trace = mp.mpf("0")
        determinant_trace_coercivity_lower = mp.inf
        determinant_trace_capture_ratio = mp.mpf("1")
    return {
        "spatial_data": spatial_data,
        "alignment_certificate": alignment,
        "block_endpoints": list(block_endpoints),
        "block_measures": block_measures,
        "block_direction_integrals": block_direction_integrals,
        "block_response_integrals": block_response_integrals,
        "block_null_integrals": block_null_integrals,
        "projected_metric": projected_metric,
        "projected_remainder_metric": projected_remainder_metric,
        "unit_cell_partition": unit_cell_partition,
        "unit_cell_variance_metric": unit_cell_variance_metric,
        "unit_cell_poincare_majorant": unit_cell_poincare_majorant,
        "wedge_pairs": wedge_pairs,
        "wedge_vectors": wedge_vectors,
        "wedge_pair_count": wedge_pair_count,
        "wedge_vectors_materialized": wedge_vectors_materialized,
        "discrete_response_energy": discrete_response_energy,
        "response_energy_capture_ratio": response_energy_capture_ratio,
        "discrete_null_metric": discrete_null_metric,
        "discrete_null_coupling": discrete_null_coupling,
        "wedge_lower_metric": wedge_lower_metric,
        "wedge_normalized_compact": wedge_compact,
        "wedge_generalized_eigenvalues": wedge_eigenvalues,
        "wedge_lower_coercivity": wedge_lower_coercivity,
        "wedge_remainder_metric": wedge_remainder_metric,
        "wedge_remainder_generalized_eigenvalues": (
            wedge_remainder_eigenvalues
        ),
        "wedge_remainder_coercivity": wedge_remainder_coercivity,
        "captured_coercivity_ratio": captured_coercivity_ratio,
        "wedge_normalized_determinant": wedge_normalized_determinant,
        "wedge_normalized_trace": wedge_normalized_trace,
        "determinant_trace_coercivity_lower": (
            determinant_trace_coercivity_lower
        ),
        "determinant_trace_capture_ratio": (
            determinant_trace_capture_ratio
        ),
    }


def mobius_cell_vandermonde_recovery_certificate(
    size: int,
    direction_count: int,
    squarefree_nodes: list[int] | None = None,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Recover fixed Mobius Vandermonde rows from initial unit-cell means."""
    if size < 3:
        raise ValueError("size must be at least three")
    if direction_count < 1:
        raise ValueError("direction_count must be positive")
    if squarefree_nodes is None:
        squarefree_nodes = []
        candidate = 2
        while len(squarefree_nodes) < direction_count:
            if mobius(candidate) != 0:
                squarefree_nodes.append(candidate)
            candidate += 1
    if len(squarefree_nodes) != direction_count:
        raise ValueError("one squarefree node per direction is required")
    if len(set(squarefree_nodes)) != direction_count:
        raise ValueError("squarefree nodes must be distinct")
    if any(
        node < 2 or node >= size or mobius(node) == 0
        for node in squarefree_nodes
    ):
        raise ValueError(
            "nodes must be squarefree integers between 2 and size-1"
        )
    maximal_node = max(squarefree_nodes)
    prefix_right_endpoint = maximal_node + 1
    prefix = endpoint_spatial_block_wedge_certificate(
        size,
        direction_count,
        0,
        prefix_right_endpoint,
        list(range(prefix_right_endpoint + 1)),
        endpoint_weights,
    )
    cell_matrix = mp.matrix(
        prefix_right_endpoint, direction_count
    )
    for row, direction_integral in enumerate(
        prefix["block_direction_integrals"]
    ):
        for column in range(direction_count):
            cell_matrix[row, column] = direction_integral[column]

    def charge_increment_coefficients(integer: int) -> mp.matrix:
        coefficients = mp.matrix(prefix_right_endpoint, 1)
        logarithmic_width = mp.log(
            mp.mpf(integer + 1) / integer
        )
        if integer == 1:
            coefficients[0] = 1 / logarithmic_width
            coefficients[1] = -1 / logarithmic_width
            return coefficients
        previous_width = mp.log(mp.mpf(integer) / (integer - 1))
        coefficients[0] = 1 / logarithmic_width - 1 / previous_width
        coefficients[integer - 1] = 1 / previous_width
        coefficients[integer] = -1 / logarithmic_width
        return coefficients

    recovery_operator = mp.matrix(
        direction_count, prefix_right_endpoint
    )
    for row, node in enumerate(squarefree_nodes):
        for divisor in range(1, node + 1):
            if node % divisor != 0:
                continue
            inversion_weight = mobius(node // divisor)
            if inversion_weight == 0:
                continue
            increment_coefficients = charge_increment_coefficients(
                divisor
            )
            for column in range(prefix_right_endpoint):
                recovery_operator[row, column] += (
                    inversion_weight * increment_coefficients[column]
                )
    recovered_vandermonde = recovery_operator * cell_matrix
    expected_vandermonde = mp.matrix(
        direction_count, direction_count
    )
    logarithmic_scale = mp.log(size)
    for row, node in enumerate(squarefree_nodes):
        coordinate = mp.log(node) / logarithmic_scale
        for column in range(direction_count):
            expected_vandermonde[row, column] = (
                mobius(node)
                * (1 - coordinate)
                * coordinate ** (column + 1)
            )
    vandermonde_gram = (
        recovered_vandermonde.transpose_conj()
        * recovered_vandermonde
    )
    vandermonde_eigenvalues = mp.eigsy(
        vandermonde_gram, eigvals_only=True
    )
    recovery_gram = (
        recovery_operator * recovery_operator.transpose_conj()
    )
    recovery_eigenvalues = mp.eigsy(
        recovery_gram, eigvals_only=True
    )
    recovery_operator_norm_squared = mp.re(
        recovery_eigenvalues[recovery_eigenvalues.rows - 1]
    )
    euclidean_gram_lower = (
        mp.re(vandermonde_eigenvalues[0])
        / recovery_operator_norm_squared
    )
    endpoint_eigenvalues = mp.eigsy(
        prefix["alignment_certificate"]["endpoint_mass"],
        eigvals_only=True,
    )
    endpoint_mass_maximum = mp.re(
        endpoint_eigenvalues[endpoint_eigenvalues.rows - 1]
    )
    endpoint_coercivity_lower = (
        euclidean_gram_lower / endpoint_mass_maximum
    )
    fixed_node_vandermonde = mp.matrix(
        direction_count, direction_count
    )
    for row, node in enumerate(squarefree_nodes):
        node_logarithm = mp.log(node)
        for column in range(direction_count):
            fixed_node_vandermonde[row, column] = (
                mobius(node) * node_logarithm ** (column + 1)
            )
    fixed_node_gram_eigenvalues = mp.eigsy(
        fixed_node_vandermonde.transpose_conj()
        * fixed_node_vandermonde,
        eigvals_only=True,
    )
    fixed_node_asymptotic_constant = (
        mp.re(fixed_node_gram_eigenvalues[0])
        / (
            4
            * recovery_operator_norm_squared
            * endpoint_mass_maximum
        )
    )
    fixed_node_asymptotic_lower = (
        fixed_node_asymptotic_constant
        / logarithmic_scale ** (2 * direction_count)
    )
    fixed_node_asymptotic_valid = (
        logarithmic_scale
        >= 2 * max(mp.log(node) for node in squarefree_nodes)
    )
    maximal_node_width = mp.log(
        mp.mpf(maximal_node + 1) / maximal_node
    )
    sparse_recovery_node_upper = (
        direction_count
        * maximal_node_width**2
        * (mp.log(maximal_node) / logarithmic_scale)
        ** (2 * direction_count)
        / endpoint_mass_maximum
    )
    sparse_recovery_universal_upper = (
        direction_count
        * (mp.mpf(direction_count) / mp.e)
        ** (2 * direction_count)
        / (
            endpoint_mass_maximum
            * logarithmic_scale ** (2 * direction_count)
        )
    )
    return {
        "size": size,
        "direction_count": direction_count,
        "squarefree_nodes": list(squarefree_nodes),
        "prefix_certificate": prefix,
        "cell_matrix": cell_matrix,
        "recovery_operator": recovery_operator,
        "recovered_vandermonde": recovered_vandermonde,
        "expected_vandermonde": expected_vandermonde,
        "vandermonde_gram_eigenvalues": vandermonde_eigenvalues,
        "recovery_operator_norm_squared": (
            recovery_operator_norm_squared
        ),
        "euclidean_gram_lower": euclidean_gram_lower,
        "endpoint_mass_maximum": endpoint_mass_maximum,
        "endpoint_coercivity_lower": endpoint_coercivity_lower,
        "fixed_node_vandermonde": fixed_node_vandermonde,
        "fixed_node_asymptotic_constant": (
            fixed_node_asymptotic_constant
        ),
        "fixed_node_asymptotic_lower": fixed_node_asymptotic_lower,
        "fixed_node_asymptotic_valid": fixed_node_asymptotic_valid,
        "sparse_recovery_node_upper": sparse_recovery_node_upper,
        "sparse_recovery_universal_upper": (
            sparse_recovery_universal_upper
        ),
    }


def mobius_sparse_recovery_search(
    size: int,
    direction_count: int,
    maximal_node: int,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Search finite squarefree node sets for the strongest sparse bound."""
    maximal_node = min(maximal_node, size - 1)
    candidates = [
        node
        for node in range(2, maximal_node + 1)
        if mobius(node) != 0
    ]
    if len(candidates) < direction_count:
        raise ValueError("not enough squarefree nodes in the search range")
    best_certificate = None
    certificate_count = 0
    for nodes in itertools.combinations(candidates, direction_count):
        certificate = mobius_cell_vandermonde_recovery_certificate(
            size,
            direction_count,
            list(nodes),
            endpoint_weights,
        )
        certificate_count += 1
        if (
            best_certificate is None
            or certificate["endpoint_coercivity_lower"]
            > best_certificate["endpoint_coercivity_lower"]
        ):
            best_certificate = certificate
    return {
        "size": size,
        "direction_count": direction_count,
        "maximal_node": maximal_node,
        "candidates": candidates,
        "certificate_count": certificate_count,
        "best_certificate": best_certificate,
    }


def endpoint_transversal_hodge_completion(
    metric: mp.matrix,
    response: mp.matrix,
    strength: mp.mpf,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Add endpoint polarization only on ker(D*) and track Feshbach decay."""
    strength = mp.mpf(strength)
    if strength < 0:
        raise ValueError("strength must be nonnegative")
    base = endpoint_polarization_alignment_certificate(
        metric, response, endpoint_weights
    )
    dimension = metric.rows
    identity = mp.eye(dimension)
    homogeneous_projection = (
        identity
        - base["endpoint_representative"] * response.transpose_conj()
    )
    completion_metric = (
        homogeneous_projection.transpose_conj()
        * base["endpoint_mass"]
        * homogeneous_projection
    )
    completed_metric = mp.matrix(metric) + strength * completion_metric
    completed = endpoint_polarization_alignment_certificate(
        completed_metric, response, endpoint_weights
    )
    base_inverse_capacity = 1 / base["metric_capacity"]
    completed_inverse_capacity = 1 / completed["metric_capacity"]
    if dimension == 1:
        predicted_excess = mp.mpf("0")
        predicted_completed_inverse_capacity = base_inverse_capacity
    else:
        predicted_excess = base["endpoint_capacity"] * mp.fsum(
            abs(base["null_spectral_forcing"][index]) ** 2
            / (base["null_generalized_eigenvalues"][index] + strength) ** 2
            for index in range(dimension - 1)
        )
        predicted_completed_inverse_capacity = (
            base["response_line_energy"]
            - mp.fsum(
                abs(base["null_spectral_forcing"][index]) ** 2
                / (
                    base["null_generalized_eigenvalues"][index]
                    + strength
                )
                for index in range(dimension - 1)
            )
        )
    if strength == 0:
        capacity_secant_susceptibility = (
            base["dimensionless_excess"]
            / base["endpoint_capacity"]
        )
    else:
        capacity_secant_susceptibility = (
            completed_inverse_capacity - base_inverse_capacity
        ) / strength
    susceptibility_excess_lower = (
        base["endpoint_capacity"]
        * capacity_secant_susceptibility
    )
    if dimension == 1:
        susceptibility_excess_upper = mp.mpf("0")
        susceptibility_factor = mp.mpf("1")
    else:
        susceptibility_factor = (
            1 + strength / base["null_coercivity"]
        )
        susceptibility_excess_upper = (
            susceptibility_factor * susceptibility_excess_lower
        )
    adapted_basis = mp.matrix(dimension, dimension)
    for row in range(dimension):
        adapted_basis[row, 0] = base["endpoint_representative"][row]
    for column in range(1, dimension):
        for row in range(dimension):
            adapted_basis[row, column] = base["null_basis"][
                row, column - 1
            ]
    adapted_base_metric = (
        adapted_basis.transpose_conj()
        * mp.matrix(metric)
        * adapted_basis
    )
    adapted_completed_metric = (
        adapted_basis.transpose_conj()
        * completed_metric
        * adapted_basis
    )
    if dimension == 1:
        determinant_base_inverse_capacity = mp.re(
            adapted_base_metric[0, 0]
        )
        determinant_completed_inverse_capacity = mp.re(
            adapted_completed_metric[0, 0]
        )
    else:
        completed_null_metric = (
            base["null_metric"]
            + strength * base["null_endpoint_mass"]
        )
        determinant_base_inverse_capacity = mp.re(
            mp.det(adapted_base_metric) / mp.det(base["null_metric"])
        )
        determinant_completed_inverse_capacity = mp.re(
            mp.det(adapted_completed_metric)
            / mp.det(completed_null_metric)
        )
    return {
        "base": base,
        "completed": completed,
        "homogeneous_projection": homogeneous_projection,
        "completion_metric": completion_metric,
        "completed_metric": completed_metric,
        "strength": strength,
        "predicted_excess": predicted_excess,
        "base_inverse_capacity": base_inverse_capacity,
        "completed_inverse_capacity": completed_inverse_capacity,
        "predicted_completed_inverse_capacity": (
            predicted_completed_inverse_capacity
        ),
        "capacity_secant_susceptibility": (
            capacity_secant_susceptibility
        ),
        "susceptibility_excess_lower": susceptibility_excess_lower,
        "susceptibility_excess_upper": susceptibility_excess_upper,
        "susceptibility_factor": susceptibility_factor,
        "adapted_basis": adapted_basis,
        "adapted_base_metric": adapted_base_metric,
        "adapted_completed_metric": adapted_completed_metric,
        "determinant_base_inverse_capacity": (
            determinant_base_inverse_capacity
        ),
        "determinant_completed_inverse_capacity": (
            determinant_completed_inverse_capacity
        ),
    }


def endpoint_bidirectional_capacity_susceptibility(
    metric: mp.matrix,
    response: mp.matrix,
    relative_step: mp.mpf = mp.mpf("0.5"),
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Bracket endpoint excess by capacities of W plus/minus a contained block."""
    relative_step = mp.mpf(relative_step)
    if relative_step <= 0 or relative_step >= 1:
        raise ValueError("relative_step must lie strictly between zero and one")
    base = endpoint_polarization_alignment_certificate(
        metric, response, endpoint_weights
    )
    dimension = metric.rows
    identity = mp.eye(dimension)
    homogeneous_projection = (
        identity
        - base["endpoint_representative"] * response.transpose_conj()
    )
    completion_metric = (
        homogeneous_projection.transpose_conj()
        * base["endpoint_mass"]
        * homogeneous_projection
    )
    if dimension == 1:
        step = mp.mpf("0")
        plus_metric = mp.matrix(metric)
        minus_metric = mp.matrix(metric)
        plus = base
        minus = base
        forward_susceptibility = mp.mpf("0")
        backward_susceptibility = mp.mpf("0")
        centered_susceptibility = mp.mpf("0")
        centered_factor = mp.mpf("1")
        predicted_plus_inverse_capacity = 1 / base["metric_capacity"]
        predicted_minus_inverse_capacity = 1 / base["metric_capacity"]
    else:
        step = relative_step * base["shorted_coercivity"]
        plus_metric = mp.matrix(metric) + step * completion_metric
        minus_metric = mp.matrix(metric) - step * completion_metric
        plus = endpoint_polarization_alignment_certificate(
            plus_metric, response, endpoint_weights
        )
        minus = endpoint_polarization_alignment_certificate(
            minus_metric, response, endpoint_weights
        )
        base_delta = 1 / base["metric_capacity"]
        plus_delta = 1 / plus["metric_capacity"]
        minus_delta = 1 / minus["metric_capacity"]
        forward_susceptibility = (plus_delta - base_delta) / step
        backward_susceptibility = (base_delta - minus_delta) / step
        centered_susceptibility = (plus_delta - minus_delta) / (2 * step)
        step_ratio = step / base["null_coercivity"]
        centered_factor = 1 / (1 - step_ratio**2)
        predicted_plus_inverse_capacity = (
            base["response_line_energy"]
            - mp.fsum(
                abs(base["null_spectral_forcing"][index]) ** 2
                / (
                    base["null_generalized_eigenvalues"][index]
                    + step
                )
                for index in range(dimension - 1)
            )
        )
        predicted_minus_inverse_capacity = (
            base["response_line_energy"]
            - mp.fsum(
                abs(base["null_spectral_forcing"][index]) ** 2
                / (
                    base["null_generalized_eigenvalues"][index]
                    - step
                )
                for index in range(dimension - 1)
            )
        )
    forward_excess_lower = (
        base["endpoint_capacity"] * forward_susceptibility
    )
    backward_excess_upper = (
        base["endpoint_capacity"] * backward_susceptibility
    )
    centered_excess_upper = (
        base["endpoint_capacity"] * centered_susceptibility
    )
    centered_excess_factor_upper = (
        centered_factor * base["dimensionless_excess"]
    )
    adapted_basis = mp.matrix(dimension, dimension)
    for row in range(dimension):
        adapted_basis[row, 0] = base["endpoint_representative"][row]
    for column in range(1, dimension):
        for row in range(dimension):
            adapted_basis[row, column] = base["null_basis"][
                row, column - 1
            ]
    adapted_plus_metric = (
        adapted_basis.transpose_conj()
        * plus_metric
        * adapted_basis
    )
    adapted_minus_metric = (
        adapted_basis.transpose_conj()
        * minus_metric
        * adapted_basis
    )
    if dimension == 1:
        determinant_plus_inverse_capacity = mp.re(
            adapted_plus_metric[0, 0]
        )
        determinant_minus_inverse_capacity = mp.re(
            adapted_minus_metric[0, 0]
        )
    else:
        plus_null_metric = (
            base["null_metric"] + step * base["null_endpoint_mass"]
        )
        minus_null_metric = (
            base["null_metric"] - step * base["null_endpoint_mass"]
        )
        determinant_plus_inverse_capacity = mp.re(
            mp.det(adapted_plus_metric) / mp.det(plus_null_metric)
        )
        determinant_minus_inverse_capacity = mp.re(
            mp.det(adapted_minus_metric) / mp.det(minus_null_metric)
        )
    return {
        "base": base,
        "plus": plus,
        "minus": minus,
        "relative_step": relative_step,
        "step": step,
        "homogeneous_projection": homogeneous_projection,
        "completion_metric": completion_metric,
        "plus_metric": plus_metric,
        "minus_metric": minus_metric,
        "forward_susceptibility": forward_susceptibility,
        "backward_susceptibility": backward_susceptibility,
        "centered_susceptibility": centered_susceptibility,
        "forward_excess_lower": forward_excess_lower,
        "backward_excess_upper": backward_excess_upper,
        "centered_excess_upper": centered_excess_upper,
        "centered_factor": centered_factor,
        "centered_excess_factor_upper": centered_excess_factor_upper,
        "predicted_plus_inverse_capacity": (
            predicted_plus_inverse_capacity
        ),
        "predicted_minus_inverse_capacity": (
            predicted_minus_inverse_capacity
        ),
        "adapted_basis": adapted_basis,
        "adapted_plus_metric": adapted_plus_metric,
        "adapted_minus_metric": adapted_minus_metric,
        "determinant_plus_inverse_capacity": (
            determinant_plus_inverse_capacity
        ),
        "determinant_minus_inverse_capacity": (
            determinant_minus_inverse_capacity
        ),
    }


def endpoint_projection_alignment_stability_certificate(
    actual_metric: mp.matrix,
    projected_metric: mp.matrix,
    response: mp.matrix,
    error_majorant: mp.matrix | None = None,
    relative_step: mp.mpf = mp.mpf("0.5"),
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Transfer a projected susceptibility bound through a positive Gram error."""
    if actual_metric.rows != projected_metric.rows or (
        actual_metric.cols != projected_metric.cols
    ):
        raise ValueError("actual and projected metrics must have equal size")
    actual_metric = mp.matrix(actual_metric)
    projected_metric = mp.matrix(projected_metric)
    metric_error = actual_metric - projected_metric
    if error_majorant is None:
        error_majorant = mp.matrix(metric_error)
    else:
        error_majorant = mp.matrix(error_majorant)
    projected_cholesky = mp.cholesky(projected_metric)
    inverse_projected_cholesky = projected_cholesky**-1

    def relative_eigenvalues(metric: mp.matrix) -> mp.matrix:
        compact = (
            inverse_projected_cholesky
            * metric
            * inverse_projected_cholesky.transpose_conj()
        )
        return mp.eigsy(compact, eigvals_only=True)

    error_relative_eigenvalues = relative_eigenvalues(metric_error)
    majorant_relative_eigenvalues = relative_eigenvalues(error_majorant)
    error_majorant_gap_eigenvalues = relative_eigenvalues(
        error_majorant - metric_error
    )
    error_relative_bound = max(
        mp.mpf("0"),
        mp.re(
            error_relative_eigenvalues[
                error_relative_eigenvalues.rows - 1
            ]
        ),
    )
    majorant_relative_bound = max(
        mp.mpf("0"),
        mp.re(
            majorant_relative_eigenvalues[
                majorant_relative_eigenvalues.rows - 1
            ]
        ),
    )
    actual = endpoint_polarization_alignment_certificate(
        actual_metric, response, endpoint_weights
    )
    projected = endpoint_polarization_alignment_certificate(
        projected_metric, response, endpoint_weights
    )
    projected_susceptibility = (
        endpoint_bidirectional_capacity_susceptibility(
            projected_metric,
            response,
            relative_step,
            endpoint_weights,
        )
    )
    if projected_metric.rows == 1:
        alignment_stability_radius = mp.mpf("0")
        error_response_energy = mp.re(
            (
                projected["metric_representative"].transpose_conj()
                * metric_error
                * projected["metric_representative"]
            )[0, 0]
        )
        error_null_coupling = mp.matrix(0, 1)
        actual_null_metric = mp.matrix(0, 0)
        directional_shift = mp.matrix([mp.mpf("0")])
        directional_stability_radius = mp.mpf("0")
        directional_green_energy = mp.mpf("0")
        directional_green_radius = mp.mpf("0")
        directional_green_energy_error_schur_upper = mp.mpf("0")
        directional_green_energy_majorant_schur_upper = mp.mpf("0")
        directional_green_energy_error_balanced_schur_upper = mp.mpf("0")
        directional_green_energy_majorant_balanced_schur_upper = mp.mpf("0")
        directional_green_error_schur_radius = mp.mpf("0")
        directional_green_majorant_schur_radius = mp.mpf("0")
        directional_green_error_balanced_schur_radius = mp.mpf("0")
        directional_green_majorant_balanced_schur_radius = mp.mpf("0")
    else:
        alignment_stability_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * majorant_relative_bound
            / (
                projected["metric_capacity"]
                * projected["null_coercivity"]
            )
        )
        null_basis = projected["null_basis"]
        error_response_energy = mp.re(
            (
                projected["metric_representative"].transpose_conj()
                * metric_error
                * projected["metric_representative"]
            )[0, 0]
        )
        error_null_coupling = (
            null_basis.transpose_conj()
            * metric_error
            * projected["metric_representative"]
        )
        actual_null_metric = (
            null_basis.transpose_conj()
            * actual_metric
            * null_basis
        )
        directional_shift = (
            -null_basis
            * (actual_null_metric**-1)
            * error_null_coupling
        )
        directional_stability_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * mp.re(
                (
                    directional_shift.transpose_conj()
                    * projected["endpoint_mass"]
                    * directional_shift
                )[0, 0]
            )
        )
        directional_green_energy = mp.re(
            (
                error_null_coupling.transpose_conj()
                * (projected["null_metric"]**-1)
                * error_null_coupling
            )[0, 0]
        )
        directional_green_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * directional_green_energy
            / projected["null_coercivity"]
        )
        projected_inverse_capacity = 1 / projected["metric_capacity"]
        directional_green_energy_error_schur_upper = (
            error_relative_bound
            * max(
                mp.mpf("0"),
                error_relative_bound * projected_inverse_capacity
                - error_response_energy,
            )
        )
        directional_green_energy_majorant_schur_upper = (
            majorant_relative_bound
            * max(
                mp.mpf("0"),
                majorant_relative_bound * projected_inverse_capacity
                - error_response_energy,
            )
        )
        directional_green_energy_error_balanced_schur_upper = min(
            directional_green_energy_error_schur_upper,
            error_relative_bound
            * max(mp.mpf("0"), error_response_energy),
        )
        directional_green_energy_majorant_balanced_schur_upper = min(
            directional_green_energy_majorant_schur_upper,
            majorant_relative_bound
            * max(mp.mpf("0"), error_response_energy),
        )
        directional_green_error_schur_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * directional_green_energy_error_schur_upper
            / projected["null_coercivity"]
        )
        directional_green_majorant_schur_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * directional_green_energy_majorant_schur_upper
            / projected["null_coercivity"]
        )
        directional_green_error_balanced_schur_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * directional_green_energy_error_balanced_schur_upper
            / projected["null_coercivity"]
        )
        directional_green_majorant_balanced_schur_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * directional_green_energy_majorant_balanced_schur_upper
            / projected["null_coercivity"]
        )
    actual_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + alignment_stability_radius
    ) ** 2
    directional_actual_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + directional_stability_radius
    ) ** 2
    directional_green_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + directional_green_radius
    ) ** 2
    directional_green_error_schur_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + directional_green_error_schur_radius
    ) ** 2
    directional_green_majorant_schur_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + directional_green_majorant_schur_radius
    ) ** 2
    directional_green_error_balanced_schur_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + directional_green_error_balanced_schur_radius
    ) ** 2
    directional_green_majorant_balanced_schur_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + directional_green_majorant_balanced_schur_radius
    ) ** 2
    exact_square_root_excess_difference = abs(
        mp.sqrt(actual["dimensionless_excess"])
        - mp.sqrt(projected["dimensionless_excess"])
    )
    projected_inverse_capacity = 1 / projected["metric_capacity"]
    actual_inverse_capacity = 1 / actual["metric_capacity"]
    dimension = projected_metric.rows
    capacity_adapted_basis = mp.matrix(dimension, dimension)
    for row in range(dimension):
        capacity_adapted_basis[row, 0] = projected[
            "metric_representative"
        ][row]
        for column in range(1, dimension):
            capacity_adapted_basis[row, column] = projected[
                "null_basis"
            ][row, column - 1]
    capacity_adapted_projected_metric = (
        capacity_adapted_basis.transpose_conj()
        * projected_metric
        * capacity_adapted_basis
    )
    capacity_adapted_actual_metric = (
        capacity_adapted_basis.transpose_conj()
        * actual_metric
        * capacity_adapted_basis
    )
    if dimension == 1:
        determinant_projected_inverse_capacity = mp.re(
            capacity_adapted_projected_metric[0, 0]
        )
        determinant_actual_inverse_capacity = mp.re(
            capacity_adapted_actual_metric[0, 0]
        )
    else:
        determinant_projected_inverse_capacity = mp.re(
            mp.det(capacity_adapted_projected_metric)
            / mp.det(projected["null_metric"])
        )
        determinant_actual_inverse_capacity = mp.re(
            mp.det(capacity_adapted_actual_metric)
            / mp.det(actual_null_metric)
        )
    capacity_relaxation_energy = max(
        mp.mpf("0"),
        error_response_energy
        - (actual_inverse_capacity - projected_inverse_capacity),
    )
    if projected_metric.rows == 1:
        capacity_relaxation_actual_coercivity_radius = mp.mpf("0")
        capacity_relaxation_projected_coercivity_radius = mp.mpf("0")
    else:
        capacity_relaxation_actual_coercivity_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * capacity_relaxation_energy
            / actual["null_coercivity"]
        )
        capacity_relaxation_projected_coercivity_radius = mp.sqrt(
            projected["endpoint_capacity"]
            * capacity_relaxation_energy
            / projected["null_coercivity"]
        )
    capacity_relaxation_actual_coercivity_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + capacity_relaxation_actual_coercivity_radius
    ) ** 2
    capacity_relaxation_projected_coercivity_excess_upper = (
        mp.sqrt(
            projected_susceptibility["centered_excess_upper"]
        )
        + capacity_relaxation_projected_coercivity_radius
    ) ** 2
    return {
        "actual": actual,
        "projected": projected,
        "projected_susceptibility": projected_susceptibility,
        "metric_error": metric_error,
        "error_majorant": error_majorant,
        "error_relative_eigenvalues": error_relative_eigenvalues,
        "majorant_relative_eigenvalues": majorant_relative_eigenvalues,
        "error_majorant_gap_eigenvalues": (
            error_majorant_gap_eigenvalues
        ),
        "error_relative_bound": error_relative_bound,
        "majorant_relative_bound": majorant_relative_bound,
        "alignment_stability_radius": alignment_stability_radius,
        "error_response_energy": error_response_energy,
        "error_null_coupling": error_null_coupling,
        "actual_null_metric": actual_null_metric,
        "directional_shift": directional_shift,
        "directional_stability_radius": (
            directional_stability_radius
        ),
        "directional_green_energy": directional_green_energy,
        "directional_green_radius": directional_green_radius,
        "directional_green_energy_error_schur_upper": (
            directional_green_energy_error_schur_upper
        ),
        "directional_green_energy_majorant_schur_upper": (
            directional_green_energy_majorant_schur_upper
        ),
        "directional_green_energy_error_balanced_schur_upper": (
            directional_green_energy_error_balanced_schur_upper
        ),
        "directional_green_energy_majorant_balanced_schur_upper": (
            directional_green_energy_majorant_balanced_schur_upper
        ),
        "directional_green_error_schur_radius": (
            directional_green_error_schur_radius
        ),
        "directional_green_majorant_schur_radius": (
            directional_green_majorant_schur_radius
        ),
        "directional_green_error_balanced_schur_radius": (
            directional_green_error_balanced_schur_radius
        ),
        "directional_green_majorant_balanced_schur_radius": (
            directional_green_majorant_balanced_schur_radius
        ),
        "exact_square_root_excess_difference": (
            exact_square_root_excess_difference
        ),
        "actual_excess_upper": actual_excess_upper,
        "directional_actual_excess_upper": (
            directional_actual_excess_upper
        ),
        "directional_green_excess_upper": (
            directional_green_excess_upper
        ),
        "directional_green_error_schur_excess_upper": (
            directional_green_error_schur_excess_upper
        ),
        "directional_green_majorant_schur_excess_upper": (
            directional_green_majorant_schur_excess_upper
        ),
        "directional_green_error_balanced_schur_excess_upper": (
            directional_green_error_balanced_schur_excess_upper
        ),
        "directional_green_majorant_balanced_schur_excess_upper": (
            directional_green_majorant_balanced_schur_excess_upper
        ),
        "capacity_relaxation_energy": capacity_relaxation_energy,
        "capacity_relaxation_actual_coercivity_radius": (
            capacity_relaxation_actual_coercivity_radius
        ),
        "capacity_relaxation_projected_coercivity_radius": (
            capacity_relaxation_projected_coercivity_radius
        ),
        "capacity_relaxation_actual_coercivity_excess_upper": (
            capacity_relaxation_actual_coercivity_excess_upper
        ),
        "capacity_relaxation_projected_coercivity_excess_upper": (
            capacity_relaxation_projected_coercivity_excess_upper
        ),
        "capacity_adapted_basis": capacity_adapted_basis,
        "capacity_adapted_projected_metric": (
            capacity_adapted_projected_metric
        ),
        "capacity_adapted_actual_metric": capacity_adapted_actual_metric,
        "determinant_projected_inverse_capacity": (
            determinant_projected_inverse_capacity
        ),
        "determinant_actual_inverse_capacity": (
            determinant_actual_inverse_capacity
        ),
        "projected_inverse_capacity": projected_inverse_capacity,
        "actual_inverse_capacity": actual_inverse_capacity,
        "inverse_capacity_upper": (
            (1 + majorant_relative_bound)
            * projected_inverse_capacity
        ),
    }


def positive_rank_update_response_kernel_certificate(
    base_metric: mp.matrix,
    response: mp.matrix,
    update_columns: mp.matrix,
    update_weights: list[mp.mpf],
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Compress a positive metric update to its charge-response kernel."""
    dimension = base_metric.rows
    update_rank = update_columns.cols
    if base_metric.cols != dimension or response.rows != dimension:
        raise ValueError("incompatible base metric or response")
    if update_columns.rows != dimension or len(update_weights) != update_rank:
        raise ValueError("incompatible update columns or weights")
    weights = [mp.mpf(value) for value in update_weights]
    if update_rank < 1 or any(value <= 0 for value in weights):
        raise ValueError("positive update weights are required")
    weight_metric = mp.diag(weights)
    inverse_weight_metric = mp.diag([1 / value for value in weights])
    base_inverse = base_metric**-1
    charge_kernel = (
        inverse_weight_metric
        + update_columns.transpose_conj()
        * base_inverse
        * update_columns
    )
    response_kernel = (
        update_columns.transpose_conj() * base_inverse * response
    )
    square_root_weight_metric = mp.diag(
        [mp.sqrt(value) for value in weights]
    )
    normalized_charge_gram = (
        square_root_weight_metric
        * update_columns.transpose_conj()
        * base_inverse
        * update_columns
        * square_root_weight_metric
    )
    (
        normalized_charge_eigenvalues,
        normalized_charge_eigenvectors,
    ) = mp.eigsy(normalized_charge_gram)
    relative_update_bound = max(
        mp.mpf("0"),
        mp.re(normalized_charge_eigenvalues[update_rank - 1]),
    )
    weighted_response_kernel = square_root_weight_metric * response_kernel
    spectral_response_coordinates = (
        normalized_charge_eigenvectors.transpose_conj()
        * weighted_response_kernel
    )
    diagonal_response_energy = mp.re(
        (
            weighted_response_kernel.transpose_conj()
            * weighted_response_kernel
        )[0, 0]
    )
    base_capacity = mp.re(
        (response.transpose_conj() * base_inverse * response)[0, 0]
    )
    predicted_updated_capacity = mp.re(
        base_capacity
        - (
            response_kernel.transpose_conj()
            * (charge_kernel**-1)
            * response_kernel
        )[0, 0]
    )
    updated_metric = (
        base_metric
        + update_columns * weight_metric * update_columns.transpose_conj()
    )
    updated_inverse = updated_metric**-1
    direct_updated_capacity = mp.re(
        (response.transpose_conj() * updated_inverse * response)[0, 0]
    )
    direct_capacity_loss = base_capacity - direct_updated_capacity
    response_selective_ratio = diagonal_response_energy / base_capacity
    response_spectral_weights = [
        abs(spectral_response_coordinates[index]) ** 2 / base_capacity
        for index in range(update_rank)
    ]
    direct_capacity_loss_fraction = direct_capacity_loss / base_capacity
    capacity_loss_lower = (
        diagonal_response_energy / (1 + relative_update_bound)
    )
    capacity_loss_upper = diagonal_response_energy
    inverse_capacity_lower = 1 / (
        base_capacity - capacity_loss_lower
    )
    inverse_capacity_upper = 1 / (
        base_capacity - capacity_loss_upper
    )
    inverse_capacity_ratio_lower = 1 / (
        1 - response_selective_ratio / (1 + relative_update_bound)
    )
    inverse_capacity_ratio_upper = 1 / (
        1 - response_selective_ratio
    )
    predicted_updated_determinant = (
        mp.det(base_metric) * mp.det(weight_metric) * mp.det(charge_kernel)
    )
    direct_updated_determinant = mp.det(updated_metric)
    base_alignment = endpoint_polarization_alignment_certificate(
        base_metric, response, endpoint_weights
    )
    null_dimension = max(0, dimension - 1)
    if null_dimension == 0:
        null_update_columns = mp.matrix(0, update_rank)
        null_charge_kernel = mp.matrix(charge_kernel)
        predicted_updated_null_determinant = mp.mpf("1")
        direct_updated_null_determinant = mp.mpf("1")
    else:
        null_update_columns = (
            base_alignment["null_basis"].transpose_conj()
            * update_columns
        )
        null_charge_kernel = (
            inverse_weight_metric
            + null_update_columns.transpose_conj()
            * (base_alignment["null_metric"]**-1)
            * null_update_columns
        )
        updated_null_metric = (
            base_alignment["null_metric"]
            + null_update_columns
            * weight_metric
            * null_update_columns.transpose_conj()
        )
        predicted_updated_null_determinant = (
            mp.det(base_alignment["null_metric"])
            * mp.det(weight_metric)
            * mp.det(null_charge_kernel)
        )
        direct_updated_null_determinant = mp.det(updated_null_metric)
    return {
        "base_metric": base_metric,
        "updated_metric": updated_metric,
        "update_columns": update_columns,
        "update_weights": weights,
        "weight_metric": weight_metric,
        "base_inverse": base_inverse,
        "charge_kernel": charge_kernel,
        "response_kernel": response_kernel,
        "normalized_charge_gram": normalized_charge_gram,
        "normalized_charge_eigenvalues": (
            normalized_charge_eigenvalues
        ),
        "normalized_charge_eigenvectors": (
            normalized_charge_eigenvectors
        ),
        "relative_update_bound": relative_update_bound,
        "weighted_response_kernel": weighted_response_kernel,
        "spectral_response_coordinates": spectral_response_coordinates,
        "response_spectral_weights": response_spectral_weights,
        "diagonal_response_energy": diagonal_response_energy,
        "response_selective_ratio": response_selective_ratio,
        "base_capacity": base_capacity,
        "predicted_updated_capacity": predicted_updated_capacity,
        "direct_updated_capacity": direct_updated_capacity,
        "direct_capacity_loss": direct_capacity_loss,
        "direct_capacity_loss_fraction": direct_capacity_loss_fraction,
        "capacity_loss_lower": capacity_loss_lower,
        "capacity_loss_upper": capacity_loss_upper,
        "inverse_capacity_lower": inverse_capacity_lower,
        "inverse_capacity_upper": inverse_capacity_upper,
        "inverse_capacity_ratio_lower": inverse_capacity_ratio_lower,
        "inverse_capacity_ratio_upper": inverse_capacity_ratio_upper,
        "predicted_updated_inverse_capacity": (
            1 / predicted_updated_capacity
        ),
        "direct_updated_inverse_capacity": 1 / direct_updated_capacity,
        "predicted_updated_determinant": predicted_updated_determinant,
        "direct_updated_determinant": direct_updated_determinant,
        "null_update_columns": null_update_columns,
        "null_charge_kernel": null_charge_kernel,
        "predicted_updated_null_determinant": (
            predicted_updated_null_determinant
        ),
        "direct_updated_null_determinant": direct_updated_null_determinant,
    }


def positive_rank_update_amplitude_capacity_certificate(
    base_metric: mp.matrix,
    response: mp.matrix,
    update_columns: mp.matrix,
    update_weights: list[mp.mpf],
    amplitudes: list[mp.mpf],
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Reconstruct a positive-update capacity path from its response measure."""
    base = positive_rank_update_response_kernel_certificate(
        base_metric,
        response,
        update_columns,
        update_weights,
        endpoint_weights,
    )
    values: list[dict[str, mp.mpf]] = []
    weight_metric = base["weight_metric"]
    for raw_amplitude in amplitudes:
        amplitude = mp.mpf(raw_amplitude)
        if amplitude < 0:
            raise ValueError("amplitudes must be nonnegative")
        normalized_capacity = 1 - amplitude * mp.fsum(
            weight
            / (1 + amplitude * eigenvalue)
            for weight, eigenvalue in zip(
                base["response_spectral_weights"],
                base["normalized_charge_eigenvalues"],
            )
        )
        predicted_capacity = base["base_capacity"] * normalized_capacity
        direct_metric = (
            base_metric
            + amplitude
            * update_columns
            * weight_metric
            * update_columns.transpose_conj()
        )
        direct_inverse = direct_metric**-1
        direct_capacity = mp.re(
            (response.transpose_conj() * direct_inverse * response)[0, 0]
        )
        relative_capacity_loss = (
            1 - direct_capacity / base["base_capacity"]
        )
        if amplitude == 0:
            response_mass_lower = base["response_selective_ratio"]
            response_mass_upper = base["response_selective_ratio"]
        else:
            response_mass_lower = relative_capacity_loss / amplitude
            response_mass_upper = (
                (1 + amplitude * base["relative_update_bound"])
                * relative_capacity_loss
                / amplitude
            )
        values.append(
            {
                "amplitude": amplitude,
                "predicted_capacity": predicted_capacity,
                "direct_capacity": direct_capacity,
                "predicted_inverse_capacity": 1 / predicted_capacity,
                "direct_inverse_capacity": 1 / direct_capacity,
                "relative_capacity_loss": relative_capacity_loss,
                "response_mass_lower": response_mass_lower,
                "response_mass_upper": response_mass_upper,
            }
        )
    positive_values = [
        value for value in values if value["amplitude"] > 0
    ]
    two_amplitude_response_mass_bounds: list[dict[str, mp.mpf]] = []
    for left_index in range(len(positive_values)):
        for right_index in range(left_index + 1, len(positive_values)):
            left = positive_values[left_index]
            right = positive_values[right_index]
            left_amplitude = left["amplitude"]
            right_amplitude = right["amplitude"]
            if left_amplitude == right_amplitude:
                continue
            if left_amplitude > right_amplitude:
                left, right = right, left
                left_amplitude, right_amplitude = (
                    right_amplitude,
                    left_amplitude,
                )
            left_transform = left["relative_capacity_loss"] / left_amplitude
            right_transform = (
                right["relative_capacity_loss"] / right_amplitude
            )
            denominator = right_amplitude - left_amplitude
            lower = (
                right_amplitude * left_transform
                - left_amplitude * right_transform
            ) / denominator
            upper = (
                right_amplitude
                * (1 + left_amplitude * base["relative_update_bound"])
                * left_transform
                - left_amplitude
                * (1 + right_amplitude * base["relative_update_bound"])
                * right_transform
            ) / denominator
            two_amplitude_response_mass_bounds.append(
                {
                    "left_amplitude": left_amplitude,
                    "right_amplitude": right_amplitude,
                    "response_mass_lower": lower,
                    "response_mass_upper": upper,
                }
            )
    distinct_positive_values: list[dict[str, mp.mpf]] = []
    for value in sorted(positive_values, key=lambda item: item["amplitude"]):
        if not distinct_positive_values or value["amplitude"] != (
            distinct_positive_values[-1]["amplitude"]
        ):
            distinct_positive_values.append(value)
    multi_amplitude_response_mass_bound = None
    if len(distinct_positive_values) >= 2:
        amplitudes_for_bound = [
            value["amplitude"] for value in distinct_positive_values
        ]
        transforms_for_bound = [
            value["relative_capacity_loss"] / value["amplitude"]
            for value in distinct_positive_values
        ]
        bound_order = len(amplitudes_for_bound)
        amplitude_product = mp.fprod(amplitudes_for_bound)
        lower_coefficients: list[mp.mpf] = []
        upper_coefficients: list[mp.mpf] = []
        for index, amplitude in enumerate(amplitudes_for_bound):
            denominator = mp.fprod(
                1 - other_amplitude / amplitude
                for other_index, other_amplitude in enumerate(
                    amplitudes_for_bound
                )
                if other_index != index
            )
            lower_numerator = (
                -amplitude_product * (-1 / amplitude) ** bound_order
            )
            upper_numerator = (
                amplitude_product
                * (-1 / amplitude) ** (bound_order - 1)
                * (base["relative_update_bound"] + 1 / amplitude)
            )
            lower_coefficients.append(lower_numerator / denominator)
            upper_coefficients.append(upper_numerator / denominator)
        multi_lower = mp.fsum(
            coefficient * transform
            for coefficient, transform in zip(
                lower_coefficients, transforms_for_bound
            )
        )
        multi_upper = mp.fsum(
            coefficient * transform
            for coefficient, transform in zip(
                upper_coefficients, transforms_for_bound
            )
        )
        multi_amplitude_response_mass_bound = {
            "order": bound_order,
            "amplitudes": amplitudes_for_bound,
            "lower_coefficients": lower_coefficients,
            "upper_coefficients": upper_coefficients,
            "response_mass_lower": multi_lower,
            "response_mass_upper": multi_upper,
            "relative_width_upper": (
                amplitude_product
                * base["relative_update_bound"] ** bound_order
            ),
        }
    return {
        "base": base,
        "values": values,
        "two_amplitude_response_mass_bounds": (
            two_amplitude_response_mass_bounds
        ),
        "multi_amplitude_response_mass_bound": (
            multi_amplitude_response_mass_bound
        ),
    }


def endpoint_completion_multiamplitude_susceptibility_certificate(
    metric: mp.matrix,
    response: mp.matrix,
    relative_amplitudes: list[mp.mpf],
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Certify endpoint excess from positive completion capacities only."""
    base = endpoint_polarization_alignment_certificate(
        metric, response, endpoint_weights
    )
    if metric.rows == 1:
        return {
            "base": base,
            "relative_amplitudes": [],
            "completion_samples": [],
            "susceptibility_lower": mp.mpf("0"),
            "susceptibility_upper": mp.mpf("0"),
            "relative_width_upper": mp.mpf("0"),
        }
    amplitudes = sorted({mp.mpf(value) for value in relative_amplitudes})
    if len(amplitudes) < 1 or any(value <= 0 for value in amplitudes):
        raise ValueError("positive relative amplitudes are required")
    coercivity = base["shorted_coercivity"]
    base_inverse_capacity = 1 / base["metric_capacity"]
    samples: list[dict[str, object]] = []
    transforms: list[mp.mpf] = []
    for relative_amplitude in amplitudes:
        step = relative_amplitude * coercivity
        completion = endpoint_transversal_hodge_completion(
            metric, response, step, endpoint_weights
        )
        completed_inverse_capacity = completion[
            "completed_inverse_capacity"
        ]
        transform = (
            completed_inverse_capacity - base_inverse_capacity
        ) / step
        transforms.append(transform)
        samples.append(
            {
                "relative_amplitude": relative_amplitude,
                "step": step,
                "transform": transform,
                "completed_inverse_capacity": completed_inverse_capacity,
                "determinant_completed_inverse_capacity": completion[
                    "determinant_completed_inverse_capacity"
                ],
                "completion": completion,
            }
        )
    order = len(amplitudes)
    amplitude_product = mp.fprod(amplitudes)
    lower_coefficients: list[mp.mpf] = []
    upper_coefficients: list[mp.mpf] = []
    for index, amplitude in enumerate(amplitudes):
        denominator = mp.fprod(
            1 - other_amplitude / amplitude
            for other_index, other_amplitude in enumerate(amplitudes)
            if other_index != index
        )
        lower_coefficients.append(
            -amplitude_product * (-1 / amplitude) ** order / denominator
        )
        upper_coefficients.append(
            amplitude_product
            * (-1 / amplitude) ** (order - 1)
            * (1 + 1 / amplitude)
            / denominator
        )
    mass_lower = mp.fsum(
        coefficient * transform
        for coefficient, transform in zip(lower_coefficients, transforms)
    )
    mass_upper = mp.fsum(
        coefficient * transform
        for coefficient, transform in zip(upper_coefficients, transforms)
    )
    endpoint_capacity = base["endpoint_capacity"]
    return {
        "base": base,
        "relative_amplitudes": amplitudes,
        "completion_samples": samples,
        "lower_coefficients": lower_coefficients,
        "upper_coefficients": upper_coefficients,
        "spectral_mass": base["dimensionless_excess"] / endpoint_capacity,
        "mass_lower": mass_lower,
        "mass_upper": mass_upper,
        "susceptibility_lower": endpoint_capacity * mass_lower,
        "susceptibility_upper": endpoint_capacity * mass_upper,
        "relative_width_upper": amplitude_product,
    }


def endpoint_polyhedral_riesz_determinant_certificate(
    metric: mp.matrix,
    response: mp.matrix,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Recover exact real weighted l1 leverage from positive determinants."""
    base = endpoint_polarization_alignment_certificate(
        metric, response, endpoint_weights
    )
    dimension = metric.rows
    transform = base["transform"]
    weights = base["weights"]
    metric_inverse = metric**-1
    metric_capacity = base["metric_capacity"]
    determinant_metric = mp.det(metric)
    phase_records: list[dict[str, object]] = []
    maximal_mixed_absolute = mp.mpf("0")
    for tail_signs in itertools.product([-1, 1], repeat=dimension):
        signs = [mp.mpf("1")] + [mp.mpf(value) for value in tail_signs]
        weighted_signs = mp.matrix(
            [weights[index] * signs[index] for index in range(dimension + 1)]
        )
        phase_response = transform.transpose_conj() * weighted_signs
        plus_response = response + phase_response
        minus_response = response - phase_response
        plus_capacity = mp.re(
            (
                plus_response.transpose_conj()
                * metric_inverse
                * plus_response
            )[0, 0]
        )
        minus_capacity = mp.re(
            (
                minus_response.transpose_conj()
                * metric_inverse
                * minus_response
            )[0, 0]
        )
        mixed_response = (plus_capacity - minus_capacity) / 4
        determinant_plus_capacity = mp.re(
            mp.det(
                metric
                + plus_response * plus_response.transpose_conj()
            )
            / determinant_metric
            - 1
        )
        determinant_minus_capacity = mp.re(
            mp.det(
                metric
                + minus_response * minus_response.transpose_conj()
            )
            / determinant_metric
            - 1
        )
        maximal_mixed_absolute = max(
            maximal_mixed_absolute, abs(mixed_response)
        )
        phase_records.append(
            {
                "signs": signs,
                "phase_response": phase_response,
                "plus_response": plus_response,
                "minus_response": minus_response,
                "plus_capacity": plus_capacity,
                "minus_capacity": minus_capacity,
                "determinant_plus_capacity": determinant_plus_capacity,
                "determinant_minus_capacity": determinant_minus_capacity,
                "mixed_response": mixed_response,
            }
        )
    determinant_polyhedral_leverage = (
        maximal_mixed_absolute / metric_capacity
    )
    return {
        "base": base,
        "phase_records": phase_records,
        "phase_count": len(phase_records),
        "maximal_mixed_absolute": maximal_mixed_absolute,
        "determinant_polyhedral_leverage": (
            determinant_polyhedral_leverage
        ),
        "exact_response_leverage_l1": base[
            "exact_response_leverage_l1"
        ],
        "quadratic_response_leverage_upper": base[
            "response_leverage_l1_upper"
        ],
    }


def endpoint_alternating_external_phase_certificate(
    metric: mp.matrix,
    response: mp.matrix,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Split weighted endpoint l1 leverage into one alternating phase and defect.

    With elementary weights c_k=k+1, the alternating phase is Q'(-1),
    where Q(x)=F(1-x), and hence equals -F'(2).  The exact l1 norm is
    the absolute external derivative plus twice the smaller of the
    alternating-match and alternating-mismatch coefficient masses.
    """
    base = endpoint_polarization_alignment_certificate(
        metric, response, endpoint_weights
    )
    dimension = metric.rows
    endpoint_coefficients = (
        base["transform"] * base["metric_representative"]
    )
    weights = base["weights"]
    alternating_signs = [
        mp.mpf((-1) ** index) for index in range(dimension + 1)
    ]
    alternating_phase = mp.fsum(
        weights[index]
        * alternating_signs[index]
        * endpoint_coefficients[index]
        for index in range(dimension + 1)
    )
    exact_weighted_l1 = mp.fsum(
        weights[index] * abs(endpoint_coefficients[index])
        for index in range(dimension + 1)
    )
    orientation = mp.sign(alternating_phase)
    if orientation == 0:
        orientation = mp.mpf("1")
    matching_mass = mp.mpf("0")
    mismatching_mass = mp.mpf("0")
    coefficient_records: list[dict[str, object]] = []
    tolerance = mp.eps * max(mp.mpf("1"), exact_weighted_l1)
    for index in range(dimension + 1):
        weighted_mass = weights[index] * abs(
            endpoint_coefficients[index]
        )
        expected_sign = orientation * alternating_signs[index]
        matches = (
            abs(endpoint_coefficients[index]) <= tolerance
            or mp.sign(endpoint_coefficients[index]) == expected_sign
        )
        if matches:
            matching_mass += weighted_mass
        else:
            mismatching_mass += weighted_mass
        coefficient_records.append(
            {
                "index": index,
                "coefficient": endpoint_coefficients[index],
                "weight": weights[index],
                "weighted_mass": weighted_mass,
                "expected_sign": expected_sign,
                "matches": matches,
            }
        )
    sign_defect = exact_weighted_l1 - abs(alternating_phase)
    predicted_sign_defect = 2 * min(
        matching_mass, mismatching_mass
    )
    alternating_phase_ratio = (
        abs(alternating_phase) / exact_weighted_l1
        if exact_weighted_l1 > 0
        else mp.mpf("1")
    )
    weighted_sign_vector = mp.matrix(
        [
            weights[index] * alternating_signs[index]
            for index in range(dimension + 1)
        ]
    )
    alternating_probe = (
        base["transform"].transpose_conj() * weighted_sign_vector
    )
    metric_inverse = metric**-1
    direct_alternating_phase = mp.re(
        (
            response.transpose_conj()
            * metric_inverse
            * alternating_probe
        )[0, 0]
        / base["metric_capacity"]
    )
    elementary_weights = all(
        weights[index] == index + 1
        for index in range(dimension + 1)
    )
    external_derivative = -alternating_phase if elementary_weights else None
    external_probe_expected = (
        mp.matrix(
            [
                mp.mpf(power + 2) * 2 ** (power - 1)
                for power in range(1, dimension + 1)
            ]
        )
        if elementary_weights
        else None
    )
    return {
        "base": base,
        "endpoint_coefficients": endpoint_coefficients,
        "weights": weights,
        "coefficient_records": coefficient_records,
        "alternating_signs": alternating_signs,
        "alternating_probe": alternating_probe,
        "alternating_phase": alternating_phase,
        "direct_alternating_phase": direct_alternating_phase,
        "exact_weighted_l1": exact_weighted_l1,
        "matching_mass": matching_mass,
        "mismatching_mass": mismatching_mass,
        "sign_defect": sign_defect,
        "predicted_sign_defect": predicted_sign_defect,
        "alternating_phase_ratio": alternating_phase_ratio,
        "is_alternating": mismatching_mass <= tolerance,
        "elementary_weights": elementary_weights,
        "external_derivative": external_derivative,
        "external_probe_expected": external_probe_expected,
    }


def endpoint_external_period_capacity_loss_certificate(
    metric: mp.matrix,
    response: mp.matrix,
    amplitude: mp.mpf = mp.mpf("1"),
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Recover the alternating external period from a positive capacity loss.

    For the alternating probe q and response capacity C, the q-capacity
    lost after the positive update W+sDD^* is

        C_q-C_q(s)=s|D^*W^{-1}q|^2/(1+sC).

    Thus the absolute external period divided by C is obtained from a
    single nonnegative capacity loss.  At infinite amplitude this is the
    Schur loss C_q-C_{q|D}.
    """
    amplitude = mp.mpf(amplitude)
    if amplitude <= 0:
        raise ValueError("amplitude must be positive")
    alternating = endpoint_alternating_external_phase_certificate(
        metric, response, endpoint_weights
    )
    metric = mp.matrix(metric)
    response = mp.matrix(response)
    metric_inverse = metric**-1
    probe = alternating["alternating_probe"]
    response_capacity = alternating["base"]["metric_capacity"]
    probe_capacity = mp.re(
        (probe.transpose_conj() * metric_inverse * probe)[0, 0]
    )
    mixed_capacity = mp.re(
        (
            response.transpose_conj()
            * metric_inverse
            * probe
        )[0, 0]
    )
    conditioned_probe_capacity = (
        probe_capacity - abs(mixed_capacity) ** 2 / response_capacity
    )
    infinite_capacity_loss = (
        probe_capacity - conditioned_probe_capacity
    )
    correlation_fraction = (
        infinite_capacity_loss / probe_capacity
        if probe_capacity > 0
        else mp.mpf("0")
    )

    updated_metric = (
        metric + amplitude * response * response.transpose_conj()
    )
    updated_metric_inverse = updated_metric**-1
    updated_probe_capacity = mp.re(
        (
            probe.transpose_conj()
            * updated_metric_inverse
            * probe
        )[0, 0]
    )
    finite_capacity_loss = probe_capacity - updated_probe_capacity
    predicted_updated_probe_capacity = (
        probe_capacity
        - amplitude
        * abs(mixed_capacity) ** 2
        / (1 + amplitude * response_capacity)
    )
    external_leverage_from_finite_loss = mp.sqrt(
        (1 + amplitude * response_capacity)
        * max(mp.mpf("0"), finite_capacity_loss)
        / (amplitude * response_capacity**2)
    )
    external_leverage_from_schur_loss = mp.sqrt(
        max(mp.mpf("0"), infinite_capacity_loss)
        / response_capacity
    )
    direct_external_leverage = (
        abs(mixed_capacity) / response_capacity
    )

    determinant_metric = mp.det(metric)
    determinant_updated_metric = mp.det(updated_metric)
    determinant_response_capacity = mp.re(
        determinant_updated_metric / determinant_metric - 1
    ) / amplitude
    determinant_probe_capacity = mp.re(
        mp.det(metric + probe * probe.transpose_conj())
        / determinant_metric
        - 1
    )
    determinant_updated_probe_capacity = mp.re(
        mp.det(updated_metric + probe * probe.transpose_conj())
        / determinant_updated_metric
        - 1
    )
    dual_capacity_gram_determinant = (
        response_capacity * probe_capacity - abs(mixed_capacity) ** 2
    )
    return {
        "alternating": alternating,
        "amplitude": amplitude,
        "probe": probe,
        "response_capacity": response_capacity,
        "probe_capacity": probe_capacity,
        "mixed_capacity": mixed_capacity,
        "conditioned_probe_capacity": conditioned_probe_capacity,
        "infinite_capacity_loss": infinite_capacity_loss,
        "correlation_fraction": correlation_fraction,
        "dual_capacity_gram_determinant": (
            dual_capacity_gram_determinant
        ),
        "updated_metric": updated_metric,
        "updated_probe_capacity": updated_probe_capacity,
        "predicted_updated_probe_capacity": (
            predicted_updated_probe_capacity
        ),
        "finite_capacity_loss": finite_capacity_loss,
        "external_leverage_from_finite_loss": (
            external_leverage_from_finite_loss
        ),
        "external_leverage_from_schur_loss": (
            external_leverage_from_schur_loss
        ),
        "direct_external_leverage": direct_external_leverage,
        "determinant_response_capacity": (
            determinant_response_capacity
        ),
        "determinant_probe_capacity": determinant_probe_capacity,
        "determinant_updated_probe_capacity": (
            determinant_updated_probe_capacity
        ),
    }


def dual_observation_block_overlap_certificate(
    metric: mp.matrix,
    response: mp.matrix,
    probe: mp.matrix,
    observation: mp.matrix,
    block_rows: list[list[int]],
) -> dict[str, object]:
    """Bound a dual response/probe correlation by positive block overlap.

    For W=O^*O, partition the observation rows into blocks.  The normalized
    response and probe block energies form probability vectors d and e.
    Their squared Bhattacharyya overlap bounds the squared dual correlation.
    """
    if metric.rows != metric.cols or metric.rows < 1:
        raise ValueError("metric must be a nonempty square matrix")
    dimension = metric.rows
    if response.rows != dimension or response.cols != 1:
        raise ValueError("response must be a compatible column")
    if probe.rows != dimension or probe.cols != 1:
        raise ValueError("probe must be a compatible column")
    if observation.cols != dimension:
        raise ValueError("observation must have compatible columns")
    flattened_rows = [row for block in block_rows for row in block]
    if sorted(flattened_rows) != list(range(observation.rows)):
        raise ValueError("block_rows must partition all observation rows")
    if len(set(flattened_rows)) != observation.rows:
        raise ValueError("observation rows must occur exactly once")

    metric = mp.matrix(metric)
    response = mp.matrix(response)
    probe = mp.matrix(probe)
    observation = mp.matrix(observation)
    metric_inverse = metric**-1
    observation_metric = observation.transpose_conj() * observation
    observation_metric_residual = metric - observation_metric
    response_flow = observation * metric_inverse * response
    probe_flow = observation * metric_inverse * probe
    response_capacity = mp.re(
        (response_flow.transpose_conj() * response_flow)[0, 0]
    )
    probe_capacity = mp.re(
        (probe_flow.transpose_conj() * probe_flow)[0, 0]
    )
    mixed_capacity = (
        response_flow.transpose_conj() * probe_flow
    )[0, 0]
    if response_capacity <= 0 or probe_capacity <= 0:
        raise ValueError("response and probe capacities must be positive")

    block_records: list[dict[str, object]] = []
    bhattacharyya_overlap = mp.mpf("0")
    block_current_absolute_sum = mp.mpf("0")
    for index, rows in enumerate(block_rows):
        response_energy = mp.fsum(
            abs(response_flow[row]) ** 2 for row in rows
        )
        probe_energy = mp.fsum(
            abs(probe_flow[row]) ** 2 for row in rows
        )
        block_current = mp.fsum(
            mp.conj(response_flow[row]) * probe_flow[row]
            for row in rows
        )
        response_mass = response_energy / response_capacity
        probe_mass = probe_energy / probe_capacity
        overlap_mass = mp.sqrt(
            max(mp.mpf("0"), response_mass * probe_mass)
        )
        bhattacharyya_overlap += overlap_mass
        block_current_absolute_sum += abs(block_current)
        local_correlation_fraction = (
            abs(block_current) ** 2 / (response_energy * probe_energy)
            if response_energy > 0 and probe_energy > 0
            else mp.mpf("0")
        )
        block_records.append(
            {
                "index": index,
                "rows": list(rows),
                "response_energy": response_energy,
                "probe_energy": probe_energy,
                "block_current": block_current,
                "response_mass": response_mass,
                "probe_mass": probe_mass,
                "overlap_mass": overlap_mass,
                "local_correlation_fraction": (
                    local_correlation_fraction
                ),
            }
        )
    correlation_fraction = (
        abs(mixed_capacity) ** 2
        / (response_capacity * probe_capacity)
    )
    overlap_correlation_upper = bhattacharyya_overlap**2
    normalized_block_total_variation = (
        block_current_absolute_sum
        / mp.sqrt(response_capacity * probe_capacity)
    )
    local_coherence_correlation_upper = (
        normalized_block_total_variation**2
    )
    external_leverage = abs(mixed_capacity) / response_capacity
    local_coherence_external_leverage_upper = (
        block_current_absolute_sum / response_capacity
    )
    overlap_external_leverage_upper = (
        mp.sqrt(probe_capacity / response_capacity)
        * bhattacharyya_overlap
    )
    signed_block_cancellation_ratio = (
        abs(mixed_capacity) / block_current_absolute_sum
        if block_current_absolute_sum > 0
        else mp.mpf("0")
    )
    hellinger_distance_squared = 1 - bhattacharyya_overlap
    return {
        "observation_metric": observation_metric,
        "observation_metric_residual": observation_metric_residual,
        "response_flow": response_flow,
        "probe_flow": probe_flow,
        "response_capacity": response_capacity,
        "probe_capacity": probe_capacity,
        "mixed_capacity": mixed_capacity,
        "block_records": block_records,
        "bhattacharyya_overlap": bhattacharyya_overlap,
        "hellinger_distance_squared": hellinger_distance_squared,
        "correlation_fraction": correlation_fraction,
        "normalized_block_total_variation": (
            normalized_block_total_variation
        ),
        "local_coherence_correlation_upper": (
            local_coherence_correlation_upper
        ),
        "overlap_correlation_upper": overlap_correlation_upper,
        "external_leverage": external_leverage,
        "local_coherence_external_leverage_upper": (
            local_coherence_external_leverage_upper
        ),
        "overlap_external_leverage_upper": (
            overlap_external_leverage_upper
        ),
        "block_current_absolute_sum": block_current_absolute_sum,
        "signed_block_cancellation_ratio": (
            signed_block_cancellation_ratio
        ),
    }


def mobius_endpoint_external_dyadic_overlap_certificate(
    size: int,
    direction_count: int,
    right_endpoint: int | None = None,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Dyadically compare Mobius response and external-probe Hodge masses."""
    if right_endpoint is None:
        right_endpoint = size**2
    recovery = mobius_cell_vandermonde_recovery_certificate(
        size, direction_count, endpoint_weights=endpoint_weights
    )
    prefix_endpoint = max(recovery["squarefree_nodes"])
    observation_data = (
        mobius_endpoint_sparse_observation_flow_certificate(
            size,
            direction_count,
            prefix_endpoint=prefix_endpoint,
            right_endpoint=right_endpoint,
            endpoint_weights=endpoint_weights,
        )
    )
    spatial_data = observation_data["mertens_data"]["spatial_data"]
    alternating = endpoint_alternating_external_phase_certificate(
        spatial_data["metric"],
        spatial_data["response"],
        endpoint_weights,
    )
    cell_row_count = observation_data["cell_row_count"]
    block_rows: list[list[int]] = [[0]]
    shell_records: list[dict[str, int]] = [
        {"left": 0, "right": 0}
    ]
    shell_left = 1
    while shell_left < right_endpoint:
        shell_right = min(right_endpoint - 1, 2 * shell_left - 1)
        rows: list[int] = []
        for integer in range(shell_left, shell_right + 1):
            rows.append(integer)
            rows.append(cell_row_count + integer - 1)
        block_rows.append(rows)
        shell_records.append(
            {"left": shell_left, "right": shell_right}
        )
        shell_left *= 2
    overlap = dual_observation_block_overlap_certificate(
        spatial_data["metric"],
        spatial_data["response"],
        alternating["alternating_probe"],
        observation_data["observation"],
        block_rows,
    )
    for shell, block in zip(shell_records, overlap["block_records"]):
        block["left"] = shell["left"]
        block["right"] = shell["right"]
    return {
        "recovery": recovery,
        "observation_data": observation_data,
        "alternating": alternating,
        "shell_records": shell_records,
        "overlap": overlap,
    }


def mobius_endpoint_periodic_conductor_overlap_certificate(
    size: int,
    direction_count: int,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Parseval/Farey conductor-block purity for the periodic endpoint Gram."""
    periodic_data = mobius_endpoint_direction_periodic_gram(
        size, direction_count
    )
    metric = periodic_data["metric"]
    response = periodic_data["response"]
    observation = mp.matrix(size + 1, direction_count)
    for column in range(direction_count):
        observation[0, column] = response[column] / 2
    for denominator in range(1, size + 1):
        scale = mp.sqrt(
            reduced_denominator_density(denominator) / 12
        )
        for column in range(direction_count):
            observation[denominator, column] = (
                scale
                * periodic_data["conductor_amplitudes"][
                    denominator - 1, column
                ]
            )
    block_rows: list[list[int]] = [[0]]
    shell_records: list[dict[str, int]] = [
        {"left": 0, "right": 0}
    ]
    shell_left = 1
    while shell_left <= size:
        shell_right = min(size, 2 * shell_left - 1)
        block_rows.append(list(range(shell_left, shell_right + 1)))
        shell_records.append(
            {"left": shell_left, "right": shell_right}
        )
        shell_left *= 2
    alternating = endpoint_alternating_external_phase_certificate(
        metric, response, endpoint_weights
    )
    overlap = dual_observation_block_overlap_certificate(
        metric,
        response,
        alternating["alternating_probe"],
        observation,
        block_rows,
    )
    for shell, block in zip(shell_records, overlap["block_records"]):
        block["left"] = shell["left"]
        block["right"] = shell["right"]
    return {
        "periodic_data": periodic_data,
        "observation": observation,
        "shell_records": shell_records,
        "alternating": alternating,
        "overlap": overlap,
    }


def mobius_endpoint_conductor_completion_gap_certificate(
    size: int,
    direction_count: int,
    far_majorant_constant: mp.mpf = mp.mpf(10) / 3,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Compare available periodic completion with conductor-purity dominance."""
    far_majorant_constant = mp.mpf(far_majorant_constant)
    if far_majorant_constant <= 0:
        raise ValueError("far_majorant_constant must be positive")
    spatial_data = mobius_endpoint_direction_spatial_gram(
        size, direction_count, 0, size**2
    )
    periodic = mobius_endpoint_periodic_conductor_overlap_certificate(
        size, direction_count, endpoint_weights
    )
    spatial_metric = spatial_data["metric"]
    periodic_metric = periodic["periodic_data"]["metric"]
    periodic_cholesky = mp.cholesky(periodic_metric)
    inverse_periodic_cholesky = periodic_cholesky**-1
    relative_spatial_compact = (
        inverse_periodic_cholesky
        * spatial_metric
        * inverse_periodic_cholesky.transpose_conj()
    )
    relative_spatial_eigenvalues = mp.eigsy(
        relative_spatial_compact, eigvals_only=True
    )
    relative_spatial_minimum = mp.re(
        relative_spatial_eigenvalues[0]
    )
    relative_spatial_maximum = mp.re(
        relative_spatial_eigenvalues[
            relative_spatial_eigenvalues.rows - 1
        ]
    )
    available_periodic_amplitude = far_majorant_constant / size**2
    available_relative_error = (
        relative_spatial_maximum / available_periodic_amplitude
    )
    amplitude_for_unit_relative_error = relative_spatial_maximum
    amplitude_for_half_relative_error = 2 * relative_spatial_maximum
    available_to_unit_dominance_ratio = (
        available_periodic_amplitude
        / amplitude_for_unit_relative_error
    )
    periodic_response_capacity = periodic["overlap"][
        "response_capacity"
    ]
    periodic_probe_capacity = periodic["overlap"]["probe_capacity"]
    available_external_transfer_radius = mp.sqrt(
        periodic_probe_capacity
        / periodic_response_capacity
        * available_relative_error
    )
    half_error_external_transfer_radius = mp.sqrt(
        periodic_probe_capacity
        / periodic_response_capacity
        / 2
    )
    response = spatial_data["response"]
    spatial_external = endpoint_alternating_external_phase_certificate(
        spatial_metric, response, endpoint_weights
    )
    available_completed_metric = (
        spatial_metric
        + available_periodic_amplitude * periodic_metric
    )
    available_completed_external = (
        endpoint_alternating_external_phase_certificate(
            available_completed_metric,
            response,
            endpoint_weights,
        )
    )
    half_error_completed_metric = (
        spatial_metric
        + amplitude_for_half_relative_error * periodic_metric
    )
    half_error_completed_external = (
        endpoint_alternating_external_phase_certificate(
            half_error_completed_metric,
            response,
            endpoint_weights,
        )
    )
    return {
        "spatial_data": spatial_data,
        "periodic": periodic,
        "relative_spatial_eigenvalues": relative_spatial_eigenvalues,
        "relative_spatial_minimum": relative_spatial_minimum,
        "relative_spatial_maximum": relative_spatial_maximum,
        "far_majorant_constant": far_majorant_constant,
        "available_periodic_amplitude": available_periodic_amplitude,
        "available_relative_error": available_relative_error,
        "amplitude_for_unit_relative_error": (
            amplitude_for_unit_relative_error
        ),
        "amplitude_for_half_relative_error": (
            amplitude_for_half_relative_error
        ),
        "available_to_unit_dominance_ratio": (
            available_to_unit_dominance_ratio
        ),
        "periodic_response_capacity": periodic_response_capacity,
        "periodic_probe_capacity": periodic_probe_capacity,
        "available_external_transfer_radius": (
            available_external_transfer_radius
        ),
        "half_error_external_transfer_radius": (
            half_error_external_transfer_radius
        ),
        "spatial_external": spatial_external,
        "available_completed_metric": available_completed_metric,
        "available_completed_external": available_completed_external,
        "half_error_completed_metric": half_error_completed_metric,
        "half_error_completed_external": half_error_completed_external,
    }


def acyclic_completion_superdeterminant_certificate(
    base_metric: mp.matrix,
    update_columns: mp.matrix,
    response: mp.matrix,
    probe: mp.matrix | None = None,
) -> dict[str, object]:
    """Certify exact ghost cancellation for a positive acyclic completion.

    The even update W+UU^* is paired with the odd charge kernel
    I+U^*W^{-1}U.  Their determinant quotient equals det(W), and the odd
    logarithmic variations exactly cancel every apparent capacity or mixed
    period improvement of the even sector.
    """
    if base_metric.rows != base_metric.cols or base_metric.rows < 1:
        raise ValueError("base_metric must be a nonempty square matrix")
    dimension = base_metric.rows
    if update_columns.rows != dimension:
        raise ValueError("update_columns must have compatible rows")
    if response.rows != dimension or response.cols != 1:
        raise ValueError("response must be a compatible column")
    if probe is not None and (
        probe.rows != dimension or probe.cols != 1
    ):
        raise ValueError("probe must be a compatible column")
    base_metric = mp.matrix(base_metric)
    update_columns = mp.matrix(update_columns)
    response = mp.matrix(response)
    if probe is not None:
        probe = mp.matrix(probe)
    base_inverse = base_metric**-1
    even_metric = (
        base_metric + update_columns * update_columns.transpose_conj()
    )
    even_inverse = even_metric**-1
    update_rank = update_columns.cols
    ghost_kernel = (
        mp.eye(update_rank)
        + update_columns.transpose_conj()
        * base_inverse
        * update_columns
    )
    ghost_inverse = ghost_kernel**-1
    base_determinant = mp.det(base_metric)
    even_determinant = mp.det(even_metric)
    ghost_determinant = mp.det(ghost_kernel)
    superdeterminant = even_determinant / ghost_determinant
    superdeterminant_ratio = superdeterminant / base_determinant

    response_charge = (
        update_columns.transpose_conj() * base_inverse * response
    )
    response_capacity_loss = mp.re(
        (
            response_charge.transpose_conj()
            * ghost_inverse
            * response_charge
        )[0, 0]
    )
    base_response_capacity = mp.re(
        (
            response.transpose_conj()
            * base_inverse
            * response
        )[0, 0]
    )
    even_response_capacity = mp.re(
        (
            response.transpose_conj()
            * even_inverse
            * response
        )[0, 0]
    )
    ghost_response_log_derivative = -response_capacity_loss
    reconstructed_super_response_capacity = (
        even_response_capacity - ghost_response_log_derivative
    )
    result: dict[str, object] = {
        "base_metric": base_metric,
        "update_columns": update_columns,
        "even_metric": even_metric,
        "ghost_kernel": ghost_kernel,
        "base_determinant": base_determinant,
        "even_determinant": even_determinant,
        "ghost_determinant": ghost_determinant,
        "superdeterminant": superdeterminant,
        "superdeterminant_ratio": superdeterminant_ratio,
        "response_charge": response_charge,
        "base_response_capacity": base_response_capacity,
        "even_response_capacity": even_response_capacity,
        "response_capacity_loss": response_capacity_loss,
        "ghost_response_log_derivative": (
            ghost_response_log_derivative
        ),
        "reconstructed_super_response_capacity": (
            reconstructed_super_response_capacity
        ),
    }
    if probe is not None:
        probe_charge = (
            update_columns.transpose_conj() * base_inverse * probe
        )
        probe_capacity_loss = mp.re(
            (
                probe_charge.transpose_conj()
                * ghost_inverse
                * probe_charge
            )[0, 0]
        )
        base_probe_capacity = mp.re(
            (probe.transpose_conj() * base_inverse * probe)[0, 0]
        )
        even_probe_capacity = mp.re(
            (probe.transpose_conj() * even_inverse * probe)[0, 0]
        )
        mixed_capacity_loss = (
            response_charge.transpose_conj()
            * ghost_inverse
            * probe_charge
        )[0, 0]
        base_mixed_capacity = (
            response.transpose_conj() * base_inverse * probe
        )[0, 0]
        even_mixed_capacity = (
            response.transpose_conj() * even_inverse * probe
        )[0, 0]
        ghost_mixed_log_derivative_component = -mixed_capacity_loss
        reconstructed_super_mixed_capacity = (
            even_mixed_capacity
            - ghost_mixed_log_derivative_component
        )
        result.update(
            {
                "probe": probe,
                "probe_charge": probe_charge,
                "base_probe_capacity": base_probe_capacity,
                "even_probe_capacity": even_probe_capacity,
                "probe_capacity_loss": probe_capacity_loss,
                "ghost_probe_log_derivative": -probe_capacity_loss,
                "reconstructed_super_probe_capacity": (
                    even_probe_capacity + probe_capacity_loss
                ),
                "base_mixed_capacity": base_mixed_capacity,
                "even_mixed_capacity": even_mixed_capacity,
                "mixed_capacity_loss": mixed_capacity_loss,
                "ghost_mixed_log_derivative_component": (
                    ghost_mixed_log_derivative_component
                ),
                "reconstructed_super_mixed_capacity": (
                    reconstructed_super_mixed_capacity
                ),
            }
        )
    return result


def primitive_residual_superdeterminant_certificate(
    base_metric: mp.matrix,
    acyclic_columns: mp.matrix,
    primitive_columns: mp.matrix,
    response: mp.matrix,
) -> dict[str, object]:
    """Isolate the determinant left by unpaired primitive completion columns.

    Acyclic columns are paired with their odd charge kernel; primitive
    columns occur only in the even update.  After exact acyclic cancellation,
    the full superdeterminant is det(W) times a positive primitive Schur
    kernel.  Its determinant is one only when the primitive update vanishes.
    """
    if base_metric.rows != base_metric.cols or base_metric.rows < 1:
        raise ValueError("base_metric must be a nonempty square matrix")
    dimension = base_metric.rows
    if acyclic_columns.rows != dimension:
        raise ValueError("acyclic_columns must have compatible rows")
    if primitive_columns.rows != dimension:
        raise ValueError("primitive_columns must have compatible rows")
    if primitive_columns.cols < 1:
        raise ValueError("at least one primitive column is required")
    if response.rows != dimension or response.cols != 1:
        raise ValueError("response must be a compatible column")
    base_metric = mp.matrix(base_metric)
    acyclic_columns = mp.matrix(acyclic_columns)
    primitive_columns = mp.matrix(primitive_columns)
    response = mp.matrix(response)
    base_inverse = base_metric**-1
    acyclic_rank = acyclic_columns.cols
    primitive_rank = primitive_columns.cols
    acyclic_metric = (
        base_metric
        + acyclic_columns * acyclic_columns.transpose_conj()
    )
    acyclic_inverse = acyclic_metric**-1
    full_even_metric = (
        acyclic_metric
        + primitive_columns * primitive_columns.transpose_conj()
    )
    full_even_inverse = full_even_metric**-1
    acyclic_ghost_kernel = (
        mp.eye(acyclic_rank)
        + acyclic_columns.transpose_conj()
        * base_inverse
        * acyclic_columns
    )
    primitive_diagonal_kernel = (
        mp.eye(primitive_rank)
        + primitive_columns.transpose_conj()
        * base_inverse
        * primitive_columns
    )
    acyclic_primitive_coupling = (
        acyclic_columns.transpose_conj()
        * base_inverse
        * primitive_columns
    )
    primitive_residual_kernel = (
        primitive_diagonal_kernel
        - acyclic_primitive_coupling.transpose_conj()
        * (acyclic_ghost_kernel**-1)
        * acyclic_primitive_coupling
    )
    primitive_residual_alternative = (
        mp.eye(primitive_rank)
        + primitive_columns.transpose_conj()
        * acyclic_inverse
        * primitive_columns
    )
    primitive_residual_eigenvalues = mp.eigsy(
        primitive_residual_kernel, eigvals_only=True
    )
    primitive_residual_determinant = mp.det(
        primitive_residual_kernel
    )
    base_determinant = mp.det(base_metric)
    acyclic_ghost_determinant = mp.det(acyclic_ghost_kernel)
    full_even_determinant = mp.det(full_even_metric)
    partially_paired_superdeterminant = (
        full_even_determinant / acyclic_ghost_determinant
    )
    predicted_partially_paired_superdeterminant = (
        base_determinant * primitive_residual_determinant
    )

    base_response_capacity = mp.re(
        (
            response.transpose_conj()
            * base_inverse
            * response
        )[0, 0]
    )
    full_even_response_capacity = mp.re(
        (
            response.transpose_conj()
            * full_even_inverse
            * response
        )[0, 0]
    )
    acyclic_response_charge = (
        acyclic_columns.transpose_conj() * base_inverse * response
    )
    acyclic_response_loss = mp.re(
        (
            acyclic_response_charge.transpose_conj()
            * (acyclic_ghost_kernel**-1)
            * acyclic_response_charge
        )[0, 0]
    )
    primitive_response_charge = (
        primitive_columns.transpose_conj()
        * acyclic_inverse
        * response
    )
    primitive_response_loss = mp.re(
        (
            primitive_response_charge.transpose_conj()
            * (primitive_residual_kernel**-1)
            * primitive_response_charge
        )[0, 0]
    )
    acyclic_ghost_response_log_derivative = -acyclic_response_loss
    primitive_residual_response_log_derivative = (
        -primitive_response_loss
    )
    direct_partial_super_response_capacity = (
        full_even_response_capacity
        - acyclic_ghost_response_log_derivative
    )
    predicted_partial_super_response_capacity = (
        base_response_capacity
        + primitive_residual_response_log_derivative
    )
    return {
        "base_metric": base_metric,
        "acyclic_columns": acyclic_columns,
        "primitive_columns": primitive_columns,
        "acyclic_metric": acyclic_metric,
        "full_even_metric": full_even_metric,
        "acyclic_ghost_kernel": acyclic_ghost_kernel,
        "primitive_diagonal_kernel": primitive_diagonal_kernel,
        "acyclic_primitive_coupling": acyclic_primitive_coupling,
        "primitive_residual_kernel": primitive_residual_kernel,
        "primitive_residual_alternative": (
            primitive_residual_alternative
        ),
        "primitive_residual_eigenvalues": (
            primitive_residual_eigenvalues
        ),
        "primitive_residual_determinant": (
            primitive_residual_determinant
        ),
        "base_determinant": base_determinant,
        "acyclic_ghost_determinant": acyclic_ghost_determinant,
        "full_even_determinant": full_even_determinant,
        "partially_paired_superdeterminant": (
            partially_paired_superdeterminant
        ),
        "predicted_partially_paired_superdeterminant": (
            predicted_partially_paired_superdeterminant
        ),
        "base_response_capacity": base_response_capacity,
        "full_even_response_capacity": full_even_response_capacity,
        "acyclic_response_loss": acyclic_response_loss,
        "primitive_response_loss": primitive_response_loss,
        "acyclic_ghost_response_log_derivative": (
            acyclic_ghost_response_log_derivative
        ),
        "primitive_residual_response_log_derivative": (
            primitive_residual_response_log_derivative
        ),
        "direct_partial_super_response_capacity": (
            direct_partial_super_response_capacity
        ),
        "predicted_partial_super_response_capacity": (
            predicted_partial_super_response_capacity
        ),
    }


def mobius_endpoint_mertens_regression_certificate(
    size: int,
    direction_count: int,
    right_endpoint: int | None = None,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Factor the canonical endpoint leverage through the Mertens current.

    For f_p(n)=(log(n)/log(N))^p(1-log(n)/log(N)), Abel
    summation gives D=-A^*M, where A_{m,p}=f_p(m+1)-f_p(m)
    and M_m=sum_{n<=m} mu(n).  Consequently the canonical spatial
    representative and every weighted-l1 phase are respectively

        v=-W^{-1}A^*M/(M^*AW^{-1}A^*M),
        <q,v>=<M,-AW^{-1}q>/(M^*AW^{-1}A^*M).

    The returned dyadic records split the numerator into exact Mertens
    shell currents; no absolute-value or Cauchy--Schwarz estimate is used.
    """
    if size < 3:
        raise ValueError("size must be at least three")
    if direction_count < 1:
        raise ValueError("direction_count must be positive")
    if right_endpoint is None:
        right_endpoint = size**2
    if right_endpoint < 1:
        raise ValueError("right_endpoint must be positive")

    spatial_data = mobius_endpoint_direction_spatial_gram(
        size, direction_count, 0, right_endpoint
    )
    metric = spatial_data["metric"]
    response = spatial_data["response"]
    metric_inverse = metric**-1
    logarithmic_scale = mp.log(size)

    abel_difference = mp.matrix(size - 1, direction_count)
    for integer in range(1, size):
        left_coordinate = mp.log(integer) / logarithmic_scale
        right_coordinate = mp.log(integer + 1) / logarithmic_scale
        for offset in range(direction_count):
            power = offset + 1
            abel_difference[integer - 1, offset] = (
                right_coordinate**power * (1 - right_coordinate)
                - left_coordinate**power * (1 - left_coordinate)
            )

    mertens_vector = mp.matrix(size - 1, 1)
    mertens_value = mp.mpf("0")
    for integer in range(1, size):
        mertens_value += mobius(integer)
        mertens_vector[integer - 1] = mertens_value

    mertens_response = (
        -abel_difference.transpose_conj() * mertens_vector
    )
    response_residual = response - mertens_response
    regression_energy = mp.re(
        (
            mertens_vector.transpose_conj()
            * abel_difference
            * metric_inverse
            * abel_difference.transpose_conj()
            * mertens_vector
        )[0, 0]
    )
    metric_capacity = mp.re(
        (response.transpose_conj() * metric_inverse * response)[0, 0]
    )
    if metric_capacity <= 0:
        raise ValueError("Mertens response capacity must be positive")
    canonical_representative = (
        metric_inverse * response / metric_capacity
    )
    regression_representative = (
        -metric_inverse
        * abel_difference.transpose_conj()
        * mertens_vector
        / regression_energy
    )

    endpoint_data = endpoint_quadratic_mass(
        direction_count, endpoint_weights
    )
    transform = endpoint_data["transform"]
    weights = endpoint_data["weights"]
    endpoint_coefficients = transform * canonical_representative
    exact_response_leverage_l1 = mp.fsum(
        weights[index] * abs(endpoint_coefficients[index])
        for index in range(direction_count + 1)
    )

    phase_records: list[dict[str, object]] = []
    maximal_phase_absolute = mp.mpf("0")
    maximizing_phase_index = 0
    for tail_signs in itertools.product([-1, 1], repeat=direction_count):
        signs = [mp.mpf("1")] + [mp.mpf(value) for value in tail_signs]
        weighted_signs = mp.matrix(
            [
                weights[index] * signs[index]
                for index in range(direction_count + 1)
            ]
        )
        phase_response = transform.transpose_conj() * weighted_signs
        mertens_current = (
            -abel_difference * metric_inverse * phase_response
        )
        phase_mixed_numerator = mp.re(
            (mertens_vector.transpose_conj() * mertens_current)[0, 0]
        )
        direct_mixed_numerator = mp.re(
            (
                response.transpose_conj()
                * metric_inverse
                * phase_response
            )[0, 0]
        )

        shell_records: list[dict[str, object]] = []
        shell_left = 1
        while shell_left < size:
            shell_right = min(size - 1, 2 * shell_left - 1)
            contribution = mp.fsum(
                mertens_vector[integer - 1]
                * mertens_current[integer - 1]
                for integer in range(shell_left, shell_right + 1)
            )
            shell_records.append(
                {
                    "left": shell_left,
                    "right": shell_right,
                    "contribution": contribution,
                }
            )
            shell_left *= 2
        shell_absolute_sum = mp.fsum(
            abs(record["contribution"]) for record in shell_records
        )
        shell_cancellation_ratio = (
            abs(phase_mixed_numerator) / shell_absolute_sum
            if shell_absolute_sum > 0
            else mp.mpf("0")
        )
        phase_absolute = abs(phase_mixed_numerator)
        if phase_absolute > maximal_phase_absolute:
            maximal_phase_absolute = phase_absolute
            maximizing_phase_index = len(phase_records)
        phase_records.append(
            {
                "signs": signs,
                "phase_response": phase_response,
                "mertens_current": mertens_current,
                "phase_mixed_numerator": phase_mixed_numerator,
                "direct_mixed_numerator": direct_mixed_numerator,
                "shell_records": shell_records,
                "shell_absolute_sum": shell_absolute_sum,
                "shell_cancellation_ratio": shell_cancellation_ratio,
                "phase_leverage": phase_absolute / metric_capacity,
            }
        )

    return {
        "spatial_data": spatial_data,
        "abel_difference": abel_difference,
        "mertens_vector": mertens_vector,
        "mertens_response": mertens_response,
        "response_residual": response_residual,
        "regression_energy": regression_energy,
        "metric_capacity": metric_capacity,
        "canonical_representative": canonical_representative,
        "regression_representative": regression_representative,
        "transform": transform,
        "weights": weights,
        "endpoint_coefficients": endpoint_coefficients,
        "phase_records": phase_records,
        "maximizing_phase_index": maximizing_phase_index,
        "maximizing_phase_record": phase_records[maximizing_phase_index],
        "maximal_phase_absolute": maximal_phase_absolute,
        "polyhedral_regression_leverage": (
            maximal_phase_absolute / metric_capacity
        ),
        "exact_response_leverage_l1": exact_response_leverage_l1,
    }


def mobius_endpoint_sparse_observation_flow_certificate(
    size: int,
    direction_count: int,
    prefix_endpoint: int,
    right_endpoint: int | None = None,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Transport every Mertens phase current to finitely many unit cells.

    The exact spatial Gram is factored as W=O^*O using unit-cell means
    followed by the positive within-cell variance rows.  If P consists of
    the first unit-cell rows and has full column rank, then

        y_q=P(P^*P)^{-1}q,  P^*y_q=q.

    Hence <D,W^{-1}q>=<OW^{-1}D,y_q>.  This is an exact sparse dual-flow
    conservation law, not an upper bound.
    """
    if size < 3:
        raise ValueError("size must be at least three")
    if direction_count < 1:
        raise ValueError("direction_count must be positive")
    if right_endpoint is None:
        right_endpoint = size**2
    if prefix_endpoint < 0 or prefix_endpoint >= right_endpoint:
        raise ValueError(
            "prefix_endpoint must lie in the spatial window"
        )

    mertens_data = mobius_endpoint_mertens_regression_certificate(
        size,
        direction_count,
        right_endpoint=right_endpoint,
        endpoint_weights=endpoint_weights,
    )
    spatial_data = mertens_data["spatial_data"]
    metric = spatial_data["metric"]
    response = spatial_data["response"]
    slopes = spatial_data["slopes"]
    cumulative_charges = spatial_data["cumulative_charges"]
    metric_inverse = metric**-1

    cell_row_count = right_endpoint
    variance_row_count = max(0, right_endpoint - 1)
    observation = mp.matrix(
        cell_row_count + variance_row_count, direction_count
    )
    for column in range(direction_count):
        observation[0, column] = slopes[column]
    for integer in range(1, right_endpoint):
        logarithmic_width = mp.log(mp.mpf(integer + 1) / integer)
        variance_coefficient = (
            mp.mpf(1) / integer
            - mp.mpf(1) / (integer + 1)
            - logarithmic_width**2
        )
        variance_scale = mp.sqrt(max(mp.mpf("0"), variance_coefficient))
        for column in range(direction_count):
            charge = cumulative_charges[column][integer]
            observation[integer, column] = (
                slopes[column] - logarithmic_width * charge
            )
            observation[
                cell_row_count + integer - 1, column
            ] = variance_scale * charge

    observation_metric = observation.transpose_conj() * observation
    observation_metric_residual = metric - observation_metric
    prefix_row_count = prefix_endpoint + 1
    prefix_observation = observation[:prefix_row_count, :]
    prefix_metric = (
        prefix_observation.transpose_conj() * prefix_observation
    )
    if abs(mp.det(prefix_metric)) <= mp.eps:
        raise ValueError("prefix unit-cell observations do not span")
    prefix_metric_inverse = prefix_metric**-1

    response_flow = observation * metric_inverse * response
    response_flow_energy = mp.re(
        (response_flow.transpose_conj() * response_flow)[0, 0]
    )
    prefix_response_energy = mp.fsum(
        abs(response_flow[index]) ** 2
        for index in range(prefix_row_count)
    )

    phase_records: list[dict[str, object]] = []
    for mertens_record in mertens_data["phase_records"]:
        phase_response = mertens_record["phase_response"]
        sparse_flow = (
            prefix_observation
            * prefix_metric_inverse
            * phase_response
        )
        sparse_constraint_residual = (
            prefix_observation.transpose_conj() * sparse_flow
            - phase_response
        )
        sparse_local_contributions = [
            mp.conj(sparse_flow[index]) * response_flow[index]
            for index in range(prefix_row_count)
        ]
        sparse_mixed_numerator = mp.re(
            mp.fsum(sparse_local_contributions)
        )
        minimal_flow = observation * metric_inverse * phase_response
        minimal_flow_norm_squared = mp.re(
            (minimal_flow.transpose_conj() * minimal_flow)[0, 0]
        )
        direct_minimal_flow_norm_squared = mp.re(
            (
                phase_response.transpose_conj()
                * metric_inverse
                * phase_response
            )[0, 0]
        )
        sparse_flow_norm_squared = mp.re(
            (sparse_flow.transpose_conj() * sparse_flow)[0, 0]
        )
        phase_records.append(
            {
                "signs": mertens_record["signs"],
                "phase_response": phase_response,
                "mertens_mixed_numerator": mertens_record[
                    "phase_mixed_numerator"
                ],
                "direct_mixed_numerator": mertens_record[
                    "direct_mixed_numerator"
                ],
                "sparse_flow": sparse_flow,
                "sparse_constraint_residual": (
                    sparse_constraint_residual
                ),
                "sparse_local_contributions": (
                    sparse_local_contributions
                ),
                "sparse_mixed_numerator": sparse_mixed_numerator,
                "minimal_flow": minimal_flow,
                "minimal_flow_norm_squared": (
                    minimal_flow_norm_squared
                ),
                "direct_minimal_flow_norm_squared": (
                    direct_minimal_flow_norm_squared
                ),
                "sparse_flow_norm_squared": sparse_flow_norm_squared,
                "sparse_to_minimal_energy_ratio": (
                    sparse_flow_norm_squared / minimal_flow_norm_squared
                ),
                "phase_leverage": mertens_record["phase_leverage"],
            }
        )

    maximizing_phase_index = mertens_data["maximizing_phase_index"]
    return {
        "mertens_data": mertens_data,
        "observation": observation,
        "observation_metric": observation_metric,
        "observation_metric_residual": observation_metric_residual,
        "cell_row_count": cell_row_count,
        "variance_row_count": variance_row_count,
        "prefix_endpoint": prefix_endpoint,
        "prefix_observation": prefix_observation,
        "prefix_metric": prefix_metric,
        "response_flow": response_flow,
        "response_flow_energy": response_flow_energy,
        "prefix_response_energy": prefix_response_energy,
        "prefix_response_energy_ratio": (
            prefix_response_energy / response_flow_energy
        ),
        "phase_records": phase_records,
        "maximizing_phase_index": maximizing_phase_index,
        "maximizing_phase_record": phase_records[maximizing_phase_index],
        "exact_response_leverage_l1": mertens_data[
            "exact_response_leverage_l1"
        ],
    }


def mobius_endpoint_interpolation_period_certificate(
    size: int,
    direction_count: int,
    squarefree_nodes: list[int] | None = None,
    right_endpoint: int | None = None,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Interpolate endpoint phases from recovered squarefree evaluations.

    If E is the square evaluation matrix recovered from initial unit-cell
    observations and c_q=E^{-*}q, then q^*v=c_q^*Ev for every coefficient
    vector v.  Applied to the canonical representative, this identifies
    the global Mertens mixed current with a finite signed interpolation
    period.  The recovery operator also gives an explicit incidence cycle.
    """
    if right_endpoint is None:
        right_endpoint = size**2
    recovery = mobius_cell_vandermonde_recovery_certificate(
        size,
        direction_count,
        squarefree_nodes,
        endpoint_weights,
    )
    mertens_data = mobius_endpoint_mertens_regression_certificate(
        size,
        direction_count,
        right_endpoint=right_endpoint,
        endpoint_weights=endpoint_weights,
    )
    evaluation = recovery["recovered_vandermonde"]
    evaluation_inverse_transpose = (
        evaluation.transpose_conj()**-1
    )
    canonical_representative = mertens_data[
        "canonical_representative"
    ]
    metric_capacity = mertens_data["metric_capacity"]
    node_values = evaluation * canonical_representative
    recovery_operator = recovery["recovery_operator"]
    cell_matrix = recovery["cell_matrix"]
    metric_inverse = mertens_data["spatial_data"]["metric"] ** -1
    response = mertens_data["spatial_data"]["response"]
    prefix_response_flow = cell_matrix * metric_inverse * response
    prefix_metric = cell_matrix.transpose_conj() * cell_matrix
    prefix_metric_inverse = prefix_metric**-1

    phase_records: list[dict[str, object]] = []
    maximal_phase_leverage = mp.mpf("0")
    maximizing_phase_index = 0
    for mertens_record in mertens_data["phase_records"]:
        phase_response = mertens_record["phase_response"]
        interpolation_coefficients = (
            evaluation_inverse_transpose * phase_response
        )
        interpolation_contributions = [
            mp.conj(interpolation_coefficients[index])
            * node_values[index]
            for index in range(direction_count)
        ]
        normalized_interpolation_period = mp.re(
            mp.fsum(interpolation_contributions)
        )
        direct_normalized_period = mp.re(
            (
                phase_response.transpose_conj()
                * canonical_representative
            )[0, 0]
        )
        interpolation_absolute_sum = mp.fsum(
            abs(value) for value in interpolation_contributions
        )
        interpolation_cancellation_ratio = (
            abs(normalized_interpolation_period)
            / interpolation_absolute_sum
            if interpolation_absolute_sum > 0
            else mp.mpf("0")
        )
        interpolation_coefficient_norm = mp.sqrt(
            mp.fsum(
                abs(interpolation_coefficients[index]) ** 2
                for index in range(direction_count)
            )
        )
        node_value_norm = mp.sqrt(
            mp.fsum(
                abs(node_values[index]) ** 2
                for index in range(direction_count)
            )
        )
        interpolation_cauchy_upper = (
            interpolation_coefficient_norm * node_value_norm
        )
        highest_evaluation_column_norm = mp.sqrt(
            mp.fsum(
                abs(evaluation[index, direction_count - 1]) ** 2
                for index in range(direction_count)
            )
        )
        highest_coordinate_lower = (
            abs(phase_response[direction_count - 1])
            / highest_evaluation_column_norm
            if highest_evaluation_column_norm > 0
            else mp.inf
        )

        incidence_cycle = (
            recovery_operator.transpose_conj()
            * interpolation_coefficients
        )
        incidence_constraint_residual = (
            cell_matrix.transpose_conj() * incidence_cycle
            - phase_response
        )
        incidence_mixed_numerator = mp.re(
            (
                incidence_cycle.transpose_conj()
                * prefix_response_flow
            )[0, 0]
        )
        prefix_minimal_cycle = (
            cell_matrix * prefix_metric_inverse * phase_response
        )
        incidence_cycle_energy = mp.re(
            (incidence_cycle.transpose_conj() * incidence_cycle)[0, 0]
        )
        prefix_minimal_cycle_energy = mp.re(
            (
                prefix_minimal_cycle.transpose_conj()
                * prefix_minimal_cycle
            )[0, 0]
        )
        phase_leverage = abs(normalized_interpolation_period)
        if phase_leverage > maximal_phase_leverage:
            maximal_phase_leverage = phase_leverage
            maximizing_phase_index = len(phase_records)
        phase_records.append(
            {
                "signs": mertens_record["signs"],
                "phase_response": phase_response,
                "interpolation_coefficients": (
                    interpolation_coefficients
                ),
                "interpolation_contributions": (
                    interpolation_contributions
                ),
                "normalized_interpolation_period": (
                    normalized_interpolation_period
                ),
                "direct_normalized_period": direct_normalized_period,
                "interpolation_absolute_sum": (
                    interpolation_absolute_sum
                ),
                "interpolation_cancellation_ratio": (
                    interpolation_cancellation_ratio
                ),
                "interpolation_coefficient_norm": (
                    interpolation_coefficient_norm
                ),
                "node_value_norm": node_value_norm,
                "interpolation_cauchy_upper": (
                    interpolation_cauchy_upper
                ),
                "highest_coordinate_lower": highest_coordinate_lower,
                "incidence_cycle": incidence_cycle,
                "incidence_constraint_residual": (
                    incidence_constraint_residual
                ),
                "incidence_mixed_numerator": (
                    incidence_mixed_numerator
                ),
                "mertens_mixed_numerator": mertens_record[
                    "phase_mixed_numerator"
                ],
                "prefix_minimal_cycle": prefix_minimal_cycle,
                "incidence_cycle_energy": incidence_cycle_energy,
                "prefix_minimal_cycle_energy": (
                    prefix_minimal_cycle_energy
                ),
                "incidence_to_prefix_minimal_energy_ratio": (
                    incidence_cycle_energy
                    / prefix_minimal_cycle_energy
                ),
                "phase_leverage": phase_leverage,
            }
        )

    return {
        "recovery": recovery,
        "mertens_data": mertens_data,
        "evaluation": evaluation,
        "node_values": node_values,
        "prefix_response_flow": prefix_response_flow,
        "phase_records": phase_records,
        "maximizing_phase_index": maximizing_phase_index,
        "maximizing_phase_record": phase_records[maximizing_phase_index],
        "maximal_phase_leverage": maximal_phase_leverage,
        "exact_response_leverage_l1": mertens_data[
            "exact_response_leverage_l1"
        ],
        "metric_capacity": metric_capacity,
    }


def positive_rank_update_diagonal_susceptibility_certificate(
    base_metric: mp.matrix,
    response: mp.matrix,
    update_columns: mp.matrix,
    update_weights: list[mp.mpf],
    completion_metric: mp.matrix,
    step: mp.mpf,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Bound a three-capacity probe using only diagonal charge energies."""
    step = mp.mpf(step)
    if step <= 0:
        raise ValueError("step must be positive")
    plus = positive_rank_update_response_kernel_certificate(
        base_metric + step * completion_metric,
        response,
        update_columns,
        update_weights,
        endpoint_weights,
    )
    minus = positive_rank_update_response_kernel_certificate(
        base_metric - step * completion_metric,
        response,
        update_columns,
        update_weights,
        endpoint_weights,
    )
    endpoint_capacity = endpoint_polarization_alignment_certificate(
        base_metric, response, endpoint_weights
    )["endpoint_capacity"]
    exact_centered_excess = (
        endpoint_capacity
        * (
            plus["direct_updated_inverse_capacity"]
            - minus["direct_updated_inverse_capacity"]
        )
        / (2 * step)
    )
    diagonal_centered_excess_lower = max(
        mp.mpf("0"),
        endpoint_capacity
        * (
            plus["inverse_capacity_lower"]
            - minus["inverse_capacity_upper"]
        )
        / (2 * step),
    )
    diagonal_centered_excess_upper = (
        endpoint_capacity
        * (
            plus["inverse_capacity_upper"]
            - minus["inverse_capacity_lower"]
        )
        / (2 * step)
    )
    return {
        "step": step,
        "completion_metric": completion_metric,
        "plus": plus,
        "minus": minus,
        "endpoint_capacity": endpoint_capacity,
        "exact_centered_excess": exact_centered_excess,
        "diagonal_centered_excess_lower": (
            diagonal_centered_excess_lower
        ),
        "diagonal_centered_excess_upper": (
            diagonal_centered_excess_upper
        ),
    }


def mobius_unit_cell_tail_projection_certificate(
    size: int,
    direction_count: int,
    cutoff: int,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Certify an N-uniform O(1/M) tail after M exact unit cells."""
    right_endpoint = size**2
    if cutoff < 2 or cutoff >= right_endpoint:
        raise ValueError("cutoff must satisfy 2 <= cutoff < size^2")
    frame = endpoint_spatial_block_wedge_certificate(
        size,
        direction_count,
        0,
        right_endpoint,
        list(range(right_endpoint + 1)),
        endpoint_weights,
    )
    spatial_data = frame["spatial_data"]
    projected_metric = frame["projected_metric"]
    head_error_metric = mp.matrix(direction_count, direction_count)
    tail_error_metric = mp.matrix(direction_count, direction_count)
    head_charge_vectors: list[mp.matrix] = []
    head_variance_weights: list[mp.mpf] = []
    tail_rho_values: list[mp.mpf] = []
    for integer in range(1, right_endpoint):
        charge_vector = mp.matrix(
            [
                spatial_data["cumulative_charges"][row][integer]
                for row in range(direction_count)
            ]
        )
        logarithmic_width = mp.log(mp.mpf(integer + 1) / integer)
        variance_coefficient = (
            mp.mpf(1) / integer
            - mp.mpf(1) / (integer + 1)
            - logarithmic_width**2
        )
        contribution = (
            variance_coefficient
            * charge_vector
            * charge_vector.transpose_conj()
        )
        if integer < cutoff:
            head_error_metric += contribution
            head_charge_vectors.append(charge_vector)
            head_variance_weights.append(variance_coefficient)
        else:
            tail_error_metric += contribution
            tail_rho_values.append(
                variance_coefficient / logarithmic_width**2
            )
    head_metric = projected_metric + head_error_metric
    head_update_columns = mp.matrix(direction_count, len(head_charge_vectors))
    for column, charge_vector in enumerate(head_charge_vectors):
        for row in range(direction_count):
            head_update_columns[row, column] = charge_vector[row]
    head_kernel_certificate = (
        positive_rank_update_response_kernel_certificate(
            projected_metric,
            spatial_data["response"],
            head_update_columns,
            head_variance_weights,
            endpoint_weights,
        )
    )
    actual_metric = spatial_data["metric"]
    finite_tail_frame_bound = 2 * mp.fsum(tail_rho_values)
    uniform_tail_frame_bound = (
        mp.mpf(7)
        / (3 * mp.pi**2)
        / (cutoff - 1)
    )
    tail_majorant = uniform_tail_frame_bound * head_metric
    tail_stability = endpoint_projection_alignment_stability_certificate(
        actual_metric,
        head_metric,
        spatial_data["response"],
        tail_majorant,
        endpoint_weights=endpoint_weights,
    )
    head_alignment = tail_stability["projected"]
    actual_alignment = tail_stability["actual"]
    null_dimension = max(0, direction_count - 1)
    if null_dimension == 0:
        null_relative_eigenvalues = mp.matrix(0, 1)
        shorted_relative_eigenvalues = mp.matrix(0, 1)
    else:
        head_null_cholesky = mp.cholesky(head_alignment["null_metric"])
        inverse_head_null_cholesky = head_null_cholesky**-1
        null_relative_eigenvalues = mp.eigsy(
            inverse_head_null_cholesky
            * actual_alignment["null_metric"]
            * inverse_head_null_cholesky.transpose_conj(),
            eigvals_only=True,
        )
        head_shorted_cholesky = mp.cholesky(
            head_alignment["shorted_null_metric"]
        )
        inverse_head_shorted_cholesky = head_shorted_cholesky**-1
        shorted_relative_eigenvalues = mp.eigsy(
            inverse_head_shorted_cholesky
            * actual_alignment["shorted_null_metric"]
            * inverse_head_shorted_cholesky.transpose_conj(),
            eigvals_only=True,
        )
    inverse_capacity_ratio = (
        tail_stability["actual_inverse_capacity"]
        / tail_stability["projected_inverse_capacity"]
    )
    null_coercivity_ratio = (
        actual_alignment["null_coercivity"]
        / head_alignment["null_coercivity"]
        if null_dimension > 0
        else mp.mpf("1")
    )
    shorted_coercivity_ratio = (
        actual_alignment["shorted_coercivity"]
        / head_alignment["shorted_coercivity"]
        if null_dimension > 0
        else mp.mpf("1")
    )
    return {
        "size": size,
        "direction_count": direction_count,
        "cutoff": cutoff,
        "frame": frame,
        "projected_metric": projected_metric,
        "head_error_metric": head_error_metric,
        "head_charge_vectors": head_charge_vectors,
        "head_variance_weights": head_variance_weights,
        "head_update_columns": head_update_columns,
        "head_kernel_certificate": head_kernel_certificate,
        "tail_error_metric": tail_error_metric,
        "head_metric": head_metric,
        "actual_metric": actual_metric,
        "tail_rho_values": tail_rho_values,
        "finite_tail_frame_bound": finite_tail_frame_bound,
        "uniform_tail_frame_bound": uniform_tail_frame_bound,
        "tail_majorant": tail_majorant,
        "tail_stability": tail_stability,
        "inverse_capacity_ratio": inverse_capacity_ratio,
        "null_relative_eigenvalues": null_relative_eigenvalues,
        "shorted_relative_eigenvalues": shorted_relative_eigenvalues,
        "null_coercivity_ratio": null_coercivity_ratio,
        "shorted_coercivity_ratio": shorted_coercivity_ratio,
    }


def endpoint_spatial_shell_coercivity(
    size: int,
    direction_count: int,
    shell_endpoints: list[int],
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Generalized endpoint coercivity and rotation gain across spatial shells."""
    if len(shell_endpoints) < 2:
        raise ValueError("at least two shell endpoints are required")
    if shell_endpoints[0] != 0:
        raise ValueError("shell endpoints must start at zero")
    if any(
        left >= right
        for left, right in zip(shell_endpoints, shell_endpoints[1:])
    ):
        raise ValueError("shell endpoints must be strictly increasing")
    endpoint_data = endpoint_quadratic_mass(
        direction_count, endpoint_weights
    )
    endpoint_mass = endpoint_data["mass"]
    mass_cholesky = mp.cholesky(endpoint_mass)
    inverse_mass_cholesky = mass_cholesky**-1

    def coercivity(metric: mp.matrix) -> tuple[mp.matrix, mp.matrix]:
        compact = (
            inverse_mass_cholesky
            * metric
            * inverse_mass_cholesky.transpose_conj()
        )
        return mp.eigsy(compact)

    shell_metrics: list[mp.matrix] = []
    shell_coercivities: list[mp.mpf] = []
    total_metric = mp.matrix(direction_count, direction_count)
    response = None
    for left, right in zip(shell_endpoints, shell_endpoints[1:]):
        shell = mobius_endpoint_direction_spatial_gram(
            size, direction_count, left, right
        )
        shell_metric = shell["metric"]
        shell_metrics.append(shell_metric)
        total_metric += shell_metric
        if response is None:
            response = shell["response"]
        eigenvalues, _ = coercivity(shell_metric)
        shell_coercivities.append(
            max(mp.mpf("0"), mp.re(eigenvalues[0]))
        )
    total_eigenvalues, total_eigenvectors = coercivity(total_metric)
    total_coercivity = mp.re(total_eigenvalues[0])
    if total_coercivity <= 0:
        raise ValueError("total spatial metric must be endpoint-coercive")
    additive_coercivity = mp.fsum(shell_coercivities)
    rotation_gain = total_coercivity - additive_coercivity
    tolerance = mp.eps * max(1, abs(total_coercivity)) * 100
    if -tolerance <= rotation_gain < 0:
        rotation_gain = mp.mpf("0")
    if rotation_gain < 0:
        raise ValueError("shell coercivity violated superadditivity")

    lowest_compact_vector = mp.matrix(
        [total_eigenvectors[row, 0] for row in range(direction_count)]
    )
    worst_direction = (
        inverse_mass_cholesky.transpose_conj()
        * lowest_compact_vector
    )
    worst_endpoint_mass = mp.re(
        (
            worst_direction.transpose_conj()
            * endpoint_mass
            * worst_direction
        )[0, 0]
    )
    worst_shell_energies = [
        mp.re(
            (
                worst_direction.transpose_conj()
                * shell_metric
                * worst_direction
            )[0, 0]
        )
        for shell_metric in shell_metrics
    ]
    response_certificate = endpoint_riesz_projection_certificate(
        total_metric,
        response,
        mp.mpf("1"),
        endpoint_weights=endpoint_weights,
    )
    normalized_response = response_certificate["alphas"]
    response_endpoint_l2 = mp.sqrt(
        mp.re(
            (
                normalized_response.transpose_conj()
                * endpoint_mass
                * normalized_response
            )[0, 0]
        )
    )
    response_endpoint_l2_upper = mp.sqrt(
        1
        / (
            total_coercivity
            * response_certificate["capacity"]
        )
    )
    response_endpoint_l1_upper = (
        mp.sqrt(direction_count + 1) * response_endpoint_l2_upper
    )
    transformed_response = inverse_mass_cholesky * response
    spectral_response = (
        total_eigenvectors.transpose_conj() * transformed_response
    )
    spectral_capacity = mp.fsum(
        abs(spectral_response[index]) ** 2
        / total_eigenvalues[index]
        for index in range(direction_count)
    )
    spectral_endpoint_l2_squared = (
        mp.fsum(
            abs(spectral_response[index]) ** 2
            / total_eigenvalues[index] ** 2
            for index in range(direction_count)
        )
        / spectral_capacity**2
    )
    capacity_contributions = [
        abs(spectral_response[index]) ** 2
        / total_eigenvalues[index]
        / spectral_capacity
        for index in range(direction_count)
    ]
    endpoint_l2_contributions = [
        (
            abs(spectral_response[index]) ** 2
            / total_eigenvalues[index] ** 2
        )
        / (
            spectral_endpoint_l2_squared * spectral_capacity**2
        )
        for index in range(direction_count)
    ]
    alignment = endpoint_polarization_alignment_certificate(
        total_metric, response, endpoint_weights
    )
    null_basis = alignment["null_basis"]
    endpoint_representative = alignment["endpoint_representative"]
    shell_null_metrics: list[mp.matrix] = []
    shell_null_couplings: list[mp.matrix] = []
    shell_response_line_energies: list[mp.mpf] = []
    shell_shorted_null_metrics: list[mp.matrix] = []
    shell_shorted_coercivities: list[mp.mpf] = []
    if direction_count == 1:
        coupling_cancellation_ratio = mp.mpf("0")
        additive_shorted_coercivity = mp.inf
        shorted_dispersion_matrix = mp.matrix(0, 0)
        shorted_dispersion_coercivity = mp.inf
        shorted_superadditive_gain = mp.mpf("0")
        shorted_rotation_gain = mp.mpf("0")
    else:
        null_endpoint_mass = alignment["null_endpoint_mass"]
        null_endpoint_cholesky = mp.cholesky(null_endpoint_mass)
        inverse_null_endpoint_cholesky = (
            null_endpoint_cholesky**-1
        )

        def null_coercivity(metric: mp.matrix) -> mp.mpf:
            compact = (
                inverse_null_endpoint_cholesky
                * metric
                * inverse_null_endpoint_cholesky.transpose_conj()
            )
            eigenvalues = mp.eigsy(compact, eigvals_only=True)
            return max(mp.mpf("0"), mp.re(eigenvalues[0]))

        for shell_metric in shell_metrics:
            shell_null_metric = (
                null_basis.transpose_conj()
                * shell_metric
                * null_basis
            )
            shell_null_coupling = (
                null_basis.transpose_conj()
                * shell_metric
                * endpoint_representative
            )
            shell_response_line_energy = mp.re(
                (
                    endpoint_representative.transpose_conj()
                    * shell_metric
                    * endpoint_representative
                )[0, 0]
            )
            shell_null_metrics.append(shell_null_metric)
            shell_null_couplings.append(shell_null_coupling)
            shell_response_line_energies.append(
                shell_response_line_energy
            )
            if shell_response_line_energy > 0:
                shell_shorted_null_metric = (
                    shell_null_metric
                    - shell_null_coupling
                    * shell_null_coupling.transpose_conj()
                    / shell_response_line_energy
                )
            else:
                shell_shorted_null_metric = shell_null_metric
            shell_shorted_null_metrics.append(
                shell_shorted_null_metric
            )
            shell_shorted_coercivities.append(
                null_coercivity(shell_shorted_null_metric)
            )
        total_coupling_norm = mp.sqrt(
            mp.fsum(
                abs(alignment["null_coupling"][row]) ** 2
                for row in range(direction_count - 1)
            )
        )
        absolute_shell_coupling_mass = mp.fsum(
            mp.sqrt(
                mp.fsum(
                    abs(coupling[row]) ** 2
                    for row in range(direction_count - 1)
                )
            )
            for coupling in shell_null_couplings
        )
        coupling_cancellation_ratio = (
            total_coupling_norm / absolute_shell_coupling_mass
            if absolute_shell_coupling_mass > 0
            else mp.mpf("0")
        )
        summed_shell_shorts = mp.matrix(
            direction_count - 1, direction_count - 1
        )
        for shell_shorted_null_metric in shell_shorted_null_metrics:
            summed_shell_shorts += shell_shorted_null_metric
        shorted_dispersion_matrix = (
            alignment["shorted_null_metric"] - summed_shell_shorts
        )
        shorted_dispersion_coercivity = null_coercivity(
            shorted_dispersion_matrix
        )
        additive_shorted_coercivity = mp.fsum(
            shell_shorted_coercivities
        )
        shorted_superadditive_gain = (
            alignment["shorted_coercivity"]
            - additive_shorted_coercivity
        )
        shorted_tolerance = (
            mp.eps
            * max(1, abs(alignment["shorted_coercivity"]))
            * 100
        )
        if -shorted_tolerance <= shorted_superadditive_gain < 0:
            shorted_superadditive_gain = mp.mpf("0")
        if shorted_superadditive_gain < 0:
            raise ValueError(
                "shell shorted coercivity violated superadditivity"
            )
        shorted_rotation_gain = (
            shorted_superadditive_gain
            - shorted_dispersion_coercivity
        )
        if -shorted_tolerance <= shorted_rotation_gain < 0:
            shorted_rotation_gain = mp.mpf("0")
        if shorted_rotation_gain < 0:
            raise ValueError(
                "shorted dispersion and rotation gains exceeded total"
            )
    return {
        "endpoint_mass": endpoint_mass,
        "weights": endpoint_data["weights"],
        "transform": endpoint_data["transform"],
        "shell_metrics": shell_metrics,
        "total_metric": total_metric,
        "shell_coercivities": shell_coercivities,
        "additive_coercivity": additive_coercivity,
        "total_coercivity": total_coercivity,
        "total_generalized_eigenvalues": total_eigenvalues,
        "total_generalized_eigenvectors": total_eigenvectors,
        "rotation_gain": rotation_gain,
        "worst_direction": worst_direction,
        "worst_endpoint_mass": worst_endpoint_mass,
        "worst_shell_energies": worst_shell_energies,
        "response": response,
        "capacity": response_certificate["capacity"],
        "response_leverage_l1": response_certificate["response_leverage"],
        "response_leverage_l2": response_endpoint_l2,
        "response_leverage_l2_upper": response_endpoint_l2_upper,
        "response_leverage_l1_upper": response_endpoint_l1_upper,
        "spectral_response": spectral_response,
        "spectral_capacity": spectral_capacity,
        "spectral_endpoint_l2_squared": spectral_endpoint_l2_squared,
        "capacity_contributions": capacity_contributions,
        "endpoint_l2_contributions": endpoint_l2_contributions,
        "alignment_certificate": alignment,
        "shell_null_metrics": shell_null_metrics,
        "shell_null_couplings": shell_null_couplings,
        "shell_response_line_energies": shell_response_line_energies,
        "shell_shorted_null_metrics": shell_shorted_null_metrics,
        "shell_shorted_coercivities": shell_shorted_coercivities,
        "additive_shorted_coercivity": additive_shorted_coercivity,
        "shorted_dispersion_matrix": shorted_dispersion_matrix,
        "shorted_dispersion_coercivity": shorted_dispersion_coercivity,
        "shorted_superadditive_gain": shorted_superadditive_gain,
        "shorted_rotation_gain": shorted_rotation_gain,
        "coupling_cancellation_ratio": coupling_cancellation_ratio,
    }


def nyman_endpoint_periodic_sandwich_certificate(
    size: int,
    direction_count: int,
    far_lower_constant: mp.mpf = mp.mpf(1) / 9,
    far_upper_constant: mp.mpf = mp.mpf(10) / 3,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Two-sided periodic Loewner sandwich for the infinite response leverage."""
    far_lower_constant = mp.mpf(far_lower_constant)
    far_upper_constant = mp.mpf(far_upper_constant)
    if far_lower_constant <= 0:
        raise ValueError("far_lower_constant must be positive")
    if far_upper_constant < far_lower_constant:
        raise ValueError("far_upper_constant must dominate far_lower_constant")
    spatial = mobius_endpoint_direction_spatial_gram(
        size, direction_count, 0, size**2
    )
    periodic = mobius_endpoint_direction_periodic_gram(
        size, direction_count
    )
    lower_metric = (
        spatial["metric"]
        + far_lower_constant / size**2 * periodic["metric"]
    )
    upper_metric = (
        spatial["metric"]
        + far_upper_constant / size**2 * periodic["metric"]
    )
    endpoint_data = endpoint_quadratic_mass(
        direction_count, endpoint_weights
    )
    endpoint_mass = endpoint_data["mass"]
    mass_cholesky = mp.cholesky(endpoint_mass)
    inverse_mass_cholesky = mass_cholesky**-1
    lower_compact = (
        inverse_mass_cholesky
        * lower_metric
        * inverse_mass_cholesky.transpose_conj()
    )
    lower_generalized_eigenvalues = mp.eigsy(
        lower_compact, eigvals_only=True
    )
    lower_coercivity = mp.re(lower_generalized_eigenvalues[0])
    if lower_coercivity <= 0:
        raise ValueError("lower sandwich metric must be endpoint-coercive")
    lower_certificate = endpoint_riesz_projection_certificate(
        lower_metric,
        spatial["response"],
        mp.mpf("1"),
        endpoint_weights=endpoint_weights,
    )
    upper_certificate = endpoint_riesz_projection_certificate(
        upper_metric,
        spatial["response"],
        mp.mpf("1"),
        endpoint_weights=endpoint_weights,
    )
    quadratic_response_leverage_upper = mp.sqrt(
        (direction_count + 1)
        / (lower_coercivity * upper_certificate["capacity"])
    )
    phase_box_response_leverage_upper = mp.sqrt(
        lower_certificate["phase_box_majorant"]
        / upper_certificate["capacity"]
    )
    return {
        "spatial_metric": spatial["metric"],
        "periodic_metric": periodic["metric"],
        "response": spatial["response"],
        "lower_metric": lower_metric,
        "upper_metric": upper_metric,
        "far_lower_constant": far_lower_constant,
        "far_upper_constant": far_upper_constant,
        "lower_coercivity": lower_coercivity,
        "lower_generalized_eigenvalues": lower_generalized_eigenvalues,
        "lower_capacity": lower_certificate["capacity"],
        "upper_capacity": upper_certificate["capacity"],
        "quadratic_response_leverage_upper": quadratic_response_leverage_upper,
        "phase_box_response_leverage_upper": phase_box_response_leverage_upper,
        "lower_certificate": lower_certificate,
        "upper_certificate": upper_certificate,
    }


def localized_endpoint_riesz_leverage_certificate(
    easy_metric: mp.matrix,
    hard_metric: mp.matrix,
    response: mp.matrix,
    endpoint_weights: list[mp.mpf] | None = None,
) -> dict[str, object]:
    """Two-sided localized bound for the full response-aligned leverage."""
    if easy_metric.rows != easy_metric.cols or easy_metric.rows < 1:
        raise ValueError("easy_metric must be a nonempty square matrix")
    if hard_metric.rows != easy_metric.rows or hard_metric.cols != easy_metric.cols:
        raise ValueError("hard_metric must have the same shape as easy_metric")
    dimension = easy_metric.rows
    if response.rows != dimension or response.cols != 1:
        raise ValueError("response must be a compatible column")
    easy_metric = mp.matrix(easy_metric)
    hard_metric = mp.matrix(hard_metric)
    cholesky = mp.cholesky(easy_metric)
    inverse_cholesky = cholesky**-1
    relative_hard = (
        inverse_cholesky
        * hard_metric
        * inverse_cholesky.transpose_conj()
    )
    relative_eigenvalues = mp.eigsy(relative_hard, eigvals_only=True)
    tolerance = mp.eps * max(
        1, max(abs(relative_eigenvalues[index]) for index in range(dimension))
    ) * 50
    if relative_eigenvalues[0] < -tolerance:
        raise ValueError("hard_metric must be positive semidefinite")
    relative_leakage = max(
        mp.mpf("0"), mp.re(relative_eigenvalues[dimension - 1])
    )
    easy = endpoint_riesz_projection_certificate(
        easy_metric,
        response,
        mp.mpf("1"),
        endpoint_weights=endpoint_weights,
    )
    full = endpoint_riesz_projection_certificate(
        easy_metric + hard_metric,
        response,
        mp.mpf("1"),
        endpoint_weights=endpoint_weights,
    )
    localized_upper_bound = mp.sqrt(
        (1 + relative_leakage)
        * easy["phase_box_majorant"]
        / easy["capacity"]
    )
    return {
        "relative_leakage": relative_leakage,
        "relative_eigenvalues": relative_eigenvalues,
        "easy_capacity": easy["capacity"],
        "full_capacity": full["capacity"],
        "easy_phase_box_majorant": easy["phase_box_majorant"],
        "full_response_leverage": full["response_leverage"],
        "localized_upper_bound": localized_upper_bound,
        "easy_certificate": easy,
        "full_certificate": full,
    }


def polynomial_conductor_amplitude_via_riesz(
    size: int,
    denominator: int,
    polynomial_coefficients: list[mp.mpf],
) -> mp.mpf:
    """Exact conductor amplitude of mu(n)P(log(n)/log(N)) via Riesz moments."""
    if size < 2:
        raise ValueError("size must be at least two")
    if denominator < 1 or denominator > size:
        raise ValueError("denominator must lie between one and size")
    mobius_denominator = mobius(denominator)
    if mobius_denominator == 0:
        return mp.mpf("0")
    endpoint_data = endpoint_polynomial_riesz_data(
        polynomial_coefficients
    )
    endpoint_coefficients = endpoint_data["endpoint_coefficients"]
    ratio = mp.mpf(size) / denominator
    logarithmic_scale = mp.log(size)
    return mobius_denominator * mp.fsum(
        endpoint_coefficients[power]
        / logarithmic_scale**power
        * coprime_mobius_logarithmic_riesz_moment(
            ratio, denominator, power
        )
        for power in range(1, len(endpoint_coefficients))
    )


def reduced_cosecant_square_sum(modulus: int) -> mp.mpf:
    """Exact sum of csc(pi*c/q)^2 over reduced nonzero residues c mod q."""
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    return (
        mp.mpf(modulus**2)
        / 3
        * reduced_denominator_density(modulus)
    )


def shortest_farey_kernel_row_sum(
    lower_left: int, upper_left: int, right_denominator: int
) -> dict[str, mp.mpf | int]:
    """Sum U_(a,b)(1) over a in an interval and its inverse-residue bound."""
    if lower_left < 2 or upper_left < lower_left:
        raise ValueError("left interval must contain integers at least two")
    if right_denominator <= 1:
        raise ValueError("right denominator must exceed one")
    actual = mp.fsum(
        coprime_farey_harmonic_reciprocity(
            left_denominator, right_denominator, 1
        )["correlation"]
        for left_denominator in range(lower_left, upper_left + 1)
        if math.gcd(left_denominator, right_denominator) == 1
    )
    interval_length = upper_left - lower_left + 1
    maximum_residue_multiplicity = (
        interval_length + right_denominator - 1
    ) // right_denominator
    upper_bound = (
        2
        * mp.pi**2
        / (lower_left * right_denominator)
        * maximum_residue_multiplicity
        * reduced_cosecant_square_sum(right_denominator)
    )
    return {
        "actual_sum": actual,
        "upper_bound": upper_bound,
        "maximum_residue_multiplicity": maximum_residue_multiplicity,
    }


def squarefree_shared_gcd_allowed_residues(
    shared_gcd: int,
    left_quotient: int,
    right_quotient: int,
    reduced_determinant: int,
) -> list[int]:
    """Allowed t mod g for primitive fractions with r=g*a and r'=g*b."""
    g = shared_gcd
    a = left_quotient
    b = right_quotient
    delta = reduced_determinant
    if min(g, a, b) < 1:
        raise ValueError("gcd and quotients must be positive")
    if mobius(g) == 0:
        raise ValueError("shared_gcd must be squarefree")
    if math.gcd(g, a * b) != 1 or math.gcd(a, b) != 1:
        raise ValueError("g, a, and b must be pairwise coprime")
    if delta == 0 or math.gcd(abs(delta), a * b) != 1:
        raise ValueError("determinant must be nonzero and coprime to a*b")
    if a <= 1 or b <= 1:
        raise ValueError("generic implementation requires a,b>1")
    initial_left = delta * pow(b, -1, a) % a
    initial_right = (b * initial_left - delta) // a
    return [
        residue
        for residue in range(g)
        if math.gcd(initial_left + a * residue, g) == 1
        and math.gcd(initial_right + b * residue, g) == 1
    ]


def squarefree_shared_gcd_primitive_correlation(
    shared_gcd: int,
    left_quotient: int,
    right_quotient: int,
    reduced_determinant: int,
) -> dict[str, object]:
    """Exact primitive harmonic correlation as cotangent sums over t mod g."""
    g = shared_gcd
    a = left_quotient
    b = right_quotient
    delta = reduced_determinant
    allowed = squarefree_shared_gcd_allowed_residues(g, a, b, delta)
    initial_left = delta * pow(b, -1, a) % a
    initial_right = (b * initial_left - delta) // a
    correlation = mp.fsum(
        mp.pi
        / (g * delta)
        * (
            mp.cot(
                mp.pi * (initial_right + b * residue) / (b * g)
            )
            - mp.cot(
                mp.pi * (initial_left + a * residue) / (a * g)
            )
        )
        for residue in allowed
    )
    return {
        "allowed_residues": allowed,
        "allowed_count": len(allowed),
        "correlation": correlation,
    }


def beurling_periodic_piecewise_energy(
    mollifier_coefficients: list[mp.mpf],
) -> mp.mpf:
    """Direct one-period mean square, intended for exact small-N checks."""
    if len(mollifier_coefficients) < 2:
        raise ValueError("mollifier must contain indices zero and one")
    size = len(mollifier_coefficients) - 1
    period = math.lcm(*range(1, size + 1))
    slope = mp.fsum(
        mollifier_coefficients[index] / index
        for index in range(1, size + 1)
    )
    energy = mp.mpf("0")
    for integer in range(period):
        right_limit = 1 + mp.fsum(
            mollifier_coefficients[index]
            * mp.mpf(integer % index)
            / index
            for index in range(1, size + 1)
        )
        energy += (
            abs(right_limit) ** 2
            + mp.re(right_limit * mp.conj(slope))
            + abs(slope) ** 2 / 3
        )
    return energy / period


def linear_mollifier_periodic_mean_via_mertens(size: int) -> mp.mpf:
    """Mean of the periodic linear-mollifier boundary field via Mertens sums."""
    if size < 2:
        raise ValueError("size must be at least two")
    mertens_value = 0
    weighted_integral = mp.mpf("0")
    for integer in range(1, size):
        mertens_value += mobius(integer)
        weighted_integral += mertens_value * mp.log(
            mp.mpf(integer + 1) / integer
        )
    return 1 + weighted_integral / (2 * mp.log(size))


def mean_zero_quadratic_mobius_mollifier(size: int) -> dict[str, object]:
    """Endpoint-vanishing quadratic mollifier with zero periodic mean.

    The polynomial is 1-u+alpha*u*(1-u).  The construction fails only if
    the single scalar correction direction has zero coefficient sum.
    """
    if size < 2:
        raise ValueError("size must be at least two")
    logarithmic_scale = mp.log(size)
    linear_sum = mp.fsum(
        mobius(integer)
        * (1 - mp.log(integer) / logarithmic_scale)
        for integer in range(1, size + 1)
    )
    correction_sum = mp.fsum(
        mobius(integer)
        * (mp.log(integer) / logarithmic_scale)
        * (1 - mp.log(integer) / logarithmic_scale)
        for integer in range(1, size + 1)
    )
    if correction_sum == 0:
        raise ValueError("quadratic correction has zero coefficient sum")
    alpha = -(linear_sum + 2) / correction_sum
    coefficients = polynomial_mobius_mollifier_coefficients(
        size, [1, alpha - 1, -alpha]
    )
    return {
        "alpha": alpha,
        "linear_sum": linear_sum,
        "correction_sum": correction_sum,
        "coefficients": coefficients,
    }


def mobius_endpoint_direction_response_via_mertens(
    size: int, power: int
) -> mp.mpf:
    """Exact Abel sum of sum mu(n) u_n^power (1-u_n)."""
    if size < 2:
        raise ValueError("size must be at least two")
    if power < 1:
        raise ValueError("power must be positive")
    logarithmic_scale = mp.log(size)

    def endpoint_weight(integer: int) -> mp.mpf:
        coordinate = mp.log(integer) / logarithmic_scale
        return coordinate**power * (1 - coordinate)

    mertens_value = 0
    response = mp.mpf("0")
    for integer in range(1, size):
        mertens_value += mobius(integer)
        response += mertens_value * (
            endpoint_weight(integer) - endpoint_weight(integer + 1)
        )
    return response


def minimum_metric_mean_zero_mobius_mollifier(
    size: int,
    direction_count: int,
    metric: mp.matrix | None = None,
) -> dict[str, object]:
    """Minimum-metric endpoint-preserving correction with zero periodic mean.

    Correction directions are mu(n) u_n^j(1-u_n), 1<=j<=direction_count.
    The default metric is Euclidean on direction coefficients; callers may
    supply a positive-definite Hodge Gram in the direction basis.
    """
    if size < 2:
        raise ValueError("size must be at least two")
    if direction_count < 1:
        raise ValueError("direction_count must be positive")
    if metric is None:
        metric = mp.eye(direction_count)
    if metric.rows != direction_count or metric.cols != direction_count:
        raise ValueError("metric dimension must equal direction_count")
    metric = mp.matrix(metric)
    metric_inverse = metric**-1
    logarithmic_scale = mp.log(size)
    base = polynomial_mobius_mollifier_coefficients(size, [1, -1])
    directions: list[list[mp.mpf]] = []
    responses = mp.matrix(direction_count, 1)
    for offset in range(direction_count):
        power = offset + 1
        direction = [mp.mpf("0")] * (size + 1)
        for integer in range(1, size + 1):
            coordinate = mp.log(integer) / logarithmic_scale
            direction[integer] = (
                mobius(integer)
                * coordinate**power
                * (1 - coordinate)
            )
        directions.append(direction)
        responses[offset] = mp.fsum(direction[1:])

    response_capacity = mp.re(
        (responses.transpose_conj() * metric_inverse * responses)[0, 0]
    )
    if response_capacity <= 0:
        raise ValueError("correction space has zero mean-response capacity")
    target_response = -2 - mp.fsum(base[1:])
    alphas = (
        target_response / response_capacity * metric_inverse * responses
    )
    corrected = list(base)
    for offset, direction in enumerate(directions):
        for integer in range(1, size + 1):
            corrected[integer] += alphas[offset] * direction[integer]

    polynomial_coefficients = [mp.mpf("0")] * (direction_count + 2)
    polynomial_coefficients[0] = 1
    polynomial_coefficients[1] = -1 + alphas[0]
    for degree in range(2, direction_count + 1):
        polynomial_coefficients[degree] = (
            alphas[degree - 1] - alphas[degree - 2]
        )
    polynomial_coefficients[direction_count + 1] = -alphas[direction_count - 1]
    correction_energy = abs(target_response) ** 2 / response_capacity
    return {
        "coefficients": corrected,
        "polynomial_coefficients": polynomial_coefficients,
        "directions": directions,
        "responses": responses,
        "alphas": alphas,
        "response_capacity": response_capacity,
        "target_response": target_response,
        "correction_energy": correction_energy,
        "metric": metric,
    }


def constrained_hodge_projection(
    metric: mp.matrix,
    base_coupling: mp.matrix,
    base_energy: mp.mpf,
    response: mp.matrix,
    target_response: mp.mpf,
) -> dict[str, object]:
    """Minimize E0+2 Re(h*alpha)+alpha*W alpha subject to D*alpha=t."""
    if metric.rows != metric.cols or metric.rows < 1:
        raise ValueError("metric must be a nonempty square matrix")
    dimension = metric.rows
    if base_coupling.rows != dimension or base_coupling.cols != 1:
        raise ValueError("base_coupling must be a compatible column")
    if response.rows != dimension or response.cols != 1:
        raise ValueError("response must be a compatible column")
    metric_inverse = metric**-1
    capacity = mp.re(
        (response.transpose_conj() * metric_inverse * response)[0, 0]
    )
    if capacity <= 0:
        raise ValueError("response capacity must be positive")
    unconstrained = -metric_inverse * base_coupling
    response_residual = (
        target_response
        + (response.transpose_conj() * metric_inverse * base_coupling)[0, 0]
    )
    coefficients = (
        unconstrained
        + response_residual / capacity * metric_inverse * response
    )
    unconstrained_energy = mp.re(
        base_energy
        - (
            base_coupling.transpose_conj()
            * metric_inverse
            * base_coupling
        )[0, 0]
    )
    constrained_energy = (
        unconstrained_energy + abs(response_residual) ** 2 / capacity
    )
    direct_energy = mp.re(
        base_energy
        + 2 * (base_coupling.transpose_conj() * coefficients)[0, 0]
        + (
            coefficients.transpose_conj() * metric * coefficients
        )[0, 0]
    )
    return {
        "coefficients": coefficients,
        "capacity": capacity,
        "response_residual": response_residual,
        "unconstrained_coefficients": unconstrained,
        "unconstrained_energy": unconstrained_energy,
        "constrained_energy": constrained_energy,
        "direct_energy": direct_energy,
    }


def nested_response_capacity_update(
    core_metric: mp.matrix,
    core_response: mp.matrix,
    coupling: mp.matrix,
    complement_metric: mp.mpf,
    complement_response: mp.mpf,
) -> dict[str, mp.mpf]:
    """One-direction Feshbach increment of D*W^{-1}D."""
    if core_metric.rows != core_metric.cols or core_metric.rows < 1:
        raise ValueError("core_metric must be a nonempty square matrix")
    dimension = core_metric.rows
    if core_response.rows != dimension or core_response.cols != 1:
        raise ValueError("core_response must be a compatible column")
    if coupling.rows != dimension or coupling.cols != 1:
        raise ValueError("coupling must be a compatible column")
    core_inverse = core_metric**-1
    core_capacity = mp.re(
        (core_response.transpose_conj() * core_inverse * core_response)[0, 0]
    )
    schur_gap = mp.re(
        complement_metric
        - (coupling.transpose_conj() * core_inverse * coupling)[0, 0]
    )
    if schur_gap <= 0:
        raise ValueError("complement Schur gap must be positive")
    effective_response = (
        complement_response
        - (coupling.transpose_conj() * core_inverse * core_response)[0, 0]
    )
    increment = abs(effective_response) ** 2 / schur_gap
    return {
        "core_capacity": core_capacity,
        "schur_gap": schur_gap,
        "effective_response": effective_response,
        "capacity_increment": increment,
        "enlarged_capacity": core_capacity + increment,
    }


def nested_constrained_hodge_update(
    core_metric: mp.matrix,
    core_coupling: mp.matrix,
    core_response: mp.matrix,
    base_energy: mp.mpf,
    target_response: mp.mpf,
    new_metric: mp.mpf,
    new_core_coupling: mp.matrix,
    new_base_coupling: mp.mpf,
    new_response: mp.mpf,
) -> dict[str, mp.mpf]:
    """Exact energy gain after adjoining one constrained Hodge direction."""
    if core_metric.rows != core_metric.cols or core_metric.rows < 1:
        raise ValueError("core_metric must be a nonempty square matrix")
    dimension = core_metric.rows
    for vector, name in (
        (core_coupling, "core_coupling"),
        (core_response, "core_response"),
        (new_core_coupling, "new_core_coupling"),
    ):
        if vector.rows != dimension or vector.cols != 1:
            raise ValueError(f"{name} must be a compatible column")
    core_inverse = core_metric**-1
    capacity = mp.re(
        (core_response.transpose_conj() * core_inverse * core_response)[0, 0]
    )
    if capacity <= 0:
        raise ValueError("core response capacity must be positive")
    schur_gap = mp.re(
        new_metric
        - (
            new_core_coupling.transpose_conj()
            * core_inverse
            * new_core_coupling
        )[0, 0]
    )
    if schur_gap <= 0:
        raise ValueError("new-direction Schur gap must be positive")
    effective_response = (
        new_response
        - (
            new_core_coupling.transpose_conj()
            * core_inverse
            * core_response
        )[0, 0]
    )
    effective_coupling = (
        new_base_coupling
        - (
            new_core_coupling.transpose_conj()
            * core_inverse
            * core_coupling
        )[0, 0]
    )
    response_residual = (
        target_response
        + (
            core_response.transpose_conj()
            * core_inverse
            * core_coupling
        )[0, 0]
    )
    core_projection = constrained_hodge_projection(
        core_metric,
        core_coupling,
        base_energy,
        core_response,
        target_response,
    )
    enlarged_capacity = capacity + abs(effective_response) ** 2 / schur_gap
    enlarged_unconstrained_energy = (
        core_projection["unconstrained_energy"]
        - abs(effective_coupling) ** 2 / schur_gap
    )
    enlarged_response_residual = (
        response_residual
        + mp.conj(effective_response)
        * effective_coupling
        / schur_gap
    )
    enlarged_energy = (
        enlarged_unconstrained_energy
        + abs(enlarged_response_residual) ** 2 / enlarged_capacity
    )
    energy_gain = abs(
        capacity * effective_coupling
        - effective_response * response_residual
    ) ** 2 / (
        capacity
        * (capacity * schur_gap + abs(effective_response) ** 2)
    )
    return {
        "capacity": capacity,
        "schur_gap": schur_gap,
        "effective_response": effective_response,
        "effective_coupling": effective_coupling,
        "response_residual": response_residual,
        "enlarged_capacity": enlarged_capacity,
        "core_constrained_energy": core_projection["constrained_energy"],
        "enlarged_constrained_energy": enlarged_energy,
        "energy_gain": energy_gain,
    }


def quadratic_hodge_energy(
    metric: mp.matrix,
    coupling: mp.matrix,
    base_energy: mp.mpf,
    coefficients: mp.matrix,
) -> mp.mpf:
    """Evaluate E0+2 Re(h*alpha)+alpha*W alpha."""
    if metric.rows != metric.cols or metric.rows < 1:
        raise ValueError("metric must be a nonempty square matrix")
    dimension = metric.rows
    if coupling.rows != dimension or coupling.cols != 1:
        raise ValueError("coupling must be a compatible column")
    if coefficients.rows != dimension or coefficients.cols != 1:
        raise ValueError("coefficients must be a compatible column")
    return mp.re(
        base_energy
        + 2 * (coupling.transpose_conj() * coefficients)[0, 0]
        + (coefficients.transpose_conj() * metric * coefficients)[0, 0]
    )


def easy_hard_constrained_hodge_certificate(
    easy_metric: mp.matrix,
    easy_coupling: mp.matrix,
    easy_base_energy: mp.mpf,
    hard_metric: mp.matrix,
    hard_coupling: mp.matrix,
    hard_base_energy: mp.mpf,
    response: mp.matrix,
    target_response: mp.mpf,
) -> dict[str, object]:
    """Use the easy-block constrained optimizer as a full-energy trial vector."""
    easy_projection = constrained_hodge_projection(
        easy_metric,
        easy_coupling,
        easy_base_energy,
        response,
        target_response,
    )
    coefficients = easy_projection["coefficients"]
    hard_leakage = quadratic_hodge_energy(
        hard_metric,
        hard_coupling,
        hard_base_energy,
        coefficients,
    )
    candidate_energy = easy_projection["constrained_energy"] + hard_leakage
    combined_projection = constrained_hodge_projection(
        easy_metric + hard_metric,
        easy_coupling + hard_coupling,
        easy_base_energy + hard_base_energy,
        response,
        target_response,
    )
    return {
        "coefficients": coefficients,
        "easy_energy": easy_projection["constrained_energy"],
        "hard_leakage": hard_leakage,
        "candidate_energy": candidate_energy,
        "combined_optimal_energy": combined_projection["constrained_energy"],
        "certificate_slack": (
            candidate_energy - combined_projection["constrained_energy"]
        ),
    }


def exterior_power_matrix(operator: mp.matrix, degree: int) -> mp.matrix:
    """Matrix of the degree-th exterior power in the ordered wedge basis."""
    if operator.rows != operator.cols or operator.rows < 1:
        raise ValueError("operator must be a nonempty square matrix")
    dimension = operator.rows
    if degree < 0 or degree > dimension:
        raise ValueError("degree must lie between zero and the dimension")
    if degree == 0:
        return mp.matrix([[1]])
    index_sets = list(itertools.combinations(range(dimension), degree))
    compound = mp.zeros(len(index_sets), len(index_sets))
    for row, row_indices in enumerate(index_sets):
        for column, column_indices in enumerate(index_sets):
            minor = mp.matrix(
                [
                    [operator[left, right] for right in column_indices]
                    for left in row_indices
                ]
            )
            compound[row, column] = mp.det(minor)
    return compound


def endpoint_orbit_metric(operator: mp.matrix, power: int) -> mp.matrix:
    """Positive endpoint metric (U^power)^* U^power."""
    if operator.rows != operator.cols or operator.rows < 1:
        raise ValueError("operator must be a nonempty square matrix")
    if power < 0:
        raise ValueError("power must be nonnegative")
    iterate = operator**power
    return iterate.transpose_conj() * iterate


def thresholded_endpoint_inertia(
    operator: mp.matrix,
    power: int,
    epsilon: mp.mpf,
) -> tuple[int, int]:
    """Counts endpoint singular values above/below exponential thresholds."""
    epsilon = mp.mpf(epsilon)
    if epsilon < 0:
        raise ValueError("epsilon must be nonnegative")
    metric = endpoint_orbit_metric(operator, power)
    numeric = np.array(
        [
            [complex(metric[row, column]) for column in range(metric.cols)]
            for row in range(metric.rows)
        ],
        dtype=np.complex128,
    )
    eigenvalues = np.linalg.eigvalsh(numeric)
    upper = float(mp.e ** (2 * epsilon * power))
    lower = float(mp.e ** (-2 * epsilon * power))
    return (
        int(np.count_nonzero(eigenvalues > upper)),
        int(np.count_nonzero(eigenvalues < lower)),
    )


def spectral_atom_from_couplings(couplings: mp.matrix) -> mp.matrix:
    """Positive matrix-valued spectral atom C C^* from channel couplings."""
    if couplings.rows < 1 or couplings.cols < 1:
        raise ValueError("couplings must be a nonempty matrix")
    return couplings * couplings.transpose_conj()


def coherent_scalar_spectral_atom(
    feature: mp.matrix,
    multiplicity: int,
) -> mp.matrix:
    """Scalar-channel atom when multiplicity enters as one coherent residue."""
    if feature.cols != 1 or feature.rows < 1:
        raise ValueError("feature must be a nonempty column vector")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    amplitude = multiplicity * feature
    return amplitude * amplitude.transpose_conj()


def recover_integer_spectral_multiplicity(
    atom_weight: mp.mpf,
    feature_norm_squared: mp.mpf,
    tolerance: mp.mpf = mp.mpf("1e-20"),
) -> int:
    """Recover m from an atom weight m^2 times a known feature norm."""
    atom_weight = mp.mpf(atom_weight)
    feature_norm_squared = mp.mpf(feature_norm_squared)
    tolerance = mp.mpf(tolerance)
    if atom_weight <= 0 or feature_norm_squared <= 0:
        raise ValueError("weights and feature norm must be positive")
    if tolerance <= 0:
        raise ValueError("tolerance must be positive")
    candidate = mp.sqrt(atom_weight / feature_norm_squared)
    multiplicity = int(mp.nint(candidate))
    if multiplicity < 1 or abs(candidate - multiplicity) > tolerance * max(
        1, abs(candidate)
    ):
        raise ValueError("normalized atom weight is not an integer square")
    return multiplicity


def finite_tracial_spectral_determinant(
    point: mp.mpc,
    spectral_points: list[mp.mpc],
    trace_weights: list[int],
) -> mp.mpc:
    """Finite tracial determinant product (point-rho)^tau(P_rho)."""
    if len(spectral_points) != len(trace_weights):
        raise ValueError("spectral points and trace weights must have equal length")
    value = mp.mpc("1")
    for spectral_point, trace_weight in zip(spectral_points, trace_weights):
        if not isinstance(trace_weight, int):
            raise ValueError("trace weights must be integers")
        value *= (point - spectral_point) ** trace_weight
    return value


def finite_tracial_log_derivative(
    point: mp.mpc,
    spectral_points: list[mp.mpc],
    trace_weights: list[int],
) -> mp.mpc:
    """Log derivative of the finite tracial spectral determinant."""
    if len(spectral_points) != len(trace_weights):
        raise ValueError("spectral points and trace weights must have equal length")
    return mp.fsum(
        trace_weight / (point - spectral_point)
        for spectral_point, trace_weight in zip(spectral_points, trace_weights)
    )


def power_prefix_hodge_kernel(
    size: int,
    center_exponent: mp.mpf,
) -> mp.matrix:
    """Finite max Green matrix for the power-weighted prefix flow."""
    if size < 1:
        raise ValueError("size must be positive")
    center_exponent = mp.mpf(center_exponent)
    if center_exponent <= 0:
        raise ValueError("center_exponent must be positive")
    boundary = mp.mpf(size + 1) ** (-center_exponent)
    return mp.matrix(
        [
            [
                (
                    mp.mpf(max(left + 1, right + 1)) ** (-center_exponent)
                    - boundary
                )
                / center_exponent
                for right in range(size)
            ]
            for left in range(size)
        ]
    )


def power_prefix_dual_laplacian(
    size: int,
    center_exponent: mp.mpf,
) -> mp.matrix:
    """Inverse Jacobi matrix of the finite prefix Hodge Green kernel."""
    if size < 1:
        raise ValueError("size must be positive")
    center_exponent = mp.mpf(center_exponent)
    if center_exponent <= 0:
        raise ValueError("center_exponent must be positive")
    inverse_weights = []
    for index in range(1, size + 1):
        weight = (
            mp.mpf(index) ** (-center_exponent)
            - mp.mpf(index + 1) ** (-center_exponent)
        ) / center_exponent
        inverse_weights.append(1 / weight)
    difference = mp.zeros(size, size)
    for index in range(size):
        difference[index, index] = 1
        if index > 0:
            difference[index, index - 1] = -1
    return difference * mp.diag(inverse_weights) * difference.transpose_conj()


def chebyshev_abel_energy_dirichlet(
    endpoint: int, sigma: mp.mpf
) -> mp.mpf:
    """Finite renormalized max-kernel formula from Theorem EU."""
    if endpoint < 2:
        raise ValueError("endpoint must be at least 2")
    sigma = mp.mpf(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    exponent = 2 * sigma
    psi_value = mp.mpf("0")
    square_sum = mp.mpf("0")
    linear_sum = mp.mpf("0")
    for integer in range(2, endpoint):
        previous_psi = psi_value
        mangoldt = von_mangoldt(integer)
        psi_value += mangoldt
        square_increment = psi_value**2 - previous_psi**2
        square_sum += square_increment / mp.mpf(integer) ** (exponent + 1)
        linear_sum += mangoldt / mp.mpf(integer) ** exponent
    renormalized_square = (
        square_sum - psi_value**2 * mp.mpf(endpoint) ** (-exponent - 1)
    )
    renormalized_linear = (
        linear_sum - psi_value * mp.mpf(endpoint) ** (-exponent)
    )
    if abs(exponent - 1) < mp.mpf("1e-40"):
        continuous = mp.log(endpoint)
    else:
        continuous = (
            mp.mpf(endpoint) ** (1 - exponent) - 1
        ) / (1 - exponent)
    return (
        exponent / (exponent + 1) * renormalized_square
        - 2 * renormalized_linear
        + exponent * continuous
    )


def max_kernel_matrix(points, sigma: mp.mpf, center: mp.mpf = 1) -> mp.matrix:
    """Green matrix K_(c,sigma) from Theorems EZ and FE."""
    values = [mp.mpf(point) for point in points]
    sigma = mp.mpf(sigma)
    center = mp.mpf(center)
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    if center + 2 * sigma <= 0:
        raise ValueError("center + 2 sigma must be positive")
    if any(value < 1 for value in values):
        raise ValueError("all points must be at least 1")
    exponent = center + 2 * sigma
    coefficient = 2 * sigma / exponent
    return mp.matrix(
        [
            [
                coefficient * max(left, right) ** (-exponent)
                for right in values
            ]
            for left in values
        ]
    )


def finite_max_kernel_matrix(
    points,
    endpoint: mp.mpf,
    sigma: mp.mpf,
    center: mp.mpf = 1,
) -> mp.matrix:
    """Finite-interval Green matrix K^X from Proposition FD."""
    values = [mp.mpf(point) for point in points]
    endpoint = mp.mpf(endpoint)
    if any(value < 1 or value > endpoint for value in values):
        raise ValueError("points must lie in [1, endpoint]")
    infinite = max_kernel_matrix(values, sigma, center)
    exponent = mp.mpf(center) + 2 * mp.mpf(sigma)
    correction = (
        2 * mp.mpf(sigma) / exponent * endpoint ** (-exponent)
    )
    return infinite - correction * mp.ones(len(values), len(values))


def max_kernel_trace(sigma: mp.mpf, center: mp.mpf = 1) -> mp.mpf:
    """Trace of the general Green operator when it is trace class."""
    sigma = mp.mpf(sigma)
    center = mp.mpf(center)
    exponent = center + 2 * sigma
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    if exponent <= 1:
        raise ValueError("trace class requires center + 2 sigma > 1")
    return 2 * sigma / (exponent * (exponent - 1))


def max_kernel_eigenvalue(
    index: int, sigma: mp.mpf, center: mp.mpf = 1
) -> mp.mpf:
    """Exact Bessel eigenvalue from Theorems FF and FJ."""
    if index < 1:
        raise ValueError("index must be positive")
    sigma = mp.mpf(sigma)
    center = mp.mpf(center)
    exponent = center + 2 * sigma
    if sigma <= 0 or exponent <= 1:
        raise ValueError("require sigma > 0 and center + 2 sigma > 1")
    order = 1 / (exponent - 1)
    zero = mp.besseljzero(order, index)
    return (exponent - 1) ** 2 * zero**2 / (8 * sigma)


def max_kernel_eigenfunction(
    point: mp.mpf,
    index: int,
    sigma: mp.mpf,
    center: mp.mpf = 1,
) -> mp.mpf:
    """Normalized Bessel eigenfunction from equation (26)."""
    point = mp.mpf(point)
    sigma = mp.mpf(sigma)
    center = mp.mpf(center)
    exponent = center + 2 * sigma
    if point < 1:
        raise ValueError("point must be at least 1")
    if index < 1:
        raise ValueError("index must be positive")
    if sigma <= 0 or exponent <= 1:
        raise ValueError("require sigma > 0 and center + 2 sigma > 1")
    order = 1 / (exponent - 1)
    zero = mp.besseljzero(order, index)
    denominator = abs(mp.besselj(order + 1, zero))
    normalizer = mp.sqrt(exponent - 1) / denominator
    return (
        normalizer
        * point ** (-exponent / 2)
        * mp.besselj(
            order + 1,
            zero * point ** (-(exponent - 1) / 2),
        )
    )


def chebyshev_bessel_coefficient(
    endpoint: int,
    index: int,
    sigma: mp.mpf,
) -> mp.mpf:
    """Finite Fourier--Bessel coefficient from equation (15)."""
    if endpoint < 2:
        raise ValueError("endpoint must be at least 2")
    if index < 1:
        raise ValueError("index must be positive")
    sigma = mp.mpf(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    order = 1 / (2 * sigma)
    zero = mp.besseljzero(order, index)
    denominator = abs(mp.besselj(order + 1, zero))
    psi_value = mp.mpf("0")
    integral = mp.mpf("0")
    for integer in range(1, endpoint):
        if integer >= 2:
            psi_value += von_mangoldt(integer)
        integral += mp.quad(
            lambda value, current=psi_value: (
                (current - value)
                * value ** (-2 * sigma - mp.mpf("1.5"))
                * mp.besselj(order, zero * value ** (-sigma))
            ),
            [integer, integer + 1],
        )
    return mp.sqrt(2) * sigma / denominator * integral


def twisted_chebyshev_abel_energy(
    endpoint: int,
    sigma: mp.mpf,
    phase,
) -> mp.mpf:
    """Finite complex Euler-current energy for a nonprincipal twist."""
    if endpoint < 2:
        raise ValueError("endpoint must be at least 2")
    sigma = mp.mpf(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    cumulative = mp.mpc("0")
    total = mp.mpf("0")
    exponent = 2 * sigma + 2
    for integer in range(1, endpoint):
        if integer >= 2:
            cumulative += von_mangoldt(integer) * phase(integer)
        total += abs(cumulative) ** 2 * _power_interval_integral(
            mp.mpf(integer), mp.mpf(integer + 1), -exponent
        )
    return 2 * sigma * total


def zeta_bessel_euler_coordinate(
    index: int,
    sigma: mp.mpf,
    series_terms: int = 80,
) -> dict[str, mp.mpf]:
    """Signed Euler--Bessel coordinate and its absolute majorant.

    This is a high-precision exploratory evaluation of equations (3) and
    (7), not a directed truncation enclosure.
    """
    if index < 1:
        raise ValueError("index must be positive")
    if series_terms < 1:
        raise ValueError("series_terms must be positive")
    sigma = mp.mpf(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    order = 1 / (2 * sigma)
    bessel_order = order + 1
    zero = mp.besseljzero(order, index)
    normalizer = mp.sqrt(2 * sigma) / abs(
        mp.besselj(bessel_order, zero)
    )
    signed_sum = mp.mpf("0")
    absolute_sum = mp.mpf("0")
    for term in range(series_terms):
        magnitude = (
            (zero / 2) ** (2 * term + bessel_order)
            / (
                mp.factorial(term)
                * mp.gamma(term + bessel_order + 1)
            )
        )
        sample = 1 + 2 * sigma + 2 * sigma * term
        remainder = (
            -mp.zeta(sample, derivative=1) / mp.zeta(sample)
            - 1 / (sample - 1)
        )
        signed_sum += (-1) ** term * magnitude * remainder
        absolute_sum += magnitude * abs(remainder)
    endpoint_value = normalizer * mp.besselj(bessel_order, zero)
    coordinate = -endpoint_value + normalizer * signed_sum
    majorant = abs(endpoint_value) + normalizer * absolute_sum
    return {
        "coordinate": coordinate,
        "absolute_majorant": majorant,
        "ratio": majorant / max(abs(coordinate), mp.mpf("1e-100")),
    }


def chebyshev_block_variance(start: int) -> mp.mpf:
    """Exact dyadic block variance V(X) by piecewise polynomial integration."""
    if start < 1:
        raise ValueError("start must be positive")
    cumulative = mp.fsum(von_mangoldt(k) for k in range(2, start))
    total = mp.mpf("0")
    for integer in range(start, 2 * start):
        if integer >= 2:
            cumulative += von_mangoldt(integer)
        left = mp.mpf(integer)
        right = mp.mpf(integer + 1)
        total += (
            cumulative**2 * (right - left)
            - cumulative * (right**2 - left**2)
            + (right**3 - left**3) / 3
        )
    return total


def chebyshev_block_variance_max_kernel(start: int) -> mp.mpf:
    """Independent finite tent-kernel expansion from equation (13)."""
    if start < 1:
        raise ValueError("start must be positive")
    x = mp.mpf(start)
    prime_weights = [
        (mp.mpf(integer), von_mangoldt(integer))
        for integer in range(2, 2 * start + 1)
        if von_mangoldt(integer)
    ]
    prime_square = mp.fsum(
        left_weight
        * right_weight
        * max(2 * x - max(x, left, right), mp.mpf("0"))
        for left, left_weight in prime_weights
        for right, right_weight in prime_weights
    )
    cross = mp.fsum(
        weight * (4 * x**2 - max(x, point) ** 2)
        for point, weight in prime_weights
    )
    return prime_square - cross + mp.mpf(7) * x**3 / 3


def _default_block_window(value: mp.mpf) -> mp.mpf:
    """C1 endpoint-vanishing window sin(pi(y-1))^2 on [1, 2]."""
    if value < 1 or value > 2:
        return mp.mpf("0")
    return mp.sin(mp.pi * (value - 1)) ** 2


def chebyshev_windowed_block_energy(start: int) -> mp.mpf:
    """Physical windowed energy X int |w(y)F_X(y)|^2 dy."""
    if start < 1:
        raise ValueError("start must be positive")
    cumulative = mp.fsum(von_mangoldt(k) for k in range(2, start))
    total = mp.mpf("0")
    x = mp.mpf(start)
    for integer in range(start, 2 * start):
        if integer >= 2:
            cumulative += von_mangoldt(integer)
        total += mp.quad(
            lambda value, current=cumulative: (
                _default_block_window(value / x) ** 2
                * (current - value) ** 2
            ),
            [integer, integer + 1],
        )
    return total


def chebyshev_windowed_fourier_coefficient(
    start: int, mode: int
) -> mp.mpc:
    """Fourier coefficient g_hat_X(m) from equation (2)."""
    if start < 1:
        raise ValueError("start must be positive")
    cumulative = mp.fsum(von_mangoldt(k) for k in range(2, start))
    total = mp.mpc("0")
    x = mp.mpf(start)
    for integer in range(start, 2 * start):
        if integer >= 2:
            cumulative += von_mangoldt(integer)
        total += mp.quad(
            lambda value, current=cumulative: (
                _default_block_window(value / x)
                * (current - value)
                * mp.e ** (-2 * mp.pi * mp.j * mode * value / x)
                / x
            ),
            [integer, integer + 1],
        )
    return total


def chebyshev_triangular_discrepancy(start: int) -> mp.mpf:
    """Finite triangular Riesz coefficient A(X), formula (4)."""
    if start < 1:
        raise ValueError("start must be positive")
    x = mp.mpf(start)
    psi_at_x = mp.fsum(von_mangoldt(k) for k in range(2, start + 1))
    upper = mp.fsum(
        von_mangoldt(k) * (2 * x - k)
        for k in range(start + 1, 2 * start + 1)
    )
    return x * psi_at_x + upper - mp.mpf("1.5") * x**2


def chebyshev_triangular_discrepancy_integral(start: int) -> mp.mpf:
    """Independent piecewise integral of psi(x)-x on [X, 2X]."""
    if start < 1:
        raise ValueError("start must be positive")
    cumulative = mp.fsum(von_mangoldt(k) for k in range(2, start))
    total = mp.mpf("0")
    for integer in range(start, 2 * start):
        if integer >= 2:
            cumulative += von_mangoldt(integer)
        left = mp.mpf(integer)
        right = mp.mpf(integer + 1)
        total += cumulative * (right - left) - (right**2 - left**2) / 2
    return total


def chebyshev_primitive_discrepancy(endpoint: mp.mpf) -> mp.mpf:
    """Exact C(X)=integral_1^X (psi(x)-x) dx for real X >= 1."""
    endpoint = mp.mpf(endpoint)
    if endpoint < 1:
        raise ValueError("endpoint must be at least one")
    maximum = int(mp.floor(endpoint))
    prime_part = mp.fsum(
        von_mangoldt(integer) * (endpoint - integer)
        for integer in range(2, maximum + 1)
    )
    return prime_part - (endpoint**2 - 1) / 2


def chebyshev_normalized_primitive(
    log_scale: mp.mpf, center: mp.mpf = mp.mpf("0.5")
) -> mp.mpf:
    """Normalized arithmetic primitive p(t), equation (2) of note 045."""
    log_scale = mp.mpf(log_scale)
    center = mp.mpf(center)
    kappa = center + 1
    endpoint = mp.e**log_scale
    return mp.e ** (-kappa * log_scale) * chebyshev_primitive_discrepancy(
        endpoint
    )


def chebyshev_dilation_riesz_signal(
    log_scale: mp.mpf,
    dilation: mp.mpf = mp.mpf("2"),
    center: mp.mpf = mp.mpf("0.5"),
) -> mp.mpf:
    """Stable dilation difference d_h(t) from equations (3)--(4)."""
    log_scale = mp.mpf(log_scale)
    dilation = mp.mpf(dilation)
    center = mp.mpf(center)
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    kappa = center + 1
    log_dilation = mp.log(dilation)
    return chebyshev_normalized_primitive(
        log_scale + log_dilation, center
    ) - dilation ** (-kappa) * chebyshev_normalized_primitive(
        log_scale, center
    )


def chebyshev_normalized_error(
    log_scale: mp.mpf, center: mp.mpf = mp.mpf("0.5")
) -> mp.mpf:
    """Normalized prime error f(t)=exp(-center*t)(psi(exp(t))-exp(t))."""
    log_scale = mp.mpf(log_scale)
    center = mp.mpf(center)
    endpoint = mp.e**log_scale
    maximum = int(mp.floor(endpoint))
    chebyshev = mp.fsum(
        von_mangoldt(integer) for integer in range(2, maximum + 1)
    )
    return mp.e ** (-center * log_scale) * (chebyshev - endpoint)


def chebyshev_dilation_riesz_signal_derivative(
    log_scale: mp.mpf,
    dilation: mp.mpf = mp.mpf("2"),
    center: mp.mpf = mp.mpf("0.5"),
) -> mp.mpf:
    """A.e. derivative of d_h(t), independently using qE(qX)-E(X)."""
    log_scale = mp.mpf(log_scale)
    dilation = mp.mpf(dilation)
    center = mp.mpf(center)
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    kappa = center + 1
    endpoint = mp.e**log_scale
    upper_endpoint = dilation * endpoint

    maximum = int(mp.floor(endpoint))
    upper_maximum = int(mp.floor(upper_endpoint))
    error = mp.fsum(
        von_mangoldt(integer) for integer in range(2, maximum + 1)
    ) - endpoint
    upper_error = mp.fsum(
        von_mangoldt(integer) for integer in range(2, upper_maximum + 1)
    ) - upper_endpoint
    signal = chebyshev_dilation_riesz_signal(
        log_scale, dilation, center
    )
    return (
        -kappa * signal
        + dilation ** (-kappa)
        * endpoint ** (1 - kappa)
        * (dilation * upper_error - error)
    )


def chebyshev_dilation_quadrature_gram(
    log_times: list[mp.mpf],
    orbit_size: int,
    dilation: mp.mpf = mp.mpf("2"),
    center: mp.mpf = mp.mpf("0.5"),
    weights: list[mp.mpf] | None = None,
) -> mp.matrix:
    """Finite positive quadrature Gram for dilation translates of d_h.

    This is a finite arithmetic audit of equation (11), not an enclosure of
    the infinite Abel integral or its critical tightness.
    """
    if orbit_size < 1:
        raise ValueError("orbit_size must be positive")
    if not log_times:
        raise ValueError("at least one quadrature time is required")
    dilation = mp.mpf(dilation)
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    times = [mp.mpf(value) for value in log_times]
    if any(value < 0 for value in times):
        raise ValueError("quadrature times must be nonnegative")
    if weights is None:
        quadrature_weights = [mp.mpf("1") for _ in times]
    else:
        if len(weights) != len(times):
            raise ValueError("weights and log_times must have equal length")
        quadrature_weights = [mp.mpf(value) for value in weights]
        if any(value < 0 for value in quadrature_weights):
            raise ValueError("quadrature weights must be nonnegative")
    total_weight = mp.fsum(quadrature_weights)
    if total_weight <= 0:
        raise ValueError("quadrature weights must have positive total")

    log_dilation = mp.log(dilation)
    samples = [
        [
            chebyshev_dilation_riesz_signal(
                time + orbit * log_dilation, dilation, center
            )
            for orbit in range(orbit_size)
        ]
        for time in times
    ]
    gram = mp.matrix(orbit_size, orbit_size)
    for left in range(orbit_size):
        for right in range(orbit_size):
            gram[left, right] = mp.fsum(
                weight * row[left] * mp.conj(row[right])
                for weight, row in zip(quadrature_weights, samples)
            ) / total_weight
    return gram


def chebyshev_dilation_sobolev_quadrature_gram(
    log_times: list[mp.mpf],
    orbit_shifts: list[mp.mpf],
    dilation: mp.mpf = mp.mpf("2"),
    center: mp.mpf = mp.mpf("0.5"),
    weights: list[mp.mpf] | None = None,
) -> mp.matrix:
    """Finite positive H1 Gram from equation (9) of note 046."""
    if not log_times:
        raise ValueError("at least one quadrature time is required")
    if not orbit_shifts:
        raise ValueError("at least one orbit shift is required")
    times = [mp.mpf(value) for value in log_times]
    shifts = [mp.mpf(value) for value in orbit_shifts]
    if any(value < 0 for value in times + shifts):
        raise ValueError("times and shifts must be nonnegative")
    if weights is None:
        quadrature_weights = [mp.mpf("1") for _ in times]
    else:
        if len(weights) != len(times):
            raise ValueError("weights and log_times must have equal length")
        quadrature_weights = [mp.mpf(value) for value in weights]
        if any(value < 0 for value in quadrature_weights):
            raise ValueError("quadrature weights must be nonnegative")
    total_weight = mp.fsum(quadrature_weights)
    if total_weight <= 0:
        raise ValueError("quadrature weights must have positive total")

    signal_samples = [
        [
            chebyshev_dilation_riesz_signal(
                time + shift, dilation, center
            )
            for shift in shifts
        ]
        for time in times
    ]
    derivative_samples = [
        [
            chebyshev_dilation_riesz_signal_derivative(
                time + shift, dilation, center
            )
            for shift in shifts
        ]
        for time in times
    ]
    gram = mp.matrix(len(shifts), len(shifts))
    for left in range(len(shifts)):
        for right in range(len(shifts)):
            gram[left, right] = mp.fsum(
                weight
                * (
                    signal_row[left] * mp.conj(signal_row[right])
                    + derivative_row[left]
                    * mp.conj(derivative_row[right])
                )
                for weight, signal_row, derivative_row in zip(
                    quadrature_weights,
                    signal_samples,
                    derivative_samples,
                )
            ) / total_weight
    return gram


def triangular_ratio_profile(
    ratio: mp.mpf, exponent: mp.mpf, dilation: mp.mpf = mp.mpf("2")
) -> mp.mpf:
    """Closed homogeneous profile R_{a,q}(z), Theorem GZ."""
    ratio = mp.mpf(ratio)
    exponent = mp.mpf(exponent)
    dilation = mp.mpf(dilation)
    if ratio <= 0 or ratio > 1:
        raise ValueError("ratio must lie in (0, 1]")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    plateau = (
        (dilation - 1)
        * (dilation ** (exponent + 1) - 1)
        / (exponent * (exponent + 1))
    )
    if ratio <= 1 / dilation:
        return plateau
    return (
        dilation ** (exponent + 2)
        * (exponent + 2 - exponent * ratio)
        / (exponent * (exponent + 1) * (exponent + 2))
        - (dilation - 1) / (exponent * (exponent + 1))
        - dilation
        * ratio ** (-exponent)
        / (exponent * (exponent + 1))
        + ratio ** (-exponent - 1)
        / ((exponent + 1) * (exponent + 2))
    )


def homogeneous_triangular_current_kernel(
    left: mp.mpf,
    right: mp.mpf,
    sigma: mp.mpf,
    dilation: mp.mpf = mp.mpf("2"),
    center: mp.mpf = mp.mpf("0.5"),
) -> mp.mpf:
    """Homogeneous triangular current kernel K^0, equation (3)."""
    left = mp.mpf(left)
    right = mp.mpf(right)
    sigma = mp.mpf(sigma)
    dilation = mp.mpf(dilation)
    center = mp.mpf(center)
    if left <= 0 or right <= 0:
        raise ValueError("kernel arguments must be positive")
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    maximum = max(left, right)
    minimum = min(left, right)
    c = 2 * center
    exponent = c + 2 * sigma
    return (
        2
        * sigma
        * dilation ** (-c - 2)
        * maximum ** (-exponent)
        * triangular_ratio_profile(
            minimum / maximum, exponent, dilation
        )
    )


def triangular_plateau_kernel(
    left: mp.mpf,
    right: mp.mpf,
    sigma: mp.mpf,
    dilation: mp.mpf = mp.mpf("2"),
    center: mp.mpf = mp.mpf("0.5"),
) -> mp.mpf:
    """Plateau max-kernel polarization P, equations (11)--(12)."""
    left = mp.mpf(left)
    right = mp.mpf(right)
    sigma = mp.mpf(sigma)
    dilation = mp.mpf(dilation)
    center = mp.mpf(center)
    if left <= 0 or right <= 0:
        raise ValueError("kernel arguments must be positive")
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    c = 2 * center
    exponent = c + 2 * sigma
    plateau = (
        (dilation - 1)
        * (dilation ** (exponent + 1) - 1)
        / (exponent * (exponent + 1))
    )
    return (
        2
        * sigma
        * dilation ** (-c - 2)
        * plateau
        * max(left, right) ** (-exponent)
    )


def triangular_local_variance_kernel(
    left: mp.mpf,
    right: mp.mpf,
    sigma: mp.mpf,
    dilation: mp.mpf = mp.mpf("2"),
    center: mp.mpf = mp.mpf("0.5"),
) -> mp.mpf:
    """Positive local defect D=P-K^0 from Theorem HA."""
    return triangular_plateau_kernel(
        left, right, sigma, dilation, center
    ) - homogeneous_triangular_current_kernel(
        left, right, sigma, dilation, center
    )


def two_moment_endpoint_core(
    left_endpoint: mp.mpf,
    right_endpoint: mp.mpf,
    exponent: mp.mpf,
    mass: mp.mpf | mp.mpc,
    weighted_mass: mp.mpf | mp.mpc,
) -> tuple[mp.mpf | mp.mpc, mp.mpf | mp.mpc]:
    """Endpoint weights matching mass and u**(-a)-weighted mass."""
    left_endpoint = mp.mpf(left_endpoint)
    right_endpoint = mp.mpf(right_endpoint)
    exponent = mp.mpf(exponent)
    if left_endpoint <= 0 or right_endpoint <= left_endpoint:
        raise ValueError("endpoints must satisfy 0 < left < right")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    denominator = (
        left_endpoint ** (-exponent) - right_endpoint ** (-exponent)
    )
    left_weight = (
        weighted_mass - mass * right_endpoint ** (-exponent)
    ) / denominator
    right_weight = (
        mass * left_endpoint ** (-exponent) - weighted_mass
    ) / denominator
    return left_weight, right_weight


def endpoint_core_toeplitz_parameters(
    exponent: mp.mpf, dilation: mp.mpf = mp.mpf("2")
) -> dict[str, mp.mpf]:
    """AR(1) parameters and spectral margins from Theorem HG."""
    exponent = mp.mpf(exponent)
    dilation = mp.mpf(dilation)
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    plateau = triangular_ratio_profile(
        1 / dilation, exponent, dilation
    )
    diagonal = triangular_ratio_profile(mp.mpf("1"), exponent, dilation)
    eta = 1 - diagonal / plateau
    rho = dilation ** (-exponent / 2)
    return {
        "plateau": plateau,
        "diagonal": diagonal,
        "eta": eta,
        "rho": rho,
        "lower_margin": (1 - rho) / (1 + rho) - eta,
        "upper_margin": (1 + rho) / (1 - rho) - eta,
    }


def critical_zeta_endpoint_core_matrix(size: int) -> mp.matrix:
    """Critical K/(2 sigma) on the dyadic endpoint grid, Theorem HH."""
    if size < 1:
        raise ValueError("size must be positive")
    plateau = mp.mpf("3") / 2
    diagonal = mp.mpf("4") / 3
    factor = mp.mpf("1") / 8
    matrix = mp.matrix(size, size)
    for left in range(size):
        for right in range(size):
            profile = diagonal if left == right else plateau
            matrix[left, right] = (
                factor * profile * mp.power(2, -max(left, right))
            )
    return matrix


def geometric_max_prefix_energy(
    charges: list[mp.mpf | mp.mpc],
    exponent: mp.mpf,
    dilation: mp.mpf = mp.mpf("2"),
) -> mp.mpf:
    """Prefix-square factorization of the geometric max kernel, (2)."""
    if not charges:
        raise ValueError("at least one charge is required")
    exponent = mp.mpf(exponent)
    dilation = mp.mpf(dilation)
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    ratio = dilation ** (-exponent)
    prefix = 0
    total = mp.mpf("0")
    for index, charge in enumerate(charges):
        prefix += charge
        if index + 1 < len(charges):
            total += (
                ratio**index - ratio ** (index + 1)
            ) * abs(prefix) ** 2
        else:
            total += ratio**index * abs(prefix) ** 2
    return total


def chebyshev_log_block_moment(start: mp.mpf) -> mp.mpf:
    """H(L)=integral_L^(2L) (psi(x)-x)/x^2 dx, formula (21)."""
    start = mp.mpf(start)
    if start < 1:
        raise ValueError("start must be positive")
    left = start
    right = 2 * left
    lower_integer = int(mp.floor(left))
    upper_integer = int(mp.floor(right))
    psi_left = mp.fsum(
        von_mangoldt(integer) for integer in range(2, lower_integer + 1)
    )
    upper = mp.fsum(
        von_mangoldt(integer)
        * (1 / mp.mpf(integer) - 1 / right)
        for integer in range(lower_integer + 1, upper_integer + 1)
    )
    return psi_left / (2 * left) + upper - mp.log(2)


def chebyshev_dyadic_core_charge(start: int) -> mp.mpf:
    """Merged critical endpoint charge z(L), formula (20)."""
    if start < 2 or start % 2:
        raise ValueError("start must be a positive even integer")
    left = mp.mpf(start)
    return left * (
        2 * chebyshev_log_block_moment(start)
        - chebyshev_log_block_moment(start // 2)
    )


def chebyshev_prime_wavelet(log_scale: mp.mpf) -> mp.mpf:
    """Continuous normalized wavelet y(t)=exp(-t/2)z(exp(t))."""
    log_scale = mp.mpf(log_scale)
    scale = mp.e**log_scale
    if scale < 2:
        raise ValueError("scale must be at least two")
    charge = scale * (
        2 * chebyshev_log_block_moment(scale)
        - chebyshev_log_block_moment(scale / 2)
    )
    return mp.e ** (-log_scale / 2) * charge


def prime_wavelet_kernel(value: mp.mpf) -> mp.mpf:
    """Compact nonnegative prime-wavelet kernel phi, equation (2)."""
    value = mp.mpf(value)
    if value <= mp.mpf("0.5") or value > 2:
        return mp.mpf("0")
    if value <= 1:
        return 2 - 1 / value
    return 2 / value - 1


def chebyshev_prime_wavelet_local_charge(scale: mp.mpf) -> mp.mpf:
    """Finite local prime formula for z(L), Proposition HS."""
    scale = mp.mpf(scale)
    if scale < 2:
        raise ValueError("scale must be at least two")
    lower = int(mp.floor(scale / 2)) + 1
    upper = int(mp.floor(2 * scale))
    prime_sum = mp.fsum(
        von_mangoldt(integer) * prime_wavelet_kernel(integer / scale)
        for integer in range(max(2, lower), upper + 1)
    )
    return prime_sum - scale * mp.log(2)


def _prime_wavelet_phi_square_integral(
    left: mp.mpf, right: mp.mpf
) -> mp.mpf:
    """Integrate phi(r)^2 exactly between positive endpoints."""
    left = max(mp.mpf(left), mp.mpf("0.5"))
    right = min(mp.mpf(right), mp.mpf("2"))
    if right <= left:
        return mp.mpf("0")

    def lower_antiderivative(value: mp.mpf) -> mp.mpf:
        return 4 * value - 4 * mp.log(value) - 1 / value

    def upper_antiderivative(value: mp.mpf) -> mp.mpf:
        return value - 4 * mp.log(value) - 4 / value

    total = mp.mpf("0")
    if left < 1:
        endpoint = min(right, mp.mpf("1"))
        total += lower_antiderivative(endpoint) - lower_antiderivative(left)
    if right > 1:
        endpoint = max(left, mp.mpf("1"))
        total += upper_antiderivative(right) - upper_antiderivative(endpoint)
    return total


def chebyshev_prime_wavelet_diagonal(start: int) -> mp.mpf:
    """Exact finite diagonal D(X), equation (14)."""
    if start < 2:
        raise ValueError("start must be at least two")
    x = mp.mpf(start)
    lower = int(mp.floor(x / 2)) + 1
    upper = int(mp.floor(4 * x))
    return mp.fsum(
        von_mangoldt(integer) ** 2
        / integer
        * _prime_wavelet_phi_square_integral(
            mp.mpf(integer) / (2 * x), mp.mpf(integer) / x
        )
        for integer in range(max(2, lower), upper + 1)
    )


def chebyshev_prime_wavelet_pair_block(start: int) -> dict[str, mp.mpf]:
    """Finite prime-pair/cross/background expansion of C(X), (12)."""
    if start < 2:
        raise ValueError("start must be at least two")
    x = mp.mpf(start)
    log_two = mp.log(2)
    breakpoints = [mp.mpf(integer) / 2 for integer in range(2 * start, 4 * start + 1)]

    def prime_sum(scale: mp.mpf) -> mp.mpf:
        lower = int(mp.floor(scale / 2)) + 1
        upper = int(mp.floor(2 * scale))
        return mp.fsum(
            von_mangoldt(integer)
            * prime_wavelet_kernel(mp.mpf(integer) / scale)
            for integer in range(max(2, lower), upper + 1)
        )

    prime_pair = mp.mpf("0")
    prime_mean = mp.mpf("0")
    total = mp.mpf("0")
    for left, right in zip(breakpoints[:-1], breakpoints[1:]):
        prime_pair += mp.quad(
            lambda scale: prime_sum(scale) ** 2 / scale**2,
            [left, right],
        )
        prime_mean += mp.quad(
            lambda scale: prime_sum(scale) / scale,
            [left, right],
        )
        total += mp.quad(
            lambda scale: (
                prime_sum(scale) - scale * log_two
            )
            ** 2
            / scale**2,
            [left, right],
        )
    cross = -2 * log_two * prime_mean
    background = log_two**2 * x
    return {
        "total": total,
        "prime_pair": prime_pair,
        "cross": cross,
        "background": background,
        "diagonal": chebyshev_prime_wavelet_diagonal(start),
        "centered_remainder": total
        - chebyshev_prime_wavelet_diagonal(start),
    }


def prime_wavelet_riemann_remainder(scale: mp.mpf) -> mp.mpf:
    """R(L)=sum phi(n/L)-L*log(2), Proposition HY."""
    scale = mp.mpf(scale)
    if scale < 1:
        raise ValueError("scale must be at least one")
    lower = int(mp.floor(scale / 2)) + 1
    upper = int(mp.floor(2 * scale))
    unit_sum = mp.fsum(
        prime_wavelet_kernel(mp.mpf(integer) / scale)
        for integer in range(max(1, lower), upper + 1)
    )
    return unit_sum - scale * mp.log(2)


def chebyshev_prime_wavelet_centered_charge(scale: mp.mpf) -> mp.mpf:
    """Centered coefficient formula sum (Lambda(n)-1) phi(n/L)."""
    scale = mp.mpf(scale)
    if scale < 2:
        raise ValueError("scale must be at least two")
    lower = int(mp.floor(scale / 2)) + 1
    upper = int(mp.floor(2 * scale))
    return mp.fsum(
        (von_mangoldt(integer) - 1)
        * prime_wavelet_kernel(mp.mpf(integer) / scale)
        for integer in range(max(1, lower), upper + 1)
    )


def chebyshev_prime_wavelet_centered_diagonal(start: int) -> mp.mpf:
    """Centered diagonal D_c(X), equation (9) of note 051."""
    if start < 2:
        raise ValueError("start must be at least two")
    x = mp.mpf(start)
    lower = int(mp.floor(x / 2)) + 1
    upper = int(mp.floor(4 * x))
    return mp.fsum(
        (von_mangoldt(integer) - 1) ** 2
        / integer
        * _prime_wavelet_phi_square_integral(
            mp.mpf(integer) / (2 * x), mp.mpf(integer) / x
        )
        for integer in range(max(1, lower), upper + 1)
    )


def prime_wavelet_centered_frame_block(start: int) -> dict[str, mp.mpf]:
    """Centered energy and all-ones generic frame test on one block."""
    if start < 2:
        raise ValueError("start must be at least two")
    x = mp.mpf(start)
    breakpoints = [
        mp.mpf(integer) / 2
        for integer in range(2 * start, 4 * start + 1)
    ]

    def unit_sum(scale: mp.mpf) -> mp.mpf:
        lower = int(mp.floor(scale / 2)) + 1
        upper = int(mp.floor(2 * scale))
        return mp.fsum(
            prime_wavelet_kernel(mp.mpf(integer) / scale)
            for integer in range(max(1, lower), upper + 1)
        )

    centered_energy = mp.fsum(
        mp.quad(
            lambda scale: chebyshev_prime_wavelet_centered_charge(scale) ** 2
            / scale**2,
            [left, right],
        )
        for left, right in zip(breakpoints[:-1], breakpoints[1:])
    )
    unit_energy = mp.fsum(
        mp.quad(
            lambda scale: unit_sum(scale) ** 2 / scale**2,
            [left, right],
        )
        for left, right in zip(breakpoints[:-1], breakpoints[1:])
    )
    unit_diagonal = mp.fsum(
        1
        / integer
        * _prime_wavelet_phi_square_integral(
            mp.mpf(integer) / (2 * x), mp.mpf(integer) / x
        )
        for integer in range(max(1, int(mp.floor(x / 2)) + 1), int(4 * x) + 1)
    )
    return {
        "centered_energy": centered_energy,
        "centered_diagonal": chebyshev_prime_wavelet_centered_diagonal(
            start
        ),
        "arithmetic_rayleigh": centered_energy
        / chebyshev_prime_wavelet_centered_diagonal(start),
        "unit_energy": unit_energy,
        "unit_diagonal": unit_diagonal,
        "generic_rayleigh": unit_energy / unit_diagonal,
    }


def primitive_prime_wavelet_kernel(value: mp.mpf) -> mp.mpf:
    """Degree-zero kernel chi(r)=phi(r)-2*phi(2r), Proposition IE."""
    value = mp.mpf(value)
    if value <= mp.mpf("0.25") or value > 2:
        return mp.mpf("0")
    if value <= mp.mpf("0.5"):
        return 1 / value - 4
    if value <= 1:
        return 4 - 3 / value
    return 2 / value - 1


def prime_wavelet_homogeneous_profile(ratio: mp.mpf) -> mp.mpf:
    """k_phi(q)=integral phi(qr)phi(r)dr for 0<q<=1."""
    ratio = mp.mpf(ratio)
    if ratio <= 0 or ratio > 1:
        raise ValueError("ratio must lie in (0,1]")
    if ratio <= mp.mpf("0.25"):
        return mp.mpf("0")
    if ratio <= mp.mpf("0.5"):
        return (
            -8 * ratio
            + 2
            + (4 * ratio + 1) * mp.log(4 * ratio)
        ) / ratio
    return (
        16 * ratio
        - 10
        - (4 * ratio + 4) * mp.log(2)
        - (8 * ratio + 5) * mp.log(ratio)
    ) / ratio


def primitive_prime_wavelet_homogeneous_profile(ratio: mp.mpf) -> mp.mpf:
    """k_chi(q)=integral chi(qr)chi(r)dr for 0<q<=1."""
    ratio = mp.mpf(ratio)
    if ratio <= 0 or ratio > 1:
        raise ValueError("ratio must lie in (0,1]")
    if ratio <= mp.mpf("0.125"):
        return mp.mpf("0")

    def extended_phi_profile(value: mp.mpf) -> mp.mpf:
        if value <= 1:
            return prime_wavelet_homogeneous_profile(value)
        return prime_wavelet_homogeneous_profile(1 / value) / value

    return (
        3 * extended_phi_profile(ratio)
        - extended_phi_profile(ratio / 2)
        - 2 * extended_phi_profile(2 * ratio)
    )


def primitive_profile_chamber_coefficients(
    ratio: mp.mpf,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """Return (a,b,c,d) with k(q)=a+b log(q)+(c+d log(q))/q."""
    ratio = mp.mpf(ratio)
    if ratio <= 0 or ratio > 1:
        raise ValueError("ratio must lie in (0,1]")
    log_two = mp.log(2)
    if ratio <= mp.mpf("0.125"):
        return (mp.mpf("0"),) * 4
    if ratio <= mp.mpf("0.25"):
        return (
            16 - 24 * log_two,
            mp.mpf("-8"),
            -2 - 3 * log_two,
            mp.mpf("-1"),
        )
    if ratio <= mp.mpf("0.5"):
        return (
            -56 + 48 * log_two,
            mp.mpf("28"),
            16 + 15 * log_two,
            mp.mpf("8"),
        )
    return (
        76 - 18 * log_two,
        mp.mpf("-38"),
        -50 - 18 * log_two,
        mp.mpf("-25"),
    )


def primitive_prime_wavelet_homogeneous_kernel(
    left: mp.mpf, right: mp.mpf
) -> mp.mpf:
    """Full-scale Gram kernel integral_0^infinity chi(m/L)chi(n/L)dL/L^2."""
    left = mp.mpf(left)
    right = mp.mpf(right)
    if left <= 0 or right <= 0:
        raise ValueError("arguments must be positive")
    maximum = max(left, right)
    ratio = min(left, right) / maximum
    return primitive_prime_wavelet_homogeneous_profile(ratio) / maximum


def primitive_homogeneous_moment_energy(
    coefficients: dict[int, complex | mp.mpf | mp.mpc],
) -> mp.mpf:
    """Evaluate the finite homogeneous Gram via four prefix moments.

    This is the single-sum formula of Theorem IN.  It is algebraically
    identical to the direct double Gram sum, but uses only the prefix moments
    of a_m, a_m log(m), a_m/m, and a_m log(m)/m on three ratio chambers.
    """
    indices = sorted(index for index, value in coefficients.items() if value != 0)
    if not indices:
        return mp.mpf("0")
    values = [mp.mpc(coefficients[index]) for index in indices]
    prefix = [[mp.mpc(0)] for _ in range(4)]
    for index, value in zip(indices, values):
        log_index = mp.log(index)
        terms = (
            value,
            value * log_index,
            value / index,
            value * log_index / index,
        )
        for moment, term in zip(prefix, terms):
            moment.append(moment[-1] + term)

    diagonal_mass = 26 - 36 * mp.log(2)
    energy = mp.fsum(
        abs(value) ** 2 * diagonal_mass / index
        for index, value in zip(indices, values)
    )
    chamber_bounds = (
        (mp.mpf("0.125"), mp.mpf("0.25")),
        (mp.mpf("0.25"), mp.mpf("0.5")),
        (mp.mpf("0.5"), mp.mpf("1")),
    )
    cross = mp.mpc(0)
    for position, (index, value) in enumerate(zip(indices, values)):
        log_index = mp.log(index)
        for lower_ratio, upper_ratio in chamber_bounds:
            lower_position = bisect.bisect_right(
                indices, lower_ratio * index, 0, position
            )
            if upper_ratio == 1:
                upper_position = position
            else:
                upper_position = bisect.bisect_right(
                    indices, upper_ratio * index, 0, position
                )
            if upper_position <= lower_position:
                continue
            moments = [
                moment[upper_position] - moment[lower_position]
                for moment in prefix
            ]
            a_value, b_value, c_value, d_value = (
                primitive_profile_chamber_coefficients(upper_ratio)
            )
            inner = (
                ((a_value - b_value * log_index) * moments[0]
                 + b_value * moments[1])
                / index
                + (c_value - d_value * log_index) * moments[2]
                + d_value * moments[3]
            )
            cross += mp.conj(value) * inner
    return mp.re(energy + 2 * cross)


def primitive_centered_homogeneous_block(start: int) -> dict[str, mp.mpf]:
    """Finite four-moment RH block on X/4<n<=4X, Theorem IP."""
    if start < 4:
        raise ValueError("start must be at least four")
    x = mp.mpf(start)
    lower = int(mp.floor(x / 4)) + 1
    upper = int(mp.floor(4 * x))
    coefficients = {
        integer: von_mangoldt(integer) - 1
        for integer in range(max(1, lower), upper + 1)
    }
    energy = primitive_homogeneous_moment_energy(coefficients)
    diagonal_mass = 26 - 36 * mp.log(2)
    diagonal = mp.fsum(
        abs(value) ** 2 * diagonal_mass / integer
        for integer, value in coefficients.items()
    )
    return {
        "energy": energy,
        "diagonal": diagonal,
        "rayleigh": energy / diagonal,
    }


def primitive_prime_wavelet_mellin(value: mp.mpc) -> mp.mpc:
    """Mellin transform integral chi(r) r^(s-1) dr away from s=0,1."""
    value = mp.mpc(value)
    if value == 0 or value == 1:
        raise ValueError("use a limiting value at the removable endpoints")
    return (
        (1 - mp.power(2, 1 - value))
        * (mp.power(2, value) + mp.power(2, 1 - value) - 3)
        / (value * (value - 1))
    )


def primitive_prime_wavelet_spectral_weight(frequency: mp.mpf) -> mp.mpf:
    """Exact critical Mellin weight b(t)^3/(t^2+1/4)^2."""
    frequency = mp.mpf(frequency)
    massive = 3 - 2 * mp.sqrt(2) * mp.cos(frequency * mp.log(2))
    return massive**3 / (frequency**2 + mp.mpf("0.25")) ** 2


def massive_biharmonic_hodge_kernel(
    left: mp.mpf, right: mp.mpf
) -> mp.mpf:
    """Green kernel (2+|log(m/n)|)/max(m,n) of (-d^2+1/4)^-2."""
    left = mp.mpf(left)
    right = mp.mpf(right)
    if left <= 0 or right <= 0:
        raise ValueError("arguments must be positive")
    return (2 + abs(mp.log(left / right))) / max(left, right)


def massive_biharmonic_moment_energy(
    coefficients: dict[int, complex | mp.mpf | mp.mpc],
) -> mp.mpf:
    """Evaluate the universal H^-2 Gram using two prefix moments."""
    indices = sorted(index for index, value in coefficients.items() if value != 0)
    prefix_zero = mp.mpc(0)
    prefix_log = mp.mpc(0)
    energy = mp.mpf("0")
    cross = mp.mpc(0)
    for index in indices:
        value = mp.mpc(coefficients[index])
        log_index = mp.log(index)
        energy += 2 * abs(value) ** 2 / index
        cross += (
            mp.conj(value)
            / index
            * ((2 + log_index) * prefix_zero - prefix_log)
        )
        prefix_zero += value
        prefix_log += value * log_index
    return mp.re(energy + 2 * cross)


def centered_biharmonic_hodge_block(start: int) -> dict[str, mp.mpf]:
    """Two-moment centered H^-2 block equivalent to RH, Theorem IU."""
    if start < 4:
        raise ValueError("start must be at least four")
    x = mp.mpf(start)
    lower = int(mp.floor(x / 4)) + 1
    upper = int(mp.floor(4 * x))
    coefficients = {
        integer: von_mangoldt(integer) - 1
        for integer in range(max(1, lower), upper + 1)
    }
    energy = massive_biharmonic_moment_energy(coefficients)
    diagonal = mp.fsum(
        2 * abs(value) ** 2 / integer
        for integer, value in coefficients.items()
    )
    return {
        "energy": energy,
        "diagonal": diagonal,
        "rayleigh": energy / diagonal,
    }


def massive_sobolev_green_polynomial(
    order: int, distance: mp.mpf
) -> mp.mpf:
    """Polynomial P_{r-1} in the Green kernel of (-d^2+1/4)^-r."""
    if order < 1:
        raise ValueError("order must be positive")
    distance = abs(mp.mpf(distance))
    return mp.fsum(
        mp.factorial(2 * order - 2 - power)
        / (
            mp.factorial(order - 1)
            * mp.factorial(order - 1 - power)
            * mp.factorial(power)
        )
        * distance**power
        for power in range(order)
    )


def massive_sobolev_hodge_kernel(
    left: mp.mpf, right: mp.mpf, order: int
) -> mp.mpf:
    """Order-r Hodge kernel P_{r-1}(|log(m/n)|)/max(m,n)."""
    left = mp.mpf(left)
    right = mp.mpf(right)
    if left <= 0 or right <= 0:
        raise ValueError("arguments must be positive")
    return massive_sobolev_green_polynomial(
        order, mp.log(left / right)
    ) / max(left, right)


def massive_sobolev_moment_energy(
    coefficients: dict[int, complex | mp.mpf | mp.mpc], order: int
) -> mp.mpf:
    """Evaluate the order-r Green Gram using r logarithmic prefix moments."""
    if order < 1:
        raise ValueError("order must be positive")
    indices = sorted(index for index, value in coefficients.items() if value != 0)
    prefixes = [mp.mpc(0) for _ in range(order)]
    diagonal_value = massive_sobolev_green_polynomial(order, 0)
    diagonal = mp.mpf("0")
    cross = mp.mpc(0)
    polynomial_coefficients = [
        mp.factorial(2 * order - 2 - power)
        / (
            mp.factorial(order - 1)
            * mp.factorial(order - 1 - power)
            * mp.factorial(power)
        )
        for power in range(order)
    ]
    for index in indices:
        value = mp.mpc(coefficients[index])
        log_index = mp.log(index)
        diagonal += diagonal_value * abs(value) ** 2 / index
        inner = mp.mpc(0)
        for power, polynomial_coefficient in enumerate(
            polynomial_coefficients
        ):
            for moment in range(power + 1):
                inner += (
                    polynomial_coefficient
                    * math.comb(power, moment)
                    * log_index ** (power - moment)
                    * (-1) ** moment
                    * prefixes[moment]
                )
        cross += mp.conj(value) * inner / index
        power_value = mp.mpf("1")
        for moment in range(order):
            prefixes[moment] += value * power_value
            power_value *= log_index
    return mp.re(diagonal + 2 * cross)


def centered_dirichlet_polynomial(
    coefficients: dict[int, complex | mp.mpf | mp.mpc], frequency: mp.mpf
) -> mp.mpc:
    """D_x(t)=sum x_n n^(-1/2-it) for a finite coefficient vector."""
    frequency = mp.mpf(frequency)
    return mp.fsum(
        mp.mpc(value)
        * mp.power(index, -mp.mpf("0.5") - mp.j * frequency)
        for index, value in coefficients.items()
    )


def sampled_massive_sobolev_energy(
    coefficients: dict[int, complex | mp.mpf | mp.mpc],
    order: int,
    step: mp.mpf,
    cutoff: int,
) -> mp.mpf:
    """Finite trapezoidal spectral Gram used in Theorem JG."""
    if order < 1:
        raise ValueError("order must be positive")
    step = mp.mpf(step)
    if step <= 0:
        raise ValueError("step must be positive")
    if cutoff < 0:
        raise ValueError("cutoff must be nonnegative")
    return step / (2 * mp.pi) * mp.fsum(
        abs(centered_dirichlet_polynomial(coefficients, step * index)) ** 2
        / ((step * index) ** 2 + mp.mpf("0.25")) ** order
        for index in range(-cutoff, cutoff + 1)
    )


def centered_logarithmic_moments(
    coefficients: dict[int, complex | mp.mpf | mp.mpc],
    center: mp.mpf,
    degree: int,
) -> list[mp.mpc]:
    """M_j=sum x_n n^-1/2 log(n/center)^j for 0<=j<degree."""
    center = mp.mpf(center)
    if center <= 0:
        raise ValueError("center must be positive")
    if degree < 1:
        raise ValueError("degree must be positive")
    moments = [mp.mpc(0) for _ in range(degree)]
    for index, value in coefficients.items():
        normalized_log = mp.log(mp.mpf(index) / center)
        weighted_value = mp.mpc(value) / mp.sqrt(index)
        power_value = mp.mpf("1")
        for power in range(degree):
            moments[power] += weighted_value * power_value
            power_value *= normalized_log
    return moments


def centered_annular_euler_coordinate(
    scale: mp.mpf, dilation: mp.mpf = mp.mpf("4")
) -> mp.mpf:
    """Rank-one coordinate sum_(X/A<n<=AX)(Lambda(n)-1)/sqrt(n)."""
    scale = mp.mpf(scale)
    dilation = mp.mpf(dilation)
    if scale <= 0:
        raise ValueError("scale must be positive")
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    lower = int(mp.floor(scale / dilation)) + 1
    upper = int(mp.floor(dilation * scale))
    return mp.fsum(
        (von_mangoldt(integer) - 1) / mp.sqrt(integer)
        for integer in range(max(1, lower), upper + 1)
    )


def centered_annular_mellin_multiplier(
    value: mp.mpc, dilation: mp.mpf = mp.mpf("4")
) -> mp.mpc:
    """M_A(z)=(A^z-A^-z)/z, with its removable value at z=0."""
    value = mp.mpc(value)
    dilation = mp.mpf(dilation)
    if dilation <= 1:
        raise ValueError("dilation must exceed one")
    if value == 0:
        return 2 * mp.log(dilation)
    return (
        mp.power(dilation, value) - mp.power(dilation, -value)
    ) / value


def annular_frame_spectral_multiplier(
    frequency: mp.mpf, width_left: mp.mpf, width_right: mp.mpf
) -> mp.mpf:
    """Integral over h of |(it+1/2) 2 sin(ht)/t|^2."""
    frequency = mp.mpf(frequency)
    width_left = mp.mpf(width_left)
    width_right = mp.mpf(width_right)
    if width_left <= 0 or width_right <= width_left:
        raise ValueError("widths must satisfy 0<left<right")
    if frequency == 0:
        return (width_right**3 - width_left**3) / 3
    width_integral = (
        (width_right - width_left) / 2
        - (
            mp.sin(2 * width_right * frequency)
            - mp.sin(2 * width_left * frequency)
        )
        / (4 * frequency)
    )
    return (
        4
        * (frequency**2 + mp.mpf("0.25"))
        / frequency**2
        * width_integral
    )


def annular_abel_pair_kernel(
    left_index: int,
    right_index: int,
    left_width: mp.mpf,
    right_width: mp.mpf,
    sigma: mp.mpf,
) -> mp.mpf:
    """2 sigma integral of two annular indicators against exp(-2 sigma t)."""
    return annular_abel_moment_pair_kernel(
        left_index,
        right_index,
        left_width,
        right_width,
        sigma,
        0,
    )


def annular_abel_moment_pair_kernel(
    left_index: int,
    right_index: int,
    left_width: mp.mpf,
    right_width: mp.mpf,
    sigma: mp.mpf,
    moment_order: int,
) -> mp.mpf:
    """2 sigma integral of t^q times two annular indicators and exp(-2 sigma t)."""
    if left_index < 1 or right_index < 1:
        raise ValueError("indices must be positive")
    left_width = mp.mpf(left_width)
    right_width = mp.mpf(right_width)
    sigma = mp.mpf(sigma)
    if left_width <= 0 or right_width <= 0:
        raise ValueError("widths must be positive")
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    if moment_order < 0:
        raise ValueError("moment_order must be nonnegative")
    lower = max(
        mp.mpf("0"),
        mp.log(left_index) - left_width,
        mp.log(right_index) - right_width,
    )
    upper = min(
        mp.log(left_index) + left_width,
        mp.log(right_index) + right_width,
    )
    if upper <= lower:
        return mp.mpf("0")
    return mp.gammainc(
        moment_order + 1,
        2 * sigma * lower,
        2 * sigma * upper,
    ) / (2 * sigma) ** moment_order


def annular_gamma_sampling_pair_kernel(
    left_index: int,
    right_index: int,
    left_width: mp.mpf,
    right_width: mp.mpf,
    sigma: mp.mpf,
    shape_index: int,
    time_cutoff: mp.mpf | None = None,
) -> mp.mpf:
    """Probability that Gamma(shape_index+1, 2 sigma) lies in both annuli."""
    if shape_index < 0:
        raise ValueError("shape_index must be nonnegative")
    full_probability = (
        (2 * mp.mpf(sigma)) ** shape_index
        / mp.factorial(shape_index)
        * annular_abel_moment_pair_kernel(
            left_index,
            right_index,
            left_width,
            right_width,
            sigma,
            shape_index,
        )
    )
    if time_cutoff is None:
        return full_probability
    time_cutoff = mp.mpf(time_cutoff)
    if time_cutoff < 0:
        raise ValueError("time_cutoff must be nonnegative")
    lower = max(
        mp.mpf("0"),
        mp.log(left_index) - mp.mpf(left_width),
        mp.log(right_index) - mp.mpf(right_width),
    )
    upper = min(
        mp.log(left_index) + mp.mpf(left_width),
        mp.log(right_index) + mp.mpf(right_width),
        time_cutoff,
    )
    if upper <= lower:
        return mp.mpf("0")
    sigma = mp.mpf(sigma)
    return mp.gammainc(
        shape_index + 1,
        2 * sigma * lower,
        2 * sigma * upper,
    ) / mp.factorial(shape_index)


def annular_abel_rkhs_pair_kernel(
    left_index: int,
    right_index: int,
    left_width: mp.mpf,
    right_width: mp.mpf,
    sigma: mp.mpf,
    left_parameter: mp.mpc,
    right_parameter: mp.mpc,
) -> mp.mpc:
    """Prime-pair entry of the Abel analytic-vector RKHS kernel."""
    if left_index < 1 or right_index < 1:
        raise ValueError("indices must be positive")
    left_width = mp.mpf(left_width)
    right_width = mp.mpf(right_width)
    sigma = mp.mpf(sigma)
    if left_width <= 0 or right_width <= 0:
        raise ValueError("widths must be positive")
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    lower = max(
        mp.mpf("0"),
        mp.log(left_index) - left_width,
        mp.log(right_index) - right_width,
    )
    upper = min(
        mp.log(left_index) + left_width,
        mp.log(right_index) + right_width,
    )
    if upper <= lower:
        return mp.mpc("0")
    exponent = sigma * (
        2 - mp.mpc(left_parameter) - mp.conj(mp.mpc(right_parameter))
    )
    if exponent == 0:
        return 2 * sigma * (upper - lower)
    return (
        2
        * sigma
        * (mp.e ** (-exponent * lower) - mp.e ** (-exponent * upper))
        / exponent
    )


def rkhs_taylor_moment_weight(
    moment_order: int,
    degree: int,
    radial_parameter: mp.mpf,
) -> mp.mpf:
    """Coefficient of the normalized Abel moment in a radial Taylor Gram."""
    if moment_order < 0:
        raise ValueError("moment_order must be nonnegative")
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    radial_parameter = mp.mpf(radial_parameter)
    if radial_parameter < 0:
        raise ValueError("radial_parameter must be nonnegative")
    lower_index = max(0, moment_order - degree)
    upper_index = min(degree, moment_order)
    if lower_index > upper_index:
        return mp.mpf("0")
    binomial_mass = mp.fsum(
        mp.binomial(moment_order, left_degree)
        for left_degree in range(lower_index, upper_index + 1)
    )
    return (
        radial_parameter**moment_order
        * binomial_mass
        / (2**moment_order)
    )


def radial_taylor_sampling_weight(
    time: mp.mpf,
    degree: int,
    sigma: mp.mpf,
) -> mp.mpf:
    """Positive Poisson-cutoff density for the radial Taylor residue."""
    if degree < 2:
        raise ValueError("degree must be at least two")
    time = mp.mpf(time)
    sigma = mp.mpf(sigma)
    if time < 0:
        raise ValueError("time must be nonnegative")
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    radial_parameter = 1 - mp.mpf(1) / degree
    argument = sigma * radial_parameter * time
    truncated_exponential = mp.fsum(
        argument**power / mp.factorial(power)
        for power in range(degree + 1)
    )
    return (
        2
        * sigma
        / degree
        * mp.e ** (-2 * sigma * time)
        * truncated_exponential**2
    )


def taylor_dirichlet_polynomial(
    moments: list[mp.mpc], frequency: mp.mpf
) -> mp.mpc:
    """Taylor approximation to center^(it) D_x(t) from log moments."""
    frequency = mp.mpf(frequency)
    return mp.fsum(
        moment * (-mp.j * frequency) ** power / mp.factorial(power)
        for power, moment in enumerate(moments)
    )


def taylor_sobolev_core_energy(
    coefficients: dict[int, complex | mp.mpf | mp.mpc],
    center: mp.mpf,
    order: int,
    frequency_cutoff: mp.mpf,
    degree: int,
) -> mp.mpf:
    """Positive logarithmic-moment core obtained from Taylor compression."""
    if order < 1:
        raise ValueError("order must be positive")
    frequency_cutoff = mp.mpf(frequency_cutoff)
    if frequency_cutoff <= 0:
        raise ValueError("frequency_cutoff must be positive")
    moments = centered_logarithmic_moments(coefficients, center, degree)
    return mp.quad(
        lambda frequency: abs(
            taylor_dirichlet_polynomial(moments, frequency)
        )
        ** 2
        / (frequency**2 + mp.mpf("0.25")) ** order,
        [-frequency_cutoff, 0, frequency_cutoff],
    ) / (2 * mp.pi)


def chebyshev_primitive_prime_wavelet_charge(scale: mp.mpf) -> mp.mpf:
    """Pure-prime charge u(L)=sum Lambda(n) chi(n/L)."""
    scale = mp.mpf(scale)
    if scale < 1:
        raise ValueError("scale must be at least one")
    lower = int(mp.floor(scale / 4)) + 1
    upper = int(mp.floor(2 * scale))
    return mp.fsum(
        von_mangoldt(integer)
        * primitive_prime_wavelet_kernel(mp.mpf(integer) / scale)
        for integer in range(max(2, lower), upper + 1)
    )


def primitive_prime_wavelet_riemann_remainder(scale: mp.mpf) -> mp.mpf:
    """R_chi(L)=sum chi(n/L), uniformly bounded by Var(chi)=6."""
    scale = mp.mpf(scale)
    if scale < 1:
        raise ValueError("scale must be at least one")
    lower = int(mp.floor(scale / 4)) + 1
    upper = int(mp.floor(2 * scale))
    return mp.fsum(
        primitive_prime_wavelet_kernel(mp.mpf(integer) / scale)
        for integer in range(max(1, lower), upper + 1)
    )


def chebyshev_primitive_prime_wavelet_centered_charge(
    scale: mp.mpf,
) -> mp.mpf:
    """Centered primitive signal sum (Lambda(n)-1)chi(n/L)."""
    scale = mp.mpf(scale)
    if scale < 1:
        raise ValueError("scale must be at least one")
    lower = int(mp.floor(scale / 4)) + 1
    upper = int(mp.floor(2 * scale))
    return mp.fsum(
        (von_mangoldt(integer) - 1)
        * primitive_prime_wavelet_kernel(mp.mpf(integer) / scale)
        for integer in range(max(1, lower), upper + 1)
    )


def chebyshev_normalized_primitive_prime_wavelet(log_scale: mp.mpf) -> mp.mpf:
    """v(t)=exp(-t/2)u(exp(t)), the primitive normalized signal."""
    log_scale = mp.mpf(log_scale)
    scale = mp.e**log_scale
    return mp.e ** (-log_scale / 2) * (
        chebyshev_primitive_prime_wavelet_charge(scale)
    )


def _primitive_prime_wavelet_square_integral(
    left: mp.mpf, right: mp.mpf
) -> mp.mpf:
    """Integrate chi(r)^2 exactly between positive endpoints."""
    left = max(mp.mpf(left), mp.mpf("0.25"))
    right = min(mp.mpf(right), mp.mpf("2"))
    if right <= left:
        return mp.mpf("0")

    antiderivatives = (
        (
            mp.mpf("0.5"),
            lambda value: 16 * value - 8 * mp.log(value) - 1 / value,
        ),
        (
            mp.mpf("1"),
            lambda value: 16 * value - 24 * mp.log(value) - 9 / value,
        ),
        (
            mp.mpf("2"),
            lambda value: value - 4 * mp.log(value) - 4 / value,
        ),
    )
    total = mp.mpf("0")
    current = left
    for endpoint, antiderivative in antiderivatives:
        segment_right = min(right, endpoint)
        if segment_right > current:
            total += antiderivative(segment_right) - antiderivative(current)
            current = segment_right
        if current >= right:
            break
    return total


def chebyshev_primitive_prime_wavelet_diagonal(start: int) -> mp.mpf:
    """Exact pure-prime Gram diagonal on L in [X,2X]."""
    if start < 2:
        raise ValueError("start must be at least two")
    x = mp.mpf(start)
    lower = int(mp.floor(x / 4)) + 1
    upper = int(mp.floor(4 * x))
    return mp.fsum(
        von_mangoldt(integer) ** 2
        / integer
        * _primitive_prime_wavelet_square_integral(
            mp.mpf(integer) / (2 * x), mp.mpf(integer) / x
        )
        for integer in range(max(2, lower), upper + 1)
    )


def chebyshev_primitive_prime_wavelet_block(
    start: int,
) -> dict[str, mp.mpf]:
    """Finite pure-prime Gram energy and its signed off-diagonal part."""
    if start < 2:
        raise ValueError("start must be at least two")
    x = mp.mpf(start)
    lower = max(2, int(mp.floor(x / 4)) + 1)
    upper = int(mp.floor(4 * x))
    breakpoints = {x, 2 * x}
    for integer in range(lower, upper + 1):
        for divisor in (mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")):
            point = mp.mpf(integer) / divisor
            if x < point < 2 * x:
                breakpoints.add(point)
    ordered = sorted(breakpoints)
    energy = mp.fsum(
        mp.quad(
            lambda scale: chebyshev_primitive_prime_wavelet_charge(scale) ** 2
            / scale**2,
            [left, right],
        )
        for left, right in zip(ordered[:-1], ordered[1:])
    )
    diagonal = chebyshev_primitive_prime_wavelet_diagonal(start)
    return {
        "total": energy,
        "diagonal": diagonal,
        "off_diagonal": energy - diagonal,
    }


def prime_graph_symbol(frequency: mp.mpf, length: mp.mpf) -> mp.mpf:
    """Nonnegative full-line prime-graph Fourier multiplier.

    With zero extension and the Fourier convention used in notes/017,
    the sum of full translation squares has symbol
    4 sum Lambda(k)/sqrt(k) sin^2(t log(k)/2).
    """
    total = mp.mpf("0")
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            total += (
                4
                * mangoldt
                / mp.sqrt(k)
                * mp.sin(frequency * mp.log(k) / 2) ** 2
            )
    return total


def archimedean_multiplier(frequency: mp.mpf) -> mp.mpf:
    """The zeta archimedean multiplier K_infinity(t)."""
    return dirichlet_archimedean_multiplier(frequency, 0, 1)


def canonical_weil_multiplier(
    frequency: mp.mpf, length: mp.mpf
) -> mp.mpf:
    """Full scalar zeta multiplier h = K + G - 2P = K - 2 Re F."""
    return (
        archimedean_multiplier(frequency)
        + prime_graph_symbol(frequency, length)
        - 2 * prime_mass(length)
    )


def canonical_bad_multiplier(
    frequency: mp.mpf, length: mp.mpf
) -> mp.mpf:
    """Negative part W = max(-h, 0) of the full Weil multiplier."""
    return max(-canonical_weil_multiplier(frequency, length), mp.mpf("0"))


def prime_phase_sum(frequency: mp.mpf, length: mp.mpf) -> mp.mpc:
    """Dirichlet polynomial F_lambda(t) behind the graph multiplier."""
    total = mp.mpc("0")
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            total += (
                mangoldt
                / mp.sqrt(k)
                * mp.e ** (mp.j * frequency * mp.log(k))
            )
    return total


def twisted_prime_phase_data(
    frequency: mp.mpf,
    length: mp.mpf,
    phase,
) -> dict[str, mp.mpf | mp.mpc]:
    """Return mass, phase sum, and graph symbol for unit Euler phases.

    ``phase(k)`` should be zero for omitted/ramified prime powers and have
    modulus one otherwise.  This directly models primitive Dirichlet and
    fixed-degree unitary Euler data from notes/017 and 025.
    """
    mass = mp.mpf("0")
    phase_sum = mp.mpc("0")
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if not mangoldt:
            continue
        unit = mp.mpc(phase(k))
        if abs(unit) < mp.mpf("1e-40"):
            continue
        if abs(abs(unit) - 1) > mp.mpf("1e-30"):
            raise ValueError("nonzero Euler phases must have modulus one")
        weight = mangoldt / mp.sqrt(k)
        mass += weight
        phase_sum += weight * unit * mp.e ** (
            mp.j * frequency * mp.log(k)
        )
    graph_symbol = 2 * mass - 2 * mp.re(phase_sum)
    return {
        "mass": mass,
        "phase_sum": phase_sum,
        "graph_symbol": graph_symbol,
    }


def prime_log_moment(power: int, length: mp.mpf) -> mp.mpf:
    """Return sum Lambda(k)/sqrt(k) * log(k)^power up to exp(L)."""
    if power < 0:
        raise ValueError("power must be nonnegative")
    total = mp.mpf("0")
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            total += (
                mangoldt
                / mp.sqrt(k)
                * mp.log(k) ** power
            )
    return total


def archimedean_spectral_bottom() -> mp.mpf:
    """Exact infimum of the Riemann--Siegel phase derivative.

    ``theta'(t) = Re(digamma(1/4+it/2))/2 - log(pi)/2`` is minimized
    at zero.  The closed form is proved in Lemma CS of notes/023.
    """
    return (
        -mp.euler / 2
        - mp.pi / 4
        - mp.mpf("1.5") * mp.log(2)
        - mp.log(mp.pi) / 2
    )


def archimedean_quadratic_constant() -> mp.mpf:
    """C_infinity in ``K(t)-K(0) <= C_infinity t^2``."""
    return mp.zeta(3, mp.mpf("0.25")) / 8


def central_resonance_radius(
    length: mp.mpf, delta: mp.mpf
) -> mp.mpf:
    """Guaranteed central bad-interval radius from Theorem DH."""
    if delta <= 0:
        raise ValueError("delta must be positive")
    p_mass = prime_mass(length)
    scalar_defect = 2 * p_mass - archimedean_spectral_bottom()
    second_moment = prime_log_moment(2, length)
    return mp.sqrt(
        (scalar_defect + delta)
        / (second_moment + archimedean_quadratic_constant())
    )


def phase_volume_obstruction_constant() -> mp.mpf:
    """Optimal zeta phase-volume lower obstruction 3 sqrt(6)/(2 pi)."""
    return 3 * mp.sqrt(6) / (2 * mp.pi)


def prolate_trace_tail_bound(c: mp.mpf, rank_parameter: int) -> mp.mpf:
    """Factorial bound for sum_{n >= 2R-1} chi_n(c), Lemma DK."""
    c = mp.mpf(c)
    if not 0 < c <= 1:
        raise ValueError("c must lie in (0, 1]")
    if rank_parameter < 1:
        raise ValueError("rank_parameter must be positive")
    r = int(rank_parameter)
    return (
        5
        * mp.e**2
        * 4**r
        * c ** (2 * r + 1)
        / (mp.pi * mp.factorial(2 * r + 1))
    )


def dirichlet_archimedean_spectral_bottom(
    parity: int, conductor: int
) -> mp.mpf:
    """Exact Gamma-multiplier bottom for a primitive Dirichlet character."""
    if parity not in (0, 1):
        raise ValueError("parity must be 0 or 1")
    if conductor < 1:
        raise ValueError("conductor must be positive")
    return (
        -mp.euler / 2
        + (2 * parity - 1) * mp.pi / 4
        - mp.mpf("1.5") * mp.log(2)
        + mp.log(mp.mpf(conductor) / mp.pi) / 2
    )


def dirichlet_archimedean_multiplier(
    frequency: mp.mpf, parity: int, conductor: int
) -> mp.mpf:
    """Riemann--Siegel derivative for the Dirichlet Gamma factor."""
    if parity not in (0, 1):
        raise ValueError("parity must be 0 or 1")
    if conductor < 1:
        raise ValueError("conductor must be positive")
    argument = (
        mp.mpf("0.25")
        + mp.mpf(parity) / 2
        + mp.j * frequency / 2
    )
    return (
        mp.re(mp.digamma(argument))
        + mp.log(mp.mpf(conductor) / mp.pi)
    ) / 2


def gamma_euler_lower_bound(
    real_shifts,
    spectral_shifts,
    conductor: int,
) -> mp.mpf:
    """Common lower bound for a product of shifted Gamma_R factors.

    Factor ``j`` is ``Gamma_R(s + sigma_j + i nu_j)``.  At the center
    line its digamma real part has ``a_j = 1/4 + sigma_j/2``; positivity
    of every ``a_j`` is required.
    """
    real_values = [mp.mpf(value) for value in real_shifts]
    spectral_values = [mp.mpf(value) for value in spectral_shifts]
    if len(real_values) != len(spectral_values):
        raise ValueError("real_shifts and spectral_shifts must have equal length")
    if conductor < 1:
        raise ValueError("conductor must be positive")
    lower = mp.log(mp.mpf(conductor)) / 2
    for real_shift in real_values:
        argument_real = mp.mpf("0.25") + real_shift / 2
        if argument_real <= 0:
            raise ValueError("all centered Gamma arguments must be positive")
        lower += (mp.digamma(argument_real) - mp.log(mp.pi)) / 2
    return lower


def gamma_euler_multiplier(
    frequency: mp.mpf,
    real_shifts,
    spectral_shifts,
    conductor: int,
) -> mp.mpf:
    """Archimedean multiplier for general shifted Gamma_R data."""
    real_values = [mp.mpf(value) for value in real_shifts]
    spectral_values = [mp.mpf(value) for value in spectral_shifts]
    if len(real_values) != len(spectral_values):
        raise ValueError("real_shifts and spectral_shifts must have equal length")
    if conductor < 1:
        raise ValueError("conductor must be positive")
    result = mp.log(mp.mpf(conductor)) / 2
    for real_shift, spectral_shift in zip(
        real_values, spectral_values, strict=True
    ):
        argument_real = mp.mpf("0.25") + real_shift / 2
        if argument_real <= 0:
            raise ValueError("all centered Gamma arguments must be positive")
        argument = argument_real + mp.j * (
            frequency + spectral_shift
        ) / 2
        result += (
            mp.re(mp.digamma(argument)) - mp.log(mp.pi)
        ) / 2
    return result


def prime_graph_decomposition_for_function(
    function, length: mp.mpf
) -> dict[str, mp.mpf]:
    """Exact prime-adjacency completion of squares for a test function.

    The callable is evaluated on the centered interval [-L/2,L/2] and may
    be real or complex.  The returned quantities satisfy
    ``-correlation = edge_energy - degree_energy`` up to quadrature error.
    This helper is for structural diagnostics, not directed rounding.
    """
    ell = length / 2
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    correlation = mp.mpf("0")
    edge_energy = mp.mpf("0")
    degree_energy = mp.mpf("0")
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if not mangoldt:
            continue
        shift = mp.log(k)
        weight = mangoldt / mp.sqrt(k)
        left = -ell
        right = ell - shift
        if right <= left:
            continue
        correlation += 2 * weight * mp.re(
            mp.quad(
                lambda y: mp.conj(function(y)) * function(y + shift),
                [left, right],
            )
        )
        edge_energy += weight * mp.quad(
            lambda y: abs(function(y + shift) - function(y)) ** 2,
            [left, right],
        )
        degree_energy += weight * (
            mp.quad(lambda y: abs(function(y)) ** 2, [left, right])
            + mp.quad(
                lambda y: abs(function(y)) ** 2,
                [left + shift, right + shift],
            )
        )
    return {
        "correlation": correlation,
        "edge_energy": edge_energy,
        "degree_energy": degree_energy,
        "identity_error": -correlation - edge_energy + degree_energy,
    }


def arch_remainder_mass(length: mp.mpf) -> mp.mpf:
    """Integral of |rho(x)-1/(2x)| on [0,L] from notes/005."""

    def integrand(x: mp.mpf) -> mp.mpf:
        if abs(x) < mp.mpf("1e-25"):
            return mp.mpf("0.25")
        rho = mp.e ** (x / 2) / (mp.e**x - mp.e ** (-x))
        return abs(rho - 1 / (2 * x))

    return mp.quad(integrand, [0, length])


def off_diagonal_bound(n: int, m: int, length: mp.mpf) -> mp.mpf:
    """The explicit upper bound in Theorem O of notes/005.

    This applies only when n != m.
    """
    if n == m:
        raise ValueError("off-diagonal bound requires n != m")
    d = abs(m - n)
    lam = mp.e ** (length / 2)
    return abs(w02(n, m, length)) + (
        lam * (1 + mp.log(mp.pi * d)) + 2 * prime_mass(length)
    ) / (mp.pi * d)


def improved_off_diagonal_bound(n: int, m: int, length: mp.mpf) -> mp.mpf:
    """The no-log upper bound in Theorem Q of notes/005."""
    if n == m:
        raise ValueError("off-diagonal bound requires n != m")
    d = abs(m - n)
    return abs(w02(n, m, length)) + (
        4 + 2 * arch_remainder_mass(length) + 2 * prime_mass(length)
    ) / (mp.pi * d)


def certificate_off_diagonal_bound(n: int, m: int, length: mp.mpf) -> mp.mpf:
    """Cancellation-preserving per-entry bound from notes/005, equation (16a)."""
    if n == m:
        raise ValueError("off-diagonal bound requires n != m")
    d = abs(m - n)
    singular = abs(mp.si(2 * mp.pi * m) - mp.si(2 * mp.pi * n)) / (
        2 * mp.pi * d
    )
    remainder = 2 * arch_remainder_mass(length) / (mp.pi * d)
    return (
        abs(w02(n, m, length))
        + abs(w_primes(n, m, length))
        + singular
        + remainder
    )


def row_square_tail_bound(n: int, cutoff: int, length: mp.mpf) -> mp.mpf:
    """The explicit squared-row-tail bound in Theorem P of notes/005."""
    if cutoff < max(1, 2 * abs(n)):
        raise ValueError("cutoff must be at least max(1, 2*abs(n))")
    denominator = length**2 + 16 * mp.pi**2 * n**2
    a_value = (
        2
        * length
        * mp.sinh(length / 4) ** 2
        * (length**2 + 16 * mp.pi**2 * abs(n))
        / (mp.pi**2 * denominator)
    )
    lam = mp.e ** (length / 2)
    c_value = a_value + 4 * prime_mass(length) / mp.pi + 2 * lam / mp.pi
    b_value = 1 + mp.log(2 * mp.pi * cutoff)
    return (
        2
        * c_value**2
        / cutoff
        * (b_value**2 + 2 * b_value + 2)
    )


def improved_row_square_tail_bound(
    n: int, cutoff: int, length: mp.mpf
) -> mp.mpf:
    """The no-log squared-row-tail bound in Theorem R of notes/005."""
    if cutoff < max(1, 2 * abs(n)):
        raise ValueError("cutoff must be at least max(1, 2*abs(n))")
    c_value = ctilde(n, length)
    return 2 * c_value**2 / cutoff


def ctilde(n: int, length: mp.mpf) -> mp.mpf:
    """The row constant Ctilde_(lambda,n) in notes/005, equation (17)."""
    denominator = length**2 + 16 * mp.pi**2 * n**2
    a_value = (
        2
        * length
        * mp.sinh(length / 4) ** 2
        * (length**2 + 16 * mp.pi**2 * abs(n))
        / (mp.pi**2 * denominator)
    )
    c_value = a_value + (
        8 + 4 * arch_remainder_mass(length) + 4 * prime_mass(length)
    ) / mp.pi
    return c_value


def weighted_candidate_tail_bound(
    coefficients: dict[int, mp.mpf], cutoff: int, length: mp.mpf
) -> mp.mpf:
    """Squared residual tail in Theorem S of notes/006.

    The candidate must be supported in |n| <= cutoff/2. Outside the
    cutoff, (A-mu)c equals Ac, so this bound is independent of mu.
    """
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if cutoff < max(1, 2 * maximum):
        raise ValueError("cutoff must be at least max(1, 2*support radius)")
    weighted = mp.fsum(
        abs(coefficients[n]) * ctilde(n, length) for n in support
    )
    return 2 * weighted**2 / cutoff


def boundary_vanishing_candidate_tail_bound(
    coefficients: dict[int, mp.mpf], cutoff: int, length: mp.mpf
) -> mp.mpf:
    """The O(log(K)^2/K^3) squared tail from Theorem V of notes/006."""
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if cutoff < max(1, 2 * maximum):
        raise ValueError("cutoff must be at least max(1, 2*support radius)")
    zero = mp.mpf("0")
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    boundary_sum = mp.fsum(coefficients.values())
    coefficient_mass = mp.fsum(abs(value) for value in coefficients.values())
    if abs(boundary_sum) > 10 * mp.eps * max(1, coefficient_mass):
        raise ValueError("coefficients must have zero boundary sum")

    first_moment = mp.fsum(
        abs(coefficients[n]) * abs(n) for n in support
    )
    h_zero = mp.fsum(
        coefficients[n] / (length**2 + 16 * mp.pi**2 * n**2)
        for n in support
    )
    lam = mp.e ** (length / 2)
    p_mass = prime_mass(length)
    alpha = (
        2 * length**3 * mp.sinh(length / 4) ** 2 * abs(h_zero) / mp.pi**2
        + 2 * first_moment * (lam + 2 * p_mass) / mp.pi
    )
    beta = 2 * lam * first_moment / mp.pi
    a_cutoff = alpha + beta * mp.log(mp.pi * cutoff)
    return (
        2
        * (
            a_cutoff**2
            + 2 * beta * a_cutoff / 3
            + 2 * beta**2 / 9
        )
        / (3 * cutoff**3)
    )


def hybrid_even_candidate_tail_bound(
    coefficients: dict[int, mp.mpf], cutoff: int, length: mp.mpf
) -> mp.mpf:
    """Boundary-defect decomposition from Corollary W of notes/006."""
    zero = mp.mpf("0")
    support = [n for n, value in coefficients.items() if value != 0]
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    defect = mp.fsum(coefficients.values())
    corrected = dict(coefficients)
    corrected[0] = corrected.get(0, zero) - defect
    accelerated = boundary_vanishing_candidate_tail_bound(
        corrected, cutoff, length
    )
    defect_tail_norm = abs(defect) * mp.sqrt(
        improved_row_square_tail_bound(0, cutoff, length)
    )
    return (mp.sqrt(accelerated) + defect_tail_norm) ** 2


def candidate_leading_coefficient(
    coefficients: dict[int, mp.mpf], length: mp.mpf
) -> dict[str, mp.mpf]:
    """Combined 1/m^2 coefficient in Theorem AA of notes/008."""
    second_moment = mp.fsum(
        value * n**2 for n, value in coefficients.items()
    )

    def first_sine_moment(x: mp.mpf) -> mp.mpf:
        return mp.fsum(
            value * n * mp.sin(2 * mp.pi * n * x / length)
            for n, value in coefficients.items()
        )

    def arch_integrand(x: mp.mpf) -> mp.mpf:
        if abs(x) < mp.mpf("1e-25"):
            return mp.pi * second_moment / length
        rho = mp.e ** (x / 2) / (mp.e**x - mp.e ** (-x))
        return rho * first_sine_moment(x)

    arch = mp.quad(arch_integrand, [0, length])
    prime = mp.mpf(0)
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            prime += (
                mangoldt
                * mp.power(k, mp.mpf("-0.5"))
                * first_sine_moment(mp.log(k))
            )
    h_zero = mp.fsum(
        value / (length**2 + 16 * mp.pi**2 * n**2)
        for n, value in coefficients.items()
    )
    pole = 2 * length**3 * mp.sinh(length / 4) ** 2 * h_zero / mp.pi**2
    return {
        "pole": pole,
        "arch": -arch / mp.pi,
        "prime": -prime / mp.pi,
        "combined": pole - (arch + prime) / mp.pi,
    }


def second_order_candidate_tail_bound(
    coefficients: dict[int, mp.mpf], cutoff: int, length: mp.mpf
) -> mp.mpf:
    """Cancellation-preserving squared tail from Theorem AB of notes/008."""
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if cutoff < max(1, 2 * maximum):
        raise ValueError("cutoff must be at least max(1, 2*support radius)")
    zero = mp.mpf(0)
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    coefficient_mass = mp.fsum(abs(value) for value in coefficients.values())
    if abs(mp.fsum(coefficients.values())) > 10 * mp.eps * max(1, coefficient_mass):
        raise ValueError("coefficients must have zero boundary sum")

    leading = candidate_leading_coefficient(coefficients, length)
    second_absolute_moment = mp.fsum(
        abs(value) * n**2 for n, value in coefficients.items()
    )
    lam = mp.e ** (length / 2)
    p_mass = prime_mass(length)
    pole_remainder = abs(leading["pole"]) * length**2 / (16 * mp.pi**2)
    gamma = (
        2 * second_absolute_moment * (lam + 2 * p_mass) / mp.pi
        + pole_remainder
    )
    beta = 2 * lam * second_absolute_moment / mp.pi
    b_cutoff = gamma + beta * mp.log(mp.pi * cutoff)
    return (
        4 * abs(leading["combined"]) ** 2 / (3 * cutoff**3)
        + 4
        * (
            b_cutoff**2
            + 2 * beta * b_cutoff / 5
            + 2 * beta**2 / 25
        )
        / (5 * cutoff**5)
    )


def semilocal_sine_coefficient(m: int, length: mp.mpf) -> mp.mpf:
    """Return H_m=I_m+J_m from notes/009 and notes/011."""
    if m == 0:
        return mp.mpf(0)

    def arch_integrand(x: mp.mpf) -> mp.mpf:
        if abs(x) < mp.mpf("1e-25"):
            return mp.pi * m / length
        rho = mp.e ** (x / 2) / (mp.e**x - mp.e ** (-x))
        return rho * mp.sin(2 * mp.pi * m * x / length)

    arch_sine = mp.quad(arch_integrand, [0, length])
    prime_sine = mp.mpf(0)
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            prime_sine += (
                mangoldt
                * mp.power(k, mp.mpf("-0.5"))
                * mp.sin(2 * mp.pi * m * mp.log(k) / length)
            )
    return arch_sine + prime_sine


def third_order_oscillatory_coefficient(
    coefficients: dict[int, mp.mpf], m: int, length: mp.mpf
) -> mp.mpf:
    """The exact B_m coefficient in Theorem AC of notes/009."""
    if m == 0:
        raise ValueError("m must be nonzero")
    signed_second_moment = mp.fsum(
        value * n**2 for n, value in coefficients.items()
    )
    return (
        signed_second_moment
        * semilocal_sine_coefficient(m, length)
        / mp.pi
    )


def candidate_fourth_order_coefficient(
    coefficients: dict[int, mp.mpf], length: mp.mpf
) -> dict[str, mp.mpf]:
    """The signed D_4 coefficient in Theorem AF of notes/010."""
    leading = candidate_leading_coefficient(coefficients, length)

    def third_sine_moment(x: mp.mpf) -> mp.mpf:
        return mp.fsum(
            value
            * n**3
            * mp.sin(2 * mp.pi * n * x / length)
            for n, value in coefficients.items()
        )

    fourth_moment = mp.fsum(
        value * n**4 for n, value in coefficients.items()
    )

    def arch_integrand(x: mp.mpf) -> mp.mpf:
        if abs(x) < mp.mpf("1e-25"):
            return mp.pi * fourth_moment / length
        rho = mp.e ** (x / 2) / (mp.e**x - mp.e ** (-x))
        return rho * third_sine_moment(x)

    arch = mp.quad(arch_integrand, [0, length])
    prime = mp.mpf(0)
    maximum = int(mp.floor(mp.e**length + mp.mpf("1e-20")))
    for k in range(2, maximum + 1):
        mangoldt = von_mangoldt(k)
        if mangoldt:
            prime += (
                mangoldt
                * mp.power(k, mp.mpf("-0.5"))
                * third_sine_moment(mp.log(k))
            )
    pole = -leading["pole"] * length**2 / (16 * mp.pi**2)
    return {
        "pole": pole,
        "arch": -arch / mp.pi,
        "prime": -prime / mp.pi,
        "combined": pole - (arch + prime) / mp.pi,
    }


def third_order_candidate_tail_bound(
    coefficients: dict[int, mp.mpf], cutoff: int, length: mp.mpf
) -> mp.mpf:
    """The O(K^-3)+O(K^-5)+O(log(K)^2 K^-7) bound in notes/009."""
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if cutoff < max(1, 2 * maximum):
        raise ValueError("cutoff must be at least max(1, 2*support radius)")
    zero = mp.mpf(0)
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    coefficient_mass = mp.fsum(abs(value) for value in coefficients.values())
    if abs(mp.fsum(coefficients.values())) > 10 * mp.eps * max(1, coefficient_mass):
        raise ValueError("coefficients must have zero boundary sum")

    leading = candidate_leading_coefficient(coefficients, length)
    signed_second_moment = mp.fsum(
        value * n**2 for n, value in coefficients.items()
    )
    third_absolute_moment = mp.fsum(
        abs(value) * abs(n) ** 3 for n, value in coefficients.items()
    )
    lam = mp.e ** (length / 2)
    p_mass = prime_mass(length)
    remainder_mass = arch_remainder_mass(length)
    b_max = (
        abs(signed_second_moment)
        * (2 + remainder_mass + p_mass)
        / mp.pi
    )
    pole_remainder = abs(leading["pole"]) * length**2 / (16 * mp.pi**2)
    gamma = (
        2 * third_absolute_moment * (lam + 2 * p_mass) / mp.pi
        + pole_remainder
    )
    beta = 2 * lam * third_absolute_moment / mp.pi
    d_cutoff = gamma + beta * mp.log(mp.pi * cutoff)
    a_abs = abs(leading["combined"])
    retained = 4 * (
        a_abs**2 / (3 * cutoff**3)
        + a_abs * b_max / (2 * cutoff**4)
        + b_max**2 / (5 * cutoff**5)
    )
    remainder = (
        4
        * (
            d_cutoff**2
            + 2 * beta * d_cutoff / 7
            + 2 * beta**2 / 49
        )
        / (7 * cutoff**7)
    )
    return retained + remainder


def finite_phase_third_order_candidate_tail_bound(
    coefficients: dict[int, mp.mpf],
    cutoff: int,
    retained_cutoff: int,
    length: mp.mpf,
) -> mp.mpf:
    """The finite-phase/Minkowski squared tail from Theorem AE of notes/010.

    The exact oscillatory coefficients B_m are retained for
    cutoff < m <= retained_cutoff.  Only the remaining infinite tail uses
    the pointwise B_max envelope.
    """
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if cutoff < max(1, 2 * maximum):
        raise ValueError("cutoff must be at least max(1, 2*support radius)")
    if retained_cutoff < cutoff:
        raise ValueError("retained_cutoff must be at least cutoff")
    zero = mp.mpf(0)
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    coefficient_mass = mp.fsum(abs(value) for value in coefficients.values())
    if abs(mp.fsum(coefficients.values())) > 10 * mp.eps * max(1, coefficient_mass):
        raise ValueError("coefficients must have zero boundary sum")

    leading = candidate_leading_coefficient(coefficients, length)
    signed_second_moment = mp.fsum(
        value * n**2 for n, value in coefficients.items()
    )
    third_absolute_moment = mp.fsum(
        abs(value) * abs(n) ** 3 for n, value in coefficients.items()
    )
    lam = mp.e ** (length / 2)
    p_mass = prime_mass(length)
    remainder_mass = arch_remainder_mass(length)
    b_max = (
        abs(signed_second_moment)
        * (2 + remainder_mass + p_mass)
        / mp.pi
    )

    a_value = leading["combined"]
    a_abs = abs(a_value)
    finite_energy = mp.fsum(
        abs(
            a_value / m**2
            + third_order_oscillatory_coefficient(coefficients, m, length)
            / m**3
        )
        ** 2
        for m in range(cutoff + 1, retained_cutoff + 1)
    )
    infinite_envelope = (
        a_abs**2 / (3 * retained_cutoff**3)
        + a_abs * b_max / (2 * retained_cutoff**4)
        + b_max**2 / (5 * retained_cutoff**5)
    )
    retained_energy = 2 * (finite_energy + infinite_envelope)

    pole_remainder = abs(leading["pole"]) * length**2 / (16 * mp.pi**2)
    gamma = (
        2 * third_absolute_moment * (lam + 2 * p_mass) / mp.pi
        + pole_remainder
    )
    beta = 2 * lam * third_absolute_moment / mp.pi
    d_cutoff = gamma + beta * mp.log(mp.pi * cutoff)
    remainder_energy = (
        2
        * (
            d_cutoff**2
            + 2 * beta * d_cutoff / 7
            + 2 * beta**2 / 49
        )
        / (7 * cutoff**7)
    )
    return (mp.sqrt(retained_energy) + mp.sqrt(remainder_energy)) ** 2


def fourth_order_candidate_tail_bound(
    coefficients: dict[int, mp.mpf],
    cutoff: int,
    retained_cutoff: int,
    length: mp.mpf,
) -> mp.mpf:
    """The fourth-order finite-phase squared tail from Theorem AG."""
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if cutoff < max(1, 2 * maximum):
        raise ValueError("cutoff must be at least max(1, 2*support radius)")
    if retained_cutoff < cutoff:
        raise ValueError("retained_cutoff must be at least cutoff")
    zero = mp.mpf(0)
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    coefficient_mass = mp.fsum(abs(value) for value in coefficients.values())
    if abs(mp.fsum(coefficients.values())) > 10 * mp.eps * max(1, coefficient_mass):
        raise ValueError("coefficients must have zero boundary sum")

    leading = candidate_leading_coefficient(coefficients, length)
    fourth = candidate_fourth_order_coefficient(coefficients, length)
    signed_second_moment = mp.fsum(
        value * n**2 for n, value in coefficients.items()
    )
    fourth_absolute_moment = mp.fsum(
        abs(value) * abs(n) ** 4 for n, value in coefficients.items()
    )
    lam = mp.e ** (length / 2)
    p_mass = prime_mass(length)
    remainder_mass = arch_remainder_mass(length)
    b_max = (
        abs(signed_second_moment)
        * (2 + remainder_mass + p_mass)
        / mp.pi
    )

    a_value = leading["combined"]
    d_value = fourth["combined"]
    a_abs = abs(a_value)
    d_abs = abs(d_value)
    finite_energy = mp.fsum(
        abs(
            a_value / m**2
            + third_order_oscillatory_coefficient(coefficients, m, length)
            / m**3
            + d_value / m**4
        )
        ** 2
        for m in range(cutoff + 1, retained_cutoff + 1)
    )
    infinite_envelope = (
        a_abs**2 / (3 * retained_cutoff**3)
        + a_abs * b_max / (2 * retained_cutoff**4)
        + (b_max**2 + 2 * a_abs * d_abs)
        / (5 * retained_cutoff**5)
        + b_max * d_abs / (3 * retained_cutoff**6)
        + d_abs**2 / (7 * retained_cutoff**7)
    )
    retained_energy = 2 * (finite_energy + infinite_envelope)

    pole_remainder = (
        abs(leading["pole"]) * length**4 / (256 * mp.pi**4)
    )
    gamma = (
        2 * fourth_absolute_moment * (lam + 2 * p_mass) / mp.pi
        + pole_remainder
    )
    beta = 2 * lam * fourth_absolute_moment / mp.pi
    e_cutoff = gamma + beta * mp.log(mp.pi * cutoff)
    remainder_energy = (
        2
        * (
            e_cutoff**2
            + 2 * beta * e_cutoff / 9
            + 2 * beta**2 / 81
        )
        / (9 * cutoff**9)
    )
    return (mp.sqrt(retained_energy) + mp.sqrt(remainder_energy)) ** 2


def exact_resolvent_tail_component(
    coefficients: dict[int, mp.mpf], m: int, length: mp.mpf
) -> mp.mpf:
    """Exact off-support component from Theorem AH of notes/011."""
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if abs(m) <= maximum:
        raise ValueError("m must lie outside the coefficient support")
    zero = mp.mpf(0)
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    coefficient_mass = mp.fsum(abs(value) for value in coefficients.values())
    if abs(mp.fsum(coefficients.values())) > 10 * mp.eps * max(1, coefficient_mass):
        raise ValueError("coefficients must have zero boundary sum")

    leading = candidate_leading_coefficient(coefficients, length)
    positive = sorted(n for n in support if n > 0)
    z = mp.mpf(1) / m**2
    t = length**2 / (16 * mp.pi**2)
    rational = leading["pole"] / (1 + t * z)
    moment_resolvent = mp.mpf(0)
    for n in positive:
        h_n = semilocal_sine_coefficient(n, length)
        denominator = 1 - n**2 * z
        rational -= (
            2 * n * coefficients[n] * h_n / (mp.pi * denominator)
        )
        moment_resolvent += 2 * coefficients[n] * n**2 / denominator
    h_m = semilocal_sine_coefficient(m, length)
    return z * rational + h_m * moment_resolvent / (mp.pi * m**3)


def all_orders_candidate_tail_certificate(
    coefficients: dict[int, mp.mpf],
    cutoff: int,
    retained_cutoff: int,
    expansion_order: int,
    length: mp.mpf,
) -> dict[str, mp.mpf]:
    """All-orders rational-resolvent tail certificate (Theorem AI)."""
    support = [n for n, value in coefficients.items() if value != 0]
    maximum = max((abs(n) for n in support), default=0)
    if cutoff < max(1, 2 * maximum):
        raise ValueError("cutoff must be at least max(1, 2*support radius)")
    if retained_cutoff < cutoff:
        raise ValueError("retained_cutoff must be at least cutoff")
    if expansion_order < 1:
        raise ValueError("expansion_order must be positive")
    zero = mp.mpf(0)
    for n in support:
        if coefficients.get(-n, zero) != coefficients[n]:
            raise ValueError("coefficients must be even")
    coefficient_mass = mp.fsum(abs(value) for value in coefficients.values())
    if abs(mp.fsum(coefficients.values())) > 10 * mp.eps * max(1, coefficient_mass):
        raise ValueError("coefficients must have zero boundary sum")

    leading = candidate_leading_coefficient(coefficients, length)
    positive = sorted(n for n in support if n > 0)
    h_support = {
        n: semilocal_sine_coefficient(n, length) for n in positive
    }
    t = length**2 / (16 * mp.pi**2)

    def exact_component(m: int) -> mp.mpf:
        z = mp.mpf(1) / m**2
        rational = leading["pole"] / (1 + t * z)
        moment_resolvent = mp.mpf(0)
        for n in positive:
            denominator = 1 - n**2 * z
            rational -= (
                2
                * n
                * coefficients[n]
                * h_support[n]
                / (mp.pi * denominator)
            )
            moment_resolvent += (
                2 * coefficients[n] * n**2 / denominator
            )
        return (
            z * rational
            + semilocal_sine_coefficient(m, length)
            * moment_resolvent
            / (mp.pi * m**3)
        )

    finite_energy = 2 * mp.fsum(
        abs(exact_component(m)) ** 2
        for m in range(cutoff + 1, retained_cutoff + 1)
    )

    radius = mp.mpf(1) / retained_cutoff**2
    rational_coefficients = []
    moment_coefficients = []
    for ell in range(expansion_order):
        rational_coefficients.append(
            leading["pole"] * (-t) ** ell
            - (mp.mpf(2) / mp.pi)
            * mp.fsum(
                coefficients[n]
                * n ** (2 * ell + 1)
                * h_support[n]
                for n in positive
            )
        )
        moment_coefficients.append(
            2
            * mp.fsum(
                coefficients[n] * n ** (2 * ell + 2)
                for n in positive
            )
        )

    rational_remainder = abs(leading["pole"]) * (t * radius) ** expansion_order
    rational_remainder += (mp.mpf(2) / mp.pi) * mp.fsum(
        abs(coefficients[n] * n * h_support[n])
        * (n**2 * radius) ** expansion_order
        / (1 - n**2 * radius)
        for n in positive
    )
    moment_remainder = 2 * mp.fsum(
        abs(coefficients[n])
        * n**2
        * (n**2 * radius) ** expansion_order
        / (1 - n**2 * radius)
        for n in positive
    )
    rational_supremum = rational_remainder + mp.fsum(
        abs(value) * radius**ell
        for ell, value in enumerate(rational_coefficients)
    )
    moment_supremum = moment_remainder + mp.fsum(
        abs(value) * radius**ell
        for ell, value in enumerate(moment_coefficients)
    )

    h_max = 2 + arch_remainder_mass(length) + prime_mass(length)
    oscillatory_supremum = h_max * moment_supremum / mp.pi
    far_energy = 2 * (
        rational_supremum**2 / (3 * retained_cutoff**3)
        + rational_supremum
        * oscillatory_supremum
        / (2 * retained_cutoff**4)
        + oscillatory_supremum**2 / (5 * retained_cutoff**5)
    )
    return {
        "finite_energy": finite_energy,
        "far_energy": far_energy,
        "tail_bound": finite_energy + far_energy,
        "rational_supremum": rational_supremum,
        "moment_supremum": moment_supremum,
        "oscillatory_supremum": oscillatory_supremum,
        "rational_remainder": rational_remainder,
        "moment_remainder": moment_remainder,
    }


def all_orders_candidate_tail_bound(
    coefficients: dict[int, mp.mpf],
    cutoff: int,
    retained_cutoff: int,
    expansion_order: int,
    length: mp.mpf,
) -> mp.mpf:
    """Convenience wrapper returning Theorem AI's squared tail bound."""
    return all_orders_candidate_tail_certificate(
        coefficients,
        cutoff,
        retained_cutoff,
        expansion_order,
        length,
    )["tail_bound"]


def qw_entry(n: int, m: int, length: mp.mpf) -> mp.mpf:
    return w02(n, m, length) - w_real(n, m, length) - w_primes(
        n, m, length
    )


def build_matrix(lam: mp.mpf, cutoff: int) -> tuple[np.ndarray, list[int]]:
    length = 2 * mp.log(lam)
    indices = list(range(-cutoff, cutoff + 1))
    matrix = np.empty((len(indices), len(indices)), dtype=float)
    for i, n in enumerate(indices):
        for j in range(i, len(indices)):
            m = indices[j]
            value = float(qw_entry(n, m, length))
            matrix[i, j] = value
            matrix[j, i] = value
    return matrix, indices


def build_polarization_defect_matrices(
    lam: mp.mpf,
    cutoff: int,
    m_infinity: float | mp.mpf | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[int]]:
    """Build finite Fourier compressions of ``Ptilde``, ``Vtilde``, and QW.

    The decomposition is the compact-Hodge identity from notes/017 and 022:

    ``QW = Ptilde - Vtilde``.

    ``m_infinity`` defaults to the exact spectral bottom from Lemma CS.  A
    different shift may be supplied for structural diagnostics, but it is not
    silently interpreted as a directed-rounding infinite-operator bound.
    """
    if m_infinity is None:
        m_infinity = archimedean_spectral_bottom()
    length = 2 * mp.log(lam)
    indices = list(range(-cutoff, cutoff + 1))
    size = len(indices)
    pole = np.empty((size, size), dtype=float)
    arch = np.empty((size, size), dtype=float)
    prime = np.empty((size, size), dtype=float)
    for i, n in enumerate(indices):
        for j in range(i, size):
            m = indices[j]
            pole_value = float(w02(n, m, length))
            arch_value = -float(w_real(n, m, length))
            prime_value = float(w_primes(n, m, length))
            pole[i, j] = pole[j, i] = pole_value
            arch[i, j] = arch[j, i] = arch_value
            prime[i, j] = prime[j, i] = prime_value

    identity = np.eye(size)
    reflection = np.fliplr(identity)
    even_projection = (identity + reflection) / 2
    odd_projection = (identity - reflection) / 2
    positive_pole = even_projection @ pole @ even_projection
    negative_pole = -(odd_projection @ pole @ odd_projection)

    p_mass = float(prime_mass(length))
    graph = 2 * p_mass * identity - prime
    polarization = (
        arch
        - float(m_infinity) * identity
        + graph
        + positive_pole
    )
    defect = (
        (2 * p_mass - float(m_infinity)) * identity + negative_pole
    )
    qw = pole + arch - prime
    return polarization, defect, qw, indices


def generalized_eigenvalues(
    polarization: np.ndarray,
    defect: np.ndarray,
    epsilon: float = 0.0,
) -> np.ndarray:
    """Return all rho in ``V c = rho (P + epsilon I) c``.

    A Cholesky congruence preserves Hermitian symmetry.  Failure of Cholesky
    correctly signals that the supplied shifted polarization is not positive
    definite, so this helper never silently regularizes the pencil.
    """
    shifted = (polarization + polarization.T) / 2
    shifted = shifted + float(epsilon) * np.eye(shifted.shape[0])
    defect_symmetric = (defect + defect.T) / 2
    cholesky = np.linalg.cholesky(shifted)
    inverse_cholesky = np.linalg.inv(cholesky)
    compact_hodge = (
        inverse_cholesky @ defect_symmetric @ inverse_cholesky.T
    )
    compact_hodge = (compact_hodge + compact_hodge.T) / 2
    return np.linalg.eigvalsh(compact_hodge)


def largest_generalized_eigenvalue(
    polarization: np.ndarray,
    defect: np.ndarray,
    epsilon: float = 0.0,
) -> float:
    """Return the largest compact-Hodge generalized eigenvalue."""
    return float(
        generalized_eigenvalues(polarization, defect, epsilon)[-1]
    )


def residual_feshbach_lower_matrix(
    core_block: np.ndarray,
    residual_gram: np.ndarray,
    complement_gap: float,
) -> np.ndarray:
    """Return ``A - R/gamma`` from Theorem CT of notes/024.

    Inputs are symmetrized to remove harmless floating-point skew.  A
    nonpositive gap is rejected because the Feshbach estimate requires a
    strictly positive complement compression.
    """
    if complement_gap <= 0:
        raise ValueError("complement_gap must be positive")
    if core_block.shape != residual_gram.shape:
        raise ValueError("core_block and residual_gram must have equal shape")
    core_symmetric = (core_block + core_block.T) / 2
    residual_symmetric = (residual_gram + residual_gram.T) / 2
    lower = core_symmetric - residual_symmetric / float(complement_gap)
    return (lower + lower.T) / 2


def rank_one_resolvent_upper(
    feshbach_lower: np.ndarray,
    anchor_coordinates: np.ndarray,
) -> float:
    """Return ``2 <s,L^-1 s>`` for the odd Hodge certificate.

    Cholesky failure deliberately reports that ``L`` has not been certified
    positive definite; no numerical regularization is inserted.
    """
    lower = (feshbach_lower + feshbach_lower.T) / 2
    anchor = np.asarray(anchor_coordinates, dtype=float).reshape(-1)
    if lower.shape != (anchor.size, anchor.size):
        raise ValueError("anchor dimension must match feshbach_lower")
    cholesky = np.linalg.cholesky(lower)
    transformed = np.linalg.solve(cholesky, anchor)
    return float(2 * transformed @ transformed)


def build_parity_blocks_mp(
    lam: mp.mpf, cutoff: int
) -> tuple[mp.matrix, mp.matrix]:
    """Build parity blocks without converting entries to machine floats."""
    length = 2 * mp.log(lam)
    even = mp.matrix(cutoff + 1, cutoff + 1)
    odd = mp.matrix(cutoff, cutoff)
    even[0, 0] = qw_entry(0, 0, length)
    for m in range(1, cutoff + 1):
        value = mp.sqrt(2) * qw_entry(0, m, length)
        even[0, m] = value
        even[m, 0] = value
    for n in range(1, cutoff + 1):
        for m in range(n, cutoff + 1):
            same = qw_entry(n, m, length)
            reflected = qw_entry(n, -m, length)
            even_value = same + reflected
            odd_value = same - reflected
            even[n, m] = even_value
            even[m, n] = even_value
            odd[n - 1, m - 1] = odd_value
            odd[m - 1, n - 1] = odd_value
    return even, odd


def parity_blocks(
    matrix: np.ndarray, indices: list[int], cutoff: int
) -> tuple[np.ndarray, np.ndarray]:
    position = {n: i for i, n in enumerate(indices)}
    even_columns = []
    v0 = np.zeros(len(indices))
    v0[position[0]] = 1
    even_columns.append(v0)
    odd_columns = []
    for n in range(1, cutoff + 1):
        even = np.zeros(len(indices))
        even[position[n]] = 1 / math.sqrt(2)
        even[position[-n]] = 1 / math.sqrt(2)
        even_columns.append(even)

        odd = np.zeros(len(indices))
        odd[position[n]] = 1 / math.sqrt(2)
        odd[position[-n]] = -1 / math.sqrt(2)
        odd_columns.append(odd)
    even_transform = np.column_stack(even_columns)
    odd_transform = np.column_stack(odd_columns)
    return (
        even_transform.T @ matrix @ even_transform,
        odd_transform.T @ matrix @ odd_transform,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=float, default=math.sqrt(13))
    parser.add_argument(
        "--mu",
        type=str,
        help="set lambda=sqrt(mu), preserving the exact decimal mu",
    )
    parser.add_argument("--cutoff", type=int, default=12)
    parser.add_argument("--dps", type=int, default=40)
    parser.add_argument("--high-precision", action="store_true")
    parser.add_argument("--bound-n", type=int)
    parser.add_argument("--bound-m", type=int)
    parser.add_argument("--tail-n", type=int)
    parser.add_argument("--tail-cutoff", type=int)
    parser.add_argument("--tail-limit", type=int)
    parser.add_argument("--residual-small", type=int)
    parser.add_argument("--residual-large", type=int)
    parser.add_argument("--candidate-small", type=int)
    parser.add_argument("--candidate-buffer", type=int)
    args = parser.parse_args()
    mp.mp.dps = args.dps
    lam = mp.sqrt(mp.mpf(args.mu)) if args.mu is not None else mp.mpf(str(args.lam))
    lam_label = float(lam)

    if (args.bound_n is None) != (args.bound_m is None):
        parser.error("--bound-n and --bound-m must be supplied together")
    if args.bound_n is not None:
        length = 2 * mp.log(lam)
        actual = abs(qw_entry(args.bound_n, args.bound_m, length))
        bound = off_diagonal_bound(args.bound_n, args.bound_m, length)
        improved = improved_off_diagonal_bound(
            args.bound_n, args.bound_m, length
        )
        certificate = certificate_off_diagonal_bound(
            args.bound_n, args.bound_m, length
        )
        print(f"lambda={lam_label:.12g}, n={args.bound_n}, m={args.bound_m}")
        print("actual |W_nm|:", mp.nstr(actual, 20))
        print("Theorem O bound:", mp.nstr(bound, 20))
        print("actual / bound:", mp.nstr(actual / bound, 12))
        print("Theorem Q no-log bound:", mp.nstr(improved, 20))
        print("actual / no-log bound:", mp.nstr(actual / improved, 12))
        print("cancellation-preserving bound:", mp.nstr(certificate, 20))
        print("actual / preserving bound:", mp.nstr(actual / certificate, 12))
        return
    tail_args = (args.tail_n, args.tail_cutoff, args.tail_limit)
    if any(value is not None for value in tail_args):
        if args.tail_n is None or args.tail_cutoff is None:
            parser.error("--tail-n and --tail-cutoff must be supplied together")
        limit = args.tail_limit or args.tail_cutoff + 20
        if limit <= args.tail_cutoff:
            parser.error("--tail-limit must exceed --tail-cutoff")
        length = 2 * mp.log(lam)
        partial = mp.mpf("0")
        for m in range(args.tail_cutoff + 1, limit + 1):
            partial += abs(qw_entry(args.tail_n, m, length)) ** 2
            partial += abs(qw_entry(args.tail_n, -m, length)) ** 2
        bound = row_square_tail_bound(args.tail_n, args.tail_cutoff, length)
        improved = improved_row_square_tail_bound(
            args.tail_n, args.tail_cutoff, length
        )
        print(
            f"lambda={lam_label:.12g}, n={args.tail_n}, "
            f"tail |m|>{args.tail_cutoff}"
        )
        print(f"sampled through |m|={limit}")
        print("sampled squared tail:", mp.nstr(partial, 20))
        print("Theorem P full-tail bound:", mp.nstr(bound, 20))
        print("sampled / bound:", mp.nstr(partial / bound, 12))
        print("Theorem R no-log full-tail bound:", mp.nstr(improved, 20))
        print("sampled / no-log bound:", mp.nstr(partial / improved, 12))
        return
    residual_args = (args.residual_small, args.residual_large)
    if any(value is not None for value in residual_args):
        if args.residual_small is None or args.residual_large is None:
            parser.error(
                "--residual-small and --residual-large must be supplied together"
            )
        if args.residual_large <= args.residual_small:
            parser.error("--residual-large must exceed --residual-small")
        even_small, _ = build_parity_blocks_mp(lam, args.residual_small)
        even_large, _ = build_parity_blocks_mp(lam, args.residual_large)
        values_small, vectors_small = mp.eigsy(even_small)
        values_large = mp.eigsy(even_large, eigvals_only=True)
        trial = mp.matrix(args.residual_large + 1, 1)
        for i in range(args.residual_small + 1):
            trial[i] = vectors_small[i, 0]
        mu = values_small[0]
        residual = even_large * trial - mu * trial
        residual_norm = mp.sqrt(
            mp.fsum(abs(residual[i]) ** 2 for i in range(len(residual)))
        )
        below = sum(1 for value in values_large if value < mu)
        print(
            f"lambda={lam_label:.12g}, even cutoff "
            f"{args.residual_small}->{args.residual_large}"
        )
        print("small-section ground Rayleigh value:", mp.nstr(mu, 20))
        print("embedded residual norm:", mp.nstr(residual_norm, 20))
        print("large-section eigenvalues below mu:", below)
        print("large-section lowest values:")
        for value in list(values_large)[: min(6, len(values_large))]:
            print(" ", mp.nstr(value, 20))
        return
    candidate_args = (args.candidate_small, args.candidate_buffer)
    if any(value is not None for value in candidate_args):
        if args.candidate_small is None or args.candidate_buffer is None:
            parser.error(
                "--candidate-small and --candidate-buffer must be supplied "
                "together"
            )
        if args.candidate_buffer < max(1, 2 * args.candidate_small):
            parser.error("--candidate-buffer must be at least 2*candidate-small")
        length = 2 * mp.log(lam)
        even_small, _ = build_parity_blocks_mp(lam, args.candidate_small)
        values_small, vectors_small = mp.eigsy(even_small)
        mu = values_small[0]
        coefficients: dict[int, mp.mpf] = {0: vectors_small[0, 0]}
        for n in range(1, args.candidate_small + 1):
            value = vectors_small[n, 0] / mp.sqrt(2)
            coefficients[n] = value
            coefficients[-n] = value

        core_squared = mp.mpf("0")
        buffer_squared = mp.mpf("0")
        for m in range(-args.candidate_buffer, args.candidate_buffer + 1):
            component = mp.fsum(
                qw_entry(m, n, length) * value
                for n, value in coefficients.items()
            ) - mu * coefficients.get(m, mp.mpf("0"))
            if abs(m) <= args.candidate_small:
                core_squared += abs(component) ** 2
            else:
                buffer_squared += abs(component) ** 2
        analytic_tail = weighted_candidate_tail_bound(
            coefficients, args.candidate_buffer, length
        )
        hybrid_tail = hybrid_even_candidate_tail_bound(
            coefficients, args.candidate_buffer, length
        )
        boundary_sum = mp.fsum(coefficients.values())
        first_abs_moment = mp.fsum(
            abs(value) * abs(n) for n, value in coefficients.items()
        )
        best_tail = min(analytic_tail, hybrid_tail)
        certificate = mp.sqrt(core_squared + buffer_squared + best_tail)
        print(
            f"lambda={lam_label:.12g}, candidate |n|<="
            f"{args.candidate_small}, buffer |m|<={args.candidate_buffer}"
        )
        print("candidate Rayleigh value:", mp.nstr(mu, 20))
        print("boundary coefficient sum:", mp.nstr(boundary_sum, 20))
        print("first absolute moment:", mp.nstr(first_abs_moment, 20))
        print("core residual squared:", mp.nstr(core_squared, 20))
        print("buffer residual squared:", mp.nstr(buffer_squared, 20))
        print("Theorem S generic far-tail majorant:", mp.nstr(analytic_tail, 20))
        print("Corollary W hybrid far-tail majorant:", mp.nstr(hybrid_tail, 20))
        print("best residual upper estimate:", mp.nstr(certificate, 20))
        print("exploratory only: quadrature is not directed rounding")
        return

    if args.high_precision:
        even_mp, odd_mp = build_parity_blocks_mp(lam, args.cutoff)
        even_values_mp = list(mp.eigsy(even_mp, eigvals_only=True))
        odd_values_mp = list(mp.eigsy(odd_mp, eigvals_only=True))
        print(f"lambda={lam_label:.12g}, cutoff={args.cutoff}, dps={args.dps}")
        print("lowest even eigenvalues:")
        for value in even_values_mp[: min(5, len(even_values_mp))]:
            print(" ", mp.nstr(value, 18))
        print("lowest odd eigenvalues:")
        for value in odd_values_mp[: min(5, len(odd_values_mp))]:
            print(" ", mp.nstr(value, 18))
        print(
            "odd-even bottom gap:",
            mp.nstr(odd_values_mp[0] - even_values_mp[0], 18),
        )
        if len(even_values_mp) > 1:
            print(
                "even internal gap:",
                mp.nstr(even_values_mp[1] - even_values_mp[0], 18),
            )
        return

    matrix, indices = build_matrix(lam, args.cutoff)
    symmetry_error = np.max(np.abs(matrix - matrix[::-1, ::-1]))
    even, odd = parity_blocks(matrix, indices, args.cutoff)
    even_values = np.linalg.eigvalsh(even)
    odd_values = np.linalg.eigvalsh(odd)

    print(f"lambda={lam_label:.12g}, cutoff={args.cutoff}")
    print(f"inversion symmetry max error: {symmetry_error:.3e}")
    print("lowest even eigenvalues:", even_values[: min(5, len(even_values))])
    print("lowest odd eigenvalues: ", odd_values[: min(5, len(odd_values))])
    print(f"odd-even bottom gap: {odd_values[0] - even_values[0]:.12e}")
    if len(even_values) > 1:
        print(f"even internal gap: {even_values[1] - even_values[0]:.12e}")


if __name__ == "__main__":
    main()

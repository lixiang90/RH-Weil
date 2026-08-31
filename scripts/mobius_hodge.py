"""Exact finite ledgers for the hard Vaughan and Mobius--Hodge structures.

The routines in this module verify finite identities only.  They do not
provide asymptotic estimates or evidence for the Riemann hypothesis.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

import mpmath as mp
import numpy as np

from qw_matrix import mobius, von_mangoldt


def distinct_prime_divisors(n: int) -> list[int]:
    """Return the distinct prime divisors of a positive integer."""
    if n < 1:
        raise ValueError("n must be positive")
    primes: list[int] = []
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            primes.append(p)
            while remaining % p == 0:
                remaining //= p
        p += 1 if p == 2 else 2
    if remaining > 1:
        primes.append(remaining)
    return primes


def truncated_mobius_divisor_sum(q: int, cutoff: int) -> int:
    """Compute a_U(q)=sum_{d|q,d<=U} mu(d) exactly."""
    if q < 1 or cutoff < 1:
        raise ValueError("q and cutoff must be positive")
    return sum(
        mobius(d) for d in range(1, min(q, cutoff) + 1) if q % d == 0
    )


def _rational_rank(matrix: list[list[int]]) -> int:
    """Compute the rank of a small integer matrix exactly over Q."""
    if not matrix or not matrix[0]:
        return 0
    work = [[Fraction(value, 1) for value in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        pivot_value = work[row][column]
        work[row] = [value / pivot_value for value in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            factor = work[index][column]
            work[index] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[index], work[row])
            ]
        row += 1
        if row == len(work):
            break
    return row


def mobius_threshold_complex_data(
    q: int, cutoff: int, distinguished_prime: int | None = None
) -> dict[str, object]:
    """Return the reduced simplicial Hodge ledger of the threshold complex.

    Faces are subsets S of the prime divisors of q with product(S)<=U.  For
    q>1, the reduced Euler characteristic equals the truncated Mobius defect
    b_U(q)=epsilon(q)-a_U(q).  Rational Betti numbers are computed from the
    reduced boundary complex and are intended only for small finite audits.
    """
    if q < 1 or cutoff < 1:
        raise ValueError("q and cutoff must be positive")
    primes = distinct_prime_divisors(q)
    faces_by_dim: dict[int, list[tuple[int, ...]]] = {-1: [()]}
    for size in range(1, len(primes) + 1):
        faces = [
            face
            for face in itertools.combinations(primes, size)
            if math.prod(face) <= cutoff
        ]
        if faces:
            faces_by_dim[size - 1] = faces

    maximum_dimension = max(faces_by_dim)
    boundary_ranks: dict[int, int] = {}
    for degree in range(0, maximum_dimension + 1):
        columns = faces_by_dim.get(degree, [])
        rows = faces_by_dim.get(degree - 1, [])
        matrix = [[0 for _ in columns] for _ in rows]
        row_position = {face: index for index, face in enumerate(rows)}
        for column, face in enumerate(columns):
            if degree == 0:
                matrix[0][column] = 1
            else:
                for index in range(len(face)):
                    boundary_face = face[:index] + face[index + 1 :]
                    matrix[row_position[boundary_face]][column] = (
                        -1 if index % 2 else 1
                    )
        boundary_ranks[degree] = _rational_rank(matrix)

    betti: dict[int, int] = {}
    for degree in range(-1, maximum_dimension + 1):
        chain_dimension = len(faces_by_dim.get(degree, []))
        incoming_rank = boundary_ranks.get(degree, 0)
        outgoing_rank = boundary_ranks.get(degree + 1, 0)
        betti[degree] = chain_dimension - incoming_rank - outgoing_rank

    a_value = truncated_mobius_divisor_sum(q, cutoff)
    epsilon = 1 if q == 1 else 0
    defect = epsilon - a_value
    reduced_euler_faces = sum(
        ((-1) ** degree) * len(faces)
        for degree, faces in faces_by_dim.items()
    )
    hodge_supertrace = sum(
        ((-1) ** degree) * value for degree, value in betti.items()
    )

    boundary_shell = None
    if primes:
        prime = distinguished_prime or primes[0]
        if prime not in primes:
            raise ValueError("distinguished_prime must divide q")
        other_radical = math.prod(p for p in primes if p != prime)
        shell_terms = [
            (d, mobius(d))
            for d in range(1, min(other_radical, cutoff) + 1)
            if other_radical % d == 0 and cutoff < prime * d
        ]
        boundary_shell = {
            "prime": prime,
            "terms": shell_terms,
            "sum": sum(value for _, value in shell_terms),
        }

    return {
        "q": q,
        "cutoff": cutoff,
        "primes": primes,
        "faces_by_dimension": faces_by_dim,
        "a": a_value,
        "b": defect,
        "reduced_euler_faces": reduced_euler_faces,
        "betti": betti,
        "hodge_supertrace": hodge_supertrace,
        "boundary_shell": boundary_shell,
    }


def _euler_totient(n: int) -> int:
    result = n
    for prime in distinct_prime_divisors(n):
        result -= result // prime
    return result


def mobius_defect_second_moment(cutoff: int, length: int) -> dict[str, object]:
    """Return the exact second moment and its positive gcd-Gram limit form."""
    if cutoff < 1 or length < 1:
        raise ValueError("cutoff and length must be positive")
    values = [
        truncated_mobius_divisor_sum(q, cutoff)
        for q in range(1, length + 1)
    ]
    exact_moment = sum(value * value for value in values)

    gcd_gram = Fraction(0, 1)
    absolute_lcm_sum = Fraction(0, 1)
    for d in range(1, cutoff + 1):
        mu_d = mobius(d)
        for e in range(1, cutoff + 1):
            lcm = d * e // math.gcd(d, e)
            gcd_gram += Fraction(mu_d * mobius(e), lcm)
            absolute_lcm_sum += Fraction(1, lcm)

    positive_decomposition = Fraction(0, 1)
    for r in range(1, cutoff + 1):
        inner = sum(
            (Fraction(mobius(d), d) for d in range(r, cutoff + 1, r)),
            Fraction(0, 1),
        )
        positive_decomposition += _euler_totient(r) * inner * inner

    remainder = Fraction(exact_moment, 1) - length * gcd_gram
    return {
        "values": values,
        "exact_moment": exact_moment,
        "gcd_gram": gcd_gram,
        "positive_decomposition": positive_decomposition,
        "floor_remainder": remainder,
        "absolute_lcm_sum": absolute_lcm_sum,
        "absolute_majorant": length * absolute_lcm_sum,
    }


def canonical_vaughan_hard_coefficients(
    limit: int, cutoff_u: int, cutoff_v: int
) -> dict[str, list[mp.mpf] | list[int]]:
    """Return hard Type-I/II coefficients and their cutoff-invariant sum."""
    if limit < 1 or cutoff_u < 1 or cutoff_v < cutoff_u:
        raise ValueError("require limit>=1 and cutoff_v>=cutoff_u>=1")
    mangoldt = [mp.mpf("0")] + [
        von_mangoldt(n) for n in range(1, limit + 1)
    ]
    a_values = [0] + [
        truncated_mobius_divisor_sum(q, cutoff_u)
        for q in range(1, limit + 1)
    ]
    b_values = [0] + [
        (1 if q == 1 else 0) - a_values[q]
        for q in range(1, limit + 1)
    ]
    hard_i = [mp.mpf("0")] * (limit + 1)
    hard_ii = [mp.mpf("0")] * (limit + 1)
    target = [mp.mpf("0")] * (limit + 1)
    for n in range(1, limit + 1):
        if cutoff_u < n <= cutoff_v:
            hard_i[n] += mangoldt[n]
        for m in range(cutoff_v + 1, n + 1):
            if n % m == 0 and mangoldt[m]:
                quotient = n // m
                hard_i[n] += mangoldt[m] * a_values[quotient]
                hard_ii[n] += mangoldt[m] * b_values[quotient]
        if n > cutoff_u:
            target[n] = mangoldt[n]
    return {
        "hard_i": hard_i,
        "hard_ii": hard_ii,
        "target": target,
        "a": a_values,
        "b": b_values,
    }


def two_channel_hadamard_gram(
    first: np.ndarray, second: np.ndarray
) -> dict[str, np.ndarray | float]:
    """Return the physical/primitive Hadamard normal form of a 2x2 Gram."""
    first = np.asarray(first, dtype=complex)
    second = np.asarray(second, dtype=complex)
    if first.shape != second.shape:
        raise ValueError("the two channel vectors must have the same shape")
    gram = np.array(
        [
            [np.vdot(first, first), np.vdot(first, second)],
            [np.vdot(second, first), np.vdot(second, second)],
        ],
        dtype=complex,
    )
    hadamard = np.array([[1, 1], [1, -1]], dtype=float) / math.sqrt(2)
    transformed = hadamard @ gram @ hadamard.T
    physical = first + second
    primitive = first - second
    physical_energy = float(np.vdot(physical, physical).real)
    primitive_energy = float(np.vdot(primitive, primitive).real)
    cross_real = float(np.vdot(first, second).real)
    return {
        "gram": gram,
        "hadamard_gram": transformed,
        "physical": physical,
        "primitive": primitive,
        "physical_energy": physical_energy,
        "primitive_energy": primitive_energy,
        "cross_real": cross_real,
        "cross_identity_residual": physical_energy
        - primitive_energy
        - 4 * cross_real,
    }


def factorization_fiber_bessel_lower_bound(products: list[int]) -> int:
    """Largest exact-product fiber, a normalized synthesis-norm lower bound."""
    if not products or any(product < 1 for product in products):
        raise ValueError("products must be a nonempty list of positive integers")
    counts: dict[int, int] = {}
    for product in products:
        counts[product] = counts.get(product, 0) + 1
    return max(counts.values())

"""Exact finite-field count and rational energy certificate, without zeta zeros.

This is one fixed arithmetic example for C026, not a GRH test for number fields.
The all-degree recurrence additionally uses genus-one rationality, documented in
the companion research note; counts alone at finitely many degrees do not prove it.
"""
from __future__ import annotations

from fractions import Fraction
import json


def extension_count(p: int, modulus: tuple[int, ...]) -> int:
    """Count y^2=x^3+x+1 over F_p[X]/modulus, plus its infinity point."""
    degree = len(modulus) - 1
    assert modulus[-1] == 1
    size = p ** degree

    def coefficients(value):
        result = []
        for _ in range(degree):
            result.append(value % p)
            value //= p
        return result

    vectors = [coefficients(value) for value in range(size)]

    def encode(values):
        return sum((value % p) * p ** i for i, value in enumerate(values))

    def add(left, right):
        return encode([a + b for a, b in zip(vectors[left], vectors[right])])

    def multiply(left, right):
        values = [0] * (2 * degree - 1)
        for i, a in enumerate(vectors[left]):
            for j, b in enumerate(vectors[right]):
                values[i + j] += a * b
        for i in range(len(values) - 1, degree - 1, -1):
            for j in range(degree):
                values[i - degree + j] -= values[i] * modulus[j]
        return encode(values[:degree])

    square_counts = [0] * size
    for y in range(size):
        square_counts[multiply(y, y)] += 1
    return 1 + sum(square_counts[add(add(multiply(multiply(x, x), x), x), 1)]
                   for x in range(size))


def multiply_matrix(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def certificate():
    # X^2+2 and X^3+X+1 have no F5 roots, hence are irreducible.
    moduli = [(0, 1), (2, 0, 1), (1, 1, 0, 1)]
    for polynomial in moduli[1:]:
        assert all(sum(c * x ** i for i, c in enumerate(polynomial)) % 5
                   for x in range(5))
    counts = [extension_count(5, modulus) for modulus in moduli]
    q, trace = 5, 6 - counts[0]
    matrix = [[0, -q], [1, trace]]
    energy = [[Fraction(1), Fraction(trace, 2)],
              [Fraction(trace, 2), Fraction(q)]]
    transpose = list(map(list, zip(*matrix)))
    assert multiply_matrix(multiply_matrix(transpose, energy), matrix) == [
        [q * entry for entry in row] for row in energy]
    determinant = energy[0][0] * energy[1][1] - energy[0][1] ** 2
    assert energy[0][0] > 0 and determinant > 0
    previous, current = 2, trace
    recurrence = [current]
    for _ in range(2, 4):
        previous, current = current, trace * current - q * previous
        recurrence.append(current)
    predicted = [q ** n + 1 - recurrence[n - 1] for n in range(1, 4)]
    assert counts == predicted
    return {
        "curve": "y^2=x^3+x+1 over F5, including infinity",
        "discriminant_mod5": (-16 * (4 + 27)) % 5,
        "extension_point_counts_direct": counts,
        "trace": trace,
        "A": matrix,
        "H": [[str(entry) for entry in row] for row in energy],
        "leading_principal_minors_H": ["1", str(determinant)],
        "exact_identity": "A^T H A=5H",
        "normalized_operator": "U=A/sqrt(5), U^* H U=H",
        "trace_recurrence": "S_0=2, S_1=-3, S_n=-3*S_(n-1)-5*S_(n-2)",
        "all_degree_dependency": "Genus-one rationality and functional equation; not finite count extrapolation",
        "zeta_zero_input": False,
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), ensure_ascii=False, indent=2))

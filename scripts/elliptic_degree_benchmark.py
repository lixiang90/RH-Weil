"""Exact finite normalization checks for the E/F5 degree-positive PLF model.

All arithmetic is rational or finite-field arithmetic.  Geometric degree
theorems and the all-extension zeta identity are proved/cited in note 307,
not inferred from these finitely many checks.
"""

from collections import Counter
from fractions import Fraction as Q


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def scaled(a, c):
    return [[c * x for x in row] for row in a]


def field25_mul(x, y):
    # F5[t]/(t^2-2); 2 is a nonsquare in F5.
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % 5, (a * d + b * c) % 5)


def main():
    identity = [[1, 0], [0, 1]]
    frobenius = [[0, -5], [1, -2]]
    gram = [[1, -1], [-1, 5]]
    omega = [[0, 1], [-1, 0]]
    j = scaled([[1, -5], [1, -1]], Q(1, 2))
    assert gram[0][0] > 0 and gram[0][0] * gram[1][1] - gram[0][1]**2 == 4
    assert matmul(matmul(transpose(frobenius), gram), frobenius) == scaled(gram, 5)
    assert matmul(matmul(transpose(frobenius), omega), frobenius) == scaled(omega, 5)
    assert matmul(j, j) == scaled(identity, -1)
    assert matmul(j, frobenius) == matmul(frobenius, j)
    assert scaled(matmul(omega, j), 2) == gram
    square = matmul(frobenius, frobenius)
    assert all(square[i][k] + 2 * frobenius[i][k] + 5 * identity[i][k] == 0
               for i in range(2) for k in range(2))
    counts = [sum((y * y - (x**3 - x)) % 5 == 0 for y in range(5)) for x in range(5)]
    assert counts == [1, 1, 2, 2, 1]
    n1 = 1 + sum(counts)
    elements = [(a, b) for a in range(5) for b in range(5)]
    squares = Counter(field25_mul(y, y) for y in elements)
    n2 = 1
    for x in elements:
        cube = field25_mul(field25_mul(x, x), x)
        rhs = ((cube[0] - x[0]) % 5, (cube[1] - x[1]) % 5)
        n2 += squares[rhs]
    assert n1 == 8 == 1 + 5 - sum(frobenius[i][i] for i in range(2))
    assert n2 == 32 == 1 + 25 - sum(square[i][i] for i in range(2))
    print("PASS: exact degree Gram, primitive J, Frobenius/cup similitudes, and quadratic relation.")
    print(f"PASS: independent finite-field enumeration N1={n1}, N2={n2}.")
    print("Scope: concrete finite model checks; no general arithmetic RH assertion.")


if __name__ == "__main__":
    main()

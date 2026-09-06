"""Exact finite checks for the boundary-aware quartic certificate (note 306).

Polynomial coefficient identities certify the scalar inequalities algebraically.
The finite configuration sweep is a regression, not a proof of arbitrary
matrices or of any asymptotic prime-side input.
"""

from fractions import Fraction as F
from itertools import product
from math import comb


def multiply(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def certificate_bounds(moments, e, sigma):
    m0, m1, m2, m3, m4 = moments
    assert F(-3) <= sigma < F(3, 4)
    a = 1 - sigma
    v = m2 - 2 * m1 + m0
    w = m4 - 4 * m3 + 6 * m2 - 4 * m1 + m0
    delta = (1 - 2 * sigma) * (m0 - 1) + 4 * a * (m1 - 1)
    r = 1 - (sigma**2 - 2 * v * sigma + w) / a**2
    return (
        r + (delta - 4 * a * e) / a**2,
        (1 + r) / 2 + (delta - (3 + sigma) * a * e) / (2 * a**2),
    )


def audit_polynomials():
    # Compare every coefficient as a polynomial in sigma, not a sampled grid.
    # A coefficient is [constant, sigma coefficient, ...].
    p = [[0], [8, -8], [-6, 2], [4], [-1]]
    square = [[0] for _ in range(5)]
    factors = [[1, -1], [-2], [1]]  # x^2 - 2x + 1 - sigma
    for i, left in enumerate(factors):
        for j, right in enumerate(factors):
            terms = multiply(left, right)
            while len(square[i + j]) < len(terms):
                square[i + j].append(F(0))
            for k, term in enumerate(terms):
                square[i + j][k] += term
    affine = [[1, -2, 1], [4, -4], [0], [0], [0]]
    for k in range(5):
        for degree in range(3):
            value = lambda seq: seq[degree] if degree < len(seq) else F(0)
            assert value(affine[k]) - value(square[k]) == value(p[k])
    # (x-2)^2 (x^2+2-2 sigma) = 8(1-sigma)-p_sigma(x).
    for sigma_power in (0, 1):
        tail = [2, 0, 1] if sigma_power == 0 else [-2]
        expansion = multiply([4, -4, 1], tail)
        expansion += [F(0)] * (5 - len(expansion))
        for k in range(5):
            pk = p[k][sigma_power] if sigma_power < len(p[k]) else F(0)
            constant = (8 if sigma_power == 0 else -8) if k == 0 else 0
            assert expansion[k] == constant - pk
    print("PASS: exact polynomial identities in both x and sigma.")
    print("Scope: a>0 and 6-2sigma>0 give the x<=0 signs; sigma>=-3 gives the D ledger sign.")


def audit_boundary_configurations():
    atoms = tuple(map(F, [-2, 0, 1, 2, 3])) + (F(-1, 5), F(1, 5))
    sigmas = (F(-3), F(-1), F(0), F(1, 8), F(7, 10))
    checked = 0
    for eigenvalues in product(atoms, repeat=3):
        positive = sorted((x for x in eigenvalues if x > 0), reverse=True)
        for b in range(len(positive) + 1):
            covered = positive[b:]
            trace_p = sum(covered, F(0))
            s = max(F(len(covered)), trace_p)
            d_count = s + b
            for total in (F(2), F(3), F(7)):
                e1 = max(F(0), s + 2 * b - total)
                # Diagonal P covers precisely the undeleted positive eigenvalues;
                # Q consists of the removed positive and all nonpositive ones.
                assert trace_p <= s and len(covered) <= s
                assert s + 2 * b <= total + e1
                moments = tuple(sum((x**k for x in eigenvalues), F(0)) / total for k in range(5))
                for sigma in sigmas:
                    simple, distinct = certificate_bounds(moments, e1 / total, sigma)
                    assert s / total >= simple
                    assert d_count / total >= distinct
                    checked += 1
    # Old counterexample: G=Q=I, P=0, s=0, b=D=N, E1=N.
    moments = (F(1),) * 5
    assert certificate_bounds(moments, F(0), F(0)) == (F(1), F(1))
    simple, distinct = certificate_bounds(moments, F(1), F(0))
    assert simple <= 0 and distinct <= 1
    print(f"PASS: {checked} rational configurations/parameters; missing-E1 counterexample detected.")


def audit_extremal_moments():
    # Symmetric atoms 1 +/- sqrt(1/8), weight 8/21 each. Odd powers
    # of the square root cancel, so all moment calculations are rational.
    moments = tuple(
        F(16, 21) * sum(F(comb(k, j)) * F(1, 8)**(j // 2) for j in range(0, k + 1, 2))
        + F(5, 42) * (F(2)**k + (F(1) if k == 0 else F(0)))
        for k in range(5)
    )
    assert moments == (F(1), F(1), F(4, 3), F(2), F(13, 4))
    assert certificate_bounds(moments, F(0), F(1, 8)) == (F(16, 21), F(37, 42))
    print("PASS: exact extremal four moments and 16/21, 37/42.")


if __name__ == "__main__":
    audit_polynomials()
    audit_boundary_configurations()
    audit_extremal_moments()
    print("No analytic fourth-moment estimate or RH assertion is certified.")

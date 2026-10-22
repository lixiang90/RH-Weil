"""Exact local controls for the function-field evaluation/moving source gate.

This checks finite-field ranks and a formal branch expansion, not RH, a
moving lemma, a global collision bound, or any classical-zeta estimate.
"""
from __future__ import annotations

import json


P = 5


def det(a):
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % P


def f(x):
    return (x**5 - x + 1) % P


def mul(a, b, order=4):
    return [sum(a[i] * b[n - i] for i in range(n + 1)) % P
            for n in range(order)]


def main():
    affine = [(x, y) for x in range(P) for y in range(P)
              if y * y % P == f(x)]
    # f'=-1, so the degree-five hyperelliptic equation is squarefree.
    assert all(y != 0 for _, y in affine)
    controls = []
    for x, y in affine:
        h0 = pow(y, -1, P)
        # y'=f'(x)/(2y); h=(1/y), h'=-y'/y^2.
        y1 = -pow(2 * y, -1, P) % P
        h1 = -y1 * pow(y, -2, P) % P
        ordinary = [[h0, h0], [x * h0 % P, x * h0 % P]]
        jets = [[h0, x * h0 % P], [h1, (h0 + x * h1) % P]]
        assert det(ordinary) == 0
        assert det(jets) == h0 * h0 % P != 0
        controls.append({"point": [x, y], "ordinary_det": 0,
                         "jet_matrix": jets, "jet_det": det(jets)})
    # At a geometric branch point a, write t=y, x=a+delta.
    # f(a+delta)-f(a)=delta^5-delta=t^2; modulo t^4 delta=-t^2.
    delta = [0, 0, 4, 0]
    delta5 = [1, 0, 0, 0]
    for _ in range(5):
        delta5 = mul(delta5, delta)
    lhs = [(delta5[i] - delta[i]) % P for i in range(4)]
    assert lhs == [0, 0, 1, 0]
    # dx/y=-2 dt+O(t^8)dt. Modulo t^2, x=a, so the two
    # columns are dependent for every a (no extension-field sampling).
    branch_identity = "[[ -2, -2*a ], [ 0, 0 ]] modulo 5"
    conjugate = [[1, 4], [0, 0]]  # (0,1) and (0,-1), x frames
    generic = [[1, 1], [0, 1]]    # (0,1) and (1,1)
    assert det(conjugate) == 0 and det(generic) == 1
    output = {
        "scope": "local exact checks; global RR/moving and positivity are not computed",
        "curve": "smooth projective model of y^2=x^5-x+1 over F_5",
        "squarefree_derivative_mod_5": 4,
        "genus_by_separable_degree_two_cover": 2,
        "rational_point_count_including_infinity": len(affine) + 1,
        "nonbranch_double_point_controls": controls,
        "branch_delta_mod_t4": delta,
        "branch_equation_mod_t4": lhs,
        "branch_length_two_jet_matrix": branch_identity,
        "branch_jet_rank": 1,
        "reduced_conjugate_matrix": conjugate,
        "reduced_conjugate_det": det(conjugate),
        "distinct_x_control_matrix": generic,
        "distinct_x_control_det": det(generic),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

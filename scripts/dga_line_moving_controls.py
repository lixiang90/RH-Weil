"""Exact controls for the free graph-line source admission.

Polynomial identities specialize to the actual DGA. The finite matrices
check old model controls; neither calculation supplies a Picard family,
an arithmetic metric, or full Weil positivity for classical zeta.
"""
from __future__ import annotations

from fractions import Fraction as F
import json


def add(a, b):
    c = a.copy()
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
        if c[k] == 0:
            del c[k]
    return c


def neg(a):
    return {k: -v for k, v in a.items()}


def mul(a, b):
    c = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            key = (i + k, j + l)
            c[key] = c.get(key, 0) + u * v
    return {k: v for k, v in c.items() if v}


def mm(a, b):
    return [[add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


def mv(a, v):
    return [add(mul(a[i][0], v[0]), mul(a[i][1], v[1]))
            for i in range(2)]


def main():
    zero, one = {}, {(0, 0): 1}
    x, q = {(1, 0): 1}, {(0, 1): 1}
    y = add(x, q)
    identity = [[one, zero], [zero, one]]
    projection = [[one, zero], [x, zero]]
    transport = [[one, zero], [q, one]]
    inverse = [[one, zero], [neg(q), one]]
    vx, vy = [one, x], [one, y]
    sx, sy = [x, mul(x, x)], [y, mul(y, y)]
    assert mm(projection, projection) == projection
    assert mm(transport, inverse) == identity
    assert mv(transport, vx) == vy
    # In C[x,q,eta], |eta|=-1 and d eta=q. Therefore the
    # following right side is d(eta*v_y), with no analytic limit.
    moved = mv(transport, sx)
    defect = [add(sy[i], neg(moved[i])) for i in range(2)]
    assert defect == [mul(q, a) for a in vy]
    # Boundary localization has d(eta/q)=1. This is a formal
    # contracting homotopy, not a numerical test of an inverse norm.
    continuous = []
    for d in [F(-1, 16), F(1, 16)]:
        z = [[F(0), -d], [F(1), F(0)]]
        zdag = [[-a for a in row] for row in z]
        product = [[sum(z[i][k] * zdag[k][j] for k in range(2))
                    for j in range(2)] for i in range(2)]
        assert product == [[d, F(0)], [F(0), d]]
        continuous.append({"d": str(d), "trace_z_zdagger": str(2*d),
                           "graph_line_class": "free in both cases"})
    # On the genuine genus-two curve from the previous source gate,
    # P=(0,1), Q=(1,1) give independent canonical evaluations.
    determinant_mod5 = (1 * 1 - 1 * 0) % 5
    assert determinant_mod5 == 1
    out = {
        "scope": "formal DGA identities and finite old-model checks only",
        "graph_projection_idempotent": True,
        "principal_transport_invertible": True,
        "graph_frame_transported": True,
        "marked_defect": "q*v_(x+q) = d(eta*v_(x+q))",
        "boundary_localization": "d(eta/q)=1; localized DGA contractible",
        "continuous_controls": continuous,
        "function_field_twist_control": {
            "curve": "y^2=x^5-x+1 over F5",
            "points": [[0, 1], [1, 1]],
            "canonical_evaluation_determinant_mod5": determinant_mod5,
            "proof_responsibility": "RR and divisor argument, not finite ranks alone",
        },
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

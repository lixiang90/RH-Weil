"""Symbolic rational certificate for 447; does not certify cited analysis."""

from fractions import Fraction as F
from decimal import Decimal, localcontext
import json

from hybrid_high_continuation_exact_audit import ROOT, SOURCE, EXPECTED_SOURCE, digest, poly, add, scale, mul


def evaluate(p, t, y):
    return sum(c * t**dt * y**dy for (dt, dy), c in p.items())


def audit():
    assert digest(SOURCE) == EXPECTED_SOURCE
    t, y = {(1, 0): F(1)}, {(0, 1): F(1)}
    y2, y3 = mul(y, y), mul(y, y, y)
    py = add(poly(7), scale(y, 18), scale(y2, 8))
    j0 = add(poly(185), scale(y, 170))
    j1 = add(poly(-138), scale(y, 12), scale(y2, 96))
    v = add(poly(3), scale(y, 8), scale(mul(t, y), 48))
    w = add(poly(468), scale(t, 864))
    # Directly clear 10368 J(-E_t), separating the delta powers.
    C = scale(mul(j0, add(poly(1), scale(t, -60))), 2)
    B = add(scale(mul(j1, add(poly(1), scale(t, -60))), 2),
            scale(mul(j0, v), 2), scale(mul(w, py), -F(5, 6)))
    A = add(scale(mul(j1, v), 2), mul(w, py))
    expected_A = add(poly(2448), scale(y, 6288), scale(y2, 4512), scale(y3, 1536),
                     mul(t, add(poly(6048), scale(y, 2304), scale(y2, 8064), scale(y3, 9216))))
    expected_B = add(poly(-1896), scale(y, -3016), scale(y2, -208),
                     mul(t, add(poly(11520), scale(y, 3360), scale(y2, -960))))
    expected_C = add(poly(370), scale(y, 340), mul(t, add(poly(-22200), scale(y, -20400))))
    assert A == expected_A and B == expected_B and C == expected_C
    rows = (
        (28224, -164747520, -669772800),
        (1198848, -664266240, -775526400),
        (5344448, -877278720, -893260800),
        (7154944, -484362240, -1469952000),
        (2045696, -113203200, -752947200),
    )
    Q = add(scale(mul(A, C), 4), scale(mul(B, B), -1))
    expected_Q = {(dt, dy): F(c) for dy, row in enumerate(rows) for dt, c in enumerate(row) if c}
    assert Q == expected_Q

    def q0(vt):
        return F(rows[0][0]) + rows[0][1] * vt + rows[0][2] * vt**2

    # Unique positive root: q0 is strictly decreasing on t>=0.
    lower, upper = F(1, 5842), F(1, 5841)
    assert q0(lower) > 0 > q0(upper)
    assert upper < F(1, 5800) < F(1, 5000)
    others_lower = (1000000, 5000000, 7000000, 2000000)
    for row, bound in zip(rows[1:], others_lower):
        assert row[1] < 0 and row[2] < 0
        assert F(row[0]) + row[1] * F(1, 5000) + row[2] * F(1, 5000)**2 > bound
    assert all(c > 0 for c in A.values())

    safe = F(1, 5900)
    # Sum duplicate powers explicitly before making the Q/A certificate.
    A_safe = { (0, dy): sum(c * safe**dt for (dt, yy), c in A.items() if yy == dy)
               for dy in range(4) }
    Q_safe = { (0, dy): sum(c * safe**dt for (dt, yy), c in Q.items() if yy == dy)
               for dy in range(5) }
    a0, q_zero = A_safe[(0, 0)], Q_safe[(0, 0)]
    ratio_polynomial = add(scale(Q_safe, a0), scale(A_safe, -q_zero))
    assert ratio_polynomial and all(c > 0 for c in ratio_polynomial.values())
    p_margin = q_zero / (4 * a0)
    E_margin = p_margin / 25920
    assert p_margin == F(85046, 2960089)
    assert E_margin == F(42523, 38362753440) > F(1, 1000000)
    assert E_margin - F(1, 1000000) == F(26001541, 239767209000000)

    def geometry(vt):
        ell, lx, ly = F(1, 6) + vt, F(17, 48) - vt / 2, F(23, 48) - vt / 2
        h, sigma = F(13, 16) + F(3, 2) * vt, F(7, 8) - vt / 4
        assert sigma + lx / 2 - 1 + h / 6 == sigma - F(11, 16)
        return ell, lx, ly, h, sigma

    ell, lx, ly, h, sigma = geometry(safe)
    assert (ell, lx, ly, h, sigma) == (F(2953,17700),F(25069,70800),F(33919,70800),F(19181,23600),F(20649,23600))
    assert -F(7,1200)+F(32,25)*safe == -F(9941,1770000)
    assert -F(49,14400)+F(177,200)*safe == -F(1171,360000)
    assert -F(79,800)+F(51,100)*safe+F(63,5000) == -F(20311,236000)
    assert 5*ell-h == F(1517,70800)
    assert ell/h-F(7,37) == F(34243,2129091)
    assert min(6*sigma-F(401,100),sigma-F(3,50),F(47,50)) == F(19233,23600)
    assert min(sigma-F(1,20),3*sigma-F(3,2)) == F(19469,23600)

    # Uniform rational bounds enclosing the algebraic critical geometry.
    vt_max = F(1,5800)
    ell_max, _, ly_min, h_max, sigma_min = geometry(vt_max)
    assert F(1,6) < ell_max < F(1,5)
    assert sigma_min > F(5,6) and sigma_min > F(401,600)
    assert sigma_min-F(3,50) > F(81,100)
    assert sigma_min-F(1,20) > F(82,100)
    assert sigma_min+F(1,2) > 1+F(1,3)
    assert -F(7,1200)+F(32,25)*vt_max < -F(1,200)
    assert -F(49,14400)+F(177,200)*vt_max < -F(2,625)
    assert -F(79,800)+F(51,100)*vt_max+F(63,5000) < -F(2,25)
    assert vt_max/128 < F(1,48)
    assert h_max+vt_max/128 < 1
    stationary = lambda vt: (1896-11520*vt)/(4896+12096*vt)
    assert F(1,3) < stationary(vt_max) <= stationary(F(0)) < F(2,5)

    fail = F(1,5800)
    delta = stationary(fail)
    assert delta == F(57215,147963)
    assert F(1,50) < delta < F(3,4)
    p_fail = evaluate(A,fail,F(0))*delta**2+evaluate(B,fail,F(0))*delta+evaluate(C,fail,F(0))
    J_fail = (F(5,6)-delta)*F(37,18)+delta*F(7,9)
    assert p_fail == -F(29297,1430309) and J_fail == F(2164165,1775556)
    assert -p_fail/(10368*J_fail) == F(29297,18075106080) > 0

    with localcontext() as ctx:
        ctx.prec = 60
        Adec, Bdec, Cdec = Decimal(669772800), Decimal(164747520), Decimal(28224)
        root = 2*Cdec/(Bdec+(Bdec*Bdec+4*Adec*Cdec).sqrt())
        sigma_critical = Decimal(7)/8-root/4
        root_decimal, boundary_decimal = str(root), str(sigma_critical)
    note = ROOT / "notes" / "447-larger-slot-discriminant-and-critical-strip.md"
    report = {
        "scope": "Symbolic rational coefficients, root isolation and geometry bounds only. The cited physical arithmetic, analytic estimates, family continuation and external Lean are not certified by this script.",
        "source_sha256_canonical_lf": digest(SOURCE),
        "note_sha256_canonical_lf": digest(note),
        "symbolic_ABC_and_discriminant_identity": True,
        "discriminant_nonzero_coefficients": len(Q),
        "safe_rational_t": str(safe),
        "safe_rational_boundary": str(sigma),
        "safe_rational_extra_margin": str(E_margin),
        "ratio_polynomial_positive_coefficients": {str(key[1]):str(value) for key,value in ratio_polynomial.items()},
        "critical_root_isolating_interval": [str(lower),str(upper)],
        "critical_t_decimal_for_orientation_only": root_decimal,
        "critical_boundary_decimal_for_orientation_only": boundary_decimal,
        "critical_extra_margin_zero": True,
        "critical_high_gap_paid_by_global_beta_minus_sigma": "Analytic/quantifier argument in note 447, not a machine check of the L family.",
        "failure_parameter": {"t":str(fail),"delta":str(delta),"q":str(delta/2),"E_sigma":str(-p_fail/(10368*J_fail))},
    }
    path = ROOT / "output" / "hybrid-larger-slot-discriminant-audit.json"
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    audit()

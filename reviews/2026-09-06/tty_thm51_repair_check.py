import sys
sys.stdout.reconfigure(encoding="utf-8")
import sympy as S

x, t = S.symbols("x t", real=True)
R = S.Rational
bL, bH = R(9, 2)*(3*x-2), R(8, 3)*(2*x-1)

# name, sigma_left, sigma_right, Jutila k, tau0, c, M(tau0)
rows = [
    ("I",   R(17,22), R(41,53), 4, bL, 24-32*x,     S.Integer(1)),
    ("II",  R(41,53), R(38,49), 4, bL, (7-11*x)/2,  S.Integer(1)),
    ("III", R(38,49), R(25,32), 4, bH, (7-11*x)/2,  S.Integer(1)),
    ("IV",  R(25,32), R(11,14), 3, bH, 18-24*x,     2*bH-2),
    ("V",   R(11,14), R(4,5),   3, bH, (10-16*x)/3, 2*bH-2),
]

def interior_root_count(poly, lo, hi):
    # Remove endpoint roots before exact real-root counting.
    p = poly
    for endpoint in (lo, hi):
        factor = S.Poly(x-endpoint, x, domain=S.QQ)
        while p.degree() > 0 and p.eval(endpoint) == 0:
            p = p.exquo(factor)
    return p.count_roots(lo, hi)

def certify(label, expr, lo, hi, strict=False):
    expr = S.cancel(expr)
    n, d = S.fraction(expr)
    mid = (lo+hi)/2
    if d.subs(x, mid) < 0:
        n, d = -n, -d
    pn, pd = (S.Poly(z, x, domain=S.QQ) for z in (n, d))

    assert pd.eval(lo) > 0 and pd.eval(hi) > 0
    assert pd.eval(mid) > 0 and pd.count_roots(lo, hi) == 0

    if pn.is_zero:
        assert not strict, label
        roots = []
    else:
        values = [pn.eval(z) for z in (lo, mid, hi)]
        assert all(v > 0 if strict else v >= 0 for v in values), label
        assert interior_root_count(pn, lo, hi) == 0, label
        roots = pn.intervals(eps=R(1, 10**12))

    print(label, "NUM =", S.factor(n), "DEN =", S.factor(d),
          "ISOLATORS =", roots)
    return 1

count = 0
for name, lo, hi, k, b, c, Mb in rows:
    q = 3*(1-x)/b
    a = 2*b/3
    h = -c/(1-q)
    low = name in ("I", "II")
    p = 11-16*x+t if low else R(5,4)*t-(1+x)
    B = R(5,4)*t-(1+x)
    ph = p.subs(t, h)
    pb = p.subs(t, b)
    c1 = (4-R(2,k))-(6-R(2,k))*x
    c2 = k*(6-8*x)
    b_other = bH if low else bL
    b0 = 2-2*x

    checks = [
        ("b_positive", b, True),
        ("q_minus_third", q-R(1,3), True),
        ("half_minus_q", R(1,2)-q, True),
        ("tau0_is_min", b_other-b, False),
        ("c_ge_Jutila_c1", c-c1, False),
        ("c_ge_Jutila_c2", c-c2, False),
        ("M_branch", R(3,2)-b if name in ("I","II","III")
                     else b-R(3,2), False),
        ("h_ge_a", h-a, False),
        ("h_le_b", b-h, False),
        ("rho_le_1_constant", 1-b0, False),
        ("rho_le_1_linear", 1-b-c, False),
        ("rho_le_4_minus_2tau_constant", 4-2*b-b0, False),
        ("rho_le_4_minus_2tau_linear", 4-3*b-c, False),
        ("alpha1_zero_at_h", (h+10-14*x)/3, False),
        ("alpha1_positive_at_h", (h+10-14*x)/3-ph/6, False),
        ("F2_zero_at_h", (q-R(1,3))*h-(16-20*x)/3, False),
        ("F1_positive_at_b", 3-3*x-(pb+2-2*x), False),
        ("F2_positive_at_b",
         3-3*x-(b/3+(16-20*x)/3+pb/3), False),
        ("F5_envelope_at_b",
         3-3*x-(4*b/3+(46-68*x)/3+Mb-2*pb/3), False),
        ("p_dominates_B_at_b", pb-B.subs(t,b), False),
        ("zeta_endpoint",
         4-4*x-(8*b/3-12*(x-R(1,2))), False),
    ]

    # c is exactly the maximum of the two Jutila constants.
    assert S.simplify(c-c1) == 0 or S.simplify(c-c2) == 0
    # b is exactly one of the two candidate tau0 values.
    assert S.simplify(b-bL) == 0 or S.simplify(b-bH) == 0

    # Slopes needed for all tau endpoint reductions.
    for label, slope_gap in [
        ("alpha1_zero_slope", R(1,3)),
        ("alpha1_positive_slope", R(1,3)-S.diff(p,t)/6),
        ("F1_positive_slope_minus_q", S.diff(p,t)-q),
        ("F2_positive_slope_minus_q",
         R(1,3)+S.diff(p,t)/3-q),
        ("F5_envelope_slope_minus_q",
         R(4,3)-2*S.diff(p,t)/3-q),
    ]:
        checks.append((label, slope_gap, True))

    for label, expression, strict in checks:
        count += certify(name+"."+label, expression, lo, hi, strict)

    print("PASS", name, "interval", (lo,hi), "tau endpoints",
          [S.factor(z) for z in (a,h,b)])

print("ALL CHECKS PASSED:", count)

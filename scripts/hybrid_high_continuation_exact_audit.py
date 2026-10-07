"""Exact algebra for 442--445; no certification of the cited analytic inputs."""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex")
EXPECTED_SOURCE = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"


def digest(path):
    s = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(s.encode()).hexdigest()


# Bivariate polynomial coefficients: keys are (degree_delta, degree_y).
def poly(c):
    return {(0, 0): F(c)} if c else {}


def add(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(p, c):
    return {key: value * c for key, value in p.items() if value * c}


def mul(*terms):
    out = poly(1)
    for term in terms:
        nxt = {}
        for (d1, y1), c1 in out.items():
            for (d2, y2), c2 in term.items():
                key = d1 + d2, y1 + y2
                nxt[key] = nxt.get(key, F(0)) + c1 * c2
        out = {key: value for key, value in nxt.items() if value}
    return out


def symbolic_certificate():
    d, y = {(1, 0): F(1)}, {(0, 1): F(1)}
    y2 = mul(y, y)
    v = add(poly(51), scale(y, 41))
    py = add(poly(7), scale(y, 18), scale(y2, 8))
    jy = add(poly(185), scale(y, 170), mul(add(poly(-138), scale(y, 12), scale(y2, 96)), d))
    # 10368 J(-E0), after clearing the exact rational J and P expressions.
    lhs = mul(v, add(
        scale(mul(jy, add(poly(1), mul(add(poly(3), scale(y, 8)), d))), 2),
        scale(mul(add(poly(F(5, 6)), scale(d, -1)), d, py), -468),
    ))
    square_base = add(scale(mul(v, d), 4), poly(-79))
    rhs = add(
        mul(add(poly(3), scale(y, 5)), add(mul(square_base, square_base), poly(49))),
        scale(mul(y, add(
            scale(mul(v, d, add(
                mul(add(poly(1), scale(y, 3)), add(poly(15), scale(y, 32)), d),
                poly(9), scale(y, -13),
            )), 4), poly(265), scale(y, 3485),
        )), 4),
    )
    assert lhs == rhs
    # Bounds used with the displayed nonnegative representation, not sampling.
    assert 9 - 13 * F(1, 2) == F(5, 2) > 0
    assert add(scale(add(poly(3), scale(y, 5)), 17), scale(v, -1)) == scale(y, 44)
    return {"coefficient_identity": True, "nonzero_coefficients": len(lhs)}


def audit():
    assert digest(SOURCE) == EXPECTED_SOURCE
    ell0, t, b = F(1, 6), F(1, 20000), F(1, 8)
    ell, sigma0 = ell0 + t, F(7, 8)
    sigma = sigma0 - t / 4
    lx, ly, h = (1 - ell - b) / 2, (1 - ell + b) / 2, (1 + 3 * ell + b) / 2
    h0, alpha, z0 = F(13, 16), F(5, 6), F(17, 50)
    mad = F(49, 440640) - F(5, 3) * t
    zeta = mad / 32
    assert sigma == F(69999, 80000) and h == F(32503, 40000)
    assert mad == F(307, 11016000) > 0
    assert sigma + lx / 2 - 1 + h / 6 == sigma - F(11, 16)
    assert min(6 * sigma - F(401, 100), sigma - F(3, 50), F(47, 50)) == F(65199, 80000)
    assert min(sigma - F(1, 20), 3 * sigma - F(3, 2)) == F(65999, 80000)
    assert sigma + F(1, 2) > 1 + F(1, 3)
    assert ell / h - F(7, 37) == F(57659, 3607833)
    assert 5 * ell - h == F(2521, 120000)
    assert zeta < min(5 * ell - h, 1 - h)
    assert ell / (h + zeta) > F(1, 5) > F(7, 37)
    assert mad - 2 * zeta == F(307, 11750400)

    def exponent(ell_v, sigma_v, d, delta, q, R):
        lx_v, ly_v = (1 - ell_v - b) / 2, (1 - ell_v + b) / 2
        h_v, a = (1 + 3 * ell_v + b) / 2, (1 + delta) / 2
        raw = a - sigma_v + h_v * (z0 - F(1, 6)) - a * ly_v - ell_v / 2 + q * ell_v
        raw += d * (R + delta / 2 - z0)
        K = F(2, 3) + ell_v + b / 6 - sigma_v
        reduced = K + (F(1, 2) + ell_v) * delta + q * ell_v - h_v * (1 - R)
        reduced += (d - h_v) * (R + delta / 2 - z0)
        assert raw == reduced
        assert sigma_v + lx_v / 2 - 1 + h_v / 6 == sigma_v - F(11, 16)
        return raw

    cases = 0
    deltas = sorted({F(i, 120) for i in range(101)} | {F(1, 50)})
    for delta in deltas:
        for j in range(41):
            x, q = F(j, 80), F(j, 80) * delta
            D, P = 3 - F(17, 9) * x, (2 - F(8, 9) * x) * (1 - x)
            J = (alpha - delta) * D + delta * P
            assert F(35, 54) <= J <= F(5, 2)
            R = 1 - delta + (alpha - delta) * delta * P / (2 * J)
            assert 1 - delta <= R <= 1 - F(2, 3) * delta
            E0 = exponent(ell0, sigma0, h0, delta, q, R)
            E1 = exponent(ell, sigma, h, delta, q, R)
            assert E1 - E0 == t * (-F(1, 4) + delta + q + F(3, 2) * R)
            assert -E0 >= F(49, 440640) and -E1 >= mad
            fixed_ref = exponent(ell, sigma0, h, delta, q, R)
            assert E1 - fixed_ref == t / 4
            assert fixed_ref - E0 == t * (-F(1, 2) + delta + q + F(3, 2) * R)
            assert 0 < R + delta / 2 - z0 < 2
            for d in (F(1, 2), (F(1, 2) + h) / 2, h, h + zeta):
                E = exponent(ell, sigma, d, delta, q, R)
                assert E <= -mad + 2 * zeta
                cases += 1
            # No-slot intermediate count includes floor using its enlarged R.
            Rmid = F(76, 75) - F(2, 3) * delta
            assert Rmid + delta / 2 - z0 > 0
            if delta >= F(1, 50):
                Emid = exponent(ell, sigma, F(1, 2), delta, q, Rmid)
                assert Emid <= -F(120907, 36000000)
            for gap in (F(1, 800000), F(1, 80000)):
                assert exponent(ell, sigma + gap, h, delta, q, R) == E1 - gap

    floor = exponent(ell, sigma, h, F(1, 50), F(1, 100), F(1))
    assert floor == -F(4327, 750000)
    small_base = h * F(13, 75) - ly / 2
    assert small_base == -F(197449, 2000000)
    assert small_base + F(63, 50) * F(1, 100) == -F(172249, 2000000)
    assert small_base + F(2, 100) == -F(157449, 2000000)
    B0 = lx / 2 + 1 + ly
    assert B0 == F(132497, 80000)
    real_requirement = (B0 + h + zeta - (sigma - F(11, 16)) + 3) / zeta
    zinf = real_requirement.numerator // real_requirement.denominator + 1
    eps = zeta / (100 * (1 + h + zeta))
    large = B0 + (h + zeta) * (1 + eps) - zeta * zinf + eps
    assert zinf > 2 and large < sigma - F(11, 16) - 1

    note_names = (
        "442-shared-contours-and-principal-signal-at-the-new-boundary.md",
        "443-effective-kappa-and-actual-detector-capacity.md",
        "444-joint-error-slots-and-uniform-central-high-saving.md",
        "445-conditional-strip-improvement-and-family-continuation.md",
    )
    result = {
        "scope": "Exact displayed algebra only; analytic hypotheses, infinite contours, physical identities and external Lean are not certified by this script.",
        "source_sha256_canonical_lf": digest(SOURCE),
        "note_sha256_canonical_lf": {n: digest(ROOT / "notes" / n) for n in note_names},
        "symbolic_certificate": symbolic_certificate(),
        "finite_frequency_cases": cases,
        "boundary": str(sigma),
        "adaptive_margin": str(mad),
        "extension": str(zeta),
        "extended_margin": str(mad - 2 * zeta),
        "floor_margin": str(-floor),
        "intermediate_margin": "120907/36000000",
        "small_margin": "172249/2000000",
        "example_fixed_absolute_line": zinf,
        "reference_gap_not_double_counted": True,
    }
    out = ROOT / "output" / "hybrid-high-continuation-exact-audit.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    audit()

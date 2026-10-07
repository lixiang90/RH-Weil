"""Exact cyclic algebra and polynomial profile integrals; no analytic certificate."""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/hybrid-background-exact-audit.json"
INPUTS = [
    "notes/454-original-background-and-weighted-prime-mixed-traces.md",
    "reviews/2026-10-07/hybrid-low-high-mixed-four-word-research.md",
]


def binding(path):
    data = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return {"path": path.relative_to(ROOT).as_posix(),
            "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data)}


def cyclic(word):
    return min(word[j:] + word[:j] for j in range(len(word)))


def mixed_partition(nh, nl):
    high = tuple(f"H{i}" for i in range(nh))
    low = tuple(f"L{i}" for i in range(nl))
    expected, rhs = Counter(), Counter()
    for word in product(high+low, repeat=4):
        hs, ls = [w for w in word if w in high], [w for w in word if w in low]
        if len(hs) == 2 and (hs[0] == hs[1] or ls[0] == ls[1]):
            expected[cyclic(word)] += 1
    for p, q, r in product(high, low, low):
        rhs[cyclic((p, p, q, r))] += 4
        rhs[cyclic((p, q, p, r))] += 2
    for p, q, r in product(low, high, high):
        rhs[cyclic((p, p, q, r))] += 4
        rhs[cyclic((p, q, p, r))] += 2
    for p, q in product(high, low):
        rhs[cyclic((p, p, q, q))] -= 4
        rhs[cyclic((p, q, p, q))] -= 2
    rhs = Counter({word: n for word, n in rhs.items() if n})
    assert expected == rhs
    return {"high_labels": nh, "low_labels": nl,
            "labelled_words": sum(expected.values()), "cyclic_classes": len(expected)}


def add(*polys):
    result = {}
    for poly in polys:
        for ij, a in poly.items():
            result[ij] = result.get(ij, Q(0)) + a
    return {ij: a for ij, a in result.items() if a}


def scale(poly, a):
    return {ij: a*b for ij, b in poly.items() if a*b}


def mul(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            key = (i+k, j+l)
            result[key] = result.get(key, Q(0)) + a*b
    return {ij: a for ij, a in result.items() if a}


def power(poly, n):
    result = {(0, 0): Q(1)}
    for _ in range(n):
        result = mul(result, poly)
    return result


def shifted(poly, sign):
    """A polynomial in v becomes the polynomial at v + sign*r."""
    assert all(j == 0 for _, j in poly)
    result = {}
    for (i, _), a in poly.items():
        for j in range(i+1):
            result[(i-j, j)] = a*comb(i, j)*sign**j
    return {ij: a for ij, a in result.items() if a}


def integrate_r(poly, sign):
    """Integrate r from 0 to 1/2 - sign*v, exactly."""
    upper = {(0, 0): Q(1, 2), (1, 0): Q(-sign)}
    terms = []
    for (i, j), a in poly.items():
        terms.append(mul({(i, 0): a/Q(j+1)}, power(upper, j+1)))
    return add(*terms)


def integrate_v(poly, lower=Q(-1, 2), upper=Q(1, 2)):
    assert all(j == 0 for _, j in poly)
    return sum((a*(upper**(i+1)-lower**(i+1))/Q(i+1)
                for (i, _), a in poly.items()), Q(0))


def profile_integrals(psi):
    a = integrate_v(psi)
    h = add(scale(psi, 1/a), {(0, 0): Q(-1)})
    r = {(0, 1): Q(1)}
    d_terms, j_terms = [], []
    for sign in (-1, 1):
        pair = mul(r, shifted(psi, sign))
        d_terms.append(integrate_r(pair, sign))
        diff = add(h, scale(shifted(h, sign), -1))
        j_terms.append(integrate_r(mul(pair, power(diff, 2)), sign))
    d = scale(mul(psi, add(*d_terms)), 1/a**2)
    v4 = integrate_v(power(h, 4))
    z = integrate_v(mul(power(h, 2), d))
    j = integrate_v(scale(mul(psi, add(*j_terms)), 1/a**2))
    assert v4 >= 0 and z >= 0 and 0 <= j <= 4*z
    return {"a": str(a), "V": str(v4), "Z": str(z), "J": str(j),
            "six_Z_minus_J_plus_V": str(6*z-j+v4)}


def certify():
    expansion = Counter(cyclic(word) for word in product("AC", repeat=4))
    expected = Counter({cyclic(tuple(w)): n for w, n in
                        [("AAAA", 1), ("AAAC", 4), ("AACC", 4),
                         ("ACAC", 2), ("ACCC", 4), ("CCCC", 1)]})
    assert expansion == expected
    commutator_norm = Counter()
    for left, a in [("CA", 1), ("AC", -1)]:
        for right, b in [("AC", 1), ("CA", -1)]:
            commutator_norm[cyclic(tuple(left+right))] += a*b
    assert commutator_norm == Counter({cyclic(tuple("AACC")): 2,
                                      cyclic(tuple("ACAC")): -2})
    profiles = {
        "flat": profile_integrals({(0, 0): Q(1)}),
        "one_minus_v_squared": profile_integrals({(0, 0): Q(1), (2, 0): Q(-1)}),
    }
    assert profiles["flat"] == {
        "a": "1", "V": "0", "Z": "0", "J": "0", "six_Z_minus_J_plus_V": "0"}
    dhi = {(1, 0): Q(1, 2), (2, 0): Q(1, 2)}
    dlo = {(0, 0): Q(1, 4), (1, 0): Q(-1, 2), (2, 0): Q(1, 2)}
    dhl = 2*integrate_v(mul(dhi, dlo), Q(0), Q(1, 2))
    assert dhl == Q(23, 960)
    # x=1/2+v is a high log-prime, y=r is low; true flat overlap is 1-x-y.
    x = {(0, 0): Q(1, 2), (1, 0): Q(1)}
    y = {(0, 1): Q(1)}
    overlap = {(0, 0): Q(1, 2), (1, 0): Q(-1), (0, 1): Q(-1)}
    jhl = integrate_v(integrate_r(mul(mul(x, y), overlap), 1), Q(0), Q(1, 2))
    assert jhl == Q(1, 640)
    repeated_mixed_constant = 4*dhl+8*jhl
    assert repeated_mixed_constant == Q(13, 120)
    mixed_models = [mixed_partition(nh, nl) for nh, nl in product(range(1, 4), repeat=2)]
    return {
        "status": "PASS: finite cyclic algebra and exact polynomial integrals only",
        "cyclic_fourth_coefficients": {"".join(w): n for w, n in sorted(expansion.items())},
        "commutator_norm_coefficients": {"".join(w): n for w, n in sorted(commutator_norm.items())},
        "profile_models": profiles,
        "flat_high_low_diagonal_integral": str(dhl),
        "flat_high_low_four_corner_integral": str(jhl),
        "flat_repeated_mixed_displayed_constant": str(repeated_mixed_constant),
        "repeated_mixed_union_models": mixed_models,
        "inputs_read_and_hashed_from_disk": [binding(ROOT / p) for p in INPUTS],
        "script_read_and_hashed_from_disk": binding(Path(__file__).resolve()),
        "not_certified": [
            "Gamma/pole uniform bounds, Hilbert estimates, finite projection leakage or alias asymptotics",
            "any complete prime fourth moment or mixed-prime correlation",
            "mixed-character power saving, a new zero-free boundary, zero proportion or RH",
            "external source proofs or proof kernels",
        ],
    }


if __name__ == "__main__":
    result = certify()
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "profiles": result["profile_models"],
                      "D_HL": result["flat_high_low_diagonal_integral"],
                      "output": str(OUT)}, ensure_ascii=False))

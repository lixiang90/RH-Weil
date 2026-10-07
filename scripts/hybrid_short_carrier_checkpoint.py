"""Finite audit for the original short-carrier compression and tail results.

The analytic estimates require the full source proofs and independent reviews.
This checks exact finite identities, exponent bookkeeping, and source bindings;
it does not prove prime asymptotics, a ratio upper, or a new zero theorem.
"""

from pathlib import Path
from itertools import product
import hashlib
import json
import re
import sys

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
P = "reviews/2026-10-08/"
CARRIER = P + "hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md"
RATIO = P + "hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md"
TAIL = P + "hybrid-second-order-tail-coupling-and-strip-geometry-research-compression.md"
NOTE = "notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md"
ROOT_REVIEW = P + "hybrid-short-carrier-ratio-and-tail-review-root.md"
CARRIER_REVIEW = P + "hybrid-anchored-carrier-averaged-fourth-projection-gap-review-twisted.md"
RATIO_REVIEW = P + "hybrid-whole-short-carrier-ratio-and-distinct-criterion-review-radial.md"
TAIL_REVIEW = P + "hybrid-second-order-tail-coupling-and-strip-geometry-review-twisted.md"
NOTE_REVIEW = P + "472-original-short-carrier-review-radial.md"
SELF = "scripts/hybrid_short_carrier_checkpoint.py"
OUTPUT = ROOT / "output/hybrid-short-carrier-checkpoint.json"
FILES = [CARRIER, RATIO, TAIL, NOTE, ROOT_REVIEW, CARRIER_REVIEW,
         RATIO_REVIEW, TAIL_REVIEW, NOTE_REVIEW, SELF]
PAIRS = {CARRIER: [ROOT_REVIEW, CARRIER_REVIEW],
         RATIO: [ROOT_REVIEW, RATIO_REVIEW],
         TAIL: [ROOT_REVIEW, TAIL_REVIEW], NOTE: [NOTE_REVIEW]}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT / name)
    return {"path": name, "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data), "lines": len(data.splitlines())}


def finite():
    checks = []

    def eq(label, left, right):
        assert s.simplify(left-right) == 0, label
        checks.append(label)

    def norm2(A):
        return s.simplify(s.trace(A.conjugate().T*A))

    X, ell, window = s.symbols("X ell window", positive=True)
    leak2, raw2, dim = ell+X/window, X/ell**2, X*ell
    eq("averaged fourth fee", raw2*leak2/dim, ell**-2+X/(window*ell**3))
    eq("short-window secondary fee", (X/(window*ell**3)).subs(window, 2*s.pi*X/s.sqrt(ell)),
       1/(2*s.pi*ell**s.Rational(5, 2)))
    eq("relative endpoint displacement", (window/(2*s.pi*X)).subs(window, 2*s.pi*X/s.sqrt(ell)),
       ell**-s.Rational(1, 2))

    # Arbitrary finite Hermitian operators, solely for checking block algebra.
    E = s.eye(4)[:, :2]
    P0, Q = E*E.T, s.eye(4)-E*E.T
    H = s.Matrix([[1, 2+s.I, 3, 1-s.I],
                  [2-s.I, -2, s.I, 4],
                  [3, -s.I, 2, 1+2*s.I],
                  [1+s.I, 4, 1-2*s.I, -1]])
    L = s.Matrix([[2, s.I, 1, 2],
                  [-s.I, 1, 2-s.I, -1],
                  [1, 2+s.I, -1, s.I],
                  [2, -1, -s.I, 3]])
    W = s.diag(s.Rational(1, 3), s.Rational(3, 4))
    A = E.T*H*E
    C, Z = Q*H*E, Q*H**2*E
    K = C.conjugate().T*C
    gap = s.trace(E.T*H**4*E)-s.trace(A**4)
    eq("fourth Jensen exact positive gap", gap,
       norm2(Z)+2*s.trace(A**2*K)+s.trace(K**2))
    assert gap >= 0
    assert gap <= 7*norm2(H)*norm2(C)  # Frobenius upper for the raw operator norm.
    checks.extend(["finite Jensen nonnegativity", "finite seven-times-raw fee"])
    qs, qa = norm2(E.T*H**2*E-W), norm2(A**2-W)
    eq("two-step square residual difference", qs-qa,
       2*s.trace(A**2*K)-2*s.trace(W*K)+s.trace(K**2))
    assert -2*s.Rational(3, 4)*norm2(C) <= qs-qa <= gap
    checks.append("same-W square sandwich")

    # Exact seven closed paths for each of the 16 ordered H/L placements.
    # Q endpoints must occur in pairs; no cyclic physical trace is used.
    for labels in product("HL", repeat=4):
        ops = [H if label == "H" else L for label in labels]
        comp, physical = s.eye(2), s.eye(4)
        for B in ops:
            comp *= E.T*B*E
            physical *= B
        difference = s.trace(E.T*physical*E)-s.trace(comp)
        paths = 0
        for bits in product([0, 1], repeat=3):
            if bits == (0, 0, 0):
                continue
            inside = [Q if bit else P0 for bit in bits]
            paths += s.trace(E.T*ops[0]*inside[0]*ops[1]*inside[1]*
                             ops[2]*inside[2]*ops[3]*E)
        eq("closed three-P paths "+''.join(labels), difference, paths)

    # An antiunitary reflection fixing E; verifies the half-ratio factor two.
    J = s.zeros(4)
    for i in range(4):
        J[i, 3-i] = 1
    Ec = s.Matrix([[1, s.I], [s.I, 1], [-s.I, 1], [1, -s.I]])/2
    assert Ec.conjugate().T*Ec == s.eye(2)
    assert J*Ec.conjugate() == Ec
    U1, U2 = s.eye(2), s.Matrix([[0, 2], [3, 0]])
    atoms = []
    for U in [U1, U2]:
        B = s.zeros(4)
        B[2:4, 0:2] = U
        atoms.append(B)
    Bplus = sum(atoms, s.zeros(4))
    assert Bplus**2 == s.zeros(4)
    assert J*Bplus.conjugate()*J == Bplus.conjugate().T
    G = Bplus.conjugate().T*Bplus
    D = sum((B.conjugate().T*B for B in atoms), s.zeros(4))
    R = G-D
    Bfull = Bplus+Bplus.conjugate().T
    eq("physical half-Gram factor two", s.trace(Ec.conjugate().T*Bfull**4*Ec), 2*norm2(G*Ec))
    Rfull = R+J*R.conjugate()*J
    eq("full/half ratio factor two", norm2(Rfull*Ec), 2*norm2(R*Ec))
    eq("diagonal-ratio expansion", norm2(G*Ec),
       norm2(D*Ec)+norm2(R*Ec)+2*s.re(s.trace(Ec.conjugate().T*D*R*Ec)))

    # Scalar slot theorem and exact dual optimizers, across both tails.
    j = lambda t: (t-1)**2-max(t-2, 0)**2
    kap = lambda t: max(-t, 0)**2+4*max(-t, 0)+max(t-2, 0)**2
    F = lambda t: 4*t-t*t
    samples = [s.Rational(i, 4) for i in range(-20, 25)]
    for p in [s.Rational(i, 4) for i in range(25)]:
        phi = 2*p+1-j(p)
        for t in samples:
            if t <= p:
                assert F(t)+kap(t) <= phi
    checks.append("scalar rank-trace slot across both tails")
    for t in samples:
        b, c, d = max(t-2, 0), max(-t, 0), 1 if t < 0 else 0
        assert kap(t) == 2*b*(t-2)-b*b-2*c*t-c*c-4*d*t
    checks.append("second-order tail dual optimizers")
    x, z = s.symbols("x z", real=True)
    eq("low effect positive form", x*x+(z*z+2*x*z)/6,
       s.Rational(5, 6)*x*x+(z+x)**2/6)
    eq("low effect negative form", -x*x-z*z/6+x*z/3,
       -s.Rational(5, 6)*x*x-(z-x)**2/6)
    qstar, Sh = (s.sqrt(104899)-275)/15120, s.Rational(19, 480)
    assert 0 < qstar < Sh
    eq("whole distinct offset", s.Rational(19, 240)-Sh, Sh)
    return {"checks": checks, "count": len(checks),
            "scope": "exact finite algebra and exponent bookkeeping; no analytic prime upper",
            "residual_liminf_floor": str(qstar),
            "new_arithmetic_ratio_upper": False}


def build():
    records = {name: binding(name) for name in FILES}
    reviews, citations, links = [], [], 0
    for source, reviewers in PAIRS.items():
        digest = records[source]["sha256_canonical_lf"]
        for review in reviewers:
            assert digest in canonical(ROOT/review).decode("utf-8"), (source, review)
            reviews.append({"source": source, "source_sha256": digest, "review": review,
                            "review_sha256": records[review]["sha256_canonical_lf"]})
    for name in FILES:
        if not name.endswith(".md"):
            continue
        content = canonical(ROOT/name).decode("utf-8")
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            if not re.search(r"\.(md|py|json|tex|pdf|lean)(#.*)?$", target):
                continue
            path = (ROOT/name).parent.joinpath(target.split("#", 1)[0]).resolve()
            # The checkpoint links to this output before the first generation.
            # Its own existence is verified by the write/read in __main__.
            if path != OUTPUT.resolve():
                assert path.exists(), (name, target)
            links += 1
        for target, digest in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)\s*\|\s*([a-f0-9]{64})", content):
            path = (ROOT/name).parent.joinpath(target).resolve()
            data = path.read_bytes() if path.suffix == ".pdf" else canonical(path)
            assert hashlib.sha256(data).hexdigest() == digest, (name, target)
            citations.append({"document": name, "source": path.relative_to(ROOT).as_posix(),
                              "sha256": digest})
    return {"date": "2026-10-08", "base_commit": "2d5621dbc999e0cf313ea224b825d6d56547c45c",
            "original_field_and_scalar_carrier_retained": True,
            "new_whole_fourth_short_carrier_projection_payment": True,
            "all_16_ordered_HL_words_share_one_good_set": True,
            "projection_payment_requires_zero_free_R": False,
            "projection_payment_requires_high_fourth_bounded": False,
            "fixed_original_start_pointwise_gap_proved": False,
            "new_bidirectional_actual_ratio_L1_equivalence": True,
            "new_actual_second_order_tail_certificate": True,
            "new_high_residual_upper": False, "new_positive_tail_density_floor": False,
            "new_actual_zero_proportion": False, "new_zero_free_boundary": False,
            "new_paper": False, "finite_certificate": finite(),
            "review_bindings": reviews, "cited_source_hash_bindings": citations,
            "links_checked": links, "files": list(records.values()),
            "unproved": ["a useful complete ratio-variance upper in the same short window",
                         "an actual positive normalized second-order tail lower",
                         "a new zero proportion or zero-free boundary",
                         "independent certification of the imported R analytic kernel"]}


if __name__ == "__main__":
    result = json.loads(json.dumps(build(), default=str))
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("PASS: short-carrier exponents, closed P paths, ratio factor two, tail dual and source bindings")

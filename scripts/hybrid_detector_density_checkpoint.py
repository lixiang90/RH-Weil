"""Exact checkpoint for original-family raw zero-density and final envelopes.

The source proofs and independent reviews carry the analytic arguments.
This checks continuous affine certificates and exact polynomial identities;
it does not certify the imported sextic sieve, AFE, or a new zero theorem.
"""

from pathlib import Path
from fractions import Fraction as Q
from math import comb
import contextlib
import hashlib
import importlib.util
import io
import json
import re
import sys

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
P = "reviews/2026-10-08/"
DENSITY = P+"hybrid-original-sextic-primitive-zero-density-research-compression.md"
DOMINANCE = P+"hybrid-original-density-envelope-dominance-research-root.md"
HIGH = P+"hybrid-high-bin-strict-certificate-research-twisted.md"
NOTE = "notes/473-original-sextic-zero-density-and-final-envelope-comparison.md"
DENSITY_REVIEWS = [P+"hybrid-original-sextic-primitive-zero-density-review-root.md",
                   P+"hybrid-original-sextic-primitive-zero-density-review-twisted.md"]
DOMINANCE_REVIEW = P+"hybrid-original-density-envelope-dominance-review-twisted.md"
HIGH_REVIEW = P+"hybrid-high-bin-strict-certificate-review-root.md"
NOTE_REVIEW = P+"473-original-density-and-envelope-review-radial.md"
SELF = "scripts/hybrid_detector_density_checkpoint.py"
OUTPUT = ROOT/"output/hybrid-detector-density-checkpoint.json"
FILES = [DENSITY, DOMINANCE, HIGH, NOTE, *DENSITY_REVIEWS,
         DOMINANCE_REVIEW, HIGH_REVIEW, NOTE_REVIEW, SELF]
PAIRS = {DENSITY: DENSITY_REVIEWS, DOMINANCE: [DOMINANCE_REVIEW],
         HIGH: [HIGH_REVIEW], NOTE: [NOTE_REVIEW]}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT/name)
    return {"path": name, "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data), "lines": len(data.splitlines())}


def finite():
    checks = []

    def eq(label, left, right):
        assert s.factor(left-right) == 0, label
        checks.append(label)

    x, sigma, delta, c = s.symbols("x sigma delta c", real=True)
    M, Rw, d = s.symbols("M Rw d", positive=True)

    def affine_nonnegative(label, expr, lo, hi):
        numerator, denominator = s.fraction(s.cancel(expr))
        assert x not in denominator.free_symbols, label
        assert s.Poly(numerator, x).degree() <= 1, label
        assert expr.subs(x, lo) >= 0 and expr.subs(x, hi) >= 0, label
        checks.append(label+" (affine whole interval)")

    eq("actual conductor AFE third term", s.expand_power_base(
        (M*s.sqrt(M*Rw))**s.Rational(2, 3), force=True), M*Rw**s.Rational(1, 3))
    p = 1+d*(1-sigma)/(3-2*sigma)
    eq("Type I full height", d/4-(sigma-s.Rational(1, 2))*d/(6-4*sigma), p-1)
    eq("plain Y full height", (2-2*sigma)*d/(6-4*sigma), p-1)
    eq("7/8 original degree two height", p.subs({sigma:s.Rational(7, 8), d:2}), s.Rational(6, 5))

    r, cross = s.Rational(7, 6)-sigma, s.Rational(5, 3)-2*sigma
    y = (1+3*x)/(12*r)
    ell = (1+5*x)/6
    E = 2*x/3+cross*y
    g = 8*(1-sigma)/(7-6*sigma)
    eq("low sigma Type I balance", (ell+x)/2-(sigma-s.Rational(1, 2))*y, E)
    eq("low sigma X-first domination identity", g-(s.Rational(3, 2)-sigma),
       -6*(sigma-s.Rational(1, 2))*(sigma-s.Rational(5, 6))/(7-6*sigma))
    eq("low sigma E versus g*x", E-g*x, cross*(1-x)/(12*r))
    eq("low sigma whole layer at x=1", ((1-x)/2+E).subs(x, 1), g)
    # These two polynomials are affine in each variable separately; the four
    # corners certify their sign on the entire rectangle, not by sampling.
    rr = s.symbols("r", real=True)
    for label, polynomial in [("h <= y", 1+3*x-6*rr*x),
                               ("y <= 2x", 24*rr*x-1-3*x)]:
        assert s.degree(polynomial, x) <= 1 and s.degree(polynomial, rr) <= 1
        for xx in [s.Rational(1, 5), s.Integer(1)]:
            for rv in [s.Rational(1, 3), s.Rational(2, 3)]:
                assert polynomial.subs({x:xx, rr:rv}) >= 0
        checks.append("low sigma "+label+" (bilinear rectangle)")
    assert s.Rational(3, 5) < s.Rational(2, 3)
    checks.append("small powerful-layer cardinality")

    # The third displayed branch has two different h formulas.
    branches = [
        ("high", Q(1, 7), Q(1), (1+5*x)/6, (22*x-2)/13,
         2*(1+41*x)/39, 2*(x+(22*x-2)/13)/3, (1+41*x)/78, False),
        ("middle", Q(2, 15), Q(1, 7), (1+x)/4, (29*x-3)/13,
         (1+25*x)/13, 2*(x+(29*x-3)/13)/3, (1+25*x)/52, False),
        ("small cardinality", Q(0), Q(1, 15), (1+x)/4, s.Integer(0),
         x+s.Rational(1, 5), x, (1+5*x)/20, True),
        ("small optimized", Q(1, 15), Q(2, 15), (1+x)/4, x-s.Rational(1, 15),
         x+s.Rational(1, 5), x, (1+5*x)/20, False),
    ]
    for label, lo, hi, el, h, yy, K, ee, cardinality in branches:
        for suffix, expr in [("h nonnegative", h), ("h <= y", yy-h),
                             ("sieve >= x", K-x), ("sieve >= h", K-h),
                             ("sieve >= cross", K-2*(x+h)/3),
                             ("Type I <= E", ee-(el+K)/2+3*yy/8),
                             ("X first <= E", ee-x+3*h/4),
                             ("X cross <= E", ee-2*x/3+h/12),
                             ("Y cross <= X cross", (yy-h)/12)]:
            affine_nonnegative("7/8 "+label+" "+suffix, expr, lo, hi)
        eq("7/8 "+label+" plain balance", ee, yy/4)
        total = (1+x)/2 if cardinality else (1-x)/2+ee
        affine_nonnegative("7/8 "+label+" total <= 7/13",
                           s.Rational(7, 13)-total, lo, hi)
    eq("raw count saving", s.Rational(5, 8)-s.Rational(7, 13), s.Rational(9, 104))
    eq("maximum fixed y and sigma slope", 2*branches[0][5].subs(x, 1), s.Rational(56, 13))

    D, P0 = 3-(1+2*c)*x, (2-2*c*x)*(1-x)
    eq("whole rectangle P/D bound numerator", 2*D-3*P0, 2*x*(2+c-3*c*x))
    assert 2+s.Rational(1, 3)-3*s.Rational(50, 111)/2 > 0
    checks.append("P/D sign on entire c,x rectangle")
    alpha = s.Rational(5, 6)
    r0 = (15-16*delta)/(15-6*delta)
    eq("final monotone envelope upper", 1-delta+(alpha-delta)*delta/(3*alpha-delta), r0)
    glow = 4*(1-delta)/(4-3*delta)
    ghigh = (5*delta-2)*(1-delta)/(6*delta-3*delta**2-2)
    gsafe = 28*(1-delta)/13
    eq("actual low raw minus final upper", glow-r0,
       delta*(25-24*delta)/((4-3*delta)*(15-6*delta)))
    eq("hypothetical exact high minus final upper", ghigh-r0,
       -delta*(18*delta**2-24*delta+5)/
       (3*(2*delta-5)*(3*delta**2-6*delta+2)))
    eq("actual safe high minus final upper", gsafe-r0,
       (225-380*delta+168*delta**2)/(13*(15-6*delta)))
    eq("literature piecewise join", glow.subs(delta, s.Rational(2, 3)),
       ghigh.subs(delta, s.Rational(2, 3)))
    eq("actual safe high endpoint", gsafe.subs(delta, s.Rational(3, 4)), s.Rational(7, 13))
    eq("high safe numerator minimum endpoint",
       (225-380*delta+168*delta**2).subs(delta, s.Rational(3, 4)), s.Rational(69, 2))
    assert 336*s.Rational(3, 4)-380 < 0
    assert 36*s.Rational(2, 3)-24 >= 0
    assert (18*delta**2-24*delta+5).subs(delta, s.Rational(3, 4)) == -s.Rational(23, 8)
    checks.extend(["actual safe high numerator decreasing throughout interval",
                   "exact high quadratic increasing and strictly negative throughout interval"])
    assert s.Rational(1, 50)*9/60 == s.Rational(3, 1000)
    assert (s.Rational(2, 3)*s.Rational(23, 8))/(11*s.Rational(13, 16)) == s.Rational(92, 429)
    assert s.Rational(69, 2)/(13*11) == s.Rational(69, 286)
    checks.append("three rational full-interval strict margins")

    # This frozen module prints a report but writes no files.
    path = ROOT/"scripts/hybrid_kappa_feedback_exact_audit.py"
    assert hashlib.sha256(canonical(path)).hexdigest() == (
        "e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68")
    spec = importlib.util.spec_from_file_location("frozen_cubic_density", path)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    lo, hi = Q(30, 43), Q(3, 4)
    lower = [[45, 86, 161, 286], [52, 99, 181, 317], [61, 113, 203, 352]]
    for i in range(3):
        for j in range(4):
            z = module.Cubic(0)
            for k in range(i+1):
                for q in range(j+1):
                    A = module.A[q] if q < len(module.A) else module.Cubic(0)
                    B = module.B[q] if q < len(module.B) else module.Cubic(0)
                    C = module.C[q] if q < len(module.C) else module.Cubic(0)
                    power = [A*lo*lo-B*lo+C, (2*A*lo-B)*(hi-lo), A*(hi-lo)**2][k]/2**q
                    z += power*Q(comb(i, k), comb(2, k))*Q(comb(j, q), comb(3, q))
            assert z.interval()[0] > Q(lower[i][j], 1000) > Q(1, 25)
            checks.append(f"high bin Bernstein coefficient ({i},{j}) > 1/25")
    return {"checks": checks, "count": len(checks),
            "scope": "exact continuous affine and polynomial algebra, not analytic family certification",
            "raw_exponent_at_7_over_8": "7/13", "raw_saving": "9/104",
            "height_exponent_at_7_over_8": "6/5",
            "high_bin_strict_endpoint_margin": "1/125",
            "direct_density_min_improves_final_envelope": False}


def build():
    records = {name: binding(name) for name in FILES}
    reviews, citations, links = [], [], 0
    for source, reviewers in PAIRS.items():
        digest = records[source]["sha256_canonical_lf"]
        for review in reviewers:
            assert digest in canonical(ROOT/review).decode("utf-8"), (source, review)
            reviews.append({"source": source, "source_sha256": digest, "review": review,
                            "review_sha256": records[review]["sha256_canonical_lf"]})
    link_pattern = r"\[[^\]\n]*\]\(([^)\n]+)\)"
    hash_pattern = link_pattern+r"\s*\|\s*"+chr(96)+r"?([a-f0-9]{64})"+chr(96)+"?"
    for name in FILES:
        if not name.endswith(".md"):
            continue
        content = canonical(ROOT/name).decode("utf-8")
        for target in re.findall(link_pattern, content):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            if not re.search(r"\.(md|py|json|tex|pdf|lean)(#.*)?$", target):
                continue
            path = (ROOT/name).parent.joinpath(target.split("#", 1)[0]).resolve()
            if path != OUTPUT.resolve():
                assert path.exists(), (name, target)
            links += 1
        for target, digest in re.findall(hash_pattern, content):
            path = (ROOT/name).parent.joinpath(target).resolve()
            data = path.read_bytes() if path.suffix == ".pdf" else canonical(path)
            assert hashlib.sha256(data).hexdigest() == digest, (name, target)
            source_name = path.relative_to(ROOT).as_posix()
            citations.append({"document": name, "source": source_name, "sha256": digest})
    return {"date": "2026-10-08", "base_commit": "2681813154243e10cf4602f4e88514355060d379",
            "original_field_sixthfree_rows_and_zero_masks_retained": True,
            "new_frozen_powerful_uniform_AFE_derivation": True,
            "new_raw_primitive_zero_row_density": True,
            "density_relative_to_original_sieve_and_standard_AFE": True,
            "new_full_domain_final_envelope_dominance_proof": True,
            "new_high_bin_continuous_strict_margin": True,
            "floor_uses_actual_zero_witness": False,
            "new_density_prime_slot_joint_amplification": False,
            "new_scalar_ratio_upper": False,
            "new_actual_zero_proportion": False, "new_zero_free_boundary": False,
            "new_paper": False, "finite_certificate": finite(),
            "review_bindings": reviews, "cited_source_hash_bindings": citations,
            "links_checked": links, "files": list(records.values()),
            "unproved": ["a new actual joint density and common prime-slot amplification count",
                         "a useful original positive-height scalar fourth or ratio upper",
                         "a new actual proportion or zero-free boundary",
                         "independent certification of the imported R analytic kernel"]}


if __name__ == "__main__":
    result = json.loads(json.dumps(build(), default=str))
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("PASS: original raw-density exponents, full-domain dominance, twelve strict Bernstein coefficients and source bindings")

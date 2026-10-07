"""Finite algebra and source bindings for original fourth-power and far work.

This does not certify Perron, Hilbert, zero-density, prime arithmetic or AF.
Outcome flags report the reviewed sources' conclusions, not script proofs.
--finite-only and --check are read-only; --generate writes only the new JSON.
"""

import sys
sys.dont_write_bytecode = True
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
P = "reviews/2026-10-08/"
POWER = P+"hybrid-positive-height-zero-packet-fourth-upper-research-radial.md"
FAR = P+"hybrid-whole-ratio-smooth-carrier-far-resonance-research-twisted.md"
FIXED = P+"hybrid-fixed-start-half-gram-sampling-research-root.md"
SMOOTH = P+"hybrid-canonical-semiprime-smooth-subtraction-and-variance-obstruction-research-compression.md"
ROOT_REVIEW = P+"hybrid-original-fourth-power-and-far-review-root.md"
POWER_REVIEW = P+"hybrid-positive-height-zero-packet-fourth-upper-review-twisted.md"
FAR_REVIEW = P+"hybrid-whole-ratio-smooth-carrier-far-resonance-review-radial.md"
FIXED_REVIEW = P+"hybrid-fixed-start-half-gram-sampling-review-compression.md"
FIXED_SECOND_REVIEW = P+"hybrid-fixed-start-half-gram-sampling-review-twisted.md"
NOTE = "notes/475-original-fourth-power-saving-and-whole-far-resonance.md"
NOTE_REVIEW = P+"475-summary-review-radial.md"
SELF = "scripts/hybrid_original_fourth_power_and_far_checkpoint.py"
OUTPUT = ROOT/"output/hybrid-original-fourth-power-and-far-checkpoint.json"
FILES = [POWER, FAR, FIXED, SMOOTH, NOTE, ROOT_REVIEW, POWER_REVIEW, FAR_REVIEW,
         FIXED_REVIEW, FIXED_SECOND_REVIEW, NOTE_REVIEW, SELF]
PAIRS = {POWER: [ROOT_REVIEW, POWER_REVIEW], FAR: [ROOT_REVIEW, FAR_REVIEW],
         FIXED: [FIXED_REVIEW, FIXED_SECOND_REVIEW], SMOOTH: [ROOT_REVIEW],
         NOTE: [NOTE_REVIEW]}
# All mathematical sources and independent reviews are frozen. The script
# itself is dynamically bound, avoiding a self-hash cycle.
FROZEN = {
    POWER: "8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481",
    FAR: "9b8c6064731f65eb4449a3e9da353077baa856a4cb27f93fd5063b6f6a578054",
    FIXED: "7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc",
    SMOOTH: "7fcb097ad17d77b7281acd1f7c7d0f1580c5519c015437e104823cdfabd52645",
    NOTE: "cd295de4a909d82e50f8db4635d18cb3dfb9dffbbab8a5a4f00167aced1bf55b",
    ROOT_REVIEW: "65a4e75ac9ca79dc2c9a2752902ec89acb968eae8c696ad4d54ab1148ec26f6c",
    POWER_REVIEW: "4ca9bb7d261c6e8f5312922c9558a8e7063f72ea733658579c0c4573fc39f547",
    FAR_REVIEW: "bab74da7a1416aeea7083f47d5e398e7164f8d6f511e821919b61d1c040aae0b",
    FIXED_REVIEW: "9f5b4b76bab1483cf0eee8607928f5b85b41feb3e14aa652c838416f37b68cf8",
    FIXED_SECOND_REVIEW: "7997dbb5427f30bba5cae865a89fb3a23bc787d8a5788431283c847dbb4b2943",
    NOTE_REVIEW: "c4c8ca3ba740d16a535c8138c13706f2f6f5ee93b4aae4ad228892d574a3782e",
}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT/name)
    digest = hashlib.sha256(data).hexdigest()
    if name in FROZEN:
        assert digest == FROZEN[name], ("frozen binding differs", name)
    return {"path": name, "sha256_canonical_lf": digest,
            "canonical_utf8_bytes": len(data), "lines": len(data.splitlines())}


def finite():
    checks = []

    def eq(label, left, right):
        if isinstance(left, tuple) or isinstance(right, tuple):
            assert left == right, label
        else:
            assert s.simplify(left-right) == 0, label
        checks.append(label)

    def nonnegative_polynomial(label, expression, variables):
        poly = s.Poly(s.expand(expression), *variables)
        assert all(c >= 0 for c in poly.coeffs()), label
        checks.append(label+" (all coefficients nonnegative)")

    sigma, theta = s.symbols("sigma theta", real=True)
    u, v = s.symbols("u v", nonnegative=True)
    f1 = 4*sigma-3+3*(1-sigma)/(2-sigma)
    f2 = 4*sigma-3+3*(1-sigma)/(3*sigma-1)
    B = f2.subs(sigma, theta)
    eq("low-density derivative", s.diff(f1, sigma), 4-3/(2-sigma)**2)
    eq("high-density derivative", s.diff(f2, sigma), 4-6/(3*sigma-1)**2)
    eq("low derivative numerator at sigma=3/4-u",
       (4*(2-sigma)**2-3).subs(sigma, s.Rational(3, 4)-u),
       s.Rational(13, 4)+10*u+4*u**2)
    nonnegative_polynomial("low derivative numerator positive for u>=0",
                           s.Rational(13, 4)+10*u+4*u**2, [u])
    eq("high derivative numerator at sigma=3/4+v",
       (4*(3*sigma-1)**2-6).subs(sigma, s.Rational(3, 4)+v),
       s.Rational(1, 4)+30*v+36*v**2)
    nonnegative_polynomial("high derivative numerator positive for v>=0",
                           s.Rational(1, 4)+30*v+36*v**2, [v])
    # Denominators are respectively (5/4+u)^2 and (5/4+3v)^2.
    eq("low derivative denominator", (2-sigma).subs(sigma, s.Rational(3, 4)-u),
       s.Rational(5, 4)+u)
    eq("high derivative denominator", (3*sigma-1).subs(sigma, s.Rational(3, 4)+v),
       s.Rational(5, 4)+3*v)
    eq("first continuous endpoint", f1.subs(sigma, s.Rational(1, 2)), 0)
    eq("density functions meet at 3/4", f1.subs(sigma, s.Rational(3, 4)),
       f2.subs(sigma, s.Rational(3, 4)))
    eq("common endpoint is 3/5", f2.subs(sigma, s.Rational(3, 4)), s.Rational(3, 5))
    eq("B(5/6)", B.subs(theta, s.Rational(5, 6)), s.Rational(2, 3))
    eq("B(7/8)", B.subs(theta, s.Rational(7, 8)), s.Rational(19, 26))
    eq("old 7/8 exponent", 2*s.Rational(7, 8)-1, s.Rational(3, 4))
    gap = (2*theta-1)-B
    eq("exact strip-dependent saving", gap,
       (1-theta)*(6*theta-5)/(3*theta-1))
    eq("7/8 power saving", gap.subs(theta, s.Rational(7, 8)), s.Rational(1, 52))
    eq("saving vanishes at 5/6", gap.subs(theta, s.Rational(5, 6)), 0)
    # For 5/6<theta<=7/8, all three displayed gap factors are positive.
    eq("one-minus-theta positive lower on theta<=7/8",
       (1-theta).subs(theta, s.Rational(7, 8)-u), s.Rational(1, 8)+u)
    eq("gap denominator positive lower on theta>5/6",
       (3*theta-1).subs(theta, s.Rational(5, 6)+u), s.Rational(3, 2)+3*u)
    nonnegative_polynomial("one-minus-theta whole interval positivity",
                           s.Rational(1, 8)+u, [u])
    nonnegative_polynomial("gap denominator whole interval positivity",
                           s.Rational(3, 2)+3*u, [u])
    eq("gap numerator open-domain factor", (6*theta-5).subs(theta, s.Rational(5, 6)+u), 6*u)
    assert s.Rational(19, 26) < 1
    checks.append("monotone B upper endpoint strictly below one")
    eq("zero-packet log power 6+1-4", s.Integer(6)+1-4, 3)
    exponent = 4*(sigma-s.Rational(1, 2))-1
    eq("fourth-density exponent including normalized height", exponent, 4*sigma-3)

    n, N = s.symbols("n N", integer=True, positive=True)
    a_n = 1/(4*n*(n+1))
    eq("finite chi width telescopes", s.summation(a_n, (n, 1, N)),
       s.Rational(1, 4)*(1-1/(N+1)))
    eq("first chi factor length", a_n.subs(n, 1), s.Rational(1, 8))
    eq("first chi factor sup", 1/a_n.subs(n, 1), 8)
    width = s.Rational(1, 4)*(1-1/(N+1))
    eq("finite left support endpoint", s.Rational(1, 2)-width/2,
       s.Rational(3, 8)+1/(8*(N+1)))
    eq("finite right support endpoint", s.Rational(1, 2)+width/2,
       s.Rational(5, 8)-1/(8*(N+1)))
    eq("limiting support left", s.limit(s.Rational(1, 2)-width/2, N, s.oo), s.Rational(3, 8))
    eq("limiting support right", s.limit(s.Rational(1, 2)+width/2, N, s.oo), s.Rational(5, 8))
    eq("chi sinc argument", a_n/2, 1/(8*n*(n+1)))
    # Floor certificate: z>=256 gives r=sqrt(z)/8>=2; N=floor(r)
    # means r=N+u, 0<=u<1, N>=2. No finite sampled floors replace this.
    j, w = s.symbols("j w", nonnegative=True)
    nonnegative_polynomial("8*N*(N+1)<=16*N^2 for N>=2",
                           (16*N**2-8*N*(N+1)).subs(N, 2+j), [j])
    eq("floor upper-square slack for r=N+u",
       16*(N+u)**2-16*N**2, 16*u*(2*N+u))
    nonnegative_polynomial("floor upper-square whole interval",
                           (16*u*(2*N+u)).subs(N, 2+j), [j, u])
    eq("floor lower-root slack with u=1-w",
       (N-(N+u)/2).subs({N: 2+j, u: 1-w}), (1+j+w)/2)
    nonnegative_polynomial("N>=sqrt(z)/16 on true floor interval",
                           (1+j+w)/2, [j, w])
    eq("z/4 at z=64r^2", (64*(N+u)**2)/4, 16*(N+u)**2)
    assert s.log(4) > 1
    checks.append("log4>1 exact symbolic comparison")

    L, T, X = s.symbols("L T X", positive=True)
    span = T/s.sqrt(L)
    Delta = 1024*L**s.Rational(5, 2)/X
    eq("smooth far s*Delta with T=2piX", (span*Delta).subs(T, 2*s.pi*X),
       2048*s.pi*L**2)
    assert s.pi > 2
    checks.append("s*Delta>=4096L^2 from pi>2")
    eq("root-decay at 4096L^2", s.sqrt(4096*L**2)/16, 4*L)
    eq("far decay e^-4L=X^-4 with X=e^L", s.exp(-4*L), s.exp(L)**-4)
    # Exponents are (X power,L power), with fixed 2pi constants omitted.
    def scale(pair, factor):
        return tuple(Q(factor)*a for a in pair)
    def add(*pairs):
        return tuple(sum(entries) for entries in zip(*pairs))
    m, height, log = (Q(1, 2), Q(-1)), (Q(1), Q(0)), (Q(0), Q(1))
    eq("full far m^4 X^-4 power", add(scale(m, 4), (Q(-4), Q(0))), (Q(-2), Q(-4)))
    eq("natural near chirp scale for S=c/X", add(height, scale(log, Q(-1, 2)), (Q(-1), Q(0))),
       (Q(0), Q(-1, 2)))
    eq("box carrier far log power", -4+s.Rational(1, 2), s.Rational(-7, 2))
    eq("box Delta=L^-1 log power", s.Rational(-7, 2)+2, s.Rational(-3, 2))
    eq("near determinant 2 Delta X^2 power",
       add((Q(-1), Q(5, 2)), (Q(2), Q(0))), (Q(1), Q(5, 2)))
    eq("near determinant exact leading constant", s.Integer(2)*1024, 2048)

    # Actual half-band is [-u,L/2-u], not a global torus prime band.
    uu = s.symbols("uu", real=True)
    band_left, band_right, center = -uu, L/2-uu, L/4-uu
    eq("actual fixed-start band width", band_right-band_left, L/2)
    eq("actual fixed-start band center", (band_left+band_right)/2, center)
    eq("bump support enclosing width", (center+3*L/8)-(center-3*L/8), 3*L/4)
    eq("support width below eta period", L-3*L/4, L/4)
    eta = 2*s.pi/L
    eq("sampling Fourier-series normalization", L**2/(4*s.pi**2)/L*2*s.pi, 1/eta)
    eq("N=3 exterior amplitude exponent",
       add(scale(m, 2), scale(add(log, height), -2)), (Q(-1), Q(-4)))
    eq("N=3 raw sampling cross exponent",
       add(scale(m, 4), scale(add(log, height), -2)), (Q(0), Q(-6)))
    eq("first guard m/T exponent", add(m, scale(height, -1)), (Q(-1, 2), Q(-1)))
    eq("second guard m^2/T exponent", add(scale(m, 2), scale(height, -1)), (Q(0), Q(-2)))
    # The floor is retained: d=floor(XL), so XL=d+f, 0<=f<1.
    d, f = s.symbols("d f", positive=True)
    eq("exact sampling floor prefactor", (d+f)/d, 1+f/d)
    bpow = s.symbols("bpow", nonnegative=True)
    for label, ep in [("main", bpow), ("first cross", 3*bpow/4-s.Rational(1, 2)),
                      ("second cross", bpow/2), ("first guard square", bpow/2-1),
                      ("guard cross", bpow/4-s.Rational(1, 2)), ("second guard square", 0)]:
        nonnegative_polynomial("growth budget absorbs "+label, bpow-ep, [bpow])

    # Exact continuous triangular density and its Mellin transform. This
    # checks neither a PNT remainder nor an integer-density replacement.
    z = s.symbols("z", nonzero=True)
    y = s.symbols("y", real=True)
    F_lower = s.exp(z*y)*((y-L)/z-1/z**2)
    F_upper = s.exp(z*y)*((2*L-y)/z+1/z**2)
    eq("lower density Mellin antiderivative", s.diff(F_lower, y), (y-L)*s.exp(z*y))
    eq("upper density Mellin antiderivative", s.diff(F_upper, y), (2*L-y)*s.exp(z*y))
    Mellin = (F_lower.subs(y, 3*L/2)-F_lower.subs(y, L)
              +F_upper.subs(y, 2*L)-F_upper.subs(y, 3*L/2))
    eq("rho Mellin equals exact factor main squared", Mellin,
       ((s.exp(z*L)-s.exp(z*L/2))/z)**2)
    eq("rho mass at z=0", s.limit(Mellin, z, 0), L**2/4)
    eq("lower rho overlap length", (L/2+u)-L/2, u)
    eq("upper rho overlap length", L-(L/2+u), L/2-u)
    t0, guard = 17*T/8, 15*T/8
    eq("positive guard lower endpoint", t0-guard, T/4)
    eq("positive guard upper endpoint", t0+guard, 4*T)
    eq("triangle kernel sinc guard radius", guard/(2*T), s.Rational(15, 16))
    assert s.Rational(15, 16) < s.pi
    checks.append("triangle kernel guard lies before first sinc zero")
    eq("smooth-main raw cross X*X^-1", add((Q(1), Q(0)), (Q(-1), Q(0))), (Q(0), Q(0)))
    eq("smooth-main normalized additive log power", -4, -4)
    eq("top centered variance target X^3 L^4", 4-1, 3)
    eq("raw positive large-factor Cauchy X^4 versus target X^3 gap", 4-3, 1)
    eq("7/8 outer smooth error power", 2+2*s.Rational(7, 8), s.Rational(15, 4))
    return {"checks": checks, "count": len(checks),
            "scope": "finite exact exponent, cutoff, Mellin and sampling normalization algebra only",
            "B_7_over_8": str(Q(19, 26)), "old_power_saving": str(Q(1, 52)),
            "Perron_or_Hilbert_or_zero_density_certified": False,
            "analytic_prime_fourth_or_AF_proof_certified": False}


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
            citations.append({"document": name, "source": path.relative_to(ROOT).as_posix(),
                              "sha256": digest})
    return {"date": "2026-10-08", "base_commit": "46106dc449ac7e6d91a3646b09e63b0b0e272cc1",
            "original_prime_cutoffs_carrier_and_same_prime_center_retained": True,
            "actual_power_improved_relative_R": True, "whole_far_paid": True,
            "power_result_conditional_input": "all nontrivial zeta zeros beta<=theta, fixed 5/6<theta<=7/8",
            "fixed_start_zero_matrix_transfer_relative_AF_unscaled_S1_tail": True,
            "outcome_flags_are_reviewed_source_conclusions_not_script_analytic_proofs": True,
            "analytic_upper_certified_by_script": False,
            "constant_fourth_budget_paid": False, "new_actual_zero_proportion": False,
            "new_zero_free_boundary": False, "new_paper": False,
            "finite_certificate": finite(), "review_bindings": reviews,
            "cited_source_hash_bindings": citations, "links_checked": links,
            "files": list(records.values()),
            "unproved": ["constant-size canonical scalar fourth budget",
                         "the remaining whole signed natural-near arithmetic",
                         "a new actual zero proportion or zero-free boundary"]}


if __name__ == "__main__":
    assert set(sys.argv[1:]) <= {"--finite-only", "--generate", "--check"}, "invalid option"
    assert len(sys.argv[1:]) <= 1, "choose one mode"
    if "--finite-only" in sys.argv:
        result = finite()
        print("PASS:", result["count"], "finite algebra checks; no analytic proof certified")
    else:
        result = build()
        if "--check" in sys.argv:
            assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
        else:
            OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        print("PASS: original fourth-power, far cutoff, sampling and smooth-main source bindings")

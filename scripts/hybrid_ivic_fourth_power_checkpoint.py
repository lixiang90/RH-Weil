"""Exact algebra and frozen source bindings for the Ivić fourth-power step.

The analytic input and migration are proved in the sources and reviewed there.
This script does not certify Ivić's theorem, Perron, prime arithmetic or AF.
--finite-only and --check are read-only; --generate writes only this new JSON.
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
SOURCE = P+"hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md"
SOURCE_REVIEWS = [P+"hybrid-ivic-density-and-scalar-fourth-growth-review-root.md",
                  P+"hybrid-ivic-density-and-scalar-fourth-growth-review-radial.md"]
NOTE = "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md"
NOTE_REVIEW = P+"476-summary-review-radial.md"
PACKET = P+"hybrid-positive-height-zero-packet-fourth-upper-research-radial.md"
PACKET_REVIEW = P+"hybrid-original-fourth-power-and-far-review-root.md"
FIXED = P+"hybrid-fixed-start-half-gram-sampling-research-root.md"
FIXED_REVIEW = P+"hybrid-fixed-start-half-gram-sampling-review-compression.md"
SELF = "scripts/hybrid_ivic_fourth_power_checkpoint.py"
OUTPUT = ROOT/"output/hybrid-ivic-fourth-power-checkpoint.json"
FILES = [SOURCE, NOTE, *SOURCE_REVIEWS, NOTE_REVIEW,
         PACKET, PACKET_REVIEW, FIXED, FIXED_REVIEW, SELF]
PAIRS = {SOURCE: SOURCE_REVIEWS, NOTE: [NOTE_REVIEW],
         PACKET: [PACKET_REVIEW], FIXED: [FIXED_REVIEW]}
# All mathematical sources and reviews are frozen. SELF is dynamically
# bound; it cannot have its own embedded frozen digest.
FROZEN = {
    SOURCE: "a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d",
    SOURCE_REVIEWS[0]: "061342dfe685c5cd59114f07444ed36eba3e68905e30f11505a46e3fcc088767",
    SOURCE_REVIEWS[1]: "36125b5f68d340e317e866312ba0d82822de3ae5261d6f18da1561e45245aea7",
    NOTE: "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
    PACKET: "8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481",
    PACKET_REVIEW: "65a4e75ac9ca79dc2c9a2752902ec89acb968eae8c696ad4d54ab1148ec26f6c",
    FIXED: "7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc",
    FIXED_REVIEW: "9f5b4b76bab1483cf0eee8607928f5b85b41feb3e14aa652c838416f37b68cf8",
    NOTE_REVIEW: "c7b7b510fb967d938aff5de5a10668e47dc430df4f390a9457d036538c7b4ed4",
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
        assert s.simplify(left-right) == 0, label
        checks.append(label)

    def nonnegative_polynomial(label, expression, variables):
        assert all(c >= 0 for c in s.Poly(s.expand(expression), *variables).coeffs()), label
        checks.append(label+" (whole nonnegative-variable domain)")

    sigma, theta = s.symbols("sigma theta", real=True)
    u = s.symbols("u", nonnegative=True)
    lower = Q(3831, 4791)
    eq("Ivic stated lower range reduces exactly", s.Rational(lower.numerator, lower.denominator),
       s.Rational(1277, 1597))
    eq("4/5 strictly above Ivic lower range", s.Rational(4, 5)-s.Rational(3831, 4791),
       s.Rational(3, 7985))
    assert Q(3, 7985) > 0
    checks.append("entire fixed grid sigma>=4/5 inside strict lower range")
    eq("5/6 exceeds new-grid start", s.Rational(5, 6)-s.Rational(4, 5), s.Rational(1, 30))
    eq("7/8 strictly below upper range one", 1-s.Rational(7, 8), s.Rational(1, 8))

    f1 = 4*sigma-3+3*(1-sigma)/(2-sigma)
    f2 = 4*sigma-3+3*(1-sigma)/(3*sigma-1)
    fI = 4*sigma-3+3*(1-sigma)/(2*sigma)
    B = fI.subs(sigma, theta)
    oldB = f2.subs(sigma, theta)
    eq("old low derivative formula", s.diff(f1, sigma), 4-3/(2-sigma)**2)
    eq("old high derivative formula", s.diff(f2, sigma), 4-6/(3*sigma-1)**2)
    # These short certificates prove the whole old domain up to 4/5;
    # the earlier 81-check carrier/Perron certificate is not rerun.
    eq("old low derivative numerator sigma=3/4-u",
       (4*(2-sigma)**2-3).subs(sigma, s.Rational(3, 4)-u),
       s.Rational(13, 4)+10*u+4*u**2)
    nonnegative_polynomial("old low derivative positive numerator",
                           s.Rational(13, 4)+10*u+4*u**2, [u])
    eq("old high derivative numerator sigma=3/4+u",
       (4*(3*sigma-1)**2-6).subs(sigma, s.Rational(3, 4)+u),
       s.Rational(1, 4)+30*u+36*u**2)
    nonnegative_polynomial("old high derivative positive numerator",
                           s.Rational(1, 4)+30*u+36*u**2, [u])
    eq("old low denominator is positive", (2-sigma).subs(sigma, s.Rational(3, 4)-u),
       s.Rational(5, 4)+u)
    eq("old high denominator is positive", (3*sigma-1).subs(sigma, s.Rational(3, 4)+u),
       s.Rational(5, 4)+3*u)
    eq("old first endpoint", f1.subs(sigma, s.Rational(1, 2)), 0)
    eq("old join at 3/4", f1.subs(sigma, s.Rational(3, 4)), f2.subs(sigma, s.Rational(3, 4)))
    eq("old join value", f2.subs(sigma, s.Rational(3, 4)), s.Rational(3, 5))
    eq("old whole low-domain maximum at 4/5", f2.subs(sigma, s.Rational(4, 5)), s.Rational(22, 35))

    eq("Ivic fourth exponent derivative", s.diff(fI, sigma), 4-3/(2*sigma**2))
    eq("Ivic derivative lower endpoint", s.diff(fI, sigma).subs(sigma, s.Rational(4, 5)),
       s.Rational(53, 32))
    eq("Ivic derivative-minus-floor numerator",
       s.factor((s.diff(fI, sigma)-s.Rational(53, 32))*32*sigma**2),
       75*sigma**2-48)
    eq("Ivic derivative floor numerator sigma=4/5+u",
       (75*sigma**2-48).subs(sigma, s.Rational(4, 5)+u), 120*u+75*u**2)
    nonnegative_polynomial("Ivic derivative>=53/32 on entire sigma>=4/5",
                           120*u+75*u**2, [u])
    eq("Ivic derivative floor denominator", (32*sigma**2).subs(sigma, s.Rational(4, 5)+u),
       32*(s.Rational(4, 5)+u)**2)
    eq("Ivic-grid first value", fI.subs(sigma, s.Rational(4, 5)), s.Rational(23, 40))
    eq("grid splice need not be continuous",
       f2.subs(sigma, s.Rational(4, 5))-fI.subs(sigma, s.Rational(4, 5)), s.Rational(3, 56))
    eq("Ivic value at original lower theta boundary", fI.subs(sigma, s.Rational(5, 6)),
       s.Rational(19, 30))
    eq("whole low domain cannot win for theta>5/6",
       fI.subs(sigma, s.Rational(5, 6))-s.Rational(22, 35), s.Rational(1, 210))
    assert Q(1, 210) > 0
    checks.append("strict low-domain exclusion throughout original theta range")
    eq("Ivic value at 6/7", fI.subs(sigma, s.Rational(6, 7)), s.Rational(19, 28))
    eq("6/7 low-domain exclusion", s.Rational(19, 28)-s.Rational(22, 35), s.Rational(1, 20))
    eq("Ivic density at 7/8", (3*(1-sigma)/(2*sigma)).subs(sigma, s.Rational(7, 8)),
       s.Rational(3, 14))
    eq("Ivic fourth exponent at 7/8", B.subs(theta, s.Rational(7, 8)), s.Rational(5, 7))
    assert Q(19, 30) > 0 and Q(5, 7) < 1
    checks.append("monotonic entire original range gives 0<B_I<1")

    gap475 = oldB-B
    gap446 = (2*theta-1)-B
    eq("saving relative to 475 for full theta range", gap475,
       3*(1-theta)**2/(2*theta*(3*theta-1)))
    eq("saving relative to 446 for full theta range", gap446,
       (1-theta)*(4*theta-3)/(2*theta))
    eq("475 saving at 7/8", s.Rational(19, 26)-s.Rational(5, 7), s.Rational(3, 182))
    eq("446 saving at 7/8", s.Rational(3, 4)-s.Rational(5, 7), s.Rational(1, 28))
    eq("new factor one-minus-theta positive on theta<=7/8",
       (1-theta).subs(theta, s.Rational(7, 8)-u), s.Rational(1, 8)+u)
    eq("new factor theta positive on theta>5/6",
       theta.subs(theta, s.Rational(5, 6)+u), s.Rational(5, 6)+u)
    eq("new factor 3theta-1 positive on theta>5/6",
       (3*theta-1).subs(theta, s.Rational(5, 6)+u), s.Rational(3, 2)+3*u)
    eq("new factor 4theta-3 positive on theta>5/6",
       (4*theta-3).subs(theta, s.Rational(5, 6)+u), s.Rational(1, 3)+4*u)
    for label, polynomial in [
            ("one-minus-theta", s.Rational(1, 8)+u),
            ("theta", s.Rational(5, 6)+u),
            ("3theta-1", s.Rational(3, 2)+3*u),
            ("4theta-3", s.Rational(1, 3)+4*u)]:
        nonnegative_polynomial("full-domain strict gap factor "+label, polynomial, [u])

    # Six growth terms retained from E_T; only their new exponent budget is
    # checked here. The old kernel, guard, and Parseval proof stays frozen.
    b = s.symbols("b", nonnegative=True)
    for label, exponent in [
            ("main", b), ("first guard cross", 3*b/4-s.Rational(1, 2)),
            ("second guard cross", b/2), ("first guard square", b/2-1),
            ("guard mixed term", b/4-s.Rational(1, 2)), ("second guard square", 0)]:
        nonnegative_polynomial("new growth budget absorbs "+label, b-exponent, [b])
    return {"checks": checks, "count": len(checks),
            "original_theta_domain": "5/6<theta<=7/8",
            "B_I_7_over_8": str(Q(5, 7)),
            "saving_against_475_7_over_8": str(Q(3, 182)),
            "saving_against_446_7_over_8": str(Q(1, 28)),
            "scope": "exact finite whole-interval exponent algebra and source bindings only",
            "external_Ivic_theorem_verified_by_script": False,
            "analytic_fourth_or_AF_proof_certified_by_script": False}


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
    return {"date": "2026-10-08", "base_commit": "5fe68395d20e9738ecc0ba64e8a762f4d93bd073",
            "original_cutoffs_normalizer_positive_guard_and_carrier_retained": True,
            "actual_power_improved_relative_R": True,
            "power_result_conditional_input": "all nontrivial zeta zeros beta<=theta, fixed 5/6<theta<=7/8",
            "outcome_flags_are_reviewed_source_conclusions_not_script_analytic_proofs": True,
            "analytic_upper_certified_by_script": False,
            "constant_fourth_budget_paid": False, "whole_signed_near_paid": False,
            "new_actual_zero_proportion": False, "new_zero_free_boundary": False,
            "new_classical_density_theorem": False, "new_paper": False,
            "finite_certificate": finite(), "review_bindings": reviews,
            "cited_source_hash_bindings": citations, "links_checked": links,
            "files": list(records.values()),
            "external_primary_metadata_reported_by_sources": {
                "title": "Ivic, Topics in Recent Zeta-Function Theory",
                "theorem": "Theorem 9.3, equation (9.63)",
                "raw_pdf_sha256": "fafac152db87abe132858fa97d8fe501c61cd261e20732ef701396fba27b61aa",
                "bytes": 10538942, "pages": 278,
                "external_pdf_or_theorem_verified_by_this_script": False},
            "unproved": ["constant-size canonical scalar fourth budget",
                         "whole signed natural-near arithmetic",
                         "a new actual zero proportion or zero-free boundary"]}


if __name__ == "__main__":
    assert set(sys.argv[1:]) <= {"--finite-only", "--generate", "--check"}, "invalid option"
    assert len(sys.argv[1:]) <= 1, "choose one mode"
    if "--finite-only" in sys.argv:
        result = finite()
        print("PASS:", result["count"], "finite Ivic algebra checks; no analytic theorem certified")
    else:
        result = build()
        if "--check" in sys.argv:
            assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
        else:
            OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        print("PASS: finite Ivic whole-interval algebra and final source bindings")

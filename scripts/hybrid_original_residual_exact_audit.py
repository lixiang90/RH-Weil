"""Exact arithmetic for the original-route residual notes; no new zero theorem.

Written analytic proofs and their hypotheses are essential. In particular the
joint upper/lower arithmetic premises in note 467 are not certified here.
"""

from math import comb
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-original-residual-exact-audit.json"
PREFIX = "reviews/2026-10-07/"
NOTES = [
    "notes/465-centered-high-square-joint-fourth-budget.md",
    "notes/466-high-square-variance-commutator-obstruction.md",
    "notes/467-two-residual-schur-and-commutator-budget.md",
]
REPORTS = [
    "hybrid-whole-fourth-compression-upper-research-radial.md",
    "hybrid-high-parity-gram-and-mobius-completion-research-radial.md",
    "hybrid-three-high-one-low-joint-schur-budget-research.md",
    "hybrid-spectral-low-high-information-and-narrow-window-research-compression.md",
    "hybrid-parity-weighted-high-cubic-research.md",
    "hybrid-high-square-variance-commutator-obstruction.md",
    "hybrid-high-square-sharp-linear-variance-obstruction.md",
]
REVIEWS = [
    "hybrid-whole-fourth-compression-review-twisted.md",
    "hybrid-high-parity-gram-review-twisted.md",
    "hybrid-three-high-one-low-joint-schur-review-compression.md",
    "hybrid-three-high-one-low-joint-schur-review-radial.md",
    "hybrid-spectral-low-high-narrow-window-review-radial.md",
    "hybrid-parity-weighted-high-cubic-review-compression.md",
    "hybrid-original-residual-research-review-root.md",
    "465-centered-square-joint-budget-review-twisted.md",
    "465-466-centered-variance-joint-review-twisted.md",
    "465-466-high-square-budget-review-radial.md",
    "467-two-residual-schur-review-root.md",
    "467-two-residual-schur-review-twisted.md",
]
REVIEW_PAIRS = {
    NOTES[0]: [PREFIX+REVIEWS[i] for i in (7, 8, 9)],
    NOTES[1]: [PREFIX+REVIEWS[i] for i in (8, 9)],
    NOTES[2]: [PREFIX+REVIEWS[i] for i in (10, 11)],
    PREFIX+REPORTS[0]: [PREFIX+REVIEWS[i] for i in (0, 6)],
    PREFIX+REPORTS[1]: [PREFIX+REVIEWS[i] for i in (1, 6)],
    PREFIX+REPORTS[2]: [PREFIX+REVIEWS[i] for i in (2, 3, 6)],
    PREFIX+REPORTS[3]: [PREFIX+REVIEWS[i] for i in (4, 6)],
    PREFIX+REPORTS[4]: [PREFIX+REVIEWS[i] for i in (5, 6)],
    PREFIX+REPORTS[5]: [PREFIX+REVIEWS[6]],
    PREFIX+REPORTS[6]: [PREFIX+REVIEWS[6]],
}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT / name)
    return {"path": name, "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data)}


def exact_arithmetic():
    t, x, c, z = s.symbols("t x c z")
    half = s.Rational(1, 2)
    dh = t*(t+1)/2
    dl = s.Rational(1, 4)-t/2+t*t/2
    sh, sl, cross = [2*s.integrate(p, (t, 0, half))
                     for p in (dh*dh, dl*dl, dh*dl)]
    adjacent = half**4/4-half**5/5
    opposite = half**4/4-half**5/3
    el = 4*adjacent+8*opposite
    delta = el-sl
    assert (sh, sl, cross, el, delta) == (
        s.Rational(19, 480), s.Rational(7, 240), s.Rational(23, 960),
        s.Rational(19, 240), s.Rational(1, 20))
    kcomm = 2*s.integrate(
        x*s.integrate((dh-dh.subs(t, x-t))**2,
                      (t, x-half, half)), (x, half, 1))
    assert kcomm == s.Rational(41, 10080)
    m = s.Rational(3, 8)
    square = -4*m*z*z+m*m*z/2
    assert s.expand(square+4*m*(z-m/16)**2-m**3/64) == 0
    weaker_qmin = (kcomm-m**3/64)/(4*m)
    assert weaker_qmin == s.Rational(33479, 15482880)
    mass, w, change, row = s.symbols("mass w change row")
    sharp_gap = mass*change**2+4*mass*row-4*(w+change)*row
    sharp_sos = (mass*(change-2*row/mass)**2
                 +4*row*(mass-w)**2/mass
                 +4*row*(w*(mass-w)-row)/mass)
    assert s.simplify(sharp_gap-sharp_sos) == 0
    qmin = kcomm/(4*m)
    assert qmin == s.Rational(41, 15120) > s.Rational(1, 400)
    rejected_q = s.Rational(1, 1600)
    assert qmin > rejected_q
    assert 4*m*rejected_q+m**3/64 == s.Rational(1443, 819200) < kcomm
    # The counterfactual arithmetic in 465 is valid, but its premise is excluded.
    assert rejected_q*el < s.Rational(17, 2400)**2
    assert cross+s.Rational(17, 2400) == s.Rational(149, 4800)
    assert 16*rejected_q*s.Rational(149, 4800) < s.Rational(9, 500)**2
    old_b = sh+el+6*cross+rejected_q+6*s.Rational(17, 2400)+s.Rational(9, 500)
    assert old_b == s.Rational(2589, 8000)
    assert s.Rational(4, 9)/(s.Rational(1, 3)+old_b) == s.Rational(32000, 47301)
    # Exact lower comparisons show that the scalar envelope cannot certify 1/3.
    assert qmin > s.Rational(1, 500)
    assert qmin*el > s.Rational(1, 80)**2
    assert cross+s.Rational(1, 80) == s.Rational(7, 192)
    assert 16*qmin*s.Rational(7, 192) > s.Rational(17, 500)**2
    scalar_lower = sh+el+6*cross+s.Rational(1, 500)+6*s.Rational(1, 80)+s.Rational(17, 500)
    assert scalar_lower == s.Rational(747, 2000) > s.Rational(1, 3)
    # The centered Gram envelope also needs additional joint information.
    test_c = s.Rational(1, 30)
    test_radicand = (qmin-(test_c-cross)**2/delta)*test_c
    test_gap = (s.Rational(1, 3)-(sh+qmin+el+6*test_c))/4
    assert test_c-cross == s.Rational(3, 320)
    assert test_radicand > test_gap**2 > 0
    assert test_c**2 < (sh+qmin)*el
    # A new joint candidate: q upper and k lower, both still unproved arithmetic.
    q, k, b = s.Rational(1, 350), s.Rational(1, 40), s.Rational(81, 250)
    assert qmin < q
    assert q-qmin == s.Rational(11, 75600)
    assert q*delta < s.Rational(3, 250)**2
    hi = cross+s.Rational(3, 250)
    assert hi == s.Rational(863, 24000)
    remaining = b-(sh+q+el-k)-6*c
    assert remaining.subs(c, hi) == s.Rational(163, 14000) > 0
    polynomial = s.expand(remaining**2-16*(q-(c-cross)**2/delta)*(c-k/4))
    expected = 320*c**3+s.Rational(56, 3)*c**2-s.Rational(1257437, 504000)*c+s.Rational(717527777, 14112000000)
    assert polynomial == expected
    intervals = []
    all_coefficients = []
    for i in range(32):
        lo, upper = hi*i/32, hi*(i+1)/32
        power = s.Poly(polynomial.subs(c, lo+(upper-lo)*t), t)
        coefficients = [
            sum(power.nth(j)*s.Rational(comb(k0, j), comb(3, j))
                for j in range(k0+1)) for k0 in range(4)
        ]
        assert min(coefficients) > 0
        all_coefficients.extend(coefficients)
        intervals.append({"lo": str(lo), "hi": str(upper),
                          "cubic_bernstein_coefficients": [str(v) for v in coefficients]})
    assert min(all_coefficients) == s.Rational(665078890949, 6502809600000000)
    proportion = s.Rational(4, 9)/(s.Rational(1, 3)+b)
    assert proportion == s.Rational(1000, 1479) > s.Rational(27, 40)
    return {
        "flat_diagonal_and_low_fourth": {
            "S_high": str(sh), "S_low": str(sl), "C_high_low": str(cross),
            "low_fourth": str(el), "low_residual_variance": str(delta)},
        "high_weight_commutator_written_proof_constant": str(kcomm),
        "PSD_variance_necessary_lower_bound": str(qmin),
        "weaker_trace_dependent_PSD_variance_lower_bound": str(weaker_qmin),
        "sharp_rowwise_SOS_identity_verified": True,
        "additionally_excluded_q": "1/400",
        "excluded_counterfactual_q": str(rejected_q),
        "scalar_budget_necessary_lower_comparison": str(scalar_lower),
        "centered_gram_diagnostic_not_an_actual_matrix": {
            "q": str(qmin), "c": str(test_c), "k": "0",
            "radicand": str(test_radicand),
            "positive_gap_to_one_third_divided_by_four": str(test_gap),
            "strict_squared_margin": str(test_radicand-test_gap**2)},
        "joint_candidate_unproved_arithmetic": {
            "q_definition": "||H^2 - W||_HS^2 / d",
            "k_definition": "||[H,L]||_HS^2 / d",
            "limsup_q_required": str(q), "liminf_k_required": str(k),
            "whole_fourth_conditional_upper": str(b),
            "simple_proportion_conditional_lower": str(proportion),
            "c_enclosing_interval": ["0", str(hi)],
            "remaining_square_root_margin": "163/14000",
            "polynomial_power_coefficients_descending": [
                str(expected.coeff(c, j)) for j in (3, 2, 1, 0)],
            "minimum_bernstein_coefficient": str(min(all_coefficients)),
            "bernstein_intervals": intervals,
        },
    }


def build():
    prior = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts/hybrid_field_decision_exact_audit.py"), "--check"],
        cwd=ROOT, capture_output=True, text=True, check=True)
    assert prior.stdout.startswith("PASS:")
    files = NOTES+[PREFIX+n for n in REPORTS+REVIEWS]+[
        "scripts/hybrid_original_residual_exact_audit.py",
        "scripts/hybrid_spectral_mt_joint_exact_certificate.py",
        "output/hybrid-spectral-mt-joint-exact-certificate.json"]
    checks = []
    for source, review_names in REVIEW_PAIRS.items():
        sha = binding(source)["sha256_canonical_lf"]
        for name in review_names:
            assert sha in canonical(ROOT / name).decode("utf-8"), (source, name)
            checks.append({"source": source, "review": name, "source_sha256": sha})
    links = 0
    for name in files:
        content = canonical(ROOT / name).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", content), name
        if name.endswith(".md"):
            for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                # A displayed TeX product such as [phi(z)](phi(z+log p)) is
                # not a Markdown file link. All local links in this manifest
                # point to the explicit source/artifact extensions below.
                if not re.search(r"\.(md|py|json|tex|pdf|lean)(#.*)?$", target):
                    continue
                target = re.sub(r":\d+$", "", target.split("#", 1)[0])
                assert (ROOT / name).parent.joinpath(target).resolve().exists(), (name, target)
                links += 1
    return {
        "date": "2026-10-07", "base_repository_commit": "e8e6bb68463e31a7d28349364926f9abb9ead927",
        "scope": "exact finite arithmetic and final-source review bindings; not an analytic proof kernel",
        "new_actual_proportion": False, "new_zero_free_boundary": False, "new_paper": False,
        "unchanged_sigma_under_stated_R": "0.87495701942009894612860385056...",
        "previous_checkpoint_checked": prior.stdout.strip(),
        "finite_certificate": exact_arithmetic(),
        "links_checked": links, "review_bindings": checks,
        "files": [binding(name) for name in files],
        "unproved": [
            "the actual joint candidate limsup q <= 1/350 and liminf k >= 1/40",
            "whole high signed arithmetic with original internal projections",
            "an improved actual simple-zero proportion or zero-free boundary",
            "independent certification of the imported analytic R kernel",
        ],
    }


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "audit differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("PASS: original residual constants, PSD obstruction, 128 positive Bernstein coefficients and preserved checkpoint")

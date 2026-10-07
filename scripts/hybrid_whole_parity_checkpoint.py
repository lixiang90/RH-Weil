"""Exact algebra and source-bound review checkpoint for the whole parity research.

Analytic proofs live in the research sources and independent reviews. This script
does not prove the imported R kernel, a high residual upper bound, or new zeros.
"""

from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import re
import subprocess
import sys

import sympy as s
from hybrid_whole_low_parity_exact import path_integrals, weighted_constants

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "reviews/2026-10-08/"
NOTE = "notes/469-original-whole-parity-gap-and-joint-fourth-budget.md"
NOTE2 = "notes/470-centered-spectral-variance-excludes-small-high-residual.md"
OUTPUT = ROOT / "output/hybrid-whole-parity-checkpoint.json"
GEOMETRY = "scripts/hybrid_whole_low_parity_exact.py"
REPORTS = [
    "hybrid-positive-tail-whole-high-parity-gap-research-compression.md",
    "hybrid-whole-low-parity-fourth-research-root.md",
    "hybrid-parity-split-schur-and-even-anticommutator-research-radial.md",
]
REVIEWS = [
    "hybrid-positive-tail-whole-high-parity-gap-review-twisted.md",
    "hybrid-whole-low-parity-fourth-review-compression.md",
    "hybrid-whole-parity-and-joint-fourth-review-root.md",
    "hybrid-whole-low-and-split-gram-review-twisted.md",
    "469-whole-parity-budget-review-radial.md",
    "hybrid-parity-split-schur-and-even-anticommutator-review-compression.md",
    "470-centered-spectral-variance-review-twisted.md",
    "470-centered-spectral-variance-review-radial.md",
]
REVIEW_PAIRS = {
    PREFIX + REPORTS[0]: [PREFIX + REVIEWS[i] for i in (0, 2)],
    PREFIX + REPORTS[1]: [PREFIX + REVIEWS[i] for i in (1, 3)],
    PREFIX + REPORTS[2]: [PREFIX + REVIEWS[i] for i in (2, 3, 5)],
    GEOMETRY: [PREFIX + REVIEWS[i] for i in (1, 3)],
    NOTE: [PREFIX + REVIEWS[i] for i in (3, 4)],
    NOTE2: [PREFIX + REVIEWS[i] for i in (6, 7)],
}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT / name)
    return {"path": name, "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data), "lines": len(data.splitlines())}


def algebra():
    u, v, R = s.symbols("u v R", positive=True)
    for hu, hv, target in ((u, v, R**2 * (u-v)**2),
                            (R, v, (u*v-R**2)**2),
                            (u, R, (u*v-R**2)**2),
                            (R, R, (u*v-R**2)**2)):
        expression = (u**2*v**2-hu**2*hv**2
            -R**2*(u**2-hu**2+v**2-hv**2)+R**2*(u-v)**2)
        assert s.expand(expression-target) == 0
    m, c, z, a = s.symbols("m c z a", positive=True)
    quadratic = (a-2*m*z)**2/(4*m)+c*z**2
    minimum = a**2*c/(4*m*(m+c))
    square = (m+c)*(z-a/(2*(m+c)))**2
    assert s.simplify(quadratic-minimum-square) == 0
    branch_margin = c*a**2/(4*m**2)-minimum
    assert s.simplify(branch_margin-c**2*a**2/(4*m**2*(m+c))) == 0
    floor, Q = F(41, 15120), F(1, 350)
    rbar = (Q-floor)/2
    assert rbar == F(11, 151200)
    A, B, h = (Q-rbar)*F(11, 480), rbar*F(13, 480), F(47, 5000)
    remainder, margin = h*h-A-B, (h*h-A-B)**2-4*A*B
    assert (A, B) == (F(4631, 72576000), F(143, 72576000))
    assert remainder == F(365807, 16200000000) > 0
    assert margin == F(155910001, 22325625000000000000) > 0
    first, second = F(76, 625), F(79, 2000)
    D = first**2-F(19, 1920)
    root_margins = [D, D**2-F(1, 42000),
                    second**4-F(11, 4536000), F(13, 500)-(first+second)**2]
    assert root_margins == [F(733609, 150000000),
        F(17275154167, 157500000000000000), F(84695927, 9072000000000000),
        F(4679, 100000000)]
    assert all(x > 0 for x in root_margins)
    te, to, de, do, ze = F(16, 3), F(31), F(11, 480), F(13, 480), F(13, 500)
    g = 6+2/to
    U = (F(19, 480)+Q+F(19, 240)+2*te*Q+2*(to-te)*rbar
         +g*F(23, 960)+2*(1/te-1/to)*ze+g*g*de/(8*te)+g*g*do/(8*to))
    coefficient = 1+1/(2*to)
    assert g == F(188, 31) and coefficient == F(63, 62)
    assert U == F(25710335933, 77218272000)
    assert F(1, 3)-U == F(29088067, 77218272000) > 0
    assert F(77, 250)-(U-coefficient*F(1, 40)) == F(34485043, 77218272000) > 0
    p, t, delta, gamma = s.symbols("p t delta gamma", real=True)
    assert s.expand(gamma**2*delta/(8*t)-(gamma*p-2*t*p**2/delta)
        -2*t/delta*(p-gamma*delta/(4*t))**2) == 0
    variance, commutator_ratio = s.Rational(17, 1440), s.Rational(41, 3780)
    actual_floor = (s.sqrt(104899)-275)/15120
    assert 104899 > 275**2
    variable = s.symbols("q", nonnegative=True)
    polynomial = variable**2+(4*variance-commutator_ratio)*variable-commutator_ratio*variance
    assert s.simplify(polynomial.subs(variable, actual_floor)) == 0
    Qs = s.Rational(1, 350)
    assert polynomial.subs(variable, Qs) == -s.Rational(15199, 952560000)
    exclusion_gap = commutator_ratio-Qs-3*Qs*variance/(Qs+variance)
    assert exclusion_gap == s.Rational(15199, 13967100) > 0
    xx, yy, vv = s.symbols("x y v", nonnegative=True)
    assert s.expand(xx*(vv-yy)-yy**2-((xx+yy)*vv-yy*(xx+yy+vv))) == 0
    return {
        "clip_scalar_piecewise_square_identities": 4,
        "tail_elimination_exact_completed_square": True,
        "tail_elimination_remaining_branch_nonnegative": True,
        "earlier_actual_high_parity_gap_no_growth_premise": floor,
        "whole_low_path_integrals": path_integrals(),
        "whole_low_weighted_constants": weighted_constants(),
        "new_centered_actual_necessary_bound": {
            "spectral_diagonal_covariance_exact": "(y+epsilon-mu*m)^2 <= (x-mu^2)*(v-y)",
            "variance": str(variance), "K_over_M": str(commutator_ratio),
            "actual_q_and_parity_gap_lower": str(actual_floor),
            "decimal_lower": str(s.N(actual_floor, 45)),
            "no_fourth_growth_premise": True,
            "old_Q_excluded": True, "old_Q_polynomial_value": "-15199/952560000",
            "strict_rational_exclusion_gap": str(exclusion_gap)},
        "excluded_Q_counterfactual_forward_certificate": {
            "Q": Q, "odd_variance_cap": rbar, "covariance_root_squared_terms": [A, B],
            "covariance_upper": h, "covariance_root_remainder": remainder,
            "covariance_squared_margin": margin, "z_even_upper": ze,
            "z_even_root_margins": root_margins,
            "Young_weights": [te, to], "whole_F_upper_without_k_premise": U,
            "k_coefficient": coefficient, "one_third_strict_margin": F(1, 3)-U,
            "additional_old_k_premise": "1/40", "additional_upper": "77/250"},
    }


def build():
    prior = subprocess.run([sys.executable, "-B",
        str(ROOT / "scripts/hybrid_original_cubic_parity_checkpoint.py"), "--check"],
        cwd=ROOT, capture_output=True, text=True, check=True)
    assert prior.stdout.startswith("PASS:")
    files = [NOTE, NOTE2]+[PREFIX+n for n in REPORTS+REVIEWS]+[GEOMETRY,
        "scripts/hybrid_whole_parity_checkpoint.py"]
    reviews = []
    for source, review_names in REVIEW_PAIRS.items():
        sha = binding(source)["sha256_canonical_lf"]
        for name in review_names:
            assert sha in canonical(ROOT / name).decode("utf-8"), (source, name)
            reviews.append({"source": source, "review": name, "source_sha256": sha})
    links, cited_sources = 0, []
    for name in files:
        content = canonical(ROOT / name).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", content), name
        if not name.endswith(".md"):
            continue
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            if target.startswith(("https:", "http:", "#", "mailto:")):
                continue
            if not re.search(r"\.(md|py|json|tex|pdf|lean)(#.*)?$", target):
                continue
            target = re.sub(r":\d+$", "", target.split("#", 1)[0])
            assert (ROOT/name).parent.joinpath(target).resolve().exists(), (name, target)
            links += 1
        for target, sha in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)\s*\|\s*`?([a-f0-9]{64})`?", content):
            path = (ROOT/name).parent.joinpath(target).resolve()
            assert hashlib.sha256(canonical(path)).hexdigest() == sha, (name, target)
            cited_sources.append({"document": name, "source": path.relative_to(ROOT).as_posix(), "sha256": sha})
    return {
        "date": "2026-10-08", "base_repository_commit": "dc19ebde221a43031bf4eb822a752b21aee4beec",
        "scope": "exact finite algebra, full low path integration, final source and independent review bindings",
        "previous_checkpoint_checked": prior.stdout.strip(),
        "new_actual_whole_high_necessary_constraint": True,
        "new_actual_low_parity_constants": True,
        "new_marked_13_orthogonality_requires_stated_R_and_bounded_q": True,
        "new_high_residual_upper_bound": False, "new_actual_proportion": False,
        "old_Q_one_over_350_excluded_by_actual_centered_variance": True,
        "new_zero_free_boundary": False, "new_paper": False,
        "unchanged_sigma_under_stated_R": "0.87495701942009894612860385056...",
        "finite_certificate": algebra(), "links_checked": links,
        "review_bindings": reviews, "cited_source_hash_bindings": cited_sources,
        "files": [binding(name) for name in files],
        "unproved": ["a reachable high-residual upper bound consistent with the new actual lower",
            "a useful entire signed fourth budget beyond the excluded Q example", "liminf k_T >= 1/40",
            "an actual new simple-zero proportion or zero-free boundary",
            "independent certification of the imported analytic R kernel"],
    }


if __name__ == "__main__":
    result = json.loads(json.dumps(build(), default=str))
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("PASS: whole parity scalar identities, exact low paths, continuous Young certificate and final independent review bindings")

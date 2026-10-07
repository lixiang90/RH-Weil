"""Exact checkpoint for the original-route cubic and parity reductions.

Written analytic proofs and source-bound independent reviews are required.
This script checks finite algebra, rational integrals, links and frozen bytes;
it does not certify the analytic R input or prove a new zero proportion.
"""

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-original-cubic-parity-checkpoint.json"
PREFIX = "reviews/2026-10-07/"
NOTE = "notes/468-original-mixed-cubic-and-parity-resolved-fourth-reduction.md"
REPORTS = [
    "hybrid-high-parity-traceclass-cubic-research-compression.md",
    "hybrid-background-entire-mixed-cubic-research-compression.md",
    "hybrid-background-cubic-relative-actual-recovery-research-compression.md",
    "hybrid-parity-resolved-residual-necessary-constraints-radial.md",
    "hybrid-three-high-one-low-nonalternating-gate-research.md",
    "hybrid-thin-high-short-low-entire-three-one-research.md",
    "hybrid-thin-high-short-low-unconditional-three-one-research-radial.md",
]
REVIEWS = [
    "hybrid-high-parity-traceclass-cubic-review-root.md",
    "hybrid-three-high-one-low-nonalternating-gate-review-root.md",
    "hybrid-original-mixed-cubic-and-parity-review-root.md",
    "hybrid-three-high-one-low-gate-and-capped-review-compression.md",
    "hybrid-mixed-cubic-and-parity-constraints-review-twisted.md",
    "468-original-cubic-and-parity-review-radial.md",
]
REVIEW_PAIRS = {
    NOTE: [PREFIX+REVIEWS[i] for i in (4, 5)],
    PREFIX+REPORTS[0]: [PREFIX+REVIEWS[0]],
    PREFIX+REPORTS[1]: [PREFIX+REVIEWS[i] for i in (2, 4, 5)],
    PREFIX+REPORTS[2]: [PREFIX+REVIEWS[i] for i in (2, 4, 5)],
    PREFIX+REPORTS[3]: [PREFIX+REVIEWS[i] for i in (2, 4)],
    PREFIX+REPORTS[4]: [PREFIX+REVIEWS[i] for i in (1, 3)],
    PREFIX+REPORTS[5]: [PREFIX+REVIEWS[i] for i in (1, 3)],
    PREFIX+REPORTS[6]: [PREFIX+REVIEWS[i] for i in (1, 4)],
}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT / name)
    return {"path": name, "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data), "lines": len(data.splitlines())}


def exact_arithmetic():
    x, y, a = s.symbols("x y a", real=True)
    half = s.Rational(1, 2)
    absolute = 2*s.integrate(s.integrate(x*y*(x-y), (y, 0, x)), (x, 0, half))
    lower = s.integrate(s.integrate(x*y*(x+y), (y, 0, half-x)), (x, 0, half))
    upper = s.integrate(s.integrate(x*y*(1-x-y), (y, half-x, half)), (x, 0, half))
    assert (absolute, lower, upper) == (
        s.Rational(1, 480), s.Rational(1, 960), s.Rational(7, 1920))
    odd = 4*(absolute+lower+upper)
    even = s.Rational(1, 20)-odd
    assert (odd, even) == (s.Rational(13, 480), s.Rational(11, 480))
    floor, candidate = s.Rational(41, 15120), s.Rational(1, 350)
    odd_cap = candidate-floor
    stationary = candidate*odd/(odd+even)
    assert odd_cap == s.Rational(11, 75600) < stationary == s.Rational(13, 8400)
    first, second = floor*even, odd_cap*odd
    remaining = s.Rational(1, 10000)-first-second
    squared_margin = remaining**2-4*first*second
    assert remaining == s.Rational(3077, 90720000) > 0
    assert squared_margin == s.Rational(4883, 28576800000000) > 0
    cross = s.Rational(23, 960)
    assert cross-s.Rational(1, 100) == s.Rational(67, 4800)
    assert cross+s.Rational(1, 100) == s.Rational(163, 4800)
    thin, short, fixed_a = s.Rational(11, 20), s.Rational(1, 3), s.Rational(22, 25)
    caps = 3*thin+short
    assert caps == s.Rational(119, 60) < 2
    net_lo, net_hi = 1-thin-short, 2*thin-half+short
    assert (net_lo, net_hi) == (s.Rational(7, 60), s.Rational(14, 15))
    raw_exponent, canonical_saving = caps/2-1, 1-(fixed_a-half)*caps
    assert raw_exponent == -s.Rational(1, 120)
    assert canonical_saving == s.Rational(739, 3000)
    assert caps/2-2 == -s.Rational(121, 120)
    assert caps/2-3 == -s.Rational(241, 120)
    larger_caps = 1+2*thin+half
    assert larger_caps == s.Rational(13, 5)
    assert 1-(fixed_a-half)*larger_caps == s.Rational(3, 250)
    assert larger_caps/2-3 == -s.Rational(17, 10)
    mixed_exponent = s.Rational(5, 2)*a-s.Rational(9, 4)
    assert s.solve(mixed_exponent, a) == [s.Rational(9, 10)]
    assert mixed_exponent.subs(a, s.Rational(89, 100)) == -s.Rational(1, 40)
    traceclass_exponent = 3*a-s.Rational(5, 2)
    assert s.solve(traceclass_exponent, a) == [s.Rational(5, 6)]
    assert traceclass_exponent.subs(a, s.Rational(7, 8)) > 0
    cube, pp = s.symbols("C P", commutative=False)
    expansion = s.expand((cube+pp)**3-cube**3)
    expected = [cube**2*pp, cube*pp*cube, pp*cube**2,
                cube*pp**2, pp*cube*pp, pp**2*cube, pp**3]
    assert set(s.Add.make_args(expansion)) == set(expected)
    minkowski_sos = (x-y)**2*(7*x*x+10*x*y+7*y*y)
    assert s.expand(8*(x**4+y**4)-(x+y)**4-minkowski_sos) == 0
    return {
        "flat_low_parity_integrals": {
            "absolute_difference": str(absolute), "lower_triangle": str(lower),
            "upper_triangle": str(upper), "odd_residual_variance": str(odd),
            "even_residual_variance": str(even)},
        "high_even_residual_necessary_floor_under_bounded_q": str(floor),
        "candidate_still_unproved": {
            "q_upper": str(candidate), "odd_residual_cap": str(odd_cap),
            "root_sum_stationary_point": str(stationary),
            "strict_root_sum_upper": "1/100", "square_margin": str(squared_margin),
            "c_enclosing_interval": ["67/4800", "163/4800"]},
        "unconditional_capped_31": {
            "thin_high_cap": str(thin), "short_low_cap": str(short),
            "sum_caps": str(caps), "net_ratio_gap": [str(net_lo), str(net_hi)],
            "raw_power_exponent": str(raw_exponent), "R_input_required": False},
        "additional_R_capped_31_budget": {
            "fixed_a": str(fixed_a), "main_power_saving": str(canonical_saving),
            "Fourier_ghost_exponent": str(caps/2-2),
            "height_tail_exponent": str(caps/2-3),
            "larger_nonalternating_caps": str(larger_caps),
            "larger_nonalternating_power_saving": "3/250"},
        "mixed_cubic_threshold_under_stated_R": "9/10",
        "mixed_cubic_exponent_at_89_over_100": "-1/40",
        "traceclass_cubic_threshold_not_available_at_7_over_8": "5/6",
        "proper_power_cube_word_count": len(expected),
        "proper_power_word_powers": [1, 1, 1, 2, 2, 2, 3],
        "minkowski_fourth_factor_8_SOS_verified": True,
        "actual_cubic_relative_written_proof_bound": "(sqrt(a_T)+1)/log(X) + o(1)",
        "actual_cubic_smallness_sufficient_growth_premise": "a_T = o(log(X)^2)",
    }


def build():
    prior = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts/hybrid_original_residual_exact_audit.py"), "--check"],
        cwd=ROOT, capture_output=True, text=True, check=True)
    assert prior.stdout.startswith("PASS:")
    files = [NOTE]+[PREFIX+n for n in REPORTS+REVIEWS]+[
        "scripts/hybrid_original_cubic_parity_checkpoint.py"]
    reviews = []
    for source, review_names in REVIEW_PAIRS.items():
        sha = binding(source)["sha256_canonical_lf"]
        for name in review_names:
            assert sha in canonical(ROOT / name).decode("utf-8"), (source, name)
            reviews.append({"source": source, "review": name, "source_sha256": sha})
    links = 0
    for name in files:
        content = canonical(ROOT / name).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", content), name
        if name.endswith(".md"):
            for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                if not re.search(r"\.(md|py|json|tex|pdf|lean)(#.*)?$", target):
                    continue
                target = re.sub(r":\d+$", "", target.split("#", 1)[0])
                assert (ROOT / name).parent.joinpath(target).resolve().exists(), (name, target)
                links += 1
    return {
        "date": "2026-10-08",
        "base_repository_commit": "4b636a1c0e8374521cbfe82524e33ccb718af9b7",
        "scope": "finite exact arithmetic and final source-review bindings, not an analytic proof kernel",
        "new_actual_proportion": False, "new_zero_free_boundary": False, "new_paper": False,
        "unchanged_sigma_under_stated_R": "0.87495701942009894612860385056...",
        "previous_checkpoint_checked": prior.stdout.strip(),
        "finite_certificate": exact_arithmetic(),
        "links_checked": links, "review_bindings": reviews,
        "files": [binding(name) for name in files],
        "unproved": [
            "a new actual bound for the whole high fourth a_T",
            "whole31, whole22 and full signed fourth constant with original internal projections",
            "the actual joint candidate limsup q <= 1/350 and liminf k >= 1/40",
            "a new actual simple-zero proportion or zero-free boundary",
            "independent certification of the imported analytic R kernel",
        ],
    }


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("PASS: original cubic/parity exact integrals, capped31 powers, final review bindings and preserved checkpoint")

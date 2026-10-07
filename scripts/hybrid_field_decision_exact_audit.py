"""Exact finite checks for note 464; no analytic or zero-free certification."""

from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-field-decision-exact-audit.json"
NOTE = "notes/464-field-selection-decision-and-conjugation-obstruction.md"
REVIEWS = [
    "reviews/2026-10-07/464-field-selection-review-radial.md",
    "reviews/2026-10-07/464-field-selection-review-twisted.md",
]
INPUTS = [
    "notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md",
    "notes/457-number-field-choice-and-relative-amplification.md",
    "notes/458-gaussian-all-row-large-sieve-comparison.md",
    "notes/460-generic-power-row-obstruction-and-field-choice.md",
    "reviews/2026-10-07/hybrid-number-field-quantitative-review-radial.md",
    "reviews/2026-10-07/hybrid-field-change-special-mobius-next-research.md",
    "reviews/2026-10-07/joint-and-fourth-checkpoint.json",
]


def canonical(path):
    data = path.read_bytes()
    if path.suffix == ".pdf":
        return data
    return data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT / name)
    return {"path": name, "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data)}


def display(q):
    with localcontext() as ctx:
        ctx.prec = 60
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def polynomial(e):
    return 657 * e**3 - 954 * e**2 + 21 * e + 20


def quartic(a, b):
    q = b[0]**2 + b[1]**2
    # The two examples have prime norm 13 and invertible imaginary coordinate.
    assert q == 13
    imod = (-b[0] * pow(b[1], -1, q)) % q
    roots = {1: (1, 0), imod: (0, 1), q - 1: (-1, 0),
             (-imod) % q: (0, -1)}
    value = (a[0] + a[1] * imod) % q
    assert value != 0
    return roots[pow(value, (q - 1) // 4, q)]


def build():
    # Preserve the previous accepted papers, notes, source and review bindings.
    checked = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts/hybrid_joint_and_fourth_checkpoint.py"), "--check"],
        cwd=ROOT, text=True, capture_output=True, check=True,
    )
    assert checked.stdout.startswith("PASS:")
    lo, hi = F(16683858898627, 10**14), F(16683858898628, 10**14)
    assert polynomial(lo) > 0 > polynomial(hi)
    for _ in range(150):
        mid = (lo + hi) / 2
        if polynomial(mid) > 0:
            lo = mid
        else:
            hi = mid
    e = (lo + hi) / 2
    t = (1 + 3 * e) / (8 * e)
    delta = (5 - 9 * e) / (6 + 18 * e)
    e6, e4, e2 = [(1 + (d - 1) * t) / d for d in (6, 4, 2)]
    assert e6 - e4 == (t - 1) / 12
    assert e6 - e2 == (t - 1) / 3
    assert abs(e6 - (F(2, 3) + delta * t)) < F(1, 10**50)
    els = max(F(1), 2 * (1 + t) / 3, t + F(1, 3))
    assert els == t + F(1, 3)
    pi, nu, nubar = (-1, 2), (3, 2), (3, -2)
    for a, b in (pi, nu, nubar):
        assert a % 2 == 1 and b % 2 == 0 and (a + b - 1) % 4 == 0
    assert quartic(pi, nu) == (1, 0)
    assert quartic(pi, nubar) == (0, 1)
    shift_models = []
    for d in range(2, 101, 2):
        m, rho = d // 2, d // 2 - 1
        assert (-1 - rho) % d == m
        ntheta = d // gcd(d, rho)
        assert ntheta == (m if m % 2 else 2 * m)
        assert d == 2 or ntheta >= 3
        assert (ntheta == 3) == (d == 6)
        shift_models.append({"d": d, "rho": rho, "theta_character_order": ntheta})
    files = [NOTE, *REVIEWS, "scripts/hybrid_field_decision_exact_audit.py"]
    note_sha = binding(NOTE)["sha256_canonical_lf"]
    links = 0
    for name in files:
        data = canonical(ROOT / name).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", data), name
        if name in REVIEWS:
            assert note_sha in data, (name, "review does not bind final note")
        if name.endswith(".md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", data):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                target = re.sub(r":\d+$", "", target.split("#", 1)[0])
                assert (ROOT / name).parent.joinpath(target).resolve().exists(), (name, target)
                links += 1
    return {
        "date": "2026-10-07",
        "base_repository_commit": "a49bd509d571f95adcb9047684d81ef33b311713",
        "scope": "finite residue arithmetic and rational budget checks only; written proofs and stated hypotheses remain essential",
        "new_zero_free_boundary": False, "new_paper": False,
        "unchanged_sigma_under_stated_R": "0.87495701942009894612860385056...",
        "previous_checkpoint_checked": checked.stdout.strip(),
        "root_interval_refinement": [str(lo), str(hi)],
        "midpoint_display_not_an_analytic_bound": {
            "t": display(t), "e6": display(e6), "conditional_e4": display(e4),
            "conditional_e2": display(e2), "gaussian_LS": display(els),
            "gaussian_LS_minus_e6": display(els - e6),
            "conditional_quartic_branch_gain": display(e6 - e4),
        },
        "exact_conjugation_example": {
            "pi": list(pi), "nu": list(nu), "nu_conjugate": list(nubar), "both_column_norms": 13,
            "quartic_pi_over_nu": list(quartic(pi, nu)),
            "quartic_pi_over_nu_conjugate": list(quartic(pi, nubar)),
        },
        "finite_single_shift_models": shift_models,
        "links_checked": links,
        "preserved_inputs": [binding(name) for name in INPUTS],
        "files": [binding(name) for name in files],
        "not_certified": [
            "Gaussian special Mobius whole-row near-linear bound",
            "uniform target-twisted completed reflection and Euler reciprocal",
            "new marked/plain moments, global detector optimization or family continuation",
            "external proof-kernel certification, RH or a new zero-free region",
        ],
    }


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "audit differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PASS: exact conjugation example, 50 finite shift models, rational budgets and preserved checkpoint")

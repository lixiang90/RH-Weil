"""Bind the number-field research and verify the previous frozen artifacts."""

from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PREVIOUS = ROOT / "reviews/2026-10-07/background-mixed-sector-and-amplified-checkpoint.json"
OUTPUT = ROOT / "reviews/2026-10-07/number-field-choice-checkpoint.json"
SOURCE = Path("E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex")
BASE = "502463775b1ba2a7d4aab65e1b55f3fbe775d7de"
MUTABLE = {"goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md"}
FILES = [
    "notes/457-number-field-choice-and-relative-amplification.md",
    "reviews/2026-10-07/hybrid-number-field-choice-review.md",
    "reviews/2026-10-07/hybrid-number-field-choice-review-root.md",
    "reviews/2026-10-07/hybrid-number-field-choice-review-twisted.md",
    "reviews/2026-10-07/hybrid-number-field-quantitative-review-radial.md",
    "reviews/2026-10-07/hybrid-gaussian-quartic-feasibility-research.md",
    "scripts/hybrid_number_field_exact_audit.py",
    "scripts/hybrid_number_field_checkpoint.py",
    "output/hybrid-number-field-exact-audit.json",
    "goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md",
]
DRAFTS = [
    "notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md",
    "output/hybrid-proper-power-exact-audit.json",
    "reviews/2026-10-07/hybrid-distinct-two-two-prime-sector-research.md",
    "reviews/2026-10-07/hybrid-one-three-mixed-prime-sector-research.md",
    "reviews/2026-10-07/hybrid-three-column-reflection-research.md",
    "reviews/2026-10-07/hybrid-whole-proper-power-review-twisted.md",
    "scripts/hybrid_proper_power_exact_audit.py",
]


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    path = ROOT / name
    binary = path.suffix.lower() == ".pdf"
    data = path.read_bytes() if binary else canonical(path)
    return {"path": name, "sha256" if binary else "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "bytes" if binary else "canonical_utf8_bytes": len(data)}


def verify_record(record):
    current = binding(record["path"])
    for key in ("sha256", "sha256_canonical_lf", "bytes", "canonical_utf8_bytes"):
        if key in record:
            assert record[key] == current[key], (record["path"], key)
    return current


def build():
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    records = previous["previous_frozen_files_verified"] + [
        r for r in previous["files"] if r["path"] not in MUTABLE
    ] + [previous["public_README_unchanged"], previous["AF_primary_PDF_preserved"]]
    frozen = [verify_record(record) for record in records]
    frozen.append(binding(str(PREVIOUS.relative_to(ROOT)).replace("\\", "/")))
    source = canonical(SOURCE)
    assert hashlib.sha256(source).hexdigest() == previous["source_preserved_read_only"]["sha256_canonical_lf"]
    assert subprocess.check_output(["git", "-C", str(SOURCE.parents[3]), "status", "--porcelain"], text=True).rstrip() == ""
    spec = importlib.util.spec_from_file_location("number_field_exact_audit", ROOT / FILES[6])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    evidence = module.certify()
    assert evidence == json.loads((ROOT / FILES[8]).read_text(encoding="utf-8"))
    links = 0
    for name in FILES:
        path = ROOT / name
        data = canonical(path).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", data), name
        if path.suffix == ".md" and name not in MUTABLE:
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", data):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                candidate = target.split("#", 1)[0]
                candidate = re.sub(r":\d+$", "", candidate)
                resolved = (path.parent / candidate).resolve()
                assert resolved == OUTPUT.resolve() or resolved.exists(), (name, target)
                links += 1
    return {
        "date": "2026-10-07", "base_repository_commit": BASE,
        "current_goal_turn": "progress", "goal_status": "active",
        "user_focus": "effect of Q(sqrt(-3)) and possible improvements from other auxiliary number fields",
        "new_zero_free_boundary": False, "new_proportion": False, "new_paper": False,
        "unchanged_strict_sigma": "11/12-e*/4 = 0.874957019420098946... under existing explicit cited R",
        "accepted_scope": [
            "source dependency analysis and single-shift quadratic-terminal criterion",
            "relative order-d amplification with raw-family hypotheses for every fixed c>0",
            "DDHL v5 phase correction, split/inert proof and odd-primary-squarefree Gaussian signal",
            "explicit finite rho=1 kernel, not a global reflection theorem",
            "ordinary CM conductor exponent 1/2-s and gamma/unit-count distinctions",
        ],
        "gaussian_squarefree_signal": "gamma1(c)^2 = mu(c) alpha(c), fixed DDHL additive convention and 2-mask",
        "conditional_e6_minus_e4_at_reference_ell": "approximately 0.010352262232; not a sigma change",
        "counterfactual_count": "at the original cutoff whole saving=0; additionally keeping old short contract and rebalancing gives ~0.002993619562, not a theorem for a new field",
        "unpaid": ["actual same-probe quartic completed reflection/core coefficients", "whole reciprocal Euler quotient, masks and prime powers", "raw/marked/plain scale and height-uniform moments", "all physical contour margins and whole-family continuation", "original mixed raw saving, full fourth norm and long-term Weil/RH goals"],
        "independent_full_reviews": [FILES[3], FILES[4]],
        "root_full_review": FILES[2], "finite_evidence": evidence,
        "source_preserved_read_only": {"path": str(SOURCE), "sha256_canonical_lf": hashlib.sha256(source).hexdigest(), "external_kernel_run": False},
        "previous_frozen_files_verified": frozen,
        "files": [binding(name) for name in FILES],
        "preexisting_uncommitted_drafts_not_in_this_commit": [binding(name) for name in DRAFTS],
        "format_verification": {"control_characters_checked": True, "new_local_links_checked": links},
    }


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(result['files'])} current files, {len(result['previous_frozen_files_verified'])} frozen artifacts, exact finite evidence and read-only source")

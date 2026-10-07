"""Bind the reviewed research checkpoint; --check reads without rewriting it."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy
import subprocess
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
BASE = "1a51f5767f217c3dc02cd97ff2233d25cd8dd186"
OUT = ROOT / "reviews/2026-10-07/background-mixed-sector-and-amplified-checkpoint.json"
PREVIOUS = ROOT / "reviews/2026-10-07/prime-sector-and-critical-mixed-checkpoint.json"
MUTABLE_INDEXES = {"goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md"}
FILES = [
    "notes/454-original-background-and-weighted-prime-mixed-traces.md",
    "reviews/2026-10-07/hybrid-amplified-mixed-column-research.md",
    "reviews/2026-10-07/hybrid-amplified-mixed-column-review-root.md",
    "reviews/2026-10-07/hybrid-low-high-mixed-four-word-research.md",
    "reviews/2026-10-07/hybrid-low-high-mixed-four-word-review-root.md",
    "reviews/2026-10-07/hybrid-original-background-review-radial.md",
    "reviews/2026-10-07/hybrid-original-background-review-twisted.md",
    "reviews/2026-10-07/hybrid-background-mixed-sector-and-amplified-next-proof-plan.md",
    "scripts/hybrid_background_exact_audit.py",
    "scripts/hybrid_background_checkpoint.py",
    "output/hybrid-background-exact-audit.json",
    "goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md",
]


def canonical(raw):
    return raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(path, binary=False):
    data = path.read_bytes()
    if not binary:
        data = canonical(data)
    return {"path": path.relative_to(ROOT).as_posix(),
            "sha256" if binary else "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "bytes" if binary else "canonical_utf8_bytes": len(data)}


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd).decode("utf-8").rstrip()


def build():
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT, check=True)
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    frozen = previous["preserved_previous_delivery"] + [
        item for item in previous["files"] if item["path"] not in MUTABLE_INDEXES
    ]
    for item in frozen:
        assert binding(ROOT/item["path"], "sha256" in item) == item, item["path"]
    readme_base = subprocess.check_output(["git", "show", f"{BASE}:README.md"], cwd=ROOT)
    assert canonical(readme_base) == canonical((ROOT/"README.md").read_bytes())
    source = Path(previous["imported_source"]["path"])
    assert hashlib.sha256(canonical(source.read_bytes())).hexdigest() == \
        previous["imported_source"]["sha256_canonical_lf"]
    source_root = Path("E:/codex-build/math")
    assert git("rev-parse", "HEAD", cwd=source_root) == previous["imported_source"]["commit"]
    assert not git("status", "--porcelain", cwd=source_root)
    af = previous["AF_primary_PDF"]
    af_raw = (ROOT/af["path"]).read_bytes()
    assert hashlib.sha256(af_raw).hexdigest() == af["sha256"] and len(af_raw) == af["bytes"]
    actual = json.loads((ROOT/"output/hybrid-background-exact-audit.json").read_text(encoding="utf-8"))
    expected = runpy.run_path(str(ROOT/"scripts/hybrid_background_exact_audit.py"))["certify"]()
    assert actual == expected
    local_links = 0
    for name in FILES:
        path = ROOT/name
        if path.suffix != ".md":
            continue
        document = path.read_text(encoding="utf-8")
        assert not any(ord(c) < 32 and c not in "\n\r\t" for c in document), name
        for target in re.findall(r"\]\(([^)\s]+)\)", document):
            if target.startswith(("https:", "http:", "mailto:", "#", "codex:", "app:")):
                continue
            relative = unquote(target.split("#", 1)[0])
            candidate = (path.parent/relative).resolve()
            assert candidate.exists() or candidate == OUT.resolve(), (name, target)
            local_links += 1
    changed = [line[3:] for line in git("status", "--porcelain").splitlines() if line]
    allowed = set(FILES) | {OUT.relative_to(ROOT).as_posix()}
    assert set(changed) <= allowed, sorted(set(changed)-allowed)
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    return {
        "date": "2026-10-07",
        "base_repository_commit": BASE,
        "previous_goal_turn": "progress",
        "current_goal_turn": "progress",
        "goal_status": "active",
        "boundary": {
            "new_boundary": False, "new_proportion": False, "new_paper": False,
            "unchanged_strict_sigma": "11/12-e*/4 = 0.874957019420098946...",
            "scope": "existing cubic paper's explicit cited R; no new whole-source/kernel certification",
        },
        "paid": {
            "original_background": {
                "scope": "original finite frame; complete sharp Lambda and full Gamma/pole heights",
                "limits": ["Tr A^4/N -> V", "Tr A^3 C/N -> 0",
                           "Tr A^2 C^2/N -> Z", "Tr ACAC/N -> Z-J/2"],
                "exact_whole_fourth": "F_T + 4Y_T + 6Z-J+V+o(1)",
                "C4_assumed_for_these_limits": False,
                "conditional_bridge": "if limsup F_T <= F < infinity: upper F+4sqrt(ZF)+6Z-J+V",
            },
            "repeated_22_mixed_union": {
                "scope": "actual finite compression; two high/two low with either label repeated",
                "limit": "4D_HL,psi+8J_HL,psi",
                "flat_D": "23/960", "flat_J": "1/640", "flat_limit": "13/120",
                "physical_to_finite_multiplication_bridge_explicitly_paid": True,
            },
            "amplified_whole_mixed_column": {
                "scope": "actual mu*1*1 with one original prime-slot product, rowwise profiles and natural zeros",
                "exact_transfer_and_near_scale_simultaneous_spikes": True,
                "strict_chi_paid": False,
                "reference_raw_toll_required": "gamma < 1/3",
                "current_raw_toll": "gamma = 1/3",
            },
        },
        "review_scope": {
            "background": "two independent full reviews: radial and twisted",
            "repeated_mixed": "root full review after multiplication-bridge repair; separate sign-path audit",
            "amplified": "root full review; exact transfer and specified continuous optimization only",
        },
        "finite_evidence": {
            "certify_object_equals_current_JSON": True,
            "cyclic_background_classes": 6, "mixed_label_models": 9,
            "profile_models": 2,
            "scope": "finite free-word coefficients and rational polynomial integrals only",
        },
        "unpaid": [
            "actual structured mixed raw gamma<1/3 / strict chi>0",
            "22 all-distinct, 13 and 31 actual mixed sectors",
            "high all-distinct and whole sharp-Lambda fourth F_T",
            "actual three-Lambda background covariance Y_T",
            "proper-power whole mixed transfer and complete proportion chain",
            "pooled four-Lambda curved-prefix discrepancy and whole-cell/alias arithmetic",
            "any further full-domain boundary proof, imported source wholechain/kernel verification",
            "original long-term Weil geometry, RR and full RH",
        ],
        "format_verification": {"local_links_checked": local_links, "control_characters_checked": True},
        "source_preserved_read_only": previous["imported_source"],
        "AF_primary_PDF_preserved": af,
        "public_README_unchanged": binding(ROOT/"README.md"),
        "previous_frozen_files_verified": frozen,
        "files": [binding(ROOT/name) for name in FILES],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.check:
        assert result == json.loads(OUT.read_text(encoding="utf-8"))
    else:
        OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": "PASS: bindings and finite evidence only",
                      "files_bound": len(result["files"]),
                      "frozen_files_verified": len(result["previous_frozen_files_verified"]),
                      "local_links_checked": result["format_verification"]["local_links_checked"],
                      "checkpoint": str(OUT), "read_only_check": args.check}, ensure_ascii=False))

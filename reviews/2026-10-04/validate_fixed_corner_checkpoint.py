"""Validate saved review bindings and exact audit for notes 424--426.

This is an artifact-integrity check, not an automated proof of Hilbert analysis.
The previous 422--423 checkpoint is preserved byte for byte.
"""
from pathlib import Path
from urllib.parse import unquote
import datetime
import hashlib
import json
import re
import subprocess
import sys


sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PREVIOUS_SHA = "cc32ff12a9ec70090af5dda497b3165c5add9efce934b5ceddb7bb88e4cbc3b2"
REVIEW_BINDINGS = {
    "notes/424-f1-relative-chain-repair-and-four-component-obstruction.md": [
        "f1-relative-chain-independent-review.md",
    ],
    "notes/425-f1-recentered-geometric-corner-and-source-period-finite-part.md": [
        "f1-geometric-corner-independent-review.md",
        "f1-geometric-corner-second-review.md",
    ],
    "notes/426-f1-fixed-corner-source-commutators-and-relative-readout-module.md": [
        "f1-source-readout-independent-review.md",
        "f1-source-readout-second-review.md",
        "f1-source-readout-chain-review.md",
    ],
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert sha(HERE/"f1-research-checkpoint-validation.json") == PREVIOUS_SHA
    old_sources = {
        "notes/422-f1-radial-finite-part-and-corner-anomaly.md":
            "c928b7c53a214ff193210f230d9c2f474ccd90da8ca2e23f88c34ce190114647",
        "notes/423-f1-twisted-radial-readout-and-mixed-period-obstruction.md":
            "07592e3a7192b78db338e02c27a43a1996b9ae754935b8d1e8ce367487fb6add",
    }
    for source, expected in old_sources.items():
        assert sha(ROOT/source) == expected, source
    reviews = []
    for source, names in REVIEW_BINDINGS.items():
        digest = sha(ROOT/source)
        for name in names:
            contents = (HERE/name).read_text(encoding="utf-8")
            assert digest in contents, (source, name, "missing final source hash")
            assert "PASS" in contents, name
            reviews.append(name)
    audit_path = HERE/"f1-corner-recenter-exact-audit.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    assert audit["status"] == "passed_exact_fraction_checks"
    assert audit["total_exact_assertions"] == sum(audit["checks"].values()) == 16261
    assert sha(ROOT/"scripts/corner_recenter_exact_audit.py") == audit["script_sha256"]
    assert audit["checks"]["H_negative_wave_exact_ball_tail"] == 12
    assert audit["checks"]["minimal_H_reducing_hull_rank"] == 12
    lean_path = ROOT/"formal/checks/twisted-radial-witness-verification.json"
    lean = json.loads(lean_path.read_text(encoding="utf-8"))
    assert lean["status"] == "passed_no_sorry_dependencies"
    for source, expected in lean["source_sha256"].items():
        assert sha(ROOT/"formal"/source) == expected, source
    assert all("sorryAx" not in axioms for axioms in lean["axioms"].values())
    admissions = []
    for source in sorted((ROOT/"formal/F1").rglob("*.lean")):
        for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            if re.fullmatch(r"\s*sorry\s*", line):
                admissions.append({"source": source.relative_to(ROOT).as_posix(), "line": number})
    assert len(admissions) == 10
    goal = "goals/GOAL.20260909.md"
    old_goal = subprocess.check_output(["git", "show", "HEAD:"+goal], cwd=ROOT)
    assert sha(ROOT/goal) == hashlib.sha256(old_goal).hexdigest()
    changed = subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True).splitlines()
    untracked = subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT, text=True).splitlines()
    names = sorted(set(changed+untracked))
    errors, links = [], 0
    for name in names:
        path = ROOT/name
        if path.suffix != ".md":
            continue
        document = path.read_text(encoding="utf-8")
        document = re.sub(r"```[\s\S]*?```|`[^`\n]*`", "", document)
        for target in re.findall(r"(?<!\\)\[[^\[\]\r\n]+(?<!\\)\]\(([^\s)]+)\)", document):
            if "://" in target or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            if not (path.parent/target).exists():
                errors.append(f"{name}: missing {target}")
            links += 1
    assert not errors, errors
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "scripts/check_repo_layout.py"], cwd=ROOT, check=True)
    result = {
        "status": "passed_fixed_corner_scoped_checkpoint",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "base_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "previous_checkpoint_preserved_sha256": PREVIOUS_SHA,
        "previous_notes_unchanged_sha256": old_sources,
        "long_term_goal_unchanged": True,
        "independent_review_bindings": REVIEW_BINDINGS,
        "local_links_checked": links,
        "exact_fraction_assertions": audit["total_exact_assertions"],
        "new_lean_results": 0,
        "previous_four_lean_results_sources_unchanged": True,
        "old_admissions": admissions,
        "full_F1_build": False,
        "scope": (
            "424 continuous scalar obstruction and relative-chain identities; "
            "425 source-specific fixed corner, trace-class physical cutoffs, exact period comparison "
            "and alternative-cutoff obstruction; 426 trace-class source commutators, linear readout "
            "bimodule and explicit nonuniqueness. Infinite Hilbert analysis is independently reviewed, "
            "not machine formalized. The exact rational models do not certify actual prime parameters, "
            "full relative Chern/principal comparison, Weil positivity, RR or RH."
        ),
        "source_sha256": {
            name: sha(ROOT/name) for name in names
            if (ROOT/name).is_file()
            and name != "reviews/2026-10-04/f1-fixed-corner-checkpoint-validation.json"
        },
    }
    (HERE/"f1-fixed-corner-checkpoint-validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in {"source_sha256", "old_admissions", "independent_review_bindings"}},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()

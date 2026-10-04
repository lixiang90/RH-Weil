"""Check 427--429 review bindings, exact integrals, and protected checkpoint.

This verifies saved evidence, not the infinite-dimensional proofs themselves.
Canonical text hashes normalize Windows line endings for Git checkout use.
The earlier mathematical sources and reports are not rewritten.
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
BASE = "9d0cb1a356d79c93f28931362e303158ea7e8214"
REVIEW_BINDINGS = {
    "notes/427-f1-corner-product-algebra-and-unavoidable-trace-cocycle.md": [
        "f1-corner-product-independent-review.md", "f1-corner-cocycle-chain-review.md",
    ],
    "notes/428-f1-corner-essential-symbol-and-complete-readout-freedom.md": [
        "f1-corner-symbol-independent-review.md", "f1-corner-symbol-second-review.md",
    ],
    "notes/429-f1-original-unitary-crosses-the-fixed-corner-domain.md": [
        "f1-original-unitary-independent-review.md", "f1-original-unitary-second-review.md",
        "f1-original-unitary-source-review.md",
    ],
}


def canonical(data):
    return data.replace(b"\r\n", b"\n")


def sha(path):
    return hashlib.sha256(canonical(path.read_bytes())).hexdigest()


def git_blob(name):
    return canonical(subprocess.check_output(["git", "show", BASE+":"+name], cwd=ROOT))


def main():
    protected = ["goals/GOAL.20260909.md",
                 "reviews/2026-10-04/f1-research-checkpoint-validation.json",
                 "reviews/2026-10-04/f1-fixed-corner-checkpoint-validation.json",
                 "reviews/2026-10-04/f1-corner-recenter-exact-audit.json",
                 "scripts/corner_recenter_exact_audit.py",
                 "formal/F1/Analysis/TwistedRadialWitness.lean"]
    previous = json.loads((HERE/"f1-fixed-corner-checkpoint-validation.json").read_text(encoding="utf-8"))
    protected += list(previous["independent_review_bindings"])
    protected += ["notes/422-f1-radial-finite-part-and-corner-anomaly.md",
                  "notes/423-f1-twisted-radial-readout-and-mixed-period-obstruction.md"]
    for reviews in previous["independent_review_bindings"].values():
        protected += ["reviews/2026-10-04/"+name for name in reviews]
    for name in protected:
        assert canonical((ROOT/name).read_bytes()) == git_blob(name), (name, "protected source changed")
    for source, reviews in REVIEW_BINDINGS.items():
        digest = sha(ROOT/source)
        for name in reviews:
            report = (HERE/name).read_text(encoding="utf-8")
            assert digest in report, (source, name, "final hash binding missing")
            assert "PASS" in report, name
    audit = json.loads((HERE/"f1-corner-commutator-moment-audit.json").read_text(encoding="utf-8"))
    assert audit["status"] == "passed_exact_fraction_polynomial_integrals"
    assert audit["total_exact_assertions"] == sum(audit["checks"].values()) == 207
    assert audit["checks"]["frame_translation_moment_exact"] == 166
    assert audit["compact_polynomial_tests"]["commutator_coefficient_minus_4_moment"] == "-8192/45045"
    assert sha(ROOT/"scripts/corner_commutator_moment_audit.py") == audit["script_sha256"]
    lean = json.loads((ROOT/"formal/checks/twisted-radial-witness-verification.json").read_text(encoding="utf-8"))
    assert lean["status"] == "passed_no_sorry_dependencies"
    for name, expected in lean["source_sha256"].items():
        assert sha(ROOT/"formal"/name) == expected, name
    assert all("sorryAx" not in axioms for axioms in lean["axioms"].values())
    admissions = []
    for source in sorted((ROOT/"formal/F1").rglob("*.lean")):
        for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            if re.fullmatch(r"\s*sorry\s*", line):
                admissions.append({"source": source.relative_to(ROOT).as_posix(), "line": number})
    assert len(admissions) == 10
    changed = subprocess.check_output(["git", "diff", BASE, "--name-only"], cwd=ROOT, text=True).splitlines()
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
    subprocess.run(["git", "diff", BASE, "--check"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "scripts/check_repo_layout.py"], cwd=ROOT, check=True)
    result = {
        "status": "passed_corner_algebra_scoped_checkpoint",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "base_commit": BASE,
        "canonical_text_hashes": "SHA256 after CRLF to LF normalization",
        "protected_previous_sources": {name: sha(ROOT/name) for name in protected},
        "long_term_goal_unchanged": True,
        "independent_review_bindings": REVIEW_BINDINGS,
        "local_links_checked": links,
        "exact_polynomial_assertions": audit["total_exact_assertions"],
        "new_lean_results": 0,
        "previous_lean_sources_unchanged": True,
        "old_admissions": admissions,
        "full_F1_build": False,
        "scope": (
            "427 actual product algebra, nonzero trace-class commutator, quotient cyclic 1-cocycle "
            "and cutoff flux; 428 essential norm, C*-symbol quotient, all LF readout distributions "
            "and operator-quotient discontinuity; 429 actual original unitary's noncompact "
            "off-corner rows and failure of domain/multiplier/normalizer admission. "
            "Infinite analysis independently reviewed, not machine formalized. Exact rational "
            "polynomial models are not the smooth Haar-prime frame. No full relative Chern, "
            "canonical arithmetic principal relation, full Weil positivity, RR or RH result."
        ),
        "source_sha256": {name: sha(ROOT/name) for name in names
                          if (ROOT/name).is_file()
                          and name != "reviews/2026-10-04/f1-corner-algebra-checkpoint-validation.json"},
    }
    (HERE/"f1-corner-algebra-checkpoint-validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in {"source_sha256", "old_admissions", "independent_review_bindings",
                                   "protected_previous_sources"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()

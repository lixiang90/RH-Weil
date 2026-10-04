"""Validate saved evidence for the scoped 430--433 research checkpoint.

This binds independently reviewed analytic notes and the finite rational model.
It does not formalize infinite operators, HH1, arithmetic transfer, or RH.
Prior checkpoint sources and reports are preserved without rewriting them.
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
BASE = "c013a4cb2d5981b7868aa2bbefb8d448c93b8709"
OUTPUT = "reviews/2026-10-04/f1-source-domain-checkpoint-validation.json"
MUTABLE_INDEXES = {"README.md", "RESEARCH_BRANCHES.md", "goals/NEXT.20260909.md", "goals/PROGRESS.md"}
BINDINGS = {
    "notes/430-f1-source-stable-periodic-smoothing-algebra.md": [
        "f1-source-stable-algebra-independent-review.md",
        "f1-source-orbit-symbol-independent-review.md",
    ],
    "notes/431-f1-source-orbit-essential-symbol-and-boundary-injectivity.md": [
        "f1-source-orbit-symbol-independent-review.md",
        "f1-source-stable-algebra-independent-review.md",
    ],
    "notes/432-f1-relative-cycle-charge-and-source-invariant-cutoff.md": [
        "f1-source-relative-charge-independent-review.md",
        "f1-source-stable-algebra-independent-review.md",
    ],
    "notes/433-f1-source-cesaro-limit-and-noncompact-fixed-sector.md": [
        "f1-source-cesaro-independent-review.md", "f1-source-cesaro-second-review.md",
    ],
}


def canonical(data):
    return data.replace(b"\r\n", b"\n")


def sha(path):
    return hashlib.sha256(canonical(path.read_bytes())).hexdigest()


def git_output(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).splitlines()


def main():
    previous_name = "reviews/2026-10-04/f1-corner-algebra-checkpoint-validation.json"
    previous = json.loads((ROOT/previous_name).read_text(encoding="utf-8"))
    protected = {"goals/GOAL.20260909.md", previous_name,
                 "reviews/2026-10-04/validate_corner_algebra_checkpoint.py"}
    protected.update(previous["protected_previous_sources"])
    protected.update(set(previous["source_sha256"]) - MUTABLE_INDEXES)
    for name in sorted(protected):
        old = subprocess.check_output(["git", "show", BASE+":"+name], cwd=ROOT)
        assert canonical((ROOT/name).read_bytes()) == canonical(old), (name, "old checkpoint changed")
    changed = git_output("diff", BASE, "--name-only")
    tracked_before = set(git_output("ls-tree", "-r", "--name-only", BASE))
    assert not (set(changed) & tracked_before) - MUTABLE_INDEXES, "unapproved old source edit"
    for source, reports in BINDINGS.items():
        digest = sha(ROOT/source)
        for report in reports:
            document = (HERE/report).read_text(encoding="utf-8")
            assert digest in document and "PASS" in document, (source, report, "binding or PASS missing")
    audit = json.loads((HERE/"f1-source-orbit-gram-exact-audit.json").read_text(encoding="utf-8"))
    assert audit["status"] == "passed_exact_finite_source_fibre_models"
    assert audit["total_exact_assertions"] == sum(audit["checks"].values()) == 12664
    assert audit["checks"]["full_mixed_gram_formula"] == 1908
    assert audit["checks"]["finite_gram_identity_lower_bound"] == 36
    assert audit["script_sha256"] == sha(ROOT/"scripts/source_orbit_gram_exact_audit.py")
    admissions = []
    for source in sorted((ROOT/"formal/F1").rglob("*.lean")):
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            if re.fullmatch(r"\s*sorry\s*", line):
                admissions.append({"source": source.relative_to(ROOT).as_posix(), "line": line_number})
    assert admissions == previous["old_admissions"], "Lean admissions changed"
    lean = json.loads((ROOT/"formal/checks/twisted-radial-witness-verification.json").read_text(encoding="utf-8"))
    for source, digest in lean["source_sha256"].items():
        assert sha(ROOT/"formal"/source) == digest, source
    assert all("sorryAx" not in axioms for axioms in lean["axioms"].values())
    untracked = git_output("ls-files", "--others", "--exclude-standard")
    names = sorted(set(changed + untracked))
    links, errors = 0, []
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
        "status": "passed_source_domain_scoped_checkpoint",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "base_commit": BASE,
        "canonical_text_hashes": "SHA256 after CRLF to LF normalization",
        "protected_previous_sources": {name: sha(ROOT/name) for name in sorted(protected)},
        "long_term_goal_unchanged": True,
        "independent_review_bindings": BINDINGS,
        "local_links_checked": links,
        "exact_finite_fibre_assertions": 12664,
        "new_lean_results": 0,
        "previous_lean_sources_unchanged": True,
        "old_admissions": admissions,
        "full_F1_build": False,
        "scope": (
            "430 actual source-stable periodic smoothing algebra with exact mixed Gram and trace-class errors; "
            "431 finite-source essential norm and symbol, finite-boundary injectivity, single-corner Floquet quotient "
            "and minimal source quotient noncommutativity; 432 canonical algebraic HH1 cycle charge and per-cutoff "
            "source-invariant trace/readout mismatch; 433 norm Cesaro limit, rate, and noncompact fixed source sector "
            "forced for p<q. Infinite analysis independently reviewed, not Lean formalized. Rational audits use "
            "integer-period pointwise fibre models, not the smooth log-prime frame. No full source quotient classification, "
            "canonical arithmetic cutoff transfer, full relative Chern, principal relation, Weil positivity, RR or RH result."
        ),
        "source_sha256": {name: sha(ROOT/name) for name in names if (ROOT/name).is_file() and name != OUTPUT},
    }
    (ROOT/OUTPUT).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in {
        "protected_previous_sources", "independent_review_bindings", "source_sha256", "old_admissions"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()

"""Validate evidence for the scoped 434--437 physical-source checkpoint.

This preserves prior saved research and binds two reviews per analytic note.
The rational discrete audit does not formalize infinite operators or RH.
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
BASE = "9d6815f89144b2a87cfaf5c201212096ec956028"
OUTPUT = "reviews/2026-10-06/f1-physical-source-checkpoint-validation.json"
MUTABLE_INDEXES = {"README.md", "RESEARCH_BRANCHES.md", "goals/NEXT.20260909.md", "goals/PROGRESS.md"}
BINDINGS = {
    "notes/434-f1-haar-physical-cutoff-on-the-source-domain.md": [
        "f1-434-435-independent-review.md", "f1-434-436-437-independent-review.md"],
    "notes/435-f1-haar-trace-of-all-source-conjugates.md": [
        "f1-434-435-independent-review.md", "f1-435-437-independent-review.md"],
    "notes/436-f1-physical-cutoff-of-the-source-cesaro-limit.md": [
        "f1-435-437-independent-review.md", "f1-434-436-437-independent-review.md"],
    "notes/437-f1-finite-source-word-without-a-linear-physical-finite-part.md": [
        "f1-434-436-437-independent-review.md", "f1-435-437-independent-review.md"],
}


def canonical(data):
    return data.replace(b"\r\n", b"\n")


def sha(path):
    return hashlib.sha256(canonical(path.read_bytes())).hexdigest()


def git_lines(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).splitlines()


def main():
    previous_name = "reviews/2026-10-04/f1-source-domain-checkpoint-validation.json"
    previous = json.loads((ROOT/previous_name).read_text(encoding="utf-8"))
    protected = {"goals/GOAL.20260909.md", previous_name,
                 "reviews/2026-10-04/validate_source_domain_checkpoint.py"}
    protected.update(previous["protected_previous_sources"])
    protected.update(set(previous["source_sha256"]) - MUTABLE_INDEXES)
    for name in sorted(protected):
        original = subprocess.check_output(["git", "show", BASE+":"+name], cwd=ROOT)
        assert canonical((ROOT/name).read_bytes()) == canonical(original), (name, "prior checkpoint changed")
    changed = git_lines("diff", BASE, "--name-only")
    tracked_before = set(git_lines("ls-tree", "-r", "--name-only", BASE))
    assert not (set(changed) & tracked_before)-MUTABLE_INDEXES, "old non-index edit"
    for source, reports in BINDINGS.items():
        digest = sha(ROOT/source)
        for report in reports:
            content = (HERE/report).read_text(encoding="utf-8")
            assert digest in content and "PASS" in content, (source, report, "review binding missing")
    audit = json.loads((HERE/"f1-physical-source-trace-exact-audit.json").read_text(encoding="utf-8"))
    assert audit["status"] == "passed_exact_discrete_physical_source_trace_models"
    assert audit["total_exact_assertions"] == sum(audit["checks"].values()) == 3711
    assert audit["checks"]["full_visible_source_energy_and_signed_unit_flux"] == 42
    assert audit["checks"]["full_physical_conjugate_trace_model"] == 252
    assert audit["checks"]["actual_deep_q_strip_row"] == 3276
    assert audit["script_sha256"] == sha(ROOT/"scripts/physical_source_trace_exact_audit.py")
    assert audit["dependency_sha256"] == sha(ROOT/"scripts/source_orbit_gram_exact_audit.py")
    audit_review = (HERE/"f1-physical-source-exact-audit-review.md").read_text(encoding="utf-8")
    assert audit["script_sha256"] in audit_review and "PASS" in audit_review
    admissions = []
    for path in sorted((ROOT/"formal/F1").rglob("*.lean")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if re.fullmatch(r"\s*sorry\s*", line):
                admissions.append({"source": path.relative_to(ROOT).as_posix(), "line": line_number})
    assert admissions == previous["old_admissions"], "Lean admissions changed"
    lean = json.loads((ROOT/"formal/checks/twisted-radial-witness-verification.json").read_text(encoding="utf-8"))
    for source, digest in lean["source_sha256"].items():
        assert sha(ROOT/"formal"/source) == digest, source
    assert all("sorryAx" not in value for value in lean["axioms"].values())
    untracked = git_lines("ls-files", "--others", "--exclude-standard")
    names = sorted(set(changed+untracked))
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
        "status": "passed_physical_source_scoped_checkpoint",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "base_commit": BASE,
        "canonical_text_hashes": "SHA256 after CRLF to LF normalization",
        "protected_previous_sources": {name: sha(ROOT/name) for name in sorted(protected)},
        "long_term_goal_unchanged": True,
        "independent_review_bindings": BINDINGS,
        "local_links_checked": links,
        "exact_discrete_model_assertions": 3711,
        "new_lean_results": 0,
        "previous_lean_sources_unchanged": True,
        "old_admissions": admissions,
        "full_F1_build": False,
        "scope": (
            "434 all finite-source periodic smoothing kernels are trace class at each original Haar physical cutoff; "
            "435 all fixed integer conjugates have exact original nonzero prime periods and signed unit flux; "
            "436 actual completed source mean physical trace, fixed-cutoff trace-norm convergence, and noncommuting "
            "iterated trace limits; 437 a legal p=2 q=5 original finite word has no cofinal linear-volume physical "
            "finite part, including the original even geometric cutoff family. Infinite analysis independently "
            "reviewed twice per note, not Lean formalized. Discrete rational matrix/tail audits are separate models. "
            "No full source quotient classification, canonical phase transfer, full relative Chern, arithmetic "
            "principal relation, all-place Weil positivity, RR or RH result."
        ),
        "source_sha256": {name: sha(ROOT/name) for name in names if (ROOT/name).is_file() and name != OUTPUT},
    }
    (ROOT/OUTPUT).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in {
        "protected_previous_sources", "independent_review_bindings", "source_sha256", "old_admissions"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()

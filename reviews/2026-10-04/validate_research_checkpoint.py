"""Bind the scoped research checkpoint to checked sources and local links."""
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


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    tracked = subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True).splitlines()
    new = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT, text=True).splitlines()
    files = sorted(set(tracked+new))
    links = 0
    errors = []
    for name in files:
        path = ROOT/name
        if path.suffix != ".md":
            continue
        document = path.read_text(encoding="utf-8")
        document = re.sub(r"```[\s\S]*?```|`[^`\n]*`", "", document)
        # Mathematical \](m) is not a Markdown link; require a real label.
        for target in re.findall(r"(?<!\\)\[[^\[\]\r\n]+(?<!\\)\]\(([^\s)]+)\)", document):
            if "://" in target or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            if not (path.parent/target).exists():
                errors.append(f"{name}: missing {target}")
            links += 1
    assert not errors, errors
    lean_report = json.loads((ROOT/"formal/checks/twisted-radial-witness-verification.json").read_text(encoding="utf-8"))
    assert lean_report["status"] == "passed_no_sorry_dependencies"
    assert len(lean_report["axioms"]) == 4
    for source, expected in lean_report["source_sha256"].items():
        assert sha(ROOT/"formal"/source) == expected, source
    assert all("sorryAx" not in axioms for axioms in lean_report["axioms"].values())
    audit = json.loads((HERE/"f1-twisted-radial-witness-audit.json").read_text(encoding="utf-8"))
    assert audit["status"] == "passed_exact_integer_checks"
    assert sha(ROOT/"scripts/twisted_radial_witness_audit.py") == audit["script_sha256"]
    admissions = []
    for source in sorted((ROOT/"formal/F1").rglob("*.lean")):
        for line, text in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            if re.fullmatch(r"\s*sorry\s*", text):
                admissions.append({"source": source.relative_to(ROOT).as_posix(), "line": line})
    assert len(admissions) == 10
    goal_path = "goals/GOAL.20260909.md"
    old_goal = subprocess.check_output(["git", "show", "HEAD:"+goal_path], cwd=ROOT)
    assert sha(ROOT/goal_path) == hashlib.sha256(old_goal).hexdigest()
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    for report_name, note_name in [
        ("f1-radial-finite-part-independent-review.md", "422-f1-radial-finite-part-and-corner-anomaly.md"),
        ("f1-twisted-radial-independent-review.md", "423-f1-twisted-radial-readout-and-mixed-period-obstruction.md"),
    ]:
        text = (HERE/report_name).read_text(encoding="utf-8")
        expected = sha(ROOT/"notes"/note_name)
        assert expected in text, (report_name, "final note hash not bound")
        assert "PASS" in text
    result = {
        "status": "passed_scoped_research_checkpoint",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "base_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "local_links_checked": links,
        "lean_new_results": 4,
        "lean_no_sorry_dependencies": True,
        "old_admissions": admissions,
        "long_term_goal_unchanged": True,
        "exact_lattice_counts": {k: v for k, v in audit.items() if k.endswith("checks") or k == "finite_grid_witnesses"},
        "full_F1_build": False,
        "scope": "422 and corrected 423 independently reviewed in their stated domains; exact lattice bookkeeping and four core Lean witness theorems. No full analytic formalization, global principal relation, G0-G8 existence, RR, RH or zero proportion result.",
        "source_sha256": {name: sha(ROOT/name) for name in files if (ROOT/name).is_file() and name != "reviews/2026-10-04/f1-research-checkpoint-validation.json"},
    }
    (HERE/"f1-research-checkpoint-validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in {"source_sha256", "old_admissions"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()

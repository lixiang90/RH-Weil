"""Bind this research round to saved source bytes; not a mathematical proof checker."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--git-index", action="store_true")
args = parser.parse_args()
digest = lambda raw: hashlib.sha256(raw).hexdigest()
sha = lambda p: digest(p.read_bytes())
notes = [next(ROOT.glob(f"notes/{n}-*.md")).relative_to(ROOT).as_posix() for n in range(369, 373)]
review_names = [
    "f1-hp-unit-independent-review.md", "f1-finite-level-rigidity-independent-review.md",
    "f1-tate-weight-independent-review.md", "f1-2026-period-ring-source-audit.md",
    "f1-lurie-geometric-binding-source-audit.md", "f1-jessen-normalization-source-audit.md",
    "f1-period-ring-independent-review.md",
]
reviews = ["reviews/2026-09-10/" + name for name in review_names]
docs = notes + reviews + ["README.md", "RESEARCH_BRANCHES.md", "goals/GOAL.20260909.md",
    "goals/NEXT.20260909.md", "goals/PROGRESS.md", "literature/README.md"]
links = 0
for relative in docs:
    path = ROOT / relative
    raw = path.read_bytes()
    assert not re.search(rb"[\x00-\x08\x0b\x0c\x0e-\x1f]|\r(?!\n)", raw), relative
    text = raw.decode("utf-8")
    assert "\ufffd" not in text and text.count("```") % 2 == 0, relative
    prose = re.sub(r"```[\s\S]*?```", "", text)
    prose = re.sub(r"`[^`\n]*`", "", prose)
    for match in re.finditer(r"\[[^\]\n]+\]\(([^\s)]+)\)", prose):
        target = match[1].split("#", 1)[0]
        if target and "://" not in target:
            assert (path.parent / target).exists(), (relative, target)
            links += 1

old = ROOT.parent / "archive/GOAL.20260906.md"
assert sha(old) == "213a099265b8a88d5eb5ef6a9f0d5af0d595a8e52c6d1cb0e0f658929366e568"
prior = ROOT.parent / "archive/GOAL.20260909.f1-periodic.md"
assert sha(prior) == "d3e4bfecdfd18507cbe92e0579ce6f6c44d7fd83211a0914fc80167e7abbafd5"
boundary = "### B. 较远期目标方向".encode()
assert prior.read_bytes().split(boundary, 1)[1] == (ROOT.parent / "GOAL.20260909.md").read_bytes().split(boundary, 1)[1]
goals = json.loads((ROOT / "goals/manifest.json").read_bytes())
assert len(goals) == 18
for entry in goals:
    assert sha(ROOT.parent / entry["workspace_path"]) == entry["source_sha256"]
    assert sha(ROOT / entry["repository_path"]) == entry["mirror_sha256"]

audit = json.loads((ROOT / "formal/checks/source-audit.json").read_bytes())
for relative, expected in audit["own_source_sha256"].items():
    assert sha(ROOT / "formal" / relative) == expected, relative
assert sha(ROOT / "reviews/2026-09-10/frozen-control-closure.json") == "39f10f8bcb3d68012f74dac7839ebb9d6afad1892428366b11b5236103f5f875"
library = json.loads((ROOT / "literature/manifest.json").read_bytes())
source_names = {"f1/cc-complex-lift-1805.10501v1.pdf", "f1/cc-scaling-site-1603.03191v1.pdf",
    "f1/cc-absolute-geometry-2606.06604v1.pdf"} | {f"f1/lurie-2018-lecture{n:02d}.pdf" for n in (6, 8, 11, 19)}
sources = [e for e in library["entries"] if e.get("file") in source_names]
assert len(sources) == 7
for e in sources:
    assert sha(ROOT / "literature" / e["file"]) == e["sha256"]
jt = next(e for e in library["entries"] if e["id"] == "Jessen-Tornehave-1945")
assert jt["download_status"] == "failed" and not jt.get("file") and not jt.get("sha256")

indexed = 0
if args.git_index:
    for relative in docs + [e["repository_path"] for e in goals]:
        raw = (ROOT / relative).read_bytes()
        staged = subprocess.check_output(["git", "show", ":" + relative], cwd=ROOT)
        if relative.startswith("goals/") and "/GOAL." in relative:
            assert raw == staged, relative
        else:
            assert raw.replace(b"\r\n", b"\n") == staged.replace(b"\r\n", b"\n"), relative
        indexed += 1
    for e in sources:
        staged = subprocess.check_output(["git", "show", ":literature/" + e["file"]], cwd=ROOT)
        assert digest(staged) == e["sha256"]
        indexed += 1

report = {
    "status": "PASS_SAVED_PERIOD_RING_BATCH", "checked_document_links": links,
    "unchanged_lean_sources": len(audit["own_source_sha256"]), "goal_mirrors": len(goals),
    "long_term_goal_bytes_unchanged": True, "legacy_scan_unchanged": True,
    "exhaustive_edges_repeated": 0, "git_index_checked_blobs": indexed,
    "document_sha256_raw": {p: sha(ROOT / p) for p in docs},
    "document_sha256_lf": {p: digest((ROOT / p).read_bytes().replace(b"\r\n", b"\n")) for p in docs},
    "sources": [{k: e[k] for k in ("file", "sha256", "pages")} for e in sources],
    "unreviewed_drafts": [p for p in notes if "尚未经独立复核" in (ROOT / p).read_text(encoding="utf-8")],
    "scope": "Saved files, links and source identities. Internal mathematics/source reviews remain separately scoped; no RH or complete RR certification."
}
Path(__file__).with_name("f1-period-ring-batch-validation.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({k: report[k] for k in ("status", "checked_document_links", "goal_mirrors", "git_index_checked_blobs", "unreviewed_drafts")}))

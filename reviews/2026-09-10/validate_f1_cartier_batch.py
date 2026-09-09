"""Validate saved F1 research/source identities, not the mathematical theorems."""
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
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

notes = [
    "notes/366-f1-character-family-principal-divisors.md",
    "notes/367-f1-periodic-cartier-sections.md",
    "notes/368-f1-tropical-theta-and-coefficient-obstruction.md",
    "notes/369-f1-hp-solenoid-unit-slope.md",
]
reviews = [
    "reviews/2026-09-10/f1-character-principal-independent-review.md",
    "reviews/2026-09-10/f1-classical-orbit-source-audit.md",
    "reviews/2026-09-10/f1-periodic-cartier-independent-review.md",
    "reviews/2026-09-10/f1-tropical-coefficient-independent-review.md",
    "reviews/2026-09-10/f1-hp-next-proof-plan.md",
]
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

archive = ROOT.parent / "archive/GOAL.20260906.md"
assert sha(archive) == "213a099265b8a88d5eb5ef6a9f0d5af0d595a8e52c6d1cb0e0f658929366e568"
audit = json.loads((ROOT / "formal/checks/source-audit.json").read_bytes())
for relative, expected in audit["own_source_sha256"].items():
    assert sha(ROOT / "formal" / relative) == expected, relative
frozen = ROOT / "reviews/2026-09-10/frozen-control-closure.json"
assert sha(frozen) == "39f10f8bcb3d68012f74dac7839ebb9d6afad1892428366b11b5236103f5f875"
manifest = json.loads((ROOT / "literature/manifest.json").read_bytes())
source_files = {
    "f1/cc-complex-lift-1805.10501v1.pdf",
    "f1/cc-scaling-site-1603.03191v1.pdf",
    "background/stacks-divisors-ed88ff78-20260714.pdf",
}
sources = [e for e in manifest["entries"] if e.get("file") in source_files]
assert len(sources) == 3
for entry in sources:
    assert sha(ROOT / "literature" / entry["file"]) == entry["sha256"]

indexed = 0
if args.git_index:
    # New proof notes use canonical LF. Existing living documentation may use CRLF;
    # its staged identity is separately normalized for prose only, not raw evidence.
    for relative in docs:
        actual = (ROOT / relative).read_bytes()
        staged = subprocess.check_output(["git", "show", ":" + relative], cwd=ROOT)
        if relative.startswith("goals/GOAL."):
            assert staged == actual, relative
        else:
            assert staged.replace(b"\r\n", b"\n") == actual.replace(b"\r\n", b"\n"), relative
        indexed += 1
    for entry in sources:
        relative = "literature/" + entry["file"]
        staged = subprocess.check_output(["git", "show", ":" + relative], cwd=ROOT)
        assert hashlib.sha256(staged).hexdigest() == entry["sha256"], relative
        indexed += 1

report = {
    "status": "PASS_SAVED_F1_CARTIER_BATCH", "checked_document_links": links,
    "unchanged_lean_sources": len(audit["own_source_sha256"]),
    "original_goal_archive_unchanged": True, "legacy_scan_unchanged": True,
    "exhaustive_edges_repeated": 0, "git_index_checked_blobs": indexed,
    "document_sha256_raw": {p: sha(ROOT / p) for p in docs},
    "document_sha256_lf": {p: hashlib.sha256((ROOT / p).read_bytes().replace(b"\r\n", b"\n")).hexdigest() for p in docs},
    "sources": [{k: e[k] for k in ("file", "sha256", "pages")} for e in sources],
    "scope": "File/link/source preservation only. Mathematical internal review is recorded separately; no RH or global RR certification.",
    "unreviewed_drafts": ["notes/369-f1-hp-solenoid-unit-slope.md"],
}
Path(__file__).with_name("f1-cartier-batch-validation.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({k: report[k] for k in ("status", "checked_document_links", "unchanged_lean_sources", "git_index_checked_blobs")}))

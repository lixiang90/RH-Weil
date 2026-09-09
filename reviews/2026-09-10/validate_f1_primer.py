"""Validate the primer's document bytes, local links and unchanged Lean source boundary.

This is not a mathematical proof checker or a LaTeX renderer.
Run with ordinary Python 3.10+ from any working directory.
"""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs/f1-route-from-undergraduate-math.md"
SPEC = ROOT / "formal/blueprint/geometric-realization.md"
REVIEWED = "cdb34dc92a4cc9015b26037374dc1090e1e2b89411a87c4abb6a95f718a18b64"

raw = DOC.read_bytes()
assert hashlib.sha256(raw).hexdigest() == REVIEWED, "Primer differs from reviewed bytes"
link_count = 0
display_math_count = 0
for path in (DOC, SPEC):
    data = path.read_bytes()
    assert not re.search(rb"[\x00-\x08\x0b\x0c\x0e-\x1f]|\r(?!\n)", data), path
    text = data.decode("utf-8")
    assert text.count("```") % 2 == 0, path
    assert text.count(r"\[") == text.count(r"\]"), path
    for match in re.finditer(r"\[[^\]\n]+\]\(([^\s)]+)\)", text):
        target = match.group(1)
        if "://" in target or target.startswith("#"):
            continue
        assert (path.parent / unquote(target.split("#", 1)[0])).is_file(), (path, target)
        link_count += 1
    for formula in re.findall(r"\\\[([\s\S]*?)\\\]", text):
        depth = 0
        for brace in re.findall(r"(?<!\\)[{}]", formula):
            depth += 1 if brace == "{" else -1
            assert depth >= 0, (path, formula)
        assert depth == 0, (path, formula)
        begins = re.findall(r"\\begin\{([^}]+)\}", formula)
        ends = re.findall(r"\\end\{([^}]+)\}", formula)
        assert sorted(begins) == sorted(ends), (path, formula)
        display_math_count += 1

audit = json.loads((ROOT / "formal/checks/source-audit.json").read_text(encoding="utf-8"))
for name, digest in audit["own_source_sha256"].items():
    assert hashlib.sha256((ROOT / "formal" / name).read_bytes()).hexdigest() == digest, name

library = json.loads((ROOT / "literature/manifest.json").read_text(encoding="utf-8"))
milne = next(entry for entry in library["entries"] if entry["id"] == "Milne-LEC-2013")
pdf = (ROOT / "literature" / milne["file"]).read_bytes()
assert len(pdf) == milne["bytes"] and hashlib.sha256(pdf).hexdigest() == milne["sha256"]

report = {
    "status": "passed",
    "primer": str(DOC.relative_to(ROOT)).replace("\\", "/"),
    "primer_sha256": REVIEWED,
    "primer_characters": len(raw.decode("utf-8")),
    "primer_han_characters": len(re.findall(r"[\u4e00-\u9fff]", raw.decode("utf-8"))),
    "main_numbered_sections": len(re.findall(r"(?m)^## \d+\.", raw.decode("utf-8"))),
    "local_file_links_checked": link_count,
    "display_math_groups_checked": display_math_count,
    "unchanged_compiled_lean_sources": len(audit["own_source_sha256"]),
    "new_reference_pdf_sha256": milne["sha256"],
    "independent_review": "PASS after all listed corrections",
    "scope": "Local file targets, delimiters, control characters, reviewed bytes and archived hashes; "
             "not URL-anchor validation, mathematical theorem verification or LaTeX rendering.",
}
(Path(__file__).parent / "f1-primer-validation.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(report, ensure_ascii=False, indent=2))

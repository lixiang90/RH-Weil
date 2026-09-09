"""Audit vendored sources and the explicit admission inventory (no proof claims)."""
import hashlib
import json
import re
from pathlib import Path
from bootstrap_from_cache import strip_comments

ROOT = Path(__file__).resolve().parents[1]

def main():
    sources = json.loads((ROOT / "vendor/manifest.json").read_text(encoding="utf-8"))
    checked = 0
    for package in sources:
        for item in package["files"]:
            path = ROOT / "vendor" / package["name"] / item["path"]
            raw = path.read_bytes()
            assert len(raw) == item["bytes"], path
            assert hashlib.sha256(raw).hexdigest() == item["sha256"], path
            checked += 1
    admissions = []
    own_hashes = {}
    own = sorted((ROOT / "F1").rglob("*.lean")) + [ROOT / "F1.lean"]
    for path in own:
        own_hashes[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        text = strip_comments(path.read_text(encoding="utf-8"))
        assert not re.search(r"\b(?:axiom|admit)\b", text), path
        for match in re.finditer(r"\bsorry\b", text):
            declarations = re.findall(r"\b(?:theorem|lemma|def)\s+([\w.]+)", text[:match.start()])
            admissions.append({"file": path.relative_to(ROOT).as_posix(),
                               "line": text[:match.start()].count("\n") + 1,
                               "declaration": declarations[-1],
                               "status": "classical_sorry"})
    report = {"vendor_packages": len(sources), "vendor_files_verified": checked,
              "own_lean_files": len(own), "explicit_sorry_count": len(admissions),
              "admissions": admissions,
              "own_source_sha256": own_hashes,
              "scope": "Source inventory only; see Lean build and axiom logs for kernel checks."}
    (ROOT / "checks").mkdir(exist_ok=True)
    (ROOT / "checks/source-audit.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

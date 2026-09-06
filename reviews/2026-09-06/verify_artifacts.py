"""Verify the fixed research release bytes; no mathematical inference."""

from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
digest = lambda data: hashlib.sha256(data).hexdigest()


def main():
    build = json.loads((Path(__file__).parent / "paper-build-manifest.json").read_text(encoding="utf-8"))
    sources = set()
    for paper in build["papers"]:
        assert digest((ROOT / paper["pdf_file"]).read_bytes()) == paper["pdf_sha256"], paper["name"]
        for source in paper["sources"]:
            raw = (ROOT / source["file"]).read_bytes().replace(b"\r\n", b"\n")
            assert digest(raw) == source["sha256_lf"], source["file"]
            sources.add(source["file"])
    library = json.loads((ROOT / "literature/manifest.json").read_text(encoding="utf-8"))
    archived = 0
    for entry in library["entries"] + library.get("supplement_provenance", []):
        if entry.get("file") and entry.get("sha256"):
            assert digest((ROOT / "literature" / entry["file"]).read_bytes()) == entry["sha256"], entry.get("id", entry["file"])
            archived += 1
    old = ROOT / "goals/archive/GOAL.old.md"
    assert digest(old.read_bytes()) == "2ef693cc3f1ec6e396c5bada04ba93230c8a956511e923500cdf966f3d216a2c"
    print(f"PASS: 3 paper PDFs, {len(sources)} TeX sources, {archived} literature artifacts, original GOAL bytes")
    print("Scope: saved-version integrity only; no proof or asymptotic certification")


if __name__ == "__main__":
    main()

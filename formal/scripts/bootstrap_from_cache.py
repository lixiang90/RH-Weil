"""Optional offline bootstrap from a read-only, exact-version mathlib package cache.

Exports mathlib's pinned source and copies only imported Lean object closures.
Never edits the supplied package directory. Normal setup uses Lake instead.
"""
import argparse
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]
REVISION = "905b95818eb32af7874a58b427f50c1711a5e96c"

def strip_comments(text):
    """Preserve lines while removing Lean's nested block and line comments."""
    out, depth, i = [], 0, 0
    while i < len(text):
        pair = text[i:i+2]
        if pair == "/-":
            depth += 1
            i += 2
        elif depth and pair == "-/":
            depth -= 1
            i += 2
        elif not depth and pair == "--":
            end = text.find("\n", i)
            i = len(text) if end == -1 else end
        else:
            out.append(text[i] if not depth or text[i] == "\n" else " ")
            i += 1
    return "".join(out)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("packages", type=Path)
    args = parser.parse_args()
    packages = args.packages.resolve()
    mathlib = packages / "mathlib"
    revision = subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"],
                                      text=True).strip()
    assert revision == REVISION
    destination = ROOT / ".lake/packages/mathlib"
    destination.mkdir(parents=True, exist_ok=True)
    raw = subprocess.check_output(["git", "-C", str(mathlib), "archive", "--format=tar", revision])
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as archive:
        for item in archive.getmembers():
            assert (destination / item.name).resolve().is_relative_to(destination.resolve())
            assert not item.islnk(), item.name
        archive.extractall(destination, members=[
            m for m in archive.getmembers() if not m.issym()], filter="data")
        # Same representation as a Windows Git checkout with core.symlinks=false.
        # Benchmark-only links are text blobs; never follow or execute them here.
        for item in archive.getmembers():
            if item.issym():
                output = destination / item.name
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(item.linkname, encoding="utf-8")
    print("Exported exact mathlib source", revision, flush=True)
    records = json.loads((ROOT / "vendor/manifest.json").read_text(encoding="utf-8"))
    locations = [(ROOT, ROOT)]
    locations.append((mathlib, destination))
    for entry in records:
        origin = packages / entry["name"]
        head = subprocess.check_output(["git", "-C", str(origin), "rev-parse", "HEAD"],
                                       text=True).strip()
        assert head == entry["revision"]
        locations.append((origin, ROOT / "vendor" / entry["name"]))
    visited = set()
    missing = []
    copied = 0

    def visit(module):
        nonlocal copied
        if module in visited:
            return
        visited.add(module)
        relative = Path(*module.split("."))
        for source, target in locations:
            code = source / relative.with_suffix(".lean")
            if not code.exists():
                continue
            content = strip_comments(code.read_text(encoding="utf-8"))
            imports = re.findall(r"^(?:(?:public|private|meta)\s+)*import\s+([A-Za-z0-9_. ]+)",
                                 content, re.MULTILINE)
            for group in imports:
                for dependency in group.split():
                    if dependency == "all":
                        continue
                    visit(dependency)
            if source == ROOT:
                return
            base = source / ".lake/build/lib/lean" / relative
            if not base.with_suffix(".olean").exists():
                missing.append(module)
            for suffix in (".olean", ".olean.private", ".olean.server", ".ilean", ".trace"):
                artifact = Path(str(base) + suffix)
                if artifact.exists():
                    output = target / ".lake/build/lib/lean" / relative.parent / artifact.name
                    output.parent.mkdir(parents=True, exist_ok=True)
                    if not output.exists() or output.stat().st_size != artifact.stat().st_size:
                        shutil.copy2(artifact, output)
                        copied += 1
            return
        # Lean/Std/Lake modules are supplied by the pinned toolchain.
        assert module.split(".")[0] in ("Lean", "Std", "Init", "Lake"), module

    visit("F1")
    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "build/bootstrap.json").write_text(json.dumps({
        "mathlib_revision": revision, "visited_modules": len(visited),
        "copied_artifacts": copied, "missing_cached_modules": missing},
        indent=2) + "\n", encoding="utf-8")
    print("Visited", len(visited), "modules; copied", copied, "; missing", len(missing), flush=True)
    if missing:
        print("\n".join(missing))

if __name__ == "__main__":
    main()

"""Optional cache reuse AFTER lake update, from read-only exact-version packages.

Requires the target mathlib Git checkout; never initializes or overwrites sources.
Copies imported artifact closures using the pinned Cache.IO.mkBuildPaths layout.
Never edits the supplied package directory. Normal setup uses Lake instead.
"""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess

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
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    packages = args.packages.resolve()
    mathlib = packages / "mathlib"
    revision = subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"],
                                      text=True).strip()
    assert revision == REVISION
    destination = ROOT / ".lake/packages/mathlib"
    assert (destination / ".git").exists(), "Run lake update before optional cache reuse"
    target_revision = subprocess.check_output(
        ["git", "-C", str(destination), "rev-parse", "HEAD"], text=True).strip()
    assert target_revision == REVISION
    assert subprocess.run(["git", "-C", str(destination), "diff", "--quiet", "HEAD"]).returncode == 0, \
        "Target mathlib has source changes; refusing cache reuse"
    records = json.loads((ROOT / "vendor/manifest.json").read_text(encoding="utf-8"))
    locations = [(ROOT, ROOT)]
    locations.append((mathlib, destination))
    for entry in records:
        origin = packages / entry["name"]
        head = subprocess.check_output(["git", "-C", str(origin), "rev-parse", "HEAD"],
                                       text=True).strip()
        assert head == entry["revision"]
        locations.append((origin, ROOT / "vendor" / entry["name"]))
    if args.check_only:
        print("Source and target package revisions verified; no artifacts copied.")
        return
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
            assert code.read_bytes() == (target / relative.with_suffix(".lean")).read_bytes(), code
            lib = Path(".lake/build/lib/lean") / relative
            ir = Path(".lake/build/ir") / relative
            required = [Path(str(lib) + ext) for ext in (".olean", ".olean.hash", ".ilean", ".ilean.hash")]
            required += [Path(str(ir) + ext) for ext in (".c", ".c.hash")]
            trace = Path(str(lib) + ".trace")
            complete = all((source / p).exists() for p in required + [trace])
            if not complete:
                missing.append(module)
            artifacts = required + [Path(str(lib) + ext) for ext in (
                ".olean.private", ".olean.server", ".ir", ".olean.private.hash",
                ".olean.server.hash", ".ir.hash", ".extra")]
            # Invalidate the marker before copying; only install it after all
            # required and available optional outputs have been copied successfully.
            marker = target / trace
            artifact_root = (target / ".lake/build").resolve()
            assert marker.resolve().is_relative_to(artifact_root)
            marker.unlink(missing_ok=True)
            for artifact_path in artifacts + ([trace] if complete else []):
                artifact = source / artifact_path
                if artifact.exists():
                    output = target / artifact_path
                    assert output.resolve().is_relative_to(artifact_root)
                    output.parent.mkdir(parents=True, exist_ok=True)
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

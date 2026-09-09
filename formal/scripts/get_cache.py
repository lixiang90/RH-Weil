"""Run the official cache against its unchanged mathlib manifest.

Root dependencies intentionally use local source paths. Verify their exact bytes
first, then let the official cache use the upstream Git manifest for hashing.
Run via `lake env python scripts/get_cache.py [Mathlib.Module ...]`.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import shutil
from audit import main as audit_sources
from bootstrap_from_cache import ROOT, REVISION, strip_comments
import re

audit_sources()
mathlib = ROOT / ".lake/packages/mathlib"
head = subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
assert head == REVISION, head
upstream = json.loads((mathlib / "lake-manifest.json").read_text(encoding="utf-8"))
vendored = json.loads((ROOT / "vendor/manifest.json").read_text(encoding="utf-8"))
versions = {p["name"]: p["rev"] for p in upstream["packages"]}
assert all(versions[p["name"]] == p["revision"] for p in vendored)
env = os.environ.copy()
if env.get("LEAN_SYSROOT"):
    env["PATH"] = str(Path(env["LEAN_SYSROOT"]) / "bin") + os.pathsep + env["PATH"]
targets = sys.argv[1:]
command = "get"
if targets and targets[0] == "--repair":
    targets = targets[1:]
    # Incomplete optional caches can have traces but lack IR/hash companions.
    # Remove only generated trace markers inside this project, so official get
    # re-extracts matching local archives without forcing network downloads.
    cache_roots = [mathlib] + [ROOT / "vendor" / p["name"] for p in vendored]
    marker_roots = [(root / ".lake/build/lib/lean").resolve() for root in cache_roots]
    markers = [p for root in marker_roots for p in root.rglob("*.trace")]
    assert all(any(p.resolve().is_relative_to(root) for root in marker_roots) for p in markers)
    for marker in markers:
        marker.unlink()
if not targets:
    targets = sorted({name for path in (ROOT / "F1").rglob("*.lean")
        for name in re.findall(r"(?m)^import (Mathlib\.[\w.]+)",
                               strip_comments(path.read_text(encoding="utf-8")))})
binary = mathlib / ".lake/build/bin" / ("cache.exe" if os.name == "nt" else "cache")
result = subprocess.call([str(binary), command, *targets], cwd=mathlib, env=env)
if result:
    raise SystemExit(result)
# Official dependency archives contain .lake/packages/NAME paths. Running the
# official tool from mathlib preserves hashes but cannot redirect those paths to
# this project's vendor layout; copy the generated outputs explicitly afterwards.
installed = 0
for package in vendored:
    name = package["name"]
    assert re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name)
    origin = (mathlib / ".lake/packages" / name / ".lake/build").resolve()
    if not origin.is_dir():
        continue
    destination = (ROOT / "vendor" / name / ".lake/build").resolve()
    files = [path for path in origin.rglob("*") if path.is_file()]
    traces = [path for path in files if path.suffix == ".trace"]
    for path in traces:
        marker = destination / path.relative_to(origin)
        assert marker.resolve().is_relative_to(destination)
        marker.unlink(missing_ok=True)
    for path in [p for p in files if p.suffix != ".trace"] + traces:
        assert path.resolve().is_relative_to(origin)
        output = destination / path.relative_to(origin)
        assert output.resolve().is_relative_to(destination)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, output)
    installed += 1
print("Installed official artifact sets for", installed, "vendored packages.", flush=True)

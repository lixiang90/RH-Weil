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
    markers = [p for root in cache_roots
               for p in (root / ".lake/build/lib/lean").rglob("*.trace")]
    assert all(p.resolve().is_relative_to(ROOT.resolve()) for p in markers)
    for marker in markers:
        marker.unlink()
if not targets:
    targets = sorted({name for path in (ROOT / "F1").rglob("*.lean")
        for name in re.findall(r"(?m)^import (Mathlib\.[\w.]+)",
                               strip_comments(path.read_text(encoding="utf-8")))})
binary = mathlib / ".lake/build/bin" / ("cache.exe" if os.name == "nt" else "cache")
raise SystemExit(subprocess.call([str(binary), command, *targets], cwd=mathlib, env=env))

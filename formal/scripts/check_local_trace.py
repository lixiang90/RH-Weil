"""Check LocalTrace against the pinned mathlib, without rebuilding the full library.

Normal checkout: python scripts/check_local_trace.py
This host's preserved cache: python scripts/check_local_trace.py --cache-backup .lake/hdd-backup-05156b5b
The optional backup is read as a dependency cache; sources and old junctions are not edited.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
REV = "905b95818eb32af7874a58b427f50c1711a5e96c"
NAMES = [
    "reflected_involutive", "reflected_fixed_neg", "selfConvolution_at_zero",
    "selfConvolution_at_zero_pos", "test_selfConvolution_at_zero_pos",
    "identityCorrection_eq_of_zero", "identityCorrection_self_difference",
    "identityCorrection_self_ne",
]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-backup", type=Path)
    parser.add_argument("--runtime-dir", type=Path, help="Prepared local artifact directory; research sources stay in formal")
    parser.add_argument("--check-weil", action="store_true", help="Also compile the affected Weil module; its two existing admissions remain explicit")
    args = parser.parse_args()
    backup = (ROOT / args.cache_backup).resolve() if args.cache_backup else None
    if backup:
        assert backup.is_relative_to(ROOT), "Use a preserved cache inside this formal project"
    mathlib = backup / "mathlib" if backup else ROOT / ".lake/packages/mathlib"
    lean = shutil.which("lean")
    git = shutil.which("git")
    assert lean and git, "Lean and Git must be on PATH"
    version = subprocess.check_output([lean, "--version"], cwd=ROOT, text=True).strip()
    assert "version 4.32.2," in version, version
    revision = subprocess.check_output(
        [git, "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    assert revision == REV, revision
    runtime = args.runtime_dir.resolve() if args.runtime_dir else None
    if runtime:
        shutil.copyfile(ROOT / "lean-toolchain", runtime / "lean-toolchain")
        cache_manifest = json.loads((runtime / "cache-manifest.json").read_text(encoding="utf-8"))
        assert cache_manifest["mathlib_revision"] == REV
        assert not cache_manifest["missing"], cache_manifest["missing"]
    output = runtime / "lib/lean" if runtime else ROOT / ".lake/local-trace-check/lib/lean"
    (output / "F1/Analysis").mkdir(parents=True, exist_ok=True)
    libraries = [output] if runtime else [output, mathlib / ".lake/build/lib/lean"]
    for name in ["aesop", "batteries", "Qq", "plausible", "importGraph",
                 "LeanSearchClient", "proofwidgets", "Cli"]:
        if runtime:
            continue
        candidates = [mathlib / ".lake/packages" / name / ".lake/build/lib/lean"]
        if backup:
            candidates.insert(0, backup / ("vendor-" + name) / "build/lib/lean")
        candidates.append(ROOT / "vendor" / name / ".lake/build/lib/lean")
        if backup:
            # The preserved cache and official package cache can contain complementary
            # modules. Lean selects a package root, not individual files across roots.
            # Merge generated artifacts into our isolated output; keep sources intact.
            for candidate in candidates:
                if not candidate.is_dir():
                    continue
                for source in candidate.rglob("*"):
                    if not source.is_file() or ".tmp" in source.name:
                        continue
                    if not any(source.name.endswith(suffix) for suffix in
                               (".olean", ".olean.private", ".olean.server", ".ilean", ".ir")):
                        continue
                    target = output / source.relative_to(candidate)
                    assert target.resolve().is_relative_to(output.resolve())
                    if target.exists() and target.stat().st_size == source.stat().st_size:
                        continue
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, target)
        else:
            libraries.extend(next(([p] for p in candidates if p.is_dir()), []))
    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(map(str, libraries))
    checks = ROOT / "checks"
    report = {
        "status": "incomplete", "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lean_version": version, "mathlib_revision": revision,
        "cache_backup": str(args.cache_backup) if backup else None,
        "runtime_dir": str(runtime) if runtime else None,
        "scope": "Shared test-function definitions recompiled; eight LocalTrace results checked. No full F1 build.",
        "commands": [], "source_sha256": {}, "axioms": {},
    }
    report_path = checks / "local-trace-verification.json"
    def save():
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                               encoding="utf-8")
    save()
    sources = ["F1/Analysis/TestFunctions.lean", "F1/Analysis/LocalTrace.lean",
               "checks/LocalTraceAudit.lean"]
    if args.check_weil:
        sources.append("F1/Analysis/Weil.lean")
        report["scope"] += " Affected Weil module compatibility compiled with its original admissions."
    with (checks / "local-trace-build.txt").open("w", encoding="utf-8") as log:
        for source in sources:
            report["source_sha256"][source] = hashlib.sha256((ROOT / source).read_bytes()).hexdigest()
            if runtime:
                target_source = runtime / source
                target_source.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / source, target_source)
            command = [lean]
            if source.startswith("F1/"):
                command += ["-o", str(output / Path(source).with_suffix(".olean"))]
            command.append(source)
            run = subprocess.run(command, cwd=runtime or ROOT, env=env, capture_output=True, text=True,
                                 encoding="utf-8", errors="replace", timeout=1200)
            text = run.stdout + run.stderr
            print(source, "exit", run.returncode, flush=True)
            print(text, end="", flush=True)
            log.write(source + "\n" + text.rstrip("\r\n") + "\n")
            log.flush()
            report["commands"].append({"source": source, "exit_code": run.returncode})
            if run.returncode:
                report["status"] = "failed"
                save()
                raise SystemExit(run.returncode)
            if source.startswith("checks/"):
                (checks / "local-trace-axioms.txt").write_text(text, encoding="utf-8")
                for name, axioms in re.findall(
                    r"'([^']+)' (?:depends on axioms: \[([\s\S]*?)\]|does not depend on any axioms)", text):
                    report["axioms"][name] = re.findall(r"[A-Za-z_][A-Za-z0-9_.]*", axioms)
            save()
    for name in NAMES:
        axioms = report["axioms"]["RHWeil.F1." + name]
        assert set(axioms) <= {"propext", "Classical.choice", "Quot.sound"}, (name, axioms)
    report["status"] = "passed_no_sorry_dependencies"
    report["existing_admissions"] = "The existing Weil convergence and criterion admissions are not imported by these eight results."
    save()
    print(report["status"])

if __name__ == "__main__":
    main()

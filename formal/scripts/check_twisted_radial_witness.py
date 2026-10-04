"""Compile note 423's core Lean witnesses, without a mathlib cache or full build."""
from pathlib import Path
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
NAMES = ["twistedLattice_rankOne", "twistedLattice_twoDimensional",
         "twistedWitness_forwardLabel", "twistedWitness_reverseLabel"]


def main():
    lean = shutil.which("lean")
    assert lean, "Lean must be on PATH"
    version = subprocess.check_output([lean, "--version"], cwd=ROOT, text=True).strip()
    assert "version 4.32.2," in version, version
    output = ROOT/"checks"/".twisted-radial-runtime"/"lib"/"lean"
    (output/"F1"/"Analysis").mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["LEAN_PATH"] = str(output)
    prefix = ROOT/"checks"/"twisted-radial-witness"
    report = {"status": "incomplete", "lean_version": version,
              "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "scope": "Four core integer results: pointwise unilateral and two-dimensional finite-rank witness, and both product labels for arbitrary gamma. No operator analysis, cyclic theory, RH, mathlib cache or full F1 build.",
              "commands": [], "source_sha256": {}, "axioms": {}}
    sources = ["F1/Analysis/TwistedRadialWitness.lean", "checks/TwistedRadialWitnessAudit.lean"]
    with Path(str(prefix)+"-build.txt").open("w", encoding="utf-8") as log:
        for source in sources:
            report["source_sha256"][source] = hashlib.sha256((ROOT/source).read_bytes()).hexdigest()
            command = [lean]
            if source.startswith("F1/"):
                command += ["-o", str(output/Path(source).with_suffix(".olean"))]
            command.append(source)
            run = subprocess.run(command, cwd=ROOT, env=env, capture_output=True,
                                 text=True, encoding="utf-8", errors="replace", timeout=120)
            text = run.stdout+run.stderr
            log.write(source+"\n"+text+"\n")
            print(source, "exit", run.returncode)
            if text:
                print(text, end="")
            report["commands"].append({"source": source, "exit_code": run.returncode})
            if run.returncode:
                report["status"] = "failed"
                Path(str(prefix)+"-verification.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
                raise SystemExit(run.returncode)
            if source.startswith("checks/"):
                Path(str(prefix)+"-axioms.txt").write_text(text, encoding="utf-8")
                for name, axioms in re.findall(r"'([^']+)' (?:depends on axioms: \[([\s\S]*?)\]|does not depend on any axioms)", text):
                    report["axioms"][name] = re.findall(r"[A-Za-z_][A-Za-z0-9_.]*", axioms)
    for name in NAMES:
        axioms = report["axioms"]["RHWeil.F1."+name]
        assert set(axioms) <= {"propext", "Classical.choice", "Quot.sound"}, (name, axioms)
    report["status"] = "passed_no_sorry_dependencies"
    Path(str(prefix)+"-verification.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(report["status"])


if __name__ == "__main__":
    main()

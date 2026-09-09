"""Build the entire blueprint and check the transitive axiom boundary.

Run from formal with the pinned Lean/Lake on PATH. Requires Python 3.10+.
This verifies an admitted blueprint, not an unconditional RH proof.
"""
import json
from pathlib import Path
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / "checks"
CHECKS.mkdir(exist_ok=True)
results = []
(CHECKS / "verification.json").write_text(
    '{"status": "verification_incomplete"}\n', encoding="utf-8")

def run(name, command):
    lines = []
    with (CHECKS / (name + ".txt")).open("w", encoding="utf-8", newline="\n") as log:
        result = subprocess.Popen(command, cwd=ROOT, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
        for line in result.stdout:
            lines.append(line)
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
        exit_code = result.wait()
    output = "".join(lines)
    results.append({"name": name, "command": command, "exit_code": exit_code})
    print(name, "exit", exit_code, flush=True)
    if exit_code:
        (CHECKS / "verification.json").write_text(json.dumps(
            {"status": "failed", "checks": results}, indent=2) + "\n", encoding="utf-8")
        raise SystemExit(exit_code)
    return output

version = run("lean-version", ["lean", "--version"])
assert "version 4.32.2," in version, version
run("lake-version", ["lake", "--version"])
run("lake-build", ["lake", "build"])
axioms = run("axioms", ["lake", "env", "lean", "F1/Audit.lean"])
run("source-audit", [sys.executable, "scripts/audit.py", "--tracked"])
dependencies = {name: set(re.findall(r"[A-Za-z_][A-Za-z0-9_.]*", values or ""))
    for name, values in re.findall(
        r"'([A-Za-z0-9_.]+)' (?:depends on axioms: \[([\s\S]*?)\]|does not depend on any axioms)",
        axioms)}
pure = ["prime_scaling_surjective", "restrict_restrict", "two_three_six",
        "graphParam_injective", "graphParam_surjective", "graphEquiv",
        "jensen_const_two", "nonpositive_of_existence"]
admitted = ["jensen_not_max_additive", "exponentPresheaf_isSheaf",
            "exponent_stalk_at_prime", "mem_primeLocalization_iff",
            "newtonEquivalent_iff_hull", "finiteLift_circleIntegrable",
            "jensen_finite_lift", "finiteProfile_weakSecond",
            "jensen_one_add_and_sub", "weil_convergence", "weilCriterion", "rh_of_existence"]
for name in pure + admitted:
    key = "RHWeil.F1." + name
    assert key in dependencies, ("Missing axiom output", key)
    assert dependencies[key] <= {"propext", "Classical.choice", "Quot.sound", "sorryAx"}, key
    assert ("sorryAx" in dependencies[key]) == (name in admitted), (key, dependencies[key])
report = {"status": "passed_with_explicit_admissions", "checks": results,
          "axioms": {key: sorted(value) for key, value in dependencies.items()},
          "scope": "Entire F1 library built; listed transitive axiom boundaries verified. "
                   "Classical admissions and geometric existence hypotheses remain unproved."}
(CHECKS / "verification.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(report["status"], flush=True)

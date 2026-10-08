#!/usr/bin/env python3
"""Replay the fixed public PC8CL finite data, without building its project.

This adapts pure declarations to Lean's standard library. It does not compile
the external Real/analytic proof, and cannot alone prove a zero proportion.
Source: josusanmartin/riemann, commit d272437e7ebeb17b87c8c3d7cece592aa23785ab,
submissions/dani-bound-2026/proof/Solution.lean. See the two local PC8 audits
for source provenance, interval semantics and the separate admission gates.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess

if not __debug__:
    raise RuntimeError("PC8 replay requires assertions enabled; do not use Python -O")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "tmp" / "pc8-am-admission"
OUTPUT = ROOT / "output" / "am-pc8-finite-replay.json"
SOURCE_SHA = "012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f"
COMMIT = "d272437e7ebeb17b87c8c3d7cece592aa23785ab"
SOURCE_URL = ("https://raw.githubusercontent.com/josusanmartin/riemann/" + COMMIT
              + "/submissions/dani-bound-2026/proof/Solution.lean")
COMMAND = re.compile(
    r"^(?:(?:@\[[^\n]*\]\s*)?(?:private |noncomputable )?"
    r"(?:def |abbrev |structure |theorem |lemma |instance |opaque |axiom )"
    r"|namespace |end(?: |$)|section(?: |$)|noncomputable section|open "
    r"|variable |set_option |#|local |notation)")
REAL_DEPENDENCIES = re.compile(
    r"ℝ|\b(?:Real|Finset|HasDerivAt|Filter|InCell|CovBy|Covered|WalkOK|CovK|"
    r"Pg|Base|GapR|Enc|WCert|Fw|wfun|TVal|KOK|PyrOK|PTOK)\b")

PRELUDE = """import Std
notation "ℕ" => Nat
notation "ℤ" => Int
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option linter.unusedVariables false
universe u
@[macro_inline] def boolRec {motive : Bool → Sort u} (a : motive false)
    (b : motive true) (c : Bool) : motive c :=
  match c with | false => a | true => b
def listRec {α : Type} {motive : List α → Sort u} (a : motive [])
    (b : (h : α) → (t : List α) → motive t → motive (h :: t))
    (c : List α) : motive c :=
  match c with | [] => a | h :: t => b h t (listRec a b t)
theorem boolRec_equivalent {motive : Bool → Sort u} (a : motive false)
    (b : motive true) (c : Bool) : boolRec a b c = Bool.rec a b c := by
  cases c <;> rfl
theorem listRec_equivalent {α : Type} {motive : List α → Sort u}
    (a : motive []) (b : (h : α) → (t : List α) → motive t → motive (h :: t))
    (c : List α) : listRec a b c = List.rec a b c := by
  induction c with
  | nil => rfl
  | cons h t ih => exact congrArg (b h t) ih
namespace AMW.Cert.Pyr
def extractionNamespaceSentinel : Nat := 0
end AMW.Cert.Pyr
namespace AMW.Cert.PyrD
def extractionNamespaceSentinel : Nat := 0
end AMW.Cert.PyrD
namespace AMW.Cert.PCell
def extractionNamespaceSentinel : Nat := 0
end AMW.Cert.PCell
namespace AMW.Cert.PC8CL
def extractionNamespaceSentinel : Nat := 0
end AMW.Cert.PC8CL
"""
CALLBACK_GUARDS = """
namespace ReplayCallbackEquivalence
theorem forceR_equivalent (a : Nat) (k : Nat → Nat) :
 AMW.Cert.Pyr.forceR a k = Nat.rec (motive := fun _ => Nat) (k 0)
   (fun n _ => k (Nat.succ n)) a := by cases a <;> rfl
theorem forceB_equivalent (a : Nat) (k : Nat → Bool) :
 AMW.Cert.PyrD.forceB a k = Nat.rec (motive := fun _ => Bool) (k 0)
   (fun n _ => k (Nat.succ n)) a := by cases a <;> rfl
theorem forceT_equivalent {α : Sort u} (a : Nat) (k : Nat → α) :
 AMW.Cert.PCell.forceT a k = Nat.rec (motive := fun _ => α) (k 0)
   (fun n _ => k (Nat.succ n)) a := by cases a <;> rfl
end ReplayCallbackEquivalence
"""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def extract(lines: list[str]) -> tuple[str, list[dict]]:
    starts = [i for i, x in enumerate(lines) if COMMAND.match(x)] + [len(lines)]
    stack: list[tuple[str, str]] = []
    parts, index, namespace = [PRELUDE], [], ""
    callback_count = 0
    for j, i in enumerate(starts[:-1]):
        line = lines[i]
        text = "\n".join(lines[i:starts[j + 1]]).strip()
        if line.startswith("namespace "):
            stack.append(("namespace", line[10:].strip()))
            continue
        if line.startswith("section") or line.startswith("noncomputable section"):
            stack.append(("section", line.split("section", 1)[1].strip()))
            continue
        if re.match(r"^end(?: |$)", line):
            if stack:
                stack.pop()
            continue
        if not 7184 <= i + 1 <= 18649:
            continue
        m = re.match(r"^(?:@\[[^\n]*\]\s*)?(?:private |noncomputable )?"
                     r"(def|abbrev|structure)\s+(\S+)", line)
        if not m or REAL_DEPENDENCIES.search(text):
            continue
        header = text.split(":=", 1)[0]
        if re.search(r": Prop\b|→ Prop\b", header):
            continue
        name = m[2]
        nsp = ".".join(v for t, v in stack if t == "namespace")
        if namespace != nsp:
            if namespace:
                parts.append("end " + namespace)
            if nsp:
                parts.append("namespace " + nsp)
            if nsp.startswith("AMW.Cert"):
                parts.append("open AMW.G AMW.Cert AMW.Cert.Pyr "
                             "AMW.Cert.PyrD AMW.Cert.PCell AMW.Cert.PC8CL")
            if nsp == "AMW.G.CellA":
                parts.append("variable (c : CellA)")
            namespace = nsp
        text = re.sub(r"^(?:@\[[^\n]*\]\s*)?(?:private |noncomputable )?", "", text)
        if name in {"forceR", "forceB", "forceT"}:
            assert text.split(":=", 1)[1].lstrip().startswith("Nat.rec")
            text = text.split(":=", 1)[0] + ":= k a"
            callback_count += 1
        text = text.replace("Bool.rec", "boolRec").replace("List.rec", "listRec")
        if name in {"dsel", "dpk"}:
            # Pure branch routers: inline so unused subtrees are not evaluated.
            # This is compiler metadata only; the defining term is unchanged.
            text = "@[macro_inline] " + text
        parts.append(f"-- Fixed source lines {i + 1}-{starts[j + 1]}\n" + text)
        index.append({"name": nsp + "." + name, "first": i + 1, "last": starts[j + 1]})
    if namespace:
        parts.append("end " + namespace)
    parts.append(CALLBACK_GUARDS)
    assert len(index) == 2744 and callback_count == 3
    return "\n\n".join(parts) + "\n", index


def planned_checks(lines: list[str]) -> list[tuple[str, str]]:
    checks = [
        ("win16", "AMW.Cert.Pyr.allBelow 16 AMW.Cert.winOk"),
        ("value-top", "topOk TOP BK"),
        ("value-block512", "allFrom 0 512 (fun j => blockOk (BK j) j)"),
        ("derivative-top", "topOk2 TOPD BKD"),
        ("derivative-block512", "allFrom 0 512 (fun j => blockOk2 (BKD j) j)"),
        ("convex-regions", "rgOk REG"),
        ("large-gap7", "allBelow 7 (fun r => Nat.ble (cN * SC) (BS.getD r 0 * SMAX r))"),
        ("adjacent7", "allBelow 7 (fun r => Nat.ble (cN * 4) (tA TS (ADJ.getD r 0)))"),
        ("root-W", "Nat.ble (7 * KB) 1099511627776"),
    ]
    checks.extend((f"cover-{r}", f"coverChk cN (tA TS (ADJ.getD {r} 0)) "
                   f"(SC / 2) (SMAX {r}) (COV.getD {r} [])") for r in range(7))
    for line in lines:
        m = re.fullmatch(r"def PTL_(\d+) \(x : ℕ\) : ℕ := ptl (.+) x", line)
        if m:
            checks.append(("point-list-" + m[1], "ptlOk " + m[2]))
    for line in lines:
        m = re.match(r"theorem wcc(\d+)_\d+ : (.+) = (\d+) :=", line)
        if m:
            assert int(m[3]) > 0
            checks.append(("root-" + m[1], "Nat.beq (" + m[2] + ") " + m[3]))
    names = [n for n, _ in checks]
    assert len(checks) == len(set(names)) == 240
    assert sum(n.startswith("point-list-") for n in names) == 192
    assert {f"root-{j}" for j in range(32)} <= set(names)
    return checks


def structure_checks(lines: list[str]) -> list[str]:
    def table(name: str, after: int = 12800):
        line = next(x for i, x in enumerate(lines) if i + 1 >= after and
                    re.match(r"^def " + name + r"\s*:", x))
        return ast.literal_eval(line.split(":=", 1)[1].strip())
    pr, ts, sl, bs, adj = (table(n) for n in ("PR", "TS", "SL", "BS", "ADJ"))
    assert pr == [(i, j) for i in range(8) for j in range(i + 2, 8)]
    assert len(ts) == 26 and len(set((i, j) for i, j, _, _ in ts)) == 26
    assert all(0 <= i < j <= 7 and a > 0 and
               (j == i + 1 or pr[k] == (i, j)) for i, j, a, k in ts)
    assert len(sl) == 64
    for i in range(8):
        for j in range(i + 1, 8):
            assert sl[8 * i + j] == (i if j == i + 1 else 7 + pr.index((i, j)))
    assert len(adj) == 7 and all(ts[adj[r]][:2] == (r, r + 1) for r in range(7))
    assert bs == bs[::-1] and sum(bs) == 404350
    weights = {(i, j): a for i, j, a, k in ts}
    assert all(weights.get((7 - j, 7 - i)) == a for (i, j), a in weights.items())
    assert all(sum(a for i, j, a, k in ts if j - i == d) <= 200000000
               for d in range(1, 8))
    return ["PR21", "TS26", "SL28", "ADJ7", "pressure-sum-and-reversal",
            "pair-weight-reversal", "span-capacity7"]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, default=WORK / "Solution.lean")
    ap.add_argument("--lean", default=r"C:\Users\A\.elan\bin\lean.exe")
    ap.add_argument("--generate-only", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    raw = args.source.read_bytes()
    assert len(raw) == 1675641 and digest(raw) == SOURCE_SHA, "fixed source identity failed"
    lines = raw.decode("utf-8").splitlines()
    assert len(lines) == 19049
    core, index = extract(lines)
    bridges = []
    for name in ("AMPC8StructuralBridge.lean", "AMPC8MinorantBridge.lean"):
        path = ROOT / "formal" / "certificates" / name
        content = canonical(path.read_bytes())
        assert not re.search(rb"\bsorry\b|^\s*axiom\b", content, flags=re.M)
        bridges.append({"path": path.relative_to(ROOT).as_posix(), "sha256": digest(content)})
        core += "\n" + content.decode("utf-8")
    checks = planned_checks(lines)
    finite_structure = structure_checks(lines)
    run = core + "\nnamespace ReplayRun\nopen AMW.Cert AMW.Cert.Pyr " \
          "AMW.Cert.PyrD AMW.Cert.PCell AMW.Cert.PC8CL AMW.Cert.PC8CLData\n" \
          'def emit (name : String) (passed : Bool) : IO Unit := ' \
          'IO.println ("CHECK " ++ name ++ " " ++ toString passed)\n'
    run += "\n".join('#eval emit "' + n + '" (' + e + ')' for n, e in checks)
    run += "\nend ReplayRun\n"
    WORK.mkdir(parents=True, exist_ok=True)
    (WORK / "NumericCore.lean").write_bytes(core.encode())
    run_path = WORK / "NumericRun.lean"
    run_path.write_bytes(run.encode())
    (WORK / "numeric-extraction-index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.generate_only:
        print("generated 2744 pure declarations, 240 finite checks, 7 structure checks")
        return
    command = [args.lean, "+leanprover/lean4:v4.34.1", "--tstack=32768", "-j1", str(run_path)]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, timeout=1800)
    log = (completed.stdout + completed.stderr).decode("utf-8", errors="replace")
    (WORK / "numeric-replay-log.txt").write_text(log, encoding="utf-8")
    actual = re.findall(r"^CHECK (\S+) (true|false)$", log, flags=re.M)
    expected = [(n, "true") for n, _ in checks]
    assert completed.returncode == 0, f"Lean exit {completed.returncode}; see numeric-replay-log.txt"
    assert actual == expected, "missing, duplicate, reordered, or false finite check"
    assert not re.search(r"error:|error\(|Stack overflow|Aborting|sorry|panic", log), "invalid replay log"
    result = {
        "status": "all finite data checks passed; continuous semantics requires separate audit",
        "proves_external_analytic_theorems": False,
        "proves_zero_proportion_by_itself": False,
        "source_commit": COMMIT, "source_url": SOURCE_URL, "source_raw_sha256": SOURCE_SHA,
        "generator_canonical_sha256": digest(canonical(Path(__file__).read_bytes())),
        "lean_toolchain": "leanprover/lean4:v4.34.1", "lean_exit": completed.returncode,
        "numeric_core_sha256": digest(core.encode()), "numeric_runner_sha256": digest(run.encode()),
        "symbolic_bridges": bridges,
        "symbolic_main_bridges": 30, "kernel_adapter_guards": 5,
        "retained_declarations": len(index), "compiled_checks": len(checks),
        "exact_structure_checks": finite_structure,
        "checks": [{"name": n, "passed": True} for n, _ in checks],
    }
    rendered = (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode()
    if args.check:
        assert canonical(OUTPUT.read_bytes()) == rendered, "saved output differs from replay"
        print("PASS: 240 compiled checks, 7 exact structure checks; saved output matches")
    else:
        OUTPUT.write_bytes(rendered)
        print("PASS: 240 compiled checks, 7 exact structure checks; output saved")


if __name__ == "__main__":
    main()

"""Read-only static scan of the requested OpenAI Lean entry point, not a build."""

import hashlib
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MATH = Path(r"E:\codex-build\math")
LEAN = MATH / "lean"
ENTRY = "OAI.NumberTheory.DirichletL.Nonvanishing"


def without_comments_and_strings(source):
    result = []
    i, depth, quoted = 0, 0, False
    while i < len(source):
        if depth:
            if source.startswith("/-", i):
                depth += 1
                result.extend("  ")
                i += 2
            elif source.startswith("-/", i):
                depth -= 1
                result.extend("  ")
                i += 2
            else:
                result.append("\n" if source[i] == "\n" else " ")
                i += 1
        elif quoted:
            if source[i] == "\\":
                result.extend("  ")
                i += 2
            else:
                if source[i] == '"':
                    quoted = False
                result.append("\n" if source[i] == "\n" else " ")
                i += 1
        elif source.startswith("--", i):
            end = source.find("\n", i)
            end = len(source) if end < 0 else end
            result.extend(" " * (end - i))
            i = end
        elif source.startswith("/-", i):
            depth = 1
            result.extend("  ")
            i += 2
        elif source[i] == '"':
            quoted = True
            result.append(" ")
            i += 1
        else:
            result.append(source[i])
            i += 1
    return "".join(result)


def main():
    pending = [ENTRY]
    visited, external, missing, suspicious = set(), set(), set(), []
    lines, hashes = 0, {}
    while pending:
        module = pending.pop()
        if module in visited:
            continue
        path = LEAN / (module.replace(".", "/") + ".lean")
        if not path.is_file():
            (missing if module.startswith("OAI.") else external).add(module)
            continue
        visited.add(module)
        source = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
        code = without_comments_and_strings(source)
        lines += len(source.splitlines())
        hashes[module] = hashlib.sha256(source.encode()).hexdigest()
        for match in re.finditer(r"\b(?:sorry|admit|sorryAx)\b|(?m:^\s*(?:(?:private|protected)\s+)?axiom\b)", code):
            suspicious.append({"module": module, "line": code.count("\n", 0, match.start()) + 1,
                               "token": match.group().strip()})
        for match in re.finditer(r"(?m)^\s*import[ \t]+([^\n]+)", code):
            imports = match.group(1).split()
            for dependency in imports:
                if not re.fullmatch(r"[\w']+(?:\.[\w']+)*", dependency):
                    raise ValueError(f"Unparsed import: {module}: {dependency}")
                pending.append(dependency)
        if re.search(r"(?m)^\s*import[ \t]*$", code):
            raise ValueError(f"Multiline import requires parser extension: {module}")
    commit = subprocess.run(["git", "-C", str(MATH), "rev-parse", "HEAD"], check=True,
                            capture_output=True, text=True).stdout.strip()
    report = {
        "status": "passed_static_scan" if not missing and not suspicious else "findings",
        "math_commit": commit,
        "entry": ENTRY,
        "local_modules": len(visited),
        "local_source_lines": lines,
        "missing_oai_modules": sorted(missing),
        "suspicious_tokens": suspicious,
        "external_modules_not_scanned": sorted(external),
        "canonical_lf_source_sha256": dict(sorted(hashes.items())),
        "scope": "Static local-source import closure only. External imports, Lean elaboration/kernel, comparator output and approved axiom closure were not verified.",
    }
    path = ROOT / "output/openai-math-nonvanishing-static-closure.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in ("canonical_lf_source_sha256", "external_modules_not_scanned")},
                     ensure_ascii=False))
    assert not missing and not suspicious


if __name__ == "__main__":
    main()

"""Check the paper layout without compiling or modifying research artifacts."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
PAPERS = (
    "rh-weil-structure-paper",
    "partial-weil-configurations-paper",
    "abel-mass-obstruction-paper",
    "seven-eighths-boundary-improvement-paper",
    "free-b-compensated-probe-boundary-paper",
    "kappa-feedback-cubic-boundary-paper",
    "lossless-eight-point-simple-critical-paper",
    "nine-point-joint-minorant-simple-critical-paper",
    "expanded-nine-point-tangent-simple-critical-paper",
    "ninth-span-simple-critical-paper",
)


def check_layout(root: Path) -> list[str]:
    errors: list[str] = []
    for suffix in ("*.tex", "*.pdf"):
        for path in sorted(root.glob(suffix)):
            errors.append(f"Paper artifact still in repository root: {path.name}")
    for name in PAPERS:
        for relative in (f"papers/{name}.tex", f"output/pdf/{name}.pdf"):
            if not (root / relative).is_file():
                errors.append(f"Missing paper artifact: {relative}")
    for tex in sorted((root / "papers").glob("*.tex")):
        # TeX is compiled from the repository root; these sources use literal paths.
        source = re.sub(r"(?m)(?<!\\)%.*$", "", tex.read_text(encoding="utf-8"))
        for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", source):
            path = root / target
            if not path.suffix:
                path = path.with_suffix(".tex")
            if not path.is_file():
                errors.append(f"Missing TeX input from {tex.name}: {target}")
    for relative in (
        "README.md", "papers/README.md", "AUDIT_REPORT.md",
        "docs/history/README-progress-2026-10-07.md",
    ):
        document = root / relative
        if not document.is_file():
            errors.append(f"Missing layout documentation: {relative}")
            continue
        for target in re.findall(
            r"\]\(([^)\s]+\.(?:tex|pdf)(?:#[^)\s]*)?)\)",
            document.read_text(encoding="utf-8"),
        ):
            if "://" in target:
                continue
            path = document.parent / unquote(target.split("#", 1)[0])
            if not path.is_file():
                errors.append(f"Broken paper link in {relative}: {target}")
    # Versioned PDFs are project outputs or archived external literature.
    tracked = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.pdf"],
        cwd=root, check=True, capture_output=True,
    ).stdout.decode("utf-8").split("\0")
    for relative in filter(None, tracked):
        # Before staging a migration, Git still lists old paths which no longer exist.
        if (root / relative).is_file() and not relative.startswith(("output/pdf/", "literature/")):
            errors.append(f"Versioned PDF outside output/pdf or literature: {relative}")
    return errors


def main() -> None:
    errors = check_layout(ROOT)
    if errors:
        raise SystemExit("\n".join(errors))
    print("Paper layout, TeX inputs, and documentation links passed.")


if __name__ == "__main__":
    main()

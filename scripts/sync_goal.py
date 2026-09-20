"""Mirror the workspace goal and its history into the versioned repository.

Only local Markdown link targets are rebased. GOAL.old.md stays byte-identical.
The workspace files are authoritative; --check performs no writes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
FILES = (
    "GOAL.20260909.md",
    "archive/GOAL.20260909.f1-geometric-quotient.md",
    "archive/GOAL.20260909.f1-real-scales.md",
    "archive/GOAL.20260909.f1-periodic.md",
    "archive/GOAL.20260906.md",
    "archive/GOAL.old.md",
    "archive/GOAL.proposed.md",
    "archive/GOAL.20260906.phase1.md",
    "archive/GOAL.20260906.phase2.md",
    "archive/GOAL.20260906.phase3.md",
    "archive/GOAL.20260906.cycle4.md",
    "archive/GOAL.20260906.cycle5.md",
    "archive/GOAL.20260906.cycle6.md",
    "archive/GOAL.20260906.cycle7.md",
    "archive/GOAL.20260906.cycle8.md",
    "archive/GOAL.20260906.cycle9.md",
    "archive/GOAL.20260906.cycle10.md",
    "archive/GOAL.20260906.cycle11.md",
    "archive/GOAL.20260906.cycle12.md",
    "archive/README.md",
)


def mirror_bytes(relative: str, raw: bytes) -> bytes:
    if relative == "archive/GOAL.old.md":
        return raw
    source = raw.decode("utf-8")
    def rebase(match: re.Match[str]) -> str:
        target = match[1]
        if relative == "archive/GOAL.proposed.md" and target == "../GOAL.20260906.md":
            return "](GOAL.20260906.md)"
        if relative.startswith(("archive/GOAL.20260906", "archive/GOAL.20260909")):
            # This exact snapshot retains the link context of the former root goal.
            if target.startswith("RH-Weil/"):
                target = "../../" + target[len("RH-Weil/"):]
            elif target.startswith("archive/"):
                target = target[len("archive/"):]
            return "](" + target + ")"
        if target.startswith("RH-Weil/"):
            target = "../" + target[len("RH-Weil/"):]
        elif target.startswith("../RH-Weil/"):
            target = "../../" + target[len("../RH-Weil/"):]
        return "](" + target + ")"
    return re.sub(r"\]\(([^)]+)\)", rebase, source).encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    records = []
    for relative in FILES:
        raw = (WORKSPACE / relative).read_bytes()
        mirrored = mirror_bytes(relative, raw)
        destination = ROOT / "goals" / relative
        if args.check:
            if not destination.is_file() or destination.read_bytes() != mirrored:
                raise SystemExit(f"Goal mirror out of date: {relative}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(mirrored)
        records.append({
            "workspace_path": relative,
            "repository_path": "goals/" + relative,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "mirror_sha256": hashlib.sha256(mirrored).hexdigest(),
            "transformation": "none" if raw == mirrored else "local Markdown link rebasing only",
        })
    manifest = (json.dumps(records, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    destination = ROOT / "goals" / "manifest.json"
    if args.check:
        if not destination.is_file() or destination.read_bytes() != manifest:
            raise SystemExit("Goal manifest out of date")
    else:
        destination.write_bytes(manifest)
    print(f"Goal mirror {'verified' if args.check else 'saved'}: {len(records)} files.")


if __name__ == "__main__":
    main()

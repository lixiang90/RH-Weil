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
    "archive/GOAL.20260909.f1-before-weighted-hardy-trace.md",
    "archive/GOAL.20260909.f1-before-hardy-index.md",
    "archive/GOAL.20260909.f1-before-connected-time-comparison.md",
    "archive/GOAL.20260909.f1-before-split-transfer.md",
    "archive/GOAL.20260909.f1-before-defect-residue.md",
    "archive/GOAL.20260909.f1-before-boundary-unitary.md",
    "archive/GOAL.20260909.f1-before-two-place-gluing.md",
    "archive/GOAL.20260909.f1-before-transverse-trace.md",
    "archive/GOAL.20260909.f1-before-full-rational-boundary.md",
    "archive/GOAL.20260909.f1-before-boundary-k-class.md",
    "archive/GOAL.20260909.f1-before-boundary-defect.md",
    "archive/GOAL.20260909.f1-before-orbit-completion.md",
    "archive/GOAL.20260909.f1-before-prime-arrows.md",
    "archive/GOAL.20260909.f1-before-unit-descent.md",
    "archive/GOAL.20260909.f1-before-moment-radical.md",
    "archive/GOAL.20260909.f1-before-adelic-local-trace.md",
    "archive/GOAL.20260909.f1-before-fourth-space-review.md",
    "archive/GOAL.20260909.f1-before-tower-limit.md",
    "archive/GOAL.20260909.f1-before-kernel-descent.md",
    "archive/GOAL.20260909.f1-before-noncartier.md",
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
    # Read and validate every source before touching any existing mirror.
    # A truncated archive must not silently replace a preserved historical goal.
    sources = [(relative, (WORKSPACE / relative).read_bytes()) for relative in FILES]
    for relative, raw in sources:
        if not raw.strip():
            raise SystemExit(f"Refusing empty goal source before mirror writes: {relative}")
    records = []
    for relative, raw in sources:
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

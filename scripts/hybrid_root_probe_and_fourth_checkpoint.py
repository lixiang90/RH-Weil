"""Bind Gaussian root-probe research and the accepted 455/456 reductions."""

from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PREVIOUS = ROOT / "reviews/2026-10-07/number-field-choice-checkpoint.json"
OUTPUT = ROOT / "reviews/2026-10-07/root-probe-and-fourth-checkpoint.json"
SOURCE = Path("E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex")
MUTABLE = {"goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md"}
FILES = [
    "notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md",
    "notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md",
    "reviews/2026-10-07/hybrid-whole-proper-power-review-radial.md",
    "reviews/2026-10-07/hybrid-whole-proper-power-review-twisted.md",
    "reviews/2026-10-07/hybrid-high-opposite-prime-research-twisted.md",
    "reviews/2026-10-07/hybrid-high-opposite-prime-review-radial.md",
    "reviews/2026-10-07/hybrid-high-opposite-prime-review-twisted.md",
    "reviews/2026-10-07/hybrid-proper-power-and-high-opposite-review-root.md",
    "reviews/2026-10-07/hybrid-gaussian-root-weight-probe-research.md",
    "reviews/2026-10-07/hybrid-gaussian-root-probe-review-radial.md",
    "reviews/2026-10-07/hybrid-gaussian-root-probe-review-twisted.md",
    "reviews/2026-10-07/hybrid-gaussian-root-probe-review-root.md",
    "scripts/hybrid_proper_power_exact_audit.py",
    "scripts/hybrid_high_opposite_exact_audit.py",
    "scripts/hybrid_root_probe_and_fourth_checkpoint.py",
    "output/hybrid-proper-power-exact-audit.json",
    "output/hybrid-high-opposite-exact-audit.json",
    "goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md",
]
DRAFTS = [
    "reviews/2026-10-07/hybrid-distinct-two-two-prime-sector-research.md",
    "reviews/2026-10-07/hybrid-one-three-mixed-prime-sector-research.md",
    "reviews/2026-10-07/hybrid-three-column-reflection-research.md",
]


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    path = ROOT / name
    binary = path.suffix.lower() == ".pdf"
    data = path.read_bytes() if binary else canonical(path)
    return {"path": name, "sha256" if binary else "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "bytes" if binary else "canonical_utf8_bytes": len(data)}


def verify(record):
    current = binding(record["path"])
    for key in ("sha256", "sha256_canonical_lf", "bytes", "canonical_utf8_bytes"):
        if key in record:
            assert record[key] == current[key], (record["path"], key)
    return current


def exact(script, output):
    spec = importlib.util.spec_from_file_location(Path(script).stem, ROOT / script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.certify()
    assert result == json.loads((ROOT / output).read_text(encoding="utf-8"))
    return result


def build():
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    # Previous draft hashes were snapshots, not accepted immutable artifacts.
    records = previous["previous_frozen_files_verified"] + [
        r for r in previous["files"] if r["path"] not in MUTABLE
    ]
    frozen = [verify(r) for r in {r["path"]: r for r in records}.values()]
    frozen.append(binding(PREVIOUS.relative_to(ROOT).as_posix()))
    previous_drafts = {r["path"]: r for r in previous["preexisting_uncommitted_drafts_not_in_this_commit"]}
    for name in DRAFTS:
        verify(previous_drafts[name])
    source = canonical(SOURCE)
    assert hashlib.sha256(source).hexdigest() == previous["source_preserved_read_only"]["sha256_canonical_lf"]
    source_repo = str(SOURCE.parents[3])
    assert subprocess.check_output(["git", "-C", source_repo, "status", "--porcelain"], text=True).rstrip() == ""
    assert subprocess.check_output(["git", "-C", source_repo, "rev-parse", "HEAD"], text=True).strip() == "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
    evidence = [exact("scripts/hybrid_proper_power_exact_audit.py", "output/hybrid-proper-power-exact-audit.json"),
                exact("scripts/hybrid_high_opposite_exact_audit.py", "output/hybrid-high-opposite-exact-audit.json")]
    links = 0
    for name in FILES:
        path = ROOT / name
        data = canonical(path).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", data), name
        if path.suffix == ".md" and name not in MUTABLE:
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", data):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                candidate = re.sub(r":\d+$", "", target.split("#", 1)[0])
                resolved = (path.parent / candidate).resolve()
                assert resolved == OUTPUT.resolve() or resolved.exists(), (name, target)
                links += 1
    return {
        "date": "2026-10-07", "base_repository_commit": "5b7effad9126499583a2243e462e16e28b346265",
        "current_goal_turn": "progress", "goal_status": "active",
        "new_zero_free_boundary": False, "new_proportion": False, "new_paper": False,
        "accepted": ["whole proper-power S4-small and same-frame fourth-root equivalence",
                     "actual high opposite repeated trace O(N/log X) and repeated-sector limit 2S_psi",
                     "Gaussian target-preserving root-weight Poisson probe with exact unit-dual isolation and sign-adapted linear-row numerator",
                     "narrow same-sign Gaussian inverse/prime-slot raw moment with explicit U+column_length^2 cost"],
        "not_accepted": ["full genuine-prime or centered fourth budget", "new simple critical-line proportion",
                         "arbitrary-target completed Gaussian theta reflection and reciprocal Euler quotient",
                         "Gaussian raw contract for every H>=D^(1+c), c>0", "new zero-free boundary"],
        "unchanged_strict_sigma": "11/12-e*/4 = 0.874957019420098946... under existing explicit cited R",
        "source_preserved_read_only": {"path": str(SOURCE), "sha256_canonical_lf": hashlib.sha256(source).hexdigest(), "external_kernel_run": False},
        "finite_evidence_only": evidence, "previous_frozen_files_verified": frozen,
        "files": [binding(name) for name in FILES],
        "preexisting_uncommitted_drafts_not_in_this_commit": [binding(name) for name in DRAFTS],
        "format_verification": {"control_characters_checked": True, "new_local_links_checked": links},
    }


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {len(result['files'])} current files, {len(result['previous_frozen_files_verified'])} frozen artifacts, exact finite evidence and read-only source")

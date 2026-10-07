"""Bind the unmarked Gaussian all-row comparison; no analytic kernel claim."""

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PREVIOUS = ROOT / "reviews/2026-10-07/root-probe-and-fourth-checkpoint.json"
OUTPUT = ROOT / "reviews/2026-10-07/gaussian-all-row-large-sieve-checkpoint.json"
SOURCE = Path("E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex")
MUTABLE = {"goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md"}
FILES = [
    "notes/458-gaussian-all-row-large-sieve-comparison.md",
    "reviews/2026-10-07/hybrid-gaussian-all-row-large-sieve-review-radial.md",
    "reviews/2026-10-07/hybrid-gaussian-all-row-large-sieve-review-twisted.md",
    "scripts/hybrid_gaussian_all_row_checkpoint.py",
    "goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md",
]
OTHER_REVIEWS = [
    "reviews/2026-10-07/hybrid-distinct-two-two-prime-review-radial.md",
    "reviews/2026-10-07/hybrid-one-three-mixed-prime-review-twisted.md",
    "reviews/2026-10-07/hybrid-three-column-reflection-review-mixed.md",
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


def build():
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    records = previous["previous_frozen_files_verified"] + [
        r for r in previous["files"] if r["path"] not in MUTABLE
    ]
    frozen = [verify(r) for r in {r["path"]: r for r in records}.values()]
    frozen.append(binding(PREVIOUS.relative_to(ROOT).as_posix()))
    drafts = [verify(r) for r in previous["preexisting_uncommitted_drafts_not_in_this_commit"]]
    source = canonical(SOURCE)
    assert hashlib.sha256(source).hexdigest() == previous["source_preserved_read_only"]["sha256_canonical_lf"]
    source_repo = str(SOURCE.parents[3])
    assert subprocess.check_output(["git", "-C", source_repo, "status", "--porcelain"], text=True).rstrip() == ""
    assert subprocess.check_output(["git", "-C", source_repo, "rev-parse", "HEAD"], text=True).strip() == "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
    note_hash = binding(FILES[0])["sha256_canonical_lf"]
    for review in FILES[1:3]:
        assert note_hash in canonical(ROOT / review).decode("utf-8"), (review, "review does not bind current note")
    links = 0
    for name in FILES:
        path = ROOT / name
        data = canonical(path).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", data), name
        if path.suffix == ".md":
            # Historical indices are preserved; check the new leading section.
            scan = "\n## ".join(data.split("\n## ", 2)[:2]) if name in MUTABLE else data
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", scan):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                candidate = re.sub(r":\d+$", "", target.split("#", 1)[0])
                resolved = (path.parent / candidate).resolve()
                assert resolved == OUTPUT.resolve() or resolved.exists(), (name, target)
                links += 1
    return {
        "date": "2026-10-07", "base_repository_commit": "01851b2632523ef7d06428a0fd7e53fa4ba11dd6",
        "current_goal_turn": "progress", "goal_status": "active",
        "new_zero_free_boundary": False, "new_proportion": False, "new_paper": False,
        "accepted": ["unmarked Gaussian all-element-row second moment U+(UD)^(2/3)+D U^(1/3), with fixed-profile scale supremum, using cited quartic and quadratic large sieves",
                     "actual units, lambda valuations, powerful rows and zero masks retained",
                     "positive H powers show fourth-power amplification does not improve this large-sieve envelope; initial rows must be fourth-power-free"],
        "not_accepted": ["Gaussian near-linear raw moment for every U>=D^(1+c), c>0",
                         "prime-slot extension of the new squarefree-column estimate",
                         "arbitrary-target completed Gaussian theta reflection and quadratic terminal",
                         "new zero-free boundary or critical-line proportion",
                         "root acceptance of other mixed/reflection drafts and their reviews"],
        "unchanged_strict_sigma": previous["unchanged_strict_sigma"],
        "source_preserved_read_only": {"path": str(SOURCE), "sha256_canonical_lf": hashlib.sha256(source).hexdigest(), "external_kernel_run": False},
        "proof_status": "analytic derivation and two independent limited-scope reviews; hash/link checks are not proof-kernel certification",
        "previous_frozen_files_verified": frozen, "files": [binding(name) for name in FILES],
        "preexisting_uncommitted_drafts_not_in_this_commit": drafts,
        "other_reviews_not_accepted_or_in_this_commit": OTHER_REVIEWS,
        "format_verification": {"control_characters_checked": True, "local_links_checked": links},
    }


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {len(result['files'])} current files, {len(result['previous_frozen_files_verified'])} frozen artifacts, read-only source and review bindings")

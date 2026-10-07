"""Bind limited analytic results and reviews; hashes are not proof certification."""

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PREVIOUS = ROOT / "reviews/2026-10-07/gaussian-all-row-large-sieve-checkpoint.json"
OUTPUT = ROOT / "reviews/2026-10-07/joint-and-fourth-checkpoint.json"
SOURCE = Path("E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex")
MUTABLE = {"goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md"}
PREFIX = "reviews/2026-10-07/"
NOTES = [
    "notes/459-natural-inverse-and-primitive-zero-joint-reduction.md",
    "notes/461-original-one-high-three-low-fourth-trace.md",
    "notes/462-original-low-prime-fourth-path-constant.md",
    "notes/463-two-sided-height-stability-for-original-fourth-words.md",
]
REVIEWS = [
    "hybrid-one-three-mixed-prime-sector-research.md",
    "hybrid-one-three-mixed-prime-review-twisted.md",
    "hybrid-distinct-two-two-prime-sector-research.md",
    "hybrid-distinct-two-two-prime-review-radial.md",
    "hybrid-distinct-two-two-prime-review-twisted.md",
    "hybrid-three-column-reflection-research.md",
    "hybrid-three-column-reflection-review-mixed.md",
    "hybrid-mixed-and-three-column-review-root.md",
    "hybrid-natural-inverse-primitive-joint-review-twisted.md",
    "hybrid-natural-primitive-joint-review-compression.md",
    "hybrid-natural-primitive-joint-review-root.md",
    "hybrid-natural-principal-extension-review-compression.md",
    "hybrid-signed-one-three-physical-resonance-research.md",
    "hybrid-signed-one-three-physical-review-radial.md",
    "hybrid-one-three-finite-band-admission-research.md",
    "hybrid-one-three-finite-band-review-radial.md",
    "hybrid-one-three-finite-band-review-compression.md",
    "hybrid-low-prime-exact-fourth-path-constant-research.md",
    "hybrid-low-prime-exact-fourth-review-radial.md",
    "hybrid-low-prime-exact-fourth-review-compression.md",
    "hybrid-two-sided-height-escape-research.md",
    "hybrid-two-sided-height-review-radial.md",
    "hybrid-two-sided-height-review-compression.md",
    "hybrid-field-change-special-mobius-next-research.md",
    "hybrid-field-change-special-mobius-review-radial.md",
    "hybrid-field-change-special-mobius-review-compression.md",
]
FILES = NOTES + [PREFIX + name for name in REVIEWS] + [
    "scripts/hybrid_joint_and_fourth_checkpoint.py",
    "goals/PROGRESS.md", "goals/NEXT.20260909.md", "RESEARCH_BRANCHES.md",
]
ADDITIONAL_FROZEN = [
    ("notes/460-generic-power-row-obstruction-and-field-choice.md",
     "9625c0d618854769de90edfb3ee3b8d8b89e1d3b2b83d676dffccb927e09d85f"),
    (PREFIX + "hybrid-generic-power-row-obstruction-review-radial.md",
     "63130b11339ed28ba44eb050ea13ad751e0af720a05fca64be0b22ee25150b6a"),
    (PREFIX + "hybrid-generic-power-row-obstruction-review-compression.md",
     "6d2c23c0385f69419ee53a5442590b1bd7b4fcffb7d52813d62dfc35454431a1"),
]
REVIEW_PAIRS = {
    NOTES[0]: ["hybrid-natural-inverse-primitive-joint-review-twisted.md",
               "hybrid-natural-primitive-joint-review-compression.md",
               "hybrid-natural-primitive-joint-review-root.md"],
    NOTES[1]: ["hybrid-one-three-finite-band-review-radial.md",
               "hybrid-one-three-finite-band-review-compression.md"],
    NOTES[2]: ["hybrid-low-prime-exact-fourth-review-radial.md",
               "hybrid-low-prime-exact-fourth-review-compression.md"],
    NOTES[3]: ["hybrid-two-sided-height-review-radial.md",
               "hybrid-two-sided-height-review-compression.md"],
    PREFIX + "hybrid-natural-primitive-joint-review-root.md":
              ["hybrid-natural-principal-extension-review-compression.md"],
    PREFIX + "hybrid-signed-one-three-physical-resonance-research.md":
              ["hybrid-signed-one-three-physical-review-radial.md"],
    PREFIX + "hybrid-one-three-finite-band-admission-research.md":
              ["hybrid-one-three-finite-band-review-radial.md",
               "hybrid-one-three-finite-band-review-compression.md"],
    PREFIX + "hybrid-low-prime-exact-fourth-path-constant-research.md":
              ["hybrid-low-prime-exact-fourth-review-radial.md",
               "hybrid-low-prime-exact-fourth-review-compression.md"],
    PREFIX + "hybrid-two-sided-height-escape-research.md":
              ["hybrid-two-sided-height-review-radial.md",
               "hybrid-two-sided-height-review-compression.md"],
    PREFIX + "hybrid-one-three-mixed-prime-sector-research.md":
              ["hybrid-one-three-mixed-prime-review-twisted.md",
               "hybrid-mixed-and-three-column-review-root.md"],
    PREFIX + "hybrid-distinct-two-two-prime-sector-research.md":
              ["hybrid-distinct-two-two-prime-review-radial.md",
               "hybrid-distinct-two-two-prime-review-twisted.md",
               "hybrid-mixed-and-three-column-review-root.md"],
    PREFIX + "hybrid-three-column-reflection-research.md":
              ["hybrid-three-column-reflection-review-mixed.md",
               "hybrid-mixed-and-three-column-review-root.md"],
    PREFIX + "hybrid-field-change-special-mobius-next-research.md":
              ["hybrid-field-change-special-mobius-review-radial.md",
               "hybrid-field-change-special-mobius-review-compression.md"],
}
PENDING = [
    PREFIX + "hybrid-whole-fourth-compression-upper-research-radial.md",
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


def finite_constant_check():
    """Only finite combinatorics and rational arithmetic, not asymptotic proofs."""
    from collections import Counter
    from fractions import Fraction as F
    from itertools import permutations, product
    paired = Counter()
    for p, q in product((2, 3), repeat=2):
        for s, t in product((-1, 1), repeat=2):
            paired.update([
                ((p, s), (p, -s), (q, t), (q, -t)),
                ((p, s), (q, t), (q, -t), (p, -s)),
                ((p, s), (q, t), (p, -s), (q, -t)),
            ])
    exact = Counter()
    for word in product(product((2, 3), (-1, 1)), repeat=4):
        plus = sorted(p for p, s in word if s == 1)
        minus = sorted(p for p, s in word if s == -1)
        if plus == minus:
            exact[word] = 1
    for p in (2, 3):
        for signs in set(permutations((1, 1, -1, -1))):
            paired[tuple((p, s) for s in signs)] -= 1
    assert paired == exact
    # Direct integration after symmetry of max: 2 int_0^b x(1-x) int_0^x y dy dx.
    b = F(1, 2)
    adjacent = b**4/F(4) - b**5/F(5)
    opposite = b**4/F(4) - b**5/F(3)
    assert adjacent == F(3, 320) and opposite == F(1, 192)
    assert 4*adjacent + 8*opposite == F(19, 240)
    return {"balanced_words_checked": len(exact), "flat_low_fourth": "19/240",
            "scope": "finite pairing enumeration and rational integration only"}


def build():
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    records = previous["previous_frozen_files_verified"] + [
        r for r in previous["files"] if r["path"] not in MUTABLE
    ] + [{"path": p, "sha256_canonical_lf": h} for p, h in ADDITIONAL_FROZEN]
    frozen = [verify(r) for r in {r["path"]: r for r in records}.values()]
    frozen.append(binding(PREVIOUS.relative_to(ROOT).as_posix()))
    # Preserve the old snapshot exactly. A single TeX control-space at the end
    # of line 292 is now explicit thin space; no formula or prose changed.
    corrected = PREFIX + "hybrid-three-column-reflection-research.md"
    old_sha = "72c6f95ef52bd6a759da23067e3c3e8d32d1e7278c9fb68adacafed733cefc15"
    new_sha = "30929e068a6b1610a1ea64aea4e5a0d46623b9fd2f7e41c18f77044d7b209878"
    original_line = " {\\cal R}_H=\\{-r\\le\\Re s\\le c,\\ \n"
    corrected_line = " {\\cal R}_H=\\{-r\\le\\Re s\\le c,\\,\n"
    recovered_drafts = []
    for record in previous["preexisting_uncommitted_drafts_not_in_this_commit"]:
        if record["path"] != corrected:
            recovered_drafts.append(verify(record))
            continue
        current = canonical(ROOT / corrected)
        text = current.decode("utf-8")
        assert text.count(corrected_line) == 1
        original = text.replace(corrected_line, original_line).encode("utf-8")
        assert hashlib.sha256(original).hexdigest() == record["sha256_canonical_lf"] == old_sha
        assert len(original) == record["canonical_utf8_bytes"]
        assert hashlib.sha256(current).hexdigest() == new_sha
        recovered_drafts.append(binding(corrected))
    assert all(r["path"] in FILES for r in recovered_drafts)
    source = canonical(SOURCE)
    assert hashlib.sha256(source).hexdigest() == previous["source_preserved_read_only"]["sha256_canonical_lf"]
    source_repo = str(SOURCE.parents[3])
    assert subprocess.check_output(["git", "-C", source_repo, "status", "--porcelain"], text=True).rstrip() == ""
    assert subprocess.check_output(["git", "-C", source_repo, "rev-parse", "HEAD"], text=True).strip() == "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
    review_checks = []
    for name, reviews in REVIEW_PAIRS.items():
        sha = binding(name)["sha256_canonical_lf"]
        for review in reviews:
            target = PREFIX + review
            assert sha in canonical(ROOT / target).decode("utf-8"), (name, target, "review binding")
            review_checks.append({"source": name, "review": target, "sha256_canonical_lf": sha})
    links = 0
    for name in FILES:
        path = ROOT / name
        data = canonical(path).decode("utf-8")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", data), name
        if path.suffix == ".md":
            scan = "\n## ".join(data.split("\n## ", 2)[:2]) if name in MUTABLE else data
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", scan):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                candidate = re.sub(r":\d+$", "", target.split("#", 1)[0])
                resolved = (path.parent / candidate).resolve()
                assert resolved == OUTPUT.resolve() or resolved.exists(), (name, target)
                links += 1
    return {
        "date": "2026-10-07", "base_repository_commit": "8adf98ea84a25cabe925fe39376e1df746f54294",
        "current_goal_turn": "progress", "goal_status": "active",
        "new_zero_free_boundary": False, "new_proportion": False, "new_paper": False,
        "accepted": [
            "entire original finite-matrix one-high-three-low fourth trace o(N), relative to stated [R] theta<9/10",
            "entire original low-genuine-prime fourth trace path constant, flat 19/240, without new [R] or whole-fourth precondition",
            "two-sided height-band stability in trace norm for any original prime fourth word, without [R] or whole-fourth precondition",
            "natural/primitive inverse recovery with fixed original profiles, masks, heights, residues and joins; strict joint-budget equivalence but no strict saving",
            "explicit ordinary principal inverse extension, separately reviewed; no principal plain-column residue deletion",
            "limited repeated13/31, distinct22 reductions and ordinary three-column reflection; their unproved joint budgets remain open",
            "fourth-power Gaussian Mobius subfamily saving under explicit fixed-target reciprocal control; stated Dirichlet norm-base-change specialization of [R] only",
            "actual fixed-profile small-scale supremum has a unit-ideal Omega(U) baseline; whole Gaussian raw still requires primitive joint energy",
        ],
        "not_accepted": [
            "whole fourth-moment constant, higher zero proportion or new zero-free boundary",
            "entire original 31, distinct22 or high all-distinct upper budget",
            "free removal of internal finite projections using height stability",
            "strict primitive joint saving or uniform inverse/L-prime bounds from a zero-free region",
            "Gaussian near-linear special Mobius raw estimate or arbitrary-target completed theta reflection",
            "the pending whole-fourth compression-upper research report",
        ],
        "unchanged_strict_sigma": previous["unchanged_strict_sigma"],
        "source_preserved_read_only": {"path": str(SOURCE), "sha256_canonical_lf": hashlib.sha256(source).hexdigest(), "external_kernel_run": False},
        "proof_status": "analytic derivations and independent limited-scope reviews; hash, link and finite checks are not proof-kernel certification",
        "previous_frozen_files_verified": frozen,
        "previous_drafts_now_accepted_with_limited_scope": recovered_drafts,
        "previous_draft_snapshots_verified": previous["preexisting_uncommitted_drafts_not_in_this_commit"],
        "format_corrections": [{"path": corrected, "old_sha256_canonical_lf": old_sha,
                                "new_sha256_canonical_lf": new_sha,
                                "change": "one TeX control-space replaced by explicit thin space on line 292; original snapshot reconstructed and verified; four review hash references updated"}],
        "files": [binding(name) for name in FILES],
        "review_bindings": review_checks,
        "pending_not_accepted_or_in_this_commit": [binding(name) for name in PENDING],
        "finite_verification": finite_constant_check(),
        "format_verification": {"control_characters_checked": True, "local_links_checked": links},
    }


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {len(result['files'])} current files, {len(result['previous_frozen_files_verified'])} frozen artifacts, read-only source and {len(result['review_bindings'])} review bindings")

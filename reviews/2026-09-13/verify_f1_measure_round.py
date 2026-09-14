"""Verify this round's saved bytes and links, not its mathematical conclusions."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = ROOT.parent
OUT = "reviews/2026-09-13/f1-measure-round-validation.json"
BASE = "73b68d6a67bbad98162dedcc6227c58afcb21c0a"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def long_term(raw):
    return raw.split("### B. 较远期目标方向".encode(), 1)[1].split(
        "### D. 保存、动态修订及停止纪律".encode(), 1
    )[0]


def main():
    subprocess.run(["python", "scripts/sync_goal.py", "--check"], cwd=ROOT, check=True)
    subprocess.run(["python", "scripts/check_repo_layout.py"], cwd=ROOT, check=True)
    subprocess.run(["python", "reviews/2026-09-06/verify_artifacts.py"], cwd=ROOT, check=True)
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    subprocess.run(["git", "diff", "--cached", "--check"], cwd=ROOT, check=True)
    assert not git("diff", "--name-only", BASE, "--", "formal").strip()

    archives = {
        "archive/GOAL.20260906.md": "213a099265b8a88d5eb5ef6a9f0d5af0d595a8e52c6d1cb0e0f658929366e568",
        "archive/GOAL.20260909.f1-periodic.md": "d3e4bfecdfd18507cbe92e0579ce6f6c44d7fd83211a0914fc80167e7abbafd5",
        "archive/GOAL.20260909.f1-real-scales.md": "3a7823c197fd60e29325b22b068cb959a6dbb54ac603a99dd6003eaec8647c23",
    }
    for relative, sha in archives.items():
        assert digest((WORKSPACE / relative).read_bytes()) == sha, relative
    assert long_term((WORKSPACE / "GOAL.20260909.md").read_bytes()) == long_term(
        (WORKSPACE / "archive/GOAL.20260909.f1-real-scales.md").read_bytes()
    )
    assert digest((ROOT / "reviews/2026-09-10/frozen-control-closure.json").read_bytes()) == (
        "39f10f8bcb3d68012f74dac7839ebb9d6afad1892428366b11b5236103f5f875"
    )

    staged = [x for x in git("diff", "--cached", "--name-only", "-z").decode().split("\0") if x and x != OUT]
    forbidden = {
        "reviews/2026-09-08/control-prefix-curvature-budget.json",
        "reviews/2026-09-08/radius-five-continuous-period-pressure.json",
        "scripts/control_prefix_curvature_budget.py",
        "scripts/radius_five_continuous_period_pressure.py",
    }
    assert not forbidden.intersection(staged)
    for name in staged:
        # Respect .gitattributes: goal mirrors intentionally preserve raw CRLF.
        expected_oid = git("hash-object", "--path=" + name, name).strip()
        assert git("rev-parse", ":" + name).strip() == expected_oid, name

    docs = {ROOT / x for x in staged if x.endswith(".md")}
    docs.update(ROOT / x for x in ("README.md", "RESEARCH_BRANCHES.md", "goals/NEXT.20260909.md", "goals/PROGRESS.md", "goals/GOAL.20260909.md", "literature/README.md"))
    docs.update(p for p in (ROOT / "notes").glob("*.md") if p.name[:3].isdigit() and 365 <= int(p.name[:3]) <= 389)
    link_count = 0
    for path in docs:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not re.search(r"\.(?:md|pdf|json|py|lean|tex|toml|txt|png|svg|html|cpp|ya?ml)$", target) and not target.endswith("/"):
                continue  # Avoid mathematical expressions such as ](m).
            assert (path.parent / unquote(target)).exists(), (path, target)
            link_count += 1

    library = json.loads((ROOT / "literature/manifest.json").read_text(encoding="utf-8"))
    artifacts = [e for e in library["entries"] + library.get("supplement_provenance", []) if e.get("file") and e.get("sha256")]
    source = next(e for e in library["entries"] if e.get("id") == "Baker-Rumely-2006-draft-archive20070417")
    report = {
        "status": "PASS_SAVED_MEASURE_ROUND",
        "date": "2026-09-15",
        "mathematical_review_date": "2026-09-13",
        "base_commit": BASE,
        "checked_document_links": link_count,
        "goal_mirrors": 19,
        "long_term_goal_bytes_unchanged": True,
        "unchanged_lean_sources": 11,
        "git_index_checked_blobs": len(staged),
        "literature_artifacts_verified": len(artifacts),
        "new_source": {k: source[k] for k in ("file", "sha256", "bytes", "pages")},
        "document_sha256_raw": {str(p.relative_to(ROOT)).replace('\\', '/'): digest(p.read_bytes()) for p in sorted(docs)},
        "new_notes": [388, 389],
        "next_task_is_unproved": "reviews/2026-09-13/f1-section-dimension-next-proof-plan.md",
        "scope": "Saved bytes, source integrity, reference targets, and preserved boundaries only. Direct mathematical/source review scope is recorded separately. No RH/RR/priority certification.",
    }
    (ROOT / OUT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "checked_document_links", "git_index_checked_blobs", "literature_artifacts_verified")}, ensure_ascii=False))


if __name__ == "__main__":
    main()

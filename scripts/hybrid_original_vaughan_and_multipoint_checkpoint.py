#!/usr/bin/env python3
"""Bind the reviewed original Vaughan reduction and replayed MT proportion.

This checkpoint verifies exact finite algebra, source bytes, review bindings,
local links, and previously completed cover records. It does not recompute
the seven-point cover, certify analytic inputs, or prove a new zero-free strip.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
R = "reviews/2026-10-08/"
FILES = [
    "notes/477-original-vaughan-reduction-and-replayed-multipoint-proportion.md",
    R+"hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md",
    R+"hybrid-original-vaughan-type-i-and-type-ii-reduction-review-twisted.md",
    R+"hybrid-multipoint-spectral-envelope-source-read-root.md",
    R+"hybrid-multipoint-spectral-envelope-source-review-radial.md",
    R+"hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md",
    R+"hybrid-original-multipoint-envelope-and-actual-counting-review-radial.md",
    R+"477-summary-review-twisted.md",
    "scripts/hybrid_multipoint_cap_replay.py",
    "output/hybrid-multipoint-cap-exact-algebra.json",
    "output/hybrid-multipoint-seven-primary-replay.json",
    "output/hybrid-multipoint-three-rational-replay.json",
    R+"artifacts/hybrid-multipoint-ainta-040c5e8/source-manifest.json",
    R+"artifacts/hybrid-multipoint-schwarz-e2453c1/source-manifest.json",
]
PAIRS = [
    (FILES[2], FILES[1]),
    (FILES[4], FILES[3]),
    (FILES[6], FILES[5]),
    (FILES[7], FILES[0]),
]
OLD = {
    "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md":
        "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
    "scripts/mt_triple_slack_audit.py":
        "597e950849415d979f236611a1ed623c4e2aff2e19dc73c801b5f5a244f0bf34",
}
OUT = ROOT / "output/hybrid-original-vaughan-and-multipoint-checkpoint.json"


def canonical(p):
    return p.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def build():
    checks = []
    def require(ok, label):
        if not ok:
            raise AssertionError(label)
        checks.append(label)

    snapshots = {}
    for name in FILES + list(OLD):
        p = ROOT/name
        require(p.is_file(), "file exists: "+name)
        b = canonical(p)
        snapshots[name] = {"canonical_sha256": sha(b),
                           "canonical_bytes": len(b), "lines": len(b.splitlines())}
    for name, expected in OLD.items():
        require(snapshots[name]["canonical_sha256"] == expected,
                "old frozen source unchanged: "+name)
    for review, source in PAIRS:
        require(snapshots[source]["canonical_sha256"] in
                (ROOT/review).read_text("utf-8"), "review binds final source: "+source)
    link_count = 0
    for name in FILES[:8]:
        p = ROOT/name
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", p.read_text("utf-8")):
            if re.match(r"^[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            require((p.parent/target).resolve().exists(), "local link: "+name+" -> "+target)
            link_count += 1

    artifact_files = {}
    for name in FILES[-2:]:
        p = ROOT/name
        manifest = json.loads(p.read_text("utf-8"))
        for entry in manifest["files"]:
            raw = (p.parent/entry["path"]).read_bytes()
            expected = entry.get("raw_sha256", entry.get("sha256_raw"))
            require(sha(raw) == expected, "raw upstream source: "+entry["path"])
            require(len(raw) == entry["bytes"], "raw upstream size: "+entry["path"])
            artifact_files[str((p.parent/entry["path"]).relative_to(ROOT)).replace("\\", "/")] = expected

    def record(name):
        return json.loads((ROOT/name).read_text("utf-8"))
    seven = record(FILES[10])
    three = record(FILES[11])
    algebra = record(FILES[9])
    runner = snapshots[FILES[8]]["canonical_sha256"]
    for data in (seven, three, algebra):
        require(data["result"]["verified"] is True, "complete record: "+data["mode"])
        require(data["provenance"]["runner_canonical_sha256"] == runner,
                "record binds current runner: "+data["mode"])
        require(data["scope"]["new_zeta_proportion_certified_by_script"] is False,
                "analytic scope preserved: "+data["mode"])
    v = seven["result"]
    require((v["grid"], v["precision_bits"], v["nodes"], v["maximum_depth"]) ==
            (4000, 128, 707901, 37), "full seven replay parameters")
    require(v["nodes"] == v["initial_boxes"]+2*v["splits"], "seven binary tree nodes")
    require(v["pruned"] == v["initial_boxes"]+v["splits"], "seven complete leaf count")
    require(v["pruned"] == sum(v["details"][k] for k in
            ("pressure_pruned", "interval_pruned", "tangent_pruned")), "seven pruning partition")
    require(v["initial_boxes"] == 3**6, "all surviving six-coordinate components")
    require(v["kernel_table_sha256"] ==
            "a9992300d2bf71665aa2b6bd2727e798624cd297103bb200c7f0ca2baea55a2c",
            "normalized MT table binding")
    t = three["result"]
    require(Q(t["minimum_leaf_lower_bound"]) >= Q(221, 1000000), "rational three target")
    require((t["visited_boxes"]-1) % 4 == 0, "three quadtree node count")
    splits = (t["visited_boxes"]-1)//4
    require(t["leaves"]+t["outside_boxes"] == 3*splits+1, "three complete cover leaf count")

    iv = {k: tuple(Q(x) for x in val)
          for k, val in algebra["result"]["intervals"].items()}
    require(Q(45600, 4000*3000) == Q(19, 5000), "exact pressure cutoff")
    require(Q(6, 3000) == Q(1, 500), "aggregated six-window pressure")
    m = 280
    A = Q(19, 5000)*(m-6)
    require(A == Q(2603, 2500), "m280 exact energy budget")
    rad = Q(m-1, m)*A
    require(rad == Q(726237, 700000), "m280 exact radicand")
    cl, cu = iv["m280_envelope_cost"]
    roots = tuple((c-A/m+1)/2 for c in (cl, cu))
    require(0 < roots[0] <= roots[1], "positive square-root interval")
    require(roots[0]**2 <= rad <= roots[1]**2, "rational square-root enclosure")
    pl, pu = iv["p280_known_envelope"]
    hl, hu = iv["C0"]
    require(pl == (m*hl-Q(m-1,500))/(m-cl), "p280 rational lower formula")
    require(pu == (m*hu-Q(m-1,500))/(m-cu), "p280 rational upper formula")
    require(0 < pl <= pu < 1, "legal proportion interval")
    require(pl > Q(6730096522791369, 10**16), "displayed p280 strict lower truncation")
    require(pl > iv["p270"][1] > iv["p269"][1], "strict two spectral assembly gains")
    require(pu < Q(6730266625438475, 10**16), "below cited Schwarz enhanced candidate")
    require(pu < Q(673316977, 10**9), "below cited later public candidate")
    require((1+pl)/2 > Q(8365048261395684, 10**16), "distinct lower truncation")
    a, h, r, n = sp.symbols("a h r n")
    y = (2+4*a)/3
    require(sp.simplify((2*y-1)-(4*a+1-y)) == 0, "fixed-cut matching powers")
    require(sp.simplify((2*y-1)-(1+8*a)/3) == 0, "fixed-cut common exponent")
    require((2*y-1).subs(a, sp.Rational(1,8)) == sp.Rational(2,3), "Type I two thirds")
    require((2*y-1).subs(a, sp.Rational(1,7)) == sp.Rational(5,7), "Type I five sevenths threshold")
    require(sp.Rational(5,7)-sp.Rational(2,3) == sp.Rational(1,21), "paid-part power gap")
    left = h+2*r+r*r+(h+r)**2/(n-h)
    right = n*(1+r)**2/(n-1)+(h-1)*(n+r)**2/((n-h)*(n-1))
    require(sp.cancel(left-right) == 0, "multi-large-eigenvalue exact identity")
    snapshots[str(Path(__file__).relative_to(ROOT)).replace("\\", "/")] = {
        "canonical_sha256": sha(canonical(Path(__file__)))}
    return {
        "schema": "hybrid-original-vaughan-and-multipoint-v1",
        "exact_checks": len(checks), "checks": checks,
        "files": snapshots, "raw_artifacts": artifact_files,
        "review_pairs": [list(pair) for pair in PAIRS], "local_links_checked": link_count,
        "rational_p280_interval": [str(pl), str(pu)],
        "outcomes": {
            "actual_type_i_and_low_part_two_thirds_paid": True,
            "complete_original_type_ii_reduction": True,
            "full_seven_certificate_replayed_in_frozen_record": True,
            "actual_proportion_cited_input_derivation_in_reviewed_sources": True,
            "new_spectral_mechanism": False,
            "new_full_fourth_growth_power": False,
            "whole_fourth_constant_paid": False,
            "whole_signed_near_paid": False,
            "new_zero_free_boundary": False,
            "new_boundary_paper": False,
            "world_record_claim": False,
            "analytic_proof_certified_by_script": False,
            "full_kernel_recomputed_by_this_checkpoint": False,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    if args.check:
        if not OUT.is_file() or json.loads(OUT.read_text("utf-8")) != data:
            raise AssertionError("checkpoint changed or absent")
    else:
        if OUT.exists():
            raise AssertionError("refuse overwrite frozen checkpoint")
        OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", "utf-8")
    print("PASS: exact checks=%d; links=%d; reviewed file snapshot=%d" %
          (data["exact_checks"], data["local_links_checked"], len(data["files"])))


if __name__ == "__main__":
    main()

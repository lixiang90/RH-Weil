#!/usr/bin/env python3
"""Bind the reviewed whole-chain MT proof, complete kernel cover and exact p.

This checks finite algebra, frozen dependencies, review bindings and links.
It reads completed cover records; it does not rerun the kernel or seven-point
cover, certify the analytic zero-correlation input, or prove a zero-free strip.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
R = "reviews/2026-10-08/"
NOTE = "notes/478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md"
SOURCE = R + "hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-research-compression.md"
RADIAL = R + "hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-review-radial.md"
TWISTED = R + "hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-review-twisted.md"
MOBIUS = R + "hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md"
MOBIUS_REVIEW = R + "hybrid-short-mobius-twist-and-vaughan-zero-residue-review-twisted.md"
KERNEL = "scripts/hybrid_mt_six_neighbor_geometry_certificate.py"
KERNEL_OUT = "output/hybrid-mt-six-neighbor-geometry-certificate.json"
ALGEBRA = "output/hybrid-multipoint-cap-exact-algebra.json"
SEVEN = "output/hybrid-multipoint-seven-primary-replay.json"
FILES = [NOTE, SOURCE, RADIAL, TWISTED, MOBIUS, MOBIUS_REVIEW, KERNEL, KERNEL_OUT]
PAIRS = [(RADIAL, SOURCE), (TWISTED, SOURCE), (TWISTED, NOTE), (MOBIUS_REVIEW, MOBIUS)]
FROZEN = {
    "notes/304-mt-triple-geometry-and-second-moment-stability.md":
        "03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4",
    "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md":
        "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
    "notes/477-original-vaughan-reduction-and-replayed-multipoint-proportion.md":
        "9c2da25b665070fe5496b9b02cbe382208cd3b60dc793af1ae018ede395bd6b5",
    R + "hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md":
        "59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa",
    "scripts/hybrid_multipoint_cap_replay.py":
        "8ac87f18cf928a51771556168e5af07400a3ba0333196b3e410394d8e4c37d05",
    ALGEBRA: "d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3",
    SEVEN: "aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6",
}
OUT = ROOT / "output/hybrid-mt-six-neighbor-proportion-checkpoint.json"


def canonical(path):
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def build():
    checks = []
    def require(ok, label):
        if not ok:
            raise AssertionError(label)
        checks.append(label)
    snapshots = {}
    for name in FILES + list(FROZEN):
        path = ROOT / name
        require(path.is_file(), "file exists: " + name)
        data = canonical(path)
        snapshots[name] = {"canonical_sha256": sha(data), "canonical_bytes": len(data),
                           "lines": len(data.splitlines())}
    for name, expected in FROZEN.items():
        require(snapshots[name]["canonical_sha256"] == expected, "frozen unchanged: " + name)
    for review, source in PAIRS:
        require(snapshots[source]["canonical_sha256"] in (ROOT / review).read_text("utf-8"),
                "review binds final source: " + source)
    link_count = 0
    for name in FILES[:6]:
        path = ROOT / name
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text("utf-8")):
            if re.match(r"^[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            resolved = (path.parent / target).resolve()
            # The note links the checkpoint being built, without a hash cycle.
            require(resolved == OUT or resolved.exists(), "local link: " + name + " -> " + target)
            link_count += 1
    def record(name):
        return json.loads((ROOT / name).read_text("utf-8"))
    kernel = record(KERNEL_OUT)
    require(kernel["script_canonical_sha256"] == snapshots[KERNEL]["canonical_sha256"],
            "kernel record binds final script")
    require(kernel["original_seven_output_canonical_sha256"] == FROZEN[SEVEN],
            "kernel binds original seven record")
    result = kernel["result"]
    require(result["verified"] is True, "completed entire-axis kernel record")
    require((result["grid"], result["precision_bits"], result["complete_closed_cells"]) ==
            (40000, 128, 241910), "complete compact kernel cover parameters")
    require(result["cell_counts_by_strongest_radius"] == [38090] * 5 + [51460],
            "complete radius partition")
    require(sum(result["cell_counts_by_strongest_radius"]) == result["complete_closed_cells"],
            "all closed cells accounted")
    require(result["closed_cell_ball_sha256"] ==
            "42d5d94ab916327d36705f6ee1385a7779ad931cb4ade50989579891f2f7bc5e",
            "closed-cell ball digest")
    require(Q(result["certified_margin_each_cell"]) == Q(1, 10**8), "strict cell margin")
    bounds = [Q(x) for x in result["kernel_bounds_by_radius"]]
    require(bounds == [Q(x, 10000) for x in (1805, 1064, 757, 588, 480, 406)],
            "certified six half-line bounds")
    require(sum(bounds) == Q(51, 100), "exact six kernel bound sum")
    sep = Q(result["separation"])
    require(sep == Q(3809, 4000) and 0 < sep < 1, "short-cluster monotone interval")
    require((7 - sep) * 40000 == 241910, "compact domain cell count")
    tail = Q(141125, 3619653)
    require(Q(result["infinite_tail_rational_bound"]) == tail < bounds[-1],
            "entire infinite-tail rational budget")
    tail_t = Q(157, 50) * 7
    require((Q(5, 6) * tail_t + Q(1, 2)) / (tail_t**2 - Q(1, 2)) == tail,
            "tail exact rational formula")
    u = Q(50, 51)
    require([Q(x) for x in result["weights_by_radius"]] == [u] * 6, "final uniform dual weights")
    require(Q(result["row_sum"]) == 2 * u * sum(bounds) == 1, "closed Schur feasibility")
    c = 2 * u - u * u
    require(c == Q(result["efficiency"]) == Q(2600, 2601), "dual edge efficiency")
    alpha, eta = c * Q(19, 5000), c / 500
    require(alpha == Q(result["node_charge"]) == Q(247, 65025), "whole-chain node charge")
    require(eta == Q(result["pressure"]) == Q(26, 13005), "whole-chain span pressure")
    require(Q(2, 3) * Q(1, 10)**2 == Q(result["cluster_per_node_charge"]) == Q(1, 150)
            and Q(1, 150) > alpha, "all nontrivial clusters paid per node")
    small_error = Q(1, 10000)
    require(0 < alpha - 2 * small_error < alpha < Q(2, 3) * (Q(1, 10) - small_error)**2,
            "fixed-profile cluster and singleton margin")
    require(kernel["scope"]["floating_point_acceptance"] is False and
            kernel["scope"]["analytic_zero_transfer_proved_by_script"] is False,
            "finite kernel scope preserved")
    seven = record(SEVEN)
    require(seven["result"]["verified"] is True and seven["result"]["nodes"] == 707901,
            "frozen seven-point complete record")
    require(seven["provenance"]["runner_canonical_sha256"] ==
            FROZEN["scripts/hybrid_multipoint_cap_replay.py"], "seven runner binding")
    require(Q(6, 3000) == Q(1, 500), "all-window aggregate gap pressure")
    algebra = record(ALGEBRA)
    require(algebra["result"]["verified"] is True, "frozen rational algebra completion")
    iv = {key: tuple(Q(x) for x in val) for key, val in algebra["result"]["intervals"].items()}
    c0 = iv["C0"]
    require(0 < c0[0] <= c0[1] < 1 and 0 < alpha < 1, "valid proportion parameters")
    p = tuple((h - eta) / (1 - alpha) for h in c0)
    require(p == tuple((65025 * h - 130) / 64778 for h in c0), "exact p6 formula")
    require(p[0] == Q(14836092823842124897870604079776674894402895,
                      22042811164404551786230480320215081201696768), "author rational lower interval")
    require(p[1] == Q(7418046411921062448935302039888337450550235,
                      11021405582202275893115240160107540600848384), "author rational upper interval")
    require(p[0] > Q(6730581101107434, 10**16), "strict simple-zero lower truncation")
    require(p[0] > iv["p280_known_envelope"][1], "strict actual project proportion gain")
    gain = p[0] - iv["p280_known_envelope"][1], p[1] - iv["p280_known_envelope"][0]
    require(gain[0] > Q(48457831, 10**12), "strict gain above 0.000048457831")
    require(p[1] < Q(673316977, 10**9), "below recorded higher public candidate")
    distinct = tuple((1 + x) / 2 for x in p)
    require(distinct[0] > Q(8365290550553717, 10**16), "strict distinct-zero lower truncation")
    snapshots[str(Path(__file__).relative_to(ROOT)).replace("\\", "/")] = {
        "canonical_sha256": sha(canonical(Path(__file__)))}
    return {"schema": "hybrid-mt-six-neighbor-proportion-v1", "exact_checks": len(checks),
            "checks": checks, "files": snapshots, "review_pairs": [list(x) for x in PAIRS],
            "local_links_checked": link_count, "rational_p6_interval": [str(x) for x in p],
            "rational_distinct_interval": [str(x) for x in distinct],
            "rational_gain_interval": [str(x) for x in gain],
            "outcomes": {"complete_kernel_cover_in_frozen_record": True,
                         "whole_chain_geometry_proved_in_reviewed_sources": True,
                         "actual_proportion_cited_input_derivation_in_reviewed_sources": True,
                         "original_short_mobius_twist_cited_strip_derivation_reviewed": True,
                         "original_vaughan_zero_residue_preserved": True,
                         "new_full_fourth_growth_power": False, "whole_fourth_constant_paid": False,
                         "whole_signed_near_paid": False, "new_zero_free_boundary": False,
                         "new_boundary_paper": False, "world_record_claim": False,
                         "analytic_proof_certified_by_script": False,
                         "full_kernel_recomputed_by_this_checkpoint": False,
                         "seven_cover_recomputed_by_this_checkpoint": False}}


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
        OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print("PASS: exact checks=%d; links=%d; source snapshots=%d" %
          (len(data["checks"]), data["local_links_checked"], len(data["files"])))


if __name__ == "__main__":
    main()

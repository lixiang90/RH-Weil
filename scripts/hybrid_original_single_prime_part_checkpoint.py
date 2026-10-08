#!/usr/bin/env python3
"""Check exact subfamily costs, moment transfers and frozen proof bindings.

Infinite estimates are supplied by the separately reviewed mathematical sources.
This checker neither proves them by enumeration nor reruns the finite kernel cover.
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
NOTE = "notes/480-original-type-ii-single-prime-part-and-whole-moment-transfer.md"
SOURCE = R + "hybrid-original-type-ii-small-single-prime-part-fourth-research-radial.md"
SOURCE_REVIEW = R + "hybrid-original-type-ii-small-single-prime-part-fourth-review-checkpoint-audit.md"
NOTE_REVIEW = R + "hybrid-original-single-prime-part-note-review-checkpoint-audit.md"
SCRIPT = "scripts/hybrid_original_single_prime_part_checkpoint.py"
SCRIPT_REVIEW = R + "hybrid-original-single-prime-part-checkpoint-review-checkpoint-audit.md"
GROWTH = "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md"
GROWTH_SOURCE = R + "hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md"
GROWTH_REVIEW = R + "hybrid-ivic-density-and-scalar-fourth-growth-review-root.md"
PACKET = R + "hybrid-positive-height-zero-packet-fourth-upper-research-radial.md"
SAMPLING = R + "hybrid-fixed-start-half-gram-sampling-research-root.md"
OLD = "output/hybrid-original-type-ii-factor-checkpoint.json"
OUT = ROOT / "output/hybrid-original-single-prime-part-checkpoint.json"
FILES = [NOTE, SOURCE, SOURCE_REVIEW, NOTE_REVIEW, SCRIPT, SCRIPT_REVIEW]
PAIRS = [(SOURCE_REVIEW, SOURCE), (NOTE_REVIEW, NOTE),
         (SCRIPT_REVIEW, SCRIPT), (GROWTH_REVIEW, GROWTH_SOURCE),
         (GROWTH_REVIEW, PACKET), (GROWTH_REVIEW, SAMPLING)]
FROZEN = {
    OLD: "88ff98918fa6fda62996e848e120a7ffdf0030472b9709c94cb9f61ac5f09b1e",
    NOTE: "13a6cbd697ad960cdb97543090861373f21b6970710bc2d247edac59bb08e791",
    SOURCE: "f0b740a85b09f70b68653bf3ec06288150876f1f761920ffb1107620fbf44580",
    SOURCE_REVIEW: "2066698dfe4079c6a174369cd48e05986d52a14177466f7b38b25fad4c2adb2f",
    GROWTH: "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
    GROWTH_SOURCE: "a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d",
    GROWTH_REVIEW: "061342dfe685c5cd59114f07444ed36eba3e68905e30f11505a46e3fcc088767",
    PACKET: "8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481",
    SAMPLING: "7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc",
}


def canonical(path):
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def build():
    checks, snapshots = [], {}
    def require(ok, label):
        if not ok:
            raise AssertionError(label)
        checks.append(label)

    require(hashlib.sha256(canonical(ROOT / OLD)).hexdigest() == FROZEN[OLD],
            "published 479 checkpoint unchanged")
    old = json.loads((ROOT / OLD).read_text("utf-8"))
    for name in dict.fromkeys(FILES + list(old["files"]) + list(FROZEN)):
        path = ROOT / name
        require(path.is_file(), "file exists: " + name)
        data = canonical(path)
        snapshots[name] = {"canonical_sha256": hashlib.sha256(data).hexdigest(),
                           "canonical_bytes": len(data), "lines": len(data.splitlines())}
    for name, snap in old["files"].items():
        require(snapshots[name]["canonical_sha256"] == snap["canonical_sha256"],
                "published dependency unchanged: " + name)
    for name, expected in FROZEN.items():
        require(snapshots[name]["canonical_sha256"] == expected, "frozen source: " + name)
    for review, source in PAIRS:
        require(snapshots[source]["canonical_sha256"] in (ROOT / review).read_text("utf-8"),
                "review binds final source: " + source)

    links = 0
    for name in FILES[:4] + [SCRIPT_REVIEW, GROWTH, GROWTH_SOURCE, GROWTH_REVIEW]:
        path = ROOT / name
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text("utf-8")):
            if re.match(r"^[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            require(resolved == OUT or resolved.exists(), "local link: " + name + " -> " + target)
            links += 1

    # All costs below are exact identities/inequalities, not analytic tests.
    v, s, b, c = Q(1, 8), Q(1, 20), Q(5, 7), Q(17, 24)
    d = max(2*s, 1 + 4*s - 4*v)
    require(d == Q(7, 10), "original small-single-prime-part cost is 7/10")
    require(Q(2)**4 == 16, "floor lower bound for V costs at most factor 16")
    require(Q(1, 20) + 4*Q(1, 20) + Q(1, 2) == Q(3, 4),
            "prefix, coefficient and dyad loss is 3/4 of final epsilon")
    require(Q(3, 4) < 1, "fixed epsilon allocation has positive margin")
    require(c-d == Q(1, 120), "subfamily fourth-power gap is 1/120")
    require(c/4-d/4 == Q(1, 480), "subfamily norm gap is 1/480")
    require(b-c == Q(1, 168), "whole exponent dominates old assembled error")
    transfer = lambda cost: (3*b+cost)/4
    require(transfer(c) == Q(479, 672), "PH to R1 transfer exponent is 479/672")
    require(transfer(d) == Q(199, 280), "R0 to R1 transfer exponent is 199/280")
    require(b-transfer(c) == Q(1, 672), "PH transfer growth-scale gap is 1/672")
    require(b-transfer(d) == Q(1, 280), "R0 transfer growth-scale gap is 1/280")

    # An affine formula is represented by (constant, coefficient of fixed delta).
    add = lambda x, y: (x[0]+y[0], x[1]+y[1])
    scale = lambda k, x: (k*x[0], k*x[1])
    at = lambda x, delta: x[0]+x[1]*delta
    a_delta = (Q(3, 56), Q(-1))
    small_delta = scale(2, a_delta)
    d_delta = add((1-4*v, Q(0)), scale(4, a_delta))
    require(d_delta == (b, Q(-4)), "general family cost is B-4delta")
    dominance = add(d_delta, scale(-1, small_delta))
    require(dominance == (Q(17, 28), Q(-2)), "two family costs differ by 17/28-2delta")
    require(at(dominance, Q(0)) > 0 and at(dominance, Q(3, 56)) > 0,
            "affine cost dominance holds throughout closed endpoint interval")
    r0_transfer = scale(Q(1, 4), add((3*b, Q(0)), d_delta))
    require(r0_transfer == (b, Q(-1)), "R0 to Rdelta transfer is B-delta")
    threshold = (b-c)/4
    require(threshold == Q(1, 672), "assembled error switch occurs at delta=1/672")
    require(at(d_delta, threshold) == c, "two error branches agree at switch")
    require(d_delta[1] < 0, "general error decreases with fixed delta")
    require(r0_transfer == (b, Q(-1)) and transfer(c) == b-threshold,
            "PH transfer branches are exactly B-min(delta,1/672)")
    require(Q(0) < threshold < Q(1, 280) < Q(3, 56), "both fixed examples lie in open family domain")
    require(at(a_delta, Q(1, 280)) == s and at(d_delta, Q(1, 280)) == d,
            "delta=1/280 recovers original cutoff and 7/10 cost")
    require(at(r0_transfer, Q(1, 280)) == Q(199, 280),
            "delta=1/280 recovers original R0 transfer")
    sharp = at(a_delta, threshold)
    require(sharp == Q(5, 96), "largest cutoff retaining old error has exponent 5/96")
    require(sharp-s == Q(1, 480), "cutoff power grows by 1/480")
    require(Q(1, 2)+4*sharp == c, "sharp-cut subfamily cost equals 17/24")
    require(2*sharp < c and Q(0) < sharp < v, "sharp cutoff is in uniform counting domain")
    require((c-Q(1, 2))/4 == sharp,
            "within this monotone cost family, a<=5/96 iff dominant cost<=17/24")
    require(at(r0_transfer, threshold) == Q(479, 672),
            "sharp-cut R0 transfer also has exponent 479/672")

    def qstr(x):
        return str(x.numerator) + "/" + str(x.denominator)
    costs = {"S_original_power": s, "D_original_fourth": d,
             "assembled_fourth": c, "whole_growth": b,
             "PH_to_R1_additive": transfer(c), "R0_to_R1_additive": transfer(d),
             "S_sharp_power": sharp, "cutoff_power_gain": sharp-s,
             "D_sharp_fourth": c, "PH_to_Rsharp_additive": transfer(c),
             "R0_to_Rsharp_additive": at(r0_transfer, threshold),
             "PH_growth_scale_gap": threshold, "R0_original_growth_scale_gap": Q(1, 280)}
    return {"schema": "original-single-prime-part-checkpoint-v1",
            "exact_checks": len(checks), "checks": checks, "files": snapshots,
            "review_pairs": [list(pair) for pair in PAIRS], "local_links_checked": links,
            "rational_costs": {name: qstr(value) for name, value in costs.items()},
            "fixed_delta_family": {"domain": "0<delta<3/56, fixed before X tends to infinity",
                                   "S_power": "3/56-delta", "D_fourth": "5/7-4delta",
                                   "R0_additive": "5/7-delta",
                                   "PH_additive": "5/7-min(delta,1/672)"},
            "preserved_p_dg_interval": old["rational_p_dg_interval"],
            "scope": ["Exact costs, affine-family identities, local links and final source/review hashes only.",
                      "All 27 published 479 snapshots are inherited unchanged; their finite covers are not rerun.",
                      "Infinite subfamily and Holder bounds are separately reviewed, not certified by this script.",
                      "Whole transfers additionally use the original R_7/8 and the published 476 growth input.",
                      "No new whole growth exponent, constant fourth moment, zero proportion or zero-free boundary."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="read-only compare with saved output")
    args = parser.parse_args()
    result = build()
    if args.check:
        if json.loads(OUT.read_text("utf-8")) != result:
            raise SystemExit("FAIL: saved checkpoint differs from current exact checks or bindings")
        print("PASS: saved checkpoint and current proof bindings agree")
    else:
        OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("WROTE: " + str(OUT.relative_to(ROOT)))
    print(f"{result['exact_checks']} checks; {len(result['files'])} snapshots; "
          f"{result['local_links_checked']} local links; {len(result['review_pairs'])} review bindings")


if __name__ == "__main__":
    main()

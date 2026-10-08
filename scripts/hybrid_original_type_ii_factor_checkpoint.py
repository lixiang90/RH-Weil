#!/usr/bin/env python3
"""Check exact costs, p_dg, frozen inputs and final review bindings.

The analytic estimates are in separately reviewed mathematical sources.
This does not certify them by enumeration or rerun the frozen kernel cover.
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
NOTE = "notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md"
FACTOR = R + "hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md"
FACTOR_T = R + "hybrid-original-type-ii-short-lambda-factor-fourth-review-twisted.md"
GAUGE = R + "hybrid-mt-six-neighbor-diagonal-gauge-and-actual-counting-research-compression.md"
GAUGE_T = R + "hybrid-mt-six-neighbor-diagonal-gauge-and-actual-counting-review-twisted.md"
REVIEW = R + "hybrid-original-type-ii-factor-checkpoint-review-checkpoint-audit.md"
SCRIPT = "scripts/hybrid_original_type_ii_factor_checkpoint.py"
OLD = "output/hybrid-mt-six-neighbor-proportion-checkpoint.json"
ALGEBRA = "output/hybrid-multipoint-cap-exact-algebra.json"
OUT = ROOT / "output/hybrid-original-type-ii-factor-checkpoint.json"
FILES = [NOTE, FACTOR, FACTOR_T, GAUGE, GAUGE_T, REVIEW, SCRIPT]
PAIRS = [(FACTOR_T, FACTOR), (GAUGE_T, GAUGE),
         (REVIEW, NOTE), (REVIEW, SCRIPT)]
FROZEN = {
    OLD: "1d92dd0f51c361043d58207c62e50efc647671c52ce8c4f746830c40a0ea8c63",
    FACTOR: "b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0",
    GAUGE: "361c32d6e28cfd2e5c30516b42e58297f11f4516c77407de39c5f32b8af7c30b",
    GAUGE_T: "b0878550dfeb1b2443772a47a197fd424f721d12fa14176a9c74c432b4c25416",
    R + "hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md":
        "cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4",
    R + "hybrid-original-vaughan-type-i-and-type-ii-reduction-review-twisted.md":
        "576a0841b5a5ad9bf8fbda74561bb83ca3d16654a0c2faac5f4aa80269fb296f",
    R + "hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md":
        "f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7",
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
            "published 478 checkpoint unchanged")
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
    for name in FILES[:-1]:
        path = ROOT / name
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text("utf-8")):
            if re.match(r"^[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            require(resolved == OUT or resolved.exists(), "local link: " + name + " -> " + target)
            links += 1

    a, b, y = Q(1, 8), Q(1, 4), Q(5, 6)
    short = Q(1, 3) + a + b
    type_i = Q(1, 3) + 2*a
    sf, pp = max(Q(0), 1-4*a), max(Q(0), 1-2*b)
    lower = 2*y-1
    require(0 < a < b and a+b < y < 1, "frozen legal cuts and Y/M>V")
    require(y-a-b == Q(11, 24), "expanded sharp inner lower length")
    require(short == Q(17, 24) and short/2 == Q(17, 48), "short-family fourth and sup costs")
    require(type_i == Q(7, 12), "original Type I fourth cost")
    require(sf == pp == Q(1, 2), "two sparse-family fourth costs")
    require(lower == Q(2, 3), "unchanged lower block cost")
    error = max(short, type_i, sf, pp, lower)
    require(error == Q(17, 24) and error/4 == Q(17, 96), "assembled error function L4 cost")
    require(Q(5, 7)-short == Q(1, 168) > 0, "strict family margin below whole baseline")
    require(lower-type_i == Q(1, 12) > 0 and short > lower, "Type I improvement and coupling limit")
    require(Q(8, 21)-a == Q(43, 168) > b, "fixed-a short-factor cost frontier")

    iv = json.loads((ROOT / ALGEBRA).read_text("utf-8"))["result"]["intervals"]
    c0 = tuple(Q(x) for x in iv["C0"])
    e, S, tau, h = Q(1, 62500), Q(51, 50), Q(19, 5000), Q(1, 500)
    u = (1+e)/S
    c = 2*u-u*u
    alpha, eta = c*tau-e*e, c*h
    require(u == Q(62501, 63750) and -e+u*S == 1, "one-sided dual upper feasibility")
    require(c == Q(4062502499, 4064062500), "diagonal-gauge edge efficiency")
    require(alpha == Q(77187542279, 20320312500000), "complete node charge with e squared cost")
    require(eta == Q(4062502499, 2032031250000), "complete span pressure")
    require(6*c*tau-6*alpha == 6*e*e > 0, "endpoint charge is 6 c tau, not 6 alpha")
    require(alpha-2*(1+e)/10000 == Q(36561707377, 10160156250000) > 0,
            "fixed-profile singleton error paid")
    require(Q(2, 3)*(Q(1, 10)-Q(1, 10000))**2-alpha ==
            Q(232041622759, 81281250000000) > 0, "fixed-profile short-cluster margin")
    p = tuple((x-eta)/(1-alpha) for x in c0)
    require(0 < c0[0] < c0[1] < 1 and 0 < alpha < 1, "valid exact interval and denominator")
    require(p == tuple((20320312500000*x-40625024990)/20243124957721 for x in c0),
            "exact actual p_dg formula")
    require(p[0] == Q(144883718717093990038447236655639983274406783850455,
                      215261827327800757567083368853099932747578493370368), "strict author lower")
    require(p[1] == Q(72441859358546995019223618327819991669906394854915,
                      107630913663900378783541684426549966373789246685184), "strict author upper")
    old_p = tuple(Q(x) for x in old["rational_p6_interval"])
    gain = p[0]-old_p[1], p[1]-old_p[0]
    require(gain[0] == Q(38202658750375724709585783275561655495674769405,
                         223107690410244439578888423481057719096362234296731172864) > 0,
            "new strict lower exceeds old strict upper")
    u0 = 1/S
    c_old = 2*u0-u0*u0
    dc = c-c_old
    require(dc == 2*u0*(1-u0)*e-u0*u0*e*e, "exact efficiency increment")
    for x in c0:
        numerator = dc*(tau*x-h)-(x-h*c_old)*e*e
        require(numerator > 0 and (x-eta)/(1-alpha)-(x-h*c_old)/(1-tau*c_old) ==
                numerator/((1-alpha)*(1-tau*c_old)), "exact same-budget gain identity")
    require(p[0] > Q(6730581102819731, 10**16), "strict displayed simple proportion")
    return {"schema": "hybrid-original-type-ii-factor-v1", "exact_checks": len(checks),
            "checks": checks, "files": snapshots, "review_pairs": [list(x) for x in PAIRS],
            "local_links_checked": links,
            "rational_costs": {"short_m": str(short), "type_i": str(type_i),
                               "squarefull_k": str(sf), "large_proper_power_m": str(pp),
                               "lower_block": str(lower), "assembled_error": str(error)},
            "rational_p_dg_interval": [str(x) for x in p],
            "rational_distinct_interval": [str((1+x)/2) for x in p],
            "rational_gain_interval": [str(x) for x in gain],
            "scope": {"original_factor_subfamilies_proved_in_reviewed_sources": True,
                      "actual_mt_diagonal_gain_proved_in_reviewed_sources": True,
                      "remaining_large_prime_m_non_squarefull_k_paid": False,
                      "new_whole_fourth_growth_power": False, "whole_fourth_constant_paid": False,
                      "new_joint_kappa_feedback": False, "new_zero_free_boundary": False,
                      "new_boundary_paper": False, "world_record_claim": False,
                      "analytic_proof_certified_by_script": False,
                      "frozen_kernel_or_seven_cover_recomputed": False}}


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
    print("PASS: exact checks=%d; links=%d; source snapshots=%d" %
          (len(data["checks"]), data["local_links_checked"], len(data["files"])))


if __name__ == "__main__":
    main()

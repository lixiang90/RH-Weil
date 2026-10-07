#!/usr/bin/env python3
"""Replay fully read, pinned finite kernel certificates into NEW outputs.

This runner has no network operations and writes no source or bytecode.
It validates exact archived module bytes before importing them.  A complete
cover is required; terminal or resource failures raise without writing PASS.
The algebra mode uses exact rational intervals only.  Neither mode certifies
the analytic AF trace/inertia/zero counting transfer or a world record.
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True
import argparse
from dataclasses import asdict
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import factorial, isqrt
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "reviews/2026-10-08/artifacts/hybrid-multipoint-ainta-040c5e8"
COMMIT = "040c5e899e658aed7b56a2a87f501798fe10761d"
EXPECTED = {
    "__init__.py": "fed3f612069c72d4efac4250c6b1e63733762bf5911a973a445c1908d7b4b5d1",
    "constants.py": "8344ed3792603e51a5621a72fc04e0f5bcb115c6599a72579b7a0f4b89c0bbff",
    "kernel.py": "e83aa966699770bc72f67d3e55079cff89c2432a05ad25abd12afc8cbf9af1dd",
    "report.py": "6305c3a072a3839aff80ad9854fc8e1e259df86078b8a20821fa778b966833fc",
    "rounding.py": "2419f77bae2fb73ccb1da4e5d2bbaf3247e7d900d53871de9011296f7de5844e",
    "verify_three.py": "ef2b91bb3323fba459cc5e0b2be2e9408da7a39ba9c56517833c6e3c7109ab20",
    "verify_seven.py": "66ff0b10d18125144521f110afb5c0de9f9201e04c7e6ad6ad6cc6311080c355",
}
LICENSE_SHA = "1f157d0f9ab2186d23b5a573e160090b50b580bea1a56b29c4472693dccc81aa"
RATIONAL_SOURCE = ROOT / "scripts/mt_triple_slack_audit.py"
RATIONAL_SHA = "597e950849415d979f236611a1ed623c4e2aff2e19dc73c801b5f5a244f0bf34"
OUTPUTS = {
    "seven": "output/hybrid-multipoint-seven-primary-replay.json",
    "arb-three": "output/hybrid-multipoint-three-primary-replay.json",
    "rational-three": "output/hybrid-multipoint-three-rational-replay.json",
    "algebra": "output/hybrid-multipoint-cap-exact-algebra.json",
}


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def canonical(path):
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def validate_archive():
    manifest = json.loads((ARCHIVE / "source-manifest.json").read_text("utf-8"))
    require(manifest["source_commit"] == COMMIT, "pinned source commit")
    listed = {Path(f["path"]).name: f for f in manifest["files"]}
    require(set(listed) == set(EXPECTED), "complete module manifest")
    for name, expected in EXPECTED.items():
        raw = (ARCHIVE / "zeta_simple_zeros" / name).read_bytes()
        require(sha(raw) == expected, "unmodified archived module: " + name)
        require(listed[name]["raw_sha256"] == expected, "manifest hash: " + name)
        require(listed[name]["bytes"] == len(raw), "manifest size: " + name)
    require(sha((ARCHIVE / "LICENSE").read_bytes()) == LICENSE_SHA, "MIT license")
    return {"source_commit": COMMIT, "raw_module_hashes": EXPECTED,
            "license_raw_sha256": LICENSE_SHA,
            "manifest_canonical_sha256": sha(canonical(ARCHIVE / "source-manifest.json"))}


def rational_module():
    require(sha(canonical(RATIONAL_SOURCE)) == RATIONAL_SHA, "frozen rational source")
    spec = importlib.util.spec_from_file_location("frozen_mt_rational_source", RATIONAL_SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rational_three(max_depth, max_nodes, max_seconds):
    start = time.perf_counter()
    module = rational_module()
    kernel = module.RationalKernel()
    scale = kernel.scale
    target = Q(221, 1000000)
    stack = [(0, 0, 0)]
    visited = leaves = pruned = deepest = 0
    least = None
    while stack:
        i, j, depth = stack.pop()
        visited += 1
        require(visited <= max_nodes, "node limit reached; NOT certified")
        if visited % 512 == 0:
            require(time.perf_counter() - start <= max_seconds,
                    "time limit reached; NOT certified")
        denominator = 1 << depth
        if i + j > denominator:
            pruned += 1
            continue
        require(depth + 1 < kernel.bits, "exact dyadic centers")
        ca = 2 * (2 * i + 1) * scale // denominator
        cb = 2 * (2 * j + 1) * scale // denominator
        radius = module.ceildiv(2 * kernel.pi[1], denominator)
        sq = 0
        for center, error in ((ca, radius), (cb, radius), (ca + cb, 2 * radius)):
            lo, hi = kernel.kernel(center)
            lo, hi = lo - error, hi + error
            distance = lo if lo > 0 else (-hi if hi < 0 else 0)
            sq += distance * distance
        if target.denominator * sq >= target.numerator * scale * scale:
            leaves += 1
            deepest = max(deepest, depth)
            least = sq if least is None else min(least, sq)
            continue
        require(depth < max_depth, "depth limit reached; NOT certified")
        stack.extend((2 * i + di, 2 * j + dj, depth + 1)
                     for di in (0, 1) for dj in (0, 1))
    require(leaves > 0 and not stack, "complete nonempty cover")
    lower = Q(least, scale * scale)
    require(lower >= target, "global rational target")
    return {"certificate": "rational-three-point", "verified": True,
            "domain": "a,b>=0; a+b<=4", "target": str(target),
            "visited_boxes": visited, "leaves": leaves, "outside_boxes": pruned,
            "maximum_leaf_depth": deepest, "cached_centers": len(kernel.cache),
            "bits": kernel.bits, "sinc_last_index": kernel.terms,
            "minimum_leaf_lower_bound": str(lower),
            "rational_source_canonical_sha256": RATIONAL_SHA,
            "elapsed_seconds": time.perf_counter() - start}


def exact_algebra():
    module = rational_module()
    k = module.RationalKernel()
    scale, m = k.scale, k.terms
    x2 = k.mul(k.beta, k.beta)
    term = total = (scale, scale)
    for index in range(1, m + 1):
        term = k.div_integer(k.neg(k.mul(term, x2)), (2 * index - 1) * (2 * index))
        total = k.add(total, term)
    height = max(abs(x) for x in k.beta)
    remainder = module.ceildiv(height ** (2 * m + 2),
                              scale ** (2 * m + 1) * factorial(2 * m + 2))
    cosine = total[0] - remainder, total[1] + remainder
    ratio = k.divide_positive(cosine, k.sinc(k.beta))
    c0 = (Q(3, 2) - Q(ratio[1], scale), Q(3, 2) - Q(ratio[0], scale))
    tau = Q(19, 5000)
    require(Q(45600, 4000 * 3000) == tau, "integer local pressure cutoff")
    require(Q(6, 3000) == Q(1, 500), "six window charges")
    budgets = {n: tau * (n - 6) for n in (269, 270, 271, 280)}
    require(budgets[269] == Q(4997, 5000), "old budget")
    require(budgets[270] == Q(627, 625), "270 budget")
    require(Q(270, 269) - budgets[270] == Q(87, 168125), "270 cap slack")
    require(budgets[271] - Q(271, 270) == Q(89, 27000), "271 cap failure")
    def cap_p(n):
        return tuple((n * c - Q(n - 1, 500)) / (n - budgets[n]) for c in c0)
    p269, p270 = cap_p(269), cap_p(270)
    require(p270[0] > p269[1], "strict new cap improvement by intervals")
    n = 280
    radicand = Q(n - 1, n) * budgets[n]
    root = isqrt(radicand.numerator * scale * scale // radicand.denominator)
    require(Q(root * root, scale * scale) <= radicand
            <= Q((root + 1) ** 2, scale * scale), "rational square-root enclosure")
    cost = tuple(budgets[n] / n + 2 * Q(r, scale) - 1 for r in (root, root + 1))
    require(0 < cost[0] <= cost[1] < n, "known spectral-envelope cost")
    p280 = ((n * c0[0] - Q(n - 1, 500)) / (n - cost[0]),
            (n * c0[1] - Q(n - 1, 500)) / (n - cost[1]))
    require(p280[0] > p270[1], "strict envelope improvement by intervals")
    intervals = {"C0": c0, "p269": p269, "p270": p270,
                 "p280_known_envelope": p280, "m280_envelope_cost": cost}
    return {"verified": True, "certificate": "exact rational interval algebra",
            "local_target": str(tau), "local_pressure": "1/3000",
            "aggregate_pressure": "1/500",
            "budgets": {str(n): str(a) for n, a in budgets.items()},
            "intervals": {key: [str(a), str(b)] for key, (a, b) in intervals.items()},
            "decimal_display_only": {key: [float(a), float(b)]
                                     for key, (a, b) in intervals.items()},
            "analytic_transfer_certified_by_script": False,
            "known_envelope_proof_certified_by_script": False}


def without_runtime(value):
    if isinstance(value, dict):
        return {k: without_runtime(v) for k, v in value.items()
                if k not in ("elapsed_seconds", "seconds")}
    if isinstance(value, list):
        return [without_runtime(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=OUTPUTS)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--max-depth", type=int, default=28)
    parser.add_argument("--max-nodes", type=int, default=2000000)
    parser.add_argument("--max-seconds", type=float, default=600)
    args = parser.parse_args()
    output = ROOT / OUTPUTS[args.mode]
    if args.check:
        require(output.is_file(), "existing NEW output required for check")
    else:
        require(not output.exists(), "refuse to overwrite any output")
    provenance = validate_archive()
    provenance["runner_canonical_sha256"] = sha(canonical(Path(__file__)))
    if args.mode in ("seven", "arb-three"):
        sys.path.insert(0, str(ARCHIVE))
        import flint
        provenance["python_flint_version"] = flint.__version__
        if args.mode == "seven":
            from zeta_simple_zeros.verify_seven import verify_seven
            result = asdict(verify_seven(progress_every=100000))
        else:
            from zeta_simple_zeros.verify_three import verify_three
            result = asdict(verify_three(progress_every=100000))
    elif args.mode == "rational-three":
        result = rational_three(args.max_depth, args.max_nodes, args.max_seconds)
    else:
        result = exact_algebra()
    require(result["verified"], "completed certificate only")
    data = {"schema": "hybrid-multipoint-cap-replay-v1", "mode": args.mode,
            "provenance": provenance, "result": result,
            "scope": {"finite_kernel_certificate": True,
                      "original_AF_analytic_transfer_certified_by_script": False,
                      "new_zeta_proportion_certified_by_script": False,
                      "world_record_claim": False}}
    if args.check:
        old = json.loads(output.read_text("utf-8"))
        require(without_runtime(old) == without_runtime(data), "exact deterministic replay")
        print("PASS complete replay --check: " + str(output.relative_to(ROOT)), flush=True)
    else:
        output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", "utf-8")
        print(json.dumps({"status": "PASS complete finite replay",
                          "output": str(output.relative_to(ROOT)), "result": result},
                         sort_keys=True), flush=True)


if __name__ == "__main__":
    main()

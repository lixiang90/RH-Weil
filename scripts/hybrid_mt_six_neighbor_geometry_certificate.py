#!/usr/bin/env python3
"""Complete real-axis MT kernel bounds for a NEW six-neighbor spectral dual.

Exact rational parameters, Arb closed-cell enclosures, and a monotone rational
tail cover the entire half-line.  No optimization or floating-point samples
accept cells.  This finite kernel certificate does not prove the imported
seven-point inequality or the analytic zero-counting theorem by itself.
"""
from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time
from flint import arb, ctx, fmpq
import flint

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-mt-six-neighbor-geometry-certificate.json"
SEVEN = ROOT / "output/hybrid-multipoint-seven-primary-replay.json"
SEVEN_SHA = "aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6"
GRID = 40000
SEP = Q(3809, 4000)
END = 7
BOUNDS = [Q(n, 10000) for n in (1805, 1064, 757, 588, 480, 406)]
WEIGHTS = [Q(50, 51)] * 6


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def canonical(path):
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def ball(q):
    return arb(fmpq(q.numerator, q.denominator))


def finite_certificate():
    started = time.perf_counter()
    require(sha(canonical(SEVEN)) == SEVEN_SHA, "frozen original seven-point output")
    seven = json.loads(SEVEN.read_text("utf-8"))
    require(seven["result"]["verified"]
            and seven["result"]["target"] == "F6 >= 19/5000", "original local target")
    ctx.prec = 128
    beta = arb(2).sqrt() / 2
    pi = arb.pi()
    mt_alpha = beta * beta.cos() / beta.sin()
    require(0 < mt_alpha < ball(Q(5, 6)), "exact MT endpoint coefficient bound")
    require(pi > ball(Q(157, 50)), "rational pi lower bound")
    sep_cells = SEP * GRID
    require(sep_cells.denominator == 1, "separation on exact grid")
    first = sep_cells.numerator
    stop = END * GRID
    counts = [0] * 6
    digest = hashlib.sha256()
    margin = ball(Q(1, 100000000))
    for index in range(first, stop):
        # Exact closed cell [index/GRID,(index+1)/GRID].
        x = arb(fmpq(2 * index + 1, 2 * GRID), fmpq(1, 2 * GRID))
        t = pi * x
        denominator = t * t - arb(fmpq(1, 2))
        require(denominator > 0, "outside removable singularities")
        value = (mt_alpha * t * t.sin() - arb(fmpq(1, 2)) * t.cos()) / denominator
        radius_index = min(6, index // first) - 1
        require(radius_index >= 0, "applicable separation radius")
        upper = value.abs_upper()
        require(upper + margin < ball(BOUNDS[radius_index]),
                "unresolved closed cell: " + str(index))
        counts[radius_index] += 1
        digest.update((str(index) + ":" + str(value) + "\n").encode("utf-8"))
        if (index - first + 1) % 50000 == 0:
            print("kernel closed cells completed=" + str(index - first + 1), flush=True)
    require(sum(counts) == stop - first, "all compact closed cells")
    # For x>=7, t=pi*x>=1099/50 and alpha_MT<5/6.  The bound
    # (alpha*t+1/2)/(t^2-1/2) is decreasing for t>sqrt(1/2).
    # Its derivative numerator is -alpha*t^2-t-alpha/2 < 0.
    tail_t = Q(157, 50) * END
    tail_bound = (Q(5, 6) * tail_t + Q(1, 2)) / (tail_t * tail_t - Q(1, 2))
    require(tail_bound < BOUNDS[-1], "entire infinite tail")
    endpoint_t = pi * ball(SEP)
    endpoint = (mt_alpha * endpoint_t * endpoint_t.sin()
                - arb(fmpq(1, 2)) * endpoint_t.cos()) / (
                    endpoint_t * endpoint_t - arb(fmpq(1, 2)))
    require(endpoint > ball(Q(1, 10)), "positive short-cluster endpoint")
    require(0 < SEP < 1, "monotonicity on [0,separation]")
    row_sum = 2 * sum((u * m for u, m in zip(WEIGHTS, BOUNDS)), Q())
    require(row_sum == Q(1), "closed Schur norm budget")
    efficiency = 2 * WEIGHTS[-1] - WEIGHTS[-1] ** 2
    require(all(2 * u - u * u == efficiency for u in WEIGHTS), "uniform edge efficiency")
    require(efficiency == Q(2600, 2601), "uniform efficiency")
    node_charge = efficiency * Q(19, 5000)
    pressure = efficiency / 500
    cluster_charge = Q(2, 3) * Q(1, 10) ** 2
    require(node_charge == Q(247, 65025), "whole-chain node charge")
    require(pressure == Q(26, 13005), "whole-chain pressure")
    require(cluster_charge == Q(1, 150) > node_charge, "all short clusters paid")
    return {
        "verified": True, "precision_bits": ctx.prec, "grid": GRID,
        "separation": str(SEP), "compact_interval": [str(SEP), str(END)],
        "complete_closed_cells": stop - first, "cell_counts_by_strongest_radius": counts,
        "closed_cell_ball_sha256": digest.hexdigest(),
        "certified_margin_each_cell": "1/100000000",
        "kernel_bounds_by_radius": [str(m) for m in BOUNDS],
        "weights_by_radius": [str(u) for u in WEIGHTS],
        "infinite_tail_rational_bound": str(tail_bound),
        "short_cluster_kernel_lower": "1/10", "row_sum": str(row_sum),
        "efficiency": str(efficiency), "node_charge": str(node_charge),
        "pressure": str(pressure), "cluster_per_node_charge": str(cluster_charge),
        "elapsed_seconds": time.perf_counter() - started,
    }


def without_runtime(value):
    if isinstance(value, dict):
        return {k: without_runtime(v) for k, v in value.items() if k != "elapsed_seconds"}
    if isinstance(value, list):
        return [without_runtime(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    require(OUTPUT.is_file() if args.check else not OUTPUT.exists(),
            "check existing new output, or refuse any overwrite")
    result = finite_certificate()
    data = {
        "schema": "hybrid-mt-six-neighbor-geometry-v1",
        "script_canonical_sha256": sha(canonical(Path(__file__))),
        "python_flint_version": flint.__version__,
        "original_seven_output_canonical_sha256": SEVEN_SHA,
        "result": result,
        "scope": {"complete_real_axis_kernel_bounds": True,
                  "floating_point_acceptance": False,
                  "imported_seven_certificate_reproved_here": False,
                  "analytic_zero_transfer_proved_by_script": False,
                  "world_record_claim": False},
    }
    if args.check:
        old = json.loads(OUTPUT.read_text("utf-8"))
        require(without_runtime(old) == without_runtime(data), "exact full replay consistency")
        print("PASS entire real-axis MT six-neighbor certificate --check", flush=True)
    else:
        OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", "utf-8")
        print(json.dumps({"status": "PASS entire real-axis finite kernel certificate",
                          "output": str(OUTPUT.relative_to(ROOT)), "result": result}),
              flush=True)


if __name__ == "__main__":
    main()

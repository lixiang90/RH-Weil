"""E-only count of negative-offset branches through depth four.

This finite pilot does not settle longer paths or the length-four graph.
"""

import hashlib
import json
import argparse
from pathlib import Path
import time

import numpy as np
from scipy.interpolate import CubicSpline
from fractions import Fraction as F

from radius_five_subaction_grid import exact_profile_as_float

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix-pruning", action="store_true")
    args = parser.parse_args()
    source = ROOT / "reviews/2026-09-08/kernel-curvature-tail-table.json"
    raw = source.read_bytes()
    data = json.loads(raw)
    z = np.array([float(F(v)) for v in data["control_nodes"]])
    q = len(z)
    kernel, alpha, eta = exact_profile_as_float()
    x = np.linspace(0, 640, 320001)
    fast = CubicSpline(x, kernel(x), extrapolate=False)
    delta, loss = float(F(data["delta"])), float(F(data["delta"]))/2
    scalar = 2*fast(z)**2+eta*z/(2*np.pi)-alpha-delta+loss
    words = np.zeros((1,0), dtype=np.int16)
    offsets = np.zeros(1)
    records = []
    start = time.perf_counter()
    for depth in range(1,5):
        kept_words, kept_offsets = [], []
        count, negative_count, minimum, witness = 0, 0, 0., []
        for low in range(0,len(words),64):
            w = words[low:low+64]
            current = np.broadcast_to(scalar[None,:], (len(w),q)).copy()
            threshold = np.zeros_like(current)
            if w.shape[1]:
                prefix = np.cumsum(z[w], axis=1)
                prefix_costs, short_cost = [], np.zeros(len(w))
                for length in range(1,w.shape[1]+1):
                    short_cost = short_cost+scalar[w[:,length-1]]
                    for first in range(length-1):
                        short_cost += 2*fast(np.sum(z[w[:,first:length]],axis=1))**2
                    prefix_costs.append(short_cost.copy())
                assert np.max(abs(short_cost-offsets[low:low+64])) < 1e-14
                for j in range(w.shape[1]):
                    if args.prefix_pruning:
                        prefix_value = current if j == 0 else current+prefix_costs[j-1][:,None]
                        threshold = np.minimum(threshold,prefix_value)
                    current += 2*fast(prefix[:,j,None]+z[None,:])**2
            costs = offsets[low:low+64,None]+current
            negative_count += int(np.sum(costs < 0))
            rows, cols = np.nonzero(costs < threshold)
            count += len(rows)
            if costs.min() < minimum:
                row, col = np.unravel_index(costs.argmin(),costs.shape)
                minimum = float(costs[row,col])
                witness = [float(z[col])]+list(map(float,z[w[row]]))
            if depth < 4:
                kept_words.append(np.column_stack([cols.astype(np.int16),w[rows]]))
                kept_offsets.append(costs[rows,cols])
        records.append(dict(depth=depth, parent_count=len(words),
                            evaluated_extensions=len(words)*q,
                            negative_branch_count=negative_count, retained_branch_count=count,
                            minimum_offset=minimum,
                            minimizing_word=witness))
        print(records[-1],flush=True)
        output = dict(status="E only: negative short-path branching pilot",
                      table_sha256=hashlib.sha256(raw).hexdigest(),
                      profile_sha256=data["profile_sha256"], control_count=q,
                      delta=delta, endpoint_loss=loss, records=records,
                      prefix_pruning=args.prefix_pruning,
                      elapsed_seconds=time.perf_counter()-start,
                      scope="Parents with nonnegative offsets are dominated and omitted. No length-four graph closure, rounding proof or eventual offset floor is certified.")
        name = "finite-control-prefix-pilot.json" if args.prefix_pruning else "finite-control-branching-pilot.json"
        (source.parent/name).write_text(
            json.dumps(output,indent=2)+"\n",encoding="utf-8")
        if depth < 4:
            words, offsets = np.concatenate(kept_words), np.concatenate(kept_offsets)
            if len(words) > 2000000:
                raise RuntimeError("Pilot storage cap reached after a complete level")


if __name__ == "__main__":
    main()

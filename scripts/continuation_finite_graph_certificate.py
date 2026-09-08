"""Strict finite-alphabet certificate using freshly computed Arb values.

All state/edge combinations of one exact ten-symbol alphabet are covered.
This does not certify the surrounding continuous domain.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations_with_replacement
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from radius_five_arb_kernel import Kernel, PROFILE_SHA256, arb, rational, rational_bounds

ROOT = Path(__file__).resolve().parents[1]
SCALE = 10**15


def scaled_bounds(value):
    lo, hi = rational_bounds(value)
    return lo.numerator*SCALE//lo.denominator, -((-hi.numerator*SCALE)//hi.denominator)


def fraction_scaled(value):
    return value.numerator*SCALE//value.denominator, -((-value.numerator*SCALE)//value.denominator)


def main():
    source = ROOT / "reviews/2026-09-08/radius-five-continuation-plans-266.json"
    raw = source.read_bytes()
    candidate = json.loads(raw)
    assert candidate["profile_sha256"] == PROFILE_SHA256
    alpha, eta, delta = [F(candidate[key]) for key in ("alpha", "eta", "delta")]
    alphabet = list(map(F, ["5.7", "6.43", "6.52", "6.56", "6.6", "12.34", "12.43", "12.52", "18.41", "80"]))
    q = len(alphabet)
    plans = [(list(map(F, item["gaps"])), F(item["offset"])) for item in candidate["plans"]]
    assert plans[0] == ([], F(0)) and len(plans) == 266
    assert all(len(w) <= 4 and abs(b) < 1 and all(F("5.7") <= x <= 128 for x in w) for w, b in plans)
    sums = {n: set(map(sum, combinations_with_replacement(alphabet, n))) for n in range(1, 6)}
    queries = set().union(*sums.values())
    for w, _ in plans:
        prefix = F(0)
        for j, x in enumerate(w, 1):
            prefix += x
            for i in range(j-1, len(w)):
                queries.update(s+prefix for s in sums[4-i])
    assert all(F("5.7") <= x <= 640 for x in queries)
    kernel = Kernel(192)
    values = {}
    cache_digest = hashlib.sha256()
    start_time = time.perf_counter()
    for index, x in enumerate(sorted(queries)):
        k = kernel.value(x)
        lo, hi = scaled_bounds(2*k*k)
        lo = max(0, lo)  # 2*k^2 is analytically nonnegative.
        assert 0 <= lo <= hi <= 3*SCALE
        values[x] = (lo, hi)
        cache_digest.update(f"{x}:{lo}:{hi}\n".encode())
        if (index+1) % 10000 == 0:
            print(f"Arb scalar enclosures {index+1}/{len(queries)}", flush=True)
    # At most 20 energy terms, 4 fees and one offset per plan.
    # Each energy bound <=3*SCALE, every fee/offset absolute bound <=SCALE+1.
    # Thus all intermediate sums/differences below are far inside int64.
    assert 100*SCALE < np.iinfo(np.int64).max
    fees = [scaled_bounds(rational(eta*x)/(2*arb.pi())-rational(alpha+delta)) for x in alphabet]
    assert max(abs(v) for pair in fees for v in pair) <= SCALE
    assert delta*SCALE == int(delta*SCALE)
    delta_scaled = int(delta*SCALE)
    assert 0 <= delta_scaled <= SCALE
    grid100 = np.array([int(x*100) for x in alphabet], dtype=np.int64)
    state_ids = np.arange(q**4, dtype=np.int64)
    state_digits = np.column_stack([(state_ids//q**j) % q for j in range(3, -1, -1)])
    state_gaps = grid100[state_digits]
    field_cache = {}

    def field(integer_sum, offset=F(0)):
        unique, inverse = np.unique(integer_sum, return_inverse=True)
        key = (tuple(map(int, unique)), offset)
        if key not in field_cache:
            field_cache[key] = np.array([values[F(int(v), 100)+offset] for v in unique], dtype=np.int64)
        return field_cache[key][inverse]

    internal = np.zeros((q**4, 2), dtype=np.int64)
    h = np.zeros_like(internal)
    for m in range(1, 5):
        internal += np.array(fees, dtype=np.int64)[state_digits[:, m-1]]
        partial = np.cumsum(state_gaps[:, m-1:], axis=1)
        for column in range(partial.shape[1]):
            internal += field(partial[:, column])
        for w, b in plans:
            if len(w) != m:
                continue
            bpair = np.array(fraction_scaled(b), dtype=np.int64)
            value = internal+bpair
            prefix = F(0)
            for j, x in enumerate(w, 1):
                prefix += x
                for i in range(j-1, m):
                    value += field(state_gaps[:, i:].sum(axis=1), prefix)
            # Bounds for the minimum use the minimum of all lower endpoints
            # and the minimum of all upper endpoints, including the empty plan.
            h = np.minimum(h, value)
    assert np.all(h[:, 0] <= h[:, 1])
    edge_ids = np.arange(q**5, dtype=np.int64)
    digits = np.column_stack([(edge_ids//q**j) % q for j in range(4, -1, -1)])
    gaps = grid100[digits]
    cost = np.array(fees, dtype=np.int64)[digits[:, 0]]+delta_scaled
    partial = np.cumsum(gaps, axis=1)
    for column in range(5):
        cost += field(partial[:, column])
    head, tail = edge_ids//q, edge_ids % q**4
    lower = cost[:, 0]+h[tail, 0]-h[head, 1]
    upper = cost[:, 1]+h[tail, 1]-h[head, 0]
    target = F(1, 200000)  # 0.000005.
    assert np.all(lower <= upper)
    worst = int(np.argmin(lower))
    assert int(lower[worst])*target.denominator > target.numerator*SCALE
    output = dict(status="PASS: every edge of the exact ten-symbol graph has R > 0.000005",
                  scope="Finite alphabet only. No all-real-gap subaction or actual zero bound is certified.",
                  candidate_sha256=hashlib.sha256(raw).hexdigest(), profile_sha256=PROFILE_SHA256,
                  arithmetic_script_sha256=hashlib.sha256((ROOT/"scripts/radius_five_arb_kernel.py").read_bytes()).hexdigest(),
                  certificate_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  plans=len(plans), alphabet=[str(x) for x in alphabet],
                  states=q**4, edges=q**5, scalar_queries=len(queries),
                  scalar_bounds_sha256=cache_digest.hexdigest(),
                  arb_precision_bits=192, integer_denominator=str(SCALE),
                  strict_threshold=str(target),
                  minimum_lower_numerator=str(int(lower[worst])),
                  corresponding_upper_numerator=str(int(upper[worst])),
                  worst_word=[str(F(int(x), 100)) for x in gaps[worst]],
                  max_state_interval_width_numerator=str(int(np.max(h[:, 1]-h[:, 0]))),
                  elapsed_seconds=time.perf_counter()-start_time,
                  overflow_guard="100*SCALE < int64 maximum; all scalar, fee, offset and summand bounds checked")
    (source.parent / "continuation-finite-graph-certificate.json").write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: all {q**5} exact alphabet edges > {target}; min lower {int(lower[worst])}/{SCALE}.", flush=True)


if __name__ == "__main__":
    main()

"""Adversarial floating search of a frozen exact continuation candidate.

This can locate witnesses for subsequent rigorous checking; success of a
search never certifies a real box or the compact domain.
"""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize

from radius_five_continuation_plan_search import Plans
from radius_five_subaction_grid import exact_profile_as_float
from radius_five_stopped_continuation import StoppedPlans

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", default="radius-five-continuation-plans-266.json")
    parser.add_argument("--iterations", type=int, default=220)
    parser.add_argument("--stopped", action="store_true")
    args = parser.parse_args()
    path = ROOT / "reviews/2026-09-08" / args.candidate
    raw = path.read_bytes()
    data = json.loads(raw)
    profile = ROOT / "reviews/2026-09-08" / data["profile_source"]
    assert hashlib.sha256(profile.read_bytes()).hexdigest() == data["profile_sha256"]
    kernel, alpha, eta = exact_profile_as_float()
    assert alpha == float(data["alpha"]) and eta == float(data["eta"])
    candidate_class = StoppedPlans if args.stopped else Plans
    plans = candidate_class(kernel, alpha, eta, float(data["delta"]))
    for item in data["plans"][1:]:
        plans.add(list(map(float, item["gaps"])), float(item["offset"]))
    assert len(plans.items) == len(data["plans"])

    def objective(v):
        ar = np.asarray(v)
        g = ar[None, :] if ar.ndim == 1 else ar.T
        values = plans.residual(g)
        return float(values[0]) if ar.ndim == 1 else values

    records = []
    bounds_list = [
        [(5.7, 13.5)]*5,
        [(5.7, 21.)]*5,
        [(5.7, 52.)]+[(5.7, 128.)]*4,
        [(6.3, 6.8), (12.1, 12.8), (6.3, 6.8), (5.7, 128.), (5.7, 128.)],
        [(12.1, 12.8), (6.3, 6.8), (5.7, 128.), (5.7, 128.), (5.7, 128.)],
    ]
    suffix = "-stopped-pressure.json" if args.stopped else "-continuous-pressure.json"
    output_path = path.with_name(path.stem+suffix)
    for i, bounds in enumerate(bounds_list):
        result = differential_evolution(
            objective, bounds, seed=826600+i, maxiter=args.iterations,
            popsize=10, vectorized=True, updating="deferred", polish=False,
            tol=1e-9, atol=1e-11)
        polished = minimize(objective, result.x, bounds=bounds, method="Nelder-Mead",
                             options={"maxiter": 1200, "xatol": 1e-9, "fatol": 1e-12})
        point = polished.x if polished.fun < result.fun else result.x
        direct = float(plans.residual(point[None, :], exact=True)[0])
        head, head_id = plans.value(point[None, :4], exact=True)
        tail, tail_id = plans.value(point[None, 1:], exact=True)
        records.append(dict(bounds=bounds, seed=826600+i,
                            word=[str(float(v)) for v in point],
                            spline_residual=objective(point),
                            all_plan_original_kernel_residual=direct,
                            head_plan=int(head_id[0]), tail_plan=int(tail_id[0]),
                            head_value=float(head[0]), tail_value=float(tail[0]),
                            differential_evolution_success=bool(result.success),
                            local_success=bool(polished.success)))
        output = dict(status="E only: adversarial floating search of an unchanged candidate",
                      candidate=args.candidate,
                      candidate_sha256=hashlib.sha256(raw).hexdigest(),
                      profile_sha256=data["profile_sha256"], plan_count=len(plans.items),
                      iterations_per_DE=args.iterations, searches=records,
                      stopped_branches=args.stopped,
                      scope="All-plan direct double evaluation at saved points; no domain coverage or strict sign proof")
        output_path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
        print(f"search {i}: R={direct:+.12e}; head={head_id[0]}, tail={tail_id[0]}; {point}", flush=True)


if __name__ == "__main__":
    main()

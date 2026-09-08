"""E-only finite graph and continuous refinement with partial future words."""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from radius_five_partial_continuation import PartialPlans
from radius_five_subaction_grid import exact_profile_as_float

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    source = ROOT / "reviews/2026-09-08/radius-five-continuation-plans-266.json"
    raw = source.read_bytes()
    data = json.loads(raw)
    kernel, alpha, eta = exact_profile_as_float()
    plans = PartialPlans(kernel, alpha, eta, float(data["delta"]))
    output_path = source.with_name("partial-continuation-search.json")
    if args.resume:
        previous = json.loads(output_path.read_bytes())
        assert previous["source_sha256"] == hashlib.sha256(raw).hexdigest()
        for item in previous["plans"]:
            plans.add(item["gaps"], item["offset"])
        history, updates = previous["history"], previous["updates"]
    else:
        for item in data["plans"]:
            if float(item["offset"]) < 0:
                assert len(item["gaps"]) == 4
                plans.add(list(map(float, item["gaps"])), float(item["offset"]))
        history, updates = [], []
    target = 5e-6
    alphabet = np.array([5.7, 6.43, 6.52, 6.56, 6.6, 12.34, 12.43, 12.52, 18.41, 80.])
    q = len(alphabet)
    ids = np.arange(q**4)
    states = alphabet[np.column_stack([(ids//q**j) % q for j in range(3, -1, -1)])]
    ids = np.arange(q**5)
    words = alphabet[np.column_stack([(ids//q**j) % q for j in range(4, -1, -1)])]
    costs = plans.cost(words)

    def graph():
        heights = plans.value(states)[0]
        return costs+heights[ids % q**4]-heights[ids//q]

    def update(word, reason):
        direct = float(plans.residual(word[None, :], exact=True)[0])
        if direct >= target:
            return
        _, tail_ids = plans.value(word[None, 1:], exact=True)
        before = len(plans.items)
        result = plans.extend(word, int(tail_ids[0]))
        updates.append(dict(reason=reason, plans_before=before, tail_id=int(tail_ids[0]),
                            word=list(map(float, word)), direct_residual=direct,
                            added_or_existing_plan_id=int(result)))

    def save():
        output = dict(status="E only: partial-future candidates, no continuous certificate",
                      source_sha256=hashlib.sha256(raw).hexdigest(),
                      profile_sha256=data["profile_sha256"], alpha=alpha, eta=eta,
                      delta=plans.margin, target=target, plans=plans.items,
                      implicit_branches="zero and stopped I_1,I_2,I_3,I_4",
                      branch_definition="I_4 plus cross energies to listed future word plus offset",
                      history=history, updates=updates,
                      scope="All offsets are floating search values. Final candidate is not automatically covered by preceding searches.")
        output_path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")

    for iteration in range(len(history), len(history)+args.rounds):
        entry = dict(iteration=iteration, graph_rounds=[], local_searches=[])
        history.append(entry)
        for j in range(16):
            residual = graph()
            entry["graph_rounds"].append(dict(plans_before=len(plans.items),
                minimum=float(residual.min()), below_target=int(np.sum(residual < target))))
            print(f"iteration {iteration} graph {j}, plans {len(plans.items)}, min {residual.min():+.6e}", flush=True)
            if residual.min() >= target:
                break
            seen = set()
            for index in np.argsort(residual):
                if residual[index] >= target or len(seen) >= 80:
                    break
                head = int(index)//q
                if head not in seen:
                    seen.add(head)
                    update(words[index], f"{iteration}:graph:{j}")
        residual = graph()
        starts, seen = [], set()
        for j in np.argsort(residual):
            key = tuple(np.round(words[j]/3).astype(int))
            if key not in seen:
                starts.append(words[j].copy())
                seen.add(key)
            if len(starts) >= 24:
                break
        for index, start in enumerate(starts):
            count = len(plans.items)
            def objective(v):
                return float(plans.residual(np.asarray(v)[None, :])[0])
            result = minimize(objective, start, method="Nelder-Mead", bounds=[(5.7,128.)]*5,
                              options={"maxiter":1400, "xatol":1e-8, "fatol":1e-12})
            direct = float(plans.residual(result.x[None, :], exact=True)[0])
            entry["local_searches"].append(dict(plans_before=count, initial_word=start.tolist(),
                word=result.x.tolist(), direct_residual=direct, success=bool(result.success)))
            update(result.x, f"{iteration}:local:{index}")
        final = graph()
        entry["after_updates"] = dict(plans=len(plans.items),
                                      graph_minimum=float(final.min()),
                                      below_target=int(np.sum(final < target)),
                                      graph_worst_word=words[final.argmin()].tolist())
        print(f"iteration {iteration} end, plans {len(plans.items)}, graph {final.min():+.6e}; "
              f"earlier local minimum {min(v['direct_residual'] for v in entry['local_searches']):+.6e}", flush=True)
        save()


if __name__ == "__main__":
    main()

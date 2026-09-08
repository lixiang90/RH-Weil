"""E only: propagate new low state values through sampled predecessors."""

from collections import deque
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from radius_five_continuation_plan_search import Plans
from radius_five_subaction_grid import exact_profile_as_float

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=float, default=0.)
    args = parser.parse_args()
    source = ROOT / "reviews/2026-09-08/radius-five-continuation-plans-32.json"
    raw = source.read_bytes()
    data = json.loads(raw)
    kernel, alpha, eta = exact_profile_as_float()
    plans = Plans(kernel, alpha, eta, float(data["delta"]))
    assert 0 <= args.target < plans.margin
    for item in data["plans"][1:]:
        plans.add(list(map(float, item["gaps"])), float(item["offset"]))
    initial_count = len(plans.items)
    queue, updates, searches = deque(), [], []
    rng = np.random.default_rng(38812)
    roots = np.array([5.7, 6.43, 6.52, 6.56, 6.60, 12.34, 12.43, 12.52, 18.41])
    core = np.clip(rng.choice(roots, (6000, 5))+rng.normal(0, .6, (6000, 5)), 5.7, 128)
    broad = rng.uniform(5.7, 128, (4000, 5))
    broad[:, 0] = np.clip(rng.choice([6.55, 12.5], 4000)+rng.normal(0, .5, 4000), 5.7, 128)
    words = np.r_[core, broad]
    values = plans.residual(words)

    def update(word, reason, parent=None):
        # Direct kernel minimum over all current plans; still double precision.
        residual = float(plans.residual(word[None, :], exact=True)[0])
        if residual >= args.target:
            return
        _, tail_ids = plans.value(word[None, 1:], exact=True)
        before = len(plans.items)
        new_id = plans.extend(word, tail_ids[0])
        item = dict(reason=reason, parent_search=parent,
                    word=list(map(float, word)), original_kernel_residual=residual,
                    plans_before=before, tail_plan=int(tail_ids[0]), result_plan=new_id)
        updates.append(item)
        if new_id == before:
            queue.append((word[:4].copy(), len(updates)-1))

    alphabet = np.r_[roots, 80.]
    q = len(alphabet)
    edge_ids = np.arange(q**5)
    states = alphabet[np.column_stack([(np.arange(q**4)//q**j) % q for j in range(3, -1, -1)])]
    grid_words = alphabet[np.column_stack([(edge_ids//q**j) % q for j in range(4, -1, -1)])]
    grid_costs = plans.cost(grid_words)
    grid_heights = plans.value(states)[0]
    grid_residual = grid_costs+grid_heights[edge_ids % q**4]-grid_heights[edge_ids//q]
    initial_grid = dict(minimum=float(grid_residual.min()), negative_edges=int(np.sum(grid_residual < 0)),
                        word=list(map(float, grid_words[np.argmin(grid_residual)])))
    grid_rounds = []
    for round_id in range(12):
        grid_heights = plans.value(states)[0]
        grid_residual = grid_costs+grid_heights[edge_ids % q**4]-grid_heights[edge_ids//q]
        grid_rounds.append(dict(round=round_id, plans_before=len(plans.items),
                                minimum=float(grid_residual.min()),
                                negative_edges=int(np.sum(grid_residual < 0)),
                                below_target_edges=int(np.sum(grid_residual < args.target))))
        if grid_residual.min() >= args.target:
            break
        seen_heads = set()
        for index in np.argsort(grid_residual):
            if grid_residual[index] >= args.target or len(seen_heads) >= 80:
                break
            head = int(index)//q
            if head not in seen_heads:
                seen_heads.add(head)
                update(grid_words[index], f"complete_finite_graph_round_{round_id}")
    for index in np.argsort(values)[:80]:
        if values[index] < args.target:
            update(words[index], "initial_random")
    first_axis = np.unique(np.r_[np.linspace(5.7, 20, 716), np.linspace(20, 128, 541)])
    for step in range(160):
        if not queue:
            break
        state, parent = queue.popleft()
        predecessors = np.column_stack([first_axis, np.tile(state, (len(first_axis), 1))])
        vals = plans.residual(predecessors)
        best = int(np.argmin(vals))
        best_x, best_value = float(first_axis[best]), float(vals[best])

        def scalar(x):
            return float(plans.residual(np.r_[x, state][None, :])[0])

        for index in np.argsort(vals)[:3]:
            left, right = first_axis[max(0, index-1)], first_axis[min(len(first_axis)-1, index+1)]
            if left == right:
                continue
            result = minimize_scalar(scalar, bounds=(left, right), method="bounded",
                                     options={"xatol": 1e-9, "maxiter": 80})
            if result.fun < best_value:
                best_x, best_value = float(result.x), float(result.fun)
        searches.append(dict(state=list(map(float, state)), parent_update=parent,
                             plans_before=len(plans.items), predecessor=best_x,
                             sampled_refined_residual=best_value))
        if best_value < args.target:
            update(np.r_[best_x, state], "backward_predecessor", len(searches)-1)
        if (step+1) % 20 == 0:
            print(f"backward steps={step+1}, plans={len(plans.items)}, queue={len(queue)}", flush=True)
    # Fresh sample, including gaps absent from the initialization alphabet.
    pressure = rng.uniform(5.7, 128, (10000, 5))
    pressure[:, 0] = np.clip(rng.choice([6.55, 12.5], 10000)+rng.normal(0, .5, 10000), 5.7, 128)
    result = plans.residual(pressure)
    worst = int(np.argmin(result))
    direct = float(plans.residual(pressure[worst:worst+1], exact=True)[0])
    grid_heights = plans.value(states)[0]
    final_grid_residual = grid_costs+grid_heights[edge_ids % q**4]-grid_heights[edge_ids//q]
    output = dict(status="E only: sampled backward updates, not all predecessors",
                  source_sha256=hashlib.sha256(raw).hexdigest(), alpha=alpha, eta=eta,
                  margin=plans.margin, initial_count=initial_count,
                  target=args.target,
                  initial_sample_min=float(values.min()), updates=updates,
                  initial_finite_graph=initial_grid,
                  finite_graph_rounds=grid_rounds,
                  final_finite_graph=dict(minimum=float(final_grid_residual.min()),
                                          negative_edges=int(np.sum(final_grid_residual < 0)),
                                          below_target_edges=int(np.sum(final_grid_residual < args.target)),
                                          word=list(map(float, grid_words[np.argmin(final_grid_residual)]))),
                  backward_searches=searches,
                  queue_remaining=[dict(state=list(map(float, s)), parent_update=p) for s, p in queue],
                  final_plans=plans.items,
                  final_pressure=dict(count=len(pressure), word=list(map(float, pressure[worst])),
                                      spline_residual=float(result[worst]), original_kernel_residual=direct),
                  scope="Finite scalar grids and local minimization are not global; no subaction or zero bound is certified")
    filename = ("radius-five-backward-plan-refinement.json" if args.target == 0
                else "radius-five-backward-margin-refinement.json")
    (ROOT / "reviews/2026-09-08" / filename).write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(f"final plans={len(plans.items)}, updates={len(updates)}, backward={len(searches)}, "
          f"fresh pressure residual={direct:+.8e}", flush=True)


if __name__ == "__main__":
    main()

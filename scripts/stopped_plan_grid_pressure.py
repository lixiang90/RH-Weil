"""E-only original 266 plus I_1..I_4: graph and local pressure check."""

import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from radius_five_stopped_continuation import StoppedPlans
from radius_five_subaction_grid import exact_profile_as_float

ROOT = Path(__file__).resolve().parents[1]


def main():
    path = ROOT / "reviews/2026-09-08/radius-five-continuation-plans-266.json"
    raw = path.read_bytes()
    data = json.loads(raw)
    kernel, alpha, eta = exact_profile_as_float()
    plans = StoppedPlans(kernel, alpha, eta, float(data["delta"]))
    for v in data["plans"][1:]:
        plans.add(list(map(float, v["gaps"])), float(v["offset"]))
    alphabet = np.array([5.7,6.43,6.52,6.56,6.6,12.34,12.43,12.52,18.41,80.])
    n = len(alphabet)
    ids = np.arange(n**4)
    states = alphabet[np.column_stack([(ids//n**j) % n for j in range(3,-1,-1)])]
    heights = plans.value(states)[0]
    ids = np.arange(n**5)
    words = alphabet[np.column_stack([(ids//n**j) % n for j in range(4,-1,-1)])]
    residual = plans.cost(words)+heights[ids % n**4]-heights[ids//n]
    selected, seen = [], set()
    for j in np.argsort(residual):
        key = tuple(np.round(words[j]/3).astype(int))
        if key not in seen:
            selected.append(int(j))
            seen.add(key)
        if len(selected) >= 20:
            break
    out = dict(status="E only: finite graph and local continuous searches for stopped augmentation",
               source_sha256=hashlib.sha256(raw).hexdigest(),
               grid_minimum=float(residual.min()), grid_word=words[residual.argmin()].tolist(),
               local_searches=[])
    for idx, j in enumerate(selected):
        def fun(v):
            return float(plans.residual(np.asarray(v)[None, :])[0])
        opt = minimize(fun, words[j], method="Nelder-Mead", bounds=[(5.7,128.)]*5,
                       options={"maxiter":1800, "xatol":1e-9, "fatol":1e-12})
        direct = float(plans.residual(opt.x[None, :], exact=True)[0])
        out["local_searches"].append(dict(initial_word=words[j].tolist(), word=opt.x.tolist(),
                                           direct_residual=direct, success=bool(opt.success)))
        print(idx, direct, flush=True)
    (path.parent / "stopped-plan-grid-pressure.json").write_text(
        json.dumps(out, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()

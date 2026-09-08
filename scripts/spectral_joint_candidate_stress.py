"""E only: ternary and broad-gap stress of the last joint Riesz candidate."""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize

from spectral_periodic_graph_prefilter import mt_kernel
from spectral_riesz_window_prefilter import periodic_value

ROOT=Path(__file__).resolve().parents[1]


def main():
    prior=json.loads((ROOT/"reviews/2026-09-08/spectral-joint-periodic-law-prefilter.json").read_text())
    record=prior["history"][-1]
    t=np.array(record["distances"])
    y=np.array(record["profile_coefficients"])
    keep=y!=0
    t,y=t[keep],y[keep]
    sinc=lambda x:np.sinc(x/(2*np.pi))
    def kernel(x):
        x=np.asarray(x)
        H=(.5*(sinc(x[...,None]-t)+sinc(x[...,None]+t))
           -mt_kernel(x)[...,None]*sinc(t))*(t*t/(t*t-2))
        return mt_kernel(x)+H@y
    alpha=record["alpha_from_active_stationarity"]
    eta=record["eta_from_active_stationarity"]
    def objective(g):
        ar=np.asarray(g)
        words=ar[None,:] if ar.ndim==1 else ar.T
        v=periodic_value(words,kernel)+eta*words.mean(axis=1)/(2*np.pi)
        return float(v[0]) if ar.ndim==1 else v
    patterns=[]
    for n in range(1,7):
        for word in product((1,2,3),repeat=n):
            if 3 not in word or word!=min(word[k:]+word[:k] for k in range(n)):
                continue
            if any(n%d==0 and word==word[:d]*(n//d) for d in range(1,n)):
                continue
            patterns.append(word)
    cuts=[]
    for idx,pattern in enumerate(patterns):
        starts={1:6.52,2:12.43,3:18.5}
        boxes={1:(5.7,7),2:(11.7,13.3),3:(17.7,19.6)}
        found=minimize(objective,[starts[x] for x in pattern],method="L-BFGS-B",
                       bounds=[boxes[x] for x in pattern],
                       options=dict(maxiter=180,ftol=1e-14,gtol=1e-9))
        cuts.append(dict(kind="ternary_box",pattern=list(pattern),
            gaps=list(map(float,found.x)),residual=float(found.fun-alpha),
            local_search_success=bool(found.success)))
        if (idx+1)%25==0:
            print(f"searched {idx+1}/{len(patterns)} ternary words; "
                  f"worst residual={min(c['residual'] for c in cuts):+.6e}",flush=True)
    for period in (2,3,4,6):
        for seed in (901,902):
            found=differential_evolution(objective,[(0,32)]*period,
                seed=seed+10*period,popsize=10,maxiter=280,vectorized=True,
                updating="deferred",polish=True)
            cuts.append(dict(kind="broad_DE",period=period,seed=seed,
                gaps=list(map(float,found.x)),residual=float(found.fun-alpha),
                search_success=bool(found.success)))
            print(f"broad period={period},seed={seed},residual={found.fun-alpha:+.6e}",flush=True)
    worst=min(cuts,key=lambda c:c["residual"])
    print("worst",worst,flush=True)
    output=dict(status="E only; no rigorous exclusion or global optimum",
        source="spectral-joint-periodic-law-prefilter.json last history entry",
        alpha=alpha,eta=eta,ternary_patterns=len(patterns),
        cuts=cuts,worst=worst,
        caution="All intervals here are optimizer search domains, not outward numerical intervals.")
    (ROOT/"reviews/2026-09-08/spectral-joint-candidate-stress.json").write_text(
        json.dumps(output,indent=2)+"\n",encoding="utf-8")


if __name__=="__main__":
    main()

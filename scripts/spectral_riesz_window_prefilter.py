"""E only: a radius-five full-space Riesz candidate and binary periodic cuts."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from spectral_periodic_graph_prefilter import C0, TARGET, fit_constraints, mt_kernel

ROOT=Path(__file__).resolve().parents[1]


def primitive_necklaces(max_period):
    for n in range(1,max_period+1):
        for word in product((1,2),repeat=n):
            if word != min(word[k:]+word[:k] for k in range(n)):
                continue
            if any(n%d==0 and word==word[:d]*(n//d) for d in range(1,n)):
                continue
            yield word


def construct_candidate():
    p1=tuple(map(Fraction,("6.52066","12.34276","6.52066")))
    p2=tuple(map(Fraction,("6.55444","12.42931")))
    z1,z2=(float(sum(p)/len(p))/(2*np.pi) for p in (p1,p2))
    w1=(TARGET*z2-1)/(z2-z1)
    w2=TARGET-w1
    grouped={}
    for word,weight in ((p1,w1),(p2,w2)):
        for i in range(len(word)):
            for r in range(1,6):
                t=sum(word[(i+l)%len(word)] for l in range(r))
                grouped[t]=grouped.get(t,0)+2*weight/len(word)
    distances=sorted(grouped)
    t=np.array(list(map(float,distances)))
    weights=np.array([grouped[x] for x in distances])
    sinc=lambda x:np.sinc(x/(2*np.pi))
    def representers(x):
        x=np.asarray(x)
        return (.5*(sinc(x[...,None]-t)+sinc(x[...,None]+t))
                -mt_kernel(x)[...,None]*sinc(t))*(t*t/(t*t-2))
    H=representers(t)
    y=np.linalg.solve(np.diag(1/weights)-H,mt_kernel(t))
    baseline=float(C0-y@H@y)
    def kernel(x):
        x=np.asarray(x)
        return mt_kernel(x)+representers(x)@y
    beta=1/math.sqrt(2)
    p0max=1/(math.sqrt(2)*math.sin(beta))
    density_floor=math.cos(beta)*p0max-float(
        np.sum(abs(y)*(t*t/(t*t-2))*(1+abs(sinc(t))*p0max)))
    assert density_floor>0
    description=dict(
        interpretation="floating coefficients for p0 + sum y_a r_ta; not an exact certified profile",
        words=[[str(x) for x in p] for p in (p1,p2)],
        distances=[str(x) for x in distances],coefficients=list(map(float,y)),
        baseline=baseline,density_lower_bound_float=density_floor)
    return kernel,baseline,description


def periodic_value(words,kernel):
    words=np.atleast_2d(np.asarray(words,dtype=float))
    distances=np.zeros_like(words)
    kernels=[]
    for offset in range(5):
        distances=distances+np.roll(words,-offset,axis=1)
        kernels.append(kernel(distances))
    degree=np.zeros_like(words)
    for r,k in enumerate(kernels,1):
        degree+=abs(k)+np.roll(abs(k),r,axis=1)
    degree=np.maximum(degree,1)
    value=np.zeros_like(words)
    for r,k in enumerate(kernels,1):
        dd=degree*np.roll(degree,-r,axis=1)
        value+=2*k*k*(2/np.sqrt(dd)-1/dd)
    return value.mean(axis=1)


def main():
    kernel,baseline,description=construct_candidate()
    words=[np.linspace(0,40,4001)[:,None]]
    old=json.loads((ROOT/"reviews/2026-09-08/spectral-periodic-graph-prefilter.json").read_text())
    words += [np.array([c["gaps"]]) for row in old["rows"] if row["radius"]==5
              for c in row["periodic_candidates"]]
    old=json.loads((ROOT/"reviews/2026-09-08/spectral-window-response-prefilter.json").read_text())
    words += [np.array([c["gaps"]]) for row in old["rows"] if row["radius"]==5
              for h in row["history"] for c in h["cuts"]]
    patterns=list(primitive_necklaces(8))
    rounds=[]
    for iteration in range(3):
        z=np.concatenate([p.mean(axis=1)/(2*np.pi) for p in words])
        values=np.concatenate([periodic_value(p,kernel) for p in words])
        fit=fit_constraints(z,values,baseline,TARGET)
        cuts=[]
        print(f"round={iteration}: output={fit['relaxed_output']:.12f}, "
              f"slack={fit['target_slack']:+.4e}",flush=True)
        for pattern in patterns:
            start=np.array([6.52 if bit==1 else 12.43 for bit in pattern])
            bounds=[(5.7,7) if bit==1 else (11.7,13.3) for bit in pattern]
            def obj(g):
                return float(periodic_value(g,kernel)[0]+fit["eta"]*np.mean(g)/(2*np.pi))
            found=minimize(obj,start,method="L-BFGS-B",bounds=bounds,
                           options=dict(maxiter=180,ftol=1e-14,gtol=1e-9))
            cuts.append(dict(pattern=list(pattern),gaps=list(map(float,found.x)),
                             residual=float(found.fun-fit["alpha"]),
                             local_search_success=bool(found.success)))
            words.append(found.x[None,:])
        worst=min(cuts,key=lambda x:x["residual"])
        print(f"  worst residual={worst['residual']:+.5e}, "
              f"pattern={worst['pattern']}, gaps={worst['gaps']}",flush=True)
        rounds.append(dict(fit=fit,cuts=cuts))
    z=np.concatenate([p.mean(axis=1)/(2*np.pi) for p in words])
    values=np.concatenate([periodic_value(p,kernel) for p in words])
    result=dict(status="E only, no verified full-domain subaction or zero proportion",
        candidate=description,target=TARGET,primitive_binary_patterns=len(patterns),
        maximum_period=8,rounds=rounds,
        final_fit=fit_constraints(z,values,baseline,TARGET),
        scope="local search in fixed binary boxes plus old sampled periods; unsampled gaps and longer periods remain open")
    (ROOT/"reviews/2026-09-08/spectral-riesz-window-prefilter.json").write_text(
        json.dumps(result,indent=2)+"\n",encoding="utf-8")


if __name__=="__main__":
    main()

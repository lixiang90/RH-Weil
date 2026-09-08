"""Two-mode window response to the periodic constraints; exploratory only."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize

from spectral_periodic_graph_prefilter import (
    C0, TARGET, cosine_kernel, fit_constraints, mt_kernel, periodic_value,
)

ROOT = Path(__file__).resolve().parents[1]


def prepare_basis(words, radius):
    words = np.atleast_2d(words)
    distances = np.zeros_like(words)
    basis = []
    for offset in range(radius):
        distances = distances + np.roll(words, -offset, axis=1)
        basis.append(np.stack([mt_kernel(distances), cosine_kernel(distances,1),
                               cosine_kernel(distances,2)]))
    return np.stack(basis)


def values_from_basis(basis, a, b):
    kernels = basis[:,0]+a*basis[:,1]+b*basis[:,2]
    # kernels: radius x batch x period
    degrees = np.zeros_like(kernels[0])
    for r,k in enumerate(kernels,start=1):
        degrees += abs(k)+np.roll(abs(k),r,axis=1)
    degrees = np.maximum(degrees,1)
    values = np.zeros_like(degrees)
    for r,k in enumerate(kernels,start=1):
        dd=degrees*np.roll(degrees,-r,axis=1)
        values += 2*k*k*(2/np.sqrt(dd)-1/dd)
    return np.mean(values,axis=1)


def main():
    previous=json.loads((ROOT/"reviews/2026-09-08/spectral-periodic-graph-prefilter.json").read_text())
    rng=np.random.default_rng(349)
    rows=[]
    cost=np.array([.5-1/(4*np.pi**2),.5-1/(16*np.pi**2)])
    for radius in (2,3,4,5):
        prior=next(r for r in previous["rows"] if r["radius"]==radius)
        words=[np.array([[g]]) for g in np.linspace(0,40,1001)]
        # Batch the constant words, then each nonconstant periodic witness.
        words=[np.linspace(0,40,1001)[:,None]]
        words += [np.array([c["gaps"]]) for c in prior["periodic_candidates"]]
        # Targeted binary clusters supplement broad DE's local minima.
        for period in (2,3,4,6):
            batch=rng.choice([2*np.pi,4*np.pi],size=(150,period))+rng.uniform(-.3,.4,(150,period))
            words.append(batch)
        history=[]
        for iteration in range(3):
            bases=[prepare_basis(w,radius) for w in words]
            zs=np.concatenate([w.mean(axis=1)/(2*np.pi) for w in words])
            def evaluate(ab, details=False):
                a,b=map(float,ab)
                baseline=C0-float(cost@np.array([a*a,b*b]))
                values=np.concatenate([values_from_basis(base,a,b) for base in bases])
                f=fit_constraints(zs,values,baseline,TARGET)
                return f if details else -f["target_slack"]
            start=np.zeros(2) if not history else np.array(history[-1]["coefficients"])
            opt=minimize(evaluate,start,method="Nelder-Mead",
                         bounds=[(-.15,.15)]*2,
                         options=dict(xatol=1e-8,fatol=1e-11,maxiter=400))
            a,b=map(float,opt.x)
            fit=evaluate(opt.x,True)
            eta=fit["eta"]
            record=dict(iteration=iteration,coefficients=[a,b],fit=fit,
                        local_optimizer_success=bool(opt.success),
                        baseline=C0-float(cost@np.array([a*a,b*b])),cuts=[])
            print(f"R={radius},round={iteration},a={a:+.7f},b={b:+.7f},"
                  f"relaxed output={fit['relaxed_output']:.12f}",flush=True)
            for period in (1,2,3,4,6):
                def obj(x):
                    ar=np.asarray(x)
                    w=ar[None,:] if ar.ndim==1 else ar.T
                    v=periodic_value(w,radius,((1,a,b),))+eta*w.mean(axis=1)/(2*np.pi)
                    return float(v[0]) if ar.ndim==1 else v
                # Include neighborhoods of both first low-energy frequencies.
                found=differential_evolution(obj,[(5.7,13.2)]*period,
                    seed=20000+100*radius+10*iteration+period,popsize=12,maxiter=300,
                    tol=1e-10,vectorized=True,updating="deferred",polish=True)
                value=float(periodic_value(found.x,radius,((1,a,b),))[0])
                residual=value+eta*np.mean(found.x)/(2*np.pi)-fit["alpha"]
                record["cuts"].append(dict(period=period,gaps=list(map(float,found.x)),
                    value=value,residual=float(residual),search_success=bool(found.success)))
                words.append(found.x[None,:])
                print(f"  period={period}: residual={residual:+.4e}",flush=True)
            history.append(record)
        rows.append(dict(radius=radius,history=history))
    output=dict(status="E only; local window optimization and finite periodic necessary constraints",
        profiles="single MT + a*cos(2*pi*u) + b*cos(4*pi*u); both coefficients bounded by .15",
        caution="No global optimum, stationary certificate or actual zero bound; output is optimistic relaxation",
        rows=rows)
    (ROOT/"reviews/2026-09-08/spectral-window-response-prefilter.json").write_text(
        json.dumps(output,indent=2)+"\n",encoding="utf-8")


if __name__=="__main__":
    main()

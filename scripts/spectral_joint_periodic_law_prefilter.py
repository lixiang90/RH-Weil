"""E only: jointly fit several periodic laws and the full Riesz response."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from spectral_periodic_graph_prefilter import C0, TARGET, mt_kernel
from spectral_riesz_window_prefilter import periodic_value, primitive_necklaces

ROOT=Path(__file__).resolve().parents[1]


def assemble(laws):
    ts=[]
    owners=[]
    factors=[]
    for owner,word in enumerate(laws):
        d=np.zeros(len(word))
        for offset in range(5):
            d=d+np.roll(word,-offset)
            ts.extend(d)
            owners.extend([owner]*len(word))
            factors.extend([2/len(word)]*len(word))
    t=np.array(ts)
    owners=np.array(owners)
    factors=np.array(factors)
    sinc=lambda x:np.sinc(x/(2*np.pi))
    def representers(x):
        x=np.asarray(x)
        return (.5*(sinc(x[...,None]-t)+sinc(x[...,None]+t))
                -mt_kernel(x)[...,None]*sinc(t))*(t*t/(t*t-2))
    H=representers(t)
    b=mt_kernel(t)
    identity=np.eye(len(t))
    def response(w):
        W=factors*w[owners]
        sample=np.linalg.solve(identity-H*W,b)
        coefficients=W*sample
        upper=float(C0+b@coefficients)
        gradient=np.array([np.sum(factors[owners==i]*sample[owners==i]**2)
                           for i in range(len(laws))])
        return upper,gradient,coefficients,W
    return response,representers,H,t


def quadratic_value(word,kernel):
    words=np.atleast_2d(word)
    d=np.zeros_like(words)
    value=np.zeros_like(words)
    for offset in range(5):
        d=d+np.roll(words,-offset,axis=1)
        value+=2*kernel(d)**2
    return value.mean(axis=1)


def main():
    laws=[np.array(g) for g in (
        [6.55444,12.42931],
        [6.52066,12.34276,6.52066],
        [6.52280349,6.52280351,12.37083356,6.56513129,12.37083354],
        [6.58227864,12.52065796,12.52065796])]
    z=np.array([g.mean()/(2*np.pi) for g in laws])
    w_low=(TARGET*z[0]-1)/(z[0]-z[1])
    initial=np.array([TARGET-w_low,w_low,0,0])
    patterns=list(primitive_necklaces(8))
    history=[]
    for iteration in range(3):
        z=np.array([g.mean()/(2*np.pi) for g in laws])
        response,representers,H,t=assemble(laws)
        fit=minimize(lambda w:response(w)[0],initial,
                     jac=lambda w:response(w)[1],method="SLSQP",
                     bounds=[(0,TARGET)]*len(laws),
                     constraints=[
                         dict(type="eq",fun=lambda w:sum(w)-TARGET,
                              jac=lambda w:np.ones(len(w))),
                         dict(type="eq",fun=lambda w:w@z-1,jac=lambda w:z)],
                     options=dict(ftol=2e-14,maxiter=500))
        assert fit.success,fit.message
        upper,gradient,coefficients,W=response(fit.x)
        positive=fit.x>1e-8
        # Multipliers recovered from the active gradient; these are numerical
        # stationarity data, never a certified lower bound on all gap words.
        slope=np.linalg.lstsq(np.column_stack([np.ones(sum(positive)),z[positive]]),
                              gradient[positive],rcond=None)[0]
        alpha=float(slope[0])
        eta=float(-slope[1])
        baseline=float(C0-coefficients@H@coefficients)
        eig=float(np.linalg.eigvalsh((H+H.T)/2*np.sqrt(W[:,None]*W[None,:]))[-1])
        assert eig<1 and eta>=0
        def kernel(x):
            return mt_kernel(np.asarray(x))+representers(np.asarray(x))@coefficients
        record=dict(iteration=iteration,laws=[list(map(float,g)) for g in laws],
            weights=list(map(float,fit.x)),relaxed_full_space_upper=upper,
            baseline=baseline,alpha_from_active_stationarity=alpha,
            eta_from_active_stationarity=eta,
            candidate_output=(baseline-eta)/(1-alpha),
            top_M_eigenvalue_float=eig,
            moment_residuals=[float(sum(fit.x)-TARGET),float(fit.x@z-1)],
            distances=list(map(float,t)),profile_coefficients=list(map(float,coefficients)),
            cuts=[])
        print(f"round={iteration},laws={len(laws)},upper={upper:.12f},"
              f"candidate output={record['candidate_output']:.12f},eig={eig:.5f}",flush=True)
        for index,pattern in enumerate(patterns):
            start=np.array([6.52 if bit==1 else 12.43 for bit in pattern])
            bounds=[(5.7,7) if bit==1 else (11.7,13.3) for bit in pattern]
            def objective(g):
                return float(quadratic_value(g,kernel)[0]+eta*np.mean(g)/(2*np.pi))
            found=minimize(objective,start,method="L-BFGS-B",bounds=bounds,
                           options=dict(maxiter=160,ftol=1e-14,gtol=1e-9))
            quad=float(quadratic_value(found.x,kernel)[0])
            full=float(periodic_value(found.x,kernel)[0])
            record["cuts"].append(dict(pattern=list(pattern),gaps=list(map(float,found.x)),
                quadratic_stationarity_residual=float(found.fun-alpha),
                full_graph_residual=float(full+eta*np.mean(found.x)/(2*np.pi)-alpha),
                branch_loss=quad-full,local_search_success=bool(found.success)))
            if (index+1)%25==0:
                print(f"  searched {index+1}/{len(patterns)} binary words",flush=True)
        ranked=sorted(record["cuts"],key=lambda x:x["quadratic_stationarity_residual"])
        print("  worst residual",ranked[0]["quadratic_stationarity_residual"],
              "pattern",ranked[0]["pattern"],flush=True)
        history.append(record)
        # Keep the active laws and add up to three newly found independent
        # primitive patterns. Dropped positive mass is repaired below exactly
        # at the floating linear-constraint level.
        kept=[i for i,x in enumerate(fit.x) if x>1e-8]
        laws=[laws[i] for i in kept]
        initial=np.array([fit.x[i] for i in kept])
        initial*=TARGET/sum(initial)
        zz=np.array([g.mean()/(2*np.pi) for g in laws])
        lo,hi=int(np.argmin(zz)),int(np.argmax(zz))
        shift=(1-initial@zz)/(zz[hi]-zz[lo])
        initial[hi]+=shift
        initial[lo]-=shift
        assert min(initial)>=0
        added_patterns=set()
        for cut in ranked:
            key=tuple(cut["pattern"])
            if key not in added_patterns and cut["quadratic_stationarity_residual"]< -1e-9:
                laws.append(np.array(cut["gaps"]))
                initial=np.r_[initial,0]
                added_patterns.add(key)
            if len(added_patterns)==3:
                break
    output=dict(status="E only; finite numerical law optimization and local periodic searches",
        caution="No certified minimax value, global subaction, interval proof or actual zero improvement",
        radius=5,target=TARGET,primitive_binary_patterns=len(patterns),
        history=history,next_candidate_laws=[list(map(float,g)) for g in laws])
    (ROOT/"reviews/2026-09-08/spectral-joint-periodic-law-prefilter.json").write_text(
        json.dumps(output,indent=2)+"\n",encoding="utf-8")


if __name__=="__main__":
    main()

"""Frozen C001 source audit; ordinary arithmetic, no spectrum certificate."""
from __future__ import annotations
import datetime as dt
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
sys.dont_write_bytecode = True
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reviews/2026-10-13/c001-source'
SOURCE = ROOT / 'scripts/qw_matrix.py'
spec = importlib.util.spec_from_file_location('qw_sources', SOURCE)
qw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qw)

def digest(path):
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()

def num(x):
    return mp.nstr(x, mp.mp.dps + 5)

def maximum(M):
    return max((abs(x) for x in M), default=mp.mpf(0))

def data(M):
    return [[num(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def mat(rows):
    return mp.matrix([[mp.mpf(x) for x in row] for row in rows])

def blocks(W,N):
    B=mp.matrix([[W[N+n,N+m] for m in range(1,N+1)] for n in range(1,N+1)])
    H=mp.matrix([[W[N+n,N-m] for m in range(1,N+1)] for n in range(1,N+1)])
    d=mp.matrix([W[N+n,N] for n in range(1,N+1)])
    return B-H,H,d,W[N,N]

def source_scalars(sources,N,v):
    out={}
    for name,W in sources.items():
        O,H,d,a=blocks(W,N)
        o=(v.T*O*v)[0]; h=(v.T*H*v)[0]; b=mp.sqrt(2)*(d.T*v)[0]
        out[name]={'a0':a,'o':o,'A':a-o,'h':h,'beta':b}
    A=mp.fsum(s['A'] for s in out.values()); h=mp.fsum(s['h'] for s in out.values()); b=mp.fsum(s['beta'] for s in out.values())
    diagonal={s:2*x['A']*x['h']-x['beta']**2 for s,x in out.items()}
    names=list(out); crosses={}
    for i,s in enumerate(names):
        for t in names[i+1:]:
            x,y=out[s],out[t]
            crosses[s+' | '+t]=2*(x['A']*y['h']+y['A']*x['h'])-2*x['beta']*y['beta']
    D=2*A*h-b*b
    return {'sources':{s:{k:num(vv) for k,vv in x.items()} for s,x in out.items()},'A':num(A),'h':num(h),'beta':num(b),'D':num(D),'diagonal':{s:num(x) for s,x in diagonal.items()},'crosses':{s:num(x) for s,x in crosses.items()},'D_sum_residual':num(D-mp.fsum(diagonal.values())-mp.fsum(crosses.values()))}

def qprime(x,n,m,L):
    if n==m:
        return -2/L*mp.cos(2*mp.pi*n*x/L)-4*mp.pi*n/L*(1-x/L)*mp.sin(2*mp.pi*n*x/L)
    return 2/L*(m*mp.cos(2*mp.pi*m*x/L)-n*mp.cos(2*mp.pi*n*x/L))/(n-m)

def main():
    t0=time.perf_counter(); archived=ROOT/'reviews/2026-10-13/goal-start-pilot/pilot-results.json'
    pilot=json.loads(archived.read_text(encoding='utf-8')); frozen=json.loads((OUT/'preregistration.json').read_text(encoding='utf-8'))
    if digest(SOURCE)!=pilot['preregistration']['source_file_lf_sha256']:
        raise RuntimeError('Source differs from frozen pilot')
    report={'started_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'input_lf_sha256':digest(archived),'source_lf_sha256':digest(SOURCE),'registration_lf_sha256':digest(OUT/'preregistration.json'),'script_lf_sha256':digest(Path(__file__)),'scope':'experiment; frozen finite matrices; no directed rounding','runs':[],'source_matrices':{},'complete':False}
    for dps in frozen['dps']:
        mp.mp.dps=dps; L=mp.log(13); nmax=6
        ks=[k for k in range(2,14) if qw.von_mangoldt(k)]
        full={s:mp.zeros(13) for s in ['pole','arch']+[f'prime:{k}' for k in ks]}
        # Reflection and transpose permit evaluation of one representative only.
        done=set()
        for n in range(-nmax,nmax+1):
            for m in range(-nmax,nmax+1):
                if (n,m) in done: continue
                orbit={(n,m),(m,n),(-n,-m),(-m,-n)}
                values={'pole':qw.w02(n,m,L),'arch':-qw.w_real(n,m,L)}
                values.update({f'prime:{k}':-qw.von_mangoldt(k)/mp.sqrt(k)*qw.q_nm(mp.log(k),n,m,L) for k in ks})
                for nn,mm in orbit:
                    for s,x in values.items(): full[s][nn+6,mm+6]=x
                done.update(orbit)
        report['source_matrices'][str(dps)]={s:data(M) for s,M in full.items()}
        for N in frozen['N']:
            base=next(r for r in pilot['runs'] if r['N']==N and r['dps']==dps and r['delta']=='0')
            v0=mp.matrix([mp.mpf(x) for x in base['odd_bottom_vector']])
            sliced={s:mp.matrix([[M[n+6,m+6] for m in range(-N,N+1)] for n in range(-N,N+1)]) for s,M in full.items()}
            # Independent sine-integral transcription for the off-diagonal arch H,d.
            sine={n:mp.quad(lambda x:mp.exp(x/2)/(mp.exp(x)-mp.exp(-x))*mp.sin(2*mp.pi*n*x/L),[0,L])/mp.pi for n in range(1,N+1)}
            _,Ha,da,_=blocks(sliced['arch'],N)
            sine_res=max(max(abs(da[n-1]-sine[n]/n) for n in range(1,N+1)),max(abs(Ha[n-1,m-1]-(sine[n]+sine[m])/(n+m)) for n in range(1,N+1) for m in range(1,N+1)))
            derivative=mp.matrix([[-qw.von_mangoldt(2)/mp.sqrt(2)*qprime(mp.log(2),n,m,L) for m in range(-N,N+1)] for n in range(-N,N+1)])
            Od,Hd,dd,ad=blocks(derivative,N)
            O0,H0,d0,a0=blocks(mat(base['W']),N)
            op=(v0.T*Od*v0)[0]; hp=(v0.T*Hd*v0)[0]; bp=mp.sqrt(2)*(dd.T*v0)[0]
            h0=(v0.T*H0*v0)[0]; o0=(v0.T*O0*v0)[0]; b0=mp.sqrt(2)*(d0.T*v0)[0]
            Dp=2*(ad-op)*h0+2*(a0-o0)*hp-2*b0*bp
            for label in frozen['delta']:
                saved=next(r for r in pilot['runs'] if r['N']==N and r['dps']==dps and r['delta']==label)
                delta=mp.mpf(0) if label=='0' else mp.mpf(1 if label[0]=='+' else -1)/1000
                sources={s:mp.matrix(M) for s,M in sliced.items()}
                sources['prime:2']=mp.matrix([[-qw.von_mangoldt(2)/mp.sqrt(2)*qw.q_nm(mp.log(2)+delta,n,m,L) for m in range(-N,N+1)] for n in range(-N,N+1)])
                W=sum(sources.values(),mp.zeros(2*N+1)); O,_,_,_=blocks(W,N)
                vals,vecs=mp.eigsy(O); v=vecs[:,0]
                if (v0.T*v)[0]<0: v=-v
                fixed=source_scalars(sources,N,v0); moving=source_scalars(sources,N,v)
                moving['D_vs_archived_residual']=num(mp.mpf(moving['D'])-mp.mpf(saved['D_2_a0_minus_o_h_minus_beta_squared']))
                report['runs'].append({'N':N,'dps':dps,'delta':label,'source_sum_vs_W_max':num(maximum(W-mat(saved['W']))),'arch_sine_transcription_residual':num(sine_res),'odd_bottom_vs_archived_residual':num(vals[0]-mp.mpf(saved['lowest_odd'])),'odd_gap':num(vals[1]-vals[0]),'overlap_v0_vdelta_abs':num(abs((v0.T*v)[0])),'fixed':fixed,'moving':moving,'fixed_origin_derivative':{'o_prime':num(op),'h_prime':num(hp),'beta_prime':num(bp),'a0_prime':num(ad),'D_prime':num(Dp)},'fixed_D_linear_remainder':num(mp.mpf(fixed['D'])-mp.mpf(source_scalars(sliced,N,v0)['D'])-delta*Dp)})
            print(f'N={N}, dps={dps}: source decomposition complete',flush=True)
        (OUT/'source-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    report['elapsed_seconds']=time.perf_counter()-t0; report['complete']=len(report['runs'])==12
    report['finished_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
    (OUT/'source-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Finished {len(report["runs"])} frozen cases in {report["elapsed_seconds"]:.3f}s',flush=True)

if __name__=='__main__': main()

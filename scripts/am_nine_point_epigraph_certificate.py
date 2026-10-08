"""Exact nine-point epigraph dual certificate under the disclosed PC8 admission.

--check uses only integer/Fraction arithmetic on the committed captured atoms
and rational duals. --replay additionally regenerates the isolated Lean capture.
Continuous tangent semantics and the all-zero analytic transport are proved
in the accompanying paper, not by this finite verifier alone.
"""
import argparse
import ast
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import subprocess

import am_nine_point_low_slack_cover as old

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'output/am-nine-point-epigraph-certificate.json'
WORK=ROOT/'tmp/pdfs/am-nine-point-epigraph'
SC,SA=32768,10**8
DEN=SA*335544320000000000
BS=[28898,57272,75526,80958,75526,57272,28898]
ROWS=[[13630830,0,19565904,20317441,45030671,100000000,200000000],
      [29997996,30621878,47766489,79682558,109938656,100000000],
      [37356140,69378121,65335210,79682558,45030671],
      [38030065,69378121,47766489,20317441],
      [37356140,30621878,19565904],[29997996,0],[13630830]]
TERMS=[(i,j,ROWS[i][j-i-1]) for i in range(7) for j in range(i+1,8) if ROWS[i][j-i-1]]
CS=[12310798,-15041681,3867664,6489926,-992327,5580097,-6846472,
    3781297,-5670353,3355089,-450523,-218483]


def sha(raw):
    return hashlib.sha256(raw.replace(b'\r\n',b'\n').replace(b'\r',b'\n')).hexdigest()


def modes(k,m):
    assert 0<=m<=1024
    return ((0,1024,0) if k==1 else (1024-m,m,0) if k==2
            else (0,1024-m,m) if k==3 else (1024,0,0))


def fields(pack):
    assert type(pack) is int and pack>=0
    return pack%(2**32),(pack>>32)%(2**32),pack>>64


def recover(cell):
    L=cell['gap_bounds'][::2];U=cell['gap_bounds'][1::2]
    cons=old.constraints(cell)
    cr=[1024*10**9*b for b in BS]
    base=10240000000000*sum(b*l for b,l in zip(BS,L))
    assert len(cell['atoms'])==26 and len(cell['ya'])==16
    for (i,j,a),atom in zip(TERMS,cell['atoms']):
        assert len(atom)==10 and all(type(x) is int and x>=0 for x in atom)
        k,m,p,r,l,u,l0,lb,pp,rp=atom
        low,high=(v//5 for v in cons[i,j])
        true_l=max(low,sum(L[i:j]));true_u=min(high,sum(U[i:j]))
        assert true_l<=true_u and l==true_l and l0==sum(L[i:j])
        assert u==(true_u if true_u>l else l+1)
        c,w1,w2=modes(k,m);mv=c*lb;msl=mw=mc=0
        for weight,point,pack in ((w1,p,pp),(w2,r,rp)):
            v,pplus,mplus=fields(pack)
            if weight:
                assert true_l<=point<=true_u and pplus>=1 and mplus>=1
                assert pplus+mplus<=4*10**9
            mv+=weight*v;msl+=weight*pplus;mw+=weight
            mc+=weight*(mplus-2*10**9)*max(point-l0,0)
        base+=SC*a*mv+10*a*mc
        for t in range(i,j):cr[t]+=a*(msl-2*10**9*mw)
    p,s,cp,cm=cell['ya'][:7],cell['ya'][7:14],cell['ya'][14],cell['ya'][15]
    assert all(type(x) is int and x>=0 for x in cell['ya'])
    bound=base+10*(cm-cp)-10*sum((u-l)*max(-(c+v-w),0) for u,l,c,v,w in zip(U,L,cr,s,p))
    assert bound>=335544320000000000*cell['paid_reward_numerator']
    return base-10*sum(c*l for c,l in zip(cr,L)),cr


def forms(cell):
    cons=old.constraints(cell);result={}
    for (i,j,a),atom in zip(TERMS,cell['atoms']):
        k,m,p,r,l,u,l0,lb,pp,rp=atom
        _,w1,w2=modes(k,m)
        true_l=max(cons[i,j][0]//5,sum(cell['gap_bounds'][2*t] for t in range(i,j)))
        true_u=min(cons[i,j][1]//5,sum(cell['gap_bounds'][2*t+1] for t in range(i,j)))
        assert l==true_l<=true_u
        lines=[(Q(lb,10**10),Q(0))]
        for weight,point,pack in ((w1,p,pp),(w2,r,rp)):
            if not weight:continue
            v,pplus,mplus=fields(pack)
            lo,hi=Q(pplus-2*10**9,10**9),Q(2*10**9-mplus,10**9)
            assert lo<=hi and true_l<=point<=true_u
            xp,L,U=Q(point,SC),Q(true_l,SC),Q(true_u,SC)
            value=Q(v,10**10)
            lines.append((value-hi*xp+(hi-lo)*L,lo))
            lines.append((value-lo*xp+(lo-hi)*U,hi))
        result[i,j]=lines
    return result


def reflected(cell):
    atoms={(7-j,7-i):atom for (i,j,a),atom in zip(TERMS,cell['atoms'])}
    cons={(7-j,7-i):v for (i,j),v in old.constraints(cell).items()}
    return {**cell,'gap_bounds':[v for i in range(6,-1,-1) for v in cell['gap_bounds'][2*i:2*i+2]],
            'span_bounds':[v//5 for span in old.SPANS for v in cons[span]],
            'atoms':[atoms[i,j] for i,j,a in TERMS]}


def problem(left_cell,right_cell):
    left,right=old.constraints(left_cell),old.constraints(right_cell)
    weights={}
    for offset in (0,1):
        for i,j,a in TERMS:
            weights[i+offset,j+offset]=weights.get((i+offset,j+offset),0)+a
    weights[0,8]=4*10**8
    pairs=list(weights);index={span:8+k for k,span in enumerate(pairs)}
    assert len(pairs)==34
    objective=[Q(BS[0])]+[Q(BS[i-1]+BS[i]) for i in range(1,7)]+[Q(BS[6])]
    objective+=[Q(weights[span]) for span in pairs]
    size=len(objective);matrix=[];rhs=[]
    def add(span,slope,zcoef,b):
        row=[Q(0)]*size;i,j=span
        for t in range(i,j):row[t]=slope
        if zcoef:row[index[span]]=zcoef
        matrix.append(row);rhs.append(b)
    for cons,offset,fs in ((left,0,forms(left_cell)),(right,1,forms(right_cell))):
        for (i,j),(lo,hi) in cons.items():
            add((i+offset,j+offset),Q(1),Q(0),Q(hi,5*SC))
            add((i+offset,j+offset),Q(-1),Q(0),-Q(lo,5*SC))
        for (i,j),lines in fs.items():
            for intercept,slope in lines:
                add((i+offset,j+offset),slope,Q(-1),-intercept)
    d=old.closure(left,right);assert d
    bounds=[(max(Q(4,5),Q(-d[i+1][i],5*SC)),Q(d[i][i+1],5*SC)) for i in range(8)]
    bounds+=[(Q(0),Q(1)) for _ in pairs]
    assert all(lo<=hi for lo,hi in bounds)
    return objective,matrix,rhs,bounds


def dual_lower(objective,matrix,rhs,bounds,sparse):
    dual=[Q(0)]*len(rhs);used=set()
    for row,value in sparse:
        assert type(row) is int and 0<=row<len(rhs) and row not in used
        used.add(row);dual[row]=Q(value);assert dual[row]>0
    residual=[c+sum(lam*row[i] for lam,row in zip(dual,matrix)) for i,c in enumerate(objective)]
    lower=-sum(lam*b for lam,b in zip(dual,rhs))
    lower+=sum(r*(lo if r>=0 else hi) for r,(lo,hi) in zip(residual,bounds))
    return lower/Q(2*SA)


def capture_program():
    source=old.build_instrumented()
    frozen=json.loads((ROOT/'reviews/2026-10-08/am-nine-point-adaptive-round-manifest.json').read_text(encoding='utf-8'))
    assert sha(source.encode('utf-8'))==frozen['transient_diagnostics']['pins'][0]['canonical_lf_sha256']
    rows=[]
    for n,(i,j,a) in enumerate(TERMS):
        tag=f'{i}{j}'
        args=[f'k{tag}',f'm{tag}',f'p{tag}',f'r{tag}',f'eL TS (toCl s) {n}',
              f'uc (eL TS (toCl s) {n}) (eU TS (toCl s) {n})',f'eL0 TS (toCl s) {n}',
              f'lb top bk (eL TS (toCl s) {n}) (uc (eL TS (toCl s) {n}) (eU TS (toCl s) {n}))',
              f'pb p{tag}',f'pb r{tag}']
        rows.append('['+', '.join('('+arg+')' for arg in args)+']')
    ya=[f'y.P{i}' for i in range(7)]+[f'y.S{i}' for i in range(7)]+['y.Cp','y.Cm']
    before='     dbg_trace s!"LOWPAID {paid}"\n     result'
    after=('     dbg_trace s!"LOWPAID {paid}"\n'
           '     dbg_trace s!"LOWRAW {['+', '.join(rows)+']}"\n'
           '     dbg_trace s!"LOWYA {['+', '.join(ya)+']}"\n     result')
    assert source.count(before)==1
    return source.replace(before,after)


def parse_capture(log):
    # Strip the extra diagnostics only for the original strict parser.
    base_log='\n'.join(line for line in log.splitlines() if not line.startswith(('LOWRAW ','LOWYA ')))
    base_cells=old.parse_log(base_log)
    records=[];record=None
    for line in log.splitlines():
        if line.startswith('LOWCELL '):
            assert record is None
            a,b=line[8:].split('|');record={'gap_bounds':ast.literal_eval(a),'span_bounds':ast.literal_eval(b)}
        elif line.startswith('LOWPAID '):record['paid_reward_numerator']=int(line[8:])
        elif line.startswith('LOWRAW '):record['atoms']=ast.literal_eval(line[7:])
        elif line.startswith('LOWYA '):
            record['ya']=ast.literal_eval(line[6:]);records.append(record);record=None
    assert record is None and len(records)==70
    assert [{k:v for k,v in c.items() if k not in ('atoms','ya')} for c in records]==base_cells
    return records


def verify(report):
    assert report['script_canonical_lf_sha256']==sha(Path(__file__).read_bytes())
    old_path=ROOT/'output/am-nine-point-low-slack-cover.json'
    assert report['low_cover_canonical_lf_sha256']==sha(old_path.read_bytes())
    frozen=json.loads(old_path.read_text(encoding='utf-8'))
    original=report['captured_cells']
    assert [{k:v for k,v in c.items() if k not in ('atoms','ya')} for c in original]==frozen['cells']
    for cell in original:recover(cell)
    # cos(sqrt(2)*u)>=3/4 on |u|<=1/2, so the AM density is positive.
    # Its positive normalization and total mass one give 0<=K(t)^2<=1.
    assert sum(abs(x) for x in CS)==64604710<750000000
    labelled=original+[reflected(cell) for cell in original]
    assert [(x['left'],x['right']) for x in report['pairs']]==[(x['left'],x['right']) for x in frozen['analysis']['pairs']]
    lowers=[]
    for result in report['pairs']:
        a,b=result['left'],result['right']
        lower=dual_lower(*problem(labelled[a],labelled[b]),result['dual_sparse'])
        assert lower==Q(result['lower'])>=Q(805103,SA)
        lowers.append(lower)
    minimum=min(lowers)
    assert len(lowers)==289 and str(minimum)==report['minimum_lower']
    assert str(minimum-Q(805103,SA))==report['strict_margin_over_target']
    assert Q(67216841-404350,SA)/(1-Q(805103,SA))==Q(66812491,99194897)
    return minimum


def main():
    if not __debug__:raise SystemExit('Run without -O: all assertions are required')
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check',action='store_true');mode.add_argument('--replay',action='store_true')
    parser.add_argument('--lean',default=r'C:\Users\A\.elan\bin\lean.exe')
    args=parser.parse_args();report=json.loads(OUTPUT.read_text(encoding='utf-8'))
    if args.replay:
        WORK.mkdir(parents=True,exist_ok=True);path=WORK/'AffineCapture.lean'
        path.write_text(capture_program(),encoding='utf-8')
        run=subprocess.run([args.lean,'+leanprover/lean4:v4.34.1','--tstack=32768','-j1',str(path)],
                           cwd=ROOT,capture_output=True,timeout=1800)
        log=(run.stdout+run.stderr).decode('utf-8');(WORK/'capture-log.txt').write_text(log,encoding='utf-8')
        assert run.returncode==0,'Lean failed; see isolated capture-log.txt'
        assert parse_capture(log)==report['captured_cells']
    minimum=verify(report)
    print('PASS 289 exact nine-point epigraph duals; local reward >=805103/100000000')
    print('minimum:',minimum,'; finite verification under disclosed PC8 admission')


if __name__=='__main__':main()

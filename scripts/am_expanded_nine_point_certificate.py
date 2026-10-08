"""Expanded nine-point exact certificate under the disclosed PC8 admission.

--check needs the committed data and Python standard library only.
--replay also checks PTL/REG against the fixed source and recaptures Lean leaves.
The continuous and all-zero mathematical transport is stated in the paper.
"""
import argparse
import ast
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re
import subprocess

import am_nine_point_epigraph_certificate as epi

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'output/am-expanded-nine-point-certificate.json'
WORK=ROOT/'tmp/pdfs/am-expanded-nine-point'
SC,SA=32768,10**8
STRONG,TARGET=805803,805260
SOURCE_SHA='012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f'
epi.old.STRONG=STRONG


def capture_program():
    source=epi.capture_program()
    old_call='(mcheckStrongP 805203 '
    old_search=') 8 805003 805203'
    assert source.count(old_call)==source.count(old_search)==1
    source=source.replace(old_call,f'(mcheckStrongP {STRONG} ',1)
    source=source.replace(old_search,f') 10 805003 {STRONG}',1)
    assert source.count('def cN : ℕ := 805003')==1 and source.count('#eval emit ')==41
    return source


def parse_capture(log):
    assert not re.search(r'error:|error\(|Stack overflow|Aborting|sorry|panic',log)
    checks=[];cells=[];record=None
    for line in log.splitlines():
        m=re.fullmatch(r'PILOT (\S+) (true|false)',line)
        if m:
            assert record is None
            checks.append(m.groups())
        elif line.startswith('LOWCELL '):
            assert record is None
            a,b=line[8:].split('|')
            record={'gap_bounds':ast.literal_eval(a),'span_bounds':ast.literal_eval(b)}
        elif line.startswith('LOWPAID '):
            assert record is not None
            record['paid_reward_numerator']=int(line[8:])
        elif line.startswith('LOWRAW '):
            assert record is not None
            record['atoms']=ast.literal_eval(line[7:])
        elif line.startswith('LOWYA '):
            assert record is not None
            record['ya']=ast.literal_eval(line[6:]);cells.append(record);record=None
    names=['large-gap7','adjacent7']+[f'cover-{i}' for i in range(7)]+[f'root-{i}' for i in range(32)]
    assert record is None and checks==[(n,'true') for n in names] and len(cells)==241
    return cells


def geometry(cells):
    cs=[epi.old.constraints(c) for c in cells]
    pairs=[];coordinates=shared=0
    for a,left in enumerate(cs):
        for b,right in enumerate(cs):
            if any(max(left[i+1,i+2][0],right[i,i+1][0])>
                   min(left[i+1,i+2][1],right[i,i+1][1]) for i in range(6)):continue
            coordinates+=1
            if any(max(left[i+1,j+1][0],right[i,j][0])>
                   min(left[i+1,j+1][1],right[i,j][1])
                   for i,j in epi.old.SPANS if j<=6):continue
            shared+=1
            if epi.old.closure(left,right) is not None:pairs.append((a,b))
    return pairs,coordinates,shared


def extra_lines(cell,item,catalog,region):
    i,j=item['span'];assert (i,j) in [(a,b) for a,b,_ in epi.TERMS]
    point,pack,list_id=item['point'],item['pack'],item['list']
    assert catalog[point]==(pack,list_id)
    cons=epi.old.constraints(cell)
    L=max(cons[i,j][0]//5,sum(cell['gap_bounds'][2*t] for t in range(i,j)))
    U=min(cons[i,j][1]//5,sum(cell['gap_bounds'][2*t+1] for t in range(i,j)))
    lp,up=min(L,point),max(U,point)
    assert L<=U and item['expanded_bounds']==[lp,up]
    k=(point+16384)>>15;assert k<16
    a=(region[0]>>(20*k))&1048575;b=(region[1]>>(20*k))&1048575
    v,plus,minus=epi.fields(pack)
    assert a<=lp<=point<=up<=b and plus>=1 and minus>=1 and plus+minus<=4*10**9
    lo,hi=Q(plus-2*10**9,10**9),Q(2*10**9-minus,10**9)
    p,l,u=Q(point,SC),Q(lp,SC),Q(up,SC);value=Q(v,10**10)
    return [(value-hi*p+(hi-lo)*l,lo),(value-lo*p+(lo-hi)*u,hi)]


def problem(left,right,extra,catalog,region):
    obj,matrix,rhs,bounds=epi.problem(left,right)
    weights={}
    for offset in (0,1):
        for i,j,a in epi.TERMS:
            weights[i+offset,j+offset]=weights.get((i+offset,j+offset),0)+a
    weights[0,8]=4*SA;index={span:8+n for n,span in enumerate(weights)}
    used=set()
    for item in extra:
        offset=item['offset'];assert offset in (0,1)
        i,j=item['span'];key=(offset,i,j,item['point']);assert key not in used
        used.add(key)
        lines=extra_lines((left,right)[offset],item,catalog,region)
        for intercept,slope in lines:
            row=[Q(0)]*42
            for t in range(i+offset,j+offset):row[t]=slope
            row[index[i+offset,j+offset]]=Q(-1)
            matrix.append(row);rhs.append(-intercept)
    return obj,matrix,rhs,bounds


def dual_lower(obj,matrix,rhs,bounds,sparse):
    residual=list(obj);value=Q(0);used=set()
    for row,multiplier in sparse:
        assert type(row) is int and row not in used and 0<=row<len(rhs)
        used.add(row);lam=Q(multiplier);assert lam>0
        value-=lam*rhs[row]
        for i,a in enumerate(matrix[row]):
            if a:residual[i]+=lam*a
    return (value+sum(r*(lo if r>=0 else hi)
             for r,(lo,hi) in zip(residual,bounds)))/Q(2*SA)


def verify(report):
    assert report['script_canonical_lf_sha256']==epi.sha(Path(__file__).read_bytes())
    assert report['strong_target_numerator']==STRONG and report['target_numerator']==TARGET
    for path,pin in report['dependency_pins'].items():
        assert epi.sha((ROOT/path).read_bytes())==pin
    original=report['captured_cells'];assert len(original)==241
    assert len({tuple(c['gap_bounds']+c['span_bounds']) for c in original})==241
    for cell in original:epi.recover(cell)
    catalog={p:(pack,list_id) for p,pack,list_id in report['point_catalog']}
    assert len(catalog)==len(report['point_catalog']) and len(report['region'])==2
    cells=original+[epi.reflected(c) for c in original]
    pairs,coordinates,shared=geometry(cells)
    assert (len(cells),coordinates,shared,len(pairs))==(482,4796,2405,2399)
    assert pairs==[(x['left'],x['right']) for x in report['pairs']]
    minimum=None
    for record in report['pairs']:
        a,b=record['left'],record['right']
        lower=dual_lower(*problem(cells[a],cells[b],record['extra_points'],catalog,report['region']),
                         record['dual_sparse'])
        assert lower==Q(record['lower'])>=Q(TARGET,SA)
        minimum=lower if minimum is None else min(minimum,lower)
    assert str(minimum)==report['minimum_lower']
    assert str(minimum-Q(TARGET,SA))==report['strict_margin_over_target']
    assert Q(STRONG+805003,2*SA)>Q(TARGET,SA)
    assert Q(67216841-404350,SA)/(1-Q(TARGET,SA))==Q(66812491,99194740)
    return minimum


def check_catalog_source(report):
    raw=(ROOT/'tmp/pc8-am-admission/Solution.lean').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA
    points={};region=None
    for line in raw.decode('utf-8').splitlines():
        match=re.fullmatch(r'def PTL_(\d+) \(x : ℕ\) : ℕ := ptl (.+) x',line)
        if match:
            for p,pack in ast.literal_eval(match[2]):
                assert p not in points;points[p]=(pack,int(match[1]))
        if line.startswith('def REG : '):region=ast.literal_eval(line.split(':=',1)[1].strip())[:2]
    assert len(points)==2196 and list(region)==report['region']
    assert all(points[p]==(pack,list_id) for p,pack,list_id in report['point_catalog'])


def main():
    if not __debug__:raise SystemExit('Run without -O: assertions are required')
    parser=argparse.ArgumentParser(description=__doc__)
    modes=parser.add_mutually_exclusive_group(required=True)
    modes.add_argument('--check',action='store_true');modes.add_argument('--replay',action='store_true')
    parser.add_argument('--lean',default=r'C:\Users\A\.elan\bin\lean.exe')
    args=parser.parse_args();report=json.loads(OUTPUT.read_text(encoding='utf-8'))
    if args.replay:
        check_catalog_source(report)
        source=capture_program();assert epi.sha(source.encode())==report['capture_source_canonical_lf_sha256']
        WORK.mkdir(parents=True,exist_ok=True);path=WORK/'ExpandedCapture.lean'
        path.write_text(source,encoding='utf-8')
        run=subprocess.run([args.lean,'+leanprover/lean4:v4.34.1','--tstack=32768','-j1',str(path)],
                           cwd=ROOT,capture_output=True,timeout=1800)
        log=(run.stdout+run.stderr).decode('utf-8');(WORK/'capture-log.txt').write_text(log,encoding='utf-8')
        assert run.returncode==0,'Lean capture failed; see isolated log'
        assert parse_capture(log)==report['captured_cells']
    minimum=verify(report)
    print('PASS all2399 exact domains; local reward >=805260/100000000')
    print('minimum:',minimum,'; inherited PC8/REG/PTL admission required')


if __name__=='__main__':main()

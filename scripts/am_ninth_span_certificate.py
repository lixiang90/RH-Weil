"""No SciPy: exact closed full-span branches and complete 2399-domain check."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import time
import argparse
import ast
import re
ROOT=next(p for p in Path(__file__).resolve().parents
          if (p/'output/am-expanded-nine-point-certificate.json').is_file())
sys.path.insert(0,str(ROOT/'scripts'))
import am_expanded_nine_point_certificate as inherited

epi=inherited.epi
SC,SA=inherited.SC,inherited.SA
OLD=ROOT/'output/am-expanded-nine-point-certificate.json'
SOURCE_SHA=inherited.SOURCE_SHA
SOURCE_URL=epi.old.old.SOURCE_URL

def load_catalog(path,cert,report,source_path=None):
    data=json.loads(path.read_text(encoding='utf8'))
    assert data['source_raw_sha256']==cert['source_raw_sha256']==SOURCE_SHA
    assert data['source_url']==SOURCE_URL
    assert data['original_expanded_report_canonical_lf_sha256']==epi.sha(OLD.read_bytes())
    assert data['certificate_canonical_lf_sha256']==epi.sha(CERT.read_bytes())
    assert data['region']==report['region'] and data['original_point_count']==2196
    points={p:(pack,n) for p,pack,n in data['point_catalog']}
    assert len(points)==len(data['point_catalog'])==data['used_point_count']==541
    used={(d[3],d[4],d[5]) for r in cert['replacements'] for b in r['branches']
          if not b['empty'] for d in b['added_rows']
          if d[0]=='tangent' and d[6]=='direct-region'}
    assert used=={(p,pack,n) for p,(pack,n) in points.items()}
    inherited_points={p:(pack,n) for p,pack,n in report['point_catalog']}
    assert all(points[p]==item for p,item in inherited_points.items() if p in points)
    if source_path is not None:
        raw=source_path.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA
        full={};region=None
        for line in raw.decode('utf8').splitlines():
            m=re.fullmatch(r'def PTL_(\d+) \(x : ℕ\) : ℕ := ptl (.+) x',line)
            if m:
                for p,pack in ast.literal_eval(m[2]):
                    assert p not in full
                    full[p]=(pack,int(m[1]))
            if line.startswith('def REG : '):
                region=ast.literal_eval(line.split(':=',1)[1].strip())[:2]
        assert len(full)==2196 and list(region)==report['region']
        assert all(full[p]==item for p,item in points.items())
        assert all(full[p]==item for p,item in inherited_points.items())
    return points

def closure(left,right,lo,hi):
    d=epi.old.closure(epi.old.constraints(left),epi.old.constraints(right))
    assert d and type(lo) is int and type(hi) is int and lo<=hi
    d[0][8]=min(d[0][8],hi);d[8][0]=min(d[8][0],-lo)
    for k in range(9):
        for i in range(9):
            for j in range(9):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
        if any(d[i][i]<0 for i in range(9)):return None
    return d

def added_row(left,right,d,desc,points,region,zindex):
    tag,i,j=desc[:3]
    assert type(i) is int and type(j) is int and 0<=i<j<=8
    lo,hi=Q(-d[j][i],5*SC),Q(d[i][j],5*SC)
    row=[Q(0)]*42
    if tag in ('closure-upper','closure-lower'):
        assert len(desc)==3
        sign=Q(1) if tag=='closure-upper' else Q(-1)
        for t in range(i,j):row[t]=sign
        return row,hi if sign==1 else -lo
    assert tag=='tangent' and len(desc)==8 and (i,j) in zindex
    point,pack,list_id,guard,side=desc[3:]
    assert side in ('L','U')
    p=Q(point,SC)
    if guard=='direct-region':
        assert points[point]==(pack,list_id)
        k=(point+16384)>>15;assert k<16
        a=Q((region[0]>>(20*k))&1048575,SC)
        b=Q((region[1]>>(20*k))&1048575,SC)
        assert a<=min(lo,p)<=p<=max(hi,p)<=b
    else:
        assert guard=='old-enabled' and list_id==-1
        found=False
        for cell,offset in ((left,0),(right,1)):
            cons=epi.old.constraints(cell)
            for (s,t,_),atom in zip(epi.TERMS,cell['atoms']):
                if (s+offset,t+offset)!=(i,j):continue
                k,m,p1,p2,*_,pp,rp=atom;_,w1,w2=epi.modes(k,m)
                if (w1 and (point,pack)==(p1,pp)) or (w2 and (point,pack)==(p2,rp)):
                    old_lo=Q(max(cons[s,t][0]//5,sum(cell['gap_bounds'][2*v] for v in range(s,t))),SC)
                    old_hi=Q(min(cons[s,t][1]//5,sum(cell['gap_bounds'][2*v+1] for v in range(s,t))),SC)
                    assert old_lo<=min(lo,p)<=p<=max(hi,p)<=old_hi
                    found=True
        assert found
    value,plus,minus=epi.fields(pack)
    assert plus>=1 and minus>=1 and plus+minus<=4*10**9
    dl,du=Q(plus-2*10**9,10**9),Q(2*10**9-minus,10**9)
    l,u=min(lo,p),max(hi,p)
    if side=='L':intercept=Q(value,10**10)-du*p+(du-dl)*l;slope=dl
    else:intercept=Q(value,10**10)-dl*p+(dl-du)*u;slope=du
    for t in range(i,j):row[t]=slope
    row[zindex[i,j]]=Q(-1)
    return row,-intercept

def branch_problem(left,right,branch,points,region):
    lo,hi=branch['bounds_5sc']
    d=closure(left,right,lo,hi)
    if branch['empty']:
        assert d is None
        return None
    assert d
    obj,matrix,rhs,bounds=epi.problem(left,right)
    assert len(rhs)==branch['base_rows']
    bounds[:8]=[(max(Q(4,5),Q(-d[i+1][i],5*SC)),Q(d[i][i+1],5*SC)) for i in range(8)]
    assert all(lo<=hi for lo,hi in bounds)
    weights={}
    for offset in (0,1):
        for i,j,a in epi.TERMS:weights[i+offset,j+offset]=weights.get((i+offset,j+offset),0)+a
    weights[0,8]=4*SA
    zindex={span:8+n for n,span in enumerate(weights)}
    for descriptor in branch['added_rows']:
        row,b=added_row(left,right,d,descriptor,points,region,zindex)
        matrix.append(row);rhs.append(b)
    return obj,matrix,rhs,bounds

def main():
    if not __debug__:raise SystemExit('assertions must remain enabled')
    started=time.monotonic()
    global CERT
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='check the fixed complete certificate')
    parser.add_argument('--certificate',type=Path,default=ROOT/'output/am-ninth-span-certificate.json')
    parser.add_argument('--catalog',type=Path,default=ROOT/'output/am-ninth-span-point-catalog.json')
    parser.add_argument('--source',type=Path,default=None,
                        help='optional raw pinned original Lean source; not needed offline')
    parser.add_argument('--audit-output',type=Path,default=None)
    parser.add_argument('--edge-lowers',type=Path,default=None)
    args=parser.parse_args();CERT=args.certificate
    cert=json.loads(CERT.read_text(encoding='utf8'))
    assert epi.sha(OLD.read_bytes())==cert['old_report_canonical_lf_sha256']
    report=json.loads(OLD.read_text(encoding='utf8'))
    assert report['script_canonical_lf_sha256']==epi.sha(Path(inherited.__file__).read_bytes())
    for path,pin in report['dependency_pins'].items():
        assert epi.sha((ROOT/path).read_bytes())==pin
    points=load_catalog(args.catalog,cert,report,args.source)
    for cell in report['captured_cells']:epi.recover(cell)
    cells=report['captured_cells']+[epi.reflected(c) for c in report['captured_cells']]
    pairs,gaps,spans=inherited.geometry(cells)
    assert (len(cells),gaps,spans,len(pairs))==(482,4796,2405,2399)
    assert pairs==[(x['left'],x['right']) for x in report['pairs']]
    replacement={(x['left'],x['right']):x for x in cert['replacements']}
    assert len(replacement)==len(cert['replacements'])==47
    old_points={p:(pack,n) for p,pack,n in report['point_catalog']}
    lowers=[];branch_count=0;point_uses=0
    edge_lowers=[]
    for n,old in enumerate(report['pairs']):
        a,b=old['left'],old['right']
        if (a,b) in replacement:
            record=replacement[a,b]
            original=epi.old.closure(epi.old.constraints(cells[a]),epi.old.constraints(cells[b]))
            expected_lo,expected_hi=-original[8][0],original[0][8]
            branches=record['branches'];assert branches
            assert branches[0]['bounds_5sc'][0]==expected_lo
            assert branches[-1]['bounds_5sc'][1]==expected_hi
            assert all(x['bounds_5sc'][1]==y['bounds_5sc'][0] for x,y in zip(branches,branches[1:]))
            branch_lowers=[]
            for branch in branches:
                prob=branch_problem(cells[a],cells[b],branch,points,report['region'])
                branch_count+=1
                if prob is None:continue
                lower=inherited.dual_lower(*prob,branch['dual_sparse'])
                assert lower==Q(branch['lower'])
                branch_lowers.append(lower)
                point_uses+=sum(x[0]=='tangent' for x in branch['added_rows'])
            assert branch_lowers
            lower=min(branch_lowers)
            assert lower==Q(record['lower'])
        else:
            lower=inherited.dual_lower(*inherited.problem(cells[a],cells[b],old['extra_points'],old_points,report['region']),old['dual_sparse'])
            assert lower==Q(old['lower'])
        lowers.append(lower)
        edge_lowers.append({'left':a,'right':b,'lower':str(lower)})
        if n%500==0:print('checked',n,flush=True)
    finite_min=min(lowers)
    outside=Q(report['strong_target_numerator']+805003,2*SA)
    reward=min(finite_min,outside)
    ratio=Q(66812491,SA)/(1-reward)
    assert reward==Q(805403,SA) and ratio==Q(66812491,99194597)
    assert ratio>Q(66812491,99194740)
    output={'finite_certificate_pass':True,'domains':2399,'replacements':47,
            'closed_branches':branch_count,'positive_tangent_row_uses':point_uses,
            'minimum_domain_lower':str(finite_min),'outside_lower':str(outside),
            'uniform_reward':str(reward),'simple_critical_proportion':str(ratio),
            'elapsed_seconds':time.monotonic()-started,
            'certificate_raw_sha256':hashlib.sha256(CERT.read_bytes()).hexdigest(),
            'checker_raw_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output['point_catalog_canonical_lf_sha256']=epi.sha(args.catalog.read_bytes())
    output['certificate_canonical_lf_sha256']=epi.sha(CERT.read_bytes())
    output['checker_canonical_lf_sha256']=epi.sha(Path(__file__).read_bytes())
    output['source_file_verified']=args.source is not None
    if args.audit_output is not None:
        args.audit_output.write_text(json.dumps(output,indent=2)+'\n',encoding='utf8')
    if args.edge_lowers is not None:
        args.edge_lowers.write_text(json.dumps(edge_lowers,indent=2)+'\n',encoding='utf8')
    print('PASS',output)

if __name__=='__main__':main()

"""Exact strengthened AM single-frame and unchanged ninth-span assembly.

Python standard library only. Original continuous PC8/capture, PTL/REG and
all-zero analytic transport remain the admitted mathematical dependencies.
This is a finite mathematical checker, not a new Lean/NaNoDa or website PASS.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse,ast,hashlib,json,re,runpy,sys,time
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'output/am-expanded-nine-point-certificate.json').is_file())
sys.path.insert(0,str(ROOT/'scripts'))
import am_expanded_nine_point_certificate as inherited
epi=inherited.epi
SC,SA=inherited.SC,inherited.SA
REPORT=ROOT/'output/am-expanded-nine-point-certificate.json'
NINTH=ROOT/'output/am-ninth-span-certificate.json'
LOW=Q(805021,10**8)
REWARD=Q(8054119,10**9)
MATHEMATICAL_MIN=Q(263917374155379049835090394947,32768000000000000000000000000000)

def sha(p):return hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n').replace(b'\r',b'\n')).hexdigest()

def original_points(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==inherited.SOURCE_SHA
    points={};region=None
    for line in path.read_text(encoding='utf8').splitlines():
        m=re.fullmatch(r'def PTL_(\d+) \(x : ℕ\) : ℕ := ptl (.+) x',line)
        if m:
            for p,pack in ast.literal_eval(m[2]):
                assert p not in points;points[p]=(pack,int(m[1]))
        if line.startswith('def REG : '):region=ast.literal_eval(line.split(':=',1)[1].strip())[:2]
    assert len(points)==2196
    return points,list(region)

def paid_exact(cell):
    """Unrounded original YA bound, with exactly the original signs/scales."""
    epi.recover(cell)
    L=cell['gap_bounds'][::2];U=cell['gap_bounds'][1::2]
    cr=[1024*10**9*b for b in epi.BS]
    base=10240000000000*sum(b*l for b,l in zip(epi.BS,L))
    for (i,j,a),atom in zip(epi.TERMS,cell['atoms']):
        k,m,p,r,l,u,l0,lb,pp,rp=atom
        c,w1,w2=epi.modes(k,m);mv=c*lb;msl=mw=mc=0
        for w,pt,pk in ((w1,p,pp),(w2,r,rp)):
            v,plus,minus=epi.fields(pk)
            mv+=w*v;msl+=w*plus;mw+=w;mc+=w*(minus-2*10**9)*max(pt-l0,0)
        base+=SC*a*mv+10*a*mc
        for t in range(i,j):cr[t]+=a*(msl-2*10**9*mw)
    p,s,cp,cm=cell['ya'][:7],cell['ya'][7:14],cell['ya'][14],cell['ya'][15]
    bound=base+10*(cm-cp)-10*sum((u-l)*max(-(c+v-w),0) for u,l,c,v,w in zip(U,L,cr,s,p))
    assert bound>=335544320000000000*cell['paid_reward_numerator']
    return Q(bound,335544320000000000*SA)

def problem(cell,added,points,region):
    # Exactly seven real gaps and 26 physical squares; no artificial
    # neighboring gap or capture of an additional frame is needed.
    spans=[(i,j) for i,j,_ in epi.TERMS]
    index={span:7+n for n,span in enumerate(spans)}
    obj=[Q(b) for b in epi.BS]+[Q(a) for _,_,a in epi.TERMS]
    cons=epi.old.constraints(cell)
    matrix=[];rhs=[]
    def add(span,slope,z,b):
        row=[Q(0)]*33
        for t in range(*span):row[t]=slope
        if z:row[index[span]]=z
        matrix.append(row);rhs.append(b)
    for (i,j),(lo,hi) in cons.items():
        add((i,j),Q(1),0,Q(hi,5*SC));add((i,j),Q(-1),0,-Q(lo,5*SC))
    for (i,j),lines in epi.forms(cell).items():
        for intercept,slope in lines:add((i,j),slope,-1,-intercept)
    baseline=len(rhs)
    seen=set()
    for i,j,p,pack,n,side in added:
        assert (i,j) in index and side in ('L','U')
        assert type(p) is int and points[p]==(pack,n)
        assert (i,j,p,pack,n,side) not in seen;seen.add((i,j,p,pack,n,side))
        lo=Q(max(cons[i,j][0]//5,sum(cell['gap_bounds'][2*t] for t in range(i,j))),SC)
        hi=Q(min(cons[i,j][1]//5,sum(cell['gap_bounds'][2*t+1] for t in range(i,j))),SC)
        assert lo<=hi
        k=(p+16384)>>15;assert k<16
        a=Q((region[0]>>(20*k))&1048575,SC);b=Q((region[1]>>(20*k))&1048575,SC)
        xp=Q(p,SC);l,u=min(lo,xp),max(hi,xp)
        assert a<=l<=xp<=u<=b
        v,plus,minus=epi.fields(pack)
        assert plus>=1 and minus>=1 and plus+minus<=4*10**9
        dm,dp=Q(plus-2*10**9,10**9),Q(2*10**9-minus,10**9)
        if side=='L':intercept=Q(v,10**10)-dp*xp+(dp-dm)*l;slope=dm
        else:intercept=Q(v,10**10)-dm*xp+(dm-dp)*u;slope=dp
        add((i,j),slope,-1,-intercept)
    bounds=[(max(Q(4,5),Q(cell['gap_bounds'][2*i],SC)),Q(cell['gap_bounds'][2*i+1],SC)) for i in range(7)]+[(Q(0),Q(1)) for _ in spans]
    assert all(lo<=hi for lo,hi in bounds)
    return obj,matrix,rhs,bounds,baseline

def dual_lower(obj,matrix,rhs,bounds,sparse):
    residual=list(obj);lower=Q(0);used=set()
    for i,mult in sparse:
        assert type(i) is int and i not in used and 0<=i<len(rhs);used.add(i)
        lam=Q(mult);assert lam>0
        lower-=lam*rhs[i]
        for j,c in enumerate(matrix[i]):
            if c:residual[j]+=lam*c
    return (lower+sum(r*(lo if r>=0 else hi) for r,(lo,hi) in zip(residual,bounds)))/SA


def replay_inherited(data,source=None):
    import am_ninth_span_certificate as ninth
    ninth.CERT=NINTH
    nc=json.loads(NINTH.read_text())
    catalog=ROOT/'output/am-ninth-span-point-catalog.json'
    points=ninth.load_catalog(catalog,nc,data,source)
    cells=data['captured_cells']+[epi.reflected(c) for c in data['captured_cells']]
    pairs,gaps,spans=inherited.geometry(cells)
    assert (len(cells),gaps,spans,len(pairs))==(482,4796,2405,2399)
    assert pairs==[(r['left'],r['right']) for r in data['pairs']]
    replacements={(r['left'],r['right']):r for r in nc['replacements']}
    assert len(replacements)==len(nc['replacements'])==47
    oldpoints={p:(pack,n) for p,pack,n in data['point_catalog']}
    unchanged=[];changed=[];allbranches=[]
    for rec in data['pairs']:
        a,b=rec['left'],rec['right']
        if (a,b) in replacements:
            replacement=replacements[a,b]
            d=epi.old.closure(epi.old.constraints(cells[a]),epi.old.constraints(cells[b]))
            branches=replacement['branches']
            assert branches and branches[0]['bounds_5sc'][0]==-d[8][0] and branches[-1]['bounds_5sc'][1]==d[0][8]
            assert all(x['bounds_5sc'][1]==y['bounds_5sc'][0] for x,y in zip(branches,branches[1:]))
            values=[]
            for branch in branches:
                prob=ninth.branch_problem(cells[a],cells[b],branch,points,data['region'])
                if prob is None:continue
                lower=inherited.dual_lower(*prob,branch['dual_sparse'])
                assert lower==Q(branch['lower'])>REWARD
                values.append(lower);allbranches.append(lower)
            assert values and min(values)==Q(replacement['lower'])
            changed.append(min(values))
        else:
            lower=inherited.dual_lower(*inherited.problem(cells[a],cells[b],rec['extra_points'],oldpoints,data['region']),rec['dual_sparse'])
            assert lower==Q(rec['lower'])>REWARD
            unchanged.append(lower)
    assert (len(unchanged),len(changed),len(allbranches))==(2352,47,84)
    assert min(unchanged+changed)==MATHEMATICAL_MIN
    return {'minimum_public_complete_cover_lower':str(min(unchanged+changed)),
            'minimum_public_unchanged_lower':str(min(unchanged)),
            'minimum_public_replacement_lower':str(min(changed)),
            'minimum_public_branch_lower':str(min(allbranches))}

def replay_canonical(formal_root,gate):
    for f,pin in gate['all_source_hashes'].items():
        assert hashlib.sha256((formal_root/f).read_bytes()).hexdigest()==pin
    reviewer=formal_root/'scripts/review_ninth_span_data.py'
    assert hashlib.sha256(reviewer.read_bytes()).hexdigest()==gate['reviewer_raw_sha256']
    saved_argv=sys.argv
    try:
        sys.argv=[str(reviewer),'--root',str(formal_root)]
        state=runpy.run_path(str(reviewer))
    finally:sys.argv=saved_argv
    assert min(state['kernel_checked_route_lowers'])==Q(gate['minimum_actual_kernel_route_lower'])>REWARD
    assert all(v>REWARD for v in state['kernel_checked_route_lowers'])
    assert all(v>REWARD for v in state['branch_lowers'])
    return True

def main():
    if not __debug__:raise SystemExit('Do not use -O: exact assertions are necessary')
    p=argparse.ArgumentParser(description=__doc__);mode=p.add_mutually_exclusive_group();mode.add_argument('--check',action='store_true',help='check new low frames and fully replay existing 2399-domain certificate');mode.add_argument('--replay-inherited',action='store_true',help='explicit alias for the complete replay included in --check');p.add_argument('--certificate',type=Path,default=ROOT/'output/am-low-frame-strengthening-certificate.json');p.add_argument('--source',type=Path);p.add_argument('--formal-root',type=Path,help='optionally pin all formal sources and replay actual canonical integer literals, without Lean');p.add_argument('--audit-output',type=Path);args=p.parse_args()
    started=time.monotonic();cert=json.loads(args.certificate.read_text());data=json.loads(REPORT.read_text())
    assert cert['schema']=='rh-weil-am-low-frame-public-v1'
    assert cert['original_report_canonical_lf_sha256']==sha(REPORT)=='3a3c8b24015162a4835f5c1d8633a4f9f8bdace26d711631dd6374c689bce04f'
    assert cert['checker_canonical_lf_sha256']==sha(Path(__file__))
    assert cert['original_source_raw_sha256']==inherited.SOURCE_SHA and cert['original_point_count']==2196
    assert cert['region']==data['region']
    assert cert['strong_reward']==str(Q(inherited.STRONG,SA))==str(Q(805803,10**8))
    assert cert['low_reward']==str(LOW) and cert['uniform_ninth_reward']==str(REWARD)
    for f,pin in data['dependency_pins'].items():assert sha(ROOT/f)==pin
    assert data['script_canonical_lf_sha256']==sha(Path(inherited.__file__))
    points={p:(pack,n) for p,pack,n in cert['point_catalog']};assert len(points)==len(cert['point_catalog'])==32
    if args.source is not None:
        full,region=original_points(args.source)
        assert region==cert['region'] and all(full[p]==v for p,v in points.items())
    paid=[paid_exact(c) for c in data['captured_cells']]
    assert [str(v) for v in paid]==cert['old_ya_lowers']
    critical=[i for i,v in enumerate(paid) if v<LOW]
    assert critical==[17,53,64,74,111,131,148,166,183,213]
    assert [r['label'] for r in cert['patches']]==critical
    used=set();dualsupport=0;addedcount=0;strengthened=paid[:]
    for rec in cert['patches']:
        label=rec['label'];assert rec['old_paid_exact']==str(paid[label])
        prob=problem(data['captured_cells'][label],rec['added_rows'],points,cert['region'])
        assert prob[4]==rec['base_rows']
        lower=dual_lower(*prob[:4],rec['dual_sparse'])
        assert lower==Q(rec['lower_exact'])>=LOW
        strengthened[label]=lower;dualsupport+=len(rec['dual_sparse']);addedcount+=len(rec['added_rows'])
        used.update((p,pack,n) for _,_,p,pack,n,_ in rec['added_rows'])
    assert used=={(p,pack,n) for p,(pack,n) in points.items()}
    assert len(strengthened)==241 and all(v>=LOW for v in strengthened)
    terms={(i,j):a for i,j,a in epi.TERMS}
    assert terms=={(7-j,7-i):a for (i,j),a in terms.items()} and epi.BS==list(reversed(epi.BS))
    assert len(data['captured_cells']+[epi.reflected(c) for c in data['captured_cells']])==482
    # Default public checking replays every existing physical domain and its
    # unchanged multipliers, not merely an inherited numerical summary.
    gate=cert['inherited_ninth_exact_gate']
    assert gate['status']=='PASS' and gate['public_unchanged_domains']==2352 and gate['public_replacement_domains']==47 and gate['closed_branches']==84
    assert gate['all_source_hashes']['output/am-ninth-span-certificate.json']==sha(NINTH)=='9fc7f9d8a00ebbc3e2f8ff236b247af5ac3173c3942ec72b9180c4473a65cf96'
    assert sha(ROOT/'output/am-ninth-span-point-catalog.json')=='cda8ce5fce3d0a639975f54e57b1991c7d5a2a2cb112df4e3dd13237a954fb27'
    assert sha(ROOT/'scripts/am_ninth_span_certificate.py')=='b03b3259a385702300520bd02f33c79d228b76a0e07c6b42cec23b6a02a5e673'
    expected_sources={'RecordProportion/NinthSpanFiniteData.lean','RecordProportion/NinthSpanFinite.lean','RecordProportion/NinthSpanPoints.lean','RecordProportion/NinthSpanLocal.lean','RecordProportion/NinthSpan.lean','RecordProportion/NinthSpanAnalytic.lean','RecordProportion/NinthSpanPathSoundness.lean','RecordProportion/FiniteCertificateData.lean','RecordProportion/FiniteCertificate.lean','scripts/generate_ninth_span_certificate.py','output/am-ninth-span-certificate.json','output/am-ninth-span-point-catalog.json','output/am-expanded-nine-point-certificate.json'}
    assert set(gate['all_source_hashes'])==expected_sources
    replay=replay_inherited(data,args.source)
    for key,value in replay.items():assert gate[key]==value
    assert gate['minimum_public_complete_cover_lower']==str(MATHEMATICAL_MIN)
    assert Q(gate['minimum_public_branch_lower'])>REWARD and Q(gate['minimum_public_unchanged_lower'])>REWARD
    canonical=Q(gate['minimum_actual_kernel_route_lower'])
    # The canonical summary is informational unless the actual formal root
    # is supplied. It is not needed for the fully rechecked public theorem.
    canonical_replayed=replay_canonical(args.formal_root,gate) if args.formal_root is not None else False
    actual_low=min(strengthened);outer=(Q(805803,10**8)+actual_low)/2
    assert outer>MATHEMATICAL_MIN>REWARD
    assert (Q(805803,10**8)+LOW)/2==Q(805412,10**8)>REWARD
    ratio=Q(66812491,10**8)/(1-REWARD);exactratio=Q(66812491,10**8)/(1-MATHEMATICAL_MIN);old=Q(941021,1397107)
    assert ratio==Q(668124910,991945881)
    oldpointset={p for c in data['captured_cells'] for a in c['atoms'] for p in (a[2],a[3])}|{p for p,*_ in data['point_catalog']}
    result={'status':'PASS','scope':'complete finite single-frame strengthening and all2399-domain exact assembly under disclosed existing continuous and analytic admission','certificate_canonical_lf_sha256':sha(args.certificate),'checker_canonical_lf_sha256':sha(Path(__file__)),'source_matched':args.source is not None,'low_original_labels':241,'reflected_low_labels':241,'patched_original_labels':critical,'unchanged_ya_original_labels':231,'new_tangent_rows':addedcount,'positive_dual_support_total':dualsupport,'used_original_point_count':len(points),'points_outside_old_1089_catalog':sorted(set(points)-oldpointset),'global_F8_reward':str(LOW),'minimum_actual_low_reward':str(actual_low),'safe_high_low_reward':str(Q(805412,10**8)),'exact_high_low_reward':str(outer),'inherited_public_low_low_reward':str(MATHEMATICAL_MIN),'inherited_actual_canonical_kernel_route_reward':str(canonical),'uniform_reward':str(REWARD),'simple_critical_proportion':str(ratio),'simple_critical_percent_float':100*float(ratio),'exact_finite_minimum_proportion':str(exactratio),'gain_percentage_points_exact':str(100*(ratio-old)),'gain_percentage_points_float':100*float(ratio-old),'elapsed_seconds':time.monotonic()-started,'standard_library_only_check':True,'inherited_2399_certificate_replayed_this_run':True,'canonical_literals_replayed_this_run':canonical_replayed,'all_canonical_current_source_hashes_matched':canonical_replayed,'canonical_receipt_scope':'informational and not needed for public mathematical payment unless --formal-root rechecks every raw source hash and all actual integer literals','new_lean_or_nanoda_check_performed':False,'website_accepted':False}
    if args.audit_output is not None:args.audit_output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

"""Whole-domain frame/pair certificate for round505, Python stdlib only.

The original continuous AM, original 2196 PTL/REG, complete strong capture,
and all-zero transport remain explicit admitted mathematical dependencies.
Float searches are separate scripts. This checker consumes only Fractions.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,json,sys,time
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'output/am-low-frame-strengthening-certificate.json').is_file())
W=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scripts'))
import am_low_frame_strengthening_certificate as low
import am_ninth_span_certificate as ninth
epi=low.epi
SC,SA=low.SC,low.SA
ELL=Q(805094,10**8)

def sha(path):return hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n').replace(b'\r',b'\n')).hexdigest()

def frame_closure(cell,span,lo=None,hi=None):
    d=[[0 if i==j else 10**30 for j in range(8)] for i in range(8)]
    for (i,j),(a,b) in epi.old.constraints(cell).items():d[i][j]=min(d[i][j],b);d[j][i]=min(d[j][i],-a)
    if lo is not None:
        assert type(lo) is int and type(hi) is int and lo<=hi
        i,j=span;d[i][j]=min(d[i][j],hi);d[j][i]=min(d[j][i],-lo)
    for k in range(8):
        for i in range(8):
            for j in range(8):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
        if any(d[i][i]<0 for i in range(8)):return None
    return d

def frame_branch_problem(cell,record,branch,points,region):
    span=record['span'];lo,hi=branch['bounds_5sc'];d=frame_closure(cell,span,lo,hi)
    if branch['empty']:
        assert d is None;return None
    assert d is not None
    obj,A,b,bounds,base=low.problem(cell,[],points,region)
    assert base==branch['base_rows']
    index={(i,j):7+n for n,(i,j,_) in enumerate(epi.TERMS)}
    bounds[:7]=[(max(Q(4,5),Q(-d[i+1][i],5*SC)),Q(d[i][i+1],5*SC)) for i in range(7)]
    assert all(a<=z for a,z in bounds)
    for desc in branch['added_rows']:
        tag,i,j=desc[:3];assert 0<=i<j<=7
        row=[Q(0)]*33
        if tag in ('closure-upper','closure-lower'):
            assert len(desc)==3
            sign=Q(1) if tag=='closure-upper' else Q(-1)
            bound=Q(d[i][j] if sign==1 else d[j][i],5*SC)
            for t in range(i,j):row[t]=sign
        else:
            assert tag=='tangent' and len(desc)==7 and (i,j) in index
            p,pack,n,side=desc[3:];assert points[p]==(pack,n) and side in ('L','U')
            k=(p+16384)>>15;assert k<16
            a=Q((region[0]>>(20*k))&1048575,SC);z=Q((region[1]>>(20*k))&1048575,SC)
            lo,hi=Q(-d[j][i],5*SC),Q(d[i][j],5*SC);xp=Q(p,SC);l,u=min(lo,xp),max(hi,xp)
            assert a<=l<=xp<=u<=z
            v,plus,minus=epi.fields(pack);assert plus>=1 and minus>=1 and plus+minus<=4*10**9
            dm,dp=Q(plus-2*10**9,10**9),Q(2*10**9-minus,10**9)
            if side=='L':intercept=Q(v,10**10)-dp*xp+(dp-dm)*l;slope=dm
            else:intercept=Q(v,10**10)-dm*xp+(dm-dp)*u;slope=dp
            for t in range(i,j):row[t]=slope
            row[index[i,j]]=Q(-1);bound=-intercept
        A.append(row);b.append(bound)
    return obj,A,b,bounds

def check(path,source=None,audit_output=None):
    started=time.monotonic();cert=json.loads(path.read_text());assert cert['schema']=='rh-weil-am-joint-frame-pair-505-v1'
    assert cert['checker_canonical_lf_sha256']==sha(Path(__file__))
    for name,pin in cert['dependency_canonical_lf_sha256'].items():assert sha(ROOT/name)==pin
    assert sha(low.REPORT)=='3a3c8b24015162a4835f5c1d8633a4f9f8bdace26d711631dd6374c689bce04f'
    old=json.loads(low.REPORT.read_text());base=json.loads((ROOT/'output/am-ninth-span-certificate.json').read_text())
    assert cert['global_F8_reward']==str(ELL) and cert['strong_reward']==str(Q(805803,SA))
    target=Q(cert['uniform_F9_reward']);assert Q(8054119,10**9)<target<Q(1,40)
    assert cert['original_source_raw_sha256']==low.inherited.SOURCE_SHA and cert['region']==old['region'] and cert['original_point_count']==2196
    points={p:(pack,n) for p,pack,n in cert['point_catalog']};assert len(points)==len(cert['point_catalog'])
    if source is not None:
        full,region=low.original_points(source);assert region==cert['region'] and all(full[p]==v for p,v in points.items())
    paid=[low.paid_exact(c) for c in old['captured_cells']];assert [str(v) for v in paid]==cert['old_ya_lowers']
    critical=[i for i,v in enumerate(paid) if v<ELL]
    frame_labels=[r['label'] for r in cert['frame_patches']];split_labels=[r['label'] for r in cert['frame_split_patches']]
    assert len(set(frame_labels))==len(frame_labels) and len(set(split_labels))==len(split_labels) and not set(frame_labels)&set(split_labels)
    assert set(critical)==set(frame_labels+split_labels)
    strengthened=paid[:];frame_support=0;frame_rows=0;used=set()
    for rec in cert['frame_patches']:
        label=rec['label'];prob=low.problem(old['captured_cells'][label],rec['added_rows'],points,cert['region'])
        assert prob[4]==rec['base_rows']
        value=low.dual_lower(*prob[:4],rec['dual_sparse']);assert value==Q(rec['lower_exact'])>=ELL
        strengthened[label]=value;frame_support+=len(rec['dual_sparse']);frame_rows+=len(rec['added_rows'])
        used.update((p,pack,n) for _,_,p,pack,n,_ in rec['added_rows'])
    split_count=0
    for rec in cert['frame_split_patches']:
        label=rec['label'];span=rec['span'];assert 0<=span[0]<span[1]<=7
        cell=old['captured_cells'][label];d=frame_closure(cell,span);assert d
        expected=[-d[span[1]][span[0]],d[span[0]][span[1]]]
        assert rec['original_bounds_5sc']==expected
        bs=rec['branches'];assert bs and bs[0]['bounds_5sc'][0]==expected[0] and bs[-1]['bounds_5sc'][1]==expected[1]
        assert all(x['bounds_5sc'][1]==y['bounds_5sc'][0] for x,y in zip(bs,bs[1:]))
        vals=[]
        for b in bs:
            split_count+=1;prob=frame_branch_problem(cell,rec,b,points,cert['region'])
            if prob is None:continue
            value=low.dual_lower(*prob,b['dual_sparse']);assert value==Q(b['lower'])>=ELL
            vals.append(value);frame_support+=len(b['dual_sparse']);frame_rows+=len(b['added_rows'])
            used.update((x[3],x[4],x[5]) for x in b['added_rows'] if x[0]=='tangent')
        assert vals and min(vals)==Q(rec['lower']);strengthened[label]=min(vals)
    assert all(v>=ELL for v in strengthened)
    terms={(i,j):a for i,j,a in epi.TERMS};assert epi.BS==list(reversed(epi.BS)) and terms=={(7-j,7-i):a for (i,j),a in terms.items()}
    originals=old['captured_cells'];cells=originals+[epi.reflected(c) for c in originals]
    pairs,gaps,spans=low.inherited.geometry(cells);assert (len(cells),gaps,spans,len(pairs))==(482,4796,2405,2399)
    assert pairs==[(r['left'],r['right']) for r in old['pairs']]
    newpairs={(r['left'],r['right']):r for r in cert['pair_patches']};assert len(newpairs)==len(cert['pair_patches']) and set(newpairs)<=set(pairs)
    priorpairs={(r['left'],r['right']):r for r in base['replacements']};assert len(priorpairs)==47
    ninth.CERT=ROOT/'output/am-ninth-span-certificate.json'
    priorpoints=ninth.load_catalog(ROOT/'output/am-ninth-span-point-catalog.json',base,old,source)
    oldpoints={p:(pack,n) for p,pack,n in old['point_catalog']}
    complete=[];prior_branch_count=0;new_branch_count=0;old_count=0;newpair_support=0;newpair_tangents=0
    for previous in old['pairs']:
        a,b=previous['left'],previous['right'];key=(a,b)
        if key in newpairs or key in priorpairs:
            fresh=key in newpairs;r=newpairs[key] if fresh else priorpairs[key]
            d=epi.old.closure(epi.old.constraints(cells[a]),epi.old.constraints(cells[b]));assert d
            bs=r['branches'];assert bs and bs[0]['bounds_5sc'][0]==-d[8][0] and bs[-1]['bounds_5sc'][1]==d[0][8]
            assert all(x['bounds_5sc'][1]==y['bounds_5sc'][0] for x,y in zip(bs,bs[1:]))
            vals=[]
            for br in bs:
                if fresh:new_branch_count+=1
                else:prior_branch_count+=1
                prob=ninth.branch_problem(cells[a],cells[b],br,points if fresh else priorpoints,old['region'])
                if prob is None:continue
                value=low.inherited.dual_lower(*prob,br['dual_sparse']);assert value==Q(br['lower'])>target
                vals.append(value)
                if fresh:
                    newpair_support+=len(br['dual_sparse']);newpair_tangents+=sum(x[0]=='tangent' for x in br['added_rows'])
                    used.update((x[3],x[4],x[5]) for x in br['added_rows'] if x[0]=='tangent' and x[6]=='direct-region')
            assert vals and min(vals)==Q(r['lower']);value=min(vals)
        else:
            old_count+=1
            value=low.inherited.dual_lower(*low.inherited.problem(cells[a],cells[b],previous['extra_points'],oldpoints,old['region']),previous['dual_sparse'])
            assert value==Q(previous['lower'])>target
        complete.append((key,value))
    assert len(complete)==2399 and used=={(p,pack,n) for p,(pack,n) in points.items()}
    finite_min=min(v for _,v in complete);outside=(Q(805803,SA)+ELL)/2;exact_outside=(Q(805803,SA)+min(strengthened))/2
    assert finite_min>target and outside>target
    ratio=Q(66812491,SA)/(1-target);oldratio=Q(668124910,991945881)
    best=min(finite_min,exact_outside);exactratio=Q(66812491,SA)/(1-best)
    result={'status':'PASS','scope':'all real-gap frame and pair finite certificates under unchanged continuous original AM/capture admission; all-zero analytic assembly unchanged','certificate_canonical_lf_sha256':sha(path),'checker_canonical_lf_sha256':sha(Path(__file__)),'source_matched':source is not None,'frame_unsplit_patches':len(frame_labels),'frame_split_patches':len(split_labels),'frame_closed_branches':split_count,'frame_original_YA_retained':241-len(frame_labels)-len(split_labels),'frame_positive_dual_support':frame_support,'frame_added_rows':frame_rows,'new_pair_domains':len(newpairs),'new_pair_closed_branches':new_branch_count,'prior_ninth_closed_branches':prior_branch_count,'old_pair_multipliers_retained':old_count,'new_pair_positive_dual_support':newpair_support,'new_pair_positive_tangent_rows':newpair_tangents,'used_original_points':len(points),'ordered_low_low_domains':2399,'global_F8_reward':str(ELL),'minimum_exact_low_frame':str(min(strengthened)),'minimum_frame_labels':[i for i,v in enumerate(strengthened) if v==min(strengthened)],'minimum_low_low':str(finite_min),'minimum_pair_labels':[list(key) for key,v in complete if v==finite_min],'safe_outside':str(outside),'exact_outside':str(exact_outside),'uniform_reward':str(target),'maximum_reward_paid_by_current_data':str(best),'simple_critical_proportion':str(ratio),'simple_critical_percent':100*float(ratio),'gain_percentage_points_exact':str(100*(ratio-oldratio)),'gain_percentage_points':100*float(ratio-oldratio),'exact_current_data_proportion':str(exactratio),'strict_margins':{'low_low':str(finite_min-target),'outside':str(outside-target)},'elapsed_seconds':time.monotonic()-started,'new_lean_or_nanoda_check_performed':False,'website_accepted':False}
    if audit_output is not None:audit_output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
    print(json.dumps(result,indent=2))
    return result

def main():
    if not __debug__:
        raise SystemExit('Assertions required; do not use -O')
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true',help='recompute the complete fixed certificate')
    p.add_argument('--certificate',type=Path,default=ROOT/'output/am-joint-frame-pair-certificate.json')
    p.add_argument('--source',type=Path,help='optional pinned original PTL/REG source; no Lean invocation')
    p.add_argument('--audit-output',type=Path,help='optional output receipt, default check writes nothing')
    args=p.parse_args()
    check(args.certificate,args.source,args.audit_output)
if __name__=='__main__':
    main()

"""Round506 whole-domain outer-frame certificate, Python standard library only.

Uses the unchanged admitted continuous AM/capture/PTL/REG and analytic
all-zero transport. Replays mathematical finite witnesses, including a
distinct 201-cell base-only dual adapter. Does not invoke Lean or claim a
new Lean/NaNoDa or website result.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,json,sys,time

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'output/am-joint-frame-pair-certificate.json').is_file())
sys.path.insert(0,str(ROOT/'scripts'))
import am_joint_frame_pair_certificate as inherited
old=inherited.low
epi=old.epi
SC,SA=old.SC,old.SA
ELL=Q(805117,10**8)
REWARD=Q(805460,10**8)
STRONG=Q(805803,10**8)
ADAPTER_PIN='6871cc80f90aea753ac9db95321f6f6099a4b50fbe2fd2494e475251eb8140ec'

def sha(path):
    return hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n').replace(b'\r',b'\n')).hexdigest()

def frame_closure(cell,span=None,lo=None,hi=None):
    d=[[0 if i==j else 10**30 for j in range(8)] for i in range(8)]
    for (i,j),(a,b) in epi.old.constraints(cell).items():
        d[i][j]=min(d[i][j],b);d[j][i]=min(d[j][i],-a)
    if span is not None:
        assert type(lo) is int and type(hi) is int and lo<=hi
        i,j=span;assert 0<=i<j<=7
        d[i][j]=min(d[i][j],hi);d[j][i]=min(d[j][i],-lo)
    for k in range(8):
        for i in range(8):
            for j in range(8):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
        if any(d[i][i]<0 for i in range(8)):return None
    return d

def frame_problem(cell,span,branch,points,region):
    lo,hi=branch['bounds_5sc'];d=frame_closure(cell,span,lo,hi)
    if branch['empty']:
        assert d is None;return None
    assert d is not None and branch['closure_5sc']==d
    obj,A,b,bounds,base=old.problem(cell,[],points,region)
    assert base==branch['base_rows']
    bounds[:7]=[(max(Q(4,5),Q(-d[i+1][i],5*SC)),Q(d[i][i+1],5*SC)) for i in range(7)]
    assert all(L<=U for L,U in bounds)
    index={(i,j):7+n for n,(i,j,_) in enumerate(epi.TERMS)}
    seen=set()
    for desc in branch['added_rows']:
        tag,i,j=desc[:3];assert 0<=i<j<=7
        assert tuple(desc) not in seen;seen.add(tuple(desc))
        row=[Q(0)]*33
        if tag in ('closure-upper','closure-lower'):
            assert len(desc)==3
            slope=Q(1) if tag=='closure-upper' else Q(-1)
            bound=Q(d[i][j] if slope==1 else d[j][i],5*SC)
        else:
            assert tag=='tangent' and len(desc)==7 and (i,j) in index
            p,pack,n,side=desc[3:];assert points[p]==(pack,n) and side in ('L','U')
            k=(p+16384)>>15;assert k<16
            a=Q((region[0]>>(20*k))&1048575,SC);z=Q((region[1]>>(20*k))&1048575,SC)
            L,U,xp=Q(-d[j][i],5*SC),Q(d[i][j],5*SC),Q(p,SC)
            l,u=min(L,xp),max(U,xp);assert a<=l<=xp<=u<=z
            v,plus,minus=epi.fields(pack);assert plus>=1 and minus>=1 and plus+minus<=4*10**9
            dm,dp=Q(plus-2*10**9,10**9),Q(2*10**9-minus,10**9)
            if side=='L':intercept,slope=Q(v,10**10)-dp*xp+(dp-dm)*l,dm
            else:intercept,slope=Q(v,10**10)-dm*xp+(dm-dp)*u,dp
            row[index[i,j]]=Q(-1);bound=-intercept
        for t in range(i,j):row[t]=slope
        A.append(row);b.append(bound)
    return obj,A,b,bounds

def replay_pairs(data,prior,source=None):
    """Replay all 2399 old witnesses, never consume a gate minimum summary."""
    ninth=inherited.ninth
    base=json.loads((ROOT/'output/am-ninth-span-certificate.json').read_text())
    originals=data['captured_cells'];cells=originals+[epi.reflected(c) for c in originals]
    pairs,gaps,spans=old.inherited.geometry(cells)
    assert (len(cells),gaps,spans,len(pairs))==(482,4796,2405,2399)
    assert pairs==[(r['left'],r['right']) for r in data['pairs']]
    replacements={(r['left'],r['right']):r for r in prior['pair_patches']}
    oldreplacements={(r['left'],r['right']):r for r in base['replacements']}
    assert len(replacements)==10 and len(oldreplacements)==47
    points={p:(pack,n) for p,pack,n in prior['point_catalog']}
    ninth.CERT=ROOT/'output/am-ninth-span-certificate.json'
    ninthpoints=ninth.load_catalog(ROOT/'output/am-ninth-span-point-catalog.json',base,data,source)
    oldpoints={p:(pack,n) for p,pack,n in data['point_catalog']}
    values=[];counts={'new505_domains':0,'prior503_domains':0,'old_domains':0,'new505_branches':0,'prior503_branches':0}
    for rec in data['pairs']:
        a,b=rec['left'],rec['right'];key=(a,b)
        if key in replacements or key in oldreplacements:
            fresh=key in replacements;r=replacements[key] if fresh else oldreplacements[key]
            d=epi.old.closure(epi.old.constraints(cells[a]),epi.old.constraints(cells[b]));assert d
            branches=r['branches']
            assert branches and branches[0]['bounds_5sc'][0]==-d[8][0] and branches[-1]['bounds_5sc'][1]==d[0][8]
            assert all(x['bounds_5sc'][1]==y['bounds_5sc'][0] for x,y in zip(branches,branches[1:]))
            live=[];counts['new505_domains' if fresh else 'prior503_domains']+=1
            for branch in branches:
                counts['new505_branches' if fresh else 'prior503_branches']+=1
                prob=ninth.branch_problem(cells[a],cells[b],branch,points if fresh else ninthpoints,data['region'])
                if prob is None:continue
                value=old.inherited.dual_lower(*prob,branch['dual_sparse'])
                assert value==Q(branch['lower'])>REWARD
                live.append(value)
            assert live and min(live)==Q(r['lower']);value=min(live)
        else:
            counts['old_domains']+=1
            value=old.inherited.dual_lower(*old.inherited.problem(cells[a],cells[b],rec['extra_points'],oldpoints,data['region']),rec['dual_sparse'])
            assert value==Q(rec['lower'])>REWARD
        values.append((key,value))
    assert len(values)==2399
    assert counts=={'new505_domains':10,'prior503_domains':47,'old_domains':2342,'new505_branches':20,'prior503_branches':84}
    minimum=min(v for _,v in values)
    return minimum,[list(k) for k,v in values if v==minimum],counts

def check(path,source=None,audit_output=None):
    started=time.monotonic();cert=json.loads(path.read_text(encoding='utf8'))
    assert cert['schema']=='rh-weil-am-outer-frame-506-v1'
    assert cert['checker_canonical_lf_sha256']==sha(Path(__file__))
    for name,pin in cert['dependency_canonical_lf_sha256'].items():assert sha(ROOT/name)==pin
    prior=json.loads((ROOT/'output/am-joint-frame-pair-certificate.json').read_text(encoding='utf8'))
    assert prior['checker_canonical_lf_sha256']==sha(Path(inherited.__file__))
    for name,pin in prior['dependency_canonical_lf_sha256'].items():assert sha(ROOT/name)==pin
    assert sha(old.REPORT)=='3a3c8b24015162a4835f5c1d8633a4f9f8bdace26d711631dd6374c689bce04f'
    data=json.loads(old.REPORT.read_text(encoding='utf8'))
    assert cert['original_source_raw_sha256']==old.inherited.SOURCE_SHA and cert['original_point_count']==2196
    assert cert['region']==data['region']==prior['region']
    assert cert['global_F8_reward']==str(ELL) and cert['uniform_F9_reward']==str(REWARD) and cert['strong_reward']==str(STRONG)
    assert cert['base33_adapter_raw_sha256']==ADAPTER_PIN
    adapter=cert['base33_adapter']
    adapter_bytes=(json.dumps(adapter,indent=2)+'\n').encode('utf8')
    assert hashlib.sha256(adapter_bytes).hexdigest()==ADAPTER_PIN
    points={p:(pack,n) for p,pack,n in cert['point_catalog']}
    assert len(points)==len(cert['point_catalog'])
    priorpoints={p:(pack,n) for p,pack,n in prior['point_catalog']}
    if source is not None:
        full,region=old.original_points(source)
        assert region==cert['region'] and all(full[p]==v for p,v in points.items()) and all(full[p]==v for p,v in priorpoints.items())
    original_labels=set(range(241))
    oldpatches={r['label']:r for r in prior['frame_patches']}
    oldsplit={r['label']:r for r in prior['frame_split_patches']}
    assert len(oldpatches)==39 and set(oldsplit)=={17}
    adapter_labels={r['label'] for r in adapter['records']}
    assert len(adapter_labels)==len(adapter['records'])==201 and adapter_labels==original_labels-set(oldpatches)-set(oldsplit)
    frame_values={};baseline_values=[]
    for rec in adapter['records']:
        label=rec['label'];assert rec['added_rows']==[]
        prob=old.problem(data['captured_cells'][label],[],{},data['region'])
        assert rec['base_rows']==prob[4] and Q(rec['original_YA_exact'])==old.paid_exact(data['captured_cells'][label])
        value=old.dual_lower(*prob[:4],rec['dual_sparse']);assert value==Q(rec['lower_exact'])>=ELL
        frame_values[label]=value;baseline_values.append((label,value))
    fresh={r['label']:r for r in cert['frame_patches']}
    assert len(fresh)==len(cert['frame_patches'])==5 and set(fresh)=={17,69,74,131,183}
    retained=[]
    for label,rec in oldpatches.items():
        if label in fresh:continue
        prob=old.problem(data['captured_cells'][label],rec['added_rows'],priorpoints,data['region'])
        assert prob[4]==rec['base_rows']
        value=old.dual_lower(*prob[:4],rec['dual_sparse']);assert value==Q(rec['lower_exact'])>=ELL
        frame_values[label]=value;retained.append((label,value))
    assert len(retained)==35
    used=set();newcases=[];support=rows=0
    for label,rec in fresh.items():
        cell=data['captured_cells'][label];span=rec['span'];d=frame_closure(cell)
        assert rec['original_bounds_5sc']==[-d[span[1]][span[0]],d[span[0]][span[1]]]
        bs=rec['branches']
        assert bs and bs[0]['bounds_5sc'][0]==rec['original_bounds_5sc'][0] and bs[-1]['bounds_5sc'][1]==rec['original_bounds_5sc'][1]
        assert all(x['bounds_5sc'][1]==y['bounds_5sc'][0] for x,y in zip(bs,bs[1:]))
        live=[]
        for n,br in enumerate(bs):
            prob=frame_problem(cell,span,br,points,data['region'])
            if prob is None:continue
            value=old.dual_lower(*prob,br['dual_sparse']);assert value==Q(br['lower'])>=ELL
            live.append(value);newcases.append((label,n,value));support+=len(br['dual_sparse']);rows+=len(br['added_rows'])
            used.update((x[3],x[4],x[5]) for x in br['added_rows'] if x[0]=='tangent')
        assert live and min(live)==Q(rec['lower']);frame_values[label]=min(live)
    assert used=={(p,pack,n) for p,(pack,n) in points.items()}
    assert set(frame_values)==original_labels and all(v>=ELL for v in frame_values.values())
    terms={(i,j):a for i,j,a in epi.TERMS}
    assert epi.BS==list(reversed(epi.BS)) and terms=={(7-j,7-i):a for (i,j),a in terms.items()}
    pair_min,pair_labels,paircounts=replay_pairs(data,prior,source)
    frame_min=min(frame_values.values());outside=(STRONG+ELL)/2;exact_outside=(STRONG+frame_min)/2
    assert outside==REWARD and exact_outside>REWARD and pair_min>REWARD
    best=min(pair_min,exact_outside);ratio=Q(66812491,SA)/(1-REWARD);priorratio=Q(66812491,99194552)
    result={'status':'PASS','scope':'all real frame and ordered pair finite certificates under unchanged continuous AM/capture/PTL/REG admission and all-zero analytic transport',
            'certificate_canonical_lf_sha256':sha(path),'checker_canonical_lf_sha256':sha(Path(__file__)),
            'source_matched':source is not None,'single_frame_original_labels':241,'single_frame_reflected_labels':241,
            'base_only_distinct_adapter_frames':201,'retained_505_frame_patches':35,'new_frame_labels':sorted(fresh),
            'new_frame_closed_cases':len(newcases),'total_frame_paid_cases':201+35+len(newcases),
            'new_frame_positive_dual_support':support,'new_frame_added_rows':rows,'new_frame_used_original_points':len(points),
            'minimum_exact_frame':str(frame_min),'minimum_frame_labels':[i for i,v in frame_values.items() if v==frame_min],
            'minimum_new_cases':[[i,n] for i,n,v in newcases if v==frame_min],
            'minimum_base_only_adapter':str(min(v for _,v in baseline_values)),
            'minimum_retained_505_frames':str(min(v for _,v in retained)),
            'ordered_low_low_domains':2399,'pair_witness_counts':paircounts,'minimum_exact_pair':str(pair_min),'minimum_pair_labels':pair_labels,
            'global_F8_reward':str(ELL),'strong_reward':str(STRONG),'safe_outside':str(outside),'exact_paid_outside':str(exact_outside),
            'uniform_F9_reward':str(REWARD),'maximum_uniform_reward_paid_by_fixed_data':str(best),
            'simple_critical_proportion':str(ratio),'simple_critical_percent':100*float(ratio),
            'gain_percentage_points_exact':str(100*(ratio-priorratio)),'gain_percentage_points':100*float(ratio-priorratio),
            'strict_actual_margins':{'frame':str(frame_min-ELL),'pair':str(pair_min-REWARD),'exact_outside':str(exact_outside-REWARD)},
            'safe_outside_margin':'0','new_lean_or_nanoda_check_performed':False,'website_accepted':False,
            'elapsed_seconds':time.monotonic()-started}
    if audit_output is not None:audit_output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
    print(json.dumps(result,indent=2));return result

def main():
    if not __debug__:raise SystemExit('Assertions required; do not use -O')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true')
    ap.add_argument('--certificate',type=Path,default=ROOT/'output/am-outer-frame-certificate.json')
    ap.add_argument('--source',type=Path);ap.add_argument('--audit-output',type=Path);args=ap.parse_args()
    check(args.certificate,args.source,args.audit_output)
if __name__=='__main__':main()

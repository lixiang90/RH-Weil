"""Capture old PC8 low-slack leaves and check their exact adjacent geometry.

--check checks the committed captured data only. --replay builds an isolated
instrumented copy of the admitted core and compares actual Lean runtime data.
No command certifies a positive uniform nine-point reward or new proportion.
The fixed upstream source must already be at tmp/pc8-am-admission/Solution.lean.
"""
import argparse
import ast
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re
import subprocess

import am_pc8_finite_replay as old

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT/'output/am-nine-point-low-slack-cover.json'
WORK = ROOT/'tmp/pdfs/am-nine-point-low-slack'
SPANS = [(i,j) for i in range(6) for j in range(i+2,8)]
SC, REWARD, STRONG = 32768, 805003, 805203
TARGET = 805103


def sha(raw):
    return hashlib.sha256(raw.replace(b'\r\n',b'\n').replace(b'\r',b'\n')).hexdigest()


def decode_log(raw):
    return raw.decode('utf-16' if raw.startswith(b'\xff\xfe') else 'utf-8-sig')


def parse_log(log):
    checks=[]; cells=[]; waiting=None
    assert not re.search(r'error:|error\(|Stack overflow|Aborting|sorry|panic',log)
    for line in log.splitlines():
        match=re.fullmatch(r'PILOT (\S+) (true|false)',line)
        if match:
            assert waiting is None
            checks.append(match.groups())
        elif line.startswith('LOWCELL '):
            assert waiting is None
            a,b=line[8:].split('|')
            waiting={'gap_bounds':ast.literal_eval(a),'span_bounds':ast.literal_eval(b)}
        elif line.startswith('LOWPAID '):
            assert waiting is not None
            waiting['paid_reward_numerator']=int(line[8:])
            cells.append(waiting); waiting=None
    names=['large-gap7','adjacent7']+[f'cover-{i}' for i in range(7)]+[f'root-{i}' for i in range(32)]
    assert checks==[(name,'true') for name in names] and waiting is None
    assert len(cells)==70
    return cells


def build_instrumented():
    raw=(old.WORK/'Solution.lean').read_bytes()
    assert len(raw)==1675641 and hashlib.sha256(raw).hexdigest()==old.SOURCE_SHA
    lines=raw.decode('utf-8').splitlines()
    core,_=old.extract(lines)
    for name in ('AMPC8StructuralBridge.lean','AMPC8MinorantBridge.lean'):
        core+='\n'+old.canonical((ROOT/'formal/certificates'/name).read_bytes()).decode('utf-8')
    admitted=json.loads((ROOT/'output/am-pc8-finite-replay.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(core.encode('utf-8')).hexdigest()==admitted['numeric_core_sha256']

    def block(name):
        match=re.search(r'^def '+name+r'\b',core,re.M)
        assert match
        end=core.index('-- Fixed source',match.end())
        return match.start(),end,core[match.start():end]

    _,end_check,checker=block('mcheckP')
    assert len(re.findall(r'\bcN\b',checker))==1
    strong=checker.replace('def mcheckP ','def mcheckStrongP (cTarget : ℕ) ',1)
    strong=re.sub(r'\bcN\b','cTarget',strong)
    start,end,leaf=block('mleafP')
    begin=leaf.index('(fun y : YA => ')+len('(fun y : YA => ')
    match=re.search(r'\)\n\s*\(ydec',leaf[begin:])
    assert match
    finish=begin+match.start(); body=leaf[begin:finish]
    calls=re.findall(r'\(mcheckP [^()]*\)',body)
    assert len(calls)==1
    stronger=calls[0].replace('(mcheckP ','(mcheckStrongP 805203 ',1)
    gap_fields=[x for i in range(7) for x in (f's.l{i}',f's.u{i}')]
    span_fields=[x for i,j in SPANS for x in (f's.A{i}{j}',f's.B{i}{j}')]
    message='LOWCELL {['+', '.join(gap_fields)+']}|{['+', '.join(span_fields)+']}'
    callback=('\n   let result := '+body+'\n'
              '   if '+stronger+' || result == 0 then result else\n'
              '     let paid := lowMaxReward (fun reward => '+stronger.replace('805203','reward',1)+') 8 805003 805203\n'
              '     dbg_trace s!"'+message+'"\n'
              '     dbg_trace s!"LOWPAID {paid}"\n'
              '     result')
    leaf=leaf[:begin]+callback+leaf[finish:]
    helper=('def lowMaxReward (test : ℕ → Bool) : ℕ → ℕ → ℕ → ℕ\n'
            ' | 0, lo, _ => lo\n | fuel+1, lo, hi =>\n'
            '   if lo+1 < hi then\n     let mid := (lo+hi)/2\n'
            '     if test mid then lowMaxReward test fuel mid hi\n'
            '     else lowMaxReward test fuel lo mid\n   else lo\n\n')
    instrumented=core[:start]+leaf+core[end:]
    instrumented=instrumented[:end_check]+strong+helper+instrumented[end_check:]
    assert instrumented.count('def cN : ℕ := 805003')==1
    checks=[(name,expr) for name,expr in old.planned_checks(lines)
            if name in ('large-gap7','adjacent7') or name.startswith(('cover-','root-')) and name!='root-W']
    assert len(checks)==41
    tail=('\nnamespace RewardPilot\nopen AMW.Cert AMW.Cert.Pyr AMW.Cert.PyrD '
          'AMW.Cert.PCell AMW.Cert.PC8CL AMW.Cert.PC8CLData\n'
          'def emit (name : String) (passed : Bool) : IO Unit := '
          'IO.println ("PILOT " ++ name ++ " " ++ toString passed)\n')
    tail+='\n'.join('#eval emit "'+name+'" ('+expr+')' for name,expr in checks)
    return instrumented+tail+'\nend RewardPilot\n'


def constraints(cell):
    a,b=cell['gap_bounds'],cell['span_bounds']
    assert len(a)==14 and len(b)==42
    assert all(type(x) is int and x>=0 for x in a+b)
    out={(i,i+1):(5*a[2*i],5*a[2*i+1]) for i in range(7)}
    out.update({span:(5*b[2*k],5*b[2*k+1]) for k,span in enumerate(SPANS)})
    assert all(lo<=hi for lo,hi in out.values())
    assert REWARD<=cell['paid_reward_numerator']<STRONG
    return out


def closure(left,right):
    infinity=10**30
    d=[[0 if i==j else infinity for j in range(9)] for i in range(9)]
    for cell,offset in ((left,0),(right,1)):
        for (i,j),(lo,hi) in cell.items():
            i+=offset; j+=offset
            d[i][j]=min(d[i][j],hi); d[j][i]=min(d[j][i],-lo)
    for i in range(8):
        d[i+1][i]=min(d[i+1][i],-4*SC) # theta=4/5 in 5*SC units
    for k in range(9):
        for i in range(9):
            if d[i][k]==infinity: continue
            for j in range(9):
                if d[k][j]!=infinity:
                    d[i][j]=min(d[i][j],d[i][k]+d[k][j])
        if any(d[i][i]<0 for i in range(9)): return None
    # Row 0 gives an exact feasible prefix potential, not just absence of a witness.
    assert all(d[0][j]-d[0][i]<=d[i][j] for i in range(9) for j in range(9))
    return d


def analyze(cells):
    originals=[constraints(cell) for cell in cells]
    assert len(cells)==70
    assert len({tuple(c['gap_bounds']+c['span_bounds']) for c in cells})==70
    labelled=originals+[{(7-j,7-i):v for (i,j),v in c.items()} for c in originals]
    paid=[c['paid_reward_numerator'] for c in cells]*2
    coordinate_count=span_count=0; pairs=[]
    for a,left in enumerate(labelled):
        for b,right in enumerate(labelled):
            if any(max(left[i+1,i+2][0],right[i,i+1][0])>
                   min(left[i+1,i+2][1],right[i,i+1][1]) for i in range(6)): continue
            coordinate_count+=1
            if any(max(left[i+1,j+1][0],right[i,j][0])>
                   min(left[i+1,j+1][1],right[i,j][1]) for i,j in SPANS if j<=6): continue
            span_count+=1
            d=closure(left,right)
            if d is None: continue
            lo,hi=Q(-d[8][0],5*SC),Q(d[0][8],5*SC)
            assert Q(32,5)<=lo<=hi<=Q(2870483,72245)
            total=paid[a]+paid[b]
            pairs.append({'left':a,'right':b,'span_lower':str(lo),'span_upper':str(hi),
                          'reward_sum_numerator':total,'average_pays_target':total>=2*TARGET})
    paid_count=sum(pair['average_pays_target'] for pair in pairs)
    assert (coordinate_count,span_count,len(pairs),paid_count)==(422,289,289,78)
    return {'labelled_cells':140,'distinct_geometric_cells':len({tuple(sorted(c.items())) for c in labelled}),
            'ordered_pairs_examined':19600,'coordinate_candidates':coordinate_count,
            'shared_span_candidates':span_count,'feasible_pairs':len(pairs),
            'average_paid_pairs':paid_count,'unpaid_pairs':len(pairs)-paid_count,'pairs':pairs}


def report(cells):
    return {'schema':'rh-weil-am-nine-point-low-slack-cover-v1',
            'scope':'captured admitted-core runtime leaves plus exact closed difference constraints',
            'uniform_nine_point_gain_proved':False,'new_actual_zero_proportion':False,
            'lean_runtime_trust_required':True,'old_reward_numerator':REWARD,
            'strong_target_numerator':STRONG,'nine_point_target_numerator':TARGET,
            'reward_denominator':10**8,'coordinate_denominator':SC,
            'old_checks_true':41,'original_low_cells':70,
            'script_canonical_lf_sha256':sha(Path(__file__).read_bytes()),
            'admitted_core_raw_sha256':json.loads((ROOT/'output/am-pc8-finite-replay.json').read_text(encoding='utf-8'))['numeric_core_sha256'],
            'cells':cells,'analysis':analyze(cells)}


def main():
    if not __debug__: raise SystemExit('Run without -O: all assertions are required')
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check',action='store_true')
    mode.add_argument('--from-log',type=Path)
    mode.add_argument('--replay',action='store_true')
    parser.add_argument('--lean',default=r'C:\Users\A\.elan\bin\lean.exe')
    args=parser.parse_args()
    if args.from_log:
        result=report(parse_log(decode_log(args.from_log.read_bytes())))
        OUTPUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print('PASS captured-log import and exact geometry; uniform gain unproved')
        return
    frozen=json.loads(OUTPUT.read_text(encoding='utf-8'))
    cells=frozen['cells']
    if args.replay:
        WORK.mkdir(parents=True,exist_ok=True)
        path=WORK/'Low805203.lean'; path.write_text(build_instrumented(),encoding='utf-8')
        run=subprocess.run([args.lean,'+leanprover/lean4:v4.34.1','--tstack=32768','-j1',str(path)],
                           cwd=ROOT,capture_output=True,timeout=1800)
        log=(run.stdout+run.stderr).decode('utf-8')
        (WORK/'replay-log.txt').write_text(log,encoding='utf-8')
        assert run.returncode==0,'Lean runtime failed; see isolated replay log'
        cells=parse_log(log)
    assert report(cells)==frozen
    print('PASS '+('actual isolated Lean replay; ' if args.replay else 'captured data only; ')+
          '289 compatible pairs, 78 average-paid, 211 unpaid; no uniform gain')


if __name__=='__main__': main()

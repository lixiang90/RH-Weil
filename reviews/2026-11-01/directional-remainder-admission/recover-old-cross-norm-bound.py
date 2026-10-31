"""One bounded OLD-ASSET scalar recovery, not a new source/probe run.

Standalone; never imports a scientific driver or changes old evidence. Reads
only existing A/B and the605 point. Requires a new explicit root freeze.
"""
import time
START=time.monotonic()
import argparse,hashlib,json,math,os,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
SELF=Path(__file__).resolve()
OUT=ROOT/'literature/local/2026-11-01-directional-remainder-old-norm/run-01'
U=1<<1024
Q=1<<257

def need(ok,msg):
    if not ok:raise ValueError(msg)
def clock():need(time.monotonic()-START<50,'OLD_RECOVERY_DEADLINE')
def sha(b):return hashlib.sha256(b).hexdigest()
def packed(v):return (json.dumps(v,sort_keys=True,separators=(',',':'))+'\n').encode()
def fraction(v):return F(*map(int,v))
def pair(x):return [str(x.numerator),str(x.denominator)]
def sqrt_grid(x):
    need(x>=0,'SQRT_DOMAIN')
    a=math.isqrt((x.numerator<<2048)//x.denominator)
    lo=F(a,U)
    return lo,lo if lo*lo==x else F(a+1,U)
def load_pin(record):
    p=(ROOT/record['path']).resolve();need(p.is_relative_to(ROOT) and p.is_file(),'PIN_PATH')
    b=p.read_bytes();need(sha(b)==record['sha256'],'PIN_HASH:'+record['path']);clock()
    return b

def run(path):
    raw=path.read_bytes();g=json.loads(raw)
    need(g['schema']=='RH_WEIL_OLD605_NORM_BOUND_RECOVERY_V1'
         and g['authorization']=='ROOT_EXPLICIT_OLD_ASSET_SCALAR_RECOVERY_ONLY'
         and g['numericalExecutionAuthorized'] is True and g['newC069'] is False
         and g['runtimeGoalCreatedAt']==1793085111 and g['capSeconds']==60
         and g['capBytes']==1048576 and g['oneAttemptOnly'] is True,'ROOT_RECOVERY_SCOPE')
    need(g['codeSHA256']==sha(SELF.read_bytes()),'SELF_PIN')
    need(not OUT.exists(),'OLD_RECOVERY_ALREADY_ATTEMPTED')
    review=load_pin(g['reviewPin']);need(g['codeSHA256'].encode() in review,'EXACT_CODE_REVIEW')
    inputs={k:load_pin(v) for k,v in g['inputPins'].items()}
    OUT.mkdir(parents=True,exist_ok=False)
    with (OUT/'attempt.json').open('xb') as f:f.write(packed(dict(freezeSHA256=sha(raw),pid=os.getpid())))
    try:
        point=json.loads(inputs['point']);root_scalar=json.loads(inputs['headUpper'])
        replay=json.loads(inputs['pointReplay'])
        need(point['status']=='FIXED_WHOLE_RECIPE_REJECTED'
             and replay['status']=='NEGATIVE_FIXED_WHOLE_RECIPE_CERTIFICATE_VERIFIED','ACCEPTED605_POINT')
        w=point['witness'];need(w['sector']=='even' and w['originalDegrees']==list(range(0,448,2)),'FIXED605_SOURCE')
        an=list(map(int,w['rawSourceNumerators']));aden=int(w['rawSourceDenominator'])
        zz=list(map(int,w['Z']));need(len(an)==len(zz)==224,'POINT_DIMENSION')
        aa=[F(x,aden) for x in an];z=[F(x,U) for x in zz]
        d=[F(9,4*(2*j+1)) for j in range(0,448,2)]
        n=sum((dd*x*x for dd,x in zip(d,aa)),F(0));need(n==fraction(w['exactPhysicalNorm']) and n>0,'EXACT_OLD_NORM')
        upper=fraction(root_scalar['actualCretRayleighStrictUpper']);need(upper>0,'HEAD_UPPER')
        packet=json.loads(inputs['matrices'])['packet'];p=packet['parameters']
        need(p['N']==448 and p['L']=='9/8' and p['omega']==256 and p['outputBits']==256,'OLD_SOURCE_PARAMETERS')
        matrices={}
        for name in ('A','B'):
            data=packet['matrices'][name];need(len(data)==50400,'OLD_MATRIX_ROWS')
            m=[[0]*224 for _ in range(224)];pos=0
            for i in range(448):
                for j in range(i,448,2):
                    row=data[pos];need(len(row)==4 and row[:2]==[i,j],'OLD_MATRIX_ORDER')
                    lo,hi=map(int,row[2:]);need(lo<=hi,'OLD_MATRIX_ENDPOINT_ORDER')
                    if i%2==0:m[i//2][j//2]=m[j//2][i//2]=lo+hi
                    pos+=1
                clock()
            matrices[name]=m
        # Raw A/B centers are midpoint sums /2^257. No inverse or new matrix.
        avec=[sum(x*y for x,y in zip(row,an)) for row in matrices['A']]
        bnum=sum(an[i]*sum(x*y for x,y in zip(row,an)) for i,row in enumerate(matrices['B']))
        aq=sum((F(x*x,dd) for x,dd in zip(avec,d)),F(0))
        dh=F(bnum,Q*aden*aden)-aq/(Q*Q*aden*aden)
        bnorm=sum((dd*(x-y)**2 for dd,x,y in zip(d,aa,z)),F(0))
        f_lower,_=sqrt_grid(max(F(0),dh/n-F(1,1<<233)))
        _,b_upper=sqrt_grid(bnorm/n)
        e=F(1389,1<<85)+F(1,1<<440)
        lower=max(F(0),f_lower-F(9,5)*(b_upper+F(1,1<<225))-e)
        decision=lower*lower>11*upper
        clock()
        result=dict(schema='RH_WEIL_OLD605_NORM_BOUND_RESULT_V1',
            status=('OLD_ASSETS_CERTIFY_BOUNDED_LRET_INDEFINITE' if decision else 'OLD_NORM_BOUND_INCONCLUSIVE'),
            runtimeGoalCreatedAt=1793085111,sourceIteration=605,newMathematicalIterations=0,
            exactPhysicalNorm=pair(n),centerCovarianceQuadraticOverN=pair(dh/n),
            modelBNormSquaredOverN=pair(bnorm/n),trueFNormLowerOverSqrtN=pair(f_lower),
            modelBNormUpperOverSqrtN=pair(b_upper),trueNNormLowerOverSqrtN=pair(lower),
            actualHeadUpper=pair(upper),thresholdSquared=pair(11*upper),
            actualBoundedLretIndefinite=decision,negativeFullQClaim=False,positivityClaim=False,
            newRowsComputed=False,newSourceOrGramProduced=False,oldMatricesParsed=True,
            inputPins=g['inputPins'],selfSHA256=g['codeSHA256'],freezeSHA256=sha(raw),
            internalElapsedSeconds=time.monotonic()-START,externalFullLifetimeRequired=True,
            interpretation='Old Dh233, B transport225, Xnorm9/5 and Ynorme only. Inconclusive lower is no sign or norm upper; never a new candidate/source attempt.')
        need(path.read_bytes()==raw and sha(SELF.read_bytes())==g['codeSHA256'],'FINAL_SELF_FREEZE')
        for record in g['inputPins'].values():load_pin(record)
        output=packed(result);need(len(output)<262144,'RESULT_SIZE')
        with (OUT/'result.json').open('xb') as f:f.write(output);f.flush();os.fsync(f.fileno())
        return result
    except BaseException as error:
        fail=packed(dict(status='OLD_SCALAR_RECOVERY_TECHNICAL_STOP',errorType=type(error).__name__,
            reason=str(error)[:1500],newMathematicalIterations=0,mathematicalSignConclusion=False))
        with (OUT/'failure.json').open('xb') as f:f.write(fail)
        raise

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root-freeze-file',type=Path,required=True)
    if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
    result=run(parser.parse_args().root_freeze_file)
    print(json.dumps(dict(status=result['status'],internalElapsedSeconds=result['internalElapsedSeconds'],
        newMathematicalIterations=0,negativeFullQClaim=False)))

"""AST-isolated 3D synthetic controls; never import/run the scientific checker."""
import argparse,ast,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
H=Path(__file__).resolve().parent
CODE=H/'verify-prefix-terminal.py'
raw=CODE.read_bytes()
parser=argparse.ArgumentParser()
parser.add_argument('--code-sha',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
EXPECTED=args.code_sha
assert hashlib.sha256(raw).hexdigest()==EXPECTED
names={'need','IntegerWidthError','checked','width_diagnostic','integer','fraction','frac','direct_replay'}
nodes=[x for x in ast.parse(raw).body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names]
assert {x.name for x in nodes}==names
U=1<<1024;Q=1<<257;B=9*(1<<255)
lam=F(1,1<<122)+F(1,1<<224)+F(1,1<<216)
ns=dict(F=F,P=1024,N=6,NSECTOR=3,UNIT=U,Q=Q,B=B,MAX_BITS=16384,DIAGNOSTIC_BITS=65536,LAMBDA=lam)
exec(compile(ast.Module(body=nodes,type_ignores=[]),'PURE_SYNTHETIC_REPLAY_ONLY','exec'),ns)

def inverse3(a):
    m=[[F(x) for x in row]+[F(i==j) for j in range(3)] for i,row in enumerate(a)]
    for i in range(3):
        assert m[i][i]!=0
        d=m[i][i];m[i]=[x/d for x in m[i]]
        for j in range(3):
            if i!=j:
                c=m[j][i];m[j]=[x-c*y for x,y in zip(m[j],m[i])]
    return [row[3:] for row in m]

def mv(a,x):return [sum((v*y for v,y in zip(row,x)),F(0)) for row in a]
def quad(a,x):return sum((v*y for v,y in zip(x,mv(a,x))),F(0))
class Dummy:
    context={}
    def check(self):pass
checks=0
for parity in (0,1):
    idx=list(range(parity,6,2));w=[2*j+1 for j in idx];d=[F(9,4*j) for j in w]
    aa=[[0]*6 for _ in range(6)];jj=[[0]*6 for _ in range(6)];gg=[[0]*6 for _ in range(6)]
    hh=[[0]*6 for _ in range(2)]
    small=[[Q//3,5,-7],[5,Q//4,9],[-7,9,Q//5]]
    for i,di in enumerate(idx):
        hh[parity][di]=i-2
        for j,dj in enumerate(idx):
            gg[di][dj]=small[i][j]
            aa[di][dj]=-10*Q if i==j else 3*(i+j+1)
            jj[di][dj]=Q if i==j else -(i+j+1)
    g=[[F(gg[i][j],Q) for j in idx] for i in idx]
    s=[[g[i][j]+(d[i] if i==j else 0) for j in range(3)] for i in range(3)]
    sinv=inverse3(s)
    c=[[F(aa[i][j]+jj[i][j],Q)+F(36*sum(hh[t][i]*hh[t][j] for t in (0,1)),1<<1282)
        for j in idx] for i in idx]
    # Independent original Chat=C+Graw*(Graw+D)^-1*Graw, not expanded K.
    chat=[[c[i][j]+sum((g[i][k]*sinv[k][l]*g[l][j] for k in range(3) for l in range(3)),F(0))
           for j in range(3)] for i in range(3)]
    zint=[U//3,-U//4,U];z=[F(x,U) for x in zint]
    a=[x/d[i] for i,x in enumerate(mv(s,z))]
    anum=[int(x*(B*U)) for x in a]
    assert all(F(v,B*U)==x for v,x in zip(anum,a))
    norm=sum((d[i]*a[i]*a[i] for i in range(3)),F(0));qk=quad(chat,a);qpre=qk-lam*norm
    assert norm>0 and qpre<0
    pair=lambda q:[str(q.numerator),str(q.denominator)]
    witness=dict(sector=('even' if parity==0 else 'odd'),originalDegrees=idx,zDenominatorPower=1024,
        proposalCount=1,prefixNegativeCertified=True,negativeCretClaim=False,negativeLretClaim=False,
        negativeQClaim=False,Z=list(map(str,zint)),pivot=2,rawSourceDenominator=str(B*U),
        rawSourceNumerators=list(map(str,anum)),exactChatQuadratic=pair(qk),exactPhysicalNorm=pair(norm),
        lambdaExact=pair(lam),exactPrerequisiteQuadratic=pair(qpre),exactPrerequisiteRayleigh=pair(qpre/norm))
    result=ns['direct_replay'](Dummy(),witness,aa,jj,hh,gg)
    assert ns['fraction'](result['exactChatQuadratic'])==qk
    assert ns['fraction'](result['exactPhysicalNorm'])==norm
    assert ns['fraction'](result['exactPrerequisiteQuadratic'])==qpre
    checks+=3
    wrong=dict(witness,exactChatQuadratic=pair(qk+1))
    try:ns['direct_replay'](Dummy(),wrong,aa,jj,hh,gg);raise AssertionError('bad q accepted')
    except ValueError as e:assert 'EXACT_STORED_WITNESS_MATCH' in str(e)
    checks+=1
for value in (F(1<<16384),F(1,1<<16384),F(-(1<<65535)),F(1<<65536)):
    try:ns['frac'](value);raise AssertionError('width accepted')
    except ns['IntegerWidthError'] as e:
        d=ns['width_diagnostic'](e);assert not d['mathematicalSignConclusion']
        if e.actualBitLength<=65536:assert int(d['signedHexValue'],16)==e.value
        else:assert d['valueOmitted'] and d['unconsumable']
    checks+=1
receipt=dict(status='PASS',checks=checks,codeSHA256=EXPECTED,ASTSelectedNames=sorted(names),
    checkerImported=False,authorizeOrMainCalled=False,actualResearchSourcesRead=False,
    syntheticDimension=3,independentTruth='original Chat with exact3x3 inverse on synthetic inputs ONLY',
    bothOriginalParityMetrics=True,noncommutingGrawAndD=True,wrongSavedScalarRejected=True,
    normalWidthAndBoundedFailureDiagnostics=True,newMathematicalIterations=0)
assert Path(args.output).name==args.output and args.output.endswith('.json')
with (H/args.output).open('x',encoding='utf-8') as f:
    json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt))

"""Root-only isolated checks: pure AST functions, Fraction truth, SYNTHETIC data.

Never imports the driver, validates a live freeze, claims OUTER, or reads actual
research sources. --code-sha binds the exact future reviewed code version.
"""
import argparse
import ast
from fractions import Fraction as F
import hashlib
import json
from math import lcm
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)
parser=argparse.ArgumentParser()
parser.add_argument('--code-sha',required=True)
parser.add_argument('--output',required=True,help='Unique receipt basename; never overwrite a prior check')
args=parser.parse_args()
HERE=Path(__file__).resolve().parent
CODE=HERE/'whole-prerequisite.py'
raw=CODE.read_bytes()
assert hashlib.sha256(raw).hexdigest()==args.code_sha
tree=ast.parse(raw)
names={'need','up','checked','frac','IntegerWidthError','integer_width_diagnostic','nearest','IV','prerequisite_ldl',
       'sole_prefix_witness','evaluate_prefix'}
nodes=[x for x in tree.body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names]
assert {x.name for x in nodes}==names
lam_node=next(x.value for x in tree.body if isinstance(x,ast.Assign)
              and any(isinstance(y,ast.Name) and y.id=='LAMBDA' for y in x.targets))
# This particular scalar expression may call Fraction only, never a file/tool.
assert all(isinstance(x,(ast.Expression,ast.BinOp,ast.Add,ast.LShift,ast.Call,
                        ast.Name,ast.Load,ast.Constant)) for x in ast.walk(lam_node))
assert all(isinstance(x.func,ast.Name) and x.func.id=='F' for x in ast.walk(lam_node)
           if isinstance(x,ast.Call))
lam=eval(compile(ast.Expression(lam_node),'SCALAR_LAMBDA_ONLY','eval'),{'F':F})
assert lam==F(1,1<<122)+F(1,1<<224)+F(1,1<<216)
P=1024
U=1<<P
ns=dict(F=F,P=P,UNIT=U,LAMBDA=lam,MAX_BITS=16384,DIAGNOSTIC_BITS=65536,n=3)
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(CODE)+'::isolated-review','exec'),ns)
iv=ns['IV']()
checks=0

# Width limits apply to normal persisted Fractions, including denominators.
# Overflow evidence is separate and cannot certify any mathematical sign.
assert ns['frac'](F((1<<16384)-1,1))==[str((1<<16384)-1),'1']
checks+=1
for value,part in ((F(1<<16384,1),'fraction-numerator'),
                   (F(1,1<<16384),'fraction-denominator'),
                   (F(-(1<<65535),1),'fraction-numerator'),
                   (F(1<<65536,1),'fraction-numerator')):
    try:
        ns['frac'](value)
        raise AssertionError('Fraction width overflow was not stopped')
    except ns['IntegerWidthError'] as error:
        offending=value.numerator if part=='fraction-numerator' else value.denominator
        assert error.value==offending and error.serializedPart==part
        assert error.actualBitLength==abs(offending).bit_length() and error.normalLimit==16384
        diagnostic=ns['integer_width_diagnostic'](error)
        assert diagnostic['technicalStopOnly'] and not diagnostic['mathematicalSignConclusion']
        assert not diagnostic['normalArithmeticDataUsable']
        if error.actualBitLength<=65536:
            assert diagnostic['fullDiagnosticValuePresent'] and not diagnostic['valueOmitted']
            assert int(diagnostic['signedHexValue'],16)==offending
        else:
            assert diagnostic['valueOmitted'] and diagnostic['unconsumable']
            assert diagnostic['signedHexValue'] is None
        assert len(json.dumps(diagnostic).encode())<131072
        checks+=6
def enclosure(a,q):
    global checks
    assert F(a[0],U)<=q<=F(a[1],U),(a,q)
    checks+=1

points=sorted({-2*U,-U,-U//3,-1,0,1,U//3,U,2*U})
intervals=[(a,b) for a in points for b in points if a<=b]
for a in intervals:
    for x in a:enclosure(iv.square(a),F(x*x,U*U))
    if a[0]<=0<=a[1]:enclosure(iv.square(a),F(0))
    for b in intervals:
        for x in a:
            for y in b:
                enclosure(iv.mul(a,b),F(x*y,U*U))
                enclosure(iv.sub(a,b),F(x-y,U))
                if b[0]>0:enclosure(iv.div_positive(a,b),F(x,y))
for a in (-17,-1,0,1,17):
    for b in (3,7,19,1<<1100):enclosure(iv.rat(F(a,b)),F(a,b))
for a,b,c in ((1,2,1),(-1,2,0),(3,2,2),(-3,2,-1),(2,3,1),(-2,3,-1)):
    assert ns['nearest'](a,b)==c
    checks+=1

class Budget:
    def __init__(self):self.context={}
    def progress(self,*args,**kwargs):pass
    def check(self):pass
class Log:
    def __init__(self):self.rows=[]
    def write(self,x):self.rows.append(x)

def datum(parity=0,kind='positive'):
    indices=[2*i+parity for i in range(3)]
    w=[2*j+1 for j in indices]
    common=lcm(*w)
    if kind=='positive':k=[[4,1,0],[1,3,1],[0,1,2]];den=1
    elif kind=='negative':k=[[4,1,0],[1,-1,0],[0,0,2]];den=1
    elif kind in ('positive_chat_negative_prefix','exact_zero_prefix'):
        factor=2 if kind=='positive_chat_negative_prefix' else 1
        den=4*common*lam.denominator*factor
        k=[[9*(common//w[i])*lam.numerator if i==j else 0 for j in range(3)] for i in range(3)]
    else:raise AssertionError(kind)
    return dict(sector=('even' if parity==0 else 'odd'),indices=indices,w=w,
                Kint=k,dK=den,g=[[0]*3 for _ in range(3)],Jint=[[0]*3 for _ in range(3)],
                Bint=[[int(i==j) for j in range(3)] for i in range(3)],b=1)

for parity in (0,1):
    status,k,_,_=ns['prerequisite_ldl'](datum(parity),Budget(),Log())
    assert status=='ALL_POSITIVE' and k==3
    checks+=1
    d=datum(parity,'negative')
    status,k,ell,_=ns['prerequisite_ldl'](d,Budget(),Log())
    assert status=='NEGATIVE_PIVOT' and k==1
    witness=ns['sole_prefix_witness'](d,k,ell,Budget())
    Z=list(map(int,witness['Z']))
    anum=[sum(d['Bint'][i][j]*Z[j] for j in range(3)) for i in range(3)]
    den=d['b']*U
    norm=sum((F(9*anum[i]*anum[i],4*d['w'][i]*den*den) for i in range(3)),F(0))
    q=F(sum(Z[i]*d['Kint'][i][j]*Z[j] for i in range(3) for j in range(3)),d['dK']*U*U)
    assert norm==F(*map(int,witness['exactPhysicalNorm']))>0
    assert q==F(*map(int,witness['exactChatQuadratic']))
    assert q-lam*norm==F(*map(int,witness['exactPrerequisiteQuadratic']))<0
    assert witness['prefixNegativeCertified'] and not witness['negativeCretClaim']
    assert not witness['negativeLretClaim'] and not witness['negativeQClaim']
    checks+=5
    # Crucial scope control: Chat can be strictly positive while Hpre is negative.
    d=datum(parity,'positive_chat_negative_prefix')
    status,k,ell,_=ns['prerequisite_ldl'](d,Budget(),Log())
    assert status=='NEGATIVE_PIVOT' and k==0
    witness=ns['sole_prefix_witness'](d,k,ell,Budget())
    norm=F(*map(int,witness['exactPhysicalNorm']))
    q=F(*map(int,witness['exactChatQuadratic']))
    assert q>0 and q/norm==lam/2
    assert F(*map(int,witness['exactPrerequisiteQuadratic']))==-q<0
    assert witness['prefixNegativeCertified'] and not witness['negativeCretClaim']
    checks+=4
    status,k,_,pivot=ns['prerequisite_ldl'](datum(parity,'exact_zero_prefix'),Budget(),Log())
    assert status=='INTERVAL_UNRESOLVED' and k==0 and pivot==(0,0)
    checks+=1

original_witness=ns['sole_prefix_witness']
def evaluate(kinds,fail_proposal=False):
    calls=[]
    proposals=[]
    def assemble(parity,*args):
        calls.append(parity)
        return datum(parity,kinds[parity])
    def proposal(d,k,ell,budget):
        proposals.append(d['sector'])
        if fail_proposal:return {'prefixNegativeCertified':False}
        return original_witness(d,k,ell,budget)
    ns['assemble']=assemble
    ns['sole_prefix_witness']=proposal
    result=ns['evaluate_prefix'](None,None,None,None,Budget(),Log())
    return result,calls,proposals

r,c,p=evaluate(['positive','positive'])
assert r[0]=='PREFIX_NECESSARY_PASS' and c==[0,1] and p==[]
checks+=1
r,c,p=evaluate(['exact_zero_prefix','exact_zero_prefix'])
assert r[0]=='PREFIX_UNRESOLVED' and c==[0,1] and p==[]
checks+=1
r,c,p=evaluate(['exact_zero_prefix','positive_chat_negative_prefix'])
assert r[0]=='FIXED_WHOLE_RECIPE_REJECTED' and c==[0,1] and p==['odd']
checks+=1
r,c,p=evaluate(['positive_chat_negative_prefix','positive_chat_negative_prefix'])
assert r[0]=='FIXED_WHOLE_RECIPE_REJECTED' and c==[0] and p==['even']
checks+=1
r,c,p=evaluate(['positive_chat_negative_prefix','positive_chat_negative_prefix'],True)
assert r[0]=='PREFIX_UNRESOLVED' and c==[0] and p==['even']
checks+=1

result=dict(status='PASS',codeSHA256=args.code_sha,checks=checks,
    pureASTSelectedNames=sorted(names),driverImported=False,freezeOrMainCalled=False,
    actualResearchSourcesRead=False,actualResearchMatrixComputed=False,
    syntheticDimension=3,lambdaExact=[str(lam.numerator),str(lam.denominator)],
    scopeControls=['Chat positive with Hpre negative','minus lambda without extra source EPS',
                   'both original parity metrics','zero pivot unresolved',
                   'Fraction numerator and denominator width limits; bounded signed overflow evidence',
                   'ordinary unresolved continues only other prescheduled sector',
                   'global one proposal and failed proposal immediate terminal'],
    wholeQCertified=False,formalC068Admitted=False,newMathematicalIterations=0)
assert Path(args.output).name==args.output and args.output.endswith('.json')
out=HERE/args.output
with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result))

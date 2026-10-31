"""Root review only: AST-selected pure arithmetic and SYNTHETIC matrices.

Never import the research driver, read actual sources, or run its gate/main.
Independent Fraction corner values test outward inclusion; tiny known quadratic
forms test positive, negative and source-band logic, not actual Cret sign.
"""
import ast
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
CODE=HERE/'signed-head-gate.py'
EXPECTED='ed32fa2749c11c1dd1adae3bb078a331c5206a9d79f975a23c45e7df5f2fb7c3'
raw=CODE.read_bytes()
assert hashlib.sha256(raw).hexdigest()==EXPECTED
names={'need','up','checked','frac','nearest','IV','interval_ldl','negative_proposal'}
tree=ast.parse(raw)
nodes=[x for x in tree.body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names]
assert {x.name for x in nodes}==names
P=1024
U=1<<P
ns=dict(F=F,P=P,UNIT=U,EPS=F(1,1<<201),MAX_BITS=16384,n=3)
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(CODE)+'::review-selected','exec'),ns)
iv=ns['IV']()
checks=0
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
for num in (-17,-1,0,1,17):
    for den in (3,7,19,1<<1100):enclosure(iv.rat(F(num,den)),F(num,den))
for numerator,denominator,expected in ((1,2,1),(-1,2,0),(3,2,2),(-3,2,-1),(2,3,1),(-2,3,-1)):
    assert ns['nearest'](numerator,denominator)==expected
    checks+=1

class Budget:
    context={}
    def progress(self,*args,**kwargs):pass
    def check(self):pass
class Log:
    def __init__(self):self.rows=[]
    def write(self,x):self.rows.append(x)

def data(k,scale=1):
    return dict(sector='synthetic',indices=[0,2,4],w=[1,5,9],
                Kint=k,dK=scale,g=[[0]*3 for _ in range(3)],
                Jint=[[0]*3 for _ in range(3)],Bint=[[int(i==j) for j in range(3)] for i in range(3)],b=1)
pd=data([[4,1,0],[1,3,1],[0,1,2]])
for sign in (1,-1):
    status,k,_,_=ns['interval_ldl'](pd,sign,Budget(),Log())
    assert status=='ALL_POSITIVE' and k==3
    checks+=1
nd=data([[4,1,0],[1,-1,0],[0,0,2]])
status,k,ell,_=ns['interval_ldl'](nd,1,Budget(),Log())
assert status=='NEGATIVE_PIVOT' and k==1
w=ns['negative_proposal'](nd,k,ell,Budget())
assert w['negativeCertified']
Z=list(map(int,w['Z']))
q=F(sum(Z[i]*nd['Kint'][i][j]*Z[j] for i in range(3) for j in range(3)),U*U)
nrm=sum((F(9*Z[i]*Z[i],4*nd['w'][i]*U*U) for i in range(3)),F(0))
assert q==F(*map(int,w['exactModelQuadratic']))
assert nrm==F(*map(int,w['exactPhysicalNorm']))
assert q+ns['EPS']*nrm==F(*map(int,w['exactUpperQuadratic']))<0
checks+=4
zero=data([[0]*3 for _ in range(3)])
assert ns['interval_ldl'](zero,1,Budget(),Log())[0]=='ALL_POSITIVE'
assert ns['interval_ldl'](zero,-1,Budget(),Log())[0]=='NEGATIVE_PIVOT'
checks+=2
# Exact cancellation in the first upper pivot must never be divided through.
cancel=data([[-9,0,0],[0,0,0],[0,0,0]],4*(1<<201))
status,k,_,pivot=ns['interval_ldl'](cancel,1,Budget(),Log())
assert status=='INTERVAL_UNRESOLVED' and k==0 and pivot==(0,0)
checks+=1
result=dict(status='PASS',codeSHA256=EXPECTED,checks=checks,
            method='AST-selected pure scalar functions and three-dimensional synthetic matrices only',
            actualResearchSourcesRead=False,actualCretComputed=False,driverImported=False,
            arithmeticFamilies=['rational conversion','signed subtraction','four product corners',
                                'square crossing zero','positive-denominator signed division',
                                'point midpoint ties','positive LDL','negative exact witness',
                                'source-band ambiguity','zero pivot refusal'])
out=HERE/'arithmetic-leaves-result.json'
with out.open('xb') as f:f.write((json.dumps(result,indent=2)+'\n').encode())
print(json.dumps(result))

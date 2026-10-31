"""AST-isolated controls on small synthetic sources; never import producer.

No actual moment/prime/V/h file is opened. N=4, degree=6, work192/downscale128.
Independent Fraction polynomial integration and symbolic log2 coefficients are
the oracles. These are mechanism checks, not the actual native230 predicate.
"""
import ast
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
source = (HERE/"source-model.py").read_bytes()
tree = ast.parse(source)
allowed = {"need", "ceil_div", "integer", "product_bounds", "Mesh", "dot", "rational_polynomials",
           "legendre_at", "ell_monomials", "shift_rows", "kernel_seeds", "polynomial_y",
           "true_pi", "Tail", "weighted_gram", "log_raw"}
selected = [node for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in allowed]
assert len(selected) == len(allowed)
scope = {"Fraction":F, "math":math, "re":re, "N":4, "DEGREE":6,
         "COEFFICIENT_BITS":8192, "CONTRACTION_BITS":128, "RAW_BITS":64}
exec(compile(ast.Module(body=selected, type_ignores=[]), "AST_SYNTHETIC_ONLY", "exec"), scope)
Mesh, need = scope["Mesh"], scope["need"]
mesh = Mesh(192)
tick = lambda: None
count = 0


def inside(iv, value, scale=192):
    global count
    assert F(iv[0],1 << scale) <= value <= F(iv[1],1 << scale)
    count += 1


def polynomials(n, shift=F(0)):
    yield [F(1)]
    if n == 1:
        return
    p0, p1 = [F(1)], [-shift,F(1)]
    yield p1
    for k in range(1,n-1):
        out = [F(0)]*(k+2)
        for j,v in enumerate(p1):
            out[j+1] += F(2*k+1,k+1)*v
            out[j] -= F(2*k+1,k+1)*shift*v
        for j,v in enumerate(p0):
            out[j] -= F(k,k+1)*v
        p0,p1 = p1,out
        yield out


def product(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def integral(poly,lo,hi):
    return sum((a*(hi**(k+1)-lo**(k+1))/(k+1) for k,a in enumerate(poly)),F(0))


def atan_interval(d,terms=256):
    mid=sum((F((-1)**k,(2*k+1)*d**(2*k+1)) for k in range(terms)),F(0))
    radius=F(1,(2*terms+1)*d**(2*terms+1))
    return mid-radius,mid+radius


def log2_interval():
    mid=2*sum((F(1,(2*k+1)*3**(2*k+1)) for k in range(256)),F(0))
    return mid,mid+F(1,3**512)


lnlo,lnhi=log2_interval()
lniv=mesh.log_series(1,3,tick)
assert F(lniv[0],mesh.unit) <= lnlo <= lnhi <= F(lniv[1],mesh.unit)
count += 1

for a in ((-5,-2),(-3,0),(-2,3),(0,4),(2,5),(0,0)):
    for b in ((-5,-2),(-3,0),(-2,3),(0,4),(2,5),(0,0)):
        products=[x*y for x in a for y in b]
        assert scope["product_bounds"](a,b)==(min(products),max(products))
        count += 1

# Directed arithmetic, signs and one-round dot must enclose exact rationals.
for a in (F(-7,3),F(0),F(5,7)):
    for b in (F(-4,5),F(0),F(8,9)):
        inside(mesh.mul(mesh.rat(a),mesh.rat(b)),a*b)
        inside(mesh.scale(mesh.rat(a),b.numerator,b.denominator),a*b)
inside(scope["dot"](mesh,[mesh.rat(F(2,3)),mesh.rat(F(-5,7))],
                    [mesh.rat(F(-3,5)),mesh.rat(F(9,11))],tick),F(-2,5)-F(45,77))

# J rectangle: independent monomial integration, all parities and j=0.
for t in (F(1,2),F(1),F(3,2)):
    plain=list(polynomials(7))
    shifted=list(polynomials(4,t))
    for r,jrow,brow in scope["shift_rows"](mesh,t,4,6,tick):
        for k in range(7):
            inside(jrow[k],integral(product(shifted[r],plain[k]),t-1,F(1)))

# B at t=1: exact symbolic A*log2+B integral of every monomial.
def ell_moment(k):
    rational=F(0)
    logcoef=F(1,k+1)
    minus=sum((F(math.comb(k,m)*(-1)**m,-(m+1)**2) for m in range(k+1)),F(0))
    plus_log=plus_rat=F(0)
    for m in range(k+1):
        coefficient=math.comb(k,m)*(-1)**(k-m)
        plus_log += coefficient*F(2**(m+1),m+1)
        plus_rat += coefficient*F(1-2**(m+1),(m+1)**2)
    return logcoef-plus_log/2, -(minus+plus_rat)/2

plain=list(polynomials(4)); shifted=list(polynomials(4,F(1)))
for r,jrow,brow in scope["shift_rows"](mesh,F(1),4,6,tick):
    for j in range(4):
        a=b=F(0)
        for k,v in enumerate(product(shifted[r],plain[j])):
            aa,bb=ell_moment(k);a+=v*aa;b+=v*bb
        lower,upper=sorted((a*lnlo+b,a*lnhi+b))
        assert F(brow[j][0],mesh.unit) <= lower <= upper <= F(brow[j][1],mesh.unit)
        count += 1

# Noncentral rational endpoints use a separately authored exact-rational
# 2atanh series; this checks the general log primitive, not only log2 cases.
def add_interval(a,b):
    return a[0]+b[0],a[1]+b[1]


def scaled_interval(a,q):
    return tuple(sorted((a[0]*q,a[1]*q)))


def log_interval(q):
    if q==1:
        return F(0),F(0)
    if q==2:
        return lnlo,lnhi
    if q==F(1,2):
        return -lnhi,-lnlo
    assert q==F(3,2)
    mid=2*sum((F(1,(2*k+1)*5**(2*k+1)) for k in range(256)),F(0))
    return mid,mid+F(1,5**512)


def primitive_interval(q,m):
    logarithm=scaled_interval(log_interval(q),F(1,m+1))
    inner=add_interval(logarithm,(-F(1,(m+1)**2),)*2)
    return scaled_interval(inner,q**(m+1))


def ell_integral_interval(poly,t):
    lo=hi=F(0)
    for k,coefficient in enumerate(poly):
        plain=F(1-(t-1)**(k+1),k+1)
        value=scaled_interval((lnlo,lnhi),plain)
        for m in range(k+1):
            minus=scaled_interval(primitive_interval(2-t,m),F(math.comb(k,m)*(-1)**m))
            plus=add_interval(primitive_interval(F(2),m),scaled_interval(primitive_interval(t,m),F(-1)))
            plus=scaled_interval(plus,F(math.comb(k,m)*(-1)**(k-m)))
            value=add_interval(value,scaled_interval(add_interval(minus,plus),F(-1,2)))
        term=scaled_interval(value,coefficient)
        lo+=term[0];hi+=term[1]
    return lo,hi


for t in (F(1,2),F(3,2)):
    plain=list(polynomials(4));shifted=list(polynomials(4,t))
    for r,jrow,brow in scope["shift_rows"](mesh,t,4,6,tick):
        for j in range(4):
            lower,upper=ell_integral_interval(product(shifted[r],plain[j]),t)
            assert F(brow[j][0],mesh.unit)<=lower<=upper<=F(brow[j][1],mesh.unit)
            count+=1

# Full Kstar model including signed pole Taylor and FULL h raw36 convention.
moments=[F(1,3),F(-1,7),F(2,11),F(0)]
h=[[0]*7 for _ in range(2)]
h[0][0]=h[0][4]=1 << 640
h[1][1]=h[1][5]=1 << 640
columns=scope["polynomial_y"](mesh,Mesh(128),moments,h,tick)
coefficients={2*q:(2*F(9,8)**(2*q)+(-1)**q*theta*576**(2*q))/math.factorial(2*q)
              for q,theta in enumerate(moments)}
plain=list(polynomials(7))
for j in range(4):
    for pos,i in enumerate(range(4+j%2,7,2)):
        raw=F(0)
        for m,cm in coefficients.items():
            for k in range(m+1):
                raw += F(81,64)*cm*F(math.comb(m,k)*(-1)**k,2**m)*\
                       integral([F(0)]*(m-k)+plain[i],F(-1),F(1))*\
                       integral([F(0)]*k+plain[j],F(-1),F(1))
        raw+=F(36*h[j%2][i]*h[j%2][j],1 << 1282)
        inside(columns[j][pos],raw,128)

# True pi enclosure by an independent exact alternating rational series.
p=scope["true_pi"](mesh,tick)
a0,a1=atan_interval(5);b0,b1=atan_interval(239)
assert F(p[0],mesh.unit)<=16*a0-4*b1<=16*a1-4*b0<=F(p[1],mesh.unit)
count += 1

# Infinite-tail sign/normalization: positive rational partial sums and explicit
# decreasing tail upper, not a numerical truncation asserted to be exact.
tail=scope["Tail"](mesh,6,tick)
for j in range(4):
    for k in range(j,4,2):
        i0=7 if 7%2==j%2 else 8
        partial=sum((F(9*(2*i+1),4*(i-j)*(i+j+1)*(i-k)*(i+k+1))
                     for i in range(i0,i0+200,2)),F(0))
        first=i0+200
        bound=108*(F(1,first**3)+F(1,4*first**2))
        lo,hi=tail.raw(j,k)
        assert partial <= F(lo,mesh.unit)<=F(hi,mesh.unit)<=partial+bound
        count += 1

out={"status":"AST_ISOLATED_SYNTHETIC_SOURCE_CONTROLS_PASS",
     "producerSHA256":hashlib.sha256(source).hexdigest(),"checkedContainments":count,
     "syntheticN":4,"syntheticDegree":6,"syntheticWorkBits":192,"syntheticContractionBits":128,
     "plainShiftArguments":["1/2","1","3/2"],"logShiftArguments":["1/2","1","3/2"],
     "fullSignedPoleAndFullH36Checked":True,"infiniteCXOffdiagonalChecked":True,
     "actualSourceFilesRead":False,"producerImported":False,"actual230Certificate":False,
     "actualRowsGramOrSolveComputed":False}
(HERE/"source-model-synthetic-result.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out))

"""Exact rational enclosure of one actual H quadratic form.

No mpmath input or zeta-zero data. Fixed dyadic outward bounds, elementary
Taylor remainders, and an analytic positive Gram tail are the certificate.
This checks only v=(1,-1), L=log(13), not the full Weil form.
"""
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path

BITS=256
GRID=1<<BITS

def down(x): return F((x.numerator*GRID)//x.denominator,GRID)
def up(x): return -down(-x)

class I:
    def __init__(self,a,b=None):
        self.lo=down(F(a)); self.hi=up(F(a if b is None else b))
        assert self.lo<=self.hi
    def __add__(self,y):
        y=as_i(y); return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,y): return self+-as_i(y)
    def __rsub__(self,y): return as_i(y)+-self
    def __mul__(self,y):
        y=as_i(y); z=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=as_i(y); assert y.lo*y.hi>0
        z=[a/b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(z),max(z))
    def __rtruediv__(self,y): return as_i(y)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0: return I(1)
        if n%2==0 and self.lo<=0<=self.hi:
            return I(0,max(abs(self.lo),abs(self.hi))**n)
        vals=[self.lo**n,self.hi**n]; return I(min(vals),max(vals))

def as_i(x): return x if isinstance(x,I) else I(x)

def log_int(k):
    z=F(k-1,k+1); M=1800
    # log(k)=2 sum z^(2j+1)/(2j+1); positive remainder bound.
    total=F(0); power=z
    for j in range(M): total+=power/(2*j+1); power*=z*z
    error=2*power/((2*M+1)*(1-z*z))
    return I(2*total,2*total+error)

def atan_inv(k):
    z=F(1,k); M=180
    total=sum(((-1)**j*z**(2*j+1)/F(2*j+1) for j in range(M)),F(0))
    error=z**(2*M+1)/F(2*M+1)
    return I(total-error,total+error)

def sqrt_int(k):
    q=isqrt(k*GRID*GRID); return I(F(q,GRID),F(q+1,GRID))

def sin(x):
    M=100; x=as_i(x)
    result=I(0)
    for j in range(M): result+=((-1)**j)*x**(2*j+1)/factorial(2*j+1)
    # Taylor's theorem with bounded derivatives on the entire real axis.
    error=max(abs(x.lo),abs(x.hi))**(2*M+1)/factorial(2*M+1)
    return result+I(-error,error)

def exp(x):
    x=as_i(x); assert x.lo>=0
    reductions=0
    while x.hi>F(1,2): x=x/2; reductions+=1
    M=100; result=sum((x**j/factorial(j) for j in range(M)),I(0))
    # Ratios of omitted positive terms are at most x.hi/(M+1).
    error=x.hi**M/F(factorial(M))/(1-x.hi/F(M+1))
    result+=I(0,error)
    for _ in range(reductions): result=result**2
    return result

def record(x):
    return {'lower_rational':str(x.lo),'upper_rational':str(x.hi),'lower_decimal_approx':float(x.lo),'upper_decimal_approx':float(x.hi)}

def main():
    L=log_int(13); pi=16*atan_inv(5)-4*atan_inv(239)
    xi1=2*pi/L; xi2=2*xi1
    e=exp(L/2); K=8/L*(e+1/e-2)
    f1=1/(1+4*xi1**2); f2=1/(1+4*xi2**2)
    pole=K*((f1-f2)**2+(2*xi1*f1-2*xi2*f2)**2)
    J=100; arch=I(0)
    for j in range(J):
        t=I(F(4*j+1,2))
        r1=t/(t**2+xi1**2); r2=t/(t**2+xi2**2)
        s1=xi1/(t**2+xi1**2); s2=xi2/(t**2+xi2**2)
        # Dropping the positive exponential correction for j>=10 is an upper bound.
        c=1-1/exp(t*L) if j<10 else I(1)
        arch+=2/L*c*((r1-r2)**2+(s1-s2)**2)
    tJ=F(4*J+1,2)
    def tail(p): return I(tJ**(-p)+tJ**(1-p)/F(2*(p-1)))
    remainder=2/L*((xi2**2-xi1**2)**2*tail(6)+(xi1+xi2)**2*tail(4))
    arch_upper=I(0,arch.hi+remainder.hi)
    primes={}; prime_total=I(0)
    for k,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13)):
        theta=xi1*log_int(k)
        contribution=log_int(p)/sqrt_int(k)/(6*pi)*(2*sin(theta)-sin(2*theta))
        primes[str(k)]=record(contribution); prime_total+=contribution
    witness=pole+arch_upper+prime_total
    assert witness.hi<0, 'No strict witness certified'
    report={'scope':'proved exact rational upper enclosure of H11+H22-2H12 only, L=log13, v=(1,-1); not QW positivity or RH','bits':BITS,'parameters':{'J':J,'exponential_terms_retained':10,'log_terms':1800,'atan_terms':180,'sin_terms':100,'exp_terms':100},'pole':record(pole),'arch_nonnegative_upper':record(arch_upper),'arch_series_tail_upper':record(remainder),'prime_terms':primes,'prime_total':record(prime_total),'witness':record(witness),'strict_negative':True,'script_byte_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    destination=Path(__file__).resolve().parents[1]/'reviews/2026-10-13/c001-source/rational-witness.json'
    destination.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Strict negative H witness upper:',float(witness.hi),'arch tail upper:',float(remainder.hi))

if __name__=='__main__':main()

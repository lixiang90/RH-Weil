"""Exact outward integer-interval certificate for the note 350 window ceiling.

No floating arithmetic enters verification.  A separately saved rational vector
is merely a trial solution; its residual is bounded rigorously in this program.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import json
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCALE = 10**80


def ceildiv(a, b):
    assert b > 0
    return -((-a)//b)


@dataclass(frozen=True)
class IV:
    lo: int
    hi: int

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def exact(value):
        q = Fraction(value)
        return IV(q.numerator*SCALE//q.denominator,
                  ceildiv(q.numerator*SCALE,q.denominator))

    def __add__(self, other):
        b = asiv(other)
        return IV(self.lo+b.lo,self.hi+b.hi)

    __radd__ = __add__

    def __neg__(self):
        return IV(-self.hi,-self.lo)

    def __sub__(self, other):
        return self+-asiv(other)

    def __rsub__(self, other):
        return asiv(other)+-self

    def __mul__(self, other):
        b = asiv(other)
        corners = (self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return IV(min(corners)//SCALE,ceildiv(max(corners),SCALE))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not self.lo <= 0 <= self.hi, "division interval crosses zero"
        if self.hi < 0:
            return -(-self).reciprocal()
        return IV(SCALE*SCALE//self.hi,ceildiv(SCALE*SCALE,self.lo))

    def __truediv__(self, other):
        return self*asiv(other).reciprocal()

    def __rtruediv__(self, other):
        return asiv(other)*self.reciprocal()

    def square(self):
        if self.lo <= 0 <= self.hi:
            return IV(0,ceildiv(max(self.lo*self.lo,self.hi*self.hi),SCALE))
        return self*self

    def sqrt(self):
        assert self.lo >= 0
        a=isqrt(self.lo*SCALE)
        b=isqrt(self.hi*SCALE)
        if b*b < self.hi*SCALE:
            b+=1
        return IV(a,b)

    def absupper(self):
        return max(abs(self.lo),abs(self.hi))

    def report(self):
        return {"lo_numerator":str(self.lo),"hi_numerator":str(self.hi),
                "denominator":str(SCALE)}


def asiv(value):
    return value if isinstance(value,IV) else IV.exact(value)


@lru_cache(maxsize=None)
def sin_iv(x):
    # Polynomial through degree 319.  Taylor through degree 320 has the
    # same polynomial; its real Lagrange remainder is <= |x|^321/321!.
    assert x.absupper() <= 60*SCALE
    xx=x.square()
    term=x
    total=x
    for n in range(1,160):
        term=-term*xx/((2*n)*(2*n+1))
        total=total+term
    nextterm=-term*xx/(320*321)
    error=nextterm.absupper()
    return IV(total.lo-error,total.hi+error)


@lru_cache(maxsize=None)
def sinc_iv(x):
    # m(x) = integral_I exp(ixu)du, including m(0)=1.
    if x.lo==x.hi==0:
        return asiv(1)
    assert not x.lo <= 0 <= x.hi
    return sin_iv(x/2)/(x/2)


def atan_small(x):
    assert 0 < x.lo <= x.hi < SCALE
    xx=x.square()
    power=x
    total=asiv(0)
    for n in range(120):
        term=power/(2*n+1)
        total=total+term if n%2==0 else total-term
        power=power*xx
    # Alternating-series remainder for each real x in the input interval.
    error=(power/241).absupper()
    return IV(total.lo-error,total.hi+error)


def pi_iv():
    # Machin's identity; no decimal approximation of pi is trusted.
    return 16*atan_small(asiv(Fraction(1,5)))-4*atan_small(asiv(Fraction(1,239)))


def input_geometry():
    p1=tuple(map(Fraction,("6.53624","12.37939","6.53624")))
    p2=tuple(map(Fraction,("6.56433","12.44546")))
    radius=4
    target=Fraction(673399,1000000)
    return p1,p2,radius,target


def main():
    p1,p2,radius,target=input_geometry()
    pi=pi_iv()
    a=asiv(2).sqrt()
    ma=sinc_iv(a)
    c0=asiv(Fraction(3,2))-(1-2*sin_iv(a/4).square())/ma
    # cos(a/2) = 1 - 2*sin(a/4)^2 and ma = sin(a/2)/(a/2).
    z1=asiv(sum(p1)/len(p1))/(2*pi)
    z2=asiv(sum(p2)/len(p2))/(2*pi)
    w1=(target*z2-1)/(z2-z1)
    w2=target-w1
    assert w1.lo>0 and w2.lo>0
    # Merge coincident distances as rational numbers before interval arithmetic.
    grouped={}
    for word,weight in ((p1,w1),(p2,w2)):
        for i in range(len(word)):
            for r in range(1,radius+1):
                t=sum(word[(i+l)%len(word)] for l in range(r))
                grouped[t]=grouped.get(t,asiv(0))+2*weight/len(word)
    distances=sorted(grouped)
    W=[grouped[t] for t in distances]
    t=[asiv(x) for x in distances]
    k=[(sinc_iv(x-a)+sinc_iv(x+a))/(2*ma) for x in t]
    H=[]
    for si,s in enumerate(t):
        row=[]
        for u in t:
            j=(sinc_iv(s-u)+sinc_iv(s+u))/2
            row.append(u.square()/(u.square()-2)*(j-sinc_iv(u)*k[si]))
        H.append(row)
    m=len(t)
    S=[w.sqrt() for w in W]
    row_bounds=[sum((H[i][j]*S[i]*S[j]).absupper() for j in range(m)) for i in range(m)]
    rho=max(row_bounds)
    assert rho < 9*SCALE//10
    assert max(w.hi for w in W) < 2*SCALE
    # Symmetric M = sqrt(W) H sqrt(W) has norm <= rho < .9.
    # A = W^-1-H >= (1-rho) W^-1 >= I/20.
    A=[[((1/W[i]) if i==j else asiv(0))-H[i][j] for j in range(m)] for i in range(m)]
    candidate=json.loads((ROOT/"reviews/2026-09-08/periodic-window-quadratic-candidate.json").read_text(encoding="utf-8"))
    assert candidate["distances"]==[str(x) for x in distances]
    y=[asiv(Fraction(v)) for v in candidate["trial_vector"]]
    assert len(y)==m
    Ay=[sum((A[i][j]*y[j] for j in range(m)),asiv(0)) for i in range(m)]
    residual=[k[i]-Ay[i] for i in range(m)]
    residual2=sum((v.square() for v in residual),asiv(0))
    gain=2*sum((k[i]*y[i] for i in range(m)),asiv(0))-sum((y[i]*Ay[i] for i in range(m)),asiv(0))+20*residual2
    upper=c0+gain
    bound=Fraction(673332,1000000)
    assert upper.hi*bound.denominator < bound.numerator*SCALE
    output=dict(status="PASS: rigorous outward integer interval certificate",
        arithmetic="integer endpoints on 10^-80 grid, outward-rounded operations; Taylor and Machin remainders included",
        scope="arbitrary finite even L2 profile ensembles, note 349 degree-normalized radii 1 through 4; no upper bound on actual zeros",
        target=str(target),certified_output_bound=str(bound),radius=radius,
        words=[[str(x) for x in p1],[str(x) for x in p2]],
        distances=[str(x) for x in distances],dimension=m,
        weights=[w1.report(),w2.report()],C0=c0.report(),
        max_abs_M_row_bound=dict(numerator=str(rho),denominator=str(SCALE)),
        residual_norm_squared=residual2.report(),gain_upper= gain.report(),total_upper=upper.report(),
        coercivity="A >= I/20",
        use_of_candidate="rational trial only; its residual is rigorously bounded, not assumed zero")
    out=ROOT/"reviews/2026-09-08/periodic-window-quadratic-certificate.json"
    out.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print("PASS: universal radius <= 4 certificate output < 0.673332")
    print("Scope: method ceiling only; exact interval record saved.")


if __name__=="__main__":
    main()

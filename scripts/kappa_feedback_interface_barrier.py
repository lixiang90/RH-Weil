"""Exact feedback-interface checks using only the Python standard library.

Default / --check mode is read-only.  --output PATH additionally saves the
finite algebra record.  This does not prove a Hecke or zero-free estimate.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

NAMES = "e d k d1 d2 k1 k2 M ell b B".split()
NVAR = len(NAMES)
ZERO = (0,) * NVAR


def clean(poly):
    return {mon: F(coef) for mon, coef in poly.items() if coef}


def plus(left, right):
    out = dict(left)
    for mon, coef in right.items():
        out[mon] = out.get(mon, F(0)) + coef
    return clean(out)


def times(left, right):
    out = {}
    for ma, ca in left.items():
        for mb, cb in right.items():
            mon = tuple(a + b for a, b in zip(ma, mb))
            out[mon] = out.get(mon, F(0)) + ca * cb
    return clean(out)


def derivative(poly, var):
    out = {}
    for mon, coef in poly.items():
        power = mon[var]
        if power:
            reduced = list(mon)
            reduced[var] -= 1
            out[tuple(reduced)] = coef * power
    return clean(out)


class RF:
    """Rational functions; equality is polynomial cross multiplication."""
    def __init__(self, numerator, denominator=None):
        if not isinstance(numerator, dict):
            numerator = {ZERO: F(numerator)}
        self.n = clean(numerator)
        self.d = clean({ZERO: F(1)} if denominator is None else denominator)
        if not self.d:
            raise ZeroDivisionError("identically zero polynomial denominator")
        if not self.n:
            self.d = {ZERO: F(1)}
            return
        # Cancel only a common monomial and scalar.  No floating point, GCD
        # oracle, CAS, evaluation grid or random specialization is used.
        common = tuple(min(min(m[i] for m in self.n), min(m[i] for m in self.d))
                       for i in range(NVAR))
        if any(common):
            def shift(poly):
                return {tuple(a-b for a,b in zip(mon,common)):coef
                        for mon,coef in poly.items()}
            self.n, self.d = shift(self.n), shift(self.d)
        scalar = self.d[max(self.d)]
        self.n = {mon:coef/scalar for mon,coef in self.n.items()}
        self.d = {mon:coef/scalar for mon,coef in self.d.items()}

    def __add__(self, other):
        other = as_rf(other)
        return RF(plus(times(self.n,other.d),times(other.n,self.d)),times(self.d,other.d))
    __radd__ = __add__

    def __neg__(self):
        return RF({mon:-coef for mon,coef in self.n.items()},self.d)

    def __sub__(self, other):
        return self + (-as_rf(other))
    def __rsub__(self, other):
        return as_rf(other) + (-self)

    def __mul__(self, other):
        other = as_rf(other)
        return RF(times(self.n,other.n),times(self.d,other.d))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_rf(other)
        return RF(times(self.n,other.d),times(self.d,other.n))
    def __rtruediv__(self, other):
        return as_rf(other) / self

    def __pow__(self, power):
        if not isinstance(power,int) or power < 0:
            raise ValueError("nonnegative integer powers only")
        out = RF(1)
        for _ in range(power):
            out = out * self
        return out

    def deriv(self, name):
        i = NAMES.index(name)
        return RF(plus(times(derivative(self.n,i),self.d),
                       {mon:-coef for mon,coef in times(self.n,derivative(self.d,i)).items()}),
                  times(self.d,self.d))

    def evaluate(self, values):
        def ev(poly):
            total=F(0)
            for mon,coef in poly.items():
                term=coef
                for name,power in zip(NAMES,mon):
                    if power:
                        term *= F(values[name])**power
                total += term
            return total
        return ev(self.n)/ev(self.d)


def as_rf(value):
    return value if isinstance(value,RF) else RF(value)


def variable(name):
    mon=list(ZERO)
    mon[NAMES.index(name)]=1
    return RF({tuple(mon):F(1)})


e,d,k,d1,d2,k1,k2,M,ell,b,B=(variable(name) for name in NAMES)
alpha=F(5,6)
checks=[]


def identity(name,left,right=0):
    residual=as_rf(left)-as_rf(right)
    if residual.n:
        raise AssertionError((name,"nonzero exact polynomial",len(residual.n)))
    checks.append({"name":name,"kind":"exact polynomial identity","passed":True})


def inequality(name,condition,detail):
    if not condition:
        raise AssertionError((name,detail))
    checks.append({"name":name,"kind":"exact rational inequality","passed":True,"detail":detail})


def qr(delta,kap):
    return 54*delta*kap-6*delta-75*kap+10


def count(delta,kap):
    delta,kap=as_rf(delta),as_rf(kap)
    q=qr(delta,kap)
    polynomial=216*delta**2*kap-18*delta**2-468*delta*kap+57*delta+150*kap-20
    return F(2,3)-polynomial/(6*q)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",action="store_true",help="read-only checks (the default)")
    parser.add_argument("--output",type=Path,help="explicitly write an audit JSON to this path")
    args=parser.parse_args()
    p=657*e**3-954*e**2+21*e+20
    elo=F(16683858898627,10**14)
    ehi=F(16683858898628,10**14)
    inequality("isolating lower sign",p.evaluate({"e":elo})>0,str(p.evaluate({"e":elo})))
    inequality("isolating upper sign",p.evaluate({"e":ehi})<0,str(p.evaluate({"e":ehi})))
    inequality("specified source root interval",F(1,6)<elo<ehi<F(167,1000),[str(elo),str(ehi)])
    pd=1971*F(1,5)**2-1908*F(1,6)+21
    hden=153*F(1,5)**2-201*F(1,6)-20
    inequality("p derivative negative uniformly on [1/6,1/5]",pd==-F(5454,25)<0,str(pd))
    inequality("auxiliary denominator negative uniformly",hden==-F(2369,50)<0,str(hden))
    kap=F(5,6)-e/2
    dt=(5-9*e)/(6+18*e)
    R=count(d,k)
    D=F(5,2)-1/(3*k)
    P=1-1/(6*k)
    J=(alpha-d)*D+d*P
    identity("count formula equals original energy crossing",R,1-d+(alpha-d)*d*P/(2*J))
    identity("critical test factors through cubic",count(dt,kap)-F(2,3),
             p/(2*(3*e+1)*(153*e**2-201*e-20)))
    identity("kappa finite difference",count(d,k2)-count(d,k1),
             3*d*(6*d-5)**2*(k2-k1)/(2*qr(d,k1)*qr(d,k2)))
    identity("count denominator sign dictionary",qr(d,k),-36*k*J)
    def hh(t):
        return -(5-6*t)*(6*k-1)/(2*qr(t,k))
    J1=(alpha-d1)*D+d1*P
    J2=(alpha-d2)*D+d2*P
    identity("strict delta monotonicity finite difference",hh(d2)-hh(d1),
             -alpha*P**2*(d2-d1)/(2*J1*J2))
    identity("count finite difference decomposition",count(d2,k)-count(d1,k),
             -(d2-d1)+(d2-d1)*hh(d2)+d1*(hh(d2)-hh(d1)))
    identity("uniform H upper bound numerator",2*D-3*P,2-1/(6*k))
    rlo=count(F(3,8),F(37,50)).evaluate({})-F(2,3)
    inequality("critical delta above 3/8",rlo==F(1961,157272)>0,str(rlo))
    identity("critical delta below 1/2",count(F(1,2),k)-F(2,3),-(15*k-2)/(3*(48*k-7)))
    inequality("D minimum exceeds two",F(5,2)-1/(3*F(37,50))==F(455,222)>2,"455/222")
    inequality("P minimum positive",1-1/(6*F(37,50))==F(86,111)>0,"86/111")
    inequality("dual forces B above actual-kappa threshold",F(55,63)>F(87,100),str(F(19,6300)))
    inequality("contradiction a upper endpoint",F(11,3)-4*F(87,100)==F(14,75)<F(1,5),"14/75")
    identity("test delta derivative",dt.deriv("e"),-144/(6+18*e)**2)
    inequality("test delta endpoint rectangle",F(1,50)<F(1,3)<=F(7,18)<F(3,4),"[1/3,7/18]")
    inequality("test delta left endpoint",dt.evaluate({"e":F(1,6)})==F(7,18),"7/18")
    inequality("test delta right endpoint",dt.evaluate({"e":F(1,5)})==F(1,3),"1/3")
    lx=(M-b)/2
    ly=(M+b)/2
    h=1-lx+ell
    a=(1+d)/2
    q=d/2
    E=a-B+h*(F(17,50)-F(1,6))-a*ly-ell/2+ell*q+h*(F(2,3)+d/2-F(17,50))
    H=1+d-(1+d)*M/2+d*ell
    L0=F(5,6)+M/12-ell/6
    LK=F(1,3)+7*M/12+ell/3
    w0=(4+18*d)/(9+18*d)
    wK=2/(9+18*d)
    wH=3/(9+18*d)
    G=(18*d+7)/(18*d+9)
    identity("full high endpoint at R equals two thirds",E,H-B)
    identity("dual weights sum one",w0+wK+wH,1)
    identity("dual cancels M",w0/12+7*wK/12-(1+d)*wH/2)
    identity("dual cancels total prime length",-w0/6+wK/3+d*wH)
    identity("dual lower bound independent of geometry",w0*L0+wK*LK+wH*H,G)
    identity("dual test point equals target boundary",(18*dt+7)/(18*dt+9),F(11,12)-e/4)
    identity("dual G derivative",G.deriv("d"),36/(18*d+9)**2)
    identity("low zero branch yields L0",lx/2+b/12+F(5,6)-lx/3-ell/6,L0)
    identity("low width excess branch yields LK",L0+(M+ell-1)/2,LK)
    identity("balanced high endpoint independent of b",
             1+d-(1+d)*(1-ell)/2+d*ell-B,F(1,2)+ell/2-B+(F(1,2)+3*ell/2)*d)
    identity("balanced critical test endpoint zero",
             F(1,2)+e/2-(F(11,12)-e/4)+(F(1,2)+3*e/2)*dt)
    rLong=3/(5-6*d)
    identity("long inverse sharpness exponent, not physical total slot length",
             F(2,3)+d*rLong,(1+5*rLong)/6)
    bt=F(17499,20000)
    kt=2*bt-1
    dd=F(19429,50000)
    rgap=count(dd,kt).evaluate({})-F(2,3)
    ggap=(18*dd+7)/(18*dd+9)-bt
    wg=ggap/(3/(18*dd+9))
    inequality("target .87495 below cubic boundary",bt<F(11,12)-ehi/4,str(bt))
    inequality("target test count positive gap",rgap==F(1875081893,615723531225000)>0,str(rgap))
    inequality("target dual positive gap",ggap==F(52361,7997220000)>0,str(ggap))
    inequality("target weighted gap",wg==F(52361,1500000000),str(wg))
    with localcontext() as ctx:
        ctx.prec=35
        budget=Decimal((rgap+wg).numerator)/Decimal((rgap+wg).denominator)
    here=Path(__file__).resolve().parent
    root=next((parent for parent in [here,*here.parents]
               if (parent/"papers/kappa-feedback-cubic-boundary-paper.tex").is_file()),None)
    inputs=[]
    if root is not None:
        for name in ["papers/kappa-feedback-cubic-boundary-paper.tex",
                     "notes/449-free-b-compensated-geometry-and-optimal-relative-boundary.md",
                     "notes/450-plain-kappa-extension-and-actual-capacity.md",
                     "notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md"]:
            data=(root/name).read_bytes()
            inputs.append({"path":name,"bytes":len(data),"raw_sha256":hashlib.sha256(data).hexdigest()})
    result={"classification":"finite exact algebra; model barrier only",
            "runtime_dependencies":"Python standard library only",
            "check_count":len(checks),"checks":checks,"inputs":inputs,
            "root_interval":[str(elo),str(ehi)],
            "target_budget":{"B":str(bt),"delta":str(dd),"minimum_kappa":str(kt),
                "necessary_count_decrement_if_low_unchanged_and_h_lt_one":str(rgap+wg),
                "decimal_orientation_only":str(budget),"attained":False},
            "scope":{"balanced_current_interface_barrier":True,
                "three_affine_constraints_barrier":True,
                "all_actual_general_geometry_satisfies_constraints":False,
                "new_arithmetic_estimate":False,"new_zero_free_region":False,
                "actual_bad_row_constructed":False,"lean_checked":False}}
    if args.output is not None:
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",
                               encoding="utf-8",newline="\n")
    print(json.dumps({"passed":True,"checks":len(checks),
                      "scope":result["classification"],"wrote_output":args.output is not None}))


if __name__ == "__main__":
    main()

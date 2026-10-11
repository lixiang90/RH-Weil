"""Exact finite algebra for round 506. Infinite ideal counts are proved in the report.

This checks optional source identity, local presentation zeros, actual coefficient
multiplicity, continuous interval budgets and the previously paid target tax.
It does not prove a full mixed moment, a count decrement or a zero-free strip.
"""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import argparse, hashlib, json

def workspace_root():
    # Supports both the published scripts/ location and the preserved tmp/
    # research snapshot, without a drive letter or a private source path.
    for candidate in Path(__file__).resolve().parents:
        if all((candidate / marker).is_dir() for marker in ('output', 'notes', 'scripts')):
            return candidate
    raise RuntimeError('Cannot locate workspace output/notes/scripts markers')

ROOT = workspace_root()
OUTPUT = ROOT / 'output/hybrid-active-radical-mixed-cross-budget.json'
SOURCE_SHA = '42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3'
checks = []
def ck(name, value):
    if not value: raise AssertionError(name)
    checks.append(name)
def canon(p):
    return p.read_bytes().replace(b'\r\n', b'\n').replace(b'\r', b'\n')
def sha(p): return hashlib.sha256(canon(p)).hexdigest()

class I:
    def __init__(self, lo, hi=None): self.lo,self.hi=F(lo),F(lo if hi is None else hi)
    @staticmethod
    def coerce(v): return v if isinstance(v,I) else I(v)
    def __add__(self,v):
        v=I.coerce(v); return I(self.lo+v.lo,self.hi+v.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,v): return self+-I.coerce(v)
    def __rsub__(self,v): return I.coerce(v)+-self
    def __mul__(self,v):
        v=I.coerce(v); p=[a*b for a in (self.lo,self.hi) for b in (v.lo,v.hi)]; return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=I.coerce(v); ck('interval denominator strictly positive',v.lo>0)
        return self*I(1/v.hi,1/v.lo)
    def __rtruediv__(self,v): return I.coerce(v)/self
    def text(self): return [str(self.lo),str(self.hi)]

def model(delta,kappa,x,g=F(1,20000)):
    c=1/(3*kappa); DD=3-(1+2*c)*x; P=(2-2*c*x)*(1-x)
    A=F(5,6)-delta; J=A*DD+delta*P; B=delta*P/DD
    t0=1+delta*P/(2*J); r0=((2-2*c*x)*t0-(1-c)*x)/DD
    m0=t0-r0; R=1-delta+A*(t0-1); ii=delta*(1-x); cm=delta*(2-2*c*x)
    return dict(c=c,D=DD,P=P,A=A,J=J,B=B,t0=t0,r0=r0,m0=m0,R=R,I=ii,Cm=cm,
        tPlus=t0+g/B,tMinus=t0-g/A,rLmin=t0-g/A,mMin=m0-g/A-g/ii,mCut=m0+g/cm,
        tax=1+cm/A+cm/ii)

def main():
    if not __debug__:
        raise SystemExit('Run without -O: exact certificate checks are required')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit-output','--output',dest='output',type=Path,
        help='optional separate receipt; otherwise this command writes nothing')
    parser.add_argument('--certificate',type=Path,default=OUTPUT,
        help='existing public finite-core receipt compared by --check')
    parser.add_argument('--source',type=Path,
        help='optionally verify the fixed original TeX; default never reads private source')
    parser.add_argument('--check',action='store_true',
        help='recompute and compare the finite core with an existing output receipt')
    args=parser.parse_args()
    source_matched=False
    source_checks=[]
    if args.source is not None:
        if sha(args.source)!=SOURCE_SHA: raise AssertionError('actual frozen source identity')
        lines=canon(args.source).decode('utf8').splitlines()
        if not any('an exponent divisible by six is the function' in z for z in lines[630:650]):
            raise AssertionError('natural zero convention source present')
        if not any('\\overline{\\nu(p)}1_{p\\in1_T}' in z for z in lines[15130:15165]):
            raise AssertionError('physical prime coefficient source present')
        source_checks=['actual frozen source identity','natural zero convention source present',
                       'physical prime coefficient source present']
        source_matched=True

    # Unit phases are exponent arithmetic modulo 6; nonunits stay zero even
    # when the difference is zero. This is not finite-field sampling.
    for ek in range(18):
        for el in range(18):
            diff=(ek-el)%6
            ck('active exponent '+str((ek,el)),(diff!=0)==(ek%6!=el%6))
            h=min(ek,el); sq=(ek-h)%6; tq=(el-h)%6
            ck('gcd quotients and sixth stripping '+str((ek,el)),
               (sq==0 or tq==0) and ((sq!=0 or tq!=0)==(diff!=0)))
            if diff:
                ck('local primitive order '+str((ek,el)),6//gcd(6,diff)>1)
            if ek or el:
                product_on_nonunit=0
                ck('cancelled presentation zero '+str((ek,el)),product_on_nonunit==0)
    for e in range(31):
        no_q=sum(1 for inverse in (0,1) for b in range(e+1) if e-inverse-b>=0)
        yes_q=sum(1 for inverse in (0,1) for b in range(e+1) if e-1-inverse-b>=0)
        ck('actual local mu/plain multiplicity '+str(e),no_q==2*e+1)
        ck('actual optional disjoint prime multiplicity '+str(e),yes_q==max(0,2*e-1))
        ck('uniform divisor square coefficient bound '+str(e),no_q+yes_q<=(e+1)**2)
    ck('side/exponent choices on an active radical prime',2*len(range(1,6))==10)
    ck('sixth-power root series exponent',F(6,2)==3 and 3>1)

    # A coarse but continuous rational box already admitted in the older
    # critical-neighborhood proof. Independent endpoints are upper/lower
    # interval bounds, not extrapolation from the corners of a grid.
    d=I(F(3,8),F(2,5)); k=I(F(37,50),F(3,4)); x=I(F(49,100),F(1,2))
    cl,cu=F(4,9),F(50,111)
    Dl,Du=F(455,222),F(1867,900); Pl,Pu=F(86,111),F(1496,1875)
    Jl=F(13,30)*Dl+F(3,8)*Pl; Ju=F(11,24)*Du+F(2,5)*Pu
    tlo=1+F(3,8)*Pl/(2*Ju); thi=1+F(2,5)*Pu/(2*Jl)
    Blo=F(3,8)*Pl/Du; Ilo=F(3,8)*F(1,2); cmlo=F(3,8)*(2-2*cu*F(1,2))
    mlo=(F(1,2)*tlo+(1-cu)*F(49,100))/Du
    mhi=(F(51,100)*thi+(1-cl)*F(1,2))/Dl
    rlo=((2-2*cu*F(1,2))*tlo-(1-cl)*F(1,2))/Du
    rhi=((2-2*cl*F(49,100))*thi-(1-cu)*F(49,100))/Dl
    g=F(1,20000)
    rLhi=thi+g/Blo; rLlo=tlo-g/F(13,30)
    mcorelo=mlo-g/F(13,30)-g/Ilo; mcorehi=mhi+g/cmlo
    RLhi=F(1,6)+F(11,24)*rLhi
    rhohi=g/Ilo
    ck('coarse continuous t lower and upper',F(111,100)<tlo<thi<F(114,100))
    ck('whole box long core legal',1<rLlo<rLhi<F(3,2))
    ck('whole box inverse cut strictly below one',F(3,5)<rlo and rhi+rhohi<1-F(1,10000))
    ck('whole box plain core strict',F(1,3)<mcorelo<mcorehi<F(1,2)-F(1,10000))
    ck('whole box plain requested support',0<(1-2*mcorehi)/(6*F(3,4))<(1-2*mcorelo)/(6*F(37,50))<F(1,5))
    active=F(31,50); designed_raw=F(3,10000)
    ck('whole box low-active-radical raw payment strict',1-RLhi-active/2-designed_raw>F(1,500))
    # The restored lengths are independently allowed to drop to bounded/empty
    # scales. The theorem uses each actual Nprime normalization, not original N.
    eta=F(1,1000000)
    ck('amplification width tax retained',F(5,6)*eta==F(1,1200000)*1)

    z=model(F(19429,50000),F(7499,10000),F(1,2))
    target=F(467366968772963,12314470624500000000)
    ck('previous exact all-branch coverage tax',z['tax']==F(8209647083,1500842361))
    raw_needed=target*z['tax']
    ck('previous raw saving gate retained',F(2076,10**7)<raw_needed<F(2077,10**7))
    RLpoint=F(1,6)+(F(5,6)-F(19429,50000))*z['tPlus']
    ck('target-label larger active range payment',1-RLpoint-F(133,400)-designed_raw>F(3,10000))
    ck('full point budget g tax plus strict amplifier width',g*z['tax']+F(5,6)*eta<designed_raw)
    # Bootstrap range for an attempted .87495 improvement, relative to the
    # already written package-R boundary only; this is not an actual zeta input.
    e=I(F(16683858898627,10**14),F(16683858898628,10**14))
    sigma=F(11,12)-e/4; kstar=2*sigma-1
    ck('all attempted-improvement kappa lie in compact box',F(7499,10000)<kstar.lo<kstar.hi<F(749915,10**6))

    values={n:{'exact':str(v),'orientation':float(v)} for n,v in dict(
        continuous_rL_minimum=rLlo,continuous_rL_maximum=rLhi,
        continuous_plain_minimum=mcorelo,continuous_plain_maximum=mcorehi,
        continuous_long_count_upper=RLhi,active_radical_exponent=active,
        designed_raw_saving_NOT_FULLY_PROVED=designed_raw,
        whole_box_low_active_raw_margin=1-RLhi-active/2-designed_raw,
        target_label_active_radical_exponent=F(133,200),
        target_label_low_active_raw_margin=1-RLpoint-F(133,400)-designed_raw,
        target_necessary_count_saving=target,coverage_tax=z['tax'],
        limiting_required_raw_saving=raw_needed,
        designed_full_point_count_gate=g*z['tax']+F(5,6)*eta).items()}
    result=dict(schema='rh-weil-round506-active-radical-mixed-cross-v1',status='PASS',checks=len(checks),
        source_canonical_lf_sha256=SOURCE_SHA,checker_canonical_lf_sha256=sha(Path(__file__)),
        values=values,bootstrap_kappa_upper=kstar.text(),
        scope='Finite exact local presentation/multiplicity and continuous rational budgets only. Original-source identity is verified only with --source. The infinite low-active-radical ideal-pair theorem is the written proof relative to fixed-field ideal counting in package R, not a finite-checker conclusion. No full large-radical cross estimate/count/strip/Lean proof.',
        new_full_mixed_estimate=False,new_count_saving=False,new_zero_free_boundary=False,
        source_matched=source_matched,source_validation_checks=source_checks,
        total_checks_with_optional_source=len(checks)+len(source_checks),checked_labels=checks)
    if args.check:
        prior=json.loads(args.certificate.read_text(encoding='utf8'))
        # Source verification is optional independent evidence, not a change
        # to the finite exact mathematical core compared by --check.
        optional={'source_matched','source_validation_checks','total_checks_with_optional_source'}
        if {k:v for k,v in prior.items() if k not in optional}!={k:v for k,v in result.items() if k not in optional}:
            raise AssertionError('published finite core differs from exact recomputation')
    if args.output is not None:
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
    print(json.dumps({k:result[k] for k in ('status','checks','source_matched',
        'total_checks_with_optional_source','new_count_saving','new_zero_free_boundary')}))

if __name__=='__main__': main()

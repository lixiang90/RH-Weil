"""Independent rational source-row checks for the phase/flux formulas in note507.

This integer-period model does not prove the prime-log small-divisor theorem.
Source matrices are evaluated before comparing the asserted edge formulas.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import json
from source_orbit_gram_exact_audit import Fibre

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/'reviews/2026-10-11/f1-source-phase-exact-audit.json'


def main():
    counts=Counter()
    def check(value,name):
        assert value,name
        counts[name]+=1
    fibre=Fibre(5,7)
    L,M=fibre.L,fibre.M
    times=range(2*max(L,M))
    @lru_cache(None)
    def moved(power,x):
        return fibre.source(x,fibre.vector(x),power)

    for weights in ((Q(1),Q(2),Q(3),Q(1,2),Q(4,3),Q(2,5),Q(7,6)),
                    (Q(1),Q(-2),Q(3),Q(-1,2),Q(4,3),Q(-2,5),Q(7,6))):
        def C(x):
            return weights[x%M]
        def P(theta):
            return sum((fibre.c(t)**2*C(t+theta) for t in times),Q(0))
        @lru_cache(None)
        def rectangle(r,s,kp,kq):
            result=Q(0)
            for t in times:
                for j in range(-kp,13):
                    for k in range(-kq,5):
                        x=t-j*L-k*M
                        a=moved(r,x).get((j,k),Q(0))
                        b=moved(s,x).get((j,k),Q(0))
                        if a and b:
                            result+=a*b*C(x)
            return result
        for r in range(-1,2):
            for s in range(-1,2):
                mu=Q(0)
                for y in range(-30,31):
                    formula=(fibre.d(y)**2-fibre.f(y)**2
                             +fibre.f(y-r*M)*fibre.f(y-s*M))
                    actual=Q(0)
                    for j in range(-12,13):
                        t=y+j*L
                        x=t-j*L+20*M
                        actual+=(moved(r,x).get((j,-20),Q(0))
                                 *moved(s,x).get((j,-20),Q(0)))
                    check(actual==formula,'full_source_deep_q_cross_energy')
                    mu+=formula*C(y)
                beta=sum((fibre.f(y)*fibre.f(y-(s-r)*M)*C(y)
                          for y in times),Q(0))
                charge=Q(r==s)*sum(weights,Q(0))-beta
                for kp,kq in ((18,16),(21,19)):
                    value=rectangle(r,s,kp,kq)
                    check(rectangle(r,s,kp+1,kq)-value==Q(r==s)*P((kp+1)*L),
                          'independent_rectangle_p_increment')
                    check(rectangle(r,s,kp,kq+1)-value==mu,
                          'independent_rectangle_q_increment')
                    for shift in (-1,1):
                        check(rectangle(r+shift,s+shift,kp,kq)-value==-shift*charge,
                              'weighted_source_conjugation_flux')
        check(sum((P(theta) for theta in range(M)),Q(0))
              ==L*sum(weights,Q(0)),'square_partition_mean_of_p_profile')

    def add(a,b):return a[0]+b[0],a[1]+b[1]
    def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
    def neg(a):return -a[0],-a[1]
    def div(a,b):
        d=b[0]**2+b[1]**2
        return (a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d
    one=(Q(1),Q(0));zero=(Q(0),Q(0))
    for z in ((Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(-3,5),Q(4,5))):
        g=div(z,add(z,neg(one)))
        for rho2 in (Q(1,2),Q(1,3)):
            h=div(mul((1-rho2,Q(0)),z),add(one,neg(mul((rho2,Q(0)),z))))
            power=one;total=zero
            for k in range(1,21):
                power=mul(power,z);total=add(total,power)
                direct=add(total,mul(h,power))
                expected=add(mul(add(g,h),power),neg(g))
                check(direct==expected,'exact_fourier_phase_telescoping_with_ball_tail')
    receipt={'status':'passed_exact_source_phase_models','total_exact_assertions':sum(counts.values()),
             'checks':dict(sorted(counts.items())),
             'script_sha256':hashlib.sha256(Path(__file__).read_bytes().replace(b'\r\n',b'\n')).hexdigest(),
             'dependency_sha256':hashlib.sha256((ROOT/'scripts/source_orbit_gram_exact_audit.py').read_bytes().replace(b'\r\n',b'\n')).hexdigest(),
             'model':{'p_period':L,'q_period':M,'weights':'nonconstant positive and signed rational periodic diagonals'},
             'scope':'Exact source-matrix cross energies, cutoff increments and nonconstant weighted conjugation flux; Fourier telescoping retains the full rational ball tail. Integer-period discrete models do not prove smooth prime-log trace-class, irrational Diophantine bounds, infinite cutoff limits, positivity, adelic comparison, RR or RH.'}
    REPORT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(receipt,ensure_ascii=False))


if __name__=='__main__':main()

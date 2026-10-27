"""Certify the first four finite-domain terms of the frozen c2 test.

The input is the already certified exact analytic ell*=g+p*, f=B h0.
No old lowband scalar or G action is recomputed. Integer endpoint sine
products are integrated exactly through Si identities; all transcendental
evaluation uses rational pi and outward integer intervals.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from math import isqrt
import hashlib
import json
from pathlib import Path
import time

from tf_reader_arch_gap_certificate import Intervals


class Fixed:
    def __init__(self, precision):
        self.a = Intervals(precision)
        self.unit = self.a.unit
        self.zero = self.a.enclose(F(0))
        self.one = self.a.enclose(F(1))

    def scale(self, value, coefficient):
        return ((value[0]*coefficient, value[1]*coefficient) if coefficient >= 0
                else (value[1]*coefficient, value[0]*coefficient))

    def div_int(self, value, positive):
        assert positive > 0
        return value[0]//positive, -((-value[1])//positive)

    def rational_mul(self, value, coefficient):
        return self.div_int(self.scale(value, coefficient.numerator), coefficient.denominator)

    def serialize(self, value):
        return [str(F(x, self.unit)) for x in value]


class HalfIntegerSi:
    """Q(k)=pi*k*(pi/2-Si(pi*k)), k integer>=0, Q(0)=0.

    At k>=80 the value is (-1)^k times a positive Laplace integral.
    This parity is essential: the old integer-frequency T reader only saw
    even k. The small-k Taylor has a real integrated sine remainder.
    """
    def __init__(self, fixed, pi_low, pi_high, target_digits=60):
        self.f = fixed
        self.a = fixed.a
        self.pi = self.a.enclose(pi_low, pi_high)
        self.pi2 = self.a.mul(self.pi, self.pi)
        self.pi_mid = self.a.enclose((pi_low+pi_high)/2)
        self.pi_radius = self.a.enclose((pi_high-pi_low)/2)[1]
        self.tolerance = 10**(len(str(fixed.unit))-1-target_digits)
        self.cache = {0: fixed.zero}
        self.max_taylor_terms = 0
        self.max_laplace_terms = 0

    def at(self, k):
        assert isinstance(k, int) and k >= 0
        if k in self.cache:
            return self.cache[k]
        f,a = self.f,self.a
        if k >= 80:
            x = f.scale(self.pi, k)
            x2 = a.mul(x,x)
            term,total,j = f.one,f.zero,0
            while True:
                total = a.add(total, term if j%2 == 0 else a.neg(term))
                nxt = a.div(f.scale(term,(2*j+2)*(2*j+1)),x2)
                j += 1
                if nxt[1] <= self.tolerance:
                    remainder = (0,nxt[1]) if j%2 == 0 else (-nxt[1],0)
                    amplitude = a.add(total,remainder)
                    value = amplitude if k%2 == 0 else a.neg(amplitude)
                    self.max_laplace_terms = max(self.max_laplace_terms,j)
                    break
                if j>1000 or nxt[1]>term[1]:
                    raise ArithmeticError('Laplace remainder missed frozen target')
                term=nxt
        else:
            x=f.scale(self.pi_mid,k)
            x2=a.mul(x,x)
            term,total,j=x,f.zero,0
            while True:
                total=a.add(total,term if j%2 == 0 else a.neg(term))
                nxt=f.div_int(f.scale(a.mul(term,x2),2*j+1),(2*j+3)**2*(2*j+2))
                j+=1
                if nxt[1] <= self.tolerance:
                    total=a.add(total,(-nxt[1],nxt[1]))
                    # |Si'|<=1 transports actual pi from its rational midpoint.
                    arg_error=k*self.pi_radius
                    si=a.add(total,(-arg_error,arg_error))
                    value=a.sub(f.div_int(f.scale(self.pi2,k),2),
                                a.mul(f.scale(self.pi,k),si))
                    self.max_taylor_terms=max(self.max_taylor_terms,j)
                    break
                if j>3000:
                    raise ArithmeticError('Small Si Taylor missed frozen target')
                term=nxt
        self.cache[k]=value
        return value


def add_endpoint(weights, twice_frequency, coefficient):
    assert twice_frequency > 0 and isinstance(twice_frequency,int)
    weights[twice_frequency]=weights.get(twice_frequency,0)+coefficient


def product_integral(left, right, radius, nf, fixed, reader, label):
    """Integral of two endpoint sin/(pi*y) sums on (0,radius).

    Dictionary key m means frequency a=m/2; coefficients are integer/nf.
    2*radius*a and 2*radius*b are integers for all inputs here. The exact
    product kernel is min(a,b)+(Q(kminus)-Q(kplus))/(2*pi²*radius).
    """
    a=fixed.a
    grouped={}
    base_twice=0
    for m,cm in sorted(left.items()):
        assert (radius*m).denominator == 1
        for n,cn in sorted(right.items()):
            assert (radius*n).denominator == 1
            coefficient=cm*cn
            base_twice += coefficient*min(m,n)
            plus=int(radius*(m+n))
            minus=int(radius*abs(m-n))
            assert plus%2 == minus%2
            grouped[minus]=grouped.get(minus,0)+coefficient
            grouped[plus]=grouped.get(plus,0)-coefficient
    grouped={k:c for k,c in grouped.items() if k and c}
    value=fixed.zero
    for count,(k,coefficient) in enumerate(sorted(grouped.items()),1):
        value=a.add(value,fixed.scale(reader.at(k),coefficient))
        if count%20000 == 0:
            print(json.dumps({'stage':label,'frequencies_done':count,
                              'frequencies_total':len(grouped)}),flush=True)
    factor=F(1,2*nf*nf)/radius
    correction=a.div(fixed.rational_mul(value,factor),reader.pi2)
    result=a.add(a.enclose(F(base_twice,2*nf*nf)),correction)
    return result, {'endpoint_pairs':len(left)*len(right),
                    'nonzero_Q_frequencies':len(grouped),
                    'exact_full_halfline_kernel_sum':str(F(base_twice,2*nf*nf))}


def sine_moments(twice_frequency, radius, degree, fixed, reader):
    """J_j=integral_0^R y^(2j-1) sin(pi*m*y)/pi, j0 is Si/pi."""
    m=twice_frequency
    k=radius*m
    assert k.denominator == 1 and m>0
    k=int(k)
    a=fixed.a
    inv_pi=a.div(fixed.one,reader.pi)
    inv_frequency=fixed.div_int(inv_pi,m)  # 1/(pi*m)
    inv_frequency2=a.mul(inv_frequency,inv_frequency)
    value0=a.sub(a.enclose(F(1,2)),
                 a.div(fixed.div_int(reader.at(k),k),reader.pi2))
    values=[value0]
    sign=1 if k%2 == 0 else -1
    integral=fixed.rational_mul(inv_frequency,-radius*sign)
    for j in range(1,degree+1):
        if j>1:
            n=2*j-1
            first=fixed.rational_mul(inv_frequency,-radius**n*sign)
            integral=a.sub(first,fixed.scale(a.mul(inv_frequency2,integral),n*(n-1)))
        values.append(a.mul(integral,inv_pi))
    return values


def polynomial_endpoint_pair(poly, endpoints, radius, nf, fixed, reader):
    total=fixed.zero
    a=fixed.a
    for m,coefficient in sorted(endpoints.items()):
        moments=sine_moments(m,radius,len(poly)-1,fixed,reader)
        for pj,moment in zip(poly,moments):
            total=a.add(total,fixed.rational_mul(moment,pj*F(coefficient,nf)))
    return total


def lfhash(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b'\r\n',b'\n')).hexdigest()


def make_record(vector_path,gap_path,precision=180):
    started=time.perf_counter()
    fixed=Fixed(precision);a=fixed.a
    vector=json.loads(Path(vector_path).read_text())
    gap=json.loads(Path(gap_path).read_text())
    assert vector['primes']==[2,3,5,7,11,13,17,19] and vector['N_F']==9699690
    nf=vector['N_F']
    pi_low,pi_high=map(F,gap['pi_interval'])
    reader=HalfIntegerSi(fixed,pi_low,pi_high,target_digits=60)
    sqrt_integer=isqrt(2*fixed.unit*fixed.unit)
    assert sqrt_integer*sqrt_integer<=2*fixed.unit*fixed.unit<(sqrt_integer+1)**2
    sqrt2=(sqrt_integer,sqrt_integer+1)
    inverse_sqrt2=a.div(fixed.one,sqrt2)
    tau={2*t['u']:t['numerator'] for t in vector['g_descriptor']['tau_scaled_integer_terms']}
    assert sum(tau.values())==0
    poly=list(map(F,vector['p_star_even_monomial_coefficients']))
    steps=[]
    for t in vector['f_B_h0_step_terms']:
        l,r,c=F(t['left']),F(t['right']),F(t['coefficient'])
        assert l.denominator==r.denominator==1 and (c*nf).denominator==1
        steps.append((int(l),int(r),int(c*nf)))
    first_exact=F(sum(c*d*max(0,min(r,2*v)-max(l,2*u))
                         for l,r,c in steps for u,v,d in steps),nf*nf)
    first=a.mul(a.enclose(first_exact),inverse_sqrt2)
    endpoint_up={};endpoint_down={}
    for l,r,c in steps:
        add_endpoint(endpoint_up,4*r,c)
        add_endpoint(endpoint_up,4*l,-c)
        left=max(F(1),F(l,2));right=F(r,2)
        if right>left:
            add_endpoint(endpoint_down,int(2*right),c)
            add_endpoint(endpoint_down,int(2*left),-c)
    endpoint_up={m:c for m,c in endpoint_up.items() if c}
    endpoint_down={m:c for m,c in endpoint_down.items() if c}
    assert sum(endpoint_up.values())==sum(endpoint_down.values())==0
    print(json.dumps({'stage':'cross_down','endpoint_terms':len(endpoint_down)}),flush=True)
    gg_down,ledger_down=product_integral(tau,endpoint_down,F(1),nf,fixed,reader,'cross_down')
    pg_down=polynomial_endpoint_pair(poly,endpoint_down,F(1),nf,fixed,reader)
    cross_down=a.mul(a.add(gg_down,pg_down),sqrt2)
    print(json.dumps({'stage':'cross_up','endpoint_terms':len(endpoint_up),
                      'elapsed_seconds':time.perf_counter()-started}),flush=True)
    gg_up,ledger_up=product_integral(tau,endpoint_up,F(1),nf,fixed,reader,'cross_up')
    pg_up=polynomial_endpoint_pair(poly,endpoint_up,F(1),nf,fixed,reader)
    cross_up=a.mul(a.add(gg_up,pg_up),inverse_sqrt2)
    twice_tau={2*m:c for m,c in tau.items()}
    print(json.dumps({'stage':'compact_dilation','elapsed_seconds':time.perf_counter()-started}),flush=True)
    gg_dilation,ledger_dilation=product_integral(tau,twice_tau,F(1,2),nf,fixed,reader,'compact_dilation')
    gg_dilation=fixed.div_int(gg_dilation,2)
    p_twice=[pj*4**j for j,pj in enumerate(poly)]
    gp_dilation=polynomial_endpoint_pair(p_twice,tau,F(1,2),nf,fixed,reader)
    pg_dilation=fixed.div_int(polynomial_endpoint_pair(poly,twice_tau,F(1,2),nf,fixed,reader),2)
    pp_dilation=sum((pj*pk*4**k*F(1,2)**(2*j+2*k+1)/F(2*j+2*k+1)
                    for j,pj in enumerate(poly) for k,pk in enumerate(poly)),F(0))
    compact=a.mul(a.add(a.add(gg_dilation,gp_dilation),
                       a.add(pg_dilation,a.enclose(pp_dilation))),sqrt2)
    terms={'f_U_f':first,'ell_FH_Uinverse_f':cross_down,
           'ell_FH_U_f':cross_up,'ell_Uinverse_ell':compact}
    widths={key:F(value[1]-value[0],fixed.unit) for key,value in terms.items()}
    assert all(width <= F(1,16384) for width in widths.values()),widths
    return {
      'schema':'tf-reader-fixed-c2-first-four-v1',
      'scope':'First four exact finite-domain terms for the same frozen real input; not assembled c2, G action or q0 acceptance.',
      'precision':precision,'Q_target_digits':60,'interval_unit':str(fixed.unit),
      'source_files_lf_sha256':{str(vector_path):lfhash(vector_path),str(gap_path):lfhash(gap_path),
                              'scripts/tf_reader_arch_gap_certificate.py':lfhash('scripts/tf_reader_arch_gap_certificate.py'),
                              'scripts/tf_reader_c2_mixed_terms.py':lfhash(__file__)},
      'terms':{key:fixed.serialize(value) for key,value in terms.items()},
      'term_widths':{key:str(value) for key,value in widths.items()},
      'all_term_widths_le_1_over16384':True,
      'display_only':{key:[float(F(x,fixed.unit)) for x in value] for key,value in terms.items()},
      'error_ledger':{
          'arithmetic':'Outward fixed-point integer intervals at every elementary operation; sqrt2 via exact isqrt, pi via existing rational Machin enclosure.',
          'sine_products':'Exact endpoint kernel min(a,b)+(Qminus-Qplus)/(2*pi^2*R), no quadrature/grid or physical tail clipping.',
          'high_Q':'k>=80: Q(k)=(-1)^k integral_0^infinity exp(-s)/(1+(s/(pi*k))^2) ds; finite geometric remainder signed and <=next factorial term.',
          'small_Q':'k<80: Si at rational pi midpoint with real integrated sine Taylor remainder and actual argument error via |Si prime|<=1.',
          'polynomial_pairs':'Exact odd sine-moment recurrence plus j0 Si/pi; rational p* coefficients selected in previous vector record are used exactly.',
          'input_transport':'Not included here: root must pay delta_v for v->v* when assembling the five terms.',
          'missing_fifth_term':'Not included: integral_0^2 Fell*(x)*2^-1/2 Fell*(x/2)dx certified by separate module.'},
      'counts':{'f_steps':len(steps),'g_endpoints':len(tau),'p_even_terms':len(poly),
                'cross_up_endpoints':len(endpoint_up),'cross_down_endpoints':len(endpoint_down),
                'unique_Q_values_including0':len(reader.cache),'max_small_Si_Taylor_terms':reader.max_taylor_terms,
                'max_Laplace_terms':reader.max_laplace_terms},
      'product_ledgers':{'cross_down':ledger_down,'cross_up':ledger_up,'compact_dilation':ledger_dilation},
      'exact_subexpressions':{'f_U_f_before_inverse_sqrt2':str(first_exact),'p_p2_integral_before_sqrt2':str(pp_dilation)},
      'elapsed_seconds':time.perf_counter()-started,
      'claim_limits':'Fixed physical h0/F8, cutoff1 and real coefficient input only. Does not alter all-complex/source-growth coverage, full signed Weil/Gamma/proper-power/pole accounting, whole4/5 UPPER, G inverse or long Goal gate.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--vector',default='reviews/2026-10-27/tf-reader-execution/lowband-vector-input.json')
    parser.add_argument('--gap',default='reviews/2026-10-27/tf-reader/arch-gap-certificate.json')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    record=make_record(args.vector,args.gap)
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes((json.dumps(record,indent=2)+'\n').encode())
    print(json.dumps({'status':'certified-first-four-c2-terms','terms':record['display_only'],
                      'elapsed_seconds':record['elapsed_seconds'],'output':str(output)}),flush=True)


if __name__=='__main__':
    main()

"""Own exact rational geometric upper bound for the frozen even64 proposal."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json
import hashlib
import mpmath as mp

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[2]
mp.mp.dps=80
results=json.loads((HERE/'sonin-source-reconstruction.json').read_text())
proposal=next(r for r in results['results'] if r['size_per_sector']==64 and r['parity']==0)
coeff=[F(mp.nstr(mp.mpf(x),50)) for x in proposal['raw_polynomial_coefficients']]
orders=proposal['orders']
frozen={'kind':'fixed-exact-rational-closed-form-source','orders':orders,
        'raw_coefficients':[str(c) for c in coeff],
        'source_half_window':'17/16','zero_extension':True,'polynomial_degree':126,
        'origin':'even64 ordinary80 proposal,50-significant-decimal rational rounding'}
(HERE/'sonin-even64-rational-source.json').write_text(json.dumps(frozen,indent=2)+'\n')

L=F(17,16); O=256
norm=sum(c*c*2*L/(2*n+1) for n,c in zip(orders,coeff))
derivatives=[]
for k in range(127):
    derivatives.append(sum(c*F(factorial(n+k),2**k*factorial(k)*factorial(n-k))
                           for n,c in zip(orders,coeff) if n>=k)/L**k)
series=[[(k+1,(-1)**(k//2)*derivatives[k]) for k in range(parity,127,2)]
        for parity in (0,1)]
convolution={}
for a in series:
    for m,cm in a:
        for n,cn in a:
            convolution[m+n]=convolution.get(m+n,F(0))+cm*cn
integrals=[sum(cm*F(1,O**(m+q-1)*(m+q-1)) for m,cm in convolution.items())
           for q in range(3)]
log_extra=sum(cm*F(1,O**(m-1)*(m-1)**2) for m,cm in convolution.items())
assert all(x>=0 for x in integrals) and log_extra>=0

def atan_bounds(x,N=160):
    a=sum((-1)**k*x**(2*k+1)/(2*k+1) for k in range(N))
    return a,a+x**(2*N+1)/(2*N+1)
def dyadic_bounds(lo,hi,bits=256):
    unit=2**bits
    return F((lo.numerator*unit)//lo.denominator,unit),F(-((-hi.numerator*unit)//hi.denominator),unit)
al,ah=atan_bounds(F(1,5)); bl,bh=atan_bounds(F(1,239))
pi_lo,pi_hi=dyadic_bounds(16*al-4*bh,16*ah-4*bl)
assert F(3)<pi_lo<pi_hi<F(4)
def log_rational_bounds(x,N=160):
    k=0
    while x>=2:
        x/=2;k+=1
    assert 1<=x<2
    def part(z):
        lo=2*sum(z**(2*j+1)/(2*j+1) for j in range(N))
        return lo,lo+2*z**(2*N+1)/((2*N+1)*(1-z*z))
    l2,h2=part(F(1,3)); l,h=part((x-1)/(x+1))
    return dyadic_bounds(l+k*l2,h+k*h2)
_,log_hi=log_rational_bounds(F(O,2)/pi_lo)
tail_upper=8/pi_lo*((log_hi-F(7,2))*integrals[0]+log_extra
                    +integrals[1]/15+F(25,8)*integrals[2])
assert tail_upper>=0

packet=(BASE/'tmp/c009-liu/fresh-b-20261014/certificates/source-matrices.json').read_bytes()
assert hashlib.sha256(packet).hexdigest()==results['input_hashes']['source-matrices.json']
mat=json.loads(packet)['matrices']
raw={name:{(i,j):F(int(lo)+int(hi),2**257) for i,j,lo,hi in mat[name]}
     for name in ('A','J0')}
head=F(0)
for ni,ci in zip(orders,coeff):
    for nj,cj in zip(orders,coeff):
        key=min(ni,nj),max(ni,nj)
        head+=ci*cj*(raw['A'][key]+raw['J0'][key])
head_error=F(1,2**204)+F(2,2**220)
upper=head/norm+head_error+tail_upper/norm
def display(q):
    return mp.nstr(mp.mpf(q.numerator)/q.denominator,65)
outward_hi=dyadic_bounds(upper,upper,bits=256)[1]
assert outward_hi<F(7,10**35)
out={
    'kind':'exact-rational-geometric-upper-budget',
    'source':'sonin-even64-rational-source.json','norm':display(norm),
    'band_plus_prime_plus_pole_rayleigh_midpoint':display(head/norm),
    'paid_head_operator_error':display(head_error),
    'gamma_tail_upper_normalized':display(tail_upper/norm),
    'actual_Q_rayleigh_upper':display(outward_hi),
    'actual_Q_upper_dyadic':{'numerator':str(outward_hi.numerator),'denominator':str(outward_hi.denominator)},
    'readable_strict_upper':'7e-35',
    'tail_integrals':[display(x/norm) for x in integrals],
    'tail_log_extra_integral':display(log_extra/norm),
    'constants':{'pi_lo':str(pi_lo),'pi_hi':str(pi_hi),'log_upper':str(log_hi)},
    'tail_source': 'A(t)-7/2 <= log(t/(2pi))+1/(15t)+25/(8t^2), t>=256',
    'fourier_bound':'|F(t)|^2<=8(S(t)^2+C(t)^2); exact finite endpoint derivative series',
    'source_error_paid':True,'unbounded_gamma_tail_retained':True,'RH_or_zero_data_used':False,
}
(HERE/'sonin-even64-geometric-upper.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['band_plus_prime_plus_pole_rayleigh_midpoint',
    'gamma_tail_upper_normalized','actual_Q_rayleigh_upper']}),flush=True)

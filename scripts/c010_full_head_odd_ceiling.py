"""Own original-head odd proposal and exact source-error ceiling. No zero data."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import time
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reviews/2026-10-14/c010-inertia'
INPUT=ROOT/'tmp/c009-liu/fresh-b-20261014/certificates'
mp.mp.dps=80
EXPECTED={'source-matrices.json':'4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac',
          'tail-columns.json':'2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2'}
packets={}
for name,sha in EXPECTED.items():
    raw=(INPUT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha
    packets[name]=json.loads(raw)
data=packets['source-matrices.json']; tail=packets['tail-columns.json']
mat={name:{(i,j):F(int(lo)+int(hi),2**257) for i,j,lo,hi in data['matrices'][name]}
     for name in ('A','J0')}
cols={(row['column'],row['index']):F(int(row['lo'])+int(row['hi']),2**641)
      for row in tail['entries']}
ids=list(range(1,448,2)); dim=224; L=F(17,16)
gamma=lambda n:2*L/(2*n+1)
asmp=lambda q:mp.mpf(q.numerator)/q.denominator
R=mp.matrix(dim)
for i,ni in enumerate(ids):
    for j,nj in enumerate(ids):
        k=min(ni,nj),max(ni,nj)
        raw=mat['A'][k]+mat['J0'][k]+F(648,17)*(cols[0,ni]*cols[0,nj]+cols[1,ni]*cols[1,nj])
        R[i,j]=asmp(raw)/mp.sqrt(asmp(gamma(ni)*gamma(nj)))
print(json.dumps({'stage':'original224_odd_head_assembled','dps':80}),flush=True)
old=json.loads((OUT/'sonin-source-reconstruction.json').read_text())
seed=next(r for r in old['results'] if r['size_per_sector']==64 and r['parity']==1)
v=mp.matrix([mp.mpf(x) for x in seed['eigenvector_orthonormal']]+[mp.mpf(0)]*160)
tick=time.monotonic()
factor=mp.cholesky(R)
print(json.dumps({'stage':'proposal_cholesky_completed','seconds':time.monotonic()-tick}),flush=True)
def solve(v):
    y=mp.matrix(dim,1);x=mp.matrix(dim,1)
    for i in range(dim):
        y[i]=(v[i]-mp.fsum(factor[i,j]*y[j] for j in range(i)))/factor[i,i]
    for i in range(dim-1,-1,-1):
        x[i]=(y[i]-mp.fsum(factor[j,i]*x[j] for j in range(i+1,dim)))/factor[i,i]
    return x
iterations=[]
for j in range(8):
    v=solve(v);v/=mp.norm(v)
    ray=mp.fdot(v,R*v)
    iterations.append(mp.nstr(ray,65))
    print(json.dumps({'stage':'inverse_iteration','iteration':j+1,'ordinary_rayleigh':iterations[-1]}),flush=True)
coeff=[F(mp.nstr(v[i]/mp.sqrt(asmp(gamma(n))),50)) for i,n in enumerate(ids)]
witness={'kind':'exact-rational-original-whole-head-odd-source','orders':ids,
         'raw_coefficients':[str(x) for x in coeff],'half_window':'17/16','zero_extension':True,
         'proposal_dps':80,'iterations':iterations,'source_hashes':EXPECTED}
(OUT/'full-head-odd-source.json').write_text(json.dumps(witness,indent=2)+'\n')
norm=sum(c*c*gamma(n) for n,c in zip(ids,coeff))
head=F(0)
for i,ni in enumerate(ids):
    for j in range(i,dim):
        nj=ids[j];k=ni,nj
        head+=(1 if i==j else 2)*coeff[i]*coeff[j]*(mat['A'][k]+mat['J0'][k])
u=F(648,17)*sum(sum(c*cols[column,n] for n,c in zip(ids,coeff))**2 for column in (0,1))
eps=F(1,2**204)+F(2,2**220)+F(9,2**512)
ceiling=(head+u)/norm+eps
even=F(7954159549289785371664718615168914673915149,2**256)
shift=F(1,10**34)
tau=F(1,2**49162)
bits=256;unit=2**bits
ceiling_hi=F(-((-ceiling.numerator*unit)//ceiling.denominator),unit)
result={'kind':'paid-exact-rational-original-R-odd-ceiling','head_dimension':224,
        'source':'full-head-odd-source.json','norm_decimal':mp.nstr(asmp(norm),65),
        'midpoint_rayleigh_decimal':mp.nstr(asmp((head+u)/norm),65),
        'epsilonR_decimal':mp.nstr(asmp(eps),65),
        'ceiling_decimal':mp.nstr(asmp(ceiling_hi),65),
        'ceiling_dyadic':{'numerator':str(ceiling_hi.numerator),'denominator':str(ceiling_hi.denominator)},
        'ceiling_below_even_upper':ceiling_hi<even,
        'ceiling_plus_tau_below_even_upper':ceiling_hi+tau<even,
        'ceiling_below_shift_1e_minus34':ceiling_hi<shift,
        'exact_margin_to_even_upper':{'numerator':str((even-ceiling_hi).numerator),
                                      'denominator':str((even-ceiling_hi).denominator)},
        'scope':'Only fixedR supplier ceiling; not an actual Q upper or negative Q test',
        'input_hashes':EXPECTED,'proposal_precision_digits':80,'wall_seconds':time.monotonic()-tick}
(OUT/'full-head-odd-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['ceiling_decimal','ceiling_below_even_upper',
    'ceiling_plus_tau_below_even_upper','ceiling_below_shift_1e_minus34','wall_seconds']}),flush=True)

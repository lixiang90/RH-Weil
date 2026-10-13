"""Own exact shifted compilation and whole-row Gram proposals/checks."""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import hashlib
import json
import time
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reviews/2026-10-14/c010-inertia'
INPUT=ROOT/'tmp/c009-liu/fresh-b-20261014/certificates'
mp.mp.dps=80
N=224;BITS=512;GUARD=1<<372;W_BITS=192;RANK_COEFFICIENT=1<<23
tick=time.monotonic()
def read(name):
    raw=(INPUT/name).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def emit(value): print(json.dumps(value),flush=True)
def transpose(a): return [list(x) for x in zip(*a)]
def product(a,b):
    cols=transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in cols] for row in a]
def symmetric(a): return all(a[i][j]==a[j][i] for i in range(N) for j in range(i))
def asmp(q): return mp.mpf(q.numerator)/q.denominator
def write(name,value):
    raw=(json.dumps(value,separators=(',',':'))+'\n').encode()
    (OUT/name).write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()
source,source_sha=read('source-matrices.json')
assert source_sha=='4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac'
raw={name:{(i,j):int(lo)+int(hi) for i,j,lo,hi in source['matrices'][name]}
     for name in ('A','B')}
m=F(9617,10400);b=F(63183,10400);t=F(1,10**34)
r=F(1,2**95);p=F(1,2**440)
e=1389*r+p;n=896*r*r+p;h=11696*r*r+p;theta=F(1,2**48)
def ab(m): return e*theta+2*e*e/(m-n),(e/theta+n)/(m*m)+2*h*h/(m*m*(m-n))
alpha,beta=ab(m);alpha_t,beta_t=ab(m-t)
da=alpha_t-alpha;db=beta_t-beta
epsA=F(1,2**220);epsB=epsA;epsD=epsB+(2*b+epsA)*epsA
S0=2**257;Cw=29*2**769;T0=17*29*607630911*2**1282
d=9617*(9617*2**435-325*(896*2**250+1))
scalars=[t/m*d*289*Cw*T0,d*17*T0*(da+db*epsD),d*T0*db/S0,d*T0*db/(17*S0*S0)]
assert d>0 and 0<t<m-n and da>0 and db>0
assert scalars[2]==17*S0*scalars[3]
den=lcm(*(x.denominator for x in scalars))
scalar_int=[x.numerator*(den//x.denominator) for x in scalars]
assert all(F(v,den)==x for v,x in zip(scalar_int,scalars))
ci,cd,cb,ca=scalar_int
summary={'kind':'new-exact-shifted-inertia-sign-gate','t':str(t),'s':str(t),
         'common_denominator':str(den),'denominator_bits':den.bit_length(),
         'scalar_denominator_bits':[x.denominator.bit_length() for x in scalars],
         'proposal_dps':80,'sectors':[],'source_matrix_sha256':source_sha}
emit({'stage':'exact_shift_scalars','denominator_bits':summary['denominator_bits']})

for sector in (1,0):
    ids=list(range(sector,448,2));q=[8*(2*j+1) for j in ids]
    cong,cong_sha=read(f'sector-{sector}-congruence.json')
    old,old_sha=read(f'sector-{sector}-target.json')
    V=cong['V'];K0=old['matrix']
    assert old['indices']==ids and old['sector']==sector and symmetric(V) and symmetric(K0)
    assert all(V[i][j]%q[j]==0 for i in range(N) for j in range(N))
    Y=[[V[i][j]//q[j] for j in range(N)] for i in range(N)]
    a=[[raw['A'][min(i,j),max(i,j)] for j in ids] for i in ids]
    braw=[[raw['B'][min(i,j),max(i,j)] for j in ids] for i in ids]
    aqa=product([[a[i][j]*q[j] for j in range(N)] for i in range(N)],a)
    f=[[aqa[i][j]-17*S0*braw[i][j] for j in range(N)] for i in range(N)]
    middle=[[ca*q[i]*f[i][j]*q[j]-(cd*q[i] if i==j else 0)
             for j in range(N)] for i in range(N)]
    correction=product(product(Y,middle),transpose(Y))
    K=[[den*K0[i][j]-ci*V[i][j]+correction[i][j] for j in range(N)] for i in range(N)]
    assert symmetric(K)
    bitB=max(abs(x).bit_length() for row in K for x in row)
    lower=[[(K[i][j]*(1<<BITS))//(1<<bitB)-(N if i==j else 0)
            for j in range(N)] for i in range(N)]
    assert symmetric(lower)
    # Check exact floor mapping and all entry-rounding bounds, not float truncation.
    assert all(0<=K[i][j]*(1<<BITS)-(lower[i][j]+(N if i==j else 0))*(1<<bitB)<1<<bitB
               for i in range(N) for j in range(N))
    emit({'stage':'shifted_target_compiled','sector':sector,'bitB':bitB,'elapsed':time.monotonic()-tick})
    rank=None
    mat=mp.matrix([[mp.mpf(x)/(1<<BITS) for x in row] for row in lower])
    if sector==0:
        # Only a direction proposal. Its precision/normalization is not a sign premise.
        perm,lo,up=mp.lu(mat)
        v=mp.matrix([1]+[0]*(N-1))
        for _ in range(8):
            pv=perm*v;y=mp.matrix(N,1);x=mp.matrix(N,1)
            for i in range(N):
                y[i]=(pv[i]-mp.fsum(lo[i,j]*y[j] for j in range(i)))/lo[i,i]
            for i in range(N-1,-1,-1):
                x[i]=(y[i]-mp.fsum(up[i,j]*x[j] for j in range(i+1,N)))/up[i,i]
            v=x/mp.norm(x)
        w=[int(mp.nint(v[i]*(1<<W_BITS))) for i in range(N)]
        rank={'coefficient':RANK_COEFFICIENT,'vector':w}
        ordinary=mp.fdot(v,mat*v)
        emit({'stage':'even_rank_proposal','ordinary_rayleigh':mp.nstr(ordinary,55)})
    target=[[lower[i][j]+(RANK_COEFFICIENT*rank['vector'][i]*rank['vector'][j] if rank else 0)
             for j in range(N)] for i in range(N)]
    packet={'sector':sector,'indices':ids,'bits':BITS,'guard':GUARD,'matrix':lower,'rank_one':rank}
    target_sha=write(f'shifted-sector-{sector}-target.json',packet)
    receipt={'sector':sector,'source_matrix_sha256':source_sha,'congruence_sha256':cong_sha,
             'original_target_sha256':old_sha,'common_denominator':str(den),'integer_bitB':bitB,
             'positive_actual_scale':'common_denominator / 2^integer_bitB multiplying Kt',
             'lower_target_error':'each symmetric floor error<2^-512;224I pays full Loewner norm',
             'target_sha256':target_sha,'rank_one_bits':W_BITS if rank else None,
             'rank_one_rho':'2^-105' if rank else None}
    shifted=mp.matrix([[mp.mpf(target[i][j]-(GUARD if i==j else 0))/(1<<BITS)
                       for j in range(N)] for i in range(N)])
    try:
        factor=mp.cholesky(shifted)
    except Exception as ex:
        receipt.update(status='PROPOSAL_CHOLESKY_FAILED',reason=repr(ex))
        write(f'shifted-sector-{sector}-compile-receipt.json',receipt)
        summary['sectors'].append(receipt)
        emit({'stage':'proposal_failed','sector':sector,'reason':repr(ex)})
        continue
    ints=[[int(mp.floor(factor[i,j]*(1<<256))) if j<=i else 0 for j in range(N)] for i in range(N)]
    gram_sha=write(f'shifted-sector-{sector}-gram.json',{'sector':sector,'factor':ints})
    row_sums=[]
    for i in range(N):
        row_sums.append(sum(abs(target[i][j]-sum(ints[i][k]*ints[j][k] for k in range(min(i,j)+1))
                                -(GUARD if i==j else 0)) for j in range(N)))
    passed=max(row_sums)<GUARD
    receipt.update(status='EXACT_ALL_ROWS_PASS' if passed else 'EXACT_RESIDUAL_FAILED',
                   gram_sha256=gram_sha,checked_rows=N,guard=GUARD,
                   maximum_row_residual=max(row_sums),maximum_residual_bits=max(row_sums).bit_length(),
                   row_sums=row_sums)
    write(f'shifted-sector-{sector}-compile-receipt.json',receipt)
    summary['sectors'].append({k:v for k,v in receipt.items() if k!='row_sums'})
    emit({'stage':receipt['status'],'sector':sector,'residual_bits':receipt['maximum_residual_bits'],
          'guard_bits':GUARD.bit_length(),'elapsed':time.monotonic()-tick})
summary['all_pass']=all(x['status']=='EXACT_ALL_ROWS_PASS' for x in summary['sectors'])
summary['wall_seconds']=time.monotonic()-tick
write('shifted-inertia-result.json',summary)
emit({'stage':'complete','all_pass':summary['all_pass'],'wall_seconds':summary['wall_seconds']})

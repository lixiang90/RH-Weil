"""Exact scalar and local coefficient checks. This is NOT an arithmetic mixed moment proof."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json
if not __debug__:
    raise RuntimeError('optimized Python would disable checks')
checks=[]
def check(name,ok,detail=None):
    if not ok: raise AssertionError(name)
    checks.append(dict(name=name,passed=True,detail=detail))
alpha=F(5,6);delta=F(19429,50000);B0=F(17499,20000)
kappa=2*B0-1;c=1/(3*kappa);D=F(5,2)-c;P=1-c/2
J=(alpha-delta)*D+delta*P
t=1+delta*P/(2*J)
r=((2-c)*t-(1-c)/2)/D
m=t-r
z=(1-2*m)/(6*kappa)
R=1-delta+(alpha-delta)*(t-1)
check('common feedback kappa',kappa==F(7499,10000))
check('actual detector parameter range',F(1,50)<delta<F(3,4) and F(37,50)<kappa<F(3,4))
check('short plain capacity saturated before strict decrement',2*m+6*kappa*z==1)
check('physical selected product spike',2*delta*m+delta*z==1-R)
check('sixth inverse moment reference',R+delta*t==(1+5*t)/6)
check('raw-to-amplified mixed exponent identity',1+delta*t+(t-1)/6==t+1-R)
check('long differs from short inverse',t>1 and F(3,5)<r<1)
check('plain length range',F(1,3)<m<F(1,2))
check('positive selected capacity',0<z<F(1,5))
raw_goal=t+1-R
full_length=t+2*m+z
check('mixed product beyond raw row range',full_length>t)
check('sixth free class count exponent',F(1,3)+F(2,3)==1)
# Exact local formal polynomial identities. x includes the natural prime phase.
# Deleted local coefficients are [1,0,...]; restore squarefree inverse by 1-x,
# and each plain polynomial by 1+x+... . This works after specializing x=0 too.
for max_degree in range(1,19):
    inverse=[F(1),F(-1)]+[F(0)]*(max_degree-1)
    plain=[F(1)]*(max_degree+1)
    deleted=[F(1)]+[F(0)]*max_degree
    def conv(a,b):
        return [sum((a[j]*b[n-j] for j in range(n+1)
                     if j<len(a) and n-j<len(b)),F(0)) for n in range(max_degree+1)]
    check('inverse restoration degree '+str(max_degree),conv(inverse,deleted)==inverse[:max_degree+1])
    check('plain restoration degree '+str(max_degree),conv(plain,deleted)==plain)
    check('inverse/plain exact Euler cancellation degree '+str(max_degree),
          conv(inverse,plain)==deleted)
# Fixed alpha and sixth-power map budget. Eta is a genuine strict width cost.
eta=F(1,1000000)
lam=F(1,20000)  # a proposed raw saving, NOT obtained
chi=lam-F(5,6)*eta
check('strict raw inverse margin',t+eta>t)
check('amplification consumes five-sixths of width slack',
      (1+5*(t+eta))/6+(1-R)-lam==1+delta*t-chi)
gap=R-F(2,3)
weighted=F(52361,1500000000)
necessary=gap+weighted
check('known count gap exact',gap==F(1875081893,615723531225000))
check('hypothetical net saving beats necessary target',chi>necessary)
check('same-class raw block is below target with positive exponent gap',1-R-lam>0)
check('existing marked input needs extra width',t+2*z>t+eta)
# Marker-slot gain and width cost have positive net slope at x=1/2.
check('existing inverse+Q amplification cannot alone save',
      F(5,3)-delta>0)

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'output/hybrid-mixed-sixth-restoration-budget.json'
SOURCE_SHA='42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check',action='store_true')
parser.add_argument('--source',type=Path)
args=parser.parse_args()
source_matched=False
if args.source is not None:
    raw=args.source.read_bytes().replace(b'\r\n',b'\n')
    assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA
    source_matched=True
vals=dict(target=B0,kappa=kappa,delta=delta,tLong=t,rShort=r,mShort=m,zSelected=z,
          R=R,mixed_spike=delta*t+2*delta*m+delta*z,mixed_reference=1+delta*t,
          convolution_length=full_length,raw_target_without_new_saving=raw_goal,
          raw_goal_below_generic_length=full_length-raw_goal,
          necessary_count_decrement=necessary,proposed_raw_saving=lam,
          strict_width_slack=eta,conditional_net_saving=chi,
          conditional_slack_over_necessary=chi-necessary)
canonical=Path(__file__).read_bytes().replace(b'\r\n',b'\n').replace(b'\r',b'\n')
result=dict(schema='rh-weil-mixed-sixth-restoration-budget-v1',
            scope='finite exact scalar/local algebra only; no arithmetic cross estimate or full detector count proved',
            script_canonical_lf_sha256=hashlib.sha256(canonical).hexdigest(),
            frozen_source_canonical_lf_sha256=SOURCE_SHA,
            source_description='math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex',
            values={n:dict(exact=str(x),orientation=float(x)) for n,x in vals.items()},
            checks=checks,attained_new_count_saving=False,
            attained_new_zero_free_region=False,lean_checked=False,
            simultaneous_witness_for_all_detector_rows_proved=False)
if args.check:
    assert json.loads(OUTPUT.read_text(encoding='utf8'))==result
else:
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print(json.dumps(dict(passed=True,checks=len(checks),source_matched=source_matched,
                     result=str(OUTPUT),scope=result['scope'])))

"""Read ONLY previously consumed public metadata; exact scalar old-fee recovery.

No source coordinates, matrix/Gram/inverse calculation, or scientific rerun.
The operator meaning of these reported scalars is a separate root premise.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
PINS={
 'reviews/2026-10-31/retained-tail-center-admission/center-certificate-result.json':'3eb9e77d71f92ead44775bfbafb7499a7ff0fd2e5bc81ac00095332a4f912739',
 'reviews/2026-10-29/weil-9-8-admission/source-stage-verification.json':'dbb31208d0568feac7c9adff27722d5b55d08381002d23e0a4e35f150b1472c1',
 'reviews/2026-10-29/weil-9-8-admission/full-weil-analytic-transfer-fresh.md':'0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466',
 'reviews/2026-11-01/retained-tail-signed-head/head-result.json':'ba31ccef92293cdc1f308ea05bdd507b5d2fb4695cbfab6c341aa74718d4ea4e',
}
data={}
for p,h in PINS.items():
    raw=(ROOT/p).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==h
    if p.endswith('.json'):data[p]=json.loads(raw)
center=data[next(iter(PINS))]
assert center['status']=='CENTER_ONLY_FULL_H_SOURCE_VERIFIED_PENDING_ROOT'
ledger=center['globalSourceErrorLedger']
fraction=lambda q:F(*map(int,q))
qerr=fraction(ledger['independentQBound'])
band=fraction(ledger['acceptedOldGlobalBandBound'])
rho2=fraction(center['finiteVNativeError']['independentFullNativeHSSquared'])
pow2=lambda n:F(1,1<<n)
assert qerr<pow2(227) and band<pow2(265) and rho2<pow2(478)
analytic=qerr+band+9*pow2(512)+pow2(600)
eps=pow2(226)
assert analytic+pow2(239)<eps
assert 22*analytic+pow2(239)<pow2(221)
stage=data['reviews/2026-10-29/weil-9-8-admission/source-stage-verification.json']
mat=next(x for x in stage['stages'] if x['stage']=='matrices')['receipt']
rows={}
for k in ('A','B','J0'):
    r=mat['matrixChecks'][k]
    assert r['checkedRows']==448 and r['status']=='PASS'
    assert int(r['maxWeightedWidthNumerator'])==2405760
    assert int(r['denominator'])==18*(1<<256)
    row=F(int(r['maxWeightedWidthNumerator']),int(r['denominator']))
    assert row<pow2(238)
    rows[k]=r
# A/B's already-paid primitive/rounding transport is in the cited proof.
# One extra bit leaves room even if the negligible primitive fee is added again.
epsA=epsB=epsJround=pow2(237)
epsC=epsA+epsJround+band+9*pow2(512)
b=F(433,64)
epsDh=epsB+(2*b+epsA)*epsA
assert epsC<pow2(235) and epsDh<pow2(233)
epsHead=epsC+3*eps
assert epsHead<pow2(224)
whole=(48+576/(1-eps))*eps
assert whole<pow2(216)
head=data['reviews/2026-11-01/retained-tail-signed-head/head-result.json']
assert head['status']=='POSITIVE_HEAD_ONLY'
assert all(x['lowerStatus']=='ALL_POSITIVE' and x['lowerPivot']==224 for x in head['sectors'])
# The old ROOT-consumed lower traces prove Chat>2^-201 I. No trace is rerun.
assert fraction(head['comparisonEps'])==pow2(201)
assert pow2(201)-epsHead>pow2(202)
# Proposed NEW integration tolerance; not claimed achieved by a supplier.
arith=pow2(256)
epsCX=4*eps+arith
epsZ=F(209,64)*eps+2*pow2(1008)+arith
joint=epsDh+2*epsZ+epsCX
assert joint<pow2(222)<pow2(221)
result={
 'status':'EXACT_SCALAR_OLD_FEE_RECOVERY_PASS_PENDING_ROOT_SCOPE',
 'method':'Read old reported exact Fractions only; no matrix/source/Gram/inverse rerun',
 'inputPins':PINS,'oldMatrixRowMetadata':rows,
 'bounds':{'bandOperatorPower':-265,'finiteNativeHSRoundingPower':-239,
           'VAndGOperatorPower':-226,'VFullHSPower':-221,
           'oldA_B_JroundConservativePower':-237,'C0SourcePower':-235,
           'DhSourcePower':-233,'CretCenterSourcePower':-224,
           'wholeUApproximationPower':-216,'oldImpliedCretLowerPower':-202},
 'prospectiveOnly':{'integrationArithmeticPower':-256,'jointGramEnvelopePower':-221,
                    'actualCX_ZValuesPaid':False},
 'oldIssued203_198_204_220_193BoundsRemainTrue':True,
 'newMathematicalIterations':0,'runtimeGoalCreatedAt':1793085111,
 'scope':'Root must consume the original operator/norm/domain and true-enclosure premises; status labels alone prove none of them',
}
out=HERE/'old-fee-recovery.json'
with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'status':result['status'],'bounds':result['bounds'],'output':str(out)}))

"""Exact bookkeeping for actual two-cutoff detector coverage. No new mixed upper estimate."""
import argparse
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
if not __debug__: raise RuntimeError('optimized mode disables no required checks')
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check',action='store_true')
parser.add_argument('--source',type=Path,help='optional fixed original TeX, checked by canonical SHA256')
parser.add_argument('--audit-output',type=Path)
args=parser.parse_args()
checks=[]
def ck(name,cond,detail=None):
    if not cond: raise AssertionError(name)
    checks.append({'name':name,'passed':True,'detail':detail})
alpha=F(5,6);delta=F(19429,50000);kappa=F(7499,10000);x=F(1,2);q=delta*x
c=1/(3*kappa);D=3-(1+2*c)*x;P=(2-2*c*x)*(1-x)
J=(alpha-delta)*D+delta*P
t0=1+delta*P/(2*J)
r0=((2-2*c*x)*t0-(1-c)*x)/D
m0=t0-r0
R=1-delta+(alpha-delta)*(t0-1)
A=alpha-delta;beta=delta*P/D;I=delta*(1-x);Cm=delta*(2-2*c*x)
gamma=F(1,20000)
sp=gamma/beta;sm=gamma/A;aa=gamma/A;rho=gamma/I
tp=t0+sp;tm=t0-sm;rCut=r0+rho;mMin=m0-sm-rho;rMin=t0-aa
def L(t): return 1-delta+A*(t-1)
def short(t): return 1-delta+beta*(F(3,2)-t)
def inv(r): return 1-delta*(x+(1-x)*r)
def zplain(m): return (1-2*m)/(6*kappa)
def phi(m): return 2*delta*m+2*q*zplain(m)
ck('dynamic feedback parameter',kappa==2*F(17499,20000)-1)
ck('t0 crosses actual long and short counts',L(t0)==short(t0)==R)
ck('r0 crosses actual inverse and plain counts',inv(r0)==1-phi(m0)==R)
ck('two legal detector cutoffs',1<tm<t0<tp<F(3,2))
ck('nontrivial long core range',1<rMin<tp)
ck('inverse cut has positive marked margin',F(3,5)<rCut<1)
ck('short core bounded below by positive length',F(1,3)<mMin<m0<F(1,2))
ck('upper cutoff short branch saves gamma',short(tp)==R-gamma)
ck('upper cutoff shorter long branch saves gamma',L(rMin)==R-gamma)
ck('lower cutoff marked inverse branch saves gamma',inv(rCut)==R-gamma)
ck('lower cutoff long branch saves gamma',L(tm)==R-gamma)
ck('joint core length lower support',tm-rCut==mMin)
ck('short plus selected Q spike affine',phi(m0)-phi(mMin)==Cm*(sm+rho))
tax=Cm*(sm+rho)
needed=gamma+tax
ck('conditional core count with mixed saving chi',
   1-phi(mMin)-needed==R-gamma)
ck('coverage multiplier exact',needed/gamma==F(8209647083,1500842361))
nuCap=F(1,10000)
ck('fixed inverse near-one cap',rCut<1-nuCap)
ck('near-one unmarked inverse handled at stronger exponent',
   1-delta+delta*nuCap<R-gamma)
ck('inverse selected capacity bounded by supply',
   (1-rCut)/2<F(1,5))
ck('plain core capacity bounded by supply',0<zplain(mMin)<F(1,5))
# Genuine strict marked margin after request zM-nu0.
nu0=F(1,1000000000)
zM=(1-rCut)/2-nu0
ck('strict marked first width',1-rCut-2*zM==2*nu0>0)
ck('strict marked second width',3-2*rCut-8*zM==8*nu0+2*rCut-1>0)
zP=zplain(mMin)-nu0
ck('strict plain capacity paid',1-2*mMin-6*kappa*zP==6*kappa*nu0>0)
eta=F(1,1000000);oldLam=F(1,20000);oldChi=oldLam-F(5,6)*eta
ck('old single-core numerical proposal insufficient',oldChi<needed)
maxOldUniformDecrement=oldChi/(needed/gamma)
minimumTarget=F(467366968772963,12314470624500000000)
ck('coverage tax blocks old proposal even with zero other losses',
   maxOldUniformDecrement<minimumTarget)
inputChi=F(3,10000);allLoss=F(1,100000)
ck('proposed new uniform mixed chi has positive core margin',
   inputChi>needed)
ck('hypothetical all-branch net decrement',gamma-allLoss==F(1,25000))
ck('hypothetical net decrement exceeds target necessary budget',
   gamma-allLoss>minimumTarget)
fixedRExtra=A*sp
rawFixedNeeded=needed+fixedRExtra+F(5,6)*eta
ck('raw fixed-R pays new upper long width',
   L(tp)-R==fixedRExtra)
# Full finite contract countermodel: one row, M_r^2=U^(delta*r),
# S_0^2=1, S_m^2=0 for every fixed positive m. Pair r=t,m=0
# satisfies all numerical detector lower/upper statements. It is not a
# Hecke family or coefficients model, and can be discarded by the partition.
for r in [F(0),F(1,2),F(1),tm,t0,tp,F(3,2)]:
    e=max(F(1),(1+5*r)/6)
    ck('one-row scalar inverse marginal exponent '+str(r),delta*r<=e)
ck('toy target short witness absent',m0>0)
def rcrit(t):
    return ((2-2*c*x)*t-(1-c)*x)/D
def mcrit(t):
    return t-rcrit(t)
rder=(2-2*c*x)/D
mder=(1-x)/D
ck('crossing r slope exact',rcrit(tp)-rcrit(tm)==rder*(tp-tm))
ck('crossing m slope exact',mcrit(tp)-mcrit(tm)==mder*(tp-tm))
ck('two crossing derivatives sum one',rder+mder==1)
ck('short count slope equals inverse slope times crossing slope',beta==I*rder)
rhoAtLower=(gamma+beta*sm)/I
ck('moving crossing requires additional inverse cutoff offset',
   rCut==rcrit(tm)+rhoAtLower)
ck('apparently smaller m derivative is paid back exactly',
   mMin==mcrit(tm)-rhoAtLower and m0-mMin==mder*sm+rhoAtLower==sm+rho)
ck('endpoint half amplitude m derivative',mder==1/(5-2*c))
minimumVariableRaw=minimumTarget*(needed/gamma)
minimumCentralRaw=minimumTarget*(needed/gamma+A/beta)
ck('coverage-aware raw requirement exceeds old single label proposal',
   minimumVariableRaw>oldLam)
ck('central reference stronger than variable long reference',
   minimumCentralRaw>minimumVariableRaw)
mCut=m0+gamma/Cm
nuPlain=F(1,10000)
ck('large actual short length covered by existing plain count',
   1-phi(mCut)==R-gamma)
ck('mCut leaves fixed positive plain capacity',mCut<F(1,2)-nuPlain)
ck('near-half and beyond-half covered by unmarked plain',
   1-delta+2*delta*nuPlain<R-gamma)
ck('actual remaining short range narrow and positive',
   F(1,3)<mMin<mCut<F(1,2))
ck('core minimum requested selected capacity positive',
   0<zplain(mCut)<zplain(mMin)<F(1,5))
sha='42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3'
if args.source is not None:
    b=args.source.read_bytes().replace(bytes([13,10]),bytes([10]))
    ck('frozen source identity',hashlib.sha256(b).hexdigest()==sha)
vals=dict(delta=delta,kappa=kappa,x=x,t0=t0,r0=r0,m0=m0,R=R,gamma=gamma,
          short_count_slope=beta,long_count_slope=A,inverse_count_slope=I,
          sPlus=sp,sMinus=sm,aLong=aa,rhoInverse=rho,tPlus=tp,tMinus=tm,
          rLongMinimum=rMin,rInverseCut=rCut,mPlainMinimum=mMin,
          zPlainMaximum=zplain(mMin),coverageTax=tax,
          requiredMixedChiBeforeOtherLosses=needed,coverageMultiplier=needed/gamma,
          oldConditionalMixedChi=oldChi,oldMaxOverallSaving=maxOldUniformDecrement,
          targetNecessaryCountSaving=minimumTarget,
          proposedUniformMixedChi_NOT_PROVED=inputChi,allLossReserve=allLoss,
          requiredRawLambdaForVariableLongThreshold=needed+F(5,6)*eta,
          extraRawSavingForCentralRThreshold=fixedRExtra,
          requiredRawLambdaForCentralRThreshold=rawFixedNeeded,
          mCritDerivative=mder,rCritDerivative=rder,rhoRelativeToLowerCrossing=rhoAtLower,
          limitingNecessaryRawLambdaForVariableLongThreshold=minimumVariableRaw,
          limitingNecessaryRawLambdaForCentralRThreshold=minimumCentralRaw,
          mPlainCut=mCut,zPlainMinimum=zplain(mCut))
result={'scope':'exact coverage budget only; source-relative actual partition proof in companion report',
        'source_canonical_lf_sha256':sha,
        'values':{k:{'exact':str(v),'orientation':float(v)} for k,v in vals.items()},
        'checks':checks,'new_mixed_upper_estimate':False,'new_count_saving':False,
        'new_zero_free_region':False,'lean_checked':False}
result['source_matched']=args.source is not None
if args.audit_output is not None:
    args.audit_output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'passed':True,'checks':len(checks),'source_matched':args.source is not None,'new_count_saving':False,'new_zero_free_region':False}))

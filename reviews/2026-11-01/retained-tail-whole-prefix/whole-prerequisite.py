"""NEW fixed WHOLE-candidate prerequisite, CODE PREPARATION ONLY.

Standalone stdlib. No import/invocation/modification of an old driver/result.
No run without a NEW C068 whole-prefix freeze and independent ROOT execution gate.
Hpre=Chat-(2^-122+2^-224+2^-216)I. One P1024 LDL per parity, even then odd.
Globally ONE midpoint-L point proposal, final EXACT qpre=qK-lambda*physicalnorm.
This is NOT qK+old-source-eps and not an actual negative Cret/Lret/Q test.
No CX/Z/inverse/Gram production, lower/upper retry, or automatic Stage2 dispatch.
Normal stored arithmetic integers are limited to16384 bits. On overflow ONLY,
a signed-hex diagnostic may preserve up to65536 bits; it is not arithmetic data.

Future freeze: RH_WEIL_WHOLE_PREFIX_FREEZE_V1,
authorization ROOT_EXPLICIT_C068_WHOLE_PREFIX_EXECUTION, contractId C068,
runtimeGoalCreatedAt1793085111, codeSHA256, parameters=PARAMETERS,
sourceMathPins=PINS, stagedBudget=STAGED_BUDGET, targetId=TARGET_ID,
protocolPin, protocolDesignPin, executionGatePin, contractPin,
chargedMetadataPins, reviewPins>=2. Root execution
gate has its own distinct schema/true authorization; current preparation/spec
false numerical flags cannot authorize this main. See validate_freeze.

Preparation: AST/static ONLY; do not import/main/evaluate actual source arrays.
"""
from __future__ import annotations
import time
PROCESS_STARTED=time.monotonic()
PROCESS_STARTED_WALL=time.time()
STARTUP_RESERVE_SECONDS=1.0
CHARGED_EXTERNAL_BYTES=0
import argparse
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SELF=Path(__file__).resolve()
OUTER=ROOT/"literature/local/2026-11-01-retained-tail-whole-candidate/run-01"
OUT=OUTER/"stage-01-prefix"
LOCK=OUTER/"run-lock.json"
P,N,n=1024,448,224
UNIT=1 << P
LAMBDA=F(1,1 << 122)+F(1,1 << 224)+F(1,1 << 216)
SECONDS,BYTES,MAX_BITS=600,4*(1 << 20),16384
DIAGNOSTIC_BITS=65536
TARGET_ID="RH_WEIL_FIXED_9_8_COVARIANCE_JOINT_GRAM_T_WHOLE_V1"
CURRENT_STAGE="stage-01-prefix"
PARAMETERS=dict(L="9/8",N=N,sectorDimension=n,eta=1,omega=256,intervalBits=P,
    lambdaPowers=[122,224,216],capSeconds=SECONDS,capBytes=BYTES,
    maxStoredIntegerBits=MAX_BITS,sectorOrder=["even","odd"],ldlPassesPerSector=1,
    ordinarySectorUnresolvedPolicy="continue_other_prescheduled_sector_with_same_budget",
    maxWitnessProposals=1,witnessBits=P,
    witnessTieRule="nearest_ties_toward_positive_infinity",inverseComputed=False,
    exactMatmulsPerSector=3,autoStage2Dispatch=False)
STAGED_BUDGET=dict(aggregateCapSeconds=7200,stageCapSeconds=[600,3000,3600],
    stageCapBytes=[4*(1 << 20),48*(1 << 20),12*(1 << 20)],laterStagesAuthorized=False)
OLD="literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/"
CENTER="reviews/2026-10-31/retained-tail-center-admission/"
WHOLE="reviews/2026-11-01/retained-tail-whole-admission/"
PREFIX="reviews/2026-11-01/retained-tail-whole-prefix/"
MATRIX=OLD+"source-matrices.json"
TAIL=OLD+"tail-columns.json"
GCOLS="literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl"
CERT="literature/local/2026-10-31-retained-tail-center-certificate/run-01/result.json"
# Fresh source/math authority set for THIS WHOLE candidate. No old driver's PINS.
PINS={
 MATRIX:"a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
 TAIL:"d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
 GCOLS:"d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080",
 CERT:"3eb9e77d71f92ead44775bfbafb7499a7ff0fd2e5bc81ac00095332a4f912739",
 CENTER+"root-consumption-scope.json":"6e0df0fed60465622f8b95551e4e361203a8de9b199bf167c38709caf4caaac3",
 "reviews/2026-10-29/weil-9-8-admission/source-stage-verification.json":"dbb31208d0568feac7c9adff27722d5b55d08381002d23e0a4e35f150b1472c1",
 "reviews/2026-10-29/weil-9-8-admission/full-weil-analytic-transfer-fresh.md":"0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466",
 WHOLE+"selected-whole-certificate.md":"0328afa478fce4f73873776dc22e702f849233468f3afad09fc2d078a0a98ea7",
 WHOLE+"candidate-preparation.json":"d9eb014c9769a9f00eeb09b66aeb043a7ff7415fb495f15d63d4fa9abf6f6950",
 WHOLE+"root-consumed.md":"577685f4ea977ee686f9e6c09fa16527184e40b6f0933a28b0c7290a45d585ee",
 WHOLE+"root-consumption-scope.json":"07884950934555087e3a1efbdc9c0d529c302f852dfb47efd12e4344c93057de",
 WHOLE+"selected-target-fresh.md":"b37f3beea0eb6cbee29b2d57ee5dbf9444eb3ecf297ae6c42fb75703922b2519",
 WHOLE+"old-fee-recovery.json":"1b07b329e390089f34d86777ecbf6b257b40ab3636a7123fe08023317c98c344",
 WHOLE+"old-fee-recovery-fresh.md":"a77888cd710f41a7abba87687e2724de009dbc6500bce5eddac16b3771895fc1",
 WHOLE+"recover-paid-source-fees.py":"63e428ebeaeed3ffd3ed90d8ca54079e21d2efe2d9a1177853c8b62adc08682c",
 WHOLE+"next-code-preparation.md":"3ecd7b4753f540ee92034b14094d2f840d369c4825e7b40c4b764b3af208b3ed",
 PREFIX+"prefix-math-admission.md":"ce8e3d793881c2849aeb19abcaaa16d3d72de5d0870f86097dd5446d63dee984",
 "reviews/2026-11-01/retained-tail-signed-head/math-admission.md":"6547b2ff0e0b2a4deeeb88ae549930cb51d7a16b99a77c6053e9c30413e04c95",
 "goals/GOAL.20261027.md":"b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de",
 "goals/review-cadence.json":"712195abe82736fd5f8dbb79a7fec509f36fe3cf6222e8981adc9b286b8abdb9",
 "literature/manifest.json":"3223cffd0205b9a1f8660445ac33d0f3cec13b3bd1fa5e7799ed8abfb2746d42",
}

def need(ok,message):
    if not ok: raise ValueError(message)

def up(a,b):
    need(b>0,"POSITIVE_DENOMINATOR")
    return -((-a)//b)

def packed(v):
    return (json.dumps(v,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n").encode("ascii")

def sha(raw): return hashlib.sha256(raw).hexdigest()

def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,"DUPLICATE_JSON_KEY")
        d[k]=v
    return d

def decode(raw):
    return json.loads(raw,object_pairs_hook=unique,
        parse_constant=lambda _:need(False,"NONFINITE_JSON"))

def integer(v):
    need(type(v) is str,"INTEGER_STRING")
    a=int(v);need(str(a)==v,"CANONICAL_INTEGER")
    return a

def frac(q):
    q=F(q)
    try:numerator=checked(q.numerator)
    except IntegerWidthError as error:
        error.serializedPart="fraction-numerator"
        raise
    try:denominator=checked(q.denominator)
    except IntegerWidthError as error:
        error.serializedPart="fraction-denominator"
        raise
    return [str(numerator),str(denominator)]

def utc(): return datetime.now(timezone.utc).isoformat()

class IntegerWidthError(ValueError):
    def __init__(self,value):
        self.value=value
        self.actualBitLength=abs(value).bit_length()
        self.normalLimit=MAX_BITS
        self.serializedPart=None
        super().__init__("STORED_INTEGER_SIZE_STOP actualBitLength="+str(self.actualBitLength)
                         +" normalLimit="+str(self.normalLimit))

def checked(a):
    if abs(a).bit_length()>MAX_BITS:raise IntegerWidthError(a)
    return a

def integer_width_diagnostic(error):
    """Bounded exception evidence only; never clips/replaces an arithmetic value."""
    diagnostic=dict(actualBitLength=error.actualBitLength,normalLimitBits=error.normalLimit,
        diagnosticCapBits=DIAGNOSTIC_BITS,serializedPart=error.serializedPart,
        normalArithmeticDataUsable=False,mathematicalSignConclusion=False,
        technicalStopOnly=True)
    if error.actualBitLength<=DIAGNOSTIC_BITS:
        value=error.value
        diagnostic.update(encoding="FULL_SIGNED_HEXADECIMAL_DIAGNOSTIC_ONLY",
            signedHexValue=("-0x" if value<0 else "0x")+format(abs(value),"x"),
            fullDiagnosticValuePresent=True,valueOmitted=False)
    else:
        diagnostic.update(encoding="OMITTED_ABOVE_FIXED_DIAGNOSTIC_CAP",
            signedHexValue=None,fullDiagnosticValuePresent=False,valueOmitted=True,
            unconsumable=True,omissionReason="Value exceeds65536-bit diagnostic cap; no replacement or sign is asserted")
    return diagnostic

def hash_pins(pins,budget):
    result={}
    for name,expected in pins.items():
        budget.context=dict(operation="hash-input",path=name,bytes=0,expectedSHA256=expected)
        path=(ROOT/name).resolve();need(path.is_relative_to(ROOT) and path.is_file(),"PIN_PATH: "+name)
        h=hashlib.sha256();size=0
        with path.open("rb") as f:
            while block:=f.read(1 << 20):
                h.update(block);size+=len(block);budget.context["bytes"]=size;budget.check()
        budget.context["observedSHA256"]=h.hexdigest()
        need(h.hexdigest()==expected,"PIN_SHA: "+name)
        result[name]=dict(bytes=size,sha256=expected)
    return result

def read_json(name,budget):
    budget.context=dict(operation="read-json",path=name)
    raw=(ROOT/name).read_bytes();need(sha(raw)==PINS[name],"JSON_CHANGED_AT_USE: "+name)
    return decode(raw)

def load_centers(budget):
    cert=read_json(CERT,budget)
    need(cert["status"]=="CENTER_ONLY_FULL_H_SOURCE_VERIFIED_PENDING_ROOT"
        and cert["runtimeGoalCreatedAt"]==1793085111
        and cert["nativeGOperatorErrorPower"]==-203,"CENTER_CERTIFICATE_SCOPE")
    root=read_json(CENTER+"root-consumption-scope.json",budget)
    need(root["status"]=="ROOT_CONSUMED_SAME_FINAL_CENTER_FULL_H_SOURCE_NOT_OLD_BOX_TRUTH"
        and root["runtimeGoalCreatedAt"]==1793085111,"EXTERNAL_ROOT_SOURCE_AUTHORITY")
    packet=read_json(MATRIX,budget)["packet"];p=packet["parameters"]
    need(p["N"]==N and p["L"]=="9/8" and p["omega"]==256 and p["beta"]=="7/2"
        and p["outputBits"]==256,"OLD_SOURCE_PARAMETERS")
    need(packet["sourceConventions"]["J0"]=="L_squared_H"
        and packet["sourceConventions"]["orderedPrimePairs"]==225,"OLD_SOURCE_CONVENTIONS")
    mats={}
    for name in ("A","J0"):
        rows=packet["matrices"][name];need(len(rows)==50400,"OLD_MATRIX_SHAPE")
        a=[[0]*N for _ in range(N)];pos=0
        for i in range(N):
            for j in range(i,N,2):
                budget.context=dict(operation="parse-old-raw-center",matrix=name,row=pos,column=i,degree=j)
                row=rows[pos];need(type(row) is list and len(row)==4 and row[:2]==[i,j],"OLD_RAW_ORDER")
                lo,hi=integer(row[2]),integer(row[3]);need(lo<=hi,"OLD_RAW_ENDPOINT_ORDER")
                a[i][j]=a[j][i]=checked(lo+hi);pos+=1
            budget.check()
        mats[name]=a
    need(len(packet["matrices"]["B"])==50400,"UNUSED_B_WRAPPER_SHAPE")
    del packet
    t=read_json(TAIL,budget)["packet"];tp=t["parameters"]
    need(tp["dimension"]==N and tp["omega"]==256 and tp["LNumerator"]==9
        and tp["LDenominator"]==8 and tp["outputBits"]==640,"OLD_TAIL_PARAMETERS")
    need(len(t["entries"])==896,"OLD_TAIL_SHAPE")
    h=[[0]*N for _ in range(2)]
    for k,row in enumerate(t["entries"]):
        s,i=divmod(k,N);budget.context=dict(operation="parse-old-h-center",column=s,degree=i)
        need(row["column"]==s and row["index"]==i,"OLD_TAIL_ORDER")
        lo,hi,mid=(integer(row[x]) for x in ("lo","hi","midTwice"))
        need(lo<=hi and mid==lo+hi and (i%2==s or (lo,hi,mid)==(0,0,0)),"OLD_TAIL_PARITY_CENTER")
        h[s][i]=checked(mid)
    g=[[0]*N for _ in range(N)];hsh=hashlib.sha256();count=size=headcount=0
    with (ROOT/GCOLS).open("rb") as f:
        for j in range(N):
            for i in range(j%2,2047,2):
                budget.context=dict(operation="parse-NEW-G-from-SAME-V-stream",column=j,degree=i,
                                    streamRow=count+1,byteOffset=size)
                raw=f.readline(65537);need(raw and raw.endswith(b"\n") and len(raw)<=65536,"V_STREAM_LINE")
                hsh.update(raw);size+=len(raw);count+=1
                row=decode(raw);need(type(row) is list and len(row)==4 and row[:2]==[j,i],"V_STREAM_FULL_ORDER")
                lo,hi=integer(row[2]),integer(row[3]);need(lo<=hi,"V_STREAM_ENDPOINT_ORDER")
                if i<N:
                    mid=checked(lo+hi)
                    if i<j:need(g[i][j]==mid,"G_SAME_HEAD_CENTER_SYMMETRY")
                    g[j][i]=mid;headcount+=1
                if count%1024==0:budget.check()
            budget.check()
        need(f.read(1)==b"","V_STREAM_EXTRA")
    need(count==458528 and headcount==100352 and size==73598411 and hsh.hexdigest()==PINS[GCOLS],
         "V_STREAM_COMPLETE_SHA_SHAPE")
    return mats["A"],mats["J0"],h,g

def transpose(a):return list(map(list,zip(*a)))

def matmul(a,b,budget,label,sector):
    cols=transpose(b);out=[]
    for i,row in enumerate(a):
        budget.progress(label,sector=sector,row=i,rows=n)
        result=[]
        for j,col in enumerate(cols):
            budget.context.update(column=j)
            result.append(checked(sum(x*y for x,y in zip(row,col))))
            if j%16==0:budget.check()
        out.append(result);budget.check()
    return out

def symmetric(a,label):
    need(all(a[i][j]==a[j][i] for i in range(n) for j in range(i,n)),"EXACT_SYMMETRY: "+label)

def assemble(parity,aa,jj,hh,gg,budget):
    sector="even" if parity==0 else "odd";idx=list(range(parity,N,2))
    w=[2*j+1 for j in idx];g=[[gg[i][j] for j in idx] for i in idx]
    c=[[(aa[i][j]+jj[i][j])*(1 << 1025)+36*sum(hh[s][i]*hh[s][j] for s in (0,1))
        for j in idx] for i in idx]
    b=9*(1 << 255)
    bi=[[checked((b if i==j else 0)+w[i]*g[i][j]) for j in range(n)] for i in range(n)]
    symmetric(g,"G");symmetric(c,"C0")
    gw=[[g[i][j]*w[j] for j in range(n)] for i in range(n)]
    jint=matmul(gw,g,budget,"exact-Jint",sector);symmetric(jint,"Jint")
    cp=[[checked(c[i][j]+(g[i][j] << 1025)) for j in range(n)] for i in range(n)]
    m=matmul(cp,bi,budget,"exact-CG-times-Bint",sector)
    ki=matmul(transpose(bi),m,budget,"exact-Bint-adjoint-times-product",sector)
    for i in range(n):
        budget.context=dict(operation="exact-Kint-subtractions",sector=sector,row=i)
        for j in range(n):
            ki[i][j]=checked(ki[i][j]-81*(g[i][j] << 1535)-9*(jint[i][j] << 1280))
        budget.check()
    symmetric(ki,"Kint")
    return dict(sector=sector,indices=idx,w=w,g=g,Bint=bi,Jint=jint,Kint=ki,
                b=b,dK=81*(1 << 1792))

class IV:
    def rat(self,q):
        q=F(q);return checked(q.numerator*UNIT//q.denominator),checked(up(q.numerator*UNIT,q.denominator))
    def sub(self,a,b):return checked(a[0]-b[1]),checked(a[1]-b[0])
    def mul(self,a,b):
        v=[x*y for x in a for y in b]
        return checked(min(v)//UNIT),checked(up(max(v),UNIT))
    def square(self,a):
        low=0 if a[0]<=0<=a[1] else min(a[0]*a[0],a[1]*a[1])
        return checked(low//UNIT),checked(up(max(a[0]*a[0],a[1]*a[1]),UNIT))
    def div_positive(self,a,b):
        need(b[0]>0,"LDL_POSITIVE_DIVISOR")
        if a[0]>=0:lo,hi=a[0]*UNIT//b[1],up(a[1]*UNIT,b[0])
        elif a[1]<=0:lo,hi=a[0]*UNIT//b[0],up(a[1]*UNIT,b[1])
        else:lo,hi=a[0]*UNIT//b[0],up(a[1]*UNIT,b[0])
        return checked(lo),checked(hi)

def nearest(a,d):
    q,r=divmod(a,d)
    return q+(2*r>=d)

def output_bytes():
    """All prefix-owned bytes, INCLUDING the outer immutable attempt lock."""
    return CHARGED_EXTERNAL_BYTES+sum(p.stat().st_size for p in OUTER.rglob("*") if p.is_file())

class Budget:
    def __init__(self,bindings):
        self.started=PROCESS_STARTED
        self.startedUTC=datetime.fromtimestamp(PROCESS_STARTED_WALL,timezone.utc).isoformat()
        self.stage="authorized-start";self.context={};self.lastWrite=0.;self.lastSize=0.
        self.bindings=bindings;self.log=None
    def elapsed(self):return time.monotonic()-self.started+STARTUP_RESERVE_SECONDS
    def check(self):
        need(self.elapsed()<=SECONDS,"WHOLE_PREFIX_DEADLINE_STOP")
        now=time.monotonic()
        if now-self.lastSize>=1:
            need(output_bytes()<=BYTES-262144,"WHOLE_PREFIX_OUTPUT_CAP_STOP")
            need({p.name for p in OUTER.iterdir()}<={"run-lock.json",CURRENT_STAGE},
                 "UNAUTHORIZED_OTHER_STAGE_OR_PARENT_OUTPUT")
            self.lastSize=now
    def atomic(self,name,obj,emergency=False):
        raw=packed(obj)
        need(len(raw)<(131072 if emergency else BYTES-262144),"PREFIX_RECORD_SIZE_STOP")
        if not emergency:
            self.check();need(output_bytes()+len(raw)<=BYTES-262144,"WHOLE_PREFIX_OUTPUT_CAP_STOP")
        p=OUT/name;tmp=OUT/(name+".tmp")
        with tmp.open("wb") as f:f.write(raw);f.flush();os.fsync(f.fileno())
        os.replace(tmp,p)
    def progress(self,stage=None,force=False,**ctx):
        if stage is not None and stage!=self.stage:self.stage=stage;self.context={}
        if ctx:self.context=ctx
        self.check()
        if force or time.monotonic()-self.lastWrite>=3:
            if self.log is not None and not self.log.handle.closed:
                self.log.handle.flush()
                if force:os.fsync(self.log.handle.fileno())
            self.atomic("progress.json",dict(schema="RH_WEIL_WHOLE_PREFIX_PROGRESS_V1",
                status="RUNNING_WHOLE_PREREQUISITE",terminal=False,stage=self.stage,
                context=self.context,elapsedSecondsIncludingReserve=self.elapsed(),
                bindings=self.bindings,contractId="C068",targetId=TARGET_ID,
                mathematicalSettlement="PENDING_ROOT_C068",autoStage2Dispatched=False))
            self.lastWrite=time.monotonic()

class PivotLog:
    def __init__(self,budget):
        self.path=OUT/"pivots.jsonl.part";self.handle=self.path.open("xb")
        self.budget=budget;self.h=hashlib.sha256();self.size=0;self.rows=0
        budget.log=self
    def write(self,obj):
        raw=packed(obj);physical=self.path.stat().st_size
        self.budget.check()
        need(output_bytes()-physical+self.size+len(raw)<=BYTES-262144,"PREFIX_PIVOT_LOG_CAP_STOP")
        self.handle.write(raw);self.h.update(raw);self.size+=len(raw);self.rows+=1
    def finish(self):
        if not self.handle.closed:self.handle.flush();os.fsync(self.handle.fileno());self.handle.close()
        if self.path.name.endswith(".part"):
            os.replace(self.path,OUT/"pivots.jsonl");self.path=OUT/"pivots.jsonl"
    def record(self):
        return dict(file=self.path.name,rows=self.rows,bytes=self.size,sha256=self.h.hexdigest(),
                    closed=self.handle.closed)

def prerequisite_ldl(data,budget,log):
    """ONE unpivoted interval LDL of exact Khead-lambda*Thead."""
    iv=IV();sector=data["sector"];a=[]
    for i in range(n):
        budget.progress("prefix-interval-initialize",sector=sector,row=i)
        row=[]
        for j in range(n):
            budget.context["column"]=j
            t=F(2*data["g"][i][j],1 << 257)+F(data["Jint"][i][j],9*(1 << 512))
            if i==j:t+=F(9,4*data["w"][i])
            row.append(iv.rat(F(data["Kint"][i][j],data["dK"])-LAMBDA*t))
            if j%32==0:budget.check()
        a.append(row);budget.check()
    ell=[[(0,0)]*n for _ in range(n)]
    for k in range(n):
        d=a[k][k]
        budget.progress("prefix-ONE-LDL",force=True,operation="prefix-pivot",sector=sector,
            pivot=k,originalDegree=data["indices"][k],pivotEndpoints=list(map(str,d)),endpointBits=P)
        log.write(dict(sector=sector,phase="Hpre",pivot=k,degree=data["indices"][k],
            endpoints=list(map(str,d)),endpointBits=P,target="Khead-lambda*Thead"))
        if d[1]<0:return "NEGATIVE_PIVOT",k,ell,d
        if d[0]<=0:return "INTERVAL_UNRESOLVED",k,ell,d
        ell[k][k]=(UNIT,UNIT)
        for i in range(k+1,n):
            budget.context.update(updateRow=i,updateColumn=k,operation="prefix-LDL-factor")
            ell[i][k]=iv.div_positive(a[i][k],d)
        for i in range(k+1,n):
            budget.context.update(updateRow=i,updateColumn=None,operation="prefix-Schur-update")
            for j in range(i,n):
                budget.context["updateColumn"]=j
                product=iv.square(a[i][k]) if i==j else iv.mul(a[i][k],a[j][k])
                v=iv.sub(a[i][j],iv.div_positive(product,d));a[i][j]=a[j][i]=v
                if j%32==0:budget.check()
            budget.check()
    return "ALL_POSITIVE",n,ell,None

def sole_prefix_witness(data,k,ell,budget):
    """Point rounding proposes only. Exact SUBTRACT-lambda quadratic decides."""
    budget.progress("SOLE-prefix-proposal",force=True,sector=data["sector"],pivot=k)
    z=[0]*n;z[k]=UNIT
    for i in range(k-1,-1,-1):
        budget.context.update(backsolveRow=i)
        z[i]=checked(nearest(-sum((ell[j][i][0]+ell[j][i][1])*z[j]
                                 for j in range(i+1,k+1)),2*UNIT));budget.check()
    anum=[];qnum=0
    for i in range(n):
        budget.context=dict(operation="EXACT-prefix-model-quadratic",sector=data["sector"],row=i)
        anum.append(checked(sum(x*y for x,y in zip(data["Bint"][i],z))))
        qnum+=z[i]*sum(x*y for x,y in zip(data["Kint"][i],z));budget.check()
    aden=data["b"]*UNIT;qk=F(qnum,data["dK"]*UNIT*UNIT);norm=F(0)
    for i in range(n):
        budget.context=dict(operation="EXACT-prefix-fdu-metric",sector=data["sector"],row=i)
        norm+=F(9*anum[i]*anum[i],4*data["w"][i]*aden*aden);budget.check()
    qpre=qk-LAMBDA*norm
    answer=dict(sector=data["sector"],pivot=k,originalDegrees=data["indices"],
        Z=list(map(str,z)),zDenominatorPower=P,rawSourceNumerators=list(map(str,anum)),
        rawSourceDenominator=str(aden),exactChatQuadratic=frac(qk),exactPhysicalNorm=frac(norm),
        normMeaning="a*D*a=||f_a||du^2=int e^-u|r_a|^2du; r_a=e^(u/2)f_a; not unweighted r-du",
        lambdaExact=frac(LAMBDA),exactPrerequisiteQuadratic=frac(qpre),
        prefixNegativeCertified=norm>0 and qpre<0,proposalCount=1,
        authority="EXACT qpre=qK-lambda*physicalnorm; NO additional sourceEPS",
        scope="Negative Hpre ONLY rejects fixed whole sufficient recipe for ALL valid later Gram",
        congruenceRole="B0=D^-1(Graw+D), NOT the whole coefficient map B=AG",
        negativeCretClaim=False,negativeLretClaim=False,negativeQClaim=False)
    if norm>0:answer["exactPrerequisiteRayleigh"]=frac(qpre/norm)
    return answer

def evaluate_prefix(aa,jj,h,g,budget,log):
    sectors=[]
    for parity in (0,1):
        data=assemble(parity,aa,jj,h,g,budget)
        status,k,ell,_=prerequisite_ldl(data,budget,log)
        rec=dict(sector=data["sector"],prefixStatus=status,pivot=k)
        if status=="NEGATIVE_PIVOT":
            witness=sole_prefix_witness(data,k,ell,budget)
            rec["soleProposalPrefixNegativeCertified"]=witness["prefixNegativeCertified"]
            sectors.append(rec)
            return ("FIXED_WHOLE_RECIPE_REJECTED" if witness["prefixNegativeCertified"]
                    else "PREFIX_UNRESOLVED"),sectors,witness
        rec["necessarySectorPassed"]=status=="ALL_POSITIVE";sectors.append(rec)
    outcome="PREFIX_NECESSARY_PASS" if all(x["necessarySectorPassed"] for x in sectors) else "PREFIX_UNRESOLVED"
    return outcome,sectors,None

def canonical(x):return packed(x)

def preflight_clock_check():
    # Before valid authorization/namespace ownership, the external root launch
    # receipt is the terminal authority. This check never authorizes a retry.
    need(time.monotonic()-PROCESS_STARTED+STARTUP_RESERVE_SECONDS<=SECONDS,
         "PREFIX_PREFLIGHT_DEADLINE_STOP_EXTERNAL_ROOT_RECEIPT_REQUIRED")

def read_external_pin(record,label,code_sha=None,exact_path=None):
    preflight_clock_check()
    need(type(record) is dict and set(record)=={"path","sha256"},"EXTERNAL_PIN_SCHEMA: "+label)
    name,expected=record["path"],record["sha256"]
    need(type(name) is str and type(expected) is str,"EXTERNAL_PIN_TYPES: "+label)
    if exact_path is not None:need(name==exact_path,"EXTERNAL_PIN_PATH: "+label)
    path=(ROOT/name).resolve()
    need(path.is_relative_to(ROOT) and not path.is_relative_to(OUTER) and path!=SELF and path.is_file(),
         "READONLY_EXTERNAL_PIN_PATH: "+label)
    need(path.stat().st_size<=1024*1024,"EXTERNAL_PIN_SIZE: "+label)
    raw=path.read_bytes();need(sha(raw)==expected,"EXTERNAL_PIN_SHA: "+label)
    preflight_clock_check()
    if code_sha is not None:need(code_sha.encode("ascii") in raw,"REVIEW_MUST_NAME_EXACT_CODE: "+label)
    return name,path,raw

def validate_freeze(freeze_path):
    """No current preparation file is execution authorization."""
    global CHARGED_EXTERNAL_BYTES
    freeze_path=freeze_path.resolve()
    preflight_clock_check()
    need(not freeze_path.is_relative_to(OUTER),"FREEZE_OUTSIDE_NEW_RUN")
    raw=freeze_path.read_bytes();need(len(raw)<65536,"WHOLE_PREFIX_FREEZE_SIZE")
    preflight_clock_check()
    freeze=decode(raw);code=sha(SELF.read_bytes())
    need(freeze.get("schema")=="RH_WEIL_WHOLE_PREFIX_FREEZE_V1"
        and freeze.get("authorization")=="ROOT_EXPLICIT_C068_WHOLE_PREFIX_EXECUTION"
        and freeze.get("contractId")=="C068" and type(freeze.get("runtimeGoalCreatedAt")) is int
        and freeze.get("runtimeGoalCreatedAt")==1793085111
        and freeze.get("targetId")==TARGET_ID and freeze.get("currentStage")==CURRENT_STAGE,
        "NO_NEW_C068_WHOLE_PREFIX_FREEZE")
    need(freeze.get("numericalExecutionAuthorized") is True
        and freeze.get("laterStagesAuthorized") is False and freeze.get("oneAttemptOnly") is True,
        "PREFIX_ONLY_EXPLICIT_ONCE_EXECUTION_REQUIRED")
    need(freeze.get("codeSHA256")==code and freeze.get("sourceMathPins")==PINS
        and canonical(freeze.get("parameters"))==canonical(PARAMETERS)
        and canonical(freeze.get("stagedBudget"))==canonical(STAGED_BUDGET),
        "EXACT_WHOLE_CODE_PARAMETERS_SOURCE_FREEZE")
    dynamic={};external_sizes={}
    pn,_,protocol_raw=read_external_pin(freeze["protocolPin"],"protocol",exact_path=PREFIX+"staged-whole-protocol.md")
    dynamic[pn]=freeze["protocolPin"]["sha256"]
    sn,_,spec_raw=read_external_pin(freeze["protocolDesignPin"],"protocol-design",exact_path=PREFIX+"prefix-design.json")
    dynamic[sn]=freeze["protocolDesignPin"]["sha256"];spec=decode(spec_raw)
    need(spec.get("schema")=="RH_WEIL_STAGED_WHOLE_PROTOCOL_V1"
        and spec.get("status")=="PROTOCOL_SPECIFICATION_ONLY"
        and spec.get("numericalExecutionAuthorized") is False
        and spec.get("formalC068Admitted") is False and spec.get("prospectiveContractId")=="C068"
        and spec.get("runtimeGoalCreatedAt")==1793085111 and spec.get("targetId")==TARGET_ID
        and spec.get("currentStage")==CURRENT_STAGE
        and canonical(spec.get("parameters"))==canonical(PARAMETERS)
        and canonical(spec.get("stagedBudget"))==canonical(STAGED_BUDGET)
        and spec.get("aggregateOutputCapBytes")==64*(1 << 20)
        and spec.get("outerRelativePath")==str(OUTER.relative_to(ROOT)).replace("\\","/")
        and spec.get("prefixRelativePath")==str(OUT.relative_to(ROOT)).replace("\\","/"),
        "SPEC_ONLY_NOT_AUTHORIZATION_OR_PARAMETER_VARIANT")
    cn,cp,contract_raw=read_external_pin(freeze["contractPin"],"new-whole-contract")
    need(cp.is_relative_to(ROOT/"goals/contracts") and cp.name.startswith("C068")
        and cp.suffix==".md" and b"C068" in contract_raw,"ACTUAL_NEW_C068_CONTRACT_REQUIRED")
    dynamic[cn]=freeze["contractPin"]["sha256"]
    reviews=freeze.get("reviewPins");need(type(reviews) is dict and len(reviews)>=2,"NEW_CODE_REVIEWS_REQUIRED")
    resolved_reviews=set()
    for name,digest in reviews.items():
        rn,rp,_=read_external_pin(dict(path=name,sha256=digest),"code-review",code_sha=code)
        need(rp.is_relative_to(HERE),"REVIEW_MUST_BELONG_TO_NEW_PREFIX")
        need(rp not in resolved_reviews,"DISTINCT_REVIEW_FILES_REQUIRED");resolved_reviews.add(rp)
        need(rn not in dynamic,"REVIEW_PIN_COLLISION")
        dynamic[rn]=digest
    charges=freeze.get("chargedMetadataPins")
    need(type(charges) is dict,"EXPLICIT_EXTERNAL_ATTEMPT_METADATA_CHARGES_REQUIRED")
    for name,digest in charges.items():
        en,_,eraw=read_external_pin(dict(path=name,sha256=digest),"attempt-metadata-charge")
        need(en not in dynamic and en not in PINS,"ATTEMPT_METADATA_PIN_COLLISION")
        dynamic[en]=digest;external_sizes[en]=len(eraw)
    gn,_,gate_raw=read_external_pin(freeze["executionGatePin"],"root-execution-gate")
    need(gn not in dynamic and gn not in PINS,"EXECUTION_GATE_PIN_COLLISION")
    dynamic[gn]=freeze["executionGatePin"]["sha256"];gate=decode(gate_raw)
    need(gate.get("schema")=="RH_WEIL_WHOLE_PREFIX_ROOT_EXECUTION_GATE_V1"
        and gate.get("status")=="ROOT_EXPLICIT_PREFIX_EXECUTION_APPROVED"
        and gate.get("authorization")=="ROOT_EXPLICIT_C068_WHOLE_PREFIX_EXECUTION"
        and gate.get("contractId")=="C068" and type(gate.get("runtimeGoalCreatedAt")) is int
        and gate.get("runtimeGoalCreatedAt")==1793085111
        and gate.get("targetId")==TARGET_ID and gate.get("currentStage")==CURRENT_STAGE
        and gate.get("numericalExecutionAuthorized") is True
        and gate.get("laterStagesAuthorized") is False and gate.get("oneAttemptOnly") is True,
        "NEW_ROOT_WHOLE_EXECUTION_GATE_REQUIRED")
    for key in ("codeSHA256","sourceMathPins","parameters","stagedBudget","protocolPin",
                "protocolDesignPin","contractPin","reviewPins","chargedMetadataPins"):
        need(canonical(gate.get(key))==canonical(freeze.get(key)),"ROOT_GATE_FREEZE_AGREEMENT: "+key)
    need(not set(dynamic).intersection(PINS),"DYNAMIC_SOURCE_MATH_PIN_COLLISION")
    # Do not hash the freeze inside itself. Charge its ACTUAL bytes separately.
    external_sizes[gn]=len(gate_raw);external_sizes[str(freeze_path)]=len(raw)
    CHARGED_EXTERNAL_BYTES=sum(external_sizes.values())
    need(CHARGED_EXTERNAL_BYTES<BYTES-262144,"EXTERNAL_METADATA_CAP_STOP")
    need(not OUTER.exists(),"ONE_WHOLE_CANDIDATE_OUTER_ATTEMPT_ALREADY_EXISTS")
    OUTER.mkdir(parents=True,exist_ok=False)
    bindings=dict(codeSHA256=code,freezeSHA256=sha(raw),rootExecutionGateSHA256=sha(gate_raw),
        protocolSHA256=sha(protocol_raw),protocolDesignSHA256=sha(spec_raw),
        contractSHA256=sha(contract_raw),contractId="C068",targetId=TARGET_ID)
    return bindings,dict(PINS,**dynamic),raw,freeze_path,external_sizes

def create_lock(bindings,budget):
    need(not LOCK.exists(),"OUTER_ATTEMPT_LOCK_ALREADY_EXISTS")
    data=packed(dict(schema="RH_WEIL_C068_OUTER_ATTEMPT_LOCK_V1",contractId="C068",
        targetId=TARGET_ID,currentStage=CURRENT_STAGE,oneAttemptOnly=True,
        pid=os.getpid(),createdUTC=utc(),bindings=bindings,laterStagesAuthorized=False,
        mayBeRemovedByProgram=False))
    with LOCK.open("xb") as f:f.write(data);f.flush();os.fsync(f.fileno())
    budget.context=dict(operation="outer-attempt-lock",bytes=len(data),sha256=sha(data))
    budget.check()
    return dict(file=str(LOCK.relative_to(ROOT)).replace("\\","/"),bytes=len(data),sha256=sha(data))

def output_manifest():
    result=[]
    for path in sorted(OUTER.rglob("*")):
        if path.is_file() and path!=OUT/"progress.json":
            raw=path.read_bytes();result.append(dict(file=str(path.relative_to(ROOT)).replace("\\","/"),
                bytes=len(raw),sha256=sha(raw)))
    return result

def run_prefix(path):
    bindings,pins,freeze_raw,freeze_path,external_sizes=validate_freeze(path)
    budget=Budget(bindings);log=None;lock_record=None
    try:
        OUT.mkdir(exist_ok=False)
        lock_record=create_lock(bindings,budget)
        budget.progress("prefix-initial-input-review-pins",force=True)
        inventory=hash_pins(pins,budget)
        # Authorities select this exact charged prerequisite, not a fresh head test.
        selected=read_json(WHOLE+"candidate-preparation.json",budget)
        need(selected["numericalExecutionAuthorized"] is False
            and selected["formalC068Admitted"] is False,"PREPARATION_INPUT_REMAINS_NONAUTHORIZING")
        fees=read_json(WHOLE+"old-fee-recovery.json",budget)
        need(fees["bounds"]["CretCenterSourcePower"]==-224
            and fees["bounds"]["VAndGOperatorPower"]==-226,"RECOVERED_FIXED_WHOLE_SOURCE_AUTHORITY")
        aa,jj,h,g=load_centers(budget);log=PivotLog(budget)
        outcome,sectors,witness=evaluate_prefix(aa,jj,h,g,budget,log);log.finish()
        budget.progress("prefix-final-source-self-freeze-log",force=True)
        need(hash_pins(pins,budget)==inventory,"FINAL_PREFIX_SOURCE_REVIEW_PIN_GUARDS")
        budget.context=dict(operation="final-prefix-self-pin",path=str(SELF.relative_to(ROOT)))
        need(sha(SELF.read_bytes())==bindings["codeSHA256"],"FINAL_PREFIX_SELF_PIN")
        budget.context=dict(operation="final-prefix-freeze-pin",path=str(freeze_path))
        need(freeze_path.read_bytes()==freeze_raw,"FINAL_PREFIX_FREEZE_PIN")
        budget.context=dict(operation="final-outer-lock-pin",path=str(LOCK.relative_to(ROOT)))
        lock_raw=LOCK.read_bytes()
        need(len(lock_raw)==lock_record["bytes"] and sha(lock_raw)==lock_record["sha256"],"FINAL_OUTER_LOCK_PIN")
        lr=log.record();budget.context=dict(operation="final-prefix-pivot-log",file=lr["file"])
        raw=(OUT/lr["file"]).read_bytes()
        need(lr["closed"] is True and len(raw)==lr["bytes"] and sha(raw)==lr["sha256"],"FINAL_CLOSED_PREFIX_PIVOT_LOG")
        result=dict(schema="RH_WEIL_WHOLE_PREFIX_RESULT_V1",status=outcome,terminal=True,
            terminalScope="STAGE_01_PROCESS_ONLY",
            runtimeGoalCreatedAt=1793085111,contractId="C068",targetId=TARGET_ID,currentStage=CURRENT_STAGE,
            parameters=PARAMETERS,stagedBudget=STAGED_BUDGET,bindings=bindings,inputs=inventory,
            startedUTC=budget.startedUTC,endedUTC=utc(),elapsedSecondsIncludingReserve=budget.elapsed(),
            clockOrigin="first time import, before other imports/auth/guards;1s reserve NOT a startup proof",
            actualFullProcessLifetimeRequiresExternalRootVerification=True,
            sectors=sectors,pivotLog=lr,witness=witness,outerLock=lock_record,
            lambdaExact=frac(LAMBDA),prefixTarget="Chat-lambda*I; congruent Khead-lambda*Thead",
            normMeaning="original f-du; r=e^(u/2)f; ||f||du^2=int e^-u|r|^2du",
            exactPointSignAuthority="qK-lambda*physicalNorm; NO old qK+sourceEPS",
            predicateScope="Necessary condition of ONE fixed whole sufficient recipe for every valid later Gram",
            prerequisitePassIsWholeProof=False,negativeCretClaim=False,negativeLretClaim=False,negativeQClaim=False,
            C_X_ZProduced=False,autoStage2Dispatched=False,laterStagesAuthorized=False,
            stage2Eligibility=("NECESSARY_PREFIX_ONLY_PENDING_NEW_ROOT_GATE" if outcome=="PREFIX_NECESSARY_PASS"
                               else "BLOCKED_BY_THIS_STAGE"),
            mathematicalSettlement="PENDING_ROOT_C068",programSettlesIterations=0,
            technicalFailureIsNotMathematicalRefutation=True,
            wholeQCertified=False,RHCertified=False,GoalComplete=False,pendingProcesses=[],
            chargedExternalMetadataBytes=CHARGED_EXTERNAL_BYTES,chargedExternalMetadataFiles=external_sizes,
            runtimeOwnedBytesBeforeTerminalOutput=output_bytes(),
            postExitReceiptsAndScientificCheckersMustBeChargedExternally=True,
            nextAction="Root reconcile this same whole responsibility; NO automatic stage2, retry or separate head settlement")
        budget.check();budget.atomic("result.json",result)
        manifest=output_manifest()
        budget.atomic("progress.json",dict(schema="RH_WEIL_WHOLE_PREFIX_PROGRESS_V1",status=outcome,
            terminal=True,terminalScope="STAGE_01_PROCESS_ONLY",mathematicalSettlement="PENDING_ROOT_C068",contractId="C068",targetId=TARGET_ID,
            elapsedSecondsIncludingReserve=budget.elapsed(),filesExcludingThisProgress=manifest,
            bytesExcludingThisProgress=CHARGED_EXTERNAL_BYTES+sum(x["bytes"] for x in manifest),
            chargedExternalMetadataFiles=external_sizes,
            externalRootMustVerifyActualProcessLifetimeAndAllLaterReceipts=True,
            autoStage2Dispatched=False,laterStagesAuthorized=False))
        return result
    except BaseException as error:
        if not OUT.exists():OUT.mkdir(exist_ok=True)
        if log is not None:log.finish()
        failure=dict(schema="RH_WEIL_WHOLE_PREFIX_STOP_V1",status="PREFIX_TECHNICAL_STOP",terminal=True,
            terminalScope="STAGE_01_PROCESS_ONLY",
            runtimeGoalCreatedAt=1793085111,contractId="C068",targetId=TARGET_ID,currentStage=CURRENT_STAGE,
            parameters=PARAMETERS,stagedBudget=STAGED_BUDGET,bindings=bindings,
            startedUTC=budget.startedUTC,endedUTC=utc(),elapsedSecondsIncludingReserve=budget.elapsed(),
            stage=budget.stage,context=budget.context,errorType=type(error).__name__,reason=str(error)[:1500],
            integerWidthDiagnostic=(integer_width_diagnostic(error) if isinstance(error,IntegerWidthError) else None),
            pivotLog=(log.record() if log is not None else None),outerLock=lock_record,
            chargedExternalMetadataBytes=CHARGED_EXTERNAL_BYTES,chargedExternalMetadataFiles=external_sizes,
            mathematicalSettlement="PENDING_ROOT_C068",programSettlesIterations=0,
            technicalFailureIsNotMathematicalRefutation=True,noSource0OrReplacementBudgetClaim=True,
            C_X_ZProduced=False,autoStage2Dispatched=False,laterStagesAuthorized=False,
            negativeCretClaim=False,negativeLretClaim=False,negativeQClaim=False,
            wholeQCertified=False,RHCertified=False,GoalComplete=False,pendingProcesses=[],
            nextAction="Terminal same whole attempt; root settlement only; NO retry/alpha/precision/direction/route/source successor")
        budget.atomic("result.json",failure,True);budget.atomic("progress.json",failure,True)
        raise

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze-file",type=Path,required=True);args=parser.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    result=run_prefix(args.freeze_file)
    print(json.dumps(dict(status=result["status"],result=str(OUT/"result.json"),
        mathematicalSettlement="PENDING_ROOT_C068",autoStage2Dispatched=False)))

if __name__=="__main__":main()

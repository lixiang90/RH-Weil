"""ONE inverse-free fixed retained-tail head gate. PREPARATION: AST ONLY, NO RUN.

Standalone stdlib; never imports/invokes an old producer/checker/science driver.
Exact integer3-matmul assembly per parity, fixedP1024 outward Schur LDL,
eps2^-201, even then odd, upper then conditional lower. Globally ONE midpoint-L
point proposal; its sign authority is a direct EXACT rational quadratic.

Run requires --freeze-file JSON: schema RH_WEIL_SIGNED_HEAD_FREEZE_V1,
authorization ROOT_EXPLICIT_FREEZE_AND_RUN_SIGNED_HEAD, runtimeGoalCreatedAt
1793085111, codeSHA256=thisfile, parameters=PARAMETERS, pins=PINS, reviewPins
mapping>=2 new root/independent review paths to SHA. Each review must name this
exact codeSHA. Reviews/freeze are read-only and rechecked at end.

New ignored run-01 only,1800s/8MiB, atomic progress/result/pivot log, no restart,
parameter/precision/route/old-direction/eigenvector search. Strict negative
stops only bounded Lret PSD, not Q. Positive is HEAD ONLY. Root alone settles
mathematical iteration/cadence; unresolved arithmetic is experiment0.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SELF=Path(__file__).resolve()
OUT=ROOT/"literature/local/2026-11-01-retained-tail-signed-head/run-01"
P,N,n=1024,448,224
UNIT=1 << P
EPS=F(1,1 << 201)
SECONDS,BYTES,MAX_BITS=1800,8*(1 << 20),16384
PARAMETERS=dict(L="9/8",N=N,sectorDimension=n,eta=1,omega=256,intervalBits=P,
    sourceErrorPower=201,capSeconds=SECONDS,capBytes=BYTES,maxStoredIntegerBits=MAX_BITS,
    sectorOrder=["even","odd"],phaseOrder=["upper","conditional-lower"],
    maxWitnessProposals=1,witnessBits=P,witnessTieRule="nearest_ties_toward_positive_infinity",
    inverseComputed=False,exactMatmulsPerSector=3)
OLD="literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/"
CENTER="reviews/2026-10-31/retained-tail-center-admission/"
NEW="reviews/2026-11-01/retained-tail-signed-head/"
MATRIX=OLD+"source-matrices.json"
TAIL=OLD+"tail-columns.json"
GCOLS="literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl"
CERT="literature/local/2026-10-31-retained-tail-center-certificate/run-01/result.json"
PINS={
    MATRIX:"a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
    TAIL:"d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
    GCOLS:"d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080",
    CERT:"3eb9e77d71f92ead44775bfbafb7499a7ff0fd2e5bc81ac00095332a4f912739",
    CENTER+"root-consumption-scope.json":"6e0df0fed60465622f8b95551e4e361203a8de9b199bf167c38709caf4caaac3",
    CENTER+"source-centers-consumed.md":"a823cabb902b1fd0270fd210db0d2efa4a0085d7918b49ec3afb79739178a4a6",
    CENTER+"next-signed-head-admission.md":"3449a74e67fc71a9c5d0cb20430ddf420071ad803af50deb9af7bf644b5e2a56",
    "reviews/2026-10-29/weil-9-8-admission/source-stage-verification.json":"dbb31208d0568feac7c9adff27722d5b55d08381002d23e0a4e35f150b1472c1",
    "reviews/2026-10-29/weil-9-8-admission/full-weil-analytic-transfer-fresh.md":"0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466",
    NEW+"algorithm-design.md":"b545e7fdc5bcdce6bcc091be381c46bf3fddb23084559b6c9e9db0b515472eda",
    NEW+"design-freeze.json":"4c2bdb0bd298d36e6d59ae781595441beb666848c67ee53c9b5287fae35148a9",
    NEW+"math-admission.md":"6547b2ff0e0b2a4deeeb88ae549930cb51d7a16b99a77c6053e9c30413e04c95",
    NEW+"root-admission.md":"f75c4cf526a1ae5cfac512937a4f08424edbb4f3f41cfc64591757b75668b436",
    NEW+"congruence-fresh.md":"6dc809f6c5c46e63ab8f08ae00a11a9521ad42d32d3d316dd30cd126a07e0694",
    "goals/GOAL.20261027.md":"b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de",
    "goals/review-cadence.json":"4e556b9a84fd365a3a55bc4c345dc3dbe0f6e0543394dcca04093387a77560de",
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
    q=F(q);return [str(q.numerator),str(q.denominator)]
def utc(): return datetime.now(timezone.utc).isoformat()
def checked(a):
    need(abs(a).bit_length()<=MAX_BITS,"STORED_INTEGER_SIZE_STOP")
    return a

class Budget:
    def __init__(self,bindings):
        self.started=time.monotonic();self.startedUTC=utc()
        self.stage="start";self.context={};self.lastWrite=0.;self.lastSize=0.
        self.bindings=bindings;self.log=None
    def check(self):
        now=time.monotonic()
        need(now-self.started<=SECONDS,"SIGNED_HEAD_DEADLINE_STOP")
        if now-self.lastSize>=1:
            need(sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())<=BYTES-262144,
                 "SIGNED_HEAD_OUTPUT_CAP_STOP")
            self.lastSize=now
    def atomic(self,name,obj,emergency=False):
        raw=packed(obj)
        need(len(raw)<(131072 if emergency else BYTES-262144),"TERMINAL_RECORD_SIZE_STOP")
        if not emergency:
            self.check()
            need(sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())+len(raw)<=BYTES-262144,
                 "SIGNED_HEAD_OUTPUT_CAP_STOP")
        target=OUT/name;tmp=OUT/(name+".tmp")
        with tmp.open("wb") as f:
            f.write(raw);f.flush();os.fsync(f.fileno())
        os.replace(tmp,target)
    def progress(self,stage=None,force=False,**ctx):
        if stage is not None and stage!=self.stage:
            self.stage=stage;self.context={}
        if ctx:self.context=ctx
        self.check()
        if force or time.monotonic()-self.lastWrite>=3:
            if self.log is not None and not self.log.handle.closed:
                self.log.handle.flush()
                if force:os.fsync(self.log.handle.fileno())
            self.atomic("progress.json",dict(schema="RH_WEIL_SIGNED_HEAD_PROGRESS_V1",
                status="RUNNING_NEW_SIGNED_HEAD_GATE",stage=self.stage,context=self.context,
                startedUTC=self.startedUTC,elapsedSeconds=time.monotonic()-self.started,
                bindings=self.bindings,mathematicalSettlement="PENDING_ROOT"))
            self.lastWrite=time.monotonic()

class PivotLog:
    def __init__(self,budget):
        self.path=OUT/"pivots.jsonl.part";self.handle=self.path.open("xb")
        self.budget=budget;self.h=hashlib.sha256();self.size=0;self.rows=0
        budget.log=self
    def write(self,obj):
        raw=packed(obj)
        others=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file() and x!=self.path)
        self.budget.check();need(others+self.size+len(raw)<=BYTES-262144,"PIVOT_LOG_CAP_STOP")
        self.handle.write(raw);self.h.update(raw);self.size+=len(raw);self.rows+=1
    def finish(self):
        if not self.handle.closed:
            self.handle.flush();os.fsync(self.handle.fileno());self.handle.close()
        if self.path.name.endswith(".part"):
            os.replace(self.path,OUT/"pivots.jsonl");self.path=OUT/"pivots.jsonl"
    def record(self):
        return dict(file=self.path.name,rows=self.rows,bytes=self.size,sha256=self.h.hexdigest(),
                    closed=not self.handle.closed)

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

def interval_ldl(data,sign,budget,log):
    phase="upper" if sign==1 else "lower";iv=IV();sector=data["sector"]
    a=[]
    for i in range(n):
        budget.progress("interval-initialize",sector=sector,phase=phase,row=i)
        row=[]
        for j in range(n):
            budget.context["column"]=j
            t=F(2*data["g"][i][j],1 << 257)+F(data["Jint"][i][j],9*(1 << 512))
            if i==j:t+=F(9,4*data["w"][i])
            row.append(iv.rat(F(data["Kint"][i][j],data["dK"])+sign*EPS*t))
        a.append(row)
    ell=[[(0,0)]*n for _ in range(n)]
    for k in range(n):
        d=a[k][k]
        budget.context=dict(operation="LDL-pivot",sector=sector,phase=phase,pivot=k,
            originalDegree=data["indices"][k],pivotEndpoints=list(map(str,d)),endpointBits=P)
        budget.progress("interval-Schur-LDL",force=True,**budget.context)
        log.write(dict(sector=sector,phase=phase,pivot=k,degree=data["indices"][k],
            endpoints=list(map(str,d)),endpointBits=P))
        if d[1]<0:return "NEGATIVE_PIVOT",k,ell,d
        if d[0]<=0:return "INTERVAL_UNRESOLVED",k,ell,d
        ell[k][k]=(UNIT,UNIT)
        for i in range(k+1,n):ell[i][k]=iv.div_positive(a[i][k],d)
        for i in range(k+1,n):
            budget.context.update(updateRow=i,updateColumn=None)
            for j in range(i,n):
                budget.context["updateColumn"]=j
                product=iv.square(a[i][k]) if i==j else iv.mul(a[i][k],a[j][k])
                v=iv.sub(a[i][j],iv.div_positive(product,d))
                a[i][j]=a[j][i]=v
                if j%32==0:budget.check()
            budget.check()
    return "ALL_POSITIVE",n,ell,None

def nearest(a,d):
    q,r=divmod(a,d)
    return q+(2*r>=d)

def negative_proposal(data,k,ell,budget):
    budget.progress("SOLE-dyadic-negative-proposal",force=True,sector=data["sector"],pivot=k)
    z=[0]*n;z[k]=UNIT
    for i in range(k-1,-1,-1):
        budget.context.update(backsolveRow=i)
        z[i]=checked(nearest(-sum((ell[j][i][0]+ell[j][i][1])*z[j] for j in range(i+1,k+1)),2*UNIT))
        budget.check()
    anum=[];qnum=0
    for i in range(n):
        budget.context=dict(operation="EXACT-witness-quadratic",sector=data["sector"],row=i)
        anum.append(checked(sum(x*y for x,y in zip(data["Bint"][i],z))))
        qnum+=z[i]*sum(x*y for x,y in zip(data["Kint"][i],z));budget.check()
    aden=data["b"]*UNIT;qk=F(qnum,data["dK"]*UNIT*UNIT);norm=F(0)
    for i in range(n):
        budget.context=dict(operation="EXACT-physical-norm",sector=data["sector"],row=i)
        norm+=F(9*anum[i]*anum[i],4*data["w"][i]*aden*aden);budget.check()
    upper=qk+EPS*norm
    result=dict(sector=data["sector"],pivot=k,originalDegrees=data["indices"],
        Z=list(map(str,z)),zDenominatorPower=P,rawSourceNumerators=list(map(str,anum)),
        rawSourceDenominator=str(aden),exactModelQuadratic=frac(qk),exactPhysicalNorm=frac(norm),
        exactUpperQuadratic=frac(upper),sourceError=frac(EPS),
        negativeCertified=norm>0 and upper<0,proposalCount=1,
        finalAuthority="EXACT rational qK+eps*physicalnorm; midpoint-L accuracy is not assumed")
    if norm>0:result["strictPhysicalRayleighUpper"]=frac(upper/norm)
    return result

def gate(aa,jj,h,g,budget,log):
    sectors=[]
    for parity in (0,1):
        data=assemble(parity,aa,jj,h,g,budget)
        status,k,ell,pivot=interval_ldl(data,1,budget,log)
        rec=dict(sector=data["sector"],upperStatus=status,upperPivot=k)
        if status=="NEGATIVE_PIVOT":
            witness=negative_proposal(data,k,ell,budget)
            rec["soleProposalNegativeCertified"]=witness["negativeCertified"];sectors.append(rec)
            return ("NEGATIVE_HEAD" if witness["negativeCertified"] else "UNRESOLVED"),sectors,witness
        if status=="ALL_POSITIVE":
            low,lk,_,_=interval_ldl(data,-1,budget,log)
            rec.update(lowerStatus=low,lowerPivot=lk,positiveHeadSector=low=="ALL_POSITIVE")
        else:rec["positiveHeadSector"]=False
        sectors.append(rec)
    outcome="POSITIVE_HEAD_ONLY" if all(x.get("positiveHeadSector",False) for x in sectors) else "UNRESOLVED"
    return outcome,sectors,None

def freeze_guard(path):
    path=path.resolve();need(not path.is_relative_to(OUT),"FREEZE_OUTSIDE_OUTPUT")
    raw=path.read_bytes();need(len(raw)<65536,"FREEZE_SIZE")
    f=decode(raw);code=sha(SELF.read_bytes())
    need(f.get("schema")=="RH_WEIL_SIGNED_HEAD_FREEZE_V1"
        and f.get("authorization")=="ROOT_EXPLICIT_FREEZE_AND_RUN_SIGNED_HEAD"
        and f.get("runtimeGoalCreatedAt")==1793085111,"NO_ROOT_SIGNED_HEAD_FREEZE")
    need(packed(f.get("parameters"))==packed(PARAMETERS) and f.get("pins")==PINS
        and f.get("codeSHA256")==code,"EXACT_CODE_PARAMETER_INPUT_FREEZE")
    reviews=f.get("reviewPins");need(type(reviews) is dict and len(reviews)>=2,"ROOT_AND_INDEPENDENT_REVIEWS_REQUIRED")
    for name,digest in reviews.items():
        p=(ROOT/name).resolve()
        need(p.is_relative_to(HERE) and p!=SELF and p.is_file(),"NEW_REVIEW_PATH")
        data=p.read_bytes();need(sha(data)==digest and code.encode("ascii") in data,"EXACT_CODE_REVIEW_BINDING")
    need(not set(reviews).intersection(PINS),"REVIEW_INPUT_COLLISION")
    need(not OUT.exists(),"ONE_SIGNED_HEAD_ATTEMPT_ALREADY_EXISTS")
    OUT.mkdir(parents=True,exist_ok=False)
    return dict(codeSHA256=code,freezeSHA256=sha(raw)),dict(PINS,**reviews),raw,path

def run(path):
    bindings,pins,freeze_raw,freeze_path=freeze_guard(path);budget=Budget(bindings);log=None
    try:
        budget.progress("initial-input-pins",force=True)
        inventory=hash_pins(pins,budget)
        # Explicit native source error, separate from exact assembly and outward LDL.
        epsc=F(1,1 << 204)+2*F(1,1 << 220)+9*F(1,1 << 512)
        source=epsc+3*F(1,1 << 203);need(source<EPS,"SOURCE_BOUND_LT_EPS201")
        aa,jj,h,g=load_centers(budget);log=PivotLog(budget)
        outcome,sectors,witness=gate(aa,jj,h,g,budget,log);log.finish()
        budget.progress("final-source-self-freeze-guards",force=True)
        need(hash_pins(pins,budget)==inventory,"END_INPUT_INVENTORY")
        budget.context=dict(operation="final-code-pin",path=str(SELF.relative_to(ROOT)))
        need(sha(SELF.read_bytes())==bindings["codeSHA256"],"END_CODE_PIN")
        budget.context=dict(operation="final-freeze-pin",path=str(freeze_path))
        need(freeze_path.read_bytes()==freeze_raw,"END_FREEZE_PIN")
        lr=log.record()
        budget.context=dict(operation="final-pivot-log-pin",path=lr["file"],
                            expectedBytes=lr["bytes"],expectedSHA256=lr["sha256"])
        raw=(OUT/lr["file"]).read_bytes()
        need(len(raw)==lr["bytes"] and sha(raw)==lr["sha256"],"END_PIVOT_LOG_PIN")
        result=dict(schema="RH_WEIL_RETAINED_SIGNED_HEAD_V1",status=outcome,
            runtimeGoalCreatedAt=1793085111,parameters=PARAMETERS,bindings=bindings,inputs=inventory,
            startedUTC=budget.startedUTC,endedUTC=utc(),elapsedSeconds=time.monotonic()-budget.started,
            sectors=sectors,pivotLog=lr,witness=witness,
            sourceNativeErrorBound=frac(source),comparisonEps=frac(EPS),
            finiteArithmetic="EXACT rational/integer K,T; outward fixed1024-bit LDL; negative authority EXACT q",
            inverseComputed=False,oldDirectionRead=False,sameAcceptedGSourceUsed=True,
            mathematicalSettlement="PENDING_ROOT; strict sign eligibleONE, arithmetic unresolvedEXPERIMENT0",
            mathIterationsSettledByProgram=0,wholeQCertified=False,RHCertified=False,GoalComplete=False,
            scope="NEW Cret finite head ONLY; negative boundedLretPSD failure does not implyQnegative; wholecorrelation unpaid",
            pendingProcesses=[])
        budget.check();budget.atomic("result.json",result);budget.progress("complete-pending-root",force=True)
        return result
    except BaseException as e:
        if log is not None:log.finish()
        result=dict(schema="RH_WEIL_RETAINED_SIGNED_HEAD_STOP_V1",status="STOPPED_NO_RETRY",
            runtimeGoalCreatedAt=1793085111,parameters=PARAMETERS,bindings=bindings,
            startedUTC=budget.startedUTC,endedUTC=utc(),elapsedSeconds=time.monotonic()-budget.started,
            stage=budget.stage,context=budget.context,reason=str(e)[:1500],errorType=type(e).__name__,
            pivotLog=(log.record() if log is not None else None),mathIterationsSettledByProgram=0,
            classification="EXPERIMENT0 untilroot; no boundedcandidatefailuretheorem from arithmetic stop",
            wholeQCertified=False,RHCertified=False,GoalComplete=False,pendingProcesses=[],
            nextAction="root reconcile exact stop; no precision/vector/sector-order/source/parameter retry")
        budget.atomic("result.json",result,True);budget.atomic("progress.json",result,True)
        raise

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--freeze-file",type=Path,required=True)
    args=p.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    r=run(args.freeze_file);print(json.dumps(dict(status=r["status"],result=str(OUT/"result.json"))))
if __name__=="__main__":main()

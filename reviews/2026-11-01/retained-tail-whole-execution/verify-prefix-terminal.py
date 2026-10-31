"""Independent C068 NEGATIVE-prefix witness replay; preparation is AST ONLY.

Future invocation: --gate-file ROOT-authored RH_WEIL_C068_TERMINAL_REPLAY_GATE_V1.
Never imports/calls the producer, repeats LDL, forms its three matrix products,
inverts a matrix, proposes a direction, or dispatches another stage/process.
Only FIXED_WHOLE_RECIPE_REJECTED permits coordinate reads. Other terminal
statuses yield NOT_NEGATIVE_CERTIFICATE, with no positivity conclusion.

Gate pin records are {path: repository-relative POSIX path, sha256: hex digest}.
Required: verifierPin, producerCodePin, resultPin, freezePin, rootGatePin,
pivotLogPin, outerLockPin, reviewPins (path->SHA, >=2 naming this checker SHA),
sourceMathPins (same map as producer freeze), processControl (controllerPin,
phase='checker', cutoffSeconds<=100, noAutomaticNextProcess=true), and
stageAccounting (priorProcessSecondsUpper/remainingSeconds decimal strings,
priorChargedBytesUpper/remainingBytes integers, priorReceiptPins path->SHA).
The ROOT ledger must charge every preexisting/launch/checker byte and actual
full process lifetime to SAME stage01 600s/4MiB; this is not a new allowance.
priorChargedBytesUpper excludes ONLY this new gate and checker directory,
whose actual bytes this checker additionally charges. External root verifies
the interpreter/controller/post-exit lifetimes and receipt bytes as well.

Source/review paths and future C068 contract are dynamically pinned by the
gate/freeze. Immutable producer and three coordinate hashes below identify
the reviewed SAME object, not an alternate packet. No gate exists merely
because this preparation file exists. Do not import/run during preparation.
"""
from __future__ import annotations
import time
STARTED=time.monotonic()
STARTED_WALL=time.time()
import argparse
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,os,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
SELF=Path(__file__).resolve()
OUTER=ROOT/'literature/local/2026-11-01-retained-tail-whole-candidate/run-01'
PREFIX=OUTER/'stage-01-prefix'
OUT=PREFIX/'independent-negative-verifier'
REPORT=OUT/'checker-result.json'
GOAL=1793085111
TARGET='RH_WEIL_FIXED_9_8_COVARIANCE_JOINT_GRAM_T_WHOLE_V1'
STAGE='stage-01-prefix'
P,N,NSECTOR=1024,448,224
UNIT=1<<P
Q=1<<257
B=9*(1<<255)
MAX_BITS=16384
DIAGNOSTIC_BITS=65536
REPORT_CAP=128*(1<<10)
STAGE_SECONDS=600
STAGE_BYTES=4*(1<<20)
LAMBDA=F(1,1<<122)+F(1,1<<224)+F(1,1<<216)
PRODUCER='reviews/2026-11-01/retained-tail-whole-prefix/whole-prerequisite.py'
PRODUCER_SHA='c4a470a4e7aa887f51d3b37edc200cc0c9a129534d3d0a46ab3a6f5e34b25c4b'
OLD='literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/'
MATRIX=OLD+'source-matrices.json'
TAIL=OLD+'tail-columns.json'
GCOLS='literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl'
CORE={MATRIX:'a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2',
      TAIL:'d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e',
      GCOLS:'d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080'}
PARAMETERS=dict(L='9/8',N=448,sectorDimension=224,eta=1,omega=256,intervalBits=1024,
    lambdaPowers=[122,224,216],capSeconds=600,capBytes=4194304,maxStoredIntegerBits=16384,
    sectorOrder=['even','odd'],ldlPassesPerSector=1,
    ordinarySectorUnresolvedPolicy='continue_other_prescheduled_sector_with_same_budget',
    maxWitnessProposals=1,witnessBits=1024,witnessTieRule='nearest_ties_toward_positive_infinity',
    inverseComputed=False,exactMatmulsPerSector=3,autoStage2Dispatch=False)
STAGED=dict(aggregateCapSeconds=7200,stageCapSeconds=[600,3000,3600],
    stageCapBytes=[4194304,50331648,12582912],laterStagesAuthorized=False)

def need(ok,message):
    if not ok:raise ValueError(message)

def packed(value):
    return (json.dumps(value,ensure_ascii=True,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')

def digest(raw):return hashlib.sha256(raw).hexdigest()

def unique(pairs):
    out={}
    for k,v in pairs:
        need(k not in out,'DUPLICATE_JSON_KEY');out[k]=v
    return out

def decode(raw):
    return json.loads(raw,object_pairs_hook=unique,
        parse_constant=lambda _:need(False,'NONFINITE_JSON'))

def canon(v):return packed(v)

class IntegerWidthError(ValueError):
    def __init__(self,value):
        self.value=value;self.actualBitLength=abs(value).bit_length()
        self.normalLimit=MAX_BITS;self.serializedPart=None
        super().__init__('NORMAL_INTEGER_WIDTH_STOP actualBitLength='+str(self.actualBitLength)
                         +' normalLimit='+str(self.normalLimit))

def checked(value):
    need(type(value) is int,'EXACT_INTEGER_TYPE')
    if abs(value).bit_length()>MAX_BITS:raise IntegerWidthError(value)
    return value

def width_diagnostic(error):
    out=dict(actualBitLength=error.actualBitLength,normalLimitBits=error.normalLimit,
        diagnosticCapBits=DIAGNOSTIC_BITS,serializedPart=error.serializedPart,
        normalArithmeticDataUsable=False,mathematicalSignConclusion=False,technicalStopOnly=True)
    if error.actualBitLength<=DIAGNOSTIC_BITS:
        value=error.value
        out.update(encoding='FULL_SIGNED_HEXADECIMAL_DIAGNOSTIC_ONLY',
            signedHexValue=('-0x' if value<0 else '0x')+format(abs(value),'x'),
            fullDiagnosticValuePresent=True,valueOmitted=False)
    else:
        out.update(encoding='OMITTED_ABOVE_FIXED_DIAGNOSTIC_CAP',signedHexValue=None,
            fullDiagnosticValuePresent=False,valueOmitted=True,unconsumable=True,
            omissionReason='Value exceeds65536-bit diagnostic cap; no replacement or sign is asserted')
    return out

def integer(value):
    need(type(value) is str and 0<len(value)<=5000,'INTEGER_STRING_SHAPE')
    out=int(value);need(str(out)==value,'CANONICAL_INTEGER_STRING')
    return checked(out)

def fraction(value):
    need(type(value) is list and len(value)==2,'FRACTION_PAIR')
    a,b=map(integer,value);need(b>0,'FRACTION_POSITIVE_DENOMINATOR')
    out=F(a,b);need(out.numerator==a and out.denominator==b,'REDUCED_FRACTION')
    return out

def frac(value):
    value=F(value)
    try:numerator=checked(value.numerator)
    except IntegerWidthError as error:
        error.serializedPart='fraction-numerator';raise
    try:denominator=checked(value.denominator)
    except IntegerWidthError as error:
        error.serializedPart='fraction-denominator';raise
    return [str(numerator),str(denominator)]

def decimal(value):
    need(type(value) is str and 0<len(value)<=80,'LEDGER_DECIMAL_STRING')
    need(all(c in '0123456789.' for c in value) and value.count('.')<=1,'NONNEGATIVE_DECIMAL_LEDGER')
    out=F(value);need(out>=0,'NONNEGATIVE_LEDGER');return out

def relative(path):return str(path.relative_to(ROOT)).replace('\\','/')

def path_for(name):
    need(type(name) is str and '\\' not in name,'REPOSITORY_POSIX_PATH')
    p=Path(name);need(not p.is_absolute() and '..' not in p.parts,'REPOSITORY_RELATIVE_PATH')
    out=(ROOT/p).resolve();need(out.is_relative_to(ROOT),'PATH_ESCAPES_REPOSITORY')
    need(relative(out)==name,'CANONICAL_REPOSITORY_PATH');return out

def validate_pin(pin):
    need(type(pin) is dict and set(pin)=={'path','sha256'},'PIN_RECORD')
    path=path_for(pin['path']);h=pin['sha256']
    need(type(h) is str and len(h)==64 and all(c in '0123456789abcdef' for c in h),'SHA256_FORMAT')
    return path

class Replay:
    def __init__(self,gate_path,gate_raw,gate):
        self.gate_path=gate_path;self.gate_raw=gate_raw;self.gate=gate
        self.context={};self.snapshots={};self.report_written=False
        a=gate['stageAccounting'];self.prior_seconds=decimal(a['priorProcessSecondsUpper'])
        self.remaining=decimal(a['remainingSeconds'])
        self.prior_bytes=a['priorChargedBytesUpper'];self.remaining_bytes=a['remainingBytes']
        need(type(self.prior_bytes) is int and type(self.remaining_bytes) is int
             and self.prior_bytes>=0 and self.remaining_bytes>0,'LEDGER_BYTE_INTEGER')
        need(self.prior_seconds+self.remaining<=STAGE_SECONDS and self.remaining>0,'NO_FRESH_TIME_ALLOWANCE')
        need(self.prior_bytes+self.remaining_bytes<=STAGE_BYTES,'NO_FRESH_BYTE_ALLOWANCE')
        control=gate['processControl'];cutoff=control['cutoffSeconds']
        need(type(cutoff) in (int,float) and 0<cutoff<=100,'CHECKER_CONTROLLER_CUTOFF')
        self.cutoff=min(float(self.remaining),float(cutoff))

    def elapsed(self):return time.monotonic()-STARTED

    def own_bytes(self):
        return len(self.gate_raw)+sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())

    def check(self):
        need(self.elapsed()<=self.cutoff,'CHECKER_REMAINING_TIME_STOP')
        need(self.own_bytes()<self.remaining_bytes,'CHECKER_SHARED_STAGE_BYTE_STOP')

    def pin(self,pin,label,limit=None,keep=False):
        self.context=dict(operation='read-pinned-file',label=label,path=pin.get('path'),bytes=0)
        p=validate_pin(pin);need(p.is_file(),'PIN_FILE_MISSING: '+label)
        self.check();h=hashlib.sha256();size=0;parts=[]
        with p.open('rb') as stream:
            while block:=stream.read(1<<20):
                size+=len(block);self.context['bytes']=size
                need(limit is None or size<=limit,'PIN_SIZE: '+label)
                h.update(block)
                if keep:parts.append(block)
                self.check()
        need(h.hexdigest()==pin['sha256'],'PIN_HASH: '+label)
        record=dict(bytes=size,sha256=h.hexdigest())
        old=self.snapshots.get(pin['path']);need(old is None or old==record,'PIN_CHANGED_DURING_USE')
        self.snapshots[pin['path']]=record
        return b''.join(parts) if keep else record

    def json_pin(self,pin,label,limit=65536):
        return decode(self.pin(pin,label,limit,True))

    def pin_map(self,pins,label,read_sources=True):
        need(type(pins) is dict and len(pins)>0,'NONEMPTY_PIN_MAP: '+label)
        for name,h in pins.items():
            p=validate_pin(dict(path=name,sha256=h))
            need(not p.is_relative_to(OUT),'INPUT_INSIDE_CHECKER_OUTPUT')
            if read_sources:self.pin(dict(path=name,sha256=h),label)

    def final_guards(self):
        self.context=dict(operation='final-gate-self-guard',path=relative(self.gate_path))
        need(self.gate_path.read_bytes()==self.gate_raw,'FINAL_VERIFIER_GATE_CHANGED')
        # Replay all consumed pins, INCLUDING original sources, reviews, self,
        # old terminal result/freezes/log/lock/controller/prior receipts.
        previous=dict(self.snapshots)
        for name,record in previous.items():
            now=self.pin(dict(path=name,sha256=record['sha256']),'final-immutable-input')
            need(now==record,'FINAL_INPUT_BYTES_CHANGED')
        self.check()

    def write(self,value):
        need(not self.report_written,'ONE_TERMINAL_CHECKER_RECORD')
        raw=packed(value);need(len(raw)<REPORT_CAP,'CHECKER_REPORT_128K_STOP')
        # Prior bytes + this gate + actual current files + atomic temporary
        # record never exceed the one shared stage budget.
        need(self.own_bytes()+len(raw)<=self.remaining_bytes,'NO_REMAINING_REPORT_BYTES')
        tmp=OUT/'checker-result.json.tmp'
        with tmp.open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
        os.replace(tmp,REPORT);self.report_written=True

def common_scope(obj):
    need(obj.get('runtimeGoalCreatedAt')==GOAL and type(obj.get('runtimeGoalCreatedAt')) is int
         and obj.get('contractId')=='C068' and obj.get('targetId')==TARGET
         and obj.get('currentStage')==STAGE,'SAME_C068_GOAL_OBJECT_STAGE')

def false_claims(obj):
    for name in ('negativeCretClaim','negativeLretClaim','negativeQClaim','wholeQCertified',
                 'RHCertified','GoalComplete','C_X_ZProduced','autoStage2Dispatched','laterStagesAuthorized'):
        need(obj.get(name) is False,'FALSE_SCOPE_FLAG: '+name)
    need(obj.get('programSettlesIterations')==0 and obj.get('mathematicalSettlement')=='PENDING_ROOT_C068',
         'NO_DRIVER_ITERATION_SETTLEMENT')

def authorize(gate_path):
    gate_path=gate_path.resolve();need(gate_path.is_relative_to(ROOT),'GATE_IN_REPOSITORY')
    need(not gate_path.is_relative_to(OUT),'GATE_OUTSIDE_CHECKER_OUTPUT')
    raw=gate_path.read_bytes();need(len(raw)<65536,'REPLAY_GATE_SIZE')
    gate=decode(raw);common_scope(gate)
    need(gate.get('schema')=='RH_WEIL_C068_TERMINAL_REPLAY_GATE_V1'
         and gate.get('authorization')=='ROOT_EXPLICIT_C068_TERMINAL_REPLAY'
         and gate.get('numericalExecutionAuthorized') is True
         and gate.get('laterStagesAuthorized') is False and gate.get('oneAttemptOnly') is True,
         'NO_FUTURE_EXPLICIT_TERMINAL_REPLAY_AUTHORIZATION')
    need(validate_pin(gate['verifierPin'])==SELF and digest(SELF.read_bytes())==gate['verifierPin']['sha256'],
         'EXACT_VERIFIER_CODE_AUTHORIZATION')
    control=gate['processControl']
    need(control.get('phase')=='checker' and control.get('noAutomaticNextProcess') is True,
         'CHECKER_ONLY_EXTERNAL_CONTROLLER')
    validate_pin(control['controllerPin'])
    need(validate_pin(gate['resultPin'])==PREFIX/'result.json','SAME_PREFIX_TERMINAL_PATH')
    need(validate_pin(gate['pivotLogPin'])==PREFIX/'pivots.jsonl','SAME_PREFIX_LOG_PATH')
    need(validate_pin(gate['outerLockPin'])==OUTER/'run-lock.json','SAME_OUTER_LOCK_PATH')
    need(gate['producerCodePin']==dict(path=PRODUCER,sha256=PRODUCER_SHA),'EXACT_IMMUTABLE_PRODUCER')
    reviews=gate.get('reviewPins');need(type(reviews) is dict and len(reviews)>=2,'INDEPENDENT_CHECKER_REVIEWS')
    for name,h in reviews.items():
        p=validate_pin(dict(path=name,sha256=h));need(not p.is_relative_to(OUT),'REVIEW_OUTSIDE_NEW_OUTPUT')
    replay=Replay(gate_path,raw,gate)
    need(PREFIX.is_dir() and not OUT.exists(),'ONE_CHECKER_ATTEMPT_ONLY')
    OUT.mkdir(exist_ok=False)  # exclusive durable attempt marker, never removed
    return replay

def metadata(replay):
    gate=replay.gate
    replay.pin(gate['verifierPin'],'verifier-self')
    replay.pin(gate['producerCodePin'],'immutable-producer-code')
    replay.pin(gate['processControl']['controllerPin'],'external-controller')
    reviews=gate['reviewPins']
    for name,h in reviews.items():
        raw=replay.pin(dict(path=name,sha256=h),'checker-review',1<<20,True)
        need(gate['verifierPin']['sha256'].encode('ascii') in raw,'REVIEW_NAMES_FINAL_CHECKER_SHA')
    replay.pin_map(gate['stageAccounting']['priorReceiptPins'],'prior-full-process-ledger-receipt')
    freeze=replay.json_pin(gate['freezePin'],'producer-freeze')
    root=replay.json_pin(gate['rootGatePin'],'producer-root-execution-gate')
    result=replay.json_pin(gate['resultPin'],'producer-terminal-result',STAGE_BYTES)
    for obj in (freeze,root,result):common_scope(obj)
    need(freeze.get('schema')=='RH_WEIL_WHOLE_PREFIX_FREEZE_V1'
         and root.get('schema')=='RH_WEIL_WHOLE_PREFIX_ROOT_EXECUTION_GATE_V1'
         and root.get('status')=='ROOT_EXPLICIT_PREFIX_EXECUTION_APPROVED','ORIGINAL_PREFIX_AUTHORIZATION_SCHEMAS')
    for obj in (freeze,root):
        need(obj.get('authorization')=='ROOT_EXPLICIT_C068_WHOLE_PREFIX_EXECUTION'
             and obj.get('numericalExecutionAuthorized') is True
             and obj.get('laterStagesAuthorized') is False and obj.get('oneAttemptOnly') is True,
             'ORIGINAL_ONCE_PREFIX_AUTHORIZATION')
        need(obj.get('codeSHA256')==PRODUCER_SHA and canon(obj.get('parameters'))==canon(PARAMETERS)
             and canon(obj.get('stagedBudget'))==canon(STAGED),'ORIGINAL_FIXED_PREFIX_PARAMETERS')
    for key in ('codeSHA256','sourceMathPins','parameters','stagedBudget','protocolPin',
                'protocolDesignPin','contractPin','reviewPins','chargedMetadataPins'):
        need(canon(root.get(key))==canon(freeze.get(key)),'ORIGINAL_ROOT_FREEZE_AGREEMENT: '+key)
    need(freeze['executionGatePin']==gate['rootGatePin'],'SAME_ORIGINAL_ROOT_GATE_PIN')
    source=freeze['sourceMathPins'];need(source==gate.get('sourceMathPins'),'REPLAY_SOURCE_MAP_EXACT')
    replay.pin_map(source,'source-map-schema',False)
    need(all(source.get(name)==h for name,h in CORE.items()),'SAME_THREE_COORDINATE_PACKETS')
    need(result.get('terminal') is True and result.get('terminalScope')=='STAGE_01_PROCESS_ONLY',
         'ACTUAL_TERMINAL_PREFIX_RESULT')
    need(canon(result.get('parameters'))==canon(PARAMETERS) and canon(result.get('stagedBudget'))==canon(STAGED),
         'RESULT_FIXED_PARAMETERS')
    false_claims(result)
    bindings=result['bindings']
    expected=dict(codeSHA256=PRODUCER_SHA,freezeSHA256=gate['freezePin']['sha256'],
        rootExecutionGateSHA256=gate['rootGatePin']['sha256'],
        protocolSHA256=freeze['protocolPin']['sha256'],protocolDesignSHA256=freeze['protocolDesignPin']['sha256'],
        contractSHA256=freeze['contractPin']['sha256'],contractId='C068',targetId=TARGET)
    need(bindings==expected,'EXACT_RESULT_BINDINGS')
    lock=replay.json_pin(gate['outerLockPin'],'original-outer-once-lock')
    need(lock.get('schema')=='RH_WEIL_C068_OUTER_ATTEMPT_LOCK_V1'
         and lock.get('contractId')=='C068' and lock.get('targetId')==TARGET
         and lock.get('currentStage')==STAGE and lock.get('oneAttemptOnly') is True
         and lock.get('laterStagesAuthorized') is False and lock.get('mayBeRemovedByProgram') is False
         and lock.get('bindings')==bindings,'ORIGINAL_ONCE_ATTEMPT_LOCK')
    lr=result['outerLock']
    need(lr['file']==gate['outerLockPin']['path'] and lr['sha256']==gate['outerLockPin']['sha256']
         and lr['bytes']==replay.snapshots[lr['file']]['bytes'],'RESULT_OUTER_LOCK_RECORD')
    # Dynamic metadata pins are consumed now. Coordinate source pins deliberately
    # remain unopened until the exact NEGATIVE result status is established.
    for key in ('protocolPin','protocolDesignPin','contractPin'):
        replay.pin(freeze[key],'original-'+key)
    replay.pin_map(freeze['reviewPins'],'original-producer-review')
    need(type(freeze['chargedMetadataPins']) is dict,'ORIGINAL_CHARGED_METADATA_MAP')
    if freeze['chargedMetadataPins']:
        replay.pin_map(freeze['chargedMetadataPins'],'original-charged-metadata')
    return result,freeze

def validate_log(replay,result,witness):
    gate=replay.gate;record=result['pivotLog']
    need(record['closed'] is True and record['file']=='pivots.jsonl'
         and record['sha256']==gate['pivotLogPin']['sha256'],'TRUE_CLOSED_LOG_PIN')
    raw=replay.pin(gate['pivotLogPin'],'complete-terminal-pivot-log',1<<20,True)
    need(record['bytes']==len(raw) and raw.endswith(b'\n'),'TERMINAL_LOG_BYTES')
    need(not (PREFIX/'pivots.jsonl.part').exists() and not (PREFIX/'result.json.tmp').exists()
         and not (PREFIX/'progress.json.tmp').exists(),'NO_UNCLOSED_PRODUCER_ARTIFACT')
    lines=raw.splitlines();need(record['rows']==len(lines) and 1<=len(lines)<=448,'LOG_ACTUAL_ROW_COUNT')
    sectors=result['sectors'];need(type(sectors) is list and 1<=len(sectors)<=2,'SECTOR_RECORDS')
    pos=0;negative_count=0
    for si,sector in enumerate(sectors):
        name=('even','odd')[si];need(sector.get('sector')==name,'PRESCHEDULED_SECTOR_ORDER')
        parity=si;kind=sector['prefixStatus'];k=sector['pivot']
        need(type(k) is int,'PIVOT_INDEX_TYPE')
        if kind=='ALL_POSITIVE':
            need(k==224 and sector.get('necessarySectorPassed') is True,'POSITIVE_LOG_ONLY')
            count=224
        else:
            need(kind in ('INTERVAL_UNRESOLVED','NEGATIVE_PIVOT') and 0<=k<224,'TERMINAL_SECTOR_KIND')
            count=k+1
        for i in range(count):
            replay.context=dict(operation='check-log-row',row=pos+1,sector=name,pivot=i)
            need(pos<len(lines),'LOG_MISSING_ROW');row=decode(lines[pos]);pos+=1
            need(row.get('sector')==name and row.get('phase')=='Hpre' and row.get('pivot')==i
                 and row.get('degree')==parity+2*i and row.get('endpointBits')==P
                 and row.get('target')=='Khead-lambda*Thead','EXACT_LOG_LOCATION_TARGET')
            ep=row.get('endpoints');need(type(ep) is list and len(ep)==2,'LOG_ENDPOINT_PAIR')
            lo,hi=map(integer,ep);need(lo<=hi,'LOG_ENDPOINT_ORDER')
            if i<count-1 or kind=='ALL_POSITIVE':need(lo>0,'LOG_POSITIVE_PREFIX')
            elif kind=='INTERVAL_UNRESOLVED':need(lo<=0<=hi,'LOG_ORDINARY_UNRESOLVED')
            else:
                need(hi<0 and si==len(sectors)-1,'SOLE_FINAL_NEGATIVE_PIVOT');negative_count+=1
                need(witness['sector']==name and witness['pivot']==i,'WITNESS_LOG_LOCATION')
            replay.check()
    need(pos==len(lines) and negative_count==1,'EXACT_ONE_NEGATIVE_LOG_TERMINAL')
    need(all(s.get('necessarySectorPassed') is False for s in sectors
             if s['prefixStatus']=='INTERVAL_UNRESOLVED'),'UNRESOLVED_SECTOR_NOT_POSITIVE')
    need(sectors[-1].get('soleProposalPrefixNegativeCertified') is True,'SOLE_PROPOSAL_CERTIFIED_RECORD')
    return dict(rows=pos,sectors=len(sectors),closed=True,sha256=record['sha256'],
                bytes=len(raw),logValidationIsNotLDLReplay=True)

def load_coordinates(replay,source):
    # Only called after exact negative-status admission and source hash guards.
    packet=replay.json_pin(dict(path=MATRIX,sha256=source[MATRIX]),'old-raw-A-J0',32*(1<<20))['packet']
    p=packet['parameters']
    need(p['N']==N and p['L']=='9/8' and p['omega']==256 and p['beta']=='7/2' and p['outputBits']==256,
         'OLD_MATRIX_PARAMETERS')
    need(packet['sourceConventions']['J0']=='L_squared_H'
         and packet['sourceConventions']['orderedPrimePairs']==225,'OLD_MATRIX_CONVENTIONS')
    mats={}
    for name in ('A','J0'):
        rows=packet['matrices'][name];need(type(rows) is list and len(rows)==50400,'OLD_PARITY_TRIANGLE_SHAPE')
        a=[[0]*N for _ in range(N)];pos=0
        for i in range(N):
            for j in range(i,N,2):
                replay.context=dict(operation='parse-old-matrix',matrix=name,position=pos,column=i,degree=j)
                row=rows[pos];need(type(row) is list and len(row)==4 and row[:2]==[i,j],'OLD_TRIANGLE_ORDER')
                lo,hi=map(integer,row[2:]);need(lo<=hi,'OLD_ENDPOINT_ORDER')
                a[i][j]=a[j][i]=checked(lo+hi);pos+=1
            replay.check()
        mats[name]=a
    need(len(packet['matrices']['B'])==50400,'UNUSED_B_WRAPPER_SHAPE');del packet
    tail=replay.json_pin(dict(path=TAIL,sha256=source[TAIL]),'old-ranktwo-h',1<<20)['packet'];tp=tail['parameters']
    need(tp['dimension']==N and tp['omega']==256 and tp['LNumerator']==9 and tp['LDenominator']==8
         and tp['outputBits']==640 and len(tail['entries'])==896,'OLD_H_PARAMETERS_SHAPE')
    h=[[0]*N for _ in range(2)]
    for k,row in enumerate(tail['entries']):
        s,i=divmod(k,N);replay.context=dict(operation='parse-old-h',position=k,column=s,degree=i)
        need(row['column']==s and row['index']==i,'OLD_H_ORDER')
        lo,hi,mid=(integer(row[key]) for key in ('lo','hi','midTwice'))
        need(lo<=hi and mid==lo+hi and (i%2==s or (lo,hi,mid)==(0,0,0)),'SAME_H_CENTER_PARITY')
        h[s][i]=mid
    g=[[0]*N for _ in range(N)];hsh=hashlib.sha256();count=size=head=0
    with path_for(GCOLS).open('rb') as stream:
        for j in range(N):
            for i in range(j%2,2047,2):
                replay.context=dict(operation='parse-entire-SAME-V-stream',position=count+1,column=j,degree=i,byteOffset=size)
                raw=stream.readline(65537)
                need(raw and raw.endswith(b'\n') and len(raw)<=65536,'FINITE_STREAM_LINE')
                hsh.update(raw);count+=1;size+=len(raw);row=decode(raw)
                need(type(row) is list and len(row)==4 and row[:2]==[j,i],'FINITE_STREAM_FULL_ORDER')
                lo,hi=map(integer,row[2:]);need(lo<=hi,'FINITE_STREAM_ENDPOINT_ORDER')
                if i<N:
                    mid=checked(lo+hi)
                    if i<j:need(g[i][j]==mid,'SAME_G_FULL_HEAD_COPY_SYMMETRY')
                    g[j][i]=mid;head+=1
                if count%1024==0:replay.check()
            replay.check()
        need(stream.read(1)==b'','NO_EXTRA_FINITE_STREAM_ROW')
    need(count==458528 and head==100352 and size==73598411 and hsh.hexdigest()==source[GCOLS],
         'ENTIRE_FINITE_STREAM_SHA_COUNTS')
    need(replay.snapshots[GCOLS]==dict(bytes=size,sha256=hsh.hexdigest()),'STREAM_MATCHES_INITIAL_SOURCE_HASH')
    return mats['A'],mats['J0'],h,g

def direct_replay(replay,witness,aa,jj,hh,gg):
    sector=witness['sector'];need(sector in ('even','odd'),'WITNESS_SECTOR')
    idx=list(range(0 if sector=='even' else 1,N,2));w=[2*i+1 for i in idx]
    need(witness['originalDegrees']==idx and witness['zDenominatorPower']==P,'SAME_RAW_BASIS_WITNESS')
    need(witness.get('proposalCount')==1 and witness.get('prefixNegativeCertified') is True,'ONE_SAVED_PROPOSAL')
    for flag in ('negativeCretClaim','negativeLretClaim','negativeQClaim'):
        need(witness.get(flag) is False,'WITNESS_NO_PHYSICAL_NEGATIVITY_CLAIM')
    rows=witness['Z'];need(type(rows) is list and len(rows)==NSECTOR,'WITNESS_VECTOR_SHAPE')
    z=[integer(x) for x in rows];k=witness['pivot'];need(type(k) is int and 0<=k<NSECTOR,'WITNESS_PIVOT')
    need(z[k]==UNIT and all(x==0 for x in z[k+1:]),'SAVED_PIVOT_DIRECTION_SUPPORT')
    need(witness['rawSourceDenominator']==str(B*UNIT),'RAW_PHYSICAL_DENOMINATOR')
    stored=witness['rawSourceNumerators'];need(type(stored) is list and len(stored)==NSECTOR,'RAW_SOURCE_VECTOR_SHAPE')
    stored=[integer(x) for x in stored]
    # First and only matrix-vector multiplication gZ, O(224^2); exact integers.
    y=[]
    for ri,i in enumerate(idx):
        replay.context=dict(operation='direct-g-times-saved-Z',sector=sector,row=ri,degree=i)
        y.append(checked(sum(gg[i][j]*z[cj] for cj,j in enumerate(idx))));replay.check()
    anum=[checked(B*z[i]+w[i]*y[i]) for i in range(NSECTOR)]
    for i,(got,expected) in enumerate(zip(anum,stored)):
        replay.context=dict(operation='compare-raw-physical-source',sector=sector,index=i,
                            computed=str(got),stored=str(expected),denominator=str(B*UNIT))
        need(got==expected,'SAME_STORED_RAW_PHYSICAL_SOURCE')
    # Direct quadratic of A+J0+Graw and rank-two h, not the producer's Kint.
    core=0
    for ri,i in enumerate(idx):
        replay.context=dict(operation='direct-A-J0-G-quadratic',sector=sector,row=ri,degree=i)
        dot=checked(sum((aa[i][j]+jj[i][j]+gg[i][j])*anum[cj] for cj,j in enumerate(idx)))
        core=checked(core+anum[ri]*dot);replay.check()
    hdot=[checked(sum(hh[s][j]*anum[cj] for cj,j in enumerate(idx))) for s in (0,1)]
    aden=B*UNIT
    term1=F(core,Q*aden*aden)
    term2=F(36*sum(t*t for t in hdot),(1<<1282)*aden*aden)
    term3=F(sum(z[i]*y[i] for i in range(NSECTOR)),Q*UNIT*UNIT)
    term4=F(sum(w[i]*y[i]*y[i] for i in range(NSECTOR)),9*(1<<512)*UNIT*UNIT)
    qk=term1+term2-term3-term4
    norm=sum((F(9*anum[i]*anum[i],4*w[i]*aden*aden) for i in range(NSECTOR)),F(0))
    qpre=qk-LAMBDA*norm
    replay.context=dict(operation='exact-saved-negative-certificate',sector=sector,pivot=k,
        exactChatQuadratic=frac(qk),exactPhysicalNorm=frac(norm),exactPrerequisiteQuadratic=frac(qpre))
    for key,computed in (('exactChatQuadratic',qk),('exactPhysicalNorm',norm),
                         ('lambdaExact',LAMBDA),('exactPrerequisiteQuadratic',qpre)):
        need(fraction(witness[key])==computed,'EXACT_STORED_WITNESS_MATCH: '+key)
    need(norm>0,'STRICT_POSITIVE_PHYSICAL_NORM')
    rayleigh=qpre/norm
    need(fraction(witness['exactPrerequisiteRayleigh'])==rayleigh,'EXACT_STORED_RAYLEIGH')
    need(qpre<0,'STRICT_NEGATIVE_FIXED_RECIPE_PREREQUISITE')
    replay.check()
    return dict(sector=sector,pivot=k,originalDegrees=idx,proposalCount=1,
        exactChatQuadratic=frac(qk),exactPhysicalNorm=frac(norm),lambdaExact=frac(LAMBDA),
        exactPrerequisiteQuadratic=frac(qpre),exactPrerequisiteRayleigh=frac(rayleigh),
        directQuadraticTerms=dict(A_J0_G=frac(term1),rankTwo=frac(term2),
                                  Gsubtraction=frac(term3),GDinvGsubtraction=frac(term4)),
        rawSourceNumeratorsVerified=True,rawSourceDenominator=str(aden),
        reconstruction='anum=b Z+diag(2degree+1)gZ; raw a=anum/(b*2^1024)',
        normMeaning='f in L2(du); r=exp(u/2)f; norm=int exp(-u)|r|^2du')

def base_report(replay,status):
    return dict(schema='RH_WEIL_C068_TERMINAL_REPLAY_RESULT_V1',status=status,terminal=True,
        runtimeGoalCreatedAt=GOAL,contractId='C068',targetId=TARGET,currentStage=STAGE,
        verifierSHA256=replay.gate['verifierPin']['sha256'],verifierGateSHA256=digest(replay.gate_raw),
        producerResultPin=replay.gate['resultPin'],startedUTC=datetime.fromtimestamp(STARTED_WALL,timezone.utc).isoformat(),
        endedUTC=datetime.now(timezone.utc).isoformat(),internalElapsedSeconds=replay.elapsed(),
        stageAccounting=replay.gate['stageAccounting'],processControl=replay.gate['processControl'],
        externalRootMustVerifyFullLifetimeAndAllChargedBytes=True,freshStageBudgetGranted=False,
        negativeCretClaim=False,negativeLretClaim=False,negativeQClaim=False,
        wholeQCertified=False,RHCertified=False,GoalComplete=False,positivityCertified=False,
        laterStagesAuthorized=False,autoStage2Dispatched=False,programSettlesIterations=0,
        mathematicalSettlement='PENDING_ROOT_C068',newDirectionProposed=False,
        matrixProductsOrLDLOrInverseRepeated=False,sourceRegenerated=False)

def run(gate_path):
    replay=authorize(gate_path) # no output before exact new gate/once guard
    try:
        result,freeze=metadata(replay)
        status=result.get('status')
        if status!='FIXED_WHOLE_RECIPE_REJECTED':
            need(status in ('PREFIX_NECESSARY_PASS','PREFIX_UNRESOLVED','PREFIX_TECHNICAL_STOP'),
                 'KNOWN_ORIGINAL_TERMINAL_STATUS')
            replay.final_guards()
            report=base_report(replay,'NOT_NEGATIVE_CERTIFICATE')
            report.update(producerStatus=status,coordinateSourcesRead=False,
                logNumericRowsRead=False,negativeCertificateVerified=False,
                reason='No saved strict negative prerequisite certificate; no source/quadratic replay or positivity inference')
        else:
            need(result.get('schema')=='RH_WEIL_WHOLE_PREFIX_RESULT_V1','NEGATIVE_RESULT_SCHEMA')
            need(result.get('prerequisitePassIsWholeProof') is False,'NEGATIVE_SCOPE_NOT_WHOLE_PROOF')
            need(fraction(result['lambdaExact'])==LAMBDA,'RESULT_EXACT_LAMBDA')
            witness=result['witness'];need(type(witness) is dict,'SAVED_NEGATIVE_WITNESS')
            log=validate_log(replay,result,witness)
            source=freeze['sourceMathPins'];replay.pin_map(source,'initial-original-source-math')
            inventory=result['inputs'];need(type(inventory) is dict,'ORIGINAL_INPUT_INVENTORY')
            for name,record in replay.snapshots.items():
                if name in source:
                    need(inventory.get(name)==record,'ORIGINAL_SOURCE_INVENTORY_MATCH')
            # Check every original dynamic input record, not only three packets.
            required=dict(source)
            for key in ('protocolPin','protocolDesignPin','contractPin'):
                pin=freeze[key];required[pin['path']]=pin['sha256']
            required.update(freeze['reviewPins']);required.update(freeze['chargedMetadataPins'])
            required[freeze['executionGatePin']['path']]=freeze['executionGatePin']['sha256']
            need(set(inventory)==set(required),'ORIGINAL_COMPLETE_INVENTORY_KEYS')
            for name,h in required.items():
                need(inventory[name]==replay.snapshots[name] and inventory[name]['sha256']==h,
                     'ORIGINAL_COMPLETE_INVENTORY_HASH_BYTES')
            aa,jj,hh,gg=load_coordinates(replay,source)
            certificate=direct_replay(replay,witness,aa,jj,hh,gg)
            replay.final_guards()
            report=base_report(replay,'NEGATIVE_FIXED_WHOLE_RECIPE_CERTIFICATE_VERIFIED')
            report.update(producerStatus=status,coordinateSourcesRead=True,
                negativeCertificateVerified=True,pivotLog=log,exactWitnessReplay=certificate,
                scope='Saved negative Hpre rejects ONLY the fixed whole sufficient recipe uniformly over valid later Gram; does not establish negative Cret, Lret, Q, RH or Goal completion',
                originalProducerFilesUnmodified=True)
        report['consumedPins']=replay.snapshots
        report['checkerOwnedBytesBeforeReport']=replay.own_bytes()
        replay.check();replay.write(report)
        return report
    except BaseException as error:
        report=base_report(replay,'TERMINAL_REPLAY_TECHNICAL_STOP')
        report.update(negativeCertificateVerified=False,mathematicalSignConclusion=False,
            errorType=type(error).__name__,reason=str(error)[:1500],context=replay.context,
            integerWidthDiagnostic=(width_diagnostic(error) if isinstance(error,IntegerWidthError) else None),
            scope='Unconsumable verifier failure; no retry, replacement direction or positivity inference')
        # One bounded terminal record; never overwrite an already committed report.
        if not replay.report_written:replay.write(report)
        raise

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gate-file',type=Path,required=True);args=parser.parse_args()
    if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
    result=run(args.gate_file)
    print(json.dumps(dict(status=result['status'],checkerResult=str(REPORT),
        mathematicalSettlement='PENDING_ROOT_C068',laterStagesAuthorized=False)))

if __name__=='__main__':main()

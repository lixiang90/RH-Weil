"""Metadata/process controller only: no scientific source or arithmetic replay.

Root charges its externally observed full lifetime as a conservative envelope
of its ONE sequential scientific child, including all controller overhead.
Never adds that envelope to the already enclosed child lifetime a second time.
No stage or retry is dispatched automatically. AST preparation only until gate.
"""
import time
ORIGIN=time.monotonic()
import argparse
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SELF=Path(__file__).resolve()
PREFIX=HERE.parent/'retained-tail-whole-prefix'
OUTER=ROOT/'literature/local/2026-11-01-retained-tail-whole-candidate/run-01'

def need(ok,msg):
    if not ok:raise ValueError(msg)

def utc():return datetime.now(timezone.utc).isoformat()

def digest(raw):return hashlib.sha256(raw).hexdigest()

def load(path):return json.loads(path.read_text(encoding='utf-8'))

def pin(record):
    p=(ROOT/record['path']).resolve()
    need(p.is_relative_to(ROOT) and p.is_file(),'PIN_PATH')
    raw=p.read_bytes();need(digest(raw)==record['sha256'],'PIN_SHA:'+record['path'])
    return p,raw

def save(path,obj):
    raw=(json.dumps(obj,sort_keys=True,ensure_ascii=True,indent=2)+'\n').encode('ascii')
    need(len(raw)<65536,'CONTROLLER_RECORD_CAP')
    with path.open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())

def run(phase):
    need(phase in ('producer','checker'),'PHASE')
    if phase=='producer':
        freeze=HERE/'prefix-execution-freeze.json';f=load(freeze)
        _,gate_raw=pin(f['executionGatePin']);gate=json.loads(gate_raw)
        need(gate['schema']=='RH_WEIL_WHOLE_PREFIX_ROOT_EXECUTION_GATE_V1'
             and gate['status']=='ROOT_EXPLICIT_PREFIX_EXECUTION_APPROVED'
             and gate['authorization']=='ROOT_EXPLICIT_C068_WHOLE_PREFIX_EXECUTION'
             and gate['numericalExecutionAuthorized'] is True,'PRODUCER_ROOT_GATE')
        code=PREFIX/'whole-prerequisite.py'
        need(digest(code.read_bytes())==f['codeSHA256']==gate['codeSHA256'],'PRODUCER_SELF_PIN')
        need(not OUTER.exists(),'WHOLE_ATTEMPT_ALREADY_CLAIMED')
        command=[sys.executable,str(code),'--freeze-file',str(freeze)]
        fixed_maximum=450
    else:
        freeze=HERE/'terminal-replay-gate.json';gate=load(freeze)
        need(gate['schema']=='RH_WEIL_C068_TERMINAL_REPLAY_GATE_V1'
             and gate['authorization']=='ROOT_EXPLICIT_C068_TERMINAL_REPLAY'
             and gate['numericalExecutionAuthorized'] is True,'CHECKER_ROOT_GATE')
        code,_=pin(gate['verifierPin'])
        need(code==HERE/'verify-prefix-terminal.py','CHECKER_PATH')
        command=[sys.executable,str(code),'--gate-file',str(freeze)]
        fixed_maximum=100
    need(gate['contractId']=='C068' and gate['runtimeGoalCreatedAt']==1793085111
         and gate['laterStagesAuthorized'] is False,'SAME_WHOLE_RESPONSIBILITY')
    control=gate['processControl'];p,_=pin(control['controllerPin'])
    need(p==SELF,'CONTROLLER_SELF_PIN')
    cutoff=control['cutoffSeconds']
    need(type(cutoff) is int and 0<cutoff<=fixed_maximum,'CONSERVATIVE_CHILD_CUTOFF')
    need(control['phase']==phase and control['noAutomaticNextProcess'] is True,'PHASE_ONCE_POLICY')
    marker=HERE/(phase+'-launch.json');terminal=HERE/(phase+'-terminal.json')
    out=HERE/(phase+'-stdout.txt');err=HERE/(phase+'-stderr.txt')
    need(not any(p.exists() for p in (marker,terminal,out,err)),'PHASE_ALREADY_ATTEMPTED')
    save(marker,dict(schema='RH_WEIL_C068_PROCESS_LAUNCH_V1',phase=phase,contractId='C068',
        runtimeGoalCreatedAt=1793085111,controllerPID=os.getpid(),startedUTC=utc(),
        authorizationFile=str(freeze.relative_to(ROOT)),authorizationSHA256=digest(freeze.read_bytes()),
        command=command,childCutoffSeconds=cutoff,oneAttemptOnly=True,mayBeRemoved=False))
    started=time.monotonic();started_utc=utc();timed_out=False;output_stop=False
    with out.open('xb') as stdout,err.open('xb') as stderr:
        child=subprocess.Popen(command,cwd=ROOT,stdout=stdout,stderr=stderr)
        while child.poll() is None:
            if time.monotonic()-started>cutoff:
                timed_out=True;child.kill();break
            if out.stat().st_size+err.stat().st_size>131072:
                output_stop=True;child.kill();break
            time.sleep(.2)
        exit_code=child.wait()
        ended=time.monotonic();ended_utc=utc()
        stdout.flush();os.fsync(stdout.fileno());stderr.flush();os.fsync(stderr.fileno())
    if out.stat().st_size+err.stat().st_size>131072:output_stop=True
    files=[]
    for p in (out,err):
        raw=p.read_bytes();files.append(dict(path=str(p.relative_to(ROOT)),bytes=len(raw),sha256=digest(raw)))
    record=dict(schema='RH_WEIL_C068_PROCESS_TERMINAL_V1',terminal=True,phase=phase,
        contractId='C068',runtimeGoalCreatedAt=1793085111,childPID=child.pid,
        childStartedUTC=started_utc,childObservedExitedUTC=ended_utc,
        childLifetimeUpperSeconds=ended-started,controllerElapsedBeforeReceiptSeconds=time.monotonic()-ORIGIN,
        actualControllerFullLifetimeRequiresExternalRootObservation=True,
        exitCode=exit_code,cutoffSeconds=cutoff,timedOut=timed_out,outputCapStop=output_stop,
        files=files,noAutomaticNextProcess=True,wholeQCertified=False,RHCertified=False,GoalComplete=False)
    save(terminal,record)
    print(json.dumps(dict(phase=phase,exitCode=exit_code,terminalReceipt=str(terminal.relative_to(ROOT)),
        childLifetimeUpperSeconds=record['childLifetimeUpperSeconds'],timedOut=timed_out,outputCapStop=output_stop)))
    return 0 if exit_code==0 and not timed_out and not output_stop else 1

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase',choices=['producer','checker'],required=True)
    sys.exit(run(parser.parse_args().phase))

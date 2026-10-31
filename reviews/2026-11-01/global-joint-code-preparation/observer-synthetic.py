"""Isolated Goal42 metadata controls plus harmless Windows Job-list children.

No main/ARM, actual C069 directory, source packet, numerical kernel or scientific
driver is imported/executed. Temporary fixture target is checked before cleanup.
"""
import ast
import ctypes
from ctypes import wintypes
from datetime import datetime,timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import threading
import time

HERE=Path(__file__).resolve().parent
raw=(HERE/"observe-global-once.py").read_bytes()
tree=ast.parse(raw)
names={"need","utc","pack","unique","decode","uint","path","pin","record_pin","save_new",
       "WindowsTree","Capture","child_command","prior_costs","limits_ok","funded_child_window",
       "lifetime_policy","ready_value","final_gate"}
body=[node for node in tree.body if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name in names]
assert len(body)==len(names)
scope={"ctypes":ctypes,"wintypes":wintypes,"datetime":datetime,"timezone":timezone,"hashlib":hashlib,
       "json":json,"math":math,"os":os,"Path":Path,"re":re,"subprocess":subprocess,"sys":sys,
       "threading":threading,"time":time,"GOAL":42,"TARGET":"SYNTHETIC_TARGET",
       "PHASES":("source-produce","source-verify","finite-produce","finite-verify"),
       "BASE":"fictional-code/","CODES":{"source-produce":"source.py","source-verify":"source.py",
                                       "finite-produce":"finite.py","finite-verify":"replay.py"},
       "CAP_MS":{"source":3600000,"finite":3600000,"aggregate":7200000},
       "CAP_BYTES":{"source":48*(1<<20),"finite":16*(1<<20),"aggregate":64*(1<<20)}}
exec(compile(ast.Module(body=body,type_ignores=[]),"AST_SYNTHETIC_OBSERVER_ONLY","exec"),scope)
count=0


def ok(x):
    global count
    assert x
    count+=1


def rejects(fn,part=None):
    global count
    try:fn()
    except BaseException as error:
        assert part is None or part in str(error),(part,str(error))
        count+=1
    else:raise AssertionError("expected rejection")


for x in (-1,True,1.0,"1"):
    rejects(lambda x=x:scope["uint"](x,"fixture"))
rejects(lambda:scope["decode"](b'{"x":1,"x":2}'),"DUPLICATE_JSON")
rejects(lambda:scope["decode"](b'{"x":NaN}'),"NONFINITE_JSON")
costs={"sourceMs":800,"finiteMs":0,"sourceBytes":400000,"finiteBytes":0}
limits={"phaseAllowanceMs":120000,"internalScientificCutoffMs":80000,"externalObserverChildTimeoutMs":90000}
scope["limits_ok"](limits,costs,"source-verify");count+=1
rejects(lambda:scope["limits_ok"](limits|{"phaseAllowanceMs":100000},costs,"source-verify"),"REMAINING_PHASE")
ok(scope["funded_child_window"](limits,10000)==90000)
rejects(lambda:scope["funded_child_window"](limits,10001),"ACTUAL_CHILD_INTERNAL")
rejects(lambda:scope["funded_child_window"](limits,500,500),"ACTUAL_CHILD_INTERNAL")
ok(scope["funded_child_window"](limits|{"phaseAllowanceMs":130000,"externalObserverChildTimeoutMs":100000},500,500)==99500)
rejects(lambda:scope["funded_child_window"](limits,60000,1000),"ACTUAL_CHILD_INTERNAL")
for arguments,expected in (((301,1,True,False,True),(301,True)),
                           ((301,1,True,True,True),(301,True)),
                           ((301,1,False,False,True),(None,False)),
                           ((2,1,True,True,True),(1,True)),
                           ((0,0,False,False,False),(1,True)),
                           ((2,0,True,False,True),(2,True))):
    ok(scope["lifetime_policy"](*arguments)==expected)
prior={"schema":"RH_WEIL_GLOBAL_OBSERVER_PRIOR_ACCOUNTING_V1",
       "status":"ROOT_VERIFIED_ALL_PRIOR_SCIENTIFIC_PROCESSES_TERMINAL","targetId":"SYNTHETIC_TARGET",
       "runtimeGoalCreatedAt":42,"contractId":"C069","noLiveScientificProcesses":True,
       "sourceConsumedUpperMs":800,"finiteConsumedUpperMs":0,"sourceChargedUpperBytes":400000,
       "finiteChargedUpperBytes":0,"phaseLifetimes":[{"phase":"source-produce","fullObservedUpperMs":800,
            "exitCode":0,"enclosedChildAddedAgain":False}]}
ok(scope["prior_costs"](prior,"source-verify")==costs)
rejects(lambda:scope["prior_costs"](prior|{"sourceConsumedUpperMs":0},"source-verify"),"ALL_PRIOR")
rejects(lambda:scope["prior_costs"](prior,"finite-produce"),"EXACT_PRIOR_PHASES")

outcomes=[]
with tempfile.TemporaryDirectory(prefix="synthetic-observer-",dir=HERE) as temporary:
    root=Path(temporary).resolve()
    assert root.is_relative_to(HERE.resolve()) and root.name.startswith("synthetic-observer-")
    for name in ("../escape","/absolute","C:/outside","a\\b","a//b"):
        rejects(lambda name=name:scope["path"](root,name))
    (root/"metadata").mkdir()
    scope["save_new"](root/"metadata/once.json",{"fixture":42})
    rejects(lambda:scope["save_new"](root/"metadata/once.json",{"fixture":43}))
    p=scope["record_pin"](root,root/"metadata/once.json")
    ok(scope["decode"](scope["pin"](root,p))=={"fixture":42})
    ready_arm={"phaseLimits":limits,"externalOutputPaths":[{"path":"metadata/stdout.txt","maxBytes":1000}],
               "armIdentity":"SYNTHETIC_NONCE_0042","childCodePin":p,"_armPin":p,"rootArmGatePin":p,
               "rootAdmissionPin":p,"priorAccountingPin":p,"_claimPin":p}
    ready=scope["ready_value"](ready_arm,"source-produce",p)
    ok(ready["observerPID"]==os.getpid() and ready["phase"]=="produce" and ready["codePin"]==p)
    final_ready=scope["ready_value"](ready_arm,"finite-verify",p)
    ok(final_ready["schema"]=="RH_WEIL_GLOBAL_FINITE_REPLAY_ROOT_ATTEMPT_V1"
       and final_ready["currentStage"]=="stage-02-finite-checker")
    command=scope["child_command"](root,"source-verify","metadata/final.json")
    ok(command[-3:]==["verify","--root-freeze-file","metadata/final.json"])
    command=scope["child_command"](root,"finite-produce","metadata/final.json")
    ok(command[-2:]==["--root-freeze-file",str(root/"metadata/final.json")])
    # Synthetic READY first, then ROOT-written final freeze/gate: no assumed PID.
    ready_path=root/"metadata/ready.json";scope["save_new"](ready_path,ready)
    ready_pin=scope["record_pin"](root,ready_path)
    gate={"schema":"RH_WEIL_GLOBAL_SOURCE_PHASE_ROOT_GATE_V1",
          "status":"ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION_APPROVED","runtimeGoalCreatedAt":42,
          "contractId":"C069","targetId":"SYNTHETIC_TARGET","contractPin":p,"launchPin":ready_pin,
          "controllerPin":p,"freezeIdentity":ready_arm["armIdentity"],"phaseLimits":limits,
          "externalOutputPaths":ready_arm["externalOutputPaths"],"phase":"produce"}
    prior_path=root/"metadata/prior.json"
    scope["save_new"](prior_path,{"sourceObservedUpperMs":800,"aggregateObservedUpperMs":800,
                                "sourceChargedUpperBytes":400000,"aggregateChargedUpperBytes":400000})
    gate["priorAccountingPin"]=scope["record_pin"](root,prior_path)
    gate["chargedMetadataPins"]={p["path"]:p}
    gate_path=root/"metadata/gate.json";scope["save_new"](gate_path,gate)
    freeze=gate|{"schema":"RH_WEIL_GLOBAL_SOURCE_PHASE_FREEZE_V1",
                 "authorization":"ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION",
                 "rootGatePin":scope["record_pin"](root,gate_path)}
    freeze_path=root/"metadata/freeze.json";scope["save_new"](freeze_path,freeze)
    arm=ready_arm|{"finalFreezeRelativePath":"metadata/freeze.json","finalRootGateRelativePath":"metadata/gate.json",
                   "contractPin":p,"_costs":costs,"_metadataPins":{},"_claimPin":p}
    scope["final_gate"](root,arm,"source-produce",ready_pin);count+=1
    rejects(lambda:scope["final_gate"](root,arm|{"externalOutputPaths":[]},"source-produce",ready_pin),"SOURCE_READY")
    fgate={"schema":"RH_WEIL_GLOBAL_FINITE_ROOT_GATE_V1","authorization":"ROOT_EXPLICIT_C069_GLOBAL_FINITE_EXECUTION",
           "numericalExecutionAuthorized":True,"runtimeGoalCreatedAt":42,"contractId":"C069","targetId":"SYNTHETIC_TARGET",
           "contractPin":p,"externalAttemptPin":ready_pin,"launchNonce":arm["armIdentity"],"codePin":p,
           "externalRuntimePaths":[x["path"] for x in arm["externalOutputPaths"]],"chargedMetadataPins":[p],
           "budget":{"producerDeadlineSeconds":80,"sourceConsumedUpperSeconds":1,"finitePriorUpperSeconds":0,
                     "sourceConsumedOutputBytes":400000,"finitePriorOutputBytes":0,"externalRuntimeChargedUpperBytes":1000}}
    fgate_path=root/"metadata/finite-gate.json";scope["save_new"](fgate_path,fgate)
    ffreeze=fgate|{"schema":"RH_WEIL_GLOBAL_FINITE_FREEZE_V1","rootGatePin":scope["record_pin"](root,fgate_path)}
    ffreeze_path=root/"metadata/finite-freeze.json";scope["save_new"](ffreeze_path,ffreeze)
    farm=arm|{"finalFreezeRelativePath":"metadata/finite-freeze.json","finalRootGateRelativePath":"metadata/finite-gate.json"}
    scope["final_gate"](root,farm,"finite-produce",ready_pin);count+=1
    ffreeze["budget"]["externalRuntimeChargedUpperBytes"]=999
    ffreeze_path.write_bytes(scope["pack"](ffreeze))  # Synthetic fixture only, not an immutable execution gate.
    rejects(lambda:scope["final_gate"](root,farm,"finite-produce",ready_pin),"FINITE_EXTERNAL_OUTPUT_MAXIMA")
    # The following tiny child fixtures are OS mechanism tests, never source math.
    script=root/"fixture-child.py"
    script.write_text("import os,sys,time,subprocess\nmode=sys.argv[1]\n"
        "if mode=='normal':\n print('HELLO_FIXTURE42',flush=True); print('ERR_FIXTURE42',file=sys.stderr,flush=True)\n"
        "elif mode=='sleep':\n time.sleep(30)\n"
        "elif mode=='spam':\n print('Z'*20000,flush=True);time.sleep(30)\n"
        "elif mode=='grandchild':\n p=subprocess.Popen([sys.executable,'-c','import time;time.sleep(30)']);print('GRANDCHILD',p.pid,flush=True);time.sleep(30)\n",
        encoding="utf-8")
    for mode in ("normal","sleep","spam","grandchild"):
        directory=root/mode;directory.mkdir()
        stop=threading.Event();caps=[];job=None
        reason=None;maximum_processes=0
        started=time.monotonic()
        try:
            caps=[scope["Capture"](directory/"stdout.txt",1000 if mode=='spam' else 4096,stop),
                  scope["Capture"](directory/"stderr.txt",4096,stop)]
            with open(os.devnull,"rb") as stdin:
                job=scope["WindowsTree"]([sys.executable,str(script),mode],root,stdin.fileno(),caps[0].write_fd,caps[1].write_fd)
                for capture in caps:capture.inherited()
                pid=job.pid;job.resume()
                while True:
                    total,active=job.counts();maximum_processes=max(maximum_processes,total)
                    if stop.is_set():reason='capture-cap';break
                    unexpected,members=job.unexpected_descendants()
                    if unexpected:reason='descendant';break
                    if job.poll() is not None:break
                    if time.monotonic()-started>(0.3 if mode=='sleep' else 3):reason='timeout';break
                    time.sleep(0.01)
                if reason is not None:job.kill()
                code=job.wait(5);job.kill();job.wait_empty(5)
                ok(job.counts()[1]==0)
                for capture in caps:capture.finish()
                if mode=='normal':
                    if not (code==0 and reason is None):
                        raise AssertionError({"fixture":mode,"code":code,"reason":reason,
                            "maxProcesses":maximum_processes,"captures":[(directory/n).read_bytes()[:4096].decode("utf-8",errors="replace") for n in ("stdout.txt","stderr.txt")]})
                    ok(code==0 and reason is None)
                    ok((directory/"stdout.txt").read_bytes()==b'HELLO_FIXTURE42\r\n'
                       or (directory/"stdout.txt").read_bytes()==b'HELLO_FIXTURE42\n')
                elif mode=='sleep':ok(reason=='timeout' and code!=0)
                elif mode=='spam':ok(reason=='capture-cap' and caps[0].saved_bytes==1000 and caps[0].read_bytes>1000)
                else:ok(reason=='descendant' and maximum_processes>=2)
                outcomes.append({"fixture":mode,"reason":reason,"exitCode":code,
                                 "maximumJobProcesses":maximum_processes,"activeAfterKill":0,
                                 "stdoutBytesSaved":caps[0].saved_bytes,"stderrBytesSaved":caps[1].saved_bytes})
        finally:
            if job is not None:
                try:job.kill();job.wait(5);job.wait_empty(5)
                finally:job.close()
            for capture in caps:
                try:capture.finish()
                except BaseException:pass

result={"status":"AST_ISOLATED_OBSERVER_METADATA_AND_WINDOWS_JOB_CONTROLS_PASS",
        "observerSHA256":hashlib.sha256(raw).hexdigest(),"controls":count,
        "syntheticGoal":42,"actualARMOrC069OrScientificNamespaceCreated":False,
        "actualScientificSourceOrKernelReadOrExecuted":False,"observerImported":False,
        "nativeWindowsJobListExecuted":True,"harmlessOSFixtures":outcomes,
        "temporaryDirectoryScopeCheckedBeforeCleanup":True,"dataExecutionAuthorized":False}
(HERE/"observer-synthetic-result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))

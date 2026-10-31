"""AST-isolated controller controls in an artificial TemporaryDirectory.

Never import source-stage-controller; never call main, code_module on real
science, a root execution gate, an actual C069 contract or the real namespace.
The control namespace has synthetic target, Goal42 and synthetic-once/run.
"""
import ast
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import tempfile
import time
import types


HERE=Path(__file__).resolve().parent
raw=(HERE/"source-stage-controller.py").read_bytes()
tree=ast.parse(raw)
names={"need","utc","packed","unique","decode","unsigned","relative_file","pin_shape",
       "read_pin","hash_pin","atomic_new","check_header","phase_claim","accounting",
       "Budget","packet_keys","Packet","code_module","width_diagnostic"}
body=[x for x in tree.body if isinstance(x,(ast.ClassDef,ast.FunctionDef)) and x.name in names]
assert len(body)==len(names)
scope={"datetime":datetime,"timezone":timezone,"hashlib":hashlib,"json":json,"math":math,
       "os":os,"Path":Path,"re":re,"time":time,"types":types,
       "PROCESS_STARTED":time.monotonic(),"GOAL":42,"TARGET":"SYNTHETIC_TARGET",
       "OUTER_REL":"synthetic-once/run","SOURCE_REL":"synthetic-once/run/source",
       "PACKET_REL":"synthetic-once/run/source/joint-centers.jsonl",
       "SOURCE_MS":3600000,"SOURCE_BYTES":48*(1<<20),"AGG_MS":7200000,"AGG_BYTES":64*(1<<20),
       "TERMINAL_RESERVE":262144,"EMERGENCY_MAX":131072,
       "PARAMETERS":{"syntheticN":4,"oneAttempt":True,"externalTerminalReserveMs":20000,
                     "packetOrder":["CX","FX","FY","XY","YY"]}}
exec(compile(ast.Module(body=body,type_ignores=[]),"AST_SYNTHETIC_CONTROLLER_ONLY","exec"),scope)
count=0


def ok(value):
    global count
    assert value
    count+=1


def rejects(fn,part=None):
    global count
    try:
        fn()
    except BaseException as error:
        assert part is None or part in str(error),(part,str(error))
        count+=1
    else:
        raise AssertionError("expected rejection")


for x in (-1,True,1.0,"1"):
    rejects(lambda x=x:scope["unsigned"](x,"fixture"))
ok(scope["unsigned"](0,"fixture")==0)
for text in (b'{"x":1,"x":2}',b'{"x":NaN}'):
    rejects(lambda text=text:scope["decode"](text))

with tempfile.TemporaryDirectory(prefix="synthetic-controller-",dir=HERE) as temporary:
    root=Path(temporary).resolve()
    # Before automatic recursive cleanup, verify this exact target is our own
    # generated fixture inside the writable preparation directory.
    assert root.is_relative_to(HERE.resolve()) and root.name.startswith("synthetic-controller-")
    for path in ("../escape","/absolute","C:/outside","a//b","a/./b","a\\b",""):
        rejects(lambda path=path:scope["relative_file"](root,path))
    ok(scope["relative_file"](root,"fixture/input.bin")==root/"fixture"/"input.bin")
    (root/"fixture").mkdir()
    content=b"SYNTHETIC_METADATA_ONLY\n"
    (root/"fixture/input.bin").write_bytes(content)
    pin={"path":"fixture/input.bin","bytes":len(content),"sha256":hashlib.sha256(content).hexdigest()}
    ok(scope["read_pin"](root,pin)==content)
    rejects(lambda:scope["read_pin"](root,dict(pin,bytes=1)),"PIN_SIZE")
    rejects(lambda:scope["read_pin"](root,dict(pin,sha256="0"*64)),"PIN_HASH")
    scope["hash_pin"](root,pin,lambda:None);count+=1
    scope["atomic_new"](root/"fixture/once.json",b"first")
    rejects(lambda:scope["atomic_new"](root/"fixture/once.json",b"second"))
    ok((root/"fixture/once.json").read_bytes()==b"first")
    common={"phase":"produce","runtimeGoalCreatedAt":42,"contractId":"C069",
            "targetId":"SYNTHETIC_TARGET","outerRelativePath":"synthetic-once/run",
            "parameters":scope["PARAMETERS"],"freezeIdentity":"SYNTHETIC_IDENTITY_0001",
            "rootAdmissionNonce":"SYNTHETIC_IDENTITY_0001"}
    fields=("contractPin","controllerPin","producerPin","verifierPin","protocolPin","sourcePins",
            "mathPins","reviewPins","launchPin","admissionPin","priorAccountingPin","chargedMetadataPins",
            "externalOutputPaths","phaseLimits","producerResultPin","producerTerminalPin","outerClaimPin")
    freeze=common|dict.fromkeys(fields,None)|{"schema":"RH_WEIL_GLOBAL_SOURCE_PHASE_FREEZE_V1",
                "authorization":"ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION"}
    gate=common|dict.fromkeys(fields,None)|{"schema":"RH_WEIL_GLOBAL_SOURCE_PHASE_ROOT_GATE_V1",
              "status":"ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION_APPROVED"}
    scope["check_header"](freeze,gate,"produce");count+=1
    broken=freeze|{"parameters":dict(scope["PARAMETERS"],syntheticN=4.0)}
    rejects(lambda:scope["check_header"](broken,gate,"produce"),"TARGET_GOAL_PARAMETERS")
    rejects(lambda:scope["check_header"](freeze,gate,"verify"),"PHASE_MATCH")
    output,early=scope["phase_claim"](root,freeze,"produce","0"*64,"1"*64)
    ok(output==root/"synthetic-once/run/source/produce" and len(early)==2)
    immutable=(root/"synthetic-once/run/run-lock.json").read_bytes()
    rejects(lambda:scope["phase_claim"](root,freeze,"produce","0"*64,"1"*64))
    ok((root/"synthetic-once/run/run-lock.json").read_bytes()==immutable)
    outerpin={"path":"synthetic-once/run/run-lock.json","bytes":len(immutable),
              "sha256":hashlib.sha256(immutable).hexdigest()}
    voutput,vearly=scope["phase_claim"](root,freeze|{"outerClaimPin":outerpin},"verify","2"*64,"1"*64)
    ok(voutput.name=="verify" and len(vearly)==1)
    rejects(lambda:scope["phase_claim"](root,freeze|{"outerClaimPin":outerpin},"verify","2"*64,"1"*64))
    # Producer-phase budget must reject verify artifacts. Use the verify-phase
    # budget for this intentionally two-claim fixture; count both claims early.
    prior=[0,0,0,0,{}]
    limits={"phaseAllowanceMs":120000,"internalScientificCutoffMs":80000,
            "externalObserverChildTimeoutMs":90000}
    budget=scope["Budget"](root,"verify",voutput,prior,limits,0,
                            sum(x[1] for x in early+vearly),[])
    ok(budget.generated>sum(x[1] for x in early+vearly))
    before=budget.generated
    budget.write("fixture.json",{"value":1})
    # The whitelist must reject arbitrary new numerical products.
    rejects(lambda:budget.poll(force=True),"UNACCOUNTED_SOURCE_OUTPUT")
    (voutput/"fixture.json").unlink()  # Synthetic-only fixture cleanup never refunds the budget.
    ok(budget.generated>before)
    after=budget.generated
    budget.progress("synthetic-stage",fixture=1)
    budget.last_progress=0
    budget.poll(force=True)
    ok(budget.generated>after and not (voutput/"progress.json.tmp").exists())
    rejects(lambda:budget.charge(scope["SOURCE_BYTES"]),"OUTPUT_WRITE_CAP")
    saved=budget.internal;budget.internal=0
    rejects(lambda:budget.poll(),"INTERNAL_SCIENTIFIC_DEADLINE")
    budget.internal=saved
    scope["packet_keys"]=lambda:iter([("CX",0,0),("CX",0,2)])
    packet=scope["Packet"](root,budget)
    packet.emit(["CX",0,0,"0"])
    rejects(lambda:packet.emit(["CX",0,2,"00"]),"PACKET_CANONICAL_INTEGER")
    packet.close()
    ok(packet.rows==1 and packet.path.exists() and not packet.final.exists())
    ok(packet.path.read_bytes()==b'["CX",0,0,"0"]\n')
    rejects(packet.finish,"PACKET_COMPLETE_ROWS")
    # Code bytes are the authenticated input, not a later pathname reread.
    fake=root/"fixture/new-module.py";fake.write_bytes(b"x=18\n")
    module=scope["code_module"](b"x=17\n",fake,"synthetic_module")
    ok(module.x==17)

base={"schema":"RH_WEIL_ROOT_OBSERVED_GLOBAL_ACCOUNTING_V1","status":"ROOT_VERIFIED_NO_RETRY_ACCOUNTING",
      "targetId":"SYNTHETIC_TARGET","runtimeGoalCreatedAt":42,"outerRelativePath":"synthetic-once/run",
      "sourceObservedUpperMs":0,"aggregateObservedUpperMs":0,"sourceChargedUpperBytes":0,
      "aggregateChargedUpperBytes":0,"phaseLifetimes":[],"outerPreviouslyCreated":False,
      "chargedPathBindings":{}}
ok(scope["accounting"](base,"produce")[:4]==(0,0,0,0))
terminal={"internalElapsedCeilingMs":500,"sourceChargeUpperIncludingTerminalReserve":400000,
          "aggregateChargeUpperIncludingTerminalReserve":400000}
life={"phase":"source-produce","fullObservedUpperMs":800,"enclosedKernelAddedAgain":False,
      "exitCode":0,"terminalPin":{"fixture":True}}
saved=base|{"sourceObservedUpperMs":800,"aggregateObservedUpperMs":800,
            "sourceChargedUpperBytes":400000,"aggregateChargedUpperBytes":400000,
            "phaseLifetimes":[life],"outerPreviouslyCreated":True,"producerTerminalPin":{"fixture":True}}
ok(scope["accounting"](saved,"verify",terminal)[:4]==(800,800,400000,400000))
rejects(lambda:scope["accounting"](saved|{"sourceObservedUpperMs":0},"verify",terminal),"SUM_ALL_PROCESS")
rejects(lambda:scope["accounting"](saved|{"sourceChargedUpperBytes":0},"verify",terminal),"NO_BYTE_RESET")
rejects(lambda:scope["accounting"](saved|{"phaseLifetimes":[life,life]},"verify",terminal),"NO_DUPLICATE")
rejects(lambda:scope["accounting"](saved|{"aggregateObservedUpperMs":0},"verify",terminal),"NO_AGGREGATE_RESET")

def diagnostic_fixture():
    center=1 << 270
    scope["need"](False,"FINAL_CENTER_INTEGER_WIDTH")

try:
    diagnostic_fixture()
except ValueError as error:
    diag=scope["width_diagnostic"](error)
    ok(diag["mathematicalSignConclusion"] is False and diag["values"][0]["actualBitLength"]==271)
    ok(diag["values"][0]["value"]=="0x"+format(1 << 270,"x"))

result={"status":"AST_ISOLATED_SYNTHETIC_SOURCE_CONTROLLER_CONTROLS_PASS",
        "controllerSHA256":hashlib.sha256(raw).hexdigest(),"controls":count,
        "artificialTemporaryDirectoryOnly":True,"syntheticGoal":42,
        "actualNamespaceCreated":False,"actualRootGateContractOrSourceRead":False,
        "controllerImported":False,"sourceProducerOrVerifierImported":False,
        "actualSourceRowGramSolveComputed":False,"dataExecutionAuthorized":False}
(HERE/"source-controller-synthetic-result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))

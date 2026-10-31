#!/usr/bin/env python3
"""Metadata-only C069 first-source admission builder; never launches science.

plan is read-only. Only ROOT may invoke either writing command, supplying the
explicit flag and its own immutable authorization/live-observation records.
This module never imports any scientific/observer/controller implementation.
"""
import argparse
import ast
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[3]
BASE = "reviews/2026-11-01/global-joint-code-preparation/"
EXEC = "reviews/2026-11-01/global-joint-execution/"
META = EXEC + "source-produce"
SCIENCE = "literature/local/2026-11-01-directional-remainder-whole/run-01"
OBSERVER = "literature/local/2026-11-01-directional-remainder-whole-observer/run-01"
PHASE_DIR = OBSERVER + "/source-produce"
CONTRACT = "goals/contracts/C069-global-exact-directional-whole.md"
CLOSURE = BASE + "root-code-closure.json"
GOAL = 1793085111
TARGET = "RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1"
RESERVE_BYTES = 1048576
LIMITS = {"phaseAllowanceMs":1500000,
          "externalObserverChildTimeoutMs":1380000,
          "internalScientificCutoffMs":1200000}
ARM_WAIT_MS = 60000
PARAMETERS = {
    "N":448, "degree":2046, "coefficientBits":8192, "contractionBits":1024,
    "rawBits":256, "nativeArithmeticPower":-230, "packetRows":401856,
    "packetOrder":["CX", "FX", "FY", "XY", "YY"], "oneAttempt":True,
    "sourceCapMs":3600000, "sourceCapBytes":50331648,
    "aggregateCapMs":7200000, "aggregateCapBytes":67108864,
    "terminalReserveBytes":262144, "externalTerminalReserveMs":20000,
    "packetCopyAllowed":False, "YArrayOutputAllowed":False,
}
EXPECTED_CODES = {
    "source-model.py":(27057,"89bb4eb23264b6f7d1bd56459e2d7825b94ec5a02e5ff7c36e6cc0bfa1237975"),
    "verify-source-model.py":(26778,"2b1c1de335e2412c2f6e1cec7a219f3bd496561df6f4d134a5c87ea42a7603db"),
    "source-stage-controller.py":(36959,"0188ebfe2a0565bcfa53687a82b4dad068b57aae4413d3ff2aed18f8e7a7c9d9"),
    "finite-whole-consumer.py":(47909,"6919ea1306ba9539520851634f0fa68980499a479bd529e73cf4b36a5116ab17"),
    "independent-finite-checker.py":(36234,"4cdbc6fcb9ae52cf1766ddbd71bf5e7f579a91f7d331939779448c9075539602"),
    "verify-finite-augmented.py":(8210,"3ef31ca2255ed7a0aa4bc17cac979d49f93c95e43fb3ca18c8a67bd95f0ba6f9"),
    "finite-independent-inputs.py":(8400,"05bb27e4fb457aa29d7cae57115260dc4ca716d4899f1019feea274876cf5a97"),
    "observe-global-once.py":(44215,"88d54d68d5119aff6eacc6581a3de56d53f9121ffacc3a6c17e7f87df8c4637d"),
    "runtime-protocol.md":(8747,"fe70954d6716290bc5b8421fa236d775aefb99e3f3819d777ec72e9ca89c7161"),
}
EXTERNAL = [{"path":PHASE_DIR+"/"+name,"maxBytes":maximum} for name,maximum in
            (("stdout.txt",16384),("stderr.txt",16384),("child.json",8192),
             ("terminal.json",131072),("root-observed.json",131072))]
PATHS = {name:META+"/"+name+".json" for name in
         ("source-prior", "observer-prior", "source-admission", "observer-admission",
          "prepared-context", "observer-arm-root-gate", "observer-arm")}
FINAL_GATE = PHASE_DIR+"/final-root-gate.json"
FINAL_FREEZE = PHASE_DIR+"/final-freeze.json"
READY = PHASE_DIR+"/ready.json"
CLAIM = PHASE_DIR+"/claim.json"
AUTH_SCHEMA = "RH_WEIL_C069_ROOT_SOURCE_METADATA_AUTHORIZATION_V1"
LIVE_SCHEMA = "RH_WEIL_C069_OBSERVER_LIVE_ROOT_OBSERVATION_V1"
RESERVE_SCHEMA = "RH_WEIL_C069_ROOT_ADMINISTRATIVE_RESERVE_PLAN_V1"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def packed(value):
    return (json.dumps(value,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n").encode("ascii")


def unique(items):
    out = {}
    for key,value in items:
        need(key not in out,"DUPLICATE_JSON_KEY")
        out[key] = value
    return out


def decode(raw):
    return json.loads(raw,object_pairs_hook=unique,
                      parse_constant=lambda _:need(False,"NONFINITE_JSON"))


def path(name):
    need(type(name) is str and name and ":" not in name and "\\" not in name
         and all(p not in ("", ".", "..") for p in name.split("/")),"CANONICAL_RELATIVE_PATH")
    result = ROOT.joinpath(*name.split("/")).resolve()
    need(result.is_relative_to(ROOT),"PATH_OUTSIDE_WORKSPACE")
    return result


def byte_pin(name, raw):
    path(name)
    return {"path":name,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}


def hash_file(name):
    """Opaque byte hashing only, including the four large scientific inputs."""
    file = path(name)
    need(file.is_file(),"MISSING_PINNED_FILE:"+name)
    digest,size = hashlib.sha256(),0
    with file.open("rb") as handle:
        for chunk in iter(lambda:handle.read(1 << 20),b""):
            digest.update(chunk)
            size += len(chunk)
    need(file.stat().st_size == size,"FILE_CHANGED_DURING_HASH:"+name)
    return {"path":name,"bytes":size,"sha256":digest.hexdigest()}


def pin_shape(pin):
    need(type(pin) is dict and set(pin) == {"path","bytes","sha256"},"PIN_SHAPE")
    path(pin["path"])
    need(type(pin["bytes"]) is int and pin["bytes"] >= 0,"PIN_BYTES")
    need(type(pin["sha256"]) is str and re.fullmatch("[0-9a-f]{64}",pin["sha256"]),"PIN_SHA256")


def read_pin(pin, maximum=4*(1 << 20)):
    pin_shape(pin)
    need(pin["bytes"] <= maximum,"METADATA_PIN_TOO_LARGE")
    raw = path(pin["path"]).read_bytes()
    need(byte_pin(pin["path"],raw) == pin,"METADATA_PIN_CHANGED:"+pin["path"])
    return raw


def read_json(name):
    pin = hash_file(name)
    return decode(read_pin(pin)),pin


def scope():
    return {"runtimeGoalCreatedAt":GOAL,"contractId":"C069","targetId":TARGET}


def same_scope(obj):
    need(type(obj.get("runtimeGoalCreatedAt")) is int
         and all(obj.get(k) == v for k,v in scope().items()),"SAME_RUNTIME_GOAL_C069_TARGET_REQUIRED")


def add_pins(destination, pins):
    for name,pin in pins.items():
        pin_shape(pin)
        need(name == pin["path"],"CHARGED_PIN_PATH_KEY")
        need(not path(name).is_relative_to(path(SCIENCE)),"METADATA_INSIDE_SCIENTIFIC_OUTER")
        need(name not in {x["path"] for x in EXTERNAL},"METADATA_EXTERNAL_RESERVE_OVERLAP")
        need(name not in destination or destination[name] == pin,"INCONSISTENT_DUPLICATE_PIN")
        destination[name] = pin


def literal_assignment(tree, name):
    matches = [node.value for node in tree.body if isinstance(node,ast.Assign)
               and any(isinstance(t,ast.Name) and t.id == name for t in node.targets)]
    need(len(matches) == 1,"EXACT_STATIC_ASSIGNMENT:"+name)
    return ast.literal_eval(matches[0])


def frozen_assets():
    code = {}
    for name,(size,sha) in EXPECTED_CODES.items():
        actual = hash_file(BASE+name)
        need(actual["bytes"] == size and actual["sha256"] == sha,"ACTUAL_FINAL_CODE:"+name)
        code[name] = actual
    closure,closure_pin = read_json(CLOSURE)
    need(closure.get("status") == "CODE_PREPARATION_CLOSED_ELIGIBLE_FOR_NEW_RESPONSIBILITY_ADMISSION"
         and closure.get("runtimeGoalCreatedAt") == GOAL
         and closure.get("codePins") == list(code.values()),"ACTUAL_FINAL_CODE_CLOSURE")
    # Parse only two literal maps in the hash-fixed controller, never import it.
    tree = ast.parse(read_pin(code["source-stage-controller.py"]).decode("utf-8"))
    data_hashes = literal_assignment(tree,"DATA_PINS")
    math_hashes = literal_assignment(tree,"MATH_PINS")
    need(len(data_hashes) == 4 and len(math_hashes) == 6,"EXACT_INPUT_MAP_COUNTS")
    source_pins,math_pins = {},{}
    for mapping,destination in ((data_hashes,source_pins),(math_hashes,math_pins)):
        for name,sha in mapping.items():
            actual = hash_file(name)
            need(actual["sha256"] == sha,"FROZEN_INPUT_BYTES:"+name)
            destination[name] = actual
    controller = code["source-stage-controller.py"]
    producer = code["source-model.py"]
    verifier = code["verify-source-model.py"]
    protocol = code["runtime-protocol.md"]
    observer = code["observe-global-once.py"]
    vector = [p["sha256"] for p in (controller,producer,verifier)]
    reviews,arm_reviews = [],[]
    for role,owner,name in (("math","/root","root-consumed.md"),
                            ("protocol","/root/global_independent_verifier","observer-final-protocol-review.md")):
        pin = hash_file(BASE+name)
        raw = read_pin(pin)
        need(owner.encode("utf-8") in raw
             and all(sha.encode("ascii") in raw for sha in vector+[protocol["sha256"],observer["sha256"]]),
             "FULL_SHA_AND_OWNER_REVIEW_TEXT:"+name)
        reviews.append({"role":role,"owner":owner,"pin":pin,"approvedCodeSHA256":vector,
                        "approvedProtocolSHA256":protocol["sha256"],
                        "approvedObserverSHA256":observer["sha256"]})
        arm_reviews.append({"role":role,"owner":owner,"pin":pin,
                            "observerSHA256":observer["sha256"],"childSHA256":controller["sha256"]})
    contract_pin = hash_file(CONTRACT)
    contract_raw = read_pin(contract_pin)
    need(b"C069" in contract_raw and str(GOAL).encode() in contract_raw
         and TARGET.encode() in contract_raw,"GENUINE_SAME_GOAL_C069_CONTRACT")
    return {"codePins":code,"codeClosurePin":closure_pin,"contractPin":contract_pin,
            "controllerPin":controller,"producerPin":producer,"verifierPin":verifier,
            "protocolPin":protocol,"observerCodePin":observer,"sourcePins":source_pins,
            "mathPins":math_pins,"reviewPins":reviews,"armReviewPins":arm_reviews}


def root_authorization(name, assets):
    auth,auth_pin = read_json(name)
    need(not path(name).is_relative_to(path(META)),"ROOT_AUTH_MUST_PREEXIST_OUTSIDE_BUILDER_DIRECTORY")
    need(auth.get("schema") == AUTH_SCHEMA
         and auth.get("status") == "ROOT_AUTHORIZED_ONE_SOURCE_PRODUCE_METADATA_GRAPH","ROOT_METADATA_AUTHORIZATION_REQUIRED")
    same_scope(auth)
    need(auth.get("rootRuntimeGoalCheckedActive") is True
         and auth.get("codePreparationActualFinalVerified") is True,"FRESH_ROOT_GOAL_AND_PUBLICATION_OBSERVATION_REQUIRED")
    need(auth.get("contractPin") == assets["contractPin"]
         and auth.get("codeClosurePin") == assets["codeClosurePin"],"ROOT_AUTH_EXACT_CONTRACT_AND_CLOSURE")
    nonce = auth.get("rootAdmissionNonce")
    need(type(nonce) is str and re.fullmatch("[A-Za-z0-9_-]{16,128}",nonce),"NEW_ROOT_NONCE_REQUIRED")
    reserve_pin = auth["rootAdministrativeReservePlanPin"]
    reserve = decode(read_pin(reserve_pin))
    same_scope(reserve)
    need(reserve.get("schema") == RESERVE_SCHEMA
         and reserve.get("status") == "ROOT_PREPAID_CURRENT_C069_MUTABLE_ADMINISTRATIVE_OUTPUTS"
         and type(reserve.get("prechargedBytes")) is int
         and reserve["prechargedBytes"] == RESERVE_BYTES
         and reserve.get("nonRefundable") is True,"ROOT_PREPAID_ADMINISTRATIVE_PLAN_REQUIRED")
    # Root/auditor supplies its exact mutable-path policy and cumulative ledger;
    # this builder neither pins mutable STATE nor invents its accounting evidence.
    need(type(reserve.get("mutablePathPolicy")) in (dict,list)
         and bool(reserve["mutablePathPolicy"])
         and type(reserve.get("cumulativeWritePolicy")) in (dict,str)
         and bool(reserve["cumulativeWritePolicy"]),"ROOT_RESERVE_DISJOINT_PATH_AND_CUMULATIVE_POLICY_REQUIRED")
    extras = auth.get("extraChargedMetadataPins",{})
    need(type(extras) is dict,"EXTRA_CHARGED_METADATA_MAP")
    charged = {auth_pin["path"]:auth_pin,reserve_pin["path"]:reserve_pin,
               assets["contractPin"]["path"]:assets["contractPin"]}
    add_pins(charged,extras)
    for pin in charged.values():
        need(pin["path"] not in ("goals/STATE.json",),"MUTABLE_STATE_CANNOT_BE_PINNED")
        need(not path(pin["path"]).is_relative_to(path(OBSERVER)),"NEW_ROOT_METADATA_OUTSIDE_OBSERVER_OUTER")
        read_pin(pin)
    for name in (EXEC+"build-source-admission.py",EXEC+"builder-notes.md"):
        pin = hash_file(name)
        add_pins(charged,{name:pin})
    return auth,auth_pin,reserve_pin,charged


def new_record(records, label, value):
    raw = packed(value)
    need(len(raw) <= 262144,"BOUNDED_NEW_METADATA")
    name = PATHS[label]
    records[name] = raw
    return byte_pin(name,raw)


def initial_absence():
    for name in (SCIENCE,OBSERVER,META):
        need(not path(name).exists(),"FIRST_ATTEMPT_PATH_MUST_BE_ABSENT:"+name)


def prepare_graph(assets, auth_name):
    initial_absence()
    auth,auth_pin,reserve_pin,charged = root_authorization(auth_name,assets)
    nonce = auth["rootAdmissionNonce"]
    records = {}
    observer_prior = {**scope(),"schema":"RH_WEIL_GLOBAL_OBSERVER_PRIOR_ACCOUNTING_V1",
        "status":"ROOT_VERIFIED_ALL_PRIOR_SCIENTIFIC_PROCESSES_TERMINAL",
        "noLiveScientificProcesses":True,"sourceConsumedUpperMs":0,"finiteConsumedUpperMs":0,
        "sourceChargedUpperBytes":RESERVE_BYTES,"finiteChargedUpperBytes":0,
        "phaseLifetimes":[],"baselinePins":{},"rootAdministrativeReservePlanPin":reserve_pin}
    source_prior = {**scope(),"schema":"RH_WEIL_ROOT_OBSERVED_GLOBAL_ACCOUNTING_V1",
        "status":"ROOT_VERIFIED_NO_RETRY_ACCOUNTING","outerRelativePath":SCIENCE,
        "sourceObservedUpperMs":0,"aggregateObservedUpperMs":0,
        "sourceChargedUpperBytes":RESERVE_BYTES,"aggregateChargedUpperBytes":RESERVE_BYTES,
        "phaseLifetimes":[],"outerPreviouslyCreated":False,"chargedPathBindings":{},
        "producerTerminalPin":None,"outerClaimPin":None,"rootAdministrativeReservePlanPin":reserve_pin}
    observer_prior_pin = new_record(records,"observer-prior",observer_prior)
    source_prior_pin = new_record(records,"source-prior",source_prior)
    observer_admission_pin = new_record(records,"observer-admission",{
        **scope(),"schema":"RH_WEIL_C069_IRREVOCABLE_OBSERVER_ARM_ADMISSION_V1",
        "status":"ADMITTED_BEFORE_ARM_NO_RETRY","phase":"source-produce","armIdentity":nonce})
    source_admission_pin = new_record(records,"source-admission",{
        **scope(),"schema":"RH_WEIL_C069_IRREVOCABLE_PHASE_ADMISSION_V1",
        "status":"ADMITTED_BEFORE_LAUNCH_NO_RETRY","phase":"produce","freezeIdentity":nonce})
    context = {**scope(),"schema":"RH_WEIL_C069_SOURCE_PREPARED_CONTEXT_V1",
        "status":"ROOT_PREPARED_METADATA_ONLY_NO_ARM_OR_SCIENCE_STARTED_BY_BUILDER",
        "assets":assets,"rootAuthorizationPin":auth_pin,"rootAdministrativeReservePlanPin":reserve_pin,
        "armIdentity":nonce,"parameters":PARAMETERS,"phaseLimits":LIMITS,
        "externalOutputPaths":EXTERNAL,"armWaitMaxMs":ARM_WAIT_MS,
        "sourcePriorPin":source_prior_pin,"sourceAdmissionPin":source_admission_pin,
        "observerPriorPin":observer_prior_pin,"observerAdmissionPin":observer_admission_pin}
    context_pin = new_record(records,"prepared-context",context)
    add_pins(charged,{p["path"]:p for p in (observer_prior_pin,source_prior_pin,
             observer_admission_pin,source_admission_pin,context_pin)})
    common = {**scope(),"phase":"source-produce","armIdentity":nonce,
        "observerCodePin":assets["observerCodePin"],"childCodePin":assets["controllerPin"],
        "contractPin":assets["contractPin"],"rootAdmissionPin":observer_admission_pin,
        "priorAccountingPin":observer_prior_pin,"phaseLimits":LIMITS,"armWaitMaxMs":ARM_WAIT_MS,
        "externalOutputPaths":EXTERNAL,"finalFreezeRelativePath":FINAL_FREEZE,
        "finalRootGateRelativePath":FINAL_GATE,"reviewPins":assets["armReviewPins"],
        "chargedMetadataPins":charged}
    gate = {**common,"schema":"RH_WEIL_GLOBAL_OBSERVER_ARM_ROOT_GATE_V1",
        "status":"ROOT_EXPLICIT_OBSERVER_ARM_APPROVED",
        "armRelativePath":PATHS["observer-arm"],"sameRuntimeGoalLiveAndActiveChecked":True}
    gate_pin = new_record(records,"observer-arm-root-gate",gate)
    arm = {**common,"schema":"RH_WEIL_GLOBAL_OBSERVER_ARM_V1",
        "authorization":"ROOT_EXPLICIT_C069_OBSERVER_ARM_ONLY","rootArmGatePin":gate_pin}
    new_record(records,"observer-arm",arm)
    validate_prepared_graph(records,assets)
    return records


def validate_prepared_graph(records, assets):
    """Schema/map/DAG checks in memory; calls no observer/controller functions."""
    arm = decode(records[PATHS["observer-arm"]])
    gate = decode(records[PATHS["observer-arm-root-gate"]])
    need(arm["rootArmGatePin"] == byte_pin(PATHS["observer-arm-root-gate"],records[PATHS["observer-arm-root-gate"]]),"ARM_GATE_PIN")
    need(gate["armRelativePath"] == PATHS["observer-arm"],"ARM_GATE_PATH_ONLY_NO_SELF_HASH")
    for key in gate.keys()-{"schema","status","armRelativePath","sameRuntimeGoalLiveAndActiveChecked"}:
        need(arm[key] == gate[key],"ARM_GATE_REPEAT:"+key)
    need(LIMITS["internalScientificCutoffMs"]+10000 <= LIMITS["externalObserverChildTimeoutMs"]
         and LIMITS["externalObserverChildTimeoutMs"]+20000 <= LIMITS["phaseAllowanceMs"]
         and LIMITS["phaseAllowanceMs"] <= 3600000,"FUNDED_PHASE_LIMITS")
    need(sum(p["maxBytes"] for p in EXTERNAL) == 303104 <= 524288,"EXACT_FIVE_EXTERNAL_RESERVES")
    need(len(EXTERNAL) == 5 and len({p["path"] for p in EXTERNAL}) == 5,"EXACT_EXTERNAL_MAP")
    for name,pin in arm["chargedMetadataPins"].items():
        if name in records:
            need(pin == byte_pin(name,records[name]),"IN_MEMORY_METADATA_PIN")
        else:
            read_pin(pin)
    need(PATHS["observer-arm"] not in arm["chargedMetadataPins"]
         and PATHS["observer-arm-root-gate"] not in arm["chargedMetadataPins"],"NO_ARM_SELF_HASH_CYCLE")
    need(assets["reviewPins"][0]["owner"] != assets["reviewPins"][1]["owner"],"DISTINCT_OWNERS")


def write_once(name, raw):
    need(len(raw) <= 262144,"BOUNDED_IMMUTABLE_WRITE")
    with path(name).open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())


def pid_is_live(pid):
    """Actual kernel liveness check, without launching or inspecting science."""
    need(os.name == "nt","WINDOWS_ACTUAL_PID_CHECK_REQUIRED")
    need(type(pid) is int and pid > 0,"ACTUAL_READY_PID_REQUIRED")
    kernel = ctypes.WinDLL("kernel32",use_last_error=True)
    kernel.OpenProcess.argtypes = (wintypes.DWORD,wintypes.BOOL,wintypes.DWORD)
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.WaitForSingleObject.argtypes = (wintypes.HANDLE,wintypes.DWORD)
    kernel.WaitForSingleObject.restype = wintypes.DWORD
    kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
    kernel.CloseHandle.restype = wintypes.BOOL
    handle = kernel.OpenProcess(0x00100000,False,pid)  # SYNCHRONIZE, no mutation rights.
    need(bool(handle),"CANNOT_OPEN_ACTUAL_READY_PID")
    try:
        need(kernel.WaitForSingleObject(handle,0) == 258,"ACTUAL_READY_PID_NOT_LIVE")
    finally:
        kernel.CloseHandle(handle)


def aware_time(value):
    need(type(value) is str,"ACTUAL_UTC_STRING_REQUIRED")
    result = datetime.fromisoformat(value.replace("Z","+00:00"))
    need(result.tzinfo is not None and result.utcoffset().total_seconds() == 0,"UTC_OFFSET_REQUIRED")
    return result


def finalize_graph(live_name):
    need(path(META).is_dir() and not path(SCIENCE).exists(),"PREPARED_METADATA_AND_UNSTARTED_SCIENCE_REQUIRED")
    need(not path(FINAL_GATE).exists() and not path(FINAL_FREEZE).exists(),"NO_FINAL_GATE_RETRY_OR_OVERWRITE")
    arm,arm_pin = read_json(PATHS["observer-arm"])
    arm_gate = decode(read_pin(arm["rootArmGatePin"]))
    context_pin = arm["chargedMetadataPins"][PATHS["prepared-context"]]
    context = decode(read_pin(context_pin))
    same_scope(context)
    assets = context["assets"]
    # Every ARM-pinned immutable record is checked again. Scientific inputs are
    # not reread here: their opaque hashes were checked before ARM, and the
    # source controller rehashes all four under its own complete runtime budget.
    charged = {}
    add_pins(charged,arm["chargedMetadataPins"])
    add_pins(charged,{p["path"]:p for p in (arm_pin,arm["rootArmGatePin"],arm["rootAdmissionPin"],
                                          arm["priorAccountingPin"],arm["contractPin"])})
    for pin in charged.values():
        read_pin(pin)
    need(arm_gate["armRelativePath"] == PATHS["observer-arm"]
         and arm["armIdentity"] == context["armIdentity"]
         and arm["phaseLimits"] == context["phaseLimits"] == LIMITS
         and arm["externalOutputPaths"] == context["externalOutputPaths"] == EXTERNAL,
         "FROZEN_PREPARED_ARM_CONTEXT")
    for name,pin in assets["codePins"].items():
        need(hash_file(BASE+name) == pin,"FINAL_CODE_CHANGED_AFTER_ARM")
    for pin in assets["mathPins"].values():
        read_pin(pin)
    for review in assets["reviewPins"]:
        read_pin(review["pin"])
    ready,ready_pin = read_json(READY)
    claim,claim_pin = read_json(CLAIM)
    live,live_pin = read_json(live_name)
    need(not path(live_name).is_relative_to(path(SCIENCE))
         and not path(live_name).is_relative_to(path(PHASE_DIR)),"ROOT_LIVE_RECORD_OUTSIDE_OWNED_NAMESPACES")
    for obj in (ready,claim,live):
        same_scope(obj)
    need(ready["schema"] == "RH_WEIL_SOURCE_EXTERNAL_OBSERVER_LAUNCH_V1"
         and ready["phase"] == "produce" and ready["observerPhase"] == "source-produce"
         and ready["freezeIdentity"] == ready["launchNonce"] == arm["armIdentity"]
         and ready["phaseLimits"] == LIMITS and ready["externalOutputPaths"] == EXTERNAL
         and ready["observerCodePin"] == arm["observerCodePin"]
         and ready["codePin"] == arm["childCodePin"]
         and ready["armPin"] == arm_pin and ready["rootArmGatePin"] == arm["rootArmGatePin"]
         and ready["rootAdmissionPin"] == arm["rootAdmissionPin"]
         and ready["priorAccountingPin"] == arm["priorAccountingPin"]
         and ready["observerClaimPin"] == claim_pin
         and ready["rootMustVerifyFullLifetimeAfterTerminal"] is True and ready["noRetry"] is True,
         "ACTUAL_READY_EXACT_ARM_BINDING")
    need(claim["schema"] == "RH_WEIL_GLOBAL_OBSERVER_ONCE_ARM_CLAIM_V1"
         and claim["phase"] == "source-produce" and claim["observerPID"] == ready["observerPID"]
         and claim["armIdentity"] == arm["armIdentity"] and claim["armPin"] == arm_pin
         and claim["noRetry"] is True,"ACTUAL_OBSERVER_CLAIM_BINDING")
    need(live["schema"] == LIVE_SCHEMA
         and live["status"] == "ROOT_OBSERVED_READY_PID_AND_LIVE_SESSION"
         and live["phase"] == "source-produce" and live["observerPID"] == ready["observerPID"]
         and live["readyPin"] == ready_pin and live["handle_type"] == "exec_command"
         and type(live["handle"]) in (int,str) and bool(live["handle"])
         and live["liveStatus"] == "running" and live["actualToolHandleObservedLive"] is True,
         "ROOT_ACTUAL_READY_PID_AND_LIVE_TOOL_SESSION_REQUIRED")
    now = datetime.now(timezone.utc)
    ready_utc,live_utc = aware_time(ready["readyUTC"]),aware_time(live["observedUTC"])
    need(0 <= (now-ready_utc).total_seconds() <= 50
         and ready_utc <= live_utc <= now and (now-live_utc).total_seconds() <= 30,
         "FRESH_LIVE_OBSERVATION_AND_FUNDED_ARM_HANDSHAKE_REQUIRED")
    pid_is_live(ready["observerPID"])
    need(not path(PHASE_DIR+"/terminal.json").exists(),"OBSERVER_ALREADY_TERMINAL")
    add_pins(charged,{claim_pin["path"]:claim_pin,live_pin["path"]:live_pin})
    extras = live.get("additionalChargedMetadataPins",{})
    need(type(extras) is dict,"FINAL_ROOT_EXTRA_METADATA_MAP")
    add_pins(charged,extras)
    for pin in extras.values():
        need(pin["path"] != "goals/STATE.json","MUTABLE_STATE_CANNOT_BE_PINNED")
        read_pin(pin)
    common = {**scope(),"phase":"produce","outerRelativePath":SCIENCE,"parameters":PARAMETERS,
        "freezeIdentity":arm["armIdentity"],"rootAdmissionNonce":arm["armIdentity"],
        "contractPin":assets["contractPin"],"controllerPin":assets["controllerPin"],
        "producerPin":assets["producerPin"],"verifierPin":assets["verifierPin"],
        "protocolPin":assets["protocolPin"],"sourcePins":assets["sourcePins"],"mathPins":assets["mathPins"],
        "reviewPins":assets["reviewPins"],"launchPin":ready_pin,
        "admissionPin":context["sourceAdmissionPin"],"priorAccountingPin":context["sourcePriorPin"],
        "chargedMetadataPins":charged,"externalOutputPaths":EXTERNAL,"phaseLimits":LIMITS,
        "producerResultPin":None,"producerTerminalPin":None,"outerClaimPin":None}
    gate = {**common,"schema":"RH_WEIL_GLOBAL_SOURCE_PHASE_ROOT_GATE_V1",
        "status":"ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION_APPROVED","freezeRelativePath":FINAL_FREEZE}
    gate_raw = packed(gate)
    freeze = {**common,"schema":"RH_WEIL_GLOBAL_SOURCE_PHASE_FREEZE_V1",
        "authorization":"ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION",
        "rootGatePin":byte_pin(FINAL_GATE,gate_raw)}
    freeze_raw = packed(freeze)
    need(len(gate_raw) <= 262144 and len(freeze_raw) <= 262144,"BOUNDED_FINAL_METADATA")
    # Never exclude an ARM charge; READY/gate/freeze are additionally charged by
    # the exact controller. No record hashes itself or a successor in this DAG.
    for name,pin in charged.items():
        need(name not in (FINAL_GATE,FINAL_FREEZE,READY),"NO_FINAL_SELF_HASH_OR_LAUNCH_DOUBLE_ROLE")
        read_pin(pin)
    pid_is_live(ready["observerPID"])
    need((datetime.now(timezone.utc)-ready_utc).total_seconds() <= 52
         and not path(PHASE_DIR+"/terminal.json").exists(),"HANDSHAKE_EXPIRED_BEFORE_COMMIT")
    return {FINAL_GATE:gate_raw,FINAL_FREEZE:freeze_raw}


def summary(records=None):
    result = {**scope(),"mode":"METADATA_ONLY_NO_LAUNCH",
        "builderMetadataDirectory":META,"scienceOuterMustInitiallyBeAbsent":SCIENCE,
        "observerOuterMustInitiallyBeAbsent":OBSERVER,"armFile":PATHS["observer-arm"],
        "readyFile":READY,"finalRootGateFile":FINAL_GATE,"finalFreezeFile":FINAL_FREEZE,
        "phaseLimits":LIMITS,"armWaitMaxMs":ARM_WAIT_MS,
        "prepaidCurrentC069RootAdministrativeBytes":RESERVE_BYTES,
        "initialScienceTimeMs":0,"initialPriorSciencePhases":[],"initialPriorInventory":{},
        "externalOutputPaths":EXTERNAL,"externalReservedBytes":303104,
        "rootAuthorizationSchema":AUTH_SCHEMA,"rootLiveObservationSchema":LIVE_SCHEMA,
        "rootReservePlanSchema":RESERVE_SCHEMA,
        "requiredRootAuthorizationFields":["schema","status","runtimeGoalCreatedAt","contractId","targetId",
            "rootAdmissionNonce","rootRuntimeGoalCheckedActive","codePreparationActualFinalVerified",
            "contractPin","codeClosurePin","rootAdministrativeReservePlanPin"],
        "requiredReservePolicyFields":["mutablePathPolicy","cumulativeWritePolicy"],
        "requiredRootLiveFields":["schema","status","runtimeGoalCreatedAt","contractId","targetId","phase",
            "observerPID","readyPin","handle_type","handle","liveStatus","actualToolHandleObservedLive","observedUTC"]}
    if records is not None:
        result["immutableOutputPins"] = [byte_pin(n,raw) for n,raw in records.items()]
        result["newBuilderMetadataBytes"] = sum(map(len,records.values()))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command",choices=("plan","prepare","finalize-after-ready"))
    parser.add_argument("--root-authorization-file")
    parser.add_argument("--root-live-observation-file")
    parser.add_argument("--root-authorize",action="store_true",
                        help="ROOT explicit authorization; never inferred from documentation")
    args = parser.parse_args()
    if args.command == "plan":
        initial_absence()
        assets = frozen_assets()
        records = prepare_graph(assets,args.root_authorization_file) if args.root_authorization_file else None
        result = summary(records)
        result["allNineActualFinalCodePins"] = list(assets["codePins"].values())
        result["contractPin"] = assets["contractPin"]
        result["codeClosurePin"] = assets["codeClosurePin"]
        result["readOnly"] = True
        print(packed(result).decode("ascii"),end="")
        return
    need(args.root_authorize,"EXPLICIT_ROOT_AUTHORIZE_FLAG_REQUIRED_FOR_ANY_WRITE")
    if args.command == "prepare":
        need(args.root_authorization_file is not None,"ROOT_AUTHORIZATION_FILE_REQUIRED")
        records = prepare_graph(frozen_assets(),args.root_authorization_file)
        # Validate every byte before acquiring once ownership. Partial writes
        # are preserved; no cleanup/retry/reset branch exists.
        initial_absence()
        path(META).mkdir(parents=True,exist_ok=False)
        for name,raw in records.items():
            write_once(name,raw)
    else:
        need(args.root_live_observation_file is not None,"ROOT_LIVE_OBSERVATION_FILE_REQUIRED")
        records = finalize_graph(args.root_live_observation_file)
        for name,raw in records.items():
            write_once(name,raw)
    # Small stdout/tool copies belong to ROOT's prepaid administrative reserve.
    print(packed({"status":"ROOT_REQUESTED_IMMUTABLE_METADATA_WRITTEN_NO_PROCESS_LAUNCHED",
                  "command":args.command,"pins":[byte_pin(n,b) for n,b in records.items()]}).decode("ascii"),end="")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("C069_METADATA_BUILDER_STOP: "+str(exc),file=sys.stderr)
        raise SystemExit(2)

#!/usr/bin/env python3
"""ROOT-only metadata handoff after ACTUAL live exec-session/READY observation.

No ARM, observer, controller or scientific process is launched here. ROOT's
explicit invocation asserts that the supplied exec session was really observed
running. This helper can check the kernel PID, but cannot query that tool session.
The existing ARM pins root-admin-write.py; this late ROOT helper is frozen into
root-live's additional charged pins and then the final scientific metadata map.
"""
import argparse
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
EXEC = "reviews/2026-11-01/global-joint-execution/"
META = EXEC+"source-produce/"
OBSERVER = "literature/local/2026-11-01-directional-remainder-whole-observer/run-01/source-produce/"
SCIENCE = "literature/local/2026-11-01-directional-remainder-whole/run-01/"
READY = OBSERVER+"ready.json"
ARM = META+"observer-arm.json"
CONTEXT = META+"prepared-context.json"
LIVE = META+"root-live.json"
FINAL_GATE = OBSERVER+"final-root-gate.json"
FINAL_FREEZE = OBSERVER+"final-freeze.json"
GOAL = 1793085111
TARGET = "RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def utc():
    return datetime.now(timezone.utc).isoformat()


def path(name):
    need(type(name) is str and name and ":" not in name and "\\" not in name
         and all(x not in ("", ".", "..") for x in name.split("/")),"CANONICAL_RELATIVE_PATH")
    p = ROOT.joinpath(*name.split("/")).resolve()
    need(p.is_relative_to(ROOT),"WORKSPACE_PATH_REQUIRED")
    return p


def unique(rows):
    result = {}
    for key,value in rows:
        need(key not in result,"DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def raw_pin(name):
    raw = path(name).read_bytes()
    need(len(raw) <= 262144,"SMALL_METADATA_ONLY")
    return raw,{"path":name,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}


def record(name):
    raw,pin = raw_pin(name)
    return json.loads(raw,object_pairs_hook=unique),pin


def scope(obj):
    need(type(obj.get("runtimeGoalCreatedAt")) is int
         and obj["runtimeGoalCreatedAt"] == GOAL and obj.get("contractId") == "C069"
         and obj.get("targetId") == TARGET,"SAME_ACTIVE_GOAL_C069_METADATA_REQUIRED")


def pid_live(pid):
    need(os.name == "nt" and type(pid) is int and pid > 0,"ACTUAL_WINDOWS_OBSERVER_PID_REQUIRED")
    kernel = ctypes.WinDLL("kernel32",use_last_error=True)
    kernel.OpenProcess.argtypes = (wintypes.DWORD,wintypes.BOOL,wintypes.DWORD)
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.WaitForSingleObject.argtypes = (wintypes.HANDLE,wintypes.DWORD)
    kernel.WaitForSingleObject.restype = wintypes.DWORD
    kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
    handle = kernel.OpenProcess(0x00100000,False,pid)
    need(bool(handle),"READY_PID_NOT_OPENABLE")
    try:
        need(kernel.WaitForSingleObject(handle,0) == 258,"READY_PID_ALREADY_TERMINAL")
    finally:
        kernel.CloseHandle(handle)


def metadata_module(filename, module_name):
    spec = importlib.util.spec_from_file_location(module_name,HERE/filename)
    need(spec is not None and spec.loader is not None,"METADATA_WRITER_LOADER")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def trimmed_state(state, admin):
    """Keep current causal fields; discard only obsolete publication prose first."""
    publication = state.get("publication_approval_gate",{})
    publication.pop("metadata_child_condition",None)
    publication["current_scope"] = "C069 actual SOURCE-PRODUCE; later phases require separate ROOT gates and remaining-budget acceptance."
    if len(admin.packed(state)) >= 16000:
        # Historical exact scopes remain in the existing macro frontier and
        # each referenced immutable correction; preserve their paths/statuses.
        freezes = state.get("semantic_dependency_freeze",{})
        for key,value in list(freezes.items()):
            if isinstance(value,dict):
                freezes[key] = {k:value[k] for k in ("path","status") if k in value}
    need(len(admin.packed(state)) < 16000,"TRIMMED_STATE_STILL_TOO_LARGE")
    return state


def save_state(admin, state, session, pid, ready_pin, when, stage, pending_status="running"):
    primary = state["primary_contract"]
    primary["status"] = "running"
    primary["stage"] = stage
    primary["next_action"] = (
        "Observe SAME exec_command session "+str(session)+" and actual observer PID "+str(pid)+
        "; preserve all partial/terminal evidence and full pre-ARM/post-exit UTC/process/byte accounting. "
        "No relaunch or automatic SOURCE-VERIFY/finite phase.")
    state["pending_processes"] = [{
        "handle_type":"exec_command","handle":session,"status":pending_status,
        "observed_at":when,"observer_pid":pid,"ready_pin":ready_pin,
        "output_paths":[READY,OBSERVER+"terminal.json",SCIENCE+"stage-01-source/produce/terminal.json",FINAL_FREEZE],
        "next_action":"Poll SAME actual session; observation timeout is not terminal. Never relaunch."}]
    state["process_inventory_observed_on"] = (
        "ROOT supplied actual running exec session; helper checked READY binding and kernel observer PID. "
        "Only source-produce is admitted; complete child/process closure remains unverified.")
    trimmed_state(state,admin)
    return admin.write_json("goals/STATE.json",state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-authorize",action="store_true")
    parser.add_argument("--session-id",type=int,required=True,
                        help="ACTUAL exec_command session ROOT just observed running; never invent")
    parser.add_argument("--before-arm-file")
    parser.add_argument("--final-audit-file")
    args = parser.parse_args()
    need(args.root_authorize and args.session_id > 0,"ROOT_ACTUAL_RUNNING_SESSION_AUTHORIZATION_REQUIRED")
    need(not path(LIVE).exists() and not path(FINAL_GATE).exists()
         and not path(FINAL_FREEZE).exists(),"HANDOFF_IS_ONCE_ONLY_NO_RETRY")
    arm,arm_pin = record(ARM)
    context,context_pin = record(CONTEXT)
    ready,ready_pin = record(READY)
    for obj in (arm,context,ready):
        scope(obj)
    charged = arm["chargedMetadataPins"]
    for name in (EXEC+"root-admin-write.py",EXEC+"build-source-admission.py"):
        _,pin = raw_pin(name)
        need(charged.get(name) == pin,"HELPER_MUST_ALREADY_BE_FROZEN_AND_CHARGED:"+name)
    need(charged.get(CONTEXT) == context_pin
         and ready["schema"] == "RH_WEIL_SOURCE_EXTERNAL_OBSERVER_LAUNCH_V1"
         and ready["phase"] == "produce" and ready["observerPhase"] == "source-produce"
         and ready["armPin"] == arm_pin
         and ready["freezeIdentity"] == ready["launchNonce"] == context["armIdentity"] == arm["armIdentity"]
         and ready["observerCodePin"] == arm["observerCodePin"]
         and ready["codePin"] == arm["childCodePin"]
         and ready["phaseLimits"] == arm["phaseLimits"] == context["phaseLimits"]
         and ready["externalOutputPaths"] == arm["externalOutputPaths"] == context["externalOutputPaths"],
         "ACTUAL_READY_CONTEXT_ARM_BINDING")
    ready_utc = datetime.fromisoformat(ready["readyUTC"].replace("Z","+00:00"))
    need(ready_utc.tzinfo is not None and ready_utc.utcoffset().total_seconds() == 0
         and 0 <= (datetime.now(timezone.utc)-ready_utc).total_seconds() <= 40,
         "FRESH_ACTUAL_READY_HANDSHAKE_REQUIRED")
    need(not path(OBSERVER+"terminal.json").exists() and not path(SCIENCE.rstrip("/")).exists(),
         "OBSERVER_NOT_TERMINAL_AND_SCIENCE_NOT_STARTED_REQUIRED")
    pid = ready["observerPID"]
    pid_live(pid)
    state,_ = record("goals/STATE.json")
    primary = state["primary_contract"]
    observation = state["runtime_goal_observation"]
    need(primary["id"] == "C069" and primary["path"] == "goals/contracts/C069-global-exact-directional-whole.md"
         and primary.get("settled_iterations") == []
         and observation["status"] == "active" and observation["created_at_unix"] == GOAL,
         "STATE_SAME_UNSETTLED_C069_ACTIVE_GOAL_REQUIRED")
    admin = metadata_module("root-admin-write.py","c069_root_admin_metadata")
    observed = utc()
    # This durable checkpoint MUST precede the scientific gate/freeze. Its raw
    # SHA is deliberately not pinned: STATE will be written again after handoff.
    save_state(admin,state,args.session_id,pid,ready_pin,observed,
        "SOURCE-PRODUCE actual ARM/READY and ROOT running session observed; STATE saved before final scientific gate. No source acceptance.")
    _,self_pin = raw_pin(EXEC+"root-ready-handoff.py")
    extras = {self_pin["path"]:self_pin}
    for name in (args.before_arm_file,args.final_audit_file):
        if name is not None:
            need(not path(name).is_relative_to(path(SCIENCE.rstrip("/")))
                 and not path(name).is_relative_to(path(OBSERVER.rstrip("/"))),"ROOT_METADATA_PIN_OUTSIDE_RUNTIME_NAMESPACES")
            _,pin = raw_pin(name)
            extras[name] = pin
    live = {"schema":"RH_WEIL_C069_OBSERVER_LIVE_ROOT_OBSERVATION_V1",
        "status":"ROOT_OBSERVED_READY_PID_AND_LIVE_SESSION","runtimeGoalCreatedAt":GOAL,
        "contractId":"C069","targetId":TARGET,"phase":"source-produce",
        "observerPID":pid,"readyPin":ready_pin,"handle_type":"exec_command","handle":args.session_id,
        "liveStatus":"running","actualToolHandleObservedLive":True,"observedUTC":observed,
        "rootReadyStateCheckpointWrittenBeforeFinalFreeze":True,
        "rootRuntimeGoalCheckedActive":True,"additionalChargedMetadataPins":extras}
    admin.write_json(LIVE,live,fresh=True)
    command = [sys.executable,str(HERE/"build-source-admission.py"),"finalize-after-ready",
               "--root-authorize","--root-live-observation-file",LIVE]
    try:
        result = subprocess.run(command,cwd=ROOT,capture_output=True,timeout=20,check=False)
        need(len(result.stdout)+len(result.stderr) <= 16384,"BOUNDED_METADATA_FINALIZER_OUTPUT")
        if result.returncode:
            raise RuntimeError("FINALIZE_EXIT_"+str(result.returncode)+":"+
                               result.stderr.decode("utf-8",errors="replace")[-4096:])
    except Exception as exc:
        save_state(admin,state,args.session_id,pid,ready_pin,utc(),
            "SOURCE-PRODUCE metadata handoff stopped after READY; preserve same irrevocable attempt and any partial gate/freeze. "+str(exc)[:600],"unknown")
        raise
    need(path(FINAL_GATE).is_file() and path(FINAL_FREEZE).is_file(),"SUCCESSFUL_FINALIZER_MUST_EMIT_BOTH_RECORDS")
    save_state(admin,state,args.session_id,pid,ready_pin,observed,
        "SOURCE-PRODUCE final gate/freeze issued on actual READY after durable STATE checkpoint. Authorized child may be running; no source230/whole acceptance.")
    print(json.dumps({"status":"ROOT_READY_STATE_AND_SCIENTIFIC_METADATA_HANDOFF_COMPLETE",
        "sessionId":args.session_id,"observerPID":pid,"rootLiveFile":LIVE,
        "finalGate":FINAL_GATE,"finalFreeze":FINAL_FREEZE,
        "nextAction":"Observe SAME actual exec session; no automatic later phase."},separators=(",",":")))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("C069_ROOT_READY_HANDOFF_STOP: "+str(exc),file=sys.stderr)
        raise SystemExit(2)

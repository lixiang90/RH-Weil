"""One inert host/host observation; no scientific imports or child launch."""
import argparse
import ctypes as c
from ctypes import wintypes as w
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ONCE = HERE / "once"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def raw(v):
    return (json.dumps(v, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def write(p, value, maximum, state=False):
    b = (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8") if state else raw(value)
    need(len(b) <= maximum, "OUTPUT_CAP")
    q = p.with_name(p.name + ".inert.tmp") if state else p
    with q.open("xb") as f:
        f.write(b)
        f.flush()
        os.fsync(f.fileno())
    if state:
        os.replace(q, p)


def pin(p):
    b = p.read_bytes()
    return dict(path=p.relative_to(ROOT).as_posix(), bytes=len(b), sha256=hashlib.sha256(b).hexdigest())


def kernel():
    k = c.WinDLL("kernel32", use_last_error=True)
    k.OpenProcess.argtypes = (w.DWORD, w.BOOL, w.DWORD)
    k.OpenProcess.restype = w.HANDLE
    k.WaitForSingleObject.argtypes = (w.HANDLE, w.DWORD)
    k.WaitForSingleObject.restype = w.DWORD
    k.GetCurrentProcess.restype = w.HANDLE
    k.GetProcessTimes.argtypes = (w.HANDLE,) + (c.POINTER(w.FILETIME),) * 4
    k.GetProcessTimes.restype = w.BOOL
    k.CloseHandle.argtypes = (w.HANDLE,)
    k.CloseHandle.restype = w.BOOL
    return k


def creation(k, handle):
    values = [w.FILETIME() for _ in range(4)]
    need(k.GetProcessTimes(handle, *(c.byref(v) for v in values)), "GET_TIMES_FAILED")
    return (values[0].dwHighDateTime << 32) | values[0].dwLowDateTime


def main():
    a = argparse.ArgumentParser()
    a.add_argument("mode", choices=("launch", "check"))
    a.add_argument("--root-authorize", action="store_true")
    a.add_argument("--session-id", type=int)
    args = a.parse_args()
    need(args.root_authorize and os.name == "nt", "ROOT_WINDOWS_ONLY")
    plan = json.loads((HERE / "plan.json").read_bytes())
    need(plan["runtimeGoalCreatedAt"] == 1793085111 and plan["rootAuthorizesOneInertPairing"] is True, "SAME_GOAL_ROOT_INERT_AUTHORIZATION")
    need(pin(Path(__file__).resolve()) == plan["programPin"], "FROZEN_PROGRAM")
    need(Path.cwd().resolve() == ROOT and plan["pairing"] == "exec_command:require_escalated->exec_command:require_escalated", "EXACT_CONTEXT")
    initial = json.loads((ROOT / "goals/STATE.json").read_bytes())
    need(initial["primary_contract"]["id"] == "C069" and initial["primary_contract"]["status"] == "stopped"
         and initial["runtime_goal_observation"]["status"] == "active"
         and initial["runtime_goal_observation"]["created_at_unix"] == 1793085111, "SAME_SPENT_CONTRACT_ACTIVE_GOAL")
    k = kernel()
    if args.mode == "launch":
        ONCE.mkdir(exist_ok=False)
        write(ONCE / "claim.json", dict(nonce=plan["nonce"], pid=os.getpid()), 256)
        ready = dict(nonce=plan["nonce"], pid=os.getpid(), parentPID=os.getppid(),
                     creation100ns=creation(k, k.GetCurrentProcess()), readyUTC=utc(),
                     cwd=str(ROOT), executable=sys.executable, programPin=plan["programPin"])
        write(ONCE / "ready.json", ready, 1024)
        print(json.dumps(ready, separators=(",", ":")), flush=True)
        time.sleep(35)
        write(ONCE / "terminal.json", dict(status="INERT_SELF_TERMINATED", pid=os.getpid(),
              nonce=plan["nonce"], endedUTC=utc(), scientificWork=False), 512)
        return 0
    need(args.session_id and args.session_id > 0, "ACTUAL_ROOT_TOOL_SESSION_REQUIRED")
    write(ONCE / "check-claim.json", dict(nonce=plan["nonce"], session=args.session_id), 256)
    result = dict(status="FAIL", nonce=plan["nonce"], session=args.session_id, checkedUTC=utc())
    h = query = None
    try:
        ready = json.loads((ONCE / "ready.json").read_bytes())
        latency = (datetime.now(timezone.utc) - datetime.fromisoformat(ready["readyUTC"])).total_seconds()
        result.update(pid=ready["pid"], readyPin=pin(ONCE / "ready.json"), latencyMs=latency * 1000)
        need(0 <= latency <= 20, "READY_LATENCY")
        need(ready["nonce"] == plan["nonce"] and ready["programPin"] == plan["programPin"]
             and ready["cwd"] == str(ROOT) and ready["executable"] == sys.executable, "READY_IDENTITY")
        h = k.OpenProcess(0x00100000, False, ready["pid"])
        result["synchronizeOpenWinError"] = 0 if h else c.get_last_error()
        need(h, "SYNC_OPEN_FAILED")
        result["syncWaitBefore"] = k.WaitForSingleObject(h, 0)
        need(result["syncWaitBefore"] == 258, "SYNC_NOT_LIVE")
        query = k.OpenProcess(0x1000, False, ready["pid"])
        result["identityQueryOpenWinError"] = 0 if query else c.get_last_error()
        need(query, "IDENTITY_QUERY_OPEN_FAILED")
        result["creationIdentityMatches"] = creation(k, query) == ready["creation100ns"]
        need(result["creationIdentityMatches"], "PID_REUSED")
        result["syncWaitAfter"] = k.WaitForSingleObject(h, 0)
        need(result["syncWaitAfter"] == 258, "SYNC_ENDED_DURING_QUERY")
        result["latencyMs"] = (datetime.now(timezone.utc) - datetime.fromisoformat(ready["readyUTC"])).total_seconds() * 1000
        need(0 <= result["latencyMs"] <= 20000, "COMPLETED_CHECK_LATENCY")
        result["checkedUTC"] = utc()
        result["status"] = "LIVE_RIGHTS_IDENTITY_OBSERVED_PENDING_ROOT_CLOSURE"
    except Exception as error:
        result["reason"] = str(error)[:160]
    finally:
        for handle in (query, h):
            if handle:
                k.CloseHandle(handle)
    write(ONCE / "checked.json", result, 1024)
    state = json.loads((ROOT / "goals/STATE.json").read_bytes())
    need(state["primary_contract"]["id"] == "C069" and state["primary_contract"]["status"] == "stopped", "C069_MUST_REMAIN_SPENT")
    state["primary_contract"]["stage"] = "One inert host-host check emitted; C069 stopped. Scientific work forbidden. Actual same-session closure pending."
    state["primary_contract"]["next_action"] = "Close SAME inert session " + str(args.session_id) + "; consume actual latency/identity/full120s64KiB; no retry or scientific admission."
    state["pending_processes"] = [dict(handle_type="exec_command", handle=args.session_id,
        status="running" if result["status"].startswith("LIVE_") else "unknown", observed_at=utc(), output_paths=[(ONCE / "ready.json").relative_to(ROOT).as_posix(),
        (ONCE / "terminal.json").relative_to(ROOT).as_posix()], next_action="Observe SAME inert handle to terminal, never relaunch.")]
    write(ROOT / "goals/STATE.json", state, 11000, state=True)
    print(json.dumps(result, separators=(",", ":")))
    return 0 if result["status"].startswith("LIVE_") else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print("INERT_STOP:" + str(error)[:200], file=sys.stderr)
        raise SystemExit(2)

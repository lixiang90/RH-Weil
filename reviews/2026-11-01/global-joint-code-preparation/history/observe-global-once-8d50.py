"""Future one-child C069 ARM/READY/final-freeze observer. CODE_PREP ONLY.

An authenticated ARM may claim only its separate observer directory. READY
contains the actual observer PID. ROOT then writes the separately authenticated
scientific freeze/gate referring to READY; no scientific child starts earlier.
No ARM/freeze/data attempt is created merely by authoring or importing this file.
Windows10+ JOB_LIST creates the suspended child INSIDE a kill-on-close job.
Only its three explicit standard handles are inherited. No shell is invoked.
"""
from __future__ import annotations
import time
STARTED = time.monotonic()
STARTED_UTC = time.time()
import argparse
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import threading

ROOT = Path(__file__).resolve().parents[3]
SELF = Path(__file__).resolve()
BASE = "reviews/2026-11-01/global-joint-code-preparation/"
OUTER = "literature/local/2026-11-01-directional-remainder-whole/run-01"
OBSERVER = "literature/local/2026-11-01-directional-remainder-whole-observer/run-01"
GOAL, TARGET = 1793085111, "RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1"
PHASES = ("source-produce", "source-verify", "finite-produce", "finite-verify")
CODES = {"source-produce":"source-stage-controller.py", "source-verify":"source-stage-controller.py",
         "finite-produce":"finite-whole-consumer.py", "finite-verify":"independent-finite-checker.py"}
CAP_MS = {"source":3600000, "finite":3600000, "aggregate":7200000}
CAP_BYTES = {"source":48*(1 << 20), "finite":16*(1 << 20), "aggregate":64*(1 << 20)}
CONSOLE_RESERVE, TERMINAL_RESERVE = 4096, 262144


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def utc():
    return datetime.now(timezone.utc).isoformat()


def pack(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))+"\n").encode("ascii")


def unique(rows):
    out = {}
    for key, value in rows:
        need(key not in out, "DUPLICATE_JSON_KEY")
        out[key] = value
    return out


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique,
                      parse_constant=lambda _: need(False, "NONFINITE_JSON"))


def uint(x, name, maximum=None):
    need(type(x) is int and x >= 0 and (maximum is None or x <= maximum), name+"_UINT_RANGE")
    return x


def path(root, name):
    need(type(name) is str and name and ":" not in name and "\\" not in name
         and all(x not in ("", ".", "..") for x in name.split("/")), "CANONICAL_RELATIVE_PATH")
    result = root.joinpath(*name.split("/")).resolve()
    need(result.is_relative_to(root.resolve()), "PATH_OUTSIDE_WORKSPACE")
    return result


def pin(root, item, limit=4*(1 << 20)):
    need(type(item) is dict and set(item) == {"path", "bytes", "sha256"}, "PIN_SHAPE")
    uint(item["bytes"], "PIN_BYTES", limit)
    need(type(item["sha256"]) is str and re.fullmatch("[0-9a-f]{64}", item["sha256"]), "PIN_SHA")
    p = path(root, item["path"])
    need(p.is_file() and p.stat().st_size == item["bytes"], "PIN_SIZE")
    raw = p.read_bytes()
    need(len(raw) == item["bytes"] and hashlib.sha256(raw).hexdigest() == item["sha256"], "PIN_HASH")
    return raw


def record_pin(root, p):
    raw = p.read_bytes()
    return {"path":p.relative_to(root).as_posix(), "bytes":len(raw), "sha256":hashlib.sha256(raw).hexdigest()}


def save_new(p, value, maximum=65536):
    raw = pack(value)
    need(len(raw) <= maximum, "BOUNDED_OBSERVER_RECORD")
    with p.open("xb") as handle:
        handle.write(raw); handle.flush(); os.fsync(handle.fileno())
    return len(raw)


class WindowsTree:
    """One suspended process atomically assigned to a non-breakaway job.

    No process is created until all job/attribute/std-handle setup succeeds.
    JOB_LIST assignment is part of CreateProcess, closing the suspended-orphan
    window of a later AssignProcessToJobObject call. This backend needs Win10+.
    """
    def __init__(self, command, cwd, stdin_fd, stdout_fd, stderr_fd):
        need(os.name == "nt", "WINDOWS10_JOB_BACKEND_REQUIRED")
        import msvcrt
        C, W = ctypes, wintypes
        self.k = C.WinDLL("kernel32", use_last_error=True)
        self.job = self.process = self.thread = None
        self.pid = None
        self.console_pids = set()
        self.historical_processes = 0
        SIZE = C.c_size_t
        HANDLE = W.HANDLE
        class BASIC(C.Structure):
            _fields_ = [("PerProcessUserTimeLimit",C.c_longlong),("PerJobUserTimeLimit",C.c_longlong),
                ("LimitFlags",W.DWORD),("MinimumWorkingSetSize",SIZE),("MaximumWorkingSetSize",SIZE),
                ("ActiveProcessLimit",W.DWORD),("Affinity",SIZE),("PriorityClass",W.DWORD),
                ("SchedulingClass",W.DWORD)]
        class IO(C.Structure):
            _fields_ = [(name,C.c_ulonglong) for name in
                        ("ReadOperationCount","WriteOperationCount","OtherOperationCount",
                         "ReadTransferCount","WriteTransferCount","OtherTransferCount")]
        class EXTENDED(C.Structure):
            _fields_ = [("BasicLimitInformation",BASIC),("IoInfo",IO),
                ("ProcessMemoryLimit",SIZE),("JobMemoryLimit",SIZE),
                ("PeakProcessMemoryUsed",SIZE),("PeakJobMemoryUsed",SIZE)]
        class STARTUP(C.Structure):
            _fields_ = [("cb",W.DWORD),("lpReserved",W.LPWSTR),("lpDesktop",W.LPWSTR),
                ("lpTitle",W.LPWSTR),("dwX",W.DWORD),("dwY",W.DWORD),("dwXSize",W.DWORD),
                ("dwYSize",W.DWORD),("dwXCountChars",W.DWORD),("dwYCountChars",W.DWORD),
                ("dwFillAttribute",W.DWORD),("dwFlags",W.DWORD),("wShowWindow",W.WORD),
                ("cbReserved2",W.WORD),("lpReserved2",C.c_void_p),
                ("hStdInput",HANDLE),("hStdOutput",HANDLE),("hStdError",HANDLE)]
        class STARTUP_EX(C.Structure):
            _fields_ = [("StartupInfo",STARTUP),("lpAttributeList",C.c_void_p)]
        class PROCESS_INFO(C.Structure):
            _fields_ = [("hProcess",HANDLE),("hThread",HANDLE),("dwProcessId",W.DWORD),("dwThreadId",W.DWORD)]
        class ACCOUNTING(C.Structure):
            _fields_ = [("TotalUserTime",C.c_longlong),("TotalKernelTime",C.c_longlong),
                ("ThisPeriodTotalUserTime",C.c_longlong),("ThisPeriodTotalKernelTime",C.c_longlong),
                ("TotalPageFaultCount",W.DWORD),("TotalProcesses",W.DWORD),
                ("ActiveProcesses",W.DWORD),("TotalTerminatedProcesses",W.DWORD)]
        self.account_type = ACCOUNTING
        specs = {
            "CreateJobObjectW":([C.c_void_p,W.LPCWSTR],HANDLE),
            "SetInformationJobObject":([HANDLE,C.c_int,C.c_void_p,W.DWORD],W.BOOL),
            "InitializeProcThreadAttributeList":([C.c_void_p,W.DWORD,W.DWORD,C.POINTER(SIZE)],W.BOOL),
            "UpdateProcThreadAttribute":([C.c_void_p,W.DWORD,SIZE,C.c_void_p,SIZE,C.c_void_p,C.c_void_p],W.BOOL),
            "DeleteProcThreadAttributeList":([C.c_void_p],None),
            "CreateProcessW":([W.LPCWSTR,W.LPWSTR,C.c_void_p,C.c_void_p,W.BOOL,W.DWORD,
                               C.c_void_p,W.LPCWSTR,C.POINTER(STARTUP),C.POINTER(PROCESS_INFO)],W.BOOL),
            "ResumeThread":([HANDLE],W.DWORD),"CloseHandle":([HANDLE],W.BOOL),
            "WaitForSingleObject":([HANDLE,W.DWORD],W.DWORD),
            "GetExitCodeProcess":([HANDLE,C.POINTER(W.DWORD)],W.BOOL),
            "SetHandleInformation":([HANDLE,W.DWORD,W.DWORD],W.BOOL),
            "TerminateJobObject":([HANDLE,W.UINT],W.BOOL),
            "QueryInformationJobObject":([HANDLE,C.c_int,C.c_void_p,W.DWORD,C.POINTER(W.DWORD)],W.BOOL),
            "OpenProcess":([W.DWORD,W.BOOL,W.DWORD],HANDLE),
            "QueryFullProcessImageNameW":([HANDLE,W.DWORD,W.LPWSTR,C.POINTER(W.DWORD)],W.BOOL),
            "GetSystemDirectoryW":([W.LPWSTR,W.UINT],W.UINT),
        }
        for name,(args,restype) in specs.items():
            fn = getattr(self.k,name); fn.argtypes = args; fn.restype = restype
        attribute = None
        attribute_initialized = False
        inherited = []
        try:
            self.job = self.k.CreateJobObjectW(None,None)
            self.check(self.job,"CREATE_JOB")
            limits = EXTENDED(); limits.BasicLimitInformation.LimitFlags = 0x2000  # KILL_ON_JOB_CLOSE only.
            self.check(self.k.SetInformationJobObject(self.job,9,C.byref(limits),C.sizeof(limits)),"JOB_KILL_ON_CLOSE")
            size = SIZE()
            self.k.InitializeProcThreadAttributeList(None,2,0,C.byref(size))
            need(0 < size.value <= 65536,"ATTRIBUTE_LIST_SIZE")
            buffer = C.create_string_buffer(size.value)
            attribute = C.cast(buffer,C.c_void_p)
            self.check(self.k.InitializeProcThreadAttributeList(attribute,2,0,C.byref(size)),"INIT_ATTRIBUTES")
            attribute_initialized = True
            jobs = (HANDLE*1)(self.job)
            handles = (HANDLE*3)(*[msvcrt.get_osfhandle(fd) for fd in (stdin_fd,stdout_fd,stderr_fd)])
            for handle in handles:
                self.check(self.k.SetHandleInformation(handle,1,1),"INHERIT_STD_HANDLE")
                inherited.append(handle)
            # ProcThreadAttributeValue(JobList=13,input=True)=0x2000D.
            self.check(self.k.UpdateProcThreadAttribute(attribute,0,0x2000D,C.byref(jobs),C.sizeof(jobs),None,None),"ATOMIC_JOB_LIST")
            self.check(self.k.UpdateProcThreadAttribute(attribute,0,0x20002,C.byref(handles),C.sizeof(handles),None,None),"STD_HANDLE_LIST")
            startup = STARTUP_EX(); startup.StartupInfo.cb = C.sizeof(startup)
            startup.StartupInfo.dwFlags = 0x100
            startup.StartupInfo.hStdInput, startup.StartupInfo.hStdOutput, startup.StartupInfo.hStdError = handles
            startup.lpAttributeList = attribute
            info = PROCESS_INFO()
            command_line = C.create_unicode_buffer(subprocess.list2cmdline(command))
            flags = 0x4 | 0x80000 | 0x08000000  # SUSPENDED|EXTENDED_STARTUPINFO|NO_WINDOW.
            self.check(self.k.CreateProcessW(command[0],command_line,None,None,True,flags,None,str(cwd),
                                            C.byref(startup.StartupInfo),C.byref(info)),"CREATE_PROCESS_IN_JOB")
            self.process,self.thread,self.pid = info.hProcess,info.hThread,int(info.dwProcessId)
            system = C.create_unicode_buffer(32768)
            length = self.k.GetSystemDirectoryW(system,len(system))
            need(0 < length < len(system),"SYSTEM_DIRECTORY_BOUND")
            self.console_image = os.path.normcase(str(Path(system.value)/"conhost.exe"))
            self.members()  # Capture OS-console role before resuming science.
        except BaseException:
            self.close()
            raise
        finally:
            if attribute_initialized:
                self.k.DeleteProcThreadAttributeList(attribute)
            for handle in inherited:
                self.k.SetHandleInformation(handle,1,0)

    def check(self, ok, name):
        if not ok:
            raise OSError(ctypes.get_last_error(),name)

    def resume(self):
        need(self.thread is not None,"ALREADY_RESUMED")
        self.check(self.k.ResumeThread(self.thread) != 0xFFFFFFFF,"RESUME_CHILD")
        self.k.CloseHandle(self.thread); self.thread = None

    def poll(self):
        state = self.k.WaitForSingleObject(self.process,0)
        if state == 258:
            return None
        need(state == 0,"WAIT_CHILD_FAILURE")
        code = wintypes.DWORD()
        self.check(self.k.GetExitCodeProcess(self.process,ctypes.byref(code)),"CHILD_EXIT_CODE")
        return int(code.value)

    def counts(self):
        info = self.account_type()
        self.check(self.k.QueryInformationJobObject(self.job,1,ctypes.byref(info),ctypes.sizeof(info),None),"JOB_ACCOUNTING")
        self.historical_processes = max(self.historical_processes,int(info.TotalProcesses))
        return int(info.TotalProcesses),int(info.ActiveProcesses)

    def members(self):
        # Hidden console Python can have a system conhost in the job. It is OS
        # control overhead, not another scientific kernel. No basename-only
        # whitelist: the queried image must equal GetSystemDirectoryW/conhost.exe.
        C = ctypes
        buffer = C.create_string_buffer(8+256*C.sizeof(C.c_size_t))
        self.check(self.k.QueryInformationJobObject(self.job,3,buffer,len(buffer),None),"JOB_PROCESS_IDS")
        count = C.c_uint32.from_buffer(buffer,4).value
        need(count <= 256,"JOB_PROCESS_ID_COUNT")
        pids = (C.c_size_t*count).from_buffer(buffer,8)
        records = []
        for value in pids:
            pid = int(value)
            if pid == self.pid:
                records.append({"pid":pid,"role":"DIRECT_SCIENTIFIC_CHILD"})
                continue
            handle = self.k.OpenProcess(0x1000,False,pid)
            if not handle:
                records.append({"pid":pid,"role":"UNCLASSIFIED_OR_EXITED_DESCENDANT"})
                continue
            try:
                image = C.create_unicode_buffer(32768);length = wintypes.DWORD(len(image))
                good = self.k.QueryFullProcessImageNameW(handle,0,image,C.byref(length))
                if good and os.path.normcase(image.value) == self.console_image:
                    self.console_pids.add(pid)
                    records.append({"pid":pid,"role":"EXACT_SYSTEM_CONSOLE_METADATA","image":self.console_image})
                else:
                    records.append({"pid":pid,"role":"UNEXPECTED_DESCENDANT"})
            finally:
                self.k.CloseHandle(handle)
        return records

    def unexpected_descendants(self):
        members = self.members()
        unknown = any(r["role"] not in ("DIRECT_SCIENTIFIC_CHILD","EXACT_SYSTEM_CONSOLE_METADATA") for r in members)
        total,active = self.counts()
        # A process that exited before image classification is not silently paid.
        return unknown or total > 1+len(self.console_pids),members

    def kill(self):
        if self.job:
            self.check(self.k.TerminateJobObject(self.job,0xC069),"KILL_PROCESS_TREE")

    def wait(self, seconds=5):
        need(self.k.WaitForSingleObject(self.process,int(seconds*1000)) == 0,"CHILD_KILL_WAIT_TIMEOUT")
        return self.poll()

    def wait_empty(self, seconds=5):
        until = time.monotonic()+seconds
        while self.counts()[1] != 0:
            need(time.monotonic() <= until,"DESCENDANTS_NOT_TERMINAL")
            time.sleep(0.02)

    def close(self):
        if getattr(self,"job",None):
            self.k.CloseHandle(self.job);self.job = None  # Kills descendants, even on observer exit.
        for name in ("thread","process"):
            handle = getattr(self,name,None)
            if handle:
                self.k.CloseHandle(handle);setattr(self,name,None)


class Capture:
    """Drain one pipe, persist at most limit bytes, signal overflow immediately.

    On overflow the phase is UNCONSUMABLE. Read/discard counters and possible
    unread pipe bytes are explicit; a truncated stdout is never called a complete
    output/cap certificate. The watchdog kills the whole job on that signal.
    """
    def __init__(self, destination, limit, stop):
        self.read_fd,self.write_fd = os.pipe()
        self.destination,self.limit,self.stop = destination,limit,stop
        self.read_bytes = self.saved_bytes = 0
        self.error = None
        self.thread = threading.Thread(target=self.drain,daemon=True)
        self.thread.start()

    def drain(self):
        try:
            with os.fdopen(self.read_fd,"rb",buffering=0) as reader, self.destination.open("xb") as writer:
                while True:
                    data = reader.read(4096)
                    if not data:
                        break
                    self.read_bytes += len(data)
                    kept = data[:max(0,self.limit-self.saved_bytes)]
                    if kept:
                        writer.write(kept);writer.flush();self.saved_bytes += len(kept)
                    if len(kept) != len(data):
                        self.stop.set()
                writer.flush();os.fsync(writer.fileno())
        except BaseException as error:
            self.error = type(error).__name__+":"+str(error)[:256]
            self.stop.set()

    def inherited(self):
        os.close(self.write_fd);self.write_fd = None

    def finish(self):
        if self.write_fd is not None:
            self.inherited()
        self.thread.join(timeout=2)
        need(not self.thread.is_alive(),"CAPTURE_THREAD_NOT_TERMINAL")

    def summary(self, root):
        return {"pin":record_pin(root,self.destination),"bytesRead":self.read_bytes,
                "bytesSaved":self.saved_bytes,"omittedReadBytes":self.read_bytes-self.saved_bytes,
                "captureError":self.error,"unreadPipeBytesMayExistAfterOverflow":self.stop.is_set()}


def child_command(root, phase, freeze_relative):
    need(phase in PHASES,"FIXED_PHASE")
    code = path(root,BASE+CODES[phase])
    command = [sys.executable,str(code)]
    if phase.startswith("source-"):
        command.append("produce" if phase.endswith("produce") else "verify")
        freeze_arg = freeze_relative
    else:
        freeze_arg = str(path(root,freeze_relative))
    return command+["--root-freeze-file",freeze_arg]


def prior_costs(prior, phase):
    need(prior["schema"] == "RH_WEIL_GLOBAL_OBSERVER_PRIOR_ACCOUNTING_V1"
         and prior["status"] == "ROOT_VERIFIED_ALL_PRIOR_SCIENTIFIC_PROCESSES_TERMINAL"
         and prior["targetId"] == TARGET and prior["runtimeGoalCreatedAt"] == GOAL
         and prior["contractId"] == "C069" and prior["noLiveScientificProcesses"] is True,
         "ACTUAL_ROOT_PRIOR_ACCOUNTING")
    st,ft = (uint(prior[k],k,3600000) for k in ("sourceConsumedUpperMs","finiteConsumedUpperMs"))
    sb,fb = (uint(prior[k],k,CAP_BYTES[s]) for k,s in
             (("sourceChargedUpperBytes","source"),("finiteChargedUpperBytes","finite")))
    entries = prior["phaseLifetimes"]
    need([x["phase"] for x in entries] == list(PHASES[:PHASES.index(phase)]),"EXACT_PRIOR_PHASES_NO_RETRY")
    sums = {"source":0,"finite":0}
    for entry in entries:
        ms = uint(entry["fullObservedUpperMs"],"PRIOR_FULL_PHASE_MS")
        need(ms > 0 and entry["exitCode"] == 0 and entry["enclosedChildAddedAgain"] is False,
             "PRIOR_SUCCESS_AND_NO_DOUBLECOUNT")
        sums[entry["phase"].split("-")[0]] += ms
    need(st >= sums["source"] and ft >= sums["finite"] and st+ft <= CAP_MS["aggregate"],"ALL_PRIOR_LIFETIMES_SUMMED")
    return {"sourceMs":st,"finiteMs":ft,"sourceBytes":sb,"finiteBytes":fb}


def limits_ok(limits, costs, phase):
    stage = phase.split("-")[0]
    allowance = uint(limits["phaseAllowanceMs"],"ALLOWANCE",3600000)
    internal = uint(limits["internalScientificCutoffMs"],"INTERNAL",3600000)
    external = uint(limits["externalObserverChildTimeoutMs"],"EXTERNAL",3600000)
    need(0 < internal <= external-10000 and external+20000 <= allowance
         and allowance <= min(3600000-costs[stage+"Ms"],7200000-costs["sourceMs"]-costs["finiteMs"]),
         "REMAINING_PHASE_AND_TERMINAL_RESERVES")


def ready_value(arm, phase, observer_pin):
    item = {"observerPhase":phase,"observerPID":os.getpid(),"parentPID":os.getppid(),
            "observerCodePin":observer_pin,"phaseLimits":arm["phaseLimits"],
            "externalOutputPaths":arm["externalOutputPaths"],"readyUTC":utc(),
            "runtimeGoalCreatedAt":GOAL,"contractId":"C069","targetId":TARGET,
            "launchNonce":arm["armIdentity"],"freezeIdentity":arm["armIdentity"],
            "codePin":arm["childCodePin"],"rootMustVerifyFullLifetimeAfterTerminal":True,
            "armPin":arm["_armPin"],"rootArmGatePin":arm["rootArmGatePin"],
            "rootAdmissionPin":arm["rootAdmissionPin"],"priorAccountingPin":arm["priorAccountingPin"],
            "observerClaimPin":arm["_claimPin"],"noRetry":True}
    if phase.startswith("source-"):
        item.update(schema="RH_WEIL_SOURCE_EXTERNAL_OBSERVER_LAUNCH_V1",phase=phase.split("-")[1])
    elif phase == "finite-produce":
        item.update(schema="RH_WEIL_GLOBAL_FINITE_PRODUCER_ROOT_ATTEMPT_V1",
                    status="ROOT_CLAIMED_ONE_GLOBAL_FINITE_PRODUCER",currentStage="stage-02-finite")
    else:
        item.update(schema="RH_WEIL_GLOBAL_FINITE_REPLAY_ROOT_ATTEMPT_V1",
                    status="ROOT_CLAIMED_ONE_FINITE_REPLAY",currentStage="stage-02-finite-checker")
    return item


def final_gate(root, arm, phase, ready_pin):
    freeze_raw = path(root,arm["finalFreezeRelativePath"]).read_bytes()
    need(len(freeze_raw) <= 2*(1 << 20),"FINAL_FREEZE_BOUND")
    freeze = decode(freeze_raw)
    gate = decode(pin(root,freeze["rootGatePin"]))
    need(freeze["rootGatePin"]["path"] == arm["finalRootGateRelativePath"],"EXACT_FINAL_GATE_PATH")
    for obj in (freeze,gate):
        need(obj["runtimeGoalCreatedAt"] == GOAL and obj["contractId"] == "C069"
             and obj["targetId"] == TARGET and obj["contractPin"] == arm["contractPin"],"FINAL_GATE_SCOPE")
    if phase.startswith("source-"):
        need(freeze["schema"] == "RH_WEIL_GLOBAL_SOURCE_PHASE_FREEZE_V1"
             and freeze["authorization"] == "ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION"
             and gate["schema"] == "RH_WEIL_GLOBAL_SOURCE_PHASE_ROOT_GATE_V1"
             and gate["status"] == "ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION_APPROVED", "FINAL_SOURCE_GATE")
        for obj in (freeze,gate):
            need(obj["launchPin"] == ready_pin and obj["controllerPin"] == arm["childCodePin"]
                 and obj["phase"] == phase.split("-")[1]
                 and obj["freezeIdentity"] == arm["armIdentity"] and obj["phaseLimits"] == arm["phaseLimits"]
                 and pack(obj["externalOutputPaths"]) == pack(arm["externalOutputPaths"]),"SOURCE_READY_BINDING")
        child_prior = decode(pin(root,freeze["priorAccountingPin"]))
        need(child_prior["sourceObservedUpperMs"] >= arm["_costs"]["sourceMs"]
             and child_prior["aggregateObservedUpperMs"] >= arm["_costs"]["sourceMs"]+arm["_costs"]["finiteMs"]
             and child_prior["sourceChargedUpperBytes"] >= arm["_costs"]["sourceBytes"]
             and child_prior["aggregateChargedUpperBytes"] >= arm["_costs"]["sourceBytes"]+arm["_costs"]["finiteBytes"],
             "CHILD_SOURCE_PRIOR_CANNOT_DISCOUNT_ARM_PRIOR")
        child_metadata = freeze["chargedMetadataPins"]
    else:
        replay = phase == "finite-verify"
        expected = "RH_WEIL_GLOBAL_FINITE_REPLAY_FREEZE_V1" if replay else "RH_WEIL_GLOBAL_FINITE_FREEZE_V1"
        expected_gate = "RH_WEIL_GLOBAL_FINITE_REPLAY_ROOT_GATE_V1" if replay else "RH_WEIL_GLOBAL_FINITE_ROOT_GATE_V1"
        authorization = "ROOT_EXPLICIT_C069_GLOBAL_FINITE_REPLAY" if replay else "ROOT_EXPLICIT_C069_GLOBAL_FINITE_EXECUTION"
        need(freeze["schema"] == expected and gate["schema"] == expected_gate,"FINAL_FINITE_GATE_SCHEMA")
        for obj in (freeze,gate):
            need(obj["authorization"] == authorization and obj["numericalExecutionAuthorized"] is True
                 and obj["externalAttemptPin"] == ready_pin and obj["launchNonce"] == arm["armIdentity"]
                 and obj["codePin"] == arm["childCodePin"]
                 and set(obj["externalRuntimePaths"]) == {x["path"] for x in arm["externalOutputPaths"]},
                 "FINITE_READY_AND_OUTPUT_BINDING")
        deadline = freeze["budget"]["checkerDeadlineSeconds" if replay else "producerDeadlineSeconds"]
        need(type(deadline) in (int,float) and math.isfinite(deadline) and deadline > 0
             and deadline*1000 <= arm["phaseLimits"]["internalScientificCutoffMs"],"FINITE_INTERNAL_DEADLINE")
        b = freeze["budget"]
        need(b["sourceConsumedUpperSeconds"]*1000 >= arm["_costs"]["sourceMs"]
             and b["finiteConsumedUpperSeconds" if replay else "finitePriorUpperSeconds"]*1000 >= arm["_costs"]["finiteMs"]
             and b["sourceConsumedOutputBytes"] >= arm["_costs"]["sourceBytes"]
             and b["finiteConsumedOutputBytes" if replay else "finitePriorOutputBytes"] >= arm["_costs"]["finiteBytes"],
             "CHILD_FINITE_PRIOR_CANNOT_DISCOUNT_ARM_PRIOR")
        child_metadata = {x["path"]:x for x in freeze["chargedMetadataPins"]}
    for name,item in (arm["_metadataPins"]|{arm["_claimPin"]["path"]:arm["_claimPin"]}).items():
        need(child_metadata.get(name) == item,"CHILD_MUST_CHARGE_OBSERVER_ARM_METADATA")
    pin(root,arm["childCodePin"])
    return freeze, {"path":arm["finalFreezeRelativePath"],"bytes":len(freeze_raw),
                    "sha256":hashlib.sha256(freeze_raw).hexdigest()}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("phase",choices=PHASES)
    parser.add_argument("--root-arm-file",required=True)
    args = parser.parse_args(argv)
    owned = tree = None
    captures = []
    exit_code = child_started = child_ended = child_pid = None
    reason, overflow, descendants = None, False, False
    console_pids = []
    historical_total, last_members = 0, []
    metadata, baseline, external, stage = {}, {}, {}, args.phase.split("-")[0]
    try:
        arm_path = path(ROOT,args.root_arm_file)
        need(arm_path.stat().st_size <= 262144,"ARM_BOUND")
        arm_raw = arm_path.read_bytes();arm = decode(arm_raw)
        gate = decode(pin(ROOT,arm["rootArmGatePin"]))
        need(arm["schema"] == "RH_WEIL_GLOBAL_OBSERVER_ARM_V1"
             and arm["authorization"] == "ROOT_EXPLICIT_C069_OBSERVER_ARM_ONLY"
             and gate["schema"] == "RH_WEIL_GLOBAL_OBSERVER_ARM_ROOT_GATE_V1"
             and gate["status"] == "ROOT_EXPLICIT_OBSERVER_ARM_APPROVED", "NEW_ROOT_ARM_REQUIRED")
        fields = ("phase","runtimeGoalCreatedAt","contractId","targetId","armIdentity","observerCodePin",
                  "childCodePin","contractPin","rootAdmissionPin","priorAccountingPin","phaseLimits",
                  "armWaitMaxMs","externalOutputPaths","finalFreezeRelativePath","finalRootGateRelativePath",
                  "reviewPins","chargedMetadataPins")
        need(all(arm[k] == gate[k] for k in fields) and gate["armRelativePath"] == args.root_arm_file,
             "ROOT_ARM_SEMANTIC_MATCH")
        need(arm["phase"] == args.phase and arm["runtimeGoalCreatedAt"] == GOAL
             and arm["contractId"] == "C069" and arm["targetId"] == TARGET
             and gate["sameRuntimeGoalLiveAndActiveChecked"] is True,"ARM_SAME_ACTIVE_GOAL")
        need(type(arm["armIdentity"]) is str and re.fullmatch("[A-Za-z0-9_-]{16,128}",arm["armIdentity"]),"ARM_NONCE")
        need(path(ROOT,arm["observerCodePin"]["path"]) == SELF
             and pin(ROOT,arm["observerCodePin"]) == SELF.read_bytes(),"EXACT_OBSERVER_SELF")
        need(arm["childCodePin"]["path"] == BASE+CODES[args.phase],"FIXED_CHILD_PATH")
        pin(ROOT,arm["childCodePin"])
        need(arm["contractPin"]["path"] == "goals/contracts/C069-global-exact-directional-whole.md", "ACTUAL_NEW_C069_CONTRACT")
        pin(ROOT,arm["contractPin"])
        admission = decode(pin(ROOT,arm["rootAdmissionPin"]))
        need(admission["schema"] == "RH_WEIL_C069_IRREVOCABLE_OBSERVER_ARM_ADMISSION_V1"
             and admission["status"] == "ADMITTED_BEFORE_ARM_NO_RETRY"
             and admission["armIdentity"] == arm["armIdentity"] and admission["phase"] == args.phase
             and admission["runtimeGoalCreatedAt"] == GOAL and admission["contractId"] == "C069"
             and admission["targetId"] == TARGET,"IRREVOCABLE_ARM_ADMISSION")
        owners,roles = set(),set()
        for review in arm["reviewPins"]:
            data = pin(ROOT,review["pin"])
            need(review["role"] in ("math","protocol") and type(review["owner"]) is str
                 and review["owner"] and review["observerSHA256"] == arm["observerCodePin"]["sha256"]
                 and review["childSHA256"] == arm["childCodePin"]["sha256"]
                 and review["observerSHA256"].encode() in data and review["childSHA256"].encode() in data,
                 "FINAL_OBSERVER_CHILD_REVIEW")
            owners.add(review["owner"]);roles.add(review["role"])
        need(len(owners) >= 2 and roles == {"math","protocol"},"DISTINCT_FINAL_ARM_REVIEWS")
        prior = decode(pin(ROOT,arm["priorAccountingPin"]))
        costs = prior_costs(prior,args.phase);limits_ok(arm["phaseLimits"],costs,args.phase)
        arm["_costs"] = costs
        wait_ms = uint(arm["armWaitMaxMs"],"ARM_WAIT",60000)
        need(0 < wait_ms < arm["phaseLimits"]["phaseAllowanceMs"]-30000,"BOUNDED_ARM_WAIT")
        for name,p in prior["baselinePins"].items():
            need(p["path"] == name,"BASELINE_PIN_NAME");pin(ROOT,p,limit=64*(1 << 20));baseline[name] = p
        phase_dir = OBSERVER+"/"+args.phase
        need(arm["finalFreezeRelativePath"] == phase_dir+"/final-freeze.json"
             and arm["finalRootGateRelativePath"] == phase_dir+"/final-root-gate.json", "FRESH_PHASE_FREEZE_PATHS")
        external = {x["path"]:x["maxBytes"] for x in arm["externalOutputPaths"]}
        need(len(external) == len(arm["externalOutputPaths"]) and set(external) ==
             {phase_dir+"/"+n for n in ("stdout.txt","stderr.txt","child.json","terminal.json","root-observed.json")},
             "EXACT_EXTERNAL_OUTPUT_DESTINATIONS")
        for name,maximum in external.items():
            path(ROOT,name);uint(maximum,"EXTERNAL_MAX",131072)
        need(external[phase_dir+"/child.json"] >= 4096 and external[phase_dir+"/terminal.json"] >= 65536
             and sum(external.values()) <= 524288,"BOUNDED_TERMINAL_AND_CAPTURE_RESERVES")
        for name,p in arm["chargedMetadataPins"].items():
            need(p["path"] == name,"METADATA_PIN_NAME");pin(ROOT,p);metadata[name] = p
        for p in (arm["rootArmGatePin"],arm["rootAdmissionPin"],arm["priorAccountingPin"],arm["contractPin"]):
            metadata[p["path"]] = p
        metadata[args.root_arm_file] = record_pin(ROOT,arm_path)
        arm["_metadataPins"] = metadata
        need(not any(path(ROOT,n).exists() for n in (arm["finalFreezeRelativePath"],arm["finalRootGateRelativePath"])),
             "FREEZE_MUST_BE_WRITTEN_AFTER_READY")
        owned = path(ROOT,phase_dir);owned.mkdir(parents=True,exist_ok=False)
        save_new(owned/"claim.json",{"schema":"RH_WEIL_GLOBAL_OBSERVER_ONCE_ARM_CLAIM_V1",
            "phase":args.phase,"observerPID":os.getpid(),"createdUTC":utc(),
            "targetId":TARGET,"runtimeGoalCreatedAt":GOAL,"contractId":"C069",
            "armIdentity":arm["armIdentity"],"armPin":metadata[args.root_arm_file],"noRetry":True})
        arm["_armPin"],arm["_claimPin"] = metadata[args.root_arm_file],record_pin(ROOT,owned/"claim.json")
        save_new(owned/"ready.json",ready_value(arm,args.phase,arm["observerCodePin"]))
        ready_pin = record_pin(ROOT,owned/"ready.json")
        # Poll metadata only. READY's actual PID breaks the PID/freeze pin cycle.
        def guard():
            elapsed = math.ceil((time.monotonic()-STARTED)*1000)
            need(elapsed+20000 <= arm["phaseLimits"]["phaseAllowanceMs"],"FULL_OBSERVER_PHASE_DEADLINE")
            seen = {}
            for directory in (path(ROOT,OUTER),path(ROOT,OBSERVER)):
                if directory.exists():
                    for p in directory.rglob("*"):
                        if p.is_file():
                            need(p.resolve().is_relative_to(directory),"OUTPUT_LINK_ESCAPE")
                            name = p.relative_to(ROOT).as_posix()
                            if name not in baseline:
                                seen[name] = p.stat().st_size
            for name,p in metadata.items():
                if name not in baseline:
                    seen[name] = p["bytes"]
            for name,maximum in external.items():
                p = path(ROOT,name)
                if p.exists():
                    need(p.stat().st_size <= maximum,"EXTERNAL_OUTPUT_CAP")
            added = sum(seen.values())+TERMINAL_RESERVE+CONSOLE_RESERVE
            need(costs[stage+"Bytes"]+added <= CAP_BYTES[stage]
                 and costs["sourceBytes"]+costs["finiteBytes"]+added <= CAP_BYTES["aggregate"],"ACTUAL_PHASE_OUTPUT_CAP")
            return added
        armed_at = time.monotonic()
        while not (path(ROOT,arm["finalFreezeRelativePath"]).is_file()
                   and path(ROOT,arm["finalRootGateRelativePath"]).is_file()):
            guard();need((time.monotonic()-armed_at)*1000 <= wait_ms,"ARMED_WAIT_EXHAUSTED_NO_CHILD")
            time.sleep(0.1)
        _,freeze_pin = final_gate(ROOT,arm,args.phase,ready_pin)
        guard()
        remaining = arm["phaseLimits"]["phaseAllowanceMs"]-math.ceil((time.monotonic()-STARTED)*1000)-20000
        child_timeout_ms = min(arm["phaseLimits"]["externalObserverChildTimeoutMs"],remaining)
        need(child_timeout_ms > 1000,"NO_FUNDED_CHILD_WINDOW_AFTER_ARM_WAIT")
        stop = threading.Event()
        captures = [Capture(owned/"stdout.txt",external[phase_dir+"/stdout.txt"],stop),
                    Capture(owned/"stderr.txt",external[phase_dir+"/stderr.txt"],stop)]
        need(not stop.is_set(),"CAPTURE_SETUP_FAILED_BEFORE_CHILD")
        with open(os.devnull,"rb") as stdin:
            command = child_command(ROOT,args.phase,arm["finalFreezeRelativePath"])
            child_started = time.monotonic()
            tree = WindowsTree(command,ROOT,stdin.fileno(),captures[0].write_fd,captures[1].write_fd)
            child_pid = tree.pid
            for capture in captures:
                capture.inherited()
            save_new(owned/"child.json",{"schema":"RH_WEIL_GLOBAL_OBSERVER_CHILD_CREATED_V1",
                "phase":args.phase,"observerPID":os.getpid(),"childPID":tree.pid,
                "createdSuspendedInKillOnCloseJob":True,"command":command,"freezePin":freeze_pin,
                "readyPin":ready_pin,"createdUTC":utc(),"actualChildTimeoutMs":child_timeout_ms,
                "armAndValidationAlreadyElapsedMs":math.ceil((child_started-STARTED)*1000),
                "initialJobMembers":tree.members(),"noRetry":True})
            tree.resume()
            while True:
                unexpected,members = tree.unexpected_descendants()
                historical_total = max(historical_total,tree.historical_processes)
                last_members = members
                if unexpected:
                    descendants = True;reason = "UNEXPECTED_DESCENDANT_PROCESS";break
                if stop.is_set():
                    overflow = True;reason = "BOUNDED_CAPTURE_OVERFLOW_OR_FAILURE";break
                guard()
                exit_code = tree.poll()
                if exit_code is not None:
                    break
                if (time.monotonic()-child_started)*1000 > child_timeout_ms:
                    reason = "STRICTER_CHILD_WATCHDOG_TIMEOUT";break
                time.sleep(0.05)
            if reason is not None:
                tree.kill()
            exit_code = tree.wait(5)
            child_ended = time.monotonic()
            unexpected,members = tree.unexpected_descendants()
            historical_total = max(historical_total,tree.historical_processes)
            last_members = members
            if unexpected:
                descendants = True;reason = reason or "UNEXPECTED_DESCENDANT_PROCESS"
            tree.kill()  # Also kills an orphaned descendant after normal direct-child exit.
            tree.wait_empty(5)
            console_pids = sorted(tree.console_pids)
            for capture in captures:
                capture.finish()
            tree.close();tree = None
        guard()
        need(not any(c.error or c.read_bytes != c.saved_bytes for c in captures),"INCOMPLETE_CAPTURE")
        status = "CHILD_EXIT0_REQUIRES_ROOT_FULL_PHASE_ACCOUNTING" if exit_code == 0 and reason is None else "GLOBAL_OBSERVER_TECHNICAL_STOP_NO_RETRY"
        multiplicity = max(1,historical_total) if descendants else 1
        elapsed_ceiling = math.ceil((time.monotonic()-STARTED)*1000)
        summary = {"schema":"RH_WEIL_GLOBAL_OBSERVER_TERMINAL_V1","status":status,"phase":args.phase,
            "targetId":TARGET,"runtimeGoalCreatedAt":GOAL,"contractId":"C069","observerPID":os.getpid(),
            "childPID":child_pid,"historicalJobProcessCount":historical_total,"lastClassifiedJobMembers":last_members,
            "exitCode":exit_code,"failure":reason,"overflow":overflow,"unexpectedDescendants":descendants,
            "exactSystemConsoleMetadataPIDs":console_pids,"consoleMetadataIsObserverOverhead":True,
            "scientificProcessMultiplicityUpper":multiplicity,
            "rootMustMultiplyFullObservedPhaseMsByMultiplicity":multiplicity,
            "internalAllScientificLifetimeUpperMs":elapsed_ceiling*multiplicity,
            "internalConservativeLifetimeCapViolation":costs[stage+"Ms"]+elapsed_ceiling*multiplicity > 3600000
                or costs["sourceMs"]+costs["finiteMs"]+elapsed_ceiling*multiplicity > 7200000,
            "childCreationToObservedExitUpperMs":math.ceil((child_ended-child_started)*1000),
            "observerInternalFullElapsedCeilingMs":elapsed_ceiling,
            "observerInternalStartedEpoch":STARTED_UTC,"endedUTC":utc(),"captures":[c.summary(ROOT) for c in captures],
            "readyPin":ready_pin,"freezePin":freeze_pin,"phaseAllowanceMs":arm["phaseLimits"]["phaseAllowanceMs"],
            "internalTimerExcludesInterpreterStartup":True,"rootUTCAnchorsBeforeArmAfterTerminalRequired":True,
            "enclosedChildAddedAgain":False,"noAutomaticNextPhase":True,"noRetry":True,
            "allCapAndPriorAccountingStillRequiresRootConsumption":True,"wholeSignClaim":False,"GoalComplete":False}
        save_new(owned/"terminal.json",summary,external[phase_dir+"/terminal.json"])
        return 0 if status.startswith("CHILD_EXIT0") else 2
    except BaseException as error:
        if tree is not None:
            try:
                historical_total = max(historical_total,tree.counts()[0])
                console_pids = sorted(tree.console_pids)
                tree.kill();exit_code = tree.wait(5);tree.wait_empty(5)
            except BaseException:
                pass
            finally:
                tree.close()
        for capture in captures:
            try:
                capture.finish()
            except BaseException:
                pass
        if owned is not None:
            try:
                save_new(owned/"terminal.json",{"schema":"RH_WEIL_GLOBAL_OBSERVER_TERMINAL_V1",
                    "status":"GLOBAL_OBSERVER_TECHNICAL_STOP_NO_RETRY","phase":args.phase,
                    "observerPID":os.getpid(),"exitCode":exit_code,"endedUTC":utc(),
                    "childPID":child_pid,"historicalJobProcessCount":historical_total,
                    "lastClassifiedJobMembers":last_members,"exactSystemConsoleMetadataPIDs":console_pids,
                    "unexpectedDescendants":descendants,
                    "rootMustMultiplyFullObservedPhaseMsByMultiplicity":max(1,historical_total) if descendants else 1,
                    "reason":type(error).__name__+":"+str(error)[:512],"childStarted":child_started is not None,
                    "internalElapsedCeilingMs":math.ceil((time.monotonic()-STARTED)*1000),
                    "captures":[c.summary(ROOT) for c in captures if c.destination.exists()],
                    "wholeSignClaim":False,"GoalComplete":False,"noRetry":True,
                    "rootFullTimeByteAndOmittedCaptureAuditRequired":True})
            except BaseException:
                pass
        sys.stderr.write("C069_OBSERVER_ARM_OR_PHASE_REFUSED\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

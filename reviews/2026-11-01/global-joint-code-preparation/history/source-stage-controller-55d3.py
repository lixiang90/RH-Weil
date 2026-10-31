"""Prospective C069 source producer/checker controller; NOT RUN ADMISSION.

Future CLI: produce|verify --root-freeze-file PROJECT_RELATIVE_JSON.
Only an authenticated future root gate plus actual C069 contract may create
the fixed once-only namespace. No producer/verifier import occurs before that
gate and all remaining code/review/source/math/resource pins have passed.
The scientific kernel runs inside this process; its lifetime is NOT added to
the enclosing controller lifetime. External launch-to-terminal observation is
mandatory and remains the authoritative charge for interpreter/startup/kill.
"""
from __future__ import annotations
import time
PROCESS_STARTED = time.monotonic()
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import types


ROOT = Path(__file__).resolve().parents[3]
SELF = Path(__file__).resolve()
BASE = "reviews/2026-11-01/global-joint-code-preparation/"
OUTER_REL = "literature/local/2026-11-01-directional-remainder-whole/run-01"
OUTER = ROOT / OUTER_REL
SOURCE_REL = OUTER_REL + "/stage-01-source"
PACKET_REL = SOURCE_REL + "/joint-centers.jsonl"
TARGET = "RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1"
GOAL = 1793085111
SOURCE_MS, SOURCE_BYTES = 3600000, 48*(1 << 20)
AGG_MS, AGG_BYTES = 7200000, 64*(1 << 20)
TERMINAL_RESERVE = 262144
EMERGENCY_MAX = 131072
PARAMETERS = {
    "N":448, "degree":2046, "coefficientBits":8192, "contractionBits":1024,
    "rawBits":256, "nativeArithmeticPower":-230, "packetRows":401856,
    "packetOrder":["CX", "FX", "FY", "XY", "YY"], "oneAttempt":True,
    "sourceCapMs":SOURCE_MS, "sourceCapBytes":SOURCE_BYTES,
    "aggregateCapMs":AGG_MS, "aggregateCapBytes":AGG_BYTES,
    "terminalReserveBytes":TERMINAL_RESERVE, "externalTerminalReserveMs":20000,
    "packetCopyAllowed":False, "YArrayOutputAllowed":False,
}
DATA_PINS = {
    "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/source-matrices.json":
        "a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
    "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/moments.json":
        "2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9",
    "literature/local/2026-10-31-retained-tail-source/run-01/h-columns.jsonl":
        "37f2c0410beb1b1c43b9f8d2df24d72fce3170b5f359d089c198742f1eee4e74",
    "literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl":
        "d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080",
}
MATH_PINS = {
    "reviews/2026-11-01/directional-remainder-admission/selected-global-preparation.json":
        "c3bda91eeee0c83993e2d2b5d6efeb2a959eb1a3817d34d77c3764b611f54984",
    "reviews/2026-11-01/directional-remainder-admission/full-k-column-supplier.md":
        "5bfd27fc7bed256367b8ed83a2be4eb972791718ec1fc844dde7ebb250cfa96a",
    "reviews/2026-11-01/directional-remainder-admission/whole-directional-consumer.md":
        "051797ca8a1db1f1e041de31b79e5ae18ab2096df9ba3f482d1c1b004c1e6555",
    "goals/GOAL.20261027.md":
        "b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de",
    "goals/review-cadence.json":
        "c57d42559b05b25c37fca829c7c4cd60c050dfff21be46f2909e79d5c582b8d4",
    "literature/manifest.json":
        "3223cffd0205b9a1f8660445ac33d0f3cec13b3bd1fa5e7799ed8abfb2746d42",
}


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def utc():
    return datetime.now(timezone.utc).isoformat()


def packed(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
                       separators=(",", ":"))+"\n").encode("ascii")


def unique(items):
    result = {}
    for key, value in items:
        need(key not in result, "DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique,
                      parse_constant=lambda _: need(False, "NONFINITE_JSON"))


def unsigned(value, name, maximum=None):
    need(type(value) is int and value >= 0, name+"_UNSIGNED_INTEGER")
    need(maximum is None or value <= maximum, name+"_UPPER_BOUND")
    return value


def relative_file(root, relative):
    need(type(relative) is str and relative and "\\" not in relative
         and not relative.startswith("/") and ":" not in relative,
         "CANONICAL_RELATIVE_PATH")
    parts = relative.split("/")
    need(all(p not in ("", ".", "..") for p in parts), "RELATIVE_PATH_PARTS")
    candidate = root.joinpath(*parts).resolve()
    need(candidate.is_relative_to(root.resolve()), "PATH_ESCAPES_WORKSPACE")
    return candidate


def pin_shape(row):
    need(type(row) is dict and set(row) == {"path", "bytes", "sha256"}, "PIN_SHAPE")
    unsigned(row["bytes"], "PIN_BYTES")
    need(type(row["sha256"]) is str and re.fullmatch("[0-9a-f]{64}", row["sha256"]), "PIN_SHA")
    return row


def read_pin(root, row, *, limit=4*(1 << 20)):
    pin_shape(row)
    path = relative_file(root, row["path"])
    need(path.is_file() and path.stat().st_size == row["bytes"] <= limit, "PIN_SIZE:"+row["path"])
    raw = path.read_bytes()
    need(len(raw) == row["bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"],
         "PIN_HASH:"+row["path"])
    return raw


def hash_pin(root, row, poll):
    pin_shape(row)
    path = relative_file(root, row["path"])
    need(path.is_file() and path.stat().st_size == row["bytes"], "SOURCE_PIN_SIZE")
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
            size += len(chunk)
            poll()
    need(size == row["bytes"] and digest.hexdigest() == row["sha256"], "SOURCE_PIN_HASH")


def atomic_new(path, raw):
    """Fresh immutable record only; no overwrite/reset is possible."""
    with path.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())


def check_header(freeze, gate, phase):
    need(freeze["schema"] == "RH_WEIL_GLOBAL_SOURCE_PHASE_FREEZE_V1"
         and freeze["authorization"] == "ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION",
         "FUTURE_FREEZE_REQUIRED")
    need(gate["schema"] == "RH_WEIL_GLOBAL_SOURCE_PHASE_ROOT_GATE_V1"
         and gate["status"] == "ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION_APPROVED",
         "FUTURE_ROOT_GATE_REQUIRED")
    need(phase in ("produce", "verify") and freeze["phase"] == gate["phase"] == phase,
         "PHASE_MATCH")
    for obj in (freeze, gate):
        need(obj["runtimeGoalCreatedAt"] == GOAL and type(obj["runtimeGoalCreatedAt"]) is int
             and obj["contractId"] == "C069" and obj["targetId"] == TARGET
             and obj["outerRelativePath"] == OUTER_REL
             and packed(obj["parameters"]) == packed(PARAMETERS),
             "TARGET_GOAL_PARAMETERS")
    identity = freeze["freezeIdentity"]
    need(type(identity) is str and re.fullmatch("[A-Za-z0-9_-]{16,128}", identity)
         and gate["freezeIdentity"] == identity, "FREEZE_IDENTITY")
    for field in ("contractPin", "controllerPin", "producerPin", "verifierPin", "protocolPin",
                  "sourcePins", "mathPins", "reviewPins", "launchPin", "admissionPin",
                  "priorAccountingPin", "chargedMetadataPins", "externalOutputPaths",
                  "phaseLimits", "producerResultPin", "producerTerminalPin", "outerClaimPin"):
        need(freeze[field] == gate[field], "GATE_FREEZE_MATCH:"+field)


def phase_claim(root, freeze, phase, freeze_sha, gate_sha):
    """Minimal authorized claim; all following failures are this SAME attempt."""
    created = []
    outer = relative_file(root, OUTER_REL)
    if phase == "produce":
        outer.mkdir(parents=True, exist_ok=False)
        claim = {"schema":"RH_WEIL_GLOBAL_ONCE_OUTER_CLAIM_V1", "contractId":"C069",
                 "targetId":TARGET, "runtimeGoalCreatedAt":GOAL,
                 "rootAdmissionNonce":freeze["freezeIdentity"], "producerPID":os.getpid(),
                 "createdUTC":utc(), "noRetry":True}
        raw = packed(claim)
        atomic_new(outer/"run-lock.json", raw)
        created.append((OUTER_REL+"/run-lock.json", len(raw)))
    else:
        need(outer.is_dir(), "MISSING_PRODUCER_OUTER")
        raw = read_pin(root, freeze["outerClaimPin"])
        claim = decode(raw)
        need(freeze["outerClaimPin"]["path"] == OUTER_REL+"/run-lock.json"
             and claim["schema"] == "RH_WEIL_GLOBAL_ONCE_OUTER_CLAIM_V1"
             and claim["targetId"] == TARGET and claim["runtimeGoalCreatedAt"] == GOAL
             and claim["noRetry"] is True, "OUTER_OWNER_BINDING")
    stage = relative_file(root, SOURCE_REL)
    if phase == "produce":
        stage.mkdir(exist_ok=False)
    else:
        need(stage.is_dir(), "SOURCE_STAGE_MISSING")
    output = stage/phase
    output.mkdir(exist_ok=False)
    raw = packed({"schema":"RH_WEIL_SOURCE_ONCE_PHASE_CLAIM_V1", "phase":phase,
                  "pid":os.getpid(), "parentPID":os.getppid(), "createdUTC":utc(),
                  "freezeSHA256":freeze_sha, "rootGateSHA256":gate_sha,
                  "outerRelativePath":OUTER_REL, "targetId":TARGET, "noRetry":True})
    atomic_new(output/"claim.json", raw)
    created.append(((output/"claim.json").relative_to(root).as_posix(), len(raw)))
    return output, created


def fixed_inputs(rows, required):
    need(type(rows) is dict and set(rows) >= set(required), "MANDATORY_PIN_SET")
    for path, sha in required.items():
        pin_shape(rows[path])
        need(rows[path]["path"] == path and rows[path]["sha256"] == sha, "FROZEN_PIN:"+path)


def accounting(prior, phase, producer_terminal=None):
    need(prior["schema"] == "RH_WEIL_ROOT_OBSERVED_GLOBAL_ACCOUNTING_V1"
         and prior["status"] == "ROOT_VERIFIED_NO_RETRY_ACCOUNTING"
         and prior["targetId"] == TARGET and prior["runtimeGoalCreatedAt"] == GOAL
         and prior["outerRelativePath"] == OUTER_REL, "ROOT_PRIOR_ACCOUNTING")
    source_ms = unsigned(prior["sourceObservedUpperMs"], "PRIOR_SOURCE_MS", SOURCE_MS)
    all_ms = unsigned(prior["aggregateObservedUpperMs"], "PRIOR_AGGREGATE_MS", AGG_MS)
    source_bytes = unsigned(prior["sourceChargedUpperBytes"], "PRIOR_SOURCE_BYTES", SOURCE_BYTES)
    all_bytes = unsigned(prior["aggregateChargedUpperBytes"], "PRIOR_AGGREGATE_BYTES", AGG_BYTES)
    need(all_ms >= source_ms and all_bytes >= source_bytes, "NO_AGGREGATE_RESET")
    lifetimes = prior["phaseLifetimes"]
    need(type(lifetimes) is list, "PRIOR_PHASE_LIFETIMES")
    phases = [x["phase"] for x in lifetimes]
    need(len(set(phases)) == len(phases), "NO_DUPLICATE_PHASE_ACCOUNTING")
    source_sum = all_sum = 0
    for entry in lifetimes:
        ms = unsigned(entry["fullObservedUpperMs"], "PHASE_LIFETIME")
        need(ms > 0 and entry["enclosedKernelAddedAgain"] is False, "FULL_LIFETIME_NO_DOUBLECOUNT")
        all_sum += ms
        if entry["phase"].startswith("source-"):
            source_sum += ms
    need(source_ms >= source_sum and all_ms >= all_sum, "SUM_ALL_PROCESS_LIFETIMES")
    if phase == "produce":
        need(not lifetimes and source_ms == all_ms == 0
             and prior["outerPreviouslyCreated"] is False, "FIRST_NEW_RESPONSIBILITY_ONLY")
    else:
        need(phases == ["source-produce"] and lifetimes[0]["exitCode"] == 0
             and prior["outerPreviouslyCreated"] is True, "EXACT_ONE_SUCCESSFUL_PRODUCER")
        need(lifetimes[0]["terminalPin"] == prior["producerTerminalPin"]
             and producer_terminal is not None
             and source_ms >= producer_terminal["internalElapsedCeilingMs"], "NO_ZERO_TIME_RESET")
        need(source_bytes >= producer_terminal["sourceChargeUpperIncludingTerminalReserve"]
             and all_bytes >= producer_terminal["aggregateChargeUpperIncludingTerminalReserve"],
             "NO_BYTE_RESET")
    old = prior["chargedPathBindings"]
    need(type(old) is dict, "PRIOR_CHARGED_PATHS")
    for name, pin in old.items():
        pin_shape(pin)
        need(pin["path"] == name, "PRIOR_CHARGED_PIN_NAME")
    return source_ms, all_ms, source_bytes, all_bytes, old


class Budget:
    def __init__(self, root, phase, output, prior, limits, new_static_bytes, early_bytes,
                 external_paths):
        self.root, self.phase, self.output = root, phase, output
        self.prior_source_ms, self.prior_all_ms, self.prior_source_bytes, self.prior_all_bytes = prior[:4]
        self.generated = early_bytes
        self.new_static = new_static_bytes
        self.external = external_paths
        self.external_reserved = sum(x["maxBytes"] for x in external_paths)
        self.allowance = unsigned(limits["phaseAllowanceMs"], "PHASE_ALLOWANCE", AGG_MS)
        self.internal = unsigned(limits["internalScientificCutoffMs"], "INTERNAL_CUTOFF", AGG_MS)
        external_timeout = unsigned(limits["externalObserverChildTimeoutMs"], "EXTERNAL_TIMEOUT", AGG_MS)
        need(0 < self.internal <= external_timeout-10000
             and external_timeout+PARAMETERS["externalTerminalReserveMs"] <= self.allowance
             and self.allowance <= min(SOURCE_MS-self.prior_source_ms, AGG_MS-self.prior_all_ms),
             "ACTUAL_REMAINING_TIME_AND_TERMINAL_RESERVES")
        self.last_progress = self.last_scan = 0.0
        self.stage, self.detail = "authenticated-preflight", {}
        self.packet = None
        self.poll(force=True)

    def elapsed_ms(self):
        return math.ceil((time.monotonic()-PROCESS_STARTED)*1000)

    def charges(self):
        added = self.generated+self.new_static+self.external_reserved
        return self.prior_source_bytes+added, self.prior_all_bytes+added

    def poll(self, *, force=False):
        need(self.elapsed_ms() <= self.internal, "INTERNAL_SCIENTIFIC_DEADLINE")
        source, all_bytes = self.charges()
        need(source+TERMINAL_RESERVE <= SOURCE_BYTES
             and all_bytes+TERMINAL_RESERVE <= AGG_BYTES, "COMPLETE_OUTPUT_CAP_WITH_TERMINAL_RESERVE")
        now = time.monotonic()
        if force or now-self.last_scan >= 0.25:
            for row in self.external:
                path = relative_file(self.root, row["path"])
                if path.exists():
                    need(path.is_file() and path.stat().st_size <= row["maxBytes"], "EXTERNAL_OUTPUT_BOUND")
            actual_bytes = 0
            allowed = {OUTER_REL+"/run-lock.json", PACKET_REL, PACKET_REL+".part"}
            for phase in (("produce",) if self.phase == "produce" else ("produce", "verify")):
                allowed.update(SOURCE_REL+"/"+phase+"/"+name for name in
                               ("claim.json", "progress.json", "progress.json.tmp", "result.json", "terminal.json"))
            for path in relative_file(self.root, OUTER_REL).rglob("*"):
                if path.is_file():
                    need(path.resolve().is_relative_to(relative_file(self.root, OUTER_REL)), "OUTPUT_LINK_ESCAPE")
                    need(path.relative_to(self.root).as_posix() in allowed, "UNACCOUNTED_SOURCE_OUTPUT")
                    actual_bytes += path.stat().st_size
            need(actual_bytes <= source and actual_bytes <= all_bytes, "ACTUAL_OUTPUT_BYTES_NOT_COVERED")
            need(not (relative_file(self.root, PACKET_REL).exists()
                      and relative_file(self.root, PACKET_REL+".part").exists()), "PACKET_DUPLICATE_FORBIDDEN")
            self.last_scan = now
        if now-self.last_progress >= 5:
            # Record liveness/resource position even during a long coefficient
            # phase before the first packet row. The external handle observation
            # is still required; a heartbeat record alone is not a live handle.
            self.last_progress = now  # Set BEFORE write->charge->poll recursion.
            if self.packet is not None:
                self.packet.flush()
            self.write("progress.json", {"phase":self.phase, "pid":os.getpid(),
                "status":"RUNNING_ONE_SOURCE_PHASE", "stage":self.stage,
                "detail":self.detail, "elapsedMs":self.elapsed_ms(), "observedUTC":utc(),
                "sourceChargedBeforeRecord":source, "aggregateChargedBeforeRecord":all_bytes}, replace=True)

    def charge(self, size, *, emergency=False):
        unsigned(size, "WRITE_BYTES")
        if not emergency:
            self.poll()
            source, all_bytes = self.charges()
            need(source+size+TERMINAL_RESERVE <= SOURCE_BYTES
                 and all_bytes+size+TERMINAL_RESERVE <= AGG_BYTES, "OUTPUT_WRITE_CAP")
        self.generated += size  # Every rewrite/tmp is charged; deleting never refunds.

    def write(self, name, value, *, emergency=False, replace=False):
        need(re.fullmatch("[a-z0-9-]+\\.json", name), "RECORD_BASENAME")
        raw = packed(value)
        need(len(raw) <= (EMERGENCY_MAX if emergency else 65536), "BOUNDED_RECORD")
        self.charge(len(raw), emergency=emergency)
        path = self.output/name
        if replace:
            tmp = self.output/(name+".tmp")
            atomic_new(tmp, raw)
            os.replace(tmp, path)
        else:
            atomic_new(path, raw)

    def progress(self, stage=None, **detail):
        if stage is not None:
            self.stage = stage
        if detail:
            self.detail = detail
        self.poll()

    def terminal(self, status, *, result_pin=None, failure=None):
        source, all_bytes = self.charges()
        value = {"schema":"RH_WEIL_SOURCE_PHASE_TERMINAL_V1", "phase":self.phase,
                 "status":status, "pid":os.getpid(), "parentPID":os.getppid(),
                 "endedUTC":utc(), "internalElapsedCeilingMs":self.elapsed_ms(),
                 "sourceChargeUpperIncludingTerminalReserve":source+TERMINAL_RESERVE,
                 "aggregateChargeUpperIncludingTerminalReserve":all_bytes+TERMINAL_RESERVE,
                 "terminalReserveBytes":TERMINAL_RESERVE,
                 "externalFutureOutputMaxBytesAlreadyCharged":self.external_reserved,
                 "allWritesIncludingRewritesCharged":True, "resultPin":result_pin,
                 "failure":failure, "externalFullLifetimeObservationStillRequired":True,
                 "enclosedKernelAddedAgain":False, "noRetry":True, "wholeSignClaim":False}
        self.write("terminal.json", value, emergency=True)


def packet_keys():
    for label in PARAMETERS["packetOrder"]:
        for parity in (0, 1):
            for i in range(parity, 448, 2):
                for j in range(i if label in ("CX", "YY") else parity, 448, 2):
                    yield label, i, j


class Packet:
    def __init__(self, root, budget):
        self.path = relative_file(root, PACKET_REL+".part")
        self.final = relative_file(root, PACKET_REL)
        need(not self.final.exists(), "PACKET_ALREADY_FINAL")
        self.handle = self.path.open("xb")
        self.budget, self.digest = budget, hashlib.sha256()
        self.keys, self.rows, self.size = packet_keys(), 0, 0
        budget.packet = self

    def emit(self, row):
        need(type(row) is list and len(row) == 4 and type(row[1]) is int
             and type(row[2]) is int and tuple(row[:3]) == next(self.keys), "PACKET_ORDER")
        text = row[3]
        need(type(text) is str and len(text) <= 80
             and re.fullmatch("0|-[1-9][0-9]*|[1-9][0-9]*", text), "PACKET_CANONICAL_INTEGER")
        need(abs(int(text)).bit_length() <= 262, "PACKET_CENTER_WIDTH")
        raw = (json.dumps(row, separators=(",", ":"))+"\n").encode("ascii")
        need(len(raw) < 100, "PACKET_ROW_BYTES")
        self.budget.charge(len(raw))
        self.handle.write(raw)
        self.digest.update(raw)
        self.rows += 1
        self.size += len(raw)
        self.budget.stage = "producing-canonical-packet"
        self.budget.detail = {"rows":self.rows, "bytes":self.size, "block":row[0], "i":row[1]}

    def flush(self):
        if not self.handle.closed:
            self.handle.flush()

    def close(self):
        if not self.handle.closed:
            self.handle.flush()
            os.fsync(self.handle.fileno())
            self.handle.close()

    def finish(self):
        need(self.rows == 401856 and next(self.keys, None) is None, "PACKET_COMPLETE_ROWS")
        self.close()
        need(not self.final.exists(), "PACKET_FINAL_OVERWRITE")
        os.replace(self.path, self.final)  # Rename only; NEVER duplicate the packet.
        return {"relativePath":PACKET_REL, "sha256":self.digest.hexdigest(),
                "bytes":self.size, "rows":self.rows, "rawBits":256}


def code_module(raw, path, name):
    """Execute only authenticated NEW code bytes; no reread/import of old drivers."""
    module = types.ModuleType(name)
    module.__file__ = str(path)
    module.__package__ = None
    exec(compile(raw, str(path), "exec"), module.__dict__)
    return module


def width_diagnostic(error):
    """Bounded exact HEX when a kernel exposes an offending integer in frames."""
    if "WIDTH" not in str(error).upper() and "BIT" not in str(error).upper():
        return None
    frames, current = [], error.__traceback__
    while current is not None:
        frames.append(current.tb_frame)
        current = current.tb_next
    values = []
    for frame in reversed(frames[-8:]):
        for name in ("center", "value", "x", "a", "n", "d"):
            item = frame.f_locals.get(name)
            candidates = [item] if type(item) is int else list(item) if type(item) is tuple and len(item) == 2 else []
            for number in candidates:
                if type(number) is not int or abs(number).bit_length() <= 262:
                    continue
                bits = abs(number).bit_length()
                record = {"role":frame.f_code.co_name+":"+name, "actualBitLength":bits,
                          "arithmeticValueUsable":False}
                if bits <= 65536:
                    record.update(encoding="SIGNED_HEX_DIAGNOSTIC_ONLY",
                                  value=("-0x" if number < 0 else "0x")+format(abs(number), "x"))
                else:
                    record.update(encoding="OMITTED_ABOVE_DIAGNOSTIC_CAP", value=None)
                values.append(record)
                if len(values) == 4:
                    return {"values":values, "diagnosticLimitBits":65536,
                            "mathematicalSignConclusion":False}
    return {"values":values, "diagnosticLimitBits":65536,
            "mathematicalSignConclusion":False, "missingValueNotInvented":not values}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("produce", "verify"))
    parser.add_argument("--root-freeze-file", required=True)
    args = parser.parse_args(argv)
    output = budget = packet = None
    try:
        # A malformed/unmatched launch can be refused before a safe claim. Its
        # PRECREATED root admission token is still spent; external observer must
        # record that terminal failure and must not relabel it as a new attempt.
        freeze_path = relative_file(ROOT, args.root_freeze_file)
        need(freeze_path.is_file() and not freeze_path.is_relative_to(OUTER)
             and freeze_path.stat().st_size <= 262144, "ROOT_FREEZE_LOCATION_SIZE")
        freeze_raw = freeze_path.read_bytes()
        freeze = decode(freeze_raw)
        gate_raw = read_pin(ROOT, freeze["rootGatePin"])
        gate = decode(gate_raw)
        check_header(freeze, gate, args.phase)
        need(gate["freezeRelativePath"] == args.root_freeze_file, "GATE_FREEZE_PATH")
        contract = freeze["contractPin"]
        need(contract["path"].startswith("goals/contracts/C069-") and contract["path"].endswith(".md"),
             "ACTUAL_NEW_C069_CONTRACT")
        read_pin(ROOT, contract)
        output, early = phase_claim(ROOT, freeze, args.phase,
                                    hashlib.sha256(freeze_raw).hexdigest(),
                                    hashlib.sha256(gate_raw).hexdigest())
        # All failures after this exclusive claim are owned terminal failures.
        code_rows = (freeze["controllerPin"], freeze["producerPin"], freeze["verifierPin"])
        need([r["path"] for r in code_rows] ==
             [BASE+"source-stage-controller.py", BASE+"source-model.py", BASE+"verify-source-model.py"],
             "EXACT_NEW_EXECUTABLE_PATHS")
        code = [read_pin(ROOT, row) for row in code_rows]
        need(code[0] == SELF.read_bytes(), "EXACT_CONTROLLER_SELF")
        need(freeze["protocolPin"]["path"] == BASE+"runtime-protocol.md", "PROTOCOL_PATH")
        read_pin(ROOT, freeze["protocolPin"])
        fixed_inputs(freeze["mathPins"], MATH_PINS)
        need(set(freeze["sourcePins"]) == set(DATA_PINS), "EXACT_FOUR_SOURCES")
        fixed_inputs(freeze["sourcePins"], DATA_PINS)
        for row in freeze["mathPins"].values():
            read_pin(ROOT, row)
        reviews, owners, roles = freeze["reviewPins"], set(), set()
        need(type(reviews) is list and len(reviews) >= 2, "TWO_FINAL_CODE_REVIEWS")
        for review in reviews:
            need(review["role"] in ("math", "protocol") and type(review["owner"]) is str
                 and review["owner"], "REVIEW_ROLE_OWNER")
            need(review["approvedCodeSHA256"] == [row["sha256"] for row in code_rows]
                 and review["approvedProtocolSHA256"] == freeze["protocolPin"]["sha256"],
                 "EXACT_FINAL_CODE_PROTOCOL_REVIEW")
            raw = read_pin(ROOT, review["pin"])
            need(all(sha.encode("ascii") in raw for sha in review["approvedCodeSHA256"])
                 and review["approvedProtocolSHA256"].encode("ascii") in raw, "REVIEW_TEXT_VERSION_BINDING")
            owners.add(review["owner"])
            roles.add(review["role"])
        need(len(owners) >= 2 and roles == {"math", "protocol"}, "DISTINCT_MATH_PROTOCOL_REVIEWERS")
        launch = decode(read_pin(ROOT, freeze["launchPin"]))
        admission = decode(read_pin(ROOT, freeze["admissionPin"]))
        need(launch["schema"] == "RH_WEIL_SOURCE_EXTERNAL_OBSERVER_LAUNCH_V1"
             and launch["phase"] == args.phase and launch["observerPID"] == os.getppid()
             and type(launch["observerPID"]) is int and launch["observerPID"] > 0
             and launch["freezeIdentity"] == freeze["freezeIdentity"]
             and launch["phaseLimits"] == freeze["phaseLimits"]
             and launch["rootMustVerifyFullLifetimeAfterTerminal"] is True,
             "EXTERNAL_LAUNCH_OBSERVER_REQUIRED")
        observer_pin = launch["observerCodePin"]
        read_pin(ROOT, observer_pin)
        for review in reviews:
            need(review["approvedObserverSHA256"] == observer_pin["sha256"], "EXTERNAL_OBSERVER_REVIEW_VERSION")
            need(observer_pin["sha256"].encode("ascii") in read_pin(ROOT, review["pin"]),
                 "EXTERNAL_OBSERVER_REVIEW_TEXT_BINDING")
        need(admission["schema"] == "RH_WEIL_C069_IRREVOCABLE_PHASE_ADMISSION_V1"
             and admission["status"] == "ADMITTED_BEFORE_LAUNCH_NO_RETRY"
             and admission["targetId"] == TARGET and admission["contractId"] == "C069"
             and admission["runtimeGoalCreatedAt"] == GOAL and admission["phase"] == args.phase
             and admission["freezeIdentity"] == freeze["freezeIdentity"], "IRREVOCABLE_ROOT_ADMISSION")
        producer_result = producer_terminal = None
        if args.phase == "produce":
            need(freeze["producerResultPin"] is None and freeze["producerTerminalPin"] is None
                 and freeze["outerClaimPin"] is None, "NEW_PRODUCER_ONLY")
        else:
            need(freeze["producerResultPin"]["path"] == SOURCE_REL+"/produce/result.json"
                 and freeze["producerTerminalPin"]["path"] == SOURCE_REL+"/produce/terminal.json",
                 "EXACT_PRODUCER_RESULT_TERMINAL")
            producer_result = decode(read_pin(ROOT, freeze["producerResultPin"]))
            producer_terminal = decode(read_pin(ROOT, freeze["producerTerminalPin"]))
            need(producer_result["status"] == "MODEL_FIVE_BLOCKS_CENTER_CERTIFIED_PENDING_ROOT"
                 and producer_result["targetId"] == TARGET and producer_result["rows"] == 401856
                 and producer_result["inputPins"] == DATA_PINS
                 and producer_terminal["status"] == "SOURCE_PRODUCER_EMITTED_REQUIRES_INDEPENDENT_CHECK"
                 and producer_terminal["phase"] == "produce"
                 and producer_terminal["resultPin"] == freeze["producerResultPin"], "SUCCESSFUL_SAME_PRODUCER")
        prior_raw = read_pin(ROOT, freeze["priorAccountingPin"])
        prior_obj = decode(prior_raw)
        prior = accounting(prior_obj, args.phase, producer_terminal)
        if args.phase == "verify":
            need(prior_obj["producerTerminalPin"] == freeze["producerTerminalPin"], "ROOT_PRIOR_TERMINAL_MATCH")
            need(prior_obj["outerClaimPin"] == freeze["outerClaimPin"], "ROOT_PRIOR_OUTER_MATCH")
        for pin in prior[4].values():
            hash_pin(ROOT, pin, lambda: None)
        if args.phase == "verify":
            previous_outer_files = {p.relative_to(ROOT).as_posix() for p in OUTER.rglob("*") if p.is_file()}
            previous_outer_files -= {name for name, _ in early}
            need(previous_outer_files == {name for name in prior[4] if name.startswith(OUTER_REL+"/")},
                 "EXACT_PRIOR_OUTPUT_INVENTORY")
        metadata = freeze["chargedMetadataPins"]
        need(type(metadata) is dict, "CHARGED_METADATA_MAP")
        for name, pin in metadata.items():
            need(pin["path"] == name and not relative_file(ROOT, name).is_relative_to(OUTER),
                 "CHARGED_EXTERNAL_METADATA_PATH")
            read_pin(ROOT, pin)
        all_static = dict(metadata)
        for pin in (freeze["rootGatePin"], freeze["launchPin"], freeze["admissionPin"],
                    freeze["priorAccountingPin"], freeze["contractPin"]):
            all_static[pin["path"]] = pin
        all_static[args.root_freeze_file] = {"path":args.root_freeze_file, "bytes":len(freeze_raw),
                                           "sha256":hashlib.sha256(freeze_raw).hexdigest()}
        new_static = 0
        for name, pin in all_static.items():
            if name in prior[4]:
                need(pin == prior[4][name], "IMMUTABLE_PRIOR_CHARGED_METADATA")
            else:
                new_static += pin["bytes"]
        external = freeze["externalOutputPaths"]
        need(type(external) is list and len(external) >= 3, "STDOUT_STDERR_ROOT_RECEIPT_RESERVES")
        external_names = set()
        for row in external:
            need(type(row) is dict and set(row) == {"path", "maxBytes"}, "EXTERNAL_OUTPUT_SPEC")
            path = relative_file(ROOT, row["path"])
            need(not path.is_relative_to(OUTER) and row["path"] not in all_static
                 and row["path"] not in prior[4] and row["path"] not in external_names,
                 "FRESH_EXACT_EXTERNAL_OUTPUT_PATH")
            unsigned(row["maxBytes"], "EXTERNAL_OUTPUT_BYTES", TERMINAL_RESERVE)
            external_names.add(row["path"])
        need(sum(x["maxBytes"] for x in external) <= 2*TERMINAL_RESERVE, "EXTERNAL_RESERVE_TOTAL")
        budget = Budget(ROOT, args.phase, output, prior, freeze["phaseLimits"],
                        new_static, sum(size for _, size in early), external)
        for row in freeze["sourcePins"].values():
            hash_pin(ROOT, row, budget.poll)
        budget.progress("authenticated-all-pins", phase=args.phase)
        if args.phase == "produce":
            budget.progress("producing-exact-model-kernels")
            module = code_module(code[1], relative_file(ROOT, code_rows[1]["path"]), "c069_new_source_producer")
            need(module.INPUTS == DATA_PINS, "PRODUCER_SOURCE_SET")
            packet = Packet(ROOT, budget)
            attest = {"status":"ROOT_EXPLICIT_C069_SOURCE_EXECUTION_APPROVED",
                "runtimeGoalCreatedAt":GOAL, "targetId":TARGET, "contractId":"C069",
                "producerSHA256":code_rows[1]["sha256"],
                "controllerAuthenticatedGateAndFreeze":True, "exclusiveOnceOwnerCreated":True}
            result = module.produce(ROOT, packet.emit, budget.poll, attest)
            result["packet"] = packet.finish()
            need(result["status"] == "MODEL_FIVE_BLOCKS_CENTER_CERTIFIED_PENDING_ROOT"
                 and result["rows"] == 401856 and result["fullNativeArithmeticPower"] == -230,
                 "PRODUCER_RESULT_CONTRACT")
            result.update(controllerSHA256=code_rows[0]["sha256"], producerSHA256=code_rows[1]["sha256"],
                          freezeSHA256=hashlib.sha256(freeze_raw).hexdigest(), rootGateSHA256=freeze["rootGatePin"]["sha256"])
            terminal_status = "SOURCE_PRODUCER_EMITTED_REQUIRES_INDEPENDENT_CHECK"
        else:
            budget.progress("independent-full-endpoint-check")
            info = producer_result["packet"]
            need(info["relativePath"] == PACKET_REL and info["rows"] == 401856
                 and info["rawBits"] == 256, "SAME_CANONICAL_PACKET")
            packet_pin = {"path":PACKET_REL, "bytes":info["bytes"], "sha256":info["sha256"]}
            hash_pin(ROOT, packet_pin, budget.poll)
            module = code_module(code[2], relative_file(ROOT, code_rows[2]["path"]), "c069_new_independent_source_verifier")
            names = ("matrices", "moments", "h", "v")
            paths = dict(zip(names, (relative_file(ROOT, name) for name in DATA_PINS)))
            pins = dict(zip(names, DATA_PINS.values()))
            result = module.verify_packet(relative_file(ROOT, PACKET_REL), paths, pins,
                                          poll=budget.poll, progress=budget.progress)
            need(result["status"] == "FIVE_MODEL_BLOCKS_FINAL_CENTER_NATIVE_ARITHMETIC230_VERIFIED"
                 and result["packetSHA256"] == packet_pin["sha256"] and result["packetRows"] == 401856
                 and result["bothHermitianTrianglesCharged"] is True
                 and result["exactInfiniteCXOffdiagonalTailIncluded"] is True,
                 "INDEPENDENT_ENDPOINT230_RESULT")
            hash_pin(ROOT, packet_pin, budget.poll)  # Same shared immutable bytes, no copy.
            result.update(packetPin=packet_pin, producerResultPin=freeze["producerResultPin"],
                          controllerSHA256=code_rows[0]["sha256"], verifierSHA256=code_rows[2]["sha256"],
                          freezeSHA256=hashlib.sha256(freeze_raw).hexdigest(),
                          rootAcceptanceAndFiniteGateStillRequired=True)
            terminal_status = "SOURCE_INDEPENDENT_CHECK_EMITTED_REQUIRES_ROOT_ACCEPTANCE"
        budget.poll(force=True)
        budget.write("result.json", result)
        result_path = output/"result.json"
        pin = {"path":result_path.relative_to(ROOT).as_posix(), "bytes":result_path.stat().st_size,
               "sha256":hashlib.sha256(result_path.read_bytes()).hexdigest()}
        budget.terminal(terminal_status, result_pin=pin)
        return 0
    except BaseException as error:
        if packet is not None:
            packet.close()  # Preserve .part and all charged bytes; no cleanup/retry.
        failure = {"exception":type(error).__name__, "reason":str(error)[:512],
                   "integerDiagnostic":width_diagnostic(error), "noRetry":True,
                   "mathematicalSignConclusion":False, "newDataUsable":False}
        if budget is not None:
            try:
                budget.terminal("GLOBAL_TECHNICAL_STOP_NO_RETRY", failure=failure)
            except BaseException:
                pass  # Root external observer must record inability to save terminal.
        elif output is not None:
            try:
                atomic_new(output/"terminal.json", packed({"schema":"RH_WEIL_SOURCE_PHASE_TERMINAL_V1",
                    "phase":args.phase, "status":"ADMITTED_PREFLIGHT_TECHNICAL_STOP_NO_RETRY",
                    "pid":os.getpid(), "endedUTC":utc(), "failure":failure,
                    "internalElapsedCeilingMs":math.ceil((time.monotonic()-PROCESS_STARTED)*1000),
                    "rootFullTimeAndBytesAuditRequired":True}))
            except BaseException:
                pass
        # Root's precreated admission token remains spent even before a safeclaim.
        sys.stderr.write("C069_SOURCE_PHASE_TERMINAL_UNCONSUMABLE_NO_RETRY\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

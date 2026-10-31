"""Independent finite replay controller; CODE PREPARATION ONLY.

Generic metadata/pin/encoding helpers are copied AS TEXT from the finite
consumer. No consumer import, assembly, solve, matrix or width certificate is
used as independent sign evidence. After a distinct NEW authenticated C069
replay gate, hash-compile ONLY root's independent augmented kernel and original
input adapter, then read the original sources and ONE root-accepted packet.
No current numerical execution, C069 or private attempt is authorized.
"""
from __future__ import annotations
import time
PROCESS_STARTED = time.monotonic()
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[3]
SELF = Path(__file__).resolve()
OUTER = ROOT / "literature/local/2026-11-01-directional-remainder-whole/run-01"
OUT = OUTER / "stage-02-finite-checker"
PRODUCER_OUT = OUTER / "stage-02-finite"
TARGET = "RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1"
LIBRARIES = {
 "reviews/2026-11-01/global-joint-code-preparation/verify-finite-augmented.py":
  {"bytes":8210,"sha256":"3ef31ca2255ed7a0aa4bc17cac979d49f93c95e43fb3ca18c8a67bd95f0ba6f9"},
 "reviews/2026-11-01/global-joint-code-preparation/finite-independent-inputs.py":
  {"bytes":8400,"sha256":"05bb27e4fb457aa29d7cae57115260dc4ca716d4899f1019feea274876cf5a97"}
}
OLD = "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/"
ORIGINAL_INPUT_PINS = {
 OLD+"source-matrices.json":"a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
 OLD+"tail-columns.json":"d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
 "literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl":
 "d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080"
}
MATH_SOURCE_PINS = dict(ORIGINAL_INPUT_PINS)
MATH_SOURCE_PINS.update({
 "reviews/2026-11-01/directional-remainder-admission/selected-global-preparation.json":
 "c3bda91eeee0c83993e2d2b5d6efeb2a959eb1a3817d34d77c3764b611f54984",
 "reviews/2026-11-01/directional-remainder-admission/whole-directional-consumer.md":
 "051797ca8a1db1f1e041de31b79e5ae18ab2096df9ba3f482d1c1b004c1e6555",
 "reviews/2026-11-01/retained-tail-whole-admission/old-fee-recovery-fresh.md":
 "a77888cd710f41a7abba87687e2724de009dbc6500bce5eddac16b3771895fc1",
 "reviews/2026-11-01/retained-tail-whole-prefix/prefix-math-admission.md":
 "ce8e3d793881c2849aeb19abcaaa16d3d72de5d0870f86097dd5446d63dee984",
 "goals/GOAL.20261027.md":
 "b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de",
 "goals/review-cadence.json":
 "c57d42559b05b25c37fca829c7c4cd60c050dfff21be46f2909e79d5c582b8d4",
 "literature/manifest.json":
 "3223cffd0205b9a1f8660445ac33d0f3cec13b3bd1fa5e7799ed8abfb2746d42"
})
POSITIVE = "WHOLE_POINT_POSITIVE_PENDING_INDEPENDENT_CHECKER_AND_ROOT"
REJECTED = "SUFFICIENT_WHOLE_FLOOR_REJECTED_PENDING_INDEPENDENT_CHECKER_AND_ROOT"
PARAMETERS = dict(N=448, sectorDimension=224, intervalBits=1024,
 activeDimensionPerParity=448, rawBits=256, normalIntegerBits=16384,
 integerStringLimit=20000, sectorOrder=["even","odd"],
 signMethod="INDEPENDENT_NEGATIVE_ACTIVE_AUGMENTATION",
 betaPower=-224,nuPower=-216,zetaPower=-216,alpha=None,
 YBottomCoefficient=0,packetRows=401856,oneAttempt=True,
 producerWidthPredicateRecomputed=False,consumerImported=False,
 inverseOrSolveOutputRead=False,packetCopyOutput=False,
 unresolvedPolicy="TERMINAL_NO_RETRY")


def need(ok, message):
    if not ok:
        raise ValueError(message)

def packed(obj):
    return (json.dumps(obj, ensure_ascii=True, sort_keys=True,
                       separators=(",", ":")) + "\n").encode("ascii")

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def unique(pairs):
    answer = {}
    for k, v in pairs:
        need(k not in answer, "DUPLICATE_JSON_KEY")
        answer[k] = v
    return answer

def decode(raw):
    return json.loads(raw, object_pairs_hook=unique,
        parse_constant=lambda _: need(False, "NONFINITE_JSON"))

def relative_path(name):
    p = (ROOT / name).resolve()
    need(p.is_relative_to(ROOT) and p.is_file(), "ROOT_INPUT_PATH")
    return p

def read_pin(pin):
    need(type(pin) is dict and set(pin) == {"path", "bytes", "sha256"}, "PIN_SCHEMA")
    need(type(pin["bytes"]) is int and 0 <= pin["bytes"] <= (2 << 20)
         and type(pin["sha256"]) is str and len(pin["sha256"]) == 64
         and all(c in "0123456789abcdef" for c in pin["sha256"]), "BOUNDED_METADATA_PIN")
    p = relative_path(pin["path"])
    need(p.stat().st_size == pin["bytes"], "METADATA_PIN_BYTES")
    raw = p.read_bytes()
    need(len(raw) == pin["bytes"] and digest(raw) == pin["sha256"], "METADATA_PIN_SHA")
    return p, raw


def opaque_pin(pin, poll=lambda: None):
    """Metadata/hash verification only, including the shared large packet."""
    need(type(pin) is dict and set(pin) == {"path", "bytes", "sha256"}, "OPAQUE_PIN_FIELDS")
    need(type(pin["bytes"]) is int and pin["bytes"] >= 0 and type(pin["sha256"]) is str
         and len(pin["sha256"]) == 64 and all(c in "0123456789abcdef" for c in pin["sha256"]),
         "OPAQUE_PIN_TYPES")
    path = relative_path(pin["path"])
    need(path.stat().st_size == pin["bytes"], "OPAQUE_PIN_SIZE")
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(1 << 20):
            poll()
            h.update(chunk)
    need(h.hexdigest() == pin["sha256"], "OPAQUE_PIN_HASH")
    return path


def bounded_ratio(pair):
    need(type(pair) is list and len(pair) == 2, "FINITE_WIDTH_RATIO")
    integers = []
    for s in pair:
        need(type(s) is str and len(s) <= 5000, "FINITE_WIDTH_RATIO_ENCODING")
        z = int(s)
        need(str(z) == s and abs(z).bit_length() <= 16384, "FINITE_WIDTH_RATIO_INTEGER")
        integers.append(z)
    need(integers[1] > 0, "FINITE_WIDTH_RATIO_DENOMINATOR")
    q = Fraction(*integers)
    need(0 <= q <= Fraction(1, 1 << 216), "PRODUCER_NATIVE216_NOT_PAID")
    return q


def validate_producer(producer, code_pin, result_pin, closed_log_pin):
    need(producer["schema"] == "RH_WEIL_GLOBAL_FINITE_RESULT_V1"
         and producer["status"] in (POSITIVE, REJECTED), "TECHNICAL_PRODUCER_NOT_REPLAY_ELIGIBLE")
    for k, v in (("contractId", "C069"), ("targetId", TARGET), ("runtimeGoalCreatedAt", 1793085111)):
        need(producer[k] == v, "PRODUCER_SCOPE_" + k)
    need(producer["codeSHA256"] == code_pin["sha256"]
         and producer["sourceMathPins"] == MATH_SOURCE_PINS, "PRODUCER_ACTUAL_CODE_OR_PREMISES")
    need(producer["targetFeeMultiplicity"] == dict(beta=1, nu=1, zeta=1, alpha=0)
         and producer["sourceBetaPower"] == -224 and producer["coefficientNuPower"] == -216
         and producer["finiteZetaPower"] == -216, "PRODUCER_FIXED_FEES")
    for k, v in dict(N=448,sectorDimension=224,intervalBits=1024,activeDimensionPerParity=448,
                     YBottomCoefficient=0,alpha=None,packetRows=401856).items():
        need(producer["parameters"][k] == v, "PRODUCER_PARAMETERS_" + k)
    need(producer["GoalComplete"] is False and producer["wholePositiveClaim"] is False
         and producer["negativeActualLretClaim"] is False and producer["negativeActualQClaim"] is False,
         "PRODUCER_SCOPE_UPGRADE")
    pl = producer["pivotLog"]
    expected_path = (PRODUCER_OUT / "pivots.jsonl").relative_to(ROOT).as_posix()
    need(result_pin["path"] == (PRODUCER_OUT/"result.json").relative_to(ROOT).as_posix()
         and closed_log_pin["path"] == expected_path and pl["path"] == "pivots.jsonl"
         and pl["closed"] is True and pl["bytes"] == closed_log_pin["bytes"]
         and pl["sha256"] == closed_log_pin["sha256"], "PRODUCER_CLOSED_LOG_BINDING")
    need(type(pl["rows"]) is int and 0 < pl["rows"] <= 1344, "PRODUCER_PIVOT_COUNT")
    sectors = producer["sectors"]
    need(type(sectors) is list and 0 < len(sectors) <= 2, "PRODUCER_SECTORS")
    for i, row in enumerate(sectors):
        need(row["sector"] == ("even", "odd")[i]
             and row["status"] == "TARGET_ASSEMBLED_WITH_FINITE_ERROR_CERTIFIED"
             and row["activePositivePivots"] == 448
             and row["targetContainsZetaExactlyOnce"] is True, "PRODUCER_FINITE_WIDTH_SCOPE")
        bounded_ratio(row["nativeArithmeticErrorBound"])
    if producer["status"] == POSITIVE:
        need(len(sectors) == 2 and all(r["wholeStatus"] == "ALL_POSITIVE" for r in sectors),
             "PRODUCER_BOTH_FULL_SECTORS")
    else:
        need(sectors[-1]["wholeStatus"] == "STRICT_NEGATIVE_PIVOT"
             and all(r["wholeStatus"] == "ALL_POSITIVE" for r in sectors[:-1]),
             "PRODUCER_STRICT_TARGET_REJECTION")


def validate_inventory(rows, kind):
    need(type(rows) is list and 0 < len(rows) <= 256, "PRIOR_INVENTORY_" + kind)
    paths, total = {}, 0
    for pin in rows:
        need(type(pin) is dict and type(pin.get("bytes")) is int and pin["bytes"]>=0,
             "PRIOR_INVENTORY_BYTES")
        total += pin["bytes"]
        need(total <= (50331648 if kind=="source" else 16777216), "PRIOR_INVENTORY_CAP")
        p = opaque_pin(pin)
        need(p not in paths, "DUPLICATE_PRIOR_INVENTORY_PATH")
        paths[p] = pin
    return paths, total


def claim_attempt(path):
    """Bounded minimal authority, then exclusive ownership BEFORE full preflight.

    A root external attempt is already immutable before this child is launched.
    Its pin does not contain a freeze hash, avoiding a self-referential pin cycle.
    Every failure after ownership is a consumed once-attempt, not a free retry.
    """
    need(path.is_file() and path.stat().st_size <= (2<<20), "BOUNDED_REPLAY_FREEZE")
    raw=path.read_bytes();freeze=decode(raw)
    need(freeze["schema"]=="RH_WEIL_GLOBAL_FINITE_REPLAY_FREEZE_V1"
         and freeze["authorization"]=="ROOT_EXPLICIT_C069_GLOBAL_FINITE_REPLAY"
         and freeze["numericalExecutionAuthorized"] is True,"MINIMAL_NEW_ROOT_AUTHORIZATION")
    for k,v in (("runtimeGoalCreatedAt",1793085111),("contractId","C069"),
                ("targetId",TARGET),("currentStage","stage-02-finite-checker")):
        need(freeze[k]==v,"MINIMAL_REPLAY_SCOPE_"+k)
    cp,code=read_pin(freeze["codePin"])
    need(cp==SELF and digest(code)==freeze["selfSHA256"],"MINIMAL_REPLAY_SELF")
    contractpath,contractraw=read_pin(freeze["contractPin"])
    need(contractpath==ROOT/"goals/contracts/C069-global-exact-directional-whole.md"
         and b"C069" in contractraw,"MINIMAL_ACTUAL_NEW_CONTRACT")
    gp,gr=read_pin(freeze["rootGatePin"]);gate=decode(gr)
    need(gate["schema"]=="RH_WEIL_GLOBAL_FINITE_REPLAY_ROOT_GATE_V1"
         and gate["authorization"]=="ROOT_EXPLICIT_C069_GLOBAL_FINITE_REPLAY"
         and gate["numericalExecutionAuthorized"] is True,"MINIMAL_ROOT_GATE")
    for k in ("runtimeGoalCreatedAt","contractId","targetId","currentStage","codePin","selfSHA256",
              "externalAttemptPin","launchNonce","preflightConsumesThisAttempt","contractPin",
              "wholeRunLockPin","rootAdmissionNonce"):
        need(gate[k]==freeze[k],"MINIMAL_GATE_MISMATCH_"+k)
    need(freeze["preflightConsumesThisAttempt"] is True
         and type(freeze["launchNonce"]) is str and 0<len(freeze["launchNonce"])<=128,
         "EXPLICIT_CONSUMED_PREFLIGHT_NONCE")
    ap,ar=read_pin(freeze["externalAttemptPin"]);attempt=decode(ar)
    need(attempt["schema"]=="RH_WEIL_GLOBAL_FINITE_REPLAY_ROOT_ATTEMPT_V1"
         and attempt["status"]=="ROOT_CLAIMED_ONE_FINITE_REPLAY","ACTUAL_ROOT_ONCE_CLAIM")
    for k in ("runtimeGoalCreatedAt","contractId","targetId","currentStage","codePin","launchNonce"):
        need(attempt[k]==freeze[k],"ROOT_ATTEMPT_SCOPE_"+k)
    need(freeze["budget"]["reservedCheckerOutputBytes"]>262144,"MINIMAL_TERMINAL_RESERVE")
    need(OUTER.is_dir() and not OUT.exists(),"REPLAY_STAGE_ALREADY_CLAIMED")
    OUT.mkdir(exist_ok=False)
    claim=dict(schema="RH_WEIL_GLOBAL_FINITE_REPLAY_ATTEMPT_V1",phase="CLAIMED_BEFORE_FULL_PREFLIGHT",
        terminal=False,pid=os.getpid(),freezeSHA256=digest(raw),rootGatePin=freeze["rootGatePin"],
        externalAttemptPin=freeze["externalAttemptPin"],launchNonce=freeze["launchNonce"],
        targetId=TARGET,contractId="C069",runtimeGoalCreatedAt=1793085111)
    claimraw=packed(claim);need(len(claimraw)<16384,"BOUNDED_ONCE_CLAIM")
    with (OUT/"attempt.json").open("xb") as f:
        f.write(claimraw);f.flush();os.fsync(f.fileno())
    return claim,claimraw


def validate_freeze(path,claim,claimraw):
    """No source math/array parsing until this NEW semantic gate is closed."""
    need(path.is_file() and path.stat().st_size <= (2 << 20), "BOUNDED_REPLAY_FREEZE")
    frozen_raw = path.read_bytes()
    need(digest(frozen_raw)==claim["freezeSHA256"]
         and (OUT/"attempt.json").read_bytes()==claimraw,"CLAIM_OR_FREEZE_CHANGED")
    freeze = decode(frozen_raw)
    need(freeze["schema"] == "RH_WEIL_GLOBAL_FINITE_REPLAY_FREEZE_V1"
         and freeze["authorization"] == "ROOT_EXPLICIT_C069_GLOBAL_FINITE_REPLAY"
         and freeze["numericalExecutionAuthorized"] is True, "NEW_REPLAY_AUTHORIZATION_REQUIRED")
    for k, v in (("runtimeGoalCreatedAt",1793085111),("contractId","C069"),
                 ("targetId",TARGET),("currentStage","stage-02-finite-checker")):
        need(freeze[k] == v, "REPLAY_SCOPE_" + k)
    need(freeze["parameters"] == PARAMETERS and freeze["mathSourcePins"] == MATH_SOURCE_PINS,
         "REPLAY_FIXED_PARAMETERS_AND_MATH")
    codepath, code = read_pin(freeze["codePin"])
    need(codepath == SELF and digest(code) == freeze["selfSHA256"], "REPLAY_FINAL_SELF")
    cp, cr = read_pin(freeze["contractPin"])
    need(cp == ROOT/"goals/contracts/C069-global-exact-directional-whole.md"
         and b"C069" in cr, "ACTUAL_NEW_C069_CONTRACT")
    protocolpath, _ = read_pin(freeze["protocolPin"])
    gatepath, gate_raw = read_pin(freeze["rootGatePin"])
    gate = decode(gate_raw)
    need(gate["schema"] == "RH_WEIL_GLOBAL_FINITE_REPLAY_ROOT_GATE_V1"
         and gate["authorization"] == "ROOT_EXPLICIT_C069_GLOBAL_FINITE_REPLAY"
         and gate["numericalExecutionAuthorized"] is True, "DISTINCT_REPLAY_ROOT_GATE")
    semantics = ("runtimeGoalCreatedAt","contractId","targetId","currentStage","parameters",
                 "mathSourcePins","codePin","selfSHA256","contractPin","protocolPin","libraryPins",
                 "producerCodePin","producerResultPin","producerClosedLogPin","rootPriorAccountingPin",
                 "sourceRootAcceptancePin","sharedpacketPin","reviewPins","reviewOwners","reviewKinds","budget",
                 "chargedMetadataPins","externalRuntimePaths","externalAttemptPin","launchNonce",
                 "preflightConsumesThisAttempt","wholeRunLockPin","rootAdmissionNonce")
    need(all(gate[k] == freeze[k] for k in semantics), "REPLAY_ROOT_GATE_SEMANTIC_MISMATCH")
    need(gate["sameRuntimeGoalLiveAndActiveChecked"] is True
         and gate["producerTerminalAndNoLiveProcessChecked"] is True
         and gate["sameResponsibilityNoReset"] is True
         and gate["finalMathematicalAndProtocolReviewsRootConsumed"] is True,
         "REPLAY_ROOT_LIVE_AND_ONCE_PREMISES")
    expected = {"augmentation": next(k for k in LIBRARIES if k.endswith("verify-finite-augmented.py")),
                "inputs": next(k for k in LIBRARIES if k.endswith("finite-independent-inputs.py"))}
    need(set(freeze["libraryPins"]) == set(expected), "REPLAY_LIBRARY_SET")
    library_raw = {}
    for role, filename in expected.items():
        pin = freeze["libraryPins"][role]
        need(pin == dict(path=filename, **LIBRARIES[filename]), "EXACT_INDEPENDENT_LIBRARY_VERSION")
        p, raw = read_pin(pin)
        need(p != SELF and "consumer" not in p.name, "NO_CONSUMER_LIBRARY_IMPORT")
        library_raw[role] = (p, raw)
    owners, reviews = freeze["reviewOwners"], freeze["reviewPins"]
    kinds=freeze["reviewKinds"]
    need(type(owners) is list and len(owners) == len(reviews) >= 2
         and all(type(s) is str and 0 < len(s) <= 256 for s in owners)
         and len(set(owners)) == len(owners), "DISTINCT_FINAL_REVIEW_OWNERS")
    need(type(kinds) is list and len(kinds)==len(reviews)
         and set(kinds)>={"math","protocol"},"FINAL_MATH_AND_PROTOCOL_REVIEWS")
    reviewpaths = set()
    for pin, owner in zip(reviews, owners):
        p, raw = read_pin(pin)
        need(owner.encode() in raw and freeze["selfSHA256"].encode() in raw
             and all(v["sha256"].encode() in raw for v in LIBRARIES.values()),
             "REVIEW_NOT_FINAL_WRAPPER_AND_BOTH_LIBRARIES")
        reviewpaths.add(p)
    need(len(reviewpaths) == len(reviews), "DISTINCT_FINAL_REVIEW_PATHS")
    _, producer_code = read_pin(freeze["producerCodePin"])
    need(digest(producer_code) == freeze["producerCodePin"]["sha256"], "PRODUCER_CODE_PIN")
    producerpath, producer_raw = read_pin(freeze["producerResultPin"])
    producer = decode(producer_raw)
    logpath = opaque_pin(freeze["producerClosedLogPin"])
    validate_producer(producer, freeze["producerCodePin"], freeze["producerResultPin"], freeze["producerClosedLogPin"])
    logrows=0
    with logpath.open("rb") as stream:
        while line:=stream.readline(4096):
            need(len(line)<4096 and line.endswith(b"\n"),"PRODUCER_LOG_BOUNDED_LINES")
            logrows+=1;need(logrows<=1344,"PRODUCER_LOG_ROW_CAP")
    need(logrows==producer["pivotLog"]["rows"],"ACTUAL_CLOSED_PRODUCER_LOG_ROWS")
    priorpath, prior_raw = read_pin(freeze["rootPriorAccountingPin"])
    prior = decode(prior_raw)
    need(prior["schema"] == "RH_WEIL_GLOBAL_FINITE_PRIOR_ROOT_OBSERVATION_V1"
         and prior["status"] == "PRODUCER_TERMINAL_COSTS_AND_LOG_ROOT_VERIFIED",
         "ACTUAL_PRIOR_ROOT_OBSERVATION_REQUIRED")
    for k, v in (("runtimeGoalCreatedAt",1793085111),("contractId","C069"),("targetId",TARGET)):
        need(prior[k] == v, "PRIOR_ROOT_SCOPE_" + k)
    need(prior["producerResultPin"] == freeze["producerResultPin"]
         and prior["producerClosedLogPin"] == freeze["producerClosedLogPin"]
         and prior["sourceRootAcceptancePin"] == freeze["sourceRootAcceptancePin"]
         and prior["producerProcessObservedTerminal"] is True
         and prior["producerObservedExitCode"] == 0
         and prior["sourceProcessObservedTerminal"] is True
         and prior["noLiveSourceOrProducerProcess"] is True
         and prior["producerNative216PredicateRootConsumed"] is True
         and prior["closedProducerLogRootConsumed"] is True
         and prior["allScientificLifetimesSummedWithoutOverlapDiscount"] is True
         and prior["allNumericalCopiesMetadataTmpFailuresAccounted"] is True,
         "PRIOR_ROOT_ACTUAL_EXECUTION_OR_WIDTH_UNCLOSED")
    lockpath,lockraw=read_pin(freeze["wholeRunLockPin"])
    lock=decode(lockraw)
    need(lockpath==(OUTER/"run-lock.json").resolve()
         and lock["schema"]=="RH_WEIL_GLOBAL_ONCE_OUTER_CLAIM_V1"
         and lock["runtimeGoalCreatedAt"]==1793085111 and lock["contractId"]=="C069"
         and lock["targetId"]==TARGET and lock["noRetry"] is True
         and lock["rootAdmissionNonce"]==freeze["rootAdmissionNonce"]
         and type(lock["producerPID"]) is int and lock["producerPID"]>0
         and type(lock["createdUTC"]) is str and 0<len(lock["createdUTC"])<=128
         and prior["wholeRunLockPin"]==freeze["wholeRunLockPin"],"ACTUAL_WHOLE_LOCK_SCOPE")
    source_paths, source_bytes = validate_inventory(prior["sourceOutputInventory"], "source")
    finite_paths, finite_bytes = validate_inventory(prior["finiteOutputInventory"], "finite")
    need(not set(source_paths)&set(finite_paths), "PRIOR_STAGE_INVENTORY_OVERLAP")
    baseline = dict(source_paths)
    baseline.update(finite_paths)
    need(producerpath in finite_paths and logpath in finite_paths, "PRODUCER_OUTPUTS_NOT_CHARGED")
    sp, sr = read_pin(freeze["sourceRootAcceptancePin"])
    accept = decode(sr)
    need(accept["schema"] == "RH_WEIL_GLOBAL_SOURCE_ROOT_ACCEPTANCE_V1"
         and accept["status"] == "ROOT_CONSUMED_FIVE_BLOCK_ENDPOINT230_CERTIFICATES"
         and accept["runtimeGoalCreatedAt"] == 1793085111 and accept["targetId"] == TARGET,
         "ROOT_ACCEPTED_SAME_SOURCE_REQUIRED")
    need(accept["fullNativeArithmeticPower"] == -230
         and accept["blocks"] == ["CX","FX","FY","XY","YY"]
         and accept["packetRows"] == 401856
         and accept["sharedpacketPin"] == freeze["sharedpacketPin"]
         and producer["sharedpacketPin"] == freeze["sharedpacketPin"]
         and accept["independentScientificVerificationPassed"] is True
         and accept["bothHermitianTrianglesCharged"] is True
         and accept["CXInfiniteOffdiagonalTailIncluded"] is True,
         "ACTUAL_ENDPOINT230_MODEL_SOURCE_NOT_HASH_ONLY")
    need(len(accept["sourceVerificationPins"]) >= 2, "SOURCE_SCIENTIFIC_RESULTS_REQUIRED")
    for pin in accept["sourceVerificationPins"]:
        read_pin(pin)
    packetpath = opaque_pin(freeze["sharedpacketPin"])
    need(packetpath.is_relative_to(OUTER/"stage-01-source")
         and packetpath in source_paths and freeze["sharedpacketPin"]["bytes"] <= 40185600,
         "ONE_CHARGED_SHARED_PACKET")
    budget = freeze["budget"]
    need(budget["aggregateCapSeconds"] == 7200 and budget["aggregateCapBytes"] == 67108864
         and budget["finiteCapSeconds"] == 3600 and budget["finiteCapBytes"] == 16777216,
         "FIXED_REPLAY_CAPS")
    for key in ("sourceConsumedUpperSeconds","finiteConsumedUpperSeconds","checkerDeadlineSeconds",
                "reservedTerminalSeconds"):
        need(type(budget[key]) in (int,float) and 0 <= budget[key] <= 7200, "REPLAY_TIME_"+key)
    for key in ("sourceConsumedOutputBytes","finiteConsumedOutputBytes","reservedCheckerOutputBytes"):
        need(type(budget[key]) is int and 0 <= budget[key] <= 67108864, "REPLAY_BYTES_"+key)
    for key in ("sourceConsumedUpperSeconds","finiteConsumedUpperSeconds",
                "sourceConsumedOutputBytes","finiteConsumedOutputBytes"):
        need(prior[key] == budget[key], "ACTUAL_PRIOR_COST_CHANGED_"+key)
    need(source_bytes <= budget["sourceConsumedOutputBytes"] <= 50331648
         and finite_bytes <= budget["finiteConsumedOutputBytes"] <= 16777216
         and budget["sourceConsumedUpperSeconds"] <= 3600, "ACTUAL_STAGE_COSTS")
    need(prior["nonRetainedMonotonicChargesRootVerified"] is True,"PRIOR_NONRETAINED_CHARGES_UNVERIFIED")
    for kind,retained,paid in (("source",source_bytes,budget["sourceConsumedOutputBytes"]),
                               ("finite",finite_bytes,budget["finiteConsumedOutputBytes"])):
        authorities=prior["nonRetainedChargeAuthorityPins"][kind]
        need(type(authorities) is list and (paid==retained or len(authorities)>0),
             "NONRETAINED_CHARGE_AUTHORITY_MISSING_"+kind)
        for pin in authorities:read_pin(pin)
    remaining_finite = 3600-budget["finiteConsumedUpperSeconds"]
    remaining_whole = 7200-budget["sourceConsumedUpperSeconds"]-budget["finiteConsumedUpperSeconds"]
    need(0 < budget["checkerDeadlineSeconds"] and budget["reservedTerminalSeconds"] > 0
         and budget["checkerDeadlineSeconds"]+budget["reservedTerminalSeconds"] <= min(remaining_finite,remaining_whole),
         "ACTUAL_REMAINING_TIME_NOT_NOMINAL")
    need(262144 < budget["reservedCheckerOutputBytes"]
         <= min(16777216-budget["finiteConsumedOutputBytes"],
                67108864-budget["sourceConsumedOutputBytes"]-budget["finiteConsumedOutputBytes"]),
         "ACTUAL_REMAINING_OUTPUT_NOT_NOMINAL")
    need(type(budget["externalRuntimeChargedUpperBytes"]) is int
         and 0<=budget["externalRuntimeChargedUpperBytes"]<budget["reservedCheckerOutputBytes"],
         "EXTERNAL_RUNTIME_MONOTONIC_RESERVE")
    need((OUTER/"run-lock.json").is_file() and OUT.is_dir()
         and {p.name for p in OUT.iterdir()}=={"attempt.json"}, "REPLAY_ONCE_OWNERSHIP")
    lock = (OUTER/"run-lock.json").resolve()
    need(lock in baseline and baseline[lock]==freeze["wholeRunLockPin"],
         "ORIGINAL_WHOLE_LOCK_NOT_CHARGED")
    attemptpath,_=read_pin(freeze["externalAttemptPin"])
    meta = {path.resolve(),gatepath,priorpath,sp,protocolpath,cp,attemptpath}
    for pin in freeze["chargedMetadataPins"]:
        q, _ = read_pin(pin)
        meta.add(q)
    meta -= set(baseline)
    mutable = set()
    for name in freeze["externalRuntimePaths"]:
        need(type(name) is str, "EXTERNAL_RUNTIME_PATH")
        q = (ROOT/name).resolve()
        need(q.is_relative_to(ROOT) and not q.is_relative_to(OUT) and q not in baseline
             and q not in meta and q != packetpath and q != SELF,
             "EXTERNAL_RUNTIME_PATH_OVERLAP")
        mutable.add(q)
    need(len(mutable) == len(freeze["externalRuntimePaths"]), "DUPLICATE_EXTERNAL_RUNTIME_PATH")
    existing = {p.resolve() for p in OUTER.rglob("*") if p.is_file()}
    need(existing <= set(baseline)|meta|mutable|{(OUT/"attempt.json").resolve()},
         "UNACCOUNTED_EXISTING_WHOLE_OUTPUT")
    need(all(not p.is_relative_to(OUT) for p in baseline), "REPLAY_ATTEMPT_ALREADY_IN_BASELINE")
    bindings = dict(freezeSHA256=digest(frozen_raw),codeSHA256=freeze["selfSHA256"],
        libraryPins=freeze["libraryPins"],producerResultPin=freeze["producerResultPin"],
        producerClosedLogPin=freeze["producerClosedLogPin"],sourceRootAcceptancePin=freeze["sourceRootAcceptancePin"],
        rootPriorAccountingPin=freeze["rootPriorAccountingPin"],sharedpacketPin=freeze["sharedpacketPin"])
    return freeze,producer,packetpath,library_raw,baseline,meta,mutable,bindings


class Runtime:
    def __init__(self,freeze,baseline,meta,mutable,bindings):
        self.freeze=freeze
        self.budget=freeze["budget"]
        self.baseline=baseline
        self.meta=meta
        self.mutable=mutable
        self.bindings=bindings
        self.log=None
        self.context={}
        self.lastwrite=self.lastsize=0.0
        self.created=sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())

    def bytes(self):
        own=sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
        if self.log is not None and not self.log.closed:
            own+=max(0,self.log.tell()-Path(self.log.name).stat().st_size)
        external=sum(p.stat().st_size for p in self.meta if p.is_file())
        mutable=sum(p.stat().st_size for p in self.mutable if p.is_file())
        need(mutable<=self.budget["externalRuntimeChargedUpperBytes"],"EXTERNAL_RUNTIME_RESERVE_EXCEEDED")
        return external+self.budget["externalRuntimeChargedUpperBytes"]+max(self.created,own)

    def charge(self,size,emergency=False):
        need(type(size) is int and size>=0,"MONOTONIC_WRITE_SIZE")
        # A denied allocation performs no write. Once allocation is funded,
        # precharge BEFORE the write and retain it even on I/O failure.
        need(self.bytes()+size+(0 if emergency else 262144)<=self.budget["reservedCheckerOutputBytes"],
             "MONOTONIC_REPLAY_WRITE_CAP_STOP")
        self.created+=size

    def check(self):
        need(time.monotonic()-PROCESS_STARTED+1 <= self.budget["checkerDeadlineSeconds"],
             "REPLAY_PROCESS_DEADLINE_STOP")
        if time.monotonic()-self.lastsize>=0.5:
            now=self.bytes()
            need(now+262144<=self.budget["reservedCheckerOutputBytes"],"REPLAY_OUTPUT_RESERVE_STOP")
            need(self.budget["finiteConsumedOutputBytes"]+now+262144<=16777216,
                 "REPLAY_FINITE_STAGE_OUTPUT_STOP")
            need(self.budget["sourceConsumedOutputBytes"]+self.budget["finiteConsumedOutputBytes"]
                 +now+262144<=67108864,"REPLAY_AGGREGATE_OUTPUT_STOP")
            allowed=set(self.baseline)|self.meta|self.mutable
            need(all(p.resolve() in allowed or p.resolve().is_relative_to(OUT)
                     for p in OUTER.rglob("*") if p.is_file()),"UNACCOUNTED_CONCURRENT_WHOLE_OUTPUT")
            self.lastsize=time.monotonic()

    def atomic(self,name,obj,emergency=False):
        raw=packed(obj)
        need(len(raw)<131072,"BOUNDED_REPLAY_RECORD")
        if not emergency:
            self.check()
        self.charge(len(raw),emergency)
        with (OUT/(name+".tmp")).open("wb") as f:
            f.write(raw);f.flush();os.fsync(f.fileno())
        os.replace(OUT/(name+".tmp"),OUT/name)

    def poll(self,phase=None,**context):
        self.check()
        if phase is not None:self.context=dict(phase=phase,**context)
        if time.monotonic()-self.lastwrite>=3:
            if self.log is not None:self.log.flush()
            self.atomic("progress.json",dict(schema="RH_WEIL_GLOBAL_FINITE_REPLAY_PROGRESS_V1",
                status="RUNNING",terminal=False,bindings=self.bindings,context=self.context,
                monotonicOwnedBytesBeforeThisProgress=self.created,
                elapsedSecondsWithReserve=time.monotonic()-PROCESS_STARTED+1))
            self.lastwrite=time.monotonic()


def load_authenticated_library(path,raw,name):
    # Code bytes were authenticated against fixed independent library versions.
    # __name__ is deliberately not __main__; only future explicit calls read data.
    env={"__name__":name,"__file__":str(path),"__builtins__":__builtins__}
    exec(compile(raw,str(path),"exec"),env)
    return env


def compare_outcomes(producer_status,sectors):
    statuses=[r["status"] for r in sectors]
    positive=len(statuses)==2 and all(s=="EXACT_SELECTED_TARGET_POSITIVE" for s in statuses)
    negative=bool(statuses) and statuses[-1]=="SUFFICIENT_TARGET_REJECTED"
    if positive:
        return ("EXACT_TARGET_POSITIVE_INDEPENDENTLY_VERIFIED_PENDING_ROOT" if producer_status==POSITIVE
                else "PRODUCER_CHECKER_SIGN_DISAGREEMENT_UNRESOLVED")
    if negative:
        return ("EXACT_TARGET_REJECTED_INDEPENDENTLY_VERIFIED_PENDING_ROOT" if producer_status==REJECTED
                else "PRODUCER_CHECKER_SIGN_DISAGREEMENT_UNRESOLVED")
    return "INDEPENDENT_FINITE_REPLAY_UNRESOLVED"


def preserve_claim_failure(claim,error,phase):
    result=dict(schema="RH_WEIL_GLOBAL_FINITE_REPLAY_RESULT_V1",
        status=phase,terminal=True,claim=claim,errorType=type(error).__name__,
        error=str(error)[:2048],noRetry=True,mathematicalSignConclusion=False,GoalComplete=False,
        elapsedSecondsIncludingReserve=time.monotonic()-PROCESS_STARTED+1)
    raw=packed(result);need(len(raw)<131072,"BOUNDED_CLAIMED_FAILURE_TERMINAL")
    with (OUT/"result.json").open("xb") as f:
        f.write(raw);f.flush();os.fsync(f.fileno())
    print(packed(dict(status=result["status"],result=(OUT/"result.json").relative_to(ROOT).as_posix(),
                     resultSHA256=digest(raw))).decode(),end="")
    return 2


def execute(path):
    sys.set_int_max_str_digits(20000)
    claim,claimraw=claim_attempt(path)
    try:
        freeze,producer,packetpath,libraries,baseline,meta,mutable,bindings=validate_freeze(path,claim,claimraw)
    except Exception as error:
        # Minimal authorized ownership is already irrevocably consumed. The
        # external observer additionally charges this full failed child phase.
        return preserve_claim_failure(claim,error,"PREFLIGHT_TECHNICAL_STOP_AFTER_ONCE_CLAIM")
    rt=Runtime(freeze,baseline,meta,mutable,bindings)
    logpath=OUT/"signed-pivots.jsonl.part"
    try:
        rt.atomic("admission.json",dict(schema="RH_WEIL_GLOBAL_FINITE_REPLAY_ADMISSION_V1",pid=os.getpid(),
            bindings=bindings,targetId=TARGET,runtimeGoalCreatedAt=1793085111,parameters=PARAMETERS))
        log=logpath.open("xb");rt.log=log
    except Exception as error:
        return preserve_claim_failure(claim,error,"CONTROLLED_STARTUP_STOP_AFTER_ONCE_CLAIM")
    h=hashlib.sha256();count=logsize=0;sector_name=None

    def emit(pivot,expected,endpoints):
        nonlocal count,logsize
        rt.poll("independent-signed-LDL",sector=sector_name,pivot=pivot,expected=expected)
        need(all(type(v) is int and abs(v).bit_length()<=16384 for v in endpoints),"REPLAY_PIVOT_WIDTH")
        raw=packed(dict(sector=sector_name,pivot=pivot,expected=expected,
            endpoints=list(map(str,endpoints)),endpointBits=1024))
        need(len(raw)<12000,"REPLAY_BOUNDED_PIVOT_RECORD")
        rt.charge(len(raw))
        log.write(raw);h.update(raw);count+=1;logsize+=len(raw)

    result=None
    try:
        # Mathematical source inputs are hashed independently; not producer data.
        for filename,sha in MATH_SOURCE_PINS.items():
            p=relative_path(filename)
            opaque_pin(dict(path=filename,bytes=p.stat().st_size,sha256=sha),rt.poll)
        kernel=load_authenticated_library(*libraries["augmentation"],"independent_augmented_kernel")
        adapter=load_authenticated_library(*libraries["inputs"],"independent_original_inputs")
        need(adapter["PINS"]==ORIGINAL_INPUT_PINS and kernel["P"]==1024
             and kernel["WIDTH"]==16384,"AUTHENTICATED_LIBRARY_FIXED_PARAMETERS")
        rt.poll("independent-original-source-read")
        centers=adapter["load_old_centers"](ROOT,poll=rt.poll)
        rt.poll("independent-shared-packet-read-only")
        blocks=adapter["load_packet"](packetpath,dict(sha256=freeze["sharedpacketPin"]["sha256"],
                        bytes=freeze["sharedpacketPin"]["bytes"]),poll=rt.poll)
        sectors=[]
        for parity in (0,1):
            sector_name=("even","odd")[parity]
            rt.poll("independent-original-raw-sector-forms",sector=sector_name)
            d,g,dh,c0=adapter["sector_forms"](centers,parity,poll=rt.poll)
            rt.poll("independent-augmentation",sector=sector_name)
            answer=kernel["verify_sector"](d,g,dh,c0,blocks[parity],poll=rt.poll,emit=emit)
            answer["sector"]=sector_name;sectors.append(answer)
            if answer["status"]!="EXACT_SELECTED_TARGET_POSITIVE":break
        result=dict(schema="RH_WEIL_GLOBAL_FINITE_REPLAY_RESULT_V1",
            status=compare_outcomes(producer["status"],sectors),contractId="C069",targetId=TARGET,
            runtimeGoalCreatedAt=1793085111,bindings=bindings,parameters=PARAMETERS,sectors=sectors,
            producerStatus=producer["status"],producerNative216PredicateRecomputed=False,
            producerNative216RootConsumed=True,rootMustConsumeBothProducerWidthAndIndependentSign=True,
            independentSignAuthority="Original-input exact-target augmented inertia; no consumer solve/inverse/output matrices",
            actualNegativeLretClaim=False,actualNegativeQClaim=False,wholePositiveClaim=False,
            mathematicalSettlement="PENDING_ROOT_SAME_C069",GoalComplete=False)
    except Exception as error:
        result=dict(schema="RH_WEIL_GLOBAL_FINITE_REPLAY_RESULT_V1",status="INDEPENDENT_FINITE_REPLAY_TECHNICAL_STOP",
            targetId=TARGET,contractId="C069",bindings=bindings,errorType=type(error).__name__,
            error=str(error)[:2048],context=rt.context,mathematicalSignConclusion=False,
            noRetry=True,GoalComplete=False)
    finally:
        log.flush();os.fsync(log.fileno());log.close();rt.log=None
        os.replace(logpath,OUT/"signed-pivots.jsonl")
    result["pivotLog"]=dict(path="signed-pivots.jsonl",sha256=h.hexdigest(),rows=count,bytes=logsize,closed=True)
    result["elapsedSecondsIncludingReserve"]=time.monotonic()-PROCESS_STARTED+1
    result["newReplayOutputBytesBeforeResult"]=rt.bytes()
    result["monotonicOwnedBytesBeforeResult"]=rt.created
    result["externalRuntimeChargedUpperBytes"]=rt.budget["externalRuntimeChargedUpperBytes"]
    rt.atomic("result.json",result,emergency=True)
    need(rt.bytes()<=rt.budget["reservedCheckerOutputBytes"],"REPLAY_TERMINAL_OUTPUT_CAP_STOP")
    print(packed(dict(status=result["status"],result=(OUT/"result.json").relative_to(ROOT).as_posix(),
                     finalMonotonicChargedUpperBytes=rt.bytes(),
                     resultSHA256=digest((OUT/"result.json").read_bytes()))).decode(),end="")
    return 0 if result["status"].endswith("VERIFIED_PENDING_ROOT") else 2


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-freeze-file",type=Path,required=True)
    args=parser.parse_args()
    sys.set_int_max_str_digits(20000)
    return execute(args.root_freeze_file.resolve())


if __name__=="__main__":
    raise SystemExit(main())

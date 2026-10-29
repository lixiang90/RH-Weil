"""One fixed L=9/8 source-only experiment, never a full-Weil certificate.

`prepare` verifies the six frozen originals and produces isolated local copies.
Other stages require the freshly printed manifest and worker SHA256 pins.
Run with Python -I -S -B; no stage dispatches a subprocess or a core compiler.
The copied third-party programs and numeric packets remain in literature/local/.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import socket
import subprocess
import sys
import time
import traceback
import types
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction

REPO = Path(__file__).resolve().parents[1]
BASE = REPO / "literature/local/2026-10-29-weil-9-8"
ORIGINAL = BASE / "source/frozen-source/reproduction/source"
PILOT = BASE / "pilot"
SOURCE = PILOT / "source"
MANIFEST = PILOT / "source-manifest.json"
RUN = PILOT / "run-01"
CERT, RECEIPTS = RUN / "certificates", RUN / "receipts"
SCHEMA = "RH_WEIL_9_8_SOURCE_PILOT_V1"
STATUS = "SOURCE_ONLY_NOT_FULL_Q"
ORIGINAL_PINS = {
    "01-check.py": "4ed7661f1f869ed6d37d7bc52f1a0889a8d305a790663dc0ae43d76f2ea0e356",
    "02-produce.py": "0b338cf043e8bcf2c22e3f9cd26914d3b39a00b03f13070b0de02b7a9210556a",
    "07-check.py": "bee8f860c1919059e8888be3e8941bfd6dd592f467165d53ef8ec04fcd532635",
    "08-produce.py": "7b980b6dd8ff7a8dd0163cef970f3bf8ac9dff8bddb6b2762d56669e2723680d",
    "11-checker_quotient.py": "c951ce0d4075c3b93739901f6aa938421841ab183b816172b2685ffac5bbce8a",
    "12-raw_column_producer.py": "6342dca29469c61034aa39c5a648285691244ef6863a4fe9f2de3a0af07f516e",
}
MOMENT_PARAMETERS = {
    "L": "9/8", "beta": "7/2", "omega": 256, "shift": 256,
    "binetTerms": 256, "qMin": 0, "qMax": 1023,
    "producerBits": 6144, "checkerBits": 6400,
    "outputBits": 1152, "radiusBits": 1098,
}
MATRIX_PARAMETERS = {
    "N": 448, "L": "9/8", "beta": "7/2", "omega": 256, "qMax": 1023,
    "producerBits": 3072, "checkerBits": 3328, "centerBits": 2048,
    "outputBits": 256, "epsilonBits": 220, "sourceEntryPower": -2021,
    "kernelSourceBits": 204,
}
TAIL_PARAMETERS = {
    "LNumerator": 9, "LDenominator": 8, "omega": 256, "dimension": 448,
    "terms": 1024, "machinTerms": 160, "deltaPower": 49158,
    "workingBits": 2048, "outputBits": 640,
}
CONFIG = {"schema": SCHEMA, "halfWidth": "9/8", "moments": MOMENT_PARAMETERS,
          "matrices": MATRIX_PARAMETERS, "tails": TAIL_PARAMETERS,
          "primePowers": [2, 3, 4, 5, 7, 8, 9], "orderedPairs": 225,
          "fullWeilPositivity": "NOT_ESTABLISHED", "coreStageAdmitted": False}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode()


CONFIG_SHA = digest(canonical(CONFIG))


def sha(path):
    return digest(Path(path).read_bytes())


def now():
    return datetime.now(timezone.utc).isoformat()


def need(value, message):
    if not value:
        raise ValueError(message)


def same(a, b):
    return type(a) is type(b) and (a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
                                  if isinstance(a, dict) else
                                  len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
                                  if isinstance(a, list) else a == b)


def within(path, root):
    return path == root or root in path.parents


def regular(path, root):
    need(within(path.resolve(), root.resolve()), "PATH_OUTSIDE_FIXED_ROOT")
    for part in [path, *path.parents]:
        need(not part.is_symlink(), "SYMLINK_PATH")
        if part == root:
            break


def checked_ast(data, path):
    tree = ast.parse(data, filename=str(path))
    permitted = (ast.Import, ast.ImportFrom, ast.Assign, ast.AnnAssign,
                 ast.FunctionDef, ast.ClassDef, ast.Expr)
    need(all(isinstance(n, permitted) for n in tree.body), "UNREVIEWED_MODULE_TOP_LEVEL")
    for node in tree.body:
        if isinstance(node, ast.Expr):
            need(isinstance(node.value, ast.Constant) and isinstance(node.value.value, str),
                 "TOP_LEVEL_CALL")
    compile(tree, str(path), "exec", dont_inherit=True, optimize=0)


def patched(name, raw):
    """Every replacement has an explicit exact occurrence count and receipt."""
    text = raw.decode("utf-8")
    changes = []

    def replace(label, old, new, count=1):
        nonlocal text
        actual = text.count(old)
        need(actual == count, f"PATCH_COUNT:{name}:{label}:{actual}!={count}")
        text = text.replace(old, new)
        changes.append({"label": label, "occurrences": count,
                        "oldSHA256": digest(old.encode()), "newSHA256": digest(new.encode()),
                        "old": old, "new": new})

    # Remove all historical CLI/legacy packet reading. Only reviewed pure entries remain.
    marker = "\ndef main():" if name[:2] in ("01", "02", "07", "08") else '\nif __name__ == "__main__":'
    need(text.count(marker) == 1, "LEGACY_CLI_MARKER")
    discarded = text[text.index(marker):]
    text = text[:text.index(marker)].rstrip() + "\n"
    changes.append({"label": "remove-legacy-cli", "occurrences": 1,
                    "discardedSHA256": digest(discarded.encode()), "discardedBytes": len(discarded.encode())})
    if name[:2] in ("01", "02"):
        replace("window-metadata", '"L": "17/16"', '"L": "9/8"')
        replace("moment-precision", '"outputBits": 1024, "radiusBits": 970',
                '"outputBits": 1152, "radiusBits": 1098')
    if name.startswith("01"):
        replace("checker-output-conversion", "BITS - 1024", "BITS - 1152")
        replace("checker-output-bound", "896 << 1024", "896 << 1152", 3)
        replace("radius-label", "2^-970", "2^-1098")
        replace("out-of-range-control-lo", "1024 << 1024", "1024 << 1152")
        replace("out-of-range-control-hi", "1025 << 1024", "1025 << 1152")
    if name.startswith("02"):
        replace("producer-output-conversion", "m.bits-1024", "m.bits-1152")
        replace("producer-output-bound", "896 << 1024", "896 << 1152")
    if name.startswith("07"):
        replace("window-center", "L_CENTER = 17 << 2044", "L_CENTER = 18 << 2044")
        replace("window-metadata", '"L": "17/16"', '"L": "9/8"')
        replace("center-keys", '"+8", "-8"]', '"+8", "-8", "+9", "-9"]')
        replace("ordered-pair-convention", '"orderedPrimePairs": 169', '"orderedPrimePairs": 225')
        replace("full-prime-list", "(2, 3, 4, 5, 7, 8)", "(2, 3, 4, 5, 7, 8, 9)", 2)
        replace("support-upper", "17 * U // 8", "9 * U // 4")
        replace("mangoldt-proper-power", "mangoldt = logs[2] if n in (4, 8) else logs[n]",
                "mangoldt = logs[2] if n in (4, 8) else logs[3] if n == 9 else logs[n]")
        replace("next-integer-cutoff", 'bounds = {"0": (ZERO, rational(7, 2))}',
                'need(log_integer(10, log_two)[0] > 9 * U // 4, "all integers n>=10 excluded")\n    bounds = {"0": (ZERO, rational(7, 2))}')
        replace("center-shape", 'len(items) == 13, "all 13 prime centers required"',
                'len(items) == 15, "all 15 prime centers required"')
        replace("center-symmetry", "range(1, 13, 2)", "range(1, 15, 2)")
        replace("weight-total", "+ 12 < 10 * C", "+ 14 < 11 * C")
        replace("fixture-correct-width", "== 9 * C", "== 10 * C", 2)
        replace("fixture-omitted-width", "== 13 * C", "== 14 * C")
        replace("fixture-rejection-label", "rejects 13/8", "rejects 7/4")
        replace("fixture-correct-label", '"exactO00": "9/8"', '"exactO00": "5/4"')
        replace("fixture-wrong-label", '"wrongO00": "13/8"', '"wrongO00": "7/4"')
        replace("overlap-L", "scale(jump, 17, 16 * (2 * j + 1))", "scale(jump, 18, 16 * (2 * j + 1))")
        replace("census", '== 169', '== 225', 2)
        replace("census-shifts", '== 13', '== 15')
        replace("pole-L-square", "power17 *= 289", "power17 *= 324")
        replace("kernel-argument-square", "power544 *= 295936", "power544 *= 331776")
        replace("moment-midpoint-denominator", "exponent = max(4 * m, 1025)", "exponent = max(4 * m, 1153)")
        replace("moment-midpoint-shift", "exponent - 1025", "exponent - 1153")
        replace("raw-J0-L-square", "scale(values[j], 289, 256)", "scale(values[j], 81, 64)")
        replace("B-one-sided-trace-2L", "traces[j]), 17, 8 * (2 * j + 1))", "traces[j]), 18, 8 * (2 * j + 1))")
        replace("raw-metric-error", "17 * OUT", "18 * OUT", 2)
        replace("matrix-packet-schema", '"W199_FULL_SOURCE_MATRICES_V1"', '"RH_WEIL_9_8_SOURCE_MATRICES_V1"')
        replace("pair-mutation", '= 168', '= 224')
        # Dormant legacy moment helper is removed rather than retaining 1024-bit shortcuts.
        old = text[text.index("\ndef hash_string"):]
        text = text[:text.index("\ndef hash_string")].rstrip() + "\n"
        changes.append({"label": "remove-legacy-moment-file-helper", "discardedSHA256": digest(old.encode()), "discardedBytes": len(old.encode()), "occurrences": 1})
        start = text.index('ROOT = Path(')
        end = text.index('\nBITS =', start)
        text = text[:start] + text[end+1:]
        start = text.index('MOMENT = ROOT /')
        end = text.index('\n\n\ndef need', start)
        removed = text[start:end]
        text = text[:start] + text[end:]
        changes.append({"label": "remove-unused-legacy-locators", "discardedSHA256": digest(removed.encode()), "occurrences": 1})
    if name.startswith("08"):
        replace("window-center", "LN = 17 * (C >> 4)", "LN = 18 * (C >> 4)")
        replace("window-metadata", '"L":"17/16"', '"L":"9/8"')
        replace("ordered-pair-convention", '"orderedPrimePairs":169', '"orderedPrimePairs":225')
        replace("proper-power-log9", "logs[8] = scale(log2, 3)", "logs[8] = scale(log2, 3)\n    logs[9] = scale(logs[3], 2)\n    require(add(log2, logs[5])[0] > 9*S//4, \"all integers n>=10 excluded\")")
        replace("full-prime-list", "(2, 3, 4, 5, 7, 8)", "(2, 3, 4, 5, 7, 8, 9)")
        replace("mangoldt-proper-power", "lam = log2 if n in (4, 8) else logs[n]", "lam = log2 if n in (4, 8) else logs[3] if n == 9 else logs[n]")
        replace("support-upper", "17*S//8", "9*S//4")
        replace("weight-total", "< 10*C", "< 11*C")
        replace("overlap-L", "scale(diff, 17, 16*(2*j+1))", "scale(diff, 18, 16*(2*j+1))")
        replace("pair-census", "pair_count == 169", "pair_count == 225")
        replace("pole-L-square", "power17 *= 17*17", "power17 *= 18*18")
        replace("kernel-argument-square", "power544 *= 544*544", "power544 *= 576*576")
        replace("moment-midpoint-denominator", "exponent = max(4*m, 1025)", "exponent = max(4*m, 1153)")
        replace("moment-midpoint-shift", "exponent-1025", "exponent-1153")
        replace("B-one-sided-trace-2L", "17, 8*(2*j+1)))", "18, 8*(2*j+1)))")
        replace("raw-J0-L-square", "scale(value, 289, 256)", "scale(value, 81, 64)")
        replace("raw-metric-error", "<= 17*(1 << 36)", "<= 18*(1 << 36)")
        old = text[text.index("\ndef moment_rows"):]
        text = text[:text.index("\ndef moment_rows")].rstrip() + "\n"
        changes.append({"label": "remove-legacy-moment-file-helper", "discardedSHA256": digest(old.encode()), "discardedBytes": len(old.encode()), "occurrences": 1})
        replace("remove-unused-moment-pin", '\nMOMENT_SHA = "a847d543db876606c671897b11d0ecd3436b98db410d39859f8b8a24527c73ea"\n', '\n')
    if name.startswith("11"):
        replace("tail-window", "LNumerator=17, LDenominator=16", "LNumerator=9, LDenominator=8")
        replace("tail-packet-schema", '"W199_RAW_TAIL_COLUMN_CANDIDATE_V1"', '"RH_WEIL_9_8_RAW_TAIL_COLUMN_CANDIDATE_V1"')
        replace("tail-replay-schema", '"W199_RAW_TAIL_COLUMN_REPLAY_V1"', '"RH_WEIL_9_8_RAW_TAIL_COLUMN_REPLAY_V1"')
        replace("unpaid-normalized-label", '"normalizedColumnErrorPower": None if synthetic else -512', '"normalizedColumnErrorPower": None')
        replace("unpaid-ranktwo-label", '"rankTwoErrorPower": None if synthetic else -510', '"rankTwoErrorPower": None')
    if name.startswith("12"):
        replace("tail-window", '"LNumerator": 17, "LDenominator": 16', '"LNumerator": 9, "LDenominator": 8')
        replace("tail-packet-schema", '"W199_RAW_TAIL_COLUMN_CANDIDATE_V1"', '"RH_WEIL_9_8_RAW_TAIL_COLUMN_CANDIDATE_V1"')
    data = text.encode("utf-8")
    checked_ast(data, SOURCE / name)
    return data, changes


def prepare():
    need(not MANIFEST.exists() and not SOURCE.exists(), "PREPARATION_ALREADY_EXISTS")
    copies, entries = {}, []
    for name, expected in ORIGINAL_PINS.items():
        original = ORIGINAL / name
        regular(original, BASE)
        raw = original.read_bytes()
        need(digest(raw) == expected, "FROZEN_ORIGINAL_HASH:" + name)
        data, changes = patched(name, raw)
        copies[name] = data
        entries.append({"path": "source/" + name, "sha256": digest(data), "bytes": len(data),
                        "originalSHA256": expected, "originalBytes": len(raw), "patches": changes})
    # All six hashes, patch counts and ASTs pass before any source copy is written.
    SOURCE.mkdir(parents=True)
    CERT.mkdir(parents=True)
    RECEIPTS.mkdir(parents=True)
    for name, data in copies.items():
        with (SOURCE / name).open("xb") as stream:
            stream.write(data)
    manifest = {"schema": SCHEMA, "scope": STATUS, "configuration": CONFIG,
                "configurationSHA256": CONFIG_SHA, "entries": entries,
                "upstreamCommit": "b6cd2183c1e79c6c27a34267812a7b2d73ed1b59",
                "preparedAt": now(), "numericExecution": False,
                "fullWeilPositivity": "NOT_ESTABLISHED", "coreStageAdmitted": False}
    with MANIFEST.open("xb") as stream:
        stream.write(canonical(manifest))
    print(json.dumps({"status": "PREPARED_ONLY_NOT_EXECUTED", "manifest": str(MANIFEST),
                      "manifestSHA256": sha(MANIFEST), "workerSHA256": sha(__file__),
                      "configurationSHA256": CONFIG_SHA, "copiedModules": len(entries)}))


def run_stage(args):
    started, start_clock = now(), time.monotonic()
    regular(PILOT, BASE)
    need(sha(MANIFEST) == args.manifest_sha and sha(__file__) == args.worker_sha,
         "MANIFEST_OR_WORKER_PIN")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    need(manifest["schema"] == SCHEMA and same(manifest["configuration"], CONFIG)
         and manifest["configurationSHA256"] == CONFIG_SHA and manifest["scope"] == STATUS,
         "NEW_PILOT_CONFIGURATION_BINDING")
    entries = manifest["entries"]
    need(len(entries) == 6 and {Path(e["path"]).name for e in entries} == set(ORIGINAL_PINS),
         "EXACT_SIX_SOURCE_SET")
    source_pins = {}
    for entry in entries:
        path = PILOT / entry["path"]
        regular(path, SOURCE)
        need(path.parent == SOURCE and entry["originalSHA256"] == ORIGINAL_PINS[path.name]
             and sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"], "COPIED_SOURCE_PIN")
        source_pins[path] = entry["sha256"]
    names = {"isolation-test": [], "moments": [], "tails": [],
             "matrices": ["certificates/moments.json", "receipts/moments.json"]}
    allowed_reads = {MANIFEST, Path(__file__).resolve(), *source_pins}
    allowed_reads.update(RUN / name for name in names[args.stage])
    own_outputs = {RECEIPTS / (args.stage + suffix) for suffix in (".json", "-failure.json", "-access.json")}
    packet_names = {"moments": "moments.json", "matrices": "source-matrices.json", "tails": "tail-columns.json"}
    if args.stage in packet_names:
        own_outputs.add(CERT / packet_names[args.stage])
    for path in own_outputs:
        regular(path, PILOT)
        need(not path.exists(), "EXCLUSIVE_OUTPUT_ALREADY_EXISTS:" + str(path))
    input_pins = {str(path): sha(path) for path in allowed_reads if path not in source_pins}
    observed, violations = {}, []
    runtime_roots = {Path(sys.base_prefix).resolve() / "Lib", Path(sys.base_prefix).resolve() / "DLLs"}
    runtime_files = {Path(sys.executable).resolve(), Path(sys.base_prefix).resolve() / ("python%d%d.zip" % sys.version_info[:2])}
    guard_active = True

    def audit(event, values):
        if not guard_active:
            return
        if event.startswith(("socket.", "ctypes.")) or event in ("subprocess.Popen", "os.system", "os.exec", "os.posix_spawn", "os.spawn", "os.fork", "os.forkpty"):
            violations.append({"event": event})
            raise PermissionError("NETWORK_OR_PROCESS_DENIED:" + event)
        if event != "open":
            return
        if isinstance(values[0], int):
            if values[0] not in (0, 1, 2):
                violations.append({"event": "unknown-descriptor", "descriptor": values[0]})
                raise PermissionError("UNKNOWN_DESCRIPTOR")
            return
        path = Path(os.fsdecode(values[0])).resolve()
        mode, flags = values[1] or "", values[2] or 0
        writing = any(v in mode for v in "wax+") or bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        runtime = path in runtime_files or (any(within(path, root) for root in runtime_roots)
                                          and "site-packages" not in path.parts and path.suffix.lower() in (".py", ".pyc", ".pyd"))
        okay = path in own_outputs if writing else path in allowed_reads or runtime
        key = str(path) + (" | write" if writing else " | read")
        observed[key] = observed.get(key, 0) + 1
        if not okay:
            violations.append({"event": event, "path": str(path), "writing": writing})
            raise PermissionError("UNADMITTED_FILE:" + str(path))

    sys.addaudithook(audit)

    def read(path):
        return json.loads(Path(path).read_text(encoding="utf-8"))

    def write(path, obj):
        with path.open("xb") as stream:
            stream.write(canonical(obj))
        allowed_reads.add(path)
        need(same(read(path), obj), "SERIALIZED_OBJECT_MISMATCH")

    def load(index):
        paths = [p for p in source_pins if p.name.startswith("%02d-" % index)]
        need(len(paths) == 1, "MODULE_ID")
        path = paths[0]
        data = path.read_bytes()
        need(digest(data) == source_pins[path], "MODULE_CHANGED")
        checked_ast(data, path)
        name = "rh_weil_9_8_source_%02d" % index
        module = types.ModuleType(name)
        module.__file__, module.__package__ = str(path), ""
        sys.modules[name] = module
        exec(compile(data, str(path), "exec", dont_inherit=True, optimize=0), module.__dict__)
        return module

    def event(label):
        print(json.dumps({"stage": args.stage, "event": label, "elapsedSeconds": time.monotonic() - start_clock}), flush=True)

    def unchanged():
        need(all(sha(p) == expected for p, expected in source_pins.items()), "COPIED_SOURCE_CHANGED")
        need(all(sha(p) == expected for p, expected in input_pins.items()), "INPUT_CHANGED")

    def moments():
        producer, checker = load(2), load(1)
        need(same(producer.PARAMETERS, MOMENT_PARAMETERS) and same(checker.PARAMETERS, MOMENT_PARAMETERS), "MOMENT_PARAMETER_BINDING")
        event("source-moment-generation")
        rows = producer.build_moments()
        event("independent-complete-moment-oracle")
        oracle = checker.complete_oracle()
        checker.check_rows(rows, oracle)
        controls = checker.mutation_controls(rows, oracle)
        packet = {"schema": "RH_WEIL_9_8_SOURCE_MOMENTS_V1", "scope": STATUS,
                  "configurationSHA256": CONFIG_SHA, "parameters": MOMENT_PARAMETERS,
                  "rows": rows, "binetRemainderIncludedOnce": True, "fullQCertified": False}
        output = CERT / "moments.json"
        write(output, packet)
        return {"checkedMoments": len(rows), "completeIndependentContainment": True,
                "mutationControls": controls, "parameters": MOMENT_PARAMETERS, "outputSHA256": sha(output)}

    def matrices():
        moment_path, receipt_path = CERT / "moments.json", RECEIPTS / "moments.json"
        mr, mp = read(receipt_path), read(moment_path)
        need(mr["schema"] == SCHEMA and mr["status"] == STATUS and mr["stage"] == "moments"
             and mr["configurationSHA256"] == CONFIG_SHA and mr["workerSHA256"] == args.worker_sha
             and mr["sourceManifestSHA256"] == args.manifest_sha and mr["outputSHA256"] == sha(moment_path)
             and mr["completeIndependentContainment"] is True, "CHECKED_MOMENT_RECEIPT_BINDING")
        need(set(mp) == {"schema", "scope", "configurationSHA256", "parameters", "rows", "binetRemainderIncludedOnce", "fullQCertified"}
             and mp["schema"] == "RH_WEIL_9_8_SOURCE_MOMENTS_V1" and mp["scope"] == STATUS
             and mp["configurationSHA256"] == CONFIG_SHA and same(mp["parameters"], MOMENT_PARAMETERS)
             and mp["binetRemainderIncludedOnce"] is True and mp["fullQCertified"] is False,
             "1152_BIT_MOMENT_PACKET_BINDING")
        rows = mp["rows"]
        producer, checker = load(8), load(7)
        need(same(producer.PARAMS, MATRIX_PARAMETERS) and same(checker.PARAMETERS, MATRIX_PARAMETERS), "MATRIX_PARAMETER_BINDING")
        need(same(producer.ERRORS, checker.ERRORS) and same(producer.CONVENTIONS, checker.CONVENTIONS), "SOURCE_CONVENTION_BINDING")
        event("prime-constants-and-full-source-matrices")
        centers = producer.prime_sources()
        a0, a1, b0, b1, ends = producer.make_ab_seeds(centers)
        j0, j1 = producer.make_j_seeds(rows)
        arrays = {"A": producer.assemble("A", a0, a1), "B": producer.assemble("B", b0, b1, ends),
                  "J0": producer.assemble("J0", j0, j1)}
        event("independent-prime-and-matrix-oracle")
        bounds = checker.prime_source()
        parsed = checker.verify_centers(centers, bounds)
        oracle, census = checker.matrix_oracle(parsed, rows)
        pins = {p.name: h for p, h in source_pins.items()}
        config = {"sourceFiles": pins}
        identities = {"inputSHA": digest(canonical({"configSHA": CONFIG_SHA, "momentSHA": sha(moment_path)})),
                      "producerSHA": source_pins[SOURCE / "08-produce.py"], "checkerSHA": source_pins[SOURCE / "07-check.py"]}
        packet = {"schema": "RH_WEIL_9_8_SOURCE_MATRICES_V1", "status": "SOURCE_MATRICES_PRODUCED_NOT_SIGN",
                  **identities, "sourceFiles": pins, "parameters": MATRIX_PARAMETERS, "primeCenters": centers,
                  "matrices": arrays, "errors": producer.ERRORS, "sourceConventions": producer.CONVENTIONS, "createdAt": now()}
        _, checks = checker.verify_packet(packet, config, identities, bounds, oracle)
        fixture = checker.overlap_fixture()
        controls = checker.mutation_controls(packet, config, identities, bounds, oracle)
        need(census["orderedPairs"] == 225 and census["A_shifts"] == 15 and len(controls) == 9, "COMPLETE_NEW_SOURCE_CENSUS")
        output = CERT / "source-matrices.json"
        write(output, {"schema": SCHEMA, "scope": STATUS, "configurationSHA256": CONFIG_SHA,
                       "momentSHA256": sha(moment_path), "packet": packet,
                       "analyticErrorFeesPaid": False, "fullQCertified": False})
        return {"parameters": MATRIX_PARAMETERS, "primeCenters": len(centers), "orderedPairCensus": census,
                "matrixIntervals": sum(len(v) for v in arrays.values()), "matrixChecks": checks,
                "overlapFixture": fixture, "mutationControls": controls,
                "completeIndependentContainment": True, "momentSHA256": sha(moment_path), "outputSHA256": sha(output)}

    def tails():
        producer, checker = load(12), load(11)
        need(same(producer.FROZEN, TAIL_PARAMETERS) and same(checker.expected_parameters(), TAIL_PARAMETERS), "TAIL_PARAMETER_BINDING")
        event("source-tail-vectors")
        packet = producer.produce(dict(TAIL_PARAMETERS), synthetic=False)
        event("independent-factorial-quotient-oracle")
        checked = checker.replay(packet, dict(TAIL_PARAMETERS), synthetic=False)
        controls = []
        for label in ("missing-coordinate", "changed-midpoint", "nonzero-parity-coordinate", "same-width-shift"):
            changed = copy.deepcopy(packet)
            if label == "missing-coordinate":
                changed["entries"].pop()
            elif label == "changed-midpoint":
                changed["entries"][0]["midTwice"] = str(int(changed["entries"][0]["midTwice"]) + 1)
            elif label == "nonzero-parity-coordinate":
                changed["entries"][1].update(lo="1", hi="1", midTwice="2")
            else:
                for key, multiplier in (("lo", 1), ("hi", 1), ("midTwice", 2)):
                    changed["entries"][0][key] = str(int(changed["entries"][0][key]) + multiplier * (1 << 128))
            try:
                checker.replay(changed, dict(TAIL_PARAMETERS), synthetic=False)
            except ValueError as exc:
                if label == "same-width-shift":
                    need(str(exc) == "INDEPENDENT_ENCLOSURE_NOT_CONTAINED", "TAIL_SHIFT_CONTROL_NOT_CONTAINMENT")
                controls.append({"name": label, "rejected": True, "reason": str(exc)})
            else:
                raise ValueError("TAIL_NEGATIVE_CONTROL_ACCEPTED:" + label)
        output = CERT / "tail-columns.json"
        write(output, {"schema": SCHEMA, "scope": STATUS, "configurationSHA256": CONFIG_SHA,
                       "packet": packet, "analyticErrorFeesPaid": False, "fullQCertified": False})
        return {"parameters": TAIL_PARAMETERS, "tailCoordinates": len(packet["entries"]),
                "coordinateReplay": checked, "mutationControls": controls, "outputSHA256": sha(output),
                "normalizedColumnErrorClaimed": False, "rankTwoErrorClaimed": False}

    def isolation():
        controls = []
        for label, call in [("outside-read", lambda: (BASE / "forbidden-input.json").read_bytes()),
                            ("network", lambda: socket.socket()),
                            ("subprocess", lambda: subprocess.run([sys.executable, "-c", "raise SystemExit(0)"]))]:
            try:
                call()
            except PermissionError:
                controls.append({"name": label, "rejected": True})
            else:
                raise ValueError("ISOLATION_CONTROL_ACCEPTED:" + label)
        need(len(violations) == 3, "ISOLATION_CONTROL_CENSUS")
        return {"controls": controls, "expectedDeniedEvents": 3, "numericExecution": False}

    try:
        unchanged()
        result = {"isolation-test": isolation, "moments": moments, "matrices": matrices, "tails": tails}[args.stage]()
        unchanged()
        need(not violations or args.stage == "isolation-test", "AUDIT_VIOLATIONS")
        result.update({"schema": SCHEMA, "status": STATUS, "stage": args.stage,
                       "configurationSHA256": CONFIG_SHA, "sourceManifestSHA256": args.manifest_sha,
                       "workerSHA256": args.worker_sha, "startedAt": started, "finishedAt": now(),
                       "elapsedSeconds": time.monotonic() - start_clock, "inputSHA256": input_pins,
                       "sourceCodeSHA256": {p.name: h for p, h in source_pins.items()},
                       "historicalNumericalInputsRead": False, "networkUsed": False,
                       "analyticErrorFeesPaid": False, "fullQCertified": False, "coreStageAdmitted": False})
        write(RECEIPTS / (args.stage + ".json"), result)
        event(STATUS)
    except BaseException as exc:
        failure = {"schema": SCHEMA, "status": "NONPASS", "stage": args.stage,
                   "configurationSHA256": CONFIG_SHA, "workerSHA256": args.worker_sha,
                   "errorType": type(exc).__name__, "error": str(exc), "startedAt": started, "finishedAt": now(),
                   "fullQCertified": False}
        traceback.print_exc()
        write(RECEIPTS / (args.stage + "-failure.json"), failure)
        raise
    finally:
        guard_active = False
        with (RECEIPTS / (args.stage + "-access.json")).open("xb") as stream:
            stream.write(canonical({"stage": args.stage, "startedAt": started, "finishedAt": now(),
                                    "observedOpenPaths": observed, "violations": violations,
                                    "policy": "Exact source/input reads and stage-exclusive writes; standard library only; network/process/ctypes denied.",
                                    "limit": "Python audit hook for reviewed Python code, not an OS syscall sandbox."}))


def main():
    need(__debug__ and not sys.flags.optimize and sys.flags.isolated and sys.flags.no_site,
         "REQUIRE_PYTHON_I_S_B_ASSERTIONS")
    need(sys.dont_write_bytecode, "REQUIRE_B")
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["prepare", "isolation-test", "moments", "matrices", "tails"])
    parser.add_argument("--manifest-sha")
    parser.add_argument("--worker-sha")
    args = parser.parse_args()
    regular(PILOT, BASE)
    if args.stage == "prepare":
        need(args.manifest_sha is None and args.worker_sha is None, "PREPARE_TAKES_NO_RUN_PINS")
        prepare()
    else:
        need(args.manifest_sha is not None and re.fullmatch(r"[a-f0-9]{64}", args.manifest_sha)
             and args.worker_sha is not None and re.fullmatch(r"[a-f0-9]{64}", args.worker_sha), "EXPLICIT_RUN_PINS_REQUIRED")
        run_stage(args)


if __name__ == "__main__":
    main()

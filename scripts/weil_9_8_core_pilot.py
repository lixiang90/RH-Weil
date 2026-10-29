"""One fixed 9/8 finite-comparison pilot; never a full-Q/RH certificate.

Original implementation of the recorded mu=1/8 rational identities.  No
upstream program is imported.  Decimal only proposes a trial and one Gram
factor.  Exact independent contractions and every residual row pay signs.
Use -I -S -B.  prepare creates metadata only; scientific stages need pins.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from decimal import Decimal, DecimalException, ROUND_HALF_EVEN, localcontext
from fractions import Fraction as F

REPO = Path(__file__).resolve().parents[1]
PILOT = REPO / "literature/local/2026-10-29-weil-9-8/pilot"
SOURCE_RUN = PILOT / "run-01"
CORE = PILOT / "core-run-02"
MANIFEST = CORE / "manifest.json"
SOURCE_MANIFEST = PILOT / "source-manifest.json"
SOURCE_WORKER = REPO / "scripts/weil_9_8_source_pilot.py"
MATH = REPO / "reviews/2026-10-29/weil-9-8-admission/new-inverse-threshold-admission.md"
SOURCE_MANIFEST_SHA = "15ae30f087481a40d9c9d6bf3ff517ea1e50aba04b3899fcdd049c55364511e4"
SOURCE_WORKER_SHA = "7589b854cbcd2f1c2fcdf0ecce60b614af7e1d73992b6f64719e1624a0ad0961"
SOURCE_CONFIG_SHA = "8e4e59c11469cf35e5ad2e85a433660e6720ebd322d7ffd5c87d805cf2c0d364"
MATH_SHA = "e60800f4b36e737d3bd13efa0bd57bcd0d799a79ac81a0e9313f20b73450af42"
SCHEMA = "RH_WEIL_9_8_FINITE_COMPARISON_V1"
SOURCE_SCHEMA = "RH_WEIL_9_8_SOURCE_PILOT_V1"
SOURCE_STATUS = "SOURCE_ONLY_NOT_FULL_Q"
S, R, CW = 1 << 257, 1 << 256, 1 << 769
CONFIG = {"halfWidth":"9/8", "Omega":256, "N":448, "mu":"1/8",
          "m":"15/64", "b":"433/64", "rPower":-85, "polePower":-440,
          "thetaPower":-48, "chi":1, "alphaPower":-122, "betaPower":-22,
          "sourceConfigurationSHA256":SOURCE_CONFIG_SHA,
          "trialDecimalDigits":110, "trialOutputBits":256,
          "gramDecimalDigits":256, "gramOutputBits":512, "gramShiftBits":480,
          "windowWeightDegreePrecisionSearch":False, "fullQCertified":False}


def encoded(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=True)+"\n").encode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


CONFIG_SHA = hashlib.sha256(encoded(CONFIG)).hexdigest()


def need(condition, reason):
    if not condition:
        raise ValueError(reason)


def now():
    return datetime.now(timezone.utc).isoformat()


def regular(path, root):
    root, path = root.resolve(), path.absolute()
    need(path.resolve() == root or root in path.resolve().parents, "PATH_OUTSIDE_ROOT")
    for p in [path, *path.parents]:
        need(not p.is_symlink(), "SYMLINK_PATH")
        if p == root:
            break


def strict_integer(value, limit_bits=4000):
    need(type(value) is str and re.fullmatch(r"0|-?[1-9][0-9]*", value, re.ASCII), "INTEGER_ENCODING")
    x = int(value)
    need(abs(x).bit_length() <= limit_bits, "INTEGER_LIMIT")
    return x


def symmetric(matrix):
    n = len(matrix)
    need(n == 224 and all(len(row) == n for row in matrix), "SECTOR_DIMENSION")
    need(all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(i)), "MATRIX_NOT_SYMMETRIC")


def transpose(a):
    return [list(col) for col in zip(*a)]


def dot_product_multiply(a, b):
    columns = transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in columns] for row in a]


def accumulation_multiply(a, b):
    # Deliberately different loop order from the direct compiler's dot products.
    result = [[0]*len(b[0]) for _ in a]
    for i, row in enumerate(a):
        out = result[i]
        for k, coefficient in enumerate(row):
            brow = b[k]
            for j in range(len(out)):
                out[j] += coefficient*brow[j]
    return result


def matrix_strings(a):
    return [[str(x) for x in row] for row in a]


def decode_matrix(a, bits=4000):
    need(type(a) is list and len(a) == 224, "MATRIX_ROWS")
    result = [[strict_integer(x,bits) for x in row] for row in a]
    need(all(len(row) == 224 for row in result), "MATRIX_COLUMNS")
    return result


def coefficients():
    lam = F(1,2**122)+F(1,2**204)+F(1,2**220)+F(465,2**247)+F(1,2**462)+F(9,2**512)
    raw = [9*2**1025, 324, 162*2**1282*lam, 9*2**1003, 2**745, 2916*2**2051]
    need(all(F(x).denominator == 1 for x in raw), "NONINTEGER_COMPILER_COEFFICIENT")
    return [int(x) for x in raw]


def trial_proposal(a, b, q):
    """A single 110-digit stationary solve; it supplies no sign certificate."""
    n = len(q)
    system = [[q[i]*(8*b[i][j]-a[i][j])*q[j] for j in range(n)] for i in range(n)]
    rhs = [[8*q[i]*a[i][j]-(18*S if i == j else 0) for j in range(n)] for i in range(n)]
    scale_bits = max(abs(x).bit_length() for row in system for x in row)
    with localcontext() as context:
        context.prec = CONFIG["trialDecimalDigits"]
        context.rounding = ROUND_HALF_EVEN
        unit = Decimal(2)**scale_bits
        lower = [[Decimal(0)]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                value = Decimal(system[i][j])/unit
                for k in range(j):
                    value -= lower[i][k]*lower[j][k]
                if i == j:
                    need(value > 0, "TRIAL_DECIMAL_NONPOSITIVE_PIVOT")
                    lower[i][j] = value.sqrt()
                else:
                    lower[i][j] = value/lower[j][j]
        solutions = [[Decimal(0)]*n for _ in range(n)]
        for col in range(n):
            intermediate = [Decimal(0)]*n
            for i in range(n):
                value = Decimal(rhs[i][col])/unit
                for k in range(i):
                    value -= lower[i][k]*intermediate[k]
                intermediate[i] = value/lower[i][i]
            for i in range(n-1,-1,-1):
                value = intermediate[i]
                for k in range(i+1,n):
                    value -= lower[k][i]*solutions[k][col]
                solutions[i][col] = value/lower[i][i]
        z = [[int((value*R).to_integral_value(rounding=ROUND_HALF_EVEN)) for value in row] for row in solutions]
    need(all(abs(x) <= 2**272 for row in z for x in row), "TRIAL_Z_CAP")
    nu = sum(q[i]*q[j]*z[i][j]**2 for i in range(n) for j in range(n))
    k = 0
    while nu > 1 << (512+2*k):
        k += 1
    need(k <= 37, "ACTUAL_FROBENIUS_NORM_CAP")
    return z, {"normPower":k, "normUpper":str(1<<k), "squaredFrobeniusNumerator":str(nu),
               "squaredFrobeniusDenominatorPower":512, "trialDecimalDigits":110}


def inverse_integer(a, b, z, q, norm_power):
    y, n = 1 << norm_power, len(q)
    u = [[q[i]*x for x in z[i]] for i in range(n)]
    au, bu = dot_product_multiply(a,u), dot_product_multiply(b,u)
    quad_a = dot_product_multiply(transpose(u),au)
    quad_b = dot_product_multiply(transpose(u),bu)
    f = [[18*S*R*(z[i][j]+z[j][i])-quad_a[i][j]+8*quad_b[i][j]
          -8*R*(au[i][j]+au[j][i]) for j in range(n)] for i in range(n)]
    need(all(abs(x) < 2**864 for row in f for x in row), "F_INTEGER_CAP")
    c = 8*CW+(9*y*y+16*y)*2**549
    v = [[q[i]*q[j]*f[i][j]+(18*c*q[i] if i == j else 0) for j in range(n)] for i in range(n)]
    symmetric(v)
    need(all(v[i][j] % q[j] == 0 for i in range(n) for j in range(n)), "V_COLUMN_DIVISIBILITY")
    need(all(abs(x) < 2**891 for row in v for x in row), "V_INTEGER_CAP")
    return v


def direct_compiler(a,b,j,tails,q,v):
    """Six separate source contractions; no combined-kernel intermediate."""
    c_j,c_u,c_g,c_b,c_aa,c_w = coefficients()
    n = len(q)
    vjv = dot_product_multiply(v,dot_product_multiply(j,v))
    vbv = dot_product_multiply(v,dot_product_multiply(b,v))
    v_div = [[v[i][k]//q[k] for k in range(n)] for i in range(n)]
    vqv = dot_product_multiply(v_div,v)
    av = dot_product_multiply(a,v)
    av_q = [[q[k]*av[k][i] for k in range(n)] for i in range(n)]
    avqav = dot_product_multiply(av_q,av)
    vt = [[sum(v[i][k]*tail[k] for k in range(n)) for i in range(n)] for tail in tails]
    return [[c_j*vjv[i][k]-c_g*vqv[i][k]-c_b*vbv[i][k]+c_aa*avqav[i][k]
             +c_u*sum(t[i]*t[k] for t in vt)+c_w*v[i][k] for k in range(n)] for i in range(n)]


def combined_compiler(a,b,j,tails,q,v):
    """An independent accumulated combined-kernel formula."""
    c_j,c_u,c_g,c_b,c_aa,c_w = coefficients()
    n = len(q)
    aqa = [[0]*n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            coefficient = a[i][k]*q[k]
            for col in range(n):
                aqa[i][col] += coefficient*a[k][col]
    middle = [[q[i]*(c_j*j[i][col]-c_b*b[i][col]+c_aa*aqa[i][col])*q[col]
               -(c_g*q[i] if i == col else 0)
               +c_u*sum((q[i]*t[i])*(q[col]*t[col]) for t in tails)
               for col in range(n)] for i in range(n)]
    yv = [[v[i][col]//q[col] for col in range(n)] for i in range(n)]
    answer = accumulation_multiply(accumulation_multiply(yv,middle),transpose(yv))
    return [[answer[i][col]+c_w*v[i][col] for col in range(n)] for i in range(n)]


def failed_direction(k, lower, pivot):
    """Propose one rational witness; exact original K evaluation decides it."""
    vector = [Decimal(0)]*len(k)
    vector[pivot] = Decimal(1)
    for i in range(pivot-1,-1,-1):
        value = -lower[pivot][i]
        for h in range(i+1,pivot):
            value -= lower[h][i]*vector[h]
        vector[i] = value/lower[i][i]
    out = [int((x*(1<<512)).to_integral_value(rounding=ROUND_HALF_EVEN)) for x in vector]
    quadratic = sum(out[i]*sum(k[i][h]*out[h] for h in range(len(k))) for i in range(len(k)))
    return {"vector": [str(x) for x in out], "vectorDenominatorPower":512,
            "quadraticNumerator":str(quadratic), "quadraticDenominatorPower":1024,
            "actualFiniteTargetNegative":quadratic < 0,
            "scope":"Original finite comparison K only; never a negative full-Q test"}


def gram_proposal(k):
    n = len(k)
    scale = max(1,max(abs(x).bit_length() for row in k for x in row))
    with localcontext() as context:
        context.prec = CONFIG["gramDecimalDigits"]
        context.rounding = ROUND_HALF_EVEN
        unit, shift = Decimal(2)**scale, Decimal(2)**-480
        lower = [[Decimal(0)]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                value = Decimal(k[i][j])/unit-(shift if i == j else 0)
                for h in range(j):
                    value -= lower[i][h]*lower[j][h]
                if i == j:
                    if value <= 0:
                        return {"kind":"inconclusive", "reason":"GRAM_DECIMAL_NONPOSITIVE_PIVOT",
                                "pivot":i,"targetScaleBits":scale,
                                "direction":failed_direction(k,lower,i)}
                    lower[i][j] = value.sqrt()
                else:
                    lower[i][j] = value/lower[j][j]
        factor = [[int((x*(1<<512)).to_integral_value(rounding=ROUND_HALF_EVEN)) for x in row] for row in lower]
    return {"kind":"factor", "targetScaleBits":scale, "factor":factor}


def residual_check(k,factor,scale,*,early=False):
    n = len(k)
    need(len(factor) == n and all(len(row) == n for row in factor), "GRAM_FACTOR_DIMENSION")
    need(all(factor[i][j] == 0 for i in range(n) for j in range(i+1,n)), "GRAM_FACTOR_TRIANGULAR")
    diagonal = 1 << (scale+544)
    rows = []
    for i in range(n):
        total = 0
        for j in range(n):
            product = sum(factor[i][h]*factor[j][h] for h in range(min(i,j)+1))
            remainder = (k[i][j]<<1024)-(product<<scale)-(diagonal if i == j else 0)
            total += abs(remainder)
        rows.append(total)
        if early and total >= diagonal:
            return False,rows
    return max(rows) < diagonal,rows


def prepare():
    regular(CORE,PILOT)
    need(not CORE.exists(), "CORE_PREPARATION_ALREADY_EXISTS")
    need(sha(SOURCE_MANIFEST) == SOURCE_MANIFEST_SHA and sha(SOURCE_WORKER) == SOURCE_WORKER_SHA
         and sha(MATH) == MATH_SHA, "FIXED_PREPARATION_PINS")
    metadata = {"schema":SCHEMA,"configuration":CONFIG,"configurationSHA256":CONFIG_SHA,
                "workerSHA256":sha(__file__),"sourceWorkerSHA256":SOURCE_WORKER_SHA,
                "sourceManifestSHA256":SOURCE_MANIFEST_SHA,"mathematicalRecordSHA256":MATH_SHA,
                "preparedAt":now(),"numericExecution":False,"fullQCertified":False}
    CORE.mkdir()
    with MANIFEST.open("xb") as stream:
        stream.write(encoded(metadata))
    print(json.dumps({"status":"CORE_PREPARED_NOT_EXECUTED","manifestSHA256":sha(MANIFEST),
                      "workerSHA256":sha(__file__),"configurationSHA256":CONFIG_SHA}))


def execute(args):
    regular(CORE,PILOT)
    need(sha(__file__) == args.worker_sha and sha(MANIFEST) == args.manifest_sha, "CORE_RUN_PINS")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    need(manifest["schema"] == SCHEMA and manifest["workerSHA256"] == args.worker_sha and manifest["configuration"] == CONFIG
         and manifest["configurationSHA256"] == CONFIG_SHA,"CORE_CONFIGURATION")
    source_files = {SOURCE_MANIFEST:SOURCE_MANIFEST_SHA,SOURCE_WORKER:SOURCE_WORKER_SHA,MATH:MATH_SHA}
    if args.stage != "isolation-test":
        for name in ("moments","matrices","tails"):
            source_files[SOURCE_RUN/"receipts"/(name+".json")] = None
        for name in ("moments.json","source-matrices.json","tail-columns.json"):
            source_files[SOURCE_RUN/"certificates"/name] = None
    allowed = {Path(__file__).resolve(),MANIFEST,*source_files}
    stage_outputs = {CORE/(args.stage+suffix) for suffix in ("-receipt.json","-failure.json","-access.json")}
    if args.stage == "trial":
        stage_outputs.update(CORE/(p+"-trial.json") for p in ("even","odd"))
    if args.stage in ("compile","gram"):
        allowed.update(CORE/(p+"-trial.json") for p in ("even","odd"))
        allowed.add(CORE/"trial-receipt.json")
    if args.stage == "compile":
        stage_outputs.update(CORE/(p+"-target.json") for p in ("even","odd"))
    if args.stage == "gram":
        allowed.update(CORE/(p+"-target.json") for p in ("even","odd"))
        allowed.add(CORE/"compile-receipt.json")
        stage_outputs.update(CORE/(p+"-gram.json") for p in ("even","odd"))
    for path in stage_outputs:
        regular(path,PILOT)
        need(not path.exists(),"CORE_EXCLUSIVE_OUTPUT:"+str(path))
    for path,expected in source_files.items():
        regular(path,REPO)
        need(expected is None or sha(path) == expected,"SOURCE_FIXED_PIN")
    input_pins = {str(path):sha(path) for path in allowed}
    observed,violations = {},[]
    runtime_roots = [Path(sys.base_prefix).resolve()/"Lib",Path(sys.base_prefix).resolve()/"DLLs"]
    runtime_files = {Path(sys.executable).resolve(),Path(sys.base_prefix).resolve()/("python%d%d.zip" % sys.version_info[:2])}
    guard = True

    def audit(event,values):
        if not guard:
            return
        if event.startswith(("socket.","ctypes.")) or event in ("subprocess.Popen","os.system","os.exec","os.posix_spawn","os.spawn","os.fork","os.forkpty"):
            violations.append({"event":event})
            raise PermissionError("NETWORK_PROCESS_DENIED:"+event)
        if event != "open":
            return
        if isinstance(values[0],int):
            need(values[0] in (0,1,2),"UNKNOWN_DESCRIPTOR")
            return
        path = Path(os.fsdecode(values[0])).resolve()
        mode,flags = values[1] or "",values[2] or 0
        writing = any(x in mode for x in "wax+") or bool(flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))
        runtime = path in runtime_files or any((path == p or p in path.parents) and "site-packages" not in path.parts
                                               and path.suffix.lower() in (".py",".pyc",".pyd") for p in runtime_roots)
        okay = path in stage_outputs if writing else path in allowed or runtime
        key = str(path)+(" | write" if writing else " | read")
        observed[key] = observed.get(key,0)+1
        if not okay:
            violations.append({"event":event,"path":str(path),"writing":writing})
            raise PermissionError("UNADMITTED_FILE:"+str(path))

    sys.addaudithook(audit)
    started,clock = now(),time.monotonic()

    def read(path):
        return json.loads(path.read_text(encoding="utf-8"))

    def write(path,value):
        with path.open("xb") as stream:
            stream.write(encoded(value))
        allowed.add(path)
        need(read(path) == value,"SERIALIZED_OUTPUT_MISMATCH")

    def event(message,sector=None):
        print(json.dumps({"stage":args.stage,"event":message,"sector":sector,
                          "elapsedSeconds":time.monotonic()-clock}),flush=True)

    def unchanged():
        need(all(sha(path) == expected for path,expected in input_pins.items()),"INPUT_CHANGED")

    def bound_output(stage,name):
        receipt = read(CORE/(stage+"-receipt.json"))
        need(receipt["status"] == "FINITE_STAGE_PASS_NOT_FULL_Q" and receipt["stage"] == stage
             and receipt["configurationSHA256"] == CONFIG_SHA and receipt["workerSHA256"] == args.worker_sha
             and receipt["outputs"][name] == sha(CORE/name)
             and all(input_pins.get(p) == h for p,h in receipt["inputSHA256"].items()),"CORE_PRIOR_STAGE_BINDING")
        return read(CORE/name)

    def sources():
        for stage,packet_name in (("moments","moments.json"),("matrices","source-matrices.json"),("tails","tail-columns.json")):
            receipt = read(SOURCE_RUN/"receipts"/(stage+".json"))
            packet_path = SOURCE_RUN/"certificates"/packet_name
            need(receipt["schema"] == SOURCE_SCHEMA and receipt["status"] == SOURCE_STATUS
                 and receipt["stage"] == stage and receipt["configurationSHA256"] == SOURCE_CONFIG_SHA
                 and receipt["workerSHA256"] == SOURCE_WORKER_SHA and receipt["sourceManifestSHA256"] == SOURCE_MANIFEST_SHA
                 and receipt["outputSHA256"] == sha(packet_path) and receipt["fullQCertified"] is False,"SOURCE_RECEIPT_BINDING")
            if stage in ("moments","matrices"):
                need(receipt["completeIndependentContainment"] is True,"SOURCE_ORACLE_MISSING")
            if stage == "moments":
                need(receipt["checkedMoments"] == 1024 and len(receipt["mutationControls"]) == 4,"MOMENT_COVERAGE")
            elif stage == "matrices":
                need(receipt["matrixIntervals"] == 151200 and receipt["primeCenters"] == 15
                     and receipt["orderedPairCensus"]["orderedPairs"] == 225 and len(receipt["mutationControls"]) == 9,"MATRIX_COVERAGE")
            else:
                need(receipt["tailCoordinates"] == 896 and len(receipt["mutationControls"]) == 4,"TAIL_COVERAGE")
        mp = read(SOURCE_RUN/"certificates/moments.json")
        need(mp["parameters"]["outputBits"] == 1152 and mp["parameters"]["radiusBits"] == 1098
             and mp["binetRemainderIncludedOnce"] is True,"TRUE_MOMENT_PRECISION")
        matrix = read(SOURCE_RUN/"certificates/source-matrices.json")
        tail = read(SOURCE_RUN/"certificates/tail-columns.json")
        for wrapper in (matrix,tail):
            need(wrapper["schema"] == SOURCE_SCHEMA and wrapper["scope"] == SOURCE_STATUS
                 and wrapper["configurationSHA256"] == SOURCE_CONFIG_SHA and wrapper["fullQCertified"] is False,"SOURCE_WRAPPER")
        need(matrix["momentSHA256"] == sha(SOURCE_RUN/"certificates/moments.json"),"MATRIX_MOMENT_CHAIN")
        parameters = matrix["packet"]["parameters"]
        need(parameters["L"] == "9/8" and parameters["N"] == 448 and parameters["outputBits"] == 256,"RAW_MATRIX_SCALE")
        raw = {}
        for name,rows in matrix["packet"]["matrices"].items():
            need(name in ("A","B","J0") and len(rows) == 50400,"RAW_MATRIX_COVERAGE")
            full = [[0]*448 for _ in range(448)]
            cursor = 0
            for i in range(448):
                for j in range(i,448,2):
                    row = rows[cursor]
                    need(type(row) is list and len(row) == 4 and row[:2] == [i,j],"RAW_MATRIX_ORDER")
                    lo,hi = strict_integer(row[2]),strict_integer(row[3])
                    need(lo <= hi,"RAW_MATRIX_INTERVAL")
                    full[i][j] = full[j][i] = lo+hi
                    cursor += 1
            need(cursor == 50400 and all(abs(x) <= 2**273 for row in full for x in row),"RAW_CENTER_CAP")
            raw[name] = full
        need(set(raw) == {"A","B","J0"},"RAW_SOURCE_SET")
        tp = tail["packet"]
        need(tp["parameters"]["outputBits"] == 640 and tp["parameters"]["LNumerator"] == 9
             and tp["parameters"]["LDenominator"] == 8 and tp["synthetic"] is False,"TAIL_SCALE")
        columns = [[0]*448 for _ in range(2)]
        need(len(tp["entries"]) == 896,"TAIL_ENTRIES")
        for number,entry in enumerate(tp["entries"]):
            col,index = divmod(number,448)
            need(entry["column"] == col and entry["index"] == index,"TAIL_ORDER")
            value = strict_integer(entry["midTwice"])
            need(value == strict_integer(entry["lo"])+strict_integer(entry["hi"])
                 and abs(value) <= 2**641 and (index%2 == col or value == 0),"TAIL_MIDPOINT")
            columns[col][index] = value
        return raw,columns

    outputs,result = {},{}
    try:
        unchanged()
        if args.stage == "isolation-test":
            controls = []
            for label,call in (("outside-read",lambda:(PILOT/"forbidden-core.json").read_bytes()),
                               ("socket",lambda:socket.socket()),
                               ("subprocess",lambda:subprocess.run([sys.executable,"-c","raise SystemExit(0)"]))):
                try:
                    call()
                except PermissionError:
                    controls.append({"name":label,"rejected":True})
                else:
                    raise ValueError("ISOLATION_CONTROL_ACCEPTED")
            need(len(violations) == 3,"ISOLATION_CONTROL_CENSUS")
            result["controls"] = controls
        else:
            raw,tails = sources()
            for parity,label in ((0,"even"),(1,"odd")):
                indices = list(range(parity,448,2))
                q = [8*(2*i+1) for i in indices]
                a,b,j = [[[raw[name][i][h] for h in indices] for i in indices] for name in ("A","B","J0")]
                columns = [[t[i] for i in indices] for t in tails]
                for mat in (a,b,j):
                    symmetric(mat)
                if args.stage == "trial":
                    event("stationary-trial-proposal",label)
                    z,norm = trial_proposal(a,b,q)
                    packet = {"schema":SCHEMA,"configurationSHA256":CONFIG_SHA,"sector":label,
                              "Z":matrix_strings(z),"norm":norm,"fullQCertified":False}
                    filename = label+"-trial.json"
                elif args.stage == "compile":
                    trial = bound_output("trial",label+"-trial.json")
                    z = decode_matrix(trial["Z"],273)
                    nu = sum(q[i]*q[h]*z[i][h]**2 for i in range(224) for h in range(224))
                    power = trial["norm"]["normPower"]
                    need(type(power) is int and 0 <= power <= 37 and nu <= 1 << (512+2*power)
                         and str(nu) == trial["norm"]["squaredFrobeniusNumerator"],"ACTUAL_TRIAL_NORM")
                    event("inverse-integer-and-direct-compiler",label)
                    v = inverse_integer(a,b,z,q,power)
                    target = direct_compiler(a,b,j,columns,q,v)
                    event("independent-combined-compiler",label)
                    second = combined_compiler(a,b,j,columns,q,v)
                    need(all(target[i][h] == second[i][h] for i in range(224) for h in range(224)),"COMPILER_ENTRY_MISMATCH")
                    symmetric(target)
                    need(all(abs(x) < 2**3200 for row in target for x in row),"TARGET_INTEGER_CAP")
                    packet = {"schema":SCHEMA,"configurationSHA256":CONFIG_SHA,"sector":label,
                              "target":matrix_strings(target),"coefficients":[str(x) for x in coefficients()],
                              "completeCompilerEquality":True,"entryComparisons":224**2,
                              "normPower":power,"VColumnDivisibility":True,"fullQCertified":False}
                    filename = label+"-target.json"
                else:
                    compiled = bound_output("compile",label+"-target.json")
                    need(compiled["completeCompilerEquality"] is True,"UNCHECKED_COMPILER")
                    target = decode_matrix(compiled["target"],3200)
                    symmetric(target)
                    event("single-decimal-Gram-proposal",label)
                    proposal = gram_proposal(target)
                    if proposal["kind"] != "factor":
                        write(CORE/(label+"-gram.json"),{**proposal,"schema":SCHEMA,"configurationSHA256":CONFIG_SHA,
                                                        "fullQCertified":False})
                        raise ValueError("FINITE_GRAM_PROPOSAL_INCONCLUSIVE:"+label)
                    factor,scale = proposal["factor"],proposal["targetScaleBits"]
                    event("complete-exact-residual-rows",label)
                    passed,rows = residual_check(target,factor,scale)
                    packet = {"schema":SCHEMA,"configurationSHA256":CONFIG_SHA,"sector":label,
                              "factor":matrix_strings(factor),"targetScaleBits":scale,
                              "gramCoefficientPower":scale,"diagonalPower":scale+544,
                              "targetMultiplicationPower":1024,"allRowSums":[str(x) for x in rows],
                              "allRowsStrict":passed,"complexSignCovered":passed,"fullQCertified":False}
                    if not passed:
                        write(CORE/(label+"-gram.json"),packet)
                        raise ValueError("FINITE_EXACT_RESIDUAL_NONPASS:"+label)
                    changed = [row[:] for row in factor]
                    changed[0][0] += 1 << 600
                    mutated_pass,_ = residual_check(target,changed,scale,early=True)
                    need(not mutated_pass,"FACTOR_MUTATION_ACCEPTED")
                    packet["factorMutationRejected"] = True
                    write(CORE/(label+"-gram.json"),packet)
                    outputs[label+"-gram.json"] = sha(CORE/(label+"-gram.json"))
                    result[label] = {"targetScaleBits":scale,"checkedRows":224,"allRowsStrict":True,
                                     "factorMutationRejected":True}
                    continue
                write(CORE/filename,packet)
                outputs[filename] = sha(CORE/filename)
                result[label] = {"packet":filename,"status":"GENERATED_AND_CHECKED_NOT_FULL_Q"}
        unchanged()
        need(not violations or args.stage == "isolation-test","AUDIT_VIOLATIONS")
        receipt = {"schema":SCHEMA,"status":"FINITE_STAGE_PASS_NOT_FULL_Q","stage":args.stage,
                   "configurationSHA256":CONFIG_SHA,"workerSHA256":args.worker_sha,
                   "sourceManifestSHA256":SOURCE_MANIFEST_SHA,"coreManifestSHA256":args.manifest_sha,
                   "inputSHA256":input_pins,"outputs":outputs,"results":result,
                   "startedAt":started,"finishedAt":now(),"elapsedSeconds":time.monotonic()-clock,
                   "fullQCertified":False,"requiresRootAnalyticPremiseClosure":True,
                   "noParameterSearch":True,"networkUsed":False,
                   "sourceOnlyReceiptsDoNotPayAnalyticFees":True}
        write(CORE/(args.stage+"-receipt.json"),receipt)
        event("FINITE_STAGE_PASS_NOT_FULL_Q")
    except BaseException as exc:
        traceback.print_exc()
        write(CORE/(args.stage+"-failure.json"),{"schema":SCHEMA,"status":"NONPASS","stage":args.stage,
              "configurationSHA256":CONFIG_SHA,"workerSHA256":args.worker_sha,"errorType":type(exc).__name__,
              "error":str(exc),"startedAt":started,"finishedAt":now(),"partialOutputs":outputs,
              "fullQCertified":False,"finiteFailureDoesNotEstablishNegativeQ":True})
        raise
    finally:
        guard = False
        with (CORE/(args.stage+"-access.json")).open("xb") as stream:
            stream.write(encoded({"observedOpenPaths":observed,"violations":violations,
                                  "policy":"Exact pinned inputs, exclusive outputs, stdlib; network/process/ctypes denied",
                                  "limit":"Python audit for reviewed code, not an OS syscall sandbox"}))


def main():
    need(__debug__ and sys.flags.isolated and sys.flags.no_site and not sys.flags.optimize
         and sys.dont_write_bytecode,"REQUIRE_PYTHON_I_S_B_ASSERTIONS")
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage",choices=["prepare","isolation-test","trial","compile","gram"])
    parser.add_argument("--worker-sha")
    parser.add_argument("--manifest-sha")
    args = parser.parse_args()
    if args.stage == "prepare":
        need(args.worker_sha is None and args.manifest_sha is None,"PREPARE_TAKES_NO_PINS")
        prepare()
    else:
        need(args.worker_sha and re.fullmatch("[a-f0-9]{64}",args.worker_sha)
             and args.manifest_sha and re.fullmatch("[a-f0-9]{64}",args.manifest_sha),"EXPLICIT_CORE_PINS_REQUIRED")
        execute(args)


if __name__ == "__main__":
    main()

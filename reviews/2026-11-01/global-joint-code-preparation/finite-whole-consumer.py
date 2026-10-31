"""Prospective no-alpha whole consumer; CODE PREPARATION, NOT RUN ADMISSION.

Stdlib only. Never import/invoke an old scientific driver. Exact old point
centers and the ONE future shared five-block packet define the tested model.
Only active [F,X] is solved. No dense inverse, Y array, packet copy or alternate
consumer is written. The future independent finite checker is still required.

The CLI accepts ONLY a separately pinned NEW C069 root execution freeze. The
current preparation spec has false numerical flags and cannot authorize it.
Current preparation may AST-extract pure kernels for isolated synthetic tests;
do not import this module or call main/load_centers/evaluate on actual data.
"""
from __future__ import annotations
import time
PROCESS_STARTED = time.monotonic()
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SELF = Path(__file__).resolve()
OUTER = ROOT / "literature/local/2026-11-01-directional-remainder-whole/run-01"
OUT = OUTER / "stage-02-finite"
TARGET = "RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1"
N, SECTOR, P, RAW = 448, 224, 1024, 256
UNIT = 1 << P
NORMAL_BITS, DIAGNOSTIC_BITS = 16384, 65536
FEE = F(1, 1 << 224) + F(1, 1 << 216) + F(1, 1 << 216)
EPS, ETA = F(1, 1 << 226), F(1, 1 << 221)
DLOW = F(15, 64) - F(896, 1 << 170) - F(1, 1 << 440)
CINV = F(209, 32)
OLD = "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/"
MATRIX, TAIL = OLD + "source-matrices.json", OLD + "tail-columns.json"
GCOLS = "literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl"
SOURCE_PINS = {
    MATRIX: "a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
    TAIL: "d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
    GCOLS: "d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080",
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
        "3223cffd0205b9a1f8660445ac33d0f3cec13b3bd1fa5e7799ed8abfb2746d42",
}
PARAMETERS = dict(N=N, sectorDimension=SECTOR, intervalBits=P, rawBits=RAW,
    maxNormalIntegerBits=NORMAL_BITS, maxDiagnosticBits=DIAGNOSTIC_BITS,
    activeDimensionPerParity=448, sectorOrder=["even", "odd"],
    jointPaddingPower=-221, coefficientNuPower=-216, headBetaPower=-224,
    finiteZetaPower=-216, sourceArithmeticPower=-230, alpha=None,
    YBottomCoefficient=0, packetRows=401856, independentCheckerRequired=True,
    oneAttempt=True, inverseOutput=False, packetCopyOutput=False,
    ordinaryUnresolvedPolicy="TERMINAL_UNRESOLVED_NO_RETRY")


def need(ok, message):
    if not ok:
        raise ValueError(message)


class IntegerWidthError(ValueError):
    def __init__(self, value):
        self.value = value
        self.bitLength = abs(value).bit_length()
        super().__init__("NORMAL_INTEGER_WIDTH_STOP bits=" + str(self.bitLength))


def checked(a):
    need(type(a) is int, "INTEGER_TYPE")
    if abs(a).bit_length() > NORMAL_BITS:
        raise IntegerWidthError(a)
    return a


def width_diagnostic(error):
    result = dict(actualBitLength=error.bitLength, normalLimitBits=NORMAL_BITS,
        diagnosticLimitBits=DIAGNOSTIC_BITS, arithmeticValueUsable=False,
        technicalStopOnly=True, mathematicalSignConclusion=False)
    if error.bitLength <= DIAGNOSTIC_BITS:
        result.update(fullDiagnosticValuePresent=True, encoding="SIGNED_HEX_DIAGNOSTIC_ONLY",
            value=("-0x" if error.value < 0 else "0x") + format(abs(error.value), "x"))
    else:
        result.update(fullDiagnosticValuePresent=False, encoding="OMITTED_ABOVE_DIAGNOSTIC_CAP",
                      value=None, omissionDoesNotAuthorizeRetry=True)
    return result


def ceildiv(a, b):
    need(b > 0, "POSITIVE_DIVISOR")
    return -((-a) // b)


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


def integer(value):
    need(type(value) is str and len(value) <= 6000, "INTEGER_STRING_SIZE")
    result = int(value)
    need(str(result) == value, "NONCANONICAL_INTEGER")
    return checked(result)


def point(q):
    q = F(q)
    checked(q.numerator)
    checked(q.denominator)
    return (checked(q.numerator * UNIT // q.denominator),
            checked(ceildiv(q.numerator * UNIT, q.denominator)))


def add(a, b):
    return checked(a[0] + b[0]), checked(a[1] + b[1])


def sub(a, b):
    return checked(a[0] - b[1]), checked(a[1] - b[0])


def neg(a):
    return checked(-a[1]), checked(-a[0])


def mul(a, b):
    vals = [x * y for x in a for y in b]
    return checked(min(vals) // UNIT), checked(ceildiv(max(vals), UNIT))


def square(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(a[0] ** 2, a[1] ** 2)
    hi = max(a[0] ** 2, a[1] ** 2)
    return checked(lo // UNIT), checked(ceildiv(hi, UNIT))


def divpos(a, b):
    need(b[0] > 0, "POSITIVE_INTERVAL_DIVISOR")
    if a[0] >= 0:
        lo, hi = a[0] * UNIT // b[1], ceildiv(a[1] * UNIT, b[0])
    elif a[1] <= 0:
        lo, hi = a[0] * UNIT // b[0], ceildiv(a[1] * UNIT, b[1])
    else:
        lo, hi = a[0] * UNIT // b[0], ceildiv(a[1] * UNIT, b[0])
    return checked(lo), checked(hi)


def intersect(a, b):
    v = max(a[0], b[0]), min(a[1], b[1])
    need(v[0] <= v[1], "SYMMETRIC_ENCLOSURES_DISJOINT")
    return v


ZERO, ONE = (0, 0), (UNIT, UNIT)


def transpose(a):
    return [list(row) for row in zip(*a)]


def iv_product(a, b, tick, label):
    cols = transpose(b)
    need(a and b and len(a[0]) == len(b), "PRODUCT_SHAPE")
    out = []
    for i, row in enumerate(a):
        tick(label, row=i)
        r = []
        for j, col in enumerate(cols):
            total = ZERO
            for x, y in zip(row, col):
                total = add(total, mul(x, y))
            r.append(total)
            if j % 8 == 0:
                tick(label, row=i, column=j)
        out.append(r)
    return out


def symmetrize(a):
    need(len(a) == len(a[0]), "SYMMETRIC_SHAPE")
    for i in range(len(a)):
        for j in range(i, len(a)):
            a[i][j] = a[j][i] = intersect(a[i][j], a[j][i])
    return a


def interval_ldl(a, tick, emit, phase, sector):
    """Enclose ONE exact symmetric matrix; no point-matrix shortcut.

    Positive prefix pivots are required for every division. A negative pivot
    encloses the exact LDL pivot strictly below zero and refutes THIS exact
    sufficient model, without making an actual Lret/Q sign claim.
    """
    a = [row[:] for row in a]
    n = len(a)
    ell = [[ZERO] * n for _ in range(n)]
    ds = []
    for k in range(n):
        d = a[k][k]
        tick(phase, pivot=k, sector=sector)
        emit(dict(phase=phase, sector=sector, pivot=k,
                  endpoints=list(map(str, d)), endpointBits=P))
        if d[1] < 0:
            return "STRICT_NEGATIVE_PIVOT", ell, ds, k
        if d[0] <= 0:
            return "INTERVAL_UNRESOLVED", ell, ds, k
        ds.append(d)
        ell[k][k] = ONE
        for i in range(k + 1, n):
            ell[i][k] = divpos(a[i][k], d)
        for i in range(k + 1, n):
            tick(phase, sector=sector, pivot=k, row=i)
            for j in range(i, n):
                p = square(a[i][k]) if i == j else mul(a[i][k], a[j][k])
                a[i][j] = a[j][i] = sub(a[i][j], divpos(p, d))
                if j % 16 == 0:
                    tick(phase, sector=sector, pivot=k, row=i, column=j)
    return "ALL_POSITIVE", ell, ds, n


def interval_solve(ell, ds, rhs, tick, sector):
    """H^-1 rhs from outward LDL; no dense inverse is constructed."""
    n, nrhs = len(ell), len(rhs[0])
    need(len(ds) == n and len(rhs) == n, "SOLVE_SHAPE")
    v = [[ZERO] * nrhs for _ in range(n)]
    for i in range(n):
        tick("active-forward-solve", sector=sector, row=i)
        for j in range(nrhs):
            s = rhs[i][j]
            for k in range(i):
                s = sub(s, mul(ell[i][k], v[k][j]))
            v[i][j] = s
        tick("active-forward-solve", sector=sector, row=i)
    for i in range(n):
        for j in range(nrhs):
            v[i][j] = divpos(v[i][j], ds[i])
        tick("active-diagonal-solve", sector=sector, row=i)
    z = [[ZERO] * nrhs for _ in range(n)]
    for i in range(n - 1, -1, -1):
        tick("active-backward-solve", sector=sector, row=i)
        for j in range(nrhs):
            s = v[i][j]
            for k in range(i + 1, n):
                s = sub(s, mul(ell[k][i], z[k][j]))
            z[i][j] = s
        tick("active-backward-solve", sector=sector, row=i)
    return z


def exact_product(a, b, tick, label):
    cols = transpose(b)
    out = []
    for i, row in enumerate(a):
        tick(label, row=i)
        out.append([checked(sum(x * y for x, y in zip(row, col))) for col in cols])
    return out


def old_head_and_covariance(parity, centers, tick):
    """Exact raw point matrices; same algebra as the already paid head source.

    No head sign/prefix is tested here. Head assembly is a dependency of the
    actual whole consumer. Source denominators are A/B/J0/G=2^257,h=2^641.
    """
    aa, bb, jj, hh, gg = centers
    idx = list(range(parity, N, 2))
    n = len(idx)
    w = [2 * j + 1 for j in idx]
    d = [F(9, 4 * x) for x in w]
    a = [[aa[i][j] for j in idx] for i in idx]
    b = [[bb[i][j] for j in idx] for i in idx]
    g = [[gg[i][j] for j in idx] for i in idx]
    c = [[checked(((aa[i][j] + jj[i][j]) << 1025) +
           36 * sum(hh[s][i] * hh[s][j] for s in (0, 1))) for j in idx] for i in idx]
    aw = [[a[i][j] * w[j] for j in range(n)] for i in range(n)]
    a2 = exact_product(aw, a, tick, "exact-old-covariance")
    dh = [[F(b[i][j], 1 << 257) - F(a2[i][j], 9 * (1 << 512))
           for j in range(n)] for i in range(n)]
    # D^-1 has factor4/9; A denominator2^257, hence4/2^514=1/2^512.
    bscale = 9 * (1 << 255)
    bi = [[checked((bscale if i == j else 0) + w[i] * g[i][j])
           for j in range(n)] for i in range(n)]
    b0 = [[F(x, bscale) for x in row] for row in bi]
    gw = [[g[i][j] * w[j] for j in range(n)] for i in range(n)]
    jint = exact_product(gw, g, tick, "exact-old-head-metric")
    cp = [[checked(c[i][j] + (g[i][j] << 1025)) for j in range(n)] for i in range(n)]
    tmp = exact_product(cp, bi, tick, "exact-old-head-right-congruence")
    ki = exact_product(transpose(bi), tmp, tick, "exact-old-head-left-congruence")
    for i in range(n):
        for j in range(n):
            ki[i][j] = checked(ki[i][j] - 81 * (g[i][j] << 1535)
                                 - 9 * (jint[i][j] << 1280))
        tick("exact-old-head-subtractions", row=i)
    khead = [[F(x, 81 * (1 << 1792)) for x in row] for row in ki]
    thead = [[(d[i] if i == j else F(0)) + F(2 * g[i][j], 1 << 257)
                + F(jint[i][j], 9 * (1 << 512)) for j in range(n)] for i in range(n)]
    for name, mat in (("Dh", dh), ("Khead", khead), ("Thead", thead)):
        need(all(mat[i][j] == mat[j][i] for i in range(n) for j in range(i, n)),
             "EXACT_SYMMETRY_" + name)
    return idx, d, g, dh, b0, khead, thead


def assembled_target(parity, centers, blocks, tick, emit):
    """Outward raw B0-congruence of exact T; all coefficients remain raw.

    Block-row sums reduce K3*[B0;B0-I;B0] to THREE n-by-n products.
    The third Y coefficient is zero in H; YY still belongs to cross energy.
    """
    idx, d, g, dh, b0, khead, thead = old_head_and_covariance(parity, centers, tick)
    n = len(idx)
    sector = "even" if parity == 0 else "odd"
    biv = [[point(x) for x in row] for row in b0]
    names = (("DH", "FX", "FY"), ("XF", "CX", "XY"), ("YF", "YX", "YY"))

    def value(name, i, j):
        if name == "DH":
            return dh[i][j]
        if name in ("XF", "YF", "YX"):
            other = {"XF": "FX", "YF": "FY", "YX": "XY"}[name]
            return F(blocks[other][idx[j]][idx[i]], 1 << RAW)
        return F(blocks[name][idx[i]][idx[j]], 1 << RAW)

    k = []
    for r in range(3):
        rr = []
        for s in range(3):
            rr.append([[point(value(names[r][s], i, j) +
                        (ETA * d[i] if r == s and i == j else F(0)))
                        for j in range(n)] for i in range(n)])
        k.append(rr)
        tick("joint-raw-block-initialize", sector=sector, blockrow=r)
    h = [[ZERO] * (2 * n) for _ in range(2 * n)]
    dinv = point(1 / DLOW)
    for r in range(2):
        for s in range(2):
            for i in range(n):
                for j in range(n):
                    v = mul(k[r][s][i][j], dinv)
                    if r == s == 0 and i == j:
                        v = add(v, point(CINV * d[i]))
                    if r == s == 1:
                        v = add(v, point(F(g[i][j], 1 << 257) +
                                        ((1 + EPS) * d[i] if i == j else F(0))))
                    h[r * n + i][s * n + j] = v
                tick("active-raw-H-initialize", sector=sector, blockrow=r, row=i)
    symmetrize(h)
    status, ell, pivots, failed = interval_ldl(h, tick, emit, "active-H-LDL", sector)
    if status != "ALL_POSITIVE":
        return None, dict(status="ACTIVE_SOLVE_UNRESOLVED", activeStatus=status,
                          failedPivot=failed, sector=sector)
    u = []
    for r in range(3):
        rowsum = [[add(add(k[r][0][i][j], k[r][1][i][j]), k[r][2][i][j])
                   for j in range(n)] for i in range(n)]
        prod = iv_product(rowsum, biv, tick, "joint-row-times-B0")
        u.append([[sub(prod[i][j], k[r][1][i][j]) for j in range(n)] for i in range(n)])
    v = u[0] + u[1]
    solution = interval_solve(ell, pivots, v, tick, sector)
    correction = iv_product(transpose(v), solution, tick, "active-quadratic-energy")
    sumu = [[add(add(u[0][i][j], u[1][i][j]), u[2][i][j]) for j in range(n)] for i in range(n)]
    first = iv_product(transpose(biv), sumu, tick, "L-adjoint-K-L")
    dinv2 = point(1 / (DLOW * DLOW))
    target = []
    for i in range(n):
        row = []
        for j in range(n):
            energy = sub(mul(sub(first[i][j], u[1][i][j]), dinv),
                         mul(correction[i][j], dinv2))
            row.append(sub(point(khead[i][j] - FEE * thead[i][j]), energy))
        target.append(row)
        tick("whole-target-raw-assembly", sector=sector, row=i)
    symmetrize(target)
    # Width/2 bounds any entry's distance from the mathematical midpoint.
    # In native coordinates ||S^-1||<2 and Dmin>=min(d): transport costs<4/Dmin.
    # The EXACT T already subtracts zeta once. This extra finite-width predicate
    # certifies actual arithmetic and is never added again as another fee.
    maxwidth = max(sum(b - a for a, b in row) for row in target)
    error = F(2 * maxwidth, UNIT) / min(d)
    need(error <= F(1, 1 << 216), "FINITE_NATIVE_ZETA216_UNPAID")
    return target, dict(status="TARGET_ASSEMBLED_WITH_FINITE_ERROR_CERTIFIED",
        sector=sector, activePositivePivots=len(pivots),
        nativeArithmeticErrorBound=[str(error.numerator), str(error.denominator)],
        rawMaxRowWidth=str(maxwidth), endpointBits=P, originalMetricDMin=str(min(d)),
        inverseNormTransportStrictUpper=2, targetContainsZetaExactlyOnce=True)


def packet_expected():
    for name in ("CX", "FX", "FY", "XY", "YY"):
        for parity in (0, 1):
            idx = list(range(parity, N, 2))
            for i in idx:
                for j in (range(i, N, 2) if name in ("CX", "YY") else idx):
                    yield name, i, j


def read_shared_packet(path, pin, tick):
    need(path.stat().st_size == pin["bytes"] <= 40185600, "PACKET_BYTES")
    blocks = {k: [[0] * N for _ in range(N)] for k in ("CX", "FX", "FY", "XY", "YY")}
    h, rows, size = hashlib.sha256(), 0, 0
    with path.open("rb") as f:
        for name, i, j in packet_expected():
            raw = f.readline(101)
            need(raw and raw.endswith(b"\n") and len(raw) < 100, "PACKET_LINE_BYTES")
            row = decode(raw)
            need(type(row) is list and len(row) == 4 and row[:3] == [name, i, j]
                 and type(row[0]) is str and type(row[1]) is int and type(row[2]) is int,
                 "PACKET_ORDER")
            z = integer(row[3])
            need(abs(z).bit_length() <= 262, "PACKET_CENTER_WIDTH")
            need(raw == (json.dumps(row, ensure_ascii=True, separators=(",", ":")) + "\n").encode("ascii"),
                 "PACKET_NOT_CANONICAL_COMPACT_JSONL")
            blocks[name][i][j] = z
            if name in ("CX", "YY"):
                blocks[name][j][i] = z
            h.update(raw)
            size += len(raw)
            rows += 1
            if rows % 1024 == 0:
                tick("shared-packet-read-only", rows=rows, bytes=size)
        need(f.read(1) == b"", "PACKET_EXTRA_ROWS")
    need(rows == 401856 and h.hexdigest() == pin["sha256"] and size == pin["bytes"], "PACKET_SHA_ROWS")
    return blocks


def file_hash(path, tick):
    h, size = hashlib.sha256(), 0
    with path.open("rb") as f:
        while raw := f.read(1 << 20):
            h.update(raw)
            size += len(raw)
            tick("pin-hash", path=path.name, bytes=size)
    return h.hexdigest(), size


def relative_path(name):
    p = (ROOT / name).resolve()
    need(p.is_relative_to(ROOT) and p.is_file(), "ROOT_INPUT_PATH")
    return p


def load_centers(tick):
    # All source byte pins are checked again at use, not just at a past preflight.
    for name, sha in SOURCE_PINS.items():
        observed, _ = file_hash(relative_path(name), tick)
        need(observed == sha, "SOURCE_PIN_CHANGED:" + name)
    raw = relative_path(MATRIX).read_bytes()
    need(digest(raw) == SOURCE_PINS[MATRIX], "MATRIX_CHANGED_AT_PARSE")
    packet = decode(raw)["packet"]
    p = packet["parameters"]
    need(p["N"] == N and p["L"] == "9/8" and p["omega"] == 256
         and p["outputBits"] == 256 and p["beta"] == "7/2", "OLD_PARAMETERS")
    need(packet["sourceConventions"]["J0"] == "L_squared_H"
         and packet["sourceConventions"]["orderedPrimePairs"] == 225, "OLD_SOURCE_CONVENTIONS")
    mats = {}
    for name in ("A", "B", "J0"):
        rows = packet["matrices"][name]
        need(len(rows) == 50400, "OLD_MATRIX_ROWS")
        mat, pos = [[0] * N for _ in range(N)], 0
        for i in range(N):
            for j in range(i, N, 2):
                row = rows[pos]
                need(type(row) is list and len(row) == 4 and row[:2] == [i, j], "OLD_MATRIX_ORDER")
                lo, hi = integer(row[2]), integer(row[3])
                need(lo <= hi, "OLD_MATRIX_ENDPOINTS")
                mat[i][j] = mat[j][i] = checked(lo + hi)
                pos += 1
            tick("old-point-centers", matrix=name, row=i)
        mats[name] = mat
    del raw, packet
    raw = relative_path(TAIL).read_bytes()
    need(digest(raw) == SOURCE_PINS[TAIL], "TAIL_CHANGED_AT_PARSE")
    tail = decode(raw)["packet"]
    tp = tail["parameters"]
    need(tp["dimension"] == N and tp["omega"] == 256 and tp["LNumerator"] == 9
         and tp["LDenominator"] == 8 and tp["outputBits"] == 640, "OLD_HEAD_H_PARAMETERS")
    need(len(tail["entries"]) == 896, "OLD_HEAD_H_ROWS")
    h = [[0] * N for _ in range(2)]
    for k, row in enumerate(tail["entries"]):
        s, i = divmod(k, N)
        need(row["column"] == s and row["index"] == i, "OLD_HEAD_H_ORDER")
        lo, hi, mid = (integer(row[x]) for x in ("lo", "hi", "midTwice"))
        need(lo <= hi and mid == lo + hi and (i % 2 == s or (lo, hi, mid) == (0, 0, 0)),
             "OLD_HEAD_H_PARITY_CENTER")
        h[s][i] = mid
        tick("old-head-h-point-centers", row=k)
    g, hh, count, size, heads = [[0] * N for _ in range(N)], hashlib.sha256(), 0, 0, 0
    with relative_path(GCOLS).open("rb") as f:
        for j in range(N):
            for i in range(j % 2, 2047, 2):
                raw = f.readline(65537)
                need(raw and raw.endswith(b"\n") and len(raw) <= 65536, "OLD_V_LINE")
                hh.update(raw)
                size += len(raw)
                count += 1
                row = decode(raw)
                need(type(row) is list and len(row) == 4 and row[:2] == [j, i], "OLD_V_FULL_ORDER")
                lo, hi = integer(row[2]), integer(row[3])
                need(lo <= hi, "OLD_V_ENDPOINTS")
                if i < N:
                    mid = checked(lo + hi)
                    if i < j:
                        need(g[i][j] == mid, "OLD_G_HEAD_CENTER_SYMMETRY")
                    g[j][i] = mid
                    heads += 1
                if count % 1024 == 0:
                    tick("old-G-from-SAME-V-stream", rows=count)
        need(f.read(1) == b"", "OLD_V_EXTRA")
    need(count == 458528 and heads == 100352 and size == 73598411
         and hh.hexdigest() == SOURCE_PINS[GCOLS], "OLD_V_COMPLETE_SHA_SHAPE")
    return mats["A"], mats["B"], mats["J0"], h, g


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

def validate_inventory(rows, kind):
    need(type(rows) is list and 0 <= len(rows) <= 256, "PRIOR_INVENTORY_" + kind)
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
    need(freeze["schema"]=="RH_WEIL_GLOBAL_FINITE_FREEZE_V1"
         and freeze["authorization"]=="ROOT_EXPLICIT_C069_GLOBAL_FINITE_EXECUTION"
         and freeze["numericalExecutionAuthorized"] is True,"MINIMAL_NEW_ROOT_AUTHORIZATION")
    for k,v in (("runtimeGoalCreatedAt",1793085111),("contractId","C069"),
                ("targetId",TARGET),("currentStage","stage-02-finite")):
        need(freeze[k]==v,"MINIMAL_REPLAY_SCOPE_"+k)
    cp,code=read_pin(freeze["codePin"])
    need(cp==SELF and digest(code)==freeze["selfSHA256"],"MINIMAL_REPLAY_SELF")
    contractpath,contractraw=read_pin(freeze["contractPin"])
    need(contractpath==ROOT/"goals/contracts/C069-global-exact-directional-whole.md"
         and b"C069" in contractraw,"MINIMAL_ACTUAL_NEW_CONTRACT")
    gp,gr=read_pin(freeze["rootGatePin"]);gate=decode(gr)
    need(gate["schema"]=="RH_WEIL_GLOBAL_FINITE_ROOT_GATE_V1"
         and gate["authorization"]=="ROOT_EXPLICIT_C069_GLOBAL_FINITE_EXECUTION"
         and gate["numericalExecutionAuthorized"] is True,"MINIMAL_ROOT_GATE")
    for k in ("runtimeGoalCreatedAt","contractId","targetId","currentStage","codePin","selfSHA256",
              "externalAttemptPin","launchNonce","preflightConsumesThisAttempt","contractPin",
              "wholeRunLockPin","rootAdmissionNonce"):
        need(gate[k]==freeze[k],"MINIMAL_GATE_MISMATCH_"+k)
    need(freeze["preflightConsumesThisAttempt"] is True
         and type(freeze["launchNonce"]) is str and 0<len(freeze["launchNonce"])<=128,
         "EXPLICIT_CONSUMED_PREFLIGHT_NONCE")
    ap,ar=read_pin(freeze["externalAttemptPin"]);attempt=decode(ar)
    need(attempt["schema"]=="RH_WEIL_GLOBAL_FINITE_PRODUCER_ROOT_ATTEMPT_V1"
         and attempt["status"]=="ROOT_CLAIMED_ONE_GLOBAL_FINITE_PRODUCER","ACTUAL_ROOT_ONCE_CLAIM")
    for k in ("runtimeGoalCreatedAt","contractId","targetId","currentStage","codePin","launchNonce"):
        need(attempt[k]==freeze[k],"ROOT_ATTEMPT_SCOPE_"+k)
    need(freeze["budget"]["reservedRemainingFiniteBytes"]>262144,"MINIMAL_TERMINAL_RESERVE")
    need(OUTER.is_dir() and not OUT.exists(),"REPLAY_STAGE_ALREADY_CLAIMED")
    OUT.mkdir(exist_ok=False)
    claim=dict(schema="RH_WEIL_GLOBAL_FINITE_ATTEMPT_V1",phase="CLAIMED_BEFORE_FULL_PREFLIGHT",
        terminal=False,pid=os.getpid(),freezeSHA256=digest(raw),rootGatePin=freeze["rootGatePin"],
        externalAttemptPin=freeze["externalAttemptPin"],launchNonce=freeze["launchNonce"],
        targetId=TARGET,contractId="C069",runtimeGoalCreatedAt=1793085111)
    claimraw=packed(claim);need(len(claimraw)<16384,"BOUNDED_ONCE_CLAIM")
    with (OUT/"attempt.json").open("xb") as f:
        f.write(claimraw);f.flush();os.fsync(f.fileno())
    return claim,claimraw

def validate_freeze(path, claim, claimraw):
    """Metadata only; source numerical parsing occurs solely after admission."""
    need(path.is_file() and path.stat().st_size <= (2 << 20), "BOUNDED_FREEZE_FILE")
    raw = path.read_bytes()
    need(digest(raw)==claim["freezeSHA256"] and (OUT/"attempt.json").read_bytes()==claimraw,
         "CLAIM_OR_FREEZE_CHANGED")
    freeze = decode(raw)
    need(freeze["schema"] == "RH_WEIL_GLOBAL_FINITE_FREEZE_V1"
         and freeze["authorization"] == "ROOT_EXPLICIT_C069_GLOBAL_FINITE_EXECUTION"
         and freeze["numericalExecutionAuthorized"] is True, "NEW_ROOT_FINITE_AUTHORIZATION_REQUIRED")
    for k, v in (("runtimeGoalCreatedAt", 1793085111), ("contractId", "C069"),
                 ("targetId", TARGET), ("currentStage", "stage-02-finite")):
        need(freeze[k] == v, "FREEZE_SCOPE_" + k)
    need(freeze["parameters"] == PARAMETERS and freeze["sourceMathPins"] == SOURCE_PINS,
         "FREEZE_FIXED_PARAMETERS_OR_SOURCE")
    codepath, code = read_pin(freeze["codePin"])
    need(codepath == SELF and freeze["selfSHA256"] == digest(code), "EXACT_FINAL_SELF_CODE")
    contractpath, contractraw = read_pin(freeze["contractPin"])
    need(contractpath == ROOT / "goals/contracts/C069-global-exact-directional-whole.md"
         and b"C069" in contractraw, "ACTUAL_NEW_CONTRACT")
    gatepath, gateraw = read_pin(freeze["rootGatePin"])
    gate = decode(gateraw)
    need(gate["schema"] == "RH_WEIL_GLOBAL_FINITE_ROOT_GATE_V1"
         and gate["authorization"] == "ROOT_EXPLICIT_C069_GLOBAL_FINITE_EXECUTION"
         and gate["numericalExecutionAuthorized"] is True, "DISTINCT_ROOT_STAGE_GATE")
    for k in ("runtimeGoalCreatedAt", "contractId", "targetId", "currentStage", "parameters",
              "sourceMathPins", "codePin", "selfSHA256", "contractPin", "sourceRootAcceptancePin",
              "sharedpacketPin", "reviewPins", "reviewOwners", "reviewKinds", "budget", "finiteCheckerPin",
              "chargedMetadataPins","rootPriorAccountingPin","wholeRunLockPin","rootAdmissionNonce",
              "externalAttemptPin","launchNonce","preflightConsumesThisAttempt","externalRuntimePaths"):
        need(gate[k] == freeze[k], "ROOT_GATE_FREEZE_MISMATCH_" + k)
    need(gate["sameRuntimeGoalLiveAndActiveChecked"] is True
         and gate["sourceTerminalAndNoLiveProcessChecked"] is True
         and gate["sameResponsibilityNoReset"] is True
         and gate["finalMathematicalAndProtocolReviewsRootConsumed"] is True,
         "ROOT_LIVE_SOURCE_AND_ONCE_PREMISES")
    need(len(freeze["reviewPins"]) >= 2, "DISTINCT_FINAL_REVIEWS")
    owners = freeze["reviewOwners"]
    kinds=freeze["reviewKinds"]
    need(type(owners) is list and len(owners) == len(freeze["reviewPins"])
         and all(type(s) is str and 0 < len(s) <= 256 for s in owners)
         and len(set(owners)) == len(owners), "DISTINCT_FINAL_REVIEW_OWNERS")
    need(type(kinds) is list and len(kinds)==len(owners) and set(kinds)>={"math","protocol"},
         "FINAL_MATH_AND_PROTOCOL_REVIEWS")
    reviewpaths = set()
    for review, owner in zip(freeze["reviewPins"], owners):
        rp, rr = read_pin(review)
        reviewpaths.add(rp)
        need(digest(code).encode() in rr and owner.encode() in rr,
             "REVIEW_DOES_NOT_BIND_FINAL_CODE_AND_OWNER")
    need(len(reviewpaths) >= 2, "DISTINCT_REVIEW_FILES")
    # An actual separately reviewed independent executable is mandatory; this
    # consumer neither executes it nor treats its file hash as its future PASS.
    checkpath, _ = read_pin(freeze["finiteCheckerPin"])
    need(checkpath != SELF and checkpath.suffix == ".py", "INDEPENDENT_FINITE_CHECKER_MISSING")
    ap, ar = read_pin(freeze["sourceRootAcceptancePin"])
    acceptance = decode(ar)
    need(acceptance["schema"] == "RH_WEIL_GLOBAL_SOURCE_ROOT_ACCEPTANCE_V1"
         and acceptance["status"] == "ROOT_CONSUMED_FIVE_BLOCK_ENDPOINT230_CERTIFICATES"
         and acceptance["runtimeGoalCreatedAt"] == 1793085111
         and acceptance["targetId"] == TARGET, "ACTUAL_SOURCE_ENDPOINT230_ACCEPTANCE_REQUIRED")
    need(acceptance["fullNativeArithmeticPower"] == -230
         and acceptance["blocks"] == ["CX", "FX", "FY", "XY", "YY"]
         and acceptance["packetRows"] == 401856
         and acceptance["sharedpacketPin"] == freeze["sharedpacketPin"]
         and acceptance["independentScientificVerificationPassed"] is True
         and acceptance["bothHermitianTrianglesCharged"] is True
         and acceptance["CXInfiniteOffdiagonalTailIncluded"] is True,
         "ROOT_SOURCE_MODEL_OR_COVERAGE_UNCLOSED")
    need(len(acceptance["sourceVerificationPins"]) >= 2, "SOURCE_RESULT_AND_INDEPENDENT_CHECKER_REQUIRED")
    for p in acceptance["sourceVerificationPins"]:
        read_pin(p)
    pp = freeze["sharedpacketPin"]
    need(set(pp) == {"path", "bytes", "sha256"}, "SHARED_PACKET_PIN_SCHEMA")
    packetpath = relative_path(pp["path"])
    need(packetpath.is_relative_to(OUTER / "stage-01-source")
         and packetpath.stat().st_size == pp["bytes"] <= 40185600, "ONE_SHARED_SOURCE_PACKET")
    budget = freeze["budget"]
    need(budget["aggregateCapSeconds"] == 7200 and budget["aggregateCapBytes"] == 67108864
         and budget["finiteCapSeconds"] == 3600 and budget["finiteCapBytes"] == 16777216,
         "FIXED_WHOLE_AND_FINITE_CAPS")
    for key in ("sourceConsumedUpperSeconds", "finitePriorUpperSeconds", "producerDeadlineSeconds",
                "reservedVerifierTerminalSeconds", "sourceConsumedOutputBytes", "finitePriorOutputBytes"):
        need(type(budget[key]) in (int, float) and budget[key] >= 0, "BUDGET_NONNEGATIVE_" + key)
    for key in ("sourceConsumedOutputBytes", "finitePriorOutputBytes", "reservedRemainingFiniteBytes"):
        need(type(budget[key]) is int and budget[key] >= 0, "BUDGET_INTEGER_BYTES_" + key)
    need(budget["sourceConsumedUpperSeconds"] <= 3600
         and budget["sourceConsumedOutputBytes"] <= 50331648, "SOURCE_STAGE_CAP_NOT_REUSABLE")
    need(budget["reservedVerifierTerminalSeconds"] > 0 and budget["producerDeadlineSeconds"] > 0,
         "MISSING_FINITE_VERIFIER_TERMINAL_RESERVE")
    need(budget["producerDeadlineSeconds"] + budget["reservedVerifierTerminalSeconds"]
         + budget["finitePriorUpperSeconds"] <= 3600, "FINITE_PRODUCER_NO_CHECKER_TIME")
    need(budget["sourceConsumedUpperSeconds"] + budget["finitePriorUpperSeconds"]
         + budget["producerDeadlineSeconds"] + budget["reservedVerifierTerminalSeconds"] <= 7200,
         "AGGREGATE_TIME_DEPLETED")
    need(budget["finitePriorOutputBytes"] + budget["reservedRemainingFiniteBytes"] <= 16777216
         and budget["sourceConsumedOutputBytes"] + budget["finitePriorOutputBytes"]
         + budget["reservedRemainingFiniteBytes"] <= 67108864, "OUTPUT_RESERVE_NOT_FUNDED")
    need(OUT.is_dir() and {p.name for p in OUT.iterdir()}=={"attempt.json"},"FINITE_ONCE_OWNER_CHANGED")
    priorpath,priorraw=read_pin(freeze["rootPriorAccountingPin"]);prior=decode(priorraw)
    need(prior["schema"]=="RH_WEIL_GLOBAL_FINITE_PRODUCER_PRIOR_ROOT_ACCOUNTING_V1"
         and prior["status"]=="ROOT_VERIFIED_SOURCE_TERMINAL_AND_FINITE_PRIOR_ACCOUNTING",
         "ROOT_ACTUAL_PRIOR_ACCOUNTING_REQUIRED")
    for k,v in (("runtimeGoalCreatedAt",1793085111),("contractId","C069"),("targetId",TARGET)):
        need(prior[k]==v,"ACTUAL_PRIOR_SCOPE_"+k)
    need(prior["sourceRootAcceptancePin"]==freeze["sourceRootAcceptancePin"]
         and prior["sourceProcessObservedTerminal"] is True
         and prior["noLiveSourceOrFiniteProcess"] is True
         and prior["sourceScientificVerificationRootConsumed"] is True
         and prior["allScientificLifetimesSummedWithoutOverlapDiscount"] is True
         and prior["allNumericalCopiesMetadataTmpFailuresAccounted"] is True,
         "ACTUAL_PRIOR_SOURCE_PROCESS_AND_SCIENCE_UNCLOSED")
    for k in ("sourceConsumedUpperSeconds","finitePriorUpperSeconds",
              "sourceConsumedOutputBytes","finitePriorOutputBytes"):
        need(prior[k]==budget[k],"ACTUAL_PRIOR_COST_CHANGED_"+k)
    sourcepaths,sourcebytes=validate_inventory(prior["sourceOutputInventory"],"source")
    finitepaths,finitebytes=validate_inventory(prior["finiteOutputInventory"],"finite")
    need(sourcebytes<=budget["sourceConsumedOutputBytes"] and finitebytes<=budget["finitePriorOutputBytes"]
         and not set(sourcepaths)&set(finitepaths),"ACTUAL_PRIOR_OUTPUT_INVENTORY")
    need(prior["nonRetainedMonotonicChargesRootVerified"] is True,"PRIOR_NONRETAINED_CHARGES_UNVERIFIED")
    for kind,retained,paid in (("source",sourcebytes,budget["sourceConsumedOutputBytes"]),
                               ("finite",finitebytes,budget["finitePriorOutputBytes"])):
        authorities=prior["nonRetainedChargeAuthorityPins"][kind]
        need(type(authorities) is list and (paid==retained or len(authorities)>0),
             "NONRETAINED_CHARGE_AUTHORITY_MISSING_"+kind)
        for pin in authorities:read_pin(pin)
    need(type(budget["externalRuntimeChargedUpperBytes"]) is int
         and 0<=budget["externalRuntimeChargedUpperBytes"]<budget["reservedRemainingFiniteBytes"],
         "EXTERNAL_RUNTIME_MONOTONIC_RESERVE")
    baseline=dict(sourcepaths);baseline.update(finitepaths)
    need(packetpath in sourcepaths and sourcepaths[packetpath]==freeze["sharedpacketPin"],
         "SHARED_PACKET_NOT_IN_ACTUAL_SOURCE_COST")
    lockpath,lockraw=read_pin(freeze["wholeRunLockPin"]);lock=decode(lockraw)
    need(lockpath==(OUTER/"run-lock.json").resolve()
         and lock["schema"]=="RH_WEIL_GLOBAL_ONCE_OUTER_CLAIM_V1"
         and lock["runtimeGoalCreatedAt"]==1793085111 and lock["contractId"]=="C069"
         and lock["targetId"]==TARGET and lock["noRetry"] is True
         and lock["rootAdmissionNonce"]==freeze["rootAdmissionNonce"]
         and type(lock["producerPID"]) is int and lock["producerPID"]>0
         and type(lock["createdUTC"]) is str and 0<len(lock["createdUTC"])<=128
         and prior["wholeRunLockPin"]==freeze["wholeRunLockPin"]
         and lockpath in baseline and baseline[lockpath]==freeze["wholeRunLockPin"],
         "ACTUAL_WHOLE_ONCE_LOCK_SCOPE_AND_CHARGE")
    attemptpath,_=read_pin(freeze["externalAttemptPin"])
    external = {path.resolve(), gatepath, ap, contractpath, priorpath,attemptpath}
    external |= {relative_path(p["path"]) for p in freeze["chargedMetadataPins"]}
    for p in freeze["chargedMetadataPins"]:
        read_pin(p)
    external-=set(baseline)
    mutable=set()
    for name in freeze["externalRuntimePaths"]:
        need(type(name) is str,"EXTERNAL_RUNTIME_PATH")
        p=(ROOT/name).resolve()
        need(p.is_relative_to(ROOT) and not p.is_relative_to(OUT) and p not in baseline
             and p not in external and p!=packetpath and p!=SELF,"EXTERNAL_RUNTIME_PATH_OVERLAP")
        mutable.add(p)
    need(len(mutable)==len(freeze["externalRuntimePaths"]),"DUPLICATE_EXTERNAL_RUNTIME_PATH")
    existing={p.resolve() for p in OUTER.rglob("*") if p.is_file()}
    need(existing<=set(baseline)|external|mutable|{(OUT/"attempt.json").resolve()},
         "UNACCOUNTED_EXISTING_WHOLE_OUTPUT")
    need(all(not p.is_relative_to(OUT) for p in baseline),"FINITE_ALREADY_IN_PRIOR_INVENTORY")
    return freeze, packetpath, external, baseline, mutable


class Runtime:
    def __init__(self, freeze, external_paths, baseline, mutable):
        self.freeze = freeze
        self.limits = freeze["budget"]
        self.external = external_paths
        self.baseline = baseline
        self.mutable = mutable
        self.context = {}
        self.lastwrite = 0.0
        self.lastsize = 0.0
        self.started = PROCESS_STARTED
        self.log = None
        self.created = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())

    def bytes(self):
        own=sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
        if self.log is not None and not self.log.closed:
            # Buffered pivots already exist logically even before OS flush.
            own += max(0, self.log.tell() - Path(self.log.name).stat().st_size)
        external=sum(p.stat().st_size for p in self.external if p.is_file())
        mutable=sum(p.stat().st_size for p in self.mutable if p.is_file())
        need(mutable<=self.limits["externalRuntimeChargedUpperBytes"],"EXTERNAL_RUNTIME_RESERVE_EXCEEDED")
        return external+self.limits["externalRuntimeChargedUpperBytes"]+max(self.created,own)

    def charge(self,size,emergency=False):
        need(type(size) is int and size>=0,"MONOTONIC_WRITE_SIZE")
        # Denied allocation writes nothing; funded allocation is charged before
        # writing, and that charge is never refunded after an I/O failure.
        need(self.bytes()+size+(0 if emergency else 262144)<=self.limits["reservedRemainingFiniteBytes"],
             "MONOTONIC_FINITE_WRITE_CAP_STOP")
        self.created+=size

    def check(self):
        elapsed = time.monotonic() - self.started + 1.0
        need(elapsed <= self.limits["producerDeadlineSeconds"], "FINITE_PRODUCER_DEADLINE_STOP")
        if time.monotonic() - self.lastsize >= 0.5:
            current = self.bytes()
            need(current + 262144 <= self.limits["reservedRemainingFiniteBytes"], "FINITE_OUTPUT_CAP_STOP")
            need(current + self.limits["finitePriorOutputBytes"] + 262144 <= 16777216,
                 "FINITE_STAGE_CAP_STOP")
            need(current + self.limits["finitePriorOutputBytes"] + self.limits["sourceConsumedOutputBytes"]
                 + 262144 <= 67108864, "AGGREGATE_OUTPUT_CAP_STOP")
            allowed=set(self.baseline)|self.external|self.mutable
            need(all(p.resolve() in allowed or p.resolve().is_relative_to(OUT)
                     for p in OUTER.rglob("*") if p.is_file()),"UNACCOUNTED_CONCURRENT_WHOLE_OUTPUT")
            self.lastsize = time.monotonic()

    def atomic(self, name, obj, emergency=False):
        raw = packed(obj)
        need(len(raw) < 131072, "BOUNDED_FINITE_RECORD")
        if not emergency:
            self.check()
        self.charge(len(raw),emergency)
        temp = OUT / (name + ".tmp")
        with temp.open("wb") as f:
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, OUT / name)

    def tick(self, phase=None, **context):
        self.check()
        self.context = dict(phase=phase, **context)
        if time.monotonic() - self.lastwrite >= 3:
            if self.log is not None:
                self.log.flush()
            self.atomic("progress.json", dict(schema="RH_WEIL_GLOBAL_FINITE_PROGRESS_V1",
                status="RUNNING", terminal=False, targetId=TARGET, contractId="C069",
                monotonicOwnedBytesBeforeThisProgress=self.created,
                context=self.context, elapsedSecondsWithReserve=time.monotonic()-self.started+1))
            self.lastwrite = time.monotonic()


def preserve_claim_failure(claim,error,phase):
    result=dict(schema="RH_WEIL_GLOBAL_FINITE_RESULT_V1",status=phase,
        terminal=True,claim=claim,errorType=type(error).__name__,error=str(error)[:2048],
        mathematicalSignConclusion=False,noRetry=True,GoalComplete=False,
        elapsedSecondsIncludingReserve=time.monotonic()-PROCESS_STARTED+1)
    raw=packed(result);need(len(raw)<131072,"BOUNDED_CLAIMED_FAILURE_TERMINAL")
    with (OUT/"result.json").open("xb") as f:
        f.write(raw);f.flush();os.fsync(f.fileno())
    print(packed(dict(status=result["status"],result=(OUT/"result.json").relative_to(ROOT).as_posix(),
                     resultSHA256=digest(raw))).decode(),end="")
    return 2


def execute(freeze_path):
    sys.set_int_max_str_digits(20000)
    claim,claimraw=claim_attempt(freeze_path)
    try:
        freeze, packetpath, external, baseline, mutable = validate_freeze(freeze_path,claim,claimraw)
    except Exception as error:
        return preserve_claim_failure(claim,error,"PREFLIGHT_TECHNICAL_STOP_AFTER_ONCE_CLAIM")
    runtime = Runtime(freeze, external, baseline, mutable)
    logpath = OUT / "pivots.jsonl.part"
    try:
        runtime.atomic("admission.json", dict(schema="RH_WEIL_GLOBAL_FINITE_ADMISSION_V1",
            freezeSHA256=digest(freeze_path.read_bytes()), pid=os.getpid(),
            targetId=TARGET, runtimeGoalCreatedAt=1793085111, parameters=PARAMETERS))
        log = logpath.open("xb")
        runtime.log = log
    except Exception as error:
        return preserve_claim_failure(claim,error,"CONTROLLED_STARTUP_STOP_AFTER_ONCE_CLAIM")
    h, count, logsize = hashlib.sha256(), 0, 0

    def emit(obj):
        nonlocal count, logsize
        raw = packed(obj)
        need(len(raw) < 4096, "FINITE_PIVOT_RECORD_WIDTH")
        runtime.check()
        runtime.charge(len(raw))
        log.write(raw)
        h.update(raw)
        count += 1
        logsize += len(raw)

    result = None
    try:
        centers = load_centers(runtime.tick)
        blocks = read_shared_packet(packetpath, freeze["sharedpacketPin"], runtime.tick)
        sectors = []
        outcome = "WHOLE_POINT_POSITIVE_PENDING_INDEPENDENT_CHECKER_AND_ROOT"
        for parity in (0, 1):
            target, rec = assembled_target(parity, centers, blocks, runtime.tick, emit)
            if target is None:
                sectors.append(rec)
                outcome = "FINITE_TECHNICAL_UNRESOLVED"
                break
            status, _, _, pivot = interval_ldl(target, runtime.tick, emit, "whole-T-LDL", rec["sector"])
            rec.update(wholeStatus=status, finalPivot=pivot)
            sectors.append(rec)
            if status != "ALL_POSITIVE":
                outcome = ("SUFFICIENT_WHOLE_FLOOR_REJECTED_PENDING_INDEPENDENT_CHECKER_AND_ROOT"
                           if status == "STRICT_NEGATIVE_PIVOT" else "FINITE_TECHNICAL_UNRESOLVED")
                break
        result = dict(schema="RH_WEIL_GLOBAL_FINITE_RESULT_V1", status=outcome,
            contractId="C069", targetId=TARGET, runtimeGoalCreatedAt=1793085111,
            codeSHA256=digest(SELF.read_bytes()), parameters=PARAMETERS,
            sourceMathPins=SOURCE_PINS, sharedpacketPin=freeze["sharedpacketPin"],
            sourceRootAcceptancePin=freeze["sourceRootAcceptancePin"], sectors=sectors,
            sourceBetaPower=-224, coefficientNuPower=-216, finiteZetaPower=-216,
            targetFeeMultiplicity=dict(beta=1, nu=1, zeta=1, alpha=0),
            originalPhysicalNorm="f-du; r=exp(u/2)f with exp(-u)du; Djj=9/[4(2j+1)]",
            scope="ONLY exact fixed9/8 sufficient whole floor; positive needs independent finite checker/root, negative is NOT actualLret/Q negative",
            wholePositiveClaim=False, negativeActualLretClaim=False,
            negativeActualQClaim=False, GoalComplete=False, mathematicalSettlement="PENDING_ROOT")
    except Exception as error:
        result = dict(schema="RH_WEIL_GLOBAL_FINITE_RESULT_V1", status="FINITE_TECHNICAL_STOP",
            errorType=type(error).__name__, error=str(error)[:2048], context=runtime.context,
            targetId=TARGET, contractId="C069", codeSHA256=digest(SELF.read_bytes()),
            mathematicalSignConclusion=False, noRetry=True, GoalComplete=False)
        if isinstance(error, IntegerWidthError):
            result["integerWidthDiagnostic"] = width_diagnostic(error)
    finally:
        log.flush()
        os.fsync(log.fileno())
        log.close()
        runtime.log = None
        os.replace(logpath, OUT / "pivots.jsonl")
    result["pivotLog"] = dict(path="pivots.jsonl", sha256=h.hexdigest(), rows=count,
                               bytes=logsize, closed=True)
    result["elapsedSecondsIncludingReserve"] = time.monotonic() - runtime.started + 1
    result["producerStageOutputBytesBeforeResult"] = runtime.bytes()
    result["monotonicOwnedBytesBeforeResult"] = runtime.created
    result["externalRuntimeChargedUpperBytes"] = runtime.limits["externalRuntimeChargedUpperBytes"]
    runtime.atomic("result.json", result, emergency=True)
    # Emergency terminal bytes must also fit, or terminal accounting is a STOP.
    need(runtime.bytes() <= runtime.limits["reservedRemainingFiniteBytes"], "FINITE_TERMINAL_BYTES_STOP")
    print(packed(dict(status=result["status"], result=str((OUT/"result.json").relative_to(ROOT)),
                      finalMonotonicChargedUpperBytes=runtime.bytes(),
                      resultSHA256=digest((OUT/"result.json").read_bytes()))).decode(), end="")
    return 0 if result["status"].endswith("PENDING_INDEPENDENT_CHECKER_AND_ROOT") else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-freeze-file", type=Path, required=True)
    args = parser.parse_args()
    sys.set_int_max_str_digits(20000)
    return execute(args.root_freeze_file.resolve())


if __name__ == "__main__":
    raise SystemExit(main())

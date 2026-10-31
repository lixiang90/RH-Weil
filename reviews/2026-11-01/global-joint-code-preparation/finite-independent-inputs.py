"""Independent original-input adapter; CODE PREPARATION ONLY.

No consumer/source-producer imports. Future authenticated checker controller must
bind this code and root-accepted shared packet before invoking these functions.
No actual file is read by import/main; current preparation uses text/AST only.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

N = 448
DEGREE = 2046
OLD = "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/"
MATRIX = OLD + "source-matrices.json"
TAIL = OLD + "tail-columns.json"
V = "literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl"
PINS = {MATRIX: "a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
        TAIL: "d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
        V: "d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080"}
DECIMAL = re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)\Z", re.ASCII)


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def unique(pairs):
    result = {}
    for k, v in pairs:
        need(k not in result, "DUPLICATE_JSON_KEY")
        result[k] = v
    return result


def number(x, limit=16384):
    need(type(x) is str and DECIMAL.fullmatch(x) is not None, "INTEGER_ENCODING")
    need(len(x) <= 5000, "INTEGER_DECIMAL_LENGTH")
    v = int(x)
    need(abs(v).bit_length() <= limit, "INTEGER_WIDTH")
    return v


def bounded(v):
    need(type(v) is int and abs(v).bit_length() <= 16384, "NORMAL_INTEGER_WIDTH")
    return v


def json_record(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=unique)


def read_pinned(root, relative, poll):
    path = Path(root) / relative
    need(path.resolve().is_relative_to(Path(root).resolve()), "PATH_OUTSIDE_ROOT")
    h = hashlib.sha256()
    chunks = []
    with path.open("rb") as stream:
        while True:
            poll()
            b = stream.read(1 << 20)
            if not b:
                break
            h.update(b)
            chunks.append(b)
    need(h.hexdigest() == PINS[relative], "SOURCE_HASH_CHANGED")
    return json_record(b"".join(chunks))


def load_old_centers(root, *, poll):
    """Read-only three original files. Gate/controller remains externally required."""
    obj = read_pinned(root, MATRIX, poll)["packet"]
    p = obj["parameters"]
    need(p["N"] == N and p["L"] == "9/8" and p["omega"] == 256
         and p["beta"] == "7/2" and p["outputBits"] == 256, "SOURCE_PARAMETERS")
    need(obj["sourceConventions"]["J0"] == "L_squared_H"
         and obj["sourceConventions"]["orderedPrimePairs"] == 225, "SOURCE_CONVENTIONS")
    matrices = {}
    for name in ("A", "B", "J0"):
        rows = obj["matrices"][name]
        need(len(rows) == 50400, "OLD_MATRIX_COUNT")
        a = [[0] * N for _ in range(N)]
        pos = 0
        for i in range(N):
            poll()
            for j in range(i, N, 2):
                row = rows[pos]
                need(type(row) is list and len(row) == 4 and type(row[0]) is int
                     and type(row[1]) is int and row[:2] == [i, j], "OLD_MATRIX_ORDER")
                lo, hi = number(row[2]), number(row[3])
                need(lo <= hi, "OLD_ENDPOINT_ORDER")
                a[i][j] = a[j][i] = bounded(lo + hi)
                pos += 1
        matrices[name] = a
    tail = read_pinned(root, TAIL, poll)["packet"]
    p = tail["parameters"]
    need(p["dimension"] == N and p["omega"] == 256 and p["LNumerator"] == 9
         and p["LDenominator"] == 8 and p["outputBits"] == 640, "OLD_H_PARAMETERS")
    need(len(tail["entries"]) == 2*N, "OLD_H_COUNT")
    h = [[0] * N for _ in range(2)]
    for pos, row in enumerate(tail["entries"]):
        s, j = divmod(pos, N)
        need(type(row["column"]) is int and type(row["index"]) is int
             and row["column"] == s and row["index"] == j, "OLD_H_ORDER")
        lo, hi, mid = [number(row[k]) for k in ("lo", "hi", "midTwice")]
        need(lo <= hi and mid == bounded(lo + hi), "OLD_H_CENTER")
        need(j % 2 == s or (lo, hi, mid) == (0, 0, 0), "OLD_H_PARITY")
        h[s][j] = mid
    g = [[0] * N for _ in range(N)]
    seen = [[False] * N for _ in range(N)]
    digest = hashlib.sha256()
    count = headcount = size = 0
    with (Path(root) / V).open("rb") as stream:
        for j in range(N):
            for i in range(j % 2, DEGREE + 1, 2):
                if count % 256 == 0:
                    poll()
                raw = stream.readline(65537)
                need(0 < len(raw) <= 65536 and raw.endswith(b"\n"), "V_LINE_BYTES")
                digest.update(raw)
                size += len(raw)
                row = json_record(raw)
                need(type(row) is list and len(row) == 4 and type(row[0]) is int
                     and type(row[1]) is int and row[:2] == [j, i], "V_ORDER")
                lo, hi = number(row[2]), number(row[3])
                need(lo <= hi, "V_ENDPOINT_ORDER")
                if i < N:
                    mid = bounded(lo + hi)
                    if seen[i][j]:
                        need(g[i][j] == mid, "G_CENTER_SYMMETRY")
                    g[j][i] = mid
                    seen[j][i] = True
                    headcount += 1
                count += 1
        need(stream.read(1) == b"", "V_EXTRA")
    need(count == 458528 and headcount == 100352 and size == 73598411
         and digest.hexdigest() == PINS[V], "V_FULL_SOURCE_BINDING")
    return matrices, h, g


def sector_forms(centers, parity, *, poll):
    """Exact point forms from original midpoint integers, no rounded-head reuse."""
    need(type(parity) is int and parity in (0, 1), "PARITY")
    mats, h, gs = centers
    ids = list(range(parity, N, 2))
    d = [F(9, 4*(2*j+1)) for j in ids]
    g = [[F(gs[i][j], 1 << 257) for j in ids] for i in ids]
    c0, dh = [], []
    aa, bb, jj = mats["A"], mats["B"], mats["J0"]
    for i in ids:
        poll()
        cr, dr = [], []
        for j in ids:
            hprod = bounded(bounded(h[0][i]*h[0][j]) + bounded(h[1][i]*h[1][j]))
            first = bounded(bounded(aa[i][j] + jj[i][j]) << 1025)
            cr.append(F(bounded(first + bounded(36*hprod)), 1 << 1282))
            q = bounded(bounded(9*bb[i][j]) << 255)
            for k in ids:
                term = bounded(bounded(aa[i][k] * (2*k+1)) * aa[k][j])
                q = bounded(q - term)
            dr.append(F(q, 9*(1 << 512)))
        c0.append(cr)
        dh.append(dr)
    return d, g, dh, c0


def load_packet(path, pin, *, poll):
    """Independent strict original packet reader; one read-only packet, no copy."""
    need(type(pin) is dict and set(pin) == {"sha256", "bytes"}, "PACKET_PIN_FIELDS")
    result = {p: {} for p in (0, 1)}
    h = hashlib.sha256()
    count = size = 0
    with Path(path).open("rb") as stream:
        for block in ("CX", "FX", "FY", "XY", "YY"):
            for parity in (0, 1):
                m = N // 2
                a = [[F(0)]*m for _ in range(m)]
                for i in range(parity, N, 2):
                    poll()
                    for j in range(i if block in ("CX", "YY") else parity, N, 2):
                        raw = stream.readline(100)
                        need(0 < len(raw) < 100 and raw.endswith(b"\n"), "PACKET_RECORD_BYTES")
                        row = json_record(raw)
                        need(type(row) is list and len(row) == 4 and type(row[1]) is int
                             and type(row[2]) is int and row[:3] == [block, i, j], "PACKET_ORDER")
                        center = number(row[3], 262)
                        canonical = (json.dumps(row, separators=(",", ":"), ensure_ascii=True)+"\n").encode("ascii")
                        need(raw == canonical, "PACKET_NONCANONICAL")
                        a[i//2][j//2] = F(center, 1 << 256)
                        if block in ("CX", "YY"):
                            a[j//2][i//2] = a[i//2][j//2]
                        h.update(raw)
                        size += len(raw)
                        count += 1
                result[parity][block] = a
        need(stream.read(1) == b"", "PACKET_EXTRA")
    need(count == 401856 and size == pin["bytes"] and h.hexdigest() == pin["sha256"], "PACKET_BINDING")
    return result


if __name__ == "__main__":
    raise SystemExit("CODE_PREPARATION_ONLY: no authenticated checker controller/actual input access")

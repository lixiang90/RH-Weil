"""Canonical packet syntax only. This module proves NO source value or sign.

Current CLI permits synthetic controls only; actual packet use requires the future
root-gated scientific source/verifier/consumer, not this preparation module.
"""
import argparse
import hashlib
import io
import json
import re

BLOCKS = ("CX", "FX", "FY", "XY", "YY")
INTEGER = re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)\Z", re.ASCII)
N = 448
ROWS = 401856
MAX_RECORD = 99  # strict <100, including LF
MAX_BITS = 262


def need(condition, message):
    if not condition:
        raise ValueError(message)


def expected(n=N):
    need(type(n) is int and 0 < n <= N and n % 2 == 0, "DIMENSION")
    for block in BLOCKS:
        for parity in (0, 1):
            for i in range(parity, n, 2):
                start = i if block in ("CX", "YY") else parity
                for j in range(start, n, 2):
                    yield block, i, j


def encode(row):
    return (json.dumps(row, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def validate(stream, n=N, hook=lambda: None):
    """Stream strict syntax/order/count; does not certify a Gram or its error."""
    digest = hashlib.sha256()
    size = count = 0
    block_counts = dict.fromkeys(BLOCKS, 0)
    for block, i, j in expected(n):
        hook()
        raw = stream.readline(MAX_RECORD + 1)
        need(0 < len(raw) <= MAX_RECORD and raw.endswith(b"\n"), "RECORD_BYTES_OR_EOF")
        try:
            row = json.loads(raw.decode("ascii"))
        except (UnicodeError, ValueError) as error:
            raise ValueError("RECORD_JSON") from error
        need(type(row) is list and len(row) == 4, "RECORD_SHAPE")
        need(type(row[0]) is str and type(row[1]) is int and type(row[2]) is int,
             "COORDINATE_TYPES")
        need(tuple(row[:3]) == (block, i, j), "BLOCK_PARITY_ORDER")
        value = row[3]
        need(type(value) is str and INTEGER.fullmatch(value) is not None, "SIGNED_INTEGER")
        need(abs(int(value)).bit_length() <= MAX_BITS, "CENTER_WIDTH")
        need(raw == encode(row), "NONCANONICAL_RECORD")
        digest.update(raw)
        size += len(raw)
        count += 1
        block_counts[block] += 1
    need(stream.read(1) == b"", "EXTRA_RECORD_OR_BYTES")
    need(size <= count * MAX_RECORD, "PAYLOAD_BYTES")
    return dict(syntaxOnly=True, mathematicalSourceVerified=False,
                rows=count, bytes=size, sha256=digest.hexdigest(), blockCounts=block_counts)


def synthetic_controls():
    # Tiny artificial packet only; no source, matrix file or actual coefficient.
    rows = [[block, i, j, "0"] for block, i, j in expected(4)]
    fixture = b"".join(map(encode, rows))
    result = validate(io.BytesIO(fixture), 4)
    need(result["rows"] == 36, "TINY_COUNT")
    tests = 1
    cases = [fixture[:-1], fixture + b"\n", fixture.replace(b'"0"', b'"-0"', 1),
             fixture.replace(b'"0"', b'"00"', 1), fixture.replace(b'"0"', b'"+1"', 1),
             fixture.replace(b'"0"', b'0', 1), fixture.replace(b',0,0,', b',true,0,', 1),
             fixture.replace(b'"CX"', b'"FX"', 1), fixture.replace(b'"0"', b' "0"', 1),
             fixture.replace(b'"0"', encode([str(1 << 262)])[1:-2], 1),
             fixture.replace(b"\n", b"\r\n", 1)]
    for bad in cases:
        try:
            validate(io.BytesIO(bad), 4)
        except ValueError:
            tests += 1
        else:
            raise AssertionError("BAD_PACKET_ACCEPTED")
    m = N // 2
    need(2 * (m * (m + 1)) + 3 * (2 * m * m) == ROWS, "GLOBAL_COUNT")
    longest = encode(["FX", 447, 447, str(-((1 << MAX_BITS) - 1))])
    need(len(longest) == 98 and len(longest) <= MAX_RECORD, "WORST_RECORD")
    return dict(status="SYNTHETIC_FORMAT_CONTROLS_PASS", controls=tests + 2,
                syntheticDimension=4, prospectiveRows=ROWS,
                worstRecordBytes=len(longest), strictPayloadUpperBytes=ROWS * MAX_RECORD,
                actualPacketRead=False, actualSourceEvaluated=False,
                mathematicalSourceVerified=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--synthetic-only", action="store_true", required=True)
    parser.parse_args()
    print(json.dumps(synthetic_controls(), sort_keys=True))

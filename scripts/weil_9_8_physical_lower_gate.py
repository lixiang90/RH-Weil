"""One exact same-source Llow test after the fixed C058 comparison failed.

No new source generation, trial, compiler, Gram or parameter search.  The
input vector is in congruence coordinates; this script transports it to
raw physical Legendre coefficients before evaluating M+Kcompact+U.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
OLD = "reviews/2026-10-29/weil-9-8-admission/"
ROOT_SHA = "7333762b917efbd8fd92b95a177576eea92a7a6f231d8ff7236dca7cdf93a7c3"
CORE = "literature/local/2026-10-29-weil-9-8/pilot/core-run-02/"
DEST = REPO / "reviews/2026-10-29/weil-9-8-physical-lower-gate"
S, R, CW = 2**257, 2**256, 2**769


def mv(matrix, vector):
    return [sum(a*x for a, x in zip(row, vector)) for row in matrix]


def transpose_mv(matrix, vector):
    return [sum(row[k]*x for row, x in zip(matrix, vector))
            for k in range(len(vector))]


def transport(a, b, z, q, v, y):
    """u=Vint*v, without constructing Vint or changing the actual trial."""
    p = [qi*vi for qi, vi in zip(q, v)]
    zp, ztp = mv(z, p), transpose_mv(z, p)
    qzp = [qi*zi for qi, zi in zip(q, zp)]
    az, bz, ap = mv(a, qzp), mv(b, qzp), mv(a, p)
    quadratic = transpose_mv(z, [qi*(8*bi-ai) for qi, bi, ai in zip(q, bz, az)])
    ztqap = transpose_mv(z, [qi*ai for qi, ai in zip(q, ap)])
    fp = [18*S*R*(zi+zti)+quad-8*R*(ai+ati)
          for zi, zti, quad, ai, ati in zip(zp, ztp, quadratic, az, ztqap)]
    c = 8*CW+(9*y*y+16*y)*2**549
    return [qi*fi+18*c*pi for qi, fi, pi in zip(q, fp, p)]


def fraction(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def calculate():
    pins = {}

    def raw(relative, expected):
        path = (REPO / relative).resolve()
        assert path.is_relative_to(REPO) and path.is_file()
        data = path.read_bytes()
        observed = hashlib.sha256(data).hexdigest()
        assert observed == expected, f"INPUT_SHA:{relative}"
        name = path.relative_to(REPO).as_posix()
        assert name not in pins or pins[name]["sha256"] == expected
        pins[name] = {"sha256": expected, "bytes": len(data)}
        return data

    def read(relative, expected):
        return json.loads(raw(relative, expected))

    root = read(OLD+"root-consumption-scope.json", ROOT_SHA)
    bound = {entry["path"]: entry for entry in root["bindings"]}
    for entry in bound.values():
        raw(entry["path"], entry["sha256"])
    source = read(OLD+"source-stage-verification.json", bound[OLD+"source-stage-verification.json"]["sha256"])
    core = read(OLD+"core-stage-verification.json", bound[OLD+"core-stage-verification.json"]["sha256"])
    witness = read(OLD+"negative-direction-independent-replay.json", bound[OLD+"negative-direction-independent-replay.json"]["sha256"])
    for entry in witness["bindings"]:
        raw(entry["path"], entry["sha256"])
    for stage in core["completed_stages"]:
        if stage["stage"] in ("trial", "compile"):
            for path, sha in stage["receipt"]["inputSHA256"].items():
                raw(path, sha)
    packets = {}
    for item in source["stages"]:
        assert item["receipt"]["status"] == "SOURCE_ONLY_NOT_FULL_Q"
        assert item["audit_violation_count"] == 0
        packets[item["stage"]] = read(item["packet_path"], item["receipt"]["outputSHA256"])
    trial_receipt = next(item["receipt"] for item in core["completed_stages"] if item["stage"] == "trial")
    trial = read(CORE+"even-trial.json", trial_receipt["outputs"]["even-trial.json"])
    assert trial["sector"] == "even" and trial["norm"]["normPower"] == 3
    z = [[int(x) for x in row] for row in trial["Z"]]
    assert len(z) == 224 and all(len(row) == 224 for row in z)
    q = [8*(4*k+1) for k in range(224)]
    nu = sum(q[i]*q[k]*z[i][k]**2 for i in range(224) for k in range(224))
    assert str(nu) == trial["norm"]["squaredFrobeniusNumerator"] and nu <= 2**518

    packet = packets["matrices"]["packet"]
    assert packet["parameters"]["L"] == "9/8" and packet["parameters"]["outputBits"] == 256
    arrays = {}
    for name in ("A", "B", "J0"):
        rows = packet["matrices"][name]
        assert len(rows) == 50400
        matrix, cursor = [[0]*224 for _ in range(224)], 0
        for i in range(448):
            for k in range(i, 448, 2):
                row = rows[cursor]
                assert row[:2] == [i, k] and int(row[2]) <= int(row[3])
                if i % 2 == 0:
                    matrix[i//2][k//2] = matrix[k//2][i//2] = int(row[2])+int(row[3])
                cursor += 1
        assert cursor == 50400
        arrays[name] = matrix
    tail = packets["tails"]["packet"]
    assert tail["parameters"]["LNumerator"] == 9 and tail["parameters"]["LDenominator"] == 8
    assert tail["parameters"]["outputBits"] == 640 and len(tail["entries"]) == 896
    columns = [[0]*224 for _ in range(2)]
    for position, entry in enumerate(tail["entries"]):
        col, degree = divmod(position, 448)
        assert entry["column"] == col and entry["index"] == degree
        value = int(entry["midTwice"])
        assert value == int(entry["lo"])+int(entry["hi"])
        assert degree % 2 == col or value == 0
        if degree % 2 == 0:
            columns[col][degree//2] = value

    assert witness["full_dimension"] == 224 and witness["sector"] == "even"
    support = witness["nonzero_support_indices"]
    v = [0]*224
    for i, value in zip(support, witness["integer_vector_on_support"]):
        v[i] = int(value)
    old_n = sum(int(value)*v[i]*v[k]*(1 if i == k else 2)
                for i, k, value in witness["principal_block_upper_triangle"])
    assert old_n == int(witness["integer_quadratic_numerator"]) < 0
    u = transport(arrays["A"], arrays["B"], z, q, v, 8)
    assert any(u)
    au, ju = mv(arrays["A"], u), mv(arrays["J0"], u)
    energy = F(sum(x*(ai+ji) for x, ai, ji in zip(u, au, ju)), S)
    energy += F(36*sum(sum(t*x for t, x in zip(column, u))**2 for column in columns), 2**1282)
    norm = 18*sum((F(x*x, qi) for x, qi in zip(u, q)), F(0))
    assert norm > 0
    epsilon = F(1, 2**204)+F(2, 2**220)+F(9, 2**512)
    center = energy/norm
    low, high = center-epsilon, center+epsilon
    sign = "strictly_negative" if high < 0 else "strictly_positive" if low > 0 else "undecided"
    for relative, observed in list(pins.items()):
        raw(relative, observed["sha256"])
    return {
        "schema": "weil-9-8-same-source-physical-lower-gate-v1",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "object": "Actual Llow=M+Kcompact+U on the single mapped physical source, original du norm",
        "configuration": "Same actual595 L9/8 Omega256 N448 source/Z/y8; no parameter or proposal change",
        "sector": "even", "raw_original_degrees": list(range(0, 448, 2)),
        "congruence_input_integer_vector": [str(x) for x in v],
        "raw_source_coefficients_numerator_u": [str(x) for x in u],
        "raw_source_common_denominator": str(18*CW),
        "scaling": "Use integer v rather than v/2^512: same physical ray, source enlarged by 2^512. E0/N0 use raw u; divide both by (18Cw)^2 for physical energy/norm.",
        "E0": fraction(energy), "N0_original_du_norm": fraction(norm),
        "physical_source_norm_squared": fraction(norm/(18*CW)**2),
        "epsilon_low": fraction(epsilon), "center_rayleigh": fraction(center),
        "actual_Llow_rayleigh_interval": {"lower": fraction(low), "upper": fraction(high)},
        "actual_Llow_direction_sign": sign,
        "whole_Llow_nonnegative_certified": False,
        "full_Q_negative_certified": False, "window_coercivity_certified": False,
        "source_domain": "Finite Legendre polynomial on I, zero outside: compact BV and in Dlog. Norm/error are physical du; no sparse-physical claim.",
        "input_pins": pins, "upstream_driver_executed": False,
        "new_source_trial_Gram_or_parameter_search": False,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    assert __debug__ and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    output = parser.parse_args().output.resolve()
    assert output.is_relative_to(DEST) and not output.exists()
    result = calculate()
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as stream:
        stream.write((json.dumps(result, indent=2)+"\n").encode("utf-8"))
    print(json.dumps({"output": str(output), "sign": result["actual_Llow_direction_sign"],
                      "input_pins": len(result["input_pins"]),
                      "full_Q_negative_certified": False}))


if __name__ == "__main__":
    main()

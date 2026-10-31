"""ONE numerical spectrum of the frozen actual 448-mode Llow compression.

No old P0/Kcert/witness/trial, source production, inverse or parameter search.
Uses only inherited source intervals and the original physical du Gram.
Float eigenvalues and residuals are experiments, never sign certificates.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np


REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "actual-lowlow-spectrum-pilot.json"
N = 448
INPUTS = {
    "reviews/2026-10-29/weil-9-8-admission/source-stage-verification.json":
        "dbb31208d0568feac7c9adff27722d5b55d08381002d23e0a4e35f150b1472c1",
    "reviews/2026-10-29/weil-9-8-admission/full-weil-analytic-transfer-fresh.md":
        "0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466",
    "reviews/2026-10-31/direct-weil-core-admission/matrix-input-audit.md":
        "6b94561b7502c3327434c2339247a9c732b017431e019bb767a0e7281e5ac3a7",
    "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/source-matrices.json":
        "a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
    "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/tail-columns.json":
        "d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
}


def read_pinned(name: str, inventory: dict) -> bytes:
    path = REPO / name
    data = path.read_bytes()
    observed = hashlib.sha256(data).hexdigest()
    assert observed == INPUTS[name], name
    inventory[name] = {"bytes": len(data), "sha256": observed}
    return data


def raw_matrix(rows: list) -> np.ndarray:
    assert len(rows) == 50400
    result = np.zeros((N, N), dtype=np.float64)
    cursor = 0
    for i in range(N):
        for j in range(i, N, 2):
            row = rows[cursor]
            assert row[:2] == [i, j]
            lo, hi = int(row[2]), int(row[3])
            assert lo <= hi
            center = math.ldexp(float(lo + hi), -257)
            result[i, j] = result[j, i] = center
            cursor += 1
    assert cursor == len(rows)
    return result


def run() -> dict:
    assert not OUTPUT.exists(), "Single frozen pilot; never overwrite or rerun"
    started = time.perf_counter()
    inventory: dict = {}
    stage = json.loads(read_pinned(next(iter(INPUTS)), inventory))
    read_pinned("reviews/2026-10-29/weil-9-8-admission/full-weil-analytic-transfer-fresh.md", inventory)
    read_pinned("reviews/2026-10-31/direct-weil-core-admission/matrix-input-audit.md", inventory)
    matrix_name = "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/source-matrices.json"
    tail_name = "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/tail-columns.json"
    for record in stage["stages"]:
        if record["stage"] == "matrices":
            assert record["packet_path"].replace("\\", "/") == matrix_name
            assert record["receipt"]["outputSHA256"] == INPUTS[matrix_name]
        if record["stage"] == "tails":
            assert record["packet_path"].replace("\\", "/") == tail_name
            assert record["receipt"]["outputSHA256"] == INPUTS[tail_name]
    wrapper = json.loads(read_pinned(matrix_name, inventory))
    packet = wrapper["packet"]
    parameters = packet["parameters"]
    assert parameters["L"] == "9/8" and parameters["N"] == N
    assert parameters["omega"] == 256 and parameters["beta"] == "7/2"
    assert parameters["outputBits"] == 256
    assert packet["sourceConventions"]["J0"] == "L_squared_H"
    assert packet["sourceConventions"]["orderedPrimePairs"] == 225
    # A and J0 are raw Legendre centers (lo+hi)/2^257, not orthonormal matrices.
    araw = raw_matrix(packet["matrices"]["A"])
    jraw = raw_matrix(packet["matrices"]["J0"])
    tail = json.loads(read_pinned(tail_name, inventory))["packet"]
    tp = tail["parameters"]
    assert tp["LNumerator"] == 9 and tp["LDenominator"] == 8
    assert tp["dimension"] == N and tp["omega"] == 256
    assert tp["outputBits"] == 640 and len(tail["entries"]) == 2*N
    columns = np.zeros((2, N), dtype=np.float64)
    for position, entry in enumerate(tail["entries"]):
        col, degree = divmod(position, N)
        assert entry["column"] == col and entry["index"] == degree
        lo, hi, twice = int(entry["lo"]), int(entry["hi"]), int(entry["midTwice"])
        assert lo <= hi and twice == lo + hi
        assert degree % 2 == col or twice == 0
        columns[col, degree] = math.ldexp(float(twice), -641)
    # Exactly the frozen physical-gate convention: U_raw=36 sum column column*.
    craw = araw + jraw + 36.0 * (columns.T @ columns)
    gamma_du = 9.0 / (4.0 * (2.0*np.arange(N) + 1.0))
    inverse_sqrt = 1.0 / np.sqrt(gamma_du)
    native = np.outer(inverse_sqrt, inverse_sqrt) * craw
    assert np.all(np.isfinite(native))
    assert np.array_equal(native, native.T)
    assert np.count_nonzero(native[0::2, 1::2]) == 0
    results = []
    for parity, label in enumerate(("even", "odd")):
        block = native[parity::2, parity::2]
        assert block.shape == (224, 224)
        eigenvalues, eigenvectors = np.linalg.eigh(block)
        v = eigenvectors[:, 0]
        lam = float(eigenvalues[0])
        norm_inf = float(np.max(np.sum(np.abs(block), axis=1)))
        # A descriptive numerical screening threshold, explicitly NOT an error bound.
        screen = 1.0e-10 * max(1.0, norm_inf)
        classification = ("negative_center_candidate_only" if lam < -screen else
                          "positive_center_only" if lam > screen else
                          "roundoff_scale_unresolved_no_sign_certificate")
        raw_direction = inverse_sqrt[parity::2] * v
        results.append({
            "sector": label,
            "dimension": 224,
            "minimum_center_eigenvalue": lam,
            "lowest_16_center_eigenvalues": eigenvalues[:16].tolist(),
            "maximum_center_eigenvalue": float(eigenvalues[-1]),
            "negative_float_eigenvalue_count": int(np.sum(eigenvalues < 0)),
            "counts_below_minus_screen": int(np.sum(eigenvalues < -screen)),
            "counts_within_screen": int(np.sum(np.abs(eigenvalues) <= screen)),
            "matrix_infinity_norm": norm_inf,
            "eigenpair_residual_l2": float(np.linalg.norm(block @ v - lam*v)),
            "orthogonality_defect_infinity": float(np.linalg.norm(eigenvectors.T @ eigenvectors - np.eye(224), ord=np.inf)),
            "screening_threshold_not_rigorous": screen,
            "classification": classification,
            "minimum_eigenvector_native_du_coefficients": v.tolist(),
            "same_direction_raw_legendre_coefficients_float": raw_direction.tolist(),
            "raw_physical_du_norm_squared_float": float(np.sum(gamma_du[parity::2] * raw_direction**2)),
            "rigorous_sign_established": False,
        })
    for name in inventory:
        assert hashlib.sha256((REPO / name).read_bytes()).hexdigest() == INPUTS[name]
    return {
        "schema": "actual-lowlow-fixed448-spectrum-pilot-v1",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "object": "Actual C=E* Llow E, Llow=M+Kcompact+U, original L9/8 Omega256 N448; NOT P0, Kcert or full Q",
        "task": "New parent-authorized counterfactual whole-head center-sign gate; one run, no parameter/rank/precision sequence",
        "formula": "C=Gamma_du^-1/2 [(Aint+J0int)/2^257 +36 sum tint tint*/2^1282] Gamma_du^-1/2; Gamma_du,jj=9/[4(2j+1)]",
        "domain": "Both full224 parity sectors, original physical du normalization. Finite Legendre zero extension is in Dlog; Gamma_du is NOT Dlog Gram",
        "full_target_preserved": "Input-source construction retains all pp2/3/4/5/7/8/9, full compact Gamma/contact and even/odd pole terms, rank-two U only. Unused nonfinite Fourier tail is NOT included in Llow",
        "inherited_operator_error": "epsilon_low=2^-204+2*2^-220+9*2^-512, from old allsource A/H/U allowances; does not certify floating eigensolver/assembly errors",
        "numerical_method": "Single numpy.linalg.eigh for each original full224 sector; float64 center assembly, no source modules, no old calculate/old witness/old trial read",
        "runtime": {"python": sys.version, "executable": sys.executable, "numpy": np.__version__, "elapsed_seconds": time.perf_counter()-started},
        "input_pins": inventory,
        "results": results,
        "scope": "Experiment only. Negative center candidate needs a separate exact/interval certificate admission. Positive finite head does NOT prove whole Llow/Q; no followup pilot authorized",
        "source_rebuilt": False,
        "old_witness_or_P0_replayed": False,
        "whole_Llow_or_full_Q_certified": False,
        "mathematical_iteration_settled": False,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    result = run()
    with OUTPUT.open("xb") as stream:
        stream.write((json.dumps(result, ensure_ascii=False, indent=2)+"\n").encode("utf-8"))
    print(json.dumps({"output": str(OUTPUT), "results": [{k: item[k] for k in ("sector", "minimum_center_eigenvalue", "classification", "counts_below_minus_screen")} for item in result["results"]], "elapsed_seconds": result["runtime"]["elapsed_seconds"], "rigorous_sign_established": False}))

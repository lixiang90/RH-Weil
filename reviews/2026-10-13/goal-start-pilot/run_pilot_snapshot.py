"""C001 stage A smoke pilot. Exploratory finite sections; no certificates."""

from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import inspect
import json
import platform
import sys
import time
import traceback
import warnings
from pathlib import Path

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "scripts" / "qw_matrix.py"
T0 = time.perf_counter()
LOG = HERE / "run.log"


def lf_hash(text):
    return hashlib.sha256(text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")).hexdigest()


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def log(message):
    line = f"{time.perf_counter() - T0:.3f}s {message}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


def num(value):
    return mp.nstr(value, mp.mp.dps + 5)


def matrix_data(matrix):
    return [[num(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def maxabs(matrix):
    return max((abs(v) for v in matrix), default=mp.mpf(0))


def residual_data(matrix, scale):
    maximum = maxabs(matrix)
    return {"max_abs": num(maximum), "frobenius": num(mp.sqrt(sum(abs(v) ** 2 for v in matrix))), "relative_max_abs": num(maximum / max(mp.mpf(1), scale))}


def transforms(N):
    """The exact mp version of the source parity_blocks column convention."""
    Ue, Uo = mp.matrix(2 * N + 1, N + 1), mp.matrix(2 * N + 1, N)
    Ue[N, 0] = 1
    for n in range(1, N + 1):
        Ue[N + n, n] = Ue[N - n, n] = 1 / mp.sqrt(2)
        Uo[N + n, n - 1] = 1 / mp.sqrt(2)
        Uo[N - n, n - 1] = -1 / mp.sqrt(2)
    return Ue, Uo


def evaluate(qw, W, N, delta):
    Ue, Uo = transforms(N)
    E, O = Ue.T * W * Ue, Uo.T * W * Uo
    evals, evecs = mp.eigsy(E)
    ovals, ovecs = mp.eigsy(O)
    v = ovecs[:, 0]
    pivot = max(range(N), key=lambda i: abs(v[i]))
    if v[pivot] < 0:
        v = -v
    H = mp.matrix([[W[N + n, N - m] for m in range(1, N + 1)] for n in range(1, N + 1)])
    d = mp.matrix([W[N + n, N] for n in range(1, N + 1)])
    a0 = W[N, N]
    o = (v.T * O * v)[0]
    h = (v.T * H * v)[0]
    beta = mp.sqrt(2) * (d.T * v)[0]
    D = 2 * (a0 - o) * h - beta ** 2
    b = {n: n * W[N + n, N] for n in range(-N, N + 1)}
    displacement = mp.matrix(2 * N + 1)
    reflection = mp.matrix(2 * N + 1)
    for i, n in enumerate(range(-N, N + 1)):
        for j, m in enumerate(range(-N, N + 1)):
            reflection[i, j] = W[i, j] - W[2 * N - i, 2 * N - j]
            displacement[i, j] = (n - m) * W[i, j] - (b[n] - b[m])
    hankel_displacement = mp.matrix([[H[n - 1, m - 1] - (b[n] + b[m]) / (n + m) for m in range(1, N + 1)] for n in range(1, N + 1)])
    E_formula = mp.matrix(N + 1)
    E_formula[0, 0] = a0
    for n in range(1, N + 1):
        E_formula[0, n] = E_formula[n, 0] = mp.sqrt(2) * d[n - 1]
        for m in range(1, N + 1):
            E_formula[n, m] = O[n - 1, m - 1] + 2 * H[n - 1, m - 1]
    scale = maxabs(W)
    tau = mp.mpf("1e-10")

    def inertia(values):
        return {"negative_below_minus_tau": sum(x < -tau for x in values), "gray_abs_le_tau": sum(abs(x) <= tau for x in values), "positive_above_tau": sum(x > tau for x in values)}

    data = {
        "N": N, "dps": mp.mp.dps, "delta": delta,
        "W": matrix_data(W), "even_block": matrix_data(E), "odd_block": matrix_data(O),
        "even_spectrum": [num(x) for x in evals], "odd_spectrum": [num(x) for x in ovals],
        "lowest_even": num(evals[0]), "next_even": num(evals[1]), "lowest_odd": num(ovals[0]),
        "odd_minus_even_bottom": num(ovals[0] - evals[0]),
        "lowest_finite_parity": "even" if evals[0] < ovals[0] else "odd" if ovals[0] < evals[0] else "tie",
        "tau": num(tau), "even_inertia": inertia(evals), "odd_inertia": inertia(ovals),
        "reflection_residual": residual_data(reflection, scale),
        "symmetry_residual": residual_data(W - W.T, scale),
        "displacement_residual": residual_data(displacement, 2 * N * scale),
        "hankel_displacement_residual": residual_data(hankel_displacement, scale),
        "even_odd_cross_block_residual": residual_data(Ue.T * W * Uo, scale),
        "even_formula_residual": residual_data(E - E_formula, scale),
        "transform_orthonormality_residual": num(max(maxabs(Ue.T * Ue - mp.eye(N + 1)), maxabs(Uo.T * Uo - mp.eye(N)))),
        "odd_bottom_vector": [num(x) for x in v],
        "odd_bottom_vector_sign_rule": "largest-absolute coordinate positive; first coordinate on a tie",
        "odd_eigenvector_residual": num(mp.norm(O * v - ovals[0] * v)),
        "odd_vector_norm_residual": num(abs((v.T * v)[0] - 1)),
        "odd_rayleigh_minus_eigenvalue": num(o - ovals[0]),
        "H": matrix_data(H), "d": [num(x) for x in d],
        "a0": num(a0), "o": num(o), "h": num(h), "beta": num(beta),
        "D_2_a0_minus_o_h_minus_beta_squared": num(D),
        "a0_gt_o": bool(a0 > o),
        "finite_two_dimensional_D_criterion_applicable": bool(a0 > o),
        "finite_two_dimensional_D_negative_when_applicable": bool(D < 0) if a0 > o else None,
        "statement_class": "exploratory finite diagnostic; no interval enclosure or continuous operator claim",
    }
    if delta == "0":
        # This second independent source route checks the actual mp parity API.
        route_t0 = time.perf_counter()
        source_even, source_odd = qw.build_parity_blocks_mp(mp.sqrt(mp.mpf(13)), N)
        data["source_build_parity_blocks_mp_residual"] = {
            "even": residual_data(E - source_even, scale),
            "odd": residual_data(O - source_odd, scale),
            "seconds": time.perf_counter() - route_t0,
        }
    return data


def main():
    HERE.mkdir(parents=True, exist_ok=True)
    LOG.write_text("", encoding="utf-8", newline="\n")
    source_text = SOURCE.read_text(encoding="utf-8")
    source_sha = lf_hash(source_text)
    spec = importlib.util.spec_from_file_location("qw_pilot_source", SOURCE)
    qw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(qw)
    function_hashes = {name: lf_hash(inspect.getsource(getattr(qw, name))) for name in ("qw_entry", "q_nm", "von_mangoldt", "w02", "w_real", "w_primes", "build_parity_blocks_mp", "parity_blocks")}
    preregistration = {
        "candidate_id": "C001", "phase": "pending-run stage A smoke pilot",
        "mu": "13", "lambda": "sqrt(13)", "length": "log(13)", "N": [4, 6], "dps": [50, 70],
        "deltas": ["0", "+1/1000", "-1/1000"], "tau": "1e-10",
        "perturbed_atom": "p=2, exponent=1 only: pair +/-log(2) becomes +/-(log(2)+delta)",
        "fixed_weight": "von_mangoldt(2)/sqrt(2)=log(2)/sqrt(2)",
        "update": "W_delta(n,m)=W0(n,m)-weight*(q_nm(log(2)+delta,n,m,L)-q_nm(log(2),n,m,L))",
        "other_prime_power_atoms": "unchanged, including powers of 2 and endpoint 13; q_nm already represents the pair, no extra factor of 2",
        "matrix_construction": "Every W0 entry independently calls original qw_entry; cache separately for each N,dps; controls reuse W0",
        "true_parity_transform": "even V0, (Vn+V(-n))/sqrt2; odd (Vn-V(-n))/sqrt2, n=1..N, matching source APIs",
        "displacement_check": "b_n=n*W(n,0), b_0=0; (n-m)*W(n,m)=b_n-b_m; Hnm=W(n,-m)=(b_n+b_m)/(n+m)",
        "diagnostic": "v is re-solved true finite odd-bottom unit vector for each control; o=v^T O v, h=v^T H v, beta=sqrt2*d^T v, D=2*(a0-o)*h-beta^2; D criterion only applied when a0>o",
        "scope": "No zeta zeros, prolate candidate, interval certificate, new bound, RH decision, or completed mathematical research round",
        "source_file": str(SOURCE), "source_file_lf_sha256": source_sha, "source_function_lf_sha256": function_hashes,
    }
    prereg_path = HERE / "preregistration.json"
    if prereg_path.exists() and json.loads(prereg_path.read_text(encoding="utf-8")) != preregistration:
        raise RuntimeError("Existing preregistration differs; refusing to overwrite a frozen registration")
    save(prereg_path, preregistration)
    report = {
        "preregistration": preregistration,
        "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "environment": {"python": sys.version, "platform": platform.platform(), "mpmath": mp.__version__, "numpy": np.__version__},
        "exceptions": [], "warnings": [], "runs": [], "complete": False,
        "limits": "Exploratory finite smoke pilot only. No interval rounding, continuous spectral claim, new theorem/bound, RH verdict, prolate comparison, or completed mathematical round.",
    }
    out = HERE / "pilot-results.json"
    log("registration frozen; starting four W0 baselines")
    with warnings.catch_warnings(record=True) as captured:
        warnings.simplefilter("always")
        for N in (4, 6):
            for dps in (50, 70):
                mp.mp.dps = dps
                case_t0 = time.perf_counter()
                try:
                    L = mp.log(mp.mpf(13))
                    weight = qw.von_mangoldt(2) / mp.sqrt(2)
                    x0 = mp.log(2)
                    cache_file = HERE / f"W0-N{N}-dps{dps}.json"
                    if cache_file.exists():
                        cache = json.loads(cache_file.read_text(encoding="utf-8"))
                        if cache["source_file_lf_sha256"] != source_sha or cache["mu"] != "13" or cache["N"] != N or cache["dps"] != dps:
                            raise RuntimeError("W0 cache source/parameters mismatch")
                        W0 = mp.matrix([[mp.mpf(x) for x in row] for row in cache["W0"]])
                        baseline_seconds = cache["original_build_seconds"]
                        from_cache = True
                    else:
                        build_t0 = time.perf_counter()
                        W0 = mp.matrix(2 * N + 1)
                        for i, n in enumerate(range(-N, N + 1)):
                            for j, m in enumerate(range(-N, N + 1)):
                                W0[i, j] = qw.qw_entry(n, m, L)
                            log(f"N={N} dps={dps}: W0 row {i + 1}/{2 * N + 1}")
                        baseline_seconds = time.perf_counter() - build_t0
                        from_cache = False
                        save(cache_file, {"mu": "13", "N": N, "dps": dps, "source_file_lf_sha256": source_sha, "source_function_lf_sha256": function_hashes, "original_build_seconds": baseline_seconds, "indices": list(range(-N, N + 1)), "W0": matrix_data(W0)})
                    log(f"N={N} dps={dps}: W0 ready, original build {baseline_seconds:.3f}s")
                    for label in ("0", "+1/1000", "-1/1000"):
                        control_t0 = time.perf_counter()
                        delta = mp.mpf(0) if label == "0" else mp.mpf(1 if label[0] == "+" else -1) / 1000
                        W = mp.matrix(W0)
                        update = mp.matrix(2 * N + 1)
                        if delta:
                            for i, n in enumerate(range(-N, N + 1)):
                                for j, m in enumerate(range(-N, N + 1)):
                                    update[i, j] = -weight * (qw.q_nm(x0 + delta, n, m, L) - qw.q_nm(x0, n, m, L))
                                    W[i, j] += update[i, j]
                        data = evaluate(qw, W, N, label)
                        data.update({"base_cache_file": cache_file.name, "base_reused_from_existing_disk_cache": from_cache, "W0_build_seconds": baseline_seconds, "control_seconds": time.perf_counter() - control_t0, "fixed_weight_numeric": num(weight), "atom_location_numeric": num(x0 + delta), "displacement_update": matrix_data(update)})
                        report["runs"].append(data)
                        save(out, report)
                        log(f"N={N} dps={dps} delta={label}: even={num(mp.mpf(data['lowest_even']))} odd={num(mp.mpf(data['lowest_odd']))} next-even={num(mp.mpf(data['next_even']))}; done {data['control_seconds']:.3f}s")
                    log(f"N={N} dps={dps}: case done {time.perf_counter() - case_t0:.3f}s")
                except Exception as exc:
                    item = {"N": N, "dps": dps, "type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc(), "elapsed_seconds": time.perf_counter() - T0}
                    report["exceptions"].append(item)
                    save(out, report)
                    log(f"EXCEPTION N={N} dps={dps}: {item['type']}: {item['message']}")
        report["warnings"] = [{"category": w.category.__name__, "message": str(w.message), "filename": w.filename, "lineno": w.lineno} for w in captured]
    mp.mp.dps = 80
    report["cross_precision_absolute_differences"] = []
    for N in (4, 6):
        for delta in ("0", "+1/1000", "-1/1000"):
            pair = {r["dps"]: r for r in report["runs"] if r["N"] == N and r["delta"] == delta}
            if set(pair) == {50, 70}:
                report["cross_precision_absolute_differences"].append({"N": N, "delta": delta, **{key: num(abs(mp.mpf(pair[70][key]) - mp.mpf(pair[50][key]))) for key in ("lowest_even", "lowest_odd", "next_even", "o", "h", "beta", "D_2_a0_minus_o_h_minus_beta_squared")}})
    report["source_file_lf_sha256_end"] = lf_hash(SOURCE.read_text(encoding="utf-8"))
    report["source_unchanged"] = report["source_file_lf_sha256_end"] == source_sha
    report["wrapper_lf_sha256"] = lf_hash(Path(__file__).read_text(encoding="utf-8"))
    report["elapsed_seconds"] = time.perf_counter() - T0
    report["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    report["complete"] = len(report["runs"]) == 12 and not report["exceptions"] and report["source_unchanged"]
    save(out, report)
    log(f"finished {len(report['runs'])}/12 cases; exceptions={len(report['exceptions'])}; warnings={len(report['warnings'])}; complete={report['complete']}")
    return 0 if report["complete"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        HERE.mkdir(parents=True, exist_ok=True)
        save(HERE / "fatal-exception.json", {"type": sys.exc_info()[0].__name__, "message": str(sys.exc_info()[1]), "traceback": traceback.format_exc(), "elapsed_seconds": time.perf_counter() - T0})
        raise

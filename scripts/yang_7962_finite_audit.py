#!/usr/bin/env python3
"""Exact finite diagnostics for the Yang--Yang 79.62% candidate.

This checks a rational consumer and distinguishes three finite lock energies.
It does not prove zeta trace-moment limits, truncation, or a zero-count bridge.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/yang-7962-finite-audit.json"
PDF = ROOT / "literature/unreviewed/2026-yang-7962-unreviewed-v1.pdf"
PDF_SHA256 = "0abaa78e0eb4421fdbae647a0b3b6b0299a4dde5d49b0e56ca6f33831c5e3ea0"


def multiply(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def show(x):
    with localcontext() as ctx:
        ctx.prec = 55
        decimal = str(Decimal(x.numerator) / Decimal(x.denominator))
    return {"rational": str(x), "decimal": decimal}


def build():
    checks = []

    def require(ok, label):
        if not ok:
            raise AssertionError(label)
        checks.append(label)

    require(hashlib.sha256(PDF.read_bytes()).hexdigest() == PDF_SHA256,
            "archived English PDF fixed")
    roots = [Q(5323, 10000), Q(6561, 5000), Q(10293, 5000)]
    cubic = [Q(1)]
    for r in roots:
        cubic = multiply(cubic, [Q(1), -1 / r])
    y = multiply(cubic, cubic)
    require(y[0] == 1 and len(y) == 7, "degree-six square normalized")
    require(all((-1) ** k * v > 0 for k, v in enumerate(y)),
            "strict alternating coefficient signs")
    moments = [Q(1), Q(1), Q(4, 3), Q(2), Q(13, 4), Q(101, 18), Q(12809, 1260)]
    w0 = sum(v * m for v, m in zip(y, moments))
    require(w0 == Q(829278553005924403328783, 8140995278473611944088783),
            "exact nominal consumer value")
    require(1 - 2 * w0 > Q(7962, 10000), "conditional simple headline strict")
    require(1 - w0 > Q(8981, 10000), "conditional distinct headline strict")
    target = Q(6734824, 10**7)
    slack = (1 - target) / 2 - w0
    require(slack > 0, "positive consumer error budget against comparison target")
    common = slack / sum(abs(v) for v in y[1:])
    individual = {str(k): slack / abs(y[k]) for k in [4, 5, 6]}
    require(1 - 2 * (w0 + common * sum(abs(v) for v in y[1:])) == target,
            "common absolute moment error budget endpoint")
    for k, e in individual.items():
        require(1 - 2 * (w0 + abs(y[int(k)]) * e) == target,
                "single moment error budget endpoint: " + k)
    v, b4 = Q(1, 3), Q(1, 4)
    central_p = (1 - v) ** 2 / (1 - 2 * v + b4)
    require(central_p == Q(16, 21), "existing conditional central-fourth payoff")
    central_cap = (1 - v) ** 2 / target - 1 + 2 * v
    require((1 - v) ** 2 / (1 - 2 * v + central_cap) == target,
            "central-fourth comparison threshold")

    # Indicator sequence f=1_{0,1}. Complete integer ranges, no FFT wrap.
    def f(x):
        return int(x in [0, 1])

    ac = {t: sum(f(x) * f(x + t) for x in [0, 1]) for t in [-1, 0, 1]}
    rho = {s: sum(ac.get(t, 0) * ac.get(t - s, 0) for t in ac)
           for s in [-2, -1, 0, 1, 2]}
    resolved = {f"{k},{j}": sum(f(m) * f(m - k) * f(m + j) * f(m + j - k)
                               for m in [0, 1])
                for k in [-1, 0, 1] for j in [-1, 0, 1]}
    resolved_energy = sum(n * n for n in resolved.values())
    density_energy = sum(n * n for n in rho.values())
    all_free_locks_energy = sum(a ** 4 for a in ac.values())
    require((resolved_energy, density_energy, all_free_locks_energy) == (8, 70, 18),
            "resolved locks, density Parseval, and all-free locks are distinct")
    positive_k_energy = sum(n * n for kj, n in resolved.items() if int(kj.split(",")[0]) > 0)
    require(positive_k_energy == 1, "positive-k resolved variant")
    offsets = [0, -2, 4, 2]
    four_allowed = sum(all((m + off) % 3 != 0 for off in offsets) for m in range(3))
    twin_allowed = sum(all((m + off) % 3 != 0 for off in [0, -2]) for m in range(3))
    require(four_allowed == 0 and twin_allowed == 1,
            "fixed four-point local mask differs from independent twin product")
    return {
        "status": "conditional finite audit only",
        "proves_analytic_moments": False,
        "proves_zero_proportion": False,
        "proves_zero_free_region": False,
        "author_commit": "d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8",
        "pdf_sha256": PDF_SHA256,
        "roots": [show(r) for r in roots],
        "coefficients": [show(v) for v in y],
        "nominal_moments": [show(m) for m in moments],
        "nominal_w0": show(w0),
        "conditional_simple": show(1 - 2 * w0),
        "conditional_distinct": show(1 - w0),
        "comparison_target": show(target),
        "consumer_slack": show(slack),
        "common_absolute_moment_error": show(common),
        "individual_moment_errors": {k: show(e) for k, e in individual.items()},
        "central_fourth_conditional_payoff": show(central_p),
        "central_fourth_cap_against_target": show(central_cap),
        "finite_lock_diagnostic": {
            "sequence_support": [0, 1], "autocorrelation": ac, "density": rho,
            "resolved": resolved, "resolved_energy": resolved_energy,
            "density_energy": density_energy, "all_free_locks_energy": all_free_locks_energy,
            "positive_k_energy": positive_k_energy,
            "mod3_four_offsets": offsets, "mod3_four_allowed": four_allowed,
            "mod3_twin_allowed": twin_allowed,
            "scope": "generic finite identity diagnostic; not a counterexample to prime asymptotics",
        },
        "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.write:
        OUT.write_text(encoded, encoding="utf-8", newline="\n")
    elif args.check:
        if OUT.read_text(encoding="utf-8") != encoded:
            raise AssertionError("saved finite audit differs")
    print(f"PASS: {len(result['checks'])} exact finite checks; analytic inputs remain unproved.")


if __name__ == "__main__":
    main()

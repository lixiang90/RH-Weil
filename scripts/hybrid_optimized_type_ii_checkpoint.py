#!/usr/bin/env python3
"""Exact cuts, costs, and finite coefficient checks for the original Type II.

Infinite estimates and analytic continuations require the separate math reviews.
The finite checks do not prove a new whole fourth-moment or zero-free bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import gcd
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/hybrid-optimized-type-ii-checkpoint.json"
NOTE = "notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md"
TAIL = "reviews/2026-10-08/hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md"
FROZEN = {
    TAIL: "66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab",
    "reviews/2026-10-08/hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md":
        "cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4",
    "reviews/2026-10-08/hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md":
        "b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0",
    "reviews/2026-10-08/hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md":
        "f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7",
    "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md":
        "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
}


def canonical(p):
    return p.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def floor_power(x, num, den):
    target = x ** num
    lo, hi = 0, x + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** den <= target:
            lo = mid
        else:
            hi = mid
    return lo


def factor(n):
    out, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mu(n):
    f = factor(n)
    return 0 if any(v > 1 for v in f.values()) else (-1) ** len(f)


def divisors(n):
    d = [1]
    for p, e in factor(n).items():
        d = [a * p ** j for a in d for j in range(e + 1)]
    return sorted(d)


def b(v, k):
    return sum(mu(d) for d in divisors(k) if d <= v)


def once(k):
    s = 1
    for p, e in factor(k).items():
        if e == 1:
            s *= p
    return s


def add(a, b0, weight=1):
    out = dict(a)
    for p, value in b0.items():
        out[p] = out.get(p, 0) + weight * value
    return {p: v for p, v in out.items() if v}


def lam(n):
    f = factor(n)
    return {next(iter(f)): 1} if len(f) == 1 else {}


def build():
    checks = []

    def require(ok, label):
        if not ok:
            raise AssertionError(label)
        checks.append(label)

    files = {}
    for s in [NOTE, *FROZEN, "scripts/hybrid_optimized_type_ii_checkpoint.py"]:
        data = canonical(ROOT / s)
        h = hashlib.sha256(data).hexdigest()
        if s in FROZEN:
            require(h == FROZEN[s], "frozen input: " + s)
        files[s] = {"canonical_sha256": h, "canonical_bytes": len(data),
                    "lines": len(data.splitlines())}
    v, a, y = Q(2, 21), Q(4, 21), Q(17, 21)
    costs = {"low": 2 * y - 1, "type_i": Q(1, 3) + 2 * v,
             "short_lambda": Q(1, 3) + a + v,
             "proper_power": 1 - 2 * a, "squarefull_tail": 1 - 4 * v}
    require(0 < v < a and max(Q(1, 2), a + v) < y < 1, "parameter domain")
    require(max(costs.values()) == Q(13, 21), "complete error cost")
    require(costs["type_i"] == Q(11, 21), "type I cost")
    c, whole = Q(13, 21), Q(5, 7)
    require(Q(1, 3) + 3 * (1 - c) / 4 == c, "cost-family lower-bound equality")
    transfer = (3 * whole + c) / 4
    require(transfer == Q(29, 42), "complete moment transfer cost")
    require(whole - transfer == Q(1, 42), "saving against whole growth scale")
    require(Q(479, 672) - transfer == Q(5, 224), "saving against old transfer error")

    finite_counts = []
    # Symbolic prime logarithms, not floating approximations to coefficients.
    for x in [4096, 6561]:
        u = vcut = floor_power(x, 2, 21)
        mcut, ycut = floor_power(x, 4, 21), floor_power(x, 17, 21)
        hcut = vcut ** 2
        require(2 <= u < mcut and mcut * vcut < ycut and hcut <= mcut,
                "exact finite floor domain: " + str(x))
        g = {}
        for aa in range(1, u + 1):
            for dd in range(1, vcut + 1):
                g[aa * dd] = add(g.get(aa * dd, {}), lam(aa), -mu(dd))
        count = 0
        for n in range(ycut + 1, x + 1):
            ds = divisors(n)
            i2, i3, c4 = {}, {}, {}
            parts = [{}, {}, {}, {}]
            merged_tail = {}
            for d in ds:
                i2 = add(i2, g.get(d, {}))
                if d <= vcut:
                    i3 = add(i3, factor(n // d), mu(d))
                m, k = d, n // d
                if m <= u or k <= vcut or not lam(m):
                    continue
                coeff = b(vcut, k)
                c4 = add(c4, lam(m), -coeff)
                fm = factor(m)
                part = 0 if m <= mcut else 1 if next(iter(fm.values())) > 1 else 2 if k // once(k) > hcut else 3
                parts[part] = add(parts[part], lam(m), -coeff)
            for rr in ds:
                if rr <= hcut or once(rr) != 1:
                    continue
                nn = n // rr
                for m in divisors(nn):
                    s = nn // m
                    if m > mcut and factor(m) == {m: 1} and mu(s) != 0 and gcd(s, rr) == 1 and s * rr > vcut:
                        merged_tail = add(merged_tail, {m: 1}, -b(vcut, s * rr))
            require(add(add(i2, i3), c4) == lam(n), "finite Vaughan coefficient: " + str(x) + ":" + str(n))
            total = {}
            for p0 in parts:
                total = add(total, p0)
            require(total == c4, "finite exact partition: " + str(x) + ":" + str(n))
            require(merged_tail == parts[2], "finite merged squarefull tail: " + str(x) + ":" + str(n))
            count += 1
        finite_counts.append({"X": x, "U": u, "V": vcut, "M": mcut,
                              "H": hcut, "floor_Y": ycut, "high_coefficients": count})

    euler_counts = []
    for vv in [2, 3, 5]:
        hh = vv ** 2
        primes = [p for p in range(2, hh + 1) if factor(p) == {p: 1}]
        sf = [1]
        product = Q(1)
        for p in primes:
            sf += [s * p for s in sf]
            product *= 1 + Q(1, p ** 2)
        ts = [t for t in range(1, hh + 1) if once(t) == 1]
        left, cvh = Q(0), Q(0)
        for t in ts:
            for s in sf:
                if gcd(s, t) == 1 and s * t > vv:
                    left += Q(b(vv, s * t), (s * t) ** 2)
            ft = Q(0)
            rad = 1
            for p in factor(t):
                rad *= p
            for qq in divisors(rad):
                if qq > vv:
                    continue
                for aa in range(1, vv // qq + 1):
                    if mu(aa) == 0 or gcd(aa, t) != 1:
                        continue
                    term = Q(mu(qq) * mu(aa), aa ** 2)
                    for p in factor(aa * t):
                        term /= 1 + Q(1, p ** 2)
                    ft += term
            cvh += ft / t ** 2
        require(left == product * cvh - 1, "finite-prime Euler identity with exact minus one: V=" + str(vv))
        euler_counts.append({"V": vv, "H": hh, "prime_count": len(primes),
                             "squarefree_count": len(sf), "squarefull_count": len(ts)})
    return {"status": "finite arithmetic and source bindings only",
            "proves_infinite_estimates": False, "proves_new_whole_bound": False,
            "proves_new_zero_proportion_or_region": False,
            "parameters": {"v": str(v), "a": str(a), "y": str(y), "H": "V^2"},
            "costs": {k: str(z) for k, z in costs.items()}, "complete_error": str(c),
            "quoted_whole": str(whole), "conditional_transfer": str(transfer),
            "finite_coefficient_runs": finite_counts, "finite_euler_runs": euler_counts,
            "check_count": len(checks), "check_digest": hashlib.sha256("\n".join(checks).encode()).hexdigest(),
            "files": files}


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
    elif args.check and OUT.read_text("utf-8") != encoded:
        raise AssertionError("saved optimized checkpoint differs")
    print(f"PASS: {result['check_count']} exact checks; infinite conclusions require math reviews.")


if __name__ == "__main__":
    main()

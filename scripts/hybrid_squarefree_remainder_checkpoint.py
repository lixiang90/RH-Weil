"""Check formal Dirichlet coefficients and finite costs, not analytic limits."""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-squarefree-remainder-checkpoint.json"
INPUTS = {
    "notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md":
        "17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487",
    "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md":
        "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
    "reviews/2026-10-08/hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md":
        "66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab",
    "reviews/2026-10-08/hybrid-original-squarefree-core-euler-perron-research-perron.md":
        "2f25a678b0c38c95a40469c41a757506c6f1fe64343bed327c7effe298e980c0",
    "reviews/2026-10-08/hybrid-original-squarefree-core-euler-perron-review-peer.md":
        "3b6891622b6d76008223062308d2f053fa8186e02d5defcf3b872d027a1a618a",
    "reviews/2026-10-08/hybrid-original-weighted-mobius-squarefree-perron-research-high-product.md":
        "426e0e72e9234e6a9eccbe9a82e3055e7bbbc1669956ae78b9c4a6f82e9799b6",
    "reviews/2026-10-08/hybrid-original-weighted-mobius-squarefree-perron-review-peer.md":
        "543ff156e86c0b051a69559e1d8c553f61fddaaf228a682759d457ce9012f4ac",
    "notes/488-original-squarefree-core-and-half-power-error.md":
        "0e2f1cf88d4de1a804c1b9e6ce21febe85c8c5856726fd66c2d778cce29b5825",
    "notes/490-original-weighted-mobius-squarefree-conditional-remainder.md":
        "a5bf40493c864774da5f8fbecce8d257bc21176a78b16ff1841c89843d4924ef",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def factors(n: int) -> dict[int, int]:
    result: dict[int, int] = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def convolution(a: Sequence[int | Q], b: Sequence[int | Q]) -> list[int | Q]:
    limit = len(a)-1
    result: list[int | Q] = [0]*(limit+1)
    for i in range(1, limit+1):
        if a[i]:
            for j in range(1, limit//i+1):
                result[i*j] += a[i]*b[j]
    return result


def log_convolution(a: list[dict[int, int]], b: list[int]) -> list[dict[int, int]]:
    """The independent formal basis consists of log(p), for prime p."""
    limit = len(a)-1
    result: list[dict[int, int]] = [{} for _ in range(limit+1)]
    for i in range(1, limit+1):
        if a[i]:
            for j in range(1, limit//i+1):
                if b[j]:
                    row = result[i*j]
                    for p, coefficient in a[i].items():
                        row[p] = row.get(p, 0)+coefficient*b[j]
    return [{p: c for p, c in row.items() if c} for row in result]


def finite_case(limit: int, v: int, u: int) -> dict:
    facts = [factors(n) if n else {} for n in range(limit+1)]
    mu = [0]+[(-1)**len(facts[n]) if all(e == 1 for e in facts[n].values()) else 0
               for n in range(1, limit+1)]
    squarefree = [m*m for m in mu]
    ones = [0]+[1]*limit
    inverse_zeta2 = [0]*(limit+1)
    for n in range(1, isqrt(limit)+1):
        inverse_zeta2[n*n] = mu[n]
    if convolution(ones, inverse_zeta2) != squarefree:
        raise RuntimeError("Finite zeta/zeta(2s) coefficients differ")

    def local_series(r: int, bound: int) -> list[int]:
        """Expand the inverse factors, including all prime powers up to bound."""
        result = [0]*(bound+1)
        rprimes = set(facts[r])
        radical = 1
        for p in rprimes:
            radical *= p
        for q in range(1, min(radical, v)+1):
            if radical % q or not mu[q]:
                continue
            for a in range(1, min(v//q, bound)+1):
                if not mu[a] or gcd(a, r) != 1:
                    continue
                allowed = rprimes | set(facts[a])
                for j in range(1, bound//a+1):
                    if set(facts[j]) <= allowed:
                        result[a*j] += mu[q]*mu[a]*(-1)**sum(facts[j].values())
        return result

    h = v*v
    ch = [0]*(limit+1)
    squarefull_count = 0
    for r in range(2, min(h, limit)+1):
        if all(e >= 2 for e in facts[r].values()):
            squarefull_count += 1
            series = local_series(r, limit//r)
            for n in range(1, len(series)):
                ch[r*n] += series[n]
    c1 = local_series(1, limit)
    non_squarefree = convolution(squarefree, ch)
    sf_series = convolution(squarefree, c1)
    sf_series[1] -= 1

    def b(k: int) -> int:
        return sum(mu[d] for d in range(1, min(v, k)+1) if k % d == 0)

    expected_non_sf = [0]*(limit+1)
    expected_sf = [0]*(limit+1)
    for k in range(1, limit+1):
        r = 1
        for p, e in facts[k].items():
            if e >= 2:
                r *= p**e
        if k > v:
            if 2 <= r <= h:
                expected_non_sf[k] = b(k)
            elif r == 1:
                expected_sf[k] = b(k)
    if non_squarefree != expected_non_sf or sf_series != expected_sf:
        raise RuntimeError("Original squarefull/squarefree coefficients differ")

    prime_above: list[dict[int, int]] = [{} for _ in range(limit+1)]
    pp_and_small_prime: list[dict[int, int]] = [{} for _ in range(limit+1)]
    proper_above: list[dict[int, int]] = [{} for _ in range(limit+1)]
    for n in range(2, limit+1):
        if len(facts[n]) == 1:
            p, e = next(iter(facts[n].items()))
            if e == 1 and n > u:
                prime_above[n] = {p: 1}
            if e >= 2 or (e == 1 and n <= u):
                pp_and_small_prime[n] = {p: 1}
            if e >= 2 and n > u:
                proper_above[n] = {p: 1}
    left = log_convolution(prime_above, non_squarefree)
    left = [{p: -c for p, c in row.items()} for row in left]
    cancelled = log_convolution(pp_and_small_prime, ones)
    for n in range(1, limit+1):
        for p, e in facts[n].items():
            cancelled[n][p] = cancelled[n].get(p, 0)-e
    right = log_convolution(cancelled, convolution(ch, inverse_zeta2))
    if left != right:
        raise RuntimeError("Genuine-prime convolution after pole cancellation differs")

    finite_mu = [0]*(limit+1)
    finite_mu[1:v+1] = mu[1:v+1]
    all_k = convolution(ones, finite_mu)
    all_k[1] -= 1
    expected_all = [0]+[b(k) if k > v else 0 for k in range(1, limit+1)]
    if all_k != expected_all:
        raise RuntimeError("Proper-power product-cut kernel coefficients differ")
    if log_convolution(proper_above, all_k) != log_convolution(proper_above, expected_all):
        raise RuntimeError("Complete proper-power coefficients differ")
    return {"limit": limit, "U": u, "V": v, "H": h,
            "squarefull_r_values": squarefull_count,
            "coefficient_checks": 4*limit,
            "formal_log_prime_basis": True}


def display(value: Q) -> str:
    with localcontext() as context:
        context.prec = 60
        return str(Decimal(value.numerator)/Decimal(value.denominator))


def weighted_euler_case(limit: int, r: int, w: int) -> dict:
    """Exact rational specialisations; no assertion about complex half-planes."""
    rprimes = set(factors(r))
    mu = [Q(0)]
    left = [Q(0)]
    correction = [Q(0)]
    for n in range(1, limit+1):
        fs = factors(n)
        m = (-1)**len(fs) if all(e == 1 for e in fs.values()) else 0
        mu.append(Q(m))
        value = Q(m if not set(fs) & rprimes else 0)
        k = Q(1)
        for p in fs:
            value *= Q(p**w, p**w+1)
            if p not in rprimes:
                k *= Q(1, p**w+1)
        left.append(value)
        correction.append(k)
    if convolution(mu, correction) != left:
        raise RuntimeError("Weighted Euler quotient coefficients differ")
    return {"limit": limit, "r": r, "integer_real_w": w,
            "identity": "weighted_mu = inverse_zeta * correction",
            "proves_complex_uniform_convergence": False}


def replay() -> dict:
    checks: list[str] = []

    def check(name: str, valid: bool) -> None:
        if not valid:
            raise RuntimeError("Failed finite check: "+name)
        checks.append(name)

    for name, expected in INPUTS.items():
        check("frozen input: "+name, sha(ROOT/name) == expected)
    cases = []
    for limit in [128, 256]:
        for v in [2, 3, 4, 8, 12]:
            for u in [v, 2*v-1]:
                cases.append(finite_case(limit, v, u))
                checks.append(f"formal coefficients N={limit}, V={v}, U={u}")
    weighted_cases = []
    for r in [1, 4, 8, 36, 72]:
        for w in [1, 2]:
            weighted_cases.append(weighted_euler_case(128, r, w))
            checks.append(f"weighted Euler rational specialisation r={r}, w={w}")
    v, y = Q(1, 8), Q(3, 4)
    costs = [2*y-1, 4*v, 2*v, 4*v, 1-4*v, Q(0)]
    check("complete unconditional costs", max(costs) == Q(1, 2))
    check("Vaughan guards", 0 < v < Q(1, 4) and max(Q(1, 2), 2*v) < y < 1)
    check("complete nominal transfer", (3*Q(5, 7)+Q(1, 2))/4 == Q(37, 56))
    check("nominal transfer margin", Q(5, 7)-Q(37, 56) == Q(3, 56))
    check("previous conditional error saving", Q(9, 17)-Q(1, 2) == Q(1, 34))
    check("previous conditional transfer saving", Q(159, 238)-Q(37, 56) == Q(1, 136))
    check("previous unconditional error saving", Q(3, 5)-Q(1, 2) == Q(1, 10))
    elo, ehi = Q(16683858898627, 10**14), Q(16683858898628, 10**14)
    poly = lambda e: 657*e**3-954*e**2+21*e+20
    check("451 cubic endpoint signs", poly(elo) > 0 > poly(ehi))
    tlo, thi = Q(11, 12)-ehi/4, Q(11, 12)-elo/4
    bfun = lambda t: 4*t-3+3*(1-t)/(2*t)
    glo, ghi = (3*bfun(tlo)+Q(1, 2))/4, (3*bfun(thi)+Q(1, 2))/4
    check("existing whole derivative throughout interval", 4-Q(3, 2)/tlo**2 > 0)
    check("strict existing-boundary transfer envelope", Q('.6606485022147674') < glo <= ghi < Q('.6606485022147714'))
    beta, cv, cy = Q(3, 4), Q(1, 7), Q(5, 7)
    conditional_costs = [2*cy-1, 4*beta*cv, 2*beta*cv, 4*beta*cv, 1-4*cv, Q(0)]
    check("nominal weighted complete costs", max(conditional_costs) == Q(3, 7))
    check("nominal weighted guards", 0 < cv < Q(1, 4) and max(Q(1, 2), 2*cv) < cy < 1)
    check("nominal weighted transfer", (3*Q(5, 7)+Q(3, 7))/4 == Q(9, 14))
    check("weighted error saving over half", Q(1, 2)-Q(3, 7) == Q(1, 14))
    check("weighted transfer saving over half", Q(37, 56)-Q(9, 14) == Q(1, 56))
    branch_examples = []
    for theta in [Q(3, 4), Q(5, 6), Q(7, 8), Q(9, 10)]:
        vv, yy = 1/(8*theta), 1-1/(4*theta)
        cc = 1-1/(2*theta)
        vec = [2*yy-1, 4*(2*theta-1)*vv, 1-4*vv, Q(0)]
        check(f"finite weighted branch theta={theta}", max(vec) == cc and
              0 < vv < Q(1, 4) and max(Q(1, 2), 2*vv) < yy < 1)
        branch_examples.append({"theta": str(theta), "v": str(vv), "y": str(yy),
                                "costs": list(map(str, vec)), "maximum": str(cc)})
    cfun = lambda t: 1-1/(2*t)
    clo, chi = cfun(tlo), cfun(thi)
    cglo, cghi = (3*bfun(tlo)+clo)/4, (3*bfun(thi)+chi)/4
    check("weighted boundary error envelope", Q('.4285433582424544') < clo <= chi < Q('.4285433582424561'))
    check("weighted boundary transfer envelope", Q('.6427843417753810') < cglo <= cghi < Q('.6427843417753854'))
    check("weighted boundary inside analytic domain", Q(5, 6) < tlo < thi < Q(7, 8))
    check("weighted boundary parameter guards over entire interval", 0 < 1/(8*thi) <= 1/(8*tlo) < Q(1, 4)
          and max(Q(1, 2), 1/(4*tlo)) < 1-1/(4*tlo) <= 1-1/(4*thi) < 1)
    return {"schema": "rh-weil-squarefree-remainder-finite-checkpoint-v1", "status": "PASS",
            "baseline_commit": "a4e4c8cf3de71450325174028f0ed09dd5ef4dec",
            "check_count": len(checks), "checks": checks, "finite_cases": cases,
            "weighted_euler_rational_specialisations": weighted_cases,
            "input_canonical_lf_sha256": INPUTS, "script_canonical_lf_sha256": sha(Path(__file__)),
            "nominal_costs": list(map(str, costs)), "unconditional_error": "1/2",
            "conditional_nominal_transfer": "37/56",
            "existing_boundary_transfer": {"rational_lower": str(glo), "rational_upper": str(ghi),
                                           "decimal_lower_informational": display(glo),
                                           "decimal_upper_informational": display(ghi)},
            "weighted_nominal_costs": list(map(str, conditional_costs)),
            "weighted_conditional_error": "3/7", "weighted_conditional_transfer": "9/14",
            "weighted_finite_branch_examples_only": branch_examples,
            "weighted_existing_boundary_error": {"rational_lower": str(clo), "rational_upper": str(chi),
                                                  "decimal_lower_informational": display(clo),
                                                  "decimal_upper_informational": display(chi)},
            "weighted_existing_boundary_transfer": {"rational_lower": str(cglo), "rational_upper": str(cghi),
                                                     "decimal_lower_informational": display(cglo),
                                                     "decimal_upper_informational": display(cghi)},
            "proves_infinite_euler_products": False, "proves_infinite_perron_shift": False,
            "proves_conditional_weighted_prefix": False,
            "proves_classical_zeta_fourth_mean": False, "proves_complete_fourth_moment_bound": False,
            "proves_new_zero_proportion": False, "proves_new_zero_free_boundary": False,
            "proves_riemann_hypothesis": False}


def main() -> None:
    if not __debug__:
        raise RuntimeError("Optimized mode is not supported")
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = replay()
    encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)+"\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
    elif OUTPUT.read_text(encoding="utf-8") != encoded:
        raise RuntimeError("Saved finite output differs")
    print(f"PASS: {result['check_count']} finite checks; analytic proofs are separate")


if __name__ == "__main__":
    main()

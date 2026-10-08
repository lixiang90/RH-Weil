"""Replay finite rational costs and root enclosures, not analytic estimates."""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-double-perron-checkpoint.json"
INPUTS = {
    "notes/484-original-double-perron-conditional-remainder.md":
        "38c94314687ccddf1cda08b2d7611c0e1409927b0fb62fdfb0760b32256d1cad",
    "reviews/2026-10-08/hybrid-original-double-log-derivative-perron-research-checkpoint-audit.md":
        "8673c02894a1503a8e4bb9e25bfe1c693347ddfc1f5acb070b55a64b3c275b27",
    "reviews/2026-10-08/hybrid-original-double-log-derivative-perron-review-peer.md":
        "1f05daa4c005b8e8363f985d31468188e312b1615fff2f1123bb227646a66f02",
    "notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md":
        "17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487",
    "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md":
        "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
}


def canonical(path: Path) -> bytes:
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha(path: Path) -> str:
    return hashlib.sha256(canonical(path)).hexdigest()


def display(value: Q) -> str:
    with localcontext() as context:
        context.prec = 60
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def enclosure(lo: Q, hi: Q) -> dict:
    if not lo <= hi:
        raise RuntimeError("Invalid enclosure")
    return {
        "rational_lower": str(lo), "rational_upper": str(hi),
        "decimal_lower_informational": display(lo),
        "decimal_upper_informational": display(hi),
    }


def replay() -> dict:
    checks: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            raise RuntimeError(f"Failed finite check: {name}")
        checks.append(name)

    for name, expected in INPUTS.items():
        check(f"frozen input: {name}", sha(ROOT / name) == expected)

    theta = Q(7, 8)
    v, a, y = Q(8, 75), Q(16, 75), Q(59, 75)

    def costs(t: Q, vv: Q, aa: Q, yy: Q) -> list[Q]:
        return [2 * yy - 1, Q(1, 3) + 2 * vv,
                Q(1, 3) + (2 * t - 1) * (aa + vv),
                1 - 2 * aa, 1 - 4 * vv, Q(0)]

    nominal = costs(theta, v, a, y)
    check("7/8 complete cost vector", nominal ==
          [Q(43, 75), Q(41, 75), Q(43, 75), Q(43, 75), Q(43, 75), Q(0)])
    check("7/8 general parameter guards",
          0 < v < a and v < Q(1, 4) and max(Q(1, 2), a + v) < y < 1)
    c = max(nominal)
    whole = Q(5, 7)
    transfer = (3 * whole + c) / 4
    check("complete transfer 713/1050", transfer == Q(713, 1050))
    check("complete transfer margin 37/1050", whole - transfer == Q(37, 1050))
    check("482 error saving 64/2025", Q(49, 81) - c == Q(64, 2025))
    check("482 transfer saving 16/2025", Q(779, 1134) - transfer == Q(16, 2025))
    check("481 error saving 8/175", Q(13, 21) - c == Q(8, 175))
    check("481 transfer saving 2/175", Q(29, 42) - transfer == Q(2, 175))
    check("fixed 482 full prime band cost",
          Q(1, 3) + Q(3, 4) * (Q(64, 243) + Q(8, 81)) == Q(49, 81))
    check("fixed 482 cutoff width", Q(64, 243) - Q(16, 81) == Q(16, 243))

    branch_examples = []
    for t in (Q(1, 2), Q(3, 4), Q(5, 6), theta, Q(19, 20)):
        if t <= Q(5, 6):
            vv, aa, yy = Q(1, 9), Q(2, 9), Q(7, 9)
        else:
            den = 18 * t + 3
            vv, aa, yy = 2 / den, 4 / den, (18 * t - 1) / den
        family_c = max(Q(5, 9), (18 * t - 5) / (18 * t + 3))
        values = costs(t, vv, aa, yy)
        check(f"finite branch example theta={t}", max(values) == family_c)
        branch_examples.append({"theta": str(t), "v": str(vv), "a": str(aa),
                                "y": str(yy), "costs": list(map(str, values)),
                                "maximum": str(family_c)})
    check("exact branch junction", (18 * Q(5, 6) - 5) / (18 * Q(5, 6) + 3) == Q(5, 9))

    elo = Q(16683858898627, 10**14)
    ehi = Q(16683858898628, 10**14)

    def polynomial(e: Q) -> Q:
        return 657 * e**3 - 954 * e**2 + 21 * e + 20

    check("451 polynomial endpoint signs", polynomial(elo) > 0 > polynomial(ehi))
    derivative_upper = 1971 * ehi**2 - 1908 * elo + 21
    check("451 derivative strictly negative on root interval", derivative_upper < 0)
    tlo, thi = Q(11, 12) - ehi / 4, Q(11, 12) - elo / 4
    check("existing boundary lies in both analytic parameter domains",
          Q(5, 6) < tlo < thi < Q(7, 8))

    def error(t: Q) -> Q:
        return (18 * t - 5) / (18 * t + 3)

    def density_whole(t: Q) -> Q:
        return 4 * t - 3 + 3 * (1 - t) / (2 * t)

    def gamma(t: Q) -> Q:
        return (3 * density_whole(t) + error(t)) / 4

    clo, chi = error(tlo), error(thi)
    blo, bhi = density_whole(tlo), density_whole(thi)
    glo, ghi = gamma(tlo), gamma(thi)
    check("error monotonicity denominator positive", 18 * tlo + 3 > 0)
    check("density derivative positive on entire interval", 4 - Q(3, 2) / tlo**2 > 0)
    check("strict error decimal envelope",
          Q("0.5733157277613751") < clo < chi < Q("0.5733157277613762"))
    check("strict transfer decimal envelope",
          Q("0.6789774341551112") < glo < ghi < Q("0.6789774341551154"))
    check("error strictly below inherited whole bound", chi < blo)
    check("stronger existing-boundary application", chi < c and ghi < transfer)

    vlo, vhi = 2 / (18 * thi + 3), 2 / (18 * tlo + 3)
    alo, ahi = 2 * vlo, 2 * vhi
    ylo, yhi = (1 + clo) / 2, (1 + chi) / 2
    check("algebraic parameter guards on entire interval",
          0 < vlo <= vhi < Q(1, 4) and vhi < alo and ahi + vhi < ylo and
          Q(1, 2) < ylo < yhi < 1)
    check("algebraic error formula in e",
          error(tlo) == (23 - 9 * ehi) / (39 - 9 * ehi) and
          error(thi) == (23 - 9 * elo) / (39 - 9 * elo))

    return {
        "schema": "rh-weil-double-perron-finite-checkpoint-v1",
        "status": "PASS",
        "baseline_commit": "fdf86cb439a6c5df8ca0a8e8a526b2b9d177d286",
        "input_canonical_lf_sha256": INPUTS,
        "script_canonical_lf_sha256": sha(Path(__file__)),
        "check_count": len(checks), "checks": checks,
        "nominal_7_8": {"v": str(v), "a": str(a), "y": str(y),
                        "costs": list(map(str, nominal)), "error": str(c),
                        "inherited_whole": str(whole), "transfer": str(transfer)},
        "finite_branch_examples_only": branch_examples,
        "existing_cubic_boundary": {
            "e": enclosure(elo, ehi),
            "polynomial_at_lower": str(polynomial(elo)),
            "polynomial_at_upper": str(polynomial(ehi)),
            "derivative_upper": str(derivative_upper),
            "theta": enclosure(tlo, thi), "v": enclosure(vlo, vhi),
            "a": enclosure(alo, ahi), "y": enclosure(ylo, yhi),
            "error": enclosure(clo, chi),
            "inherited_whole": enclosure(blo, bhi),
            "transfer": enclosure(glo, ghi),
        },
        "proves_infinite_perron_estimates": False,
        "proves_zero_free_input": False,
        "proves_actual_mobius_cancellation": False,
        "proves_complete_fourth_moment_bound": False,
        "proves_new_zero_proportion": False,
        "proves_new_zero_free_boundary": False,
        "proves_riemann_hypothesis": False,
    }


def main() -> None:
    if not __debug__:
        raise SystemExit("Python -O is not admitted for this finite checkpoint")
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = replay()
    data = (json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if args.write:
        OUTPUT.write_bytes(data)
        print(f"PASS: {result['check_count']} finite checks; saved output written")
    else:
        if not OUTPUT.is_file() or canonical(OUTPUT) != data:
            raise SystemExit("Saved finite checkpoint does not match this replay")
        print(f"PASS: {result['check_count']} finite checks; saved output matches")


if __name__ == "__main__":
    main()

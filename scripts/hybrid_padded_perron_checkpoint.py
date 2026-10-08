"""Check finite costs and existing root enclosures, not infinite estimates."""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-padded-perron-checkpoint.json"
INPUTS = {
    "notes/486-original-padded-perron-fourth-mean-remainder.md":
        "5e98058d6d47545aedb98b6e70f66f4e11a904b623351903e3846e01bbe7eaf7",
    "reviews/2026-10-08/hybrid-original-extended-inner-zeta-fourth-perron-research-perron.md":
        "54d39f22b370be40a780fac6fe80968e24c014fc48d1156ab87248d5310a2549",
    "reviews/2026-10-08/hybrid-original-extended-inner-zeta-fourth-perron-review-peer.md":
        "ac4ae783ce662b5584047b22e475fb5d20ea3381b26d5227e3827687bf05e1b2",
    "notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md":
        "17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487",
    "notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md":
        "179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6",
    "notes/484-original-double-perron-conditional-remainder.md":
        "38c94314687ccddf1cda08b2d7611c0e1409927b0fb62fdfb0760b32256d1cad",
}


def sha(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def display(value: Q) -> str:
    with localcontext() as context:
        context.prec = 60
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def enclosure(lo: Q, hi: Q) -> dict:
    if lo > hi:
        raise RuntimeError("Invalid enclosure")
    return {"rational_lower": str(lo), "rational_upper": str(hi),
            "decimal_lower_informational": display(lo),
            "decimal_upper_informational": display(hi)}


def costs(theta: Q, v: Q, a: Q, y: Q) -> list[Q]:
    return [2*y-1, 4*v, 2*(2*theta-1)*(a+v), 1-2*a, 1-4*v, Q(0)]


def guards(v: Q, a: Q, y: Q) -> bool:
    return 0 < v < a and v < Q(1, 4) and max(Q(1, 2), a+v) < y < 1


def replay() -> dict:
    checks: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            raise RuntimeError(f"Failed finite check: {name}")
        checks.append(name)

    for name, expected in INPUTS.items():
        check(f"frozen input: {name}", sha(ROOT / name) == expected)
    theta, v, a, y = Q(7, 8), Q(2, 17), Q(4, 17), Q(13, 17)
    c, b, gamma = Q(9, 17), Q(5, 7), Q(159, 238)
    vector = costs(theta, v, a, y)
    check("nominal complete costs", vector == [c, Q(8, 17), c, c, c, Q(0)])
    check("nominal guards and a=2v", guards(v, a, y) and a == 2*v)
    check("complete transfer 159/238", (3*b+c)/4 == gamma)
    check("transfer margin 11/238", b-gamma == Q(11, 238))
    check("484 error saving", Q(43, 75)-c == Q(56, 1275))
    check("484 transfer saving", Q(713, 1050)-gamma == Q(14, 1275))
    uvector = costs(Q(1), Q(1, 10), Q(1, 5), Q(4, 5))
    check("unconditional trivial-factor costs", uvector ==
          [Q(3, 5), Q(2, 5), Q(3, 5), Q(3, 5), Q(3, 5), Q(0)])
    check("unconditional parameter guards", guards(Q(1, 10), Q(1, 5), Q(4, 5)))
    check("unconditional 481 saving", Q(13, 21)-Q(3, 5) == Q(2, 105))
    examples = []
    for th in [Q(1, 2), Q(3, 4), Q(5, 6), Q(7, 8), Q(19, 20)]:
        beta = 2*th-1
        cc = max(Q(1, 2), 3*beta/(2+3*beta))
        if th <= Q(5, 6):
            vv, aa, yy = Q(1, 8), Q(1, 4), Q(3, 4)
        else:
            vv, aa = 1/(2*(6*th-1)), 1/(6*th-1)
            yy = (6*th-2)/(6*th-1)
        cv = costs(th, vv, aa, yy)
        check(f"finite branch example theta={th}", max(cv) == cc and guards(vv, aa, yy))
        examples.append({"theta": str(th), "v": str(vv), "a": str(aa),
                         "y": str(yy), "costs": list(map(str, cv)), "maximum": str(cc)})
    check("branch junction", (6*Q(5, 6)-3)/(6*Q(5, 6)-1) == Q(1, 2))
    check("fixed 484 prime band", Q(3, 2)*(Q(62, 225)+Q(8, 75)) == Q(43, 75))
    check("fixed 482 prime band", Q(3, 2)*(Q(74, 243)+Q(8, 81)) == Q(49, 81))
    check("fixed band widths", Q(62, 225)-Q(16, 75) == Q(14, 225) and
          Q(74, 243)-Q(16, 81) == Q(26, 243))
    check("fixed band guards", guards(Q(8, 75), Q(62, 225), Q(59, 75)) and
          guards(Q(8, 81), Q(74, 243), Q(65, 81)))
    elo, ehi = Q(16683858898627, 10**14), Q(16683858898628, 10**14)
    poly = lambda e: 657*e**3-954*e**2+21*e+20
    deriv = lambda e: 1971*e**2-1908*e+21
    check("451 cubic signs", poly(elo) > 0 > poly(ehi))
    check("451 cubic strictly decreasing on root interval",
          3942*ehi-1908 < 0 and deriv(elo) < 0)
    tlo, thi = Q(11, 12)-ehi/4, Q(11, 12)-elo/4
    cfun = lambda th: (6*th-3)/(6*th-1)
    bfun = lambda th: 4*th-3+3*(1-th)/(2*th)
    clo, chi = cfun(tlo), cfun(thi)
    blo, bhi = bfun(tlo), bfun(thi)
    glo, ghi = (3*blo+clo)/4, (3*bhi+chi)/4
    check("existing boundary in both analytic domains", Q(5, 6) < tlo < thi < Q(7, 8))
    check("error monotonicity denominator positive", 6*tlo-1 > 0)
    check("density derivative positive throughout interval", 4-Q(3, 2)/tlo**2 > 0)
    check("error formula in e", clo == (5-3*ehi)/(9-3*ehi) and
          chi == (5-3*elo)/(9-3*elo))
    check("strict error decimal envelope", Q(".5293832084010138") < clo <= chi <
          Q(".5293832084010156"))
    check("strict transfer decimal envelope", Q(".6679943043150209") < glo <= ghi <
          Q(".6679943043150252"))
    check("error strictly below inherited whole", chi < blo)
    check("stronger existing-boundary application", chi < c and ghi < gamma)
    vlo, vhi = 1/(9-3*elo), 1/(9-3*ehi)
    ylo, yhi = (7-3*ehi)/(9-3*ehi), (7-3*elo)/(9-3*elo)
    check("parameter guards on entire root interval",
          0 < vlo <= vhi < Q(1, 4) and max(Q(1, 2), 3*vhi) < ylo <= yhi < 1)
    return {
        "schema": "rh-weil-padded-perron-finite-checkpoint-v1", "status": "PASS",
        "baseline_commit": "e51a51e2225c9216b23cc7b12bc97e8fa8cf2ea1",
        "check_count": len(checks), "checks": checks,
        "input_canonical_lf_sha256": INPUTS,
        "script_canonical_lf_sha256": sha(Path(__file__)),
        "nominal_7_8": {"costs": list(map(str, vector)), "error": str(c),
                         "transfer": str(gamma), "v": str(v), "a": str(a), "y": str(y)},
        "unconditional_trivial_factors": {"costs": list(map(str, uvector)),
                                           "error": "3/5", "uses_zero_free_input": False},
        "finite_branch_examples_only": examples,
        "existing_cubic_boundary": {"e": enclosure(elo, ehi), "theta": enclosure(tlo, thi),
                                    "error": enclosure(clo, chi), "inherited_whole": enclosure(blo, bhi),
                                    "transfer": enclosure(glo, ghi), "v": enclosure(vlo, vhi),
                                    "a": enclosure(2*vlo, 2*vhi), "y": enclosure(ylo, yhi)},
        "proves_infinite_perron_estimates": False, "proves_classical_zeta_fourth_mean": False,
        "proves_actual_mobius_cancellation": False, "proves_zero_free_input": False,
        "proves_complete_fourth_moment_bound": False, "proves_new_zero_proportion": False,
        "proves_new_zero_free_boundary": False, "proves_riemann_hypothesis": False,
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("Optimized mode is not supported")
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = replay()
    encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
    elif OUTPUT.read_text(encoding="utf-8") != encoded:
        raise RuntimeError("Saved finite output differs")
    print(f"PASS: {result['check_count']} finite checks; saved output matches" if args.check
          else f"PASS: wrote {result['check_count']} finite checks; analytic proofs are separate")


if __name__ == "__main__":
    main()

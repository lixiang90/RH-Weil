"""Reproduce Franklin's exact single-point exclusion of the round-0 h."""

from bisect import bisect_right
from decimal import Decimal
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path

from periodic_window_quadratic_certificate import SCALE, asiv, sinc_iv, pi_iv

ROOT = Path(__file__).resolve().parents[1]


def main():
    snapshot = ROOT / "reviews/2026-09-08/radius-five-interpolated-subaction.json"
    raw = snapshot.read_bytes()
    data = json.loads(raw, parse_float=Decimal)
    round0 = data["history"][0]
    grid, h = list(map(F, data["grid"])), list(map(F, round0["h"]))
    assert len(h) == len(grid)**4 and all(0 <= x <= F(1, 100) for x in h)
    cut = min(round0["cuts"], key=lambda x: F(x["residual"]))
    g = list(map(F, cut["gaps"]))

    def interpolate(state):
        left = [min(max(bisect_right(grid, x)-1, 0), len(grid)-2) for x in state]
        fraction = [(x-grid[l])/(grid[l+1]-grid[l]) for x, l in zip(state, left)]
        assert all(0 <= x <= 1 for x in fraction)
        total = F(0)
        for bits in product((0, 1), repeat=4):
            index, weight = 0, F(1)
            for l, v, bit in zip(left, fraction, bits):
                index = index*len(grid)+l+bit
                weight *= v if bit else 1-v
            total += h[index]*weight
        return total

    proposal = json.loads((ROOT / "reviews/2026-09-08/radius-five-rational-profile-candidate.json").read_text())
    t = [asiv(F(v["t"])) for v in proposal["terms"]]
    y = [asiv(F(v["y"])) for v in proposal["terms"]]
    a = asiv(2).sqrt()
    ma = sinc_iv(a)
    z = [yy*x.square()/(x.square()-2) for x, yy in zip(t, y)]
    A = 1-sum((zz*sinc_iv(x) for x, zz in zip(t, z)), asiv(0))

    def kernel(x):
        x = asiv(x)
        base = (sinc_iv(x-a)+sinc_iv(x+a))/(2*ma)
        return A*base+sum((zz*(sinc_iv(x-u)+sinc_iv(x+u))/2
                          for u, zz in zip(t, z)), asiv(0))

    prefix, current = [], F(0)
    for x in g:
        current += x
        prefix.append(current)
    residual = (2*sum((kernel(x).square() for x in prefix), asiv(0))
                +asiv(F(proposal["eta"]))*asiv(g[0])/(2*pi_iv())
                -asiv(F(proposal["alpha"]))
                +asiv(interpolate(g[1:])-interpolate(g[:4])))
    assert F("-.004787546377") < F(residual.lo, SCALE) <= F(residual.hi, SCALE) < F("-.004787546376")
    payment = F(proposal["eta"])*F("29.2")*F(7, 44)-F(proposal["alpha"])-F(1, 100)
    assert payment == F(39781, 2200000000) > 0
    output = dict(status="PASS: this fixed interpolant has a strictly negative point",
                  snapshot_sha256=hashlib.sha256(raw).hexdigest(),
                  candidate_iteration=round0["iteration"],
                  exact_decimal_cut=[str(x) for x in g],
                  residual=residual.report(),
                  strict_enclosure=["-.004787546377", "-.004787546376"],
                  all_snapshot_node_heights_in_0_to_001=True,
                  first_gap_payment_margin=str(payment),
                  scope="Excludes one saved h only; no method-wide impossibility or actual zero conclusion")
    (ROOT / "reviews/2026-09-08/subaction-interpolant-counterexample.json").write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print("PASS: -.004787546377 < residual < -.004787546376; this h fails.")


if __name__ == "__main__":
    main()

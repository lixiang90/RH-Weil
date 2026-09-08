"""Exact-input Arb evaluation of every continuation plan at saved points."""

from functools import cache
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from radius_five_arb_kernel import Kernel, PROFILE_SHA256, arb, rational, rational_bounds

ROOT = Path(__file__).resolve().parents[1]


class PointCertificate:
    def __init__(self, candidate):
        self.kernel = Kernel(192)
        assert candidate["profile_sha256"] == PROFILE_SHA256
        self.alpha, self.eta, self.delta = [F(candidate[k]) for k in ("alpha", "eta", "delta")]
        self.plans = [(tuple(map(F, p["gaps"])), F(p["offset"])) for p in candidate["plans"]]
        assert self.plans[0] == ((), F(0))
        assert all(len(w) <= 4 for w, _ in self.plans)
        self.query_count = 0

    @cache
    def energy(self, x):
        self.query_count += 1
        k = self.kernel.value(x)
        return 2*k*k

    @cache
    def loss(self, word):
        assert len(word) == 5
        prefix, value = F(0), rational(self.eta*word[0])/(2*arb.pi())-rational(self.alpha+self.delta)
        for x in word:
            prefix += x
            value += self.energy(prefix)
        return value

    def height_bounds(self, state):
        endpoints = []
        for word, offset in self.plans:
            joined = state+word
            value = rational(offset)
            for i in range(len(word)):
                value += self.loss(joined[i:i+5])
            endpoints.append(rational_bounds(value))
        lower = min(lo for lo, hi in endpoints)
        upper = min(hi for lo, hi in endpoints)
        selected = min(range(len(endpoints)), key=lambda i: endpoints[i][1])
        return lower, upper, selected

    def residual_bounds(self, word):
        head_lo, head_hi, head_id = self.height_bounds(word[:4])
        tail_lo, tail_hi, tail_id = self.height_bounds(word[1:])
        cost_lo, cost_hi = rational_bounds(self.loss(word)+rational(self.delta))
        return (cost_lo+tail_lo-head_hi, cost_hi+tail_hi-head_lo,
                dict(head_plan_upper=head_id, tail_plan_upper=tail_id))


def main():
    folder = ROOT / "reviews/2026-09-08"
    source = folder / "radius-five-continuation-plans-266.json"
    raw = source.read_bytes()
    data = json.loads(raw)
    search_path = source.with_name(source.stem+"-continuous-pressure.json")
    search_raw = search_path.read_bytes()
    search = json.loads(search_raw)
    assert search["candidate_sha256"] == hashlib.sha256(raw).hexdigest()
    cert = PointCertificate(data)
    records = []
    for point in search["searches"]:
        if point["all_plan_original_kernel_residual"] >= 0:
            continue
        word = tuple(map(F, point["word"]))
        assert all(F("5.7") <= x <= 128 for x in word)
        lo, hi, ids = cert.residual_bounds(word)
        assert hi < 0
        records.append(dict(word=[str(x) for x in word],
                            lower=str(lo), upper=str(hi), **ids))
        unit = 10**15
        # Expand strictly to readable rational decimal-grid endpoints.
        display_lo = F(lo.numerator*unit//lo.denominator-1, unit)
        display_hi = F(-((-hi.numerator*unit)//hi.denominator)+1, unit)
        assert display_lo < lo <= hi < display_hi < 0
        print(f"Strict negative: {display_lo} < R < {display_hi}", flush=True)
    assert records
    output = dict(status="PASS: strict counterexamples to the frozen 266-plan continuous subaction",
                  candidate_sha256=hashlib.sha256(raw).hexdigest(),
                  search_sha256=hashlib.sha256(search_raw).hexdigest(),
                  profile_sha256=PROFILE_SHA256, plans=len(cert.plans), bits=192,
                  arithmetic_script_sha256=hashlib.sha256((ROOT/"scripts/radius_five_arb_kernel.py").read_bytes()).hexdigest(),
                  records=records, distinct_scalar_queries=cert.query_count,
                  scope="Only this frozen candidate is excluded; its exact finite-alphabet positivity remains valid.")
    (folder / "continuation-point-counterexamples.json").write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()

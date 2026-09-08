"""Exact height and reset payment only; does not verify a subaction."""

from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path

from periodic_window_quadratic_certificate import pi_iv, SCALE

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", default="radius-five-continuation-plans-32.json")
    args = parser.parse_args()
    assert Path(args.candidate).name == args.candidate
    path = ROOT / "reviews/2026-09-08" / args.candidate
    raw = path.read_bytes()
    candidate = json.loads(raw)
    alpha, eta, delta = [F(candidate[k]) for k in ("alpha", "eta", "delta")]
    a, B = map(F, candidate["domain"])
    H = F(candidate["requested_height_bound"])
    profile = json.loads((path.parent / candidate["profile_source"]).read_text())
    assert alpha == F(profile["alpha"]) and eta == F(profile["eta"])
    assert 0 < alpha < 1 and eta > 0 and delta > 0 and a == F("5.7") and B == 128
    assert pi_iv().hi*7 < 22*SCALE
    upper_D = alpha+delta-eta*a*F(7, 44)
    assert upper_D > 0
    plans = candidate["plans"]
    assert plans[0] == {"gaps": [], "offset": "0.0"}
    height = F(0)
    for item in plans:
        gaps, b = list(map(F, item["gaps"])), F(item["offset"])
        assert len(gaps) <= 4 and all(a <= g <= B for g in gaps)
        height = max(height, len(gaps)*upper_D-b)
    assert height < H == F(23, 1000)
    C = 5*alpha+H
    payment = eta*B*F(7, 44)-C
    assert payment == F(894851, 55000000) > 0
    output = dict(status="PASS: finite candidate height and large-gap payment only",
                  candidate_sha256=hashlib.sha256(raw).hexdigest(), plans=len(plans),
                  upper_D=str(upper_D), certified_height_upper=str(height),
                  strict_height_bound=str(H), reset_threshold=str(B),
                  endpoint_cost=str(C), strict_payment_lower=str(payment),
                  proof="Each L>=-(alpha+delta-eta*a/(2*pi)); each m-step plan>=b-mD; h is the minimum with zero.",
                  open_input="The five-gap subaction inequality on [5.7,128]^5 is not proved.")
    filename = ("continuation-plan-height-certificate.json" if args.candidate == "radius-five-continuation-plans-32.json"
                else path.stem+"-height.json")
    (path.parent / filename).write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {len(plans)} plans, height < {H}, reset payment > {payment}.")
    print("OPEN: global subaction inequality.")


if __name__ == "__main__":
    main()

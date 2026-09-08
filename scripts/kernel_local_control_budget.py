"""Refine the same control mesh using local one-body curvature.

All future-word entries must belong to the already fixed control alphabet.
No endpoint inequalities or final offset bounds are established here.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from radius_five_arb_kernel import Kernel, rational, rational_bounds, radius_ball

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = ROOT / "reviews/2026-09-08/kernel-curvature-tail-table.json"
    raw = source.read_bytes()
    data = json.loads(raw)
    kernel = Kernel(192)
    a, end, step = map(F, [data["a"],data["end"],data["step"]])
    A = min(map(F,data["control_nodes"]))
    scale = int(data["integer_denominator"])
    suffix = list(data["f_second_upper_numerators"])
    tail_constant = F(data["f_second_tail_constant"])
    tail_bound = F(data["f_second_tail_bound_at_end"])
    carry = -((-tail_bound.numerator*scale)//tail_bound.denominator)
    for i in range(len(suffix)-1,-1,-1):
        carry = max(carry,suffix[i])
        suffix[i] = carry

    def U(x):
        if x >= end:
            return min(F(2),tail_constant/x**2)
        return F(suffix[int((x-a)//step)],scale)

    records = []
    for cell in data["control_cells"]:
        left,right,parts = F(cell["left"]),F(cell["right"]),cell["parts"]
        width = (right-left)/parts
        for segment in range(parts):
            u,v = left+segment*width,left+(segment+1)*width
            ball = rational((u+v)/2)+radius_ball(rational(width/2))
            local = rational_bounds(kernel.energy_jet(ball)[2])[1]
            # Last anchor: f(z) is local; the other four shifts contain only
            # controlled future gaps, hence at least j*A.
            M = local+sum(U(u+j*A) for j in range(1,5))
            # Four original anchors: j future gaps and 5-i original gaps.
            M += sum(U(u+(5-i)*a+j*A) for j in range(4) for i in range(j+1,5))
            M = max(F(0),M)
            records.append(dict(left=str(u),right=str(v),one_body_second_upper=str(local),
                                M_upper=str(M),payment=str(M*width**2/8)))
    maximum = max(F(record["payment"]) for record in records)
    delta = F(data["delta"])
    output = dict(status="Refined continuous-control curvature budget only; endpoint closure unproved",
                  table_sha256=hashlib.sha256(raw).hexdigest(),
                  future_gap_minimum=str(A),original_gap_minimum=str(a),
                  segment_count=len(records),records=records,
                  maximum_curvature_payment=str(maximum),
                  available_endpoint_loss=str(delta-maximum),
                  additional_loss_above_delta_half=str(delta/2-maximum),
                  scope="Same 313 nodes and 310 intervals. Requires every future word to use this control alphabet and the original table offset-floor/pressure hypotheses.")
    source.with_name("kernel-local-control-budget.json").write_text(
        json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(f"310-segment maximum curvature payment {float(maximum):.12g}; "
          f"available endpoint loss {float(delta-maximum):.12g}",flush=True)


if __name__ == "__main__":
    main()

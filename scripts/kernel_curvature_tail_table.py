"""Arb upper table for positive f'' on the whole ray, plus control pilot.

This arithmetic table does not certify the finite-word closure in note361.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from radius_five_arb_kernel import Kernel, PROFILE_SHA256, arb, rational, rational_bounds, radius_ball

ROOT = Path(__file__).resolve().parents[1]
SCALE = 10**12


def ceil_scaled(x):
    return -((-x.numerator*SCALE)//x.denominator)


def upper(x):
    return rational_bounds(x)[1]


def main():
    kernel = Kernel(192)
    a, end, step = F("5.7"), F(640), F("0.05")
    alpha, eta, delta, b_floor = F(".007535"), F(".00377855"), F(".00001"), F("-.007")
    # p(u)=A*cos(sqrt(2)*u)/m(sqrt(2))+sum z*cos(t*u).
    # These uniform bounds imply integration-by-parts derivative tails.
    p_bound = abs(kernel.A)/kernel.ma+sum((abs(z) for z in kernel.z), arb(0))
    p_prime_bound = abs(kernel.A)*kernel.a/kernel.ma+sum(
        (abs(z)*t for z, t in zip(kernel.z, kernel.t)), arb(0))
    P, Q = upper(p_bound), upper(p_prime_bound)
    D0, D1, D2 = 2*P+Q, P+1+Q/2, P/2+1+Q/4
    tail_constant = 4*(D1*D1+D0*D2)
    tail_upper = min(F(2), tail_constant/end**2)
    n = int((end-a)/step)
    assert a+n*step == end
    cells, pressure = [], []
    start = time.perf_counter()
    for i in range(n):
        left, right = a+i*step, a+(i+1)*step
        ball = rational((left+right)/2)+radius_ball(rational(step/2))
        f, _, f_second = kernel.energy_jet(ball)
        bound = min(2*SCALE, max(0, ceil_scaled(upper(f_second))))
        cells.append(bound)
        if right <= 25:
            fee = rational(eta*left)/(2*arb.pi())-rational(alpha+delta)+rational(b_floor)
            f_lower = max(F(0), rational_bounds(f)[0])
            lower = rational_bounds(fee)[0]+f_lower
            pressure.append(dict(left=str(left), right=str(right),
                                 lower=str(lower), excluded=lower >= 0))
        if (i+1) % 2000 == 0:
            print(f"closed curvature cells {i+1}/{n}", flush=True)
    suffix = [0]*n
    current = ceil_scaled(tail_upper)
    for i in range(n-1, -1, -1):
        current = max(current, cells[i])
        suffix[i] = current

    def U(x):
        if x >= end:
            return min(F(2), tail_constant/x**2)
        index = int((x-a)//step)
        assert 0 <= index < n
        return F(suffix[index], SCALE)

    control_cells, nodes = [], set()
    for record in pressure:
        if record["excluded"]:
            continue
        left, right = F(record["left"]), F(record["right"])
        M = sum(r*U(left+(r-1)*a) for r in range(1,6))
        parts = 1
        # Reserve delta/2 for finite endpoint closure losses.
        while M*((right-left)/parts)**2/8 > delta/2:
            parts *= 2
        control_cells.append(dict(left=str(left), right=str(right), M_upper=str(M),
                                  parts=parts,
                                  curvature_payment=str(M*((right-left)/parts)**2/8)))
        nodes.update(left+(right-left)*F(j,parts) for j in range(parts+1))
    infinite_pressure = rational(eta*25)/(2*arb.pi())-rational(alpha+delta)+rational(b_floor)
    assert rational_bounds(infinite_pressure)[0] > 0
    output = dict(status="Closed-cell f'' upper table and conditional control mesh; closure not certified",
                  profile_sha256=PROFILE_SHA256, bits=192, a=str(a), end=str(end), step=str(step),
                  integer_denominator=str(SCALE), f_second_upper_numerators=cells,
                  density_bounds=dict(p_upper=str(P), derivative_upper=str(Q)),
                  derivative_tail_constants=[str(D0),str(D1),str(D2)],
                  f_second_tail_constant=str(tail_constant),
                  f_second_tail_bound_at_end=str(tail_upper),
                  tail_proof="|k^(j)(x)|<=D_j/x by integration by parts; f''<=4(D_1^2+D_0*D_2)/x^2",
                  alpha=str(alpha), eta=str(eta), delta=str(delta), offset_floor=str(b_floor),
                  pressure_cells=pressure, control_cells=control_cells,
                  control_nodes=[str(x) for x in sorted(nodes)],
                  control_node_count=len(nodes), excluded_pressure_cells=sum(v["excluded"] for v in pressure),
                  infinite_pressure_lower=str(rational_bounds(infinite_pressure)[0]),
                  elapsed_seconds=time.perf_counter()-start,
                  arithmetic_script_sha256=hashlib.sha256((ROOT/"scripts/radius_five_arb_kernel.py").read_bytes()).hexdigest(),
                  scope="Mesh sufficient only if every exact branch has b>=offset_floor and all required endpoint closures hold with e<=delta/2.")
    path = ROOT / "reviews/2026-09-08/kernel-curvature-tail-table.json"
    path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(f"PASS arithmetic: {n} closed cells, {len(nodes)} control nodes; "
          f"{output['excluded_pressure_cells']} scalar cells excluded.", flush=True)


if __name__ == "__main__":
    main()

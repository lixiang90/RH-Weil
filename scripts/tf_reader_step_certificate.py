"""Certified physical step approximation of F 1_[1,2].

The primitive is actually evaluated; it is not a q0/T_F computation.
All certificate arithmetic is rational or outward fixed-point integer arithmetic.
The result is a finite dyadic step function with rational coefficients.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from math import factorial
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter

from tf_reader_arch_gap_certificate import Intervals, atan_interval


def power2(k: int) -> F:
    return F(2**k) if k >= 0 else F(1, 2**(-k))


def floor_log2(x: F) -> int:
    k = x.numerator.bit_length()-x.denominator.bit_length()
    while power2(k) > x:
        k -= 1
    while power2(k+1) <= x:
        k += 1
    return k


def ceil_log2(x: F) -> int:
    k = floor_log2(x)
    return k if power2(k) == x else k+1


def plan(tolerance: F):
    if not 0 < tolerance < 1:
        raise ValueError("Use a rational tolerance strictly between zero and one")
    eps2 = tolerance**2
    # 4*delta <= eps²/8; using pi>3, 4/(pi² X)<=4/(9X)<=eps²/8.
    kmin = floor_log2(eps2/32)
    kmax = ceil_log2(F(32, 9)/eps2)
    count = kmax-kmin
    band_budget = eps2/(2*count)
    bands = []
    mesh_total = F(0)
    for k in range(kmin, kmax):
        a = power2(k)
        derivative = F(19) if k < 0 else F(7)/a
        cells = 1
        while derivative**2*a**3/(12*cells**2) > band_budget:
            cells *= 2
        mesh = derivative**2*a**3/(12*cells**2)
        mesh_total += mesh
        bands.append({"k": k, "left": str(a), "right": str(2*a),
                      "cells": cells, "derivative_upper": str(derivative),
                      "midpoint_L2_error_squared_upper": str(mesh)})
    return {"tolerance": str(tolerance), "delta": str(power2(kmin)),
            "X": str(power2(kmax)), "band_count": count,
            "cells": sum(b["cells"] for b in bands),
            "near_zero_L2_error_squared_upper": str(4*power2(kmin)),
            "far_tail_L2_error_squared_upper": str(F(4, 9)/power2(kmax)),
            "midpoint_L2_error_squared_upper": str(mesh_total), "bands": bands}


class CertifiedSine:
    def __init__(self, precision: int = 30, degree: int = 14):
        self.arithmetic = Intervals(precision)
        ar5, ar239 = atan_interval(5, 100), atan_interval(239, 100)
        lo, hi = 16*ar5[0]-4*ar239[1], 16*ar5[1]-4*ar239[0]
        if not F(3) < lo < hi < F(19, 6):
            raise ArithmeticError("Pi enclosure does not certify derivative constants")
        self.pi = self.arithmetic.enclose(lo, hi)
        self.two_pi = self.arithmetic.add(self.pi, self.pi)
        self.degree = degree
        self.coefficients = [self.arithmetic.enclose(F((-1)**j, factorial(2*j+1)))
                             for j in range(degree+1)]
        pi_upper = F(self.pi[1], self.arithmetic.unit)
        # Taylor polynomial through degree2d+2 (even term zero), next remainder.
        self.remainder = self.arithmetic.enclose(
            pi_upper**(2*degree+3)/factorial(2*degree+3))[1]
        for point, exact in [(F(0), 0), (F(1, 4), 1), (F(1, 2), 0),
                             (F(3, 4), -1), (F(-1, 4), -1)]:
            low, high = self.sin_two_pi(point)
            if not low <= exact*self.arithmetic.unit <= high:
                raise ArithmeticError("Known sine value not enclosed")

    def sin_two_pi(self, x: F):
        # Exact rational period reduction, so actual angle is in [-pi,pi].
        reduced = x-((x+F(1, 2)).numerator//(x+F(1, 2)).denominator)
        a = self.arithmetic
        angle = a.mul(self.two_pi, a.enclose(reduced))
        square = a.mul(angle, angle)
        value = self.coefficients[-1]
        for coefficient in reversed(self.coefficients[:-1]):
            value = a.add(a.mul(value, square), coefficient)
        value = a.mul(angle, value)
        return (max(-a.unit, value[0]-self.remainder),
                min(a.unit, value[1]+self.remainder))

    def fourier_steps(self, x: F, steps):
        """steps are exact rational triples(left,right,coefficient)."""
        a = self.arithmetic
        numerator = a.enclose(F(0))
        for left, right, coefficient in steps:
            value = a.sub(self.sin_two_pi(right*x), self.sin_two_pi(left*x))
            numerator = a.add(numerator, a.mul(a.enclose(coefficient), value))
        denominator = a.mul(self.pi, a.enclose(x))
        return a.div(numerator, denominator)

    def fourier_h0(self, x: F):
        return self.fourier_steps(x, [(F(1), F(2), F(1))])


def execute(record, precision=30, degree=14):
    start = perf_counter()
    sine = CertifiedSine(precision, degree)
    unit = sine.arithmetic.unit
    digest = sha256()
    coefficient_error = F(0)
    approximant_norm = F(0)
    summaries = []
    for band in record["bands"]:
        k, n = band["k"], band["cells"]
        left = F(band["left"])
        width = left/n
        radius_square_sum = 0
        center_square_sum = 0
        max_radius = 0
        for index in range(n):
            midpoint = left+(F(index)+F(1, 2))*width
            low, high = sine.fourier_h0(midpoint)
            center = (low+high)//2
            radius = max(center-low, high-center)
            if radius < 0:
                raise ArithmeticError("Invalid outward scalar interval")
            radius_square_sum += radius**2
            center_square_sum += center**2
            max_radius = max(max_radius, radius)
            digest.update(f"{k},{n},{index},{center},{radius}\n".encode("ascii"))
        coefficient_error += width*F(radius_square_sum, unit**2)
        approximant_norm += width*F(center_square_sum, unit**2)
        summaries.append({"k": k, "cells_evaluated": n,
            "max_scalar_radius": str(F(max_radius, unit)),
            "coefficient_L2_error_squared_upper": str(width*F(radius_square_sum, unit**2))})
    mesh = F(record["midpoint_L2_error_squared_upper"])
    # Young with theta=1/16 combines two errors on the same interior domain.
    error2 = F(record["near_zero_L2_error_squared_upper"])+F(
        record["far_tail_L2_error_squared_upper"])+F(17, 16)*mesh+17*coefficient_error
    eps = F(record["tolerance"])
    if error2 > eps**2:
        raise ArithmeticError("Executed primitive did not meet its L2 tolerance")
    if not (1-eps)**2 <= approximant_norm <= (1+eps)**2:
        raise ArithmeticError("Norm consistency failed for unitary Fourier input")
    return {"status": "executed-and-certified", "fixed_input": "h0=1_[1,2], original L2 norm1",
        "target": "Fh0 physical L2 step approximation only, not q0/T/E",
        "precision": precision, "sine_odd_degree": 2*degree+1,
        "integer_interval_unit": str(unit), "cells_evaluated": record["cells"],
        "coefficient_stream_sha256": digest.hexdigest(),
        "coefficient_L2_error_squared_upper": str(coefficient_error),
        "true_Hilbert_L2_error_squared_upper": str(error2),
        "approximant_norm_squared": str(approximant_norm),
        "error_upper_display_only": float(error2)**0.5,
        "norm_squared_display_only": float(approximant_norm),
        "tolerance_met_by_rational_comparison": True,
        "elapsed_seconds": perf_counter()-start, "band_evaluation_summaries": summaries}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--tolerance", default="1/32")
    parser.add_argument("--precision", type=int, default=30)
    parser.add_argument("--sine-degree", type=int, default=14)
    parser.add_argument("--max-cells", type=int, default=500000)
    args = parser.parse_args()
    chosen = plan(F(args.tolerance))
    record = {"schema": "tf-reader-step-primitive-v1", "plan": chosen,
        "implementation_sha256": sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
        "interval_dependency_sha256": sha256(Path(__file__).with_name(
            "tf_reader_arch_gap_certificate.py").read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
        "cost_plans": [{k: v for k, v in plan(F(x)).items() if k != "bands"}
                       for x in ["1/16", "1/32", "1/128", "1/1024", "1/65536"]],
        "scope": "Sufficient cost for this certified dyadic step primitive, not a necessary cost lower bound for q0 or another representation.",
        "q0_status": "not computed", "T_E_status": "not computed"}
    if chosen["cells"] > args.max_cells:
        record["execution"] = {"status": "not-executed-cost-cap", "max_cells": args.max_cells}
    else:
        record["execution"] = execute(chosen, args.precision, args.sine_degree)
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes((json.dumps(record, indent=2)+"\n").encode())
    print(json.dumps({"status": record["execution"]["status"], "cells": chosen["cells"],
        "error_upper_display_only": record["execution"].get("error_upper_display_only"),
        "elapsed_seconds": record["execution"].get("elapsed_seconds"), "output": str(p)}))


if __name__ == "__main__":
    main()

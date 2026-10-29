"""Exact scalar reclosure for one L=9/8 source-only admission.

This does not generate source intervals or certify the full Weil form.
The integral/operator arguments are recorded separately; this checks their
specified rational leaves without importing or executing upstream drivers.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path


def calculate():
    checks = {}

    def require(name, condition):
        checks[name] = bool(condition)

    length = F(9, 8)
    delta = F(1, 2**49158)
    c = 288
    exterior = F(123, 1280)
    require("tail-new-remainder", 2 * F(81, 128)**4096 < F(1, 32))
    require("Lagrange-weight-and-exponent", 6*4095 == 24570 and 2*(5+4+24570) == 49158)
    require("tail-tau", delta/16 == F(1, 2**49162) and exterior > F(1, 16))
    lower0 = F(7*(c-1), 22*c*c)
    lower1 = F(21*(c-2), 22*c*c)
    upper0 = F(50*(c+1), 157*c*c)
    upper1 = F(50*(3*c*c+6*c+2), 157*c**3)
    require("tail-nondegeneracy", min(lower0, lower1) > F(1, 2**11) > delta)
    require("tail-rank-two-C", 81*upper0 < exterior and 27*upper1 < exterior)
    require("tail-column-norms", upper0 < F(1,29**2) and upper1 < F(3,50)**2)
    require("rank-two-column-transport", 2*(F(81,29)+F(81,50))*F(1,2**512)
            +108*F(1,2**1024) < 9*F(1,2**512))

    # e < 68/25 follows from a positive exponential series and its tail.
    e_upper = sum((F(1, factorial(k)) for k in range(7)), F(0)) + F(1,4410)
    require("exponential-upper", e_upper == F(31967,11760) < F(68,25))
    require("new-ellipse-r", 81*68**240*2**1066 < 25**240*3**896)
    r, pole = F(1,2**85), F(1,2**440)
    require("pole-Taylor", F(36,factorial(448)) < pole and 2*length == F(3,2)**2)
    require("pole-exponential", F(68,25)**9 < 2**16 and length/2 < 1)
    m, b = F(15,64), F(433,64)  # Independently established row receipt.
    e, n, h = 1389*r+pole, 896*r*r+pole, 11696*r*r+pole
    require("complement-positive", 0 <= n < m and h >= n)

    # The actual rational Binet remainder is much sharper than its old
    # printed 2^-1034 relaxation. The new producer encloses the true moment
    # with this remainder already included. Do not add it again below.
    binet = F(4*factorial(513)*4**514, 6**514*1025**514)
    moment_binet = F(256,3)*binet  # pi>3, all q>=0.
    midpoint = F(1,2**1098)       # CONDITIONAL true-moment interval radius.
    cosh_upper = F(68,25)**576
    kernel_taylor = F(914*576**2048, factorial(2048))
    kernel_total = 2*length*(kernel_taylor+midpoint*cosh_upper)
    require("Binet-actual-remainder", binet < F(1,2**1500))
    require("Binet-integrated-inside-moment", moment_binet < F(1,2**1493))
    require("kernel-new-Taylor", kernel_taylor < F(1,2**600))
    require("kernel-new-conditional-budget", kernel_total < F(1,2**204))
    band_taylor = F(576**2049,3*factorial(2049))
    require("band-new-Taylor", band_taylor < F(1,2**513))
    # Machin's alternating remainder; no approximation to pi is needed.
    pi_error = F(16,321*5**321)+F(4,321*239**321)
    require("Machin-error", pi_error < F(1,2**646))
    gamma_product = (2*length/F(895))*(2*length/F(3))
    require("raw-column-normalization", gamma_product > F(1,1024) and 448 < 32**2)
    require("conditional-total-column", F(1,2**514)+band_taylor+pi_error < F(1,2**512))
    require("raw-tail-new-factors", 81/(2*length) == 27/(2*length/3) == 36
            and 256*length**2 == 324)
    eta = F(1,2**2048)
    primitive_pad = 121*400514*eta+3*(2*11*14*eta+196*eta**2)
    require("conditional-primitive-padding", primitive_pad < 2**26*eta < F(1,2**2021))
    return {
        "schema": "weil-9-8-analytic-scalar-reclosure-v1",
        "checks": checks, "all_specified_scalar_leaves_passed": all(checks.values()),
        "parameters": {"L":"9/8", "Omega":256, "N":448, "qCount":1024,
                       "momentOutputBits":1152, "momentRadiusBits":1098,
                       "m":str(m), "b":str(b), "rPower":-85, "polePower":-440},
        "paid_scope": "Exact rational leaves of stated analytic bounds only",
        "conditional_inputs": [
            "New 1024 TRUE moment intervals independently contained and radius <=2^-1098; Binet already included once by producer and checker",
            "New primitive true-center errors <=2^-2048, 15 shifts and absolute mass <11",
            "All new matrix weighted rows and tail coordinate errors independently paid",
            "Upstream integral/operator proof transport and root premise closure"],
        "unpaid": ["new inverse/congruence/full Gram signs", "full complement/cross finite target"],
        "binet_payment": "Included in true-moment interval oracle; no additional Binet term in kernel_total",
        "source_intervals_generated": False, "full_weil_positivity":"NOT_ESTABLISHED",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    destination = Path(parser.parse_args().output)
    assert not destination.exists(), "Preserve prior attempts"
    result = calculate()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(destination), "passed":result["all_specified_scalar_leaves_passed"],
                      "checks":len(result["checks"]),"full_weil_positivity":"NOT_ESTABLISHED"}))
    return 0 if result["all_specified_scalar_leaves_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

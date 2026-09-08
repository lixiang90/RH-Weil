"""Arb enclosures for the fixed profile and its first two derivatives.

This module is an arithmetic component, not a subaction certificate.
Install the pinned wheel described in reviews/2026-09-08/interval-runtime.json,
or provide python-flint 0.9.0 in the invoking interpreter.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from pathlib import Path
import hashlib
import json
import sys

try:
    from flint import arb, ctx
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tmp/interval-runtime/site"))
    from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]
PROFILE_SHA256 = "3a89799a5705cc8c30c629643f32d72ee000c34bf67798510d6bfdd8575bdca0"


def rational(value):
    return arb(str(Fraction(value)))


def radius_ball(upper):
    """A zero-centered ball using a proven dyadic upper radius."""
    return arb(0, tuple(map(int, upper.upper().man_exp())))


def dyadic_fraction(value):
    mantissa, exponent = map(int, value.man_exp())
    return Fraction(mantissa)*(Fraction(2)**exponent)


def rational_bounds(value):
    assert value.is_finite()
    return dyadic_fraction(value.lower()), dyadic_fraction(value.upper())


class Kernel:
    def __init__(self, bits=192):
        ctx.prec = bits
        self.bits = bits
        path = ROOT / "reviews/2026-09-08/radius-five-rational-profile-candidate.json"
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == PROFILE_SHA256
        proposal = json.loads(raw)
        self.t = [rational(v["t"]) for v in proposal["terms"]]
        y = [rational(v["y"]) for v in proposal["terms"]]
        self.a = arb(2).sqrt()
        self.ma = (self.a/2).sinc()
        self.z = [yy*t*t/(t*t-2) for t, yy in zip(self.t, y)]
        self.A = 1-sum((z*(t/2).sinc() for t, z in zip(self.t, self.z)), arb(0))
        self.polynomials = []
        for derivative in range(3):
            coefficients = []
            for degree in range(33):
                power = degree+derivative
                c = Fraction(0) if power % 2 else Fraction(
                    (-1)**(power//2), 2**power*(power+1)*factorial(degree))
                coefficients.append(rational(c))
            self.polynomials.append(coefficients)

    def sinc_jet(self, x):
        """m(x)=integral[-1/2,1/2] exp(ixu)du and its derivatives."""
        if x.abs_upper() <= arb("1/2"):
            answer = []
            for j, coefficients in enumerate(self.polynomials):
                value = arb(0)
                for coefficient in reversed(coefficients):
                    value = value*x+coefficient
                # Taylor in the real x variable through degree 32;
                # sup |m^(33+j)| <= 1/(2^(33+j)*(34+j)).
                remainder = x.abs_upper()**33 / (factorial(33)*2**(33+j)*(34+j))
                answer.append(value+radius_ball(remainder))
            return tuple(answer)
        assert not x.contains(0)
        sine, cosine = (x/2).sin(), (x/2).cos()
        return (2*sine/x,
                cosine/x-2*sine/(x*x),
                -sine/(2*x)-2*cosine/(x*x)+4*sine/(x*x*x))

    def jet(self, x):
        assert ctx.prec >= self.bits
        if not isinstance(x, arb):
            x = rational(x)
        left, right = self.sinc_jet(x-self.a), self.sinc_jet(x+self.a)
        result = [self.A*(l+r)/(2*self.ma) for l, r in zip(left, right)]
        for t, z in zip(self.t, self.z):
            left, right = self.sinc_jet(x-t), self.sinc_jet(x+t)
            result = [v+z*(l+r)/2 for v, l, r in zip(result, left, right)]
        return tuple(result)

    def value(self, x):
        if not isinstance(x, arb):
            x = rational(x)
        result = self.A*((x-self.a)/2).sinc()/(2*self.ma)
        result += self.A*((x+self.a)/2).sinc()/(2*self.ma)
        for t, z in zip(self.t, self.z):
            result += z*(((x-t)/2).sinc()+((x+t)/2).sinc())/2
        return result

    def energy_jet(self, x):
        k, first, second = self.jet(x)
        return 2*k*k, 4*k*first, 4*(first*first+k*second)


def main():
    kernel = Kernel()
    points = ["0", "1.414213562373095", "5.7", "6.5209647", "6.5217874",
              "12.4351276", "50.6166493", "60", "128", "400", "640"]
    records = []
    for x in points:
        jet = kernel.jet(x)
        direct = kernel.value(x)
        assert direct.overlaps(jet[0])
        assert all(v.is_finite() for v in jet)
        records.append(dict(x=x, kernel_jet=[[str(q) for q in rational_bounds(v)] for v in jet],
                            direct_value=[str(q) for q in rational_bounds(direct)]))
    assert kernel.jet(0)[0].contains(1)
    assert kernel.jet(0)[1].contains(0)
    output = dict(status="Arithmetic component smoke checks passed; independent proof review pending",
                  bits=kernel.bits, profile_sha256=PROFILE_SHA256, points=records,
                  near_zero_taylor_degree=32,
                  remainder="|x|^33/(33!*2^(33+j)*(34+j)) for derivative j=0,1,2",
                  scope="No all-cell table, finite graph, or continuous subaction is certified here")
    (ROOT / "reviews/2026-09-08/radius-five-arb-kernel-smoke.json").write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {len(points)} point jets finite, value formulas overlap, x=0 normalization.")


if __name__ == "__main__":
    main()

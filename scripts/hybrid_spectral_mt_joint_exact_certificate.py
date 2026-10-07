"""Exact algebra/interval certificate for the new MT spectral data model.

The continuous Taylor enclosure and paired-inertia statements are proved in
the research report. This script reproduces only rational polynomial integrals
and interval feasibility. It neither certifies the actual prime Gram nor adds
any unproved arithmetic premise. All output is written to a new file.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as s


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(str(lo))
        self.hi = F(str(lo if hi is None else hi))

    def __add__(self, rhs):
        rhs = rhs if isinstance(rhs, Interval) else Interval(rhs)
        return Interval(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, rhs):
        return self + -(rhs if isinstance(rhs, Interval) else Interval(rhs))

    def __rsub__(self, lhs):
        return Interval(lhs) + -self

    def __mul__(self, rhs):
        rhs = rhs if isinstance(rhs, Interval) else Interval(rhs)
        vals = [self.lo * rhs.lo, self.lo * rhs.hi,
                self.hi * rhs.lo, self.hi * rhs.hi]
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, rhs):
        rhs = rhs if isinstance(rhs, Interval) else Interval(rhs)
        assert rhs.lo * rhs.hi > 0
        return self * Interval(1 / rhs.hi, 1 / rhs.lo)

    def __pow__(self, exponent):
        ans = Interval(1)
        for _ in range(exponent):
            ans = ans * self
        return ans

    def json(self):
        return {"lo_exact": str(self.lo), "hi_exact": str(self.hi),
                "lo_display": float(self.lo), "hi_display": float(self.hi)}


z, x, y = s.symbols("z x y")
half = s.Rational(1, 2)


def poly(n, t):
    return sum(s.Rational((-1)**j * 2**j, s.factorial(2*j)) * t**(2*j)
               for j in range(n+1))


def sin_poly(n, t):
    return sum(s.Rational((-1)**j * 2**j, s.factorial(2*j+1)) * t**(2*j+1)
               for j in range(n+1))


def integrate_z(expression, lo, hi):
    return s.integrate(s.Poly(s.expand(expression), z).as_expr(), (z, lo, hi))


al = integrate_z(poly(5, z), -half, half)
au = integrate_z(poly(6, z), -half, half)
alpha_lo = poly(5, z) / au - 1
alpha_hi = poly(6, z) / al - 1
delta = s.Rational(1, 10**9)
remainder = s.Rational(1, 64 * s.factorial(12))
assert remainder / al + (au-al) / al**2 < delta
assert 1/al - 1 < s.Rational(1, 5)
assert alpha_lo.subs(z, half) > -s.Rational(1, 5)
root_lo, root_hi = s.Rational(287, 1000), s.Rational(288, 1000)
assert alpha_lo.subs(z, root_lo) > 0
assert alpha_hi.subs(z, root_hi) < 0

exact = {}
exact["v"] = (poly(5, half)/au-half, poly(6, half)/al-half)
for key, power in [("V", 2), ("M4", 4)]:
    center = integrate_z(alpha_lo**power, -half, half)
    exact[key] = (center-delta, center+delta)
for power in [1, 3]:
    lo = (2*integrate_z(alpha_lo**power, 0, root_lo)
          - 2*integrate_z(alpha_hi**power, root_lo, half))
    hi = (2*integrate_z(alpha_hi**power, 0, root_lo)
          - 2*integrate_z(alpha_lo**power, root_lo, half)
          + s.Rational(4, power+1) * (root_hi-root_lo)**(power+1))
    exact["K"+str(power)] = (lo, hi)
glo = ((1-x)*poly(5, x)+sin_poly(5, 1-x))/2
ghi = ((1-x)*poly(6, x)+sin_poly(6, 1-x))/2
exact["VH"] = (2*s.integrate(x*glo, (x, half, 1))/au**2,
               2*s.integrate(x*ghi, (x, half, 1))/al**2)

def path_numerator(degree):
    f = poly(degree, z)
    paths = [
        (f*f*poly(degree, z+x)*poly(degree, z+y), -half, half-x),
        (f*f*poly(degree, z+x)*poly(degree, z-y), -half+y, half-x),
        (f*poly(degree, z+x)*poly(degree, z+y)*poly(degree, z+x+y),
         -half, half-x-y),
    ]
    result = s.Rational(0)
    for expression, lo, hi in paths:
        iz = integrate_z(expression, lo, hi)
        iy = s.integrate(s.expand(x*y*iz), (y, 0, x))
        result += s.integrate(iy, (x, 0, half))
    return 8*result


raw_lower = path_numerator(1)
raw_upper = path_numerator(2)
assert raw_lower == s.Rational(3989807597, 66421555200)
assert raw_upper == s.Rational(418537850292443239, 6920254601035776000)
exact["c"] = (raw_lower/s.Rational(147, 160)**4,
              raw_upper/s.Rational(11, 12)**4)

inputs = {
    "v": Interval(".32749", ".32751"),
    "V": Interval(".0061271", ".0061273"),
    "M4": Interval(".00007878", ".00007880"),
    "K1": Interval(".0675305", ".0675326"),
    "K3": Interval(".000654884", ".000654885"),
    "VH": Interval(".1499168", ".1499170"),
    "c": Interval(".08430", ".08566"),
}
for name, (lo, hi) in exact.items():
    assert inputs[name].lo < F(str(lo)) <= F(str(hi)) < inputs[name].hi

v, V, M4, K1, K3, VH, c = [inputs[k] for k in
                          ["v", "V", "M4", "K1", "K3", "VH", "c"]]
B, B2, Z2 = v-K1, v*V-K3, (1-v)*V
m = VH/B
c0 = (B*(1-m)**3 + 3*B2*(2-3*m+m*m)
      + 3*V*(VH-B*m*m) + K1-4*V+6*K3-3*M4)
c1 = 3*(B-VH+V*K1-K3)
u = (c-c0)/c1
w = (VH-B*(m*m+u))/(1-v)
ehl3 = m*(1-m)**3 + (-3+9*m-6*m*m)*u-u*u
ehl = m-m*m-u
k = (B*ehl3+3*B2*ehl-3*Z2*w)/(1-v)
gap = k-w*w
assert u.lo > F(".04323") and u.hi < F(".04742")
assert w.lo > F(".07602") and w.hi < F(".07768")
assert k.lo > F(".01904") and k.hi < F(".01959")
assert gap.lo > F(".01301")

workspace = Path(__file__).resolve().parents[1]
report = workspace / "reviews/2026-10-07/hybrid-spectral-low-high-information-and-narrow-window-research-compression.md"
canonical = report.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
output = {
    "scope": "Exact rational algebra/interval certificate; no actual-prime or feature-kernel realization.",
    "report_canonical_lf_sha256": hashlib.sha256(canonical).hexdigest(),
    "raw_low4_numerator_lower": str(raw_lower),
    "raw_low4_numerator_upper": str(raw_upper),
    "taylor_exact_intervals": {name: {"lo": str(lo), "hi": str(hi)}
                               for name, (lo, hi) in exact.items()},
    "coarse_inputs": {name: val.json() for name, val in inputs.items()},
    "feasibility": {name: val.json() for name, val in
                    {"B": B, "m": m, "c0": c0, "c1": c1,
                     "u": u, "w": w, "k": k, "k_minus_w_squared": gap}.items()},
    "all_assertions_passed": True,
}
destination = workspace / "output/hybrid-spectral-mt-joint-exact-certificate.json"
destination.write_text(json.dumps(output, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
print(json.dumps({"output": str(destination), "all_assertions_passed": True,
                  "report_hash": output["report_canonical_lf_sha256"]}, ensure_ascii=False))

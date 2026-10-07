"""Exact algebra audit for free-b compensated-probe geometry.

This script certifies displayed finite polynomial identities and inequalities.
It does not certify imported analytic lemmas, actual prime sums, infinite
contours, a zero-free theorem, RH, or an external proof kernel. No files are
written. Arithmetic is in Q or Q(sqrt(921)); floats are not used.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


@dataclass(frozen=True)
class Quad:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Quad) else Quad(F(value))

    def __add__(self, other):
        other = self.coerce(other)
        return Quad(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Quad(self.a * other.a + 921 * self.b * other.b,
                    self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        denominator = other.a * other.a - 921 * other.b * other.b
        if not denominator:
            raise ZeroDivisionError
        return self * Quad(other.a / denominator, -other.b / denominator)

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def sign(self):
        a, b = self.a, self.b
        if not b:
            return (a > 0) - (a < 0)
        if a >= 0 and b > 0:
            return 1
        if a <= 0 and b < 0:
            return -1
        if b > 0:
            difference = 921 * b * b - a * a
        else:
            difference = a * a - 921 * b * b
        return (difference > 0) - (difference < 0)

    def text(self):
        if not self.b:
            return str(self.a)
        return f"({self.a})+({self.b})*sqrt(921)"


ZERO = Quad()
ONE = Quad(F(1))
CHECKS = 0


def check(condition, name):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(name)


def positive(value, name):
    check(Quad.coerce(value).sign() > 0, name)


def equal(left, right, name):
    check(Quad.coerce(left) == Quad.coerce(right), name)


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == ZERO:
        poly.pop()
    return poly


def add(p, q):
    result = [ZERO] * max(len(p), len(q))
    for i, v in enumerate(p):
        result[i] = result[i] + v
    for i, v in enumerate(q):
        result[i] = result[i] + v
    return trim(result)


def scale(p, value):
    return trim([v * value for v in p])


def multiply(p, q):
    result = [ZERO] * (len(p) + len(q) - 1)
    for i, v in enumerate(p):
        for j, w in enumerate(q):
            result[i + j] = result[i + j] + v * w
    return trim(result)


def evaluate(p, value):
    result = ZERO
    for v in reversed(p):
        result = result * value + v
    return result


def coefficients(ell, b):
    """648*(-2 J E_sigma)=A(y) delta^2-B(y) delta+C(y)."""
    ell, b = Quad.coerce(ell), Quad.coerce(b)
    A = [252 + 756 * ell - 576 * b,
         648 + 288 * ell + 720 * b,
         288 + 1008 * ell + 864 * b, 1152 * ell]
    B = [624 - 1440 * ell - 1176 * b,
         504 - 420 * ell - 456 * b,
         -48 + 120 * ell + 432 * b]
    C = [555 - 2775 * ell - 370 * b,
         510 - 2550 * ell - 340 * b]
    Q = add(scale(multiply(A, C), 4), scale(multiply(B, B), -1))
    return A, B, C, Q


def row_symbol(delta, y):
    x = Quad.coerce(F(1, 2)) - y
    D = 3 - F(17, 9) * x
    P = (2 - F(8, 9) * x) * (1 - x)
    J = (F(5, 6) - delta) * D + delta * P
    R = 1 - delta + (F(5, 6) - delta) * delta * P / (2 * J)
    return D, P, J, R


def endpoint(ell, b, delta, y):
    ell, b, delta, y = map(Quad.coerce, (ell, b, delta, y))
    _, _, J, R = row_symbol(delta, y)
    h = (1 + 3 * ell + b) / 2
    K = -F(1, 4) + F(5, 4) * ell + b / 6
    x = F(1, 2) - y
    E = K + (F(1, 2) + ell) * delta + ell * delta * x - h * (1 - R)
    return E, J, R


def geometry(ell, b, zeta):
    ell, b, zeta = map(Quad.coerce, (ell, b, zeta))
    lx, ly = (1 - ell - b) / 2, (1 - ell + b) / 2
    h, sigma = (1 + 3 * ell + b) / 2, F(11, 12) - ell / 4
    values = {
        "ell": ell, "b": b, "lx": lx, "ly": ly, "h": h,
        "sigma": sigma, "low": (1 - ell) / 4 - b / 6,
        "C_sigma": sigma - F(2, 3) - b / 6,
        "minimum_M_prime": 1 - 3 * ell,
        "minimum_lx_prime": lx - ell,
        "minimum_ly_prime": ly - ell,
        "all_J_Gram_gap": ly - ell - F(11, 6) * b,
        "full_Gram_gap": ly - F(11, 6) * b,
        "supply_gap": ell / (h + zeta) - F(7, 37),
        "supply_to_one_fifth": 5 * ell - h - zeta,
        "small_exponent": h * F(13, 75) - ly / 2 + F(63, 5000),
        "floor_exponent": -F(1, 4) + F(5, 4) * ell + b / 6
                          + (F(1, 2) + ell) / 50 + ell / 100,
        "middle_exponent": -F(71, 600) + F(329, 400) * ell
                           - F(421, 1200) * b,
        "principal_w": ly / 20, "principal_z": h / 600,
        "good_margin": sigma - F(3, 50),
        "ramified_margin": sigma - F(1, 20),
        "absolute_B0": F(7, 4) - F(3, 4) * ell + b / 4,
    }
    equal(values["low"], values["C_sigma"], "low intersection")
    positive(ell - F(1, 6), "ell above one-sixth")
    positive(F(1, 5) - ell, "ell below one-fifth")
    for name in ["b", "minimum_M_prime", "minimum_lx_prime",
                 "minimum_ly_prime", "all_J_Gram_gap", "full_Gram_gap",
                 "supply_gap", "supply_to_one_fifth", "principal_w",
                 "principal_z", "good_margin", "ramified_margin"]:
        positive(values[name], name)
    positive(1 - h - zeta, "retained d ceiling below one")
    positive(-values["floor_exponent"] - F(1, 200), "floor margin")
    positive(-values["middle_exponent"] - F(1, 50), "middle margin")
    positive(-values["small_exponent"] - F(2, 25), "small margin")
    positive(sigma - F(5, 6), "small/principal analytic box")
    positive(sigma + F(1, 2) - F(4, 3), "small D1 one-third")
    return {name: value.text() for name, value in values.items()}


ell_r = Quad(F(5831, 34950))
b_r = Quad(F(617, 5000))
Ar, Br, Cr, Qr = coefficients(ell_r, b_r)
for name, polynomial in [("A", Ar), ("C", Cr), ("Q", Qr)]:
    for i, value in enumerate(polynomial):
        positive(value, f"rational {name} coefficient {i}")
ratio = add(scale(Qr, Ar[0]), scale(Ar, -Qr[0]))
equal(ratio[0], 0, "ratio constant zero")
for i, value in enumerate(ratio[1:], 1):
    positive(value, f"rational Q/A comparison coefficient {i}")
margin = Qr[0] / (12960 * Ar[0])
equal(margin, F(10580567, 347281513800000), "rational margin")
mad = Quad(F(1, 100000000))
positive(margin - mad, "safe rational margin")
geometry_r = geometry(ell_r, b_r, mad / 32)

root = Quad(F(0), F(1))
ell_c = (33 + 8 * root) / 1653
b_c = (2185 * ell_c - 213) / 1228
delta_c = (49 - root) / 48
equal(1653 * ell_c * ell_c - 66 * ell_c - 35, 0, "critical quadratic")
positive(ell_c - F(1, 6), "critical lower isolating bound")
positive(F(167, 1000) - ell_c, "critical upper isolating bound")
Ac, Bc, Cc, Qc = coefficients(ell_c, b_c)
expected_Q = [
    ZERO,
    F(17404800, 169157) * (5465 - 31728 * ell_c),
    F(1200, 169157) * (47597384 - 214807491 * ell_c),
    F(4800, 169157) * (131691060 * ell_c - 18009311),
    F(14400, 8903) * (1377691 * ell_c - 209998),
]
for i, value in enumerate(expected_Q):
    equal(Qc[i], value, f"critical Q coefficient identity {i}")
for name, polynomial in [("A", Ac), ("C", Cc)]:
    for i, value in enumerate(polynomial):
        positive(value, f"critical {name} coefficient {i}")
for i, value in enumerate(Qc[1:], 1):
    positive(value, f"critical Q positive coefficient {i}")
equal(Bc[0] / (2 * Ac[0]), delta_c, "unique equality delta")
E_c, J_c, R_c = endpoint(ell_c, b_c, delta_c, ZERO)
equal(E_c, 0, "critical equality")
equal(R_c, F(2, 3), "b-independent witness")
equal(ell_c, (5 - 6 * delta_c) / (9 + 18 * delta_c),
      "global optimizing ell")
positive(F(3, 4) + F(3, 2) * delta_c, "global obstruction slope")
zeta_max = (ell_c - F(1, 6)) / 128
geometry_c = geometry(ell_c, b_c, zeta_max)

# Independent direct endpoint evaluations: not the continuous proof.
for delta in [F(1, 50) + F(i, 20) * (F(3, 4) - F(1, 50))
              for i in range(21)]:
    for y in [F(i, 16) for i in range(9)]:
        E, J, R = endpoint(ell_r, b_r, delta, y)
        p = evaluate(Ar, y) * delta * delta \
            - evaluate(Br, y) * delta + evaluate(Cr, y)
        equal(p, -1296 * J * E, "direct polynomial identity")
        positive(J, "direct positive J")
        positive(-E - mad, "direct rational margin")
        D, P, _, _ = row_symbol(Quad(delta), Quad(y))
        check((2 * D - 3 * P).sign() >= 0, "capacity comparison")

# Discriminant-at-y=0 optimizing identity, evaluated exactly in the field.
q0_formula = (-530496 * b_c * b_c + 1887840 * b_c * ell_c
              - 184032 * b_c - 10465200 * ell_c * ell_c
              + 678240 * ell_c + 170064)
equal(Qc[0], q0_formula, "critical discriminant optimization identity")
equal(q0_formula, 0, "critical optimizing discriminant")

result = {
    "scope": "Exact displayed algebra in Q and Q(sqrt(921)) only; imported "
             "analytic inputs, primes, contours, zero-free conclusions, RH, "
             "and external kernels are not certified.",
    "source_sha256_canonical_lf":
        "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3",
    "checks": CHECKS,
    "status": "PASS",
    "continuous_method": "A>0 and 4AC-B^2 coefficient positivity; "
                         "complete the quadratic in delta. No grid inference.",
    "rational": {
        "geometry": geometry_r, "A": [v.text() for v in Ar],
        "B": [v.text() for v in Br], "C": [v.text() for v in Cr],
        "Q": [v.text() for v in Qr], "certified_margin": margin.text(),
        "safe_margin": mad.text(),
    },
    "critical": {
        "geometry": geometry_c, "delta": delta_c.text(),
        "Q": [v.text() for v in Qc], "endpoint_margin": "0",
        "unique_equality": "y=0, delta=(49-sqrt(921))/48",
        "closure_interface": "E_beta<=-Delta before real losses; choose "
                             "Delta budgets, mesh, K, then mu, all before target.",
    },
}
this_source = Path(__file__).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
result["script_sha256_canonical_lf"] = hashlib.sha256(this_source).hexdigest()
print(json.dumps(result, ensure_ascii=False, indent=2))

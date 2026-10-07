"""Exact displayed-algebra audit of the kappa-feedback boundary.

Only rational arithmetic and Q[e]/(657e^3-954e^2+21e+20) are used.
The isolated real embedding is certified by rational interval arithmetic.
No files are written. This does not certify the imported analytic inputs,
the plain-moment induction, prime estimates, contours, or a zero-free theorem.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LO = F(16683858898627, 10**14)
HI = F(16683858898628, 10**14)
CHECKS = 0


def cubic(t):
    return 657*t**3 - 954*t**2 + 21*t + 20


def require(condition, label):
    global CHECKS
    assert condition, label
    CHECKS += 1


def interval_multiply(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


class Cubic:
    def __init__(self, a=0, b=0, c=0):
        self.v = (F(a), F(b), F(c))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Cubic) else Cubic(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Cubic(*(x+y for x, y in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return Cubic(*(-x for x in self.v))

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        result = [F(0)] * 5
        for i, x in enumerate(self.v):
            for j, y in enumerate(other.v):
                result[i+j] += x*y
        # e^3=(-20-21e+954e^2)/657.
        for n in (4, 3):
            value = result[n]
            result[n] = F(0)
            for j, coefficient in enumerate((-20, -21, 954)):
                result[n-3+j] += value*F(coefficient, 657)
        return Cubic(*result[:3])

    __rmul__ = __mul__

    def inverse(self):
        basis = (Cubic(1), Cubic(0, 1), Cubic(0, 0, 1))
        columns = [(self*b).v for b in basis]
        matrix = [[columns[j][i] for j in range(3)] +
                  [F(i == 0)] for i in range(3)]
        for j in range(3):
            pivot = next(i for i in range(j, 3) if matrix[i][j])
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            divisor = matrix[j][j]
            matrix[j] = [value/divisor for value in matrix[j]]
            for i in range(3):
                if i != j:
                    multiplier = matrix[i][j]
                    matrix[i] = [x-multiplier*y
                                 for x, y in zip(matrix[i], matrix[j])]
        result = Cubic(*(matrix[i][-1] for i in range(3)))
        assert (self*result).v == Cubic(1).v
        return result

    def __truediv__(self, other):
        return self*self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other)*self.inverse()

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        result = Cubic(1)
        for _ in range(power):
            result *= self
        return result

    def interval(self):
        result = (self.v[2], self.v[2])
        for value in (self.v[1], self.v[0]):
            result = interval_multiply(result, (LO, HI))
            result = result[0]+value, result[1]+value
        return result

    def text(self):
        return [str(value) for value in self.v]


def equal(a, b, label):
    require(Cubic.coerce(a).v == Cubic.coerce(b).v, label)


def positive(a, label):
    require(Cubic.coerce(a).interval()[0] > 0, label)


def add(*polynomials):
    result = [Cubic(0)]*max(map(len, polynomials))
    for p in polynomials:
        for i, value in enumerate(p):
            result[i] += value
    return result


def scale(p, value):
    return [value*x for x in p]


def multiply(p, q):
    result = [Cubic(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i+j] += x*y
    return result


def evaluate(p, value):
    result = Cubic(0)
    for coefficient in reversed(p):
        result = result*value+coefficient
    return result


require(cubic(LO) > 0 > cubic(HI), "isolating endpoint signs")
# On [1/6,167/1000], p'(e)=1971e^2-1908e+21<0.
require(1971*F(167, 1000)**2-1908*F(1, 6)+21 < 0,
        "strict monotonicity throughout the isolating region")
require([int(cubic(F(j))) % 7 for j in range(7)] ==
        [6, 3, 4, 3, 1, 6, 5], "irreducible cubic modulo seven")
old_lo, old_hi = F(16683838746, 10**11), F(16683838748, 10**11)
require(1653*old_lo**2-66*old_lo-35 < 0 <
        1653*old_hi**2-66*old_hi-35, "previous quadratic root bracket")
require(LO > old_hi, "new ell strictly exceeds previous ell")

e = Cubic(0, 1)
k = F(5, 6)-e/2
b = (5040*e*k**2-900*e*k+25*e-432*k**2+36*k+3) / (
     3312*k**2-936*k+67)
sigma = F(11, 12)-e/4
lx, ly = (1-e-b)/2, (1-e+b)/2
h = (1+3*e+b)/2
equal(657*e**3-954*e**2+21*e+20, 0, "minimal polynomial")
equal(k, 2*sigma-1, "feedback reference kappa")
equal(7884*sigma**3-18819*sigma**2+14643*sigma-3686, 0,
      "boundary cubic")
positive(k-F(37, 50), "kappa above extended lower endpoint")
positive(F(3, 4)-k, "kappa below original endpoint")

c = 1/(3*k)
D = [F(5, 2)-c, 1+2*c]
P = [1-c/2, Cubic(2), 2*c]
K = -F(1, 4)+5*e/4+b/6
W_minus_h = [F(1, 2)+3*e/2-h, -e]
A = add(scale(multiply(add(P, scale(D, -1)), W_minus_h), -2),
        scale(P, h))
B = add(scale(add(P, scale(D, -1)), 2*K),
        scale(multiply(D, W_minus_h), F(5, 3)),
        scale(P, F(5, 6)*h))
C = scale(D, -F(5, 3)*K)
Q = add(scale(multiply(A, C), 4), scale(multiply(B, B), -1))
equal(Q[0], 0, "critical discriminant constant")
for j, value in enumerate(A):
    positive(value, f"A coefficient {j}")
for j, value in enumerate(C):
    positive(value, f"C coefficient {j}")
for j, value in enumerate(Q[1:], 1):
    positive(value, f"Q coefficient {j}")
delta_star = (5-9*e)/(6+18*e)
equal(delta_star, B[0]/(2*A[0]), "unique delta equality")
positive(delta_star-F(1, 50), "equality delta in actual rectangle")
positive(F(3, 4)-delta_star, "equality delta below bootstrap cap")

direct_cases = 0
for delta in map(F, (F(1, 50), F(1, 8), F(1, 4), F(3, 8),
                     F(1, 2), F(5, 8), F(3, 4))):
    for y in map(F, (0, F(1, 12), F(1, 6), F(1, 4),
                     F(1, 3), F(5, 12), F(1, 2))):
        dd, pp = evaluate(D, y), evaluate(P, y)
        jj = (F(5, 6)-delta)*dd+delta*pp
        rr = 1-delta+(F(5, 6)-delta)*delta*pp/(2*jj)
        endpoint = K+(F(1, 2)+e)*delta+e*delta*(F(1, 2)-y)-h*(1-rr)
        ff = evaluate(A, y)*delta**2-evaluate(B, y)*delta+evaluate(C, y)
        equal(ff, -2*jj*endpoint, "direct endpoint identity")
        equal(ff, evaluate(A, y)*(delta-evaluate(B, y)/
              (2*evaluate(A, y)))**2+evaluate(Q, y)/
              (4*evaluate(A, y)), "direct square completion")
        direct_cases += 1
jj = (F(5, 6)-delta_star)*D[0]+delta_star*P[0]
rr = 1-delta_star+(F(5, 6)-delta_star)*delta_star*P[0]/(2*jj)
equal(rr, F(2, 3), "critical count equality")
equal(K+(F(1, 2)+3*e/2)*delta_star-h*(1-rr), 0,
      "critical endpoint equality")

zeta_max = F(1, 384000)
geometry = {
    "ell": e, "b": b, "kappa_reference": k, "sigma": sigma,
    "lx": lx, "ly": ly, "h": h,
    "minimum_M_prime": 1-3*e, "minimum_lx_prime": lx-e,
    "minimum_ly_prime": ly-e,
    "all_J_Gram_gap": ly-e-F(11, 6)*b,
    "full_Gram_gap": ly-F(11, 6)*b,
    "supply_gap": 5*e-h-zeta_max,
    "floor_exponent": -F(6, 25)+F(32, 25)*e+b/6,
    "middle_exponent": -F(71, 600)+F(329, 400)*e-F(421, 1200)*b,
    "small_exponent": F(13, 75)*h-ly/2+F(63, 5000),
    "principal_w": ly/20, "principal_z": h/600,
    "good_defect": sigma-F(3, 50),
    "ramified_defect": sigma-F(1, 20),
}
for name in ("b", "minimum_M_prime", "minimum_lx_prime",
             "minimum_ly_prime", "principal_w", "principal_z"):
    positive(geometry[name], name)
positive(e-F(1, 6), "ell above one sixth")
positive(F(1, 5)-e, "ell below one fifth")
positive(geometry["all_J_Gram_gap"]-F(2, 25), "full-subset Gram gap")
positive(geometry["supply_gap"]-F(1, 50), "supply exceeds one fifth")
positive(1-h-zeta_max, "outer ceiling below one")
positive(-geometry["floor_exponent"]-F(1, 200), "floor fixed margin")
positive(-geometry["middle_exponent"]-F(1, 50), "middle fixed margin")
positive(-geometry["small_exponent"]-F(2, 25), "small fixed margin")
positive(geometry["good_defect"]-F(81, 100), "good Euler domain")
positive(geometry["ramified_defect"]-F(82, 100), "ramified Euler domain")
positive(sigma+F(1, 2)-F(4, 3), "small D1 one-third box")
positive(zeta_max-(e-F(1, 6))/128, "Delta/32 within zeta ceiling")
equal((1-e)/4-b/6, sigma-F(2, 3)-b/6, "same low normalizer")

require(F(625, 36963) < F(1, 50), "count-feedback derivative bound")
require(F(24, 25)-F(1, 16) == F(359, 400),
        "feedback and d-extension saving")
require(F(25, 516) < F(1, 20), "extended comparison bound")
require(F(1, 20)-F(25, 516) == F(1, 645), "comparison slack")
require(F(1, 18*F(37, 50)) < F(1, 5), "plain slot supply")
require(F(35, 48) > F(7, 10), "uniform J bound")


def canonical_sha(path):
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


report = {
    "status": "PASS", "checks": CHECKS,
    "scope": "Exact displayed cubic-field algebra, rational interval signs and finite identity models only. Imported estimates, plain induction, actual prime sums, infinite contours, zero-free conclusions, RH and external kernels are not certified.",
    "source_sha256_canonical_lf": "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3",
    "script_sha256_canonical_lf": canonical_sha(Path(__file__)),
    "root_interval": [str(LO), str(HI)],
    "root_polynomial": [20, 21, -954, 657],
    "field_basis": ["1", "ell_star", "ell_star^2"],
    "geometry": {name: value.text() for name, value in geometry.items()},
    "A": [value.text() for value in A],
    "B": [value.text() for value in B],
    "C": [value.text() for value in C],
    "Q": [value.text() for value in Q],
    "coefficient_signs": {"A": "all positive", "C": "all positive",
                          "Q": "Q0=0; Q1..Q4 positive"},
    "equality_delta": delta_star.text(),
    "direct_endpoint_models": direct_cases,
    "count_feedback_derivative_upper_bound": "625/36963 < 1/50",
    "central_saving_before_other_losses": "359/400 * Delta",
    "continuous_proof": "A>0, Q(y)>=0 for y>=0, followed by exact quadratic square completion. Finite models are not used to infer continuity.",
}
print(json.dumps(report, ensure_ascii=False, indent=2))

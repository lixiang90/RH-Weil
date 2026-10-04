"""Exact finite-fibre model audit for 430's original-source Gram formulas.

Integer periods and pointwise rational partitions model finite fibre algebra.
This is not the smooth prime-log frame, an essential-norm proof, or an RH test.
No coordinate truncation is used: all nonzero source rows are enumerated.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reviews/2026-10-04/f1-source-orbit-gram-exact-audit.json"
PAIRS = [(Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13)),
         (Q(8, 17), Q(15, 17)), (Q(7, 25), Q(24, 25)),
         (Q(20, 29), Q(21, 29))]


class Fibre:
    def __init__(self, length, period):
        self.L, self.M = length, period

    def c(self, t):
        cell, residue = divmod(t, self.L)
        return PAIRS[residue % len(PAIRS)][cell] if cell in (0, 1) else Q(0)

    def d(self, t):
        cell, residue = divmod(t, self.M)
        return PAIRS[(residue + 2) % len(PAIRS)][cell] if cell in (0, 1) else Q(0)

    def f(self, t):
        return self.c(t) * self.d(t)

    def c_rows(self, x, k):
        # Solve 0 <= x+jL+kM < 2L exactly, with no tail approximation.
        offset = x + k * self.M
        lower = -(offset // self.L)  # integer ceiling of -offset/L
        upper = (2 * self.L - 1 - offset) // self.L
        return range(lower, upper + 1)

    def d_rows(self, x):
        lower = -((x) // self.M)  # integer ceiling of -x/M
        upper = (2 * self.M - 1 - x) // self.M
        return range(lower, upper + 1)

    def f_rows(self, x):
        diameter = min(2 * self.L, 2 * self.M)
        return range(-(x // self.M), (diameter - 1 - x) // self.M + 1)

    def vector(self, x):
        out = {}
        for j in self.c_rows(x, 0):
            if j < 0:
                out[j, 0] = self.c(x + j * self.L)
        for k in self.d_rows(x):
            if k < 0:
                out[0, k] = self.d(x + k * self.M)
        return clean(out)

    def source(self, x, vector, power):
        """1-e+v_power, using the full rank-one source fibres directly."""
        dots = defaultdict(Q)
        for (j, k), value in vector.items():
            dots[k] += self.c(x + j * self.L + k * self.M) * value
        out = defaultdict(Q, vector)
        for k, dot in dots.items():
            for j in self.c_rows(x, k):
                out[j, k] -= self.c(x + j * self.L + k * self.M) * dot
            target = k + power
            for j in self.c_rows(x, target):
                out[j, target] += self.c(x + j * self.L + target * self.M) * dot
        return clean(out)

    def formula(self, x, r):
        ap = sum((self.c(x + j*self.L)**2 for j in self.c_rows(x, 0) if j < 0), Q(0))
        aq = sum((self.d(x + k*self.M)**2 for k in self.d_rows(x) if k < 0), Q(0))
        if not r:
            return ap + aq
        z0 = sum((self.f(x + k*self.M)**2 for k in self.f_rows(x) if k < 0), Q(0))
        zr = sum((self.f(x + k*self.M) * self.f(x + (k-r)*self.M)
                  for k in self.f_rows(x) if k < 0 and k-r < 0), Q(0))
        return ap + aq - ap**2 - z0 + zr + ap * self.f(x - abs(r)*self.M)

    def tail(self, x, r):
        alpha = sum((self.f(x+k*self.M)**2 for k in self.f_rows(x)), Q(0))
        beta = sum((self.f(x+k*self.M) * self.f(x+(k-r)*self.M)
                    for k in self.f_rows(x)), Q(0))
        return Q(r == 0) + 1 - alpha + beta


def clean(vector):
    return {key: value for key, value in vector.items() if value}


def inner(left, right):
    return sum((value * right.get(key, Q(0)) for key, value in left.items()), Q(0))


def main():
    checks = Counter()

    def check(condition, name):
        assert condition, name
        checks[name] += 1

    for length, period in ((5, 7), (7, 5)):
        model = Fibre(length, period)
        for x in range(-28, 78):
            check(sum((model.c(x+j*length)**2 for j in model.c_rows(x, 0)), Q(0)) == 1,
                  "pointwise_p_partition")
            check(sum((model.d(x+k*period)**2 for k in model.d_rows(x)), Q(0)) == 1,
                  "pointwise_q_partition")
            vector = model.vector(x)
            for r in range(-4, 5):
                moved = model.source(x, vector, r)
                check(inner(vector, moved) == model.formula(x, r), "full_mixed_gram_formula")
                check(inner(moved, moved) == inner(vector, vector), "source_unitary_norm")
                repeated = vector
                for _ in range(abs(r)):
                    repeated = model.source(x, repeated, 1 if r > 0 else -1)
                check(moved == repeated, "integer_source_power_without_truncation")
                check(model.source(x, moved, -r) == vector, "source_inverse")
                check(model.formula(x, r) == model.formula(x, -r), "gram_adjoint_symmetry")
                if x >= 2*max(length, period) + 4*period:
                    check(model.formula(x, r) == model.tail(x, r), "exact_right_tail")
                check(model.tail(x+period, r) == model.tail(x, r), "right_tail_periodicity")
        # These use actual orbit vectors, independently of the scalar tail formula.
        for x0 in range(period):
            x = x0 + 12*period + 2*length
            for indices, coefficients in (
                ((-2, 0, 3), (Q(1), Q(-2), Q(3))),
                ((-1, 0, 1, 2), (Q(2, 3), Q(-3, 5), Q(5, 7), Q(1, 2))),
                ((0, 1, 4), (Q(1), Q(1), Q(1))),
            ):
                vector = model.vector(x)
                combined = defaultdict(Q)
                for j, coefficient in zip(indices, coefficients):
                    for key, value in model.source(x, vector, j).items():
                        combined[key] += coefficient * value
                actual = inner(combined, combined)
                symbol = sum((coefficients[j]*coefficients[k]*model.tail(x, indices[k]-indices[j])
                              for j in range(len(indices)) for k in range(len(indices))), Q(0))
                check(actual == symbol, "actual_finite_orbit_gram")
                check(actual >= sum((coefficient**2 for coefficient in coefficients), Q(0)),
                      "finite_gram_identity_lower_bound")
    result = {
        "status": "passed_exact_finite_source_fibre_models",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
        "checks": dict(sorted(checks.items())),
        "total_exact_assertions": sum(checks.values()),
        "arithmetic": "fractions.Fraction only; all nonzero source rows, no coordinate truncation",
        "models": [{"p_period": 5, "q_period": 7}, {"p_period": 7, "q_period": 5}],
        "scope": "Pointwise rational discrete partitions and finite source fibres audit source powers, full mixed Gram, exact periodic tail and finite Gram lower bound. Integer periods are commensurate; these are not the original smooth log-prime frame. No essential-norm, trace-class analytic, HH1, full Chern, arithmetic readout, RR or RH proof.",
    }
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "scope"}))


if __name__ == "__main__":
    main()

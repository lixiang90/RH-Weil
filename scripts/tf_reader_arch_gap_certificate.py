"""Exact rational certificate for the fixed (0,1) cosine compression.

This is an operator-error input, not a numerical Weil/T_F experiment.
K_N(x,y)=sum_{j=0}^N c_j x^(2j)y^(2j), c_j=2(-1)^j(2*pi)^(2j)/(2j)!.
H_ij=1/(2i+2j+1). If a H^{-1} +/- diag(c_j) are positive definite,
then ||K_N||<a. The real Taylor remainder bounds ||K_0-K_N|| by eps.
Every bound below uses rational or outward-rounded integer arithmetic.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path


def atan_interval(q: int, terms: int) -> tuple[F, F]:
    value = sum((F((-1) ** k, (2*k+1)*q**(2*k+1)) for k in range(terms)), F(0))
    other = value + F((-1) ** terms, (2*terms+1)*q**(2*terms+1))
    return min(value, other), max(value, other)


def floor_fraction(value: F) -> int:
    return value.numerator // value.denominator


def ceil_fraction(value: F) -> int:
    return -((-value.numerator) // value.denominator)


class Intervals:
    """Endpoints are integers representing endpoint / 10**precision."""
    def __init__(self, precision: int):
        self.unit = 10 ** precision

    def enclose(self, low: F, high: F | None = None):
        if high is None:
            high = low
        return floor_fraction(low*self.unit), ceil_fraction(high*self.unit)

    def add(self, x, y):
        return x[0]+y[0], x[1]+y[1]

    def neg(self, x):
        return -x[1], -x[0]

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        candidates = [a*b for a in x for b in y]
        return min(candidates)//self.unit, -((-max(candidates))//self.unit)

    def div(self, x, y):
        if y[0] <= 0 <= y[1]:
            raise ArithmeticError("Interval divisor contains zero")
        candidates = [F(a*self.unit, b) for a in x for b in y]
        return floor_fraction(min(candidates)), ceil_fraction(max(candidates))


def cauchy_gram_inverse(i: int, j: int, n: int) -> F:
    pi = 1
    pj = 1
    for k in range(n+1):
        pi *= 2*i+2*k+1
        pj *= 2*j+2*k+1
    return F((-1)**(i+j)*pi*pj,
             (2*i+2*j+1)*2**(2*n)*factorial(i)*factorial(n-i)*factorial(j)*factorial(n-j))


def positive_ldl(matrix, arithmetic: Intervals):
    n = len(matrix)
    zero = arithmetic.enclose(F(0))
    one = arithmetic.enclose(F(1))
    lower = [[zero for _ in range(n)] for _ in range(n)]
    pivots = []
    for j in range(n):
        lower[j][j] = one
        value = matrix[j][j]
        for k in range(j):
            term = arithmetic.mul(arithmetic.mul(lower[j][k], lower[j][k]), pivots[k])
            value = arithmetic.sub(value, term)
        if value[0] <= 0:
            raise ArithmeticError(f"Positive pivot not certified at {j}: {value}")
        pivots.append(value)
        for i in range(j+1, n):
            value = matrix[i][j]
            for k in range(j):
                term = arithmetic.mul(arithmetic.mul(lower[i][k], lower[j][k]), pivots[k])
                value = arithmetic.sub(value, term)
            lower[i][j] = arithmetic.div(value, pivots[j])
    return pivots


def certificate(n: int, precision: int, terms: int):
    atan5 = atan_interval(5, terms)
    atan239 = atan_interval(239, terms)
    pi_low = 16*atan5[0]-4*atan239[1]
    pi_high = 16*atan5[1]-4*atan239[0]
    arithmetic = Intervals(precision)
    # Keep the published rational witness short while rounding outwards.
    pi_low = F(floor_fraction(pi_low*arithmetic.unit), arithmetic.unit)
    pi_high = F(ceil_fraction(pi_high*arithmetic.unit), arithmetic.unit)
    a = F(999999, 1000000)
    inverse = [[cauchy_gram_inverse(i, j, n) for j in range(n+1)]
               for i in range(n+1)]
    # Validate the actual finite witness, independently of its closed form.
    for i in range(n+1):
        for j in range(n+1):
            product = sum((inverse[i][k]*F(1, 2*k+2*j+1)
                           for k in range(n+1)), F(0))
            if product != int(i == j):
                raise ArithmeticError("Cauchy Gram inverse failed exact identity")
    coefficients = []
    for j in range(n+1):
        low = F(2, factorial(2*j))*(2*pi_low)**(2*j)
        high = F(2, factorial(2*j))*(2*pi_high)**(2*j)
        if j % 2:
            low, high = -high, -low
        coefficients.append(arithmetic.enclose(low, high))
    base = [[arithmetic.enclose(a*inverse[i][j])
             for j in range(n+1)] for i in range(n+1)]
    results = {}
    for sign in (-1, 1):
        matrix = [row[:] for row in base]
        for j in range(n+1):
            matrix[j][j] = arithmetic.add(matrix[j][j],
                coefficients[j] if sign == 1 else arithmetic.neg(coefficients[j]))
        pivots = positive_ldl(matrix, arithmetic)
        results[str(sign)] = [{"lower": str(x), "upper": str(y)} for x, y in pivots]
    remainder_exact = F(2, factorial(2*n+2))*(2*pi_high)**(2*n+2)
    remainder = F(ceil_fraction(remainder_exact*arithmetic.unit), arithmetic.unit)
    norm_upper = a+remainder
    gap_lower = F(floor_fraction((1-norm_upper**2)*arithmetic.unit), arithmetic.unit)
    if gap_lower <= 0:
        raise ArithmeticError("Taylor remainder does not leave a positive gap")
    return {"schema": "tf-reader-arch-gap-exact-v1", "scope": "Fixed physical cutoff1, K0 kernel2cos(2*pi*x*y) on(0,1); not T_F or Weil numerics.",
        "n": n, "precision": precision, "arctan_terms": terms,
        "gram_inverse_exact_identity_verified": True,
        "ldl_interval_unit": str(arithmetic.unit), "pi_interval": [str(pi_low), str(pi_high)],
        "polynomial_norm_upper": str(a), "taylor_remainder_upper": str(remainder),
        "operator_norm_upper": str(norm_upper), "one_minus_norm_squared_lower": str(gap_lower),
        "resolvent_norm_upper": str(F(ceil_fraction(arithmetic.unit/gap_lower), arithmetic.unit)),
        "positive_pivot_intervals": results,
        "conclusion": "Both aHinv +/- C positive by outward interval LDL; Taylor HS remainder gives actual K0 gap and R0 bound. No infinite-dimensional residual inferred from a finite candidate alone."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--degree", type=int, default=20)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--terms", type=int, default=100)
    args = parser.parse_args()
    record = certificate(args.degree, args.precision, args.terms)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((json.dumps(record, indent=2)+"\n").encode())
    gap = F(record["one_minus_norm_squared_lower"])
    print(json.dumps({"status": "certified", "degree": args.degree,
                      "gap_gt_1e_minus6": gap > F(1, 10**6),
                      "R0_lt_1e6": 1/gap < 10**6, "output": str(output)}))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite MT triple/slack audit and an exact rational global certificate.

The certificate proves sum K(a)^2,K(b)^2,K(a+b)^2 >= 1/10000 on
a,b >= 0, a+b <= 4.  K is the SHARP normalized MT kernel, with Fourier
convention exp(-2*pi*i*v*u), support [-1/2,1/2].  Every bound used for
accepting a box is rational: Machin alternating series bounds for pi,
integer square-root bounds for 1/sqrt(2), fixed-point outward rounding,
and the explicit sinc Taylor remainder.  No floating-point optimization
selects or accepts boxes.  Failed depth/node/time limits raise an error.

The separate MP80 matrix and sampling checks have status [E].  They use
synthetic Hermitian/Weil matrices, not actual zeros or a prime-side sum.
Neither finite experiments nor the kernel certificate prove the required
external pair-correlation theorem or any zeta proportion on their own.
No files are written; only the Python standard library and mpmath are used.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial, isqrt
import json
import random
import time

import mpmath as mp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def ceildiv(a, b):
    return -((-a) // b)


def atan_reciprocal_bounds(q, count):
    partial = sum((Fraction((-1) ** k, (2*k+1)*q**(2*k+1))
                   for k in range(count)), Fraction())
    other = partial + Fraction((-1) ** count, (2*count+1)*q**(2*count+1))
    return min(partial, other), max(partial, other)


class RationalKernel:
    """Intervals are integer endpoints divided by one common exact scale."""

    def __init__(self, bits=128, terms=48):
        self.scale = 1 << bits
        self.bits, self.terms = bits, terms
        a, b = atan_reciprocal_bounds(5, 48)
        c, d = atan_reciprocal_bounds(239, 12)
        self.pi = self.from_fractions(16*a-4*d, 16*b-4*c)
        root = isqrt(self.scale*self.scale // 2)
        self.beta = root, root+1
        self.denominator = tuple(2*x for x in self.sinc(self.beta))
        require(self.denominator[0] > 0, "positive sinc normalization")
        self.cache = {}

    def from_fractions(self, lo, hi):
        s = self.scale
        return lo.numerator*s//lo.denominator, ceildiv(hi.numerator*s, hi.denominator)

    @staticmethod
    def add(a, b):
        return a[0]+b[0], a[1]+b[1]

    @staticmethod
    def neg(a):
        return -a[1], -a[0]

    def mul(self, a, b):
        products = [x*y for x in a for y in b]
        return min(products)//self.scale, ceildiv(max(products), self.scale)

    @staticmethod
    def div_integer(a, n):
        return a[0]//n, ceildiv(a[1], n)

    def divide_positive(self, a, b):
        require(b[0] > 0, "positive interval divisor")
        return (min(x*self.scale//y for x in a for y in b),
                max(ceildiv(x*self.scale, y) for x in a for y in b))

    def sinc(self, x):
        # sin(x)/x = sum_{k=0}^m (-1)^k x^(2k)/(2k+1)! + remainder.
        # Taylor's theorem applied to sin through degree 2m+2 gives the
        # globally valid real remainder |x|^(2m+2)/(2m+3)!, including x=0.
        s, m = self.scale, self.terms
        x2 = self.mul(x, x)
        term = total = (s, s)
        for k in range(1, m+1):
            term = self.div_integer(self.neg(self.mul(term, x2)), (2*k)*(2*k+1))
            total = self.add(total, term)
        height = max(abs(x[0]), abs(x[1]))
        remainder = ceildiv(height**(2*m+2), s**(2*m+1)*factorial(2*m+3))
        return total[0]-remainder, total[1]+remainder

    def kernel(self, coordinate):
        if coordinate not in self.cache:
            raw = self.mul(self.pi, (coordinate, coordinate))
            plus = self.sinc(self.add(raw, self.beta))
            minus = self.sinc(self.add(raw, self.neg(self.beta)))
            self.cache[coordinate] = self.divide_positive(self.add(plus, minus), self.denominator)
        return self.cache[coordinate]


def exact_certificate(max_depth, max_nodes, max_seconds):
    start = time.perf_counter()
    kernel = RationalKernel()
    scale = kernel.scale
    stack = [(0, 0, 0)]
    visited = leaves = pruned = deepest = 0
    least_square_numerator = None
    while stack:
        i, j, depth = stack.pop()
        visited += 1
        require(visited <= max_nodes, "rational certificate node limit; NOT certified")
        if visited % 512 == 0:
            require(time.perf_counter()-start <= max_seconds,
                    "rational certificate time limit; NOT certified")
        denominator = 1 << depth
        # This box is [4i/2^depth,4(i+1)/2^depth] times the analogous j box.
        # Boxes merely touching a+b=4 are retained.  Intersecting boundary
        # boxes are certified on the whole box, which is a safe enlargement.
        if i+j > denominator:
            pruned += 1
            continue
        require(depth+1 < kernel.bits, "dyadic centers must be exactly represented")
        ca = (2*(2*i+1)*scale)//denominator
        cb = (2*(2*j+1)*scale)//denominator
        radius = ceildiv(2*kernel.pi[1], denominator)
        # |K'| <= 2*pi*integral |u| f0(u)du <= pi.  For K(a+b), the
        # half-width is twice that of either individual coordinate.
        square_numerator = 0
        for center, error in ((ca, radius), (cb, radius), (ca+cb, 2*radius)):
            lo, hi = kernel.kernel(center)
            lo, hi = lo-error, hi+error
            distance = lo if lo > 0 else (-hi if hi < 0 else 0)
            square_numerator += distance*distance
        if 10000*square_numerator >= scale*scale:
            leaves += 1
            deepest = max(deepest, depth)
            least_square_numerator = (square_numerator if least_square_numerator is None
                                     else min(least_square_numerator, square_numerator))
            continue
        require(depth < max_depth, "rational certificate depth limit; NOT certified")
        stack.extend((2*i+di, 2*j+dj, depth+1) for di in (0, 1) for dj in (0, 1))
    require(leaves > 0, "nonempty exact cover")
    lower = Fraction(least_square_numerator, scale*scale)
    require(lower >= Fraction(1, 10000), "global rational threshold")
    return {"status": "PASS exact rational kernel certificate", "B": 4,
            "threshold": "1/10000", "leaves": leaves, "outside_boxes": pruned,
            "visited_boxes": visited, "maximum_leaf_depth": deepest,
            "cached_kernel_centers": len(kernel.cache), "bits": kernel.bits,
            "sinc_last_index": kernel.terms,
            "minimum_leaf_lower_bound": str(lower),
            "minimum_leaf_lower_decimal_display_only": float(lower),
            "seconds": round(time.perf_counter()-start, 3)}


def sinc(x):
    return mp.mpf(1) if x == 0 else mp.sin(x)/x


def mt_kernel(v):
    beta = 1/mp.sqrt(2)
    return (sinc(mp.pi*v-beta)+sinc(mp.pi*v+beta))/(2*sinc(beta))


def trace(matrix):
    return mp.re(sum(matrix[i, i] for i in range(matrix.rows)))


def hs2(matrix):
    return sum(abs(x)**2 for x in matrix)


def defect(p):
    return (p-1)**2-max(p-2, 0)**2


def jtrace(gram):
    values = list(mp.eigh(gram, eigvals_only=True))
    require(min(values) >= -mp.mpf("1e-65"), "positive Gram, up to MP error")
    return sum(defect(max(value, 0)) for value in values)


def principal(matrix, indices):
    return mp.matrix([[matrix[i, j] for j in indices] for i in indices])


def matrix_check(name, synthesis, operator, b, expected_trace):
    tolerance = mp.mpf("1e-55")
    gram = synthesis.H*synthesis
    p = synthesis*synthesis.H
    s = synthesis.cols
    q = operator-p
    q_values = list(mp.eigh(q, eigvals_only=True))
    require(sum(value > tolerance for value in q_values) <= b, "positive inertia bound for Q")
    require(abs(trace(p)-s) < tolerance, "unit simple-vector traces")
    require(abs(trace(operator)-expected_trace) < tolerance, "original whole trace")
    require(expected_trace >= s+2*b-tolerance, "rank/trace multiplicity ledger")
    slack = hs2(operator)-2*expected_trace+s
    penalty = jtrace(gram)
    ledger_surplus = 2*(expected_trace-s-2*b)
    require(slack >= penalty+ledger_surplus-tolerance, "convex-j slack bridge")
    blocks = [list(range(i, min(i+3, s))) for i in range(0, s, 3)]
    pinched = sum(jtrace(principal(gram, block)) for block in blocks)
    require(penalty >= pinched-tolerance, "scalar-Jensen block pinching")
    return {"name": name, "simple_rank": s, "b": b,
            "whole_slack": mp.nstr(slack, 14), "j_Gram": mp.nstr(penalty, 14),
            "pinched_j": mp.nstr(pinched, 14)}


def finite_matrix_checks():
    rng = random.Random(30420260906)

    def random_columns(rows, cols, complex_values=False):
        mat = mp.matrix(rows, cols)
        for j in range(cols):
            column = [mp.mpf(rng.randint(-20, 20))/19 for _ in range(rows)]
            if complex_values:
                column = [z+mp.j*mp.mpf(rng.randint(-20, 20))/23 for z in column]
            norm = mp.sqrt(sum(abs(z)**2 for z in column))
            for i, value in enumerate(column):
                mat[i, j] = value/norm
        return mat

    rows = []
    for s, b, negative, complex_values in ((3, 1, 1, False), (6, 2, 2, False),
                                            (4, 2, 1, True), (6, 1, 2, True)):
        dimension = s+b+negative
        x = random_columns(dimension, s, complex_values)
        if s == 6 and b == 1:
            x = mp.matrix(dimension, s)
            for j in range(s):
                x[0, j], x[j+1, j] = mp.sqrt(mp.mpf(".8")), mp.sqrt(mp.mpf(".2"))
        y = random_columns(dimension, b, complex_values)
        z = random_columns(dimension, negative, complex_values)
        q = ((2*b+negative)/mp.mpf(b))*(y*y.H)-z*z.H
        rows.append(matrix_check("synthetic Hermitian", x, x*x.H+q, b, s+2*b))

    # A genuine finite exponential/Weil-form construction, still synthetic.
    simple = [mp.mpf(x)/3 for x in (-7, -4, -1, 2, 5, 8)]
    repeated = [(mp.mpf("3.4"), 2)]
    pairs = [(mp.mpc(".4", ".25"), 1), (mp.mpc("1.5", ".2"), 2)]
    specs = [[(x, mp.mpf(1))] for x in simple]
    specs += [[(x, mp.mpf(1))] for x, _ in repeated]
    specs += [[(z, mp.mpf(".5")), (mp.conj(z), mp.mpf(".5"))] for z, _ in pairs]
    specs += [[(z, -mp.j/2), (mp.conj(z), mp.j/2)] for z, _ in pairs]
    gram = mp.matrix(len(specs))
    for i, left in enumerate(specs):
        for j, right in enumerate(specs):
            value = sum(c*mp.conj(d)*mt_kernel(z-mp.conj(w))
                        for z, c in left for w, d in right)
            require(abs(mp.im(value)) < mp.mpf("1e-65"), "real-type Gram")
            gram[i, j] = mp.re(value)
    synthesis = mp.cholesky(gram).T
    coefficients = [1]*len(simple)+[m for _, m in repeated]
    coefficients += [2*m for _, m in pairs]+[-2*m for _, m in pairs]
    operator = synthesis*mp.diag(coefficients)*synthesis.T
    total = len(simple)+sum(m for _, m in repeated)+2*sum(m for _, m in pairs)
    rows.append(matrix_check("synthetic MT Weil form", synthesis[:, :len(simple)],
                             operator, len(repeated)+len(pairs), total))
    return rows


def finite_triple_checks():
    rng = random.Random(304)
    rows = []
    for bound in (4, 5, 6):
        count = 48
        kernels = [mt_kernel(mp.mpf(bound)*i/count) for i in range(count+1)]
        candidates = [(kernels[i]**2+kernels[j]**2+kernels[i+j]**2,
                       mp.mpf(bound)*i/count, mp.mpf(bound)*j/count)
                      for i in range(count+1) for j in range(count+1-i)]
        minimum = min(candidates)
        for _ in range(24):
            a = mp.mpf(rng.randrange(1, 1000000))/1000000*bound
            b = mp.mpf(rng.randrange(1, 1000000))/1000000*(bound-a)
            values = (mt_kernel(a), mt_kernel(b), mt_kernel(a+b))
            g = mp.matrix([[1, values[0], values[2]],
                           [values[0], 1, values[1]], [values[2], values[1], 1]])
            energy = sum(value**2 for value in values)
            require(jtrace(g) >= mp.mpf("1.5")*energy-mp.mpf("1e-60"),
                    "three-vector j lower bound")
        rows.append({"B": bound, "grid_subdivisions": count,
                     "grid_minimum_E_only": mp.nstr(minimum[0], 14),
                     "at": [mp.nstr(minimum[1], 12), mp.nstr(minimum[2], 12)]})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=24)
    parser.add_argument("--max-nodes", type=int, default=1000000)
    parser.add_argument("--max-seconds", type=float, default=120)
    args = parser.parse_args()
    start = time.perf_counter()
    print(json.dumps(exact_certificate(args.max_depth, args.max_nodes, args.max_seconds)), flush=True)
    mp.mp.dps = 80
    print(json.dumps({"status": "[E] finite matrices PASS", "cases": finite_matrix_checks()}), flush=True)
    print(json.dumps({"status": "[E] finite MT samples PASS", "cases": finite_triple_checks()}), flush=True)
    require(2*13**2*Fraction(1, 110000) < Fraction(1, 300), "older conservative rational error")
    require(29*Fraction(1, 300)+Fraction(1, 300)**2 < Fraction(1, 10), "rational contradiction cost")
    print(json.dumps({"status": "PASS", "actual_zeros_used": False,
                      "global_certificate_uses_optimizer": False,
                      "zeta_asymptotic_certified_by_script": False,
                      "seconds": round(time.perf_counter()-start, 3)}), flush=True)


if __name__ == "__main__":
    main()

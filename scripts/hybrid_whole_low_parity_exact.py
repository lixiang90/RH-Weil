"""Exact whole-low parity path integrals; algebra only, not analytic admission."""

from fractions import Fraction as F
from itertools import product
from math import factorial
import json


def value(form, point):
    c, a, b = form
    x, y = point
    return c + a * x + b * y


def subtract(f, g):
    return tuple(a - b for a, b in zip(f, g))


def clip(poly, form):
    if not poly:
        return []
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp, fq = value(form, p), value(form, q)
        if fp >= 0:
            out.append(p)
        if (fp > 0 and fq < 0) or (fp < 0 and fq > 0):
            ratio = fp / (fp - fq)
            out.append(tuple(p[i] + ratio * (q[i] - p[i]) for i in range(2)))
    result = []
    for p in out:
        if not result or p != result[-1]:
            result.append(p)
    if len(result) > 1 and result[0] == result[-1]:
        result.pop()
    return result


def multiply(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            key = i + k, j + l
            out[key] = out.get(key, F(0)) + a * b
    return out


def triangle_integral(p, q, r, length):
    """Integrate x*y*length over the triangle using exact simplex moments."""
    det = abs((q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]))
    if not det:
        return F(0)
    factors = [
        {(0, 0): p[0], (1, 0): q[0] - p[0], (0, 1): r[0] - p[0]},
        {(0, 0): p[1], (1, 0): q[1] - p[1], (0, 1): r[1] - p[1]},
        {(0, 0): value(length, p), (1, 0): value(length, q) - value(length, p),
         (0, 1): value(length, r) - value(length, p)},
    ]
    polynomial = {(0, 0): F(1)}
    for factor in factors:
        polynomial = multiply(polynomial, factor)
    return det * sum(c * F(factorial(i) * factorial(j), factorial(i + j + 2))
                     for (i, j), c in polynomial.items())


def overlap_integral(steps, labels, initial_half):
    """Half is +1 on [0,1/2], -1 on [-1/2,0]."""
    if labels.count("o") % 2:
        return F(0), 0
    half = initial_half
    shift = (F(0), F(0))
    lower, upper = [], []
    for j in range(5):
        lo, hi = (F(0), F(1, 2)) if half == 1 else (F(-1, 2), F(0))
        lower.append((lo, -shift[0], -shift[1]))
        upper.append((hi, -shift[0], -shift[1]))
        if j < 4:
            shift = tuple(shift[i] + steps[j][i] for i in range(2))
            if labels[j] == "o":
                half = -half
    assert shift == (0, 0) and half == initial_half
    lower, upper = sorted(set(lower)), sorted(set(upper))
    square = [(F(0), F(0)), (F(1, 2), F(0)),
              (F(1, 2), F(1, 2)), (F(0), F(1, 2))]
    total, cells = F(0), 0
    for lo, hi in product(lower, upper):
        poly = square
        for other in lower:
            poly = clip(poly, subtract(lo, other))
        for other in upper:
            poly = clip(poly, subtract(other, hi))
        length = subtract(hi, lo)
        poly = clip(poly, length)
        if len(poly) < 3:
            continue
        integral = sum(triangle_integral(poly[0], poly[i], poly[i + 1], length)
                       for i in range(1, len(poly) - 1))
        if integral:
            assert integral > 0
            cells += 1
            total += integral
    return total, cells


def path_integrals():
    result = {}
    for labels_tuple in product("eo", repeat=4):
        labels = "".join(labels_tuple)
        by_pairing = {}
        cells = 0
        for pairing in ("A", "A_prime", "O"):
            total = F(0)
            for sigma, eta, half in product((-1, 1), repeat=3):
                x, y = (F(sigma), F(0)), (F(0), F(eta))
                nx, ny = tuple(-v for v in x), tuple(-v for v in y)
                steps = {"A": (x, nx, y, ny), "A_prime": (x, y, ny, nx),
                         "O": (x, y, nx, ny)}[pairing]
                integral, count = overlap_integral(steps, labels, half)
                total += integral
                cells += count
            by_pairing[pairing] = total
        result[labels] = {"pairings": by_pairing,
                          "total": sum(by_pairing.values()), "positive_cells": cells}
    assert result["eeee"]["total"] == F(1, 60)
    assert result["oooo"]["total"] == F(1, 60)
    assert result["eeoo"]["total"] == F(3, 320)
    assert result["eoeo"]["total"] == F(1, 240)
    assert sum(row["total"] for row in result.values()) == F(19, 240)
    return result


def integrate_polynomial(coefficients, upper=F(1, 2)):
    return sum(c * upper ** (i + 1) / (i + 1) for i, c in enumerate(coefficients))


def polynomial_product(a, b):
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def weighted_constants():
    ve, vo, w = [F(1, 8), F(-1, 2), F(1)], [F(1, 8), F(0), F(-1, 2)], [F(0), F(1, 2), F(1, 2)]
    output = {}
    for name, a, b in (("Se", ve, ve), ("So", vo, vo), ("Seo", ve, vo),
                       ("Ce", w, ve), ("Co", w, vo)):
        output[name] = 2 * integrate_polynomial(polynomial_product(a, b))
    output["second_even"] = 2 * integrate_polynomial(ve)
    output["second_odd"] = 2 * integrate_polynomial(vo)
    output["variance_even_low_square"] = F(1, 60) - output["Se"]
    output["variance_odd_low_square"] = F(1, 60) - output["So"]
    output["covariance_low_squares"] = F(3, 320) - output["Seo"]
    output["variance_even_total_square"] = (output["variance_even_low_square"]
        + output["variance_odd_low_square"] + 2 * output["covariance_low_squares"])
    output["variance_odd_total_square"] = 2 * (F(3, 320) + F(1, 240))
    expected = {"Se": F(7, 960), "So": F(1, 120), "Seo": F(13, 1920),
        "Ce": F(9, 640), "Co": F(19, 1920), "second_even": F(1, 12),
        "second_odd": F(1, 12), "variance_even_low_square": F(3, 320),
        "variance_odd_low_square": F(1, 120), "covariance_low_squares": F(1, 384),
        "variance_even_total_square": F(11, 480), "variance_odd_total_square": F(13, 480)}
    assert output == expected
    return output


def main():
    result = {"whole_low_fourth_paths": path_integrals(), "whole_weighted_constants": weighted_constants()}
    print(json.dumps(result, default=str, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

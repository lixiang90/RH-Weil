#!/usr/bin/env python3
"""Audit the scalar constants recorded in note 305, using rational arithmetic.

This does not verify any zero asymptotics or replay a local-gap interval search.
Decimal output is for display only; every comparison below uses Fraction.
Upstream provenance and the complete verification boundary are in note 305.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import factorial, isqrt


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def display(value):
    with localcontext() as ctx:
        ctx.prec = 45
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def alternating_bounds(offset, count=40):
    # cos(1/sqrt(2)) for offset=0; sinc(1/sqrt(2)) for offset=1.
    partial = sum((F((-1)**k, 2**k * factorial(2*k + offset))
                   for k in range(count)), F())
    other = partial + F((-1)**count,
                        2**count * factorial(2*count + offset))
    return min(partial, other), max(partial, other)


def sqrt_bounds(value, digits=60):
    scale = 10**digits
    root = isqrt(value.numerator * scale**2 // value.denominator)
    low, high = F(root, scale), F(root + 1, scale)
    require(low**2 <= value < high**2, "square-root enclosure")
    return low, high


def window_capacity(size, numerators, denominator):
    pairs = [(i, j) for i in range(size) for j in range(i + 1, size)]
    require(len(pairs) == len(numerators), "pair count")
    require(all(x >= 0 for x in numerators), "nonnegative pair weights")
    for span in range(1, size):
        total = sum(n for (i, j), n in zip(pairs, numerators)
                    if j - i == span)
        require(total == 2 * denominator, "exact span capacity")


def main():
    cos_lo, cos_hi = alternating_bounds(0)
    sinc_lo, sinc_hi = alternating_bounds(1)
    require(sinc_lo > 0, "positive denominator")
    c_lo = F(3, 2) - cos_hi / sinc_lo
    c_hi = F(3, 2) - cos_lo / sinc_hi
    require(c_hi - c_lo < F(1, 10**100), "MT enclosure width")

    internal = lambda c: (c - F(1, 40000)) / (1 - F(1, 20000))
    triple = lambda c: (c - F(221, 4000000)) / (1 - F(221, 2000000))
    seven = lambda c: (1345000*c - 2680) / 1340003
    require(seven(c_lo) > F(673, 1000), "ainta exceeds 67.3 percent")
    require(triple(c_lo) > internal(c_hi), "ainta triple exceeds note 304")

    # Exact tables from trmdy commit 1610b97b7895ff34982260f8dcaf04a0f7b82cf7.
    window_capacity(7, [
        236484,535224,969656,1000000,1000000,2000000,
        381281,464776,30344,0,1000000,382235,0,30344,1000000,
        382235,464776,969656,381281,535224,236484], 1000000)
    window_capacity(9, [
        1802576,4832031,5411933,10000000,10000000,10000000,10000000,20000000,
        2694869,2295599,1780844,0,0,0,10000000,
        2714860,0,2807223,0,0,10000000,2787695,5744740,2807223,0,10000000,
        2787695,0,1780844,10000000,2714860,2295599,5411933,
        2694869,4832031,1802576], 10000000)

    h = F(3362285207, 5000000000)
    eps9 = F(15211, 2500000)
    a9_old = eps9 * (177 - 8)
    root_old = sqrt_bounds(F(176, 177) * a9_old)
    r_old = [2*x - 1 + a9_old / 177 for x in root_old]
    old_bound = lambda r: (177*h - F(169*8, 2500)) / (177-r)
    old_lo, old_hi = [old_bound(r) for r in r_old]

    m = 219
    a7, a9 = F(891*213, 200000), eps9*211
    p7, p9 = F(1, 2736), F(1, 2500)
    require(a7 < F(m, m-1) < a9, "trace profile branches")
    require(a7/p7 - 3*a9/(4*p9) == F(18909069, 100000),
            "supporting-plane side condition")
    radicand = F(349837789, 273750000)
    r_lo, r_hi = [2*x - 1 + a9/m for x in sqrt_bounds(radicand)]
    require(a7 < r_lo < r_hi < a9 < 2, "positive interpolation weights")

    def joint_bound(r):
        u = (r - a7) / (a9 - a7)
        beta, gamma = (1-u)*p7, u*p9
        require(3*beta/(4*p9) + gamma/p9 < 1, "slope condition")
        tax = beta*6*213 + gamma*8*211
        require(tax == F(19769000,31814873)*r
                - F(389820601,3181487300), "affine pressure identity")
        return (m*h - tax) / (m-r)

    require(m*h + F(389820601,3181487300)
            - F(19769000,31814873)*m > 0, "bound increases with R")
    b_lo, b_hi = joint_bound(r_lo), joint_bound(r_hi)
    r0 = F(6333939, 5000000)
    require(radicand - ((r0+1-a9/m)/2)**2 ==
            F(239006467199, 4796100000000000000), "exact radical margin")
    require(joint_bound(r0) - F(673316977,10**9) ==
            F(4570374547679819,34635772470125253000000000),
            "strict rational comparison")
    require(F(673316977,10**9) < b_lo < b_hi < F(673399,10**6),
            "ordering of public values")

    for label, lo, hi in [
        ("MT baseline", c_lo, c_hi),
        ("note 304", internal(c_lo), internal(c_hi)),
        ("ainta triple", triple(c_lo), triple(c_hi)),
        ("ainta seven", seven(c_lo), seven(c_hi)),
        ("trmdy nine", old_lo, old_hi),
        ("Shi joint", b_lo, b_hi),
    ]:
        print(f"{label}: {display(lo)} .. {display(hi)}")
    for target in (F(673,1000), F(673399,10**6)):
        print(f"flat-window fourth-moment target for p={target}: "
              f"{display(F(4,9)/target-F(1,3))}")
    # MT v=1-C0; its threshold is C0^2/p + 1 - 2*C0.
    target = F(673399,10**6)
    mt_threshold = lambda c: c*c/target + 1 - 2*c
    # Derivative 2*C0/p-2 is negative on the certified C0 interval.
    require(c_hi < target, "MT threshold monotonicity")
    print("MT-window fourth-moment threshold for p=0.673399: "
          f"{display(mt_threshold(c_hi))} .. {display(mt_threshold(c_lo))}")
    print("PASS: scalar enclosures, exact side conditions, pair capacities.")
    print("NOT CHECKED: analytic interfaces, kernel inequalities, large certificates, Lean builds.")


if __name__ == "__main__":
    main()

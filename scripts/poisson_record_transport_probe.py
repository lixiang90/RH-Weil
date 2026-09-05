"""Finite MP50 [E] checks of Poisson transport of synthetic signed lag sources.

These three-atom BV models are NOT actual von Mangoldt sources or certified
arithmetic records. Integer lags make every symbol 2*pi-periodic; the wrapped
Poisson kernel therefore retains the whole real line, not a frequency cutoff.
Finite MP agreement is not interval certification or an asymptotic theorem.
Only mpmath is required. No files, network, registry, or plots are used.
"""

import sys
from time import perf_counter

import mpmath as mp

sys.dont_write_bytecode = True


def wrapped_poisson(width, angle):
    return mp.sinh(width) / (2 * mp.pi * (mp.cosh(width) - mp.cos(angle)))


def symbol(atoms, t, shift=0):
    return mp.fsum(c * mp.exp(-shift * u) * mp.cos(u * t) for u, c in atoms.items())


def history_intervals(atoms):
    last = mp.mpf(0)
    value = mp.mpf(0)
    intervals = []
    for location in sorted(atoms):
        intervals.append((last, mp.mpf(location), value))
        value += atoms[location]
        last = mp.mpf(location)
    return intervals, value


def exponential_integral(left, right, exponent):
    if exponent == 0:
        return right - left
    return mp.exp(exponent * left) * mp.expm1(exponent * (right - left)) / exponent


def weighted_history(atoms, shift, t):
    intervals, mass = history_intervals(atoms)
    length = max(atoms)
    transform = mp.fsum(h * exponential_integral(left, right, -shift + 1j*t)
                       for left, right, h in intervals)
    weighted_l1 = mp.fsum(abs(h) * exponential_integral(left, right, -shift)
                         for left, right, h in intervals)
    weighted_l2_sq = mp.fsum(h*h * exponential_integral(left, right, -2*shift)
                            for left, right, h in intervals)
    boundary = mass * mp.exp(-shift * length) * mp.cos(t * length)
    # Keep BOTH integral terms and the complete upper-endpoint atom.
    by_parts = boundary + shift * mp.re(transform) + t * mp.im(transform)
    return by_parts, weighted_l1, mp.sqrt(weighted_l2_sq)


def bisection(function, left, right):
    assert function(left) * function(right) < 0
    root = mp.findroot(function, (left, right), solver="bisect",
                       tol=mp.mpf("1e-35"), maxsteps=160)
    assert abs(function(root)) < mp.mpf("1e-27")
    return root


def original_roots(atoms):
    length = max(atoms)
    late = atoms[length]
    remainder_tv = mp.fsum(abs(c) for u, c in atoms.items() if u != length)
    assert late > remainder_tv
    # Values at k*pi/L alternate sign. A degree-L polynomial in cos(t)
    # has at most L roots on (0,pi), so these L brackets exhaust the roots.
    return [bisection(lambda t: symbol(atoms, t), k*mp.pi/length, (k+1)*mp.pi/length)
            for k in range(length)]


def shifted_roots(atoms, shift):
    length = max(atoms)
    early = -atoms[1]
    late = atoms[length] * mp.exp(-shift * length)
    assert atoms[2] == 2*early
    e1, e2 = mp.exp(-shift), mp.exp(-2*shift)
    quadratic = lambda x: early * (4*e2*x*x - e1*x - 2*e2)
    # The shifted early part is quadratic in x=cos(t). The remaining
    # late term is late*T_L(x); |T_L|<=1 and |T_L'|<=L^2 on [-1,1].
    # Verify monotonicity on each bracket and signs everywhere outside them.
    left_bracket = (mp.mpf("-0.75"), mp.mpf("-0.25"))
    right_bracket = (mp.mpf("0.75"), mp.mpf(1))
    assert early*(2*e2+e1) > late*length**2
    assert early*(6*e2-e1) > late*length**2
    assert quadratic(left_bracket[0]) > late
    assert quadratic(right_bracket[1]) > late
    assert max(quadratic(left_bracket[1]), quadratic(right_bracket[0])) < -late
    # On [-1,-.75] the quadratic decreases and stays positive; on
    # [-.25,.75] convexity bounds it by its two negative endpoint values.
    polynomial = lambda x: quadratic(x) + late * mp.chebyt(length, x)
    roots_x = [bisection(polynomial, *left_bracket), bisection(polynomial, *right_bracket)]
    return sorted(mp.acos(x) for x in roots_x)


def weighted_traces(atoms, shift, trace_width, roots):
    boundaries = [mp.mpf(0)] + roots + [mp.pi]
    positive = mp.mpf(0)
    negative = mp.mpf(0)
    for left, right in zip(boundaries, boundaries[1:]):
        integral = 2 * mp.quad(lambda t: symbol(atoms, t, shift) * wrapped_poisson(trace_width, t),
                              [left, right])
        if symbol(atoms, (left+right)/2, shift) > 0:
            positive += integral
        else:
            negative -= integral
    exact_mean = mp.fsum(c * mp.exp(-(shift+trace_width)*u) for u, c in atoms.items())
    assert abs(positive-negative-exact_mean) < mp.mpf("1e-32")
    return positive, negative, positive+negative


def main():
    started = perf_counter()
    mp.mp.dps = 50
    decay = mp.mpf(1)/8
    shift = mp.mpf(1)/2
    worst_poisson = mp.mpf(0)
    worst_ibp = mp.mpf(0)
    print("[E] Synthetic mixed-sign atoms only; fixed d=1/8, a=1/2, L=12,24.")
    print("[E] Wrapped Poisson and wrapped Cauchy kernels include the entire real line.")
    for length in (12, 24):
        early = mp.exp(-decay*length)
        atoms = {1: -early, 2: 2*early, length: 1-early}
        intervals, mass = history_intervals(atoms)
        assert abs(mass-1) < mp.mpf("1e-45")
        # The original signed cumulative path has guard constant exactly 1
        # as an admissible upper bound, including H(L)=M.
        for left, right, h in intervals:
            assert abs(h) <= abs(mass)*mp.exp(-decay*(length-left))
        before_roots = original_roots(atoms)
        after_roots = shifted_roots(atoms, shift)
        before = weighted_traces(atoms, 0, 1, before_roots)
        weighted_before = weighted_traces(atoms, 0, 1+shift, before_roots)
        after = weighted_traces(atoms, shift, 1, after_roots)
        assert after[0] <= weighted_before[0] + mp.mpf("1e-32")
        assert after[1] <= weighted_before[1] + mp.mpf("1e-32")
        assert after[2] <= weighted_before[2] + mp.mpf("1e-32")
        assert weighted_before[2] <= (1+shift)*before[2] + mp.mpf("1e-32")
        # For a>d, this is the explicit old-guard norm upper bound.
        _, w1, w2 = weighted_history(atoms, shift, mp.mpf(0))
        via_history = mp.exp(-shift*length) + shift*w1 + w2/mp.sqrt(2)
        guard_bound = mp.exp(-shift*length) + mp.exp(-decay*length) * (
            shift/(shift-decay) + 1/(2*mp.sqrt(shift-decay)))
        assert after[2] <= via_history + mp.mpf("1e-32")
        assert via_history <= guard_bound + mp.mpf("1e-32")
        _, h1, h2 = weighted_history(atoms, 0, mp.mpf(0))
        assert before[2] <= 1+h2/mp.sqrt(2)
        # Direct full-period convolution, independently of the atomwise tilt.
        grid = [j*mp.pi/(2*length) for j in range(4*length+1)]
        for t in (mp.mpf(0), mp.mpf("0.37"), mp.mpf("1.1")):
            convolution = mp.quad(lambda s: wrapped_poisson(shift, t-s)*symbol(atoms, s), grid)
            target = symbol(atoms, t, shift)
            worst_poisson = max(worst_poisson, abs(convolution-target))
            assert abs(convolution-target) < mp.mpf("1e-38")
            for sign in (1, -1):
                signed_atoms = {u: sign*c for u, c in atoms.items()}
                by_parts, _, _ = weighted_history(signed_atoms, shift, t)
                worst_ibp = max(worst_ibp, abs(by_parts-sign*target))
                assert abs(by_parts-sign*target) < mp.mpf("1e-40")
        print(f"[E] L={length}: L1 before={float(before[2]):.12g}, "
              f"after={float(after[2]):.12g}, weighted-before={float(weighted_before[2]):.12g}")
        print(f"[E] L={length}: path upper={float(via_history):.12g}, "
              f"guard upper={float(guard_bound):.12g}; H1={float(h1):.8g}, H2={float(h2):.8g}")
        print(f"[E] L={length}: Jensen deficits for P and -P = "
              f"{float(weighted_before[1]-after[1]):.12g}, {float(weighted_before[0]-after[0]):.12g}")
    print("[E] Maximum direct-Poisson/tilt discrepancy:", mp.nstr(worst_poisson, 8))
    print("[E] Maximum complete weighted-IBP discrepancy:", mp.nstr(worst_ibp, 8))
    print("[E] Nested min(Poisson P+, Poisson P-) integration was NOT performed.")
    print(f"PASS; elapsed_seconds={perf_counter()-started:.3f}; no files written.")


if __name__ == "__main__":
    main()

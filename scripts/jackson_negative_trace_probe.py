"""Finite checks for note 291; no actual zeta spectrum or asymptotic certificate.

Uses mpmath only. Integer convolution checks are exact; all other checks are
MP60 diagnostics, not interval certification. No files or network are used.
"""

from fractions import Fraction
from time import perf_counter

import mpmath as mp


def convolve(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, 0) + x * y
    return out


def add_scaled(a, b, scale=1):
    out = a.copy()
    for k, x in b.items():
        out[k] = out.get(k, 0) + scale * x
    return out


def kernel_coefficients(m):
    triangular = {j: m - abs(j) for j in range(1 - m, m)}
    fourth = convolve(triangular, triangular)
    normalization = (2 * m**3 + m) // 3
    assert fourth[0] == normalization
    assert sum(fourth.values()) == m**4
    assert all(0 < value <= normalization for value in fourth.values())
    assert all(fourth[-j] == value for j, value in fourth.items())
    if m <= 8:
        positive = convolve(dict.fromkeys(range(m), 1), dict.fromkeys(range(m), 1))
        independent = convolve(positive, {-j: v for j, v in positive.items()})
        assert independent == fourth
    return {j: Fraction(v, normalization) for j, v in fourth.items()}


def to_mp(q):
    return mp.mpf(q.numerator) / q.denominator


def chebyshev_coefficients(m):
    kernel = kernel_coefficients(m)
    coeff = [mp.mpf(0)] * (2 * m - 1)
    coeff[0] = mp.mpf("0.5")
    for j in range(1, len(coeff), 2):
        coeff[j] = -2 * (-1) ** ((j - 1) // 2) * to_mp(kernel[j]) / (mp.pi * j)
    return coeff


def evaluate(coeff, x):
    # Independent forward Chebyshev recurrence, not power-basis conversion.
    previous, current = mp.mpf(1), x
    result = coeff[0]
    for j in range(1, len(coeff)):
        result += coeff[j] * current
        previous, current = current, 2 * x * current - previous
    return result


def kernel_value(m, t):
    if abs(mp.sin(t / 2)) < mp.mpf("1e-55"):
        raw = mp.mpf(m)
    else:
        raw = mp.sin(m * t / 2) / mp.sin(t / 2)
    return raw**4 / ((2 * m**3 + m) / mp.mpf(3))


def scalar_probe():
    maximum_identity_error = mp.mpf(0)
    for m in (1, 2, 3, 4, 8, 16, 32):
        coeff = chebyshev_coefficients(m)
        points = [mp.mpf(j) / 200 for j in range(-200, 201)]
        points += [mp.mpf(j) / (20 * m) for j in range(-40, 41)]
        points = [x for x in points if abs(x) <= 1]
        maximum_gap = mp.mpf(0)
        for x in points:
            value = evaluate(coeff, x)
            gap = max(-x, 0) + x * value**2
            assert -mp.mpf("1e-50") <= value <= 1 + mp.mpf("1e-50")
            assert -mp.mpf("1e-50") <= gap <= 3 * mp.pi / m
            assert abs(value + evaluate(coeff, -x) - 1) < mp.mpf("1e-50")
            maximum_gap = max(maximum_gap, gap)
        if m <= 8:
            # Integrate the step over its exact half-circle, avoiding jumps.
            for x in (mp.mpf("-0.7"), mp.mpf(0), mp.mpf("0.23")):
                theta = mp.acos(x)
                boundaries = [mp.pi / 2 + j * mp.pi / (4 * m) for j in range(4 * m + 1)]
                integral = mp.quad(lambda y: kernel_value(m, theta - y), boundaries) / (2 * mp.pi)
                error = abs(integral - evaluate(coeff, x))
                maximum_identity_error = max(maximum_identity_error, error)
                assert error < mp.mpf("1e-45")
        print(f"[E] m={m}, degree<={2*m-2}, sampled max gap={float(maximum_gap):.12g}, "
              f"m*sampled gap={float(m*maximum_gap):.12g}; bound=3*pi")
    print("[E] max direct-step-integral/Chebyshev error =", mp.nstr(maximum_identity_error, 8))


def lag_polynomial(coeff, base, bound):
    previous = {0: mp.mpf(1)}
    current = {j: x / bound for j, x in base.items()}
    result = {0: coeff[0]}
    for j in range(1, len(coeff)):
        result = add_scaled(result, current, coeff[j])
        following = convolve(base, current)
        following = {k: 2 * x / bound for k, x in following.items()}
        following = add_scaled(following, previous, -1)
        previous, current = current, following
    return result


def lag_probe():
    # Fixed synthetic real symbol, NOT von Mangoldt/continuum/Gamma data.
    base = {0: -mp.mpf(1) / 5, -1: mp.mpf(9) / 20, 1: mp.mpf(9) / 20,
            -2: mp.mpf(3) / 20, 2: mp.mpf(3) / 20}
    bound = mp.mpf(7) / 5  # Independently certified total variation bound.
    assert sum(abs(x) for x in base.values()) == bound
    value = lambda t: -mp.mpf(1)/5 + mp.mpf(9)/10*mp.cos(t) + mp.mpf(3)/10*mp.cos(2*t)
    density = lambda t: mp.sinh(1) / (2 * mp.pi * (mp.cosh(1) - mp.cos(t)))
    # The negative part has one sign change on (0, pi); split there.
    root = mp.acos((-9 + mp.sqrt(201)) / 12)
    negative_trace = 2 * mp.quad(lambda t: -value(t) * density(t), [root, mp.pi])
    maximum_error = mp.mpf(0)
    for m in (2, 4, 8):
        coeff = chebyshev_coefficients(m)
        effect = lag_polynomial(coeff, base, bound)
        response = {j: -x for j, x in convolve(base, convolve(effect, effect)).items()}
        via_lags = mp.fsum(x * mp.exp(-abs(j)) for j, x in response.items())
        boundaries = [j * mp.pi / (8 * m) for j in range(8 * m + 1)]
        via_integral = -2 * mp.quad(
            lambda t: value(t) * evaluate(coeff, value(t) / bound)**2 * density(t),
            boundaries,
        )
        error = abs(via_lags - via_integral)
        maximum_error = max(maximum_error, error)
        assert error < mp.mpf("1e-42")
        gap = negative_trace - via_lags
        assert -mp.mpf("1e-42") <= gap <= 3 * mp.pi * bound / m
        # This bound is on polynomial degree; lag support also uses base degree 2.
        assert max(map(abs, response)) <= 2 * (4 * m - 3)
        print(f"[E] synthetic Cauchy m={m}: negative_trace={float(negative_trace):.12g}, "
              f"signed_response={float(via_lags):.12g}, gap={float(gap):.12g}, "
              f"lag/integral error={mp.nstr(error, 5)}")
    print("[E] max full-period Cauchy/lag-convolution error =", mp.nstr(maximum_error, 8))


def main():
    started = perf_counter()
    mp.mp.dps = 60
    print("Finite exact integer kernels + MP60 probes; no interval, spectral, or RH certificate.")
    scalar_probe()
    lag_probe()
    print(f"PASS; elapsed_seconds={perf_counter()-started:.3f}; no files written.")


if __name__ == "__main__":
    main()

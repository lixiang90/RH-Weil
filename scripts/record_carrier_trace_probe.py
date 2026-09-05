"""Finite [E] checks of the record-carrier identities, using synthetic BV paths.

The deterministic models below are NOT von Mangoldt sources, actual zeta zeros,
or certified arithmetic records. MP50 checks do not prove an asymptotic bound
or certify continuum extrema. The full Cauchy mean/L2 checks use the exact
characteristic kernel exp(-abs(u-v)), not an unreported frequency cutoff.
Only mpmath is required. No files, network, registry, or plots are used.
"""

import sys
from time import perf_counter

import mpmath as mp

sys.dont_write_bytecode = True


class PathModel:
    """H(u)=M*(exp(delta*u)-1)/(exp(delta*L)-1), 0<=u<=L."""

    def __init__(self, length, delta, mass=1):
        self.length = mp.mpf(length)
        self.delta = mp.mpf(delta)
        self.mass = mp.mpf(mass)
        assert self.length > 0 and 0 < self.delta < 1 and self.mass != 0
        self.r = mp.exp(-self.delta * self.length)
        self.denominator = -mp.expm1(-self.delta * self.length)
        self.prefactor = self.mass * self.delta / self.denominator

    def history(self, u):
        return self.mass * (mp.exp(self.delta * (u - self.length)) - self.r) / self.denominator

    def density(self, u):
        return self.prefactor * mp.exp(self.delta * (u - self.length))

    def backward_transform(self, q):
        z = self.delta + 1j * q
        first = -mp.expm1(-z * self.length) / z
        second = self.length if q == 0 else -mp.expm1(-1j * q * self.length) / (1j * q)
        return self.mass * (first - self.r * second) / self.denominator

    def amplitude(self, q):
        z = self.delta + 1j * q
        return self.prefactor * (-mp.expm1(-z * self.length)) / z

    def symbol(self, q):
        # Direct cosine transform of dH, independent of the carrier assembly.
        numerator = mp.exp(1j * self.length * q) - self.r
        return self.prefactor * mp.re(numerator / (self.delta + 1j * q))

    def zero_numerator(self, q):
        return self.delta * mp.cos(self.length * q) + q * mp.sin(self.length * q) - self.delta * self.r

    def cauchy_closed(self):
        # E cos(u*t)=exp(-u); E cos(u*t)cos(v*t)
        # = (exp(-abs(u-v))+exp(-u-v))/2, for u,v>=0.
        d, r, length = self.delta, self.r, self.length
        small_integral = -mp.expm1(-(1 - d) * length) / (1 - d)
        a = self.prefactor * r
        mean = a * small_integral
        square = self.prefactor**2 / (d + 1) * (
            (1 - r**2) / (2 * d) - r**2 * small_integral
        ) + mean**2 / 2
        history_l2 = self.mass**2 / self.denominator**2 * (
            (1 - r**2) / (2 * d) - 2 * r * (1 - r) / d + r**2 * length
        )
        return mean, square, history_l2


def cauchy_weight(q):
    return 1 / (mp.pi * (1 + q**2))


def quarter_period_grid(length, endpoint):
    step = mp.pi / (2 * length)
    points = [j * step for j in range(int(mp.floor(endpoint / step)) + 1)]
    if points[-1] < endpoint:
        points.append(endpoint)
    return points


def finite_negative_traces(model, endpoint):
    """Split every sign change; both signs of M use the same exact zero set."""
    assert model.length >= 2 / model.delta and model.mass > 0
    grid = quarter_period_grid(model.length, endpoint)
    roots = []
    for left, right in zip(grid, grid[1:]):
        f_left = model.zero_numerator(left)
        f_right = model.zero_numerator(right)
        if f_left * f_right < 0:
            root = mp.findroot(model.zero_numerator, (left, right), solver="bisect",
                               tol=mp.mpf("1e-35"), maxsteps=160)
            assert abs(model.zero_numerator(root)) < mp.mpf("1e-28")
            roots.append(root)
    # Write phi=L*q-atan(q/delta), alpha=acos(r*delta/sqrt(delta^2+q^2)).
    # phi'>=1/delta and 0<=alpha'<=r/(delta*sqrt(1-r^2))<1/delta.
    # Thus phi+/-alpha are increasing. Consecutive roots have phi-spacing
    # at least 2*acos(r)>pi/2, whereas a grid cell changes phi by at most pi/2.
    # There can therefore be at most one root in each scanned cell.
    boundaries = [mp.mpf(0)] + roots + [endpoint]
    positive = mp.mpf(0)
    negative = mp.mpf(0)
    for left, right in zip(boundaries, boundaries[1:]):
        contribution = 2 * mp.quad(lambda q: model.symbol(q) * cauchy_weight(q), [left, right])
        if model.symbol((left + right) / 2) >= 0:
            positive += contribution
        else:
            negative -= contribution
    signed_direct = 2 * mp.quad(lambda q: model.symbol(q) * cauchy_weight(q), grid)
    assert abs(positive - negative - signed_direct) < mp.mpf("1e-32")
    average = 2 / mp.pi * mp.quad(lambda q: abs(model.amplitude(q)) * cauchy_weight(q), grid)
    return positive, negative, average


def audit_identities(model, independent_quadrature=False):
    worst = mp.mpf(0)
    assert abs(model.history(0)) < mp.mpf("1e-45")
    assert abs(model.history(model.length) - model.mass) < mp.mpf("1e-45")
    assert abs(model.amplitude(0) - model.mass) < mp.mpf("1e-45")
    for q in (mp.mpf(0), model.delta / 2, model.delta, mp.mpf(1), -mp.mpf(1)):
        assembled = model.mass - 1j * q * model.backward_transform(q)
        error = max(abs(assembled - model.amplitude(q)),
                    abs(mp.re(mp.exp(1j * model.length * q) * assembled) - model.symbol(q)))
        worst = max(worst, error / abs(model.mass))
    if independent_quadrature:
        q = mp.mpf(3) / 8
        pieces = [j * model.length / 4 for j in range(5)]
        direct = model.mass * mp.cos(model.length * q) + q * mp.quad(
            lambda u: model.history(u) * mp.sin(q * u), pieces)
        lag_transform = mp.quad(lambda u: model.density(u) * mp.cos(q * u), pieces)
        worst = max(worst, abs(direct - model.symbol(q)) / abs(model.mass),
                    abs(lag_transform - model.symbol(q)) / abs(model.mass))
    assert worst < mp.mpf("1e-40")
    return worst


def audit_full_cauchy(model):
    mean, square, history_l2 = model.cauchy_closed()
    pieces = [j * model.length / 4 for j in range(5)]
    mean_lag = mp.quad(lambda u: model.density(u) * mp.exp(-u), pieces)
    a = model.density(0)
    # Exact inner triangle integral, followed by independent outer quadrature.
    triangle = mp.quad(
        lambda u: model.density(u) * (model.density(u) - a * mp.exp(-u)) / (model.delta + 1),
        pieces,
    )
    square_lag = triangle + mean_lag**2 / 2
    history_lag = mp.quad(lambda u: model.history(u)**2, pieces)
    error = max(abs(mean - mean_lag) / abs(model.mass),
                abs(square - square_lag) / model.mass**2,
                abs(history_l2 - history_lag) / model.mass**2)
    assert error < mp.mpf("1e-38")
    # The first bound is the general path/Plancherel estimate, not a fit.
    assert 0 <= square <= 2 * model.mass**2 + 2 * history_l2
    assert history_l2 <= model.mass**2 / (2 * model.delta)
    # This particular dH has a single sign, so its TV also gives this sharper bound.
    assert square <= model.mass**2
    return mean, square, error


def main():
    started = perf_counter()
    mp.mp.dps = 50
    delta = mp.mpf(1) / 8
    endpoint = mp.mpf(1)
    worst_identity = mp.mpf(0)
    worst_cauchy = mp.mpf(0)
    # |A|<=|M| and |A'|<=|M|/delta for this truncated exponential model.
    # Freeze B=w_C*A on full carrier periods. The leftover single partial
    # period gives error <= (2*pi+2)/L * (||B'||_1+||B||_infinity).
    weight_mass = 2 * mp.atan(endpoint) / mp.pi
    weight_variation = 2 * (cauchy_weight(0) - cauchy_weight(endpoint))
    carrier_constant = (2 * mp.pi + 2) * (cauchy_weight(0) + weight_variation + weight_mass / delta)
    print("[E] Synthetic BV paths only; MP50 finite checks, NOT arithmetic records or asymptotic certification.")
    print("[E] Fixed window [-1,1]; columns: L, M, negative trace, carrier average, L*absolute error/|M|.")
    for length in (16, 32, 64, 128, 256):
        positive_model = PathModel(length, delta)
        positive, negative, average = finite_negative_traces(positive_model, endpoint)
        for mass in (1, -1):
            model = PathModel(length, delta, mass)
            worst_identity = max(worst_identity, audit_identities(model, length == 16))
            mean, square, error = audit_full_cauchy(model)
            worst_cauchy = max(worst_cauchy, error)
            observed = negative if mass == 1 else positive
            scaled_error = length * abs(observed - average)
            assert scaled_error <= carrier_constant
            print(f"[E] {length:3d} {mass:+d} {float(observed):.12g} {float(average):.12g} "
                  f"{float(scaled_error):.8g}; full mean={float(mean):.8g}, full L2_squared={float(square):.10g}")
    print("[E] Analytic carrier bound on the displayed scaled error:", mp.nstr(carrier_constant, 10))
    print("[E] Max carrier/path identity error:", mp.nstr(worst_identity, 8))
    print("[E] Max full-Cauchy-kernel/lag quadrature error:", mp.nstr(worst_cauchy, 8))
    print(f"PASS; elapsed_seconds={perf_counter()-started:.3f}; no files written.")


if __name__ == "__main__":
    main()

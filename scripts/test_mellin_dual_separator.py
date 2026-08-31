"""Finite sanity checks for the Mellin-coherent FPW4b extractor.

This validates Fourier/Mellin normalizations and the finite Schur bound only.
It is not an RH test or an interval-certified proof.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 40

A0 = mp.mpf(4)
B = mp.log(A0)
CENTER = mp.mpf("0.5")
KAPPA = mp.mpf("0.5")
ORDER = 2
T = mp.mpf("1.1")
Z0 = mp.mpc("0.3", "0.7")

COEFFICIENTS = {
    2: mp.mpc("1.25", "-0.2"),
    3: mp.mpc("-0.7", "0.4"),
    5: mp.mpc("0.3", "0.1"),
}


def h(z: mp.mpc, tau: mp.mpf) -> mp.mpc:
    value = z - 1j * tau
    if abs(value) < mp.mpf("1e-35"):
        return 2 * B
    return 2 * mp.sinh(B * value) / value


def q(tau: mp.mpf) -> mp.mpc:
    return h(Z0, tau) if abs(tau) <= T else mp.mpc(0)


def feature(n: int, x_scale: mp.mpf, tau: mp.mpf) -> mp.mpc:
    if not (x_scale / A0 < n <= A0 * x_scale):
        return mp.mpc(0)
    return mp.power(n, -CENTER) * mp.exp(-1j * tau * mp.log(n / x_scale))


def ell_value(x_scale: mp.mpf) -> mp.mpc:
    def integrand(tau: mp.mpf) -> mp.mpc:
        signal = sum(
            value * feature(n, x_scale, tau)
            for n, value in COEFFICIENTS.items()
        )
        return signal * mp.conj(q(tau))

    return mp.quad(integrand, [-T, T]) / (2 * mp.pi)


def mellin_identity_check() -> None:
    z = mp.mpc("0.8", "0.35")
    breakpoints = sorted(
        {mp.mpf(n) / A0 for n in COEFFICIENTS}
        | {mp.mpf(n) * A0 for n in COEFFICIENTS}
    )
    lhs = mp.quad(lambda x: ell_value(x) * x ** (-z - 1), breakpoints)
    k_factor = mp.quad(
        lambda tau: mp.conj(q(tau)) * h(z, tau), [-T, T]
    ) / (2 * mp.pi)
    l_value = sum(
        value * mp.power(n, -(CENTER + z))
        for n, value in COEFFICIENTS.items()
    )
    rhs = k_factor * l_value
    relative = abs(lhs - rhs) / max(1, abs(rhs))
    assert relative < mp.mpf("1e-25"), relative

    positive_multiplier = mp.quad(
        lambda tau: abs(h(Z0, tau)) ** 2, [-T, T]
    ) / (2 * mp.pi)
    assert positive_multiplier > 0


def green_kernel(u: mp.mpf) -> mp.mpf:
    # (2 pi)^(-1) integral exp(i tau u)/(tau^2+1/4)^2 d tau
    return (2 + abs(u)) * mp.exp(-abs(u) / 2)


def schur_bound_check() -> None:
    scale = mp.mpf(3)
    indices = [n for n in COEFFICIENTS if scale / A0 < n <= A0 * scale]
    size = len(indices)
    gram = mp.matrix(size)
    row = mp.matrix(1, size)

    for j, n in enumerate(indices):
        row[0, j] = mp.quad(
            lambda tau: feature(n, scale, tau) * mp.conj(q(tau)), [-T, T]
        ) / (2 * mp.pi)
        for k, m in enumerate(indices):
            gram[j, k] = (
                mp.power(n * m, -CENTER)
                * green_kernel(mp.log(mp.mpf(m) / n))
            )

    column = mp.matrix([mp.conj(row[0, j]) for j in range(size)])
    exact_dual_sq = (row * (gram ** -1) * column)[0]
    analytic_bound_sq = mp.quad(
        lambda tau: abs(q(tau)) ** 2
        * (tau**2 + KAPPA**2) ** ORDER,
        [-T, T],
    ) / (2 * mp.pi)
    assert abs(mp.im(exact_dual_sq)) < mp.mpf("1e-30"), exact_dual_sq
    assert mp.re(exact_dual_sq) > 0
    assert mp.re(exact_dual_sq) <= analytic_bound_sq * (1 + mp.mpf("1e-30"))


def main() -> None:
    mellin_identity_check()
    schur_bound_check()
    print("Mellin dual-separator identity and Schur checks passed.")


if __name__ == "__main__":
    main()
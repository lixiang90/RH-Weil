"""Finite checks for the B1j Stieltjes transfer and fixed-lag diagnostics.

The identities checked here are proved analytically in Note 252.  The final
ratio table is numerical evidence illustrating the fixed-lag no-go; it is not
used as a proof of the asymptotic statement.
"""

from __future__ import annotations

import math

import mpmath as mp


SIGMA = mp.mpf(3) / 5


def von_mangoldt_table(limit: int) -> tuple[mp.mpf, ...]:
    smallest = list(range(limit + 1))
    for prime in range(2, math.isqrt(limit) + 1):
        if smallest[prime] != prime:
            continue
        for multiple in range(prime * prime, limit + 1, prime):
            if smallest[multiple] == multiple:
                smallest[multiple] = prime
    values = [mp.mpf(0)] * (limit + 1)
    for integer in range(2, limit + 1):
        prime = smallest[integer]
        remainder = integer
        while remainder % prime == 0:
            remainder //= prime
        if remainder == 1:
            values[integer] = mp.log(prime)
    return tuple(values)


def kernel(x: mp.mpf, scale: mp.mpf, phase: mp.mpf, m: int) -> mp.mpf:
    return (
        x ** (-SIGMA)
        * mp.exp(-x / scale)
        * (1 - mp.cos(phase * mp.log(x) / m))
    )


def kernel_derivative(
    x: mp.mpf, scale: mp.mpf, phase: mp.mpf, m: int
) -> mp.mpf:
    angle = phase * mp.log(x) / m
    base = x ** (-SIGMA) * mp.exp(-x / scale)
    return base * (
        phase * mp.sin(angle) / (m * x)
        - (SIGMA / x + 1 / scale) * (1 - mp.cos(angle))
    )


def prime_symbol(
    scale: int,
    cutoff: int,
    phase: mp.mpf,
    m: int,
    mangoldt: tuple[mp.mpf, ...],
) -> mp.mpf:
    return mp.fsum(
        mangoldt[integer]
        * kernel(mp.mpf(integer), mp.mpf(scale), phase, m)
        for integer in range(2, cutoff + 1)
    )


def continuum_symbol(
    scale: int, lag_end: mp.mpf, phase: mp.mpf, m: int
) -> mp.mpf:
    return mp.quad(
        lambda lag: mp.exp(
            (1 - SIGMA) * lag - mp.exp(lag) / scale
        )
        * (1 - mp.cos(phase * lag / m)),
        [0, lag_end],
    )


def stieltjes_remainder(
    scale: int,
    cutoff: int,
    phase: mp.mpf,
    m: int,
    mangoldt: tuple[mp.mpf, ...],
) -> mp.mpf:
    psi = mp.mpf(0)
    integral = mp.mpf(0)
    for integer in range(1, cutoff):
        psi += mangoldt[integer]
        integral += mp.quad(
            lambda x, psi=psi: (psi - x)
            * kernel_derivative(x, mp.mpf(scale), phase, m),
            [integer, integer + 1],
        )
    psi += mangoldt[cutoff]
    endpoint = kernel(mp.mpf(cutoff), mp.mpf(scale), phase, m) * (
        psi - cutoff
    )
    return endpoint - integral


def main() -> None:
    mp.mp.dps = 60
    scale = 16
    cutoff = 15
    m = 4
    phase = mp.mpf("1.375")
    mangoldt = von_mangoldt_table(4096)
    prime = prime_symbol(scale, cutoff, phase, m, mangoldt)
    main_integral = mp.quad(
        lambda x: kernel(x, mp.mpf(scale), phase, m),
        [1, cutoff],
    )
    remainder = stieltjes_remainder(
        scale, cutoff, phase, m, mangoldt
    )
    stieltjes_error = abs(prime - main_integral - remainder)

    lag_end = mp.log(cutoff)
    lag_integral = continuum_symbol(scale, lag_end, phase, m)
    substitution_error = abs(lag_integral - main_integral)
    if stieltjes_error > mp.mpf("1e-48"):
        raise AssertionError("finite Stieltjes identity lost precision")
    if substitution_error > mp.mpf("1e-48"):
        raise AssertionError("x=exp(lambda) substitution lost precision")

    print("stieltjes_identity_error=" + mp.nstr(stieltjes_error, 8))
    print("lag_substitution_error=" + mp.nstr(substitution_error, 8))
    print("fixed_lag_ratio_table:")
    resonant = 2 * mp.pi / mp.log(2)
    previous_generic = mp.mpf(0)
    previous_resonant = mp.mpf(0)
    for exponent in (4, 6, 8, 10, 12):
        current_scale = 2**exponent
        generic_prime = prime_symbol(
            current_scale, current_scale, mp.mpf(1), exponent, mangoldt
        )
        generic_continuum = continuum_symbol(
            current_scale, mp.mpf(2), mp.mpf(1), exponent
        )
        resonant_prime = prime_symbol(
            current_scale, current_scale, resonant, exponent, mangoldt
        )
        resonant_continuum = continuum_symbol(
            current_scale, mp.mpf(2), resonant, exponent
        )
        generic_ratio = generic_prime / generic_continuum
        resonant_ratio = resonant_prime / resonant_continuum
        if generic_ratio <= previous_generic or resonant_ratio <= previous_resonant:
            raise AssertionError("diagnostic fixed-lag ratios were not increasing")
        previous_generic = generic_ratio
        previous_resonant = resonant_ratio
        print(
            f"m={exponent},Y={current_scale},"
            f" ratio(t=1)={mp.nstr(generic_ratio, 12)},"
            f" ratio(t=2pi/log2)={mp.nstr(resonant_ratio, 12)}"
        )
    print("B1j Stieltjes/substitution finite checks passed")
    print("[scope] identities exact; ratio table is [E], not an asymptotic proof")


if __name__ == "__main__":
    main()

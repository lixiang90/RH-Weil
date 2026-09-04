"""Finite regression for Note 254's degree-two multiplier normal form.

The polynomial identities and asymptotic extinction are proved analytically in
Note 254.  The scale table below is finite evidence only and makes no RH claim.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))

mp.mp.dps = 60

from b1j_stieltjes_fixed_lag_audit import (  # noqa: E402
    SIGMA,
    continuum_symbol,
    prime_symbol,
    von_mangoldt_table,
)


KAPPA = mp.sqrt(3) / 2
ALPHA = KAPPA / (KAPPA + mp.mpf(1) / 3)
RESPONSE_CONSTANT = 4 * ALPHA**2 / 9
EPSILON_0 = mp.mpf(1) / 1000
LAMBDA_MINUS = (4 - mp.sqrt(13)) / 2
LAMBDA_PLUS = (4 + mp.sqrt(13)) / 2
REMAINDER_CONSTANT = 2 * (30 * KAPPA * EPSILON_0 + 31 * EPSILON_0**2)
C_MINUS = KAPPA**2 * LAMBDA_MINUS - REMAINDER_CONSTANT
C_PLUS = KAPPA**2 * LAMBDA_PLUS + REMAINDER_CONSTANT


def normalized_q(mu: mp.mpf, delta: mp.mpf) -> mp.mpf:
    """Evaluate the expanded discrepancy normal form from Note 254-(10)."""
    return (
        KAPPA**2 * (delta**2 - 3 * mu * delta + 3 * mu**2)
        + 2
        * KAPPA
        * (delta**3 - 4 * mu * delta**2 + 6 * mu**2 * delta - 4 * mu**3)
        + (
            delta**4
            - 5 * mu * delta**3
            + 10 * mu**2 * delta**2
            - 10 * mu**3 * delta
            + 5 * mu**4
        )
    )


def normalized_q_unexpanded(mu: mp.mpf, delta: mp.mpf) -> mp.mpf:
    x = mu - delta
    return (
        x**4
        + (mu - 2 * KAPPA) * x**3
        + (mu - KAPPA) ** 2 * x**2
        + mu * (mu - KAPPA) ** 2 * x
        + mu**2 * (mu - KAPPA) ** 2
    )


def prime_mass(
    scale: int, cutoff: int, mangoldt: tuple[mp.mpf, ...]
) -> mp.mpf:
    return mp.fsum(
        mangoldt[integer]
        * mp.mpf(integer) ** (-SIGMA)
        * mp.exp(-mp.mpf(integer) / scale)
        for integer in range(2, cutoff + 1)
    )


def continuum_mass(scale: int, cutoff: int) -> mp.mpf:
    return mp.quad(
        lambda x: x ** (-SIGMA) * mp.exp(-x / scale),
        [1, cutoff],
    )


def main() -> None:
    if C_MINUS <= mp.mpf("0.09589") or C_PLUS >= mp.mpf("2.905"):
        raise AssertionError("explicit local quadratic constants changed")

    grid = (
        -EPSILON_0,
        -EPSILON_0 / 2,
        mp.mpf(0),
        EPSILON_0 / 2,
        EPSILON_0,
    )
    for mu in grid:
        for delta in grid:
            if abs(mu) + abs(delta) > EPSILON_0:
                continue
            expanded = normalized_q(mu, delta)
            unexpanded = normalized_q_unexpanded(mu, delta)
            if abs(expanded - unexpanded) > mp.mpf("1e-55"):
                raise AssertionError("normalized polynomial expansion failed")
            norm_squared = mu**2 + delta**2
            if not (
                C_MINUS * norm_squared - mp.mpf("1e-55")
                <= expanded
                <= C_PLUS * norm_squared + mp.mpf("1e-55")
            ):
                raise AssertionError("local quadratic two-sided bound failed")

    mangoldt = von_mangoldt_table(4096)
    previous_multiplier = mp.inf
    print("local_c_minus=" + mp.nstr(C_MINUS, 15))
    print("local_c_plus=" + mp.nstr(C_PLUS, 15))
    print("response_constant=" + mp.nstr(RESPONSE_CONSTANT, 15))
    print("matched_multiplier_table:")
    for exponent in (4, 6, 8, 10, 12):
        scale = 2**exponent
        cutoff = scale
        source_prime = prime_mass(scale, cutoff, mangoldt)
        source_continuum = continuum_mass(scale, cutoff)
        source_norm = source_prime + source_continuum
        total_mass = source_prime - source_continuum
        wp = prime_symbol(
            scale, cutoff, mp.mpf(1), exponent, mangoldt
        )
        wc = continuum_symbol(
            scale, mp.log(cutoff), mp.mpf(1), exponent
        )
        mu = total_mass / source_norm
        delta = (wp - wc) / source_norm
        q_value = normalized_q(mu, delta)
        wp_physical = prime_symbol(
            scale, cutoff, mp.mpf(exponent), exponent, mangoldt
        )
        wc_physical = continuum_symbol(
            scale, mp.log(cutoff), mp.mpf(exponent), exponent
        )
        delta_physical = (wp_physical - wc_physical) / source_norm
        multiplier_physical = RESPONSE_CONSTANT * abs(
            normalized_q(mu, delta_physical)
        )

        level = KAPPA * source_norm
        dhat = total_mass - wp + wc
        unnormalized_q = (
            dhat**4
            + (total_mass - 2 * level) * dhat**3
            + (total_mass - level) ** 2 * dhat**2
            + total_mass * (total_mass - level) ** 2 * dhat
            + total_mass**2 * (total_mass - level) ** 2
        )
        multiplier = RESPONSE_CONSTANT * abs(q_value)
        reconstructed = (
            RESPONSE_CONSTANT * abs(unnormalized_q) / source_norm**4
        )
        if abs(multiplier - reconstructed) > mp.mpf("1e-50"):
            raise AssertionError("homogeneous multiplier reconstruction failed")
        if multiplier >= previous_multiplier:
            raise AssertionError("finite diagnostic multiplier did not decrease")
        previous_multiplier = multiplier
        print(
            f"m={exponent},Y={scale},"
            f" mu={mp.nstr(mu, 10)},"
            f" delta(t=1)={mp.nstr(delta, 10)},"
            f" |gamma*Q|(t=1)={mp.nstr(multiplier, 12)},"
            f" delta(xi=1)={mp.nstr(delta_physical, 10)},"
            f" |gamma*Q|(xi=1)={mp.nstr(multiplier_physical, 12)}"
        )

    print("B1l multiplier normal-form checks passed")
    print("[scope] algebra regression plus finite [E] table; total energy capture remains open")


if __name__ == "__main__":
    main()

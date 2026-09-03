"""Finite Schur audit of the actual Vaughan--Brownian physical direction.

The three response channels are Type I, Type II, and continuum.  This script
does not optimize an arbitrary vector: it keeps the physical prime vector
e=(1,1) and the actual continuum coefficient 1, and verifies the exact
continuum Schur completion of their Brownian primitive Gram.
"""

from __future__ import annotations

import math
import numpy as np

from audit_soft_zeta_orbit import soft_zeta_orbit_audit
from qw_matrix import canonical_vaughan_two_channel_coefficients


def audit_schur(scale: float, integer_cutoff: int) -> None:
    square_root_cutoff = math.isqrt(integer_cutoff)
    vacuous = canonical_vaughan_two_channel_coefficients(
        integer_cutoff, square_root_cutoff, square_root_cutoff
    )
    if vacuous["type_ii_support_lower_bound"] <= integer_cutoff:
        raise AssertionError("square-root Type-II support should be empty")
    if max(
        abs(value) for value in vacuous["components"]["type_ii"]
    ) > 1.0e-14:
        raise AssertionError("square-root Type-II coefficients are not zero")
    audit = soft_zeta_orbit_audit(
        scale=scale,
        integer_cutoff=integer_cutoff,
        lag_cells=2,
        degree=2,
    )
    channel = audit["vaughan_brownian_audit"]
    if channel is None:
        raise AssertionError("degree-two Vaughan channel audit is missing")
    data = channel["channel_gram"]
    labels = tuple(data["labels"])
    expected = ("type_i", "type_ii", "continuum")
    if labels != expected:
        raise AssertionError(f"unexpected channel order: {labels}")
    gram = np.asarray(data["gram"], dtype=complex)
    gram = 0.5 * (gram + np.conjugate(gram.T))
    prime_block = gram[:2, :2]
    continuum_cross = gram[:2, 2]
    continuum_energy = float(gram[2, 2].real)
    if continuum_energy <= 0.0:
        raise AssertionError("continuum Brownian energy is not positive")

    physical_prime = np.ones(2, dtype=complex)
    prime_energy = float(
        np.real(np.conjugate(physical_prime) @ prime_block @ physical_prime)
    )
    prime_diagonal = float(np.trace(prime_block).real)
    type_i_energy = float(prime_block[0, 0].real)
    type_ii_energy = float(prime_block[1, 1].real)
    if type_ii_energy <= 1.0e-14:
        raise AssertionError("Type-II response is vacuous at this cutoff")
    prime_cross = prime_energy - prime_diagonal
    type_i_ii_coherence = float(
        np.real(prime_block[0, 1])
        / math.sqrt(type_i_energy * type_ii_energy)
    )
    if abs(type_i_ii_coherence) > 1.0 + 1.0e-10:
        raise AssertionError("Type-I/II coherence violates Cauchy--Schwarz")
    continuum_linear = np.vdot(continuum_cross, physical_prime)
    prime_continuum_cross = 2.0 * float(continuum_linear.real)
    prime_continuum_coherence = float(
        continuum_linear.real / math.sqrt(prime_energy * continuum_energy)
    )
    prime_continuum_balance = (
        2.0
        * math.sqrt(prime_energy * continuum_energy)
        / (prime_energy + continuum_energy)
    )
    if abs(prime_continuum_coherence) > 1.0 + 1.0e-10:
        raise AssertionError("prime/continuum coherence violates Cauchy--Schwarz")
    if not 0.0 <= prime_continuum_balance <= 1.0 + 1.0e-10:
        raise AssertionError("prime/continuum balance is outside [0,1]")
    direct_total = prime_energy + prime_continuum_cross + continuum_energy

    schur_block = prime_block - np.outer(
        continuum_cross, np.conjugate(continuum_cross)
    ) / continuum_energy
    schur_block = 0.5 * (schur_block + np.conjugate(schur_block.T))
    shorted_residual = float(
        np.real(np.conjugate(physical_prime) @ schur_block @ physical_prime)
    )
    optimal_continuum_coefficient = -continuum_linear / continuum_energy
    mismatch = continuum_energy * abs(
        1.0 - optimal_continuum_coefficient
    ) ** 2
    reconstructed_total = shorted_residual + mismatch

    tolerance = 1.0e-10 * max(1.0, abs(direct_total))
    if abs(direct_total - data["total_energy"]) > tolerance:
        raise AssertionError("three-channel physical energy mismatch")
    if abs(reconstructed_total - direct_total) > tolerance:
        raise AssertionError("continuum Schur completion failed")
    if shorted_residual < -tolerance or mismatch < -tolerance:
        raise AssertionError("Schur defects are not nonnegative")
    if np.linalg.eigvalsh(schur_block).min() < -1.0e-10:
        raise AssertionError("continuum-shorted prime block is not PSD")

    full_diagonal = prime_diagonal + continuum_energy
    print(
        f"scale={scale:>4.0f}, cutoff={integer_cutoff:>2d}: "
        f"U=V={channel['mobius_cutoff']}, "
        f"II-start={channel['type_ii_support_lower_bound']}, "
        f"E={direct_total:.7e}, diag/E={full_diagonal/direct_total:.3f}, "
        f"II/prime-diag={type_ii_energy/prime_diagonal:.3f}, "
        f"prime-cross/prime-diag={prime_cross/prime_diagonal:+.3f}, "
        f"rho_I,II={type_i_ii_coherence:+.3f}, "
        f"pcross/(P+C)={prime_continuum_cross/(prime_energy+continuum_energy):+.3f}, "
        f"rho_p,c={prime_continuum_coherence:+.3f}, "
        f"balance_p,c={prime_continuum_balance:.3f}, "
        f"short/E={shorted_residual/direct_total:.3f}, "
        f"mismatch/E={mismatch/direct_total:.3f}, "
        f"alpha_opt={optimal_continuum_coefficient.real:+.3f}"
        f"{optimal_continuum_coefficient.imag:+.3f}i"
    )


def main() -> None:
    for scale, integer_cutoff in (
        (4.0, 7),
        (8.0, 10),
        (12.0, 12),
        (16.0, 15),
    ):
        audit_schur(scale, integer_cutoff)
    print("Vaughan--Brownian physical Schur audits passed")
    print("[scope] exact finite identity/evidence only; no RH asymptotic")


if __name__ == "__main__":
    main()

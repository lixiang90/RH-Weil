"""Finite frequency-domain audit of Vaughan prime/continuum ratio capture."""

from __future__ import annotations

import numpy as np

from audit_soft_zeta_orbit import soft_zeta_orbit_audit
from formal_lag_response import symmetric_spectral_ratio_capture_quadrature


RATIO_BANDS = ((0.25, 4.0), (0.5, 2.0), (0.75, 4.0 / 3.0))


def audit_capture(scale: float, integer_cutoff: int, lag_cells: int) -> None:
    audit = soft_zeta_orbit_audit(
        scale=scale,
        integer_cutoff=integer_cutoff,
        lag_cells=lag_cells,
        degree=2,
    )
    channel = audit["vaughan_brownian_audit"]
    if channel is None:
        raise AssertionError("Vaughan Brownian channel data are missing")
    spectral = channel["spectral_overlap_data"]
    quadrature = symmetric_spectral_ratio_capture_quadrature(
        **spectral,
        ratio_bands=RATIO_BANDS,
        frequency_cutoff=256.0,
        frequency_step=0.01,
    )
    gram = np.asarray(channel["channel_gram"]["gram"], dtype=complex)
    physical_prime = np.ones(2, dtype=complex)
    exact_prime = float(
        np.real(np.conjugate(physical_prime) @ gram[:2, :2] @ physical_prime)
    )
    exact_continuum = float(gram[2, 2].real)
    exact_cross = float(np.real(np.sum(gram[:2, 2])))
    exact_diagonal = exact_prime + exact_continuum
    spectral_diagonal = float(quadrature["diagonal_energy"])
    coverage = spectral_diagonal / exact_diagonal
    cross_coverage = float(quadrature["cross"]) / exact_cross

    if quadrature["minimum_prime_symbol"] < -1.0e-9:
        raise AssertionError("centered prime Fourier symbol lost its sign")
    if quadrature["minimum_continuum_symbol"] < -1.0e-9:
        raise AssertionError("centered continuum Fourier symbol lost its sign")
    if quadrature["maximum_prime_imaginary"] > 1.0e-9:
        raise AssertionError("prime Fourier symbol is not even-real")
    if quadrature["maximum_continuum_imaginary"] > 1.0e-9:
        raise AssertionError("continuum Fourier symbol is not even-real")
    if not 0.95 <= coverage <= 1.01:
        raise AssertionError("frequency cutoff does not capture the Brownian diagonal")
    if not 0.90 <= cross_coverage <= 1.05:
        raise AssertionError("frequency cutoff does not capture the Brownian cross")

    captures = quadrature["band_capture_fractions"]
    exact_captures = tuple(
        energy / exact_diagonal for energy in quadrature["band_energies"]
    )
    print(
        f"scale={scale:>4.0f}, cutoff={integer_cutoff:>2d}, cells={lag_cells:>2d}: "
        f"spectral/exact={coverage:.5f}, cross-coverage={cross_coverage:.5f}, "
        f"capture[1/4,4]/exact={exact_captures[0]:.5f}, "
        f"capture[1/2,2]/exact={exact_captures[1]:.5f}, "
        f"capture[3/4,4/3]/exact={exact_captures[2]:.5f}, "
        f"truncated-wide={captures[0]:.5f}, "
        f"crude-tail/exact="
        f"{quadrature['absolute_diagonal_tail_bound']/exact_diagonal:.3e}",
        flush=True,
    )


def main() -> None:
    for scale, integer_cutoff, lag_cells in (
        (8.0, 10, 4),
        (16.0, 15, 4),
    ):
        audit_capture(scale, integer_cutoff, lag_cells)
    print("Vaughan spectral ratio-capture audits passed")
    print("[scope] finite quadrature evidence only; no uniform asymptotic")


if __name__ == "__main__":
    main()

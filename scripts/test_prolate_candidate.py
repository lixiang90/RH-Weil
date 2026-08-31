"""Sanity checks for the Legendre prolate candidate implementation."""

from __future__ import annotations

import math
import mpmath as mp

from prolate_candidate import (
    build_candidate,
    build_near_radical_trial_family,
    candidate_diagnostics,
    corrected_fourier_coefficients,
    high_precision_diagnostics,
)


def main() -> None:
    mp.mp.dps = 60
    candidate = build_candidate(math.sqrt(13), basis_size=70)
    diagnostics = candidate_diagnostics(candidate, grid_size=401)

    # The constructed linear combination has zero Legendre integral up to
    # the backward error of the floating-point eigensolve.
    assert abs(math.sqrt(2) * candidate.coefficients[0]) < 1e-14
    assert diagnostics["corrected_endpoint_max"] < 1e-13
    assert diagnostics["corrected_inversion_max"] < 1e-13
    assert diagnostics["relative_odd_norm"] < 1
    assert diagnostics["relative_correction_norm"] < 1

    # Low spectral data should be stable when the Legendre cutoff is raised.
    refined = build_candidate(math.sqrt(13), basis_size=90)
    for coarse, fine in zip(candidate.eigenvalues, refined.eigenvalues):
        assert abs(coarse - fine) <= 1e-9 * max(1, abs(fine))

    family = build_near_radical_trial_family(
        math.sqrt(13), dimension=3, basis_size=70
    )
    assert len(family) == 3
    for item in family:
        assert abs(math.sqrt(2) * item.coefficients[0]) < 1e-14
        # The positive-Fourier branch makes h(0) an exponentially small
        # dependent defect; it is deliberately not hard-constrained.
        assert abs(float(item.psi(0.0))) < 1e-10

    coefficients, metadata = corrected_fourier_coefficients(
        candidate, cutoff=6, quadrature_order=32
    )
    assert abs(mp.fsum(coefficients.values())) < mp.mpf("1e-45")
    assert abs(
        mp.fsum(abs(value) ** 2 for value in coefficients.values()) - 1
    ) < mp.mpf("1e-45")
    for n in range(1, 7):
        assert coefficients[n] == coefficients[-n]
    assert metadata["boundary_correction_distance"] >= 0

    high_precision = high_precision_diagnostics(
        mp.sqrt(13), basis_size=40, dps=60
    )
    assert abs(high_precision["integral_residual"]) < mp.mpf("1e-55")
    assert abs(high_precision["boundary_average"]) < mp.mpf("1e-10")

    print("Prolate boundary-correction sanity checks passed.")


if __name__ == "__main__":
    main()

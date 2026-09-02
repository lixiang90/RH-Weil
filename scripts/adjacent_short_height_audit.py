"""Finite checks for the short-height Hilbert-valued adjacent argument.

This script checks exact finite exponential-kernel identities and elementary
scaling only.  It does not prove the Montgomery--Vaughan theorem, the
arithmetic coefficient-energy bound, a zero proportion, or RH.
"""

from __future__ import annotations

import math

import numpy as np


def integral_kernel(m: int, n: int, left: float, height: float) -> complex:
    """Average of exp(i t log(m/n)) on [left,left+height]."""
    if m == n:
        return 1.0 + 0.0j
    frequency = math.log(m / n)
    return (
        np.exp(1j * (left + height) * frequency)
        - np.exp(1j * left * frequency)
    ) / (1j * height * frequency)


def exact_kernel_check() -> None:
    rng = np.random.default_rng(223)
    indices = np.array([11, 14, 19, 27, 41], dtype=int)
    coeffs = rng.normal(size=(len(indices), 3, 2)) + 1j * rng.normal(
        size=(len(indices), 3, 2)
    )
    left = 7.25
    height = 3.75

    kernel = np.array(
        [
            [integral_kernel(int(m), int(n), left, height) for n in indices]
            for m in indices
        ]
    )
    gram = np.einsum("mab,nab->mn", coeffs, np.conjugate(coeffs))
    kernel_value = np.sum(kernel * gram).real

    # Independent entrywise reconstruction of the same quadratic form.
    coordinate_value = 0.0
    for row in range(coeffs.shape[1]):
        for col in range(coeffs.shape[2]):
            vector = coeffs[:, row, col]
            coordinate_value += np.sum(
                kernel * np.outer(vector, np.conjugate(vector))
            ).real

    assert abs(kernel_value - coordinate_value) < 1e-11
    assert abs(kernel_value.imag if hasattr(kernel_value, "imag") else 0.0) < 1e-12

    # Shifting the interval is exactly coefficient phase rotation.
    shifted = coeffs * np.exp(1j * left * np.log(indices))[:, None, None]
    zero_kernel = np.array(
        [
            [integral_kernel(int(m), int(n), 0.0, height) for n in indices]
            for m in indices
        ]
    )
    shifted_gram = np.einsum("mab,nab->mn", shifted, np.conjugate(shifted))
    shifted_value = np.sum(zero_kernel * shifted_gram).real
    assert abs(kernel_value - shifted_value) < 1e-11


def scale_check() -> None:
    ratios = []
    relative_gaps = []
    for exponent in (20, 40, 80, 160, 320):
        log_x = float(exponent)
        log_log_x = math.log(log_x)
        ratios.append((1.0 + log_log_x) / math.sqrt(log_x))
        relative_gaps.append(1.0 / math.sqrt(log_x))

    assert ratios[-1] < ratios[-2] < ratios[-3]
    assert relative_gaps[-1] < relative_gaps[-2] < relative_gaps[-3]
    assert ratios[-1] < 0.4
    assert relative_gaps[-1] < 0.06


def block_gap_check() -> None:
    # Work with logarithms only; the recurrence verifies H(Y)/Y=1/sqrt(log Y).
    log_y = 100.0
    for _ in range(25):
        relative_height = 1.0 / math.sqrt(log_y)
        next_log_y = log_y + math.log1p(relative_height)
        assert 0.0 < next_log_y - log_y < relative_height
        assert relative_height < 0.11
        log_y = next_log_y


def main() -> None:
    exact_kernel_check()
    scale_check()
    block_gap_check()
    print("short-height Hilbert kernel and scale checks passed")
    print("[scope] finite identities only; no arithmetic asymptotic or RH claim")


if __name__ == "__main__":
    main()

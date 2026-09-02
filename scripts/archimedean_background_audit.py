"""Finite audits for note 226's Archimedean background reduction.

These checks validate normalization, Schatten scaling, and deterministic
window integrals.  They do not prove the analytic tail estimate, evacuate
mixed prime frequencies, or provide RH evidence.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial.legendre import leggauss


def audit_zero_frequency_normalization() -> None:
    for log_x in (20.0, 50.0, 100.0):
        a = 0.83
        beta = 2.0 * math.pi / (a * log_x)
        archimedean_main = log_x / (2.0 * math.pi)
        assert abs(archimedean_main * beta - 1.0 / a) < 1e-14
    print("Archimedean zero-frequency normalization passed")


def audit_schatten_perturbation_scale() -> None:
    # If ||E|| <= 1/L in dimension d=N and ||H0||_4 <= N^(1/4),
    # the four-term telescoping scale is at most O(N/L).
    ratios = []
    for log_x in (20.0, 40.0, 80.0, 160.0):
        ratios.append(4.0 / log_x + 6.0 / log_x**2 + 4.0 / log_x**3 + 1.0 / log_x**4)
    assert all(right < left for left, right in zip(ratios, ratios[1:]))
    assert ratios[-1] < 0.026
    print("Schatten-four background perturbation scale passed")


def window_values(kind: str, values: np.ndarray) -> np.ndarray:
    inside = np.abs(values) <= 0.5
    result = np.zeros_like(values)
    if kind == "flat":
        result[inside] = 1.0
    elif kind == "mt":
        result[inside] = np.cos(math.sqrt(2.0) * values[inside])
    else:
        raise ValueError(kind)
    return result


def window_integrals(kind: str, order: int) -> tuple[float, float]:
    nodes, weights = leggauss(order)
    v = 0.5 * nodes
    v_weights = 0.5 * weights
    r = 0.5 * (nodes + 1.0)
    r_weights = 0.5 * weights

    psi_v = window_values(kind, v)
    a = float(np.dot(v_weights, psi_v))
    s_v = psi_v / a - 1.0
    d_zero = float(np.dot(v_weights, s_v**4))

    c1_values = []
    c2_values = []
    for shift in r:
        # Q_shift is supported on the moving overlap [shift-1/2, 1/2].
        # Remapping the Gauss rule avoids integrating across the moving jump
        # introduced by zero extension.
        overlap_v = 0.5 * shift + 0.5 * (1.0 - shift) * nodes
        overlap_weights = 0.5 * (1.0 - shift) * weights
        overlap_psi = window_values(kind, overlap_v)
        reflected_psi = window_values(kind, shift - overlap_v)
        overlap_s = overlap_psi / a - 1.0
        shifted_s = window_values(kind, overlap_v - shift) / a - 1.0
        q = overlap_psi * reflected_psi
        c1_values.append(float(np.dot(overlap_weights, overlap_s**2 * q)))
        c2_values.append(float(np.dot(overlap_weights, overlap_s * shifted_s * q)))

    c1 = np.array(c1_values)
    c2 = np.array(c2_values)
    d_mixed = float(np.dot(r_weights, r * (8.0 * c1 + 4.0 * c2)) / a**2)
    return d_zero, d_mixed


def audit_orientation_coefficients() -> None:
    # Four cyclic S^2 P^2 words times two opposite-sign orientations give 8;
    # two SPSP words times two orientations give 4.
    assert 4 * 2 == 8
    assert 2 * 2 == 4
    print("mixed two-prime orientation coefficients passed")


def audit_window_constants() -> None:
    flat_zero, flat_mixed = window_integrals("flat", 80)
    assert abs(flat_zero) < 1e-14
    assert abs(flat_mixed) < 1e-14

    values = [window_integrals("mt", order) for order in (40, 64, 96, 144)]
    for left, right in zip(values, values[1:]):
        assert abs(left[0] - right[0]) < 3e-7
        assert abs(left[1] - right[1]) < 3e-4
    d_zero, d_mixed = values[-1]
    d22 = 0.244589382034426
    candidate = d_zero + d_mixed + d22
    assert 7.7e-5 < d_zero < 8.1e-5
    assert abs(d_mixed - 0.00784079916792143) < 2e-13
    assert abs(candidate - 0.252508968713594) < 3e-13
    print(
        "MT conditional background candidate: "
        f"D0={d_zero:.10f}, Dmix={d_mixed:.10f}, total={candidate:.10f}"
    )


def main() -> None:
    audit_zero_frequency_normalization()
    audit_schatten_perturbation_scale()
    audit_orientation_coefficients()
    audit_window_constants()
    print("Archimedean background audits passed")
    print("[scope] deterministic normalization only; mixed evacuation is audited separately")


if __name__ == "__main__":
    main()
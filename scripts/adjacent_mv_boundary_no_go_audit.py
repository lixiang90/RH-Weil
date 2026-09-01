"""Audits for the adjacent Montgomery--Vaughan/boundary split.

The script checks finite identities and a sharp abstract obstruction.  It does
not certify any zeta asymptotic; those are proved analytically in note 205.
"""

from __future__ import annotations

import math

import numpy as np


def toeplitz_from_hat(hat: dict[int, complex], d: int) -> np.ndarray:
    return np.array(
        [[hat.get(j - k, 0.0) for k in range(d)] for j in range(d)],
        dtype=complex,
    )


def modulation(x: float, h: float, d: int) -> np.ndarray:
    return np.diag(np.exp(1j * h * x * np.arange(d)))


def audit_diagonal_fibre_identity() -> None:
    rng = np.random.default_rng(205)
    d = 13
    length = 9.0
    h = 2.0 * math.pi / length
    beta = 0.37
    base = 17.0
    products = [6, 10, 14, 15, 21]
    hats: dict[int, dict[int, complex]] = {}
    matrices: list[np.ndarray] = []

    for m in products:
        hat = {
            r: (rng.normal() + 1j * rng.normal()) / (1.0 + r * r)
            for r in range(-5, 6)
        }
        hats[m] = hat
        x = math.log(m)
        matrix = (
            beta**2
            * np.exp(1j * base * x)
            * toeplitz_from_hat(hat, d)
            @ modulation(x, h, d)
        )
        matrices.append(matrix)

    direct = np.linalg.norm(sum(matrices), "fro") ** 2
    fibres = 0.0
    for r in range(-(d - 1), d):
        indices = range(max(0, -r), min(d, d - r))
        for k in indices:
            amplitude = sum(
                beta**2
                * hats[m].get(r, 0.0)
                * np.exp(1j * (base + k * h) * math.log(m))
                for m in products
            )
            fibres += abs(amplitude) ** 2

    np.testing.assert_allclose(direct, fibres, rtol=2e-12, atol=2e-12)
    print("exact Toeplitz diagonal-fibre identity passed")


def circular_spacing(values: list[float]) -> float:
    ordered = sorted(value % 1.0 for value in values)
    gaps = [ordered[j + 1] - ordered[j] for j in range(len(ordered) - 1)]
    gaps.append(1.0 + ordered[0] - ordered[-1])
    return min(gaps)


def audit_log_product_spacing() -> None:
    for x_cap in (200, 2_000, 20_000):
        length = math.log(x_cap)
        products = list(range(4, x_cap + 1))
        spacing = circular_spacing([math.log(m) / length for m in products])
        scaled = spacing * length * x_cap
        assert scaled > 0.45
        print(
            f"X={x_cap:6d}: circular spacing={spacing:.6e}, "
            f"L*X*spacing={scaled:.6f}"
        )
    print("log-product circular spacing scale 1/(L X) passed")


def hankel_defect(
    f_hat: dict[int, complex], g_hat: dict[int, complex], d: int
) -> np.ndarray:
    result = np.zeros((d, d), dtype=complex)
    # The chosen monomials only require the two nearest exterior indices.
    exterior = (-1, d)
    for j in range(d):
        for k in range(d):
            result[j, k] = sum(
                f_hat.get(j - ell, 0.0) * g_hat.get(ell - k, 0.0)
                for ell in exterior
            )
    return result


def audit_sharp_boundary_no_go() -> None:
    d = 11
    length = 12.0
    h = 2.0 * math.pi / length
    # f(u)=exp(-ihu), g(u)=exp(ihu) in the note's Fourier convention.
    defect = hankel_defect({1: 1.0}, {-1: 1.0}, d)
    expected = np.zeros((d, d), dtype=complex)
    expected[0, 0] = 1.0
    np.testing.assert_allclose(defect, expected, atol=0.0)

    count = 41
    budget = 3.25
    base = 23.0
    frequencies = [2.0 * math.pi * j / base for j in range(1, count + 1)]
    pieces = [
        math.sqrt(budget / count)
        * np.exp(1j * base * x)
        * defect
        @ modulation(x, h, d)
        for x in frequencies
    ]
    direct_sum = sum(np.linalg.norm(piece, "fro") ** 2 for piece in pieces)
    coherent = np.linalg.norm(sum(pieces), "fro") ** 2
    np.testing.assert_allclose(direct_sum, budget, rtol=2e-13, atol=2e-13)
    np.testing.assert_allclose(coherent, count * budget, rtol=2e-13, atol=2e-13)
    print(
        "rank-one Toeplitz--Hankel obstruction passed: "
        f"direct={direct_sum:.6f}, aggregate={coherent:.6f}, ratio={count}"
    )


def main() -> None:
    audit_diagonal_fibre_identity()
    audit_log_product_spacing()
    audit_sharp_boundary_no_go()
    print("Adjacent MV/boundary no-go audits passed.")


if __name__ == "__main__":
    main()

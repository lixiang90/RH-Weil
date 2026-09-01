"""Finite audits for the quadratic-channel fourth-moment route.

The matrix identities are exact.  The Dirichlet-polynomial experiment is an
unweighted finite prototype of the new arithmetic channel; it is not an
estimate for the tapered zeta compression.
"""

from __future__ import annotations

import math
from collections import defaultdict
from math import comb

import numpy as np


TOL = 2.0e-9


def hermitian_random(rng: np.random.Generator, dimension: int) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    return 0.5 * (raw + np.conjugate(raw.T))


def quadratic_channel_gram(
    background: np.ndarray, prime: np.ndarray
) -> dict[str, object]:
    """Factor tr(background+prime)^4 through three HS channels."""
    channels = (
        background @ background,
        background @ prime + prime @ background,
        prime @ prime,
    )
    gram = np.array(
        [[np.vdot(left, right) for right in channels] for left in channels],
        dtype=complex,
    )
    direct = float(
        np.real(np.trace(np.linalg.matrix_power(background + prime, 4)))
    )
    total = float(np.real(np.ones(3) @ gram @ np.ones(3)))

    lower = gram[:2, :2]
    coupling = gram[:2, 2]
    coefficients = np.linalg.pinv(lower) @ coupling
    projected_quadratic = sum(
        coefficient * channel
        for coefficient, channel in zip(coefficients, channels[:2])
    )
    orthogonal_quadratic = channels[2] - projected_quadratic
    residual = float(
        np.real(
            gram[2, 2]
            - np.conjugate(coupling) @ np.linalg.pinv(lower) @ coupling
        )
    )
    residual_direct = float(np.real(np.vdot(orthogonal_quadratic, orthogonal_quadratic)))
    shorted_total = float(
        np.real(
            np.vdot(
                channels[0] + channels[1] + projected_quadratic,
                channels[0] + channels[1] + projected_quadratic,
            )
        )
        + residual_direct
    )
    return {
        "channels": channels,
        "gram": gram,
        "direct_fourth_trace": direct,
        "gram_fourth_trace": total,
        "quadratic_channel_energy": float(np.real(gram[2, 2])),
        "quadratic_schur_residual": max(0.0, residual),
        "quadratic_projection_residual": residual_direct,
        "shorted_fourth_trace": shorted_total,
        "minimum_gram_eigenvalue": float(np.linalg.eigvalsh(gram).min()),
    }


def von_mangoldt_prime_powers(limit: int) -> dict[int, float]:
    """Return Lambda(n)/sqrt(n), supported on prime powers n <= limit."""
    if limit < 2:
        return {}
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    atoms: dict[int, float] = {}
    for p in np.flatnonzero(sieve):
        value = int(p)
        while value <= limit:
            atoms[value] = math.log(int(p)) / math.sqrt(value)
            if value > limit // int(p):
                break
            value *= int(p)
    return atoms


def multiplicative_convolution_power(
    atoms: dict[int, float], power: int
) -> dict[int, float]:
    """Power under Dirichlet/multiplicative convolution."""
    result: dict[int, float] = {1: 1.0}
    for _ in range(power):
        updated: defaultdict[int, float] = defaultdict(float)
        for left, left_coefficient in result.items():
            for right, right_coefficient in atoms.items():
                updated[left * right] += left_coefficient * right_coefficient
        result = dict(updated)
    return result


def interval_fourier_kernel(frequency: np.ndarray, height: float) -> np.ndarray:
    """T^{-1} integral_T^{2T} exp(i t frequency) dt."""
    return np.exp(1.5j * height * frequency) * np.sinc(
        height * frequency / (2.0 * math.pi)
    )


def multiplicative_mean(
    left: dict[int, float],
    right: dict[int, float],
    height: float,
    chunk_size: int = 384,
) -> complex:
    """Mean of Q_left(t) conjugate(Q_right(t)) on [T,2T]."""
    left_items = tuple(left.items())
    right_integers = np.array(tuple(right), dtype=float)
    right_coefficients = np.array(tuple(right.values()), dtype=float)
    right_logs = np.log(right_integers)
    total = 0.0 + 0.0j
    for start in range(0, len(left_items), chunk_size):
        block = left_items[start : start + chunk_size]
        left_integers = np.array([item[0] for item in block], dtype=float)
        left_coefficients = np.array([item[1] for item in block], dtype=float)
        frequency = np.log(left_integers)[:, None] - right_logs[None, :]
        kernel = interval_fourier_kernel(frequency, height)
        total += np.sum(
            left_coefficients[:, None]
            * right_coefficients[None, :]
            * kernel
        )
    return complex(total)


def prime_sign_resonance_ledger(limit: int, height: float) -> dict[str, object]:
    """Split the fourth mean of Q+conj(Q) into 2+2, 3+1 and 4+0."""
    atoms = von_mangoldt_prime_powers(limit)
    powers = {
        power: multiplicative_convolution_power(atoms, power)
        for power in range(5)
    }
    means = {
        positive: multiplicative_mean(
            powers[positive], powers[4 - positive], height
        )
        for positive in range(5)
    }
    two_two_full = means[2]
    two_two_diagonal = sum(value * value for value in powers[2].values())
    two_two_off_diagonal = two_two_full.real - two_two_diagonal
    family_contributions = {
        "2+2": 6.0 * two_two_full.real,
        "3+1": 4.0 * (means[3] + means[1]).real,
        "4+0": (means[4] + means[0]).real,
    }
    total = sum(family_contributions.values())
    return {
        "limit": limit,
        "height": height,
        "atom_count": len(atoms),
        "square_support": len(powers[2]),
        "cube_support": len(powers[3]),
        "fourth_support": len(powers[4]),
        "means": means,
        "family_contributions": family_contributions,
        "total_fourth_mean": total,
        "two_two_full": float(two_two_full.real),
        "two_two_imaginary_residual": float(abs(two_two_full.imag)),
        "two_two_diagonal": float(two_two_diagonal),
        "two_two_off_diagonal": float(two_two_off_diagonal),
        "two_two_full_to_diagonal": float(
            two_two_full.real / two_two_diagonal
        ),
    }


def direct_sampled_fourth_mean(
    atoms: dict[int, float], height: float, samples: int
) -> float:
    times = np.linspace(height, 2.0 * height, samples)
    integers = np.array(tuple(atoms), dtype=float)
    coefficients = np.array(tuple(atoms.values()), dtype=float)
    q_values = np.exp(1j * np.outer(times, np.log(integers))) @ coefficients
    symbol = 2.0 * np.real(q_values)
    return float(np.trapezoid(symbol**4, times) / height)


def audit_quadratic_matrix_channels() -> None:
    rng = np.random.default_rng(260901)
    for dimension in (3, 7, 11):
        background = hermitian_random(rng, dimension)
        prime = hermitian_random(rng, dimension)
        ledger = quadratic_channel_gram(background, prime)
        scale = max(1.0, abs(ledger["direct_fourth_trace"]))
        assert (
            abs(
                ledger["direct_fourth_trace"]
                - ledger["gram_fourth_trace"]
            )
            <= TOL * scale
        )
        assert ledger["minimum_gram_eigenvalue"] >= -TOL * scale
        assert ledger["quadratic_schur_residual"] >= 0.0
        assert (
            abs(
                ledger["quadratic_schur_residual"]
                - ledger["quadratic_projection_residual"]
            )
            <= TOL * scale
        )
        assert (
            abs(
                ledger["direct_fourth_trace"]
                - ledger["shorted_fourth_trace"]
            )
            <= TOL * scale
        )
        assert (
            ledger["quadratic_schur_residual"]
            <= ledger["quadratic_channel_energy"] + TOL * scale
        )
    print("quadratic matrix-channel Gram identities passed")


def audit_prime_sign_resonances() -> None:
    small_limit, small_height = 11, 17.0
    small = prime_sign_resonance_ledger(small_limit, small_height)
    sampled = direct_sampled_fourth_mean(
        von_mangoldt_prime_powers(small_limit), small_height, 30_001
    )
    assert abs(sampled - small["total_fourth_mean"]) <= 2.0e-5 * max(
        1.0, abs(sampled)
    )
    assert small["two_two_full"] >= -TOL
    assert small["two_two_imaginary_residual"] <= TOL

    for limit in (24, 48, 72):
        ledger = prime_sign_resonance_ledger(limit, float(limit))
        assert ledger["two_two_full"] >= -TOL
        assert abs(
            sum(ledger["family_contributions"].values())
            - ledger["total_fourth_mean"]
        ) <= TOL * max(1.0, abs(ledger["total_fourth_mean"]))
        print(
            "prime fourth prototype: "
            f"X=T={limit}, atoms={ledger['atom_count']}, "
            f"|supp Lambda*Lambda|={ledger['square_support']}, "
            f"2+2 full/diag={ledger['two_two_full_to_diagonal']:.6f}, "
            f"families={ledger['family_contributions']}"
        )


def audit_flat_window_target_ledger() -> None:
    kappa = 0.672500703679
    threshold = 4.0 / (9.0 * kappa) - 1.0 / 3.0
    formal_diagonal = 4.0 / 15.0
    allowed_remainder = threshold - formal_diagonal
    sine_prediction = 1.0 / 4.0
    predicted_off_diagonal = sine_prediction - formal_diagonal
    assert abs(predicted_off_diagonal + 1.0 / 60.0) <= TOL
    assert 0.0608 < allowed_remainder < 0.0610
    print(
        "flat-window target: "
        f"b4 threshold={threshold:.12f}, "
        f"formal diagonal={formal_diagonal:.12f}, "
        f"allowed total remainder={allowed_remainder:.12f}, "
        f"sine off-diagonal={predicted_off_diagonal:.12f}"
    )


def main() -> None:
    audit_quadratic_matrix_channels()
    audit_prime_sign_resonances()
    audit_flat_window_target_ledger()
    print("Fourth-moment channel audits passed.")


if __name__ == "__main__":
    main()

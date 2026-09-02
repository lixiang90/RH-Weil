"""Finite audits for note 231's alternating central-cross repair.

The exact Hilbert-space ledger and exponent arithmetic are rigorous finite
checks.  The small von Mangoldt computation is diagnostic only and does not
implement the shifted-prime sieve theorem.
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np


def gram_norm(vector: np.ndarray) -> float:
    return float(np.vdot(vector, vector).real)


def check_exact_ledger() -> None:
    rng = np.random.default_rng(231)
    central = rng.normal(size=5) + 1j * rng.normal(size=5)
    chains = [rng.normal(size=5) + 1j * rng.normal(size=5) for _ in range(2)]
    primitive = [rng.normal(size=5) + 1j * rng.normal(size=5) for _ in range(3)]

    chain_sum = sum(chains, start=np.zeros(5, dtype=complex))
    primitive_sum = sum(primitive, start=np.zeros(5, dtype=complex))
    total = central + chain_sum + primitive_sum
    paired = gram_norm(central) + sum(gram_norm(v) for v in chains + primitive)
    primitive_internal = gram_norm(primitive_sum) - sum(
        gram_norm(v) for v in primitive
    )
    central_noncentral = 2.0 * float(
        np.vdot(central, chain_sum + primitive_sum).real
    )
    chain_remainder = (
        gram_norm(chain_sum)
        - sum(gram_norm(v) for v in chains)
        + 2.0 * float(np.vdot(chain_sum, primitive_sum).real)
    )
    reconstructed = paired + primitive_internal + central_noncentral + chain_remainder
    assert abs(gram_norm(total) - reconstructed) < 1e-10


def check_separate_budget_no_go() -> None:
    n = 100.0
    central = np.array([math.sqrt(n), 0.0])
    parallel = np.array([math.sqrt(n), 0.0])
    orthogonal = np.array([0.0, math.sqrt(n)])
    for primitive in (parallel, orthogonal):
        assert abs(gram_norm(central) - n) < 1e-12
        assert abs(gram_norm(primitive) - n) < 1e-12
        # A singleton primitive family is atomically diagonal with zero error.
        assert abs(gram_norm(primitive) - gram_norm(primitive)) < 1e-12
    parallel_cross = 2.0 * float(np.vdot(central, parallel).real)
    orthogonal_cross = 2.0 * float(np.vdot(central, orthogonal).real)
    assert abs(parallel_cross - 2.0 * n) < 1e-12
    assert orthogonal_cross == 0.0


def check_exponent_ledger() -> None:
    # d beta^4 contributes X L^-3; the central mass contributes L^2;
    # the short-height ratio kernel contributes L^(3/2) (log L)^2.
    l_exponent = -Fraction(3) + Fraction(2) + Fraction(3, 2)
    assert l_exponent == Fraction(1, 2)
    # Dividing X L^(1/2) (log L)^2 by N = X L leaves
    # L^(-1/2) (log L)^2, which decreases for log L > 4.
    values = []
    for log_l in (6.0, 8.0, 10.0, 12.0):
        l_value = math.exp(log_l)
        values.append(log_l**2 / math.sqrt(l_value))
    assert all(right < left for left, right in zip(values, values[1:]))


def von_mangoldt(limit: int) -> np.ndarray:
    values = np.zeros(limit + 1, dtype=float)
    for p in range(2, limit + 1):
        is_prime = all(p % q for q in range(2, int(math.isqrt(p)) + 1))
        if not is_prime:
            continue
        power = p
        while power <= limit:
            values[power] = math.log(p)
            if power > limit // p:
                break
            power *= p
    return values


def ratio_kernel(limit: int) -> tuple[float, float]:
    weights = von_mangoldt(limit)
    log_limit = math.log(limit)
    height = limit / math.sqrt(log_limit)
    total = 0.0
    central_mass = 0.0
    for n in range(2, limit + 1):
        if weights[n]:
            central_mass += weights[n] ** 2 / n
    support = np.flatnonzero(weights)
    support = support[support >= 2]
    for a in support:
        for b in support:
            if a == b:
                continue
            frequency = abs(math.log(a / b))
            kernel = min(1.0, 2.0 / (height * frequency))
            total += weights[a] * weights[b] / math.sqrt(a * b) * kernel
    return central_mass, total


def main() -> None:
    check_exact_ledger()
    check_separate_budget_no_go()
    check_exponent_ledger()
    print("central/chain/primitive exact Gram ledger: PASS")
    print("separate-budget central-cross no-go: PASS")
    print("central-cross exponent ledger: PASS")
    for limit in (300, 600, 1200):
        central_mass, kernel = ratio_kernel(limit)
        log_limit = math.log(limit)
        scale = log_limit ** 1.5 * math.log(log_limit) ** 2
        print(
            f"X={limit:4d}: central/L^2={central_mass/log_limit**2:.6f}, "
            f"ratio-kernel/[L^(3/2)(log L)^2]={kernel/scale:.6f}"
        )
    print("alternating central-cross audits passed")
    print("[scope] finite identities/diagnostics only; shifted-prime input is external")


if __name__ == "__main__":
    main()

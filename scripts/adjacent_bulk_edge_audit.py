"""Finite audit for the adjacent-product bulk edge theorem.

The theorem proved in note 203 reduces the arithmetic majorant to

    2 K L^{-4} sum_{ab in (X^(1-delta), X]} w_a w_b
        (1 - log(ab)/L)^q,

where w_n = Lambda(n)^2/n, q = 2*kappa+1, and K is the endpoint
overlap constant. Prefix log-moments evaluate this sum without forming
all pairs. The computation checks only the finite arithmetic reduction
and its predicted limiting integral; it is not evidence for a zeta
fourth-moment asymptotic.
"""

from __future__ import annotations

import argparse
import bisect
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class PrimePowerWeight:
    n: int
    weight: float
    log_n: float


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_power_weights(limit: int) -> list[PrimePowerWeight]:
    values: list[PrimePowerWeight] = []
    for p in primes_up_to(limit):
        log_p = math.log(p)
        power = p
        while power <= limit:
            values.append(
                PrimePowerWeight(power, log_p * log_p / power, math.log(power))
            )
            if power > limit // p:
                break
            power *= p
    values.sort(key=lambda item: item.n)
    return values


def prefix_log_moments(
    values: list[PrimePowerWeight], max_degree: int
) -> list[list[float]]:
    prefix = [[0.0] * (len(values) + 1) for _ in range(max_degree + 1)]
    for index, item in enumerate(values, start=1):
        log_power = 1.0
        for degree in range(max_degree + 1):
            prefix[degree][index] = prefix[degree][index - 1] + item.weight * log_power
            log_power *= item.log_n
    return prefix


def interval_moment(prefix: list[float], left: int, right: int) -> float:
    return prefix[right] - prefix[left]


def weighted_edge_proxy(limit: int, delta: float, q: int, overlap_k: float) -> float:
    if q < 0 or q % 2 != 1:
        raise ValueError("q must be a nonnegative odd integer")
    if not 0.0 < delta <= 1.0:
        raise ValueError("delta must lie in (0, 1]")

    values = prime_power_weights(limit)
    integers = [item.n for item in values]
    prefix = prefix_log_moments(values, q)
    log_x = math.log(limit)
    lower_product = math.exp((1.0 - delta) * log_x)
    total = 0.0

    for item in values:
        upper_b = limit / item.n
        lower_b = lower_product / item.n
        left = bisect.bisect_right(integers, lower_b)
        right = bisect.bisect_right(integers, upper_b)
        if left >= right:
            continue

        center = log_x - item.log_n
        inner = 0.0
        for degree in range(q + 1):
            coefficient = (
                math.comb(q, degree)
                * center ** (q - degree)
                * (-1.0) ** degree
            )
            inner += coefficient * interval_moment(prefix[degree], left, right)
        if inner < 0.0 and abs(inner) < 1e-7:
            inner = 0.0
        if inner < 0.0:
            raise AssertionError(f"negative prefix-moment result: {inner}")
        total += item.weight * inner / log_x**q

    return 2.0 * overlap_k * total / log_x**4


def limiting_edge_majorant(delta: float, q: int, overlap_k: float) -> float:
    # 2K * integral_{r+s in (1-delta,1]} r s (1-r-s)^q dr ds
    # = (K/3) integral_0^delta t^q (1-t)^3 dt.
    integral = 0.0
    for degree in range(4):
        integral += (
            math.comb(3, degree)
            * (-1.0) ** degree
            * delta ** (q + degree + 1)
            / (q + degree + 1)
        )
    return overlap_k * integral / 3.0


def run_audit(limits: list[int], delta: float) -> None:
    cases = (
        ("flat", 1, 1.0),
        ("endpoint-cosine", 3, math.pi**2 / 6.0),
    )
    for label, q, overlap_k in cases:
        target = limiting_edge_majorant(delta, q, overlap_k)
        print(f"{label}: delta={delta:.3f}, limiting majorant={target:.12g}")
        last_error = None
        for limit in limits:
            value = weighted_edge_proxy(limit, delta, q, overlap_k)
            error = abs(value - target)
            print(
                f"  X={limit:>8d}: finite={value:.12g}, "
                f"ratio={value / target:.8f}, abs_error={error:.3e}"
            )
            last_error = error
        assert last_error is not None and math.isfinite(last_error)

    flat_small = limiting_edge_majorant(delta, 1, 1.0)
    cosine_small = limiting_edge_majorant(delta, 3, math.pi**2 / 6.0)
    assert flat_small <= delta**2 / 6.0 + 1e-15
    assert cosine_small <= math.pi**2 * delta**4 / 72.0 + 1e-15


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limits", nargs="+", type=int, default=[20_000, 100_000, 500_000])
    parser.add_argument("--delta", type=float, default=0.20)
    args = parser.parse_args()
    run_audit(args.limits, args.delta)


if __name__ == "__main__":
    main()

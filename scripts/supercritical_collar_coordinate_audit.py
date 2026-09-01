"""Finite identity checks for note 215's supercritical collar.

This script audits the product-excess/ratio coordinate map, the exact radial
support depth, the determinant-scale lift, and the alias support gap beyond
``ab <= X``.  It does not test the asymptotic E2 theorem or prove an infinite
Gram estimate.
"""

from __future__ import annotations

import bisect
import math
from dataclasses import dataclass

from alternating_ratio_cluster_audit import prime_power_atoms


@dataclass(frozen=True)
class CollarAtom:
    a: int
    b: int
    prime_a: int
    prime_b: int
    x_a: float
    x_b: float
    excess: float
    ratio: float


def primitive_atoms(limit: int) -> list[CollarAtom]:
    logarithm = math.log(limit)
    atoms = prime_power_atoms(limit)
    records: list[CollarAtom] = []
    for left in atoms:
        for right in atoms:
            if left.prime == right.prime:
                continue
            x_a = math.log(left.n)
            x_b = math.log(right.n)
            records.append(
                CollarAtom(
                    a=left.n,
                    b=right.n,
                    prime_a=left.prime,
                    prime_b=right.prime,
                    x_a=x_a,
                    x_b=x_b,
                    excess=x_a + x_b - logarithm,
                    ratio=x_a - x_b,
                )
            )
    records.sort(key=lambda item: item.ratio)
    return records


def support_interval(record: CollarAtom, length: float) -> tuple[float, float]:
    lower = (record.excess + record.ratio) / 2.0
    upper = length / 2.0 + min(0.0, record.ratio)
    return lower, upper


def audit_coordinates_and_depth(limit: int, records: list[CollarAtom]) -> None:
    length = math.log(limit)
    tolerance = 2.0e-12
    for record in records:
        reconstructed_a = (length + record.excess + record.ratio) / 2.0
        reconstructed_b = (length + record.excess - record.ratio) / 2.0
        assert abs(reconstructed_a - record.x_a) <= tolerance
        assert abs(reconstructed_b - record.x_b) <= tolerance
        assert abs(record.ratio) <= length - abs(record.excess) + tolerance

        lower, upper = support_interval(record, length)
        depth = (length - record.excess - abs(record.ratio)) / 2.0
        assert depth >= -tolerance
        assert abs((upper - lower) - depth) <= tolerance
        assert lower >= -length / 2.0 - tolerance
        assert upper <= length / 2.0 + tolerance


def audit_determinant_scale(limit: int, records: list[CollarAtom]) -> None:
    length = math.log(limit)
    if not records:
        raise AssertionError("empty primitive family")
    stride = max(1, len(records) // 137)
    sample = records[::stride][:137]
    for left in sample:
        for right in sample[::7]:
            delta = left.ratio - right.ratio
            m = left.a * right.b
            n = left.b * right.a
            predicted_m = length + (left.excess + right.excess + delta) / 2.0
            predicted_n = length + (left.excess + right.excess - delta) / 2.0
            assert abs(math.log(m) - predicted_m) <= 3.0e-12
            assert abs(math.log(n) - predicted_n) <= 3.0e-12
            assert abs(math.log(m / n) - delta) <= 3.0e-12


def audit_alias_gap(limit: int, records: list[CollarAtom]) -> int:
    length = math.log(limit)
    radius = 0.45
    ratios = [record.ratio for record in records]
    checked = 0
    minimum_gap = math.inf
    for high in records:
        target = high.ratio - length
        start = bisect.bisect_left(ratios, target - radius)
        stop = bisect.bisect_right(ratios, target + radius)
        for low in records[start:stop]:
            delta = high.ratio - low.ratio
            epsilon = length - delta
            if abs(epsilon) >= min(radius, math.log(2.0)):
                continue
            assert high.ratio >= 0.0
            assert low.ratio <= 0.0
            high_interval = support_interval(high, length)
            low_interval = support_interval(low, length)
            shifted_low = (low_interval[0] - epsilon, low_interval[1] - epsilon)
            assert shifted_low[0] >= -length / 2.0 - 2.0e-12
            gap = high_interval[0] - shifted_low[1]
            assert abs(gap - high.x_b) <= 3.0e-12
            assert gap >= math.log(2.0) - 3.0e-12
            minimum_gap = min(minimum_gap, gap)
            checked += 1
    if checked == 0:
        raise AssertionError("no +L alias pairs found")
    print(
        f"X={limit:>5d}: primitive={len(records):>7d}, "
        f"alias-pairs={checked:>7d}, min-gap={minimum_gap:.9f}"
    )
    return checked


def audit_logarithmic_collar(limit: int, records: list[CollarAtom]) -> None:
    length = math.log(limit)
    kappa = 0.5
    cutoff = limit * length**kappa
    hyperbolic = sum(record.a * record.b <= limit for record in records)
    collar = sum(record.a * record.b <= cutoff for record in records)
    supercritical = collar - hyperbolic
    assert supercritical > 0
    assert collar > hyperbolic
    print(
        f"  kappa={kappa:.1f}: ab<=X atoms={hyperbolic}, "
        f"ab<=X*L^k atoms={collar}, new-collar={supercritical}"
    )


def main() -> None:
    for limit in (300, 1_000):
        records = primitive_atoms(limit)
        audit_coordinates_and_depth(limit, records)
        audit_determinant_scale(limit, records)
        audit_alias_gap(limit, records)
        audit_logarithmic_collar(limit, records)
    print("supercritical collar coordinate and alias audits passed")


if __name__ == "__main__":
    main()

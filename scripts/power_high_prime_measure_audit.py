"""Finite prime-power audit of the theta=3/4 response measure.

The experiment keeps the four von Mangoldt factors, a balanced factor cell,
the flat translated six-window overlap, the exact carrier, and all consecutive
Gabor samples.  It reports mesoscopic discrepancy and signed band response;
no finite trend is promoted to an asymptotic statement.
"""

from __future__ import annotations

import math

from alternating_ratio_cluster_audit import prime_power_atoms
from ordinary_seam_kernel_audit import (
    RatioRecord,
    flat_support,
    periodic_shifted_overlap,
)
from power_high_bandpass_audit import finite_kernel


def balanced_records(limit: int) -> tuple[int, list[RatioRecord]]:
    center = limit**0.75
    lower = 0.70 * center
    upper = 1.30 * center
    factors = [atom for atom in prime_power_atoms(limit) if lower <= atom.n <= upper]
    records: list[RatioRecord] = []
    for numerator in factors:
        for denominator in factors:
            if numerator.prime == denominator.prime:
                continue
            numerator_log = math.log(numerator.n)
            denominator_log = math.log(denominator.n)
            records.append(
                RatioRecord(
                    numerator=numerator.n,
                    denominator=denominator.n,
                    numerator_log=numerator_log,
                    denominator_log=denominator_log,
                    ratio_log=numerator_log - denominator_log,
                    weight=(
                        numerator.log_prime
                        * denominator.log_prime
                        / (
                            4.0
                            * math.pi**2
                            * math.sqrt(numerator.n * denominator.n)
                        )
                    ),
                )
            )
    records.sort(key=lambda record: record.ratio_log)
    return len(factors), records


def flat_overlap_weight(
    left: RatioRecord, right: RatioRecord, length: float
) -> float:
    delta = left.ratio_log - right.ratio_log
    overlap = periodic_shifted_overlap(
        flat_support(left, length),
        flat_support(right, length),
        delta,
        length,
    )
    return overlap / length


def cumulative_discrepancy(
    events: list[tuple[float, float]], radius: float
) -> tuple[float, float]:
    events.sort(key=lambda item: item[0])
    total = sum(weight for _, weight in events)
    density = total / (2.0 * radius)
    cumulative = 0.0
    discrepancy = 0.0
    for location, weight in events:
        baseline = density * (location + radius)
        discrepancy = max(discrepancy, abs(cumulative - baseline))
        cumulative += weight
        discrepancy = max(discrepancy, abs(cumulative - baseline))
    discrepancy = max(discrepancy, abs(cumulative - total))
    return total, discrepancy


def audit_prime_measure(limit: int) -> None:
    length = math.log(limit)
    factor_count, records = balanced_records(limit)
    radius = limit**0.25
    ratio_radius = radius / limit

    events: list[tuple[float, float]] = []
    signed = 0.0
    absolute = 0.0
    core_signed = 0.0
    core_mass = 0.0
    determinant_two_mass = 0.0
    pair_count = 0

    for left_index, left in enumerate(records):
        for right in records[left_index + 1 :]:
            ratio_gap = right.ratio_log - left.ratio_log
            if ratio_gap > ratio_radius:
                break
            determinant = (
                left.numerator * right.denominator
                - left.denominator * right.numerator
            )
            if determinant == 0:
                continue
            overlap = flat_overlap_weight(left, right, length)
            if overlap <= 0.0:
                continue
            t = limit * ratio_gap
            one_direction_mass = left.weight * right.weight * overlap
            ordered_mass = 2.0 * one_direction_mass
            response = finite_kernel(limit, t)
            events.append((-t, one_direction_mass))
            events.append((t, one_direction_mass))
            signed += ordered_mass * response
            absolute += ordered_mass * abs(response)
            if t <= 1.0:
                core_signed += ordered_mass * response
                core_mass += ordered_mass
            if abs(determinant) == 2:
                determinant_two_mass += ordered_mass
            pair_count += 1

    total_mass, discrepancy = cumulative_discrepancy(events, radius)
    if total_mass <= 0.0 or core_mass <= 0.0:
        raise AssertionError("empty prime-power response measure")
    if abs(signed) > absolute + 1.0e-12:
        raise AssertionError("signed response exceeds its absolute majorant")
    if abs(total_mass - sum(weight for _, weight in events)) > 1.0e-12:
        raise AssertionError("response-measure mass mismatch")

    print(
        f"X={limit:>5d}: factors={factor_count:>3d}, ratios={len(records):>5d}, "
        f"M=X^.25={radius:.4f}, pairs={pair_count:>7d}, "
        f"core-mass/B={core_mass/total_mass:.6e}, "
        f"core-signed/B={core_signed/total_mass:+.6e}, "
        f"band-signed/B={signed/total_mass:+.6e}, "
        f"band-abs/B={absolute/total_mass:.6e}, "
        f"E*log(M)/B={discrepancy*math.log(radius)/total_mass:.6e}, "
        f"det2-mass/B={determinant_two_mass/total_mass:.6e}, "
        f"B={total_mass:.6e}, signed/L^4={signed/length**4:+.6e}, "
        f"E*log(M)/L^4={discrepancy*math.log(radius)/length**4:.6e}"
    )


def main() -> None:
    for limit in (400, 800, 1_600, 3_200, 6_400):
        audit_prime_measure(limit)
    print("power-high prime response-measure diagnostics passed")
    print("[scope] finite flat-window evidence only; no four-prime asymptotic")


if __name__ == "__main__":
    main()

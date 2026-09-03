"""Finite audit of the centered Vaughan divisor-kernel pullback.

For a balanced numerator cell this script builds the exact synthesis map

    T[a,r] = sum_{v > V, r*v*w = a} Lambda(v),

checks T*mu = Lambda, constructs the central-shell centered physical response
kernel K = T^* B T, and verifies the two-dimensional discrete Abel identity.
The reported mixed-variation budgets are diagnostics only; they are not prime
asymptotics and make no RH claim.
"""

from __future__ import annotations

import math

from alternating_ratio_cluster_audit import prime_power_atoms
from ordinary_seam_kernel_audit import RatioRecord
from power_high_bandpass_audit import finite_kernel
from power_high_physical_vaughan_channel_audit import (
    mobius_and_von_mangoldt,
)
from power_high_prime_measure_audit import flat_overlap_weight


def exact_central_average(limit: int, radius: float) -> float:
    """Average of the exact consecutive-band kernel on [0, radius]."""

    length = math.log(limit)
    dimension = round(limit * length)
    total = 0.0
    for index in range(dimension):
        frequency = 1.0 + index / (limit * length)
        angle = 2.0 * math.pi * frequency * radius
        total += math.sin(angle) / angle
    return total / dimension


def divisor_synthesis(
    lower: int,
    upper: int,
    cutoff_v: int,
    von_mangoldt: list[float],
) -> tuple[int, list[dict[int, float]]]:
    """Return the active r range and sparse rows of the map T."""

    r_bound = upper // (cutoff_v + 1)
    rows: list[dict[int, float]] = [dict() for _ in range(upper + 1)]
    high_prime_powers = [
        value
        for value in range(cutoff_v + 1, upper + 1)
        if von_mangoldt[value]
    ]
    for divisor in range(1, r_bound + 1):
        for prime_power in high_prime_powers:
            product = divisor * prime_power
            if product > upper:
                break
            first_completion = max(1, (lower + product - 1) // product)
            last_completion = upper // product
            coefficient = von_mangoldt[prime_power]
            for completion in range(first_completion, last_completion + 1):
                numerator = product * completion
                rows[numerator][divisor] = (
                    rows[numerator].get(divisor, 0.0) + coefficient
                )
    return r_bound, rows


def divisor_ratio_records(
    limit: int,
    lower: int,
    upper: int,
    von_mangoldt: list[float],
    prime_base: list[int],
    synthesis_rows: list[dict[int, float]],
) -> list[tuple[RatioRecord, dict[int, float]]]:
    denominator_atoms = [
        atom
        for atom in prime_power_atoms(limit)
        if lower <= atom.n <= upper
    ]
    records: list[tuple[RatioRecord, dict[int, float]]] = []
    for numerator in range(lower, upper + 1):
        if not synthesis_rows[numerator]:
            continue
        numerator_log = math.log(numerator)
        for denominator in denominator_atoms:
            # Fixed channel-independent mask.  On the Lambda support this is
            # the original distinct-prime-base restriction.
            if (
                prime_base[numerator]
                and prime_base[numerator] == denominator.prime
            ):
                continue
            normalization = denominator.log_prime / (
                4.0 * math.pi**2 * math.sqrt(numerator * denominator.n)
            )
            record = RatioRecord(
                numerator=numerator,
                denominator=denominator.n,
                numerator_log=numerator_log,
                denominator_log=math.log(denominator.n),
                ratio_log=numerator_log - math.log(denominator.n),
                weight=normalization * von_mangoldt[numerator],
            )
            features = {
                divisor: normalization * coefficient
                for divisor, coefficient in synthesis_rows[numerator].items()
            }
            records.append((record, features))
    records.sort(key=lambda item: item[0].ratio_log)
    return records


def audit_pullback(limit: int, cutoff_exponent: float = 0.25) -> None:
    length = math.log(limit)
    center = limit**0.75
    lower = math.ceil(0.70 * center)
    upper = math.floor(1.30 * center)
    cutoff = max(2, round(center**cutoff_exponent))
    mobius, von_mangoldt, prime_base = mobius_and_von_mangoldt(upper)
    r_bound, synthesis_rows = divisor_synthesis(
        lower, upper, cutoff, von_mangoldt
    )

    synthesis_error = 0.0
    for numerator in range(lower, upper + 1):
        reconstructed = sum(
            mobius[divisor] * coefficient
            for divisor, coefficient in synthesis_rows[numerator].items()
        )
        synthesis_error = max(
            synthesis_error,
            abs(reconstructed - von_mangoldt[numerator]),
        )
    if synthesis_error > 1.0e-10:
        raise AssertionError("T*mu does not reconstruct Lambda")

    records = divisor_ratio_records(
        limit,
        lower,
        upper,
        von_mangoldt,
        prime_base,
        synthesis_rows,
    )
    central_radius = limit**0.5
    ratio_radius = central_radius / limit
    kernel_average = exact_central_average(limit, central_radius)
    kernel = [
        [0.0 for _ in range(r_bound + 1)]
        for _ in range(r_bound + 1)
    ]
    direct_response = 0.0
    pair_count = 0

    for left_index, (left, left_features) in enumerate(records):
        for right, right_features in records[left_index + 1 :]:
            gap = right.ratio_log - left.ratio_log
            if gap > ratio_radius:
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
            centered_response = (
                finite_kernel(limit, limit * gap) - kernel_average
            )
            direct_response += (
                2.0
                * left.weight
                * right.weight
                * overlap
                * centered_response
            )
            for row, left_value in left_features.items():
                for column, right_value in right_features.items():
                    contribution = (
                        overlap
                        * centered_response
                        * left_value
                        * right_value
                    )
                    kernel[row][column] += contribution
                    kernel[column][row] += contribution
            pair_count += 1

    pullback_response = 0.0
    for row in range(1, r_bound + 1):
        for column in range(1, r_bound + 1):
            pullback_response += (
                mobius[row] * kernel[row][column] * mobius[column]
            )
    if abs(pullback_response - direct_response) > 1.0e-9 * max(
        1.0, abs(direct_response)
    ):
        raise AssertionError("K = T^* B T pullback reconstruction failed")

    mertens = [0.0] * (r_bound + 1)
    for divisor in range(1, r_bound + 1):
        mertens[divisor] = mertens[divisor - 1] + mobius[divisor]

    abel_response = 0.0
    weighted_variation = 0.0
    mixed_variation = 0.0
    block_count = r_bound.bit_length()
    dyadic_blocks = [
        [0.0 for _ in range(block_count)]
        for _ in range(block_count)
    ]
    for row in range(1, r_bound + 1):
        for column in range(1, r_bound + 1):
            value = kernel[row][column]
            if row < r_bound:
                value -= kernel[row + 1][column]
            if column < r_bound:
                value -= kernel[row][column + 1]
            if row < r_bound and column < r_bound:
                value += kernel[row + 1][column + 1]
            signed_abel_entry = mertens[row] * mertens[column] * value
            abel_response += signed_abel_entry
            dyadic_blocks[row.bit_length() - 1][
                column.bit_length() - 1
            ] += signed_abel_entry
            weighted_variation += (
                abs(mertens[row] * mertens[column] * value)
            )
            mixed_variation += abs(value)

    if abs(abel_response - direct_response) > 1.0e-9 * max(
        1.0, abs(direct_response)
    ):
        raise AssertionError("two-dimensional Abel identity failed")
    maximum_mertens = max(abs(value) for value in mertens)
    crude_variation_bound = maximum_mertens**2 * mixed_variation
    dyadic_reconstruction = sum(sum(block) for block in dyadic_blocks)
    if abs(dyadic_reconstruction - direct_response) > 1.0e-9 * max(
        1.0, abs(direct_response)
    ):
        raise AssertionError("dyadic Abel blocks do not reconstruct response")
    dyadic_l1 = sum(
        abs(value) for block in dyadic_blocks for value in block
    )
    dyadic_l2 = math.sqrt(
        sum(value * value for block in dyadic_blocks for value in block)
    )
    dyadic_cauchy_bound = block_count * dyadic_l2
    if dyadic_l1 + 1.0e-14 < abs(direct_response):
        raise AssertionError("dyadic signed-block majorant failed")
    if dyadic_cauchy_bound + 1.0e-14 < abs(direct_response):
        raise AssertionError("dyadic mean-square majorant failed")
    if weighted_variation + 1.0e-14 < abs(direct_response):
        raise AssertionError("weighted Abel majorant is smaller than response")
    if crude_variation_bound + 1.0e-14 < weighted_variation:
        raise AssertionError("crude mixed-variation majorant failed")

    relative_retention = (
        abs(direct_response) / weighted_variation
        if weighted_variation
        else 0.0
    )
    print(
        f"X={limit:>5d}: U=V={cutoff:>2d}, r={r_bound:>3d}, "
        f"records={len(records):>6d}, pairs={pair_count:>8d}, "
        f"avgK={kernel_average:+.3e}, max|M|={maximum_mertens:.0f}, "
        f"response/L^4={direct_response/length**4:+.3e}, "
        f"Abel-abs/L^4={weighted_variation/length**4:.3e}, "
        f"retention={relative_retention:.3e}, "
        f"dyadic-l1/L^4={dyadic_l1/length**4:.3e}, "
        f"dyadic-Cauchy/L^4={dyadic_cauchy_bound/length**4:.3e}, "
        f"crude/Abel-abs={crude_variation_bound/weighted_variation:.3e}"
    )


def main() -> None:
    for limit in (400, 800, 1_600, 3_200):
        audit_pullback(limit)
    print("Mobius divisor pullback and Abel audits passed")
    print("[scope] exact finite identity/evidence only; no prime asymptotic")


if __name__ == "__main__":
    main()

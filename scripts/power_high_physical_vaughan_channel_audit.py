"""Finite one-factor Vaughan audit of the power-high physical response.

The numerator von Mangoldt coefficient is split by the exact canonical
Type-I/Type-II identity, while the denominator coefficient, six-window
overlap, height phases, and all-ones physical direction are kept unchanged.
The output measures cancellation among the actual 2 x 2 response entries.
It is finite evidence only and proves no prime asymptotic.
"""

from __future__ import annotations

import math

from power_high_bandpass_audit import finite_kernel
from alternating_ratio_cluster_audit import prime_power_atoms
from ordinary_seam_kernel_audit import RatioRecord
from power_high_prime_measure_audit import flat_overlap_weight


def mobius_and_von_mangoldt(
    bound: int,
) -> tuple[list[int], list[float], list[int]]:
    mobius = [1] * (bound + 1)
    is_prime = [True] * (bound + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, bound + 1):
        if not is_prime[prime]:
            continue
        for multiple in range(prime, bound + 1, prime):
            is_prime[multiple] = False if multiple != prime else True
            mobius[multiple] *= -1
        square = prime * prime
        for multiple in range(square, bound + 1, square):
            mobius[multiple] = 0

    von_mangoldt = [0.0] * (bound + 1)
    prime_base = [0] * (bound + 1)
    for prime in range(2, bound + 1):
        if not is_prime[prime]:
            continue
        log_prime = math.log(prime)
        power = prime
        while power <= bound:
            von_mangoldt[power] = log_prime
            prime_base[power] = prime
            if power > bound // prime:
                break
            power *= prime
    return mobius, von_mangoldt, prime_base


def canonical_channels(
    bound: int, cutoff_u: int, cutoff_v: int
) -> tuple[list[float], list[float], list[float], list[int]]:
    mobius, von_mangoldt, prime_base = mobius_and_von_mangoldt(bound)

    a_u = [0] * (bound + 1)
    for divisor in range(1, min(cutoff_u, bound) + 1):
        coefficient = mobius[divisor]
        if coefficient == 0:
            continue
        for multiple in range(divisor, bound + 1, divisor):
            a_u[multiple] += coefficient

    lambda_high = [
        value if index > cutoff_v else 0.0
        for index, value in enumerate(von_mangoldt)
    ]
    convolution = [0.0] * (bound + 1)
    for divisor in range(1, bound + 1):
        coefficient = a_u[divisor]
        if coefficient == 0:
            continue
        for quotient in range(1, bound // divisor + 1):
            high_value = lambda_high[quotient]
            if high_value:
                convolution[divisor * quotient] += coefficient * high_value

    type_i = [
        convolution[index]
        + (von_mangoldt[index] if index <= cutoff_v else 0.0)
        for index in range(bound + 1)
    ]
    type_ii = [
        von_mangoldt[index] - type_i[index]
        for index in range(bound + 1)
    ]
    mu_high_lambda_high = [0.0] * (bound + 1)
    for divisor in range(cutoff_u + 1, bound + 1):
        mu_value = mobius[divisor]
        if mu_value == 0:
            continue
        for quotient in range(cutoff_v + 1, bound // divisor + 1):
            high_value = von_mangoldt[quotient]
            if high_value:
                mu_high_lambda_high[divisor * quotient] += (
                    mu_value * high_value
                )
    type_ii_direct = [0.0] * (bound + 1)
    for product in range(1, bound + 1):
        coefficient = mu_high_lambda_high[product]
        if coefficient == 0.0:
            continue
        for multiple in range(product, bound + 1, product):
            type_ii_direct[multiple] += coefficient

    maximum_residual = max(
        abs(type_i[index] + type_ii[index] - von_mangoldt[index])
        for index in range(1, bound + 1)
    )
    direct_type_ii_residual = max(
        abs(type_ii[index] - type_ii_direct[index])
        for index in range(1, bound + 1)
    )
    assert maximum_residual < 1.0e-12
    assert direct_type_ii_residual < 1.0e-10
    return von_mangoldt, type_i, type_ii, prime_base


def canonical_ratio_records(
    limit: int,
    von_mangoldt: list[float],
    type_i: list[float],
    type_ii: list[float],
    prime_base: list[int],
) -> tuple[list[RatioRecord], list[tuple[float, float]]]:
    center = limit**0.75
    lower = math.ceil(0.70 * center)
    upper = math.floor(1.30 * center)
    denominator_atoms = [
        atom
        for atom in prime_power_atoms(limit)
        if lower <= atom.n <= upper
    ]

    records_with_channels: list[
        tuple[RatioRecord, tuple[float, float]]
    ] = []
    for numerator in range(lower, upper + 1):
        if abs(type_i[numerator]) + abs(type_ii[numerator]) < 1.0e-15:
            continue
        numerator_log = math.log(numerator)
        for denominator in denominator_atoms:
            # This fixed mask agrees with the distinct-prime-base restriction
            # on the original Lambda support and is independent of the channel.
            if (
                prime_base[numerator]
                and prime_base[numerator] == denominator.prime
            ):
                continue
            denominator_log = math.log(denominator.n)
            normalization = denominator.log_prime / (
                4.0
                * math.pi**2
                * math.sqrt(numerator * denominator.n)
            )
            record = RatioRecord(
                numerator=numerator,
                denominator=denominator.n,
                numerator_log=numerator_log,
                denominator_log=denominator_log,
                ratio_log=numerator_log - denominator_log,
                weight=normalization * von_mangoldt[numerator],
            )
            records_with_channels.append(
                (
                    record,
                    (
                        normalization * type_i[numerator],
                        normalization * type_ii[numerator],
                    ),
                )
            )

    records_with_channels.sort(key=lambda item: item[0].ratio_log)
    records = [item[0] for item in records_with_channels]
    channel_weights = [item[1] for item in records_with_channels]
    return records, channel_weights


def audit_physical_channels(limit: int, cutoff_exponent: float) -> None:
    length = math.log(limit)
    center = limit**0.75
    cutoff = max(2, round(center**cutoff_exponent))
    bound = math.floor(1.30 * center)
    von_mangoldt, type_i, type_ii, prime_base = canonical_channels(
        bound, cutoff, cutoff
    )
    records, channel_weights = canonical_ratio_records(
        limit, von_mangoldt, type_i, type_ii, prime_base
    )

    radius = limit**0.25
    ratio_radius = radius / limit
    response_matrix = [[0.0, 0.0], [0.0, 0.0]]
    direct_response = 0.0
    pair_count = 0

    for left_index, left in enumerate(records):
        left_channels = channel_weights[left_index]
        for right_index in range(left_index + 1, len(records)):
            right = records[right_index]
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
            response = finite_kernel(limit, limit * ratio_gap)
            direct_response += (
                2.0 * left.weight * right.weight * overlap * response
            )
            right_channels = channel_weights[right_index]
            for row in range(2):
                for column in range(2):
                    response_matrix[row][column] += overlap * response * (
                        left_channels[row] * right_channels[column]
                        + right_channels[row] * left_channels[column]
                    )
            pair_count += 1

    reconstructed = sum(sum(row) for row in response_matrix)
    component_budget = sum(
        abs(value) for row in response_matrix for value in row
    )
    if abs(reconstructed - direct_response) > 1.0e-11 * max(
        1.0, abs(direct_response)
    ):
        raise AssertionError("physical two-channel reconstruction failed")
    if abs(response_matrix[0][1] - response_matrix[1][0]) > 1.0e-12:
        raise AssertionError("physical response matrix is not symmetric")

    cancellation_ratio = (
        abs(reconstructed) / component_budget if component_budget else 0.0
    )
    print(
        f"X={limit:>5d}: kappa={cutoff_exponent:.3f}, "
        f"U=V={cutoff:>2d}, pairs={pair_count:>7d}, "
        f"atoms={len(records):>6d}, "
        f"Delta_I,I={response_matrix[0][0]:+.6e}, "
        f"Delta_I,II={response_matrix[0][1]:+.6e}, "
        f"Delta_II,II={response_matrix[1][1]:+.6e}, "
        f"physical={reconstructed:+.6e}, "
        f"|physical|/entry-l1={cancellation_ratio:.6e}, "
        f"physical/L^4={reconstructed/length**4:+.6e}"
    )


def main() -> None:
    for limit in (400, 800, 1_600, 3_200, 6_400):
        for cutoff_exponent in (0.25, 1.0 / 3.0, 0.50):
            audit_physical_channels(limit, cutoff_exponent)
    print("power-high physical Vaughan-channel audits passed")
    print("[scope] exact finite identity/evidence only; no prime asymptotic")


if __name__ == "__main__":
    main()

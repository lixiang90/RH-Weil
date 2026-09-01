"""Finite exploration of the ordinary radial aperture seam.

The audit uses the exact time lattice ``alpha_k=T+2*pi*k/L`` and the
translated-support main term from note 213.  A flat compact window is used so
that every symbol overlap is an exact interval length.  This isolates the
arithmetic phase/determinant channel; it is not a proof for the smooth window
and it is not evidence for a zeta asymptotic.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass

import numpy as np

from alternating_ratio_cluster_audit import prime_power_atoms


@dataclass(frozen=True)
class RatioRecord:
    numerator: int
    denominator: int
    numerator_log: float
    denominator_log: float
    ratio_log: float
    weight: float


def primitive_hyperbolic_records(limit: int) -> list[RatioRecord]:
    atoms = prime_power_atoms(limit)
    records: list[RatioRecord] = []
    for numerator in atoms:
        for denominator in atoms:
            if numerator.n * denominator.n > limit:
                break
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
                        / (4.0 * math.pi**2 * math.sqrt(numerator.n * denominator.n))
                    ),
                )
            )
    records.sort(key=lambda item: item.ratio_log)
    assert len({(item.numerator, item.denominator) for item in records}) == len(
        records
    )
    return records


def flat_support(record: RatioRecord, length: float) -> tuple[float, float]:
    lower = record.numerator_log - length / 2.0
    upper = length / 2.0 + min(0.0, record.ratio_log)
    assert lower <= upper + 1.0e-12
    return lower, upper


def periodic_shifted_overlap(
    left: tuple[float, float],
    right: tuple[float, float],
    shift: float,
    period: float,
) -> float:
    total = 0.0
    for winding in (-1, 0, 1):
        right_lower = right[0] + shift + winding * period
        right_upper = right[1] + shift + winding * period
        total += max(0.0, min(left[1], right_upper) - max(left[0], right_lower))
    return total


def geometric_sum(dimension: int, spacing: float, delta: float) -> complex:
    angle = spacing * delta
    denominator = math.sin(angle / 2.0)
    if abs(denominator) < 1.0e-12:
        return complex(dimension)
    return complex(
        math.cos((dimension - 1) * angle / 2.0),
        math.sin((dimension - 1) * angle / 2.0),
    ) * (math.sin(dimension * angle / 2.0) / denominator)


def cross_main_term(
    left: RatioRecord,
    right: RatioRecord,
    length: float,
    height: float,
    dimension: int,
) -> tuple[float, float, int]:
    delta = left.ratio_log - right.ratio_log
    overlap = periodic_shifted_overlap(
        flat_support(left, length),
        flat_support(right, length),
        delta,
        length,
    )
    phase = complex(math.cos(height * delta), math.sin(height * delta))
    response = phase * geometric_sum(dimension, 2.0 * math.pi / length, delta)
    beta = 2.0 * math.pi / length
    # Twice the real part, since each unordered block pair occurs once.
    contribution = (
        2.0
        * beta**4
        * left.weight
        * right.weight
        * (overlap / length)
        * response.real
    )
    absolute_majorant = (
        2.0
        * beta**4
        * left.weight
        * right.weight
        * (overlap / length)
        * abs(response)
    )
    determinant = left.numerator * right.denominator - left.denominator * right.numerator
    return contribution, absolute_majorant, determinant


def diagonal_main_term(record: RatioRecord, length: float, dimension: int) -> float:
    support_length = flat_support(record, length)[1] - flat_support(record, length)[0]
    beta = 2.0 * math.pi / length
    return beta**4 * record.weight**2 * (support_length / length) * dimension


def audit_ordinary_neighbor_kernel() -> None:
    aperture_width = 0.25
    shifts = (0.0, 0.071, 0.139)
    for limit in (500, 1_000, 2_000, 5_000):
        length = math.log(limit)
        height = 2.0 * math.pi * limit
        dimension = round(limit * length)
        records = primitive_hyperbolic_records(limit)
        diagonal = sum(diagonal_main_term(record, length, dimension) for record in records)
        zero_scale = limit * length
        assert diagonal > 0.0

        reports: list[tuple[float, float, float, float, int]] = []
        for partition_shift in shifts:
            blocks: defaultdict[int, list[RatioRecord]] = defaultdict(list)
            for record in records:
                index = math.floor((record.ratio_log - partition_shift) / aperture_width)
                blocks[index].append(record)

            signed = 0.0
            absolute = 0.0
            critical_absolute = 0.0
            pair_count = 0
            for index, left_block in blocks.items():
                right_block = blocks.get(index + 1)
                if not right_block:
                    continue
                for left in left_block:
                    for right in right_block:
                        contribution, majorant, determinant = cross_main_term(
                            left, right, length, height, dimension
                        )
                        signed += contribution
                        absolute += majorant
                        if abs(left.ratio_log - right.ratio_log) <= 1.0 / limit:
                            critical_absolute += majorant
                        if determinant != 0:
                            pair_count += 1
            reports.append(
                (
                    signed / diagonal,
                    absolute / diagonal,
                    critical_absolute / max(absolute, 1.0e-300),
                    signed / zero_scale,
                    pair_count,
                )
            )

        print(f"X={limit:>5d}: atoms={len(records):>5d}, diag/N={diagonal/zero_scale:.6e}")
        for shift, report in zip(shifts, reports):
            signed_ratio, absolute_ratio, critical_share, signed_n, pair_count = report
            print(
                f"  shift={shift:.3f}: signed/diag={signed_ratio:+.6e}, "
                f"abs/diag={absolute_ratio:.6e}, critical_abs_share={critical_share:.6e}, "
                f"signed/N={signed_n:+.6e}, pairs={pair_count}"
            )
        assert all(math.isfinite(value) for report in reports for value in report[:-1])


def convolution_weights(limit: int) -> tuple[np.ndarray, np.ndarray]:
    """Return Lambda*Lambda and its prime-prime part up to ``limit``."""
    atoms = prime_power_atoms(limit)
    full = np.zeros(limit + 1, dtype=float)
    prime_part = np.zeros(limit + 1, dtype=float)
    for left in atoms:
        for right in atoms:
            product = left.n * right.n
            if product > limit:
                break
            value = left.log_prime * right.log_prime
            full[product] += value
            if left.exponent == 1 and right.exponent == 1:
                prime_part[product] += value
    return full, prime_part


def harmonic_autocorrelation(values: np.ndarray) -> float:
    support = values.size
    transform_size = 1
    while transform_size < 2 * support:
        transform_size *= 2
    transform = np.fft.rfft(values, n=transform_size)
    correlation = np.fft.irfft(transform.conjugate() * transform, n=transform_size)
    shifts = np.arange(1, support, dtype=float)
    return float(np.sum(correlation[1:support] / shifts))


def audit_semiprime_harmonic_budget() -> None:
    for limit in (2_000, 5_000, 20_000, 100_000):
        logarithm = math.log(limit)
        full, prime_part = convolution_weights(limit)
        prime_power_error = full - prime_part
        harmonic = harmonic_autocorrelation(full)
        second_moment = float(np.dot(full, full))
        error_mass = float(np.sum(prime_power_error))
        assert np.all(prime_power_error >= -1.0e-12)
        integers = np.arange(2, limit + 1, dtype=float)
        assert np.all(full[2:] <= np.log(integers) ** 2 + 1.0e-10)
        assert harmonic >= 0.0
        assert harmonic <= 0.2 * limit * logarithm**4
        assert second_moment <= limit * logarithm**3
        assert error_mass <= 3.0 * limit
        print(
            f"semiprime X={limit:>6d}: H/(X L^4)={harmonic/(limit*logarithm**4):.6e}, "
            f"M2/(X L^3)={second_moment/(limit*logarithm**3):.6e}, "
            f"pp-error/X={error_mass/limit:.6e}"
        )

def main() -> None:
    audit_ordinary_neighbor_kernel()
    audit_semiprime_harmonic_budget()
    print("ordinary-seam flat-window kernel audit passed")


if __name__ == "__main__":
    main()

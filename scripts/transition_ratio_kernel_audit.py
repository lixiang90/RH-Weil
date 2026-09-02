"""Finite audit of the transition-scale alternating ratio kernel.

The experiment keeps prime-power coefficients, the exact Gabor time lattice,
the flat compact-window overlap, and the signed Dirichlet factor.  It restricts
``ab`` to a band around ``X log X`` and reports ordinary cross terms by the
determinant depth ``|ad-bc| / log X``.  The output is exploratory only.
"""

from __future__ import annotations

import math

from alternating_ratio_cluster_audit import prime_power_atoms
from ordinary_seam_kernel_audit import (
    RatioRecord,
    cross_main_term,
    diagonal_main_term,
)


def transition_records(
    limit: int, lower_kappa: float, upper_kappa: float
) -> list[RatioRecord]:
    atoms = prime_power_atoms(limit)
    logarithm = math.log(limit)
    lower_product = limit * logarithm**lower_kappa
    upper_product = limit * logarithm**upper_kappa
    records: list[RatioRecord] = []
    for numerator in atoms:
        for denominator in atoms:
            product = numerator.n * denominator.n
            if product < lower_product or product > upper_product:
                continue
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
    records.sort(key=lambda item: item.ratio_log)
    return records


def determinant_bin(determinant: int, logarithm: float) -> str:
    scaled = abs(determinant) / logarithm
    if scaled <= 1.0:
        return "h<=L"
    if scaled <= 4.0:
        return "L<h<=4L"
    if scaled <= 16.0:
        return "4L<h<=16L"
    return "h>16L"


def audit_transition_band(limit: int) -> None:
    length = math.log(limit)
    height = 2.0 * math.pi * limit
    dimension = round(limit * length)
    records = transition_records(limit, 0.75, 1.25)
    if not records:
        raise AssertionError("empty transition band")

    diagonal = sum(diagonal_main_term(record, length, dimension) for record in records)
    if diagonal <= 0.0:
        raise AssertionError("nonpositive diagonal")

    signed_by_bin = {
        "h<=L": 0.0,
        "L<h<=4L": 0.0,
        "4L<h<=16L": 0.0,
        "h>16L": 0.0,
    }
    absolute_by_bin = {key: 0.0 for key in signed_by_bin}
    count_by_bin = {key: 0 for key in signed_by_bin}

    ratio_radius = 0.35
    for left_index, left in enumerate(records):
        for right in records[left_index + 1 :]:
            delta = right.ratio_log - left.ratio_log
            if delta > ratio_radius:
                break
            contribution, majorant, determinant = cross_main_term(
                left, right, length, height, dimension
            )
            if determinant == 0:
                continue
            label = determinant_bin(determinant, length)
            signed_by_bin[label] += contribution
            absolute_by_bin[label] += majorant
            count_by_bin[label] += 1

    signed_total = sum(signed_by_bin.values())
    absolute_total = sum(absolute_by_bin.values())
    print(
        f"X={limit:>5d}: transition-atoms={len(records):>5d}, "
        f"diag/N={diagonal/(limit*length):.6e}, "
        f"signed/diag={signed_total/diagonal:+.6e}, "
        f"abs/diag={absolute_total/diagonal:.6e}"
    )
    for label in signed_by_bin:
        print(
            f"  {label:>12s}: pairs={count_by_bin[label]:>8d}, "
            f"signed/diag={signed_by_bin[label]/diagonal:+.6e}, "
            f"abs/diag={absolute_by_bin[label]/diagonal:.6e}"
        )
    assert math.isfinite(signed_total)
    assert math.isfinite(absolute_total)
    assert absolute_total >= abs(signed_total)


def main() -> None:
    for limit in (300, 600, 1_200):
        audit_transition_band(limit)
    print("transition-scale ratio kernel audit passed")


if __name__ == "__main__":
    main()

"""Finite audit of the critical logarithmic-square local-box energy.

Note 218 reduces the next unresolved primitive ratio layer to the positive
circle-box energy at ``ab`` near ``X log(X)^2``.  This script evaluates that
specific quantity for the flat compact window.  The data are exploratory and
do not supply an asymptotic estimate.
"""

from __future__ import annotations

import math
from collections import defaultdict

from clustered_fejer_transition_audit import ARC_MULTIPLIER, circle_bin
from ordinary_seam_kernel_audit import (
    diagonal_main_term,
    flat_support,
    periodic_shifted_overlap,
)
from transition_ratio_kernel_audit import transition_records


def critical_shell(limit: int, lower_kappa: float = 1.5) -> None:
    length = math.log(limit)
    dimension = round(limit * length)
    bandwidth = 2 * dimension
    bin_count = math.ceil(2.0 * math.pi * bandwidth / ARC_MULTIPLIER)
    beta = 2.0 * math.pi / length
    records = transition_records(limit, lower_kappa, 2.0)
    blocks: defaultdict[int, list[int]] = defaultdict(list)
    for index, record in enumerate(records):
        theta = 2.0 * math.pi * record.ratio_log / length
        blocks[circle_bin(theta, bin_count)].append(index)

    diagonal = sum(diagonal_main_term(record, length, dimension) for record in records)
    local_mass = 0.0
    off_pairs = 0
    max_scaled_determinant = 0.0
    max_block_size = max((len(indices) for indices in blocks.values()), default=0)
    for indices in blocks.values():
        for left_position, left_index in enumerate(indices):
            left = records[left_index]
            left_support = flat_support(left, length)
            self_overlap = periodic_shifted_overlap(left_support, left_support, 0.0, length)
            local_mass += left.weight**2 * self_overlap / length
            for right_index in indices[left_position + 1 :]:
                right = records[right_index]
                delta = left.ratio_log - right.ratio_log
                overlap = periodic_shifted_overlap(
                    left_support,
                    flat_support(right, length),
                    delta,
                    length,
                )
                if overlap <= 1.0e-14:
                    continue
                alias = round(delta / length)
                if alias != 0:
                    raise AssertionError("critical alias survived the support-gap check")
                off_pairs += 1
                local_mass += 2.0 * left.weight * right.weight * overlap / length
                determinant = left.numerator * right.denominator - left.denominator * right.numerator
                smaller_cross_product = min(
                    left.numerator * right.denominator,
                    left.denominator * right.numerator,
                )
                max_scaled_determinant = max(
                    max_scaled_determinant,
                    abs(determinant) * limit / smaller_cross_product,
                )

    local_scale = beta**4 * dimension * local_mass
    normalization = limit * length
    assert local_scale + 1.0e-12 >= diagonal
    assert max_scaled_determinant <= 1.0
    print(
        f"X={limit:>5d}: atoms={len(records):>6d}, blocks={len(blocks):>6d}, "
        f"max-block={max_block_size:>2d}, off-pairs={off_pairs:>5d}, "
        f"diag/N={diagonal/normalization:.6e}, "
        f"local/N={local_scale/normalization:.6e}, "
        f"off/local={(local_scale-diagonal)/max(local_scale, 1.0e-300):.6e}, "
        f"max-Xdet/min={max_scaled_determinant:.6f}"
    )


def main() -> None:
    for limit in (300, 600, 1_200, 2_500, 5_000, 10_000):
        critical_shell(limit)
    print("critical logarithmic-square local-box audit passed")


if __name__ == "__main__":
    main()

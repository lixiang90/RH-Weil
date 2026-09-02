"""Finite checks for the clustered vector-valued Fejer large sieve.

The analytic result is proved in note 218.  This script only checks its
normalizations in two finite settings:

1. random nonnegative Hilbert-cone vectors with arbitrary carrier phases;
2. the actual flat-window transition atoms used by the ratio-kernel audits.

No finite computation is promoted to an asymptotic statement.
"""

from __future__ import annotations

import math
import random
from collections import defaultdict

import numpy as np

from ordinary_seam_kernel_audit import (
    diagonal_main_term,
    flat_support,
    geometric_sum,
    periodic_shifted_overlap,
)
from transition_ratio_kernel_audit import transition_records


LARGE_SIEVE_CERTIFICATE = 200.0
ARC_MULTIPLIER = 8.0


def circle_bin(theta: float, bin_count: int) -> int:
    return int(math.floor((theta % (2.0 * math.pi)) * bin_count / (2.0 * math.pi)))


def random_cone_check(seed: int, dimension: int, atom_count: int) -> float:
    rng = random.Random(seed)
    hilbert_dimension = 5
    frequencies = [rng.random() * 2.0 * math.pi for _ in range(atom_count)]
    carriers = [rng.random() * 2.0 * math.pi for _ in range(atom_count)]
    amplitudes = np.array([0.1 + rng.random() for _ in range(atom_count)])
    cone_vectors = np.array(
        [[rng.random() for _ in range(hilbert_dimension)] for _ in range(atom_count)]
    )
    vectors = amplitudes[:, None] * cone_vectors * np.exp(1j * np.array(carriers))[:, None]

    sampled_energy = 0.0
    for index in range(dimension):
        phases = np.exp(1j * index * np.array(frequencies))[:, None]
        sampled_energy += float(np.vdot(np.sum(vectors * phases, axis=0), np.sum(vectors * phases, axis=0)).real)

    bandwidth = 2 * dimension
    bin_count = math.ceil(2.0 * math.pi * bandwidth / ARC_MULTIPLIER)
    blocks: defaultdict[int, list[int]] = defaultdict(list)
    for atom_index, frequency in enumerate(frequencies):
        blocks[circle_bin(frequency, bin_count)].append(atom_index)

    local_energy = 0.0
    for indices in blocks.values():
        positive_sum = np.sum(amplitudes[indices, None] * cone_vectors[indices], axis=0)
        local_energy += float(np.dot(positive_sum, positive_sum))

    ratio = sampled_energy / (dimension * local_energy)
    assert sampled_energy >= -1.0e-10
    assert ratio <= LARGE_SIEVE_CERTIFICATE
    return ratio


def actual_transition_check(limit: int) -> tuple[int, float, float]:
    length = math.log(limit)
    height = 2.0 * math.pi * limit
    dimension = round(limit * length)
    bandwidth = 2 * dimension
    bin_count = math.ceil(2.0 * math.pi * bandwidth / ARC_MULTIPLIER)
    beta = 2.0 * math.pi / length
    records = transition_records(limit, 0.75, 1.25)

    blocks: defaultdict[int, list[int]] = defaultdict(list)
    for index, record in enumerate(records):
        theta = 2.0 * math.pi * record.ratio_log / length
        blocks[circle_bin(theta, bin_count)].append(index)

    local_mass = 0.0
    max_scaled_determinant = 0.0
    for indices in blocks.values():
        for left_position, left_index in enumerate(indices):
            left = records[left_index]
            left_support = flat_support(left, length)
            left_overlap = periodic_shifted_overlap(left_support, left_support, 0.0, length)
            local_mass += left.weight**2 * left_overlap / length
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
                    raise AssertionError("a nonzero translated overlap survived an alias bin")
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
    sampled_main = sum(diagonal_main_term(record, length, dimension) for record in records)
    for left_index, left in enumerate(records):
        left_support = flat_support(left, length)
        for right in records[left_index + 1 :]:
            delta = left.ratio_log - right.ratio_log
            overlap = periodic_shifted_overlap(
                left_support,
                flat_support(right, length),
                delta,
                length,
            )
            if overlap <= 0.0:
                continue
            response = complex(
                math.cos(height * delta), math.sin(height * delta)
            ) * geometric_sum(dimension, 2.0 * math.pi / length, delta)
            sampled_main += (
                2.0
                * beta**4
                * left.weight
                * right.weight
                * overlap
                / length
                * response.real
            )

    ratio = sampled_main / local_scale
    assert sampled_main >= -1.0e-8 * max(local_scale, 1.0)
    assert ratio <= LARGE_SIEVE_CERTIFICATE
    assert max_scaled_determinant <= 1.0
    return len(records), ratio, max_scaled_determinant


def main() -> None:
    random_ratios = [
        random_cone_check(seed, dimension, 40)
        for seed, dimension in ((7, 8), (11, 16), (29, 24))
    ]
    print("random cone ratios:", " ".join(f"{value:.6f}" for value in random_ratios))
    for limit in (120, 200, 300):
        atom_count, ratio, scaled_determinant = actual_transition_check(limit)
        print(
            f"X={limit:>3d}: atoms={atom_count:>4d}, main/local={ratio:.6f}, "
            f"max X|det|/min={scaled_determinant:.6f}"
        )
    print("clustered Fejer transition audit passed")


if __name__ == "__main__":
    main()

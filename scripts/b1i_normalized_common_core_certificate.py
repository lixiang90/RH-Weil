"""Exact normalized common-core certificate for the B1g/B1h ledgers.

For Y=8 and Y=16, theta=xi log(Y) becomes respectively 3 xi log(2) and
4 xi log(2).  Thus t=theta/log(2) places both directed certificates on one
exact rational grid.  The script intersects the verified parent cells there
and transfers their pointwise lower densities to common subcells.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256

import b1g_directed_numerator_interval_audit as b1g
import b1h_second_scale_interval_audit as b1h
from brownian_interval_certificate import rational_decimal_lower


FROZEN_COMMON_SUBCELL_COUNT = 5931
FROZEN_COMMON_RANGE_COUNT = 18
FROZEN_COMMON_RANGES = (
    (732, 1239),
    (29368, 29560),
    (39090, 39540),
    (41048, 41271),
    (57468, 57738),
    (62316, 62368),
    (64480, 64548),
    (83064, 83406),
    (92196, 92520),
    (101208, 101997),
    (110841, 111184),
    (113264, 113760),
    (121797, 122032),
    (135168, 135252),
    (136852, 137199),
    (148074, 148912),
    (151857, 151892),
    (152500, 152836),
)
FROZEN_LONGEST_COMMON_RANGE = (838, 148074, 148912)
FROZEN_COMMON_INDEX_SHA256 = (
    "80f057bb217ce9ae7f2dd12515c7ccac0f407387ab41bb7380f1632e95873703"
)
FROZEN_COMMON_BOUND_SHA256 = (
    "2e89fecb2f7c56905d73ba5efcc89e462d0c7a48f7191c1c608f0865373d86a3"
)
FROZEN_COMMON_NUMERATOR8_LOWER = Fraction(
    "0.000039220662642190066268978048"
)
FROZEN_COMMON_NUMERATOR16_LOWER = Fraction(
    "0.000116177723841047733338034809"
)


def compress(indices: set[int]) -> tuple[tuple[int, int], ...]:
    if not indices:
        return ()
    ordered = sorted(indices)
    ranges = []
    start = previous = ordered[0]
    for index in ordered[1:]:
        if index == previous + 1:
            previous = index
            continue
        ranges.append((start, previous + 1))
        start = previous = index
    ranges.append((start, previous + 1))
    return tuple(ranges)


def normalized_common_core(
    indices8: tuple[int, ...],
    bound_pairs8: tuple[tuple[int, int], ...],
    indices16: tuple[int, ...],
    bound_pairs16: tuple[tuple[int, int], ...],
) -> dict[str, object]:
    """Intersect the exact 3-to-4 normalized grids and split parent lowers."""
    bounds8 = dict(bound_pairs8)
    bounds16 = dict(bound_pairs16)
    if set(indices8) != set(bounds8) or set(indices16) != set(bounds16):
        raise ValueError("verified indices and contribution ledgers disagree")
    normalized8 = {
        subcell for index in indices8 for subcell in range(3 * index, 3 * index + 3)
    }
    normalized16 = {
        subcell for index in indices16 for subcell in range(4 * index, 4 * index + 4)
    }
    common = normalized8 & normalized16
    ranges = compress(common)
    common8 = sum(
        (Fraction(bounds8[index // 3], 3 * b1g.FIXED_SCALE) for index in common),
        Fraction(0),
    )
    common16 = sum(
        (Fraction(bounds16[index // 4], 4 * b1g.FIXED_SCALE) for index in common),
        Fraction(0),
    )
    payload = (
        "B1i-v1|theta/log2-grid=1/200|"
        + ",".join(str(index) for index in sorted(common))
    ).encode("ascii")
    bound_payload = (
        "B1i-v1|scale=10^60|"
        + ",".join(
            f"{index}:{bounds8[index // 3]}:{bounds16[index // 4]}"
            for index in sorted(common)
        )
    ).encode("ascii")
    return {
        "common": frozenset(common),
        "ranges": ranges,
        "longest": max((right - left, left, right) for left, right in ranges),
        "numerator8_lower": common8,
        "numerator16_lower": common16,
        "index_hash": sha256(payload).hexdigest(),
        "bound_hash": sha256(bound_payload).hexdigest(),
    }


def main() -> None:
    result8 = b1g.directed_numerator_certificate()
    result16 = b1h.directed_numerator_lower(b1h.build_interval_data())
    if result8["index_hash"] != b1g.FROZEN_VERIFIED_INDEX_SHA256:
        raise AssertionError("B1g extraction did not match the frozen index hash")
    if result8["bound_hash"] != b1g.FROZEN_VERIFIED_BOUND_SHA256:
        raise AssertionError("B1g extraction did not match the frozen bound hash")
    if result16["index_hash"] != b1h.FROZEN_B1H_INDEX_SHA256:
        raise AssertionError("B1h extraction did not match the frozen index hash")
    if result16["bound_hash"] != b1h.FROZEN_B1H_BOUND_SHA256:
        raise AssertionError("B1h extraction did not match the frozen bound hash")

    core = normalized_common_core(
        tuple(result8["verified_indices"]),
        tuple(result8["verified_bounds"]),
        tuple(result16["verified_indices"]),
        tuple(result16["verified_bounds"]),
    )
    common = core["common"]
    ranges = core["ranges"]
    longest = core["longest"]
    common8 = core["numerator8_lower"]
    common16 = core["numerator16_lower"]
    capture8 = common8 / b1g.FROZEN_B1F_INTENDED_DENOMINATOR_UPPER
    capture16 = common16 / b1h.FROZEN_B1H_INTENDED_DENOMINATOR_UPPER
    if len(common) != FROZEN_COMMON_SUBCELL_COUNT:
        raise AssertionError("frozen B1i common-subcell count changed")
    if len(ranges) != FROZEN_COMMON_RANGE_COUNT:
        raise AssertionError("frozen B1i common-range count changed")
    if ranges != FROZEN_COMMON_RANGES:
        raise AssertionError("frozen B1i common ranges changed")
    if longest != FROZEN_LONGEST_COMMON_RANGE:
        raise AssertionError("frozen B1i longest common range changed")
    if core["index_hash"] != FROZEN_COMMON_INDEX_SHA256:
        raise AssertionError("frozen B1i common index hash changed")
    if core["bound_hash"] != FROZEN_COMMON_BOUND_SHA256:
        raise AssertionError("frozen B1i common bound hash changed")
    if common8 < FROZEN_COMMON_NUMERATOR8_LOWER:
        raise AssertionError("frozen B1i scale-8 numerator lower is too large")
    if common16 < FROZEN_COMMON_NUMERATOR16_LOWER:
        raise AssertionError("frozen B1i scale-16 numerator lower is too large")
    if min(capture8, capture16) <= Fraction(1, 20):
        raise AssertionError("normalized common core did not clear 1/20")
    print(f"common_subcell_count={len(common)}")
    print(f"common_range_count={len(ranges)}")
    print(
        "common_ranges="
        + ",".join(f"[{left}/200,{right}/200]" for left, right in ranges)
    )
    print(
        "common_normalized_width=",
        rational_decimal_lower(len(common) * Fraction(1, 200), 12),
        sep="",
    )
    print(
        f"longest_common_range=[{longest[1]}/200,{longest[2]}/200],"
        f" width={longest[0]}/200"
    )
    print(f"common_index_sha256={core['index_hash']}")
    print(f"common_bound_sha256={core['bound_hash']}")
    print(
        "common_numerator8_lower=",
        rational_decimal_lower(common8, 30),
        sep="",
    )
    print(
        "common_capture8_lower=",
        rational_decimal_lower(
            capture8, 18
        ),
        sep="",
    )
    print(
        "common_numerator16_lower=",
        rational_decimal_lower(common16, 30),
        sep="",
    )
    print(
        "common_capture16_lower=",
        rational_decimal_lower(
            capture16, 18
        ),
        sep="",
    )
    print(
        "common_overlap_delta_lower=",
        rational_decimal_lower(Fraction(1, 85), 18),
        sep="",
    )
    print(
        "common_diagonal_to_full_lower=",
        rational_decimal_lower(Fraction(85, 83), 18),
        sep="",
    )
    print("B1i normalized common-core certificate passed")
    print("[scope] two finite scales only; scale-uniform overlap and RH remain open")


if __name__ == "__main__":
    main()

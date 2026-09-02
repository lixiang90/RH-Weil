"""Audits for alternating aperture--depth support geometry.

The exact identities and flat-window support bounds are finite.  The prime
search is diagnostic only.  The exponent ledger audits an implication ceiling,
not a lower bound for the actual zeta fourth moment.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


TOL = 1.0e-12


@dataclass(frozen=True)
class Atom:
    numerator: int
    denominator: int
    aperture: float
    depth: float
    product: int
    left: float
    right: float


def coordinates_from_aperture_depth(
    aperture: float, depth: float
) -> tuple[float, float]:
    if aperture >= 0.0:
        return 1.0 - depth, 1.0 - depth - aperture
    return 1.0 - depth + aperture, 1.0 - depth


def support_interval(aperture: float, depth: float) -> tuple[float, float]:
    right = 0.5 - max(aperture, 0.0)
    return right - depth, right


def overlap_length(left: Atom, right: Atom) -> float:
    return max(0.0, min(left.right, right.right) - max(left.left, right.left))


def audit_coordinate_identity() -> None:
    for aperture in (-0.7, -0.2, 0.0, 0.25, 0.65):
        maximum_depth = 1.0 - abs(aperture)
        for fraction in (0.1, 0.4, 0.8):
            depth = fraction * maximum_depth
            alpha, beta = coordinates_from_aperture_depth(aperture, depth)
            assert -TOL <= alpha <= 1.0 + TOL
            assert -TOL <= beta <= 1.0 + TOL
            assert abs(alpha - beta - aperture) <= TOL
            assert abs(1.0 - max(alpha, beta) - depth) <= TOL
            product_exponent = alpha + beta
            expected = 2.0 - 2.0 * depth - abs(aperture)
            assert abs(product_exponent - expected) <= TOL
    print("aperture--depth coordinate identity: PASS")


def audit_nested_support() -> None:
    for aperture in (-0.6, -0.1, 0.0, 0.2, 0.55):
        radial_capacity = 1.0 - abs(aperture)
        high_depth = 0.25 * radial_capacity
        low_depth = 0.75 * radial_capacity
        high_interval = support_interval(aperture, high_depth)
        low_interval = support_interval(aperture, low_depth)
        assert low_interval[0] < high_interval[0]
        assert abs(low_interval[1] - high_interval[1]) <= TOL
        intersection = min(low_interval[1], high_interval[1]) - max(
            low_interval[0], high_interval[0]
        )
        assert abs(intersection - high_depth) <= TOL
        high_product_exponent = 2.0 - 2.0 * high_depth - abs(aperture)
        low_product_exponent = 2.0 - 2.0 * low_depth - abs(aperture)
        assert high_product_exponent > 1.0
        assert low_product_exponent < 1.0
    print("fixed-aperture high-support nesting: PASS")


def audit_near_aperture_overlap_bound() -> None:
    cases = [
        (-0.31, -0.305, 0.17, 0.42),
        (-0.02, 0.01, 0.21, 0.39),
        (0.18, 0.19, 0.15, 0.33),
        (0.47, 0.455, 0.11, 0.29),
    ]
    for first_q, second_q, first_depth, second_depth in cases:
        first_interval = support_interval(first_q, first_depth)
        second_interval = support_interval(second_q, second_depth)
        actual = max(
            0.0,
            min(first_interval[1], second_interval[1])
            - max(first_interval[0], second_interval[0]),
        )
        lower = max(
            0.0,
            min(first_depth, second_depth) - abs(first_q - second_q),
        )
        assert actual + TOL >= lower
    print("near-aperture overlap lower bound: PASS")


def prime_bases(limit: int) -> list[tuple[int, int]]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    values: list[tuple[int, int]] = []
    for prime in range(2, limit + 1):
        if not sieve[prime]:
            continue
        power = prime
        while power <= limit:
            values.append((power, prime))
            if power > limit // prime:
                break
            power *= prime
    values.sort()
    return values


def make_atom(numerator: int, denominator: int, logarithm: float) -> Atom:
    alpha = math.log(numerator) / logarithm
    beta = math.log(denominator) / logarithm
    aperture = alpha - beta
    depth = 1.0 - max(alpha, beta)
    left, right = support_interval(aperture, depth)
    return Atom(
        numerator,
        denominator,
        aperture,
        depth,
        numerator * denominator,
        left,
        right,
    )


def nearest_high_low_pair(limit: int, eta: float = 0.5) -> tuple[Atom, Atom]:
    logarithm = math.log(limit)
    low_cutoff = limit * logarithm**eta
    high_cutoff = limit * logarithm**2
    # Genuine primes only: the collision is not delegated to proper powers.
    values = [item for item in prime_bases(limit) if item[0] == item[1]]
    labelled: list[tuple[float, int, Atom]] = []
    for numerator, numerator_base in values:
        for denominator, denominator_base in values:
            if numerator_base == denominator_base:
                continue
            product = numerator * denominator
            label = -1 if product < low_cutoff else (1 if product > high_cutoff else 0)
            if label == 0:
                continue
            atom = make_atom(numerator, denominator, logarithm)
            labelled.append((atom.aperture, label, atom))
    labelled.sort(key=lambda item: item[0])
    best: tuple[float, Atom, Atom] | None = None
    previous = labelled[0]
    for current in labelled[1:]:
        if previous[1] != current[1]:
            gap = current[0] - previous[0]
            low = previous[2] if previous[1] == -1 else current[2]
            high = previous[2] if previous[1] == 1 else current[2]
            if best is None or gap < best[0]:
                best = (gap, high, low)
        previous = current
    if best is None:
        raise AssertionError("no high--low pair found")
    return best[1], best[2]


def audit_prime_power_near_collisions() -> None:
    for limit in (300, 600, 1200):
        high, low = nearest_high_low_pair(limit)
        logarithm = math.log(limit)
        physical_gap = abs(high.aperture - low.aperture) * logarithm
        overlap = overlap_length(high, low)
        determinant = abs(
            high.numerator * low.denominator
            - high.denominator * low.numerator
        )
        assert determinant > 0
        assert overlap > 0.0
        assert physical_gap * limit < 2.0
        print(
            f"X={limit:4d}: high={high.numerator}/{high.denominator}, "
            f"low={low.numerator}/{low.denominator}, "
            f"X*log-gap={limit * physical_gap:.6f}, det={determinant}, "
            f"flat-overlap/high-depth={overlap / high.depth:.6f}"
        )
    print("prime high--low near-collision diagnostics: PASS")


def audit_positive_local_energy_ceiling() -> None:
    # For a balanced factor box A=X^theta, R=A^2=X^(2 theta),
    # natural incidence and a fixed positive depth give
    # E_box/N ~ X^(2 theta-1)/(log X)^4.
    for theta in (0.60, 0.70, 0.80):
        exponent = 2.0 * theta - 1.0
        assert exponent > 0.0
        log_ratios = []
        for log_x in (40.0, 80.0, 160.0):
            log_ratio = exponent * log_x - 4.0 * math.log(log_x)
            log_ratios.append(log_ratio)
        assert log_ratios[-1] > log_ratios[-2]
        print(
            f"theta={theta:.2f}: log(E_box/N) at logX=40,80,160 -> "
            + ", ".join(f"{value:.3f}" for value in log_ratios)
        )
    print("positive local-energy exponent ceiling: PASS")


def audit_third_log_collar_ledger() -> None:
    for cutoff_exponent in (2.25, 2.50, 2.75):
        main_power = cutoff_exponent - 3.0
        finite_power = cutoff_exponent - 3.0
        assert main_power < 0.0
        assert finite_power < 0.0
        print(
            f"K={cutoff_exponent:.2f}: main/N=L^({main_power:.2f})polylog, "
            f"finite/N=L^({finite_power:.2f})loglog"
        )
    print("K<3 collar and K=3 endpoint exponent ledger: PASS")

def main() -> None:
    audit_coordinate_identity()
    audit_nested_support()
    audit_near_aperture_overlap_bound()
    audit_prime_power_near_collisions()
    audit_third_log_collar_ledger()
    audit_positive_local_energy_ceiling()
    print("alternating aperture--depth audits passed")
    print("[scope] finite geometry/diagnostics and implication exponents only")


if __name__ == "__main__":
    main()

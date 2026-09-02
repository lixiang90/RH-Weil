"""Independent cyclic reconstruction of the centered fourth constant.

The paired 2+2 term is integrated from all twelve raw signed pairing paths,
without inserting the pre-grouped 4(A_+ + A_- + B) formula.  The script also
reconstructs the 8/4 deterministic mixed multiplicities.  Numerical agreement
checks normalization only; it does not estimate unpaired prime correlations.
"""

from __future__ import annotations

import itertools
import math
from collections import Counter

import numpy as np
from numpy.polynomial.legendre import leggauss


Point = tuple[int, int]
Path = tuple[Point, Point, Point, Point]


def paired_paths() -> list[Path]:
    paths: list[Path] = []
    for signs in sorted(set(itertools.permutations((1, 1, -1, -1)))):
        plus = [index for index, sign in enumerate(signs) if sign == 1]
        minus = [index for index, sign in enumerate(signs) if sign == -1]
        for matching in itertools.permutations((0, 1)):
            increments: list[Point | None] = [None] * 4
            increments[plus[0]] = (1, 0)
            increments[plus[1]] = (0, 1)
            for minus_index, plus_index in zip(minus, matching):
                source = increments[plus[plus_index]]
                assert source is not None
                increments[minus_index] = (-source[0], -source[1])

            current = (0, 0)
            path: list[Point] = []
            for increment in increments:
                assert increment is not None
                path.append(current)
                current = (current[0] + increment[0], current[1] + increment[1])
            assert current == (0, 0)
            paths.append(tuple(path))  # type: ignore[arg-type]
    assert len(paths) == 12
    return paths


def canonical(path: Path) -> tuple[Point, ...]:
    candidates: list[tuple[Point, ...]] = []
    for swap in (False, True):
        transformed = [(y, x) if swap else (x, y) for x, y in path]
        for sign in (-1, 1):
            signed = [(sign * x, sign * y) for x, y in transformed]
            for origin in signed:
                shifted = tuple(
                    sorted((x - origin[0], y - origin[1]) for x, y in signed)
                )
                candidates.append(shifted)
    return min(candidates)


TEMPLATES = {
    canonical(((0, 0), (0, 0), (1, 0), (0, 1))): "A_plus",
    canonical(((0, 0), (0, 0), (1, 0), (0, -1))): "A_minus",
    canonical(((0, 0), (1, 0), (0, 1), (1, 1))): "B",
}


def check_path_multiplicities(paths: list[Path]) -> None:
    classes = Counter(TEMPLATES[canonical(path)] for path in paths)
    assert classes == Counter({"A_plus": 4, "A_minus": 4, "B": 4})


def psi(kind: str, values: np.ndarray) -> np.ndarray:
    inside = np.abs(values) <= 0.5 + 1e-14
    result = np.zeros_like(values)
    if kind == "flat":
        result[inside] = 1.0
    elif kind == "mt":
        result[inside] = np.cos(math.sqrt(2.0) * values[inside])
    else:
        raise ValueError(kind)
    return result


def path_overlap(kind: str, path: Path, r: float, s: float, order: int) -> float:
    shifts = [x * r + y * s for x, y in path]
    lower = max(-0.5 - shift for shift in shifts)
    upper = min(0.5 - shift for shift in shifts)
    if lower >= upper:
        return 0.0
    nodes, weights = leggauss(order)
    u = 0.5 * (lower + upper) + 0.5 * (upper - lower) * nodes
    product_values = np.ones_like(u)
    for shift in shifts:
        product_values *= psi(kind, u + shift)
    return float(0.5 * (upper - lower) * np.dot(weights, product_values))


def paired_constant(kind: str, paths: list[Path], order: int) -> float:
    nodes, weights = leggauss(order)
    unit_nodes = 0.5 * (nodes + 1.0)
    unit_weights = 0.5 * weights
    window_nodes = 0.5 * nodes
    window_weights = 0.5 * weights
    a = float(np.dot(window_weights, psi(kind, window_nodes)))
    triangles = (
        ((0.0, 0.0), (1.0, 0.0), (0.5, 0.5)),
        ((0.0, 0.0), (0.0, 1.0), (0.5, 0.5)),
        ((1.0, 1.0), (1.0, 0.0), (0.5, 0.5)),
        ((1.0, 1.0), (0.0, 1.0), (0.5, 0.5)),
    )
    total = 0.0
    for vertex0, vertex1, vertex2 in triangles:
        determinant = abs(
            (vertex1[0] - vertex0[0]) * (vertex2[1] - vertex0[1])
            - (vertex1[1] - vertex0[1]) * (vertex2[0] - vertex0[0])
        )
        for first, first_weight in zip(unit_nodes, unit_weights):
            for second, second_weight in zip(unit_nodes, unit_weights):
                r = (
                    vertex0[0]
                    + first * (vertex1[0] - vertex0[0])
                    + (1.0 - first) * second * (vertex2[0] - vertex0[0])
                )
                s = (
                    vertex0[1]
                    + first * (vertex1[1] - vertex0[1])
                    + (1.0 - first) * second * (vertex2[1] - vertex0[1])
                )
                jacobian = determinant * (1.0 - first)
                raw_path_sum = sum(
                    path_overlap(kind, path, r, s, order) for path in paths
                )
                total += (
                    first_weight
                    * second_weight
                    * jacobian
                    * r
                    * s
                    * raw_path_sum
                )
    return total / a**4


def deterministic_constants(kind: str, order: int) -> tuple[float, float]:
    nodes, weights = leggauss(order)
    v = 0.5 * nodes
    v_weights = 0.5 * weights
    r_nodes = 0.5 * (nodes + 1.0)
    r_weights = 0.5 * weights
    a = float(np.dot(v_weights, psi(kind, v)))
    s_v = psi(kind, v) / a - 1.0
    d_zero = float(np.dot(v_weights, s_v**4))

    placements = list(itertools.combinations(range(4), 2))
    adjacent = sum(
        1
        for left, right in placements
        if (right - left) % 4 in (1, 3) or {left, right} == {0, 3}
    )
    alternating = len(placements) - adjacent
    assert (adjacent, alternating) == (4, 2)
    adjacent_orientations = 2 * adjacent
    alternating_orientations = 2 * alternating
    assert (adjacent_orientations, alternating_orientations) == (8, 4)

    c1_values: list[float] = []
    c2_values: list[float] = []
    for r in r_nodes:
        overlap_v = 0.5 * r + 0.5 * (1.0 - r) * nodes
        overlap_weights = 0.5 * (1.0 - r) * weights
        psi_v = psi(kind, overlap_v)
        reflected = psi(kind, r - overlap_v)
        s_current = psi_v / a - 1.0
        s_shifted = psi(kind, overlap_v - r) / a - 1.0
        q_r = psi_v * reflected
        c1_values.append(float(np.dot(overlap_weights, s_current**2 * q_r)))
        c2_values.append(float(np.dot(overlap_weights, s_current * s_shifted * q_r)))
    mixed = float(
        np.dot(
            r_weights,
            r_nodes
            * (
                adjacent_orientations * np.array(c1_values)
                + alternating_orientations * np.array(c2_values)
            ),
        )
        / a**2
    )
    return d_zero, mixed


def main() -> None:
    paths = paired_paths()
    check_path_multiplicities(paths)

    flat_paired = paired_constant("flat", paths, 16)
    assert abs(flat_paired - 4.0 / 15.0) < 2e-12

    mt_values = [paired_constant("mt", paths, order) for order in (12, 16, 20)]
    assert abs(mt_values[-1] - mt_values[-2]) < 2e-10
    mt_paired = mt_values[-1]
    assert abs(mt_paired - 0.244589382034426) < 3e-10

    d_zero, d_mixed = deterministic_constants("mt", 120)
    centered_fourth = d_zero + d_mixed + mt_paired
    assert abs(d_zero - 0.000078787511) < 2e-9
    assert abs(d_mixed - 0.007840799168) < 3e-8
    assert abs(centered_fourth - 0.252508968714) < 4e-8

    print("raw paired paths: A_plus=4, A_minus=4, B=4")
    print("mixed placements: adjacent orientations=8, alternating orientations=4")
    print(
        "MT constants: "
        f"D0={d_zero:.12f}, Dmix={d_mixed:.12f}, "
        f"D22={mt_paired:.12f}, total={centered_fourth:.12f}"
    )
    print("cyclic fourth-constant reconstruction: PASS")


if __name__ == "__main__":
    main()

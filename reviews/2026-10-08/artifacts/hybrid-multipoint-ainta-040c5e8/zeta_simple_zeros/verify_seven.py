"""Computer-assisted certificate for the 7-point pressure inequality."""

from __future__ import annotations

import itertools
import math
import time
from typing import Iterable, List, Optional, Sequence, Tuple

from flint import arb, fmpq

from .kernel import (
    RangeMinimum,
    build_kernel_table,
    build_second_derivative_lower_table,
    kernel_constants,
    squared_kernel_derivatives,
    table_sha256,
)
from .report import VerificationReport
from .rounding import down_add, down_mul, down_ratio, up_ratio


GRID = 4_000
PRECISION_BITS = 128
TARGET_NUMERATOR = 19
TARGET_DENOMINATOR = 5_000
PRESSURE_DENOMINATOR = 3_000
PRESSURE_CUTOFF_CELLS = 45_600

# c_s = 2/(7-s), where s is the number of gaps crossed by a pair.
COEFFICIENTS = {
    1: down_ratio(1, 3),
    2: down_ratio(2, 5),
    3: down_ratio(1, 2),
    4: down_ratio(2, 3),
    5: 1.0,
    6: 2.0,
}
COEFFICIENTS_UP = {
    1: up_ratio(1, 3),
    2: up_ratio(2, 5),
    3: up_ratio(1, 2),
    4: up_ratio(2, 3),
    5: 1.0,
    6: 2.0,
}
COEFFICIENT_RATIONALS = {
    1: fmpq(1, 3),
    2: fmpq(2, 5),
    3: fmpq(1, 2),
    4: fmpq(2, 3),
    5: fmpq(1),
    6: fmpq(2),
}

CellRange = Tuple[int, int]
SevenBox = Tuple[CellRange, CellRange, CellRange, CellRange, CellRange, CellRange]


def _components(indices: Iterable[int]) -> List[CellRange]:
    result: List[List[int]] = []
    for index in indices:
        if not result or index > result[-1][1] + 1:
            result.append([index, index])
        else:
            result[-1][1] = index
    return [(left, right) for left, right in result]


def verify_seven(progress_every: int = 0) -> VerificationReport:
    r"""Prove F6(g1,...,g6) >= 19/5000 for all nonnegative gaps.

    Arb first encloses k(x)^2 on a fixed 1/4000 grid. The second phase uses
    only lower bounds, outward-rounded binary64 arithmetic, range minima, and
    exhaustive subdivision of the remaining six-dimensional cell boxes.
    """

    started = time.perf_counter()
    cell_count = PRESSURE_CUTOFF_CELLS + 8
    table = build_kernel_table(GRID, cell_count, PRECISION_BITS)
    ranges = RangeMinimum(table)
    second_table = build_second_derivative_lower_table(
        GRID, cell_count, start_index=3_800, precision=PRECISION_BITS
    )
    second_ranges = RangeMinimum(second_table)
    constants = kernel_constants()
    target_upper = up_ratio(TARGET_NUMERATOR, TARGET_DENOMINATOR)

    def kernel_min(left: int, right: int) -> float:
        # If the interval extends past the pressure cutoff, zero is still a
        # rigorous lower bound for the nonnegative function w=k^2.
        if right >= ranges.length:
            return 0.0
        return ranges.query(left, right)

    def second_derivative_min(left: int, right: int) -> float:
        if right >= second_ranges.length:
            return float("-inf")
        return second_ranges.query(left, right)

    # U(g)=g/3000+w(g)/3 is a term of F6. Any cell on which U already
    # exceeds the target can be removed before forming 6D boxes.
    surviving_cells: List[int] = []
    for index in range(PRESSURE_CUTOFF_CELLS):
        one_body = down_ratio(index, GRID * PRESSURE_DENOMINATOR)
        one_body = down_add(one_body, down_mul(COEFFICIENTS[1], table[index]))
        if one_body < target_upper:
            surviving_cells.append(index)
    components = _components(surviving_cells)

    stack: List[Tuple[SevenBox, int]] = [
        (tuple(parts), 0)  # type: ignore[arg-type]
        for parts in itertools.product(components, repeat=6)
    ]
    initial_boxes = len(stack)
    nodes = pruned = splits = maximum_depth = 0
    pressure_pruned = interval_pruned = 0
    tangent_pruned = 0

    def box_lower(box: SevenBox) -> float:
        lows = [part[0] for part in box]
        highs = [part[1] for part in box]
        low_prefix = [0]
        high_prefix = [0]
        for low, high in zip(lows, highs):
            low_prefix.append(low_prefix[-1] + low)
            high_prefix.append(high_prefix[-1] + high)

        result = down_ratio(low_prefix[-1], GRID * PRESSURE_DENOMINATOR)
        for span in range(1, 7):
            coefficient = COEFFICIENTS[span]
            for start in range(7 - span):
                left = low_prefix[start + span] - low_prefix[start]
                # A sum of `span` closed cells has this inclusive cell range.
                right = (
                    high_prefix[start + span] - high_prefix[start] + span - 1
                )
                result = down_add(
                    result,
                    down_mul(coefficient, kernel_min(left, right)),
                )
        return result

    def coefficient_times_signed_lower(span: int, lower: float) -> float:
        if lower == float("-inf"):
            return lower
        coefficient = COEFFICIENTS[span] if lower >= 0.0 else COEFFICIENTS_UP[span]
        # Multiplication is rounded to nearest first, then widened down.
        return math.nextafter(coefficient * lower, -math.inf)

    def float_ldl_is_positive(matrix: List[List[float]]) -> bool:
        """Cheap heuristic; success is rechecked with Arb below."""

        lower = [[0.0] * 6 for _ in range(6)]
        diagonal = [0.0] * 6
        for column in range(6):
            pivot = matrix[column][column]
            for previous in range(column):
                pivot -= (
                    lower[column][previous]
                    * lower[column][previous]
                    * diagonal[previous]
                )
            if pivot <= 1e-12:
                return False
            diagonal[column] = pivot
            lower[column][column] = 1.0
            for row in range(column + 1, 6):
                value = matrix[row][column]
                for previous in range(column):
                    value -= (
                        lower[row][previous]
                        * lower[column][previous]
                        * diagonal[previous]
                    )
                lower[row][column] = value / pivot
        return True

    def exact_float(value: float) -> arb:
        numerator, denominator = value.as_integer_ratio()
        return arb(fmpq(numerator, denominator))

    def arb_ldl_is_positive(terms: Sequence[Tuple[int, int, float]]) -> bool:
        """Prove the rational lower-Hessian matrix positive definite."""

        matrix = [[arb(0) for _ in range(6)] for _ in range(6)]
        for start, span, coefficient in terms:
            exact = exact_float(coefficient)
            for row in range(start, start + span):
                for column in range(start, start + span):
                    matrix[row][column] += exact

        lower = [[arb(0) for _ in range(6)] for _ in range(6)]
        diagonal = [arb(0) for _ in range(6)]
        for column in range(6):
            lower[column][column] = arb(1)
            pivot = matrix[column][column]
            for previous in range(column):
                pivot -= (
                    lower[column][previous]
                    * lower[column][previous]
                    * diagonal[previous]
                )
            if not (pivot > 0):
                return False
            diagonal[column] = pivot
            for row in range(column + 1, 6):
                value = matrix[row][column]
                for previous in range(column):
                    value -= (
                        lower[row][previous]
                        * lower[column][previous]
                        * diagonal[previous]
                    )
                lower[row][column] = value / pivot
        return True

    def convex_tangent_lower(box: SevenBox) -> Optional[arb]:
        """Return a rigorous tangent lower bound when convexity is certified."""

        low_prefix = [0]
        high_prefix = [0]
        for low, high in box:
            low_prefix.append(low_prefix[-1] + low)
            high_prefix.append(high_prefix[-1] + high)

        terms: List[Tuple[int, int, float]] = []
        heuristic = [[0.0] * 6 for _ in range(6)]
        for span in range(1, 7):
            for start in range(7 - span):
                left = low_prefix[start + span] - low_prefix[start]
                right = (
                    high_prefix[start + span] - high_prefix[start] + span - 1
                )
                second_lower = second_derivative_min(left, right)
                scalar = coefficient_times_signed_lower(span, second_lower)
                if scalar == float("-inf"):
                    return None
                terms.append((start, span, scalar))
                for row in range(start, start + span):
                    for column in range(start, start + span):
                        heuristic[row][column] += scalar

        if not float_ldl_is_positive(heuristic):
            return None
        if not arb_ldl_is_positive(terms):
            return None

        midpoints = [fmpq(low + high + 1, 2 * GRID) for low, high in box]
        radii = [fmpq(high - low + 1, 2 * GRID) for low, high in box]
        value = sum((arb(point) for point in midpoints), arb(0)) / PRESSURE_DENOMINATOR
        gradient = [arb(fmpq(1, PRESSURE_DENOMINATOR)) for _ in range(6)]

        for span in range(1, 7):
            coefficient = arb(COEFFICIENT_RATIONALS[span])
            for start in range(7 - span):
                point = sum(midpoints[start : start + span], fmpq(0))
                potential, derivative, _ = squared_kernel_derivatives(
                    arb(point), constants
                )
                value += coefficient * potential
                for coordinate in range(start, start + span):
                    gradient[coordinate] += coefficient * derivative

        lower = value
        for derivative, radius in zip(gradient, radii):
            lower -= derivative.abs_upper() * arb(radius)
        return lower

    while stack:
        box, depth = stack.pop()
        nodes += 1
        maximum_depth = max(maximum_depth, depth)

        if sum(part[0] for part in box) >= PRESSURE_CUTOFF_CELLS:
            pruned += 1
            pressure_pruned += 1
            continue

        lower = box_lower(box)
        if lower >= target_upper:
            pruned += 1
            interval_pruned += 1
            continue

        tangent_lower = convex_tangent_lower(box)
        if tangent_lower is not None and tangent_lower >= arb(
            fmpq(TARGET_NUMERATOR, TARGET_DENOMINATOR)
        ):
            pruned += 1
            tangent_pruned += 1
            continue

        widths = [right - left for left, right in box]
        if max(widths) == 0:
            raise RuntimeError(
                "7-point certificate failed at a terminal cell: "
                f"box={box}, lower={lower.hex()}"
            )

        splits += 1
        coordinate = max(range(6), key=widths.__getitem__)
        left, right = box[coordinate]
        midpoint = (left + right) // 2
        lower_half = list(box)
        upper_half = list(box)
        lower_half[coordinate] = (left, midpoint)
        upper_half[coordinate] = (midpoint + 1, right)
        stack.append((tuple(lower_half), depth + 1))  # type: ignore[arg-type]
        stack.append((tuple(upper_half), depth + 1))  # type: ignore[arg-type]

        if progress_every and nodes % progress_every == 0:
            print(f"seven: nodes={nodes} pending={len(stack)} depth={maximum_depth}")

    elapsed = time.perf_counter() - started
    component_text = ";".join(f"[{a},{b}]" for a, b in components)
    return VerificationReport(
        certificate="seven-point",
        verified=True,
        target="F6 >= 19/5000",
        grid=GRID,
        precision_bits=PRECISION_BITS,
        kernel_table_sha256=table_sha256(table),
        nodes=nodes,
        pruned=pruned,
        splits=splits,
        maximum_depth=maximum_depth,
        initial_boxes=initial_boxes,
        elapsed_seconds=elapsed,
        details={
            "pressure_pruned": pressure_pruned,
            "interval_pruned": interval_pruned,
            "tangent_pruned": tangent_pruned,
            "second_derivative_table_sha256": table_sha256(second_table),
            "surviving_gap_components_cells": component_text,
            "surviving_gap_components_count": len(components),
        },
    )

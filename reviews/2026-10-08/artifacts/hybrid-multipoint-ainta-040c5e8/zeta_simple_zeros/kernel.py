"""Arb enclosures for the normalized Montgomery-Taylor overlap kernel."""

from __future__ import annotations

import hashlib
import math
import struct
from dataclasses import dataclass
from typing import List, Sequence

from flint import arb, ctx, fmpq

from .rounding import down_mul


def configure_arb(precision: int = 128) -> None:
    """Set the working precision used to produce cell enclosures."""

    if precision < 80:
        raise ValueError("at least 80 bits are required")
    ctx.prec = precision


@dataclass(frozen=True)
class KernelConstants:
    sqrt_two: arb
    inv_sqrt_two: arb
    pi: arb
    k_zero: arb


def kernel_constants() -> KernelConstants:
    sqrt_two = arb(2).sqrt()
    inv_sqrt_two = 1 / sqrt_two
    return KernelConstants(
        sqrt_two=sqrt_two,
        inv_sqrt_two=inv_sqrt_two,
        pi=arb.pi(),
        k_zero=sqrt_two * inv_sqrt_two.sin(),
    )


def normalized_kernel(x: arb, constants: KernelConstants | None = None) -> arb:
    r"""Enclose k(x) = K(x)/K(0) using the entire sinc representation.

    Here K(x) = integral_{-1/2}^{1/2} cos(sqrt(2)t) cos(2 pi x t) dt.
    The sinc form has no removable-singularity special cases.
    """

    c = constants or kernel_constants()
    frequency = 2 * c.pi * x
    left = ((c.sqrt_two - frequency) / 2).sinc()
    right = ((c.sqrt_two + frequency) / 2).sinc()
    return ((left + right) / 2) / c.k_zero


def squared_kernel_derivatives(
    x: arb, constants: KernelConstants | None = None
) -> tuple[arb, arb, arb]:
    r"""Return enclosures for w(x)=k(x)^2 and its first two derivatives.

    This formula divides by z^3 and is therefore used only for x >= 0.95 in
    the 7-point verifier; the entire sinc formula remains the general kernel
    evaluator.
    """

    c = constants or kernel_constants()
    z_left = c.pi * x - c.inv_sqrt_two
    z_right = c.pi * x + c.inv_sqrt_two

    def sinc_derivatives(z: arb) -> tuple[arb, arb, arb]:
        sine = z.sin()
        cosine = z.cos()
        z_squared = z * z
        value = sine / z
        first = (z * cosine - sine) / z_squared
        second = ((2 - z_squared) * sine - 2 * z * cosine) / (z_squared * z)
        return value, first, second

    left, left_prime, left_second = sinc_derivatives(z_left)
    right, right_prime, right_second = sinc_derivatives(z_right)
    raw = (left + right) / 2
    raw_prime = c.pi * (left_prime + right_prime) / 2
    raw_second = c.pi * c.pi * (left_second + right_second) / 2
    normalization_squared = c.k_zero * c.k_zero

    value = raw * raw / normalization_squared
    first = 2 * raw * raw_prime / normalization_squared
    second = 2 * (raw_prime * raw_prime + raw * raw_second) / normalization_squared
    return value, first, second


def closed_cell(index: int, grid: int) -> arb:
    """Return the exact ball [index/grid, (index+1)/grid]."""

    if index < 0 or grid <= 0:
        raise ValueError("index must be nonnegative and grid must be positive")
    return arb(fmpq(2 * index + 1, 2 * grid), fmpq(1, 2 * grid))


def _arb_nonnegative_lower_to_float(value: arb) -> float:
    """Convert an Arb nonnegative lower endpoint to a widened binary64 bound."""

    candidate = float(value.lower())
    if candidate <= 0.0:
        return 0.0
    return math.nextafter(candidate, -math.inf)


def arb_lower_to_float(value: arb) -> float:
    """A widened binary64 lower bound for a signed Arb enclosure."""

    return math.nextafter(float(value.lower()), -math.inf)


def squared_kernel_cell_lower(
    index: int, grid: int, constants: KernelConstants | None = None
) -> float:
    """Rigorous binary64 lower bound for min k(x)^2 on one closed cell."""

    enclosure = normalized_kernel(closed_cell(index, grid), constants)
    absolute_lower = _arb_nonnegative_lower_to_float(enclosure.abs_lower())
    return down_mul(absolute_lower, absolute_lower)


def build_kernel_table(grid: int, cell_count: int, precision: int = 128) -> List[float]:
    """Build rigorous lower bounds for k^2 on consecutive grid cells."""

    configure_arb(precision)
    constants = kernel_constants()
    return [squared_kernel_cell_lower(i, grid, constants) for i in range(cell_count)]


def build_second_derivative_lower_table(
    grid: int, cell_count: int, start_index: int, precision: int = 128
) -> List[float]:
    """Build lower bounds for w'' on cells safely away from the removable pole."""

    configure_arb(precision)
    constants = kernel_constants()
    values = [-math.inf] * cell_count
    for index in range(start_index, cell_count):
        _, _, second = squared_kernel_derivatives(closed_cell(index, grid), constants)
        values[index] = arb_lower_to_float(second.lower())
    return values


def table_sha256(values: Sequence[float]) -> str:
    """Hash the exact binary64 table representation."""

    digest = hashlib.sha256()
    for value in values:
        digest.update(struct.pack(">d", value))
    return digest.hexdigest()


class RangeMinimum:
    """O(1) idempotent sparse-table range-minimum queries."""

    def __init__(self, values: Sequence[float]):
        if not values:
            raise ValueError("values must be nonempty")
        self._length = len(values)
        levels: List[List[float]] = [list(values)]
        width = 1
        while 2 * width <= self._length:
            previous = levels[-1]
            half = width
            width *= 2
            levels.append(
                [
                    min(previous[i], previous[i + half])
                    for i in range(self._length - width + 1)
                ]
            )
        self._levels = levels

    @property
    def length(self) -> int:
        return self._length

    def query(self, left: int, right: int) -> float:
        """Return min(values[left:right+1])."""

        if left < 0 or right < left or right >= self._length:
            raise IndexError((left, right, self._length))
        level = (right - left + 1).bit_length() - 1
        width = 1 << level
        row = self._levels[level]
        return min(row[left], row[right - width + 1])

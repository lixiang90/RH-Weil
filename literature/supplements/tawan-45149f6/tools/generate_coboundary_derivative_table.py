#!/usr/bin/env python3
"""Generate a directed-MPFR CWD2 derivative table for verify_coboundary.cpp.

The compact CWK2 generator already provides the MPFR interval primitives.  This
entry point reuses them and evaluates the analytic sinc derivatives directly;
it does not use numerical differentiation or the unavailable derivative ZIP.
"""
from __future__ import annotations

import argparse
import ctypes
import ctypes.util
import hashlib
import math
import os
import struct
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

# The archived CWK2 module defaults to the Linux soname.  Select an installed
# Windows DLL before importing it so the same source works on this machine.
if os.name == "nt":
    _dll = os.environ.get("ZETA_MPFR_DLL", r"C:\Strawberry\c\bin\libmpfr-6.dll")
    if Path(_dll).is_file():
        ctypes.util.find_library = lambda _name: _dll

import generate_joint_kernel_table as base

MPFR_RNDN = base.MPFR_RNDN
MPFR_RNDU = base.MPFR_RNDU
MPFR_RNDD = base.MPFR_RNDD
Num = base.Num
Interval = base.Interval
add = base.add
subtract = base.subtract
multiply = base.multiply
divide = base.divide
divide_unsigned = base.divide_unsigned
interval_add = base.interval_add
interval_subtract = base.interval_subtract
interval_multiply = base.interval_multiply
interval_divide = base.interval_divide

base.lib.mpfr_cos.argtypes = [base.P, base.P, ctypes.c_int]


def cosine(value: Num, rounding: int) -> Num:
    result = Num()
    base.lib.mpfr_cos(result.pointer, value.pointer, rounding)
    return result


def interval_cosine(value: Interval) -> Interval:
    # All intervals used here are shorter than 1e-3 and away from a
    # monotonicity ambiguity.  A midpoint/Lipschitz enclosure is rigorous.
    midpoint = divide_unsigned(
        add(value.lower, value.upper, MPFR_RNDN), 2, MPFR_RNDN
    )
    radius = base.maximum(
        [
            subtract(midpoint, value.lower, MPFR_RNDU),
            subtract(value.upper, midpoint, MPFR_RNDU),
        ]
    ).copy()
    return Interval(
        subtract(cosine(midpoint, MPFR_RNDD), radius, MPFR_RNDD),
        add(cosine(midpoint, MPFR_RNDU), radius, MPFR_RNDU),
    )


def sinc_interval(value: Interval) -> Interval:
    return interval_divide(base.sine_of_tiny_interval(value), value)


def sinc_prime_interval(value: Interval) -> Interval:
    z2 = interval_multiply(value, value)
    numerator = interval_subtract(
        interval_multiply(value, interval_cosine(value)),
        base.sine_of_tiny_interval(value),
    )
    return interval_divide(numerator, z2)


def sinc_second_interval(value: Interval) -> Interval:
    z2 = interval_multiply(value, value)
    z3 = interval_multiply(z2, value)
    term1 = interval_multiply(z2, base.sine_of_tiny_interval(value))
    # Explicitly form -z^2 sin(z) - 2 z cos(z) + 2 sin(z).
    neg_term1 = Interval(
        subtract(Num.unsigned(0), term1.upper, MPFR_RNDD),
        subtract(Num.unsigned(0), term1.lower, MPFR_RNDU),
    )
    zcos = interval_multiply(value, interval_cosine(value))
    twice_zcos = interval_multiply(
        Interval(Num.unsigned(2), Num.unsigned(2)), zcos
    )
    neg_twice_zcos = Interval(
        subtract(Num.unsigned(0), twice_zcos.upper, MPFR_RNDD),
        subtract(Num.unsigned(0), twice_zcos.lower, MPFR_RNDU),
    )
    twice_sin = interval_multiply(
        Interval(Num.unsigned(2), Num.unsigned(2)),
        base.sine_of_tiny_interval(value),
    )
    numerator = interval_add(interval_add(neg_term1, neg_twice_zcos), twice_sin)
    return interval_divide(numerator, z3)


def _interval_ratio(index: int, denominator: int) -> Interval:
    n = Num.unsigned(index)
    return Interval(
        divide_unsigned(n, denominator, MPFR_RNDD),
        divide_unsigned(n, denominator, MPFR_RNDU),
    )


class Constants:
    def __init__(self) -> None:
        numerator = Num.unsigned(147)
        self.half_a = Interval(
            divide_unsigned(numerator, 200, MPFR_RNDD),
            divide_unsigned(numerator, 200, MPFR_RNDU),
        )
        self.pi = Interval(
            base.pi(MPFR_RNDD), base.pi(MPFR_RNDU)
        )
        self.normalizer = interval_divide(
            base.sine_of_tiny_interval(self.half_a), self.half_a
        )


def kernel_derivatives(x: Interval, constants: Constants):
    pi_x = interval_multiply(constants.pi, x)
    left = interval_subtract(pi_x, constants.half_a)
    right = interval_add(pi_x, constants.half_a)
    s0 = interval_add(sinc_interval(left), sinc_interval(right))
    s1 = interval_add(sinc_prime_interval(left), sinc_prime_interval(right))
    s2 = interval_add(sinc_second_interval(left), sinc_second_interval(right))
    two = Interval(Num.unsigned(2), Num.unsigned(2))
    raw0 = interval_divide(s0, two)
    raw1 = interval_divide(s1, two)
    raw2 = interval_divide(s2, two)
    k = interval_divide(raw0, constants.normalizer)
    kp = interval_divide(
        interval_multiply(constants.pi, raw1), constants.normalizer
    )
    kpp = interval_divide(
        interval_multiply(
            interval_multiply(constants.pi, constants.pi), raw2
        ),
        constants.normalizer,
    )
    w = interval_multiply(k, k)
    wp = interval_multiply(
        Interval(Num.unsigned(2), Num.unsigned(2)),
        interval_multiply(k, kp),
    )
    wpp = interval_add(
        interval_multiply(
            Interval(Num.unsigned(2), Num.unsigned(2)),
            interval_multiply(kp, kp),
        ),
        interval_multiply(
            Interval(Num.unsigned(2), Num.unsigned(2)),
            interval_multiply(k, kpp),
        ),
    )
    return w, wp, wpp


def _chunks(begin: int, end: int, count: int):
    width = max(1, (end - begin + count - 1) // count)
    return [(left, min(end, left + width))
            for left in range(begin, end, width)]


def _second_chunk(begin: int, end: int, grid: int, start: int) -> list[float]:
    constants = Constants()
    values: list[float] = []
    for i in range(begin, end):
        left = _interval_ratio(i, grid)
        right = _interval_ratio(i + 1, grid)
        interval = Interval(left.lower, right.upper)
        _, _, second = kernel_derivatives(interval, constants)
        values.append(second.lower.binary64(MPFR_RNDD))
    return values


def _point_chunk(begin: int, end: int, grid: int) -> tuple[list[float], ...]:
    constants = Constants()
    values = [[] for _ in range(4)]
    for i in range(begin, end):
        x = _interval_ratio(i, 2 * grid)
        value, first, _ = kernel_derivatives(x, constants)
        values[0].append(value.lower.binary64(MPFR_RNDD))
        values[1].append(value.upper.binary64(MPFR_RNDU))
        values[2].append(first.lower.binary64(MPFR_RNDD))
        values[3].append(first.upper.binary64(MPFR_RNDU))
    return tuple(values)


def generate(grid: int, cells: int, start: int, output: Path,
             workers: int = 1) -> str:
    workers = max(1, workers)
    second = [-math.inf] * cells
    nan = math.nan
    second_chunks = _chunks(start, cells, workers)
    point_chunks = _chunks(2 * start, 2 * cells + 1, workers)
    with ProcessPoolExecutor(max_workers=workers) as pool:
        second_futures = [
            pool.submit(_second_chunk, left, right, grid, start)
            for left, right in second_chunks
        ]
        point_futures = [
            pool.submit(_point_chunk, left, right, grid)
            for left, right in point_chunks
        ]
        for (left, _), future in zip(second_chunks, second_futures):
            part = future.result()
            second[left:left + len(part)] = part
    points = 2 * cells + 1
    values = [[nan] * points for _ in range(4)]
    for (left, _), future in zip(point_chunks, point_futures):
        part = future.result()
        for row in range(4):
            values[row][left:left + len(part[row])] = part[row]
    with output.open("wb") as stream:
        stream.write(b"CWD2")
        stream.write(struct.pack(">III", grid, cells, start))
        for value in second:
            stream.write(struct.pack(">d", value))
        for row in values:
            for value in row:
                stream.write(struct.pack(">d", value))
    return hashlib.sha256(output.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=4000)
    parser.add_argument("--cells", type=int, default=43247)
    parser.add_argument("--start", type=int, default=3500)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    digest = generate(args.grid, args.cells, args.start, args.output, args.workers)
    print(f"mpfr_version={base.lib.mpfr_get_version().decode()}")
    print(f"sha256={digest}")
    print(f"wrote={args.output}")


if __name__ == "__main__":
    if os.name == "nt":
        dll = os.environ.get("ZETA_MPFR_DLL", r"C:\Strawberry\c\bin\libmpfr-6.dll")
    main()

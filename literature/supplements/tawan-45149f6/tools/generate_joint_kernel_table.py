#!/usr/bin/env python3
"""Rigorous lower table for the squared cosine-window kernel a=147/100.

The script uses system MPFR through ctypes, so python-flint is not required.
Every transcendental endpoint is enclosed with directed MPFR rounding.  A
closed-cell enclosure follows from linear interpolation and the elementary
uniform bound |k''| < 4.
"""
from __future__ import annotations

import argparse
import ctypes
import ctypes.util
import hashlib
import math
import struct
import time
from pathlib import Path

MPFR_RNDN = 0
MPFR_RNDU = 2
MPFR_RNDD = 3


class _MPFRStruct(ctypes.Structure):
    _fields_ = [
        ("_mpfr_prec", ctypes.c_long),
        ("_mpfr_sign", ctypes.c_int),
        ("_mpfr_exp", ctypes.c_long),
        ("_mpfr_d", ctypes.POINTER(ctypes.c_ulong)),
    ]


P = ctypes.POINTER(_MPFRStruct)
_library_name = ctypes.util.find_library("mpfr") or "libmpfr.so.6"
lib = ctypes.CDLL(_library_name)

_PROTOTYPES = {
    "mpfr_init2": [P, ctypes.c_long],
    "mpfr_clear": [P],
    "mpfr_set": [P, P, ctypes.c_int],
    "mpfr_set_ui": [P, ctypes.c_ulong, ctypes.c_int],
    "mpfr_add": [P, P, P, ctypes.c_int],
    "mpfr_sub": [P, P, P, ctypes.c_int],
    "mpfr_mul": [P, P, P, ctypes.c_int],
    "mpfr_div": [P, P, P, ctypes.c_int],
    "mpfr_div_ui": [P, P, ctypes.c_ulong, ctypes.c_int],
    "mpfr_sqrt": [P, P, ctypes.c_int],
    "mpfr_sin": [P, P, ctypes.c_int],
    "mpfr_const_pi": [P, ctypes.c_int],
    "mpfr_cmp": [P, P],
    "mpfr_sgn": [P],
    "mpfr_get_d": [P, ctypes.c_int],
}
for _name, _args in _PROTOTYPES.items():
    _fn = getattr(lib, _name)
    _fn.argtypes = _args
lib.mpfr_cmp.restype = ctypes.c_int
lib.mpfr_sgn.restype = ctypes.c_int
lib.mpfr_get_d.restype = ctypes.c_double
lib.mpfr_get_version.restype = ctypes.c_char_p


class Num:
    __slots__ = ("value", "alive")
    precision = 256

    def __init__(self) -> None:
        self.value = _MPFRStruct()
        self.alive = True
        lib.mpfr_init2(ctypes.byref(self.value), self.precision)

    def __del__(self) -> None:
        if getattr(self, "alive", False):
            lib.mpfr_clear(ctypes.byref(self.value))
            self.alive = False

    @property
    def pointer(self):
        return ctypes.byref(self.value)

    @classmethod
    def unsigned(cls, value: int, rounding: int = MPFR_RNDN) -> "Num":
        result = cls()
        lib.mpfr_set_ui(result.pointer, value, rounding)
        return result

    def copy(self, rounding: int = MPFR_RNDN) -> "Num":
        result = Num()
        lib.mpfr_set(result.pointer, self.pointer, rounding)
        return result

    def binary64(self, rounding: int) -> float:
        return float(lib.mpfr_get_d(self.pointer, rounding))


def _binary(name: str, left: Num, right: Num, rounding: int) -> Num:
    result = Num()
    getattr(lib, name)(result.pointer, left.pointer, right.pointer, rounding)
    return result


def add(left: Num, right: Num, rounding: int) -> Num:
    return _binary("mpfr_add", left, right, rounding)


def subtract(left: Num, right: Num, rounding: int) -> Num:
    return _binary("mpfr_sub", left, right, rounding)


def multiply(left: Num, right: Num, rounding: int) -> Num:
    return _binary("mpfr_mul", left, right, rounding)


def divide(left: Num, right: Num, rounding: int) -> Num:
    return _binary("mpfr_div", left, right, rounding)


def divide_unsigned(value: Num, denominator: int, rounding: int) -> Num:
    result = Num()
    lib.mpfr_div_ui(result.pointer, value.pointer, denominator, rounding)
    return result


def square_root(value: Num, rounding: int) -> Num:
    result = Num()
    lib.mpfr_sqrt(result.pointer, value.pointer, rounding)
    return result


def sine(value: Num, rounding: int) -> Num:
    result = Num()
    lib.mpfr_sin(result.pointer, value.pointer, rounding)
    return result


def pi(rounding: int) -> Num:
    result = Num()
    lib.mpfr_const_pi(result.pointer, rounding)
    return result


def minimum(values: list[Num]) -> Num:
    result = values[0]
    for value in values[1:]:
        if lib.mpfr_cmp(value.pointer, result.pointer) < 0:
            result = value
    return result


def maximum(values: list[Num]) -> Num:
    result = values[0]
    for value in values[1:]:
        if lib.mpfr_cmp(value.pointer, result.pointer) > 0:
            result = value
    return result


class Interval:
    __slots__ = ("lower", "upper")

    def __init__(self, lower: Num, upper: Num) -> None:
        if lib.mpfr_cmp(lower.pointer, upper.pointer) > 0:
            raise ValueError("reversed interval")
        self.lower = lower
        self.upper = upper


def interval_add(left: Interval, right: Interval) -> Interval:
    return Interval(
        add(left.lower, right.lower, MPFR_RNDD),
        add(left.upper, right.upper, MPFR_RNDU),
    )


def interval_subtract(left: Interval, right: Interval) -> Interval:
    return Interval(
        subtract(left.lower, right.upper, MPFR_RNDD),
        subtract(left.upper, right.lower, MPFR_RNDU),
    )


def interval_multiply(left: Interval, right: Interval) -> Interval:
    lowers = [
        multiply(a, b, MPFR_RNDD)
        for a in (left.lower, left.upper)
        for b in (right.lower, right.upper)
    ]
    uppers = [
        multiply(a, b, MPFR_RNDU)
        for a in (left.lower, left.upper)
        for b in (right.lower, right.upper)
    ]
    return Interval(minimum(lowers).copy(), maximum(uppers).copy())


def interval_divide(left: Interval, right: Interval) -> Interval:
    lower_sign = lib.mpfr_sgn(right.lower.pointer)
    upper_sign = lib.mpfr_sgn(right.upper.pointer)
    if lower_sign <= 0 <= upper_sign:
        raise ZeroDivisionError("denominator interval contains zero")
    lowers = [
        divide(a, b, MPFR_RNDD)
        for a in (left.lower, left.upper)
        for b in (right.lower, right.upper)
    ]
    uppers = [
        divide(a, b, MPFR_RNDU)
        for a in (left.lower, left.upper)
        for b in (right.lower, right.upper)
    ]
    return Interval(minimum(lowers).copy(), maximum(uppers).copy())


def interval_divide_unsigned(value: Interval, denominator: int) -> Interval:
    return Interval(
        divide_unsigned(value.lower, denominator, MPFR_RNDD),
        divide_unsigned(value.upper, denominator, MPFR_RNDU),
    )


def sine_of_tiny_interval(value: Interval) -> Interval:
    """Enclose sin(value) via a midpoint and the global Lipschitz constant 1."""
    midpoint = divide_unsigned(
        add(value.lower, value.upper, MPFR_RNDN), 2, MPFR_RNDN
    )
    left_radius = subtract(midpoint, value.lower, MPFR_RNDU)
    right_radius = subtract(value.upper, midpoint, MPFR_RNDU)
    radius = maximum([left_radius, right_radius]).copy()
    return Interval(
        subtract(sine(midpoint, MPFR_RNDD), radius, MPFR_RNDD),
        add(sine(midpoint, MPFR_RNDU), radius, MPFR_RNDU),
    )


def sinc_of_tiny_interval(value: Interval) -> Interval:
    return interval_divide(sine_of_tiny_interval(value), value)


class Constants:
    def __init__(self) -> None:
        numerator = Num.unsigned(147)
        half_a = Interval(
            divide_unsigned(numerator, 200, MPFR_RNDD),
            divide_unsigned(numerator, 200, MPFR_RNDU),
        )
        self.half_a = half_a
        self.pi = Interval(pi(MPFR_RNDD), pi(MPFR_RNDU))
        self.kernel_zero = interval_divide(
            sine_of_tiny_interval(self.half_a),
            self.half_a,
        )


def endpoint_kernel(index: int, grid: int, constants: Constants) -> tuple[float, float]:
    numerator = Num.unsigned(index)
    x = Interval(
        divide_unsigned(numerator, grid, MPFR_RNDD),
        divide_unsigned(numerator, grid, MPFR_RNDU),
    )
    pi_x = interval_multiply(constants.pi, x)
    left = interval_subtract(pi_x, constants.half_a)
    right = interval_add(pi_x, constants.half_a)
    raw = interval_divide_unsigned(
        interval_add(sinc_of_tiny_interval(left), sinc_of_tiny_interval(right)), 2
    )
    normalized = interval_divide(raw, constants.kernel_zero)
    return (
        normalized.lower.binary64(MPFR_RNDD),
        normalized.upper.binary64(MPFR_RNDU),
    )


def downward_product(left: float, right: float) -> float:
    return math.nextafter(left * right, -math.inf)


def generate(grid: int, cell_count: int, progress_every: int) -> tuple[list[float], float]:
    constants = Constants()
    endpoints: list[tuple[float, float]] = []
    started = time.perf_counter()
    for index in range(cell_count + 1):
        endpoints.append(endpoint_kernel(index, grid, constants))
        if progress_every and index and index % progress_every == 0:
            elapsed = time.perf_counter() - started
            print(f"endpoints={index}/{cell_count} elapsed={elapsed:.1f}s", flush=True)

    # From the integral representation:
    # |k''(x)| <= pi^2/(3 k(0)) < 4.  Therefore the error of linear
    # interpolation on a cell of width h is at most 4 h^2 / 8 = h^2/2.
    interpolation_error = math.nextafter(1.0 / (2.0 * grid * grid), math.inf)
    lower_table: list[float] = []
    for index in range(cell_count):
        lower = math.nextafter(
            min(endpoints[index][0], endpoints[index + 1][0])
            - interpolation_error,
            -math.inf,
        )
        upper = math.nextafter(
            max(endpoints[index][1], endpoints[index + 1][1])
            + interpolation_error,
            math.inf,
        )
        if lower <= 0.0 <= upper:
            lower_table.append(0.0)
        else:
            absolute_lower = min(abs(lower), abs(upper))
            lower_table.append(max(0.0, downward_product(absolute_lower, absolute_lower)))
    return lower_table, interpolation_error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=4000)
    parser.add_argument("--cells", type=int, default=43247)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--progress-every", type=int, default=10000)
    args = parser.parse_args()
    if args.grid <= 0 or args.cells <= 0:
        raise SystemExit("grid and cells must be positive")

    table, interpolation_error = generate(
        args.grid, args.cells, args.progress_every
    )
    with args.output.open("wb") as output:
        output.write(b"CWK2")
        output.write(struct.pack(">II", args.grid, args.cells))
        for value in table:
            output.write(struct.pack(">d", value))

    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(f"mpfr_version={lib.mpfr_get_version().decode()}")
    print(f"interpolation_error={interpolation_error:.17g}")
    print(f"sha256={digest}")
    print(f"wrote={args.output} cells={len(table)}")


if __name__ == "__main__":
    main()

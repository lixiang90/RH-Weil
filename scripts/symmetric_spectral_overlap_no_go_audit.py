"""Exact rational audit for symmetric-cone sign and overlap degeneration."""

from __future__ import annotations

from fractions import Fraction


Measure = dict[int, Fraction]


def convolve(left: Measure, right: Measure) -> Measure:
    result: Measure = {}
    for x, a in left.items():
        for y, b in right.items():
            result[x + y] = result.get(x + y, Fraction(0)) + a * b
    return {x: a for x, a in result.items() if a}


def primitive_inner(left: Measure, right: Measure) -> Fraction:
    if sum(left.values()) or sum(right.values()):
        raise AssertionError("primitive measures must have zero mass")
    positions = range(min(min(left), min(right)), max(max(left), max(right)))
    left_cumulative = Fraction(0)
    right_cumulative = Fraction(0)
    inner = Fraction(0)
    for position in positions:
        left_cumulative += left.get(position, Fraction(0))
        right_cumulative += right.get(position, Fraction(0))
        inner += left_cumulative * right_cumulative
    return inner


def alternating_multiplier(length: int) -> Measure:
    if length <= 0 or length % 2:
        raise ValueError("length must be positive and even")
    return {index: Fraction((-1) ** index) for index in range(length)}


def main() -> None:
    prime = {-1: Fraction(1, 2), 0: Fraction(-1), 1: Fraction(1, 2)}
    continuum = {-2: Fraction(-1, 2), 0: Fraction(1), 2: Fraction(-1, 2)}

    rows = []
    for length in (4, 8, 16, 32, 64, 128):
        multiplier = alternating_multiplier(length)
        prime_response = convolve(prime, multiplier)
        continuum_response = convolve(continuum, multiplier)
        prime_energy = primitive_inner(prime_response, prime_response)
        continuum_energy = primitive_inner(
            continuum_response, continuum_response
        )
        cross = primitive_inner(prime_response, continuum_response)
        assert cross <= 0
        rows.append((length, prime_energy, continuum_energy, cross))
        print(
            f"N={length:>2}: P={prime_energy}, C={continuum_energy}, "
            f"z={cross}, -z/(P+C)={float(-cross/(prime_energy+continuum_energy)):.8f}"
        )

    for length, prime_energy, continuum_energy, cross in rows:
        assert prime_energy == length - Fraction(1, 2)
        assert continuum_energy == 1
        assert cross == -1
    print("symmetric spectral-overlap no-go passed")
    print("[scope] exact rational finite theorem/no-go; no RH asymptotic")


if __name__ == "__main__":
    main()

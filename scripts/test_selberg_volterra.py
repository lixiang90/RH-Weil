"""Regression checks for the Selberg--Volterra transport ledger."""

from __future__ import annotations

import cmath

from selberg_volterra import (
    constant_block_obstruction,
    prefix_transport_ledger,
)


def main() -> None:
    increments = [
        1 - 2j,
        -3 + 0.5j,
        2.25 + 4j,
        -0.75 - 1.5j,
        3 + 0j,
    ]
    weights = [
        cmath.exp(-(0.4 + 2.3j) * index / 7)
        for index in range(1, len(increments) + 1)
    ]
    ledger = prefix_transport_ledger(increments, weights)
    assert abs(ledger["direct"] - ledger["transported"]) < 1e-12
    assert abs(ledger["direct"]) ** 2 <= ledger["cauchy_majorant"] + 1e-12

    for length in (1, 4, 17, 64):
        obstruction = constant_block_obstruction(length)
        assert obstruction["coefficient_square_mass"] == length
        assert obstruction["terminal_prefix_square"] == length**2
        assert obstruction["amplification"] == length

    print("Selberg--Volterra transport checks passed.")


if __name__ == "__main__":
    main()

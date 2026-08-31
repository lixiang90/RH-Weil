"""Finite ledgers for the Selberg--Volterra transport identity.

These routines verify exact finite summation-by-parts identities and their
Cauchy majorants.  They do not prove a Selberg-integral estimate or the
Riemann hypothesis.
"""

from __future__ import annotations

from collections.abc import Sequence


def prefix_transport_ledger(
    increments: Sequence[complex], weights: Sequence[complex]
) -> dict[str, object]:
    """Return the exact discrete Volterra/Abel transport ledger.

    If B_j=sum_{k<=j} a_k, summation by parts gives

        sum_j f_j a_j
        = f_H B_H + sum_{j<H} (f_j-f_{j+1}) B_j.

    The returned majorant is the two-term Cauchy bound used by the
    continuous Selberg--Hardy argument.
    """
    if not increments or len(increments) != len(weights):
        raise ValueError("increments and weights must have the same positive length")

    prefixes: list[complex] = []
    running = 0j
    for value in increments:
        running += complex(value)
        prefixes.append(running)

    direct = sum(
        complex(weight) * complex(value)
        for weight, value in zip(weights, increments)
    )
    differences = [
        complex(weights[index]) - complex(weights[index + 1])
        for index in range(len(weights) - 1)
    ]
    transported = complex(weights[-1]) * prefixes[-1] + sum(
        difference * prefixes[index]
        for index, difference in enumerate(differences)
    )

    endpoint_energy = abs(complex(weights[-1]) * prefixes[-1]) ** 2
    volterra_energy = sum(
        abs(difference * prefixes[index]) ** 2
        for index, difference in enumerate(differences)
    )
    cauchy_majorant = 2 * endpoint_energy + 2 * max(
        1, len(differences)
    ) * volterra_energy

    return {
        "direct": direct,
        "transported": transported,
        "prefixes": prefixes,
        "weight_differences": differences,
        "endpoint_energy": endpoint_energy,
        "volterra_energy": volterra_energy,
        "cauchy_majorant": cauchy_majorant,
    }


def constant_block_obstruction(length: int) -> dict[str, int]:
    """A finite no-go ledger for coefficient-diagonal-only control.

    For a_j=1, the coefficient square mass is H whereas the terminal prefix
    square is H^2.  Thus a scalar second moment cannot by itself give a
    linear prefix-profile estimate.
    """
    if length < 1:
        raise ValueError("length must be positive")
    coefficient_square_mass = length
    terminal_prefix_square = length * length
    return {
        "length": length,
        "coefficient_square_mass": coefficient_square_mass,
        "terminal_prefix_square": terminal_prefix_square,
        "amplification": length,
    }

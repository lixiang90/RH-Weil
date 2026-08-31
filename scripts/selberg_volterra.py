"""Finite ledgers for the Selberg--Volterra transport identity.

These routines verify exact finite summation-by-parts identities and their
Cauchy majorants.  They do not prove a Selberg-integral estimate or the
Riemann hypothesis.
"""

from __future__ import annotations

from collections.abc import Sequence
import math


def cumulative_prefix_support(length: int) -> tuple[tuple[int, ...], ...]:
    """Supports of the canonical cumulative-prefix matrix.

    Row ``k`` contains physical increments ``0,...,k``.  These are the
    nonzero positions of the lower-triangular Volterra matrix.
    """
    if length < 1:
        raise ValueError("length must be positive")
    return tuple(tuple(range(endpoint + 1)) for endpoint in range(length))


def sliding_prefix_support(
    length: int, window_size: int
) -> tuple[tuple[int, ...], ...]:
    """Supports of consecutive sliding interval rows on a finite chain."""
    if length < 1:
        raise ValueError("length must be positive")
    if not 1 <= window_size <= length:
        raise ValueError("window size must lie between one and length")
    return tuple(
        tuple(range(start, min(length, start + window_size)))
        for start in range(length)
    )


def transport_support_audit(
    physical_count: int,
    channel_to_physical: Sequence[int],
    prefix_supports: Sequence[Sequence[int]],
) -> dict[str, object]:
    """Audit the support graph of channel--physical--prefix transport.

    A channel vertex is attached to its terminal physical product.  A
    prefix vertex is attached to every physical increment in its support.
    Empty prefix rows and isolated vertices are reported separately, and
    connected components are computed after pruning them.
    """
    if physical_count < 1:
        raise ValueError("physical count must be positive")
    for physical in channel_to_physical:
        if not 0 <= int(physical) < physical_count:
            raise ValueError("channel terminal index lies outside physical range")

    normalized_supports: list[tuple[int, ...]] = []
    empty_prefix_rows: list[int] = []
    for row, support in enumerate(prefix_supports):
        normalized = tuple(sorted(set(int(index) for index in support)))
        if any(index < 0 or index >= physical_count for index in normalized):
            raise ValueError("prefix support index lies outside physical range")
        normalized_supports.append(normalized)
        if not normalized:
            empty_prefix_rows.append(row)

    physical_vertices = [("physical", index) for index in range(physical_count)]
    channel_vertices = [("channel", index) for index in range(len(channel_to_physical))]
    prefix_vertices = [("prefix", index) for index in range(len(normalized_supports))]
    vertices = physical_vertices + channel_vertices + prefix_vertices
    adjacency: dict[tuple[str, int], set[tuple[str, int]]] = {
        vertex: set() for vertex in vertices
    }

    def add_edge(left: tuple[str, int], right: tuple[str, int]) -> None:
        adjacency[left].add(right)
        adjacency[right].add(left)

    for channel, physical in enumerate(channel_to_physical):
        add_edge(("channel", channel), ("physical", int(physical)))
    for row, support in enumerate(normalized_supports):
        for physical in support:
            add_edge(("prefix", row), ("physical", physical))

    isolated = tuple(vertex for vertex in vertices if not adjacency[vertex])
    active = {vertex for vertex in vertices if adjacency[vertex]}
    unseen = set(active)
    components: list[tuple[tuple[str, int], ...]] = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        unseen.remove(seed)
        component: list[tuple[str, int]] = []
        while stack:
            vertex = stack.pop()
            component.append(vertex)
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
        components.append(tuple(sorted(component)))

    physical_component = [-1] * physical_count
    for component_index, component in enumerate(components):
        for kind, index in component:
            if kind == "physical":
                physical_component[index] = component_index

    return {
        "physical_count": physical_count,
        "channel_count": len(channel_to_physical),
        "prefix_count": len(normalized_supports),
        "empty_prefix_rows": tuple(empty_prefix_rows),
        "isolated_vertices": isolated,
        "components": tuple(components),
        "component_count_after_pruning": len(components),
        "connected_after_pruning": len(components) <= 1,
        "physical_component": tuple(physical_component),
    }


def cumulative_transport_singular_values(length: int) -> tuple[float, ...]:
    """Exact singular values of ``C[k,j]=1(j<=k)`` in descending order."""
    if length < 1:
        raise ValueError("length must be positive")
    return tuple(
        1.0
        / (
            2.0
            * math.sin((2 * index - 1) * math.pi / (4 * length + 2))
        )
        for index in range(1, length + 1)
    )


def cumulative_transport_condition_ledger(length: int) -> dict[str, float | int]:
    """Return exact extremal singular values and condition number."""
    singular_values = cumulative_transport_singular_values(length)
    largest = singular_values[0]
    smallest = singular_values[-1]
    return {
        "length": length,
        "largest_singular_value": largest,
        "smallest_singular_value": smallest,
        "condition_number": largest / smallest,
    }


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

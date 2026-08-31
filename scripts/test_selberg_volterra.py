"""Regression checks for the Selberg--Volterra transport ledger."""

from __future__ import annotations

import cmath

import numpy as np

from selberg_volterra import (
    constant_block_obstruction,
    cumulative_prefix_support,
    cumulative_transport_condition_ledger,
    cumulative_transport_singular_values,
    prefix_transport_ledger,
    sliding_prefix_support,
    transport_support_audit,
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

    for length in (1, 2, 7, 19):
        cumulative = np.tril(np.ones((length, length)))
        numerical = np.linalg.svd(cumulative, compute_uv=False)
        exact = np.array(cumulative_transport_singular_values(length))
        assert np.allclose(numerical, exact, atol=1.0e-12, rtol=1.0e-12)
        condition = cumulative_transport_condition_ledger(length)
        assert abs(condition["largest_singular_value"] - numerical[0]) < 1.0e-12
        assert abs(condition["smallest_singular_value"] - numerical[-1]) < 1.0e-12
        assert abs(condition["condition_number"] - numerical[0] / numerical[-1]) < (
            1.0e-11
        )

    # Cumulative prefixes connect every physical increment and all channel
    # copies attached to their terminal products.
    cumulative_audit = transport_support_audit(
        physical_count=6,
        channel_to_physical=[0, 0, 2, 5, 5],
        prefix_supports=cumulative_prefix_support(6),
    )
    assert cumulative_audit["connected_after_pruning"]
    assert cumulative_audit["component_count_after_pruning"] == 1
    assert not cumulative_audit["isolated_vertices"]

    # Consecutive two-point windows connect a chain; singleton windows do not.
    connected_sliding = transport_support_audit(
        physical_count=8,
        channel_to_physical=[1, 6],
        prefix_supports=sliding_prefix_support(8, 2),
    )
    assert connected_sliding["connected_after_pruning"]
    disconnected_sliding = transport_support_audit(
        physical_count=8,
        channel_to_physical=[1, 6],
        prefix_supports=sliding_prefix_support(8, 1),
    )
    assert disconnected_sliding["component_count_after_pruning"] == 8

    # A genuine gap in prefix support leaves two components even though each
    # component can contain several factorization channels.
    gap_audit = transport_support_audit(
        physical_count=6,
        channel_to_physical=[0, 2, 2, 3, 5],
        prefix_supports=[(0, 1, 2), (3, 4, 5)],
    )
    assert gap_audit["component_count_after_pruning"] == 2
    assert gap_audit["physical_component"][2] != gap_audit["physical_component"][3]

    print("Selberg--Volterra transport checks passed.")


if __name__ == "__main__":
    main()

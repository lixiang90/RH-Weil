"""Regression checks for the capped-correspondence kernel theorem."""

from __future__ import annotations

import numpy as np

from capped_correspondence import capped_index, effect_objective, gram_from_measure


def main() -> None:
    rng = np.random.default_rng(170)
    heights = np.array([-3.0, -1.25, -0.2, 0.7, 2.4, 5.0])
    weights = np.array([0.07, 0.16, 0.22, 0.19, 0.24, 0.12])
    lengths = np.array([0.0, 0.3, 0.9, 1.7, 2.8])
    effect = rng.uniform(0.0, 1.0, heights.size)

    ambient = gram_from_measure(lengths, heights, weights)
    selected = gram_from_measure(lengths, heights, weights * effect)
    complement = ambient - selected
    assert np.linalg.eigvalsh(selected).min() > -1e-12
    assert np.linalg.eigvalsh(complement).min() > -1e-12

    symbol = np.array([-2.0, 0.4, -0.1, 1.7, -3.2, 0.0])
    optimizer = (symbol < 0.0).astype(float)
    exact = capped_index(symbol, weights)
    assert abs(effect_objective(symbol, weights, optimizer) + exact) < 1e-14
    for _ in range(200):
        trial = rng.uniform(0.0, 1.0, heights.size)
        assert effect_objective(symbol, weights, trial) >= -exact - 1e-14

    cut = 3
    block_sum = capped_index(symbol[:cut], weights[:cut]) + capped_index(
        symbol[cut:], weights[cut:]
    )
    assert abs(block_sum - exact) < 1e-14

    grid = np.linspace(-np.pi, np.pi, 2001)
    haar_weights = np.full(grid.size, 1.0 / grid.size)
    for scale in (1.0, 10.0, 100.0):
        nonnegative_symbol = scale * (1.0 + np.cos(grid))
        assert capped_index(nonnegative_symbol, haar_weights) == 0.0
        l2_mass = float(np.dot(haar_weights, nonnegative_symbol**2))
        assert l2_mass > scale**2

    print("capped correspondence kernel checks passed")


if __name__ == "__main__":
    main()

"""Finite audits for radial cross-box coherence obstructions.

The checks cover the sharp pairwise-versus-union Hilbert-space example, the
exact radial factorization of the alternating symbol, plateau-window radial
coherence, and saturation of the cross-scale determinant degree Schur bound.
They do not establish decay for the actual prime-power radial Gram.
"""

from __future__ import annotations

import math

import numpy as np

from toeplitz_hankel_adjacent_audit import smooth_compact_window


TOL = 3.0e-11


def audit_pairwise_union_no_go() -> None:
    for length in (32, 64, 128, 256):
        box_count = length
        main_scale = float(length)
        local_norm_squared = main_scale / length**2
        pair_ratio = local_norm_squared / main_scale
        union_norm_squared = box_count**2 * local_norm_squared
        union_ratio = union_norm_squared / main_scale
        assert pair_ratio == 1.0 / length**2
        assert abs(union_ratio - 1.0) <= TOL
        print(
            f"Hilbert no-go L={length}: pair/N={pair_ratio:.3e}, "
            f"union/N={union_ratio:.6f}"
        )


def real_line_window(argument: np.ndarray, length: float) -> np.ndarray:
    return smooth_compact_window(argument, length)


def radial_symbol(
    grid: np.ndarray, length: float, ratio_shift: float, numerator_log: float
) -> np.ndarray:
    return (
        real_line_window(grid, length)
        * real_line_window(grid - ratio_shift, length)
        * real_line_window(numerator_log - grid, length) ** 2
    )


def audit_exact_radial_factorization() -> None:
    length = 32.0
    grid = np.linspace(-length / 2.0, length / 2.0, 1 << 14, endpoint=False)
    numerator_log = 12.3
    denominator_log = 9.7
    ratio_shift = numerator_log - denominator_log
    q_numerator = real_line_window(grid, length) * real_line_window(
        numerator_log - grid, length
    )
    translated_q_denominator = real_line_window(
        grid - ratio_shift, length
    ) * real_line_window(
        denominator_log - (grid - ratio_shift), length
    )
    direct = q_numerator * translated_q_denominator
    factored = radial_symbol(grid, length, ratio_shift, numerator_log)
    assert np.linalg.norm(direct - factored) <= TOL * max(
        1.0, np.linalg.norm(factored)
    )
    print("exact alternating radial symbol factorization passed")


def normalized_gram(vectors: np.ndarray) -> np.ndarray:
    gram = vectors @ vectors.T / vectors.shape[1]
    norms = np.sqrt(np.diag(gram))
    assert np.all(norms > 0.0)
    return gram / np.outer(norms, norms)


def audit_plateau_radial_coherence() -> None:
    ratio_shift = 0.37
    for length in (32.0, 64.0, 128.0, 256.0):
        grid = np.linspace(
            -length / 2.0, length / 2.0, 1 << 14, endpoint=False
        )
        radial_logs = np.arange(
            length / 4.0, length / 2.0, math.log(2.0)
        )
        vectors = np.stack(
            [
                radial_symbol(grid, length, ratio_shift, numerator_log)
                for numerator_log in radial_logs
            ]
        )
        gram = normalized_gram(vectors)
        minimum = float(np.min(gram))
        minimum_row_sum = float(np.min(np.sum(np.abs(gram), axis=1)))
        normalized_row_sum = minimum_row_sum / radial_logs.size
        assert minimum >= 0.70
        assert normalized_row_sum >= 0.80
        print(
            f"plateau radial L={length:g}: blocks={radial_logs.size}, "
            f"min-correlation={minimum:.6f}, "
            f"min-row/J={normalized_row_sum:.6f}"
        )


def audit_degree_schur_saturation() -> None:
    for radial_ratio in (2, 4, 8, 16, 32):
        source_count = 12
        matrix = np.zeros(
            (source_count, source_count * radial_ratio), dtype=float
        )
        for source in range(source_count):
            start = source * radial_ratio
            matrix[source, start : start + radial_ratio] = 1.0
        operator_norm = float(np.linalg.svd(matrix, compute_uv=False)[0])
        assert abs(operator_norm - math.sqrt(radial_ratio)) <= TOL
        assert int(np.max(np.sum(matrix, axis=1))) == radial_ratio
        assert int(np.max(np.sum(matrix, axis=0))) == 1
        print(
            f"degree Schur lambda={radial_ratio}: "
            f"operator={operator_norm:.6f}, sqrt(lambda)={math.sqrt(radial_ratio):.6f}"
        )


def main() -> None:
    audit_pairwise_union_no_go()
    audit_exact_radial_factorization()
    audit_plateau_radial_coherence()
    audit_degree_schur_saturation()
    print("Radial cross-box obstruction audits passed.")


if __name__ == "__main__":
    main()

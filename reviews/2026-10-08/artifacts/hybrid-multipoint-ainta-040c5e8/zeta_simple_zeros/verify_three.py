"""Computer-assisted certificate for the 3-point overlap inequality."""

from __future__ import annotations

import time
from typing import List, Tuple

from .kernel import RangeMinimum, build_kernel_table, table_sha256
from .report import VerificationReport
from .rounding import down_add, up_ratio


GRID = 16_000
PRECISION_BITS = 128
DOMAIN_LENGTH = 4
TARGET_NUMERATOR = 221
TARGET_DENOMINATOR = 1_000_000

CellRange = Tuple[int, int]
ThreeBox = Tuple[CellRange, CellRange, int]


def verify_three(progress_every: int = 0) -> VerificationReport:
    r"""Prove k(u)^2 + k(v)^2 + k(u+v)^2 >= 221/10^6.

    The domain is u,v >= 0 and u+v <= 4. Each integer cell i denotes the
    closed interval [i/GRID, (i+1)/GRID]. All transcendental cell bounds are
    produced by Arb before the branch-and-bound phase begins.
    """

    started = time.perf_counter()
    cutoff = DOMAIN_LENGTH * GRID
    cell_count = cutoff + 3
    table = build_kernel_table(GRID, cell_count, PRECISION_BITS)
    ranges = RangeMinimum(table)
    target_upper = up_ratio(TARGET_NUMERATOR, TARGET_DENOMINATOR)

    def kernel_min(left: int, right: int) -> float:
        # A box can extend past u+v=4 before it is split. Returning zero there
        # remains a valid lower bound and avoids evaluating irrelevant cells.
        if right >= ranges.length:
            return 0.0
        return ranges.query(left, right)

    stack: List[ThreeBox] = [((0, cutoff - 1), (0, cutoff - 1), 0)]
    nodes = pruned = splits = maximum_depth = 0

    while stack:
        u, v, depth = stack.pop()
        nodes += 1
        maximum_depth = max(maximum_depth, depth)

        # The rectangle is disjoint from the closed triangle u+v <= 4.
        if u[0] + v[0] > cutoff:
            pruned += 1
            continue

        lower = down_add(ranges.query(*u), ranges.query(*v))
        lower = down_add(
            lower,
            kernel_min(u[0] + v[0], u[1] + v[1] + 1),
        )
        if lower >= target_upper:
            pruned += 1
            continue

        u_width = u[1] - u[0]
        v_width = v[1] - v[0]
        if max(u_width, v_width) == 0:
            raise RuntimeError(
                "3-point certificate failed at a terminal cell: "
                f"u={u}, v={v}, lower={lower.hex()}"
            )

        splits += 1
        if u_width >= v_width:
            midpoint = (u[0] + u[1]) // 2
            stack.append(((u[0], midpoint), v, depth + 1))
            stack.append(((midpoint + 1, u[1]), v, depth + 1))
        else:
            midpoint = (v[0] + v[1]) // 2
            stack.append((u, (v[0], midpoint), depth + 1))
            stack.append((u, (midpoint + 1, v[1]), depth + 1))

        if progress_every and nodes % progress_every == 0:
            print(f"three: nodes={nodes} pending={len(stack)} depth={maximum_depth}")

    elapsed = time.perf_counter() - started
    return VerificationReport(
        certificate="three-point",
        verified=True,
        target=f"epsilon_4 >= {TARGET_NUMERATOR}/{TARGET_DENOMINATOR}",
        grid=GRID,
        precision_bits=PRECISION_BITS,
        kernel_table_sha256=table_sha256(table),
        nodes=nodes,
        pruned=pruned,
        splits=splits,
        maximum_depth=maximum_depth,
        initial_boxes=1,
        elapsed_seconds=elapsed,
        details={
            "domain": "u>=0, v>=0, u+v<=4",
            "certified_epsilon": TARGET_NUMERATOR / TARGET_DENOMINATOR,
        },
    )

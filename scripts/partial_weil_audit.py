"""Finite audits for partial Weil configurations.

This script checks only finite-dimensional linear-algebra identities used in
the companion paper.  It neither locates zeta zeros nor supplies an analytic
estimate for the prime side.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 2.0e-9


def rank_trace_rhs(P: np.ndarray, Q: np.ndarray, b: int) -> float:
    G = P + Q
    return float(
        2.0 * np.trace(P)
        + 4.0 * np.trace(Q)
        - 4.0 * b
        - np.vdot(G, G).real
    )


def partial_weil_bounds(tau: float, second_moment: float) -> tuple[float, float]:
    """Return the normalized simple-line and distinct-point bounds."""
    return (
        max(0.0, 4.0 * tau - 2.0 - second_moment),
        max(0.0, 0.5 * (4.0 * tau - second_moment - 1.0)),
    )


def four_moment_rank_inertia_bound(b2: float, b4: float) -> tuple[float, float]:
    """Exact quartic bound from the centred second and fourth moments."""
    denominator = 1.0 - 2.0 * b2 + b4
    assert denominator > 0.0
    line = (1.0 - b2) ** 2 / denominator
    return line, 0.5 * (1.0 + line)


def random_orthogonal(rng: np.random.Generator, d: int) -> np.ndarray:
    q, r = np.linalg.qr(rng.normal(size=(d, d)))
    signs = np.sign(np.diag(r))
    signs[signs == 0.0] = 1.0
    return q * signs


def audit_random_rank_trace() -> None:
    rng = np.random.default_rng(20260901)
    worst_slack = math.inf
    for _ in range(300):
        d = int(rng.integers(3, 18))
        r = int(rng.integers(0, d + 1))
        b = int(rng.integers(0, d + 1))
        up = random_orthogonal(rng, d)
        uq = random_orthogonal(rng, d)
        p_eigs = np.zeros(d)
        if r:
            p_eigs[:r] = rng.uniform(0.0, 3.5, size=r)
        q_eigs = -rng.uniform(0.0, 3.5, size=d)
        if b:
            q_eigs[:b] = rng.uniform(0.0, 3.5, size=b)
        P = (up * p_eigs) @ up.T
        Q = (uq * q_eigs) @ uq.T
        slack = r - rank_trace_rhs(P, Q, b)
        worst_slack = min(worst_slack, slack)
        assert slack >= -TOL
    print(f"random rank--trace minimum slack: {worst_slack:.6e}")


def audit_sharp_two_moment_model() -> None:
    N, simple, pairs = 600, 400, 100
    d = N
    P = np.zeros((d, d))
    Q = np.zeros((d, d))
    P[np.arange(simple), np.arange(simple)] = 1.0
    idx = np.arange(simple, simple + pairs)
    Q[idx, idx] = 2.0
    G = P + Q
    trace = float(np.trace(G))
    hs2 = float(np.vdot(G, G).real)
    rhs = rank_trace_rhs(P, Q, pairs)
    assert abs(trace - N) <= TOL
    assert abs(hs2 / N - 4.0 / 3.0) <= TOL
    assert abs(rhs - simple) <= TOL
    line_bound, distinct_bound = partial_weil_bounds(1.0, hs2 / N)
    assert abs(line_bound - 2.0 / 3.0) <= TOL
    assert abs(distinct_bound - 5.0 / 6.0) <= TOL
    eigs = np.linalg.eigvalsh(G)
    polynomial_trace = float(np.sum(eigs / 2.0))
    positive_index = int(np.sum(eigs > TOL))
    assert polynomial_trace <= positive_index + TOL
    print(
        "sharp model: "
        f"trace/N={trace/N:.9f}, HS2/N={hs2/N:.9f}, "
        f"simple={line_bound:.9f}, distinct={distinct_bound:.9f}"
    )


def audit_montgomery_taylor_constant() -> None:
    x = 1.0 / math.sqrt(2.0)
    c_inverse = 0.5 + x / math.tan(x)
    line, distinct = partial_weil_bounds(1.0, c_inverse)
    assert 0.6724 < line < 0.6726
    assert 0.8362 < distinct < 0.8363
    print(
        "Montgomery--Taylor: "
        f"R={c_inverse:.12f}, simple={line:.12f}, distinct={distinct:.12f}"
    )


def audit_four_moment_certificate() -> None:
    b2, b4 = 1.0 / 3.0, 1.0 / 4.0
    line, distinct = four_moment_rank_inertia_bound(b2, b4)
    assert abs(line - 16.0 / 21.0) <= TOL
    assert abs(distinct - 37.0 / 42.0) <= TOL

    # The older positive-index/Christoffel count has Lambda_2(0)=5/36,
    # hence 1-2 Lambda_2(0)=13/18.  The exact rank--trace--inertia
    # constraints retain more information.
    christoffel_line = 1.0 - 2.0 * (5.0 / 36.0)
    assert abs(christoffel_line - 13.0 / 18.0) <= TOL
    assert line > christoffel_line

    # Matching extremal spectral measure:
    # 8/21 at 1 +/- 1/(2 sqrt(2)), 5/42 at 2 and 5/42 at 0.
    atoms = np.array(
        [1.0 + 1.0 / (2.0 * math.sqrt(2.0)),
         1.0 - 1.0 / (2.0 * math.sqrt(2.0)),
         2.0,
         0.0]
    )
    weights = np.array([8.0 / 21.0, 8.0 / 21.0, 5.0 / 42.0, 5.0 / 42.0])
    moments = np.array([np.sum(weights * atoms**k) for k in range(5)])
    expected = np.array([1.0, 1.0, 4.0 / 3.0, 2.0, 13.0 / 4.0])
    assert np.max(np.abs(moments - expected)) <= TOL

    # Quartic dual polynomial at the optimizing sigma=1/8.  A dense grid
    # checks its global sign pattern and maximum; the proof is algebraic.
    sigma = 1.0 / 8.0
    xs = np.linspace(-12.0, 12.0, 200_001)
    polynomial = (
        (1.0 - sigma) ** 2
        + 4.0 * (1.0 - sigma) * xs
        - ((xs - 1.0) ** 2 - sigma) ** 2
    )
    assert np.max(polynomial[xs <= 0.0]) <= 2.0e-8
    assert np.max(polynomial) <= 8.0 * (1.0 - sigma) + 2.0e-8

    x = 1.0 / math.sqrt(2.0)
    kappa = 2.0 - (0.5 + x / math.tan(x))
    threshold = 4.0 / (9.0 * kappa) - 1.0 / 3.0
    assert 0.3275 < threshold < 0.3276
    assert b4 < threshold
    print(
        "four moments: "
        f"Christoffel={christoffel_line:.12f}, "
        f"rank-inertia={line:.12f}, distinct={distinct:.12f}, "
        f"b4 threshold={threshold:.12f}"
    )


def audit_depth_visibility() -> None:
    d, deep = 9, 3
    C = np.zeros((d, d))
    B = np.zeros((d, d))
    idx = np.arange(d - deep, d)
    C[idx, idx] = 0.5
    B[idx, idx] = 1.0
    G = C @ C.T - B @ B.T
    eigs = np.linalg.eigvalsh(G)
    negative_trace = float(np.sum(np.maximum(-eigs, 0.0)))
    visibility = 0.75
    assert negative_trace + TOL >= deep * visibility
    assert int(np.sum(eigs <= -visibility + TOL)) >= deep
    print(
        "depth visibility: "
        f"deep directions={deep}, v={visibility:.3f}, "
        f"negative trace={negative_trace:.6f}"
    )


def main() -> None:
    audit_random_rank_trace()
    audit_sharp_two_moment_model()
    audit_montgomery_taylor_constant()
    audit_four_moment_certificate()
    audit_depth_visibility()
    print("Partial Weil finite audits passed.")


if __name__ == "__main__":
    main()

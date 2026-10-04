"""Exact lattice checks for note 423; not an analytic or RH certificate.

The functions have finite deviations from quadrant/edge steps.  Residuals are
summed as pointwise lattice functions, independently of the symbolic anomaly
formula.  The arbitrary-label obstruction is proved in the note; this program
checks a finite grid of its concrete witnesses using integer arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def step(j):
    return 1 if j is None or j >= 0 else 0


def atom(j, at=0):
    return int(j is not None and j == at)


def shift(f, g):
    return lambda j, k: f(None if j is None else j-g[0],
                          None if k is None else k-g[1])


def product(f, v):
    return lambda j, k: f(j, k)*v(j, k)


def data(f, radius=9):
    """Read all four components from actual tails and residual lattice sums."""
    indices = range(-radius, radius+1)
    corner = f(None, None)
    p_edge = sum(f(None, k)-corner*step(k) for k in indices)
    q_edge = sum(f(j, None)-corner*step(j) for j in indices)
    finite_part = sum(
        f(j, k)-step(j)*f(None, k)-step(k)*f(j, None)
        +step(j)*step(k)*corner
        for j in indices for k in indices
    )
    return finite_part, p_edge, q_edge, corner


def audit():
    functions = [
        lambda j, k: step(j)*step(k),
        lambda j, k: step(j)*atom(k),
        lambda j, k: atom(j)*step(k),
        lambda j, k: (2*step(j)*step(k) + 3*step(j)*atom(k, -1)
                      - 5*atom(j, 1)*step(k)+7*atom(j, -1)*atom(k, 2)),
    ]
    labels = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]
    invariance_checks = 0
    anomaly_checks = 0
    corrected_source_checks = 0
    zero_label_source_checks = 0
    q = lambda g: lambda j, k: step(None if j is None else j-max(0, g[0]))*step(None if k is None else k-max(0, g[1]))
    for gamma in labels:
        for f in functions:
            before = data(f)
            after = data(shift(f, (-gamma[0], -gamma[1])))
            expected = (gamma[0]*before[1]+gamma[1]*before[2]
                        + gamma[0]*gamma[1]*before[3])
            assert after[0]-before[0] == expected
            assert after == data(shift(f, (-gamma[0], -gamma[1])), 12)
            invariance_checks += 1
        for g in labels:
            v_label = (gamma[0]-g[0], gamma[1]-g[1])
            f, v = functions[(g[0]+2) % 4], functions[(g[1]+1) % 4]
            # AB has coefficient f beta_g(v); B sigma_gamma(A) has
            # coefficient v beta_{-g}(f) at the SAME label gamma.
            forward = product(f, shift(v, g))
            reverse = product(v, shift(f, (-g[0], -g[1])))
            fd = data(forward)
            measured = fd[0]-data(reverse)[0]
            expected = -g[0]*fd[1]-g[1]*fd[2]-g[0]*g[1]*fd[3]
            assert measured == expected, (gamma, g, v_label)
            anomaly_checks += 1
            # Standard E_gamma uses sigma^{-1} on B, not sigma on A.
            if g != (0, 0):
                first = product(q(g), shift(q(v_label), g))
                second = product(shift(q(v_label), gamma), shift(q(g), v_label))
                r = tuple(max(0, g[i], gamma[i]) for i in range(2))
                rr = tuple(max(gamma[i], 2*gamma[i]-g[i], gamma[i]-g[i]) for i in range(2))
                assert data(first)[0]-data(second)[0] == r[0]*r[1]-rr[0]*rr[1]
                corrected_source_checks += 1
        # The independent identity and Q*f_0 parts of (T*)_0 differ.
        m = tuple(max(0, x) for x in gamma)
        expected_unit = m[0]*m[1]-(gamma[0]+m[0])*(gamma[1]+m[1])
        assert data(q(gamma))[0]-data(shift(q(gamma), gamma))[0] == expected_unit
        first_f0 = product(q((0, 0)), q(gamma))
        second_f0 = product(shift(q(gamma), gamma), shift(q((0, 0)), gamma))
        assert data(first_f0)[0]-data(second_f0)[0] == expected_unit
        zero_label_source_checks += 2
    s = lambda j, k: step(j)*atom(k)
    witnessed = []
    for gamma in [(a, b) for a in range(-4, 5) for b in range(-4, 5)]:
        # A=s z_(1,0), B=s z_(gamma-(1,0)).  Their twisted
        # commutator coefficient is independent of gamma.
        forward = product(s, shift(s, (1, 0)))
        reverse = product(s, shift(s, (-1, 0)))
        coeff = lambda j, k: forward(j, k)-reverse(j, k)
        assert data(coeff) == (-1, 0, 0, 0)
        for j in range(-9, 10):
            for k in range(-9, 10):
                assert coeff(j, k) == -atom(j)*atom(k)
        witnessed.append(list(gamma))
    # Cyclicity failure: gamma=(1,0), A=H(j)delta_0(k) z_gamma,
    # B=H(j)H(k).  D(A,B)=-1 and D(B,sigma(A))=0.
    q = functions[0]
    cyclic_defect = data(product(s, shift(q, (1, 0))))[0]-data(product(q, s))[0]
    assert cyclic_defect == -1
    return {
        "status": "passed_exact_integer_checks",
        "invariance_checks": invariance_checks,
        "twisted_monomial_anomaly_checks": anomaly_checks,
        "corrected_source_nonzero_label_checks": corrected_source_checks,
        "corrected_source_zero_label_checks": zero_label_source_checks,
        "finite_grid_witnesses": len(witnessed),
        "witness_labels": witnessed,
        "witness_twisted_trace": -1,
        "cyclic_defect_witness": -1,
        "scope": "Finite exact lattice witnesses and boundary bookkeeping only; arbitrary-label theorem and all infinite operator arguments are separately proved in note 423. No RH certificate.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "witness_labels"}))


if __name__ == "__main__":
    main()

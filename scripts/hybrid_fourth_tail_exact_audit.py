"""Exact rational exponent and free-word certificate for note 452.

This verifies displayed finite algebra, not analytic estimates or prime moments.
Input hashes are read from disk after only CRLF/CR to LF normalization.
"""

from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/452-subquarter-padding-and-fourth-trace-stability.md"
PAPER = ROOT / "papers/kappa-feedback-cubic-boundary-paper.tex"
OUT = ROOT / "output/hybrid-fourth-tail-exact-audit.json"


def canon_binding(path):
    content = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = content.encode("utf-8")
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
        "canonical_utf8_bytes": len(data),
    }


def cubic(e):
    return 657 * e**3 - 954 * e**2 + 21 * e + 20


def cubic_derivative(e):
    return 1971 * e**2 - 1908 * e + 21


def certify():
    lo, hi = Q(16683858898627, 10**14), Q(16683858898628, 10**14)
    assert cubic(lo) > 0 > cubic(hi)
    # e is positive: this endpoint bound proves negativity throughout [lo,hi].
    derivative_upper = 1971 * hi**2 - 1908 * lo + 21
    assert derivative_upper < 0
    sigma_lo, sigma_hi = Q(11, 12) - hi / 4, Q(11, 12) - lo / 4
    theta_upper = Q(437479, 500000)
    a, r = Q(87497, 100000), Q(6249, 25000)
    assert Q(3, 4) < sigma_lo < sigma_hi < theta_upper < a < 1
    assert Q(0) < r < Q(1, 4)
    tail_upper = theta_upper - Q(1, 2) - 2 * r
    transfer_upper = theta_upper + 3 * a - 3 - 2 * r
    quarter_transfer_upper = theta_upper + 3 * a - Q(7, 2)
    assert tail_upper == -Q(62481, 500000)
    assert transfer_upper == -Q(13, 250000)
    assert quarter_transfer_upper == -Q(33, 250000)
    assert 2 * sigma_hi - Q(3, 2) < r
    # Exact identity in the free, noncommutative polynomial algebra Q<A,B>.
    # No cyclic permutation, commutativity, or sampled matrix is assumed.
    expanded = Counter()
    for j in range(4):
        expanded["A" * (3 - j) + "A" + "B" * j] += 1
        expanded["A" * (3 - j) + "B" + "B" * j] -= 1
    reduced = {word: coeff for word, coeff in expanded.items() if coeff}
    assert reduced == {"AAAA": 1, "BBBB": -1}
    return {
        "status": "PASS: finite algebra only",
        "scope": [
            "cubic root isolation by exact signs and negative derivative",
            "fixed rational line and padding exponent inequalities",
            "fourth-power telescoping identity in the free word algebra",
        ],
        "not_certified": [
            "imported source theorem and external kernels",
            "zero-free continuation or the cubic paper's analytic proof",
            "zero-tail or complete Gabor operator estimates",
            "actual prime fourth moment, proportions or RH",
        ],
        "e_root_interval": [str(lo), str(hi)],
        "sigma_interval": [str(sigma_lo), str(sigma_hi)],
        "theta_rational_upper": str(theta_upper),
        "fixed_line_a": str(a),
        "padding_exponent": str(r),
        "trace_norm_exponent_upper": str(tail_upper),
        "normalized_fourth_exponent_upper_before_logs": str(transfer_upper),
        "normalized_fourth_power_saving_after_logs": str(-transfer_upper / 2),
        "quarter_padding_exponent_upper_before_logs": str(quarter_transfer_upper),
        "free_word_identity": reduced,
        "inputs_read_and_hashed_from_disk": [canon_binding(NOTE), canon_binding(PAPER)],
        "script_read_and_hashed_from_disk": canon_binding(Path(__file__).resolve()),
    }


if __name__ == "__main__":
    result = certify()
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "padding_exponent": result["padding_exponent"],
        "fourth_exponent_before_logs": result["normalized_fourth_exponent_upper_before_logs"],
        "output": str(OUT),
    }, ensure_ascii=False))

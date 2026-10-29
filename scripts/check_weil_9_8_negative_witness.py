"""Verify the public compact negative witness for one finite comparison.

This checks the encoded congruent K block, never the classical Weil form.
Its provenance is bound by the separate source/compiler/root receipts.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re


def integer(value):
    assert isinstance(value, str) and re.fullmatch(r"0|-?[1-9][0-9]*", value)
    answer = int(value)
    assert abs(answer).bit_length() <= 4000
    return answer


def verify(data):
    assert data["schema"] == "weil-9-8-fixed-target-negative-independent-replay-v1"
    assert data["full_dimension"] == 224 and data["sector"] == "even"
    support = data["nonzero_support_indices"]
    assert support == sorted(set(support)) and all(type(i) is int and 0 <= i < 224 for i in support)
    vector = [integer(x) for x in data["integer_vector_on_support"]]
    assert len(vector) == len(support) > 0 and all(vector)
    lookup = dict(zip(support, vector))
    entries = data["principal_block_upper_triangle"]
    expected = [(i, j) for k, i in enumerate(support) for j in support[k:]]
    assert [(row[0], row[1]) for row in entries] == expected
    numerator = sum(integer(value) * lookup[i] * lookup[j] * (1 if i == j else 2)
                    for i, j, value in entries)
    assert numerator == integer(data["integer_quadratic_numerator"]) < 0
    assert hashlib.sha256(str(numerator).encode()).hexdigest() == data["quadratic_numerator_sha256"]
    norm = sum(x*x for x in vector)
    assert norm == integer(data["integer_vector_norm_squared"])
    assert data["vector_denominator_power_two"] == 512
    assert data["quadratic_denominator_power_two"] == 1024
    ratio = Fraction(numerator, norm * 2**data["target_scale_bits"])
    assert -Fraction(1, 2**79) < ratio < -Fraction(1, 2**80)
    assert data["full_q_negative_certified"] is False
    assert data["window_9_8_coercivity_certified"] is False
    return {"status": "ENCODED_FINITE_COMPARISON_STRICTLY_NEGATIVE",
            "support_size": len(support), "checked_upper_entries": len(entries),
            "negative_numerator_bits": abs(numerator).bit_length(),
            "full_weil_sign": "NOT_ESTABLISHED"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("witness", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(json.loads(args.witness.read_text(encoding="utf-8")))))


if __name__ == "__main__":
    main()

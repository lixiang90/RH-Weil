"""Exact small-grid tests for the B1i normalized common-core transfer."""

from __future__ import annotations

from fractions import Fraction

from b1g_directed_numerator_interval_audit import FIXED_SCALE
from b1i_normalized_common_core_certificate import compress, normalized_common_core


def main() -> None:
    assert compress(set()) == ()
    assert compress({2, 3, 4, 8, 10, 11}) == ((2, 5), (8, 9), (10, 12))

    # Scale 8 parent 4 maps to t-subcells 12,13,14; scale 16 parent 3 maps
    # to 12,13,14,15. Their common core therefore has exactly three cells.
    core = normalized_common_core(
        (4,),
        ((4, 300),),
        (3,),
        ((3, 400),),
    )
    assert core["common"] == frozenset({12, 13, 14})
    assert core["ranges"] == ((12, 15),)
    assert core["longest"] == (3, 12, 15)
    assert core["numerator8_lower"] == Fraction(300, FIXED_SCALE)
    assert core["numerator16_lower"] == Fraction(300, FIXED_SCALE)

    try:
        normalized_common_core((4,), (), (3,), ((3, 400),))
    except ValueError:
        pass
    else:
        raise AssertionError("mismatched index and bound ledgers were accepted")

    assert Fraction(4, 17) * Fraction(1, 20) == Fraction(1, 85)
    assert 1 / (1 - 2 * Fraction(1, 85)) == Fraction(85, 83)
    print("B1i normalized common-core exact tests passed")


if __name__ == "__main__":
    main()

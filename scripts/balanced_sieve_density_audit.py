"""Finite checks for note 221's local sieve density and exponent ledger.

This validates elementary identities only.  It is not an implementation of
the Bettin--Chandee theorem and is not evidence for RH.
"""

from __future__ import annotations

from fractions import Fraction


def local_survivors(p: int, h: int) -> int:
    """Count nonzero (a,c) mod p with a-c=h; b=d=1 is representative."""
    return sum(
        1
        for a in range(p)
        for c in range(p)
        if (a - c - h) % p == 0 and a != 0 and c != 0
    )


def check_local_density() -> None:
    for p in (3, 5, 7, 11, 13, 17, 19):
        for h in range(p):
            expected = p - 1 if h == 0 else p - 2
            actual = local_survivors(p, h)
            assert actual == expected, (p, h, actual, expected)


def check_exponent_ledger() -> None:
    # Corollary 1 contributes Y^(1 + 7/10 + 1/4) = Y^(39/20).
    assert Fraction(1) + Fraction(7, 10) + Fraction(1, 4) == Fraction(39, 20)

    # q_1,q_2 <= D^2 cost D^(14/10+1/2)=D^(19/10), and the
    # ordered Selberg pair costs D^2, for D^(39/10) in total.
    q_cost = 2 * Fraction(7, 20) * 2 + Fraction(1, 4) * 2
    assert q_cost == Fraction(19, 10)
    assert Fraction(2) + q_cost == Fraction(39, 10)

    # A fixed kappa < 1/78 preserves a positive power of Y.
    assert -Fraction(1, 20) + Fraction(39, 10) * Fraction(1, 100) < 0
    assert -Fraction(1, 20) + Fraction(39, 10) * Fraction(1, 78) == 0


def main() -> None:
    check_local_density()
    check_exponent_ledger()
    print("balanced sieve density and exponent ledger: PASS")


if __name__ == "__main__":
    main()

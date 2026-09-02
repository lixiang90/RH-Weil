"""Finite audits for note 222's two-regime critical-shell proof.

These checks cover local root counts, gcd/shift cancellation, and exponent
inequalities.  They do not implement the cited analytic sieve theorems and
are not evidence for RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


PRIMES = (3, 5, 7, 11, 13, 17, 19)


def roots_mod_p(p: int, b: int, d: int, a0: int, c0: int) -> int:
    return sum(
        1
        for k in range(p)
        if (a0 + b * k) % p == 0 or (c0 + d * k) % p == 0
    )


def check_two_form_local_roots() -> None:
    for p in PRIMES:
        for b in range(1, p):
            for d in range(1, p):
                for a0 in range(p):
                    for c0 in range(p):
                        h = (d * a0 - b * c0) % p
                        actual = roots_mod_p(p, b, d, a0, c0)
                        expected = 1 if h == 0 else 2
                        assert actual == expected, (p, b, d, a0, c0)


def check_coefficient_prime_roots() -> None:
    # If p divides b but not d, p|h forces the a-form to vanish identically;
    # otherwise only the c-form excludes one residue.
    for p in PRIMES:
        b = p
        d = 1
        for a0 in range(p):
            for c0 in range(p):
                h = (d * a0 - b * c0) % p
                actual = roots_mod_p(p, b, d, a0, c0)
                if h == 0:
                    assert actual == p
                else:
                    assert actual == 1


def check_gcd_shift_cancellation() -> None:
    # For b,d with common gcd g, the affine length is proportional to g*K
    # while the number of admissible nonzero shifts is proportional to H/g.
    for b, d, h_bound in ((9, 27, 270), (25, 125, 500), (49, 343, 686)):
        g = gcd(b, d)
        admissible = 2 * (h_bound // g)
        normalized = Fraction(admissible * g, 2 * h_bound)
        assert normalized == 1


def check_exponent_split() -> None:
    delta = Fraction(1, 10)
    kappa = Fraction(1, 100)
    moderate_saving = Fraction(1, 20) - Fraction(39, 10) * kappa
    assert moderate_saving > 0

    # epsilon is chosen after delta and kappa.
    epsilon = delta * moderate_saving / 4
    assert epsilon < delta * moderate_saving / 2

    # The extreme direct-sieve remainder has exponent -1+2*kappa_0+eps.
    kappa_0 = Fraction(1, 10)
    direct_epsilon = Fraction(1, 100)
    assert -1 + 2 * kappa_0 + direct_epsilon < 0

    # Long proper powers are negligible whenever delta<1/2.
    assert delta - Fraction(1, 2) < 0


def main() -> None:
    check_two_form_local_roots()
    check_coefficient_prime_roots()
    check_gcd_shift_cancellation()
    check_exponent_split()
    print("unbalanced critical two-regime sieve audit: PASS")


if __name__ == "__main__":
    main()

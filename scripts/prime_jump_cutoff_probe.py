#!/usr/bin/env python3
"""[E] Bounded actual prime-jump choices of a matched Abel cutoff.

Run: python -B scripts/prime_jump_cutoff_probe.py

For sigma=.25 and dyadic m=4,6,8,10,12,16, integer trial division finds
the first prime q in (Y,2Y). Both sources use exactly the same integer
cutoff q-1 or q. Continuum integrals use the analytic incomplete-gamma
formula evaluated with mpmath at 50 digits; this is not interval arithmetic.
The selected cutoff maximizes the displayed floating-point absolute mass.
Any rigorous cutoff choice must use exact quantities or certified intervals.
No general mass lower bound or infinite-frequency tail estimate is certified
by these finite numerical samples. No files are written.
"""

import math
import sys

sys.dont_write_bytecode = True

import mpmath as mp
import numpy as np

from abel_mass_discrepancy_probe import continuum_mass, prime_power_ledger


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, math.isqrt(n)+1, 2))


def first_prime_above(Y):
    candidate = Y+1
    while candidate < 2*Y:
        if is_prime(candidate):
            return candidate
        candidate += 1
    raise AssertionError("No prime found in the bounded search interval.")


def von_mangoldt_mp(n):
    """Independent trial-factorization coefficient for the small checks."""
    for factor in range(2, math.isqrt(n)+1):
        if n % factor == 0:
            rest = n
            while rest % factor == 0:
                rest //= factor
            return mp.log(factor) if rest == 1 else mp.mpf(0)
    return mp.log(n) if n >= 2 else mp.mpf(0)


def mass_float(n, lam, Y, N):
    count = np.searchsorted(n, N, side="right")
    active_n = n[:count]
    weights = lam[:count]*np.exp(-.25*np.log(active_n)-active_n/Y)
    A = np.sum(weights, dtype=np.longdouble)
    B = np.longdouble(str(continuum_mass(.25, Y, N)))
    return A-B, count


def mass_mp_small(Y, N):
    A = mp.fsum(von_mangoldt_mp(n)*mp.power(n, mp.mpf("-.25"))
                *mp.exp(-mp.mpf(n)/Y) for n in range(2, N+1))
    return A-continuum_mass(.25, Y, N)


def jump_formula_mp(Y, q):
    a = mp.mpf(".75")
    coefficient = mp.log(q)*mp.power(q, mp.mpf("-.25"))*mp.exp(-mp.mpf(q)/Y)
    continuum_jump = mp.power(Y, a)*mp.gammainc(
        a, mp.mpf(q-1)/Y, mp.mpf(q)/Y)
    return coefficient, continuum_jump, coefficient-continuum_jump


def main():
    mp.mp.dps = 50
    m_values = (4, 6, 8, 10, 12, 16)
    qs = {m: first_prime_above(2**m) for m in m_values}
    assert max(qs.values()) <= 131072
    for m, q in qs.items():
        Y = 2**m
        assert Y < q < 2*Y and is_prime(q)
        assert not any(is_prime(n) for n in range(Y+1, q))
    n, lam = prime_power_ledger(max(qs.values()))
    print("[E] bounded matched-cutoff mass probe; sigma=.25")
    print("Prime identities and first-prime searches use exact integer trial division.")
    print(f"largest_integer={max(qs.values())}; prime_power_terms={len(n)}; "
          f"longdouble_explicit_mantissa_bits={np.finfo(np.longdouble).nmant}")
    print("Cutoff selection is floating-point, not a certified maximizer. "
          "Gamma formulas are evaluated at 50 digits, not interval-certified.")
    print("m,Y,q,prime_powers_through_q,M_qminus1,M_q,aq,"
          "jump_from_gamma,jump_over_aq,float_jump_absolute_error,"
          "selected_N,selected_N_over_Y,selected_absM_over_YminusSigma_logY,"
          "selected_absM_over_aq")
    small_checks = []
    for m in m_values:
        Y, q = 2**m, qs[m]
        before, _ = mass_float(n, lam, Y, q-1)
        after, count = mass_float(n, lam, Y, q)
        aq, continuum_jump, jump = jump_formula_mp(Y, q)
        measured_jump = mp.mpf(str(after-before))
        jump_error = abs(measured_jump-jump)
        selected_N, selected_mass = ((q-1, before) if abs(before) >= abs(after)
                                    else (q, after))
        scale = mp.power(Y, mp.mpf("-.25"))*mp.log(Y)
        normalized = abs(mp.mpf(str(selected_mass)))/scale
        atom_normalized = abs(mp.mpf(str(selected_mass)))/aq
        assert jump > 0 and jump/aq > mp.mpf(".5")
        assert atom_normalized > mp.mpf(".25")
        print(f"{m},{Y},{q},{count},{before:.16g},{after:.16g},"
              f"{mp.nstr(aq, 16)},{mp.nstr(jump, 16)},"
              f"{mp.nstr(jump/aq, 14)},{mp.nstr(jump_error, 7)},"
              f"{selected_N},{selected_N/Y:.12g},"
              f"{mp.nstr(normalized, 14)},{mp.nstr(atom_normalized, 14)}")
        if m in (4, 6):
            before_mp, after_mp = mass_mp_small(Y, q-1), mass_mp_small(Y, q)
            mp_selected = q-1 if abs(before_mp) >= abs(after_mp) else q
            formula_error = abs((after_mp-before_mp)-jump)
            errors = (abs(mp.mpf(str(before))-before_mp),
                      abs(mp.mpf(str(after))-after_mp))
            assert formula_error < mp.mpf("1e-45")
            assert max(errors) < mp.mpf("1e-11")
            assert mp_selected == selected_N
            small_checks.append((m, before_mp, after_mp, formula_error,
                                 max(errors), mp_selected))
    print("Independent small-case 50-digit direct sums "
          "(trial-factorization coefficients):")
    print("m,M_qminus1_mp,M_q_mp,jump_identity_residual,"
          "largest_double_mass_error,matching_selected_N")
    for m, before, after, residual, error, selected in small_checks:
        print(f"{m},{mp.nstr(before, 24)},{mp.nstr(after, 24)},"
              f"{mp.nstr(residual, 6)},{mp.nstr(error, 7)},{selected}")
    print("PASS bounded comparisons. General prime-jump guarantees and "
          "full J4 tail bounds require their separate analytic proofs.")


if __name__ == "__main__":
    main()

"""Bounded checks for notes 515-517, with explicit scope.

SymPy checks exact polynomial orbit and jet identities in a hypothetical
multiple-zero model. It does not exhibit a multiple zero of zeta. mpmath
checks actual prime weights, the quarter-Gamma constant and the Mellin
division sign on a Gaussian ODE input. Floating checks are not interval or
Lean proofs. Analytic kernel and convergence theorems are proved in the notes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTES = (
    "notes/515-f1-common-central-mixed-kernels.md",
    "notes/516-f1-global-mixed-radical-and-mellin-jets.md",
    "notes/517-f1-weak-observable-limit-and-source-cutoffs.md",
)


def lf_hash(path):
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def exact_checks():
    s = sp.Symbol("s")
    rho = sp.Rational(1, 3) + 2 * sp.I
    orbit = (rho, sp.conjugate(rho), 1-rho, 1-sp.conjugate(rho))
    q = sp.expand(sp.prod(lam-s for lam in orbit))
    checks = 0
    assert sp.Poly(q, s).domain == sp.QQ
    checks += 1
    assert sp.expand(q.subs(s, 1-s)-q) == 0
    checks += 1
    # Mock order-two orbit: value-only radical versus order-two source jets.
    original = s*(s-1)*q**2
    divided = sp.cancel(original/q)
    assert sp.expand(q*divided-original) == 0
    checks += 1
    assert divided.subs(s, 0) == divided.subs(s, 1) == 0
    checks += 1
    for lam in orbit:
        assert sp.simplify(original.subs(s, lam)) == 0
        assert sp.simplify(sp.diff(original, s).subs(s, lam)) == 0
        assert sp.simplify(divided.subs(s, lam)) == 0
        assert sp.simplify(sp.diff(divided, s).subs(s, lam)) != 0
        checks += 4
    # Sharp conjugation sends D to -D-1, fixing the exact degree operator.
    d = sp.Symbol("d")
    assert sp.expand((-d-1)**2+(-d-1)-(d**2+d)) == 0
    checks += 1
    return {"checks": checks, "orbit_polynomial": str(q),
            "model_is_an_actual_zeta_multiple_zero": False}


def bump(t, radius):
    if abs(t) >= radius:
        return mp.mpf(0)
    return mp.exp(-1/(1-(t/radius)**2))


def eta(t, radius):
    return (1-3*(t/radius)**2)*bump(t, radius)


def prime_density(p, t, radius):
    """Locally finite formula; no infinite series is silently truncated."""
    length = mp.log(p)
    top = int(mp.floor((abs(t)+radius)/length))
    return length*mp.fsum(
        p**(-mp.mpf(n)/2)*(eta(t-n*length, radius)+eta(t+n*length, radius))
        for n in range(1, top+1)
    )


def numerical_checks():
    mp.mp.dps = 40
    errors = []
    count = 0

    def close(left, right, tol=mp.mpf("1e-28")):
        nonlocal count
        error = abs(left-right)
        assert error < tol, (left, right, error)
        errors.append(error)
        count += 1

    # Exact Euler weight multiplier versus a finite geometric expansion.
    for p in (2, 3, 17):
        length, a = mp.log(p), 1/mp.sqrt(p)
        for tau in (mp.mpf(0), mp.mpf("0.37"), mp.mpf("2.1")):
            closed = 2*length*a*(mp.cos(length*tau)-a)/(
                1-2*a*mp.cos(length*tau)+a*a)
            series = 2*length*mp.fsum(
                a**n*mp.cos(n*length*tau) for n in range(1, 250))
            tail = 2*length*a**250/(1-a)
            assert abs(closed-series) < tail+mp.mpf("1e-38")
            close(closed, series)
        tau0 = mp.acos(a)/length
        close(2*length*a*(mp.cos(length*tau0)-a)/(
            1-2*a*mp.cos(length*tau0)+a*a), 0)

    # Quarter-Gamma normalization, including the original identity constant.
    gamma_zero = mp.log(mp.pi)-mp.digamma(mp.mpf(1)/4)
    close(gamma_zero, mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi))
    assert gamma_zero > 0

    # Detector for a signed compact input with log(2) < 2R: new general case.
    radius, cutoff, p = mp.mpf("0.8"), mp.mpf("2.4"), 2
    length, a = mp.log(p), 1/mp.sqrt(p)
    top = int(mp.floor((radius+cutoff)/length))
    breaks = {-cutoff, cutoff, mp.mpf(0)}
    for n in range(1, top+1):
        for sign in (-1, 1):
            for edge in (-radius, radius):
                point = sign*n*length+edge
                if -cutoff < point < cutoff:
                    breaks.add(point)
    breaks = sorted(breaks)
    density = lambda t: prime_density(p, t, radius)
    zeta = lambda t: bump(t, cutoff)*density(t)
    square_charge = mp.quad(lambda t: density(t)*zeta(t), breaks)
    euler_charge = 2*length*mp.fsum(
        a**n*mp.quad(lambda t: eta(n*length-t, radius)*zeta(t), breaks)
        for n in range(1, top+1))
    assert square_charge > mp.mpf("1e-5")
    close(square_charge, euler_charge)

    # Local support stability: later primes are exactly absent on this window.
    window = mp.mpf(1)
    early, late = (2, 3, 5), (7, 11, 13, 17, 19, 23, 29)
    assert max(early) < mp.exp(radius+window) < min(late)
    for t in (-window, -mp.mpf("0.4"), mp.mpf(0), mp.mpf("0.4"), window):
        first = mp.fsum(prime_density(p, t, radius) for p in early)
        enlarged = mp.fsum(prime_density(p, t, radius) for p in early+late)
        assert first == enlarged
        count += 1
    escaped = prime_density(29, mp.log(29), radius)
    assert escaped > 0
    count += 1

    # Division sign and both endpoint primitives, on an explicit Schwartz ODE.
    lam = mp.mpf(1)/3+2j
    g = lambda t: mp.exp(-t*t)
    f = lambda t: (lam-2*t)*g(t)
    total = mp.quad(lambda t: mp.exp(lam*t)*f(t), [-mp.inf, 0, mp.inf])
    close(total, 0)
    for t in (-2, 0, 2):
        left = mp.exp(-lam*t)*mp.quad(
            lambda u: mp.exp(lam*u)*f(u), [-mp.inf, t])
        right = -mp.exp(-lam*t)*mp.quad(
            lambda u: mp.exp(lam*u)*f(u), [t, mp.inf])
        close(left, g(t))
        close(right, g(t))
    for s in (mp.mpf("0.2"), mp.mpc("0.8", "1.1")):
        mf = mp.quad(lambda t: mp.exp(s*t)*f(t), [-mp.inf, 0, mp.inf])
        mg = mp.sqrt(mp.pi)*mp.exp(s*s/4)
        close(mf, (lam-s)*mg)

    return {
        "checks": count, "working_decimal_digits": mp.mp.dps,
        "maximum_observed_error": mp.nstr(max(errors), 20),
        "non_small_support_detector_charge": mp.nstr(square_charge, 24),
        "local_support_threshold": mp.nstr(mp.exp(radius+window), 24),
        "late_prime_29_charge_at_its_logarithm": mp.nstr(escaped, 24),
        "floating_diagnostics_are_interval_or_lean_proofs": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "schema": "rh-weil-central-mixed-kernel-diagnostics-v1",
        "status": "PASS",
        "source_sha256_normalized_lf": {n: lf_hash(ROOT/n) for n in NOTES},
        "exact_hypothetical_orbit_checks": exact_checks(),
        "bounded_floating_diagnostics": numerical_checks(),
        "external_simple_zero_theorem_is_reproved_here": False,
        "global_hh_completion_is_computationally_certified": False,
    }
    payload = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8", newline="\n")
    print(payload, end="")


if __name__ == "__main__":
    main()

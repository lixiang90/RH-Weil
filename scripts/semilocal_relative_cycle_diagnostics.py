"""Bounded floating diagnostics for notes 511-512, not a proof certificate.

The Gaussian source and log test functions below are Schwartz, not compactly
supported. They check the normalization and finite-place signs only. The
compact double-moment countertests and trace-class claims are proved in prose.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
NOTES = (
    "notes/511-f1-semilocal-fourier-inversion-cycle.md",
    "notes/512-f1-finite-place-double-moment-sign-test.md",
)


def run() -> dict:
    mp.mp.dps = 45
    checks = []

    def check(label, actual, expected, tolerance=mp.mpf("1e-30")):
        error = abs(actual - expected)
        assert error < tolerance, (label, mp.nstr(error, 20))
        checks.append({"label": label, "absolute_error": mp.nstr(error, 18)})

    primes = (2, 5)

    def finite_phase(p, tau):
        a, angle = mp.mpf(p)**(-mp.mpf(1)/2), tau * mp.log(p)
        return (1 - a * mp.exp(-1j * angle)) / (1 - a * mp.exp(1j * angle))

    def real_phase(tau):
        z = mp.mpf(1)/4 + 1j * tau/2
        return mp.exp(1j * tau * mp.log(mp.pi)) * mp.gamma(z.conjugate())/mp.gamma(z)

    def common_phase(tau):
        return real_phase(tau) * mp.fprod(finite_phase(p, tau) for p in primes)

    def density(tau):
        value = mp.re(mp.digamma(mp.mpf(1)/4 + 1j*tau/2)) - mp.log(mp.pi)
        for p in primes:
            w = mp.mpf(p)**(-mp.mpf(1)/2) * mp.exp(1j*tau*mp.log(p))
            value -= 2 * mp.log(p) * mp.re(w/(1-w))
        return value

    for tau in map(mp.mpf, ["-100", "-9", "-1", "-0.1", "0", "0.1", "1", "9", "100"]):
        check(f"common-unitarity:{tau}", abs(common_phase(tau)), 1)
        check(f"common-log-derivative:{tau}", 1j*mp.diff(common_phase, tau)/common_phase(tau), density(tau))

    # phi(x)=exp(-pi*x^2) is fixed by the actual real Fourier transform.
    # The finite unit balls are also fixed by their self-dual transforms.
    # The Mellin integral is evaluated directly; the periodization denominator
    # is the absolutely convergent identity in note 511.
    def source_mellin(s):
        integral = mp.quad(lambda r: mp.exp(-mp.pi*r*r)*r**(s-1), [0, 1, mp.inf])
        return 2*integral/mp.fprod(1-mp.mpf(p)**(-s) for p in primes)

    for tau in map(mp.mpf, ["0", "0.4", "2", "6"]):
        s = mp.mpf(1)/2 - 1j*tau
        check(f"self-dual-source-mellin:{tau}", source_mellin(s)/source_mellin(1-s), common_phase(tau),
              tolerance=mp.mpf("1e-20"))

    # Compare the finite spectral density to the arithmetic prime-power sum.
    # Gaussian Schwartz tails justify both integrals/series in this diagnostic.
    for sigma in map(mp.mpf, ["0.6", "1.1"]):
        for zero_at_origin in (False, True):
            def eta(t):
                return (t*t if zero_at_origin else 1)*mp.exp(-t*t/(2*sigma*sigma))

            def phi(tau):
                base = mp.sqrt(2*mp.pi)*sigma*mp.exp(-sigma*sigma*tau*tau/2)
                return base*sigma*sigma*(1-sigma*sigma*tau*tau) if zero_at_origin else base

            for p in (2, 5, 11):
                a, length = mp.mpf(p)**(-mp.mpf(1)/2), mp.log(p)

                def finite_b(tau):
                    w = a*mp.exp(1j*tau*length)
                    return -2*length*mp.re(w/(1-w))

                breaks = [mp.mpf(j)/2 for j in range(81)] + [mp.inf]
                spectral = -mp.quad(lambda tau: finite_b(tau)*phi(tau)/mp.pi, breaks)
                arithmetic = 2*length*mp.fsum(a**n*eta(n*length) for n in range(1, 301))
                check(f"finite-charge:{p}:sigma={sigma}:eta0={not zero_at_origin}", spectral, arithmetic)

    norm_samples = 0
    for p in (3, 7, 11, 97):
        a = mp.mpf(p)**(-mp.mpf(1)/2)
        tau = mp.acos(a)/mp.log(p)
        check(f"natural-inclusion-norm-attained:{p}", abs(finite_phase(p, tau)-1), 2*a)
        for j in range(129):
            tau = 2*mp.pi*j/(128*mp.log(p))
            assert abs(finite_phase(p, tau)-1) <= 2*a + mp.mpf("1e-40")
            norm_samples += 1

    expected_zero_density = (mp.euler + mp.pi/2 + 3*mp.log(2) + mp.log(mp.pi)
                            + 2*mp.fsum(mp.log(p)*mp.mpf(p)**(-mp.mpf(1)/2)/
                                        (1-mp.mpf(p)**(-mp.mpf(1)/2)) for p in primes))
    check("fixed-S-density-at-zero", -density(0), expected_zero_density)
    assert expected_zero_density > 0

    return {
        "schema": "rh-weil-semilocal-relative-cycle-diagnostics-v1",
        "status": "PASS",
        "precision_decimal_digits": mp.mp.dps,
        "identity_check_count": len(checks),
        "natural_inclusion_norm_sample_count": norm_samples,
        "maximum_identity_absolute_error": mp.nstr(max(mp.mpf(c["absolute_error"]) for c in checks), 18),
        "checks": checks,
        "source_lf_sha256": {
            path: hashlib.sha256((ROOT/path).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
            for path in NOTES
        },
        "limits": [
            "Floating arithmetic, not interval arithmetic or a Lean/kernel certificate.",
            "Schwartz Gaussian diagnostics do not prove the compact-test sign obstruction.",
            "No trace-class admission, quotient descent, global negativity or RH is certified by this script.",
            "No uniform bound or limit as S increases is tested.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(json.dumps({k: result[k] for k in (
            "status", "identity_check_count", "natural_inclusion_norm_sample_count",
            "maximum_identity_absolute_error")}, ensure_ascii=False))
    else:
        print(rendered, end="")

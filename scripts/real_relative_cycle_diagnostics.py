"""Numerical diagnostics for notes 509-510, not an interval or Lean proof.

Checks independent kernel integrals, the actual Mellin gamma phase, and
time/spectral pairings including the value at the identity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]


def run() -> dict:
    mp.mp.dps = 45
    checks = []

    def check(label, actual, expected, tolerance=mp.mpf("1e-32")):
        error = abs(actual - expected)
        assert error < tolerance, (label, mp.nstr(error, 20))
        checks.append({"label": label, "absolute_error": mp.nstr(error, 18)})

    def phase(tau):
        z = mp.mpf(1) / 4 + 1j * tau / 2
        return mp.exp(1j * tau * mp.log(mp.pi)) * mp.gamma(z.conjugate()) / mp.gamma(z)

    def conductor(tau):
        return mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * tau / 2)) - mp.log(mp.pi)

    for tau in map(mp.mpf, ["-100", "-9", "-1", "-0.1", "0", "0.1", "1", "9", "100"]):
        check(f"unitarity:{tau}", abs(phase(tau)), 1)
        check(f"log-derivative-sign:{tau}", 1j * mp.diff(phase, tau) / phase(tau), conductor(tau))

    for a in map(mp.mpf, ["-2", "-0.5", "0.5", "2"]):
        for lam in map(mp.mpf, ["0.5", "1", "2"]):
            c = a - 1
            primitive = 2 * mp.si(2 * mp.pi * c * lam**2) / (mp.pi * c)

            def diagonal_in_original_coordinate(x):
                # Kernel (R_Lambda S_a)(x,x), not its Si primitive.
                z = (1 - 1 / a) * x
                sinc = 2 * lam if z == 0 else mp.sin(2 * mp.pi * lam * z) / (mp.pi * z)
                return sinc / abs(a)

            end = abs(a) * lam
            breaks = [-end + 2 * end * j / 32 for j in range(33)]
            check(f"hard-kernel:{a}:{lam}", mp.quad(diagonal_in_original_coordinate, breaks), primitive)

        for radius in map(mp.mpf, ["0.75", "2", "5"]):
            diagonal = lambda x: radius / abs(a) * mp.exp(
                -mp.pi * radius**2 * (x - x / a)**2
                -mp.pi * (x / a)**2 / radius**2
            )
            primitive = 1 / mp.sqrt((1 - a)**2 + radius**-4)
            check(
                f"gaussian-kernel:{a}:{radius}",
                mp.quad(diagonal, [-mp.inf, 0, mp.inf]),
                primitive,
            )

    bound_checks = 0
    for a in map(mp.mpf, ["-5", "-2", "-0.5", "0.5", "2", "5"]):
        for lam in map(mp.mpf, ["1", "2", "4", "8", "16"]):
            c = a - 1
            hard = 2 * mp.si(2 * mp.pi * c * lam**2) / (mp.pi * c)
            assert abs(hard - 1 / abs(c)) <= 2 / (mp.pi**2 * c**2 * lam**2)
            gaussian = 1 / mp.sqrt(c**2 + lam**-4)
            assert abs(gaussian - 1 / abs(c)) <= lam**-4 / (2 * abs(c)**3)
            bound_checks += 2

    pairings = []
    for sigma in map(mp.mpf, ["0.4", "0.8", "1.3"]):
        for vanishes_at_zero in (False, True):
            eta_zero = 0 if vanishes_at_zero else 1

            def eta(t):
                return (t**2 if vanishes_at_zero else 1) * mp.exp(-t**2 / (2 * sigma**2))

            def eta_hat(tau):
                base = mp.sqrt(2 * mp.pi) * sigma * mp.exp(-sigma**2 * tau**2 / 2)
                return base * sigma**2 * (1 - sigma**2 * tau**2) if vanishes_at_zero else base

            def real_integrand(t):
                if t == 0:
                    return 0 if vanishes_at_zero else mp.mpf(3) / 4
                return (mp.exp(-t / 2) * eta(t) - mp.exp(-2 * t) * eta_zero) / (-mp.expm1(-2 * t))

            real_value = (
                (mp.log(mp.pi) + mp.euler) * eta_zero
                + 2 * mp.quad(real_integrand, [0, mp.mpf("0.5"), 1, 3, 8, mp.inf])
            )
            spectral_value = -mp.quad(
                lambda tau: conductor(tau) * eta_hat(tau) / mp.pi,
                [0, 1, 4, 12, 40, mp.inf],
            )
            label = f"full-time-spectral-pairing:{sigma}:eta0={eta_zero}"
            check(label, spectral_value, real_value, mp.mpf("1e-30"))
            pairings.append({
                "sigma": str(sigma),
                "eta_at_zero": eta_zero,
                "time_pairing": mp.nstr(real_value, 35),
                "spectral_pairing": mp.nstr(spectral_value, 35),
                "compact_support": False,
            })

    paths = [
        "notes/509-f1-real-cutoff-kernel-and-relative-boundary.md",
        "notes/510-f1-real-fourier-inversion-relative-cycle.md",
    ]
    return {
        "schema": "rh-weil-real-relative-cycle-numerical-diagnostics-v1",
        "precision_decimal_digits": mp.mp.dps,
        "identity_checks": len(checks),
        "finite_bound_checks": bound_checks,
        "maximum_identity_absolute_error": mp.nstr(
            max(mp.mpf(item["absolute_error"]) for item in checks), 18
        ),
        "checks": checks,
        "time_spectral_pairings": pairings,
        "source_sha256_normalized_lf": {
            path: hashlib.sha256((ROOT / path).read_text(encoding="utf-8").encode()).hexdigest()
            for path in paths
        },
        "limits": [
            "Floating point quadrature; no outward-rounded interval certificate.",
            "Does not prove the Schatten ideal, HH1 descent, or infinite source comparisons.",
            "Gaussian eta tests are noncompact diagnostic functions, not the fixed prime-gap mixed pair.",
            "No Lean proof or RH, zero-free-region, or zero-proportion theorem.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "reviews/2026-10-11/f1-real-relative-cycle-diagnostics.json",
    )
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f'{result["identity_checks"]} identities and {result["finite_bound_checks"]} finite bounds passed.')
    print(f'Maximum numerical identity error: {result["maximum_identity_absolute_error"]}')


if __name__ == "__main__":
    main()

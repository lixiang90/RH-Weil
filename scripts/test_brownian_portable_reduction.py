"""Regression for version-independent B1e/B1f binary64 component masses.

The small hexadecimal input fixture records the original B1e base atoms,
not 35,000 expanded response coefficients.  Exact Fraction sums independently
check the reference masses.  The unchanged full B1e and B1f audits still
verify the original rational energy and denominator inequalities.
"""

from __future__ import annotations

from fractions import Fraction

from b1f_base_coefficient_interval_audit import audited_centered_component
from formal_lag_response import (
    FormalLag,
    complex_fsum,
    degree_two_centered_response_channel_maps,
)


PRIME_ATOMS = (
    "0x1.6cb2c72407baep-2", "0x1.8ff480a061c3ap-2",
    "0x1.76c6bee500a8ap-3", "0x1.4fdc2130ac551p-2",
    "0x1.02701bcd701ddp-2", "0x1.2bf1172829b61p-4",
    "0x1.86e92644af8afp-4",
)
CONTINUUM_ATOMS = (
    "-0x1.b38d040e84ea3p-6", "-0x1.dd2577aae31c9p-2",
    "-0x1.053897f2f314ep-1", "-0x1.0b70400baf956p-1",
    "-0x1.eb016dc3a3246p-2",
)


def exact_component_sum(values: list[complex]) -> complex:
    return complex(
        float(sum((Fraction.from_float(v.real) for v in values), Fraction(0))),
        float(sum((Fraction.from_float(v.imag) for v in values), Fraction(0))),
    )


def main() -> None:
    prime = [complex(float.fromhex(v) / 2) for v in PRIME_ATOMS for _ in (0, 1)]
    continuum = [complex(float.fromhex(CONTINUUM_ATOMS[0]))] + [
        complex(float.fromhex(v) / 2) for v in CONTINUUM_ATOMS[1:] for _ in (0, 1)
    ]
    for values, expected in (
        (prime, "0x1.adc35ce40f258p+0"),
        (continuum, "-0x1.00962cb5967c8p+1"),
        (prime + continuum, "-0x1.4da3f21c774e2p-2"),
    ):
        reference = exact_component_sum(values)
        assert reference.real.hex() == expected
        assert complex_fsum(iter(values)) == reference
        assert complex_fsum(reversed(values)) == reference
    legacy_mass = 0j
    for value in prime + continuum:
        legacy_mass += value
    assert legacy_mass.real.hex() == "-0x1.4da3f21c774e6p-2"
    assert legacy_mass != complex_fsum(prime + continuum)
    cancellation = [complex(1e16, -1e16), complex(1, 2), complex(-1e16, 1e16)]
    assert complex_fsum(cancellation) == exact_component_sum(cancellation) == 1 + 2j
    assert complex_fsum([]) == 0j

    # Exercise the production reducer and the independent B1f replay on a
    # small cancellation-sensitive channel, without the costly full audit.
    zero = FormalLag.zero(0)
    values = [complex(0.1), complex(0.2), complex(-0.3)]
    component = {FormalLag.prime(p, 0): v for p, v in zip((2, 3, 5), values)}
    expected_mass = exact_component_sum(values)
    factorization = degree_two_centered_response_channel_maps(
        {"test": component}, spectral_bound=1.0, rho=1 / 3,
    )
    assert factorization["total_mass"] == expected_mass
    assert factorization["component_masses"]["test"] == expected_mass
    # Use a nonzero mass here: a near-zero origin atom can be pruned, which
    # would hide a wrong legacy reduction in the B1f replay test.
    component = {FormalLag.prime(p, 0): complex(v)
                 for p, v in zip((2, 3, 5), (0.1, 0.2, 0.3))}
    expected_mass = exact_component_sum(list(component.values()))
    centered, certified_error = audited_centered_component(component, zero)
    assert centered[zero] == -expected_mass
    exact = {lag: Fraction.from_float(v.real) for lag, v in component.items()}
    exact[zero] = -sum(exact.values(), Fraction(0))
    tv = sum(
        (abs(exact.get(lag, Fraction(0)) -
             Fraction.from_float(centered.get(lag, 0j).real))
         for lag in set(exact) | set(centered)),
        Fraction(0),
    )
    assert tv <= certified_error
    print("Portable Brownian component reduction passed")
    print("[scope] deterministic finite surrogate/replay; unchanged certificate bounds")


if __name__ == "__main__":
    main()

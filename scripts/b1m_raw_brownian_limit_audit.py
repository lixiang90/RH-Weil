"""Finite diagnostics for Note 255's universal raw Brownian limit law.

The probability normalization and weak limit are proved analytically in the
note.  Numerical integrations here only evaluate the frozen 18-component core.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60
LOG_TWO = mp.log(2)
COMMON_RANGES = (
    (mp.mpf(732) / 200, mp.mpf(1239) / 200),
    (mp.mpf(29368) / 200, mp.mpf(29560) / 200),
    (mp.mpf(39090) / 200, mp.mpf(39540) / 200),
    (mp.mpf(41048) / 200, mp.mpf(41271) / 200),
    (mp.mpf(57468) / 200, mp.mpf(57738) / 200),
    (mp.mpf(62316) / 200, mp.mpf(62368) / 200),
    (mp.mpf(64480) / 200, mp.mpf(64548) / 200),
    (mp.mpf(83064) / 200, mp.mpf(83406) / 200),
    (mp.mpf(92196) / 200, mp.mpf(92520) / 200),
    (mp.mpf(101208) / 200, mp.mpf(101997) / 200),
    (mp.mpf(110841) / 200, mp.mpf(111184) / 200),
    (mp.mpf(113264) / 200, mp.mpf(113760) / 200),
    (mp.mpf(121797) / 200, mp.mpf(122032) / 200),
    (mp.mpf(135168) / 200, mp.mpf(135252) / 200),
    (mp.mpf(136852) / 200, mp.mpf(137199) / 200),
    (mp.mpf(148074) / 200, mp.mpf(148912) / 200),
    (mp.mpf(151857) / 200, mp.mpf(151892) / 200),
    (mp.mpf(152500) / 200, mp.mpf(152836) / 200),
)


def limit_density(value: mp.mpf) -> mp.mpf:
    if value == 0:
        return mp.mpf(0)
    return (1 - mp.cos(value * LOG_TWO)) ** 2 / (
        mp.pi * LOG_TWO * value**2
    )


def main() -> None:
    # Analytically, 2 I(a) - I(2a)/2 = pi*a for
    # I(b)=integral_R (1-cos(bt))/t^2 dt=pi*|b|.
    analytic_numerator_mass = 2 * mp.pi * LOG_TWO - (
        mp.pi * 2 * LOG_TWO / 2
    )
    analytic_total_mass = analytic_numerator_mass / (mp.pi * LOG_TWO)
    if analytic_total_mass != 1:
        raise AssertionError("limit-density analytic normalization failed")

    component_masses = tuple(
        mp.quad(limit_density, [lower, upper])
        for lower, upper in COMMON_RANGES
    )
    positive_core_mass = mp.fsum(component_masses)
    reflected_core_mass = 2 * positive_core_mass
    if not mp.mpf("0.18173") < positive_core_mass < mp.mpf("0.18175"):
        raise AssertionError("frozen common-core limit mass changed")
    if not component_masses[0] > mp.mpf("0.18160"):
        raise AssertionError("first component no longer carries the main raw mass")
    if not reflected_core_mass < 1:
        raise AssertionError("reflected core exceeded total probability mass")

    print("analytic_total_mass=" + mp.nstr(analytic_total_mass, 10))
    print("positive_common_core_mass=" + mp.nstr(positive_core_mass, 20))
    print("reflected_common_core_mass=" + mp.nstr(reflected_core_mass, 20))
    print("first_component_mass=" + mp.nstr(component_masses[0], 20))
    print("remaining_components_mass=" + mp.nstr(mp.fsum(component_masses[1:]), 20))
    print("B1m raw Brownian limit diagnostics passed")
    print("[scope] limit law is [T]; common-core decimal integration is [E]")


if __name__ == "__main__":
    main()

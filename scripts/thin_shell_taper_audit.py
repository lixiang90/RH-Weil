"""Finite physical endcap and tapered-Poisson evidence for note 345."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

from alternating_ratio_cluster_audit import prime_power_atoms
from free_variable_poisson_audit import (
    continuous_average, continuous_kernel, overlap, poisson_case,
)


@lru_cache(None)
def divisor_count(n: int) -> int:
    root = math.isqrt(n)
    return 2 * sum(n % a == 0 for a in range(1, root + 1)) - (root * root == n)


def endcap_audit(limit: int) -> dict:
    y, length, radius, delta = limit ** .75, math.log(limit), math.sqrt(limit), limit ** -.25
    lower, upper = math.ceil(.7 * y), math.floor(1.3 * y)
    atoms = [a for a in prime_power_atoms(upper) if lower <= a.n <= upper]
    products = defaultdict(list)
    for a in atoms:
        for d in atoms:
            products[a.n * d.n].append((a, d))
    center = continuous_average(radius)
    actual_change = absolute_change = divisor_majorant = 0.0
    cap_terms = candidate_products = 0
    for b in atoms:
        for c in atoms:
            bc = b.n * c.n
            caps = [
                (bc * math.exp((radius - delta) / limit), bc * math.exp(radius / limit)),
                (bc * math.exp(-radius / limit), bc * math.exp(-(radius - delta) / limit)),
            ]
            candidates = {n for lo, hi in caps for n in range(math.ceil(lo), math.floor(hi) + 1)}
            candidate_products += len(candidates)
            for n in sorted(candidates):
                t = limit * math.log(n / bc)
                assert radius - delta - 1e-10 <= abs(t) <= radius + 1e-10
                s = min(1., max(0., (radius - abs(t)) / delta))
                factor = abs(float(continuous_kernel(t)) - center) * (1 - 3*s*s + 2*s*s*s)
                decompositions = products.get(n, [])
                assert len(decompositions) <= divisor_count(n)
                # Pointwise finite majorant behind note 345-(1); no asymptotic constant fitted.
                bc_weight = b.log_prime * c.log_prime / math.sqrt(bc)
                divisor_majorant += (
                    bc_weight * math.log(upper)**2 / lower
                    * divisor_count(n) * factor / (16 * math.pi**4)
                )
                for a, d in decompositions:
                    if a.n == b.n or c.n == d.n or n == bc:
                        continue
                    weight = (
                        a.log_prime * b.log_prime * c.log_prime * d.log_prime
                        / (16 * math.pi**4 * math.sqrt(n * bc))
                    )
                    response = float(continuous_kernel(t)) - center
                    change = (weight * float(overlap(a.n, b.n, c.n, d.n, length))
                              * response * (1 - 3*s*s + 2*s*s*s))
                    actual_change += change
                    absolute_change += abs(change)
                    cap_terms += 1
    assert abs(actual_change) <= absolute_change + 1e-12
    assert absolute_change <= divisor_majorant + 1e-12
    return dict(X=limit, delta=delta, atom_count=len(atoms),
                ordered_masked_cap_terms=cap_terms,
                candidate_integer_products=candidate_products,
                actual_taper_change=actual_change, absolute_taper_change=absolute_change,
                finite_divisor_majorant=divisor_majorant,
                scope="finite weighted endcaps; not an asymptotic divisor estimate")


def main():
    result = dict(
        scope="E only; does not certify the all-outer-variable tail bound",
        endcaps=[endcap_audit(x) for x in (100, 400, 1600)],
        tapered_poisson=[
            poisson_case("tapered_no_integer_endpoint", 5, 67, 71, 73, True),
            poisson_case("tapered_integer_cell_endpoint", 7, 67, 71, 73, True),
            poisson_case("tapered_ratio_diagonal_deletion", 9, 73, 81, 73, True),
        ],
    )
    root = Path(__file__).resolve().parents[1]
    target = root / "reviews/2026-09-08/thin-shell-taper.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in result["endcaps"]:
        print(f"X={row['X']}: cap terms={row['ordered_masked_cap_terms']}, "
              f"signed={row['actual_taper_change']:.3e}, "
              f"absolute={row['absolute_taper_change']:.3e}, "
              f"divisor majorant={row['finite_divisor_majorant']:.3e}")
    for row in result["tapered_poisson"]:
        print(f"{row['label']}: R2048 tail={-row['convergence'][-1]['difference']:.3e}, "
              f"quadrature difference={row['quadrature_discrepancy']:.3e}")
    print("PASS finite evidence only; no all-outer-variable or asymptotic certification")


if __name__ == "__main__":
    main()

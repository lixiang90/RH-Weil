"""Exact discrete models for physical source traces in notes 434--437.

Reuse the prior rational fibre model without executing its report writer.
Visible energy is computed from the actual source matrix, not the asserted
trace formula. Infinite geometric ball correlations use exact rational tails.
Integer periods and pointwise partitions are not the smooth prime-log frame.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import json
from source_orbit_gram_exact_audit import Fibre, clean

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reviews/2026-10-06/f1-physical-source-trace-exact-audit.json"


def geometric_correlation(rho, shift):
    """Sum the normalized ball correlation as prefix plus exact tail."""
    offset = abs(shift)
    prefix = sum(((1-rho*rho)*rho**(2*d+offset) for d in range(9)), Q(0))
    tail = rho**(18+offset)
    return prefix + tail


def main():
    checks = Counter()

    def check(condition, name):
        assert condition, name
        checks[name] += 1

    for rho in (Q(3, 5), Q(5, 13), Q(8, 17)):
        for shift in range(-12, 13):
            check(geometric_correlation(rho, shift) == rho**abs(shift),
                  "escaped_ball_correlation_with_exact_tail")

    for length, period in ((5, 7), (7, 5)):
        fibre = Fibre(length, period)
        time = range(2*max(length, period))
        overlap = sum((fibre.f(t)**2 for t in time), Q(0))
        mass = period - overlap
        check(mass >= 0, "nonnegative_fixed_q_mass")

        @lru_cache(None)
        def moved(r, x):
            return fibre.source(x, fibre.vector(x), r)

        @lru_cache(None)
        def fixed(x):
            vector = fibre.vector(x)
            dots = defaultdict(Q)
            for (j, k), value in vector.items():
                dots[k] += fibre.c(x+j*length+k*period)*value
            out = defaultdict(Q, vector)
            for k, dot in dots.items():
                for j in fibre.c_rows(x, k):
                    out[j, k] -= fibre.c(x+j*length+k*period)*dot
            return clean(out)

        def visible_energy(rows, kp, kq, jupper, kupper):
            return sum((rows(t-j*length-k*period).get((j, k), Q(0))**2
                        for t in time for j in range(-kp, jupper+1)
                        for k in range(-kq, kupper+1)), Q(0))

        jp = Q(0)
        for x in range(4*length):
            ap = sum((fibre.c(x+j*length)**2 for j in fibre.c_rows(x, 0) if j < 0), Q(0))
            jp += ap*(1-ap)

        for r in range(-3, 4):
            jupper = 4+(abs(r)*period+2*max(length, period))//length
            kupper = max(0, r)+3
            # Compute all deep q strip rows directly from the source matrix.
            local_q = Q(0)
            for t in time:
                for j in range(-jupper, jupper+1):
                    k = -15
                    x = t-j*length-k*period
                    actual = moved(r, x).get((j, k), Q(0))
                    formula = (Q(j == 0)*fibre.d(t) + fibre.c(t)*(
                        fibre.f(t-j*length-r*period)-fibre.f(t-j*length)))
                    check(actual == formula, "actual_deep_q_strip_row")
                    local_q += actual**2
            check(local_q == period, "actual_deep_q_strip_energy")

            for kp, kq in ((12, 12), (14, 17), (17, 14)):
                energy = visible_energy(lambda x: moved(r, x), kp, kq, jupper, kupper)
                check(energy == kp*length+kq*period-r*mass,
                      "full_visible_source_energy_and_signed_unit_flux")
                for rho_p, rho_q in ((Q(3, 5), Q(5, 13)), (Q(8, 17), Q(3, 5))):
                    # Finite discrete convolution kernels, including both signs.
                    for h in ({0: Q(2), length: Q(3), -period: Q(-1)},
                              {-length: Q(1)}, {0: Q(-2), -2*length: Q(1, 3), period: Q(4, 5)}):
                        pball = length*sum((geometric_correlation(rho_p, s//length)*value
                                           for s, value in h.items() if s % length == 0), Q(0))
                        qball = local_q*sum((geometric_correlation(rho_q, s//period)*value
                                            for s, value in h.items() if s % period == 0), Q(0))
                        actual = energy*h.get(0, Q(0))+pball+qball
                        lam = (length+period)*h.get(0, Q(0))
                        lam += length*sum((rho_p**abs(s//length)*value for s, value in h.items()
                                          if s and s % length == 0), Q(0))
                        lam += period*sum((rho_q**abs(s//period)*value for s, value in h.items()
                                          if s and s % period == 0), Q(0))
                        expected = (kp*length+kq*period-r*mass)*h.get(0, Q(0))+lam
                        check(actual == expected, "full_physical_conjugate_trace_model")

        jupper = 4+2*max(length, period)//length
        qfixed = sum((fixed(t-j*length+15*period).get((j, -15), Q(0))**2
                      for t in time for j in range(-jupper, jupper+1)), Q(0))
        check(qfixed == mass, "actual_fixed_q_strip_energy")
        for kp, kq in ((12, 12), (14, 17), (17, 14)):
            energy = visible_energy(fixed, kp, kq, jupper, 3)
            check(energy == kq*mass+jp, "actual_fixed_sector_visible_energy")
        # An isolated p step in these coprime integer models is absent on q.
        check(length % period != 0, "isolated_p_step_model")
        for rho in (Q(3, 5), Q(5, 13)):
            for n in (1, 2, 4, 7):
                traces = [length*geometric_correlation(rho, -1) for _ in range(n)]
                check(sum(traces, Q(0))/n == length*rho,
                      "finite_average_isolated_p_trace")
                check(Q(0) != length*rho, "fixed_limit_loses_isolated_p_trace")

    # Q(i): direct H Fourier coefficients versus the increment multiplier.
    # This checks the exact algebra only, not irrational rotation density.
    def add(a, b):
        return a[0]+b[0], a[1]+b[1]

    def mul(a, b):
        return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

    def div(a, b):
        norm = b[0]**2+b[1]**2
        return ((a[0]*b[0]+a[1]*b[1])/norm,
                (a[1]*b[0]-a[0]*b[1])/norm)

    one = Q(1), Q(0)
    for z in ((Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13)),
              (Q(-3, 5), Q(4, 5)), (Q(0), Q(1))):
        denominator = add(one, mul((Q(-1, 2), Q(0)), z))
        hcoefficient = div(mul((Q(1, 2), Q(0)), z), denominator)
        direct = add(z, mul(add(z, (Q(-1), Q(0))), hcoefficient))
        predicted = div(mul((Q(1, 2), Q(0)), z), denominator)
        check(direct == predicted and direct != (0, 0), "nonzero_one_step_increment_multiplier")
        check(mul(direct, add(one, z)) != (0, 0), "nonzero_even_cutoff_increment_multiplier")

    result = {
        "status": "passed_exact_discrete_physical_source_trace_models",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
        "dependency_sha256": hashlib.sha256((ROOT/"scripts/source_orbit_gram_exact_audit.py").read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
        "checks": dict(sorted(checks.items())),
        "total_exact_assertions": sum(checks.values()),
        "models": [{"p_period": 5, "q_period": 7}, {"p_period": 7, "q_period": 5}],
        "arithmetic": "Fraction and rational complex pairs only; source rows complete; geometric tails exact",
        "scope": "Independent discrete source matrix computes visible flux and fixed-sector energies; rational ball tails and finite convolution steps audit physical trace formulas and Fourier increment algebra. Integer commensurate periods and pointwise partitions are not the smooth prime-log operators. This does not prove analytic trace class, cutoff limits, irrational density, relative Chern, RR or RH. Infinite analysis is in separately reviewed notes.",
    }
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "scope"}))


if __name__ == "__main__":
    main()

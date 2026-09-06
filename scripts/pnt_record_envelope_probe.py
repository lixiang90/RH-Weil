"""MP50 finite [E] checks of Chebyshev/PNT-type record-envelope intersections.

These are explicit envelope functions, NOT actual von Mangoldt samples,
certified PNT constants, arithmetic records, or numerical RH evidence.
The half-axis norm uses direct quadrature before the final intersection and
an EXACT exponential tail after it. This is not a frequency-cutoff experiment.
Finite checks do not establish an asymptotic theorem or interval certificate.
Only mpmath is required. No files, network, registry, or plots are used.
"""

import sys
from time import perf_counter

import mpmath as mp

sys.dont_write_bytecode = True


def j_closed(rate, root_coefficient):
    a, c = rate, root_coefficient
    return 1/a + c*mp.sqrt(mp.pi)/(2*a**mp.mpf("1.5")) * mp.exp(c*c/(4*a)) * mp.erfc(-c/(2*mp.sqrt(a)))


def j_quadrature(rate, root_coefficient):
    # Direct integration of exp(-a*t+c*sqrt(t)); the last interval is infinite.
    split = max(mp.mpf(2), (root_coefficient/rate)**2)
    return mp.quad(lambda t: mp.exp(-rate*t+root_coefficient*mp.sqrt(t)),
                   [0, 1, split, mp.inf])


def intersection(r, b, c, log_b):
    k = r+b
    v = (c+mp.sqrt(c*c+4*k*log_b))/(2*k)
    u = v*v
    log_value = log_b-b*u
    # For log(B)=0 the origin is also an intersection. This v is the FINAL
    # crossing; the PNT prefix is the lower envelope strictly between them.
    return v, u, log_value


def normalized_norm_power(p, r, b, c, v):
    # u=x^2 removes the square-root endpoint. Divide by the intersection
    # value to the p-th power before integrating, avoiding huge exponentials.
    prefix = mp.quad(
        lambda x: 2*x*mp.exp(p*(r*(x*x-v*v)-c*(x-v))),
        [0, v/2, v],
    )
    tail = 1/(p*b)  # EXACT integral from u_* to infinity, after normalization.
    return prefix+tail


def main():
    started = perf_counter()
    mp.mp.dps = 50
    sigma0 = mp.mpf(1)/4
    beta = mp.mpf(3)/8
    sigma_values = (mp.mpf("0.5"), mp.mpf("0.6"), mp.mpf("0.75"))
    c_values = (mp.mpf("0.125"), mp.mpf("0.5"), mp.mpf(2))
    log_b_values = (mp.mpf(0), mp.mpf(4), mp.mpf(16), mp.mpf(64), mp.mpf(256))
    worst_j = mp.mpf(0)
    worst_crossing = mp.mpf(0)
    worst_rate_identity = mp.mpf(0)
    case_count = 0
    naive_sup_failures = 0
    cache = {}

    def checked_j(rate, coefficient):
        nonlocal worst_j
        key = (str(rate), str(coefficient))
        if key not in cache:
            closed = j_closed(rate, coefficient)
            numerical = j_quadrature(rate, coefficient)
            error = abs(closed-numerical)/max(1, abs(closed))
            worst_j = max(worst_j, error)
            assert error < mp.mpf("1e-40")
            cache[key] = closed
        return cache[key]

    print("[E] Synthetic envelopes only; MP50 finite grid, no certified arithmetic/PNT constants.")
    print("[E] R=log(B) in {0,4,16,64,256}; c in {1/8,1/2,2}; exact infinite exponential tails.")
    for c in c_values:
        # Also verify the same-c prefix integration constant used to pass from
        # a PNT-type discrepancy bound to its Abel cumulative-path bound.
        checked_j(1-sigma0, c)
    for sigma in sigma_values:
        r, b = 1-sigma, sigma-beta
        k = r+b
        theta = r/k
        for c in c_values:
            j_bounds = {p: checked_j(p*r, p*c)+1/(p*b) for p in (1, 2)}
            rate = b*c/k**mp.mpf("1.5")
            summaries = {}
            for log_b in log_b_values:
                case_count += 1
                v, u, log_value = intersection(r, b, c, log_b)
                crossing_error = max(abs(k*u-c*v-log_b),
                                     abs(r*u-c*v-log_value))
                worst_crossing = max(worst_crossing, crossing_error)
                assert crossing_error < mp.mpf("1e-44")
                assert u >= log_b/k
                # Check which envelope is smaller on both sides of the final crossing.
                for fraction in (mp.mpf(0), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf(1)):
                    point = fraction*u
                    assert k*point-c*mp.sqrt(point)-log_b <= mp.mpf("1e-44")
                for step in (mp.mpf(1), mp.mpf(10)):
                    point = u+step
                    assert k*point-c*mp.sqrt(point)-log_b > 0
                # The prefix first decreases and then increases. Thus the
                # exact supremum of the minimum envelope is max(1,V_*), NOT V_*.
                log_sup_ratio = max(mp.mpf(0), -log_value)
                assert log_sup_ratio <= c*c/(4*r)+mp.mpf("1e-44")
                if log_value < 0:
                    naive_sup_failures += 1
                norm_ratios = []
                for p in (1, 2):
                    power = normalized_norm_power(p, r, b, c, v)
                    assert power <= j_bounds[p]+mp.mpf("1e-38")*max(1, j_bounds[p])
                    chebyshev_power = -mp.expm1(-p*theta*log_b)/(p*r)+1/(p*b)
                    norm_ratio = mp.exp(log_value-theta*log_b)*(power/chebyshev_power)**(mp.mpf(1)/p)
                    assert 0 < norm_ratio <= 1+mp.mpf("1e-40")
                    norm_ratios.append(norm_ratio)
                exact_gap = theta*log_b-log_value
                assert exact_gap >= rate*mp.sqrt(log_b)-mp.mpf("1e-44")
                if log_b > 0:
                    # Finite, explicit remainder after the sqrt(R) and constant terms.
                    correction = exact_gap-rate*mp.sqrt(log_b)-b*c*c/(2*k*k)
                    correction_bound = b*c**3/(8*k**mp.mpf("2.5")*mp.sqrt(log_b))
                    assert -mp.mpf("1e-44") <= correction <= correction_bound+mp.mpf("1e-44")
                    delta_v = c*c/(4*k*k)/(mp.sqrt(log_b/k+c*c/(4*k*k))+mp.sqrt(log_b/k))
                    error = abs(correction-(b*c/k)*delta_v)
                    worst_rate_identity = max(worst_rate_identity, error)
                    assert error < mp.mpf("1e-44")
                summaries[int(log_b)] = (log_value, exact_gap, norm_ratios, log_sup_ratio)
            low = summaries[0]
            high = summaries[256]
            print(f"[E] sigma'={float(sigma):.2f}, c={float(c):.3g}: "
                  f"R=0 log(V*)={float(low[0]):.8g}, sup/V*={float(mp.exp(low[3])):.8g}; "
                  f"R=256 sqrt-rate={float(high[1]/16):.8g}, leading={float(rate):.8g}, "
                  f"norm ratios L1/L2={float(high[2][0]):.8g}/{float(high[2][1]):.8g}")
    print(f"[E] Cases={case_count}; finite cases refuting the naive sup<=V* claim={naive_sup_failures}.")
    print("[E] Maximum relative J-closed/infinite-integral error:", mp.nstr(worst_j, 8))
    print("[E] Maximum crossing residual:", mp.nstr(worst_crossing, 8))
    print("[E] Maximum finite sqrt-rate remainder identity error:", mp.nstr(worst_rate_identity, 8))
    print(f"PASS; elapsed_seconds={perf_counter()-started:.3f}; no files written.")


if __name__ == "__main__":
    main()

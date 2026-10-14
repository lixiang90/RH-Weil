"""Exact actual-prime growth split admission, without matrix or zero data.

All decisions use Fraction/integer outward bounds. This checks scalar inputs
to the separately proved full-source carrier/compact-supplier obstruction;
it is not a sign test for the complete Weil form.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path


def dyadic_bounds(lo, hi, bits=256):
    scale = 1 << bits
    return (F(lo.numerator * scale // lo.denominator, scale),
            F(-((-hi.numerator * scale) // hi.denominator), scale))


def log_bounds(value, terms=128):
    assert value >= 1
    x, k = F(value), 0
    while x >= 2:
        x /= 2
        k += 1

    def series(z):
        lo = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(terms)), F(0))
        remainder = 2*z**(2*terms+1) / ((2*terms+1)*(1-z*z))
        return lo, lo + remainder

    lo2, hi2 = series(F(1, 3))
    lo, hi = series((x-1)/(x+1))
    return dyadic_bounds(lo + k*lo2, hi + k*hi2)


def sqrt_bounds(n, bits=256):
    scale = 1 << bits
    lower = isqrt(n * scale * scale)
    upper = lower if lower * lower == n * scale * scale else lower + 1
    assert lower*lower <= n*scale*scale <= upper*upper
    return F(lower, scale), F(upper, scale)


def exp_three_bounds(terms=80):
    term, partial = F(1), F(1)
    for j in range(1, terms+1):
        term *= F(3, j)
        partial += term
    next_term = term * F(3, terms+1)
    return partial, partial + next_term / (1-F(3, terms+2))


def main():
    assert __debug__
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    exp_lo, exp_hi = exp_three_bounds()
    assert 20 < exp_lo <= exp_hi < 21
    # These are exactly the prime powers below e^3, including 4,8,9,16.
    atoms = [(2,1), (3,1), (2,2), (5,1), (7,1), (2,3),
             (3,2), (11,1), (13,1), (2,4), (17,1), (19,1)]
    generated = []
    for p in range(2, 21):
        if all(p % d for d in range(2, isqrt(p)+1)):
            k, n = 1, p
            while n <= 20:
                generated.append((n, p, k))
                k += 1
                n *= p
    assert sorted(generated) == [(p**k, p, k) for p, k in atoms]
    rows = []
    cost_lo, cost_hi = F(0), F(0)
    for p, k in atoms:
        n = p**k
        log_lo, log_hi = log_bounds(F(p))
        root_lo, root_hi = sqrt_bounds(n)
        assert 0 < k*log_lo <= k*log_hi < 3
        overlap_lo, overlap_hi = 1-k*log_hi/3, 1-k*log_lo/3
        lo = 2*log_lo/root_hi * overlap_lo
        hi = 2*log_hi/root_lo * overlap_hi
        assert 0 < lo <= hi
        cost_lo += lo
        cost_hi += hi
        rows.append({'n':n, 'prime':p, 'exponent':k,
                     'Lambda_bounds':[str(log_lo),str(log_hi)],
                     'sqrt_n_bounds':[str(root_lo),str(root_hi)],
                     'contribution_bounds':[str(lo),str(hi)]})
    cost_lo, cost_hi = dyadic_bounds(cost_lo, cost_hi)
    assert cost_lo > 4
    beta, tau = F(7, 2), F(1, 2**49162)
    assert beta+tau-cost_lo < -F(1, 2)
    # pi > 3 makes this a conservative upper for actual Gamma(256).
    # The full Gamma Binet bound is independently proved in 538 and C011.
    _, log_hi = log_bounds(F(128, 3))
    gamma_hi = log_hi + F(1, 15*256) + F(25, 8*256**2)
    gamma_hi = dyadic_bounds(gamma_hi, gamma_hi)[1]
    assert gamma_hi < 4 < cost_lo
    result = {
        'kind':'C011 exact actual-prime scalar gate',
        'scope':'Bounded constant-envelope/compact lower supplier only; not full Q negativity or new macro completion.',
        'half_window':'3/2', 'beta':'7/2', 'omega':256,
        'precision_policy':'Exact fractions; logs128 terms and256bit outward grids, exp80terms; no spectra or zeta zeros.',
        'actual_prime_powers':rows,
        'e_to_three_bounds':[str(x) for x in dyadic_bounds(exp_lo, exp_hi)],
        'cost_C_bounds':[str(cost_lo),str(cost_hi)],
        'strict_cost_floor':'4',
        'beta_plus_original_tau_minus_cost_strict_ceiling':'-1/2',
        'actual_Gamma_256_upper':str(gamma_hi),
        'Gamma_256_strict_ceiling':'4',
        'strict_cost_minus_Gamma_margin':str(cost_lo-gamma_hi),
        'complete_scalar_gate_pass':True,
        'source_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print('Exact full12-prime gate: C(3/2)>4>Gamma(256); beta+tau-C<-1/2.')


if __name__ == '__main__':
    main()

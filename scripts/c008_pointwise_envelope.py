"""Exact rational countercheck of the *broad* pointwise-threshold claim.

No zeta zeros, Weil matrix, or external code.  For L=4/5 only n=2,3,4
occur.  Certify the crude digamma lower envelope minus the actual comb
on [118,121], then use its constant-mass bound for t>=121.
This is a high-frequency symbol bound, NOT a Weil positivity certificate.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json

SCALE = 10**35


def down(x):
    return F(x.numerator * SCALE // x.denominator, SCALE)


def up(x):
    return -down(-x)


def log_bounds(x, terms=300):
    assert x > 1
    z = (x - 1) / (x + 1)
    total = sum((2 * z**(2*k+1) / (2*k+1) for k in range(terms)), F(0))
    remainder = 2*z**(2*terms+1) / ((2*terms+1)*(1-z*z))
    return down(total), up(total + remainder)


def atan_bounds(x, terms=30):
    total = sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(terms)), F(0))
    other = total + (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(total, other), max(total, other)


def sqrt_bounds(n):
    a = isqrt(n * SCALE * SCALE)
    return F(a, SCALE), F(a+1, SCALE)


def cos_upper(x):
    assert abs(x) <= F(16, 5)
    total = sum(((-1)**k*x**(2*k)/factorial(2*k) for k in range(21)), F(0))
    # Taylor degree 41 has zero odd coefficients. Lagrange remainder.
    return up(total + abs(x)**42/factorial(42))


def main():
    a, b = atan_bounds(F(1,5))
    c, d = atan_bounds(F(1,239))
    pi_lo, pi_hi = down(16*a-4*d), up(16*b-4*c)  # Machin identity
    logs = {n: log_bounds(F(n), 100) for n in (2,3)}
    logs[4] = (2*logs[2][0], 2*logs[2][1])
    roots = {n: sqrt_bounds(n) for n in (2,3,4)}
    coeff = {n: (2*logs[2 if n==4 else n][0]/roots[n][1],
                 2*logs[2 if n==4 else n][1]/roots[n][0]) for n in (2,3,4)}
    A_hi = sum((v[1] for v in coeff.values()), F(0))
    base_lo = log_bounds(F(118)/(2*pi_hi))[0] - F(1,118)
    rows = []
    for j in range(30):
        left, right = F(118)+F(j,10), F(118)+F(j+1,10)
        center = (left+right)/2
        comb_hi = F(0)
        for n in (2,3,4):
            llo, lhi = logs[n]
            pmid = (pi_lo+pi_hi)/2
            lmid = (llo+lhi)/2
            phase = center*lmid
            k = (phase/ (2*pmid) + F(1,2)).numerator // (phase/(2*pmid)+F(1,2)).denominator
            y = phase - 2*k*pmid
            # |cos'|<=1 pays both interval width and constant uncertainties.
            delta = (right-left)*lhi/2 + center*(lhi-llo)/2 + k*(pi_hi-pi_lo)
            v = min(F(1), cos_upper(y)+delta)
            # Multiplying a negative upper bound needs the LOWER coefficient.
            comb_hi += coeff[n][1 if v>=0 else 0]*v
        floor = base_lo-comb_hi
        assert floor > F(1,200)
        rows.append({'left':str(left), 'right':str(right), 'lower_bound':str(down(floor))})
    beyond = log_bounds(F(121)/(2*pi_hi))[0]-F(1,121)-A_hi
    assert beyond > F(1,200)
    # T1>118: log(118/(2pi))<A. This does not need exp rounding.
    A_lo = sum((v[0] for v in coeff.values()), F(0))
    assert log_bounds(F(118)/(2*pi_lo))[1] < A_lo
    out = {'arithmetic':'fractions.Fraction; integer isqrt; explicit Taylor remainders',
           'L':'4/5', 'prime_powers':[2,3,4], 'T':'118', 'beta':'1/200',
           'scope':'Psi_L(t)>=1/200 for all |t|>=118; T1>118. No low-frequency/Weil positivity claim.',
           'pi_interval':[str(pi_lo),str(pi_hi)],
           'tail_121_lower_bound':str(down(beyond)), 'panels':rows}
    path=Path('reviews/2026-10-14/c008-certificate/pointwise-envelope-rational.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('exact rational PASS:',out['scope'])
    print('minimum panel lower bound >', float(min(F(x['lower_bound']) for x in rows)))
    print('tail at 121 lower bound >',float(beyond))


if __name__ == '__main__':
    main()

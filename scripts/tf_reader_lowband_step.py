"""Certified low-band scalar for the fixed h0=1_[1,2] and F8 input.

Computes ||P B h0||^2, not the full inverse q0. A high precision solve chooses
a rational polynomial trial; all acceptance uses outward integer intervals,
an actual Hilbert polynomial residual and the global R0/RN operator error.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import factorial, comb, isqrt
import json
from pathlib import Path
import time

import mpmath as mp

from tf_reader_arch_gap_certificate import Intervals, floor_fraction, ceil_fraction
from tf_reader_q0_cost_certificate import PRIMES, finite_b_h0_steps, reciprocal_sqrt_interval


class Fixed:
    def __init__(self, precision):
        self.a = Intervals(precision)
        self.u = self.a.unit
        self.zero = self.a.enclose(Q(0))
        self.one = self.a.enclose(Q(1))

    def scale(self, x, n):
        return (x[0]*n, x[1]*n) if n >= 0 else (x[1]*n, x[0]*n)

    def div_int(self, x, n):
        assert n > 0
        return x[0]//n, -((-x[1])//n)

    def abs_upper(self, x):
        return max(abs(x[0]), abs(x[1]))

    def square_upper(self, x):
        t = self.abs_upper(x)
        return -((-t*t)//self.u)

    def sqrt_upper(self, value):
        assert value >= 0
        k = isqrt(value*self.u)
        return k if k*k == value*self.u else k+1

    def serialize(self, x):
        return [str(Q(x[0], self.u)), str(Q(x[1], self.u))]


class TReader:
    """T(n)=2*pi*n*(pi/2-Si(2*pi*n)), with T(0)=0 convention."""
    def __init__(self, fixed, pi_low, pi_high, target_digits=102):
        self.f = fixed
        self.a = fixed.a
        self.pi = self.a.enclose(pi_low, pi_high)
        self.pi_mid = self.a.enclose((pi_low+pi_high)/2)
        self.pi_radius = self.a.enclose((pi_high-pi_low)/2)[1]
        self.tolerance = 10**(len(str(fixed.u))-1-target_digits)
        self.cache = {0: fixed.zero}
        self.maximum_taylor_terms = 0
        self.maximum_asymptotic_terms = 0

    def at(self, n):
        if n in self.cache:
            return self.cache[n]
        f, a = self.f, self.a
        if n >= 40:
            x = f.scale(self.pi, 2*n)
            x2 = a.mul(x, x)
            term = f.one
            total = f.zero
            k = 0
            while True:
                total = a.add(total, term if k % 2 == 0 else a.neg(term))
                nxt = a.div(f.scale(term, (2*k+2)*(2*k+1)), x2)
                k += 1
                if nxt[1] <= self.tolerance:
                    # Exact geometric-Laplace remainder has sign (-1)^k.
                    remainder = (0, nxt[1]) if k % 2 == 0 else (-nxt[1], 0)
                    result = a.add(total, remainder)
                    self.maximum_asymptotic_terms = max(self.maximum_asymptotic_terms, k)
                    break
                if k > 1000 or nxt[1] > term[1]:
                    raise ArithmeticError("Fixed T asymptotic remainder did not reach its target")
                term = nxt
        else:
            # Evaluate at the rational pi midpoint. The actual argument error
            # is transported using |Si'|<=1, not through a huge Taylor tree.
            x = f.scale(self.pi_mid, 2*n)
            x2 = a.mul(x, x)
            term = x
            total = f.zero
            k = 0
            while True:
                total = a.add(total, term if k % 2 == 0 else a.neg(term))
                nxt = f.div_int(f.scale(a.mul(term, x2), 2*k+1),
                                 (2*k+3)**2*(2*k+2))
                k += 1
                if nxt[1] <= self.tolerance:
                    total = a.add(total, (-nxt[1], nxt[1]))
                    arg_error = 2*n*self.pi_radius
                    si = a.add(total, (-arg_error, arg_error))
                    result = a.sub(f.scale(a.mul(self.pi, self.pi), n),
                                   a.mul(f.scale(self.pi, 2*n), si))
                    self.maximum_taylor_terms = max(self.maximum_taylor_terms, k)
                    break
                if k > 3000:
                    raise ArithmeticError("Si Taylor remainder did not terminate")
                term = nxt
        self.cache[n] = result
        return result


def legendre_moment(l, n):
    return Q(factorial(n)**2, factorial(n-l)*factorial(n+l+1)) if n >= l else Q(0)


def scaled_vector_norm_upper(vector, fixed):
    # Shifted Legendre coefficients: ||sum x_l L_l||^2=sum x_l^2/(2l+1).
    total = 0
    for l, value in enumerate(vector):
        total += -((-fixed.square_upper(value))//(2*l+1))
    return total


def matvec(matrix, vector, fixed):
    a = fixed.a
    return [sum_intervals((a.mul(v, x) for v, x in zip(row, vector)), fixed)
            for row in matrix]


def sum_intervals(values, fixed):
    result = fixed.zero
    for value in values:
        result = fixed.a.add(result, value)
    return result


def make_record(precision, degree, gap_path):
    started = time.perf_counter()
    f = Fixed(precision)
    a = f.a
    gap = json.loads(Path(gap_path).read_text())
    pi_low, pi_high = map(Q, gap['pi_interval'])
    pi = a.enclose(pi_low, pi_high)
    pi2 = a.mul(pi, pi)
    tr = TReader(f, pi_low, pi_high)
    divisors, cells, norm_f2 = finite_b_h0_steps()
    nf = 9699690
    tau = {}
    for d, mu in divisors:
        n = mu*(nf//d)
        tau[2*d] = tau.get(2*d, 0)+n
        tau[d] = tau.get(d, 0)-n
    tau = {k:v for k,v in tau.items() if v}
    assert sum(tau.values()) == 0
    grouped = {}
    items = sorted(tau.items())
    for i, (u, cu) in enumerate(items):
        for v, cv in items[i:]:
            coefficient = cu*cv*(1 if u == v else 2)
            grouped[u+v] = grouped.get(u+v, 0)+coefficient
            grouped[abs(u-v)] = grouped.get(abs(u-v), 0)-coefficient
    grouped = {k:v for k,v in grouped.items() if k and v}
    print(json.dumps({'stage':'T_frequency_sum','frequencies':len(grouped),
                      'step_terms':len(divisors)}), flush=True)
    numerator = f.zero
    for count, (n, coefficient) in enumerate(sorted(grouped.items()), 1):
        numerator = a.add(numerator, f.scale(tr.at(n), coefficient))
        if count % 5000 == 0:
            print(json.dumps({'stage':'T_frequency_sum','completed':count,
                              'total':len(grouped)}), flush=True)
    tail_f2 = a.div(f.div_int(numerator, 2*nf*nf), pi2)
    norm_g2 = a.sub(a.enclose(norm_f2), tail_f2)
    print(json.dumps({'stage':'low_moments','elapsed_seconds':time.perf_counter()-started}), flush=True)
    # Monomial moments of g. The constant Si term cancels because sum tau=0.
    moment0 = sum_intervals((f.div_int(f.scale(tr.at(u), cu), u)
                            for u,cu in items), f)
    moment0 = a.neg(a.div(f.div_int(moment0, 2*nf), pi2))
    moments = [moment0]
    inverse_pi = a.div(f.one, pi)
    inverse_pi_powers = [f.one]
    for k in range(1, 2*degree+3):
        inverse_pi_powers.append(a.mul(inverse_pi_powers[-1], inverse_pi))
    # Aggregate exact rational inverse-frequency moments once.
    sums = {power:sum((Q(cu, nf*u**power) for u,cu in items), Q(0))
            for power in range(1, 2*degree+2, 2)}
    for k in range(1, 2*degree+1):
        n = k-1
        value = f.zero
        for j in range((n-1)//2+1):
            coefficient = Q((-1)**(j+1)*factorial(n),
                             factorial(n-2*j)*2**(2*j+1))*sums[2*j+1]
            value = a.add(value, a.mul(a.enclose(coefficient), inverse_pi_powers[2*j+2]))
        moments.append(value)
    size = 2*degree+1
    c = []
    two_pi = f.scale(pi, 2)
    two_pi2 = a.mul(two_pi, two_pi)
    power = f.one
    for j in range(degree+1):
        coefficient = f.div_int(f.scale(power, 2*(-1)**j), factorial(2*j))
        c.append(coefficient)
        power = a.mul(power, two_pi2)
    lm = [[legendre_moment(l, 2*j) for j in range(degree+1)] for l in range(size)]
    # A is the coefficient matrix of C_N in unnormalized shifted Legendre basis.
    matrix = [[f.zero for _ in range(size)] for _ in range(size)]
    for l in range(size):
        for m in range(l, size):
            value = sum_intervals((a.mul(c[j], a.enclose(lm[l][j]*lm[m][j]))
                                   for j in range(degree+1) if lm[l][j] and lm[m][j]), f)
            matrix[l][m] = f.scale(value, 2*l+1)
            matrix[m][l] = f.scale(value, 2*m+1)
    x = [f.scale(sum_intervals((a.mul(a.mul(c[j], moments[2*j]), a.enclose(lm[l][j]))
                               for j in range(degree+1) if lm[l][j]), f), 2*l+1)
         for l in range(size)]
    print(json.dumps({'stage':'rational_trial_solve','dimension':size,
                      'elapsed_seconds':time.perf_counter()-started}), flush=True)
    # The midpoint solve only chooses a trial. It is not a certificate.
    with mp.workdps(150):
        def middle(value):
            return mp.mpf(value[0]+value[1])/(2*f.u)
        sym = mp.matrix(size)
        xs = mp.matrix(size, 1)
        for l in range(size):
            xs[l] = middle(x[l])/mp.sqrt(2*l+1)
            for m in range(size):
                sym[l,m] = middle(matrix[l][m])*mp.sqrt(mp.mpf(2*m+1)/(2*l+1))
        candidate = mp.lu_solve(mp.eye(size)-sym*sym, xs)
        trial = []
        for l in range(size):
            q = Q(mp.nstr(candidate[l]*mp.sqrt(2*l+1), 130))
            trial.append(a.enclose(q))
    ay = matvec(matrix, trial, f)
    aay = matvec(matrix, ay, f)
    residual = [a.add(a.sub(x[l], trial[l]), aay[l]) for l in range(size)]
    residual2_upper = scaled_vector_norm_upper(residual, f)
    x2_upper = scaled_vector_norm_upper(x, f)
    inner = sum_intervals((f.div_int(a.mul(x[l], trial[l]), 2*l+1)
                           for l in range(size)), f)
    # Global polynomial-resolvent error, not a finite solve residual substitute.
    delta = Q(2, factorial(2*degree+2))*(2*pi_high)**(2*degree+2)
    kappa0 = Q(gap['operator_norm_upper'])
    kappaN = kappa0+delta
    assert kappaN < 1
    M0 = Q(gap['resolvent_norm_upper'])
    MN = 1/(1-kappaN*kappaN)
    etaR = M0*MN*delta*(kappa0+kappaN)
    residual_product = Q(residual2_upper, f.u)*Q(x2_upper, f.u)
    sqrt_product = f.sqrt_upper(ceil_fraction(residual_product*f.u))
    trial_error = ceil_fraction(MN*sqrt_product)
    correction = a.add(inner, (-trial_error, trial_error))
    global_error = ceil_fraction(etaR*norm_f2*f.u)
    norm_v2 = a.add(a.sub(tail_f2, correction), (-global_error, global_error))
    norm_v2 = max(0, norm_v2[0]), min(ceil_fraction(norm_f2*f.u), norm_v2[1])
    assert norm_v2[1] >= norm_v2[0]
    # Coarse spectral q0 consequence; the full inverse residual target is unpaid.
    mlow = mhigh = Mlow = Mhigh = Q(1)
    for p in PRIMES:
        lo,hi = reciprocal_sqrt_interval(p, 10**64)
        mlow *= 1-hi; mhigh *= 1-lo
        Mlow *= 1+lo; Mhigh *= 1+hi
    dlow, uhigh = mlow*mlow, Mhigh*Mhigh
    qlow = Q(norm_v2[0], f.u)/uhigh
    qhigh = min(Q(1), Q(norm_v2[1], f.u)/dlow)
    def short_upper(value):
        return str(Q(ceil_fraction(value*10**100), 10**100))
    return {
      'schema':'tf-reader-lowband-step-v1','scope':'Actual fixed h0/F8 projected-input norm only; q0 coarse spectral enclosure is not width1/16 acceptance.',
      'precision':precision,'degree':degree,'interval_unit':str(f.u),
      'input_norm_squared_exact':str(norm_f2),'tau_terms':len(items),
      'tail_T_frequencies':len(grouped),'T_cache_entries':len(tr.cache),
      'max_Si_Taylor_terms':tr.maximum_taylor_terms,'max_T_Laplace_terms':tr.maximum_asymptotic_terms,
      'F_input_tail_after1_squared':f.serialize(tail_f2),
      'low_forcing_norm_squared':f.serialize(norm_g2),
      'R_N_correction_interval':f.serialize(correction),
      'polynomial_trial_coefficients':[f.serialize(t) for t in trial],
      'true_polynomial_H_residual_squared_upper':str(Q(residual2_upper,f.u)),
      'C_N_g_norm_squared_upper':str(Q(x2_upper,f.u)),
      'trial_quadratic_error_upper':str(Q(trial_error,f.u)),
      'cosine_Taylor_operator_error_upper':short_upper(delta),
      'global_R0_minus_RN_norm_upper':short_upper(etaR),
      'global_quadratic_transport_error_upper':str(Q(global_error,f.u)),
      'P_B_h0_norm_squared_interval':f.serialize(norm_v2),
      'q0_coarse_spectral_interval':[str(Q(floor_fraction(qlow*10**64),10**64)),str(Q(ceil_fraction(qhigh*10**64),10**64))],
      'q0_width_le_1_over16':qhigh-qlow <= Q(1,16),
      'full_G_nonzero_trial_residual_executed':False,
      'unpaid':['Actual full G nonzero trial and true H residual','J enclosure width1/128 for full G trial','Target q0 width1/16','Original five source T/E/cross table'],
      'elapsed_seconds':time.perf_counter()-started,
      'claim_limits':'All lowband interval bounds include actual C0/R0 transport. mpmath solve chooses a rational trial only; acceptance is outward polynomial H residual. This is not full q0 or a sign/RH result.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--precision',type=int,default=260)
    parser.add_argument('--degree',type=int,default=26)
    parser.add_argument('--gap',default='reviews/2026-10-27/tf-reader/arch-gap-certificate.json')
    args=parser.parse_args()
    record=make_record(args.precision,args.degree,args.gap)
    target=Path(args.output);target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes((json.dumps(record,indent=2)+'\n').encode())
    print(json.dumps({'status':'certified-projected-input-norm-only',
        'P_B_h0_norm_squared_interval':record['P_B_h0_norm_squared_interval'],
        'q0_coarse_spectral_interval':record['q0_coarse_spectral_interval'],
        'q0_target_passed':record['q0_width_le_1_over16'],
        'elapsed_seconds':record['elapsed_seconds'],'output':str(target)}),flush=True)


if __name__=='__main__':
    main()

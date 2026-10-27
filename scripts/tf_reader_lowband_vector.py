"""Extract a reusable analytic vector input from the existing low-band witness.

No scalar Si recomputation or G action is performed. The old interval trial
contains the exact rational midpoint selected here. C_N times that trial is
reconstructed in the even monomial basis, then rounded to a rational polynomial
with an explicit full L2(0,1) coefficient-error bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from math import factorial, isqrt
import hashlib
import json
from pathlib import Path

from tf_reader_arch_gap_certificate import Intervals, floor_fraction, ceil_fraction
from tf_reader_q0_cost_certificate import finite_b_h0_steps


def shifted_legendre_moment(l: int, n: int):
    if n < l:
        return F(0)
    return F(factorial(n)**2, factorial(n-l)*factorial(n+l+1))


def sqrt_upper(value: F, scale: int):
    if value < 0:
        raise ArithmeticError('negative square-root input')
    square = ceil_fraction(value*scale*scale)
    n = isqrt(square)
    if n*n < square:
        n += 1
    return F(n, scale)


def upper_decimal_fraction(value: F, digits=120):
    scale = 10**digits
    return F(ceil_fraction(value*scale), scale)


def lf_hash(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def build_record(lowband_path, gap_path):
    lowband = json.loads(Path(lowband_path).read_text())
    gap = json.loads(Path(gap_path).read_text())
    degree = lowband['degree']
    precision = lowband['precision']
    assert degree == 26 and precision == 260
    arithmetic = Intervals(precision)
    unit = arithmetic.unit
    pi_low, pi_high = map(F, gap['pi_interval'])
    pi = arithmetic.enclose(pi_low, pi_high)
    two_pi = (2*pi[0], 2*pi[1])
    two_pi2 = arithmetic.mul(two_pi, two_pi)
    power = arithmetic.enclose(F(1))
    trial_intervals = [[F(a), F(b)] for a, b in lowband['polynomial_trial_coefficients']]
    assert len(trial_intervals) == 2*degree+1
    trial = [(a+b)/2 for a, b in trial_intervals]
    assert all(a <= t <= b for (a, b), t in zip(trial_intervals, trial))
    exact_trial_moments = []
    coefficient_intervals = []
    rational_coefficients = []
    radii = []
    for j in range(degree+1):
        moment = sum((trial[l]*shifted_legendre_moment(l, 2*j)
                      for l in range(2*j+1)), F(0))
        exact_trial_moments.append(moment)
        raw = arithmetic.mul(power, arithmetic.enclose(2*moment/F(factorial(2*j))))
        if j % 2:
            raw = arithmetic.neg(raw)
        coefficient_intervals.append([F(raw[0], unit), F(raw[1], unit)])
        midpoint = F(raw[0]+raw[1], 2*unit)
        rational_coefficients.append(midpoint)
        radii.append(F(raw[1]-raw[0], 2*unit))
        power = arithmetic.mul(power, two_pi2)
    # A direct finite coefficient bound on the actual whole low interval.
    delta_poly = sum(radii, F(0))
    polynomial_legendre = []
    for l in range(2*degree+1):
        polynomial_legendre.append((2*l+1)*sum(
            (rational_coefficients[j]*shifted_legendre_moment(l, 2*j)
             for j in range(degree+1)), F(0)))
    delta_cosine = F(lowband['cosine_Taylor_operator_error_upper'])
    kappa_upper = F(gap['operator_norm_upper'])+delta_cosine
    assert kappa_upper < 1
    MN_upper_exact = 1/(1-kappa_upper*kappa_upper)
    assert MN_upper_exact < 10**6
    MN_upper = F(10**6)
    eta_R_upper = F(lowband['global_R0_minus_RN_norm_upper'])
    g2_upper = F(lowband['low_forcing_norm_squared'][1])
    residual2_upper = F(lowband['true_polynomial_H_residual_squared_upper'])
    g_norm_upper = sqrt_upper(g2_upper, unit)
    residual_norm_upper = sqrt_upper(residual2_upper, unit)
    # kappa_N <= 1 is deliberately used here instead of a tighter multiplier.
    delta_resolvent = eta_R_upper*g_norm_upper
    delta_trial = MN_upper*residual_norm_upper
    delta_ell = delta_resolvent+delta_trial+delta_poly
    delta_ell_public = upper_decimal_fraction(delta_ell)
    divisors, cells, normf2 = finite_b_h0_steps()
    nf = 9699690
    tau = {}
    for d, mu in divisors:
        a = mu*(nf//d)
        tau[2*d] = tau.get(2*d, 0)+a
        tau[d] = tau.get(d, 0)-a
    tau = {u:a for u,a in tau.items() if a}
    assert sum(tau.values()) == 0
    assert normf2 == F(lowband['input_norm_squared_exact'])
    return {
      'schema':'tf-reader-lowband-analytic-vector-v1',
      'scope':'Existing fixed h0/F8 low-band witness extracted as an explicit reusable analytic vector with true Hilbert error; not a G action or q0 acceptance.',
      'degree':degree, 'precision':precision,
      'source_files_lf_sha256':{
          str(lowband_path):lf_hash(lowband_path), str(gap_path):lf_hash(gap_path)},
      'input_h0':'1_[1,2], physical L2 norm1',
      'primes':[2,3,5,7,11,13,17,19], 'N_F':nf,
      'f_B_h0_step_terms':[{'left':d,'right':2*d,'coefficient':str(F(mu,d))}
                          for d,mu in divisors],
      'f_B_h0_norm_squared_exact':str(normf2),
      'g_descriptor':{
          'domain':'0<y<1, zero outside; removable value at0',
          'formula':'g(y)=sum_u tau_u sin(2*pi*u*y)/(pi*y)',
          'tau_common_denominator':nf,
          'tau_scaled_integer_terms':[{'u':u,'numerator':a} for u,a in sorted(tau.items())]},
      'old_trial_interval_midpoints_legendre':[str(x) for x in trial],
      'old_trial_intervals_all_singletons':all(a==b for a,b in trial_intervals),
      'old_trial_box_contains_selected_midpoint':True,
      'C_N_times_trial_even_monomial_intervals':[[str(a),str(b)]
                                               for a,b in coefficient_intervals],
      'p_star_even_monomial_coefficients':[str(x) for x in rational_coefficients],
      'p_star_unormalized_shifted_legendre_coefficients':[str(x) for x in polynomial_legendre],
      'p_star_formula':'p_star(y)=sum_(j=0)^26 a_j*y^(2j); coefficients are exact rationals above.',
      'ell_app_descriptor':{
          'formula':'ell_app(y)=1_(0,1)(y)*(g(y)+p_star(y))',
          'true_target':'ell=R0 g, R0=(I-C0^2)^-1'},
      'v_app_descriptor':{
          'formula':'v_app=f_B_h0 - 1_(1,infinity)*F(ell_app)',
          'true_target':'v=P B h0',
          'infinite_tail':'The exact cosine transform of the explicit compact analytic ell_app is retained; no physical tail truncation.'},
      'error_ledger':{
          'eta_R_upper':str(eta_R_upper),
          'g_norm_upper':str(upper_decimal_fraction(g_norm_upper)),
          'old_true_low_Hilbert_residual_squared_upper':str(residual2_upper),
          'old_residual_norm_upper':str(upper_decimal_fraction(residual_norm_upper,180)),
          'M_N_upper':'1000000',
          'kappa_N_upper':str(upper_decimal_fraction(kappa_upper)),
          'resolvent_input_error_upper':str(upper_decimal_fraction(delta_resolvent)),
          'trial_solve_error_upper':str(upper_decimal_fraction(delta_trial,180)),
          'coefficient_rounding_L2_error_upper':str(upper_decimal_fraction(delta_poly,200)),
          'ell_and_v_true_Hilbert_error_upper':str(delta_ell_public),
          'error_below_2e_minus16':delta_ell_public < F(2,10**16)},
      'bounded_action_transport':'For any actually defined bounded action A, ||A v-A v_app||<=||A||*delta_v. In particular U_log2 is unitary, so transport costs no larger delta_v. Full G still requires its action/integration error certificate.',
      'not_executed':['No scalar Si/T recomputation', 'No full G action', 'No new q0 J/residual or width1/16 acceptance', 'No five-source T/E/cross table'],
      'claim_limits':'This adds an actual analytic-vector input beyond a scalar norm. It does not itself certify a future G-action computation or the long RH Goal.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--lowband',default='reviews/2026-10-27/tf-reader-execution/lowband-step-certificate.json')
    parser.add_argument('--gap',default='reviews/2026-10-27/tf-reader/arch-gap-certificate.json')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    record=build_record(args.lowband,args.gap)
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes((json.dumps(record,indent=2)+'\n').encode())
    print(json.dumps({'status':'analytic-vector-input-extracted',
        'polynomial_terms':len(record['p_star_even_monomial_coefficients']),
        'g_terms':len(record['g_descriptor']['tau_scaled_integer_terms']),
        'delta_v_upper':record['error_ledger']['ell_and_v_true_Hilbert_error_upper'],
        'delta_v_below_2e_minus16':record['error_ledger']['error_below_2e_minus16'],
        'q0_acceptance':False,'output':str(output)}))


if __name__=='__main__':
    main()

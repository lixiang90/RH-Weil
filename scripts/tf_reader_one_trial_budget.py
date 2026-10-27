"""One frozen correlated-residual budget from the actual fixed n/c2 inputs.

All acceptance arithmetic is exact Fraction arithmetic on already certified
rational intervals. This does not evaluate Gv or an actual residual value.
It pays a>=n^2 before consuming the weaker p2/rest lower bound and never
replaces the correlated b<=u*a by an independent a/b rectangle.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def lf_hash(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def interval(values):
    low, high = map(F, values)
    if low > high:
        raise ArithmeticError('Reversed interval')
    return low, high


def serial(values):
    return [str(x) for x in values]


def multiply(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def subtract(x, y):
    return x[0]-y[1], x[1]-y[0]


def square_positive(x):
    if x[0] < 0:
        raise ArithmeticError('Positive square expected')
    return x[0]**2, x[1]**2


def prime_product_bounds(witnesses, selected):
    dlow = dhigh = ulow = uhigh = F(1)
    for p in selected:
        low, high = witnesses[p]
        if not 0 < low <= high < 1 or not p*low*low <= 1 <= p*high*high:
            raise ArithmeticError(f'Invalid inverse-sqrt witness for p={p}')
        dlow *= (1-high)**2
        dhigh *= (1-low)**2
        ulow *= (1+low)**2
        uhigh *= (1+high)**2
    return (dlow, dhigh), (ulow, uhigh)


def build_record(norm_path, pair_path, cost_path):
    started = time.perf_counter()
    norm, pair, cost = map(read_json, (norm_path, pair_path, cost_path))
    if pair['fixed_primes'] != PRIMES or cost['primes'] != PRIMES:
        raise ArithmeticError('The frozen F8 input changed')
    if not pair['width_target_met_by_rational_comparison']:
        raise ArithmeticError('The fixed c2 input has not passed its own gate')
    for path, expected in pair['source_files_lf_sha256'].items():
        if lf_hash(path) != expected:
            raise ArithmeticError(f'Changed c2 dependency: {path}')
    n = interval(norm['P_B_h0_norm_squared_interval'])
    c2 = interval(pair['c2_of_actual_v_interval'])
    d, u = interval(cost['d_interval']), interval(cost['u_interval'])
    if not 0 < n[0] <= n[1] < 1 or not 0 < d[0] <= u[1]:
        raise ArithmeticError('Input positivity bounds failed')
    witnesses = {int(w['p']): interval(w['inverse_sqrt_interval'])
                 for w in cost['inverse_sqrt_witnesses']}
    if sorted(witnesses) != PRIMES:
        raise ArithmeticError('Missing fixed-prime square-root witness')
    whole_d, whole_u = prime_product_bounds(witnesses, PRIMES)
    if not d[0] <= whole_d[0] <= whole_d[1] <= d[1]:
        raise ArithmeticError('Saved d bound does not enclose its prime witnesses')
    if not u[0] <= whole_u[0] <= whole_u[1] <= u[1]:
        raise ArithmeticError('Saved u bound does not enclose its prime witnesses')
    drest, urest = prime_product_bounds(witnesses, PRIMES[1:])
    # sqrt(2)=2/sqrt(2) uses the original rational inverse-sqrt witness.
    sqrt2 = (2*witnesses[2][0], 2*witnesses[2][1])
    a2 = subtract((F(3,2)*n[0], F(3,2)*n[1]), multiply(sqrt2, c2))
    if a2[0] <= 0:
        raise ArithmeticError('The p2 energy lower endpoint is not positive')
    rest_a = multiply(drest, a2)[0], multiply(urest, a2)[1]
    old_source_lower = n[0]**2
    old_spectral_lower = d[0]*n[0]
    old_upper = u[1]*n[1]
    a = (max(old_source_lower, old_spectral_lower, rest_a[0]),
         min(old_upper, rest_a[1]))
    if not 0 < a[0] <= a[1]:
        raise ArithmeticError('Incompatible energy interval')
    t = 1/u[1]
    J = (2*t*n[0]-t*t*a[1], 2*t*n[1]-t*t*a[0])
    residual_upper = n[1]-a[0]/u[1]
    # The best scalar symbolic envelope if n,a were free exact inputs has
    # value n-a/u_hi; this is a lower endpoint for that envelope, NOT r^2.
    best_envelope_lower = n[0]-a[1]/u[1]
    target_residual = d[0]/32
    J_radius = (J[1]-J[0])/2
    variational = (max(F(0), J[0]), min(F(1), J[1]+residual_upper/d[0]))
    old_q0_lower = n[0]/u[1]
    fixed_cauchy_lower = n[0]**2/a[1]
    combined = (max(variational[0], old_q0_lower, fixed_cauchy_lower),
                variational[1])
    if not 0 <= combined[0] <= combined[1] <= 1:
        raise ArithmeticError('Invalid q0 intersection')
    source_paths = (norm_path, pair_path, cost_path,
                    'reviews/2026-10-27/tf-reader-c2/next-one-trial-budget-admission.md')
    return {
      'schema': 'tf-reader-one-trial-correlated-budget-v1',
      'scope': 'One exact rational budget comparison for the saved physical v=P B h0; no G action or actual residual value evaluated.',
      'fixed_primes': PRIMES,
      'physical_object': 'H=L2(R+,dx), h0=1_[1,2], v=P B h0, G=P B*B P|RanP, q0=<v,G^-1v>',
      'source_files_lf_sha256': {str(p):lf_hash(p) for p in source_paths},
      'implementation_lf_sha256': lf_hash(__file__),
      'input_n_interval': serial(n), 'input_c2_interval': serial(c2),
      'd_interval': serial(d), 'u_interval': serial(u),
      'rest_seven_d_interval': serial(drest),
      'rest_seven_u_interval': serial(urest),
      'sqrt2_interval': serial(sqrt2), 'a2_interval': serial(a2),
      'p2_rest_a_interval': serial(rest_a),
      'old_source_a_lower_n_squared': str(old_source_lower),
      'old_spectral_a_lower': str(old_spectral_lower),
      'old_spectral_a_upper': str(old_upper),
      'combined_a_interval': serial(a),
      'a_lower_uses_old_n_squared': a[0] == old_source_lower,
      'new_p2_lower_improves_old_source_lower': rest_a[0] > old_source_lower,
      'new_p2_upper_improves_old_spectral_upper': rest_a[1] < old_upper,
      'correlation_used': 'b=||Gv||^2<=u_hi*a; r^2<=n+(u_hi*t^2-2*t)*a, coefficient=-1/u_hi at frozen t=1/u_hi',
      'frozen_trial_scalar': str(t),
      'J_interval': serial(J), 'J_radius': str(J_radius),
      'J_radius_le_1_over128': J_radius <= F(1,128),
      'true_residual_squared_upper_from_symbol_envelope': str(residual_upper),
      'reserved_residual_squared_target_d_lower_over32': str(target_residual),
      'residual_reserved_budget_met': residual_upper <= target_residual,
      'free_exact_a_best_symbolic_envelope_lower': str(best_envelope_lower),
      'even_free_exact_a_symbol_envelope_exceeds_target': best_envelope_lower > target_residual,
      'free_a_diagnostic_scope': 'The lower endpoint bounds only the minimum value of this sufficient b<=u_hi*a scalar envelope, not the actual residual and not general trials.',
      'variational_q0_interval': serial(variational),
      'old_coarse_q0_lower': str(old_q0_lower),
      'fixed_cauchy_q0_lower_from_new_a_upper': str(fixed_cauchy_lower),
      'combined_q0_interval': serial(combined),
      'combined_q0_width': str(combined[1]-combined[0]),
      'q0_width_le_1_over16': combined[1]-combined[0] <= F(1,16),
      'whole_G_action_admitted': False,
      'not_executed': ['Gv', 'Actual full-G residual norm', 'Other dilation ratios',
                       'Different trial scalar', 'Krylov/Chebyshev iteration',
                       'Original five-source T/E/cross table or Hfin sign'],
      'stop': 'The frozen symbolic-envelope input is insufficient: stop automatic continuation of this input/envelope, without tuning t/prime/degree. New actual global mixed/tail or independent arithmetic input is required for readmission.',
      'mathematical_round_increment': 0,
      'claim_limits': 'Fixed constructive numerical budget only. No new classical all-source/growth sign, whole4/5 UPPER improvement, primitiveRR or substantial method-class impossibility. A stronger fixed q0 lower does not meet its width gate or the long Goal.',
      'elapsed_seconds': time.perf_counter()-started,
      'display_only': {
          'n_interval': [float(x) for x in n],
          'a2_interval': [float(x) for x in a2],
          'p2_rest_a_interval': [float(x) for x in rest_a],
          'combined_a_interval': [float(x) for x in a],
          'J_interval': [float(x) for x in J],
          'residual_upper': float(residual_upper),
          'residual_target': float(target_residual),
          'free_a_best_envelope_lower': float(best_envelope_lower),
          'residual_upper_over_target': float(residual_upper/target_residual),
          'free_a_envelope_lower_over_target': float(best_envelope_lower/target_residual),
          'old_coarse_q0_lower': float(old_q0_lower),
          'new_fixed_cauchy_q0_lower': float(fixed_cauchy_lower),
          'combined_q0_interval': [float(x) for x in combined]}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--norm', default='reviews/2026-10-27/tf-reader-execution/lowband-step-certificate.json')
    parser.add_argument('--pair', default='reviews/2026-10-27/tf-reader-execution/fixed-c2-certificate.json')
    parser.add_argument('--cost', default='reviews/2026-10-27/tf-reader-execution/variational-cost-certificate.json')
    parser.add_argument('--output', default='reviews/2026-10-27/tf-reader-c2/one-trial-budget.json')
    args = parser.parse_args()
    record = build_record(args.norm, args.pair, args.cost)
    if record['residual_reserved_budget_met'] or record['q0_width_le_1_over16']:
        raise ArithmeticError('Frozen expected stop changed: review actual result before automatic continuation')
    Path(args.output).write_bytes((json.dumps(record, indent=2)+'\n').encode())
    print(json.dumps({'status':'executed-budget-insufficient-stop',
          **record['display_only'],'elapsed_seconds':record['elapsed_seconds'],
          'q0_width_target_met':record['q0_width_le_1_over16'],'output':args.output}))


if __name__ == '__main__':
    main()

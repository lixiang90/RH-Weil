"""Combine the five certified terms of the fixed analytic-vector c2 test.

This does not execute G or accept q0. Producer records must enclose the actual
finite integrals, including their arithmetic and analytic remainder errors.
The independent input-vector error is then added in the full physical H norm.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def lf_hash(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def interval(values):
    low, high = map(F, values)
    if low > high:
        raise ArithmeticError('Interval endpoints are reversed')
    return low, high


def serial(values):
    return [str(value) for value in values]


def build_record(mixed_path, tail_path, vector_path, norm_path):
    mixed, tail = load(mixed_path), load(tail_path)
    vector, norm = load(vector_path), load(norm_path)
    for record in (mixed, tail, vector):
        for path, expected in record.get('source_files_lf_sha256', {}).items():
            if lf_hash(path) != expected:
                raise ArithmeticError(f'Changed input version: {path}')
    keys = ('f_U_f', 'ell_FH_Uinverse_f', 'ell_FH_U_f', 'ell_Uinverse_ell')
    terms = {key: interval(mixed['terms'][key]) for key in keys}
    tail_value = interval(tail['integral_interval'])
    total = [F(0), F(0)]
    for key, sign in zip(keys, (1, -1, -1, 1)):
        a, b = terms[key]
        if sign < 0:
            a, b = -b, -a
        total[0] += a
        total[1] += b
    total[0] -= tail_value[1]
    total[1] -= tail_value[0]
    delta = F(vector['error_ledger']['ell_and_v_true_Hilbert_error_upper'])
    norm_squared = interval(norm['P_B_h0_norm_squared_interval'])
    norm_upper = F(389, 1000)
    if norm_squared[1] > norm_upper**2:
        raise ArithmeticError('Input norm bound no longer applies')
    input_error = delta*(2*norm_upper+delta)
    answer = [total[0]-input_error, total[1]+input_error]
    target = F(1, 1024)
    if answer[1]-answer[0] > target:
        raise ArithmeticError('Fixed c2 total width target not met')
    if answer[0] > norm_squared[1] or answer[1] < -norm_squared[1]:
        raise ArithmeticError('Pair interval violates unitary Cauchy-Schwarz')
    source_paths = (mixed_path, tail_path, vector_path, norm_path,
                    'scripts/tf_reader_c2_mixed_terms.py',
                    'scripts/tf_reader_c2_tail_term.py',
                    'scripts/tf_reader_arch_gap_certificate.py',
                    'scripts/tf_reader_lowband_step.py',
                    'scripts/tf_reader_q0_cost_certificate.py')
    return {
        'schema': 'tf-reader-fixed-c2-certificate-v1',
        'scope': 'One fixed bounded mixed pair for the original h0/F8 physical vector; not a G action or q0 acceptance.',
        'target_object': 'c2=<v,U_log2 v>, v=P B h0, h0=1_[1,2], physical L2(R+,dx)',
        'dilation_convention': 'U_log2 f(x)=2^-1/2 f(x/2)',
        'fixed_primes': vector['primes'],
        'source_files_lf_sha256': {str(p): lf_hash(p) for p in source_paths},
        'implementation_lf_sha256': lf_hash(__file__),
        'four_mixed_intervals': {key: serial(terms[key]) for key in keys},
        'finite_tail_product_interval': serial(tail_value),
        'coefficient_signs': '+ f_U_f - ell_FH_Uinverse_f - ell_FH_U_f + ell_Uinverse_ell - finite_tail_product',
        'c2_of_explicit_vstar_interval': serial(total),
        'input_delta_v_upper': str(delta),
        'true_v_norm_upper': str(norm_upper),
        'full_H_input_pair_transport_error_upper': str(input_error),
        'c2_of_actual_v_interval': serial(answer),
        'total_width': str(answer[1]-answer[0]),
        'width_target': str(target),
        'width_target_met_by_rational_comparison': True,
        'display_only': {'c2_interval': [float(x) for x in answer],
                         'total_width': float(answer[1]-answer[0]),
                         'input_pair_error': float(input_error)},
        'physical_infinite_tail': 'Retained through the exact Plancherel/cutoff five-term identity; finite-domain quadrature/remainders are certified in the producer records.',
        'q0_width_target_accepted': False,
        'not_executed': ['Full G action', 'Full-G nonzero trial/J/true residual',
                         'Original five-source T/E/cross table', 'Hfin sign'],
        'claim_limit': 'This changes only the certified mixed-pair executability of the saved analytic representation. No automatic other-prime/Krylov continuation, new classical positivity, growth/core/coupling or long-Goal completion.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mixed', default='reviews/2026-10-27/tf-reader-c2/mixed-terms.json')
    parser.add_argument('--tail', default='reviews/2026-10-27/tf-reader-c2/tail-term.json')
    parser.add_argument('--vector', default='reviews/2026-10-27/tf-reader-execution/lowband-vector-input.json')
    parser.add_argument('--norm', default='reviews/2026-10-27/tf-reader-execution/lowband-step-certificate.json')
    parser.add_argument('--output', default='reviews/2026-10-27/tf-reader-execution/fixed-c2-certificate.json')
    args = parser.parse_args()
    record = build_record(args.mixed, args.tail, args.vector, args.norm)
    Path(args.output).write_bytes((json.dumps(record, indent=2)+'\n').encode())
    print(json.dumps({'status': 'fixed-c2-width-certified', **record['display_only'],
                      'q0_accepted': False, 'output': args.output}))


if __name__ == '__main__':
    main()

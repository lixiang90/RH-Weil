"""Certified finite correction integral for the one frozen c2 test.

Computes integral_0^2 (F ell*)(x) (F ell*)(x/2) / sqrt(2) dx.
The compact analytic input ell*=g+p* is exactly the saved rational witness.
All acceptance arithmetic is outward integer intervals and rational bounds.
No previous full scalar, full G action, or q0 inverse is recomputed here.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import time

from tf_reader_arch_gap_certificate import ceil_fraction
from tf_reader_lowband_step import Fixed, TReader, sum_intervals
from tf_reader_q0_cost_certificate import reciprocal_sqrt_interval


def lf_hash(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def make_record(vector_path, gap_path, precision=260, degree=32):
    started = time.perf_counter()
    if precision != 260 or degree != 32:
        raise ValueError('This is the single frozen degree32/precision260 test')
    vector = json.loads(Path(vector_path).read_text(encoding='utf-8'))
    gap = json.loads(Path(gap_path).read_text(encoding='utf-8'))
    assert vector['primes'] == [2,3,5,7,11,13,17,19]
    assert vector['N_F'] == 9699690
    f = Fixed(precision)
    a = f.a
    pi_low, pi_high = map(Q, gap['pi_interval'])
    pi = a.enclose(pi_low, pi_high)
    pi2 = a.mul(pi, pi)
    nf = vector['g_descriptor']['tau_common_denominator']
    terms = [(int(t['u']), int(t['numerator']))
             for t in vector['g_descriptor']['tau_scaled_integer_terms']]
    assert len(terms) == 384 and sum(c for u,c in terms) == 0
    polynomial = list(map(Q, vector['p_star_even_monomial_coefficients']))
    assert len(polynomial) == 27
    norm_f2 = Q(vector['f_B_h0_norm_squared_exact'])
    assert norm_f2 < 4
    # ||g||_1 <= ||g||_2 <= ||f||_2 < 2 on(0,1).
    # The second bound is a direct exact majorization of the rational p*.
    ell_l1_bound = Q(2) + sum((abs(c)/Q(2*j+1)
                               for j,c in enumerate(polynomial)), Q(0))
    tr = TReader(f, pi_low, pi_high)
    # integral g = -sum tau_u T(u)/u /(2 NF pi^2), since sum tau=0.
    moment0_numerator = sum_intervals(
        (f.div_int(f.scale(tr.at(u), c), u) for u,c in terms), f)
    g_moment0 = a.neg(a.div(f.div_int(moment0_numerator, 2*nf), pi2))
    inverse_pi = a.div(f.one, pi)
    inverse_pi_powers = [f.one]
    for k in range(1, 2*degree+1):
        inverse_pi_powers.append(a.mul(inverse_pi_powers[-1], inverse_pi))
    sums = {power:sum((Q(c, nf*u**power) for u,c in terms), Q(0))
            for power in range(1, 2*degree, 2)}
    g_even_moments = [g_moment0]
    # Integer endpoints give sin(2pi u)=0, cos(2pi u)=1 exactly.
    # For k=2j>=2, integration by parts terminates in odd inverse frequencies.
    for j in range(1, degree+1):
        n = 2*j-1
        moment = f.zero
        for l in range(j):
            coefficient = Q((-1)**(l+1)*factorial(n),
                            factorial(n-2*l)*2**(2*l+1))*sums[2*l+1]
            moment = a.add(moment, a.mul(a.enclose(coefficient),
                                       inverse_pi_powers[2*l+2]))
        g_even_moments.append(moment)
    ell_even_moments = []
    for j, g_moment in enumerate(g_even_moments):
        p_moment = sum((coefficient/Q(2*(j+k)+1)
                       for k,coefficient in enumerate(polynomial)), Q(0))
        ell_even_moments.append(a.add(g_moment, a.enclose(p_moment)))
    two_pi = f.scale(pi, 2)
    two_pi2 = a.mul(two_pi, two_pi)
    power = f.one
    cosine_coefficients = []
    for j in range(degree+1):
        coefficient = f.div_int(f.scale(power, 2*(-1)**j), factorial(2*j))
        cosine_coefficients.append(a.mul(coefficient, ell_even_moments[j]))
        power = a.mul(power, two_pi2)
    # P(x)=sum_j q_j x^(2j).  Exact monomial integration gives
    # integral_0^2 P(x)P(x/2) dx = sum_jk q_j q_k 2^(2j+1)/(2(j+k)+1).
    polynomial_integral = f.zero
    product_terms = 0
    for j, qj in enumerate(cosine_coefficients):
        for k, qk in enumerate(cosine_coefficients):
            term = f.div_int(f.scale(a.mul(qj,qk), 2**(2*j+1)), 2*(j+k)+1)
            polynomial_integral = a.add(polynomial_integral, term)
            product_terms += 1
    inv_sqrt2_low, inv_sqrt2_high = reciprocal_sqrt_interval(2, f.u)
    inv_sqrt2 = a.enclose(inv_sqrt2_low, inv_sqrt2_high)
    polynomial_integral = a.mul(polynomial_integral, inv_sqrt2)
    # Real cosine Taylor through degree2N+1 (odd term zero) has remainder
    # |cos z - sum_0^N(-1)^j z^(2j)/(2j)!| <= |z|^(2N+2)/(2N+2)!.
    # For 0<=x<=2, 0<=y<=1, |z|<=4pi.  Integrating against2ell* gives eps.
    remainder_exact = 2*ell_l1_bound*(4*pi_high)**(2*degree+2)/factorial(2*degree+2)
    remainder_upper = Q(ceil_fraction(remainder_exact*f.u), f.u)
    a_sup_upper = 2*ell_l1_bound
    # |a(x)a(x/2)-P(x)P(x/2)| <= 2 A eps + eps^2.
    integral_remainder = 2*inv_sqrt2_high*(2*a_sup_upper*remainder_upper
                                         +remainder_upper**2)
    integral_remainder = Q(ceil_fraction(integral_remainder*f.u), f.u)
    lo = Q(polynomial_integral[0],f.u)-integral_remainder
    hi = Q(polynomial_integral[1],f.u)+integral_remainder
    width = hi-lo
    if not width <= Q(1,16384):
        raise ArithmeticError('Frozen finite correction did not meet width1/16384')
    paths=[str(vector_path),str(gap_path),'scripts/tf_reader_c2_tail_term.py',
           'scripts/tf_reader_arch_gap_certificate.py',
           'scripts/tf_reader_lowband_step.py','scripts/tf_reader_q0_cost_certificate.py']
    return {
        'schema':'tf-reader-fixed-c2-finite-correction-v1',
        'status':'executed-and-certified',
        'scope':'Only integral_0^2 (F ell*)(x)*(F ell*)(x/2)/sqrt2 dx for the exact saved ell*. No q0/fullG/five-source result.',
        'source_files_lf_sha256':{p:lf_hash(p) for p in paths},
        'physical_input':'Same h0=1_[1,2], F8 and saved compact analytic ell*=g+p*. Infinite physical tail handled by the root Plancherel identity, not truncated here.',
        'precision':precision,'cosine_Taylor_degree_parameter':degree,
        'cosine_polynomial_degree':2*degree,
        'g_integer_frequency_terms':len(terms),
        'p_even_monomial_terms':len(polynomial),
        'T_values_read':len(tr.cache)-1,
        'maximum_Si_Taylor_terms':tr.maximum_taylor_terms,
        'maximum_Laplace_terms':tr.maximum_asymptotic_terms,
        'even_moments': [f.serialize(x) for x in ell_even_moments],
        'cosine_polynomial_coefficients': [f.serialize(x) for x in cosine_coefficients],
        'integrated_product_terms':product_terms,
        'polynomial_integral_interval':f.serialize(polynomial_integral),
        'integral_interval':[str(lo),str(hi)],
        'integral_width':str(width),
        'width_le_1_over16384':True,
        'error_ledger':{
            'input_Bh0_norm_squared_exact':str(norm_f2),
            'g_L1_upper':'2',
            'ell_L1_upper':str(ell_l1_bound),
            'uniform_Fell_sup_upper':str(a_sup_upper),
            'uniform_cosine_Taylor_error_upper':str(remainder_upper),
            'integral_Taylor_transport_error_upper':str(integral_remainder),
            'polynomial_arithmetic_width':str(Q(polynomial_integral[1]-polynomial_integral[0],f.u)),
            'inverse_sqrt2_interval':[str(inv_sqrt2_low),str(inv_sqrt2_high)],
            'Si_and_moment_rounding':'Outward260-digit integer intervals; moment0 uses finite-Laplace/Taylor reader with real argument transport, higher even moments exact integer-endpoint recurrence.',
            'physical_input_transport':'Not included: this record targets exact saved ell*. Root separately pays ||v-v*|| in the complete c2 result.'},
        'elapsed_seconds':time.perf_counter()-started,
        'display_only':{'integral_midpoint':float((lo+hi)/2),
                        'integral_width':float(width),
                        'uniform_cosine_error':float(remainder_upper),
                        'integral_Taylor_error':float(integral_remainder),
                        'ell_L1_upper':float(ell_l1_bound)},
        'claim_limits':'Only this finite correction, no G action/J/residual/q0 acceptance or RH/whole growth consequence. Decimal summaries are not proof endpoints.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--vector',default='reviews/2026-10-27/tf-reader-execution/lowband-vector-input.json')
    parser.add_argument('--gap',default='reviews/2026-10-27/tf-reader/arch-gap-certificate.json')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    record=make_record(args.vector,args.gap)
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes((json.dumps(record,indent=2)+'\n').encode('utf-8'))
    print(json.dumps({'status':record['status'],**record['display_only'],
                      'width_pass':record['width_le_1_over16384'],
                      'elapsed_seconds':record['elapsed_seconds'],'output':str(output)}))


if __name__=='__main__':
    main()

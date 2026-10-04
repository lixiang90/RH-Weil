"""Exact polynomial surrogates for the fixed-corner commutator moment.

Fraction arithmetic integrates compact pieces analytically.  The profiles
have tails 0 and 2, but are rational piecewise polynomials, not the actual
smooth Haar-prime sampling frame.  The audit does not certify trace ideals,
essential norms, LF classifications, actual prime parameters, or RH.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZERO, ONE = F(0), F(1)


def trim(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == ZERO:
        result.pop()
    return result


def add(left, right):
    result = [ZERO]*max(len(left), len(right))
    for i, c in enumerate(left):
        result[i] += c
    for i, c in enumerate(right):
        result[i] += c
    return trim(result)


def scale(poly, scalar):
    return trim([c*scalar for c in poly])


def multiply(left, right):
    result = [ZERO]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return trim(result)


def affine(poly, multiplier, offset):
    """Return the coefficients of poly(multiplier*x+offset)."""
    result = [ZERO]*len(poly)
    for i, a in enumerate(poly):
        for j in range(i+1):
            result[j] += a*F(comb(i, j))*multiplier**j*offset**(i-j)
    return trim(result)


def integrate(poly, left, right):
    return sum((c*(right**(i+1)-left**(i+1))/F(i+1)
                for i, c in enumerate(poly)), ZERO)


def evaluate(poly, value):
    return sum((c*value**i for i, c in enumerate(poly)), ZERO)


def derivative(poly):
    return trim([F(i)*c for i, c in enumerate(poly) if i] or [ZERO])


PROFILES = [
    {'name': 'cubic_C1_step', 'origin': ZERO, 'width': ONE,
     'local_poly': [ZERO, ZERO, F(6), F(-4)]},
    {'name': 'quintic_C2_step', 'origin': F(-2, 3), 'width': F(7, 5),
     'local_poly': [ZERO, ZERO, ZERO, F(20), F(-30), F(12)]},
]


def profile_piece(profile, midpoint, delay=ZERO):
    left = profile['origin']+delay
    if midpoint <= left:
        return [ZERO]
    if midpoint >= left+profile['width']:
        return [F(2)]
    return affine(profile['local_poly'], ONE/profile['width'], -left/profile['width'])


def profile_moment(profile, shift):
    """Closed exact integral m(x)[m(x-s)-m(x+s)] over its compact support."""
    breaks = sorted({profile['origin']+delay+edge
                     for delay in (ZERO, shift, -shift)
                     for edge in (ZERO, profile['width'])})
    result = ZERO
    for left, right in zip(breaks, breaks[1:]):
        mid = (left+right)/2
        m0 = profile_piece(profile, mid)
        minus = profile_piece(profile, mid, shift)
        plus = profile_piece(profile, mid, -shift)
        result += integrate(multiply(m0, add(minus, scale(plus, F(-1)))), left, right)
    return result


def audit():
    counts = {}

    def check(name, condition, detail=None):
        if not condition:
            raise AssertionError((name, detail))
        counts[name] = counts.get(name, 0)+1

    shifts = sorted({F(n, d) for d in range(1, 8) for n in range(-8, 9)}
                    | {F(-9, 2), F(9, 2), F(-11, 3), F(11, 3)})
    sampled_profiles = []
    for profile in PROFILES:
        local = profile['local_poly']
        check('profile_tails_and_endpoints', evaluate(local, ZERO) == ZERO
              and evaluate(local, ONE) == F(2))
        check('profile_flat_first_derivative_endpoints', evaluate(derivative(local), ZERO) == ZERO
              and evaluate(derivative(local), ONE) == ZERO)
        for shift in shifts:
            measured = profile_moment(profile, shift)
            check('frame_translation_moment_exact', measured == -4*shift,
                  (profile['name'], str(shift), str(measured)))
        sampled_profiles.append({
            'name': profile['name'], 'origin': str(profile['origin']),
            'width': str(profile['width']),
            'local_polynomial_coefficients_ascending': [str(c) for c in local],
            'left_tail': '0', 'right_tail': '2',
            'identity': 'integral m(x)*(m(x-s)-m(x+s)) dx = -4*s',
        })

    # beta(t)=(1-t^2)^3 on [-1,1], zero outside: C2, not C-infinity.
    bump = [ONE, ZERO, F(-3), ZERO, F(3), ZERO, F(-1)]
    h = multiply([ONE, ONE], bump)
    k_even = bump
    reflected_h = affine(h, F(-1), ZERO)
    s_poly = [ZERO, ONE]
    moment = integrate(multiply(s_poly, multiply(h, affine(k_even, F(-1), ZERO))), F(-1), ONE)
    positive_form = integrate(multiply([ZERO, ZERO, ONE], multiply(bump, bump)), F(-1), ONE)
    check('non_even_h_even_k_moment_positive', moment == positive_form and moment > ZERO)
    coefficient = -4*moment
    check('commutator_coefficient_nonzero', coefficient != ZERO and coefficient < ZERO)
    reflected_moment = integrate(multiply(s_poly, multiply(h, affine(reflected_h, F(-1), ZERO))),
                                 F(-1), ONE)
    check('reflected_k_moment', reflected_moment == 2*moment and reflected_moment > ZERO)
    symmetric_zero = integrate(multiply(s_poly, multiply(bump, bump)), F(-1), ONE)
    check('even_even_moment_zero', symmetric_zero == ZERO)

    bump_l1 = integrate(bump, F(-1), ONE)
    check('compact_bump_L1_exact', bump_l1 == F(32, 35))
    check('compact_bump_center_value', evaluate(bump, ZERO) == ONE)
    center, atom_weight = F(-3, 2), F(7, 11)
    scaling_examples = []
    previous_l1 = None
    for n in range(1, 9):
        epsilon = F(1, 2**n)
        scaled_poly = affine(bump, ONE/epsilon, -center/epsilon)
        exact_l1 = integrate(scaled_poly, center-epsilon, center+epsilon)
        check('scaled_compact_bump_L1', exact_l1 == epsilon*bump_l1, n)
        check('isolated_toy_atom_stays_nonzero', atom_weight*evaluate(scaled_poly, center)
              == atom_weight, n)
        check('scaled_bump_avoids_zero', center+epsilon < ZERO, n)
        if previous_l1 is not None:
            check('scaled_L1_strictly_decreases', exact_l1 == previous_l1/2, n)
        previous_l1 = exact_l1
        scaling_examples.append({
            'epsilon': str(epsilon), 'L1_norm': str(exact_l1),
            'symbolic_operator_norm_upper_bound_2_L1': str(2*exact_l1),
            'toy_atom_value': str(atom_weight),
        })

    return {
        'status': 'passed_exact_fraction_polynomial_integrals',
        'arithmetic': 'fractions.Fraction; exact polynomial antiderivatives; no floating point or quadrature',
        'profiles': sampled_profiles,
        'shift_count_per_profile': len(shifts),
        'shift_set_rule': 'n/d for -8<=n<=8 and 1<=d<=7, union +/-9/2 and +/-11/3',
        'checks': counts,
        'total_exact_assertions': sum(counts.values()),
        'compact_polynomial_tests': {
            'beta': '(1-t^2)^3 for |t|<=1, zero outside (C2, not C-infinity)',
            'h': '(1+t)*beta(t)', 'k_even': 'beta(t)',
            'integral_t_h_t_k_minus_t': str(moment),
            'commutator_coefficient_minus_4_moment': str(coefficient),
            'k_reflected_h': 'h(-t)',
            'reflected_moment': str(reflected_moment),
            'reflected_commutator_coefficient': str(-4*reflected_moment),
            'even_even_moment': str(symmetric_zero),
        },
        'isolated_toy_atom_scaling': {
            'center': str(center), 'weight': str(atom_weight),
            'base_bump_L1_norm': str(bump_l1), 'examples': scaling_examples,
        },
        'scope': ('Finite rational piecewise-polynomial surrogate identities and exact scaling only. '
                  'The polynomials are not actual smooth Haar-prime frame data or C_c^infinity tests. '
                  'No trace-class, noncompactness, essential-norm, topology, cyclic-source, '
                  'actual-prime, global positivity or RH certification.'),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'reviews/2026-10-04/f1-corner-commutator-moment-audit.json')
    args = parser.parse_args()
    result = audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'assertions': result['total_exact_assertions'],
                      'moment': result['compact_polynomial_tests']['integral_t_h_t_k_minus_t'],
                      'output': str(args.output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()

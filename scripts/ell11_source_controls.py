"""Exact typed/q-series controls for the one fixed marked-cusp candidate.

This is not a Pan-relation certificate or an arithmetic/Maass lift.
The only external modular input is the eta transformation formula. Its
multiplier is checked on a full Schreier generating system of Gamma0(11).
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb
from pathlib import Path


def mul_poly(a, b, degree):
    out = [0]*(degree+1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:degree+1-i]):
                out[i+j] += x*y
    return out


def power_poly(a, power, degree):
    out = [1]+[0]*degree
    for _ in range(power):
        out = mul_poly(out, a, degree)
    return out


def q_series(degree):
    e4 = [1]+[240*sum(d**3 for d in range(1,n+1) if n%d == 0)
              for n in range(1,degree+1)]
    inverse_delta_core = [1]+[0]*degree
    eta_core = [1]+[0]*degree
    for n in range(1,degree+1):
        inv = [0]*(degree+1)
        for k in range(degree//n+1):
            inv[k*n] = comb(23+k, 23)
        inverse_delta_core = mul_poly(inverse_delta_core, inv, degree)
        for step in (n,11*n):
            factor = [1]+[0]*degree
            if step <= degree:
                factor[step] = -2
            if 2*step <= degree:
                factor[2*step] = 1
            eta_core = mul_poly(eta_core, factor, degree)
    q_times_j = mul_poly(power_poly(e4,3,degree), inverse_delta_core,degree)
    g = [0]+eta_core[:-1]
    return q_times_j,g


def matmul(a,b):
    return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])


def inverse(a):
    assert a[0]*a[3]-a[1]*a[2] == 1
    return a[3],-a[1],-a[2],a[0]


def dedekind(d,c):
    assert c > 0
    return sum((Q(r,c)*(Q((d*r)%c,c)-Q(1,2)) for r in range(1,c)),Q(0))


def normalize(a):
    if a[2] < 0 or (a[2] == 0 and a[3] < 0):
        return tuple(-x for x in a)
    return a


def coset_index(a):
    c,d = a[2]%11,a[3]%11
    if c == 0:
        return 0
    return 1+(d*pow(c,-1,11))%11


def schreier_record():
    identity = (1,0,0,1)
    S,T = (0,-1,1,0),(1,1,0,1)
    representatives = [identity]+[(0,-1,1,r) for r in range(11)]
    generators = {'S':S,'T':T,'S_inverse':inverse(S),'T_inverse':inverse(T)}
    records = []
    for i,rep in enumerate(representatives):
        assert coset_index(rep) == i
        for name,generator in generators.items():
            word = matmul(rep,generator)
            target = coset_index(word)
            subgroup = normalize(matmul(word,inverse(representatives[target])))
            a,b,c,d = subgroup
            assert a*d-b*c == 1 and c%11 == 0
            if c == 0:
                assert a == d == 1
                exponent = Q(b)
            else:
                # DLMF23.18.5--7: multiplying the two squared eta
                # transformations gives exp(2*pi*i*exponent)*(c*tau+d)^2.
                exponent = Q(a+d,c)-dedekind(d,c)-dedekind(d,c//11)-Q(1,2)
            assert exponent.denominator == 1
            records.append({'representative_index':i,'right_generator':name,
                            'target_index':target,'Gamma0_matrix':list(subgroup),
                            'eta_product_phase_over_2pi':str(exponent)})
    return {'coset_count':len(representatives),'representatives':[list(x) for x in representatives],
            'Schreier_relations':records,'all_eta_product_multipliers_equal1':True}


def explicit_bounds(radius):
    # sigma3(n)<=n^4, sum n^4 R^n = R(1+11R+11R²+R³)/(1-R)^5.
    fourth_sum = radius*(1+11*radius+11*radius**2+radius**3)/(1-radius)**5
    exponential_argument = 24*radius/(1-radius)**2
    assert exponential_argument < 1
    # exp(x)<=1/(1-x), x in[0,1), so every displayed bound is rational.
    j_upper = (1+240*fourth_sum)**3/(radius*(1-exponential_argument))
    eta_exponential_argument = 2*radius/(1-radius)+2*radius**11/(1-radius**11)
    assert eta_exponential_argument < 1
    g_upper = radius/(1-eta_exponential_argument)
    return j_upper,g_upper


def build_record(degree=12):
    if degree < 4:
        raise ValueError('Need at least four q-coefficients for the controls')
    j,g = q_series(degree)
    kernel_jets = []
    constant_j_jets = []
    for n in range(degree+1):
        j_power = power_poly(j,n,degree)
        kernel_jets.append(mul_poly(j_power,g,degree)[n])
        constant_j_jets.append(j_power[n])
    assert kernel_jets[:4] == [0,1,1486,2246795]
    s,R = Q(1,1024),Q(1,512)
    j_s,g_s = explicit_bounds(s)
    j_R,g_R = explicit_bounds(R)
    epsilon = Q(1,2**20)
    assert j_R*epsilon < 1
    H_prime0 = Q(kernel_jets[3])-Q(kernel_jets[1],4)
    V_prime0 = Q(constant_j_jets[3])-Q(constant_j_jets[1],4)
    common_factor = epsilon*(j_R**4+j_R**2/4)/(1-j_R*epsilon)
    H_prime_variation = g_R*common_factor
    V_prime_variation = common_factor
    assert H_prime0 > H_prime_variation > 0
    assert V_prime0 > V_prime_variation > 0
    return {'schema':'ell11-source-typed-controls-v1',
            'scope':'One fixed q-analytic marked-cusp functional, typed eta-product and exact local/source-norm controls only; no Pan relation or arithmetic lift.',
            'implementation_lf_sha256':sha256(Path(__file__).read_bytes().replace(b'\r\n',b'\n')).hexdigest(),
            'q_degree':degree,'q_times_j_coefficients':j,'g11_q_coefficients':g,
            'K11_derivatives_at0':kernel_jets,'constant_kernel_derivatives_at0':constant_j_jets,
            'eta_modularity':schreier_record(),
            'cusp_orders':{'infinity':1,'zero':1,'Fricke_W11_eigenvalue':-1,'character':'trivial'},
            'contour_source_bounds':{'s':str(s),'R':str(R),'j_s_upper':str(j_s),'j_R_upper':str(j_R),
                                     'g_R_upper':str(g_R),'series_ratio':str(s/R),
                                     'series_functional_multiplier':str(g_R*s/(R-s)),
                                     'p_A_definition':'integral |r(u)| exp(A |u|)du, as in583',
                                     'direct_contour_bound':'|K11^(k)(u)|<=g_R_upper*j_R_upper^k*exp(j_R_upper*|u|)',
                                     'fixed_source_du_bound':'|ell11(r)|<=g_R_upper*sqrt(2L)*exp(j_R_upper*L)*||r||L2 for supp r subset[-L,L]',
                                     'Dlog_bound':'multiply the du bound by(log2)^(-1/2), using the original zero-extension Dlog norm'},
            'common_small_537_control_family':{'epsilon_upper':str(epsilon),
                                             'family':'r_phi=(D^2-1/4)(u phi), phi>=0 nonzero even smooth compact supported in(-epsilon,epsilon)',
                                             'original_record':'reviews/2026-10-27/cusp-transport/principal-relations-and-nonroot-test.md(15)--(17)',
                                             'H_prime_at0':str(H_prime0),'H_prime_variation_upper':str(H_prime_variation),
                                             'old_V_prime_at0':str(V_prime0),'old_V_prime_variation_upper':str(V_prime_variation),
                                             'both_positive_for_common_epsilon':True,
                                             'consequence':'For every phi in this common sufficiently-small subfamily, the same actual source has ell11(r_phi)>0, olda0(r_phi)>0, doublepolezero and Qzeta(r_phi)>0 by537.',
                                             'not_claimed':'No unique old numerical waveform was fixed by537 or583. The separate573 even-chi source has not been evaluated.'},
            'not_claimed':['All Pan annihilation','Pan counterexample','Actual harmonic Maass source/lift','Weil-rho transport','Petersson/xi normalization','Relative Picard/arithmetic Green or mixedRR','All-source coverage or RH positivity'],
            'display_only':{'j_s_upper':float(j_s),'j_R_upper':float(j_R),'g_R_upper':float(g_R),
                            'H_prime0':float(H_prime0),'H_prime_variation':float(H_prime_variation),
                            'old_V_prime0':float(V_prime0),'old_V_prime_variation':float(V_prime_variation)}}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='reviews/2026-10-27/marked-cusp/source-controls.json')
    args=parser.parse_args()
    record=build_record()
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes((json.dumps(record,indent=2)+'\n').encode())
    print(json.dumps({'status':'exact-source-controls-passed','K_first4':record['K11_derivatives_at0'][:4],
                      'Schreier_relations':len(record['eta_modularity']['Schreier_relations']),
                      **record['display_only'],'output':args.output}))


if __name__=='__main__':main()

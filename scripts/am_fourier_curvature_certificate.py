"""AM13 derivative research: point jets and a whole-interval Fourier lift.

All numerical bounds use Python integers/Fractions. The elementary Fourier
and Taylor justification is recorded separately; this is not a Lean proof
and is not an input to the round506 proportion certificate.
"""
from fractions import Fraction as Q
from math import factorial, isqrt
from pathlib import Path
import argparse, json, hashlib, time, sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'scripts/am_lossless_majorant_certificate.py').is_file())
sys.path.insert(0, str(ROOT/'scripts'))
import am_lossless_majorant_certificate as am

PRECISION = 10**22


def canonical_sha(path):
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n').replace(b'\r', b'\n')).hexdigest()


def enclosure(a):
    lo, hi = a
    assert lo <= hi
    return (Q((lo*PRECISION).numerator//(lo*PRECISION).denominator, PRECISION),
            Q(-((-hi*PRECISION).numerator//(-hi*PRECISION).denominator), PRECISION))


def point(x):
    return Q(x), Q(x)


def plus(a, b):
    return enclosure((a[0]+b[0], a[1]+b[1]))


def times(a, b):
    values = [x*y for x in a for y in b]
    return enclosure((min(values), max(values)))


def scale(a, c):
    return times(a, point(c))


def divide(a, b):
    assert b[0]*b[1] > 0
    return times(a, enclosure((1/b[1], 1/b[0])))


def power(a, k):
    assert type(k) is int and k >= 0
    if k == 0:
        return point(1)
    lo, hi = a
    if k % 2:
        return enclosure((lo**k, hi**k))
    return enclosure((0 if lo <= 0 <= hi else min(lo**k, hi**k),
                      max(lo**k, hi**k)))


PI = enclosure(am.add(am.scale(am.atan_interval(5), 16),
                      am.scale(am.atan_interval(239), -4)))
root_floor = isqrt(2*PRECISION**2)
SQRT2 = Q(root_floor, PRECISION), Q(root_floor+1, PRECISION)
assert SQRT2[0]**2 < 2 < SQRT2[1]**2
BETA = divide(SQRT2, scale(PI, 2))
Z = enclosure(am.trig_interval(point(Q(1, 2)), True))


def cos_sinc(x):
    q = power(x, 2)
    assert 0 <= q[0] <= q[1] < 10
    values = []
    for shift in (0, 1):
        value = point(0)
        for k in range(13):
            value = plus(value, scale(power(q, k), Q((-1)**k, factorial(2*k+shift))))
        # Beginning at k=13, the uniform tail ratios are strictly below 1.
        assert Q(10, (28+shift)*(27+shift)) < 1
        error = q[1]**13/factorial(26+shift)
        values.append(enclosure((value[0]-error, value[1]+error)))
    return values


def sinc_jet(v):
    radius = max(map(abs, v))
    if v[0] <= 0 <= v[1] or radius <= Q(1, 4):
        assert PI[1]**2*radius**2 < 10
        result = []
        for r in range(3):
            value = point(0)
            for k in range(13):
                if 2*k < r:
                    continue
                coefficient = Q((-1)**k*factorial(2*k),
                                factorial(2*k-r)*factorial(2*k+1))
                value = plus(value, scale(times(power(PI, 2*k), power(v, 2*k-r)), coefficient))
            # T_(k+1)/T_k <= 10*(2k+1)/((2k+3)*(2k+2-r)*(2k+1-r));
            # this expression decreases for k>=13 and r=0,1,2.
            assert Q(270, 29*(28-r)*(27-r)) < 1
            error = Q(factorial(26), factorial(26-r)*factorial(27))*PI[1]**26*radius**(26-r)
            result.append(enclosure((value[0]-error, value[1]+error)))
        return result
    mid = (v[0]+v[1])/2+Q(1, 2)
    n = mid.numerator//mid.denominator
    phase = times(PI, plus(v, point(-n)))
    cosine, sine_sinc = cos_sinc(phase)
    cosine = scale(cosine, (-1)**n)
    sine = scale(times(phase, sine_sinc), (-1)**n)
    s0 = divide(sine, times(PI, v))
    s1 = plus(divide(cosine, v), scale(divide(sine, times(PI, power(v, 2))), -1))
    s2 = plus(plus(scale(divide(times(PI, sine), v), -1),
                   scale(divide(cosine, power(v, 2)), -2)),
              scale(divide(sine, times(PI, power(v, 3))), 2))
    return [s0, s1, s2]


def kernel_jet(t):
    left, right = sinc_jet(plus(t, scale(BETA, -1))), sinc_jet(plus(t, BETA))
    result = [scale(plus(x, y), Q(1, 2)) for x, y in zip(left, right)]
    for j, coefficient in enumerate(am.CS, 1):
        left, right = sinc_jet(plus(t, point(-j))), sinc_jet(plus(t, point(j)))
        result = [plus(s, scale(plus(x, y), Q(coefficient, 2*10**9)))
                  for s, x, y in zip(result, left, right)]
    return [divide(value, Z) for value in result]


def w_second(t):
    k, first, second = kernel_jet(t)
    return scale(plus(power(first, 2), times(k, second)), 2)


def certificate():
    assert __debug__, 'Assertions are required; do not use -O'
    started = time.monotonic()
    assert am.CS == [12310798,-15041681,3867664,6489926,-992327,5580097,
                     -6846472,3781297,-5670353,3355089,-450523,-218483]
    absolute_coefficients = sum(Q(abs(c), 10**9) for c in am.CS)
    assert absolute_coefficients == Q(6460471, 10**8)
    assert Z[0] > Q(9, 10) and Q(0) < PI[0] <= PI[1] < Q(3141592654, 10**9)
    # cos(sqrt(2)*u) >= 1-u^2 >= 3/4 on |u|<=1/2.
    density_numerator_lower = Q(3, 4)-absolute_coefficients
    assert density_numerator_lower == Q(68539529, 10**8) > 0
    density_upper = (1+absolute_coefficients)/Z[0]
    # The convolution moment integral is 2/((r+1)*(r+2)). For r=3 it is 1/10.
    cubic_moment = 2*(Q(1, 4)-Q(1, 5))
    assert cubic_moment == Q(1, 10)
    third_derivative_upper = density_upper**2*(2*PI[1])**3*cubic_moment
    assert third_derivative_upper < 34
    lo, hi, n = Q(9, 5), Q(21, 10), 256
    step = (hi-lo)/n
    values = []
    for i in range(n):
        node = lo+(Q(i)+Q(1, 2))*step
        low, high = w_second(point(node))
        values.append([str(node), str(low), str(high)])
    point_lower = min(Q(v[1]) for v in values)
    interval_lower = point_lower-Q(34)*step/2
    assert interval_lower > Q(17, 100)
    return {'schema':'rh-weil-am-fourier-curvature-506-v1', 'status':'PASS',
            'scope':'actual fixed AM13 kernel; exact point jets lifted to one full interval by the proved Fourier derivative bound; no new proportion input or Lean verification',
            'script_canonical_lf_sha256':canonical_sha(Path(__file__)),
            'am_lossless_script_canonical_lf_sha256':canonical_sha(ROOT/'scripts/am_lossless_majorant_certificate.py'),
            'coefficient_numerators':am.CS, 'coefficient_denominator':10**9,
            'pi_enclosure':[str(v) for v in PI], 'sqrt2_enclosure':[str(v) for v in SQRT2],
            'beta_enclosure':[str(v) for v in BETA], 'normalization_enclosure':[str(v) for v in Z],
            'density_numerator_positive_lower':str(density_numerator_lower),
            'density_absolute_upper':str(density_upper), 'cubic_convolution_moment':'1/10',
            'global_abs_w_third_derivative_rational_upper':str(third_derivative_upper),
            'global_abs_w_third_derivative_strict_upper':'34',
            'interval':[str(lo),str(hi)], 'midpoint_count':n, 'step':str(step),
            'nearest_midpoint_distance_upper':str(step/2), 'point_curvatures':values,
            'minimum_point_lower':str(point_lower), 'whole_interval_strict_lower':str(interval_lower),
            'strong_convexity_lower':'17/100', 'elapsed_seconds':time.monotonic()-started,
            'used_by_round506_proportion_certificate':False, 'lean_or_nanoda_performed':False}


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Assertions required; do not use -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='recompute and compare the public exact certificate')
    parser.add_argument('--certificate', type=Path, default=ROOT/'output/am-fourier-curvature-certificate.json')
    parser.add_argument('--audit-output', type=Path, help='optional receipt; otherwise this command writes nothing')
    args = parser.parse_args()
    result = certificate()
    if args.check:
        stored = json.loads(args.certificate.read_text(encoding='utf8'))
        assert {k:v for k,v in stored.items() if k != 'elapsed_seconds'} == {k:v for k,v in result.items() if k != 'elapsed_seconds'}
    if args.audit_output:
        args.audit_output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'point_curvatures'},indent=2))

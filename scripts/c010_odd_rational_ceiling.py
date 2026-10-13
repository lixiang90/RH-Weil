"""Exact source-paid odd Rayleigh upper bound for R=M+K+U, not Q.

Reads frozen data only; no author modules, zero data, or PASS labels.
The pilot only proposes a vector, rounded to an exact rational source.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys


def read(path, expected):
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected
    return json.loads(raw)


def main():
    assert __debug__
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    root = Path(__file__).resolve().parents[1]
    source_path = root/'tmp/c009-liu/fresh-b-20261014/certificates/source-matrices.json'
    tail_path = root/'tmp/c009-liu/fresh-b-20261014/certificates/tail-columns.json'
    pilot_path = root/'reviews/2026-10-14/c010-inertia/source-compression-pilot.json'
    hashes = {
        'source': '4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac',
        'tail': '2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2',
        'pilot': 'a7c1ac311188b6121899826d09d6c207eeea82f35bcf279faff0508e2f8b43aa',
    }
    source = read(source_path, hashes['source'])
    tail = read(tail_path, hashes['tail'])
    pilot = read(pilot_path, hashes['pilot'])
    assert source['parameters']['L'] == '17/16'
    assert source['parameters']['N'] == 448
    assert source['parameters']['outputBits'] == 256
    assert tail['parameters']['outputBits'] == 640
    assert tail['deltaRetained'] and not tail['synthetic']
    proposed = next(x['min_vector_raw'] for x in pilot['results']
                    if x['sector'] == 1 and x['n'] == 64)
    assert len(proposed) == 64
    denominator = 10**50
    numerators = []
    for value in proposed:
        q = F(value)*denominator + F(1, 2)
        numerators.append(q.numerator//q.denominator)
    coefficients = [F(n, denominator) for n in numerators]
    degrees = list(range(1, 128, 2))
    wanted = set(degrees)
    matrices = {}
    for name in ('A', 'J0'):
        entries = {}
        for i, j, lo, hi in source['matrices'][name]:
            assert i <= j
            if i in wanted and j in wanted:
                assert (i, j) not in entries
                assert int(lo) <= int(hi)
                entries[(i, j)] = F(int(lo)+int(hi), 2**257)
        assert len(entries) == 64*65//2
        matrices[name] = entries
    numerator = F(0)
    for i, n in enumerate(degrees):
        for j, m in enumerate(degrees):
            key = (min(n, m), max(n, m))
            numerator += coefficients[i]*coefficients[j]*(
                matrices['A'][key]+matrices['J0'][key])
    columns = {0: {}, 1: {}}
    for entry in tail['entries']:
        if entry['index'] in wanted:
            c, n = entry['column'], entry['index']
            assert n not in columns[c]
            assert int(entry['lo']) <= int(entry['hi'])
            columns[c][n] = F(int(entry['lo'])+int(entry['hi']), 2**641)
    assert all(len(x) == 64 for x in columns.values())
    for column in columns.values():
        pairing = sum((coefficients[i]*column[n]
                       for i, n in enumerate(degrees)), F(0))
        numerator += F(648, 17)*pairing**2
    norm_squared = sum((coefficients[i]**2*F(17, 8*(2*n+1))
                        for i, n in enumerate(degrees)), F(0))
    assert norm_squared > 0
    center = numerator/norm_squared
    error = F(1, 2**204)+F(2, 2**220)+F(9, 2**512)
    upper = center+error
    ceiling = F(2, 10**31)
    assert upper < ceiling
    result = {
        'scope': 'Actual odd R=M+K+U Rayleigh upper bound only; not Q upper or a simple-ground proof.',
        'arithmetic': 'All decisions are exact fractions.Fraction/integer arithmetic.',
        'input_sha256': hashes,
        'degrees': degrees,
        'coefficient_numerators': numerators,
        'coefficient_denominator': denominator,
        'norm_squared': str(norm_squared),
        'center_rayleigh': str(center),
        'operator_error': str(error),
        'actual_upper_bound': str(upper),
        'strict_ceiling': str(ceiling),
        'strict_margin': str(ceiling-upper),
        'source_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out = root/'reviews/2026-10-14/c010-inertia/c010-odd-rational-ceiling.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('Exact source-paid Rodd upper PASS: lambda1(Rodd)<2e-31.')
    print('Center display only:', float(center), '; norm display only:', float(norm_squared))


if __name__ == '__main__':
    main()

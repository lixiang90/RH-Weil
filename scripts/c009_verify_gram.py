"""Independent whole-integer Gram check of the newly rebuilt C009 targets.

Reads data only; no author modules or PASS labels are used to decide PSD.
This checks the final finite sign gate, not the analytic/source error gates.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def read(path):
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def check(matrix, factor):
    n = len(matrix)
    assert n == 224 and len(factor) == n
    assert all(len(row) == n and all(type(x) is int for x in row) for row in matrix)
    assert all(len(row) == i+1 and all(type(x) is int for x in row)
               for i, row in enumerate(factor))
    assert all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
    sums = [0]*n
    for i in range(n):
        for j in range(i+1):
            gram = sum(x*y for x,y in zip(factor[i][:j+1], factor[j]))
            residual = matrix[i][j] - (gram << 2329)
            if i == j:
                residual -= 1 << 2873
            sums[i] += abs(residual)
            if j != i:
                sums[j] += abs(residual)
    return sums


def main():
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument('run', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    results=[]
    for sector in (0,1):
        target, th = read(args.run/'certificates'/f'sector-{sector}-target.json')
        proposal, gh = read(args.run/'certificates'/f'sector-{sector}-gram.json')
        assert target['sector'] == sector
        assert target['indices'] == list(range(sector,448,2))
        matrix, factor = target['matrix'], proposal['factor']
        assert max(abs(v).bit_length() for row in matrix for v in row) == 3353
        rows = check(matrix, factor)
        assert all(v < 1 << 2848 for v in rows)
        # A real wrong-sign perturbation must fail the SAME whole-row test.
        damaged = [row[:] for row in matrix]
        damaged[0][0] = -(1 << 3353)
        assert max(check(damaged, factor)) >= 1 << 2873
        results.append({'sector':sector,'rows_checked':224,
                        'row_sums':rows,'all_rows_strictly_below_power_two':2848,
                        'paid_diagonal_power_two':2873,'gram_scale_power_two':2329,
                        'strict_matrix_floor_power_two':2872,
                        'target_sha256':th,'factor_sha256':gh,
                        'wrong_sign_negative_control_rejected':True})
    result={'status':'independent_exact_Gram_gate_pass','sectors':results,
            'scope':'Finite integer sign only; all analytic/source/normalization/error gates remain separate.',
            'source_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print('Both complete 224-row Gram gates and wrong-sign controls passed.')


if __name__ == '__main__':
    main()

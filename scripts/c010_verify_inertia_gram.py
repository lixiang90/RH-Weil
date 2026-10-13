"""Independent complete integer sign gate for C010 shifted inertia.

The producer proposes factors; this reader reconstructs every Gram entry.
Only after the separately audited source, rounding, congruence and whole-form
bridges does the finite gate imply the claimed Q spectral counts.
"""
import argparse
import hashlib
import json
from pathlib import Path


def read(path):
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def rows(matrix, factor, guard):
    n = len(matrix)
    out = [0] * n
    for i in range(n):
        for j in range(i + 1):
            gram = sum(a * b for a, b in zip(factor[i][:j + 1], factor[j]))
            residual = matrix[i][j] - gram - (guard if i == j else 0)
            out[i] += abs(residual)
            if i != j:
                out[j] += abs(residual)
    return out


def main():
    assert __debug__
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    upstream = root / 'tmp/c009-liu/fresh-b-20261014/certificates'
    expected = {
        'source-matrices.json': '4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac',
        'sector-0-congruence.json': '4303b0e6dacad1c181320a719f6b33d328c068341c4d8e720e057bdc673c2589',
        'sector-0-target.json': 'ce9f39f5e355b9bd77e0a04c0b94bab4c4a1e922024dfdd626e05f8a8c2d201d',
        'sector-1-congruence.json': '311df181b573940eb8e964727c9a9905107f5ff8eed16284f91d44e4021137db',
        'sector-1-target.json': 'a4e7bdbd70b37fe82a39a8d8a718d95010094a4f439f440abb4b33ad6f3510fd',
    }
    for name, digest in expected.items():
        assert hashlib.sha256((upstream / name).read_bytes()).hexdigest() == digest
    results = []
    for sector in (0, 1):
        packet, target_sha = read(args.directory / f'shifted-sector-{sector}-target.json')
        proposal, factor_sha = read(args.directory / f'shifted-sector-{sector}-gram.json')
        receipt, receipt_sha = read(args.directory / f'shifted-sector-{sector}-compile-receipt.json')
        assert receipt['sector'] == sector
        assert receipt['source_matrix_sha256'] == expected['source-matrices.json']
        assert receipt['congruence_sha256'] == expected[f'sector-{sector}-congruence.json']
        assert receipt['original_target_sha256'] == expected[f'sector-{sector}-target.json']
        assert receipt['target_sha256'] == target_sha and receipt['gram_sha256'] == factor_sha
        assert packet['sector'] == proposal['sector'] == sector
        assert packet['indices'] == list(range(sector, 448, 2))
        assert packet['bits'] == 512 and packet['guard'] == 1 << 372
        matrix, factor = packet['matrix'], proposal['factor']
        n = 224
        assert len(matrix) == len(factor) == n
        assert all(len(row) == n and all(type(v) is int for v in row) for row in matrix)
        assert all(len(row) in (i + 1, n) and all(type(v) is int for v in row)
                   for i, row in enumerate(factor))
        assert all(not any(row[i + 1:]) for i, row in enumerate(factor))
        assert all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
        modified = [row[:] for row in matrix]
        rank = packet['rank_one']
        if sector == 0:
            assert rank['coefficient'] == 1 << 23
            vector = rank['vector']
            assert len(vector) == n and all(type(v) is int for v in vector)
            assert any(vector)
            for i in range(n):
                for j in range(n):
                    modified[i][j] += (1 << 23) * vector[i] * vector[j]
        else:
            assert rank is None
        guard = packet['guard']
        row_sums = rows(modified, factor, guard)
        assert all(v < guard for v in row_sums)
        # A changed diagonal with the wrong sign must fail this same criterion.
        control = [row[:] for row in modified]
        control[0][0] = -(abs(control[0][0]) + guard)
        assert max(rows(control, factor, guard)) >= guard
        results.append({
            'sector': sector, 'rows_checked': n, 'gram_entries_checked': n * (n + 1) // 2,
            'row_sums': row_sums, 'guard': guard,
            'strict_positive_floor': guard - max(row_sums),
            'target_sha256': target_sha, 'factor_sha256': factor_sha,
            'compile_receipt_sha256': receipt_sha,
            'rank_one_added': sector == 0, 'negative_index_upper_bound': 1 - sector,
            'wrong_sign_control_rejected': True,
        })
    result = {
        'kind': 'independent-full-integer-shifted-inertia-Gram-gate',
        'threshold': '10^-34',
        'status': 'pass', 'sectors': results,
        'source_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'original_input_sha256': expected,
        'scope': 'Finite sign only. Exact source/rounding/positive-congruence/full-form bridges are separately required.',
    }
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print('All 448 integer Gram rows and both wrong-sign controls passed.')


if __name__ == '__main__':
    main()

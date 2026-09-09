"""Read-only exhaustive verification of one frozen sparse integer candidate.

This module imports neither initialization nor relaxation code. It enumerates
every stored tail/control pair, including the empty and all short words, and
rebuilds prefix minima from the actual sparse lists. A rejected lower-bound
certificate is not by itself a negative continuous residual.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def digest(array):
    h = hashlib.sha256()
    for start in range(0, len(array), 1 << 20):
        h.update(array[start:start + (1 << 20)].tobytes(order='C'))
    return h.hexdigest()


def decode(code, depth, base):
    return [int(code // base**j % base) for j in range(depth - 1, -1, -1)]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint', default='reviews/2026-09-08/finite-control-integer-iteration.json')
    ap.add_argument('--output', default='reviews/2026-09-10/frozen-control-closure.json')
    ap.add_argument('--batch', type=int, default=8192)
    args = ap.parse_args()
    assert 1 <= args.batch <= 32768
    clock = time.perf_counter()
    init_path = ROOT / 'reviews/2026-09-08/finite-control-integer-initialization.json'
    raw_init = init_path.read_bytes()
    init = json.loads(raw_init)
    checkpoint_path = ROOT / args.checkpoint
    raw_checkpoint = checkpoint_path.read_bytes()
    checkpoint = json.loads(raw_checkpoint)
    assert checkpoint['initialization_sha256'] == hashlib.sha256(raw_init).hexdigest()
    q, scale, denominator = init['control_count'], init['scale'], init['control_denominator']
    loss_fraction = Fraction(init['endpoint_loss']) * scale
    floor_fraction = Fraction(init['offset_floor']) * scale
    assert loss_fraction.denominator == floor_fraction.denominator == 1
    loss, floor = int(loss_fraction), int(floor_fraction)
    assert (q, scale, denominator, loss, floor) == (313, 10**12, 80, 5000000, -7000000000)
    dependencies = [
        ('reviews/2026-09-08/kernel-curvature-tail-table.json', init['table_sha256']),
        ('reviews/2026-09-08/radius-five-rational-profile-candidate.json', init['profile_sha256']),
    ]
    for path, expected in dependencies:
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
    records, arrays = [], []

    def checked(record):
        path = (ROOT / record['path']).resolve()
        assert path.is_relative_to(ROOT.resolve())
        a = np.load(path, mmap_mode='r', allow_pickle=False)
        assert a.ndim == 1 and a.dtype == np.dtype('int64')
        assert list(a.shape) == record['shape'] and str(a.dtype) == record['dtype']
        assert a.nbytes == record['bytes'] and digest(a) == record['data_sha256']
        records.append(record)
        arrays.append(a)
        return a

    units = checked(init['kernel_arrays']['units'])
    energy = checked(init['kernel_arrays']['energy_lower'])
    fees = checked(init['kernel_arrays']['fees_lower'])
    assert len(units) == len(fees) == q
    assert np.all(units[1:] > units[:-1]) and units[0] == 492 and units[-1] == 1600
    assert len(energy) > 5 * int(units.max())
    assert np.all((energy >= 0) & (energy <= 2 * scale))
    assert np.all((fees >= -scale) & (fees <= scale))
    table = json.loads((ROOT / dependencies[0][0]).read_bytes())
    assert [Fraction(int(u), denominator) for u in units] == list(map(Fraction, table['control_nodes']))
    assert all(init[k] == table[k] for k in ('alpha', 'eta', 'delta'))
    assert Fraction(init['endpoint_loss']) == Fraction(init['delta']) / 2
    levels = [(np.array([0], dtype=np.int64), np.array([0], dtype=np.int64))]
    for record in init['records'][:3]:
        levels.append((checked(record['codes']), checked(record['offsets'])))
    levels.append((checked(checkpoint['current_codes']), checked(checkpoint['current_offsets'])))
    # Candidate labels, not their construction history, are checked here.
    for depth, (codes, offsets) in enumerate(levels):
        assert len(codes) == len(offsets) > 0
        assert codes[0] >= 0 and codes[-1] < q**depth
        assert np.all(codes[1:] > codes[:-1])
        assert np.all((offsets >= floor) & (offsets <= 0))
    # All costs and differences have absolute value < 12*S; code < q**4.
    assert max(12 * scale, q**4) < np.iinfo(np.int64).max
    best = [np.array([0], dtype=np.int64)]
    rebuilt = []
    for depth in range(1, 4):
        b = np.repeat(best[-1], q)
        codes, offsets = levels[depth]
        b[codes] = np.minimum(b[codes], offsets)
        expected = init['records'][depth - 1]['prefix_best']
        actual_hash = digest(b)
        assert actual_hash == expected['data_sha256']
        rebuilt.append({'depth': depth, 'data_sha256': actual_hash, 'matches_initialized_prefix_table': True})
        best.append(b)

    long_codes, long_offsets = levels[4]
    controls = np.arange(q, dtype=np.int64)
    results = []
    for depth, (codes, offsets) in enumerate(levels):
        began = time.perf_counter()
        visited = failures = 0
        maximum = None
        witness = None
        for start in range(0, len(codes), args.batch):
            tail_codes = codes[start:start + args.batch]
            tail_offsets = offsets[start:start + args.batch]
            child_depth = min(depth + 1, 4)
            # Truncation forgets the old last symbol only at depth four.
            suffix = tail_codes // q if depth == 4 else tail_codes
            unique_suffix, inverse = np.unique(suffix, return_inverse=True)
            child_codes = unique_suffix[:, None] + controls[None, :] * q**(child_depth - 1)
            if child_depth <= 3:
                effective = best[child_depth][child_codes]
            else:
                effective = best[3][child_codes // q].copy()
                pos = np.searchsorted(long_codes, child_codes)
                pos = np.minimum(pos, len(long_codes) - 1)
                present = long_codes[pos] == child_codes
                effective[present] = np.minimum(effective[present], long_offsets[pos[present]])
            # Direct sum for EACH original tail; no grouped-minimum reduction.
            candidate = tail_offsets[:, None] + fees[None, :] + loss + energy[units][None, :]
            prefix_sum = np.zeros(len(tail_codes), dtype=np.int64)
            for digit_position in range(depth - 1, -1, -1):
                prefix_sum += units[(tail_codes // q**digit_position) % q]
                arguments = prefix_sum[:, None] + units[None, :]
                assert int(arguments.max()) < len(energy)
                candidate += energy[arguments]
            deficit = effective[inverse] - candidate
            failures += int(np.count_nonzero(deficit > 0))
            visited += deficit.size
            top = int(deficit.max())
            if maximum is None or top > maximum:
                maximum = top
                row, control = np.unravel_index(np.argmax(deficit), deficit.shape)
                code = int(tail_codes[row])
                digits = decode(code, depth, q)
                arguments = [int(units[control])]
                for digit in digits:
                    arguments.append(arguments[-1] + int(units[digit]))
                child_digits = ([int(control)] + digits)[:4]
                prefix_labels = [{'depth': 0, 'code': 0, 'offset_integer': 0}]
                head_code = 0
                for j, digit in enumerate(child_digits, 1):
                    head_code = head_code * q + digit
                    all_codes, all_offsets = levels[j]
                    position = int(np.searchsorted(all_codes, head_code))
                    if position < len(all_codes) and int(all_codes[position]) == head_code:
                        prefix_labels.append({'depth': j, 'code': head_code, 'offset_integer': int(all_offsets[position])})
                actual_effective = min(v['offset_integer'] for v in prefix_labels)
                actual_candidate = int(tail_offsets[row]) + int(fees[control]) + loss + sum(int(energy[x]) for x in arguments)
                assert actual_effective - actual_candidate == top
                witness = dict(tail_code=code, tail_digits=digits, tail_units=[int(units[d]) for d in digits],
                               tail_offset_integer=int(tail_offsets[row]), control_index=int(control),
                               control_units=int(units[control]), child_digits=child_digits,
                               retained_child_prefixes=prefix_labels, energy_argument_units=arguments,
                               energy_lower_integers=[int(energy[x]) for x in arguments],
                               fee_lower_integer=int(fees[control]), endpoint_loss_integer=loss,
                               effective_label_integer=actual_effective, candidate_integer=actual_candidate,
                               deficit_integer=top)
            if start // 1048576 != (start + len(tail_codes)) // 1048576:
                print(f'depth {depth}: {start + len(tail_codes)}/{len(codes)} tails; failures {failures}; max deficit {maximum}/{scale}', flush=True)
        assert visited == len(codes) * q
        results.append(dict(depth=depth, tail_count=len(codes), edges=visited, failed_edges=failures,
                            maximum_deficit_integer=maximum, witness=witness,
                            minimum_offset_integer=int(offsets.min()), elapsed_seconds=time.perf_counter() - began))
        print(f'depth {depth} COMPLETE: {visited} edges; {failures} failed; max deficit {maximum}/{scale}', flush=True)

    # Check that the frozen inputs did not change while the scan ran.
    assert init_path.read_bytes() == raw_init and checkpoint_path.read_bytes() == raw_checkpoint
    for record, array in zip(records, arrays):
        assert digest(array) == record['data_sha256']
    for path, expected in dependencies:
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
    total_edges = sum(r['edges'] for r in results)
    total_failed = sum(r['failed_edges'] for r in results)
    output = dict(status='PASS_INTEGER_ENDPOINTS' if total_failed == 0 else 'FAIL_FROZEN_INTEGER_SUFFICIENT_CERTIFICATE',
                  complete=True, all_inputs_unchanged=True, initialization_sha256=hashlib.sha256(raw_init).hexdigest(),
                  checkpoint_path=args.checkpoint, checkpoint_sha256=hashlib.sha256(raw_checkpoint).hexdigest(),
                  verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  control_count=q, scale=scale, endpoint_loss_integer=loss, offset_floor_integer=floor,
                  array_records=records, rebuilt_prefix_tables=rebuilt, levels=results,
                  total_words=sum(len(c) for c, b in levels), total_edges=total_edges, failed_edges=total_failed,
                  elapsed_seconds=time.perf_counter() - clock,
                  scope='Exhaustive integer endpoint test using previously certified lower costs. Failure does not itself imply a negative real continuous residual or exclude other certificates. Continuous transfer requires all endpoints and the existing curvature/amplitude hypotheses.')
    destination = ROOT / args.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: output[k] for k in ('status', 'total_words', 'total_edges', 'failed_edges', 'elapsed_seconds')}), flush=True)


if __name__ == '__main__':
    main()

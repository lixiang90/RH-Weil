"""Recheck the exhaustive scan's worst witness with 320-bit Arb.

An exact prefix-closure failure still need not give h(head)>L+h(tail),
because other head branches can lower h. The conclusion is kept scalar.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from radius_five_arb_kernel import Kernel, arb, rational, rational_bounds

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '77287d18687dd55a9032fa20396714ba2cca37d94560d98d0130ec22a203f60c'


def enclosure(value):
    low, high = rational_bounds(value)
    return {'lower': str(low), 'upper': str(high), 'display': str(value)}


def main():
    source = ROOT / 'reviews/2026-09-10/frozen-control-closure.json'
    raw = source.read_bytes()
    data = json.loads(raw)
    assert data['complete'] and data['all_inputs_unchanged']
    assert data['verifier_sha256'] == SOURCE_SHA
    assert hashlib.sha256((ROOT / 'scripts/verify_frozen_control_closure.py').read_bytes()).hexdigest() == SOURCE_SHA
    assert data['total_edges'] == 6237815186 and data['total_words'] == 19929122
    assert data['failed_edges'] > 0
    row = max(data['levels'], key=lambda r: r['maximum_deficit_integer'])
    w = row['witness']
    init_raw = (ROOT / 'reviews/2026-09-08/finite-control-integer-initialization.json').read_bytes()
    assert hashlib.sha256(init_raw).hexdigest() == data['initialization_sha256']
    init = json.loads(init_raw)
    scale, den = init['scale'], init['control_denominator']
    kernel = Kernel(320)
    z = F(w['control_units'], den)
    fee = rational(F(init['eta']) * z) / (2 * arb.pi()) - rational(F(init['alpha']) + F(init['delta']))
    energies = [2 * kernel.value(F(x, den))**2 for x in w['energy_argument_units']]
    assert rational_bounds(fee)[0] >= F(w['fee_lower_integer'], scale)
    for ball, lo in zip(energies, w['energy_lower_integers']):
        assert rational_bounds(ball)[0] >= F(lo, scale)
    true_candidate = rational(F(w['tail_offset_integer'], scale)) + fee + sum(energies, arb(0)) + rational(F(init['endpoint_loss']))
    true_deficit = rational(F(w['effective_label_integer'], scale)) - true_candidate
    rounding_slack = true_candidate - rational(F(w['candidate_integer'], scale))
    assert rational_bounds(rounding_slack)[0] >= 0
    assert rational_bounds(true_deficit)[0] > 0
    output = {
        'status': 'STRICT_REAL_PREFIX_CLOSURE_FAILURE', 'bits': 320,
        'scan_sha256': hashlib.sha256(raw).hexdigest(), 'scan_verifier_sha256': SOURCE_SHA,
        'witness_verifier_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'kernel_sha256': hashlib.sha256((ROOT / 'scripts/radius_five_arb_kernel.py').read_bytes()).hexdigest(),
        'witness': w, 'true_fee': enclosure(fee), 'true_energies': list(map(enclosure, energies)),
        'true_candidate': enclosure(true_candidate), 'true_deficit': enclosure(true_deficit),
        'downward_rounding_slack': enclosure(rounding_slack),
        'scope': 'A strict failure of the real same-child-or-prefix scalar sufficient criterion for this frozen label table. Does not prove negative full continuous h residual, failure of all certificates, or a changed zero proportion.'
    }
    destination = source.with_name('frozen-control-witness-arb.json')
    destination.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: output[k] for k in ('status', 'true_deficit', 'downward_rounding_slack')}))


if __name__ == '__main__':
    main()

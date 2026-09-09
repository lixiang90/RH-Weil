"""Check saved restart evidence and the unchanged Lean boundary, not RH."""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = ROOT.parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--git-index', action='store_true', help='Also check staged bytes after staging evidence.')
args = parser.parse_args()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


archive = WORKSPACE / 'archive/GOAL.20260906.md'
assert sha(archive) == '213a099265b8a88d5eb5ef6a9f0d5af0d595a8e52c6d1cb0e0f658929366e568'
assert not (WORKSPACE / 'GOAL.20260906.md').exists()
assert (WORKSPACE / 'GOAL.20260909.md').is_file()
scan_path = ROOT / 'reviews/2026-09-10/frozen-control-closure.json'
witness_path = scan_path.with_name('frozen-control-witness-arb.json')
scan, witness = [json.loads(p.read_bytes()) for p in (scan_path, witness_path)]
assert scan['complete'] and scan['all_inputs_unchanged']
assert scan['total_words'] == 19929122 and scan['total_edges'] == 6237815186
assert scan['failed_edges'] == 13755190
assert sum(r['edges'] for r in scan['levels']) == scan['total_edges']
assert sum(r['failed_edges'] for r in scan['levels']) == scan['failed_edges']
assert all(r['failed_edges'] == 0 for r in scan['levels'][:4])
assert all(r['minimum_offset_integer'] >= scan['offset_floor_integer'] for r in scan['levels'])
assert max(r['maximum_deficit_integer'] for r in scan['levels']) == 126501794
assert sha(ROOT / 'scripts/verify_frozen_control_closure.py') == scan['verifier_sha256']
assert scan['verifier_sha256'] == '77287d18687dd55a9032fa20396714ba2cca37d94560d98d0130ec22a203f60c'
assert sha(scan_path) == witness['scan_sha256']
assert sha(ROOT / 'scripts/verify_frozen_control_witness.py') == witness['witness_verifier_sha256']
assert sha(ROOT / 'scripts/radius_five_arb_kernel.py') == witness['kernel_sha256']
assert F(witness['true_deficit']['lower']) > F('0.0001265017922')
assert F(witness['true_deficit']['upper']) < F('0.0001265017923')
assert F(witness['downward_rounding_slack']['lower']) >= 0
assert F(witness['downward_rounding_slack']['upper']) < F('0.000000000002')
assert F(witness['true_deficit']['lower']) + F(1, 200000) > F(1, 100000)

audit = json.loads((ROOT / 'formal/checks/source-audit.json').read_bytes())
for path, expected in audit['own_source_sha256'].items():
    assert sha(ROOT / 'formal' / path) == expected, path
docs = [
    'README.md', 'RESEARCH_BRANCHES.md', 'goals/GOAL.20260909.md', 'goals/NEXT.20260909.md',
    'goals/ACCEPTANCE.cycle13.md', 'formal/blueprint/README.md',
    'notes/364-frozen-integer-candidate-verification.md',
    'notes/365-f1-rational-comparison-and-witt-coefficients.md',
    'reviews/2026-09-10/frozen-control-independent-review.md',
    'reviews/2026-09-10/f1-rational-witt-independent-review.md',
]
links = 0
for relative in docs:
    path = ROOT / relative
    raw = path.read_bytes()
    assert not re.search(rb'[\x00-\x08\x0b\x0c\x0e-\x1f]|\r(?!\n)', raw), relative
    text = raw.decode('utf-8')
    assert text.count('```') % 2 == 0, relative
    prose = re.sub(r'```[\s\S]*?```', '', text)
    prose = re.sub(r'`[^`\n]*`', '', prose)
    for match in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)', prose):
        target = match.group(1).split('#', 1)[0]
        if not target or '://' in target:
            continue
        destination = path.parent / target
        assert destination.is_dir() if target.endswith('/') else destination.is_file(), (relative, target)
        links += 1
literature = json.loads((ROOT / 'literature/manifest.json').read_bytes())
sources = []
for e in literature['entries']:
    if e.get('file') in {'f1/cc-complex-lift-1805.10501v1.pdf', 'f1/cc-arithmetic-site-1502.05580v1.pdf'}:
        assert sha(ROOT / 'literature' / e['file']) == e['sha256']
        assert any(r['date'] == '2026-09-10' for r in e['reading_updates'])
        sources.append({'path': e['file'], 'sha256': e['sha256']})
assert len(sources) == 2
git_blobs = None
if args.git_index:
    mirrors = json.loads((ROOT / 'goals/manifest.json').read_bytes())
    git_paths = [item['repository_path'] for item in mirrors] + [
        'reviews/2026-09-08/finite-control-integer-initialization.json',
        'reviews/2026-09-08/finite-control-integer-iteration.json',
        'reviews/2026-09-08/radius-five-rational-profile-candidate.json',
        'reviews/2026-09-08/kernel-curvature-tail-table.json',
        'reviews/2026-09-10/frozen-control-closure.json',
        'reviews/2026-09-10/frozen-control-witness-arb.json',
        'scripts/radius_five_arb_kernel.py', 'scripts/finite_control_integer_initialization.py',
        'scripts/finite_control_integer_iteration.py', 'scripts/verify_frozen_control_closure.py',
        'scripts/verify_frozen_control_witness.py',
    ]
    for relative in git_paths:
        staged = subprocess.check_output(['git', 'show', ':' + relative], cwd=ROOT)
        assert staged == (ROOT / relative).read_bytes(), relative
    git_blobs = len(git_paths)
report = {
    'status': 'PASS_SAVED_EVIDENCE', 'archive_byte_identity': True,
    'full_scan_status': scan['status'], 'scan_sha256': sha(scan_path),
    'witness_sha256': sha(witness_path), 'witness_script_sha256': witness['witness_verifier_sha256'],
    'edges_previously_scanned': scan['total_edges'], 'edges_repeated_by_this_check': 0,
    'unchanged_lean_sources': len(audit['own_source_sha256']), 'checked_document_links': links,
    'git_index_blobs_equal_to_verified_working_bytes': git_blobs,
    'document_sha256': {p: sha(ROOT / p) for p in docs}, 'source_pdfs': sources,
    'scope': 'Saved evidence, source binding and documentation integrity. Not an additional exhaustive scan or a new RH theorem.'
}
Path(__file__).with_name('goal-restart-validation.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: report[k] for k in ('status', 'full_scan_status', 'unchanged_lean_sources', 'checked_document_links')}))

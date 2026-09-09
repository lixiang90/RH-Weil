"""Preservation audit for the profile/twisted-module round, separately from b267533."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--git-index', action='store_true')
args=parser.parse_args()
digest=lambda b:hashlib.sha256(b).hexdigest()
notes=[next(ROOT.glob(f'notes/{n}-*.md')).relative_to(ROOT).as_posix() for n in (373,374)]
docs=notes+['reviews/2026-09-10/f1-profile-surjectivity-independent-review.md',
    'README.md','RESEARCH_BRANCHES.md','goals/GOAL.20260909.md',
    'goals/NEXT.20260909.md','goals/PROGRESS.md','literature/README.md']
for optional in ('f1-twisted-module-independent-review.md','f1-general-ff-geometric-source-audit.md'):
    p='reviews/2026-09-10/'+optional
    if (ROOT/p).exists(): docs.append(p)
links=0
for rel in docs:
    path=ROOT/rel
    raw=path.read_bytes()
    assert not re.search(rb'[\x00-\x08\x0b\x0c\x0e-\x1f]|\r(?!\n)',raw),rel
    text=raw.decode('utf-8')
    assert '\ufffd' not in text and text.count('```')%2==0,rel
    prose=re.sub(r'```[\s\S]*?```|`[^`\n]*`','',text)
    for match in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)',prose):
        target=match[1].split('#',1)[0]
        if target and '://' not in target:
            assert (path.parent/target).exists(),(rel,target)
            links+=1
boundary='### B. 较远期目标方向'.encode()
prior=(ROOT.parent/'archive/GOAL.20260909.f1-periodic.md').read_bytes()
assert digest(prior)=='d3e4bfecdfd18507cbe92e0579ce6f6c44d7fd83211a0914fc80167e7abbafd5'
assert prior.split(boundary,1)[1]==(ROOT.parent/'GOAL.20260909.md').read_bytes().split(boundary,1)[1]
goals=json.loads((ROOT/'goals/manifest.json').read_bytes())
assert len(goals)==18
for e in goals:
    assert digest((ROOT.parent/e['workspace_path']).read_bytes())==e['source_sha256']
    assert digest((ROOT/e['repository_path']).read_bytes())==e['mirror_sha256']
sources=json.loads((ROOT/'reviews/2026-09-10/f1-general-ff-source-download.json').read_bytes())
assert len(sources)==2
for e in sources:
    assert digest((ROOT/'literature'/e['file']).read_bytes())==e['sha256']
aud=json.loads((ROOT/'formal/checks/source-audit.json').read_bytes())
for rel,expected in aud['own_source_sha256'].items():
    assert digest((ROOT/'formal'/rel).read_bytes())==expected
indexed=0
if args.git_index:
    for rel in docs:
        raw=(ROOT/rel).read_bytes()
        staged=subprocess.check_output(['git','show',':'+rel],cwd=ROOT)
        if rel=='goals/GOAL.20260909.md': assert staged==raw
        else: assert staged.replace(b'\r\n',b'\n')==raw.replace(b'\r\n',b'\n'),rel
        indexed+=1
    for e in sources:
        staged=subprocess.check_output(['git','show',':literature/'+e['file']],cwd=ROOT)
        assert digest(staged)==e['sha256']
        indexed+=1
report=dict(status='PASS_SAVED_PROFILE_ROUND',checked_document_links=links,goal_mirrors=18,
    long_term_goal_bytes_unchanged=True,unchanged_lean_sources=len(aud['own_source_sha256']),
    git_index_checked_blobs=indexed,source_files=[{k:e[k] for k in ('file','sha256','pages')} for e in sources],
    document_sha256_raw={r:digest((ROOT/r).read_bytes()) for r in docs},
    document_sha256_lf={r:digest((ROOT/r).read_bytes().replace(b'\r\n',b'\n')) for r in docs},
    unreviewed_drafts=[r for r in notes if '[O]' in (ROOT/r).read_text(encoding='utf-8')[:180]],
    scope='Saved identities and links only. Mathematical review and source-reading scope are in their separate reports; no full FF, RR or RH certification.')
Path(__file__).with_name('f1-profile-round-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:report[k] for k in ('status','checked_document_links','git_index_checked_blobs','unreviewed_drafts')}))

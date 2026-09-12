"""Saved identities and references for 376–377; not a mathematical proof test."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--git-index',action='store_true')
args=parser.parse_args()
digest=lambda b:hashlib.sha256(b).hexdigest()
docs=[next(ROOT.glob(f'notes/{n}-*.md')).relative_to(ROOT).as_posix() for n in (376,377)]
docs += ['README.md','RESEARCH_BRANCHES.md','goals/GOAL.20260909.md','goals/NEXT.20260909.md',
         'goals/PROGRESS.md','literature/README.md']
docs += [p.relative_to(ROOT).as_posix() for p in sorted(Path(__file__).parent.glob('*.md'))]
links=0
for rel in docs:
    path=ROOT/rel
    raw=path.read_bytes()
    assert not re.search(rb'[\x00-\x08\x0b\x0c\x0e-\x1f]|\r(?!\n)',raw),rel
    source=raw.decode('utf-8')
    assert '\ufffd' not in source and source.count('```')%2==0,rel
    prose=re.sub(r'```[\s\S]*?```|`[^`\n]*`','',source)
    for m in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)',prose):
        target=m[1].split('#',1)[0]
        if target and '://' not in target:
            assert (path.parent/target).exists(),(rel,target)
            links+=1
prior=(ROOT.parent/'archive/GOAL.20260909.f1-real-scales.md').read_bytes()
assert digest(prior)=='3a7823c197fd60e29325b22b068cb959a6dbb54ac603a99dd6003eaec8647c23'
boundary='### B. 较远期目标方向'.encode()
assert prior.split(boundary,1)[1]==(ROOT.parent/'GOAL.20260909.md').read_bytes().split(boundary,1)[1]
goals=json.loads((ROOT/'goals/manifest.json').read_bytes())
assert len(goals)==19
for e in goals:
    assert digest((ROOT.parent/e['workspace_path']).read_bytes())==e['source_sha256']
    assert digest((ROOT/e['repository_path']).read_bytes())==e['mirror_sha256']
sources=json.loads((Path(__file__).parent/'f1-hahn-witt-source-download.json').read_bytes())
assert len(sources)==3
for e in sources:
    assert digest((ROOT/'literature'/e['file']).read_bytes())==e['sha256']
aud=json.loads((ROOT/'formal/checks/source-audit.json').read_bytes())
for rel,expected in aud['own_source_sha256'].items():
    assert digest((ROOT/'formal'/rel).read_bytes())==expected
assert digest((ROOT/'reviews/2026-09-10/frozen-control-closure.json').read_bytes())=='39f10f8bcb3d68012f74dac7839ebb9d6afad1892428366b11b5236103f5f875'
assert not subprocess.check_output(['git','diff','--name-only','--','formal','papers','paper-sections','output/pdf',
                                  'reviews/2026-09-10/frozen-control-closure.json'],cwd=ROOT).strip()
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
report=dict(status='PASS_SAVED_REAL_SCALE_ROUND',date='2026-09-13',checked_document_links=links,
    goal_mirrors=19,long_term_goal_bytes_unchanged=True,unchanged_lean_sources=len(aud['own_source_sha256']),
    git_index_checked_blobs=indexed,source_files=[{k:e[k] for k in ('file','sha256','pages')} for e in sources],
    document_sha256_raw={r:digest((ROOT/r).read_bytes()) for r in docs},
    document_sha256_lf={r:digest((ROOT/r).read_bytes().replace(b'\r\n',b'\n')) for r in docs},
    unreviewed_drafts=[r for r in docs[:2] if '[O]' in (ROOT/r).read_text(encoding='utf-8')[:180]],
    scope='Saved identities and links only. Independent mathematical and source reviews have their own scope; no full FF, RR, RH, or priority certification.')
Path(__file__).with_name('f1-real-round-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:report[k] for k in ('status','checked_document_links','git_index_checked_blobs','unreviewed_drafts')}))

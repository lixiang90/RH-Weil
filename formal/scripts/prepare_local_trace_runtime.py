"""Prepare this project's import closure on a local disk; report every missing artifact.
Use the pinned official cache to repair any missing modules, then rerun this command.
This copies generated artifacts only. Research sources and old junctions stay intact.
"""
from pathlib import Path
import os,sys,subprocess,re,json,hashlib,shutil,importlib.util,argparse
sys.stdout.reconfigure(encoding='utf-8')
r=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description="Copy the fixed import closure to a prepared local runtime without modifying source/cache originals")
parser.add_argument("--cache-backup",type=Path,required=True)
parser.add_argument("--runtime-dir",type=Path,required=True)
parser.add_argument("--entry",default="F1.Analysis.LocalTrace",help="Module whose source imports determine the dependency closure")
args=parser.parse_args()
backup=(r/args.cache_backup).resolve()
assert backup.is_relative_to(r)
m=backup/'mathlib'
revision=subprocess.check_output(["git","-C",str(m),"rev-parse","HEAD"],text=True).strip()
assert revision=="905b95818eb32af7874a58b427f50c1711a5e96c",revision
run=args.runtime_dir.resolve();out=run/'lib/lean';out.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('rh_bootstrap',r/'scripts/bootstrap_from_cache.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
roots=[r,m]+[p for p in (r/'vendor').iterdir() if p.is_dir()]
manifest=run/'cache-manifest.json'
if manifest.exists():
 assert json.loads(manifest.read_text(encoding='utf-8'))['mathlib_revision']==revision
libs=[out,r/'.lake/local-trace-check/lib/lean',m/'.lake/build/lib/lean']
for name in ['aesop','batteries','Qq','plausible','importGraph','LeanSearchClient','proofwidgets','Cli']:
 libs.extend([backup/('vendor-'+name)/'build/lib/lean',m/'.lake/packages'/name/'.lake/build/lib/lean'])
seen=set();files=[];missing=[];copied=0
def visit(name):
 global copied
 if name in seen or name.split('.')[0] in ['Lean','Std','Init','Lake']:return
 seen.add(name);relative=Path(*name.split('.'))
 source=next((root/relative.with_suffix('.lean') for root in roots if (root/relative.with_suffix('.lean')).is_file()),None)
 if source is None:raise RuntimeError('missing source '+name)
 text=mod.strip_comments(source.read_text(encoding='utf-8'))
 for names in re.findall(r'(?m)^(?:(?:public|private|meta)\s+)*import\s+([A-Za-z0-9_. ]+)',text):
  for dep in names.split():
   if dep!='all':visit(dep)
 if name.startswith('F1.'):return
 required=['.olean','.olean.server','.olean.private','.ir'];optional=[]
 for suffix in required+optional:
  rel=Path(str(relative)+suffix);artifact=next((lib/rel for lib in libs if (lib/rel).is_file()),None)
  if artifact is None:
   if suffix in required:missing.append({'module':name,'suffix':suffix})
   continue
  target=out/rel;target.parent.mkdir(parents=True,exist_ok=True)
  if not target.exists() or target.stat().st_size!=artifact.stat().st_size:shutil.copy2(artifact,target);copied+=1
  files.append({'module':name,'suffix':suffix,'source':str(artifact),'bytes':artifact.stat().st_size})
 if len(seen)%200==0:print('visited',len(seen),'copied',copied,'missing',len(missing),flush=True)
visit(args.entry)
report={'mathlib_revision':'905b95818eb32af7874a58b427f50c1711a5e96c','lean':'4.32.2','entry':args.entry,'modules':len(seen),'copied':copied,'files':files,'missing':missing}
(run/'cache-manifest.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'runtime':str(run),'modules':len(seen),'copied':copied,'missing':missing},ensure_ascii=False),flush=True)

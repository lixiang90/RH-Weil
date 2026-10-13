"""Frozen geometric R=M+K+U compression diagnostics; NOT a spectral certificate."""
import hashlib
import json
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'tmp/c009-liu/fresh-b-20261014'
OUT=ROOT/'reviews/2026-10-14/c010-inertia'
SIZES=(16,32,64)
PRECISION=80


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    paths=[RUN/'certificates/source-matrices.json',RUN/'certificates/tail-columns.json']
    expected=['4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac',
              '2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2']
    for p,h in zip(paths,expected):
        assert hashlib.sha256(p.read_bytes()).hexdigest()==h
    prereg={'sizes_per_parity':SIZES,'dps':PRECISION,'L':'17/16',
            'source_sha256':expected,'source_norm':'Lebesgue L2; raw Gamma=17/(8(2n+1))',
            'formula':'Rraw=Araw+J0raw+(648/17)(r0r0^T+r1r1^T); R=Gamma^-1/2 Rraw Gamma^-1/2',
            'scope':'Ordinary high precision exploration only; no zeros/data fitting or true Q spectrum claim.'}
    (OUT/'pilot-preregistration.json').write_text(json.dumps(prereg,indent=2)+'\n',encoding='utf-8')
    source,tail=(json.loads(p.read_text(encoding='utf-8')) for p in paths)
    mp.mp.dps=PRECISION
    scal=mp.mpf(2)**257
    mids={name:{(i,j):(mp.mpf(lo)+mp.mpf(hi))/scal
                for i,j,lo,hi in source['matrices'][name] if i<128 and j<128}
          for name in ('A','J0')}
    results=[]
    for sector in (0,1):
        for n in SIZES:
            degrees=list(range(sector,2*n,2))
            gamma=[mp.mpf(17)/(8*(2*i+1)) for i in degrees]
            r=[mp.mpf(tail['entries'][448*sector+i]['midTwice'])/(mp.mpf(2)**641)
               for i in degrees]
            mat=mp.matrix(n)
            for k,i in enumerate(degrees):
                for l,j in enumerate(degrees):
                    key=(min(i,j),max(i,j))
                    value=mids['A'][key]+mids['J0'][key]+mp.mpf(648)/17*r[k]*r[l]
                    mat[k,l]=value/mp.sqrt(gamma[k]*gamma[l])
            values,vecs=mp.eigsy(mat)
            row={'sector':sector,'n':n,'least_three':[mp.nstr(values[k],75) for k in range(3)],
                 'min_vector_normalized':[mp.nstr(vecs[k,0],75) for k in range(n)],
                 'min_vector_raw':[mp.nstr(vecs[k,0]/mp.sqrt(gamma[k]),75) for k in range(n)],
                 'residual_norm':mp.nstr(mp.norm(mat*vecs[:,0]-values[0]*vecs[:,0]),20)}
            results.append(row)
            print(sector,n,row['least_three'],flush=True)
    (OUT/'source-compression-pilot.json').write_text(json.dumps({'preregistration':prereg,'results':results},indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()

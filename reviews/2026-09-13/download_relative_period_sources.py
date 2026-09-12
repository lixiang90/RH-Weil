"""Archive fixed relative-period-ring references for subsequent interface checks."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import io
import json
import urllib.request
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
sources=[
    ('KL-foundations-1301.0792v5','Kiran S. Kedlaya; Ruochuan Liu','Relative p-adic Hodge theory: Foundations','1301.0792v5','2015-05-09'),
    ('KL-imperfect-1602.06899v3','Kiran S. Kedlaya; Ruochuan Liu','Relative p-adic Hodge theory, II: Imperfect period rings','1602.06899v3','2019-10-21'),
    ('Tong-big-coefficients-2012.07338v1','Xin Tong','Period Rings with Big Coefficients and Applications I','2012.07338v1','2020-12-14'),
]
records=[]
for ident,authors,title,version,date in sources:
    item=dict(id=ident,authors=authors,title=title,version='arXiv:'+version+', '+date,
              category='f1',source_url='https://arxiv.org/abs/'+version,
              pdf_url='https://arxiv.org/pdf/'+version,file='f1/'+ident.lower()+'.pdf',attempted_on='2026-09-13')
    path=ROOT/'literature'/item['file']
    try:
        if path.exists():
            data=path.read_bytes()
            item['download_reused']=True
        else:
            req=urllib.request.Request(item['pdf_url'],headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=45) as response:
                data=response.read()
                item['resolved_pdf_url']=response.url
        assert data.startswith(b'%PDF-')
        r=PdfReader(io.BytesIO(data))
        lengths=[len(p.extract_text() or '') for p in r.pages]
        if not path.exists(): path.write_bytes(data)
        item.update(download_status='downloaded',bytes=len(data),pages=len(r.pages),sha256=hashlib.sha256(data).hexdigest(),
                    retrieved_at_utc=datetime.now(timezone.utc).isoformat(),pdf_parse_status='all pages parsed',
                    text_characters=sum(lengths),empty_text_pages=[i+1 for i,n in enumerate(lengths) if n==0],
                    status='固定原件归档并全页解析；仅核对元数据，证明／与378的系数环接口尚未审查。')
    except Exception as e:
        item.update(download_status='failed',error=str(e),status='获取失败，未核读原件。')
        item.pop('file',None)
    records.append(item)
    print(json.dumps({k:item.get(k) for k in ('id','download_status','pages','sha256','error')}),flush=True)
Path(__file__).with_name('f1-relative-period-source-download.json').write_text(
    json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

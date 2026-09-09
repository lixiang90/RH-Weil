"""Save fixed primary F1 sources; byte preservation/parse is not proof review."""
from pathlib import Path
from datetime import datetime, timezone
import concurrent.futures
import hashlib
import json
import urllib.request
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
SOURCES = [
    ('Borger-2009-F1', 'James Borger', 'Lambda-rings and the field with one element', '0906.3146v1', 'borger-lambda-rings-0906.3146v1.pdf'),
    ('Lorscheid-2012-blueprints', 'Oliver Lorscheid', 'The geometry of blueprints. Part I: Algebraic background and scheme theory', '1103.1745v2', 'lorscheid-blueprints-1103.1745v2.pdf'),
    ('CC-2015-arithmetic-site', 'Alain Connes; Caterina Consani', 'Geometry of the arithmetic site', '1502.05580v1', 'cc-arithmetic-site-1502.05580v1.pdf'),
    ('CC-2016-scaling-site', 'Alain Connes; Caterina Consani', 'Geometry of the scaling site', '1603.03191v1', 'cc-scaling-site-1603.03191v1.pdf'),
    ('CC-2018-complex-lift', 'Alain Connes; Caterina Consani', 'The Riemann-Roch strategy, Complex lift of the Scaling Site', '1805.10501v1', 'cc-complex-lift-1805.10501v1.pdf'),
    ('CC-2023-RR-Z', 'Alain Connes; Caterina Consani', 'Riemann-Roch for the ring Z', '2306.00456v1', 'cc-riemann-roch-z-2306.00456v1.pdf'),
    ('CC-2026-Jacobian', 'Alain Connes; Caterina Consani', 'On the Jacobian of the Arakelov compactification of Spec Z', '2602.15941v1', 'cc-jacobian-2602.15941v1.pdf'),
    ('CC-2026-absolute-geometry', 'Alain Connes; Caterina Consani', 'On the Absolute Geometry of Spec Z', '2606.06604v1', 'cc-absolute-geometry-2606.06604v1.pdf'),
]

def fetch(row):
    key, authors, title, version, filename = row
    url = 'https://arxiv.org/pdf/' + version
    path = ROOT / 'literature/f1' / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({'http': 'http://127.0.0.1:10808', 'https': 'http://127.0.0.1:10808'}))
    with opener.open(urllib.request.Request(url, headers={'User-Agent': 'RH-Weil literature archive'}), timeout=55) as response:
        raw = response.read()
        resolved = response.url
    assert raw.startswith(b'%PDF-'), (key, raw[:40])
    if path.exists():
        assert path.read_bytes() == raw, 'Refusing to overwrite a changed archived source'
    else:
        path.write_bytes(raw)
    reader = PdfReader(path)
    pages = [p.extract_text() or '' for p in reader.pages]
    temporary = ROOT / 'tmp/pdfs/f1'
    temporary.mkdir(parents=True, exist_ok=True)
    (temporary / (filename + '.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n{text}' for i, text in enumerate(pages)), encoding='utf-8')
    return dict(id=key, category='f1', authors=authors, title=title,
                version='arXiv:' + version, file='f1/' + filename,
                source_url='https://arxiv.org/abs/' + version, pdf_url=url,
                resolved_pdf_url=resolved, download_status='downloaded',
                bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
                retrieved_at_utc=datetime.now(timezone.utc).isoformat(),
                pages=len(pages), pdf_parse_status='all pages parsed',
                text_characters=sum(map(len, pages)),
                pdf_metadata_title=(reader.metadata.title or '') if reader.metadata else '',
                status='原始PDF归档；数学核读范围另记，下载不等于认证')

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        entries = list(pool.map(fetch, SOURCES))
    (Path(__file__).parent / 'f1-source-download.json').write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for entry in entries:
        print(entry['id'], entry['pages'], entry['sha256'])

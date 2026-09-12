"""Archive fixed primary sources; parsing is not a mathematical full-text audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import io
import json
import urllib.request
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
sources = [
    dict(id="Poonen-maximally-complete-author-20260913", authors="Bjorn Poonen",
         title="Maximally complete fields",
         version="Author copy retrieved 2026-09-13; dated March 4, 1992; published L'Enseignement Mathématique 39 (1993), 87–106",
         file="f1/poonen-maximally-complete-author-20260913.pdf",
         source_url="https://math.mit.edu/~poonen/",
         pdf_url="https://math.mit.edu/~poonen/papers/amsval.pdf"),
    dict(id="Kedlaya-power-series-math-9906030v2", authors="Kiran S. Kedlaya",
         title="Power series and p-adic algebraic closures",
         version="arXiv:math/9906030v2, 1999-12-16; replaces v1 with corrected proof of Theorem 1",
         file="f1/kedlaya-power-series-math-9906030v2.pdf",
         source_url="https://arxiv.org/abs/math/9906030v2",
         pdf_url="https://arxiv.org/pdf/math/9906030v2"),
    dict(id="Efimov-hahn-witt-2406.19163v1", authors="Alexander I. Efimov",
         title="On the Hahn-Witt series and their generalizations",
         version="arXiv:2406.19163v1, 2024-06-27",
         file="f1/efimov-hahn-witt-2406.19163v1.pdf",
         source_url="https://arxiv.org/abs/2406.19163v1",
         pdf_url="https://arxiv.org/pdf/2406.19163v1"),
]
records = []
for item in sources:
    entry = dict(item, category="f1", attempted_on="2026-09-13")
    path = ROOT / "literature" / entry["file"]
    try:
        if path.exists():
            data = path.read_bytes()
            entry["download_reused"] = True
        else:
            req = urllib.request.Request(entry["pdf_url"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read()
                entry["resolved_pdf_url"] = response.url
        assert data.startswith(b"%PDF-"), "Response was not a PDF"
        reader = PdfReader(io.BytesIO(data))
        lengths = [len(page.extract_text() or "") for page in reader.pages]
        if not path.exists():
            path.write_bytes(data)
        entry.update(download_status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                     pages=len(lengths), pdf_parse_status="all pages parsed", text_characters=sum(lengths),
                     empty_text_pages=[i+1 for i, n in enumerate(lengths) if n == 0],
                     retrieved_at_utc=datetime.now(timezone.utc).isoformat(),
                     status="原始版本归档、全页解析；只核对标题／作者与版本，尚未核读证明。")
    except Exception as error:
        entry.update(download_status="failed", error=str(error), status="获取失败；未核读原件。")
        entry.pop("file", None)
    records.append(entry)
    print(json.dumps({k: entry.get(k) for k in ("id", "download_status", "pages", "sha256", "error")}), flush=True)
Path(__file__).with_name("f1-hahn-witt-source-download.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")

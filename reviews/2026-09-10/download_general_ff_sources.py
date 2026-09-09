"""Archive public author copies for the general-perfectoid-field interface."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import io
import json
import urllib.request
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
sources = [
    dict(id="FF-Courbe-author-20260910", authors="Laurent Fargues; Jean-Marc Fontaine; preface by Pierre Colmez",
         title="Courbes et fibrés vectoriels en théorie de Hodge p-adique",
         version="Author-hosted full manuscript, snapshot 2026-09-10; not asserted byte-identical to Astérisque 406",
         file="f1/ff-courbe-author-20260910.pdf",
         source_url="https://webusers.imj-prg.fr/~laurent.fargues/Publications.html",
         pdf_url="https://webusers.imj-prg.fr/~laurent.fargues/Courbe_fichier_principal.pdf"),
    dict(id="Lurie-FF-overview-author-20260910", authors="Jacob Lurie",
         title="Lecture 1: Overview", version="Author copy under ffcurve/, snapshot 2026-09-10; distinct from 205notes lectures",
         file="f1/lurie-ffcurve-overview-20260910.pdf",
         source_url="https://www.math.ias.edu/~lurie/FF.html",
         pdf_url="https://www.math.ias.edu/~lurie/ffcurve/Lecture1-Overview.pdf"),
]
records = []
for entry in sources:
    entry.update(category="f1", attempted_on="2026-09-10")
    path = ROOT / "literature" / entry["file"]
    assert not path.exists(), path
    try:
        req = urllib.request.Request(entry["pdf_url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
            entry["resolved_pdf_url"] = response.url
        assert data.startswith(b"%PDF-"), "Response was not a PDF"
        reader = PdfReader(io.BytesIO(data))
        lengths = [len(page.extract_text() or "") for page in reader.pages]
        path.write_bytes(data)
        entry.update(download_status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                     pages=len(lengths), pdf_parse_status="all pages parsed", text_characters=sum(lengths),
                     empty_text_pages=[i+1 for i, length in enumerate(lengths) if length == 0],
                     retrieved_at_utc=datetime.now(timezone.utc).isoformat(),
                     status="原始版本归档、全页解析；当前仅定位一般F章节／开篇警告，未核审全文。")
    except Exception as error:
        entry.update(download_status="failed", error=str(error), status="获取失败；未核读原件全文。")
        entry.pop("file", None)
    records.append(entry)
    print(json.dumps({k: entry.get(k) for k in ("id", "download_status", "pages", "sha256", "error")}), flush=True)
Path(__file__).with_name("f1-general-ff-source-download.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")

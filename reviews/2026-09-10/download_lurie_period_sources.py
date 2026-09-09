"""Archive the primary lecture PDFs used for the next period-ring comparison."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
NAMES = {
    6: "Lecture6-Curve.pdf", 8: "Lecture8-BdR.pdf",
    11: "Lecture11-TrivialEigenspaces.pdf", 19: "Lecture19-LineBundles.pdf",
}

def fetch(item):
    number, name = item
    url = "https://www.math.ias.edu/~lurie/205notes/" + name
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({
        "http": "http://127.0.0.1:10808", "https": "http://127.0.0.1:10808"}))
    with opener.open(url, timeout=45) as response:
        data, resolved = response.read(), response.url
    assert data.startswith(b"%PDF-")
    relative = f"f1/lurie-2018-lecture{number:02d}.pdf"
    (ROOT / "literature" / relative).write_bytes(data)
    return {
        "id": f"Lurie-FF-2018-L{number:02d}", "category": "f1", "authors": "Jacob Lurie",
        "title": name.removesuffix(".pdf"), "version": "Math 205, Fall 2018; author-hosted lecture notes",
        "file": relative, "source_url": "https://www.math.ias.edu/~lurie/205.html",
        "pdf_url": url, "resolved_pdf_url": resolved, "download_status": "downloaded",
        "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
        "retrieved_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, NAMES.items()))
    destination = ROOT / "reviews/2026-09-10/f1-lurie-source-download.json"
    destination.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(records, ensure_ascii=False))

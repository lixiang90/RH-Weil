"""Register archived originals and the precise additional reading scope."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / "literature/manifest.json"
manifest = json.loads(path.read_bytes())
scopes = {
    "f1/cc-complex-lift-1805.10501v1.pdf": (
        "PDF18–22页Jensen、23–27页Jessen陈述；31–38、42–44、62–65页指定轨道、字符及右作用命题。"
        "Jensen公式页20及关键字符公式经渲染；全局算术平方、全部完备化和RR未认证。",
        "reviews/2026-09-10/f1-classical-orbit-source-audit.md",
    ),
    "f1/cc-scaling-site-1603.03191v1.pdf": (
        "PDF21–29页§5.1–5.3：Hp系数、阶数、deg/chi主除子条件、theta及仿射余循环；"
        "23页定义与定理经渲染。本文重建指定除子的有限斜率方程，不宣称全文RR或全部Pic满性重审。",
        "notes/368-f1-tropical-theta-and-coefficient-obstruction.md",
    ),
}
for entry in manifest["entries"]:
    if entry.get("file") in scopes:
        scope, note = scopes[entry["file"]]
        update = {"date": "2026-09-10", "scope": scope, "note": note}
        updates = entry.setdefault("reading_updates", [])
        if update not in updates:
            updates.append(update)

download = json.loads((ROOT / "reviews/2026-09-10/f1-cartier-source-download.json").read_bytes())
entry = {
    "id": "Stacks-Divisors-ed88ff78", "category": "background", "authors": "The Stacks Project Authors",
    "title": "Divisors", "version": download["version"],
    "file": download["file"].removeprefix("literature/"),
    "source_url": download["source_url"], "pdf_url": download["pdf_url"],
    "resolved_pdf_url": download["pdf_url"], "download_status": "downloaded",
    "status": "定义来源；采用局部环空间上的正则截面／亚纯层，不移植scheme专属结论",
    **{k: download[k] for k in ("sha256", "bytes", "pages", "retrieved_at_utc", "pdf_parse_status", "text_characters")},
    "reading_scope": "PDF57页Tag01X1定义、茎与全商环警告，已渲染核对；全部94页文字解析通过。",
}
manifest["entries"] = [e for e in manifest["entries"] if e["id"] != entry["id"]] + [entry]
suffix = "; 2026-09-10：周期Cartier/字符族与热带theta比较来源"
if suffix not in manifest["scope"]:
    manifest["scope"] += suffix
path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print("Registered archived Stacks PDF and two precise reading updates.")

"""ROOT metadata writer/charge journal. No scientific model/array evaluation."""
from pathlib import Path
import hashlib
import json
import os
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PLAN = HERE / "root-administrative-reserve-plan.json"
LOG = HERE / "root-admin-write-log.jsonl"


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def packed(v):
    return (json.dumps(v, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def charge_record(relative, raw, prepaid_elsewhere=False, event="WRITE"):
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    need(plan["prechargedBytes"] == 1048576 and plan["nonRefundable"] is True, "RESERVE_PLAN")
    total = plan["preInstrumentationUpperBytes"]
    if LOG.exists():
        for line in LOG.read_bytes().splitlines():
            row = json.loads(line)
            need(row["previousTotal"] == total, "ADMIN_JOURNAL_CHAIN")
            total = row["totalAfter"]
    content = 0 if prepaid_elsewhere else len(raw)
    entry = dict(event=event, path=relative, rawBytes=len(raw),
                 sha256=hashlib.sha256(raw).hexdigest(), chargedContentBytes=content,
                 prepaidElsewhere=prepaid_elsewhere, previousTotal=total,
                 observedUTC=datetime.now(timezone.utc).isoformat(), totalAfter=0)
    for _ in range(10):
        encoded = (json.dumps(entry, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
        target = total + content + len(encoded)
        if entry["totalAfter"] == target:
            break
        entry["totalAfter"] = target
    else:
        raise ValueError("ADMIN_JOURNAL_SIZE_FIXED_POINT")
    need(entry["totalAfter"] <= plan["prechargedBytes"], "ROOT_ADMIN_RESERVE_EXHAUSTED")
    with LOG.open("ab") as f:
        f.write(encoded)
        f.flush()
        os.fsync(f.fileno())
    return entry


def write_json(relative, value, *, prepaid_elsewhere=False, fresh=False):
    need(type(relative) is str and relative and ":" not in relative and "\\" not in relative
         and all(s not in ("", ".", "..") for s in relative.split("/")), "CANONICAL_ROOT_RECORD_PATH")
    p = (ROOT / relative).resolve()
    need(p.is_relative_to(ROOT), "ROOT_METADATA_PATH")
    if prepaid_elsewhere:
        need(relative == "literature/local/2026-11-01-directional-remainder-whole-observer/run-01/source-produce/root-observed.json",
             "EXACT_PREPAID_ROOT_RECEIPT_ONLY")
        need(fresh, "PREPAID_ROOT_RECEIPT_MUST_BE_FRESH")
    if not prepaid_elsewhere:
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        need(relative in plan["mutableExactPaths"] or any(relative.startswith(s) for s in plan["mutablePrefixes"]),
             "ROOT_ADMIN_PATH_SCOPE")
    raw = packed(value)
    need(len(raw) < (16000 if relative == "goals/STATE.json" else 131072), "BOUNDED_ROOT_RECORD")
    if fresh:
        need(not p.exists(), "ROOT_RECORD_ALREADY_EXISTS")
    charge_record(relative, raw, prepaid_elsewhere)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".c069-root.tmp")
    with tmp.open("xb") as f:
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, p)
    return dict(path=relative, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


if __name__ == "__main__":
    raise SystemExit("ROOT metadata library only; no source/ARM launch path")

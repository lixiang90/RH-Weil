# Pivot-log status field: inverted metadata, unchanged bytes

2026-11-01; `/root/retained_tail_source_design`. Metadata-only clarification. Recovered STATE/check/show and inspected frozen code, terminal-result metadata and output names/sizes. No pivot values, matrices, source coefficients, inverse or sign computation was read/replayed here. No code/result/source was changed. Zero new mathematics.

The frozen code ed32fa2749c11c1dd1adae3bb078a331c5206a9d79f975a23c45e7df5f2fb7c3 has a serialization bug at PivotLog.record: `closed=not self.handle.closed`. Python's `handle.closed` is already true after close; negating it writes false. Thus the terminal `pivotLog.closed=false` means that this expression observed a CLOSED handle. The field name and stored Boolean are inconsistent. It must not be consumed as a truthful assertion that the file remained open.

The successful path calls `log.finish()` before final source/self/freeze/log checks. Finish flushes and fsyncs the handle, closes it, then renames pivots.jsonl.part to pivots.jsonl. Afterwards the program reads the published file and requires its bytes/SHA to equal the accumulated log record before writing the terminal result. The supplied terminal observation is process80570 exit0. Together these facts support successful close/publication; rename alone would not prove complete sign verification, because the exception path can also finish a partial log.

Actual metadata inspected:

- result.json:5676bytes, SHA ba31ccef92293cdc1f308ea05bdd507b5d2fb4695cbfab6c341aa74718d4ea4e; status POSITIVE_HEAD_ONLY,248.6810276000033seconds; both sectors report224 positive upper and224 positive lower pivots.
- Declared pivots.jsonl:896rows,636836bytes, SHA0198a20e06349bcc8f2a53a9a38e35d44bd79d45382a163d4b5c2f13d2ee5366. The directory stat agrees on size and shows only pivots.jsonl,progress.json,result.json; no .part/.tmp remains. This task did not hash/read the pivot contents afresh.

External root closure must preserve the erroneous raw Boolean and explicitly record the real closed/published-log evidence: terminal exit0, audited finish-before-record control flow, final filename/no partial, and independently verified actual log bytes/SHA/count. Root/result-fresh must separately verify the896 pivot records, complete sector/phase coverage, source pins and mathematical implications. This note does not substitute for that audit.

The bug does not enter matrix assembly, interval arithmetic, pivots, source-error slack or sign branches. Subject to the independent result audit, the mathematical status is unchanged: strict finite HEAD positivity only, not whole Lret/Q positivity or RH. No rerun or retroactive edit is needed to document this bounded metadata discrepancy; no old/new source acceptance scope is enlarged.

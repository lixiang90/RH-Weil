"""One or more exact-integer relaxations of the sparse four-word graph.

Grouped minima are only an acceleration of all stored tail/control edges.
Even a stable pass still requires the separate complete final verifier.
"""

import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from finite_control_integer_initialization import ROOT, WORK, SCALE, array_digest, save_array

INF = 10**16


def checked_array(record):
    array = np.load(ROOT / record["path"],mmap_mode="r")
    assert list(array.shape) == record["shape"] and str(array.dtype) == record["dtype"]
    assert array_digest(array) == record["data_sha256"]
    return array


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds",type=int,default=1)
    parser.add_argument("--resume",action="store_true")
    args = parser.parse_args()
    source = ROOT / "reviews/2026-09-08/finite-control-integer-initialization.json"
    raw = source.read_bytes()
    init = json.loads(raw)
    q = init["control_count"]
    units = checked_array(init["kernel_arrays"]["units"])
    values = checked_array(init["kernel_arrays"]["energy_lower"])
    fees = checked_array(init["kernel_arrays"]["fees_lower"])
    prefix_best = checked_array(init["records"][2]["prefix_best"])
    assert len(prefix_best) == q**3 and np.max(prefix_best) <= 0
    loss_scaled = 5000000
    assert init["scale"] == SCALE and init["endpoint_loss"] == "1/200000"
    scalar = fees+values[units]+loss_scaled
    output_path = source.with_name("finite-control-integer-iteration.json")
    if args.resume:
        previous = json.loads(output_path.read_bytes())
        assert previous["initialization_sha256"] == hashlib.sha256(raw).hexdigest()
        codes = checked_array(previous["current_codes"])
        offsets = checked_array(previous["current_offsets"])
        history = previous["history"]
    else:
        codes = checked_array(init["records"][3]["codes"])
        offsets = checked_array(init["records"][3]["offsets"])
        history = []
    assert INF+100*SCALE < np.iinfo(np.int64).max
    assert np.all(codes[1:] > codes[:-1])
    for iteration in range(len(history),len(history)+args.rounds):
        start_time = time.perf_counter()
        prefixes, starts, counts = np.unique(codes//q,return_index=True,return_counts=True)
        updates_c,updates_b = [],[]
        evaluated,processed,update_count = 0,0,0
        max_defect,minimum_candidate = 0,0
        bucket = 1
        while bucket < int(counts.max()):
            bucket *= 2
        capacities = [2**i for i in range(bucket.bit_length())]
        for capacity in capacities:
            selected = np.flatnonzero((counts > capacity//2) & (counts <= capacity))
            batch = max(1,min(128,2000000//(q*capacity)))
            for low in range(0,len(selected),batch):
                group_ids = selected[low:low+batch]
                u = prefixes[group_ids]
                positions = starts[group_ids,None]+np.arange(capacity)[None,:]
                valid = np.arange(capacity)[None,:] < counts[group_ids,None]
                positions = np.minimum(positions,len(codes)-1)
                tail_b = np.where(valid,offsets[positions],INF)
                tail_last = units[codes[positions] % q]
                digits = np.column_stack([u//q**2,(u//q) % q,u % q])
                partials = np.cumsum(units[digits],axis=1)
                arguments = units[None,:,None]+partials[:,-1,None,None]+tail_last[:,None,:]
                assert arguments.max() < len(values)
                candidate = np.min(tail_b[:,None,:]+values[arguments],axis=2)
                candidate += scalar[None,:]
                for j in range(3):
                    candidate += values[partials[:,j,None]+units[None,:]]
                child_codes = np.arange(q,dtype=np.int64)[None,:]*q**3+u[:,None]
                threshold = prefix_best[child_codes//q]
                positions = np.minimum(np.searchsorted(codes,child_codes),len(codes)-1)
                present = codes[positions] == child_codes
                existing = np.where(present,offsets[positions],threshold)
                effective = np.minimum(existing,threshold)
                deficit = effective-candidate
                max_defect = max(max_defect,int(deficit.max()))
                minimum_candidate = min(minimum_candidate,int(candidate.min()))
                rows,cols = np.nonzero(deficit > 0)
                updates_c.append(child_codes[rows,cols])
                updates_b.append(candidate[rows,cols])
                update_count += len(rows)
                evaluated += q*int(np.sum(counts[group_ids]))
                processed += len(group_ids)
                if update_count > 20000000:
                    raise RuntimeError("Update storage cap exceeded; no closure claim")
            if len(selected):
                print(f"round {iteration}, fanout <= {capacity}, groups {processed}/{len(prefixes)}, "
                      f"updates {update_count}, max deficit {max_defect}/{SCALE}",flush=True)
        assert evaluated == len(codes)*q and processed == len(prefixes)
        assert minimum_candidate >= -7000000000, "Required offset floor violated"
        update_codes = np.concatenate(updates_c)
        update_values = np.concatenate(updates_b)
        if len(update_codes):
            order = np.argsort(update_codes)
            update_codes,update_values = update_codes[order],update_values[order]
            assert np.all(update_codes[1:] > update_codes[:-1])
            combined = np.union1d(codes,update_codes)
            if len(combined) > 30000000:
                raise RuntimeError("State storage cap exceeded; no closure claim")
            combined_b = np.zeros(len(combined),dtype=np.int64)
            combined_b[np.searchsorted(combined,codes)] = offsets
            where = np.searchsorted(combined,update_codes)
            combined_b[where] = np.minimum(combined_b[where],update_values)
            codes,offsets = combined,combined_b
        assert np.all(offsets < prefix_best[codes//q])
        assert int(offsets.min()) >= -7000000000
        current_codes = save_array(f"iteration-{iteration+1}-codes.npy",np.asarray(codes))
        current_offsets = save_array(f"iteration-{iteration+1}-offsets.npy",np.asarray(offsets))
        history.append(dict(round=iteration,previous_tail_count=evaluated//q,
                            evaluated_edges=evaluated,groups=processed,
                            updated_head_count=update_count,maximum_deficit_integer=str(max_defect),
                            resulting_tail_count=len(codes),minimum_offset_integer=str(int(offsets.min())),
                            elapsed_seconds=time.perf_counter()-start_time))
        output = dict(status="Stable grouped pass; final independent full scan still required" if not update_count
                             else "Integer labels updated; endpoint closure remains open",
                      initialization_sha256=hashlib.sha256(raw).hexdigest(),
                      current_codes=current_codes,current_offsets=current_offsets,
                      history=history,
                      scope="Exact integer arithmetic using certified lower scalar costs. This search is not a final certificate.")
        output_path.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
        print(f"round {iteration} complete: {len(codes)} states, {update_count} changed heads",flush=True)
        if not update_count:
            break


if __name__ == "__main__":
    main()

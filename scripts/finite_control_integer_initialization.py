"""Integer short-word initialization for the finite control closure problem.

All costs use certified downward scalar bounds. Depth four is not closure.
Large arrays stay in the ignored local work directory; hashes are recorded.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from radius_five_arb_kernel import Kernel, PROFILE_SHA256, arb, rational, rational_bounds

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "tmp/control-closure"
SCALE = 10**12
DENOMINATOR = 80


def floor_scaled(value):
    lo = rational_bounds(value)[0]
    return lo.numerator*SCALE//lo.denominator


def array_digest(value):
    return hashlib.sha256(value.tobytes(order="C")).hexdigest()


def save_array(name, value):
    path = WORK / name
    np.save(path, value)
    return dict(path=str(path.relative_to(ROOT)).replace("\\","/"),
                shape=list(value.shape), dtype=str(value.dtype),
                data_sha256=array_digest(value), bytes=value.nbytes)


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    source = ROOT / "reviews/2026-09-08/kernel-curvature-tail-table.json"
    raw = source.read_bytes()
    data = json.loads(raw)
    assert data["profile_sha256"] == PROFILE_SHA256
    controls = list(map(F, data["control_nodes"]))
    assert all(v*DENOMINATOR == int(v*DENOMINATOR) for v in controls)
    units = np.array([int(v*DENOMINATOR) for v in controls], dtype=np.int64)
    q = len(units)
    alpha, eta, delta = [F(data[k]) for k in ("alpha","eta","delta")]
    loss = delta/2
    assert loss*SCALE == int(loss*SCALE)
    loss_scaled = int(loss*SCALE)
    kernel = Kernel(192)
    values = np.zeros(5*int(units.max())+1, dtype=np.int64)
    for index in range(int(units.min()), len(values)):
        k = kernel.value(F(index,DENOMINATOR))
        values[index] = max(0, floor_scaled(2*k*k))
    assert np.all((0 <= values) & (values <= 2*SCALE))
    fees = np.array([floor_scaled(rational(eta*z)/(2*arb.pi())-rational(alpha+delta))
                     for z in controls], dtype=np.int64)
    assert np.max(abs(fees)) <= SCALE
    assert 100*SCALE < np.iinfo(np.int64).max
    scalar = fees+values[units]+loss_scaled
    kernel_arrays = dict(units=save_array("control-units.npy",units),
                         energy_lower=save_array("energy-lower.npy",values),
                         fees_lower=save_array("fees-lower.npy",fees))
    codes, offsets = np.array([0],dtype=np.int64), np.array([0],dtype=np.int64)
    prefix_best = np.array([0],dtype=np.int64)
    records = []
    start = time.perf_counter()
    for depth in range(1,5):
        kept_codes, kept_offsets = [], []
        negative_count = 0
        for low in range(0,len(codes),64):
            parent_codes = codes[low:low+64]
            costs = offsets[low:low+64,None]+scalar[None,:]
            if depth > 1:
                digits = np.column_stack([(parent_codes//q**j) % q for j in range(depth-2,-1,-1)])
                prefixes = np.cumsum(units[digits],axis=1)
                for j in range(depth-1):
                    argument = prefixes[:,j,None]+units[None,:]
                    assert argument.max() < len(values)
                    costs += values[argument]
                child_prefix = np.arange(q,dtype=np.int64)[None,:]*q**(depth-2)+parent_codes[:,None]//q
                threshold = prefix_best[child_prefix]
            else:
                threshold = np.zeros_like(costs)
            negative_count += int(np.sum(costs < 0))
            rows, cols = np.nonzero(costs < threshold)
            new_codes = cols.astype(np.int64)*q**(depth-1)+parent_codes[rows]
            kept_codes.append(new_codes)
            kept_offsets.append(costs[rows,cols])
        new_codes, new_offsets = np.concatenate(kept_codes),np.concatenate(kept_offsets)
        order = np.argsort(new_codes)
        new_codes, new_offsets = new_codes[order],new_offsets[order]
        assert np.all(new_codes[1:] > new_codes[:-1])
        assert np.all(new_offsets < 0)
        assert int(new_offsets.min()) >= int(F(data["offset_floor"])*SCALE)
        record = dict(depth=depth,parent_count=len(codes),
                      extensions=len(codes)*q,negative_extensions=negative_count,
                      retained_count=len(new_codes),minimum_offset_integer=str(int(new_offsets.min())),
                      codes=save_array(f"level-{depth}-codes.npy",new_codes),
                      offsets=save_array(f"level-{depth}-offsets.npy",new_offsets))
        if depth < 4:
            prefix_best = np.repeat(prefix_best,q)
            prefix_best[new_codes] = np.minimum(prefix_best[new_codes],new_offsets)
            record["prefix_best"] = save_array(f"prefix-best-{depth}.npy",prefix_best)
        records.append(record)
        print(f"integer depth {depth}: {len(new_codes)} retained, min {int(new_offsets.min())}/{SCALE}",flush=True)
        codes,offsets = new_codes,new_offsets
        output = dict(status="Integer short-word initialization only; length-four closure remains open",
                      table_sha256=hashlib.sha256(raw).hexdigest(),profile_sha256=PROFILE_SHA256,
                      control_count=q,control_denominator=DENOMINATOR,scale=SCALE,
                      alpha=str(alpha),eta=str(eta),delta=str(delta),endpoint_loss=str(loss),
                      offset_floor=data["offset_floor"],kernel_arrays=kernel_arrays,
                      records=records,elapsed_seconds=time.perf_counter()-start,
                      scope="All stored offsets are exact integers chosen using lower energy/fee bounds. No final fixed point or endpoint scan is claimed.")
        (source.parent/"finite-control-integer-initialization.json").write_text(
            json.dumps(output,indent=2)+"\n",encoding="utf-8")


if __name__ == "__main__":
    main()

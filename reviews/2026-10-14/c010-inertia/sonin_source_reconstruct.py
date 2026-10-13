"""Independent small source assembly. Ordinary 80-digit diagnostic only."""
from pathlib import Path
import hashlib
import json
import mpmath as mp

BASE = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
INPUT = BASE / "tmp/c009-liu/fresh-b-20261014/certificates"
mp.mp.dps = 80
EXPECTED = {
    "source-matrices.json": "4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac",
    "tail-columns.json": "2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2",
}
packets = {}
for name, expected in EXPECTED.items():
    raw = (INPUT / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected
    packets[name] = json.loads(raw)
data = packets["source-matrices.json"]
tail = packets["tail-columns.json"]
assert tail["synthetic"] is False and tail["parameters"]["outputBits"] == 640
mat = {
    name: {(int(i), int(j)): (int(lo), int(hi)) for i, j, lo, hi in rows}
    for name, rows in data["matrices"].items()
}
columns = {
    (int(row["column"]), int(row["index"])): (int(row["lo"]), int(row["hi"]))
    for row in tail["entries"]
}
L = mp.mpf(17) / 16
gamma = lambda n: 2*L/(2*n+1)
def midpoint(bounds, bits):
    return mp.mpf(bounds[0]+bounds[1]) / mp.mpf(2)**(bits+1)
def raw_entry(name, i, j):
    return midpoint(mat[name][(min(i,j), max(i,j))], 256)
def tail_entry(column, n):
    return midpoint(columns[(column,n)], 640)
fmt = lambda x: mp.nstr(x, 65)
results = []
for size in (16, 32, 64):
    for parity in (0, 1):
        ids = [2*j+parity for j in range(size)]
        a, k, u = [mp.matrix(size) for _ in range(3)]
        for i, ni in enumerate(ids):
            for j, nj in enumerate(ids):
                norm = mp.sqrt(gamma(ni)*gamma(nj))
                a[i,j] = raw_entry("A",ni,nj)/norm
                k[i,j] = raw_entry("J0",ni,nj)/norm
                u[i,j] = (mp.mpf(648)/17)*(tail_entry(0,ni)*tail_entry(0,nj)
                            +tail_entry(1,ni)*tail_entry(1,nj))/norm
        r = a+k+u
        eigenvalues, vectors = mp.eigsy(r)
        v = vectors[:,0]
        record = {
            "size_per_sector":size, "parity":parity,
            "first_eigenvalues": [fmt(eigenvalues[j]) for j in range(min(5,size))],
            "eigenvector_orthonormal": [fmt(x) for x in v],
            "raw_polynomial_coefficients": [fmt(v[j]/mp.sqrt(gamma(n))) for j,n in enumerate(ids)],
            "orders":ids,
            "minimum_residual_norm":fmt(mp.norm(r*v-eigenvalues[0]*v)),
            "R00":fmt(r[0,0]), "A00":fmt(a[0,0]), "J00":fmt(k[0,0]), "U00":fmt(u[0,0]),
            "R_AplusK_minimum":fmt(mp.eigsy(a+k,eigvals_only=True)[0]),
            "wrong_extra_L_squared_on_J_minimum":fmt(mp.eigsy(a+L**2*k+u,eigvals_only=True)[0]),
            "source_error_norm":fmt(mp.mpf(2)**-204+2*mp.mpf(2)**-220+9*mp.mpf(2)**-512),
        }
        results.append(record)
        print(json.dumps({key:record[key] for key in ("size_per_sector","parity","first_eigenvalues","R00")}),flush=True)
(HERE/"sonin-source-reconstruction.json").write_text(json.dumps({
    "kind":"ordinary-high-precision-exploration", "precision_digits":80,
    "input_hashes":EXPECTED, "results":results,
}, indent=2)+"\n", encoding="utf-8")

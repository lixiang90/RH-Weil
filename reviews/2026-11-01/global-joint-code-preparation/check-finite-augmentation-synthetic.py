"""Isolated AST controls; tiny artificial inputs only, no scientific source IO."""
import ast
from fractions import Fraction as F
import hashlib
import json
import io
from pathlib import Path

HERE = Path(__file__).resolve().parent
CODE = HERE / "verify-finite-augmented.py"
raw = CODE.read_bytes()
tree = ast.parse(raw)
nodes = [node for node in tree.body if isinstance(node, (ast.ImportFrom, ast.Assign, ast.FunctionDef))]
ns = {}
exec(compile(ast.Module(body=nodes, type_ignores=[]), "isolated-augmentation-kernels", "exec"), ns)


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def tr(a):
    return list(map(list, zip(*a)))


def inv(a):
    n = len(a)
    z = [[F(v) for v in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        p = z[k][k]
        assert p != 0
        z[k] = [v / p for v in z[k]]
        for i in range(n):
            if i != k:
                t = z[i][k]
                z[i] = [x - t * y for x, y in zip(z[i], z[k])]
    return [row[n:] for row in z]


def exact_aug(d, g, covariance, c0, blocks):
    m = len(d)
    b = [[F(i == j) + g[i][j] / d[i] for j in range(m)] for i in range(m)]
    w = b + [[b[i][j] - F(i == j) for j in range(m)] for i in range(m)] + b
    cg = [[c0[i][j] + g[i][j] for j in range(m)] for i in range(m)]
    head = mul(tr(b), mul(cg, b))
    gdg = mul(g, [[g[i][j] / d[i] for j in range(m)] for i in range(m)])
    metric = mul(tr(b), [[d[i] * b[i][j] for j in range(m)] for i in range(m)])
    tiles = [[covariance, blocks["FX"], blocks["FY"]],
             [tr(blocks["FX"]), blocks["CX"], blocks["XY"]],
             [tr(blocks["FY"]), tr(blocks["XY"]), blocks["YY"]]]
    k = [[F(tiles[i // m][j // m][i % m][j % m]) for j in range(3*m)] for i in range(3*m)]
    for i in range(3*m):
        k[i][i] += ns["PADDING"] * d[i % m]
    d0 = ns["DFLOOR"]
    h = [[k[i][j] / d0 for j in range(2*m)] for i in range(2*m)]
    for i in range(m):
        h[i][i] += ns["ACTIVE_INVERSE"] * d[i]
        for j in range(m):
            h[m+i][m+j] += g[i][j]
        h[m+i][m+i] += (1 + ns["EPSILON"]) * d[i]
    kw = mul(k, w)
    e = mul(tr(w), kw)
    base = [[head[i][j] - g[i][j] - gdg[i][j] - ns["LAMBDA"]*metric[i][j] - e[i][j]/d0
             for j in range(m)] for i in range(m)]
    r = [[kw[i][j]/d0 for j in range(m)] for i in range(2*m)]
    aug = [[-h[i][j] for j in range(2*m)] + r[i] for i in range(2*m)]
    aug += [tr(r)[i] + base[i] for i in range(m)]
    extra = mul(tr(r), mul(inv(h), r))
    target = [[base[i][j] + extra[i][j] for j in range(m)] for i in range(m)]
    return aug, target


checks = 0
for alo, ahi in [(-3, -1), (-1, 2), (1, 4), (0, 0)]:
    for blo, bhi in [(-4, -2), (2, 5)]:
        a, b = (alo << 1024, ahi << 1024), (blo << 1024, bhi << 1024)
        q = ns["divided"](a, b)
        for x in (F(alo), F(alo+ahi, 2), F(ahi)):
            for y in (F(blo), F(blo+bhi, 2), F(bhi)):
                assert F(q[0], ns["SCALE"]) <= x/y <= F(q[1], ns["SCALE"])
                checks += 1

cases = []
for m in (1, 2):
    d = [F(3, 2), F(2, 3)][:m]
    g = [[F(1, 8) if i == j else F(1, 64) for j in range(m)] for i in range(m)]
    cov = [[F(1, 10) if i == j else F(1, 100) for j in range(m)] for i in range(m)]
    blocks = {name: [[F(1, den) if i == j else F(1, den*10) for j in range(m)] for i in range(m)]
              for name, den in [("CX", 20), ("FX", 100), ("FY", 1000), ("XY", 2000), ("YY", 10000)]}
    for sign in (1, -1):
        c0 = [[sign * 10 * d[i] if i == j else F(1, 128) for j in range(m)] for i in range(m)]
        cases.append((d, g, cov, c0, blocks, "EXACT_SELECTED_TARGET_POSITIVE" if sign > 0 else "SUFFICIENT_TARGET_REJECTED"))
# Y-only countercontrol: adding YY to the positive bottom would change this sign.
cases.append(([F(1)], [[F(0)]], [[F(0)]], [[F(4)]],
              {k: [[F(k == "YY")]] for k in ("CX", "FX", "FY", "XY", "YY")}, "SUFFICIENT_TARGET_REJECTED"))

for d, g, cov, c0, blocks, wanted in cases:
    aug_exact, target = exact_aug(d, g, cov, c0, blocks)
    aug = ns["assemble_sector"](d, g, cov, c0, blocks, lambda: None)
    for i in range(len(aug)):
        for j in range(len(aug)):
            assert F(aug[i][j][0], ns["SCALE"]) <= aug_exact[i][j] <= F(aug[i][j][1], ns["SCALE"])
            checks += 1
    verdict = ns["signed_ldl"](aug, 2*len(d), lambda: None)
    assert verdict["status"] == wanted, (verdict, wanted)
    assert (target[0][0] > 0) == (wanted == "EXACT_SELECTED_TARGET_POSITIVE")
    if len(d) == 2 and wanted == "EXACT_SELECTED_TARGET_POSITIVE":
        assert target[0][0]*target[1][1] - target[0][1]*target[1][0] > 0
    checks += 2

adapter_raw = (HERE / "finite-independent-inputs.py").read_bytes()
adapter_tree = ast.parse(adapter_raw)
adapter_nodes = [n for n in adapter_tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign, ast.FunctionDef))]
adapter = {}
exec(compile(ast.Module(body=adapter_nodes, type_ignores=[]), "isolated-independent-inputs", "exec"), adapter)
adapter["N"] = 4
original = {}
ints = {}
for name, den in [("A", 32), ("B", 8), ("J0", 64)]:
    a = [[F(i+j+1, den) if (i-j) % 2 == 0 else F(0) for j in range(4)] for i in range(4)]
    original[name] = a
    ints[name] = [[int(v*(1 << 257)) for v in row] for row in a]
h = [[F(i+1, 128) if i % 2 == s else F(0) for i in range(4)] for s in range(2)]
hi = [[int(v*(1 << 641)) for v in row] for row in h]
g = [[F(i+j+1, 256) if (i-j) % 2 == 0 else F(0) for j in range(4)] for i in range(4)]
gi = [[int(v*(1 << 257)) for v in row] for row in g]
for parity in (0, 1):
    d, gr, covariance, c0 = adapter["sector_forms"]((ints, hi, gi), parity, poll=lambda: None)
    ids = list(range(parity, 4, 2))
    for i, oi in enumerate(ids):
        for j, oj in enumerate(ids):
            assert gr[i][j] == g[oi][oj]
            assert covariance[i][j] == original["B"][oi][oj] - sum(
                original["A"][oi][ok] * original["A"][ok][oj]/d[k] for k, ok in enumerate(ids))
            assert c0[i][j] == original["A"][oi][oj] + original["J0"][oi][oj] + 36*sum(h[s][oi]*h[s][oj] for s in (0, 1))
            checks += 3
for bad in ("-0", "+1", "01", "", " 0", True, 1):
    try:
        adapter["number"](bad)
    except ValueError:
        checks += 1
    else:
        raise AssertionError("ADAPTER_NONCANONICAL_INTEGER")
for bad in (1 << 16384, -(1 << 16384)):
    try:
        adapter["bounded"](bad)
    except ValueError:
        checks += 1
    else:
        raise AssertionError("ADAPTER_WIDTH_GUARD")

# Resize ONLY the isolated packet count for a tiny memory fixture, never an
# actual file/row or production dimension. Global448 count is separately tested.
class TinyCount(ast.NodeTransformer):
    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(36), node) if node.value == 401856 else node

packet_node = next(n for n in adapter_tree.body if isinstance(n, ast.FunctionDef) and n.name == "load_packet")
packet_node = TinyCount().visit(packet_node)
exec(compile(ast.fix_missing_locations(ast.Module(body=[packet_node], type_ignores=[])), "tiny-memory-packet", "exec"), adapter)
packet = []
for block in ("CX", "FX", "FY", "XY", "YY"):
    for parity in (0, 1):
        for i in range(parity, 4, 2):
            for j in range(i if block in ("CX", "YY") else parity, 4, 2):
                packet.append([block, i, j, str(i*11+j-16)])
memory = ("\n".join(json.dumps(row, separators=(",", ":")) for row in packet)+"\n").encode()
class MemoryPath:
    def __init__(self, value):
        assert value == "ARTIFICIAL_MEMORY_ONLY"
    def open(self, mode):
        assert mode == "rb"
        return io.BytesIO(memory)
adapter["Path"] = MemoryPath
got = adapter["load_packet"]("ARTIFICIAL_MEMORY_ONLY", dict(sha256=hashlib.sha256(memory).hexdigest(), bytes=len(memory)), poll=lambda: None)
for block, i, j, value in packet:
    assert got[i % 2][block][i//2][j//2] == F(int(value), 1 << 256)
    if block in ("CX", "YY"):
        assert got[i % 2][block][j//2][i//2] == F(int(value), 1 << 256)
    checks += 1

result = dict(status="ISOLATED_AUGMENTED_FINITE_SYNTHETIC_PASS", controls=checks,
              codeSHA256=hashlib.sha256(raw).hexdigest(), maximumSyntheticHeadDimension=2,
              independentInputCodeSHA256=hashlib.sha256(adapter_raw).hexdigest(),
              syntheticOriginalDimension=4, mockedPacketBytesOnly=True,
              actualSourceRead=False, actualPacketRead=False, actualGramSolve=False,
              scientificModuleImported=False, YPositiveBottomCountercontrol=True,
              independentExactFractionReference=True, codePreparationOnly=True)
print(json.dumps(result, sort_keys=True))

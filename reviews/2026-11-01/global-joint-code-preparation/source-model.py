"""Directed MODEL kernels for the fixed five-block global source.

CODE PREPARATION. There is deliberately no command-line execution path. The
future controller must first authenticate the C069 contract, exact code/reviews,
root gate/freeze, one-attempt owner and complete source+verification budget.
Only then may it call produce(). Importing this file performs no file reads or
model computation. The sink is the ONE canonical packet, never a second copy.

All arrays in memory represent raw forms <p_i, Op p_j>, unless explicitly
named expansion coefficients. Projection Q deletes degrees <448 exactly.
Fstar=Q Mc E, Xstar=Q Vhat, Ystar=Q Kstar E. The old finite V/h boxes are NOT
asserted true: their exact midpoint functions, plus X's EXACT infinite tail,
define the model. Actual-source fees belong to the separately reviewed consumer.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import re


N, DEGREE, COEFFICIENT_BITS, CONTRACTION_BITS, RAW_BITS = 448, 2046, 8192, 1024, 256
TARGET = "RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1"
BLOCKS = ("CX", "FX", "FY", "XY", "YY")
INPUTS = {
    "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/source-matrices.json":
        "a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2",
    "literature/local/2026-10-29-weil-9-8/pilot/run-01/certificates/moments.json":
        "2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9",
    "literature/local/2026-10-31-retained-tail-source/run-01/h-columns.jsonl":
        "37f2c0410beb1b1c43b9f8d2df24d72fce3170b5f359d089c198742f1eee4e74",
    "literature/local/2026-10-31-retained-tail-source/run-01/finite-columns.jsonl":
        "d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080",
}


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def ceil_div(a, b):
    need(type(a) is int and type(b) is int and b > 0, "DIVISION_DOMAIN")
    return -((-a) // b)


def integer(text, bits=32768):
    need(type(text) is str and len(text) <= 10000
         and re.fullmatch(r"0|-[1-9][0-9]*|[1-9][0-9]*", text), "INTEGER_CANONICAL")
    x = int(text)
    need(abs(x).bit_length() <= bits, "INTEGER_WIDTH")
    return x


def product_bounds(a, b):
    """Exact rectangle extrema; two products whenever one interval has a sign."""
    x, y = a
    u, v = b
    if x >= 0:
        if u >= 0:
            return x*u, y*v
        if v <= 0:
            return y*u, x*v
        return y*u, y*v
    if y <= 0:
        if u >= 0:
            return x*v, y*u
        if v <= 0:
            return y*v, x*u
        return x*v, x*u
    if u >= 0:
        return x*v, y*v
    if v <= 0:
        return y*u, x*u
    return min(x*v, y*u), max(x*u, y*v)


class Mesh:
    """Closed integer endpoint interval divided by 2**bits; outward every step."""
    def __init__(self, bits):
        need(type(bits) is int and 16 <= bits <= COEFFICIENT_BITS, "MESH_BITS")
        self.bits, self.unit, self.zero = bits, 1 << bits, (0, 0)

    def check(self, a):
        need(type(a) is tuple and len(a) == 2 and a[0] <= a[1], "INTERVAL_ORDER")
        need(max(abs(x).bit_length() for x in a) <= 32768, "INTERVAL_WIDTH_GUARD")
        return a

    def rat(self, n, d=1):
        if isinstance(n, Fraction):
            n, d = n.numerator, n.denominator*d
        need(type(n) is int and type(d) is int and d > 0, "RATIONAL_DOMAIN")
        need(max(abs(n).bit_length(), d.bit_length()) <= 32768, "RATIONAL_WIDTH_GUARD")
        return self.check((n*self.unit//d, ceil_div(n*self.unit, d)))

    def add(self, a, b):
        return self.check((a[0]+b[0], a[1]+b[1]))

    def sub(self, a, b):
        return self.check((a[0]-b[1], a[1]-b[0]))

    def scale(self, a, n, d=1):
        need(type(n) is int and type(d) is int and d > 0, "SCALE_DOMAIN")
        lo, hi = (a[0]*n, a[1]*n) if n >= 0 else (a[1]*n, a[0]*n)
        return self.check((lo//d, ceil_div(hi, d)))

    def mul(self, a, b):
        lo, hi = product_bounds(a, b)
        return self.check((lo//self.unit, ceil_div(hi, self.unit)))

    def power(self, a, n):
        need(type(n) is int and n >= 0, "POWER_DOMAIN")
        out = (self.unit, self.unit)
        for _ in range(n):
            out = self.mul(out, a)
        return out

    def convert(self, a, other_bits):
        need(16 <= other_bits <= self.bits, "MESH_CONVERSION")
        shift = 1 << (self.bits-other_bits)
        return a[0]//shift, ceil_div(a[1], shift)

    def log_series(self, n, d, tick):
        """True 2atanh(n/d), n/d in [0,1/3], with positive tail."""
        need(0 <= 3*n <= d, "LOG_SERIES_DOMAIN")
        if n == 0:
            return self.zero
        count = (self.bits+11)//3
        ratio = self.rat(n, d)
        squared, power, total = self.mul(ratio, ratio), ratio, self.zero
        for k in range(count):
            total = self.add(total, self.scale(power, 2, 2*k+1))
            power = self.mul(power, squared)
            if k % 64 == 0:
                tick()
        # Tail <= 3**(-2count) < 2**(-3count). Rounding is inside intervals.
        return self.check((total[0], total[1]+ceil_div(self.unit, 1 << (3*count))))

    def log(self, q, log2, tick):
        q = Fraction(q)
        need(q > 0, "LOG_ARGUMENT")
        n, d = q.numerator, q.denominator
        k = n.bit_length()-d.bit_length()
        a, b = (n, d << k) if k >= 0 else (n << (-k), d)
        if a < b:
            a *= 2
            k -= 1
        elif a >= 2*b:
            b *= 2
            k += 1
        need(b <= a < 2*b, "LOG_RANGE_REDUCTION")
        return self.add(self.scale(log2, k), self.log_series(a-b, a+b, tick))


def dot(mesh, a, b, tick):
    need(len(a) == len(b), "DOT_SHAPE")
    lo = hi = 0
    # Round the ENTIRE dot once, not one multiplication at a time.
    for k, (x, y) in enumerate(zip(a, b)):
        lower, upper = product_bounds(x, y)
        lo += lower
        hi += upper
        if k % 128 == 0:
            tick()
    return mesh.check((lo//mesh.unit, ceil_div(hi, mesh.unit)))


def rational_polynomials(mesh, count, shift, tick):
    """Yield P_r(z-shift) coefficients as intervals; exact rational shift."""
    one, t = mesh.rat(1), mesh.rat(shift)
    p0 = [one]
    yield p0
    if count == 1:
        return
    p1 = [mesh.scale(t, -1), one]
    yield p1
    for r in range(1, count-1):
        out = [mesh.zero]*(r+2)
        for k, v in enumerate(p1):
            out[k+1] = mesh.add(out[k+1], mesh.scale(v, 2*r+1, r+1))
            out[k] = mesh.sub(out[k], mesh.scale(mesh.mul(t, v), 2*r+1, r+1))
        for k, v in enumerate(p0):
            out[k] = mesh.sub(out[k], mesh.scale(v, r, r+1))
        p0, p1 = p1, out
        tick()
        yield out


def legendre_at(mesh, x, count):
    values = [mesh.rat(1)]
    if count == 1:
        return values
    xx = mesh.rat(x)
    values.append(xx)
    for k in range(2, count):
        values.append(mesh.sub(mesh.scale(mesh.mul(xx, values[-1]), 2*k-1, k),
                               mesh.scale(values[-2], k-1, k)))
    return values


def ell_monomials(mesh, t, degree, tick):
    """Integrals_beta^1 z**k ell(z) dz, ell=log2-log(1-z²)/2.

    x**(m+1)*log(x)->0 at x=0 is inserted EXACTLY, no endpoint sampling.
    The other endpoints are positive rational t, 2-t and 2.
    """
    t = Fraction(t)
    need(0 < t < 2, "SHIFT_INTERVAL")
    beta = t-1
    log2 = mesh.log_series(1, 3, tick)
    args = (2-t, t, Fraction(2))
    logs = [mesh.log(q, log2, tick) if q != 2 else log2 for q in args]
    primitives = []
    for q, logq in zip(args, logs):
        power, qq, column = mesh.rat(q), mesh.rat(q), []
        for m in range(degree+1):
            inner = mesh.sub(mesh.scale(logq, 1, m+1), mesh.rat(1, (m+1)**2))
            column.append(mesh.mul(power, inner))
            power = mesh.mul(power, qq)
        primitives.append(column)
    beta_power, beta_iv = mesh.rat(1), mesh.rat(beta)
    out = []
    for k in range(degree+1):
        tick()
        beta_power = mesh.mul(beta_power, beta_iv)
        plain = mesh.scale(mesh.sub(mesh.rat(1), beta_power), 1, k+1)
        minus = plus = mesh.zero
        for m in range(k+1):
            binomial = math.comb(k, m)
            minus = mesh.add(minus, mesh.scale(primitives[0][m], (-1)**m*binomial))
            plus = mesh.add(plus, mesh.scale(mesh.sub(primitives[2][m], primitives[1][m]),
                                           (-1)**(k-m)*binomial))
        out.append(mesh.sub(mesh.mul(log2, plain), mesh.scale(mesh.add(minus, plus), 1, 2)))
    return out


def shift_rows(mesh, t, n, degree, tick):
    """Yield J_rk and B_rj for r<n, k<=degree, j<n.

    J=integral P_r(z-t) P_k(z); B=integral P_r(z-t)P_j(z)ell(z).
    Recurrences keep shrinking boundary surplus; no symmetry is imposed on B.
    C_rj=integral P_r(z-t) z P_j'(z). B's j=0 column is integrated directly.
    """
    top, btop = degree+n-1, 2*n-2
    beta = t-1
    values = legendre_at(mesh, beta, top+2)
    first = [mesh.rat(2-t)]
    first.extend(mesh.scale(mesh.sub(values[k-1], values[k+1]), 1, 2*k+1)
                 for k in range(1, top+1))
    moments = ell_monomials(mesh, t, btop, tick)
    bfirst = [dot(mesh, row, moments[:len(row)], tick)
              for row in rational_polynomials(mesh, btop+1, Fraction(0), tick)]
    bcolumn = [dot(mesh, row, moments[:len(row)], tick)
               for row in rational_polynomials(mesh, n, t, tick)]
    prev_j2 = prev_j1 = prev_b2 = prev_b1 = prev_c2 = prev_c1 = None
    tiv = mesh.rat(t)
    for r in range(n):
        tick()
        width, bwidth = top-r, btop-r
        if r == 0:
            jr = first[:]
            br = bfirst[:]
        elif r == 1:
            jr = [mesh.sub(first[1], mesh.mul(tiv, first[0]))]
            jr.extend(mesh.sub(mesh.add(mesh.scale(first[k+1], k+1, 2*k+1),
                                        mesh.scale(first[k-1], k, 2*k+1)),
                               mesh.mul(tiv, first[k])) for k in range(1, width+1))
            br = [bcolumn[1]]
            br.extend(mesh.sub(mesh.add(mesh.scale(bfirst[k+1], k+1, 2*k+1),
                                        mesh.scale(bfirst[k-1], k, 2*k+1)),
                               mesh.mul(tiv, bfirst[k])) for k in range(1, bwidth+1))
        else:
            jr = [mesh.scale(first[r], (-1)**r)]
            jr.extend(mesh.sub(prev_j2[k], mesh.scale(mesh.sub(prev_j1[k+1], prev_j1[k-1]),
                                                     2*r-1, 2*k+1))
                      for k in range(1, width+1))
            br = None
        cr = [mesh.zero]
        if bwidth >= 1:
            cr.append(jr[1])
        for k in range(2, bwidth+1):
            cr.append(mesh.add(cr[k-2], mesh.add(mesh.scale(jr[k], k),
                                                mesh.scale(jr[k-2], k-1))))
        if r >= 2:
            br = [bcolumn[r]]
            for k in range(1, bwidth+1):
                recurrence = mesh.sub(prev_b2[k], mesh.scale(
                    mesh.sub(prev_b1[k+1], prev_b1[k-1]), 2*r-1, 2*k+1))
                br.append(mesh.add(recurrence, mesh.scale(mesh.sub(cr[k], prev_c2[k]),
                                                         1, k*(k+1))))
        yield r, jr[:degree+1], br[:n]
        prev_j2, prev_j1 = prev_j1, jr
        prev_b2, prev_b1 = prev_b1, br
        prev_c2, prev_c1 = prev_c1, cr


def kernel_seeds(mesh, coefficients, top, tick):
    boundary = [mesh.zero]*(top+2)
    for m, coefficient in enumerate(coefficients):
        if coefficient == 0:
            continue
        tick()
        a, weight = mesh.rat(coefficient), mesh.rat(1, m+1)
        for j in range(min(m, top+1)+1):
            boundary[j] = mesh.add(boundary[j], mesh.mul(a, weight))
            if j < min(m, top+1):
                weight = mesh.scale(weight, m-j, m+j+2)
    boundary = [mesh.scale(v, 2*(-1)**j) for j, v in enumerate(boundary)]
    first, second = [mesh.zero]*(top+1), [mesh.zero]*top
    first[0] = mesh.scale(mesh.add(boundary[0], boundary[1]), 2)
    for j in range(2, top+1, 2):
        first[j] = mesh.scale(mesh.sub(boundary[j+1], boundary[j-1]), 2, 2*j+1)
    for j in range(1, top, 2):
        second[j] = mesh.scale(mesh.add(mesh.sub(first[j-1], first[j+1]),
                                      mesh.scale(mesh.sub(boundary[j+1], boundary[j-1]), 2)),
                               1, 2*j+1)
    return first, second


def polynomial_y(mesh, contract_mesh, moments, h, tick):
    """Full signed pole+band Kstar, plus raw36 FULL-h rank two; Q projection."""
    coefficients = [Fraction(0)]*(DEGREE+1)
    for q, theta in enumerate(moments):
        m = 2*q
        coefficients[m] = (2*Fraction(9, 8)**m+(-1)**q*theta*576**m)/math.factorial(m)
    top = DEGREE+N-1
    first, second = kernel_seeds(mesh, coefficients, top, tick)
    columns = []
    previous2 = previous1 = None
    for r in range(N):
        tick()
        if r == 0:
            current = {j:first[j] if j <= DEGREE else mesh.zero for j in range(0, top+1, 2)}
        elif r == 1:
            current = {j:second[j] if j <= DEGREE else mesh.zero for j in range(1, top, 2)}
        else:
            current = {}
            for j in range(r, top-r+1, 2):
                current[j] = (mesh.zero if j > DEGREE else mesh.sub(previous2[j], mesh.scale(
                    mesh.sub(previous1[j+1], previous1[j-1]), 2*r-1, 2*j+1)))
        s = r % 2
        column = []
        for i in range(N+s, DEGREE+1, 2):
            value = mesh.add(mesh.scale(current[i], 81, 64),
                             mesh.rat(36*h[s][i]*h[s][r], 1 << 1282))
            column.append(mesh.convert(value, contract_mesh.bits))
        columns.append(column)
        previous2, previous1 = previous1, current
    return columns


def true_pi(mesh, tick):
    # Exact Machin identity; alternating truncation is bracketed, not treated exact.
    def atan(d):
        power, square, out = mesh.rat(1, d), mesh.rat(1, d*d), mesh.zero
        count = (mesh.bits+3)//4+2
        for k in range(count):
            out = mesh.add(out, mesh.scale(power, (-1)**k, 2*k+1))
            power = mesh.mul(power, square)
            if k % 64 == 0:
                tick()
        # d>=5 implies d**(-2count-1)<2**(-4count-2).
        radius = ceil_div(mesh.unit, 1 << (4*count+2))
        return mesh.check((out[0]-radius, out[1]+radius))
    return mesh.sub(mesh.scale(atan(5), 16), mesh.scale(atan(239), 4))


class Tail:
    """Exact infinite endpoint-log tail Gram through rational sums and true pi²."""
    def __init__(self, mesh, degree, tick):
        self.mesh, self.degree = mesh, degree
        limit = degree+N+2
        self.h, self.odd, self.h2, self.odd2 = [[mesh.zero] for _ in range(4)]
        for k in range(1, limit+1):
            self.h.append(mesh.add(self.h[-1], mesh.rat(1, k)))
            self.odd.append(mesh.add(self.odd[-1], mesh.rat(1, 2*k-1)))
            self.h2.append(mesh.add(self.h2[-1], mesh.rat(1, k*k)))
            self.odd2.append(mesh.add(self.odd2[-1], mesh.rat(1, (2*k-1)**2)))
            if k % 128 == 0:
                tick()
        pi = true_pi(mesh, tick)
        self.pi2 = mesh.mul(pi, pi)

    def raw(self, j, k):
        mesh = self.mesh
        need(j % 2 == k % 2, "TAIL_PARITY")
        if j > k:
            j, k = k, j
        i0 = self.degree+1
        if i0 % 2 != j % 2:
            i0 += 1
        if j == k:
            start = (i0-j)//2
            native = mesh.sub(mesh.sub(self.odd2[start+j], mesh.scale(self.h2[start-1], 1, 4)),
                              mesh.scale(self.pi2, 1, 12))
            need(native[0] >= 0, "TAIL_DIAGONAL_NONNEGATIVE")
            return mesh.scale(native, 9, 4*(2*j+1))
        positive = mesh.sub(self.odd[(i0+k)//2], self.odd[(i0+j)//2])
        negative = mesh.scale(mesh.sub(self.h[(i0-j)//2-1], self.h[(i0-k)//2-1]), 1, 2)
        return mesh.scale(mesh.sub(positive, negative), -9,
                          4*(k*(k+1)-j*(j+1)))


def weighted_gram(mesh, a, b, parity, tick):
    need(len(a) == len(b), "GRAM_COLUMN_SHAPE")
    weighted = [mesh.scale(y, 4*(2*i+1), 9)
                for y, i in zip(b, range(N+parity, DEGREE+1, 2))]
    return dot(mesh, a, weighted, tick)


def log_raw(j, k, harmonic):
    """Raw <p_k,p_j ell>, rational; no floating log2 survives."""
    need(j % 2 == k % 2, "LOG_RAW_PARITY")
    if j != k:
        return Fraction(9, 4*abs(j-k)*(j+k+1))
    d = Fraction(9, 4*(2*j+1))
    return d*(Fraction(1, 2*j+1)+2*(harmonic[2*j]-harmonic[j]))


def shift_sums(mesh, contract_mesh, centers, tick):
    """Sum7 paired shifts FIRST, then one contraction per model product."""
    jrows = [[contract_mesh.zero]*((DEGREE-i % 2)//2+1) for i in range(N)]
    brows = [[contract_mesh.zero]*(N//2) for _ in range(N)]
    positives = [row for row in centers if row["key"].startswith("+")]
    for record in positives:
        a, w = integer(record["a"], 2052), integer(record["w"], 2052)
        t = Fraction(8*a, 9*(1 << 2048))
        for r, jr, br in shift_rows(mesh, t, N, DEGREE, tick):
            tick()
            for pos, k in enumerate(range(r % 2, DEGREE+1, 2)):
                value = mesh.convert(mesh.scale(jr[k], 9*w, 4*(1 << 2048)), contract_mesh.bits)
                jrows[r][pos] = contract_mesh.add(jrows[r][pos], value)
            for pos, k in enumerate(range(r % 2, N, 2)):
                value = mesh.convert(mesh.scale(br[k], 9*w, 4*(1 << 2048)), contract_mesh.bits)
                brows[r][pos] = contract_mesh.add(brows[r][pos], value)
    return jrows, brows


def verify_pin(path, digest, tick):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
            tick()
    need(h.hexdigest() == digest, "INPUT_HASH:"+path.name)


def load_inputs(root, tick):
    # This is called ONLY after the future root controller's authenticated gate.
    for relative, digest in INPUTS.items():
        verify_pin(root/relative, digest, tick)
    matrix_path, moment_path, h_path, v_path = [root/p for p in INPUTS]
    matrix_key, moment_key, h_key, v_key = list(INPUTS)
    raw = matrix_path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == INPUTS[matrix_key], "MATRIX_CONSUMED_HASH")
    source = json.loads(raw)["packet"]
    p = source["parameters"]
    need(p["N"] == N and p["L"] == "9/8" and p["omega"] == 256 and p["outputBits"] == 256,
         "OLD_SOURCE_PARAMETERS")
    centers = source["primeCenters"]
    need(len(centers) == 15 and [x["key"] for x in centers] ==
         ["0"]+[sign+str(n) for n in (2, 3, 4, 5, 7, 8, 9) for sign in ("+", "-")],
         "PRIME_CENTER_CENSUS")
    need(centers[0] == {"key":"0", "a":"0", "w":str(7*(1 << 2048)//2)}, "IDENTITY_CENTER")
    for positive, negative in zip(centers[1::2], centers[2::2]):
        a, w = integer(positive["a"], 2052), integer(positive["w"], 2052)
        need(0 < a < 9*(1 << 2048)//4 and w < 0
             and integer(negative["a"], 2052) == -a and negative["w"] == positive["w"],
             "PAIRED_PRIME_CENTERS")
    need(sum(abs(integer(x["w"], 2052)) for x in centers) < 11*(1 << 2048), "CENTER_MASS")
    raw = moment_path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == INPUTS[moment_key], "MOMENT_CONSUMED_HASH")
    data = json.loads(raw)
    q = data["parameters"]
    need(data["schema"] == "RH_WEIL_9_8_SOURCE_MOMENTS_V1" and q["L"] == "9/8"
         and q["omega"] == 256 and q["beta"] == "7/2" and q["outputBits"] == 1152
         and q["qMax"] == 1023 and data["binetRemainderIncludedOnce"] is True, "MOMENT_SCHEMA")
    need(len(data["rows"]) == 1024, "MOMENT_COUNT")
    moments = []
    for q, row in enumerate(data["rows"]):
        need(type(row["q"]) is int and row["q"] == q, "MOMENT_ORDER")
        lo, hi = integer(row["lo"]), integer(row["hi"])
        need(lo <= hi and hi-lo <= (1 << 55), "MOMENT_INTERVAL")
        moments.append(Fraction(lo+hi, 1 << 1153))
    h, count = [[0]*(DEGREE+1) for _ in range(2)], 0
    consumed = hashlib.sha256()
    with h_path.open("rb") as handle:
        for s in range(2):
            for i in range(s, DEGREE+1, 2):
                raw = handle.readline(65537)
                need(0 < len(raw) <= 65536 and raw.endswith(b"\n"), "H_LINE_BYTES")
                consumed.update(raw)
                row = json.loads(raw)
                need(len(row) == 4 and type(row[0]) is int and type(row[1]) is int
                     and row[:2] == [s, i], "H_ROW_ORDER")
                lo, hi = integer(row[2], 660), integer(row[3], 660)
                need(lo <= hi, "H_BOX_ORDER")
                h[s][i] = lo+hi
                count += 1
            tick()
        need(handle.read(1) == b"" and count == DEGREE+1, "H_COMPLETE_SHAPE")
    need(consumed.hexdigest() == INPUTS[h_key], "H_CONSUMED_HASH")
    x, count = [], 0
    mesh = Mesh(CONTRACTION_BITS)
    consumed = hashlib.sha256()
    with v_path.open("rb") as handle:
        for j in range(N):
            column = []
            for i in range(j % 2, DEGREE+1, 2):
                raw = handle.readline(65537)
                need(0 < len(raw) <= 65536 and raw.endswith(b"\n"), "V_LINE_BYTES")
                consumed.update(raw)
                row = json.loads(raw)
                need(len(row) == 4 and type(row[0]) is int and type(row[1]) is int
                     and row[:2] == [j, i], "V_ROW_ORDER")
                lo, hi = integer(row[2], 280), integer(row[3], 280)
                need(lo <= hi, "V_BOX_ORDER")
                if i >= N:
                    column.append(mesh.rat(lo+hi, 1 << 257))
                count += 1
            x.append(column)
            tick()
        need(handle.read(1) == b"" and count == 458528, "V_COMPLETE_SHAPE")
    need(consumed.hexdigest() == INPUTS[v_key], "V_CONSUMED_HASH")
    return centers, moments, h, x


def produce(root, emit, tick, admission):
    """Controller-only future API. emit receives ONE canonical packet record.

    Admission must already be authenticated by the future controller, which
    owns exclusive once-lock, source/verifier3600s/48MiB and external watchdog.
    This kernel additionally refuses an untyped or unauthenticated invocation.
    No C069/execution is admitted merely by this function's existence.
    """
    need(admission.get("status") == "ROOT_EXPLICIT_C069_SOURCE_EXECUTION_APPROVED"
         and admission.get("runtimeGoalCreatedAt") == 1793085111
         and admission.get("targetId") == TARGET and admission.get("contractId") == "C069"
         and admission.get("producerSHA256") == hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
         and admission.get("controllerAuthenticatedGateAndFreeze") is True
         and admission.get("exclusiveOnceOwnerCreated") is True, "ROOT_EXECUTION_GATE_REQUIRED")
    root = Path(root).resolve()
    need(callable(emit) and callable(tick), "CONTROLLER_INTERFACE")
    tick()
    centers, moments, h, x = load_inputs(root, tick)
    working, mesh = Mesh(COEFFICIENT_BITS), Mesh(CONTRACTION_BITS)
    y = polynomial_y(working, mesh, moments, h, tick)
    tail = Tail(working, DEGREE, tick)
    shifts, blogs = shift_sums(working, mesh, centers, tick)
    harmonic = [Fraction(0)]
    for k in range(1, 2*N):
        harmonic.append(harmonic[-1]+Fraction(1, k))
    pi_columns = []
    y_expansion = []
    for j in range(N):
        tick()
        coeffs, ycoeff = [], []
        offset = 0
        for k in range(j % 2, DEGREE+1, 2):
            raw = mesh.zero if k < N else x[j][offset]
            if k >= N:
                offset += 1
            coeffs.append(mesh.scale(mesh.sub(raw, mesh.rat(log_raw(j, k, harmonic))),
                                     4*(2*k+1), 9))
        ycoeff = [mesh.scale(v, 4*(2*k+1), 9)
                  for v, k in zip(y[j], range(N+j % 2, DEGREE+1, 2))]
        pi_columns.append(coeffs)
        y_expansion.append(ycoeff)
    certificates, total_rows = [], 0
    center_step = 1 << (CONTRACTION_BITS-RAW_BITS)
    for block in BLOCKS:
        weighted_distance, rows = 0, 0
        for parity in (0, 1):
            for i in range(parity, N, 2):
                tick()
                for j in range(i if block in ("CX", "YY") else parity, N, 2):
                    if block == "CX":
                        interval = mesh.add(weighted_gram(mesh, x[i], x[j], parity, tick),
                                            working.convert(tail.raw(i, j), mesh.bits))
                    elif block == "FX":
                        interval = mesh.add(blogs[i][j//2], dot(mesh, shifts[i], pi_columns[j], tick))
                    elif block == "FY":
                        interval = dot(mesh, shifts[i][N//2:], y_expansion[j], tick)
                    elif block == "XY":
                        interval = dot(mesh, x[i], y_expansion[j], tick)
                    else:
                        interval = dot(mesh, y[i], y_expansion[j], tick)
                    center = (interval[0]+interval[1]+center_step)//(2*center_step)
                    need(abs(center).bit_length() <= 262, "FINAL_CENTER_INTEGER_WIDTH")
                    distance = max(abs(center*center_step-interval[0]),
                                   abs(interval[1]-center*center_step))
                    multiplicity = 2 if block in ("CX", "YY") and i != j else 1
                    weighted_distance += multiplicity*distance*distance*(2*i+1)*(2*j+1)
                    need(16*weighted_distance <= 81*(1 << (2*CONTRACTION_BITS-460)),
                         "FINAL_FULL_NATIVE_ARITHMETIC_230")
                    record = [block, i, j, str(center)]
                    raw = (json.dumps(record, separators=(",", ":"))+"\n").encode("ascii")
                    need(len(raw) < 100, "CANONICAL_PACKET_RECORD_SIZE")
                    emit(record)
                    rows += 1
        expected = 50400 if block in ("CX", "YY") else 100352
        need(rows == expected, "BLOCK_CENSUS")
        certificates.append({"block":block, "rows":rows,
                             "finalWeightedDistanceNumerator":str(weighted_distance),
                             "distanceDenominatorPower":CONTRACTION_BITS,
                             "fullNativeArithmeticPower":-230,
                             "hermitianTriangleMultiplicityPaid":block in ("CX", "YY")})
        total_rows += rows
    need(total_rows == 401856, "TOTAL_CENSUS")
    tick()
    return {"status":"MODEL_FIVE_BLOCKS_CENTER_CERTIFIED_PENDING_ROOT", "targetId":TARGET,
            "blocks":list(BLOCKS), "blockCertificates":certificates, "rows":total_rows, "rawBits":RAW_BITS,
            "coefficientBits":COEFFICIENT_BITS, "contractionBits":CONTRACTION_BITS,
            "fullNativeArithmeticPower":-230, "inputPins":INPUTS,
            "actualSourceFeesIncluded":False, "globalSignClaim":False,
            "independentVerifierAndRootAcceptanceRequired":True}


if __name__ == "__main__":
    raise SystemExit("CODE_PREPARATION_ONLY: no standalone run; future authenticated root controller required")

"""Independent reference checker for the selected five-block model packet.

CODE PREPARATION ONLY. No top-level source reads, source evaluation or run path.
The future root controller must authenticate code/source/model pins, own the one
attempt, and supply mandatory time/output guard ``poll``. This module writes no
files and never imports the producer or any historical scientific driver.

It recomputes mathematical intervals from the four original model inputs and
compares them with FINAL packet centers. Hash/order/shape checks alone are never
a source certificate. All intervals denote closed dyadic intervals; all kernel,
log, tail and contraction rounding remains inside the per-block native HS test.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re


N, D, HIGH, LOW, CENTER = 448, 2046, 8192, 1024, 256
L = Fraction(9, 8)
BLOCKS = ("CX", "FX", "FY", "XY", "YY")
ZERO = (0, 0)
MAX_ENDPOINT_BITS = 65536
DECIMAL = re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)\Z")


def require(test, message):
    if not test:
        raise ValueError(message)


def ceildiv(n, d):
    require(d > 0, "positive divisor")
    return -((-n) // d)


def integer(text, bits):
    require(type(text) is str and len(text) <= (bits * 30103 // 100000 + 3),
            "bounded decimal string")
    require(DECIMAL.fullmatch(text) is not None, "canonical decimal integer")
    value = int(text)
    require(value.bit_length() <= bits, "integer width")
    return value


class Dyadic:
    """Separately authored directed interval implementation, unit 2**bits."""

    def __init__(self, bits):
        require(bits in (HIGH, LOW), "fixed interval precision")
        self.bits = bits
        self.unit = 1 << bits

    def checked(self, lo, hi):
        require(type(lo) is int and type(hi) is int and lo <= hi,
                "ordered integer endpoints")
        require(max(lo.bit_length(), hi.bit_length()) <= MAX_ENDPOINT_BITS,
                "bounded interval endpoints")
        return lo, hi

    def rational(self, n, d=1):
        if isinstance(n, Fraction):
            n, d = n.numerator, n.denominator * d
        require(type(n) is int and type(d) is int and d > 0,
                "rational interval input")
        return self.checked((n << self.bits) // d,
                            ceildiv(n << self.bits, d))

    def add(self, a, b):
        return self.checked(a[0] + b[0], a[1] + b[1])

    def subtract(self, a, b):
        return self.checked(a[0] - b[1], a[1] - b[0])

    def scale(self, a, n, d=1):
        if isinstance(n, Fraction):
            n, d = n.numerator, n.denominator * d
        require(type(n) is int and type(d) is int and d > 0,
                "rational scale input")
        x, y = n * a[0], n * a[1]
        return self.checked(min(x, y) // d, ceildiv(max(x, y), d))

    def multiply(self, a, b):
        if a == ZERO or b == ZERO:
            return ZERO
        # The point-interval branch is exact until its directed final division.
        if a[0] == a[1]:
            return self.scale(b, a[0], self.unit)
        if b[0] == b[1]:
            return self.scale(a, b[0], self.unit)
        products = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
        return self.checked(min(products) // self.unit,
                            ceildiv(max(products), self.unit))

    def lower_precision(self, a):
        require(self.bits == HIGH, "only8192-to1024 downscale")
        step = 1 << (HIGH - LOW)
        return a[0] // step, ceildiv(a[1], step)


def _atanh_log(mesh, n, d, poll):
    """2 atanh(n/d), n/d in [0,1/3], with an explicit geometric tail."""
    require(0 <= 3 * n <= d and d > 0, "atanh range reduction")
    power, answer = mesh.rational(n, d), ZERO
    count = 3000
    for k in range(count):
        answer = mesh.add(answer, mesh.scale(power, 2, 2 * k + 1))
        power = mesh.scale(power, n * n, d * d)
        if k % 64 == 0:
            poll()
    # Remaining sum <= 2*z^(2K+1)/((2K+1)*(1-z^2)).
    tail = mesh.scale(power, 2 * d * d,
                      (2 * count + 1) * (d * d - n * n))
    return mesh.checked(answer[0], answer[1] + tail[1])


def logarithm(mesh, q, log2, poll):
    q = Fraction(q)
    require(q > 0, "logarithm positive argument")
    n, d = q.numerator, q.denominator
    k = n.bit_length() - d.bit_length()
    if k >= 0:
        d <<= k
    else:
        n <<= -k
    if n < d:
        n *= 2
        k -= 1
    if n >= 2 * d:
        d *= 2
        k += 1
    require(d <= n < 2 * d, "logarithm range reduction exact")
    return mesh.add(mesh.scale(log2, k), _atanh_log(mesh, n - d, n + d, poll))


def pi_interval(mesh, poll):
    """Independent alternating Machin enclosure, not an imported saved pi box."""
    def arctangent(d):
        total, power = ZERO, d
        for k in range(3000):
            term = mesh.rational(1 if k % 2 == 0 else -1,
                                 (2 * k + 1) * power)
            total = mesh.add(total, term)
            power *= d * d
            if k % 64 == 0:
                poll()
        # K is even, so the omitted alternating remainder is positive.
        next_term = mesh.rational(1, 6001 * power)
        return mesh.checked(total[0], total[1] + next_term[1])
    return mesh.subtract(mesh.scale(arctangent(5), 16),
                         mesh.scale(arctangent(239), 4))


def gram_d_inverse(i):
    return Fraction(4 * (2 * i + 1), 9)


def harmonic_table(last, squared=False):
    ans = [Fraction(0)]
    for k in range(1, last + 1):
        ans.append(ans[-1] + Fraction(1, k * k if squared else k))
    return ans


def _log_weight_raw(i, j, harmonic):
    """<p_i,p_j*ell>, ell=log2-.5*log(1-z*z), in physical du."""
    if (i - j) % 2:
        return Fraction(0)
    if i != j:
        return Fraction(9, 4 * abs(i - j) * (i + j + 1))
    return Fraction(9, 4 * (2 * j + 1)) * (
        Fraction(1, 2 * j + 1) + 2 * (harmonic[2 * j] - harmonic[j]))


def _progression_difference(a, b):
    """Sum_m>=0 (1/(a+2m)-1/(b+2m)), using exact telescoping."""
    require(a > 0 and b > 0 and (a - b) % 2 == 0,
            "positive matched parity progression")
    if a > b:
        return -sum((Fraction(1, n) for n in range(b, a, 2)), Fraction(0))
    return sum((Fraction(1, n) for n in range(a, b, 2)), Fraction(0))


def tail_gram_raw(i, j, mesh, pi2, square_harmonic, odd_square_harmonic):
    require((i - j) % 2 == 0 and 0 <= i <= j < N, "tail input indices")
    first = D + 1 if (D + 1 - i) % 2 == 0 else D + 2
    if i == j:
        k = (first - i) // 2
        exact = odd_square_harmonic[k + i] - square_harmonic[k - 1] / 4
        native = mesh.subtract(mesh.rational(exact), mesh.scale(pi2, 1, 12))
        require(native[0] >= 0, "independent diagonal-tail nonnegativity")
        return mesh.scale(native, Fraction(9, 4 * (2 * i + 1)))
    finite = _progression_difference(first - i, first - j)
    finite += _progression_difference(first + i + 1, first + j + 1)
    return mesh.rational(Fraction(9, 4) * finite /
                         (i * (i + 1) - j * (j + 1)))


def load_model_inputs(source_paths, input_pins, poll):
    """Own parsers; all source I/O happens only inside this explicitly called API."""
    require(set(source_paths) == set(input_pins) == {"matrices", "moments", "h", "v"},
            "exact four model inputs")
    # Authenticate the same bytes being parsed, not a prior read of a pathname.
    raw = Path(source_paths["matrices"]).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == input_pins["matrices"], "matrix input hash")
    wrapper = json.loads(raw)
    del raw
    packet = wrapper["packet"]
    p = packet["parameters"]
    require(p["N"] == N and p["L"] == "9/8" and p["omega"] == 256
            and p["outputBits"] == 256, "matrix model parameters")
    entries = packet["primeCenters"]
    require(len(entries) == 15, "all7 paired shifts plus identity")
    require(entries[0] == {"key": "0", "a": "0", "w": str(7 * (1 << 2048) // 2)},
            "identity shift center")
    primes = []
    for pos, n in enumerate((2, 3, 4, 5, 7, 8, 9)):
        positive, negative = entries[2 * pos + 1:2 * pos + 3]
        a, w = integer(positive["a"], 2052), integer(positive["w"], 2052)
        require(positive["key"] == "+" + str(n) and a > 0 and w < 0,
                "positive shift paired negative weight")
        require(negative == {"key": "-" + str(n), "a": str(-a), "w": str(w)},
                "exact paired centers")
        require(0 < a < (9 * (1 << 2048)) // 4, "shift in support")
        primes.append((Fraction(a, 1 << 2048), Fraction(w, 1 << 2048)))
    del packet, wrapper
    raw = Path(source_paths["moments"]).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == input_pins["moments"], "moment input hash")
    obj = json.loads(raw)
    del raw
    p = obj["parameters"]
    require(obj["schema"] == "RH_WEIL_9_8_SOURCE_MOMENTS_V1"
            and p["L"] == "9/8" and p["omega"] == 256 and p["beta"] == "7/2"
            and p["outputBits"] == 1152 and p["qMax"] == 1023
            and obj["binetRemainderIncludedOnce"] is True
            and len(obj["rows"]) == 1024, "exact old moment model")
    moments = []
    for q, row in enumerate(obj["rows"]):
        require(type(row["q"]) is int and row["q"] == q, "moment order")
        lo, hi = integer(row["lo"], 1168), integer(row["hi"], 1168)
        require(lo <= hi and hi - lo <= 1 << 55, "moment endpoints")
        moments.append(Fraction(lo + hi, 1 << 1153))
    del obj
    h = [[0] * (D + 1) for _ in range(2)]
    h_digest = hashlib.sha256()
    with Path(source_paths["h"]).open("rb") as stream:
        for s in range(2):
            for i in range(s, D + 1, 2):
                line = stream.readline(512)
                require(line.endswith(b"\n") and len(line) < 512, "h line bound")
                h_digest.update(line)
                row = json.loads(line)
                require(type(row) is list and len(row) == 4 and row[:2] == [s, i],
                        "full h stream order")
                lo, hi = integer(row[2], 656), integer(row[3], 656)
                require(lo <= hi, "h endpoint order")
                h[s][i] = lo + hi
            poll()
        require(not stream.read(1), "complete h EOF")
    require(h_digest.hexdigest() == input_pins["h"], "consumed h stream hash")
    x = [[ZERO] * (D + 1) for _ in range(N)]
    v_digest = hashlib.sha256()
    with Path(source_paths["v"]).open("rb") as stream:
        for j in range(N):
            for i in range(j % 2, D + 1, 2):
                line = stream.readline(256)
                require(line.endswith(b"\n") and len(line) < 256, "V line bound")
                v_digest.update(line)
                row = json.loads(line)
                require(type(row) is list and len(row) == 4 and row[:2] == [j, i],
                        "full V stream order")
                lo, hi = integer(row[2], 272), integer(row[3], 272)
                require(lo <= hi, "V endpoint order")
                if i >= N:
                    center = (lo + hi) << (LOW - 257)
                    x[j][i] = center, center
            poll()
        require(not stream.read(1), "complete V EOF")
    require(v_digest.hexdigest() == input_pins["v"], "consumed V stream hash")
    return primes, moments, h, x


def reference_y(moments, h, high, poll, progress):
    """Direct factorial boundary weights, then an independently coded rectangle.

    Does not reuse producer seed weights/arrays. The kstar rational coefficients
    include the SIGNED pole convolution and full rank-two h640 model.
    """
    fact = [1]
    for m in range(1, 2 * D + 3):
        fact.append(fact[-1] * m)
    top = D + N - 1
    boundary = [ZERO] * (top + 2)
    for q, theta in enumerate(moments):
        m = 2 * q
        coefficient = (2 * L ** m + (-1) ** q * theta * 576 ** m) / fact[m]
        a = high.rational(coefficient)
        factorial_square = fact[m] * fact[m]
        for j in range(m + 1):
            # Independently evaluates the factorial quotient, no seed ratio.
            weight = high.rational(factorial_square,
                                   fact[m - j] * fact[m + j + 1])
            boundary[j] = high.add(boundary[j], high.multiply(a, weight))
        if q % 8 == 0:
            poll()
    boundary = [high.scale(a, 2 if j % 2 == 0 else -2)
                for j, a in enumerate(boundary)]
    first = [ZERO] * (top + 1)
    first[0] = high.scale(high.add(boundary[0], boundary[1]), 2)
    for i in range(2, top + 1, 2):
        first[i] = high.scale(high.subtract(boundary[i + 1], boundary[i - 1]),
                              2, 2 * i + 1)
    second = [ZERO] * top
    for i in range(1, top, 2):
        second[i] = high.scale(high.add(
            high.subtract(first[i - 1], first[i + 1]),
            high.scale(high.subtract(boundary[i + 1], boundary[i - 1]), 2)),
            1, 2 * i + 1)
    y, old2, old1 = [], None, None
    for j in range(N):
        if j == 0:
            row = first
        elif j == 1:
            row = second
        else:
            row = [ZERO] * (top - j + 1)
            for i in range(j, top - j + 1, 2):
                row[i] = high.subtract(old2[i], high.scale(
                    high.subtract(old1[i + 1], old1[i - 1]), 2 * j - 1, 2 * i + 1))
        col = [ZERO] * (D + 1)
        for i in range(N + (j % 2), D + 1, 2):
            # Uhat=36 sum |sHat_s><sHat_s|, h raw centers have denominator2^641.
            rank = 36 * sum(h[s][i] * h[s][j] for s in range(2))
            raw = high.add(high.scale(row[i], L * L),
                           high.rational(rank, 1 << 1282))
            col[i] = high.lower_precision(raw)
        y.append(col)
        old2, old1 = old1, row
        poll()
        if progress is not None:
            progress("independent-Ystar", column=j)
    return y


def polynomial_stream(maximum, shift, mesh):
    """Monomial coefficients of P_n(z-shift), with directed recurrence."""
    previous2, previous1 = None, [mesh.rational(1)]
    yield previous1
    if maximum == 0:
        return
    current = [mesh.rational(-shift), mesh.rational(1)]
    yield current
    previous2, previous1 = previous1, current
    for n in range(2, maximum + 1):
        out = [ZERO] * (n + 1)
        for k, a in enumerate(previous1):
            out[k] = mesh.add(out[k], mesh.scale(a, -(2 * n - 1) * shift, n))
            out[k + 1] = mesh.add(out[k + 1], mesh.scale(a, 2 * n - 1, n))
        for k, a in enumerate(previous2):
            out[k] = mesh.subtract(out[k], mesh.scale(a, n - 1, n))
        yield out
        previous2, previous1 = previous1, out


def _dot(a, b, mesh):
    require(len(a) <= len(b), "complete scalar dot")
    answer = ZERO
    for x, y in zip(a, b):
        answer = mesh.add(answer, mesh.multiply(x, y))
    return answer


def endpoint_log_monomials(beta, maximum, mesh, log2, poll):
    """Integral_beta^1 z^k ell(z) dz, including the endpoint limits exactly."""
    args = (1 - beta, Fraction(2), 1 + beta)
    require(-1 < beta < 1, "positive support overlap")
    logs = [logarithm(mesh, q, log2, poll) for q in args]
    primitives = [[] for _ in args]
    for pos, (q, logq) in enumerate(zip(args, logs)):
        power = mesh.rational(q)
        for k in range(maximum + 1):
            bracket = mesh.subtract(mesh.scale(logq, 1, k + 1),
                                    mesh.rational(1, (k + 1) ** 2))
            primitives[pos].append(mesh.multiply(power, bracket))
            power = mesh.scale(power, q)
    beta_power = mesh.rational(beta)
    answer = []
    for k in range(maximum + 1):
        plain = mesh.scale(mesh.subtract(mesh.rational(1), beta_power), 1, k + 1)
        minus, plus, choose = ZERO, ZERO, 1
        for r in range(k + 1):
            minus = mesh.add(minus, mesh.scale(primitives[0][r],
                                              choose if r % 2 == 0 else -choose))
            pdiff = mesh.subtract(primitives[1][r], primitives[2][r])
            plus = mesh.add(plus, mesh.scale(pdiff,
                                            choose if (k - r) % 2 == 0 else -choose))
            if r < k:
                choose = choose * (k - r) // (r + 1)
        answer.append(mesh.subtract(mesh.multiply(log2, plain),
                                    mesh.scale(mesh.add(minus, plus), 1, 2)))
        beta_power = mesh.scale(beta_power, beta)
        if k % 8 == 0:
            poll()
    return answer


def reference_weighted_shift(primes, high, low, poll, progress):
    """Independent J and log-B rectangle; returns already weighted raw forms.

    J_rk=integral P_r(z-t)P_k(z)dz on [t-1,1].  B_rj adds ell(z).
    Only identity-free overlaps with X/Y in QH are requested. The prime weights
    in the input are negative; factor2L pays the paired shifts ONCE.
    """
    sj = [[ZERO] * (D + 1) for _ in range(N)]
    sb = [[ZERO] * N for _ in range(N)]
    jtop, btop = D + N, 2 * N - 1
    log2 = _atanh_log(high, 1, 3, poll)
    for prime, (a, weight) in enumerate(primes):
        t, beta = a / L, a / L - 1
        require(0 < t < 2, "shift clipped support")
        pb = [high.rational(1), high.rational(beta)]
        for n in range(2, jtop + 2):
            pb.append(high.scale(high.subtract(high.scale(pb[-1], (2 * n - 1) * beta),
                                               high.scale(pb[-2], n - 1)), 1, n))
        j0 = [high.rational(2 - t)]
        for k in range(1, jtop + 1):
            j0.append(high.scale(high.subtract(pb[k - 1], pb[k + 1]), 1, 2 * k + 1))
        j1 = [high.subtract(j0[1], high.scale(j0[0], t))]
        for k in range(1, jtop):
            v = high.add(high.scale(j0[k + 1], k + 1), high.scale(j0[k - 1], k))
            j1.append(high.subtract(high.scale(v, 1, 2 * k + 1), high.scale(j0[k], t)))
        mu = endpoint_log_monomials(beta, btop, high, log2, poll)
        b0 = []
        for n, coeff in enumerate(polynomial_stream(btop, Fraction(0), high)):
            b0.append(_dot(coeff, mu, high))
            if n % 8 == 0:
                poll()
        bcol = []
        for n, coeff in enumerate(polynomial_stream(N - 1, t, high)):
            bcol.append(_dot(coeff, mu, high))
            if n % 8 == 0:
                poll()
        b1 = [high.subtract(b0[1], high.scale(b0[0], t))]
        for k in range(1, btop):
            v = high.add(high.scale(b0[k + 1], k + 1), high.scale(b0[k - 1], k))
            b1.append(high.subtract(high.scale(v, 1, 2 * k + 1), high.scale(b0[k], t)))
        jp2 = jp1 = bp2 = bp1 = cp2 = cp1 = None
        for r in range(N):
            if r == 0:
                jr, br = j0, b0
            elif r == 1:
                jr, br = j1, b1
            else:
                jr = [high.scale(j0[r], 1 if r % 2 == 0 else -1)]
                for k in range(1, jtop - r + 1):
                    jr.append(high.subtract(jp2[k], high.scale(
                        high.subtract(jp1[k + 1], jp1[k - 1]), 2 * r - 1, 2 * k + 1)))
                br = None
            cr = [ZERO, jr[1]]
            for k in range(2, btop - r + 1):
                cr.append(high.add(cr[k - 2], high.add(
                    high.scale(jr[k], k), high.scale(jr[k - 2], k - 1))))
            if br is None:
                br = [bcol[r]]
                for k in range(1, btop - r + 1):
                    v = high.subtract(bp2[k], high.scale(
                        high.subtract(bp1[k + 1], bp1[k - 1]), 2 * r - 1, 2 * k + 1))
                    br.append(high.add(v, high.scale(high.subtract(cr[k], cp2[k]),
                                                      1, k * (k + 1))))
            for k in range(r % 2, D + 1, 2):
                sj[r][k] = low.add(sj[r][k], high.lower_precision(high.scale(jr[k], 2 * L * weight)))
            for k in range(r % 2, N, 2):
                sb[r][k] = low.add(sb[r][k], high.lower_precision(high.scale(br[k], 2 * L * weight)))
            jp2, jp1, bp2, bp1, cp2, cp1 = jp1, jr, bp1, br, cp1, cr
            poll()
        if progress is not None:
            progress("independent-shift-log", prime=prime)
    return sj, sb


def reference_pi_polynomials(x, low, poll):
    harmonic = harmonic_table(2 * N)
    out = []
    for j in range(N):
        col = [ZERO] * (D + 1)
        for i in range(j % 2, D + 1, 2):
            raw = low.subtract(x[j][i], low.rational(_log_weight_raw(i, j, harmonic)))
            col[i] = low.scale(raw, gram_d_inverse(i))
        out.append(col)
        poll()
    return out


def _weighted_column_dot(a, b, parity, low, poll):
    result = ZERO
    for i in range(N + parity, D + 1, 2):
        result = low.add(result, low.scale(low.multiply(a[i], b[i]), gram_d_inverse(i)))
        if i % 64 in (0, 1):
            poll()
    return result


def _shift_column_dot(row, col, start, parity, low, poll):
    result = ZERO
    for k in range(start + parity, D + 1, 2):
        result = low.add(result, low.multiply(row[k], col[k]))
        if k % 64 in (0, 1):
            poll()
    return result


def verify_packet(packet_path, source_paths, input_pins, *, poll, progress=None):
    """Future independently gated call; no output files/attempts are made here.

    ``poll()`` MUST enforce the ROOT source-phase remaining time/byte allowance.
    This call computes source science and is forbidden in CODE_PREP. The caller
    authenticates this file and the root/source/model/review/protocol pins first.
    """
    require(callable(poll), "mandatory external resource guard")
    poll()
    high, low = Dyadic(HIGH), Dyadic(LOW)
    primes, moments, h, x = load_model_inputs(source_paths, input_pins, poll)
    y = reference_y(moments, h, high, poll, progress)
    del moments, h
    sj, sb = reference_weighted_shift(primes, high, low, poll, progress)
    pi_poly = reference_pi_polynomials(x, low, poll)
    # FY uses raw Y expansion coefficients C_kj/d_k, not raw forms as maps.
    y_coeff = [[low.scale(v, gram_d_inverse(k)) if v != ZERO else ZERO
                for k, v in enumerate(col)] for col in y]
    pi = pi_interval(high, poll)
    pi2 = high.multiply(pi, pi)
    square_harmonic = harmonic_table(D + N + 2, squared=True)
    odd = [Fraction(0)]
    for k in range(1, D + N + 3):
        odd.append(odd[-1] + Fraction(1, (2 * k - 1) ** 2))
    digest, count, sums, counts = hashlib.sha256(), 0, {}, {}
    unit_center = 1 << (LOW - CENTER)
    with Path(packet_path).open("rb") as stream:
        for label in BLOCKS:
            error_sum, entries = 0, 0
            for parity in (0, 1):
                for i in range(parity, N, 2):
                    start = i if label in ("CX", "YY") else parity
                    for j in range(start, N, 2):
                        line = stream.readline(100)
                        require(line.endswith(b"\n") and len(line) <= 98,
                                "canonical packet line98")
                        row = json.loads(line)
                        require(type(row) is list and len(row) == 4
                                and row[:3] == [label, i, j]
                                and type(row[1]) is int and type(row[2]) is int,
                                "canonical full block/parity/order")
                        value = integer(row[3], 262)
                        canonical = (json.dumps(row, separators=(",", ":")) + "\n").encode("ascii")
                        require(line == canonical, "canonical JSONL encoding")
                        if label == "CX":
                            enclosure = _weighted_column_dot(x[i], x[j], parity, low, poll)
                            tail = tail_gram_raw(i, j, high, pi2, square_harmonic, odd)
                            enclosure = low.add(enclosure, high.lower_precision(tail))
                        elif label == "FX":
                            enclosure = low.add(sb[i][j], _shift_column_dot(
                                sj[i], pi_poly[j], 0, parity, low, poll))
                        elif label == "FY":
                            enclosure = _shift_column_dot(sj[i], y_coeff[j], N, parity, low, poll)
                        elif label == "XY":
                            enclosure = _weighted_column_dot(x[i], y[j], parity, low, poll)
                        else:
                            enclosure = _weighted_column_dot(y[i], y[j], parity, low, poll)
                        center = value * unit_center
                        radius = max(abs(enclosure[0] - center), abs(enclosure[1] - center))
                        weight = (2 * i + 1) * (2 * j + 1)
                        if label in ("CX", "YY") and i != j:
                            weight *= 2  # BOTH Hermitian triangles, never a half-Gram fee.
                        error_sum += radius * radius * weight
                        require(error_sum.bit_length() <= 4 * LOW + 64, "bounded error diagnostic")
                        digest.update(line)
                        count += 1
                        entries += 1
                    poll()
                    if progress is not None:
                        progress("independent-packet", block=label, parity=parity, row=i)
            expected = 100352 if label not in ("CX", "YY") else 50400
            require(entries == expected, "complete matrix triangle/rectangle count")
            # r_ij raw divided by sqrt(d_i*d_j), full native HS squared <=2^-460.
            require(16 * error_sum <= 81 * (1 << (2 * LOW - 460)),
                    "FINAL-center full native arithmetic230:" + label)
            sums[label], counts[label] = str(error_sum), entries
        require(not stream.read(1) and count == 401856, "complete401856 packet EOF")
    poll()
    return {
        "schema": "RH_WEIL_GLOBAL_EXACT_MODEL_INDEPENDENT_CHECK_V1",
        "status": "FIVE_MODEL_BLOCKS_FINAL_CENTER_NATIVE_ARITHMETIC230_VERIFIED",
        "packetSHA256": digest.hexdigest(), "packetRows": count,
        "sourceSHA256": dict(input_pins), "fullNativeWeightedRadiusSums": sums,
        "storedMatrixCounts": counts, "coefficientBits": HIGH,
        "contractionBits": LOW, "rawCenterBits": CENTER,
        "nativeHSSquaredIdentity": "16*weightedSum/(81*2^2048)",
        "eachMatrixNativeHSSquaredUpperPower": -460,
        "bothHermitianTrianglesCharged": True,
        "exactInfiniteCXOffdiagonalTailIncluded": True,
        "representedY": "EXACTdegree2046Kstar/fullh640; intermediate intervals included",
        "representedX": "SAME V256centers plus EXACTendpointlogtail; Qhead exactlyzero",
        "DhIsTrueCovarianceApproximationNotModelGram": True,
        "wholeSignClaim": False,
    }


if __name__ == "__main__":
    raise SystemExit("CODE_PREP library only: no direct execution or source evaluation admitted")

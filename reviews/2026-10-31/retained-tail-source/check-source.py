"""ONE independent retained-tail packet replay; do not run before root binds it.

No producer/old science module is imported.  The independent seed route uses
closed factorial double-integral quotients, not the producer's recursive
boundary weights.  Replay is containment, never interval overlap.  The final
stored half-widths independently pay native full-rectangle/h rounding errors.
The exact endpoint-log infinite tail is included in every column norm.

Required replay freeze (outside run-01): schema RH_WEIL_RETAINED_REPLAY_FREEZE_V1,
authorization ROOT_EXPLICIT_FREEZE_AND_REPLAY, runtimeGoalCreatedAt 1793085111,
checkerSHA256, producerSHA256, producerFreezeSHA256, sourceResultSHA256,
parameters exactly PARAMETERS, inputs exactly INPUTS.  This is a separate
binding; the original producer freeze must not be edited after production.

Preparation permits ast.parse and finite symbolic checks only.  Running this
main performs the actual original448 replay, once, with a hard1800s stop and
no restart/alternate precision.  PASS is a source certificate, not whole-Q,
signed Schur, growth, Xi, RH or root consumption.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
from math import comb, factorial, isqrt
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SELF = Path(__file__).resolve()
OUT = ROOT / "literature/local/2026-10-31-retained-tail-source/run-01"
BITS, OUT_BITS, H_BITS = 3072, 256, 640
N, D, QDEG, TOP = 448, 2046, 576, 2493
CAP_SECONDS, CAP_BYTES = 1800, 160 * (1 << 20)
L = Fraction(9, 8)
DELTA, TAU = Fraction(1, 1 << 49158), Fraction(1, 1 << 49162)
PARAMETERS = dict(L="9/8", omega=256, eta=1, N=N, D=D, qDegree=QDEG,
    qCoefficients=577, bandTerms=1024, sincTerms=1024, workingBits=BITS,
    outputBits=OUT_BITS, hOutputBits=H_BITS, deltaPower=49158,
    tauPower=49162, sourceCapSeconds=CAP_SECONDS, sourceCapBytes=CAP_BYTES)
PREFIX = "literature/local/2026-10-29-weil-9-8/pilot/"
INPUTS = {
    PREFIX+"run-01/certificates/moments.json": "2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9",
    PREFIX+"run-01/certificates/tail-columns.json": "d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
    PREFIX+"source/02-produce.py": "792ee1c93291459ca903b6f4f5e3c4f051f2463a1a020eac756b13fa6b913337",
    PREFIX+"source/08-produce.py": "ae0f487544c203905faecbb78b30f94fb16fe4f2f63c6b9846ca13ea673ba2b7",
    PREFIX+"source/11-checker_quotient.py": "ea6f8ed0e2780aa2835bb75f1a7e08fd807220ac4eb1b14f8c6aa0834e331af3",
    PREFIX+"source/12-raw_column_producer.py": "a8a67b4e08d540f51e152fe05bd19d77ae69fc618e4d6c08cb24c730b3afbb9c",
    "reviews/2026-10-29/weil-9-8-admission/full-weil-analytic-transfer-fresh.md": "0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466",
    "reviews/2026-10-31/retained-tail-source/source-design.md": "55373dda47da0f18e01fd6c0d75e71bb91cac0091cf199ed843d951911a16e2c",
    "reviews/2026-10-31/retained-tail-source/representation-proof.md": "d710b9ea3a094d37907965552dd132890fd930478595906a0545e2d3dbe511f4",
}


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def ceildiv(n, d):
    require(d > 0, "NONPOSITIVE_DENOMINATOR")
    q, r = divmod(n, d)
    return q + bool(r)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def unique_object(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, "DUPLICATE_JSON_KEY")
        out[k] = v
    return out


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique_object,
                      parse_constant=lambda _: require(False, "NONFINITE_JSON"))


def integer(value):
    require(type(value) is str and value != "", "INTEGER_STRING_REQUIRED")
    n = int(value)
    require(str(n) == value, "NONCANONICAL_INTEGER")
    return n


def rational(record):
    require(type(record) is list and len(record) == 2, "RATIONAL_PAIR_REQUIRED")
    n, d = map(integer, record)
    require(d > 0, "RATIONAL_DENOMINATOR")
    q = Fraction(n, d)
    require(q.numerator == n and q.denominator == d, "REDUCED_RATIONAL_REQUIRED")
    return q


def fraction_record(q):
    q = Fraction(q)
    return [str(q.numerator), str(q.denominator)]


def endpoint_pair(value):
    require(type(value) is list and len(value) == 2, "ENDPOINT_PAIR_REQUIRED")
    a, b = map(integer, value)
    require(a <= b, "REVERSED_ENDPOINTS")
    return a, b


class ReplayBudget:
    def __init__(self, bindings):
        self.started = time.monotonic()
        self.started_utc = datetime.now(timezone.utc).isoformat()
        self.stage, self.detail = "preflight", {}
        self.last_write = 0.0
        self.bindings = bindings

    def check(self):
        require(time.monotonic()-self.started <= CAP_SECONDS, "REPLAY_ELAPSED_CAP_STOP")

    def atomic(self, name, obj):
        raw = (json.dumps(obj, ensure_ascii=True, sort_keys=True,
                          separators=(",", ":"))+"\n").encode("ascii")
        require(len(raw) < 1024*1024, "REPLAY_RECORD_TOO_LARGE")
        p = OUT / name
        tmp = OUT / (name+".tmp")
        with tmp.open("wb") as f:
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, p)

    def progress(self, stage=None, force=False, **detail):
        if stage is not None:
            self.stage = stage
        if detail:
            self.detail = detail
        self.check()
        if force or time.monotonic()-self.last_write >= 3:
            self.atomic("replay-progress.json", dict(
                schema="RH_WEIL_RETAINED_SOURCE_REPLAY_PROGRESS_V1",
                status="RUNNING_INDEPENDENT_SOURCE_REPLAY", stage=self.stage,
                detail=self.detail, startedUTC=self.started_utc,
                elapsedSeconds=time.monotonic()-self.started,
                bindings=self.bindings, mathIterations=0, fullQCertified=False))
            self.last_write = time.monotonic()


class Directed:
    """Independent fixed-grid pair arithmetic, including exact-ratio seeding."""
    def __init__(self, bits=BITS):
        self.bits, self.unit = bits, 1 << bits

    def ratio(self, n, d=1):
        require(type(n) is int and type(d) is int and d > 0, "EXACT_RATIO")
        q, rem = divmod(n*self.unit, d)
        return q, q+bool(rem)

    def fraction(self, q):
        q = Fraction(q)
        return self.ratio(q.numerator, q.denominator)

    @staticmethod
    def plus(a, b):
        return a[0]+b[0], a[1]+b[1]

    @staticmethod
    def minus(a, b):
        return a[0]-b[1], a[1]-b[0]

    def times_ratio(self, a, n, d=1):
        require(type(n) is int and type(d) is int and d > 0, "SCALE_RATIO")
        v, w = a[0]*n, a[1]*n
        return min(v, w)//d, ceildiv(max(v, w), d)

    def times_fraction(self, a, q):
        q = Fraction(q)
        return self.times_ratio(a, q.numerator, q.denominator)

    def product(self, a, b):
        corners = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
        return min(corners)//self.unit, ceildiv(max(corners), self.unit)

    def atanh_log(self, n, d, budget=None):
        require(d > 0 and 0 <= 3*n <= d, "LOG_SERIES_DOMAIN")
        power, total = self.ratio(n, d), (0, 0)
        for k in range(1200):
            total = self.plus(total, self.times_ratio(power, 2, 2*k+1))
            power = self.times_ratio(power, n*n, d*d)
            if budget is not None and k % 128 == 0:
                budget.check()
        # Positive tail <=3^(-2400)<2^(-3600).
        return total[0], total[1]+ceildiv(self.unit, 1 << 3600)

    def log_positive(self, value, log2, budget=None):
        value = Fraction(value)
        require(value > 0, "LOG_POSITIVE")
        n, d = value.numerator, value.denominator
        k = n.bit_length()-d.bit_length()
        a, b = (n, d << k) if k >= 0 else (n << -k, d)
        if a < b:
            a *= 2
            k -= 1
        if a >= 2*b:
            b *= 2
            k += 1
        require(b <= a < 2*b, "LOG_RANGE_REDUCTION")
        return self.plus(self.times_ratio(log2, k), self.atanh_log(a-b, a+b, budget))


def contained(iv, pair, stored_bits, mesh, label):
    step = 1 << (mesh.bits-stored_bits)
    require(pair[0]*step <= iv[0] <= iv[1] <= pair[1]*step,
            "INDEPENDENT_CONTAINMENT: "+label)


def direct_machin(terms):
    # Reverse the exact rational summation; no producer scalar routine.
    terms_list = []
    for reciprocal, multiplier in ((239, -4), (5, 16)):
        power = reciprocal
        for k in range(terms):
            terms_list.append(Fraction(multiplier*(-1)**k, (2*k+1)*power))
            power *= reciprocal*reciprocal
    return sum(reversed(terms_list), Fraction(0))


def bernoulli_values(last, budget):
    # Akiyama--Tanigawa, distinct from the producer binomial recurrence.
    work, vals = [], []
    for m in range(last+1):
        work.append(Fraction(1, m+1))
        for j in range(m, 0, -1):
            work[j-1] = j*(work[j-1]-work[j])
        vals.append(-work[0] if m == 1 else work[0])
        if m % 16 == 0:
            budget.progress("independent-exact-bernoulli", degree=m)
    require(vals[:5] == [Fraction(1), -Fraction(1,2), Fraction(1,6),
                          Fraction(0), -Fraction(1,30)], "BERNOULLI_CONTROLS")
    return vals


def independent_scalars(packet, bernoulli, mesh, budget):
    sc = packet["scalarIntervals"]
    require(sc["workingBits"] == BITS, "SCALAR_SCALE")
    stored = {k: endpoint_pair(sc[k]) for k in ("log2", "pi", "gamma", "contact")}
    # Exact rational 2atanh(1/3), with an explicit positive geometric tail.
    total = Fraction(0)
    power = 3
    for k in range(1200):
        total += Fraction(2, (2*k+1)*power)
        power *= 9
        if k % 128 == 0:
            budget.check()
    tail = Fraction(9, 4*(2401)*3**2401)
    log2 = (mesh.fraction(total)[0], mesh.fraction(total+tail)[1])
    pi_mid = direct_machin(800)
    pi_rad = Fraction(16,1601*5**1601)+Fraction(4,1601*239**1601)
    pi_iv = (mesh.fraction(pi_mid-pi_rad)[0], mesh.fraction(pi_mid+pi_rad)[1])
    h255 = sum((Fraction(1,k) for k in range(1,256)), Fraction(0))
    rational_gamma = h255+Fraction(1,512)+sum(
        (bernoulli[2*k]/(2*k*256**(2*k)) for k in range(1,257)), Fraction(0))
    remainder = Fraction(4*factorial(513),6**514*256**514)
    require(remainder < Fraction(1,1 << 1500), "GAMMA_REAL_REMAINDER")
    gamma_iv = mesh.minus(mesh.fraction(rational_gamma), mesh.times_ratio(log2,8))
    eps = ceildiv(remainder.numerator*mesh.unit,remainder.denominator)
    gamma_iv = gamma_iv[0]-eps, gamma_iv[1]+eps
    logpi = (mesh.log_positive(Fraction(pi_iv[0],mesh.unit),log2,budget)[0],
             mesh.log_positive(Fraction(pi_iv[1],mesh.unit),log2,budget)[1])
    contact_iv = mesh.plus(gamma_iv, mesh.plus(logpi,mesh.log_positive(2*L,log2,budget)))
    for name, iv in (("log2",log2),("pi",pi_iv),("gamma",gamma_iv),("contact",contact_iv)):
        contained(iv, stored[name], BITS, mesh, "scalar-"+name)
    contact = rational(sc["contactCenter"])
    radius = rational(sc["contactRadius"])
    require(contact == Fraction(sum(stored["contact"]),2*mesh.unit)
            and radius == Fraction(stored["contact"][1]-stored["contact"][0],2*mesh.unit)
            and radius < Fraction(1,1 << 600), "CONTACT_MIDPOINT_RADIUS")
    require(rational(sc["gammaRemainder"]) == remainder, "GAMMA_REMAINDER_RECORD")
    ppi = direct_machin(160)
    require(ppi == rational(sc["sincPiExact"]) and ppi > 3, "EXACT_SINC_PI")
    return dict(log2=log2, pi=pi_iv, contact=contact, ppi=ppi)


def q_coefficients(bernoulli, budget):
    powers = [Fraction(3,4)**k for k in range(QDEG+2)]
    out = []
    for m in range(QDEG+1):
        n = m+1
        bpoly = sum((comb(n,k)*bernoulli[k]*powers[n-k]
                     for k in range(n+1)), Fraction(0))
        out.append(Fraction(2**m,factorial(n))*bpoly*(2*L)**m)
        if m % 16 == 0:
            budget.progress("independent-q-rationals", degree=m)
    require(out[:3] == [Fraction(1,4), -Fraction(3,64), -Fraction(81,512)],
            "Q_PHYSICAL_INITIAL_COEFFICIENTS")
    return out


def factorial_seeds(coefficients, mesh, budget, label):
    """Direct exact K_0j/K_1j factorial quotients, before dyadic rounding.

    For k_m(z,w)=|z-w|^m/2^m:
    K_0j=8 m!(m+1)!/((m-j+1)!(m+j+2)!), j even<=m+1;
    K_1j=-8 m!(m+1)!(m-j+1)/
          ((m-j+2)!(m+j+1)!(m+j+3)), j odd<=m+2.
    The latter permits j=m+2 for odd m.  Support/parity zeros are exact.
    No producer boundary weights or ratio recurrence are used.
    """
    fs = [1]
    for k in range(1,2*D+6):
        fs.append(fs[-1]*k)
    first, second = [(0,0)]*(TOP+1), [(0,0)]*TOP
    summands = 0
    for m, a in enumerate(coefficients):
        if not a:
            continue
        numerator = 8*a.numerator*fs[m]*fs[m+1]
        denominator = a.denominator
        for j in range(0,min(m+1,TOP)+1,2):
            term = mesh.ratio(numerator,denominator*fs[m-j+1]*fs[m+j+2])
            first[j] = mesh.plus(first[j],term)
            summands += 1
        for j in range(1,min(m+2,TOP-1)+1,2):
            n = -numerator*(m-j+1)
            term = mesh.ratio(n,denominator*fs[m-j+2]*fs[m+j+1]*(m+j+3))
            second[j] = mesh.plus(second[j],term)
            summands += 1
        budget.progress(label+"-factorial-seeds", kernelDegree=m, summands=summands)
    return first,second


def recurrence_rows(seeds, mesh, kind, budget):
    old2, old1 = None,None
    for r in range(N):
        last = TOP-r
        bound = r+QDEG if kind == "q" else D
        row = {}
        for j in range(r,last+1,2):
            if j > bound:
                row[j] = (0,0)
            elif r < 2:
                row[j] = seeds[r][j]
            else:
                diff = mesh.minus(old1[j+1],old1[j-1])
                row[j] = mesh.minus(old2[j],mesh.times_ratio(diff,2*r-1,2*j+1))
        yield row
        old2,old1 = old1,row
        budget.check()


class StreamReader:
    def __init__(self, record, expected_file, budget):
        require(set(record) == {"file","bytes","rows","sha256","complete"}
                and record["file"] == expected_file and record["complete"] is True,
                "STREAM_MANIFEST: "+expected_file)
        self.record,self.name,self.budget = record,expected_file,budget
        self.handle = (OUT/expected_file).open("rb")
        self.sha,self.size,self.count = hashlib.sha256(),0,0

    def read(self):
        raw = self.handle.readline(65537)
        require(raw and raw.endswith(b"\n") and len(raw) <= 65536,
                "STREAM_ROW_TRUNCATED: "+self.name)
        self.sha.update(raw)
        self.size += len(raw)
        self.count += 1
        if self.count % 1024 == 0:
            self.budget.check()
        return decode(raw)

    def finish(self):
        require(self.handle.read(1) == b"", "STREAM_EXTRA_ROWS: "+self.name)
        self.handle.close()
        require(self.count == self.record["rows"] and self.size == self.record["bytes"]
                and self.sha.hexdigest() == self.record["sha256"],
                "STREAM_COUNT_BYTES_HASH: "+self.name)


def parse_row(row, column, degree):
    require(type(row) is list and len(row) == 4
            and type(row[0]) is int and type(row[1]) is int
            and row[:2] == [column,degree], "ROW_COMPLETE_ORDER_PARITY")
    return endpoint_pair(row[2:])


def raw_norm2(numerator, bits):
    return Fraction(16*numerator,81*(1 << (2*bits+2)))


def replay_h(packet, stream_record, seeds, mesh, budget):
    reader = StreamReader(stream_record,"h-columns.jsonl",budget)
    centers = [[0]*(D+1),[0]*(D+1)]
    checks = packet["oldHColumns"]["fullPolynomialChecks"]
    require(type(checks) is list and len(checks) == 2, "H_COLUMN_CERTIFICATES")
    summary = []
    for s in (0,1):
        widths = squares = 0
        for i in range(s,D+1,2):
            pair = parse_row(reader.read(),s,i)
            iv = mesh.times_fraction(seeds[s][i],-L*L)
            if i == s:
                iv = mesh.plus(iv,mesh.fraction((1-DELTA)*2*L/(2*s+1)))
            contained(iv,pair,H_BITS,mesh,f"h:{s}:{i}")
            mid,weight = pair[0]+pair[1],(2*i+1)*(2*s+1)
            centers[s][i] = mid
            widths += (pair[1]-pair[0])**2*weight
            squares += mid*mid*weight
        rho2,norm2 = raw_norm2(widths,H_BITS),raw_norm2(squares,H_BITS)
        cap = Fraction(1,29) if s == 0 else Fraction(3,50)
        rec = checks[s]
        require(rec["column"] == s and integer(rec["widthWeightedNumerator"]) == widths
                and rational(rec["serializedRadiusSquared"]) == rho2
                and rational(rec["normSquared"]) == norm2
                and rational(rec["originalNormCap"]) == cap, "H_EXACT_NORM_WIDTH_RECORD")
        actual = Fraction(16*integer(rec["distanceWeightedNumerator"]),
                          81*(1 << (2*BITS+2)))
        require(rational(rec["roundingSquared"]) == actual and 0 <= actual <= rho2
                and rho2 < Fraction(1,1 << 1040), "H_FULL_NATIVE_HALF_WIDTH")
        require(norm2 <= (cap+Fraction(1,1 << 512))**2
                and rec["sourceColumnErrorPower"] == -512, "H_FULL_POLYNOMIAL_NORM")
        summary.append(dict(column=s,fullNormSquared=fraction_record(norm2),
                            independentRoundingSquared=fraction_record(rho2)))
        budget.progress("independent-h-containment",force=True,column=s)
    reader.finish()
    require(reader.count == 2047, "H_FULL_SHAPE")
    return centers,summary


def replay_v(packet, record, qseeds, bseeds, h, sc, mesh, budget):
    reader = StreamReader(record,"finite-columns.jsonl",budget)
    qrows = recurrence_rows(qseeds,mesh,"q",budget)
    brows = recurrence_rows(bseeds,mesh,"band",budget)
    harmonic = [Fraction(0)]
    for k in range(1,2*N+1):
        harmonic.append(harmonic[-1]+Fraction(1,k))
    width_sum,head_entries = 0,0
    norm,comp = [0]*N,[0]*N
    head = {}
    for j,(qr,br) in enumerate(zip(qrows,brows)):
        for i in range(j%2,D+1,2):
            pair = parse_row(reader.read(),j,i)
            if i < j:
                require(pair == head[(i,j)], "SAME_HEAD_EXACT_SYMMETRY")
            else:
                iv = mesh.times_fraction(mesh.plus(qr[i],br[i]),-L*L)
                if i == j:
                    z = Fraction(1,2*j+1)+2*(harmonic[2*j]-harmonic[j])
                    loggram = mesh.times_ratio(mesh.minus(sc["log2"],mesh.fraction(z)),4,2*j+1)
                else:
                    loggram = mesh.ratio(-4,abs(i-j)*(i+j+1))
                iv = mesh.minus(iv,mesh.times_fraction(loggram,L/2))
                unum = 36*sum(h[s][i]*h[s][j] for s in (0,1))
                iv = mesh.minus(iv,mesh.ratio(unum,1 << (2*H_BITS+2)))
                if i == j:
                    diagonal = (harmonic[j]-sc["contact"]-Fraction(7,2)-TAU)*2*L/(2*j+1)
                    iv = mesh.plus(iv,mesh.fraction(diagonal))
                contained(iv,pair,OUT_BITS,mesh,f"V:{j}:{i}")
                if i < N:
                    head[(j,i)] = pair
            mid,weight = sum(pair),(2*i+1)*(2*j+1)
            width_sum += (pair[1]-pair[0])**2*weight
            norm[j] += mid*mid*weight
            if i >= N:
                comp[j] += mid*mid*weight
            else:
                head_entries += 1
        require(norm[j] >= comp[j], "EXACT_FINITE_FULL_COMPLEMENT_GEOMETRY")
        budget.progress("independent-V-containment",column=j,rows=reader.count)
    reader.finish()
    require(reader.count == 458528 and len(head) == 50400 and head_entries == 100352,
            "V_COMPLETE_RECTANGLE_HEAD_COUNTS")
    ar = packet["arithmetic"]
    rho2 = raw_norm2(width_sum,OUT_BITS)
    actual = Fraction(16*integer(ar["distanceWeightedNumerator"]),81*(1 << (2*BITS+2)))
    require(integer(ar["widthWeightedNumerator"]) == width_sum
            and rational(ar["serializedRadiusHSSquared"]) == rho2
            and rational(ar["arithmeticHSSquared"]) == actual
            and 0 <= actual <= rho2 <= Fraction(1,1 << 440), "V_FULL_NATIVE_HALF_WIDTH_HS")
    require(ar["fullParityRows"] == 458528 and ar["uniqueHeadEntries"] == 50400
            and ar["fullHeadEntries"] == 100352
            and ar["headConstruction"] == "single_upper_triangle_then_exact_copy",
            "ARITHMETIC_HEAD_METADATA")
    return norm,comp,dict(completeParityRows=reader.count,uniqueHeadEntries=len(head),
        fullHeadEntries=head_entries,independentArithmeticHSSquared=fraction_record(rho2),
        producerInternalDistanceReplayed=False,
        internalDistanceRole="diagnostic algebraic record only; independent certificate uses full stored half-width")


def sqrt_interval(pair,bits):
    require(0 <= pair[0] <= pair[1], "NONNEGATIVE_SQUARED_NORM")
    # At output grid2^-bits, sqrt(n/2^bits)=sqrt(n*2^bits)/2^bits.
    lo = isqrt(pair[0] << bits)
    hi = isqrt(pair[1] << bits)
    if hi*hi < pair[1] << bits:
        hi += 1
    return Fraction(lo,1 << bits),Fraction(hi,1 << bits)


def replay_norms(packet,record,full_nums,comp_nums,sc,mesh,budget):
    reader = StreamReader(record,"column-norms.jsonl",budget)
    harmonic2,odd2 = [Fraction(0)],[Fraction(0)]
    # Same closed trace, independently restricted to the indices actually used.
    for r in range(1,1501):
        harmonic2.append(harmonic2[-1]+Fraction(1,r*r))
        odd2.append(odd2[-1]+Fraction(1,(2*r-1)**2))
        if r % 128 == 0:
            budget.check()
    pi2 = mesh.product(sc["pi"],sc["pi"])
    total_full,total_comp = (0,0),(0,0)
    for j in range(N):
        i0 = D+1+(1 if (D+1-j)%2 else 0)
        k = (i0-j)//2
        # b_ij²=1/(i-j)²−1/(i+j+1)².  No discarded endpoint tail.
        tail = mesh.minus(mesh.fraction(odd2[k+j]-harmonic2[k-1]/4),mesh.times_ratio(pi2,1,12))
        require(tail[0] >= 0, "EXACT_LOG_TAIL_POSITIVE")
        full = mesh.plus(mesh.fraction(raw_norm2(full_nums[j],OUT_BITS)),tail)
        comp = mesh.plus(mesh.fraction(raw_norm2(comp_nums[j],OUT_BITS)),tail)
        row = reader.read()
        require(type(row) is dict and set(row) == {"column","nativeModelNormSquared",
            "nativeModelComplementNormSquared","nativeInfiniteTailNormSquared",
            "squaredNormOutputBits","firstInfiniteDegree","K","actualColumnL2ErrorPower"}
            and row["column"] == j and row["squaredNormOutputBits"] == OUT_BITS
            and row["firstInfiniteDegree"] == i0 and row["K"] == k
            and row["actualColumnL2ErrorPower"] == -203, "COLUMN_NORM_METADATA")
        for name,iv in (("nativeModelNormSquared",full),
                        ("nativeModelComplementNormSquared",comp),
                        ("nativeInfiniteTailNormSquared",tail)):
            pair = endpoint_pair(row[name])
            require(pair[0] >= 0, "STORED_NEGATIVE_SQUARED_NORM")
            contained(iv,pair,OUT_BITS,mesh,f"norm:{j}:{name}")
        total_full,total_comp = mesh.plus(total_full,full),mesh.plus(total_comp,comp)
        budget.progress("independent-log-tail-norms",column=j)
    reader.finish()
    require(reader.count == N, "COLUMN_NORM_COMPLETE_SHAPE")
    summary = packet["complement"]
    require(summary["squaredNormOutputBits"] == OUT_BITS
            and summary["actualComplementErrorHSBoundPower"] == -198,
            "COMPLEMENT_NORM_ERROR_SCALE")
    for name,iv in (("nativeModelHSSquared",total_full),
                    ("nativeModelComplementHSSquared",total_comp)):
        pair = endpoint_pair(summary[name])
        require(pair[0] >= 0, "NEGATIVE_MODEL_HS_NORM")
        contained(iv,pair,OUT_BITS,mesh,"total-"+name)
    comp_pair = endpoint_pair(summary["nativeModelComplementHSSquared"])
    lower,upper = sqrt_interval(comp_pair,OUT_BITS)
    eps = Fraction(1,1 << 198)
    return dict(modelHSSquared=summary["nativeModelHSSquared"],
        modelComplementHSSquared=summary["nativeModelComplementHSSquared"],
        squaredNormBits=OUT_BITS,
        actualComplementHSNorm=[fraction_record(max(Fraction(0),lower-eps)),fraction_record(upper+eps)],
        errorTransport="sqrt(model squared norm) +/-2^-198; no squared-norm additive shortcut",
        fullOutsideHead="rows448..2046 plus exact symbolic infinite endpoint-log tail")


def verify_error_ledger(packet,sc):
    ledger = packet["errorLedger"]
    eq = Fraction(4608)*Fraction(3,4)**577
    eb = 2*L*(Fraction(914*576**2048,factorial(2048))+
              Fraction(1,1 << 1098)*Fraction(68,25)**576)
    es = Fraction(576**2049,factorial(2049))/Fraction(
        endpoint_pair(packet["scalarIntervals"]["pi"])[0],1 << BITS)
    require(rational(ledger["exactQBound"]) == eq < Fraction(1,1 << 227)
            and rational(ledger["exactBandBound"]) == eb < Fraction(1,1 << 204)
            and rational(ledger["exactSincBound"]) == es < Fraction(1,1 << 513),
            "EXACT_GLOBAL_KERNEL_ERROR_LEDGER")
    eps_h = Fraction(1,1 << 513)+Fraction(1,1 << 646)+Fraction(1,1 << 520)
    uerr = Fraction(1,1 << 512)*(Fraction(162,29)+Fraction(162,50)+108*Fraction(1,1 << 512))
    ev = Fraction(1,1 << 204)+Fraction(1,1 << 227)+9*Fraction(1,1 << 512)+Fraction(1,1 << 600)+Fraction(1,1 << 220)
    require(eps_h < Fraction(1,1 << 512) and uerr < 9*Fraction(1,1 << 512)
            and ev < Fraction(1,1 << 203) and 22*ev < Fraction(1,1 << 198)
            and N < 22*22, "GLOBAL_OP_HS_ERROR_TARGET")
    expected = dict(qOperatorErrorPower=-227,bandOperatorErrorPower=-204,
        hGlobalErrorPower=-512,hFullPolynomialRoundingPower=-520,
        oldRankTwoError="9*2^-512",contactScalarErrorPower=-600,
        finiteAssemblyArithmeticHSBoundPower=-220,nativeVOperatorErrorPower=-203,
        nativeVHSErrorPower=-198,nativeGOperatorErrorPower=-203,
        errorsAreGlobalOriginalDu=True,momentBinetChargedOnce=True,
        laterInversionOrWholeSchurErrorPaid=False)
    require(all(ledger.get(k) == v for k,v in expected.items()), "ERROR_LEDGER_SCOPE")


def input_inventory():
    inventory = {}
    moments_raw = None
    for name,expected in INPUTS.items():
        path = (ROOT/name).resolve()
        require(path.is_relative_to(ROOT), "INPUT_PATH_ESCAPE")
        raw = path.read_bytes()
        require(digest(raw) == expected, "INPUT_PIN: "+name)
        inventory[name] = dict(bytes=len(raw),sha256=expected)
        if name.endswith("/moments.json"):
            moments_raw = raw
    return inventory,moments_raw


def moments_from(raw):
    data = decode(raw)
    p = data["parameters"]
    require(data["schema"] == "RH_WEIL_9_8_SOURCE_MOMENTS_V1"
            and data["binetRemainderIncludedOnce"] is True
            and p["L"] == "9/8" and p["beta"] == "7/2" and p["omega"] == 256
            and p["qMin"] == 0 and p["qMax"] == 1023 and p["outputBits"] == 1152,
            "MOMENT_WRAPPER")
    require(len(data["rows"]) == 1024, "MOMENT_SHAPE")
    mids = []
    for q,row in enumerate(data["rows"]):
        require(type(row["q"]) is int and row["q"] == q, "MOMENT_ORDER")
        a,b = integer(row["lo"]),integer(row["hi"])
        require(0 <= b-a <= 1 << 55, "MOMENT_WIDTH")
        mids.append(Fraction(a+b,1 << 1153))
    return mids


def preflight(freeze_path):
    freeze_path = freeze_path.resolve()
    require(not freeze_path.is_relative_to(OUT), "REPLAY_FREEZE_OUTSIDE_PACKET")
    require(OUT.is_dir() and not (OUT/"replay-result.json").exists()
            and not (OUT/"replay-progress.json").exists(), "ONE_REPLAY_ALREADY_ATTEMPTED_OR_NO_PACKET")
    freeze_raw = freeze_path.read_bytes()
    require(len(freeze_raw) <= 65536, "REPLAY_FREEZE_SIZE")
    freeze = decode(freeze_raw)
    result_raw = (OUT/"result.json").read_bytes()
    require(len(result_raw) <= 1024*1024, "SOURCE_RESULT_SIZE")
    packet = decode(result_raw)
    producer_sha = digest((HERE/"produce-source.py").read_bytes())
    checker_sha = digest(SELF.read_bytes())
    require(freeze.get("schema") == "RH_WEIL_RETAINED_REPLAY_FREEZE_V1"
            and freeze.get("authorization") == "ROOT_EXPLICIT_FREEZE_AND_REPLAY"
            and freeze.get("runtimeGoalCreatedAt") == 1793085111,
            "NO_ROOT_REPLAY_FREEZE")
    require(freeze.get("parameters") == PARAMETERS and freeze.get("inputs") == INPUTS
            and freeze.get("checkerSHA256") == checker_sha
            and freeze.get("producerSHA256") == producer_sha
            and freeze.get("sourceResultSHA256") == digest(result_raw)
            and freeze.get("producerFreezeSHA256") == packet["freezeSHA256"],
            "REPLAY_FREEZE_BINDING")
    require(packet["schema"] == "RH_WEIL_RETAINED_SOURCE_PACKET_V1"
            and packet["status"] == "SOURCE_PACKET_PRODUCED_PENDING_INDEPENDENT_REPLAY"
            and packet["runtimeGoalCreatedAt"] == 1793085111
            and packet["parameters"] == PARAMETERS and packet["producerSHA256"] == producer_sha
            and 0 <= packet["elapsedSeconds"] <= CAP_SECONDS, "SOURCE_PACKET_BINDING")
    require(packet["fullQCertified"] is False and packet["RHCertified"] is False
            and packet["mathIterations"] == 0 and packet["signedMargin"] is None
            and packet["wholeSchurMargin"] is None, "SOURCE_ONLY_SCOPE")
    require(not list(OUT.glob("*.part")) and not list(OUT.glob("*.tmp")), "INCOMPLETE_SOURCE_OUTPUT")
    files = list(OUT.iterdir())
    require(all(p.is_file() for p in files)
            and sum(p.stat().st_size for p in files) <= CAP_BYTES, "PACKET_CAP_OR_SHAPE")
    streams = packet["streams"]
    require(type(streams) is list and len(streams) == 3
            and [x["file"] for x in streams] == ["h-columns.jsonl","finite-columns.jsonl","column-norms.jsonl"]
            and [x["rows"] for x in streams] == [2047,458528,448], "THREE_STREAMS_COMPLETE_ORDER")
    fc,hc = packet["finiteColumns"],packet["oldHColumns"]
    require(fc["file"] == "finite-columns.jsonl" and fc["intervalDenominatorPower"] == OUT_BITS
            and fc["midpointDenominatorPower"] == OUT_BITS+1 and fc["completeParityRows"] == 458528
            and hc["file"] == "h-columns.jsonl" and hc["intervalDenominatorPower"] == H_BITS
            and hc["midpointDenominatorPower"] == H_BITS+1 and hc["completeParityRows"] == 2047
            and hc["UrawCoefficient"] == 36, "SOURCE_SCALE_METADATA")
    tail = packet["symbolicInfiniteTail"]
    require(tail["firstDegree"] == D+1 and tail["endpointLogDiscarded"] is False
            and tail["nativeCoefficient"] == "sqrt((2i+1)(2j+1))/((i-j)(i+j+1))"
            and tail["rawExpansionCoefficient"] == "(2i+1)/((i-j)(i+j+1))",
            "EXACT_INFINITE_TAIL_DECLARATION")
    require(packet["Ghat"] == dict(source="first448 rows of SAME finite-columns stream",
        symmetricHeadExactlyCopied=True,modelConsistencyExact=True), "SAME_G_HEAD_DECLARATION")
    bindings = dict(checkerSHA256=checker_sha,producerSHA256=producer_sha,
        sourceResultSHA256=digest(result_raw),replayFreezeSHA256=digest(freeze_raw),
        producerFreezeSHA256=packet["freezeSHA256"])
    return packet,bindings,freeze_raw,freeze_path


def replay(freeze_path):
    packet,bindings,freeze_raw,freeze_path = preflight(freeze_path)
    budget = ReplayBudget(bindings)
    try:
        budget.progress("input-pins",force=True)
        inventory,moment_raw = input_inventory()
        require(packet["inputs"] == inventory, "ACTUAL_INPUT_INVENTORY")
        moments = moments_from(moment_raw)
        bernoulli = bernoulli_values(QDEG+1,budget)
        mesh = Directed()
        budget.progress("independent-scalars",force=True)
        sc = independent_scalars(packet,bernoulli,mesh,budget)
        verify_error_ledger(packet,sc)
        qcoeff = q_coefficients(bernoulli,budget)
        sinc = [Fraction(0)]*(D+1)
        band = [Fraction(0)]*(D+1)
        for q in range(1024):
            m = 2*q
            sinc[m] = Fraction((-1)**q*256*576**m,factorial(m+1))/sc["ppi"]
            band[m] = (-1)**q*moments[q]*576**m/factorial(m)
        hseeds = factorial_seeds(sinc,mesh,budget,"sinc")
        h,hsummary = replay_h(packet,packet["streams"][0],hseeds,mesh,budget)
        qseeds = factorial_seeds(qcoeff,mesh,budget,"q")
        bseeds = factorial_seeds(band,mesh,budget,"band")
        full_nums,comp_nums,arithmetic = replay_v(packet,packet["streams"][1],qseeds,bseeds,h,sc,mesh,budget)
        norms = replay_norms(packet,packet["streams"][2],full_nums,comp_nums,sc,mesh,budget)
        budget.progress("final-pin-recheck",force=True)
        require(input_inventory()[0] == inventory
                and digest(SELF.read_bytes()) == bindings["checkerSHA256"]
                and digest((HERE/"produce-source.py").read_bytes()) == bindings["producerSHA256"]
                and digest((OUT/"result.json").read_bytes()) == bindings["sourceResultSHA256"]
                and freeze_path.read_bytes() == freeze_raw, "INPUT_CHANGED_DURING_REPLAY")
        # Bind the files as they exist at the end as well as when streamed.
        for record in packet["streams"]:
            final_hash,final_size = hashlib.sha256(),0
            with (OUT/record["file"]).open("rb") as handle:
                while chunk := handle.read(1 << 20):
                    final_hash.update(chunk)
                    final_size += len(chunk)
                    budget.check()
            require(final_size == record["bytes"] and final_hash.hexdigest() == record["sha256"],
                    "STREAM_CHANGED_DURING_REPLAY: "+record["file"])
        result = dict(schema="RH_WEIL_RETAINED_SOURCE_REPLAY_V1",
            status="INDEPENDENT_SOURCE_REPLAY_PASS_NOT_WHOLE_Q",runtimeGoalCreatedAt=1793085111,
            parameters=PARAMETERS,startedUTC=budget.started_utc,
            endedUTC=datetime.now(timezone.utc).isoformat(),elapsedSeconds=time.monotonic()-budget.started,
            bindings=bindings,inputs=inventory,arithmetic=arithmetic,fullHColumns=hsummary,
            complement=norms,independentSeedRoute="closed exact factorial double-integral quotients",
            containment="every directed replay interval is contained in its stored raw interval",
            nativeVOperatorErrorPower=-203,nativeVHSErrorPower=-198,nativeGOperatorErrorPower=-203,
            producerOnlyResultConsumed=False,rootConsumption="PENDING_ROOT_AUDIT",
            signedMargin=None,wholeSchurMargin=None,fullQCertified=False,RHCertified=False,
            mathIterations=0,pendingProcesses=[],
            scope="original448 full-H source packet only; signed whole/core/growing/Xi premises unpaid")
        budget.check()
        budget.atomic("replay-result.json",result)
        budget.progress("complete-source-replay-pending-root",force=True)
        return result
    except BaseException as error:
        result = dict(schema="RH_WEIL_RETAINED_SOURCE_REPLAY_STOP_V1",status="STOPPED_NO_RETRY",
            runtimeGoalCreatedAt=1793085111,parameters=PARAMETERS,bindings=bindings,
            startedUTC=budget.started_utc,endedUTC=datetime.now(timezone.utc).isoformat(),
            elapsedSeconds=time.monotonic()-budget.started,stage=budget.stage,detail=budget.detail,
            errorType=type(error).__name__,reason=str(error)[:1500],
            fullQCertified=False,RHCertified=False,mathIterations=0,pendingProcesses=[],
            nextAction="root inspect exact stop; no replay/precision/degree/window/source successor")
        budget.atomic("replay-result.json",result)
        budget.atomic("replay-progress.json",result)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay-freeze-file",type=Path,required=True)
    args = parser.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    result = replay(args.replay_freeze_file)
    print(json.dumps(dict(status=result["status"],elapsedSeconds=result["elapsedSeconds"],
                         result=str(OUT/"replay-result.json")),ensure_ascii=False))


if __name__ == "__main__":
    main()

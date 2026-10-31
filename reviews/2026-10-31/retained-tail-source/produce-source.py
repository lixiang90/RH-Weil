"""ONE fixed retained-tail source producer. DO NOT RUN without root freeze.

No imports of old science drivers, network, subprocess, NumPy, retry or scans.
Output is local/ignored and is a source packet, never a sign/RH certificate.

Run guard: --freeze-file JSON must have schema RH_WEIL_RETAINED_SOURCE_FREEZE_V1,
authorization ROOT_EXPLICIT_FREEZE_AND_RUN, runtimeGoalCreatedAt 1793085111,
parameters exactly PARAMETERS, producerSHA256 this file's digest, and inputs
exactly the pinned INPUTS mapping below. The freeze file must be outside OUT.

Explicit implementation annotations to source-design.md (not silent repairs):
* K_0j is evaluated ONLY for even j; K_1j ONLY for odd j. Other parity is zero.
* gamma uses H255-psi(256), with the positive-real Binet remainder below;
  contact midpoint is frozen separately and its radius paid as scalar error.
* rectangle seeds reach2494. Head entries are computed once and then copied;
  HS accounting counts all100352 head entries, not50400 unique entries.
* actual radius is maximum distance from FINAL stored midpoint to the directed
  model interval, not half the unquantized working interval. A second larger
  serialized-half-width budget is checked too. Native square roots stay symbolic.
* the endpoint tail is symbolic/exact; output rows0..2046 do NOT truncate it.
* h polynomial centers are output640 and define Uhat exactly; their global
  source error is charged separately from arithmetic assembly of Vhat.
* the requested progress/result are atomic; .part files remain after a stop.

Only ast.parse/static review is authorized during script preparation. The small
symbolic regressions below execute inside main, after freeze and before arrays.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
import os
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "literature/local/2026-10-31-retained-tail-source/run-01"
SELF = Path(__file__).resolve()
P, OB, HB, N, D, M = 3072, 256, 640, 448, 2046, 576
TOP = D + N - 1
L = F(9, 8)
DELTA = F(1, 1 << 49158)
TAU = DELTA / 16
CAP_SECONDS, CAP_BYTES = 1800, 160 * (1 << 20)
PARAMETERS = dict(L="9/8", omega=256, eta=1, N=N, D=D, qDegree=M,
                  qCoefficients=M+1, bandTerms=1024, sincTerms=1024,
                  workingBits=P, outputBits=OB, hOutputBits=HB,
                  deltaPower=49158, tauPower=49162,
                  sourceCapSeconds=CAP_SECONDS, sourceCapBytes=CAP_BYTES)
PREFIX = "literature/local/2026-10-29-weil-9-8/pilot/"
INPUTS = {
    PREFIX + "run-01/certificates/moments.json":
        "2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9",
    PREFIX + "run-01/certificates/tail-columns.json":
        "d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e",
    PREFIX + "source/02-produce.py":
        "792ee1c93291459ca903b6f4f5e3c4f051f2463a1a020eac756b13fa6b913337",
    PREFIX + "source/08-produce.py":
        "ae0f487544c203905faecbb78b30f94fb16fe4f2f63c6b9846ca13ea673ba2b7",
    PREFIX + "source/11-checker_quotient.py":
        "ea6f8ed0e2780aa2835bb75f1a7e08fd807220ac4eb1b14f8c6aa0834e331af3",
    PREFIX + "source/12-raw_column_producer.py":
        "a8a67b4e08d540f51e152fe05bd19d77ae69fc618e4d6c08cb24c730b3afbb9c",
    "reviews/2026-10-29/weil-9-8-admission/full-weil-analytic-transfer-fresh.md":
        "0cdb4173b7664b73b47fd8789c0629f0535a208ad9af2a4af8eb86422c64a466",
    "reviews/2026-10-31/retained-tail-source/source-design.md":
        "55373dda47da0f18e01fd6c0d75e71bb91cac0091cf199ed843d951911a16e2c",
    "reviews/2026-10-31/retained-tail-source/representation-proof.md":
        "d710b9ea3a094d37907965552dd132890fd930478595906a0545e2d3dbe511f4",
}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def up(n, d):
    need(d > 0, "NONPOSITIVE_DENOMINATOR")
    return -((-n) // d)


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def packed(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
                       separators=(",", ":")) + "\n").encode("ascii")


def fraction_record(q):
    q = F(q)
    return [str(q.numerator), str(q.denominator)]


def utc():
    return datetime.now(timezone.utc).isoformat()


class Budget:
    def __init__(self, producer_sha, freeze_sha):
        self.started = time.monotonic()
        self.started_utc = utc()
        self.stage, self.detail = "starting", {}
        self.bytes_written = 0
        self.streams = []
        self.last_progress = 0.0
        self.producer_sha, self.freeze_sha = producer_sha, freeze_sha

    def check(self):
        need(time.monotonic() - self.started <= CAP_SECONDS, "ELAPSED_CAP_STOP")
        need(self.bytes_written <= CAP_BYTES - 65536, "OUTPUT_CAP_STOP")

    def atomic(self, name, value, *, emergency=False):
        raw = packed(value)
        if not emergency:
            self.bytes_written += len(raw)
            self.check()
        need(len(raw) <= 65536 or not emergency, "EMERGENCY_RECORD_TOO_LARGE")
        path = OUT / name
        tmp = OUT / (name + ".tmp")
        with tmp.open("wb") as f:
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)

    def progress(self, stage=None, *, force=False, **detail):
        if stage is not None:
            self.stage = stage
        if detail:
            self.detail = detail
        self.check()
        now = time.monotonic()
        if force or now - self.last_progress >= 2:
            # The atomic progress digest describes bytes already flushed to disk,
            # rather than an unflushed Python buffer. Force checkpoints are durable.
            for stream in self.streams:
                if not stream.handle.closed:
                    stream.handle.flush()
                    if force:
                        os.fsync(stream.handle.fileno())
            self.atomic("progress.json", {
                "schema": "RH_WEIL_RETAINED_SOURCE_PROGRESS_V1",
                "status": "RUNNING_SOURCE_ONLY", "stage": self.stage,
                "detail": self.detail, "elapsedSeconds": now-self.started,
                "startedUTC": self.started_utc, "observedUTC": utc(),
                "accountedBytes": self.bytes_written,
                "producerSHA256": self.producer_sha, "freezeSHA256": self.freeze_sha,
                "streams": [s.record() for s in self.streams],
                "mathIterations": 0, "fullQCertified": False,
            })
            self.last_progress = now


class Stream:
    def __init__(self, name, budget):
        self.name, self.budget = name, budget
        self.path = OUT / (name + ".part")
        self.handle = self.path.open("xb")
        self.digest, self.count, self.size = hashlib.sha256(), 0, 0
        self.complete = False
        budget.streams.append(self)

    def write(self, row):
        raw = packed(row)
        self.budget.bytes_written += len(raw)
        self.budget.check()
        self.handle.write(raw)
        self.digest.update(raw)
        self.count += 1
        self.size += len(raw)

    def close(self):
        if not self.handle.closed:
            self.handle.flush()
            os.fsync(self.handle.fileno())
            self.handle.close()

    def finish(self):
        self.close()
        target = OUT / self.name
        need(not target.exists(), "REFUSE_OUTPUT_OVERWRITE")
        os.replace(self.path, target)
        self.path, self.complete = target, True

    def record(self):
        return dict(file=self.path.name, bytes=self.size, rows=self.count,
                    sha256=self.digest.hexdigest(), complete=self.complete)


class Mesh:
    def __init__(self, bits=P):
        self.bits, self.unit = bits, 1 << bits
        self.zero = (0, 0)

    def rat(self, q, d=1):
        q = F(q, d) if isinstance(q, int) else F(q) / d
        n = q.numerator * self.unit
        return n // q.denominator, up(n, q.denominator)

    def add(self, a, b):
        return a[0]+b[0], a[1]+b[1]

    def sub(self, a, b):
        return a[0]-b[1], a[1]-b[0]

    def scale(self, a, n, d=1):
        q = F(n, d) if isinstance(n, int) else F(n) / d
        ends = a[0]*q.numerator, a[1]*q.numerator
        return min(ends)//q.denominator, up(max(ends), q.denominator)

    def mul(self, a, b):
        c = [x*y for x in a for y in b]
        return min(c)//self.unit, up(max(c), self.unit)

    def log_series(self, n, d):
        need(d > 0 and 0 <= 3*n <= d, "LOG_SERIES_DOMAIN")
        count = 1100
        power, total = self.rat(n, d), self.zero
        for k in range(count):
            total = self.add(total, self.scale(power, 2, 2*k+1))
            power = self.scale(power, n*n, d*d)
        # Positive 2atanh tail <3^(-2count)<2^(-3count).
        return total[0], total[1]+up(self.unit, 1 << (3*count))

    def log_rat(self, q, log2):
        q = F(q)
        need(q > 0, "LOG_POSITIVE_DOMAIN")
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
        return self.add(self.scale(log2, k), self.log_series(a-b, a+b))

    def quantize(self, iv, bits):
        need(iv[0] <= iv[1] and bits <= self.bits, "INTERVAL_ORDER")
        step = 1 << (self.bits-bits)
        lo, hi = iv[0]//step, up(iv[1], step)
        mid = lo+hi
        # Radius to FINAL stored midpoint, denominator2^(P+1).
        distance = max(abs(mid*step-2*iv[0]), abs(2*iv[1]-mid*step))
        return lo, hi, distance


def bernoulli_through(n, budget):
    # t/(exp(t)-1) convention: B1=-1/2, odd Bn=0 for n>1.
    values = [F(1)]
    for j in range(1, n+1):
        budget.check()
        if j > 1 and j % 2:
            values.append(F(0))
        else:
            values.append(-sum((comb(j+1,k)*values[k] for k in range(j)), F(0))/(j+1))
    need(values[1] == -F(1,2) and values[2] == F(1,6)
         and values[4] == -F(1,30), "BERNOULLI_CONVENTION")
    return values


def machin160():
    def arc(d):
        return sum((F((-1)**k, (2*k+1)*d**(2*k+1)) for k in range(160)), F(0))
    middle = 16*arc(5)-4*arc(239)
    radius = F(16,321*5**321)+F(4,321*239**321)
    need(middle > 3 and radius < F(1,1 << 646), "MACHIN160_BOUND")
    return middle, radius


def make_scalars(mesh, bernoulli, budget):
    budget.progress("scalars", force=True)
    log2 = mesh.log_series(1,3)
    ppi, rpi = machin160()
    pi = mesh.rat(ppi-rpi)[0], mesh.rat(ppi+rpi)[1]
    logpi = (mesh.log_rat(F(pi[0],mesh.unit), log2)[0],
             mesh.log_rat(F(pi[1],mesh.unit), log2)[1])
    h255 = sum((F(1,k) for k in range(1,256)), F(0))
    gamma = mesh.add(mesh.rat(h255+F(1,512)), mesh.scale(log2,-8))
    for k in range(1,257):
        gamma = mesh.add(gamma,mesh.rat(bernoulli[2*k]/(2*k*256**(2*k))))
        if k % 32 == 0:
            budget.check()
    # Binet for positive real x: the exact remainder of the digamma expansion
    # through B_512/(512*x^512) is bounded using |B_514({t})| <=4*514!/6^514,
    # then integral_0^infinity (x+t)^(-515)dt=x^-514/514. This yields
    # |remainder| <=4*513!/(6^514*x^514), without a complex-sector loss.
    remainder = F(4*factorial(513),6**514*256**514)
    need(remainder < F(1,1 << 1400), "REAL_BINET_REMAINDER")
    radius = up(remainder.numerator*mesh.unit,remainder.denominator)
    gamma = gamma[0]-radius,gamma[1]+radius
    contact = mesh.add(gamma,mesh.add(logpi,mesh.log_rat(2*L,log2)))
    contact_radius = F(contact[1]-contact[0],2*mesh.unit)
    need(contact_radius < F(1,1 << 600), "CONTACT_SCALAR_RADIUS")
    middle = F(contact[0]+contact[1],2*mesh.unit)
    return dict(log2=log2,pi=pi,ppi=ppi,rpi=rpi,gamma=gamma,
                contact=contact,contactCenter=middle,contactRadius=contact_radius,
                gammaRemainder=remainder)


def make_q_coefficients(bernoulli, budget):
    # Exactly the Bernoulli-polynomial formula in the consumed representation.
    powers = [F(1)]
    for _ in range(M+1):
        powers.append(powers[-1]*F(3,4))
    c = []
    for m in range(M+1):
        budget.progress("q-exact-coefficients", coefficient=m)
        n = m+1
        poly = sum((comb(n,k)*bernoulli[k]*powers[n-k] for k in range(n+1)),F(0))
        c.append(F(2**m,factorial(n))*poly)
    need(c[:3] == [F(1,4),-F(1,48),-F(1,32)], "Q_INITIAL_COEFFICIENTS")
    return [c[m]*(2*L)**m for m in range(M+1)]


def source_moments(raw):
    data = json.loads(raw)
    p = data["parameters"]
    need(data["schema"] == "RH_WEIL_9_8_SOURCE_MOMENTS_V1", "MOMENT_SCHEMA")
    need(p["L"] == "9/8" and p["omega"] == 256 and p["beta"] == "7/2"
         and p["outputBits"] == 1152 and p["qMax"] == 1023, "MOMENT_PARAMETERS")
    need(data["binetRemainderIncludedOnce"] is True, "MOMENT_BINET_ONCE")
    rows = data["rows"]
    need(len(rows) == 1024, "MOMENT_COMPLETE_SHAPE")
    centers = []
    for q,row in enumerate(rows):
        need(type(row["q"]) is int and row["q"] == q, "MOMENT_ORDER")
        lo,hi = int(row["lo"]),int(row["hi"])
        need(lo <= hi and hi-lo <= (1 << 55), "MOMENT_RADIUS")
        centers.append(F(lo+hi,1 << 1153))
    return centers


def band_coefficients(moments):
    result = [F(0)]*(D+1)
    for q,theta in enumerate(moments):
        m = 2*q
        result[m] = (-1)**q*theta*576**m/factorial(m)
    return result


def sinc_coefficients(ppi):
    result = [F(0)]*(D+1)
    for q in range(1024):
        m = 2*q
        result[m] = F((-1)**q*256*576**m,factorial(m+1))/ppi
    return result


def kernel_seeds(coefficients, mesh, budget, label, top=TOP):
    boundary = [mesh.zero]*(top+2)
    for m,coefficient in enumerate(coefficients):
        if not coefficient:
            continue
        budget.progress(label+"-seeds", kernelDegree=m)
        a,weight = mesh.rat(coefficient),mesh.rat(1,m+1)
        for j in range(min(m,top+1)+1):
            boundary[j] = mesh.add(boundary[j],mesh.mul(a,weight))
            if j < min(m,top+1):
                weight = mesh.scale(weight,m-j,m+j+2)
            if j % 128 == 0:
                budget.check()
    boundary = [mesh.scale(v,2 if j%2 == 0 else -2) for j,v in enumerate(boundary)]
    first,second = [mesh.zero]*(top+1),[mesh.zero]*top
    first[0] = mesh.scale(mesh.add(boundary[0],boundary[1]),2)
    # Parity branches are mathematical zeros, never a continuation of formulas.
    for j in range(2,top+1,2):
        first[j] = mesh.scale(mesh.sub(boundary[j+1],boundary[j-1]),2,2*j+1)
    for j in range(1,top,2):
        second[j] = mesh.scale(mesh.add(mesh.sub(first[j-1],first[j+1]),
                         mesh.scale(mesh.sub(boundary[j+1],boundary[j-1]),2)),1,2*j+1)
    return first,second


class Rectangle:
    def __init__(self, seeds, mesh, kind):
        self.first,self.second = seeds
        self.mesh,self.kind = mesh,kind
        self.previous2 = self.previous1 = None
        self.next_r = 0

    def row(self,r):
        need(r == self.next_r, "RECTANGLE_ROW_ORDER")
        bound = r+M if self.kind == "q" else D
        if r == 0:
            current = {j:(self.first[j] if j<=bound else self.mesh.zero)
                       for j in range(0,TOP+1,2)}
        elif r == 1:
            current = {j:(self.second[j] if j<=bound else self.mesh.zero)
                       for j in range(1,TOP,2)}
        else:
            current = {}
            for j in range(r,TOP-r+1,2):
                if j > bound:
                    current[j] = self.mesh.zero
                else:
                    current[j] = self.mesh.sub(self.previous2[j],self.mesh.scale(
                        self.mesh.sub(self.previous1[j+1],self.previous1[j-1]),2*r-1,2*j+1))
        self.previous2,self.previous1 = self.previous1,current
        self.next_r += 1
        return current


def weighted_square(midpoints, column):
    return sum(mid*mid*(2*i+1)*(2*column+1) for i,mid in enumerate(midpoints))


def raw_squared(numerator, center_bits):
    return F(16*numerator,81*(1 << (2*(center_bits+1))))


def make_h(sinc, mesh, budget):
    budget.progress("old-h-global-polynomials", force=True)
    first,second = kernel_seeds(sinc,mesh,budget,"sinc")
    arrays = [[0]*(D+1) for _ in range(2)]
    source_dist = [0,0]
    stored_width = [0,0]
    hstream = Stream("h-columns.jsonl",budget)
    for s,row in enumerate((first,second)):
        for i in range(s,D+1,2):
            value = mesh.scale(row[i],-L*L)
            if i == s:
                value = mesh.add(value,mesh.rat((1-DELTA)*2*L/F(2*s+1)))
            lo,hi,distance = mesh.quantize(value,HB)
            arrays[s][i] = lo+hi
            weight = (2*i+1)*(2*s+1)
            source_dist[s] += distance*distance*weight
            stored_width[s] += (hi-lo)**2*weight
            hstream.write([s,i,str(lo),str(hi)])
        budget.progress("old-h-global-polynomials", column=s, force=True)
    need(hstream.count == D+1, "H_PARITY_FULL_SHAPE")
    hstream.finish()
    records = []
    for s in range(2):
        actual_round = F(16*source_dist[s],81*(1 << (2*P+2)))
        stored_round = raw_squared(stored_width[s],HB)
        need(actual_round <= F(1,1 << 1040) and stored_round <= F(1,1 << 1040),
             "H_FULL_NATIVE_ROUNDING_HS")
        norm2 = raw_squared(weighted_square(arrays[s],s),HB)
        old_cap = F(1,29) if s == 0 else F(3,50)
        need(norm2 <= (old_cap+F(1,1 << 512))**2,"H_FULL_POLYNOMIAL_NORM")
        records.append(dict(column=s,normSquared=fraction_record(norm2),
            roundingSquared=fraction_record(actual_round),
            serializedRadiusSquared=fraction_record(stored_round),
            distanceWeightedNumerator=str(source_dist[s]),
            widthWeightedNumerator=str(stored_width[s]),
            sourceColumnErrorPower=-512,originalNormCap=fraction_record(old_cap)))
    return arrays,records


def harmonic_tables(n):
    h=[F(0)]
    for k in range(1,n+1):
        h.append(h[-1]+F(1,k))
    return h


def log_gram_raw(i,j,mesh,log2,harmonic):
    need(i%2 == j%2,"LOG_GRAM_PARITY")
    if i != j:
        return mesh.rat(F(-4,abs(i-j)*(i+j+1)))
    bracket = mesh.sub(log2,mesh.rat(F(1,2*j+1)+2*(harmonic[2*j]-harmonic[j])))
    return mesh.scale(bracket,4,2*j+1)


def make_v(qseeds,bseeds,hcenters,scalars,mesh,budget):
    qrectangle,brectangle = Rectangle(qseeds,mesh,"q"),Rectangle(bseeds,mesh,"band")
    harmonic = harmonic_tables(2*N)
    head = {}
    width_sum = distance_sum = 0
    norm_numerators,complement_numerators = [0]*N,[0]*N
    stream = Stream("finite-columns.jsonl",budget)
    c = scalars["contactCenter"]
    for j in range(N):
        budget.progress("finite-native-columns",column=j,force=True)
        qr,br = qrectangle.row(j),brectangle.row(j)
        for i in range(j%2,D+1,2):
            if i < j:
                lo,hi,distance = head[(i,j)]
            else:
                value = mesh.scale(mesh.add(qr[i],br[i]),-L*L)
                value = mesh.sub(value,mesh.scale(log_gram_raw(i,j,mesh,scalars["log2"],harmonic),L/2))
                u_num = 36*sum(hcenters[s][i]*hcenters[s][j] for s in range(2))
                value = mesh.sub(value,mesh.rat(u_num,1 << (2*HB+2)))
                if i == j:
                    value = mesh.add(value,mesh.rat((harmonic[j]-c-F(7,2)-TAU)*2*L/F(2*j+1)))
                lo,hi,distance = mesh.quantize(value,OB)
                if i < N:
                    head[(j,i)] = lo,hi,distance
            mid,weight = lo+hi,(2*i+1)*(2*j+1)
            width_sum += (hi-lo)**2*weight
            distance_sum += distance*distance*weight
            norm_numerators[j] += mid*mid*weight
            if i >= N:
                complement_numerators[j] += mid*mid*weight
            stream.write([j,i,str(lo),str(hi)])
        # actual shape/scale/HS check includes copied symmetric entries as well.
        budget.check()
    need(stream.count == 458528 and len(head) == 50400,"V_FULL_RECTANGLE_SHAPE")
    arithmetic = F(16*distance_sum,81*(1 << (2*P+2)))
    stored = raw_squared(width_sum,OB)
    need(arithmetic <= F(1,1 << 440) and stored <= F(1,1 << 440),
         "V_FULL_NATIVE_ARITHMETIC_HS")
    stream.finish()
    return dict(distanceWeightedNumerator=str(distance_sum),
                widthWeightedNumerator=str(width_sum),
                arithmeticHSSquared=fraction_record(arithmetic),
                serializedRadiusHSSquared=fraction_record(stored),
                fullParityRows=stream.count,uniqueHeadEntries=len(head),
                fullHeadEntries=100352,headConstruction="single_upper_triangle_then_exact_copy"), norm_numerators,complement_numerators


def norm_records(full_numerators,complement_numerators,scalars,mesh,budget):
    budget.progress("symbolic-tail-and-complement",force=True)
    # Prefixes need only about1250 terms; exact fractions avoid cancellation loss.
    even_prefix,odd_prefix = [F(0)],[F(0)]
    for k in range(1,D+N+2):
        even_prefix.append(even_prefix[-1]+F(1,k*k))
        odd_prefix.append(odd_prefix[-1]+F(1,(2*k-1)**2))
        if k % 64 == 0:
            budget.check()
    pi2 = mesh.mul(scalars["pi"],scalars["pi"])
    total_comp,total_full = mesh.zero,mesh.zero
    stream = Stream("column-norms.jsonl",budget)
    for j in range(N):
        i0 = D+1 if (D+1)%2 == j%2 else D+2
        k = (i0-j)//2
        tail = mesh.sub(mesh.rat(odd_prefix[k+j]-even_prefix[k-1]/4),mesh.scale(pi2,1,12))
        need(tail[0] >= 0,"SYMBOLIC_TAIL_DIAGONAL_NONNEGATIVE")
        full = mesh.add(mesh.rat(raw_squared(full_numerators[j],OB)),tail)
        complement = mesh.add(mesh.rat(raw_squared(complement_numerators[j],OB)),tail)
        # The common symbolic tail cancels exactly. Compare the exact finite
        # center contributions, not overlapping intervals for their separate sums.
        need(full_numerators[j] >= complement_numerators[j],"COLUMN_NORM_CONSISTENCY")
        total_full,total_comp = mesh.add(total_full,full),mesh.add(total_comp,complement)
        fl,fh,_ = mesh.quantize(full,OB)
        cl,ch,_ = mesh.quantize(complement,OB)
        tl,th,_ = mesh.quantize(tail,OB)
        stream.write(dict(column=j,nativeModelNormSquared=[str(fl),str(fh)],
            nativeModelComplementNormSquared=[str(cl),str(ch)],
            nativeInfiniteTailNormSquared=[str(tl),str(th)],
            squaredNormOutputBits=OB,firstInfiniteDegree=i0,K=k,
            actualColumnL2ErrorPower=-203))
        budget.progress("symbolic-tail-and-complement",column=j)
    need(stream.count == N,"COLUMN_NORM_FULL_SHAPE")
    stream.finish()
    def bracket(iv):
        lo,hi,_ = mesh.quantize(iv,OB)
        return [str(lo),str(hi)]
    return dict(nativeModelHSSquared=bracket(total_full),
                nativeModelComplementHSSquared=bracket(total_comp),
                squaredNormOutputBits=OB,
                actualComplementErrorHSBoundPower=-198,
                actualComplementInterpretation="norm differs by <=2^-198 from represented complement; finite rows448..2046 plus exact symbolic infinite tail")


def small_regressions():
    # Exact scalar/basis tests only, no actual448 columns or numerical pilots.
    def legendre(n):
        p0,p1 = [F(1)],[F(0),F(1)]
        if n == 0:
            return p0
        for k in range(1,n):
            new=[F(0)]*(k+2)
            for i,c in enumerate(p1):
                new[i+1] += F(2*k+1,k+1)*c
            for i,c in enumerate(p0):
                new[i] -= F(k,k+1)*c
            p0,p1 = p1,new
        return p1
    def direct(m,r,j):
        # Shifted Legendre coefficients on[0,1]; split the two triangles exactly.
        a=[(-1)**(r-k)*comb(r,k)*comb(r+k,k) for k in range(r+1)]
        b=[(-1)**(j-k)*comb(j,k)*comb(j+k,k) for k in range(j+1)]
        return 4*2**m*sum((F(x*y,aexp+bexp+m+2)*(
            F(factorial(bexp)*factorial(m),factorial(bexp+m+1))+
            F(factorial(aexp)*factorial(m),factorial(aexp+m+1)))
            for aexp,x in enumerate(a) for bexp,y in enumerate(b)),F(0))
    for m in range(5):
        top=10
        boundary=[]
        for j in range(top+2):
            v=(F(2*(-1)**j*2**m*factorial(m)**2,
                 factorial(m-j)*factorial(m+j+1)) if j<=m else F(0))
            boundary.append(v)
        first,second=[F(0)]*(top+1),[F(0)]*top
        first[0]=2*(boundary[0]+boundary[1])
        for j in range(2,top+1,2):
            first[j]=2*(boundary[j+1]-boundary[j-1])/(2*j+1)
        for j in range(1,top,2):
            second[j]=(first[j-1]-first[j+1]+2*(boundary[j+1]-boundary[j-1]))/(2*j+1)
        prev2=prev1=None
        for r in range(5):
            if r == 0:
                row={j:first[j] for j in range(0,top+1,2)}
            elif r == 1:
                row={j:second[j] for j in range(1,top,2)}
            else:
                row={j:prev2[j]-F(2*r-1,2*j+1)*(prev1[j+1]-prev1[j-1])
                     for j in range(r,top-r+1,2)}
            for j in range(r,5,2):
                need(row[j] == direct(m,r,j),"SMALL_RECTANGULAR_KERNEL_REGRESSION")
            prev2,prev1=prev1,row
    harmonic=harmonic_tables(12)
    for i in range(5):
        for j in range(i,5):
            direct_log=[F(0),F(0)] # coefficient of log2, rational part
            for a,x in enumerate(legendre(i)):
                for b,y in enumerate(legendre(j)):
                    degree=a+b
                    if degree%2:
                        continue
                    r=degree//2
                    direct_log[0] += x*y*F(4,2*r+1)
                    direct_log[1] += x*y*F(2,2*r+1)*(-2*harmonic[2*r+2]+harmonic[r+1])
            if (i+j)%2:
                expected=[F(0),F(0)]
            elif i != j:
                expected=[F(0),-F(4,(j-i)*(i+j+1))]
            else:
                expected=[F(4,2*j+1),-F(4,2*j+1)*(F(1,2*j+1)+2*(harmonic[2*j]-harmonic[j]))]
            need(direct_log == expected,"SMALL_LOG_GRAM_REGRESSION")
    for i in range(8,12):
        for j in range(5):
            need(F((2*i+1)*(2*j+1),(i-j)**2*(i+j+1)**2)
                 == F(1,(i-j)**2)-F(1,(i+j+1)**2),"TAIL_TELESCOPING_IDENTITY")
    return dict(status="EXACT_SMALL_REGRESSIONS_PASS",maxLegendreDegree=4,
                kernelPowers=list(range(5)),endpointTailSquareIdentity=True,
                actual448ArraysComputed=False)


def analytic_ledger(scalars):
    eps_q=F(4608)*F(3,4)**577
    eps_band=2*L*(F(914*576**2048,factorial(2048))+F(1,1 << 1098)*F(68,25)**576)
    pi_lower=F(scalars["pi"][0],1 << P)
    eps_sinc=F(576**2049,factorial(2049))/pi_lower
    need(eps_q < F(1,1 << 227),"GLOBAL_Q_REMAINDER")
    need(eps_band < F(1,1 << 204),"GLOBAL_BAND_REMAINDER")
    need(eps_sinc < F(1,1 << 513),"GLOBAL_SINC_REMAINDER")
    eh=F(1,1 << 513)+F(1,1 << 646)+F(1,1 << 520)
    need(eh < F(1,1 << 512),"H_GLOBAL_SOURCE_PLUS_ROUNDING")
    u=F(1,1 << 512)*(F(162,29)+F(162,50)+108*F(1,1 << 512))
    need(u < 9*F(1,1 << 512),"U_GLOBAL_RANK_TWO_ERROR")
    ev=F(1,1 << 204)+F(1,1 << 227)+9*F(1,1 << 512)+F(1,1 << 600)+F(1,1 << 220)
    need(ev < F(1,1 << 203) and N < (1 << 10),"V_OP_HS_TARGET")
    return dict(qOperatorErrorPower=-227,bandOperatorErrorPower=-204,
        hGlobalErrorPower=-512,hFullPolynomialRoundingPower=-520,
        oldRankTwoError="9*2^-512",contactScalarErrorPower=-600,
        finiteAssemblyArithmeticHSBoundPower=-220,
        nativeVOperatorErrorPower=-203,nativeVHSErrorPower=-198,
        nativeGOperatorErrorPower=-203,
        exactQBound=fraction_record(eps_q),exactBandBound=fraction_record(eps_band),
        exactSincBound=fraction_record(eps_sinc),
        errorsAreGlobalOriginalDu=True,momentBinetChargedOnce=True,
        laterInversionOrWholeSchurErrorPaid=False)


def verify_inputs():
    inventory={}
    moment_raw=None
    for name,expected in INPUTS.items():
        path=(ROOT/name).resolve()
        need(path.is_relative_to(ROOT),"INPUT_PATH_ESCAPE")
        raw=path.read_bytes()
        need(sha_bytes(raw) == expected,"INPUT_HASH_MISMATCH: "+name)
        inventory[name]=dict(bytes=len(raw),sha256=expected)
        if name.endswith("/moments.json"):
            moment_raw=raw
    need(moment_raw is not None,"MOMENT_INPUT_MISSING")
    return inventory,moment_raw


def validate_freeze(path):
    path=path.resolve()
    need(not path.is_relative_to(OUT),"FREEZE_MUST_BE_OUTSIDE_OUTPUT")
    raw=path.read_bytes()
    need(len(raw) <= 65536,"FREEZE_SIZE")
    obj=json.loads(raw)
    producer_sha=sha_bytes(SELF.read_bytes())
    need(obj.get("schema") == "RH_WEIL_RETAINED_SOURCE_FREEZE_V1"
         and obj.get("authorization") == "ROOT_EXPLICIT_FREEZE_AND_RUN"
         and obj.get("runtimeGoalCreatedAt") == 1793085111,"NO_ROOT_FREEZE")
    need(obj.get("parameters") == PARAMETERS,"FREEZE_PARAMETER_MISMATCH")
    need(obj.get("producerSHA256") == producer_sha,"FREEZE_PRODUCER_MISMATCH")
    need(obj.get("inputs") == INPUTS,"FREEZE_INPUT_BINDING_MISMATCH")
    return producer_sha,sha_bytes(raw)


def run(freeze_path):
    producer_sha,freeze_sha=validate_freeze(freeze_path)
    inventory,moment_raw=verify_inputs()
    need(OUT.is_relative_to(ROOT/"literature/local"),"OUTPUT_PATH_ESCAPE")
    need(not OUT.exists() or not any(OUT.iterdir()),"ONE_ATTEMPT_OUTPUT_ALREADY_EXISTS")
    OUT.mkdir(parents=True,exist_ok=True)
    budget=Budget(producer_sha,freeze_sha)
    result=None
    try:
        budget.progress("small-symbolic-regressions",force=True)
        regressions=small_regressions()
        budget.progress("exact-bernoulli",force=True)
        bernoulli=bernoulli_through(M+1,budget)
        mesh=Mesh()
        scalars=make_scalars(mesh,bernoulli,budget)
        ledger=analytic_ledger(scalars)
        moments=source_moments(moment_raw)
        qcoeff=make_q_coefficients(bernoulli,budget)
        hcenters,hrecords=make_h(sinc_coefficients(scalars["ppi"]),mesh,budget)
        qseeds=kernel_seeds(qcoeff,mesh,budget,"q")
        bseeds=kernel_seeds(band_coefficients(moments),mesh,budget,"band")
        arithmetic,full,complement=make_v(qseeds,bseeds,hcenters,scalars,mesh,budget)
        norms=norm_records(full,complement,scalars,mesh,budget)
        budget.progress("final-input-recheck",force=True)
        final_inventory,_=verify_inputs()
        need(final_inventory == inventory and sha_bytes(SELF.read_bytes()) == producer_sha,
             "INPUT_CHANGED_DURING_PRODUCTION")
        need(sha_bytes(freeze_path.resolve().read_bytes()) == freeze_sha,"FREEZE_CHANGED_DURING_PRODUCTION")
        result=dict(schema="RH_WEIL_RETAINED_SOURCE_PACKET_V1",
            status="SOURCE_PACKET_PRODUCED_PENDING_INDEPENDENT_REPLAY",
            runtimeGoalCreatedAt=1793085111,parameters=PARAMETERS,
            startedUTC=budget.started_utc,endedUTC=utc(),
            elapsedSeconds=time.monotonic()-budget.started,
            producerSHA256=producer_sha,freezeSHA256=freeze_sha,inputs=inventory,
            streams=[s.record() for s in budget.streams],regressions=regressions,
            object="V=R E448; R=Ttail-tau I-Uold; G_R=E*V, not V*V",
            norm="original L2((-9/8,9/8),du)",rawGram="g_j=9/[4(2j+1)]",
            finiteColumns=dict(file="finite-columns.jsonl",row="[column,degree,lo,hi]",
                intervalDenominatorPower=OB,midpointDenominatorPower=OB+1,
                canonicalOrder="column-major; degrees ascending of same parity; opposite parity exact0",
                completeParityRows=458528),
            oldHColumns=dict(file="h-columns.jsonl",intervalDenominatorPower=HB,
                midpointDenominatorPower=HB+1,completeParityRows=2047,
                rawObject="t_is=<p_i,(I-Bsinc_poly-delta I)p_s>",UrawCoefficient=36,
                fullPolynomialChecks=hrecords),
            symbolicInfiniteTail=dict(firstDegree=D+1,parity="same input/output parity only",
                nativeCoefficient="sqrt((2i+1)(2j+1))/((i-j)(i+j+1))",
                rawExpansionCoefficient="(2i+1)/((i-j)(i+j+1))",
                nativeDiagonalTailSum="-pi^2/12-H2_(K-1)/4+sum_(r=0)^(K+j-1)(2r+1)^-2",
                endpointLogDiscarded=False),
            Ghat=dict(source="first448 rows of SAME finite-columns stream",
                symmetricHeadExactlyCopied=True,modelConsistencyExact=True),
            scalarIntervals=dict(workingBits=P,log2=list(map(str,scalars["log2"])),
                pi=list(map(str,scalars["pi"])),gamma=list(map(str,scalars["gamma"])),
                contact=list(map(str,scalars["contact"])),
                contactCenter=fraction_record(scalars["contactCenter"]),
                contactRadius=fraction_record(scalars["contactRadius"]),
                gammaRemainder=fraction_record(scalars["gammaRemainder"]),
                sincPiExact=fraction_record(scalars["ppi"])),
            arithmetic=arithmetic,errorLedger=ledger,complement=norms,
            fullQCertified=False,RHCertified=False,mathIterations=0,
            signedMargin=None,wholeSchurMargin=None,
            scope="actual source values only; independent replay/root consumption/whole signed comparison still required")
        budget.check()
        budget.atomic("result.json",result)
        budget.stage="complete-pending-replay"
        budget.progress(force=True)
        return result
    except BaseException as error:
        for stream in budget.streams:
            stream.close()
        failure=dict(schema="RH_WEIL_RETAINED_SOURCE_STOP_V1",status="STOPPED_NO_RETRY",
            runtimeGoalCreatedAt=1793085111,parameters=PARAMETERS,
            startedUTC=budget.started_utc,endedUTC=utc(),
            elapsedSeconds=time.monotonic()-budget.started,
            stage=budget.stage,detail=budget.detail,errorType=type(error).__name__,
            reason=str(error)[:1000],producerSHA256=producer_sha,freezeSHA256=freeze_sha,
            streams=[s.record() for s in budget.streams],mathIterations=0,
            fullQCertified=False,RHCertified=False,pendingProcesses=[],
            nextAction="root inspect exact stop; no retry/parameter/precision/source successor authorized")
        budget.atomic("result.json",failure,emergency=True)
        budget.atomic("progress.json",failure,emergency=True)
        raise


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze-file",type=Path,required=True)
    args=parser.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    result=run(args.freeze_file)
    print(json.dumps({"status":result["status"],"elapsedSeconds":result["elapsedSeconds"],
                      "result":str(OUT/"result.json")},ensure_ascii=False))


if __name__ == "__main__":
    main()

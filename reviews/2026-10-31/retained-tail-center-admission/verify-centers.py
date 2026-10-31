"""ONE standalone final-center/full-H certificate; NO RUN until root freezes.

Preparation permits AST/static inspection ONLY: do not import this module or
evaluate its scientific functions. Old source/producer/checker/STOP stay read-only.
Reviewed independent factorial/directed primitives are adapted from the frozen
old checker; no producer/checker/science module is imported or invoked.

The same immutable centers define the target. Independent true enclosures pay
MAX endpoint distance to FINAL centers, not nesting/halfwidth/internal counters.
Independent contact-to-same-center/log2/pi/gamma, both pi,p_pi>3 and separate
Taylor/normalization fees are mandatory. SAME h640 centers enter W. New model
norm brackets are authoritative; old scalar/coefficient/norm box truth is NOT.

Freeze JSON schema RH_WEIL_FINAL_CENTER_FREEZE_V1 must bind authorization
ROOT_EXPLICIT_FREEZE_AND_VERIFY_CENTERS, runtimeGoalCreatedAt1793085111,
verifierSHA256, parameters=CERT_PARAMETERS and pins=ALL_PINS. Any extra root
review fields are allowed. Freeze lives outside the new output directory.
ONE1800s/4MiB attempt, no retry/recenter/parameter/route/precision fallback.
Only new progress/result/model-norms files may be written. PASS is center-only
source verification pending root, never old interval PASS, wholeQ or RH.
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
SRC = ROOT / "literature/local/2026-10-31-retained-tail-source/run-01"
OUT = ROOT / "literature/local/2026-10-31-retained-tail-center-certificate/run-01"
BITS, OUT_BITS, H_BITS = 3072, 256, 640
N, D, QDEG, TOP = 448, 2046, 576, 2493
CAP_SECONDS, INPUT_CAP_BYTES, CAP_BYTES = 1800, 160 * (1 << 20), 4 * (1 << 20)
L = Fraction(9, 8)
DELTA, TAU = Fraction(1, 1 << 49158), Fraction(1, 1 << 49162)
PARAMETERS = dict(L="9/8", omega=256, eta=1, N=N, D=D, qDegree=QDEG,
    qCoefficients=577, bandTerms=1024, sincTerms=1024, workingBits=BITS,
    outputBits=OUT_BITS, hOutputBits=H_BITS, deltaPower=49158,
    tauPower=49162, sourceCapSeconds=CAP_SECONDS, sourceCapBytes=INPUT_CAP_BYTES)
CERT_PARAMETERS = dict(sourceParameters=PARAMETERS,workingBits=BITS,
    criterion="MAX_DISTANCE_TO_SAME_FINAL_CENTERS",certificateCapSeconds=CAP_SECONDS,
    certificateCapBytes=CAP_BYTES,authoritativeNormBits=OUT_BITS,
    oldBoxTruthConsumed=False,oldProducerInternalDistanceConsumed=False)
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
OLD = "reviews/2026-10-31/retained-tail-source/"
NEW = "reviews/2026-10-31/retained-tail-center-admission/"
SOURCE_PREFIX = "literature/local/2026-10-31-retained-tail-source/run-01/"
FIXED_PINS = {
    OLD+"produce-source.py":"05f395038a4e2a75027b69996f990e1978d6e09c799dfbd43fd41fa1add8d45b",
    OLD+"check-source.py":"1d36d353cdeaccb9cfa63529bebb08d6a5f09cdf7e2b280b53f287d64ba54753",
    OLD+"producer-freeze.json":"833f360a8f1edde9c69a7287fc1f921c1585aa590cc1904ee481b6c4c9013975",
    OLD+"replay-freeze.json":"910c09a29f0b6142f22ae8aa8b1b7e2678b050d731dca0a68ebd0e32f3aa73e6",
    SOURCE_PREFIX+"result.json":"a9fb5f5150bc17f56ebc3bd9e981ce0ec421c8efdf5612554ccc3a751eff6de5",
    SOURCE_PREFIX+"replay-result.json":"5155ba3e55e0ce06d01136c15677f213a8734303b630227f04fb3f1d02d9303e",
    SOURCE_PREFIX+"h-columns.jsonl":"37f2c0410beb1b1c43b9f8d2df24d72fce3170b5f359d089c198742f1eee4e74",
    SOURCE_PREFIX+"finite-columns.jsonl":"d841d307d2b22367570e594c1bc9e3b64c8a4ffef88691382acf5d6fbeeaf080",
    SOURCE_PREFIX+"column-norms.jsonl":"0506bf585a562d2585cbf8aa0b2ca3e8106ab5816f7f09db84245a235525b1cf",
    NEW+"native-center-error-proof.md":"bca1ff76f9ef94e25a10fdbc6597641b682ae7174cc0e4c952e4edbb39ce188b",
    NEW+"acceptance-obligation-audit.md":"bbe3e1d05230c200ebf969cc76a5e9d5ae39c056948bde3f2925d807d1ba20ef",
    NEW+"scalar-denominator-clarification.md":"3ae3f5fb8bbf9215715d92cfce6ad4418b98969b97e6d7f6580677d9f5287126",
    NEW+"center-admission-fresh.md":"2601e309b40c418f3db5181a39f5d9ac0d88576e20e53c0a82aaa8b8ce262249",
    NEW+"root-comparison.md":"19bc010654b0538c87a1510a68a83aeda7e9b793288d7cce41db96a0ac8142e1",
    NEW+"center-certificate-admission.md":"603a0d3702eb9825495b02cb8cae696b9630ea9bebdab1fa9fec42a63f40fdf2",
    NEW+"proof-root-closure.json":"7a381d0037f27c82ec3372537172ad29707dc16dfd6d2cea48185689e9624576",
}
ALL_PINS = dict(INPUTS,**FIXED_PINS)
STREAM_SPECS = [
    ("h-columns.jsonl",2047,233458),
    ("finite-columns.jsonl",458528,73598411),
    ("column-norms.jsonl",448,303201),
]


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


class CertificateBudget:
    def __init__(self, bindings):
        self.started = time.monotonic()
        self.started_utc = datetime.now(timezone.utc).isoformat()
        self.stage, self.detail = "preflight", {}
        self.last_write = 0.0
        self.bindings = bindings
        self.context = {}
        self.norm_writer = None
        self.last_size_check = 0.0

    def check(self):
        now=time.monotonic()
        require(now-self.started <= CAP_SECONDS, "CENTER_CERTIFICATE_ELAPSED_CAP_STOP")
        if now-self.last_size_check >= 1:
            require(sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
                    <= CAP_BYTES-131072,"CENTER_CERTIFICATE_OUTPUT_CAP_STOP")
            self.last_size_check=now

    def atomic(self, name, obj, *, emergency=False):
        raw = (json.dumps(obj, ensure_ascii=True, sort_keys=True,
                          separators=(",", ":"))+"\n").encode("ascii")
        require(len(raw) < (65536 if emergency else 1024*1024), "CERTIFICATE_RECORD_TOO_LARGE")
        if not emergency:
            self.check()
            require(sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())+len(raw)
                    <=CAP_BYTES-131072,"CENTER_CERTIFICATE_OUTPUT_CAP_STOP")
        p = OUT / name
        tmp = OUT / (name+".tmp")
        with tmp.open("wb") as f:
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, p)

    def progress(self, stage=None, force=False, **detail):
        if stage is not None:
            if stage != self.stage:
                self.context={}
            self.stage = stage
        if detail:
            self.detail = detail
        self.check()
        if force or time.monotonic()-self.last_write >= 3:
            if self.norm_writer is not None and not self.norm_writer.handle.closed:
                self.norm_writer.handle.flush()
                if force:
                    os.fsync(self.norm_writer.handle.fileno())
            self.atomic("progress.json", dict(
                schema="RH_WEIL_FINAL_CENTER_PROGRESS_V1",
                status="RUNNING_FINAL_CENTER_CERTIFICATE", stage=self.stage,
                detail=self.detail, startedUTC=self.started_utc,
                elapsedSeconds=time.monotonic()-self.started,
                context=self.context,bindings=self.bindings,
                mathIterations=0,fullQCertified=False))
            self.last_write = time.monotonic()


class NormWriter:
    def __init__(self,budget):
        self.path=OUT/"model-norms.jsonl.part"
        self.handle=self.path.open("xb")
        self.sha,self.size,self.count=hashlib.sha256(),0,0
        self.budget=budget
        budget.norm_writer=self

    def write(self,row):
        raw=(json.dumps(row,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n").encode("ascii")
        self.budget.check()
        other_size=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file() and p!=self.path)
        require(other_size+self.size+len(raw)<=CAP_BYTES-131072,"NORM_OUTPUT_CAP_STOP")
        self.handle.write(raw)
        self.sha.update(raw)
        self.size+=len(raw)
        self.count+=1

    def close(self):
        if not self.handle.closed:
            self.handle.flush()
            os.fsync(self.handle.fileno())
            self.handle.close()

    def finish(self):
        self.close()
        target=OUT/"model-norms.jsonl"
        require(not target.exists(),"NORM_OUTPUT_EXISTS")
        os.replace(self.path,target)
        self.path=target

    def record(self):
        return dict(file=self.path.name,rows=self.count,bytes=self.size,sha256=self.sha.hexdigest(),
                    complete=self.path.name=="model-norms.jsonl")


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


def final_distance(iv,pair,stored_bits,mesh):
    require(iv[0]<=iv[1],"INDEPENDENT_TRUE_ENCLOSURE_ORDER")
    step=1 << (mesh.bits-stored_bits)
    center_twice=sum(pair)*step
    return max(abs(2*iv[0]-center_twice),abs(2*iv[1]-center_twice))


def error_context(budget,column,degree,pair,iv,bits,distance,partial,weight):
    where={k:budget.context[k] for k in ("stream","rowPosition","byteOffset") if k in budget.context}
    budget.context=dict(**where,column=column,degree=degree,
        enclosureStatus="AVAILABLE",prefixStage="INCLUDING_CURRENT_ENTRY",
        storedCenterNumerator=sum(pair),storedCenterDenominatorPower=bits+1,
        independentEndpoints=[iv[0],iv[1]],independentEndpointBits=BITS,
        maxDistanceNumerator=distance,maxDistanceDenominatorPower=BITS+1,
        nativeSquaredWeightNumerator=16*weight,nativeSquaredWeightDenominator=81,
        partialWeightedDistanceNumerator=partial,
        nativeSquaredSumNumerator=16*partial,
        nativeSquaredSumDenominator="81*2^"+str(2*BITS+2))


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
    contact = rational(sc["contactCenter"])
    radius=max(abs(Fraction(contact_iv[0],mesh.unit)-contact),
               abs(Fraction(contact_iv[1],mesh.unit)-contact))
    budget.context=dict(object="true-contact-to-SAME-stored-center",
        storedCenter=fraction_record(contact),independentEndpoints=list(map(str,contact_iv)),
        independentEndpointBits=BITS,maxDistance=fraction_record(radius))
    require(radius < Fraction(1,1 << 600),"TRUE_CONTACT_TO_FINAL_CENTER_ERROR")
    ppi = direct_machin(160)
    require(ppi == rational(sc["sincPiExact"]) and ppi > 3, "EXACT_SINC_PI")
    require(pi_iv[0]>3*mesh.unit,"TRUE_PI_COMMON_LOWER_THREE")
    machin_radius=Fraction(16,321*5**321)+Fraction(4,321*239**321)
    require(machin_radius<Fraction(1,1 << 646),"EXACT_MACHIN160_REMAINDER")
    # Independent true-pi enclosure provides a separate check on this SAME ppi.
    independent_ppi_error=max(abs(Fraction(pi_iv[0],mesh.unit)-ppi),
                              abs(Fraction(pi_iv[1],mesh.unit)-ppi))
    require(independent_ppi_error<Fraction(1,1 << 646),"TRUE_PI_TO_EXACT_PPI")
    return dict(log2=log2,pi=pi_iv,gamma=gamma_iv,contactInterval=contact_iv,
        contact=contact,contactRadius=radius,ppi=ppi,machinRadius=machin_radius,
        gammaRemainder=remainder,independentPpiError=independent_ppi_error)


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
        budget.context=dict(operation="factorial-table",source=label,factorialIndex=k,
            independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_YET_AVAILABLE")
        fs.append(fs[-1]*k)
    first, second = [(0,0)]*(TOP+1), [(0,0)]*TOP
    summands = 0
    for m, a in enumerate(coefficients):
        if not a:
            continue
        budget.progress(label+"-factorial-seeds",kernelDegree=m,summands=summands)
        budget.context=dict(operation="factorial-seeds",source=label,kernelDegree=m,
            seedRow=None,seedIndex=None,seedParity=None,
            independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_YET_AVAILABLE")
        numerator = 8*a.numerator*fs[m]*fs[m+1]
        denominator = a.denominator
        for j in range(0,min(m+1,TOP)+1,2):
            budget.context=dict(operation="factorial-seeds",source=label,kernelDegree=m,
                seedRow=0,seedIndex=j,seedParity=0,summands=summands,
                independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_YET_AVAILABLE")
            term = mesh.ratio(numerator,denominator*fs[m-j+1]*fs[m+j+2])
            first[j] = mesh.plus(first[j],term)
            summands += 1
            if j%128==0:
                budget.check()
        for j in range(1,min(m+2,TOP-1)+1,2):
            budget.context=dict(operation="factorial-seeds",source=label,kernelDegree=m,
                seedRow=1,seedIndex=j,seedParity=1,summands=summands,
                independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_YET_AVAILABLE")
            n = -numerator*(m-j+1)
            term = mesh.ratio(n,denominator*fs[m-j+2]*fs[m+j+1]*(m+j+3))
            second[j] = mesh.plus(second[j],term)
            summands += 1
            if j%128==1:
                budget.check()
        budget.progress(label+"-factorial-seeds", kernelDegree=m, summands=summands)
    return first,second


def recurrence_rows(seeds, mesh, kind, budget):
    old2, old1 = None,None
    for r in range(N):
        budget.context=dict(operation="source-rectangle-recurrence",source=kind,sourceRow=r,
            sourceParity=r%2,seedIndex=None,independentEndpoints=None,
            storedCenterNumerator=None,enclosureStatus="NOT_YET_AVAILABLE")
        last = TOP-r
        bound = r+QDEG if kind == "q" else D
        row = {}
        for j in range(r,last+1,2):
            budget.context["seedIndex"]=j
            if j > bound:
                row[j] = (0,0)
            elif r < 2:
                row[j] = seeds[r][j]
            else:
                diff = mesh.minus(old1[j+1],old1[j-1])
                row[j] = mesh.minus(old2[j],mesh.times_ratio(diff,2*r-1,2*j+1))
        yield row
        old2,old1 = old1,row
        budget.context=dict(operation="source-rectangle-recurrence",source=kind,sourceRow=r,
            sourceParity=r%2,nextSourceRow=r+1,phase="AFTER_YIELD_BEFORE_NEXT_SOURCE_ROW",
            independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_AVAILABLE_FOR_THIS_CHECK")
        budget.check()


class StreamReader:
    def __init__(self, record, expected_file, budget):
        budget.context=dict(operation="open-immutable-stream",stream=expected_file,rowPosition=1,
            byteOffset=0,independentEndpoints=None,storedCenterNumerator=None,
            enclosureStatus="NOT_YET_AVAILABLE")
        require(set(record) == {"file","bytes","rows","sha256","complete"}
                and record["file"] == expected_file and record["complete"] is True,
                "STREAM_MANIFEST: "+expected_file)
        self.record,self.name,self.budget = record,expected_file,budget
        self.handle = (SRC/expected_file).open("rb")
        self.sha,self.size,self.count = hashlib.sha256(),0,0

    def read(self,column=None,degree=None,partial=None):
        bits=H_BITS if self.name=="h-columns.jsonl" else OUT_BITS
        self.budget.context=dict(operation="read-immutable-stream-row",stream=self.name,
            rowPosition=self.count+1,byteOffset=self.size,expectedColumn=column,expectedDegree=degree,
            storedEndpointBits=bits,storedCenterDenominatorPower=bits+1,
            storedPair=None,storedCenterNumerator=None,independentEndpoints=None,
            independentEndpointBits=BITS,enclosureStatus="NOT_YET_AVAILABLE",
            prefixStage="BEFORE_CURRENT_ENTRY_ADDED",partialWeightedDistanceNumerator=partial,
            nativeSquaredSumNumerator=(16*partial if partial is not None else None),
            nativeSquaredSumDenominator="81*2^"+str(2*BITS+2))
        raw = self.handle.readline(65537)
        self.budget.context.update(rawBytes=len(raw),newlinePresent=raw.endswith(b"\n"))
        require(raw and raw.endswith(b"\n") and len(raw) <= 65536,
                "STREAM_ROW_TRUNCATED: "+self.name)
        self.sha.update(raw)
        self.size += len(raw)
        self.count += 1
        self.budget.context["bytesReadThroughCurrentRow"]=self.size
        if self.count % 1024 == 0:
            self.budget.check()
        return decode(raw)

    def finish(self):
        self.budget.context=dict(operation="finish-immutable-stream",stream=self.name,
            rowPosition=self.count+1,byteOffset=self.size,expectedEOF=True,
            observedRows=self.count,expectedRows=self.record["rows"],
            expectedBytes=self.record["bytes"],observedSHA256=self.sha.hexdigest(),
            expectedSHA256=self.record["sha256"],storedCenterNumerator=None,
            independentEndpoints=None,enclosureStatus="NOT_APPLICABLE_TO_EOF_CHECK")
        require(self.handle.read(1) == b"", "STREAM_EXTRA_ROWS: "+self.name)
        self.handle.close()
        require(self.count == self.record["rows"] and self.size == self.record["bytes"]
                and self.sha.hexdigest() == self.record["sha256"],
                "STREAM_COUNT_BYTES_HASH: "+self.name)


def parse_row(row, column, degree,budget):
    budget.context.update(operation="parse-immutable-stream-row",expectedColumn=column,
        expectedDegree=degree,observedRowType=type(row).__name__,
        observedRowLength=(len(row) if type(row) is list else None))
    if type(row) is list and len(row)==4:
        budget.context.update(observedColumnPrefix=str(row[0])[:128],
            observedDegreePrefix=str(row[1])[:128],
            rawEndpointPrefixes=[str(v)[:256] for v in row[2:]])
    require(type(row) is list and len(row) == 4
            and type(row[0]) is int and type(row[1]) is int,"ROW_COMPLETE_ORDER_PARITY")
    pair=endpoint_pair(row[2:])
    budget.context.update(storedPair=list(pair),storedCenterNumerator=sum(pair))
    require(row[:2]==[column,degree],"ROW_COMPLETE_ORDER_PARITY")
    return pair


def raw_norm2(numerator, bits):
    return Fraction(16*numerator,81*(1 << (2*bits+2)))


def verify_h_centers(packet,stream_record,seeds,mesh,budget):
    reader=StreamReader(stream_record,"h-columns.jsonl",budget)
    centers=[[0]*(D+1),[0]*(D+1)]
    summaries=[]
    for s in (0,1):
        budget.progress("full-h-final-center-distance",force=True,column=s)
        distances=squares=0
        for i in range(s,D+1,2):
            pair=parse_row(reader.read(column=s,degree=i,partial=distances),s,i,budget)
            iv=mesh.times_fraction(seeds[s][i],-L*L)
            if i==s:
                iv=mesh.plus(iv,mesh.fraction((1-DELTA)*2*L/(2*s+1)))
            d=final_distance(iv,pair,H_BITS,mesh)
            mid,weight=sum(pair),(2*i+1)*(2*s+1)
            centers[s][i]=mid
            distances+=d*d*weight
            squares+=mid*mid*weight
            error_context(budget,s,i,pair,iv,H_BITS,d,distances,weight)
            # Nonnegative sums: a failing prefix cannot be repaired by later rows.
            require(16*distances<81*(1 << (2*BITS+2-1040)),"H_FULL_FINAL_CENTER_ROUNDING")
        rho2=Fraction(16*distances,81*(1 << (2*BITS+2)))
        norm2=raw_norm2(squares,H_BITS)
        cap=Fraction(1,29) if s==0 else Fraction(3,50)
        budget.context.update(modelNormSquared=fraction_record(norm2),
            requiredNormCap=fraction_record((cap+Fraction(1,1 << 512))**2))
        require(norm2<=(cap+Fraction(1,1 << 512))**2,"H_SAME_CENTER_FULL_POLYNOMIAL_NORM")
        summaries.append(dict(column=s,completeParityRows=(D-s)//2+1,
            independentDistanceWeightedNumerator=str(distances),
            independentFullNativeRoundingSquared=fraction_record(rho2),
            sameCenterModelNormSquared=fraction_record(norm2),
            originalTrueNormCap=fraction_record(cap),
            polynomialRoundingErrorPower=-520,trueHErrorPower=-512,
            oldBoxTruthConsumed=False,oldHalfwidthAuthority=False,
            oldProducerDistanceAuthority=False))
        budget.progress("full-h-final-center-distance",force=True,column=s)
    reader.finish()
    require(reader.count==2047,"H_FULL_PARITY_SHAPE")
    return centers,summaries


def verify_v_centers(packet,record,qseeds,bseeds,h,sc,mesh,budget):
    reader=StreamReader(record,"finite-columns.jsonl",budget)
    qrows=recurrence_rows(qseeds,mesh,"q",budget)
    brows=recurrence_rows(bseeds,mesh,"band",budget)
    harmonic=[Fraction(0)]
    for k in range(1,2*N+1):
        harmonic.append(harmonic[-1]+Fraction(1,k))
    distances=head_entries=0
    norm,comp=[0]*N,[0]*N
    head={}
    for j,(qr,br) in enumerate(zip(qrows,brows)):
        budget.progress("full-V-final-center-distance",force=True,column=j,rows=reader.count)
        for i in range(j%2,D+1,2):
            pair=parse_row(reader.read(column=j,degree=i,partial=distances),j,i,budget)
            if i<j:
                old_pair,iv=head[(i,j)]
                # Guard context uses the current pair and cached TRUE symmetric
                # enclosure; its prefix explicitly excludes the current entry.
                guard_distance=final_distance(iv,pair,OUT_BITS,mesh)
                error_context(budget,j,i,pair,iv,OUT_BITS,guard_distance,distances,(2*i+1)*(2*j+1))
                budget.context.update(operation="same-head-copy-guard",storedPair=list(pair),
                    expectedStoredPair=list(old_pair),prefixStage="BEFORE_CURRENT_ENTRY_ADDED")
                require(pair==old_pair,"SAME_HEAD_EXACT_SYMMETRY")
                # SAME exact symmetric raw coefficient/enclosure; distance counted AGAIN.
            else:
                iv=mesh.times_fraction(mesh.plus(qr[i],br[i]),-L*L)
                if i==j:
                    z=Fraction(1,2*j+1)+2*(harmonic[2*j]-harmonic[j])
                    loggram=mesh.times_ratio(mesh.minus(sc["log2"],mesh.fraction(z)),4,2*j+1)
                else:
                    loggram=mesh.ratio(-4,abs(i-j)*(i+j+1))
                iv=mesh.minus(iv,mesh.times_fraction(loggram,L/2))
                # h is EXACTLY the original stored640 centers, not oracle midpoints.
                unum=36*sum(h[s][i]*h[s][j] for s in (0,1))
                iv=mesh.minus(iv,mesh.ratio(unum,1 << (2*H_BITS+2)))
                if i==j:
                    diagonal=(harmonic[j]-sc["contact"]-Fraction(7,2)-TAU)*2*L/(2*j+1)
                    iv=mesh.plus(iv,mesh.fraction(diagonal))
                if i<N:
                    head[(j,i)]=(pair,iv)
            d=final_distance(iv,pair,OUT_BITS,mesh)
            mid,weight=sum(pair),(2*i+1)*(2*j+1)
            distances+=d*d*weight
            norm[j]+=mid*mid*weight
            if i>=N:
                comp[j]+=mid*mid*weight
            else:
                head_entries+=1
            error_context(budget,j,i,pair,iv,OUT_BITS,d,distances,weight)
            require(16*distances<=81*(1 << (2*BITS+2-440)),"V_FULL_NATIVE_FINAL_CENTER_HS")
        require(norm[j]>=comp[j],"EXACT_FINITE_FULL_COMPLEMENT_GEOMETRY")
    reader.finish()
    require(reader.count==458528 and len(head)==50400 and head_entries==100352,
            "V_COMPLETE_RECTANGLE_HEAD_COUNTS")
    rho2=Fraction(16*distances,81*(1 << (2*BITS+2)))
    return norm,comp,dict(completeParityRows=reader.count,uniqueHeadEntries=len(head),
        fullHeadEntries=head_entries,independentDistanceWeightedNumerator=str(distances),
        independentFullNativeHSSquared=fraction_record(rho2),
        rawSourceMeaning="w_ij=sqrt(g_j)*<p_i,W_j>; native coefficient=w_ij/sqrt(g_i*g_j)",
        oldBoxTruthConsumed=False,oldHalfwidthAuthority=False,
        oldProducerDistanceAuthority=False,sameStoredH640Used=True,
        GhatExactlySameHead=True)


def sqrt_interval(pair,bits):
    require(0 <= pair[0] <= pair[1], "NONNEGATIVE_SQUARED_NORM")
    # At output grid2^-bits, sqrt(n/2^bits)=sqrt(n*2^bits)/2^bits.
    lo = isqrt(pair[0] << bits)
    hi = isqrt(pair[1] << bits)
    if hi*hi < pair[1] << bits:
        hi += 1
    return Fraction(lo,1 << bits),Fraction(hi,1 << bits)


def outward_pair(iv,bits,mesh):
    require(0<=iv[0]<=iv[1],"AUTHORITATIVE_NONNEGATIVE_NORM_ORDER")
    step=1 << (mesh.bits-bits)
    return iv[0]//step,ceildiv(iv[1],step)


def actual_norm_interval(model_pair,bits,error_power):
    lo,hi=sqrt_interval(model_pair,bits)
    eps=Fraction(1,1 << error_power)
    return [fraction_record(max(Fraction(0),lo-eps)),fraction_record(hi+eps)]


def verify_old_norm_syntax(record,budget):
    reader=StreamReader(record,"column-norms.jsonl",budget)
    fields={"column","nativeModelNormSquared","nativeModelComplementNormSquared",
        "nativeInfiniteTailNormSquared","squaredNormOutputBits","firstInfiniteDegree",
        "K","actualColumnL2ErrorPower"}
    for j in range(N):
        row=reader.read(column=j)
        i0=D+1+(1 if (D+1-j)%2 else 0)
        require(type(row) is dict and set(row)==fields and row["column"]==j
            and row["squaredNormOutputBits"]==OUT_BITS and row["firstInfiniteDegree"]==i0
            and row["K"]==(i0-j)//2 and row["actualColumnL2ErrorPower"]==-203,
            "OLD_NORM_SCHEMA_DIAGNOSTIC")
        for key in ("nativeModelNormSquared","nativeModelComplementNormSquared","nativeInfiniteTailNormSquared"):
            endpoint_pair(row[key]) # syntax/order ONLY; NO enclosure/norm authority.
    reader.finish()
    return dict(rows=reader.count,byteHashChecked=True,schemaChecked=True,
                oldNumericBracketTruthConsumed=False)


def new_authoritative_norms(full_nums,comp_nums,sc,mesh,budget):
    budget.progress("NEW-authoritative-model-norms",force=True)
    harmonic2,odd2=[Fraction(0)],[Fraction(0)]
    for r in range(1,1501):
        harmonic2.append(harmonic2[-1]+Fraction(1,r*r))
        odd2.append(odd2[-1]+Fraction(1,(2*r-1)**2))
        if r%128==0:
            budget.check()
    pi2=mesh.product(sc["pi"],sc["pi"])
    total_full,total_comp=(0,0),(0,0)
    writer=NormWriter(budget)
    for j in range(N):
        i0=D+1+(1 if (D+1-j)%2 else 0)
        k=(i0-j)//2
        tail=mesh.minus(mesh.fraction(odd2[k+j]-harmonic2[k-1]/4),mesh.times_ratio(pi2,1,12))
        budget.context=dict(column=j,firstInfiniteDegree=i0,K=k,
            independentTailEndpoints=list(tail),independentEndpointBits=BITS)
        require(tail[1]>=0,"EXACT_SQUARE_SUM_TAIL_UPPER_NONNEGATIVE")
        # Exact sum-of-squares identity proves nonnegativity independently of rounding.
        tail=max(0,tail[0]),tail[1]
        require(full_nums[j]>=comp_nums[j]>=0,"SAME_CENTER_EXACT_FINITE_GEOMETRY")
        full=mesh.plus(mesh.fraction(raw_norm2(full_nums[j],OUT_BITS)),tail)
        comp=mesh.plus(mesh.fraction(raw_norm2(comp_nums[j],OUT_BITS)),tail)
        fp,cp,tp=(outward_pair(iv,OUT_BITS,mesh) for iv in (full,comp,tail))
        writer.write(dict(column=j,firstInfiniteDegree=i0,K=k,squaredNormBits=OUT_BITS,
            nativeModelNormSquared=list(map(str,fp)),
            nativeModelComplementNormSquared=list(map(str,cp)),
            nativeInfiniteTailNormSquared=list(map(str,tp)),
            actualColumnNorm=actual_norm_interval(fp,OUT_BITS,203),
            authority="NEW_INDEPENDENT_SAME_CENTER_MODEL_NORM",
            oldNormBracketConsumed=False,endpointLogTailDiscarded=False))
        total_full,total_comp=mesh.plus(total_full,full),mesh.plus(total_comp,comp)
        budget.progress("NEW-authoritative-model-norms",column=j)
    require(writer.count==N,"NEW_NORM_COMPLETE_COLUMNS")
    writer.finish()
    fp,cp=outward_pair(total_full,OUT_BITS,mesh),outward_pair(total_comp,OUT_BITS,mesh)
    return dict(stream=writer.record(),squaredNormBits=OUT_BITS,
        nativeModelHSSquared=list(map(str,fp)),
        nativeModelComplementHSSquared=list(map(str,cp)),
        actualVHSNorm=actual_norm_interval(fp,OUT_BITS,198),
        actualComplementHSNorm=actual_norm_interval(cp,OUT_BITS,198),
        authority="NEW_INDEPENDENT_SAME_CENTER_MODEL_NORMS_ONLY",
        oldColumnAndTotalNormBoxesConsumed=False,
        fullOutsideHead="same rows448..2046 plus EXACT infinite endpoint-log tail",
        errorTransport="sqrt(model squared norm) +/-2^-198; never squared-norm addition")


def independent_error_ledger(sc):
    eq=Fraction(4608)*Fraction(3,4)**577
    eb=2*L*(Fraction(914*576**2048,factorial(2048))+
        Fraction(1,1 << 1098)*Fraction(68,25)**576)
    # Common lower3 is proved for BOTH true pi and exact p_pi. Never substitute
    # a true-pi-only lower endpoint into the distinct p_pi denominator.
    require(sc["pi"][0]>3*(1 << BITS) and sc["ppi"]>3,"BOTH_PI_DENOMINATORS_GT_THREE")
    taylor=Fraction(576**2049,3*factorial(2049))
    normalization=2*sc["machinRadius"]/sc["ppi"]
    require(eq<Fraction(1,1 << 227) and eb<Fraction(1,1 << 204),"GLOBAL_Q_BAND_BOUNDS")
    require(taylor<Fraction(1,1 << 513) and normalization<Fraction(1,1 << 646),
            "SEPARATE_TRUE_PI_TAYLOR_PPI_NORMALIZATION")
    eh=Fraction(1,1 << 513)+Fraction(1,1 << 646)+Fraction(1,1 << 520)
    uerr=Fraction(1,1 << 512)*(Fraction(162,29)+Fraction(162,50)+108*Fraction(1,1 << 512))
    ev=Fraction(1,1 << 204)+Fraction(1,1 << 227)+9*Fraction(1,1 << 512)+Fraction(1,1 << 600)+Fraction(1,1 << 220)
    require(eh<Fraction(1,1 << 512) and uerr<9*Fraction(1,1 << 512)
        and ev<Fraction(1,1 << 203) and 22*ev<Fraction(1,1 << 198)
        and N<22*22,"SAME_ORIGINAL_GLOBAL_OP_HS_G_TARGETS")
    return dict(qOperatorErrorPower=-227,bandOperatorErrorPower=-204,
        truePiSincTaylorErrorPower=-513,exactPpiNormalizationErrorPower=-646,
        hPolynomialRoundingErrorPower=-520,hTrueGlobalErrorPower=-512,
        oldRankTwoError="9*2^-512",contactToSameCenterErrorPower=-600,
        finiteNativeAssemblyHSErrorPower=-220,nativeVOperatorErrorPower=-203,
        nativeVHSErrorPower=-198,nativeGOperatorErrorPower=-203,
        independentQBound=fraction_record(eq),acceptedOldGlobalBandBound=fraction_record(eb),
        truePiTaylorUsingCommonLower3=fraction_record(taylor),
        exactPpiNormalizationBound=fraction_record(normalization),
        normalizationProof="Btilde=(pi/p_pi)C_pi; ||C_pi||<2; (2/p_pi)|pi-p_pi|",
        oldProducerPiEndpointUsed=False,oldExactSincBoundAuthority=False,
        momentBinetChargedOnce=True,errorsAreGlobalOriginalDu=True,
        laterInversionOrWholeSchurErrorPaid=False)


def pin_inventory(budget):
    inventory={}
    for name,expected in ALL_PINS.items():
        budget.context=dict(operation="immutable-pin",pin=name,bytes=0,expectedSHA256=expected,
            observedSHA256=None,storedCenterNumerator=None,independentEndpoints=None,
            enclosureStatus="NOT_APPLICABLE_TO_PIN_CHECK")
        path=(ROOT/name).resolve()
        require(path.is_relative_to(ROOT) and path.is_file(),"PIN_PATH: "+name)
        h,size=hashlib.sha256(),0
        with path.open("rb") as handle:
            while block:=handle.read(1 << 20):
                h.update(block)
                size+=len(block)
                budget.context["bytes"]=size
                budget.check()
        budget.context.update(bytes=size,observedSHA256=h.hexdigest())
        require(h.hexdigest()==expected,"IMMUTABLE_PIN: "+name)
        inventory[name]=dict(bytes=size,sha256=expected)
    return inventory


def small_json(path,budget):
    budget.context=dict(operation="read-metadata",metadataFile=str(path.relative_to(ROOT)),
        independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_APPLICABLE_TO_METADATA_CHECK")
    raw=path.read_bytes()
    budget.context["bytes"]=len(raw)
    require(len(raw)<=1024*1024,"METADATA_SIZE_CAP")
    return decode(raw)


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


def freeze_guard(freeze_path):
    freeze_path=freeze_path.resolve()
    require(not freeze_path.is_relative_to(OUT) and not freeze_path.is_relative_to(SRC),
            "FREEZE_OUTSIDE_NEW_OUTPUT_AND_OLD_SOURCE")
    raw=freeze_path.read_bytes()
    require(len(raw)<=65536,"CENTER_FREEZE_SIZE")
    obj=decode(raw)
    verifier_sha=digest(SELF.read_bytes())
    require(obj.get("schema")=="RH_WEIL_FINAL_CENTER_FREEZE_V1"
        and obj.get("authorization")=="ROOT_EXPLICIT_FREEZE_AND_VERIFY_CENTERS"
        and obj.get("runtimeGoalCreatedAt")==1793085111,"NO_EXACT_ROOT_CENTER_FREEZE")
    canonical=lambda x:json.dumps(x,sort_keys=True,separators=(",",":"))
    require(canonical(obj.get("parameters"))==canonical(CERT_PARAMETERS)
        and obj.get("pins")==ALL_PINS and obj.get("verifierSHA256")==verifier_sha,
        "CENTER_FREEZE_CODE_PARAMETERS_PINS")
    require(OUT.is_relative_to(ROOT/"literature/local") and SRC.is_relative_to(ROOT/"literature/local")
        and OUT!=SRC,"SEPARATE_INPUT_OUTPUT_PATHS")
    require(not OUT.exists(),"ONE_CENTER_ATTEMPT_DIRECTORY_ALREADY_EXISTS")
    OUT.mkdir(parents=True,exist_ok=False)
    return dict(verifierSHA256=verifier_sha,centerFreezeSHA256=digest(raw)),raw,freeze_path


def source_protocol(inventory,budget):
    budget.progress("immutable-source-protocol",force=True)
    budget.context=dict(operation="old-source-directory-cap",inputDirectory=str(SRC.relative_to(ROOT)),
        independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_APPLICABLE_TO_DIRECTORY_CHECK")
    require(SRC.is_dir(),"OLD_SOURCE_MISSING")
    files=list(SRC.iterdir())
    require(all(p.is_file() for p in files)
        and sum(p.stat().st_size for p in files)<=INPUT_CAP_BYTES
        and not list(SRC.glob("*.part")) and not list(SRC.glob("*.tmp")),"OLD_INPUT_CAP_OR_COMPLETENESS")
    packet=small_json(SRC/"result.json",budget)
    stop=small_json(SRC/"replay-result.json",budget)
    pf=small_json(ROOT/(OLD+"producer-freeze.json"),budget)
    rf=small_json(ROOT/(OLD+"replay-freeze.json"),budget)
    budget.context=dict(operation="source-protocol-shape",metadataFile=SOURCE_PREFIX+"result.json",
        independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_APPLICABLE_TO_METADATA_CHECK")
    require(packet["schema"]=="RH_WEIL_RETAINED_SOURCE_PACKET_V1"
        and packet["status"]=="SOURCE_PACKET_PRODUCED_PENDING_INDEPENDENT_REPLAY"
        and packet["runtimeGoalCreatedAt"]==1793085111 and packet["parameters"]==PARAMETERS
        and packet["producerSHA256"]==FIXED_PINS[OLD+"produce-source.py"]
        and packet["freezeSHA256"]==FIXED_PINS[OLD+"producer-freeze.json"]
        and 0<=packet["elapsedSeconds"]<=CAP_SECONDS,"OLD_SOURCE_BINDING")
    require(packet["fullQCertified"] is False and packet["RHCertified"] is False
        and packet["mathIterations"]==0 and packet["signedMargin"] is None
        and packet["wholeSchurMargin"] is None,"OLD_SOURCE_ONLY_SCOPE")
    budget.context["metadataFile"]=SOURCE_PREFIX+"replay-result.json"
    require(stop["schema"]=="RH_WEIL_RETAINED_SOURCE_REPLAY_STOP_V1"
        and stop["status"]=="STOPPED_NO_RETRY" and stop["runtimeGoalCreatedAt"]==1793085111
        and stop["reason"]=="INDEPENDENT_CONTAINMENT: h:0:1660"
        and stop["bindings"]["sourceResultSHA256"]==FIXED_PINS[SOURCE_PREFIX+"result.json"]
        and stop["bindings"]["checkerSHA256"]==FIXED_PINS[OLD+"check-source.py"],"PRESERVE_ACTUAL_OLD_STOP")
    budget.context["metadataFile"]=OLD+"producer-freeze.json"
    require(pf["producerSHA256"]==FIXED_PINS[OLD+"produce-source.py"]
        and pf["parameters"]==PARAMETERS and pf["inputs"]==INPUTS,"OLD_PRODUCER_FREEZE")
    budget.context["metadataFile"]=OLD+"replay-freeze.json"
    require(rf["checkerSHA256"]==FIXED_PINS[OLD+"check-source.py"]
        and rf["producerSHA256"]==FIXED_PINS[OLD+"produce-source.py"]
        and rf["sourceResultSHA256"]==FIXED_PINS[SOURCE_PREFIX+"result.json"]
        and rf["producerFreezeSHA256"]==FIXED_PINS[OLD+"producer-freeze.json"]
        and rf["parameters"]==PARAMETERS and rf["inputs"]==INPUTS,"OLD_REPLAY_FREEZE")
    budget.context["metadataFile"]=SOURCE_PREFIX+"result.json"
    require(packet["inputs"]=={k:inventory[k] for k in INPUTS},"ACCEPTED_SOURCE_INPUT_INVENTORY")
    streams=packet["streams"]
    require(type(streams) is list and len(streams)==3,"OLD_THREE_STREAMS")
    for rec,(name,rows,size) in zip(streams,STREAM_SPECS):
        budget.context.update(stream=name,expectedRows=rows,expectedBytes=size)
        require(rec==dict(file=name,rows=rows,bytes=size,
            sha256=FIXED_PINS[SOURCE_PREFIX+name],complete=True),"IMMUTABLE_STREAM_MANIFEST: "+name)
        require(inventory[SOURCE_PREFIX+name]["bytes"]==size,"ACTUAL_STREAM_SIZE: "+name)
    fc,hc=packet["finiteColumns"],packet["oldHColumns"]
    require(fc["file"]=="finite-columns.jsonl" and fc["intervalDenominatorPower"]==OUT_BITS
        and fc["midpointDenominatorPower"]==OUT_BITS+1 and fc["completeParityRows"]==458528
        and hc["file"]=="h-columns.jsonl" and hc["intervalDenominatorPower"]==H_BITS
        and hc["midpointDenominatorPower"]==H_BITS+1 and hc["completeParityRows"]==2047
        and hc["UrawCoefficient"]==36,"SAME_RAW_CENTER_SCALES")
    tail=packet["symbolicInfiniteTail"]
    require(tail["firstDegree"]==D+1 and tail["endpointLogDiscarded"] is False
        and tail["nativeCoefficient"]=="sqrt((2i+1)(2j+1))/((i-j)(i+j+1))"
        and tail["rawExpansionCoefficient"]=="(2i+1)/((i-j)(i+j+1))","SAME_EXACT_ENDPOINT_TAIL")
    require(packet["Ghat"]==dict(source="first448 rows of SAME finite-columns stream",
        symmetricHeadExactlyCopied=True,modelConsistencyExact=True),"SAME_G_HEAD_MODEL")
    return packet


def scalar_record(sc):
    return dict(workingBits=BITS,log2=list(map(str,sc["log2"])),pi=list(map(str,sc["pi"])),
        gamma=list(map(str,sc["gamma"])),trueContact=list(map(str,sc["contactInterval"])),
        SAMEStoredContactCenter=fraction_record(sc["contact"]),
        independentContactToCenterRadius=fraction_record(sc["contactRadius"]),
        exactSameMachin160=fraction_record(sc["ppi"]),
        exactMachinRemainder=fraction_record(sc["machinRadius"]),
        independentTruePiToExactPpiError=fraction_record(sc["independentPpiError"]),
        gammaRemainder=fraction_record(sc["gammaRemainder"]),
        truePiGreaterThan3=True,exactPpiGreaterThan3=True,
        oldScalarBoxTruthConsumed=False,oldContactRadiusAuthority=False)


def verify(freeze_path):
    bindings,freeze_raw,freeze_path=freeze_guard(freeze_path)
    budget=CertificateBudget(bindings)
    try:
        budget.progress("start-input-pins",force=True)
        inventory=pin_inventory(budget)
        packet=source_protocol(inventory,budget)
        budget.progress("old-norm-stream-SCHEMA-HASH-ONLY",force=True)
        old_norm_syntax=verify_old_norm_syntax(packet["streams"][2],budget)
        budget.context=dict(operation="read-accepted-moments",pin=PREFIX+"run-01/certificates/moments.json",
            independentEndpoints=None,storedCenterNumerator=None,enclosureStatus="NOT_APPLICABLE_TO_METADATA_CHECK")
        moment_raw=(ROOT/(PREFIX+"run-01/certificates/moments.json")).read_bytes()
        require(digest(moment_raw)==INPUTS[PREFIX+"run-01/certificates/moments.json"],"MOMENT_PIN_AT_USE")
        moments=moments_from(moment_raw)
        bernoulli=bernoulli_values(QDEG+1,budget)
        mesh=Directed()
        budget.progress("independent-TRUE-scalars-to-SAME-contact-center",force=True)
        sc=independent_scalars(packet,bernoulli,mesh,budget)
        ledger=independent_error_ledger(sc)
        qcoeff=q_coefficients(bernoulli,budget)
        sinc,band=[Fraction(0)]*(D+1),[Fraction(0)]*(D+1)
        for q in range(1024):
            m=2*q
            sinc[m]=Fraction((-1)**q*256*576**m,factorial(m+1))/sc["ppi"]
            band[m]=(-1)**q*moments[q]*576**m/factorial(m)
            if q%64==0:
                budget.check()
        hseeds=factorial_seeds(sinc,mesh,budget,"sinc")
        h,hsummary=verify_h_centers(packet,packet["streams"][0],hseeds,mesh,budget)
        qseeds=factorial_seeds(qcoeff,mesh,budget,"q")
        bseeds=factorial_seeds(band,mesh,budget,"band")
        full_nums,comp_nums,arithmetic=verify_v_centers(packet,packet["streams"][1],qseeds,bseeds,h,sc,mesh,budget)
        norms=new_authoritative_norms(full_nums,comp_nums,sc,mesh,budget)
        budget.progress("final-immutable-pin-recheck",force=True)
        require(pin_inventory(budget)==inventory,"BINDINGS_CHANGED_DURING_CERTIFICATE")
        budget.context=dict(operation="final-verifier-code-pin",pin=str(SELF.relative_to(ROOT)),
            expectedSHA256=bindings["verifierSHA256"],independentEndpoints=None,
            storedCenterNumerator=None,enclosureStatus="NOT_APPLICABLE_TO_PIN_CHECK")
        require(digest(SELF.read_bytes())==bindings["verifierSHA256"],"BINDINGS_CHANGED_DURING_CERTIFICATE")
        budget.context=dict(operation="final-freeze-pin",pin=str(freeze_path),
            expectedSHA256=bindings["centerFreezeSHA256"],independentEndpoints=None,
            storedCenterNumerator=None,enclosureStatus="NOT_APPLICABLE_TO_PIN_CHECK")
        require(freeze_path.read_bytes()==freeze_raw,"BINDINGS_CHANGED_DURING_CERTIFICATE")
        nr=norms["stream"]
        budget.context=dict(operation="final-new-norm-output-hash",stream=nr["file"],expectedBytes=nr["bytes"],
            expectedSHA256=nr["sha256"],independentEndpoints=None,storedCenterNumerator=None,
            enclosureStatus="NOT_APPLICABLE_TO_PIN_CHECK")
        raw=(OUT/nr["file"]).read_bytes()
        require(len(raw)==nr["bytes"] and digest(raw)==nr["sha256"],"NEW_NORM_OUTPUT_CHANGED")
        result=dict(schema="RH_WEIL_FINAL_CENTER_CERTIFICATE_V1",
            status="CENTER_ONLY_FULL_H_SOURCE_VERIFIED_PENDING_ROOT",
            runtimeGoalCreatedAt=1793085111,parameters=CERT_PARAMETERS,
            startedUTC=budget.started_utc,endedUTC=datetime.now(timezone.utc).isoformat(),
            elapsedSeconds=time.monotonic()-budget.started,bindings=bindings,inputs=inventory,
            originalSourceResultSHA256=FIXED_PINS[SOURCE_PREFIX+"result.json"],
            oldSTOPSHA256=FIXED_PINS[SOURCE_PREFIX+"replay-result.json"],
            oldCheckerSTOPPreserved=True,oldBudgetReopened=False,
            criterion="MAXIMUM distance of independent TRUE enclosure endpoints to SAME FINAL stored centers",
            independentSeedRoute="closed exact factorial double-integral quotients",
            completeHColumns=hsummary,finiteVNativeError=arithmetic,
            independentScalars=scalar_record(sc),globalSourceErrorLedger=ledger,
            authoritativeNEWNorms=norms,oldNormStreamSchemaHashDiagnostic=old_norm_syntax,
            originalNorm="L2((-9/8,9/8),du;C); g_i=9/[4(2i+1)]",
            object="V=R E448; G_R=E*V; Ghat is SAME Vhat head, not Vhat*Vhat",
            nativeVOperatorErrorPower=-203,nativeVHSErrorPower=-198,nativeGOperatorErrorPower=-203,
            sameFiniteCentersUnchanged=True,sameContactCenterUnchanged=True,
            sameH640CentersInW=True,sameExactInfiniteEndpointTail=True,
            oldScalarBoxTruthConsumed=False,oldCoefficientBoxTruthConsumed=False,
            oldNormBoxTruthConsumed=False,oldHalfwidthAuthority=False,
            oldProducerInternalDistanceAuthority=False,
            rootConsumption="PENDING_ROOT_AUDIT",fullQCertified=False,RHCertified=False,
            signedMargin=None,wholeSchurMargin=None,mathIterations=0,pendingProcesses=[],
            scope="SAME immutable final centers/full-H source errors ONLY; old interval packet not retrospectively validated; signed head/inverse/whole/growing/Xi unpaid")
        budget.check()
        budget.atomic("result.json",result)
        budget.progress("complete-center-source-pending-root",force=True)
        return result
    except BaseException as error:
        if budget.norm_writer is not None:
            budget.norm_writer.close()
        failure=dict(schema="RH_WEIL_FINAL_CENTER_STOP_V1",status="STOPPED_NO_RETRY",
            runtimeGoalCreatedAt=1793085111,parameters=CERT_PARAMETERS,bindings=bindings,
            startedUTC=budget.started_utc,endedUTC=datetime.now(timezone.utc).isoformat(),
            elapsedSeconds=time.monotonic()-budget.started,stage=budget.stage,detail=budget.detail,
            context=budget.context,errorType=type(error).__name__,reason=str(error)[:1500],
            partialNormOutput=(budget.norm_writer.record() if budget.norm_writer is not None else None),
            oldCheckerSTOPPreserved=True,oldBudgetReopened=False,
            oldScalarBoxTruthConsumed=False,oldCoefficientBoxTruthConsumed=False,
            oldNormBoxTruthConsumed=False,oldHalfwidthAuthority=False,
            oldProducerInternalDistanceAuthority=False,
            fullQCertified=False,RHCertified=False,mathIterations=0,pendingProcesses=[],
            nextAction="root reconcile exact stop; no retry/recenter/precision/source/route successor authorized")
        budget.atomic("result.json",failure,emergency=True)
        budget.atomic("progress.json",failure,emergency=True)
        raise


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center-freeze-file",type=Path,required=True)
    args=parser.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    result=verify(args.center_freeze_file)
    print(json.dumps(dict(status=result["status"],elapsedSeconds=result["elapsedSeconds"],
        result=str(OUT/"result.json")),ensure_ascii=False))


if __name__=="__main__":
    main()

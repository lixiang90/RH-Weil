"""Finite algebra and source bindings for original scalar fourth admission.

No analytic Lp theorem, prime asymptotic, scalar upper, proportion, or boundary
is certified. Generation writes only the new JSON; --check is read-only.
"""

import sys
sys.dont_write_bytecode = True
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
P = "reviews/2026-10-08/"
SOURCE = P+"hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md"
REVIEWS = [P+"hybrid-short-carrier-canonical-scalar-fourth-admission-review-twisted.md",
           P+"hybrid-short-carrier-canonical-scalar-fourth-admission-review-compression.md"]
NOTE = "notes/474-original-short-carrier-canonical-scalar-fourth-admission.md"
NOTE_REVIEW = P+"474-original-scalar-admission-review-twisted.md"
SELF = "scripts/hybrid_scalar_fourth_admission_checkpoint.py"
OUTPUT = ROOT/"output/hybrid-scalar-fourth-admission-checkpoint.json"
FILES = [SOURCE, NOTE, *REVIEWS, NOTE_REVIEW, SELF]
PAIRS = {SOURCE: REVIEWS, NOTE: [NOTE_REVIEW]}
FROZEN = {
    SOURCE: "f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7",
    REVIEWS[0]: "f9b42278677a371bd38d8cb9555ac4306635336bd23a566be19e7a61eba047c3",
    REVIEWS[1]: "288546e77100d32ac22a0da71a9a89ec3f1c771ef32c7a06baf6d66740a4c605",
    NOTE: "37306c6d403f48c93d5d0f92782088225084e2e4b6b694cd89644a75fe39e99f",
    NOTE_REVIEW: "1ed9e97fa043c407d60d70d440f8f475a8e294b69040d0abe6dab72b2935981a",
}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT/name)
    digest = hashlib.sha256(data).hexdigest()
    if name in FROZEN:
        assert digest == FROZEN[name], ("frozen binding differs", name)
    return {"path": name, "sha256_canonical_lf": digest,
            "canonical_utf8_bytes": len(data), "lines": len(data.splitlines())}


def finite():
    checks = []

    def eq(label, left, right):
        assert left == right, label
        checks.append(label)

    def tidy(poly):
        return {monomial: value for monomial, value in poly.items() if value}

    def product(left, right):
        out = defaultdict(int)
        for a, av in left.items():
            for b, bv in right.items():
                out[tuple(sorted(a+b))] += av*bv
        return tidy(out)

    def atom(*names, sign=1):
        return {tuple(sorted(names)): sign}

    def add(target, key, polynomial):
        dest = target.setdefault(key, defaultdict(int))
        for monomial, value in polynomial.items():
            dest[monomial] += value

    def clean_columns(columns):
        return {key: tidy(poly) for key, poly in columns.items() if tidy(poly)}

    # Exact formal real-line frequencies for actual primes 5,7,11. A site
    # vector represents u+sum_j v_j log(p_j); no torus or wrapping occurs.
    # Window values remain formal symbols: this checks an algebraic identity
    # for every taper, not a numerical surrogate for its analytic bounds.
    primes = [5, 7, 11]
    units = [tuple(int(i == j) for i in range(3)) for j in range(3)]
    zero = (0, 0, 0)
    plus = lambda a, b: tuple(x+y for x, y in zip(a, b))
    minus = lambda a, b: tuple(x-y for x, y in zip(a, b))
    phi = lambda site: "phi:"+str(site)
    bp = lambda index: "b:"+str(primes[index])

    def A_at(site):
        return {plus(site, e): atom(bp(j), phi(site), phi(plus(site, e)), sign=-1)
                for j, e in enumerate(units)}

    for site in [zero, (1, -2, 1), (-1, 1, 0)]:
        direct = {}
        for j, e in enumerate(units):
            shifted = minus(site, e)
            prefactor = atom(bp(j), phi(site), phi(shifted), sign=-1)
            for phase, poly in A_at(shifted).items():
                add(direct, phase, product(prefactor, poly))
        pu = {e: atom(bp(j), phi(minus(site, e)), phi(minus(site, e)))
              for j, e in enumerate(units)}
        filtered = {}
        for e, poly in pu.items():
            for j, f in enumerate(units):
                phase = minus(f, e)
                value = product(poly, atom(bp(j), phi(plus(site, phase)), phi(site)))
                add(filtered, plus(site, phase), value)
        eq("exact A* A versus two multiplier frequencies at "+str(site),
           clean_columns(direct), clean_columns(filtered))
        diagonal = defaultdict(int)
        for j, e in enumerate(units):
            for monomial, value in atom(bp(j), bp(j), phi(site), phi(site),
                                        phi(minus(site, e)), phi(minus(site, e))).items():
                diagonal[monomial] += value
        eq("original same-prime diagonal at "+str(site),
           tidy(direct[site]), tidy(diagonal))
        eq("six distinct prime-ratio frequencies at "+str(site),
           len(clean_columns(direct))-1, 6)

    # Universal finite interval counting; rational examples include integral
    # and nonintegral s/eta and both endpoint overlaps. Continuous identities
    # are proved in the source; this tests exact finite values, not sampling.
    for T, eta, span in [(Q(100), Q(5, 2), Q(20)),
                         (Q(111, 10), Q(3, 7), Q(23, 7)),
                         (Q(29), Q(3), Q(7, 2))]:
        d = int(T/eta)
        intervals = [(T+k*eta, T+span+k*eta) for k in range(d)]
        ends = sorted({t for interval in intervals for t in interval})
        count = lambda t: sum(lo <= t <= hi for lo, hi in intervals)
        total = sum((hi-lo)*count((hi+lo)/2) for lo, hi in zip(ends, ends[1:]))
        eq("overlap normalized integral for "+str((T, eta, span)), total/(span*d), Q(1))
        probe = ends+[(a+b)/2 for a, b in zip(ends, ends[1:])]
        assert all(Q(count(t), span*d) <= (1+eta/span)/(d*eta) for t in probe)
        checks.append("overlap upper including all endpoints for "+str((T, eta, span)))
        assert ends[0] == T and ends[-1] <= 2*T+span and span < T/2
        assert min(T-T/2, 3*T-(2*T+span)) >= T/2
        assert min(T/2-T/4, 4*T-3*T) >= T/4
        checks.append("positive guard support for "+str((T, eta, span)))

    # Exponents are (power of X, power of ell), ignoring fixed 2pi constants.
    multiply = lambda a, b: tuple(x+y for x, y in zip(a, b))
    scale = lambda a, q: tuple(q*x for x in a)
    m, height = (Q(1, 2), Q(-1)), (Q(1), Q(0))
    eq("first normalized guard m/T", multiply(m, scale(height, -1)), (Q(-1, 2), Q(-1)))
    eq("second normalized guard m^2/T", multiply(scale(m, 2), scale(height, -1)), (Q(0), Q(-2)))
    eq("first guard L4 before normalization", multiply(m, scale(height, Q(-3, 4))), (Q(-1, 4), Q(-1)))
    eq("square-prime fourth energy root", scale((Q(-1, 2), Q(-2)), Q(1, 4)), (Q(-1, 8), Q(-1, 2)))
    eq("square-prime MV error root", scale((Q(-1), Q(0)), Q(1, 4)), (Q(-1, 4), Q(0)))
    assert Q(-1, 8) < Q(-1, 12) and Q(-1, 4) < Q(-1, 12)
    checks.append("both square-prime L4 powers faster than total X^(-1/12)")
    ell = (Q(0), Q(1))
    carrier_size = multiply(height, ell)
    span_size = multiply(height, scale(ell, Q(-1, 2)))
    eq("floor unit loss divided by carrier size", scale(carrier_size, -1), (Q(-1), Q(-1)))
    eq("eta/span relative cost", multiply(scale(ell, -1), scale(span_size, -1)),
       (Q(-1), Q(-1, 2)))
    terms = [("N", Q(1, 2)), ("delta", Q(1, 4)), ("epsilon", Q(0))]
    growth_square = [{"coefficient": 1 if i == j else 2,
                      "factors": [a, b], "power_of_M": str(e+f)}
                     for i, (a, e) in enumerate(terms)
                     for j, (b, f) in enumerate(terms) if i <= j]
    eq("all six growth-square terms retained", len(growth_square), 6)

    def factors(n):
        out = {}
        p = 2
        while p*p <= n:
            while n % p == 0:
                out[p] = out.get(p, 0)+1
                n //= p
            p += 1
        if n > 1:
            out[n] = out.get(n, 0)+1
        return out

    def von_mangoldt(n):
        fac = factors(n)
        return next(iter(fac)) if len(fac) == 1 else None

    def mobius(n):
        fac = factors(n)
        return 0 if any(e > 1 for e in fac.values()) else (-1)**len(fac)

    X, Y = 16, 4
    example = None
    for n in range(X+1, X*X+1):
        full, low, upper, original, completed = (defaultdict(int) for _ in range(5))
        for a in range(1, n+1):
            if n % a:
                continue
            b = n//a
            pa, pb = von_mangoldt(a), von_mangoldt(b)
            if pa is not None and pb is not None:
                key = tuple(sorted((pa, pb)))
                full[key] += 1
                if a <= Y:
                    low[key] += 2
                if a > X and b > Y:
                    upper[key] += 2
                if Y < a <= X and Y < b <= X:
                    original[key] += 1
            mu = mobius(a)
            for p, ep in factors(b).items():
                for q, eq_ in factors(b).items():
                    completed[tuple(sorted((p, q)))] += mu*ep*eq_
        pn = von_mangoldt(n)
        if pn is not None:
            for q, exponent in factors(n).items():
                completed[tuple(sorted((pn, q)))] -= exponent
        eq("formal mu*log^2 minus Lambda log at n="+str(n), tidy(completed), tidy(full))
        corrected = defaultdict(int, completed)
        for term in [low, upper]:
            for monomial, value in term.items():
                corrected[monomial] -= value
        eq("both sharp-factor corrections at n="+str(n), tidy(corrected), tidy(original))
        if n == 95:
            example = {"full": tidy(full), "low": tidy(low), "upper": tidy(upper),
                       "original": tidy(original)}
    eq("upper-cutoff n95 has full two log5 log19", example["full"], {(5, 19): 2})
    eq("upper-cutoff n95 low correction vanishes", example["low"], {})
    eq("upper-cutoff n95 upper correction required", example["upper"], {(5, 19): 2})
    eq("upper-cutoff n95 original column is zero", example["original"], {})
    return {"checks": checks, "count": len(checks), "cutoff_coefficients_checked": 240,
            "growth_square_terms": growth_square,
            "scope": "finite formal frequency, interval, exponent and prime-log algebra only",
            "analytic_Lp_bound_verified_by_this_script": False,
            "canonical_scalar_upper_verified_by_this_script": False}


def build():
    records = {name: binding(name) for name in FILES}
    reviews, citations, links = [], [], 0
    for source, reviewers in PAIRS.items():
        digest = records[source]["sha256_canonical_lf"]
        for review in reviewers:
            assert digest in canonical(ROOT/review).decode("utf-8"), (source, review)
            reviews.append({"source": source, "source_sha256": digest, "review": review,
                            "review_sha256": records[review]["sha256_canonical_lf"]})
    link_pattern = r"\[[^\]\n]*\]\(([^)\n]+)\)"
    hash_pattern = link_pattern+r"\s*\|\s*"+chr(96)+r"?([a-f0-9]{64})"+chr(96)+"?"
    for name in FILES:
        if not name.endswith(".md"):
            continue
        content = canonical(ROOT/name).decode("utf-8")
        for target in re.findall(link_pattern, content):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            if not re.search(r"\.(md|py|json|tex|pdf|lean)(#.*)?$", target):
                continue
            path = (ROOT/name).parent.joinpath(target.split("#", 1)[0]).resolve()
            # A note may link the not-yet-generated new output. Its own hash
            # is never a bound input, so generation has no first-output cycle.
            if path != OUTPUT.resolve():
                assert path.exists(), (name, target)
            links += 1
        for target, digest in re.findall(hash_pattern, content):
            path = (ROOT/name).parent.joinpath(target).resolve()
            data = path.read_bytes() if path.suffix == ".pdf" else canonical(path)
            assert hashlib.sha256(data).hexdigest() == digest, (name, target)
            citations.append({"document": name, "source": path.relative_to(ROOT).as_posix(),
                              "sha256": digest})
    return {"date": "2026-10-08", "base_commit": "2681813154243e10cf4602f4e88514355060d379",
            "original_prime_coefficients_and_same_prime_center_retained": True,
            "new_shared_profile_to_canonical_scalar_admission": True,
            "two_sharp_factor_cutoff_corrections_retained": True,
            "growth_uniform_finite_form_retained": True,
            "analytic_upper": False, "new_actual_zero_proportion": False,
            "new_zero_free_boundary": False, "new_paper": False,
            "finite_certificate": finite(), "review_bindings": reviews,
            "cited_source_hash_bindings": citations, "links_checked": links,
            "files": list(records.values()),
            "unproved": ["canonical scalar fourth mean on the original positive-height guard",
                         "a useful original ratio upper or actual proportion",
                         "independent arithmetic certification of that mean-square"]}


if __name__ == "__main__":
    result = build()
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        assert set(sys.argv[1:]) <= {"--generate"}, "use --generate or --check"
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("PASS: finite original shifts, density, growth powers, 240 full cutoff coefficients and source bindings")

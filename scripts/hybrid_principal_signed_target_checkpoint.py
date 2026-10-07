"""Exact finite checkpoint for principal subtraction and the signed target.

The source proofs and independent reviews supply the analytic estimates.
This checks the primitive, finite tensor identities, atomic combinatorics,
and canonical source bindings. It certifies no new zeta boundary or proportion.
"""

from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib
import json
import re
import subprocess
import sys

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
P = "reviews/2026-10-08/"
PRINCIPAL = P + "hybrid-whole-prime-principal-subtraction-and-product-length-research.md"
TENSOR = P + "hybrid-whole-joint-moment-information-amplification-research-radial.md"
NOTE = "notes/471-original-principal-subtraction-and-signed-four-distinct-target.md"
ROOT_REVIEW = P + "hybrid-principal-subtraction-and-information-limit-review-root.md"
PRINCIPAL_REVIEW = P + "hybrid-whole-prime-principal-subtraction-review-radial.md"
TENSOR_REVIEWS = [
    P + "hybrid-whole-joint-moment-information-amplification-review-twisted.md",
    P + "hybrid-whole-joint-moment-information-review-compression.md",
]
NOTE_REVIEWS = [
    P + "471-principal-and-signed-four-distinct-review-twisted.md",
    P + "471-principal-and-signed-four-distinct-review-compression.md",
]
SELF = "scripts/hybrid_principal_signed_target_checkpoint.py"
OUTPUT = ROOT / "output/hybrid-principal-signed-target-checkpoint.json"
FILES = [PRINCIPAL, TENSOR, NOTE, ROOT_REVIEW, PRINCIPAL_REVIEW,
         *TENSOR_REVIEWS, *NOTE_REVIEWS, SELF]
PAIRS = {
    PRINCIPAL: [ROOT_REVIEW, PRINCIPAL_REVIEW],
    TENSOR: [ROOT_REVIEW, *TENSOR_REVIEWS],
    NOTE: NOTE_REVIEWS,
}


def canonical(path):
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def binding(name):
    data = canonical(ROOT / name)
    return {"path": name, "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data), "lines": len(data.splitlines())}


def exact_algebra():
    checked = []

    def eq(label, left, right):
        assert s.simplify(left-right) == 0, label
        checked.append(label)

    x, X, ell = s.symbols("x X ell", positive=True)
    t = s.symbols("t", real=True)
    primitive = s.exp((s.Rational(1, 2)+s.I*t)*s.log(x))/(s.Rational(1, 2)+s.I*t)
    eq("principal primitive derivative", s.diff(primitive, x),
       s.exp((-s.Rational(1, 2)+s.I*t)*s.log(x)))
    lower_exponent = (s.Rational(1, 2)+s.I*t)/2
    eq("sqrt-X lower endpoint exponent", lower_exponent, s.Rational(1, 4)+s.I*t/2)
    assert s.simplify(lower_exponent-(s.Rational(1, 4)+s.I*t)) != 0
    rho, raw, dim = X**(-s.Rational(1, 2))/ell, X**s.Rational(1, 2)/ell, X*ell
    eq("whole actual word error", rho*raw, ell**-2)
    eq("good physical crossing error", ell*rho*raw**3/dim, ell**-4)
    eq("dual-height error", X**-2*raw**4/dim, X**-1*ell**-5)

    # Two different primes give two ordered factorizations; squares give one.
    primes = [2, 3, 5, 7]
    weights = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 5), Fraction(4, 7)]
    coefficients = {}
    for p, b in zip(primes, weights):
        for q, c in zip(primes, weights):
            coefficients[p*q] = coefficients.get(p*q, Fraction())+b*c
    atomic = sum(n*c*c for n, c in coefficients.items())
    expected = 2*sum(p*b*b for p, b in zip(primes, weights))**2
    expected -= sum(p*p*b**4 for p, b in zip(primes, weights))
    assert atomic == expected
    checked.append("ordered atomic product energy")

    # Arbitrary finite Hermitian base matrices; these are not prime realizations.
    H = s.Matrix([[1, 2+s.I], [2-s.I, -2]])
    L = s.Matrix([[2, 1-s.I], [1+s.I, 1]])
    W, V = s.diag(s.Rational(1, 3), s.Rational(2, 3)), s.diag(s.Rational(1, 4), s.Rational(3, 4))
    U = s.diag(1, -1)
    m = 8
    A = s.diag(2, -2, *([0]*(m-2)))
    I = s.eye(m)
    D = A*A-I
    gamma = s.Rational(m, 2)
    tau = lambda B: s.simplify(s.trace(B)/B.rows)
    lift = lambda B: s.kronecker_product(B, I)
    Ht, Lt, Wt, Vt, Ut = s.kronecker_product(H, A), lift(L), lift(W), lift(V), lift(U)
    G, Dt, Z = H*H-W, L*L-V, (H*L+L*H)/2
    Gt, Dtt, Zt = Ht*Ht-Wt, Lt*Lt-Vt, (Ht*Lt+Lt*Ht)/2
    parity = lambda B, C, sign: (B+sign*C*B*C)/2
    for label, B, value in [
        ("fiber first", A, 0), ("fiber second", A**2, 1),
        ("fiber third", A**3, 0), ("fiber fourth", A**4, gamma),
        ("blind mean", D, 0), ("blind-Z orthogonality", D*A, 0),
        ("blind energy", D**2, gamma-1),
    ]:
        eq(label, tau(B), value)
    for i, R in enumerate([s.eye(2), W, V]):
        eq(f"center row {i}", tau(Gt*lift(R)), tau(G*R))
        for j, S in enumerate([s.eye(2), W, V]):
            eq(f"weighted high second {i},{j}", tau(lift(R)*Ht*lift(S)*Ht), tau(R*H*S*H))
    for sign in [1, -1]:
        Gj, Dj, Zj = [parity(B, U, sign) for B in [G, Dt, Z]]
        Gtj, Dtj, Ztj = [parity(B, Ut, sign) for B in [Gt, Dtt, Zt]]
        Sqj = parity(H*H, U, sign)
        eq(f"split covariance {sign}", tau(Gtj*Dtj), tau(Gj*Dj))
        eq(f"split Z energy {sign}", tau(Ztj**2), tau(Zj**2))
        eq(f"split delta-Z {sign}", tau(Dtj*Ztj), 0)
        eq(f"split gamma-Z {sign}", tau(Gtj*Ztj), 0)
        eq(f"split blind energy {sign}", tau(Gtj**2), tau(Gj**2)+(gamma-1)*tau(Sqj**2))
    for signs in product([1, -1], repeat=4):
        base, lifted = s.eye(2), s.eye(2*m)
        for sign in signs:
            base *= parity(L, U, sign)
            lifted *= parity(Lt, Ut, sign)
        eq("low parity word "+str(signs), tau(lifted), tau(base))
    a, e, c = tau(H**4), tau(L**4), tau(H*H*L*L)
    comm = H*L-L*H
    k = tau(comm.conjugate().T*comm)
    eq("whole q increment", tau(Gt**2), tau(G**2)+(gamma-1)*a)
    gap_increment = tau(H*H*U*H*H*U)
    assert gap_increment >= 0
    eq("whole gap increment", tau(Gt*Ut*Gt*Ut), tau(G*U*G*U)+(gamma-1)*gap_increment)
    eq("whole signed fourth", tau((Ht+Lt)**4), gamma*a+e+6*c-k)
    assert k <= 4*c
    assert tau((Ht+Lt)**4) >= gamma*tau(H*H)**2
    checked.extend(["commutator bound", "whole fourth lower bound", "PSD gap increment"])

    Sh, repeated = s.Rational(19, 480), s.Rational(19, 240)
    eq("repeated-to-residual offset", repeated-Sh, Sh)
    qstar = (s.sqrt(104899)-275)/15120
    assert 0 < qstar < Sh
    assert qstar > s.Rational(1, 350)
    return {
        "identities_and_inequalities": checked, "count": len(checked),
        "principal_lower_endpoint_exponent": str(lower_exponent),
        "atomic_test_energy": str(atomic),
        "finite_tensor_dimension": 2*m, "fixed_fiber_dimension": m,
        "high_repeated_limit": str(repeated), "high_square_diagonal_limit": str(Sh),
        "four_distinct_liminf_floor": str(qstar-Sh),
        "four_distinct_liminf_floor_decimal": str(s.N(qstar-Sh, 45)),
        "scope": "finite exact algebra and exponent bookkeeping only; no asymptotic prime certificate",
    }


def build():
    prior = subprocess.run([sys.executable, str(ROOT/"scripts/hybrid_whole_parity_checkpoint.py"), "--check"],
                           cwd=ROOT, check=True, capture_output=True, text=True)
    records = {name: binding(name) for name in FILES}
    review_bindings = []
    for source, reviewers in PAIRS.items():
        digest = records[source]["sha256_canonical_lf"]
        for review in reviewers:
            assert digest in canonical(ROOT/review).decode("utf-8"), (source, review)
            review_bindings.append({"source": source, "source_sha256": digest, "review": review,
                                    "review_sha256": records[review]["sha256_canonical_lf"]})
    citations, links = [], 0
    for name in FILES:
        if not name.endswith(".md"):
            continue
        content = canonical(ROOT/name).decode("utf-8")
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            if not re.search(r"\.(md|py|json|tex|pdf|lean)(#.*)?$", target):
                continue
            relative = target.split("#", 1)[0]
            assert (ROOT/name).parent.joinpath(relative).resolve().exists(), (name, target)
            links += 1
        for target, digest in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)\s*\|\s*([a-f0-9]{64})", content):
            path = (ROOT/name).parent.joinpath(target).resolve()
            assert hashlib.sha256(canonical(path)).hexdigest() == digest, (name, target)
            citations.append({"document": name, "source": path.relative_to(ROOT).as_posix(), "sha256": digest})
    return {
        "date": "2026-10-08", "base_commit": "88e86a35a3dc2c7988ec1fabe0fde6c485a1fc0b",
        "previous_checkpoint_checked": prior.stdout.strip(),
        "new_whole_actual_principal_subtraction_proved": True,
        "principal_subtraction_requires_high_fourth_bounded": False,
        "principal_subtraction_shortens_atomic_products": False,
        "new_finite_moment_information_limitation_proved": True,
        "tensor_model_realizes_original_scalar_prime_carrier": False,
        "new_high_residual_upper": False, "new_actual_zero_proportion": False,
        "new_zero_free_boundary": False, "new_paper": False,
        "old_Q_one_over_350_excluded": True,
        "finite_certificate": exact_algebra(), "links_checked": links,
        "review_bindings": review_bindings, "cited_source_hash_bindings": citations,
        "files": list(records.values()),
        "unproved": [
            "a useful signed entire four-distinct upper on the original finite carrier",
            "a reachable original high-square residual upper",
            "the remaining original internal P fourth compression budget",
            "an actual new simple-zero proportion or zero-free boundary",
            "independent certification of the imported R analytic kernel",
        ],
    }


if __name__ == "__main__":
    result = json.loads(json.dumps(build(), default=str))
    if "--check" in sys.argv:
        assert result == json.loads(OUTPUT.read_text(encoding="utf-8")), "checkpoint differs"
    else:
        OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("PASS: principal primitive, finite tensor identities, signed four-distinct offset and final review bindings")

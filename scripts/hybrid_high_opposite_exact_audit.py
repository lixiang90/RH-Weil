"""Exact cyclic-word and residue algebra for note 456; no analytic certificate."""

from collections import Counter
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md"
OUT = ROOT / "output/hybrid-high-opposite-exact-audit.json"


def binding(path):
    data = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return {"path": path.relative_to(ROOT).as_posix(),
            "sha256_canonical_lf": hashlib.sha256(data).hexdigest(),
            "canonical_utf8_bytes": len(data)}


def cyclic(word):
    return min(word[k:] + word[:k] for k in range(4))


def word_model(n):
    labels = range(n)
    target = Counter(cyclic(w) for w in itertools.product(labels, repeat=4) if len(set(w)) < 4)
    rhs = Counter()
    for p, q, r in itertools.product(labels, repeat=3):
        rhs[cyclic((p, p, q, r))] += 4
        rhs[cyclic((p, q, p, r))] += 2
    for p, q in itertools.product(labels, repeat=2):
        rhs[cyclic((p, p, q, q))] -= 2
        rhs[cyclic((p, q, p, q))] -= 1
        rhs[cyclic((p, p, p, q))] -= 8
    for p in labels:
        rhs[cyclic((p, p, p, p))] += 6
    assert dict(target) == {w: c for w, c in rhs.items() if c}
    return {"labels": n, "ordered_repeated_words": sum(target.values()),
            "cyclic_classes_checked": len(target)}


def certify():
    words = [word_model(n) for n in range(1, 7)]
    primes = [p for p in range(3, 102, 2) if all(p % d for d in range(2, int(p**0.5) + 1))]
    residue_checks = 0
    zero_progressions = 0
    for ell in primes:
        counts = Counter(p*p % ell for p in range(1, ell))
        assert max(counts.values()) <= 2
        residue_checks += ell - 1
        harmonic_majorant = 2*sum((Q(1, min(a, ell-a)) for a in range(1, ell)), Q(0))
        actual = sum((Q(1, min(p*p % ell, ell-p*p % ell)) for p in range(1, ell)), Q(0))
        assert actual <= harmonic_majorant
        # The zero-residue branch must remove exactly its zero denominator.
        for multiplier in [1, 2, 3]:
            p = ell*multiplier
            center = p*p//ell
            for xmax in [center-1, center, center+7]:
                direct = sum((Q(1, abs(p*p-ell*q)) for q in range(1, xmax+1) if q != center), Q(0))
                shifted = sum((Q(1, abs(q-center)) / ell for q in range(1, xmax+1) if q != center), Q(0))
                assert direct == shifted
                zero_progressions += 1
    # On v >= 0, d_H(v)=(v+v^2)/2; use symmetry for the full integral.
    s_flat = sum((Q(c, 2)*Q(1, 2)**(k+1)/Q(k+1) for k, c in [(2, 1), (3, 2), (4, 1)]), Q(0))
    assert s_flat == Q(19, 480)
    assert 2*s_flat == Q(19, 240)
    return {
        "status": "PASS: finite cyclic-word, residue and rational-integral algebra only",
        "cyclic_word_models": words,
        "odd_prime_moduli": primes,
        "nonzero_residue_checks": residue_checks,
        "zero_residue_progression_checks": zero_progressions,
        "flat_S_psi": str(s_flat), "flat_repeated_limit": str(2*s_flat),
        "input_read_and_hashed_from_disk": binding(INPUT),
        "script_read_and_hashed_from_disk": binding(Path(__file__).resolve()),
        "not_certified": ["infinite prime harmonic estimates and dyadic summation",
                          "finite-projection deletion and physical support bounds",
                          "full fourth moment, zero proportion or a zero-free boundary"],
    }


if __name__ == "__main__":
    result = certify()
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "cyclic_models": len(result["cyclic_word_models"]),
                      "residue_checks": result["nonzero_residue_checks"],
                      "zero_progressions": result["zero_residue_progression_checks"]}))

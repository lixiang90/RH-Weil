"""Finite exact checks for note 457; does not certify analytic moments or zeros."""

from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/hybrid-number-field-exact-audit.json"


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def split_model(p):
    for a in range(-isqrt(p), isqrt(p) + 1):
        b2 = p - a * a
        if b2 <= 0:
            continue
        b = isqrt(b2)
        if b * b == b2 and a % 2 and b % 2 == 0 and (a + b - 1) % 4 == 0:
            break
    else:
        raise AssertionError(p)
    assert gcd(a, b) == 1
    imod = (-a * pow(b, -1, p)) % p
    roots = {1: (1, 0), imod: (0, 1), p - 1: (-1, 0), -imod % p: (0, -1)}

    def chi(x):
        return roots[pow(x % p, (p - 1) // 4, p)] if x % p else (0, 0)

    jacobi = (0, 0)
    for x in range(p):
        term = mul(chi(x), chi(1 - x))
        jacobi = jacobi[0] + term[0], jacobi[1] + term[1]
    epsilon = chi(-1)[0]
    supplement = mul(chi(a - b * imod), chi(a - b * imod))[0]
    assert supplement == epsilon
    assert jacobi == (-epsilon * a, -epsilon * b)
    assert jacobi[0] ** 2 + jacobi[1] ** 2 == p
    return {"p": p, "primary_pi": [a, b], "epsilon": epsilon,
            "supplement": supplement, "exact_J": list(jacobi)}


def inert_model(p):
    def product(z, w):
        return ((z[0] * w[0] - z[1] * w[1]) % p,
                (z[0] * w[1] + z[1] * w[0]) % p)

    def power(x, n):
        result = (1, 0)
        while n:
            if n & 1:
                result = product(result, x)
            x = product(x, x)
            n //= 2
        return result

    roots = {(1, 0): (1, 0), (0, 1): (0, 1),
             (p - 1, 0): (-1, 0), (0, p - 1): (0, -1)}

    def chi(x):
        return roots[power(x, (p * p - 1) // 4)] if x != (0, 0) else (0, 0)

    trace_coefficients = []
    for a in range(p):
        total = (0, 0)
        for b in range(p):
            x = (a, b)
            value = chi(x)
            assert chi(power(x, p)) == (value[0], -value[1])
            total = total[0] + value[0], total[1] + value[1]
        assert total[1] == 0
        trace_coefficients.append(total[0])
    assert len(set(trace_coefficients[1:])) == 1
    # Trace additive character is exp(-4 pi i a/p). Its nonzero-a sum is -1.
    tau = trace_coefficients[0] - trace_coefficients[1]
    assert tau * tau == p * p
    return {"p": p, "primary_pi": [-p, 0], "exact_gauss_sum": tau,
            "normalized_gauss_square": 1}


def certify():
    split = [split_model(p) for p in range(5, 501) if is_prime(p) and p % 4 == 1]
    inert = [inert_model(p) for p in [3, 7, 11, 19, 23, 31]]
    ell = Fraction(11242271468, 10000000000)

    def exponent(d, r):
        return max(Fraction(1), (1 + (d - 1) * r) / d)

    e6, e4, e2 = (exponent(d, ell) for d in [6, 4, 2])
    assert e6 - e4 == (ell - 1) / 12
    assert e6 - e2 == (ell - 1) / 3
    for r in [Fraction(0), Fraction(1, 2), Fraction(1)]:
        assert all(exponent(d, r) == 1 for d in [2, 4, 6])
    rows = []
    for d in range(2, 21, 2):
        m = d // 2
        rho = m - 1
        assert (-1 - rho) % d == m
        order = d // gcd(d, rho)
        assert order == (m if m % 2 else 2 * m)
        rows.append({"d": d, "rho": rho, "gauss_character_order": order})
    return {
        "scope": "finite Gaussian residue/Jacobi arithmetic and rational exponents only; no analytic reflection, moment, Euler quotient or zero-free certification",
        "split_prime_models": len(split), "split_examples": split[:5],
        "all_split_supplements_checked": True,
        "inert_prime_models": inert,
        "v3_uniform_minus_alpha_counterexample": split[0],
        "reference_ell_rounded": str(ell),
        "conditional_exponents": {str(d): str(exponent(d, ell)) for d in [6, 4, 2]},
        "conditional_e6_minus_e4": str(e6 - e4),
        "conditional_e6_minus_e2": str(e6 - e2),
        "single_shift_models": rows,
        "caveat": "general claims in note 457 require its written proofs and explicit raw-family hypotheses; finite models do not prove them",
    }


if __name__ == "__main__":
    result = certify()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"finite checks passed: {result['split_prime_models']} split primes, 6 inert primes, 10 shift models")

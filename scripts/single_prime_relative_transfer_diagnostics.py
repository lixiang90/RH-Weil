"""Exact chain checks and bounded floating diagnostics for notes 513-514.

The algebra checks use reduced formal words and integer coefficients. They
verify signs and retained unit terms, not the analytic source construction.
Compact bump quadrature and finite series are numerical diagnostics, not Lean
or interval certificates. Infinite trace-class claims are proved in the notes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
NOTES = (
    "notes/513-f1-single-prime-relative-chain-transfer.md",
    "notes/514-f1-late-prime-tail-and-mixed-charge.md",
)
INVERSES = {"u": "U", "U": "u", "v": "V", "V": "v"}


def word(value: str) -> str:
    """Free invertible u,v; c is arbitrary and a is central."""
    reduced = []
    central_power = value.count("a")
    for token in value.replace("a", ""):
        if reduced and INVERSES.get(token) == reduced[-1]:
            reduced.pop()
        else:
            reduced.append(token)
    return "".join(reduced) + "a" * central_power


def chain(*terms):
    result = defaultdict(int)
    for coefficient, factors in terms:
        result[tuple(word(factor) for factor in factors)] += coefficient
    return {key: value for key, value in result.items() if value}


def add(*chains):
    return chain(*((value, key) for item in chains for key, value in item.items()))


def scale(value, item):
    return chain(*((value * coefficient, key) for key, coefficient in item.items()))


def b2(item):
    terms = []
    for (x, y, z), coefficient in item.items():
        terms += [
            (coefficient, (word(x + y), z)),
            (-coefficient, (x, word(y + z))),
            (coefficient, (word(z + x), y)),
        ]
    return chain(*terms)


def cycle(inverse, direct, test, corrected=True):
    terms = [(1, (inverse, direct + test))]
    if corrected:
        terms.append((-1, ("", test)))
    return chain(*terms)


def exact_checks():
    # Note 513 (19): v c v^{-1} remains noncommutative.
    cv = "vcV"
    lhs = add(cycle("VU", "uv", "c"),
              scale(-1, cycle("V", "v", "c")),
              scale(-1, cycle("U", "u", cv)))
    homotopy = chain((1, ("U", "u", cv)),
                     (-1, ("VU", "u", "vc")))
    if lhs != b2(homotopy):
        raise AssertionError("noncommutative corrected product identity")
    bare = add(cycle("VU", "uv", "c", False),
               scale(-1, cycle("V", "v", "c", False)),
               scale(-1, cycle("U", "u", cv, False)))
    if bare == b2(homotopy):
        raise AssertionError("bare identity incorrectly drops the unit term")
    if add(bare, chain((1, ("", cv)))) != b2(homotopy):
        raise AssertionError("bare identity has the wrong unit correction")

    # Note 514 (9): a commutes with all factors, c need not commute with v.
    original = cycle("V", "v", "c")
    central_action = chain(*(
        (coefficient, ("a" + x, y))
        for (x, y), coefficient in original.items()
    ))
    mixed_lhs = add(central_action, scale(-1, cycle("V", "v", "ca")))
    mixed_h = chain((1, ("V", "vc", "a")), (-1, ("", "c", "a")))
    if mixed_lhs != b2(mixed_h):
        raise AssertionError("central mixed homotopy")
    # Test the chain-map relation on a noncommuting 2-chain.
    test = chain((1, ("u", "c", "v")))
    delta_b = chain(*(
        (coefficient, ("a" + x, y))
        for (x, y), coefficient in b2(test).items()
    ))
    b_delta = b2(chain((1, ("au", "c", "v"))))
    if delta_b != b_delta:
        raise AssertionError("central action is not a chain map")
    return [
        "513: corrected product b2 identity in the free noncommutative algebra",
        "513: bare product retains the nonzero formal unit tensor",
        "514: central mixed b2 identity including both unit terms",
        "514: central action commutes with b2 on noncommuting factors",
    ]


def run():
    mp.mp.dps = 45
    exact = exact_checks()
    numerical = []

    def check(label, actual, expected, tolerance=mp.mpf("1e-34")):
        error = abs(actual - expected)
        if error >= tolerance:
            raise AssertionError((label, mp.nstr(error, 20)))
        numerical.append({"label": label, "absolute_error": mp.nstr(error, 18)})

    def bump(t, radius):
        if abs(t) >= radius:
            return mp.mpf(0)
        return mp.exp(-1 / (1 - (t / radius)**2))

    def coefficient(n, a):
        if n == 1:
            return -a
        return (1 - a*a) * a**(-n) if n <= 0 else mp.mpf(0)

    cutoff = 360
    for prime in (2, 3, 11, 97):
        a, length = mp.mpf(prime)**(-mp.mpf(1)/2), mp.log(prime)
        coeff = {n: coefficient(n, a) for n in range(-cutoff, 2)}
        check(f"coefficient-l1:{prime}", mp.fsum(abs(x) for x in coeff.values()), 1+2*a)
        check(f"coefficient-first-weight:{prime}",
              mp.fsum(abs(n*x) for n, x in coeff.items()), 2*a/(1-a))
        check(f"coefficient-away-from-zero:{prime}",
              mp.fsum(abs(x) for n, x in coeff.items() if n), 2*a+a*a)
        for tau in map(mp.mpf, ("-2", "-0.1", "0", "0.7", "3")):
            series = mp.fsum(x*mp.exp(-1j*n*length*tau) for n, x in coeff.items())
            rational = (1-a*mp.exp(-1j*tau*length))/(1-a*mp.exp(1j*tau*length))
            check(f"physical-shift-phase:{prime}:{tau}", series, rational)
        for r in (-3, -2, -1, 0, 1, 2, 3):
            sampled = mp.fsum(n*x*coefficient(n-r, a) for n, x in coeff.items())
            check(f"shift-diagonal-weight:{prime}:{r}", sampled,
                  0 if r == 0 else -a**abs(r))
        # Compact test with a visible prime charge, evaluated from shift traces.
        radius = mp.mpf("1.4")
        max_r = int(mp.floor(radius/length))
        trace_from_shifts = -length*mp.fsum(
            mp.fsum(n*x*coefficient(n-r, a) for n, x in coeff.items())
            * bump(-r*length, radius)
            for r in range(-max_r, max_r+1)
        )
        charge = 2*length*mp.fsum(
            a**r*bump(r*length, radius) for r in range(1, max_r+1)
        )
        check(f"compact-shift-trace-charge:{prime}", trace_from_shifts, charge)

    radius = mp.mpf("0.2")
    norm_squared = mp.quad(lambda t: bump(t, radius)**2, [-radius, 0, radius])
    late_examples = []
    for prime in (3, 11):
        a, length = mp.mpf(prime)**(-mp.mpf(1)/2), mp.log(prime)
        if length <= 2*radius:
            raise AssertionError("late-prime support condition")

        def shifted_test(t):
            return (bump(t-length, radius)+bump(t+length, radius))/2

        mixed_at_first = mp.quad(
            lambda t: bump(t, radius)*shifted_test(length-t),
            [-radius, 0, radius],
        )
        check(f"late-mixed-first-sample:{prime}", mixed_at_first, norm_squared/2)
        for n in (2, 3):
            value = mp.quad(
                lambda t: bump(t, radius)*shifted_test(n*length-t),
                [-radius, 0, radius],
            )
            check(f"late-mixed-vanishing-sample:{prime}:{n}", value, 0)
        # Independently sum the squared physical output-block coefficients.
        sampled_hs = length*norm_squared*(
            a*a+(1-a*a)**2*mp.fsum(j*a**(2*j) for j in range(1, cutoff+1))
        )
        check(f"late-hs-geometric-energy:{prime}", sampled_hs,
              2*length*norm_squared/prime)
        mixed_charge = 2*length*a*mixed_at_first
        check(f"late-mixed-charge:{prime}", mixed_charge, length*a*norm_squared)
        if mixed_charge <= 0 or bump(length, radius) != 0:
            raise AssertionError("zero original / positive mixed charge")
        late_examples.append({
            "prime": prime, "original_charge": "0 (compact support)",
            "mixed_charge": mp.nstr(mixed_charge, 24),
            "trace_norm_lower_bound": mp.nstr(length*a/mp.e, 24),
            "hs_norm_squared": mp.nstr(sampled_hs, 24),
        })

    return {
        "schema": "rh-weil-single-prime-transfer-diagnostics-v1",
        "status": "PASS",
        "notes_sha256_normalized_lf": {
            path: hashlib.sha256((ROOT/path).read_text(encoding="utf-8").encode()).hexdigest()
            for path in NOTES
        },
        "exact_formal_word_checks": exact,
        "numerical_checks": numerical,
        "numerical_check_count": len(numerical),
        "working_decimal_digits": mp.mp.dps,
        "series_cutoff": cutoff,
        "maximum_observed_error": max(
            (mp.mpf(item["absolute_error"]) for item in numerical), default=mp.mpf(0)
        ).__str__(),
        "late_compact_bump_examples": late_examples,
        "scope": [
            "Exact checks verify formal algebra identities and signs only.",
            "Floating finite series and quadrature are not interval or Lean proofs.",
            "Actual-source descent, S1 bounds, infinite-prime divergence, and HH1 nonzero detection are proved in notes 513-514.",
            "No new zero proportion, zero-free bound, or RH proof.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(json.dumps({
        "status": result["status"],
        "exact_checks": len(result["exact_formal_word_checks"]),
        "numerical_checks": result["numerical_check_count"],
        "maximum_observed_error": result["maximum_observed_error"],
    }, ensure_ascii=False))

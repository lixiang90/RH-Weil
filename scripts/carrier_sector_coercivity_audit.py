#!/usr/bin/env python3
"""Exact finite audits for note 260; stdlib only, no asymptotic inference.

Run: python scripts/carrier_sector_coercivity_audit.py

Independent routes compare physical centered convolution, Laurent-sector
enumeration, closed sector formulas, primitive integration, distance kernels,
and an explicit fourfold formula. All arithmetic uses fractions.Fraction.
"""

from fractions import Fraction as F
from itertools import product
from random import Random


def measure(items):
    out = {}
    for x, a in items:
        x, a = F(x), F(a)
        out[x] = out.get(x, F(0)) + a
    return {x: a for x, a in out.items() if a}


def add(*mus):
    return measure((x, a) for mu in mus for x, a in mu.items())


def scale(mu, a):
    return measure((x, a * b) for x, b in mu.items())


def reflect(mu):
    return measure((-x, a) for x, a in mu.items())


def convolve(mu, nu):
    return measure((x + y, a * b) for x, a in mu.items()
                   for y, b in nu.items())


def mass(mu):
    return sum(mu.values(), F(0))


def first(mu):
    return sum((x * a for x, a in mu.items()), F(0))


def distance(mu):
    """Collision functional, defined even when mass(mu) is nonzero."""
    return -sum((a * b * abs(x - y) for x, a in mu.items()
                 for y, b in mu.items()), F(0)) / 2


def primitive_energy(mu):
    """Independent integration of the step primitive of a zero-mass measure."""
    assert mass(mu) == 0, "The primitive needs zero total mass."
    xs = sorted(mu)
    cumulative, result = F(0), F(0)
    for i in range(len(xs) - 1):
        cumulative += mu[xs[i]]
        result += cumulative ** 2 * (xs[i + 1] - xs[i])
    return result


def fourfold_energy(rho):
    assert mass(rho) == 0
    return -sum((a * b * c * d * abs(x + y - z - w)
                 for (x, a), (y, b), (z, c), (w, d)
                 in product(rho.items(), repeat=4)), F(0)) / 2


def centered(mu, L):
    """Physical k_(L+u) integration; does not use a sector formula."""
    return measure((x, value) for u, a in mu.items()
                   for x, value in ((L + u, a / 2),
                                    (-L - u, a / 2), (F(0), -a)))


def direct_response(rho, tau, L):
    r = centered(rho, L)
    return convolve(convolve(r, r), centered(tau, L))


def enumerate_sectors(rho, tau):
    """Expand elementary 3-choice Laurent atoms, independent of closed forms."""
    elementary = []
    for mu in (rho, rho, tau):
        terms = []
        for u, a in mu.items():
            terms.extend(((1, u, a / 2), (0, F(0), -a),
                          (-1, -u, a / 2)))
        elementary.append(terms)
    buckets = {q: [] for q in range(-3, 4)}
    for a, b, c in product(*elementary):
        buckets[a[0] + b[0] + c[0]].append(
            (a[1] + b[1] + c[1], a[2] * b[2] * c[2]))
    return {q: measure(items) for q, items in buckets.items()}


def closed_sectors(rho, tau):
    M, T = mass(rho), mass(tau)
    rr = convolve(rho, rho)
    rb = convolve(rho, reflect(rho))
    delta = {F(0): F(1)}
    out = {
        3: scale(convolve(rr, tau), F(1, 8)),
        2: add(scale(rr, -T / 4),
               scale(convolve(rho, tau), -M / 2)),
        1: add(scale(convolve(rr, reflect(tau)), F(1, 8)),
               scale(rho, M * T), scale(tau, M * M / 2),
               scale(convolve(rb, tau), F(1, 4))),
        0: add(scale(convolve(rho, reflect(tau)), -M / 2),
               scale(convolve(reflect(rho), tau), -M / 2),
               scale(delta, -T * M * M), scale(rb, -T / 2)),
    }
    out.update({-q: reflect(out[q]) for q in (1, 2, 3)})
    return out


def reconstruct(sectors, L):
    return measure((q * L + x, a) for q, mu in sectors.items()
                   for x, a in mu.items())


def audit_pair(alpha, beta, L):
    rho = add(alpha, scale(beta, -1))
    A, B, M = mass(alpha), mass(beta), mass(rho)
    H = max((abs(x) for x in set(alpha) | set(beta)), default=F(0))
    assert 6 * H < L
    collision, numerator, balanced_energies = F(0), F(0), []
    for tau in (alpha, beta):
        enumerated = enumerate_sectors(rho, tau)
        closed = closed_sectors(rho, tau)
        assert enumerated == closed, "Laurent enumeration != closed sectors"
        physical = direct_response(rho, tau, L)
        assert reconstruct(enumerated, L) == physical
        actual = primitive_energy(physical)
        assert distance(physical) == actual
        numerator += actual
        collision += sum((distance(mu) for mu in closed.values()), F(0))
        if M == 0:
            es = {q: primitive_energy(mu) for q, mu in closed.items()}
            assert all(es[q] == distance(closed[q]) for q in es)
            Er = primitive_energy(convolve(rho, rho))
            assert Er == fourfold_energy(rho)
            assert Er == primitive_energy(convolve(rho, reflect(rho)))
            T = mass(tau)
            fixed = es[-2] + es[0] + es[2]
            assert fixed == F(3, 8) * T * T * Er
            assert actual == sum(es.values(), F(0))
            assert actual >= F(3, 8) * T * T * Er
            if all(a >= 0 for a in tau.values()):
                assert actual <= F(11, 16) * T * T * Er
            balanced_energies.append(Er)
    d1, a1, b1 = first(rho), first(alpha), first(beta)
    main = F(63, 16) * (L * M**4 * (A*A + B*B)
                        + F(2, 3) * M**3 * (A*A + B*B) * d1
                        + F(1, 3) * M**4 * (A*a1 + B*b1))
    assert numerator == main + collision, "Note 259 carrier identity failed"
    if M == 0:
        assert numerator == collision
        lower = F(3, 8) * (A*A + B*B) * balanced_energies[0]
        assert numerator >= lower
        if all(a >= 0 for mu in (alpha, beta) for a in mu.values()):
            upper = F(11, 16) * (A*A + B*B) * balanced_energies[0]
            assert numerator <= upper
    raw = primitive_energy(centered(alpha, L))
    raw += primitive_energy(centered(beta, L))
    return numerator, raw


def audit_centered_perturbation(alpha, beta, L):
    """Note 260-C: independent physical-measure checks for positive sources."""
    assert all(a >= 0 for mu in (alpha, beta) for a in mu.values())
    A, B = mass(alpha), mass(beta)
    assert B > 0
    M, K = A - B, A * A + B * B
    H = max((abs(x) for x in set(alpha) | set(beta)), default=F(0))
    assert 6 * H < L
    zeta = add(alpha, scale(beta, -A / B))
    assert mass(zeta) == 0
    Ezeta = primitive_energy(zeta)
    Ezeta2 = primitive_energy(convolve(zeta, zeta))
    assert Ezeta2 == fourfold_energy(zeta)
    rzeta = centered(zeta, L)
    rbeta = centered(beta, L)
    v = scale(rbeta, M / B)
    r = centered(add(alpha, scale(beta, -1)), L)
    assert r == add(rzeta, v)
    baseline_energy, first_energy, second_energy, D = [F(0)] * 4
    for tau in (alpha, beta):
        channel = centered(tau, L)
        actual = convolve(convolve(r, r), channel)
        baseline = convolve(convolve(rzeta, rzeta), channel)
        first_change = scale(convolve(convolve(rzeta, v), channel), 2)
        second_change = convolve(convolve(v, v), channel)
        difference = add(actual, scale(baseline, -1))
        assert difference == add(first_change, second_change)
        for mu in (baseline, first_change, second_change):
            assert primitive_energy(mu) == distance(mu)
        baseline_energy += primitive_energy(baseline)
        first_energy += primitive_energy(first_change)
        second_energy += primitive_energy(second_change)
        D += primitive_energy(channel)
    assert F(3, 8) * K * Ezeta2 <= baseline_energy
    assert baseline_energy <= F(11, 16) * K * Ezeta2
    assert first_energy <= 32 * M * M * K * Ezeta
    assert second_energy <= 16 * M**4 * D
    assert (L - H) * K / 2 <= D <= (L + H) * K / 2


def main():
    delta = {F(0): F(1)}
    k = centered(delta, F(1))
    triple = convolve(convolve(k, k), k)
    expected = [F(1, 8), F(-3, 4), F(15, 8), F(-5, 2),
                F(15, 8), F(-3, 4), F(1, 8)]
    assert [triple[F(q)] for q in range(-3, 4)] == expected
    assert primitive_energy(triple) == distance(triple) == F(63, 16)

    cases = [
        (measure([(F(1, 3), 1)]), measure([(F(-1, 3), 1)])),
        (measure([(-1, F(2, 3)), (F(1, 2), F(1, 3))]),
         measure([(F(-1, 2), F(1, 4)), (1, F(3, 4))])),
        (measure([(-1, F(1, 7)), (0, F(3, 7)), (1, F(3, 7))]),
         measure([(F(-2, 3), F(5, 11)), (F(2, 3), F(6, 11))])),
        (measure([(-1, F(2, 3)), (F(1, 2), F(2, 3))]),
         measure([(F(-1, 2), F(1, 5)), (1, F(3, 5))])),
        # Signed source cases test algebra and energy, not positivity contraction.
        (measure([(-1, 2), (0, -1)]), measure([(0, F(3, 2)), (1, F(-1, 2))])),
        (measure([(-1, 3), (0, -1)]), measure([(0, F(3, 2)), (1, F(-1, 2))])),
        (delta, delta),
    ]
    rng = Random(260)
    grid = [F(i, 3) for i in range(-3, 4)]
    for i in range(18):
        ax, bx = rng.sample(grid, 3), rng.sample(grid, 3)
        aw, bw = [rng.randint(1, 9) for _ in ax], [rng.randint(1, 9) for _ in bx]
        alpha = measure(zip(ax, (F(a, sum(aw)) for a in aw)))
        beta = measure(zip(bx, (F(b, sum(bw)) for b in bw)))
        if i % 3 == 2:
            alpha = scale(alpha, F(5, 3))
        cases.append((alpha, beta))
    balanced, perturbations = 0, 0
    for alpha, beta in cases:
        audit_pair(alpha, beta, F(20))
        balanced += mass(alpha) == mass(beta)
        if all(a >= 0 for mu in (alpha, beta) for a in mu.values()):
            audit_centered_perturbation(alpha, beta, F(20))
            perturbations += 1

    h, L = F(2, 3), F(13)
    numerator, raw = audit_pair({h: F(1)}, {-h: F(1)}, L)
    assert numerator == 5 * h and raw == L
    J4 = numerator / (16 * raw)
    assert J4 == 5 * h / (16 * L) == F(5, 312)
    print("PASS: exact carrier-sector coercivity audit (stdlib Fraction)")
    print("Carrier masses and Brownian constant: 63/16")
    print(f"General rational cases: {len(cases)}; balanced cases: {balanced}")
    print("Checked: direct convolution = enumerated sectors = closed sector formulas")
    print("Checked: primitive energy = distance energy; balanced fourfold energy")
    print("Checked: note 259 main identity and balanced bounds 3/8, 11/16")
    print(f"Checked: note 260-C perturbation and local raw bounds ({perturbations} positive cases)")
    print("Perturbation budgets: first <=32 M^2 K E(zeta); second <=16 M^4 D")
    print(f"Atomic mass-only obstruction: h={h}, L={L}, Q={numerator}, D={raw}, J4={J4}")
    print("Finite exact checks only; no asymptotic or RH/GRH claim follows from them.")


if __name__ == "__main__":
    main()

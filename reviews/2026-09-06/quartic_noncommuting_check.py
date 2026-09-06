# Independent finite regression supplied by Pauli; not an asymptotic proof.
import random
import sympy as sp


def main():
    rng = random.Random(20260906)
    sigmas = (
        sp.Integer(-3),
        sp.Rational(-29, 10),
        sp.Integer(-1),
        sp.Integer(0),
        sp.Rational(1, 8),
        sp.Rational(749, 1000),
    )
    checked = noncommuting = 0
    minima = [None, None]

    for d in range(1, 6):
        for case in range(18):
            rank = rng.randrange(d + 1)
            U = sp.Matrix(
                d, rank,
                lambda i, j: sp.Rational(rng.randrange(-3, 4), 3),
            )
            P = U * U.T  # Exactly positive semidefinite.

            # Unit lower triangular: invertible with determinant 1.
            V = sp.eye(d)
            for i in range(d):
                for j in range(i):
                    V[i, j] = sp.Rational(rng.randrange(-3, 4), 2)

            qdiag = [
                sp.Rational(rng.choice([-7, -2, 0, 1, 5]), 3)
                for _ in range(d)
            ]
            Q = V * sp.diag(*qdiag) * V.T
            G = P + Q
            noncommuting += int(P * Q != Q * P)

            s = (
                max(sp.Integer(P.rank()), sp.trace(P))
                + sp.Rational(case % 3, 5)
            )
            # Sylvester's law gives n_+(Q) exactly from qdiag.
            b = (
                sp.Integer(sum(1 for q in qdiag if q > 0))
                + sp.Rational(case % 4, 7)
            )
            N = sp.Rational(d + case % 3, 2)
            E1 = (
                max(sp.Integer(0), s + 2*b - N)
                + sp.Rational(case % 2, 9)
            )
            D = s + b
            # E0 = E1 also satisfies tr(P) + 2*b <= N + E0.

            for sigma in sigmas:
                a = 1 - sigma
                L = sp.trace(
                    -G**4 + 4*G**3
                    - (6 - 2*sigma)*G**2 + 8*a*G
                ) / N

                # Equivalent forms of the two finite bounds,
                # computed directly from tr(p_sigma(G)).
                lower_s = (L - 4*a*(1 + E1/N)) / a**2
                lower_d = (
                    L - a*(3 + sigma)*(1 + E1/N)
                ) / (2*a**2)

                margins = [s/N - lower_s, D/N - lower_d]
                assert all(v >= 0 for v in margins), (
                    d, case, sigma, margins
                )
                minima = [
                    v if old is None else min(v, old)
                    for v, old in zip(margins, minima)
                ]
                checked += 1

    assert (checked, noncommuting) == (540, 58)
    assert minima == [
        sp.Rational(3077, 6480),
        sp.Rational(1, 5),
    ]
    print(
        f"checks={checked}; configurations=90; "
        f"noncommuting={noncommuting}"
    )
    print("minimum margins:", minima)


if __name__ == "__main__":
    main()

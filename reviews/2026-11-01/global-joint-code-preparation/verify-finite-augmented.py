"""Independent finite signed-augmentation kernel, CODE PREPARATION ONLY.

No source reads, writes, actual run or consumer import at module scope. A future
authenticated controller MUST independently load/pin raw old centers and the one
root-accepted packet. This kernel alone is NOT a runnable scientific verifier.
It verifies the EXACT selected target by interval inertia, rather than trusting
the producer's inverse/solve/Schur output or its reported finite error.
"""
from fractions import Fraction

P = 1024
SCALE = 1 << P
WIDTH = 16384
EPSILON = Fraction(1, 1 << 226)
PADDING = Fraction(1, 1 << 221)
LAMBDA = Fraction(1, 1 << 224) + 2 * Fraction(1, 1 << 216)
DFLOOR = Fraction(15, 64) - Fraction(896, 1 << 170) - Fraction(1, 1 << 440)
ACTIVE_INVERSE = Fraction(209, 32)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def integer(x):
    require(type(x) is int and abs(x).bit_length() <= WIDTH, "INTEGER_WIDTH")
    return x


def ceiling(a, b):
    require(b > 0, "DENOMINATOR")
    return -((-a) // b)


def point(x):
    q = Fraction(x)
    require(q.denominator.bit_length() <= WIDTH and abs(q.numerator).bit_length() <= WIDTH,
            "POINT_WIDTH")
    a = integer(q.numerator * SCALE)
    return integer(a // q.denominator), integer(ceiling(a, q.denominator))


def add(a, b):
    return integer(a[0] + b[0]), integer(a[1] + b[1])


def minus(a, b):
    return integer(a[0] - b[1]), integer(a[1] - b[0])


def negative(a):
    return integer(-a[1]), integer(-a[0])


def times(a, b):
    v = [integer(x * y) for x in a for y in b]
    return integer(min(v) // SCALE), integer(ceiling(max(v), SCALE))


def squared(a):
    hi = max(integer(a[0] * a[0]), integer(a[1] * a[1]))
    lo = 0 if a[0] <= 0 <= a[1] else min(a[0] * a[0], a[1] * a[1])
    return integer(lo // SCALE), integer(ceiling(hi, SCALE))


def divided(a, b):
    require(b[1] < 0 or b[0] > 0, "DIVISOR_CONTAINS_ZERO")
    if b[1] < 0:
        return divided(negative(a), negative(b))
    candidates = [(integer(x * SCALE), y) for x in a for y in b]
    return (integer(min(x // y for x, y in candidates)),
            integer(max(ceiling(x, y) for x, y in candidates)))


def transpose(a):
    return [list(x) for x in zip(*a)]


def product(a, b, poll):
    require(a and b and len(a[0]) == len(b), "PRODUCT_SHAPE")
    bt = transpose(b)
    out = []
    for row in a:
        result = []
        for j, col in enumerate(bt):
            if j % 8 == 0:
                poll()
            q = (0, 0)
            for k, (x, y) in enumerate(zip(row, col)):
                if k % 64 == 0:
                    poll()
                q = add(q, times(x, y))
            result.append(q)
        out.append(result)
    return out


def symmetric_enclosure(a):
    require(len(a) == len(a[0]), "SQUARE_SHAPE")
    # Exact intended matrix is symmetric: an intersection of independently
    # valid enclosures is a valid enclosure; an empty intersection is fatal.
    for i in range(len(a)):
        for j in range(i):
            z = max(a[i][j][0], a[j][i][0]), min(a[i][j][1], a[j][i][1])
            require(z[0] <= z[1], "SYMMETRY_INCONSISTENCY")
            a[i][j] = a[j][i] = z
    return a


def signed_ldl(matrix, active, poll, emit=lambda *args: None):
    """Eliminate -H first; its Schur complement is the exact T congruence."""
    a = [row[:] for row in matrix]
    n = len(a)
    require(0 < active < n and all(len(row) == n for row in a), "SIGNED_LDL_SHAPE")
    for k in range(n):
        poll()
        d = a[k][k]
        expected = "NEGATIVE_ACTIVE" if k < active else "POSITIVE_TARGET"
        emit(k, expected, d)
        if k < active:
            if d[1] >= 0:
                return dict(status="UNRESOLVED_ACTIVE_BLOCK", pivot=k, enclosure=d)
        elif d[0] <= 0:
            status = "SUFFICIENT_TARGET_REJECTED" if d[1] < 0 else "TARGET_INTERVAL_UNRESOLVED"
            return dict(status=status, pivot=k, enclosure=d,
                        actualNegativeLretClaim=False, actualNegativeQClaim=False)
        for i in range(k + 1, n):
            if i % 8 == 0:
                poll()
            factor = divided(a[i][k], d)
            for j in range(i, n):
                if j % 32 == 0:
                    poll()
                update = divided(squared(a[i][k]), d) if i == j else times(factor, a[j][k])
                a[j][i] = a[i][j] = minus(a[j][i], update)
    return dict(status="EXACT_SELECTED_TARGET_POSITIVE", negativeActivePivots=active,
                positiveTargetPivots=n - active, intervalBits=P,
                consumerImported=False, inverseRead=False, GoalComplete=False)


def assemble_sector(d, g, covariance, c0, blocks, poll):
    """All arguments are ORIGINAL raw point forms, NOT producer results.

    d is raw D diagonal for one parity. g=Graw, c0=Ahat+Jhat+Uhat,
    covariance=Bhat-Ahat D^-1 Ahat. blocks are the five accepted raw centers.
    Caller must derive/pin these independently from original files, not import
    a consumer loader/assembled matrix or trust a claimed center dictionary.
    """
    m = len(d)
    require(0 < m <= 224 and all(Fraction(v) > 0 for v in d), "RAW_METRIC")
    for name, a in [("G", g), ("Dh", covariance), ("C0", c0)] + list(blocks.items()):
        require(len(a) == m and all(len(row) == m for row in a), "INPUT_SHAPE_" + name)
    require(set(blocks) == {"CX", "FX", "FY", "XY", "YY"}, "FIVE_BLOCKS")
    z = (0, 0)
    ds = [point(v) for v in d]
    g = [[point(v) for v in row] for row in g]
    c0 = [[point(v) for v in row] for row in c0]
    dh = [[point(v) for v in row] for row in covariance]
    bb = {name: [[point(v) for v in row] for row in a] for name, a in blocks.items()}
    ident = [[point(int(i == j)) for j in range(m)] for i in range(m)]
    s0 = [[add(g[i][j], ds[i] if i == j else z) for j in range(m)] for i in range(m)]
    b0 = [[divided(s0[i][j], ds[i]) for j in range(m)] for i in range(m)]
    w = b0 + [[minus(b0[i][j], ident[i][j]) for j in range(m)] for i in range(m)] + b0
    cg = [[add(c0[i][j], g[i][j]) for j in range(m)] for i in range(m)]
    kh = product(transpose(b0), product(cg, b0, poll), poll)
    gdg = product(g, [[divided(g[i][j], ds[i]) for j in range(m)] for i in range(m)], poll)
    for i in range(m):
        for j in range(m):
            kh[i][j] = minus(minus(kh[i][j], g[i][j]), gdg[i][j])
    metric = product(transpose(b0), [[times(ds[i], b0[i][j]) for j in range(m)]
                                   for i in range(m)], poll)
    # Kbar raw; covariance is true-Gram approximation, not Fstar*Fstar.
    tiles = [[dh, bb["FX"], bb["FY"]],
             [transpose(bb["FX"]), bb["CX"], bb["XY"]],
             [transpose(bb["FY"]), transpose(bb["XY"]), bb["YY"]]]
    kbar = [[tiles[i // m][j // m][i % m][j % m] for j in range(3 * m)]
            for i in range(3 * m)]
    for i in range(3 * m):
        kbar[i][i] = add(kbar[i][i], times(point(PADDING), ds[i % m]))
    d0 = point(DFLOOR)
    h = [[divided(kbar[i][j], d0) for j in range(2 * m)] for i in range(2 * m)]
    for i in range(m):
        h[i][i] = add(h[i][i], times(point(ACTIVE_INVERSE), ds[i]))
        for j in range(m):
            h[m + i][m + j] = add(h[m + i][m + j], g[i][j])
        h[m + i][m + i] = add(h[m + i][m + i], times(point(1 + EPSILON), ds[i]))
    kw = product(kbar, w, poll)
    energy = product(transpose(w), kw, poll)
    base = [[minus(minus(kh[i][j], times(point(LAMBDA), metric[i][j])),
                   divided(energy[i][j], d0)) for j in range(m)] for i in range(m)]
    r = [[divided(kw[i][j], d0) for j in range(m)] for i in range(2 * m)]
    aug = [[negative(h[i][j]) for j in range(2 * m)] + r[i] for i in range(2 * m)]
    rt = transpose(r)
    aug += [rt[i] + base[i] for i in range(m)]
    return symmetric_enclosure(aug)


def verify_sector(d, g, covariance, c0, blocks, *, poll, emit=lambda *args: None):
    require(callable(poll), "MANDATORY_EXTERNAL_BUDGET_POLL")
    return signed_ldl(assemble_sector(d, g, covariance, c0, blocks, poll),
                      2 * len(d), poll, emit)


if __name__ == "__main__":
    raise SystemExit("CODE_PREPARATION_ONLY: authenticated independent loader/controller/reviews still required")

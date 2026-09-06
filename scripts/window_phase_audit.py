"""Finite independent integral checks for note 327; not an asymptotic proof."""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 60
ROOT = Path(__file__).resolve().parents[1]
b = 1 / mp.sqrt(2)
sinc_b = mp.sin(b) / b


def laplace(A, z):
    return (
        z * mp.sinh(z * A) * mp.cos(b)
        + b / A * mp.cosh(z * A) * mp.sin(b)
    ) / (A * sinc_b * (z * z + (b / A) ** 2))


def theta(A, e, d, delta):
    G = (laplace(A, 2 * e) + 1) / 2
    H = (laplace(A, 2 * d) - 1) / 2
    cross = mp.im(laplace(A, e + d + 1j * delta)
                  + laplace(A, d - e + 1j * delta)) / 2
    return cross / mp.sqrt(G * H)


cases = []
for A, e, d, delta in [(8, ".27", ".15", ".73"), (20, ".15", ".27", "-.4"),
                       (12, ".2", ".2", ".3"), (9, ".4", ".15", "0")]:
    A, e, d, delta = map(mp.mpf, (A, e, d, delta))
    density = lambda u: mp.cos(b * u / A) / (2 * A * sinc_b)
    G = mp.quad(lambda u: density(u) * mp.cosh(e * u) ** 2, [-A, 0, A])
    H = mp.quad(lambda u: density(u) * mp.sinh(d * u) ** 2, [-A, 0, A])
    cross = mp.quad(
        lambda u: density(u) * mp.sin(delta * u) * mp.cosh(e * u) * mp.sinh(d * u),
        [-A, 0, A],
    )
    error = abs(cross / mp.sqrt(G * H) - theta(A, e, d, delta))
    assert error < mp.mpf("1e-45")
    cases.append({"A": str(A), "e": str(e), "d": str(d), "Delta": str(delta),
                  "absolute_error": mp.nstr(error, 10)})

L, width, e, d, delta = map(mp.mpf, ("2000", "60", ".27", ".15", ".73"))
average = mp.quad(lambda y: theta((L - y) / 2, e, d, delta) ** 2,
                  list(mp.linspace(0, width, 25))) / width
limit = 2 * e * d / ((e + d) ** 2 + delta ** 2)
result = {
    "scope": "60-digit finite integral checks only; no actual zero data or asymptotic certification.",
    "independent_integral_cases": cases,
    "average_example": {
        "L": str(L), "H": str(width), "e": str(e), "d": str(d), "Delta": str(delta),
        "exact_kernel_numeric_average": mp.nstr(average, 20),
        "leading_average": mp.nstr(limit, 20),
        "difference": mp.nstr(average - limit, 15),
    },
}
target = ROOT / "reviews/2026-09-06/window-phase-integral-check.json"
target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(result, indent=2))

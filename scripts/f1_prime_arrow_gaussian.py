"""Exact Gaussian moment diagnostics for note 407; not a Lean or analytic proof."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]

def main():
    r, q = s.symbols("r q", positive=True)
    u = s.symbols("u", real=True)
    pi = s.pi
    eta = lambda t: pi*t**2*(pi*t**2-s.Rational(3, 2))*s.exp(-pi*t**2)
    poly = s.Poly(s.expand(pi*q**2*r**2*(pi*q**2*r**2-s.Rational(3, 2))
                         *pi*r**2*(pi*r**2-s.Rational(3, 2))), r)
    # Integral_0^infty r^(k+t-1) exp(-a*r^2) dr = Gamma((k+t)/2)/(2*a^((k+t)/2)).
    def moment(t):
        return s.factor(sum(c*s.gamma(s.Rational(k[0]+t, 2))
                              /(2*(pi*(q**2+1))**s.Rational(k[0]+t, 2))
                            for k, c in poly.terms()))
    mu = 2*moment(1)
    expected_mu = -3*q**2*(6*q**4-23*q**2+6)/(16*(q**2+1)**s.Rational(9,2))
    mc2 = s.factor(2*s.zeta(2)*moment(2))
    expected_mc2 = -pi*q**2*(q**2-3)*(3*q**2-1)/(4*(q**2+1)**5)
    assert s.simplify(mu-expected_mu) == 0
    assert s.simplify(mc2-expected_mc2) == 0
    assert s.expand(6*(u-4)**2+25*(u-4)+10-(6*u**2-23*u+6)) == 0
    derivative = -2*pi*r*s.exp(-pi*r**2)*(pi*r**2-3)*(pi*r**2-s.Rational(1,2))
    assert s.simplify(s.diff(eta(r),r)-derivative) == 0
    assert s.simplify(mu.subs(q,2)+3/(250*s.sqrt(5))) == 0
    report = {
        "status": "passed_exact_symbolic_checks",
        "scope": "Gaussian moment and polynomial identities only. Poisson summation, traces, categories and RH are not certified.",
        "sympy_version": s.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "positive_q": True,
        "mu_q": str(mu),
        "mellin_C_q_at_2": str(mc2),
        "mellin_P_q_at_2": str(s.factor(2*mc2)),
        "mellin_Z_q_at_2": str(s.factor(4*mc2)),
        "mu_2": str(s.simplify(mu.subs(q,2))),
        "polynomial_identity": "6*u^2-23*u+6 = 6*(u-4)^2+25*(u-4)+10",
        "eta_derivative": str(derivative),
        "identities_checked": 5,
    }
    target = ROOT/"reviews/2026-09-20/f1-prime-arrow-gaussian.json"
    target.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__ == "__main__":
    main()

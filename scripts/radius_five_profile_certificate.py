"""Exact profile positivity and conditional ratio check; does not verify h."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

from periodic_window_quadratic_certificate import SCALE, asiv, sin_iv, sinc_iv

ROOT=Path(__file__).resolve().parents[1]


def main():
    source=ROOT/"reviews/2026-09-08/radius-five-rational-profile-candidate.json"
    proposal=json.loads(source.read_text(encoding="utf-8"))
    t=[asiv(Fraction(item["t"])) for item in proposal["terms"]]
    y=[asiv(Fraction(item["y"])) for item in proposal["terms"]]
    a=asiv(2).sqrt()
    ma=sinc_iv(a)
    cb=1-2*sin_iv(a/4).square()
    c0=asiv(Fraction(3,2))-cb/ma
    p0min=cb/ma
    p0max=1/ma
    m=[sinc_iv(x) for x in t]
    k=[(sinc_iv(x-a)+sinc_iv(x+a))/(2*ma) for x in t]
    factors=[x.square()/(x.square()-2) for x in t]
    absiv=lambda x:asiv(Fraction(x.absupper(),SCALE))
    density_floor=p0min-sum((absiv(y[i])*factors[i]*(1+absiv(m[i])*p0max)
                            for i in range(len(t))),asiv(0))
    assert density_floor.lo*4>3*SCALE
    qcost=asiv(0)
    for i,s in enumerate(t):
        for j in range(i,len(t)):
            u=t[j]
            entry=factors[j]*((sinc_iv(s-u)+sinc_iv(s+u))/2-m[j]*k[i])
            qcost=qcost+(1 if i==j else 2)*y[i]*y[j]*entry
        if (i+1)%20==0:
            print(f"certified {i+1}/{len(t)} Riesz Gram rows",flush=True)
    baseline=c0-qcost
    alpha=asiv(Fraction(proposal["alpha"]))
    eta=asiv(Fraction(proposal["eta"]))
    assert 0<=alpha.lo<=alpha.hi<SCALE and eta.lo>=0
    conditional=(baseline-eta)/(1-alpha)
    threshold=Fraction(673415,1000000)
    assert conditional.lo*threshold.denominator>threshold.numerator*SCALE
    output=dict(
        status="PASS: exact density and conditional-ratio arithmetic only",
        scope="The global V5 + eta*gap/(2*pi) + coboundary >= alpha is NOT verified; no actual zero improvement follows yet",
        arithmetic="10^-80 outward integer intervals using independently reviewed trigonometric primitives",
        source=source.name,terms=len(t),radius=proposal["radius"],
        alpha=proposal["alpha"],eta=proposal["eta"],
        mass="exactly 1 by zero mean of each Riesz representer and normalization of p0",
        strict_density_lower_bound="3/4",density_floor=density_floor.report(),
        window_penalty=qcost.report(),baseline=baseline.report(),
        conditional_ratio=conditional.report(),
        strict_conditional_lower_bound=str(threshold),
        comparison_target=proposal["comparison_target"],
        open_input="a bounded all-gap subaction for this exact profile and these parameters")
    (ROOT/"reviews/2026-09-08/radius-five-profile-certificate.json").write_text(
        json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print("PASS: p > 3/4, integral p = 1, conditional ratio > 0.673415.")
    print("OPEN: global bounded h. This is not an actual zero proportion.")


if __name__=="__main__":
    main()

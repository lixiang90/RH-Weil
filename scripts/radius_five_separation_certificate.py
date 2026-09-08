"""Exact real-kernel envelopes for the fixed 90-term profile, not a subaction."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

from periodic_window_quadratic_certificate import SCALE, asiv, sin_iv, sinc_iv

ROOT=Path(__file__).resolve().parents[1]


def main():
    proposal=json.loads((ROOT/"reviews/2026-09-08/radius-five-rational-profile-candidate.json").read_text())
    t=[asiv(Fraction(v["t"])) for v in proposal["terms"]]
    y=[asiv(Fraction(v["y"])) for v in proposal["terms"]]
    a=asiv(2).sqrt()
    ma=sinc_iv(a)
    pmin=(1-2*sin_iv(a/4).square())/ma
    pmax=1/ma
    st=[sin_iv(x/2) for x in t]
    ct=[1-2*sin_iv(x/4).square() for x in t]
    mt=[st[i]/(t[i]/2) for i in range(len(t))]
    tt=[x.square() for x in t]
    z=[y[i]*tt[i]/(tt[i]-2) for i in range(len(t))]
    absiv=lambda x:asiv(Fraction(x.absupper(),SCALE))
    density=pmin-sum((absiv(z[i])*(1+absiv(mt[i])*pmax)
                     for i in range(len(t))),asiv(0))
    assert density.lo*4>3*SCALE
    A=1-sum((z[i]*mt[i] for i in range(len(t))),asiv(0))
    def kernel(q):
        x=asiv(q)
        sx=sin_iv(x/2)
        cx=1-2*sin_iv(x/4).square()
        xx=x.square()
        k=A*(2*pmin*x*sx-2*cx)/(xx-2)
        for i,u in enumerate(t):
            difference=x-u
            if difference.absupper()<SCALE//20:
                # Stable expression near the removable singularity x=t.
                J=(sinc_iv(difference)+sinc_iv(x+u))/2
            else:
                J=(2*x*sx*ct[i]-2*u*cx*st[i])/(xx-tt[i])
            k=k+z[i]*J
        return k
    gap=Fraction(57,10)
    small=kernel(gap)
    assert small.lo*25>3*SCALE  # k(5.7) > 3/25 = .12.
    # Since p>=0, k'(x)=-2 integral_0^.5 u p(u) sin(xu)du <= 0
    # for 0<=x<=5.7<2*pi; thus k(x)>.12 on that whole interval.
    stop=Fraction(60)
    # x>=60>max t: |J(x,t)| <= 2/(x-t), each term decreasing.
    assert max(v.hi for v in t)<60*SCALE
    tail=absiv(A)*(2*pmin*60+2)/(60**2-2)+sum(
        (2*absiv(z[i])/(60-t[i]) for i in range(len(t))),asiv(0))
    bounds=list(map(Fraction,(".184",".105",".078",".066",".062")))
    assert tail.hi*bounds[-1].denominator<bounds[-1].numerator*SCALE
    step=Fraction(1,50)
    count=int((stop-gap)/step)
    assert gap+count*step==stop
    maxima=[0]*5
    # p>=0, integral p=1 => sup |k'| <= 1/2, so center-to-cell
    # enlargement equals (step/2)/2 = 1/200.
    enlargement=SCALE//200
    for index in range(count):
        left=gap+index*step
        center=left+step/2
        band=min(5,int(left/gap))-1
        bound=kernel(center).absupper()+enlargement
        maxima[band]=max(maxima[band],bound)
        target=bounds[band]
        assert bound*target.denominator<target.numerator*SCALE,(index,band)
        if (index+1)%400==0:
            print(f"certified {index+1}/{count} real-axis cells",flush=True)
    assert 2*sum(bounds)==Fraction(99,100)
    output=dict(status="PASS: exact kernel envelopes and separated-chain degree bound",
        source="radius-five-rational-profile-candidate.json",gap_threshold=str(gap),
        small_gap_kernel_lower="3/25",small_gap_endpoint=small.report(),
        uniform_tail_bounds=[str(x) for x in bounds],
        interpretation="|k(x)|<bound[r-1] for every x>=r*5.7, r=1..5",
        real_axis_cells=count,cell_width=str(step),lipschitz_constant="1/2",
        cell_band_maxima=[dict(numerator=str(v),denominator=str(SCALE)) for v in maxima],
        tail_from=str(stop),tail_bound=tail.report(),
        row_l1_upper="99/100",
        scope="Degree normalization is identically 1 for chains whose every gap is >=5.7; no bounded h or new zero proportion is proved")
    (ROOT/"reviews/2026-09-08/radius-five-separation-certificate.json").write_text(
        json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print("PASS: small-gap k > .12; every separated-chain row sum < .99.")


if __name__=="__main__":
    main()

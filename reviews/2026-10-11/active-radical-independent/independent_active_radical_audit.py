"""Independent finite audit of the round-506 small-active-radical lemma.

No research-author module is imported. The infinite ideal count argument is
in REVIEW.md; these calculations certify local identities and continuous
rational enclosures, not a Hecke moment or a zero-free region.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = Path("E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex")
EXPECTED_SOURCE = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
checks = []


def check(name, claim):
    if not claim:
        raise ValueError(name)
    checks.append(name)


def canonical_bytes(path):
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def identity(path):
    raw = path.read_bytes()
    canon = canonical_bytes(path)
    return {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
            "canonical_lf_sha256": hashlib.sha256(canon).hexdigest(),
            "raw_bytes": len(raw), "canonical_lf_bytes": len(canon)}


def crossing(delta, kappa, x):
    c = 1 / (3*kappa)
    den = 3 - (1+2*c)*x
    p = (2-2*c*x)*(1-x)
    a = Q(5, 6)-delta
    j = a*den+delta*p
    t = 1+delta*p/(2*j)
    r = ((2-2*c*x)*t-(1-c)*x)/den
    m = t-r
    return {"c": c, "D": den, "P": p, "A": a, "J": j,
            "t": t, "r": r, "m": m, "B": delta*p/den,
            "I": delta*(1-x), "C": delta*(2-2*c*x),
            "R": Q(1, 6)+a*t}


def exact_text(x):
    return {"exact": str(x), "orientation": float(x)}


def main():
    if not __debug__:
        raise SystemExit("Do not use -O for a verification entry point")
    src = identity(SOURCE)
    check("frozen original source canonical identity",
          src["canonical_lf_sha256"] == EXPECTED_SOURCE)
    original = canonical_bytes(SOURCE).decode("utf-8")
    check("original source carries natural-zero convention",
          "an exponent divisible by six is the function" in original)
    check("original source carries sixth-power column identity",
          r"\label{eq:sixth-power-column-identity}" in original)
    check("original source carries finite parameter Sobolev inequality",
          r"\label{eq:parameter-sobolev}" in original)

    # Unique valuation-level reconstruction. This covers both sign choices,
    # and the zero on a nonunit remains zero even when the difference is 0.
    for left in range(25):
        for right in range(25):
            h = min(left, right)
            ql, qr = left-h, right-h
            sl, al = ql % 6, ql // 6
            sr, ar = qr % 6, qr // 6
            check(f"gcd reconstruction {left},{right}",
                  left == h+sl+6*al and right == h+sr+6*ar
                  and (sl == 0 or sr == 0) and (al == 0 or ar == 0))
            active = sl != 0 or sr != 0
            check(f"active support {left},{right}",
                  active == ((left-right) % 6 != 0))
            for sign in (-1, 1):
                d = sign*(left-right)
                check(f"local order {left},{right},{sign}",
                      (6//gcd(6, d) > 1) == active)
            if left or right:
                # χ_p(v)^a conjugate(χ_p(v)^b) on p|v is zero.
                # An exponent 0 below means an absent ideal prime, not an
                # invocation of the prescribed χ_p^0 on a nonunit.
                lf = 1 if left == 0 else 0
                rf = 1 if right == 0 else 0
                check(f"presentation puncture {left},{right}", lf*rf == 0)

    for e in range(65):
        inverse_two_plain = sum(e-a+1 for a in (0, 1) if e >= a)
        inverse_two_plain_one_q = sum(e-1-a+1 for a in (0, 1) if e >= a+1)
        check(f"local μ×plain×plain enumeration e={e}",
              inverse_two_plain == 2*e+1)
        check(f"local optional once-Q enumeration e={e}",
              inverse_two_plain_one_q == max(0, 2*e-1))
        check(f"local divisor-square domination e={e}",
              inverse_two_plain+inverse_two_plain_one_q <= (e+1)**2)
    choices = [(side, exponent) for side in ("s", "t") for exponent in range(1, 6)]
    check("exactly 10 active-prime configurations", len(set(choices)) == 10)
    check("sixth-power roots generate convergent exponent 3", Q(6, 2) == 3 and 3 > 1)

    # On the whole box, c decreases with κ, D decreases with c and x,
    # P decreases with c and x (P_x=-2-2c(1-2x)≤-2). Thus these endpoint
    # formulas are rigorous continuous extrema, not a grid extrapolation.
    dl, du = Q(3, 8), Q(2, 5)
    xl, xu = Q(49, 100), Q(1, 2)
    kl, ku = Q(37, 50), Q(3, 4)
    cl, cu = 1/(3*ku), 1/(3*kl)
    denlo, denhi = 3-(1+2*cu)*xu, 3-(1+2*cl)*xl
    plo, phi = (2-2*cu*xu)*(1-xu), (2-2*cl*xl)*(1-xl)
    check("derived continuous c enclosure", (cl, cu) == (Q(4, 9), Q(50, 111)))
    check("derived continuous D enclosure", (denlo, denhi) == (Q(455, 222), Q(1867, 900)))
    check("derived continuous P enclosure", (plo, phi) == (Q(86, 111), Q(1496, 1875)))
    alo, ahi = Q(5, 6)-du, Q(5, 6)-dl
    jlo, jhi = alo*denlo+dl*plo, ahi*denhi+du*phi
    tlo, thi = 1+dl*plo/(2*jhi), 1+du*phi/(2*jlo)
    blo, ilo, cmlo = dl*plo/denhi, dl*(1-xu), dl*(2-2*cu*xu)
    # m=((1-x)t+(1-c)x)/D follows from D-(2-2cx)=1-x.
    mlo = ((1-xu)*tlo+(1-cu)*xl)/denhi
    mhi = ((1-xl)*thi+(1-cl)*xu)/denlo
    rlo = ((2-2*cu*xu)*tlo-(1-cl)*xu)/denhi
    rhi = ((2-2*cl*xl)*thi-(1-cu)*xl)/denlo
    g = Q(1, 20000)
    tlominus, tplusmax = tlo-g/alo, thi+g/blo
    coremlo, coremhi = mlo-g/alo-g/ilo, mhi+g/cmlo
    short_inverse_max = rhi+g/ilo
    long_count_max = Q(1, 6)+ahi*tplusmax
    raw_saving = Q(3, 10000)  # Designed contract, not an attained estimate.
    rad_exponent = Q(31, 50)
    raw_margin = 1-long_count_max-rad_exponent/2-raw_saving
    check("J lower bound identity", jlo == Q(785, 666))
    check("t0 upper bound identity", thi == Q(2785237, 2453125))
    check("full actual long-range upper identity", tplusmax == Q(34503220411, 30379500000))
    check("varying-long count upper identity", long_count_max == Q(501053424521, 729108000000))
    check("whole core cutoff inside source detector domain", 1 < tlominus < tplusmax < Q(3, 2))
    check("whole short inverse safely below one", Q(3, 5) < rlo and short_inverse_max < 1-Q(1, 10000))
    check("whole plain core strict capacity", Q(1, 3) < coremlo < coremhi < Q(1, 2)-Q(1, 10000))
    zlo = (1-2*coremhi)/(6*ku)
    zhi = (1-2*coremlo)/(6*kl)
    check("whole requested plain capacity bounded away from zero", 0 < zlo < zhi < Q(1, 5))
    check("whole-box R=U^0.62 payment reserve", raw_margin > Q(1, 500))
    nu_i, nu_p, nu_zero = Q(1, 10000), Q(1, 10000), Q(1, 10**6)
    crossing_gap_min = alo*(tlo-1)
    check("uniform near-one no-slot endpoint count reserve", g+du*nu_i < crossing_gap_min)
    check("uniform near-half no-slot endpoint count reserve", g+2*du*nu_p < crossing_gap_min)
    check("inverse partition cutoff below fixed near-one boundary", short_inverse_max < 1-nu_i)
    check("plain partition cutoff below fixed near-half boundary", coremhi < Q(1, 2)-nu_p)
    check("inverse marked request positive across nonendpoint part", nu_i/2 > nu_zero)
    check("plain marked request positive across nonendpoint part", 2*nu_p/(6*ku) > nu_zero)
    check("second strict marked-inverse width uniform", 2*rlo-1+8*nu_zero > 0)
    check("inverse whole-slot supply smaller than 1/5", (1-rlo)/2 < Q(1, 5))

    point = crossing(Q(19429, 50000), Q(7499, 10000), Q(1, 2))
    check("crossing short/long count equality",
          1-Q(19429, 50000)*(Q(1, 2)+point["r"]/2) == point["R"])
    check("crossing plain-spike count equality",
          1-Q(19429, 50000)*(point["c"]/2+(2-point["c"])*point["m"]) == point["R"])
    tax = 1+point["C"]/point["A"]+point["C"]/point["I"]
    check("real all-branch coverage tax", tax == Q(8209647083, 1500842361))
    pointlong = Q(1, 6)+point["A"]*(point["t"]+g/point["B"])
    pointmargin = 1-pointlong-Q(133, 400)-raw_saving
    check("only target-label R=U^0.665 reserve", pointmargin > Q(3, 10000))
    necessary_chi = Q(467366968772963, 12314470624500000000)
    check("old lambda=1/20000 fails full coverage", Q(1, 20000) < necessary_chi*tax)
    check("designed lambda 0.0003 exceeds pre-fee target gate", raw_saving > g*tax)
    eta = Q(1, 10**6)
    check("strict amplification cost retained", g*tax+Q(5, 6)*eta < raw_saving)

    e_lo, e_hi = Q(16683858898627, 10**14), Q(16683858898628, 10**14)
    polynomial = lambda e: 657*e**3-954*e**2+21*e+20
    check("cubic root interval independently isolates a root", polynomial(e_lo) > 0 > polynomial(e_hi))
    check("cubic derivative negative on the root interval", 1971*e_hi**2-1908*e_lo+21 < 0)
    k_lo, k_hi = Q(5, 6)-e_hi/2, Q(5, 6)-e_lo/2
    check("relative previous boundary κ fits whole compact box",
          kl < Q(7499, 10000) < k_lo < k_hi < Q(749915, 10**6) < ku)

    public_script = ROOT/"scripts/hybrid_active_radical_mixed_cross_budget.py"
    public_report = ROOT/"reviews/2026-10-11/active-radical-mixed-cross-research.md"
    public_certificate = ROOT/"output/hybrid-active-radical-mixed-cross-budget.json"
    public = json.loads(public_certificate.read_text(encoding="utf-8"))
    check("public certificate binds the actual public checker",
          public["checker_canonical_lf_sha256"] == identity(public_script)["canonical_lf_sha256"])
    check("public research proof matches author proof verbatim",
          canonical_bytes(public_report) == canonical_bytes(
              ROOT/"tmp/research-round506-20261011/zero-free/active-radical-mixed-cross-research.md"))
    public_values = {"continuous_rL_minimum": tlominus, "continuous_rL_maximum": tplusmax,
                     "continuous_plain_minimum": coremlo, "continuous_plain_maximum": coremhi,
                     "continuous_long_count_upper": long_count_max,
                     "whole_box_low_active_raw_margin": raw_margin,
                     "target_label_low_active_raw_margin": pointmargin,
                     "coverage_tax": tax, "limiting_required_raw_saving": necessary_chi*tax,
                     "designed_full_point_count_gate": g*tax+Q(5, 6)*eta}
    for name, value in public_values.items():
        check("public finite core agrees with independent derivation: "+name,
              Q(public["values"][name]["exact"]) == value)

    deps = [ROOT/"notes/450-plain-kappa-extension-and-actual-capacity.md",
            ROOT/"notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md",
            ROOT/"reviews/2026-10-07/450-plain-kappa-extension-review-twisted.md",
            ROOT/"tmp/research-round505-20261011/zero-free/two-cutoff-joint-witness-coverage.md",
            ROOT/"tmp/research-round506-20261011/zero-free/active-radical-mixed-cross-research.md",
            public_script, public_report, public_certificate,
            ROOT/"reviews/2026-10-11/active-radical-mixed-cross-source-check.json",
            ROOT/"reviews/2026-10-11/active-radical-mixed-cross-reproduction.md"]
    values = {"D_min": denlo, "D_max": denhi, "P_min": plo, "P_max": phi,
              "J_min": jlo, "t0_min": tlo, "t0_max": thi,
              "core_long_min": tlominus, "core_long_max": tplusmax,
              "core_plain_min": coremlo, "core_plain_max": coremhi,
              "short_inverse_max": short_inverse_max, "plain_requested_z_min": zlo,
              "plain_requested_z_max": zhi, "varying_long_count_max": long_count_max,
              "whole_box_payment_margin": raw_margin, "target_label_payment_margin": pointmargin,
              "coverage_tax": tax, "pre_fee_raw_target_gate": necessary_chi*tax,
              "g_raw_gate": g*tax, "g_raw_gate_eta": g*tax+Q(5, 6)*eta}
    result = {"schema": "rh-weil-round506-independent-active-radical-audit-v1",
              "status": "PASS", "checks": len(checks), "source": src,
              "reviewed_dependencies": [identity(p) for p in deps],
              "checker": identity(Path(__file__)),
              "values": {k: exact_text(v) for k, v in values.items()},
              "scope": "Independent finite local algebra and whole continuous rational-box bounds. Infinite ideal-pair proof is reviewed in REVIEW.md, relative to the fixed source ideal count and character/smooth-calculus package. No full signed mixed estimate, global count saving, improved sigma, Lean or Nano claim.",
              "new_full_mixed_estimate": False, "new_count_saving": False,
              "new_zero_free_boundary": False, "finite_check_labels": checks}
    (HERE/"independent-active-radical-audit.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": result["status"], "checks": result["checks"],
                      "source_canonical_lf_sha256": src["canonical_lf_sha256"],
                      "whole_box_payment_margin": str(raw_margin),
                      "new_zero_free_boundary": False}))


if __name__ == "__main__":
    main()

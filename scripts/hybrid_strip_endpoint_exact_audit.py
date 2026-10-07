"""Exact finite algebra for notes 438--441; no analytic/Lean certification."""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def canonical_hash(path):
    content = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    return hashlib.sha256(content.encode()).hexdigest()


def endpoint_cases():
    alpha, ell0, b, shift = F(5, 6), F(1, 6), F(1, 8), F(1, 20000)
    ell1 = ell0 + shift
    h0, h1 = (1 + 3 * ell0 + b) / 2, (1 + 3 * ell1 + b) / 2
    margin = F(49, 440640) - F(5, 3) * shift
    assert margin == F(307, 11016000) > 0
    cases = 0
    for i in range(41):
        delta = F(i, 48)
        for j in range(21):
            x = F(j, 40)
            q, y = x * delta, F(1, 2) - x
            D = 3 - F(17, 9) * x
            P = 2 - F(26, 9) * x + F(8, 9) * x * x
            J = (alpha - delta) * D + delta * P
            assert J > 0 and 3 * P <= 2 * D
            R = 1 - delta + (alpha - delta) * delta * P / (2 * J)
            assert R <= 1 - F(2, 3) * delta

            def high(ell, h):
                K = -F(1, 4) + F(5, 4) * ell + b / 6
                return K + (F(1, 2) + ell) * delta + ell * q - h * (1 - R)

            E0, E1 = high(ell0, h0), high(ell1, h1)
            v = 51 + 41 * y
            rhs = (3 + 5 * y) * ((4 * v * delta - 79) ** 2 + 49)
            rhs += 4 * y * (
                4 * v * delta * ((1 + 3 * y) * (15 + 32 * y) * delta + 9 - 13 * y)
                + 265 + 3485 * y
            )
            assert 10368 * v * J * (-E0) == rhs
            assert -E0 >= F(49, 440640)
            derivative = -F(1, 4) + delta + q + F(3, 2) * R
            assert E1 - E0 == shift * derivative
            assert derivative <= F(5, 3) and -E1 >= margin
            # General source exponent: retain the z-residue at 1/6.
            lx, ly = (1 - ell1 - b) / 2, (1 - ell1 + b) / 2
            sigma = F(11, 12) - ell1 / 4
            a, z0 = (1 + delta) / 2, F(17, 50)
            source = a - sigma + h1 * (z0 - F(1, 6)) - a * ly - ell1 / 2 + ell1 * q
            source += h1 * (R + delta / 2 - z0)
            assert source == E1
            assert sigma + lx / 2 - 1 + h1 / 6 == sigma - F(2, 3) - b / 6
            cases += 1

    assert ell1 < F(1, 5)
    assert 9 * ell1 + 8 * b < 3 and 3 * ell1 + b < 1
    assert 1 - 3 * ell1 > 0
    assert (1 - 3 * ell1 - b) / 2 > 0
    assert (1 - 3 * ell1 + b) / 2 - F(11, 6) * b > 0
    assert ell1 / h1 > ell0 / h0 == F(8, 39)
    assert ell1 / h1 > F(7, 37)
    floor_margin = F(7, 1200) - F(32, 25) * shift
    intermediate_margin = F(49, 14400) - F(177, 200) * shift
    assert floor_margin > 0 and intermediate_margin > 0
    return {
        "rational_parameter_cases": cases,
        "slot_length": str(ell1),
        "conditional_boundary": str(F(7, 8) - shift / 4),
        "nominal_endpoint_margin": str(margin),
        "nominal_floor_margin": str(floor_margin),
        "nominal_intermediate_margin": str(intermediate_margin),
        "scope": "Exact identities and sampled finite inequalities only; capacity/contour extension not certified.",
    }


def clipped_low_cases():
    cases = 0
    for ell in (F(1, 12), F(1, 6), F(1, 6) + F(1, 20000), F(1, 5), F(1, 4)):
        values = []
        for j in range(33):
            d = ell * F(j, 32)
            Mprime, ellprime = 1 - ell - 2 * d, ell - d
            assert 1 + 3 * ellprime - 2 * Mprime == 5 * ell - 1 + d
            values.append(-d + max(F(0), 5 * ell - 1 + d) / 8)
            cases += 1
        assert max(values) == max(F(0), 5 * ell - 1) / 8
    return {"rational_cases": cases, "scope": "Clipped exponent algebra, including parameters outside analytic admission."}


def euler_identity_cases():
    cases = 0
    for Q in (2, 3, 5, 11):
        v = F(1, Q)
        for D in (F(-1, 3), F(0), F(1, 4)):
            for r in (F(-1, 7), F(0), F(1, 9)):
                Pstar = ((r * (1 - v) - D * (Q - 1) * v * v) / (1 - v) - D + v * r) / (1 - r)
                P = 1 / (1 - v) + v / (1 - v) + Pstar
                assert Pstar == (1 + v) * (r - D) / (1 - r)
                H = P * (1 - v) ** 2 / (1 - D)
                closed = (1 - v * v) / (1 - r) * (1 + v * (D - r) / (1 - D))
                assert H == closed
                cases += 1
    sigma = F(7, 8) - F(1, 80000)
    assert sigma > F(401, 600) > F(2, 3)
    good = min(6 * sigma - F(401, 100), sigma - F(3, 50), F(47, 50))
    ramified = min(sigma - F(1, 20), 3 * sigma - F(3, 2))
    assert good > 0 and ramified > 0
    return {"rational_local_models": cases, "candidate_good_decay": str(good), "candidate_ramified_decay": str(ramified),
            "scope": "Finite local algebra only; normal convergence is proved in note 440, not by sampling."}


def positive_spectrum_models():
    rows = []
    for m in (2, 4, 8, 16, 32):
        N = 3 * m * (m - 1)
        ones, zeros = N - m, m - 1
        assert ones + 1 + zeros == N
        assert ones + m == N
        second = F(ones + m * m, N)
        fourth = F((m - 1) ** 4 + zeros, N)
        assert second == F(4, 3) and fourth >= F(m * m, 48)
        rows.append({"m": m, "N": N, "normalized_second": str(second), "normalized_centered_fourth": str(fourth)})
    return {"cases": len(rows), "models": rows,
            "scope": "Abstract positive spectra; this is not the Lamzouri carrier construction or actual zeta zeros."}


def variable_low_dyads():
    retained, empty_slots = 0, 0
    for ell in (F(1, 6), F(1, 6) + F(1, 20000), F(1, 5)):
        for d in (F(0), ell / 2, ell):
            Mp, lp = 1 - ell - 2 * d, ell - d
            for O in (F(0), Mp / 3, Mp / 2):
                for gap in (F(0), Mp / 8):
                    H = Mp - O - gap
                    for A0 in (F(0), O / 2):
                        for N0 in (F(0), A0):
                            for za in (F(0), lp / 2, lp):
                                Td = 2 * H + 2 * A0 + 2 * za - 1 - lp - N0
                                identity = H - Mp + 2 * A0 + 2 * (za - lp) - N0
                                assert Td - (H - 3 * d) == identity <= 0
                                # S0=B0=theta_N=e_lambda=0; exact retained models.
                                if Td < 0:
                                    continue
                                for v, lb in ((F(0), F(0)), (Td, F(0)), (F(0), Td / 3), (Td / 2, Td / 6)):
                                    y = v + 3 * lb
                                    assert y <= Td and max(H, v + lb) == H
                                    u = min(v, za, (v + za) / 3)
                                    E = O / 2 + H + za - u - lb - max(F(0), Td - y) / 2
                                    assert E <= Mp + max(F(0), 5 * ell - 1 + d) / 4
                                    if za == 0:
                                        assert E <= Mp
                                        empty_slots += 1
                                    retained += 1
    return {"retained_dyad_models": retained, "empty_slot_models": empty_slots,
            "scope": "Exact bounded dyads with S0=B0=theta_N=e_lambda=0. Full masks, Fourier profiles and analytic tails are paper proofs, not finite models."}


def main():
    sources = [
        "notes/438-seven-eighths-and-zero-proportion-interfaces.md",
        "notes/439-prime-slot-geometry-and-a-conditional-strip-improvement.md",
        "notes/440-principal-euler-correction-below-seven-eighths.md",
        "notes/441-variable-slot-low-bound-on-the-original-probe.md",
    ]
    report = {
        "status": "passed",
        "date": "2026-10-07",
        "sources_canonical_lf_sha256": {p: canonical_hash(ROOT / p) for p in sources},
        "endpoint": endpoint_cases(),
        "clipped_low": clipped_low_cases(),
        "principal_euler": euler_identity_cases(),
        "positive_spectrum": positive_spectrum_models(),
        "variable_low": variable_low_dyads(),
        "scope": "Finite Fraction audits. No numerical root certification, full analytic proof, external Lean build, new zero-free region, or improved zeta proportion.",
    }
    destination = ROOT / "output/hybrid-strip-endpoint-exact-audit.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = ROOT / "reviews/2026-10-07/hybrid-strip-endpoint-exact-audit.md"
    summary.write_text(
        "# 438–441 精确有限代数审计\n\n"
        "2026-10-07。运行 scripts/hybrid_strip_endpoint_exact_audit.py，通过。\n\n"
        "861 个有理端点参数，165 个 clipped-low 参数，36 个局部 Euler 模型及 5 个抽象正谱模型；"
        "全部使用 Fraction。端点恒等式、候选余量和闭式模型分别核对。\n\n"
        f"另有{report['variable_low']['retained_dyad_models']}个retained反射dyad模型，"
        f"其中{report['variable_low']['empty_slot_models']}个empty-slot模型，核Td/H恒等式与row loss。\n\n"
        "nominal endpoint margin = 307/11016000；candidate boundary = 69999/80000。\n\n"
        "这些是有限模型检查。连续域有理下界的证明见439，Euler无限乘积见440；"
        "实际AF/Lamzouri算子分析见438及独立报告。没有重跑外部Lean，也没有证明新比例或新无零区。\n\n"
        "机器数据及正文绑定哈希见 output/hybrid-strip-endpoint-exact-audit.json。\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": report["status"], "endpoint_cases": report["endpoint"]["rational_parameter_cases"],
                      "candidate_margin": report["endpoint"]["nominal_endpoint_margin"], "report": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

# Gibbs补证提交原文

2026-09-06。主线程保存工具报告，仅将工具专用文献标记改为仓库相对链接。后续核查见[328](../../notes/328-tty-thm51-proof-repair-and-scope.md)。

下面提交的是**候选修补的完整代数证据**。我将此前分段检查合并为等价脚本复跑，结果为五段、130项检查全部通过；解析输入仍按下列源定理引用，供主线程独立交叉审。

所有页码均为 TTY v1 印刷页码，与 PDF 页序一致：[TTY v1原件](../../literature/background/tao-trudgian-yang-exponents-2501.16779v1.pdf)

- **第17页式(15)**：对正整数 \(k\)，
  \[
  LV(\sigma,\tau)\le\max\left\{2-2\sigma,\,
  \tau+(4-2/k)-(6-2/k)\sigma,\,
  \tau+k(6-8\sigma)\right\}.
  \]
  修补在前三段取 \(k=4\)，后两段取 \(k=3\)。
- **Theorem 32(ii)，第18页**：令 \(\rho=LV(\sigma,\tau)\)。在
  \(\rho\le\min(1,4-2\tau)\)、\(\alpha_1,\alpha_2\ge0\) 下，
  \[
  \rho\le\max\left\{
  \alpha_2+2-2\sigma,\,
  \alpha_1+\alpha_2/2+2-2\sigma,\,
  -\alpha_2+2\tau+4-8\sigma,\,
  -2\alpha_1+\tau+12-16\sigma,\,
  4\alpha_1+2+\max(1,2\tau-2)-4\sigma
  \right\}.
  \]
- **第22页式(25)**：对 \(\tau\ge2\)，
  \[
  LV_\zeta(\sigma,\tau)\le2\tau-12(\sigma-1/2).
  \]
- **第27页 Corollary 43**：若上述两类大值指数分别在
  \[
  2\tau_0/3\le\tau\le\tau_0,\qquad
  2\le\tau<4\tau_0/3
  \]
  上不超过 \(3(1-\sigma)\tau/\tau_0\)，则
  \(A(\sigma)\le3/\tau_0\)。这里使用43，不使用44。

取 \(x=\sigma\)，统一记
\[
b=\tau_0,\quad q=\frac{3(1-x)}b,\quad
a=\frac{2b}3,\quad h=-\frac{c}{1-q}.
\]
下表各段均为闭区间；公共端点可采用任一侧证书。

| 段 | \(x\) 范围 | \(k\) | \(b\) | \(c\) |
|---|---|---:|---|---|
| I | \([17/22,41/53]\) | 4 | \(9(3x-2)/2\) | \(24-32x\) |
| II | \([41/53,38/49]\) | 4 | \(9(3x-2)/2\) | \((7-11x)/2\) |
| III | \([38/49,25/32]\) | 4 | \(8(2x-1)/3\) | \((7-11x)/2\) |
| IV | \([25/32,11/14]\) | 3 | \(8(2x-1)/3\) | \(18-24x\) |
| V | \([11/14,4/5]\) | 3 | \(8(2x-1)/3\) | \((10-16x)/3\) |

这里 \(c\) 恰为所选 \(k\) 在式(15)中两个线性项的常数部分之最大值。因此
\[
\rho\le\max(2-2x,\tau+c).
\]
对应的分割端点为
\[
h=
\begin{cases}
\dfrac{24(3x-2)(4x-3)}{11x-8},&\mathrm I,\\[3pt]
\dfrac{3(3x-2)(11x-7)}{2(11x-8)},&\mathrm {II},\\[3pt]
\dfrac{4(2x-1)(11x-7)}{25x-17},&\mathrm {III},\\[3pt]
\dfrac{48(2x-1)(4x-3)}{25x-17},&\mathrm {IV},\\[3pt]
\dfrac{16(2x-1)(8x-5)}{3(25x-17)},&\mathrm V.
\end{cases}
\]
证书检查 \(a\le h\le b\) 及 \(1/3<q<1/2\)。在 \([a,h]\)，两个 Jutila 项分别满足
\[
2-2x\le q\tau,\qquad \tau+c\le q\tau.
\]

在 \([h,b]\)，定义
\[
p(\tau)=
\begin{cases}
11-16x+\tau,&\mathrm{I,II},\\
5\tau/4-(1+x),&\mathrm{III,IV,V},
\end{cases}
\]
\[
\alpha_2=\max(p(\tau),0),\qquad
\alpha_1=\frac{\tau+10-14x}{3}-\frac{\alpha_2}{6}.
\]
\(\alpha_2\) 的分界为 \(\tau=16x-11\) 或 \(4(1+x)/5\)；末项还有 \(\tau=3/2\) 的分界。下面的包络归约同时处理这些内部端点，无须假定它们与 \(h\) 的先后顺序。

令
\[
B(\tau)=5\tau/4-(1+x).
\]
Theorem 32(ii) 的五项准确化为
\[
\begin{aligned}
F_1&=\alpha_2+2-2x,\\
F_2&=\tau/3+(16-20x)/3+\alpha_2/3,\\
F_3&=F_2-\tfrac43(\alpha_2-B(\tau)),\\
F_4&=F_2,\\
F_5&=4\tau/3+(46-68x)/3+\max(1,2\tau-2)-2\alpha_2/3.
\end{aligned}
\]

完整检查清单及其端点归约如下；代码中的 `checks` 将每项明确列出并生成其分子、分母多项式。

- **Bourgain 前提**：在 \(\tau=b\) 检查 Jutila 两项均不超过 \(1\) 和 \(4-2b\)。这些是整个 \([h,b]\) 的最坏端点。
- **\(\alpha_1\ge0\)**：分别将 \(\alpha_2=0,p(\tau)\) 代入，在 \(\tau=h\) 检查；两条仿射函数的斜率均正。实际 \(\alpha_1\) 是两者之小者。
- **\(F_1\le q\tau\)**：零分支由 \(\tau\ge a\) 保证；正分支检查 \(\tau=b\)。
- **\(F_2\le q\tau\)**：零分支检查 \(\tau=h\)，正分支检查 \(\tau=b\)。
- **\(F_3\le F_2\)**：检查 \(p(b)\ge B(b)\)。I、II段的 \(p-B\) 随 τ 递减，其余三段恒为零；故 \(\alpha_2\ge B\)。
- **\(F_5\le q\tau\)**：用
  \[
  \max(1,2\tau-2)\le M_b:=\max(1,2b-2),\qquad \alpha_2\ge p(\tau).
  \]
  所得仿射包络的斜率为 I、II段 \(2/3\)，其余段 \(1/2\)，均大于 \(q\)，故只检查 \(\tau=b\)。
- **ζ 大值条件**：检查
  \[
  8b/3-12(x-1/2)\le4-4x.
  \]
  因斜率 \(2>q\)，该端点足够。I—III段的所需 ζ 区间实际为空，脚本仍检查这一充分条件。

原印刷证明失效处对应的关键修补余量是
\[
G=(q-\tfrac13)h-\frac{16-20x}{3}.
\]
五段的分解结果分别为
\[
\begin{array}{c|l}
\mathrm I&-\dfrac{4(5x-4)(13x-10)}{3(11x-8)}\\[3pt]
\mathrm {II}&\dfrac{(5x-4)(55x-43)}{6(11x-8)}\\[3pt]
\mathrm {III}&\dfrac{(17x-13)(31x-23)}{6(25x-17)}\\[3pt]
\mathrm {IV}&-\dfrac{2(266x^2-437x+179)}{3(25x-17)}\\[3pt]
\mathrm V&\dfrac{2(406x^2-615x+233)}{9(25x-17)}.
\end{array}
\]
它们在各自闭区间均严格为正。

以下是实际复跑的合并代码。每项先消去公因子、确定分母正号，再用精确实根计数检查区间内无根；同时打印分子的有理实根隔离区间。全部运算使用有理数。

```python
import sys
sys.stdout.reconfigure(encoding="utf-8")
import sympy as S

x, t = S.symbols("x t", real=True)
R = S.Rational
bL, bH = R(9, 2)*(3*x-2), R(8, 3)*(2*x-1)

# name, sigma_left, sigma_right, Jutila k, tau0, c, M(tau0)
rows = [
    ("I",   R(17,22), R(41,53), 4, bL, 24-32*x,     S.Integer(1)),
    ("II",  R(41,53), R(38,49), 4, bL, (7-11*x)/2,  S.Integer(1)),
    ("III", R(38,49), R(25,32), 4, bH, (7-11*x)/2,  S.Integer(1)),
    ("IV",  R(25,32), R(11,14), 3, bH, 18-24*x,     2*bH-2),
    ("V",   R(11,14), R(4,5),   3, bH, (10-16*x)/3, 2*bH-2),
]

def interior_root_count(poly, lo, hi):
    # Remove endpoint roots before exact real-root counting.
    p = poly
    for endpoint in (lo, hi):
        factor = S.Poly(x-endpoint, x, domain=S.QQ)
        while p.degree() > 0 and p.eval(endpoint) == 0:
            p = p.exquo(factor)
    return p.count_roots(lo, hi)

def certify(label, expr, lo, hi, strict=False):
    expr = S.cancel(expr)
    n, d = S.fraction(expr)
    mid = (lo+hi)/2
    if d.subs(x, mid) < 0:
        n, d = -n, -d
    pn, pd = (S.Poly(z, x, domain=S.QQ) for z in (n, d))

    assert pd.eval(lo) > 0 and pd.eval(hi) > 0
    assert pd.eval(mid) > 0 and pd.count_roots(lo, hi) == 0

    if pn.is_zero:
        assert not strict, label
        roots = []
    else:
        values = [pn.eval(z) for z in (lo, mid, hi)]
        assert all(v > 0 if strict else v >= 0 for v in values), label
        assert interior_root_count(pn, lo, hi) == 0, label
        roots = pn.intervals(eps=R(1, 10**12))

    print(label, "NUM =", S.factor(n), "DEN =", S.factor(d),
          "ISOLATORS =", roots)
    return 1

count = 0
for name, lo, hi, k, b, c, Mb in rows:
    q = 3*(1-x)/b
    a = 2*b/3
    h = -c/(1-q)
    low = name in ("I", "II")
    p = 11-16*x+t if low else R(5,4)*t-(1+x)
    B = R(5,4)*t-(1+x)
    ph = p.subs(t, h)
    pb = p.subs(t, b)
    c1 = (4-R(2,k))-(6-R(2,k))*x
    c2 = k*(6-8*x)
    b_other = bH if low else bL
    b0 = 2-2*x

    checks = [
        ("b_positive", b, True),
        ("q_minus_third", q-R(1,3), True),
        ("half_minus_q", R(1,2)-q, True),
        ("tau0_is_min", b_other-b, False),
        ("c_ge_Jutila_c1", c-c1, False),
        ("c_ge_Jutila_c2", c-c2, False),
        ("M_branch", R(3,2)-b if name in ("I","II","III")
                     else b-R(3,2), False),
        ("h_ge_a", h-a, False),
        ("h_le_b", b-h, False),
        ("rho_le_1_constant", 1-b0, False),
        ("rho_le_1_linear", 1-b-c, False),
        ("rho_le_4_minus_2tau_constant", 4-2*b-b0, False),
        ("rho_le_4_minus_2tau_linear", 4-3*b-c, False),
        ("alpha1_zero_at_h", (h+10-14*x)/3, False),
        ("alpha1_positive_at_h", (h+10-14*x)/3-ph/6, False),
        ("F2_zero_at_h", (q-R(1,3))*h-(16-20*x)/3, False),
        ("F1_positive_at_b", 3-3*x-(pb+2-2*x), False),
        ("F2_positive_at_b",
         3-3*x-(b/3+(16-20*x)/3+pb/3), False),
        ("F5_envelope_at_b",
         3-3*x-(4*b/3+(46-68*x)/3+Mb-2*pb/3), False),
        ("p_dominates_B_at_b", pb-B.subs(t,b), False),
        ("zeta_endpoint",
         4-4*x-(8*b/3-12*(x-R(1,2))), False),
    ]

    # c is exactly the maximum of the two Jutila constants.
    assert S.simplify(c-c1) == 0 or S.simplify(c-c2) == 0
    # b is exactly one of the two candidate tau0 values.
    assert S.simplify(b-bL) == 0 or S.simplify(b-bH) == 0

    # Slopes needed for all tau endpoint reductions.
    for label, slope_gap in [
        ("alpha1_zero_slope", R(1,3)),
        ("alpha1_positive_slope", R(1,3)-S.diff(p,t)/6),
        ("F1_positive_slope_minus_q", S.diff(p,t)-q),
        ("F2_positive_slope_minus_q",
         R(1,3)+S.diff(p,t)/3-q),
        ("F5_envelope_slope_minus_q",
         R(4,3)-2*S.diff(p,t)/3-q),
    ]:
        checks.append((label, slope_gap, True))

    for label, expression, strict in checks:
        count += certify(name+"."+label, expression, lo, hi, strict)

    print("PASS", name, "interval", (lo,hi), "tau endpoints",
          [S.factor(z) for z in (a,h,b)])

print("ALL CHECKS PASSED:", count)
```

复跑尾部为：

```text
PASS I
PASS II
PASS III
PASS IV
PASS V
ALL CHECKS PASSED: 130
```

结合上述端点归约，证书支持 Corollary 43 所需的两个完整 τ 区间，从而得到候选修补结论
\[
A(x)\le\frac3b
=\max\left\{\frac2{9x-6},\frac9{8(2x-1)}\right\},
\qquad 17/22\le x\le4/5.
\]

这份证据没有修改源文件或仓库文件；候选状态留待主线程交叉审。本旁线到此结束。

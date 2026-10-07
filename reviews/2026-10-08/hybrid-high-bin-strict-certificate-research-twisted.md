# 451 高行区间的严格连续余量：独立补证

2026-10-08。状态：新推导，待另一作者全文独审。本稿仅证明已冻结
451 在高 detector 行区间本来就有固定余量；不认证新密度定理，不给新的
无零区域或比例。所有分析准入仍限于 451/450 的同一个 [R]。

## 1. 冻结输入与实际变量

canonical LF 均只将 CRLF、lone CR 替换为 LF，不删除尾空白。

| 输入 | canonical LF SHA-256 |
|---|---|
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | `17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487` |
| [原 Cubic 审计](../../scripts/hybrid_kappa_feedback_exact_audit.py) | `e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68` |
| [冻结输出](../../output/hybrid-kappa-feedback-exact-audit.json) | `309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba` |

设 $e=e_*$ 是 $657e^3-954e^2+21e+20=0$ 的指定根，且

\[
 \frac{16683858898627}{10^{14}}<e<
 \frac{16683858898628}{10^{14}}.
 \tag{1}
\]

保留 451 的 $b=b_*,h=(1+3e+b)/2,
\kappa_*=5/6-e/2,c=(3\kappa_*)^{-1}$，并令

\[
 D(y)=\frac52-c+(1+2c)y,\quad
 P(y)=1-\frac c2+2y+2cy^2,\quad
 J=(5/6-\delta)D+\delta P.
 \tag{2}
\]

这里 $a$ 是实际 row-bin 零点实部参数，

\[
 \delta=2a-1,\qquad x=q/\delta,\qquad y=1/2-x.
\]

它不是全族零点上确界 $\beta_*$。whole-family bootstrap
$\beta_*\le7/8$ 给 $\delta\le3/4$。以下仅考虑闭矩形

\[
 a\ge73/86\quad\Longleftrightarrow\quad
 30/43\le\delta\le3/4,\qquad0\le y\le1/2.
 \tag{3}
\]

## 2. 双 Bernstein 的严格有理证书

沿 451 §3 的显示式，记 $K=-1/4+5e/4+b/6$、
$W=1/2+3e/2-ey$，并完整保留其三个多项式

\[
 A=-2(P-D)(W-h)+hP,
\]
\[
 B=2K(P-D)+\frac53D(W-h)+\frac56hP,\qquad
 C=-\frac53DK.
 \tag{4}
\]

原 endpoint 指数 $E_*(h)$ 满足精确恒等式

\[
 F(y,\delta):=-2JE_*(h)=A(y)\delta^2-B(y)\delta+C(y).
 \tag{5}
\]

作真实区间的仿射代换

\[
 \delta=l+(r-l)u,\quad y=v/2,\quad
 l=30/43,\ r=3/4,\quad (u,v)\in[0,1]^2.
\]

若 $A_j,B_j,C_j$ 为 $y^j$ 的系数（越界系数为零），那么代换后
power 系数 $t_{ij}$ 准确为

\[
 t_{0j}=2^{-j}(A_jl^2-B_jl+C_j),
\]
\[
 t_{1j}=2^{-j}(2A_jl-B_j)(r-l),\qquad
 t_{2j}=2^{-j}A_j(r-l)^2.
 \tag{6}
\]

$F$ 的双次数至多为 $(2,3)$。其 Bernstein 系数是

\[
 \mathcal B_{ij}=
 \sum_{k=0}^{i}\sum_{s=0}^{j}
 t_{ks}\frac{\binom ik}{\binom2k}
       \frac{\binom js}{\binom3s},\quad
 0\le i\le2,\ 0\le j\le3.
 \tag{7}
\]

这不是采样。由恒等式
$u^k=\sum_{i=k}^2\binom ik\binom2k^{-1}
\binom2i u^i(1-u)^{2-i}$ 和 $v$ 的对应三次恒等式，
$F$ 等于这些系数对非负、总和为一的双 Bernstein 基函数的组合。

在 $\mathbb Q[e]/(657e^3-954e^2+21e+20)$ 中准确形成 (6)–(7)，
再以 (1) 的有理 interval Horner 取下端，得到如下严格下界；表中
每个整数都需除以 $1000$：

| $i\backslash j$ | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| 0 | 45 | 86 | 161 | 286 |
| 1 | 52 | 99 | 181 | 317 |
| 2 | 61 | 113 | 203 | 352 |

每个 interval 下端严格大于表中值，所有表中值又严格大于 $1/25$。
因此整个 (3) 连续域上严格有

\[
 F(y,\delta)>1/25.
 \tag{8}
\]

原参数 $c>0$ 给 $D\le3,P\le2$，且 $J>0$。所以

\[
 J\le3(5/6-\delta)+2\delta\le5/2,\qquad
 E_*(h)<-1/125.
 \tag{9}
\]

## 3. 实际反馈与其范围

在 451 的反证合同内，$\Delta=\beta_*-\sigma_*>0$，
$\kappa_{\rm act}=2\beta_*-1$ 真正进入原 plain moment。
沿 451 已付的一致 derivative bound，$h<1$ 给

\[
 E_{\beta_*}(h)=E_*(h)-\Delta+
 h(R_{*,\kappa_{\rm act}}-R_{*,\kappa_*})
 <-1/125-24\Delta/25.
 \tag{10}
\]

这没有调用 $\kappa_*$ 的未成立零自由前件。$1/2\le d\le h$
的 actual endpoint 斜率在 451 中为正，故较小 $d$ 不增加指数。
其 $h\le d\le h+\zeta$、$\zeta=\Delta/32$ 费用至多 $\Delta/16$，
所以这段在其他 real losses 之前仍严格小于

\[
 -1/125-359\Delta/400.
 \tag{11}
\]

反之，冻结连续证书唯一等号点为

\[
 y=0,\quad\delta_*=(5-9e)/(6+18e),\quad R_*=2/3.
\]

(1) 的准确区间计算给

\[
 .38858335426599<\delta_*<.38858335426605,
\]
\[
 .69429167713299<a_*=(1+\delta_*)/2<.69429167713303.
 \tag{12}
\]

因此仅在 $a>73/86$ 加强实际行计数，会强化原来已严格的高行区间。
直接取旧最终联合包络与新高行包络的较小值，不能改变唯一等号点，
不足以给新的 $\sigma$ 边界。若新计数覆盖较低 $a$，还须与已付的
联合 inverse/plain/amplified 包络比较；仅优于最初 raw inverse
包络不等于优于最终 $R_*$。这里也不排除重新证明有槽的新联合估计。

## 4. 不改任何冻结文件的复跑代码

从仓库根执行以下代码。它导入冻结 Cubic 模块但不写文件；先核其字节
哈希，再复构造全部 12 个系数和有理严格比较。

```python
import contextlib, hashlib, importlib.util, io, math
from pathlib import Path
from fractions import Fraction as Q

p = Path('scripts/hybrid_kappa_feedback_exact_audit.py')
t = p.read_bytes().decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
assert hashlib.sha256(t.encode('utf-8')).hexdigest() == (
    'e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68')
spec = importlib.util.spec_from_file_location('frozen_cubic', p)
m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(m)
l, r = Q(30, 43), Q(3, 4)
lower = [[45, 86, 161, 286], [52, 99, 181, 317],
         [61, 113, 203, 352]]
for i in range(3):
    for j in range(4):
        z = m.Cubic(0)
        for k in range(i + 1):
            for s in range(j + 1):
                A = m.A[s] if s < len(m.A) else m.Cubic(0)
                B = m.B[s] if s < len(m.B) else m.Cubic(0)
                C = m.C[s] if s < len(m.C) else m.Cubic(0)
                v = [A*l*l-B*l+C, (2*A*l-B)*(r-l),
                     A*(r-l)**2][k] / 2**s
                z += v * Q(math.comb(i,k), math.comb(2,k)) * (
                    Q(math.comb(j,s), math.comb(3,s)))
        assert z.interval()[0] > Q(lower[i][j], 1000) > Q(1,25)
print('PASS: all twelve Bernstein coefficients exceed 1/25')
```

执行该准确计算只认证显示代数、指定实嵌入和连续多项式下界；不认证
AFE、density detector、原无限轮廓、实际素数估计、[R] 全包、Lean 或 RH。

# 476. Ivić 密度使原四阶增长幂进一步降至 5/7

2026-10-08。基线 5fe68395d20e9738ecc0ba64e8a762f4d93bd073。
继续原路线，本次只加强 475 中已付的加权零点计数步骤。
原 sharp cutoffs、正高度窗、normalizer、half-Gram 和 fixed carrier 均保留。
没有新的常数四阶预算、零点比例或无零边界。

## 1. 完整来源与适用前件

canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim 或改变 EOF。

| 完整证明来源 | canonical LF SHA256 |
|---|---|
| [Ivić 密度迁移作者源](../reviews/2026-10-08/hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [475 原正高度完整零点包](../reviews/2026-10-08/hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [原 fixed-start 采样](../reviews/2026-10-08/hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc |

[root 完整独审](../reviews/2026-10-08/hybrid-ivic-density-and-scalar-fourth-growth-review-root.md)
核准整个实部包络和原对象迁移。本轮未回改 475、原论文或旧证书。

仍设 [Rθ] 为 ζ 的全部非平凡零点实部 β≤θ，固定 5/6<θ≤7/8。
保留 X=T/(2π)、ell=log X、原 even C² taper 与 a_ell≥c_phi>0，及

\[
 P_H(t)=\frac1{a_\ell\ell}\sum_{\sqrt X<p\le X}
          \frac{\log p}{\sqrt p}p^{it},
 \qquad M_T=\frac1T\int_{T/4}^{4T}|P_H(t)|^4dt.
\]

## 2. 新采用的外部输入及全实部最大值

Ivić 本人的原书 *Topics in Recent Zeta-Function Theory*，Theorem 9.3、
(9.63)，以及[作者本人综述 §3](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/Ivic-Sanutalk.pdf)，给普通 ζ 的无条件输入

\[
 N(\sigma,V)\ll_{\sigma,\epsilon}
       V^{3(1-\sigma)/(2\sigma)+\epsilon},
 \qquad 3831/4791<\sigma<1.
 \tag{1}
\]

原作者书与综述均已实际读取；没有将 Hecke masked rows 换成原 n^(it)。
实际新增网格从 4/5 起，严格位于 (1) 的范围内。

475 已付的 entire combined Perron 与 full-tail Jensen 给 Λ 版本
widehat M_T≪ell³/T·Σ_(|γ|≤16T)X^[4(β−1/2)_+]+O(X^(−2)ell^4)。
在 [1/2,4/5] 用原 Ingham/Huxley 密度，整个低段的指数最大值为 22/35；
在 [4/5,θ] 由 (1) 得

\[
 f_I(\sigma)=4\sigma-3+\frac{3(1-\sigma)}{2\sigma},
 \qquad f'_I(\sigma)\ge53/32>0.
\]

f_I(5/6)=19/30 比 22/35 大 1/210。所以整个原参数域的最大值
恰为 f_I(θ)，不是只将顶端零点的密度替换后遗漏中段。
先固定有限网格再令 T 增大，日志与网格宽度各吸收到 epsilon，
不要求 σ 随 T 移动时的未知一致常数。

474 的 proper-power L4 norm 差经 Minkowski 返回 genuine primes，得

\[
 \boxed{M_T\ll_{\phi,\theta,\epsilon}T^{B_I(\theta)+\epsilon},
 \quad B_I(\theta)=4\theta-3+\frac{3(1-\theta)}{2\theta}.}
 \tag{2}
\]

## 3. 具体节省与同一个固定起点

在 θ=7/8，(2) 的幂为 5/7。原路线的上界现在依次为

| 输入及付款 | 四阶增长幂 |
|---|---|
| 446 的 strip + 原二矩 | 3/4 |
| 475 的完整零点包 + Ingham/Huxley | 19/26 |
| 本次相同零点包 + Ivić 密度 | 5/7 |

19/26−5/7=3/182，3/4−5/7=1/28；一般两次节省分别为
3(1−θ)²/[2θ(3θ−1)]>0 和 (1−θ)(4θ−3)/(2θ)>0。
在 451 原 θ*=0.874957019420098946… 下，B_I≈0.714198002953028；
该 θ* 本身未改变，仍相对其原 [R]。

475 新采样准入对全部 sigma∈[T,T+T/sqrt ell] 保留 exact floor 及
E_T(M) 的全部 guard/cross。代入 (2) 后，r_sigma、actual finite high
fourth 与 entire prime fourth 在原每个固定起点均继承同幂。
最后转同配置 centered zero matrix 时，仍保留 AF 的明示 [R]、背景和
真正未归一化 S1 尾项合同。这里传递一侧上界，不恢复 quartic 等式。

## 4. 完成范围和继续研究的目标

本次确认的是同对象增长幂的进一步加强，外部 Ivić 密度是既有定理；
不声称新的经典密度结果或四矩 exponent 的文献首次性。
475 的完整远共振付款保持有效，剩余仍是频差约 1/X 的 signed near。
指数 5/7 仍为正，不能充当改善惯性比例所需的常数四阶预算，
也不能免费替代原零自由证明的 capacity 前件。
尚无实际新比例或无零边界，未新增边界论文。

# 原正高度零点包四矩增长上界：独立全文审查

2026-10-08，twisted_research。结论：限定 PASS。实读另一作者源全部
332 行，并独立复算 twisted Perron、全零点包 Jensen、固定网格密度
与原 prime 转移；没有修改源、冻结笔记、math、Git 或证书。

## 1. 最终源绑定和外部范围

canonical LF 只统一 CRLF/lone CR，不 trim 或改变 EOF。

| 来源 | canonical LF SHA-256 | bytes /行 |
|---|---|---:|
| [被审完整源](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 | 12641 /332 |
| [474 原 scalar 准入](../../notes/474-original-short-carrier-canonical-scalar-fourth-admission.md) | 37306c6d403f48c93d5d0f92782088225084e2e4b6b694cd89644a75fe39e99f | 5350 /121 |
| [474 完整作者源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 | 14699 /370 |

源的 446、451 链接/hash 亦逐一与磁盘实际文件核对。原 math 源的
42a5ee0f…ec6a3 及 451 范围保持冻结；本审查不重新认证它们的完整
无零证明。这里确切使用的条件是 Riemann ζ 的全体非平凡零点
实部 β≤固定 θ，5/6<θ≤7/8；不是任意 Hecke family 的 masked
零点密度，也不是从本稿反向得到新 strip。

本次浏览并核对两份 primary：
[Fesenko–Ricotta–Suzuki, Appendix A](https://www.numdam.org/article/AIF_2012__62_5_1819_0.pdf)
的 Proposition A.1、(A.3)、(A.6) 给局部重数计数及 logarithmic
derivative 的局部零点展开；将圆盘截取改成 ordinate 截取的差为
O(log |t|)。其证明支持源 (4)–(5) 的 ζ 特例与大高度 uniform strip。
没有使用该文 mean-periodicity 结论。

[Guth–Maynard 原研究论文 (1.2)–(1.3)](https://arxiv.org/html/2405.20552v1)
准确记录 Ingham/Huxley 两个零密度指数和原出处。
这里只引用这些经典密度输入。没有把其 shorter-polynomial
large-value theorem 免费应用到原长度 X² 的 Λ_H*Λ_H 列。

## 2. 同一个 sharp high signal，combined Perron 的真实留数

x=floor X+1/2、y=floor sqrt X+1/2 精确保留
sqrt X<n≤X 的原整数集合；端点距每个整数至少 1/2。
s₀=1/2−it，c=1/2+1/L，使 Re(s₀+c)=1+1/L。
直接对 Λ(n)n^(−1/2+it) 使用 truncated Perron，其误差只用
系数模 Λ(n)/sqrt n，不产生 Abel 的 |t| 费用。

近端误差为 sqrt x log²x/H；远端利用
ΣΛ(n)n^(−1−1/L)=O(L)。H~T~X 因此确为
O(X^(−1/2)L²)，y 前缀更小。
在移线前合并
\[
 F_{x,y}(z)=\frac{x^z-y^z}{z}
          =\int_{\log y}^{\log x}e^{zu}\,du
\]
消去的是核自身在 z=0 的人工 pole。若 ζ(s₀)=0，
D(s₀+z)=−ζ'/ζ 仍有 pole，留数准确是
−m_ρ F(0)=−m_ρ log(x/y)；源 (9) 确实保留这一项。
因此没有用 F entire 错删 critical-line actual zero residue。

选择 H_t∈[10T,11T] 时，−t±H_t 都是大高度且 |height|≤16T。
两个条件各自排除零 ordinate 的 c₁/L 邻域；
总数 O(TL) 使删除长度 O(c₁T)，先取固定小 c₁ 即可同时满足。
这个选择逐 t 作，不要求 H_t 连续。

移至 Re z=−3/2 后 Re(s₀+z)=−1，未跨 trivial zeros。
左边利用 functional equation 得 D(−1+iv)=O(log(2+|v|))，
积分费用 O(y^(−3/2)L²)。横边零点距离保证 D=O(L²)，
F=O(sqrt X/H)，费用 O(X^(−1/2)L²)。
ζ-pole 留数为正 F(1/2+it)，zero 留数为负；
|γ+t|<H_t 的所有实际零点含重数均保留。
正高度 t~T 使 principal 项 O(X^(−1/2))，未删除 height 0 峰后
声称全高度均小。

## 3. Full-tail 零点包和 Jensen 对数幂

对 a=β−1/2，完整界是
\[
 |F(a+iv)|\ll X^{a_+}\min(L,|v|^{-1})
 \ll X^{a_+}k_L(v),\qquad
 k_L(v)=\frac{L}{1+L|v|}.
\]
它在 a=0,v=0 同样合法，不除以 β−1/2，不假设零点简单。
在取绝对值后才将 row-dependent contour 内零点扩大到
|γ|≤16T，因此可以不用 H_t 的 measurability 作后续积分。

局部零点数 O(L) 给
Σ k_L(t+γ)≤C L²；超过单位距离的所有 bins 的 harmonic sum
仍包含，没有偷截成 fixed-height near 包。
每一个 k 的完整正高度积分为 O(L)。
重数逐项应用加权 Hölder：
\[
 (\sum c_\rho k_\rho)^4
 \le(\sum k_\rho)^3\sum c_\rho^4k_\rho.
\]
因此原 (a_L L)^4 normalizer 后的费用为
L⁶·L/L⁴=L³，确切得到
\[
 \widehat{\mathcal M}_T\ll_\phi
 \frac{L^3}{T}\sum_{|\gamma|\le16T}X^{4(\beta-1/2)_+}
 +O(X^{-2}L^4).
\]
这是一侧 upper；不提供某个 packet 不会被其他 packet 抵消的 detector。

## 4. 固定 σ 网格、连续最大值和严格幂改善

先给定最终 ε，再固定有限 β 网格及 density 的 ε₁；
各 bin 的密度常数随后才吸收于充分大 T。
没有让 σ 随 T 接近 θ 而要求未知一致常数。
β≤1/2 的总量 O(TL) 只贡献 polylog。

两段的指数为 4σ−3+n(σ)。独立复算：
低段导数 4−3/(2−σ)²>0；
高段导数 4−6/(3σ−1)²>0，后者在 σ=3/4 已为 4/25。
两段在 3/4 连续等于 3/5，1/2 端为零。
所以全范围最大值准确在 θ：
\[
 B(\theta)=4\theta-3+\frac{3(1-\theta)}{3\theta-1}.
\]
有理计算给 B(7/8)=19/26，且
\[
 (2\theta-1)-B(\theta)
 =\frac{(1-\theta)(6\theta-5)}{3\theta-1}>0,
 \qquad (3/4)-(19/26)=1/52.
\]
θ_* 的小数只作展示，不参与证明。
这个新上界改进的是既有增长指数，B 仍为正。

## 5. 原 proper powers、ratio 和固定起点范围

474 的同窗 normalized L⁴ proper-power norm 差 O(X^(−1/12))
使 prime signal 用 L⁴ triangle 继承同一个增长幂。
没有在未知增长四矩时声称两矩的 additive difference 为 o(1)。

源第6节只引用已冻结 474 的平均 scalar 准入，保留
m/T·M^(1/4)、m²/T 及其平方 cross；代入 B<1 后都由主幂控制。
它未自行宣称 fixed-start ratio 等同 carrier 平均，
也未把 q_sq 换成完整 half-Gram。新的 fixed-start sampling
若另经独审，是独立新增输入；不是本源的隐含前件。

第7节的 local Nikolskii 也是合法的一侧结果：
给原 prime frequencies 选 C∞ multiplier 后先切真正 L⁴ 正高度窗，
再用 kernel L^(4/3) norm O(L^(1/4)) 与 exterior Schwartz tail。
因而 bounded M 推出局部 spike O((TL)^(1/4))。
此上界没有 actual zero noncancellation lower detector，
所以不能反向宣布 3/4 无零，也不能排除孤立固定低高度离线零点。

限定 PASS：源支付原 canonical scalar fourth 的严格增长幂上界及
其现有平均 ratio 后果。没有支付 O(1)、有用固定 residual 常数、
实际新比例、新边界、全 family 或 RH。


# Ivić 密度与原 scalar 四阶增长：radial 独立全文审查

2026-10-08。审查者：radial_review。基线 5fe68395d20e9738ecc0ba64e8a762f4d93bd073。

结论：限定 PASS。逐行读取最终作者源全部 184 行，核对一手 Ivić 定理、整个实部包络、有限网格量词、proper-power 范数迁移及原 fixed-carrier 增长前件。没有需要作者修改的数学阻断。结论是原对象的增长幂加强；外部密度定理仍是引用输入，未重新证明其全部零点检测与指数对分析。

canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim，不改变 EOF。

| 实读或核对的冻结对象 | canonical LF SHA256 | bytes / 行 |
|---|---|---|
| [被审作者源](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d | 9802 / 184 |
| [已独审的原正高度零包源](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 | 12641 / 332 |
| [已独审的 scalar 准入源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 | 14699 / 370 |
| [原 fixed-start 采样源](hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc | 7522 / 199 |
| [采样源的 compression 独审](hybrid-fixed-start-half-gram-sampling-review-compression.md) | 9f5b4b76bab1483cf0eee8607928f5b85b41feb3e14aa652c838416f37b68cf8 | 5786 / 119 |

后面三份数学来源沿用已完成的独立审查；本次不将作者本人对早先零包源的自核替代其不同作者审查。新作者源所做的密度替换与迁移在本报告中独立核验。

## 1. 普通 ζ 的准确一手输入

独立浏览了 Ivić 本人综述 [The distribution of zeros of the zeta-function](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/Ivic-Sanutalk.pdf) §3、印刷第 5–6 页。其 (3.1) 计数满足实部 β≥σ、两侧高度 |γ|≤V；随后给出的无条件界为

\[
 N(\sigma,V)\ll_{\sigma,\varepsilon}
 V^{3(1-\sigma)/(2\sigma)+\varepsilon}.
\]

另只在内存读取了作者原书 [Topics in recent zeta function theory](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/86/6d/866d1cf0-a942-4f8a-9d30-7cb3b03e1b1c/i_ivic-66.pdf) 的相关页：印刷第 182–183 页 / PDF 第 187–188 页，Theorem 9.3、(9.63) 及其 k=2 前件。原书 Chapter 9 印刷第 167 页的 N 定义与印刷第 169 页的零点检测、unit-strip 计数说明也已读。它给 A(σ)≤3/(2σ)，下端 3831/4791，换成作者源 (2) 正确。未将后面的 LH 条件段混入此定理。

普通零点数按重数读取。即便从 separated 代表计数表述开始，原 Riemann–von Mangoldt 的单位高度 O(log V) 计数恢复重数只增固定日志，仍吸收到 ε。这里不是 character/Hecke 家族密度。

作者源选严格下端是合法收紧。实际新增网格满足 σ≥4/5，且精确有

\[
 \frac45-\frac{3831}{4791}=\frac3{7985}>0.
\]

因此原书与后来综述在端点的表述差异不影响使用。外部经典定理作引用输入；本次没有重证其全篇证明、宣布新密度结果，或认证整个原无零证明。

## 2. 整个实部包络与非连续拼接

核准作者源 (3)–(6)。在 [1/2,3/4] 与 [3/4,4/5] 分别使用 Ingham、Huxley 的普通 ζ 密度。两段的 f=4σ−3+n 导数为

\[
 4-\frac3{(2-\sigma)^2},
 \qquad
 4-\frac6{(3\sigma-1)^2},
\]

各自在相应闭区间正；在 3/4 连续。整个低层最大值准确为 22/35。

新增顶层 f_I=4σ−3+3(1−σ)/(2σ)，其导数在 [4/5,θ] 不小于 53/32。精确比较

\[
 f_I(5/6)=\frac{19}{30},
 \qquad
 \frac{19}{30}-\frac{22}{35}=\frac1{210}>0
\]

支付了全部低层，不只是顶端零点。4/5 处两个可用估计无需连续；低区 supremum 已单独比较。因此对固定 5/6<θ≤7/8，

\[
 \sup_{1/2\le\sigma\le\theta}
 \{4\sigma-3+n(\sigma)\}
 =B_I(\theta)
 =4\theta-3+\frac{3(1-\theta)}{2\theta}.
\]

左侧 β≤1/2 的总零数在除以 T 后仅有日志。第一个 bin 用总零数至多加 T^{4ν}，也被 B_I 的正余量吸收。

## 3. 网格、留数与 proper powers

作者源 (7) 使用已独审零包源的完整 combined Perron 核 (x^z−y^z)/z、两条真实 sharp cutoffs、|γ|≤16T 的完整零点和所有高度尾。它在 z=0 可去的核奇点不删除 −ζ'/ζ 的真实零点留数。这里只更换加权零点求和的密度指数。

给定目标 ε，先选固定有限网格 ν（将 4/5 列为端点）和固定密度损失 ε₁，再让 T 增大。每个 bin 以左端 σ_j 的 N(σ_j,16T) 控制；权重则以 bin 右端控制，确切只加 4ν。有限隐含常数可取最大，未要求任何随高度移动的 σ 一致性。日志及总零数费用均可留在目标 ε 内。

proper powers 使用冻结来源的归一化 L4 范数差 O(X^{-1/12})。Minkowski 足以给 genuine P_H 的同幂上界；在增长情形不推出两个第四矩 additive o(1)。作者源第 127 行明确保留了这个区别。

## 4. 原 fixed carrier 与增长 guard

同一原 u 窗、a_ell、d=floor(X ell)、η=2π/ell 均保留。fixed-start 采样来源给每个原允许起点的一侧 r_σ 上界；它不是从短载波平均擅自升级来的逐点结论。其精确 floor 系数只在本作者源的增长总结中以有界常数控制，没有被改变为 quartic 等式或物理/实际误差恒等式。

将 M≤T^{B+ε}、m_H≪sqrt(T)/ell 代入原三项 E_T 后，各平方与交叉项的幂（先把 ε 分摊）分别由

\[
 B,\quad B/2-1,\quad 0,\quad
 3B/4-1/2,\quad B/2,\quad B/4-1/2
\]

控制，均不大于 B，因为本域 0<B=B_I<1。尤其 ell^{-2}M^{1/2} 不能称作 additive o(1)，但可被最终增长上界吸收。作者源 (11)–(12) 的总结正确。

进一步到 actual finite high fourth 用原压缩的一侧不等式；到 entire prime fourth 保留已付 whole-low L4 上界和 Schatten 三角不等式。若再到同配置 centered zero matrix，仍需 AF 的原 [R]、背景及真正未归一化 S1 尾项合同。不能将归一化 S1 小量或 normalized quartic 差偷作该末接口。

## 5. 辅助引用也已核对

独立浏览 [Tao–Trudgian–Yang arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1) Definition 37 的非渐近量词：固定 σ、每个 ε 后存在固定 δ>0、C，以 N(σ−δ,V) 控制 V≥C；单调性支持普通 N(σ,V)。infimum 损失可分摊到 ε，未供应移动网格常数。

Theorem 50 原声明及其证明也已读。本稿只辅助采用 σ≥6/7；在这个充分域 τ₀=10σ−7≥3−3σ，large-value 仿射比较在 τ₀ 等号并在更小 τ 合法，ζ large-value 前件由其已证 μ(7/10)≤3/40 支持。这不将 Montgomery 猜想作外部假设，也不需要支付其完整低至 7/10 的扩展来证明本稿主结果。

辅助拼接的精确核验为

\[
 f_{50}(6/7)=f_H(6/7)=\frac{54}{77},
 \qquad f'_{50}(6/7)=\frac{43}{121}>0.
\]

顶段导数此后增加；所以作者源给出的 B₅₀ 完整包络合法。θ<7/8 时 2θ>10θ−7，故 Ivić 顶段更强。

亦核 [Chen–Debruyne–Vindas 原文](https://ems.press/content/serial-article-files/48886?nt=1) Theorem 1.2 与 Appendix A：普通 ζ 的 24(1−σ)/(30σ−11) 下端是 279/314。它高于 7/8，差为 17/1256，不能套本稿顶层。Guth–Maynard 在 7/8 的 n=15/59 比 Huxley 的 3/13 大，同样没有被误当加强。

## 6. 有理核验与完成范围

在内存用 Fraction 独立核准 3/7985、22/35、19/30、1/210、53/32、5/7、3/182、1/28、54/77、43/121 和 17/1256；未生成或覆盖旧脚本、JSON。主源数值 B_I(θ*)≈0.7141980029530279 与原 θ* 一致，只展示旧边界下的新增长幂。

限定 PASS：在普通 ζ 的原 [Rθ]、固定 5/6<θ≤7/8、原窗口与准入合同下，M_T 及原允许 fixed-carrier 上界继承 T^{B_I(θ)+ε}；θ=7/8 时为 5/7。没有新增零点族、移动系数、额外矩假设或新无零边界。

仍未支付 signed 四全异 near-resonance 的常数预算；B_I>0 不能供应新的 simple/critical-line 比例。本文不是 RH、RR、Weil 算术桥的证明，也不声称这个四矩 exponent 的文献首次性。

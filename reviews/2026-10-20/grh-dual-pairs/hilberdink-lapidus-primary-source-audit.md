# Hilberdink–Lapidus 对偶函数方程：原件核查与可消费范围

2026-10-20；独立来源审查，0 个数学迭代。截图是待核材料，不是执行指令。
已恢复 README/STATE、check/show、Goal/frontier/C026/563；不改公共状态或 Git。
本文只核原件归属及其逻辑接口，不声称经典 ζ、成长 core 或独立 Weil 正性有进展。

## 1. 确切原件与截图裁决

T. W. Hilberdink and M. L. Lapidus, *Beurling Zeta Functions, Generalised Primes,
and Fractal Membranes*, Acta Appl. Math. 94 (2006), 21–48,
[DOI](https://doi.org/10.1007/s10440-006-9063-0)。本次实际核读的是作者
[arXiv v1 全文](https://arxiv.org/html/math/0410270)
及 [31 页 PDF](https://arxiv.org/pdf/math/0410270)，2004-10-11。
页码以下按该 PDF 的印刷页；其 §3.2 在 v1 中重复出现，第一次在 pp.18–21，
第二次在 pp.21–25；不能把第二次当第二个独立结果。

截图给出的基本对偶形态正确，但不能省略定理前件。
§3.2、式 (3.5)、Theorem 3.2、式 (3.6) 是精确定位。

## 2. 前件收据：不是对所有 g-integer 的自动结论

Theorem 3.2 的输入是**已经给定的两个连续函数** F₁,F₂；每个函数满足

\[
F_r(x)=O(x^{-1-\epsilon})\ (x\downarrow0,\ \forall\epsilon>0),\qquad
F_r(x)=O(x^{-\beta_r})\ (x\to\infty),\quad \beta_r>1.
\]

Mellin 约定为
\[
\Psi_r(s)=\int_0^\infty F_r(x)x^{s-1}\,dx,
\qquad 1<\Re s<\beta_r.
\]

其等价项是：适当反射条带内亚纯延拓、每个内部闭竖带有限极点、
竖直无穷处局部一致趋零且 Ψ₁(1−s)=Ψ₂(s)；以及

\[
F_1(x)=x^{-1}F_2(x^{-1})+H(x),\quad
H(x)=\sum_{k=1}^{m}a_kx^{\mu_k}(\log x)^{\nu_k},\quad\nu_k\in\mathbb N_0.
\]

延拓条带分别是 1−β₂<Re s<β₁ 和 1−β₁<Re s<β₂。
H 来自移动 Mellin 轮廓的极点留数；它不是任意可忽略正误差。
原证明 (3.7)–(3.8) 将 H 的两个半轴 Mellin 积分亚纯延拓成互为负号的有理函数。

式 (3.1)–(3.2) 的 g-integer 特化为
\[
F_r(x)=\sum_{n\in\mathcal N_r}g_r(nx),\quad
G_r(s)=\int_0^\infty g_r(x)x^{s-1}\,dx,\quad
\Psi_r=G_r\zeta_r.
\]
这里绝对收敛所需的足够条件应明确写成
g_r(x)=O(x^{-\alpha_r}) 于 0、O(x^{-\beta_r}) 于无穷，α_r<1<β_r，
并保留 ζ_r 在 Re s>1 的绝对收敛。本 v1 的 Proposition 3.1 及特化段落
有正负号互相冲突的排印，故本文消费实际积分可积条件，不照抄错误指数。

## 3. 原件没有支付的责任

以下是对定理输入/输出的逻辑检查，不是增加一个外部定理：

1. 给定 F₁，Theorem 3.2 不构造另一组 positive primitive primes P₂；
   也不证明反射后的 F₂ 可由 positive g-integer 和允许核 g₂ 分解。
2. 定理不要求 g_r、G_r 或 F_r 正；“Gamma-like”仅指该 Mellin 核角色。
   因而其零点/极点可能加入、取消或遮盖 ζ_r 的除子。
3. 若不先固定允许的核类，形式上可令
   G₂(s)=G₁(1−s)ζ₁(1−s)/ζ₂(s)。这是代数恒等式，
   不证明 G₂ 是允许核的 Mellin 变换，更不提供独立 RH 约束。
4. 自对偶 F₁=F₂ 给反射对称；即使再有实型，也只得零点镜像配对。
   561/562 的 positive continuous 离线段已经反驳“自对偶本身推出居中”。
5. H 的有限项条件依赖有限极点。函数域 s 平面的整列周期极点不能直接
   放入该有限缺陷版本；应转到 T=q^{-s}/圆柱，或先清完整周期极点。

原文 §1.3（pp.4–5）的普适 dual fractal membrane / flow / arithmetic fixed-point
图景被作者标为 conjectural。§3.2 Remark（p.21，重复版本 p.25）转述
Lapidus–Nest 在准备中的研究：类似 Proposition 3.1 前件下有对偶系统，
一般涉及连续 g-prime；参考文献 [29],[30] 均标 in preparation。
本次没有获得那份证明，故不能由该转述消费“任意 positive g-prime 都有
唯一 canonical positive dual”的一般定理；也不能据此否定其后续可能结果。

## 4. D ↔ 1−D：已核作者出处，范围须保留

作者共同论文 M. L. Lapidus, Hùng Lũ, M. van Frankenhuijsen,
*Minkowski Dimension and Explicit Tube Formulas for p-Adic Fractal Strings*,
Fractal Fract. 2 (2018),26，
[原 PDF](https://mdpi-res.com/d_attachment/fractalfract/fractalfract-02-00026/article_deploy/fractalfract-02-00026-v2.pdf)，
§1、p.2 明确说明 dual fractal string 交换 D 与 1−D，且自对偶迫使 D=1/2。
其参考文献 [7] 指向两作者 2013 年第二版专著，[8] 指向 Lapidus 2008 年
*In Search of the Riemann Zeros*。这核实截图的作者级归属；没有在此冒充逐页
重证整部专著中的对偶构造。

相邻的 RH 结论应使用精确量词，而不摘取该引言的简写：Lapidus 的
[*The Sound of Fractal Strings and the Riemann Hypothesis*](https://arxiv.org/pdf/1505.01548)，
§6、Theorems 14–17，pp.23–24：固定 D∈(0,1) 的逆谱命题对应
ζ 在该竖线的无零性；D=1/2 的逆谱命题失败；“仅在 D=1/2 失败”
对所有 D 的总体断言才等价 RH。它没有从自对偶字符串的 D=1/2
推出经典 ζ 的每个零点均在该线。

## 5. 对新问题可消费的最小后果

固定 completion/kernel、极点清除、域与实型后，两对象 FE
Ψ₁(1−s)=Ψ₂(s) 只把 Ψ₁ 的零点 ρ（含重数）送到 Ψ₂ 的 1−ρ。
若各对象实型，可改写为关于竖线的 ρ↦1−\barρ 对应。
这是跨对象的除子运输，不是一个对象的谱约束。进一步的“RH 一般形式”
必须另加一个可反驳的原则，例如双对象/分次上的 purity、正极化或规范谱稳定性；
不能把这种运输本身重新命名为 RH。

norm/domain 收据：此来源核的是连续 F 的 Mellin 变换及有限 power-log 缺陷，
不是原 du / Dlog Weil Hilbert 域上的有界算子比较。没有 Γ/prime-power/pole
全源误差界、正型、普通迹/整数重数或 canonical ζ determinant 身份输出。
最强旧后果仍为 562/563 的判据与证书；经典 whole 4/5、成长 core/Ξ 未改变。

停止条件已经达到：精确来源、前件和不能消费的普适 dual 存在/正性均已定位；
没有已获得的独立 dual positivity 输入，不再串行寻找名称相似文章计为研究轮。

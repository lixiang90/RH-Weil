# 原二阶证书的可加谱尾、实际效果对偶与固定条带的几何范围

2026-10-08。基线为 2d5621dbc999e0cf313ea224b825d6d56547c45c。
本篇只新增研究源；不改 197、304、既有比例或冻结的四矩研究。

研究结论：原 rank--trace 证明可同时保留 simple Gram 的 Schur--Jensen
余项与完整算子的负尾、超过 2 的正尾，得到一个不使用四阶上界的实际
二阶证书及非交换效果对偶。固定 7/8 条带不提供其正密度下界，也不改变
304 的实轴三点核。现有固定位置权重、low-only 线性平方效果不能付出
正的主项。没有得到新实际零点比例、完整 fourth upper 或新无零边界。

[T] 以下完整有限证明；[R] 所列原二矩及已付 mixed cubic 接口；
[O] 实际谱尾的非零渐近下界与本结果的新颖性。没有把有限谱恒等式称为
新的算术估计，也没有重建弱于既有文献的 tiny-mu 比例。

## 1. 实际来源与范围

Markdown 按 UTF-8 canonical LF 计算 SHA256；PDF 绑定原始字节。

| 实读来源 | SHA256 |
|---|---|
| [197 partial Weil](../../notes/197-partial-weil-proportions-regions-four-moments.md) | 98bd8ea89679030e0ffb8135d324b5654900f260b3f45c9ae816d5ea870eaae7 |
| [304 三点几何](../../notes/304-mt-triple-geometry-and-second-moment-stability.md) | 03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4 |
| [305 文献比较](../../notes/305-post-6725-literature-baseline-audit.md) | fab0841ee5734d35db023f0b1305bf75f9b19fcd11feda2ff08c73b2562d1aa9 |
| [AF v2 原论文](../../literature/baseline/2026-alpoge-furman-6725-v2.pdf) | 6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444 |
| [454 actual weighted second](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [entire mixed cubic](../2026-10-07/hybrid-background-entire-mixed-cubic-research-compression.md) | 19c715587681c95c3e8750e4751a30bff798b372f68dc516f029c0a5e71020dd |
| [relative actual cubic recovery](../2026-10-07/hybrid-background-cubic-relative-actual-recovery-research-compression.md) | 1dbdad713d2694d9fce6391971fc0044fcbf18d0ad3dbdd2d3fba5111ba80d38 |

AF §§2--4 的对象为原标量 interval carrier 的有限矩阵，不是完整 Weil
正性：simple on-line 列形成 P，重复实点及 off-axis 共轭对形成 Q，
完整 prime/Gamma/pole 矩阵仅以已付 trace-norm 小尾恢复该有限零点矩阵。
304 §5 的对象为固定平滑窗口下全部前缀零点特征的有限实张成；其一阶迹
恰为 N，二阶 HS 由固定测试函数的无条件全零点相关公式支付。
二者分别使用各自已经验证的计数与矩输入，不同定其未知第四迹。

305 已登记同类更强三点、多点证书。本篇不主张重新发现该机制；下面
新增的是同一证明中能安全同加的完整谱尾与实际低度效果接口。

## 2. 完整有限二阶尾耦合

令 A=P+Q 为 Hermitian，P=VV* 半正定，V 有 s 列，p=tr P，
n_+(Q)≤b。列可以相关、范数也不必等于 1。记 G=V*V，补零维使 d≥s+b。
定义

\[
 j(t)=(t-1)^2-(t-2)_+^2,\qquad
 \kappa_2(t)=t_-^2+4t_-+(t-2)_+^2,
 \quad t_-:=\max(-t,0).
 \tag{1}
\]

j 在 [0,∞) 上凸且为 2-Lipschitz；κ₂ 在整个实轴凸、非负，在 [0,2] 为零。
有以下**同一实际矩阵**不等式：

\[
 \boxed{\ 4\operatorname{tr}A-\operatorname{tr}A^2
 \le4b+2p+s-\operatorname{tr}j(G)-\operatorname{tr}\kappa_2(A).\ }
 \tag{2}
\]

证明。把 A 的降序谱记 λ_i，P 的谱补到 s 项记 p_i≥0。原最小最大原理
给 λ_{i+b}≤p_i，i>s 时 p_i=0。置 F(t)=4t-t²，并置

\[
 \phi(p)=\begin{cases}4p-p^2,&0\le p\le2,\\4,&p\ge2.\end{cases}
 \qquad \phi(p)=2p+1-j(p).
 \tag{3}
\]

对任意 λ≤p、p≥0，有 F(λ)+κ₂(λ)≤φ(p)：

* λ<0 时左边为 0；
* 0≤λ≤p≤2 时差为 (p−λ)(4−p−λ)≥0；
* 0≤λ≤2≤p 时差为 (λ−2)²≥0；
* 2<λ≤p 时左边恰为 4。

前 b 个谱槽位独立满足 F(λ)+κ₂(λ)≤4。后续超过 s 的槽位有 λ≤0，
左边为 0。逐槽求和、使用 Σp_i=p 及 (3)，得到 (2)。证明不使用
operator convexity、不删负谱、不交换 P 与 Q，不要求 A 半正定。

特别地，负谱成本 4tr A_-+tr A_-² 与正尾 tr(A−2I)_+²可以和
tr j(G) 同加。只有原同一槽位的不等式支持这项可加性；不能再把其他
对同一个 j(G) 的配对/多点下界重复相加。

## 3. 原计数账本与三点接口

在 197 的有限账本 p+2b≤N+E₀、s+2b≤N+E₁、D≥s+b、p≤s 下，(2) 给

\[
 s\ge4\operatorname{tr}A-\operatorname{tr}A^2-2N-2E_0
          +\operatorname{tr}j(G)+\operatorname{tr}\kappa_2(A),
 \tag{4}
\]

\[
 D\ge\tfrac12\bigl(4\operatorname{tr}A-\operatorname{tr}A^2-N-E_1
          +\operatorname{tr}j(G)+\operatorname{tr}\kappa_2(A)\bigr).
 \tag{5}
\]

(5) 使用 4b+2p+s≤4b+3s≤N+E₁+2D，不用可能错误的 D≥(N+s)/2。
在 304 的完整固定平滑配置，p=s、tr A=N、E₀=E₁=0，故

\[
 \operatorname{tr}A^2-2N+s
 \ge\operatorname{tr}j(G)+\operatorname{tr}\kappa_2(A).
 \tag{6}
\]

如果使用 304 已有的三点证书 M(B,µ) 与不交块箱数 m，则
tr j(G)≥(µ/2)s−µm，直接得到

\[
 s\ge\frac{2N-\operatorname{tr}A^2-\mu m+
                     \operatorname{tr}\kappa_2(A)}{1-\mu/2}.
 \tag{7}
\]

这保留两项不同来源的成本；不调整原三点 µ。只有另证实际
c_tail=liminf tr κ₂(A_T)/N(T)>0 才能给额外比例增益。当前没有该下界。
即便存在个别离线零点，也不能推出 c_tail>0；本篇不将 (7) 作为新比例。

原 AF 的 on-line 单列在有限 carrier 中范数≤1。令 G∞ 为同一批 simple
点在无限 interval Fourier basis 中的 Gram，Gc 为原 d 列压缩后的 Gram，
则 G∞−Gc 是漏出列的 Gram，半正定。因 j 为 2-Lipschitz，

\[
 \operatorname{tr}j(G_c)\ge\operatorname{tr}j(G_\infty)
                         -2\operatorname{tr}(G_\infty-G_c).
 \tag{8}
\]

对原 I′=[T−√T,2T+√T]，outside-I 的 simple 点数 O(√T log T)，
inside-I 的 packet tails 由原 C² 估计和单位高度计数求和。故 (8) 的
损失 o(N)。G∞ 的实轴核是原 φ²/(aL) 的 Fourier transform；它与 MT 核
在实轴的一致误差 O(1/L) 只用于固定三点块：每块的三项平方下界损失
O(1/L)，总块数 O(N)，所以总损失 o(N)。不以逐条目误差声称完整
Gram 的 trace-norm 接近。这里保留真实零延伸 carrier；
没有将它换成全局 frequency band 或假设它与 prime shifts 交换。

## 4. 可计算的非交换效果对偶

对每个实际有限 Hermitian A，以下变分式精确成立：

\[
 \operatorname{tr}\kappa_2(A)=
 \sup_{B,C\succeq0,\ 0\preceq D\preceq I}
 \left\{2\operatorname{tr}B(A-2I)-\operatorname{tr}B^2
       -2\operatorname{tr}CA-\operatorname{tr}C^2
       -4\operatorname{tr}DA\right\}.
 \tag{9}
\]

证明平方项的标准变分公式，可直接用谱基中的标量完成平方：
tr(A−2I)_+²=sup_{B≥0}(2tr B(A−2I)−tr B²)，
tr A_-²=sup_{C≥0}(−2tr CA−tr C²)。谱基的非对角 B、C 条目只增加
平方成本；PSD 保证对角非负。另有 tr A_-=sup_{0≤D≤I}(−tr DA)。
三份变量独立，最优值分别由 B=(A−2I)_+、C=A_-、D=1_{(-∞,0)}(A)
达到。任意选定的有限 PSD 效果都给严格下界，不要求它们与 A 交换。

例如任意 orthonormal 原 carrier vectors w_j，标量 Jensen 给
tr κ₂(A)≥Σ_j κ₂(w_j*Aw_j)。如果已计算的 Rayleigh 商大于 2 或小于 0，
就有可审计的有限成本。此说法不保证正密度多的这类向量存在。

令 E 的第 k 列为 L⁻¹/² 1_{[-L/2,L/2]}(u)e^{iα_ku}，
α_k=T+2πk/L，k=0,...,d−1；它是原零延伸 interval carrier。
原 all-height prime/Gamma/pole 矩阵可写

\[
 A_\nu=F^*\frac{2\pi\nu_X}{aL}F,
 \quad F=\mathcal F M_\phi E,
 \quad F_k(t)=\frac{\widehat\phi(t-\alpha_k)}{\sqrt{2\pi L}}.
 \tag{10}
\]

于是 (9) 的每个 tr AνZ 均为
(2π/(aL))∫ν_X(t) tr(F(t)Z F(t)*)dt。Γ multiplier 全局无界，但这里
每个 C² packet 衰减 O(|t|⁻²)，有限和乘 log(|t|+3) 可积；(10) 是良定义
的有限矩阵/有限域拉回，不需要声称整个 Γ multiplier 为 bounded operator。
所有 prime 项仍为同一有限 n≤X sum，pole 与 Γ 也同时保留。

这给实际 prime-side 线性响应及已知 effect-square 成本，避开 full fourth。
以 A 的未知谱效果作最优变量只是精确重写；若要渐近增益，须提供由实际
算术控制的效果及其正收益，不能将优化式本身记为该收益已经支付。

## 5. κ₂ 的恢复只需二矩

对任意同维 Hermitian A,B，Hoffman--Wielandt 及标量导数界给

\[
 \frac{|\operatorname{tr}\kappa_2(A)-\operatorname{tr}\kappa_2(B)|}{d}
 \le(4+2\|A\|_{2,d}+2\|B\|_{2,d})\|A-B\|_{2,d},
 \quad \|A\|_{2,d}^2:=d^{-1}\operatorname{tr}A^2.
 \tag{11}
\]

具体地 |κ₂(x)−κ₂(y)|≤(4+2|x|+2|y|)|x−y|，对排序特征值求和再
Cauchy。补零维不改变 κ₂ 迹。这无需全局 operator bound 或四矩。
AF 原 zero-side trace-norm tail o(1) 与已付 normalized second 因而支付
κ₂/d 的 all-height 恢复。Flat profile 也可由已付 background second、
proper-power op O(1/L) 恢复 Aν=I+H+L+o_{S2,d}(1)，再用 (11)。
MT profile 必须保留实际 bounded background；不能把它改成 I。

## 6. 固定 7/8 条带的实际作用

采用原无零输入和函数方程，只用其较弱结论 |β−1/2|≤d₀=3/8。
304 坐标 z=−i(ρ−1/2)log T/(2π) 下，|Im z|≤3log T/(16π)，
不是固定窄带，也不是 o(1)。所有 simple on-line Gram 条目仍严格为
同一个实轴核 Kδ(x_i−x_j)；条带没有约束这些实间距，故不能直接提高 µ。

对完整 Hilbert packet v_z=η(u)e^{-2πizu}，η 实偶、∫η²=1，写
d=|β−1/2|、L=log T、g=(v_z+v_barz)/2、h=(v_z−v_barz)/(2i)。则

\[
 g\perp h,\quad
 M(dL):=\int\eta(u)^2\cosh(2dLu)\,du,
 \quad \|g\|^2=\frac{M+1}{2},\quad\|h\|^2=\frac{M-1}{2}.
 \tag{12}
\]

该未压缩单对 2m(g⊗g−h⊗h) 的谱为 m(M+1)、−m(M−1)。支撑
[-1/2,1/2] 给 M≤cosh(dL)，但没有 M−1 的正下界。d→0 时负特征成本
趋零。对随 L 变化的原 AF 归一化 profile η_L(s)=φ(Ls)/√a，固定
d>0 时原 taper 的固定物理长度 endpoint 子区间给 M≥c_d e^{dL}/L。
对 304 的固定 ηδ，端部已有固定 δ 切除，本篇不声称该同指数下界；
上述一般 cosh 上界仍成立。因而 strip 不推出 near-line 特征近似。
只有 dL=o(1) 才由 cosh x−1≤x²e^{|x|}/2 得到 M−1=o(1)。
有限 carrier 压缩后 g、h 一般不再正交，多个 pair 与实点的谱也不能
逐项相加。因此 (12) 不是 tr A_- 的下界，更不是 off-axis count 的可见性。

连 termwise positivity 也不能由任意非零条带恢复：MT 实轴核的任意
非可去简单实根 a 满足 K₀′(a)≠0，所以
Re K₀(a+iy)²=−y²K₀′(a)²+O(y⁴)<0 对充分小的非零 y 成立。
这仅检查真实 kernel 的几何，未声称实际零点出现在该位置。

条带确实改进原 zero-feature 误差的上界：原 C² packet square 中
X^{1/2} 可换成 X^{d₀}。保持原 √T collar，原 tail proof 给
||E||₁≪X^{d₀}T⁻¹=O(T⁻⁵/⁸)，trace error 给 O(X^{d₀}L²)，另计
collar 点数 O(√T L)。这些仍为 o(N)，只改 convergence rates，不改变
R_MT、s+2b≤N 或 kernel 三点常数。不能把误差改进改称渐近比例增益。

## 7. 已付实际数据检验的效果方向

先限 flat 的实际 A，不将此检验无条件移给 MT。对任何固定 complex
x,z，V=xI+zL，B=V*V≥0。Low fourth 已付，故 B 的 normalized HS 有界；
(11) 所用 flat 恢复在 tr AB 中也合法。已付 τL=τH=τHL=o(1)、
τL²=1/6+o(1)、τL³=o(1)、τHL²=o(1) 给

\[
 \tau AB=|x|^2+\frac{|z|^2+2\operatorname{Re}(\bar xz)}6+o(1),
 \qquad
 \tau B(A-2I)=-|x|^2-\frac{|z|^2}6+
                         \frac{\operatorname{Re}(\bar xz)}3+o(1).
 \tag{13}
\]

两份 Hermitian quadratic forms 分别正、负定：其 Schur complement 为
1−1/6=5/6。因此 B 的正尾线性收益已为负，负尾效果 C=B 的线性收益
也为负；再减 square 成本不能得到正主项。此为原有限算子的已付词计算，
不是 abstract tensor 或另一个假想零点模型。

固定正 smooth row mark 的方向也相同：原 carrier multiplication effect
B=E*M_fE≥0，flat background 的 τAB−τB=o(1)。Prime weighted first
可由原 bounded overlap 与 Dirichlet kernel 绝对估计及两-P leakage 支付：
kernel 的 endpoint denominator 被 overlap (L−log p)/L 抵消，剩余
O(d⁻¹ Σ_p|b_p| L/log p)=o(1)；cross fee≤ell_f ell_prime/d=o(1)。
于是 τB(A−2I)=−τB+o(1)、−τAB=−τB+o(1)。这里 f 固定、非负且
有 bounded smooth/BV seminorm；不声称对随 T 任意变化的 spectral effect 一致。

若 V=xI+yH+zL，加入 H 的平方成本涉及未知 high fourth；在
a_T=o(L²) 使已付 relative high cubic 成为 o(1) 的范围，使用 454 真正
weighted second 恢复，线性收益的 Schur gap 为 1−1/6−1/6=2/3，仍不为正。
在没有该增长前件时不删 relative cubic error，不使用小 S2 background
误差乘未知 H² 来代替 weighted-second 证明。现有 K、W 和 low fourth
尚未支付其他 PSD/contraction effect 的正收益；由 qstar fourth lower
也不能免费推出 [0,2] 之外的 quadratic tail。

## 8. 本轮完成项与未付对象

已完成同对象有限式 (2)、原计数式 (4)--(8)、非交换精确对偶 (9)、
只需二矩的 κ₂ 恢复 (11)、完整特征的条带量纲和误差核对，以及原
low/row 效果的实际主项方向检验。四阶全局算术目标仍由 471 的
signed four-distinct 净项控制；本篇没有替它支付上界。

可执行的新路线是寻找原 finite carrier 中、positivity 可直接验证的效果，
使 (9) 的线性响应减已知 square 成本有正密度收益。其未付对象是该
具体收益的 actual 算术下界。固定 7/8 strip、现有 bounded row effects、
low-only linear squares 均没有提供它；不另引入新 correlation assumption。

本篇是作者完整证明与范围核对，尚待其他作者独立全文审查；不能自行
记独立 PASS，也没有运行新的大规模零点、外部多点证书或 Lean 工程。

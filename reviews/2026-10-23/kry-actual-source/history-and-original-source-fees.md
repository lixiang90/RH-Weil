# KRY 实际源候选：历史扣除、Gaussian 像与原费用

2026-10-23；独占分支，供 root 审核，不更新 STATE 或 cadence。输入为 KRY1999 已消费的 Mellin 身份、405/537/545/552/553；本文不按 Q 或零点选择映射。所得是一个具体候选的解析接入检验，不是算术 cycle lift 或独立 Weil 正性。

## 1. 历史扣除与本次实际测试

已读 [405](../../../notes/405-f1-adelic-restriction-moments-and-radical.md)、[523](../../../notes/523-f1-natural-hilbert-collapse-and-growth-gap.md)、[545](../../../notes/545-modular-packet-norm-cusp-blindness-and-weil-transport-gate.md)、[552](../../../notes/552-radial-adelic-green-principal-and-comparison-gate.md)、[553](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md)及[上轮 KRY 来源门](../../../goals/reviews/2026-10-23-arithmetic-theta-capacity-source-admission.md)。定点检索 notes/reviews/goals 中 Gaussian dilation、Mellin、sech/cosh、Gamma 与 Carleman；未定位与下面 R² map 完全相同的已消费公式。不把关键词未命中当作世界新颖性证明。

必须扣除的强旧结论：

* 405 已有实际 Gaussian/Poisson 源关系，不以目标型定义；其全部平移合法。physical 坐标 r=e^{u/2}f 中 p_phys=e^{u/2}(D²+D)h=(D²−1/4)(e^{u/2}h) 非零。
* 523/553 已给这些 physical 全 Pan 关系的平移 span 在原 du 和 Hlog 中稠密。因而一个全域 du/Hlog 连续、正确消去所有关系的 Hausdorff Hilbert 读出必为零。这不是本次新定理。
* 552 的真实 radial adelic metric 存在，但其 energy 不消关系；t² 与完整 Γ 的 log|t| 频率费用失配。不能再把“合法度量已存在”记作未解决问题。
* 545 §3 的逆乘子域反测不能排除 §4 的 direct vector compensation；后者已付全轴原 du upper。下面也必须保留相同逃逸。

本次可判的具体问题是 R² Gaussian scale map 是否已提供一个可继续接到 primitive cycle 的合法源、关系与原费接口。其原 du 上界与准确 smoothing 可直接算出；raw map 不消关系，bounded primitive quotient 则由 553 全退化。这个结论只限制明确范围。

## 2. 确切对象、Gram 与 Mellin 因子

在 H=L²(R²,dx) 的 radial 子空间定义

\[
 (Tr)(x)=\int_{\mathbb R} r(u)e^{u/2}e^{-\pi e^u|x|^2}\,du,\qquad
 r\in C_c^\infty(\mathbb R;\mathbb C).
 \tag{1}
\]

先在 compact 源上绝对换序。R² Gaussian 积分给

\[
 \langle Tr,Ts\rangle_H
 =\iint r(u)\overline{s(v)}\,k(u-v)\,du\,dv,
 \quad k(a)=\frac1{2\cosh(a/2)}.
 \tag{2}
\]

Fourier 约定始终 rhat(t)=∫r(u)e^{−itu}du，故

\[
 \widehat k(t)=w(t)=\frac{\pi}{\cosh(\pi t)},\qquad
 \|Tr\|_H^2=\frac1{2\pi}\int w(t)|\widehat r(t)|^2dt.
 \tag{3}
\]

一个不另引积分公式的核验是 log-radial 酉映射

\[
 (JF)(y)=\sqrt\pi e^{y/2}F(\sqrt{e^y}),
 \quad JTr(y)=\int r(u)a(y+u)du,
 \quad a(v)=\sqrt\pi e^{v/2}e^{-\pi e^v}.
\]

代入 z=πe^v 得 ahat(t)=π^{it}Γ(1/2−it)；Gamma 反射给 |ahat(t)|²=π/cosh(πt)。这也固定了维数、常数和反射方向。

(1) 因而唯一延拓为全 L²(du) 上的 bounded map，\|T\|²=π，而且 w(t)>0 a.e. 给 injectivity。T 并非普通 Weil 目标：它的完整频率谱平滑而衰减，不能只因正 Gram 就认作完整 Γ−prime+pole。

全部 real 或 complex 源均合法；原 Hlog norm 是

\[
 \|r\|_{Hlog}^2=(2\pi)^{-1}\int[1+\log(2+|t|)]|\widehat r(t)|^2dt.
\]

由 \|Tr\|²≤π\|r\|²，T 对 Hlog 同样连续，没有更换原 norm。

对每个 r∈S_exp，(1) 还是一个真实 radial Schwartz(R²) 函数。逐 x 导数的 Gaussian 估计和 r 的两端指数半范数支付每个 Schwartz 半范数，故有连续 S_exp→Schwartz 映射；这不声称 Schwartz 半范数由单一 du/Hlog 控制。直接换序另给

\[
 Tr(0)=\ell_+(r),\qquad \int_{\mathbb R^2}Tr(x)dx=\ell_-(r).
 \tag{3a}
\]

所以双 pole-zero 源自然进入在0与积分皆消失的真实 Schwartz 子空间。compact 源时逐项绝对换序最直接；S_exp 的带权绝对积分给同样结论。这是合法源接入，不自动等于 relative primitive descent。

## 3. 405 与 537 的第一门

由 injectivity，T(p_phys)≠0；对每个平移 τ_a p_phys 仍非零。这里 p_phys 属于真实 noncompact S_exp，不把它裁成 compact 像。因此 raw Gaussian map 若被直接当作最终 primitive 读出，已经失败全 405 主关系门。只消两个 pole 矩不会修复这个失败。这不排后续 theta/relative 操作使它成为正确的 principal 同构；本段只测试 raw map 本身及下述 bounded Hilbert quotient。

537 的实际 compact 双 pole-zero 非根 r₀=(D²−1/4)ψ，ψ∈C_c^∞((−17/16,17/16)) 非零，满足 Qζ(r₀)>0，也满足 Tr₀≠0。故 raw T 保留非根，但同时保留不该有值的全部关系；这不是 primitive lift。

如果另给 closed Hilbert base B⊂H 以及 du/Hlog bounded 线性读出 ΠT:L²(du)→H/B（或 Hlog→H/B），且它精确消去全部 physical Pan，那么由 553 的稠密性 ΠT=0，因而也杀 r₀。更一般地，只要求 Π 在 closure Ran(T) 上 bounded 已足够。这里使用的是一个固定全域读出及 closed Hausdorff quotient；强 Fréchet、unbounded regulator、变域或源依赖几何并未被排除。

因此“raw Gaussian source → bounded primitive projection”不是尚待试验的独立容量方案；其失败是旧 553 在具体 map 上的直接消费。也不能把 compact 窗内无 Pan 关系误作全关系已消：553 已给 P_an∩C_c^∞={0}。

## 4. 实际 compact 源上的 smoothing 与逆费用

固定非零 h∈C_c^∞(I)，I 为任一非空固定有限开窗。取两个同窗 smooth dual templates v_±，使

\[
 \ell_\pm(v_j)=\delta_{\pm,j},\qquad
 \ell_\pm(r)=\int e^{\pm u/2}r(u)du.
\]

两个不同位置的小 bump 的矩阵可逆，故这一步不使用 Q 或零点。定义实际源

\[
 r_\tau=e^{i\tau u}h(u)-\ell_+(e^{i\tau\cdot}h)v_+
                              -\ell_-(e^{i\tau\cdot}h)v_-.
 \tag{4}
\]

反复分部积分给每个 N 的两个修正系数 O_{I,h,N}(τ^{−N})。于是

\[
 \ell_\pm(r_\tau)=0,\quad
 \|r_\tau\|_{du}^2\longrightarrow\|h\|_2^2>0,
 \quad \|r_\tau\|_{Hlog}^2=\log\tau\,\|h\|_2^2+O_{I,h}(1).
 \tag{5}
\]

从 (3) 将 ξ=t−τ 积分分为 |ξ|≤τ/2 与其补集，利用 w 的指数下降和 hhat 的所有多项式尾，得到对每个 N

\[
 \|Tr_\tau\|_H^2=O_{I,h,N}(\tau^{-N}).
 \tag{6}
\]

这是实际像而非全空间 inverse norm 论证。不能无依据加强为 e^{−πτ}：compact 源的 Fourier leakage 可能主导该指数。

原实际完整型在同一源上为

\[
 Q_\zeta(r_\tau)=\log\tau\,\|h\|_2^2+O_{I,h}(1).
 \tag{7}
\]

理由是完整 Γ(t)=Re ψ(1/4+it/2)−logπ=log|t|−log(2π)+O(t^{−2})；fixed I 的全部 prime-power shifts 是一个 bounded 原 du form，而两 pole 在 (4) 精确为零。没有从定义删除 prime powers 或 poles。(7) 是 552/545 已付高频机制在此 map 上的消费。

因此 T 的 ambient H norm 不能以固定源常数反向控制 du 或 Hlog，甚至在固定窗和双 pole-zero 源上也不能。固定 bounded H energy 加 fixed O(\|r\|²) 也不可能覆盖 (7)。这不排除一个 genuinely unbounded arithmetic height、非局部几何或其他源接入；尚未构造这些对象，不能由本反测声称其费用必然不付。

## 5. 预逆与 direct 极分解必须分开

写 K=T*T=w(D)。如果方案明确要求先对输入取 K^{−1/2}r∈L²，则其精确 domain 要求

\[
 \int \cosh(\pi t)|\widehat r(t)|^2dt<\infty.
 \tag{8}
\]

(8) 给每个 a<π/2 的 holomorphic strip 代表；非零 compact r 不可能满足，因为它在一个实开区间恒零。因此该“先预逆再送入 T”的 L² source 操作对任何非零 compact 源都不合法；K^{−1} 的 domain 更小。

但这不是所有补偿的禁阻。T 的 polar factor U=TK^{−1/2} 在稠密 domain 组合后延拓为 L²(du) 到 radial H 的酉映射；log-radial Fourier 下只是 ahat/|ahat| 加反射。因 ahat 非零 a.e. 且乘子 range 稠密，延拓成立。直接定义 U r 没有源 inverse 的无穷费用，不能谎称不合法。

这个真实逃逸没有解决任务：U 仍 injective，U p_phys≠0；其 norm 是原 du，既不是完整 Γ能量也没有 finite-place cycle/primitive descent。若再接一个全域 bounded primitive quotient，§3 的 553 退化照旧。合法 direct normalization 与独立算术比较是两件事；545 已明确警告过这种区分。

## 6. KRY 算术逆的 actual finite Euler 作用

固定有限 primes F、σ>0，使用上轮已固定 χ。令

\[
 B_F(s)=\prod_{p\in F}(1-p^{-s})(1-\chi(p)p^{-s})
       =\sum_n a_F(n)n^{-s}.
\]

系数有限、真实且可 signed。对应原 physical 源操作为

\[
 A_{F,\sigma}r=\sum_n a_F(n)n^{-\sigma}\tau_{\log n}r,
 \qquad \tau_a r(u)=r(u-a).
 \tag{9}
\]

Fourier 乘子正是 B_F(σ+it)，故在 du 与 Hlog 都有完整 finite upper

\[
 \|A_{F,\sigma}r\|\le b_{F,\sigma}\|r\|,
\quad b_{F,\sigma}\le
 \prod_{\chi(p)=1}(1+p^{-\sigma})^2
 \prod_{\chi(p)=-1}(1+p^{-2\sigma})
 \prod_{\chi(p)=0}(1+p^{-\sigma}).
 \tag{10}
\]

事实上 (10) 的右边是 exact 全线 operator norm：log p 的 rational independence 及 finite-torus character criterion 给任意精度的共同 phase，分别趋近 split 的 −1、inert 的 i、ramified 的 −1。这是有限 F 的 supremum；没有称某个预定 fixed-window 源实现它。

实际 Gaussian 像也没有神秘换 norm。由 (1)

\[
 T\tau_a=\mathcal D_aT,
 \quad (\mathcal D_aF)(x)=e^{a/2}F(e^{a/2}x),
 \quad \|\mathcal D_aF\|_H=\|F\|_H,
\]

故 (9) 在真实像上是同一 finite unitary dilation 组合，并且

\[
 \|T A_{F,\sigma}r\|_H^2
 =(2\pi)^{-1}\int w(t)|B_F(\sigma+it)|^2|\widehat r(t)|^2dt.
 \tag{11}
\]

对实际 rτ，(9) 的 du norm 是各 shifted h 的完整 mixed correlation 和，不等于仅把 b_F² 当作其实际费用。尤其 h 的支撑宽度若小于有限 log n 之间的最小间距，像互不交叠，其 norm²恰为 \|h\|²Σ|a_F(n)|²n^{−2σ}，不依赖 τ 的相位；fixed 窗与 cofinal prime family 不可合并。

源支撑从 I 扩到 I+[0,2Σ_{p∈F}logp]；χ(p)=0 或其他抵消只可能缩小这个安全范围。两 pole-zero 在所有 shifts 下保持，因 ℓ_±(τ_a r)=e^{±a/2}ℓ_±(r)。这是完整 local Euler 因子的精确逆，恰为 degree≤2 的多项式，不是把原几何级数的高幂当误差截掉；二次项不能省略。KRY D_q 中的全部 Λ(p^k) 与临界 Γ/poles 仍由原完整身份负责，有限 F 的 (9) 本身不代它们。

当 σ>1 时，Σ|a_F(n)|n^{−σ}≤∏_p(1+p^{−σ})² 对 F 一致有限，因而有真实全线 du/Hlog bounded signed 极限。到 σ=1/2 不能搬运此一致费：(10) 的 exact norms 沿全部 primes 增长。split 因子至少给 1+1/p，inert 恰给 1+1/p，只有有限 ramified 例外；Euler 的 Σ1/p=∞ 已足推出 b_F→∞，不用未知零点。

如需 actual 源见证而非 operator 标签，可先固定 F，以归一化长 smooth packet h_L(u)=L^{−1/2}h(u/L) 使每个有限 shift 的 overlap→\|h\|²，再取足够大的共同 phase τ；两 pole 修正仍由 §4 模板精确完成，先固定 L 后令 τ 足够大使该修正任意小。du 与 Hlog 的同一 norm ratio 均可逼近 (10)。L、τ可依赖 F，不能由这组成长源断言某个 fixed 源的费用发散。

这些 upper/exact norms 不给 actual q_R 的 necessary lower，也不支付 signed cycle degree 的差/商。保全 Γ 的预逆、无穷 prime tail、临界 signed 抵消及相同 arithmetic height 仍须另证；不能用全空间 factor norm 大来代实际原源费用。

## 7. 连续正反例、函数域与停止范围

§2 map 和 Gram 不读取 g-integer 数据。故它在 562/578 的连续正例与负例上完全相同而且始终正。若据此不加新输入声称其 norm 等于 native 完整 Weil form，则负例的实际 compact 负源立刻反驳该识别。它们未接入 KRY 模对象，不能宣称通过了 KRY 几何前件或直接反驳 KRY 定理。

函数域真正的正号来自同一 C×C 的 mixed primitive 交数与 RR/Hodge，不来自任意 Gaussian source norm。保全部 Frobenius returns、周期 aliases 与 H⁰/H²极点后，是否有 source→same cycles 仍需具体映射；给一个 du isometry 不支付这项比较。

本分支付清：一个不按 Q/零点定义的 actual Gaussian source、准确全 du/Hlog upper、405/537实际检验、actual 高频费、direct polar 逃逸及 finite Euler 在真实像上的完整 mixed norm。未付：relative primitive 算术 cycle map、同对象局部过滤/截面 lift/RR二次容量、完整 Γ/pp/pole 身份及 actual q_R 消失。

上述候选公式可作为本轮具体输入，是否达到新数学轮由 root 扣强旧后决定；不能以“此前没有 sech 公式”认定新的独立容量。strong-old542+555→557 whole leading4/5仍只是负惯性上预算，core/coupling/Ξ及长期 Goal 门均未变。停止 raw Gaussian＋bounded primitive quotient／无费预逆入口，保 strong Fréchet、unbounded relative height、变域、direct vector 与实际 signed 同源恒等式等未排方案。

# 保完整 Γ 的窗化与有限高度正谱修补

2026-10-22；本分支独占固定窗候选的构造、完整 Γ 费用和连续谱修补。不改 STATE／cadence，不单独结算轮数。旧输入为 569 的指定 Fourier／有限部分、576 的正分布与原范数门、553 的全线关系稠密及 537 非根。

**结论。** 从有限素数幂、两极点与既定 Γ，可独立算出每层正型分布，而且保持 Γ 的完整穿孔奇性及指定 contact。具体修补是一个非负、紧支撑、连续的谱密度，不读取任何 ζ 零点。但证明这笔修补预算趋零，仍与完整 Weil 正性等价。本文另独立付清一个原范数模块：窗化与“整块 Weil 窗化”之差为负 L¹ 核，连其 Fourier L¹ 费用均为 O(R⁻²)。此估计无需 RH；将它用于控制实际负谱修补的那一步需要完整正性。

## 1. 对象、固定规范与明确窗口

用原 physical 源 r=e^{u/2}f，hat r(t)=∫r(u)e^{-itu}du，r*(u)=overline{r(−u)}；第一变量线性，Q_W(r)=W(r*r*)。Γ 的指定乘子是

\[
 \Gamma(t)=\Re\psi(1/4+it/2)-\log\pi,\quad
 \Gamma_0=\psi(1/4)-\log\pi.
\]

记 a(v)=e^{-v/2}/(1-e^{-2v})。569 已固定的完整分布为

\[
 W_\Gamma(h)=\Gamma_0h(0)+\int_0^\infty
 2a(v)\{h(0)-(h(v)+h(-v))/2\}\,dv.                 \tag{1}
\]

这包含指定有限部分及 contact，而非只取 log|t|。固定完整经典目标

\[
 W_\zeta=W_\Gamma+M,\quad M=H-P,\quad
 H=2\cosh(u/2)du,
\]
\[
 P=\sum_{p,k\ge1}(\log p)p^{-k/2}
      (\delta_{k\log p}+\delta_{-k\log p})
  =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
      (\delta_{\log n}+\delta_{-\log n}).             \tag{2}
\]

不能用 primes-only 项替代 P。两个极点亦不投影消去。

选实偶、非负、非零 η∈C_c∞((−1/2,1/2))，定义

\[
 \phi={\eta*\eta^*\over\|\eta\|_2^2},\qquad
 \phi_R(u)=\phi(u/R),\quad R\ge1.                  \tag{3}
\]

于是 φ∈C_c∞([−1,1])、φ(0)=1、0≤φ≤1、hat φ=|hat η|²/||η||²≥0。令 M_j=||φ^(j)||∞，κ=−φ''(0)>0。所有常数只依赖这个固定 η。

先定义不修补的实际层

\[
 V_R^0=W_\Gamma+\phi_R M,\qquad
 g_R(t)=\Gamma(t)+2\int\phi_R(u)\cosh(u/2)\cos(tu)du
  -2\sum_{n\le e^R}{\Lambda(n)\over\sqrt n}
        \phi(\log n/R)\cos(t\log n).               \tag{4}
\]

hat V_R^0=g_R。每个 k 次幂按原系数进入同一个窗，不删 proper powers；窗外余额是明确的 (1−φ_R)M，未宣称它为零。Γ 没有被窗化。R→∞ 时 V_R^0→Wζ 于 D′，这一步纯为局部有限测度与 φ_R→1 的事实，无需 RH。

## 2. 无零点的有限高度非负谱规则

记

\[
 B_R=\|\phi_RM\|_{TV}<\infty,
 \quad c_R=\max(0,-\min_{t\in\mathbb R}g_R(t)),
 \quad q_R(t)=(-g_R(t))_+.                         \tag{5}
\]

Γ 为实偶连续函数、趋向 +∞；其严格递增性可由

\[
 \Gamma(t)-\Gamma_0=
 \sum_{n\ge0}{(t/2)^2\over(n+1/4)((n+1/4)^2+(t/2)^2)}
\]

在 t≥0 逐项看出。选任意整数 T_R 使 Γ(T_R)>B_R+1，则 |t|≥T_R 时 g_R(t)>0。因而 q_R 为实偶非负连续紧支撑密度，c_R=||q_R||∞，且

\[
 0\le c_R\le\max(0,B_R-\Gamma_0).                  \tag{6}
\]

(4)–(6)只使用有限算术和、指定极点及 digamma；可以在 [−T_R,T_R] 上以误差界求值、求积。未用未知零点选择频率或系数。这个粗上界随 R 可以很大，不能据其有限性说误差变小。 由直接 TV 预算亦有 B_R≤8sinh(R/2)+2Σ_{n≤e^R}Λ(n)/√n=O(e^{R/2})（使用旧 Chebyshev 上界）；这只给可能很大的有限高度 T_R，不付成长费用。

**contact 修补。** V_R^δ=V_R^0+c_Rδ₀ 为正型，谱乘子 g_R+c_R≥0。但 c_Rδ₀ 是额外 contact，不能称该层已在固定完成化纤维中。

**保持 contact 的修补。** 定义

\[
 K_R(u)={1\over2\pi}\int q_R(t)e^{itu}dt,
 \quad \widetilde V_R=V_R^0+K_R(u)du.
                                                               \tag{7}
\]

K_R 是实偶光滑函数，所有阶导数由有限高度积分给出，且没有 δ₀ 或其他 point-supported 项。于是 Γ 的完整有限部分／指定 contact 都保留，

\[
 \widehat {\widetilde V_R}=\max(g_R,0)\ge0,\quad
 Q_{\widetilde V_R}(r)={1\over2\pi}\int\max(g_R(t),0)
                                  |\widehat r(t)|^2dt\ge0.\tag{8}
\]

这是一般连续正谱证书，并未证明它有通常整数重数 determinant，亦未证明修补后的 zeta 有非负 Euler primitive。原 Γ、P 与 H 是被比较的指定 summands；额外 K_R 的算术／几何身份及其消失仍待支付。

### 2.1 合法的 Schwartz 修补

若需要 physical 修补为 Schwartz，可进一步选实偶 ρ_R∈C_c∞([−2T_R,2T_R])，0≤ρ_R≤1，在 [−T_R,T_R] 恒1，并定义

\[
 q_{R,\epsilon}(t)=\rho_R(t)
 {\sqrt{g_R(t)^2+\epsilon^2}-g_R(t)\over2},\qquad
 \epsilon_R={R^{-2}\over1+2T_R}.                     \tag{8a}
\]

q_R 的负区间均在 [−T_R,T_R] 内，故 g_R+q_{R,ε}≥0；在外圈 g_R 本已为正，新增项亦非负。全线有

\[
 0\le q_{R,\epsilon}-q_R\le\epsilon/2,\quad
 \|q_{R,\epsilon}-q_R\|_1\le2T_R\epsilon.
                                                               \tag{8b}
\]

其逆 Fourier K_{R,ε} 是 Schwartz，无 contact；(8a) 完全由实际 g_R 及固定 cutoff 构造。取 ε_R 后新增谱质量≤R⁻²，新增乘子 norm≤ε_R/2。因此下文 RH 条件下的 O(R⁻²) 费用及消失预算⇔RH 对这个 smooth 版本仍成立（常数加上明确 O(R⁻²)）。这是支付了误差的真正平滑修复，不是未经核查的“抹平保正”。

## 3. 窗化协同误差：独立的 L¹ 及 Fourier-L¹ 费用

令

\[
 \mu_R(u)=(1-\phi_R(u))a(|u|)\ge0.
\]

由 (1)，(1−φ_R)(0)=0，严格得到

\[
 E_R:=(1-\phi_R)W_\Gamma=-\mu_R(u)du,\qquad
 V_R^0=\phi_RW_\zeta-\mu_R(u)du.                   \tag{9}
\]

这里不漏 contact：乘 (1−φ_R) 后指定 contact 为零。不能只拿穿孔 Γ 计算而任意改接触常数。

Taylor 给 0≤1−φ_R(u)≤M₂u²/(2R²)，故

\[
 e_R:=\|\mu_R\|_1\le {C_0\over R^2},\quad
 C_0={M_2\over2}\int_\mathbb R u^2a(|u|)du,
 \quad \int_\mathbb R u^2a(|u|)du
       =32\sum_{n\ge0}(4n+1)^{-3}.                \tag{10}
\]

因 μ_R≥0，卷积形式满足对全部原 du 源（不限制支撑）

\[
 |Q_{E_R}(r)|\le e_R\|r\|_2^2,
 \qquad \|Q_{E_R}\|_{L^2\to(L^2)^*}=e_R.          \tag{11}
\]

最后一个等号是 Fourier 乘子 norm：|hat μ_R|≤e_R 且 hat μ_R(0)=e_R。它不是说 E_R 的二次型总为负：μ_R≥0 只给物理核的符号，hat μ_R 可变号。

还可付比 TV 更强的

\[
 \|\widehat\mu_R\|_1\le {4\sqrt{C_0C_2}\over R^2}  \tag{12}
\]

，其中 C₂ 为固定、可显式积分的常数，证明如下。写 a(v)=1/(2v)+h(v)，h∈C∞([0,1])；记 H_j=sup_[0,1]|h^(j)|。令

\[
 A_{tail}=\int_1^\infty
   \{v^2|a''(v)|/2+2v|a'(v)|+a(v)\}dv<\infty,
\]
\[
 C_2={\kappa\over2}+{11M_4\over24}
        +2M_2\{H_2/6+H_1+H_0+A_{tail}\}.           \tag{13}
\]

对 b(v)=1−φ(v/R)，μ_R(v)=a(v)b(v)，且 μ_R(v)=κv/(4R²)+O(v²/R²) 于 v↓0。分布二阶导数因左右一阶导跳跃含 κδ₀/(2R²)。在 0<v≤1，奇性部分为

\[
 (b/(2v))''=b''/(2v)-b'/v^2+b/v^3.
\]

b 的 κv²/(2R²) 首项在该组合中精确抵消。φ 偶，四阶 Taylor 余项逐项给其绝对值≤(11M₄/24)v/R⁴。光滑余项 (hb)'' 用 |b|≤M₂v²/(2R²)、|b'|≤M₂v/R²、|b''|≤M₂/R² 控制。在 v≥1 用 a、a'、a'' 的指数尾；同一三项 Taylor 界对全部 v 仍成立。积分并加 δ₀ 跳跃，得到

\[
 \|\mu_R''\|_{TV}\le C_2/R^2.
\]

因此 |hat μ_R(t)|≤R⁻²min(C₀,C₂/t²)，在 |t|=sqrt(C₂/C₀) 分段积分即 (12)。这些估计全由实际 Γ 核及窗口给出，无 RH、无谱点选择。

## 4. 哪个箭头仍承担完整 RH

在 **RH／完整 Weil 正性前件** 下，φ_R 为正型且 Wζ 为正型 tempered 分布；乘积 φ_RWζ 仍正型。其 Fourier 为正谱与非负 Schwartz 核的卷积，是非负密度 k_R(t)。由 (9)

\[
 g_R=k_R-\widehat\mu_R,\qquad
 0\le q_R\le(\widehat\mu_R)_+\le|\widehat\mu_R|.    \tag{14}
\]

注意 (14) 的 k_R≥0 尚非独立支付；写成正谱卷积只是消费完整正性的一个方式。结合 (10)、(12) 可严格推出

\[
 c_R\le C_0/R^2,
 \quad m_R:=K_R(0)={1\over2\pi}\int q_R(t)dt
       \le {2\sqrt{C_0C_2}\over\pi R^2}.           \tag{15}
\]

反过来，若沿任意 R_j→∞ 有 c_Rj→0 或 m_Rj→0，均有 K_Rj→0 于 D′：前者用 Q_K≤c_R||r||² 及极化，后者直接用 |K_R(u)|≤m_R。于是 (8) 的正型锥闭及 V_R^0→Wζ 给完整 Weil 正性。因此，对这一个明确规则，

\[
 \boxed{\ RH\iff c_R\to0\iff m_R\to0\ }
 \quad\text{也等价于存在相应 cofinal 子序列趋零。}  \tag{16}
\]

c_R→0 的 D′ 结论亦可直接由 q_R≤c_R：对测试 h，|K_R(h)|≤(c_R/2π)||hat h||₁。每个有限 R 的数值和正性可独立检验；全 R 消失结论仍是完整目标责任。

若完整 Weil 正性为假，存在固定 compact complex r、Qζ(r)<0。下节原 fixed 窗误差给 c_R≥−Qζ(r)/||r||²−O_r(R⁻²)，故 liminf c_R>0。若 m_R 沿子序列趋零会违反正型闭性。不能把“每层都有无零点正修补”误写成“真实负谱预算已经支付”。

## 5. 原 du／Dlog 费用与量词

固定 L>0，supp r⊂[−L,L]，保持全线 zero extension 原 Hlog

\[
 \|r\|_{Hlog}^2=(2\pi)^{-1}\int
 [1+\log(2+|t|)]|\widehat r(t)|^2dt.
\]

令

\[
 D_L={M_2\over2}\int_{[-2L,2L]}u^2\,d|M|(u)<\infty.
\]

该常数含所有 n≤e^(2L) 的 proper powers 及完整双极点背景。由 |r*r*(u)|≤||r||²，直接有

\[
 |Q_{V_R^0}(r)-Q_\zeta(r)|\le{D_L\over R^2}\|r\|_2^2,
\]
\[
 0\le Q_{K_R}(r)\le c_R\|r\|_2^2,
 \qquad Q_{K_R}(r)\le m_R\|r\|_1^2\le2Lm_R\|r\|_2^2,
\]
\[
 |Q_{\widetilde V_R}(r)-Q_\zeta(r)|
  \le\{D_L/R^2+\min(c_R,2Lm_R)\}\|r\|_2^2.        \tag{17}
\]

这覆盖固定窗内全部 complex 源，不是逐源高频估计。用 ||r||₂≤||r||Hlog 得同一 Hlog 控制；转为仓库原 Dlog 保其既定等价常数，不更换 zero-extension 域。RH 前件下 (17) 为 O_L(R⁻²) 的原 du 全源误差，因此也为原 Dlog 全源误差。

这是“同一个固定窗上所有源”的统一结论，**不是全线所有支撑共同统一**。D_L 含成长素数幂／极点预算，不能当不依赖 L 的常数。每固定 R 的 V_R^0、K_R 在全线 Hlog 上有界；完整 Wζ 若也全线有界，因405全 Pan 被杀且553其全线 Hlog 闭包稠密，会迫使 Bζ=0，与537非根矛盾。因此在相同全线域上，每个 R 的完整差都不能有有限全局 Hlog operator norm。局部原 du 小费并未绕过原全线关系密度门。

(9)–(12) 的 E_R 却确有全线 du 小费；二者不矛盾，因为它比较的是 V_R^0 与 φ_RWζ，而不是完整 Wζ。不能将这笔已付费用跨越未付的 (1−φ_R)M 成长余额。

## 6. continuous± 与真实函数域对照

1. 取 Γ=0、完整目标 W=2cos(γu)du，保持其连续 g-system 的完整 H−P 身份。φ_RW 正型，故 g_R≥0、q_R=c_R=0。不是只验正对角，而是全部混合 Gram 正。
2. 取 Γ=0、W=2cosh(au)du，a>0，对照562/567已给双极点矩零 compact 负 Gram。若修补趋零，则 D′ 正型闭性会使该负核正型，矛盾。更具体，固定负见证 r 使 c_R≥−Q_W(r)/||r||²−O_r(R⁻²)>0。每层“加正谱即可正”因此对正反例都成立，区别全在预算能否消失。
3. 对固定真实椭圆曲线 E/F₅ 与全部 returns，W_FF=L∑_{n∈Z}2cos(nθ)δ_nL 已由真实 U,H／RR 证明正型。其 φ_R 窗化 Fourier 是全部周期谱的非负卷积，修补为0。此处 Γ 是目标自身的 archimedean/contact 数据，不能把经典 Γ 额外塞入函数域。极点亦须保完整周期族；不能只取 fundamental strip 来证明 positivity。
4. 函数域的预算0由独立几何正性／同一对象容量支付；classic 的 (14) 仍缺相应输入。FF 正例只是核对规则，不提供经典 k_R≥0。

## 7. 与576原子正原料的准确关系

(7) 的 q_R 是真正连续谱，不能把它的正求积近似当成逐层严格正性。若 g_R 在某个开区间为负，加入任何有限正 cos 混合，或576有限正 FF 混合，其 Fourier 增量均为纯点正测度；它无法消除 g_R(t)dt 的负绝对连续部分。Lebesgue 分解即给反测；对有限 FF 格点并可在负区间取避开所有原子的子区间。

更一般，任意局部有限纯点正增量仍不能修复负的绝对连续部分。无限逼近的 D′ 极限可能产生连续谱，因而这不否定576闭包定理；它只排除“每层真 Γ ＋负密度 ＋有限原子混合”这一确切加法 recipe。必须采用真实连续修补、改变基底或证明 g_R 本身已非负。

K_R 光滑且无 δ，使本轮绕过576逐层 Radon 模型漏 Γ 的 fixed 窗 Hlog 门；代价是留下独立可计算但尚未证明趋零的连续正谱预算。不能称该预算是旧 FF 整数截面维数或已存在的算术容量。

## 8. 405／537与独立输入准入

本候选首先是 D′ 正分布逼近，不是每层通过经典405源商的几何 map。完整 Γ 保留并不使每层杀405非compact Pan；这里可直接证明失败：每层正谱密度在 |t|≥T_R 严格为正，任何非零 S_exp 源的 Fourier 为非零整函数、实零集测度零，故 Q_tildeV(r_p)>0。对405实际 r_p，553 已给 hat r_p(t)=s(s−1)ξ(s)/2、s=1/2−it；不借 RH 即知它非零 a.e.。其所有 translates 同样失败；Schwartz 修补版本亦然。不能要求每个中间层满足经典关系后又免费把谱限制到未知零集。

在固定 compact 537 非根 r₀ 上，令 τ=Qζ(r₀)>0、supp r₀⊂[−L,L]。因为修补自身正型，Q_K(r₀)≥0，故已无条件得到

\[
 Q_{\widetilde V_R}(r_0)\ge\tau-D_LR^{-2}\|r_0\|_2^2>0
 \quad(R\text{ 足够大}).                              \tag{17a}
\]

这是由实际 signed 窗尾加正修补所得的 raw 非根 lower，不只来自“每层一般正性”，亦不需先证明 c_R／m_R 趋零。数值向 τ 收敛、对应 upper 以及同一目标源商的比较，仍须支付修补预算；(17a) 本身不产生每层405源商 map。noncompact 全 Pan 不由 D′ 自动覆盖，但本具体 recipe 可以另付每个固定强源的尾：对 r,s∈S_exp，

\[
 |B_{V_R^0}(r,s)-B_\zeta(r,s)|
 \le {M_2\over2R^2}\int u^2|(r*s^*)(u)|\,d|M|(u)<\infty.\tag{18}
\]

取任一 N>1/2，用 S_exp 的指数卷积界把右侧控制为 C_N R⁻²p_(N+1,0)(r)p_(N+1,0)(s)；常数中的完整 prime-power 和为 ΣΛ(n)(log n)²n^(−N−1/2)，双极点积分亦收敛。这一步不依赖 RH。加上修补的 c_R||r||₂||s||₂ 或 m_R||r||₁||s||₁ 费用后，在预算消失前件下，全部固定405关系及其固定配对确会趋零；还可对指定 S_exp 有界集统一。但每层仍没有405源商 map，亦不覆盖所有 translates 的同一原 Hlog 统一费用。

本分支新增可消费模块是：固定 Γ／contact 不变的明确连续谱修补规则；(9) 的真实 signed 协同；(10)–(13) 原 du 及 Fourier-L¹ 完整费用；(17) 的原 fixed 窗 uniform transport；以及纯点加法无法修复负 ac 部分的 typed 门。这些都不独立证明 classic 正性。

下一独立输入必须在不先证明 k_R≥0／不读取 ζ 零点的条件下，给出实际 q_R 的消失预算（例如独立主要化 q_R≤ε_R b_R、ε_R→0 且 b_R 的原 norm／谱质量费用可付），或在同一算术对象用截面／RR 容量产生 g_R+修补的具体非负分解并证明其修补预算趋零。只把 c_R／m_R 改名“容量亏损”不改变 (16)。

最强旧 actual 仍542＋555→557 whole leading4/5上预算；本模块不改变成长 core／coupling／Ξ 或宏观独立容量瓶颈。是否准入一轮新数学结算由root比较本轮各分支后的实际净值确定。

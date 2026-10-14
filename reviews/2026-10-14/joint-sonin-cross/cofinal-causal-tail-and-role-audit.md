# Cofinal causal inverse：实际跨半线范数下界与角色边界

2026-10-14；只写本独占短审，不改公共 STATE/Goal/cadence/Git，不另计轮。
已恢复 AGENTS/README/STATE/check/show、当前 Goal/frontier/C023/AD、实际 ratio 门。
现场 HEAD `ac4122a4f494be50143cfce1eb1214d7ea5295a2`；STATE 与 joint-sonin-cross
原稿目录由父线程并发工作，未覆盖。本审只核以下 growing auxiliary inverse，不审 560 的最终消费。

**结论：候选下界成立。** 对每个先固定 ε>0，ALL 实数族
T_L≤(2−ε)e^L，当 L→∞ 时，原物理 H=L²(R,dy) 上严格有

    μ_L{log n>T_L}→1,
    m_L ||1_(T_L,∞) D_L 1_(-∞,0)||_(H→H)→1.          (1)

第二项是实际辅助算子范数的反例，不只是充分 tail upper 的常数失控。
其输入角色不够支付 actual k_R／Weil source／完整 signed error 的下界。

## 1. 全部算术对象、范数与概率归一化

令 L≥1，x_L=e^(2L)，F_L={p prime:p<x_L}，包含全部 base primes，保 strict cutoff。
在共同 unitary log 物理空间 H 中，U_t f(y)=f(y−t)。定义

    B_L=Π_(p∈F_L)(I−q_p U_(a_p)), q_p=p^(−1/2), a_p=logp,
    D_L=B_L^(−1)=Σ_(n F_L-smooth)n^(−1/2)U_(logn),
    m_L=Π_(p∈F_L)(1−q_p)>0.

包括 n=1；smooth n 的唯一分解保证 coefficient 正好 n^(−1/2)，没有额外 word 重数。
每个固定 L 的逆级数在 operator norm 绝对收敛，全部 geometric factors 有限乘积。
μ_L(n)=m_L n^(−1/2) 是该 smooth 整数集上的概率。等价地，取独立几何变量

    P(K_p=k)=(1−q_p)q_p^k, k≥0,
    X_L=Σ_(p∈F_L)a_p K_p=logn.

于是 m_L D_L f=E[U_(X_L)f]，是合法 Hilbert-valued 绝对概率和。
||m_L D_L||≤1。其 Fourier multiplier 在 s=0 等于1且连续，故原 norm 准确为

    ||D_L||=m_L^(−1).                                (2)

这不是 weighted norm 或源 label 概率；概率只表示原 causal inverse 的正系数归一化。

## 2. PNT 量词与显式 uniform 方差

几何矩准确给

    M_L=E X_L=Σ_(p<x_L) a_p q_p/(1−q_p),
    V_L=Var X_L=Σ_(p<x_L) a_p² q_p/(1−q_p)².           (3)

仅用旧经典无条件 PNT／Chebyshev／Abel；不依赖任何未知 ζ 零点位置。
由 θ(x)=Σ_(p≤x)logp~x 与 Abel，

    Σ_(p<x)logp/sqrtp=2sqrtx+o(sqrtx).

余项 q/(1−q)−q=q²/(1−q) 的加权 prime 和为 O(logx)：
它 ≤(1−1/sqrt2)^(−1)Σ_(p<x)logp/p，后者由旧 B_<(x) 账本支付。
因此准确 leading 是

    M_L=2e^L+o(e^L).                                 (4)

PNT 量词为：∀先固定 η>0，∃L_η，∀L≥L_η，|M_L−2e^L|≤ηe^L。
不是有效零点高度界，也没有选随 L 缩小的未付 η(L)。strict/closed 差在 prime 端点
至多 O(logx/sqrtx)，不改变 (4) 或下面的 uniform upper。

由 q_p≤1/sqrt2、a_p≤2L 以及旧 ψ_≤(x)≤4log2·x，Abel 给

    Σ_(p<x_L)logp/sqrtp≤8log2·e^L,
    V_L≤C_V L e^L, C_V=16log2/(1−1/sqrt2)².           (5)

(5) 对 ALL L≥1 是显式 upper，不使用 PNT 的不明误差率。
独立几何变量的方差相加已包含所有 smooth primepower combinations；未删除 proper powers。

## 3. 归一绝对 tail 的必要 lower

固定 ε>0。由 (4)，最终 M_L−T_L≥(ε/2)e^L。Chebyshev 与 (5) 因而给

    μ_L(X_L≤T_L)≤4 C_V ε^(−2)L e^(−L),
    m_L Σ_(logn>T_L)n^(−1/2)
       =μ_L(X_L>T_L)≥1−4 C_V ε^(−2)L e^(−L).          (6)

若 T_L<0，左侧 tail 本来就是1；同一 lower 仍合法。
量词在最终 ALL L、ALL T≤(2−ε)e^L 一致。与 (6) 相比，先前
A_(F,γ)e^(−γT) 只是充分 upper；本节直接核正系数质量自身的实际 lower。
但 scalar 绝对质量仍不能自动变为 Hilbert block norm；下一节单独支付这一步。

## 4. 原 H 上实际跨半线 norm 的测试向量

固定 φ∈Cc∞(−1,1)，||φ||₂=1。令

    h_L=εe^L/8,
    f_L(y)=h_L^(−1/2)φ((y+2h_L)/h_L).

这是原物理 smooth norm1 向量，supp f_L⊂(−3h_L,−h_L)，
||f_L′||₂=||φ′||₂/h_L。不是全域 constant 或 plane wave。
任何 H¹ 向量都满足 translation Lipschitz 上界

    ||U_x f−U_z f||₂≤|x−z| ||f′||₂.

由概率和、Cauchy–Schwarz 与 (5)，

    ||m_L D_L f_L−U_(M_L) f_L||₂
       ≤||f_L′||₂ E|X_L−M_L|
       ≤||φ′||₂ sqrt(V_L)/h_L
       ≤C_(ε,φ)sqrtL e^(−L/2),
    C_(ε,φ)=8 sqrt(C_V)||φ′||₂/ε.                    (7)

当 L 最终足够大，M_L−T_L≥εe^L/2=4h_L。
故 supp U_(M_L)f_L⊂(M_L−3h_L,M_L−h_L) 严格落在 (T_L,∞)，且范数仍1。
写 P_-=1_(-∞,0)、H_T=1_(T,∞)。P_-f_L=f_L，而 H_T U_(M_L)f_L=U_(M_L)f_L。
所以原 H 的准确 block norm 有

    1−C_(ε,φ)sqrtL e^(−L/2)
      ≤m_L||H_(T_L)D_L P_-||≤m_L||D_L||=1.           (8)

式 (8) 支付 (1)，也给 ||H_(T_L)D_L P_-||/||D_L||→1。
这无需 rough operator upper 饱和假设；(7) 的实际输入直接达到 asymptotic lower。

因此若某 cofinal 全物理 Hilbert norm 的 decoupling 需要
m_L||H_(T_L)D_LP_-||→0，则必须有 liminf T_L/e^L≥2。
作为边界核对，若 T_L≥(2+ε)e^L，Chebyshev 另给 normalized 正系数 tail O_ε(L e^−L)，
且 block norm ≤该 tail，故趋0。T_L/e^L→2 的过渡不由本稿判定。

## 5. actual Γ、映射角色与不能运输的 lower

若按 actual carrier 选择 T_L=Γ(R_L)=2θ′(R_L)，本 lower 在
Γ(R_L)≤(2−ε)e^L 时仍成立。Γ(R)=log(|R|/(2π))+O(R^−2) 是原对象；
本稿没有把 Γ window 当 freely paid parameter，也没有删除 Γ 的源费用。
它只是说明此半线 block 在相应全物理 norm 下不能用 small causal tail 解耦。

以下角色差别是消费范围的必要前件：

- f_L 是 D_L 作用域 H 的负半线输入。实际 arch Sonin M=RanP⊂positive 物理半线，
  因此 f_L 不属于 M，也不是裸求值 k_R。
- 真实有限窗 residual 中，D_L 的低输入形如 P_-D_L*P_T w_R 或相关受限像。
  未证本 f_L 位于这些像；不能把全 H operator norm lower 送到该 particular 配对。
- f_L 的 physical log 宽度约 e^L；原 Weil source g/r 的支撑 I_L 宽度仅2L，
  且 source g→A_g 与 physical f 是不同角色。没有 dual pole、allpp 或 norm transport
  的附加审计把此向量送到完整 Weil 测试源。

因此 (8) 不证明 actual ρ_(F_L) 的 error 大、不证明 joint compact 型非紧/符号错误，
不证明 Q_W 负、core 无界或任何 ζ 谱位置。粗 inverse norm m_L^−1 很大也不补这些箭头。
新信息仅为这个明确的原 H 辅助半线 norm：其 normalized lower 实际接近1，
不允许再把充分 upper 失败作为全部证据，也不允许把该 lower 扩到受限源。

保留的合法逃逸包括：source-adapted 有效输入／受限像更小、signed whole cancellation、
另付 Γ 并增加真实 carrier window、不同 factorization/parametrix、直接 actual projection
或 joint error 估计，以及不同 core/norm 的已付运输。本稿不排这些方法类。
最强旧 whole 对照仍为542+555→557 leading4/5；本稿没有较强 whole 或 Ξ 净后果，
不能通过宏观 Goal 完成门。PNT 是已有输入，不宣称新外部定理。

下一仅由 root 将 (8) 作为 cofinal 全 Hilbert norm 门消费并保角色边界；
actual k/source 的 signed 共同费用须另给输入。无后台计算／下载 pending。

## 6. 必要依赖

原 B/D 与两边界消费对象取自
`reviews/2026-10-14/joint-sonin-cross/general-finite-set-model-and-growth-fees.md` §§1–4；
该原稿明确其 cofinal 常数仅 sufficient upper，本稿追加 actual norm lower 而不修改旧文。
经典无条件 PNT／Chebyshev／Abel 的当前 paid范围见
`notes/555-actual-prime-weighted-schur-and-growing-weil-inertia.md` §3；
原物理 unitary norm、Sonin cutoff1及 Γ 与 k 的角色见531/532及 joint root 消费收据。
所有新数学均由 (3)–(8) 本稿推导；此为独立出稿，不代 root premise closure／结算。

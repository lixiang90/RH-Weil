# Th6.5 的量化收缩窗与三段协方差预算：独立证明稿

2026-10-29；同一 G20261027/runtime createdAt 1793085111；冻结基线 0c4f3a3eb609bb1d9564138fa4a35701f05605f2。本文是 localization/rate 分工输出，尚未 root consumption；不改 STATE、cadence、Goal、Git，不预领轮号或新合同。

结论：既有 C052 的 uniform entire evaluation 与原 Lemma 6.1 的实际误差证明，足以自含推出 Th6.5 所需的 shrinking-window (6.20)，包括 δ=(log p)^(-2/5) 和省略最后一个素数 p。若独立域稿支付实际 Sonin 正交投影的 Toeplitz commutator、严格 trace/HS 分解及 G 逆界，则三段预算给 C_p=O_h((log p)^(9/10))。本文没有发现这两个量化步骤需要未读的 6.4 sharp 或 §7；没有把它们当作已支付依赖。下文完整写出量化证明，并把域稿消费条件列开。

## 1. 输入、对象与消费边界

固定原件为 bramble_trace, *Sharp Schatten asymptotics and Sonin trace localization for semilocal Fourier cutoffs*, rStation riemann_hypothesis_2 v2，16 Oct 2026 01:00 UTC：`literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md`，61862 bytes，SHA256 `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`。原件为待审数学材料，平台标签及作者声明不支付结论。

实际读取范围：原 §1 lines21–57 的物理/Fourier 约定；必要 §6.1 lines477–563 的素数和及其误差证明；旧 C052 所用 lines667–720、817–869 的 uniform evaluation、Gram 核和插值；lines601–633 的 J_X 定义；Th6.5 statement/proof lines959–1100。恢复时读取 goals/README、STATE，执行 research_state.py check 后 show，并读取同 Goal、D20261029X、macro summary 和 `reviews/2026-10-29/core-input-portfolio/next-critical-prime-covariance-proof-gate.md`。原 6.4 sharp、§7、后文、新论文均非本文输入。

记 L=log X、A=sqrt(X)/L，最终 X=p，r=p^(-1/2)。F 可以是 {q:q≤X}，或最终的 {q:q<p}。原物理源 h∈C_c^∞(R) 首先固定，可复值；其 Fourier 变换 H(t)=∫h(y)e^(-ity)dy，w(t)=|H(t)|² 为非负 Schwartz 函数。所有 O_h 常数可依赖此固定 h 的有限个 Schwartz 半范数、固定 cutoff；不依赖 p。没有令 h 随 p 变化。

原始 arch Mellin 函数以下记 v，避免与物理 h 混淆。其加权范数是 ||v||_F²=∫|D_F(t)v(t)|²dt/(2π)，其中 D_F(t)=∏_{q∈F}(1-q^(-1/2-it))。既有 C052 的确切已付输入是：

1. 对所有有限 F，同一个常数 C 满足

   sup_(|z|≤R)|v(z)| ≤ exp(C R log(R+2)) ||v||_F，R≥2。             (U)

2. 实际 Sonin 正交投影的 diagonal kernel，相对于 dt/(2π)，满足

   k_F(t,t)=|D_F(t)|² Q_F(t)，Q_F(z)=sup_(||v||_F≤1)|v(z)|²。       (K)

(U) 不是删除 Gram 逆的结果。其已付依赖链为固定-gap Burnol entire/kernel estimate → reflected Hardy evaluation（Im z≥1 上 |D_F^+(z)|≥ζ(3/2)^(-1)）→ arch conjugation 保持同一 weighted norm → 上下边界与 strip barrier。最后先对固定 F、ε 令矩形宽度趋于无穷，再令 ε↓0，消除 F-dependent prefactor。它覆盖所有有限 F，并非固定 X 的 inverse-angle 界。本文以这条已消费输入为起点；不重新宣称证明 Burnol 结构定理。范围相等 S_F H=D_F S_0 H 本身不是等距，本文从未如此使用。

本文独立证明从 (U)、(K) 与原6.1已付误差到 shrinking-window localization 的推导。最后协方差消费另需独立域稿支付第6节的 (D1)–(D4)，不能由本稿局部预算自动推出实际投影域正确。

## 2. 原6.1误差可量化为 O(A/L)

对每个固定 B>0，原证明可给出绝对一致估计

   ∑_(q≤X) q^(-1/2-it) = 2A e^(-itL)/(1-2it) + O_B(A/L)， |t|≤X^B。 (P)

这里不是把原 statement 的 o(A) 无证升级。其 proof 已对 Ψ_t(y)=∑_(n≤y)Λ(n)n^(-it) 使用高度 y^(B+2) 的 Perron 与 VK zero-free rectangle，误差为

   O_B(y exp(-c_B (log y)^(1/3)/(log log y)^(1/3)))。

去除高素数幂的 O(sqrt(y) log²y) 及分割点 sqrt(X) 以下的 O(X^(1/4) polylog X)，在目标尺度均为 o(A/L)。对上段用固定指数 2B 覆盖所有 y；偏和分部积分的权是 y^(-1/2)/log y，twist 已置于 Ψ_t，故误差积分不额外乘 |t|。剩余主积分 ∫_2^X y^(-1/2-it)/log y dy，用 v=log y 分割 [L/2,L]，一次分部积分给端点项 2A e^(-itL)/(1-2it)；余项 O(A/L)，因为 |1/2-it|^(-1)≤2 一致。低端贡献同为 o(A/L)。VK 衰减快于任意固定 log 幂。这正是原证明已有估计的定量结算，没有添加新零点分布假设。

Euler logarithm 的二阶及以上项满足

   log|D_F(t)|² = -2 Re∑_(q∈F)q^(-1/2-it) + O(log L)，             (E)

对所有实 t 一致。理由是每个 q 的 log(1-z)+z 由 C|z|² 控制，且 |z|≤1/sqrt(2)；再用 ∑_(q≤X)1/q=O(log log X)。O(log L)=o(A/L)。故由(P)，对全素数集

   log|D_≤X(t)|² ≤ 4A/(sqrt(1+4t²)) + C_B A/L， |t|≤X^B。         (E+)

原件的实际区间是

   J_X=[π/L-L^(-2), π/L+L^(-2)]，m=|J_X|=2L^(-2)。

在 J_X 上 t=O(1/L)、tL=π+O(1/L)，从而

   Re(e^(-itL)/(1-2it)) = -1+O(L^(-2))。

代入(P)、(E)得

   inf_(J_X) log|D_≤X|² ≥ 4A-C A/L。                             (J)

这里 O(A/L) 已覆盖 Euler 高次项与相位/振幅 O(A/L²)。若 ||v||_≤X≤1，则

   ||v||_(L²(J_X,dt)) ≤ sqrt(2π) exp(-2A+C A/L)。                 (Jv)

右端中的 2π 源于范数约定；以后仅并入固定常数。

## 3. Shrinking-set 插值的显式常数

对 E⊂[-1,1]、|E|=m>0、复多项式 P（次数≤n），及 T≥1，存在绝对 C，使

   sup_(|z|≤T)|P(z)| ≤ C m^(-1/2) [C(T+1)/m]^n ||P||_(L²(E))。   (I)

证明：Chebyshev inequality 给 E 的子集 E'，测度 m'≥m/2，且其上 |P|≤sqrt(2/m)||P||₂。按 E' 的累积测度选 n+1 个等分 quantile 节点 x_j（可取闭包上的极限点），使 |x_j-x_k|≥m'|j-k|/(n+1)。连续性保留同一节点值界。Lagrange 分母满足

   ∏_(k≠j)|x_j-x_k| ≥ [m/(2(n+1))]^n j!(n-j)!。

分子对 |z|≤T 至多 (T+1)^n。求和用 ∑_j 1/(j!(n-j)!)=2^n/n!，以及 n!≥(n/e)^n，便给(I)；n=0 直接成立。因而没有隐含未知 C_m，也没有残留 n log n 代价。该证明允许 m 随 X 缩小，允许复系数及复目标 z。

设 λ=log A，取原6.5参数

   R=A/λ³，n=ceil(3A/λ)，T=L^b，b>0 首先固定。

当 X 足够大，T/R→0。对 ||v||_F≤1，以原点 Taylor polynomial P_n 逼近。由(U)与 Cauchy estimate，

   ε_X:=sup_(|z|≤T)|v(z)-P_n(z)|
       ≤ exp(C R log(R+2)) (T/R)^(n+1)/(1-T/R)。

由于 λ=L/2-log L，

   C R log(R+2)=O(A/λ²)，
   (n+1)log(T/R)=-3A+O_b(A log L/L)，

故

   ε_X ≤ exp(-3A+C_b A log L/L)。                               (Tay)

对 E=J_X 应用(I)，m=2L^(-2)。插值因子 M 满足

   log M ≤ O(log L)+n log(C(T+1)/m)=O_b(A log L/L)。

又 ||P_n||_(L²(J_X))≤||v||_(L²(J_X))+sqrt(m) ε_X，故由(Jv)、(Tay)

   sup_(|z|≤L^b)|v(z)|
     ≤ M sqrt(2π)exp(-2A+C A/L)+(1+M sqrt(m)) ε_X
     ≤ exp(-2A+C_b A log L/L)。

取 weighted unit ball 上确界并平方，得到

   log Q_≤X(t) ≤ -4A+C_b A log L/L， |t|≤L^b。                  (Q)

若 Q=0，将 log Q 解释为 -∞。没有使用 common-zero-free 下界、receiver 强极限或原(6.9)的 lower bound。

## 4. 真正 cofinal 的 δ=L^(-2/5) 以及 omit p

将(K)、(Q)、(E+)相乘；固定 b 后 L^b≤X^B 在充分大 X 成立，故

   log k_≤X(t,t)
     ≤ -4A[1-(1+4t²)^(-1/2)] + C_b A log L/L。                  (KL)

对 0<δ≤1/2，有 1-(1+4δ²)^(-1/2)≥cδ²。令 δ=L^(-2/5)，则

   (log L/L)/δ² = (log L)L^(-1/5) → 0。

所以存在 c>0 及 X_0(b)，对所有 X≥X_0(b)

   sup_(δ≤|t|≤L^b) k_≤X(t,t) ≤ exp(-c A δ²)。                  (Loc)

这条结论是同一个 cofinal 上界；没有先固定 δ 再无依据地交换 δ↓0、X→∞。实际上上述证明对任一首先固定的 a∈(0,1/2)、δ=L^(-a) 同样成立，但本文只消费指定的 a=2/5，不做指数优化。

现在 X=p，省略最后素数：对所有实 t

   |log|D_≤p(t)|²-log|D_<p(t)|²|
     = |log|1-p^(-1/2-it)|²| ≤ C p^(-1/2)。

而 p^(-1/2)=o(A/L)。故(J)、(E+)对 D_<p 仍成立，仅改固定常数。(U) 本已对每个有限 F 一致；使用 ||v||_<p≤1 重新运行第3节，得到对应 Q_<p 的(Q)，再用实际(K)便得

   sup_(L^(-2/5)≤|t|≤L^b) k_<p(t,t) ≤ exp(-c A L^(-4/5))。      (Loc<)

没有由权重逐点比较直接猜测 inverse Gram 的同向关系，也没有用 weighted isometry 或 fixed-X inverse angle 替代 uniform evaluation。c、阈值可依赖固定 b；对所有充分大 prime p 一致。

## 5. 三段 commutator 量化

令 χ 为固定偶 C_c^∞ cutoff，在 |s|≤1 为1、|s|≥2 为0，且在非负半轴单调不增。谱上 B(t)=2+2cos(Lt)，0≤B≤4。取

   d=δ=L^(-2/5)，T=L，
   u_0=w χ(t/d)，
   u_1=w[χ(t/T)-χ(t/d)]，
   u_2=w[1-χ(t/T)]。

三者非负，w=u_0+u_1+u_2。

本节使用域稿需支付的 uniform Toeplitz 结论：对任意 Cayley 尺度 a>0，b_a(t)=(t-ia)/(t+ia)，以及相应 circle multiplier v，

   ||[S,M_(v∘b_a)]||_S1 ≤ 2 ∑_(n∈Z)|n||vhat(n)|，              (C1)
   ∑ |n||vhat(n)| ≤ C(||v||₂+||v||₂^(1/4)||v''||₂^(3/4))。       (C2)

这里 S 是实际 S_<p，在全 boundary L² 经过相同 unitary Cayley map 的正交投影；不能只在 Hardy 内部压缩或换成仅关系相等的模型。为透明起见，(C2) 的指数来自 Fourier split：对整数 N≥1，低频用 Cauchy 给 C N^(3/2)||v||₂，高频给 C N^(-1/2)||v''||₂；优化 N 并处理 N=1 即得。该数值常数与 F、a 无关。

### 中央段

对 a=d 做 Cayley。u_0B 支持 |t|≤2d，其 circle 支集一致远离 Cayley 无穷点。此处 ∂θt、∂θ²t 均 O(d)。w 的前两阶导数固定有界；χ(t/d) 的 θ 导数一致有界；B 的 t 导数分别 O(L)、O(L²)。当 d≤1，所得 circle multiplier v_0 满足

   ||v_0||₂≤C_h，||v_0''||₂≤C_h(1+Ld)²。

于是由(C1)、(C2)

   ||[S,u_0B]||_S1 ≤ C_h(1+Ld)^(3/2)=O_h(L^(9/10))。            (Cent)

complex h 仅通过非负实函数 |H|² 出现；无 h 的偶性假设。

### 中段

u_1 的支持位于 d≤|t|≤2T，不是只到 T。故在(Loc<)取固定 b=2：2L≤L² 对大 p 成立。若域稿支付严格 diagonal trace 身份，则

   Tr(u_1 S)=∫u_1(t)k_<p(t,t) dt/(2π)
            ≤ C_h L exp(-c A L^(-4/5))。                       (Mid)

这里只用 ||w||∞ 和支持长度；无需 entire h，更没有物理源随 p 改变。

### 尾段

对 a=1 做 Cayley，令 a_T(t)=u_2(t)B(t)。有 |∂θt|≤C(1+t²)、|∂θ²t|≤C(1+|t|)³，且 dθ≤Cdt。对 j≤2 及任意固定 M，Schwartz 性与 cutoff 的导数给

   |a_T^(j)(t)|≤C_(h,M)(1+L)²(1+|t|)^(-M)， |t|≥T，T≥1。

因而相应 v_2 满足

   ||v_2||_H²(circle)
      ≤ C∑_(j≤2)||(1+|t|)^4 a_T^(j)(t)||_(L²(dt))
      ≤ C_(h,N)(1+L)² T^(-N)，任意首先固定 N。

最后一步先选 M>N+5；circle 无穷点光滑延拓为零由 Schwartz 性保证。再用 Fourier Cauchy，∑|n||vhat_2(n)|≤C||v_2||_H²，从(C1)得

   ||[S,u_2B]||_S1≤C_(h,N)(1+L)²T^(-N)。                      (Tail)

消费固定 N=4、T=L，仅需 O_h(L^(-2))。未搜索参数、未改目标指数。

## 6. 域稿的准确消费条件与协方差结算

令 S=S_<p，G=(1+r)²I-rSBS 在 S H 上。本文最终协方差推导需要独立域稿实际证明：

- (D1) actual Sonin S 经 unitary Cayley transport 是全 boundary L² 上相应 Toeplitz kernel 的正交投影；因此(C1)适用且常数对所有有限 prime sets、所有所用 Cayley 尺度统一。仅有 range identity、quotient relation 或 Hardy 内部形式不够。
- (D2) (K) 的 kernel measure 为 dt/(2π)，对非负 u_1 的实际 trace 有 Tr(u_1S)=∫u_1k dt/(2π)，并可由(Mid)支付其有限性。
- (D3) G≥(1-r)²I，故 ||G^(-1)||≤(1-r)^(-2)；strict trace domains 允许下列式子及有界因子的 cyclicity/ideal estimates。
- (D4) 对 a=u_jB，commutator trace estimate 成立：

      |Tr(S a(I-S)BSG^(-1))|
          ≤4(1-r)^(-2)||[S,a]||_S1；                           (Tr1)

  对非负 u 且 Tr(uS)<∞，由实际 HS factorization（u 与 B 均为谱乘子）成立

      ||S u B(I-S)B S||_S1 ≤32 Tr(uS)。                       (Tr2)

本稿不以“原件写出(6.25)/(6.26)”代替(D1)–(D4)。它们由独立域稿另行证明、由 root 逐项消费。本文也不以原(6.19)里 q 的符号自动支付 q-to-K；旧560物理字典、actual Gram update 与 actual ΔT 是独立消费事项。

在(D1)–(D4)成立时，将 w 三段分解代入

   C_p=Tr(S wB(I-S)BSG^(-1))。

中央段、尾段用(Tr1)和(Cent)/(Tail)；中段用(Tr2)、(Mid)再乘 ||G^(-1)||。r≤1/sqrt(2)，故这些 G 逆因子有同一绝对上界。得到

   |C_p| ≤ C_h[L^(9/10)+L exp(-c A L^(-4/5))+L^(-2)]
          =O_h(L^(9/10))。

因为 A=sqrt(p)/log p，第二项超越任意固定 log 幂地衰减。证明的所有极限均是固定 h、固定 χ、固定 b=2、固定 N=4 后 p→∞；没有依赖 p 的 hidden norm constant。C_p 未被假设为正；这里证明其绝对值界，足以供后续 exact trace update 消费。

## 7. 已付、未付与强度限制

本稿自含闭合的新局部链：原6.1误差 O(A/L) → 真实 J_X 的 weighted smallness → 带显式 m 常数的 quantile interpolation → uniform Taylor remainder → δ=L^(-2/5) 的 cofinal localization，包括 omit p → 在所列实际域/trace 前提下的 L^(9/10) 三段协方差预算。既有 C052 的(U)/(K)保留原 weighted norm、Gram 与物理/原始函数角色；未用6.4 sharp、§7、commonzero下界。

尚需 root 消费独立域稿及 fresh audit，并扣除最强旧结论，才可认定 actual C_p、actual ΔT 与旧560 ΔK 的净后果。本文不宣称 whole-object Weil 正性、full Q 符号、core coupling、全域 GRH/RH 或长期 Goal 完成；也不自行决定这是几轮或固定为零轮。文稿发出仅为 draft completion，不是 root-consumed 数学结果。

本分工发现的实际量化障碍已经去除：固定 δ 的旧 localization 可以付清所需 shrinking δ；中段 2L 端点由 fixed b=2 覆盖。整体研究瓶颈是否改变，取决于 root 对 actual covariance/Gram update/旧560字典及最强旧基线的合并消费；本文不提前领取。

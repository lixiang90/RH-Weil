# Sonin、成长范围与下一来源门：路线图修订审计

2026-10-20。为本轮用户要求的路线图回顾提供独占审计；不执行下一数学门，不建合同，
不修改公共 STATE/cadence/Git，不计新数学迭代。固定 G20261014／0c4f≤538 基线。
下述数学结论按已消费原稿与收据复核范围，并非本稿重证外部定理或另行推导新界。

## 1. 相对旧路线图，actual signed 分支发生了什么

旧[设施路线图](../../../goals/reviews/2026-10-20-generalized-weil-facilities-literature-roadmap.md)
把 560 的同源正迹减紧误差作为并行备选。570–572 已使这条支路更具体，
但没有从“正迹＋误差身份”跨到“独立完整正性”。现在应把它列为**有明确已付局部资产、
只允许一次 actual transport 来源检查的受限支路**，不再列成宽泛待开发的 signed 计划。

| 结算 | 新支付的对象与范围 | 决策信息与未付责任 |
|---|---|---|
| [570](../../../notes/570-actual-joint-sonin-signed-mixed-and-narrow-source-cost.md) | 真正固定 $S=\{\infty,2,3\}$ Sonin 全 Gram 逆及全部 returns；双矩零窄源 $E_{23}(g_\eta^\pm)=\pm C_{23}\log^2(1/\eta)+O(\log(1/\eta))$，同一固定源窗无限两号指数 | 无费共同取号及有限秩／有限余维补丁失败；非有限秩紧修复、Γ-relative、源适应和不同全逆仍合法。原 L²、Dlog 归一后该误差趋零，完整 Q 两族都正；不是 Q 的反例 |
| [571](../../../notes/571-actual-receiver-two-boundary-signed-comparison-and-growth.md) | 模型全 inverse 的真实 receiver pair 与双边界 Gram 差；严格 $T=\Gamma(R)$ 的固定单 prime actual carrier 两号；$\theta>1$ 同步高度区间的 $m_F^2$ 归一 receiver 均值 | 旧全空间 norm witness 不能代真实 receiver 费用。模型差不等 actual ε；均值不等 receiver 方向放大率，也不等原范数或原源费用 |
| [572](../../../notes/572-finite-euler-receiver-coherent-tail-and-original-weighted-cost.md) | 实际 $\bar b_F$ 乘 receiver 后按最终 delay 合并；半线原域、完整 diagonal $O(L^4)$、全部 coherent 尾与 finite-height／完整 Γ 端点费；$\theta>2e$ 得 actual $\lvert b_F\rvert^2$ 原 dy 平均 $O_\theta(L^4)$ | 571 的一项模型原加权费用缺口真正改变。未加权 receiver、actual Sonin／source 运输、其余 $S_T$ 主项尾、平方缺陷与危险 core 未付；不优化阈值或幂次续轮 |

570 的 dense nonexact 控制使用已知 BMS／Matveev 的固定有限 log 算术实例，
不由一般 g-integer 对偶自动获得。572 的普通 log 间距、unique factorization、
PNT／Mertens 与 partition 增长也都是明确额外输入；一般 g 或 continuous 系统须另有自己的替代设施。
把这些前件逐项写成分析证书是可行推广方向，但它们目前只支付所证模型费用，并非完整 Weil 正性。

## 2. 本支路必须固定的对象、域与角色

在酉 log 物理坐标中 $\mathcal H=L^2(\mathbb R,dy)$，

\[
B_F=\prod_{p\in F}(1-p^{-1/2}U_{\log p}),\quad D_F=B_F^{-1},
\quad W_F=B_F^*B_F.
\]

这里 $B_F$ 有界可逆、normal、因果，非酉；$D_F$ 是完整因果逆。
令 $P_M$ 为真实实位 Sonin 空间 $M$ 的投影，$P_T=1_{(0,T)}$。

| 符号 | 真正角色／域 | 禁止的消费替换 |
|---|---|---|
| $k_R\in M$ | 裸 Mellin 求值向量 | 不能当 Γ-completed evaluator 或原 Weil 源 |
| $w_R=e^{iRy}1_{(0,T)}/\sqrt{2\pi}$ | $P_T\mathcal H$ 的 carrier，$T=\Gamma(R)$ | $P_T$ 不是 Sonin 投影；载波范数 $T/(2\pi)$ 不是原源范数 |
| $G_M=P_MW_FP_M\vert_M$ | actual Sonin 压缩 Gram | 不能当 window Gram $G_T=P_TW_FP_T\vert_{P_T\mathcal H}$ |
| $v=L_-D_F^*P_Tw_R,\ u=H_+D_FP_Tw_R$ | 原 dy 半线 receiver pair | 不能代任意低半线输入；全空间 operator 下界不证明它们承受相同费用 |
| $z_T=S_Tw_R\in P_T\mathcal H,\ y=P_Mz_T\in M$ | 下一待审 actual 变分候选 | $S_T$ 是双边界 parametrix，不是完整 inverse；候选尚无已付成长误差 |
| $r\in L^2((-L,L),du)\cap D_{\log}$ | 原 complex Weil 源，zero-extension 的 log Fourier 型域 | 物理向量 $y,v,w,k$ 的 dy 费用须经真实 map 运输后才可消费为源费用 |

需要与旧关系／非根测试衔接时，旧坐标 $f$ 和物理 log 源 $r=e^{u/2}f$ 也不能省略。
dy 与 du 可以是同型 Lebesgue 空间，但向量角色、映射范围和型域不同；改变量名不支付运输。

真实 actual 密度及完整源保持

\[
2\pi\rho_F=\Gamma-2\sum_{p\in F,k\ge1}(\log p)p^{-k/2}\cos(kR\log p)+\epsilon_F,
\]
\[
Q_W(r)=t_F(r)-\langle r,K_{F,I}r\rangle
+2|\langle r,\cosh(u/2)\rangle|^2-2|\langle r,\sinh(u/2)\rangle|^2.
\]

$\epsilon_F\in C_0$ 及固定源窗的原 L² 紧 $K_{F,I}$ 已由 560 付清；
这不表示 $K_{F_L,I_L}$ 成长小、有利号或有限秩。
570 的 $E_{23}$ 是 actual ε 的源二次型；仅对该篇最终 pp／pole 精确零的特殊源才等于 $T_{23}-Q_W$。
572 未设置这种额外源矩条件。完整 Γ/contact、全部 prime powers 与双 pole 均不能删。
有限 Euler 分子的 Möbius 系数不是 $-\zeta'/\zeta$ 素数幂分布的替代品。

## 3. 模型差和双边界相位应怎样保留

571 的 exact 窗口差是

\[
\delta_{\rm win}=\|v\|^2+\|u\|^2-
\left\langle(v,u),J^{-1}(v,u)\right\rangle,
\quad J=\begin{pmatrix}I&K\\K^*&I\end{pmatrix},\ K=L_-B_FD_F^*H_+.
\]

完整 inverse、两侧 self-returns 与 cross 都在。完成平方给
$\delta_{\rm win}\le\min(\|v\|^2,\|u\|^2)$，正向 upper 无坏 gap 分母，
并不表示负部、绝对值或所有 inverse 费用都免 gap。
固定 single-prime 的两号是严格 Γ 锁定 carrier 上的模型两号，不是 ε 的新符号定理。

572 左右分别 clean 为 $V=\bar b v$、$U=b u$ 时，必须将

\[
J\longmapsto J_b=C_b^*JC_b,
\quad C_b=\operatorname{diag}(I,\bar b/b),
\quad K_b=(\bar b/b)K.
\]

单独改 receiver 相位却沿用原 K 会改 cross 配对。保上述协同后，572 仅推出
$\operatorname{av}|b|^2(\delta_{\rm win})_+=O_\theta(L^4)$。
“正 J”“正投影 trace”“有界逆”各有真实内容，均不自动把该 signed 差变成正容量。

## 4. 高度量词和最强旧后果

571：$F_L=\{p<e^{2L}\}$，固定 $\theta>1$，

\[
R_0=\exp(\theta e^L),\ I_L=[R_0,R_0+R_0^\beta],\quad T_R=\Gamma(R),
\]

在相应 $\beta$ 范围有 $\operatorname{av}m_F^2\|v\|^2/\|w\|^2\to0$。
它是 normalized receiver 能量，不是原 receiver 小费，除 $m_F^2$ 会重新引入 condition number。
572 在更受限的固定 $\theta>2e$、$2e/\theta<\beta<1$ 范围真正得到

\[
\operatorname{av}_{I_L}|b_F(R)|^2\|v\|_{dy}^2=O_\theta(L^4),
\quad \operatorname{av}_{I_L}|b_F(R)|^2\|v\|^2/\|w\|^2=O_\theta(L^4e^{-L}).
\]

这是 actual b 权原 dy 费，不是 m² 归一；免费除 b 又可能引入 $m_F^{-2}$。
平均不是逐 R／所有高度／所有源，也不证明 receiver 方向跨窗放大率小。
$\theta>2e$ 是该 l¹-tail／MV 证书的充分范围，不是 actual tail 的必要阈值或整个方法边界。

最强旧短链仍为 [542](../../../notes/542-actual-prime-high-moments-and-strong-baseline-audit.md)
ALL k／ALL band 高矩＋[555](../../../notes/555-actual-prime-weighted-schur-and-growing-weil-inertia.md)
原 ALL-source $A_L\le\beta_L I,\ \beta_L\sim e^L$，经
[557](../../../notes/557-joint-row-norm-and-gamma-arithmetic-moment-budget.md) 的 mixed 下界及 concentration／Bessel 运输，
给 ALL L、ALL complex 原 Dlog 源的 issued whole 负惯性上预算
$\log B_{\rm mix}(L)/e^L\to4/5$。这是安全上预算，非 actual 负惯性 lower 或比例。
557 已归最强旧直接后果，不重计本轮新输入。

$\Gamma(R)\sim\theta e^L$ 且 $\theta>1$ 已处在 555 的有利高频大小层；
572 的 $\theta>2e$ 更未覆盖 $\theta\le1$ 危险核心。不能把当前平均再与旧分解拼成“core 已缩小”。
core／补空间 coupling、通常 Ξ 识别、独立 global 容量以及 whole 4/5 均未改变。

## 5. 唯一下一门为何值得一次便宜审查

应维持 [572 结算](../../../goals/reviews/2026-10-20-euler-receiver-572-settlement.md)
限定的来源门，不将本次路线图回顾当已执行该门。
原[560 carrier-error 稿](../../2026-10-14/joint-sonin-cross/full-inverse-carrier-error.md) §§3–5
给 ALL 有限区间 $J$ 的实位 clipping，常数独立区间位置、长度和 finite F；
有限 translation／clipping words 可用绝对系数质量支付。
但完整 inverse 桥同时有 word 费 $\Omega_F^N$ 和谱尾 $\rho_F^N$；
fixed F 的 $o(1)$ 不能换成 cofinal F_L。旧 word／谱尾 certificate 失效也不是 actual 误差 lower。

下一候选 $z_T=S_Tw_R$、$y=P_Mz_T$ 的优点是对象完全指定、进入真实 M，
且 $S_T$ 已有完整 D／D* 的 interval 展开。它比再调 θ／c／β 或宣称未知 det metric 正
更容易被一次原件检查判真伪。它的价值尚是**信息差**，不是已证明的新费用。

来源门须回答四个可验问题：

1. 真实完整 $S_Tw_R$ 的展开是否在所需原域收敛，clipping 所需绝对系数总价是什么？
   必须核 full bulk 和两单边界，不能只消费 receiver 一项。
2. 从 $z_T$ 到 $P_Mz_T$、从 k 到 w 的误差在 $F_L,T_R$ 同步尺度下到底有多大？
   不能把旧 ALL-J lemma 的直接推论计成新的独立 source 费用。
3. 保 actual $G_M^{-1}$ 的正 Gram 变分身份，并保留 window 完整平方缺陷
   \[
   D_{\rm var}(R)=\|G_T^{-1/2}(G_TS_T-I)w_R\|^2.
   \]
   这是结算已指定的未付量；本审计未执行或证明它的新估计。
   572 的 receiver norm 或 δ 正部不支付这个非负平方。
4. 扣最强旧后，是否至少产生一项原 source／cofinal 费用的净改进，或严格削弱一项可用前件？
   只把“需支付 D_var”改写成“需一个 gap／容量定理”没有净信息。

**准入数学合同的证据**只能是具体的原域及可闭费用／可否定比较，带原 norm、全部误差、
实际系数方向、source/growth 量词与至少一个净后果；不能凭候选合法就晋级。
**必须停的结果**是：只得旧 interval clipping 的直接 corollary，加一个 unknown D_var 或 growing gap。
那就记录该入口停止，不建 C036，不重跑模型参数，不把它放进下一张来源队列。

## 6. 若该门停止，两个现实备选怎样重新准入

两个备选当前都不是已启动合同，也没有从 572 自动得到所缺新输入。

**备选 A：actual source 层的 Γ-relative／非有限秩 signed 修复。**
输入是 560 的真实 $Q=t-K+\text{双pole}$ 原域身份及 570 已知的不定性。
必须新增同一 actual 压缩对象上的联合身份、有效局部化或比旧 word 组织更强的 source-adapted clipping，
使其直接比较 ε／K 与完整 Γ、正迹和 pole；仅估模型 δ 不够。
最便宜负对照是 570 的两号窄源及旧 Γ 主费用：若只排除了 finite-rank 而没有付费 nonfinite-compact 修复，
不能声称方法类障碍。若新费用只覆盖旧有利高度，也要单列其实际用途，不能报 core 净进展。

**备选 B：真实 global 评价载体＋同一对象的容量不等式。**
输入是 568 的 nonzero evaluation／local jets 和 569 的 matched budget cocycle；
它们只提供前端局部设施。准入至少须展示一个具体 global source→sections/jets 的 map，
在旧 f／物理 r 坐标通过关系 η₀ 与非根 r₀ 双测试，并独立给乘法、消失和 global 高度／容量预算。
Landau–Siegel 的 same-D 局部整除＋无穷位 upper 可作组织基准，不能移植其 scalar χ 结论充作 full mixed Gram。
仅再引用 square RR 计划、正 determinant line metric 或未知 H⁰ 不准入；连续正反例必须在实际容量前件分流。

停止后的策略不应是先 A 的 unknown domination、再 B 的 unknown H⁰、再另一篇 paper 的 unknown pairing。
只有收到上面某项具体新 map／identity／可算预算才恢复数学合同。
若只需辨认某个已有来源是否提供它，保留一个限定章节且有停止条件的来源审查即可；
不连续串多个 source-only 门，不另造轮数或把每次“更接近”计成容量推进。

## 7. 本稿实际核读范围与结算

本稿本地读取了 README／STATE、check/show、Goal、C035、MACRO_FRONTIER、最新 D20261020O；
旧设施路线图；542、555、557、560、570、571、572 主稿；
570／571／572 的 root-consumption-scope；570／572 结算及 cycle14 宏观复盘；
560 的 full-inverse-carrier-error 原件（特别 §§3–5）。
本稿读取 572 fresh review 的目录／范围定位，没有声称本轮重做其独立证明审查；
没有重新浏览或重证 MV／BMS／Matveev 原论文，没有实际执行下一候选 test。

结论：局部 signed/receiver/model 原加权费用自旧路线图以来确有新结果；
独立完整容量与 actual 成长 core 的宏观瓶颈没有改变。
本次贡献为策略审计与范围闭合，0 新数学轮，不重置 cadence，不完成长期 Goal。

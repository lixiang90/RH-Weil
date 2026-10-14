# Cycle 11 来源入口：旧 Sonin/Poisson 与承担 core 的 integer carry 门

2026-10-14，代理 `/root/c017_macro_net`；准备审查计零数学轮。
只写本稿；不改 STATE/cadence/Git，不修改已经完成的 C017 宏观审查。
恢复 AGENTS/README/STATE/check/show/Goal/frontier/C017/D20261014R 后，
现场 HEAD 仍为25d856b；STATE 为 C017 running、cadence3、latest545，546已实际落盘待根结算。
子 Goal null 不代表根 Goal 终态。完整 Goal/固定≤538基线与暂停规则保持。

## 546 最终范围只读核验

已读 [546](../../../notes/546-arithmetic-comb-full-weil-positivity-and-form-core-noncoverage.md)，
所见 raw SHA256 为 `7d5657845d1d6e86b02cfb1c9c935d1e20b2f84b55918e0158a51116df0d6a95`。
其 actual Γ、原 complex norm、strict全primepowers、独立profiles和signed双pole没有被替换；
特殊类下界与原 Dlog 补空间逼近被分别列明，没有升级 whole count/RH/宏观完成。
两处纯措辞建议已通知根：generic measure bound 是 Γ尾/Plancherel 的直接消费，
不宜使读者以为023原件已经写出该明确 μ 下界；smooth complement 应写 open gaps
`Cc∞((-R,R)\overlineΩ_N)`。它们不改变数学。
原宏观独立审查 SHA256 仍为
`e4b862de1ae428b7ed621e195059efab854f137b2c62d0443fdcb31a2237cae4`。

## 一级原件筛选：两项都没有新的可直接消费 signed growth 输入

只核作者/arXiv实际原件，不凭标签、摘要或第三方评价升级。

- [CCM 2310.18423v2 原文](https://arxiv.org/html/2310.18423v2)，核§4.6–4.8、(57)–(59)、Theorem4.6/Prop4.7–4.8。
  原有限 S Sonin 同构与 Fourier/mixed pairing 真实；共同 entire 函数空间的内积依赖 S。
  531/532已精准消费这些输入，532的实际 compact bridge只付 fixed p、fixed source support，
  535的边界也只排 canonical single-prime，无声扩大到全 S 不合法。
  **全 S 共同 signed growth费用未被旧稿全部支付，但本原件同样没有给它的定量定理。**
  恢复稳定性不等于找到遗漏的 uniform residual/gap、完整 Γ/pole domination 或新 whole forcing。
  本地原PDF现场SHA与旧receipt相同：
  `8bc197642ee9ca4f2393b6cbfd3db292be6a315ce76ad61bfb845d9fedb47f2e`。
- [Connes–Consani 1910.14368v1 原PDF](https://arxiv.org/pdf/1910.14368)，核印页111–114、118–121
  （PDF页10–13、17–20），Lemma2.2–2.4、Theorem2.5/(2.28)–(2.30)、Lemma3.4、Conjecture4.1及§4.1。
  真有限 S unitary Fourier 与规范 trace identity 已有共同框架；Poisson 固定基本字符和principal-value规范。
  (2.29)是固定 S/test 的 cutoff极限，含必须保留的 `2f(1)logΛ`，不是 growing S/source 的正误差定理。
  所需半局部 Weil 正性仍为 Conjecture4.1；§4.1倍率推导明示 formal/heuristic，
  Poisson/Sonine construction没有补出原complex全域 signed norm、growth误差或dual-pole费用。

**裁定：两项来源恢复均入口零轮停止。** 不开一个把旧稳定性/trace或Conjecture4.1改名的C018；
不复活已降级的等价Hilbert酉化/源修正。2006.13771的arch输入也不重新计新。
这不排未来真正 multi-prime mixed 来源；重新准入必须有具体原定理及同 actual Q 的全源净费。

## 一个较有信息的实际入口：完整 log-cell 的 carry 与平均/零平均

以下是本代理的直接准备推导，不归属于上述作者原定理，不消费研究轮。
只给同源接口与有判真伪价值的候选费用门，不宣称新的正性定理。

冻结整数N、L=logN/2。用 `x=exp(u+L)` 将原 physical source unitary 写为

    H_N=L²((1,N),dx/x)，F(x)=f(logx−L)。

完整Γ仍在u-Fourier侧取actual2θ′，两个pole原functionals精确变为

    A_+=N⁻¹/⁴∫_1^N F(x)x^(1/2)dx/x，
    A_−=N^(1/4)∫_1^N F(x)x^(−1/2)dx/x，
    Pole=2Re(A_+ bar A_−)。

cell weighted均值0不等于这两个pole moment为0；两者没有删除。
完整 natural cells J_n=(n,n+1)，n=1,…,M=N−1 分割全部源域。
这不是薄Ω子集，每格可以保留任意complex profile；Jacobian为 dx/x。
令 ℓ_n=log((n+1)/n)，e_n=1_Jn/√ℓ_n，P为span{e_n}的**原norm正交投影**，R=I−P。
`RF` 的每个 cell weighted平均 ∫_Jn RF dx/x 为0，不能换成未经付费的 Lebesgue-dx 平均。
P有限秩、各e_n零延拓BV且属Dlog，所以对每个fixedN，P与R都保持原Dlog；
此处没有 uniformN乘子范数声明。

原prime partial translation是

    T_qF(x)=F(qx)，F在(1,N)外为0，q<N为所有实际primepowers。

它在原L²是contraction；不是有限interval上的unitary。
对 x=n+v、0<v<1，r=floor(qv)，0≤r≤q−1，有

    qx=qn+r+w，w=qv−r。

所有 qm+r carry 都要保留，r≠0不可删。
相关积分精确分解为

    ∫F(qx)bar F(x)dx/x
      =Σ_n Σ_(0≤r<q, qn+r≤M)
         ∫_(r/q)^((r+1)/q)
            F_(qn+r)(qv−r)bar F_n(v) dv/(n+v)。

换 w=qv−r 后 dv/(n+v)=dw/(qn+r+w)，原norm无丢失。
边界N为整数，最后存在的 target cell仍完整；无未付fractional target误差。

### 精确三角关系：P T_q R=0，反向费用仍在

对 RF，有

    ∫_Jn T_q(RF)(x)dx/x
      =∫_((qn,q(n+1))∩(1,N)) RF(y)dy/y =0。

积分区间端点是整数，是若干完整 input cells 的并。
即使 output cell被N/q截断，右边只是在整数N停止，仍为完整cells并。
因此对全部complex L² profiles、全部整数q≥2，

    P T_q R=0，R T_q R=T_q R，R T_q* P=0。

这是真forward整数缩放对detail子空间的不变性。
但 `P T_q* R` 与 `R T_q P` 一般非零，完整自伴prime块不是两边对角，
Γ与dual-pole也不由此分解。不能把1910 Lemma3.4的**unitary**假设套给这个partial T_q。

令C_q=P T_q P。其原normalized cell basis matrix精确是

    (C_q)_(n,m)=√(ℓ_m/ℓ_n)，
    当 qn≤m≤min(q(n+1)−1,M)；否则0。

于是 mean block 原prime adjacency 为 Σ_(q<N)Λ(q)/√q(C_q+C_q*)，
而非仅 m=qn 的divisibility matrix。
全部carry row重新带回全prime质量；不承诺logM费用。

### 一个便宜 sign 负对照

取0≠g∈Cc∞((1,3/2))，满足∫g(x)dx/x=0，令h(x)=g(x/2)。
N≥4时g、h分别在J_1、J_2，二者均属detail R。
F_±=g±h是原合法smooth source，并有

    ∫F_±(2x)bar F_±(x)dx/x=±||g||²，||F_±||²=2||g||²。

其他 q≥3 无相关。因此首prime detail contribution有两个符号。
这不推 wholeQ负，Γ/双pole仍保留；它只禁止把三角关系升级为detail prime正性。

## 为什么这个入口比再恢复Poisson更有信息价值

自然cell均值真正捕获 fixed form core。固定g∈Cc∞((-A,A))，相关cells有O_A(√N)个，
它们在u坐标的最大宽度 ε_N=O_A(N⁻¹/²)。
r_N=P_Ng−g支持于[-A−ε_N,A+ε_N]，幅度O_g(ε_N)。
内部variation来自−g'，cell间相邻均值jump至多C_g ε_N；总BV为O_A,g(1)。
因此完整频轴有

    |Fr_N(t)|≤C_A,g min(ε_N,1/|t|)。

在|t|≤1/ε_N和其外分别积分，得到

    ||P_Ng−g||Dlog²≤C_A,g ε_N[1+log(1/ε_N)]
                         =O_A,g(logN/√N)→0。

P_Ng是有限BV step源，原Dlog合法；可在原source域用smooth approximations消费。
smooth approximation不必仍位于piecewise-constant P_N；不能声称P_N本身有非零smooth basis。

与546薄Ω相反，**P_N均值core在原Dlog逼近每个fixed smooth源**。
所有完整实际primepowers、Γ与双pole也都在同一个source transport里。
但P_N有限矩阵正性未知，R-tail/coupling未知；表示和本三角恒等式本身不产生新macro结果。
这与164/167的coefficient synthesis/diagonal Gram有对象差别：这里直接是whole physical source，
并非把已付 Möbius coefficientdiagonal改名。
没有逐篇排除全部历史重复；原同行/新颖性仍按真实状态陈述。

先消费一个已经有答案的费用负对照，避免“mean-zero自动logarithmic prime费”的shortcut。
原[539](../../../notes/539-growing-weil-prime-cost-and-constant-tail-boundary.md)的finite-source-conditions/carriers
适用于R_N的M个cell weighted均值条件：这些是finite L²-continuous functionals。
所以每个fixed N，令B_N=Σ_(q<N)Λ(q)/√q(T_q+T_q*)，有

    ||R_N B_N R_N|| ≥ C_(L_N)，
    C_L=Σ_(q<exp(2L))2Λ(q)/√q[1−logq/(2L)]。

原543已付Chebyshev下界给 C_(L_N)≥A_≤(√N)≳N^(1/4)，故成长下界远大于logN。
所以free `||R_N B_N R_N||≤logN+O(1)` 已被旧实际资产排除，不能把它留为未知新输入。
这些high-frequency carriers的Γ费随log|ω|上升，539没有给统一返回费，
因此不推R_N上的wholeQ负值，也不排保Γ的relative/signed估计。

比完整R_N正性更便宜、有具体可核净值的**待证**门是：保同源signed sum，是否有固定0≤η<1、C≥0使

    <B_N f,f> ≤ η JΓ(f)+C logN||f||²，
    JΓ(f)=qΓ(f)−Γ₀||f||²，f∈R_N∩Dlog，全部N≥4。          (candidate)

这是候选引理，不是已经获得的算术输入；不会从三角身份或Poisson推出来。
若真，fullQ在detail上保正evenpole、把oddpole精确按rank-one计数责任处理后，
由旧028的actualΓ强负迹得到

    n_-(Q_(L_N)) ≤ M+1+C_(η,C)logN·N^(C/(1−η))。

这里M是mean block的finite codimension责任，+1是保留的真实oddpole；
只在count下界组织中舍去positive even square，未把pole删掉或判其为正。
任何fixed polynomial预算最终严格优于543的cofinal C exp(S)、S≈√N，
故这条新Γweighted费用若实际付清会有明确whole-core收益，同时允许负方向，非RH等价输入。
没有付candidate本身，当前不能记这个polynomial后果为已证。

更强的下一门仍可以是：对全部R_N∩Dlog源，由actualΓ/全部pp/dual-pole给

    Q_(L_N)|_R_N ≥0（或指定的−ε_N），

并给mean/detail完整cross的原norm预算。先做原合法反例/fee必要量，不先扩大finite matrices。
若R_N≥0真，则仅由codimR_N=M便严格给 n_-(Q_LN)≤M=N−1，
潜在 polynomial core 比543的cofinal C exp(S), S≈√N 强很多。
这只是**若费用支付后的具体收益**，不是该sourceidentity已经给出的后果。
若只给−ε，则对应的是shifted惯性，不能改称未shifted count。
完整PSD仍另需P_N最低值、reversecross及Schur费用，不能用RH等价全domination充独立输入。

推荐next只进入这一可反例的detail source费/mean-zero response门；
若只有carry表示和三角代数，无新Γ/pole joint或实际费用负对照，则入口零轮止损，
不用“已经捕获core”掩盖仍未付费用，也不继续薄positive classes。
原Goal保持完整；来源筛选、准备恒等式和此次最终范围核验均不另推进cadence。

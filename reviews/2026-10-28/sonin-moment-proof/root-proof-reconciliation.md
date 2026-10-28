# C050 proof reconciliation：Gaussian比较与actual源矩量

2026-10-28；同Goal/runtime1793085111/原0c4f。两当前独占终稿12142b/1ce4ebc0与13009b/e76fefa4，以及fresh9957b/a1359cc4已root全文核。全线norm/t²尾/frame逆、Jacobi HS域与fixed-degree路径前件已对齐，以下作为已闭合证明消费。最终证据587只统一一轮；Goal仍open。Fresh绑定本稿5063b/b277ff81的条件草稿，最终稿仅解除已核conditional并记录同链最强scope。

## 共同尺度与角色

ℓ=logX、A=√X/ℓ，w_X=|D_Euler,X|²。H₀为585已付的同一个实际Sonin向量，全部polynomial倍合法。固定小δ使H₀及h=rhat₀在|t|≤δ均非零；c>0固定且足小，N=⌊c A/ℓ⌋。实际Hilbert measure为dt/(2π)。

辅助 measure为 `dμ_G=w_X e^(-t²)dt/(2π)`，真实trial measure为 `dμ_H=w_X|H₀|²dt/(2π)`。Gaussian没有被放进Sonin空间，μ_G不是actualρ_X；只有D_Euler pH₀是真实trial向量。p_j为μ_G的real正交规范多项式。

norm腿已完整付款：对deg≤N+2所有complex polynomial的两套**全线**norm统一等价，Gaussian的t²加权core外尾也小。因此对n≤N+1的Jacobi系数有a_n²≤C₀，不是从未加权的概率集中直接省掉t²尾。旧H₀全尾与Gaussian全尾须分别核；后者|t|>X²用Gaussian压过degree和Euler指数。

## Gaussian Jacobi核心：一个可独立检查的全局lemma

令V=t²−logw_X。有限Euler的绝对可微级数给

\[
 |V''(t)|\le2+2\sum_{p\le X}(\log p)^2\frac{p^{-1/2}}{(1-p^{-1/2})^2}
 \le\Lambda_X\le C\sqrt X\log X=C A\ell^2.
\]

这里prime upper只需Chebyshev。μ_G为even positive全线权，正交polynomial满足 `tp_n=a_(n+1)p_(n+1)+a_n p_(n-1)`、a_n>0。记P_n投影到degree<n。所有有限rank核与t、V′的乘积由Gaussian全矩保证HS；不套未经证明的operator-Lipschitz定理。

分部积分与正交性给 `〈V′p_n,p_(n-1)〉=n/a_n`。核逐点Lip界给

\[
 \|[V',P_n]\|_{HS}\le\Lambda_X\|[t,P_n]\|_{HS}
 =\sqrt2\Lambda_X a_n.
\]

左侧两个共轭矩阵元已至少为 `sqrt2 n/a_n`，从而 **a_n²≥n/Λ_X**。这一步是新proof核心，不能以三个scalar moment lower替代。

## 从辅助polynomial trace到actual trace

令v_j=D_Euler H₀p_j，j<N，真实frame Gram H满足cI≤H≤CI。实际投影是V H⁻¹V*，保全Gram逆。对source多项式P，真实source为Fourier hP的r；必须使用源域而非把p_j叫source。

数值型B(P)由 `∫|hP|² v_j overline(v_k) dt/(2π)` 给，故

\[
 t_X[r]\ge\operatorname{Tr}(H^{-1}B(P))
 \ge C^{-1}\sum_{j<N}\int|hPp_j|^2d\mu_H.
\]

在core中h有固定正lower，μ_H与μ_G可比；对Pp_j degree仍在已付范围时，Gaussian多项式全尾小，得到

\[
 t_X[r]\ge c\sum_{j}\|Pp_j\|_{L^2(\mu_G)}^2.
\]

这里可只取j<N−d以保证deg(Pp_j)<N（d=degP先fixed），不增degree预算。所有求和有限且actual Π_X ordinary trace/HS域已付。

## 三源与更强fixed-degree后果

P=a+ibt−ct²时，parity分解及p_j、p_(j+1)、p_(j+2)分量给

\[
 \sum_{j<N}\|Pp_j\|^2\ge c\frac{N^3}{\Lambda_X^2}
 (|a|^2+|b|^2+|c|^2),
 \qquad N^3/\Lambda_X^2\asymp\sqrt X/(\log X)^8.
\]

Jacobi腿已付款：p_(j+2)分量是−c a_(j+1)a_(j+2)，p_(j+1)为ib a_(j+1)，p_j为a−c(a_j²+a_(j+1)²)，使用共同a_j upper与a/c分情形，不让moving系数取消方向漏掉。actual运输后即给E₃共同lower，进而𝔇_X≥c√X/log⁸X。

同lemma已经给更强**每先fixed degree d**的后果。对j∈[N/2,N−d)，t^ℓp_j在p_(j+k)分量的每条Jacobi路径都含所有mandatory up-edges a_(j+1)…a_(j+k)。除去这一乘积后，剩余路径系数由a≤C₀固定有界，三角矩阵diag1及其inverse均由d控制。完整路径代数已核闭，故

\[
 \sum_j\|Pp_j\|^2\ge c_d N(N/\Lambda_X)^d\|\operatorname{coeff}P\|^2
 \asymp c_d\sqrt X/(\log X)^{3d+2}\|\operatorname{coeff}P\|^2.
\]

消费这份同lemma最强fixed-degree后果，路径代数已由主稿/fresh/root逐项核闭。d必须先fixed，不能宣称d_X成长uniform。所有源都是固定r₀导数的fixed有限维空间，原du/Dlog基Gram固定正定，费用可依d。

## 完整型与净scope

所有X用fixed I=(-17/16,17/16)，大X覆盖本源全部visible prime后，KGram=traceGram−QGram+PGram。后二矩阵fixed且完整Γ/FP-contact、properpowers、双pole均保；odd pole负号不删。源基Norm congruence须显式支付。

E_(d+1)实际最小特征值下界已闭合，故对任意共同Hermitian source-rank≤d补偿R_X，压缩kernel内moving单位向量给residual operatornorm同阶必要费；有限个**fixed**极化测试把pointwise-fixed全部有界的声称转为矩阵有界，因而矛盾。允许R的norm成长、range移动/非局部、系数有符号；不能把receiver-trial projection rank当source-form rank，也不把逐源不组成共同Hermitian型的规则塞进此类。

这给指定actual K上新的finite-dimensional source-uniform/core费用，既非Q负例，也不支付净signed正号、whole4/5改善、primitive/principal/mixed或Ξ。Growing rank/无限秩及不同正D′/有费joint规则仍可能；宏观Goal完成门保持open。新math/轮数仅在两个终稿、fresh和root最终闭合后统一结算一次。

## 最终根消费与停止

根确认actual𝔇≥c√X/log8及所有先fixed d的c_d√X/log^(3d+2)源共同lower。固定原du/Dlog费、完整Q/P和actual source-rank角色闭合。若补偿rank沿某子列有固定上限，同一有限极化测试在该子列仍矛盾，所以bounded-fixed-source residual要求rank→∞；无增长率。每fixed-X自伴紧K的|λ|>1谱截断是已付非空成长rank逃逸，但按K定义，非独立正性input。非零finite receiver projection诱导的源型可无限rank，不能套本边界；不回滚EX原停门。C050耗尽，不续log/degree/rank优化或source查询；真正新净signed/成长rank独立实物才另判。详587及root-consumption-scope.json，宏观关键门/whole4/5UPPER仍未改。

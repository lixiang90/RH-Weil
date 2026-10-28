# 588：共同支撑弱源强制性与局部正补全的最优边界

2026-10-28；C051，G20261027／原冻结0c4f。当前主证明7402b、域证明12612b和独立逆审11860b已root逐段核对。本文统一消费一轮新数学；准入、辅助域腿、审稿与发布不另计。依赖与规范版本见[root消费收据](../reviews/2026-10-28/local-anchor-proof/root-consumption-scope.json)。

## 1. 原对象与新的弱源量词

沿560／585／587的实际Sonin投影Π_X，有限Euler乘子及其完整Gram逆／returns全部保留。物理log源记r，原裸源为e^(-u/2)r；Fourier规范为rhat(t)=∫r(u)e^(-itu)du。实际普通迹为

\[
 T_X[r]=\operatorname{Tr}(A_r\Pi_XA_r^*)
       =\int_{\mathbb R}|\widehat r(t)|^2\rho_X(t)\,dt\ge0.
\]

ρ_X已经含归一化；Plancherel及trial norm内才用dt/(2π)。任意先固定有界开窗J上，源域为零延拓

\[
 V_J=D_{\log}(J)=\left\{r\in L^2(J,du):
 \frac1{2\pi}\int\log(2+|t|)|\widehat r(t)|^2dt<\infty\right\}.
\]

**弱源定理。** 若X_n→∞，f_n∈V_J，sup_n||f_n||du<∞，且f_n⇀f≠0于L²(J)，则

\[
 \boxed{T_{X_n}[f_n]\longrightarrow+\infty.}\tag{L}
\]

不要求Dlog norm共同有界，也不要求弱极限f仍在V_J。更确切地，令k=ord₀ fhat（有限），存在依该序列／弱极限的c>0和起点，使

\[
 T_{X_n}[f_n]\ge c\frac{\sqrt{X_n}}{(\log X_n)^{3k+2}}.
\]

这是序列依赖的下界，不是全L²单位球的统一速率。

证明：共同支撑与du界给F_n(z)=fhat_n(z)的entire normal-family界；弱du收敛给每个complex z的极限，因此F_n→F局部一致，F不恒零。选一次fixed disk使F除0处k重零外无零。Rouché使F_n在盘内恰有k根，全部趋0。提出其monic多项式P_n，商U_n=F_n/P_n在盘内holomorphic；边界及最大模原理给U_n→F/z^k一致。因而在fixed real core上|F_n|≥u_*|P_n|，u_*>0、||coeff P_n||≥1。k=0同理。

按这个core一次选择587允许的fixed c_δ及N=⌊c_δ√X/log²X⌋，不沿用较大core的c。取ceil(N/2)≤j<N−k的真实trial D_Euler H₀p_j。完整frame Gram逆、core比较和全部多项式全线尾给

\[
 T_X[f_n]\ge c\sum_j\|P_np_j\|^2_{w_Xe^{-t^2}dt/(2\pi)}
 \ge c_k\frac{\sqrt X}{(\log X)^{3k+2}}.
\]

这里deg(P_np_j)<N，k先固定，系数可移动；Gaussian仅辅助norm，H₀仍是真实Sonin向量。没有把o(1) Fourier误差乘无界迹质量，也没有改候选的源、窗口或成长秩。完整论证见[root主稿](../reviews/2026-10-28/local-anchor-proof/root-weak-source-and-anchor-proof.md)。

## 2. 任意维数局部正修正都不能覆盖窗外源

取537原anchor I₀=(-17/16,17/16)，其完整经典Weil型满足

\[
 Q_W[q]\ge\kappa\|q\|_{du}^2,
 \quad\kappa=2^{-49162},\qquad q\in V_A=D_{\log}(I_0).
\]

r₀为587中du norm1、支持[-1,1]的固定实偶bump；固定r_a=τ₄r₀，支持[3,5]。完整型平移不变，包含全部Γ／FP-contact、Λ(p^k)=log p以及两个pole的Lorentz差。因此Q_W[r_a]=Q_W[r₀]≥κ，为固定有限正值。

对于任何合法q_X(r_a)∈V_A，考虑两项正分解

\[
 W_X[r_a]=T_X[r_a-q_X]+Q_W[q_X].
\]

若沿cofinal子列有界，两项非负及κ先给q_X的du界。抽弱子列后，残差支持共同大窗J，du有界，弱极限在[3,5]仍等于r_a，故非零。(L)矛盾。近似极小元也给同一论证，所以最强同类结论是

\[
 \boxed{\inf_{q\in V_A}\{T_X[r_a-iq]+Q_W[q]\}\longrightarrow+\infty.}\tag{1}
\]

i表示零延拓。它覆盖任意成长秩、合法无限维局部range和逐源适应／非线性选择，不需投影或线性假设。若称共同positive form，仍须另核sesquilinearity。

实际非空候选是E_X=span{r₀,…,r₀^(⌊logX⌋)}，以T_X有限正定Gram全逆构造源投影P_X，再令W_X(r,s)=T_X((1−P_X)r,(1−P_X)s)+Q_W(P_Xr,P_Xs)。它只在E_X精确匹配Q；P_X不同于receiver Π_X，有限层PSD form不自动是一变量正D′。本定理排除它对全部fixed源趋于完整Q。

两正项系数各有统一正下界时仍失败；fixed test上有界的signed扰动也不能修复。若额外项B_X使总值趋于Q_W[r_a]，则必有B_X[r_a]→−∞。成长／漂移anchor、消失迹权、失去统一coercivity及无界signed cross均不在本边界内。

## 3. 最优能量的完整域与极限

固定J包含anchor及[3,5]，H_J=L²(J)，H_A=L²(I₀)，i:H_A→H_J零延拓，i*为restriction。它们均为源空间，区别于receiver Hilbert。

560给2πρ_X=log(2+|t|)+b_X，b_X为逐fixed-X有界实symbol，所以T_X是域准确为V_J的非负闭型；ordinary trace身份沿原core保持。Fourier band截断的HS核给V_J↪H_J紧；高频ρ_X>0和compact源Fourier entire给kernel0。因此逐fixed-X的T_X norm与V_J norm等价，常数允许依X。anchor Q为同一log主型加bounded自伴项，κdu使Qnorm与V_A norm等价且闭。这里只在anchor用Q正性。

定义最佳能量

\[
 \mathcal F_X[r]=\min_{q\in V_A}\{T_X[r-iq]+Q_W[q]\}.
\]

其有限域准确为V_J。混合能量方程

\[
 T_X(iq_X,iv)+Q_W(q_X,v)=T_X(r,iv),\quad v\in V_A
\]

以Lax–Milgram给唯一complex-linear极小元，完成平方核极小性；它不是自动存在的无限维T-正交投影。逐fixed-X norm等价给F_X闭性。

由(L)及Q的V_A弱下半连续性，若r_n⇀r且F_(X_n)[r_n]有界，最优q_n在V_A弱趋q，残差弱极限必须为0，故r=iq且liminf≥Q[q]。anchor内取constant recovery，直接得到Mosco极限及全部fixed r的extended点态极限

\[
 \mathcal F_X\longrightarrow\mathcal F_\infty,
 \qquad
 \mathcal F_\infty[r]=
 \begin{cases}Q_W[q],&r=iq,\ q\in V_A,\\+\infty,&\text{其余 }r\in H_J.\end{cases}\tag{2}
\]

极限有限域iV_A在H_J中非稠密。令𝒜_X、𝓑_X分别为T_X、F_X的源自伴算子，𝒜_Q只在H_A上关联anchor Q。能量恒等式与(L)进一步给

\[
 (\mathcal A_X+1)^{-1}\xrightarrow{strong}0,
 \qquad
 (\mathcal B_X+1)^{-1}\xrightarrow{strong}
 i(\mathcal A_Q+1)^{-1}i^*.
\]

这些是bounded resolvent的强极限；右侧是消掉anchor外方向的广义resolvent，不是整个H_J上稠密自伴算子的普通resolvent。不声称operator-norm收敛或λ_X→∞。域和能量自给证明见[独占域稿](../reviews/2026-10-28/local-anchor-proof/source-form-domain-and-resolvent-corollary.md)。

## 4. 净增量与停止范围

585的每fixed源发散、587的fixed有限导数空间共同gap及更强trial设施均为输入；新增是任意commoncompact／du弱非零moving源的exact解析因子化消费，以及整个fixed-coercive-anchor正分解类的最佳能量边界。未提供新的独立算术数据或外部优先权声明。

局部方法瓶颈改变：提升rank或允许局部无限维最优化不能修复此类。完整signed消失、成长／非局部耦合、同一非零primitive／principal／截面乘法／mixed RR与Ξ仍欠；whole542＋555→557 leading4/5仅负惯性UPPER未改。587按K定义的成长秩谱截断不属于本类，合法逃逸保留。

C051统一一数学轮，cadence1→2、历史51→52，formal17不重置；预算耗尽，不续anchor参数／rank／rate优化。Goal同实例1793085111仍active，原完成门open／not-eligible。下一先完成授权main发布；后继数学须有真正新actual输入或能改变选择的具体比较，未排标签本身不授合同／来源预算。

# 真实半局部 Sonin 正迹的算术主项与完整首素数型的紧余项桥

2026-10-14；C005第二轮，基线 `3a72930e9f9f554b03b41d17d8c8002f1813ca82`。
状态：proved，消费范围为每个固定单素数、固定有限源域。
证明由[独立密度推导](../reviews/2026-10-13/c005-flux/direct-symbol-audit.md)、
[来源/单边界审查](../reviews/2026-10-13/c005-flux/trace-source-audit.md)及
[不同组织逆审](../reviews/2026-10-13/c005-flux/reverse-audit.md)核对。
完整 Weil 正性、剩余紧型符号及成长素数集费用未证。

## 1. 实际对象和结论

沿[531](531-semilocal-sonin-positive-trace-and-non-hilbert-schmidt-cutoff.md)，
实际物理偶空间unitary转为 `L²(R,dy)`，源scaling `U_t f(y)=f(y−t)`。
固定Sonin cutoff1；P为真实实位Sonin正交投影，不是标准锥或未知最低态。
对固定素数p，`a=logp,q=p^(−1/2),B=I−qU_a`，

\[
 P_p=BP G^{-1}PB^*,\quad G=(PB^*BP)|_{\operatorname{Ran}P},
 \qquad T_p(g)=\operatorname{Tr}(A_gP_pA_g^*)\ge0,
 \quad A_g=\int g(t)U_tdt.
\]

θ_p只是有界可逆同构；上式保留真实物理正交化。光滑紧支g的正迹已由531支付。
以下原一级输入是[CCM v2 (57)–(59)、Theorem4.6](https://arxiv.org/html/2310.18423v2)
及实位正迹原定理；已有相位/同构不重记新。

**算术主项定理。** 令ρ_p为真实裸unitary Mellin求值的迹密度，
`T_p(g)=∫|ĝ(s)|²ρ_p(s)ds`，这里 `ĝ(s)=∫g(t)e^(−ist)dt`。
每个固定p有

\[
 \rho_p(s)-\rho_\infty(s)
 =-\frac{a}{\pi}\sum_{n\ge1}q^n\cos(nas)
   +O_p(|s|^{-1/4}\sqrt{\log|s|}),\qquad |s|\to\infty.
\]

因此对**每个固定有限测度源支持U**，存在有界自伴紧算子C_{p,U}，使

\[
 T_p(g)-T_\infty(g)
 =-a\sum_{n\ge1}q^n\bigl(R_g(na)+R_g(-na)\bigr)
   +\langle g,C_{p,U}g\rangle,
 \quad R_g(t)=\int g(y+t)\overline{g(y)}dy.
\]

这正是实际p及其全部primepowers的负贡献，权重`Λ(p^n)/√(p^n)=a q^n`。
不拟合ζ零点、不移原子、不增加C001样本，也不从相对Gamma范数界消费固定质量费用。

## 2. 原生 Gamma 相位给统一窗口运输

实际cosine Fourier在log频率中的表达为

\[
 \widehat{Ff}(s)=m(s)\widehat f(-s),\quad
 m(s)=\pi^{is}\frac{\Gamma(1/4-is/2)}{\Gamma(1/4+is/2)}.
\]

连续相位满足 `φ′(s)=−K(s)`，actual `K=2θ′`，
`K(R)=log(R/(2π))+O(R^(−2))`、`K′=O(1/R)`；
标准Gamma展开见[DLMF5.11](https://dlmf.nist.gov/5.11)。取R大、T=K(R)>0。
对任意有限区间J，有与J位置/长度无关的估计

\[
 \|F(e^{iRy}1_J)-m(-R)e^{-iRy}1_{T-J}\|_2\le cR^{-1/4}. \tag{1}
\]

证明：频率中心为−R；在`|ξ|≤√R`相位差≤`cξ²/R`，外区模差≤2。
区间傅里叶变换统一满足`|hat1_J(ξ)|≤c/|ξ|`。
Plancherel误差平方由`∫_{|ξ|≤√R}ξ²/R²+∫_{|ξ|>√R}ξ^(−2)`控制，
为O(R^(−1/2))。线性相位对应T−J；没有额外RT相位。
所有载波都乘有限区间，未把全域plane wave当L²向量。

令L=1_{y<0}、H=I−L、K₀=LFL、R₀=(I−K₀²)^(−1)。
实位有限Fourier紧且norm<1，真实Sonin投影是

\[
 P=H-HFLR_0LFH. \tag{2}
\]

其依据为`(HFL)*(HFL)=I_L−K₀²`，是正交投影公式。
两次使用(1)：r=LFH载波近反射后的低区间，K₀r=O(R^(−1/4))，
故`(R₀−I)r=O(R^(−1/4))`。于是实际P给统一clipping

\[
 \|P(e^{iRy}1_J)-e^{iRy}1_{J\cap[0,T]}\|_2\le c_PR^{-1/4}. \tag{3}
\]

这已经支付双边界和实际逆算子；不能只凭单边界Poisson核替代它。

## 3. 真实求值域与完整 Gram 逆

裸Mellin求值k_R为RanP中的Riesz向量。合法构造是
`P(e^{iRy}1_[−M,M])/√(2π)`的弱极限，M>T。
(3)使它有界并且距 `w_R=e^{iRy}1_[0,T]/√(2π)` 至多O(R^(−1/4))。
稠密物理核心`P Cc∞((0,∞))`在x<1为0、x→∞为O(1/x)：
(2)的低区间resolvent向量由光滑核平滑至端点，Fourier分部积分给该尾。
故核心上的裸Mellin积分绝对收敛，弱极限与真实求值一致且唯一，

\[
 \|k_R-w_R\|=O(R^{-1/4}). \tag{4}
\]

原Sonin/de Branges连续求值保证密度局部有界且范数连续，
不是仅从弱连续性推范数连续性。保持裸求值及Gamma-completed求值的区别。

真实密度由HS迹的Tonelli求和给

\[
 \rho_\infty(R)=\|k_R\|^2,\qquad
 \rho_p(R)=|1-qe^{-iaR}|^2\langle k_R,G^{-1}k_R\rangle.
\]

设C=P(U_a+U_a*)P、C_T=1_[0,T](U_a+U_a*)1_[0,T]，
α=1+q²、r=q/α、ρ=2r<1。两者完整Gram逆均有Neumann级数。
C_T^j w_R至多包含2^j个区间载波；由(3)、(4)递推

\[
 \|C^jk_R-C_T^jw_R\|\le c(j+1)2^jR^{-1/4}.
\]

加权`Σr^j(j+1)2^j=Σ(j+1)ρ^j<∞`，故**完整**逆的向量误差为O_p(R^(−1/4))。
密度误差为O_p(R^(−1/4)√logR)。没有留下随载频增长的未控relativeΓ尾。

## 4. 有误差控制后的窗口精确算术计算

将[0,T]按 `y=θ+ja,0≤θ<a`分解，每fiber有n(θ)个连续格点。
B把基e_j送到`e_j−qe_(j+1)`；其范围在n+1维中的正交补是
`v_j=q^(n−j),j=0,...,n`。该fiber的投影密度差为

\[
 \frac1{2\pi}\left(1-
 \frac{|\sum_{k=0}^nq^ke^{-iRak}|^2}{\sum_{k=0}^nq^{2k}}\right).
\]

积分θ、统一几何尾，得到

\[
 \rho_{p,\mathrm{model}}(R)-T/(2\pi)
 =\frac a{2\pi}\left(1-\frac{1-q^2}{|1-qe^{-iRa}|^2}\right)
  +O_p(q^{\lfloor T/a\rfloor}).
\]

Poisson恒等式给`−a/π Σq^n cos(naR)`；几何尾O_p(R^(−1/2))。
与实际投影/求值/完整逆误差合并即主项定理。负载频由真实算子的实结构对称。
它不仅是线性first-order q近似，所有真实p幂在同一身份中出现。

## 5. 真正源 L² 紧余项与完整冻结消费

令
`r_p(s)=2π(ρ_p−ρ∞)+2aΣq^ncos(nas)`。
真实求值的局部有界性及主项估计给r_p∈C₀(R)。
在固定U上压缩单位Fourier乘子M_{r_p}：频率截到[−N,N]的核有界，
在U×U为HS；外频尾范数≤`sup_|s|>N |r_p(s)|→0`。所以余项确为源L²紧算子。
这是实际诱导二次型紧性，符合530的准确拓扑。

还可不依赖旧ε核的点值解释，直接写真实overlap乘子
`ε_p(s)=2πρ_p(s)−K(s)+2aΣq^ncos(nas)`。
因(4)给`2πρ∞−K→0`，有ε_p∈C₀(R)。
所以`T_p=Γ−Pprime_p+<g,F* M_εp Fg>`，余项与下文实际overlap迹相同。
这给剩余低域一个准确可审对象；ε_p∈C₀仍不表示ε_p≤0。

对C004冻结 `a=log2,b=log(3/2)/4,μ=13/5` 两patch：
pole因ℓ₁/₂=0消失，真实primepower只有2，原实位E∞亦为源紧型。
因此

\[
 T_2-T_\infty=-w_2\mathrm{Swap}+C_U,\qquad
 Q_W-T_2=\widetilde C_U,\qquad w_2=\log2/\sqrt2.
\]

所有常数、完整Gamma、prime和pole都在同对象上保留。
合法弱零h_R给

\[
 (T_2-T_\infty)(U(h_R,\pm h_R))\longrightarrow\mp2w_2.
\]

首素数非紧费用已支付；`Q_W−T2`不再留530的非紧Swap。
两个紧算子不预设正负，结论不推出Q_W≥T2或Q_W出现负值。

另可精确识别实际剩余：令E为高半线、Q_v为F_v高半线投影、
S_v为真正双边界Sonin投影，`R_v=S_v−E−Q_v+I`。
源夹心`A_gR_pA_g*`为TC（完整正迹差和单边界TC差组织），
单边界trace精确为负prime型，实位trace为Γ+E∞，因而
`T_p=Γ−Pprime_p+Tr(A_gR_pA_g*)`。
在冻结实际域 `Q_W−T2=−Tr(A_gR2A_g*)`；本定理支付该实际overlap的源紧性，
其低域符号仍是新的明确未付输入。ambient R2非HS与源紧性并不冲突。

## 6. 净后果、边界及下一动作

此前缺的是独立正来源对实际prime的消费；这次通过真实Gamma相位和双边界投影，
支付全部固定p幂主项及固定源余项，改变了这条箭头，
不是只把未知正性换成Hilbert同构或给新等价命名。
原2021正迹/2024Sonin同构、旧511Fourier相位和514不同边界费用不重复记新。
内部模型逆审、原件核读及基线范围均留原件，不声称世界优先权/外部评议完成。

531的非HS/绝对系数边界保持；新证明用实际Gamma相位有符号分析绕过它，
不无声复活已停止的绝对prolate证明。
本结论只给固定p、固定U；不提供全成长S/U统一常数、紧误差符号或最低态/prolate排序。
长期Goal保持active。

停止重新计算已付首素数或将C₀当正性。重新准入旧绝对路线仍须新实际有符号输入。
唯一下一动作转[C006](../goals/contracts/C006-late-prime-sonin-overlap-budget.md)：
在同一冻结源域审晚素数添加的真实Sonin overlap费用，
区分可求和算术抵消与仅粗normtransport，不能把固定源紧性当成长预算。

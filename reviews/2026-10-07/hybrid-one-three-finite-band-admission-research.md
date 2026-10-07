# 原 actual13 的有限频带准入：两次 P crossing 与全高度替换

2026-10-07。作者 twisted_research。状态：新完整推导，等待独立全文审查。
不修改旧报告、notes、论文、math、脚本、output 或 Git。

接 [物理13推导](hybrid-signed-one-three-physical-resonance-research.md)，
本次补上此前留下的 finite-P bridge。相对于其同一 [R]（只需 zeta
zero-free theta<9/10 与 fixed-gap logarithmic-control），证明

\[
 \boxed{\operatorname{Tr}(C_HC_L^3)=o(d).}                 \tag{1}
\]

这是**原 actual finite matrix**的 entire13 sector，包括全部重复与
distinct genuine-prime 标签、所有 signs、四 placements、carrier 和内部 P。
它不证明31、distinct22或全 fourth budget；不能由此宣布新比例或 RH。
新工作是下面具体 finite-band / two-crossing bridge，未以未知 full fourth
或任意 moving coefficients 的 canonical cancellation 为前件。

## 1. 原对象及准确 Fourier 乘子

定义与原归一化完全沿用上述物理报告的 (2)–(6)：
`X=T/(2pi)`，`L=logX`，`Z=sqrtX`，`d=floorXL`，
`E e_k=L^{-1/2}1_I exp(i tau_k u)`，`tau_k=T+2pi k/L`，
`P=EE*`，`Q=1-P`，原 even C² taper phi 支撑 I、0<=phi<=1。
`phi` 和 `phi²` 的二阶导数 L¹ uniformly bounded，`a_L` 有固定正下界。

本报告 Fourier transform取 unitary `F f(t)=(2pi)^{-1/2}int f(u)e^{-itu}du`。
另以 `hat phi` 表示 nonunitary integral transform。置

\[
 Q_R(t)=\sum_{p\in R}\frac{\log p}{\sqrt p}p^{it},\qquad
 D_R(t)=-\frac{Q_R(t)+Q_R(-t)}{a_LL},\qquad
 B_R=M_\phi\mathcal F^{-1}M_{D_R}\mathcal F M_\phi.        \tag{2}
\]

R=L 指 p<=Z，R=H指 Z<p<=X；D_R 是原 real even multiplier。
(2) 准确等于 `sum B_p`，没有改变符号或 Fourier normalization。
Chebyshev 的全高度 absolute bounds给

\[
 m_L:=\|D_L\|_\infty\ll\sqrt Z/L,\qquad
 m_H:=\|D_H\|_\infty\ll\sqrt X/L.                        \tag{3}
\]

定义同一 fixed numerical band与辅助 operators

\[
 J=[T/2,3T],\quad D_R^g=D_R\mathbf1_J,\qquad
 B_R^g=M_\phi\mathcal F^{-1}M_{D_R^g}\mathcal F M_\phi,
 \quad C_R^g=E^*B_R^gE.                                  \tag{4}
\]

B_R^g 仍 selfadjoint，因为 D_R^g real；不要求 J 关于0对称。
它是本次估计的辅助域，最终结论回到原 (2)，不更换研究目标。

由 [446 的 shifted sharp Λ Perron](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md)
并保留 principal term与 pointwise proper-power difference，对每个固定
theta<a<1，在 J 及 -J 上同用

\[
 q_H:=\|D_H^g\|_\infty\ll_a X^{a-1/2}L,
 \qquad q_L:=\|D_L^g\|_\infty\ll_a Z^{a-1/2}L.            \tag{5}
\]

这里 (5) 只控制原 canonical sharp prime sums，尚未用于任何随 row 变化的
error coefficients；`||B_R^g||<=q_R` 是真正的 global Hilbert-space norm。
取 a=89/100，原 theta=7/8 已足够。

## 2. 全高度 packet 尾：原 finite matrices 与带内 matrices

令 `F_0=mathcal F M_phi E`（此符号不是低素数 F budget）。其 columns为
`(2pi L)^{-1/2}hat phi(t-tau_k)`。因此

\[
 \|F_0\|\le1,\quad\|F_0\|_2\le\sqrt d,\qquad
 \|\mathbf1_{J^c}F_0\|_2^2
 \ll(d/L)T^{-3}\ll T^{-2}.                               \tag{6}
\]

所有 tau_k 在 [T,2T)，距 J^c 至少 T/2；二阶 Fourier尾给每列
`int_|t-tau_k|>=T/2 |hat phi|²<<T^{-3}`。这里 d/L~T，不能遗漏
原 E normalization的 1/L。
`C_R-C_R^g=F_0* M_{D_R 1_Jc} F_0`，故

\[
 \|C_R-C_R^g\|_2\ll m_R/T.                               \tag{7}
\]

有限 word telescoping 的每项用 HS–HS，另外三个 compressed factors的
op<=m_R（good/original均如此），得到对任何一个13 placement

\[
 |\operatorname{Tr}(C_HC_L^3)
       -\operatorname{Tr}(C_H^g(C_L^g)^3)|
 \ll\frac{\sqrt d}{T}m_Hm_L^3.                            \tag{8}
\]

实际 normalized费用

\[
 \frac{m_Hm_L^3}{T\sqrt d}
 \ll X^{-1/4}L^{-9/2}=o(1).                               \tag{9}
\]

此处未在 low absolute height使用 (5)；全 height ghost项由 (3)、(6) 支付。

## 3. 物理四词也可回到同一带内：first-large-jump HS

写 `K=mathcal F M_phi² mathcal F^{-1}`，其 convolution kernel为
`(2pi)^{-1}hat(phi²)(t-s)`。原 physical word 的准确 Fourier形式是

\[
 \operatorname{Tr}(F_0^*D_{R_1}K D_{R_2}K D_{R_3}K D_{R_4}F_0).
                                                               \tag{10}
\]

固定 `J_0=[9T/10,21T/10]`，eta=1/100。按 kernel 分解
`K=K_near+K_far`，near取 `|t-s|<=eta T`。C²尾的 Schur与平方积分给

\[
 \|K_{\rm far}\|\ll T^{-1},\quad\|K_{\rm near}\|\le2,
 \quad\|K_{\rm far}\mathbf1_{J'}\|_2\ll T^{-1}            \tag{11}
\]

对任意 length O(T) 的 interval J' 一致。最后一界由
`|J'| int_|v|>etaT |hat(phi²)(v)|² dv<<T*T^{-3}`，不是单用 op尾。
同时 `||1_J0c F_0||_2<<T^{-1}`，证明与 (6)相同。

在右 input `1_J0 F_0` 且三个 K全为 near 时，所有四个 multiplier heights
均在 `J_0+[-3eta T,3eta T] subset J`。因此 (10) 在这个子词中，
**逐个** D_R改为 D_R^g 后准确不变。无需假设 prime相位或 profiles独立。

展开三个 K的其余七个词，取从右数第一个 far：之前的 operators均 near，
其 input频带为某个固定 length O(T) interval J'。用 (11) 的 HS界，
之前 operators op<=2^3乘对应m_R，之后亦以全高度 m_R和固定op界控制。
左端 `F_0*` 的 HS norm<=sqrt d，故每词trace费用
`O(sqrt d T^{-1} product m_R)`。右 input `1_J0c F_0` 的费用同型。
raw/good两组均满足此证明，all-near共同子词相消。

得到对每个 placement，准确的比较界

\[
 \left|\operatorname{Tr}(E^*V_1V_2V_3V_4E)
 -\operatorname{Tr}(E^*V_1^gV_2^gV_3^gV_4^gE)\right|
 \ll\frac{\sqrt d}{T}m_Hm_L^3=o(d).                       \tag{12}
\]

这是保持原 full-height multipliers的有限算子证明；不能只用
`||K_far||=O(1/T)` 乘 d，因为那会给错误的正幂费用。first-large-jump
的 HS界和左 finite packet HS是 (12)的两个关键。外侧与原 finite carrier
均已包含；不需要 entire prime第四矩。

## 4. 带内 operator 的原 P crossing

这是新 bridge的第二核心：global band op (5) 并不能自动控制
`Q B_R^g P`，须按原 e基实际计算。
因为 B_R^g输出支撑于 I，Q 的相关部分是 I 上 full Fourier basis中
j不在[0,d-1]的那些项；没有漏掉实线 I^c分量。对任意 j∈Z、0<=k<d，

\[
 (B_R^g)_{jk}=\frac1{2\pi L}\int
 \overline{\widehat\phi(\xi-2\pi(j-k)/L)}
 D_R^g(\tau_k+\xi)\widehat\phi(\xi)\,d\xi.                \tag{13}
\]

对每个 n=j-k，outside j对应 k 的数量正好 `min(d,|n|)`。定义

\[
 W_L(\xi)=L^{-2}\sum_{n\in\mathbb Z}\min(d,|n|)
          |\widehat\phi(2\pi n/L-\xi)|^2.
                                                               \tag{14}
\]

Uniform shifted-grid bound为

\[
 W_L(\xi)\ll\ell_0+L|\xi|,\qquad
 L^{-2}\sum_n|\widehat\phi(2\pi n/L-\xi)|^2\ll1.           \tag{15}
\]

证明：置 nu=Lxi/(2pi)，用 `|n|<=|n-nu|+|nu|`。
第二项由 (15)右界付 `O(L|xi|)`。第一项对最近格点用 `|hat phi|<=CL`，
距离1到O(L)用 `|hat phi|<=CL/|n-nu|`，产生 harmonic logL；更远用
二阶界 `CL²/|n-nu|²`，square后的加权尾为O(1)。因此 shifted lattice
任意接近整数的情况亦包含；不能把 xi当作整数格点。

Minkowski于 (13)、sup D_R^g=q_R及 (14)，给

\[
 \begin{aligned}
 l_R^g:=\|Q B_R^gP\|_2
 &\ll q_R\int|\widehat\phi(\xi)|\sqrt{W_L(\xi)}d\xi\\
 &\ll q_R\{\ell_0^{3/2}+\sqrt L
        \int |\xi|^{1/2}|\widehat\phi(\xi)|d\xi\}
 \ll q_R\sqrt L.                                        \tag{16}
 \end{aligned}
\]

最后的 weighted Fourier integral为O(1)，由原 `min(L,C/|xi|,C/xi²)`
在 0、1处分段可直接验证。最终 L充分大时 `ell_0^{3/2}<<sqrt L`。
这是真正原 physical P的 crossing estimate，未偷换为连续 invariant
frequency projection。sharp J不会妨碍证明，(13)只用了真实 global sup。

## 5. 三个内部 P 的两次 crossing 引理

令 V_i selfadjoint bounded，`y_i=||V_i||`，`l_i=||QV_iP||_2`。
每个 trace因P有限rank定义。准确 telescoping同物理13报告 (24)–(25)：

\[
 \begin{aligned}
 \Delta={}&\operatorname{Tr}(PV_1QV_2V_3V_4P)\\
 &+\operatorname{Tr}(PV_1PV_2QV_3V_4P)\\
 &+\operatorname{Tr}(PV_1PV_2PV_3QV_4P).
 \end{aligned}                                           \tag{17}
\]

由 `||[P,V_i]||_2=sqrt2 l_i`，以及 product commutator expansion，

\[
 \|Q V_{i_1}\cdots V_{i_r}P\|_2
 \le\sqrt2\sum_j l_{i_j}\prod_{k\ne j}y_{i_k}.            \tag{18}
\]

第一项配 `l_1` 与右 triple的 (18)；第二项左cross为
`||Q V_2P V_1P||_2<=l_2y_1`，右为 (18)的二因子；第三项两边为
`l_3y_2y_1` 与 l_4。HS–HS于是给

\[
 |\Delta|\ll\sum_{1\le i<j\le4}l_i l_j
                       \prod_{k\ne i,j}y_k.              \tag{19}
\]

该 bound含**两次** crossing。只以一个 crossing乘剩余 physical op会
损失本次节省；也不能对 original B直接在整个实线声称 canonical op。

对 V_i=B_R^g，用 (5)、(16)，one H、three L任何placement都有

\[
 |\Delta|\ll L q_Hq_L^3,\qquad
 d^{-1}|\Delta|\ll X^{(5/2)a-9/4}L^4.                    \tag{20}
\]

取 a=89/100得 `O(X^{-1/40}L⁴)=o(1)`。无需 [P,V] operator norm
小量、commutativity、Chern类或 unknown full prime四范数。

## 6. 回到原 actual13 及剩余主预算

[物理13推导](hybrid-signed-one-three-physical-resonance-research.md) 的
四 placement原 traces各自 o(d)。由 (12)，good physical四词各自亦o(d)。
由 (17)–(20)，每个good physical词与其 **actual finite** compressed词
相差o(d)。再由 (8)，回到原未截频的 C_H、C_L也仅相差o(d)。
故 (1) 成立；有限矩阵中四 placements循环相等，其整个13 coefficient
`4Tr C_HC_L³=o(d)`。保持 d/N(T,2T)→1时，同为o(N)。

该结论需要物理报告与本次三个新 bridges共同通过独审；不能以本报告
反过来省略物理 near/alias/long triple的付款。具体误差可合并为

\[
 d^{-1}|\operatorname{Tr}(C_HC_L^3)|
 \ll \ell_0^4/L+L^{-2}+X^{-1/40}L^C
                  +X^{-1/4}L^{-9/2}+X^{-3/4}L^C=o(1).    \tag{21}
\]

所有profiles与 fixed a先固定，再令 T趋∞；无 moving gap、目标后选择
window或反向填prime coefficients。引用范围 [R]是446同一zero-free/
logarithmic-control，而非整个外部原稿已由本研究认证。

31换成three H + one L时，(20)变成
`X^{(7/2)a-11/4}polylog`，在此输入下仍为正幂；且其 physical near
产品可长至XZ。这两项不能把13的 proof自动搬过去。
原 distinct22、31及 high all-distinct signed余额仍未闭合。本次无需
也没有相加 high repeated、low scalar主常数、proper powers或padding
形成完整四迹常数。没有新临界线比例、无零界或 RH claim。

# 原四高素数：至少一个较小标签的完整混合族付款

2026-10-08，作者 high_product_joint；本轮基线 b763892。仅新增本源，待不同作者全文审查。
结论是同一原参数下完整四全异族 min(p₁,p₂,p₃,p₄)≤X^u 的 signed χ-平均与完整主频带付款；
不是最大标签前缀、任意 minor 子掩码、固定 ordered box 或全局四矩的新幂。

## 1. 原对象、条件与冻结输入

保留 X=T/(2π)、L=log X、d=floor(XL)、η=2π/L、s_T=T/√L，
原 even C² 零延拓 φ、a_L=L^−1||φ||₂²≥c_φ、N_L=a_LL、b_p=log p/(N_L√p)。
原 E_σe_k=L^−1/2 1_I exp(i(σ+kη)w)，I=[−L/2,L/2]、P_σ=E_σE_σ*、Q_σ=1−P_σ；
σ=T+s_Tv，χ≥0、∫χ=1、supp χ⊂[3/8,5/8]，同一 χ、φ、共同空间 w 与原 floors 全保留。
唯一条件为普通 [R_7/8]：非平凡 ζ 零点 β≤7/8；不加入 Dirichlet/Hecke 前件。
固定 17/20≤u≤1、Z=X^u、Y=√X；标签始终是真实素数 Y<p≤X。
令 B_p=−b_pM_φ(R_log p+R_−log p)M_φ，B_R=Σ_(p∈R)B_p、C_R=E_σ*B_RE_σ、τ=Tr/d；
H=(Y,X]、<=(Y,Z]、>=(Z,X] 是这些真实 prime 集，C_H=C_<+C_>，不改有限空间或平滑切口。

| 已全文读取的输入及范围 | canonical LF SHA256 |
|---|---|
| [短上端175行](hybrid-original-prime-cutoff-fourth-and-max-label-research-perron.md)：原 cutoff 的 scalar/finite 四矩 | d7aaee914be30cfee19b4aa62b3efcb36adaa0f058155cc05d2e82e1c8740062 |
| [370行](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md)：两乘子、shared w、终端空间与二矩运输 | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [184行](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md)：普通条件 whole 5/7 | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [276行](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md)：closed two-cross 与反线性 half factor | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [456重复图](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md)：有限 partition、单 prime leakage、正 graph | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [545行](hybrid-whole-fourth-double-nonunit-actual-research-whole.md)：真实 completion、H_n 与零频完整付款 | 2d27661262a1e672a9bb93846de68a661e0d17d8f5e0444117ae6a8debac4215 |
| [425行](hybrid-whole-fourth-unit-unit-actual-research-whole.md)：ν 主带、全 chirp、carry/graph/边界 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |

## 2. χ × finite Schatten 四阶：先付完整 tail，再展开15词

在同一个 normalized Schatten4 与 χ 概率空间定义
\[
 \mathcal N_R=\left(\int\chi(v)\,\tau|C_R|^4\,dv\right)^{1/4}.
 \tag{1}
\]
短上端来源给 B(u)=3u/2−11/14、N_<⁴≪X^(B(u)+ε)；370与184给 N_H⁴≪X^(5/7+ε)。
Minkowski 在这个直接积 L4 空间给 N_>≤N_H+N_<≪X^(5/28+ε)，因为 B(u)≤5/7。
这是对完整 C_> 的合法范数付款；不对子 mask 从 full signed trace 删除系数。
非交换展开 C_H⁴−C_>⁴ 恰有15个 {<,>} 四词。对有 k≥1 个 < 的每个词，
pointwise finite Schatten Hölder 后作 χ-Hölder，得
\[
 \int\chi(v)|\tau(C_{R_1}C_{R_2}C_{R_3}C_{R_4})|dv
 \le\prod_i\mathcal N_{R_i}
 \ll X^{[kB(u)+(4-k)5/7]/4+\varepsilon}.
 \tag{2}
\]
最坏 k=1，因此15个 grouped traces 的 absolute 平均之和至多
\[
 X^{E(u)+\varepsilon},\qquad
 E(u)=\frac{B(u)+15/7}{4}=\frac57-\frac{3(1-u)}8.
 \tag{3}
\]
这不控制每个 prime tuple 的 absolute 和。u=9/10 时 E=379/560；最小 u=17/20 时 E=737/1120>1/2。

## 3. 重复标签须完整相减；finite 与 physical 各自直接付款

对 R=H 或 >，记 S₂,R=Σ_Rb_p²=O(1)。Σ_RC_p²≤S₂,RI。
原 weighted MV 对任意 shift、同一原系数子集给 M₂(P_R;J)≪Σb_p²+T^−1Σp b_p²=O(1)；
370的原 one-leg L2 contraction/χ-overlap 给 ∫χτC_R²=O(1)。没有借用未知四矩常数。
沿用456(20)的未归一化有限 trace partition：
\[
 S_{\rm rep,R}=4T_0+2T_{\rm opp}-2T_{22}-T_\times-8T_3+6T_4.
 \tag{4}
\]
直接有 T₀/d≤S₂,RτC_R²、|T_opp|/d≤同一界；
后者逐项用 |Tr((C_pC_R)²)|≤Tr(C_p²C_R²)，不是 scalar trace square。
同理 T₂₂/d、|T_×|/d≤S₂,R²；|T₃|/d≤(Σb_p³)(τC_R²)^1/2、T₄/d≤Σb_p⁴。
χ-Cauchy后，∫χ|S_rep,R|/d=O(1)。所以 mixed repeated 精确等于 S_rep,H−S_rep,>，也付 O(1)。
此差包括任何位置有 small 标签的所有 repeated tuples，不只“被重复的标签较小”。

为运输到 physical，不能使用 free cyclic trace。记
l_R=||Q_σB_RE_σ||_HS、m_R=||B_R||_op、Φ_σ(W)=d^−1Tr(E_σ*WE_σ)。
原 C² Fourier outside 权 W_L(ξ)≪log(2+L)+L|ξ| 及 shifted MV 直接给
\[
 \int\chi l_R^2\ll L+X/s_T=O(L),\quad m_R\ll\sqrt X/L,\quad
 l_p\ll b_p\sqrt{\ell_0},\qquad \ell_0=\log(2+L).
 \tag{5}
\]
对任意 selfadjoint 四腿，展开三个内部 I=P_σ+Q_σ；七个非全P路径皆闭合且至少两次穿过P/Q。
两个 crossings 用 HS，其余腿用 operator norm，得
\[
 |\Phi_\sigma(B_1B_2B_3B_4)-\tau(C_1C_2C_3C_4)|
 \le\frac C d\sum_{i<j}l_i l_j\prod_{k\ne i,j}m_k.
 \tag{6}
\]
对15个整 color words，χ-Cauchy与(5)给总误差 O(m_H²L/d)=O(L^−2)。
重复族按 finite set partitions 展成有限种 ordered patterns，再逐 pattern 使用(6)。
一对 repeated p、两条 B_R 腿的每种位置顺序，聚合误差至多
d^−1[ m_R²Σl_p²+m_Rl_RΣb_pl_p+l_R²Σb_p² ]；
两对、三重、四重 patterns 分别以 Σb_p²、Σb_p³、Σb_p⁴ 付款，大小不超过同一 χ-平均界
\[
 \frac C d\left(m_H^2\ell_0+m_H\sqrt{L\ell_0}+L\right)=o(1).
 \tag{7}
\]
这里各 cyclic orientation 先单独运输，只有 finite trace 内才用(4)；不在 physical state 中循环换词。
所以两个完整 physical repeated 族也各为 O(1)。从15词分别减去完整 mixed repeated 得
\[
 |\mathcal D_{\rm mix}^{\rm act}|+|\mathcal D_{\rm mix}^{\rm phy}|
 \ll X^{E(u)+\varepsilon}.
 \tag{8}
\]
两项均指原 χ-平均的完整 four-distinct union，mask 为 min(labels)≤Z。

## 4. 原共同 profile、half factor 与 hard-near

原两真实乘子、两个 C² tails、J_0/J_1/J guards、χ-overlap 和终端空间均在上述准入中保留；
没有为不同 colors 重选 w、ν、height 或有限 P。令 A_R 为原 positive translation 腿，则 A_R²=0。
原 K=complex-conjugation × reflection 固定每个 E_σe_k，并将 A_R 变成 A_R*。
真实 <、> 切口的系数仍为实数；min(labels)≤Z 在此 reflection 下不变。
故完整 four-distinct physical mixed union 的两个 alternating half-block 准确配对：
H_mix,near=D_mix,near^phy/2。这只是固定 factor2，不把 mixed 差认成正方差或单词恒等式。
原 Ψ(S)=e^(iTS)Γ(s_TS)K_d⁰(S)，Δ=1024L^(5/2)/X。
原 |S|≥Δ 时 |Ψ|≤X^−4，整个四权正质量 (Σ_Hb_p)⁴≪X²/L⁴；
mask≤1，故 full mixed physical far 直接付 O(X^−2L^C)。actual 先用(6)整词桥，不逐 tuple 删除P。
因此(8)与 half factor 支付原 ν/Δ 下完整 H_mix,near，不改 canonical scalar 观察窗。

## 5. 三矩形直接重估 double-nn；不能从 signed full_nn 截取

按545真实最大素数 q、另一分子 s<q、分母 p,r<q 分解，所有四种最大位置照原式恢复。
q≤Z 或 s≤Z 时 mixed mask 为1；q,s>Z 时，真实 mask 恰为
\[
 1_{p\le Z}+1_{r\le Z}-1_{p\le Z}1_{r\le Z}.              \tag{9}
\]
至多三个 signed bilinear rectangles，只改545(4)–(5)的实际 prime coefficients；
仍有 p,r≠s、同一个 w、sharp q-prefix、原 graph p≠r、A=qs、a=qs−h 与 gate 1≤a<q²。
在每个 rectangle，||A||₂、||B||₂≪1，||A||₁、||B||₁≪√q/L。
准确 Z_nn=q^−2Σ_(n mod q)H_nB_n 中，H_n 只依 W_A(a)，不依 p/r cut；
rectangle 只改 B_n。非零 n 的 restricted Fourier matrix 仍给 |B_n|≤√q||A||₂||B||₂；
Σ|H_n|≪qsΔ+1+qlogq≪qL^(5/2)。外权直接按完整 q≤X 聚合：
\[
 \sum_q\frac{b_q}{\sqrt q}\sum_{Y<s<q}b_s\ll\sqrt X/L^2,
 \quad |\mathcal D_{\rm nn,mix}^{\ne0}|\ll X^{1/2}L^{1/2}.
 \tag{10}
\]
零频的 A≤4X、q−s≤4qΔ 是原正计数费用，rectangle 只减绝对 coefficient；
内区 A>4X、q−s>4qΔ 的 H₀≪X^−3L^C 原 Γ Taylor全0与高阶EM proof原样有效。
尤其不能将 p/r 的下端 Z 放进 H_n：它在辅助整数 a 上的原支撑不变，阈值仍4X，不产生4Z²。
|B₀|的原 L1 粗界仍足够。hard/smooth、q² aliases 与 diagonal roots≤2 的正 graph 修正照545直接求和。
所以全部 s 排除、所有位置与 graph 扣除后 |D_nn,mix|≪X^(1/2+ε)。
原 exact completion 线性且保留(9)，给 H_mix,near=U_mix+D_nn,mix；
由 E(u)>1/2 得 |U_mix|≪X^(E(u)+ε)。这是完整 union 相减，不是 arbitrary frequency mask 的范数估计。

## 6. 完整实际主频带与尚未消费的 minor

对425每个 rectangle，原宽near、A≤4X与q−s≤4qδ两边界、aliases及 graph 都由正包络重新付款；
interior 的有限 log-Taylor 全项与原 ν 导数界不变，restricted prime rows/columns 的 TT* norm不增。
ν correction幅 X^−2L^12、(A/q²)|I_(q,s)|≪X，以及完整外权
Σ_qb_qΣ_(s<q)b_s√(qX/s)≪X^(3/2)L^C，直接给整个 mixed chirp O(X^1/2L^C)。
故425(36)加入准确 min(labels)≤Z 后的完整主频带 L_T,mix 满足
\[
 U_{\rm mix}=\mathfrak L_{T,\rm mix}+O(X^{1/2}L^C)+O(X^\varepsilon),
 \qquad |\mathfrak L_{T,\rm mix}|\ll X^{E(u)+\varepsilon}.
 \tag{11}
\]
原 prefactor (2πs/q)ν(2πsn/q)、n∈I_(q,s)、q∤n、e_q(ns)e_q²(−npr)、
所有 shared profiles、s/p/r排除、q² carry 与 floors 仍准确。没有新 smooth prime approximation。
u=.9 得379/560，低于5/7；支付的是完整至少一较小 high label 族，允许另三标签到X。
在上述 complete union 或 complete mainband 中精确减它，剩余为四个 genuine primes 都>X^.9。
本源不支付该 mixed 族的 minor、major、cap外或固定 box；各 signed 子 mask 仍须各自 exact桥和直接费用。
u=1回到既有5/7；所有标签>Z的完整剩余尚未省幂，global whole四矩、中心常数、比例与无零区域均未改善。
无需有限采样或新计算证书：新付款由(1)–(11)与这些冻结输入的解析证明和不同作者审查认证。

# 原短载波窗口的完整比值方差与四全异相消：同一 good set

2026-10-08，twisted_research。起点只读核到main
`2d5621dbc999e0cf313ea224b825d6d56547c45c`，工作区干净。
只新增本稿，不改冻结材料、math、论文、脚本、输出或Git。
状态：完整新联合推导，待其他作者全文审查。

短carrier二矩/P桥由radial_review提出。本稿的新增部分是：在同一
原scalar系统与自然短窗口上，把实际q和整个四全异D双向等同一个
明确的half-ratio正方差，并把全部16种H/L四词放到同一个good set。
下面核对桥所需的量词和uniform加权中心化，不将桥冒充本人新输入。
尚未证明这个完整方差的有用算术上界；没有新比例或新无零区域。

## 1. 原载波只作短平移，系数和窗口共同冻结

取X=T/(2π)、ell=log X、d=floor(X ell)，原even C² taperφ及
a_ell=||φ||₂²/ell。令h=T/√ell，σ∈J_T=[T,T+h]，并记

\[
 E_\sigma e_k=\ell^{-1/2}1_I e^{i(\sigma+2\pi k/\ell)u},
 \quad I=[-\ell/2,\ell/2],\quad P_\sigma=E_\sigma E_\sigma^*,
 \quad Q_\sigma=1-P_\sigma .
\tag{1}
\]

尖锐prime cutoff X、high sqrt X<p≤X、low p≤sqrt X、b_p=
(log p)/(a_ell ell sqrt p)与φ在整个σ窗口共同冻结。
它不是先对不同σ重选一套profile或独立素数行；原zero extension保留。
写B_H、B_L为原physical算子，H_σ=E_σ*B_HE_σ、
L_σ=E_σ*B_LE_σ，τ=Tr/d。尖括号指J_T上normalized Lebesgue均值。

冻结输入：

| 输入 | canonical UTF-8 LF SHA-256 |
|---|---|
| [新anchored raw carrier/P平均桥](hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md) | c0e874ab9061982c8ef4365c8e9313eeac77eeddb756dc0b455cab3349f99dd8 |
| [真实finite band / closed two-cross](../2026-10-07/hybrid-one-three-finite-band-admission-research.md) | bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f |
| [high半区间Gram](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [465实际加权中心化](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [456完整重复union](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [471四全异目标](../../notes/471-original-principal-subtraction-and-signed-four-distinct-target.md) | a66dcc18606b59ac0aa1a879f64f6f7dae4a3278981e5fbc2c94190efa3a3ef6 |

以下新增桥与有限代数不需要[R]，也不假设high fourth或q bounded。
把选择的载波用于原零侧账本时仍须保留原228的同配置合同；本稿不
重证该零侧输入，尤其不把long carrier mean替代它的自然height窗口。

## 2. 短窗口P桥的共同均值与全部16词

令l_R(σ)=||Q_σ B_R E_σ||HS，m_R=||B_R||op；raw界为
m_H≪√X/ell、m_L≪X^(1/4)/ell。原Fourier entry公式及outside
count min(d,|n|)的权重W_ell(ξ)满足

\[
 W_\ell(\xi)\ll\log(2+\ell)+\ell|\xi|.
\tag{2}
\]

连续scalar MV对任意共同shift α给

\[
 \frac1h\int_T^{T+h}|D_R(\sigma+\alpha)|^2d\sigma
 \ll \sum_{p\in R}b_p^2+\frac1h\sum_{p\in R}p b_p^2
 \ll1+\frac{Y_R}{h\ell},\quad Y_H=X,\ Y_L=\sqrt X .
\tag{3}
\]

正负log p frequencies一同包含；其local real gap≥c/p。
shift只改变系数的unit-modulus相位，MV常数不依赖α。
这里是[Montgomery–Vaughan原文Theorem 2、Corollaries 2–3]
(https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的weighted mean value，已核原文；有限Dirichlet和不含height尾缺口。
Σp p b_p²≪Y_R/ell由Chebyshev给，不能粗换成Y_R再丢ell。

在共同L²(σ;outside matrix entries)空间用Minkowski，再用(2)、
原φhat的C² L¹及√|ξ|加权L¹界，得到

\[
 \langle l_R^2\rangle\ll
 \left(1+\frac{Y_R}{h\ell}\right)
 \left(\int|\widehat\phi(\xi)|\sqrt{W_\ell(\xi)}d\xi\right)^2
 \ll\ell+Y_R/h=O(\ell).
\tag{4}
\]

没有先令P与global Fourier guard交换；outside entry仍是原I的
完整Fourier基。σ、k与ξ的所有shift共用(3)，故不需要逐行重选prime
系数，也不依赖[R]提供good-height sup。

对w=(R₁,R₂,R₃,R₄)∈{H,L}⁴定义准确closed-word差

\[
 \epsilon_w(\sigma)=d^{-1}\operatorname{Tr}
 (E_\sigma^*B_{R_1}B_{R_2}B_{R_3}B_{R_4}E_\sigma)
 -\tau(C_{R_1,\sigma}C_{R_2,\sigma}
             C_{R_3,\sigma}C_{R_4,\sigma}).
\tag{5}
\]

原two-cross lemma给|ε_w|≤C/d Σ_{i<j} l_i l_j Π_{k≠i,j}m_k。
共同σ上的Cauchy与(4)合法，不假装不同prime列独立。因此

\[
 \left\langle\sum_{w\in\{H,L\}^4}|\epsilon_w|\right\rangle
 \ll \frac{m_H^2\ell}{d}=O(\ell^{-2})=:e_T.
\tag{6}
\]

这一full-height桥含原raw算子，无额外bad-height费用待付。
它是窗口均值，不是原σ=T处的pointwise equality。
Markov给共同集合G_T⊂J_T，relative measure≥1−η_T，η_T≪√e_T，
且在G_T上每个16词均有|ε_w|≤√e_T。零个或两个high因子的
词没有另选集合，complex trace也按absolute error同时控制。

## 3. 465中心化对同一窗口uniform，不索取q bounded

原physical high same-prime diagonal写w_T(u)，W_σ=E_σ*M_wTE_σ。
因为乘法M_wT与carrier modulation交换，W_σ的有限矩阵本身不依赖σ。
令S_T=ell^−1∫w_T²，则

\[
 \tau W_\sigma^2=S_T-\|Q_\sigma M_{w_T}E_\sigma\|_{\rm HS}^2/d,
 \qquad S_T\longrightarrow S_\psi .
\tag{7}
\]

该乘法leakage同样不依赖base carrier。465的weighted HH二矩
比较费用是O(m_H² log(2+ell))/d=o(1)，raw bounds对σ uniform。
其physical不同prime差频主项用Hilbert；base σ只是prime-only的
unitary相位，numerator两端也可同样吸收。和频/±ell alias remainder
用absolute正质量及共同overlap，亦不依赖σ。因此准确有

\[
 \sup_{\sigma\in J_T}|\tau(W_\sigma H_\sigma^2)-S_T|=o(1),
 \qquad
 q_\sigma:=\tau(H_\sigma^2-W_\sigma)^2
 =\tau H_\sigma^4-S_T+o(1),
\tag{8}
\]

第二个o(1)uniform且不乘a_σ或q_σ。不需要未知fourth bounded。
465的WL²、WHL与其其余static weight同理；本稿只用HH项。

456的repeated-label删除helper按平方权重Σb_p²付款，carrier只给
unitary phase；physical Topp的near/far估计用|K_d|及overlap。
所以其完整repeated union=2S_ψ+o(1)也uniform于这个短窗口。
若D_σ为原actual四全异完整signed union，准确有

\[
 D_\sigma=\tau H_\sigma^4-2S_\psi+o(1),\qquad
 q_\sigma=S_\psi+D_\sigma+o(1).
\tag{9}
\]

这个D没有删prime标签、near/far或internal P；其定义与471相同，
只是保持共同系数而允许短base carrier shift。

## 4. Half-ratio的factor2：原正频载波被反线性对称固定

定义physical正平移块

\[
 A=-\sum_{\sqrt X<p\le X}b_pM_\phi R_{\log p}M_\phi,
 \quad B_H=A+A^*,\quad G=A^*A,
 \quad D_+=\sum_p A_p^*A_p=M_{d_+},\quad R_+=G-D_+.
\tag{10}
\]

A=Π_-AΠ_+，故A²=(A*)²=0。G、D_+、R_+只作用在I_+。
本稿的R_+始终是这个half-ratio算子，不是full B_H²−M_wT。

令Jf(u)=f(−u)，C为复共轭，K=CJ。原窗偶且coefficients实，
所以K A K=A*。而K(E_σe_k)=E_σe_k准确成立：反射独自把正
载波变负，复共轭再恢复；不能只声称J保持原carrier。
因此两个physical block的HS norm相等，且outputs正交：

\[
 \frac1d\operatorname{Tr}(E_\sigma^* B_H^4E_\sigma)
 =\frac2d\|G E_\sigma\|_{\rm HS}^2.
\tag{11}
\]

展开G=D_++R_+。原highGram已付的D_+R_+ cross为O(1/ell)，
其Hilbert proof同§3对σ uniform。两个D_+的反射半块给w_T，
且两半支撑不交，所以2||D_+E_σ||²/d=S_T。令

\[
 r_\sigma=\frac1d\|R_+E_\sigma\|_{\rm HS}^2\ge0,
 \qquad
 \frac1d\operatorname{Tr}(E_\sigma^* B_H^4E_\sigma)
 =S_T+2r_\sigma+O(\ell^{-1}).
\tag{12}
\]

Full ratio R_full=R_++K R_+K=B_H²−M_wT满足
||R_full E_σ||²=2||R_+E_σ||²。factor2没有来自free cyclic
physical trace，亦没有把E_σ换成full Hilbert identity。

## 5. 完整双向预算与可合法选择的同一载波

从(6)、(8)、(9)、(12)得到whole L¹等价

\[
 \langle|q_\sigma-2r_\sigma|\rangle=o(1),\qquad
 \langle|D_\sigma-(2r_\sigma-S_\psi)|\rangle=o(1).
\tag{13}
\]

o(1)不要求r、q或fourth有界。更准确地，pointwise只有ε_HHHH
与uniform o(1)；其可能增长值不能被当成pointwise small。
在§2同一G_T上则两个差皆o(1)，且全部16词同时可比较。

若今后真的付款⟨r_σ⟩≤B_T，r≥0给

\[
 \inf_{\sigma\in G_T}r_\sigma\le\frac{B_T}{1-\eta_T},
 \quad \exists\sigma_T\in G_T:\quad
 q_{\sigma_T}\le\frac{2B_T}{1-\eta_T}+o(1),\quad
 D_{\sigma_T}\le\frac{2B_T}{1-\eta_T}-S_\psi+o(1).
\tag{14}
\]

若inf未取到，先容许任意ε_T→0再选择点；这不改变显示o(1)。
全部word和uniform weighted centering沿此同一σ_T保持。
当B_T=O(1)才可把1/(1−η_T)的费用吸收成additive o(1)；
若B_T增长，必须保留(14)原式。本稿未提出任何未付款数值Q或B。

重要区分：旧scalar compression Jensen本来已给pointwise
τH_σ4≤Tr(E_σ*B_H4E_σ)/d，故q_σ≤2r_σ+o(1)。
因此单独r upper向q upper的one-sided转移不是本轮新突破。
新桥的增益是(13)双向且growth-uniform的整个D/q等价，以及
(14)中同一good set上的16个mixed words同时可传递，消除了此前
不能免费删除的whole fourth compression correction。
仍须真正证明自然短窗的完整r upper；没有以(14)代替它。

## 6. 实际待付列与long carrier mean为何不够

R_+原column的准确标量表达是

\[
 r_\sigma=\frac1\ell\int_{I_+}\phi(u)^2\frac1d\sum_{k=0}^{d-1}
 \left|\sum_{p\ne q}b_pb_q\phi(u-\log p)^2
 \phi(u+\log(q/p))e^{i(\sigma+2\pi k/\ell)\log(q/p)}\right|^2du.
\tag{15}
\]

这个square仍有全部四prime labels和同一个u-window。prime ratio
p/q是primitive且唯一，但分母可到X，局部log-ratio spacing仅能
按X^−2付款；square里的两侧prime products仍可∼X²。
外σ与k总采样height尺度O(X)，没有获得length X²的免费MV。
用positive sum替signed square或逐moving ratio设新角色family，
都不是(15)的原对象准入。

还可精确审计long carrier平均。固定X、d、φ与所有coefficients，
E_σ* MφR_{±log p}Mφ E_σ=e^{±iσlog p} times一个固定有限矩阵。
故完整D_σ为有限指数和。四distinct标签没有零频率，因为唯一
分解禁止∏p_i^{ε_i}=1。2+/2−的最小可能非零|S|只保证≥X^−2；
3+/1−与4same signs的gap更大，不能改善2+/2−这个长列。

取w_A(t)=(2πA)^−1[sinc(t/(2A))]²，其中sinc x=sin x/x，
其Fourier特征函数是(1−A|S|)_+。因此A≥X²时

\[
 \int_{\mathbb R}D_{\sigma_0+t}w_A(t)dt=0
\tag{16}
\]

准确消去整个finite D，包含所有P、signs和alias，未取absolute。
但这是固定prime cutoff下宽度X²的全height平均，不能替换
σ∈[T,T+T/√ell]的原零侧配置。自然width h对|S|≲1/X的真实
near项只给1−O(1/√ell)，没有将其消掉。所需determinant宽度仍
可达X²/h∼X√ell；long mean0不证明自然窗口的r≤有限目标。

本轮得到的是原全量算术upper的准确可转移判据及其真实长度，
不是新的O(d)四矩。下一步须对(15)保留共同相位证明short-window
净upper，或支付其equivalent四全异D的负相消；旧静态Gram与
long carrier orthogonality不足以完成这一付款。

# 465：高素数平方残差对整个混合四矩的联合预算

2026-10-07。原 finite 矩阵上的证明及条件性比例接口。
新增进展是把 whole high4、entire31 和 entire22 联合约束为同一个
非负平方残差，而不是分别为它们索取不相关的上界。
没有得到新的实际零点比例或无零边界。下述联合预算是有效接口；
其 flat 小残差示例随后被原空间交换子的正下界排除，见
[466](466-high-square-variance-commutator-obstruction.md)。

## 1. 原对象、已付输入与明确前件

保留 [461](461-original-one-high-three-low-fourth-trace.md) 的
原 \(X=T/(2\pi)\)、\(\mathcal L=\log X\)、\(d=\lfloor X\mathcal L\rfloor\)、
interval carrier \(E\)、\(P=EE^*\)、\(Q=1-P\)、even taper \(\phi\)、
\(a_{\mathcal L}=\|\phi\|_2^2/\mathcal L\) 与实际高度
\(\tau_k=T+2\pi k/\mathcal L\)。设
\[
 b_p=\frac{\log p}{a_{\mathcal L}\mathcal L\sqrt p},\quad
 B_R=-\sum_{p\in R}b_pM_\phi(R_{\log p}+R_{-\log p})M_\phi,
 \quad H=E^*B_HE,\quad L=E^*B_LE,
\]
其中 high 为 \(\sqrt X<p\le X\)，low 为 \(p\le\sqrt X\)。
所有平移仍在实线上零延拓，所有有限内部投影保留。

使用以下已明确的输入：

- [454](454-original-background-and-weighted-prime-mixed-traces.md)：
  原全部 log range 的加权二矩、alias 与投影泄漏，Gamma/pole 背景；
- [462](462-original-low-prime-fourth-path-constant.md)：
  \(e_T=d^{-1}\operatorname{Tr}L^4\to e_\psi>0\)，flat 时 \(e_1=19/240\)；
- 461：\(\eta_T=d^{-1}\operatorname{Tr}(HL^3)=o(1)\)，使用其明列
  fixed-gap \(\theta<9/10\) 的 [R]；原 \(7/8\) 输入足够；
- [455](455-whole-proper-power-fourth-norm-and-prime-equivalence.md)、
  [452](452-subquarter-padding-and-fourth-trace-stability.md)：
  proper powers 与零侧 padding 的原 Schatten 稳定性；
- [197](197-partial-weil-proportions-regions-four-moments.md)、
  [228](228-relative-dense-zero-block-transfer.md)：
  同配置的一侧中心四矩到 simple-critical-line 比例接口。

除 \(\eta_T=o(1)\) 外，下面的加权二矩及 finite 代数无需新无零输入。
本稿不把另一数域角色、大筛或独立标量四矩当作原对象。

## 2. 原高素数对角与三个实际加权二矩

定义 bounded multiplication
\[
 w_{\mathcal L}(u)=\phi(u)^2
 \sum_{\sqrt X<p\le X}b_p^2
 [\phi(u+\log p)^2+\phi(u-\log p)^2],
 \qquad W=E^*M_{w_{\mathcal L}}E .
 \tag{1}
\]
令 \(\Psi\) 为 \(\psi\) 的零延拓，\(a=\int_{-1/2}^{1/2}\psi\)，并置
\[
 d_{R,\psi}(v)=\frac{\Psi(v)}{a^2}
 \int_{\mathcal I_R}x[\Psi(v+x)+\Psi(v-x)]\,dx,\quad
 \mathcal I_L=[0,1/2],\quad\mathcal I_H=[1/2,1].
 \tag{2}
\]
记
\[
 S_\psi=\int d_{H,\psi}^2,\qquad
 C_\psi=\int d_{H,\psi}d_{L,\psi}.
 \tag{3}
\]
所有积分在 \([-1/2,1/2]\)，两常数非负。

**加权二矩引理。** 在同一原 finite frame 上，
\[
 \frac{\operatorname{Tr}W^2}{d}\to S_\psi,\qquad
 \frac{\operatorname{Tr}(WH^2)}{d}\to S_\psi,\qquad
 s_T:=\frac{\operatorname{Tr}(WL^2)}d\to C_\psi,\qquad
 t_T:=\frac{\operatorname{Tr}(WHL)}d=o(1).
 \tag{4}
\]
没有以 \(H^4=O(d)\) 为前件。

证明需要保留权重与原投影。Mertens 给 \(\sum_Hb_p^2=O(1)\)，
所以 \(w_{\mathcal L}\) 的 sup 有界；乘法求导及原 taper 的统一
derivative bounds 给 \(\|w_{\mathcal L}'\|_1+
\|w_{\mathcal L}''\|_1=O(1)\)。两端值和导数均为零。
454 的圆周 Fourier 计算因而给
\[
 \ell_w:=\|QM_{w_{\mathcal L}}E\|_{\rm HS}
 \ll\sqrt{\log(2+\mathcal L)}.
 \tag{5}
\]
写 \(m_H\ll\sqrt X/\mathcal L,\ m_L\ll X^{1/4}/\mathcal L\) 为 raw op
上界，\(\ell_R=\|QB_RE\|_{\rm HS}\ll m_R\sqrt{\log(2+\mathcal L)}\)。
将 \(B_RE=EC_R+QB_RE\) 两侧展开，实际 middle-weight 二矩与物理
\(\operatorname{Tr}(E^*B_RM_wB_SE)\) 的差不超过
\[
 m_R\ell_w\ell_S+m_S\ell_w\ell_R+\|w\|_\infty\ell_R\ell_S.
 \tag{6}
\]
HH 时为 \(O(X\log(2+\mathcal L)/\mathcal L^2)=o(d)\)，
HL 与 LL 更小。有限循环迹合法，故
\(\operatorname{Tr}(WL^2)=\operatorname{Tr}(LWL)\)；
\(\operatorname{Tr}(WHL)\) 是 \(\operatorname{Tr}(HWL)\) 的共轭。

物理加权二矩使用454的全部差频 Hilbert主项、endpoint remainder
及和频 overlap-alias付款。其证明是 bilinear 的，亦可对
\(B_H+zB_L,\ z=1,i\) 极化；系数都来自同一窗口、sharp primes 和原高度。
不同 prime labels 的 cross 为 \(o(d)\)。因此 HL 没有同素数对角，
HH、LL 的对角分别是
\(d\langle w_{\mathcal L}^2\rangle\) 与
\(d\langle w_{\mathcal L}d_{L,\mathcal L}\rangle\)。
这里 \(d_{L,\mathcal L}\) 是(1)把 high 换成 low 的函数。
标准 partial summation 与 dominated convergence 给(2)–(4)。
最后
\(\operatorname{Tr}W^2=d\langle w_{\mathcal L}^2\rangle-\ell_w^2\)。
没有对带末端 \(P\) 的物理乘积作循环，也没有删除 nonseparable 窗口。

## 3. 同一个平方残差约束整个 31 与 22

取真实 selfadjoint residual
\[
 \Gamma=H^2-W,\qquad q_T=d^{-1}\|\Gamma\|_{\rm HS}^2\ge0,\qquad
 a_T=d^{-1}\operatorname{Tr}H^4.
 \tag{7}
\]
式(4)与精确平方展开立即给
\[
 a_T=S_\psi+q_T+o(1).
 \tag{8}
\]
这里使用 \(q_T\) 本身；不把可能略小于 \(S_\psi\) 的有限
\(a_T-S_\psi\) 未经处理放进根号。

设
\[
 c_T=d^{-1}\operatorname{Tr}H^2L^2=d^{-1}\|HL\|_{\rm HS}^2,\quad
 b_T=d^{-1}\operatorname{Tr}H^3L .
 \tag{9}
\]
准确地，
\[
 c_T=s_T+d^{-1}\operatorname{Tr}(\Gamma L^2)
 \le s_T+\sqrt{q_Te_T},
 \qquad
 |b_T|\le|t_T|+\sqrt{q_Tc_T}.
 \tag{10}
\]
第二式来自
\(b_T=t_T+d^{-1}\operatorname{Tr}(\Gamma HL)\)。
HS Cauchy 允许 \(HL\) 非 selfadjoint，且
\(\|HL\|_{\rm HS}^2=dc_T\)；此式覆盖整个原 31，而非某个 signed 子词。

设 \(r_T=d^{-1}\operatorname{Tr}HLHL\)。HS Cauchy 给
\(|r_T|\le c_T\)，故完整 22 系数
\(4c_T+2r_T\le6c_T\)。finite cyclic expansion 是
\[
 F_T:=d^{-1}\operatorname{Tr}(H+L)^4
 =a_T+e_T+4b_T+4\eta_T+4c_T+2r_T.
 \tag{11}
\]
于是对每个有限 \(T\)，令 \(u_T=s_T+\sqrt{q_Te_T}\ge0\)，严格有
\[
 F_T\le a_T+e_T+6u_T+4\sqrt{q_Tu_T}
             +4|t_T|+4|\eta_T|.
 \tag{12}
\]
此有限式无需先假定 \(q_T\) 有界。

**条件性 whole-prime 上界。** 若另行证明
\(\limsup q_T\le Q<\infty\)，则由连续性与单调性，
\[
 \boxed{\limsup F_T\le \mathcal B_\psi(Q)}
 \]
\[
 \mathcal B_\psi(Q)=S_\psi+Q+e_\psi+
 6(C_\psi+\sqrt{Qe_\psi})+
 4\sqrt{Q(C_\psi+\sqrt{Qe_\psi})}.
 \tag{13}
\]
这是一个具体的新联合预算。small \(q_T\) 同时支付 high4、
entire31 及 entire22，不需要独立先证这两个混合量很小。
现有 [R] 尚未给出这个 \(Q\)；尤其不把 high repeated 常数冒充 \(a_T\)。

## 4. Flat 同窗口的反事实算术门槛

仅本节取 \(\psi=1\)，保留原 endpoint taper。置 \(t=|v|\)。
公式(2)准确给
\[
 d_H(v)=t(t+1)/2,\qquad d_L(v)=1/4-t/2+t^2/2 .
 \tag{14}
\]
因此
\[
 S_1=19/480,\quad C_1=23/960,\quad e_1=19/240,\quad
 \mathcal B_1(0)=S_1+e_1+6C_1=21/80.
 \tag{15}
\]
这些都在同一 flat 窗下，未混入 MT 的二矩或 Gamma 常数。

完整实际 response 的 centered channel 为原背景 \(A\) 加全部
\(\Lambda\) channel。由(13)有界、455的proper-power小 \(S_4\)，
全部 \(\Lambda\) fourth 有界。454在 flat 时给 \(V=Z=J=0\)，
其实际背景 cubic Cauchy界也趋零；故
\[
 \limsup d^{-1}\operatorname{Tr}(G-I)^4\le\mathcal B_1(Q).
 \tag{16}
\]
这一步在得到 bounded whole-prime fourth 后才使用；
没有在未知增长的 cubic 上免费乘一个 \(O(1/\mathcal L)\) 背景误差。
452支付同对象的零侧padding，且 \(d/N(T,2T)\to1\)；
因此(16)可以接原 partial-Weil 账本。

仅从(13)看，一个不用数值寻优的充分前件是
\[
 \boxed{\limsup q_T\le1/1600.}
 \tag{17}
\]
但466证明原 flat 矩阵不可能满足它。下面保留此反事实计算，
用于区分预算公式的有效性与其前件的可达到性。取 \(Q=1/1600\)：
\[
 \sqrt{Qe_1}<17/2400,\qquad
 C_1+17/2400=149/4800,\qquad
 4\sqrt{Q(149/4800)}<9/500.
 \tag{18}
\]
两项严格根号上界分别可平方，用有理数直接验证。于是
\[
 \mathcal B_1(Q)<21/80+1/1600+6(17/2400)+9/500
 =2589/8000<1/3.
 \tag{19}
\]
在197/228的完整有限误差及全局前件下，flat中心二矩 \(v=1/3\)，
一侧上界 \(B=2589/8000\) 给条件性比例
\[
 \liminf\frac{s(T)}{N(T)}
 \ge\frac{(1-v)^2}{1-2v+B}
 =\frac{32000}{47301}>\frac{27}{40}=0.675.
 \tag{20}
\]
辅助 LP 参数 \((v-B)/(1-v)\) 为正且小于 \(3/4\)，分母为正；
适用一侧四矩接口，不要求先另证三阶矩极限。
若极端的 \(Q=0\) 前件成立，则(15)对应条件性 \(320/429\)。
这些是已被原结构排除的前件下的蕴含，不能作为实际比例成果
或后续算术付款目标。

## 5. 已确认的阻断与下一接口

若只使用本稿粗联合预算，曾会提出如下原算术前件：
\[
 \limsup_{T\to\infty}
 \frac{\|(E^*B_HE)^2-E^*M_{w_{\mathcal L}}E\|_{\rm HS}^2}{d}
 \le1/1600 .
 \tag{21}
\]
现在原空间交换子已经严格给出
\[
 \liminf q_T\ge33479/15482880>1/1600.
 \tag{22}
\]
因此(21)不再是可追求的目标。466还给有理验证：
在此下界处，\(\mathcal B_1(Q)>1/3\)；本稿单独的
monotone scalar budget 不能认证超过 flat 二矩比例。
该结论只排除本预算，不排除原路线的更精确联合估计。

下一步需要保留 low 平方残差与 \(\Gamma\) 的协方差、
已付 entire13 对两残差的正交约束，以及 22 的负 commutator 项。
这些结构可以收紧(10)与 \(4c_T+2r_T\le6c_T\) 的独立 Cauchy 松弛。
实际 \(\Gamma\) 包括 projection leakage，仍不能以物理 ratio norm
或重复词替换。

已有 7/8/cubic-boundary 输入只给 canonical prime prefix的幂界，
不足以支付新的联合协方差上界。完整 ratio columns 的 signed cancellation和
同窗口内部有限投影，仍是结合无零区域与比例路线的关键算术工作。
本轮取得更具体的联合条件；现有实际比例与
原明列 [R] 下的 \(\sigma_*=0.874957019420098946\ldots\) 保持既定状态，
未确认新边界，不新增边界论文。

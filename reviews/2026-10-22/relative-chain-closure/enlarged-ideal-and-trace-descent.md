# 实际加权边界理想：代数闭链、旧 HH₁ 电荷与范数闭零化

2026-10-22。本分支独占推导。对象是 430–432 的原 Hilbert 表示、实际 V 和原酉 u；不以 Ξ 零除子定义底空间，不对 u 取字符值。本文不改公共 STATE，不自行结算轮数。

## 1. 待检验的实际理想与结论范围

保留

\[
 A=A_{\rm src}=\operatorname{alg}(1,u,u^*,D_{\rm src}),\qquad
 I=\mathcal S_1(\mathcal H),\qquad
 A(h)=VU(h)V^*,\quad \delta F=F-uFu^*.
\]

U(h) 是原时间卷积，\(\|V\|=\sqrt2\)。物理紧支源的 raw map 为
\(r\mapsto F_r=A(h_r),\ h_r(s)=r(-s)\)，不是实际相对 DGA 中的 Schwartz dilation lift。
432 已给

\[
 \Omega:HH_1(A/I)\to\mathbf C,\qquad
 \Omega\Big(\sum a_i\otimes b_i\Big)
 =\operatorname{Tr}\sum[A_i,B_i].                         \tag{1}
\]

其定义要求商上的整条一链闭合。对 raw weighted 链
\(q(u^*)\otimes q(uF_r)\)，边界正是 \(q(\delta F_r)\)。

下面实际构造一个紧支、双极点矩为零、在 537 正窗内的非根源 \(r_*\)，令

\[
 J_*=\langle I,\delta F_{r_*}\rangle_A                    \tag{2}
\]

为**代数**双侧理想。它使这一个 weighted 链在 \(A/J_*\) 形式闭合，但：

1. 存在 \(T,T^*\in J_*\cap D_{\rm src}\)，使 \([T,T^*]\) 有限秩且普通迹为 \(-4\)。
2. 因此不存在 \(J_*\) 上匹配 I 普通迹的循环线性泛函；不需连续性或正性假设。
3. 旧 \(\Omega\) 不能沿自然商映射
   \(HH_1(A/I)\to HH_1(A/J_*)\) 下降。
4. 在 \(C^*(A)\) 中，(2) 的范数闭理想恰为 \(\overline{D_{\rm src}}\)，于是杀掉全部 raw \(F_r\)，包括指定 537 非根。

第 4 条只属于范数闭包；**不声称代数 \(J_*=D_{\rm src}\)**。也不声称每个可能的新相对边/余圈都不成立。

## 2. 用真实有限 Γ 矩阵隔离一个角

430–431 给有限源指标 \(J=\{0,1\}\)、真实
\(X_J=(V,uV)\)，以及光滑 M 周期的严格正矩阵

\[
 \Gamma(x)=\begin{bmatrix}\gamma_0(x)&\gamma_1(x)\\
                       \gamma_{-1}(x)&\gamma_0(x)\end{bmatrix}
 \succeq I_2,\qquad \gamma_0=2,\quad M=\log q.             \tag{3}
\]

对 \(B\in M_2(G_M)\) 记 \(F(B)=X_JBX_J^*\)。商 \(D_{\rm src}/I\) 的实际乘法为

\[
 [F(B)]\,[F(C)]=[F(B\Gamma C)].                          \tag{4}
\]

等号的提升差已由 430 的光滑紧支核证明在 I 中；不是忽略一个非紧余项。\(G_M\) 为光滑、联合 M 周期、有限传播核代数。左右乘光滑周期函数仍留在 \(G_M\)。

给定 \(C,D\in G_M\)，取只有第 0 行/列非零的有限矩阵

\[
 L_{0i}=C M_{(\Gamma^{-1})_{0i}},\qquad
 R_{j0}=M_{(\Gamma^{-1})_{j0}}D.                          \tag{5}
\]

\(\Gamma^{-1}\) 光滑周期，故两个实际有界提升 \(F(L),F(R)\in D_{\rm src}\) 合法。
\(\delta A(h)\) 的符号为 \(E_{00}U(h)-E_{11}U(h)\)。由 (4)–(5)，

\[
 \begin{aligned}
 [F(L)\,\delta A(h)\,F(R)]
 &=\big[F\{L\Gamma(E_{00}U(h)-E_{11}U(h))\Gamma R\}\big]\\
 &=[F(E_{00} C U(h)D)].                                \tag{6}
 \end{aligned}
\]

有限矩阵的 \(\Gamma^{-1}\Gamma\) 乘积在正确腿上相消；不假设 C、D 与周期系数交换。
所以在包含 I 和 \(\delta A(h)\) 的任何代数双侧理想中，

\[
                      V C U(h) D V^*\text{ 都在该理想中}. \tag{7}
\]

只用了二阶有限 Γ，无无限 Γ 的有界性/逆假设。

## 3. 一个双矩为零的实际 h₀，使周期秩一角成为理想元素

取
\(0<L_0<\min(M/2,17/16)\)、\(0<\epsilon<L_0/8\)，选紧区间 \(I_0\Subset(0,M)\)，其宽度 w 小于 ε。
取非负实 \(\phi\in C_c^\infty(I_0)\)，\(\|\phi\|_2=1\)，记
\(m_\phi=\int\phi>0\)、\(\phi_n(x)=\phi(x-nM)\)。

取实偶 \(\chi\in C_c^\infty((-L_0,L_0))\)，在 \(|s|\le2\epsilon\) 恒为 1。令

\[
 c_\phi=m_\phi^{-2},\qquad \psi_*=-4c_\phi\chi,
 \qquad h_0=(D^2-1/4)\psi_*
          =c_\phi(\chi-4\chi'').                         \tag{8}
\]

h₀ 在相关差集恒为 \(c_\phi\)。分部积分且 \((D^2-1/4)e^{\pm s/2}=0\) 给

\[
 \int e^{s/2}h_0(s)ds=\int e^{-s/2}h_0(s)ds=0;            \tag{9}
\]

取实际物理源 \(r_*(u)=h_0(-u)=h_0(u)\)。它明确具有 537 的 \((D^2-1/4)\psi_*\) 形式，非零、双矩为零、紧支于严格正窗；因此 \(Q_W(r_*)>0\)，不是 Pan 或 Weil 零方向。

定义真实全线周期算子

\[
 P=\sum_{n\in\mathbf Z}|\phi_n\rangle\langle\phi_n|,
 \qquad B=\sum_{n\in\mathbf Z}|\phi_{n+1}\rangle\langle\phi_n|. \tag{10}
\]

P 是正交投影，\(B^*B=BB^*=P\)，\(\|P\|=\|B\|=1\)。核为局部有限和，光滑、联合 M 周期且有限传播，因此 \(P,B,B^*\in G_M\)。无限和以正交胞元给有界算子；不是对原 u 做无限转移修补。

当 n=m 时，h₀ 在相关差集恒为 \(m_\phi^{-2}\)，故
\(\langle\phi_n,U(h_0)\phi_n\rangle=1\)。当 n≠m 时，差集位于
\((n-m)M+(I_0-I_0)\)，与 h₀ 支撑不交。因此

\[
                         P U(h_0)P=P.                    \tag{11}
\]

因为 \(BP=B\)、\(B^*P=B^*\)，在 (7) 中分别选 \((C,D)=(P,P),(B,P),(B^*,P)\)，得到

\[
                  VPV^*,\quad T=VBV^*,\quad T^*=VB^*V^*
                         \quad\in J_*.                  \tag{12}
\]

这是真实理想包含式，不只是在商上同类。理由是 (6) 的误差在 I，而 I 已包含于 J₍*₎。

## 4. 有限秩交换子与非零普通迹

令 \(\xi_n=V\phi_n\)，

\[
 a_n=\|\xi_n\|^2=\int m(x)|\phi_n(x)|^2dx,
 \qquad V^*V=M_m.                                      \tag{13}
\]

不同 n 的 \(\xi_n\) 正交，因为 \(\phi_n\) 支撑不交，而 \(M_m\) 是乘法。
427 给 m 充分左端为 0、充分右端为 2，故 aₙ 在充分负 n 为 0、充分正 n 为 2。
在 \(\xi_n\ne0\) 的归一化向量上，

\[
 T\xi_n=a_n\xi_{n+1},\quad
 T^*\xi_n=a_n\xi_{n-1},\quad
 [T,T^*]\xi_n=a_n(a_{n-1}-a_{n+1})\xi_n.                 \tag{14}
\]

其在 \(\overline{\operatorname{span}}\{\xi_n\}\) 的正交补为零；(14) 的系数仅有限项非零，故交换子有限秩。
对 N 足够大，求和严格伸缩为

\[
 \begin{aligned}
 \operatorname{Tr}[T,T^*]
 &=\sum_{n=-N}^{N}a_n(a_{n-1}-a_{n+1})\\
 &=a_{-N-1}a_{-N}-a_Na_{N+1}
 =-4.                                                    \tag{15}
 \end{aligned}
\]

若有 aₙ=0，其项本来为零，未引入不存在的归一化向量。正负端只用原 m 的 0→2 跳变；不需单调性或特殊分割。

循环线性泛函 \(\tau:J_*\to\mathbf C\) 若在 I 上为普通迹，因 \(T,T^*\in J_*\)，则
\(\tau([T,T^*])=0\)，与 (15) 矛盾。即使只要求 A-central 的理想迹，亦同样不可能。

更直接地，\(c=q_I(T)\otimes q_I(T^*)\) 是 \(A/I\) 上的一循环，
\(\Omega(c)=-4\)。其在 \(A/J_*\) 的张量像为 0，所以任何经该 HH₁ 商映射因式分解的泛函都在 c 上为 0。
因此不能把旧 432 Ω 原样搬到新 quotient，再向形式闭合的 weighted 链赋值。

## 5. 范数闭理想恰好吞并原源域

设 \(\bar A=C^*(A)\)，令 \(\bar J_*\) 为 (2) 在 \(\bar A\) 的闭双侧理想。
\(D_{\rm src}\) 为 A 双侧理想，故 \(\overline{D_{\rm src}}\) 是 \(\bar A\) 双侧理想，包含 (2) 的生成元；因此

\[
                         \bar J_*\subset\overline{D_{\rm src}}. \tag{16}
\]

反向，由 (12) \(VPV^*\in J_*\)。对任意 i,j、C,D∈G₍M₎，430 的实际乘法给

\[
 F_{i,0}(C)\,(VPV^*)\,F_{0,j}(D)
                  =4F_{i,j}(CPD)+S,
 \qquad S\in I.                                         \tag{17}
\]

这里两次共同角的周期 Gram 都准确等于 \(\gamma_0=2\)。故所有 \(F_{i,j}(CPD)\in J_*\)。

胞元内任意 \(f,g\in C_c^\infty(0,M)\) 及整数 ℓ，定义

\[
 C_{f,\ell}=\sum_n|f_{n+\ell}\rangle\langle\phi_n|,
 \qquad D_g=\sum_n|\phi_n\rangle\langle g_n|.
\]

它们均在 G₍M₎，且 \(C_{f,\ell}PD_g=\sum_n|f_{n+\ell}\rangle\langle g_n|\)。
这些就是胞元 Fourier 下的 Laurent 单项式乘光滑秩一块。
431 §6 已证明其有限线性组合在
\(\overline{G_M}\cong C(S^1)\otimes\mathbb K(L^2(0,M))\) 中范数稠密。
于是所有 \(F_{i,j}(B)\), B∈G₍M₎，都在 \(\bar J_*\)；加上 \(I\subset\bar J_*\)，得到

\[
                          \boxed{\bar J_*=\overline{D_{\rm src}}.} \tag{18}
\]

这一步使用真实算子范数完成，不能删掉闭包、改成代数相等。但 (18) 足以说明范数闭 quotient 把每一个 raw \(F_r\) 及其 u 轨道送为 0，因而不能保指定 537 非根或任何原 raw 源的信息。
它不说 \(\bar A/\bar J_*\) 的纯 u 部分也为零；本稿只消费其原源 ideal 被零化。

只在 C* 目标上还能合法扩展这个零化范围。对任意 \(r\in L^1(du)\)，原卷积仍为有界算子，定义同一 \(F_r=VU(r(-\cdot))V^*\)。
取 \(r_n\in C_c^\infty\) 在 L¹ 中逼近，严格有

\[
                    \|F_r-F_{r_n}\|\le2\|r-r_n\|_1.     \tag{18a}
\]

故所有这些 bounded raw 源都在 \(\overline{D_{\rm src}}\)。特别对 smooth S_exp 源与光滑 compact cutoff \(\chi_R\)，
\(\|F_r-F_{\chi_Rr}\|\le2\|(1-\chi_R)r\|_1\to0\)。
因此 C* quotient 消掉整个 S_exp raw 延拓，包含完整 physical Pan，但也包含所有非根。
这里付的是显式 L¹ 尾；不能由全线原 du 或 Dlog 无条件统一控制该尾。
这不是 HH₁ 或 trace-class 域的延拓定理，也不把原 weighted 链在另一个扩张域的 regulator 自动定义出来。

## 6. 原费用与新增测试边的费用必须分开

对 supp r⊂[−L,L]，原映射严格有

\[
 \|F_r\|\le2\|U(h_r)\|\le2\|r\|_1
       \le2\sqrt{2L}\|r\|_{du}
       \le2\sqrt{2L/\log2}\|r\|_{Dlog},\qquad
 \|\delta F_r\|\le2\|F_r\|.                              \tag{19}
\]

对 r₍*₎ 也成立，且
\(\|h_0\|_{du}\le c_\phi(\|\chi\|_2+4\|\chi''\|_2)\)，原 Dlog 因 h₀ 光滑紧支而有限。
若缩小胞元支撑，\(c_\phi\) 可能增长，本稿不宣称统一无代价。
上述 du/Dlog 是物理源的原范数，只控制 raw 实际有界算子。没有把一个全空间谱下界解释成 source 的必要费用。

(5) 的周期逆矩阵在二阶有限块上 \(\|\Gamma^{-1}\|\le1\)；(10) 的测试 P,B 范数为 1，(12) 的 \(\|T\|\le2\)。这些使实际理想乘法准入合法。
430 的余项 trace-norm 还使用 h₀、P、B 和 Γ 的光滑核半范数；本稿未给其由任意 r 的单一 du 范数支配的全局估计，也不需要这种估计来得到代数反证。
P、B 是**额外的合法代数测试边**，不冒称它们等于某个物理 raw \(F_r\)。其存在用于检验扩大 ideal 的电荷下降，不是通过任意 source 的 lift 算法推导必要高度。

537 原见证 \(r_0=(D^2-1/4)\psi\) 的 \(F_{r_0}\) 在 \(\bar J_*\) 中，故范数闭 quotient 确实丢掉它。
代数 J₍*₎ 是否已包含这个指定 \(F_{r_0}\)，本稿不作未证断言。

## 7. 405 关系、连续/函数域控制及完整 Weil 责任

本稿原代数含 compact r；全 physical Pan 位于 S_exp 扩张域，Pan∩C_c∞=0。故形式闭合一个 compact weighted 链不能证明 405 全主关系相容。
即使另建 S_exp 准入，规范 HH₁ 电荷下降已在 (15) 的 compact 实例上失败；不能靠加 Γ 数值或在商后指定周期读出修复旧 Ω 的这个因式分解矛盾。
在 (18a) 的 C* bounded 延拓中，405 全主关系倒确实被消去，但因全 raw 源都被消去而失去区分力；这不构成同时通过全关系和非根的比较。

连续正反例都可以携带胞元秩一边、普通迹异常及相同形式的 tensor/relative 设施；这些只提供电荷，未选择正极化。
函数域的真曲线 restriction/局部 jets、截面乘法与同一平方上的 RR 是额外结构；将一个非迹类 defect 放进更大理想，只得到 quotient 的闭链，不等于消 gluing 障碍、有费 integral lift 或 primitive 平方容量。

经典目标始终保留 568 的完整

\[
\begin{aligned}
 Q_W(r)={}&2\Re(\mu_+\overline{\mu_-})+
 [\psi(1/4)-\log\pi]\|r\|_{du}^2\\
 &+\frac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
                 \|\tau_vr-r\|_{du}^2dv\\
 &-2\sum_{p,k\ge1}(\log p)p^{-k/2}
                    \Re(r*r^*)(k\log p).
\end{aligned}                                             \tag{20}
\]

Γ/contact、全部 prime powers、两个 pole 和全 complex mixed 既未省略，也未被本局部交换子迹识别。
本稿不产生 (20) 的新正性，不给实际全源到算术截面的 map，不给原 metric lift/local order/平方 RR 身份。

## 8. 扣除强旧后本分支增加什么，未排除什么

427 已排全 D 上标量循环迹扩张；431/432 已排旧 I 上有限轨道修补。那些结论本身没有展示：
**把一个实际双矩零非根源的非紧 defect 纳入新的代数 ideal 后，会精确杀掉哪个原 HH₁ 电荷，以及范数闭 ideal 有多大。**
(6)–(18) 给该具体缺口的实际源、有限 Γ 隔离、有限秩迹见证与闭包识别。
这使“只扩大相对 ideal 使 weighted 链闭合，并原样保留 432 Ω”这一具体类停止；不是仅重述旧非闭性。

不排含额外非标量边/二次 transgression 的真相对复形，不排不要求旧 Ω 原样因式分解的新 regulator、受限 algebraic ideal/强拓扑、实质 integral filtered pair、无限转移但有独立收敛及费用证明的修复。
它们须解释被杀的 −4 电荷去了哪条边，给相容的 405 全关系与537保留、原 norm 及同对象 local filtration/lift/RR。若只给 quotient 闭性或把目标数值定义为 (20)，仍未支付这些独立前件。

最强既有实际 ζ 后果仍为 542+555→557 的 whole leading 4/5 上预算；本分支无新 whole/成长 core/coupling/Ξ 结论，也不满足宏观 Goal 完成门。

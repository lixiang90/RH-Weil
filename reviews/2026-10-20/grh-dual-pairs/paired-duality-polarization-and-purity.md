# 配对 Mellin 对偶之后的 RH：互补纯权、正极化与同对象谱身份

2026-10-20，独立原稿。恢复了 README／STATE／check/show、固定 Goal、前沿及563；
不修改公共状态、cadence 或 Git。固定基线和长期实际 ζ 目标保持，以下是一般对象框架的
新范围说明，不是经典 ζ 独立 Weil 正性的证明，也不声称 Lapidus 对偶定理已推出 RH。

## 1. 两种反射不能混同

以下 w 为事先给出的实对偶权，c=w/2。设完成背景、全部极点和去平凡因子规范已固定，
所得 E_1、E_2 是非零 entire 对象。若实际模型仅有带内亚纯性，以下全局零除子结论
须缩回已证明的共同域，不能免费使用全局 canonical product。

Mellin 对偶的线性身份是

\[
 E_1(s)=\varepsilon E_2(w-s),\qquad\varepsilon\ne0.       \tag{1}
\]

它把除子 D_1 通过 \(\tau(s)=w-s\) 送到 D_2，含原重数。
而正型／Hermitian 条件对应的反线性反射是
\(R_a(s)=2a-\bar s\)。两者不是同一个操作。
只有另核对偶与共轭伙伴的身份

\[
 E_2(s)=\kappa E_1^*(s),\qquad
 E_1^*(s)=\overline{E_1(\bar s)},\quad\kappa\ne0,          \tag{2}
\]

才由(1)得到 D_1 在 R_c 下不变；常数相位不改变除子。
裸 FE 允许先任取 E_1 再定义 E_2(s)=E_1(w-s)，故没有零点位置强制力。
例如 E_1=s-a、E_2=w-s-a，0<a<w、a≠c，满足(1)，两根分别在 a 和 w-a。
两对象都是有限阶、有限除子的合法解析对象；这本身不认证它们来自正 primitive。

更强的实际正 primitive 负对照已有561／562：连续族 Z_c（这里参数 c 应另记 c_par）
在 0<c_par<1/4 时连自对偶 FE、正 P／Π／M 和强 N 正则都成立，完整 Weil 型仍有负方向。
所以弱配对 FE 更不可能自动给正性。

## 2. 严格命题：一般配对的纯线可以不同，但必须互补

在读取未知零点前，由几何权、已指定 twist 或完成背景给出 a_1、a_2，满足
\(a_1+a_2=w\)。定义有内容的配对纯性为

\[
 \operatorname{supp}D_j\subset\{\Re s=a_j\},\qquad j=1,2.\tag{3}
\]

**命题1。** 在(1)下，下列两条件等价：

* (3)成立；
* E_j 在 Re(s)>a_j 均无零，j=1,2。

证明：第一向显然。反向若 D_1 有根 ρ 且 Reρ<a_1，则(1)给 D_2 的根 w-ρ，
其实部大于 a_2，矛盾；D_2 同理。等式边界允许所有重数，根为空也允许。
更一般地，右半平面界 β_1、β_2 通过对偶给出

\[
 w-\beta_2\le\Re D_1\le\beta_1,\qquad
 w-\beta_1\le\Re D_2\le\beta_2.                          \tag{4}
\]

当 β_1+β_2=w 时带宽归零，成为两条互补纯线；对偶单独只给(4)的镜像传输。
“令 a_j 等于实际零点实部”不是先验 RH 推广。权与分解必须从输入数据给定；
按每个未知根事后拆一个子对象会把纯性说成空话。

若再有(2)且 D_1 非空、两对象各只有一条纯线，共轭保实部，故 a_1=a_2，
再由互补性得 a_1=a_2=w/2。**共同中心线是同一归一化下共轭兼容纯性的特例。**
非共轭对偶可以有 a_1≠a_2；不能先作乘积，再强求每个权都居中。

## 3. Weil 泛函的配对关系及正性的准确位置

令

\[
 F_{h,a}(s)=\int_{\mathbb R}h(u)e^{(s-a)u}du,\qquad
 W_{j,a_j}(h)=\sum_{\rho\in D_j}m_\rho F_{h,a_j}(\rho).   \tag{5}
\]

在使用(5)的全域判据时，沿用562的明确前件：完整 E_j 的阶≤1、零点位于有限竖带、
所有重数为正整数，紧支撑光滑测试的垂直快速下降保证和式收敛。
其算术显式公式必须独立证明与(5)完全相等，包含原 Γ、全部 proper powers、pole 和原点项。
一般分布系统也可先定义算术 W；没有这项同对象身份时不能把它当作零除子 W。

写 h^-(u)=h(-u)。由 a_1+a_2=w 和(1)直接换根得到

\[
 W_{1,a_1}(h)=W_{2,a_2}(h^-).                            \tag{6}
\]

此式是双边关系，不是正性。若同中心并有(2)，它进一步给 Hermitian 身份
\(W(h^-)=\overline{W(\bar h)}\)。但 Hermitian 不等于 PSD。
定义 g*(u)=bar(g(-u))，完整二次型是

\[
 Q_{j,a_j}(g)=W_{j,a_j}(g*g^*),\qquad
 g\in C_c^\infty(\mathbb R;\mathbb C).                    \tag{7}
\]

若(3)成立，则
\(Q_j(g)=\sum m_\gamma|\widehat g(-\gamma)|^2\ge0\)，
其中 ρ=a_j+iγ，\(\widehat g(t)=\int g(u)e^{-itu}du\)。频率符号是约定，不影响 PSD。
反向在562的有限阶／完整反射除子条件下，由全部 compact 测试正性推出纯线。
因此可分别在各自 a_j 上证明完整正型，再用(6)核配对相容。

特别不能把563的实偶热 CM 判据直接用于任意非自对偶成员。正谱可能不关于 γ↦−γ 对称，
对应 W Hermitian 但非实偶。更明显的反例是有符号谱
\(\sigma=\delta_1-\delta_{-1}\)：W(u)=2i sin(u)是 Hermitian，Gaussian 热量恒0、
当然完全单调，但 Q=|hat g(−1)|²−|hat g(1)|² 可负。
只观察 γ² 丢掉非对称部分；必须保完整复测试域或额外证实实偶化没有丢失信息。

**合法的 packet 归约保留。** 先固定互补权，置
\(G(z)=E_1(a_1+z)E_2(a_2+z)\)。由(1)直接得 G(−z)=G(z)。
若各 E_j real-type，或同中心两成员恰为共轭伙伴，则适当常数相位下 G 也 real-type。
在全局 order≤1、有限竖带、完整正整数零除子且没有 quotient cancellation 的前件下，
562应用于中心0的 G 给出

\[
 \text{pair-purity}(a_1,a_2)
 \iff Q_{W_G}\ge0\text{ 于全部 complex compact 测试}.      \tag{7a}
\]

原因是 G 的根为两个平移后除子的并；packet 的纯虚根不允许任一成员有离线根。
W_G=W_{1,a_1}+W_{2,a_2}，正性不是由对偶自动给出。
若一般 pair 不 real-type，形式上还可用 H=G G* 构成实偶四因子 packet；
完整正除子前件下同样得到等价，但仍没有独立正性来源。
若 packet 的完整算术身份和563的指数阶增长域也已支付，实偶热 CM 可合法用于 packet。
特别 Dirichlet 共轭 pair 的 packet 允许这一办法；上面的警告只禁止把单成员的非实偶信息直接丢掉，
不是宣称热判据永不能用于非实 χ。packet 归约与各自中心／trace 重数均须保全部 factor，
不能只取 quotient 的净 divisor 或有限 fundamental strip。

## 4. 非循环正极化命题：先核输入能量，后读纯权

**命题2（有限 q-缩放证书）。** 给有限维复空间 V_1、V_2、可逆 F_j、非退化双线性
B:V_1×V_2→C；这些都是分布递推／几何输入。核

\[
 B(F_1v,F_2\eta)=q^w B(v,\eta),\qquad q>1.                \tag{8}
\]

预先指定 a_1+a_2=w，令 U_j=q^{-a_j}F_j。再独立给反线性双射
C:V_1→V_2，使

\[
 U_2C=CU_1,\qquad h(v,z):=B(v,Cz)
 \text{ 是正定 Hermitian 型}.                            \tag{9}
\]

则 h(U_1v,U_1z)=B(U_1v,U_2Cz)=h(v,z)，所以 U_1 相对于 h 酉；
U_2 由 C 传输也酉。故各 F_j 的全部特征值满足
\(|\alpha|=q^{a_j}\)，并且 F_j 半单。于是由指定原算子给出的精确因子

\[
 E_j(s)=\det(I-q^{-s}F_j)                                \tag{10}
\]

的所有零点，含全部 s-plane 周期副本与普通迹重数，分别在 Re(s)=a_j。
证明只用归一化守恒能量，不用未知 ζ 零点。若 h 半正，只能在不变核的商上推出结论；
被丢方向的 determinant／重数不能免费保留。

若 n=dim V_1=dim V_2，则(8)还给
E_1(s)=(-1)^n det(F_1)q^{-ns}E_2(w-s)。乘以已知零自由的 q^{ns/2}
即得到常数倍的(1)；这个指数规范也须固定，但不会移动零点。

矩阵核验形式是 F_1* H F_1=q^{2a_1}H、H>0，且输入 trace／递推确等于(10)。
它是563的有限域证书的配对版本。单有(8)只使两谱互为 q^w/α，绝不控制模。
例如 F_1=diag(q^{a_1+r},q^{a_1-r})，F_2=q^w(F_1^t)^{-1}，标准配对满足(8)，
但 r≠0 时 F_1 不纯。若强作共同中心而不先给权，任意标量 q^b 也能与 q^{w-b} 配对。

**连续流版本。** 给配对生成元 Θ_j，双线性对偶为
\(B(\Theta_1v,\eta)+B(v,\Theta_2\eta)=wB(v,\eta)\)。
若中心化 A_j=Θ_j−a_j 与反线性 C 兼容、且 B(v,Cz) 是正内积，则形式上 A_1 skew。
无限维情形还必须支付共同不变稠密域、闭性／强连续群以及最大 skew-adjoint 性；
仅在一个 core 上的反对称恒等式不足。最清楚的充分输入是事先构造完整强连续群
e^{uA_1}，证明其保持正内积并可延拓成酉群；Stone 才给 A_1=iD、D 自伴。

这还不自动等于目标 ζ。须另证同一 E 的完整谱身份：例如 D 紧 resolvent、
谱计数有多项式增长、每个紧支撑 g 的 Fourier multiplier 为 Hilbert–Schmidt，
以及 W(g*g*)=Tr(T_g T_g*)，T_g=∫g(u)e^{iuD}du。
随后 genus-one determinant 的中心零点因子、正整数重数和零自由规范也须匹配。
有连续谱的乘法算子一般没有这种 ordinary trace／离散 determinant；
可用正 state／相对 trace 的扩展，但必须按扩展对象另立身份，不能冒称普通零除子。

## 5. 三种常见“加倍”不能免费制造 RH

**自对偶乘积。** 由(1)，E_1E_2 关于 w-s 自对偶；它的除子仍是原两个除子的并，
并不会移动根。取 E_1=s-a、E_2=w-s-a，其共同中心 c 的 Weil 核是
2cosh((a-c)u)。对非零实奇 g，适当取 g=uφ、φ偶非负，即有 Q(g)<0。
所以对偶乘积自动得到 FE，不自动得到共同中心的 PSD。

这同样不否定两不同权对象各自纯性：若原先 a_1≠a_2，应逐权使用(7)，
乘积在单一中心的负性仅否定错误的全体共线要求。

**零对角块。** 若 B:H_2→H_1 是有界非零算子，则

\[
 M=\begin{pmatrix}0&B\\B^*&0\end{pmatrix}                 \tag{11}
\]

虽自伴却非 PSD。取 Bη≠0、v=−Bη，二次型为−2||Bη||²。
因此纯 off-diagonal pairing 的双对象 Gram 不可能无条件正，除非 B=0。
要正 block 必须另付正的对角能量及全交叉 Cauchy–Schwarz 约束；
把对偶伙伴辨认为共轭并取对角并不自动证明所得 h 正定。

**自伴 dilation。** 对任意闭稠密定义 A:H_1→H_2，

\[
 \mathcal D=\begin{pmatrix}0&A^*\\A&0\end{pmatrix},\qquad
 \mathcal D(\mathcal D)=\mathcal D(A)\oplus\mathcal D(A^*) \tag{12}
\]

是自伴的；但平方为 diag(A*A,AA*)，读出的是 singular values。
有限维 A=(1+i) 时，原谱为1+i，(12)的谱为±sqrt2。
原特征多项式 z−(1+i) 与 dilation 的 z²−2 不同。
因此任意系统均能自伴加倍这一事实，不给保持同一 ζ 零点与重数的 Hilbert–Pólya 实现。
不定内积下的 adjoint-compatible 也不够：A=diag(r,−r)、J=[[0,1],[1,0]] 满足
A*J+JA=0，却有非纯虚的 ±r；正定性不可删。

## 6. 数论与几何的实质检验

**非自对偶 Dirichlet L。** 对非实 primitive χ，完成函数满足
Λ(s,χ)=εχ Λ(1−s,barχ)，而 Λ(s,barχ)=overline(Λ(bar s,χ))。
两伙伴不同，但它们满足(2)，所以各自零点关于 1−bar s 反射，GRH 仍要求各自中心线1/2。
这里没有“必须先χ=barχ”这个要求，也一般没有每个成员的上下频率偶对称。
FE 的两个不同对象和共轭关系由
[Kedlaya 第6章](https://kskedlaya.org/ant/chap-funceq2.html)的 Poisson 推导核过；
[NIST DLMF 25.15.5](https://dlmf.nist.gov/25.15#E5)也列同一配对。
χ-twist 的 primitive 权是复数，故这是加权一般分布系统的检验，不是声称 untwisted 正计数测度。
这项 FE 已知不支付一般 GRH。

**高维函数域更直接说明互补纯权。** 对光滑射影 d 维 V/F_q，Poincaré 对偶把
H^j 与 H^{2d−j} 配对，Frobenius 特征值成 α·α_dual=q^d；故本稿(8)的总权 w=d。
Weil 纯性却要求两因子的 s-plane 根分别在

\[
 a_1=j/2,\qquad a_2=d-j/2,\qquad a_1+a_2=d.              \tag{13}
\]

它们通常不是共同 d/2；仅中间次数 j=d 位于该中心。
曲线 H^0、H^2 的纯线0与1正好互补，H^1才在1/2。
整个 ζ 是带交错符号的分次 determinant 商，不可抹去 grading 后要求全部零／极点同线。
几何纯性结论及其权由[Milne《The Riemann Hypothesis over Finite Fields》](https://jmilne.org/math/xnotes/pRH.pdf)
Theorem 5.1 核原件；这里不把纯性倒灌成原 Frobenius 已有正定半单实现。
正极化命题是强而明确的充分机制；若只已知特征值模，原算子的 Jordan 与正内积仍需另付。

**连续正分布的配对接口。** Root 另立原稿证明了 h-twist 的 primitive 正性后才可消费：
\(Z_{c_{par},h}(s)=1+c_{par}/[(s-h)(s-h-1)]\)，
0<c_par≤1/2、|h|<1/2，配对 h↔−h，w=1。
预先由两个实际 poles h、h+1 给自身中心 a_h=h+1/2。
当 c_par≥1/4，各对象分别在 a_h、a_−h 纯，而非共同1/2。
阈值 c_par=1/4 时，各自 own-center Weil 核为2，共同中心乘积核为4cosh(hu)，
h≠0 的奇测试负，给上节区分的正 primitive 实例。
这里的 primitive 身份不得由简单 tilt P 猜测：tilt 与 repeat-power 操作不交换；
本稿仅把独立 full P／Π／M 证明作为明确待核依赖，不据此擅自 root-consume。

## 7. 没有对偶时的准确弱形式：先验半平面／误差阈值

设正 Π 的加权 Laplace 域给 Z，并写
ψ(x)=∫_{1^-}^x log y dΠ(y)。若在读取零点前已由实际分布证明

\[
 \psi(x)=\frac\kappa a x^a+O_\epsilon(x^{\beta+\epsilon}),
 \quad a>\beta,\quad \forall\epsilon>0,                  \tag{14}
\]

则部分积分给

\[
 -Z'/Z(s)=s\int_1^\infty\psi(x)x^{-s-1}dx
 =\frac{\kappa s}{a(s-a)}+H(s),\quad\Re s>\beta,         \tag{15}
\]

H 在该半平面 holomorphic，逐紧集选择 ε<Re(s)−β 即可；误差的全部量词不可弱化成有限 x。
若 Z 在该域已 meromorphic，则除指定 a 处的净极点外没有零／极点，因 logarithmic derivative
在其余点无极点。这里只推出右侧无零，不凭空产生左侧反射或中心线。
也不能从任意正 N 的强计数误差替换(14)：N 的 Mellin 延拓不禁止 Z 的零，
561／562的 N=cx+O(log x) 负模型已经阻止这种偷换。

因此无 FE／无先验权时，一个可选 RH 型断言是“达到输入规定的最优无零半平面／
prime-error 阈值”，但没有唯一自动的1/2。仅从主 pole 或 N 增长指数取一半也不具有一般 twist 不变性。
有 FE 后可用命题1把两个先验阈值组合成互补纯线；有正极化后可独立认证这些阈值／纯性。

## 8. 消费范围与最强旧对照

本稿支付的是：(i)配对半平面⇔互补纯线的严格命题；(ii)有输入双线性对偶、
归一化共轭识别和正定能量时，有限 q-缩放给各自纯权；(iii)乘积／off-diagonal／dilation
三条伪强制机制的精确反例；(iv)一般非实偶成员不能偷用单一热 CM。

对象／norm：有限维正 H，或另付 Hilbert 群及原 domain；双线性 B 仅为关系，
不等于正物理能量。trace 重数：有限 determinant 保全整数维数；正半定商、标量 GNS、
continuous spectrum 与 signed cohomological quotient 必须分别核，不自动是普通 ζ determinant。
所有 full W 身份均须在原全部 complex compact 域支付，不是有限窗口／有限点数拟合。

没有支付经典 ζ 的独立正极化、完整 Γ／pp／pole 源身份、无限域与 faithful determinant。
563有限／周期证书、562全 compact 判据与连续谱边界作为旧输入，不重计。
实际 ζ 最强旧542＋555→557 whole leading4/5、成长 K/core/coupling／Ξ责任均未改变；
本稿不操作 Goal/cadence、不结算研究轮，由 root 对全部前件审查后统一消费。

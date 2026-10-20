# 连续源的评价载体、jet 非退化与容量差测试

2026-10-20，评价行列式路线的独立子稿。仅编辑本文件；不结算合同或 cadence。
任务：从完整分布而非零点构造一个实际候选，检验非退化评价、局部消失和全局容量能否自动给完整 Weil 型的符号。

结论：**完整分布无须预设零点便能给规范的代数 Hermitian 评价商；在连续二阶例中还能给显式 jet 代数和所有评价映射。然而同一非零 Wronskian、有限维容量及统一高度界同时存在于正反两段。目标符号位于另一个源定义的配对中，不能由评价行列式的非零性或绝对大小恢复。**

本稿的新测试是具体 carrier／jet／Gram 的比较与阈值退化责任；连续纯性与正能量矩阵已在 562、563、565 支付，不重新计为新纯性。

## 1. 原件、对象与扣除

直接使用 [562](../../../notes/562-generalized-rh-continuous-g-integers-and-spectral-multiplicity.md) §2 的全族

\[
 Z_c(s)=1+\frac{c}{s(s-1)},\quad 0<c\le\tfrac12,\qquad d=c-\tfrac14.
\]

正 primitive \(P_c\)、完整 \(\Pi_c\)、正 \(M_c\) 和延拓已由该原件给出。Gamma 为 0，两个 pole 为 0、1；本稿不改变完成化。
由原分布的所有 prime powers 与两个 pole 精确平衡，

\[
 W_d''+dW_d=0,\qquad W_d(0)=2,\quad W_d'(0)=0.                 \tag{1}
\]

这是一条全 \(D'(\mathbb R)\) 身份，不是在去掉原点后的 ODE。
旧 [563](../../../notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md) 已从 (1) 及正能量矩阵证明正段平方和；旧 [565](../../../notes/565-canonical-completion-graded-identifiability-and-independent-energy.md) 已指出阈值商维数、Jordan、trace 重数不相同。
旧 [567](../../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md) 的正式 graph 反测已经证明对偶、复合、全源 trace 与正的不同图交点不足。下面只比较实际评价结构是否比该正式 graph 增加了可用责任。

所有二次型均在 \(\mathcal D=C_c^\infty(\mathbb R;\mathbb C)\) 上，卷积与 \(g^*(u)=\overline{g(-u)}\) 固定，
\(Q_d(g)=W_d(g*g^*)\)。无物理 \(L^2\) 闭性结论，无 growing-window 量化结论。

## 2. 对任意完整源都存在的代数评价商

设 \(W\) 是 Hermitian 分布，\(W(h^*)=\overline{W(h)}\)。定义

\[
 B_W(g,h)=W(g*h^*),\quad
 R_W=\{g\in\mathcal D:B_W(g,h)=0\ (\forall h\in\mathcal D)\},\quad
 V_W=\mathcal D/R_W.                                      \tag{2}
\]

这只调用源分布。\(R_W\) 是卷积的 \(*\)-理想：例如
\(B_W(k*g,h)=B_W(g,h*k^*)\)，共轭再给 involution 稳定。于是 \(V_W\) 有非退化 Hermitian 配对，且源映射
\(g\mapsto[g]\) 满足

\[
 Q_W(g)=B_W([g],[g]).                                      \tag{3}
\]

评价可以严格解释为 \([g]\mapsto(h\mapsto B_W(g,h))\) 进入测试空间的连续反对偶，不必假设 \(W\) 有点值。商的非退化性来自其定义，**不构成独立正性输入**。它也不自动给规范 Hilbert 范数、Krein 完备化、乘积公式或局部整数消失阶。

当 \(W\) 光滑时可另写点核 \(K_W(x,y)=W(x-y)\)；经典 \(W\) 有 prime 原子及 Gamma finite-part，不能直接把这句点核公式当经典 RKHS 构造。

若先按 (2) 再声称商上的配对正，所声称的仍恰为完整 Weil 正性。若改用任意正内积，(3) 就需要重新证明；负例说明它一般失败。此候选因此支付了“代数商和同源配对存在”，没有支付 LS 证明中的独立局部整除与全局容量比较。

## 3. 连续族的源定义 jet 代数与显式评价

用收敛级数定义两个实整函数，不先求任何零点：

\[
 C_d(u)=\sum_{n\ge0}\frac{(-d)^nu^{2n}}{(2n)!},\qquad
 S_d(u)=\sum_{n\ge0}\frac{(-d)^nu^{2n+1}}{(2n+1)!}.
\]

它们满足 \(C_d'=-dS_d\)、\(S_d'=C_d\)、\(C_d(0)=1\)、\(S_d'(0)=1\)，以及

\[
 C_d(u-v)=C_d(u)C_d(v)+dS_d(u)S_d(v),\quad
 C_d(u)^2+dS_d(u)^2=1.                                  \tag{4}
\]

直接从系数构造有限 \(*\)-代数

\[
 A_d=\mathbb C[D]/(D^2+d),\quad D^*=-D,\qquad
 \tau_d(a+bD)=2a.                                       \tag{5}
\]

\(\tau_d\) 是 regular representation 的普通 trace：乘 \(1\) 的 trace 为 2，乘 \(D\) 的 trace 为 0；这在 \(d=0\) 仍成立。
在此代数中 \(e^{uD}=C_d(u)+S_d(u)D\)，所以

\[
 \tau_d(e^{uD})=2C_d(u)=W_d(u)                            \tag{6}
\]

由 (1) 唯一性及源身份严格成立。对每个 complex compact 源取

\[
 v_g=\int g(u)e^{uD}du=A_g+B_gD,
 \quad A_g=\int gC_d,\quad B_g=\int gS_d.
\]

则 (4) 直接给完整二次型身份

\[
 \boxed{Q_d(g)=\tau_d(v_g^*v_g)=2|A_g|^2+2d|B_g|^2.}       \tag{7}
\]

积分绝对收敛，误差为 0，任意支撑和任意 complex 混合项均包括。这确是 source-derived 的 carrier 与 identity；其正性结论正是旧 563 的同一有限证书，不能声称又得到一个独立正性来源。

映射 \(g\mapsto(A_g,B_g)\) 满射 \(\mathbb C^2\)：\(C_d,S_d\) 作为分布线性独立，由 0 点 value／derivative 即知；若范围不满，存在非零线性组合在所有测试上为 0，矛盾。

## 4. 非退化 jet、非零行列式与有限容量正反段都能通过

取同一解空间

\[
 \mathcal S_d=\{F=aC_d+bS_d:a,b\in\mathbb C\}.
\]

实际 1-jet 评价
\(J_0(F)=(F(0),F'(0))=(a,b)\) 是双射；任意点同样如此，因为

\[
 \det\begin{pmatrix}C_d(u)&S_d(u)\\C_d'(u)&S_d'(u)\end{pmatrix}=1.  \tag{8}
\]

因此：

- 每个非零解在任意一点的消失阶至多 1。
- 同一空间的容量严格为 2，评价 Wronskian 恒为非零常数 1。
- 对 \(|u|\le R\)，全族 \(|d|\le1/4\) 有
  \(|C_d(u)|\le e^{R/2}\)、\(|S_d(u)|\le R e^{R/2}\)，故
  \(|F(u)|\le e^{R/2}(|a|+R|b|)\)。这是固定 coefficient norm 下真正统一的全局上界。

这些性质在 \(d<0\)、\(d=0\)、\(d>0\) 全部成立。它们并没有缺少“非零 carrier”；缺少的是把这个 carrier 的实际 norm／消失量接到目标有符号配对的比较。

更直接地，两点 value 评价矩阵

\[
 M_{x,y}=\begin{pmatrix}C_d(x)&S_d(x)\\C_d(y)&S_d(y)\end{pmatrix},
 \qquad \det M_{x,y}=S_d(y-x).                            \tag{9}
\]

足够接近的不同点使所有参数段中该 determinant 非零；正反段都可构造真实的非退化评价。
还可固定同一个实际测试 \(x=0,y=1\)，无需按未知符号选点：

\[
 E_1=\begin{pmatrix}1&0\\C_d(1)&S_d(1)\end{pmatrix},
 \qquad \det E_1=S_d(1)>0\quad(-\tfrac14<d\le\tfrac14).  \tag{9a}
\]

\(d\le0\) 时级数各项非负且常数项为 1；\(0<d\le1/4\) 时交错级数给
\(S_d(1)\ge1-d/6\ge23/24\)。所以该固定两点评价在全族可逆。
但 **Weil Gram** 是另一个矩阵：

\[
 G_{x,y}=\begin{pmatrix}2&W_d(x-y)\\W_d(x-y)&2\end{pmatrix}
       =M_{x,y}\operatorname{diag}(2,2d)M_{x,y}^T,
 \qquad \det G_{x,y}=4dS_d(y-x)^2.                       \tag{10}
\]

\(d<0\) 时 (9) 非零而 (10) 负，\(d>0\) 时正，阈值为 0。
非零 \(\det M\) 或 \(\log|\det M|\) 无法识别中间配对 \(\operatorname{diag}(2,2d)\) 的符号。
在一般维数还须控制所有 principal minors／全部惯性；一个正的 full determinant 也允许偶数个负方向。

这不是反驳 LS 证明：LS 的非零整数 minor 另有真正有限位同余、同一个 minor 的整除下界及乘积公式。本模型中的非零 Wronskian 只付独立性，不自带这些设施，更未付其预算差恰为 (7)。

## 5. 阈值必须分开 jet carrier、最小 Weil 商和重数

当 \(d\ne0\)，(7) 在 \(A_d\) 上非退化；(2) 的商同构此二维 Hermitian 空间。\(d>0\) 为正定；\(d<0\) 的 signature 是 \((1,1)\)，它是合法的有限维不定载体。

当 \(d=0\)，\(A_0=\mathbb C[D]/D^2\) 仍二维，(8) 的 jet 评价仍非退化；但

\[
 \operatorname{rad}\tau_0(\cdot^*\cdot)=\mathbb C D,
 \qquad V_{W_0}\simeq A_0/\mathbb CD\simeq\mathbb C,
 \quad Q_0(g)=2\left|\int g\right|^2.                    \tag{11}
\]

所以“先造完整 ODE／jet 代数再取 source pairing radical”确能自然得到最小非退化 Weil 载体，但必丢弃 nilpotent jet。完整整个对象仍有二重零，regular trace 仍为 2；商中以权 2 保留这条源信息，不能把 quotient rank 1 当普通谱重数 1。

任何正 Hilbert \(*\)-representation 都必须把 \(D\) 作用为 skew-adjoint。若 \(D^2=0\)，则 \(\|Dv\|^2=\langle v,-D^2v\rangle=0\)，故 \(D=0\)；阈值 jet 代数没有 faithful 的正 Hilbert \(*\)-representation。这不妨碍完整 Weil 正性，也不妨碍另给二维零算子实现二重谱，但后者不是 faithful jet action。

\(d<0\) 时同理 \(D^*D=dI\)，任何非零正 Hilbert \(*\)-representation 都不可能存在。
\(d>0\) 时 (7) 的显式正内积可用。于是要求“此源 jet 代数有 faithful 正 Hilbert action”甚至排掉阈值真阳性；要求“其 source radical 商为正”才准确，但又是目标正性本身。

## 6. 人为给正 capacity，完整源身份在哪里失败

一个看似无零点输入的修复是将 coefficient metric 改为

\[
 H_{\rm abs}=\operatorname{diag}(2,2|d|),\quad(d\ne0),
 \qquad Q_{\rm abs}(g)=2|A_g|^2+2|d||B_g|^2\ge0.          \tag{12}
\]

这是实际正 norm，也可据此作最小范数插值、Hadamard 上界及容量；但负段不满足完整源身份 (7)。取实奇 \(g\)，使 \(B_g\ne0\)（因 \(S_d\) 奇且非零，取小支撑非负偶 \(\phi\) 后 \(g=u\phi\) 即可），则

\[
 A_g=0,\quad Q_d(g)=2d|B_g|^2<0,
 \qquad Q_{\rm abs}(g)=2|d||B_g|^2>0.                    \tag{13}
\]

因此 independently positive capacity 可真实存在而对应错误对象。若把同源要求具体为 translation action 保持 metric，则该要求又等价于旧 skew-energy 恒等式，其正 metric 存在正是负段的未付符号责任。

这里没有得到 LS 式非负局部整数 order \(L_n(g)\) 与 arch capacity \(A_n(g)\) 的非平凡预算差；按 (7) 反定义二者再假设预算顺序，只是等价包装。对 rational \(d\) 可以另找 quadratic algebra 的整结构，也不自动使其 Frobenius Euler 数据等于原来的连续 \(\Pi_c\)；对实参数全族甚至没有规范整数格。不能将一个附加数域的乘积公式当该连续源已经具有的 local/global 身份。

一个更窄的 holomorphic capacity 反测也可精确写出。取 \(0<a<1/2\)、\(d_+=a^2,d_-=-a^2\)。有
\(C_{d_+}(iz)=C_{d_-}(z)\)、\(S_{d_+}(iz)=iS_{d_-}(z)\)，故
\(F(z)\mapsto F(iz)\) 给 \(\mathcal S_{d_+}\to\mathcal S_{d_-}\) 的线性同构，系数为 \((A,B)\mapsto(A,iB)\)。
centered complex disk 的 sup norm、原点 vanishing jet filtration，以及旋转后所有评价 determinant 的绝对值均保持。
但是该同构把物理实线转到虚线，并且不保 \(D^*=-D\) 的 real \(*\)-structure。
因此它只排除**忘掉 real duality 后，纯 holomorphic disk 容量自动提供 Weil 符号**这一窄推断；不排除 fixed-real 结构下真正的 joint 局部／全局条件。

## 7. 一般分布的平滑评价测试与明确停止边界

对经典含分布奇性的 \(W\)，先取实偶 compact mollifier \(\rho_\epsilon\)，令
\(W_\epsilon=W*(\rho_\epsilon*\rho_\epsilon^*)\)。则所有平滑 kernel finite Gram 的 PSD 等价于 \(Q_W\ge0\)：

\[
 \sum_{i,j}a_i\overline{a_j}W_\epsilon(x_i-x_j)
 =Q_W\!\left(\sum_i a_i\rho_\epsilon(\cdot-x_i)\right).   \tag{14}
\]

正向直接。反向先固定 \(\epsilon\)，以 Riemann sums 在每一阶导数上一致逼近 \(g*\rho_\epsilon\)，再用分布连续性，最后 \(\epsilon\downarrow0\) 得任意 \(g\in\mathcal D\)；支撑落在共同 compact，所有 complex mixed 项均保留。
这给一个合法 source-only finite evaluation **等价字典**；“证明所有这样的 Gram 正”仍是完整 Weil 正性，不是独立新输入。

可判准入应当是：一个源定义的额外局部消失机制和一个独立容量定理，在相同 quotient、固定完成化和所有 mixed 方向上，导出 (14) 所需符号，而不是先赋正 metric。连续测试应至少过 (8)–(13)，阈值须分 multiplicity 与 cyclic rank。

经典旧 \(f\) 与物理 \(r=e^{u/2}f\) 的 relation／nonroot 双测试仍须按原坐标运输。本文 (2) 以完整 \(W\) 的 annihilator 定义关系，不能据此声称已经独立构造了 405 的几何 principal 消去或 552 的全部算术评价 map。它只是一个不能误叫新几何的规范代数基准。

**净后果与停止范围：**现在有一个对全连续族实际可写的源 jet carrier、精确完整二次型身份与非退化／radical 分类；它严格区分“评价空间已存在”“正 capacity 已存在”“same-source 配对正”。纯性及系数阈值属于 562/563/565 旧资产。未构造经典 local order、arch 容量预算及其完整源比较，不继续把 quotient／Krein／GNS／capacity 名称串成新存在性公理。该测试不排除真实几何、无限维或非局部的独立估计；它只否定“非零评价 determinant＋有限维上界自然足够”的推断。实际 ζ 的强旧 542＋555→557 whole leading 4/5、560 growing signed/core/coupling 及 Ξ 瓶颈不变。

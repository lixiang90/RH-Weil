# 固定权、有限部分及预算 cocycle：连续族与函数域的具体检验

2026-10-20；569 双载体／Γ来源门的独立模型稿。只编辑本稿及同目录有限核查记录，不更新 STATE、合同或轮数。

**结论：在已经固定的完整源上，可以无零点假设地写出真正的预算分片变换律，连复数混合项的相位也能协调。连续正反例和函数域真／反例全部通过它。故它修复了“每片都应单独下降”的错误，却没有提供 primitive 正号或 RR 容量。**

本稿不宣称实际几何 determinant line 已由一般分布构造出来。下文明确区分：从给定二次型得到的预算线、真实截面复形的行列式线，以及后者尚未支付的容量／曲率来源。

## 1. 固定输入与旧结果扣除

连续模型沿用 [562](../../../notes/562-generalized-rh-continuous-g-integers-and-spectral-multiplicity.md)、[563](../../../notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md)：

\[
 Z_c(s)=1+\frac{c}{s(s-1)},\quad 0<c\le\tfrac12,
 \quad d=c-\tfrac14,\qquad W_d''+dW_d=0,
 \quad W_d(0)=2,\quad W'_d(0)=0.                         \tag{1}
\]

正 primitive、完整 Π、g-integer 正性和所有 powers 的身份均归原件。本稿固定中心 1/2、Γ=0、完整双极点 0/1；不再选完成化。

测试域始终为 \(\mathcal D=C_c^\infty(\mathbb R;\mathbb C)\)，\(r^*(u)=\overline{r(-u)}\)，全部 sesquilinear form 第一变量线性。函数域也使用同一 \(\mathcal D\)，保留全部 lattice 副本；不从有限点数外推。

[568](../../../notes/568-source-evaluation-carriers-local-jets-and-weil-capacity-gap.md) 已付 signed 评价商、局部 jet、点评价费用、正反 Gram 和经典 ±1/8 的分片抵消；[567](../../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md) 已付函数域几何来源和完整周期 Gram。这里新增的具体测试是：**紧支撑关系上的全 complex 预算 cocycle、两类模型的精确 pole 倍率，以及该 cocycle 的非平凡相位和 top determinant 的区分力。** 不重新计这些模型的纯性、ODE 能量或局部载体存在。

## 2. 连续模型：紧支撑关系同时移动 pole 与全部 prime powers

定义

\[
 m_\pm(r)=\int_{\mathbb R}e^{\pm u/2}r(u)du,
 \quad B_P(r,s)=m_+(r)\overline{m_-(s)}+
                m_-(r)\overline{m_+(s)}.                  \tag{2}
\]

完整 prime-power 密度给偶光滑核

\[
 K_d(u)=2\cosh(u/2)-W_d(u),\qquad
 n_c(u)=e^{u/2}K_d(u)\quad(u>0),\quad
 d\Pi_c(u)=\frac{n_c(u)}u du.                              \tag{3}
\]

这里 \(n_c\) 是全部 Π 的密度乘 u，不是 primitive P 或累计 g-integer 计数。两段所有 u>0 都有 n_c(u)>0，此事实归 562/567。令

\[
 B_R(r,s)=\int_{\mathbb R}K_d(u)(r*s^*)(u)du,
 \quad B_W=B_P-B_R.                                       \tag{4}
\]

所有积分在共同 compact 上绝对收敛，(4) 保留全部 proper powers 和两个 pole，误差为 0。

对任意 \(\phi\in\mathcal D\) 取真实紧支撑函数

\[
 k_\phi=(\partial_u^2+d)\phi.                              \tag{5}
\]

分部积分及 (1) 给

\[
 B_W(k_\phi,r)=B_W(r,k_\phi)=0\quad(\forall r\in\mathcal D),
 \qquad m_\pm(k_\phi)=c\,m_\pm(\phi).                     \tag{6}
\]

此处关系在原 compact 域内，无需把经典 405 的非紧支 h 冒充 compact 测试。
非零 compact φ 不可能满足齐次二阶 ODE，所以 k_φ≠0。由 (6)

\[
 P(k_\phi):=B_P(k_\phi,k_\phi)=c^2P(\phi),
 \quad R(k_\phi)=P(k_\phi),\qquad Q_W(k_\phi)=0.           \tag{7}
\]

实偶非负 φ 给 \(P(k_\phi)=2c^2m_+(\phi)^2>0\)。进一步将其缩放到
\(m_+(\phi)=m_-(\phi)=1/(4c)\)，得到明确的

\[
 m_\pm(k_\phi)=1/4,\quad P(k_\phi)=R(k_\phi)=1/8.          \tag{8}
\]

这在固定 \(d=1/16,-1/16,0\) 全部成立。未归一化 pole 倍率分别是
\(25/256,9/256,1/16\)。因此阈值没有被遗漏，也不要求 faithful 正 Hilbert jet action。

对任意 complex r、complex 关系 k，精确变换为

\[
 \Delta_kP(r)=2\Re B_P(r,k)+P(k)
            =2\Re B_R(r,k)+R(k)=\Delta_kR(r).             \tag{9}
\]

两边都满足
\(\Delta_{k+l}P(r)=\Delta_kP(r+l)+\Delta_lP(r)\)。这是一条全 complex、全 mixed、全 compact 的实际预算协同律；不是只在一个实方向上看到数值抵消。

由于 (9) 在负段同样成立，它本身不产生目标符号。负段原有实奇测试使 Q<0，正段原有有限能量证书使 Q≥0；这些符号归旧 563，不计本轮新正性。

## 3. 预算线的非平凡复相位：可修复下降，却不能制造正性

取任一上述 Hermitian form B，F(r)=B(r,r)。在每个有限维 complex 测试子空间上，定义平凡线的 Hermitian metric

\[
 \|(r,z)\|_B^2=e^{F(r)}|z|^2,
 \quad j^B_k(r)=\exp\{-B(r,k)-F(k)/2\}.                   \tag{10}
\]

\(|j^B_k(r)|^2=e^{-\Delta_kF(r)}\)，所以变换 \((r,z)\mapsto(r+k,j^B_k(r)z)\) 保 metric。它不是自动的普通平移群作用，而有准确的 central multiplier

\[
 \frac{j^B_k(r+l)j^B_l(r)}{j^B_{k+l}(r)}
   =\exp\{i\,\Im B(k,l)\}.                               \tag{11}
\]

例如用 (8) 的实 k 并取 l=ik，则
\(B_P(k,ik)=B_R(k,ik)=-i/8\)，两片都出现非平凡 multiplier \(e^{-i/8}\)。忽略复混合项会漏掉这一相位。

对 \(L_P\otimes L_R^{-1}\)，两片 multiplier 完全抵消。因为 k 属于完整 B_W 的 radical，

\[
 j^{P}_k(r)/j^{R}_k(r)=1,\qquad
 \|z\|_{P-R,r}^2=e^{Q_W(r)}|z|^2                          \tag{12}
\]

沿这些关系确能下降。这是一个合法的预算线／相位补偿模型：各分片不必分别成为 quotient 上的数值函数。

但 (10)–(12) 仅使用已经给定的 B_P、B_R、B_W，**不是从独立局部 sections 或 Fredholm complex 得到的 determinant line**。负 Q 也有严格正的 metric e^Q；沿 r=zg 的复直线，\(\partial_z\partial_{\bar z}\log\|1\|^2=Q_W(g)\)。因此若额外要求这个 complex Hessian 对所有 g 有所需正号，仍是完整 Weil 正性本身。

可以用此模型审查真正 det line 的 transition 是否正确；不能把这个 tautological line 的存在当新的 RR 或正曲率来源。也不据此否定真实几何 det line／Quillen metric／局部 cocycle 可能提供独立输入。

## 4. 有限部分的相对变换可规范；绝对 contact 常数仍要锚点

本节是固定经典穿孔核的直接分布计算，不是双 conormal 载体已经提供它的声明。固定

\[
 w(v)=\frac{2e^{-v/2}}{1-e^{-2v}}=v^{-1}+O(1),\quad
 h_e(v)=\tfrac12(h(v)+h(-v)),\qquad \ell>0.
\]

定义真正收敛的有限部分表达

\[
 T_\ell(h)=\int_0^\infty
    w(v)\{h_e(v)-h(0)\mathbf1_{v<\ell}\}dv,
 \quad C_\ell=\kappa+\int_\ell^\infty w(v)dv.               \tag{13}
\]

近 0 差是 O(v²)，远处 w 指数下降；h 任意 compact smooth complex，均合法。
于是完整 Γ 分片可写成

\[
 \Gamma_\kappa(h)=-T_\ell(h)+C_\ell h(0)
 =\kappa h(0)+\int_0^\infty w(v)(h(0)-h_e(v))dv.           \tag{14}
\]

两 cutoffs 的变化为

\[
 b(\ell,\ell')=\int_\ell^{\ell'}w(v)dv,\quad
 T_{\ell'}=T_\ell-b(\ell,\ell')\delta_0,\quad
 C_{\ell'}=C_\ell-b(\ell,\ell').                           \tag{15}
\]

b 的三 cutoff cocycle 恒等式严格成立，故 (14) 不变。对 h=r*r*，contact 是 \(h(0)=\|r\|_2^2\)，全部 complex polarization 均被保留。

这支付相对有限部分变换，**没有选出绝对 \(\kappa\)**；双侧反射只要求它为实数，仍允许加实 \(a\delta_0\)。经典锚点来自已核 [405 §3.1](../../../notes/405-f1-adelic-restriction-moments-and-radical.md) 的指定全局相容 Fourier／Haar 规范（或等价的 canonical Γ 数据），在本物理坐标下 [563 §6](../../../notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md) 固定为 \(\kappa=\psi(1/4)-\log\pi\)。它不来自 (15) 的 cocycle 恒等式本身。双 conormal 候选若穿孔核已不同，改 \(\kappa\) 也不能修复；这是根主稿来源门另行核查的责任。

连续模型 (3) 则有 \(K_d(u)=cu^2+O(u^4)\)，原点没有此类 logarithmic finite-part。规范 Γ=0、固定原源时不需人为加 Γ；若仍改成 \(W_d+a\delta_0\)，(5) 的非零 compact 关系会给 \(Q(k_\phi)=a\|k_\phi\|_2^2\)，故已知关系的消失强迫 a=0。这是**相对已经固定完整源的** contact 检验，不是一般 bare 分布唯一完成化定理。它在正、反、阈值三段都通过。

## 5. 函数域：带所有周期 pole 的紧支撑关系

固定 q=5、L=log q、g=1。真曲线 E:y²=x³+x+1 取 t=−3；[290](../../../notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md) 正整数 Euler 反模型取 t=5。设

\[
 S_0=2,\ S_1=t,\ S_{n+2}=tS_{n+1}-qS_n,\quad
 a_n=q^{-n/2}S_n\ (n\ge0),\ a_{-n}=a_n.
\]

由完整有理函数及 reciprocal 方程，递推双向延伸，

\[
 W=L\sum_{n\in\mathbb Z}a_n\delta_{nL},\quad
 P=L\sum_{n\in\mathbb Z}(q^{n/2}+q^{-n/2})\delta_{nL},
 \quad R=P-W.                                             \tag{16}
\]

R 在 n≠0 的系数为 \(q^{-|n|/2}N_{|n|}\)，已包括全部 closed-point powers；n=0 系数为 2−2g=0。这保留周期 pole，而非拿连续双 cosh pole 冒充函数域 pole。
其他 genus 时 R 的 contact 2−2g 必须另保留；不能等同于无穷 raw point carrier 的维数。

令 \(T_Lr(u)=r(u-L)\)，\(a=t/\sqrt q\)，并置

\[
 p(z)=z^2-az+1,\qquad k_\phi=p(T_L)\phi.                 \tag{17}
\]

双向递推使 \(p(T_L)W=0\)，因而对全部 r∈D，\(B_W(k_\phi,r)=0\)。所有量由实系数及 shift 产生，k 仍 compact；这里既不需要枚举零点，也不需要正极化。

为计算 pole，分段 y∈[0,L) 定义

\[
 M_\pm(r;y)=\sum_jq^{\pm j/2}r(y+jL),\qquad
 P(r)=2L\Re\int_0^L M_+(r;y)\overline{M_-(r;y)}dy.        \tag{18}
\]

固定 r 时统一有限和，因此全部换序和 complex mixed 项没有极限误差。直接移位得

\[
 M_\pm(k_\phi;y)=p(q^{\pm1/2})M_\pm(\phi;y),
 \quad p(\sqrt q)=q+1-t=N_1,
 \quad p(q^{-1/2})=N_1/q.
\]

所以一个新的具体预算检验是

\[
 \boxed{P(k_\phi)=\frac{N_1^2}{q}P(\phi)=R(k_\phi),
       \qquad Q_W(k_\phi)=0.}                              \tag{19}
\]

取非零 φ 支撑于 (0,L)，则 P(φ)=2L||φ||²>0。真例 pole 倍率 81/5；反例 1/5。
两边都可独立 rescale 到 P(k)=1/8；(9)–(12) 的全 complex cocycle／相位检验因此原样通过。

这里 Γ=0；两例均不需要从 archimedean leaf 或 finite-part 人工产生 Γ。
若额外加 \(a_0\mapsto a_0+\epsilon\)，全双向递推在原点附近立即失败；
等价地，\(p(T_L)(\epsilon\delta_0)\ne0\)（有限不同支撑原子线性独立）。
它给 fixed source 的 contact 规范检验，同样不能区分两例的 primitive 符号。

## 6. 固定权与 top determinant 正确，仍不等于纯性

不求根，取 companion 矩阵与源 trace form

\[
 A_t=\begin{pmatrix}0&-q\\1&t\end{pmatrix},\quad
 H_t=\begin{pmatrix}2&t\\t&2q\end{pmatrix}.
\]

精确恒等式是

\[
 \det A_t=q,\quad A_t^TH_tA_t=qH_t,\quad
 A_t^TJA_t=qJ,\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}. \tag{20}
\]

归一化 U=A_t/√q 有 det U=1、UᵀJU=J。故两例的权一对象在 top exterior line 上都具有正确总权 2；dual determinant、symplectic 对偶及 determinant modulus 都通过。

但

\[
 \det H_{-3}=11>0,\qquad \det H_5=-5<0.                   \tag{21}
\]

正号区分本身是旧 563/567/568 资产，本轮不重计。这里检查的是：**与同源预算 cocycle 一起要求正确 top determinant／总权，仍未阻断原反模型。** 若把负 determinant 的绝对值用作正 line metric，会丢掉符号；若要求原 H_t 全正，又回到该有限递推类的纯性证书责任。不能从 top line 的范数为正反推整个 primitive form 正。

## 7. 还缺的独立容量输入与本稿消费边界

预算 cocycle 提供“同一关系如何改变各片”的相容性，既不造 relation 的几何来源，也不限制可消失的空间有多大。若要从真实 determinant line 得出 RR 预算，至少还须：

1. 同一个 global source 的乘法、局部限制及 kernel，不能用局部自由 jets 或按 Q 定义的商代替。
2. 来自该 source 的 principal／transition law，使 (9) 或 (15) 是真实 restriction determinant 的变化；不是先有目标 B 再造 (10)。
3. 局部消失阶／碰撞重数和固定 pole filtration 的独立估计；all complex signed 对应必须在同一设施中运输。
4. 原 norm 下的独立容量／RR 上界，并证明与全部 Γ、prime powers、双 pole、contact 的完整二次项相同；无限 cutoff 还须付共同尺度的误差。

真实曲线给 diagonal 函数域、\(\ker\mathrm{ev}_E=H^0(D-E)\) 和 C×C 上 RR／Hodge index；闭点的自由局部代数不提供它们。函数域反模型已经有 integer Euler、固定权、duality、全递推与本稿 cocycle，缺少这种真实截面容量。连续反例缺少同一容量与其原始 Weil form 的比较；不排除连续几何／非局部容量作为合法修复。

经典 Γ 的穿孔 profile、两半轴规范及绝对 contact 还须由所提双 carrier 共享的原始作用／trace 逐式给出；本稿 (13)–(15) 仅核 finite-part 的必要协同律。即使这一步通过，仍须 1–4 的 global 容量，不能把“Γ 已恢复”或“line metric 为正”升级为 Weil 正性。

| 消费项 | 已付范围 | 仍未付 |
|---|---|---|
| 对象／域 | 连续 ODE 与函数域全 lattice 源；全部 complex compact，真实 k_φ | 不等于一般 g-integer 的几何 principal relations |
| source／误差 | 全 Π、全部周期 pole、contact；式 (2)–(21) 精确 | 经典 leaf profile／固定权来源另审；未给 cutoff RR 误差 |
| duality／norm | 第一变量线性的 Hermitian forms，budget line metric 及 complex phase | 不自动是正 primitive metric、实际 Quillen determinant 或原 Dlog bounded evaluation |
| coefficient direction | pole 与 prime 差保持；finite-part/contact 同向移动并抵消 | signed 差的号未从两片 norm 推出 |
| coverage | 所有 r、φ∈D 和所有 complex relation；函数域全 n 递推 | 无全局 sections、独立容量和经典 growing core 费用 |
| 强旧扣除 | 563 能量／567 RR／568 carrier 与 ±1/8 归旧 | 无 actual ζ 新独立正性，whole leading4/5、560 growing K/core/coupling/Ξ 不变 |

本稿真正增加的是具体协同变换和可复算模型门；它保留 determinant line／cocycle 作为合法修复，但也表明其纯形式存在不能支付新的正性。不得据此增加本子稿独立研究轮或宣称宏观瓶颈已改变。

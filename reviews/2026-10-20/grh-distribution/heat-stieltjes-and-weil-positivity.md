# 完整分布的热变换、完全单调性与 Stieltjes 接口

2026-10-20；独立分析原稿。父任务为一般 g-integer 分布中的独立正性条件，
只写本稿，不修改 STATE／cadence／Git。恢复读 README、STATE、check/show、
固定 Goal／frontier／562 后执行。本文不声明首创，不计新的独立数学轮，
不声称经典 ζ 的 4/5／成长 core／Ξ 瓶颈改变。

## 1. 对象、完整源与能合法配对的域

先由 primitive P 定义全部 powers
Π=Σ_{k≥1}k⁻¹(T_k)_*P，再由**预先固定的同一完成化**定义完整线性分布

\[
 W=\mathcal A_\Gamma+H-\mu_\Pi-\check\mu_\Pi,
 \qquad d\mu_\Pi(u)=u e^{-c_0u}d\Pi(u),\quad u>0.             \tag{1}
\]

这里只是实自对偶、中心 c0 的典型规范；实际算术对象的 archimedean 项和极点
必须用其原显式公式，不能以此符号代替识别。H 包含全部已列极点；
函数域 s 平面的周期极点不能只留 0、1 两点。Γ 项若有 finite-part／接触项，
它仍以分布配对处理。Weil 二次型是
Q(g)=W(g*g*)，g*(u)=bar g(−u)，g 为任意 complex Cc∞。

以下热定理的独立前件：W 是实偶分布，并有有限指数阶延拓。
具体可要求存在 a,C≥0、整数 m，使在光滑超指数下降的函数上

\[
 |W(\phi)|\le C\sum_{j=0}^{m}\sup_u e^{a|u|}|\phi^{(j)}(u)|. \tag{2}
\]

这不是假设 tempered，也不假设任何零点位置。
562 的 cos／cosh 模型及完整经典 Γ／prime-power／pole 分布均满足某个此类估计；
prime powers 由绝对 Euler 收敛给某个指数界，Γ 的局部有限阶奇性须单独保留。
若一般 distribution 型对象不能满足 (2)，本稿不替它支付热配对／极限。

取热核及其完整源热平衡

\[
 k_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)},\qquad
 \Theta_W(t)=W(k_t),\quad t>0.                              \tag{3}
\]

(2) 使热配对、任意 t 导数及复 x 的 Gaussian 卷积均存在；
Θ 在 Re t>0 全纯，W*k_t 是 x 的整个函数。源侧可直接算

\[
 \Theta_W(t)=\mathcal A_\Gamma(k_t)+H(k_t)
      -2\int_0^\infty u e^{-c_0u}k_t(u)d\Pi(u).              \tag{4}
\]

先全部相加才有该对象的 Θ；删 Γ、只取 primes 而删 proper powers、删正极点，
都不再是同一判据。

## 2. 精确命题：实偶完整分布的一个一变量判据

在 (2) 及实偶前件下，以下等价：

1. W(g*g*)≥0，对全部 complex g∈Cc∞(R)。
2. Θ_W 完全单调，即
   (−1)^n Θ_W^(n)(t)≥0，对每个 n≥0 和每个 t>0。
3. 存在正测度 ν 于 [0,∞)，对每个 t>0 有
   Θ_W(t)=∫e^(−tλ)dν(λ)。

这里的 ν 是**平方频率**测度，而非 g-prime 测度；不能混同。

证明 1⇒2：正型分布由 Bochner–Schwartz 是正 tempered 频率测度 σ 的 Fourier 核；
本稿约定 W(h)=∫hat h(ξ)dσ(ξ)，无额外 2π，hat h(ξ)=∫h(u)e^(−iξu)du。
实偶使 σ 对称。故

\[
 \Theta_W(t)=\int e^{-t\xi^2}d\sigma(\xi),\qquad
 (-1)^n\Theta_W^{(n)}(t)=\int\xi^{2n}e^{-t\xi^2}d\sigma\ge0. \tag{5}
\]

2⇔3 是 Bernstein 定理，ν 不必有限，但所有正 t 的 Laplace 质量有限。
可核原件：Schilling–Song–Vondraček，*Bernstein Functions*，
[Theorem 1.4，正文 pp.3–5](https://api.pageplace.de/preview/DT0400.9783110215311_A15706968/preview-9783110215311_A15706968.pdf)。

证明 3⇒1 不预设 W 的 Fourier 变换存在：令 w_t(x)=(W*k_t)(x)。
它是偶整个函数；热方程及偶性给

\[
 \partial_x^{2n}w_t(0)=\Theta_W^{(n)}(t)
      =(-1)^n\int\lambda^n e^{-t\lambda}d\nu(\lambda),
 \qquad\partial_x^{2n+1}w_t(0)=0.                           \tag{6}
\]

另一方面

\[
 v_t(x)=\int\cos(x\sqrt\lambda)e^{-t\lambda}d\nu(\lambda)    \tag{7}
\]

也是整个函数。对复 x 的紧集，cosh(|Im x|√λ)e⁻ᵗλ
由常数倍 e⁻ᵗλ/² 控制，因此积分及全部导数合法。
(6) 使 w_t 与 v_t 的全部 Taylor 系数相同，故 w_t=v_t。
于是每个 t>0 的 w_t 是有限正对称测度
σ_t=(λ↦±√λ 的等分推前)(e⁻ᵗλν)的 Fourier 核，因而正型。
由 (2)，Gaussian 近似单位在 D′ 中给 W*k_t→W（t↓0）：
紧支撑测试的卷积在 (2) 的各指数加权导数范数中收敛；远尾由 Gaussian 吸收指数界。
正型锥在 D′ 中闭，因此 W 正型。证毕。

这也说明 ν 最终必为正 tempered σ 在 ξ² 下的推前；初始不必偷设 ν 的多项式增长。
证明使用全 t／全导数，不把有限热参数或有限阶导数检验升级为结论。

**前件确实必要：**若不要求实偶，一变量热迹只看频率测度的偶部分。
例如 W(u)=cos u+2i sin u 对应 signed 测度
(3/2)δ₋₁−(1/2)δ₁，Θ_W(t)=e⁻ᵗ 完全单调，W 却非正型。
它是 Hermitian 核但非实偶；不能把本定理无条件用于非自对偶对象。

## 3. Stieltjes 版本及其正确归一化

对 ε>0 先作热位移，定义

\[
 R_\varepsilon(x)=\int_0^\infty e^{-xt}\Theta_W(t+\varepsilon)dt. \tag{8}
\]

由 (2) 该积分首先在足够大的实 x 收敛。
若 Θ 完全单调，则它对所有 x>0 收敛，并且

\[
 R_\varepsilon(x)=\int_{[0,\infty)}
      \frac{e^{-\varepsilon\lambda}}{x+\lambda}d\nu(\lambda). \tag{9}
\]

这是有限正测度的 Stieltjes 变换；它满足
lim_{x→∞}Rε(x)=0、lim_{x→∞}xRε(x)=Θ(ε)<∞。
定义允许 λ=0 的 a/x 项，不允许任意添加常数 b。
核 [同一原件 Definition 2.1／Theorem 2.2，正文 pp.11–12](https://api.pageplace.de/preview/DT0400.9783110215311_A15706968/preview-9783110215311_A15706968.pdf)。

反向，若对一列 ε_j↓0，源侧先定义的 (8) 在其收敛半轴与 (9) 型有限正
Stieltjes 表示精确相同，则 Laplace 唯一性使 Θ(t+ε_j) 完全单调；
令 j→∞，每阶导数连续，得 Θ 全完全单调，再由上一命题得完整 Weil 正性。
这里没有声称单个 ε 的证书或 Rε 在正轴上仅为正数便够。
Stieltjes 类要求完整正表示／相应全半平面解析符号，不是普通实轴正值。

若原 Θ 在 0 附近可积，可直接 ε=0；一般 Γ 奇性下不要免费作此假设。
ε 位移保全谱而控制紫外端，也不任意给 Θ 乘 t^r：后者通常不保完全单调性。

## 4. 已付连续正反例的区分力

562 的全部 primitive／powers／N／双极点已付，Gamma=0，不换成经典 Gamma。
其完整 W_c 为

\[
 W_c(u)=\begin{cases}2\cosh(ru),&c<1/4,\ r^2=1/4-c,\\
 2\cos(\tau u),&c\ge1/4,\ \tau^2=c-1/4.
 \end{cases}
\]

故可完全从 (4) 的源侧相消直接计算

\[
 \Theta_c(t)=\begin{cases}2e^{r^2t},&c<1/4,\\
                         2e^{-\tau^2t},&c\ge1/4.
             \end{cases}                                  \tag{10}
\]

负段 Θ(t)>0 对**全部** t>0 成立，却 Θ′>0，第一次非平凡 CM 检验即失败；
“所有温度热迹非负”仍不足以推出完整 Weil PSD。
正段 ν=2δ_{τ²} 是从 primitive 源代数相消得到的独立证书，误差为 0；
阈值 ν=2δ₀ 保留中心零点的二重权。它不自动把标量 L² 变成二重迹空间。

更容易误用的是 Euler 侧的完全单调性：只要 Π≥0，便自动有

\[
 -Z'(s)/Z(s)=\int u e^{-su}d\Pi(u),\quad s>\sigma_a,
\]

及 log Z(s) 的相应交错导数非负。562 正、负段都满足；
它只控制远右半平面，不能代中心化的**完成化热平衡**完全单调性。

另一个外观更接近“background−primes”的 CM 捷径已被
[041 §3，定理 FW](../../../notes/041-euler-bessel-cancellation-no-go.md)严格排除。
令 F(s)=1/(s−1)−(−ζ′/ζ)(s)，其 Laplace inverse 为
eᵘdu−Σ_{n≥2}Λ(n)δ_{log n}。任意安全右移后是有限 signed 测度，
仍含非零负 atoms；Laplace 唯一性排除正表示，故 F 不是 CM。
任意 q>1、h>0 的 F(q+hm) 也由 [0,1] 上 moment 唯一性排除
Hausdorff 完全单调性。数域把 Λ 换成理想 powers 的正权，负 atoms 仍在，同理。
这是强旧结果恢复，不是本稿新 no-go；它不排 §2 的 Gaussian 全源变换，
因为该变换同时保留 Γ、极点和全部尺度的振荡导数核，Laplace 对象并不相同。

对 562 连续谱 log 混合，0<a<b≤1/2，

\[
 \Theta_\nu(t)=\frac{2}{b-a}\int_a^b e^{-t\tau^2}d\tau,
 \qquad d\nu_{\rm energy}(\lambda)=
 \frac{\mathbf1_{[a^2,b^2]}(\lambda)}{(b-a)\sqrt\lambda}d\lambda.\tag{11}
\]

所有 CM 检验成立；Rε 由 2/(b−a)∫_a^b e⁻ετ²/(x+τ²)dτ 给正表示。
ε=0 时为
2[(b−a)√x]⁻¹[arctan(b/√x)−arctan(a/√x)]。
因此热条件也涵盖连续正谱。该混合的 completed log determinant 有分支、失败
包含整条中心线的 meromorphic C1，CM 本身不会把它修成整个零点乘积。

## 5. 数域、函数域的真实检验

数域 K 用所有素理想的 Π_K，以及原判别式／Γ_R、Γ_C／0,1 极点构造 W_K。
实自对偶及 (2) 支付上述热定理接口；Θ_K 由原源可计算。
Π_K≥0 只给 Euler 半平面 CM，不能给 Θ_K 的全 CM。
若证明全 CM，配完整显式公式及 562 判据就会推出 Dedekind ζ_K 的 RH；
本文没有新的数域独立证书。K=Q 正是经典缺口，不能把该测试说成已验证。

函数域曲线有一个完全物理的离散热表达。令 ℓ=log q，亏格 g，并从点数定义

\[
 a_0=2g,\qquad
 a_n=q^{-n/2}\big(q^n+1-\#C(\mathbf F_{q^n})\big),\quad n\ge1,
 \quad a_{-n}=a_n.
\]

清除**全部周期极点**后，完整非平凡零分布在 log 坐标为

\[
 W_C=\ell\sum_{n\in\mathbb Z}a_n\delta_{n\ell},\qquad
 \Theta_C(t)=\frac\ell{\sqrt{4\pi t}}
   \left[2g+2\sum_{n\ge1}a_n e^{-n^2\ell^2/(4t)}\right].     \tag{12}
\]

该恒等式也可先用有理 zeta 因子的 Fourier／Laplace 展开识别，不输入纯性。
一旦几何 Weil RH 支付 α_j/√q=e^{iθ_j}，Poisson 给

\[
 \Theta_C(t)=\sum_{j=1}^{2g}\sum_{k\in\mathbb Z}
 \exp\left[-t\left(\frac{\theta_j+2\pi k}{\ell}\right)^2\right].\tag{13}
\]

右侧是显式正能量测度，所有导数绝对收敛，故 Θ_C 全 CM。
这是用独立几何纯性验证同一热条件；不是从粗点数正性重证 Weil RH。
也可把 a_n 当全部 Toeplitz 矩阵的序列证书，但核全部矩阵仍须几何输入。
genus 0 时非平凡 W=0，不能拿未清的周期 pole 做虚假的负／正比较。
较高维必须逐纯权因子中心化，整个 zeta 的多权零／极点不共一条线。
函数域规范和纯性来源沿用 562 已核
[Milne §0–1](https://jmilne.org/math/xnotes/pRH.pdf)。

## 6. 独立可认证的强化，和经典 ζ 精确缺的箭头

可成立的分布条件是：**从完整源 (4) 给出正能量 Laplace 表示 (3)**，
或者给出全部交错导数的独立 signed-moment 恒等式／非负分解，
再用上面的热定理推出 full complex compact PSD。它不先设零点位置，
也不要求零点谱离散；是否是整个对象再由 C1 与身份单独处理。

但把“Θ 完全单调”直接列为公理，在本类中只是完整 Weil 正性的一个
一变量等价重写，不自动降低证明责任。真正的新输入必须是源侧正表示／结构性证书。
从 positive Π 出发，导数核

\[
 (-\partial_t)k_t(u)=\left(\frac1{2t}-\frac{u^2}{4t^2}\right)k_t(u)
\]

已经随 u 改号；更高阶为带振荡的 Hermite／Laguerre 型核。
因此 Π 的正性、光滑性、N(x)=Ax+O(log x)、FE 都没有独立控制
Γ＋全部 poles 与 arithmetic 的这组 signed moments。

对经典 ζ，最小尚未付箭头具体是：从实际 log p、所有 k≥1、实际 Γ=2θ′、
双 pole 的源表达 (4)，独立证明

\[
 (-1)^n\frac{d^n}{dt^n}\Theta_\zeta(t)\ge0
       \quad\text{对全部 }t>0,\ n\ge0,
\]

或独立造出与其完全相等的 ν≥0。
不能以“零点已居中所以取 ν=Σδ_{γ²}”来付款；也不能以有限 t／有限 n 数值核验替代。
这条接口优于模糊“热迹正”之处是给出了严格够用的量词、失败模型和 Γ／pp／pole 账本；
它尚未改变经典实际正性／成长 core／Ξ 的未付瓶颈。

## 7. 消费收据

对象：完整实偶 W；norm/domain 为 (2) 的有限指数阶测试延拓及 Cc∞ 全复卷积平方。
源与成长量词：所有热时间 t>0、全部 n、任意 compact 支撑尺度；没有固定窗替代。
依赖：562 正／负 primitive 及 powers 已付；Bernstein 原定理已核；热充分性在 §2 原证。
系数／符号：W=Γ＋全部 H−全部 pp；热正值≠CM，Euler CM≠完成化 CM。
误差：模型恒等式误差 0；经典没有新余项估计或独立正性输入。
覆盖：实偶条件必要；非实偶反例明确。连续谱支持可以正，但不补 C1／trace 重数。
净后果：建立可从源计算的一变量完整判据并排除热迹正的伪充分性；
这是一般条件接口／旧正模型的直接消费，不冒称新的经典 whole 结论。

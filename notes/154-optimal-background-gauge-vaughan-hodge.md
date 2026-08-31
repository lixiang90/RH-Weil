# 最优 background gauge 与无 unit-cell 的 Vaughan--Hodge 分解

文档 153 先把 `Lambda-1` 分解，再以 counting-minus-Lebesgue vector补回连续项。
这是逐系数方便的 lattice-centered gauge，但不是唯一配平方式。本节证明一个
canonical Hilbert projection：把完整 continuum vector以实标量分配到 Vaughan
components，使安全的 component-diagonal budget最小。

这个 gauge 有两个结构收益：

1. 它消除“把全部 `-1` 固定塞进第一个 component”的任意性；
2. 在 exact continuum level直接写 `sum p_r-c`，所以不产生 unit-cell remainder。

它仍不证明 RH。剩余输入变成最优配平后的 Type I/II diagonal budget在 Cauchy
blocks上的可和性。

## 1. 受约束的 rank-one background projection

令 `H` 为复 Hilbert space，`p_1,...,p_R,c in H`，`C=||c||^2>0`。只考虑保持
正负 height共轭对称的实 gauge

`v_r(alpha)=p_r-alpha_r c`,

`alpha_r in R`,       `sum_r alpha_r=1`.           (1)

于是对任意 admissible `alpha`，

`sum_rv_r=sum_rp_r-c`.                             (2)

记

`x_r=Re<p_r,c>`,       `x_bar=R^(-1)sum_rx_r`.     (3)

### 定理 ABA（optimal real background split）

在式 (1)的 affine hyperplane上，

`D(alpha)=sum_r||p_r-alpha_r c||^2`                (4)

有唯一 minimizer

`alpha_r^*=1/R+(x_r-x_bar)/C`.                    (5)

其最小值为

`D_min=sum_r||p_r||^2-sum_rx_r^2/C`

`              +(C-sum_rx_r)^2/(RC)`.             (6)

#### 证明

展开得

`D(alpha)=sum_r||p_r||^2-2sum_ralpha_rx_r`

`                         +Csum_ralpha_r^2`.       (7)

在 `sum alpha=1` 下作 Lagrange variation，得到

`Calpha_r-x_r=constant`.                           (8)

求和确定 constant并给式 (5)。由于 Hessian在 constraint tangent space上是
`2C I>0`，minimizer唯一。把式 (5)代回式 (7)得到式 (6)。`□`

`alpha_r^*` 不必位于 `[0,1]`；这里优化的是 signed Hodge decomposition，不是
概率混合。若另要求 nonnegative shares，则问题变成同一个严格凸二次型在 simplex
上的投影，但该额外限制不是中心线判据所需。

## 2. Gauge-invariant full energy 与最优安全 majorant

定义 component Gram

`G_alpha(r,s)=<v_r(alpha),v_s(alpha)>`.             (9)

### 定理 ABB（background gauge conservation）

对每个满足式 (1)的 `alpha`，

`1^*G_alpha1=||sum_rp_r-c||^2`                    (10)

与 gauge无关；并且

`||sum_rp_r-c||^2<=R D(alpha)`.                   (11)

因此式 (5)在全部实标量 background splits中给唯一最小的 Cauchy--Schwarz安全
majorant `R D_min`。

若 `P_(r,s)=<p_r,p_s>`、`b_r=<p_r,c>`，则

`G_alpha(r,s)=P_(r,s)-alpha_s b_r`

` -alpha_r conjugate(b_s)+alpha_ralpha_s C`.       (12)

所以最优 gauge只需 finite Gram data，不需要知道零点。

#### 证明

式 (10)由式 (2)；式 (11)是 `||sum v_r||^2<=Rsum||v_r||^2`。定理 ABA遂给
最小 majorant。展开 inner product得到式 (12)。`□`

注意式 (10)说明 gauge不会伪造相消或改变实际 arithmetic energy；它只优化在
分别估计 components时付出的对角损失。

## 3. zeta Abel continuum 的正向量与 finite quadrature

取 `sigma=1/2+delta<1`，`Y>0`。logarithmic lag上的 positive continuum vector为

`c_(Y,sigma)=int_0^infinity`

` e^((1-sigma)lambda-e^lambda/Y)e_lambda dlambda`. (13)

其 scalar total mass是

`M_(Y,sigma)=Y^(1-sigma)Gamma(1-sigma,1/Y)`.       (14)

把 `[0,L]` 分成 cells `I_j`，以 midpoint `a_j` 和 exact mass

`m_j=int_(I_j)e^((1-sigma)lambda-e^lambda/Y)dlambda` (15)

构造 `c_Q=sum_jm_je_(a_j)`。

### 定理 ABC（certified continuum localization error）

若 cell half-width为 `r_j`，则

`||c_[0,L]-c_Q||`

` <=sum_jm_j sqrt(2min(h,r_j))`.                  (16)

遗漏 tail满足

`||c_[L,infinity)||<=sqrt(h)M_tail`,              (17)

其中

`M_tail=Y^(1-sigma)Gamma(1-sigma,e^L/Y)`.         (18)

#### 证明

文档 152 的 interval features满足

`||e_lambda-e_a||^2=2min(h,|lambda-a|)`.          (19)

对每个 cell的 Bochner integral用 Minkowski并取 `|lambda-a_j|<=r_j`，得到式
(16)。式 (17)使用 `||e_lambda||=sqrt(h)`；变量替换 `u=e^lambda/Y` 给式
(14)、(18)。`□`

实现 `abel_continuum_lag_quadrature` 使用 incomplete-Gamma exact cell masses，
并同时返回式 (16)--(18)。它是带确定性 norm error的 floating quadrature，不是
interval arithmetic。

## 4. 无 unit-cell 的 exact Vaughan gauge

沿文档 153，令未中心化的四个 Vaughan coefficients为

`P_1=mu_1*log`,

`P_2=-mu_1*Lambda_1*1`,

`P_3=mu_2*Lambda_2*1`,

`P_4=Lambda_1`.                                   (20)

定理 AAV的证明实际先给

`Lambda=P_1+P_2+P_3+P_4`.                         (21)

令 `p_r` 是式 (20)带 Abel weight与 modulation的 atomic Hodge vectors，`c` 为
式 (13)。

### 定理 ABD（optimal-gauge Vaughan--Hodge criterion）

对每个 Abel/vertical block，以定理 ABA定义 `alpha_(r,k)^*` 和 `D_min(k)`。则：

1. prime--continuum vector精确等于
   `sum_(r=1)^4[p_r-alpha_(r,k)^*c]`，没有 unit-cell remainder；
2. 其 modulated triangular energy至多 `4D_min(k)`；
3. 在文档 151 定理 AAO的 hypotheses下，若

`sup_Y sum_(k in square-root core)D_min(Y,k)/beta_(Y,k)<infinity`, (22)

则 RH 成立；core exterior仍由文档 150 定理 AAK无条件处理。

同一结论适用于任意具有 `R` 项 exact convolution identity的 Gamma--Euler data，
只需把常数 `4` 换成 `R`。

#### 证明

式 (21)减去 continuum vector并使用定理 ABB，得到前两项。式 (22)乘固定常数
`4`后给文档 151 所需的 modulated energy budget；应用定理 AAO与 exterior
localization。一般 `R` 项完全相同。`□`

这证明最优 gauge本身对 zeta无条件存在：`p_r,c`、全部 inner products和
`alpha_r^*` 都只由 primes、Möbius函数、Abel weight与 positive triangular kernel
构造。未证的是式 (22)的 uniform arithmetic bound；它仍然具有 RH 强度。

## 5. Finite gauge audit

实现 `optimal_real_rank_one_background_split` 直接使用式 (5)--(12)；
`balanced_vaughan_continuum_gauge_audit` 把四个未中心化 Vaughan vectors与式
(15)的 continuum quadrature组成扩展 Gram，并同时以直接 signed atomic energy
检查式 (10)。

取 `delta=.1,theta=.25,h=theta/T`，continuum在 `[0,log(N+1)]` 上用 24 个
geometric cells；表中未包含式 (18)的 tail：

| `N,U,V,Y,T` | optimal shares | full energy | `D_min` | anchor diagonal | equal diagonal |
|---:|:---|---:|---:|---:|---:|
| `80,4,5,30,2` | `.378,.153,.225,.243` | `.8505` | `.6021` | `1.0262` | `.6236` |
| `80,4,5,30,8` | `.271,.227,.255,.247` | `.2522` | `.1610` | `.3052` | `.1612` |
| `160,6,7,60,2` | `.346,.189,.220,.245` | `1.9043` | `1.1062` | `2.1959` | `1.1328` |
| `160,6,7,60,8` | `.261,.241,.248,.250` | `.5562` | `.2824` | `.6285` | `.2825` |

相对把全部 continuum放入第一项的 anchor gauge，`D_min`下降约 `41%--55%`；
相对 equal split只改善约 `0.04%--3.5%`，且高度增大时 shares趋近 `1/4`。这说明
equal split在这些 finite blocks上已接近最优，但定理 ABA消除了人为选择并给 exact
最优性证书。

表中的 continuum tail masses约为 `.123,.165`，故这些 full energies不是无限
continuum的近似证书；表只验证 algebra、gauge invariance和预算比较。特别地，
`D_min` 小于 full energy并不矛盾，因为式 (11)带 factor `R=4`，optimized cross
energy在这些 examples中为正。

## 6. 更新后的开放边界

文档 153 的 unit-cell remainder不是 intrinsic obstruction，而是选择
`Lambda-1` lattice gauge的代价。定理 ABD的 exact-continuum gauge将它完全移除。
现在的优先目标是：

1. 直接估计 `D_min`，或利用 equal split的近最优性先证明其 dyadic bound；
2. 对 `P_3` 的 `d>U,m>V` rectangles建立 bilinear near-product estimate；
3. 对 `P_1,P_2` 连同各自 continuum share建立 Type I main-term cancellation；
4. 使用定理 ABC把 finite quadrature audit升级为带 norm error的 block enclosure；
5. 比较直接 full Gram/Schur bound与 `4D_min`，避免固定 factor `4`成为新损失。


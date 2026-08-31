# 有上界正定 correspondence kernel 与 joint-orbit Weil 定理

文档 139 已在 Cauchy 测度上证明：频谱密度 cap `0<=theta<=1` 等价于
`r` 与 `k_C-r` 同时正定。文档 149 又把同一 cap 的最坏值识别为有限迹负指标。
本笔记把这两个事实从特定的高度模型中抽离，并完全搬到 **长度/对应侧**：一个
Hodge effect 不再被视为未知的频谱乘子，而被视为 ambient kernel 的正定
subcorrespondence。

新增内容有三点：

1. 对任意局部紧 Abel 长度群与任意有限 ambient spectral measure，给出
   capped correspondence cone 的内蕴双正定刻画；
2. 对任意 signed orbit current，证明其负指标是该 cone 上的精确线性最优化，
   并给出 block gluing 与 joint cancellation 定理；
3. 把 bounded finite-trace Hodge--Weil 定理改写成纯长度侧的
   correspondence-kernel 结构定理，并逐项审计经典 zeta 中哪些对象已存在、
   哪个统一界仍与 RH 同强。

## 1. Capped correspondence system

令 `G` 是局部紧 Abel 群，`Ghat` 为其 Pontryagin dual。固定 `Ghat` 上有限正
Radon measure `mu`，并定义 ambient correspondence kernel

`kappa(lambda)=int_(Ghat) chi(lambda)dmu(chi)`.    (1)

定义

`C_kappa={r: r and kappa-r are continuous positive definite}`. (2)

式 (2) 是纯长度侧定义，不出现未知的 spectral density。它还具有完全有限的
判据：对任意 `lambda_1,...,lambda_m in G`，

`[r(lambda_j-lambda_k)]>=0`,

`[kappa(lambda_j-lambda_k)-r(lambda_j-lambda_k)]>=0`. (3)

### 定理 ADQ（dominated correspondence/Bochner theorem）[U]

对 continuous `r:G->C`，下列条件等价：

1. `r in C_kappa`；
2. 存在唯一有限正 measure `nu` 满足 `0<=nu<=mu` 且

   `r(lambda)=int_(Ghat)chi(lambda)dnu(chi)`；       (4)

3. 存在 `q in L^infinity(mu)`, `0<=q<=1`，使

   `r(lambda)=int chi(lambda)q(chi)dmu(chi)`.       (5)

此外，式 (3) 对每个有限点集成立当且仅当以上条件成立。

#### 证明

若 `r,kappa-r` 正定，Bochner 定理分别给唯一正 measures `nu,omega`。其
Fourier transforms之和为 `kappa`，Fourier transform唯一性给
`nu+omega=mu`；故 `nu<=mu`。Radon--Nikodym 定理给 `nu=qmu` 与
`0<=q<=1`。反向由 `qmu` 与 `(1-q)mu` 的正性立得。式 (3)正是两个函数正定
的定义。`□`

因此 `C_kappa` 不是一个 relaxation：它与 ambient spectrum 中全部 effects
`0<=q<=1` 精确同构。有限 Gram 对是它的 algebraic shadow。

## 2. Signed orbit current 的精确长度侧负指标

令 `eta` 是 `G` 上有限 complex measure，`a in R`，并假设

`H(chi)=a+Re int_G chi(lambda)deta(lambda)`          (6)

为 `mu`-可积实函数。对 `r in C_kappa` 定义 correspondence functional

`L_H(r)=a r(0)+Re int_G r(lambda)deta(lambda)`.     (7)

正则化 orbit currents 也可使用式 (7)，但必须另证截断极限与 Fubini；本节先在
有限 measure 情形陈述 exact theorem。

### 定理 ADR（exact capped correspondence index）[U]

定义

`Ind_kappa(H)=sup_(r in C_kappa)[-L_H(r)]`.         (8)

则

`Ind_kappa(H)=int_(Ghat) H_-(chi)dmu(chi)`.         (9)

极值由 negative spectral subcorrespondence

`r_-(lambda)=int_(H(chi)<0)chi(lambda)dmu(chi)`     (10)

达到（零集上的选择任意）。

#### 证明

由定理 ADQ，`r` 唯一对应 `dnu=q dmu`, `0<=q<=1`。Fubini 给

`L_H(r)=int_(Ghat)H(chi)q(chi)dmu(chi)`.           (11)

逐点最小化右端，最优选择为 `q=1_(H<0)`，即得式 (9)--(10)。`□`

这把文档 149 的 spectral projection完全翻译成长度侧对象。若一个代数几何或
算术动力系统能直接构造 `r_-` 的替代 correspondence并控制式 (7)，就不必先
构造 Hilbert--Pólya operator。

## 3. Block gluing 与 joint cancellation

### 定理 ADS（orthogonal block gluing and signed subadditivity）[U]

设 `mu=sum_j mu_j`，其中 `mu_j` 两两互异且支撑于可测不交 blocks；令
`kappa_j(lambda)=int chi(lambda)dmu_j(chi)`。则

`Ind_kappa(H)=sum_j Ind_(kappa_j)(H)`              (12)

（允许两边同为 `+infinity`）。对任意 real integrable `H_1,H_2`，

`Ind_kappa(H_1+H_2)<=Ind_kappa(H_1)+Ind_kappa(H_2)`. (13)

式 (13)可以严格。

#### 证明

式 (12)由式 (9)及 measure additivity。式 (13)由逐点
`(H_1+H_2)_-<= (H_1)_-+(H_2)_-`。例如在圆周 Haar measure上取
`H_1(t)=cos t`, `H_2(t)=1-cos t`；总和恒为 `1`，左侧为零，而右侧第一项
严格为正。`□`

因此 prime、continuum 与 Gamma 必须先组成 **同一个 signed symbol** 再取
negative part。分别给三项各自分配 effects再相加，只会得到较弱上界，并可能
完全抹掉 archimedean cancellation。另一方面，高度 blocks 的 ambient measures
真正不交，故式 (12)允许逐 dyadic block严格 gluing，而不引入 cross-block损失。

## 4. 与 full Selberg profile 的严格强弱关系

Correspondence index只读取负方向，不控制 full quadratic energy。取圆周 Haar
measure及

`H_M(t)=M(1+cos t)>=0`.                           (14)

则对每个 `M`，

`Ind_kappa(H_M)=0`, 但 `int |H_M|^2dmu=3M^2/2`.   (15)

所以不存在仅依赖 capped index 的 universal reverse inequality 去控制 `L2`
profile。文档 169 的 fixed-dilation telescoping/Mellin argument需要的是 two-sided
full `L2` 控制；它不能从式 (9)自动恢复。这严格说明新的 target 比 RH 等价的
polylog Selberg profile更定向，但并不说明式 (9)的 uniform arithmetic bound
容易或已经成立。

## 5. Correspondence-kernel Hodge--Weil 结构定理

考虑文档 149 定理 AAE 的解析数据：Poisson-admissible candidates `F_n`、趋向
中心轴的 `delta_n`、Euler open set上的 logarithmic-derivative germ收敛，以及
real-type self-dual order-one divisor `Phi`。再假设对每个 `n` 给定：

1. 一个 capped correspondence system `(G_n,mu_n,kappa_n)`；
2. 只由 Euler、Gamma、pole/continuum 数据构造的 signed orbit symbol `H_n`；
3. 已证明的 defect comparison

   `J_n/pi <= Ind_(kappa_n)(H_n)+eta_n`, `eta_n>=0`. (16)

### 定理 ADT（bounded capped-correspondence Weil theorem）[C]

若

`sup_n[Ind_(kappa_n)(H_n)+eta_n]<infinity`,         (17)

则 `Phi` 的全部非零 zeros位于中心线。

#### 证明

定理 ADR 把式 (17)精确化为
`sup_n[int(H_n)_-dmu_n+eta_n]<infinity`。这正是交换有限迹代数
`L^infinity(Ghat_n,mu_n)` 中的 bounded negative Hodge index。应用文档 149
定理 AAE即得。`□`

有限域 Hodge--Riemann 情形对应更强的 `H_n>=0`，即 index恰为零。定理 ADT
允许数域中出现 arbitrarily deep但总 ambient capacity有界的负井。这里真正被
抽离出的结构不是“存在某个上同调”，而是：

- ambient positive-definite kernel `kappa`；
- 由 `r` 与 `kappa-r` 双正性定义的 subcorrespondences；
- prime/Gamma/continuum 共同产生的 signed orbit functional；
- 沿共尾系统一致有界的 correspondence index。

## 6. 经典 zeta 中的存在性审计

取长度群 `G=R`、characters `chi_t(lambda)=e^(-itlambda)`。对 dyadic height block
`I_T` 令

`dmu_T(t)=1_(I_T)(t)dt/[pi(1+t^2)]`,

`kappa_T(lambda)=int_(I_T)e^(-itlambda)dmu(t)`.    (18)

由定理 ADQ，每个 block 的 capped subcorrespondences恰是所有
`0<=q_T<=1` 的 Fourier transforms；式 (3)给完全有限的 double-Gram证书。
对 Abel candidate `P_(Y,delta)(t)=Re F_Y(delta+it)`，文档 142 与 148 已把
prime atoms、continuum、pole 与 Gamma residual放在同一 shared-lag signed orbit
functional中。因此 `(G,mu,kappa)`、orbit data、block gluing和 finite Gram
interfaces都已无条件显式存在。

仍未证明的是在 `Y->infinity`, `delta->0` 的共尾日程上

`sum_T Ind_(kappa_T)(P_(Y,delta))=O(1)`.           (19)

式 (12)表明左侧正是 global Cauchy negative mass，不是新误差；由定理 ADT，
式 (19)将推出 RH。文档 169 已无条件消去 `N<=T^(2-eta)` 的 arithmetic wedge，
所以新的 correspondence路线应集中于：

1. `N>T^(2-eta)` 的 square-root resonance blocks；
2. 低 polylogarithmic heights；
3. 在取 negative part之前保持 prime/continuum/Gamma joint symbol。

对 paired Dirichlet 或固定次数 Gamma--Euler 数据，可把 `G` 扩为带 local-system
labels 的 Abel length group并令 dual measure带有限矩阵 multiplicity；交换标量
版本逐 character适用，非交换版本则回到文档 149 的 finite-trace theorem。
local temperedness、conductor-uniform Gamma regularization 与 Rankin--Selberg
diagonal必须逐族验证，不能从抽象定理中免费获得。

## 7. 下一步

式 (19)仍是 RH-strength，但现在有一个纯长度侧、可有限检验的目标。下一步应：

1. 在 square-root wedge 的每个 dyadic block选 shared lag set，保持
   `0<=R_T<=K_T`；
2. 把 threshold-complex harmonic current直接配对到 `R_T`，而不是估计 full
   prefix `L2`；
3. 利用式 (13)只对 joint symbol取负部，禁止先拆 prime/Gamma budgets；
4. 对低 height block尝试 exact finite determinant/interval certificate，高块用
   layer-cake large-values控制 capacity；
5. 证明 block bounds按式 (12)可和，再由定理 ADT闭合。

本笔记没有证明 RH。它完成的是一个新的结构抽离：频谱 effect cone 已被完全
等价地实现为长度侧的 capped positive-definite correspondences；经典 zeta 所需
的 ambient kernel与 signed orbit correspondences确实存在，而它们的统一负指标
界仍是明确、未解决且足以推出 RH 的算术输入。

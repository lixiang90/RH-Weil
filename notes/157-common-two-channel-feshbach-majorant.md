# 公共二维 Vaughan 通道与 Feshbach--Loewner majorant

文档 156 发现每个 finite Vaughan component Gram近似 rank two，但逐块本征向量
本身依赖 `Y,T`。本节解决 finite层面的下一个问题：选取 **同一个** 二维 component
subspace，同时覆盖多个 blocks，并在该 subspace不是各 `G_k` invariant eigenspace
时仍构造严格 Loewner majorant。

核心工具是 upper Feshbach completion。它把 core--tail coupling平方吸收到二维
core，再以一个 scalar threshold控制 tail。所得 bound不是 PCA heuristic，而满足
`M-G>=0`。

## 1. 公共 channel basis

令 `G_1,...,G_K>=0` 为同一 `R` 维 component-index space上的 Grams，`omega_k>0`。
为避免大尺度 block仅因总质量支配 basis，定义 trace-normalized aggregate

`G_bar=[sum_komega_k G_k/tr(G_k)]/sum_komega_k`.   (1)

对 `1<=q<R`，令 `P_q` 为 `G_bar` 最大的 `q` 个 eigenvalues对应的 spectral
projection。

### 定理 ABM（common-channel Ky Fan optimum）

在全部 rank-`q` orthogonal projections `P` 中，`P_q` 最大化平均 captured trace

`sum_komega_k tr(PG_k)/tr(G_k)`.                  (2)

等价地，它最小化 normalized aggregate tail trace。该 basis只由 finite positive
Gram data构造，并对 component relabeling作 unitary协变。

#### 证明

式 (2)除以常数 `sum omega_k`就是 `tr(PG_bar)`。Ky Fan maximum principle说明
rank-`q` projection的最大值为 `G_bar`前 `q` 个 eigenvalues之和，并由相应 spectral
projection达到。`□`

实现 `common_component_channel_basis` 返回完整 unitary basis、`P_q`、aggregate
spectrum与 unitarity residual。也可关闭 trace normalization，以总能量而非相对
geometry加权。

## 2. 非不变 core 的 upper Feshbach completion

在 `P=P_q,Q=I-P` 坐标中写

`G=[[A,B],[B^*,C]]>=0`.                            (3)

取任意

`epsilon>||C||`,        `D=epsilon I-C>0`.         (4)

定义

`M_epsilon=`

` [[A+B D^(-1)B^*, 0], [0, epsilon I]]`.          (5)

### 定理 ABN（Feshbach--Loewner upper completion）

有

`G<=M_epsilon`.                                    (6)

core correction `B D^(-1)B^*` 为 positive、rank至多 `q`；当 `P` 是 `G` 的
invariant spectral subspace时 `B=0`，式 (5)退化为文档 156 定理 ABK的 spectral
tail bound。

#### 证明

由式 (3)--(5)，

`M_epsilon-G=`

` [[BD^(-1)B^*,-B],[-B^*,D]]`

` =[BD^(-1/2);-D^(1/2)][BD^(-1/2);-D^(1/2)]^*>=0`. (7)

这给式 (6)。`□`

所以公共 basis不必逐块对角化。偏离 invariant subspace的代价被精确记录为
Feshbach correction，而不是用全矩阵 operator norm粗暴吸收。

## 3. Physical-direction optimal threshold

把 physical vector `e` 在式 (3)坐标中写成 `(x,y)`，并令

`z=B^*x`.                                          (8)

若 `C u_j=c_j u_j`、`z_j=<u_j,z>`，则式 (5)的 physical upper bound是

`Phi(epsilon)=x^*Ax+sum_j|z_j|^2/(epsilon-c_j)`

`                         +epsilon||y||^2`.        (9)

### 定理 ABO（optimal Feshbach tail threshold）

在 `epsilon>max c_j` 上，`Phi` 为 convex，且

`Phi'(epsilon)=||y||^2`

`              -sum_j|z_j|^2/(epsilon-c_j)^2`.    (10)

若 interior root存在，它是唯一 global minimizer；否则 infimum在 spectral edge的
右极限达到。因而每个 fixed common basis都有 canonical physical-optimal tail
threshold。

#### 证明

对式 (9)求导得到式 (10)，且

`Phi''(epsilon)=2sum_j|z_j|^2/(epsilon-c_j)^3>=0`. (11)

严格为正时 root唯一；无 root时 derivative不变号，minimum在 boundary limit。
`□`

`component_channel_feshbach_majorant` 用 bisection解式 (10)，返回 core、coupling
correction、tail三项 ledger，并直接计算 `M-G` 的最小 eigenvalue。

## 4. 公共通道结构定理

### 定理 ABP（common-channel Feshbach--Weil theorem）

设 Gamma--Euler data满足文档 151 的 explicit-formula/barrier hypotheses。若存在
fixed rank `q` component channel bundle `P`（或沿 cofinal schedule相容收敛的
`P_Y`），使每个 square-root-core block都有式 (3)，并可选
`epsilon_(Y,k)>||C_(Y,k)||` 满足

`sup_Y sum_k 1/beta_(Y,k) {`

` x^*A x+x^*B(epsilon I-C)^(-1)B^*x`

`                         +epsilon||y||^2}<infinity`, (12)

则相应 zeta function的全部 zeros位于中心线。

对 zeta 的四分量 Vaughan simplex structure，`q=2` 的 finite common basis、全部
Feshbach blocks和 optimal thresholds无条件存在。尚未证明的是：basis具有由
convolution algebra决定的 cofinal limit，以及式 (12)统一成立。

#### 证明

定理 ABN给每块 Loewner majorant `M_epsilon`，式 (12)正是
`sum e^*M_epsilon e/beta<infinity`。应用文档 156 定理 ABI；core exterior由文档
150定理 AAK处理。`□`

ABP 是一个更具体的广义结构定理：所需 polarization由二维 core form、positive
Feshbach correction与 scalar tail metric组成。有限域 Hodge purity对应 `B=0` 且
tail消失；数域允许二者非零，但要求其 weighted capacities可和。

## 5. 四 block 公共二维审计

使用文档 155 的四个 simplex Grams，等权形成式 (1)。公共 basis的 aggregate
eigenvalues为

`(.62859,.28100,.08569,.00472)`.                  (13)

前两个 basis vectors在 component order

`(Type-I log, Type-I correction, Type-II, low prime power)` (14)

下，忽略小于 `.027` 的 imaginary phases，约为

`u_1=(.841,-.036,.223,.491)`,

`u_2=(.160,-.851,-.485,-.115)`.                   (15)

它们同时混合 Type I/II与 low terms，但在四个不同 blocks中保持固定。

对每块用定理 ABO优化 `epsilon`，得到严格 `M-G>=0` audit：

| `N,Y,T` | physical energy | Feshbach upper | excess | tail edge | chosen `epsilon` |
|---:|---:|---:|---:|---:|---:|
| `80,30,2` | `.805492` | `.805713` | `.0274%` | `.05605` | `.09691` |
| `80,30,8` | `.251132` | `.251147` | `.0059%` | `.01173` | `.02094` |
| `160,60,2` | `2.303470` | `2.320326` | `.7317%` | `.09501` | `.31095` |
| `160,60,8` | `.630838` | `.630844` | `.0008%` | `.01896` | `.03840` |

每个 `M-G` 的 sampled minimum eigenvalue约 `10^(-36)`，与理论上的零 Schur
directions及 35-digit arithmetic一致；没有出现负 Loewner margin。

以 `N=160,Y=60,T=8` 为例，physical upper分成

`core=.629706`, `coupling correction=.000383`, `tail=.000755`. (16)

所以公共 basis并未因非不变性支付明显 Feshbach代价。四块的严格 excess均低于
`.74%`，远优于文档 156 scalar diagonal的 `72%--169%` excess。

这仍是 truncated/midpoint finite evidence：basis来自这四块本身，尚非 independent
out-of-sample construction；也未控制 `Y->infinity`、全部 dyadic heights或
continuum/prime tails。因此不能把表解释为式 (12)已证。

## 6. 下一步

1. 以式 (15)的近实 basis为候选，做 out-of-sample `Y,T,U,V` stability audit；
2. 从 Vaughan convolution identities直接推导候选 basis，而不是从 PCA拟合；
3. 对 tail block `C`证明 `epsilon/beta`的 Cauchy加权可和性；
4. 对 coupling source `B^*x`使用 bilinear large sieve，控制式 (9)的 resolvent项；
5. 用文档 156 定理 ABJ加入 quadrature与prime-tail误差，形成 fully finite Loewner
   certificate。


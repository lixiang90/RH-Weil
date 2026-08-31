# Capped Loewner SDP 的闭式谱解

文档 139 把 contractive-outer realizability精确化为 finite double-Gram区间

`0<=R<=K_C`,                                       (1)

并提出对 arithmetic Hodge functional作 cofinal SDP lower certificates。本节
证明每个这样的有限 SDP 不需要通用 solver：任意 Hermitian linear objective
在式 (1) 上的极小值是一个 normalized objective 的 **全部负 eigenvalues之和**。

因此 finite capped-correlation certificate 最终成为一次 Hermitian spectral
calculation；这与 Weil/Hodge index语言直接一致，且比只看最低 eigenvalue更
准确，因为所有负方向都会贡献 objective。

## 1. Loewner interval 的标准化

令 `K>=0`, `C=C^*` 为 `m x m` matrices，并考虑

`v(K,C)=inf_(0<=R<=K)Tr(CR)`.                       (2)

若 `K` 可逆，写

`R=K^(1/2)XK^(1/2)`, `0<=X<=I`.                   (3)

令

`A=K^(1/2)CK^(1/2)`.                               (4)

则 objective为 `Tr(AX)`。`K` singular时同样在其 support上使用式 (3)。

### 定理 ZA（closed-form capped-Loewner minimum）

若 `lambda_1(A),...,lambda_m(A)` 是式 (4) 的 eigenvalues，则

`v(K,C)=sum_j min(lambda_j(A),0)`.                  (5)

一个 optimizer为

`R_*=K^(1/2)P_-(A)K^(1/2)`,                       (6)

其中 `P_-(A)=1_(-infinity,0)(A)`。

#### 证明

在 `A` 的 eigenbasis中，

`Tr(AX)=sum_j lambda_j(A)X_(jj)`.                  (7)

由 `0<=X<=I` 得 `0<=X_(jj)<=1`。每个正 coefficient取 `X_(jj)=0`，每个负
coefficient取 `X_(jj)=1`，给下界式 (5)及 `X=P_-(A)`。该 `X` 确实满足
`0<=X<=I`，故下界可达；代回式 (3)得式 (6)。singular `K` 只需限制到
`ran K`。`□`

注意答案不是 `lambda_min(A)`，而是 negative spectral trace。一个 density-zero
但多重的负 sector会被完整计数，这与 determinant-line/Hodge-index bookkeeping
相容。

## 2. Correlation objectives 的 arrowhead Gram

取 lag nodes `0=lambda_0,lambda_1,...,lambda_m`，并希望计算

`L(r)=Re[c_0r(0)+sum_(j>=1)c_jr(lambda_j)]`.        (8)

对 correlation Gram约定 `R_(j,0)=r(lambda_j)`。定义 Hermitian arrowhead
matrix

`C_(0,0)=Re c_0`,

`C_(0,j)=c_j/2`, `C_(j,0)=conj(c_j)/2`,            (9)

其它 entries为零。则

`Tr(CR)=L(r)`.                                     (10)

文档 138 式 (12) 经 Gamma/continuum quadrature与 prime truncation后正是式
(8)：所有 orbit lengths只出现在 first correlation column。因此式 (9)把完整
arithmetic data压成一个 sparse objective，式 (4)再由 Cauchy cap传播到全部
matrix directions。

## 3. Explicit finite capped certificate

令

`K_(jk)=e^(-|lambda_j-lambda_k|)`.                 (11)

### 推论 ZB（finite arithmetic capped bound）

对任意满足文档 139 double-positive constraints的 correlation restriction，

`L(r)>=sum_l min(lambda_l(K^(1/2)CK^(1/2)),0)`.     (12)

该界在放宽区间 `0<=R<=K` 上 sharp。

#### 证明

式 (10)后应用定理 ZA。`□`

因为真正 stationary/capped correlation matrices只是 Loewner interval的子集，
式 (12) 是可能偏低但严格有效的 lower bound：

- 若右侧为 `-o(1)`，即可用于中心线证书；
- 若右侧很负，只说明放宽 SDP存在负方向，不说明 actual outer cone存在同一
  方向。

optimizer (6) 正是 relaxation-gap witness；可进一步检查它是否满足 equal-lag
consistency、Toeplitz extension与 dominated spectral measure条件。

## 4. Cofinal eigenvalue-sum center-line theorem

对第 `n` 个 arithmetic candidate，选择 lag set `Lambda_n`、quadrature/truncation
objective `C_n` 与 Cauchy cap `K_n`。假设已证明

`|Re H_n[r]-Tr(C_nR_(Lambda_n)(r))|<=eta_n`         (13)

uniformly for the capped cone。

### 定理 ZC（negative spectral sums imply center-line purity）

若

`sum_l min(lambda_l(K_n^(1/2)C_nK_n^(1/2)),0)`

` >=-epsilon_n`,                                   (14)

且 `epsilon_n+eta_n->0`，则 arithmetic germ有 positive-real continuation，
相应 self-dual order-one divisor的全部 zeros位于中心线。

#### 证明

推论 ZB与式 (13)给文档 139 定理 YZ 的 hypotheses；再应用该定理。`□`

这给出目前最明确的 finite endgame：

`orbit quadrature + Cauchy cap`

` -> normalized Hermitian matrix A_n`

` -> negative eigenvalue sum + analytic tail error`

` -> positive-real limit -> center-line zeros`.   (15)

## 5. 实现

新增：

- `correlation_first_column_objective_gram`：式 (9)；
- `loewner_interval_linear_minimum`：式 (4)--(6)，返回 normalized spectrum、
  negative projection、optimizer与 minimum；
- `capped_correlation_gram_certificate` 可再次验证 optimizer确实满足
  `0<=R_*<=K`。

回归使用一个三节点 Cauchy cap与 complex arrowhead objective，核对 closed-form
minimum等于 optimizer objective，并核对 `R_*` 及 `K-R_*` 的 minimum
eigenvalues只差 numerical roundoff。

## 6. 下一输入：带严格误差的 Hodge quadrature

现在唯一尚未有限化的是文档 138 式 (12) 的 continuous orbit integrals。需要
构造：

1. pole integral `int e^(-sigma u)r(u)du` 的 positive quadrature；
2. digamma numerator
   `e^(-t)r(0)-e^(-sigma t/2)r(t/2)` 在 `t=0` 的 joint quadrature，不能拆项；
3. Abel continuum `e^((1-sigma)lambda)e^(-e^lambda/Y)` 的 adaptive lag mesh；
4. omitted primes与 large lags的 uniform error，估计时只能使用 capped kernel
   `0<=R<=K` 所蕴含的 bounds。

文档 141 已实现第一版 uniform-error quadrature audit，并证明 cell/tail ledger
接入定理 ZC 的充分性。其 baseline显示 tails已较小，主要损失来自三套独立
uniform lag meshes；下一步是 shared adaptive lag mesh与 optimizer stationarity
审计，再决定 interval enclosure的精度配置。

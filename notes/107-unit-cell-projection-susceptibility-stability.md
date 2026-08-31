# Unit-cell projection、Poincaré error 与 susceptibility stability

文档 106 把 endpoint excess 压成三个 determinant capacities；文档 103 又证明
actual spatial Gram 等于 unit-cell mean Gram 加一个显式 positive charge error。
本节把两者严格接合：证明 constrained Hodge representative 及 polarization excess
在 relative positive Gram perturbation 下稳定，并用 unit-cell Poincaré majorant
给出完全离散的 actual-excess upper certificate。

因此经典 zeta 路线中的 scalar susceptibility 已可无循环地归约为：cell-mean
determinants、cumulative divisibility charges 和一个 generalized eigenvalue。
剩余问题不再含 continuous spatial integral。

## 1. Positive Gram perturbation

令 `bar W>0` 是 projected Gram，`E>=0`，并令

`W=bar W+E`.                                        (1)

假设存在 `epsilon>=0` 使

`E<=epsilon bar W`.                                 (2)

对同一个 response `D`，记 normalized canonical representatives 为

`bar v=bar W^(-1)D/C_(bar W)`,

`v=W^(-1)D/C_W`.                                    (3)

令 `bar delta=1/C_(bar W)`。在 `ker D^*` 上定义 projected endpoint coercivity

`bar kappa=min_(D^*x=0) x^*bar Wx/(x^*Bx)`.         (4)

### 定理 UN（constrained minimizer stability）

inverse capacities 满足

`bar delta<=delta_W<=(1+epsilon)bar delta`.          (5)

并且

`||v-bar v||_(bar W)^2<=epsilon bar delta`,         (6)

`||v-bar v||_B^2<=epsilon bar delta/bar kappa`.     (7)

若 `A_W,A_bar` 是相对于同一 endpoint form `B` 的 dimensionless excess，则

`|sqrt(A_W)-sqrt(A_bar)|`

` <=eta:=sqrt(C_B epsilon bar delta/bar kappa)`.    (8)

#### 证明

由式 (2)，`bar W<=W<=(1+epsilon)bar W`。在 affine hyperplane
`D^*u=1` 上取 minimum，立即得到式 (5)。令 `k=v-bar v in ker D^*`。
`bar v` 对 `ker D^*` 在 `bar W`-metric 中正交，故

`v^*bar Wv=bar delta+||k||_(bar W)^2`.              (9)

另一方面

`v^*bar Wv<=v^*Wv=delta_W`

` <=bar v^*Wbar v<=(1+epsilon)bar delta`.           (10)

比较式 (9)--(10) 得式 (6)。式 (4) 给式 (7)。最后

`sqrt(A_W)=sqrt(C_B)||v-v_B||_B`,

`sqrt(A_bar)=sqrt(C_B)||bar v-v_B||_B`;             (11)

对两 norms 使用 reverse triangle inequality 并代入式 (7)，得式 (8)。`□`

这个 bound 只在 response-zero subspace 使用 coercivity，因而不要求 full-space
uniform norm equivalence。

## 2. Exact unit-cell error and relative certificate

沿用文档 103 的 Möbius field。在 unit cell `[m,m+1]` 上

`Phi(y)=s-C_m/y`.                                   (12)

令 `bar W` 是全部 unit-cell means 的 Gram。文档 103 命题 TZ 给

`W=bar W+E_cell`,                                  (13)

`E_cell=sum_m theta_m C_mC_m^*`,                   (14)

其中

`theta_m=1/[m(m+1)]-log^2(1+1/m)>0`.               (15)

定义 Poincaré majorant

`E_P=sum_m [m^(-3)-(m+1)^(-3)]/(3pi^2)`

`                                      *C_mC_m^*`. (16)

### 定理 UO（unit-cell Loewner error certificate）

有

`0<=E_cell<=E_P`.                                  (17)

若

`epsilon_P=lambda_max(E_P,bar W)`,                 (18)

则

`0<=W-bar W<=epsilon_P bar W`.                     (19)

所以定理 UN 可取 `epsilon=epsilon_P`，且式 (18) 完全由 finite cumulative
charges 与 cell-mean Gram 计算。

#### 证明

式 (17) 是文档 103 的 unit-interval Wirtinger--Poincaré inequality逐 cell
求和。式 (18) 的 generalized Rayleigh definition 等价于
`E_P<=epsilon_Pbar W`；与式 (17) 合并得到式 (19)。`□`

## 3. Projected determinant susceptibility transfer

在 projected metric `bar W` 上，取任意 certified
`0<underline sigma<=bar sigma`，令

`t=underline sigma/2`.                              (20)

由文档 106 定理 UL，从三个 projected determinant capacities 定义

`A_hat_bar=C_B[bar delta(t)-bar delta(-t)]/(2t)`,   (21)

则 `A_bar<=A_hat_bar`。

### 定理 UP（fully discrete actual-excess upper）

令

`eta_P=sqrt(C_B epsilon_P/[C_(bar W)bar kappa])`.   (22)

则 actual spatial excess 满足

`A_W<=(sqrt(A_hat_bar)+eta_P)^2=:A_disc`.           (23)

右侧全部由以下 finite data 构成：

1. unit-cell mean vectors 与 their Gram `bar W`；
2. three determinant ratios of `bar W+-tB_perp`；
3. cumulative charges `C_m` 与 Poincaré matrix `E_P`；
4. projected null generalized coercivity `bar kappa`。

#### 证明

定理 UO 允许在定理 UN 中取 `epsilon_P`，故

`sqrt(A_W)<=sqrt(A_bar)+eta_P`.                     (24)

文档 106 定理 UL 给 `A_bar<=A_hat_bar`；合并并平方得到式 (23)。`□`

这一步不以 observed closeness 代替证明：即使实际 `A_bar` 偶然偏离，式 (23)
仍是 directed upper certificate。

## 4. Discrete-cell centerline structure theorem

### 定理 UQ（cell-determinant Weil criterion）

在文档 094 的 fixed-determinant setup 中，用式 (23) 构造 `A_disc`。则

`R_c(P)<=c_1+|target|`

`          *sqrt((R+1)(1+A_disc)/C_B)`.             (25)

若右侧为

`o(sqrt(log N)/loglog(3N))`,                        (26)

则全部 fixed reduced-determinant principal strata 为 `o(1)`。对满足其余
Euler--Tate/Weil package 公理的 zeta function，式 (26) 迫使 zeros 位于中心线。

#### 证明

定理 UP 给 `A_W<=A_disc`。代入文档 100 定理 TM 的 Riesz bound，再应用文档
094 定理 SP。`□`

定理 UQ 是目前对经典 zeta existence 最具体的广义结构版本：positive structure、
determinant susceptibility 与 continuous-to-discrete error 都由 finite arithmetic
matrices 无条件构造。尚未证明的只剩式 (26) 的统一 asymptotic rate。

## 5. Finite audit

下表对 exact `W^sp=W^[0,N^2]` 使用全部 unit cells。`epsilon_P` 是式 (18)，
`A_bar/A` 显示 observed projection accuracy，`A_disc/A` 是严格 certificate 的
松弛。

| `N` | `R` | `epsilon_P` | `A_bar/A` | `A_disc/A` |
|---:|---:|---:|---:|---:|
| 10 | 2 | 0.0196 | 1.001 | 1.56 |
| 10 | 3 | 0.0252 | 0.988 | 4.55 |
| 20 | 3 | 0.0204 | 0.993 | 6.63 |
| 30 | 2 | 0.0116 | 0.967 | 2.53 |
| 30 | 3 | 0.0195 | 1.002 | 1.53 |
| 50 | 3 | 0.0164 | 1.005 | 7.08 |
| 100 | 2 | 0.00894 | 1.055 | 4.52 |
| 100 | 3 | 0.0148 | 1.001 | 1.25 |

unit projection 的 observed excess error 只有约 `0.1%--5.5%`；严格 bound 较松，
主要因为式 (7) 对全部 null directions 使用最坏 `bar kappa`。即便如此，松弛已从
早期 gap bounds 的 `10^4` 量级降至不超过 `7.08`，同时完全移除了 continuous
integral。

`epsilon_P` 在样本中为 `0.9%--2.5%`，并随部分序列下降。这提示下一步可分别
改善两个量：Poincaré charge energy 的 relative bound，以及 perturbation vector
在 forcing-visible null spectrum 中的定向 coercivity，而不是继续使用最坏
`bar kappa`。

## 6. 对经典 RH 的精确剩余输入

经典 zeta 的 fixed-rank structure 目前已有以下无条件 components：

1. unit-cell positive Gram 与 Cauchy--Binet minor representation；
2. incidence--Vandermonde transversal lower bound；
3. three-determinant capacity susceptibility；
4. exact positive cell error 与 Poincaré domination；
5. 定理 UP 的 actual-excess transfer。

因此可把剩余 analytic target 写成单个 fully discrete statement：证明

`sqrt(A_hat_bar_N)`

` +sqrt(C_(B,N)epsilon_(P,N)`

`       /[C_(bar W_N)bar kappa_N])`                (27)

为使式 (25)--(26) 成立的量级。式 (27) 只涉及 finite sums、determinants 与
generalized eigenvalues；证明它仍可能等价于 RH 强度，但不存在 continuous
completion 或 infinite-tail ambiguity。

## 7. 计算实现

新增 `endpoint_projection_alignment_stability_certificate`。它计算 exact/majorant
relative Loewner spectra、actual/projected alignment、projected three-capacity
susceptibility、square-root stability radius、directed actual-excess upper 与
capacity sandwich。

回归测试对 unit Möbius cells 核对 `E_cell<=E_P`、inverse-capacity ordering、
定理 UN 的 square-root bound、定理 UP 的 actual upper，并分别覆盖 null dimension
1 与 2。

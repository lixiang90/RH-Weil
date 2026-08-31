# Response-selective Bessel criterion

文档 114 把 finite-head update 化成三组 positive charge energies。本节再做一次
dimensionless normalization，分离两个性质不同的量：

1. `epsilon`：update frame 在全部 directions 上的最坏 Loewner norm；
2. `beta`：该 frame 在 canonical response direction 上真正可见的能量比例。

finite audit 中 `beta` 只占 `epsilon` 的 `4%--10%`。所以经典 RH 所需的不是改善
整个 charge frame，而是证明 canonical response 对其低可见性；这正是一个
response-selective large-sieve/Bessel 问题。

## 1. Selective Rayleigh quotient

令

`Y=X+E`, `0<=E<=epsilon X`,                       (1)

`c_X=D^*X^(-1)D`,                                 (2)

`q_X=D^*X^(-1)EX^(-1)D`.                         (3)

定义 response-selective Bessel ratio

`beta_X=q_X/c_X`.                                 (4)

### 定理 VN（response-selective Rayleigh identity）

若

`z_X=X^(-1/2)D/sqrt(c_X)`,                        (5)

则 `||z_X||=1` 且

`beta_X=z_X^*(X^(-1/2)EX^(-1/2))z_X`.            (6)

因此

`0<=beta_X<=epsilon`.                             (7)

#### 证明

式 (2) 立即给 `||z_X||^2=1`。把式 (5) 代入式 (6) 得
`q_X/c_X`。式 (1) 等价于
`0<=X^(-1/2)EX^(-1/2)<=epsilon I`，对 unit vector `z_X` 取 Rayleigh quotient
即得式 (7)。`□`

`epsilon` 是 uniform Bessel bound；`beta_X` 是同一 positive observation operator
在 zeta response state 上的 spectral measure first moment。二者相差很大时，使用
worst-direction norm 会丢失真正的 arithmetic alignment。

## 2. Dimensionless capacity response

定义 exact relative capacity loss

`ell_X=(C_X-C_Y)/C_X`.                            (8)

### 定理 VO（dimensionless response sandwich）

有

`beta_X/(1+epsilon)<=ell_X<=beta_X`,              (9)

以及 inverse-capacity ratio

`1/[1-beta_X/(1+epsilon)]`

` <=delta_Y/delta_X<=1/(1-beta_X)`.               (10)

#### 证明

文档 114 定理 VL 给

`q_X/(1+epsilon)<=C_X-C_Y<=q_X`。                 (11)

除以 `C_X` 并用式 (4) 得式 (9)。又

`delta_Y/delta_X=C_X/C_Y=1/(1-ell_X)`，           (12)

代入式 (9) 得式 (10)。`□`

式 (10) 不含量纲，也不依赖 update rank。只要 `beta_X=o(1)`，positive update 对
response capacity 的 relative effect 就是 `1+o(1)`，即使其他 directions 上的
frame norm显著更大。

## 3. Response-Bessel three-point criterion

对

`X_j=X+jtB_perp`, `j in {-1,1}`,                  (13)

记 base inverse capacities `delta_j^0=1/c_j`，并定义 `beta_j`、`epsilon_j`。令

`R_j^up=1/(1-beta_j)`,                            (14)

`R_j^lo=1/[1-beta_j/(1+epsilon_j)]`.              (15)

### 定理 VP（response-Bessel Weil criterion）

定义

`A_beta=C_B[delta_1^0R_1^up`

`              -delta_(-1)^0R_(-1)^lo]/(2t)`.    (16)

则 finite-head excess 满足

`A_head<=A_beta`.                                 (17)

加入文档 111 的 uniform variance-tail radius

`eta_M^2=C_Bepsilon_M^2/(2C_Mkappa_M)`，          (18)

得到

`A_W<=(sqrt(A_beta)+eta_M)^2`.                    (19)

若式 (13)--(19) 构造的 Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (20)

则 fixed reduced-determinant strata 为 `o(1)`；在其余 Euler--Tate/Weil package
公理下，相应 zeta function 的 zeros 位于中心线。

#### 证明

定理 VO 给 updated inverse capacity

`delta_j^0R_j^lo<=delta_j<=delta_j^0R_j^up`.      (21)

centered secant 中对 plus point取 upper、minus point取 lower，得到式
(16)--(17)。文档 111 定理 VD 给式 (19)，再应用文档 100 定理 TM 与文档 094
定理 SP。`□`

定理 VP 与文档 114 定理 VM 代数等价，但揭示了适合渐近估计的最小无量纲输入：

`delta_+^0, delta_-^0, beta_+, beta_-,`

`epsilon_+, epsilon_-, t`.                        (22)

其中真正需要 arithmetic cancellation 的量是两个 selective Rayleigh quotients
`beta_+、beta_-`，而非 full update spectra。

## 4. Möbius charge interpretation

对 finite-head cell update，

`beta_j=`

` [sum_(m<M)theta_m|C_m^*X_j^(-1)D|^2]`

` /[D^*X_j^(-1)D]`.                               (23)

所以 `beta_j` 是 normalized canonical response 在 cumulative-charge observation
frame 中的 weighted mean-square mass。一个 response-selective large-sieve estimate

`beta_j<=b_N`, `b_N->0`,                           (24)

会直接把 update capacities 变成 base capacities 的 `1+O(b_N)` perturbations，
而无需证明整个 frame operator norm 同速衰减。

## 5. Finite audit

| `N` | `R` | `M` | `epsilon` | `beta` | `beta/epsilon` | exact loss fraction | inverse-capacity ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 4 | 9.94e-3 | 7.48e-4 | 0.0753 | 7.44e-4 | 1.000745 |
| 12 | 3 | 5 | 1.55e-2 | 1.02e-3 | 0.0658 | 1.01e-3 | 1.001014 |
| 20 | 3 | 8 | 1.32e-2 | 5.20e-4 | 0.0394 | 5.20e-4 | 1.000520 |
| 30 | 3 | 16 | 1.38e-2 | 1.42e-3 | 0.1025 | 1.41e-3 | 1.001412 |
| 50 | 3 | 30 | 1.21e-2 | 9.38e-4 | 0.0774 | 9.35e-4 | 1.000936 |
| 100 | 3 | 100 | 1.15e-2 | 9.57e-4 | 0.0829 | 9.55e-4 | 1.000956 |

`beta/epsilon` 只有 `0.039--0.102`；exact loss fraction 又与 `beta` 在约百分之一内
一致。由此可见 update 的 worst mode 大部分不与 canonical response 对齐。

## 6. 计算实现

`positive_rank_update_response_kernel_certificate` 现返回
`response_selective_ratio`、exact relative capacity loss，以及定理 VO 的
inverse-capacity ratio bounds。回归验证 `beta<=epsilon` 与两侧 directed sandwich。

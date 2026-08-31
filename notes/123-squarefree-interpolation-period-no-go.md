# Squarefree interpolation periods 与 positivity-only no-go

文档 122 证明全局 Mertens current 可由有限 dual cycles 的 harmonic period精确
读取。本节把这些 cycles 展开到 recovered squarefree evaluations：endpoint sign
functional 是一个有限 Vandermonde interpolation formula。这样可以直接测试
total positivity、Lebesgue constant 或 Christoffel/Cauchy bounds 是否足以达到
中心线阈值。

结论是否定的。对 fixed nodes，最坏 interpolation coefficient norm 必然至少按
`(log N)^R` 增长；有限数据中的 node-value norm 没有相应衰减。更一般地，positive
Gram、fixed capacity 与 totally positive evaluation matrix 不能单独控制 harmonic
period。真正需要的是 actual Möbius--Farey polarization 产生的 signed interpolation
cancellation。

## 1. Squarefree evaluation frame

固定 `R` 个 distinct squarefree nodes `S={n_1,...,n_R}`。令 `L=log N`、
`a_i=log n_i`，并定义 evaluation matrix

`E_N(i,p)=mu(n_i)(1-a_i/L)(a_i/L)^p`,             (1)

其中 `1<=p<=R`。文档 104 的 incidence recovery 给

`E_N=T_SP_N`,                                     (2)

这里 `P_N` 是有限 unit-cell observation matrix，`T_S` 是显式 divisor-incidence
inverse。`E_N` 是 row-scaled Vandermonde，故当 `N>max S` 时可逆。

令 `v_N=W_N^(-1)D_N/C_N` 是 normalized canonical representative。其 recovered
node values 为

`g_N=E_Nv_N`.                                     (3)

对 endpoint sign probe `q_sigma`，定义 interpolation coefficients

`c_sigma=E_N^(-*)q_sigma`.                        (4)

### 定理 WL（squarefree interpolation conservation）

对每个 sign phase，

`q_sigma^*v_N=c_sigma^*g_N`.                      (5)

若 `y_sigma=T_S^*c_sigma`，则

`P_N^*y_sigma=q_sigma`,                           (6)

且

`C_N c_sigma^*g_N`

` =D_N^*W_N^(-1)q_sigma`

` =<O_NW_N^(-1)D_N,y_sigma>`

` =sum_(m<N)M(m)h_sigma(m)`.                      (7)

#### 证明

式 (4) 给 `E_N^*c_sigma=q_sigma`，故
`c_sigma^*g_N=c_sigma^*E_Nv_N=q_sigma^*v_N`。再由式 (2)，
`P_N^*T_S^*c_sigma=E_N^*c_sigma=q_sigma`，得到式 (6)。式 (7) 依次使用
文档 122 定理 WI 与文档 121 定理 WG。`□`

所以 global Mertens sum、sparse incidence cycle 与 polynomial interpolation 是同一
period 的三种 coordinates。

## 2. Fixed-node coefficient blow-up

记 `e_R` 为最高 direction coordinate。由式 (4)，

`q_sigma(R)=(E_Ne_R)^*c_sigma`.                   (8)

### 定理 WM（fixed-node interpolation barrier）

对任意 phase，

`||c_sigma||_2>=|q_sigma(R)|/||E_Ne_R||_2`        (9)

` =|q_sigma(R)|L^R`

`  /[sum_i(1-a_i/L)^2a_i^(2R)]^(1/2).`           (10)

令 `q_sigma=T^*diag(c_j)sigma`。在 full sign cube 上定义

`Q_R=max_sigma|q_sigma(R)|`

`   =sum_j c_j|T_(j,R)|>0`.                       (11)

则 fixed `S` 时

`max_sigma||c_sigma||_2>=k_(S,R)L^R`              (12)

对所有充分大 `N` 成立，其中 `k_(S,R)>0` 显式可算。

#### 证明

式 (9) 是式 (8) 的 Cauchy--Schwarz；把式 (1) 的最后一列范数代入得到式 (10)。
sign cube 的 support-function identity 给式 (11)。fixed nodes 时式 (10) 的
denominator 除去 `L^R` 后趋于 `sqrt(sum_i a_i^(2R))`，从而得到式 (12)。`□`

这与文档 105 的 recovery-energy ceiling 相容但逻辑更直接：即使不估计 divisor
recovery operator，单是 endpoint derivative interpolation 已产生 `L^R` blow-up。

## 3. Local-node sufficient condition及其 norm loss

文档 120 的 exact leverage现在成为

`L_1(N)=max_sigma|c_sigma^*g_N|.                  (13)

### 定理 WN（finite evaluation-period criterion）

在 fixed determinant setup 中，若

`c_1+|target|max_sigma|c_sigma^*g_N|`

` =o(sqrt(L)/loglog(3N)),`                        (14)

则 fixed principal strata 为 `o(1)`；连同完整 polarized Weil package 与总尾
条件即推出中心线结论。

一个更强但丢失 signs 的充分条件是

`max_sigma||c_sigma||_2 ||g_N||_2`

` =o(sqrt(L)/loglog(3N)).`                        (15)

对 fixed nodes，定理 WM 表明任何只用式 (15) 的证明都必须得到至少

`||g_N||_2=o(L^(1/2-R)/loglog(3N))`               (16)

量级的补偿（若使用统一 worst-phase coefficient bound）。

#### 证明

式 (13) 来自定理 WL 与 sign-cube duality。式 (14) 应用定理 WE；式 (15) 是
Cauchy--Schwarz sufficient condition。将式 (12) 代入式 (15)给式 (16)。`□`

式 (14) 是 sharp signed target；式 (15)--(16) 解释了 Christoffel/Lebesgue norm
路线为何会重现 sparse coercivity 的 polylog loss。

## 4. Total positivity 不能代替 arithmetic polarization

去掉 Möbius row signs 后，式 (1) 是 ordinary positive-node Vandermonde，具有
standard strict total positivity。它规定 inverse 的 checkerboard signs，但并不
限制 canonical node vector `g_N=E_Nv_N` 的 sign pattern。

### 定理 WO（positivity/capacity-only period no-go）

设 `R>=2`，固定非零 response `D`、probe `q`，且 `q` 不与 `D` 成比例。即使固定
任意 invertible totally-positive evaluation matrix `E`，也存在 positive definite
metrics `W_t`，使

`D^*W_t^(-1)D=1`,                                 (17)

而 normalized canonical periods

`|q^*W_t^(-1)D| -> infinity`.                     (18)

因此 positive Hodge Gram、capacity、evaluation nondegeneracy 与 total positivity
的组合仍不足以证明式 (14)。

#### 证明

选 `v_0` 使 `D^*v_0=1`，再选 `z in ker D^*` 且 `q^*z!=0`。令

`v_t=v_0+tz`;                                     (19)

则 `D^*v_t=1` 而 `|q^*v_t|->infinity`。对每个 `v_t`，存在 positive definite
`W_t` 满足 `W_tv_t=D`：在以 `v_t/||v_t||` 为首向量的正交基中，固定第一列为
`D/||v_t||`，其首对角元为 `1/||v_t||^2>0`，再把 orthogonal diagonal block 取
到足够大，Schur complement 即为正。于是

`W_t^(-1)D=v_t`,

`D^*W_t^(-1)D=D^*v_t=1`,                          (20)

而式 (18) 由式 (19) 得到。matrix `E` 从未被改变，所以 total positivity 也保持。
`□`

该 no-go 不否定 actual Möbius metric；它严格说明需要使用 `W_N` 与 `D_N` 的联合
算术结构，而不能从抽象 positivity/evaluation axioms 自动推出 quantitative purity。

## 5. Finite audit

使用 fixed nodes `[2,3]` 与 `[2,3,5]`。`CS/exact` 是式 (15) 对式 (13) 的倍率，
`kappa` 是 signed interpolation period 除以逐 node absolute contribution。

| `N` | `R` | exact `L_1` | `||c||_2` | `||g||_2` | CS/exact | `kappa` |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 118.77 | 206.6 | 0.607 | 1.06 | 1.000 |
| 16 | 2 | 96.61 | 323.5 | 0.330 | 1.10 | 1.000 |
| 32 | 2 | 88.32 | 476.6 | 0.230 | 1.24 | 1.000 |
| 64 | 2 | 63.39 | 663.3 | 0.298 | 3.12 | 0.393 |
| 100 | 2 | 19.12 | 800.9 | 0.466 | 19.51 | 0.053 |
| 8 | 3 | 216.87 | 1355 | 1.279 | 7.99 | 0.149 |
| 16 | 3 | 259.40 | 2637 | 1.117 | 11.35 | 0.119 |
| 32 | 3 | 71.13 | 2395 | 0.766 | 25.80 | 0.063 |
| 64 | 3 | 557.46 | 8845 | 0.897 | 14.24 | 0.114 |
| 100 | 3 | 737.64 | 11941 | 0.644 | 10.42 | 0.155 |

interpolation coefficient norm快速增长，而 node norm仍为 order one。`R=3` 的
节省主要来自 signed node cancellation；`R=2` 到较大 `N` 后也出现同一现象。
这些数据不是渐近反例，但明确反对用 node-value norm 或 total positivity 直接关闭
criterion。

## 6. 计算实现

新增 `mobius_endpoint_interpolation_period_certificate`。它构造 recovered evaluation
matrix、canonical node values、phase interpolation coefficients 与 explicit
incidence cycles，并逐 phase核对：

1. interpolation period = direct endpoint functional；
2. capacity-scaled period = Mertens mixed current；
3. incidence-cycle period = 同一 mixed current；
4. highest-coordinate lower bound、Cauchy upper 与 cycle minimum inequalities。

50-digit 回归 residual 均控制在 `1e-41` 以下。

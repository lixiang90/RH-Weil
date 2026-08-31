# Sparse dual cycles 与 canonical harmonic periods

文档 121 把 canonical endpoint leverage 写成全局 dyadic Mertens currents。该表示
揭示了算术来源，但仍含有看似需要逐尺度估计的长和。本节证明一个有限秩守恒律：
只要 Hodge Gram 来自 observation operator，任意 endpoint probe 都可由一个对偶
observation flow 表示；它与 canonical harmonic response 的 period 与 flow 的
具体代表无关。因此全局 Mertens current 可以精确搬运到有限个初始 unit cells。

对经典 zeta，文档 104 的 incidence--Vandermonde recovery 无条件保证这些有限
support cycles 存在。尚未证明的是它们的 signed harmonic periods 具有 RH 所需
速率；但这比估计每个 Mertens shell 更接近 Weil cohomology 中“cycle 对 harmonic
class 的 period”机制。

## 1. Observation Hodge duality

设 `V` 是有限维 coefficient space，`H` 是 observation Hilbert space，

`O:V -> H`, `W=O^*O>0`.                           (1)

给定 response covector `D in V`，定义其 normalized canonical vector 与 harmonic
observation flow

`v_D=W^(-1)D/C`, `C=D^*W^(-1)D`,                 (2)

`z_D=OW^(-1)D`.                                   (3)

对 probe `q in V`，称 `y in H` 是 dual cycle representative，若

`O^*y=q`.                                         (4)

### 定理 WI（dual-flow Hodge principle）

每个 `q` 的最小范数 representative 唯一且为

`y_q^min=OW^(-1)q`,                               (5)

并有

`||y_q^min||^2=q^*W^(-1)q`.                       (6)

对任意满足式 (4) 的 `y`，canonical period 都满足

`<z_D,y>=D^*W^(-1)q`.                             (7)

特别地，式 (7) 只依赖 cohomology covector `q`，不依赖 cycle representative。

#### 证明

式 (5) 满足 `O^*y_q^min=W W^(-1)q=q`。若 `O^*y=q`，则
`y-y_q^min in ker O^*=(ran O)^perp`，而 `y_q^min in ran O`，故 Pythagoras 给
其唯一最小性及式 (6)。同理 `z_D in ran O`，于是

`<z_D,y>=<OW^(-1)D,y>`

`        =D^*W^(-1)O^*y=D^*W^(-1)q`.             (8)

`□`

这是真正的 Hodge statement：`y_q^min` 是 covector `q` 的 harmonic cycle，添加
任意 exact-orthogonal component 不改变与 harmonic response 的 period。

## 2. Finite observation cycles

令 `P:V -> H_0` 是 `O` 的有限 observation subfamily，并假设 `P^*P>0`。定义

`y_q^[P]=P(P^*P)^(-1)q in H_0`,                   (9)

再把它以零延拓到 `H`。

### 定理 WJ（finite-cycle conservation law）

`P^*y_q^[P]=q`，故

`<z_D,y_q^[P]>=D^*W^(-1)q`.                       (10)

而且

`||y_q^[P]||^2=q^*(P^*P)^(-1)q`

`              >=q^*W^(-1)q=||y_q^min||^2`.      (11)

#### 证明

式 (9) 直接给 constraint。定理 WI 给式 (10)；最小范数性质给式 (11)。也可由
`P^*P<=O^*O=W` 的 inverse Loewner order 得式 (11)。`□`

因此长 Mertens sum 的跨尺度 cancellation 不是必须逐 shell 解释的概率现象：在
fixed-rank space 中，它受式 (10) 的有限 cycle conservation 强制。逐 shell 取
绝对值会破坏这个结构。

## 3. Polyhedral periods 与中心线

沿用文档 120 的 endpoint transform `T`、weights `c_j` 与 sign probes

`q_sigma=T^*diag(c)sigma`.                        (12)

对每个 sign 任选 dual cycle `y_sigma`，并定义其 canonical period

`Pi_sigma=<z_D,y_sigma>`.                         (13)

### 定理 WK（dual-cycle period Weil criterion）

exact leverage 为

`L_1(W,D)=C^(-1)max_sigma|Pi_sigma|.              (14)

所以在文档 094 的 fixed determinant setup 中，若

`c_1+|target| C^(-1)max_sigma|Pi_sigma|`

` =o(sqrt(log N)/loglog(3N)),`                    (15)

则 fixed principal strata 为 `o(1)`；连同完整 polarized Weil package 与总尾
公理即推出相应 zeta zeros 位于中心线。

如果一族 filtered packages 还具有 fixed finite observation subfamilies `P_N`，
且 `P_N^*P_N>0`，则式 (15) 可完全由 finitely supported cycles
`y_sigma^[P_N]` 检验。这构成一个广义的“positive observations + dual cycles +
small harmonic periods”中心线结构定理。

#### 证明

文档 120 定理 WC 给
`L_1=C^(-1)max_sigma|D^*W^(-1)q_sigma|`。定理 WI 把每个 mixed functional
替换成式 (13)，得到式 (14)。其余结论应用定理 WE 与抽象 polarized Weil
结构定理。有限 support statement 来自定理 WJ。`□`

单用 cycle norm 只能给

`|Pi_sigma|<=||z_D|| ||y_sigma||=sqrt(C)||y_sigma||`.(16)

对经典 fixed-prefix cycles，这回到文档 104--105 的 polylog coercivity bound，
仍达不到式 (15)。所需新信息必须是 signed period cancellation，而不是更粗的
cycle mass。

## 4. 经典 Möbius--Farey observation complex

在 spatial window `[0,N^2]`，令 `p_m` 是 unit-cell mean，`C_m` 是 cumulative
divisibility charge，并置

`theta_m=1/m-1/(m+1)-log^2(1+1/m)`.              (17)

定义 observation rows

`O_m=p_m` (`0<=m<N^2`),                           (18)

`O_(N^2+m-1)=sqrt(theta_m)C_m` (`1<=m<N^2`).      (19)

文档 103 命题 TZ 给 exact factorization

`O^*O=W_N^[0,N^2]`.                               (20)

文档 104 定理 UA--UC 进一步证明：对每个 fixed rank `R`，存在 fixed prefix
`P_N=(p_0,...,p_M)`，当 `N` 足够大时 `P_N^*P_N>0`。因此所有 endpoint sign
probes 都有无条件存在、support 位于前 `M+1` 个 cells 的 cycles。

结合文档 121 的 Mertens factorization，得到 exact three-way conservation law

`sum_(m<N)M(m)h_sigma(m)`

` =D^*W^(-1)q_sigma`

` =<OW^(-1)D,y_sigma^[P_N]>.                      (21)

式 (21) 把 Möbius prefix arithmetic、positive observation Hodge geometry 与有限
algebraic cycles 接在同一个等式中。这一结构对经典 zeta 的 fixed-rank sections
已无条件构造；开放问题是式 (15) 的 uniform period estimate，以及 growing-rank/
determinant tail 的控制。

## 5. Finite audit

`prefix mass` 是前缀 cells 捕获的 `||z_D||^2/C`；`sparse/min` 是式 (11) 两侧
cycle energies 的比。`R=2` 用 cells `0,...,3`，`R=3` 用 `0,...,5`。

| `N` | `R` | prefix response mass | sparse/min energy | exact mixed period |
|---:|---:|---:|---:|---:|
| 8 | 2 | 0.613 | 2.71 | -416.43 |
| 16 | 2 | 0.522 | 4.95 | -364.03 |
| 32 | 2 | 0.456 | 9.52 | -370.19 |
| 64 | 2 | 0.622 | 14.76 | -215.03 |
| 8 | 3 | 0.729 | 2.50 | -761.70 |
| 16 | 3 | 0.671 | 9.76 | -1007.47 |
| 32 | 3 | 0.554 | 49.65 | -298.40 |
| 64 | 3 | 0.554 | 134.60 | 2507.24 |

三种 mixed period 在 42-digit tolerance 内一致。前缀 response mass 并不趋于零，
但 sparse cycle energy 随 `N` 增长且局部 contributions 之间有大幅相消。这再次
说明 norm-only certificate 不足；应直接研究有限 incidence cycle 与 canonical
harmonic flow 的 signed period。

## 6. 计算实现

新增 `mobius_endpoint_sparse_observation_flow_certificate`。它构造式 (18)--(20)
的完整 observation matrix、有限前缀 cycle、全局 minimal cycle 与 canonical
response flow，并逐 phase 核对：

1. `W=O^*O`；
2. `P^*y_sigma=q_sigma`；
3. sparse period = minimal/direct period = Mertens current；
4. sparse cycle energy 不小于 harmonic minimum。

回归测试采用 50-digit arithmetic，并把所有 residual 控制在 `1e-42` 以下。

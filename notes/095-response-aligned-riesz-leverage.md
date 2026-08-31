# Response-aligned Riesz leverage 与 capacity-only no-go

文档 094 把 fixed determinant principal strata 的稳定性归结为 canonical
endpoint polynomial 的 weighted Riesz norm `R_N^*`。文档 086--087 则把
canonical mean-zero correction 写成 positive Gram/capacity projection。本节把
两者精确接起来，并证明一个重要的 no-go：capacity 或 correction energy
本身都不能控制 `R_N^*`。真正需要估计的是 response Riesz representer
`W^(-1)D` 在 endpoint coefficient coordinates 中的定向 leverage。

## 1. Jet coefficients 到 endpoint coefficients 的精确变换

取 correction polynomial

`P_alpha(u)=1-u+sum_(j=1)^R alpha_j u^j(1-u)`.       (1)

令 `v=1-u`，写

`P_alpha(1-v)=sum_(ell=1)^(R+1)q_ell v^ell`.        (2)

定义 `(R+1) times R` matrix

`E_(ell,j)=(-1)^(ell-1) binom(j,ell-1)`             (3)

当 `1<=ell<=j+1`，其余位置为零；并令
`e_1=(1,0,...,0)^T`。

### 定理 SQ（endpoint binomial transform）

有 exact identity

`q=e_1+E alpha`.                                    (4)

若正 weights `c_ell` 给 weighted endpoint norm

`||q||_(c,1)=sum_ell c_ell|q_ell|`,                 (5)

则单个 jet direction 的 elementary Riesz column mass 为

`sum_(ell=1)^(j+1)ell|E_(ell,j)|`

` =(j+2)2^(j-1)`.                                   (6)

#### 证明

由

`u^j(1-u)=(1-v)^jv`

` =sum_(k=0)^j(-1)^k binom(j,k)v^(k+1)`             (7)

逐列读出式 (3)--(4)。式 (6) 使用
`sum_k binom(j,k)=2^j` 与
`sum_k k binom(j,k)=j2^(j-1)`。`□`

式 (6) 已显示 degree 增长时的危险：Hilbert energy 很小的高阶 direction
仍可能在 endpoint coefficient norm 中付出 exponential binomial mass。

## 2. Minimum-metric projection 的定向 leverage

令 `W>0` 是 correction directions 的 Hodge Gram，`D` 是 boundary response，
`t` 是 target response。记

`C=D^*W^(-1)D`,  `v_D=W^(-1)D`.                    (8)

minimum-`W` correction 为

`alpha_min=t v_D/C`.                                (9)

定义 response-aligned Riesz leverage

`Lambda_c(W,D)=||Ev_D||_(c,1)/C`.                  (10)

再定义 endpoint inverse-capacity

`K_c(E,W)=sup_(|z_ell|<=c_ell)`

`                 z^*E W^(-1)E^*z`,               (11)

以及完全显式的 phase-box majorant

`K_c^#(E,W)=sum_(ell,k)c_ell c_k`

`                         *|(E W^(-1)E^*)_(ell,k)|`.(12)

### 定理 SR（capacity-to-Riesz interface）

式 (9) 产生的 endpoint polynomial 满足

`R_c(P_alpha)=||e_1+Ealpha_min||_(c,1)`

` <=c_1+|t|Lambda_c(W,D)`,                          (13)

且

`Lambda_c(W,D)<=sqrt(K_c(E,W)/C)`

`                 <=sqrt(K_c^#(E,W)/C)`.            (14)

这些量在 correction-direction basis 的任意可逆变换下保持不变，只要同时变换
`W,D,E`。

#### 证明

式 (13) 是式 (4)、(9) 与 triangle inequality。weighted `l^1` duality 给

`||Ev_D||_(c,1)=sup_(|z_ell|<=c_ell)|z^*Ev_D|`.     (15)

在 `W^(-1)` inner product 中用 Cauchy--Schwarz：

`|z^*EW^(-1)D|^2`

` <=(z^*EW^(-1)E^*z)(D^*W^(-1)D)`.                 (16)

除以 `C^2` 并取 supremum 给式 (14) 第一部分；逐 matrix entry 取绝对值给
第二部分。basis invariance 由 congruence transformation 直接验证。`□`

取文档 094 的 analytic weights `c_ell=C_ell^*`。因此 fixed determinant
稳定性的一个完全 finite、非谱隙型充分条件是

`c_1+|t_N|sqrt(K_(c,N)^#/C_N)`

`       =o(sqrt(log N)/loglog(3N)).`                 (17)

式 (17) 只要求 response-aligned inverse geometry，不要求
`lambda_min(W_N)` 有 uniform lower bound，因而避开文档 082 的 collision
no-go。

## 3. 含 base coupling 的完整 affine projection

真实 Nyman optimization 还包含文档 087 的 base coupling `h`。置

`v_h=W^(-1)h`,

`r=t+D^*W^(-1)h`,

`Gamma_c(W,h)=||Ev_h||_(c,1)`.                      (18)

### 定理 SS（affine Schur-to-Riesz bound）

定理 QQ 的 canonical coefficients

`alpha_*=-v_h+(r/C)v_D`                             (19)

满足

`R_c(P_(alpha_*))`

` <=c_1+Gamma_c(W,h)+|r|Lambda_c(W,D)`.             (20)

所以只要式 (20) 的右侧为
`o(sqrt(log N)/loglog(3N))`，文档 094 定理 SP 仍适用于完整 affine
mean-zero Nyman projection。

#### 证明

把式 (19) 代入式 (4)，对两个 transformed representers 分别使用 triangle
inequality；response 项再用定理 SR。`□`

这给出了从 actual Gram/Feshbach data 到 parabolic stability 的第一条精确
接口。它同时保留普通 residual coupling `h` 和 boundary response `D`；仅估计
其中一个不足以认证 canonical vector。

## 4. Capacity-only 控制严格不可能

### 定理 ST（fixed capacity and energy do not bound Riesz norm）

即使 direction count 固定为 `R=1`，也不存在只依赖 capacity `C` 与最小
correction energy `|t|^2/C` 的 endpoint Riesz norm 上界。

#### 证明

令 `0<epsilon<1`，并取

`W=[epsilon^2]`,  `D=[epsilon]`,  `t=1`,  `h=0`.    (21)

则

`C=D^*W^(-1)D=1`,

`alpha_min=1/epsilon`,

`alpha_min^*W alpha_min=1`.                         (22)

然而 `E=(1,-1)^T`，所以

`q=(1+epsilon^(-1),-epsilon^(-1))^T`.               (23)

对任意固定 positive weights，`||q||_(c,1)->infinity` 当
`epsilon->0`。因此 capacity 与 correction energy 保持常数仍不能阻止
coefficient explosion。`□`

这个 counterexample 不声称真实 Möbius Gram 必然退化成式 (21)；它证明的是
逻辑上不能从文档 086 的 capacity statement 单独推出文档 094 的 Riesz
threshold。必须证明式 (10)、(14) 或式 (20) 这类定向估计。

## 5. 有限尺度诊断

为区分代数恒等式与真实性能，先以 `W=I` 的试验 metric 计算文档 086 的
minimum-metric vector。下表列 elementary norm `sum ell|q_ell|`，括号内为它
除以文档 094 阈值 `sqrt(log N)/loglog(3N)` 的比值：

| `N` | `R=1` | `R=3` |
|---:|---:|---:|
| 30 | 6.667 (5.44) | 14.638 (11.94) |
| 300 | 4.648 (3.73) | 9.697 (7.79) |
| 3000 | 3.013 (2.35) | 7.395 (5.77) |
| 10000 | 4.699 (3.61) | 6.794 (5.22) |

这些数据既不单调，也没有显示所需 threshold；增加 directions 甚至可能因
binomial transform 增大 norm。由于 `W=I` 不是 actual fractional-part Gram，
该表不是反例，也不是 RH 证据。它只说明下一步应直接 enclosure
response-aligned quantities，而不应以 direction count 或 capacity monotonicity
作为替代指标。

## 6. 对广义结构的接口

定理 SR--SS 完全不使用 Möbius 函数。对任意 generalized Weil/Hodge synthesis，
只要：

1. `W` 是 correction polarization；
2. `D` 是 Tate/boundary response；
3. `E` 把 algebraic correction coordinates 映到控制 local Euler removal 的
   endpoint coordinates；

则 `Lambda_c(W,D)` 是从 positive Hodge geometry 到 arithmetic conductor
stability 的自然桥量。它比粗 condition number 更弱、更定向，也比 capacity
更强。经典 zeta 的下一项任务现在精确为：利用 actual fractional-part Gram
的 Farey/local decomposition，对式 (10) 或式 (14) 作 cofinal enclosure。

## 7. 计算实现

`scripts/qw_matrix.py` 新增：

- `endpoint_direction_riesz_transform`；
- `endpoint_riesz_projection_certificate`。

后者同时返回 exact endpoint coefficients、capacity、response/coupling
leverages、phase-box majorant、triangle certificate 与 correction energy。
回归测试核对 binomial transform、与直接 polynomial expansion 的一致性、
定理 SR 的两层 bounds，以及定理 ST 的 `epsilon=10^(-6)` counterexample。

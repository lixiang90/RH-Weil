# Localized leverage、response-anchor 不变性与 Loewner shortening

文档 095 证明 canonical endpoint stability 取决于 normalized response
representer

`v_(W,D)=W^(-1)D/(D^*W^(-1)D)`,                    (1)

而非 capacity 单独。本节把这个量接到文档 088 的 spatial positive blocks。
首先从 `y<=N` 的 complete jump formula 求出 Möbius jet directions 的 exact
local Gram；然后证明 boundary constant mode 对式 (1) 完全无效；最后给出
easy/hard Loewner sandwich 对 full leverage 的严格上界。

有限计算同时揭示一个新障碍：local Gram 虽正定，却不足以稳定高阶 endpoint
coordinates。要获得可用的 cofinal bound，easy metric 必须吸收额外的
oscillatory/Farey 正性。

## 1. Möbius endpoint jets 的 exact local Gram

固定 `N`，令

`q_j(n)=mu(n)u_n^j(1-u_n)`,

`u_n=log n/log N`, `1<=j<=R`.                       (2)

定义

`a_j=sum_(n<=N)q_j(n)/n`,

`c_j(m)=sum_(d|m)q_j(d)`,

`C_j(k)=sum_(m<=k)c_j(m)`.                          (3)

在 reciprocal coordinate 中置

`g_j(y)=sum_(n<=N)q_j(n){y/n}`.                     (4)

### 定理 SU（complete local jet Gram）

在 `0<y<1`，

`g_j(y)=a_jy`;                                      (5)

在 `k<=y<k+1`、`1<=k<N`，

`g_j(y)=a_jy-C_j(k)`.                               (6)

因此 local Hodge Gram

`W^loc_(j,l)=int_0^N g_j(y)conjugate(g_l(y))dy/y^2` (7)

有完全有限的闭式

`W^loc_(j,l)=a_j conjugate(a_l)`

` +sum_(k=1)^(N-1){a_j conjugate(a_l)`

`  -[a_j conjugate(C_l(k))+C_j(k)conjugate(a_l)]`

`       *log((k+1)/k)`

`  +C_j(k)conjugate(C_l(k))`

`       *(1/k-1/(k+1))}.`                           (8)

若 coefficient columns `q_j` 线性独立，则 `W^loc>0`。

#### 证明

式 (5)--(6) 是文档 088 定理 QW 对 target-free correction field 的版本：
连续斜率为 `a_j`，第 `m` 个整数处的 downward jump 为 `c_j(m)`。逐 interval
积分

`[a_j-C_j(k)/y]`

` *conjugate[a_l-C_l(k)/y]`                         (9)

得到式 (8)。若某 coefficient combination 的 local norm 为零，则对应
piecewise-linear field 几乎处处为零；依次读取整数 jumps 得其 low convolution
为零，Dirichlet convolution 的 triangular invertibility 再迫使全部原
coefficients 为零。故在 columns 独立时 Gram 正定。`□`

这给出一个不含 numerical quadrature、零点数据或 RH 假设的 actual Nyman
polarization block。

## 2. Boundary response rank-one anchor 完全不改变 canonical direction

令 `W>0,D!=0`，并对 `tau>=0` 定义

`W_tau=W+tau DD^*`.                                 (10)

### 定理 SV（response-anchor invariance）

若 `C=D^*W^(-1)D`，则

`C_tau=D^*W_tau^(-1)D=C/(1+tau C)`,                 (11)

但 normalized response representer 精确不变：

`W_tau^(-1)D/C_tau=W^(-1)D/C`.                     (12)

因而文档 095 的 response leverage `Lambda_c(W,D)` 也完全不变。

#### 证明

Sherman--Morrison identity 给

`W_tau^(-1)D=W^(-1)D/(1+tau C)`.                   (13)

左乘 `D^*` 得式 (11)，再相除即得式 (12)。`□`

这对文档 085 的 boundary zero mode 有直接含义：周期 constant-mode Gram
正是 response direction 上的 rank-one anchor。它会改变 capacity 与 constraint
energy，却不可能改善 canonical endpoint coefficients。真正能控制 leverage
的只能是 transversal oscillatory/local geometry。

## 3. Easy/hard relative leakage 的 Loewner bound

设 actual correction Gram 分解为

`W=W_e+W_h`, `W_e>0`, `W_h>=0`.                     (14)

定义最小的 relative leakage constant

`eta=lambda_max(W_e^(-1/2)W_hW_e^(-1/2))`,          (15)

所以

`W_e<=W<=(1+eta)W_e`.                               (16)

对 endpoint transform `E` 与 weights `c`，令 `C_e`、`K_(c,e)`、
`K_(c,e)^#` 分别为文档 095 式 (8)、(11)、(12) 用 `W_e` 计算的量。

### 定理 SW（localized response-leverage certificate）

full response leverage 满足

`Lambda_c(W,D)`

` <=sqrt((1+eta)K_(c,e)/C_e)`

` <=sqrt((1+eta)K_(c,e)^#/C_e)`.                    (17)

#### 证明

式 (16) 的 inverse Loewner order 是

`(1+eta)^(-1)W_e^(-1)<=W^(-1)<=W_e^(-1)`.          (18)

因此 full capacity `C_W` 满足

`C_e/(1+eta)<=C_W<=C_e`.                            (19)

另一方面

`EW^(-1)E^*<=EW_e^(-1)E^*`，                       (20)

所以文档 095 的 phase-box supremum 满足
`K_c(E,W)<=K_(c,e)`。把式 (19)--(20) 代入定理 SR 的
`Lambda_c<=sqrt(K_c/C_W)`，即得式 (17)。`□`

这个 certificate 不要求 full Gram 的 uniform spectral gap。它只要求选择一个
可逆 easy polarization，并控制 hard block 相对于它的 generalized eigenvalue。

## 4. 接到 fixed determinant 稳定性

### 推论 SX（localized polynomial-stability criterion）

对一列 minimum-metric mean-zero corrections，若存在 easy/hard decomposition
使

`c_1+|t_N|sqrt((1+eta_N)K_(c,e,N)^#/C_(e,N))`

` =o(sqrt(log N)/loglog(3N)),`                       (21)

则文档 094 的任意 fixed determinant principal window 贡献为 `o(1)`。

对完整 affine projection，还需加入文档 095 的 coupling 项。由同一
Cauchy--Schwarz 论证，

`Gamma_c(W,h)<=sqrt(K_(c,e)^# h^*W_e^(-1)h)`,       (22)

而

`|t+D^*W^(-1)h|`

` <=|t|+sqrt(C_e h^*W_e^(-1)h)`.                    (23)

把式 (22)--(23) 与式 (17) 代入定理 SS，得到一个只含 easy inverse 与
relative leakage 的完全有限充分条件。

#### 证明

第一部分直接组合定理 SW 与文档 095 定理 SR、文档 094 定理 SP。式 (22)
使用 `W^(-1)<=W_e^(-1)` 与 endpoint phase-box duality；式 (23) 对
`D^*W^(-1)h` 用 `W^(-1)`-Cauchy--Schwarz，再用式 (18) 的上界。`□`

## 5. Local-only easy metric 的有限审计

用定理 SU 的 exact `W^loc` 作 `W_e`，下表列 capacity、exact elementary
response leverage，以及 `W^loc` 的最小本征值：

| `N` | `R` | `C_loc` | `Lambda_loc` | `lambda_min(W_loc)` |
|---:|---:|---:|---:|---:|
| 30 | 1 | 2.895 | 5.132 | `1.18e-1` |
| 30 | 2 | 3.278 | 89.31 | `2.21e-4` |
| 30 | 3 | 5.356 | 936.0 | `7.74e-6` |
| 100 | 1 | 2.956 | 5.858 | `8.87e-2` |
| 100 | 2 | 2.981 | 16.66 | `2.71e-4` |
| 100 | 3 | 8.740 | 827.3 | `1.20e-5` |
| 1000 | 1 | 2.502 | 8.402 | `5.10e-2` |
| 1000 | 2 | 9.050 | 133.5 | `2.34e-4` |
| 1000 | 3 | 30.81 | 494.1 | `1.33e-5` |

这些是 finite high-precision diagnostics，不是渐近定理。它们给出两个可靠的
方向判断：

1. local Gram 的正定性确实能被 exact jump arithmetic 认证；
2. 对 `R>=2`，只用 local block 的 inverse endpoint geometry 极差，远大于
   文档 094 的阈值。

所以把全部 parabolic/far blocks 仅当 `W_h`、再用很大的 `eta`，预计不会
闭合。下一步必须扩大 easy metric，吸收至少一部分 Farey oscillatory positive
geometry；constant response anchor 由定理 SV 已知无效。需要寻找的是
transversal oscillatory block 的正 shorting，而不是继续强化 zero mode。

## 6. 广义 Hodge 解释

定理 SV--SW 对任意 polarized synthesis 都成立。它把 boundary/Tate direction
分成两类正结构：

- 沿 functional 本身的 rank-one polarization 只改变 constraint energy；
- 横向 polarization 才改变 normalized algebraic representative，并可能控制
  local Euler coordinates。

因此 generalized Weil structure 的存在性不能只由一个 Tate capacity 保证；
还需要 polarization 在 arithmetic endpoint map `E` 所见方向上的横向
coercivity。定理 SW 给出了这种 coercivity 的可拼接、finite-dimensional
证书。

## 7. 计算实现

`scripts/qw_matrix.py` 新增：

- `mobius_endpoint_direction_local_gram`；
- `localized_endpoint_riesz_leverage_certificate`。

回归测试把定理 SU 的 Gram quadratic form 与正负 polarization 得到的 direct
local energy 比较；核对定理 SW 的 full leverage bound；并验证给 metric 加上
`tau DD^*` 后 canonical coefficients 与 leverage 按定理 SV 精确不变。

# Incidence--Vandermonde recovery 与无条件 polylog Hodge coercivity

文档 103 把 actual Schur-short positivity 归约为 Möbius unit-cell means 的 finite
determinant frame。本节对该 frame 给出第一个无条件渐近 lower bound。关键是
cell means 可经相邻差分恢复 divisor-sum charges，再由 divisibility incidence
algebra 的 Möbius inversion 恢复若干原始 endpoint directions。选取固定的
distinct squarefree nodes 后，这些 recovered rows 是缩放 Vandermonde matrix。

结论是：对每个 fixed direction count `R`，经典 zeta 的 actual finite spatial
metric 无条件含有强度

`sigma_N>=c_R(log N)^(-2R)`                         (1)

的 transversal Hodge block，其中 `c_R>0` 显式可计算。这证明了一个真实的
quantitative structure-existence statement；但式 (1) 尚不足以单独达到文档 102
的 centerline rate，因此不构成 RH 证明。

## 1. Cell means 与 divisor charges

令 `L=log N`、`u_n=log(n)/L`。对 `j=1,...,R` 定义 endpoint direction

`r_n(j)=mu(n)(1-u_n)u_n^j`.                        (2)

令 direction-wise slope vector 为

`s=sum_(n<=N)r_n/n`,                               (3)

并定义 cumulative divisibility charge

`C_m=sum_(k<=m)sum_(n|k)r_n`

`   =sum_(n<=N)r_n floor(m/n)`.                    (4)

文档 103 的 unit-cell mean vector 为

`p_0=s`,

`p_m=s-ell_m C_m`, `ell_m=log(1+1/m)` (`m>=1`).    (5)

令 one-step divisor charge

`q_m=C_m-C_(m-1)=sum_(n|m)r_n`.                    (6)

### 定理 UA（cell-to-incidence exact recovery）

由 cell vectors 可精确恢复

`C_m=(p_0-p_m)/ell_m`,                             (7)

`q_1=(p_0-p_1)/ell_1`,                             (8)

`q_m=(p_0-p_m)/ell_m-(p_0-p_(m-1))/ell_(m-1)`      (9)

以及

`r_n=sum_(d|n)mu(n/d)q_d`.                         (10)

因此，对任意 finite node set `S={n_1,...,n_k}`，存在只依赖于 `S`、不依赖于
`N` 的显式 recovery matrix `T_S`，使

`T_S[p_0;p_1;...;p_M]=[r_(n_1);...;r_(n_k)]`,      (11)

其中 `M=max S`。

#### 证明

式 (7)--(9) 直接重排式 (5)。式 (6) 是 divisor zeta transform
`q=1*r`；其 incidence inverse 是 ordinary Möbius function，故得式 (10)。把
这些固定 linear operations 合成即为 `T_S`。`□`

这个 recovery 不使用零点、PNT 或 cancellation estimate，只使用 divisibility
incidence algebra 的 exact invertibility。

## 2. Finite recovery coercivity

取 `k=R` 个 distinct squarefree nodes `n_i<N`，令 `P_M` 是 rows
`p_0,...,p_M` 组成的 `(M+1) x R` matrix。定义 recovered matrix

`D_N=T_SP_M`.                                       (12)

由式 (2)，

`D_N(i,j)=mu(n_i)(1-log(n_i)/L)`

`                         *(log(n_i)/L)^j`.         (13)

它是 row-scaled Vandermonde matrix，因而可逆。

### 定理 UB（finite incidence--Vandermonde coercivity）

令 `B` 为 endpoint mass，`beta_R=lambda_max(B)`。则 prefix cell Gram
`bar W_M=P_M^*P_M` 满足

`bar W_M>=gamma_(N,S) B`,                           (14)

其中

`gamma_(N,S)=sigma_min(D_N)^2/(||T_S||^2 beta_R)`. (15)

同一个 bound 适用于 prefix shorted metric，并进一步适用于 actual
`W^[0,N^2]` 的 shorted coercivity：

`sigma_N>=gamma_(N,S)>0`.                           (16)

#### 证明

由式 (12)，对任意 coefficient vector `x`，

`||D_Nx||<=||T_S|| ||P_Mx||`.                      (17)

故 `P_M^*P_M>=sigma_min(D_N)^2||T_S||^(-2)I`；再用
`B<=beta_RI` 得式 (14)。在 adapted coordinates `[v_B,Z]` 中，

`B~diag(1/C_B,B_0)`.                               (18)

Loewner shorting 保序，所以式 (14) 的 response-line Schur complement 给
`bar S_M>=gamma_(N,S)B_0`。prefix projected Gram、prefix actual Gram 与
`W^[0,N^2]` 的差依次均为 PSD；文档 102 定理 TU 的 shorted superadditivity
把同一 lower bound 传播到 full spatial short，得到式 (16)。`□`

这给出了 actual transversal block 的严格 algebraic existence proof，而不仅是
finite numerical positivity。

## 3. Fixed-node polylog theorem

固定 squarefree nodes `S={n_1,...,n_R}`，令

`V_S(i,j)=mu(n_i)(log n_i)^j`, `1<=i,j<=R`.         (19)

因 `log n_i` distinct 且非零，

`det V_S=(product_i mu(n_i)log n_i)`

`        *product_(i<k)(log n_k-log n_i)!=0`.       (20)

### 定理 UC（unconditional polylog transversal polarization）

若

`log N>=2 max_i log n_i`,                           (21)

则

`sigma_N>=c_(R,S)(log N)^(-2R)`,                   (22)

其中显式常数

`c_(R,S)=lambda_min(V_S^*V_S)`

`          /(4||T_S||^2 lambda_max(B))>0`.         (23)

特别地，对每个 fixed `R`，可固定最前面的 `R` 个 squarefree integers，得到
只依赖 `R` 的 `c_R>0`，从而证明式 (1)。

#### 证明

把式 (13) 写成

`D_N=A_N diag(L^(-1),...,L^(-R))`,                 (24)

其中

`A_N=diag(1-log(n_i)/L)V_S`.                       (25)

式 (21) 保证左侧 diagonal factors 至少为 `1/2`，故

`sigma_min(A_N)>=sigma_min(V_S)/2`.                (26)

又 `L>=1` 时式 (24) 右侧 diagonal matrix 的最小 singular value 为
`L^(-R)`。所以

`sigma_min(D_N)^2>=lambda_min(V_S^*V_S)L^(-2R)/4`. (27)

代入定理 UB 即得式 (22)--(23)。`□`

这是真正的 asymptotic existence theorem：不需要猜测 Möbius cancellation，甚至
只使用 fixed initial cells。full cell frame 的其余 `N^2-O_R(1)` rows 只会增强
positivity。

## 4. 抽象 incidence--Vandermonde Hodge theorem

上述证明并不依赖 divisibility 以外的特殊分析性质，可以抽象如下。

### 定理 UD（incidence-recoverable Hodge existence）

设一个 filtered Euler--Tate package 具有：

1. locally finite incidence algebra `I`，其 zeta transform 可逆，inverse 为
   `mu_I`；
2. positive observation Gram `P_N^*P_N`；
3. fixed selected atoms `S`，存在 bounded finite recovery
   `T_SP_N=D_N`；
4. endpoint polarization `B_N>0`；
5. recovered evaluation matrix `D_N` 满列秩。

则 observation Gram 含有 endpoint polarization，强度至少为

`sigma_min(D_N)^2/(||T_S||^2lambda_max(B_N))`.      (28)

其 response-zero shorted form 含有同强度的 canonical transversal block。若
该 lower bound 与 package 的 capacity/forcing scalars 一同满足文档 102 定理 TV
的 rate，则对应 zeta zeros 位于中心线。

#### 证明

前三项给 exact recovery；对式 (17) 重复 singular-value argument 得 full
Loewner lower bound。第四项把 Euclidean bound 转成 `B_N`-bound；shorting
保序给 transversal block。最后应用定理 TV。`□`

定理 UD 抽取了 Weil-style existence 的一个纯代数核心：incidence inversion
提供 cycle recovery，Vandermonde/nondegenerate evaluations 提供 finite
intersection positivity，而 quantitative singular value 决定是否达到 purity
或 centerline rate。

## 5. Numerical audit

下表选 `R=2` 的 nodes `[2,3]`、`R=3` 的 nodes `[2,3,5]`。`gamma` 是定理 UB
的 exact finite bound，`sigma_prefix` 是相应 fixed prefix unit-frame 的直接
coercivity，`scaled=gamma(log N)^(2R)`。

| `N` | `R` | `gamma` | `sigma_prefix` | `gamma/sigma_prefix` | `scaled` |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | `1.12e-6` | `5.57e-6` | 0.202 | `3.16e-5` |
| 10 | 3 | `3.21e-9` | `4.18e-8` | 0.0767 | `4.78e-7` |
| 100 | 2 | `1.32e-7` | `9.52e-7` | 0.139 | `5.95e-5` |
| 100 | 3 | `1.69e-10` | `1.48e-9` | 0.114 | `1.61e-6` |
| 1000 | 2 | `3.08e-8` | `2.45e-7` | 0.126 | `7.02e-5` |
| 1000 | 3 | `2.01e-11` | `2.01e-10` | 0.100 | `2.19e-6` |

定理 UC 的 conservative constants 对这两个 choices 分别为约
`1.16e-5` 与 `9.26e-8`。exact scaled bounds 更大，符合式 (22)。

## 6. 为什么这仍未证明 RH

把式 (22) 单独代入文档 102 定理 TV，在不额外控制
`aC_W-1` 的情况下，Riesz upper bound 最坏增长如 `(log N)^R`；而文档 094
所需阈值约为 `sqrt(log N)/loglog N`。所以 fixed-node positivity 证明了结构
存在，却没有证明其强度足以迫使中心线。

剩余路线现在有三个严格选项：

1. 利用全部 unit cells 而非 fixed prefix，证明 `sigma_N` 比
   `(log N)^(-2R)` 强得多；
2. 联合证明 forcing factor `aC_W-1` 的 compensating decay；
3. 不用 worst-direction `sigma_N`，直接估计文档 102 的 forcing-weighted
   shorted spectral second moment。

这一区分很重要：本节解决了“positive algebraic structure 是否存在”的一部分，
但 centerline 需要更强的 quantitative purity。

## 7. 计算实现

`scripts/qw_matrix.py` 新增
`mobius_cell_vandermonde_recovery_certificate`。它构造 fixed prefix cell matrix、
相邻-charge/Möbius recovery operator、recovered 与 expected Vandermonde rows、
exact singular-value lower bound，以及式 (23) 的 `N`-independent constant。

回归测试核对 `T_SP_M=D_N` 的逐项 exact identity、finite coercivity lower bound、
式 (21) 的有效域，以及 exact bound 对 analytic polylog lower bound 的支配。

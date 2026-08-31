# Exact parabolic spatial Gram 与 far-completed leverage certificate

文档 096 证明 local-only Gram 不足以控制高阶 endpoint leverage，并指出应把
Farey oscillatory 正性纳入 easy metric。本节完成这一步的有限形式：由于
finite fractional-part field 在每个整数区间上仍是线性的，整个
`0<y<N^2` local+parabolic correction Gram 都可由有限 divisor jumps 精确求出。
剩余 `y>=N^2` block 则由文档 088 的 periodic Parseval Loewner majorant 控制。

因此 actual infinite Nyman correction Gram 的 response leverage 被化成一个
完全有限的 generalized-eigenvalue certificate，唯一未数值固定的是 continuous
large-sieve 的 absolute constant。有限审计显示 far completion 很小；高阶
leverage 的退化已经存在于 `0<y<N^2` 内部。

## 1. 任意整数窗口的 exact spatial Gram

沿用文档 096 的 endpoint directions `q_j(n)`、slopes `a_j`、low convolutions
`c_j(m)` 与 cumulative jumps `C_j(k)`。对整数

`0<=L<U`                                             (1)

定义

`W^[L,U]_(j,l)=int_L^U g_j(y)conjugate(g_l(y))dy/y^2`.(2)

### 定理 SY（complete finite-window jump Gram）

若 `L=0`，区间 `(0,1)` 对式 (2) 的贡献为
`a_j conjugate(a_l)`。其余每个整数 interval `k<=y<k+1` 的贡献为

`a_j conjugate(a_l)`

` -[a_j conjugate(C_l(k))+C_j(k)conjugate(a_l)]`

`       *log((k+1)/k)`

` +C_j(k)conjugate(C_l(k))`

`       *(1/k-1/(k+1)).`                            (3)

把式 (3) 对 `max(1,L)<=k<U` 求和即得 `W^[L,U]`。特别地，

`W^[0,N^2]=W^loc+W^par`                             (4)

是 actual Nyman correction Gram 在 local 与全部 parabolic spatial blocks 上
的精确和，并有 window additivity

`W^[L,U]+W^[U,V]=W^[L,V]`.                          (5)

#### 证明

对任意 `k`，有限 support field 仍满足

`g_j(y)=a_jy-C_j(k)`                                (6)

在 `k<=y<k+1`；这里

`c_j(m)=sum_(d|m,d<=N)q_j(d)`                       (7)

即使 `m>N` 也仍是完全有限的 divisor sum。把式 (6) 代入式 (2)逐 interval
积分，得到式 (3)。区间互不相交，故式 (5)成立；取分点 `N` 给式 (4)。`□`

这一步没有 Fourier truncation：所有 parabolic Farey collisions 已经通过同一
piecewise field 的平方范数被完整保留。

## 2. Endpoint directions 的 exact periodic Parseval Gram

对每个 direction 定义 boundary response 与 conductor amplitude

`D_j=sum_(n<=N)q_j(n)`,

`A_j(r)=sum_(r|n,n<=N)q_j(n)r/n`.                   (8)

令

`delta(r)=product_(p|r)(1-p^(-2))`.                 (9)

### 定理 SZ（periodic transversal correction Gram）

endpoint jet fields 在共同周期上的 mean-square Gram 是

`W^per_(j,l)=D_j conjugate(D_l)/4`

` +(1/12)sum_(r<=N)delta(r)`

`                   *A_j(r)conjugate(A_l(r)).`      (10)

它是 PSD；第一项是 pure response rank one，第二项是按 reduced Farey
denominator 正交直和的 transversal oscillatory Gram。

#### 证明

文档 085 定理 QB 给每个 direction 的 reduced-denominator Fourier expansion。
constant coefficient 是 `D_j/2`；固定 `r` 的全部 primitive harmonics 的
平方和由定理 QC 给 `delta(r)A_j(r)conjugate(A_l(r))/12`。不同 reduced
frequencies 在共同周期正交，求和即得式 (10)。`□`

由文档 096 定理 SV，式 (10) 的 rank-one 第一项本身不改变 normalized
response representer；真正可能 regularize endpoint coordinates 的是第二项。

## 3. 用 periodic Gram 完成 infinite far block

记

`W^sp=W^[0,N^2]`,

`W^far=int_(N^2)^infinity g(y)^*g(y)dy/y^2`,

`W=W^sp+W^far`.                                     (11)

文档 088 定理 QZ 给某个 absolute constant `C_LS`：

`0<=W^far<=(C_LS/N^2)W^per`.                        (12)

定义 fully finite relative majorant

`eta_N^#=lambda_max((W^sp)^(-1/2)`

`              *((C_LS/N^2)W^per)(W^sp)^(-1/2)).`  (13)

并令 `C_sp` 与 `K_(c,sp)^#` 是文档 095 的 capacity 和 phase-box quantity
用 `W^sp` 计算的值。

### 定理 TA（far-completed finite leverage certificate）

actual infinite Gram 的 response leverage 满足

`Lambda_c(W,D)`

` <=sqrt((1+eta_N^#)K_(c,sp)^#/C_sp).`              (14)

因此若

`c_1+|t_N|sqrt((1+eta_N^#)K_(c,sp)^#/C_sp)`

` =o(sqrt(log N)/loglog(3N)),`                       (15)

则任意 fixed reduced-determinant principal window 的 contribution 为 `o(1)`。

#### 证明

由式 (12)--(13)，actual hard block 满足

`W^far<=eta_N^# W^sp`.                              (16)

对 `W_e=W^sp,W_h=W^far` 应用文档 096 定理 SW 得式 (14)。再组合文档
095 定理 SR 与文档 094 定理 SP，得到式 (15) 的结论。`□`

式 (13)--(15) 是一套真正 finite certificate：`W^sp` 由式 (3) 的有限 sums
给出，`W^per` 由式 (10) 给出，所有 inverse 与 generalized eigenvalues 都是
finite positive linear algebra。它没有把 RH 藏进 Gram positivity；未证的是这些
finite quantities 的 cofinal asymptotic。

## 4. 有限审计：far block 很小，但 spatial leverage 仍退化

下表把 `C_LS` 暂归一为 `1`，列出 `W^sp` 的 response leverage、式 (13) 的
relative far factor 以及式 (14) 的 phase-box upper bound：

| `N` | `R` | `Lambda_sp` | `eta_N^#` | localized upper |
|---:|---:|---:|---:|---:|
| 10 | 1 | 4.773 | `7.57e-3` | 4.791 |
| 10 | 2 | 103.8 | `2.73e-2` | 175.7 |
| 10 | 3 | 371.2 | `3.62e-2` | 2325 |
| 30 | 1 | 5.132 | `9.96e-4` | 5.135 |
| 30 | 2 | 44.95 | `9.65e-3` | 198.4 |
| 30 | 3 | 788.4 | `1.37e-2` | 1321 |
| 100 | 1 | 5.858 | `1.31e-4` | 5.858 |
| 100 | 2 | 19.12 | `2.81e-3` | 200.8 |
| 100 | 3 | 737.6 | `3.89e-3` | 953.4 |

`C_LS=1` 只用于观察尺度，不能替代定理 QZ 的真实 absolute constant。不过
`eta_N^#` 已带显式 `N^(-2)`，样本清楚地区分了两个现象：

- far periodic completion 相对 `W^sp` 很小；
- `R>=2` 的 response leverage 在完整 local+parabolic spatial metric 中仍很大。

所以高阶退化不是丢弃 `y>=N^2` 造成的。它来自 finite parabolic Hodge Gram
内部的低谱 endpoint alignment。下一步应对 `W^sp` 本身作 spatial-shell 或
Farey-determinant Feshbach shorting，识别哪些高阶 jet combinations 同时具有
小 spatial energy 与大 endpoint binomial mass。

## 5. 与广义 Weil/Hodge 结构的关系

定理 SY--TA 抽象出一个可移植的“finite carrier + periodic completion”模块：

1. algebraic corrections 在 bounded carrier 上有 exact positive Gram；
2. infinite tail 被一个 finite periodic/orbit Gram Loewner majorize；
3. relative generalized eigenvalue 把 tail completion 接回 normalized response
   representative；
4. endpoint map 再把该 representative 接到 local Euler/conductor stability。

这比直接假设 infinite polarization 可逆更弱，也比只验证 finite positivity
更强。对经典 zeta，全部对象现已有限显式；剩余问题是它们的 uniform arithmetic
geometry，而不是结构的 finite existence。

## 6. 计算实现

`scripts/qw_matrix.py` 新增：

- `mobius_endpoint_direction_spatial_gram`；
- `mobius_endpoint_direction_periodic_gram`；
- `nyman_endpoint_spatial_far_certificate`。

原 `mobius_endpoint_direction_local_gram` 现在是 spatial routine 在 `[0,N]`
上的 wrapper。回归测试核对 window additivity、periodic Gram 与 direct Farey
Parseval energy 的一致性，以及 far-completed localized certificate。

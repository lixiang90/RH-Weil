# Endpoint-polynomial Riesz 稳定性与 mean-zero 修正阈值

文档 093 已证明线性 Möbius filter 的每个固定 reduced-determinant
principal sector 都是 `o(1)`。本节处理那里留下的第三个问题：canonical
mean-zero Hodge projection 会把线性 endpoint filter 改成高阶多项式，而其
系数可能依赖 `N`。核心结论是：删除有限 Euler factors 的稳定性并不局限于
一阶 logarithmic Riesz sum；所有高阶矩都满足足够强的统一界。因此，固定
determinant 结论对 endpoint polynomial 稳定，所需且可审计的量只是一个
带矩常数的 Riesz 系数范数。

这仍不是 RH 的证明。canonical projection 在每个有限 `N` 上存在，但目前
没有证明它产生的多项式族满足本节给出的统一范数阈值。

## 1. 高阶 logarithmic Riesz hierarchy

对整数 `j>=1` 定义

`G_j(X)=sum_(n<=X)mu(n)/n [log(X/n)]^j`,            (1)

并仍记

`m(t)=sum_(n<=t)mu(n)/n`.                           (2)

### 定理 SM（higher Riesz moment bound）

存在只依赖 `j` 的常数 `C_j`，使所有 `X>=1` 满足

`|G_j(X)|<=C_j(1+log X)^(j-1)`.                    (3)

更具体地，若

`C_0=int_1^infinity |m(t)|dt/t<infinity`,           (4)

则可取 `C_j=jC_0` 并把式 (3) 的右侧改成
`jC_0(log X)^(j-1)`（`X=1` 按连续约定理解）。

#### 证明

有限 Abel summation 给 exact identity

`G_j(X)=j int_1^X m(t)[log(X/t)]^(j-1)dt/t`.        (5)

文档 093 定理 SG 所用的无条件 PNT 级 zero-free region 给式 (4)。又因
`0<=log(X/t)<=log X`，对式 (5) 取绝对值即得更强的显式版本，因而得到
式 (3)。这里没有使用 RH。`□`

一阶情形正是定理 SG；高阶增长只来自 endpoint logarithm 的次数，而不是
新的 zeta 零点输入。

## 2. Local Euler-factor removal 对每一阶都稳定

置

`T_(r,j)(X)=sum_(m<=X,(m,r)=1)mu(m)/m`

`                         *[log(X/m)]^j`.           (6)

令 `D(r)` 表示全部 prime factors 均整除 `r` 的正整数集合。

### 定理 SN（higher local-smooth convolution）

对所有 `r>=1,j>=1,X>=1`，有

`T_(r,j)(X)=sum_(d in D(r),d<=X)G_j(X/d)/d`.        (7)

因此

`|T_(r,j)(X)|`

` <=C_j(1+log X)^(j-1)`

`   *product_(p|r)(1-p^(-1))^(-1).`                (8)

#### 证明

restricted Möbius coefficient identity

`mu(n)1_((n,r)=1)`

` =sum_(dk=n,d in D(r))mu(k)`                       (9)

是文档 093 式 (10) 的 coefficient form。把式 (9) 代入式 (6)，并观察
`log(X/(dk))=log((X/d)/k)`，交换有限和便得到式 (7)。定理 SM 与
`sum_(d in D(r))1/d=product_(p|r)(1-p^(-1))^(-1)` 给式 (8)。`□`

## 3. Endpoint polynomial 的 exact conductor formula

令

`P(u)=sum_(k=0)^R p_k u^k`, `P(1)=0`,              (10)

并在 endpoint coordinate `v=1-u` 中写成

`P(1-v)=sum_(j=1)^R q_j v^j`.                      (11)

对应 Möbius mollifier 与 conductor amplitude 为

`b_(N,P)(n)=mu(n)P(log n/log N)`,

`A_(N,P)(r)=sum_(r|n,n<=N)b_(N,P)(n)r/n`.          (12)

为允许 degree 随 `N` 增长，定义 analytic Riesz norm

`R_*(P)=sum_(j=1)^R C_j^* |q_j|`,                  (13)

其中可取 `C_j^*=2^(j-1)C_j`。固定 degree 时它与 elementary coefficient
norm `R(P)=sum_j j|q_j|` 等价；degree 增长时必须保留式 (13) 的 weights，
不能把依赖 `j` 的常数藏进一个所谓 absolute implied constant。

### 定理 SO（endpoint-polynomial conductor stability）

对 `N>=3` 与 squarefree `1<=r<=N`，有 exact identity

`A_(N,P)(r)=mu(r)sum_(j=1)^R q_j/(log N)^j`

`                         *T_(r,j)(N/r)`,           (14)

以及 uniform bound

`|A_(N,P)(r)|<=R_*(P)/log N * r/phi(r).`           (15)

非 squarefree `r` 时 `A_(N,P)(r)=0`。

#### 证明

在式 (12) 中写 `n=rm`。若 `r` squarefree，则
`mu(rm)=mu(r)mu(m)` 当且仅当 `(m,r)=1`，否则为零。令 `X=N/r`，则

`1-log(rm)/log N=log(X/m)/log N`。

代入式 (11)即得式 (14)。由定理 SN、`X<=N`、`log N>1`，第 `j` 项在
取绝对值后至多为

`C_j |q_j| (1+log X)^(j-1)/(log N)^j *r/phi(r)`

` <=C_j^*|q_j|/log N *r/phi(r)`。

求和得到式 (15)。若 `r` 非 squarefree，每个 `r` 的 multiple 的 Möbius
值都为零。`□`

使用定理 SM 的显式强版本还可把 `C_j^*` 取为 `jC_0`；式 (13) 的较保守
写法便于把同一论证移植到只知道 `(1+log X)^(j-1)` bounds 的一般 reciprocal
Euler algebra。

## 4. 固定 determinant sector 对高阶修正的稳定阈值

令 `P_N` 是任意可能随 `N` 变化、满足 `P_N(1)=0` 的 polynomial family，
并记 `R_N^*=R_*(P_N)`。沿用文档 093 的 principal shared-GCD modes、smooth
parabolic shells 与 `L_N=max_(n<=N)n/phi(n)`。

### 定理 SP（fixed-determinant polynomial stability）

对每个固定 `D>=1`，全部 `0<|delta|<=D` principal modes 的总贡献满足

`|C_(N,P_N)^(principal,0<|delta|<=D)|`

` <<_D (R_N^*)^2 L_N^2/log N`.                     (16)

特别地，充分条件

`R_N^*=o(sqrt(log N)/loglog(3N))`                  (17)

保证每个固定 determinant window 的贡献趋于零。

#### 证明

文档 093 推论 SL 的证明只在两处使用 mollifier 的具体形式：每个 conductor
amplitude 的统一界，以及两个 amplitudes 的 shared-`g` local losses。
把定理 SH 的线性 bound 换成式 (15)，定理 SJ 的 exact cancellation
`theta(g)(g/phi(g))^2<=1` 完全不变；两个 amplitudes 只额外产生
`(R_N^*)^2`。定理 SI 的 inverse-residue row bound 与其 fixed-`delta`
推广也不依赖 `P_N`。故文档 093 式 (26) 的同一 dyadic summation给式 (16)。
最后用 `L_N<<loglog(3N)` 即得式 (17)。`□`

## 5. 对 canonical mean-zero Hodge correction 的含义

文档 086--087 的 finite-dimensional projection 在每个 `N` 上都产生唯一
minimum-energy correction；文档 093 尚不能处理它，是因为 projection
coefficients 可能随 `N` 放大。定理 SP 把这个模糊的稳定性问题变成一个明确
数值目标：证明所得 endpoint expansion 的 `R_N^*` 满足式 (17)。

因此当前逻辑边界是：

- finite `N` 的 mean-zero polynomial correction 无条件存在；
- 若其 weighted Riesz norm 满足式 (17)，则所有固定 determinant principal
  strata 仍为 `o(1)`；
- 目前既没有式 (17) 的 uniform capacity estimate，也没有控制 growing
  determinant tail 与 nonprincipal additive modes，所以不能由此宣称 RH。

对一般 reciprocal Euler coefficients，同样可以把定理 SM、SN替换为“高阶
base Riesz bounds + local removal convolution”公理；再加 shared-factor
density absorption，即得到相同的 endpoint-polynomial stability module。这是
广义 Weil/Hodge 结构中一个可独立验证的局部组成部分。

## 6. 计算实现

`scripts/qw_matrix.py` 新增：

- `mobius_logarithmic_riesz_moment`；
- `coprime_mobius_logarithmic_riesz_moment`；
- `local_smooth_convolution_riesz_moment`；
- `endpoint_polynomial_riesz_data`；
- `polynomial_conductor_amplitude_via_riesz`。

回归测试核对 `j=1,2,3` 的 exact local-smooth convolution、endpoint expansion
`1+2u-3u^2=4v-3v^2` 及其 elementary norm `10`，并把式 (14) 与从有限
mollifier coefficients 直接计算的 conductor amplitude 比较。

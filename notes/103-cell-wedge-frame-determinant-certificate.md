# Cell wedge frame、Cauchy--Binet minors 与 shorted coercivity

文档 102 把经典 RH 路线中剩余的 finite obstruction 收缩为 actual spatial metric
的 Schur-short coercivity `sigma`。本节把 `sigma` 再转写成显式 determinant
frame。核心是：消去 response line 后的 shorted form，正是 response field 与
null fields 的两点 Plücker wedges 的平方积分。对空间作有限分块并取 conditional
means，就得到完全有限、严格位于 actual shorted form 之下的 rank-one frame。

在 Möbius--Farey spatial metric 中，取全部整数 unit cells 时，这个只用 cell
means 的 frame 已捕获测试样本中 `98.9%--99.7%` 的 actual coercivity。未捕获
部分又有一个精确的 positive cumulative-charge formula。因此剩余存在性输入可
表述为 explicit cell-minor frame lower bound，而不再是抽象 Gram gap。

## 1. Two-point wedge identity

令 `Phi(y) in C^R` 是 arithmetic field，采用 Gram convention

`W=int Phi(y)Phi(y)^*dy`.                            (1)

沿用文档 102 的 `v_B,Z`，定义

`b(y)=v_B^*Phi(y)`, `z(y)=Z^*Phi(y)`,               (2)

`a=int|b|^2`, `H=int zz^*`, `h=int z conjugate(b)`. (3)

于是 `S_0=H-hh^*/a`。

### 定理 TW（Plücker covariance identity）

令

`omega(y,x)=b(y)z(x)-b(x)z(y)`.                    (4)

则有 exact identity

`S_0=(1/(2a)) int int omega(y,x)omega(y,x)^* dydx`.(5)

特别地，`S_0>0` 当且仅当不存在非零 null direction `u` 使 scalar fields
`u^*z(y)` 与 `b(y)` 几乎处处成比例。

#### 证明

展开 double integral。两个 diagonal terms 各给 `aH`；两个 cross terms 各给
`hh^*`，故右侧为 `H-hh^*/a`。对任意 `u` 取 quadratic form，式 (5) 是
nonnegative scalar integral；其为零当且仅当所有 wedges
`b(y)u^*z(x)-b(x)u^*z(y)` 几乎处处为零，即两 scalar fields 成比例。`□`

这说明 shorting 本质上是 response/null 两通道的 projective variation；单独
控制任一通道的大小都看不到它。

## 2. Conditional block frame

把空间分成有限个不交 blocks `A_r`，measure 为 `mu_r>0`。令

`B_r=int_(A_r)b`, `Z_r=int_(A_r)z`,                (6)

并定义 block-mean Gram

`bar a=sum_r |B_r|^2/mu_r`,

`bar H=sum_r Z_rZ_r^*/mu_r`,

`bar h=sum_r Z_r conjugate(B_r)/mu_r`.             (7)

这是把 `Phi` 正交投影到 block-constant subspace 后的真实 Gram，故
`bar W<=W`。令

`bar S=bar H-bar h bar h^*/bar a`.                 (8)

### 定理 TX（finite block-wedge lower certificate）

对 `r<s` 定义

`w_rs=(B_rZ_s-B_sZ_r)/sqrt(mu_rmu_s)`.             (9)

则

`bar S=(1/bar a)sum_(r<s)w_rsw_rs^*<=S_0`.         (10)

因此

`bar sigma=lambda_min(bar S,B_0)<=sigma`.          (11)

而 `bar sigma>0` 当且仅当 finite vectors `{w_rs}` 张成整个
`C^(R-1)`。

#### 证明

式 (10) 的等号由展开 pair sum 得到：每个 diagonal `Z_rZ_r^*` 的 coefficient
是 `sum_(s!=r)|B_s|^2/(mu_rmu_s)`，合并后正是
`bar a bar H-bar hbar h^*`。另一方面 `W=bar W+W_err`，其中 conditional
expectation 的 Pythagorean theorem 给 `W_err>=0`。文档 102 定理 TU 的
shorted superadditivity 因而给 `S_0>=bar S+S_err>=bar S`。最后应用
generalized Rayleigh quotient；positive definiteness 等价于 frame spanning。
`□`

与直接对式 (5) 作 Jensen 相比，式 (10) 使用 `bar a` 而非 `a`，因而是更强的
projected-Gram certificate。

## 3. Cauchy--Binet algebraization

令 original direction field 在 block `A_r` 上的 normalized integral 为

`p_r=mu_r^(-1/2)int_(A_r)Phi(y)dy in C^R`.         (12)

则 projected full Gram 是

`bar W=sum_r p_rp_r^*`.                             (13)

### 定理 TY（minor-sum coercivity certificate）

Cauchy--Binet 给

`det(bar W)=sum_(r_1<...<r_R)`

`             |det[p_(r_1),...,p_(r_R)]|^2`.       (14)

令 `d=R-1`，并令

`K_bar=B_0^(-1/2)bar S B_0^(-1/2)`.                (15)

若 `d=1`，则 `bar sigma=det K_bar`。若 `d>=2`，定义

`delta_det=det(K_bar)/(tr(K_bar)/(d-1))^(d-1)`.    (16)

则

`0<=delta_det<=bar sigma<=sigma`.                  (17)

#### 证明

式 (14) 是 rectangular matrix `[p_1,...,p_K]` 的标准 Cauchy--Binet identity。
设 `K_bar` 的 eigenvalues 为
`0<=lambda_1<=...<=lambda_d`。对后 `d-1` 个 eigenvalues 用 AM--GM，

`product_(i=2)^d lambda_i`

` <=(tr(K_bar)/(d-1))^(d-1)`.                      (18)

以 `det K_bar=lambda_1 product_(i=2)^d lambda_i` 比较即得
`delta_det<=lambda_1=bar sigma`；`d=1` 显然。`□`

对当前主要计算的 `R=2,3`，式 (16) 分别精确，或至多损失因子 2。更重要的是，
式 (14) 把 positivity 变成显式 arithmetic minors 的平方和，形式上与 Weil
猜想中由 intersection minors 产生 Hodge positivity 的机制相同。

## 4. Möbius unit-cell formula

对文档 097 的 endpoint directions，令 `s in R^R` 是 slope vector，`C_m` 是
截至 integer `m` 的 cumulative divisibility charge vector。在 unit cell
`[m,m+1]` 上，

`Phi(y)=s-C_m/y` (`m>=1`).                          (19)

`[0,1]` 上 field 为 constant `s`。因此 cell integral 是

`p_0=s`,

`p_m=s-C_m log(1+1/m)` (`m>=1`).                   (20)

### 命题 TZ（exact cell-mean/error decomposition）

对 unit-cell projected Gram `bar W=sum_mp_mp_m^*`，有

`W=bar W+E_cell`,                                  (21)

`E_cell=sum_(m>=1) theta_m C_mC_m^*`,              (22)

其中

`theta_m=1/m-1/(m+1)-log^2(1+1/m)>0`.              (23)

并且

`theta_m<=[m^(-3)-(m+1)^(-3)]/(3pi^2)`,            (24)

`theta_m=1/(12m^4)+O(m^(-5))`.                     (25)

#### 证明

在一个 cell 上展开 `int(s-C_m/y)(s-C_m/y)^*dy`，再减去式 (20) 的 outer
product；constant 与 cross terms 精确消失，剩下式 (23) 乘 `C_mC_m^*`。
正性也来自 conditional-expectation variance。对 mean-zero function 使用长度 1
区间的 Wirtinger--Poincaré inequality：

`int|f-bar f|^2<=(1/pi^2)int|f'|^2`.               (26)

取 `f(y)=1/y` 后右侧为式 (24)。Taylor expansion 给式 (25)。`□`

因此 unit-cell certificate 丢失的不是未知 infinite tail，而是显式
`m^(-4)C_mC_m^*` energy。若能证明 cell-minor frame 的 lower bound 压过这项
charge error，actual `sigma` 的所需尺度就随之成立。

## 5. Determinant-frame centerline theorem

把文档 102 定理 TV 中的 `sigma` 替换为任意严格下界会得到更保守但仍充分的
criterion。结合定理 TY 可得：若

`R_c(P)<=c_1+|t| sqrt((R+1)/C_B`

` *[1+C_B(aC_W-1)/(delta_det a C_W^2)])`            (27)

为

`o(sqrt(log N)/loglog(3N))`,                        (28)

则全部 fixed reduced-determinant principal strata 为 `o(1)`；对满足其余
Euler--Tate/Weil package 公理的 zeta function，这迫使 zeros 位于中心线。

这里 `delta_det` 完全由 finitely many block integrals、determinants、endpoint
mass 与 traces 构成。故这是一个真正 finite algebraic centerline certificate；
对经典 zeta 尚未证明式 (28) 的渐近 bound。

## 6. Finite audit

下表对 exact `W^sp=W^[0,N^2]` 比较 uniform 32/128 blocks 与全部 integer unit
cells。各列是 certified `bar sigma/sigma`。

| `N` | `R` | 32 blocks | 128 blocks | unit cells | determinant--trace / `sigma` |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 0.288 | 0.989 | 0.989 | 0.989 |
| 10 | 3 | 0.0361 | 0.993 | 0.993 | 0.990 |
| 20 | 3 | 0.00411 | 0.388 | 0.995 | 0.991 |
| 30 | 2 | 0.00868 | 0.192 | 0.995 | 0.995 |
| 30 | 3 | 0.00397 | 0.0715 | 0.994 | 0.988 |
| 50 | 3 | `1.18e-4` | 0.0163 | 0.996 | 0.989 |
| 100 | 2 | `5.54e-5` | 0.00189 | 0.997 | 0.997 |
| 100 | 3 | `7.00e-4` | 0.00415 | 0.996 | 0.988 |

unit cells 同时捕获 response-line energy `bar a/a` 的 `99.37%--99.49%`。粗
blocks 的失败说明 arithmetic field 在 integer scale 上有必要振荡；但 unit
certificate 的成功表明几乎全部 transversal positivity 已存在于显式 discrete
cell minors 中。数值不能替代渐近证明，不过它把下一目标定得非常窄：证明式
(14) 的 normalized minor sum / trace 不会以破坏式 (28) 的速率退化。

## 7. 计算实现

`scripts/qw_matrix.py` 新增
`endpoint_spatial_block_wedge_certificate`。它计算 block integrals、projected
Gram、聚合 wedge Schur form、actual PSD remainder、generalized coercivity、
determinant--trace lower bound，以及 unit-cell charge variance/Poincaré majorant。

全部 block pairs 的 Gram 通过式 (7)--(10) 在线性时间聚合；只有 pair count
不超过 4096 时才 materialize 单个 wedge vectors。回归测试核对逐 pair 与聚合
公式、conditional PSD remainder、Cauchy--Binet minor sum、unit-cell exact
variance identity 及 Poincaré domination。

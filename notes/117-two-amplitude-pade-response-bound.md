# Two-amplitude Padé bounds for response mass

文档 116 用一个 amplitude capacity sample 在 factor `1+s epsilon` 内恢复 response
spectral mass `beta`。本节使用两个 amplitudes。两个 Stieltjes resolvents 的显式
线性组合可以在整个 support `[0,epsilon]` 上逐点夹住常数函数 `1`；所得区间宽度
从一阶 `O(epsilon)` 降为二阶 `O(epsilon^2)`。

数值上，单 sample 的相对宽度约 `2%--3%`，two-amplitude bounds 降至
`1.7e-5--1.4e-4`，且仍是完全 directed determinant certificate。

## 1. Rational interpolation of the constant function

令

`h_s(lambda)=1/(1+s lambda)`,                      (1)

并固定 `0<a<b`、`0<=lambda<=epsilon`。定义

`L_(a,b)(lambda)=[b h_a(lambda)-a h_b(lambda)]`

`                    /(b-a)`,                    (2)

`U_(a,b)(lambda)=`

` [b(1+a epsilon)h_a(lambda)`

`  -a(1+b epsilon)h_b(lambda)]/(b-a)`.            (3)

### 定理 VT（two-resolvent pointwise sandwich）

在 `[0,epsilon]` 上，

`L_(a,b)(lambda)<=1<=U_(a,b)(lambda)`.            (4)

更精确地，

`1-L_(a,b)(lambda)`

` =ab lambda^2/[(1+a lambda)(1+b lambda)]`,       (5)

`U_(a,b)(lambda)-1`

` =ab lambda(epsilon-lambda)`

`   /[(1+a lambda)(1+b lambda)]`.                 (6)

#### 证明

把式 (2)--(3) 通分到 denominator
`(1+a lambda)(1+b lambda)`。常数项与一次项直接消去，分别留下式 (5) 与
(6)。在 `0<=lambda<=epsilon` 上两式右侧非负，故得式 (4)。`□`

`L` 在 `lambda=0` 与一阶导数处匹配常数；`U` 在 support 两端
`lambda=0,epsilon` 匹配常数。这是一个 support-aware Padé/Chebyshev sandwich。

## 2. Two-amplitude mass recovery

令 `nu` 是文档 116 的 response spectral measure，

`beta=int dnu`,                                   (7)

并记 capacity transforms

`F(s)=ell(s)/s=int h_s(lambda)dnu(lambda)`.        (8)

### 定理 VU（second-order response-mass bracket）

定义

`beta_(a,b)^lo=[bF(a)-aF(b)]/(b-a)`,              (9)

`beta_(a,b)^up=`

` [b(1+a epsilon)F(a)`

`  -a(1+b epsilon)F(b)]/(b-a)`.                  (10)

则

`beta_(a,b)^lo<=beta<=beta_(a,b)^up`.             (11)

而区间宽度为

`beta_(a,b)^up-beta_(a,b)^lo`

` =int ab epsilon lambda`

`       /[(1+a lambda)(1+b lambda)]dnu(lambda)`   (12)

` <=ab epsilon^2 beta`.                           (13)

#### 证明

对定理 VT 的式 (4) 关于 positive measure `nu` 积分，并用式 (7)--(8)，得式
(9)--(11)。式 (12) 是 `U-L` 的直接积分；在 support 上以
`lambda<=epsilon`、denominator `>=1` majorize，得式 (13)。`□`

与单-sample relative width至多 `s epsilon` 相比，two-sample width至多
`ab epsilon^2`。amplitudes 可固定为常数，不随 `N` 调节。

## 3. Two-amplitude determinant Weil criterion

在 plus/minus transversal bases `X_j` 上，分别由两个 auxiliary amplitudes
`a_j<b_j` 的 capacity determinants 构造

`beta_j^lo`, `beta_j^up`。                        (14)

### 定理 VV（two-amplitude determinant response criterion）

定义

`A_2amp=C_B/(2t){`

` delta_+^0/[1-beta_+^up]`

` -delta_-^0/[1-beta_-^lo/(1+epsilon_-)]}`。      (15)

则 finite-head excess 满足

`A_head<=A_2amp`.                                 (16)

加上文档 111 的 uniform variance-tail radius，

`A_W<=(sqrt(A_2amp)+eta_M)^2`.                    (17)

若相应 Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (18)

则在其余 Euler--Tate/Weil package 公理下，相应 zeta zeros 位于中心线。

#### 证明

定理 VU 给 `beta_j` 的 directed interval。文档 115 定理 VP 的 plus upper 随
`beta_+` 单调增加，故代入 `beta_+^up`；被减去的 minus lower 随 `beta_-` 增加，
代入 `beta_-^lo` 保持 overall upper，得到式 (15)--(16)。式 (17)--(18) 由文档
111、100、094。`□`

式 (15) 只需要四个 auxiliary amplitude capacity determinants、两个 support bounds
与 base three-point data；不需 charge sums、kernel inverses 或 spectral vectors。

## 4. Finite audit

使用 amplitudes `a=1/2`、`b=2`。`oneWidth` 是单个 `s=2` sample 的 relative
mass interval宽度；`twoWidth` 是定理 VU 的 relative width。

| `N` | `R` | `M` | oneWidth | twoWidth | lower/beta | upper/beta |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 4 | 1.97e-2 | 4.87e-5 | 0.999953 | 1.000002 |
| 12 | 3 | 5 | 3.05e-2 | 1.42e-4 | 0.999867 | 1.000009 |
| 20 | 3 | 8 | 2.63e-2 | 1.75e-5 | 0.999994 | 1.000011 |
| 30 | 3 | 16 | 2.74e-2 | 5.17e-5 | 0.999960 | 1.000011 |
| 50 | 3 | 30 | 2.41e-2 | 3.90e-5 | 0.999971 | 1.000010 |
| 100 | 3 | 100 | 2.30e-2 | 2.35e-5 | 0.999986 | 1.000010 |

二采样区间比单 sample 缩窄约 `200--1500` 倍。误差远小于 support-only theorem 的
最坏 `ab epsilon^2`，因为 response spectral measure 又偏向低 eigenvalues。

## 5. 计算实现

`positive_rank_update_amplitude_capacity_certificate` 现对所有 positive amplitude
pairs 返回定理 VU 的 response-mass lower/upper。回归逐 pair 验证 exact `beta`
落在 interval 内，并继续核对每个 amplitude 的 direct/spectral capacity identity。

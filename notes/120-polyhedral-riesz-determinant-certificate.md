# Polyhedral Riesz determinant certificate

此前的 endpoint criterion 用 quadratic polarization 与 Cauchy--Schwarz 控制
weighted coefficient `ell^1` norm。文档 119 已使 quadratic susceptibility 几乎精确，
但 quadratic-to-`ell^1` 仍有一个固定维数松弛。本节在 real fixed-rank setting 中将
它完全移除：weighted `ell^1` norm 是有限 sign cube 的 support function；每个 sign
functional 又由两个 positive rank-one determinant capacities 精确极化恢复。

finite audit 同时给出一个重要的否定信息：exact `ell^1` 只比 quadratic upper 小
`10%--25%`，仍远高于 RH threshold。故主要障碍是 canonical representative 本身，
不是 Cauchy--Schwarz certification。

## 1. Real endpoint polytope

令 `W>0`、real response `D`，并记

`C_W=D^*W^(-1)D`,                                 (1)

`v_W=W^(-1)D/C_W`.                                (2)

令 `T: R^R -> R^(R+1)` 是 endpoint Riesz transform，positive weights 为
`c_0,...,c_R`。定义 exact weighted leverage

`L_1(W,D)=sum_(j=0)^R c_j|(Tv_W)_j|`.             (3)

对 sign vector `sigma in {+/-1}^(R+1)`，令

`q_sigma=T^*diag(c_j)sigma`.                      (4)

### 定理 WC（finite sign-cube duality）

有

`L_1(W,D)=max_sigma q_sigma^*v_W`                 (5)

`        =C_W^(-1)max_sigma q_sigma^*W^(-1)D`.   (6)

只需枚举 `2^R` 个 signs：固定 `sigma_0=1` 并对 functional 取 absolute value。

#### 证明

对任意 real vector `x`，

`sum_jc_j|x_j|=max_sigma sum_jc_jsigma_jx_j`;      (7)

最优 sign逐坐标取 `sign(x_j)`。令 `x=Tv_W` 并把 `T^*diag(c)sigma=q_sigma`
代入，得式 (5)。式 (2) 给式 (6)。一对 signs `sigma,-sigma` 的 functionals互为
相反数，故固定第一 sign 后取 absolute value即可。`□`

## 2. Positive determinant polarization

定义 auxiliary responses

`D_(sigma,+)=D+q_sigma`,

`D_(sigma,-)=D-q_sigma`,                           (8)

及其 metric capacities

`K_(sigma,+)=D_(sigma,+)^*W^(-1)D_(sigma,+)`,     (9)

`K_(sigma,-)=D_(sigma,-)^*W^(-1)D_(sigma,-)`.     (10)

### 定理 WD（rank-one determinant recovery）

有

`q_sigma^*W^(-1)D`

` =[K_(sigma,+)-K_(sigma,-)]/4`,                  (11)

并且

`K_(sigma,+)=det(W+D_(sigma,+)D_(sigma,+)^*)`

`                  /det W-1`,                    (12)

`K_(sigma,-)=det(W+D_(sigma,-)D_(sigma,-)^*)`

`                  /det W-1`.                    (13)

所以

`L_1(W,D)=1/(4C_W)`

` *max_(sigma_0=1)|K_(sigma,+)-K_(sigma,-)|`.     (14)

#### 证明

展开式 (9)--(10) 并相减，pure `D` 与 pure `q_sigma` terms cancel，得到式
(11)。matrix determinant lemma

`det(W+rr^*)=det W(1+r^*W^(-1)r)`                (15)

给式 (12)--(13)。与定理 WC 合并得式 (14)。`□`

式 (14) 只使用 positive definite rank-one updates；没有 phase optimization、matrix
inverse output 或 quadratic relaxation。fixed rank时 determinant 数量固定。

## 3. Exact polyhedral centerline criterion

### 定理 WE（polyhedral determinant Weil criterion）

在文档 094 的 fixed reduced-determinant setup 中，以式 (14) 定义 exact leverage
`L_1(N)`。若

`c_1+|target|L_1(N)`

` =o(sqrt(log N)/loglog(3N))`,                     (16)

则 fixed principal strata 全部为 `o(1)`；在其余 Euler--Tate/Weil package 公理下，
相应 zeta function 的 zeros 位于中心线。

#### 证明

endpoint coefficient polynomial 的 weighted Wiener/Riesz norm正是式 (3)，所以
文档 100 定理 TM 中的 quadratic Cauchy upper 可直接替换为 exact `L_1(N)`。式
(16) 随后满足文档 094 定理 SP 的 determinant stability threshold。`□`

定理 WE 是 quadratic polarization criterion 的严格 sharpened 版本；它也适用于
任何 real fixed-dimensional endpoint transform，而不限于 Möbius directions。

## 4. Finite audit and no-shortcut result

`quad/exact` 是 quadratic upper 对 exact polyhedral leverage 的倍率；`exact/T` 是
exact leverage 对所需 threshold scale `T=sqrt(log N)/loglog(3N)` 的倍率。

| `N` | `R` | exact `L_1` | quadratic upper | quad/exact | exact/T |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 103.8 | 116.8 | 1.126 | 83.7 |
| 30 | 2 | 44.95 | 49.68 | 1.105 | 36.7 |
| 100 | 2 | 19.12 | 22.83 | 1.194 | 15.5 |
| 200 | 2 | 92.13 | 102.3 | 1.110 | 74.3 |
| 10 | 3 | 371.2 | 434.2 | 1.170 | 299.4 |
| 20 | 3 | 162.7 | 192.3 | 1.182 | 132.5 |
| 50 | 3 | 102.7 | 128.7 | 1.253 | 83.7 |
| 100 | 3 | 737.6 | 882.5 | 1.196 | 598.5 |

exact polyhedral norm改善约 `10%--25%`，但仍比 threshold 高 `15--600` 倍且随
Möbius oscillation显著波动。因此：

1. quadratic-to-`ell^1` slack 已可完全认证并移除；
2. 它不是经典 RH 当前路线的主要障碍；
3. 尚需 canonical response itself 的 arithmetic cancellation，而非更换 norm bound。

## 5. 计算实现

新增 `endpoint_polyhedral_riesz_determinant_certificate`。它固定首 sign、枚举其余
`2^R` signs，计算 exact mixed responses、两侧 positive rank-one determinant
capacities 与 maximum polyhedral leverage。回归验证 determinant reconstruction
与 direct weighted `ell^1` 在 `1e-43` tolerance 内一致。

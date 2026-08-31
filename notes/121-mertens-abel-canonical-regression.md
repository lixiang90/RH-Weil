# Mertens--Abel canonical regression current

文档 120 已证明 endpoint weighted `ell^1` leverage 可以由有限个 positive
rank-one determinants 精确恢复，并同时排除了 quadratic norm slack 是主要障碍。
本节继续把 canonical response 本身完全算术化：对任意前缀可积的 reciprocal
Euler coefficients，endpoint response 是 prefix current 的离散 Abel 微分；canonical
representative 因而是这个 current 对 Hodge metric 的有限秩 regression。对经典
zeta，prefix current 正是 Mertens function。

这一步没有证明 RH。它证明了所需结构的一个重要部分对 Möbius coefficients
无条件存在，并把尚缺的估计缩成明确的 dyadic Mertens--Hodge correlation，而不再
是抽象的 Gram condition number、capacity 或 coefficient norm。

## 1. 一般 prefix--Abel 因子化

取 real coefficients `b_1,...,b_N`，令

`B_m=sum_(n<=m)b_n`, `1<=m<N`.                    (1)

取 `R` 个 endpoint functions `f_p(n)`，满足

`f_p(1)=f_p(N)=0`,                                (2)

并定义 difference matrix 与 response

`A_(m,p)=f_p(m+1)-f_p(m)`,                        (3)

`D_p=sum_(n<=N)b_nf_p(n)`.                        (4)

### 定理 WF（finite prefix--Abel factorization）

有 exact vector identity

`D=-A^*B`.                                        (5)

#### 证明

由 `b_n=B_n-B_(n-1)`（取 `B_0=0`）作有限分部求和，

`sum_(n=1)^N b_nf_p(n)`

` =B_Nf_p(N)-sum_(m=1)^(N-1)B_m[f_p(m+1)-f_p(m)]`.(6)

式 (2) 消去 boundary term，得到式 (5)。`□`

该定理不使用乘法性、Euler product 或 Möbius inversion；它适用于任何能把 Tate
boundary response 写成 endpoint-vanishing coefficient sum 的 generalized
Weil/Hodge package。

## 2. Canonical representative 是 prefix regression

令 `W>0` 是 correction directions 的 real Hodge Gram，并置

`C=D^*W^(-1)D`.                                   (7)

定义 prefix regression kernel

`G=A W^(-1)A^*`.                                  (8)

### 定理 WG（canonical Abel regression identity）

若 `D` 非零，则

`C=B^*GB`,                                        (9)

`v_W=W^(-1)D/C=-W^(-1)A^*B/(B^*GB)`.             (10)

再令 `T` 为任意 real endpoint transform、`c_j>0` 为 weights，并对 sign
vector `sigma` 定义

`q_sigma=T^*diag(c)sigma`,                        (11)

`h_sigma=-A W^(-1)q_sigma`.                       (12)

则 exact weighted polyhedral leverage 为

`L_1(W,D)=1/C max_sigma |B^*h_sigma|`.            (13)

固定一个 sign 后只需 `2^R` 个 phases。

#### 证明

把式 (5) 代入式 (7) 与 `v_W=W^(-1)D/C`，立即得到式 (9)--(10)。文档 120
定理 WC 给

`L_1=C^(-1)max_sigma|D^*W^(-1)q_sigma|`.          (14)

再次使用 `D=-A^*B` 与式 (12)，右侧变成式 (13)。`□`

所以 canonical coefficient explosion 的准确对象不是 `M(N)` 的单点大小，而是
一个 linear-over-quadratic regression quotient：numerator 是 prefix current 与
`h_sigma` 的相关，denominator 是同一 prefix current 的 `G`-energy。普通
Cauchy--Schwarz 正是文档 095 已审计过且过松的 quadratic bound；式 (13) 保留
全部 signs 与 arithmetic cancellation。

## 3. Dyadic current criterion

以 dyadic shells

`I_j=[2^j,min(2^(j+1)-1,N-1)]`                   (15)

定义

`J_(sigma,j)=sum_(m in I_j)B_mh_sigma(m)`.        (16)

### 定理 WH（dyadic Abel-current Weil criterion）

有 exact identity

`L_1(W,D)=1/C max_sigma |sum_jJ_(sigma,j)|`.       (17)

在文档 094 的 fixed reduced-determinant setup 中，若

`c_1+|target|/C max_sigma|sum_jJ_(sigma,j)|`

` =o(sqrt(log N)/loglog(3N)),`                    (18)

则每个 fixed principal determinant stratum 为 `o(1)`；若再具备总尾控制与文档
001 的 polarized Weil package 公理，则相应 zeta function 的 zeros 位于中心线。

更具体地，当 `|target|=O(1)` 时，任取正 weights `omega_j`、
`sum_jomega_j=1`。以下可直接检验的 mean-square current condition 足以推出
式 (18)：

`max_sigma sum_j |J_(sigma,j)|^2/omega_j`

` =o(C^2 log N/[loglog(3N)]^2).`                  (19)

#### 证明

式 (17) 是把式 (13) 按 shells 分组。由 weighted Cauchy--Schwarz，

`|sum_jJ_j|^2<=sum_j|J_j|^2/omega_j`,             (20)

故式 (19) 推出式 (18)。随后依次应用文档 120 定理 WE、文档 094 定理 SP 与
抽象 polarized Weil 结构定理。`□`

式 (19) 是一个充分但非必要的 mean-square 输入；式 (17) 才是保留跨尺度 signed
cancellation 的 sharp finite target。两者都只涉及 prefix arithmetic、positive
finite Gram inverse 与固定 sign cube。

## 4. 经典 zeta specialization

取

`b_n=mu(n)`, `B_m=M(m)=sum_(n<=m)mu(n)`,          (21)

`u_n=log n/log N`,

`f_p(n)=u_n^p(1-u_n)`, `1<=p<=R`.                 (22)

因为 `f_p(1)=f_p(N)=0`，定理 WF 无条件给

`D_p=-sum_(m<N)M(m)[f_p(m+1)-f_p(m)]`.           (23)

以 exact spatial fractional-part Gram `W_N^[0,N^2]` 代入，式 (9)--(17) 全部
无条件成立。因此，经典 zeta 所需的 finite-rank Abel-regression structure 已实际
构造出来；开放部分是证明 cofinal family 的式 (18)，并完成 growing determinant
tail/nonprincipal additive modes。不能把经典 RH 等价的 pointwise Mertens bound
偷偷作为式 (18) 的输入；本路线要寻找的是适配 kernel `h_sigma` 的更定向平均相消。

## 5. Finite audit

下表使用 `W=W_N^[0,N^2]` 与 elementary endpoint weights。`V/C` 是主导 sign
的 `sum_j|J_j|/C`，`kappa=|sum_jJ_j|/sum_j|J_j|`，故
`L_1=kappa(V/C)`。

| `N` | `R` | `C` | `V/C` | `kappa` | exact `L_1` |
|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 3.506 | 933.0 | 0.1273 | 118.77 |
| 16 | 2 | 3.768 | 1129 | 0.08555 | 96.61 |
| 32 | 2 | 4.192 | 1047 | 0.08436 | 88.32 |
| 64 | 2 | 3.392 | 1581 | 0.04010 | 63.39 |
| 100 | 2 | 2.955 | 1824 | 0.01048 | 19.12 |
| 8 | 3 | 3.512 | 3920 | 0.05533 | 216.87 |
| 16 | 3 | 3.884 | 14347 | 0.01808 | 259.40 |
| 32 | 3 | 4.195 | 5469 | 0.01301 | 71.13 |
| 64 | 3 | 4.498 | 10147 | 0.05494 | 557.46 |
| 100 | 3 | 7.372 | 6074 | 0.12145 | 737.64 |

跨 dyadic shells 的 residual 经常只剩 absolute shell variation 的 `1%--12%`，
说明真实 signed cancellation 确实存在；但 `V/C` 仍达 `10^3--10^4`，且
`kappa` 强烈波动。因此当前数据不支持所需渐近结论。新的最小问题是：证明
`kappa_sigma V_sigma/C` 对全部极端 phases 同时满足式 (18)，或证明更强但更容易
组织的 mean-square condition (19)。

## 6. 计算实现

新增 `mobius_endpoint_mertens_regression_certificate`。它：

1. 同时构造 `A`、Mertens vector、exact spatial Gram 与 response；
2. 独立核对 `D=-A^*M`、`C=M^*AW^(-1)A^*M` 及 canonical representative；
3. 枚举 endpoint sign cube，把每个 mixed functional 分解成 dyadic currents；
4. 精确复原文档 120 的 weighted `ell^1` leverage。

50-digit 回归同时核对 direct metric polarization 与 Mertens-current 路径，并验证
所有 shell contributions 的和等于 direct mixed response。

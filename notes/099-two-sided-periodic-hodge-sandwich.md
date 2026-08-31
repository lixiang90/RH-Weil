# 双边 periodic Hodge sandwich 与显式 infinite leverage 证书

文档 097 只用 continuous large sieve 给 infinite far Gram 的单侧 periodic
majorant，并保留一个未数值固定的 absolute constant。本节利用同一个
Montgomery--Vaughan Hilbert inequality 的双边形式，在远端 annulus
`[N^2,3N^2]` 上得到 periodic Gram 的显式正下界；再对 dyadic far shells
求和得到显式上界。

结果是 actual infinite correction Gram 被两个完全有限的 matrices 夹住：

`W^sp+(1/(9N^2))W^per`

` <=W^full`

` <=W^sp+(10/(3N^2))W^per`.                        (1)

这消除了文档 097 证书中的 unspecified large-sieve constant，并把 infinite
response leverage 严格归约为 finite inverse/generalized-eigenvalue arithmetic。

## 1. Separated Farey spectrum 的双边连续 Hilbert inequality

令 real frequencies `lambda_a` 的 separation 至少为 `Delta>0`，并置

`S(y)=sum_a c_a e^(2pi i lambda_a y)`.               (2)

Montgomery--Vaughan Hilbert inequality 给任意长度 `T` 的 interval `I`：

`|int_I |S(y)|^2dy-T sum_a|c_a|^2|`

` <=Delta^(-1)sum_a|c_a|^2`.                        (3)

#### 证明回顾

展开平方。diagonal 是 `T sum|c_a|^2`；off-diagonal integral 是两个
Hilbert bilinear forms 的差，分别带 factor `1/(2pi)`。separated Hilbert
inequality 对每个 form 给 `pi Delta^(-1)sum|c_a|^2`，两项合并正好得到
式 (3)。先对 finite frequency sets 证明，再由 `ell^2` approximation 推广到
countable separated family。`□`

对 denominator 至多 `N` 的 reduced Farey frequencies（包括 zero frequency），

`Delta>=N^(-2)`.                                    (4)

其 coefficient square sum 正是文档 097 定理 SZ 的 `W^per` quadratic form。

## 2. Far annulus 上的 periodic 正下界

定义 correction field `g(y)`，并令

`W^ann=int_(N^2)^(3N^2)g(y)^*g(y)dy/y^2`.           (5)

### 定理 TF（two-sided annular periodic polarization）

在 correction-direction matrix Loewner order 中，

`(1/(9N^2))W^per<=W^ann<=(3/N^2)W^per`.             (6)

#### 证明

interval 长度是 `T=2N^2`。式 (3)--(4) 给 unweighted bounds

`N^2 W^per<=int_(N^2)^(3N^2)g(y)^*g(y)dy`

`             <=3N^2 W^per`.                       (7)

该 annulus 上

`1/(9N^4)<=1/y^2<=1/N^4`.                          (8)

把式 (7) 与式 (8) 合并即得式 (6)。quadratic inequality 对所有 direction
coefficients 成立，故等价于 Loewner inequality。`□`

式 (6) 的下界是此前缺失的 transversal positivity。它同时包含 response
rank-one 与 oscillatory Farey Gram；前者按文档 096 定理 SV 不改变 normalized
direction，后者是真正的新 coercive contribution。

## 3. 全部 far tail 的显式 periodic 上界

### 定理 TG（explicit dyadic far majorant）

有

`W^far:=int_(N^2)^infinity g(y)^*g(y)dy/y^2`

` <=(10/(3N^2))W^per`.                              (9)

#### 证明

在 dyadic shell `[Y,2Y]`、`Y=2^jN^2` 上，式 (3) 的上界给

`int_Y^(2Y)g(y)^*g(y)dy`

` <=(Y+N^2)W^per`.                                  (10)

再用 `y^(-2)<=Y^(-2)` 并求和：

`sum_(j>=0)[1/(2^jN^2)+1/(4^jN^2)]`

` =[2+4/3]/N^2=10/(3N^2)`.                         (11)

得到式 (9)。`□`

所以文档 088 定理 QZ 在 correction space 上可取显式 constant `10/3`。

## 4. Infinite Gram 的完全有限 sandwich

令

`W^sp=int_0^(N^2)g(y)^*g(y)dy/y^2`,

`W^full=int_0^infinity g(y)^*g(y)dy/y^2`,           (12)

并定义

`W_-=W^sp+(1/(9N^2))W^per`,

`W_+=W^sp+(10/(3N^2))W^per`.                        (13)

### 定理 TH（finite periodic sandwich for the infinite Hodge metric）

有 exact Loewner sandwich

`W_-<=W^full<=W_+`.                                 (14)

若 `D` 是 response vector，则 capacities 满足

`D^*W_+^(-1)D<=D^*(W^full)^(-1)D`

`                 <=D^*W_-^(-1)D`.                 (15)

#### 证明

下界把 `W^sp` 与定理 TF 的 annular subblock 相加；上界把 `W^sp` 与定理 TG
相加。positive-definite matrices 的 inverse Loewner order 反向，左、右乘
`D^*,D` 给式 (15)。`□`

这比“far tail 很小”更强：它直接夹住 full inverse 在 distinguished response
class 上的作用。

## 5. 完全有限的 response-leverage certificate

对文档 098 的 endpoint quadratic mass `B_c`，定义

`gamma_-=gamma(W_-;B_c)`,

`C_+=D^*W_+^(-1)D`.                                 (16)

### 定理 TI（unconditional finite infinite-leverage bound）

actual infinite normalized response representer 满足

`Lambda_c(W^full,D)`

` <=sqrt((R+1)/(gamma_- C_+)).`                     (17)

phase-box 版本为

`Lambda_c(W^full,D)`

` <=sqrt(K_c^#(E,W_-)/C_+)`.                        (18)

因此若

`c_1+|t_N|sqrt((R+1)/(gamma_-(N)C_+(N)))`

` =o(sqrt(log N)/loglog(3N)),`                       (19)

则全部 fixed reduced-determinant principal strata 为 `o(1)`。

#### 证明

由式 (14)，`W^full>=W_-`，所以

`gamma(W^full;B_c)>=gamma_-`                        (20)

以及 `K_c(E,W^full)<=K_c(E,W_-)`。式 (15) 给 full capacity 至少为
`C_+`。分别代入文档 098 定理 TE 与文档 095 定理 SR，得到式 (17)--(18)。
式 (19) 再由文档 094 定理 SP 推出结论。`□`

式 (16)--(19) 的每个量都是 finite：`W^sp` 来自 integer jumps，`W^per`
来自 divisor/conductor sums，其余只是 finite positive linear algebra。没有
zero data、infinite quadrature 或隐藏的 asymptotic positivity assumption。

## 6. 有限尺度审计

以下使用 elementary weights `c_ell=ell` 与定理中的 exact constants：

| `N` | `R` | `gamma_-` | `C_+` | quadratic bound | phase-box bound |
|---:|---:|---:|---:|---:|---:|
| 10 | 1 | `2.98e-2` | 2.587 | 5.09 | 4.83 |
| 10 | 2 | `1.95e-5` | 3.760 | 202.2 | 178.5 |
| 20 | 3 | `2.49e-7` | 4.084 | 1985 | 1657 |
| 30 | 2 | `2.10e-5` | 2.897 | 222.0 | 197.9 |
| 50 | 3 | `3.59e-7` | 4.514 | 1572 | 1317 |
| 100 | 2 | `2.03e-5` | 2.954 | 223.8 | 200.5 |
| 100 | 3 | `4.21e-7` | 7.338 | 1138 | 953.6 |

periodic lower block 对 `gamma` 的数值改善很小，与文档 097 的 tiny relative
far factor 一致；但本节的价值是逻辑闭合：infinite metric 已被 explicit finite
matrices 双边夹住。当前真正需要证明的量不再包含任何 infinite tail，而是
式 (19) 的 finite arithmetic asymptotic，或更锐地文档 098 式 (14)--(17) 的
response spectral weights。

## 7. 广义结构定理接口

定理 TF--TI 抽象出一种“orbit-resolution annulus”机制。若 generalized
Weil/Hodge synthesis 具有：

1. 一个 separation 为 `Delta_N` 的 discrete orbit spectrum；
2. 一个 finite carrier Gram `W^sp_N`；
3. 一个 orbit-average polarization `W^per_N`；

则长度超过 `Delta_N^(-1)` 的 annulus 同时给 `W^per_N` 的正下界与上界，
从而把 infinite polarization 的 distinguished-class inverse 夹在两个 finite
Hodge metrics 之间。这个模块不依赖 zeta 的 Möbius coefficients；zeta 特有的
部分只是 Farey separation `Delta_N=N^(-2)` 与 finite conductor amplitudes。

## 8. 计算实现

`scripts/qw_matrix.py` 新增
`nyman_endpoint_periodic_sandwich_certificate`，返回 `W_-`、`W_+`、
`gamma_-`、`C_+` 及 quadratic/phase-box 两个 infinite leverage bounds。

回归测试在 `N=6,R=2` 上直接用 exact spatial Gram 验证定理 TF 的两个 Loewner
差均正定，并核对 sandwich capacities 的 inverse order。

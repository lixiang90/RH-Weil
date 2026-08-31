# Capacity susceptibility、determinant probes 与中心线结构

文档 100--105 把 endpoint instability 定位到 response-zero Feshbach spectral
measure，并分别研究其 coercivity 与 algebraic existence。本节证明该 spectral
measure 的关键 second moment 可以完全改写为一个 scalar capacity 的
susceptibility。更进一步，只计算 Hodge path 上三个 determinant ratios，就能在
universal factor `4/3` 内上界 exact polarization excess `A`。

这提供一个更可移植的 generalized Weil criterion：不需要构造或跟踪 individual
eigenmodes，只需 positive polarization path、distinguished response functional、
endpoint form，以及相邻 capacities 的定量控制。

## 1. Canonical transversal Hodge path

沿用文档 102 的 notation。令

`P=I-v_BD^*`, `B_perp=P^*BP`,                      (1)

并定义 Hermitian path

`W_tau=W+tau B_perp`.                              (2)

在 adapted coordinates `[v_B,Z]` 中，

`W_tau~[[a,h^*],[h,H+tau B_0]]`,                   (3)

其中 `B_0=Z^*BZ`。令

`C(tau)=D^*W_tau^(-1)D`,

`delta(tau)=1/C(tau)`.                             (4)

若 `kappa=lambda_min(H,B_0)`，则下面的 spectral formula 至少在
`tau>-kappa` 解析；若要求 full metric positive，文档 102 定理 TS 给实际区间
`tau>-sigma`，其中 `sigma=lambda_min(H-hh^*/a,B_0)<=kappa`。

### 定理 UI（capacity--Feshbach Stieltjes identity）

令文档 101 的 null generalized eigenvalues/forcing 为 `lambda_i,g_i`。则

`delta(tau)=a-sum_i |g_i|^2/(lambda_i+tau)`.        (5)

对 `n>=1`，

`(-1)^(n-1)delta^((n))(tau)`

` =n! sum_i |g_i|^2/(lambda_i+tau)^(n+1)>=0`.      (6)

特别地，

`A(W,B;D)=C_B delta'(0)`.                          (7)

而且对整个 path，

`A(W_tau,B;D)=C_B delta'(tau)`.                    (8)

#### 证明

由式 (3) 的 Schur complement，

`delta(tau)=a-h^*(H+tau B_0)^(-1)h`.               (9)

对白化 pencil `(H,B_0)` 作 spectral expansion 即得式 (5)。逐项求导得到式
(6)。文档 101 定理 TN 给
`A/C_B=sum_i|g_i|^2/lambda_i^2`，即式 (7)；将 eigenvalues 平移
`lambda_i+tau` 得式 (8)。`□`

所以 `delta` 是 increasing concave Bernstein function，`delta'` 是 completely
monotone Stieltjes transform。polarization excess 恰是 response energy 对
transversal Hodge mass 的 infinitesimal susceptibility。

## 2. Determinant quotient

令 `Q=[v_B,Z]`，并记

`G_tau=Q^*W_tau Q`.                                (10)

### 定理 UJ（determinant-capacity identity）

有

`delta(tau)=det(G_tau)/det(H+tau B_0)`.             (11)

因此 `A` 是两个 positive determinant polynomials 之比的 logarithmic-slope
combination：

`A=(C_B/C(0)) d/dtau`

`       [log det(G_tau)-log det(H+tau B_0)]_(tau=0)`. (12)

#### 证明

式 (11) 是 block matrix 式 (3) 的 determinant--Schur identity。对其取 logarithm
并求导；由 `delta(0)=1/C(0)` 与定理 UI 式 (7)，得到式 (12)。`□`

式 (11) 把 forcing second moment 变成纯 determinant data。对于文档 103 的
cell Gram，这些 determinants 又可用 Cauchy--Binet 写成 arithmetic minors 的
正平方和。

## 3. One-sided two-scale brackets

对 `tau>0` 定义 forward capacity secant

`S_+(tau)=[delta(tau)-delta(0)]/tau`.               (13)

### 定理 UK（forward susceptibility bracket）

有

`C_BS_+(tau)<=A`

` <=C_B(1+tau/kappa)S_+(tau)`.                     (14)

特别地，取 `tau=sigma` 时，

`C_BS_+(sigma)<=A<=2C_BS_+(sigma)`.                (15)

#### 证明

由式 (5)，

`S_+(tau)=sum_i |g_i|^2/[lambda_i(lambda_i+tau)]`. (16)

逐 mode 比较 `1/[lambda(lambda+tau)]` 与 `1/lambda^2`；二者 ratio 的倒数是
`1+tau/lambda<=1+tau/kappa`，得到式 (14)。因 `sigma<=kappa`，式 (15)
成立。`□`

这已把完整 spectral calculation 压缩成 `C(0),C(sigma)` 两个 scalars，并保留
factor 2 certificate。

## 4. Bidirectional factor-4/3 probe

若 `0<t<sigma`，则 `W_(+t)` 与 `W_(-t)` 均 positive。定义

`S_c(t)=[delta(t)-delta(-t)]/(2t)`.                 (17)

### 定理 UL（centered determinant susceptibility）

有

`A/C_B<=S_c(t)`

` <=[1-(t/kappa)^2]^(-1) A/C_B`.                  (18)

特别地，取 `t=sigma/2`，

`A<=A_hat:=C_BS_c(sigma/2)<=4A/3`.                (19)

#### 证明

由式 (5)，

`S_c(t)=sum_i |g_i|^2/(lambda_i^2-t^2)`.           (20)

每项不小于 `|g_i|^2/lambda_i^2`，且

`1/(lambda_i^2-t^2)`

` <=[1-(t/kappa)^2]^(-1)/lambda_i^2`.              (21)

求和得到式 (18)。再用 `t/kappa=(sigma/2)/kappa<=1/2` 得式 (19)。`□`

相比 one-sided derivative approximation，centered probe 的误差由 square ratio
控制；它只需三个 inverse capacities `delta(-t),delta(0),delta(t)`。

## 5. Capacity-susceptibility centerline theorem

### 定理 UM（three-determinant centerline structure）

在文档 094 的 fixed-determinant setup 中，设 `underline sigma` 是 actual
shorted coercivity 的任意 positive lower certificate。取

`t=underline sigma/2`,                              (22)

并从三个 determinant ratios 式 (11) 定义

`A_hat=C_B[delta(t)-delta(-t)]/(2t)`.               (23)

则 minimum-`W` endpoint polynomial 满足

`R_c(P)<=c_1+|target|`

`          *sqrt((R+1)(1+A_hat)/C_B)`.             (24)

若右侧为

`o(sqrt(log N)/loglog(3N))`,                        (25)

则全部 fixed reduced-determinant principal strata 为 `o(1)`。对任何满足其余
Euler--Tate/Weil package 公理的 zeta function，式 (25) 迫使 zeros 位于中心线。

#### 证明

`underline sigma<=sigma<=kappa` 保证 `W_(+-t)>0`，并由定理 UL 得
`A<=A_hat`。代入文档 100 定理 TM 的 exact Riesz bound，再应用文档 094
定理 SP。`□`

定理 UM 是一个广义结构定理：中心线输入由 positive Hodge path 上三个 finite
determinants 的 susceptibility 给出，而不要求 Hilbert--Pólya eigenbasis。对经典
zeta，可取文档 103 的 unit-cell determinant lower 或文档 104 的 unconditional
polylog lower 作为 `underline sigma`；尚缺的是式 (25) 的渐近 susceptibility
bound。

## 6. Finite Möbius--Farey audit

下表对 exact `W^sp=W^[0,N^2]` 取 `t=sigma/2`。`A_hat` 是式 (23)，最后一列
是定理 UL 的 universal sample-specific factor
`[1-(sigma/(2kappa))^2]^(-1)`。

| `N` | `R` | exact `A` | `A_hat` | `A_hat/A` | factor bound |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 675 | 754 | 1.117 | 1.117 |
| 10 | 3 | 9506 | 12356 | 1.300 | 1.313 |
| 20 | 3 | 2046 | 2599 | 1.270 | 1.326 |
| 30 | 2 | 116 | 150 | 1.291 | 1.291 |
| 30 | 3 | 46946 | 52153 | 1.111 | 1.111 |
| 50 | 3 | 880 | 1068 | 1.214 | 1.329 |
| 100 | 2 | 19.3 | 25.5 | 1.325 | 1.325 |
| 100 | 3 | 34598 | 36012 | 1.041 | 1.041 |

实际 overestimate 为 `4%--32.5%`，严格小于 `1/3`。尤其在最低 mode 高度主导
的样本，sample-specific factor 几乎精确。这把文档 102 某些相差 `10^4` 的
worst-coercivity upper 换成了稳定 scalar determinant probe。

## 7. 存在性含义与下一步

文档 104 已证明 fixed-rank positive path 至少在 polylog scale 存在；本节说明
forcing alignment 也可由 determinant data读取。经典 RH 的下一任务现在可以
直接表述为：对某个 certified `t_N<=sigma_N/2`，证明

`[delta_N(t_N)-delta_N(-t_N)]/(2t_N)`              (26)

满足式 (25) 所需的增长，而不必分别控制 `kappa`、forcing mass 或 eigenvectors。

这可能允许使用 determinant recurrences、Cauchy--Binet minor comparisons、
Loewner sandwich 或 arithmetic log-convexity。解析难度仍未消失，但输入已经从
matrix spectral alignment 收缩成一个三点 scalar inequality。

## 8. 计算实现

`endpoint_transversal_hodge_completion` 现返回 inverse-capacity secant、Stieltjes
prediction、one-sided excess brackets，以及 adapted determinant ratios。

新增 `endpoint_bidirectional_capacity_susceptibility`，以
`t=relative_step*sigma` 构造 positive `W_(+-t)`，返回 forward/backward/centered
susceptibilities、factor bounds、spectral predictions 与 plus/minus determinant
ratios。回归测试交叉核对 direct inverses、spectral sums、block determinants、
factor-2 one-sided bracket 和 factor-4/3 centered bracket。

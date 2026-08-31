# Conductor purity 与 periodic-completion amplitude gap

文档 126 表明 spatial dyadic cells 不产生 Weil 式 weight separation。本节改用
periodic/Farey Parseval decomposition：每个 reduced denominator 是一个 positive
conductor block。该分解对 response 与 external probe 的 Hellinger separation
显著更强，因而是更可信的 Frobenius-weight候选。

然而它属于 auxiliary periodic polarization。经典 full spatial Hodge metric 中，
无条件 far-tail theorem 只提供 `O(N^(-2))` 倍 periodic Gram。本节证明一个一般
constrained-minimizer transfer theorem，并量化该 amplitude 与让 periodic metric
支配 spatial metric 所需强度之间的差距。结论是：conductor purity 真实存在，但
已证自然 completion 太弱，不能将其传递给经典 canonical representative。

## 1. Exact conductor Parseval observations

沿用 Möbius endpoint directions `d_p(n)`。令

`D_p=sum_(n<=N)d_p(n)`                            (1)

为 zero-mode response，并令 `A_r(p)` 是 reduced denominator `r` 的 conductor
amplitude。记正 density 为 `delta(r)`。periodic Gram 的 exact formula 是

`P_N=D D^*/4`

`    +(1/12)sum_(r<=N)delta(r)A_rA_r^*`.          (2)

### 定理 XA（Farey conductor observation factorization）

定义 observation rows

`O_0=D^*/2`,                                      (3)

`O_r=sqrt(delta(r)/12) A_r^*`, `1<=r<=N`.         (4)

则

`P_N=O^*O`.                                       (5)

因此把 denominators 按 `{0},[1,1],[2,3],...` 分组给出 exact positive Hodge
block decomposition；文档 126 的 masses、local coherences与 Hellinger overlap
全部适用。

#### 证明

逐 row outer product 求和，zero row给 `DD^*/4`，第 `r` row给
`delta(r)A_rA_r^*/12`；与式 (2)逐项相同。`□`

式 (2) 来自 sawtooth Fourier Parseval：相同 reduced denominator 的 harmonics
合并为 `A_r`，其平方模总质量为 `delta(r)/12`。

## 2. Conductor-weight purity criterion

令 periodic metric 下的 normalized response/probe masses 为 `d_r^per,e_r^per`，
local coherences 为 `gamma_r^per`。

### 定理 XB（periodic conductor-purity criterion）

periodic external leverage 满足

`L_ext(P_N)<=sqrt(C_q(P_N)/C_D(P_N))`

` *sum_blocks sqrt(d_j^per e_j^per gamma_j^per).` (6)

若一个 generalized Euler--Hodge package 的 actual polarization 正是 `P_N`（或
有足够强的 transfer，见下节），且式 (6) 加 sign defect 满足文档 126 式 (22)，
则对应 zeta zeros 位于中心线。

#### 证明

定理 XA 提供 exact positive blocks，直接应用定理 WZ。`□`

这抽象出一个自然 algebraic structure：conductor sectors 扮演 Frobenius weights，
Parseval Gram扮演 polarization，不同 conductor-energy profiles 的分离产生 mixed
period orthogonality。

## 3. Positive-metric dominance transfer

下面给出从 reference conductor metric `P>0` 向 completed actual metric 的通用
定量传递。设

`0<=W<=Lambda P`,                                 (7)

`W_s=W+sP`, `s>0`.                                (8)

令 `v_s` 是 `W_s` 下满足 `D^*v=1` 的 minimum-energy representative，`v_P` 是
`P` 下对应 representative。记

`C_D(P)=D^*P^(-1)D`, `C_q(P)=q^*P^(-1)q`.         (9)

### 定理 XC（conductor-dominance transfer）

有

`||v_s-v_P||_P^2<=Lambda/[s C_D(P)]`,             (10)

从而

`|q^*v_s|<=|q^*v_P|`

` +sqrt(C_q(P)/C_D(P) * Lambda/s).`               (11)

特别地，要从 periodic external period 得到有用 transfer，必须同时控制 external
capacity ratio 与 relative amplitude error `Lambda/s`。

#### 证明

`v_s` 的变分最小性与式 (7) 给

`v_s^*W_sv_s<=v_P^*W_sv_P`

`             <=(s+Lambda)/C_D(P)`.              (12)

又 `W_s>=sP`，故

`||v_s||_P^2<=(1+Lambda/s)/C_D(P)`.               (13)

因为 `D^*(v_s-v_P)=0` 且 `Pv_P=D/C_D(P)`，Pythagorean identity 给

`||v_s-v_P||_P^2=||v_s||_P^2-1/C_D(P)`,          (14)

结合式 (13) 得式 (10)。最后在 `P` duality 中对
`q^*(v_s-v_P)` 用 Cauchy--Schwarz得到式 (11)。`□`

该 theorem 对任意 positive reference polarization适用，不限于 periodic/Farey
metric。

## 4. 经典 far-completion gap

令 `W_N^sp=W_N^[0,N^2]`，并定义 exact generalized domination constant

`Lambda_N=lambda_max(P_N^(-1/2)W_N^spP_N^(-1/2))`,(15)

所以 `W_N^sp<=Lambda_NP_N`。文档 099 定理 TG 只给 natural far tail

`W_N^far<=[10/(3N^2)]P_N`.                        (16)

定义 available amplitude

`s_N^avail=10/(3N^2)`.                            (17)

### 定理 XD（finite conductor-completion gap certificate）

若只依赖式 (16) 把 conductor purity 传入 actual metric，则必须面对 exact relative
error

`epsilon_N^avail=Lambda_N/s_N^avail`,             (18)

以及定理 XC 的 transfer radius

`R_N^avail=sqrt(C_q(P_N)/C_D(P_N)`

`                    *epsilon_N^avail).`          (19)

只有当该 radius 与 periodic external period、sign defect 的和达到 Riesz threshold
时，这条 dominance route 才能认证中心线。式 (16) 本身不提供这样的结论；它甚至
不保证 `s_N^avail P_N` 支配 `W_N^sp`。

#### 证明

式 (15) 是式 (7) 的最小 possible `Lambda`。把 `s=s_N^avail` 代入定理 XC 即得
式 (18)--(19)。`□`

注意式 (16) 是 far metric 的 upper bound，并不声称 actual far metric 等于 maximal
completion；所以本 theorem 是 certificate-level gap，不能把 maximal completion
的行为冒充 actual metric 的单调 bound。

## 5. Finite audit

先看 periodic conductor blocks：其 `BC^2` 比 spatial dyadic blocks 显著更小。

| `N` | `R` | exact `rho^2` | local upper | `BC^2` | periodic `L_1` |
|---:|---:|---:|---:|---:|---:|
| 8 | 2 | `4.54e-4` | 0.0896 | 0.102 | 4.96 |
| 32 | 2 | 0.0647 | 0.152 | 0.191 | 16.99 |
| 100 | 2 | 0.2368 | 0.297 | 0.379 | 19.63 |
| 200 | 2 | 0.3179 | 0.406 | 0.489 | 20.07 |
| 8 | 3 | `2.38e-5` | 0.0130 | 0.0939 | 8.46 |
| 32 | 3 | 0.00696 | 0.0887 | 0.1047 | 59.60 |
| 100 | 3 | 0.0276 | 0.111 | 0.129 | 66.57 |
| 200 | 3 | 0.0775 | 0.164 | 0.193 | 79.21 |

但 transfer gap 快速扩大：

| `N` | `R` | `Lambda_N` | `s_avail/Lambda` | `epsilon_avail` | transfer radius |
|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 1.755 | 0.0297 | 33.7 | 874 |
| 8 | 3 | 2.030 | 0.0257 | 39.0 | 10837 |
| 32 | 2 | 1.427 | 0.00228 | 438 | 1398 |
| 32 | 3 | 1.600 | 0.00203 | 492 | 15838 |
| 100 | 2 | 1.143 | `2.92e-4` | 3428 | 2362 |
| 100 | 3 | 1.575 | `2.12e-4` | 4726 | 27567 |
| 200 | 2 | 1.125 | `7.41e-5` | 13495 | 4135 |
| 200 | 3 | 1.293 | `6.44e-5` | 15520 | 35456 |

`Lambda_N` 保持 order one，而 available amplitude 按 `N^-2` 消失。maximal periodic
completion 对 spatial exact leverage 的影响也很小：例如 `N=200,R=3` 只从
`374.95` 降到 `373.66`，远未接近 periodic value `79.21`。因此当前 natural far
tail不能实现 conductor-pure Hodge structure；需要新的 cohomological completion、
更强的 actual conductor block，或直接保留 arithmetic phase cancellation。

## 6. 计算实现

新增：

- `mobius_endpoint_periodic_conductor_overlap_certificate`：构造式 (3)--(5) 的 exact
  Parseval observation matrix及 dyadic conductor overlap；
- `mobius_endpoint_conductor_completion_gap_certificate`：计算 `Lambda_N`、available
  amplitude/error、dominance amplitudes、定理 XC transfer radii，以及 spatial、
  maximally completed、periodic canonical leverages。

回归核对 periodic observation Gram、overlap hierarchy、generalized eigenvalue正性
及 `epsilon_avail=(s_avail/Lambda)^(-1)`，tolerance 为 `1e-43`。

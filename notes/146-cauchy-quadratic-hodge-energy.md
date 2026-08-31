# Cauchy 二次 Hodge 能量与 height-free 有限判据

文档 145 证明 Cauchy negative defect只需一致有界，不必趋零。这改变了二阶矩
的地位：文档 137 正确排除了“variance趋零”路线，因为非恒定 passive函数可有
非零 variance；但 **variance/second moment一致有界** 与 passive极限完全相容，
并已足以通过文档 145 的 normality theorem推出中心线。

本节证明 finite stationary symbol的完整 Cauchy second moment有 exact positive
Gram公式，而且可以在排序后 `O(m logm)` 时间计算，不需要任何 height grid。

## 1. Exact Cauchy moment formulas

令

`dmu(t)=dt/[pi(1+t^2)]`,                            (1)

`Q(t)=sum_(j=1)^m c_je^(-itlambda_j)`,

`P(t)=Re Q(t)`, `lambda_j>=0`.                    (2)

Cauchy characteristic function为

`int_R e^(-itx)dmu(t)=e^(-|x|)`.                  (3)

### 定理 ZW（exact stationary Cauchy Hodge energy）

有

`m_P:=int_RP(t)dmu(t)=Re sum_jc_je^(-lambda_j)`,  (4)

`M_abs:=int_R|Q(t)|^2dmu(t)`

` =sum_(j,k)c_jconj(c_k)e^(-|lambda_j-lambda_k|)`, (5)

`M_an:=int_RQ(t)^2dmu(t)`

` =(sum_jc_je^(-lambda_j))^2`,                    (6)

以及

`E_2(P):=int_RP(t)^2dmu(t)`

` =[M_abs+Re M_an]/2>=0`.                         (7)

进一步，

`int_RP(t)_-dmu(t)<=sqrt(E_2(P))`.                (8)

#### 证明

式 (3)逐项应用于 `Q`, `|Q|^2`, `Q^2`，得到式 (4)--(6)；这里
`lambda_j+lambda_k>=0` 使式 (6)因子化。恒等式

`(Re Q)^2=(|Q|^2+Re Q^2)/2`                      (9)

给式 (7)。最后 `P_-<=|P|`，而 `mu` 是 probability measure，Cauchy--Schwarz
给

`int P_-dmu<=int|P|dmu<=sqrt(intP^2dmu)`，即式 (8)。`□`

kernel `e^(-|lambda-kappa|)` 是 positive definite；在 distribution意义下

`(1-d^2/dlambda^2)e^(-|lambda-kappa|)=2delta_kappa`. (10)

所以式 (5)是 log-lag line上 massive one-dimensional Green/Hodge energy。
式 (6)则是 boundary evaluation channel。式 (7)把二者组合成 real stationary
symbol的正能量。

## 2. Linear-time ordered evaluation

若 nodes排序为 `lambda_1<=...<=lambda_m`，则式 (5)可写成

`M_abs=sum_j|c_j|^2`

` +2Re sum_j c_je^(-lambda_j)`

`              *sum_(k<j)conj(c_k)e^(lambda_k)`. (11)

维护 prefix

`B_j=sum_(k<j)conj(c_k)e^(lambda_k)`              (12)

即可在排序后的 `O(m)` arithmetic operations内计算；式 (6)本身是 `O(m)`。
因此 total cost为 sorting的 `O(m logm)`，memory为 `O(m)`。这比 height midpoint
grid以及 dense `m x m` Gram都轻。

实现 `stationary_cauchy_symbol_moments` 返回式 (4)--(8)，并用式 (11)--(12)
计算 modulus block。

## 3. Shared arithmetic approximation

文档 142 的 shared quadrature把 exact arithmetic Hodge functional `H_Y[theta]`
替换成

`L_Y[theta]=int_RP_Y(t)theta(t)dmu(t)`, `0<=theta<=1`, (13)

且有 uniform error

`sup_(0<=theta<=1)|H_Y[theta]-L_Y[theta]|<=eta_Y`. (14)

exact capped minima分别为

`inf_theta H_Y[theta]=-J_Y/pi`,

`inf_theta L_Y[theta]=-int(P_Y)_-dmu`.             (15)

所以式 (8)、(14)--(15)立刻给

`J_Y/pi<=sqrt(E_2(P_Y))+eta_Y`.                   (16)

式 (16)完全不需要 height cutoff、midpoint cells、symbol Lipschitz constant或
Cauchy tail ledger；只保留 shared lag quadrature error。

## 4. Bounded-energy generalized Weil theorem

### 定理 ZX（bounded Cauchy-energy filtered Weil theorem）

在文档 145 定理 ZT 的 holomorphy、Poisson admissibility与 Euler-germ convergence
hypotheses下，若存在 shared finite orbit symbols `P_n` 满足式 (14)，并且

`sup_n E_2(P_n)<infinity`,

`sup_n eta_n<infinity`,                           (17)

则 arithmetic divisor的全部 zeros位于中心线。

特别地，沿文档 143 的 cofinal schedule已有 `eta_n->0`，故只需

`E_2(P_n)=O(1)`.                                  (18)

#### 证明

式 (16)--(17)给 `sup J_n<infinity`；应用文档 145 定理 ZT。`□`

该定理适用于任何 additive orbit-length semigroup，只要 boundary cap的 spectral
measure是 Cauchy measure，或更一般地其 characteristic kernel `k(lambda)` 已知；
式 (5)--(7)相应把 `e^(-|.|)` 换成 `k`。

### 定理 ZY（off-center zeros force quadratic-energy divergence）

若 divisor有 off-center zero，且 `eta_n->0`，则沿每条 cofinal shared-symbol
schedule，

`E_2(P_n)->infinity`.                              (19)

#### 证明

文档 145 定理 ZU给 `J_n->infinity`。由式 (16)，

`sqrt(E_2(P_n))>=J_n/pi-eta_n->infinity`，         (20)

故得式 (19)。`□`

定理 ZY把非线性的 “negative set可以随 `Y` 移动” 障碍转成一个纯正 quadratic
energy blow-up。它不要求 rightmost zero存在，也不受 infinite packet相位相消
影响。

## 5. 与旧 variance no-go 的兼容性

文档 137 的反例 `g(q)=1+rq`, `0<r<1` 是 passive且 variance为 `r^2/2>0`。
这只排除 `variance->0`；它的 second moment是有限常数，所以完全满足定理 ZX
的 bounded-energy geometry。

因此正确区分是：

- `E_2(P_n)->0`：通常过强，甚至排除非零常数 passive limits；
- centered variance `->0`：错误地强迫 limit近常数；
- `sup E_2(P_n)<infinity`：允许任意固定 passive boundary profile，同时已足以
  给 normality和中心线。

## 6. 数值 audit

取固定 `delta=.1`, prime cutoff `N=40Y`, `tau=10^-3`, `L=3logY` 与 128
geometric lag cells。height-free certificate给：

| `Y` | nodes | `E_2(P_Y)` | `sqrt(E_2)` | shared error |
|---:|---:|---:|---:|---:|
| 2 | 160 | `.12046` | `.34708` | `.1121` |
| 5 | 189 | `.07258` | `.26940` | `.2475` |
| 10 | 226 | `.07341` | `.27095` | `.4977` |
| 30 | 351 | `.11623` | `.34093` | `1.2928` |

energy保持在 `10^-1` 尺度，而 fixed mesh的 shared error增长。对 `Y=30` 加密：

| lag cells | nodes | `E_2(P_Y)` | shared error |
|---:|---:|---:|---:|
| 128 | 351 | `.11623` | `1.2928` |
| 256 | 479 | `.09464` | `.7752` |
| 512 | 735 | `.09026` | `.4634` |
| 1024 | 1247 | `.08961` | `.2810` |

这说明 signed energy对 lag refinement稳定到约 `.09`，而 rigorous-formula upper
仍由保守 quadrature error主导。数据只用于确认新 target没有明显数值爆炸；
`delta`固定、`Y`很小且计算不是 interval arithmetic，绝不证明式 (18)。

## 7. 对 zeta 的新算术目标

对 shared signed orbit measure `nu_Y`，式 (5)是

`iint e^(-|lambda-kappa|)dnu_Y(lambda)dconj(nu_Y)(kappa)`. (21)

prime--prime block的 kernel为

`e^(-|logm-logn|)=min(m,n)/max(m,n)`.              (22)

所以定理 ZX 在一般数据上的目标是一个明确的 ratio-kernel
prime--continuum--Gamma discrepancy energy `O(1)`。这与文档 036--047 的
max/ratio Green kernels及文档 070 的 sharp Selberg variance属于同一正二次型
家族。但文档 147 证明：对 zeta 的这列 candidates，critical-line zeros本身的
positive spikes已迫使 full energy发散；可行版本必须先抽取 nonnegative
background，再只控制 residual ratio energy。

实现 `zeta_abel_shared_cauchy_energy_certificate` 直接输出式 (16)，跳过 arbitrary
Loewner relaxation与整个 height grid。下一步应把式 (21)按 prime、continuum、
Gamma blocks解析展开，寻找已有 Selberg/Barban--Davenport--Halberstam 型估计能
控制的精确 signed discrepancy，而不能对三个 blocks分别取绝对值。

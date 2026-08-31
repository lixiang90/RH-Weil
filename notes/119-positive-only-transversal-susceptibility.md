# Positive-only transversal susceptibility certification

文档 106 用 `W+/-tB_perp` 的 centered capacity probe 在 factor `4/3` 内认证 endpoint
susceptibility。文档 118 的 arbitrary-order Stieltjes machinery 可直接应用于
transversal completion path，而且只需要 positive perturbations `W+tB_perp`。

本节证明 endpoint excess 本身是一个 compact-support response spectral measure 的
总质量。`k` 个 positive completion determinant capacities 给 relative error
`O(product r_i)` 的 directed upper。三点 `(0.02,0.05,0.1)` 的 audit 把旧
`4%--30%` slack 降到 `2.4e-7--1.3e-5`。

## 1. Transversal susceptibility measure

沿用文档 101/106 的 null endpoint whitening。令

`lambda_i>0`                                      (1)

是 `W` 在 `ker D^*` 上相对 endpoint metric `B_0` 的 generalized eigenvalues，
`g_i` 是 response forcing coordinates，并令

`kappa=min_i lambda_i`.                           (2)

canonical transversal completion 为

`W_t=W+tB_perp`, `t>=0`.                          (3)

其 inverse capacity 满足

`delta(t)=a-sum_i |g_i|^2/(lambda_i+t)`.          (4)

定义 positive measure

`mu_W=sum_i |g_i|^2/lambda_i^2`

`               *delta_(kappa/lambda_i)`.         (5)

### 定理 VZ（transversal response-measure identity）

`mu_W` 支持在 `(0,1]`，且

`mu_W((0,1])=A_W/C_B`.                            (6)

对任意 relative completion amplitude `r>0`，

`[delta(rkappa)-delta(0)]/(rkappa)`

` =int_(0,1] dmu_W(x)/(1+rx)`.                   (7)

#### 证明

support statement来自 `lambda_i>=kappa`。文档 101 的 spectral formula 给

`A_W/C_B=sum_i|g_i|^2/lambda_i^2`，              (8)

即式 (6)。由式 (4)，

`[delta(t)-delta(0)]/t`

` =sum_i |g_i|^2/[lambda_i(lambda_i+t)]`

` =sum_i (|g_i|^2/lambda_i^2)/(1+t/lambda_i)`.    (9)

取 `t=rkappa` 并用式 (5)，得式 (7)。`□`

所以 endpoint excess 不是一个任意 derivative，而是 positive measure 的 mass；
completion capacity secants 是其 Stieltjes samples。

## 2. Arbitrary-order positive completion bound

取 distinct relative amplitudes

`0<r_1<...<r_k`.                                  (10)

令

`F(r_i)=[delta(r_ikappa)-delta(0)]/(r_ikappa)`.    (11)

用文档 118 定理 VW 在 support `[0,1]` 上构造 coefficients
`A_i^lo,A_i^up`。

### 定理 WA（positive-only determinant susceptibility bracket）

定义

`A_k^lo=C_Bsum_iA_i^loF(r_i)`,                    (12)

`A_k^up=C_Bsum_iA_i^upF(r_i)`.                    (13)

则

`A_k^lo<=A_W<=A_k^up`,                            (14)

且

`A_k^up-A_k^lo`

` <=(product_i r_i)A_W`.                          (15)

每个 `delta(r_ikappa)` 都是 positive metric `W+r_ikappa B_perp` 的 determinant
quotient；不需要 negative perturbation。

#### 证明

定理 VZ 把式 (11) 写成 support `[0,1]` 上同一 positive measure的 resolvent
samples。对它应用文档 118 定理 VX，mass 是 `A_W/C_B`，relative width upper 是
`product r_i`。乘 `C_B` 得式 (12)--(15)。determinant statement 来自文档 106
定理 UJ。`□`

amplitudes 可任意固定得小；对 exact finite determinants，不存在 centered probe 的
positive-cone限制。higher order 又允许避免单纯把 `r_i` 取得过小所导致的数值
subtraction问题。

## 3. Positive-only finite-head Weil criterion

对文档 111 的 finite-head metric `W_(N,M)`，用定理 WA 构造

`A_(N,M)^pos>=A_(N,M)`.                           (16)

### 定理 WB（positive-completion determinant Weil criterion）

令 uniform cell-tail radius为

`eta_M^2=C_Bepsilon_M^2/[2C_(N,M)kappa_(N,M)]`.   (17)

则 exact spatial excess 满足

`A_(W,N)<=`

` (sqrt(A_(N,M)^pos)+eta_M)^2`.                  (18)

若代入式 (18) 的 endpoint Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (19)

则 fixed reduced-determinant strata 为 `o(1)`；在其余 Euler--Tate/Weil package
公理下，相应 zeta function 的 zeros 位于中心线。

#### 证明

定理 WA 给 finite-head projected excess upper；文档 111 定理 VD 的 tail stability
给式 (18)。文档 100 定理 TM 与文档 094 定理 SP 给式 (19) 的结论。`□`

定理 WB 比 centered three-capacity criterion 有两个结构优势：全部 auxiliary forms
正定；susceptibility slack 可用固定有限个 amplitudes 提高到任意阶。

## 4. Finite audit

对 projected unit-cell mean metrics 使用 relative amplitudes
`(0.02,0.05,0.1)`，theoretical relative width upper 为 `1e-4`。

| `N` | `R` | exact `A` | positive upper/A | positive width/A | centered upper/A |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 675.7 | 1.0000133 | 3.78e-5 | 1.1178 |
| 10 | 3 | 9392.5 | 1.0000018 | 7.79e-5 | 1.3000 |
| 30 | 2 | 112.4 | 1.0000037 | 7.75e-5 | 1.2928 |
| 30 | 3 | 47028.0 | 1.0000132 | 3.60e-5 | 1.1112 |
| 50 | 3 | 884.3 | 1.0000002 | 5.49e-5 | 1.2149 |
| 100 | 3 | 34625.7 | 1.0000089 | 1.48e-5 | 1.0412 |

positive-only upper 的 slack 为 `2.4e-7--1.33e-5`，相比 centered upper 缩小四到
六个数量级。需要强调：它精确认证了很大的 `A`，并没有证明 `A` 本身达到 RH
阈值；但 certification error 已不再是障碍。

## 5. 计算实现

新增 `endpoint_completion_multiamplitude_susceptibility_certificate`。它从 actual
null coercivity选择 physical steps `t_i=r_ikappa`，计算 positive completion
capacities及其独立 determinant quotients，并返回 arbitrary-order susceptibility
lower/upper 与 theoretical relative width。回归验证 exact excess落在 bracket 内。

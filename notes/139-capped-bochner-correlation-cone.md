# Cauchy-capped Bochner cone 与双正 Gram 证书

文档 138 建议先把 contractive-outer correlation cone放宽到所有 normalized
positive-definite correlations，再求 arithmetic Hodge functional 的极值。本节
证明这种放宽过大：它允许 point-mass characters直接选中最深 negative well。

真正的 outer cone带有一个此前未显式写出的 **spectral cap**。其谱测度不仅
为正，而且被 Cauchy harmonic measure

`dmu(t)=dt/[pi(1+t^2)]`                             (1)

支配。这个 domination完全等价于两套 positive-definite kernels，因而在任意
有限 lag set上成为一个 exact Loewner interval

`0<=R<=K_C`, `K_C(j,k)=e^(-|lambda_j-lambda_k|)`.  (2)

式 (2) 把 outer realizability从 nonlinear factorization改写为 semidefinite
geometry，是通向 finite certificates 的关键结构。

## 1. Contractive outer moduli 的闭包

对 `h in H^infinity(D)`, `||h||_infinity<=1`，文档 137--138 的 correlation为

`r_h(lambda)=int_R e^(-itlambda)|h(t)|^2dmu(t)`.   (3)

这里 `h(t)` 表示经 Cayley boundary identification后的 boundary value。
定义 full Cauchy correlation

`k_C(lambda)=int_R e^(-itlambda)dmu(t)=e^(-|lambda|)`. (4)

### 定理 YV（dominated-Bochner characterization）

对 continuous function `r:R->C`，下列条件等价：

1. `r` 是 contractive outer correlations `r_h` 的 compact-uniform极限；
2. 存在 `theta in L^infinity(mu)`, `0<=theta<=1` a.e.，使

   `r(lambda)=int_R e^(-itlambda)theta(t)dmu(t)`；  (5)

3. `r` 与 `k_C-r` 都是 continuous positive-definite functions。

#### 证明

`1=>2`：每个 `r_h` 的 spectral measure为 `|h|^2mu<=mu`。dominated finite
measures在 weak-* 下 compact；任意极限仍为 `nu<=mu`，由 Radon--Nikodym
写成 `nu=theta mu`, `0<=theta<=1`，给式 (5)。Fourier transforms在 compact
lags上一致收敛。

`2=>3`：`theta mu` 与 `(1-theta)mu` 都是 positive measures；Bochner theorem
分别给 `r` 与 `k_C-r` positive definite。

`3=>2`：Bochner theorem给 positive measures `nu,eta`，其 Fourier transforms
分别为 `r,k_C-r`。因此 `nu+eta` 的 Fourier transform为 `k_C`；Fourier
transform的 uniqueness给 `nu+eta=mu`，故 `nu<=mu`，再用
Radon--Nikodym得到式 (5)。

`2=>1`：对给定 `theta` 取

`theta_epsilon=epsilon+(1-epsilon)theta`.           (6)

则 `log theta_epsilon in L1(mu)`；圆盘 outer factorization给 contractive
outer `h_epsilon` 满足 `|h_epsilon|^2=theta_epsilon`。令
`epsilon downarrow0`；`L1(mu)` convergence使 Fourier transforms甚至在全
`lambda` 上一致收敛。`□`

所以文档 138 的 `C_outer` 闭包是一个 exact order interval：spectral measure
介于 `0` 与 `mu` 之间。outer condition没有消失，而是被吸收到 complementary
positive kernel `k_C-r` 中。

## 2. Finite double-Gram characterization

给定 lag nodes `Lambda={lambda_1,...,lambda_m}`，定义

`R_Lambda(r)=[r(lambda_j-lambda_k)]_(j,k)`,         (7)

`K_Lambda=[e^(-|lambda_j-lambda_k|)]_(j,k)`.       (8)

### 推论 YW（Cauchy-cap Loewner Grams）

`r` 属于定理 YV 的 capped cone，当且仅当对每个有限 `Lambda`，

`R_Lambda(r)>=0`, `K_Lambda-R_Lambda(r)>=0`.       (9)

#### 证明

positive definiteness的定义正是全部有限 Gram matrices半正定；分别应用于
`r` 与 `k_C-r`。`□`

式 (9) 是 exact finite algebraic shadow。第一块是 Hodge/correlation positivity；
第二块是 contractive complement。仅保留第一块会把 outer density cap完全
丢掉。

## 3. 为什么 uncapped positive-definite relaxation 必然失败

令 `u(t)=Re F(delta+it)`，并把文档 138 的 functional写成

`Re H[r_nu]=int_R u(t)dnu(t)`,                      (10)

其中 `r_nu` 是 positive measure `nu` 的 Fourier transform。

### 定理 YX（uncapped character-collapse no-go）

在全部 positive-definite `r` 且 `0<=r(0)<=1` 的 cone上，

`inf Re H[r]=min(0,inf_(t in R)u(t))`.             (11)

#### 证明

Bochner把该 cone识别为 mass至多一的 positive measures。式 (10) 对 measure
线性；零 measure给值零，而 point mass `delta_t` 给 `u(t)`。任意 probability
average不小于 `inf u`，故式 (11)成立。`□`

因此 unrestricted cone的 extremizers是 characters
`r(lambda)=e^(-itlambda)`，即无限窄 spectral packets。它们不满足
`nu<=mu`，却会直接落在 Abel resonance最深点。该 relaxation失败并不反驳
outer arithmetic Hodge inequality；它只是删除了最关键的 Cauchy capacity。

## 4. Capped cone 恰恢复 negative mass

在定理 YV 的 cone上，`dnu=theta dmu`, `0<=theta<=1`。所以

`inf_(r in C_cap)Re H[r]`

` =inf_(0<=theta<=1)int u theta dmu`

` =-int u_-dmu=-J(F,delta)/pi`.                    (12)

这既重证文档 137 的 outer dual，也说明 double-Gram条件没有松弛：当全部 lag
constraints都保留时，它与原 Cauchy defect完全等价。

### 定理 YY（capped-kernel filtered Weil theorem）

在文档 136 定理 YL 的 analytic hypotheses下，若 arithmetic Hodge functionals
满足

`inf_(r: r and k_C-r positive definite) Re H_n[r]`

` >=-epsilon_n`, `epsilon_n->0`,                   (13)

则 arithmetic germ有 positive-real continuation，相应 self-dual order-one
divisor的全部 zeros位于中心线。

#### 证明

式 (12) 给 `J_n/pi<=epsilon_n`。应用文档 136 定理 YL与文档 131 定理 XQ。
`□`

定理 YY 是文档 138 定理 YU 的纯 kernel版本：不再需要显式构造 outer factors，
只需一对互补的 positive-definite correlation kernels。

## 5. Cofinal finite SDP certificate

有限 lag set只给必要条件；但把 feasible matrices放宽反而适合 sufficient
lower certificate。对 `Lambda_N` 令

`S_N={R=R^*:0<=R<=K_(Lambda_N)}`.                 (14)

设一个 Hermitian linear functional `L_N(R)` 近似完整 `Re H_n[r]`，并已证明

`sup_(r in C_cap)|Re H_n[r]-L_N(R_(Lambda_N)(r))|<=eta_N`. (15)

### 定理 YZ（finite Loewner-SDP certificates imply center-line purity）

若沿 cofinal参数

`inf_(R in S_N)L_N(R)>=-epsilon_N`,                (16)

且 `epsilon_N+eta_N->0`，则相应 arithmetic divisor的 zeros全部位于中心线。

#### 证明

actual capped restrictions属于式 (14)，所以式 (16) 对 actual `r` 也成立；再用
式 (15) 得 `Re H_n[r]>=-(epsilon_N+eta_N)`。应用定理 YY。`□`

`S_N` 比真正的 stationary restriction cone更大，因为 arbitrary matrix
`0<=R<=K` 未必只依赖 lag differences。这只会降低 SDP infimum；因此若放宽后
仍得到式 (16)，证书严格有效。失败则可能只是 relaxation gap，不能反推原
inequality失败。

## 6. 实现与 audit

新增：

- `cauchy_correlation_dominating_gram`：式 (8)；
- `capped_correlation_gram_certificate`：返回 `R` 与 `K-R` 的 spectra；
- `zeta_abel_cauchy_negative_mass_audit` 新增 capped defect与 unrestricted
  character depth的并列账本。

固定 `delta=.1,N=40Y,H=2Y` 的 sampled diagnostics：

| `Y` | capped defect `J/pi` | deepest character well | depth / capped defect |
|---:|---:|---:|---:|
| 10 | `5.80e-2` | `8.75e-2` | `1.51` |
| 30 | `1.79e-2` | `8.68e-2` | `4.84` |
| 100 | `3.69e-3` | `3.05e-1` | `82.5` |
| 300 | `1.20e-3` | `4.05e-1` | `338` |

随着 resonance wells变窄并移向高频，uncapped character cone越来越悲观；
Cauchy spectral cap恰把 narrow-well capacity计入。所有数字仍是非区间网格
诊断，不是式 (13) 的证明。

## 7. 下一步

现在可以对文档 138 式 (12) 建立真正有限的 SDP hierarchy：

1. 选择包含 `log n`、Gamma quadrature nodes与 continuum nodes的 lag set；
2. 把每个 `r(lambda)` 作为 `R` 的 first-row/difference entry，并强制
   `0<=R<=K_C`；
3. 证明 Gamma removable singularity、continuum quadrature和 prime tail的
   uniform error `eta_N`；
4. 检查 SDP lower bounds是否沿 `(Y,delta,N)` cofinal趋零。

这条路线若成功，定理 YZ直接给中心线；若失败，dual SDP witness会给一个
明确的 capped correlation obstruction，可进一步检查其 stationary/outer
realizability，而不是只得到一个无结构的负 eigenvalue。

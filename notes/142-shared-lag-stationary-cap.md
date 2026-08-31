# Shared lag mesh 与 exact stationary capped minimum

文档 141 的第一版 quadrature已给 uniform error，但 pole、Gamma、continuum
使用三套独立 meshes；文档 140 的 arbitrary Loewner interval optimizer又不强制
stationarity。二者分别造成 node浪费与 relaxation gap。

本节解决这两项：

1. 先在解析层面合并 pole与Gamma orbit weights，使全部 continuous data共用
   一个 lag variable `lambda`；
2. 再证明 finite stationary capped problem不需要 SDP，其极值是 finite boundary
   symbol的 Cauchy-weighted negative part，并给一维网格的显式 lower error。

这把 finite relaxation从 arbitrary matrices拉回真正的 dominated spectral
densities `0<=theta<=1`。

## 1. Pole--Gamma cancellation on a common lag

沿用 `sigma=1/2+delta`。pole orbit为

`int_0^infinity e^(-sigma lambda)r(lambda)dlambda`. (1)

文档 138 的 Gamma form作 `t=2lambda` 后变成

`int_0^infinity [e^(-2lambda)r(0)`

` -e^(-sigma lambda)r(lambda)]/(1-e^(-2lambda))dlambda`. (2)

式 (1) 与式 (2) 的 nonzero-lag coefficient精确合并为

`e^(-sigma lambda)-e^(-sigma lambda)/(1-e^(-2lambda))`

` =-e^(-(sigma+2)lambda)/(1-e^(-2lambda))`.        (3)

Abel continuum在同一 lag上的 weight为

`e^((1-sigma)lambda)e^(-e^lambda/Y)`.              (4)

所以定义 shared signed weight

`w_(Y,sigma)(lambda)=e^((1-sigma)lambda)e^(-e^lambda/Y)`

` -e^(-(sigma+2)lambda)/(1-e^(-2lambda))`.         (5)

### 定理 ZG（common-lag Abel Hodge identity）

完整 continuous Hodge functional可写成

`H_cont[r]=-(logpi+gamma)r(0)/2`

` +int_0^infinity e^(-2lambda)/(1-e^(-2lambda))r(0)dlambda`

` +int_0^infinity w_(Y,sigma)(lambda)r(lambda)dlambda`, (6)

其中两个 integrals在 `lambda=0` 必须联合解释；对任意 `tau>0`，在
`[tau,infinity)` 上式 (6)逐项绝对收敛，而 `[0,tau]` 使用文档 141 的 joint
Gamma bound。加上 exact prime atoms即恢复文档 138 式 (12)。

#### 证明

式 (1)--(4)逐项相加；式 (3)是代数恒等式。origin regularization与原
digamma identity相同，故没有改变 functional。`□`

式 (3) 很重要：分别估 pole tail与Gamma negative tail会丢掉一个主阶，shared
form只剩更快衰减的 residual Gamma weight。

## 2. Shared geometric quadrature

取 `0<tau<L` 与 cells

`tau=lambda_0<lambda_1<...<lambda_M=L`.            (7)

在每个 cell用 exact signed mass

`c_j=int_(lambda_j)^(lambda_(j+1))w_(Y,sigma)(lambda)dlambda` (8)

乘 midpoint correlation。误差用 total variation mass

`V_j=int_cell|w_(Y,sigma)(lambda)|dlambda`          (9)

与文档 141 定理 ZD：

`error_j<=V_j omega((lambda_(j+1)-lambda_j)/2)`.   (10)

Gamma positive zero-lag mass在 `[tau,L]` 精确为

`(1/2)[log(1-e^(-2L))-log(1-e^(-2tau))]`.          (11)

pole与continuum在 `[0,tau]` 以 `r(0)` 近似，误差由 `omega(tau)` 控制；Gamma
origin仍用文档 141 式 (12)。tails为：

- zero-lag Gamma tail `-(1/2)log(1-e^(-2L))`；
- residual Gamma tail
  `int_L^infinity e^(-(sigma+2)lambda)/(1-e^(-2lambda))dlambda`；
- incomplete-gamma continuum tail；
- Abel prime tail。

### 定理 ZH（shared-lag uniform error）

上述 shared finite functional `L_shared[r]` 满足

`|Re H_(Y,delta)[r]-L_shared[r]|<=E_shared`         (12)

uniformly for all Cauchy-capped correlations，其中 `E_shared` 是式 (10)、origin
errors与上述 tails之和。

#### 证明

定理 ZG先作 exact algebraic cancellation；每个 cell再用文档 141 式 (8)，
origin/tails沿用其 bounds。`□`

geometric mesh

`lambda_j=tau(L/tau)^(j/M)`                        (13)

自动在 singular origin附近加密，并允许远端 cells随快速衰减 weight变宽。

## 3. Arbitrary Loewner optimizer 的 stationarity gap

真正 correlation Gram满足

`R_(jk)=r(lambda_j-lambda_k)`.                     (14)

所以相同 lag differences必须给相同 entries；特别地全部 diagonal entries等于
`r(0)`。文档 140 的放宽 `0<=R<=K` 没有强制式 (14)。

### 定理 ZI（equal-lag stationarity test）

若 finite Gram来自 stationary correlation，则对任意
`lambda_j-lambda_k=lambda_l-lambda_m`，

`R_(jk)=R_(lm)`.                                   (15)

反之，若式 (15) 对 difference set成立，`R` 定义了该 finite difference set上的
Hermitian stationary kernel；是否能扩张到全 `R` 还需双正 extension条件。

#### 证明

第一项由式 (14)。反向只需令每个 observed difference的 `r` 等于共同 entry；
extension并非自动，故明确保留该条件。`□`

实现 `correlation_stationarity_defect` 对近相等 differences分组，返回 diagonal
spread与 within-group diameter。它是 numerical audit，不是 exact symbolic
collision proof。

## 4. Stationary capped finite problem 的精确变分

finite lag coefficients `c_j` 定义 boundary symbol

`P(t)=Re sum_j c_je^(-itlambda_j)`.                (16)

对 capped spectral density `0<=theta<=1`，functional为

`int_RP(t)theta(t)dmu(t)`.                         (17)

### 定理 ZJ（exact stationary capped minimum）

`inf_(0<=theta<=1)int Ptheta dmu`

` =int_Rmin(P(t),0)dmu(t)`.                        (18)

#### 证明

逐点最小化：`P(t)>=0` 时取 `theta=0`，`P(t)<0` 时取 `theta=1`。measurable
selector正是 negative-set indicator；文档 137 的 outer approximation说明它
也属于 contractive-outer cone的闭包。`□`

定理 ZJ 比 arbitrary Loewner negative trace更尖，且只剩一维积分。

## 5. 一维 finite lower ledger

在 `[-T,T]` 划 uniform midpoint cells，并使用 exact Cauchy cell masses。令

`D=sum_j|c_j||lambda_j|`, `C=sum_j|c_j|`.          (19)

则 `P` 的 Lipschitz constant至多 `D`。cell width为 `h` 时，central quadrature
误差至多 `Dh/2`；Cauchy tail mass为

`m_tail=1-(2/pi)arctanT`,                          (20)

故 omitted negative tail至多 `Cm_tail`。

### 定理 ZK（stationary capped lower certificate）

若 `v_sample` 是 exact Cauchy cell masses乘 `min(P(mid),0)` 的和，则

`int_Rmin(P,0)dmu`

` >=v_sample-Dh/2-Cm_tail`.                        (21)

结合定理 ZH，完整 arithmetic Hodge functional在 capped cone上的 infimum至少

`v_sample-Dh/2-Cm_tail-E_shared`.                  (22)

若式 (22) 沿 cofinal日程为 `-o(1)`，则由文档 139 定理 YY推出中心线。

#### 证明

map `x->min(x,0)` 是 1-Lipschitz，故每个 central cell的 symbol误差至多
`D h/2`，按 probability masses求和仍至多该量。tail上
`min(P,0)>=-C`，给式 (20)--(21)；再用定理 ZH。`□`

## 6. 实现与 audit

新增：

- `zeta_abel_shared_lag_loewner_quadrature`：式 (5)--(13)；
- `correlation_stationarity_defect`：定理 ZI 的 finite audit；
- `stationary_capped_functional_minimum`：定理 ZJ--ZK 的 sampled value与
  rigorous-formula error ledger。

取 `delta=.2,Y=2,N=40,tau=10^-3,L=6`：

| shared cells | total nodes | shared uniform error | constant-probe error |
|---:|---:|---:|---:|
| 16 | 36 | `.2969` | `9.90e-4` |
| 32 | 52 | `.1952` | `3.26e-4` |
| 64 | 84 | `.1327` | `1.91e-4` |
| 128 | 148 | `.0953` | `1.58e-4` |

旧独立 32-cell meshes需要 116 nodes且 error `1.263`；shared 32 cells只需 52
nodes且 error `.195`。tails约 `3.1e-6`，改善来自解析 cancellation与共享 mesh。

对 shared 32-cell Loewner optimizer：

- diagonal spread约 `.767`；
- equal-lag entry diameter上界约 `1.06`；

故其 relaxed value `-.3058` 是强非 stationary witness。直接用定理 ZJ，在
`T=100`, 20000 height cells下得到 sampled stationary minimum约 `-.2213`，
grid+tail error约 `.0383`，即 lower ledger约 `-.2596`。它仍为负，符合有限
`Y=2` candidate并不 passive；不是 RH反例或证据。

## 7. 下一步

目前两个误差层已明确分离：

1. arithmetic functional approximation `E_shared`；
2. stationary symbol integral的 height grid/tail error。

文档 143 已给出增长 `Y`、缩小 `delta` 的一条显式 cofinal schedule，并证明
式 (22) 中全部 lag/height/tail误差无条件趋零。文档 143 定理 ZM说明 finite
symbols的 Cauchy negative mass趋零会推出 RH；文档 145 定理 ZV进一步证明，
只要该 negative mass沿一条 cofinal schedule一致有界就已经足够。若 RH失败，
finite symbol的 capped stationary minimum反而必须共尾趋于 `-infinity`。

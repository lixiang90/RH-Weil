# Capped Hodge functional 的统一误差 quadrature

文档 140 已把 finite Cauchy-capped Loewner optimization化成 negative spectral
trace闭式；剩余问题是把文档 138 的 continuous pole/Gamma/continuum functional
近似成有限 lag objective，并对 **全部** capped correlations给统一误差。

本节构造第一版解析 error ledger。关键输入不是 differentiability，而是 spectral
cap `0<=theta<=1` 给出的显式 modulus of continuity。它足以证明 quadrature
误差随 mesh趋零，并特殊处理 digamma在 `t=0` 的 joint cancellation。

实现仍用非区间 `mpmath` 计算 scalar cell masses与 NumPy谱；所以当前数值是
audit，不是 RH certificate。但误差公式本身指出了严格 interval版本需要包围的
全部量。

## 1. Cauchy-cap 的强 modulus

由文档 139 定理 YV，

`r(lambda)=int_R e^(-itlambda)theta(t)dmu(t)`,

`0<=theta<=1`, `dmu=dt/[pi(1+t^2)]`.               (1)

故对 `d=|a-b|`，

`|r(a)-r(b)|`

` <=int_R|e^(-itd)-1|dmu(t)`.                      (2)

使用 `|e^(-ix)-1|<=min(2,|x|)`，在 `|t|=2/d` 分段积分得到

`omega_1(d)=d/pi log(1+4/d^2)`

` +(4/pi)[pi/2-arctan(2/d)]`.                      (3)

另一方面 Cauchy--Schwarz及 `hat mu(d)=e^(-d)` 给

`omega_2(d)=sqrt(2[1-e^(-d)])`.                    (4)

### 定理 ZD（Cauchy-capped correlation modulus）

对全部 capped correlations，

`|r(a)-r(b)|<=omega(d):=min(omega_1(d),omega_2(d))`. (5)

特别地，`omega(d)=O(dlog(1/d))` as `d downarrow0`。

#### 证明

式 (2)--(3)给第一界。对 measure `theta mu` 用 Cauchy--Schwarz，

`|int(e^(-ita)-e^(-itb))theta dmu|^2`

` <=int theta dmu int|e^(-itd)-1|^2theta dmu`

` <=2[1-e^(-d)]`,                                  (6)

给第二界；取较小者。`□`

相比文档 140 后最初使用的 `O(sqrt d)`，式 (3)利用了 density cap，而不仅是
total mass，显著改善 fine mesh误差。

## 2. Positive-weight cell quadrature

令 `w>=0`，cell `I=[a,b]`，midpoint `m`，并用 exact cell mass

`W_I=int_Iw(lambda)dlambda`.                       (7)

则

`|int_Iw(lambda)r(lambda)dlambda-W_Ir(m)|`

` <=W_I omega((b-a)/2)`.                           (8)

这同时适用于：

- pole weight `e^(-sigma lambda)`；
- Abel continuum weight
  `e^((1-sigma)lambda)e^(-e^lambda/Y)`；
- Gamma negative orbit weight after `lambda=t/2`。

pole cell mass有 elementary exponential闭式；continuum cell mass为

`Y^(1-sigma)Gamma(1-sigma,e^a/Y,e^b/Y)`.           (9)

所以 double-exponential continuum tail无需在 infinite interval作 numerical
quadrature。

## 3. Digamma origin 必须联合处理

Gamma form为

`G[r]=(1/2)int_0^infinity`

` [e^(-t)r(0)-e^(-sigma t/2)r(t/2)]/(1-e^(-t))dt`. (10)

两项分别在 `0` 发散。取 `0<tau<=1`，写 numerator为

`e^(-t)[r(0)-r(t/2)]`

` +[e^(-t)-e^(-sigma t/2)]r(t/2)`.                (11)

用较粗但显式的 `omega_2(t/2)<=sqrt t`、
`1-e^(-t)>=te^(-t)`，得到

`|G_[0,tau][r]|`

` <=sqrt(tau)+(tau/2)|1-sigma/2|`

`       *exp(max(0,1-sigma/2)tau)`.                (12)

在 `[tau,T]` 上，positive `r(0)` cell mass可精确加到 zero-lag coefficient；
negative `r(t/2)` cell用式 (8)。尾部由

`(1/2)int_T^infinity[e^(-t)+e^(-sigma t/2)]/(1-e^(-t))dt` (13)

控制。式 (12) 虽非 sharp，却保持了关键 cancellation，且 `tau->0` 时趋零。

## 4. Prime 与其它 tails

对 `|r|<=1`：

- pole tail为 `e^(-sigma U)/sigma`；
- continuum tail为
  `Y^(1-sigma)Gamma(1-sigma,e^L/Y,infinity)`；
- omitted Abel prime current用

  `int_N^infinity logx x^(-sigma)e^(-x/Y)dx`       (14)

  控制，条件仍是文档 132 的 integrand monotonicity margin为正。

把式 (8)、(12)--(14)求和，得到 uniform error `E_quad+E_tail`。

### 定理 ZE（finite Abel capped-Hodge quadrature）

令 `L_(Y,delta,N)(r)` 是上述 cell-mass midpoint与 exact primes组成的 finite
lag functional，`E_(Y,delta,N)` 是全部 quadrature/tail bounds之和。则对
每个 Cauchy-capped correlation，

`|Re H_(Y,delta)[r]-L_(Y,delta,N)(r)|<=E_(Y,delta,N)`. (15)

#### 证明

每个 positive-weight cell用式 (8)，Gamma origin用式 (12)，各 infinite tail
用式 (13)--(14)与 `|r|<=1`。triangle inequality后即得。`□`

这里的 `N` 概括 prime cutoff、三个 mesh sizes与三个 endpoints；它们可独立
增长。

## 5. 接入 closed-form Loewner spectrum

把 finite coefficients写成文档 140 的 arrowhead objective `C_N`，lag nodes的
Cauchy cap为 `K_N`。令

`v_N=sum_jmin(lambda_j(K_N^(1/2)C_NK_N^(1/2)),0)`. (16)

### 定理 ZF（quadrature-spectral center-line certificate）

若沿 cofinal `(Y,delta,N)`，`delta->0`，且

`v_N-E_(Y,delta,N)>=-epsilon_N`,

`epsilon_N->0`,                                    (17)

同时 Abel candidates满足文档 136 的 Euler-open-set convergence，则 RH成立。
同一结论适用于文档 138--140 的一般 self-dual orbit-semigroup zeta data。

#### 证明

定理 ZE给 actual functional至少为 finite objective减 `E`；文档 140 定理 ZA
给所有 finite feasible restrictions的 objective至少为 `v_N`。故式 (17)给
文档 139 定理 YY 的 `-o(1)` lower bound，再应用 positive-real Weil theorem。
`□`

## 6. 实现与 baseline audit

新增：

- `cauchy_capped_correlation_modulus_bound`：式 (3)--(5)；
- `zeta_abel_capped_loewner_quadrature`：组装 finite lags、coefficients、Cauchy
  cap、closed-form minimum及分项 error ledger；
- `loewner_interval_linear_minimum_numpy`：较大 exploratory matrices的
  double-precision Hermitian backend；任意精度小矩阵版本仍保留用于交叉核对。

取 `delta=.2,Y=2,N=40`，固定 endpoints
`U=6,tau=.02,T=8,L=4`，并让三套 uniform meshes都取相同 cell count：

| cells each | lag nodes | relaxed `v_N` | total error | constant-probe error |
|---:|---:|---:|---:|---:|
| 2 | 26 | `-0.6975` | `6.142` | `0.630` |
| 4 | 32 | `-0.5357` | `4.460` | `0.397` |
| 8 | 44 | `-0.4569` | `2.994` | `0.201` |
| 16 | 68 | `-0.3926` | `1.947` | `0.0866` |
| 32 | 116 | `-0.3405` | `1.263` | `0.0337` |

constant probe `r(lambda)=e^(-lambda)` 应恢复 `F_Y(delta+1)`；其误差随 mesh稳定
下降并始终被 uniform ledger覆盖，验证了转录方向。可是 `v_N-E_N` 仍远负，
所以这不是 RH evidence。

32-cell分解中主要 errors约为：pole quadrature `.341`、Gamma origin `.148`、
Gamma quadrature `.543`、continuum quadrature `.122`；总 tail仅 `.108`。
因此下一瓶颈不是 analytic infinity tails，而是 lag discretization与 Loewner
relaxation。

## 7. 下一步：shared adaptive lag mesh

当前 pole、Gamma与continuum各用独立 uniform mesh，产生近三倍 nodes且在
Gamma origin附近效率很低。下一版应：

1. 统一以 `lambda` 为 lag变量，Gamma用 `t=2lambda`，三类 weights共用同一
   adaptive cells；
2. 在 `lambda=0` 附近用 geometric grading配合式 (12)；
3. 让 cell width按 local total variation weight与 `omega(h)` 等误差原则分配；
4. 对 optimizer检查 equal-lag/stationarity defect，量化文档 140 Loewner
   relaxation gap。

文档 142 已实现 shared geometric mesh，并进一步发现 arbitrary Loewner
optimizer强烈违反 stationarity。真正 finite capped minimum可直接写成 finite
boundary symbol的 Cauchy negative part，并用一维 exact-mass grid给 lower
ledger；后续不再以 arbitrary Loewner minimum作为主证书。

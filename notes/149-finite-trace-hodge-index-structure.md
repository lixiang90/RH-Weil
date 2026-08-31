# 有限迹 Hodge 指数：比逐 character Loewner 支配更准确的广义结构

文档 148 把 prime、continuum 与 Gamma 项统一写成 signed unitary orbit
Laplacians。这给出了规范的 positive squares，但若进一步要求所有 characters 上
逐点 Loewner 支配，就忽略了 Cauchy spectral cap：越来越深、越来越窄的负井
可以有很小的 capped capacity。

本节把真正需要的结构抽离为 finite tracial Hodge algebra。有限域情形的
Hodge--Riemann positivity对应 negative index为零；数域边界只需 negative
index的规范迹一致有界。

## 1. Effect cone 上的 exact negative-index identity

令 `(M,tau)` 是 finite von Neumann algebra，`tau(1)=1`，令 `H=H*` 是
`tau`-integrable operator。写 spectral Jordan decomposition

`H=H_+-H_-`, `H_+,H_->=0`, `H_+H_-=0`.             (1)

把 `0<=E<=1` 称为 Hodge effects。

### 定理 AAD（finite-trace Hodge-index duality）

有 exact identity

`inf_(0<=E<=1) tau(HE)=-tau(H_-)`.                (2)

极小值由 negative spectral projection `E=1_(-infinity,0)(H)` 达到。

#### 证明

由 trace cyclicity，

`tau(HE)=tau(H_+^(1/2)EH_+^(1/2))`

`        -tau(H_-^(1/2)EH_-^(1/2))>=-tau(H_-)`,  (3)

因为第一项非负且 `E<=1`。取 `E` 为 `H_-` 的 support projection，第一项为零，
第二项恰为 `tau(H_-)`。`□`

式 (2) 是 Hodge index theorem 的有限迹版本：不是计算最坏 eigenvalue，而是
计算全部 negative directions按 ambient spectral capacity计权后的总指数。

## 2. 广义 bounded-index Weil 结构定理

设 `F_n` 是文档 145 定理 ZT中的 Poisson-admissible arithmetic candidates，
在 Euler open set收敛到 self-dual order-one divisor `Phi` 的 logarithmic
derivative germ。设每个 `n` 还带有：

1. normalized finite tracial algebra `(M_n,tau_n)`；
2. `tau_n`-integrable self-adjoint Hodge current `H_n`；
3. arithmetic capped test cone与 effects `0<=E<=1` 的识别，使其 functional
   与 `tau_n(H_nE)` 的 uniform误差至多 `eta_n`；
4. capped defect满足

   `J_n/pi<=tau_n((H_n)_-)+eta_n`.                 (4)

精确 realization时 3--4 是等式，而不是额外估计。

### 定理 AAE（bounded finite-trace Hodge--Weil theorem）

若

`sup_n[tau_n((H_n)_-)+eta_n]<infinity`,           (5)

则 `Phi` 的全部非零 zeros位于中心线。

#### 证明

定理 AAD把全部 Hodge effects上的 worst arithmetic depth精确化为
`-tau_n((H_n)_-)`。式 (4)--(5)给 `sup_nJ_n<infinity`，应用文档 145 定理 ZT。
`□`

这就是所求的一类广义结构定理。它允许 `M_n` 非交换，允许 Hodge current有
无限秩 negative spectrum，也允许最小 eigenvalue趋于 `-infinity`；只要其
negative spectral mass在规范迹下不发散，中心线结论仍成立。

有限域 Weil 情形是更强的 special case：primitive Hodge--Riemann relations使
`H_n>=0`，故式 (5)左侧为零。文档 148 的 bounded Loewner domination也是
special case，因为 `H_n>=-BI` 蕴含 `tau_n((H_n)_-)<=B`。

## 3. Cauchy cap 给经典 zeta 的规范交换 realization

取

`dmu(t)=dt/[pi(1+t^2)]`,

`M=L^infinity(R,mu)`, `tau(f)=int f dmu`.          (6)

令 `P_(Y,delta)(t)=Re F_Y(delta+it)`，并令 `H_(Y,delta)` 为在
`L^2(mu)` 上乘以 `P_(Y,delta)` 的 operator。effects就是乘法算子
`E=M_theta`, `0<=theta<=1`。于是定理 AAD变成

`inf_(0<=theta<=1)int P_(Y,delta)theta dmu`

` =-int [P_(Y,delta)]_-dmu=-J_(Y,delta)/pi`.       (7)

所以 finite-trace algebra、effect cone、trace与 Hodge current对 zeta Abel
candidates都已 **无条件显式构造**；文档 137--139 的 outer factorization说明
这正是 contractive Hardy tests的闭包，不是人为选取的 relaxation。

文档 148 的 orbit edges又给

`H_(Y,delta)=aI+L_--L_+`,                         (8)

其中 `L_+`、`L_-` 均由 unitary length-semigroup的 edge squares生成。因此
经典 zeta 已无条件拥有“有限迹代数 + signed Hodge squares + capped effects”三层
结构。唯一仍有 RH 强度的存在性输入是沿一条 cofinal schedule证明

`tau((H_(Y,delta))_-)=O(1)`.                      (9)

若 RH假，文档 145 定理 ZU说明式 (9)在 directed/cofinal意义下必发散。因而任何
对式 (9)的无循环 arithmetic proof都会证明 RH；当前文档没有把式 (9)当成已知。

## 4. 为什么 full Loewner order 不是正确 target

由式 (8)，逐 character domination要求

`L_+<=L_-+CI`,                                   (10)

它控制 operator norm negative depth。有限迹定理只控制

`kappa_tau(H):=tau(H_- )`.                        (11)

二者严格不同。若 `H_M=-M` 在 trace为 `1/M` 的 projection上、在其补空间为零，
则

`||H_M^-||=M ->infinity`, `tau(H_M^-)=1`.         (12)

因此 narrow resonance wells可以破坏任何 uniform pointwise Loewner constant，
却完全不妨碍 bounded-index theorem。对交换 orbit symbol，正确的 exact quantity是

`kappa_mu(P)=int [D_+(t)-D_-(t)-a]_+dmu(t)`,       (13)

而不是 `sup_t[D_+(t)-D_-(t)]`。

### 推论 AAF（trace-orbit criterion）

在定理 AAE的 analytic hypotheses下，若 finite/regularized signed orbit currents
满足 uniform functional error `eta_n=O(1)` 及

`int [D_(+,n)-D_(-,n)-a_n]_+dmu=O(1)`,            (14)

则对应 divisor的 zeros全部位于中心线。

#### 证明

式 (13)--(14)就是定理 AAE的式 (5)。`□`

推论 AAF保留文档 148 的每条 nonnegative edge square，但把 global comparison
从 operator norm降到 spectral-capacity trace；这是文档 145 bounded-defect
normality真正要求的强度。

## 5. 真实 shared-symbol audit

使用 `stationary_signed_orbit_laplacian_audit` 与
`stationary_capped_functional_minimum`，取 geometric shared lag mesh并在
`|t|<=200` 上作 midpoint诊断，得到：

| `Y` | `delta` | degree `a=P(0)` | sampled deepest well | sampled `kappa_mu(P)` |
|---:|---:|---:|---:|---:|
| 2 | .2 | -.3151 | .3151 | .2211 |
| 5 | .1 | -.1640 | .1640 | .1115 |
| 10 | .05 | -.09134 | .6348 | .06251 |
| 30 | .025 | -.03048 | 2.7033 | .03184 |

后两行正显示式 (12)的机制：pointwise well快速加深，Cauchy capacity却下降。
这些是 double-precision、非区间、非 cofinal-resolution 数值；相应 conservative
grid/tail error约为 `.021,.043,.084,.222`，所以不能作为式 (9)或 RH 的证据。
它们只证明选择 proof norm时不能把 deepest character当成 capped Hodge index。

## 6. 原 RH 与 GRH 的结构存在性

对 exact completed divisor还有一个精确的条件存在性结论。令

`H_x=M_(Re Phi'/Phi(x+it))`, `x>0`.                (15)

### 定理 AAG（exact passive Hodge realization iff center-line purity）

对 real-type、center-self-dual、order至多一的 entire divisor `Phi`，下列等价：

1. `Phi` 的全部非零 zeros位于中心线；
2. 对每个 `x>0`，式 (15)满足 `H_x>=0`；
3. `Phi'/Phi` 的 Pick kernel给一个 positive resolvent/Hodge realization。

#### 证明

乘法 operator positivity等价于 `Re Phi'/Phi(x+it)>=0` a.e.；holomorphy使其等价
于整个右半平面的 positive-real property。文档 131 定理 XQ已证明这与中心线
divisor及 positive Pick/resolvent realization等价。`□`

因此 exact正结构的存在性与 RH/GRH本身等价；它是清晰的目标，但不能作为无循环
证明。真正可研究的 arithmetic existence problem是从 Euler、Gamma与 pole data
先构造式 (6)--(8)，再不用 zeros证明式 (9)或 (14)。

对 paired Dirichlet、tempered automorphic及一般 self-dual Gamma--Euler data，
把 Satake phases放入文档 148 的 twisted orbit edges，并把 Cauchy cap作为规范迹，
定理 AAE逐字适用。local temperedness构造 positive edge squares；ramified/Gamma
项只给有限或 regularized corrections；尚缺的仍是 global negative Hodge index
的统一 arithmetic bound。

## 7. 下一步

新的正确目标不是证明式 (10)，而是直接估计式 (13)：

1. 用 negative spectral projection/level-set formula
   `tau(H_-)=int_0^infinity tau(1_(H<-u))du` 分层负井；
2. 低频用 degree anomaly与 small-`t` lag moments；
3. 中频用 block large sieve同时控制井深与 Cauchy capacity；
4. 高频使用文档 133--136 已有的 weighted defect estimates；
5. 对 finite certificates保留 exact Cauchy cell masses，而不以最小 sampled
   character代替 capped trace。

这一路线允许 resonances变深，只要求其 capacity总和一致有限，恰好匹配定理 ZT
而不额外追求一个可能为假的 uniform pointwise bound。

文档 150 已执行该计划的第一步：建立 layer-cake/block-capacity theorem，并把
zeta Abel current尚未控制的频率范围从 `Y polylogY` 无条件缩到
`sqrt(Y)delta^(-3/2)logY`。

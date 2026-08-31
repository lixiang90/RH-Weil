# Signed orbit Laplacians 与 bounded-degree Hodge domination

文档 147 说明可行的 quadratic 结构必须先构造 nonnegative background。本节把
这个 background从任意函数提升为一个规范代数对象：unitary length-semigroup
的 graph/Dirichlet Laplacian。每条 Euler、continuum或 Gamma orbit edge都能精确
完成平方；signed orbit functional因此等于

`degree anomaly + positive Laplacians - comparison Laplacians`. (1)

这把“寻找数域 Hodge--Riemann 结构”变成一个明确的 Loewner domination问题，
并同时覆盖 zeta、paired Dirichlet L-functions与 tempered unitary Euler data。

## 1. 单条 twisted orbit edge

令 `U_lambda` 是 Hilbert space `H` 上的 unitary semigroup representation，
`v in H`。对 `|u|=1` 定义 twisted edge energy

`D_(u,lambda)(v)`

` =(1/2)||v-uU_lambda v||^2`

` =||v||^2-Re[u<U_lambda v,v>] >=0`.              (2)

在 character fiber `U_lambda=e^(-itlambda)` 上，其 symbol是

`d_(u,lambda)(t)=1-Re(ue^(-itlambda))>=0`.         (3)

所以对 sign `epsilon in {+1,-1}` 与 weight `w>=0`，

`epsilon w Re(ue^(-itlambda))`

` =epsilon w-epsilon w d_(u,lambda)(t)`.          (4)

式 (4)是文档 016 引理 BC、文档 017 引理 BI在 boundary stationary model中的
共同形式。

## 2. Signed-edge Hodge decomposition

考虑 real symbol

`P(t)=a_0+sum_j epsilon_jw_jRe(u_je^(-itlambda_j))`, (5)

其中 `w_j>=0`, `epsilon_j=+/-1`。定义 degree anomaly

`a=a_0+sum_j epsilon_jw_j`,                        (6)

以及两个非负 orbit Laplacians

`D_+(t)=sum_(epsilon_j=+1)w_jd_(u_j,lambda_j)(t)`, (7)

`D_-(t)=sum_(epsilon_j=-1)w_jd_(u_j,lambda_j)(t)`. (8)

### 定理 AAA（signed orbit-Laplacian polarization identity）

有 exact identity

`P(t)=a+D_-(t)-D_+(t)`.                            (9)

在任意 unitary representation上，相应 quadratic form identity为

`H(v)=a||v||^2+<L_-v,v>-<L_+v,v>`,                (10)

其中 `L_+,L_->=0` 是式 (2)的 weighted sums。

#### 证明

对每条 edge应用式 (4)。`epsilon=+1` 的 edge给 constant `+w` 与
negative Laplacian `-wd`；`epsilon=-1` 给 constant `-w` 与 positive
Laplacian `+wd`。连同 `a_0` 收集 constants即为式 (6)，其余项给式
(7)--(10)。`□`

注意“positive coefficient”落在 comparison Laplacian `D_+`，而负 cosine
coefficient完成平方后反而产生 Hodge background `D_-`；这正是 prime negative
adjacency变成 positive graph energy的机制。

## 3. Bounded domination 已足够

### 定理 AAB（bounded degree--Laplacian Weil theorem）

设一列 Poisson-admissible arithmetic candidates满足文档 145 定理 ZT的
Euler-germ convergence。假设它们有式 (5)--(10)的 finite/regularized orbit
approximations，uniform functional error为 `eta_n=O(1)`。若存在与 `n` 无关的
`A,C<infinity`，使

`a_n>=-A`,                                         (11)

`L_(+,n)<=L_(-,n)+CI`                              (12)

作为 quadratic forms成立，则相应 divisor全部 zeros位于中心线。

更一般地，式 (12)只需在 Cauchy-capped stationary spectral representation的
cyclic subspace上成立。

#### 证明

式 (10)--(12)给每个 admissible vector

`H_n(v)>=-(A+C)||v||^2`.                           (13)

在 capped normalization `||v||<=1` 下，exact Hodge functional的 infimum至少
`-(A+C+eta_n)`。文档 139 的 identity给

`J_n/pi<=A+C+eta_n=O(1)`.                          (14)

应用文档 145 定理 ZT。`□`

有限域 Weil theory对应 `A=C=eta=0`：primitive Hodge--Riemann form给 exact
domination。数域允许统一有限 negative depth，所以定理 AAB比 exact positivity
弱，但仍因 analytic-germ rigidity推出中心线。

## 4. Scalar stationary specialization

若式 (5)的 phases都为 `u_j=1`，写 coefficients `c_j=epsilon_jw_j`。则

`a=sum_jc_j=P(0)`,                                 (15)

`D_+(t)=sum_(c_j>0)c_j[1-cos(tlambda_j)]`,         (16)

`D_-(t)=sum_(c_j<0)(-c_j)[1-cos(tlambda_j)]`.      (17)

所以式 (12)在全部 characters上成为 pointwise inequality

`D_+(t)<=D_-(t)+C`, `t in R`.                     (18)

### 推论 AAC（fully finite character-Laplacian certificate）

沿任一 shared-lag cofinal schedule，若：

1. quadrature error `eta_Y=O(1)`；
2. degree anomalies `P_Y(0)` 有统一 lower bound；
3. 式 (18)有统一 finite constant `C`；

则 RH成立。若 shared errors趋零而 RH失败，则条件 2或 3至少有一个沿每条
cofinal schedule无界失败。

#### 证明

式 (15)--(18)是定理 AAB的 scalar character fibers。反命题来自文档 145
定理 ZU。`□`

实现 `stationary_signed_orbit_laplacian_audit` 对任意 finite real coefficients
逐高度返回式 (15)--(18)两侧、minimum domination margin与 exact identity
error。sampled domination只用于诊断，不是 all-height certificate。

## 5. Abel--zeta 的 canonical edge split

文档 142 的 shared finite symbol coefficients全部为 real：

- negative edges：prime atoms，以及 combined Gamma residual为负的 cells；
- positive edges：continuum占优的 cells、pole/origin regularization及可能的
  positive combined cells；
- zero lag只进入 degree anomaly，不产生 Laplacian。

因此每个 finite Abel symbol无条件具有

`P_Y(t)=P_Y(0)+D_(prime/Gamma,-)(t)`

`                    -D_(continuum/pole,+)(t)`.   (19)

这不是假设，而是定理 AAA的代数恒等式。真正未证的 zeta Hodge input精确为：

`continuum/pole comparison Laplacian`

` <= prime/Gamma graph Laplacian + bounded identity`, (20)

同时 `P_Y(0)` 不能向 `-infinity` 逃逸。

式 (20)是文档 016--017 global graph domination在 Cauchy stationary fibers上的
版本。局部 Euler purity只构造右侧每条 positive square；全球 prime distribution
与 archimedean/pole coupling才可能证明 domination。

## 6. 一般 Gamma--Euler 数据

对 paired self-dual degree-`d` Euler data，local Satake phases
`u_(p,r)^m` 直接代入式 (2)。若 local parameters unitary，则每条 twisted edge
无条件给 positive Laplacian。ramified primes是有限 corrections；Gamma factors
经 shared orbit regularization加入 comparison/background edges。

因此得到以下广义结构包：

1. self-dual entire divisor与 Euler-open germ；
2. additive length semigroup的 unitary/twisted orbit representation；
3. signed-edge identity (10)；
4. bounded degree anomaly；
5. global Loewner domination (12)；
6. Poisson admissibility。

定理 AAB说明该包必推出对应 zeta/L-function的中心线纯性。对有限域，4--5由
weights与 Hodge--Riemann exact满足；对 zeta/Dirichlet/tempered automorphic data，
1--3及6已有自然构造，唯一全球缺口是4--5的 uniform arithmetic estimate。

## 7. 下一步

式 (20)不应按 total masses比较；两边都可有 `Y^(1/2)` 级 degree，而真正信息
在共同 resonance directions的 cancellation。可行的下一审计是：

1. 把 `D_+-D_-` 在低、中、高 heights分块；
2. 高频用 archimedean growth与文档 133--135 的 weighted core estimates；
3. 低频把 small-`t` expansion的 lag moments与 pole/Gamma degree anomaly合并；
4. 中频使用文档 018--024 的 block large sieve控制所有非零 resonance wells；
5. 只要求 uniform constant `C`，不再追求旧图结构中的 `o(1)` domination。

若这条 bounded domination仍失败，finite audit会给出明确 heights及 edge measures，
可判断缺的是 degree anomaly、continuum comparison还是 prime resonance core。

文档 149 的真实 shared-symbol audit显示，最深 character well可随 `Y` 加深而
Cauchy-capped negative mass同时下降。因此本节的 full Loewner domination是一个
方便但偏强的 sufficient condition；与 bounded-defect theorem精确匹配的广义
结构应改用 finite-trace negative Hodge index。

# Cayley inner-semigroup 与 Cauchy–Toeplitz 极化

文档 136 把 Abel--zeta 的结构存在性压缩成 Cauchy-weighted negative part

`J_(Y,delta)=int_R[-Re F_Y(delta+it)]_+/(1+t^2)dt`. (1)

本节研究式 (1) 本身。第一结论是否定性的：虽然 Cauchy weight给精确 Poisson
均值与 Hardy二阶矩，但任何只控制 variance 的方法都与目标几何不匹配；真正
的 passive limit可以非恒定、variance非零，而 negative part严格为零。

第二结论给出替代结构：式 (1) 恰等于一个 contractive outer cone 上的
Toeplitz form 最大负能量。经 Cayley transform，每个 Dirichlet phase
`n^(-it)` 成为 singular inner semigroup element

`Theta_(log n)(q)=exp[-log(n)(1+q)/(1-q)]`.          (2)

乘法 `mn` 精确对应 inner isometries 的乘法。这把 arithmetic negative defect
重写成一个真正的 Hardy--Hodge 极化问题，并给出可复用于一般 Euler semigroup
的结构定理。

## 1. Cauchy--Poisson moments

固定 `delta>0`，令 `F` 在 `Re z>delta` holomorphic、沿 boundary至多
logarithmic growth，并写

`u(t)=Re F(delta+it)`,

`dmu(t)=dt/[pi(1+t^2)]`,

`m=Re F(delta+1)`.                                  (3)

### 定理 YN（Poisson mean and exact Hardy variance）

有

`int_R u(t)dmu(t)=m`,                               (4)

以及

`int_R[u(t)-m]^2dmu(t)`

` =(1/2)int_R|F(delta+it)-F(delta+1)|^2dmu(t)`.     (5)

#### 证明

式 (4) 是右半平面在 `delta+1` 的 Poisson formula。令
`A=F(delta+1)`。由 `F^2` 的 Poisson formula，

`int Re(F(delta+it)^2)dmu=Re(A^2)`.                 (6)

又

`(Re F)^2=(|F|^2+Re F^2)/2`.                       (7)

所以

`int (Re F)^2dmu-m^2`

` =[int|F|^2dmu-|A|^2]/2`.                         (8)

式 (4) 同时给
`int|F-A|^2dmu=int|F|^2dmu-|A|^2`，得到式 (5)。
logarithmic growth保证所需 weighted integrability；一般情形可先在内半平面
截断再用 monotone/dominated convergence。`□`

对 Abel candidates，式 (4) 的右侧完全可由低高度 arithmetic value
`F_Y(delta+1)` 计算；所以 signed Cauchy mass不是未知量。未知量是把这个
signed mean拆成 positive/negative parts 所需的 one-sided information。

## 2. 二阶矩上界及其结构性 no-go

对任意实数 `x` 与 `m>0`，

`x_-<= (x-m)^2/(4m)`,                              (9)

且常数 `4` 在 `x=-m` 取等。故有：

### 推论 YO（quadratic negative-part majorant）

若式 (3) 的 `m>0`，则

`J(F,delta)<=V(F,delta)/(4m)`,                     (10)

其中

`V(F,delta)=int_R[u(t)-m]^2/(1+t^2)dt`.            (11)

但是式 (10) 不能成为正确的 cofinal 闭合机制。事实上，圆盘中的
`g(q)=1+r q`, `0<r<1`，满足 `Re g>0`，故 negative part恒为零；其 boundary
variance却为 `r^2/2>0`。经 Cayley inverse得到同样的 half-plane例子。
所以“variance趋零”会错误地要求 passive limit接近常数，比中心线结论强得多。

这排除以下路线：分别对 prime、continuum、Gamma currents取 Cauchy--Schwarz，
再希望 total `L2` energy趋零。正确证明必须保留 pointwise/Toeplitz 的单边
相消，而不能只保留二阶大小。

## 3. Negative part 的 exact outer dual

令 Cayley map

`C_delta(q)=delta+(1+q)/(1-q)`, `|q|<1`.           (12)

normalized circle Haar measure在式 (12) 下推为 `dmu`。写

`g(q)=F(C_delta(q))`.                               (13)

对 `h in H^infinity(D)` 定义 Toeplitz/accretive form

`T_g[h]=Re int_T g(e^(itheta))|h(e^(itheta))|^2dm(theta)`. (14)

### 定理 YP（outer--Toeplitz duality for passive defect）

若 `u_- in L1(dmu)`，则

`J(F,delta)/pi`

` =sup_{h in H^infinity, ||h||_infinity<=1}[-T_g[h]]`. (15)

而且 supremum 可只在 outer functions上取。

#### 证明

点态 convex duality给

`int u_-dmu=sup_(0<=theta<=1)-int theta u dmu`.     (16)

任意 contractive `h` 的 boundary modulus给 `theta=|h|^2`，所以式 (15)
右侧不超过式 (16)。反之，对任意 measurable `0<=theta<=1`，令

`theta_epsilon=epsilon+(1-epsilon)theta`.           (17)

则 `log theta_epsilon in L1`。outer factorization给一个 contractive outer
`h_epsilon`，使 `|h_epsilon|^2=theta_epsilon` a.e.。令
`epsilon downarrow0` 并用 dominated convergence，即恢复式 (16)。`□`

式 (15) 是负部的精确信息，没有二阶矩损失。formal optimizer的 modulus是
negative set indicator；outer approximation把这个 measurable方向变成 Hardy
cyclic vector。因此文档 135--136 的“arithmetic cyclic invisibility”在这里
成为一个 exact variational identity，而不只是 sufficient estimate。

若

`g(q)=sum_(j>=0)a_jq^j`, `h(q)=sum_(k>=0)h_kq^k`,

则

`int g|h|^2dm=sum_(j,k>=0)a_jh_k conjugate(h_(j+k))`. (18)

所以式 (15) 也是一个 lower-triangular Toeplitz/Hodge matrix 在
`H^infinity` contractive cone 上的最负 numerical range。

## 4. Dirichlet characters become an inner semigroup

对 `lambda>=0` 定义

`Theta_lambda(q)=exp[-lambda(1+q)/(1-q)]`.          (19)

### 定理 YQ（Cayley--Dirichlet singular-inner representation）

族 `{Theta_lambda}` 满足：

1. `Theta_lambda` 是 singular inner function；
2. `Theta_lambda Theta_mu=Theta_(lambda+mu)`；
3. `Theta_lambda(0)=e^(-lambda)`；
4. 若 `C_delta(e^(itheta))=delta+it`，则其 a.e. boundary value为
   `e^(-itlambda)`。

因此取 `lambda=log n` 时，

`n^(-1/2-delta-it)`

` =n^(-1/2-delta)Theta_(log n)(e^(itheta))`,        (20)

而 `Theta_(log m)Theta_(log n)=Theta_(log(mn))` 精确实现整数乘法。

#### 证明

`Re[(1+q)/(1-q)]>0` 在圆盘内成立，boundary上除 `q=1` 外为纯虚数，故
`Theta_lambda` 内部 contractive、boundary modulus为一。其余各项直接由
exponential law与式 (12) 得到。`□`

乘法算子 `M_(Theta_lambda)` 因而是 `H^2(D)` 上的 isometric semigroup。
Euler prime powers不再只是 scalar oscillations，而成为同一 inner flow 的
离散 arithmetic times。

## 5. Abel candidate 的 exact inner-semigroup form

令

`s_delta(q)=1/2+delta+(1+q)/(1-q)`.                (21)

文档 132 的 Abel candidate经 Cayley transform后精确为

`g_(Y,delta)(q)=A_infinity(s_delta(q))`

` +int_1^infinity x^(-1/2-delta)e^(-x/Y)`

`                  Theta_(log x)(q)dx`

` -sum_(n>=2)Lambda(n)n^(-1/2-delta)e^(-n/Y)`

`                  Theta_(log n)(q)`.              (22)

所以定理 YP 把 Cauchy defect写成

`J_(Y,delta)/pi=sup_(||h||_infinity<=1)(-Re{`

` <A_infinity(s_delta)h,h>`

` +int x^(-1/2-delta)e^(-x/Y)<Theta_(log x)h,h>dx`

` -sum Lambda(n)n^(-1/2-delta)e^(-n/Y)`

`                         <Theta_(log n)h,h>} )`.   (23)

式 (23) 保留了：

- prime orbit与continuum orbit之间的 signed cancellation；
- Gamma current的 positive archimedean barrier；
- 所有 multiplicative relations `log(mn)=logm+logn`；
- negative set通过 outer cyclic vector产生的自适应方向。

逐项使用 `||M_(Theta_lambda)||=1` 只会退化为 coefficient absolute mass，
它随 `Y` 增长，不能证明式 (23) 的负部趋零。因此任何成功估计必须对完整
signed measure使用 semigroup cancellation，不能逐 prime取 operator norm。

## 6. Inner-semigroup filtered Weil structure theorem

上述结构不依赖整数的特殊命名。令 `Gamma` 是 additive orbit semigroup，
`Theta:Gamma->H^infinity(D)` 是 inner isometric representation，候选 currents
具有

`g_n=A_n+int_Gamma Theta_lambda dnu_n(lambda)`.     (24)

其中 `nu_n` 可以是 discrete-minus-continuous signed orbit measure。

### 定理 YR（contractive-inner filtered center-line theorem）

设 `g_n` 对应一列满足文档 136 定理 YL 的 self-dual arithmetic candidates，
但把其 `J_n->0` 假设替换为

`sup_(||h||_infinity<=1)[-Re<h,g_nh>]->0`.         (25)

则 arithmetic germ 有唯一 positive-real continuation，相应 self-dual
order-one divisor 的全部 zeros 位于中心轴。

#### 证明

定理 YP说明式 (25) 恰等于 `J_n/pi->0`。应用定理 YL与文档 131 定理 XQ。
`□`

定理 YR 是一个更代数化的广义 Weil 结构：finite-field Frobenius purity使用
exact positive intersection form；这里 inner orbit semigroup提供等距动力学，
contractive outer cone提供 cyclic test objects，而式 (25) 是 filtered
Hodge--Riemann accretivity。它适用于任意具有 additive length spectrum、
self-dual determinant与 Poisson-admissible regularization的 Euler/Selberg型
数据。

## 7. Abel 数值 audit：variance 路线确实失配

`zeta_abel_cauchy_negative_mass_audit` 现在同时返回：

- exact Poisson signed target `pi Re F_Y(delta+1)`；
- sampled signed Cauchy integral及未扫描 tail residual；
- centered quadratic integral `V`；
- 当 center mean为正时的式 (10) 上界。

取 `delta=.1`, `N=40Y`, `H=2Y`, step `.25`：

| `Y` | center mean `m` | sampled `J` | sampled `V` | `V/(4m)` | upper / `J` |
|---:|---:|---:|---:|---:|---:|
| 10 | `-1.07e-2` | `1.82e-1` | `4.63e-2` | unavailable | unavailable |
| 30 | `2.92e-2` | `5.63e-2` | `1.64e-1` | `1.40` | `24.9` |
| 100 | `4.42e-2` | `1.16e-2` | `2.97e-1` | `1.68` | `144.8` |

实际 negative defect快速下降时，quadratic upper反而变坏。这与推论 YO 的
抽象 no-go一致，说明下一步不应继续优化 scalar variance常数。

这些仍是非区间 sampled diagnostics；尤其 `V` 只积分到 `H`，不是 full-line
rigorous upper。它们用于选择解析结构，不是 zero evidence。

## 8. 下一输入

经典 RH 的剩余量现在有一个精确 algebraic form：证明式 (23) 在全部
contractive outer vectors上 asymptotically accretive。合理入口是：

1. 把 `r_h(lambda)=<Theta_lambda h,h>` 视为 inner shift semigroup 的
   positive-definite correlation，刻画所有 contractive outer `h` 可产生的
   correlation cone；
2. 在这个 cone 上比较 prime orbit measure
   `sum Lambda(n)n^(-1/2-delta)e^(-n/Y)delta_(log n)` 与 continuum measure，
   而非比较其 total variation；
3. 将 Gamma term识别为 semigroup generator的 positive boundary energy，
   寻找一条对全部 correlation cone统一的 arithmetic Hodge inequality。

若第 2--3 项成立，定理 YR 已完成从 inner-semigroup 极化到中心线的全部桥接。

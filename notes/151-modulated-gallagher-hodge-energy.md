# 调制 Gallagher--Hodge 能量与乘法短区间结构

文档 150 把 zeta Abel negative trace尚未控制的频率核心缩到
`sqrt(Y)delta^(-3/2)logY`。下一步看似可直接调用 primes in short intervals或
Selberg variance；本节证明这一步必须保留一个关键 modulation。频率块
`[tau-B,tau+B]` 平移到原点时，lag measure同时乘上 `e^(-itau lambda)`。

正确的 arithmetic对象因此不是 ordinary short-interval discrepancy，而是
**modulated multiplicative short-interval energy**。它仍然是完全正的 triangular
Gram，并给出另一类足够广泛的 Weil/Hodge 结构定理。

## 1. Frequency-shifted Gallagher energy

令 `nu` 是 real line上的 finite complex measure，并定义 Fourier current

`D(t)=int_R e^(-itlambda)dnu(lambda)`.             (1)

对 center `tau`、half-bandwidth `B>0` 及 fixed `0<theta<1`，令

`dnu_tau(lambda)=e^(-itaulambda)dnu(lambda)`,      (2)

`h=theta/B`,                                      (3)

`G_nu(tau,B;theta)`

` =int_R |nu_tau([x,x+h])|^2dx`.                  (4)

### 定理 AAM（frequency-shifted Gallagher inequality）

存在只依赖 `theta` 的 `C_theta<infinity`，使

`int_(tau-B)^(tau+B)|D(t)|^2dt`

` <=C_theta B^2 G_nu(tau,B;theta)`.               (5)

#### 证明

写 `t=tau+s`，则

`D(tau+s)=int e^(-islambda)dnu_tau(lambda)`.       (6)

对 measure `nu_tau` 应用 Gallagher exponential-sum lemma（文献 32，Lemma 1）
即得式 (5)。原引理先对 discrete absolutely convergent sums陈述；以 compact
truncation及 atomic weak approximation应用，并用 Fatou/Tonelli passage可得 finite
measure版本。`□`

modulation式 (2)不是符号装饰：它精确记录正在审计哪个 vertical frequency block。

## 2. 从 modulated energy 到 negative Hodge trace

在 block `I=[tau-B,tau+B]` 上写 real Hodge symbol

`H(t)=A(t)+R(t)+Re D(t)`,                          (7)

并假设 `A>=b>0`, `|R|<=r<b`，记 `beta=b-r`。再令

`T_I=max(0,|tau|-B)`.                             (8)

### 定理 AAN（Gallagher barrier--capacity transfer）

有

`int_I H_-(t)dt<=C_theta B^2G_nu/(4beta)`,        (9)

以及

`int_I H_-(t)dmu(t)`

` <=C_theta B^2G_nu`

`   /[4pibeta(1+T_I^2)]`,                         (10)

其中 `dmu=dt/[pi(1+t^2)]`。

#### 证明

文档 150 引理 AAI取 `p=2` 给第一步

`int_IH_-<=int_I(|D|-beta)_+<=int_I|D|^2/(4beta)`. (11)

代入定理 AAM得到式 (9)。block上 Cauchy density至多
`1/[pi(1+T_I^2)]`，给式 (10)。`□`

对 dyadic blocks `tau=3T/2,B=T/2`，式 (10)中的 `B^2/(1+T_I^2)` 一致有界；
所以真正需要求和的是 `G_nu(tau,B)/beta`，而不是 deepest character well。

## 3. 广义 modulated-energy Weil structure theorem

令 `F_n` 满足文档 145 定理 ZT的 Poisson/Euler-germ hypotheses，令
`H_n(t)=Re F_n(delta_n+it)`。把 real line分成一个 core与 disjoint blocks
`I_(n,k)=[tau_(n,k)-B_(n,k),tau_(n,k)+B_(n,k)]`。假设每块有式 (7)的
arithmetic measure realization `nu_(n,k)` 与 barrier `beta_(n,k)`。

### 定理 AAO（modulated Gallagher--Hodge Weil theorem）

若

`sup_n {int_core(H_n)_-dmu`

` +sum_k B_(n,k)^2 G_(nu_(n,k))(tau_(n,k),B_(n,k);theta)`

` /[beta_(n,k)(1+T_(n,k)^2)]}<infinity`,          (12)

其中 `T_(n,k)=max(0,|tau_(n,k)|-B_(n,k))`，则相应 self-dual divisor的
全部 zeros位于中心线。

#### 证明

定理 AAN对 blocks求和给 full Cauchy negative trace一致有界；固定常数
`C_theta/(4pi)` 可吸收进式 (12)。应用文档 149 定理 AAE或文档 145 定理 ZT。
`□`

这是比文档 150 AAJ更 arithmetic的结构包：

1. additive length group与 unitary character modulation；
2. signed arithmetic lag measure；
3. interval-incidence differential；
4. positive triangular Gram/carré-du-champ；
5. archimedean barrier；
6. finite negative trace gluing。

有限域 Hodge--Riemann中相应负能量为零；数域只需式 (12) bounded。

## 4. Zeta 的无条件 arithmetic realization

令 `sigma=1/2+delta`，并在 logarithmic length `lambda=logu` 上定义

`dnu_(Y,delta)(lambda)`

` =e^(-sigmalambda)e^(-e^lambda/Y)`

`                       d[psi(e^lambda)-e^lambda]`. (13)

则

`D_(Y,delta)(t)=int e^(-itlambda)dnu_(Y,delta)`

`                 =P_Y(t)-I_Y(t)`,                (14)

而 Abel impedance满足

`F_Y(delta+it)=A_infinity(delta+it)-D_(Y,delta)(t)`. (15)

所以 zeta 的 modulated short-interval energy是完全显式的 prime--continuum平方

`G_(Y,delta)(tau,B;theta)`

` =int_0^infinity |int_(e^x)^(e^(x+theta/B))`

` u^(-sigma-itau)e^(-u/Y)d[psi(u)-u]|^2dx`.       (16)

式 (13)--(16)及 positivity全部无条件存在；没有引用 zeros。结合 vertical
Stirling barrier，定理 AAO说明：若 dyadic `(tau,B)` 上的式 (16)按
`G/logT` 可和，并且低频 core有 bounded negative trace，则 RH成立。

对 fixed-degree paired tempered Euler data，只需把 `dpsi` 换成相应 generalized
von Mangoldt/Satake signed measure；unitary local phases已被式 (13)与 modulation
吸收，定理 AAO逐字适用。

## 5. 删除 modulation 的严格 no-go

### 命题 AAP（ordinary Selberg energy cannot replace modulated energy）

不存在只依赖 `h` 的 universal常数，以 ordinary sliding energy

`int|nu([x,x+h])|^2dx`                            (17)

控制全部 centers `tau` 的式 (4)。即使 `nu` 有 real smooth density也失败。

#### 证明

在 circle `R/(LZ)` 上取 `L` 为 `h` 的整数倍、`tau=2pi/h`，并令

`dnu(lambda)=cos(taulambda)dlambda`.              (18)

每个长度 `h` 的 ordinary interval恰包含一个 cosine period，故式 (17)为零。
但调制后

`e^(-itaulambda)cos(taulambda)`

` =(1+e^(-2itaulambda))/2`,                       (19)

每个长度 `h` interval的 mass为 `h/2`，所以 modulated energy为
`Lh^2/4>0`。把 circle切开并远离 endpoints，或取许多 periods后令其数目趋于
无穷，给 real-line finite-measure反例。`□`

因此 ordinary prime short-interval PNT、Brun--Titchmarsh或未调制 Selberg
integral不能被直接代入式 (10)。它们可以参与控制式 (16)，但必须保留
`u^(-itau)` 或证明一个额外 maximal/modulated comparison。这个 no-go阻止了一条
看似会免费越过平方根核心、实际删除关键 resonance phase的错误捷径。

## 6. Finite triangular Hodge Gram

对 atomic lag measure `nu=sum_jc_jdelta_(lambda_j)`，定义
`z_j=c_je^(-itaulambda_j)`。滑动 intervals的 overlap长度给 exact identity。

### 定理 AAQ（modulated triangular-Gram identity）

`G_nu(tau,B;theta)`

` =sum_(j,k)z_jconj(z_k)(h-|lambda_j-lambda_k|)_+`, (20)

其中 `h=theta/B`。矩阵

`K_h(j,k)=(h-|lambda_j-lambda_k|)_+`              (21)

半正定。

#### 证明

atom `lambda_j` 属于 `[x,x+h]` 当且仅当
`x in [lambda_j-h,lambda_j]`。第 `j,k` 两个 indicator的 inner product就是两区间
intersection长度 `(h-|lambda_j-lambda_k|)_+`。因此式 (20)是这些 indicators的
Gram norm，式 (21)半正定。`□`

实现 `stationary_modulated_interval_energy` 直接计算式 (20)，返回 diagonal、
off-diagonal、phase coefficients与 positivity residual。排序后，对每个 `j` 只需
维护 `|lambda_j-lambda_k|<h` 的 `sum conj(z_k)` 与
`sum lambda_kconj(z_k)` 两个 sliding prefixes，故 exact计算为 `O(m logm)` 而非
dense `O(m^2)`。它把 Gallagher RHS变成可扩展的 finite positive Hodge energy，
而不是 sampled height integral。

同文档 149--150 的 shared quadrature，以 `theta=.25` 审计 pure
prime--continuum discrepancy：

| `Y` | `T` | modulated `G` | diagonal | off-diagonal | trace proxy |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | .1007 | .3172 | -.2165 | .0201 |
| 10 | 8 | .0683 | .0793 | -.0110 | .00809 |
| 10 | 32 | .01981 | .01983 | `-2.0e-5` | .00143 |
| 30 | 2 | .2537 | 1.1573 | -.9036 | .0507 |
| 30 | 8 | .2248 | .2893 | -.0645 | .0266 |
| 30 | 32 | .06807 | .07233 | -.00425 | .00491 |

这里 trace proxy为省略 `C_theta/(4pi)` 的
`B^2G/[(1+T^2)log(max(e,T))]`。低频的大幅 negative off-diagonal展示了
prime--continuum cancellation确实被 triangular Gram捕获；所有数字仍是非区间
finite diagnostics，不证明式 (22)。

## 7. 与当前 large-values 理论的接口

Guth--Maynard 的最新 large-values theorem给出改进的 zeta zero-density exponent
`30/13`，并推出长度 `x^(17/30+o(1))` 的 prime short-interval asymptotics
（文献 33）。这些结果直接说明 sophisticated large-value geometry确实能超越
generic Montgomery--Vaughan mean square。

但其已陈述推论不是式 (16)的 uniform modulated energy bound；从该论文的
large-value estimates推导式 (12)仍需保留 Abel weights、所有 dyadic centers及
Cauchy summability。本文档不把 short-interval PNT本身冒充这一缺失推导。

## 8. 下一步

剩余目标现在可以精确写成：对 `tau asymp B asymp T` 证明

`sum_(dyadic T) G_(Y,delta)(tau,B;theta)/logT=O(1)` (22)

在平方根 core的 exterior部分，文档 150已由 generic mean square完成；真正新输入
只需覆盖其 interior。可能入口是：

1. 把 Guth--Maynard superlevel bounds转成式 (16)的 weighted distribution bound；
2. 对 modulated short prime sums使用 Heath--Brown/Vaughan identity分成 Type I/II；
3. 保持 continuum subtraction在每个 local interval内，再应用 bilinear large sieve；
4. 直接认证 finite triangular Grams的 block sums，而不恢复 pointwise prime PNT。

这比“证明某个 Selberg variance bound”更精确：所需 phase、window、weight与最终
Cauchy capacity全部已固定。

文档 152 进一步证明 triangular energy与 Fejér-localized Fourier energy的 exact
Plancherel identity，并把 Dirichlet convolution实现为 lag-translation tensor
synthesis，从而给 Vaughan/Heath--Brown Type I/II 分解一个明确的 Bessel--Hodge
判据。

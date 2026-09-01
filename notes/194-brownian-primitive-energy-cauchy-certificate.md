# NCE-8：Brownian primitive energy 与 direct Cauchy certificate

文档 192--193 把 degree-two canonical response 压缩成 direct Cauchy cumulative
profile，并说明 full mass-dependent Volterra primitive 不能拆开估计。本笔记
再弱化所需的 arithmetic input：不必一致控制 cumulative profile 的 weighted
$L^1$ capacity；一个 global constant mode 加一个 positive Brownian
primitive $L^2$ energy 已经足够。

对任意 finite Hermitian lag response $q$，定义

$$T_q=q(\mathbb R),$$                              (1)

以及 Brownian energy

$$\mathcal E_B(q)
=\frac12\sum_{\omega,\eta}
q_\omega\overline{q_\eta}
\left(
|\omega|+|\eta|-|\omega-\eta|
\right).$$                                       (2)

本笔记证明

$$\left|\sum_\omega q_\omega e^{-|\omega|}\right|
\le |T_q|+\sqrt{\mathcal E_B(q)}.$$               (3)

式 (2) 是 positive Gram，并有 exact prefix-square representation。对
degree-two zeta response，$T_q$ 是一个显式 scalar polynomial，
$\mathcal E_B(q)$ 则是完整 $M$-dependent response 的单一正能量。这给
bounded finite-trace Hodge--Weil theorem 一个比 Cauchy profile capacity 更弱的
充分接口。

## 1. Centered primitive

令 $q$ 是 compactly supported finite complex measure，满足 Hermitian symmetry

$$q(-E)=\overline{q(E)}.$$                         (4)

令

$$\mu=q-T_q\delta_0,$$                             (5)

则 $\mu(\mathbb R)=0$。取 vanishing-at-infinity primitive $A_q$，使

$$DA_q=\mu.$$                                      (6)

对 finite atomic $q$，$A_q$ 是 compactly supported step function。

### 定理 AHA（direct Cauchy primitive bound）[U]

有

$$\int e^{-|x|}\,dq(x)
=T_q-\int K_C'(x)A_q(x)\,dx,$$                   (7)

其中 $K_C(x)=e^{-|x|}$。因此

$$\left|\int e^{-|x|}\,dq(x)\right|
\le |T_q|+\|A_q\|_2.$$                            (8)

#### 证明

因为 $K_C(0)=1$，

$$\int K_C\,dq
=T_q+\int K_C\,d\mu.$$                            (9)

由 $\mu=DA_q$ 作 distributional integration by parts，得到式 (7)。又

$$|K_C'(x)|=e^{-|x|},\qquad
\|K_C'\|_2^2=\int_{\mathbb R}e^{-2|x|}dx=1.$$     (10)

Cauchy--Schwarz 给式 (8)。$\square$

与文档 192 的 profile-capacity criterion 相比，式 (8) 允许 cumulative profile
在不同 radii 改变符号；它只读取 primitive 的 quadratic energy。

## 2. Brownian Gram identity

写

$$q=\sum_{\omega\in\Omega}q_\omega\delta_\omega.$$ (11)

### 定理 AHB（Brownian variogram equals primitive energy）[U]

有

$$\|A_q\|_2^2=\mathcal E_B(q),$$                  (12)

其中 $\mathcal E_B$ 由式 (2) 给出。特别地，该 quadratic form positive
semidefinite。

#### 证明一：Plancherel

令

$$\widehat q(t)=\sum_\omega q_\omega e^{-i\omega t}.$$ (13)

则 $T_q=\widehat q(0)$，且

$$\widehat {A_q}(t)
=\frac{\widehat q(t)-\widehat q(0)}{it}.$$        (14)

Plancherel 给

$$\|A_q\|_2^2
=\frac1{2\pi}\int_{\mathbb R}
\frac{|\widehat q(t)-\widehat q(0)|^2}{t^2}dt.$$  (15)

逐项展开并使用

$$\int_{\mathbb R}
\frac{(e^{-i\omega t}-1)(e^{i\eta t}-1)}{t^2}dt
=\pi\left(
|\omega|+|\eta|-|\omega-\eta|
\right)$$                                        (16)

即得式 (12)。

#### 证明二：prefix squares

定义 Brownian kernel

$$K_B(\omega,\eta)
=\frac{|\omega|+|\eta|-|\omega-\eta|}{2}.$$      (17)

若 $\omega,\eta$ 异号，则 $K_B=0$；若同为正，

$$K_B(\omega,\eta)=\min(\omega,\eta)
=\int_0^\infty
\mathbf1_{h\le\omega}\mathbf1_{h\le\eta}\,dh.$$  (18)

负半轴相同。因此

$$\mathcal E_B(q)
=\int_0^\infty
\left|\sum_{\omega\ge h}q_\omega\right|^2dh
+\int_0^\infty
\left|\sum_{\omega\le-h}q_\omega\right|^2dh.$$   (19)

这既证明 positivity，也与 step primitive 的 $L^2$ norm 相同。$\square$

式 (19) 是一个真正的 Hodge-square representation：每个 lag threshold 给一个
rank-one prefix effect，Brownian energy 是这些 squares 的正积分。

## 3. Degree-two canonical response

令 stationary symbol 为

$$P(t)=\sum_\omega d_\omega e^{-i\omega t},\qquad
M=P(0)=\sum_\omega d_\omega,$$                    (20)

并令 $L=\alpha B$，$\alpha=\sqrt3/2$。degree-two response polynomial 是

$$\widehat q_2(t)
=-c_2^2P(t)^3(P(t)-L)^2.$$                       (21)

因此 global coefficient sum 精确为

$$T_{q_2}
=-c_2^2M^3(M-L)^2.$$                             (22)

### 推论 AHC（response-specific Brownian certificate）[U]

有

$$\left|
-c_2^2\int P(t)^3(P(t)-L)^2\,d\mu_C(t)
\right|$$

$$\le
c_2^2|M|^3|M-L|^2+\sqrt{\mathcal E_B(q_2)}.$$    (23)

并且

$$\mathcal E_B(q_2)
=\frac{c_2^4}{2\pi}
\int_{\mathbb R}
\frac{
|P(t)^3(P(t)-L)^2-M^3(M-L)^2|^2
}{t^2}\,dt.$$                                    (24)

#### 证明

式 (22) 来自 frequency coefficients 全部求和，即在 $t=0$ 评价式 (21)。
把定理 AHA--AHB 应用于 $q_2$ 得式 (23)。式 (24) 是式 (15) 对
$\widehat q_2$ 的直接代入。$\square$

式 (24) 保留了 full $M$ dependence；没有把 balanced square 与 mass
correction 分开，也没有把三、四、五阶 moments 分开。

## 4. Generalized Hodge--Weil interface

沿文档 187 的 polynomial soft effect 与文档 149 的 bounded finite-trace
Hodge--Weil theorem：

### 推论 AHD（Brownian-energy center-line criterion）[C]

设 cofinal arithmetic currents 的 canonical response maps 为 $q_n$。若

$$\sup_n
\left[
|T_{q_n}|+\sqrt{\mathcal E_B(q_n)}
+2\rho_n
+5\epsilon_n\tau_n(|H_n|)
+\eta_n
\right]<\infty,$$                                (25)

其中 $\eta_n$ 包含 Gamma、quadrature 与 tail errors，则目标 self-dual
order-one divisor 的全部非零 zeros 位于中心线。

#### 证明

定理 AHA--AHB 用式 (25) 控制 canonical signed response。文档 187 定理 AGB
把 negative spectral trace 控制在该 response 加后三项误差之下；文档 149
定理 AAE 再推出中心线 purity。$\square$

这是一个新的广义结构接口：

- algebraic layer：finite Hermitian lag response；
- Hodge layer：Brownian prefix-square Gram；
- analytic layer：constant mode 与 primitive energy 一致有界；
- arithmetic realization：由 Euler/continuum/Gamma data 构造 $q_n$。

它仍是 conditional criterion；当前没有证明 zeta 的式 (25)。

## 5. 与 full Selberg profile 的区别

$\mathcal E_B(q_2)$ 只控制一个 degree-two canonical nonlinear response 的
prefix tails。它不要求：

- 原 prime current 的全部 short intervals；
- arbitrary coefficient directions；
- 全部 moments 的 PSD；
- pointwise Loewner positivity。

full Selberg profile 可能推出式 (24)，但反向蕴含目前没有建立。所以下一步应先
尝试 response-specific Type I/II factorization，再审计是否被迫恢复文档 169 的
完整等价条件。

## 6. Finite audit

脚本 scripts/formal_lag_response.py 用排序后的 centered cumulative sums 在
$O(n\log n)$ 时间计算 $\|A_q\|_2^2$，无需形成 dense Brownian Gram。

冻结 degree-two models 给：

| $Y,N$ | $T_q$ | $\|A_q\|_2$ | actual response | bound | bound/actual |
|---:|---:|---:|---:|---:|---:|
| $4,7$ | $.004042$ | $.01731$ | $.004942$ | $.02135$ | $4.32$ |
| $8,10$ | $.000538$ | $.02187$ | $.004495$ | $.02241$ | $4.98$ |
| $12,12$ | $5.47\,10^{-7}$ | $.02404$ | $.005632$ | $.02404$ | $4.27$ |
| $16,15$ | $-.000157$ | $.02331$ | $.007958$ | $.02347$ | $2.95$ |

Brownian energy 本身为约

$$.000300,\ .000478,\ .000578,\ .000543,$$        (26)

在这四个小尺度没有随 coefficient variation 一起快速增长。上界只松约
$3--5$ 倍，比 generic absolute moment/variation bounds 明显紧。

这些仍是 double-precision finite diagnostics，且使用 $\rho=B/3$；不构成
cofinal estimate 或 RH evidence。

## 7. 下一最小引理

1. 把式 (19) 的 prefix sums 按 prime/continuum provenance 写成
   response-specific Type I/II blocks；
2. 证明或否证 $\mathcal E_B(q_Y)=O(1)$ 是否可由文档 153--168 的现有
   Vaughan--Volterra machinery 在不调用 full Selberg profile 时得到；
3. 单独审计 scalar term
   $c_2^2|M|^3|M-L|^2$，寻找比 classical PNT absolute error 更强的 canonical
   cancellation；
4. 推广式 (2) 到 growing-degree Chebyshev response，同时避免文档 191 的
   coefficient tax；
5. 若 Brownian prefix energy 等价于 full Selberg profile，明确停止该路线。

## 8. 审计结论

direct Cauchy response 有一个精确的 positive Brownian Hodge certificate：
constant mode 加 primitive prefix-square energy。它自动保留 full
$M$-dependent Volterra cancellation，并把所需算术输入降为一个指定 nonlinear
response 的单一正 Gram。下一阶段的核心问题是无循环地证明式 (24)--(25) 的
uniform bound。

# 247. Exact lag quotient、cluster-safe Brownian 分母与 TV 稳定性

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：B1e rationalization / finite Brownian
denominator

状态：algebraic-grid lag quotient、rational logarithm enclosure、cluster-safe
primitive energy upper bound、TV perturbation bound及 convolution-polynomial error
compression 为 [T]；Hermite--Lindemann 输入为 [R]；固定 `(8,10,4)` 的有理替身
分母对替身本身为 [T]，对 intended transcendental coefficients 的比较仅为 [E]；
真实 coefficient TV radius及 good-cell numerator 的
directed enclosure 为 [O]。本笔记不更新 PDF，不声称 RH/GRH、uniform B1a 或新的
零点比例。

## 1. 本轮推进与错误定位

笔记 246 把 B1e 的第一个目标冻结为

\[
 (Y,N,J)=(8,10,4),\qquad h=0.005,
\tag{1}
\]

并要求对宽 ratio band `[1/4,4]` 证明

\[
 N_{\rm lower}/D_{\rm upper}>0.10.
\tag{2}
\]

直接把 degree-two response 的 3--4 万个 formal atoms转成 IEEE double位置时，
出现大量 `1.11e-16` 间隙。逆向检查表明，这些并非真实的对数小除数，而是同一
uniform-grid平移由不同 basis coordinates表示后产生的舍入分裂。例如，本应等于
`-2.03` 的若干组合被转成相差 `2e-16` 的 doubles。

本轮先解决分母几何，而不把完整 coefficient interval计算隐藏在大规模逐项区间
卷积中。核心步骤是：

1. 在 formal convolution之后、数值排序之前，先取 exact algebraic-grid quotient；
2. 用正项 `atanh` 级数给每个 logarithmic lag有理上下界；
3. 即使位置区间重叠，也用 cluster hull给 Brownian primitive energy上界；
4. 用单一 response total-variation error把有理替身分母转移到真实分母；
5. 用 measure convolution Banach algebra在 base coefficients层估计该 TV error。

这把原先 2 万多个 response coefficient intervals压缩成少量 base coefficient
intervals及一个显式多项式 Lipschitz ledger。

## 2. Algebraic-grid lag quotient

令 `r` 为正有理数，`c=(c_1,...,c_J) in Z^J`，且 grid nodes
`u_1,...,u_J` 为实代数数。formal lag的实际位置是

\[
 \Phi(r,c)=\log r+\sum_{j=1}^J c_j u_j.
\tag{3}
\]

定义 exact quotient key

\[
 K(r,c)=\left(r,\sum_{j=1}^Jc_ju_j\right).
\tag{4}
\]

### 定理 247-A（algebraic-grid quotient is exact）[T]

对上述 lags，

\[
 \Phi(r,c)=\Phi(s,d)
 \quad\Longleftrightarrow\quad
 K(r,c)=K(s,d).
\tag{5}
\]

#### 证明

反向显然。正向令

\[
 \alpha=\sum_j(d_j-c_j)u_j.
\]

则 `alpha` 为实代数数且 `exp(alpha)=r/s` 为代数数。Hermite--Lindemann 定理
[R] 断言非零代数数 `alpha` 的指数是超越数，故只能 `alpha=0`，继而
`r/s=1`。所以 `r=s` 且两个 algebraic shifts相同，即式 (4)相同。`square`

这里使用的是经典 Hermite--Lindemann 定理，而不是 RH、PNT误差或任何 Weil
positivity。对当前 uniform rational grid，shift本身是 `Fraction`，式 (4)可由整数
算术直接计算。

可核查来源：[Manuel Eberl, *The Hermite--Lindemann--Weierstrass
Transcendence Theorem*, Archive of Formal Proofs (2021)](https://isa-afp.org/entries/Hermite_Lindemann.html)。
该形式化条目明确列出所用推论：对任意非零代数数 `z`，`exp(z)` 为超越数 [R]。

当前固定网格为

\[
 (u_1,u_2,u_3,u_4)
 =\left(\frac{221}{800},\frac{123}{160},
 \frac{1009}{800},\frac{1403}{800}\right).
\tag{6}
\]

## 3. 无黑箱 logarithm 的有理 enclosure

对正有理数 `x`，唯一取整数 `m` 使

\[
 y=2^{-m}x\in[1,2).
\]

置 `z=(y-1)/(y+1)`，则 `0<=z<1/3` 且

\[
 \log y=2\sum_{k=0}^{n-1}\frac{z^{2k+1}}{2k+1}+R_n,
\qquad
0\le R_n\le
\frac{2z^{2n+1}}{(2n+1)(1-z^2)}.
\tag{7}
\]

`log 2` 使用同一公式、`z=1/3`。全部 partial sums和 remainder bounds均为
exact rationals。

### 引理 247-B（rational logarithm interval）[T]

式 (7)与

\[
 \log x=m\log2+\log y
\tag{8}
\]

给 `log x` 的显式有理闭区间；当 `m<0` 时交换 `m log 2` 的上下端点。其宽度
按 `O(3^{-2n}/n)` 衰减。

#### 证明

恒等式 `log y=2 atanh(z)` 给正项级数。尾项中以
`2k+1>=2n+1` 后提出分母，再求几何级数，得到式 (7)。式 (8)及区间加法给结论。
`square`

在 `(Y,N,J)=(8,10,4)` 的五次 response support中，所有 rational ratios只含
primes `2,3,5,7`。实现因而先分别 enclosure `log 2,log 3,log 5,log 7`，再按
prime exponents组合，避免对两万多个 ratios重复求级数。

## 4. Cluster-safe Brownian energy

令

\[
 \mu=\sum_{i=1}^m c_i\delta_{x_i},
 \qquad \sum_i c_i=0,
\]

并令 `A_mu(t)=mu((−infinity,t])`。Brownian primitive energy为

\[
 \mathcal E(\mu)=\int_{\mathbb R}|A_\mu(t)|^2dt.
\tag{9}
\]

假设只知 `x_i in I_i=[a_i,b_i]`。把相交的 intervals传递合并成 disjoint
cluster hulls

\[
 H_q=[A_q,B_q],\qquad B_q<A_{q+1}.
\]

令 `C_q` 为第 `q` 个 cluster的 atom集合，

\[
 S_{q-1}=\sum_{r<q}\sum_{i\in C_r}c_i,
 \qquad V_q=\sum_{i\in C_q}|c_i|,
 \qquad S_q=S_{q-1}+\sum_{i\in C_q}c_i.
\tag{10}
\]

### 定理 247-C（cluster-safe denominator upper bound）[T]

不需要知道每个 cluster内部的 atom顺序，就有

\[
\boxed{
 \mathcal E(\mu)\le
 \sum_q(B_q-A_q)(|S_{q-1}|+V_q)^2
 +\sum_{q< Q}(A_{q+1}-B_q)|S_q|^2.}
\tag{11}
\]

若所有 position intervals均为 singleton，则式 (11)退化为 exact prefix公式

\[
 \mathcal E(\mu)=\sum_{i=1}^{m-1}
 \left|\sum_{j\le i}c_j\right|^2(x_{i+1}-x_i).
\tag{12}
\]

#### 证明

在 hull `H_q` 内，尚未穿过哪些 atoms可能未知，但 primitive等于 incoming mass
加 cluster atoms的某个部分和，所以其模至多 `|S_(q-1)|+V_q`。在 gap
`(B_q,A_(q+1))` 内，第 `q` 个 cluster已全部穿过而下一 cluster尚未开始，primitive
恒等于 `S_q`。在最左 hull之前 primitive为零；总质量为零使最右 hull之后也为零。
分别以区间长度积分即得式 (11)。singleton情形的 hull项为零，gap项恰为式 (12)。
`square`

删除 exact zero-mass条件后，最右侧 primitive未必消失，整条实线上的能量可为
无穷；因此 centering不是可省略的技术条件。

## 5. 从有理替身到真实分母

令 `mu` 与 `mu_tilde` 都是零质量有限测度，且共同支撑于长度至多 `L` 的 interval。
假设

\[
 \|\mu-\widetilde\mu\|_{TV}\le\varepsilon,
 \qquad
 \mathcal E(\widetilde\mu)\le\widetilde D_U.
\tag{13}
\]

### 定理 247-D（TV-stable Brownian denominator）[T]

对任意 rational `tau>0`，

\[
\boxed{
 \mathcal E(\mu)
 \le(1+\tau)\widetilde D_U
 +(1+\tau^{-1})L\varepsilon^2.}
\tag{14}
\]

#### 证明

置 `nu=mu-mu_tilde`。因 `nu` 零质量并支撑于长度 `L` 的 interval，
`A_nu` 在该 interval外为零，且逐点

\[
 |A_\nu(t)|\le\|\nu\|_{TV}\le\varepsilon.
\]

所以 `||A_nu||_2<=sqrt(L) epsilon`。Minkowski不等式给

\[
 \sqrt{\mathcal E(\mu)}
 \le\sqrt{\widetilde D_U}+\sqrt L\varepsilon.
\]

平方并用 `2ab<=tau a^2+tau^(-1)b^2` 即得式 (14)。`square`

式 (14)的右端完全是 rationals，只要 `D_tilde_U,L,epsilon,tau` 使用有理上界。
它比给每个 expanded response coefficient单独传播 interval更适合独立审计。

## 6. Convolution Banach algebra error compression

有限复测度在 convolution及 total-variation norm下是 Banach algebra。设

\[
 Q(X)=\sum_{k=0}^d a_kX^k,
 \qquad
 \widetilde Q(X)=\sum_{k=0}^d\widetilde a_kX^k,
\]

并有

\[
 \|d\|_{TV},\|\widetilde d\|_{TV}\le S,
 \quad \|d-\widetilde d\|_{TV}\le\delta,
 \quad |a_k|\le A_k,
 \quad |a_k-\widetilde a_k|\le E_k.
\tag{15}
\]

### 定理 247-E（polynomial response TV ledger）[T]

有

\[
\boxed{
 \|Q(d)-\widetilde Q(\widetilde d)\|_{TV}
 \le
 \delta\sum_{k=1}^d kA_kS^{k-1}
 +\sum_{k=0}^dE_kS^k.}
\tag{16}
\]

若 `h=d_j-m_j delta_0`、`h_tilde=d_j_tilde-m_j_tilde delta_0`，则

\[
 \|h-\widetilde h\|_{TV}
 \le2\|d_j-\widetilde d_j\|_{TV}.
\tag{17}
\]

最后，对 `r=s h*Q(d)` 及其替身，任取相应上界，可用

\[
\begin{aligned}
 \|r-\widetilde r\|_{TV}
 \le{}&|s-\widetilde s|\,\|h\|\,\|Q(d)\|\\
 &+|\widetilde s|\,\|h-\widetilde h\|\,\|Q(d)\|\\
 &+|\widetilde s|\,\|\widetilde h\|\,
 \|Q(d)-\widetilde Q(\widetilde d)\|.
\end{aligned}
\tag{18}
\]

#### 证明

Telescoping给

\[
 d^{*k}-\widetilde d^{*k}
 =\sum_{j=0}^{k-1}d^{*j}*(d-\widetilde d)*
 \widetilde d^{*(k-1-j)},
\]

故其 TV norm至多 `k S^(k-1) delta`。把 polynomial coefficient变化另作三角
估计即得式 (16)。质量泛函的 norm为一，所以
`|m_j-m_j_tilde|<=||d_j-d_j_tilde||_TV`，给式 (17)。式 (18)是三项 telescoping
与 convolution submultiplicativity。`square`

## 7. 固定替身分母的 exact audit [T] 与 intended-model anchor [E]

`scripts/inspect_b1e_response_support.py` 使用以下协议：

1. 先按式 (4)聚合 formal response atoms；
2. 每个现有 binary64 response coefficient以 `Fraction.from_float` 视为一个 exact
   rational surrogate coefficient；
3. 在零点加入 surrogate total mass的相反数，故 centering exact；
4. 用 96 项式 (7) enclosure全部 positions；
5. 用式 (11)计算 exact rational energy upper。

输出为：

| channel | formal atoms | canonical atoms | certified min gap | rational energy upper |
|---|---:|---:|---:|---:|
| prime | 35103 | 22855 | `0.00004834486675790251` | `0.00055130411625587258` |
| continuum | 33977 | 21425 | `0.00004834486675790251` | `0.00015289136767059444` |

所有 position intervals严格分离，所以 cluster count等于 atom count且最大 cluster
size为一。替身 diagonal upper之和约为

\[
 \widetilde D_U\le0.00070419548392646702.
\tag{19}
\]

表中位置分离与 rational energy upper对 surrogate model是 exact finite statements
[T]。但 `Fraction.from_float` 不会自动 enclosure intended prime weights、continuum
cell masses、`sqrt(3)` 或 response normalization。因此式 (19)对 intended finite
zeta model仍只能作 [E] anchor；必须先由式 (16)--(18)给出 `epsilon_p,epsilon_c`，
再由式 (14)得到真正的 `D_upper`。

## 8. 下一最小引理 B1f [O]

对式 (1) 的 base data生成 directed rational intervals，并只输出以下小型 ledger：

\[
 \delta_p,\quad\delta_c,\quad\delta_d,
 \quad |s-\widetilde s|,
 \quad (E_0,\ldots,E_4).
\tag{20}
\]

然后用式 (16)--(18)计算 response TV radii `epsilon_p,epsilon_c`，以式 (14)认证
两个 channel denominator upper。与此同时，用笔记 246-B对同一 intervals重新计算
good-cell numerator lower。最终仍要求式 (2)，不降低阈值。

建议实现顺序：

1. prime weights：用本笔记的 log series及 exponential Taylor remainder；
2. continuum cell masses：对每个 rational cell作 interval quadrature并显式余项；
3. scalar `B,M,ell,s` 与 quartic coefficients：纯 interval polynomial ledger；
4. denominator：式 (16)--(19)；
5. numerator：directed `sin/cos` cell enclosures；
6. 单列 finite continuum quadrature与原 Archimedean current之间的 remainder。

晋级条件：脚本输出 rational endpoints、式 (20)、`D_upper`、verified cell list、
`N_lower` 及 `N_lower/D_upper>0.10`。止损条件：若 TV transfer消耗全部 margin，先提高
base coefficient精度；不得回退到 expanded-response逐项浮点 padding并称为 interval
certificate。

## 9. 公理删除、非循环性与适用范围

本轮最小输入是 finite zero-mass atomic measures、algebraic grid、Hermite--Lindemann
[R]、elementary rational series bounds和 total-variation convolution algebra。

删除审计：

- 删除 exact lag quotient，伪 `1e-16` gaps会使排序证书不稳定；
- 删除 logarithm remainder，high-precision decimal排序仍不是证明；
- 删除 cluster项，只在 intervals两两分离时公式才安全；
- 删除 zero total mass，Brownian energy可在无穷远发散；
- 删除 TV radius，surrogate denominator不能转移到 intended coefficients；
- 删除 numerator directed enclosure，分母完成也不能证明 ratio capture。

非同义反复审计：247-A--E只证明有限支持几何和误差传递，不假设 desired overlap、
Weil positivity或 RH。它们没有把式 (2)写进公理。

循环性审计：未使用 zeros、RH/GRH、Mertens平方根界、PNT误差或 bounded negative
index。唯一外部深结果 Hermite--Lindemann只用于一般 algebraic-grid equality；对当前
有限 support，也可完全用式 (7)的 disjoint position intervals替代它。

适用范围：

- Riemann/Dedekind finite positive-coefficient models可直接使用 real TV ledger；
- Dirichlet/automorphic models需把 coefficients作为 complex rectangles并以 modulus
  upper替代本脚本的 real `Fraction`；
- 函数域 degree lattice无需 logarithm enclosure，位置排序更简单；
- 本结果属于显式公式型 Weil 配置的 finite response层，不建立上同调分次、极化或
  Hard Lefschetz桥梁。

本轮严格缩小了 B1e：Brownian denominator不再需要 4 万个 transcendental response
intervals；剩余输入是 base prime/continuum coefficients的统一 rational enclosure与
good-cell trigonometric numerator。scale-uniform B1a 仍是其后的独立算术问题。

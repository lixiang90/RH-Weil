# 可变阶 Sobolev--Hodge filtration 与任意慢增长低频 core

文档 054 用 order `2` 的 massive biharmonic Green norm 把 RH 难点限制到
`|tau|<=X^(1/4)`。这里把 order 提升到任意整数 `r`，再允许
`r=r(X)=o(logX)` 缓慢增长。所得 polarization 仍以 `X^(o(1))` 精度保持
每个固定 divisor mode，却把 large-sieve 后剩余的频率窗口降到
`X^(1/(2r))`。

取 `r~logX/loglogX` 时只剩 `sqrt(logX)` 宽的 core；更一般地可把 core
压到任意趋于无穷但 subpower 的预定宽度。代价只是使用 `r` 个对数 prefix
moments，仍为 `X^(o(1))` 维的 Hodge fiber。

## 1. 任意阶 massive Green kernel

对整数 `r>=1` 定义

`mathcal H_r(x)=(1/(2pi))int_R |D_x(tau)|^2`

`                              /(tau^2+1/4)^r dtau`. (1)

### 定理 IY（order-r Green kernel）

有

`mathcal H_r(x)=sum_(m,n)x_m conjugate(x_n)G_r(m,n)`, (2)

其中

`G_r(m,n)=P_(r-1)(|log(m/n)|)/max(m,n)`,            (3)

`P_(r-1)(u)=1/(r-1)! sum_(k=0)^(r-1)`

`             [(r-1+k)!/(k!(r-1-k)!)]u^(r-1-k)`.  (4)

特别地

`P_0(u)=1`, `P_1(u)=u+2`.                          (5)

每个 `G_r` 都是正半定 kernel，并对应

`(-partial_t^2+1/4)^(-r)`.                         (6)

#### 证明

一般 Fourier--Bessel 公式为

`(1/(2pi))int_R e^(itau u)/(tau^2+a^2)^r dtau`

`=[1/(sqrt(pi)Gamma(r))](|u|/(2a))^(r-1/2)`

`                                      K_(r-1/2)(a|u|)`. (7)

取 `a=1/2`，再用 half-integer `K` 的有限展开，得到

`e^(-|u|/2)P_(r-1)(|u|)`.                         (8)

像定理 IT 一样与 `(mn)^(-1/2)` 共轭，指数因子变成
`1/max(m,n)`，得到式 (3)–(4)。正性来自式 (1)。`□`

## 2. `r` 个 prefix moments 的精确公式

令

`S_j(n)=sum_(m<n)x_m(logm)^j`, `0<=j<=r-1`.       (9)

把

`P_(r-1)(u)=sum_(k=0)^(r-1)p_(r,k)u^k`.           (10)

### 定理 IZ（finite logarithmic-moment formula）

有

`mathcal H_r(x)=P_(r-1)(0)sum_n |x_n|^2/n`

` +2Re sum_n conjugate(x_n)/n`

`   *sum_(k=0)^(r-1)p_(r,k)sum_(j=0)^k`

`             binom(k,j)(logn)^(k-j)(-1)^jS_j(n)`. (11)

所以 order `r` 的完整 double Gram 可由 `r` 个 prefix arrays 一次扫描；
不存在隐藏的 pair enumeration。

#### 证明

对 `m<n`，式 (3) 为 `P_(r-1)(logn-logm)/n`。对每个 monomial 用
binomial theorem 展开并先对 `m` 求和，得到式 (11)；再加 diagonal 与
Hermitian transpose。`□`

diagonal 常数为

`P_(r-1)(0)=binom(2r-2,r-1)`.                     (12)

它约为 `4^(r-1)/sqrt(pi(r-1))`；当 `r=o(logX)` 时仍只是 `X^(o(1))`。

## 3. 固定阶仍精确检测最右零点

对 centered finite vector

`a_X(n)=[Lambda(n)-1]1_(X/4<n<=4X)`              (13)

记 `mathcal H_r(X)=mathcal H_r(a_X)`。

### 定理 JA（fixed-order Sobolev criterion）[U]

对每个固定 `r>=1`，

`RH iff mathcal H_r(X)=X^(o(1))`.                  (14)

并且在标准有限阶显式公式条件下，

`limsup log(max(1,mathcal H_r(X)))/logX`

`=max(0,2Theta-1)`.                                (15)

#### 证明

下界不再由“fixed frequency 可见”直接推出。文档 163 推论 ACN 在
order `r` fixed 时给出 compact-frequency functional，其 dual norm 为常数，
且其算术取值的 Mellin transform 在每个 `rho` 保留真正 pole；所以
`mathcal H_r(X_j)>=X_j^(2Re rho-1-o(1))`。若
`A(t)=psi(t)-t=O_epsilon(t^(Theta+epsilon))`，对式 (3) 作两次 Abel
summation；log-polynomial degree 固定，只引入 `logX` 的固定幂，给相反
方向的 power upper bound。对 `Re rho->Theta` 取上确界，式 (15) 成立，
式 (14) 是 `Theta=1/2` 情形。`□`

## 4. 可变阶仍不丢失 divisor modes

现在令整数 `r_X>=2` 满足

`r_X=o(logX)`.                                     (16)

### 定理 JB（adaptive Sobolev detector）[U]

有

`RH iff mathcal H_(r_X)(X)=X^(o(1))`.              (17)

更精确地，可变阶 energy 的 power `limsup` 仍为

`max(0,2Theta-1)`。                                (18)

#### 证明

RH 下，对所有 `tau`，

`(tau^2+1/4)^(-r_X)`

`<=(4^(r_X-2))(tau^2+1/4)^(-2)`.                  (19)

文档 054 给 `mathcal H_2(X)=O(log^4X)`；式 (16) 使
`4^(r_X)=X^(o(1))`，故右侧为 subpower。

对一般 `Theta`，同一个式 (19) 结合定理 IV 给式 (18) 的 power 上界。

反之若有一个固定零点 `rho=beta+igamma`、`beta>1/2`，文档 163 对
`z_rho=rho-1/2` 构造支撑在 fixed frequency compact 上的 `ell_(X,rho)`。
其 dual norm 满足

`||ell_(X,rho)||<=exp[O_rho(r_X)]=X^(o(1))`,       (20)

而真正 Mellin pole 强迫其在实际向量上的取值沿子列至少为
`X^(beta-1/2-o(1))`。dual Cauchy--Schwarz 因而给
`mathcal H_(r_X)(X_j)>=X_j^(2beta-1-o(1))`，与式 (17) 矛盾。对每个 fixed
off-center zero 应用后取 `beta` 的 supremum，得到式 (18)。`□`

这一步使用的是显式 quantitative dual separation。条件 `r_X=o(logX)`
恰好把 compact-frequency dual norm 的 `exp(O(r_X))` 控制为 subpower；
它不声称对全部频率有 uniform frame lower bound。

## 5. 任意慢增长低频 core

### 定理 JC（order-r high-frequency tail）

对 `T>=1`，

`int_(|tau|>=T)|D_(a_X)(tau)|^2`

`                       /(tau^2+1/4)^r dtau`

`<<logX[T^(1-2r)+XT^(-2r)]`.                      (21)

取

`T=X^(1/(2r))`                                     (22)

即得 `O(logX)` 的无条件 tail。

#### 证明

沿用定理 IW 的 dyadic mean-value bound

`int_Y^(2Y)|D|^2<< (Y+X)logX`.                    (23)

第 `Y` 块的 order-r weight 为 `O(Y^(-2r))`；对 dyadic `Y>=T`
求和得到式 (21)。式 (22) 使第二项为 `1`，第一项为 `T/X<=1`。`□`

### 推论 JD（arbitrarily slowly expanding spectral core）

令 `Omega(X)->infinity` 且 `Omega(X)=o(logX)`，取

`r_X=floor(logX/Omega(X))`.                        (24)

则

`T_X=X^(1/(2r_X))=exp[(1+o(1))Omega(X)/2]`,        (25)

并且 RH 等价于

`int_(|tau|<=T_X)|D_(a_X)(tau)|^2`

`                     /(tau^2+1/4)^(r_X)dtau=X^(o(1))`. (26)

例如取 `Omega(X)=loglogX`，则

`r_X~logX/loglogX`, `T_X=(logX)^(1/2+o(1))`.       (27)

更一般地，给定任意 `T_X->infinity`、`T_X=X^(o(1))`，可取
`r_X~logX/(2logT_X)`，把剩余 core 压到该预定宽度。

#### 证明

式 (24) 满足定理 JB；式 (25) 是直接计算。定理 JC 清除补集，定理 JB
处理完整 energy。最后一种参数化由反解式 (22) 得到。`□`

所以高频 complexity 可以降到任意慢增长；不能降到固定窗口，因为那需要
`r_X asymp logX`，会把高处 fixed zero mode 乘成一个真正的 `X^(-delta)`，
从而改变要检测的 power exponent。

## 6. 广义 filtered Weil 结构

### 定理 JE（Mellin-coherent adaptive-polarization theorem）[U]

设 Gamma--Euler divisor data 有一族正 critical spectral Grams

`Q_X(v)=int |F_X(tau)|^2w_X(tau)dtau`,             (28)

并满足：

1. actual finite vectors 是某个 fixed centered Dirichlet series 的
   fixed-annulus truncations，因此文档 163 的 Mellin identity (17) 成立；
2. 每个目标 divisor point 是该 centered series 的真正 pole；
3. 对每个 fixed divisor point `rho`，文档 163 构造的 compact-frequency
   `q_rho` 满足
   `int |q_rho(tau)|^2/w_X(tau)dtau=X^(o(1))`；
4. 若只控制截断 core，则被删除的 tail 对 actual vector 为 subpower；
5. divisor 关于中心 `c/2` 对称。

若 `Q_X`（或与它相差 subpower 的 actual-vector core）为 subpower，则全部
divisor 位于中心线。

#### 证明

条件 1--2 与文档 163 的 Mellin abscissa 引理使 `ell_(X,rho)(v_X)` 沿子列
至少为 `X^(Re rho-c/2-o(1))`；条件 3 和 dual Cauchy--Schwarz 给
`Q_X(v_X)>=X^(2Re rho-c-o(1))`。条件 4 允许在 actual energy 层转移该结论。
所以 subpower tightness 排除全部右侧 divisor；条件 5 排除左侧。`□`

JE 的关键不是抽象的 pointwise visibility，而是同一个 Dirichlet series 在
所有尺度上的 Mellin coherence，加上可直接核验的 inverse-weight dual norm。
可变阶 Sobolev Hodge filtration 满足这些条件；任意 scale-varying Gram 不会
自动满足。

## 7. 证据边界与下一步

本笔记无条件清除了任意预定慢增长窗口之外的全部 twists，但没有控制窗口
内部。取式 (27) 后，真正剩余的目标为约 `sqrt(logX)` 宽的 weighted
Dirichlet core；每个固定 off-line zero 最终必落入其中，故不能再靠 smoothing
移除。

下一步可对这个 polylog core：

1. 使用 twisted Selberg symmetry 同时处理 `O(polylogX)` 的频率网格；
2. 证明 exponential-type sampling，把连续 core 化成 polylog 个坐标；
3. 对这些坐标作 residue/character dispersion；
4. 将有限坐标 Gram 接回定理 JE 的 filtered GNS completion。

任何成功的 subpower core bound 都会证明 RH；有限阶/可变阶 smoothing 本身
只负责无损压缩 obstruction，并不提供所缺的低频算术相消。

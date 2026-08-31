# Poisson 采样与 polylog-rank Euler--Hodge core

文档 055 把 RH obstruction 压到任意慢增长的连续频率窗口。这里利用一个
额外的刚性：centered Dirichlet polynomial 除去全局相位后具有固定
exponential type，因为 `X/4<n<=4X` 给

`|log(n/X)|<=log4`.                                (1)

对 adaptive Sobolev weight 作 Poisson summation，完整连续 Hodge Gram 与
步长 `asymp1/logX` 的离散 twisted Euler squares 只差 power-small alias。
截掉慢增长窗口外的离散尾后，得到一个 rank `X^(o(1))` 的显式正 Hodge
core；取规范参数时 rank 仅为 `O(log(X)^(3/2+o(1)))`。

## 1. Sobolev weight 的 Fourier 尾

记

`w_r(tau)=(tau^2+1/4)^(-r)`.                       (2)

### 命题 JF（exact transform and adaptive exponential decay）

有

`hat w_r(u)=int_R w_r(tau)e^(-itau u)dtau`

`=2pi e^(-|u|/2)P_(r-1)(|u|)`,                    (3)

其中 `P_(r-1)` 是定理 IY 的正系数多项式。并且

`P_(r-1)(u)<=(u+2r)^(r-1)/(r-1)!`.                (4)

若 `r=o(logX)` 且 `u=C logX`、`C>0` fixed，则

`P_(r-1)(u)=X^(o(1))`.                             (5)

#### 证明

式 (3) 就是定理 IY 在 Fourier transform normalization 下的式 (8)。
式 (4) 逐系数来自

`(2r-2-j)!/(r-1)! <=(2r)^(r-1-j)`.                (6)

令 `epsilon=r/logX->0`，Stirling 给

`log P(C logX)<=r[1+log(C/epsilon+2)]`

`=logX*epsilon[1+log(C/epsilon+2)]=o(logX)`,       (7)

因为 `epsilon log(1/epsilon)->0`。`□`

所以即使 polynomial degree 随 `X` 增长，exponential Green tail 仍压过
它；这正是 adaptive sampling 可行的原因。

## 2. Poisson alias bound

令

`D_X(tau)=sum_(X/4<n<=4X)`

`              [Lambda(n)-1]n^(-1/2-itau)`.       (8)

取 fixed `C>4` 并定义

`h_X=2pi/(C logX)`.                                (9)

### 定理 JG（continuous Gram versus infinite sampling lattice）

若 `r=o(logX)`，则

`Q_infty(X)=(h_X/(2pi))sum_(k in Z)`

`                 w_r(kh_X)|D_X(kh_X)|^2`          (10)

满足

`Q_infty(X)=mathcal H_r(X)+O(X^(1-C/2+o(1)))`.     (11)

#### 证明

令 `f(tau)=w_r(tau)|D_X(tau)|^2`。Poisson summation 给

`h_X sum_k f(kh_X)=sum_(ell in Z)`

`                         hat f(ell ClogX)`.       (12)

`ell=0` 项是 `int f=2pi mathcal H_r`。展开 `|D_X|^2` 后，其所有
frequency differences 都在 `[-log16,log16]`，所以由式 (3)

`|hat f(ell ClogX)|`

`<=2pi(sum_n |Lambda(n)-1|/sqrt(n))^2`

` *sup_(|v-ell ClogX|<=log16)`

`                      e^(-|v|/2)P_(r-1)(|v|)`.   (13)

trivial coefficient bound 为

`sum_n |Lambda(n)-1|/sqrt(n)<<sqrt(X)logX`.        (14)

命题 JF 使 `|ell|=1` 项至多
`X^(1-C/2+o(1))`；后续 aliases 构成几何尾。除以 `2pi` 得式 (11)。
`□`

这不是数值 quadrature 假设，而是带显式 alias 的精确 Poisson identity。

## 3. 截断为有限 rank-one squares

取 `T>=1`，`K=ceil(T/h_X)`，定义

`Q_core(X;r,T)=(h_X/(2pi))sum_(|k|<=K)`

`                  |D_X(kh_X)|^2/[(kh_X)^2+1/4]^r`. (15)

### 定理 JH（finite sampled Hodge core）

若 `r=o(logX)` 且

`T=X^(1/(2r))=X^(o(1))`,                           (16)

则

`Q_infty(X)-Q_core(X;r,T)=X^(o(1))`.               (17)

因此

`RH iff Q_core(X;r,T)=X^(o(1))`.                   (18)

core rank 满足

`2K+1=O(TlogX)=X^(o(1))`.                          (19)

#### 证明

点态 trivial bound `|D_X(tau)|<<sqrt(X)logX` 与 monotonicity 给

`h_X sum_(|kh_X|>T)w_r(kh_X)|D_X(kh_X)|^2`

`<<Xlog(X)^2 T^(1-2r)`.                            (20)

由式 (16)，`T^(-2r)=X^(-1)`，故右侧为
`Tlog(X)^2=X^(o(1))`，得到式 (17)。式 (11)、定理 JB 与 positivity 给
式 (18)；式 (19) 由式 (9)。`□`

连续 spectral positivity 现在成为有限个显式 rank-one squares 的 positivity；
所有未采样/高频方向已由式 (11)、(17) 统一控制。

## 4. Polylog-rank RH criterion

取

`r_X=floor(logX/loglogX)`,

`T_X=(logX)^(1/2+o(1))`.                           (21)

定义坐标

`zeta_(X,k)=sqrt(h_X/(2pi))`

` *D_X(kh_X)/[(kh_X)^2+1/4]^(r_X/2)`.             (22)

### 推论 JI（polylog many Euler coordinates detect RH）

有

`Q_core(X)=sum_(|k|<=K_X)|zeta_(X,k)|^2`,          (23)

`K_X=O(log(X)^(3/2+o(1)))`,                        (24)

并且以下条件等价：

1. RH；
2. `sum_(|k|<=K_X)|zeta_(X,k)|^2=X^(o(1))`；
3. `max_(|k|<=K_X)|zeta_(X,k)|^2=X^(o(1))`。

#### 证明

式 (23) 是定义，式 (24) 来自定理 JH。有限项均非负，且项数为
`X^(o(1))`，所以 sum 与 maximum 的 subpower 性质等价；再用式 (18)。`□`

这给出一个真正有限秩的 arithmetic Hodge core：每个 coordinate 只是一段
长度 factor `16` 的显式 twisted von Mangoldt-minus-continuum sum。

## 5. 广义 polylog-core Weil 结构

### 定理 JJ（sampled filtered Weil structure theorem）[U]

设定理 JE 的 Gamma--Euler filtered Gram 还满足：

- normalized Euler frequencies 落在 fixed compact interval；
- spectral weight 的 Fourier transform 在 dual variable 指数衰减，允许
  degree `o(logX)` 的 polynomial factor；
- coefficient `ell^1` norm 至多为 `X^(1/2+o(1))`。

则可取 mesh `asymp1/logX`，把 continuous compact-frequency core 替换为
`X^(o(1))` 个正 rank-one sampled Euler coordinates，alias 与 sampling tail
均为 subpower。若这些 coordinates 的最大 weighted square 为 subpower，
则全部 divisor 位于中心线。

#### 证明

命题 JF–定理 JH 的 Poisson argument 只使用列出的三项，并给 sampled actual
energy 与 coherent Sobolev energy 的 subpower additive comparison。修订后的
定理 JE 与文档 058 定理 JQ 的 actual-energy transfer 将 finite sampled core
bound 转成中心线结论。这里不声称 additive alias estimate 自动构造 sampled
Gram 全空间上的 FPW4b。`□`

JJ 把广义 Weil 结构进一步有限化：Hodge--Riemann positivity 的开放部分不再
是一个无限维 operator inequality，而是每个 scale 上 `X^(o(1))` 个显式
Euler periods 的联合 bound。

## 6. 数值审计与证据边界

实现对 generic complex finite vector、order `r=4` 使用 mesh `0.05` 和
`4801` 个 samples，得到

`|Q_sample-mathcal H_4|=4.63*10^(-17)`.            (25)

这验证了 Fourier normalization、权重及正负频率计数。它不是渐近 alias
证书，也不是 RH 数值证据。

本笔记无条件完成的是 continuous-to-finite-rank reduction。尚未证明的是
推论 JI 条件 3：对约 `log(X)^(3/2)` 个低频 twists 联合证明 weighted
centered Euler sums 为 subpower。下一步应在这一有限坐标族上尝试 twisted
Selberg symmetry、character dispersion 或有限 prolate/Ritz rotation。

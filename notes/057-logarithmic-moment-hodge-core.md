# 高阶 Taylor 压缩与 `logX/loglogX` 秩的算术 Hodge core

文档 056 已把 adaptive Sobolev Gram 化成约 `log(X)^(3/2)` 个 sampled
twists。这里利用 centered Dirichlet polynomial 的 fixed exponential type，
在慢增长窗口上作高阶 Taylor 压缩。由于全部 normalized frequencies
`log(n/X)` 落在 fixed interval `[-log4,log4]`，只需

`R=O(logX/loglogX)`

个 untwisted logarithmic moments，便能以 power-small 误差恢复整个低频
core。最终 RH 等价于一个显式 `R x R` 正 Hodge 矩阵在 arithmetic moment
vector 上的 subpower bound。

## 1. Centered exponential polynomial

沿用

`a_X(n)=[Lambda(n)-1]1_(X/4<n<=4X)`.              (1)

去掉不影响模方的 global phase，令

`F_X(tau)=X^(itau)D_X(tau)`

`=sum_n a_X(n)n^(-1/2)e^(-itau log(n/X))`.        (2)

定义 centered logarithmic moments

`M_j(X)=sum_n a_X(n)n^(-1/2)[log(n/X)]^j`.        (3)

则 formal Taylor polynomial 为

`F_(X,R)(tau)=sum_(j=0)^(R-1)`

`                    [(-itau)^j/j!]M_j(X)`.       (4)

### 命题 JK（uniform Taylor remainder）

令 `B=log4`。对 `|tau|<=T`，

`|F_X(tau)-F_(X,R)(tau)|`

`<=C sqrt(X)logX e^(BT)(BT)^R/R!`.                (5)

取 `L=logX`、`T=L^(1/2+o(1))` 与

`R=floor(kappa L/logL)`,                           (6)

则对每个 fixed `kappa>1`，右侧为

`X^(-(kappa-1)/2+o(1))`.                          (7)

#### 证明

trivial coefficient mass 为

`sum_n |a_X(n)|/sqrt(n)<<sqrt(X)logX`.             (8)

对每个 exponential 使用余项

`|e^z-sum_(j<R)z^j/j!|<=e^|z||z|^R/R!`,          (9)

且 `|z|<=BT`，得到式 (5)。由 Stirling，

`log[(BT)^R/R!]<=-Rlog[R/(eBT)]`。

在式 (6) 下，

`log[R/(eBT)]=(1/2+o(1))logL`，                   (10)

故 factorial tail 贡献 `-(kappa/2+o(1))L`；与式 (8) 的
`L/2+o(L)` 相加即得式 (7)。`□`

## 2. 显式有限 Hodge 矩阵

取 adaptive Sobolev order `r=r_X`、cutoff `T=T_X`。定义 `R x R` 矩阵

`H_(j,k)^(r,T)=(-i)^j i^k/[2pi j!k!]`

` *int_(-T)^T tau^(j+k)/(tau^2+1/4)^r dtau`,      (11)

`0<=j,k<R`。

### 定理 JL（positive logarithmic-moment core）

矩阵 `H^(r,T)` Hermitian positive semidefinite，且

`Q_mom(X)=M(X)^*H^(r,T)M(X)`                      (12)

精确等于 Taylor polynomial `F_(X,R)` 的 weighted low-frequency norm。

若 `r=o(logX)`, `T=X^(1/(2r))=X^(o(1))`，并在式 (6) 取任意
`kappa>2`，则

`Q_mom(X)=mathcal H_r(X)+X^(o(1))`,                (13)

其中等号按“差为 subpower”理解；更准确地，Taylor error 是一个 fixed
negative power，而高频 tail 为 subpower。

#### 证明

式 (11) 是 rank-one feature vector

`v_j(tau)=(-itau)^j/[j!(tau^2+1/4)^(r/2)]`

在 `L^2([-T,T],d tau/(2pi))` 中的 Gram，故正半定。展开式 (4) 的平方
积分给式 (12)。

命题 JK 在 `kappa>2` 时给 uniform error `X^(-1/2-eta)`。同时
`sup|F_X|<<sqrt(X)logX`，而

`int_(-T)^T(tau^2+1/4)^(-r)dtau<=2T4^r=X^(o(1))` (14)

因为 `r=o(logX)`。所以精确 core 与 Taylor core 的 energy 差为
`X^(-eta+o(1))`。定理 JC 清除 `|tau|>T`，得到式 (13)。`□`

式 (11) 的 entries 是 elementary incomplete beta integrals，可直接区间
计算；其正性不依赖数值 eigensolve。

## 3. `O(logX/loglogX)` 秩的 RH 等价判据

采用规范选择

`r_X=floor(logX/loglogX)`,

`T_X=(logX)^(1/2+o(1))`,

`R_X=floor(kappa logX/loglogX)`, `kappa>2`.         (15)

### 定理 JM（logarithmic-moment finite RH criterion）

以下条件等价：

1. RH；
2. `M(X)^*H^(r_X,T_X)M(X)=X^(o(1))`；
3. 在任意 factorization `H=C^*C` 下，
   `max_(j<R_X)|(CM(X))_j|^2=X^(o(1))`。

这里

`R_X=O(logX/loglogX)=X^(o(1))`.                   (16)

#### 证明

定理 JL 把条件 2 与定理 JB 的完整 adaptive energy 等价，后者与 RH 等价。
又因 `H>=0`，式 (12) 是 `||CM||^2`；坐标数为 subpower，所以其平方和为
subpower 当且仅当最大坐标平方为 subpower。`□`

与推论 JI 不同，这里不需要任何 nonzero twists 作为原始算术数据。全部
coordinates 都是前 `R_X` 个 centered logarithmic prime moments 的显式
线性组合。

## 4. 与 Weil primitive cohomology 的对应

moment vector

`M(X)=(M_0,...,M_(R_X-1))`                        (17)

可视为每个 scale 的有限 primitive cycle coordinates：

- `Lambda-1` 完成 Tate centering；
- powers of `log(n/X)` 是 infinitesimal dilation descendants；
- `H^(r,T)` 是正 Hodge--Riemann polarization；
- order/cutoff filtration 随 `X` 增长但 rank 仅为 subpower；
- 文档 163 的 Mellin dual 为 Sobolev carrier 定量分离每个 fixed divisor；定理 JB 再把该下界保留在 filtration 中。

### 定理 JN（finite logarithmic-moment Weil structure）[U]

设中心为 `c/2` 的 Gamma--Euler data 满足定理 JE，并且每个 scale 的
normalized Euler frequencies 落在 fixed compact interval，coefficient
`ell^1` mass 为 `X^(mu+o(1))`。若取 Taylor rank

`R_X> [4mu+epsilon]logX/loglogX`                   (18)

并使 adaptive Sobolev order 为 `o(logX)`，则 continuous filtered Hodge
core 与由前 `R_X` 个 logarithmic Euler moments 构成的 finite positive
matrix form 只差 subpower。若该 finite form 为 subpower，则全部 divisor
位于中心线。

#### 证明

命题 JK 的 `sqrt(X)` 替换为 `X^mu`；控制 energy cross term 要求 Taylor
余项小于 `X^(-mu-eta)`，即
`R(log[R/(eBT)])>2mu logX`，式 (18) 留出严格余量。定理 JL 完成
continuous-to-moment reduction；文档 163 先在 coherent Sobolev energy 上给
quantitative separation，修订后的定理 JE 与 actual-energy transfer 再给
中心线。`□`

JN 是本研究所求“广义结构定理”的一种有限 filtered 版本：其对象不必来自
代数簇，只需有 Euler trace coordinates、dilation descendants、正有限
polarization、tempered filtration、Mellin-coherent divisor trace 与 compact-frequency dual control。

## 5. 数值审计与证据边界

对 generic complex coefficient vector、`T=1,r=4,R=36`：

- 三个测试频率上的 Taylor maximum error 为 `1.20*10^(-36)`；
- 完整 low-frequency integral 与 moment Hodge form 相差
  `2.02*10^(-39)`。

这些计算验证了 center phase、factorials、共轭和积分 normalization；不是
RH 证据。

本笔记把开放条件降为 `O(logX/loglogX)` 个 untwisted arithmetic moments
的一个联合正矩阵 bound。仍未证明该 bound。下一步可以直接研究矩阵
`H^(r,T)` 的有效谱秩和 condition number，再判断是否只有更少的低阶
moment combinations 真正携带非 subpower obstruction；另一条路线是对
`M_j(X)` 应用 Selberg symmetry 的 log-derivative hierarchy。

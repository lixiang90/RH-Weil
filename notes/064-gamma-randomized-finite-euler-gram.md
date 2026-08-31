# Gamma 随机尺度与 finite Euler--Gram 中心线判据

文档 063 把最右零点压缩为单个 Abel 点的高阶矩根增长。本笔记识别这些
归一化矩的概率意义：moment order `q` 等价于在 Gamma-distributed logarithmic
scale 上抽样 prime annular energy。该表示进一步给出 exponentially finite
Euler truncations，因而把判据实现成一列真正有限的正算术 Gram。

## 1. Gamma sampling identity

固定 `sigma_0>1/2`。令 `T_q` 服从 shape `q+1`、rate `2sigma_0` 的 Gamma
分布，其 density 为

`p_q(t)=(2sigma_0)^(q+1)t^q e^(-2sigma_0t)/q!`,

`t>=0`.                                             (1)

沿用文档 063 的 normalized moments

`N_q=(2sigma_0)^q mathfrak M_q/q!`.                (2)

### 定理 KY（Gamma-randomized annular Gram identity）

有精确恒等式

`N_q=int_(h_0)^(h_1)E[|b_h(T_q)|^2]dh`.            (3)

更一般地，matrix kernel 为

`N_q(h,k)=E[b_h(T_q)conjugate(b_k(T_q))]`.         (4)

其 prime-pair kernel 是交 interval `[L,U)` 的 Gamma probability

`Pi_q(L,U)=[gamma(q+1,2sigma_0U)`

`                  -gamma(q+1,2sigma_0L)]/q!`.     (5)

特别地，每个 `q` 的 full width/prime block 都 positive semidefinite。

#### 证明

把式 (1) 代入期望，式 (3) 正好是式 (2) 与文档 063 式 (1) 的乘积。
两个 Euler indicators 同时非零恰在 `[L,U)`，积分 density `p_q` 给式 (5)。
positivity 来自随机向量 `h->b_h(T_q)` 的 covariance。`□`

式 (5) 是文档 063 incomplete-gamma moment kernel 的 regularized version；
所有 entries 都是 `[0,1]` 中的显式 probability。

## 2. Moment order 对应的算术尺度

### 命题 KZ（Gamma scale localization）

`T_q` 满足

`E T_q=(q+1)/(2sigma_0)`,

`Var(T_q)=(q+1)/(2sigma_0)^2`.                    (6)

对 fixed `0<delta<1`，存在 `c_delta>0` 使

`P(|T_q-E T_q|>=delta E T_q)`

`                         <=2e^(-c_delta(q+1))`.   (7)

所以其中心 multiplicative scale 为

`X_q=exp((q+1)/(2sigma_0))`,                       (8)

而一个标准差对应乘法因子

`exp(sqrt(q+1)/(2sigma_0))=X_q^(O(q^(-1/2)))`.     (9)

#### 证明

式 (6) 是 Gamma moments。对 mgf

`E e^(lambda T_q)=[2sigma_0/(2sigma_0-lambda)]^(q+1)`

作 Chernoff optimization 给式 (7)；式 (8)–(9) 随即成立。`□`

因此 `q` 本质上是 `log X`，而 Gamma sampling 在 `X^(1+o(1))` 的
multiplicative neighborhood 中平滑尺度。它不是 fixed sliding log block，
也不是把不同极限次序混合。

## 3. Divisor modes 是 Gamma exponential tilts

### 命题 LA（exact spectral tilt factor）

若一个 normalized divisor mode 含因子 `e^((a+itau)t)`，则其 squared
diagonal contribution 在 Gamma sampling 下乘以

`E e^(2aT_q)=[sigma_0/(sigma_0-a)]^(q+1)`,         (10)

只要 `a<sigma_0`。两个 modes `(a,tau)`、`(a',tau')` 的 cross factor 为

`[2sigma_0/(2sigma_0-a-a'-i(tau-tau'))]^(q+1)`.  (11)

所以 off-center displacement `a=beta-1/2` 正好产生文档 063 定理 KS 的
exponential root `sigma_0/(sigma_0-a)`。

#### 证明

式 (10)–(11) 都是 Gamma mgf 在 real/complex 参数处的直接代入。continuous
width frame 保证最右 divisor mode 的 coefficient 不会对全部 widths 消失；
positive trace/Laplace theorem 排除 cross cancellation 改变根半径。`□`

这给单点 moment theorem 一个 Weil 类比：有限域中 Frobenius eigenvalue 的
weight 由幂次迭代读取；这里零点横向偏移由 Gamma-randomized dilation 的
exponential growth 读取。

## 4. 无条件 finite Euler cutoff

对 zeta，在 compact width interval 上有 trivial uniform bound

`|b_h(t)|<=C(1+t)e^(t/2)`.                        (12)

固定常数 `C_0>0`，定义 cutoff

`tau_q=C_0(q+1)`，                                (13)

以及 truncated positive Gram

`N_q^[C_0]=int_(h_0)^(h_1)`

` E[1_(T_q<=tau_q)|b_h(T_q)|^2]dh`.               (14)

### 定理 LB（exponentially finite Euler approximation）

令

`kappa(C_0)=(2sigma_0-1)C_0-1-log(2sigma_0C_0)`. (15)

若 `C_0>1/(2sigma_0-1)` 且 `kappa(C_0)>0`，则

`0<=N_q-N_q^[C_0]<=exp(-kappa(C_0)q+o(q))`.       (16)

而 `N_q^[C_0]` 只使用

`n<=exp(C_0(q+1)+h_1)`                            (17)

的有限 Euler coefficients。它的 pair kernel 是

`Pi_q(L,min(U,tau_q))*1_(L<min(U,tau_q))`.        (18)

#### 证明

式 (12) 给 tail

`N_q-N_q^[C_0]`

` <<int_(C_0(q+1))^infinity(1+t)^2`

`   *(2sigma_0)^(q+1)t^q e^(-(2sigma_0-1)t)/q! dt`. (19)

在 `C_0>1/(2sigma_0-1)` 下 integrand 从 cutoff 起递减。Stirling 公式在
`t=C_0(q+1)` 给每阶指数

`1+log(2sigma_0C_0)-(2sigma_0-1)C_0`

即 `-kappa(C_0)`；余下积分与 polynomial factors 只贡献 `e^(o(q))`，
得到式 (16)。当 `t<=tau_q` 且 `h<=h_1`，annulus 中所有整数满足
`n<=e^(t+h_1)`，给式 (17)–(18)。`□`

条件 `kappa(C_0)>0` 对充分大的 `C_0` 总成立；所以这是无条件、显式且
exponentially accurate 的 finite approximation。

## 5. 有限随机尺度中心线结构

### 定理 LC（finite Gamma--Euler Gram RH theorem）

固定任意 `sigma_0>1/2`，并取满足定理 LB 的 `C_0`。则：

1. 每个 `q` 的 `N_q^[C_0]` 是由有限多个 `Lambda(n)-1` 构成的 positive
   Gram，support 满足式 (17)；
2. 其 root exponent 精确为

   `limsup_(q->infinity)(N_q^[C_0])^(1/q)`

   ` =sigma_0/[sigma_0-max(0,Theta-1/2)]`;         (20)

3. RH 等价于

   `N_q^[C_0]<=e^(o(q))`,                          (21)

   也等价于：对每个 `epsilon>0` 有
   `N_q^[C_0]<=C_epsilon(1+epsilon)^q`。

#### 证明

第 1 项由式 (14)、(17)–(18)。定理 LB 的误差 root 严格小于 `1`，而文档
063 定理 KS 给 `N_q` 的 root 至少为 `1`；因此截断不改变 root exponent，
得到第 2 项。第 3 项由 root test。`□`

这是一种真正 finite algebraic existence statement：所有 finite fibers、
pair kernels 与 positivity 都无条件构造；唯一未证的是 actual arithmetic
vectors 的 subexponential norm (21)，且它精确等价于 RH。

## 6. 生成函数与不可交换极限

### 命题 LD（Poissonized moment generating identity）

对 `|z|` 位于收敛圆盘内，

`sum_(q>=0)N_q z^q`

` =2sigma_0 int_0^infinity e^(-2sigma_0(1-z)t)dmu(t)`

` =mathfrak G_(sigma_0(1-z))/(1-z)`.              (22)

因此 moment-series radius 为

`1-max(0,Theta-1/2)/sigma_0`.                     (23)

#### 证明

对 Gamma densities 求和：

`sum_q p_q(t)z^q=2sigma_0e^(-2sigma_0(1-z)t)`，

再用 Tonelli 与 `mathfrak G_sigma=2sigma int e^(-2sigmat)dmu`。`□`

式 (22) 显示单点 moments 与完整 Abel filtration 是严格等价的
Poissonization，而不是额外假设。固定 Euler cutoff 后令 `q->infinity` 会丢失
谱；定理 LB 要求 cutoff 随 `q` cofinal 增长，仍然体现文档 062 的不可交换
极限次序。

## 7. Gamma--Euler finite-fiber theorem

### 定理 LE（general Gamma-randomized finite Euler structure）

考虑文档 063 定理 KV 的 paired Gamma--Euler current。假设其 absolute
annular growth 满足

`|b_h(t)|<=e^((omega+o(1))t)`                     (24)

uniformly on compact widths。令
`sigma_c=max(0,Theta-c/2)`，并取
`sigma_0>max(omega,sigma_c)`。若 `C_0` 满足

`2(sigma_0-omega)C_0-1-log(2sigma_0C_0)>0`,       (25)

则 cutoff `t<=C_0(q+1)` 给 exponentially accurate finite Euler Grams，且

`limsup(N_q^[C_0])^(1/q)`

` =sigma_0/[sigma_0-max(0,Theta-c/2)]`.           (26)

因此 centerline property 等价于 finite randomized Euler fibers 的
subexponential norm growth。

#### 证明

定理 KY/KZ 只使用 Gamma density；把定理 LB 中 `1/2` 换成 `omega`，tail
rate 变成 `2(sigma_0-omega)`。文档 063 定理 KV 给未截断 root，指数小的
positive tail 不改变它。`□`

## 8. 当前存在性边界

本笔记把 zeta 的 strong structure 存在性落实为一列完全有限对象：第 `q`
个 fiber 只需要 `n<=exp(O(q))` 的 Euler 数据，kernel 是 Gamma interval
probability，Gram positivity 无条件成立，且其 norm exponent 精确读取
`Theta`。尚缺的 (21) 不是极限定义问题，而是这些明确 finite prime vectors
的统一次指数范数估计。

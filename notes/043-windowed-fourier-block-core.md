# Windowed Fourier large sieve 与低频 Hodge core

文档 042 把 RH 化成 dyadic discrepancy blocks 的 `X^(2+epsilon)` 均方界。
本笔记对每个乘法块加端点消失的光滑窗并作 Fourier 分解。有限 Fourier
large sieve 无条件控制高频 signed prime modes；在
`M(X)=sqrt(X)log X` 之后，尾部已达到目标 `X^2` 尺度。于是全部开放困难
被压缩到每块 `O(sqrt(X)log X)` 个低频 Hodge coordinates。

## 1. Windowed block Fourier 恒等式

固定实函数 `w in C_c^1((1,2))`。对 `X>=2` 定义

`F_X(y)=psi(Xy)-Xy`,

`g_X(y)=w(y)F_X(y)`, `1<=y<=2`,                      (1)

并取长度一 Fourier 系数

`g_hat_X(m)=int_1^2 g_X(y)e^(-2pi i m y)dy`.         (2)

令

`S_X(m)=sum_(X<n<2X)Lambda(n)w(n/X)e^(-2pi i mn/X)`, (3)

`W_hat(m)=int_1^2w(y)e^(-2pi i m y)dy`,              (4)

`R_X(m)=int_1^2w'(y)F_X(y)e^(-2pi i m y)dy`.         (5)

### 命题 GE（exact windowed Fourier discrepancy identity）

对每个 `m!=0`，

`2pi i m g_hat_X(m)=S_X(m)-X W_hat(m)+R_X(m)`.       (6)

并且

`X int_1^2|g_X(y)|^2dy`

`=X sum_(m in Z)|g_hat_X(m)|^2`.                     (7)

#### 证明

分布意义下

`dF_X=sum_(X<n<2X)Lambda(n)delta_(n/X)-Xdy`.          (8)

因 `w` 在两个端点为零，`g_X` 的周期延拓没有边界 jump，故积分分部给

`2pi i m g_hat_X(m)=int_1^2e^(-2pi i my)d(wF_X)`，   (9)

展开 `d(wF)=w dF+w'Fdy` 即为式 (6)。式 (7) 是 Parseval，再乘回
`dx=Xdy`。`□`

式 (6) 保留了 prime exponential sum、连续背景和当前 block error 的完整
signed 组合，没有 endpoint 大项。

## 2. Prime exponential block large sieve

窗的支撑离 `1,2` 有固定正距离，所以式 (3) 的频率点 `n/X mod 1` 彼此
至少 `1/X` 分离。Chebyshev 界还给

`sum_(X<n<2X)Lambda(n)^2|w(n/X)|^2`

`<=C_w Xlog(2X)`.                                    (10)

### 定理 GF（windowed prime-frequency large sieve）

对任意整数频率区间 `I`、长度 `R>=1`，

`sum_(m in I)|S_X(m)|^2`

`<=C_w(R+X)Xlog(2X)`.                                (11)

#### 证明

对 `1/X`-分离点应用有限 Fourier large-sieve inequality

`sum_(m in I)|sum_n a_n e^(-2pi i m n/X)|^2`

`<=(R-1+X)sum_n|a_n|^2`,                             (12)

取 `a_n=Lambda(n)w(n/X)`，再用式 (10)。`□`

GF 是纯有限算术估计，不使用 PNT error 或零点。

## 3. 高频 tail 的无条件控制

令

`V(X)=int_X^(2X)|psi(x)-x|^2dx`.                     (13)

由 Parseval，

`sum_m|R_X(m)|^2=int_1^2|w'(y)F_X(y)|^2dy`

`<=||w'||_infinity^2 V(X)/X`.                        (14)

又因 `w` 端点消失，`|W_hat(m)|<=C_w/|m|`。

### 定理 GG（high Fourier modes are an unconditional small complement）

若 `1<=M<=X`，则

`X sum_(|m|>M)|g_hat_X(m)|^2`

`<=C_w{X^3log(2X)/M^2+Xlog(2X)`

`             +X^3/M^3+V(X)/M^2}`.                 (15)

特别取

`M(X)=ceil(sqrt(X)log(2X))`，                        (16)

得到

`X sum_(|m|>M(X))|g_hat_X(m)|^2`

`<=C_w[X^2+V(X)/(Xlog^2(2X))]`.                     (17)

#### 证明

将式 (6) 的三项用 `|a+b+c|^2<=3(|a|^2+|b|^2+|c|^2)` 分开。

对 prime 项，把 `|m|>M` 分成 dyadic frequency intervals。式 (11) 除以
该层的 `m^2` 后求和；`M<=R<=X` 的部分由第一层主导，给
`C X^2log(2X)/M^2`，`R>=X` 的层给 `C log(2X)`。连续项给
`C X^2sum_(m>M)m^(-4)<=CX^2/M^3`。式 (14) 给
`C V(X)/(XM^2)`。最后式 (6) 另有 `(2pi m)^(-2)`，并乘式 (7) 的
`X`，得到式 (15)。代入式 (16) 并吸收较小幂项得到式 (17)。`□`

因此高频 complement 已无条件处于 RH 所需尺度；困难只在低频 core。

## 4. 光滑乘法覆盖

取 `0<a<log2`，选择 `W in C_c^1((0,log2))`，使其 translates
`W(t-ka)` 覆盖实线且

`sum_(k in Z)|W(t-ka)|^2>=c_W>0`.                    (18)

令

`X_k=e^(ka)`, `w(y)=W(log y)`.                       (19)

每个 `x>0` 只落入有限个窗，且相应 `X_k` 与 `x` 可比。

定义低频 core energy

`L(X)=X sum_(|m|<=M(X))|g_hat_X(m)|^2`.              (20)

### 定理 GH（sqrt-X Fourier-core criterion for RH）

下列条件等价：

1. RH 成立；
2. 对每个 `epsilon>0`，沿覆盖尺度 `X_k` 有

   `L(X_k)=O_(epsilon,w)(X_k^(2+epsilon))`.           (21)

#### 证明：RH 推出低频界

RH 给 `V(X)=O(X^2log^4X)`。windowed energy 不超过常数倍 `V(X)`，低频
部分更小，故式 (21)。

#### 证明：低频界推出 RH

由覆盖式 (18) 与有限重叠，任意 dyadic block `V(Y)` 被有限个
`X_k asymp Y` 的 windowed energies 控制。对每个这些尺度应用
Parseval，把能量分为式 (20) 与定理 GG 的尾。式 (17) 中的
`V(X_k)/(X_klog^2X_k)` 再由相邻有限个窗口覆盖；对充分大尺度，其系数
小于覆盖常数的一半，可在有限邻接系统中吸收到左边。因此

`V(Y)<=C_epsilon Y^(2+epsilon)+CY^2`.                (22)

文档 042 定理 GB 给 RH。`□`

GH 把每个含约 `X/logX` 个 prime positions 的 block obstruction 压缩为
`O(sqrt X logX)` 个 signed Fourier coordinates，余空间已由无条件 large
sieve 控制。

## 5. 广义 complex Euler blocks

对文档 040 的 complex discrepancy `E_Z(x)`，用同一窗定义 `g_(Z,X)`。
若局部 Euler coefficients 满足

`sum_(X<n<2X)|b(n)|^2<=C Xlog^A X`,                  (23)

则 GF/GG 以 `logX` 替换为 `log^A X` 原封不动成立。

### 定理 GI（general windowed Fourier-core structure theorem）

设 `c>=1`，且中心为 `c/2` 的 Gamma--Euler 数据满足 divisor 对称、式 (23) 和文档
035 的 Mellin 条件。若覆盖尺度上的低频 cores（截断可取
`M(X)=sqrt(X)log^B X`、`B` 足够大）满足

`L_Z(X)=O_epsilon(X^(c+1+epsilon))`,                 (24)

则全部非平凡零点位于 `Re s=c/2`。

#### 证明

GF/GG 与覆盖吸收把式 (24) 升级为
`V_Z(X)=O_epsilon(X^(c+1+epsilon))`；应用文档 042 定理 GD。`□`

## 6. 数值与证书边界

脚本 `chebyshev_windowed_block_energy` 直接积分 windowed block，
`chebyshev_windowed_fourier_coefficient` 计算式 (2)。有限 Fourier 部分和
由 Parseval 单调位于总 windowed energy 以下，用于核对 `X`、`2pi` 与窗
归一化。

GH 仍不是 RH 证明：式 (21) 的低频 core bound 未知。但它无条件移除了
全部高频 modes，并把所需新输入降为亚线性维数的 signed exponential-sum
矩阵，而不是完整 prime block 或逐 Euler sample。

数值转录审计取默认窗 `w(y)=sin^2(pi(y-1))` 与 `X=13`。总 windowed
energy 为 `17.1947532334`；`|m|<=3`、`|m|<=5` 的 Fourier 部分和分别为
`14.6343487684`、`15.2445986020`，严格单调且低于总能量。这只检查
Parseval、`X` 缩放与 `2pi` 常数，不验证未知的全尺度低频界。

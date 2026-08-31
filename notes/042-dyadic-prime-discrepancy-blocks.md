# Dyadic prime-discrepancy Hodge blocks

文档 041 证明逐 Euler sample 的绝对估计必然失败。本笔记改为保留
prime--continuum signed measure，并按乘法尺度分块。每个块都是一个正的
finite tent-kernel Hodge norm；全部 Abel energy 是这些块的 Mellin 加权和。
RH 因而等价于一个清晰的 dyadic mean-square 界，可作为 large-sieve、
Selberg integral 或 block cancellation 方法的直接目标。

## 1. Dyadic Hodge 分解

令

`E(x)=psi(x)-x`,

`V(X)=int_X^(2X)|E(x)|^2dx`, `X>=1`.                 (1)

取 dyadic blocks `X_k=2^k`, `V_k=V(2^k)`。

### 命题 FZ（Abel energy is a weighted sum of dyadic blocks）

对每个 `sigma>0`，

`int_1^infinity |E(x)|^2x^(-2sigma-2)dx<infinity`   (2)

当且仅当

`sum_(k>=0)2^(-k(2sigma+2))V_k<infinity`.            (3)

更精确地，第 `k` 块的加权积分夹在

`2^(-(k+1)(2sigma+2))V_k`

和

`2^(-k(2sigma+2))V_k`                                (4)

之间。

#### 证明

在 `[2^k,2^(k+1)]` 上，权 `x^(-2sigma-2)` 夹在式 (4) 的两个常数之间。
逐块求和即得。`□`

这把文档 035 的单个无限积分改写成一列正有限 Hodge blocks，没有跨块
符号抵消。

## 2. Block growth exponent 与零点条带

定义 dyadic mean-square exponent

`kappa=limsup_(k->infinity) log(max(1,V_k))/(klog2)`. (5)

令 `Theta=sup_rho Re rho`。

### 定理 GA（block exponent detects off-center width）

有

`max(0,(kappa-2)/2)=max(0,Theta-1/2)`.               (6)

特别地：

- 若 `Theta>1/2`，则 `kappa=2Theta+1>2`；
- `kappa<=2` 当且仅当 RH 成立。

#### 证明

正项幂级数式 (3) 的收敛横坐标由 Cauchy--Hadamard/root test 给出

`max(0,(kappa-2)/2)`.                                (7)

文档 035 定理 EP 证明同一积分的收敛横坐标为
`max(0,Theta-1/2)`，得到式 (6)。若 `Theta>1/2`，两边严格为正，解出
`kappa=2Theta+1`。若 `kappa<=2`，左边为零，函数方程给 RH；RH 反向使
右边为零，故 `kappa<=2`。`□`

GA 不声称 RH 下 `kappa` 必须等于二；它只需不超过二。若有更强平均相消，
`kappa` 可以更小。

## 3. 一个纯均方 RH 判据

### 定理 GB（dyadic mean-square criterion for RH）

下列条件等价：

1. RH 成立；
2. 对每个 `epsilon>0`，

   `V(X)=O_epsilon(X^(2+epsilon))`;                   (8)

3. 对每个 `epsilon>0`，

   `V_k=O_epsilon(2^(k(2+epsilon)))`.                 (9)

#### 证明

RH 的经典后果 `E(x)=O(sqrt(x)log^2x)` 给

`V(X)=O(X^2log^4X)`，蕴含式 (8)。式 (8) 显然给式 (9)。反之，固定任意
`sigma>0`，在式 (9) 中选 `epsilon<2sigma`；代入式 (3) 得几何级数
`sum 2^(-k(2sigma-epsilon))`，故文档 035 的 `I_sigma` 有限。对所有
`sigma>0` 应用推论 EQ，得到 RH。`□`

GB 只要求乘法块上的平均平方根相消，不要求 pointwise PNT error 的 RH
界。它比逐点路线更适合正 Gram/large-sieve 方法。

补充：文档 070 利用 RH 下 coefficients `m_gamma/rho` 与 unit-window zero
count 证明 uniform local `L^2`，从而把本定理加强为 epsilon-free 等价
`V(X)=O(X^2)`。本节的 root-test 证明仍适用于不先假设 local divisor count
的较弱 `X^(2+epsilon)` formulation。

## 4. 每个块的 finite tent kernel

沿用 signed discrepancy current

`dnu=-delta_1+sum_n Lambda(n)delta_n-dx`,             (10)

使 `nu([1,x])=E(x)`。定义

`K_X(u,v)=(2X-max(X,u,v))_+`.                        (11)

### 命题 GC（dyadic block is a positive tent-kernel norm）

`K_X` 是正定核，且

`V(X)=int int K_X(u,v)dnu(u)dnu(v)`.                 (12)

对 zeta 展开为完全有限的恒等式

`V(X)=sum_(m,n<=2X)Lambda(m)Lambda(n)`

`                         (2X-max(X,m,n))_+`

` -sum_(n<=2X)Lambda(n)[4X^2-max(X,n)^2]`

` +(7/3)X^3`.                                        (13)

#### 证明

令 feature `Phi_u(x)=1_(X<=x<=2X)1_(u<=x)`。则

`<Phi_u,Phi_v>_(L2)=int_X^(2X)1_(u<=x)1_(v<=x)dx`

`=K_X(u,v)`，证明正性。对 current 积分 feature 得
`nu([1,x])=E(x)`，其平方 norm 是式 (12)。

直接展开 `(psi(x)-x)^2`：prime-square 项给第一行；交叉项使用

`2int_(max(X,n))^(2X)x dx=4X^2-max(X,n)^2`;          (14)

背景平方为 `int_X^(2X)x^2dx=7X^3/3`，得到式 (13)。`□`

式 (13) 的三个部分各为 `X^3` 量级；目标式 (8) 要证明它们联合降到
`X^(2+epsilon)`。这正是必须保留的 signed block cancellation。

## 5. Block Hodge sufficient theorem

### 定理 GD（abstract discrepancy-block center-line theorem）

对中心为 `c/2` 的 Gamma--Euler 数据，令
`E_Z=Psi_Z-M_Z`，并定义

`V_Z(X)=int_X^(2X)|E_Z(x)|^2dx`.                     (15)

若对每个 `epsilon>0`，

`V_Z(X)=O_epsilon(X^(c+1+epsilon))`,                 (16)

则全部非平凡零点位于 `Re s=c/2`。

更一般地，若

`V_Z(X)=O_epsilon(X^(2theta+1+epsilon))`,             (17)

则所有非平凡零点位于

`|Re rho-c/2|<=max(0,theta-c/2)`.                    (18)

#### 证明

在 dyadic blocks 上，文档 035 的一般 energy 权为
`x^(-c-2sigma-1)`。式 (16) 使其第 `k` 项至多为
`X_k^(-2sigma+epsilon)`；任取 `epsilon<2sigma` 后求和，得到所有
`sigma>0` 的有限 Hodge energy，应用定理 ES。

对式 (17)，加权块指数为
`2theta+1-(c+2sigma+1)+epsilon`
`=2(theta-c/2-sigma)+epsilon`。故 energy 对所有
`sigma>theta-c/2` 有限；文档 034/035 的条带定理给式 (18)。`□`

GD 是适用于复、twisted、automorphic currents 的广义 block 结构定理。

## 6. 存在性审计

对 zeta，无条件 Chebyshev/PNT 级别估计只给

`V(X)<=X sup_(X<=x<=2X)|E(x)|^2=X^(3-o(1))`         (19)

的 exponent 三（定量 PNT 可加入 subpower 衰减），对应文档 036 的临界
`sigma=1/2`。要得到任意固定改进，必须把 block exponent 从三严格降下；
要证明 RH，必须达到 `2+epsilon`。

与文档 041 相比，式 (13) 提供了可行的相消单位：

- 不对单个 Euler samples 取绝对值；
- prime atoms 与 continuum background 保留在同一有限 Gram block；
- 可以尝试 large sieve、dispersion、Selberg integral 或多尺度 Schur
  方法控制整块。

脚本提供 `chebyshev_block_variance` 的分段精确积分与
`chebyshev_block_variance_max_kernel` 的独立双素数展开；二者逐值一致。

数值转录审计给出

| `X` | `V(X)` | `V(X)/X^2` |
|---:|---:|---:|
| 13 | 51.87730133 | 0.3069663 |
| 101 | 870.0592896 | 0.0852916 |
| 1009 | 84570.35553 | 0.0830684 |

这些小尺度值只检查 tent-kernel 常数与三项相消；观察到 `X^2` 归一化稳定
不能替代定理 GB 所需的全尺度上界。

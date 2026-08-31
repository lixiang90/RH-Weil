# Triangular Riesz 单模态中心线判据

文档 043 把每个 discrepancy block 压缩到亚线性维数的低频 core。本笔记
发现其中的零 Fourier 模态已经能单独检测全部非平凡零点。原因是区间
`[X,2X]` 的 Mellin moment 在临界条带无零。于是一个完全显式的
triangular prime--continuum matrix coefficient 的平方根增长界，就足以
推出 RH；同一结论适用于一般 Gamma--Euler divisor。

## 1. Triangular coefficient

定义

`A(X)=int_X^(2X)[psi(x)-x]dx`.                       (1)

令

`B(Y)=int_0^Y psi(x)dx`

`=sum_(n<=Y)Lambda(n)(Y-n)`.                         (2)

则

`A(X)=B(2X)-B(X)-(3/2)X^2`.                          (3)

### 命题 GJ（finite triangular prime formula）

对整数 `X>=1`，

`A(X)=X psi(X)`

` +sum_(X<n<=2X)Lambda(n)(2X-n)-(3/2)X^2`.          (4)

等价地，若 `nu` 是文档 037 的 signed discrepancy current，

`A(X)=<nu,tau_X>`,                                   (5)

其中

`tau_X(u)=(2X-max(X,u))_+`.                          (6)

#### 证明

在式 (1) 的 `psi` 部分交换积分与有限和。`n<=X` 的贡献长度为 `X`；
`X<n<=2X` 的贡献为 `2X-n`，得到式 (4)。对 cumulative current
`E(x)=nu([1,x])` 再交换积分，source `u` 的 feature 正是式 (6)，得到式
(5)。`□`

`tau_X` 是文档 042 tent kernel 的单个 integrated feature；因此 `A(X)`
是一个真正的 Hodge matrix coefficient，而不是任意平滑。

## 2. 精确 Mellin transform

记 `D(s)=-zeta'/zeta(s)`。当 `Re s>1` 时，由式 (2) 交换和与积分，

`int_1^infinity B(X)X^(-s-2)dx=D(s)/[s(s+1)]`.      (7)

### 命题 GK（zero-free triangular Mellin multiplier）

有精确恒等式

`int_1^infinity A(X)X^(-s-2)dX`

`=[2^(s+1)-1]D(s)/[s(s+1)]-3/[2(s-1)]`.             (8)

在 `s=1`，右边的两个 pole 精确相消。若 `rho` 是非平凡零点，则右边在
`s=rho` 的留数为

`-[2^(rho+1)-1]/[rho(rho+1)]`.                      (9)

该留数在 `0<Re rho<1` 永不为零。

#### 证明

式 (7) 已证。对 `B(2X)` 令 `Y=2X`；因 `B(Y)=0` 在 `1<=Y<=2`，得到

`int_1^infinity B(2X)X^(-s-2)dX`

`=2^(s+1)D(s)/[s(s+1)]`.                            (10)

背景项的 transform 为 `3/[2(s-1)]`，证明式 (8)。`D` 在 zeta pole
`s=1` 的留数为 `+1`，而
`[2^2-1]/[1*2]=3/2`，故相消。`D` 在零点的留数为 `-1`，给式 (9)。若
`2^(rho+1)=1`，则 `Re(rho+1)=0`，即 `Re rho=-1`，不在非平凡条带。
`□`

与一般 compactly supported smoothing 不同，这个 Mellin multiplier 无需
separating 测试族：单个 `[1,2]` box moment 已看见全部非平凡零点。

## 3. 单模态 RH 等价判据

### 定理 GL（single triangular-mode criterion for RH）

下列条件等价：

1. RH 成立；
2. 对每个 `epsilon>0`，

   `A(X)=O_epsilon(X^(3/2+epsilon))`;                 (11)

3. `limsup_(X->infinity)log(max(1,|A(X)|))/logX<=3/2`. (12)

#### 证明：RH 推出增长界

RH 给 `psi(x)-x=O(sqrt(x)log^2x)`，在长度 `X` 的区间积分得
`A(X)=O(X^(3/2)log^2X)`。

#### 证明：增长界推出 RH

式 (11) 使式 (8) 左边对每个 `Re s>1/2` 解析。由命题 GK，任何
`Re rho>1/2` 的零点都会产生不能被 multiplier 消去的 pole，矛盾。函数
方程再排除左侧零点。条件 2 与 3 是标准 `epsilon`/limsup 等价。`□`

所以文档 043 的 `O(sqrt X logX)` 维低频 core 对“推出 RH”而言还可压缩
到一个标量；较大 core 的作用是证明完整 block mean square，而不是中心线
逻辑本身所必需。

文档 072 定理 MY 在 sharp local Selberg theorem 的基础上进一步去掉了这里
的 `epsilon`：RH 等价于 endpoint bound `A(X)=O(X^(3/2))`。该文档还证明
这个 triangular coefficient 的平方正是 local Green--Hodge form 的 canonical
rank-one constant-mode summand。

## 4. 与 block Hodge norm 的关系

由 Cauchy--Schwarz，

`|A(X)|^2<=X V(X)`.                                  (13)

因此文档 042 的 mean-square RH bound 自动给定理 GL。但反向不成立为纯
泛函分析事实：一个函数的平均可以小而方差大。GL 的反向成立依赖命题 GK
的零点无消失 Mellin multiplier，而不是式 (13)。

在文档 043 的未加窗 block Fourier 展开中，

`A(X)/X=int_1^2[psi(Xy)-Xy]dy`                       (14)

正是零 Fourier coefficient。这解释了它的“单模态”名称。

## 5. 广义 Gamma--Euler triangular theorem

对中心为 `c/2` 的数据，令 `E_Z=Psi_Z-M_Z`，并定义

`A_Z(X)=int_X^(2X)E_Z(x)dx`.                         (15)

### 定理 GM（general triangular Riesz center-line theorem）

假设文档 035 的有限阶、Euler/Mellin 与中心 divisor 对称条件。若对每个
`epsilon>0`，

`A_Z(X)=O_epsilon(X^(c/2+1+epsilon))`,               (16)

则全部非平凡零点位于 `Re s=c/2`。

更一般地，若 `A_Z(X)=O_epsilon(X^(theta+1+epsilon))`，则没有
`Re rho>theta` 的零点；结合 divisor 对称得到相应中心条带。

#### 证明

对每个 divisor 模态 `x^rho`，式 (15) 的 Mellin multiplier 仍为

`[2^(rho+1)-1]/(rho+1)`,                             (17)

它在标准非平凡条带中无零。式 (16) 使 triangular coefficient 的 Mellin
transform 在 `Re s>c/2` 解析，故排除右侧零点；中心对称排除左侧。一般
`theta` 同理。`□`

### 推论 GN（finite packets）

对有限 Dirichlet/automorphic packet，若每个 complex triangular
coefficient 满足式 (16)，则 packet 中全部完备 L-functions 满足 GRH。
也可把这些 coefficients 组成向量或 rank-one Gram matrix；正 Hilbert
结构由普通复内积给出。

## 6. 存在性审计

对 zeta，式 (4) 的每个有限对象都无条件、精确可算。经典 PNT 只给
`A(X)=X^(2-o(1))` 型界；定理 GL 需要完整的平方根节省
`X^(3/2+epsilon)`。因此单模态虽然极小，却没有降低 RH 的算术强度。

与前两条路线的关系是：

- triangular 单模态：最小逻辑 detector，目标是一个 signed Riesz sum；
- windowed Fourier core：亚线性维数，允许 large-sieve 分离高频；
- dyadic block norm：正均方 Hodge form，最适合 positivity/Gram 技术。

三者提供不同证明接口，但都由同一个 prime--continuum current 生成。

脚本以分段积分和式 (4) 两种独立方式计算 `A(X)`，并核对
`|A(X)|^2<=XV(X)`。

一次小规模数值审计如下；最后一列必须落在 `[0,1]`：

| `X` | finite formula `A(X)` | piecewise integral | `A(X)/X^(3/2)` | `A(X)^2/[XV(X)]` |
|---:|---:|---:|---:|---:|
| 13 | -23.1094501 | -23.1094501 | -0.493031 | 0.791878 |
| 101 | -131.024051 | -131.024051 | -0.129083 | 0.195358 |
| 1009 | -1499.91042 | -1499.91042 | -0.0467981 | 0.0263646 |

这只核对有限恒等式与能量支配，不构成增长率的证据，更不构成 RH 的
数值证明。

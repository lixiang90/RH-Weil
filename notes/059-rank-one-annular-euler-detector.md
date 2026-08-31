# Rank-one annular Euler detector 与标量 filtered Weil 结构

文档 057 将 RH 压成 `O(logX/loglogX)` 个 logarithmic moments。其第零个
moment 本身具有一个此前未利用的性质：annular Mellin multiplier 的全部零
都位于中心轴。因此它虽然可能看不见某些已经在中心线上的 modes，却不会
漏掉任何 off-center divisor。

结果是：经典 RH 等价于单个显式有限 Euler coordinate 的 subpower bound。
相应 Hodge fiber 只有一维，polarization 就是普通绝对值平方。

## 1. Centered annular coordinate

固定任意 `A>1`，定义

`B_A(X)=sum_(X/A<n<=AX)[Lambda(n)-1]/sqrt(n)`.     (1)

令

`mathcal A(s)=sum_(n>=1)[Lambda(n)-1]n^(-s)`

`             =-zeta'(s)/zeta(s)-zeta(s)`,        (2)

初始定义于 `Re s>1`。注意 `s=1` 处两个 residue 精确抵消，所以
`mathcal A` 在 `s=1` 正则；它在开临界条带右半部的 poles 恰来自 zeta
zeros，并保留重数。

### 定理 JV（exact annular Mellin identity）

当 `Re z>1/2` 时，

`int_0^infinity B_A(X)X^(-z-1)dX`

`=M_A(z)mathcal A(1/2+z)`,                         (3)

其中

`M_A(z)=[A^z-A^(-z)]/z`,                           (4)

并在 `z=0` 取 removable value `2logA`。

#### 证明

在绝对收敛半平面交换有限/可数和与积分。对每个 `n`，条件
`X/A<n<=AX` 等价于 `n/A<=X<An`，故

`int_(n/A)^(An)X^(-z-1)dX`

`=n^(-z)[A^z-A^(-z)]/z`.                          (5)

乘 `(Lambda(n)-1)n^(-1/2)` 后求和即得。`□`

## 2. Multiplier 只在中心轴消失

### 命题 JW（off-center nonvanishing）

`M_A(z)=2sinh(zlogA)/z`.                           (6)

其零点恰为

`z=pi i k/logA`, `k in Z\{0}`，                   (7)

全部位于 `Re z=0`；`z=0` 不是零点。因此

`M_A(z)!=0` 对所有 `Re z!=0`。                    (8)

#### 证明

`sinh w=0` 当且仅当 `w=pi i k`；除以 `z` 后原点为 removable nonzero
value。`□`

这正是 filtered center-line theorem 所需的最小 visibility：无需看见每个
critical-line mode，只需保证每个 off-center mode 可见。

## 3. 标量 RH 等价判据

### 定理 JX（rank-one annular criterion for RH）

对任意固定 `A>1`，以下条件等价：

1. RH；
2. 对每个 `epsilon>0`，`B_A(X)=O_epsilon(X^epsilon)`；
3. `B_A(X)=X^(o(1))`；
4. `B_A(X)=O(log(X)^2)`。

更精确地，若

`Theta=sup_rho Re rho`，                           (9)

则

`limsup_(X->infinity)`

` log(max(1,|B_A(X)|))/logX`

`=max(0,Theta-1/2)`.                               (10)

#### 证明

先假设条件 3。式 (1) 在 `X<1/A` 时为零，所以 Mellin integral 的 lower
endpoint 无问题。对任意 compact subset of `Re z>0`，取更小
`epsilon<Re z`；subpower bound 使式 (3) 左侧从 `X=1/A` 到无穷局部一致
收敛，故定义 `Re z>0` 的 holomorphic function。由 analytic continuation，

`M_A(z)mathcal A(1/2+z)`                           (11)

在右半平面 holomorphic。命题 JW 说明 `M_A` 无零，故 `mathcal A(s)` 在
`Re s>1/2` 无 poles。式 (2) 在每个 zeta zero 有不可消 pole，而 `s=1`
已抵消，所以 zeta 在右半临界条带无零。函数方程对称性给 RH。

反之假设 RH。令

`E(t)=sum_(n<=t)[Lambda(n)-1]=psi(t)-floor(t)`.    (12)

经典 RH bound 为 `E(t)=O(sqrt(t)log(t)^2)`。Stieltjes partial summation
给

`B_A(X)=[E(t)t^(-1/2)]_(X/A)^(AX)`

` +(1/2)int_(X/A)^(AX)E(t)t^(-3/2)dt`

`=O(log(X)^2)`,                                    (13)

即 `1=>4=>3=>2`。

式 (10) 的上界同样由
`E(t)=O_epsilon(t^(Theta+epsilon))` 得到。若存在 fixed zero
`rho=beta+igamma`，式 (3) 在 `z=rho-1/2` 有 pole，且命题 JW 保证 multiplier
非零；Mellin singularity theorem 给沿某子列的
`X^(beta-1/2-o(1))` 下界。对 zeros 取 supremum，得到式 (10)。`□`

所以任何 bound `B_A(X)=O_epsilon(X^(delta+epsilon))` 都推出全局条带

`Re rho<=1/2+delta`.                               (14)

## 4. Rank-one positive Weil fiber

定义

`V_X=C`, `v_X=B_A(X)`, `Q_X(v)=|v|^2`.            (15)

### 推论 JY（rank-one filtered zeta FPW）

式 (15) 连同 annular Euler trace、Mellin transform (3) 与 functional
equation 构成 rank-one quantitative filtered primitive Weil package。在一维
空间取 `ell_X(v)=v`，则 dual norm恒为 `1`；定理 JX 的独立 residue/exponent
证明给修订后 FPW4b 的 mode 下界。其 norm exponent 为

`max(0,2Theta-1)`.                                 (16)

FPW6 `Q_X(v_X)=X^(o(1))` 当且仅当 RH。

#### 证明

positivity 显然；Euler origin 来自式 (1)，off-center divisor visibility 来自
定理 JV/命题 JW，quantitative separation、exponent 与 tightness 来自定理 JX。因而可应用修订后的定理 JO；这里不以定性 visibility 代替下界。`□`

这个 rank-one package 只用于 filtered center-line detection。它一般不能恢复
全部 critical divisor、translation group 或正规化行列式，所以不能替代定理
JP 的 strong GNS package。

## 5. Gamma--Euler 标量结构定理

设中心为 `c/2`，并令 centered Euler Dirichlet series

`mathcal A_Z(s)=sum_n a_Z(n)n^(-s)`                (17)

在右侧绝对收敛，meromorphic continuation 的未知 poles 恰为目标 divisor；
已知 Tate/pole terms 已从 `a_Z` 中消去。定义

`B_(Z,A)(X)=sum_(X/A<n<=AX)a_Z(n)n^(-c/2)`.       (18)

### 定理 JZ（general rank-one annular Weil theorem）

假设 divisor 关于 `Re s=c/2` paired，对每个 off-center divisor pole 的
residue 非零，并满足标准有限阶增长。则

`int_0^infinity B_(Z,A)(X)X^(-z-1)dX`

`=M_A(z)mathcal A_Z(c/2+z)`.                       (19)

因此若

`B_(Z,A)(X)=X^(o(1))`,                             (20)

全部 divisor 位于 `Re s=c/2`。若中心线成立且 centered counting remainder
为 `O(X^(c/2)log(X)^K)`，则反向有 `B_(Z,A)=O(log(X)^K)`。

#### 证明

式 (19) 与定理 JV 相同。命题 JW 排除右半 `z` 平面的 multiplier zeros；
式 (20) 使 Mellin transform 在 `Re z>0` holomorphic，故无右侧 divisor。
paired symmetry 排除左侧 divisor。反向用 Stieltjes partial summation。`□`

它适用于 primitive Dirichlet L 函数的 paired package；对 automorphic data，
需要先准确中心化 pole/main terms，并验证 coefficient counting remainder 与
meromorphic series 的对应。

## 6. 与复杂 Hodge cores 的关系

rank-one criterion 在逻辑上最小，却没有让算术估计变容易：无条件 PNT 只给

`B_A(X)<<sqrt(X)exp[-c(logX)^(3/5)(loglogX)^(-1/5)]`, (21)

其 power exponent 仍为 `1/2`。将它推进到 subpower 正是 RH 的全部强度。

较高秩 cores 仍有两个独立价值：

1. 它们保留更多 divisor/translation geometry，可望产生 strong GNS
   Hilbert--Pólya structure；
2. arithmetic cancellation 可能在一个联合正矩阵中比单个 pointwise scalar
   bound 更容易通过 average、dispersion 或 Schur complement 证明。

因此 rank-one package 是最小中心线 detector，而文档 045–058 的高阶结构是
寻找非循环 Hodge positivity 证明机制的空间。

## 7. 数值审计

对 `A=4`：

| `X` | `B_4(X)` |
|---:|---:|
| 8 | 0.334990 |
| 16 | 0.0468891 |
| 32 | -0.000127899 |
| 64 | 0.0911291 |
| 128 | -0.154229 |
| 256 | 0.109740 |
| 512 | -0.154521 |

实现验证 `B_4(X)` 恰为文档 057 moment vector 的 `M_0`，并审计 multiplier
在左右开半平面的非消失。这些有限振荡不证明式 (20)。

# Chebyshev 单通道 Abel--Hodge 判据

文档 034 使用一个 Laplace-separating 测试族控制全部零点。本笔记证明
测试族可以压缩为一个普适指数核。对应的素数边界信号正是归一化
Chebyshev 误差 `(psi(x)-x)/sqrt(x)`；其加权平方积分的收敛横坐标精确
等于最右零点的中心偏移。这给出目前最小的算术 Hodge 结构：一个正标量
Abel 能量族已经足以迫使中心线。

## 1. 指数核与 Chebyshev 误差

把文档 032 的测试类从紧支撑光滑函数扩张到

`h_0(v)=e^(-v/2)1_(v>=0)`.                           (1)

其 Laplace 变换为

`H_0(w)=1/(w+1/2)`,                                  (2)

在 `Re w>0` 无零点。令

`psi(x)=sum_(n<=x)Lambda(n)`.                         (3)

### 命题 EO（the universal boundary signal is the Chebyshev error）

对 `x=e^t`，

`r_(h_0)(t)=(psi(x)-x)/sqrt(x)`.                     (4)

其 Laplace 变换在 `Re w>1/2` 为

`F_0(w)=int_0^infinity r_(h_0)(t)e^(-wt)dt`

`=(-zeta'/zeta(w+1/2))/(w+1/2)-1/(w-1/2)`.          (5)

#### 证明

素数部分逐项化为

`sum_(n<=x)Lambda(n)n^(-1/2)e^(-log(x/n)/2)`

`=x^(-1/2)sum_(n<=x)Lambda(n)=psi(x)/sqrt(x)`.        (6)

式 (2) 在 `w=1/2` 的值为一，所以被减 pole 主项是 `sqrt(x)`，得到式
(4)。再令 `s=w+1/2`；Stieltjes/Perron 恒等式给出

`int_1^infinity psi(x)x^(-s-1)dx=(-zeta'/zeta(s))/s`, (7)

而 `int_1^infinity x*x^(-s-1)dx=1/(s-1)`，得到式 (5)。`□`

与紧支撑边界通道相比，式 (1) 把所有乘法距离同时纳入，但指数权恰好消去
显式公式中的 `n^(-1/2)`，因此不再需要 separating 族。

## 2. 单标量正能量

对 `sigma>0` 定义

`I_sigma=2sigma int_1^infinity`

`                  |psi(x)-x|^2 x^(-2sigma-2)dx`.    (8)

由 `x=e^t`，这正是式 (4) 的 Abel Hodge norm：

`I_sigma=2sigma int_0^infinity`

`             |r_(h_0)(t)|^2e^(-2sigma t)dt`.        (9)

令

`Theta=sup_rho Re rho`,                              (10)

其中 `rho` 遍历非平凡零点。

### 定理 EP（Chebyshev L2 abscissa reads the rightmost zero）

有

`inf{sigma>0:I_sigma<infinity}=max(0,Theta-1/2)`.     (11)

#### 证明：解析性下界

若 `I_sigma<infinity`，Cauchy--Schwarz 使式 (5) 的左边在
`Re w>sigma` 解析。因 `H_0(w)=1/(w+1/2)` 在该区域无零，任何
`Re rho>1/2+sigma` 都会使式 (5) 有未消 pole，矛盾。因此

`Theta-1/2<=sigma`.                                  (12)

#### 证明：增长上界

固定 `theta>Theta`。标准 Perron contour shift（在零点右侧固定距离的
竖线上使用 `zeta'/zeta` 的多项式增长）给出

`psi(x)-x=O_theta(x^theta(log(2x))^A)`               (13)

对某个固定 `A`。若 `sigma>theta-1/2`，把式 (13) 代入式 (8)，所得幂
指数严格小于 `-1`，故积分收敛。对所有 `theta>Theta` 取下确界，结合
式 (12) 得式 (11)。`□`

定理 EP 是文档 034 定理 EJ 对非紧支撑指数核的精确延拓；式 (5) 的无零
因子避免了“测试函数可能恰好消掉某个零点”的问题。

### 推论 EQ（single-channel Hodge criterion for RH）

下列条件等价：

1. RH 成立；
2. 对每个 `sigma>0`，`I_sigma<infinity`；
3. 式 (8) 的收敛横坐标为零。

#### 证明

函数方程给出 `Theta>=1/2` 且 RH 等价于 `Theta=1/2`。应用定理 EP。也可
在正向使用经典 RH 后果
`psi(x)-x=O(sqrt(x)log^2 x)` 直接验证式 (8)。`□`

所以中心线所需的极限 Hodge 结构可由一个标量正 form 族表达，而无需先
构造高维上同调空间。真正困难完全浓缩为 Chebyshev 误差的临界加权
`L^2` 控制。

## 3. Hardy--Plancherel 平方分解

令

`s=1/2+sigma+i tau`.                                 (14)

### 命题 ER（vertical Hardy norm identity）

只要 `I_sigma<infinity`，就有

`I_sigma=(sigma/pi)int_R |(-zeta'/zeta(s))/s`

`                              -1/(s-1)|^2 d tau`.   (15)

特别地在 `sigma>1/2`，式 (15) 由绝对收敛 Euler 级数无条件成立。

#### 证明

函数 `r_(h_0)(t)e^(-sigma t)` 的 Fourier 变换由式 (5) 等于

`(-zeta'/zeta(s))/s-1/(s-1)`.                       (16)

Plancherel 定理给

`int_0^infinity |r_(h_0)(t)|^2e^(-2sigma t)dt`

`=(1/(2pi))int_R |(16)|^2d tau`.                     (17)

乘以 `2sigma` 得式 (15)。`□`

ER 把正 Abel--Hodge 能量同时表示为：

- 素数计数误差的加权平方；
- 中心化 logarithmic derivative 的 Hardy `H^2` 竖线范数。

因此把结构延拓到更小 `sigma` 等价于证明 Euler 对数导数去掉 pole 后属于
更大的 Hardy 半平面；离线零点正是阻止该延拓的 pole。

## 4. 一般 Gamma--Euler 计数函数

设 `Z` 的 Euler 对数导数为

`-Z'/Z(s)=sum_n b(n)n^(-s)`,                         (18)

完备 divisor 关于 `Re s=c/2` 对称。令

`Psi_Z(x)=sum_(n<=x)b(n)`,                           (19)

并从中减去所有已知右侧 poles `p` 的 Perron 主项

`M_Z(x)=sum_p m_p x^p/p`.                            (20)

取普适中心核

`h_c(v)=e^(-cv/2)1_(v>=0)`,                          (21)

其中心化信号为

`r_(Z,c)(log x)=x^(-c/2)(Psi_Z(x)-M_Z(x))`.          (22)

### 定理 ES（single-channel Gamma--Euler strip theorem）

在文档 031 的标准有限阶与 contour-shift 假设下，定义

`I_(Z,sigma)=2sigma int_1^infinity`

` |Psi_Z(x)-M_Z(x)|^2 x^(-c-2sigma-1)dx`.            (23)

其收敛横坐标等于

`max(0,sup_rho Re rho-c/2)`.                         (24)

因此若式 (23) 对每个 `sigma>sigma_0` 收敛，则全部非平凡零点位于

`|Re rho-c/2|<=sigma_0`; 对每个 `sigma>0` 收敛则得到广义 RH。

#### 证明

式 (21) 的 Laplace 变换为 `1/(w+c/2)`，在 `Re w>0` 无零；Perron 变换
把式 (22) 送到

`(-Z'/Z(c/2+w))/(c/2+w)-known pole fractions`.       (25)

定理 EP 的 Hardy 解析性下界与 contour-growth 上界逐字适用，最后使用
divisor 对称性。`□`

ES 是一个极简广义结构定理：Euler 计数函数的单个正加权 `L^2` 过滤足以
把全部零点压进中心条带，并在过滤宽度趋零时压到中心线。

## 5. 有限算术能量

对整数 `X>=2` 定义可直接由 von Mangoldt 数据计算的单调量

`I_sigma(X)=2sigma int_1^X`

`                  |psi(x)-x|^2x^(-2sigma-2)dx`.     (26)

在每个 `[n,n+1)` 上 `psi(x)=psi(n)`，所以式 (26) 是三个幂积分的有限和，
无需数值求积。脚本 `chebyshev_abel_energy` 实现这个精确分段公式。

每个 `I_sigma(X)>=0` 且随 `X` 单调。要由有限计算得到零自由条带，仍需一个
不引用零点的尾界

`sup_X I_sigma(X)<infinity`.                          (27)

定理 EP 表明：对 `sigma<1/2` 证明式 (27) 已是实质性新结果；对全部
`sigma>0` 证明它等价于 RH。

作为转录审计，在 `sigma=0.75` 时脚本给出

| `X` | `I_0.75(X)` |
|---:|---:|
| 13 | 1.19314351919022 |
| 101 | 1.19706108121560 |
| 1009 | 1.19711785417566 |

这些有限值只验证分段幂积分和单调性；即使在较小 `sigma` 下观察到缓慢
增长，也不能替代式 (27) 的无限尾证明。

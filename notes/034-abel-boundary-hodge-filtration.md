# Abel 加权边界 Hodge 过滤与零自由条带

文档 032 的 Besicovitch 极限要求长期均方有界，已与 RH 等价。为了把这个
终点拆成可逐级推进的目标，本笔记引入 Abel 权重 `e^(-2sigma t)`。每个
`sigma` 给出一个正 Hodge Gram form；它的最小可积参数精确等于该测试
通道所看见的零点离中心线的最大横向偏移。固定 `sigma` 的存在性给出一个
真实的全局零自由条带，而 `sigma->0` 恢复文档 032 的酉边界空间。

## 1. Abel 边界 Gram forms

沿用文档 032 的中心化素数信号

`r_h(t)=sum_n Lambda(n)n^(-1/2)h(t-log n)`

`                         -e^(t/2)H(1/2)`.           (1)

对 `sigma>0` 定义

`G_sigma(h,k)=2sigma int_0^infinity`

` r_h(t)conjugate(r_k(t))e^(-2sigma t)dt`,            (2)

只要积分收敛。任意有限测试族上的矩阵 `(G_sigma(h_j,h_k))` 自动正半定。

定义单通道的 `L^2` 收敛横坐标

`sigma_2(h)=inf{sigma>0:G_sigma(h,h)<infinity}`.      (3)

若集合为空则取 `infinity`。

## 2. 收敛横坐标精确读取零点偏移

对非平凡零点 `rho`，称它被 `h` 看见，若

`H(rho-1/2)!=0`.                                    (4)

令

`D(h)=sup{Re rho-1/2:rho is visible to h}`.           (5)

### 定理 EJ（Abel abscissa equals the visible zero abscissa）

对每个非零 `h in C_c^infinity((0,infinity))`，

`sigma_2(h)=max(0,D(h))`.                            (6)

#### 证明：上界

文档 031 定理 DV 在充分大的 `t` 给出

`r_h(t)=-sum_rho H(rho-1/2)e^((rho-1/2)t)`

` -sum_(m>=1)H(-2m-1/2)e^((-2m-1/2)t)`.             (7)

`H` 在包含所有非平凡零点横坐标的竖直带上快降，标准零点计数因此给出

`sum_rho |H(rho-1/2)|<infinity`.                     (8)

若 `sigma>D(h)`，第一和的绝对值至多为 `C_h e^(D(h)t)`，平凡零点和指数
衰减。故式 (2) 收敛，得到
`sigma_2(h)<=max(0,D(h))`（在右边为零时对任意 `sigma>0` 成立）。

#### 证明：下界

若式 (2) 在某个 `sigma` 收敛，则对 `Re w>sigma`，Cauchy--Schwarz 给出

`int_0^infinity |r_h(t)e^(-wt)|dt`

`<=||r_h e^(-sigma t)||_2`

`  (int_0^infinity e^(-2(Re w-sigma)t)dt)^(1/2)`.    (9)

所以 `r_h` 的 Laplace 变换在 `Re w>sigma` 解析。文档 032 式 (10) 把它
识别为

`H(w)(-zeta'/zeta(w+1/2))-H(1/2)/(w-1/2)`.          (10)

每个满足 `Re rho-1/2>sigma` 且式 (4) 的零点都会使式 (10) 有极点，矛盾。
因此 `D(h)<=sigma`。对所有可积 `sigma` 取下确界，与上界合并得到式
(6)。`□`

定理 EJ 不假设 RH。它把一个纯素数侧正 form 的收敛阈值与最右可见零点
精确等同。

## 3. 零自由条带的结构定理

称测试空间 `T_0` 为 separating，若每个 `w`、`Re w>0`，都有
`h in T_0` 满足 `H(w)!=0`。

### 定理 EK（fixed Abel-Hodge structure gives a zero-free strip）

若对某个 `sigma_0>=0`，一个 separating 测试空间的所有信号都满足

`G_sigma(h,h)<infinity` for every `sigma>sigma_0`,   (11)

则所有非平凡零点满足

`|Re rho-1/2|<=sigma_0`.                             (12)

特别地，若式 (2) 对每个 `sigma>0` 和 separating 测试族都存在，则 RH
成立。

#### 证明

定理 EJ 与 separating 性排除所有
`Re rho>1/2+sigma_0` 的零点。函数方程
`rho mapsto 1-conjugate(rho)` 排除对称的左侧区域，得到式 (12)。`□`

这提供一条分阶段路线：将 Abel 结构从无条件区域向左延拓到
`sigma_0<1/2`，会立即给出比 `0<Re rho<1` 更窄的全局条带；把阈值降到
零才是完整 RH。

## 4. 广义 Gamma--Euler Abel 结构

对文档 031 定理 DZ 的函数 `Z`，中心为 `c/2`，先从 Euler 边界信号中
减去所有已知右侧 pole 模态，再定义式 (2)。若 `rho` 是非平凡零点，定义
其偏移 `w_rho=rho-c/2`。

### 定理 EL（general Abel boundary-Hodge strip theorem）

在文档 031 的有限阶、Euler 对数导数、contour-shift 与 divisor 对称假设
下，单通道 Abel 收敛横坐标为

`sigma_(2,Z)(h)`

`=max(0,sup_(H(w_rho)!=0) Re w_rho)`.                (13)

若一个 separating 测试空间对所有 `sigma>sigma_0` 都具有有限 Abel
Gram forms，则 `Z` 的全部非平凡零点位于

`|Re rho-c/2|<=sigma_0`.                             (14)

#### 证明

把式 (10) 换成

`H(w)(-Z'/Z(c/2+w))-known pole terms`.               (15)

定理 EJ 的指数上界和 Laplace 解析性下界逐字适用；最后使用中心 divisor
对称性。`□`

EL 是一个“带宽版本”的广义中心线结构定理。它允许结构先只把零点约束在
中心条带，再由一族越来越强的正 Abel polarizations 把条带宽度压到零。

## 5. `sigma->0` 与 Besicovitch--GNS 极限

若 RH 成立，把不同零点纵坐标记作 `gamma`，重数为 `m_gamma`。忽略在
Abel 极限中消失的有限初段与平凡零点项，式 (7) 给出

`G_sigma(h,k)=sum_(gamma,delta)m_gamma m_delta`

` H(i gamma)conjugate(K(i delta))`

` [2sigma/(2sigma-i(gamma-delta))]+E_sigma(h,k)`,    (16)

其中 `E_sigma(h,k)->0`。

### 命题 EM（Abel polarizations converge to the boundary GNS form）

在 RH 下，

`lim_(sigma downarrow 0)G_sigma(h,k)`

`=sum_gamma m_gamma^2 H(i gamma)conjugate(K(i gamma))`

`=G_infinity(h,k)`.                                  (17)

#### 证明

式 (8) 使双和绝对收敛，而

`|2sigma/(2sigma-i(gamma-delta))|<=1`.               (18)

当 `sigma->0` 时，该因子在 `gamma=delta` 时为一，在不同频率时趋零。
控制收敛给出式 (17)。有限初段乘 `2sigma` 后消失；平凡零点和及交叉项同样
消失。`□`

所以文档 032 的 Besicovitch Hodge 空间是 Abel 正结构族在临界边界
`sigma=0` 的规范极限，而不是孤立定义。

## 6. Zeta 的无条件存在范围与障碍

由 `Lambda(n)<=log n` 和 `h` 的固定紧支撑，直接有

`r_h(t)=O_h((1+t)e^(t/2))`.                           (19)

因此：

### 命题 EN（unconditional half-plane Abel structure）

对 zeta，所有 Abel Gram forms 在

`sigma>1/2`                                           (20)

无条件存在并正半定。PNT 把式 (19) 改进为 `o_h(e^(t/2))`，但仍不足以把
任何固定 `sigma<1/2` 纳入式 (20)。对文档 035 的指数单通道，经典定量
PNT 误差还给出临界 `sigma=1/2` 的收敛；文档 036 命题 EX 说明这种
subpower 节省仍不能推进到任何固定 `sigma<1/2`。

若能无条件把存在范围推进到所有 `sigma>sigma_0`、某个
`sigma_0<1/2`，定理 EK 会给出此前未知的固定全局零自由条带。推进到
`sigma_0=0` 等价于 RH。因此“令 Abel 权重趋零”不是形式极限；每跨过一个
固定阈值都需要新的全球算术输入。

数值脚本 `zeta_boundary_zero_abel_gram` 计算式 (16) 的有限零点模型，并
检查 Hermitian 正半定性以及 `sigma` 减小时向命题 EB 的对角 Gram 收敛。
它只审计 Cauchy kernel 的符号和共轭，不是零自由证明。

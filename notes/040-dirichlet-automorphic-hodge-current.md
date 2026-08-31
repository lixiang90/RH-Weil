# Dirichlet 与 Gamma--Euler 算术 Hodge currents

文档 037–039 的一维 Hodge complex 不依赖 zeta 系数为正。把 von Mangoldt
current 换成复 Euler current，就得到 primitive Dirichlet 和固定 degree
Gamma--Euler 数据的统一结构。本笔记证明：同一个正 trace-class Green
极化无条件存在；GRH 等价于相应复 current 在所有临界 Hodge scales 中
具有有限能量。每个 Bessel 坐标仍只使用 Euler 乘积绝对收敛区的数据。

## 1. Primitive Dirichlet current

令 `chi` 是模 `N` 的 primitive nonprincipal Dirichlet character，并定义

`Psi_chi(x)=sum_(n<=x)Lambda(n)chi(n)`.               (1)

因完备 `L(s,chi)` entire，没有 pole 主项。定义复 current

`nu_chi=sum_(n>=2)Lambda(n)chi(n)delta_n`,            (2)

其累计值为 `Psi_chi(x)`。对 `sigma>0` 定义

`I_(chi,sigma)=2sigma int_1^infinity`

`                         |Psi_chi(x)|^2x^(-2sigma-2)dx`. (3)

### 定理 FP（Dirichlet Hodge membership criterion）

下列条件等价：

1. `L(s,chi)` 满足 GRH；
2. 对每个 `sigma>0`，`I_(chi,sigma)<infinity`；
3. 对每个 `sigma>0`，复 current `nu_chi` 属于文档 037 的
   `H_(-1,sigma)`；
4. 方程 `L_sigma phi_(chi,sigma)=nu_chi` 对每个 `sigma>0` 有有限
   Dirichlet energy 解。

#### 证明

取文档 035 的普适核 `h_0(v)=e^(-v/2)1_(v>=0)`。中心化信号为

`r_chi(log x)=Psi_chi(x)/sqrt(x)`.                   (4)

其 Laplace 变换在 `Re w>1/2` 为

`int_0^infinity r_chi(t)e^(-wt)dt`

`=(-L'/L)(w+1/2,chi)/(w+1/2)`.                      (5)

若式 (3) 在 `sigma` 收敛，Cauchy--Schwarz 使式 (5) 在
`Re w>sigma` 解析，故排除 `L(s,chi)` 在
`Re s>1/2+sigma` 的零点。又
`Psi_(bar chi)=conjugate(Psi_chi)`，所以同一个能量也排除
`L(s,bar chi)` 的右侧零点。函数方程把 `L(s,chi)` 的左侧零点映到
`L(s,bar chi)` 的右侧零点，因此对所有 `sigma>0` 的有限性给出 GRH。

反之，GRH 的标准显式公式给
`Psi_chi(x)=O(sqrt(x)log^2(Nx))`，代入式 (3) 对每个 `sigma>0` 收敛。
这证明 1 与 2。文档 037 定理 FB 的 Green-energy 恒等式对复 current 用
sesquilinear polarization 原封不动成立，给出 2–4 的等价。`□`

所以复系数不需要不定内积：`|Psi_chi|^2` 本身提供正 Hodge polarization，
而 paired functional equation 负责左右零点对称。

## 2. 收敛横坐标与无条件存在范围

令

`Theta_chi^pair=max(sup_(L(rho,chi)=0)Re rho,`

`                    sup_(L(rho,bar chi)=0)Re rho)`. (6)

### 命题 FQ（Dirichlet energy abscissa）

有

`inf{sigma>0:I_(chi,sigma)<infinity}`

`=max(0,Theta_chi^pair-1/2)`.                        (7)

#### 证明

式 (5) 对 `chi` 与 `bar chi` 分别给出解析性下界。反向在任意位于两组
零点右侧的竖线作 Perron contour shift，得到
`Psi_chi(x)=O(x^theta log^A(Nx))`，其中
`theta>Theta_chi^pair`；代入式 (3) 并取下确界。`□`

对固定 primitive character，平凡系数界无条件给出 `sigma>1/2` 的
有限能量。经典固定模数 PNT in arithmetic progressions（包含可能的单个
exceptional real-zero 项）还给出临界 `sigma=1/2` 的收敛，因为 exceptional
指数严格小于一。任何固定 `sigma<1/2` 的推进都会由式 (7) 给出新的全局
Dirichlet 零自由条带。

## 3. Twisted Bessel--Euler 坐标

沿用文档 038 的 `e_(n,sigma)` 与
`s_m=1+2sigma+2sigma m`、`c_m(j)`。定义

`A_(n,sigma,chi)=<nu_chi,e_(n,sigma)>`.              (8)

### 命题 FR（safe Euler formula for twisted Hodge coordinates）

有

`A_(n,sigma,chi)=C_(n,sigma)sum_(m>=0)c_m(j)`

`                         (-L'/L)(s_m,chi)`.          (9)

所有 `s_m>1`，故每项由绝对收敛 twisted Euler 级数

`(-L'/L)(s_m,chi)=sum_k Lambda(k)chi(k)k^(-s_m)`     (10)

给出。此外

`I_(chi,sigma)=sum_(n>=1)`

`               |A_(n,sigma,chi)|^2/lambda_(n,sigma)`. (11)

#### 证明

把文档 038 式 (18) 的 Bessel 幂级数与式 (2) pairing；这里没有 zeta 的
`-delta_1-dx` 背景项，所以只剩式 (10)，得到式 (9)。Green 算子的谱
分解给式 (11)。`□`

FR 把 Dirichlet GRH 化成一族完全位于 `Re s>1` 的 twisted Euler--Bessel
坐标的加权 `ell^2` 可和性。

## 4. 有限 character 族的矩阵 Hodge form

对 primitive characters `chi_1,...,chi_r`，定义矩阵

`G_sigma(i,j)=2sigma int_1^infinity`

` Psi_(chi_i)(x)conjugate(Psi_(chi_j)(x))`

`                         x^(-2sigma-2)dx`.           (12)

### 定理 FS（finite-family Dirichlet Hodge structure）

只要各积分有限，`G_sigma` 正半定。若对每个 `sigma>0` 该矩阵有限，则所有
`L(s,chi_j)` 满足 GRH。反之，若这些函数均满足 GRH，则式 (12) 对每个
`sigma>0` 存在，并在 Bessel 基中分解为

`G_sigma(i,j)=sum_n A_(n,sigma,chi_i)`

` conjugate(A_(n,sigma,chi_j))/lambda_(n,sigma)`.   (13)

#### 证明

式 (12) 是向量函数 `(Psi_(chi_j)(x))` 的 Gram 积分，故正。对角元应用
定理 FP 得中心线结论；Bessel Parseval 给式 (13)。`□`

这给出一个真正的矩阵 polarization，可同时承载一个有限 Artin/Dirichlet
packet，而不需要逐个另造 Green 几何。

## 5. 固定 degree Gamma--Euler 数据

设完备 `Z(s)` 中心为 `c/2`，

`-Z'/Z(s)=sum_n b(n)n^(-s)`,                         (14)

并令 `Psi_Z(x)=sum_(n<=x)b(n)`。减去所有已知右侧 poles 的 Perron 主项
`M_Z(x)`，定义 complex discrepancy

`E_Z(x)=Psi_Z(x)-M_Z(x)`.                            (15)

### 定理 FT（complex Gamma--Euler Hodge-current theorem）

在文档 026/035 的有限阶、Euler 收敛、Gamma growth 与中心 divisor 对称
假设下，令

`I_(Z,sigma)=2sigma int_1^infinity`

`                         |E_Z(x)|^2x^(-c-2sigma-1)dx`. (16)

若 `I_(Z,sigma)<infinity` 对所有 `sigma>sigma_0` 成立，则全部非平凡零点
位于

`|Re rho-c/2|<=sigma_0`.                             (17)

若对所有 `sigma>0` 成立，则对应广义 RH 成立。等价地，complex Euler
current `dE_Z` 属于文档 037 的全部相应负一阶 Hodge spaces。

#### 证明

复 current 的 Green norm 仍是式 (16)。其 Mellin transform 是

`(-Z'/Z(c/2+w))/(c/2+w)-known pole fractions`.       (18)

有限能量给右半平面解析性，排除右侧零点；paired divisor 对称排除左侧。
这就是文档 035 定理 ES/文档 037 定理 FE 的复 sesquilinear 版本。`□`

对于 fixed-degree tempered unitary Euler 数据，系数增长足以无条件定义
current、所有有限截断及 `sigma>1/2` 的能量；更强的存在区间由相应 prime
number theorem 决定。一般 Maass/GL(d) 若 local temperedness 未知，则
系数控制本身仍是独立的 Ramanujan 型输入，正如文档 026 的审计。

## 6. 存在性边界

Dirichlet/Gamma--Euler 情形现在具有与 zeta 完全平行的无条件部分：

1. universal Sturm--Liouville differential、正 polarization、trace-class
   Green operator；
2. complex Euler current 与全部有限 truncations；
3. 每个固定 Bessel coordinate 的绝对收敛 Euler 表达；
4. 有限 character packets 的正 Gram matrices。

开放部分仍是临界以下的统一 Hodge norm。该条件没有被“复系数”或
“twist”隐藏；命题 FQ 精确表明其收敛横坐标就是 paired divisor 的最右
偏移。

数值转录审计使用模 `5` 的 primitive quartic character。在
`sigma=0.75` 时，有限能量在 `X=13,101,1009` 分别为
`0.0539605560611`、`0.0586076023228`、`0.0587976915780`；共轭 character
逐值给出相同能量，验证了复 sesquilinear 规范化。有限数值不构成 GRH
证据。

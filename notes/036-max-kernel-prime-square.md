# Max-kernel 素数平方与 Selberg 卷积障碍

文档 035 把 RH 压缩为 Chebyshev 误差的单个正 Abel 能量。本笔记将该
能量完全展开到 von Mangoldt 系数。出现的平方不是通常的 Dirichlet
乘法卷积，而是由 `max(m,n)` 控制的有序累积核。这个核本身正定，并给出
一个规范 arithmetic discrepancy Hilbert scale；同时它解释了为什么
Selberg 对称公式的局部卷积平方不能直接提供所需的临界以下控制。

## 1. 无限 max-kernel 恒等式

令 `s=2sigma`。在 `sigma>1/2` 时，各项绝对收敛，可以展开

`I_sigma=2sigma int_1^infinity`

`                    (psi(x)-x)^2x^(-2sigma-2)dx`.   (1)

### 命题 ET（exact max-kernel prime-square identity）

对 `sigma>1/2`，

`I_sigma=[2sigma/(2sigma+1)]`

` sum_(m,n>=2) Lambda(m)Lambda(n)/max(m,n)^(2sigma+1)`

` -2sum_(n>=2)Lambda(n)/n^(2sigma)`

` +2sigma/(2sigma-1)`.                               (2)

等价地，若 `psi(n-1)=sum_(k<n)Lambda(k)`，则

`I_sigma=[2sigma/(2sigma+1)]sum_(n>=2)`

` [Lambda(n)^2+2Lambda(n)psi(n-1)]/n^(2sigma+1)`

` -2(-zeta'/zeta(2sigma))+2sigma/(2sigma-1)`.        (3)

#### 证明

平方项用 Tonelli/Fubini 展开：

`int_1^infinity psi(x)^2x^(-2sigma-2)dx`

`=sum_(m,n)Lambda(m)Lambda(n)`

` int_(max(m,n))^infinity x^(-2sigma-2)dx`

`=[1/(2sigma+1)]sum_(m,n)`

` Lambda(m)Lambda(n)/max(m,n)^(2sigma+1)`.           (4)

把双和按较大指标 `n` 分组，系数为

`Lambda(n)^2+2Lambda(n)psi(n-1)`，                  (5)

得到式 (3) 第一项。交叉项满足

`int_1^infinity psi(x)x^(-2sigma-1)dx`

`=[1/(2sigma)]sum_n Lambda(n)n^(-2sigma)`,           (6)

常数项为 `1/(2sigma-1)`。乘以 `2sigma` 得式 (2)–(3)。`□`

式 (2) 中三个部分在 `sigma downarrow 1/2` 时分别很大；有限的 Hodge
能量来自它们的联合重整化，不能逐项取绝对值。

## 2. 有限截断的精确重整化

对整数 `X>=2`，令 `N=X-1`，并记

`Delta psi^2(n)=psi(n)^2-psi(n-1)^2`

`=Lambda(n)^2+2Lambda(n)psi(n-1)`.                  (7)

### 定理 EU（finite renormalized max-kernel identity）

对任意 `sigma>0`、`s=2sigma`，

`I_sigma(X)`

`=[s/(s+1)]{sum_(n=2)^N Delta psi^2(n)n^(-s-1)`

`                         -psi(N)^2X^(-s-1)}`

` -2{sum_(n=2)^N Lambda(n)n^(-s)-psi(N)X^(-s)}`

` +s J_s(X)`,                                        (8)

其中

`J_s(X)=(X^(1-s)-1)/(1-s)` if `s!=1`,

`J_1(X)=log X`.                                      (9)

#### 证明

在文档 035 式 (26) 中分别展开三项，但只积分到 `X`。对平方项，

`int_(max(m,n))^X x^(-s-2)dx`

`=[max(m,n)^(-s-1)-X^(-s-1)]/(s+1)`.                (10)

所有 `m,n<=N` 的第二部分合成 `-psi(N)^2X^(-s-1)`；第一部分按最大指标
分组得到式 (7)。交叉项同理给出
`[sum Lambda(n)n^(-s)-psi(N)X^(-s)]/s`，常数项为式 (9)。乘以 `s`
得到式 (8)。`□`

EU 对 `sigma<1/2` 仍是完全有限、无条件的恒等式。困难被精确定位为式
(8) 三个增长部分在 `X->infinity` 时的统一联合相消。

## 3. 规范正核与 discrepancy 向量

定义

`K_sigma(u,v)=[2sigma/(2sigma+1)]`

`                         max(u,v)^(-2sigma-1)`.      (11)

### 命题 EV（max-kernel is a positive Hodge kernel）

`K_sigma` 是正定核。更具体地，在 `L^2([1,infinity),dx)` 中令

`Phi_(sigma,u)(x)=sqrt(2sigma)x^(-sigma-1)1_(x>=u)`. (12)

则

`K_sigma(u,v)=<Phi_(sigma,u),Phi_(sigma,v)>`.         (13)

若定义 signed arithmetic discrepancy measure

`dnu=-delta_1+sum_(n>=2)Lambda(n)delta_n-dx`,         (14)

则 `nu([1,x])=psi(x)-x`，而

`I_sigma=||int Phi_(sigma,u)dnu(u)||_2^2`             (15)

只要任一边有限。

#### 证明

式 (12) 的内积是

`2sigma int_(max(u,v))^infinity x^(-2sigma-2)dx`，   (16)

即式 (11)。对式 (14) 积分 feature，并交换积分次序，所得在位置 `x` 的
函数为 `sqrt(2sigma)x^(-sigma-1)(psi(x)-x)`；其平方范数就是式 (1)。`□`

因此 `I_sigma` 不是任意均方：它是一个由次序半格 `max` 规范产生的 Hodge
norm。zeta 的存在性问题变成同一个规范 discrepancy 向量 `nu` 是否属于
所有 `sigma>0` 的嵌套 Hilbert 能量空间。

## 4. 与 Selberg 对称平方的精确区别

Selberg 对称公式使用 Dirichlet 卷积系数

`(Lambda*Lambda)(n)=sum_(ab=n)Lambda(a)Lambda(b)`,    (17)

它来自 `(-zeta'/zeta(s))^2`。max-kernel 平方的系数却是式 (7)：

`Delta psi^2(n)=Lambda(n)^2+2Lambda(n)psi(n-1)`.     (18)

### 命题 EW（multiplicative convolution does not equal the Hodge square）

式 (17) 与式 (18) 不存在逐系数识别：

1. 若 `p` 是素数，式 (18) 含全局前缀 `2log(p)psi(p-1)`，取决于所有
   小于 `p` 的素数幂；
2. 在 `n=6`，`Lambda(6)=0`，故式 (18) 为零，而
   `(Lambda*Lambda)(6)=2log2 log3>0`。

因此把 Selberg 的乘法平方逐项代入式 (3) 不可能得到 max-kernel Hodge
能量；两者分别编码乘积偏序和通常次序。

#### 证明

第一条直接来自式 (18)。第二条按 `6=2*3=3*2` 计算式 (17)。`□`

EW 不排除利用 Selberg 恒等式作为更大论证的一部分；它排除的是把已有
Dirichlet convolution 正性直接当成文档 035 所需 Hodge 平方的捷径。

## 5. 现有 PNT 速率的阈值审计

### 命题 EX（subpower PNT errors do not cross a fixed Hodge strip）

若只使用形如

`|psi(x)-x|<=x exp(-omega(log x))`,                  (19)

其中 `omega(y)=o(y)`，则把该上界直接代入 `I_sigma` 只能保证
`sigma>1/2` 的收敛。若另有 `omega(y)>=c y^alpha`、`c,alpha>0`，则也能
保证临界值 `sigma=1/2` 收敛，但仍不能保证任何固定
`sigma<1/2`。

#### 证明

式 (19) 的平方 majorant 使式 (1) 至多由

`int_1^infinity x^(-2sigma)exp(-2omega(log x))dx`    (20)

控制。写 `x=e^y`，变成

`int_0^infinity exp((1-2sigma)y-2omega(y))dy`.       (21)

当 `sigma>1/2` 时线性项为负；当 `sigma=1/2` 且
`omega(y)>=cy^alpha` 时也收敛；当 `sigma<1/2` 且 `omega=o(y)` 时，该
majorant 发散。因此这种直接估计不能证明临界以下收敛。`□`

经典零自由区域给出的定量 PNT 误差属于第二种情形，所以可把文档 034
命题 EN 的无条件存在范围补到 `sigma>=1/2`；但任何固定改进仍需要真正的
幂节省，等价于新的全局零自由条带。

## 6. 广义 max-kernel Hodge 结构

对文档 035 的一般 Euler 计数误差

`E_Z(x)=Psi_Z(x)-M_Z(x)`，                            (22)

定义 signed discrepancy distribution `nu_Z=dE_Z`，连同其左端边界 atom。

### 定理 EY（max-kernel discrepancy structure theorem）

若对一个中心为 `c/2`、divisor 中心对称的 Gamma--Euler 数据，规范向量
`nu_Z` 对每个 `sigma>sigma_0` 都属于核

`K_(c,sigma)(u,v)=[2sigma/(c+2sigma)]`

`                         max(u,v)^(-c-2sigma)`       (23)

的能量空间，则全部非平凡零点满足

`|Re rho-c/2|<=sigma_0`.                             (24)

对所有 `sigma>0` 的 membership 给出广义 RH。

#### 证明

式 (23) 是 features
`sqrt(2sigma)x^(-c/2-sigma-1/2)1_(x>=u)` 的 Gram
核，其 discrepancy norm 是文档 035 式 (23)。应用定理 ES。`□`

EY 把广义中心线结论表达成一个纯正核/向量 membership 结构，形式上最接近
“存在一个 Hodge polarization 并使算术 cycle 具有有限 norm”。对 zeta，
核与有限 discrepancy 向量无条件显式存在；开放部分是临界以下的统一
有限能量。

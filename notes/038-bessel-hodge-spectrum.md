# Bessel 离散 Hodge 谱与 Euler 坐标

文档 037 构造的 Sturm--Liouville Hodge 算子可以完全对角化。Liouville
变量把半线压到有限区间，本征方程化为 Bessel 方程；Green trace 变成
Bessel 零点的 Rayleigh 和。更重要的是，算术 discrepancy current 的每个
Hodge 坐标都能写成只取值于 `Re s>1` 的绝对收敛 Euler 数据。RH 的剩余
条件因此成为一族完全显式坐标的加权 `ell^2` 可和性。

## 1. 精确本征方程

先考虑 zeta 的算子

`L_sigma=-d/dx [x^(2sigma+2)/(2sigma)]d/dx`,          (1)

左端 Neumann、无穷远衰减。令

`z=x^(-sigma)`,

`a=1+1/(2sigma)`, `nu=a-1=1/(2sigma)`.               (2)

### 定理 FF（Bessel diagonalization of the Hodge Laplacian）

`L_sigma` 的本征值为

`lambda_(n,sigma)=(sigma/2)j_(nu,n)^2`, `n>=1`,      (3)

其中 `j_(nu,n)` 是 `J_nu` 的第 `n` 个正零点。对应的规范化本征函数可取

`e_(n,sigma)(x)=C_(n,sigma)x^(-sigma-1/2)`

` J_(nu+1)(j_(nu,n)x^(-sigma))`,                     (4)

`C_(n,sigma)=sqrt(2sigma)/|J_(nu+1)(j_(nu,n))|`.     (5)

这些本征函数构成 `L^2([1,infinity),dx)` 的正交基。

#### 证明

写 `f(x)=g(z)`。直接微分把 `L_sigma f=lambda f` 化为

`g''(z)-(1+1/sigma)z^(-1)g'(z)+(2lambda/sigma)g(z)=0`. (6)

令 `g(z)=z^a h(z)`，式 (6) 变成阶数 `a` 的 Bessel 方程

`h''+z^(-1)h'+[k^2-a^2z^(-2)]h=0`,

`k^2=2lambda/sigma`.                                 (7)

`z->0` 对应 `x->infinity`。`Y_a` 分支不平方可积，故只保留
`g=z^aJ_a(kz)`。左端 Neumann 条件是 `g'(1)=0`；恒等式

`d/dz[z^aJ_a(kz)]=kz^aJ_(a-1)(kz)`                  (8)

给出 `J_nu(k)=0`，从而得到式 (3)–(4)。

换元 `x=z^(-1/sigma)` 后

`int_1^infinity |x^(-sigma-1/2)J_(nu+1)(jz)|^2dx`

`=(1/sigma)int_0^1 z J_(nu+1)(jz)^2dz`

`=J_(nu+1)(j)^2/(2sigma)`,                           (9)

最后一步使用 `J_nu(j)=0` 的 Bessel 积分恒等式，得到式 (5)。标准奇异
Sturm--Liouville 完备性给出正交基。`□`

## 2. Green trace 与 Rayleigh 和

### 命题 FG（Bessel Rayleigh sum equals the Hodge trace）

有

`sum_(n>=1)1/lambda_(n,sigma)=1/(2sigma+1)`.         (10)

#### 证明

Bessel 零点的 Rayleigh 恒等式为

`sum_(n>=1)j_(nu,n)^(-2)=1/[4(nu+1)]`.               (11)

代入式 (3) 与 `nu=1/(2sigma)` 得

`sum_n 2/[sigma j_(nu,n)^2]`

`=2/sigma *1/[4(1+1/(2sigma))]=1/(2sigma+1)`.        (12)

这与文档 037 命题 FA 的 kernel trace 完全一致。`□`

FG 是对 Green 核常数和边界条件的独立谱核对。

## 3. Arithmetic current 的离散 Hodge 展开

令 `nu_ar` 是文档 037 式 (13) 的 von Mangoldt discrepancy current。定义

`A_(n,sigma)=<nu_ar,e_(n,sigma)>`.                   (13)

当 `sigma>0` 时，每个单独坐标都良定义，因为式 (4) 在无穷远为
`O(x^(-1-2sigma))`。

### 定理 FH（spectral Hodge membership criterion）

对固定 `sigma>0`，下列条件等价：

1. `I_sigma<infinity`；
2. `nu_ar in H_(-1,sigma)`；
3. 离散谱和

   `sum_(n>=1)|A_(n,sigma)|^2/lambda_(n,sigma)`       (14)

   收敛。

并且在这些条件下

`I_sigma=sum_(n>=1)|A_(n,sigma)|^2/lambda_(n,sigma)`. (15)

因此 RH 等价于式 (14) 对每个 `sigma>0` 收敛。

#### 证明

由定理 FF 的谱分解，

`G_sigma=L_sigma^(-1)`

`=sum_n lambda_(n,sigma)^(-1)|e_(n,sigma)><e_(n,sigma)|`. (16)

故 current 的负一阶 norm 是式 (14)。文档 037 定理 FB 把同一 norm 识别
为 `I_sigma`，得到式 (15) 及三条件等价；再应用定理 FC 得 RH 陈述。`□`

这把连续 `x` 尾界替换为一个离散 Hodge 系数的 `ell^2(lambda^(-1))`
问题。

## 4. 只用绝对收敛 Euler 数据计算每个坐标

设

`q=1+2sigma`, `j=j_(1/(2sigma),n)`,

`C=C_(n,sigma)`.                                     (17)

Bessel 级数把式 (4) 展成

`e_(n,sigma)(x)=C sum_(m>=0)c_m(j)x^(-s_m)`,         (18)

其中

`s_m=q+(q-1)m>1`,                                    (19)

`c_m(j)=(-1)^m(j/2)^(2m+nu+1)`

`                 /[m! Gamma(m+nu+2)]`.              (20)

### 命题 FI（Euler-coordinate formula）

每个算术坐标满足

`A_(n,sigma)=-e_(n,sigma)(1)`

` +C sum_(m>=0)c_m(j)`

` {(-zeta'/zeta)(s_m)-1/(s_m-1)}`.                  (21)

式 (21) 中所有 `s_m>1`，所以 logarithmic derivative 由绝对收敛 Euler
级数给出；Bessel 级数按其自然顺序收敛到式 (13)。

#### 证明

式 (18) 来自 `J_(nu+1)` 的幂级数。指数计算为

`q/2+sigma(2m+nu+1)=q+(q-1)m=s_m`.                 (22)

对单项 `x^(-s_m)`，current pairing 为

`<nu_ar,x^(-s_m)>`

`=-1+sum_k Lambda(k)k^(-s_m)-int_1^infinity x^(-s_m)dx`

`=-1+(-zeta'/zeta)(s_m)-1/(s_m-1)`.                 (23)

所有 `-1` 项重求和为
`-C sum_m c_m(j)=-e_(n,sigma)(1)`，得到式 (21)。`□`

FI 很关键：Hodge Laplacian 的谱完全几何化，而每个 arithmetic coordinate
只调用 Euler product 的安全半平面。开放难点不再是单个坐标的定义，而是
当 Bessel 频率 `j_(nu,n)->infinity` 时这些高度振荡坐标的统一加权可和性。

## 5. 一般中心参数的精确谱

对文档 037 的一般算子，令

`q=c+2sigma>1`, `alpha=(q-1)/2`, `nu=1/(q-1)`.       (24)

### 定理 FJ（general Bessel Hodge spectrum）

`L_(c,sigma)` 的本征值为

`lambda_(n,c,sigma)=[(q-1)^2/(8sigma)]j_(nu,n)^2`,   (25)

规范本征函数为

`e_(n,c,sigma)(x)=sqrt(q-1)/|J_(nu+1)(j_(nu,n))|`

` x^(-q/2)J_(nu+1)(j_(nu,n)x^(-(q-1)/2))`.          (26)

并且

`sum_n lambda_(n,c,sigma)^(-1)`

`=2sigma/[q(q-1)]`,                                  (27)

与文档 037 定理 FE 的 trace 一致。

#### 证明

令 `z=x^(-alpha)`，重复定理 FF。所得 Bessel 阶数为
`nu+1`，Neumann 条件给 `J_nu(j)=0`，而
`k^2=2sigma lambda/alpha^2`，得到式 (25)。换元后的 norm 仍化为
`int_0^1zJ_(nu+1)(jz)^2dz`，给出式 (26)。最后把 Rayleigh 和式 (11)
代入式 (25)，得到式 (27)。`□`

## 6. 存在性审计

现在 zeta 的候选 Hodge 结构各层均为显式对象：

1. `L_sigma`、全部 `lambda_(n,sigma)` 与 `e_(n,sigma)` 无条件存在；
2. Green operator 正且 trace class；
3. arithmetic coordinates `A_(n,sigma)` 可由式 (21) 在 Euler 绝对收敛区
   逐个计算；
4. 每个有限谱截断

   `sum_(n<=N)|A_(n,sigma)|^2/lambda_(n,sigma)`       (28)

   无条件有限且单调。

唯一未证条件是式 (28) 对 `N->infinity` 的统一上界，尤其在
`sigma<1/2`。这不是 formal spectral theorem 的缺口，而是高 Bessel 模态
中 prime--continuum cancellation 的定量问题。式 (21) 为研究这种相消提供
了一个完全位于 `Re s>1` 的新坐标系统。

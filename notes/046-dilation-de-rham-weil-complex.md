# Dilation--de Rham 方块与连续 Weil--Hodge 复形

文档 045 从 triangular prime coefficient 的临界 Gram 极限构造了一个
离散酉 dilation。单个 dilation 只能记录 `e^(i gamma h)`，会把相差
`2pi/h` 的 ordinates alias。本笔记加入一个一阶 Hodge/Sobolev 层：有限
arithmetic 数据同时控制 triangular signal 及其导数时，临界 GNS 极限
产生强连续酉群、自伴生成元 `A`，以及

`Theta=c/2+iA`, `Theta*=c-Theta`.                    (1)

这恢复精确 ordinates，并把 normalized prime error、其 Riesz potential、
Frobenius dilation 与 Hodge differential 放进一个交换方块。

## 1. 无条件 dilation--de Rham 恒等式

先写中心为 `c/2` 的一般形式。令

`kappa=c/2+1`,

`E(x)=Psi(x)-M(x)`,

`C(X)=int_1^X E(x)dx`,                              (2)

并在 `t>=0` 定义

`p(t)=e^(-kappa t)C(e^t)`,

`f(t)=e^(-ct/2)E(e^t)`.                             (3)

记 `T_hg(t)=g(t+h)`、`r_h=e^(-kappa h)`，以及

`d_h=(T_h-r_hI)p`,

`g_h=(T_h-r_hI)f`.                                  (4)

zeta 情形为 `c=1`；`h=log2` 时，`d_h(logX)=(2X)^(-3/2)A(X)`。

### 命题 GU（arithmetic dilation--de Rham square）

在局部绝对连续/分布意义下，

`(partial_t+kappa)p=f`,                             (5)

`(partial_t+kappa)d_h=g_h`.                         (6)

因此下图交换：

`       p  --(partial+kappa)-->  f`

`       |                         |`

`   T_h-r_h                   T_h-r_h`

`       |                         |`

`       d_h --(partial+kappa)--> g_h`.              (7)

#### 证明

对式 (2) 使用 `C'(X)=E(X)`，链式法则给

`p'(t)=-kappa p(t)+e^(-(kappa-1)t)E(e^t)`

`     =-kappa p(t)+f(t)`,                           (8)

因为 `kappa-1=c/2`。常系数微分与 translation `T_h` 交换；把
`T_h-r_h` 作用于式 (5) 即得式 (6)。跳点集合测度为零，分布版本由局部
积分分部得到。`□`

这个方块完全来自 prime counting function，不使用零点或 RH。它是文档
001 的 Lefschetz--Frobenius compatibility 在一维 arithmetic current 上的
具体替代：横向是 Hodge differential，纵向是 normalized Frobenius
polynomial。

## 2. Finite Sobolev Grams 与连续 GNS

对 `sigma,T>0`、实 shifts `u,v>=0`，定义

`S_(sigma,T)(u,v)=2sigma int_0^T`

` [d_h(t+u)conj(d_h(t+v))`

`  +d_h'(t+u)conj(d_h'(t+v))]e^(-2sigma t)dt`.      (9)

任意有限 shift 集合给一个正半定矩阵。对 zeta，它只使用
`x<=exp(T+max(u,v)+h)` 的有限 von Mangoldt 数据。

令

`R_sigma(d_h)=2sigma int_0^infinity`

`       (|d_h(t)|^2+|d_h'(t)|^2)e^(-2sigma t)dt`.  (10)

### 定理 GV（critical Sobolev Grams produce a continuous Weil structure）

假设 `d_h` 局部 `H^1`，且

`sup_(0<sigma<=sigma_0)R_sigma(d_h)<infinity`.       (11)

则存在 `sigma_n downarrow0`，使所有有理 shifts 的 Gram entries 同时
收敛。任一 cofinal 极限产生：

1. 一个循环 Hilbert 空间 `H` 和强连续酉群 `U_u`；
2. 一个循环向量 `xi`，满足

   `<U_u xi,U_v xi>=lim_n 2sigma_n int_0^infinity`

   `d_h(t+u)conj(d_h(t+v))e^(-2sigma_n t)dt`;       (12)

3. `U_u=e^(iuA)` 的自伴生成元 `A`，且 `xi in Dom(A)`；
4. 对 `r_h=e^(-kappa h)`，向量

   `eta=(U_h-r_hI)^(-1)xi`,                         (13)

   `omega=(U_h-r_hI)^(-1)(iA+kappa)xi`             (14)

   都存在，并满足抽象交换方块

   `(iA+kappa)eta=omega`,

   `(U_h-r_h)eta=xi`,

   `(U_h-r_h)omega=(iA+kappa)xi`.                  (15)

最后，式 (1) 定义的闭算子满足 `Theta*=c-Theta`，所以
`Spec(Theta)` 位于 `Re s=c/2`。

#### 证明

式 (10) 的 `d_h` 部分给全部固定 shifts 的一致 Gram 界。对共同平移
`a>=0` 换元，低端 `[0,a]` 边界乘有 `2sigma`，故在 cofinal 极限消失；
极限 kernel 只依赖 `u-v`。有限 Gram 正性在极限保持。

由微积分基本定理和 Cauchy--Schwarz，

`|d_h(t+delta)-d_h(t)|^2`

`<=delta int_0^delta |d_h'(t+s)|^2ds`.             (16)

对它取 Abel mean，式 (11) 给极限估计

`||U_delta xi-xi||^2<=C delta^2`.                  (17)

所以正定 kernel 连续，GNS translation 强连续。谱定理还给

`int_R |e^(i delta lambda)-1|^2 dmu_xi(lambda)`

`<=C delta^2`.                                     (18)

除以 `delta^2` 并用 Fatou 引理，得到
`int lambda^2dmu_xi<infinity`，即 `xi in Dom(A)`。

命题 GO 说明 `U_h-r_hI` 有有界逆，且它是 `A` 的 bounded Borel
function，故保持 `Dom(A)` 并与 `A` 交换。这证明式 (13)–(15)。最后
`A*=A` 直接给

`Theta*=c/2-iA=c-Theta`.                            (19)

`□`

GV 是从 finite arithmetic objects 构造连续 Hilbert--Pólya 算子的结构
定理。式 (11) 是真正的开放输入；有限 Gram 正性本身无条件成立。

## 3. Triangular current 的显式正 Hodge kernel

对 zeta 及文档 035 的一般 Euler 数据，令 signed discrepancy current

`nu=-delta_1+sum_n Lambda_Z(n)delta_n-dM`,          (20)

使 `E(x)=nu([1,x])`。写 `q=e^h>1`，并定义 tent feature

`tau_(q,X)(u)=(qX-max(X,u))_+`.                     (21)

Fubini 给出

`A_q(X)=int_X^(qX)E(x)dx=<nu,tau_(q,X)>`.          (22)

### 命题 GW（positive Riesz-current kernel and Hardy domination）

令 `kappa=c/2+1`。triangular Abel energy

`J_(sigma,q)=2sigma int_0^infinity`

`             |d_h(t)|^2e^(-2sigma t)dt`           (23)

具有精确 current-square 表示

`J_(sigma,q)=int int K_(sigma,q,c)(u,v)dnu(u)conj(dnu(v))`, (24)

其中

`K_(sigma,q,c)(u,v)=2sigma q^(-2kappa)int_1^infinity`

`X^(-2kappa-2sigma-1)tau_(q,X)(u)tau_(q,X)(v)dX`.  (25)

`K` 是正 Gram kernel。把下限 `1` 换成 `0` 得到 homogeneous tail kernel
`K^0`，满足

`K^0(au,av)=a^(-c-2sigma)K^0(u,v)`.                (26)

当 `max(u,v)>=q` 时 `K=K^0`，所以算术尾精确具有该齐次性。

再令 normalized error 的 Abel Hodge energy 为

`I_sigma=2sigma int_1^infinity`

`       |E(x)|^2x^(-c-2sigma-1)dx`.                (27)

则有无条件 Hardy domination

`J_(sigma,q)<=C_(sigma,q,c) I_sigma`,              (28)

`C_(sigma,q,c)`

`=(q-1)q^(-c-2)[q^(c+2sigma+1)-1]/(c+2sigma+1)`.  (29)

#### 证明

式 (22) 代入式 (23)，用 `X=e^t` 并交换积分，得到式 (24)–(25)；正性
来自 features `tau_(q,X)` 的 Gram 积分。式 (26) 由 `X=ay` 换元。

Cauchy--Schwarz 给

`|A_q(X)|^2<=(q-1)X int_X^(qX)|E(x)|^2dx`.         (30)

代入式 (23)，交换 `X,x`，并把实际 `X>=1` 区间扩大到 `[x/q,x]`。积分

`int_(x/q)^x X^(-c-2sigma-2)dX`

`=[q^(c+2sigma+1)-1]x^(-c-2sigma-1)`

` /(c+2sigma+1)`，即得式 (28)–(29)。`□`

GW 把新结构的 polarization 完全写成一个显式、正、齐次的
prime--continuum double kernel。它比文档 036 的 max kernel 多一次 Riesz
平滑；式 (28) 说明 Chebyshev current Hodge norm 控制 triangular norm。
反向固定参数界一般不存在，但稳定 dilation resolvent 在临界酉 quotient
中提供无损反演。

## 4. Zeta 的连续谱坐标

固定 `c=1,h=log2,kappa=3/2`。

### 定理 GX（continuous cyclic Weil complex for zeta）

下列条件等价：

1. RH 成立；
2. `sup_(0<sigma<=1)R_sigma(d_(log2))<infinity`；
3. finite Sobolev Grams (9) 沿 `T->infinity`、`sigma downarrow0` tight，
   并生成定理 GV 的连续 Weil--Hodge 复形。

RH 下该极限唯一。若 `rho=1/2+i gamma` 的重数为 `m_gamma`，则三个循环
vectors 在频率 `gamma` 的坐标分别为

`xi_gamma=-m_gamma[2^(i gamma)-2^(-3/2)]`

`                    /[rho(rho+1)]`,               (31)

`eta_gamma=-m_gamma/[rho(rho+1)]`,                 (32)

`omega_gamma=-m_gamma/rho`.                        (33)

特别地，`A` 的循环谱是精确 ordinates `gamma`，而

`Theta=1/2+iA` 的循环谱是非平凡零点。相同 ordinate 的重数被压进向量
权重 `m_gamma^2`；单循环模型不恢复一个 `m_gamma` 维 eigenspace。

#### 证明

条件 2 包含文档 045 的 triangular `L^2` tightness，故由定理 GR 推出
RH。反之在 RH 下，式 (31) 的 coefficients 绝对可和；其一阶导数的
Besicovitch 平方和按

`sum_gamma m_gamma^2/gamma^2`                       (34)

收敛。这里使用标准 zero counting 与局部 multiplicity bound。故式 (10)
一致有界，定理 GV 适用。

命题 GS 已给式 (31)–(32)。在频率 `gamma`，`iA+kappa` 乘以
`i gamma+3/2=rho+1`，再除以
`2^(i gamma)-2^(-3/2)`，得到式 (33)。强连续群消除了文档 045 离散模型
中的 phase alias。`□`

### 无条件存在区间

经典定量 PNT 给

`f(t),d_h(t),d_h'(t)=O(e^(t/2-c_0 sqrt(t)))`.       (35)

所以 finite Sobolev Grams 全部无条件存在，infinite Abel Sobolev Gram 在
`sigma>=1/2` 也无条件收敛。把它推进到任何固定 `sigma<1/2` 会给出相应
全局零自由条带；推进到 `sigma downarrow0` 正是 RH。

## 5. 广义连续 Weil--Hodge 结构定理

### 定理 GY（Gamma--Euler dilation--de Rham structure theorem）

设中心对称 Gamma--Euler datum 满足文档 GT 的显式公式、有限阶 counting
及标准非平凡条带条件。若某个 `h>0` 的 arithmetic signal `d_(Z,h)` 满足
临界 Sobolev tightness (11)，则：

1. finite prime-current Grams 的 cofinal 极限产生一个强连续酉 dilation
   群 `U_t=e^(itA)`；
2. arithmetic potential、current 与 Riesz vector 实现式 (13)–(15) 的
   dilation--de Rham 方块；
3. `Theta=c/2+iA` 满足 `Theta*=c-Theta`；
4. 显式公式中每个非平凡 divisor point 都位于 `Re s=c/2`。

反之，若中心线结论成立，且一次 Riesz coefficients 与其一阶导数满足由
标准 divisor counting 保证的平方可和性，则 Sobolev tightness 成立，极限
谱坐标为

`A: gamma=Im rho`, `Theta: rho=c/2+i gamma`.        (36)

#### 证明

1–3 是定理 GV。仅 `d` 的 `L^2` 部分已由定理 GT 的 Mellin pole 论证排除
所有 `Re rho>c/2` 的 points，divisor 对称排除左侧，得 4。反向时，Riesz
coefficient 为 `O(|rho|^(-2))`，一阶导数为 `O(|rho|^(-1))`；假设的
counting/multiplicity 平方和给临界 Sobolev Gram，谱展开给式 (36)。`□`

GY 抽离出的广义结构是

`(finite current Grams, de Rham differential, normalized dilation,`

` critical Sobolev compactness)`.                  (37)

前三项对 zeta 已由 primes 无条件构造；第四项是尚缺的 Hodge--Riemann
紧性输入。与直接假设 `Theta*=c-Theta` 不同，这里 `Theta` 是有限算术
Gram 的 GNS 极限，因此存在性问题被保留而没有藏进定义。

## 6. 可攻击接口与证据边界

这一连续复形提供三个比单纯 `A(X)=O(X^(3/2+epsilon))` 更细的接口：

- 式 (25) 的正齐次 kernel 可按 dyadic ratio blocks 分解，并直接接入
  large-sieve/dispersion 方法；
- 式 (9) 同时测试 potential 与一阶 current，允许用 finite Sobolev
  Schur complements 认证 translation continuity；
- `U_h-r_h` 的逆范数至多 `1/(1-r_h)`，从 Riesz vector 恢复 current
  时没有由零点高度产生的 small denominator。

这些结构和恒等式不证明临界 tightness。有限 Gram 数值正性、固定截断
特征值或 `sigma>=1/2` 的收敛都不是 RH 证书。

一次有限审计取 `t=0,0.1,...,2`、权 `e^(-t/3)` 与 shifts
`0,0.2,0.4,0.6`。式 (9) 的四个本征值为

`0.03110203, 0.05156832, 0.08265263, 0.62543312`,    (38)

trace 为 `0.79075610`。在 `X=13.25,q=2`，交换方块式 (6) 两侧的
60-digit 数值误差约 `1.15e-41`。这只验证有限公式与正性。

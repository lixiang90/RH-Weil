# Canonical 二通道 Vaughan quotient 与 arithmetic-length localization

文档 153--162 把 centered Vaughan 分解提升为四分量 Hodge Gram，并研究其
低秩通道。文档 162 的 compression no-free-lunch 又指出：若 core channel
仍含完整物理方向，小 tail 本身不能控制目标。本笔记不再拟合新的 basis，而是回到
Vaughan 恒等式的逐系数代数，取一个由 physical synthesis 与 Type I/II support
共同决定的规范 quotient。

主要结论是：

1. 四个未中心化分量在物理方向上精确商化为一个 Type I 向量与一个 Type II
   向量；相应 Hodge Gram 只有 `2 x 2`，不需要 PCA、冻结 seeds 或 Feshbach
   近似；
2. Type II 在 `(U+1)(V+1)` 之前严格为零，而 Type I 在同一区间逐项等于
   `Lambda`。这是 cutoff 的 support-product 守恒：把 Type II 推远必把同一段
   prime current 完整留在 Type I；
3. 在 height `T` 取 `U_T=T/log^A T` 时，`n<=U_T` 的低 prime-power Hodge
   向量可用 Chebyshev bound 无条件证明 barrier-weighted dyadic 可和；
4. 因而 RH-strength 输入可以严格局部化到 Type I 中 `n>U_T` 的 Möbius残差与
   support `n>U_TV_T` 的 Type II 残差的一个精确 `2 x 2` Gram。

这没有证明 RH；它消除了经验 channel geometry，并无条件删去了 actual-cycle
预算中的低算术长度部分。

## 1. 从四分量到 canonical Type I/II

沿文档 153，令

`mu_1=mu 1_(n<=U)`, `mu_2=mu-mu_1`,

`Lambda_1=Lambda 1_(n<=V)`, `Lambda_2=Lambda-Lambda_1`, (1)

并定义

`a_U=mu_1*1`, `X=a_U*Lambda_2`.                  (2)

四个未中心化 Vaughan 分量是

`P_1=mu_1*log`,

`P_2=-mu_1*Lambda_1*1`,

`P_3=mu_2*Lambda_2*1`,

`P_4=Lambda_1`.                                  (3)

### 定理 ACP（canonical two-channel Vaughan quotient）[U]

定义

`I_(U,V)=P_1+P_2+P_4=X+Lambda_1`,                (4)

`II_(U,V)=P_3=Lambda-Lambda_1-X`.                 (5)

则逐整数精确成立

`Lambda=I_(U,V)+II_(U,V)`.                       (6)

式 (4) 是 Type I/low-prime channel，式 (5) 是真正的 Type II channel；两者
只使用 `mu,Lambda` 与有限 cutoffs，不使用零点。

#### 证明

由 `log=Lambda*1`，

`P_1+P_2=mu_1*(Lambda-Lambda_1)*1`

`         =mu_1*Lambda_2*1=X`.                  (7)

另一方面 `mu*1=epsilon`，故

`P_3=(mu-mu_1)*Lambda_2*1`

`   =Lambda_2-mu_1*Lambda_2*1`

`   =Lambda-Lambda_1-X`.                         (8)

式 (4)--(6)随即得到。`□`

## 2. 精确 Gram quotient

令 `T` 是从有限系数列到任意复 Hilbert space `H` 的共同线性 synthesis；它可
包含 Abel weight、vertical modulation、interval-incidence feature 与 finite
truncation。记 `p_r=T(P_r)`，并令四分量 Gram 为

`G_4(r,s)=<p_r,p_s>`.                             (9)

定义固定实矩阵

`S=[[1,1,0,1],[0,0,1,0]]`.                       (10)

### 定理 ACQ（physical Gram is an exact two-channel quotient）[U]

令

`q_I=p_1+p_2+p_4`, `q_II=p_3`,                   (11)

`G_2=S G_4 S^*`.                                 (12)

则 `G_2>=0`，并且

`(1,1)G_2(1,1)^*=1^*G_4 1`

`                  =||q_I+q_II||^2`.             (13)

换言之，四分量 physical energy 到 `2 x 2` Type I/II Gram 的传递没有
approximation、angle、tail 或 coupling error。

#### 证明

式 (12)是 Gram 在固定线性 map 下的 push-forward，故半正定。又有
`S^*(1,1)^*=1_4`，代入式 (12)即得式 (13)。`□`

这不是说任意一向量 energy 不能平凡地写成 `1 x 1` Gram；二通道 quotient 的
信息在于它同时保留标准 Type I convolution 与真正 Type II support gap。它也
不声称 `G_4` 自身 rank 至多二；被 quotient 删除的是不影响 physical sum 的
label redistribution。

## 3. Support-product 守恒

### 定理 ACR（Type II gap = Type I agreement range）[U]

记

`Q_(U,V)=(U+1)(V+1)`.                             (14)

则

`II_(U,V)(n)=0`, `1<=n<Q_(U,V)`,                 (15)

并因而

`I_(U,V)(n)=Lambda(n)`, `1<=n<Q_(U,V)`.          (16)

特别地，

`R_I(n):=I_(U,V)(n)-Lambda(n)1_(n<=U)`           (17)

支撑于 `n>U`。

#### 证明

展开式 (5)的第一种表达，`II(n)` 中每个非零三因子项都满足
`n=dmr`、`d>U`、`m>V`、`r>=1`，所以
`n>=(U+1)(V+1)`。式 (16)来自式 (6)，式 (17)再用
`Q_(U,V)>U+1`。`□`

定理 ACR 是严格的 cutoff no-free-lunch：增大 `UV` 会推迟 Type II，但在完全
相同的区间上 Type I 逐项复制原始 `Lambda`。因此“Type II tail 很小”不能自动
完成证明；必须同时控制 Type I 与 continuum 的 Hodge cancellation。

## 4. 二通道 continuum gauge

令 `p_I,p_II,c in H` 分别是式 (4)--(5)的 prime vectors 与完整 continuum
vector。对实数 `alpha` 定义

`v_I(alpha)=p_I-alpha c`,

`v_II(alpha)=p_II-(1-alpha)c`.                   (18)

于是 `v_I+v_II=p_I+p_II-c` 与 `alpha` 无关。记

`C=||c||^2>0`,

`x_I=Re<p_I,c>`, `x_II=Re<p_II,c>`.              (19)

### 定理 ACS（optimal two-channel continuum gauge）[U]

安全 diagonal budget

`D_2(alpha)=||v_I(alpha)||^2+||v_II(alpha)||^2`   (20)

有唯一极小点

`alpha^*=1/2+(x_I-x_II)/(2C)`.                   (21)

极小值为

`D_(2,min)=||p_I||^2+||p_II||^2`

`          -(x_I^2+x_II^2)/C`

`          +(C-x_I-x_II)^2/(2C)`.                (22)

并且

`||p_I+p_II-c||^2<=2D_(2,min)`.                  (23)

#### 证明

展开式 (20)得到关于 `alpha` 的严格凸二次多项式；令导数为零给式 (21)，代回
给式 (22)。式 (23)是二向量 Cauchy--Schwarz。`□`

相对文档 154 的四分量 gauge，式 (23)把固定安全因子从 `4` 降为 `2`。更重要的
是，可以完全保留 balanced `2 x 2` Gram 的 cross entry，而不使用式 (23)。

## 5. 低算术长度的无条件 dyadic 消去

令

`q_(Y,sigma)(n)=n^(-sigma)e^(-n/Y)`,

`1/2<=sigma<=3/4`.                               (24)

在 cofinal schedule 中 `sigma=1/2+delta_Y->1/2`，所以该范围最终自动满足；有限个初始尺度只改变统一常数。

并在文档 151--152 的 interval Hilbert space `H_h` 中记

`e_n=1_[logn-h,logn]`, `||e_n||=sqrt(h)`.         (25)

对任意 modulation center `tau` 定义 low-prime vector

`L_U=sum_(n<=U)Lambda(n)q_(Y,sigma)(n)n^(-itau)e_n`. (26)

### 引理 ACT（elementary low-length Hodge bound）[U]

存在 absolute `C_0`，使对全部式 (24)参数

`||L_U||^2<=C_0 h U^(2(1-sigma))`

`          <=C_0 hU`.                            (27)

#### 证明

Chebyshev bound `psi(x)<=C x` 与 partial summation给，在式 (24)的统一参数
范围内，

`sum_(n<=U)Lambda(n)n^(-sigma)<=C' U^(1-sigma)`. (28)

Abel factor至多一，modulation绝对值为一。由 triangle inequality及式 (25)，

`||L_U||<=sqrt(h)sum_(n<=U)Lambda(n)n^(-sigma)`， (29)

平方即得式 (27)。`□`

取 dyadic heights `T_k=2^k`，`B_k=T_k/2`，故
`h_k=theta/B_k asymp1/T_k`。若 barrier

`beta_k>=c log(e+T_k)`                           (30)

并对任意 fixed `A>0` 取

`U_k=max(1,floor[T_k/log^A(e+T_k)])`,             (31)

则式 (27)给

`sum_k ||L_(U_k)||^2/beta_k`

` <<sum_k 1/log^(A+1)(e+2^k)<infinity`.           (32)

式 (32)对 `Y`、`delta=sigma-1/2` 与全部 modulation centers一致。这是新的
无条件 localization：平方根 vertical core内，每块 `n<=T/log^A T` 的 prime
current已不再承载 RH 难度。

## 6. Hard two-channel center-line criterion

按每个 dyadic block选择式 (31)的 `U_k` 和任意 `V_k>=1`。由定理 ACR写

`p_I=L_(U_k)+r_I`,                                (33)

其中 `r_I` 的算术系数支撑于 `n>U_k`，而 `p_II` 支撑于

`n>=(U_k+1)(V_k+1)`.                              (34)

把 continuum 放入 hard pair，记

`W_k=r_(I,k)+p_(II,k)-c_k`.                       (35)

### 定理 ACU（arithmetic-length-localized Hodge criterion）[U]

在文档 150--151 的 square-root-core、barrier 与 analytic hypotheses 下，若沿
一条 cofinal Abel schedule

`sup_Y sum_(k in core)||W_k||^2/beta_k<infinity`, (36)

则 RH 成立。

同样可把式 (36)替换为 `r_I,p_II,c` 的 exact balanced `2 x 2` Gram bound，
或用定理 ACS 的 `2D_(2,min)` 作为更强充分条件。

#### 证明

完整 block vector是 `L_(U_k)+W_k`，故

`||L_(U_k)+W_k||^2<=2||L_(U_k)||^2+2||W_k||^2`. (37)

第一项按式 (32) barrier-weighted 可和，第二项由式 (36)控制。文档 150 已无条件
控制 square-root core 外部；把所得 modulated-energy budget代入文档 151 定理
AAO，即得 RH。`□`

定理 ACU 没有把 RH 藏入结构定义：Hilbert space、cutoffs、两个卷积 vectors、
support gaps与 low-length bound全部无条件。式 (36)明确是剩余的 RH-strength
arithmetic input。

## 7. 对广义 Gamma--Euler 数据的范围

定理 ACP--ACR 只使用一个带截断的交换卷积代数，以及

`mu*1=epsilon`, `log=Lambda*1`.                   (38)

因此它逐字适用于具有相应 twisted/inverse coefficient identities 的 Dirichlet
或 Gamma--Euler datum。若 fixed-degree local temperedness进一步给

`|Lambda_A(n)|<=d Lambda(n)`,                     (39)

则引理 ACT 与式 (32)只多固定因子 `d^2`。所以“低算术长度无条件消去 + hard
二通道 Gram”也是一个广义结构接口；对每个具体 L-function仍须验证式 (38)的
正确 twisted 版本和 ramified/Gamma corrections，不能仅由函数方程假定。

## 8. 审计边界与下一步

本笔记无条件完成：

- 从四分量 label Gram 构造 data-independent exact Type I/II quotient；
- 证明 Type II support gap与 Type I target-agreement range完全相同；
- 给出最优二通道 continuum gauge；
- 证明 `n<=T/log^A T` 的 low-prime Hodge budget在全部 dyadic heights上可和；
- 把未证输入局部化到式 (35)的两个 hard channels。

尚未完成：

- 对 `r_I` 的 signed truncated-Mobius correlation给 uniform matrix Bessel bound；
- 对 `p_II` 的 near-product incidences给 barrier-weighted bilinear large sieve；
- 控制 `r_I` 与 `p_II-c` 的 cross Gram，而不退回破坏相消的绝对值 majorant；
- 证明式 (36)。

下一步应固定式 (31)，在 multiplicative rectangles上直接展开 hard `2 x 2`
Gram。首先分别计算 diagonal incidence kernels，再保留 Möbius signs研究 cross
kernel；任何只按 `|mu(d)|` 求和的估计都应与定理 ACR 的 target-agreement账本
同时比较，防止把原问题原样留在 Type I 中。
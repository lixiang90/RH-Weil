# 半局部 Weil 矩阵的显式尾界

本笔记把文档 004 中低高耦合的矩阵尾和变成显式可求和的不等式。记 `L=2log(lambda)`，并使用 Connes–Consani–Moscovici 的周期基 `V_n`。令

`W_(n,m)=QW_lambda(V_n,V_m)`。

论文公式给出

`W_(n,m)=W_(0,2)(n,m)-W_R(n,m)-W_P(n,m)`,                (1)

其中最后两项分别为无穷处与有限素数贡献。

## 1. 基本振荡函数的双重界

对 `n!=m`，论文的函数为

`q_(n,m)(x)=[sin(2pi m x/L)-sin(2pi n x/L)]/[pi(n-m)]`,

`0<=x<=L`。

### 引理 N

若 `d=|m-n|>=1`，则

`|q_(n,m)(x)| <= min(2x/L, 2/(pi d))`.                    (2)

#### 证明

由 `|sin A-sin B|<=|A-B|` 得到第一项 `2x/L`；分别以 `1` 控制两个正弦得到第二项。`□`

第一项消除了无穷处核在 `x=0` 的表面奇性，第二项给出关于频率差的衰减；两者缺一不可。

## 2. 三项分别估计

定义有限的素数质量

`P_lambda=sum_(2<=k<=lambda^2) Lambda(k)k^(-1/2)`.         (3)

### 极点项

论文 (4.2) 给出精确值

`B_(n,m) = 32L sinh(L/4)^2 |L^2-16pi^2mn|`

`/[(L^2+16pi^2m^2)(L^2+16pi^2n^2)]`.                    (4)

因此 `|W_(0,2)(n,m)|=B_(n,m)`。

### 素数项

由式 (2)，

`|W_P(n,m)| <= 2P_lambda/(pi d)`.                         (5)

### 无穷处项

当 `n!=m` 时，论文 (4.4) 中的对角常数消失，故

`W_R(n,m)=integral_0^L rho(x)q_(n,m)(x)dx`,

`rho(x)=e^(x/2)/(e^x-e^(-x))`。

因为 `2sinh(x)>=2x` 且 `e^(x/2)<=e^(L/2)=lambda`，

`rho(x)<=lambda/(2x)`.                                   (6)

以 `x_0=L/(pi d)` 分割积分。在 `[0,x_0]` 使用式 (2) 第一项，在 `[x_0,L]` 使用第二项，得到

`|W_R(n,m)| <= lambda[1+log(pi d)]/(pi d)`.               (7)

这里 `d>=1` 保证 `0<x_0<L`。

## 3. 单个矩阵元素的显式界

### 定理 O（off-diagonal Weil matrix bound）

对所有 `n!=m`，令 `d=|m-n|`，则

`|W_(n,m)| <= B_(n,m)`

` + {lambda[1+log(pi d)]+2P_lambda}/(pi d)`.              (8)

#### 证明

对分解式 (1) 使用三角不等式以及式 (4)、(5)、(7)。`□`

该估计完全由有限素数和、初等函数及整数指标组成，不使用 RH、零点位置或 Weil 二次型正性。

## 4. 固定低模的平方尾

固定 `n`，记

`D_n=L^2+16pi^2n^2`,

`A_(lambda,n)=2L sinh(L/4)^2[L^2+16pi^2|n|]/(pi^2 D_n)`,

`C_(lambda,n)=A_(lambda,n)+4P_lambda/pi+2lambda/pi`.       (9)

若 `|m|>=1`，由式 (4) 直接有

`B_(n,m)<=A_(lambda,n)/|m|`.                              (10)

若再有 `|m|>N>=2|n|`，则 `d>=|m|/2` 且

`log(pi d)<=log(2pi|m|)`。因此定理 O 推出

`|W_(n,m)| <= C_(lambda,n)[1+log(2pi|m|)]/|m|`.           (11)

### 定理 P（显式平方尾）

若 `N>=max(1,2|n|)`，令 `b_N=1+log(2pi N)`，则

`sum_(|m|>N)|W_(n,m)|^2`

`<= (2C_(lambda,n)^2/N)[b_N^2+2b_N+2]`.                  (12)

#### 证明

式 (11) 后只需估计正整数尾。函数

`f(x)=[1+log(2pi x)]^2/x^2`

在 `x>=1` 单调下降，所以

`sum_(m>N)f(m)<=integral_N^infinity f(x)dx`

`=[b_N^2+2b_N+2]/N`。

正负两个尾使用同一上界，产生式 (12) 的因子 `2`。`□`

特别地，固定 `lambda,n` 时

`sum_(|m|>N)|W_(n,m)|^2=O_(lambda,n)(log(N)^2/N)`.         (13)

## 5. 分离奇核后去掉对数损失

上一节为了完全初等地逐点取绝对值，损失了一个 `log N`。无穷处核的奇性可以精确分离：

`rho(x)=1/(2x)+r_lambda(x)`,

`R_lambda=integral_0^L |r_lambda(x)|dx<infinity`.          (14)

### 定理 Q（无对数 off-diagonal 界）

对 `n!=m`、`d=|m-n|`，

`|W_R(n,m)| <= |Si(2pi m)-Si(2pi n)|/(2pi d)`

` + 2R_lambda/(pi d)`                                    (15)

` <= [4+2R_lambda]/(pi d)`。

从而有更适合严格计算、保留有限素数抵消的逐项界

`|W_(n,m)| <= B_(n,m)+|W_P(n,m)|`

` + |Si(2pi m)-Si(2pi n)|/(2pi d)+2R_lambda/(pi d)`,     (16a)

以及较粗但便于闭式求和的

`|W_(n,m)| <= B_(n,m)`

` + [4+2R_lambda+2P_lambda]/(pi d)`.                     (16)

#### 证明

奇核部分可精确积分为

`[Si(2pi m)-Si(2pi n)]/[2pi(n-m)]`，

其中 `Si(x)=integral_0^x sin(t)dt/t`。一个足够的全局初等界是 `|Si(x)|<=4`：当 `|x|<=1` 时直接估计；当 `x>=1` 时，对 `integral_1^x sin(t)dt/t` 分部积分，边界项与 `integral_1^infinity dt/t^2` 的绝对值总和小于 `3`，再加 `|Si(1)|<=1`；负数由奇性处理。因此奇核贡献精确给出式 (15) 第一项，并至多为 `4/(pi d)`。

余项使用式 (2) 的第二个界，至多为 `2R_lambda/(pi d)`，得到式 (15)。保留有限和 `W_P(n,m)` 得到式 (16a)；再使用式 (5) 得到式 (16)。`□`

定义

`Ctilde_(lambda,n)=A_(lambda,n)`

` + [8+4R_lambda+4P_lambda]/pi`.                          (17)

### 定理 R（无对数平方尾）

若 `N>=max(1,2|n|)`，则

`sum_(|m|>N)|W_(n,m)|^2 <= 2Ctilde_(lambda,n)^2/N`.       (18)

#### 证明

对 `|m|>N>=2|n|` 有 `d>=|m|/2`。式 (10)、(16) 给出

`|W_(n,m)|<=Ctilde_(lambda,n)/|m|`。

最后使用 `sum_(m>N)m^(-2)<=integral_N^infinity x^(-2)dx=1/N`，并计入正负两个尾。`□`

所以真正的逐行速率是至少

`sum_(|m|>N)|W_(n,m)|^2=O_(lambda,n)(1/N)`,               (19)

不需要对数损失。`R_lambda` 只是固定紧区间上一个连续可积函数的绝对积分，可由 interval quadrature 严格包围。

对于实际证书，应优先使用式 (16a)，因为 `W_P(n,m)` 是一个有限、可用 directed rounding 直接计算的三角和。用 `P_lambda` 取绝对值会丢掉各素数幂之间的大量抵消；式 (16) 主要用于证明尾和收敛率。

## 6. 从单行尾到有限低频空间

令 `S` 是固定有限指标集，`U=span{V_n:n in S}`。若 `N>=2max_(n in S)|n|`，则矩形耦合算子满足

`||(1-P_N)A_lambda|U||^2`

`<=sum_(n in S)sum_(|m|>N)|W_(n,m)|^2`

`<=sum_(n in S) 2Ctilde_(lambda,n)^2/N`.                  (20)

第一步是 operator norm 不超过 Hilbert–Schmidt norm。式 (20) 因而严格证明：任何**固定有限低频核心**到远端 Fourier 尾的耦合以 `O(N^(-1/2))` 的速率趋于零。

若低频维数本身随 `N` 增长，不能直接把 (20) 的有限和视为统一常数；认证算法应使用“核心 + 有限 buffer + 远端尾”三层分解，buffer 纳入有限 interval matrix，只有固定核心与远端尾使用式 (20)。这避免把逐行收敛误当成无限维一致收敛。

## 7. 对存在性路线的意义

1. 文档 004 式 (3a) 中的无限矩阵尾现在有了无条件显式 majorant，且分离奇核后平方尾速率改进为 `O(1/N)`。
2. 该界虽很粗，却足以证明固定核心—远端尾耦合确实消失，而不仅是数值观察。
3. simple-even 认证剩余的无限维工作主要是：给 buffer+尾整体建立足够高的 form 下界，并控制 buffer 与远端尾的 Schur correction。
4. 由于目标只需某列 `lambda_j->infinity`，可为每个 `lambda_j` 自适应选择核心和 buffer；但要完成 RH 仍需对这些证书及 quasimode 速率给出随 `j` 的统一控制。

### `lambda=sqrt(13)` 的量级审计

用脚本对 `n=0,N=8` 检查：采样到 `|m|=30` 的实际平方尾约为 `0.04314`；定理 P 的原始闭式上界约为 `708.45`，定理 R 的无对数上界约为 `23.51`。去掉对数损失改善约三十倍，但仍远大于实际尾，更远大于 `10^(-20)` 量级的有限截面偶奇谱隙。

因此定理 R 的正确用途是证明远端耦合消失和支撑严格截断，不足以单独完成 simple-even 证书。要接近真实谱隙，必须使用式 (16a)、候选向量系数造成的行间抵消，或直接在 prolate/Weil 最低态适配的基中估计 residual；逐行绝对值 majorant 在定量上过于昂贵。

脚本还验证了小 Fourier 截面的最低向量并不稳定：`N=8` 的最低偶向量嵌入 `N=12` 后 residual 约 `8.74e-13`，而其 Rayleigh 值只有 `7.67e-23`，且大截面已有两个特征值位于它之下。这进一步支持把矩阵尾界用于严格控制，而把真正候选态固定为连续构造的 `k_lambda`，避免随 cutoff 追错谱支。

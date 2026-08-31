# 规范 trace-class Hodge defect 与最优有限秩 core

文档 018–028 通过 resonance wells、prolate modes 和调制多项式逐步构造
有限 core。本笔记说明这些 core 都在逼近同一个规范算子：完整 Weil
multiplier 负部的有限时间 Toeplitz 压缩。该算子正且 trace class；加上极点
负锚后，得到一个规范的紧 Hodge defect。其最高本征向量组成给定秩下最优
core，而显式 prolate/resonance cores 是它的可计算外逼近。

## 1. 完整 multiplier 的正负分解

对 zeta 固定 `lambda`，令

`h_lambda(t)=K_infinity(t)+G_lambda(t)-2P_lambda`,     (1)

并定义

`h_lambda^+(t)=max(h_lambda(t),0)`,

`W_lambda(t)=max(-h_lambda(t),0)`.                    (2)

因为 `K_infinity(t)->infinity`、`G_lambda>=0`，`W_lambda` 有紧支撑且可积。
完整 Weil form 是

`QW_lambda(f,f)=int h_lambda(t)|hat f(t)|^2dt/(2pi)`

`                    +2|C(f)|^2-2|S(f)|^2`.          (3)

在 `H_lambda=L^2([-ell,ell])` 上定义正 forms

`Pcan_lambda(f)=int h_lambda^+(t)|hat f(t)|^2dt/(2pi)`

`                       +2|C(f)|^2`,                 (4)

`Vcan_lambda(f)=int W_lambda(t)|hat f(t)|^2dt/(2pi)`

`                       +2|S(f)|^2`.                 (5)

### 引理 DM（canonical Toeplitz defect is trace class）

式 (5) 对应一个正 trace-class 算子 `Vcan_lambda`，且

`Tr Vcan_lambda`

`=ell/pi int_R W_lambda(t)dt+2||s||^2`,              (6)

其中 `S(f)=<f,s>`。式 (4) 是闭非负 form；对每个 `epsilon>0`，其算子
`Acan_lambda+epsilon I` 具有紧 resolvent。

#### 证明

负 multiplier 部分的算子是

`T_W=1_[-ell,ell] F^(-1)M_(W_lambda)F 1_[-ell,ell]`. (7)

写 `T_W=B^*B`，其中

`B=M_(sqrt(W_lambda))F1_[-ell,ell]`.                  (8)

`B` 的 kernel 平方积分为

`||B||_(HS)^2=(2ell)/(2pi)int W_lambda`

`                =ell/pi int W_lambda`.              (9)

故 `T_W` 正且 trace class，trace 等于式 (9)。rank-one 算子
`2|s><s|` 的 trace 是 `2||s||^2`，得到式 (6)。

`h_lambda^+>=0` 且最终等于趋于无穷的 `h_lambda`；加上有限秩正 form
`2|C|^2` 后仍闭。文档 022 引理 CG 的 Fourier-tail 证明给出紧 form 嵌入。
`□`

### 命题 DN（canonical compact-defect polarization）

有精确分解

`QW_lambda=Pcan_lambda-Vcan_lambda`.                  (10)

对 `epsilon>0` 定义

`Tcan_(lambda,epsilon)`

`=(Acan_lambda+epsilon I)^(-1/2)Vcan_lambda`

` (Acan_lambda+epsilon I)^(-1/2)`.                   (11)

则 `Tcan` 是正 trace-class 算子，而且

`QW_lambda>=-epsilon I`

`iff ||Tcan_(lambda,epsilon)||<=1`.                  (12)

#### 证明

式 (10) 由式 (2)–(5)。两个 inverse square-root 因子有界，trace-class ideal
在有界左右乘下保持 trace class。变量替换
`u=(Acan+epsilon I)^(1/2)f` 把
`QW+epsilon I` 化为 `<u,(I-Tcan)u>`，证明式 (12)。`□`

DN 与文档 022 的分解互补：那里 defect 是 scalar mass、正极化有紧
resolvent；这里 defect 本身 trace class，并由全部正负相消后的真实坏
multiplier 决定。

## 2. 广义 compact-defect 中心线结构

考虑任意完备 zeta/L 数据的相容过滤 `(H_t,q_t)`。假设每个截面已有

`q_t=p_t-v_t`,                                        (13)

其中 `p_t` 是闭非负 form，`v_t` 是正 trace-class form；并且有 Weil 型
正性判据。对 `epsilon>0` 定义式 (11) 的抽象版本 `T_(t,epsilon)`。

### 定理 DO（compact-defect Weil structure theorem）

若存在 cofinal `t_j`、正数 `epsilon_j->0`，使

`||T_(t_j,epsilon_j)||<=1`,                           (14)

则对应完备 zeta/L 函数的全部非平凡零点位于函数方程中心线。

#### 证明

命题 DN 的变量替换逐截面给出
`q_(t_j)>=-epsilon_jI`。文档 015 定理 AY 将其升级为全部固定 forms
非负，再应用 Weil 判据。`□`

有限域 Hodge--Riemann 情形的 negative primitive defect 是有限维的；DO
允许其数域对应物只是 trace-class，并只要求沿过滤渐近被正极化控制。

## 3. Canonical eigen-core 的最优性

把 `Vcan_lambda` 的本征值按

`nu_0>=nu_1>=...>=0`, `nu_n->0`                       (15)

排列，`Q_R^can` 为前 `R` 个本征向量张成的空间。

### 定理 DP（optimal compact-defect core）

有

`QW_lambda(f,f)>=-nu_R||f||^2`,

`f perpendicular Q_R^can`,                           (16)

并且

`nu_R=inf_(dim Q=R) sup_(f perpendicular Q,||f||=1)`

`                         Vcan_lambda(f,f)`.          (17)

此外

`nu_R<=Tr(Vcan_lambda)/(R+1)`.                        (18)

所有 `nu_n>0` 对应的 canonical eigenvectors 都属于
`Dom(Acan_lambda)`。

#### 证明

在 `Q_R^can` 的正交补上，正紧算子 `Vcan` 的范数为 `nu_R`；而
`Pcan>=0`，得到式 (16)。式 (17) 是正紧算子的 Courant--Fischer
min--max 原理。前 `R+1` 个本征值都至少为 `nu_R`，所以
`(R+1)nu_R<=Tr Vcan`，得到式 (18)。`□`

最后说明 domain。`W_lambda` 紧支撑，所以式 (7) 的 convolution kernel 在
有限位置区间上光滑。若 `nu_n>0`，则
`phi_n=nu_n^(-1)Vcan phi_n` 属于该光滑 range 加上 `sinh` rank-one range。
其零延拓 Fourier 尾至多为 `O(1/|t|)`；另一方面
`h_lambda^+(t)=O(log(2+|t|))`。因此
`h_lambda^+ hat phi_n in L^2`，即 `phi_n in Dom(Acan_lambda)`。

这说明对每个固定 `lambda`、任意目标误差，都无条件存在最小秩意义下最优
的有限 Hodge core。它不证明 core 内正性，也不给出随 `lambda` 可用的秩
增长率。

## 4. 显式 resonance core 是 canonical core 的外逼近

令 `Q` 是包含 `sinh` anchor 的任意显式 core。因为 `S(f)=0` 在 `Q^perp`
上，文档 028 定理 DJ 给出

`||(I-P_Q)Vcan_lambda(I-P_Q)||`

`<=Tr[(I-P_Q)Vcan_lambda(I-P_Q)]`

`<=eta_Q`,                                             (19)

其中 `eta_Q` 是 core-renormalized 加权 evaluation-density 积分。若
`dim Q=R`，定理 DP 还给出

`nu_R<=eta_Q`.                                        (20)

因此 prolate、调制多项式和 block large-sieve cores 的作用可以精确表述为：
不用求 canonical eigenfunctions，就构造一个有严格 `eta_Q` 上界的显式
近最优子空间。

## 5. Canonical core 的 cofinal Feshbach 终点

### 推论 DQ（canonical-core finite certificates imply RH）

若存在 `lambda_j->infinity`、正数 `eta_j->0`,`delta_j->0`，并选择
`R_j` 使 `nu_(R_j)<=eta_j`；再令 `Q_j=Q_(R_j)^can`。若 shifted operator

`B_j=QW_(lambda_j)+(eta_j+delta_j)I`                  (21)

的 core block `A_j` 与完整 residual Gram `R_j^res` 满足

`A_j-R_j^res/delta_j>=0`,                             (22)

则 RH 成立。

#### 证明

定理 DP 使 `B_j` 在 `Q_j^perp` 上至少为 `delta_jI`。文档 024 定理 CT 与
式 (22) 给出 `B_j>=0`，即
`QW_(lambda_j)>=-(eta_j+delta_j)I`。误差趋零后应用文档 015 定理 AY。`□`

DQ 是一个规范存在性终点：所有对象都由显式公式唯一确定，没有任意井覆盖
或 basis 选择。它仍未证明 RH，因为式 (22) 是 canonical core 内的全球
算术正性；而 canonical eigenfunctions 本身也尚无可用的统一显式描述。

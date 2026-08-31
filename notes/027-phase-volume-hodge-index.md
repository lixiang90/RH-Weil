# Phase-volume 低谱计数与中心 resonance 的测度障碍

文档 023 用调制多项式 core 控制坏频率 concentration。本笔记先研究一个
更简单的问题：仅知道坏集 Lebesgue 测度时，能控制多少正极化低谱？答案
是一个精确的 time--frequency trace 界。它给出 Hodge 负惯性数的显式上界，
但对 zeta 的中心 resonance，该上界存在严格大于 `1` 的渐近障碍；所以纯
测度路线不能替代 prolate/residual core。

## 1. Time--frequency trace 的低谱计数

令 `H=L^2([-ell,ell])`，函数零延拓到全线。设

`p(f)=int_R M(t)|hat f(t)|^2dt/(2pi)+r(f)`,            (1)

其中 `M>=0`、`M(t)->infinity`、`r>=0`，相应算子为 `A`。给定 `b>0`，令

`E_b={t:M(t)<b}`.                                     (2)

记低谱计数

`N_A(beta)=# {eigenvalues alpha_n(A)<beta}`.           (3)

### 定理 DE（phase-volume low-spectrum bound）

若 `0<=beta<b`，则

`N_A(beta)<= [ell |E_b|/pi]/[1-beta/b]`.              (4)

#### 证明

令 `K_E` 是先 Fourier 变换、限制到 `E_b`、再拉回有限时间区间的
concentration operator。其 kernel 对角值为 `|E_b|/(2pi)`，所以

`Tr K_E=(2ell)|E_b|/(2pi)=ell|E_b|/pi`.              (5)

取 `A` 的任一规范低谱本征向量 `phi_n`，`alpha_n<beta`。因为
`M>=b` 在 `E_b^c` 上且 `r>=0`，

`beta>p(phi_n)>=b[1-<phi_n,K_E phi_n>]`,              (6)

故

`<phi_n,K_E phi_n>>1-beta/b`.                         (7)

对全部 `alpha_n<beta` 求和。左侧不超过 `Tr K_E`，得到式 (4)。`□`

这是文档 023 定理 CM 的无 core、trace-class 对偶版本：CM 从一个给定
codimension core 推出谱隙；DE 从坏集的总 phase volume 限制低谱维数。

## 2. Hodge 负惯性数的测度界

对 entire unitary Euler 数据，文档 026 的 Weil form 是

`q_lambda=A_lambda-a_lambda I`.                       (8)

取 `Delta>0`、`b=a_lambda+Delta`，坏集为

`E_(lambda,Delta)`

`={t:K_infinity(t)-2Re F_lambda(t)<Delta}`.           (9)

### 推论 DF（phase-volume Hodge-index bound）

若 `0<epsilon<a_lambda`，则

`n_-(q_lambda+epsilon I)`

`<=ell |E_(lambda,Delta)|/pi`

`  *(a_lambda+Delta)/(Delta+epsilon)`.                (10)

对 zeta，右侧再加 `1` 即为有效上界。

#### 证明

entire scalar-defect 情形有

`n_-(q_lambda+epsilon I)=N_(A_lambda)(a_lambda-epsilon)`. (11)

把 `beta=a_lambda-epsilon`、`b=a_lambda+Delta` 代入定理 DE 得式 (10)。
zeta 还从 scalar threshold operator 减去一个奇极点 rank-one
`2|s><s|`；rank-one 扰动最多把负惯性增加 `1`。`□`

对 paired 非自对偶数据，可逐分量应用式 (10)；总负惯性上界是各分量之和。

### 推论 DG（phase-volume center-line criterion）

对文档 026 的 entire unitary Euler 数据，若存在 cofinal
`lambda_j->infinity`、正数 `epsilon_j->0` 和 `Delta_j>0`，使

`ell_j |E_(lambda_j,Delta_j)|/pi`

` *(a_(lambda_j)+Delta_j)/(Delta_j+epsilon_j)<1`,    (12)

则全部非平凡零点位于中心线。

#### 证明

式 (10) 的左侧是非负整数；式 (12) 迫使它为 `0`，所以
`q_(lambda_j)>=-epsilon_jI`。应用文档 026 定理 DC。`□`

DG 是一个只含坏集测度的严格 GRH 充分条件。下面证明它不能处理 zeta 的
中心井，也说明为什么文档 018 的密度界本身不够。

## 3. zeta 中心井的显式相干半宽

令 `x=lambda^2`，

`P(x)=sum_(k<=x)Lambda(k)/sqrt(k)`,                    (13)

`M_2(x)=sum_(k<=x)Lambda(k)(log k)^2/sqrt(k)`.         (14)

并记

`a_lambda=2P(x)-m_infinity`.                          (15)

文档 023 引理 CS 的正项级数还给出全局二次上界

`K_infinity(t)-m_infinity<=C_infinity t^2`,           (16)

`C_infinity=(1/8)zeta(3,1/4)`,                        (17)

其中右侧是 Hurwitz zeta。另一方面 `cos u>=1-u^2/2` 给出

`Re F_x(t)>=P(x)-t^2 M_2(x)/2`.                       (18)

### 定理 DH（central phase-volume obstruction）

对每个 `Delta>0`，zeta 的坏集式 (9) 包含中心区间

`[-r_(lambda,Delta),r_(lambda,Delta)]`,               (19)

其中

`r_(lambda,Delta)`

`=sqrt[(a_lambda+Delta)/(M_2(x)+C_infinity)]`.        (20)

进一步，若 `epsilon_lambda->0`，则对任意选择 `Delta_lambda>0`，

`liminf_(lambda->infinity)`

` {ell |E_(lambda,Delta_lambda)|/pi`

`  *(a_lambda+Delta_lambda)/(Delta_lambda+epsilon_lambda)}`

`>=3sqrt(6)/(2pi)>1`.                                 (21)

所以推论 DG 的纯 phase-volume 条件不可能用于证明 zeta RH。

#### 证明

引理 CS 的式 (32) 取 `y=t/2` 后，逐项以
`(n+1/4)^2+t^2/4>=(n+1/4)^2` 估计，得到式 (16)–(17)。由式 (18)，

`K_infinity(t)-2Re F_x(t)`

`<=-a_lambda+[M_2(x)+C_infinity]t^2`.                (22)

当 `|t|<r_(lambda,Delta)` 时右侧小于 `Delta`，得到式 (19)。

素数定理与分部求和给出

`P(x)=2sqrt(x)(1+o(1))`,                              (23)

`M_2(x)=2sqrt(x)(log x)^2(1+o(1))`.                  (24)

又 `ell=log lambda=(1/2)log x`。令

`c_lambda=Delta_lambda/a_lambda`,

`e_lambda=epsilon_lambda/a_lambda->0`.                (25)

由式 (19)–(24)，式 (21) 左侧括号中的量至少为

`sqrt(2)/pi * (1+c_lambda)^(3/2)/(c_lambda+e_lambda)`

` *[1+o(1)]`.                                         (26)

对 `c>0`，函数 `(1+c)^(3/2)/c` 在 `c=2` 取得最小值
`3sqrt(3)/2`。即使 `c_lambda` 趋向 `0` 或无穷，式 (26) 的下极限只会更大；
结合 `e_lambda->0` 得

`sqrt(2)/pi *3sqrt(3)/2=3sqrt(6)/(2pi)>1`.            (27)

这证明式 (21)。`□`

DH 是一个策略排除定理，不是 RH 的负面证据。它只说明：把所有危险 Fourier
质量压成坏集总测度再取 trace，必然丢失中心井内部的有限秩几何。文档 018
的 prolate removal、文档 021 的调制多项式 blocks 和文档 024 的 residual
Feshbach 正是保留这部分几何所必需的结构。

脚本回归给出 `C_infinity=8.08298374609606`、
`3sqrt(6)/(2pi)=1.16954520185051`；在 `lambda^2=13,Delta=1` 时，式 (20)
保证的中心半宽为 `0.755543525828178`。这些数值只检查闭式和不等式实现，
定理 DH 本身使用的是上述解析证明。

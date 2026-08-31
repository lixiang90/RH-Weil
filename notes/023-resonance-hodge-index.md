# Resonance concentration、正极化低谱与 Hodge 惯性指数

文档 021 控制坏频率井中的 Fourier concentration，文档 022 则把 Weil
正性写成紧 Hodge 算子特征值不越过 `1`。本笔记证明二者之间缺少的
min--max 桥梁：坏集 concentration 的有限余维上界会把正极化算子的低谱
排除到同一个有限 core 中，并给出 Weil form 负惯性指数的显式上界。

## 1. 从坏频率 concentration 到正极化谱隙

令 `H=L^2([-ell,ell])`，函数零延拓到全线。设闭非负 form

`p(f)=int_R M(t)|hat f(t)|^2dt/(2pi)+r(f)`,            (1)

其中 `M>=0`、`M(t)->infinity`，且 `r>=0`。记其自伴算子为 `A`，本征值按

`0<=alpha_1<=alpha_2<=...->infinity`                 (2)

排列并计重数。对阈值 `b>0` 定义

`E_b={t:M(t)<b}`.                                     (3)

### 定理 CM（concentration-to-polarization spectral gap）

设 `Q subset H` 是 `r_0` 维子空间，并且存在 `0<=chi<1`，使

`int_(E_b)|hat f(t)|^2dt/(2pi)<=chi||f||^2`           (4)

对所有 `f perpendicular Q` 成立。则

`p(f)>=b(1-chi)||f||^2`, `f perpendicular Q`,        (5)

以及

`alpha_(r_0+1)>=b(1-chi)`.                           (6)

#### 证明

在 `E_b^c` 上 `M>=b`，而在 `E_b` 上 `M>=0`。所以

`p(f)>=b int_(E_b^c)|hat f|^2/(2pi)`

`     >=b(1-chi)||f||^2`,                             (7)

得到式 (5)。若式 (6) 不成立，则 `A` 的前 `r_0+1` 个本征向量张成的空间
与 codimension `r_0` 的 `Q^perp` 有非零交；交中的向量 Rayleigh 商小于
`b(1-chi)`，与式 (5) 矛盾。`□`

定理 CM 不要求井数有限，也不要求 `Q` 由 `A` 的本征向量组成。任何能证明
式 (4) 的显式 time--frequency core 都能给出理想正极化低谱的计数上界。

## 2. zeta 的 near-resonance 低谱 core

对文档 022 的 zeta 正极化，令

`M_lambda(t)=K_infinity(t)-m_infinity+G_lambda(t)`,    (8)

`a_lambda=2P_lambda-m_infinity`,                      (9)

故 `Ptilde_lambda` 是式 (1)，其中
`r(f)=2|C(f)|^2>=0`。给定 `Delta>0`，取

`b_lambda=a_lambda+Delta`.                            (10)

由 `G_lambda=2P_lambda-2Re F_lambda`，相应坏集恰为

`E_(lambda,Delta)`

`={t:K_infinity(t)-2Re F_lambda(t)<Delta}`.           (11)

它不是任意定义的谱集：正是 archimedean kinetic 尚未把 prime-phase
coherence 压低到 scalar defect 以下 `Delta` 裕量的 near-resonance 集。

### 推论 CN（block large-sieve spectral exclusion）

若用文档 021 的调制多项式空间 `Q_(lambda,Delta)` 证明

`int_(E_(lambda,Delta))|hat f|^2dt/(2pi)`

`<=chi_(lambda,Delta)||f||^2`,

`f perpendicular Q_(lambda,Delta)`,                  (12)

则正极化算子满足

`alpha_(dim Q+1)(A_lambda)`

`>=(a_lambda+Delta)(1-chi_(lambda,Delta))`.           (13)

特别地，若

`chi_(lambda,Delta)<(Delta+epsilon)/(a_lambda+Delta)`, (14)

则在 `Q^perp` 上

`Ptilde_lambda(f)+epsilon||f||^2`

`   -a_lambda||f||^2>=gamma||f||^2`,                 (15)

其中

`gamma=Delta+epsilon`

`       -(a_lambda+Delta)chi_(lambda,Delta)>0`.       (16)

#### 证明

把式 (8)–(12) 代入定理 CM 得式 (13)。式 (5) 再减
`a_lambda||f||^2`、加 `epsilon||f||^2`，所得常数正是式 (16)。`□`

定理 CD 对 `delta`-分离、半宽 `c<=1` 的等宽井给出可取

`chi<=B(delta)e^2 4^R c^(2R+1)/[pi(2R+1)!]`.         (17)

若坏集分成有限个井族，就把各族式 (17) 相加。于是式 (14) 是一个完全
显式的 factorial inequality；它说明所需 core 秩由“井几何＋目标谱裕量”
决定，而不是由任意 Fourier cutoff 决定。

## 3. 紧 Hodge 越界数等于 Weil 负惯性

对 Hermitian form `h`，记 `n_-(h)` 为其最大负定子空间维数。固定
`lambda,epsilon>0`，沿用文档 022 的

`T=A_(lambda,epsilon)^(-1/2)V_lambda`

`                         A_(lambda,epsilon)^(-1/2)`. (18)

### 定理 CO（compact Hodge inertia correspondence）

有精确等式

`n_-(QW_lambda+epsilon I)`

`=# {eigenvalues of T_(lambda,epsilon) greater than 1}`, (19)

右侧计重数，且该数有限。

#### 证明

文档 022 式 (11) 给出 form-domain 到 `H_lambda` 的双射

`f mapsto u=A_(lambda,epsilon)^(1/2)f`，              (20)

并把 `QW_lambda+epsilon I` 变成 `I-T`。双射保持负定子空间的维数，所以
两侧负惯性相等。`T` 正紧，故其大于 `1` 的特征值只有有限多个；`I-T` 的
负谱子空间正由这些本征向量张成。`□`

这给出一个数域 Hodge index：有限域里 primitive polarization 排除错误
权重；这里每个固定截面的所有潜在错误中心线方向，恰对应显式紧 Hodge
算子越过阈值 `1` 的有限个本征方向。

## 4. Resonance Hodge-index bound

把推论 CN 的 core 再扩大一维以包含奇极点锚
`s(y)=sinh(y/2)`，记所得空间为 `Q'`。若 `f perpendicular Q'`，则
`S(f)=0`，所以式 (15)–(16) 给出

`QW_lambda(f,f)+epsilon||f||^2>=gamma||f||^2`.        (21)

### 推论 CP（explicit resonance Hodge-index bound）

在推论 CN 的假设及式 (14) 下，

`n_-(QW_lambda+epsilon I)<=dim Q'<=dim Q+1`.          (22)

等价地，`T_(lambda,epsilon)` 大于 `1` 的特征值至多有 `dim Q+1` 个。

#### 证明

任一维数大于 `dim Q'` 的子空间都与 `Q'^perp` 有非零交，而式 (21) 在该
交上严格为正，所以它不可能负定。这证明第一条；第二条由定理 CO。`□`

推论 CP 比“负谱离散”更强：它用 prime-resonance cover 的显式维数控制
全部 RH obstruction 的个数。它仍不排除 core 内存在一个越过 `1` 的方向。

## 5. 有限 core 的严格 Schur 终点

令 `h=QW_lambda+epsilon I`，并作
`H=Q' direct_sum Q'^perp`。假设除式 (21) 外，有限计算与尾估计给出

`h(u,u)>=mu||u||^2`, `u in Q'`,                       (23)

`|h(u,v)|<=beta||u||||v||`,

`u in Q', v in Q'^perp`.                             (24)

### 推论 CQ（resonance-core Schur certificate）

若

`mu>=0`, `gamma>0`, `beta^2<=mu gamma`,               (25)

则

`QW_lambda>=-epsilon I`.                              (26)

若沿 `lambda_j->infinity` 可取正数 `epsilon_j->0` 并逐个验证式
(12)、(14)、(23)–(25)，则 RH 成立。

#### 证明

写 `f=u+v`。式 (21)、(23)–(24) 给出

`h(f,f)>=mu||u||^2-2beta||u||||v||+gamma||v||^2`.    (27)

式 (25) 说明右侧二次型非负，得到式 (26)。沿 cofinal 序列应用文档 015
定理 AY 或文档 022 定理 CI 即得 RH。`□`

至此，统一存在性问题被压成四个可逐项审计的量：

1. near-resonance cover 的 `c,delta`；
2. block large-sieve concentration `chi`；
3. 有限 core 最低值 `mu`；
4. core--complement coupling `beta`。

前两项已有文档 018–021 的无条件估计；尚未证明的是沿 cofinal 截面让
`beta^2<=mu gamma` 且 `epsilon->0` 的联合算术裕量。

## 6. 反例的有限可探测性

### 推论 CR（finite detectability of a positivity failure）

若某固定截面存在 `f` 与 `delta>0` 使

`QW_lambda(f,f)<=-delta||f||^2`,                      (28)

则对任意 `0<epsilon<delta`，存在文档 022 定理 CJ 的某个有限 Galerkin
空间，使其最大广义特征值 `rho_n>1`。

#### 证明

式 (28) 给出 `n_-(QW_lambda+epsilon I)>=1`。定理 CO 因而给出
`||T_(lambda,epsilon)||>1`。定理 CJ 的 `rho_n` 单调趋于该范数，所以某个
有限 `n` 已满足 `rho_n>1`。`□`

因此 RH 若为假，其 Weil 正性失败原则上有有限广义特征值见证；证明 RH
之所以更难，是因为必须给出所有截面、全部未计算尾的一致上界。

脚本回归还对定理 CO 做了非平凡惯性测试：在 `lambda^2=13`、cutoff `3`
的 `7` 维 Hodge pencil 上人为增加 `0.101I` defect，并保留
`epsilon=0.1`。此时 `QW+epsilon I` 恰有 `5` 个负特征值，而广义 Hodge
谱也恰有 `5` 个特征值大于 `1`。该扰动只用于检查 Sylvester 惯性实现，
不是对真实 zeta form 的修改或证据。

## 7. Archimedean 谱底的精确闭式

Riemann--Siegel 相位的导数为

`K_infinity(t)=1/2 Re psi(1/4+it/2)-1/2 log pi`,      (29)

其中 `psi=Gamma'/Gamma`。

### 引理 CS（exact archimedean spectral bottom）

对所有实数 `t`，

`K_infinity(t)>=K_infinity(0)=m_infinity`,            (30)

且

`m_infinity`

`=-gamma/2-pi/4-(3/2)log 2-(1/2)log pi`.             (31)

等号只在 `t=0` 取得。

#### 证明

对 `a>0`，digamma 的绝对收敛差分级数给出

`Re psi(a+iy)-psi(a)`

`=sum_(n=0)^infinity [1/(n+a)`

` -(n+a)/((n+a)^2+y^2)]`

`=sum_(n=0)^infinity y^2`

` /[(n+a)((n+a)^2+y^2)]>=0`.                         (32)

当 `y!=0` 时每项严格为正。取 `a=1/4,y=t/2` 得式 (30)。最后，digamma
反射与倍乘公式给出

`psi(3/4)-psi(1/4)=pi`,

`psi(1/4)+psi(3/4)=2psi(1/2)-2log2`

`                         =-2gamma-6log2`.            (33)

联立即得

`psi(1/4)=-gamma-pi/2-3log 2`                         (34)

代入式 (29)，得到式 (31)。`□`

因此文档 016–023 中的平移常数 `m_infinity` 不再需要数值搜索或保守猜测；
它是显式公式数据的一部分。脚本现用式 (31) 作为 Hodge 分解的默认移位。

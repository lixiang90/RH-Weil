# Tempered Gamma--Euler 数据的广义紧 Hodge 定理

文档 025 的 Dirichlet 结构有两个本质特征：有限处 Euler 参数在单位圆上，
无穷处 Gamma multiplier 有显式下界。本笔记把这两点抽成固定 degree 的
tempered Gamma--Euler 数据，并证明只要完备 L 函数 entire，全球 defect
仍是 scalar mass。于是广义中心线条件再次变成一个正极化最低本征值问题。

这不是在假设零点位于中心线；`tempered` 只约束局部 Satake/Gamma 数据。
最后仍需一个同时耦合全部 primes 的全球 Hodge 下界。

## 1. 多个 shifted Gamma 因子的共同下界

记

`Gamma_R(s)=pi^(-s/2)Gamma(s/2)`.                     (1)

考虑中心为 `1/2`、analytic conductor 数据为 `N` 的 archimedean 因子

`N^(s/2) product_(j=1)^d Gamma_R(s+sigma_j+i nu_j)`, (2)

其中 `sigma_j,nu_j in R`，并要求
`a_j=1/4+sigma_j/2>0`。中心线上对应 multiplier 为

`K_infinity(t)=1/2 log N`

` +1/2 sum_(j=1)^d [Re psi(a_j+i(t+nu_j)/2)-log pi]`, (3)

`a_j=1/4+sigma_j/2`.                                  (4)

### 引理 DA（tempered Gamma lower bound）

对全部实数 `t`，

`K_infinity(t)>=m_Gamma`,                             (5)

其中显式常数

`m_Gamma=1/2 log N`

` +1/2 sum_(j=1)^d[psi(a_j)-log pi]`.                (6)

若全部 `nu_j` 相等，则式 (5) 的下界在共同点 `t=-nu_j` 精确取得；若它们
不全相等，则式 (5) 对每个 `t` 都严格。

#### 证明

文档 023 引理 CS 对任意 `a>0,y in R` 证明

`Re psi(a+iy)>=psi(a)`,                               (7)

且仅当 `y=0` 取等。逐项取
`a=a_j,y=(t+nu_j)/2` 并求和，得到式 (5)–(6)。所有项同时取等当且仅当
`t=-nu_j` 对全部 `j` 成立。`□`

重要的是，`m_Gamma` 不必等于真实谱底；任何已证明的共同下界都足以做
正极化平移。不同 spectral shifts 只可能让真实 kinetic 更强。当
`sigma_j in {0,1}` 时，文档 025 式 (6) 又把式 (6) 化成引理 CW 的初等
闭式；一般 discrete-series 实移位则保留显式 digamma 值。

## 2. 固定 degree 的单位 Euler 图

设每个纳入显式公式的 prime power `p^m` 有非负权

`b_(p,m)=log p/p^(m/2)`,                              (8)

并且 normalized coefficient 有有限纯相位展开

`a(p^m)=sum_(r=1)^(d_p) u_(p,r)^m`,

`|u_(p,r)|=1`, `0<=d_p<=d`.                           (9)

零参数直接省略。固定 cutoff `p^m<=lambda^2`，定义 edge mass

`M_lambda=sum_(p^m<=lambda^2)b_(p,m)d_p`.             (10)

若对象非自对偶，就与 contragredient 配对。对每个相位应用文档 017 引理
BI，得到非负 graph multiplier

`G_lambda(t)=2M_lambda-2Re F_lambda(t)>=0`,           (11)

`F_lambda(t)=sum_(p,m,r)b_(p,m)u_(p,r)^m`

`                              exp(itm log p)`.       (12)

假设完备 L 函数 entire，因而没有 pole anchors。令

`Pcal_lambda(f)=int [K_infinity(t)-m_Gamma+G_lambda(t)]`

`                         |hat f(t)|^2dt/(2pi)`,      (13)

`Vcal_lambda(f)=a_lambda||f||^2`,                    (14)

`a_lambda=2M_lambda-m_Gamma`.                         (15)

只考虑 `a_lambda>=0` 的充分大截面；固定 degree 且除有限 primes 外
`d_p=d` 时，`M_lambda=2d lambda+o(lambda)`，所以这不限制 cofinal 性。

### 命题 DB（entire unitary Euler compact polarization）

paired Weil form 有精确分解

`q_lambda=Pcal_lambda-Vcal_lambda`,                   (16)

其中两项非负，且 `Pcal_lambda+epsilon I` 对每个 `epsilon>0` 具有紧
resolvent。

#### 证明

式 (9) 使每个 local term 都由酉 translation identity 精确完成平方；求和
产生式 (11) 及 scalar `2M_lambda`。引理 DA 使
`K_infinity-m_Gamma>=0`。entire 假设排除极点负锚，故得到式 (13)–(16)。
最后 `K_infinity(t)->infinity`，文档 022 引理 CG 的 Fourier-tail 紧嵌入
证明原样适用。`□`

## 3. 广义最低谱中心线定理

令 `A_lambda` 是式 (13) 的正自伴算子，最低本征值为 `alpha_1(lambda)`。
紧 Hodge 算子简化为

`T_(lambda,epsilon)=a_lambda(A_lambda+epsilon I)^(-1)`. (17)

### 定理 DC（tempered Gamma--Euler center-line criterion）

假设该完备 L 数据具有相容 cofinal 显式公式过滤和 paired Weil 正性判据。
若存在 `lambda_j->infinity`、正数 `epsilon_j->0`，使

`alpha_1(lambda_j)>=a_(lambda_j)-epsilon_j`,          (18)

则全部非平凡零点位于 `Re(s)=1/2`。

#### 证明

由式 (17)，式 (18) 等价于
`||T_(lambda_j,epsilon_j)||<=1`。文档 022 定理 CI 于是给出全部固定 Weil
forms 非负，再应用假设的 paired Weil 判据。`□`

DC 是文档 017 定理 BL 在“entire＋所有 local roots 酉＋tempered Gamma
shifts”情况下的紧谱版本。有限域中局部纯性最终由几何极化给出；数域中
式 (9) 只完成局部平方，式 (18) 才是尚缺的全球 Hodge--Riemann 输入。

## 4. Resonance/Feshbach 有限版本

给定 `Delta>0`，正极化 symbol 低于 `a_lambda+Delta` 的集合仍精确化为

`E_(lambda,Delta)`

`={t:K_infinity(t)-2Re F_lambda(t)<Delta}`.           (19)

若调制多项式 core `Q_lambda` 在该集合上的 concentration 至多 `chi_lambda`
且

`chi_lambda<(Delta+epsilon)/(a_lambda+Delta)`,        (20)

则文档 023 定理 CM 给出 threshold operator

`B_lambda=A_lambda+(epsilon-a_lambda)I`               (21)

在 `Q_lambda^perp` 上的谱隙

`gamma_lambda=Delta+epsilon`

` -(a_lambda+Delta)chi_lambda>0`.                    (22)

### 推论 DD（finite tempered-Euler Hodge certificates）

若沿 cofinal `lambda_j`、正数 `epsilon_j->0`，式 (20) 成立，并且 core
block `A_j`、完整 residual Gram `R_j` 满足严格 enclosure

`A_j-R_j/gamma_j>=0`,                                 (23)

则对应 L 数据的全部非平凡零点位于中心线。

#### 证明

文档 024 定理 CT 用式 (22)–(23) 给出 `B_(lambda_j)>=0`，即
`q_(lambda_j)>=-epsilon_jI`；再应用定理 DC。`□`

## 5. 特定 automorphic 问题的存在性边界

1. **Primitive Dirichlet L 函数。** `d=1`，有限处单位相位和无穷处
   `kappa` 数据无条件成立；文档 025 是 DB–DD 的精确 degree-one 实例。
2. **归一化 holomorphic cuspidal newforms。** 在未分歧 primes，Deligne
   的 Ramanujan 定理使两个 normalized Satake roots 位于单位圆；标准 L
   函数 entire，Gamma 因子显式。因此去掉/单独完成有限 ramified local
   corrections 后，局部平方、Gamma 下界与紧性无条件存在。尚无的是式
   (18)/(23) 的全球统一下界。
3. **Maass forms 与一般 GL(d) cuspidal 数据。** 若假设所有相关 normalized
   local roots tempered，则 DB–DD 适用；一般情形这一 local temperedness
   本身包含尚未证明的 Ramanujan 型问题。即使局部 temperedness 已知，仍
   不能推出全球式 (18)。
4. **有极点的 L 数据。** 必须像 zeta 一样把有限秩正负 pole anchors 加回；
   此时使用文档 022 的一般紧 Hodge 算子和 rank-one/finite-rank resolvent，
   不能直接使用 scalar 公式 (17)。

有限 ramified corrections 若不能写成单位相位平方，可作为显式有界
Hermitian operator 取正负部分并分别加入 `Pcal,Vcal`；紧性仍保持，但
defect 不再纯 scalar，中心线条件应退回定理 CI 的一般范数判据。

所以当前结构已覆盖一个相当广的代数/解析类别，但没有把 Ramanujan 或
全球 Hodge positivity 偷放进定义：前者是局部存在性输入，后者正是 GRH
强度的剩余障碍。

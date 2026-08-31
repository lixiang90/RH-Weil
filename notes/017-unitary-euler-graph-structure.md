# 酉 Euler 图极化与广义中心线结构定理

文档 016 在有限区间上把素数 partial translations 写成图 Dirichlet 能量减
degree 势。本笔记改用零延拓后的全线平移。优点是平移严格酉，且局部
Frobenius/Satake 相位可以直接并入平移；于是“局部纯性”被翻译成一个精确
的 twisted graph 平方。这样可同时覆盖 Riemann zeta、Dirichlet L 函数以及
具有 tempered Euler 参数的更一般 L 数据。

## 1. 酉扭曲平移的平方恒等式

令 `H=L^2(R,V)`，其中 `V` 是 Hilbert 空间。记

`(tau_a f)(y)=f(y+a)`.                                 (1)

若 `U` 是 `V` 上的酉算子，则 `U tau_a` 在 `H` 上酉。

### 引理 BI（unitary Euler edge identity）

对每个 `f in H`，

`-2Re<f,U tau_a f>`

`=||f-U tau_a f||^2-2||f||^2`.                         (2)

#### 证明

展开平方，并使用 `||U tau_a f||=||f||`。`□`

若 `f` 原先只定义在有限区间，则先零延拓；式 (2) 的内积自动只在两个支撑
的重叠区间积分。因此它与文档 016 的 partial graph 恒等式完全等价，只是
把边界 degree 质量吸收到常数 `2||f||^2` 中。

## 2. zeta 的 Fourier–prime graph multiplier

对 zeta 令

`w_k=Lambda(k)/sqrt(k)`, `a_k=log k`,

`P_lambda=sum_(2<=k<=lambda^2)w_k`.                    (3)

引理 BI 求和得到

`-W_P(f,f)=sum_k w_k||f-tau_(a_k)f||^2`

`             -2P_lambda||f||^2`.                      (4)

取全线 Fourier 变换后，正图能量的 multiplier 为

`G_lambda(t)=4sum_(k<=lambda^2)w_k sin^2(t log(k)/2)>=0`, (5)

所以

`-W_P(f,f)=int_R G_lambda(t)|hat f(t)|^2 dt/(2pi)`

`             -2P_lambda||f||^2`.                      (6)

脚本函数 `prime_graph_symbol` 计算式 (5)，回归测试检查
`0<=G_lambda(t)<=4P_lambda` 及 `G_lambda(0)=0`。

令 `K_infinity`、`m_infinity`、`C`、`S` 沿用文档 016。定义

`Ptilde_lambda(f)=<(K_infinity-m_infinity)f,f>`

` +int G_lambda(t)|hat f(t)|^2dt/(2pi)+2|C(f)|^2`,     (7)

`Vtilde_lambda(f)=(2P_lambda-m_infinity)||f||^2`

` +2|S(f)|^2`.                                        (8)

### 命题 BJ（Fourier–Euler 极化恒等式）

`Ptilde_lambda>=0`，且

`QW_lambda(f,f)=Ptilde_lambda(f)-Vtilde_lambda(f)`.     (9)

#### 证明

式 (7) 各项非负。将式 (6) 与极点恒等式
`Q_(0,2)=2|C|^2-2|S|^2` 代入，并消去 `m_infinity||f||^2`。`□`

文档 016 的 degree representation 适合位置空间 localization；式 (9) 适合
频率空间/Diophantine 分析。两者是同一素数图 Laplacian 的两种完成平方。

由命题 BJ，定理 BG 等价于证明

`(2P_lambda-m_infinity)||f||^2+2|S(f)|^2`

`<=<(K_infinity-m_infinity)f,f>`

`  +int G_lambda|hat f|^2/(2pi)+2|C(f)|^2`

`  +epsilon_lambda||f||^2`,                            (10)

其中 `epsilon_lambda->0`。式 (10) 清楚展示三个频率区间：

- `t` 很大时由 `K_infinity(t)~(1/2)log|t|` 控制；
- 一般 `t` 由许多素数相位的 `G_lambda(t)` 控制；
- `t` 靠近共同 resonance、特别是 `t=0` 时，必须由时间限制不确定性及极点
  锚 `C,S` 控制。

## 3. 抽象酉 Euler–Weil 结构

考虑一个完备 zeta/L 函数 `Lambda(s)`，函数方程中心为 `c/2`。设其 prime
power 显式公式系数可写成有限个纯相位之和

`a(p^m)=sum_(r=1)^d u_(p,r)^m`, `|u_(p,r)|=1`,         (11)

允许在 ramified primes 删除或单独处理有限项。式 (11) 等价于 normalized
local Frobenius/Satake matrix 的特征值位于单位圆；它是局部纯性/temperedness
的 Hilbert 空间表达。

在测试函数过滤 `H_T` 上，假设显式公式 Hermitian form 具有

`q_T(f,f)=<K_Tf,f>`

` -2sum_(p^m in E_T) b_(p,m) Re[a(p^m)C_(m log p)(f)]`

` +||B_T^+f||^2-||B_T^-f||^2`,                         (12)

其中 `b_(p,m)>=0`，`K_T>=m_T`，`C_a(f)=<f,tau_a f>`，
而 `B_T^+`,`B_T^-` 编码极点、Gamma 因子中有限秩的正负锚。

对式 (11) 的每个相位应用引理 BI。令

`M_T=sum_(p^m in E_T)b_(p,m)d`,                        (13)

`mathcal P_T(f)=<(K_T-m_T)f,f>`

` +sum_(p,m,r)b_(p,m)||f-u_(p,r)^m tau_(m log p)f||^2`

` +||B_T^+f||^2`,                                     (14)

`mathcal V_T(f)=(2M_T-m_T)||f||^2+||B_T^-f||^2`.       (15)

则 `mathcal P_T>=0` 且 `q_T=mathcal P_T-mathcal V_T`。

### 定义 BK（酉 Euler–Weil 渐近极化结构）

称上述数据具有酉 Euler–Weil 渐近极化，如果：

1. `(H_T,q_T)` 是相容、cofinal 穷尽的过滤；
2. 局部系数满足式 (11)，并且式 (12) 是已证明的显式公式；
3. 存在 cofinal `T_j` 与 `epsilon_j->0`，使

   `mathcal V_(T_j)(f)<=mathcal P_(T_j)(f)`

   `                         +epsilon_j||f||^2`;       (16)

4. 已建立 Weil 型判据：全部 `q_T>=0` 等价于 `Lambda` 的非平凡零点位于
   `Re(s)=c/2`。

### 定理 BL（酉 Euler–Weil 中心线结构定理）

具有定义 BK 结构的 `Lambda` 的全部非平凡零点位于中心线
`Re(s)=c/2`。

#### 证明

引理 BI 给出 `q_(T_j)=mathcal P_(T_j)-mathcal V_(T_j)`。式 (16) 因而给出

`q_(T_j)(f,f)>=-epsilon_j||f||^2`.                     (17)

文档 015 的过滤渐近正性定理 AY 把它升级为全部固定 `q_T>=0`，再应用
定义 BK 的第 4 项。`□`

BL 是一个足够广泛、又比“假设存在自伴零点算子”具体的结构定理：局部
Frobenius 数据必须真正给出酉 twisted edges，全球只剩一个明确的
Hodge–Riemann domination (16)。

## 4. 特定 L 函数的存在性审计

### 命题 BM（局部酉图结构的已知实例）

1. **Riemann zeta。** `d=1,u_p=1`，定义 BK 的 1–2 项由经典显式公式和
   命题 BJ 无条件成立；第 4 项是 Weil 判据。唯一未证核心是式 (16)。
2. **primitive Dirichlet L 函数。** 对 `p` 不整除 conductor，
   `u_p=chi(p)` 且 `|u_p|=1`；ramified primes 的 Euler 因子缺失。因此
   χ 与 `bar chi` 配对后的局部 twisted graph 平方无条件存在。全球
   domination (16) 仍等价强度地触及 GRH，本文尚未证明。
3. **tempered automorphic Euler 数据。** 若 normalized Satake 参数
   `u_(p,r)` 全部在单位圆，则式 (11) 成立，故局部平方分解成立。对一般
   automorphic 表示，这一 temperedness 本身可能是未证的 Ramanujan 型输入；
   即使已知，仍不能替代全球式 (16)。
4. **有限域 Weil 情形。** Hodge–Riemann 极化与 Frobenius–Lefschetz
   adjoint relation 使归一化 Frobenius 在 primitive 部分酉，并给出
   `epsilon=0` 的精确 domination；这与文档 001 的有限维定理是同一机制。

#### 证明

前三项把相应 Euler 参数代入引理 BI；第四项由文档 001 的极化
Lefschetz–Frobenius 结构定理。`□`

命题 BM 精确区分了两层存在性：

- 局部纯性提供每条 Euler edge 的正平方；
- 全球 Hodge–Riemann domination 同时耦合所有 primes、Gamma 因子和支撑
  截断，才迫使解析延拓后的零点位于中心线。

这也解释了为什么“所有局部因子都纯”不能单独证明 GRH。

## 5. 下一分析目标：resonance 集的三段估计

对 zeta，令

`R_lambda(delta)={t:G_lambda(t)<2P_lambda-delta}`.     (18)

若能选择 `delta_lambda` 使：

1. 在 `R_lambda(delta_lambda)^c` 上，prime graph multiplier 已提供式 (10)
   所需的大部分 `2P_lambda`；
2. 在 `R_lambda` 的大 `|t|` 部分，archimedean `log|t|` 补足缺口；
3. 在剩余低频小测度部分，时间限制的 prolate concentration 与 `C,S` 锚
   给出严格有限秩控制；

并使总损失为 `o(1)`，就得到定义 BK 的式 (16)。这把下一步从笼统的
“证明正性”变成 prime-phase resonance 集的测度/Diophantine 估计加一个
有限维 prolate 证书。文档 018 已证明第一层全局密度界：固定比例强
resonance 的相对测度是 `O(log^2(lambda)/lambda^2)`；剩余缺口是把
Lebesgue 密度升级为对所有 time-limited `|hat f|^2` 成立的大筛不等式。
文档 018 的定理 BT 已单独解决不可避免的 `t=0` resonance 井：其
time–bandwidth product 保持常数，剥离缓慢增长的有限 prolate core 后，
正交补在该井中的 Fourier 质量一致趋零。剩余问题是所有非零 resonance
井的可求和控制。

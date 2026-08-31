# Ihara--Bass companion Frobenius 与 Ramanujan Hodge 结构

本节给出一个真正闭合的存在性实例：对有限正则图，zeta、Frobenius、
极化恒等式与 Hodge 惯性都能从邻接代数直接构造。它既验证文档 073 的
tempered 广义结构确实覆盖边界 Jordan 情形，也清楚区分“构造结构”与
“证明结构正定”。

以下固定 `q>1`。所有空间有限维，`A=A*`。

## 1. 二次 Hecke--Weil package

令 `V` 为有限维 Hilbert 空间，`A in End(V)` 自伴。定义

`F_A = [[A,-qI],[I,0]]` on `V direct_sum V`,             (1)

`D_A(u)=det(I-uA+qu^2I)`.                               (2)

若 `lambda` 是 `A` 的特征值，则 `F_A` 在对应二维块上的特征多项式为

`x^2-lambda x+q`.                                       (3)

因此两根乘积为 `q`，这就是有限图版本的 reciprocal Frobenius pairing。

### 定理 OH（quadratic companion Weil theorem）

有精确恒等式

`det(I-uF_A)=D_A(u)`.                                   (4)

此外，令 `u=q^(-s)`。式 (2) 对应 `lambda` 的两个零点都位于
`|u|=q^(-1/2)`，等价于

`|lambda|<=2sqrt(q)`,                                   (5)

也等价于对应 `s` 的实部为 `1/2`。

#### 证明

对 `I-uF_A=[[I-uA,uqI],[-uI,I]]` 对右下单位块取 Schur determinant，
得到式 (4)。式 (3) 的根记作 `alpha,beta`。若
`|lambda|<2sqrt(q)`，二根互为共轭且乘积为 `q`，故模均为 `sqrt(q)`；
等号时为重根 `+/-sqrt(q)`。反之若两根模均为 `sqrt(q)` 且和
`lambda` 为实数，则 `|lambda|<=2sqrt(q)`。`u=alpha^(-1)` 给最后结论。
`□`

这个定理已是一个较广的代数结构定理：输入不是图，而只是一个自伴 Hecke
算子 `A` 和二次 reciprocal polynomial。图只负责自然地产生这些数据。

## 2. 显式 Hodge form

定义自伴型

`H_A=[[I,-A/2],[-A/2,qI]]`.                             (6)

### 定理 OI（exact similitude and Hodge inertia）

对任意自伴 `A`，不作任何 Ramanujan 假设，就有

`F_A^* H_A F_A=qH_A`.                                   (7)

若 `n_<(A),n_=(A),n_>(A)` 分别按重数计数满足

`|lambda|<2sqrt(q), |lambda|=2sqrt(q), |lambda|>2sqrt(q)`

的邻接特征值，则

`inertia(H_A)=(2n_<+n_=, n_>, n_=)`,                   (8)

其中顺序是 `(positive,negative,null)`。

#### 证明

直接 block multiplication 给式 (7)。由谱定理，只需在每个 `lambda` 块
考察

`H_lambda=[[1,-lambda/2],[-lambda/2,q]]`,

其 trace 为 `1+q>0`，determinant 为

`q-lambda^2/4`.                                         (9)

于是区间内给两个正方向，边界给一正一零，区间外给一正一负，求和即得
式 (8)。`□`

这是一条完全显式的有限 Hodge index theorem：错误 weight 不只是使正性
失败，而是逐重数产生一个负方向；临界边界逐重数产生一个 radical 方向。

### 推论 OJ（strict purity 等价于正极化存在）

以下等价：

1. `spec(A)` 严格包含于 `(-2sqrt(q),2sqrt(q))`；
2. 式 (6) 是正定的 exact polarization；
3. 存在某个正定 `K` 满足 `F_A^*KF_A=qK`。

#### 证明

`1 => 2` 来自式 (9)，`2 => 3` 显然。若 3 成立，`q^(-1/2)F_A` 在
`K` 内积下酉，因而可对角化且谱在单位圆。区间外根的模不对；边界块
`[[+/-2sqrt(q),-q],[1,0]]` 有非平凡二阶 Jordan 块，也不可能酉化。
故只能有严格不等式。`□`

边界 Jordan 块说明：若把“极化”只定义为 exact positive similitude，就会
错误排除合法的临界重根。文档 073 的 tempered 放宽正是必要的。

## 3. Tempered 结构恰好恢复闭 Ramanujan 界

令 `U_A=q^(-1/2)F_A`。

### 定理 OK（tempered quadratic Weil structure）

以下等价：

1. `spec(A) subset [-2sqrt(q),2sqrt(q)]`；
2. `U_A` 的正反 powers 双向 subexponential；
3. 实际上 `||U_A^n||+||U_A^(-n)||=O(1+|n|)`；
4. `D_A(q^(-s))` 的全部零点位于 `Re(s)=1/2`。

#### 证明

区间内部的二维块可对角化且 eigenvalues 在单位圆；边界块为大小二的
unit-circle Jordan block，所以正反 powers 至多线性增长。这给 `1=>3=>2`。
若有区间外 `lambda`，式 (3) 有一个 normalized root 模大于一，正向或反向
orbit 指数增长，否定 2。`1<=>4` 是定理 OH。`□`

所以 exact positive polarization 对应 strict purity，而 two-sided tempered
polarization 精确对应含边界的通常 purity。这里不是术语修补，而是由 zeta
允许重临界根强迫的结构分层。

## 4. 有限正则图的完整存在性

令 `X` 为有限连通 `(q+1)`-正则无向图，顶点数 `n`、边数 `m`，邻接算子
为 `A_X`。Bass--Ihara determinant formula 为

`Z_X(u)^(-1)=(1-u^2)^(m-n) det(I-uA_X+qu^2I)`.          (10)

常值向量给 trivial eigenvalue `q+1`；若图二分，另有 `-(q+1)`。令 `V_0`
为这些 trivial eigenspaces 的正交补，并把上述结构限制到
`V_0 direct_sum V_0`。

### 定理 OL（Ihara RH = Ramanujan = tempered Weil）

对 `X`，以下等价：

1. `X` 是 Ramanujan，即每个 nontrivial `lambda` 满足
   `|lambda|<=2sqrt(q)`；
2. Ihara zeta 的全部 nontrivial poles 位于 `|u|=q^(-1/2)`；
3. 写 `u=q^(-s)` 后，它们位于 `Re(s)=1/2`；
4. nontrivial companion Frobenius `q^(-1/2)F_(A_X|V_0)` 双向 tempered；
5. 显式 Hodge form (6) 在 nontrivial 部分没有负方向。

而且其负惯性恰等于违反 Ramanujan 界的 nontrivial adjacency eigenvalues
总重数，nullity 恰等于落在边界的总重数。

#### 证明

式 (10) 中 `(1-u^2)^(m-n)`、`lambda=+/-(q+1)` 所给因子是 trivial
部分。对剩余每个 eigenvalue 逐一应用定理 OH、OI、OK 即得。`□`

### 命题 OM（结构存在性已经实现）

对每个有限正则图，以下对象都由有限组合数据无条件给出：

- Euler product `Z_X`（primitive non-backtracking cycles）；
- self-adjoint Hecke operator `A_X`；
- companion Frobenius `F_A` 与 trace determinant (4)；
- reciprocal pairing；
- exact、但可能不定或退化的 Hodge form (6)；
- 精确 Hodge inertia formula (8)。

额外需要证明的只有 Hodge nonnegativity；它与该图的 Ramanujan/RH 命题
完全等价。另一方面，这种正结构不是空类：LPS 给出显式 Ramanujan 图族，
Marcus--Spielman--Srivastava 更证明每个 degree `>2` 都有无限二分
Ramanujan 图族。故对这些具体 zeta，所需 tempered Weil 结构确实存在。

## 5. 对经典 RH 路线的审计

### 结论 ON（可迁移结构与不可偷渡之处）

本模型把 Weil 机制压缩成四个可迁移部件：

1. prime/closed-orbit Euler product；
2. 自伴 Hecke operator `A`；
3. reciprocal companion `F` 与 determinant trace formula；
4. 一个由 `A` 直接写出的 Hodge form，其 nonnegativity 等价于正确谱界。

对有限图，四项全部无条件构造，且 positivity 可由独立的组合/表示论方法
证明。对 Riemann zeta，本仓库前面各节已分别构造 prime Euler current、
filtered determinant carriers 与正 Gram forms，但还没有一个不使用零点位置的
单一自伴 `A`，使其 companion determinant 精确等于 completed zeta，并使
Ramanujan 型谱界能由独立几何定理证明。

因此有限图例子证明了“广义结构定理”并非循环定义，也证明了这套结构在一大
类真正的 zeta 问题上存在；但把 `A_X` 替换成 `Spec Z` 的 canonical Hecke
operator，仍是原版 RH 的核心存在性障碍，而不是本节已经解决的结论。

## 6. 可复核计算

`scripts/qw_matrix.py` 新增：

- `ihara_frobenius_operator`；
- `ihara_hodge_metric`；
- `ihara_bass_matrix`。

回归测试核对 `K_4` 的 determinant/similitude 恒等式，并用同时含区间内、
边界、区间外特征值的对角模型核对负惯性和 nullity。数值测试只检查实现，
定理证明是上面的有限维代数恒等式。

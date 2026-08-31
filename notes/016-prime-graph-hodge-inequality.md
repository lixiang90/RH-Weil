# 素数图平方分解与算术 Hodge–Riemann 不等式

文档 015 把经典 RH 的一个足够条件降为

`QW_lambda>=-epsilon_lambda I`, `epsilon_lambda->0`.     (1)

本笔记继续拆解式 (1) 的代数内容。有限素数项不是任意有界扰动：它是对数
区间上一族 partial translations 的加权邻接算子。每个负邻接项都能精确
完成平方，变成正的图 Dirichlet 能量减去显式度数势。这给出一个真正的
“正极化减去 primitive defect”结构，也证明了逐项取绝对值为何原则上不可能
完成文档 015 的 `o(1)` 目标。

## 1. 素数平移的精确图能量

写 `ell=log(lambda)`、`L=2ell`，在中心化坐标

`H_lambda=L^2([-ell,ell],dy)`                           (2)

中把函数延拓为区间外零。对 `0<a<=L` 定义

`C_a(f)=int_(-ell)^(ell-a) conjugate(f(y))f(y+a)dy`,   (3)

`E_a(f)=int_(-ell)^(ell-a)|f(y+a)-f(y)|^2dy`.          (4)

再令

`d_a(y)=1_[-ell,ell-a](y)+1_[-ell+a,ell](y)`.          (5)

### 引理 BC（partial translation 完成平方）

对每个 `f in H_lambda`，

`-2Re C_a(f)=E_a(f)-int_(-ell)^ell d_a(y)|f(y)|^2dy`. (6)

#### 证明

展开式 (4)：

`E_a=int_(-ell)^(ell-a)(|f(y+a)|^2+|f(y)|^2)dy`

`    -2Re C_a(f)`.                                    (7)

第一行的两个平方积分分别在 `[-ell+a,ell]` 与 `[-ell,ell-a]` 上，
其和正是式 (5) 的度数积分。移项即得。`□`

令

`w_k=Lambda(k)/sqrt(k)`, `a_k=log k`,

`2<=k<lambda^2`,                                      (8)

其中 `k=lambda^2` 的可能边界项具有零长度重叠，可删去。定义加权度数势

`D_lambda(y)=sum_(k<lambda^2)w_k d_(a_k)(y)`.           (9)

Weil form 的有限素数贡献满足精确恒等式

`-W_P(f,f)=sum_(k<lambda^2)w_k E_(a_k)(f)`

`             -int D_lambda(y)|f(y)|^2dy`.             (10)

因此素数项自身已经是一个加权有限图的“Laplacian 减 degree potential”。
脚本函数 `prime_graph_decomposition_for_function` 直接验证式 (10)，回归测试
同时检查其 identity error。

## 2. degree 势的尺度及逐项估计 no-go

记

`P_lambda^-=sum_(2<=k<lambda^2)Lambda(k)/sqrt(k)`.      (11)

### 引理 BD（degree 势至少具有线性尺度）

有

`||D_lambda||_infinity>=P_lambda^-`,                   (12)

并且由素数定理及分部求和，

`P_lambda^-=2lambda+o(lambda)`.                        (13)

#### 证明

令 `y->-ell` 从区间内部趋近左端点。在式 (5) 中，第一指示函数最终包含每个
固定 `a_k<L`，第二指示函数最终消失。因此 `D_lambda(y)->P_lambda^-`，
给出式 (12)。令 `psi(x)=sum_(n<=x)Lambda(n)`；素数定理给出
`psi(x)=x+o(x)`。Stieltjes 分部求和得到

`sum_(n<=x)Lambda(n)n^(-1/2)`

`=psi(x)/sqrt(x)+(1/2)int_1^x psi(t)t^(-3/2)dt`

`=2sqrt(x)+o(sqrt(x))`.                                (14)

取 `x=lambda^2` 即得。`□`

### 定理 BE（逐块 operator-norm 路线不能证明 BB）

任何按下列方式形成的下界：

1. 把每个正图能量 `E_(a_k)` 只用 `0` 下界；
2. 把 degree 势只用 `D_lambda<=||D_lambda||_infinity I`；
3. 把 archimedean 部分只用其与 `lambda` 无关的全局谱底；
4. 对有限秩极点项分别使用 Cauchy–Schwarz/operator norm，

所得负误差至少具有线性 `lambda` 尺度，因而不可能满足式 (1)。即使只看
偶子空间、使极点的负奇分量消失，degree 项仍留下

`-||D_lambda||_infinity<=-2lambda+o(lambda)`.           (15)

#### 证明

式 (10) 在步骤 1–2 后只能给出 `-W_P>=-||D_lambda||_infinity I`；
引理 BD 说明该常数线性发散。archimedean 的独立谱底只能贡献固定常数，
而分别估计有限秩项不能恢复被丢弃的、依赖 `f` 的图/极点相消。`□`

定理 BE 不是说式 (1) 不可能；它排除的是文档 004 式 (6) 那类把有限素数
质量整体取绝对值的证明策略。任何成功证明都必须联合估计 kinetic、graph、
degree 和 pole，而不能把它们拆开后比较算子范数。

数值上，`P_lambda^-/lambda` 在 `lambda^2=2,3,5,7,13,19,101,1009`
时约为

`0.347,0.649,0.980,1.106,1.379,1.493,1.727,1.912`,

清楚趋向式 (13) 的常数 `2`。

## 3. 完整 Weil form 的正部分减势分解

令 `K_infinity` 表示 Weil form 的 archimedean 自伴部分；在全线 Fourier
侧它是论文中的实 multiplier `partial_t theta(t)`，有有限谱底

`m_infinity=inf_t partial_t theta(t)>-infinity`.        (16)

文档 023 引理 CS 进一步无条件证明下确界在 `t=0` 取得，并给出
`m_infinity=-gamma/2-pi/4-(3/2)log2-(1/2)log pi` 的精确闭式。

极点 `0,1` 的 rank-two form 由文档 004 给出：

`Q_(0,2)(f)=2|C(f)|^2-2|S(f)|^2`,                     (17)

`C(f)=int f(y)cosh(y/2)dy`,

`S(f)=int f(y)sinh(y/2)dy`.

定义

`P_lambda(f)=< (K_infinity-m_infinity)f,f>`

` +sum_k w_k E_(a_k)(f)+2|C(f)|^2`,                   (18)

`V_lambda(f)=int D_lambda(y)|f(y)|^2dy`

` +2|S(f)|^2-m_infinity||f||^2`.                       (19)

### 命题 BF（Weil–graph 极化恒等式）

`P_lambda(f)>=0`，且

`QW_lambda(f,f)=P_lambda(f)-V_lambda(f)`.               (20)

#### 证明

`K_infinity-m_infinity>=0`，图能量和 `|C|^2` 也非负，所以第一条成立。
把式 (10)、(17) 代入，并在 (18)–(19) 中消去 `m_infinity||f||^2`，
恰恢复 `K_infinity-W_P+Q_(0,2)`。`□`

式 (20) 是数域版本最接近 Hodge–Riemann primitive decomposition 的对象：

- `P_lambda` 是明确的正极化；
- `V_lambda` 是必须被极化控制的 primitive/degree defect；
- global radical 与 prolate near-radical 对应二者几乎相等的方向。

## 4. 真正需要证明的算术 Hodge–Riemann 不等式

### 定理 BG（Weil–graph domination 到 RH）

若存在 `lambda_j->infinity`、`epsilon_j->0`，使对所有 form-domain `f`，

`V_(lambda_j)(f)<=P_(lambda_j)(f)+epsilon_j||f||^2`,   (21)

则 RH 成立。

#### 证明

命题 BF 与式 (21) 给出

`QW_(lambda_j)(f,f)>=-epsilon_j||f||^2`.               (22)

文档 015 的过滤渐近正性定理 AY/推论 BB 把式 (22) 升级为所有固定支撑
Weil form 的精确非负性，最后应用 Weil 判据。`□`

式 (21) 是本研究目前最简洁的经典 RH 存在性目标。它不是抽象地说“找一个
正内积”，而是要求以下完全显式的联合 coercivity：

`archimedean kinetic + prime graph gradients + even pole square`

`>= prime degree potential + odd pole square - o(1) mass`. (23)

在偶子空间上 `S(f)=0`；在奇子空间上 `C(f)=0`。所以式 (21) 可分成两个
独立不等式认证，但奇块多出负的 `2|S(f)|^2`，不能从偶块自动推出。

## 5. degree 轮廓与极点锚方向的尺度匹配

定义

`A(X)=sum_(2<=k<X)Lambda(k)/sqrt(k)`.                   (24)

### 引理 BH（degree profile）

对 `|y|<=ell`，有精确公式

`D_lambda(y)=A(lambda e^(-y))+A(lambda e^y)`.           (25)

因此：

1. 对每个固定 `Y`，在 `|y|<=Y` 上局部一致地

   `D_lambda(y)=4sqrt(lambda)cosh(y/2)+o(sqrt(lambda))`; (26)

2. 若 `y=z log(lambda)`、`|z|<1` 固定，则

   `D_lambda(y)=2lambda^((1-z)/2)+2lambda^((1+z)/2)`

   `             +o(lambda^((1+|z|)/2))`.              (27)

#### 证明

式 (9) 的第一指示函数等价于 `log k<=ell-y`，即 `k<=lambda e^(-y)`；
第二个等价于 `k<=lambda e^y`，得到式 (25)。引理 BD 的分部求和论证对
任意 `X->infinity` 给出 `A(X)=2sqrt(X)+o(sqrt(X))`。分别代入式 (25)
即得 (26)–(27)；固定紧区间上的一致性来自素数定理余项定义的通常一致化。
`□`

令极点锚函数

`c(y)=cosh(y/2)`, `s(y)=sinh(y/2)`.                    (28)

它们的精确范数为

`||c||^2=sinh(ell)+ell=(lambda-lambda^(-1))/2+log lambda`,

`||s||^2=sinh(ell)-ell=(lambda-lambda^(-1))/2-log lambda`. (29)

所以 rank-one forms `2|C(f)|^2` 与 `2|S(f)|^2` 的非零算子特征值分别为

`2||c||^2=lambda-lambda^(-1)+2log lambda`,

`2||s||^2=lambda-lambda^(-1)-2log lambda`.              (30)

它们与引理 BD 的 endpoint degree 尺度 `2lambda` 同阶；尤其不能在渐近
估计中把极点项当作低阶有限秩误差。

图能量在这两个锚方向上也可精确计算。令 `b=ell-a/2`，则

`E_a(c)=4sinh^2(a/4)[sinh(b)-b]`,

`E_a(s)=4sinh^2(a/4)[sinh(b)+b]`.                       (31)

这是因为

`c(y+a)-c(y)=2sinh(a/4)sinh(y/2+a/4)`，

`s(y+a)-s(y)=2sinh(a/4)cosh(y/2+a/4)`，

并把积分区间平移成对称的 `[-b,b]`。

式 (26) 与 (28) 的相同 `cosh(y/2)` 轮廓说明：偶极点平方是 prime degree
势的自然“常数/ample 类”锚，而素数图梯度应控制与它正交的 primitive
方向。这比抽象选择 prolate 子空间更接近有限域 Hodge–Riemann 分解的形状。
奇块则由 `s` 锚和式 (31) 的较大图能量共同决定，不能从偶块复制结论。

## 6. Schur/Hodge 分解的下一种可计算形式

选择一个由正 Fourier prolate 模态生成的有限维 near-radical 空间 `R_lambda`，
写

`H_lambda=R_lambda direct_sum R_lambda^perp`.           (32)

证明式 (21) 的一种充分方案是：

1. 在 `R_lambda` 上用保留全部素数相消的 interval matrix 证明
   `QW_lambda>=-a_lambda`；
2. 在 `R_lambda^perp` 上证明联合 form `P_lambda-V_lambda>=d_lambda>0`；
3. 对两个空间间的完整联合 form 耦合证明 `gamma_lambda`；
4. 令二乘二 Schur 下界

   `L(a,d,gamma)=(-a+d-sqrt((a+d)^2+4gamma^2))/2`      (33)

   满足 `L>=-epsilon_lambda`, `epsilon_lambda->0`。

这里第二步必须直接使用式 (23)，不能再退回 `P_lambda`、`V_lambda` 的独立
operator norms。它是数域中尚未构造出的 Hodge–Riemann primitive 正性。

## 7. 有限谱证据与边界

为避免 `lambda^2` 位于整数/素数边界时浮点取整错误，脚本新增 `--mu x`，
按高精度精确使用 `lambda=sqrt(x)`。在 Fourier cutoff `N=8` 时：

| `x=lambda^2` | 最低偶值 | 最低奇值 |
|---:|---:|---:|
| 2  | `1.4190e-3` | `9.1513e-2` |
| 3  | `1.0256e-7` | `1.8813e-5` |
| 5  | `4.5701e-15` | `2.2078e-12` |
| 7  | `2.2471e-18` | `8.9830e-16` |
| 11 | `8.9082e-22` | `4.6763e-19` |
| 13 | `7.6744e-23` | `3.9148e-20` |
| 17 | `1.3799e-24` | `6.5056e-22` |
| 19 | `5.2737e-25` | `2.8986e-22` |

这些有限矩阵均为正且显示偶 near-radical 分支，但它们不是式 (21) 的
无限维下界，也不能证明 RH。其价值是指出式 (24) 的核心应包含若干偶、奇
prolate 低模，而非只追踪一个候选向量。

下一步的最小分析任务已经很具体：为 degree 势 `D_lambda(y)` 建立一个
保留 endpoint pole square 与 prime graph gradients 的加权 Poincare/IMS
不等式，并检查其常数是否能在 prolate near-radical 空间的正交补上保持正值。
文档 017 又给出等价的全线 Fourier 表述：prime graph 的非负 multiplier
`G_lambda(t)` 与局部酉 Frobenius 相位自然兼容，从而得到覆盖 Dirichlet 与
tempered automorphic Euler 数据的定理 BL。

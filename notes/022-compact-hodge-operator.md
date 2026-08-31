# 紧 Hodge 算子与有限广义特征值证书

文档 017 把 zeta 的 Weil form 写成正极化减正 defect，文档 021 又把
prime resonance 的负方向有限余维化。本笔记给出二者之间更标准的算子
接口：用正极化定义一个 Birman--Schwinger 型紧算子。全球
Hodge--Riemann domination 恰好等价于该算子的最大特征值不超过 `1`。

这个改写没有预设零点，也没有把 RH 藏进算子的自伴性；算子的全部输入是
显式公式中的 archimedean multiplier、Euler 图平方和极点锚。

## 1. 正极化具有紧 resolvent

固定 `lambda`，令 `H_lambda=L^2([-ell,ell])`，函数在全线上零延拓。沿用
文档 017 的分解

`QW_lambda(f,f)=Ptilde_lambda(f)-Vtilde_lambda(f)`,     (1)

其中

`Ptilde_lambda(f)=int [K_infinity(t)-m_infinity+G_lambda(t)]`

`                         |hat f(t)|^2dt/(2pi)`

`                    +2|C(f)|^2`,                     (2)

`Vtilde_lambda(f)=a_lambda||f||^2+2|S(f)|^2`,          (3)

`a_lambda=2P_lambda-m_infinity>0`.                     (4)

这里 `K_infinity-m_infinity>=0`、`G_lambda>=0`，且
`K_infinity(t)->infinity`。在固定有限区间上，`C,S` 是有界线性泛函。

### 引理 CG（compact polarization resolvent）

式 (2) 是稠密定义的闭非负 form。对每个 `epsilon>0`，令

`p_(lambda,epsilon)(f)=Ptilde_lambda(f)+epsilon||f||^2` (5)

并令 `A_(lambda,epsilon)` 为它对应的正自伴算子。则

`A_(lambda,epsilon)>=epsilon I`，且
`A_(lambda,epsilon)^(-1)` 与
`A_(lambda,epsilon)^(-1/2)` 都是紧算子。              (6)

#### 证明

Fourier multiplier
`K_infinity-m_infinity` 的非负闭 form，加上有界非负 multiplier
`G_lambda` 和有限秩非负 form `2|C|^2`，仍是闭非负 form。

只需证明式 (5) 的 form domain 到 `H_lambda` 的嵌入紧。设 `{f_n}` 在
form norm 中有界。对充分大的 `T`，

`int_(|t|>T)|hat f_n(t)|^2dt/(2pi)`

`<=sup_(|t|>T)[K_infinity(t)-m_infinity+epsilon]^(-1)`

`  *p_(lambda,epsilon)(f_n)`.                          (7)

因 multiplier 趋于无穷，式 (7) 对所有 `n` 一致趋零。另一方面，从有限
位置区间到有限频带 `[-T,T]` 的 Fourier restriction 具有平方可积 kernel
`exp(-ity)`，因而是 Hilbert--Schmidt 算子；所以 `{hat f_n|_[-T,T]}`
预紧。低频预紧与式 (7) 的一致高频尾合并，再用 Plancherel，得到 `{f_n}`
在 `H_lambda` 中预紧。故 form 嵌入紧，相关算子有紧 resolvent；式 (6)
由谱演算得到。`□`

## 2. 紧 Hodge 算子的范数判据

令 `V_lambda` 是式 (3) 对应的有界正算子，即

`V_lambda=a_lambda I+2|s><s|`,                        (8)

其中 `S(f)=<f,s>`。定义

`T_(lambda,epsilon)`

`=A_(lambda,epsilon)^(-1/2)V_lambda`

` A_(lambda,epsilon)^(-1/2)`.                         (9)

### 定理 CH（compact Hodge domination criterion）

`T_(lambda,epsilon)` 是正紧自伴算子，而且下列命题等价：

1. `QW_lambda(f,f)>=-epsilon||f||^2` 对全部 form-domain `f` 成立；
2. `T_(lambda,epsilon)<=I`；
3. `||T_(lambda,epsilon)||<=1`；
4. `T_(lambda,epsilon)` 的最大特征值不超过 `1`。

#### 证明

引理 CG 说明两个 `A^(-1/2)` 因子紧；式 (8) 有界正，故式 (9) 正、紧且
自伴。又因 `A>=epsilon I`，映射

`u=A_(lambda,epsilon)^(1/2)f`                         (10)

把 form domain 双射到 `H_lambda`。代入式 (1) 得

`QW_lambda(f,f)+epsilon||f||^2`

`=<u,[I-T_(lambda,epsilon)]u>`.                       (11)

因此 1 等价于 2；正自伴性给出 2 等价于 3。正紧算子的非零范数是其最大
特征值，故又等价于 4。`□`

定理 CH 把文档 016 的全球 Hodge--Riemann 不等式变成一个真正的谱半径
问题，但与循环的 Hilbert--Polya 假设不同：这里没有假设零点是 `T` 的谱；
`T` 是从 prime graph 与 Gamma/pole 数据直接定义的紧算子。

## 3. 广义紧 Hodge--Weil 中心线结构定理

考虑文档 015 的相容 cofinal 过滤 `(H_t,q_t)`。假设每个 form 都有

`q_t=p_t-v_t`,                                        (12)

其中 `p_t` 是闭非负 form，`v_t` 由有界正算子 `V_t` 给出；并假设对每个
`epsilon>0`，`p_t+epsilon I` 的 form 嵌入紧。定义

`T_(t,epsilon)=(A_t+epsilon I)^(-1/2)V_t`

`                         (A_t+epsilon I)^(-1/2)`.    (13)

### 定理 CI（紧 Hodge--Weil 中心线定理）

若：

1. `(H_t,q_t)` 满足 Weil 型正性判据；
2. 存在 cofinal `t_j` 和正数 `epsilon_j->0`，使

   `||T_(t_j,epsilon_j)||<=1`,                         (14)

则对应完备 zeta/L 函数的全部非平凡零点位于函数方程中心线。

#### 证明

把定理 CH 的证明逐个应用于式 (12)–(13)，式 (14) 给出

`q_(t_j)>=-epsilon_j I`.                              (15)

文档 015 的过滤渐近正性定理 AY 将式 (15) 升级为每个固定 `q_t>=0`；最后
应用 Weil 型判据。`□`

有限域的极化 Lefschetz--Frobenius 情形在 primitive/coercive 部分对应有限
维 `T` 和精确 `epsilon=0` domination；若正极化有 kernel，则先取相应商或
保留正的 `epsilon`。文档 017 的酉 Euler--Weil 结构在满足上述紧嵌入时
给出数域版本。因此 CI 是同一个 Hodge--Riemann 机制的有限维、紧算子与
过滤渐近三种实现的共同表述。

对经典 zeta，引理 CG 验证紧性，命题 BJ 验证式 (12)，所以尚未证明的
存在性条件精确变成：构造 `lambda_j->infinity`、正数 `epsilon_j->0` 并证明

`lambda_max(T_(lambda_j,epsilon_j))<=1`.              (16)

式 (16) 与 RH 等价强度地接触，但其算子完全由素数和 archimedean 数据
定义，因而是一个非循环、可实际攻击的存在性目标。

## 4. 有限广义特征值与双边证书

固定 `lambda,epsilon`。令 `E_n` 是嵌套且在 form norm 中稠密的有限维
子空间，并令

`W_n=A_(lambda,epsilon)^(1/2)E_n`,                    (17)

`Pi_n` 为到 `W_n` 的正交投影。定义有限 Ritz 值

`rho_n=max_(0!=f in E_n)`

`       Vtilde_lambda(f)/p_(lambda,epsilon)(f)`.       (18)

### 定理 CJ（finite generalized-eigenvalue certificate）

有

`rho_n=||Pi_n T_(lambda,epsilon)Pi_n||`

`       increasing to ||T_(lambda,epsilon)||`.        (19)

并且

`eta_n=||T_(lambda,epsilon)-Pi_nT_(lambda,epsilon)Pi_n||`

`       ->0`.                                         (20)

所以任一严格可证的有限数据界

`rho_n+eta_n<=1`                                      (21)

蕴含 `QW_lambda>=-epsilon I`。若 `e_1,...,e_N` 是 `E_n` 的基，`rho_n`
正是 Hermitian 矩阵 pencil

`V^(n)c=rho P_epsilon^(n)c`,                           (22)

`V^(n)_(ab)=Vtilde_lambda(e_a,e_b)`,

`P_epsilon^(n)_(ab)=p_(lambda,epsilon)(e_a,e_b)`       (23)

的最大广义特征值。

#### 证明

form 稠密性说明 `W_n` 的并在 `H_lambda` 中稠密，故 `Pi_n->I` 强收敛。
式 (18) 经变量替换 `u=A^(1/2)f` 即为 `T` 在 `W_n` 上的最大 Rayleigh
商，得到式 (19) 的等号与单调性。紧算子在强收敛有限秩投影下满足

`||(I-Pi_n)T||+||T(I-Pi_n)||->0`,                     (24)

从而得到式 (20) 及式 (19) 的极限。式 (21) 给出 `||T||<=1`，再用定理
CH。最后，有限 Rayleigh 商的驻值方程就是式 (22)。`□`

还有一个有用的严格裕量事实：若固定 `lambda` 上已经有
`QW_lambda>=0`，则对每个 `epsilon>0`，

`||T_(lambda,epsilon)||<1`.                           (25)

否则紧性使特征值 `1` 被某个非零 `u` 取得；式 (11) 就给出
`QW_lambda(f,f)+epsilon||f||^2=0`，与两项均非负且 `f!=0` 矛盾。因此在
RH 为真的前提下，每个固定截面和正 `epsilon` 最终都存在有限的严格
Galerkin 证书。困难不在固定截面的有限可逼近性，而在不假设 RH 地给出
沿 `lambda->infinity,epsilon->0` 的统一 `eta_n` 上界。

## 5. zeta 的奇偶块与 rank-one resolvent 判据

`K_infinity(t)` 与 `G_lambda(t)` 都是偶 multiplier，`c(y)=cosh(y/2)` 为
偶函数，`s(y)=sinh(y/2)` 为奇函数。因此式 (2)–(3) 在

`H_lambda=H_lambda^even direct_sum H_lambda^odd`       (26)

下完全约化。令 `A_lambda^+`,`A_lambda^-` 分别为未加 `epsilon` 的正极化
算子在偶、奇子空间的限制，并仍记

`a_lambda=2P_lambda-m_infinity`.                       (27)

### 定理 CK（parity/rank-one Hodge criterion）

固定 `epsilon>0`。下界

`QW_lambda>=-epsilon I`                               (28)

等价于以下两个独立条件：

1. 偶块最低谱满足

   `inf spec(A_lambda^+)>=a_lambda-epsilon`;           (29)

2. 令

   `B_(lambda,epsilon)=A_lambda^-`

   `                         +(epsilon-a_lambda)I`.   (30)

   则 `B_(lambda,epsilon)>=0`、`s` 与其 kernel 正交，并且

   `2<s,B_(lambda,epsilon)^dagger s><=1`,             (31)

   其中 `dagger` 是在 `ker(B)^perp` 上的逆。

若式 (30) 严格正，则式 (31) 就是通常的 resolvent 不等式

`2<s,B_(lambda,epsilon)^(-1)s><=1`.                   (32)

#### 证明

偶块上 `S=0`，而式 (3) 只剩 `a_lambda I`；所以式 (28) 的偶块恰为
`A_lambda^++(epsilon-a_lambda)I>=0`，即式 (29)。

奇块上 `C=0`，而 defect 是
`a_lambda I+2|s><s|`。故式 (28) 的奇块等价于

`B_(lambda,epsilon)>=2|s><s|`.                        (33)

对具有紧 resolvent 的非负算子 `B`，rank-one form domination

`B>=2|s><s|`                                          (34)

成立，当且仅当 `s perpendicular ker(B)` 且
`sqrt(2)B^(-1/2)s` 的范数不超过 `1`。这是
Cauchy--Schwarz 的充分性；必要性可把线性泛函
`f mapsto sqrt(2)<f,s>` 延拓到以 `||B^(1/2)f||` 为范数的空间后应用 Riesz
表示。紧 resolvent 保证零特征空间有限维、其正交补上有正谱隙，所以该范数
正是式 (31)。`□`

定理 CK 把一般的有限核心矩阵进一步拆开：偶块只需认证一个最低特征值，
奇块则先认证同一 scalar threshold，再计算单个 resolvent 矩阵元。沿
`lambda_j->infinity,epsilon_j->0` 若能证明式 (29)、(31)，定理 CI 立即给出
RH。它也精确显示极点两锚的不同作用：`cosh` 已进入偶块正极化，`sinh`
只作为奇块的一个 rank-one defect。

## 6. 正极化谱基中的显式紧算子尾

令 `A=A_(lambda,epsilon)`，并取其规范正交本征系

`A phi_n=alpha_n phi_n`,

`epsilon<=alpha_1<=alpha_2<=...->infinity`.            (35)

记 `Pi_N` 为前 `N` 个本征向量的投影，

`u=A^(-1/2)s`.                                        (36)

由式 (8)–(9) 有精确分解

`T_(lambda,epsilon)=a_lambda A^(-1)+2|u><u|`.          (37)

### 推论 CL（polarization-spectral tail certificate）

在上述谱投影下，定理 CJ 的尾满足

`eta_N=||T-Pi_NTPi_N||`

`<=a_lambda/alpha_(N+1)`

`  +4||A^(-1/2)s||`

`    *(sum_(n>N)|<s,phi_n>|^2/alpha_n)^(1/2)`         (38)

`<=a_lambda/alpha_(N+1)`

`  +4||A^(-1/2)s|| ||(I-Pi_N)s||/sqrt(alpha_(N+1))`.  (39)

因此只要有限截面给出 `rho_N`，并以严格谱下界和 `sinh` 投影尾证明式
(38) 的右端不超过 `1-rho_N`，就得到定理 CJ 的完整证书。

#### 证明

因为 `Pi_N` 与 `A^(-1)` 交换，

`||a_lambda[A^(-1)-Pi_NA^(-1)Pi_N]||`

`=a_lambda/alpha_(N+1)`.                              (40)

令 `u_N=Pi_Nu`。rank-one 算子的初等恒等式给出

`|||u><u|-|u_N><u_N|||`

`<= (||u||+||u_N||)||u-u_N||`

`<=2||u||||(I-Pi_N)u||`.                              (41)

乘以式 (37) 中的系数 `2`，并注意

`||(I-Pi_N)u||^2`

`=sum_(n>N)|<s,phi_n>|^2/alpha_n`,                    (42)

得到式 (38)。再用 `alpha_n>=alpha_(N+1)` 得式 (39)。`□`

式 (38) 说明理想有限核心就是正极化 `A` 的低谱空间，而不是任意 Fourier
截面。要使第一项小于 `1` 至少需把 `alpha_n` 不显著大于 `a_lambda` 的方向
纳入 core；这些方向正是 `K_infinity+G_lambda` 较小的 prime-resonance
态。文档 018–021 的 resonance packing 和调制多项式 blocks 因而可解释为
对这个理想低谱空间的显式外逼近。

粗略只用 `K_infinity(t)~(1/2)log|t|` 会再次产生
`exp(O(P_lambda))` 规模；有用的统一证明必须利用 `G_lambda` 在绝大多数
频率上的大正值来提高 `alpha_(N+1)`，而不是依赖 archimedean 项单独增长。

## 7. 与 prime-resonance core 的接口

文档 021 的调制多项式 core 可直接选作式 (17) 中的 `E_n`。于是：

- `P_epsilon^(n)` 的 prime 部分是 twisted translation squares 的 Gram
  矩阵；
- `V^(n)` 是标量质量矩阵加一个奇极点 rank-one Gram 矩阵；
- 定理 CD/推论 CE 控制弱 resonance 在 core 外的负 Fourier 质量；
- 推论 CF 保证每个固定截面可有限余维化。

但 CE/CF 本身尚未给出式 (20) 所需的完整 `eta_n`，因为 `eta_n` 同时测量
core--complement coupling，而不仅是 complement 上的 Rayleigh 下界。下一
个精确目标因此是证明 resonance-adapted spaces 满足

`eta_(lambda_j,n_j)=o(1)`                              (43)

并以 interval arithmetic 证明相应有限 pencil 的

`rho_(lambda_j,n_j)<=1-eta_(lambda_j,n_j)`.            (44)

式 (43)–(44) 同时处理有限核正性和 Schur 耦合；由定理 CI/CJ 将直接推出
RH。当前结果没有证明这两个统一估计。

## 8. 有限矩阵一致性审计

脚本 `scripts/qw_matrix.py` 的函数
`build_polarization_defect_matrices` 按式 (2)–(4) 分别构造有限 Fourier
压缩 `P,V,QW`；`largest_generalized_eigenvalue` 用 Cholesky congruence
计算式 (22) 的最大广义特征值。回归测试直接检查

`P-V=QW`                                                (45)

以及

`rho_max<=1 iff lambda_min(QW+epsilon I)>=0`.          (46)

例如在 `lambda^2=13`、Fourier cutoff `3`、引理 CS 的精确
`m_infinity=-2.686091709612832...`、`epsilon=0.1` 时，普通双精度输出为

- 式 (45) 的最大逐元素误差 `1.55e-15`；
- `lambda_min(P)=11.207082593866186`；
- `lambda_min(V)=11.207082593861522`；
- `rho_max=0.991462309571396`；
- `lambda_min(QW+epsilon I)=0.100000000004655`。

这些浮点数不是 RH 证书；它们只验证新 Hodge pencil 与原 QW 有限矩阵的
代数实现一致，并再次显示 `P`、`V` 在 near-radical 方向上发生极尖相消。
`m_infinity` 本身则由文档 023 引理 CS 严格证明，不依赖该浮点实验。

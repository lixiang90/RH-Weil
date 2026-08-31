# 过滤 near-radical 与渐近 Hodge–Riemann 正性

前面的 AM、AQ、AV、AW 都试图识别半局部 Weil 算子的某条最低谱线，
以便构造自伴 rank-one 算子并让其行列式趋于 `Xi`。原始 Weil 判据还提供
另一条更弱的出口：只要显式公式二次型在所有紧支撑测试函数上非负，就直接
得到 RH，并不需要最低特征值单重、偶性或谱隙。

本笔记把这一点抽象成一个“过滤渐近极化”结构定理。其核心是：在不断扩大的
测试空间上，最低 Rayleigh 值单调下降；若在一列趋于全空间的截面上只差
`o(1)` 就非负，那么每个固定小截面事实上必须**严格非负**。这提供了一个
比相对谱夹逼弱得多的存在性目标。

## 1. 相容过滤的最低值

令 `(H_t)_(t in T)` 是按有向参数递增的 Hilbert 子空间族，等距地视为同一
线性空间中的子空间。对每个 `t` 有下有界闭 Hermitian form `q_t`，并满足
相容性

`q_s|_(H_t)=q_t,  whenever s>=t`.                     (1)

定义

`mu_t=inf_(0!=f in Dom(q_t)) q_t(f,f)/||f||^2`.       (2)

### 引理 AX（过滤单调性）

若 `s>=t`，则 `mu_s<=mu_t`。

#### 证明

式 (2) 在更大的集合上取下确界。`□`

这里不需要离散谱；`mu_t` 可以只是谱底。若 form 对应紧预解式算子，它才是
最低特征值。

## 2. `o(1)` 下界自动升级为精确正性

### 定理 AY（过滤渐近正性定理）

设 `t_j` 是 cofinal 序列，即对每个固定 `t` 最终都有 `t_j>=t`。若存在
`epsilon_j>=0`，

`epsilon_j->0`,  `mu_(t_j)>=-epsilon_j`,               (3)

则

`q_t(f,f)>=0` 对每个 `t` 和每个 `f in Dom(q_t)`。   (4)

#### 证明

固定 `t`。对所有充分大的 `j`，由引理 AX，

`mu_t>=mu_(t_j)>=-epsilon_j`.                          (5)

令 `j->infinity` 得 `mu_t>=0`，即式 (4)。`□`

定理 AY 的量词非常重要：不要求对每个大截面先证明精确正性，只要求一个
随截面消失的统一负误差。相容性会把渐近信息反向传回每个固定测试函数。

### 推论 AZ（渐近极化/平方分解）

若沿 cofinal 序列存在 Hilbert 空间 `K_j`、线性算子 `D_j` 和 Hermitian
余项 `r_j`，使

`q_(t_j)(f,f)=||D_j f||_(K_j)^2+r_j(f,f)`,             (6)

`r_j(f,f)>=-epsilon_j||f||^2`, `epsilon_j->0`,         (7)

则所有 `q_t` 非负。

这就是一种**渐近 Hodge–Riemann 结构**：`D_j^*D_j` 是正极化部分，
`r_j` 是算子范数下界趋零的缺陷。有限域 Weil 证明中的 Hodge–Riemann
正性可看作 `epsilon_j=0` 的精确版本；数域显式公式只需构造渐近版本。

式 (6) 并不要求 `D_j` 可逆，也不排斥大的 radical。事实上 near-radical
正是合理结构的一部分，而不是障碍。

## 3. near-radical 只负责证明界是尖的

假设另有单位向量 `k_j in Dom(q_(t_j))` 满足

`q_(t_j)(k_j,k_j)<=eta_j`, `eta_j->0`.                 (8)

则 `mu_(t_j)<=eta_j`。与式 (3) 合并得到

`-epsilon_j<=mu_(t_j)<=eta_j`,                         (9)

所以 `mu_(t_j)->0`。

注意定理 AY 推出正性本身并不需要式 (8)；near-radical 的作用是说明谱底
确实趋于 `0`，而非停在正数。对 prolate 路线，文档 013 的 radical truncation
identity 正是在解释式 (8)，但从 Fourier leakage 到 form 能量仍需式 (13)
那样的 form-continuity 估计。

## 4. 广义中心线结构定理

设 `Lambda(s)` 是具有函数方程中心 `c/2` 的完备 zeta/L 函数，并有如下
显式公式结构：

1. 一个递增、穷尽允许测试函数的过滤 `(H_t)`；
2. 相容 Hermitian forms `q_t`，其素数/周期轨道侧由 `Lambda` 的显式公式
   定义；
3. 一个已证明的 Weil 型判据：全部非平凡零点位于 `Re(s)=c/2` 当且仅当
   `q_t>=0` 对所有 `t`；
4. 沿某 cofinal 序列存在式 (6)–(7) 的渐近极化。

### 定理 BA（过滤渐近 Weil 结构定理）

满足 1–4 的 `Lambda` 的全部非平凡零点位于中心线 `Re(s)=c/2`。

#### 证明

推论 AZ 给出所有 `q_t>=0`，再应用假设 3 的 Weil 型判据。`□`

对非自对偶 L 函数，应在 `L(s,pi)` 与 `L(s,pi^vee)` 的配对测试空间上取
Hermitian form；只要相应显式公式的正性判据已建立，定理 BA 原样适用。
不能仅从每个素数的局部参数纯性推导假设 3。

定理 BA 抽离出的结构比“构造一个自伴零点算子”更宽：

- 不要求零点预先作为某个算子的离散谱；
- 不要求 simple-even 最低态；
- 不要求正规化行列式收敛；
- 只要求素数侧显式公式 form 有一个负缺陷趋零的正平方分解。

这正是可以尝试在 Selberg zeta、automorphic L 函数或其他具有 Weil 型
显式公式的系统中复用的广义结构。

## 5. 经典 zeta 的直接 specialization

取

`H_lambda=L^2([lambda^(-1),lambda],du/u)`,

`q_lambda=QW_lambda`.                                 (10)

零延拓给出递增过滤，相容性来自同一个全局 Weil 分布。原论文
[Zeta Spectral Triples 的定理 3.6 与推论 3.7–3.8](https://arxiv.org/html/2511.22755)
证明连续谱底
`mu_lambda` 随 `lambda` 单调下降，并证明：若 `mu_lambda->0`，则 RH。
它同时明确警告不能无条件断言 `mu_lambda>=0`。

由定理 AY，经典 RH 的一个足够条件是：存在 `lambda_j->infinity` 以及
显式可证的

`QW_(lambda_j)(f,f)>=-epsilon_j||f||^2`,

`epsilon_j->0`,                                       (11)

对整个 form domain 成立。式 (11) 已直接推出每个固定 `QW_lambda>=0`；
若再用 prolate near-radical 给出式 (8)，就恢复 `mu_lambda->0` 的精确表述。

与定理 AW 相比，式 (11) 不需要下界误差小于 `10^(-30)` 的 Ritz 值或第一
谱隙；任何绝对速率如

`epsilon_j=O(1/log lambda_j)`                          (12)

都足够。困难仍是真实的：现有粗略“archimedean 正项减去素数有界扰动”下界
随 `lambda` 恶化，并没有给出式 (11)。但目标强度已经被正确降低。

## 6. 可计算的 Schur 证书版本

令 `P_N` 是 Fourier 低频截面。沿 `(lambda_j,N_j)`，假设 interval/解析
估计给出

- `a_j<=inf spec(P_N A P_N)`；
- `d_j<=inf q` 在高频余空间上的 Rayleigh 下界；
- `|q(u,v)|<=gamma_j||u||||v||` 的低高耦合界。

文档 004 引理 J 给出全空间下界

`L_j=(a_j+d_j-sqrt((a_j-d_j)^2+4gamma_j^2))/2`.       (13)

### 推论 BB（有限 Schur 证书到 RH）

若 `lambda_j->infinity` 且存在 `epsilon_j->0` 使

`L_j>=-epsilon_j`,                                    (14)

则 RH 成立。

#### 证明

式 (13)–(14) 是定理 AY 的假设 (3)，再用经典 Weil 判据。`□`

BB 是目前最宽松的有限证书终点。它只认证整个 form “几乎非负”，不必追踪
任何极小本征向量。现有文档 005 的逐行尾界不足以控制随 `N_j` 增长的整个
矩形耦合算子；下一步应针对式 (13) 直接构造三层 core–buffer–tail 的
Hilbert–Schmidt/Schur 下界，并检查是否能让负修正绝对趋零。

## 7. 循环性边界

以下说法不能冒充式 (11) 的证明：

1. 假设 `QW_lambda>=0`；这就是 Weil 正性本身。
2. 只验证有限矩阵正定；未控制的无限尾可能产生负方向。
3. 对每个固定 `lambda` 给出一个依赖它的有限负常数；必须证明该常数沿
   cofinal 截面趋于 `0`。
4. 只证明存在 near-radical 上界；上界 `mu_lambda<=o(1)` 不排除谱底趋于
   负常数或 `-infinity`。

真正的新存在性问题已经压缩成：从 archimedean multiplier 的增长、有限
素数平移的结构以及 global radical 的截断几何，构造式 (6) 的渐近平方分解，
或等价地完成推论 BB 的绝对 `o(1)` Schur 下界。文档 016 已把素数负平移
精确完成平方为图 Dirichlet 能量减 degree 势，并将所需联合 coercivity
写成定理 BG 的算术 Hodge–Riemann 不等式。

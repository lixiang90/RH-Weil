# Residual--Feshbach 消元与奇偶 Hodge 有限证书

文档 023 推论 CQ 的最终条件仍使用单个耦合常数 `beta`。这会丢失不同
resonance core 方向之间的大量相消。本笔记用 residual Gram 矩阵保留全部
有限维几何，并通过 Feshbach/Schur 消元得到严格的矩阵证书。结果与文档
006–011 的 cancellation-preserving residual 方法相容，但现在直接作用于
正极化阈值算子，而不是只追踪一个候选最低向量。

## 1. 抽象 residual--Feshbach 下界

令 `B` 是 Hilbert 空间 `H` 上的自伴算子，`Q subset Dom(B)` 为 `r` 维
子空间，`P` 是到 `Q` 的正交投影。相对于

`H=Q direct_sum Q^perp`                               (1)

写 form block

`B=[A C^*; C D]`,                                     (2)

其中

`A=PBP|_Q`, `C=(I-P)BP|_Q`.                           (3)

假设余空间压缩满足严格 form 下界

`D>=gamma I`, `gamma>0`.                              (4)

定义 residual Gram 算子及有限 Schur 下界

`R=C^*C>=0`,                                          (5)

`L=A-gamma^(-1)R`.                                    (6)

### 定理 CT（residual--Feshbach matrix certificate）

在上述假设下：

1. 精确 Feshbach complement

   `S=A-C^*D^(-1)C`                                   (7)

   满足 `S>=L`；
2. 若 `L>=0`，则 `B>=0`；
3. 若 `L>0`，则 `B>0`，而且对每个 `z in Q`，

   `<z,B^(-1)z><=<z,L^(-1)z>`.                        (8)

#### 证明

式 (4) 给出 `0<D^(-1)<=gamma^(-1)I`，所以

`C^*D^(-1)C<=gamma^(-1)C^*C`,                        (9)

即 `S>=L`。对 `u in Q,v in Q^perp` 完成平方：

`<u+v,B(u+v)>`

`=<u,Su>+<D^(1/2)[v+D^(-1)Cu],`

`               D^(1/2)[v+D^(-1)Cu]>`.              (10)

因此 `L>=0` 蕴含 `S>=0`，再由式 (10) 得 `B>=0`。若 `L>0`，则
`S>0,D>0`，故 `B>0`。block inverse 公式给出

`P B^(-1)P|_Q=S^(-1)<=L^(-1)`,                       (11)

其中最后一步使用正算子逆序性，得到式 (8)。`□`

若 `e_1,...,e_r` 是 `Q` 的规范正交基，则式 (5) 可完全由 core action
计算：

`R_(ij)=<Be_i,Be_j>-sum_(k=1)^r`

`                    <Be_i,e_k><e_k,Be_j>`.          (12)

所以证书不需要构造余空间基或显式求 `D^(-1)`。它只需要：有限 core 矩阵
`A`、各 core 基向量的完整 operator residual，以及一个余空间谱隙
`gamma`。

## 2. 标量 Schur 界是矩阵证书的粗化

若已有

`A>=mu I`, `||C||<=beta`,                             (13)

则 `R<=beta^2I`，从而

`L>= (mu-beta^2/gamma)I`.                             (14)

文档 023 的条件 `beta^2<=mu gamma` 正是式 (14) 的标量充分条件。定理 CT
保留 `A` 与 `R` 的共同本征方向和非对角相消，可能在标量界失败时仍认证
`L>=0`。

## 3. zeta 偶块的有限证书

沿用文档 022 的正极化奇偶限制 `A_lambda^+`,`A_lambda^-`，并令

`a_lambda=2P_lambda-m_infinity`.                       (15)

固定 `epsilon>0`，定义 threshold operators

`B_lambda^+=A_lambda^+ +(epsilon-a_lambda)I`,          (16)

`B_lambda^-=A_lambda^- +(epsilon-a_lambda)I`.          (17)

取由文档 021/023 的对称 resonance cover 生成的有限 core，并分解成
`Q_lambda^+`,`Q_lambda^-`。把 `s(y)=sinh(y/2)` 加入奇 core。推论 CN 给出

`B_lambda^+|_(Q_lambda^+)^perp>=gamma_+ I`,

`B_lambda^-|_(Q_lambda^-)^perp>=gamma_- I`,           (18)

其中可取

`gamma_+`,`gamma_-`

`>=Delta+epsilon-(a_lambda+Delta)chi`.                (19)

对两个 parity block 分别用式 (3)、(5)–(6) 构造

`L_lambda^+=A_core^+-R_+/gamma_+`,                    (20)

`L_lambda^-=A_core^--R_-/gamma_-`.                    (21)

这里 `A_core^+`,`A_core^-`,`R_+`,`R_-` 都针对相应 threshold operator
`B_lambda^+`,`B_lambda^-`，不是原始 `QW` 矩阵。

### 定理 CU（parity residual Hodge certificate）

若 interval/解析估计严格证明

`L_lambda^+>=0`,                                      (22)

`L_lambda^->0`,                                       (23)

以及在奇 core 的坐标中

`2<s,L_lambda^-^(-1)s><=1`,                           (24)

则

`QW_lambda>=-epsilon I`.                              (25)

#### 证明

偶块的 Weil form 加 `epsilon I` 就是 `B_lambda^+`。式 (18)、(20)、(22)
与定理 CT 给出 `B_lambda^+>=0`。

奇块的 Weil form 加 `epsilon I` 是

`B_lambda^--2|s><s|`.                                (26)

由式 (18)、(21)、(23) 及定理 CT，`B_lambda^->0`，并且

`2<s,(B_lambda^-)^(-1)s>`

`<=2<s,(L_lambda^-)^(-1)s><=1`.                      (27)

文档 022 定理 CK 的 rank-one 判据因而给出式 (26) 非负。合并奇偶块得到
式 (25)。`□`

式 (24) 中的 `s` 是其到 `Q_lambda^-` 的坐标向量；因为构造时已把完整
`s` 加入 core，不存在遗漏的 anchor 尾。

## 4. Cofinal residual--Feshbach 结构定理

### 定理 CV（cofinal finite Hodge certificates imply RH）

若存在 `lambda_j->infinity`、正数 `epsilon_j->0`，以及相应有限
resonance cores，使：

1. 文档 023 式 (12)、(14) 给出正的余空间隙 `gamma_j^+`,`gamma_j^-`；
2. 所有 core action 与 residual Gram 矩阵都有严格 enclosure；
3. 式 (22)–(24) 对每个 `j` 成立；

则 RH 成立。

#### 证明

定理 CU 对每个 `j` 给出

`QW_(lambda_j)>=-epsilon_j I`.                        (28)

文档 015 定理 AY 把 cofinal 渐近下界升级为全部固定 Weil forms 的非负性，
再应用 Weil 正性判据。`□`

CV 是目前最具体的有限存在性结构：输入不再包含未知无限谱或抽象耦合范数，
只有 resonance cover、block concentration、有限矩阵和完整 residual Gram
尾。它没有证明这些 enclosure 沿 `lambda` 具有所需裕量。

## 5. 与既有 exact-resolvent 尾的接口

对 core 基 `e_i`，式 (12) 需要完整向量 `B e_i` 的 Gram 矩阵。文档 006
把单个有限支撑候选的完整 residual 化成 finite buffer 加远尾；文档 008–011
又给出保留极点、archimedean、prime 相消的全阶 exact-resolvent 尾。因此
可对每一对 core 基向量使用极化恒等式

`<r_i,r_j>=1/4 sum_(omega in {1,-1,i,-i})`

`             omega ||r_i+omega r_j||^2`             (29)

（按所用内积约定调整共轭系数），把已有平方尾证书升级为 residual Gram
entry enclosure。

真正的新计算瓶颈是 core 维数随 resonance cover 增长；逐对极化需要
`O(r^2)` 个 enclosure。下一步应直接对 residual block 使用 Hilbert--Schmidt/
low-rank factorization，避免对巨大 core 做逐项平方尾。

脚本中的非零耦合 `5` 维回归例给出

- `lambda_min(L)=2.93523870265794`；
- `lambda_min(S-L)=0.00221816879916>0`；
- 精确 `2<z,B^(-1)z>=0.07619913201595`；
- 证书上界 `2<z,L^(-1)z>=0.07633050914982`。

这只检查定理 CT 的有限线性代数实现，不是 zeta 的 interval 证书。

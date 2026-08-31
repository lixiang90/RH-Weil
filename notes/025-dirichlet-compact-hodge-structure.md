# Primitive Dirichlet L 函数的紧 Hodge 结构

文档 017 已指出 primitive Dirichlet Euler 参数局部酉，但当时把全球部分只
记为抽象 domination。本笔记把文档 022–024 的紧 Hodge、resonance 低谱与
residual--Feshbach 结构完整专门化。对非主 primitive 特征，完备 L 函数
没有极点，因此 zeta 奇块中的 `sinh` rank-one defect 完全消失；全球 GRH
条件只剩一个正极化算子的最低本征值下界。

## 1. 奇偶 Gamma 因子的精确谱底

令 `chi` 是 conductor `N` 的 primitive Dirichlet 特征，并以

`kappa in {0,1}`, `chi(-1)=(-1)^kappa`               (1)

记其 parity。完备函数的 Gamma 因子为

`(N/pi)^((s+kappa)/2) Gamma((s+kappa)/2)`.            (2)

在中心线 `s=1/2+it` 上，相应 archimedean multiplier 是

`K_(kappa,N)(t)`

`=1/2 Re psi(1/4+kappa/2+it/2)`

` +1/2 log(N/pi)`.                                    (3)

### 引理 CW（Dirichlet Gamma spectral bottom）

式 (3) 的严格全局最低点在 `t=0`，且

`m_(kappa,N)=inf_t K_(kappa,N)(t)`

`=-gamma/2+(2kappa-1)pi/4-(3/2)log2`

` +1/2 log(N/pi)`.                                    (4)

#### 证明

文档 023 引理 CS 的级数证明对每个 `a>0` 都给出

`Re psi(a+iy)>=psi(a)`,                               (5)

且 `y!=0` 时严格。取 `a=1/4+kappa/2` 得最低点。引理 CS 证明中反射与倍乘
公式给出

`psi(1/4)=-gamma-pi/2-3log2`,

`psi(3/4)=-gamma+pi/2-3log2`.                         (6)

代入式 (3) 即得式 (4)。`□`

特别地，`kappa=0,N=1` 恢复 zeta 的引理 CS。导体只把整个 multiplier 平移
`(1/2)log N`，不会改变最低点或 compact-resolvent 机制。

## 2. Paired Euler 图平方

固定截断 `lambda`，令

`P_(chi,lambda)=sum_(2<=k<=lambda^2,(k,N)=1)`

`                    Lambda(k)/sqrt(k)`.              (7)

对每个未分歧 prime power `k=p^m`，

`u_k=chi(k)=chi(p)^m`, `|u_k|=1`.                     (8)

在

`H_lambda=L^2([-log lambda,log lambda],C^2)`          (9)

上配对 `chi,bar chi`，并令

`U_k=diag(chi(k),bar chi(k))`.                        (10)

零延拓后的 `U_k tau_(log k)` 是酉算子。文档 017 引理 BI 给出

`-2Re<f,U_k tau_(log k)f>`

`=||f-U_k tau_(log k)f||^2-2||f||^2`.                (11)

其 Fourier graph multiplier 是对角矩阵

`G_(chi,lambda)(t)`

`=diag(2P-2Re F_chi(t),2P-2Re F_barchi(t))>=0`,       (12)

其中

`F_chi(t)=sum_(k<=lambda^2,(k,N)=1)`

`              Lambda(k)chi(k)k^(it)/sqrt(k)`.        (13)

第二个对角元是第一个在 `t mapsto -t` 下的反射。

非主 primitive `chi` 的完备 L 函数是 entire，所以没有 zeta 的 `C,S` 极点
锚。定义

`Pcal_(chi,lambda)(f)`

`=int <hat f(t),[K_(kappa,N)(t)-m_(kappa,N)`

`                    +G_(chi,lambda)(t)]hat f(t)>`

`                    dt/(2pi)`,                       (14)

`Vcal_(chi,lambda)(f)=a_(chi,lambda)||f||^2`,         (15)

`a_(chi,lambda)=2P_(chi,lambda)-m_(kappa,N)`.         (16)

下文只取满足 `a_(chi,lambda)>=0` 的截面。对固定 `N`，删去有限个 ramified
primes 不改变
`P_(chi,lambda)=2lambda+o(lambda)`，所以该条件对所有充分大的 `lambda`
自动成立，且不影响 cofinal 判据。

### 命题 CX（primitive Dirichlet compact polarization）

paired Weil form 满足精确分解

`q_(chi,lambda)=Pcal_(chi,lambda)-Vcal_(chi,lambda)`, (17)

其中 `Pcal>=0`、`Vcal>=0`。`Pcal+epsilon I` 对每个 `epsilon>0` 具有紧
resolvent。

#### 证明

式 (11) 对所有未分歧 prime powers 求和，得到式 (12) 的正 graph energy
减 `2P||f||^2`。式 (3) 减去其精确谱底非负；非主 primitive 情形没有极点
项。因此收集 scalar mass 即得式 (14)–(17)。

`K_(kappa,N)(t)-m_(kappa,N)->infinity`，而图 multiplier 有界非负，所以
文档 022 引理 CG 的有限支撑 Fourier-tail 证明原样给出紧 form 嵌入。`□`

对实特征，两个 paired 分量相同，可只保留一个；对复特征，配对保证
Hermitian Weil form 同时控制 `L(s,chi)` 与 `L(s,bar chi)`。

## 3. 最低正极化本征值的 GRH 判据

令 `A_(chi,lambda)` 是式 (14) 的正自伴算子，最低本征值记为

`alpha_1(chi,lambda)`.                                (18)

因为 defect 只是 scalar identity，紧 Hodge 算子简化为

`T_(chi,lambda,epsilon)`

`=a_(chi,lambda)[A_(chi,lambda)+epsilon I]^(-1)`.     (19)

### 定理 CY（primitive Dirichlet compact-Hodge GRH criterion）

下列固定截面条件等价：

1. `q_(chi,lambda)>=-epsilon I`；
2. `||T_(chi,lambda,epsilon)||<=1`；
3. `alpha_1(chi,lambda)>=a_(chi,lambda)-epsilon`.     (20)

若存在 `lambda_j->infinity`、正数 `epsilon_j->0`，使式 (20) 沿该序列
成立，则 `L(s,chi)` 与 `L(s,bar chi)` 的全部非平凡零点均位于
`Re(s)=1/2`。

#### 证明

前两项由文档 022 定理 CH。式 (19) 的范数是

`a_(chi,lambda)/(alpha_1(chi,lambda)+epsilon)`,       (21)

所以范数不超过 `1` 等价于式 (20)。沿 cofinal 序列，文档 015 定理 AY
把渐近下界升级为全部 paired Weil forms 非负；经典 paired Weil 判据给出
两函数的 GRH。`□`

与 zeta 相比，这里没有奇块 rank-one resolvent 条件。困难完全聚焦为：局部
酉 Euler 图与 Gamma kinetic 的联合最低本征值能否达到 scalar degree mass。

## 4. Dirichlet resonance 与有限 Feshbach 证书

对第一 paired 分量，给定 `Delta>0`，正极化 multiplier 低于
`a_(chi,lambda)+Delta` 的集合是

`E_(chi,lambda,Delta)`

`={t:K_(kappa,N)(t)-2Re F_chi(t)<Delta}`.             (22)

另一分量是其反射。文档 021 的 block large-sieve 证明只使用频率分离与
`|x|<=1`，不要求 Euler 相位为 `1`，所以对这些 twisted resonance 井原样
成立。若调制多项式 core `Q` 给出 concentration `chi_0`，文档 023 定理 CM
给出

`alpha_(dim Q+1)(A_(chi,lambda))`

`>=[a_(chi,lambda)+Delta](1-chi_0)`.                 (23)

若

`chi_0<(Delta+epsilon)/(a_(chi,lambda)+Delta)`,       (24)

则 threshold operator

`B=A_(chi,lambda)+(epsilon-a_(chi,lambda))I`          (25)

在 `Q^perp` 上有正隙

`gamma=Delta+epsilon`

`       -(a_(chi,lambda)+Delta)chi_0`.               (26)

### 推论 CZ（finite Dirichlet Feshbach certificates imply GRH）

沿 `lambda_j->infinity`、正数 `epsilon_j->0`，若能选择 twisted-resonance
cores，使式 (24) 成立，并对式 (25) 的 core block `A_j` 与 residual Gram
`R_j` 严格证明

`A_j-R_j/gamma_j>=0`,                                 (27)

则 `L(s,chi)` 和 `L(s,bar chi)` 满足 GRH。

#### 证明

式 (26) 是余空间隙。文档 024 定理 CT 与式 (27) 给出 `B>=0`，即固定截面
`q_(chi,lambda_j)>=-epsilon_jI`。再应用定理 CY。`□`

因此 primitive Dirichlet 情形的局部/解析结构存在性已经无条件完成：

- Euler phases 在所有未分歧 primes 上严格酉；
- Gamma 谱底有闭式；
- 正极化有紧 resolvent；
- resonance complement 与 residual--Feshbach 有无遗漏的有限证书框架。

尚未完成、且与 GRH 等价强度接触的唯一全球输入，是证明式 (27) 沿某
cofinal 截面具有 `epsilon_j->0` 的统一裕量。

脚本还用模 `5` 的四次 primitive 特征数值检查式 (12)：ramified
prime powers 被省略，其他相位严格位于单位圆，`0<=G_chi<=4P_chi`，且
`G_(bar chi)(-t)=G_chi(t)`。这只是公式实现回归，不是 GRH 数值证书。

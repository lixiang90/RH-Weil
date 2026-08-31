# 二通道边界 Hodge block 与 RH

文档 032 用素数边界信号构造了有限时间正 Gram forms。本笔记把这些信号
直接放回 Weil form：固定左、右边界剖面张成一个二维子空间。其两个对角
矩阵元在截断增大后保持常数，而非对角矩阵元等于中心化素数信号的负值
加一个一致有界的 archimedean/pole 修正。因此，仅要求这一族显式
`2 x 2` Hodge blocks 具有统一下界，就已经等价于 RH。

这把“canonical Hodge defect 的全球正性”进一步压缩成一个 separating
二维边界块族。它仍不是 RH 的证明，但提供了一个极小、完全显式的有限
Schur 目标。

## 1. 边界二维子空间

固定单位范数

`f_L,f_R in C_c^infinity((0,B))`.                    (1)

令 `ell=log lambda`, `t=2ell`, 并在 `[-ell,ell]` 中定义

`l_lambda(-ell+u)=f_L(u)`,

`r_lambda(ell-z)=f_R(z)`,                            (2)

其他位置为零。`ell>B` 时两向量正交且范数为一。把 Weil sesquilinear
form 限制到它们的张成空间，记矩阵

`M_lambda=[[a_L(lambda),c_lambda],`

`          [conjugate(c_lambda),a_R(lambda)]]`.       (3)

这里采用 form 对第二变量线性的约定。定义

`L_0=int f_L(u)e^(-u/2)du`, `R_0=int f_R(u)e^(-u/2)du`,

`L_+=int f_L(u)e^(u/2)du`,  `R_+=int f_R(u)e^(u/2)du`, (4)

以及文档 031 的边界卷积

`h(v)=int_0^v conjugate(f_L(u))f_R(v-u)du`,

`H(s)=L^sharp(s)R(s)`.                               (5)

### 命题 EE（exact two-channel boundary block）

当 `2log lambda>3B` 时：

1. `a_L(lambda)=a_L`、`a_R(lambda)=a_R` 与 `lambda` 无关；
2. 非对角元精确满足

   `c_lambda=-r_h(2log lambda)+b_lambda`,             (6)

   其中 `r_h` 是文档 032 式 (3)，而

   `b_lambda=K_infinity(l_lambda,r_lambda)`

   `                 +lambda^(-1)conjugate(L_+)R_+` (7)

   一致有界。

#### 证明

先看 prime part。小平移 `log n<=B` 只能在同一个边界层内部作用，所以
两个对角元只含一个与 `lambda` 无关的有限和。大平移只从左层走向右层；
文档 030 的换元给出其非对角元

`-sum_n Lambda(n)n^(-1/2)h(log(lambda^2/n))`

`=-A_h(lambda^2)`.                                   (8)

archimedean multiplier 对平移酉不变、对反射不变，故两个对角元固定。
交叉矩阵元虽然带相位，但由

`|K_infinity(s)|<=C+log(2+|s|)`                      (9)

与剖面 Fourier 快降一致有界。

对 pole form，令

`I_+(f)=int f(y)e^(y/2)dy`, `I_-(f)=int f(y)e^(-y/2)dy`. (10)

其 sesquilinear 化为

`q_pole(f,g)=conjugate(I_+(f))I_-(g)`

`                         +conjugate(I_-(f))I_+(g)`. (11)

式 (2) 给出

`I_+(l)=lambda^(-1/2)L_+`, `I_-(l)=lambda^(1/2)L_0`,

`I_+(r)=lambda^(1/2)R_0`,  `I_-(r)=lambda^(-1/2)R_+`. (12)

因此 pole 对角元分别为
`2Re(conjugate(L_+)L_0)`、`2Re(conjugate(R_0)R_+)`，均固定；交叉元为

`lambda conjugate(L_0)R_0`

` +lambda^(-1)conjugate(L_+)R_+`.                    (13)

由 `H(1/2)=conjugate(L_0)R_0` 和
`r_h(t)=A_h(e^t)-e^(t/2)H(1/2)`，式 (8)、(13) 加 archimedean
交叉元即为式 (6)、(7)。`□`

所以所有可能的无界负惯性都集中在单个复数 `c_lambda` 中；两个自能量通道
本身没有 endpoint 增长。

## 2. 二维半有界性判据

称一族剖面对 `P` 是 separating，若对每个 `w`、`Re w>0`，存在
`(f_L,f_R) in P` 使

`L^sharp(w)R(w)!=0`.                                 (14)

### 定理 EF（uniform two-channel Hodge lower bounds are equivalent to RH）

下列条件等价：

1. RH 成立；
2. 对某个 separating 剖面族 `P` 中的每一对，存在常数
   `C_(f_L,f_R)<infinity`，使所有充分大的 `lambda` 满足

   `M_lambda>=-C_(f_L,f_R) I_2`.                     (15)

#### 证明：RH 推出式 (15)

RH 的 Weil 正性判据事实上给出每个紧支撑测试空间上的 `QW>=0`，故可取
`C=0`。也可只用文档 031 定理 DY：它使 `c_lambda` 有界，而两个对角元
固定，故最低本征值一致有下界。

#### 证明：式 (15) 推出 RH

由式 (3)，`M_lambda+C I>=0` 蕴含

`|c_lambda|^2<=(a_L+C)(a_R+C)`,                      (16)

其中若需要可增大 `C` 使右侧两个因子为正。因此 `c_lambda=O(1)`。命题 EE
又有 `b_lambda=O(1)`，所以每个 separating pair 的
`r_h(2log lambda)=O(1)`。文档 031 定理 DY 的 Mellin 极点论证于是排除
所有 `Re rho>1/2` 的零点；函数方程排除左侧零点，得到 RH。`□`

EF 的条件远弱于完整 Weil 正性：它允许每个二维 block 有任意固定负下界，
也不控制边界空间之外的任何向量。移动端点把一个 off-center 零点放大为
`lambda^(2Re rho-1)`，所以仅仅防止二维最低本征值趋于 `-infinity` 已足够。

## 3. Besicovitch Gram 与非对角 Hodge 元

定义去掉有界几何项的中心化非对角元

`d_h(t)=c_(e^(t/2))-b_(e^(t/2))`.                    (17)

### 命题 EG（boundary Gram is the square of a Hodge matrix coefficient）

有精确恒等式

`d_h(t)=-r_h(t)`,                                    (18)

因此文档 032 的有限时间 Gram form 为

`G_T(h,k)=(1/T)int_0^T d_h(t)conjugate(d_k(t))dt`.   (19)

#### 证明

式 (18) 就是命题 EE 的式 (6)。代入文档 032 式 (4) 得式 (19)。`□`

这说明 Besicovitch--Hodge 空间不是另行添加的谱模型；它是有限 Weil
forms 的左右边界 off-diagonal matrix coefficients 的长期 Gram
完备化。

## 4. 一个显式 `2 x 2` Schur 终点

固定一对剖面，并取

`C>max(-a_L,-a_R)`.                                  (20)

### 推论 EH（finite determinant boundary certificate）

若对 separating 族中的每一对剖面都能选择固定 `C`，使所有充分大的
`lambda` 满足

`(a_L+C)(a_R+C)-|c_lambda|^2>=0`,                    (21)

则 RH 成立。

反之，RH 下可取 `C=0`，且式 (21) 是 Weil 正性的二维主子式。

#### 证明

在式 (20) 下，`M_lambda+C I>=0` 当且仅当其两个对角元非负且 determinant
非负；后者正是式 (21)。应用定理 EF。`□`

与文档 024 的 residual--Feshbach 证书相比，EH 不需要估计二维空间与其
正交补的耦合，因为它不试图证明完整 form 非负；移动边界块本身已经是
一个 separating RH detector。

## 5. 与 canonical compact Hodge defect 的连接

使用文档 029 的精确分解

`QW_lambda=Pcan_lambda-Vcan_lambda`.                 (22)

令 `X_lambda:C^2->H_lambda` 把标准基送到 `l_lambda,r_lambda`，并定义

`Pbd_lambda=X_lambda^*Pcan_lambda X_lambda`,

`Vbd_lambda=X_lambda^*Vcan_lambda X_lambda`.         (23)

### 命题 EI（canonical boundary compression）

有

`M_lambda=Pbd_lambda-Vbd_lambda`.                    (24)

对任意使 `Pbd_lambda+C I>0` 的固定 `C`，式 (15) 等价于二维
Birman--Schwinger 条件

`||(Pbd_lambda+C I)^(-1/2)Vbd_lambda`

`             (Pbd_lambda+C I)^(-1/2)||<=1`.         (25)

因此，若能对一个 separating 剖面族无条件证明式 (25) 的统一版本，RH
成立。

#### 证明

式 (24) 是式 (22) 的压缩。把
`M+C I=(Pbd+C I)-Vbd` 左右共轭于 `(Pbd+C I)^(-1/2)`，得到式 (25)。
再应用定理 EF。`□`

EI 把文档 029 的无限维 canonical defect 与文档 032 的边界 GNS 空间精确
接通：前者在移动二维边界通道上的压缩，正是后者的生成矩阵元。当前仍缺
的不是 residual tail，而是式 (21)/(25) 中对中心化 prime discrepancy 的
统一算术控制。

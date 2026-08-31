# Local Selberg Green block、Dirichlet inverse 与尺度 Markov gluing

文档 070 证明 sharp Selberg variance `V(X)=O(X^2)` 等价于 RH。本笔记把
每个 block 本身写成纯离散 Hodge structure。所有早于 `X` 的 Euler data 被
精确压缩为一个 scalar boundary state `A_X=psi(X)-X`；block 内部是 ordinary
line-graph Green/Laplacian pair。

所以跨乘法尺度的无限历史不是高维耦合：它只通过一个 prefix flux 传递。

## 1. Boundary-compressed local charges

令

`d_n=Lambda(n)-1`, `A_n=sum_(k<=n)d_k`.           (1)

对 integer `X>=1` 定义 length-`X` block charge

`q_1^[X]=A_X`,

`q_j^[X]=d_(X+j-1)`, `2<=j<=X`.                  (2)

令 local prefixes

`S_j^[X]=sum_(i<=j)q_i^[X]`.                      (3)

### 命题 MP（exact history compression）

有

`S_j^[X]=A_(X+j-1)`, `1<=j<=X`,                  (4)

从而 step Selberg variance

`V_step(X)=int_X^(2X)|psi(x)-floor(x)|^2dx`

`          =sum_(j=1)^X|S_j^[X]|^2`.              (5)

#### 证明

式 (4) 对 `j=1` 是定义；每增加一个 `j` 就加入下一个 charge
`d_(X+j-1)`，故 induction 成立。在 `[n,n+1)` 上 step discrepancy 等于
`A_n`；取 `n=X,...,2X-1` 给式 (5)。`□`

所以所有 indices `<X` 的 effect 只剩 `A_X`，没有遗漏的高维 boundary data。

## 2. Reverse Brownian Green matrix

令 `L_X` 为 ordinary prefix matrix，并定义

`K_X=L_X^*L_X`.                                   (6)

### 定理 MQ（local Green/Laplacian pair）

对 `1<=i,j<=X`，

`K_X(i,j)=X-max(i,j)+1`.                          (7)

它 positive definite，`detK_X=1`。其 inverse

`J_X=K_X^(-1)=B_XB_X^*`,                          (8)

其中 `B_X=L_X^(-1)` 是 first-difference matrix，并且

`<u,J_Xu>=sum_(j=1)^(X-1)|u_j-u_(j+1)|^2+|u_X|^2`. (9)

若 `B(s)` 是 standard Brownian motion，令

`Y_j=B(X-j+1)`，                                  (10)

则 `E[Y_iY_j]=K_X(i,j)`。

#### 证明

charge pair `(i,j)` 同时出现在 prefixes `k>=max(i,j)`，其个数是式 (7)。
factorization (6) 给 positivity 与 determinant。取 inverse 得式 (8)，展开
`B_X^*u` 给式 (9)。Brownian covariance
`min(X-i+1,X-j+1)=X-max(i,j)+1` 给式 (10)。`□`

这是文档 069 power max-kernel 的 local unweighted analogue；方向反转来自
block energy 向右端累计。

## 3. 最优 local Hodge--Sobolev inequality

### 定理 MR（Selberg variance is the optimal local constant）

对 block charge (2)，以下 inequality 对所有 `u in C^X` 成立：

`|A_Xconjugate(u_1)`

` +sum_(n=X+1)^(2X-1)d_nconjugate(u_(n-X+1))|^2`

` <=V_step(X){sum_(j<X)|u_j-u_(j+1)|^2+|u_X|^2}`. (11)

而 `V_step(X)` 是最小可能常数。等号 test vector 是

`u=K_Xq^[X]` 的 scalar multiples。

#### 证明

命题 MP 与式 (6) 给

`V_step(X)=<q^[X],K_Xq^[X]>`.                     (12)

对 pair `K_X,J_X` 应用定理 MF 的 Green--Dirichlet duality，得到式 (11)、
optimality 与 equality case。`□`

左侧把 boundary prime discrepancy 与 block 内 centered primes 保留在同一个
functional；分别取绝对值会破坏 sharp cancellation。

## 4. Sharp local Hodge--Riemann RH theorem

### 定理 MS（uniform local Sobolev criterion for RH）

以下条件等价：

1. RH；
2. 存在 `C`，使所有 integer `X>=2` 与全部 `u in C^X` 满足

   `|<q^[X],u>|^2<=CX^2<u,J_Xu>`；                (13)

3. local Euler functionals 的 optimal constants 满足

   `C_X^opt=O(X^2)`。                              (14)

并且

`C_X^opt=V_step(X)`.                              (15)

若 `Theta>1/2`，则

`limsup_(X->infinity)log C_X^opt/logX=2Theta+1`;  (16)

一般地 RH 等价于 normalized constants `C_X^opt/X^2` uniformly bounded。

#### 证明

定理 MR 给式 (15)。step/smooth discrepancy 的 difference 在 `[X,2X]`
有 squared norm `O(X)`，所以文档 070 定理 ML 把 RH 等价于
`V_step(X)=O(X^2)`，得到 1–3。文档 042 定理 GA 与相同 step/smooth
comparison 给 off-center exponent式 (16)。`□`

式 (13) 是 local finite Hodge--Riemann inequality；其 target constant
`X^2` 正是中心 weight，而不是带任意 `X^epsilon` 的松弛。

## 5. Dyadic state transfer 与 Markov gluing

### 命题 MT（one-dimensional scale boundary state）

block `X` 的 output prefix 满足

`A_(2X-1)=sum_(j=1)^Xq_j^[X]`.                    (17)

下一 dyadic block 的 boundary input 是

`q_1^[2X]=A_(2X)=A_(2X-1)+d_(2X)`.               (18)

因此从 scale `X` 到 `2X`，过去全部 Euler history 只经 scalar state
`A_(2X)` 传递；其余 coordinates 是新 block charges。

此外 global prefix Hodge energy 有 exact gluing

`P(2^J)=sum_(k=0)^(J-1)`

` sum_(n=2^k)^(2^(k+1)-1)|A_n|^2/[n(n+1)]`.      (19)

#### 证明

式 (17) 是 local prefix 的末值；再加入 `d_(2X)` 给式 (18)。式 (19) 是
整数 edges 的 dyadic partition，亦即文档 070 命题 MM。`□`

这个 Markov property 给可能的 induction/renormalization 路线：每个新 block
只需控制一个 inherited boundary flux 与 fresh centered Euler charges 的联合
local Sobolev norm。

## 6. General Gamma--Euler local Hodge theorem

### 定理 MU（general local Green-block centerline theorem）

考虑文档 070 定理 MO 的中心 `c/2` Gamma--Euler data。令 discrete centered
charges 为 `d_n`、prefixes 为 `A_n`。固定 integer ratio `A>=2`；在 block
`[X,AX)` 中把 past history 压成 first coordinate `A_X`，其后列出 fresh
charges。对应 local prefix matrix `L_(X,A)` 与 Green matrix
`K_(X,A)=L^*L` 均 positive，inverse 是 ordinary Dirichlet difference form。

若 local divisor count hypotheses 成立，则 centerline property 等价于所有
这些 local functionals 满足

`|<q^[X,A],u>|^2<=C_A X^(c+1)<u,J_(X,A)u>`       (20)

对全部 finite `u` uniformly in `X`。optimal constant 恰为 step Selberg
variance

`int_X^(AX)|E_(Z,step)(x)|^2dx`.                  (21)

#### 证明

命题 MP–定理 MR 只使用 prefix algebra，对任意 centered charges 与任意
integer block length 成立。定理 MO 对 fixed `A>=2` 把 centerline 等价于
式 (21) 的 `O_A(X^(c+1))` bound，所以得到式 (20)。
`□`

## 7. 存在性边界

对 zeta，每个 local Green matrix、inverse Laplacian、boundary compression、
Brownian covariance 与 optimal variational identity 都无条件存在。唯一未证
的是式 (13) 的 sharp `CX^2` constant。该 formulation 把潜在证明缩成一列
local finite inequalities，并表明跨尺度 residual 只有 rank-one scalar state；
但控制该 state 与 fresh primes 的联合 norm 仍具有 RH 的全部强度。

文档 072 对此 block 作 exact Schur elimination：constant mode 是一个
triangular rank-one detector，orthogonal remainder 是 Brownian bridge；在
zeta/Gamma--Euler divisor hypotheses 下，sharp scalar bound 会经中心线判据
自动补全为这里的 full local inequality。

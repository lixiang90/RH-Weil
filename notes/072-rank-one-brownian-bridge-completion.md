# Rank-one block mean、Brownian bridge 与 Hodge completion

文档 071 把 sharp Selberg variance 写成 finite Green--Dirichlet optimal
constant。本笔记对这个 Green block 做一次 exact Schur elimination。结果是：

- past Euler history 只出现在一个 rank-one constant mode；
- orthogonal remainder 是只依赖 fresh charges 的 Brownian-bridge energy；
- 对 zeta，rank-one mode 单独已有完整 RH 强度，而且在 RH 下达到无
  `epsilon` 的 endpoint bound；
- 在标准 Gamma--Euler hypotheses 下，同一 scalar bound 会自动补全为 full
  local Hodge inequality。

## 1. Constant mode 与 bridge 的正交分解

沿用文档 071 的 length-`X` charge `q=q^[X]`、prefix matrix `L_X` 与

`y=L_Xq=(A_X,A_(X+1),...,A_(2X-1))^T`.             (1)

定义

`T_X=sum_(n=X)^(2X-1)A_n`, `barA_X=T_X/X`,          (2)

`R_X=|T_X|^2/X`,                                   (3)

`W_X=sum_(n=X)^(2X-1)|A_n-barA_X|^2`.              (4)

### 定理 MV（exact scalar--bridge Hodge splitting）

step Selberg energy 有 orthogonal decomposition

`V_step(X)=R_X+W_X`.                               (5)

令 `e_1=(1,0,...,0)^T`、`K_X=L_X^*L_X`，并置

`v_X=K_Xe_1=(X,X-1,...,1)^T`.                      (6)

则

`K_X^sc=v_Xv_X^*/X`, `K_X^br=K_X-K_X^sc`           (7)

均 positive semidefinite，ranks 分别为 `1` 与 `X-1`，且

`R_X=<q,K_X^scq>`, `W_X=<q,K_X^brq>`.              (8)

#### 证明

在 observation space `C^X` 中，把 `y` 正交投影到 constant vector
`1_X` 及其 orthogonal complement：

`||y||^2=|<1_X,y>|^2/X+||y-barA_X1_X||^2`.         (9)

这就是式 (5)。又 `L_Xe_1=1_X`，所以把两个 observation-space
projections 拉回 charge space，得到式 (6)–(8)。`□`

因此 rank-one part 不是任意挑出的 detector，而是 local Hodge polarization
的 canonical constant-mode summand。

## 2. Schur complement 是 Brownian bridge

写 fresh charges

`g_i=d_(X+i)`, `1<=i<=X-1`.                       (10)

相对于 `q=(A_X,g)`，Green matrix 的 block form 是

`K_X=[[X,r^*],[r,K_ff]]`, `r_i=X-i`.               (11)

### 定理 MW（Brownian-bridge Schur complement）

消去 boundary state `A_X` 后的 Schur complement 为

`C_X=K_ff-rr^*/X`,                                 (12)

且对 `1<=i,j<=X-1`，

`C_X(i,j)=min(i,j)[X-max(i,j)]/X`.                 (13)

它 positive definite、`detC_X=1/X`，并且

`C_X^(-1)=D_X`,                                    (14)

其中 `D_X` 是 diagonal 为 `2`、相邻 off-diagonal 为 `-1` 的 ordinary
Dirichlet Laplacian。进一步，

`W_X=<g,C_Xg>`.                                    (15)

若 `B(t)` 是 Brownian motion，则

`Z_i=B(i)-(i/X)B(X)`                               (16)

满足 `E[Z_iZ_j]=C_X(i,j)`。

#### 证明

式 (11) 由 `K_X(i,j)=X-max(i,j)+1` 直接读出。若 `i<=j`，则

`X-j-(X-i)(X-j)/X=i(X-j)/X`，得到式 (13)。这是式 (16) 的标准
covariance；其 inverse 是带左右 Dirichlet boundary 的 path Laplacian。
也可直接相乘验证式 (14)。由 `detK_X=1` 与 block determinant formula 得
`detC_X=1/X`。最后，对 fixed fresh charges 最小化

`sum_(r=0)^(X-1)|a+sum_(i<=r)g_i|^2`               (17)

时 `a=-X^(-1)sum_rsum_(i<=r)g_i`，最小值同时等于式 (4) 与
`<g,C_Xg>`，证明式 (15)。`□`

特别地，past history `A_X` 从 bridge part 完全消失；它只通过 scalar mean
`barA_X` 影响 full block。

## 3. 与 triangular Riesz detector 的精确连接

令文档 044 的 smooth triangular coefficient 为

`mathcal A(X)=int_X^(2X)[psi(x)-x]dx`.              (18)

### 命题 MX（finite scalar projection formula）

对 integer `X>=1`，

`T_X=X A_X+sum_(i=1)^(X-1)(X-i)d_(X+i)`,           (19)

并且

`mathcal A(X)=T_X-X/2`.                            (20)

#### 证明

每个 fresh charge `d_(X+i)` 出现在后面 `X-i` 个 prefixes，得到式 (19)。
在 `[n,n+1)` 上

`psi(x)-x=A_n-(x-n)`.                              (21)

积分给 `A_n-1/2`，再对 `n=X,...,2X-1` 求和即得式 (20)。`□`

所以文档 044 的 signed triangular detector，平方并除以 `X` 后，正是
local Green polarization 的 canonical rank-one summand，差异只有显式 Tate
项 `X/2`。

## 4. Epsilon-free rank-one RH criterion

### 定理 MY（rank-one local Hodge criterion for RH）

以下条件等价：

1. RH；
2. `mathcal A(X)=O(X^(3/2))`；
3. 对 integer `X>=2`，`T_X=O(X^(3/2))`；
4. `R_X=O(X^2)`；
5. 文档 071 的 full optimal constants 满足 `C_X^opt=O(X^2)`。

因此仅检查 full local Hodge form 的一个 canonical rank-one projection，已经
足以推出全部 local inequalities。

#### 证明

RH 与 5 的 equivalence 是文档 071 定理 MS。由式 (5)，5 推出 4，再由
式 (3) 得 3。式 (20) 给 2 与 3 的 equivalence；从 integer 到 real `X`
只产生 `O(X logX)` 的 unit-scale variation，而这低于 `X^(3/2)`，也可直接
使用文档 044 的 continuous formula。条件 2 显然蕴含文档 044 定理 GL 的
`O_epsilon(X^(3/2+epsilon))`，故推出 RH。

反向的关键 endpoint strengthening 是：RH 下文档 070 定理 ML 给
`V_step(X)=O(X^2)`；Cauchy--Schwarz 或式 (5) 给

`|T_X|^2<=X V_step(X)=O(X^3)`,                     (22)

再用式 (20) 得 2–4。`□`

这里的 `rank-one => full` 不是一般 Hilbert-space 事实。它使用 triangular
Mellin multiplier 对全部非平凡 zeros 无消失，从 scalar bound 先推出 RH，
再由 RH 的 uniform local `L^2` 补回 Brownian-bridge remainder。

## 5. Polynomial exponent saturation

令

`Theta=sup_rho Re rho`.                            (23)

### 定理 MZ（rank-one projection retains the full zero exponent）

对 zeta，

`limsup_(X->infinity) log max(1,|T_X|)/logX=Theta+1`, (24)

从而

`limsup_(X->infinity) log max(1,R_X)/logX=2Theta+1`. (25)

这与文档 071 定理 MS 的 full optimal constant exponent 完全相同。

#### 证明

标准 finite-order explicit formula 给任意 `epsilon>0` 下
`mathcal A(X)=O_epsilon(X^(Theta+1+epsilon))`。反向地，文档 044 命题 GK
表明其 Mellin transform 在每个 zero `rho` 有非零 residue；若 growth
abscissa 小于 `Re rho+1`，该 transform 会在 `rho` 解析，矛盾。对 zeros
取 supremum 得 continuous `mathcal A` 的 exponent 为 `Theta+1`。

Chebyshev bound 给 `mathcal A` 在 unit interval 上 variation 为
`O(X logX)`；因 `Theta>=1/2`，integer sampling 不改变 exponent。式 (20)
中的 `X/2` 同样是 lower order，于是得到式 (24)，再由式 (3) 得式 (25)。
`□`

Polynomial exponent 相同不意味着任意序列上 scalar bound 控制 full norm；
这里精确 endpoint `O(X^2)` 的 completion 仍依赖定理 MY 的 divisor argument。

## 6. General Gamma--Euler rank-one completion theorem

固定 `A>1`。对中心 `c/2` 的 Gamma--Euler discrepancy `E_Z(x)` 定义

`S_(Z,A)(X)=int_X^(AX)E_Z(x)dx`,                   (26)

`R_(Z,A)(X)=|S_(Z,A)(X)|^2/[(A-1)X]`.             (27)

### 定理 NA（rank-one-to-full centerline structure theorem）

假设：

1. divisor 关于 `Re s=c/2` 对称，并位于 `Re s>-1` 的标准非平凡条带；
2. Euler/Mellin explicit formula 与 finite-order growth 足以作一次 Riesz
   transform；
3. 文档 070 定理 MO 的 local divisor-count hypotheses 成立。

则以下条件等价：

1. 全部非平凡 divisor 位于 `Re s=c/2`；
2. `S_(Z,A)(X)=O_A(X^(c/2+1))`；
3. `R_(Z,A)(X)=O_A(X^(c+1))`；
4. full local Selberg/Hodge constants 为 `O_A(X^(c+1))`。

若 `Theta_Z` 是最右 divisor 横坐标，则 scalar amplitude 与 energy 的
polynomial exponents 分别为 `Theta_Z+1` 与 `2Theta_Z+1`。

#### 证明

centerline 下定理 MO 给

`int_X^(AX)|E_Z(x)|^2dx=O_A(X^(c+1))`.             (28)

Cauchy--Schwarz 给 2，且 2 与 3 等价。反之，一次 Riesz transform 对
divisor mode `x^rho` 的 multiplier 为

`[A^(rho+1)-1]/(rho+1)`.                           (29)

其 zeros 全在 `Re rho=-1`，故在假设 1 的 divisor strip 无消失。条件 2
使 Mellin transform 在 `Re s>c/2` 解析，排除右侧 divisor；对称性排除
左侧。于是 2 推出 1，再由定理 MO 得 4。4 推 3 是 constant-mode
Cauchy--Schwarz。相同的 Mellin abscissa argument 给两个 exact exponents。
`□`

## 7. 存在性边界

对 zeta，`K_X^sc`、Brownian-bridge kernel、Dirichlet inverse、finite scalar
prime formula 与 orthogonal splitting 全部无条件存在。未证的是
`R_X=O(X^2)`；定理 MY 证明它已经与 RH 等价，不能由 rank reduction 本身
获得。

这个分解仍带来结构上的实质收缩：若尝试从 primes 建立 full local Hodge
positivity，不必同时估计 inherited history 与 internal fluctuation。past
history 只进入一个 scalar triangular channel；fresh charges 的 remainder
是一个两端 Dirichlet Brownian bridge。任何未来的 induction、large sieve
或 renormalization 证明都可以分别针对这两个正交 channels，再用式 (5)
无损拼合。

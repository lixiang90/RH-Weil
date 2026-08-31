# Dual Jacobi Laplacian、最优 Hodge--Sobolev 不等式与 RH

文档 068 把 centered Euler charges 的临界能量写成 finite max Green kernel。
本笔记求出该 kernel 的精确 inverse：一个 weighted tridiagonal Dirichlet
Laplacian。由此 RH 等价于一族完全有限、常数最优的 prime--Tate
Hodge--Sobolev inequalities。

这把“实际 arithmetic vector 的 Rayleigh bound”转成更接近 Weil
Hodge-index 论证的 dual 形式：Euler divisor 对任意有限 test cochain 的 pairing
由 test cochain 的 Dirichlet intersection energy 控制。

## 1. Max Green kernel 的精确逆

固定 `c>0`、size `N`。沿用

`w_n=[n^(-c)-(n+1)^(-c)]/c`,                      (1)

`K_N(m,n)=[max(m,n)^(-c)-(N+1)^(-c)]/c`.         (2)

令 `L` 是 prefix matrix

`L_(n,k)=1_(k<=n)`，                              (3)

并令 `B=L^(-1)`，即

`(Bx)_1=x_1`, `(Bx)_n=x_n-x_(n-1)`.              (4)

### 定理 ME（exact inverse weighted Laplacian）

有

`K_N=L^*WL`, `W=diag(w_1,...,w_N)`,               (5)

以及

`J_N=K_N^(-1)=B W^(-1)B^*`.                      (6)

其 quadratic form 为

`<u,J_Nu>=sum_(n=1)^(N-1)|u_n-u_(n+1)|^2/w_n`

`                              +|u_N|^2/w_N`.      (7)

并且

`det K_N=product_(n=1)^Nw_n`,

`det J_N=product_(n=1)^Nw_n^(-1)`.                (8)

#### 证明

定理 LZ 已给式 (5)。因所有 `w_n>0` 且 `L` unit lower triangular，`K_N`
positive definite。取 inverse 得式 (6)。展开 `B^*u`：其前 `N-1` 个
coordinates 为 `u_n-u_(n+1)`，末 coordinate 为 `u_N`，给式 (7)。
`detL=1` 给式 (8)。`□`

对 zeta 的 `c=1`，

`w_n=1/[n(n+1)]`,                                 (9)

所以 dual conductances 恰为 `n(n+1)`。

## 2. 最优 dual Hodge inequality

### 定理 MF（optimal Green--Dirichlet duality）

对任意 charge vector `d in C^N`，令

`P_N(d)=<d,K_Nd>`.                                (10)

则 `P_N(d)` 是以下 inequality 的最小可能常数：

`|<d,u>|^2<=P_N(d)<u,J_Nu>` 对全部 `u in C^N`。 (11)

等号在 `u=K_Nd` 的 scalar multiples 处取得。等价地，

`P_N(d)=sup_u!=0 |<d,u>|^2/<u,J_Nu>`             (12)

` =sup_u {2Re<d,u>-<u,J_Nu>}`。                  (13)

#### 证明

在 inner product `<u,v>_J=<u,J_Nv>` 中，functional
`u-><d,u>` 的 Riesz vector 是 `K_Nd`，因为 `J_NK_N=I`。Cauchy--Schwarz
给式 (11)，并在 stated vector 取等。完成平方给式 (13)。`□`

所以 prefix Hodge energy 不是某个粗上界，而是 centered Euler functional 的
精确 negative-Sobolev norm squared。

## 3. Zeta 的 finite Hodge--Sobolev RH criterion

对 size `N` 令

`d_n=Lambda(n)-1`, `1<=n<=N`.                     (14)

### 定理 MG（prime--Tate Sobolev inequality iff RH）

以下条件等价：

1. RH；
2. 存在 absolute `C`，使每个 `N>=2`、每个 `u in C^N` 满足

   `|sum_(n<=N)(Lambda(n)-1)conjugate(u_n)|^2`

   ` <=C log(N+1){sum_(n<N)n(n+1)|u_n-u_(n+1)|^2`

   `                         +N(N+1)|u_N|^2}`；   (15)

3. 式 (15) 的最优常数 `C_N^opt` 满足 `(N+1)^(o(1))`。

更精确地，

`C_N^opt=P(N+1)`                                  (16)

且

`limsup_(N->infinity)log C_N^opt/logN`

`                         =max(0,2Theta-1)`.       (17)

RH 下还有

`C_N^opt/logN->sum_gamma m_gamma^2/|rho|^2`.      (18)

#### 证明

定理 MF 与式 (7)、(9) 说明式 (15) 的 optimal constant 是
`<d,K_Nd>`。文档 068 定理 LZ/MA 把它识别为 `P(N+1)`，并给式 (17) 及
RH 等价；定理 MC 给式 (18)。`□`

这是一条纯有限不等式：左侧是 prime divisor 减 Tate divisor 对 test
cochain 的 pairing，右侧是显式 local Dirichlet energy，不含零点或解析延拓。

## 4. Brownian Green realization

### 命题 MH（Brownian covariance model）

令

`x_n=1/(c n^c)`，                                  (19)

并取 standard Brownian motion `B(x)`。定义

`X_n=B(x_n)-B(x_(N+1))`, `1<=n<=N`.               (20)

则

`E[X_mX_n]=K_N(m,n)`.                             (21)

因此

`P_N(d)=E|sum_(n<=N)d_nX_n|^2`.                  (22)

#### 证明

`x_n` 随 `n` 递减，而 Brownian covariance 是
`E[B(s)B(t)]=min(s,t)`。两个从 `x_(N+1)` 出发的 increments 的 covariance
为

`min(x_m,x_n)-x_(N+1)`

` =[max(m,n)^(-c)-(N+1)^(-c)]/c`，

即式 (2)。展开 variance 给式 (22)。`□`

这不是随机证明 RH；它说明 finite Hodge polarization 已有 canonical Gaussian
intersection model。缺少的是特定 arithmetic charge 在该 covariance 中的
临界 norm bound。

## 5. 与 Weil 的 Hodge-index 模式

有限域曲线的 RH 证明把 correspondence 的 trace pairing 置于一个具有负定
primitive part 的 intersection form 中，再用 Hodge index 控制 eigenvalues。
当前 finite number-field analogue 可压缩为：

- Euler--Tate divisor：`d_n`；
- primitive potential/flow：`A=Ld`；
- positive Green polarization：`K=L^*WL`；
- dual intersection form：`J=B W^(-1)B^*`；
- Hodge--Riemann input：式 (15) 的 `O(logN)` optimal constant。

前四项对 zeta 无条件存在。第五项由定理 MG 与 RH 等价，不能从矩阵正性本身
推出；generic charges 的 optimal constant 可远大于 `logN`。

## 6. General Gamma--Euler dual Hodge theorem

### 定理 MI（general dual divergence--Hodge centerline theorem）

在定理 MD 的 hypotheses 下，取 centered charges `d_1,...,d_N`，并定义
weights (1)。则全部 finite Green matrices `K_N` 与 dual Jacobi forms `J_N`
无条件存在且 positive definite。令

`C_(Z,N)^opt=sup_(u!=0)`

` |sum_(n<=N)d_n conjugate(u_n)|^2`

` /{sum_(n<N)|u_n-u_(n+1)|^2/w_n+|u_N|^2/w_N}`. (23)

则

`C_(Z,N)^opt=sum_(n=1)^Nw_n|sum_(k<=n)d_k|^2`,   (24)

并且

`limsup_(N->infinity)log C_(Z,N)^opt/logN`

`                         =max(0,2Theta-c)`.       (25)

所以全部 divisor 位于 `Re rho=c/2` 当且仅当

`C_(Z,N)^opt=O(logN)`，                            (26)

也当且仅当 `C_(Z,N)^opt=N^(o(1))`。centerline critical trace square
summable 时，这些 optimal constants 除以 `logN` 收敛到相应 divisor spectral
mass，并由 prefix GNS 产生 `Theta_op*=c-Theta_op`。

#### 证明

定理 ME–MF 给式 (23)–(24)。定理 MD 给 exponent、centerline equivalence
与 GNS statement。`□`

## 7. 存在性边界

对 zeta，finite dual Laplacian、determinant、Brownian covariance、最优
variational identity 与 prime--Tate pairing 全部无条件构造。未证的是式
(15) 的 uniform `C logN` constant。与先前表述相比，这一形式允许直接尝试
Sobolev、large-sieve、transport 或 intersection-theoretic 方法，而不必操作
零点或无限 RKHS completion。

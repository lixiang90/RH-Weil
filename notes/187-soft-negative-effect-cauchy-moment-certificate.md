# Soft negative effect、Chebyshev orbit moments 与有限 Cauchy 证书

文档 186 证明低 degree universal word effects无法捕获任意 negative level set。
本笔记换一个方向：不逼近未知 level set 的几何位置，而对 current 本身作一个
canonical one-sided functional calculus。对 `rho>0` 定义

`a_rho(x)=(-x)_+/[(-x)_+ +rho]`.                 (1)

`a_rho(X)` 是一个不读取 eigenvectors 的 canonical contraction；它的 square
response以统一 additive `2rho` error恢复全部 negative trace。再在已知 spectral
interval 上用 universal Chebyshev polynomial逼近 `a_rho`，便把 Hodge index
化成有限个 current moments。对 stationary zeta orbit symbol，这些 moments由
Cauchy characteristic function精确展开为有限 lag-resonance sums，不引用 zeros。

这给出一条新的 constructive/nonconstructive bridge：spectral effect 的存在由
functional calculus自动保证，而真正算术任务变成控制一个明确的 finite
Chebyshev convolution response。

## 1. Canonical soft negative effect

令 `(M,tau)` 是 finite tracial von Neumann algebra，`tau(1)=1`，
`X=X^* in L^1(M,tau)`。令

`A_rho=a_rho(X)=X_-(X_-+rho I)^(-1)`.            (2)

这里 inverse在 `supp(X_-)` 上取，正谱 sector 上定义为零。

### 定理 AGA（soft negative-index sandwich）[U]

`A_rho` 是 positive contraction，并且

`-tau(XA_rho^2)<=tau(X_-)`

` <=-tau(XA_rho^2)+2rho`.                        (3)

#### 证明

在 spectral value `x=-y<0` 上，soft response为

`y[y/(y+rho)]^2`.                                (4)

其与 `y` 的差为

`y-y^3/(y+rho)^2`

` =rho*t(2t+1)/(t+1)^2`, `t=y/rho`,             (5)

而 `0<=t(2t+1)/(t+1)^2<=2`。正谱上 `A_rho=0`。对 spectral
measure积分并用 `tau(supp X_-)<=1` 即得式 (3)。`square`

与 hard projection `1_(X<0)` 相比，`A_rho` 在零点连续且 `1/rho`-Lipschitz，
所以可以作不依赖 spectral gaps 的 uniform polynomial approximation。

## 2. Polynomial square certificate

假设 `||X||<=B`。令 real polynomial `p` 在 `[-B,B]` 上满足

`||p-a_rho||_infinity<=epsilon<=1`.             (6)

置

`b=p/(1+epsilon)`,                               (7)

则 `||b(X)||<=1`。

### 定理 AGB（finite polynomial Hodge-index certificate）[U]

有

`tau(X_-)`

` <=-tau[Xb(X)^2]+2rho+5epsilon*tau(|X|)`.       (8)

#### 证明

由式 (6)--(7)，在 `[-B,B]` 上 `|b|<=1`，并且

`|b^2-a_rho^2|<=5epsilon`.                       (9)

functional calculus 与 trace Hölder inequality 给

`|tau[X(b(X)^2-A_rho^2)]|`

` <=5epsilon tau(|X|)`.                          (10)

与定理 AGA 合并即得式 (8)。`square`

因为 `a_rho` 的 Lipschitz constant至多 `1/rho`，Jackson approximation theorem
给某个 universal `C_J`，使 degree `L` 可取

`epsilon<=C_J B/(rho L)`.                        (11)

这个 rate 未必足够共尾可和，但它不需要 zero-free region 或 spectral gap。

## 3. Shifted Hankel moment form

写

`b(x)=sum_(j=0)^L c_jx^j`, `m_k=tau(X^k)`.       (12)

则式 (8)的唯一 signed response为

`-tau[Xb(X)^2]`

` =-sum_(i,j=0)^L conjugate(c_i)c_jm_(i+j+1)`.  (13)

即 shifted Hankel matrix

`H_L^shift=(m_(i+j+1))_(0<=i,j<=L)`             (14)

在 canonical coefficient vector `c` 上的负 quadratic response。与文档 185
的 full noncommutative word matrix不同，这里只需 current自身生成的 commutative
polynomial algebra和一个指定 vector。

### 推论 AGC（soft-moment bounded-index criterion）[C]

对 cofinal finite currents `(X_n,tau_n)`，若有 arithmetic bounds `B_n>=||X_n||`，
选择 `rho_n>0`、degree `L_n` universal approximants `b_n` 及 certified errors
`epsilon_n`，并且

`sup_n{-tau_n[X_nb_n(X_n)^2]`

`       +2rho_n+5epsilon_n tau_n(|X_n|)+eta_n}<infinity, (15)

其中 `eta_n` 是 explicit-formula approximation ledger，则目标 divisor满足
bounded finite-trace Hodge--Weil theorem，因而全部非零 zeros 位于中心线。

式 (15) 没有假设 `X_n>=0`，允许深而窄的 negative wells；它直接控制文档 149
所需的规范 negative spectral mass。

## 4. Exact stationary Cauchy moments

令 finite real stationary symbol 写为

`P(t)=sum_(omega in Omega)d_omega exp(-i omega t)`, (16)

其中 `d_(-omega)=conjugate(d_omega)`。取 normalized Cauchy measure

`dmu(t)=dt/[pi(1+t^2)]`.                         (17)

其 characteristic function为

`int exp(-iut)dmu(t)=exp(-|u|)`.                 (18)

### 定理 AGD（finite lag-resonance moment formula）[U]

对每个 integer `k>=0`，

`m_k=int P(t)^k dmu(t)`

` =sum_(omega_1,...,omega_k in Omega)`

`   d_(omega_1)...d_(omega_k)`

`   *exp(-|omega_1+...+omega_k|)`.               (19)

空 tuple给 `m_0=1`。

#### 证明

有限展开 `P^k`，逐项使用式 (18)。`square`

对 Abel-truncated zeta current，frequencies是 `log n` 及其 negatives，
coefficients由 prime、continuum 与 Gamma finite approximation共同给出。因此式
(19) 是完全 arithmetic 的 near-product resonance sum：

`omega_1+...+omega_k approx 0`                   (20)

等价于相应 products近乎相等。这里没有使用 zeros；困难是 tuple multiplicity与
cancellation，而不是公式存在性。

## 5. Chebyshev lag-convolution form

高 degree 时把 Chebyshev approximant转换到 monomial coefficients 会造成巨大
cancellation。有限实验在 degree `32--48` 已出现 power-basis Hankel evaluation
失稳，而 Chebyshev evaluation保持稳定。因此正式证书应在 orbit algebra 中直接
使用三项递推。

令 `Q_0(t)=1`,`Q_1(t)=P(t)/B`，并定义

`Q_(k+1)=2(P/B)Q_k-Q_(k-1)`.                     (21)

则 `Q_k=T_k(P/B)`。若 `q_k(u)` 是 `Q_k` 的 finite frequency coefficients，
式 (21) 等价于 exact convolution recursion

`q_(k+1)=2B^(-1)(d*q_k)-q_(k-1)`.               (22)

对 Chebyshev approximant

`b(P)=sum_(k=0)^L alpha_kQ_k/(1+epsilon)`,       (23)

令合成 frequency coefficients为 `beta_u`。则

`-int P(t)|b(P(t))|^2dmu(t)`

` =-sum_(omega,u,v)d_omega beta_u conjugate(beta_v)`

`       *exp(-|omega+u-v|)`.                    (24)

式 (22)--(24) 是比式 (13) 数值和结构上更合适的 arithmetic certificate：它保留
Chebyshev conditioning，并直接暴露 near-product resonance。

## 6. Constructive/nonconstructive meaning

### 非构造部分

`A_rho` 对每个 current自动存在；不需要显式 spectral projector。Stone--Weierstrass
或 Jackson theorem保证 finite polynomial squares逼近它。因此“存在一族能 norm
negative trace 的算术 effects”在把 current本身允许为 generator 后得到无条件
答案。

### 构造部分

对 finite zeta approximants，`P`、`B`、Chebyshev coefficients、lag convolution
和 Cauchy kernel全部由 Euler/Gamma data显式给出。若能不用 zeros证明式 (24)
加 approximation errors一致有界，就得到原 RH/GRH 的 bounded Hodge index。

### 循环性审计

以下做法没有产生新证明：

- 用 diagonalization 后已知的 negative eigenvalues选择 interpolation polynomial；
- 直接数值计算式 (24) 并把有限尺度有界外推到 cofinal limit；
- 以完整 Selberg profile或等价 RH 的 near-product bound控制所有 tuples；
- 忽略 `epsilon tau(|X|)` 或 power/Chebyshev basis conditioning。

真正可能的新输入是对 canonical coefficient vector `alpha` 的 response-specific
convolution bound；它比控制所有 degree-`L` moments或全部 word matrix更窄。

## 7. 下一最小引理

在 actual balanced prime--continuum symbol 上实现式 (22)--(24)，并分解：

1. exact product tuples `omega+u-v=0`；
2. near-product tuples `0<|omega+u-v|<=1`；
3. far tuples，由 `exp(-|.|)` 衰减；
4. Gamma/continuum cross terms；
5. Chebyshev recurrence 中 coefficient `L1/L2` growth。

首先测试 canonical `alpha` 是否比 arbitrary moment directions显著降低 resonance
amplification。若没有，就把该路线归约到文档 178/169 已知 occupancy/RH barrier；
若有，再寻找 response-specific large-sieve或 Hodge pairing。

## 8. 审计结论

本笔记给出一个新的广义结构接口：任意 finite tracial current 的 negative index
都由单个 canonical soft polynomial square在显式误差内控制；对 stationary
Cauchy zeta currents，该 response又有完全有限、无零点输入的 lag-resonance
展开。剩余问题从“构造未知负谱投影”缩为“控制一个指定 Chebyshev convolution
方向”，同时明确保留了 conditioning与 near-product障碍。


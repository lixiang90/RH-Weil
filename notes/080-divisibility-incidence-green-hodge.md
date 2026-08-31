# Divisibility incidence differential 与 Möbius Green--Hodge 结构

文档 079 证明 pure prime-local normal determinant limit 不可能产生 global
zeta zeros。本节构造所要求的最小非局部对象：由整除关系给出的 Dirichlet
convolution differential。它无条件混合任意多个素因子，其 inverse propagator
正是 reciprocal `L`-coefficients。中心线随后等价于一个完全有限、正的
rank-one Green--Hodge 能量具有零 Lyapunov exponent。

## 1. 有限整除 incidence differential

令

`L(s)=sum_(n>=1)a(n)n^(-s)`,  `a(1)=1`,                (1)

并令 Dirichlet inverse `b` 满足

`a*b=delta_1`,  `1/L(s)=sum_(n>=1)b(n)n^(-s)`          (2)

（先在绝对收敛半平面理解）。对 `1<=d,n<=N` 定义

`C_(a,N)(n,d)=a(n/d)` if `d|n`, else `0`.              (3)

把 `C_(a,N):C_N^0 -> C_N^1` 看作一个 finite arithmetic differential。

### 定理 OU（finite Dirichlet inversion）

`C_(a,N)` 为 lower triangular、对角元全为一，而且

`C_(a,N)^(-1)=C_(b,N)`.                                (4)

特别地所有 finite complexes 都 acyclic 且 determinant 为一；但 inverse 的
第一列是

`C_(a,N)^(-1)e_1=(b(1),...,b(N))^T`.                   (5)

#### 证明

矩阵乘积的 `(n,d)` 元为

`sum_(d|m|n)a(n/m)b(m/d)=(a*b)(n/d)`.                  (6)

它在 `n=d` 为一，其余为零，故得式 (4)；其余结论立即成立。`□`

对 zeta，`a(n)=1,b(n)=mu(n)`，所以 `C_a` 是 divisibility-poset 的 zeta
incidence matrix，`C_b` 是 Möbius matrix。与独立 prime blocks 不同，
`C_a(n,d)` 已在单个矩阵内连接所有复合整数及其全部素因子。

## 2. Global Dirichlet symbol

对有限支撑序列 `f` 定义 Dirichlet transform

`D(f)(s)=sum_n f(n)n^(-s)`.                             (7)

### 定理 OV（convolution differential has L-symbol）

在绝对收敛区域，

`D(C_a f)(s)=L(s)D(f)(s)`,                             (8)

`D(C_a^(-1)f)(s)=D(f)(s)/L(s)`.                        (9)

#### 证明

展开并按 `n=dm` 重排：

`sum_n sum_(d|n)a(n/d)f(d)n^(-s)`

` =(sum_m a(m)m^(-s))(sum_d f(d)d^(-s))`.              (10)

式 (9) 对 `b` 同理。`□`

所以 global `L(s)` 已经是一个不使用 zeros 构造的 arithmetic differential
symbol。有限 determinant 恒为一并不矛盾：zeros 是 infinite-volume symbol
失去可逆性的 boundary spectrum，而不是某个 finite incidence determinant
的零点。这正是文档 079 所允许的 singular/global-cohomological 路线。

## 3. Positive Green--Hodge observable

固定 functional-equation center `c/2`。令

`v_(c,N)=N^(-c/2)(1,...,1)^T`,                         (11)

`K_(a,c,N)=C_(a,N)^(-*) v_(c,N)v_(c,N)^* C_(a,N)^(-1)`.
                                                                    (12)

### 定理 OW（rank-one incidence Hodge identity）

`K_(a,c,N)` 正半定、rank 至多一，而且

`E_(a,c,N):=<e_1,K_(a,c,N)e_1>`

`            =N^(-c)|sum_(n<=N)b(n)|^2`.               (13)

它同时是一维最优平方：

`E_(a,c,N)`

` =sup_(0!=x in span(e_1)) |<v_(c,N),C_a^(-1)x>|^2/||x||^2`.
                                                                    (14)

若把 supremum 扩到完整 `C^N`，所得值为
`||C_a^(-*)v_(c,N)||^2`。

#### 证明

式 (12) 是向量 `C_a^(-*)v` 的 outer product，故正半定。代入式 (5) 即得
式 (13)。一维 Rayleigh quotient 给最后表述。`□`

这是一个真正有限的 Hodge object：differential、Green inverse、Tate constant
mode 与正 Gram form 全部由 coefficients `a(1),...,a(N)` 算出，不需要知道
任何零点。

## 4. Reciprocal-summatory centerline theorem

令非平凡 divisor 关于 `rho -> c-conjugate(rho)` 对称，并设

`Theta=sup_rho Re(rho)`.                               (15)

定义 reciprocal summatory exponent

`beta_b=limsup_(N->infinity) log(1+|B(N)|)/log N`,

`B(N)=sum_(n<=N)b(n)`.                                 (16)

采用以下标准 Perron admissibility：

1. `1/L(s)=s int_1^infinity B(x)x^(-s-1)dx` 在初始半平面成立；
2. 若 `B(x)=O(x^theta)`，该积分给 `Re(s)>theta` 的解析延拓；
3. 在任何无零 half-plane `Re(s)>theta` 中，`1/L` 有足够的 vertical
   polynomial growth，使截断 Perron/平滑移线给
   `B(x)=O_epsilon(x^(theta+epsilon))`。

这些条件对 zeta 是标准定理；对 primitive Dirichlet 和通常 finite-order
Gamma--Euler data 也由相应 Perron estimates 给出。

### 定理 OX（incidence--Hodge centerline theorem）

在上述条件下，

`beta_b=Theta`,                                        (17)

且

`limsup_(N->infinity) log(1+E_(a,c,N))/log N`

`                 =max(0,2Theta-c)`.                  (18)

因此以下等价：

1. 全部非平凡 zeros 位于 `Re(s)=c/2`；
2. `E_(a,c,N)=N^(o(1))`；
3. 对每个 `epsilon>0`，`E_(a,c,N)=O_epsilon(N^epsilon)`；
4. finite positive Green--Hodge packets (12) 的 distinguished arithmetic
   Rayleigh values 具有零 scale-Lyapunov exponent。

#### 证明

若 `B(x)=O(x^theta)`，Mellin 式使 `1/L` 在 `Re(s)>theta` 全纯，故该区域
无 `L`-zero，于是 `Theta<=beta_b`。反过来，对任意 `theta>Theta`，Perron
admissibility 给 `B(x)=O_epsilon(x^(theta+epsilon))`，令 `theta downarrow
Theta` 得 `beta_b<=Theta`，证明式 (17)。式 (13) 直接给式 (18)。

若全体 zeros 在中心线，则 `Theta=c/2`，故 exponent 为零。反之 exponent
为零给 `Theta<=c/2`；functional-equation symmetry 把任意左侧 zero 配到
右侧，故每个 zero 只能满足 `Re(rho)=c/2`。`□`

定理 OX 是文档 073/074 tempered Weil principle 的 multiplicative-incidence
版本：exact positivity 已无条件存在；真正的 purity 输入是一个明确 finite
positive observable 的 subpower growth。

## 5. Riemann zeta specialization

### 推论 OY（Möbius Green--Hodge criterion）

对 `a(n)=1,b(n)=mu(n),c=1`，令 Mertens function

`M(N)=sum_(n<=N)mu(n)`.                                (19)

则

`E_N=M(N)^2/N`,                                        (20)

并且

`RH iff E_N=N^(o(1))`

`   iff M(N)=O_epsilon(N^(1/2+epsilon)) for every epsilon>0`.
                                                                    (21)

这里所有 `C_N,K_N,E_N` 都无条件、有限且只使用 divisibility。未证明的是
式 (21) 的 subpower bound；它正是 RH 的经典 Mertens 等价形式，而不是一项
被矩阵正性偷偷解决的新估计。

### 结构解释

1. 文档 079 的 local orbit carrier 给 Euler traces；
2. 本节 `C_N` 把 local multiplicative data 组装成 global divisibility
   differential；
3. `C_N^(-1)e_1=mu` 是 arithmetic Green response；
4. `v_N` 是 constant/Tate boundary channel；
5. RH 要求这一 Green response 在该 channel 上 tempered。

所以我们已经构造了此前缺失的 nonlocal differential，但还没有证明其
tempered Hodge estimate。

## 6. Dirichlet GRH 与一般 reciprocal coefficients

### 推论 OZ（paired Dirichlet incidence package）

对 primitive character `chi`，

`a(n)=chi(n)`, `b(n)=mu(n)chi(n)`, `c=1`.               (22)

矩阵 `C_(chi,N)` 及正 kernel (12) 无条件存在。对 real `chi`，GRH 等价于

`N^(-1)|sum_(n<=N)mu(n)chi(n)|^2=N^(o(1))`.            (23)

对 complex `chi`，与 `conjugate(chi)` 组成 paired package；二者 summatory
functions 互为共轭，故同一个正能量同时控制 functional-equation 两侧，式
(23) 仍等价于该 pair 的 GRH。

更一般地，任何满足定理 OX reciprocal/Perron hypotheses 的 normalized
Gamma--Euler `L`-data，都以其 Dirichlet coefficients `a` 和 reciprocal
coefficients `b` 得到同一 finite incidence--Hodge package。若 local
reciprocal coefficients 可有效计算，这给一个真正 finite 的 GRH certificate
sequence；证明其 uniform subpower rate 仍是相应 GRH 的全部强度。

## 7. 已实现的有限核对

`scripts/qw_matrix.py` 新增：

- `dirichlet_convolution_matrix`；
- `dirichlet_inverse_coefficients`；
- `dirichlet_incidence_hodge_kernel`；
- `dirichlet_incidence_hodge_energy`。

回归测试对 `N=10` 精确核对：

- zeta incidence inverse 的第一列为 `mu(1),...,mu(10)`；
- `C_1 C_mu=I`；
- kernel (12) 的 `(1,1)` 元等于 `M(10)^2/10`；
- kernel 为显式 outer product，故其正性不是数值猜测。

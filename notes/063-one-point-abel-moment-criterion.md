# 单点 Abel--Stieltjes 矩、Hankel Gram 与 RH

文档 062 把 RH 等价为 annular Abel positive Gram 对每个 `sigma>0` 的真实
收敛。本笔记进一步证明：不必同时观察所有 `sigma`。任选一个无条件收敛点
`sigma_0>1/2`，该点的全部正高阶矩已经精确决定最右零点位置。

核心机制不是解析延拓，而是正 Laplace transform 的 Landau boundary
theorem：收敛半平面的实边界必是 Taylor series 的真实奇点。因此，一个
无条件存在的 Stieltjes moment sequence 的根增长率就编码 RH 的全部强度。

## 1. 单点 Abel moment kernels

沿用文档 062 的 centered annular signals `b_h(t)`。固定
`0<h_0<h_1` 与 `sigma_0>1/2`，定义 matrix moments

`M_q(h,k)=2sigma_0 int_0^infinity t^q`

`              b_h(t)conjugate(b_k(t))e^(-2sigma_0 t)dt`, (1)

以及 width trace

`mathfrak M_q=int_(h_0)^(h_1)M_q(h,h)dh`.          (2)

所有 `q>=0` 的式 (1)–(2) 都无条件绝对收敛。

### 命题 KQ（exact Abel moment prime-pair kernel）

对 finite Euler truncations，

`M_q(h,k)=sum_(m,n)a_m a_n/sqrt(mn) K_q^(h,k)(m,n)`, (3)

其中 `a_n=Lambda(n)-1`，令

`L=max(0,logm-h,logn-k)`,

`U=min(logm+h,logn+k)`，则

`K_q^(h,k)(m,n)`

` =1_(U>L)(2sigma_0)^(-q)`

`   *[gamma(q+1,2sigma_0 U)-gamma(q+1,2sigma_0 L)]`. (4)

这里 `gamma(r,x)` 是 lower incomplete gamma。特别地 `q=0` 恢复命题 KK。
对任意有限 widths `h_alpha` 与 polynomial coefficients `xi_(alpha,j)`，

`sum_(alpha,beta,j,k)xi_(alpha,j)conjugate(xi_(beta,k))`

`                   *M_(j+k)(h_alpha,h_beta)>=0`.  (5)

因此 `(M_(j+k))_(j,k>=0)` 是一个 block Stieltjes--Hankel Gram system。

#### 证明

两个 annular indicators 的交集仍为 `[L,U)`；代换
`x=2sigma_0t` 即给式 (4)。式 (5) 等于

`2sigma_0 int_0^infinity`

` |sum_(alpha,j)xi_(alpha,j)t^j b_(h_alpha)(t)|^2`

`                                      *e^(-2sigma_0t)dt`，

故非负。取 cofinal Euler truncation 给无限素数信号；`sigma_0>1/2` 保证
absolute dominated convergence。`□`

这些是完全显式、有限逼近且无条件正的算术矩阵；尚未使用任何零点位置。

## 2. 正 Laplace transform 的根半径

### 定理 KR（positive Laplace--Landau moment theorem）

设 `mu` 是 `[0,infinity)` 上非零 locally finite positive measure，

`L(s)=int_0^infinity e^(-st)dmu(t)`，             (6)

其有限收敛横坐标为 `a`。固定 real `s_0>a` 并令

`mu_q=int_0^infinity t^q e^(-s_0t)dmu(t)`.        (7)

则

`limsup_(q->infinity)(mu_q/q!)^(1/q)=1/(s_0-a)`.  (8)

#### 证明

`L` 在 `Re s>a` 解析，并在 `s_0` 有 Taylor expansion

`L(s_0-z)=sum_(q>=0)mu_q z^q/q!`.                 (9)

圆盘 `|z|<s_0-a` 位于收敛半平面，所以 radius 至少为 `s_0-a`。若 radius
严格更大，取 real `z` 满足 `s_0-a<z<radius`。因各项非负，Tonelli 与
monotone convergence 给

`sum_(q>=0)mu_q z^q/q!`

` =int e^(-s_0t)sum_(q>=0)(zt)^q/q! dmu(t)`

` =int e^(-(s_0-z)t)dmu(t)<infinity`，

但 `s_0-z<a`，与 `a` 是收敛横坐标矛盾。故 radius 精确为 `s_0-a`；
Cauchy--Hadamard 公式给式 (8)。这也是此处所需的 Laplace--Landau theorem
的正测度特例。`□`

positivity 在这里有实质作用：一般带符号 transform 可能靠 cancellation
跨越其逐项收敛边界。

## 3. 单点高阶矩精确读取最右零点

令 `Theta=sup_rho Re rho`，并定义

`R_(sigma_0)=limsup_(q->infinity)`

`       [(2sigma_0)^q mathfrak M_q/q!]^(1/q)`.    (10)

### 定理 KS（one-point Abel moment RH criterion）

对 Riemann zeta 与任意 fixed `sigma_0>1/2`，

`R_(sigma_0)=sigma_0/[sigma_0-max(0,Theta-1/2)]`. (11)

特别地，以下条件等价：

1. RH；
2. `R_(sigma_0)=1`；
3. `R_(sigma_0)<=1`；
4. 对每个 `epsilon>0`，存在 `C_epsilon` 使全部 `q>=0` 满足

   `mathfrak M_q<=C_epsilon q!`

   `                    *[(1+epsilon)/(2sigma_0)]^q`. (12)

更一般地，式 (11) 反演为

`max(0,Theta-1/2)=sigma_0(1-1/R_(sigma_0))`.       (13)

所以单个无条件 Abel point 的高阶矩不仅判定 RH，还精确给出最右零点偏移。

#### 证明

令 positive width-trace measure

`dmu(t)=int_(h_0)^(h_1)|b_h(t)|^2dh dt`.          (14)

定理 KL/KM/EP 给其 Laplace 横坐标

`a=2max(0,Theta-1/2)`.                            (15)

若右端为正，这是定理 KL 的 divergence/convergence 边界；若右端为零，
定理 KN 的非零 critical spectral mean（zeta 有非平凡零点且 width frame
不消去它）排除负横坐标。

把定理 KR 用于 `s_0=2sigma_0`；式 (2) 中额外常数 `2sigma_0` 不影响
`q` 次根，得到式 (11)。函数方程给 `Theta>=1/2`，所以
`R_(sigma_0)>=1`；式 (11)–(13) 与 root-test 给全部等价。`□`

还有一个只用无条件区数据的 derivative 版本：

`mathfrak M_q=2sigma_0(-1/2)^q`

` *[d^q/dsigma^q (mathfrak G_sigma/(2sigma))]_(sigma=sigma_0)`. (16)

因此 criterion 完全位于同一个 real point `sigma_0` 的正 Taylor jet 中。

## 4. Moment GNS 与 exponential-vector existence

### 定理 KT（one-point moment-GNS structure）

在 canonical space `L^2([0,infinity),dt)` 中令

`v_h(t)=sqrt(2sigma_0)e^(-sigma_0t)b_h(t)`,

`(Txi)(t)=t xi(t)`.                               (17)

则 `T` 是 positive selfadjoint，且

`M_(j+ell)(h,k)=<T^jv_h,T^ell v_k>`.              (18)

对 `0<sigma<sigma_0`，只要右端有限，就有精确 reconstruction

`G_sigma(h,k)=sigma/sigma_0`

`       *<v_h,e^(2(sigma_0-sigma)T)v_k>`.         (19)

zeta 的 RH 等价于：对每个 `u<sigma_0` 都有

`int_(h_0)^(h_1)||e^(uT)v_h||^2dh<infinity`.       (20)

等价地，式 (18) 的 block-Hankel moment functional 具有直到 exponential
type `sigma_0` 的 collective analytic vectors。

#### 证明

式 (18) 直接展开为式 (1)。式 (19) 中 exponential multiplier 把
`e^(-2sigma_0t)` 改成 `e^(-2sigmat)`，常数恰给 `2sigma`。因此
`v_h in Dom(e^(uT))` 的 collective width trace 条件等价于
`mathfrak G_(sigma_0-u)<infinity`。令 `u` 遍历 `[0,sigma_0)`，再用定理 KL
即得 RH 等价。`□`

这个 positive multiplication operator `T` 不是 Hilbert--Pólya 的零点
operator；它是控制从一个无条件 Abel fiber 向临界 fiber 延拓的 GNS
generator。一旦 analytic-vector existence 成立，文档 062 的
`sigma downarrow0` GNS 才产生零点纵坐标的 selfadjoint generator。

## 5. Positivity-only no-go

### 命题 KU（Hankel positivity alone cannot force the centerline）

对任意 `0<=a<sigma_0`，模型 positive measure

`dmu_a(t)=e^(2at)dt`                               (21)

具有全部 Hankel positivity 与 finite moments at `sigma_0`，但其 normalized
root rate 为

`R_a=sigma_0/(sigma_0-a)`.                        (22)

所以仅有式 (5) 的代数 positivity、甚至全部有限 moment matrices 的存在，
不能推出 `R=1`；必须加入 sharp analytic-vector/exponential-type bound，或
利用 zeta 素数系数的额外算术关系证明它。

#### 证明

直接计算

`2sigma_0 int_0^infinity t^q`

`              *e^(-2(sigma_0-a)t)dt`

` =2sigma_0 q!/[2(sigma_0-a)]^(q+1)`，            (23)

再取式 (10) 的根极限。`□`

这解释了为什么“有限正 Gram 已存在”仍不等于 RH：真正缺失的是所有阶矩之间
具有临界常数 `1/(2sigma_0)` 的统一增长律。

## 6. Gamma--Euler 单点矩结构定理

### 定理 KV（general one-point Abel--moment theorem）

对中心 `c/2` 的 paired finite-order Gamma--Euler current，假设其 divisor
非空、关于中心对称，且 continuous width family 是 divisor-separating
frame。令

`Theta=sup_D Re rho`,

`sigma_c=max(0,Theta-c/2)`.                       (24)

在任意 absolute-convergence point `sigma_0>sigma_c` 构造式 (1)–(5) 的
Euler moments，则

`R_(sigma_0)=sigma_0/(sigma_0-sigma_c)`.          (25)

因此 centerline property `Theta=c/2` 等价于单点 block-Hankel GNS vectors
具有 maximal exponential type `sigma_0`，也等价于 `R_(sigma_0)=1`。

#### 证明

命题 KQ 只使用 Euler indicator fibers；定理 KP 给 Abel 横坐标
`sigma_c`；定理 KR 与 KT 随后逐字适用。复或非自对偶数据先与
contragredient 配对，以得到 Hermitian positive width trace。`□`

## 7. Endpoint recurrence 与新的算术目标

### 命题 KW（exact moment endpoint recurrence）

命题 KQ 的 pair kernel 满足

`K_(q+1)=((q+1)/(2sigma_0))K_q+E_(q+1)`,         (26)

其中

`E_(q+1)=1_(U>L)[L^(q+1)e^(-2sigma_0L)`

`                         -U^(q+1)e^(-2sigma_0U)]`. (27)

令 normalized width-trace moments

`N_q=(2sigma_0)^q mathfrak M_q/q!`.               (28)

则

`N_(q+1)-N_q=(2sigma_0)^(q+1)/(q+1)!`

` *int_(h_0)^(h_1)sum_(m,n)a_ma_n/sqrt(mn)`

`                         *E_(q+1)^(h,h)(m,n)dh`. (29)

#### 证明

对 `int_L^U t^(q+1)e^(-2sigma_0t)dt` 分部积分，或对 lower incomplete
gamma 使用

`gamma(q+2,x)=(q+1)gamma(q+1,x)-x^(q+1)e^(-x)`，

即得式 (26)–(27)。代入式 (3)，再按式 (28) 归一化，主项恰变成 `N_q`，
余项给式 (29)。`□`

### 定理 KX（endpoint-increment RH criterion）

对任意 fixed `sigma_0>1/2`，RH 等价于

`limsup_(q->infinity)|N_(q+1)-N_q|^(1/q)<=1`.     (30)

所以存在性问题可以具体表述为：证明式 (29) 的 signed prime-pair endpoint
sum 对 moment order 只有 subexponential growth。

#### 证明

若 RH 成立，定理 KS 给 `limsup N_q^(1/q)=1`，三角不等式给式 (30)。反之，
式 (30) 与 telescoping identity

`N_q=N_0+sum_(j<q)(N_(j+1)-N_j)`                 (31)

给 `limsup N_q^(1/q)<=1`；定理 KS 即推出 RH。`□`

式 (29) 保留了 lower/upper annulus endpoints 的相反符号。逐项取绝对值只会
恢复 trivial exponential rate `sigma_0/(sigma_0-1/2)`；所以可行证明必须
利用两端点以及 `Lambda(n)-1` 的联合 cancellation，而不能只估计正质量。

## 8. 对存在性问题的新定位

对 zeta，现在已经无条件存在：

- 任意 `sigma_0>1/2` 上的全部 finite/cofinal prime-pair moment Grams；
- 全部 block Hankel positivity；
- canonical positive moment-GNS operator `T`；
- 精确读取 `Theta` 的 root-rate identity。

尚未证明且与 RH 等价的是 sharp bound (12)，即证明 prime-built vectors 的
exponential type 从无条件的 trivial barrier 改进到临界值 `sigma_0`。
PNT 的 `o(e^(t/2))` 只改进非统一 prefactor，不能改变式 (10) 的
根极限；下一步必须寻找能跨所有 moment orders 的算术 recurrence、Hodge
inequality 或 trace-compatible cancellation。命题 KW/定理 KX 已把这一输入
缩成式 (29) 的显式 endpoint prime-pair 增量。

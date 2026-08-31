# Prefix flow、整数线图 Hodge 极化与 RH

文档 067 把 RH 等价为 annular Hodge energy 的 anchored Cesàro bound。本笔记
把同一条件离散到最小可能的算术复形：正整数的 oriented line graph。
von Mangoldt charge 减去 Tate charge 后，其唯一 prefix flow 是
`psi(n)-n`；临界 Hodge norm 是一个完全显式的 max-kernel 正二次型。

这给出无需连续 widths、Gamma sampling 或 Taylor 极限即可陈述的 finite
algebraic structure，同时说明这些较丰富结构的共同一维骨架。

## 1. Chebyshev current 的精确离散能量

令

`d_n=Lambda(n)-1`,

`A_n=sum_(k<=n)d_k=psi(n)-n`.                      (1)

并定义 centered step discrepancy

`E_step(x)=psi(x)-floor(x)`.                       (2)

### 命题 LY（exact prefix-flow energy identity）

对 integer `N>=2`，

`P(N)=int_1^N |E_step(x)|^2x^(-2)dx`

`    =sum_(n=1)^(N-1)|A_n|^2/[n(n+1)]`.          (3)

等价地，若

`f(t)=e^(-t/2)E_step(e^t)`，                       (4)

则

`P(N)=int_0^(logN)|f(t)|^2dt`.                    (5)

#### 证明

在 `[n,n+1)` 上 `E_step(x)=psi(n)-n=A_n`，且

`int_n^(n+1)x^(-2)dx=1/n-1/(n+1)=1/[n(n+1)]`，

逐段求和给式 (3)。在式 (4) 中令 `x=e^t`，则
`|f(t)|^2dt=|E_step(x)|^2x^(-2)dx`，给式 (5)。`□`

所以每个 finite `P(N)` 都是单调、正且只使用 `Lambda(n)` 的精确有限量。

## 2. Line-graph incidence 与 max Green kernel

更一般地固定 `c>0`，令

`w_(c,n)=[n^(-c)-(n+1)^(-c)]/c`.                  (6)

在 rooted oriented line graph

`1--2--3--...--N`                                 (7)

上，把 `A_n` 看作 edge `n->n+1` 的 flow，并取 divergence convention

`(partial A)_n=A_n-A_(n-1)=d_n`, `A_0=0`.         (8)

### 定理 LZ（finite line-graph Hodge factorization）

对任意 complex charges `d_1,...,d_N`，令 `A_n=sum_(k<=n)d_k`。则

`mathcal E_(c,N)(d)=sum_(n=1)^Nw_(c,n)|A_n|^2`   (9)

` =sum_(m,n<=N)d_m conjugate(d_n)K_(c,N)(m,n)`，

其中

`K_(c,N)(m,n)`

` =[max(m,n)^(-c)-(N+1)^(-c)]/c`.                (10)

因此 `K_(c,N)=L_N^*W_(c,N)L_N` positive
semidefinite；这里 `L_N` 是 lower-triangular prefix operator。去掉 finite
boundary 后的 Green kernel 为

`K_c(m,n)=1/[c max(m,n)^c]`.                      (11)

#### 证明

展开式 (9) 后，charge pair `(m,n)` 出现在全部 `k>=max(m,n)` 的 prefix
square 中，其 coefficient 为

`sum_(k=max(m,n))^Nw_(c,k)`

` =[max(m,n)^(-c)-(N+1)^(-c)]/c`，

即式 (10)。矩阵 factorization 与 positivity 来自式 (9)；令 `N->infinity`
给式 (11)。`□`

式 (10) 的末项是 scalar boundary flux `|sum_(n<=N)d_n|^2` 的 rank-one
subtraction。它是 finite relative Hodge boundary condition，而不是需要猜测的
renormalization。

## 3. 单个 prefix energy 的 RH 判据

### 定理 MA（discrete prefix-Hodge RH theorem）

对 zeta 的 `P(N)`，有精确 exponent

`limsup_(N->infinity)log P(N)/log N`

`                       =max(0,2Theta-1)`.         (12)

以下条件等价：

1. RH；
2. `P(N)=O(log N)`；
3. `P(N)=N^(o(1))`；
4. zeta charge vector `(Lambda(n)-1)_(n<N)` 在 finite max-kernel
   polarization (10), `c=1` 中的 energies 为 `O(log N)`。

#### 证明

式 (5) 把 `P(e^T)` 写成 normalized Chebyshev step current 的 cumulative
positive energy。`E_step(x)` 与文档 035 的 `psi(x)-x` 相差
`x-floor(x)`；其 normalized log-time current 的 full `L^2` norm 有限，
所以不改变 Abel convergence abscissa、cumulative exponential rate 或
linear mean bound。

定理 EP 给 squared-current Laplace abscissa
`2max(0,Theta-1/2)`。对 positive measure，文档 067 定理 LV 的
Laplace--cumulative theorem 给式 (12)，并说明 RH 等价于 cumulative energy
`O(T)` 或 `e^(o(T))`。置 `T=logN` 得 1–3。命题 LY 与定理 LZ 给 4。`□`

这是目前最小的 finite RH structure：一个 lower-triangular incidence matrix、
一个 positive diagonal edge metric，以及实际 centered prime charge vector。

## 4. 与 annular frame 的直接关系

### 定理 MB（prefix and annular Hodge means are equivalent）

令文档 067 的 annular energy 为

`M_ann(T)=int_0^Tint_(h_0)^(h_1)|b_h(t)|^2dhdt`. (13)

则

`P(e^T)=O(T)` 当且仅当 `M_ann(T)=O(T)`。          (14)

#### 证明

命题 KA 给 `b_h=(partial+1/2)J_hf`。定理 KM 把 width-averaged Abel energy
与 `f` 的 Abel energy 作 uniform 双侧比较；文档 067 定理 LV 的正
Abel--Cesàro theorem 分别把两侧的 small-`sigma` boundedness 等价为对应
cumulative energy 的 `O(T)`。因此得到式 (14)。这避开了把 anchored
Cesàro mean 与 fixed sliding boundary error 混同。`□`

这说明 continuum annular structure 的作用是为 prefix flow 提供一个
divisor-separating stable frame；中心线能量本身已存在于一维 line graph。

## 5. RH 下的 prefix spectral constant

定义

`C_prefix=sum_gamma m_gamma^2/|1/2+igamma|^2`.     (15)

### 定理 MC（critical prefix mean）

RH 下，式 (15) 收敛，并且

`lim_(N->infinity)P(N)/log N=C_prefix`.            (16)

#### 证明

RH 下 normalized step current (4) 与 smooth Chebyshev current 相差一个
`L^2(0,infinity)` remainder。其 Besicovitch expansion 为

`f(t)~-sum_gamma[m_gamma/(1/2+igamma)]e^(igamma t)`，

trivial/archimedean terms decay。coefficients square summable；Cesàro
orthogonality 消去不同 ordinates 的 cross terms，给 mean square (15)。再用
式 (5) 与 `T=logN` 得式 (16)。`□`

与 annular constant `C_crit` 相比，式 (15) 没有 width multiplier；定理 KB
说明二者由有界且有 gap 的 spectral weight 联系。

## 6. General prefix-divergence Weil structure

### 定理 MD（general discrete divergence--Hodge centerline theorem）

设中心为 `c/2`, `c>0` 的 paired finite-order Gamma--Euler data 可中心化为
discrete charges `d_n`，prefixes

`A_n=sum_(k<=n)d_k`,                               (17)

并满足：

1. `d_n` 由 Euler coefficients 减去显式 polar/Tate increments 构成；
2. step current `f(t)=e^(-ct/2)A_(floor(e^t))` 的 Laplace transform 等于
   centered logarithmic derivative乘一个在 `Re w>0` 无零的 visible factor；
3. divisor 非空、关于 `Re rho=c/2` 对称，并有标准 finite-order contour
   growth。

定义 finite line-graph energy

`P_c(N)=sum_(n<N)w_(c,n)|A_n|^2`,                 (18)

其中 `w_(c,n)` 由式 (6) 给出。若

`Theta=sup_D Re rho`，则

`limsup_(N->infinity)log P_c(N)/logN`

`                         =max(0,2Theta-c)`.       (19)

因此全部 divisor 位于中心线当且仅当

`P_c(N)=O(logN)`，                                 (20)

也当且仅当 `P_c(N)=N^(o(1))`。中心线且 critical coefficients square
summable 时，prefix-flow completions 产生 translation GNS，并满足

`Theta_op=c/2+iA`, `Theta_op*=c-Theta_op`.         (21)

#### 证明

由式 (6)，

`P_c(N)=int_1^N|A_(floor x)|^2x^(-c-1)dx`。       (22)

置 `x=e^t` 即为 `f` 的 cumulative `L^2` energy。假设 2 的 visible 无零
Mellin factor 与假设 3 使定理 EP/ES 的 analytic lower bound 和 contour
upper bound 适用，所以 squared-current Laplace abscissa 为
`2max(0,Theta-c/2)`。positive Laplace--cumulative theorem 给式 (19)–(20)。
定理 LZ 给每个 finite energy 的 Hodge positivity；critical tightness 后用
定理 JP/KP 作 GNS，给式 (21)。`□`

对 primitive Dirichlet/entire automorphic data，polar increments 为空；对
zeta/Dedekind-type pole，取 main term 在相邻 integers 的 increments，使
prefix telescoping 精确成立。若用 smooth polar main term 替代 step version，
两者的 local interpolation remainder 必须单独验证为 subcritical `L^2`。

## 7. 存在性边界

对 zeta，以下结构全部无条件存在：

- finite charges `Lambda(n)-1` 与 exact divergence identity；
- unique prefix flow `psi(n)-n`；
- positive edge metric `1/[n(n+1)]`；
- explicit finite max Green matrix (10)；
- 与 Chebyshev、annular、Abel、RKHS structures 的严格兼容。

唯一未证量是 `P(N)=O(logN)`。定理 MA 证明它与 RH 等价；所以 line-graph
Hodge structure 的 algebraic part 已存在，而所缺 Hodge--Riemann input 是
actual arithmetic flow 的临界 logarithmic energy bound。

# Annular Abel--GNS filtration 与临界零点谱测度

文档 060 证明 continuous annular widths 构成 uniform spectral frame，但把
strong tightness 表述为 Besicovitch 长期均方。本笔记加入 Abel 参数
`sigma>0`，得到：

- 素数侧的显式正 pair kernel；
- 收敛横坐标精确等于最右零点偏移；
- RH 下 `sigma downarrow0` 的纯点 covariance；
- 由素数 Gram 产生的显式 GNS 空间与 selfadjoint 零点生成元。

这避免了把 fixed sliding block、长期 Cesaro mean 与 Abel mean 混为一谈。

## 1. Annular Abel covariance 的素数核

沿用

`b_h(t)=sum_(e^(t-h)<n<=e^(t+h))a_n/sqrt(n)`,

`a_n=Lambda(n)-1`.                                (1)

对 `sigma>0` 定义 matrix-valued Abel covariance

`G_sigma(h,k)=2sigma int_0^infinity`

`                 b_h(t)conjugate(b_k(t))e^(-2sigma t)dt`. (2)

### 命题 KK（exact positive Abel pair kernel）

对 finite Euler truncations，

`G_sigma(h,k)=sum_(m,n)a_m a_n/sqrt(mn)`

`                                  K_sigma^(h,k)(m,n)`, (3)

其中令

`L=max(0,logm-h,logn-k)`,

`U=min(logm+h,logn+k)`，则

`K_sigma^(h,k)(m,n)=[e^(-2sigma L)-e^(-2sigma U)]`

`                              *1_(U>L)`.          (4)

任意 finite width packet 的 block matrix 为 Hermitian positive
semidefinite。对 zeta，式 (2) 至少在 `sigma>1/2` 绝对收敛。

#### 证明

index `m` 的 indicator support in `t` 是
`[logm-h,logm+h)`，再与 `t>=0` 相交。两个 indicators 的交集为 `[L,U)`；
积分

`2sigma int_L^Ue^(-2sigma t)dt`

就是式 (4)。positive semidefiniteness 来自式 (2) 的 Gram 表示。trivial
bound `b_h(t)<<e^(t/2)(1+t)` 给 `sigma>1/2` 的绝对收敛。`□`

所以 Abel filtration 在无条件 half-plane 中已经是由纯有限素数截断逼近的
正 kernel，不依赖零点位置。

这里及下文的临界极限总按

`G_sigma=lim_(N->infinity)G_(sigma,N)`，再取 `sigma downarrow0`       (5)

的次序理解。两极限不可交换：固定 `N` 时信号具有 compact time support，
故 normalized Abel mean 在 `sigma downarrow0` 必趋零。

## 2. 精确收敛横坐标

固定 `0<h_0<h_1`，定义 width trace

`mathfrak G_sigma=int_(h_0)^(h_1)G_sigma(h,h)dh`.  (6)

令

`sigma_c=inf{sigma>=0:mathfrak G_sigma'<infinity`

`                          for every sigma'>sigma}`. (7)

### 定理 KL（annular Abel abscissa theorem）

在标准 finite-order explicit formula 条件下，

`sigma_c=max(0,Theta-1/2)`.                        (8)

因此以下条件等价：

1. RH；
2. `mathfrak G_sigma<infinity` 对每个 `sigma>0`；
3. annular Abel positive Grams 可从无条件区 `sigma>1/2` 延伸到任意
   `sigma>0`，且保持实际积分意义的 positivity。

#### 证明

zero `rho=beta+igamma` 对 normalized current `f` 给 mode
`e^((rho-1/2)t)`。命题 KA 后，其 annular coefficient 乘 analytic multiplier

`r_h(-i(rho-1/2))`.                               (9)

对 width interval 积分不会恒为零：若式 (9) 对全部 `h` 为零，则 analytic
function `sinh(h(rho-1/2))` 在 interval 恒零，矛盾。该 mode 的平方 Abel
integral 收敛当且仅当

`sigma>beta-1/2`.                                 (10)

finite-order Mellin/Laplace singularity theorem 排除最右 fixed exponent 的
完全相消。取所有 zeros 的 supremum 给式 (8)。函数方程保证
`Theta>=1/2`，并给三个条件的等价。更直接地，下面定理 KM 把
`mathfrak G_sigma` 与 `I_sigma` 双侧比较，而定理 EP 已证明后者的收敛
横坐标恰为 `max(0,Theta-1/2)`；`floor(e^t)` 与 `e^t` 的差只贡献指数衰减
项，不改变横坐标。`□`

“meromorphic continuation of a formula” 不足以替代条件 3；要求的是原正
integral/Gram 的真实收敛，否则 positivity 可能在解析延拓中丢失。

## 3. Width frame 与 Chebyshev Abel filtration 等价

定义 normalized Chebyshev Abel energy

`I_sigma=2sigma int_0^infinity|f(t)|^2e^(-2sigma t)dt`. (11)

### 定理 KM（annular-frame Abel equivalence）

对 fixed `0<h_0<h_1`，存在与 sufficiently small `sigma` 无关的常数
`0<c<C<infinity`，使

`c I_sigma-O(sigma)<=mathfrak G_sigma`

`                         <=C I_sigma+O(sigma)`.   (12)

因此 annular 与 Chebyshev Abel filtrations 有相同收敛横坐标和相同
`sigma downarrow0` tightness。

#### 证明

令 `F_sigma(t)=e^(-sigma t)f(t)`。把 Abel weight 共轭进 annular operator
后，未加权 multiplier `r_h(tau)` 被解析变形为

`r_(h,sigma)(tau)=(itau+sigma+1/2)`

`            *2sinh(h(sigma+itau))/(sigma+itau)`. (13)

它在 `sigma=0` 回到定理 KB 的 multiplier，并在
`0<=sigma<=sigma_0`、全部 real `tau` 上保持同样的 uniform upper bound
与 width-averaged positive lower bound（高频由主项一致控制，剩余 compact
frequency set 用连续性）。因此对 `F_sigma` 应用 Plancherel 给双侧不等式。
半线 `t>=0` 与 translations `t+-h` 只在 fixed boundary interval 产生误差；
乘 `2sigma` 后为 `O(sigma)`。对 Sobolev core 先在 compactly supported
smooth vectors 证明，再由 closure。`□`

这说明 annular construction 不是另一个独立 RH criterion，而是 Chebyshev
Hodge current 的一个 arithmetic frame realization。

## 4. RH 下的 `sigma->0` 纯点谱极限

假设 RH，并将同一 ordinate 的 multiplicity 记为 `m_gamma`。去掉显式的
decaying trivial/archimedean remainder 后，normalized current 的
Besicovitch expansion 为

`f(t)~-sum_gamma [m_gamma/(1/2+igamma)]e^(igamma t)`. (14)

令

`q_gamma(h)=-r_h(gamma)/(1/2+igamma)`，

`c_gamma(h)=m_gamma q_gamma(h)`；                  (15)

这里 `gamma=0` 时取连续延拓。事实上
`q_gamma(h)=-2sin(hgamma)/gamma`。

### 定理 KN（critical annular spectral covariance）

RH 下，

`lim_(sigma downarrow0)G_sigma(h,k)`

`=G_0(h,k)=sum_gamma c_gamma(h)conjugate(c_gamma(k))`, (16)

在每个 compact width rectangle 上以 Hilbert--Schmidt/Gram 意义成立。并且

`int_(h_0)^(h_1)G_0(h,h)dh`

`=sum_gamma m_gamma^2/|1/2+igamma|^2`

`                         *m_(h_0,h_1)(gamma)<infinity`. (17)

#### 证明

RH 下 coefficients in (14) 平方可和；`r_h(gamma)` 在 compact widths 上
uniform bounded，zero density 与标准 multiplicity bound 使式 (17) 收敛。
Abel covariance 的两个 modes 给 Cauchy factor

`2sigma/[2sigma-i(gamma-gamma')]`.                 (18)

当 `sigma downarrow0`，不同 ordinates 的 factor 趋零，相同 ordinate 趋一。
平方可和性与 Abel/Besicovitch theorem 给式 (16)–(17)。`□`

式 (16) 是数域 analogue of a pure Frobenius spectral measure：width vectors
`h->c_gamma(h)` 是各个临界 eigenmodes 的 period coordinates。

## 5. 显式 strong GNS realization

### 推论 KO（prime-built Hilbert--Pólya space under RH）

RH 下，按式 (5) 的次序先取 cofinal prime limit、再取 `sigma downarrow0`，
所得 Abel Grams 产生最小 Hilbert space

`mathcal H_ann=closure span{c_.(h):h_0<h<h_1}`

`                         subset ell^2({distinct gamma})`. (19)

translation 定义为

`(U_t xi)_gamma=e^(igamma t)xi_gamma`;             (20)

其 generator `A xi=(gamma xi_gamma)` selfadjoint，并且

`Theta=1/2+iA`, `Theta*=1-Theta`.                  (21)

continuous width frame 使每个 distinct ordinate coordinate 可见。最小 GNS
operator 的谱因此恢复零点的 support；其 spectral weight
`|c_gamma|^2=m_gamma^2|q_gamma|^2` 在已知 normalization `q_gamma` 后又恢复
正整数 `m_gamma`。若只要求一个 ambient operator 的 eigenspace dimension
等于零点重数，可作放大

`ell^2({(gamma,j):1<=j<=m_gamma})`,

并令每个 width vector 的 `(gamma,j)` coordinate 为
`sqrt(m_gamma)q_gamma(h)`；所得 Gram 仍恰为式 (16)，而 `A` 的 eigenvalue
`gamma` 此时具有 multiplicity `m_gamma`。但是每个 width vector 在该 block
只沿 `(1,...,1)` 的 diagonal line；其 orthogonal complement 的 `m_gamma-1`
个方向不在 width vectors 的 cyclic span 中。因此 minimal GNS 仍对每个
distinct `gamma` 只有一维；上述是由 recovered integer weight 选择的
nonminimal amplification，而不是 scalar Gram 自动产生 independent cycles。

反之，若 prime-built Abel Grams 对所有 `sigma>0` 存在且在 `sigma downarrow0`
tight，并产生上述 trace-compatible strong GNS realization，则 RH 成立。

#### 证明

式 (16) 是 vectors `c_.(h)` 的 Gram，故 Kolmogorov/GNS decomposition 给
式 (19)。式 (20) 酉且强连续，标准 diagonal operator selfadjoint；式 (21)
成立。定理 KB 保证 width vectors 对每个 frequency 不全为零，所以谱不丢失；
上述整数权放大给 nonminimal 按重数 ambient 版本；最小性边界由直接检查
cyclic span 得到。反向用定理 KL 或定理 JP。`□`

这条 existence theorem 是有意条件化于 RH 的：它说明若中心线成立，所求
strong structure 可从素数 Abel Grams 而非“以零点为基后宣布正交”来恢复；
尚缺的是无条件把正 Grams 推到 `sigma=0`。

文档 077 说明 spectral atom weight 还有一个 minimal 用法：不作 ambient
amplification，而在 atomic spectral algebra 上定义 trace dimension
`tau(P_gamma)=m_gamma`；相应 tracial determinant 已能按重数恢复 divisor。

## 6. Gamma--Euler Abel theorem

### 定理 KP（general annular Abel--GNS structure）

对中心 `c/2` 的 paired Gamma--Euler current，width-averaged Abel Gram 的
收敛横坐标为

`max(0,Theta-c/2)`.                                (22)

若全部 divisor 在中心线且 critical coefficients 平方可和，则
`sigma downarrow0` 给相应 pure point covariance；若 prime/Euler Abel Grams
对所有 `sigma>0` 正收敛并 critical tight，则 GNS generator 满足

`Theta_op*=c-Theta_op`.                            (23)

#### 证明

把定理 KL–KO 中 `1/2` 换成 `c/2`，并用定理 KE 的 width frame。复/非自对偶
数据在与 contragredient 配对的 packet 上取 Hermitian Gram。`□`

## 7. 存在性边界

对 zeta，已无条件得到：

- `sigma>1/2` 的正 Abel prime kernels；
- 精确收敛横坐标公式；
- annular/Chebyshev filtration 的 frame 等价；
- RH 下由 prime Gram 极限恢复 full pure-point GNS 的构造定理。

未证且与 RH 等价的是把实际正积分收敛推进到每个 `sigma>0`，或等价地把
`sigma downarrow0` tightness 无条件建立。解析延拓 kernel 而不保持正积分
不能填补这一缺口。

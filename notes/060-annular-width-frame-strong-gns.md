# 连续 annular-width frame 与 strong Weil--GNS 重构

文档 059 的单个 annulus 给 rank-one off-center detector，但其 critical
multiplier 在离散频率上为零，因而不能恢复完整中心谱。本笔记证明：把
annulus log-width `h` 在任意非退化区间上连续平均，所有 phase aliases
自动消失，并得到与 normalized Chebyshev current 双侧等价的 uniform
spectral frame。

所以 rank-one arithmetic fibers 的连续族可以产生 strong GNS/Hilbert--Pólya
候选；同时证明任何固定有限个 widths 都不可能给 uniform frame gap。

## 1. Annular de Rham identity

令

`a_n=Lambda(n)-1`,

`E(x)=sum_(n<=x)a_n=psi(x)-floor(x)`,              (1)

`f(t)=e^(-t/2)E(e^t)`.                             (2)

对 `h>0` 定义有限 arithmetic signal

`b_h(t)=sum_(e^(t-h)<n<=e^(t+h))a_n/sqrt(n)`.      (3)

再令 box averaging operator

`J_h f(t)=int_(t-h)^(t+h)f(u)du`.                 (4)

### 命题 KA（annular dilation--de Rham identity）

在 distributions 意义下有精确恒等式

`b_h=(partial_t+1/2)J_h f`                         (5)

`=f(t+h)-f(t-h)+(1/2)int_(t-h)^(t+h)f(u)du`.      (6)

在 frequency `tau` 上 multiplier 为

`r_h(tau)=(itau+1/2)2sin(h tau)/tau`,              (7)

在 `tau=0` 连续取值 `h`。

#### 证明

式 (3) 是 Stieltjes integral

`int_(e^(t-h))^(e^(t+h))x^(-1/2)dE(x)`.           (8)

partial summation 后令 `x=e^u`，得到式 (6)。而
`partial_tJ_h=T_h-T_(-h)`，给式 (5)。Fourier transform 给式 (7)。`□`

对 divisor mode `f(t)=e^((rho-1/2)t)`，式 (7) 的 analytic continuation
正好恢复文档 059 的 annular multiplier，并解释其中心轴 aliases。

## 2. 连续 width average 的 uniform frame gap

固定 `0<h_0<h_1`，定义 spectral frame multiplier

`m_(h_0,h_1)(tau)=int_(h_0)^(h_1)|r_h(tau)|^2dh`. (9)

### 定理 KB（continuous annular frame theorem）

有闭式

`m(tau)=4(tau^2+1/4)/tau^2`

` *{(h_1-h_0)/2`

`   -[sin(2h_1tau)-sin(2h_0tau)]/(4tau)}`,         (10)

且在原点连续取值

`m(0)=(h_1^3-h_0^3)/3`.                           (11)

存在只依赖 `h_0,h_1` 的常数

`0<delta_(h_0,h_1)<=Delta_(h_0,h_1)<infinity`     (12)

使所有实 `tau` 满足

`delta<=m(tau)<=Delta`.                            (13)

因此在任意 translation-unitary spectral representation 中，

`delta||f||^2<=int_(h_0)^(h_1)||b_h||^2dh`

`                                      <=Delta||f||^2`. (14)

#### 证明

积分 `sin^2(h tau)` 得式 (10)，Taylor expansion 给式 (11)。若
`tau!=0`，函数 `h->sin(h tau)` 不可能在整个 interval 恒为零，所以
式 (9) 严格正。`m` 连续；当 `|tau|->infinity`，式 (10) 趋于
`2(h_1-h_0)>0`。故在 compactified real line 上取得严格正 minimum 和有限
maximum，得到式 (12)–(13)。Plancherel/spectral theorem 给式 (14)。`□`

例如 `[h_0,h_1]=[log2,2log2]` 时，数值 minimum 位于原点，

`m(0)=7(log2)^3/3=0.7770575213...`,                (15)

而高频极限为 `2log2=1.3862943611...`。数值只用于审计；定理不依赖
minimum 的位置。

## 3. Strong GNS 与完整 divisor recovery

对 `T>0` 定义 finite arithmetic width Gram

`G_T(h,k)=(1/T)int_0^T b_h(t)conjugate(b_k(t))dt`. (16)

每个 finite discretization in `(t,h)` 都是显式 prime coefficients 的正
Gram。

### 定理 KC（annular-frame strong Weil structure）

以下条件等价：

1. normalized Chebyshev current `f` 的 critical Besicovitch/Sobolev Grams
   uniformly tight；
2. 对某个（因而每个）`0<h_0<h_1`，

   `sup_T (1/T)int_0^T int_(h_0)^(h_1)|b_h(t)|^2dhdt<infinity`; (17)

3. width-averaged finite Grams 有 translation-covariant strong GNS
   completion。

任一条件成立时，GNS completion 上有 selfadjoint generator `A`，

`Theta=1/2+iA`, `Theta*=1-Theta`,                  (18)

且 width continuum 对全部 critical spectral frequencies separating。若与
zeta explicit formula 相容，则 RH 成立。

#### 证明

定理 KB 的 frame inequalities 对 finite-time cutoff 作 boundary enlargement
后取 Besicovitch limit，给条件 1 与 2 等价。条件 2 的 positive Gram、
translation covariance 与 uniform tightness按定理 JP 作 GNS，得到条件 3
与式 (18)。反向由 frame lower bound重构 `f`。对任意 `tau`，式 (9) 严格
正，故 continuum widths separating；定理 E/JP 给中心线。`□`

对 zeta，RH 下 explicit zero expansion 的 coefficients 为 `O(1/rho)`，其
平方按 zero density 可和，所以条件 1–3 成立；若有 off-center zero，则相应
Besicovitch blocks 指数增长。因此 strong annular-frame existence 与 RH 等价。

## 4. 为什么有限个 widths 不够 strong

### 定理 KD（finite-width uniform-frame no-go）

给定任意有限集合 `h_1,...,h_N>0`，

`inf_(tau in R)sum_(j=1)^N|r_(h_j)(tau)|^2=0`.     (19)

所以有限个 annular channels 即使 pointwise separating，也不能给全谱 uniform
frame lower bound。

#### 证明

对 numbers `h_j/pi` 使用 simultaneous Dirichlet approximation，存在
`tau_k->infinity` 与 integers `m_(j,k)`，使

`|tau_k h_j-pi m_(j,k)|->0` 对所有 `j`.           (20)

故 `sin(tau_k h_j)->0`。式 (7) 中
`|(itau+1/2)/tau|->1`，所以每一项都趋零，得到式 (19)。`□`

两个 incommensurable widths 的 multiplier 零集可能没有公共点，因此足以
作 pointwise divisor detector；但 Diophantine near-resonances 仍使 uniform
lower bound 失败。continuous interval 正是消除该区别的最小稳健方式之一。

## 5. Gamma--Euler width-frame theorem

### 定理 KE（general annular-frame Weil structure）

设中心 `c/2` 的 paired Gamma--Euler datum 有 centered counting current

`f_Z(t)=e^(-ct/2)E_Z(e^t)`，                      (21)

并令 annular Stieltjes signals 使用 weight `n^(-c/2)`。则相同 partial
summation 给

`b_(Z,h)=(partial_t+c/2)J_h f_Z`.                 (22)

width-averaged multiplier 为

`4(tau^2+c^2/4)/tau^2`

`                    *int_(h_0)^(h_1)sin^2(h tau)dh`, (23)

它具有严格全谱双侧 frame bounds。若 finite Euler Grams 临界 tight、与
paired divisor trace 相容，则 strong GNS generator 满足

`Theta*=c-Theta`,                                  (24)

故全部 divisor 位于 `Re rho=c/2`。

#### 证明

命题 KA–定理 KC 只需把 `1/2` 换成 `c/2`；式 (23) 在原点取正值
`c^2(h_1^3-h_0^3)/3`，高频趋于 `2(h_1-h_0)`，故定理 KB 的 compactness
证明适用。最后用定理 JP。`□`

## 6. 存在性边界

对经典 zeta，以下均无条件存在：

- 每个 `(T,h)` 的 finite prime Gram；
- width continuum 与闭式 frame multiplier；
- uniform spectral frame gap；
- translation/dilation covariance 与 off-center/full critical visibility。

尚缺且与 RH 等价的是式 (17) 的 critical arithmetic tightness。连续 width
average 解决了 phase alias 和 strong reconstruction，却没有提供所需的素数
均方上界。

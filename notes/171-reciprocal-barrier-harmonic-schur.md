# Reciprocal-barrier correspondence kernel 与 harmonic Schur shorting

文档 150 已用固定下界 `beta` 证明二次 barrier inequality；文档 170 又把
negative index精确搬到 capped correspondence cone。本笔记保留一个此前未使用
的自由度：**正背景本身可以随 height变化，并可吸收由算术 Hodge
correspondences构造的 predictor**。

这给出一条严格弱于 full `L2` profile、但仍足以推出中心线的路线：不估计原始
joint symbol 的完整平方，而只估计它相对某个正 Hodge background 的
Pearson/Schur residual。主要结论是：

1. negative part有一个 exact reciprocal-barrier infimum；
2. reciprocal barrier把 Cauchy measure变成新的正 spectral measure，故自动生成
   positive-definite correspondence kernel；
3. finite harmonic predictor的最优 gain是该 kernel Gram的 Schur complement；
4. predictor必须满足 pointwise amplitude/positivity证书，单独的小 Schur residual
   会产生明确的 no-go；
5. 在 zeta square-root wedge中，剩余 RH-strength输入可改写为
   threshold-complex predictor后的 barrier-weighted shorted energy，而不是 full
   Selberg profile。

## 1. Exact reciprocal-barrier identity

令 `(X,mu)` 是有限 measure space，`H in L1(mu)` 为实函数。对 measurable
`B>0` 定义

`Q_B(H)=1/4 int_X (H-B)^2/B dmu`,                 (1)

允许取值 `+infinity`。

### 定理 ADU（exact adaptive-barrier duality）[U]

有

`int_X H_-dmu=inf_(B>0 measurable) Q_B(H)`.       (2)

更强地，对每个 `0<=q<=1` 与 `B>0`，逐点恒等式

`(H-B)^2/(4B)+Hq`

` =[H+B(2q-1)]^2/(4B)+Bq(1-q)>=0`               (3)

成立。因此每个 explicit positive background 都给

`int H_-dmu<=Q_B(H)`.                            (4)

#### 证明

式 (3)直接展开即可。对 `q=1_(H<0)` 积分给式 (4)。反向取

`B_epsilon=(H^2+epsilon^2)^(1/2)`.               (5)

则式 (1)的 integrand逐点趋于 `H_-`，并被 `|H|+epsilon/4` 控制；dominated
convergence给式 (2)。当 `H ne0` 时形式最优背景是 `B=|H|`。`□`

式 (2)与文档 170 的 effect supremum组成 exact saddle dictionary：

`sup_(0<=q<=1)(-int Hq dmu)`

` =int H_-dmu=inf_(B>0)Q_B(H)`.                  (6)

但任意选择 `B=|H|` 只是重写 negative set，不能作为 arithmetic proof。可用的
背景必须来自不引用零点的 explicit positive Hodge cone，并带 uniform estimates。

## 2. Reciprocal barrier 生成新的 correspondence kernel

回到局部紧 Abel 长度群 `G`。令 `I subset Ghat` 是 spectral block，`mu_I` 为其
有限 ambient measure，并假设 `B:I->(0,infinity)` 满足

`int_I B^(-1)dmu<infinity`.                       (7)

定义 reciprocal-barrier measure与 kernel

`dnu_B(chi)=B(chi)^(-1)dmu_I(chi)`,

`kappa_B(lambda)=int_I chi(lambda)dnu_B(chi)`.    (8)

### 定理 ADV（barrier-weighted orbit Gram）[U]

`kappa_B` 是 continuous positive-definite function。若 finite complex orbit
measure `xi` 定义

`Q_xi(chi)=int_G chi(lambda)dxi(lambda)`,

`R_xi=Re Q_xi`,                                  (9)

则

`int_I R_xi(chi)^2/B(chi)dmu(chi)`

` =1/2 intint kappa_B(lambda-kappa)`

`                 dxi(lambda)dconj(xi)(kappa)`

` +1/2 Re intint kappa_B(lambda+kappa)`

`                 dxi(lambda)dxi(kappa)>=0`.      (10)

同一公式的 polarization给任意两个 real orbit symbols的 weighted cross Gram。

#### 证明

正 measure `nu_B` 的 Fourier transform由 Bochner theorem正定。再用
`(Re Q)^2=(|Q|^2+Re Q^2)/2`，对有限 measures应用 Fubini，即得式 (10)。`□`

所以 reciprocal barrier并不破坏长度侧 algebra：它只是把 ambient Cauchy
measure改成 `mu/B`。式 (10)给一个新的 positive correspondence kernel，恰好
保留 prime、continuum、Gamma 与 harmonic predictor之间的全部 cross terms。

## 3. Harmonic predictor 的 Schur shorting

固定 block `I`。令 `B_0>0`，写

`H=B_0+R`.                                        (11)

取 real predictor space `V=span_R{v_1,...,v_m}`，其中每个 `v_j` 是由有限
orbit/Hodge correspondence构造的显式 real symbol。在 Hilbert space

`L2(I,dmu/B_0)`                                   (12)

中定义

`E=<R,R>`, `G_(jk)=<v_j,v_k>`, `d_j=<R,v_j>`.     (13)

令 `G^dagger` 为 Moore--Penrose inverse，

`alpha_*=G^dagger d`, `C_*=sum_j alpha_(ast,j)v_j`,

`D=d^T G^dagger d=||C_*||^2=<R,C_*>`.            (14)

这里 `d in Ran G` 自动成立：`ker G`中的系数组合在式 (12)为零，故也与 `R`
正交。

### 定理 ADW（amplitude-certified harmonic Schur bound）[U]

固定 `0<theta<1`。令

`M=ess sup_I |C_*|/B_0`,

`s=min(1,theta/M)`,                               (15)

约定 `M=0` 时 `s=1`、`M=infinity` 时 `s=0`。则

`B_s=B_0+sC_*>=(1-theta)B_0>0`,                  (16)

且

`int_I H_-dmu`

` <=[E-(2s-s^2)D]/[4(1-theta)]`.                 (17)

若未经缩放的投影已满足 `|C_*|<=theta B_0`，则 `s=1`，右端为

`(E-d^TG^dagger d)/[4(1-theta)]`,                (18)

即 weighted Gram的 Schur complement。

#### 证明

式 (15)给 `|sC_*|<=theta B_0`，从而式 (16)。对定理 ADU取背景 `B_s`：

`Q_(B_s)(H)=1/4 int (R-sC_*)^2/(B_0+sC_*)dmu`

` <=1/[4(1-theta)] ||R-sC_*||^2_(L2(mu/B_0))`.   (19)

由式 (14)的 projection identities，

`||R-sC_*||^2=E-2sD+s^2D`,                      (20)

即得式 (17)--(18)。`□`

式 (17)明确区分两种任务：

- `D` 衡量 harmonic correspondences真正捕获了多少 joint current；
- `M` 认证该 predictor能否进入正背景而不越过 barrier。

二者缺一不可。若只计算很小的 Schur residual而不验证 amplitude，结论可完全错误：
取 `B_0=1`, `H=-L`, `R=-L-1`，并令 predictor space包含 `R`。则 Schur residual
为零，但 `B_0+C_*=H<0`；真实 negative mass为 `L`。这与早先
capacity/leverage及 Feshbach no-go是同一个 positivity边界。

## 4. Block theorem 与有限 LMI

令 spectral space分成不交 blocks `I_j`，并在每块给定式 (11)--(15)的数据。

### 定理 ADX（shorted-background bounded-index Weil theorem）[C]

在文档 170 定理 ADT 的解析假设下，若 approximation errors `eta_n` 一致有界，
且存在 fixed `theta<1` 使

`sup_n sum_j [E_(n,j)-(2s_(n,j)-s_(n,j)^2)D_(n,j)]`

`                   /[4(1-theta)] <infinity`,    (21)

则相应 self-dual divisor的全部非零 zeros位于中心线。

#### 证明

每块应用定理 ADW，再用文档 170 的 exact block additivity；式 (21)给 uniform
correspondence index。应用定理 ADT。`□`

有限 spectral grid上，式 (1)还有 exact convex epigraph。对每个 grid point，

`z_i >=(h_i-b_i)^2/(4b_i)`, `b_i>0`              (22)

等价于

`[[4z_i,h_i-b_i],[h_i-b_i,b_i]]>=0`.             (23)

因此若 `b_i` 是 harmonic-background coefficients的 affine function，最小化
`sum mu_i z_i` 是一个 finite LMI。它只有在另加 interval/tail与全 block误差后才是
严格无限证书；单个 sampled grid不是 RH 证据。

## 5. 对 full Selberg profile 的严格分离

该结构不恢复 full quadratic profile。若 `H_M=B_M>0` 且
`int B_M^2dmu->infinity`，取背景 `B=B_M`，则 `Q_B(H_M)=0`，而 full `L2`
发散。更一般地，任何被 positive predictor吸收的巨大正方向都不计入式 (17)。

所以文档 169 的 fixed-dilation Mellin continuation不能从式 (21)反推；式 (21)
只控制 Poisson normality真正读取的负部。对具体 zeta candidates，证明式 (21)
当然仍足以推出 RH，因而仍是开放的 RH-strength arithmetic input。

## 6. Zeta square-root wedge 的精确 shorted target

对 zeta Abel candidate，在 dyadic height block `I_T` 上写

`H_(Y,delta)=B_(0,T)+R_T`,                        (24)

其中 `B_(0,T)` 取 joint pole/continuum/Gamma background；在文档 150 已控制的
高块上可验证

`B_(0,T)(t)>=c log(e+T)`.                        (25)

prime truncation、continuous residual与 quadrature error留在 `R_T`。令

`dnu_T(t)=1_(I_T)(t)dt`

` /[pi(1+t^2)B_(0,T)(t)]`.                       (26)

定理 ADV给 reciprocal-barrier kernel

`kappa_(B,T)(lambda)=int_(I_T)e^(-itlambda)dnu_T(t)`. (27)

在文档 164 的 `U_T=T/log^A T` 下，取 predictor space由以下 finite orbit
currents生成：

1. canonical Type I residual的 dyadic length rectangles；
2. Type II coefficients

   `R_II(n)=sum_(mq=n,m>V)Lambda(m)`

   ` *Str P^harm(K_(U_T)(q))`；                  (28)

3. shared-lag continuum/Gamma correction modes。

这些 generators都由 primes、divisor complexes与 archimedean data构造，不引用
zeros。式 (10)把它们的 `G_T,d_T,E_T` 变成纯长度侧
`kappa_(B,T)` Gram；式 (28)的 harmonic projection是文档 166--167 已构造的
threshold-complex对象。

由于 `dmu/B_0` 在 shell上约为 `dt/[T^2logT]`，新的 square-root target是

`sum_T [E_T-(2s_T-s_T^2)D_T]=O(1)`               (29)

（这里 `E_T,D_T` 已按式 (26)计权），连同 `M_T` 的统一 amplitude证书。若改用
Lebesgue energies，则相应账本为

`sum_T [E_T^Leb-(2s_T-s_T^2)D_T^Leb]`

`                    /(T^2logT)=O(1)`.           (30)

文档 167 已无条件控制 coefficient diagonals；文档 169 已无条件删除
`N<=T^(2-eta)`。因此式 (29)--(30)真正未决的部分是：在
`N>T^(2-eta)` 内由 cross-fiber correspondences证明足够大的 projection gain
`D_T`，同时控制 leverage `M_T`。这比“证明 full Selberg profile”更精确：
bad off-diagonal energy可以被 Hodge background吸收，而不是必须先变小。

## 7. 下一步

下一步不再泛称“构造 superconnection”，而是计算式 (28) generators在
`kappa_(B,T)` 下的三个量：

1. `G_T`：harmonic predictor自身的 reciprocal-barrier Gram；
2. `d_T`：predictor与 joint prime/continuum/Gamma residual的 cross map；
3. `M_T`：投影背景相对 archimedean barrier的 pointwise leverage。

应先在单个 multiplicative rectangle上用 boundary-shell formula计算 `d_T`，再用
profinite cylinder Gram控制 `G_T`，最后研究 `M_T` 的 large-value/maximum transfer。
若 `D_T`不能抵消 square-root off-diagonal budget，或 `M_T`必然发散，本路线会给
一个明确 no-go；若三者满足式 (29)，定理 ADX直接推出 RH。

本笔记没有证明 RH。它把文档 170 的 exact negative index进一步转成一个新的、
可计算的正 kernel target：**reciprocal-barrier Gram的 amplitude-certified Schur
residual**。

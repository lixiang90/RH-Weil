# Square-completed Hodge background 与无 amplitude 的 Schur--L4 判据

文档 171 将 zeta 的 joint negative index压到 reciprocal-barrier Schur residual，
但需要 pointwise leverage

`M=ess sup |C_*|/B_0`                            (1)

来保证线性 predictor不会把正背景推成负数。对 Dirichlet polynomials，supremum
可能远大于 Cauchy capacity；若继续硬估式 (1)，可能重新引入文档 149--150 已经
绕开的 deepest-well 障碍。

本笔记用一个 sharp square completion消除式 (1)。代价不再是 `L^infinity`，而是
predictor的 weighted `L4` Hodge moment。这个四阶量仍由正 spectral measure生成
correspondence Gram，并可由 large values或 fourth-moment工具研究。

主要结论：

1. 给定任意 real predictor `C`，有一个无条件正的 quadratic Hodge background；
2. 该 quadratic correction在所有 amplitude-uniform lifts中系数最优；
3. negative index由 Schur residual加 weighted fourth moment控制；
4. fourth moment本身是 squared-orbit measure在 `dmu/B_0^3` 下的正 Gram；
5. zeta square-root wedge的下一目标从 `(G_T,d_T,M_T)` 改为
   `(G_T,d_T,P_(4,T))`，不再需要 pointwise maximum。

## 1. Sharp quadratic positivity lift

令 `B_0>0`、`C` 为任意实函数，固定 `0<epsilon<1`。定义

`B_(epsilon,C)=B_0+C+C^2/[4(1-epsilon)B_0]`.      (2)

### 定理 ADY（sharp square-completed background）[U]

逐点有

`B_(epsilon,C)`

` =epsilon B_0+(1-epsilon)`

`  *[sqrt(B_0)+C/(2(1-epsilon)sqrt(B_0))]^2`

` >=epsilon B_0>0`.                              (3)

而且式 (2)中的 coefficient是 sharp：对 fixed `a>=0`，

`B_0+C+a C^2/B_0>=epsilon B_0`                   (4)

对全部 real `C` 成立，当且仅当

`a>=1/[4(1-epsilon)]`.                           (5)

#### 证明

展开右端即得式 (3)。令 `x=C/B_0`，式 (4)等价于
`1+x+ax^2>=epsilon` 对全部 `x in R` 成立。`a=0`显然失败；`a>0` 时左侧最小值为
`1-1/(4a)`，故条件恰为式 (5)。`□`

所以若不限制 predictor amplitude，任何 universal quadratic positivity lift都必须
至少支付式 (2)的 `C^2/B_0` correction。后续出现 fourth moment不是粗估偶然，
而是这一 sharp positivity price的平方。

## 2. 无 amplitude 的 Schur--L4 negative-index bound

在有限 measure block `I` 上写

`H=B_0+R`, `B_0>0`.                              (6)

对任意 real predictor `C` 定义

`A_2(C)=int_I (R-C)^2/B_0 dmu`,

`P_4(C)=int_I C^4/B_0^3 dmu`.                    (7)

### 定理 ADZ（square-completed Schur--L4 bound）[U]

对每个 `0<epsilon<1`，

`int_I H_-dmu`

` <=A_2(C)/(2epsilon)`

`   +P_4(C)/[32epsilon(1-epsilon)^2]`.            (8)

特别地，取 `epsilon=1/3`，

`int_I H_-dmu<=3A_2(C)/2+27P_4(C)/128`.          (9)

#### 证明

对文档 171 定理 ADU取正背景 `B_(epsilon,C)`。由定理 ADY，分母至少为
`epsilon B_0`；而

`H-B_(epsilon,C)`

` =(R-C)-C^2/[4(1-epsilon)B_0]`.                 (10)

使用 `(x-y)^2<=2x^2+2y^2`，

`Q_(B_(epsilon,C))(H)`

` <=1/(2epsilon) int (R-C)^2/B_0 dmu`

`  +1/[32epsilon(1-epsilon)^2]`

`    *int C^4/B_0^3 dmu`,                        (11)

再用 reciprocal-barrier upper bound即得式 (8)。代入 `epsilon=1/3`给式 (9)。
`□`

更一般地可用
`(x-y)^2<=(1+gamma)x^2+(1+1/gamma)y^2` 优化两个 moments的相对常数；式 (9)
选择固定常数以简化 block summation。

## 3. 与 harmonic Schur projection 的结合

沿文档 171，在 Hilbert space `L2(I,dmu/B_0)` 中取 predictor space
`V=span_R{v_1,...,v_m}`，令

`E=<R,R>`, `G_(jk)=<v_j,v_k>`, `d_j=<R,v_j>`,

`C_*=sum_j(G^dagger d)_jv_j`,

`D=d^T G^dagger d`.                              (12)

则

`A_2(C_*)=E-D`.                                  (13)

### 推论 AEA（amplitude-free harmonic Schur criterion）[U]

记

`P_4^*=int_I C_*^4/B_0^3dmu`.                   (14)

则

`int_IH_-dmu<=3(E-D)/2+27P_4^*/128`.             (15)

#### 证明

式 (13)是正交投影/Schur complement恒等式；代入定理 ADZ式 (9)。`□`

式 (15)彻底删除 pointwise `M`。它允许 predictor在很小 spectral sets上超过
`B_0`，只要相应 fourth capacity可控。与文档 171相比，这是从 maximum norm到
large-value/fourth-moment norm的实质降阶；当然它并未证明 zeta 所需的 uniform
bound。

## 4. Fourth moment 仍是正 correspondence Gram

设 `C=Re Q_xi`，其中

`Q_xi(chi)=int_G chi(lambda)dxi(lambda)`.          (16)

令 `tilde(conj(xi))` 表示先取 complex conjugate、再由
`lambda->-lambda` push-forward的 measure，并定义 convolution measure

`zeta_xi=1/2[xi*tilde(conj(xi))+xi*xi]`.          (17)

则

`C(chi)^2=Re int_G chi(lambda)dzeta_xi(lambda)`.  (18)

固定 `B_0`，定义 fourth-order reciprocal kernel

`kappa_(B_0,3)(lambda)`

` =int_I chi(lambda)B_0(chi)^(-3)dmu(chi)`.       (19)

### 定理 AEB（positive fourth-order correspondence Gram）[U]

`kappa_(B_0,3)` 正定，且 `P_4(C)` 等于 orbit measure `zeta_xi` 在该 kernel下的
real stationary Gram：

`P_4(C)=1/2 intint kappa_(B_0,3)(lambda-rho)`

`                 dzeta_xi(lambda)dconj(zeta_xi)(rho)`

` +1/2 Re intint kappa_(B_0,3)(lambda+rho)`

`                 dzeta_xi(lambda)dzeta_xi(rho)>=0`. (20)

#### 证明

由

`C^2=(|Q_xi|^2+Re Q_xi^2)/2`                    (21)

及 convolution theorem得式 (17)--(18)。measure `B_0^(-3)mu`为正，故其
Fourier transform式 (19)正定。对 real orbit symbol `C^2`应用文档 171 定理 ADV，
得到式 (20)。`□`

因此 quartic price仍完全位于长度侧：它不是任意四线性绝对值，而是 squared
harmonic orbit measure的 positive correspondence Gram。对 finite lag data，
式 (17)只增加 pair-sum与 pair-difference nodes。

## 5. Bounded Schur--L4 Weil theorem

### 定理 AEC（square-completed background Hodge--Weil theorem）[C]

在文档 170 定理 ADT 的解析与 approximation hypotheses下，把每个 ambient
spectrum分成不交 blocks。若每块有 explicit `B_(0,n,j)>0` 与 finite arithmetic
predictor space，并令 `E_(n,j),D_(n,j),P_(4,n,j)^*` 如式 (12)--(14)。若

`sup_n sum_j [3(E_(n,j)-D_(n,j))/2`

`              +27P_(4,n,j)^*/128]<infinity`,    (22)

则相应 self-dual divisor的全部非零 zeros位于中心线。

#### 证明

每块应用推论 AEA，再用 exact block additivity；式 (22)给 bounded capped
correspondence index。应用文档 170 定理 ADT。`□`

这个定理比文档 171 的 amplitude-certified criterion有不同强弱：前者支付
weighted `L4`，后者支付 pointwise leverage缩放。实际证明可逐 block取二者较小；
二者都只读取 negative-index sufficient quantity，不推出 full Selberg profile。

## 6. Zeta square-root wedge 的新目标

沿文档 171，在 dyadic shell `I_T` 上取

`B_(0,T)=Re[A_infinity+I_Y]+controlled corrections`

并在适用高块验证 `B_(0,T)>=c log(e+T)`。用 threshold-complex harmonic currents
与 canonical Type I rectangles形成 reciprocal-barrier projection `C_(ast,T)`。
定义

`A_T=E_T-d_T^TG_T^dagger d_T`,

`P_(4,T)=int_(I_T) C_(ast,T)^4/B_(0,T)^3dmu`.     (23)

则新的 sufficient target为

`sum_T [3A_T/2+27P_(4,T)/128]=O(1)`,              (24)

再加低 polylog-height block与既有 approximation errors。

在 shell上 `dmu asymp dt/T^2`、`B_0 asymp logT`，所以若改用 Lebesgue moments，

`A_T asymp A_T^Leb/(T^2logT)`,

`P_(4,T) asymp P_(4,T)^Leb/(T^2log^3T)`.          (25)

第四矩比二阶 residual多得到两个 archimedean log denominators。文档 167 已控制
coefficient diagonals，文档 169 已删除 `N<=T^(2-eta)`；真正未决的是
square-root rectangles中：

1. cross map `d_T`是否使 `A_T`可和；
2. projected harmonic current的 fourth moment是否满足式 (25)的总预算。

这正适合 large-value/level-set工具：无需控制 supremum，只需积分第四次方。若 generic
fourth moment仍在 square-root range过大，则应对式 (17)的 pair-sum/difference
measure使用 boundary-shell signs与 profinite correspondences，而不能逐项取绝对值。

## 7. 有限 LMI/SOS 接口

在 finite spectral grid上，给定 `B_0(i)>0` 与 predictor values `C(i)`，式 (2)是
显式 sum-of-squares background。无需额外 positivity solver；只需计算

`A_2=sum_i mu_i(R_i-C_i)^2/B_(0,i)`,

`P_4=sum_i mu_i C_i^4/B_(0,i)^3`.                (26)

定理 ADZ给 certified algebraic upper。若 predictor coefficients仍需优化，可以：

1. 先用 quadratic Gram求 Schur projection；
2. 再用式 (26)审计 quartic price；
3. 或直接把 square background与文档 171 的 `2 x 2` epigraph LMI组合。

本笔记新增的有限回归验证：sharp coefficient、square positivity、Schur--L4 upper、
quartic kernel positivity及 convolution identity。它们是有限代数检查，不是 interval
或 RH 证书。

## 8. 下一步

下一步应在单个 Type II multiplicative rectangle上显式构造 `xi_T` 与
`zeta_(xi_T)`：

1. 用 boundary-shell formula先在 product fibers内保留 Möbius signs；
2. 用 `kappa_(B_0,1)`计算 `G_T,d_T`；
3. 用 `kappa_(B_0,3)`计算 pair-sum/difference Gram `P_(4,T)`；
4. 比较 generic fourth-moment bound与 profinite signed bound，判断式 (24)是否可能
   在 `N>T^(2-eta)` 可和。

若 fourth price可控，第171篇的 pointwise leverage瓶颈即被绕开；若不可控，
定理 ADY的 sharpness说明任何 amplitude-free quadratic background都必须引入同阶
correction，届时需要非二次 Hodge background或真正的 pointwise structure。

本笔记没有证明 RH；它把剩余存在性问题从 maximum norm推进到两个完全正的
correspondence quantities：二阶 Schur residual与四阶 squared-orbit Gram。

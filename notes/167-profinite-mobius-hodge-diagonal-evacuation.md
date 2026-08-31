# Length-compatible supertrace、profinite gcd polarization 与 hard diagonal evacuation

文档 166 将 truncated Möbius defect `b_U=mu_(>U)*1` 实现为乘法 threshold
complex 的 Hodge heat supertrace。该结构是否比 coefficient identity 更强，取决于
它能否与 logarithmic interval incidence 相容。本笔记完成第一轮严格审计：

1. 当 length feature 在每个 divisor complex 上按 scalar identity作用时，
   McKean--Singer cancellation与 interval synthesis精确相容；
2. 但仅把局部 complexes作 direct sum不能产生跨不同 `q` 的 polarization，故
   fiberwise heat supertrace本身仍不控制 physical cross energy；
3. 一个真正的 global positive polarization来自 profinite divisibility cylinders：
   kernel `1/[d,e]` 是 Haar Gram，并自然推广到 twists和 Dedekind ideals；
4. 该 Gram给 `b_U(q)` 的任意单调加权二阶矩；结合
   `sum_(m|n)Lambda(m)=log n`，可无条件证明 Type II 与 Type I hard coefficient
   diagonals至多为 polylogarithmic；
5. 在 dyadic heights `T>=log^K Y`, `K>6`，这些 diagonals除以 archimedean
   barrier后总和为 `o(1)`。

所以 RH 强度进一步局部化到低 polylog height、triangular off-diagonal
near-products及 continuum cross terms。这没有证明 RH，但它是 threshold Hodge
首次给出的非循环定量后果。

## 1. Length-scalar McKean--Singer compatibility

令 `(C_*,partial)` 是有限维 reduced Hilbert chain complex，

`D=partial+partial^*`, `Delta=D^2`,               (1)

`Gamma|_(C_j)=(-1)^j`, `Str(A)=Tr(Gamma A)`.      (2)

令 `H` 是任意复 Hilbert space。对 `xi in H` 与 `A in End(C)`，把
`xi tensor A` 的 `H`-valued supertrace定义为

`Str_H(xi tensor A)=xi Str(A)`.                   (3)

### 定理 ADC（length-scalar heat compatibility）[U]

对任意有限 index set `J`，若每个 `j` 带有限 complex `C_j` 与外部 feature
`xi_j in H`，则对全部 `t>=0`，

`sum_(j in J)Str_H[xi_j tensor exp(-t Delta_j)]`

` =sum_j xi_j chi_tilde(C_j)`

` =sum_j Str_H[xi_j tensor P_j^harm]`.            (4)

特别地，在文档 164--166 的 interval Hilbert space中取

`xi_(m,q)=Lambda(m)(mq)^(-sigma-itau)`

`          *exp(-mq/Y)e_(log(mq))`,               (5)

并取 `C_(m,q)=C_tilde_*(K_U(q);C)`，则

`V_II=sum_(m>V,q>=2)xi_(m,q)b_U(q)`               (6)

在任意 finite truncation上等于式 (4)的 harmonic或 heat supertrace。

#### 证明

对每个 `j`，文档 166 的有限 McKean--Singer identity给

`Str exp(-tDelta_j)=chi_tilde(C_j)=Str P_j^harm`. (7)

乘以 `xi_j` 后有限求和即得式 (4)。式 (5)--(6)使用
`R_II=b_U*Lambda_(>V)`。`□`

式 (4)中的关键是 external feature在 `C_j` 上作用为 scalar identity；因此
它与 `D_j` 对易，nonzero even/odd modes在相同 length feature下成对消去。若把
face-dependent length加入 feature，配对一般会破坏，必须额外控制 commutator。

## 2. Local-complex lift 的 cross-polarization 缺口

定理 ADC 给出 exact lift，但并未自动给 inequality。为看清原因，记

`z=sum_j chi_j xi_j`, `chi_j=chi_tilde(C_j)`.      (8)

则

`||z||^2=sum_(j,k)chi_j chi_k<xi_j,xi_k>`.        (9)

### 命题 ADD（fiberwise supertrace does not create cross maps）[U]

只给 local complexes `C_j`、各自的 `D_j,Gamma_j` 及 direct sum

`C=directsum_j C_j`                               (10)

时，canonical heat/harmonic operators均为 block diagonal。其 supertraces只能
读取各个 `j` 的 diagonal blocks；而式 (9)的 `j ne k` 项需要显式 correspondences

`T_(j,k):C_k -> C_j`.                             (11)

因此 direct-sum McKean--Singer lift本身不提供 physical Gram bound。若用
Euler map

`sum_j xi_j tensor [C_j] -> sum_j chi_j xi_j`     (12)

定义 cross pairing，则所得 norm逐字就是式 (9)，没有减弱原目标。

#### 证明

对 block-diagonal operator `A=directsum A_j`，

`Str_C(A)=sum_j Str_(C_j)(A_j)`.                  (13)

它不含任意 `j ne k` matrix entry。式 (9)恰含所有这类 entries，故必须增加式
(11)，或直接经式 (12)先降到 scalar Euler characteristics。后一做法给 exact
factorization但不产生新 inequality。`□`

这精确限定“superconnection”的含义：把许多 local Laplacians写成大矩阵还不够；
必须从 arithmetic构造跨 fibers 的 maps及其 adjoint/polarization relation。

## 3. Profinite divisibility polarization

令 `Zhat=lim_N Z/NZ`，带 normalized Haar probability `m`. 对正整数 `d` 定义
clopen divisibility cylinder

`E_d=d Zhat`.                                     (14)

则

`m(E_d)=1/d`, `E_d intersection E_e=E_[d,e]`.    (15)

### 定理 ADE（profinite gcd Gram）[U]

对任意有限复系数 `c_d`，

`sum_(d,e)c_d conjugate(c_e)/[d,e]`

` =||sum_d c_d 1_(E_d)||^2_(L2(Zhat,m))>=0`.      (16)

特别地，取 `c_d=mu(d)1_(d<=U)` 得文档 166 的

`Q_U=||sum_(d<=U)mu(d)1_(E_d)||^2>=0`.           (17)

取 `c_d=mu(d)chi(d)1_(d<=U)` 则给任意 Dirichlet twist的正 Hermitian gcd
Gram；local phases不破坏 positivity。

#### 证明

式 (15)来自 `dZhat` 在 `Zhat` 中 index为 `d`，两个主 ideals的交为
`[d,e]Zhat`。展开式 (16)的 `L2` norm即得。`□`

该结构不依赖整数的主 ideal 性。若 `O_K` 是数域整数环，`Ohat_K` 是其 profinite
completion，`a` 是非零 integral ideal，则

`m(a Ohat_K)=1/N(a)`,

`a Ohat_K intersection b Ohat_K=(a intersection b)Ohat_K`. (18)

故

`K(a,b)=1/N(a intersection b)`                   (19)

对任意有限 ideal coefficients构成 positive Gram。这里 `a intersection b` 是
ideal divisibility lattice中的 lcm。于是 profinite gcd polarization无条件适用于
Dedekind zeta与有限 Hecke twists；要得到后续与 `log^3 U` 同强的定量界，还需相应
ideal counting与 inverse-coefficient estimates。

## 4. 单调权的 Möbius defect 二阶矩

沿文档 166，令

`S_U(X)=sum_(q<=X)|a_U(q)|^2`,

`a_U=mu_(<=U)*1`, `b_U=epsilon-a_U`.              (20)

已有无条件 bound

`S_U(X)<=C X log^3(2U)`.                          (21)

### 引理 ADF（monotone-weight transfer）[U]

若 `w_q>=0` 单调不增且有限支撑或右端可取极限，则

`sum_(q>=2)|b_U(q)|^2w_q`

` <=C log^3(2U)sum_(q>=2)w_q`.                   (22)

#### 证明

对 `q>1` 有 `|b_U(q)|=|a_U(q)|`。先截断到 `2<=q<=N`，记相应 partial
sum为 `B_U(x)`，则 `B_U(x)<=S_U(x)<=Cxlog^3(2U)`。离散 Abel summation给

`sum_(q=2)^N |b_U(q)|^2w_q`

` =B_U(N)w_N+sum_(q=2)^(N-1)B_U(q)(w_q-w_(q+1))` (23)

` <=C log^3(2U)[Nw_N`

`        +sum_(q=2)^(N-1)q(w_q-w_(q+1))]`

` <=C log^3(2U)sum_(q=2)^Nw_q`.                  (24)

最后令 `N` 趋于支撑端点或无穷。`□`

引理 ADF 不要求 pointwise 控制 `b_U(q)`，只使用 profinite/gcd second moment。
它保留了 fiberwise Möbius cancellation，避免定理 ACY 的 raw representation
multiplicity。

## 5. Hard Type II coefficient diagonal

取 `V>=U`，文档 165 给

`R_II(n)=sum_(mq=n,m>V)Lambda(m)b_U(q)`.          (25)

记 `1/2<=sigma<=3/4`，并定义 Abel coefficient diagonals

`D_II=sum_(n>=1)|R_II(n)|^2n^(-2sigma)e^(-2n/Y)`, (26)

`D_I=sum_(n>=1)|R_I(n)|^2n^(-2sigma)e^(-2n/Y)`.  (27)

### 定理 ADG（polylogarithmic hard-channel diagonal bound）[U]

存在 absolute `C_1`，使对全部 `Y>=2,U>=1,V>=U` 与上述 `sigma`，

`D_II<=C_1 log^3(2U)log^3(2Y)`,                  (28)

`D_I<=C_1[log^2(2Y)+log^3(2U)log^3(2Y)]`.        (29)

#### 证明

对固定 `n`，weighted Cauchy--Schwarz与 `Lambda(m)>=0` 给

`|R_II(n)|^2`

` <=[sum_(m|n,m>V)Lambda(m)]`

`   *[sum_(mq=n,m>V)Lambda(m)|b_U(q)|^2]`

` <=log n sum_(mq=n,m>V)Lambda(m)|b_U(q)|^2`,    (30)

因为 `Lambda*1=log`。又 `2sigma>=1`，故式 (26)至多为

`sum_(m>V)Lambda(m)/m`

` *sum_(q>=2)|b_U(q)|^2 [log(mq)/q]e^(-2mq/Y)`.  (31)

对固定 `m>=2`，

`w_m(q)=log(mq)q^(-1)e^(-2mq/Y)`                 (32)

在 `q>=2` 单调不增，因为 `mq>=4>e`。对内和应用引理 ADF，再放回全部
`m>=1`，得到

`D_II<=C log^3(2U)`

` *sum_(m,q>=1)Lambda(m)log(mq)/(mq)e^(-2mq/Y)`  (33)

` =C log^3(2U)sum_(n>=1)(log n)^2/n e^(-2n/Y)`,  (34)

再次使用 `sum_(m|n)Lambda(m)=log n`。积分比较或 dyadic decomposition给

`sum_n(log n)^2n^(-1)e^(-2n/Y)<<log^3(2Y)`,      (35)

证明式 (28)。

另一方面定理 ACV给 `R_I=Lambda_(>U)-R_II`，所以

`D_I<=2sum_nLambda(n)^2n^(-2sigma)e^(-2n/Y)`

`       +2D_II`.                                  (36)

由 `Lambda(n)^2<=Lambda(n)log n`、Chebyshev bound
`psi(x)<<x` 与 partial summation，第一项为 `O(log^2(2Y))`，得到式 (29)。`□`

定理 ADG 是对 actual hard coefficients 的估计，不是 raw factor labels 的
Bessel bound；exact-product collisions已经在式 (25)内求和，式 (30)只支付恒等的
`log n` divisor mass。

## 6. Dyadic diagonal evacuation

在文档 151--164 的 interval Hilbert space中，triangular kernel的 coefficient
diagonal满足

`K_h(log n,log n)=h`.                             (37)

因此高度 `T`、`B asymp T`、`h=theta/B` 的两个 hard arithmetic channels的
Gram diagonals之和至多

`h(D_I+D_II)<<[log^3(2U)log^3(2Y)+log^2(2Y)]/T`. (38)

### 推论 ADH（polylog-height diagonal evacuation）[U]

取 dyadic `T_k=2^k`，`beta_k>=c log(e+T_k)`，并在 square-root core内取

`U_k=T_k/log^A(e+T_k)<=Y`.                        (39)

对任意 fixed `K>6`，

`sum_(T_k>=log^K(2Y)) [Diag_I(k)+Diag_II(k)]/beta_k`

` <<log^(6-K)(2Y)/loglog(3Y)=o(1)`.              (40)

#### 证明

在式 (38)使用 `log(2U_k)<=log(2Y)`，得到每块至多

`C log^6(2Y)/[T_k log(e+T_k)]`.                  (41)

对 dyadic `T_k>=T_*=log^K(2Y)` 求和，由几何级数支配于首块，得到

`C log^6(2Y)/[T_*log T_*]`,                      (42)

即式 (40)。`□`

推论 ADH 无条件删去平方根核心中绝大多数高度的 arithmetic coefficient
diagonals。它不控制：

1. `|t|<log^K Y` 的低 polylog-height core；
2. triangular kernel中 `n ne n'` 的 modulated near-product entries；
3. hard channels彼此以及与 continuum/Gamma的 cross terms。

这些 off-diagonal terms仍可为正，不能由 diagonal bound在无 overlap-multiplicity
代价下自动控制。因而本结果没有证明文档 164 的 physical-energy budget。

## 7. 广义结构与下一步

本笔记得到的结构链为

`threshold complexes --Euler/heat supertrace--> b_U(q)`

` --profinite Haar Gram--> monotone weighted L2 bound`

` --Lambda*1=log--> hard coefficient diagonal evacuation`. (43)

前两箭头适用于带相位的 divisor coefficients；在 Dedekind ideal semigroup中，
profinite Haar Gram仍无条件存在。第三箭头需要具体 Euler datum的 logarithmic
derivative convolution identity及相应 coefficient growth，不能仅由函数方程推出。

下一步应集中于式 (40)没有处理的 cross geometry。一个明确目标是：对

`|log(mq/m'q')|<h`                               (44)

构造由 profinite cylinder intersections与 threshold-complex restriction maps共同
给出的 correspondences `T_((m,q),(m',q'))`，并证明其 commutator/negative-index
cost在 `T>=log^K Y` 可和。若只能先用 absolute overlap count，则会重新引入约
`Y/T` 的 multiplicity，抵消推论 ADH；必须保留 modulation或 boundary-shell signs。

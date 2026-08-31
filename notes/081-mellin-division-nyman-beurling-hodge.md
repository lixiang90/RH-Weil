# Mellin division、Nyman--Beurling completion 与 finite Hodge distance

文档 080 构造了 global divisibility differential，但其 finite determinants
恒为一，zeros 只表现为 infinite symbol 的不可逆性。本节给出所需 Hilbert
completion：把 `L(s)` 视为 Mellin/Hardy multiplier，把 arithmetic inverse
问题变成一个闭值域/cokernel 问题。有限阶段是普通正 Gram 矩阵的 Schur
complement；对 zeta，Nyman--Beurling--Báez-Duarte theorem 证明该 completion
无条件存在，并且 cokernel 消失精确等价于 RH。

## 1. 抽象 Mellin division--Hodge package

固定中心 `c/2` 与右半域 `Omega={Re(s)>c/2}`。一个 **Mellin
division--Hodge package** 包含：

1. Hilbert space `H`、target vector `chi` 与 arithmetic features
   `r_1,r_2,...`；
2. 到一个解析 Hilbert/Smirnov space 的等距 boundary transform `M`；
3. meromorphic `L(s)`、nonvanishing target transform `tau=M chi`，以及
   `M r_n=L q_n`；
4. bounded point evaluations in `Omega`；
5. **division/cyclicity axiom**：`chi` 属于 `closure span(r_n)` 当且仅当
   `tau/L` 在 `Omega` 没有 divisor obstruction（等价地 `L` 在 `Omega`
   无零，允许预先列出的 trivial cancellations）；
6. divisor 关于 `rho -> c-conjugate(rho)` 对称。

### 定理 PA（Mellin division centerline theorem）

对任何上述 package，以下等价：

1. `L` 的全部 nontrivial zeros 位于 `Re(s)=c/2`；
2. `chi in closure span(r_n)`；
3. finite Hodge distances

   `d_N=dist(chi,span(r_1,...,r_N))`                    (1)

   满足 `d_N downarrow 0`。

#### 证明

若存在 `rho in Omega` 且 `L(rho)=0`，则 point evaluation at `rho` 消灭
每个 `M r_n=Lq_n`，却不消灭 `M chi=tau`，故 `chi` 不在闭 span。反之，
division/cyclicity axiom 在 `Omega` 无零时给 density。functional symmetry
把“右半域无零”提升为所有 nontrivial zeros 都在 boundary `Re(s)=c/2`。
最后，nested finite spans 的距离单调趋于到 infinite closed span 的距离。
`□`

这里真正需要独立证明的是第 5 项。它是解析函数空间中的 division theorem，
而不是把 RH 写进 inner product；对 zeta，这一项正由 Nyman--Beurling theory
实现。

## 2. 有限 Hodge--Schur 证书

令 synthesis map

`B_N:C^N -> H`,  `B_N e_n=r_n`,                        (2)

并定义

`G_N=B_N^*B_N`,  `h_N=B_N^*chi`,  `q=||chi||^2`.       (3)

### 定理 PB（finite Gram distance identity）

block Gram matrix

`[[G_N,h_N],[h_N^*,q]]`                                (4)

正半定。若 features 线性独立，则

`d_N^2=q-h_N^*G_N^(-1)h_N`;                            (5)

一般情形以 Moore--Penrose inverse 代替。最优 coefficients 满足 normal
equation `G_N c=h_N`，且 `d_(N+1)<=d_N`。

#### 证明

式 (4) 是 vectors `(r_1,...,r_N,chi)` 的 Gram matrix。正交投影 theorem
给 normal equation；完成平方或取 Schur complement 得式 (5)。扩大 trial
space 只能降低距离。`□`

因此定理 PA 把 centerline 化为一列完全有限的 **positive Hodge radical
formation**：每个 block 无条件正半定，RH 断言 distinguished Schur
complement 在穷尽极限中变成零。

## 3. Zeta 的无条件 Mellin realization

令 `rho(y)=y-floor(y)`，在 `H=L^2(0,infinity;dx)` 中定义

`r_n(x)=rho(1/(nx))`,  `n>=1`,                         (6)

`chi(x)=1_(0,1)(x)`.                                   (7)

采用 Mellin transform

`M f(s)=int_0^infinity f(x)x^(s-1)dx`.                 (8)

在 `Re(s)=1/2`，Mellin Plancherel 给

`||f||_2^2=(1/(2pi))int_R |M f(1/2+it)|^2dt`.          (9)

### 定理 PC（fractional-part Euler multiplier）

在 `0<Re(s)<1`，

`M r_n(s)=-n^(-s)zeta(s)/s`,                           (10)

`M chi(s)=1/s`.                                        (11)

#### 证明

经典 Mellin identity

`int_0^infinity rho(1/x)x^(s-1)dx=-zeta(s)/s`          (12)

先由分段积分/Abel continuation 得到。式 (10) 再由 `y=nx` 缩放；式 (11)
是 `int_0^1x^(s-1)dx`。`□`

对 Dirichlet polynomial

`A_N(s)=sum_(n<=N)c_n n^(-s)`,                         (13)

取 approximant `g_N=-sum_(n<=N)c_n r_n`。式 (9)--(11) 给

`||chi-g_N||_2^2`

` =(1/(2pi))int_R |1-zeta(s)A_N(s)|^2/|s|^2 dt`,

`s=1/2+it`.                                             (14)

### 定理 PD（Nyman--Beurling--Báez-Duarte Hodge theorem）

令 `d_N` 为式 (14) 对所有 length-`N` Dirichlet polynomials 的 infimum。
则

`RH iff lim_(N->infinity)d_N=0`.                        (15)

而且只用 integer dilations (6) 已足够，不需要连续 dilation parameters。

#### 证明来源与结构含义

continuous density equivalence 是 Nyman--Beurling theorem；Báez-Duarte
证明 integer family 已足够。式 (10) 说明这一已知 theorem 正是定理 PA 的
zeta Mellin division/cyclicity axiom，式 (14) 则把它变成定理 PB 的 finite
positive Hodge distances。`□`

所以对经典 zeta，以下对象现已全部无条件存在：

- fixed Hilbert space 与 positive norm；
- prime/divisibility-generated arithmetic feature family；
- Mellin transform 与 zeta multiplier identity；
- finite PSD Gram matrices 与最优 Schur complements；
- off-center zero 的 cokernel/evaluation obstruction。

未证明的只有 `d_N->0`；它仍与 RH 等价。

## 4. 与 Möbius incidence Green response 的精确桥梁

文档 080 给 `C_1^(-1)e_1=(mu(1),...,mu(N))`。令

`A_N^mu(s)=sum_(n<=N)mu(n)n^(-s)`.                     (16)

### 定理 PE（coefficientwise inverse versus critical Hodge inverse）

在 `Re(s)>1`，

`zeta(s)A_N^mu(s)=1+sum_(m>N)R_N(m)m^(-s)`;            (17)

换言之，右侧 `2<=m<=N` 的全部 Dirichlet coefficients 精确为零。另一方面，

`d_N^2<=||(1-zeta A_N^mu)/s||_(L^2(Re=1/2))^2`         (18)

只在右侧有定义时成立；coefficientwise tail cancellation 本身不给该 critical
norm 趋零。

#### 证明

式 (17) 是有限 Dirichlet convolution identity
`sum_(d|m,d<=N)mu(d)=delta_(m,1)` 对 `m<=N`。式 (18) 因为 `d_N` 是所有
Dirichlet polynomial 中的最小值。`□`

这精确解释了两个 completion 的差异：

1. incidence inverse `mu` 在 formal Dirichlet coefficient topology 中最优；
2. Nyman--Beurling coefficients `G_N^(-1)h_N` 在 critical Mellin `L^2`
   topology 中最优；
3. 从前者到后者需要 global Gram renormalization，不能由 triangular
   coefficient cancellation 自动推出。

Báez-Duarte 的 constructive approximants 对 Möbius coefficients 加全局
smoothing；这与本仓库 Abel/Cesàro Hodge filtration 的角色一致。

## 5. Full Hodge criterion 严格强于单通道审计

文档 080 的 energy

`E_N=M(N)^2/N`                                          (19)

只测 `C_1^(-1)e_1` 在 constant/Tate channel 上的一个 matrix element。
本节 `d_N` 则对整个 feature range 作 orthogonal projection，等价于在所有
critical frequencies 上最小化 residual `1-zeta A_N`。

### 命题 PF（rank-one/full hierarchy）

1. `E_N` 与 RH 等价，但只编码一个 distinguished Green response 的增长；
2. `d_N` 与 RH 等价，并显式给出完整 cokernel distance；
3. 任意具体 trial coefficients（包括 truncated/smoothed Möbius）只给
   `d_N` 的 upper bound；
4. off-center zero 给所有 finite trial spaces 的共同 annihilating evaluation
   obstruction，所以 full distance 不可能趋零。

这把“证明某个 Möbius bound”和“构造 Hilbert cohomology”区分开：前者是
一个 arithmetic matrix element，后者是整个 multiplier range 的 closure。

## 6. 广义 L-functions

de Roton 已把 Beurling--Nyman criterion 推广到广泛的 Dirichlet series / 
Selberg-class data：在其解析与增长 hypotheses 下，适当 arithmetic feature
space 的 density 等价于相应右半平面无零。

### 定理 PG（general division--Hodge template）

设 normalized completed `L` 具有 center `c/2`，并满足一个已证明的
Beurling--Nyman division theorem。则：

1. generalized Müntz/arithmetic features 给 Mellin factors `L(s)q_n(s)`；
2. finite feature Grams 给无条件 PSD Hodge blocks；
3. target Schur distances `d_N` 单调；
4. `GRH iff d_N->0`。

对 primitive nonprincipal Dirichlet character，一个显式 local carrier 是

`S_chi(y)=sum_(m<=y)chi(m)`,

`r_chi(x)=-S_chi(1/x)`,  `r_(chi,n)(x)=r_chi(nx)`,      (20)

其 Mellin transform 满足

`M r_(chi,n)(s)=-n^(-s)L(s,chi)/s`                    (21)

（`S_chi` bounded，故 real-space vector 属于 `L^2`）。与 conjugate character
配对后，functional symmetry 把 right-half-plane density criterion 提升为
该 pair 的 GRH。

#### 证明

式 (21) 由 partial summation
`L(s,chi)=s int_1^infinity S_chi(y)y^(-s-1)dy`
及变量替换得到。其余逐项应用定理 PA、PB 和 generalized division theorem。
`□`

## 7. 存在性审计与下一障碍

本节比文档 080 多构造了真正的 Hilbert cokernel：zeta zeros 不再只是一个
formal symbol 的 singularities，而是 arithmetic synthesis range 的 evaluation
obstructions。它也给出了一个完全有限的目标：证明 PSD Schur complements
`d_N^2` 趋零。

但这仍不是 RH 证明。存在性状态是：

- carrier、Mellin transform、features、Gram positivity、division theorem：
  **无条件已知**；
- target 成为 radical，即 `d_N->0`：**精确等价于 RH**；
- 任何新证明必须从 arithmetic Gram geometry 给出非循环 upper bound。

最直接的下一步是把 `G_N` 分成 Möbius incidence core、critical-frequency
resonance blocks 与可控 complement，再使用文档 024/029 的 residual--Feshbach
技术证明 `d_N` upper bounds；仅检查有限 Gram positivity 不足，因为它对每个
`N` 本来就自动成立。

## 8. 计算实现

`scripts/qw_matrix.py` 新增：

- `beurling_fractional_feature`；
- `positive_gram_schur_distance`；
- `sampled_beurling_hodge_data`。

回归测试用正 quadrature packet 核对：block Gram positivity、Schur complement
与直接最小二乘 residual 完全相同，增加 feature 后 distance 单调不增。该采样
只验证有限线性代数实现，不作为 RH 或 exact continuous Gram 的数值证据。

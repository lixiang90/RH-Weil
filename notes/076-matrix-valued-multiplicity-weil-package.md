# Scalar multiplicity no-go 与 matrix-valued Weil package

文档 075 证明 exterior powers 能按重数统计一个真正 Frobenius/operator
space 的 weights，但 zeta 的 scalar logarithmic-derivative current 在重零点处
只有一个 residue channel。本笔记严格区分三件常被混淆的事：

1. scalar spectral atom 的 **mass** 可以含有零点重数；
2. minimal scalar GNS 中该 atom 的 eigenspace dimension 仍等于 `1`；
3. 要由普通 operator determinant 按重数实现 divisor，需要 matrix-valued
   atom rank 或一个明确标注为 nonminimal 的外部 amplification。

## 1. Scalar cyclic GNS has multiplicity one

令 `phi:R->C` 是 continuous positive-definite function。Bochner theorem 给
positive measure `mu`：

`phi(t)=int_R e^(itgamma)dmu(gamma)`.               (1)

### 定理 NV（scalar-GNS spectral multiplicity-one theorem）

`phi` 的 minimal cyclic GNS representation unitary equivalent 于

`H_phi=closure span{e^(it·):t in R} subset L^2(mu)`, (2)

translation generator 是 multiplication by `gamma`。若 `mu` 在 distinct
point `gamma_0` 有任意 positive atom mass `w`，则 spectral projection
`1_{gamma_0}` 的 range dimension 是 `1`，与 `w` 的大小无关。

#### 证明

式 (1) 给

`<e^(it·),e^(is·)>_(L2(mu))=phi(t-s)`,             (3)

所以 Kolmogorov/GNS uniqueness 给式 (2)。在 singleton atom 上，`L^2` fiber
只是 scalar functions on one point，即 `C`；改变 mass 只把其 norm 乘以
`sqrt(w)`，不改变 dimension。`□`

因此 scalar kernel 可以恢复 support 与 atom weights，却不能把 weight `m` 或
`m^2` 自动解释为一个 `m` 维 eigenspace。

## 2. Linear filters cannot split repeated copies

考虑 scalar divisor signal

`f(t)=sum_gamma m_gamma a_gamma e^(igamma t)`.      (4)

取任意 finite/continuous family of translation-invariant linear filters `L_eta`。
在 frequency `gamma`，令 multiplier 为 `ell_eta(gamma)`。

### 定理 NW（coherent repeated-mode rank-one no-go）

filtered channel vector 在 `gamma` 处恒为

`c_gamma(eta)=m_gamma a_gamma ell_eta(gamma)`.      (5)

相应 matrix/operator-valued covariance atom是 outer product

`M_gamma=c_gamma c_gamma^*`,                       (6)

故只要该 mode 可见，

`rank M_gamma=1`,                                  (7)

不论 `m_gamma` 多大，也不论 filter family 有多少 channels。

#### 证明

translation-invariant filter 对 exponential mode 只乘 scalar multiplier。
同一点的 `m_gamma` copies 在 scalar trace中先合并为 coefficient
`m_gamma a_gamma`；所有 channels 因而仍是同一个 feature vector的 scalar
coordinates。covariance 是式 (6) 的单个 outer product，rank 为一。`□`

所以增加 annular widths、Sobolev orders、Taylor moments 或 sampled
frequencies可以分离 **不同** ordinates，却不能分裂同一 ordinate 的 coherent
copies。confluent Vandermonde 只有在另有 independent jet channels 时才适用。

## 3. Matrix-valued atoms recover Hilbert multiplicity

令 channel space `E=C^r`，`K(t)` 是 positive-definite `End(E)`-valued
stationary kernel。operator-valued Bochner theorem 给 positive matrix measure
`M(dgamma)`：

`K(t)=int e^(itgamma)M(dgamma)`.                    (8)

### 定理 NX（spectral multiplicity equals atom rank）

在 minimal vector-valued GNS representation 中，atom `gamma_0` 的 spectral
multiplicity 等于

`dim closure Ran M({gamma_0})^(1/2)`

`                         =rank M({gamma_0})`.      (9)

若 `m` 个潜在 copies 对 channels 的 coupling columns 组成 `r x m` matrix
`C_gamma`，则

`M({gamma})=C_gamma C_gamma^*`,                    (10)

所以 multiplicity 被完整看见当且仅当

`rank C_gamma=m`。                                 (11)

#### 证明

matrix-valued `L^2(M)` construction 在每个 atom 的 fiber 是 quotient of `E`
by `ker M_gamma^(1/2)`，也即 `closure Ran M_gamma^(1/2)`。其 dimension 是
rank。factorization (10) 给 `rank M_gamma=rank C_gamma`。`□`

式 (11) 是 multiplicity-complete visibility 的正确公理；scalar visibility
只要求 `C_gamma!=0`。

## 4. Minimality versus external amplification

### 定理 NY（same scalar Gram admits arbitrary dark amplification）

设 scalar atom mass 为 `w>0`。对任意 integer `m>=1`，可在 ambient fiber
`C^m` 中取 observation vector

`v=sqrt(w/m)(1,...,1)`.                             (12)

它产生同一 scalar Gram `||v||^2=w`，但 cyclic span 仍只有 line `Cv`；其
orthogonal complement `v^perp` 是完全不可见的 dark eigenspace。因此：

1. minimal scalar GNS multiplicity 必为 `1`；
2. scalar Gram 本身不决定 ambient eigenspace dimension；
3. 若另有 arithmetic rule 从 `w` 恢复 integer `m`，可以选择一个
   multiplicity-`m` nonminimal amplification，但新增 `m-1` 个方向不是原
   scalar observables 生成的。

#### 证明

式 (12) 的 norm 是 `w`，所以所有 cyclic matrix coefficients 与一维 atom
完全相同。translations 在整个 `C^m` 上乘同一个 phase，故 `Cv` 与
`v^perp` 都 invariant；从 `v` 生成的最小 invariant subspace只有 `Cv`。
任意 `m` 都可作此构造，证明 nonuniqueness。`□`

对 zeta 的 annular covariance，`w_gamma=m_gamma^2|q_gamma|^2`。在已知
normalization `q_gamma` 后确可取 positive square root恢复 integer
`m_gamma`，再按文档 062 的方式放大；但这是一项基于 spectral atom weight
的 nonminimal completion，不是 scalar prime vectors 自己生成了
`m_gamma` 个独立 cycles。

## 5. Multiplicity-complete Weil package

定义一个 **multiplicity-complete strong Weil package** 包含：

1. 从 Euler/arithmetic data 独立构造的 matrix-valued positive finite Grams；
2. critical tightness 与 translation covariance，产生 stationary matrix kernel；
3. trace/divisor compatibility；
4. 对每个 divisor point `rho=c/2+igamma`，critical atom满足

   `rank M({gamma})=m_rho`;                         (13)

5. regularized determinant 的 trace convention 与这些 ranks 相容。

### 定理 NZ（matrix-valued Weil multiplicity theorem）

若上述 package 存在，则 minimal GNS translation generator `A=A^*` 在
`gamma` 的 eigenspace dimension 恰为 `m_rho`。置

`Theta=c/2+iA`,                                    (14)

则

`Theta^*=c-Theta`,                                 (15)

且 ordinary/regularized determinant按正确 algebraic multiplicity恢复目标
divisor；特别地全部 divisor 位于 `Re rho=c/2`。

#### 证明

定理 NX 与式 (13) 给 eigenspace dimensions。stationary GNS translations
unitary，Stone theorem 给 `A=A^*`，所以式 (15) 成立。determinant 中一个
`m_rho` 维 eigenspace贡献 factor `(s-rho)^(m_rho)`；trace compatibility 给
完整 divisor。`□`

对 nonselfdual data，在与 contragredient 配对的 matrix kernel 上令 adjoint
交换两个 blocks，结论相同。

## 6. Zeta existence audit

### 命题 OA（centerline package exists conditionally; multiplicity-complete carrier does not yet）

对 classical zeta：

1. 文档 062 的 scalar annular Abel kernel 在 RH 下 critical completion为

   `M_gamma(h,k)=m_gamma^2q_gamma(h)conjugate(q_gamma(k))`; (16)

2. 每个 atom operator是 rank-one，故 minimal GNS 只按 distinct ordinates
   实现 simple spectrum；
3. atom mass 与已知 `q_gamma` 可恢复 integer `m_gamma`，所以存在一个按重数
   的 nonminimal amplification，但其 dark directions 不由 width vectors
   生成；
4. 任意只对同一 scalar prime current 作 linear filtering 的 finite/continuous
   FPW family 仍受定理 NW 的 rank-one no-go；
5. 当前没有无条件 prime-built matrix kernel 被证明在 critical boundary
   tight，且 atom rank恰为 `m_gamma`。

所以：证明 RH 只需要 scalar centerline package，multiplicity-complete package
不是必要条件；若目标是普通 Hilbert--Pólya operator 同时自然实现零点重数，
则还需要 genuinely independent arithmetic channels。可能来源包括多个独立
cycles/cohomological correspondences 或一个真正 matrix-valued trace formula，
而不是同一 scalar current 的更多 smoothings。

#### 证明

1 是文档 062 定理 KN。2 用定理 NW/NX。3 用定理 NY 与
`w_gamma/|q_gamma|^2=m_gamma^2`。4 是定理 NW。5 是当前存在性审计：已有
finite kernels 均为 scalar current features，critical tightness 本身又与 RH
等价。`□`

这个 no-go 不削弱中心线路线；它防止把“spectral mass 记录重数”误说成
“minimal prime-built eigenspace 已有相同维数”。同时它给广义结构定理增加
了一个可选但精确的层次：centerline purity 需要 scalar positive structure，
ordinary determinant multiplicity则需要 matrix atom rank。

若不坚持用 ordinary Hilbert eigenspace dimension编码重数，文档 077 给出更
小的替代：在 minimal scalar GNS 的 spectral algebra 上定义
`tau(P_rho)=m_rho`，tracial determinant 即可按重数恢复 divisor，而无需加入
dark directions。

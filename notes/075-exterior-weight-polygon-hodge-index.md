# Exterior weight polygon、endpoint Hodge index 与 divisor multiplicities

文档 074 的 Cesàro norm 只记录最大 weight error。本笔记用 endpoint positive
metrics 与 exterior powers 恢复全部 radial weights 及其重数，并把
off-center modes 的数量写成 finite Hermitian forms 的 threshold inertia。

这更接近 Weil/Hodge-index 机制：functional equation 给 reciprocal slopes，
positive endpoint forms 给一列有限 signatures，而 temperedness 迫使整个
weight polygon 塌缩到中心。

## 1. Exterior powers recover every weight

令 `U` 是 `d` 维 Hermitian space 上的 invertible operator。将 eigenvalues
按 modulus 排列：

`|lambda_1|>=...>=|lambda_d|`,                     (1)

并置 slopes

`a_j=log|lambda_j|`.                               (2)

令 singular values of `U^m` 为

`s_1(m)>=...>=s_d(m)>0`.                           (3)

### 定理 NP（exterior singular-weight theorem）

对每个 `1<=j<=d`，极限存在且

`lim_(m->infinity)log s_j(m)/m=a_j`.               (4)

等价地，对 `1<=k<=d`，

`lim_(m->infinity)log||wedge^k U^m||/m`

`                         =sum_(j=1)^k a_j`.       (5)

#### 证明

singular-value calculus 给

`||wedge^k U^m||=product_(j=1)^k s_j(m)`.          (6)

另一方面，`wedge^k U^m=(wedge^k U)^m`。其 spectral radius 是全部
`k` 个 eigenvalue products 中 modulus 最大者，即
`product_(j<=k)|lambda_j|`。Gelfand spectral-radius formula 给式 (5)。
相邻 `k` 的式 (5) 相减得到式 (4)。`□`

因此 positive matrices

`S_m=(U^m)^*U^m`                                   (7)

的全部 eigenvalue exponents，不只是最大值，都精确恢复 algebraic spectrum
的 radial weights；nonnormal transient 只贡献 subexponential/polynomial
factors。

## 2. Threshold endpoint Hodge index

固定 `epsilon>=0`，定义 Hermitian forms

`D_(m,+,epsilon)=S_m-exp(2epsilon m)I`,            (8)

`D_(m,-,epsilon)=S_m-exp(-2epsilon m)I`.           (9)

记 `n_+(A)`、`n_-(A)` 为 positive/negative inertia indices。

### 定理 NQ（threshold inertia counts off-weight multiplicity）

若 `epsilon` 不等于任何 `|a_j|`，则 sufficiently large `m` 时

`n_+(D_(m,+,epsilon))=#{j:a_j>epsilon}`,           (10)

`n_-(D_(m,-,epsilon))=#{j:a_j< -epsilon}`.         (11)

若没有 `a_j=0`，取 `epsilon=0` 得

`Inertia(S_m-I)`

`=(#{|lambda|>1},0,#{|lambda|<1})`                 (12)

for all sufficiently large `m`。

#### 证明

`S_m` 的 eigenvalues 是 `s_j(m)^2`。定理 NP 给

`log s_j(m)^2/(2m)->a_j`.                          (13)

若 `a_j>epsilon`，对应 eigenvalue 最终大于 `exp(2epsilon m)`；若
`a_j<epsilon` 则最终小于。对 lower threshold 同理。Sylvester inertia
等于相应 eigenvalue count，得到式 (10)–(12)。`□`

在 threshold `epsilon>0` 下，unit-circle Jordan blocks 只有 polynomial
distortion，不影响 inertia count。这把文档 074 的 weight/Jordan 两级审计
严格分离。

## 3. Functional equation as a Hodge-index symmetry

假设 normalized spectrum 在

`lambda mapsto 1/conjugate(lambda)`                (14)

下 invariant；这是 centered functional equation/duality 的 finite form。

### 定理 NR（reciprocal endpoint Hodge-index theorem）

slopes 满足

`a_j=-a_(d+1-j)`.                                  (15)

因此对每个不撞 slope 的 `epsilon>0`，eventually

`n_+(D_(m,+,epsilon))=n_-(D_(m,-,epsilon))`.       (16)

以下条件等价：

1. 全部 eigenvalues 在单位圆；
2. 对每个 `epsilon>0`，sufficiently large `m` 有

   `exp(-2epsilon m)I<=S_m<=exp(2epsilon m)I`;     (17)

3. 所有 positive threshold inertia eventually 为 `0`；
4. 所有 negative threshold inertia eventually 为 `0`。

#### 证明

式 (14) 取 modulus/log 得 slope multiset 在 `a mapsto-a` 下 invariant，故
式 (15)–(16)。定理 NP 把式 (17) 等价成 `-epsilon<=a_j<=epsilon` 对每个
`epsilon>0` 成立，即全部 `a_j=0`。定理 NQ 给 3–4 的 equivalence。`□`

所以 functional equation 只保证 Hodge index 的两侧 obstruction 成对出现；
positive tempered bound 才迫使两侧同时消失。这是“对称不等于中心线”的
finite signature 版本。

## 4. Lyapunov--Weil polygon and tensor calculus

定义 polygon vertices

`P_U(0)=0`,

`P_U(k)=sum_(j=1)^k a_j`, `1<=k<=d`.               (18)

### 定理 NS（exterior Weil polygon theorem）

`P_U` 由 positive exterior norms 唯一恢复：

`P_U(k)=lim_(m->infinity)log||wedge^kU^m||/m`.     (19)

并有以下 calculus：

1. direct sum 的 slopes 是两个 slope multisets 的 union；
2. tensor product 的 slopes 是所有 `a_i+b_j`；
3. dual slopes 是 `-a_d,...,-a_1`；
4. degree-`r` exterior/symmetric/Schur constructions 的 slopes 是相应
   weight sums；
5. reciprocal duality 给 slope polygon 的中心反对称性。

在 reciprocal 情形，purity 等价于 single top slope `P_U(1)=0`；一般情形
则等价于全部 successive slopes `P_U(k)-P_U(k-1)` 为 `0`。

#### 证明

式 (19) 是定理 NP。四种 operations 的 eigenvalues 分别为 union、pairwise
products、reciprocals 及 prescribed monomials；取 logarithmic modulus 得
1–4。5 来自定理 NR。reciprocal slopes 中 `a_1>=0` 且 `a_d=-a_1`，所以
`a_1=0` 强迫全部 slopes 为零。`□`

这把文档 073 的 tensor-category closure 提升为一个可计算的 weight-polygon
functor。

## 5. Exterior-separating filtered Weil packages

对 scale `X=e^t` 的 finite packet，设每个 visible divisor mode `rho` 有
normalized feature vector

`e^((rho-c/2)t)m_t(rho)`, `m_t(rho)=e^(o(t))`.     (20)

称 packet **exterior separating**，若任意 fixed divisor-channel list
`rho_1,...,rho_k` 在 sufficiently large fibers 中的 feature wedge 非零，且其
norm 与 inverse condition loss 都是 `e^(o(t))`。不同 locations 自动给不同
channels；同一 location 若按 multiplicity 重复，则定义要求另有 independent
multiplicity channels，不能只重复同一个 scalar residue vector。

### 定理 NT（filtered exterior Hodge-index theorem）

对 exterior-separating、center-dual filtered Weil package：

1. 任意 fixed visible divisor packet 的 `k`-th exterior Hodge norm exponent
   是

   `2sum_(j=1)^k(Re rho_j-c/2)`                     (21)

   对应的 ordered upper weight sum；
2. threshold endpoint inertia 统计 `Re rho>c/2+epsilon` 与
   `Re rho<c/2-epsilon` 的 visible multiplicities；
3. subexponential first exterior norm 已迫使 centerline；
4. higher exterior norms不降低证明 RH 所需强度，但恢复 obstruction 的数量、
   multiplicity 与完整 weight polygon。

#### 证明

对 fixed packet，把式 (20) 取 wedge；exponential factors 相乘，而
exterior-separating hypothesis 保证 determinant 不被 feature alias 消去，
只产生 `e^(o(t))` distortion。于是 exterior Gram 的 exponent 是式 (21)。
定理 NQ/NR 给 inertia statement。`k=1` 与 center duality 给 3；全部 `k`
给 polygon。`□`

## 6. Zeta/Gamma--Euler exterior carrier existence

### 命题 NU（distinct-mode exterior separation and multiplicity boundary）

文档 057–058 的 logarithmic-moment fibers 对每个由 **distinct divisor
locations** 组成的 fixed finite packet 都 exterior separating：

- distinct modes 的前 `k` 个 moment features 形成 Vandermonde matrix；
- 这些 determinants 对 fixed packet 是 nonzero constants，adaptive
  normalization 只产生 `X^(o(1))` distortion；
- exterior Gram/compound matrices 的 entries 是原 finite positive Euler
  moment matrices 的 minors，故仍无条件 positive semidefinite 且 finite。

因此 zeta、primitive Dirichlet L-functions 以及定理 JU hypotheses 下的
Gamma--Euler data，无条件拥有 **distinct-location-sensitive** finite exterior
Weil carriers。若 actual arithmetic translation/moment packets 的 first
exterior norm 为 subpower，则中心线成立；若全部 exterior norms可控，则还能
在每个 fixed spectral window 恢复 distinct off-center locations 的 weight
polygon 与 inertia counts。

但是 scalar logarithmic derivative 在一个 multiplicity-`m` zero 处只有 residue
`m` 的单个 simple-pole channel；ordinary moment vectors 因而把这些 copies
保持 collinear。要让 exterior inertia 按 algebraic multiplicity 计数，必须
额外构造 independent jet/derivative descendants 或 semisimple multiplicity
channels。FPW1–FPW5 本身不自动提供这项 enriched structure。

#### 证明

对 distinct spectral parameters `z_1,...,z_k`，moment feature determinant 是

`det(z_i^(j-1))=product_(i<j)(z_j-z_i)!=0`.         (22)

文档 055–058 的 tempered polarization equivalence 与 tail bounds 只贡献
subpower factors。positive matrix 的 exterior power仍 positive，其 coordinate
matrix就是 compound minor matrix。应用定理 NT 得 distinct-location
statement。若另行给出 independent jets，则相同 determinant argument 变成
confluent Vandermonde，并恢复 algebraic multiplicity；但这是一项额外假设，
不是当前 finite scalar Euler construction 的结论。`□`

无条件新增的是 carrier、exterior visibility 与 finite inertia machinery，
不是 RH：actual Euler packets 的 subpower bound 仍未证明，且 `k=1` 已与
RH/GRH 等价。higher `k` 的价值是把一个失败的 scalar bound解析成“有多少个
错误 weights、偏离多远、是否有 multiplicity/Jordan obstruction”的有限
Hodge-index profile。对 repeated zeros，当前 profile 只记录 residue weight；
完整 multiplicity inertia 仍需上述 enriched jet package。

文档 076 证明更一般的 scalar-filter no-go：同一 scalar divisor current 的
任意 linear filter family 在 repeated ordinate 仍只产生 rank-one atom；
minimal eigenspace multiplicity 必须由 matrix-valued atom rank实现。

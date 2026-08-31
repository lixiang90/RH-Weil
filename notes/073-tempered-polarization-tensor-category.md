# Tempered polarization、unitarization 与 Weil tensor category

文档 001 的 PLF theorem 使用 exact positive similitude；文档 058 的 FPW
theorem 只要求随 scale 的 subpower Hodge growth。两者之间需要一个抽象
bridge：中心线结论究竟需要 exact unitarity，还是只需要 normalized dynamics
在正反时间均不出现 exponential drift？

本笔记证明后者已经足够。uniform bounded dynamics 还可反向构造一个等价
positive polarization，使 normalized Frobenius/flow 精确 unitary。由此得到一
个对 direct sum、tensor、dual、subquotient 与 Schur functors 封闭的广义
Weil category，并明确 filtered FPW 在其中属于 cyclic tempered object，而
不是尚未构造出的完整 cohomology。

## 1. Two-sided tempered Frobenius modules

固定 `q>1`。一个 weight-`w` **tempered polarized Frobenius module** 是
finite-dimensional Hermitian space `(V,h)`、invertible `F`，使 normalized
operator

`U=q^(-w/2)F`                                      (1)

满足：对每个 `epsilon>0`，存在 `C_epsilon` 使

`||U^n||_h<=C_epsilon exp(epsilon|n|)`, `n in Z`.   (2)

若式 (2) 可加强为 `sup_(n in Z)||U^n||_h<infinity`，称为 **strong**。

### 定理 NB（tempered polarization forces purity）

对任意 tempered polarized Frobenius module，

`Spec(F) subset {alpha:|alpha|=q^(w/2)}`.           (3)

换言之，exact Hodge similitude 可放宽为任意 two-sided subexponential
distortion，而不改变 Weil weight conclusion。

#### 证明

由 spectral-radius formula 与式 (2)，

`r(U)=lim_(n->infinity)||U^n||^(1/n)<=1`.           (4)

对 `U^(-1)` 同理有 `r(U^(-1))<=1`。若 `lambda in Spec(U)`，则
`lambda^(-1) in Spec(U^(-1))`，所以同时有 `|lambda|<=1` 与
`|lambda|>=1`。故 `|lambda|=1`，乘回 `q^(w/2)` 得式 (3)。`□`

finite dimension 中反向也成立：若全部 eigenvalues 在单位圆上，则 Jordan
normal form 给 `||U^n||+||U^(-n)||=O(n^r)`，因而式 (2) 成立。于是 temperedness
精确检测 purity，但不自动检测 semisimplicity。

## 2. Uniform dynamics reconstructs exact polarization

固定一个 reference metric，设

`sup_(n in Z)||U^n||<=M`.                           (5)

定义 finite Cesaro orbit metric

`H_N=(1/(2N+1))sum_(n=-N)^N (U^n)^*U^n`.           (6)

### 定理 NC（bounded unitarization theorem）

在式 (5) 下，存在 positive definite Hermitian operator `H_infinity`，满足

`M^(-2)I<=H_infinity<=M^2I`,                       (7)

`U^*H_infinity U=H_infinity`.                      (8)

因此新内积 `h_infinity(x,y)=h(H_infinity x,y)` 与原内积等价，并使

`h_infinity(Fx,Fy)=q^w h_infinity(x,y)`.           (9)

在 finite dimension，strong modules 恰是 diagonalizable pure modules。

#### 证明

式 (5) 及其对 inverse 的应用给

`M^(-1)||x||<=||U^n x||<=M||x||`,                 (10)

所以每个 `H_N` 满足式 (7)。finite-dimensional compactness 给 convergent
subsequence `H_(N_j)->H_infinity`。另一方面，

`U^*H_NU-H_N`

`=[(U^(N+1))^*U^(N+1)-(U^(-N))^*U^(-N)]/(2N+1)`. (11)

其 norm 为 `O(M^2/N)`；取极限得到式 (8)，式 (9) 随即成立。
exact unitary operators 可对角化，故 strong 推出 semisimple。反之，若
`U=SDS^(-1)` 且 `D` diagonal unitary，则 `||U^n||<=||S||||S^(-1)||`，得到
strong。`□`

式 (6) 是从 dynamics 构造 polarization 的非循环有限算法；真正困难被放在
证明 two-sided uniform orbit bound，而不是先猜 inner product。

## 3. Rigid tensor closure

令 morphisms 为 intertwining linear maps。允许按 weight 分次取 direct sum。

### 定理 ND（tempered Weil tensor category）

tempered modules 在以下操作下封闭：

1. 同 weight direct sums；
2. tensor product，weight 从 `(w_1,w_2)` 变成 `w_1+w_2`；
3. contragredient dual，weight `w` 变成 `-w`；
4. invariant subobjects 与 quotient objects；
5. fixed-degree symmetric、exterior 及一般 Schur functors；
6. Tate twist `F mapsto q^(-r)F`，weight `w mapsto w-2r`。

strong modules 对同一组操作也封闭，并形成 semisimple rigid tensor
subcategory。tempered category 本身一般不 semisimple；unit-circle Jordan
blocks 是 polynomial-growth counterexamples。

#### 证明

tensor normalized operator 是 `U_1 tensor U_2`，故

`||(U_1 tensor U_2)^n||<=||U_1^n||||U_2^n||`;       (12)

两个 subexponential bounds 的乘积仍 subexponential。direct sum 取 maximum。
dual normalized operator 是 `(U^(-1))^*`，所以正反 powers 继承同一 bound。
restriction 与 quotient operator norm 不增；fixed Schur functors 是 fixed
tensor power 的 invariant subquotients。Tate twist 不改变 normalized `U`。
这些证明对 uniform bounds 同样成立。strong 情形由定理 NC unitarize；
unitary invariant subspace 的 orthogonal complement 仍 invariant，故
semisimple。`□`

这给 PLF/Weil objects 一个真正的 algebraic closure theorem，而不仅是逐个
zeta function 的谱位置断言。

## 4. Determinants and weights under operations

### 定理 NE（tempered Lefschetz determinant theorem）

对 weight-`w` tempered module 定义 rational factor

`Z_F(T)=det(1-TF)^(-1)`                             (13)

或其任意整数次幂。它的 reciprocal zeros/poles 全满足

`|alpha|=q^(w/2)`.                                 (14)

令 `T=q^(-s)`，相应 divisor 位于

`Re s=w/2`.                                        (15)

direct sum 对应 factors 相乘；tensor product 的 reciprocal roots 是
`alpha_i beta_j`，故 weights 相加；dual 取 reciprocal roots；degree-`r`
Schur functor 产生 weight `rw`。

#### 证明

定理 NB 给式 (14)。方程 `1-alpha q^(-s)=0` 取 absolute value 得式 (15)。
其余陈述来自 determinant 与 eigenvalues 对相应线性代数操作的标准公式。
`□`

必须区分：这里的 tensor determinant 是由两个 **global Frobenius modules**
构造的新 rational factor。对 number-field Rankin--Selberg L-function，局部
Satake parameters 虽按 tensor 相乘，但 global zero space 不是两个旧 zero
spaces 的朴素 tensor product；仍需独立 global trace/determinant theorem。

## 5. Continuous tempered polarization theorem

令 `(G_t)_(t in R)` 是 Hilbert space 上的 strongly continuous invertible
group，generator 为 closed operator `B`。

### 定理 NF（tempered flow centerline theorem）

若对每个 `epsilon>0`，

`||G_t||<=C_epsilon exp(epsilon|t|)`,               (16)

则

`Spec(B) subset iR`.                               (17)

因此对任意 real `c`，`Theta=c/2+B` 的 spectrum 位于
`Re s=c/2`。若进一步 `sup_t||G_t||<=M`，则存在 equivalent positive
inner product 使 `G_t` unitary；在该内积下

`Theta^*=c-Theta`.                                 (18)

#### 证明

若 `Re lambda>0`，在式 (16) 中取 `epsilon<Re lambda`，则

`(lambda-B)^(-1)=int_0^infinity e^(-lambda t)G_tdt` (19)

norm-convergent。`Re lambda<0` 使用 backward group 的对应积分。因此
`C\iR` 属于 resolvent set，证明式 (17)。

uniform 情形定义

`H_T=(1/(2T))int_(-T)^T G_t^*G_tdt`.               (20)

与定理 NC 相同，`M^(-2)I<=H_T<=M^2I`。取 weak-operator cluster point
`H_infinity`；对 fixed `s`，平移积分区间只留下总长 `2|s|` 的 boundary，
故 `G_s^*H_infinity G_s=H_infinity`。新内积中 `G_t` unitary，Stone theorem
说明 `B^*=-B`，得到式 (18)。`□`

若完成函数有不使用 divisor 实部构造的正规化 determinant/trace identity

`Lambda(s)=E(s)det_infinity(s-Theta)`,              (21)

且 `E` 的 divisor 已知，则定理 NF 给 number-field 形式的广义 Weil
centerline theorem。它严格弱化文档 001 定理 E 的先验 exact adjoint 公理。

## 6. PLF 与 FPW 的统一接口

### 定理 NG（exact、strong 与 filtered Weil structures）[U]

三种结构的逻辑关系如下：

1. PLF 的 degree-`n` cohomology 由文档 001 定理 B 满足 exact similitude
   `F^*hF=q^n h`，故给 weight-`n` strong module；
2. strong FPW 的 covariant Gram completion 给 uniformly bounded translation
   group，定理 NF 重建 exact polarization 与 `Theta^*=c-Theta`；
3. filtered FPW6 在 scale `X=e^t` 上给 distinguished arithmetic cyclic
   orbit 的 forward subexponential Hodge growth；functional equation/dual
   package 提供 backward direction，而修订后的 FPW4b quantitative dual
   separation 把每个 fixed off-center mode 转成范数下界；这才是定理 NB 的
   cyclic/divisor 版本。定性 visibility 本身不够。

所以 filtered FPW 不是形式上模仿 PLF：它把 exact Frobenius similitude放宽为
two-sided tempered polarization，同时保留相同的 weight conclusion。

#### 证明

1 是 PLF 计算 `h(Fx,Fy)=q^n h(x,y)`。2 是文档 058 定理 JP 的 GNS group
配合定理 NF 的 unitarization。对 3，divisor mode `rho` 在 normalized orbit
中的幅度是

`exp[(rho-c/2)t]m_t(rho)`, `m_t(rho)=exp(o(t))`.    (22)

若 `Re rho>c/2`，FPW4b 给 dual functional `ell_t`，其 norm 为 `exp(o(t))`，
而 `|ell_t(v_t)|>=exp[(Re rho-c/2)t-o(t)]`。dual Cauchy--Schwarz 因而迫使
`||v_t||` 有同一 exponential lower growth，与 FPW6 的 `exp(o(t))` bound
矛盾；dual symmetry 排除左侧。这是修订后的文档 058 定理 JO。若只有定性
visibility，上述范数下界并不成立。`□`

文档 163 进一步证明：对 Mellin-coherent fixed-annulus adaptive Sobolev
carrier，compact-frequency extractor 的 dual norm 为 `exp[O(r_X)]`；当
`r_X=o(logX)` 时即为 `exp(o(t))`。所以 zeta 的这一具体 carrier 已严格满足
第 3 项所需的 FPW4b，而任意 filtered Gram 仍不能由定性 visibility 自动推出。

注意 FPW6 只控制 actual cyclic vector 时，得到的是 divisor purity，不自动
得到 operator-wide uniform boundedness或 semisimplicity；只有 strong
covariant frame hypotheses 才允许定理 NF 构造完整 Hilbert--Pólya operator。

## 7. Arithmetic existence audit

### 命题 NH（non-circular existence boundary）

- finite fields：Weil cohomology、Hard Lefschetz 与 Hodge--Riemann positivity
  给 exact/strong objects，定理 NE 无条件恢复各 weight line；
- classical zeta：文档 058 的 finite carriers（FPW1–FPW3、FPW4a、FPW5）、
  文档 163 对 adaptive Sobolev carrier 的 FPW4b，以及文档 071–072 的 local
  scalar/bridge positive fibers 与 normalized dilation correspondences 均
  无条件存在；
- primitive Dirichlet L-functions：paired Gamma factors、finite unitary Euler
  phases 与 positive fibers 无条件存在，但 global tempered arithmetic orbit
  bound 仍等价于 GRH；
- fixed-degree automorphic data：在 theorem JU 的 Rankin--Selberg/local
  hypotheses 下 finite tempered carrier 存在；若 local temperedness 本身是
  Ramanujan input，则不能把它计作无条件。

对 zeta，尚缺的断言可等价写成以下任一种：

`||U^t v_arith||=exp(o(|t|))`（filtered），          (23)

`sup_t||U^t v_arith||<infinity`（strong local family）， (24)

或文档 072 的 finite rank-one endpoint bound

`R_X=O(X^2)`.                                      (25)

这些不是从定理 NB/NF 自动产生的；它们正是需要 prime-side arithmetic
cancellation 的 Hodge--Riemann content，并分别具有 RH/GRH 的全部强度。

本笔记的新增存在性结论是：一旦能独立证明 uniform orbit bound，就无需再
猜测极化或 adjoint identity；Cesaro averages (6)/(20) 会从 arithmetic
dynamics 自动、正定且无循环地构造它们。当前开放点因此从“同时构造内积与
证明中心线”缩成“在已经存在的 finite positive carriers 上证明双向
tempered/uniform orbit bound”。

文档 074 进一步计算这些 Cesaro metrics 的 exact Lyapunov exponent，并
证明其 exponential growth 检测 weight、polynomial growth 检测 Jordan
depth；这把 tempered/uniform orbit hypotheses 变成 cofinal finite PSD
matrix certificates。

文档 075 证明 exterior-power slopes 在本 tensor category 中按 direct union、
pairwise sum、dual negation 与 Schur weight sums 变换，因而得到一个
multiplicity-sensitive weight-polygon functor。

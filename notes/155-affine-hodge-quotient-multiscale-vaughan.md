# Affine Hodge 商范数与多 cutoff Vaughan gauge

文档 154 消除了 continuum 分配的任意性，但仍固定一对 Vaughan cutoffs
`(U,V)`。不同 cutoffs给不同 Type I/II components，却都精确重构同一个
`Lambda`。因此 cutoff choice本身也是一个零和 gauge。

本节把有限组 exact decompositions放进同一个 affine Hodge quotient，联合优化：

- 各 cutoff decomposition的混合权重；
- continuum在 component categories间的 shares。

所得 quadratic program只用 finite positive Gram data。无约束 affine optimum给
理论下界；对 cutoff weights施加 simplex constraint则给稳定、无负权放大的规范
版本。

## 1. 多分解 gauge

令 `H` 为 Hilbert space。对 `j=1,...,J`，假设同一个向量 `p` 有 `R` 项 exact
decomposition

`p=sum_(r=1)^R p_(j,r)`.                           (1)

另取 nonzero background vector `c`。给实数 `w_j,alpha_r`，满足

`sum_jw_j=1`,        `sum_ralpha_r=1`,             (2)

并定义

`v_r(w,alpha)=sum_jw_jp_(j,r)-alpha_r c`.         (3)

### 定理 ABE（multi-decomposition gauge conservation）

每个满足式 (2)的 gauge都满足

`sum_rv_r=p-c`.                                    (4)

因此完整 Hodge energy `||p-c||^2` 与 `(w,alpha)` 无关，并有

`||p-c||^2<=R D(w,alpha)`,

`D(w,alpha)=sum_r||v_r(w,alpha)||^2`.              (5)

#### 证明

对式 (3)先对 `r` 求和，再用式 (1)--(2)：

`sum_rv_r=sum_jw_jp-(sum_ralpha_r)c=p-c`.          (6)

式 (5)是 Cauchy--Schwarz。`□`

所以 `D` 是 decomposition-dependent 的安全预算，而 `||p-c||^2` 是 quotient
中的 gauge invariant physical energy。

## 2. Gram--KKT 闭式结构

令实变量向量

`z=(w_1,...,w_J,alpha_1,...,alpha_R)^T`.           (7)

定义 real symmetric matrix `Q` 的 blocks：

`Q_(w_j,w_k)=sum_r Re<p_(j,r),p_(k,r)>`,

`Q_(w_j,alpha_r)=-Re<p_(j,r),c>`,

`Q_(alpha_r,alpha_s)=delta_(r,s)||c||^2`.          (8)

则直接展开给

`D(w,alpha)=z^TQz`.                                (9)

令 `A` 是两行 constraint matrix，第一行对全部 `w` 为 `1`，第二行对全部
`alpha` 为 `1`，并令 `b=(1,1)^T`。

### 定理 ABF（affine Hodge quotient minimizer）

`Q` 为 positive semidefinite。式 (2)上的全部 minimizers恰由 KKT system

`[Q  A^T][z     ]=[0]`,

`[A   0 ][lambda]=[b]`                             (10)

给出；若 `Q` 在 `ker A` 上 positive definite，则解唯一。所得

`D_aff=min_(Az=b)z^TQz`                            (11)

是由给定 decomposition family与 background span确定的 canonical affine
Hodge quotient norm。

#### 证明

式 (9)是 direct-sum Hilbert norm的 Gram form，故 `Q>=0`。对 equality-constrained
convex quadratic作一阶 variation得到式 (10)；凸性使每个 stationary solution
为 global minimizer。`ker A`上的 strict positivity给唯一性。若存在 null gauge，
先除去该 nullspace或使用 Moore--Penrose解，最小值不变。`□`

实现 `constrained_real_quadratic_minimizer` 直接解式 (10)，并返回 constraint与
stationarity residual。

## 3. Stable simplex gauge

无约束式 (11)允许负 `w_j`。对 exact vectors这仍是合法恒等分解，但 finite
truncation或 quadrature error会被

`L_w=sum_j|w_j|`                                   (12)

放大。稳定版本要求

`w_j>=0`,       `sum_jw_j=1`,                      (13)

而 continuum shares `alpha_r` 仍只满足 affine constraint。

### 定理 ABG（simplex optimum and error stability）

在式 (13)与 `sum alpha=1` 下，`D` 有 global minimizer `D_simp`，且

`D_aff<=D_simp<=min_jD_j`,                         (14)

其中 `D_j` 是只使用第 `j` 个 decomposition并最优分配 continuum的预算。

若 finite approximants满足

`||p_tilde_(j,r)-p_(j,r)||<=eta_(j,r)`,

`||c_tilde-c||<=eta_c`,                            (15)

则令

`E_gauge^2=sum_r[sum_j|w_j|eta_(j,r)`

`                         +|alpha_r|eta_c]^2`,     (16)

有

`|sqrt(D_tilde)-sqrt(D)|<=E_gauge`.                (17)

特别地，simplex gauge固定有 `L_w=1`。

#### 证明

simplex乘 affine hyperplane上的 quadratic为 coercive modulo its nullspace；有限维
closed convex minimization给 minimizer。单个 vertex `w_j=1` 都可行，故右侧
不等式；放松 nonnegativity给左侧。近似 component误差为

`d_r=sum_jw_je_(j,r)-alpha_re_c`.                  (18)

triangle inequality给式 (16)内每项；在 direct sum `H^R` 中使用 reverse triangle
inequality得到式 (17)。`□`

实现 `simplex_scale_affine_quadratic_minimizer` 枚举所有 nonempty cutoff faces；
每个 face用定理 ABF求内部 optimum，拒绝负 active weights，再取全部 feasible
faces的最小值。因此对最多 12 个 cutoffs它给 finite global optimum，不是局部
优化 heuristic。

## 4. 多 cutoff Vaughan specialization

对每对 `(U_j,V_j)`，文档 153 定理 AAV给四项未中心化 exact decomposition

`Lambda=P_(j,1)+P_(j,2)+P_(j,3)+P_(j,4)`.         (19)

加 Abel weight、vertical modulation与 interval-incidence feature，得到式 (1)的
`p_(j,r)`；文档 154 式 (13)给 `c`。

### 定理 ABH（multiscale Vaughan--Hodge center-line criterion）

对每个 square-root-core block取任意 finite cutoff family，并令 `D_simp(Y,k)` 为
定理 ABG的 stable optimum。若 exact vectors满足

`sup_Y sum_(k in core)D_simp(Y,k)/beta_(Y,k)<infinity`, (20)

则 RH成立。

若只计算 finite approximants，则更强但完全可认证的充分条件是

`sup_Y sum_(k in core)`

` [sqrt(D_tilde_simp(Y,k))+E_gauge(Y,k)]^2/beta_(Y,k)<infinity`. (21)

对具有有限组 exact convolution decompositions的 Gamma--Euler data，同一结论
成立，常数 `4` 换成 component count `R`。

#### 证明

由定理 ABE，完整 energy至多 `4D_simp`。式 (20)遂给文档 151 定理 AAO的
modulated-energy budget；core exterior由文档 150 定理 AAK处理。式 (17)说明
式 (21)推出式 (20)。一般 `R` 项相同。`□`

这进一步证明所需结构的 finite-level existence：对任意 finite cutoff family，
Gram、KKT quotient、simplex optimum及 error leverage都由 primes、Möbius函数与
positive continuum kernel无条件构造。未证的仍是式 (20)或式 (21)的 uniform
dyadic bound。

## 5. Finite multiscale audit

取 `delta=.1,theta=.25,h=theta/T`，continuum在 `[0,log(N+1)]` 上作 20-cell
geometric midpoint quadrature。`D_free` 是定理 ABF的无约束值，`D_simp` 是
stable simplex值，`D_best` 是候选中的最佳单 cutoff：

| `N,Y,T` | cutoff pairs | `D_free` | `D_simp` | `D_best` | simplex gain |
|---:|:---|---:|---:|---:|---:|
| `80,30,2` | `(2,3),(4,5),(6,7),(8,9)` | `.53885` | `.54085` | `.56068` | `3.54%` |
| `80,30,8` | same | `.14574` | `.14574` | `.15553` | `6.29%` |
| `160,60,2` | `(3,4),(6,7),(9,10),(12,13)` | `1.04705` | `1.07204` | `1.11345` | `3.72%` |
| `160,60,8` | same | `.27041` | `.27051` | `.27777` | `2.61%` |

simplex scale weights分别为

`(.232,.451,0,.317)`,

`(.523,.239,.058,.179)`,

`(.608,0,.392,0)`,

`(.678,0,.276,.047)`.                              (22)

无约束 weights的 `L_w` 分别约 `1.66,1,2.63,1.21`。负权只比 simplex多改善
`0%--2.3%`，却明显增加前两项低频 audit中的 error leverage。因此 stable simplex
是更合理的 proof target；free optimum保留为 decomposition family能够达到的理论
下界。

全部 continuum shares在这些 samples中仍为正且接近文档 154 的 equal split。
完整 physical energy在 free/simplex/single gauges间数值不变；表中的变化只来自
component-diagonal majorant。continuum tail及 midpoint localization仍按文档 154
定理 ABC单独计入，故表不是 RH evidence。

## 6. 结论与下一步

多 cutoff优化确实降低预算，但 finite gain只有几个百分点。这排除了“仅调 Vaughan
cutoffs就会产生数量级突破”的期待。下一步应把精力放在：

1. 对 simplex active cutoffs统一证明 Type I/II rectangle bounds；
2. 使用式 (16)把 prime tail与 continuum localization误差严格传递到 finite Gram；
3. 构造 matrix-valued而非 diagonal-only Bessel bound，以保留四个 component
   categories之间更大的 cross cancellation；
4. 审计 `D_simp` 随 `Y,T` 的 growth exponent，判断 diagonal criterion是否本身过强。

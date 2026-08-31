# NCE-1：有限正算术锥、秩一分离证人与 Type II rectangle

文档 174 的定理 AEI--AEJ 把最优安全 predictor 的存在性化成 closed arithmetic
cone 的投影与 polar-separator bound。本笔记完成该路线的第一个有限层目标：
在有限采样或有限 correspondence Gram 上，polar cone 不再是抽象对象，而由
显式 evaluation normals 或 rank-one Gram packets生成；任意证人在消去
arithmetic annihilator 后只需有限多个原子。

该结论是构造性的：给定 arithmetic synthesis matrix 与有限 lag set，cone、
dual witnesses、KKT complementarity 和 obstruction complexity均可直接计算。
它没有证明统一高度估计；新的开放输入是这些 rank-one packets能否由
threshold boundary shells统一控制。

## 1. 有限 evaluation cone

令 `H=R^m`，赋予内积

`<x,y>_W=x^T W y`,                              (1)

其中 `W` 正定。令 `A subset H` 是维数 `r` 的 arithmetic subspace，并以满列秩
矩阵 `Phi:R^r->R^m` 表示。定义

`K=A cap R_+^m`.                                (2)

记 `e_i` 为标准基，evaluation normal 为

`n_i=W^(-1)e_i`,                                (3)

于是 `<n_i,x>_W=x_i`。记 `A_W^perp` 为 `W`-正交补。

### 定理 AEK（finite arithmetic cone Farkas theorem）[U]

`K` 的 polar cone 精确为

`K^o=A_W^perp+cone{-n_1,...,-n_m}`.             (4)

在 quotient `H/A_W^perp` 中，

`K^o/A_W^perp`

` =cone{-pi(n_1),...,-pi(n_m)}`.                (5)

因此：

1. quotient cone 的每条 extreme ray由某个 projected evaluation normal生成；
2. 每个 polar class可由至多 `r` 个 evaluation normals的非负组合表示。

#### 证明

`A` 是线性子空间，故 `A^o=A_W^perp`。正 orthant 对式 (1) 的 polar 为

`(R_+^m)^o=cone{-W^(-1)e_i:1<=i<=m}`.           (6)

有限维 closed convex cones满足

`(A cap R_+^m)^o=A_W^perp+(R_+^m)^o`;           (7)

也可直接由有限维 Farkas lemma得到。式 (4)--(5)随即成立。有限生成 cone 的
extreme rays来自其生成 rays；quotient dimension不超过 `r`，conic
Caratheodory theorem又把任意元素约化为至多 `r` 个生成元。`□`

这里“有限复杂度”依赖 `r=dim A`，而不依赖 ambient sample数 `m`。这是真进展，
但还不是 uniform theorem：若 `r` 随高度快速增长，Caratheodory bound仍可能
承载完整 RH obstruction。

## 2. Projection 的 KKT 证书

固定 `X in H`，令

`E^*=proj_K X`, `Y^*=X-E^*`.                    (8)

### 定理 AEL（atomic KKT certificate）[U]

存在 `z in A_W^perp` 与 `lambda_i>=0`，使

`Y^*=z-sum_i lambda_i n_i`,                     (9)

`lambda_i E_i^*=0` 对每个 `i`，且

`dist_W(X,K)^2=||Y^*||_W^2`.                    (10)

反过来，若 `E in K`、`Y=X-E` 满足式 (9)与 complementarity，则
`E=proj_KX`。

#### 证明

metric projection的特征条件是 `Y^* in K^o` 与
`<Y^*,E^*>_W=0`。由定理 AEK写成式 (9)。因 `z` 消灭 `A`，

`0=<Y^*,E^*>_W=-sum_i lambda_iE_i^*`.           (11)

各项非正，故逐项 complementarity成立。反向条件给
`<Y,E'-E>_W<=0` 对每个 `E' in K`，正是 projection variational
inequality。`□`

因此非构造 projection可以由一个完全有限的 active-set certificate认证：
只需给出 `E,z,lambda` 并检查线性等式、非负性与 complementarity。

## 3. Finite correspondence Gram 的 rank-one dual

evaluation positivity依赖所选 sample points。长度侧更自然的有限条件是
positive-definite Gram。令 `V` 是 `r` 维实 predictor space，`L:V->Herm_N`
是线性 Gram pencil，定义

`K_L={v in V:L(v)>=0}`.                         (12)

假设 Slater 条件：存在 `v_0` 使 `L(v_0)>0`。以任意固定内积识别 `V` 与其对偶，
记 `L^*` 为 adjoint。

### 定理 AEM（rank-one correspondence separator theorem）[U]

在 Slater 条件下，

`K_L^o={-L^*(Q):Q>=0}`.                         (13)

每个 dual witness都能写成

`-sum_(j=1)^s L^*(u_ju_j^*)`, `s<=r`.           (14)

若 `v^*=proj_(K_L)x`，则存在 `Q>=0` 使

`x-v^*=-L^*(Q)`,                                (15)

`Tr[Q L(v^*)]=0`.                               (16)

`Q` 可取为至多 `r` 个 rank-one packets之和。

#### 证明

semidefinite Farkas lemma与 Slater 条件给式 (13)及 closedness。谱分解把
`Q` 写成 rank-one正和；再在维数 `r` 的 image `L^*(Herm_N)` 中应用 conic
Caratheodory theorem，得到式 (14)。projection normal-cone条件给式 (15)，
而 `<-L^*(Q),v^*>=-Tr[Q L(v^*)]=0` 给式 (16)。正矩阵之间 trace配对为零
也等价于 `Q^(1/2)L(v^*)Q^(1/2)=0`。`□`

对 capped finite correspondence effect

`0<=L(v)<=G_kappa`,                             (17)

同一 KKT 论证给两个 PSD witnesses `Q_-,Q_+`：

`x-v^*=-L^*(Q_-)+L^*(Q_+)`,                    (18)

`Tr[Q_-L(v^*)]=0`,                              (19)

`Tr[Q_+(G_kappa-L(v^*))]=0`.                    (20)

所以 lower/upper cap obstruction分别集中在 active zero与active saturation
subspaces；两类 witnesses都可分解为 rank-one packets。

## 4. Type II rectangle 的显式解释

固定有限 dyadic rectangle

`D subset (U,2U]`, `M subset (V,2V]`,           (21)

列出 product atoms `q_alpha=d_alpha m_alpha`，并取 shared lags

`lambda_(alpha,beta)=log(q_alpha/q_beta)`.       (22)

对 arithmetic predictor `r_v(lambda)` 定义

`L_R(v)=[r_v(lambda_(alpha,beta))]_(alpha,beta)`. (23)

每个 rank-one witness `u u^*` 对 predictor的作用为

`Tr[u u^* L_R(v)]`

` =sum_(alpha,beta)conj(u_alpha)u_beta`

`   r_v(log(q_alpha/q_beta))`.                  (24)

式 (24)正是一个有限 near-product quadratic packet。它完整保留：

- `dm` 与 `d'm'` 的 multiplicative collision；
- vertical modulation；
- Gram cross terms；
- prime/continuum/Gamma在 predictor中预先完成的 joint gluing。

于是 NCE-1 的有限层结论是：

> 每个 finite Type II correspondence obstruction，均可约化为至多
> `dim V` 个 rank-one near-product packets，而不必搜索任意 matrix-valued
> effect。

这个 reduction严格弱于证明这些 packets的统一界。`u` 仍可能是 product atoms上
的任意向量；若允许的 `u` 随 rectangle维数变得任意，式 (24)仍可恢复 full
physical Gram，文档 165 的 no-free-lunch障碍没有消失。

## 5. 与 threshold boundary 的下一接口

文档 166 的 one-vertex shell formula说明 Möbius defect只来自
`U/p<d<=U` 的未配对 faces。因而下一目标不再是“描述 polar cone”——这已由
定理 AEK/AEM完成——而是证明 rank-one vectors `u` 的 arithmetic action可压到
这些 boundary shells。

一个可证伪的目标是：存在 boundary synthesis `S_R` 与 annihilator error
`Z_R`，使每个 active rank-one packet满足

`L_R^*(u u^*)=S_R^*omega+Z_R`,                  (25)

其中 `omega` 支撑于阈值壳，且

`||omega||^2<=C ||u||^4`                        (26)

的 `C` 不随 rectangle与高度增长。若式 (25)--(26)成立，polar bound可转化为
文档 166 的 gcd Gram与 shell incidence；若最小 `C` 随 product multiplicity
无界增长，则 NCE-1在该 carrier上应降级。

## 6. 审计结论

本笔记无条件完成：

1. finite evaluation polar cone的原子分解；
2. 最优 predictor的 active-set KKT证书；
3. finite correspondence Gram dual的 rank-one分解；
4. Type II obstruction到 near-product packets的精确识别。

尚未完成：

1. rectangle-uniform boundary-shell factorization式 (25)--(26)；
2. rank-one packets除以 Cauchy barrier后的可和性；
3. cofinal finite Gram条件向完整 correspondence cone的无损极限。

因此这是构造性路线的有限结构定理，不是 RH 证明。它把下一步从“寻找未知
separator”缩成了一个明确的 rank-one boundary factorization问题。

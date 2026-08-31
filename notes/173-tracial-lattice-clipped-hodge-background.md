# Tracial lattice clipping 与无四阶代价的 Hodge background

文档 171 的 linear Schur background需要 pointwise amplitude；文档 172 用 universal
quadratic lift删除 amplitude，却支付 weighted fourth moment。本笔记先证明该四阶
代价存在一个不可忽略的 capacity lower bound，再给出一个更强的修复：在有限迹
代数中对 predictor 作 fixed relative spectral clipping。所得 background自动严格
为正，而 negative index只由一个 clipped quadratic residual控制。

这里的 clipping只作用于由 primes、Gamma、continuum 与有限 correspondences
构造的 predictor，不作用于未知 divisor 的零点投影，也不把 `H_-` 放进定义。
因此它不同于文档 147 警告的“用未知 positive/negative spectral part定义背景”。

主要结论：

1. 文档 172 的 unscaled fourth moment满足 sharp capacity必要条件；
2. reciprocal-barrier upper bound扩展到任意有限 von Neumann algebra，不要求
   background与 current对易；
3. relative continuous functional calculus给 canonical clipped predictor；
4. bounded clipped residual推出 bounded finite-trace index，继而推出中心线；
5. 对 zeta，下一目标可从 `(Schur residual)+(fourth moment)` 进一步替换为一个
   one-sided quadratic approximation problem。

## 1. Quartic capacity audit

在有限 measure block上令 `B_0>0`，并定义

`D(C)=int C^2/B_0 dmu`,

`P_4(C)=int C^4/B_0^3 dmu`,

`M_0=int B_0 dmu`.                               (1)

### 定理 AED（quartic-capacity lower bound）[U]

对每个 real `C`，

`P_4(C) M_0>=D(C)^2`.                            (2)

常数 `1` sharp；当 `C/B_0` 几乎处处为常数时取等。

#### 证明

把 `D(C)` 写成

`int [C^2/B_0^(3/2)] B_0^(1/2)dmu`，

再用 Cauchy--Schwarz即得式 (2)。等号条件也是 Cauchy--Schwarz等号条件。`□`

对文档 172 的 harmonic projection，`D=d^TG^dagger d`。在 zeta dyadic shell
`I_T` 上，

`dmu asymp dt/T^2`, `B_(0,T)asymp log T`,

且 shell宽度为 `asymp T`，所以

`M_(0,T)=int_(I_T)B_(0,T)dmu asymp log T/T`.      (3)

因此 unscaled fourth price必满足

`P_(4,T)^* >= T D_T^2/log T`.                    (4)

式 (4)不是 RH 障碍的证明，但它是严格必要性审计：若文档 172 的 full Schur
predictor满足 `sum_T P_(4,T)^*<infinity`，则必须有

`sum_T T D_T^2/log T<infinity`.                  (5)

所以 generic fourth-moment或 pair-collision bound只有在 gain `D_T` 已相当小时
才可能闭合；不能默认第四矩总是比 pointwise leverage便宜。缩放 predictor可缓解
式 (4)，但也同时失去 Schur gain。

## 2. 非交换 reciprocal-barrier upper bound

令 `(M,tau)` 是 finite von Neumann algebra，`tau` 为 faithful normal finite trace。
对 self-adjoint `H` 与 strictly positive invertible `B`，定义

`Q_B(H)=1/4 tau[(H-B)B^(-1)(H-B)]`.              (6)

### 定理 AEE（tracial operator reciprocal barrier）[U]

有

`tau(H_-)<=Q_B(H)`.                              (7)

该结论不要求 `H` 与 `B` 对易。若代数可交换，取 infimum over `B>0` 恢复文档
171 的 exact reciprocal-barrier identity。

#### 证明

有限迹负部的 variational formula给

`tau(H_-)=sup_(0<=E<=1)-tau(HE)`.                 (8)

置 `X=H-B`、`q=tau(XB^(-1)X)`、`y=tau(BE)`。tracial
Hilbert--Schmidt Cauchy--Schwarz给

`|tau(XE)|`

` =|tau(B^(-1/2) X E B^(1/2))|`

` <=q^(1/2) tau(BE^2)^(1/2)`

` <=q^(1/2)y^(1/2)`,                             (9)

因为 `0<=E^2<=E`。于是

`-tau(HE)<=sqrt(qy)-y<=q/4`.                     (10)

对 effects取 supremum即得式 (7)。`□`

这一定理把 scalar spectral measure版本提升成真正的 tracial Hodge index工具：
background可以是 matrix-valued、operator-valued，且可以与 arithmetic current
不对易。

## 3. Relative lattice clipping

固定 strictly positive invertible `B_0`、self-adjoint residual `R`，写

`H=B_0+R`.                                       (11)

给定任意 self-adjoint predictor `C` 与 `0<epsilon<1`，令

`U=B_0^(-1/2) C B_0^(-1/2)`,

`phi_epsilon(x)=max{x,-(1-epsilon)}`,             (12)

并定义 relative clipped predictor

`C^[epsilon]=B_0^(1/2)phi_epsilon(U)B_0^(1/2)`.  (13)

### 定理 AEF（lattice-clipped Hodge background）[U]

背景

`B^[epsilon]=B_0+C^[epsilon]`

满足 Loewner lower bound

`B^[epsilon]>=epsilon B_0>0`,                    (14)

并且

`tau(H_-)`

` <=1/(4epsilon)`

`   *tau[(R-C^[epsilon])B_0^(-1)`

`                         (R-C^[epsilon])]`.      (15)

#### 证明

由 functional calculus，

`I+phi_epsilon(U)>=epsilon I`，

左右乘 `B_0^(1/2)` 得式 (14)。对定理 AEE 取背景 `B^[epsilon]`。
此时 `H-B^[epsilon]=R-C^[epsilon]`。又由 inverse order，

`(B^[epsilon])^(-1)<=epsilon^(-1)B_0^(-1)`.      (16)

把式 (16)放入式 (6)并利用 trace positivity，即得式 (15)。`□`

在 commutative spectral model中，式 (13)只是

`C^[epsilon](chi)=max{C(chi),-(1-epsilon)B_0(chi)}`. (17)

因此式 (15)等于

`1/(4epsilon) int (R-C^[epsilon])^2/B_0 dmu`.    (18)

它具有明确的 one-sided 结构：

- 在 `C>=-(1-epsilon)B_0` 的安全区域，residual仍是 `R-C`；
- 在 predictor越过负 barrier的区域，residual变成
  `R+(1-epsilon)B_0`，不再支付 `C^4`；
- predictor的巨大正值不因 positivity lift本身产生 quartic price。

文档 171 的反例也被正确捕获：若 `B_0=1`、`R=C=-L-1`，则 clipped predictor
为 `-(1-epsilon)`，式 (18)仍看到 `L+epsilon` 的大 residual。

## 4. Correspondence algebra 的 closure

若 `A` 是 unital C-star algebra，`B_0,C in A_sa` 且 `B_0` invertible，则式
(12)--(13)仍属于 `A_sa`：square root、inverse与 fixed continuous function
`phi_epsilon` 都由 continuous functional calculus给出。

在 commutative orbit model中，若 block compact、`B_0,C` continuous，则
`C^[epsilon]` 可由 `C/B_0` 的 polynomials一致逼近。每个 polynomial power对应
finite orbit measure的 repeated convolution；所以 clipping可以由长度侧
correspondences逼近，而不查询 divisor zeros。若只给 measurable carrier，
则 bounded Borel functional calculus仍在生成的 von Neumann algebra中成立。

这给出一个比“有限 predictor space”更自然的广义结构：

`arithmetic correspondences`

` -> self-adjoint C-star/von Neumann algebra`

` -> relative order functional calculus`

` -> positive clipped Hodge backgrounds`.        (19)

所需 closure是标准 operator-algebra closure，不是额外的零点纯性假设。

## 5. Lattice-clipped bounded-index Weil theorem

### 定理 AEG（tracial lattice Hodge--Weil theorem）[C]

在 bounded finite-trace Hodge--Weil theorem的 Poisson、Euler-germ、self-dual
divisor与 approximation hypotheses下，把每个 approximating current分成不交
blocks `H_(n,j)=B_(0,n,j)+R_(n,j)`。假设每块位于 finite von Neumann algebra，
且有由 arithmetic/Gamma correspondences生成的 self-adjoint predictor
`C_(n,j)`。固定某个 `0<epsilon<1`，按式 (13)定义
`C_(n,j)^[epsilon]`。若

`sup_n sum_j tau_(n,j)[`

` (R_(n,j)-C_(n,j)^[epsilon]) B_(0,n,j)^(-1)`

` (R_(n,j)-C_(n,j)^[epsilon])] <infinity`,       (20)

且已有 approximation errors一致有界，则 divisor的全部非零 zeros位于中心线。

#### 证明

逐 block应用定理 AEF；不交 blocks的 finite-trace negative index相加。式 (20)
给 uniform negative-index bound，再应用 bounded finite-trace Hodge--Weil theorem。
`□`

定理 AEG 是新的广义结构定理接口。它把有限域的“primitive part进入正锥”替换成：
actual arithmetic current可由一个 correspondence predictor在相对 order interval
中作统一 quadratic approximation。该条件对 zeta仍未证明，故标为 `[C]`。

## 6. Zeta 的新 one-sided target

在 shell `I_T` 上取文档 170--172 的显式正 background `B_(0,T)`，并由
threshold-complex、Type I/II 与 joint prime--continuum--Gamma correspondences
构造 predictor `C_T`。定义

`C_T^[epsilon]=max{C_T,-(1-epsilon)B_(0,T)}`,     (21)

`K_T(epsilon)=int_(I_T)`

` [R_T-C_T^[epsilon]]^2/B_(0,T)dmu`.             (22)

新的 sufficient target是

`sum_T K_T(epsilon)<infinity`                    (23)

再加低高度与 approximation ledger。用
`dmu asymp dt/T^2`、`B_(0,T)asymp log T`，Lebesgue形式为

`K_T(epsilon)asymp`

` 1/(T^2log T) int_(I_T)`

` [R_T-C_T^[epsilon]]^2dt`.                      (24)

式 (23)既不要求 `ess sup |C_T|/B_0`，也不要求
`int C_T^4/B_0^3`。它仍不是 RH 的证明：必须从 primes/Gamma独立证明 clipped
residual可和。与 full Selberg profile相比，它只读取 predictor无法解释的负
barrier方向；与任意定义 `H_-` 的循环方案相比，clipping threshold完全由已知
`B_0` 与 explicit `C_T` 决定。

## 7. 有限验证接口

在 finite matrices中：

1. 对 `U=B_0^(-1/2)CB_0^(-1/2)` 作 Hermitian eigendecomposition；
2. 把 eigenvalues截到 `-(1-epsilon)` 以上；
3. 重建 `C^[epsilon]` 与 `B^[epsilon]`；
4. 直接计算式 (6)、(15)与 `tau(H_-)`。

新增回归同时覆盖 noncommuting complex Hermitian matrices、Loewner lower
bound、operator barrier、clipped residual bound、scalar quartic capacity及文档
171 的 amplitude反例。它们验证有限代数恒等式，不是 zeta 渐近证书。

## 8. 下一步

下一步应在单个 square-root Type II rectangle上比较三个量：

1. linear Schur residual；
2. quartic-capacity必要条件 `T D_T^2/log T`；
3. lattice-clipped residual `K_T(epsilon)`。

若 `K_T` 能利用 boundary-shell signs而可和，定理 AEG绕开 amplitude与fourth
moment两个障碍。若 `K_T` 仍与 full profile同阶，则应对 clipping bad set
`{C_T<-(1-epsilon)B_0}` 作 layer-cake/large-values估计；此时需要的只是一侧
sublevel capacity，而不是完整 fourth moment或双侧 supremum。

本笔记没有证明 RH。它证明的是：在足够广的 tracial correspondence algebra中，
standard relative functional calculus本身就能产生严格正的 Hodge background；
剩余存在性输入可以精确写成 one-sided quadratic arithmetic approximation。

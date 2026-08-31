# Degree-one moment blindness 与 short-word point-effect leverage

文档 185 把完整 arithmetic word algebra 的 moment negative trace 与 Hodge
current 的 negative trace精确识别。下一自然尝试是从 degree one moment 开始做
Schur/SOS。本笔记证明一个 sharp no-go：对 canonical diagonal multiplication
current 与 bipartite Selberg--Volterra dilation，degree-one moment 退化成有限个
scalar features；只要 physical dimension超过 feature rank，就存在 degree-one
完全不可见、但负谱迹任意大的 signed current。

因此 degree-one Schur matrix不能作为 universal bounded-index certificate。
高 degree 的正确含义是产生 nonnegative point effects
`q_a(p)=||ae_p||^2`；所需的新结构是这些 effects 对 negative level sets 的
quantitative leverage/capture，而不是单纯增加非交换 words 的数量。

## 1. Diagonal current on a bipartite dilation

令

`H=C^P direct-sum C^R`,                           (1)

其中 `P` 是 physical terminal products，`R` 是 channel/prefix side。令
`V:C^P->C^R` 是任意 incidence matrix，并定义 self-adjoint transport

`T=[[0,V^*],[V,0]]`.                              (2)

令 current 只在 physical sector 上作用：

`X=diag((x_p)_(p in P),0_R)`, `x_p in R`.        (3)

取 commuting real diagonal labels `D_1,...,D_s`，并令 `f_a(p)` 是 `D_a`
在 physical vertex `p` 上的 label；另置 `D_0=I`,`f_0=1`。degree-one generator
list 为

`G_1={D_0,D_1,...,D_s,T}`.                       (4)

使用 normalized trace `tau=Tr/d`，`d=|P|+|R|`。

### 定理 AFX（exact degree-one bipartite collapse）[U]

degree-one moment matrix

`M_1(X)_(i,j)=tau(Xg_i^*g_j)`                    (5)

具有 block diagonal 形式

`M_1(X)=d^(-1)[[H_f,0],[0,e_V]]`,                (6)

其中

`(H_f)_(a,b)=sum_(p in P)x_pf_a(p)f_b(p)`,       (7)

`e_V=sum_(p in P)x_pkappa(p)`,                   (8)

`kappa(p)=(V^*V)_(p,p)=sum_r|V_(r,p)|^2`.        (9)

所以 degree one 只读取 feature family

`F_1=span{f_af_b:0<=a,b<=s} + span{kappa}`.      (10)

#### 证明

`D_aD_b` 仍是 diagonal，取 trace直接给式 (7)。`D_aT` 与 `TD_a` 都是
bipartite off-diagonal operators；左乘 diagonal `X` 后 trace为零。最后

`T^2=diag(V^*V,VV^*)`,                            (11)

而 `X` 在 `R` sector为零，故 `tau(XT^2)=e_V/d`。`square`

对 cumulative Volterra matrix `V=C_H=(1_(j<=k))`，

`kappa(p_j)=H-j+1`.                              (12)

因此一个 height label `ell_j` 时，整个 degree-one moment至多读取
`1,ell,ell^2,H-j+1` 四个 physical features。

## 2. Finite-feature nullspace no-go

### 定理 AFY（arbitrarily large invisible negative trace）[U]

若 `dim F_1<|P|`，则存在非零 real vector `z=(z_p)`，使相应
`X_z=diag(z,0)` 满足

`M_1(X_z)=0`,                                    (13)

但

`tau((X_z)_-)>0`.                                (14)

而且把 `z` 替换为 `Az` 可令负谱迹任意大，同时 degree-one moment仍为零。

#### 证明

取 `0 ne z in F_1^perp`。因为 `1=f_0^2 in F_1`，有 `sum_pz_p=0`；非零
real `z` 因而同时有正、负坐标，给式 (14)。正交于所有 `f_af_b` 与 `kappa`
后，定理 AFX 给式 (13)。最后作正数 scaling。`square`

这个反例不依赖 labels 的数值病态，也不依赖 Volterra condition number；它是纯
dimension obstruction。故 degree-one moment 的任何 universal Schur bound 都
不可能控制完整 negative index。

## 3. Exact point-effect formula at arbitrary degree

令 `W_L` 是 degree至多 `L` 的 word space。对任意 `a in W_L`，定义 physical
point effect

`q_a(p)=||ae_p||^2>=0`.                           (15)

### 定理 AFZ（short-word response = point-effect pairing）[U]

精确地

`tau(Xa^*a)=d^(-1)sum_(p in P)x_pq_a(p)`.        (16)

若 `||a||<=1`，则 `0<=q_a(p)<=1`。因此 degree-`L` word squares所能检测的
恰是 effect family

`E_L={q_a:a in W_L, ||a||<=1}` subset [0,1]^P.  (17)

#### 证明

在 physical basis 展开 trace：

`Tr(Xa^*a)=sum_px_p(a^*a)_(p,p)`

`           =sum_px_p||ae_p||^2`.                (18)

contraction bound给 `q_a(p)<=||a||^2<=1`。`square`

这把 word-moment route 与文档 179--181 的 one-sided packet/capture route精确
统一起来：short words只是产生一族特殊 nonnegative packets/effects。能否控制
negative trace取决于它们是否覆盖负 level-set indicators。

## 4. Quantitative effect-coverage criterion

对给定 diagonal current `x`，令 `theta_x(p)=1_(x_p<0)`。若存在
`q in conv(E_L)` 满足

`||q-theta_x||_infinity<=epsilon`,               (19)

则

`tau(X_- )`

` <=sup_(a in W_L,||a||<=1)[-tau(Xa^*a)]`

`   +epsilon tau(|X|)`.                          (20)

#### 证明

`tau(X_-)=-d^(-1)sum_px_ptheta_x(p)`。以 `q` 替换 `theta_x` 的误差至多
`epsilon d^(-1)sum_p|x_p|`。由于 `q` 是 `E_L` 的 convex combination，其
负响应不超过 `E_L` 上的最大负响应。`square`

式 (20) 是一个诚实的 short-word Hodge criterion，但若 approximation `q`
根据 `theta_x` 事后选择且没有 uniform rate，它仍是负谱投影的重述。有效输入必须
由 arithmetic geometry证明 `epsilon_L` 的共尾速率，或只对实际 zeta currents
证明 response-weighted coverage。

## 5. Exact finite interpolation and its limitation

若一个 diagonal label `L` 在完整 finite vertex set上有 distinct values
`ell_1,...,ell_d`，则 Lagrange polynomial

`p_v(t)=product_(u ne v)(t-ell_u)/(ell_v-ell_u)` (21)

满足

`p_v(L)=e_ve_v^*`.                               (22)

所以 degree `d-1` 已精确产生所有 point projections；对任意 subset `S`，
`sum_(v in S)p_v(L)` 是其 indicator projection。对 diagonal current，完全不需要
transport generator 就能在 finite dimension恢复全部 negative trace。

这既是 constructive existence result，也是 no-free-lunch：选择
`S={v:x_v<0}` 直接读取了未知负 level set；degree随 `d` 增长，而 coefficients
含 inverse spectral gaps。它没有给 cofinal uniform bound，也没有用 Euler/Gamma
data证明负质量小。

## 6. 对研究路线的修正

NCE-7 的 full-generation 与 finite-word witness已经解决，但它们主要回答
“负方向能否被算术 words看见”，而经典 zeta 的交换 realization早已能看见所有
point effects。真正问题是“不读取负谱位置，如何证明其规范迹质量一致有界”。

因此下一轮不应盲目推进 degree-two、degree-three moment矩阵。优先级应改为：

1. **Arithmetic-specific coverage**：证明实际 zeta current 的 negative level
   sets可由低 degree Volterra/threshold effects以 response norm逼近；
2. **Walk pairing/SOS**：直接把一整族 moment entries写成 Hodge squares加可和
   boundary defect，而不是逐 degree扩张；
3. **Layer-cake capacity**：允许 pointwise负井很深，只控制被 short-word effects
   看见的 Cauchy capacity；
4. **停止条件**：若所需 coverage rate等价于文档 169 的 Selberg profile/RH，
   就停止把它当作独立输入。

## 7. 审计结论

degree-one arithmetic moment route存在无条件、任意尺度的 nullspace obstruction。
高 degree 的本质不是非交换代数形式，而是 point-effect localization。这个结论
把非构造 order-density、constructive packet Hodge 与 layer-cake capacity 三条
路线汇合到同一个可证伪量：short-word effect family 对实际 negative level sets
的 quantitative capture error。


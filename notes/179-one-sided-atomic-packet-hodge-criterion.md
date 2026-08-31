# One-sided atomic packet Hodge criterion

文档 178证明 universal Fejér Bessel constant在 square-root wedge必有
`Theta(1+Nh)` 放大。该 no-go针对 full arbitrary-coefficient energy；文档 173
的 clipped Hodge criterion实际只读取 polar cone中的负方向。本笔记把这一差别
严格化：若 finite polar cone由 packet rays生成，并且这些 rays在非负组合上有
coercivity，则到正算术锥的距离只需各 packet的 **negative quadratic response**，
而不需 full two-sided packet energy。

该定理同时适用于：

- finite evaluation normals；
- finite correspondence Gram的 rank-one PSD witnesses；
- random-grid产生的不交 cell packets；
- matrix-valued、带 local phases 的 Gamma--Euler currents。

它不把 complex packet误写成普通 prime short sum：在 Hermitian
correspondence模型中，原子响应是实数 `u^*Xu`。

## 1. Atomic polar cone

令 `H` 是有限维实 Hilbert space，`K subset H` 是 nonempty closed convex cone。
先消去文档 175 的 arithmetic annihilator，即在其正交 quotient中工作。假设

`K^o=cone{-p_1,...,-p_M}`,                      (1)

其中 `p_i ne0` 是允许的 packet atoms。定义 synthesis

`P a=sum_(i=1)^M a_i p_i`, `a in R_+^M`.        (2)

假设存在 `gamma>0` 使

`||Pa||^2>=gamma||a||_2^2`

对全部 `a>=0` 成立。                              (3)

式 (3)只要求 positive-orthant coercivity，比 `P` 在全部系数空间有 lower frame
bound更弱。

对 `x in H` 定义 one-sided responses

`b_i(x)=(-<x,p_i>)_+=<x,p_i>_-`.                (4)

### 定理 AEX（one-sided atomic polar bound）[U]

有双边界

`max_i b_i(x)^2/||p_i||^2`

` <=dist(x,K)^2`

` <=gamma^(-1)sum_i b_i(x)^2`.                 (5)

#### 证明

由 Moreau decomposition，

`dist(x,K)^2`

` =sup_(y in K^o){2<x,y>-||y||^2}`.             (6)

对单个 ray取 `y=-t p_i`、`t>=0`。一元二次函数

`-2t<x,p_i>-t^2||p_i||^2`                      (7)

的上确界为 `b_i(x)^2/||p_i||^2`，给左界。

一般 `y=-Pa`。由 `a_i>=0`，

`-<x,Pa><=sum_i a_i b_i(x)`.                    (8)

再用式 (3)，式 (6)中的目标至多

`2<a,b>-gamma||a||^2`

` <=gamma^(-1)||b||^2`,                         (9)

其中最后一步为完成平方。对 `a>=0` 取 supremum即得右界。`□`

定理 AEX说明 full packet response `|<x,p_i>|^2` 是不必要的；正响应不会进入
上界。真正需要的是 polar atoms的负响应及其 nonnegative synthesis coercivity。

## 2. Annihilator 与 approximation ledger

若原 Hilbert space分解为

`H=L direct_sum L^perp`,                        (10)

其中 `L=A^perp` 是 arithmetic annihilator、`K subset L^perp`，且

`K^o=L direct_sum cone{-p_i}`, `p_i in L^perp`, (11)

则

`dist(x,K)^2=||P_Lx||^2`

`              +dist(P_(L^perp)x,K)^2`.         (12)

所以定理 AEX只需应用于 quotient component；annihilator residual另列入文档
173 的 approximation ledger，不能通过增加 atoms静默吸收。

## 3. Orthogonal cell packets

若 `p_1,...,p_M` orthonormal，则 `gamma=1`，而且式 (5)的右界取等：

### 推论 AEY（exact orthogonal one-sided certificate）[U]

若

`K^o=cone{-p_1,...,-p_M}`, ` <p_i,p_j>=delta_ij`, (13)

则

`dist(x,K)^2=sum_i <x,p_i>_-^2`.                (14)

#### 证明

polar projection逐坐标为

`proj_(K^o)x=-sum_i<x,p_i>_-p_i`.               (15)

取 norm平方即得。`□`

对固定 random-grid realization，令 `p_I` 是每个不交 cell上归一化的 constant
packet。它们在 coefficient `ell^2` 中正交。因此如果 finite polar extreme rays
确被这些 cells捕获，clipped residual不是 full Fejér energy，而是式 (14)的
one-sided cell energy。

## 4. Rank-one correspondence packets

令 `H=Herm_N`，内积为 Hilbert--Schmidt pairing

`<X,Y>=Tr(XY)`.                                  (16)

对 unit vector `u`，令 packet atom

`p_u=u u^*`.                                    (17)

则

`||p_u||_HS=1`,                                 (18)

`<X,p_u>=u^*Xu in R`.                           (19)

所以定理 AEX的 atomic input精确是

`(u^*Xu)_-^2`.                                  (20)

这保持了 correspondence phases与全部 cross terms。只有当 `X` 本身为
diagonal evaluation current时，式 (20)才退化成普通 one-sided cell average；
一般情况下不能用 `psi(x+h)-psi(x)-h` 的符号替代。

若 `u_i` 两两正交，则 `p_(u_i)` 在 Hilbert--Schmidt空间也正交，因为

`Tr(p_(u_i)p_(u_j))=|<u_i,u_j>|^2`.             (21)

因此 disjoint normalized cell vectors给推论 AEY的 exact matrix certificate。

## 5. Packet center-line criterion

考虑文档 174 的 blocks `T`。在消去已知 annihilator ledger后，假设每块的
finite arithmetic polar cone由 packets `p_(T,i)`生成，并满足式 (3)，常数为
`gamma_T`。令 `X_T` 为 joint prime--continuum--Gamma Hermitian current。

### 定理 AEZ（one-sided packet Hodge--Weil criterion）[C]

若

`sum_T gamma_T^(-1)`

` *sum_i <X_T,p_(T,i)>_-^2<infinity`,           (22)

且 annihilator、finite-to-full correspondence approximation与低高度 ledger均
可和，则目标 divisor的全部非零 zeros位于中心线。

#### 证明

逐 block应用定理 AEX，得到 positive arithmetic cone的 squared distance总和
有限。由文档 174 的 AEI--AEJ，这给文档 173 的 clipped residual budget；
再应用 AEG。`□`

式 (22)是新的广义结构接口。它比 full Selberg/Fejér energy严格单侧，但仍有
两个必须独立证明的算术输入：

1. polar cone确由所列 packets加可控 remainder捕获；
2. `gamma_T` 不因 packet overlap或冗余而崩溃。

## 6. 与 occupancy 障碍的关系

文档 178的 `Theta(1+Nh)` 是 synthesis的 **upper frame** 放大；定理 AEX使用的
是 polar atoms在 nonnegative coefficient cone上的 **lower coercivity**。二者
不是同一个量。

- densest-cell packet给一个大的 full-energy方向；
- one-sided criterion只在该 packet对 `X_T` 给负 quadratic response时付费；
- disjoint cells归一化后 `gamma=1`，不会再支付 occupancy；
- 但用 disjoint cells替代完整 rank-one polar cone可能留下 remainder，该
  remainder正是下一次 finite SDP需要审计的量。

因此 occupancy no-go没有否定 one-sided路线；它迫使所有可能收益来自
`(u^*X_Tu)_-` 的算术符号，而不是 universal norm inequality。

## 7. 下一步：有限 SDP 的 packet capture ratio

在单个 Type II rectangle上，令 `C_full` 是文档 175 的完整 rank-one polar cone，
`C_cell` 是由若干 shifted-grid cell projections生成的子锥。定义 capture ratio

`eta_R=sup_(Y in C_full, ||Y||=1)`

`       dist(Y,C_cell)`.                         (23)

下一步应数值并解析研究：

1. `eta_R` 是否随加入少量 shifts/ranks趋零；
2. cell atoms的 nonnegative coercivity `gamma_R`；
3. 未捕获 remainder对 AEJ dual objective的最坏贡献；
4. actual joint current上的 negative responses式 (20)。

若 `eta_R` 一致趋零且式 (22)可和，就得到一条真正弱于 full variance的
中心线路线。若 `eta_R` 在 rectangle增大时保持接近一，则 cell packets不能捕获
polar cone，应转向 threshold boundary或 nonlocal correspondences。

## 8. 审计结论

本笔记无条件证明 one-sided atomic polar bound及 orthogonal/rank-one版本，并
给出条件性的 packet Hodge--Weil theorem。它没有证明式 (22)对 zeta成立，也
没有把 Hermitian quadratic packet偷换成 scalar prime discrepancy。

当前最小可执行任务已经变成 finite SDP geometry：计算 cell packet cone对完整
rank-one correspondence polar cone的 capture ratio与 coercivity。

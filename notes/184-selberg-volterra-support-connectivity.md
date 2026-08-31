# Selberg--Volterra 支撑连通性、channel quotient 与 conditioning no-go

文档 183 把全局 arithmetic order-density 缩为 cross-fiber transport 的支撑
连通性。本笔记对文档 168 的离散 Selberg--Volterra transport 完成这个审计。
结论分成一正一反两部分：

1. canonical cumulative-prefix incidence 的二部图无条件连通；加入多个
   Vaughan/threshold channels 后，连通分量完全由 physical prefix hypergraph
   决定；
2. cumulative matrix 的 condition number 按 prefix length 线性增长，所以
   algebraic full-generation 不提供 uniform energy bound。解析难点没有被
   bicommutant theorem 消除。

这解决了 NCE-7 的 finite support-generation 子问题，同时保留了与 RH 等价的
Selberg-profile 障碍。

## 1. 三层有限 transport graph

令 `C` 是 channel vertices，`P` 是 distinct terminal physical products，`R`
是 prefix rows。每个 `c in C` 有唯一 terminal map

`pi:C->P`,                                        (1)

而每个 prefix row `r` 有非空 support `I_r subset P`。定义三部无向图

`c -- pi(c)`, `p -- r iff p in I_r`.              (2)

零系数 channels、empty prefix rows 与真正 isolated physical columns 在构图前
删除。多个 channels 映到同一 product 时，它们共享一个 physical vertex；这正是
文档 162 的 canonical physical quotient，而不是把 PSD component Gram 当成
有符号 current。

在 `P` 上定义等价关系：若 `p,p'` 同属某个 `I_r`，则令 `p~p'`，再取传递闭包。

### 定理 AFP（exact transport component theorem）[U]

去除零行、零列后，图 (2) 的 connected components 与 `P/~` 一一对应。
每个 channel vertex 属于 `pi(c)` 的 component，每个 prefix vertex属于其任一
support point 的 component。

#### 证明

一条经过 prefix vertex 的两步路径 `p-r-p'` 恰对应 `p,p' in I_r`，所以
physical vertices之间的 path relation 正是 `~`。channel vertices 都是附着在
`pi(c)` 上的叶；prefix vertex 的全部 neighbors 因定义属于同一 `~`-class。
故加入两类 vertices 不合并不同 classes，也不拆分任何 class。`square`

这个定理说明 channel multiplicity 本身既不制造 cross-fiber connectivity，也不
破坏它。真正连接不同 terminal products 的是共享 prefix rows。

## 2. Canonical cumulative 与 sliding prefixes

对 ordered physical increments `p_1,...,p_H`，canonical cumulative matrix 为

`C_H(k,j)=1_(j<=k)`.                              (3)

其第 `k` 行 support 是

`I_k={p_1,...,p_k}`.                              (4)

### 推论 AFQ（cumulative and sliding connectivity）[U]

1. `C_H` 的二部 support graph 对每个 `H>=1` 连通；
2. 若 sliding family 含每个相邻 pair `{p_j,p_(j+1)}`，则 support graph 连通；
3. 若 prefix rows 分裂在两个不相交 physical subsets 上，则恰保留至少两个
   components，不能由 channel leaves 修复。

第一点也可直接看出：最后一行 `I_H` 邻接全部 physical vertices。

## 3. Metric interval components

令 physical positions `x_1<...<x_H`，prefix family 包含所有长度至多 `h` 的
closed intervals 与 `P={x_j}` 的非空交。于是两个 points 可同属某个 prefix
当且仅当距离至多 `h`。

### 定理 AFR（gap characterization）[U]

metric prefix graph 的 components 恰由 gaps

`x_(j+1)-x_j>h`                                  (5)

切开。特别地，若最大相邻 gap 至多 `h`，图连通。

对 logarithmic integer positions `x_n=log n`, `N<=n<=2N`，

`max_n(x_(n+1)-x_n)<=log(1+1/N)<=1/N`.           (6)

故完整 consecutive physical grid 在 `h>=log(1+1/N)` 时连通。若
`h asymp 1/T`，transition 位于 `N asymp T`，与文档 178 的 local occupancy
transition一致。

若 arithmetic support 稀疏，不能用式 (6)；但 joint prime--continuum
discretization 中，只要 continuum quadrature mesh 的最大 log gap至多 `h`，它会
连接全部落在同一 range 的 arithmetic atoms。该 bridge 必须连同 continuum
weights 和 approximation error 一起保留，不能只借用其支撑后再删除 continuum
current。

## 4. Exact singular spectrum

`C_H` 可逆，其 inverse 是 first-difference matrix。令奇异值降序排列为
`s_1>=...>=s_H`。

### 定理 AFS（Volterra singular values and linear conditioning）[U]

精确地

`s_k(C_H)=1/[2sin((2k-1)pi/(4H+2))]`,            (7)

`k=1,...,H`。因此

`||C_H||=1/[2sin(pi/(4H+2))] asymp 2H/pi`,       (8)

`s_H=1/[2cos(pi/(2H+1))] -> 1/2`,               (9)

`kappa(C_H) asymp 4H/pi`.                        (10)

#### 证明

`D_H=C_H^(-1)` 是 diagonal `1`、subdiagonal `-1` 的 first-difference
matrix。`D_H^*D_H` 是带一个 endpoint modification 的 tridiagonal discrete
Laplacian。代入 sine modes 可得其特征值

`4sin^2((2k-1)pi/(4H+2))`.                       (11)

取 inverse square roots并按降序排列即得式 (7)。式 (8)--(10)直接推出。
`square`

所以 cumulative transform 是稳定可逆的下界变换，但 upper energy amplification
随 `H` 增长。支撑连通性只读取 entries 是否为零，完全看不到式 (10)。

## 5. Bicommutant consequence and no-free-lunch

在 channel--physical--prefix vertices 上加入一组不依赖 zeros 的 commuting
diagonal labels，用 vertex type、terminal product、`q`/face product、prefix
start/end 区分所有 vertices。若定理 AFP 的 quotient graph 连通，则 joint
spectrum simple；令 `T` 为图 (2) 的任意 self-adjoint nonzero weighted
adjacency。文档 183 的定理 AFM 给

`alg^*(labels,T)=End(H_finite)`.                 (12)

因此 finite Selberg--Volterra rectangles 的 algebraic density 条件在连通区间上
自动成立。

但式 (12) 不蕴含以下任何一项：

- `tau(Xa^*a)>=0` 对 arithmetic words成立；
- word length 的一致上界；
- `C_H` 的 uniform Bessel bound；
- Selberg prefix profile 的 square-root cancellation。

事实上 `C_H` 可逆，说明 prefix field 与 increments 含同样的有限维信息；而式
(10)说明把所有信息连通起来的代价可随 scale 退化。若利用 full generation 直接
测试全部 `a^*a`，所得条件精确等价于 current positivity，而不是其较弱推论。

## 6. Channel annihilator audit

若在 physical quotient 前保留多个 component channels，synthesis

`S:C^C->C^P`                                     (13)

通常有 `ker S ne 0`。有两种诚实处理：

1. 先 quotient `ker S`，在 physical space 上构造 signed current；
2. 保留 dilation，但把 `ker S` 作为显式 null/annihilator sector，并证明其它
   generators 对所用 quotient/shorting 相容。

不能仅因加了区分 channels 的 diagonal labels 后全图连通，就声称 kernel 已具有
新的 physical positivity。那些 labels 可能把 null combinations移出 kernel；此时
word-square positivity 是额外条件，而不是原 explicit formula 的自动结果。

## 7. 下一步

支撑连通性现已解决。NCE-7 的下一核心变成：在 full-generating finite algebra
中，把所有 word-square responses组织为可验证的有限矩阵，并寻找由
Volterra summation-by-parts、Möbius Hodge cancellation 与 Gamma boundary
产生的 PSD factorization。文档 185 给出这个 word-moment matrix 的精确结构。

## 8. 审计结论

Selberg--Volterra transport 确实足以提供 finite cross-fiber bicommutant
generation；这不是缺失环节。缺失环节是解析的 word-square positivity 与一致
conditioning。该结论同时推进非构造路线并排除了“连通性本身接近证明 RH”的
过度解释。


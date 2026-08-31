# Labelled incidence bicommutant 与 threshold-complex generator theorem

文档 182 把非构造路线的第一个开放输入写成 commutant condition
`A'=M'`。本笔记在 Möbius threshold complex 上无条件解决 fiberwise 部分：
一个取互异 face labels 的对角算子，加上 simplicial Dirac 的 incidence support，
已经生成每个有限 fiber 的全部 matrix algebra。

证明只用两个事实：unique factorization 使 face product labels 互异；包含 reduced
empty face 的 Hasse incidence graph 连通。它不使用 zeta zeros，也不使用任何
正性猜想。剩余的全局障碍与文档 167 完全一致：fiberwise direct sum 仍缺少
跨 `q` transport。若能构造支撑图连通的 arithmetic cross-fiber operator，再配合
能区分 `(q,S)` 的两个对角 labels，同一个交换子论证会生成整个 joint algebra。

## 1. Connected labelled graph lemma

令 `V` 是有限集合，`L=diag(ell_v)_(v in V)`，其中所有 `ell_v` 两两不同。
令 `B=B^*`，并以

`{v,w} in E iff B_(v,w) ne 0`                    (1)

定义无向 support graph `G_B=(V,E)`。

### 定理 AFM（simple label + connected support）[U]

若 `G_B` 连通，则

`{L,B}'=C I`,                                    (2)

因而 unital `*`-algebra `alg^*(L,B)` 等于
`M_|V|(C)`。

#### 证明

若 `X` 与 `L` 对易，则因 `L` 有 simple spectrum，`X=diag(x_v)`。再由
`XB=BX`，对每条 edge 得

`(x_v-x_w)B_(v,w)=0`,                            (3)

所以 `x_v=x_w`。图连通推出所有 `x_v` 相等，即式 (2)。有限维 bicommutant
theorem 或 Burnside theorem 随即给生成代数是全部 matrix algebra。`square`

这个证明不要求 `B` 的谱简单，也不要求 edge weights 为正；只要求非零支撑连通。

## 2. Möbius threshold fiber

沿文档 166，对 `q>1` 与 `U>=1`，令

`K_U(q)={S subset P(q): product_(p in S)p<=U}`.  (4)

在 total reduced chain space

`C_U(q)=directsum_(j>=-1) C_j(K_U(q);C)`         (5)

上令 `D_U(q)=partial+partial^*`。对每个 face `S` 定义 product-length

`L_U(q)e_S=log(product_(p in S)p)e_S`,           (6)

其中空积为一，故 empty face label 为零。

### 定理 AFN（threshold fiber full-generation）[U]

若 `K_U(q)` 非空，则

`alg^*(L_U(q),D_U(q))=End(C_U(q))`.              (7)

#### 证明

不同 squarefree faces 有不同 prime products，所以式 (6) 的 labels 两两互异。
`D_U(q)` 的非零 off-diagonal support 正是 oriented Hasse incidence edges；符号
不影响 support。任意 face 可反复删除 vertices 到达 empty face，而 complex 的
downward closure 保证沿途 faces 都在 `K_U(q)` 中。因此 Hasse graph 连通。
应用定理 AFM 即得式 (7)。`square`

### 推论

对任意 fiberwise self-adjoint current `X_q`，若 `Tr((X_q)_-)>0`，则存在
`L_U(q),D_U(q)` 的 finite noncommutative polynomial `a`，使

`Tr(X_qa^*a)<0`.                                 (8)

因此文档 182 的 finite-word witness 在每个 threshold fiber 上已经不需要额外
density 假设。尚未解决的是如何从 local Euler/Gamma identities证明所有这类
word-square responses 非负或具有可和缺陷。

## 3. 为什么 fiberwise generation 仍不够

令总空间是多个 fibers 的 direct sum：

`H=directsum_q C_U(q)`.                           (9)

只加入 `directsum_q L_U(q)` 与 `directsum_q D_U(q)` 时，每个 fiber projection
`Z_q` 都在共同 commutant 中。故生成代数至多是 block diagonal，不能产生文档
167 所需的 cross-fiber maps，也不能单独控制 physical norm 中的 `q ne q'`
polarization。

这给出一个严格的边界：定理 AFN 解决 internal cohomological visibility，但不解决
external harmonic synthesis。

## 4. Joint-label cross-fiber theorem

在一个有限 rectangle `Omega` 中，以 pairs `(q,S)` 标记 basis。令两个 commuting
diagonal operators 为

`Qe_(q,S)=log(q)e_(q,S)`,

`Le_(q,S)=log(product_(p in S)p)e_(q,S)`.        (10)

它们的 joint spectrum 是 simple，因为 pair `(q,product S)` 唯一确定 `(q,S)`。
令 `T=T^*` 是一个 arithmetic transport，其非零 matrix entries 定义
`Omega` 上的 support graph。

### 定理 AFO（cross-fiber connected-generation criterion）[U]

若 `T` 的 support graph 在除去目标 annihilator sectors 后连通，则

`{Q,L,T}'=C I`,                                  (11)

从而 `alg^*(Q,L,T)=End(C^Omega)`。

#### 证明

与 `Q,L` 同时对易的算子因 simple joint spectrum 必为 `(q,S)` basis 下的
diagonal operator。再与 `T` 对易，沿每条 support edge 的 diagonal values
相等；连通性使其为 scalar。最后应用有限维 bicommutant theorem。`square`

定理 AFO 允许 `T` 同时包含 internal incidence edges 与 cross-fiber edges。它把
“构造全局 cohomology”降为一个更离散的候选：构造不依赖 zeros 的 transport，
并证明其支撑图连接所有 relevant fibers。

## 5. 与 Selberg--Volterra transport 的接口

文档 168 的 exact Selberg--Volterra map把不同 terminal products嵌入共同 prefix
field，再由显式 connection transport。它确实提供 cross-fiber correspondence，
但目前是从 prefix field 到 terminal current 的分析算子，不自动给出式 (10)
basis 上的 self-adjoint connected graph operator。

下一最小构造是把有限 prefix discretization写成 bipartite incidence matrix `V_T`，
并取

`T_T=[[0,V_T^*],[V_T,0]]`.                       (12)

需要检查：

1. 去除 zero rows/columns 与 annihilator 后，`T_T` 的 support graph 是否连通；
2. `Q,L` 的 joint labels 是否在 prefix side 也能无歧义扩张；
3. `tau(Xa^*a)` 的 word recursion 是否可由 Volterra summation-by-parts 与
   Gamma boundary terms闭合。

第一项现在是纯有限图计算；若图在任意大 rectangle 上分裂成许多 components，
则非构造 full-generation 路线必须保留相应 center，而不能宣称生成全部 joint
algebra。

## 6. 审计结论

本笔记无条件证明 Möbius threshold complex 内部的 arithmetic generators 已经
full-generate。非构造结构路线因此前进了一步：

- fiber 内的 spectral negative effect 一定可由 length/incidence finite words
  检测；
- fiber 间仍需真实 transport，而不是 direct-sum supertrace；
- 一旦 transport support 连通，双交换子稠密性自动成立；
- 最难的剩余输入是 finite-word square positivity/缺陷递推，而非显式写出负谱
  projector。


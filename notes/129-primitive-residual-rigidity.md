# Primitive residual determinant 与 finite positive rigidity

文档 128 证明 fully contractible completion 的 positivity 被 ghost sector 完全抵消。
本节处理 partially paired 情形：auxiliary columns 分成 acyclic 与 unpaired primitive
两部分。结论是一个精确二分法：acyclic 部分仍完全消失；全部新 zeta/Weil 数据
集中到一个 positive primitive Schur determinant。若同时要求 finite positive
completion 严格保持原 determinant，则正性迫使 primitive 部分为零。

这给出 classical zeta 结构存在性的刚性约束：有效 completion 不能既是有限维纯正
更新、又严格 determinant-neutral。它必须重新解释一个真实已有的 Euler/gamma/
boundary factor，或使用无限维 regularization anomaly、relative trace等非平凡机制。

## 1. Acyclic 与 primitive charge sectors

令 `W>0`，把 completion columns 分成

`U=[U_a,U_p]`,                                    (1)

其中 `U_a` 与 odd sector配对，`U_p` 未配对。full even metric 为

`W_+=W+U_aU_a^*+U_pU_p^*`.                       (2)

acyclic ghost kernel 为

`G_a=I+U_a^*W^(-1)U_a`.                           (3)

定义 partially paired superdeterminant

`Sdet_(a,p)=det(W_+)/det(G_a)`.                   (4)

再置

`W_a=W+U_aU_a^*`,                                 (5)

`G_(p|a)=I+U_p^*W_a^(-1)U_p`.                     (6)

### 定理 XI（primitive Schur residual factorization）

有

`Sdet_(a,p)=det W det G_(p|a).`                   (7)

并且 `G_(p|a)` 也是 full charge Gram 对 `G_a` 的 Schur complement：

`G_(p|a)=I+U_p^*W^(-1)U_p`

` -U_p^*W^(-1)U_a G_a^(-1)U_a^*W^(-1)U_p`.      (8)

#### 证明

先对 `U_a` 用 determinant lemma，

`det W_a=det W det G_a`.                          (9)

再对 `W_a+U_pU_p^*` 用一次，

`det W_+=det W_a det(I+U_p^*W_a^(-1)U_p)`.       (10)

除以 `det G_a` 得式 (7)。对 `W_a^(-1)` 应用 Woodbury identity并代入式 (6)，
得到式 (8)。`□`

所以 acyclic pairing 之后没有隐藏 remainder；唯一 remainder就是 primitive charge
kernel。

## 2. Finite positive determinant rigidity

### 定理 XJ（no nontrivial positive neutral primitive sector）

有

`G_(p|a)>=I`,                                     (11)

`det G_(p|a)>=1`.                                 (12)

而且以下条件等价：

1. `det G_(p|a)=1`；
2. `G_(p|a)=I`；
3. `U_p=0`。

因此 finite-dimensional positive completion 若 partially paired superdeterminant仍
等于 `det W`，则 unpaired primitive completion 必为零。

#### 证明

式 (6) 中 `U_p^*W_a^(-1)U_p>=0`，给式 (11)。所有 eigenvalues 至少为 `1`，
故 determinant 至少为 `1`。若 determinant等于 `1`，所有 eigenvalues均为 `1`，
所以 positive semidefinite summand为零。因 `W_a^(-1)>0`，这等价于 `U_p=0`。
反向显然。`□`

这是严格有限维结论，不依赖数值或渐近。

## 3. 所有新 variations 定位到 primitive factor

令 `W(t)` 是 analytic metric path，并相应定义 `W_a(t),G_(p|a)(t)`。

### 定理 XK（primitive localization of Weil variations）

有 pointwise identity

`log Sdet_(a,p)(t)`

` =log det W(t)+log det G_(p|a)(t).`              (13)

所以每一阶新增 trace/Weil variation 精确等于 primitive residual factor 的对应
variation；acyclic sector 在所有阶继续完全抵消。

对 response path `W(t)=W+tDD^*`，令

`b_p=U_p^*W_a^(-1)D`.                             (14)

则 primitive response contribution 为

`d/dt log det G_(p|a)(t)|_0`

` =-b_p^*G_(p|a)^(-1)b_p<=0`.                    (15)

#### 证明

定理 XI 对每个 `t` 成立，取 logarithm并逐阶求导得到式 (13)。式 (15) 与文档
128 相同：对 inverse求导并用 trace cyclicity，或直接对式 (6) differentiation。
`□`

因此 primitive positivity不会免费出现：它同时携带一个明确的新 determinant factor
及其显式公式 contribution。

## 4. Finite positive completion dichotomy

### 定理 XL（same-zeta realization obstruction）

在 finite-dimensional positive Hodge setting 中，任意 completion有如下二分：

1. 若所有 added columns 与 odd sector exact pairing，则 zeta/superdeterminant及全部
   Weil variations不变，但没有新增 purity（定理 XH）；
2. 若存在 unpaired primitive columns，则留下 `det G_(p|a)>1`，全部新 variations
   来自该 factor，故 completion改变 determinant/zeta data（定理 XI--XK）。

所以不存在同时满足“非零 positive primitive gain”与“原 finite determinant严格
不变”的 completion。

#### 证明

fully paired case应用定理 XH；partially paired case应用定理 XI。若 `U_p!=0`，
定理 XJ 给 residual determinant严格大于 `1`；若要求 determinant不变，则
`U_p=0`，退回第一种情况。`□`

对 classical zeta，一个可能有效的 completion 因而必须额外证明以下之一：

- `det G_(p|a)` 正是原显式公式中尚未几何化的现有 Euler/gamma/boundary factor；
- infinite-dimensional regularized determinant产生可控 anomaly，避开有限乘法刚性；
- relative cohomology/boundary map提供未配对但已属于原 zeta 的 trace term；
- primitive sector不是简单 positive rank update，而有真实 Lefschetz/Frobenius作用。

任何方案都必须逐项匹配原 zeta，不能只宣称“determinant neutral”。

## 5. Möbius--conductor audit

取文档 127 的 strong periodic completion `sP_N`（`s=2Lambda_N`），将其 Cholesky
columns在 `R=2` 时拆成一列 acyclic、一列 primitive。结果如下：

| `N` | `det G_(p|a)` | base response capacity | full even capacity | partial-super capacity | primitive derivative |
|---:|---:|---:|---:|---:|---:|
| 8 | 6.106 | 3.506 | 0.719 | 3.460 | -0.0465 |
| 32 | 7.988 | 4.192 | 0.843 | 3.960 | -0.231 |
| 100 | 8.021 | 2.955 | 0.985 | 1.148 | -1.807 |
| 200 | 5.055 | 6.572 | 0.934 | 5.408 | -1.164 |

primitive residual determinant远离 `1`，清楚显示 stronger even purity的代价是新增
zeta factor。partial-super capacity 精确等于 base capacity 加式 (15)，而不是 full
even capacity；acyclic gain已被消去。

## 6. 计算实现

新增 `primitive_residual_superdeterminant_certificate`。它计算：

- full even、acyclic ghost及 primitive Schur kernels；
- 式 (6) 与式 (8) 两种 residual construction；
- partially paired superdeterminant与 `det W det G_(p|a)`；
- residual eigenvalues/determinant；
- response capacity的 even、acyclic ghost、primitive residual三层分解。

回归核对两种 Schur formulas、determinant factorization、全部 residual eigenvalues
至少为 `1`，以及 direct/predicted partial-super capacities在 `1e-42` 内一致。

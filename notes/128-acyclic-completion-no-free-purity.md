# Acyclic completion 的 no-free-purity theorem

文档 127 找到更可信的 conductor-pure auxiliary polarization，但 natural far
completion 强度不足。一个诱人的下一步是加入更强 cohomological completion，同时
用 contractible even/odd pairs 保持 zeta determinant 不变。本节证明这种做法本身
不能提供“免费”Hodge positivity：positive even update 的全部 determinant variations
会被 odd charge kernel 精确抵消。

因此，一个真正有效且保持原 zeta 的 completion 必须包含非平凡新上同调、边界/
迹异常、未配对 weight sector 或其它打破 exact acyclic cancellation 的结构。仅仅
添加 contractible pairs 不能证明 RH。

## 1. Positive update 与 odd charge kernel

令 `W>0` 是 even Hodge metric，`U:K->V` 是任意 finite-rank completion columns。
定义

`W_+=W+UU^*`,                                     (1)

`G_-=I+U^*W^(-1)U`.                               (2)

把 `W_+` 置于 even degree、`G_-` 置于 odd degree，定义 superdeterminant

`sdet(W,U)=det(W_+)/det(G_-)`.                    (3)

### 定理 XE（acyclic superdeterminant cancellation）

对任意 `W>0,U`，

`sdet(W,U)=det W`.                                (4)

#### 证明

matrix determinant lemma 给

`det(W+UU^*)=det W det(I+U^*W^(-1)U)`.            (5)

除以式 (2) 的 determinant 即得式 (4)。`□`

`G_-` 正是 completion charges 的 Woodbury kernel；非零 added even spectrum 与
odd spectrum成对，因此该 stabilization 在 determinant 层面 contractible。

## 2. 所有阶 log-determinant variations 均抵消

令 `W(t)` 是任意保持 positive definite 的 analytic metric path，并在每个 `t`
使用同一 columns `U`。定义

`S(t)=log det(W(t)+UU^*)`

`     -log det(I+U^*W(t)^(-1)U)`.                 (6)

### 定理 XF（all-orders Weil-variation cancellation）

有 analytic identity

`S(t)=log det W(t)`,                               (7)

所以对每个 `k>=1`，

`S^(k)(0)=[log det W(t)]^(k)|_(t=0)`.             (8)

特别地，任何由 log determinant 的一阶 trace、二阶 Weil quadratic form 或更高
susceptibility 定义的 invariant，都不会因该 acyclic completion 改善。

#### 证明

对每个 `t` 应用定理 XE，取 logarithm得到式 (7)；analytic identity 可逐阶求导，
得到式 (8)。`□`

这比只证明 zeta value 不变更强：完整显式公式/variation hierarchy逐阶不变。

## 3. Capacity 与 mixed period 的逐项补偿

令 response `D`、probe `q`，并置

`R=I+U^*W^(-1)U`,                                 (9)

`a_D=U^*W^(-1)D`, `a_q=U^*W^(-1)q`.              (10)

### 定理 XG（ghost recovery of apparent Hodge gains）

even completion 的 capacity losses 为

`C_D(W)-C_D(W_+)=a_D^*R^(-1)a_D`,                 (11)

`C_q(W)-C_q(W_+)=a_q^*R^(-1)a_q`,                 (12)

mixed period loss 为

`K(W)-K(W_+)=a_D^*R^(-1)a_q`.                     (13)

而 odd log-determinant variations分别为这些 losses 的负值；所以

`C_D^super=C_D(W_+)-d_D log det R=C_D(W)`,        (14)

`C_q^super=C_q(W)`, `K^super=K(W)`.               (15)

#### 证明

Woodbury identity

`W_+^(-1)=W^(-1)-W^(-1)UR^(-1)U^*W^(-1)`        (16)

分别在 `D,D`、`q,q`、`D,q` 两侧配对，得到式 (11)--(13)。另一方面沿 path
`W+tDD^*` 对 `log det R` 求导，得到
`-a_D^*R^(-1)a_D`；probe与 mixed polarizations同理。代入 even-minus-odd
supertrace给式 (14)--(15)。`□`

所以 even canonical representative 看似更纯，只是把同样的 obstruction搬到了
odd/ghost sector。

## 4. No-free-purity structure theorem

### 定理 XH（contractible completion cannot prove centerline）

设一个 generalized zeta package 的 zeta determinant、显式公式与 Weil form 都由
graded log superdeterminant及其 functorial variations定义。若新增 completion：

1. 是 acyclic/contractible even--odd pair；
2. added spectra 由式 (1)--(2) exact pairing；
3. test/probe paths 同时作用于 paired sectors；

则 completion 不改变 zeta、显式公式或任何阶 Weil variation，因而不能把原本非正
或未认证的 Weil form 变成足以推出中心线的 form。

#### 证明

定理 XE 保持 determinant；定理 XF 保持所有 functorial variations；定理 XG 展示
capacity/mixed-period层面的逐项抵消。因此任何只依赖这些 invariants 的中心线判据
在 completion 前后等价。`□`

要让 stronger conductor completion 有效，至少必须违反上述一个条件，例如：

- auxiliary sector 含非平凡 cohomology/primitive class，而非 contractible pair；
- relative boundary condition 产生未配对 boundary determinant或 eta/trace anomaly；
- Frobenius weights 使 even/odd sectors 不以相同 test path配对；
- 新 sector 自身满足可证明的 purity，并以非零 Lefschetz/Tate trace进入原显式公式。

这些不是技术装饰，而是避免 arbitrary positive completion“证明任何 zeta RH”的
逻辑必要条件。

## 5. Möbius--conductor finite audit

取 spatial `W_N^[0,N^2]`，并用文档 127 的 half-error amplitude
`s=2Lambda_N` 加入 `UU^*=sP_N`。下表比较 base/even/super mixed periods。

| `N` | base `K` | even `K_+` | ghost correction | reconstructed super `K` |
|---:|---:|---:|---:|---:|
| 8 | -416.43 | -16.79 | -399.64 | -416.43 |
| 32 | -370.19 | 8.74 | -378.93 | -370.19 |
| 100 | 56.50 | 19.33 | 37.17 | 56.50 |

even sector 单独看有巨大改善，甚至在 `N=32` 改变 sign；但 ghost correction
精确恢复 base period。response capacity也同样：例如 `N=8` 从 `3.506` 降到
`0.719`，super reconstruction仍为 `3.506`。所有 superdeterminant ratios 在
50-digit arithmetic 下等于 `1`。

## 6. 计算实现

新增 `acyclic_completion_superdeterminant_certificate`。它构造 even metric、odd
charge kernel、superdeterminant，并核对 response/probe capacities 与 mixed period
的 Woodbury losses、ghost log derivatives及 super reconstructions。回归要求：

- `det(W+UU^*)/[det G_- det W]=1`；
- even loss = charge-kernel quadratic form；
- even-minus-ghost response/probe/mixed quantities = base quantities。

全部 equalities 在 `1e-42` tolerance 内通过。

# 241. Divisor-scale separation no-go 与 physical-fiber-first 原则

日期：2026-09-03

分支：MOM-1 / 路线 A1u；接口：adjacent-divisor dyadic dispersion / actual centered determinant response

状态：任意远 divisor columns 的 common-multiple overlap、synthesis-only off-block
decay no-go、physical-shell/block sum commuting 与 decomposition-gauge inflation 为
[T]/[N]；separated-block energy ratios 为 [E]。A1u 作为独立远块路线停止；
MOM-1 保留，但不再通过增加 divisor-coordinate 分解推进。本笔记不更新 PDF，
不改变任何零点比例的 [C] 状态。

## 1. A1u 的判定

笔记 240 把 centered response 精确写成

\[
 Q_X=\sum_{i,j}C_{ij},\qquad
 C_{ij}=Z_i^*B_X^{\rm cent}Z_j,
\tag{1}
\]

并建议先攻击 `|i-j|>=2` 的 dyadic divisor blocks。本轮得到否定性判定：

1. divisor scale separation 不产生 numerator-support separation；
2. 仅由 Vaughan synthesis 与 positivity 不能推出 off-block decay；
3. physical response 在 finite data 中依赖 separated 与 near blocks 的反号抵消；
4. 对 blocks 分别取绝对值不是 intrinsic physical budget。

因此式 (1) 仍是有效恒等式，笔记 240-(28) 仍是有效充分条件，但没有理由优先把
`|i-j|>=2` 当作容易的 independent lemma。继续沿这条路线会违反“禁止只因框架能
重写目标就持续扩写”的止损规则。

## 2. Common-multiple overlap

沿用笔记 240 的 synthesis columns

\[
 T_{a,r}=\sum_{\substack{v>V,\ w\ge1\\rvw=a}}\Lambda(v).
\tag{2}
\]

### 定理 241-A（arbitrarily separated columns share exact rows）[T]

取任意正整数 `r,s` 与任意 prime power `p>V`。置

\[
 \ell=[r,s],\qquad a=\ell p.
\tag{3}
\]

只要 `a` 属于考虑的 numerator domain，就有

\[
 \boxed{T_{a,r}\ge\Lambda(p),\qquad
 T_{a,s}\ge\Lambda(p).}
\tag{4}
\]

特别地，`s/r` 可以任意大，两个 columns 仍在同一 row 上有共同正质量。

#### 证明

在 `T_(a,r)` 中取

\[
 v=p,qquad w=\ell/r;
\]

在 `T_(a,s)` 中取 `v=p,w=ell/s`。两组都是式 (2) 的 admissible tuples，且
其权重均为 `Lambda(p)>0`。其余 tuples 也非负，得到式 (4)。`square`

例如取 `r=1,s=2^j,p=2^k>V`，就得到任意 dyadic separation 的共同 row。
这是一条 support-level 结论，不需要素数短区间定理或 asymptotic distribution。

## 3. Synthesis-only off-block decay 不存在

令 `e_a` 是 numerator row `a` 的 coordinate vector，并定义 positive rank-one
response form

\[
 B_a=|e_a\rangle\langle e_a|.
\tag{5}
\]

### 障碍定理 241-B（no divisor-distance Schur decay）[N]

在定理 241-A 的设置下，

\[
 \boxed{
 T_r^*B_aT_s=T_{a,r}T_{a,s}\ge\Lambda(p)^2.}
\tag{6}
\]

所以不存在仅由

- `|log(r/s)|` 很大；
- 两列来自同一个 Vaughan synthesis；
- response form positive semidefinite；

推出并随 divisor separation 趋零的 universal off-block Schur factor。

#### 证明

式 (5) 读取两个 columns 的第 `a` 个 coordinates；再用式 (4)。`square`

actual `B_X^cent` 不是式 (5)，而且 centering 后一般 indefinite。因此定理 241-B
不否定 actual arithmetic decay；它证明这种 decay若存在，必须来自 exact
determinant/Gabor/window structure，不能来自 divisor block geometry本身。

## 4. Physical fibers 必须先合并 divisor blocks

把 actual centered response atoms 按任意 physical partition `q` 分组，例如：

- determinant ranges `|ad-bc|`；
- exact frequency shells `X|log(ad/bc)|`；
- fixed factor/aperture cells。

令对应 Hermitian matrices 为 `B_q`，使

\[
 B_X^{\rm cent}=\sum_qB_q.
\tag{7}
\]

沿用笔记 240 的 dyadic vectors `Z_i`；其 exact sum 为

\[
 \sum_iZ_i=\Lambda.
\tag{8}
\]

定义

\[
 C_{ij}^{(q)}=Z_i^*B_qZ_j.
\tag{9}
\]

### 定理 241-C（physical-fiber/block commuting identity）[T]

对每个 physical fiber `q`，

\[
 \boxed{
 \sum_{i,j}C_{ij}^{(q)}
 =\Lambda^*B_q\Lambda.}
\tag{10}
\]

再对 `q` 求和即恢复完整 physical response。

#### 证明

由式 (8) 与双线性，

\[
 \sum_{i,j}Z_i^*B_qZ_j
 =\left(\sum_iZ_i\right)^*B_q
   \left(\sum_jZ_j\right)
 =\Lambda^*B_q\Lambda.
\]

`square`

式 (10) 给正确的 proof order：在每个 actual determinant/frequency fiber 内，
先合并全部 divisor blocks，再使用响应相消。若先形成

\[
 \sum_{i,j}|C_{ij}^{(q)}|,
\tag{11}
\]

则丢失式 (10) 的 commuting cancellation。

## 5. Block absolute budget 的 gauge no-go

### 障碍命题 241-D（decomposition absolute inflation）[N]

固定非零 Hermitian form `B` 与一个 decomposition

\[
 \Lambda=Z_1+Z_2+\cdots+Z_J.
\tag{12}
\]

若存在 `h` 使 `h^*Bh ne0`，则保持式 (12) 不变的替换

\[
 Z_1^{(R)}=Z_1+Rh,qquad
 Z_2^{(R)}=Z_2-Rh
\tag{13}
\]

可令

\[
 \sum_{i,j}|(Z_i^{(R)})^*BZ_j^{(R)}|
\tag{14}
\]

随 `R` 至少二次增长，而 physical value `Lambda^*BLambda` 完全不变。

#### 证明

式 (13) 的总和不变。两个 diagonal entries分别为

\[
 R^2h^*Bh+O(R),
\]

故其绝对值之和为 `2R^2|h^*Bh|+O(R)`。式 (14) 至少包含这两个 terms，
因此无界。physical value只依赖式 (12) 的总和。`square`

actual dyadic `Z_i` 是 fixed，而非可任意 gauge。此命题的作用是公理审计：
blockwise absolute budget不是由 physical Weil/response structure 唯一决定的量；
若要使用它，必须单独证明 actual decomposition 的 arithmetic estimate。

## 6. Finite separated-block audit [E]

更新后的 `scripts/mobius_divisor_pullback_audit.py` 在每个尺度把 Note 240 的
dyadic matrix 分成 `|i-j|<=1` 与 `|i-j|>=2`。结果为：

| `X` | total response/`L^4` | separated signed/`L^4` | separated `l1`/`L^4` | separated `l2^2`/`L^6` | separated share of block `l2^2` |
|---:|---:|---:|---:|---:|---:|
| 400 | `+5.44e-8` | `+9.08e-8` | `1.06e-7` | `8.01e-14` | `0.438` |
| 800 | `-3.92e-8` | `+1.27e-7` | `1.81e-7` | `1.09e-13` | `0.093` |
| 1,600 | `-1.42e-8` | `+1.22e-7` | `2.03e-7` | `2.10e-13` | `0.170` |
| 3,200 | `-3.09e-9` | `+4.84e-8` | `1.14e-7` | `6.00e-14` | `0.140` |

四个尺度中 separated signed part 的绝对值都大于最终 response；后三个尺度还与
最终 response 异号。因此 total smallness依赖 near/separated cancellation。
separated block 的平方能量占比为 `9%--44%`，没有单调趋零证据。

这些数据不证明 asymptotic lower bound，也不反驳式 `sum_far|C_ij|^2=o(L^6)`；
它们只否定“远块显然次要”的路线选择，并与定理 241-A--B 的 support obstruction
一致。

## 7. A1u 止损与周期决策

本轮对 A1u 作如下判定：

- **停止**：把 dyadic divisor distance 当作 independent orthogonality source；
- **保留**：式 (24) 的 truncated Möbius identities可作为 actual Type-I/II proof
  内部坐标；
- **禁止**：对 block entries取绝对值后再求和，或以 full operator norm控制；
- **physical-first rule**：任何后续 estimate 都必须在 fixed determinant/frequency
  fiber 内先保留 `sum_(i,j)C_ij^(q)`。

这意味着 MOM-1 已完成一个 234--241 的研究周期：exact band与 mass ledger已闭合，
cumulative、band-energy、channelwise mass cancellation、raw Möbius pullback及
divisor separation五种候选证书均已分别得到 theorem或 no-go。尚未闭合的仍是
actual signed high-product determinant response；继续发明同义 kernel不再算推进。

下一周期把主要精力切换到路线 B / NCE-8 的 fixed square-root Vaughan--Brownian
physical Gram。其最小问题保持为：在一个固定 rectangle 上，直接估计 all-ones
Type-I/Type-II/continuum response或其合法 Schur shorting，并证明一个不来自
diagonal Bessel norms 的 uniform improvement。MOM-1 只在出现新的 external
determinant-correlation input时恢复。

## 8. 最小公理、删除审计与循环性

本轮 [T]/[N] 只使用：

1. positive divisor synthesis entries (2)；
2. least common multiples；
3. finite Hermitian bilinearity；
4. exact synthesis identity `sum_iZ_i=Lambda`；
5. rank-one test forms与 decomposition-preserving gauge。

删除审计：

- 删除 common-multiple closure，241-A 的 shared row不再成立；
- 限制 actual `B_X^cent` 后，241-B 只留下必要性审计，不能直接判断 actual decay；
- 在 physical fiber 内先求 block sum，241-D 的 gauge inflation消失；
- finite table删除后，strict no-go仍成立，但没有 actual route-selection evidence。

非同义反复审计：241-A--B 给显式 shared-row countermodel；241-C 规定可验证的
求和顺序；241-D 给二次增长反例。它们不是 RH 或 response smallness 的改写。

循环性审计：没有使用 RH/GRH、Mertens 点态假设、Hardy--Littlewood、Weil
positivity、谱酉性或 bounded negative index。actual high-product response仍明确
开放，且本轮不把停止一个坐标路线表述为解决该算术问题。

## 9. 模型范围与 Weil 接口

- **Riemann zeta**：common-multiple overlap直接适用于 Vaughan synthesis；finite
  data使用 actual von Mangoldt weights与 exact Gabor response。
- **Dirichlet/Dedekind/automorphic L**：若 coefficient synthesis entries不再非负，
  241-A 的 lower bound须修改；241-C--D 的线性代数仍保留。
- **函数域**：lcm由 polynomial lcm替代；shared-row obstruction保留，但 degree
  lattice对 actual response另有 alias问题。
- **一般谱模型**：241-B 适用于任何具有重叠 synthesis columns 的 class；没有
  divisor synthesis 时不适用。
- **上同调型 Weil 结构**：本轮仍只审计显式公式侧；没有建立到 Frobenius/Hodge
  polarization 的桥梁。

本轮结论不是“远 blocks 无法估计”，而是更精确的：远 divisor labels 本身不提供
估计理由，且 actual finite response显示它们与近 blocks发生主阶相消。因此 A1u
停止，下一周期转向直接 physical Gram，而非继续扩大 Möbius coordinate system。

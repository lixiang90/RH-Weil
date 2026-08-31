# Alternating endpoint coefficients 与 external-period defect

文档 120 把 exact endpoint norm 写成 `2^R` 个 sign periods；文档 123 说明 fixed
node interpolation norms 不会自动控制这些 periods。本节识别 actual Möbius--Farey
canonical polynomials 中一个更集中的现象：endpoint Taylor coefficients 经常严格
交错。交错时整个 weighted `ell^1` norm 精确等于一个外点导数 `|F'(2)|`，即只需
一个固定 positive probe；一般情形也有“单外点 period + exact sign defect”分解。

这不是普遍正性定理。有限样本已给不交错反例，且抽象 positive Gram 不能强迫
交错。本节因此提供的是一个可分叉的结构：主相位可由单一 arithmetic period
估计，剩余只需控制明确的 minority-sign mass。

## 1. Endpoint polynomial 与外点导数

令 canonical correction polynomial 为

`F(u)=(1-u)H(u)`, `H(u)=sum_(p=1)^R v_pu^p`.      (1)

置 endpoint coordinate `x=1-u`，写

`Q(x)=F(1-x)=sum_(k=0)^R a_kx^(k+1)`.            (2)

elementary Riesz leverage 为

`L_1=sum_(k=0)^R(k+1)|a_k|`.                     (3)

定义 alternating external phase

`A_ext=sum_(k=0)^R(k+1)(-1)^ka_k=Q'(-1)`

`     =-F'(2)=H(2)+H'(2)`.                        (4)

对 direction `u^p(1-u)`，相应 probe coordinate 为

`q_ext(p)=(p+2)2^(p-1)>0`.                        (5)

因此 `A_ext=q_ext^*v` 是一个 fixed positive-coordinate phase，而不需要随
canonical coefficients 选择 signs。

## 2. Exact alternating-defect identity

令 `b_k=(k+1)(-1)^ka_k`。取 `s=sign(sum_kb_k)`（为零时任取），并定义

`M=sum_(sb_k>=0)|b_k|`,

`B=sum_(sb_k<0)|b_k|`.                            (6)

这里 `B` 是相对于最佳 global alternating orientation 的 mismatch mass。

### 定理 WP（external phase plus sign defect）

有 exact identities

`L_1=M+B`, `|A_ext|=M-B`,                         (7)

`Delta_alt:=L_1-|A_ext|=2B`                      (8)

（等价地，对任意预选 orientation，右侧是两类 mass 中较小者的两倍）。所以

`L_1=|F'(2)|+Delta_alt`.                          (9)

特别地，`Delta_alt=0` 当且仅当非零 endpoint coefficients 的 signs 严格交错。

#### 证明

乘以 global sign `s` 后，matched terms 正、mismatched terms 负，故 signed sum
为 `M-B`。`s` 按总和选择保证 `M>=B`；absolute sum 为 `M+B`。相减得到式
(8)，再使用式 (4) 得式 (9)。`□`

式 (9) 是 exact decomposition，不是 triangle bound。它把 finite sign cube 的
复杂性全部压进一个 nonnegative scalar defect。

## 3. Absolute monotonicity 与实根充分条件

Taylor expansion 给

`H(1-x)=sum_(k=0)^R(-1)^kH^(k)(1)x^k/k!`,        (10)

故

`a_k=(-1)^kH^(k)(1)/k!`.                         (11)

### 定理 WQ（endpoint absolute-monotonicity criterion）

若所有非零 `H^(k)(1)`, `0<=k<=R` 具有同一 sign，则 `Delta_alt=0`，从而

`L_1=|H(2)+H'(2)|=|F'(2)|.                       (12)

一个充分但非必要的条件是：`H` 的全部 roots 均为 real 且不大于 `1`。

#### 证明

第一项由式 (11)直接得到 alternating signs，再应用定理 WP。若
`H(u)=c product_i(u-r_i)` 且 `r_i<=1`，则

`H(1+t)=c product_i(t+1-r_i)`                     (13)

的全部非零 coefficients 与 `c` 同 sign；这些 coefficients 正是
`H^(k)(1)/k!`，故满足第一项。`□`

实根条件不必要：positive Taylor coefficients 的 polynomial 仍可有 complex roots。
实际样本也确实出现这种情形。

## 4. Single-external-period centerline criterion

沿用 fixed determinant setup，并令 `Delta_(alt,N)` 由式 (8) 定义。

### 定理 WR（external-period Weil criterion）

若

`c_1+|target|[|F_N'(2)|+Delta_(alt,N)]`

` =o(sqrt(log N)/loglog(3N)),`                    (14)

则 fixed principal determinant strata 为 `o(1)`；连同完整 polarized Weil
package 与总尾条件即推出相应 zeta zeros 位于中心线。

其中主项是单个 dual-cycle/Mertens period：

`-F_N'(2)=q_ext^*W_N^(-1)D_N/C_N`.               (15)

若能另外证明 eventual endpoint absolute monotonicity，则 defect identically zero，
criterion 只剩一个 fixed positive probe。

#### 证明

定理 WP 表明方括号精确等于文档 120 的 `L_1(N)`，故应用定理 WE。式 (15) 来自
式 (4)--(5) 与 canonical representative 定义。`□`

虽然式 (14) 本身等价重写 exact leverage，但它提供了一个非平凡研究分解：主项
不再需要 uniform sign cube，defect 只检测 endpoint derivative signs 的失配。

## 5. Positive Gram 不强迫交错

### 定理 WS（alternation is extra arithmetic structure）

即使 `R=2`、capacity 固定为 `1`，positive definite Gram 也不能保证
`Delta_alt=0`。

#### 证明

取

`H(u)=u-(3/5)u^2`, `v=(1,-3/5)^T`.               (16)

则

`H(1)=2/5>0`, `H'(1)=-1/5<0`, `H''(1)=-6/5<0`,  (17)

所以式 (11) 不交错且 `Delta_alt>0`。令

`D=v/(v^*v)`, `W=I/(v^*v)`.                      (18)

则 `W>0`、`W^(-1)D=v` 且

`D^*W^(-1)D=D^*v=1`.                             (19)

因此 fixed capacity 与 Hodge positivity 均成立而 alternation 失败。`□`

所以 WQ 必须从 actual Möbius--Farey incidence/collective geometry 中证明，不能
加入广义结构定理作为“自动公理推论”。

## 6. Finite audit

下表使用 `W_N^[0,N^2]`。`external/exact=|F'(2)|/L_1`。

| `N` | `R=2` | `R=3` | `R=4` | `R=5` |
|---:|---:|---:|---:|---:|
| 8 | 1.000 | 1.000 | 1.000 | 1.000 |
| 16 | 1.000 | 0.9795 | 1.000 | 1.000 |
| 32 | 1.000 | 0.6209 | 1.000 | 1.000 |
| 64 | 1.000 | 1.000 | 1.000 | 1.000 |
| 100 | 1.000 | 1.000 | 1.000 | 1.000 |
| 200 | 1.000 | 1.000 | 1.000 | 1.000 |

这组稀疏网格中 22/24 样本严格交错。它不是 universal pattern：`N=16,32,R=3`
已是反例。实根性更早失败，例如 `N=8,R=4` 的 `H` 有 roots
`0.677684 +/- 0.088213i`，但 coefficients 仍严格交错；因此 WQ 的
absolute-monotonicity formulation 比 real-rootedness 更准确。

数据提示 `Delta_alt` 可能比 full leverage 更易控制，但尚无渐近证据；不能由
22/24 的 finite frequency 推断 eventual alternation。

## 7. 计算实现

新增 `endpoint_alternating_external_phase_certificate`。它返回 endpoint coefficients、
fixed alternating probe、direct external period、matched/mismatched masses、exact
sign defect、external derivative及是否严格交错。回归核对

`L_1=|F'(2)|+Delta_alt`,

`Delta_alt=2 min(matched mass,mismatched mass)`,   (20)

以及 `q_ext(p)=(p+2)2^(p-1)` 的逐坐标公式，tolerance 为 `1e-43`。

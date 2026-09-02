# 219. Critical logarithmic-square local energy 的 scalar-budget no-go

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / critical alternating local boxes

状态：critical-shell finite local energy 为 [E]；具有正确一阶质量、二阶矩、
pointwise bound 与逐短移位上界但保留主尺度 local proxy 的稀疏模型为 [N]；
factorization-restricted critical local energy 为 [O]。本笔记不更新 PDF。

## 1. 本轮结论

笔记 218 已把完整 primitive ratio family 推进到

\[
 ab\le X(\log X)^{2-\eta}
\tag{1}
\]

（每个 fixed `eta>0`），并把下一输入缩成 critical shell

\[
 ab\asymp XL^2,
 \qquad L=\log X.
\tag{2}
\]

本轮做两项审计。

第一，实际 prime-power atoms 的 flat-window finite data 中，笔记 218-(43) 的
local-box energy 在 `X<=10^4` 仍只有约 `0.005--0.0064` 倍 `N=XL`，但
off-diagonal share 从约 `0.16` 上升到约 `0.25`。这既没有给出主尺度 lower
bound，也没有显示可认证的 little-oh rate。

第二，证明一个严格方法障碍。仅使用下列 scalar information：

1. `0<=A(n)<=L^2`；
2. `sum A(n) asymp RL`；
3. `sum A(n)^2 asymp RL^3`；
4. 对所有 `1<=h<=L^2`，`sum A(n)A(n+h) ll R L^2`；

不能推出 critical local proxy 为 `o(N)`。事实上存在非负稀疏 sequences 同时
满足这些条件，并使该 proxy 为 `asymp N`。

这比“现有估计尚未优化”更明确：即使把 Henriot--Holowinsky 上界中的
`L^epsilon(log L)^4` 损失全部删除，只保留正确 expected-size 的逐 shift 上界，
上述四项信息仍然停在主尺度。下一步必须使用至少一种此前被正 majorant 删除的
结构：

- 四变量 factorization restrictions；
- actual six-window overlap；
- 不同 arithmetic channels 的 signed cancellation；
- 或比逐 shift scalar bounds 更强的 joint short-shift law。

## 2. Critical local proxy 的尺度

在 determinant scale

\[
 R\asymp XL^2,
 \qquad
 H=\left\lfloor\frac RX\right\rfloor\asymp L^2,
\tag{3}
\]

笔记 217 的 positive collapse 把 resolution-local energy 的最粗形式写成

\[
 \mathcal Q_X(A)
 =\frac{X}{L^3R}
 \sum_{1\le h\le H}
 \sum_{n\in\mathbb Z/R\mathbb Z}A(n)A(n+h).
\tag{4}
\]

这里 `X/L^3` 是 `beta_L^4 d_G` 的尺度，`R^(-1)` 来自 cross-product
normalization。圆周版本只为消除 endpoints；把它切成固定倍 intervals 只改变
常数。

若每个 short shift correlation 具有 natural size

\[
 \sum_nA(n)A(n+h)\asymp RL^2,
\tag{5}
\]

则

\[
 \mathcal Q_X(A)
 \asymp
 \frac{X}{L^3R}\,L^2\,RL^2
 =XL=N.
\tag{6}
\]

所以 critical exponent `2` 不是笔记 217 参数选择的偶然产物；它正是
resolution width `H=L^2` 与 degree-two coefficient density 抵消全部 normalization
saving 的位置。

## 3. Sparse correlation model

### 障碍定理 219-A（mass-and-shift budgets do not imply critical saving）[N]

令 `L` 趋于无穷，取 integers `X,R` 满足

\[
 X\asymp e^L,
 \qquad
 R\asymp XL^2,
\tag{7}
\]

并置 `H=floor(L^2)`。则存在 nonnegative sequences

\[
 A_L:\mathbb Z/R\mathbb Z\longrightarrow[0,L^2]
\tag{8}
\]

使

\[
 \sum_nA_L(n)\asymp RL,
\tag{9}
\]

\[
 \sum_nA_L(n)^2\asymp RL^3,
\tag{10}
\]

并且一致于 `1<=h<=H`，

\[
 \sum_nA_L(n)A_L(n+h)\asymp RL^2.
\tag{11}
\]

特别地，

\[
 \boxed{\mathcal Q_X(A_L)\asymp N.}
\tag{12}
\]

这些 sequences 还满足 pointwise Cauchy bound `correlation <= sum A_L^2`，以及
比笔记 217-C 所用 discriminant-uniform sieve bound 更强的

\[
 \sum_nA_L(n)A_L(n+h)
 \ll R L^2
 \ll_{\varepsilon}
 \tau(h)R L^{2+\varepsilon}(\log L)^4.
\tag{13}
\]

#### 证明

在 cyclic group `Z/RZ` 上取 independent Bernoulli variables

\[
 \xi_n\in\{0,1\},
 \qquad
 \mathbb P(\xi_n=1)=p=L^{-1},
\tag{14}
\]

并令

\[
 A_L(n)=L^2\xi_n.
\tag{15}
\]

记

\[
 S=\sum_n\xi_n.
\tag{16}
\]

则 `E S=R/L`、`Var S<=R/L`。Chebyshev inequality 给

\[
 S\asymp R/L
\tag{17}
\]

的概率趋于 `1`。在该事件上，式 (15) 立即给式 (9)--(10)，因为
`xi_n^2=xi_n`。

对 `1<=h<=H`，置

\[
 Y_h=\sum_n\xi_n\xi_{n+h}.
\tag{18}
\]

因 `H=o(R)`，充分大时 `2h` 不被 `R` 整除，故

\[
 \mathbb E Y_h=Rp^2=R/L^2.
\tag{19}
\]

式 (18) 的 summands 只有在对应 directed edges 共享 endpoint 时才相关；每条
edge 与至多固定数目的其他 edges 相关。因此

\[
 \operatorname{Var}(Y_h)ll Rp^2+Rp^3\ll R/L^2.
\tag{20}
\]

再用 Chebyshev，

\[
 \mathbb P\left(
 |Y_h-R/L^2|>\frac12R/L^2
 \right)
 \ll\frac{L^2}{R}.
\tag{21}
\]

对至多 `H<=L^2` 个 shifts 使用 union bound，失败概率至多

\[
 O(L^4/R)=o(1).
\tag{22}
\]

所以存在一个 realization 同时满足式 (17) 及全部

\[
 Y_h\asymp R/L^2,
 \qquad 1\le h\le H.
\tag{23}
\]

乘以 `L^4` 得式 (11)。式 (12) 由式 (4)、(11) 与 `H asymp L^2` 得到；
式 (13) 显然成立。`square`

### 结论边界

定理 219-A 不是 `Lambda*Lambda` 的 lower bound。模型没有 Euler
factorization、prime-power support 或 six-window coordinates。它严格排除的是
以下推理模板：

> 只从 pointwise coefficient bound、总质量、second moment 与逐 shift
> upper bounds，推出 critical local energy 为 little-oh。

任何成功证明都必须使用该模板没有记录的额外结构。把本模型说成实际 primes 的
反例会过度声称；把式 (9)--(13) 重新组合后仍期待自动出现 little-oh，同样会违反
这个 no-go。

## 4. Actual critical-shell finite audit [E]

脚本 `scripts/critical_local_box_audit.py` 使用：

1. actual prime powers 与 von Mangoldt weights；
2. product shell `XL^1.5<=ab<=XL^2`；
3. 笔记 218 的 `A=8` Fejér circle boxes；
4. flat compact physical window 的 exact translated overlap；
5. `beta_L^4 d_G` 的真实 normalization。

结果为：

| `X` | atoms | max box occupancy | nonzero off-pairs | diagonal / `N` | local / `N` | off/local |
|---:|---:|---:|---:|---:|---:|---:|
| 300 | 1,080 | 3 | 154 | 0.004270 | 0.005176 | 0.1750 |
| 600 | 2,580 | 4 | 390 | 0.004446 | 0.005267 | 0.1560 |
| 1,200 | 6,196 | 4 | 938 | 0.004603 | 0.005645 | 0.1846 |
| 2,500 | 15,450 | 5 | 2,708 | 0.004696 | 0.006043 | 0.2229 |
| 5,000 | 35,820 | 5 | 6,568 | 0.004746 | 0.006157 | 0.2290 |
| 10,000 | 82,296 | 7 | 16,498 | 0.004763 | 0.006349 | 0.2497 |

所有有贡献的 same-bin pairs 均通过

\[
 X|ad-bc|/\min(ad,bc)\le0.629
\tag{24}
\]

的 determinant-scale 检查；nonzero alias overlap 未出现。

这些数据只说明：

- critical local energy 在可达尺度上仍远小于 `N`；
- off-diagonal share 没有显示单调衰减；
- maximum occupancy 缓慢增长，与 uniform constant-occupancy猜想不相容但尚未构成
  asymptotic lower bound；
- finite values 不能区分 `o(N)` 与一个很小的正比例极限。

## 5. 与广义 Weil 配置的接口

笔记 218 的 clustered Fejér theorem 是一个从 local positive mass 到完整 sampled
Gram 的结构桥梁。定理 219-A 说明，在 critical scale 上，local mass 本身不能由
常见 scalar moment package 自动变小。因此：

- **完全/部分配置接口**：若式 (43) 成立，critical primitive response 继续
  atomic diagonalize，可缩小四阶矩 negative/excess budget；
- **障碍接口**：若只把 arithmetic input写成一阶、二阶与逐 shift upper bounds，
  可由定理 219-A 构造主尺度 positive local energy，紧性/GNS也不会消除它；
- **非循环性**：本轮没有使用 zeros、RH、Weil positivity或 bounded negative
  index；no-go 完全位于 finite nonnegative sequences。

模型范围：analytic obstruction 对所有 coefficient models成立；Riemann zeta 与
Dirichlet `L` 的下一步可继续利用 exact factorization。Dedekind/automorphic
models 若只有 Rankin--Selberg second moment，也同样落入本 no-go；函数域若能用
degree geometry证明 joint local law，则可能越过它。

## 6. 修正后的下一最小引理 219-B [O]

固定小 `rho>0`。对 actual prime-power atoms，保留四个 factors 与 physical
windows，证明

\[
 \beta_L^4d_G
 \sum_p
 \left\|
 \sum_{\substack{XL^{2-\rho}\le ab\le XL^2\\
                   \theta_{a/b}\in I_p}}
 |b_ab_b|g_{a/b}
 \right\|_H^2=o(N),
\tag{25}
\]

或证明其在某个 fixed sublayer 上 `gg N`。

允许的晋级输入只有：

1. factor-bin restricted joint correlation；
2. six-window support 产生的可量化 saving；
3. actual local-box occupancy/weighted incidence theorem；
4. 与 adjacent/continuum/Gamma channels 的统一 signed Gram。

若下一轮再次只得到式 (9)--(13) 类型的 scalar bounds，则按定理 219-A 停止该
尝试，不把符号重排当作进展。

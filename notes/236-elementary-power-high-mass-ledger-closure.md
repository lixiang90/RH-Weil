# 236. 幂级高乘积 dyadic mass ledger 的初等闭合

日期：2026-09-03

分支：MOM-1 / 路线 A1o；接口：exact dyadic response discrepancy

状态：balanced fixed-power boxes 的 elementary large-shift incidence、最优 central
scale `M=max(H,Y/H)` 与全部 mass-over-radius-squared ledger 为 [T]；实际
cumulative discrepancies 为 [O]。本笔记把笔记 235-H 的非振荡 mass 项无条件
降到 `O(L)=o(L^4)`，不更新 PDF，也不改变比例常数的 [C] 状态。

## 1. 本轮结论

笔记 235-H 把 exact finite band response 控制为

\[
 \frac{b_0}{M^2}+E_0\log(2+M)
 +\sum_{j\ge1}\left(\frac{b_j}{R_j^2}+E_j\right).
\tag{1}

其中 `b_j` 是 positive response-measure shell masses，`E_j` 是对应 cumulative
discrepancies。要闭合四矩，全部 boxes 的式 (1) 总和须为 `o(L^4)`。

本轮证明：对任意固定 balanced power exponent

\[
 \frac12<\theta<1,
 \qquad
 a,b,c,d\asymp Y=X^\theta,
\tag{2}

取

\[
 R=Y^2,
 \qquad H=R/X=X^{2\theta-1},
 \qquad
 \boxed{M=\max(H,Y/H),}
\tag{3}

则式 (1) 的全部 `b` 项总共只有

\[
 \boxed{O(L).}
\tag{4}

所以固定 balanced cell 的唯一剩余输入严格缩成

\[
 \boxed{E_0\log(2+M)+\sum_{j\ge1}E_j=o(L^4).}
\tag{5}

这一步不用 Bettin--Chandee、Selberg sieve、素数对渐近或任何零点信息；只用
`Lambda(n)<=L`、Chebyshev bound 与固定三变量后的 interval count。

## 2. Large-shift elementary incidence

固定 compact constants `0<c<C<infinity`。定义

\[
 \mathfrak D_Y(S)=
 \sum_{\substack{cY\le a,b,c,d\le CY\\
                  0<|ad-bc|\le S}}
 \Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d).
\tag{6}

distinct-base restrictions和 physical window weights只会减小该正和，故式 (6)
足以 majorize实际 response measure。

### 引理 236-A（elementary incidence above one factor length）[T]

若

\[
 Y\le S\le c_1Y^2
\tag{7}

且 `c_1` 是固定常数，则

\[
 \boxed{\mathfrak D_Y(S)\ll Y^2SL.}
\tag{8}

常数只依赖 `c,C,c_1`。

#### 证明

固定 `a,b,c`。条件 `|ad-bc|<=S` 把 `d` 限制在中心 `bc/a`、长度
`O(S/a)=O(S/Y)` 的 interval 中。因此纯点态地

\[
 \sum_{\substack{d\asymp Y\\|ad-bc|\le S}}\Lambda(d)
 \ll \left(\frac SY+1\right)L.
\tag{9}

Chebyshev bound 给

\[
 \sum_{n\asymp Y}\Lambda(n)\ll Y.
\tag{10}

对 `a,b,c` 求和，得到

\[
 \mathfrak D_Y(S)
 \ll Y^3\left(\frac SY+1\right)L
 =Y^2SL+Y^3L.
\tag{11}

由 `S>=Y`，第二项被第一项吸收，得到式 (8)。`square`

这里 proper prime powers 自动包含在 `Lambda` 中；不需要先删除。式 (8) 比
natural scale `Y^2S` 多一个对数，但 dyadic mass ledger有三个对数余量。

## 3. 从 determinant incidence 到 response mass

沿用笔记 234 的正 measure。单 atom-pair weight 是

\[
 w_{a,b;c,d}
 =\frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}
 {(4\pi^2)^2\sqrt{abcd}}W_{a,b;c,d},
 \qquad 0\le W_{a,b;c,d}\le1.
\tag{12}

在式 (2) 的 box 中，

\[
 \sqrt{abcd}\asymp Y^2=R.
\tag{13}

另外，对 `|t|<=T<=c_2X`，

\[
 t=X\log\frac{ad}{bc}
 \quad\Longrightarrow\quad
 |ad-bc|\ll \frac RX T=HT,
\tag{14}

因为 `ad,bc asymp R` 且 logarithm 在 fixed compact ratio range 上双 Lipschitz。

### 引理 236-B（response mass above the threshold）[T]

若

\[
 HT\ge Y,
\tag{15}

则实际 symmetrized positive response measure满足

\[
 \boxed{\mu_X([-T,T])\ll HTL.}
\tag{16}

#### 证明

由式 (12)--(14)，左边至多是

\[
 R^{-1}\mathfrak D_Y(C_0HT)
\]

乘固定常数。若 `C_0HT` 超过 fixed multiple of `R`，式 (16) 由全部四变量
Chebyshev mass `O(Y^4)` 除以 `R` 更直接；否则引理 236-A 与式 (15) 给

\[
 R^{-1}\mathfrak D_Y(C_0HT)
 \ll R^{-1}(RHTL)=HTL.
\]

`square`

## 4. Central scale 的精确选择

式 (3) 同时满足

\[
 HM\ge Y,
 \qquad
 \frac HM\le1.
\tag{17}

更显式地，

\[
 M=
 \begin{cases}
  X^{1-\theta},&1/2<\theta\le2/3,\\
  X^{2\theta-1},&2/3\le\theta<1.
 \end{cases}
\tag{18}

所以

\[
 HM=
 \begin{cases}
  X^\theta=Y,&1/2<\theta\le2/3,\\
  X^{4\theta-2}\ge X^\theta=Y,&2/3\le\theta<1,
 \end{cases}
\tag{19}

且 `M=o(X)`。因此所有 dyadic shells 都在 fixed-aperture pre-alias 区，并从
第一层起满足引理 236-B 的 large-shift threshold。

### 定理 236-C（mass-over-radius-squared ledger closure）[T]

对式 (3) 的 `M`，笔记 235-H 右端的全部 mass terms 满足

\[
 \boxed{
 \frac{b_0}{M^2}+
 \sum_{j\ge1}\frac{b_j}{R_j^2}ll L=o(L^4).}
\tag{20}

#### 证明

引理 236-B 在 `T=M` 给

\[
 b_0\ll HML,
\]

从而

\[
 \frac{b_0}{M^2}\ll\frac HM L\le L.
\tag{21}

对 `R_j=2^(j-1)M`，shell mass不超过 cumulative mass，故

\[
 b_j\ll HR_jL.
\]

于是

\[
 \sum_{j\ge1}\frac{b_j}{R_j^2}
 \ll HL\sum_{j\ge1}\frac1{R_j}
 \ll\frac HM L\le L.
\tag{22}

合并即得式 (20)。`square`

### 推论 236-D（fixed balanced cell discrepancy-only gate）[T/C]

对任意 fixed `theta in (1/2,1)` 与 fixed balanced factor/aperture cell，若式 (5)
成立，则该 cell 的 bulk alternating main response 为 `o(N)`。

式 (5) 推出结论的桥梁为 [T]；实际 primes 的式 (5) 为 [O]，所以四矩实例仍为
[C]。

#### 证明

定理 235-H、定理 236-C 与式 (5) 给 raw response `o(L^4)`。再由笔记 235-(1)
乘 `beta_L^4D`，得到 `o(N)`。`square`

若同时处理 `C_X` 个 cells，式 (20) 的总 mass ledger 是 `O(C_XL)`。因此任何

\[
 C_X=o(L^3)
\tag{23}

的 partition仍使 mass 项为 `o(L^4)`；discrepancy 项必须独立作 global求和，不能
由 per-cell little-oh 自动推出。

## 5. `theta=3/4` 的具体门槛

当 `theta=3/4` 时，

\[
 Y=X^{3/4},\qquad H=X^{1/2},\qquad M=X^{1/2},
 \qquad HM=X\ge Y.
\tag{24}

所以式 (20) 为 `O(L)`。笔记 235 的 finite experiment 取较小的
`M=X^(1/4)` 是为了有限计算量；它不对应证明中最有效的 central scale。后续数值
实验应逐步扩大到 `M=X^(1/2)` 或做 determinant-layer convolution，而不是把旧
finite `M` 直接解释成 asymptotic proof scale。

## 6. 删除审计与 no-go 边界

1. **`S>=Y` threshold**：负责在式 (11) 中吸收 `Y^3L`。删除后 elementary
   interval count有一个 `+1` endpoint tax，可能破坏 mass ledger。
2. **central scale `max(H,Y/H)`**：第一项保证 `H/M<=1`，第二项保证 `HM>=Y`；
   只取其中任一项不能覆盖全部 `theta in (1/2,1)`。
3. **balanced factor scale**：给 `sqrt(abcd)asymp Y^2`。unbalanced boxes必须用
   对应 long/short scales重算，不能直接引用式 (16)。
4. **positive window weight**：这里只用 `0<=W<=1`；没有利用 smoothness或符号
   cancellation。
5. **fixed aperture pre-alias**：保证 `T=O(X)` 与笔记 235 exact Abel region相容。

删除审计：

- 式 (20) 只闭合 positive mass terms，不控制 `E_j`；
- elementary `D(S)<<Y^2SL` 不能代替 signed discrepancy；
- fixed-cell结论不自动覆盖增长的 unbalanced partition；
- finite experiment 的 `M=X^(1/4)` 不验证式 (5)。

循环性审计：全部 [T] 结论只用 finite determinant geometry、pointwise von
Mangoldt bound、Chebyshev sums与既有 exact Gabor normalization；不调用 RH、
GRH、Hardy--Littlewood、Bettin--Chandee、Selberg sieve、Weil positivity、谱酉性
或 bounded negative index。

## 7. 修正后的下一最小引理 236-E [O]

先固定 `theta=3/4` 与一个 balanced factor/aperture cell，取证明尺度
`M=X^(1/2)`。对实际四-von-Mangoldt、six-window response measure证明

\[
 \boxed{
 E_0\log(2+X^{1/2})+\sum_{j\ge1}E_j=o(L^4).}
\tag{25}

允许把 determinant variable分成长度 `HM=X` 的 blocks，但必须保留各 block
内部的 cumulative discrepancy与 exact response weights。若只得到
`E_j=o(b_j)`，仍须检查绝对总量是否达到式 (25)。

若式 (25) 在无权整数模型中已失败，应构造完整 band lower bound；若无权模型
成立而 von Mangoldt模型失败，则缺口被进一步定位为 balanced four-prime
determinant discrepancy，而不是 Gabor/window geometry。

## 8. 可复现指数审计 [E]

脚本 `scripts/power_high_mass_scale_audit.py` 对多个
`theta in (1/2,1)` 检查：

1. `M` exponent严格位于 `(0,1)`；
2. `HM>=Y`；
3. `H/M<=1`；
4. `theta=2/3` 是两个 central-scale branches 的交点。

脚本只检查指数恒等式；引理 236-A--定理 236-C 的 incidence证明在本文给出。

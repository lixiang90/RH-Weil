# 249. Directed trigonometric numerator 与 finite overlap 证书

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：B1g finite ratio capture / physical
prime--continuum Schur gain

状态：Machin--Taylor 有理三角区间、60 位 fixed-point outward arithmetic、全部
frequency cells 的 whole-cell 判定、固定 `(Y,N,J,h)=(8,10,4,1/200)` numerator
下界及其与笔记 248 分母上界的合成为 [T]；尺度一致的 overlap 估计为 [O]。
本笔记不更新 PDF，不声称 RH/GRH、新零点比例或任何渐近结论。

## 1. 主结论

沿用笔记 244--248 的 two-sided prime/continuum measures、degree-two divided
difference multiplier 与 Brownian spectral measure。令

\[
 D=P+C
 =\int_{\mathbb R}(W_p^2+W_c^2)\,d\omega_R
\tag{1}
\]

为完整 intended finite diagonal，并令 `G` 是 ratio band

\[
 G=\left\{\xi:\frac14\le \frac{W_p(\xi)}{W_c(\xi)}\le4\right\}.
\tag{2}
\]

### 定理 249-A（fixed intended ratio certificate）[T]

对

\[
 (Y,N,J,h)=(8,10,4,1/200),\qquad |\xi|\le256,
\tag{3}
\]

存在 12,785 个经 outward rational intervals 验证的 positive-frequency cells；其
正频率总宽度为 `12785/200=63.925`，连同反射后的 Lebesgue 总宽度为 `127.85`，且

\[
 \mathcal N
 :=\int_{G_{\rm verified}}(W_p^2+W_c^2)\,d\omega_R
 \ge 0.000140734590642330727559468708.
\tag{4}
\]

结合笔记 248-A 的

\[
 D\le D_*:=0.000735925241553713216150037691,
\tag{5}
\]

得到严格 finite ratio

\[
 \boxed{
 \frac{\mathcal N}{D}
 \ge \frac{\mathcal N_*}{D_*}
 \ge0.191234900905432370>0.19.}
\tag{6}
\]

这里 `G_verified` 只是 `G` 的有限并子集；未验证 cells 与 `|xi|>256` 的能量全部
丢弃，因此式 (4) 是一侧下界。

### 推论 249-B（fixed physical overlap/Schur gain）[T]

在 band `[1/4,4]` 上逐点有

\[
 \frac{W_pW_c}{W_p^2+W_c^2}\ge\frac4{17}.
\tag{7}
\]

令 `z=<u_p,u_c>`，则笔记 244-A 的符号公式与式 (6) 给

\[
 \boxed{
 -z=\int W_pW_c\,d\omega_R
 >\frac{19}{425}(P+C).}
\tag{8}
\]

因而该 fixed intended response 的 full energy 满足

\[
 \|u_p+u_c\|^2=P+C+2z
 <\frac{387}{425}(P+C),
\tag{9}
\]

以及

\[
 \boxed{
 \frac{P+C}{\|u_p+u_c\|^2}>\frac{425}{387}
 =1.098191214470\ldots .}
\tag{10}
\]

式 (8)--(10) 是 actual physical prime/continuum direction 的 finite gain，而不是
任意系数 Bessel bound。它尚不对增长尺度一致。

## 2. Intended finite symbols

七个 prime-power weights 与 lags 为

\[
 w_n=(\log p)n^{-3/5}e^{-n/8},\qquad
 \lambda_n=\log n,
 \quad n\in\{2,3,4,5,7,8,9\}.
\tag{11}
\]

continuum small mass 与四个 cell masses 是笔记 248-(7) 的

\[
 C[a,b]=\int_a^b
 \exp\left(\frac{2x}{5}-\frac{e^x}{8}\right)dx,
\tag{12}
\]

其 nonzero nodes 为四个 cell midpoints

\[
 \frac{221}{800},\quad\frac{123}{160},\quad
 \frac{1009}{800},\quad\frac{1403}{800}.
\tag{13}
\]

由笔记 248 的 coefficient intervals 定义

\[
\begin{aligned}
 W_p(\xi)&=\sum_n w_n(1-\cos(\xi\lambda_n)),\\
 W_c(\xi)&=\sum_{j=1}^4 C_j(1-\cos(\xi x_j)),\\
 \widehat d(\xi)&=\sum_nw_n\cos(\xi\lambda_n)
 -C_0-\sum_{j=1}^4C_j\cos(\xi x_j).
\end{aligned}
\tag{14}
\]

`Q`、response scalar `s`、first-moment Lipschitz constants `L_p,L_c,L_d,L_Q`
完全按笔记 246、248 的 rational interval formulas 重算；不读取 production 浮点
midpoint values。

## 3. π 与 cosine 的 rational enclosure

对 `0<x<1`，置

\[
 A_m(x)=\sum_{j=0}^{m-1}\frac{(-1)^jx^{2j+1}}{2j+1}.
\tag{15}
\]

alternating-series remainder 给

\[
 |\arctan x-A_m(x)|\le\frac{x^{2m+1}}{2m+1},
\tag{16}
\]

且 remainder 的符号由 `m` 的奇偶确定。使用 Machin 恒等式

\[
 \pi=16\arctan(1/5)-4\arctan(1/239)
\tag{17}
\]

与 `m=90`，得到宽度小于 `10^{-100}` 的 rational interval `Pi`。式 (17) 可由
`tan(4 arctan(1/5))=120/119` 与 tangent subtraction 直接验证；所得角在
`(0,pi/2)` 且 tangent 为 1。脚本另核对

\[
 \frac{333}{106}<\Pi^-<\Pi^+<\frac{355}{113}.
\tag{18}
\]

对每个 rational argument interval `X`，以 `Pi` 选择整数 `k` 并 enclosure
`X-2k Pi`。运行时逐点断言 reduced interval 位于 `[-22/7,22/7]`。再用 degree-44
Taylor polynomial

\[
 T_{22}(x)=\sum_{j=0}^{22}\frac{(-1)^jx^{2j}}{(2j)!}
\tag{19}
\]

及统一 remainder

\[
 |\cos x-T_{22}(x)|
 \le\frac{(22/7)^{46}}{46!}
\tag{20}
\]

给每个 midpoint cosine 的 rational interval。最后与 `[-1,1]` 相交只使用
`|cos x|<=1`，不调用 libm 或 mpmath 的舍入性质。

## 4. Outward fixed-point lemma

置 `R=10^60`。每个 rational interval `[a,b]` 先映为

\[
 \left[\frac{\lfloor Ra\rfloor}{R},
       \frac{\lceil Rb\rceil}{R}\right].
\tag{21}
\]

### 引理 249-C（fixed-point inclusion invariant）[T]

若两个 stored intervals 分别包含 exact reals `x,y`，则代码中对加、减、乘、平方
及 rational scaling 的每次 endpoint floor/ceiling 后，所得 interval 分别包含
`x+y,x-y,xy,x^2` 与 rational multiple。Horner evaluation 因而包含式 (19) 与
`Q(d-hat)` 的 exact values。

#### 证明

加减由 endpoint monotonicity。乘法枚举四个 endpoint products；再除以 `R` 时向外
取整。平方在 interval 跨零时把 lower 置零，否则取两个 endpoint squares 的较小者。
rational scaling 按 scalar 符号先反射，再分别 floor/ceiling。有限归纳即给 Horner
invariant。`square`

每次 nonnegative lower product 仍向下取整到 `R^{-1}`；因此累计 numerator 是 exact
rational lower，而不是高精度浮点近似。

## 5. Whole-cell certificate

对 `i=1,...,51199` 置

\[
 I_i=[ih,(i+1)h],\qquad
 t_i=(i+1/2)h,\qquad h=1/200.
\tag{22}
\]

`i=0` 的 cell 接触原点，为保持笔记 246-B 的 `t-r>0` 前提而直接丢弃。对每个
midpoint用第 2--4 节得到 intervals，再加入 exact global Lipschitz radii
`L_p h/2,L_c h/2,L_Q h/2`，形成

\[
 p_i^-,p_i^+,c_i^-,c_i^+,q_i^-.
\tag{23}
\]

只有满足

\[
 p_i^-,c_i^-,q_i^->0,\qquad
 4p_i^-\ge c_i^+,\qquad p_i^+\le4c_i^-
\tag{24}
\]

的 cells 才进入证书。每格贡献取笔记 246-(11) 的 rational lower

\[
 n_i=\frac{|s|_-^2(q_i^-)^2}{\pi^+((i+1)h)^2}
 \bigl((p_i^-)^2+(c_i^-)^2\bigr)h,
\tag{25}
\]

其中所有乘法继续向下取整。求和 `sum n_i` 给式 (4)。

## 6. 可复现指纹

最终脚本输出并冻结：

- `verified_cell_count = 12785`；
- cell-index SHA-256：
  `d781244d33bbec81edb8ba786eb28f035465883981b5abde178c3da5d3cabb9b`；
- `(index, fixed lower)` SHA-256：
  `4237a9a77ce37542db43f680374d3fdba8f778e68f91070b519adc3e2e134a10`；
- `numerator_lower = 0.000140734590642330727559468708`；
- `ratio_lower = 0.191234900905432370`。

脚本会在 count、任一 hash、式 (4) 或 `ratio>0.19` 失效时退出非零。
`scripts/test_b1g_fixed_intervals.py` 另以 exact rationals 检查正负 floor/ceiling、
interval multiplication、Machin enclosure、`cos(0)`、`cos(pi)` 与 `cos(2pi)`。

## 7. 最小输入、删除与循环性审计

最小输入是：七个 explicit prime powers、五个 finite continuum integrals、笔记 248
的 coefficient intervals、alternating atan/cos series、fixed-point inclusion invariant、
笔记 246 的 Lipschitz cell theorem及笔记 248 的 denominator upper。

删除审计：

- 删除 directed π/cosine remainder，midpoint values 只剩数值证据；
- 删除 coefficient intervals，证书只适用于 binary64 surrogate；
- 删除 Lipschitz radii，midpoint good 不推出 whole-cell good；
- 删除 outward rounding，每格 lower 可能向上漂移；
- 删除 denominator upper，numerator 不能转成 capture fraction；
- 删除 fixed ratio band，overlap factor可趋零；
- 把 `(8,10,4)` 外推到增长尺度，违反 finite-to-bulk 纪律。

非同义反复审计：公理没有包含 `N_*/D_*>0.19` 或 cross gain；两者来自逐 cell
有限计算与独立 denominator transfer，证书完全可能失败。式 (7) 是 elementary
ratio inequality，而式 (6) 是新的 arithmetic finite input。

循环性审计：未使用 zeros、RH/GRH、Weil positivity、谱酉性、PNT error、Mertens
平方根界或 bounded negative index。prime side 只枚举 `n<=10` 的 von Mangoldt
weights；compactness/choice 不产生任何正性。

## 8. 模型范围与下一最小引理 B1h [O]

- Riemann zeta 的当前 fixed Abel model：定理 249-A--B 直接适用；
- Dedekind positive-coefficient finite models：同一 schema 可用，但需重新 enclosure
  ideal weights 与多 Archimedean channels；
- primitive Dirichlet/automorphic L：complex phases 破坏 scalar sign cones，不能直接
  引用 249-B；
- 函数域：degree lags 离散，trigonometric rationalization更简单；
- 本结果属于显式公式型 Weil response，不建立上同调极化或 Hard Lefschetz bridge。

B1g 已闭合。下一最小引理 B1h 是对第二个预注册实例

\[
 (Y,N,J,h)=(16,15,4,1/200)
\tag{26}
\]

完成同型 denominator/numerator certificate，并比较两个尺度的 verified frequency
arcs 在 `xi/log Y` 或其他自然归一化下是否有稳定 core。若第二尺度不能保持固定正
capture，立即停止该参数族；若保持，则下一步才尝试把 prime--continuum ratio failure
归约为独立的 smoothed prime discrepancy estimate。两个 finite points 本身仍不构成
uniform B1a。

后续：笔记 250 已对该预注册第二尺度证明
`N_lower/D_upper>0.159849154333328712>3/20` 及
`-z>(3/85)(P+C)` [T]。两个 finite points仍不构成 uniform B1a；当前下一最小
引理为在 `theta=xi log Y` 下审计两组 verified arcs 的共同 whole-cell core。

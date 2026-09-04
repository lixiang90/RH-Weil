# 253. Matched-endpoint PNT transfer 与 Schur ratio closure

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1k matched cofinal transfer / physical
prime--continuum ratio

状态：普通素数定理在 nonresonant compact normalized cores 上推出 matched
prime--continuum symbol ratio一致趋于 `1` 为 [T]，唯一外部输入为
`psi(x)=x+o(x)` [R]。这关闭 B1 的 scalar ratio leg，但不推出 response-energy
capture、完整 physical Schur gain、RH/GRH 或 Weil 正性。本笔记只更新 Markdown，
不更新 PDF。

## 1. 预注册 matched schedule

固定

\[
 0<\sigma<1,\qquad a=1-\sigma>0,
\tag{1}
\]

并令

\[
 Y_m=2^m,\qquad N_m\ge Y_m,\qquad
 L_m=\log N_m,\qquad \xi_m(t)=\frac{t}{m}.
\tag{2}
\]

沿用笔记 252 的记号

\[
 F_{Y,\xi}(x)=x^{-\sigma}e^{-x/Y}
   \bigl(1-\cos(\xi\log x)\bigr),
\tag{3}
\]

\[
 P_{Y,N}(\xi)=\sum_{2\le n\le N}\Lambda(n)F_{Y,\xi}(n),
\qquad
 C_{Y,\log N}(\xi)=\int_1^N F_{Y,\xi}(x)\,dx.
\tag{4}
\]

令 `E(x)=psi(x)-x`。笔记 252 的 exact identity 给

\[
 P_{Y,N}(\xi)-C_{Y,\log N}(\xi)
 =R_{Y,N}(\xi),
\tag{5}
\]

其中

\[
 R_{Y,N}(\xi)
 =F_{Y,\xi}(N)E(N)-\int_1^N E(x)F'_{Y,\xi}(x)\,dx.
\tag{6}
\]

matched endpoint 已使 endpoint mismatch 精确为零；本笔记暂时使用 exact continuum，
所以也没有 quadrature error。

## 2. Nonresonant compact core

设 `K subset R` 为固定非空紧集，并要求

\[
 \delta_K:=\min_{t\in K}
 \bigl(1-\cos(t\log2)\bigr)>0.
\tag{7}
\]

这等价于 `K` 与 resonant lattice

\[
 \mathcal R=\frac{2\pi}{\log2}\mathbb Z
\tag{8}
\]

有正距离。条件 (7) 不是 RH 型输入；它只是选择 normalized phase chart 中 continuum
main term不发生二阶退化的区域。

## 3. Uniform matched-symbol transfer

### 定理 253-A（qualitative PNT suffices off resonance）[T]

在式 (1)--(7) 下，若

\[
 \psi(x)=x+o(x)
\tag{9}
\]

[R]，则对任意 cutoff schedule `N_m>=Y_m`，

\[
 \boxed{
 \sup_{t\in K}
 \frac{\left|P_{Y_m,N_m}(t/m)
 -C_{Y_m,\log N_m}(t/m)\right|}
 {C_{Y_m,\log N_m}(t/m)}\longrightarrow0.}
\tag{10}
\]

不需要给式 (9) 任何显式收敛速度，也不需要对 `N_m/Y_m` 加上界。

#### 证明：continuum denominator lower

置 `M=max_(t in K)|t|`。对 `Y_m/2<=x<=Y_m`，

\[
 \left|\frac{t\log x}{m}-t\log2\right|
 =\frac{|t|}{m}\left|\log\frac{x}{Y_m}\right|
 \le\frac{M\log2}{m}.
\tag{11}
\]

因此由紧性、连续性与式 (7)，充分大 `m` 时一致有

\[
 1-\cos\frac{t\log x}{m}\ge\frac{\delta_K}{2}.
\tag{12}
\]

又因 `N_m>=Y_m`，区间 `[Y_m/2,Y_m]` 包含于式 (4) 的积分域；在该区间
`x^(-sigma)>=Y_m^(-sigma)` 且 `exp(-x/Y_m)>=e^(-1)`。故

\[
 C_{Y_m,\log N_m}(t/m)
 \ge \frac{\delta_K}{4e}Y_m^a
\tag{13}
\]

对所有 `t in K` 一致成立。

#### 证明：Stieltjes remainder upper

由笔记 252 的显式导数，对 `m>=1,t in K` 有

\[
 x\left|F'_{Y_m,t/m}(x)\right|
 \le x^{-\sigma}e^{-x/Y_m}
 \left(M+2\sigma+\frac{2x}{Y_m}\right).
\tag{14}
\]

任取 `epsilon>0`。由式 (9)，存在 `X_epsilon`，使

\[
 |E(x)|\le\epsilon x\qquad(x\ge X_\epsilon).
\tag{15}
\]

式 (14) 与 Gamma integral 给

\[
\begin{aligned}
 \int_{X_\epsilon}^{N_m}|E(x)F'(x)|\,dx
 &\le\epsilon A_{K,\sigma}Y_m^a,\\
 A_{K,\sigma}
 &:=(M+2\sigma)\Gamma(a)+2\Gamma(a+1).
\end{aligned}
\tag{16}
\]

在固定区间 `[1,X_epsilon]` 上，`E` 局部有界，式 (14) 又给一个与 `m,t`
无关的可积 majorant。因此存在只依赖 `epsilon,K,sigma` 的有限常数
`B_(epsilon,K,sigma)`，使

\[
 \sup_{t\in K}
 \int_1^{X_\epsilon}|E(x)F'(x)|\,dx
 \le B_{\epsilon,K,\sigma}.
\tag{17}
\]

因 `a>0`，右端除以 `Y_m^a` 后趋于零。

对 endpoint，置 `r_m=N_m/Y_m>=1`。充分大 `m` 时 `N_m>=X_epsilon`，故

\[
\begin{aligned}
 |F_{Y_m,t/m}(N_m)E(N_m)|
 &\le2\epsilon N_m^ae^{-N_m/Y_m}\\
 &\le2\epsilon Y_m^a
   \sup_{r\ge1}r^ae^{-r}.
\end{aligned}
\tag{18}
\]

式 (6)、(16)--(18) 遂给

\[
 \limsup_{m\to\infty}
 \sup_{t\in K}\frac{|R_{Y_m,N_m}(t/m)|}{Y_m^a}
 \le B_{K,\sigma}\epsilon.
\tag{19}
\]

令 `epsilon downarrow0`，再结合式 (5)、(13)，得到式 (10)。`square`

## 4. Ratio 与 scalar Schur factor

### 推论 253-B（ratio leg asymptotically closes）[T]

在定理 253-A 的 hypotheses 下，

\[
 \sup_{t\in K}
 \left|\frac{P_{Y_m,N_m}(t/m)}
 {C_{Y_m,\log N_m}(t/m)}-1\right|\longrightarrow0.
\tag{20}
\]

特别地，任给 `0<q_-<1<q_+<infinity`，充分大 `m` 时整个 `K` 上都有

\[
 q_-\le\frac{P_{Y_m,N_m}(t/m)}
 {C_{Y_m,\log N_m}(t/m)}\le q_+.
\tag{21}
\]

并且 scalar Schur factor满足

\[
 \sup_{t\in K}\left|
 \frac{P_{Y_m,N_m}(t/m)C_{Y_m,\log N_m}(t/m)}
 {P_{Y_m,N_m}(t/m)^2+C_{Y_m,\log N_m}(t/m)^2}
 -\frac12\right|\longrightarrow0.
\tag{22}
\]

#### 证明

式 (13) 使 denominator严格为正；式 (20) 是式 (10) 的改写。连续函数
`r/(1+r^2)` 在 `r=1` 处取 `1/2`，故 uniform convergence给式 (22)。`square`

式 (22) 真正关闭的是 B1 的 pointwise ratio/Schur scalar；它没有说明 `K` 携带总
physical response energy 的固定比例。

## 5. 有限 common core 可无损地避开共振

令 `K_0` 是笔记 251 的 18-component exact common core，总宽 `29.655`。其与
`mathcal R` 的交集有限。

### 推论 253-C（nonresonant pruning）[T]

对任意 `eta>0`，存在 compact `K_eta subset K_0`，满足

\[
 |K_0\setminus K_\eta|<\eta,
 \qquad
 \min_{t\in K_\eta}(1-\cos(t\log2))>0.
\tag{23}
\]

而且对每个给定的 `eta>0`，都可把这些删除邻域取得更小，使笔记 251 的两个
certified finite lower measures在 `K_eta` 上仍分别捕获超过 `D_8/20` 与
`D_16/20`。因此 finite common-core 证书与定理 253-A 的 nonresonant hypothesis相容。

#### 证明

在有界 `K_0` 内只有有限个 resonant points。围绕它们取总长度小于 `eta` 的有限个
开邻域，并从 `K_0` 删除；所得集合紧且与 `mathcal R` 有正距离，给式 (23)。笔记
251 的 certified lower measures具有有限 piecewise-constant densities，故对 Lebesgue
测度绝对连续。删除邻域的总宽趋零时，两份 certified mass loss同时趋零。原 lower
分别严格大于 `0.053294 D_8` 与 `0.113275 D_16`，所以可把删除取得足够小而仍同时
严格大于 `D_8/20,D_16/20`。`square`

这里没有用紧性“制造正性”：正 lower来自笔记 251 已认证的 pointwise densities；
compact pruning只删除任意小的有限质量。

## 6. 最小公理、删除审计与循环性

定理 253-A 的实际输入只有：

1. `[T]` exact Stieltjes identity；作用是把差精确化为式 (6)；
2. `[R]` qualitative PNT `E(x)=o(x)`；作用是式 (15)，没有速率要求；
3. `[T]` matched endpoint `L_m=log N_m`；作用是消去笔记 252 的 endpoint mismatch；
4. `[T]` `N_m>=Y_m`；作用是保留 denominator lower所用的 Abel bulk interval；
5. `[T]` `0<sigma<1`；作用是给增长尺度 `Y_m^a` 与可积 Gamma majorant；
6. `[T]` nonresonance (7)；作用是给 uniform denominator lower (13)。

删除审计：

- 删除 matched endpoint，笔记 252 已证明 fixed-lag ratio反而逃逸；
- 删除 PNT，式 (6) 仍精确，但没有 `o(Y_m^a)` remainder；
- 删除 `N_m>=Y_m`，当前 bulk lower区间可能落在 cutoff之外；
- 让 `K` 接触 resonant lattice，式 (13) 退化，denominator可降至
  `Y_m^a/m^2`；qualitative PNT只直接给 `o(Y_m^a)`，因而本证明失效。这是所用最小
  输入的边界，不声称 resonant transfer本身为假；
- 删除 `a>0`，固定 lower interval的贡献不再形成压倒 compact initial segment 的增长量。

结论不是 PNT 的同义改写：还使用 Abel kernel localization、matched endpoint与
nonresonant phase lower；反过来式 (10) 只测试这一核族，不推出 full PNT。循环性审计中
没有 zeros、RH/GRH、zero-density estimate、RH-strength PNT error、Weil positivity、
谱酉性、bounded negative index或选择原理。PNT 的权威来源见文献表来源 45。

## 7. 模型范围

- Riemann zeta：定理 253-A 直接适用；
- 具有 summatory law `A(x)=x+o(x)` 的非负 Euler coefficient模型：相同证明逐字适用；
- Dedekind zeta：以 ideal norm计数并使用相应 ideal PNT 后可复制，需单独记录 residue
  normalization；
- 非主 Dirichlet 或一般 oscillatory automorphic coefficients：main summatory law不是
  `x+o(x)`，式 (13) 的 continuum main term也应改变，不能直接套用；
- 函数域：连续 Gamma integral应换成 degree sum；本定理不自动提供该离散 bridge；
- 结果属于显式公式型 Weil response，不建立上同调型 polarization bridge。

## 8. B1l target 及后续障碍 [T/N]

B1j 已排除 fixed-lag cofinalization；B1k 又证明 matched scalar ratio在 nonresonant
compact core上由普通 PNT自动闭合。剩余缺口现在严格缩为 response-density capture：
对实际 Brownian/Gamma multiplier产生的 diagonal spectral energy measure
`mathcal E_m`，寻找一个由推论 253-C 允许的 fixed compact `K` 与常数 `c>0`，证明

\[
 \liminf_{m\to\infty}
 \frac{\mathcal E_m(K)}{\mathcal E_m(\mathbb R)}\ge c.
\tag{24}
\]

必须先写出 `mathcal E_m` 的实际物理 multiplier 与 normalization，再估计式 (24)；
不得用 arbitrary-coefficient Bessel bound替代，也不得从 `Y=8,16` 的 finite mass
直接外推。若式 (24) 成立，则式 (22) 与已证 symmetric response sign把它转成
scale-uniform physical Schur gain；若失败，应证明 energy escape/tightness obstruction，
而不是继续增加 finite scales。

后续：笔记 254 已证明 actual degree-two multiplier在同一 matched core 上按
`mu_m^2+Delta_m^2` 二次消失，故 raw ratio-core energy不能以 scale-neutral multiplier
直接转成 response energy [T/N]。B1l 因此以 multiplier-degeneracy obstruction 结束；
新的 B1m 必须比较带 `q_kappa(mu,Delta)^2` 权的 core 与 total energy，并为 denominator
另证 lower。Gamma residual 仍是独立第三通道，未被此二通道结论吸收。

# 243. Common-convolution 符号障碍与 physical cross-variation 分解

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：degree-two Brownian response / prime--continuum
physical Gram

状态：primitive--convolution 恒等式、正 multiplier 的符号保持、任意带符号
common multiplier 的整体符号翻转反例，以及 cross-variation 充分条件为
[T]/[N]；真实 zeta quadrature 的 base-sign 与 response leakage 为 [E]；uniform
sign-bias 和 cross-visibility 为 [O]。本笔记不更新 PDF，不声称 RH/GRH 或新的
零点比例。

## 1. 结论摘要

笔记 242 把 B1 的 intrinsic target 缩成 physical prime--continuum correlation

\[
 \Re\langle u_p,u_c\rangle
 \le -\delta(\|u_p\|_2^2+\|u_c\|_2^2).
\tag{1}
\]

一个自然尝试是利用未乘 response multiplier 前的符号：prime 原子为正，
continuum quadrature 原子为负；各自于 lag zero 居中后，其 Brownian primitives
逐点反号。本轮证明这条尝试不能直接穿过 common divided-difference multiplier：

1. 非负 common multiplier 的确保持逐点反号；
2. 一般带符号 common multiplier 不仅会产生局部正交叉，还可把**整体**内积从负
   翻成正；
3. 真实 finite zeta 数据中，base positive cross精确为零，而 response后的正交叉
   占总 cross variation 的约 `3%--9%`。

所以“原始 prime/continuum 测度符号相反”本身不足以证明式 (1)。下一输入必须
使用 actual divided-difference multiplier 的 Toeplitz/频率结构，而不能只调用
PNT 顺序或 positive/negative atom labels。

## 2. Primitive 与 common convolution

对有限紧支撑实 signed measure `sigma` 定义右连续 primitive

\[
 F_\sigma(t)=\sigma(( -\infty,t]).
\tag{2}
\]

端点取值不影响下文的 `L^2` 内积。

### 引理 243-A（primitive--convolution identity）[T]

若 `mu(R)=0`，而 `R` 为任意有限紧支撑 signed measure，则

\[
 \boxed{F_{\mu*R}(t)=\int F_\mu(t-s)\,dR(s).}
\tag{3}
\]

特别地，若记右端为 `F_mu*R`，则 common response对 primitive仍是同一个
translation convolution operator。

#### 证明

由有限 Fubini，

\[
\begin{aligned}
 F_{\mu*R}(t)
 &=\iint {\bf1}_{x+s\le t}\,d\mu(x)dR(s)\\
 &=\int F_\mu(t-s)\,dR(s).
\end{aligned}
\]

零质量条件保证 primitive 在两端消失，从而属于当前 Brownian package；恒等式
本身只需有限变差。`square`

### 命题 243-B（positive multiplier preserves opposite cones）[T]

设 `mu,nu` 是引理 243-A 中的零质量 measures，且
`F_mu<=0`、`F_nu>=0` 几乎处处。若 `R` 是非负 measure，则

\[
 F_{\mu*R}\le0,\qquad F_{\nu*R}\ge0,
\tag{4}
\]

因而

\[
 \Re\langle F_{\mu*R},F_{\nu*R}\rangle\le0.
\tag{5}
\]

#### 证明

式 (3) 将每个新 primitive 写成原 primitive 的非负 translates 平均；两个
pointwise cones 分别保持。逐点相乘并积分即得式 (5)。`square`

这里 `R>=0` 是实质公理。degree-two divided difference 是完整 signed symbol 的
四次多项式，不能无条件视为非负 measure。

## 3. Common signed multiplier 可翻转整体相关

### 障碍定理 243-C（integrated sign reversal）[N]

存在两个零质量 atomic measures `mu,nu` 与一个零质量 common signed atomic
multiplier `R`，使

\[
 F_\mu F_\nu\le0\quad\hbox{pointwise},\qquad
 \langle F_\mu,F_\nu\rangle=-1,
\tag{6}
\]

但

\[
 \boxed{\langle F_{\mu*R},F_{\nu*R}\rangle=2>0.}
\tag{7}
\]

#### 显式构造与证明

取

\[
 \mu=\delta_1-\delta_0,
 \qquad
 \nu=\delta_0-\delta_3.
\tag{8}
\]

则

\[
 F_\mu=-{\bf1}_{[0,1)},
 \qquad
 F_\nu={\bf1}_{[0,3)},
\tag{9}
\]

所以式 (6)成立。再取

\[
 R=\sum_{j=0}^{11}r_j\delta_j,
\quad
 (r_0,\ldots,r_{11})=
 (2,-3,-1,4,-2,-4,4,2,-4,1,3,-2).
\tag{10}
\]

直接相加给 `sum r_j=0`。在单位区间 `[j,j+1)` 上，式 (3)给

\[
 F_{\mu*R}=-r_j,
 \qquad
 F_{\nu*R}=r_j+r_{j-1}+r_{j-2},
\tag{11}
\]

其中范围外的 `r_j` 置零。因此

\[
\begin{aligned}
 \langle F_{\mu*R},F_{\nu*R}\rangle
 &=-\left(
 \sum_jr_j^2+
 \sum_{j\ge1}r_jr_{j-1}+
 \sum_{j\ge2}r_jr_{j-2}
 \right)\\
 &=-(100-30-72)=2.
\end{aligned}
\tag{12}
\]

这证明式 (7)。`square`

反例比“局部可能变号”更强：它说明 base primitive order甚至不控制 response
后的**积分符号**。因此任何 B1a 证明若只使用 base signs 和“两个通道乘同一
multiplier”，都在逻辑上失效。

Fourier 语言下同一障碍写成

\[
 \langle F_\mu*R,F_\nu*R\rangle
 =\frac1{2\pi}\int |\widehat R(\xi)|^2
 \widehat F_\mu(\xi)\overline{\widehat F_\nu(\xi)}\,d\xi.
\tag{13}
\]

common multiplier只提供非负频率权 `|R-hat|^2`；若 base cross-spectrum 的实部
改变符号，这个权可以重新选择正负频段。pointwise physical-space 反号并不等于
frequencywise cross-spectrum非正。

## 4. Exact cross-variation ledger

对 actual response primitives 置

\[
 x(t)=\Re(u_p(t)\overline{u_c(t)}),
\tag{14}
\]

并定义

\[
 P_+=\int x_+(t)dt,
 \qquad
 P_-=\int x_-(t)dt,
 \qquad
 V_\times=P_++P_-.
\tag{15}
\]

### 定理 243-D（sign-bias times cross-visibility）[T]

若 `V_cross>0`，置

\[
 q_+=\frac{P_+}{V_\times}.
\tag{16}
\]

则

\[
 \boxed{
 \Re\langle u_p,u_c\rangle
 =P_+-P_-=-(1-2q_+)V_\times.}
\tag{17}
\]

特别地，若存在 scale-uniform `epsilon,kappa>0` 使

\[
 q_+\le\frac12-\epsilon,
 \qquad
 V_\times\ge
 \kappa(\|u_p\|_2^2+\|u_c\|_2^2),
\tag{18}
\]

则笔记 242 的 B1a 成立，且可取

\[
 \boxed{\delta=2\epsilon\kappa.}
\tag{19}
\]

#### 证明

式 (17)只是 `x=x_+-x_-` 的积分分解。式 (18)给
`1-2q_+>=2epsilon`，代入式 (17)即得式 (19)。`square`

定理 243-D 是审计分解，不伪装成新的算术估计。它明确暴露两个必须分别防止的
机制：

1. **sign-bias failure**：正负 cross variation趋于平衡，`q_+ -> 1/2`；
2. **visibility failure**：cross variation相对于两通道能量消失，
   `V_cross/(P+C) -> 0`。

只控制第一项时可把两个向量趋于正交；只控制第二项时 cross仍可主要为正。
因此删除式 (18) 任一条件，结论均失效。

## 5. 真实 finite zeta sign ledger [E]

`scripts/vaughan_brownian_schur_audit.py` 先对未乘 common response 的 centered
prime/continuum symbols应用同一 primitive scan。由于正 prime atoms 与负
continuum atoms均为 two-sided symmetric，base primitives 在负半轴和正半轴
分别反号；脚本逐点验证 `base P_+=0`。

随后对完整 degree-two divided-difference response重算式 (15)--(17)：

| scale, `N` | base `q_+` | response `q_+` | `V_cross/(P+C)` | `Re z/(P+C)` |
|---:|---:|---:|---:|---:|
| 4, 7 | 0 | 0.04399 | 0.385 | -0.351 |
| 8, 10 | 0 | 0.08402 | 0.324 | -0.270 |
| 12, 12 | 0 | 0.09114 | 0.297 | -0.243 |
| 16, 15 | 0 | 0.03124 | 0.318 | -0.298 |

每行都满足式 (17) 的数值重构。正 leakage严格非零，故 actual response不保持
base pointwise cone；但当前四个尺度仍有明显 sign bias与 cross visibility。这只
是 finite evidence，既不证明它们一致有界，也不排除更大尺度翻转。

独立脚本 `scripts/brownian_convolution_sign_obstruction_audit.py` 用整数运算验证
定理 243-C 的 `100-30-72=-2` Toeplitz ledger。

## 6. 下一最小引理 B1b [O]

在一个固定 nonvacuous Vaughan rectangle 和真实 degree-two multiplier
`R_(M,L)(d)` 上，证明存在与 scale 无关的 `theta<1` 使

\[
\boxed{P_+\le\theta P_-.}
\tag{20}
\]

此时

\[
 q_+\le\frac{\theta}{1+\theta}
 =\frac12-\frac{1-\theta}{2(1+\theta)}.
\tag{20a}
\]

所以若再有式 (21)，定理 243-D 给

\[
 \delta=\kappa\frac{1-\theta}{1+\theta}.
\tag{20b}
\]

式 (20)只要求**积分 sign bias**，不要求错误的逐点非正。证明必须保留式 (13)
中的 actual multiplier、prime coefficients、continuum/Gamma quadrature和共同
频率权；不得用 arbitrary signed multiplier 或仅用 base atom signs。

若 B1b 成立，下一步 B1c 是独立证明 cross visibility

\[
 V_\times\ge\kappa(P+C).
\tag{21}

此二步比直接写式 (1)更可证伪，但联合起来比式 (1)略强，不能描述成已经降低
RH-strength。若 finite scales 出现 `P_+/P_- -> 1`、整体符号翻转，或式 (21)
退化，则停止 uniform-factor 路线，返回笔记 242 的 two-defect Schur absolute /
summable budgets。

## 7. 最小公理、删除审计与循环性

本轮 [T]/[N] 只用：

1. finite signed measures与 Fubini；
2. zero-mass Brownian primitives；
3. translation convolution；
4. elementary `L^2` inner product；
5. 一个显式整数 Toeplitz quadratic form。

删除审计：

- 删除 `R>=0`，243-B 被 243-C严格反驳；
- 只知道 base pointwise opposite signs，不能推出 response的局部或整体符号；
- 只知道两个通道使用同一 multiplier，式 (13)仍允许频率重加权翻转；
- 删除 sign bias 或 cross visibility 的任一项，243-D 不给 uniform `delta`；
- 把 finite `q_+` 数据升级成 asymptotic theorem，会违反 finite-to-bulk 审计。

非同义反复审计：243-A--B 是结构接口；243-C 是严格 no-go，排除一类自然证明；
243-D 明确标为 exact ledger。真正的新算术输入只有式 (20)--(21)，均标为 [O]。

循环性审计：全部 [T]/[N] 不调用 RH/GRH、Weil positivity、谱酉性、Mertens
平方根界或 bounded negative index。B1b/B1c 必须由 prime--continuum response的
独立算术估计证明。

## 8. 模型范围与 Weil 接口

- **Riemann zeta**：base sign由正 von Mangoldt atoms与负 continuum quadrature
  给出；243-C 证明这不足以穿过 degree-two response。
- **primitive Dirichlet L**：character phases通常已破坏 base pointwise order；
  必须直接控制 real cross spectrum，不能沿用 zeta 的 base-sign 图像。
- **Dedekind/automorphic L**：若 coefficients非负且 Archimedean背景反号，
  243-A--D仍适用；若 coefficients带相位，则从 complex Hermitian实部开始。
- **函数域**：有限 degree lattice上的 convolution identity保留；Frobenius纯性不能
  作为 B1b 的隐藏输入。
- **一般谱 zeta 模型**：243-C 适用于任何以 common signed translation multiplier
  处理两个 opposite primitive cones 的方案。
- **上同调型 Weil 结构**：本轮仍完全位于显式公式/Hilbert Gram侧；没有建立到
  极化、Hard Lefschetz 或 Frobenius权重的桥梁。

本轮的可发表型贡献候选是一个通用符号障碍：common response factorization并不
把原子侧的正负顺序传递到 Weil/Brownian Gram。对 zeta，下一最小输入已从模糊的
“prime--continuum cancellation”缩成 actual multiplier 下的 positive-leakage
budget (20)，随后才是 visibility (21)。

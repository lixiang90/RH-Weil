# 242. Vaughan cutoff vacuity、physical quotient invariance 与 continuum Schur

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：degree-two Brownian response / Type-I--II--continuum physical Gram

状态：simultaneous square-root cutoff 的 Type-II vacuity、channel-map quotient
invariance、physical continuum Schur completion 与 diagonal-ratio gauge no-go 为
[T]/[N]；修正后的 cube-root-cutoff Gram 为 [E]；uniform negative
prime--continuum correlation 为 [O]。本笔记修正笔记 195 的 finite evidence解释，
不更新 PDF，不声称 RH/GRH 或新的零点比例。

## 1. 关键审计结论

笔记 195 使用

\[
 U=V=\lfloor\sqrt N\rfloor
\tag{1}
\]

构造 finite Type-I/Type-II/continuum Brownian Gram，并报告
`diagonal/full=1.95--3.36`。本轮发现：在式 (1) 下 Type-II coefficients 对全部
`n<=N` 恒为零。因此旧表验证的 cross cancellation完全是 prime--continuum
cancellation，不是 Type-I--Type-II cancellation。

这不影响笔记 195 的 divided-difference factorization 与 Gram PSD 恒等式；它只
撤销旧 finite table 对非平凡 Type-II channel 的证据解释。

进一步，三通道 diagonal sum依赖 Vaughan cutoff/decomposition，而 physical
all-ones energy不依赖。故“证明 full/diagonal 小于某个常数”不是 intrinsic B1
目标；正确对象是先合并 physical prime vector，再研究它与 continuum 的 actual
correlation或 Schur residual。

## 2. Type-II 支撑与 square-root vacuity

canonical physical Vaughan quotient 为

\[
 \Lambda=I_{U,V}+II_{U,V},
\tag{2}
\]

其中

\[
 II_{U,V}
 =(\mu_{>U}*\Lambda_{>V}*1).
\tag{3}
\]

### 定理 242-A（exact Type-II support floor）[T]

对每个

\[
 n<(U+1)(V+1)
\tag{4}
\]

有

\[
 \boxed{II_{U,V}(n)=0.}
\tag{5}
\]

特别地，若 `U=V=floor(sqrt N)`，则

\[
 (U+1)^2>N,
\tag{6}
\]

所以

\[
 \boxed{II_{U,U}(n)=0\quad(1\le n\le N).}
\tag{7}
\]

#### 证明

式 (3) 的任一非零 summand有

\[
 n=rvw,\qquad r>U,\quad v>V,\quad w\ge1,
\]

故 `n>=(U+1)(V+1)`，证明式 (5)。若 `U=floor(sqrt N)`，则
`U+1>sqrt N`，给式 (6)--(7)。`square`

因此 simultaneous square-root **cutoff** 不能测试 Type II。这里不要与
“square-root response rectangle”混淆：后者可描述 lag/product geometry，但不允许
把两个 Vaughan truncations都选到 `sqrt N`。

## 3. 非空 finite normalization

修正后的审计取 balanced

\[
 \boxed{U=V=\lfloor N^{1/3}\rfloor.}
\tag{8}
\]

这不是 asymptotic 最优性主张；它只保证 finite range中有真实机会出现
`r>U,v>V,rv<=N`。脚本还逐点断言 Type-II response energy严格为正。旧的
square-root choice同时被独立重构，并断言其全部 Type-II coefficients为零。

## 4. Channel map 的 physical quotient invariance

沿用笔记 195。固定完整 symbol `d`、其 total mass `M` 与 common divided
difference multiplier `R_(M,L)(d)`。对任意 symbol component `c` 定义 linear
centered response map

\[
 {\mathcal L}_d(c)
 =-\kappa^2(c-c(\mathbb R)\delta_0)*R_{M,L}(d).
\tag{9}
\]

取其 vanishing-at-infinity Brownian primitive，记为 `U(c)`。该 primitive关于
`c` 仍线性。

若两个不同 cutoffs给 exact decompositions

\[
 d_p=d_I+d_{II}=d_I'+d_{II}',
\tag{10}
\]

则定义

\[
 u_I=U(d_I),\quad u_{II}=U(d_{II}),\quad
 u_p=U(d_p),\quad u_c=U(d_c).
\tag{11}
\]

### 定理 242-B（physical prime quotient is cutoff-invariant）[T]

对每个 exact Vaughan cutoff，

\[
 \boxed{u_I+u_{II}=u_p.}
\tag{12}
\]

因此下列 quantities 全部与 cutoff及 Type-I/II representative无关：

\[
 P=\|u_p\|_2^2,\qquad
 C=\|u_c\|_2^2,\qquad
 z=\langle u_p,u_c\rangle,
\tag{13}
\]

以及 physical energy

\[
 \boxed{E=\|u_p+u_c\|_2^2=P+C+2\Re z.}
\tag{14}
\]

#### 证明

式 (9) 与 Brownian primitive都线性。将式 (10) 代入即得式 (12)，再直接得到
式 (13)--(14)。`square`

这一定理给 B1 的正确 quotient：Type-I/II 只可作为证明 `P,z` 的内部 arithmetic
坐标，不能把 channel diagonal sum当成最终结构量。

## 5. Diagonal/full ratio 可以被 decomposition 人为放大

### 障碍定理 242-C（channel-diagonal inflation）[N]

固定 `u_p,u_c`，并取任意非零 `h in L^2`。对任意 `R>0` 置

\[
 u_I^{(R)}=u_I+Rh,\qquad
 u_{II}^{(R)}=u_{II}-Rh.
\tag{15}
\]

则 physical energy (14)保持不变，而三通道 diagonal sum

\[
 D_R=\|u_I^{(R)}\|^2+
 \|u_{II}^{(R)}\|^2+\|u_c\|^2
\tag{16}
\]

满足

\[
 D_R=2R^2\|h\|^2+O(R)\longrightarrow\infty.
\tag{17}
\]

#### 证明

式 (15) 的前两项之和恒为 `u_p`，故式 (14)不变。分别展开两个平方范数即得
式 (17)。`square`

所以 `diagonal/full` 可以在 physical response不变时任意增大。它可用来诊断
一个 fixed canonical decomposition中的 cancellation，但不能作为跨 cutoff 的
theorem target或“结构改善常数”。

## 6. Exact physical continuum Schur completion

令三通道 Gram 按 prime/continuum 分块为

\[
 G=
 \begin{pmatrix}
 A&b\\ b^*&C
 \end{pmatrix}\succeq0,
 \qquad A\in M_2(\mathbb C),\quad C>0,
\tag{18}
\]

其中 prime physical vector为 `e=(1,1)^T`。因此

\[
 P=e^*Ae,\qquad z=e^*b.
\tag{19}
\]

### 定理 242-D（two-defect physical Schur identity）[T]

有 exact nonnegative decomposition

\[
 \boxed{
 E=
 e^*\left(A-\frac{bb^*}{C}\right)e
 +C\left|1+\frac{b^*e}{C}\right|^2.}
\tag{20}
\]

第一项是 physical prime vector对 continuum span 的 shorted residual，第二项是
actual continuum coefficient `1` 相对最优系数

\[
 \alpha_{\rm opt}=-\frac{b^*e}{C}
\tag{21}
\]

的 mismatch。两项都不依 Type-I/II cutoff。

#### 证明

`G>=0,C>0` 给 Schur complement

\[
 A-bb^*/C\succeq0.
\]

展开式 (20) 的第二项；`|b^*e|^2/C` 与第一项中被减去的同项抵消，余下
`e^*Ae+C+2 Re(e^*b)=E`。`square`

式 (20) 不单独解决 uniform bound，因为两项之和正是 `E`。它的非循环用途是把
算术任务分成两个 provenance不同的 inputs：continuum projection后的 prime
residual，以及 actual coefficient mismatch。只重新命名这两项不算进展。

### 障碍推论 242-E（one Schur defect is insufficient）[N]

仅控制式 (20) 的任一项，不能统一控制另一项：

1. 取 `u_p=-u_c+v`、`v perp u_c`，则 mismatch为零而 shorted residual为
   `||v||^2`，可任意大；
2. 取 `u_p=alpha u_c`，则 shorted residual为零，而 mismatch为
   `C|1+alpha|^2`，可任意大。

所以成功证明必须同时追踪 projection residual与 actual coefficient，而不能把
Schur minimizer当成 physical continuum coefficient。

### 定理 242-F（intrinsic gain = coherence times balance）[T]

假设 `Re z<=0`，定义

\[
 \rho_{p,c}=-\frac{\Re z}{\sqrt{PC}},
 \qquad
 \beta_{p,c}=\frac{2\sqrt{PC}}{P+C}.
\tag{22}
\]

则

\[
 0\le\rho_{p,c}\le1,
 \qquad 0<\beta_{p,c}\le1,
\tag{23}
\]

且 exact physical improvement为

\[
 \boxed{
 \frac{E}{P+C}=1-\rho_{p,c}\beta_{p,c}.}
\tag{24}
\]

因此后文 uniform `delta` 目标等价于
`rho_(p,c) beta_(p,c)>=2delta`。成功需要同时排除两个失败机制：prime 与
continuum 角度趋于正交，或两者能量高度失衡。

#### 证明

Cauchy--Schwarz给 `-Re z<=|z|<=sqrt(PC)`，AM--GM给
`2sqrt(PC)<=P+C`。再把 `2 Re z/(P+C)=-rho_(p,c)beta_(p,c)` 代入式
(14)。`square`

## 7. 修正后的 finite evidence [E]

`scripts/vaughan_brownian_schur_audit.py` 对旧 square-root cutoff逐点验证
Type-II为零；随后使用式 (8) 重算真实三通道 Gram。`prime-cross` 是
`2 Re G_(I,II)` 除以两个 prime diagonals之和；`pcross` 是
`2 Re <u_p,u_c>` 除以 `P+C`。

| scale, `N` | `U=V` | II energy / prime diagonal | Type-I/II cross / prime diagonal | prime--continuum cross / `(P+C)` | shorted / `E` | mismatch / `E` | `alpha_opt` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4, 7 | 1 | 0.013 | -0.209 | -0.702 | 0.976 | 0.024 | 1.154 |
| 8, 10 | 2 | 0.004 | -0.120 | -0.539 | 0.868 | 0.132 | 1.601 |
| 12, 12 | 2 | 0.005 | -0.125 | -0.486 | 0.856 | 0.144 | 1.725 |
| 16, 15 | 2 | 0.005 | -0.130 | -0.596 | 0.734 | 0.266 | 1.808 |

Type-II norm虽小，但其 negative Type-I cross接近 Cauchy允许的尺度；这是真实
非空 channel evidence；对应 coherence 为 `-0.91` 到 `-0.94`。总体 physical
gain仍主要来自 prime--continuum cross。
physical prime--continuum coherence 为 `-0.70` 到 `-0.80`，能量 balance 为
`0.70` 到 `0.92`；两者乘积精确复原表中的 relative cross gain。
continuum mismatch占最终能量的比例从 `2.4%` 增至 `26.6%`，所以不能以
`alpha_opt approximately 1` 作为未经证明的渐近假设。

旧 square-root-cutoff 表中的 physical `E` 保持正确，因为 `I+II=Lambda`；其
三通道 diagonal/full ratio则只是 vacuous split的数值，不应继续引用为
Type-I/II evidence。

## 8. 下一最小引理 B1a [O]

固定一个真正非空的 Vaughan rectangle，并先合并 physical prime vector
`u_p=u_I+u_II`。证明存在 independent、scale-uniform `delta>0` 使

\[
 \boxed{
 \Re\langle u_p,u_c\rangle
 \le-\delta\bigl(\|u_p\|_2^2+\|u_c\|_2^2\bigr).}
\tag{25}
\]

则由式 (14)

\[
 E\le(1-2\delta)(P+C),
\tag{26}
\]

这是相对于 cutoff-invariant physical two-channel diagonal的 genuine
response-specific improvement。式 (25) 目前为 [O]；有限表只显示
`2 Re z/(P+C)=-0.49` 到 `-0.70`，不能升级为 uniform theorem。按定理
242-F，也可分别证明 `rho_(p,c)>=rho_0>0` 与 `beta_(p,c)>=beta_0>0`。

证明式 (25) 时允许在 `u_p` 内使用 corrected Type-I/II decomposition，但必须：

1. 保留 `z=<u_I+u_II,u_c>` 的共同符号；
2. 不分别 majorize `|<u_I,u_c>|+|<u_II,u_c>|`；
3. 不使用 arbitrary-vector Bessel bound；
4. 明确写出 continuum quadrature/Gamma项与 prime coefficients 的共同 multiplier。

若式 (25) 在更大 finite scales发生符号翻转或最优 `delta` 趋零，则立即停止
uniform-factor目标，改攻式 (20) 两项的 absolute/summable bounds。

## 9. 最小公理、删除审计与循环性

本轮 [T]/[N] 只用：

1. exact Vaughan convolution (3)；
2. common linear divided-difference response map (9)；
3. linear Brownian primitive；
4. Gram positivity；
5. finite-dimensional Schur completion。

删除审计：

- 删除 support truncations `r>U,v>V`，242-A失效；
- 删除 common multiplier/linearity，不同 channels不能先合并成 `u_p`；
- 把 continuum coefficient自由优化，会删除式 (20) 的 mismatch并改变 physical
  problem；
- 使用三通道 diagonal作为 invariant，被 242-C反驳；
- 只控制一个 Schur defect，被 242-E反驳。

非同义反复审计：242-A纠正一个实际 vacuous experiment；242-B--C识别正确
quotient并排除 decomposition-dependent target；242-D给 exact audit identity。
只有式 (25) 是新 arithmetic input，明确标为 [O]。

循环性审计：全部 [T]/[N] 来自 finite convolution、线性响应、Hilbert Gram 与
Schur algebra；不调用 RH/GRH、Weil positivity、谱酉性、Mertens 的 RH 等价界或
bounded negative index。式 (25) 必须从 prime/continuum arithmetic独立证明。

## 10. 模型范围与 Weil 接口

- **Riemann zeta**：242-A直接修正 finite Vaughan audit；242-B--D给 actual
  prime/continuum response的 cutoff-invariant接口。
- **primitive Dirichlet L**：support floor保留；`z` 变 complex且式 (25) 必须控制
  real part，不能假定角色相位有利。
- **Dedekind/automorphic L**：只有在建立相应 coefficient convolution与 continuum
  term后才可引用 quotient invariance。
- **函数域**：support floor与 linear quotient保留；degree lattice可能改变 continuum
  channel及 correlation sign。
- **一般谱模型**：242-B--E适用于任何共同 linear response multiplier的 channel
  decomposition；242-A需要 Vaughan型卷积。
- **上同调型 Weil 结构**：本文仍在显式公式/Hilbert Gram侧；没有从 Schur
  correlation构造 polarization、Frobenius 或 Hard Lefschetz。

本轮把 NCE-8 的 finite evidence从 vacuous Type-II解释中纠正出来，并把 B1 从
decomposition-dependent `diagonal/full` 比严格替换为 cutoff-invariant physical
prime--continuum correlation (25)。

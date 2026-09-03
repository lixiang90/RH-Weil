# 239. Vaughan quotient-first centering 与 Möbius divisor response kernel

日期：2026-09-03

分支：MOM-1 / 路线 A1t；接口：fixed-power physical Type-I/II response /
exact dyadic band centering

状态：one-factor Vaughan entries 的 explicit divisor-range expansion、channel
measure quotient、positive mass main-term no-go 与 quotient-first linear
centering 为 [T]/[N]；flat-window mass/response channel ratios 为 [E]；
centered Möbius-divisor physical bilinear bound 为 [O]。本笔记不更新 PDF，
不改变零点比例的 [C] 状态。

## 1. A1s 的问题与答案

笔记 238-G 把 numerator factor 作 exact one-factor Vaughan split，

\[
 \Lambda=I+II,
\tag{1}
\]

并把 actual six-window response 写成固定 physical vector
$e=(1,1)$ 上的 $2\times2$ Gram quadratic form。A1s 问：

> 三个 channel entries 的 leading smooth/mass terms 是否先在
> $\Delta_{I,I}+2\Delta_{I,II}+\Delta_{II,II}$ 中代数相消？

本轮答案是：

1. channel labels 本身不会把 raw mass 主项消成零；它们精确重构 original
   positive physical mass；
2. 无条件小量来自先合并到 physical quotient，再使用 exact Gabor band 对每个
   constant-density shell 的 $O(R^{-1})$ cancellation；
3. 对 signed channel masses分别取 absolute majorants会破坏这个 commuting
   structure，并受笔记 238-H 的 ghost-gauge inflation影响；
4. Vaughan split 的真正新接口是共同 centering 后的 Möbius divisor kernel，
   且只能估计 actual Möbius/physical vector，不能估计 full operator norm。

## 2. High-cell canonical coefficients

固定 balanced factor scale

\[
 a,b,c,d\asymp Y=X^{3/4},
\qquad
 U=V=Y^\kappa,\qquad 0<\kappa<1.
\tag{2}
\]

充分大 $X$ 时 $V<cY$，故在 numerator cell 内
$\Lambda_{\le V}(a)=0$。笔记 238-(35)--(37) 因而简化为

\[
 I(a)=P_U(a),\qquad II(a)=Q_U(a),
\tag{3}
\]

其中

\[
 \begin{aligned}
 P_U(a)
 &=
 \sum_{\substack{r\le U,\ v>V,\ w\ge1\\rvw=a}}
 \mu(r)\Lambda(v),\\
 Q_U(a)
 &=
 \sum_{\substack{r>U,\ v>V,\ w\ge1\\rvw=a}}
 \mu(r)\Lambda(v).
 \end{aligned}
\tag{4}
\]

### 命题 239-A（high-cell divisor split）[T]

对 cell 中每个整数 $a$，

\[
 \boxed{\Lambda(a)=P_U(a)+Q_U(a).}
\tag{5}
\]

特别地，若 $\Lambda(a)=0$，则 $P_U(a)=-Q_U(a)$；这些是笔记 238 的
composite ghost coefficients。

#### 证明

由

\[
 I=(\mu_{\le U}*1)*\Lambda_{>V}+\Lambda_{\le V},
\qquad
 II=(\mu-\mu_{\le U})*\Lambda_{>V}*1,
\]

分别展开 Dirichlet convolutions即得式 (4)。cell 中低项
$\Lambda_{\le V}$ 为零，再用笔记 238-(37)。$\square$

## 3. Explicit divisor-range determinant forms

固定一个 channel-independent integer-pair mask
$m_{\mathcal C}(a,b)$，以及 exact six-window weight
$W_{a,b;c,d}$。对任意实系数列 $f,g$ 定义 normalized off-diagonal
response bilinear form

\[
 \begin{aligned}
 {\mathfrak R}_X[f,g]
 :=
 \sum_{\substack{a,b,c,d\\(a,b)\ne(c,d)}}
 &m_{\mathcal C}(a,b)m_{\mathcal C}(c,d)
 \frac{f(a)\Lambda(b)g(c)\Lambda(d)}
 {(4\pi^2)^2\sqrt{abcd}}\\
 &\times W_{a,b;c,d}
 K_{Q,D}\left(X\log\frac{ad}{bc}\right).
 \end{aligned}
\tag{6}
\]

把 kernel 删除得到 raw mass bilinear form

\[
 {\mathfrak M}_X[f,g]
 :=
 {\mathfrak R}_X[f,g]\big|_{K_{Q,D}=1}.
\tag{7}
\]

令 $\mathcal R_I=\{r:r\le U\}$、
$\mathcal R_{II}=\{r:r>U\}$。对
$\alpha,\beta\in\{I,II\}$，式 (4) 给
$C_I=P_U,C_{II}=Q_U$，并且

\[
 \boxed{
 \begin{aligned}
 \Delta_{\alpha,\beta}
 =
 \sum_{\substack{
 r\in\mathcal R_\alpha,\ r'\in\mathcal R_\beta\\
 v,v'>V,\ w,w'\ge1\\
 a=rvw,\ c=r'v'w'}}
 &\mu(r)\mu(r')\Lambda(v)\Lambda(v')\\
 {}\times
 \sum_{\substack{b,d\\(a,b)\ne(c,d)}}
 &m_{\mathcal C}(a,b)m_{\mathcal C}(c,d)
 \frac{\Lambda(b)\Lambda(d)}
 {(4\pi^2)^2\sqrt{abcd}}\\
 &\times W_{a,b;c,d}
 K_{Q,D}\left(X\log\frac{ad}{bc}\right),
 \end{aligned}}
\tag{8}
\]

raw mass entry
$M_{\alpha,\beta}$ 由式 (8) 把 $K_{Q,D}$ 换成 $1$ 得到。

### 定理 239-B（explicit one-factor divisor-range response）[T]

\[
 \Delta_{\alpha,\beta}
 =
 {\mathfrak R}_X[C_\alpha,C_\beta],
\qquad
 M_{\alpha,\beta}
 =
 {\mathfrak M}_X[C_\alpha,C_\beta],
\tag{9}
\]

且式 (8) 是这两个 entries 的 exact divisor-range expansion。它保留
Möbius signs、两个 high von Mangoldt variables、denominator prime factors、
six-window overlap、determinant equation与 exact finite Gabor kernel。

#### 证明

把命题 239-A 的式 (4) 分别代入式 (6)--(7)，有限求和可逐项交换。$\square$

这完成 A1s 要求的 exact divisor-range formula；没有调用 asymptotic
prime correlation。

## 4. Physical quotient 精确重构正质量

令

\[
 e=(1,1),\qquad
 \Delta=(\Delta_{\alpha,\beta})_{\alpha,\beta},
\qquad
 M^{\rm ch}=(M_{\alpha,\beta})_{\alpha,\beta}.
\tag{10}
\]

### 定理 239-C（response and mass quotient identities）[T]

\[
 \boxed{
 e\Delta e^*
 =
 {\mathfrak R}_X[\Lambda,\Lambda],}
\tag{11}
\]

以及

\[
 \boxed{
 eM^{\rm ch}e^*
 =
 {\mathfrak M}_X[\Lambda,\Lambda]\ge0.}
\tag{12}
\]

只要 cell 中存在一个 distinct overlapping off-diagonal prime-power pair，
式 (12) 严格为正。

#### 证明

式 (6)--(7) 对 $f,g$ 双线性。由式 (5)，

\[
 \sum_{\alpha,\beta}{\mathfrak R}_X[\alpha,\beta]
 =
 {\mathfrak R}_X[P_U+Q_U,P_U+Q_U]
 =
 {\mathfrak R}_X[\Lambda,\Lambda],
\]

mass form 同理。对 $f=g=\Lambda$，式 (7) 的每个 summand 是

\[
 m_{\mathcal C}(a,b)m_{\mathcal C}(c,d)
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}
 {(4\pi^2)^2\sqrt{abcd}}W_{a,b;c,d}\ge0.
\]

若至少一个 admissible overlap 为正，严格正性成立。$\square$

### 障碍推论 239-D（channel mass main term不代数消失）[N]

在任何非空 actual positive cell 中，

\[
 M_{I,I}+2\Re M_{I,II}+M_{II,II}=0
\tag{13}
\]

为假。左边恰为严格正的 physical mass。

因此不能把笔记 238 中有限的 response-entry cancellation解释成 Vaughan
labels 自动删除 leading positive mass。它必须来自 exact band kernel、实际
phases 或更细的 joint arithmetic cancellation。

## 5. Quotient-first linear centering

在笔记 235 的一个 central/dyadic interval $J$ 上，对任意 finite signed
measure $\sigma$ 定义 constant-density projection

\[
 {\mathsf P}_J\sigma
 =
 \frac{\sigma(J)}{|J|}{\bf1}_J(t)\,dt,
\qquad
 {\mathsf E}_J=1-{\mathsf P}_J.
\tag{14}
\]

两个 operators 对 signed measures 都是线性的。令
$\mu_{\alpha,\beta}$ 是式 (8) 的 signed channel response measure；由
定理 239-C，

这里先对每个 channel使用同一个线性 even symmetrization
$\sigma\mapsto(\sigma+\iota_*\sigma)/2$，再限制到正半轴的共同
central/dyadic shells；这与 channel求和交换。

\[
 \mu_{\rm phys}
 =
 \sum_{\alpha,\beta}\mu_{\alpha,\beta}
\tag{15}
\]

是 original positive response measure。

### 定理 239-E（centering commutes with the physical quotient）[T]

对每个 shell $J$，

\[
 \boxed{
 \sum_{\alpha,\beta}{\mathsf P}_J\mu_{\alpha,\beta}
 =
 {\mathsf P}_J\mu_{\rm phys},}
\tag{16}
\]

且

\[
 \boxed{
 \sum_{\alpha,\beta}{\mathsf E}_J\mu_{\alpha,\beta}
 =
 {\mathsf E}_J\mu_{\rm phys}.}
\tag{17}
\]

因此

\[
 \begin{aligned}
 \int K\,d\mu_{\rm phys}
 ={}&
 \sum_J\int K\,d({\mathsf P}_J\mu_{\rm phys})\\
 &+
 \sum_J\int K\,d({\mathsf E}_J\mu_{\rm phys}),
 \end{aligned}
\tag{18}
\]

其中第一行可以在合并 channels 后直接调用笔记 235-G 与 236-C。

#### 证明

式 (16)--(17)只用式 (15)与 $\mathsf P_J,\mathsf E_J$ 的线性性；
式 (18)再对 shells求和。$\square$

### 推论 239-F（共同 smooth main term 已闭合）[T]

在 balanced cell、笔记 236 的尺度

\[
 M=\max(H,Y/H)
\tag{19}
\]

上，式 (18) 第一行的全部 physical constant-density terms满足

\[
 \boxed{
 \sum_J
 \left|
 \int K_{Q,D}\,d({\mathsf P}_J\mu_{\rm phys})
 \right|
 \ll L=o(L^4).}
\tag{20}
\]

#### 证明

对 central block 与 dyadic shells，笔记 235-G 分别给
$O(b_0/M^2)$ 与 $O(b_j/R_j^2)$。笔记 236-C 已证明这些 physical positive
mass terms 总计 $O(L)$。$\square$

所以 A1s 中的 leading common density main term不需要新的 Type-I/II
cancellation；它已经由 exact band geometry与 elementary positive incidence
无条件闭合。

## 6. 为什么 channelwise absolute centering 失效

线性 identities (16)--(17) 不允许随后对每个 channel独立取绝对值并期待仍保留
physical cancellation。定义 nonlinear budget

\[
 {\mathcal A}((\sigma_{\alpha,\beta}))
 =
 \sum_{\alpha,\beta}
 \left|\int K\,d\sigma_{\alpha,\beta}\right|.
\tag{21}
\]

### 障碍命题 239-G（absolute channel budget is gauge-dependent）[N]

仅固定 physical sum

\[
 \sum_{\alpha,\beta}\sigma_{\alpha,\beta}
 =
 \sigma_{\rm phys}
\tag{22}
\]

不能控制式 (21)。即使 $\sigma_{\rm phys}=0$，式 (21) 仍可任意大。

#### 证明

取任意 signed measure $\eta$ 使
$\int K\,d\eta\ne0$，并把两个 channel measures替换为

\[
 \sigma_1'=R\eta,\qquad \sigma_2'=-R\eta.
\]

它们的 physical sum 恒为零，而式 (21) 等于
$2R|\int K\,d\eta|$，随 $R$ 任意增长。$\square$

这是笔记 238-H ghost-gauge no-go 的 measure版本。它不否定对 fixed
convolution channels证明某个 joint estimate；它只排除从 physical response
反推 channelwise absolute budgets，或把这些 budgets冒充 intrinsic Weil
structure。

## 7. Finite mass-versus-response evidence [E]

脚本 `scripts/power_high_physical_vaughan_channel_audit.py` 同时计算：

1. exact Gabor response matrix $\Delta$；
2. 把 kernel 替换为 $1$ 的 mass matrix $M^{\rm ch}$；
3. 两者在 physical vector上的 direct reconstruction。

代表性 ratios如下：

| $X$ | $\kappa$ | response/entry-$\ell^1$ | mass/entry-$\ell^1$ |
|---:|---:|---:|---:|
| 800 | $1/4$ | 0.2633 | 0.3232 |
| 1,600 | $1/4$ | 0.0772 | 0.2475 |
| 3,200 | $1/4$ | 0.0169 | 0.8646 |
| 6,400 | $1/4$ | 0.0665 | 0.9424 |
| 3,200 | $1/3$ | 0.0351 | 0.9506 |
| 6,400 | $1/3$ | 0.1194 | 0.9599 |
| 3,200 | $1/2$ | 0.4578 | 0.9993 |
| 6,400 | $1/2$ | 0.9304 | 0.8802 |

较大 $X$ 时 raw mass 通常几乎没有 channel cancellation，而 exact response
可能小一个数量级以上。这与定理 239-D--F 一致：saving 属于 band-projected
physical direction，不属于 bare mass labels。数据不证明渐近。

## 8. Möbius divisor kernel 与下一最小引理 239-H [O]

由式 (8) 把除 $r,r'$ 外的变量全部求和，定义 common-centered kernel

\[
 {\mathcal K}_X(r,r')
 =
 \sum_{\substack{v,v'>V,\ w,w'\ge1\\
                  a=rvw,\ c=r'v'w'}}
 \Lambda(v)\Lambda(v')
 \sum_{b,d}
 {\mathcal W}^{\,\rm cent}_{a,b;c,d},
\tag{23}
\]

其中 $\mathcal W^{\rm cent}$ 明确表示：

1. fixed integer-pair masks；
2. $(4\pi^2)^{-2}(abcd)^{-1/2}$；
3. exact six-window overlap；
4. exact finite Gabor kernel；
5. 定理 239-E 后共同 constant-density projection 已删除的 remainder。

于是剩余 physical response精确为

\[
 \boxed{
 \sum_{r,r'\ge1}
 \mu(r)\mu(r'){\mathcal K}_X(r,r').}
\tag{24}
\]

下一最小引理是：固定 $\kappa=1/4$，从式 (23) 写出
$\mathcal W^{\rm cent}$ 的 central-plus-dyadic finite formula，并证明一个只对
actual Möbius vector成立的 bilinear estimate

\[
 \boxed{
 \left|
 \sum_{r,r'}\mu(r)\mu(r'){\mathcal K}_X(r,r')
 \right|
 =
 o(L^4).}
\tag{25}
\]

式 (25) 仍是 [O]，但其独立算术内容已明确：

- variables $r,r'$ 是 Vaughan Möbius divisors；
- $v,v'$ 是 $>Y^{1/4}$ 的 prime-power variables；
- $w,w'$ 是 completion variables；
- $b,d$ 保持 actual von Mangoldt weights；
- centering 是 physical quotient后的共同线性 centering；
- 只估计 vector $\mu\otimes\mu$，不要求
  $\|\mathcal K_X\|_{\rm op}$ 或 arbitrary coefficients。

要避免同义反复，下一轮必须进一步把式 (25) 的 proof拆成一个可引用的
Möbius bilinear/dispersion inequality；只把原 response换名为
$\mu^*\mathcal K_X\mu$ 不足以晋级。

止损条件：

- 若共同 centering 后 $\mathcal K_X$ 仍含一个不小的 rank-one physical mode，
  且有限数据不随 $X$ 下降，则停止该 cutoff；
- 若任何可用估计都先取 $|\mu(r)\mu(r')|$ 或 full operator norm，则由
  命题 239-G / 238-H 停止；
- 若能用 Cauchy--Schwarz、dispersion与已知 Möbius mean-square把
  $\mu\otimes\mu$ direction压到 $o(L^4)$，才晋级四矩比例链。

## 9. 最小公理、删除审计与循环性

本轮 [T]/[N] 结果使用：

1. **共同 linear synthesis**：保证式 (5)、(11)--(12)；
2. **fixed off-support mask**：防止 ghost features随目标改变；
3. **positive original coefficients**：给 physical mass 的式 (12)；
4. **linear shell centering**：给 commuting identities (16)--(17)；
5. **exact consecutive band cancellation**：给式 (20)；
6. **balanced elementary incidence**：把 physical mass ledger压到 $O(L)$。

删除审计：

- 删除共同 synthesis，channel entries不再重构 actual response；
- 删除 positivity，式 (12) 可能有符号，239-D 的严格正 no-go失效；
- 在 quotient 前取 absolute values，式 (16)--(17) 不再提供预算；
- 删除 exact band，positive mass本身不会变小；
- 删除 incidence，只知道 shell integral小，仍不能控制 mass coefficient；
- 用 full Gram/operator norm替代 actual Möbius vector会触发 ghost-gauge
  inflation。

非同义反复审计：式 (8) 给出全部 divisor ranges；式 (12) 用 actual positive
mass证明 leading channel cancellation不可能；式 (20) 调用独立已证 band 与
incidence定理。只有式 (25) 是剩余目标，并明确禁止把 kernel notation本身当成
进展。

循环性审计：全部 [T]/[N] 结论只用 finite Dirichlet convolution、bilinearity、
positive weights、linear projections、exact Gabor shell cancellation与笔记
236 的 elementary interval count；不调用 RH/GRH、Hardy--Littlewood、
Weil positivity、谱酉性或 bounded negative index。

## 10. 模型范围与 Weil 接口

- **Riemann zeta**：式 (8)、(23)--(25) 是 fixed-power four-von-Mangoldt
  response 的直接 arithmetic interface。
- **primitive Dirichlet L**：角色相位破坏 physical mass positivity；式
  (11) 与 linear centering仍成立，但 239-D--F 须改成 signed版本。
- **Dedekind/automorphic L**：需要可用的 coefficient convolution identity；
  不得默认 Ramanujan或 unitary Satake parameters。
- **函数域**：degree lattice可能 alias exact band，式 (20)须重新证明。
- **一般谱 zeta模型**：quotient-first linear centering适用于任意 fixed trace
  direction；positive mass no-go要求 underlying response measure为正。
- **上同调型 Weil 结构**：本文仍只位于 explicit-formula/Hilbert Gram侧；
  没有把 Möbius divisor kernel解释为 Frobenius、极化或 Hard Lefschetz。

本轮把 A1s 的“leading main-term cancellation”问题严格解决为：channel mass
不消失，physical constant-density response却已无条件闭合。唯一应继续估计的
是共同 centering 后 actual Möbius divisor direction (25)。

## 11. 后续 pullback 审计（笔记 240）

笔记 240 已证明式 (23)--(24) 精确因子化为

\[
 {\mathcal K}_X=T_X^*B_X^{\rm cent}T_X,
 \qquad T_X\mu=\Lambda.
\]

因此只把 response 改写成 `mu^*K_Xmu` 并不构成新 arithmetic saving；这正是
本节已警告的同义反复风险。二维 Abel 后的真实新对象是相邻 divisor columns
`U_r=T_r-T_(r+1)`，而这些 columns 由 divisibility 造成跳跃、没有形式 smoothness。
逐 entry absolute variation 的有限 retention 从 `1.65e-2` 降到 `5.51e-4`，故该
路线降级为 [E]。A1t 的下一输入已改成保留 dyadic blocks 内全部 signs 的
adjacent-divisor response mean-square；详见笔记 240-(28)--(29)。

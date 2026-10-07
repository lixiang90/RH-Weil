# 原六次幂自由行的 primitive-zero raw 密度：独立全文审查

2026-10-08。结论：限定 PASS。独立实读最终源全部 407 行，回读原
paper.tex 的 presentation、实际零点 bins、sextic sieve 和 powerful
row decomposition，并浏览一手 BGL §2/§5。未发现阻断。
这是相对明确原 [R] 的新 raw 行数推导，不是新无零边界或比例认证。

## 1. 最终来源与审查范围

| 文件 | canonical LF SHA-256 | canonical bytes /行 |
|---|---|---:|
| [被审完整源](hybrid-original-sextic-primitive-zero-density-research-compression.md) | 74ea809c6aef75638dc2bc115af2b592ff4feb999cd15e35adcfa4319235d52b | 20750 /407 |
| [450](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 | 5431 /122 |
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 | 10207 /244 |

canonical 只统一 CRLF/lone CR→LF，不 trim 或改变 EOF。
原只读来源为
[paper.tex](E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
固定 canonical SHA 为
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
本次实读 4195–4340、原 4707–4724 sieve 前件及 5181–5445
原 raw count，保留原固定算术数据和 primitive/natural 区别。

外部一手 [BGL 原文](https://arxiv.org/pdf/1112.1650) 的 Corollary 1.6
只在 squarefree primitive rows 上给 density；本文没有直接套用它。
被审稿重新证明的是每行至少有一枚零点的行数上界，不是全部零点
重数的总和。上游 sextic squarefree sieve、标准 primitive Hecke AFE、
固定域理想计数与原 primitive growth/logarithmic control 仍为 [R]。

## 2. 行族、自然零点和冻结导子

原 $\psi_{u,\nu,\varsigma}$ 的正实部零点与 primitive inducing
$L$ 一致：deleted Euler factors 的零点实部为零。原 buffered
$a>51/100$ bin 已有真正的 primitive 零点，才可转入本文计数；
不是从 inverse 大值推断零点。floor 无 witness，独立 count 保留。

原 sixth-power-free 理想分解 $(u)=\mathfrak s\mathfrak w\mathfrak k$
唯一；固定 $\mathfrak s$、单位、presentation labels 和 $\mathfrak w$
后，$\mathfrak k$ 是 outside-$S$ 的 squarefree 部分，
$(\mathfrak k,\mathfrak w)=1$ 是固定 row restriction。
源中的 factorization 保留全部零值。$\#\mathfrak w\ll V^{1/2}$、
$R_w=N\operatorname{rad}(\mathfrak w)\le V^{1/2}$，并非把 radical
误当 $V$；两者均在后续指数中计回。

在 $p\notin S$，$v_p(u)=j\in\{1,\ldots,5\}$ 的局部阶
$6/\gcd(6,j)>1$，固定 $\nu$ 未分歧，故不能取消。该非平凡有限阶
tame 局部角色的 conductor exponent 为一。fixed-$S$ local types
有限，所以 $Q_\psi=C_{\mathcal A,\mathrm{class}}q_kR_w$ 一致成立。
真正需要分层的是这些 local/infinity types，root numbers 只需逐行
模长一；最终正文已经明确不把其值误称为有限种。

在 $S$ 外 primitive 与自然系数一致。额外未分歧 deletions 仅在固定
$S$；临界线的 finite-product upper 一致。primitive-label 的有限
multiplicity 说明也正确，但此稿实际按原行求和，不依赖这项说明
把行族换成 BGL 的 squarefree 族。

## 3. 全列扩展和 AFE 的实际准入

$n=cd^2$ 按估值奇偶唯一分解，$c$ squarefree，$c,d$ 可以共享素理想。
固定 $d$ 后，$\psi(d^2)$ 是模长至多一的 row factor；它的零值
准确给固定 $(k,d)=1$ 限制。其余 $\nu(c)\chi_c(v)^\varsigma$
是先于 $k$-sum 固定的列系数。没有把一个尚未固定的 $d$ 相位塞进
任意 row-dependent coefficient。

独核 Minkowski 的三项平方根：

\[
 \frac{\sqrt{MB}}{q_d},\quad
 \frac{B}{q_d^2},\quad
 \frac{M^{1/3}B^{5/6}}{q_d^{5/3}};
\]

临界权时则为

\[
 \frac{\sqrt M}{q_d},\quad
 \frac{\sqrt B}{q_d^2},\quad
 \frac{(MB)^{1/3}}{q_d^{5/3}}.
\]

固定域理想计数使第一项只损失 $\log B$，其他两项收敛。
由此 (6)/(7) 的每个 $M,B$ 幂均正确，dyadic/prefix 支撑可固定后
再用 sieve。

AFE 的真实导子给长度 $(MR_w)^{1/2}(1+H)^{d_F/2}$。
Mellin 后 $q_k^{\epsilon/2}$ 在 dyad 付任意小幂，
$q_k^{iz/2}$ 是整列的模一 row factor；先提出再在固定 Mellin 参数
使用正 mean bound。dual root number 也先逐行提出，dual coefficients
使用原 conjugate orientation。$S$-supported 列的 Minkowski 几何和
一致收敛，不扩大 $S$ 随 $w$ 变化。

三项完整 conductor accounting 得

\[
 \mathcal L_w=M+(MR_w)^{1/2}+MR_w^{1/3},
\]

其中最后一项来自 $(MB)^{2/3}$，没有漏一个 $M$ 幂。
统一高度指数 $d_F/2$ 足够，真实权的 gamma/Mellin 费用相对
标准 AFE 明确列为 [R]；审查没有另作 kernel 认证。

## 4. Auxiliary detector 与全高度常数

$L_{\rm orig}M_X$ 在右半平面有同一个零延拓角色的 Dirichlet 系数
$c_n=\sum_{d\mid n,q_d\le X}\mu(d)$，$c_1=1$，$1<q_n\le X$
时为零。Gamma integral 移至 $\Re z=1/2-\beta$，未跨负整数
Gamma poles；$\beta=1$ 时线恰为 $-1/2$，也未跨负整数 pole。
$z=0$ residue 由真实零点消失，nonprincipal 无 $L$ pole。
因此临界线积分或长 dyadic polynomial 至少一项有固定下界。

初稿的两处需补明事项在最终源均已处理：root number 不要求有限值；
critical 项直接在全实线上用
$e^{-c\operatorname{dist}(t,[-H,H])}
(1+\operatorname{dist}(t,[-H,H]))^C$ 共同 majorant。
(9) 对每个实 $t$ 取 $H'=1+|t|$，(10) 的 LS bound 对全实线
一致；Gamma 加权积分准确付 $H(1+H)^{d_F/4+\epsilon}$。
这在固定 $H=1$ 时也完整支付，未将固定 $CH$ 外的尾假设为
$U^{-A}$，不依赖实际 $H=Z^\tau$ 最终压过 $\log U$。

逐行 $\gamma$ 的 supremum 用一维 Sobolev；导数仅插入 $\log q_n$，
partial maxima 用 binary fixed-support intervals，所有列系数先于
$k$-sum 固定。它未借用任意 row-selected 系数的 LS。
指数 (12) 的五项与这两种 detector contribution 一致，
$q_n>Y^{1+\epsilon}$ 的 exponential tail 允许预先固定大阶。
统一高度

\[
 p(\sigma)=1+\frac{d_F(1-\sigma)}{3-2\sigma}
\]

准确匹配 Type I 和 $Y^{2-2\sigma}$；其他正 $Y$-cross 不更大。
常数在先固定的 $\sigma$ 范围、数据和 losses 下统一，才选原 $\tau$。

## 5. 计回全部 powerful 行与连续优化

$M=U^x,V=U^{1-x}$ 给

\[
 \ell(x)=\max\{x,(1+x)/4,(1+5x)/6\},
\]

断点恰为 $x=1/7$。完整 count 是
$\min\{(1+x)/2,(1-x)/2+E_\sigma\}$。
这包含 $V^{1/2}$ 个 powerful parts；其 cardinality alternative
也没有丢弃。实际 dyad 的 $O(1/\log U)$ offsets 在最终连续优化
才吸收，不改实际 annulus。

低 $\sigma$ 段独核：$x\le1/5$ 可直接用 cardinality；
$x\ge1/5$ 的 $h=x/2$、$y=(1+3x)/(12r)$ 满足
$h\le y\le2x$。Type I 与 $Y$-cross 相等，其他三项不超过它；
计回 $(1-x)/2$ 后的 affine 最大值在 $x=1$，即
$8(1-\sigma)/(7-6\sigma)$。

对 $\sigma=7/8$，独立 Sympy 有理计算逐项复核 (21) 表：
每段的 Type I、$X$-cross、$Y$-plain 相等，$X$-first 的余量分别为

\[
 (31x-4)/39,\qquad (15x-2)/13.
\]

第三段须再分 $x\le1/15$ 的 $h=0$ 与 $x\ge1/15$ 的
$h=x-1/15$；其两项余量准确为
$(1-15x)/20,(3-25x)/60$，或 $0,(2-15x)/45$。
全部是指定区间上的非负 affine functions。第三段低端确实用
cardinality，另两段的总指数也均不超过 $7/13$。
这是连续证书，有限点值不是其替代。

高段本次仅支付 $7/13$ 点值和

\[
 G_{\rm safe}(\sigma)=
 \min\{1,7/13+(56/13)(7/8-\sigma)_+\},
\]

未支付整个高段精确 BGL $g$。最大 $y=28/13$，
各分支的 $\sigma$ 灵敏度最多 $2y$，故该安全延伸正确。
在实际 $a\le7/8$ 的高区间，上界恰为 $56(1-a)/13$。

## 6. 最终包络 scope 与结论

实际 above-floor 应用仍须先有原 bin 的 primitive zero。
新 $X,Y$ 是辅助 count 长度，不是改变原 physical probe 的
witness 或 slot 长度。自然 masks、shared presentations 和原
buffered reciprocal control 的角色保持明确；density 本身
没有给逐行 $1/L$ bound。

最后的全域比较独核：
$2D-3P\ge0$ 给 $R_*\le(15-16\delta)/(15-6\delta)$。
低段新指数的差为
$\delta(25-24\delta)/[(4-3\delta)(15-6\delta)]>0$；
本次实际支付的高段 $G_{\rm safe}$ 的差为

\[
 \frac{225-380\delta+168\delta^2}{13(15-6\delta)}>0.
\]

分子在 $[2/3,3/4]$ 递减且不小于 $69/2$。
因此它改善旧 inverse-only raw count，却没有强于最终 actual
inverse/plain/amplification 包络。上述 actual count 比较仅用于
above-floor；闭 floor 端点仍只是代数延拓，源 §1 的独立 floor
count 未被替代。

限定 PASS 支持把这个完整 raw 行数推导相对 [R] 记录为新结果。
新的 marked/supscale joint moment、实际 boundary/proportion
改善、原 [R] 全包、外部整篇论文、Lean 和 RH 均没有由本审查认证。

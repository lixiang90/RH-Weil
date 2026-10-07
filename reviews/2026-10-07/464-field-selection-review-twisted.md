# 464 数域选择、净均方门槛与共轭障碍独立审查

2026-10-07。**限定 PASS。** 已全文独立核对 464 的五节、冻结的
457/458/460、原 source 的指定接口，以及 GL、BGL、DDHL v5 的相应原文。
没有发现需要修改 464 的数学阻断。本审查不是新的 Gaussian 无零定理，
也不重新认证原 [R] 的整篇证明核、Lean 或 RH。

## 1. 最终被审版本与范围

被审 [464](../../notes/464-field-selection-decision-and-conjugation-obstruction.md)
canonical UTF-8 SHA256：

c534076d26fbc9612ea67946b9ab8e247bd8b13acb2d4415ba60b52501f3ae2d

raw 9100 bytes，181 行。canonical 化只把 CRLF 与 lone CR 换为 LF，
不 strip/trim。以下输入均实际读取，未修改：

| 输入 | canonical SHA256 |
|---|---|
| [457](../../notes/457-number-field-choice-and-relative-amplification.md) | 75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791 |
| [458](../../notes/458-gaussian-all-row-large-sieve-comparison.md) | 3ee821601d6e1d5da38c8235586981b28d7ebee5a5f28691a98d869834dcc8ac |
| [460](../../notes/460-generic-power-row-obstruction-and-field-choice.md) | 9625c0d618854769de90edfb3ee3b8d8b89e1d3b2b83d676dffccb927e09d85f |
| [450](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 |
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| [数域定量审查](hybrid-number-field-quantitative-review-radial.md) | a0f644818b0988355fe6bd355c288697a5842bf4a3525caa287108c5e415a2ee |

原只读 source：
E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex，
canonical SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
行号均按这个固定源。

## 2. 原数域机制、角色阶数与次数

源 568–625 确实把 \(F=\mathbf Q(\sqrt{-3})\)、Euclidean/PID、
primary \(a\equiv1\bmod3\)、有限六单位和
\(\#\{\mathfrak a:N\mathfrak a\le H\}
=\pi H/(3\sqrt3)+O(\sqrt H+1)\) 分开陈述。
源 766–835 的 \(\gamma_2(p)^3=-\alpha(p)\) 用 cubic Jacobi sum 的
primary 单位归一化；不是所有虚二次域通用的 Gauss 公式。

源 1789–1793 给普通分支 \(\chi_p(x)^{-j_p-2}\)；源
7697–7702 的 actual residual primes 为 \(j=1\)。所以 sextic 幂
\(-1-2\equiv3\bmod6\) 是二次角色，源 2640–2672 另外核对 primitive
conductor、同 sector product 与 reciprocity，才调用二次大筛。
[GL Theorem 1.1 与 Corollary 1.2](https://arxiv.org/html/1112.1642v2)
确实要求 squarefree Hecke-family 前件，后者允许偶数阶 family 取
\(n/2\) 次幂；它不把一般高阶 row 直接变成二次 row。

464 的 single-shift 同余及 gcd 证明正确：
\[
 -1-\rho\equiv m\pmod{2m},\quad
 \rho\equiv m-1,\quad
 \gcd(2m,m-1)=\gcd(2,m-1).
\]
故非平凡 \(m\ge2\) 时最小 theta 阶数为 3，只在 \(d=6,m=3\)
达到；\(d=4\) 需要阶数 4。它仅限制该 retained-\(j=1\) 模板，
不排除别的探针设计。

\(\mu_d\subset K\) 蕴含 \([K:\mathbf Q]\ge\varphi(d)\)，但角色阶数
\(d\)、数域次数和有限单位数是不同变量。固定域按 ideal norm 计数
仍是一次幂；\(u\mapsto ua^d\) 的 \(1/d\) 来自
\(N(ua^d)=Nu(Na)^d\) 与注入，不是 ambient lattice 维数或单位除法。
高次 CM 的 \(\Gamma(s)^r\) 增加高度复杂度；普通 FE 的 conductor
指数仍为 \(1/2-s\)，见
[GL (3.1)–(3.2)](https://arxiv.org/html/1112.1642v2)。
单位 rank \(r-1\) 的行代表问题亦如 464 明确所述。

## 3. Gaussian 现有上界与 raw family

[BGL Theorem 1.3](https://arxiv.org/html/1112.1650v1) 的宽度是
\(A+D+(AD)^{2/3}\)，两端均为 squarefree ideals。
458 没有将其直接用于全部元素行，而是逐 valuation 分成
\(u=\zeta\lambda^vab^2c^3r^4\)，在四次方向与平方二次方向二选一。
其 \(U+(UD)^{2/3}+DU^{1/3}\) 全行界和固定 profile 的 scale-sup
推导保持全部自然零值；460 的 pure-power 行下界针对任意列系数
算子范数，不能当成固定 Möbius 列下界。464 保留了这一区分。

本轮重算当前 critical \(t_*\) 下：
\[
 e_{\rm LS}(t_*)=t_*+\tfrac13
 =1.457560480119417863\ldots ,
\]
\[
 e_{\rm LS}(t_*)-e_6(t_*)
 =0.354037857797680755\ldots .
\]
因为 \(t_*>1\)，三个 LS 幂中 \(t_*+1/3\) 严格最大。
464 的显示值正确。这只是现有 upper envelope 不够强，并非实际
Möbius cancellation 不可能。

[DDHL v5 (3.11) 与 §4.5](https://arxiv.org/html/2306.11875v5)
保留 \((-1/\pi)_4(\bar\pi/\pi)_4^{-2}\)；457 已处理它们，
取得真实 squarefree 平方信号。该文仍把 quartic prime core 的
完整系数公式列为开放 conjecture。平方 signal 与完整任意目标
twisted completion 是不同前件；464 未将两者混同。

## 4. 有限共轭反例与 whole-family 前件

独立以 Gaussian 整数和模 13 算术核对：
\[
 \pi=-1+2i,\quad \nu=3+2i,\quad\bar\nu=3-2i
\]
均满足 primary 条件，范数分别为 \(5,13,13\)，所以互素。
在 \(\mathcal O/(\nu)\) 中 \(i=5\)，\(\pi=9\)，\(9^3=1\bmod13\)；
在 \(\mathcal O/(\bar\nu)\) 中 \(i=8\)，\(\pi=2\)，
\(2^3=8=i\bmod13\)。于是
\[
 (\pi/\nu)_4=1,\qquad(\pi/\bar\nu)_4=i.
\]
共轭符号读成 \(1,-i\)，也不相等。二次模数与全部自然 zeros 均没有
被删去；选取支持使该有限例的 mask 确实为 1。

任何 \(\chi\circ N\) 在这两个同范数理想上必取相同值，故这个
actual quartic row 不是 norm base-change。更稳固的 primitive 解释
是其奇 conductor 单独含 \((\pi)\)，不含共轭 \((\bar\pi)\)；split
rational prime 上的 norm base-change conductor 必共轭不变。
固定 2-part ray 分拆或有限 Euler deletions 不会改变这个 primitive
odd-conductor 障碍。464 因而正确排除了从已有 Dirichlet 条带免费
取得整个变化 Gaussian 行族的无零输入。

实际 feedback 必须在同一个已准入 whole family 内取
\(\kappa_{\rm act}=2\beta_*-1\)。源 12561–12566 的 positive-slot
前件是 \(\beta_*\le(1+\kappa)/2\)，450 的扩展并没有删除它。
451 的 \(\kappa_*\) 是 reference certificate 参数；反证中只调用
\(\kappa_{\rm act}\)。Eisenstein [R] 的 whole-family bootstrap
不能自动当成所有 Gaussian Hecke 角色的 bootstrap。
464 的当前 \(\sigma_*\) 限于原 [R]；未注册新 Gaussian 条带。

## 5. 净 moment 门槛的准确补充

以下是 **原 short 合同全部保留时的条件预算**，不是另一个数域的
实际 theorem。设 \(e=e_*\) 为 451 的三次根，置
\[
 \delta_*=\frac{5-9e}{6+18e},\quad
 \kappa_*=\frac56-\frac e2,\quad
 t_*=\frac{1+3e}{8e},\quad
 s=\frac{\delta_*P}{D},\
 D=\frac52-\frac1{3\kappa_*},\
 P=1-\frac1{6\kappa_*}.
\]
源 15248–15275 的 unmarked moment 与 witness spike 相除，得到
long row exponent \(e_{\rm net}(t)-\delta_*t\)；原 short 是
\[
 S(t)=1-\delta_*+s(3/2-t),\qquad S(t_*)=2/3 .
\]
因此对一般净 moment 曲线，改善这个 critical count 的准确条件是
\[
 \exists\,t>t_*:\quad
 e_{\rm net}(t)<\frac23+\delta_*t
 \quad\hbox{且该 }t\hbox{ 与所有 widths/供槽同源准入}.
 \tag{1}
\]
不能把“在 \(t_*\) 只改善 long”叫作 whole-count saving。

若新 order-\(d\) 路线是理想 affine exponent 加固定额外净损失
\[
 e_{\rm net}(t)=1+\alpha_d(t-1)+\chi,\qquad
 \alpha_d=1-\frac1d,\quad \chi\ge0 ,
\]
则在当前 \(\delta_*<1/2\) 的点，重选 cutoff 的严格门槛恰为
\[
 \boxed{\chi<(\alpha_6-\alpha_d)(t_*-1).}                 \tag{2}
\]
证明：两支交点为
\[
 t_{d,\chi}=1+\frac{s/2-\chi}{\alpha_d-\delta_*+s},
\quad
 R_6-R_{d,\chi}
 =\frac{s}{\alpha_d-\delta_*+s}
 [(\alpha_6-\alpha_d)(t_*-1)-\chi].
 \tag{3}
\]
在 (2) 下交点合法且 \(t_{d,\chi}>t_*\)，两支同时严格低于 \(2/3\)。
等号时返回旧 critical cutoff，没有这项额外 whole-count margin。

| 路线 | 理想二矩指数 \(e_d(t_*)\) | 严格允许的全部额外净 \(U\)-指数损失 |
|---|---:|---:|
| quartic \(d=4\) | \(1.093170360089563397\ldots\) | \(\chi<(1-5e)/(96e)=0.010352262232173711\ldots\) |
| quadratic \(d=2\) | \(1.062113573393042265\ldots\) | \(\chi<(1-5e)/(24e)=0.041409048928694843\ldots\) |

共同 critical threshold 是
\[
 \frac23+\delta_*t_*=e_6(t_*)=\frac{5+23e}{48e}
 =1.103522622321737108\ldots .                             \tag{4}
\]
表内数值从 (2) 的 exact rational functions 和 451 的隔离区间得到；
显示小数不是新分析证书。quartic 理想情形重选 \(t_4\) 后的 count
收益 \(0.002993619561729985\ldots\) 与 464 相符，严格小于单支
\(0.010352\ldots\)。理想 quadratic 同一反事实模型给
\(t_2=1.28444973289094\ldots,\ R_2=0.643109080852596\ldots\)，
也不是新的 \(\sigma\)。

进一步，若新 raw scale-sup 合同仅为
\(H^{1+\rho}(HD)^\varepsilon\)，\(H\ge D^{1+c}\)，则
同一个 order-\(d\) amplification 给
\(e_{\rm net}(t)=e_d(t)+\rho t\)（任意小 \(c,\varepsilon\) 已预先留余量）。
这个模型的相应严格局部门槛为
\[
 \rho<\frac{(\alpha_6-\alpha_d)(t_*-1)}{t_*}
 =\begin{cases}
 (1-5e)/(12(1+3e))=0.009208336822116889\ldots,&d=4,\\
 (1-5e)/(3(1+3e))=0.036833347288467556\ldots,&d=2.
 \end{cases}                                             \tag{5}
\]
这说明该 critical 点上的条件收益不一定要求 raw 指数严格等于 1；
但目前通用 Gaussian LS 的正幂费用远超过这一容忍度。
式 (2)/(5) 只支付这个局部 bottleneck，不单独支付全 \((\delta,x)\)
范围、所有 bins、Euler、principal、outer 与全族 continuation。

## 6. 为什么角色阶数不能直接替换源中的宽度常数

源 9254 的 marked widths 为
\(r+2z\le m-c_1,\ 2r+8z\le3m-c_2\)，源 12561 的 plain width 为
\(n_1+n_2+6\kappa z\le M\)。它们来自整套 reflection 与 induction；
不是由 field degree 或角色阶数单独决定。

若某个全新 proof 真正证明 plain coefficient \(v\kappa\)，则形式上
\[
 z_P=\frac{1-2m}{v\kappa},\qquad c_v=\frac2{v\kappa}
\]
会改变 short crossing 的 \(D,P,s\)。464 与上节只校准原 \(v=6\)，
没有假装 \(v=4\) 或 \(2\) 已证明。源 12365–12366 与 15251 的实际
inverse rows 是 sixth-power-free；不能直接把它们当成 fourth-或
square-power-free rows，沿新乘子映射免费除以 \(P\)。
新 source 必须重新提供相应 physical row support/分解与 masks。

在理想 \(d=2\) 模型中 \(\alpha_2=1/2<3/4\)，全域
\(\delta\ge1/2\) 的 long-slope/endpoint 要另行处理，不能在
\(J=(\alpha_2-\delta)D+\delta P\) 不受保证的区域照搬旧 crossing。
原 \(\kappa_{\rm act}-\kappa_*=2\Delta\) 的反馈也必须随新 whole-family
合同支付；当前 critical 小数不提供这个合同。

## 7. 新有限脚本的方法与证据边界

已只读审查
[新脚本](../../scripts/hybrid_field_decision_exact_audit.py)，canonical SHA256
36da2a5b99a8d7864d4c285d4fdfd05ff5fe92efe822bf1c537308ca21ff105b，
raw 6481 bytes，157 行。它先只读检查既有 checkpoint，随后以 Fraction
refine 三次根的已给有理区间，核有限预算、primary/mod13 角色例子，
以及 \(d=2,4,\ldots,100\) 的 50 个 single-shift 模型。

方法与证据范围相容：midpoint Decimal 只用于显示，general minimum
theta order 由正文 gcd 证明，不由这 50 个模型认证。脚本不验证
Gaussian raw、任意目标 completed reflection、marked/plain、无穷
优化或新无零区域。输出由根节点生成并绑定本最终审查，因此本审查
不反向写入输出 hash 造成绑定循环。

最终脚本仅在第 134–136 行把返回对象的五个 tuple 字段转换为 list，
使内存结果与 JSON 数组 round-trip 后一致。独立把这三行还原后，
旧 canonical SHA256 恰为
030647f7652f562bdbe11b286393bab04e47c0ba26eb173eb7ba1f0185611811，
且差恰为 30 bytes；故只修复序列化类型一致性，未改数学计算或 464。

本次独立 finite 模 13/primary 算术与高精度方向复算通过；正文所有
本地链接已核闭合。464 可以在其已写范围内验收；严格净损失门槛
(2) 的适用前件及没有 \(\sigma\) conversion 已明确。
